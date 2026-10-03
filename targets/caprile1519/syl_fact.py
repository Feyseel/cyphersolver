# 1519 two-tier cipher: factorised syllabary rebuilt from the 1882 sibling decipherments, then decoding R1128.
# 2 Oct 2026. Model: a column upper/base emits C(upper) + V(base), C in {'', one consonant, ch, gh, gl, gn, qu, ...},
# V in {'', a, e, i, o, u}; a bracket column -/[x] is a code word with its own table (any 1-8 letters).
# Factorising lets a column type never seen in the pairs (a known upper over a known base) get a value.
# Training pairs: R1130 cipher insertions (pairX/t.txt) against the 1882 decipherment 4c (pairX/plain.txt), and
# R1133 (t1133_full.txt) against 7c (crib1519.md). Hard EM: monotone alignment, re-estimate C and V counts.
# Decoding R1128 (t1519.txt): beam over each column's top C+V candidates with it-cinquecento (order 5, no spaces);
# control: the same decode with the upper and base tables permuted at random.
# Run: python syl_fact.py
import os, sys, re, math, collections, random
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, ROOT)
from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))
CONS = [''] + list('bcdfghlmnpqrstvxz') + ['ch', 'gh', 'gl', 'gn', 'qu', 'ss', 'tt', 'll', 'pr', 'tr', 'st', 'sc', 'cr']
VOW = ['', 'a', 'e', 'i', 'o', 'u']

def plain(s):
    s = lm.norm(s, 'early', False)
    return ''.join(c for c in s if c.isalpha())

def cols(line):
    return [c.replace('?', '') for c in line.split()]

def load_pairs():
    pairs = []
    T = {l.split('|')[0].strip(): cols(l.split('|')[2]) for l in open(os.path.join(HERE, 'pairX', 't.txt'), encoding='utf8') if l.startswith('S')}
    P = {l.split()[0]: plain(' '.join(l.split()[1:])) for l in open(os.path.join(HERE, 'pairX', 'plain.txt'), encoding='utf8') if l.startswith('S')}
    for k in T:
        if k in P: pairs.append(('R1130 ' + k, T[k], P[k]))
    crib = open(os.path.join(HERE, 'crib1519.md'), encoding='utf8').read()
    L = plain(crib.split('## 7c')[1].split('## 8c')[0].split('\n', 1)[1])
    T33 = []
    for l in open(os.path.join(HERE, 't1133_full.txt'), encoding='utf8'):
        if l.startswith('R1133 '): T33 += cols(l.split(':', 1)[1])
    pairs.append(('R1133', T33, L))
    return pairs

def split(t):
    if '/' not in t: return '#', '#'
    u, b = t.split('/', 1)
    return u, b

class Model:
    def __init__(self):
        self.C = collections.defaultdict(collections.Counter)   # upper -> cons counts
        self.V = collections.defaultdict(collections.Counter)   # base -> vowel counts
        self.W = collections.defaultdict(collections.Counter)   # bracket -> string counts
    def lc(self, u, c):
        n = sum(self.C[u].values()); return math.log((self.C[u][c] + 0.2) / (n + 0.2 * len(CONS))) if u not in ('#', '-') else (math.log(0.9) if c == '' and u == '-' else math.log(1 / len(CONS)))
    def lv(self, b, v):
        n = sum(self.V[b].values()); return math.log((self.V[b][v] + 0.2) / (n + 0.2 * len(VOW)))
    def emit(self, t, s):
        u, b = split(t)
        if b.startswith('['):
            n = sum(self.W[b].values()); return math.log((self.W[b][s] + 0.05) / (n + 1)) - 1.0 * len(s) * (n == 0)
        best = -1e9; arg = None
        for k in range(len(s) + 1):
            c, v = s[:k], s[k:]
            if c not in CONS or v not in VOW: continue
            sc = self.lc(u, c) + self.lv(b, v)
            if sc > best: best, arg = sc, (c, v)
        return best if arg else -1e9
    def split_best(self, t, s):
        u, b = split(t)
        best = None
        for k in range(len(s) + 1):
            c, v = s[:k], s[k:]
            if c in CONS and v in VOW:
                sc = self.lc(u, c) + self.lv(b, v)
                if best is None or sc > best[0]: best = (sc, c, v)
        return best

