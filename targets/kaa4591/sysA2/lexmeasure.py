"""Lexical measure of a System A' decrypt: share of tokens read as German words.

Each line's decrypt (clear text in [..] and code tags [F.G.]/[K] removed) is normalised ('early': j->i, v->u),
the lines of a page are joined, and the run is segmented by Viterbi into lexicon words and unknown stretches.
Lexicon: DTA 1470-1610 word counts (r9407/de1500_words.json) plus the words of the hand readings of this
correspondence (augurelio1535/pass2/reading.txt, r9416, sysA/r9410_reading.txt) and ai/ei, d/t, b/p spelling
variants of frequent words. A word of 6+ letters counts if its corpus count >= 3; 2-letter words only from the
frequent function words; 3-letter words need count >= 300, 4-letter >= 50, 5-letter >= 10
(the DTA list is full of fragments and Latin), Latin function words are excluded. A token is a lexicon word (read) or an unknown stretch, counted as ceil(len/5) unread
tokens. Prints per page and total: read tokens / all tokens, and the share of letters inside read words.
  python lexmeasure.py decrypt.txt [decrypt2.txt ...]      (V=1 lists the unread stretches)
"""
import json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
W = json.load(open(os.path.join(HERE, '..', 'r9407', 'de1500_words.json'), encoding='utf8'))

def norm(s):
    s = s.lower().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ß', 'ss')
    s = s.replace('j', 'i').replace('v', 'u')
    return re.sub(r'[^a-z]', '', s)

MINC = {2: 3000, 3: 300, 4: 50, 5: 10}
LATIN = set('non est aut sed qui quae quod cum per pro sunt etiam enim atque ita tamen esse eius vel nec ab ex'.split())
LEX = {w: c for w, c in W.items() if len(w) >= 2 and c >= MINC.get(len(w), 3) and w not in LATIN}
for f in ['../../augurelio1535/pass2/reading.txt', '../r9416/reading_p3_11-16.txt', '../sysA/r9410_reading.txt']:
    p = os.path.join(HERE, f)
    if not os.path.exists(p): continue
    for l in open(p, encoding='utf8'):
        if l.lstrip().startswith('#'): continue
        if re.match(r'\s*\d\d\s+[SD]\s', l): continue
        l = re.sub(r'\{[^}]*\}|\([^)]*\?\)|…|\[[^\]]*\]', ' ', l)
        for w in l.split():
            if '?' in w: continue
            w = norm(w)
            if len(w) >= 3: LEX[w] = max(LEX.get(w, 0), 20)
for l in open(os.path.join(HERE, 'vocab.txt'), encoding='utf8'):
    if not l.startswith('#'):
        for x in l.split():
            x, _, c = x.partition(':'); LEX[x] = max(LEX.get(x, 0), int(c or 50))
for w, c in list(LEX.items()):
    if c < 200 or len(w) < 4: continue
    for a, b in (('ei', 'ai'), ('t', 'd'), ('d', 't'), ('b', 'p'), ('p', 'b'), ('ue', 'u'), ('u', 'ue')):
        if a in w:
            v = w.replace(a, b)
            if v not in LEX: LEX[v] = 3
N = sum(LEX.values())
COST = {w: -math.log(c / N) for w, c in LEX.items()}
MAXL = 18
UNK = float(os.environ.get('UNK', 9.0))           # cost per unknown letter

def segment(s):
    n = len(s); best = [0.0] + [1e18] * n; back = [None] * (n + 1)
    for i in range(n):
        if best[i] >= 1e18: continue
        v = best[i] + UNK
        if v < best[i + 1]: best[i + 1] = v; back[i + 1] = (i, None)
        for j in range(i + 2, min(n, i + MAXL) + 1):
            c = COST.get(s[i:j])
            if c is not None and best[i] + c < best[j]: best[j] = best[i] + c; back[j] = (i, s[i:j])
    out = []; j = n
    while j > 0:
        i, w = back[j]; out.append((w, s[i:j])); j = i
    out = out[::-1]
    merged = []
    for w, t in out:
        if w is None and merged and merged[-1][0] is None: merged[-1] = (None, merged[-1][1] + t)
        else: merged.append((w, t))
    return merged

def pages(path):
    cur, name, res = [], None, []
    for l in open(path, encoding='utf8'):
        if l.startswith('=='):
            if cur: res.append((name, cur))
            name, cur = l.strip(), []
            continue
        m = re.match(r'\s*(?:P\d+\.)?(\d\d)\s+(.*)', l)
        if not m: continue
        cur.append(norm(re.sub(r'\[[^\]]*\]', ' ', m.group(2))))
    if cur: res.append((name, cur))
    return res

def measure(path, verbose=False):
    R = T = RL = TL = 0; rows = []; unk = []
    for name, lines in pages(path):
        s = ''.join(lines)
        seg = segment(s)
        r = sum(1 for w, _ in seg if w); u = sum(math.ceil(len(t) / 5) for w, t in seg if not w)
        rl = sum(len(t) for w, t in seg if w)
        rows.append((name, r, r + u, rl, len(s))); R += r; T += r + u; RL += rl; TL += len(s)
        unk += [t for w, t in seg if not w]
    return R, T, RL, TL, rows, unk

if __name__ == '__main__':
    for f in sys.argv[1:]:
        R, T, RL, TL, rows, unk = measure(f)
        print(f'{f}: tokens {R}/{T} = {R / max(T, 1):.3f}; letters in words {RL}/{TL} = {RL / max(TL, 1):.3f}')
        if os.environ.get('PAGES'):
            for name, r, t, rl, tl in rows: print(f'   {name}: {r}/{t} = {r / max(t, 1):.3f}')
        if os.environ.get('V'): print('   unread:', ' '.join(unk))
