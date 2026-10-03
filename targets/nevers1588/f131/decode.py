"""Check the reading of BnF fr. 3976 f. 131r (4 June 1588) sign by sign against the informant's key.

KEY = targets/r3708/decode.py KEY + ADDED (ff. 62, 131 glosses, 133, 139). Each sign has candidate values, some of two
letters (h, 1s = qu). The checker aligns each run's reading (reading.tsv col 2) with its signs by DP and reports any
letter outside the sign's candidates as NEW. It also decodes each run with the first candidate of every sign
(a blind decode, no reading used) and scores readings with the shared French LM.

    python targets/nevers1588/f131/decode.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'r3708'))
import decode as r3708

KEY = {k: list(v) for k, v in r3708.KEY.items()}
for k, v in r3708.ADDED.items():
    KEY.setdefault(k, [])
    KEY[k] += [c for c in v if c not in KEY[k]]
KEY['h'] = ['qu', 'q']
KEY['1s'] = ['qu', 'c', 'q']
KEY['E'] = KEY.get('E', ['t'])
# values first attested on f. 131 (this check), added to key.md
NEW131 = {'1': ['i'], 'l': ['n'], 'b': ['y'], 'Z': ['a'], 'z': ['a']}

def norm(s):
    return s.replace('v', 'u').replace('j', 'i')

def cands(sign, use_new=True):
    c = list(KEY.get(sign, []))
    if use_new:
        c += [x for x in NEW131.get(sign, []) if x not in c]
    return c

def align(signs, plain):
    """DP: each sign takes one of its candidates; return (pairs, cost) with cost = number of NEW signs."""
    plain = norm(plain)
    INF = 10**9
    n, m = len(signs), len(plain)
    best = [[INF] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0
    for i, s in enumerate(signs):
        for j in range(m + 1):
            if best[i][j] == INF:
                continue
            opts = [(norm(c), 0) for c in cands(s)] or []
            for L in (1, 2):  # a NEW value of 1 letter (or 2, penalised)
                if j + L <= m:
                    opts.append((plain[j:j + L], L))
            for val, pen in opts:
                if plain.startswith(val, j):
                    cost = best[i][j] + pen
                    if cost < best[i + 1][j + len(val)]:
                        best[i + 1][j + len(val)] = cost
                        back[i + 1][j + len(val)] = (j, val, pen)
    if best[n][m] == INF:
        return None, INF
    pairs, j = [], m
    for i in range(n, 0, -1):
        pj, val, pen = back[i][j]
        tag = 'NEW' if pen else ('f131' if val not in [norm(c) for c in cands(signs[i-1], False)] else '')
        pairs.append((signs[i - 1], val, tag))
        j = pj
    return pairs[::-1], best[n][m]

def load():
    ct, rd = {}, {}
    for line in open(os.path.join(HERE, 'ciphertext.txt'), encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        rid, sg = line.rstrip('\n').split('\t')
        ct[rid] = sg.split()
    for line in open(os.path.join(HERE, 'reading.tsv'), encoding='utf8'):
        f = line.rstrip('\n').split('\t')
        rd[f[0]] = f[1:]
    return ct, rd

def main():
    from lang import lm
    model = lm.load('fr-1600-letters')
    ct, rd = load()
    tot = ok = codes = struck = nw = vw = 0
    allsp = []
    import re
    VOCAB = set(re.findall(r"[a-z]+", lm.norm(open(os.path.join(HERE, '..', '..', '..', 'lang', 'corpora', 'fr-henri4.txt'), encoding='utf8').read(), 'early')))
    for rid, signs in ct.items():
        letters = [s for s in signs if s != '#' and not s.startswith('<')]
        codes += sum(1 for s in signs if s.startswith('<'))
        struck += signs.count('#')
        spaced = rd[rid][0].replace('<72>', '').strip()
        plain = spaced.replace(' ', '')
        words = spaced.split()
        nw += len(words); vw += sum(1 for w in words if lm.norm(w, 'early').strip() in VOCAB)
        allsp.append(spaced)
        pairs, cost = align(letters, plain)
        blind = ''.join(cands(s)[0] if cands(s) else '?' for s in letters)
        tot += len(letters)
        ok += len(letters) - cost if pairs else 0
        new = [(s, v) for s, v, t in pairs if t == 'NEW']
        f131 = [(s, v) for s, v, t in pairs if t == 'f131']
        print(f'{rid}: {len(letters):2d} signs  read {plain}  blind {blind}'
              + (f'  NEW {new}' if new else '') + (f'  f131-values {f131}' if f131 else ''))
    txt = lm.norm(' '.join(allsp), 'early')
    print(f'LM fr-1600-letters per char, all runs as read: {model.per_char(txt):.2f}')
    print(f'words of the runs found in the fr-henri4 corpus: {vw}/{nw} = {100*vw/nw:.1f}%')
    print(f'cipher signs {tot} (+{struck} struck, +{codes} code number in a run); read by the key: {ok}/{tot} = {100*ok/tot:.1f}%')

if __name__ == '__main__':
    main()