def align(T, L, M, gap=-7.0):
    n, m = len(T), len(L); INF = -1e18
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n + 1):
        t = T[i - 1] if i else None
        K = 8 if (t and '[' in t) else 3
        for j in range(m + 1):
            if i == 0 and j == 0: continue
            best, bb = INF, None
            if i:
                for k in range(1, min(K, j) + 1):
                    v = D[i - 1][j - k] + M.emit(t, L[j - k:j])
                    if v > best: best, bb = v, k
                v = D[i - 1][j] + gap
                if v > best: best, bb = v, -1
            if j:
                v = D[i][j - 1] + gap
                if v > best: best, bb = v, -2
            D[i][j], B[i][j] = best, bb
    i, j = n, m; al = []
    while i or j:
        b = B[i][j]
        if b and b > 0: al.append((T[i - 1], L[j - b:j])); i -= 1; j -= b
        elif b == -1: al.append((T[i - 1], None)); i -= 1
        else: al.append((None, L[j - 1])); j -= 1
    return D[n][m], al[::-1]

def train(pairs, it=8):
    M = Model()
    # seed from pairX notes: base m = e, n = o, 7 = none
    for _ in range(5): M.V['m']['e'] += 1; M.V['n']['o'] += 1; M.V['7'][''] += 1
    for k in range(it):
        N = Model(); tot = 0
        for _ in range(5): N.V['m']['e'] += 1; N.V['n']['o'] += 1; N.V['7'][''] += 1
        for name, T, L in pairs:
            sc, al = align(T, L, M); tot += sc
            for t, s in al:
                if not t or not s or '#' in t: continue
                u, b = split(t)
                if b.startswith('['): N.W[b][s] += 1; continue
                r = M.split_best(t, s)
                if r: N.C[u][r[1]] += 1; N.V[b][r[2]] += 1
        M = N
        print('iter', k, round(tot), flush=True)
    return M, al

def candidates(M, t, k=4):
    u, b = split(t)
    if '#' in t: return [('', -3.0)]
    if b.startswith('['):
        w = M.W[b]
        if not w: return [('', -4.0)]
        n = sum(w.values()); return [(s, math.log(c / n)) for s, c in w.most_common(k)]
    out = []
    for c in CONS:
        for v in VOW:
            if c == '' and v == '': continue
            out.append((c + v, M.lc(u, c) + M.lv(b, v)))
    out.sort(key=lambda x: -x[1]); return out[:k]

def beam_decode(T, M, m, width=400):
    A = m.A; k = m.order; idx = m.index
    beams = {(): (0.0, '')}
    for t in T:
        nb = {}
        for ctx, (sc, txt) in beams.items():
            for s, p in candidates(M, t):
                s2 = sc + p; c2 = ctx
                for ch in s:
                    if ch not in idx: continue
                    i = idx[ch]
                    if len(c2) == k - 1:
                        f = 0
                        for x in c2: f = f * A + x
                        s2 += float(m.lp[f * A + i])
                    c2 = (c2 + (i,))[-(k - 1):]
                key = c2
                if key not in nb or nb[key][0] < s2: nb[key] = (s2, txt + (s if '[' not in t else s.upper()) + '|')
        beams = dict(sorted(nb.items(), key=lambda kv: -kv[1][0])[:width])
    return max(beams.values())

def main():
    pairs = load_pairs()
    M, _ = train(pairs)
    print('upper -> consonant (top):')
    for u, c in sorted(M.C.items(), key=lambda x: -sum(x[1].values()))[:25]:
        print(' ', u, dict(c.most_common(3)))
    print('base -> vowel:')
    for b, c in sorted(M.V.items(), key=lambda x: -sum(x[1].values()))[:10]:
        print(' ', b, dict(c.most_common(4)))
    # held-out check on R1130: decode each segment and compare letters with 4c
    m = lm.load('it-cinquecento', spaces=False)
    T28 = []
    for l in open(os.path.join(HERE, 't1519.txt'), encoding='utf8'):
        if l.startswith('R1128 '): T28 += cols(l.split(':', 1)[1])
    known = sum(1 for t in T28 if '[' not in t and split(t)[0] in M.C and split(t)[1] in M.V)
    print('R1128 columns', len(T28), 'with a known upper and a known base', known)
    sc, txt = beam_decode(T28, M, m)
    plain_txt = re.sub(r'[^a-z]', '', txt)
    print('R1128 decode:', txt)
    print('LM per char', round(m.per_char(plain_txt), 3))
    # control: permute upper and base tables
    rnd = random.Random(3); ctl = []
    for r in range(5):
        M2 = Model(); us = list(M.C); vs = list(M.V)
        pu = us[:]; rnd.shuffle(pu); pv = vs[:]; rnd.shuffle(pv)
        for a, b in zip(us, pu): M2.C[a] = M.C[b]
        for a, b in zip(vs, pv): M2.V[a] = M.V[b]
        M2.W = M.W
        s2, t2 = beam_decode(T28, M2, m)
        ctl.append(m.per_char(re.sub(r'[^a-z]', '', t2)))
    print('control (tables permuted, 5 runs) LM per char', round(sum(ctl) / len(ctl), 3))

if __name__ == '__main__':
    main()
