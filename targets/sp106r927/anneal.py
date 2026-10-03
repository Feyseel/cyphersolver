"""Joint re-annealing of the homophone assignments over all three hand transcriptions (3 Oct 2026).

Each sign (shape+inner mark+dots) gets one letter; polyphones in key.json are dropped to their first value as a start.
Hill-climbing with restarts on fr-1600-letters (order 5, no spaces) over hand_p1+p2+p3. Prints the signs whose value
changed from key.json and the score of both keys. It does not write key.json.
"""
import os, sys, json, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
import numpy as np
from dec2 import tokens, KEY, HERE
M = lm.load('fr-1600-letters', spaces=False)
lines = []
for p in ('hand_p3.txt', 'hand_p1.txt', 'hand_p2.txt'):
    for lab, toks in tokens(os.path.join(HERE, p)):
        lines.append([t.rstrip('?') for t in toks if not t.startswith(('[', '<'))])
signs = sorted({t for l in lines for t in l})
idx = {s: i for i, s in enumerate(signs)}
L = [np.array([idx[t] for t in l]) for l in lines]
alpha = 'abcdefghilmnopqrstuxyz'
def score(asg):
    return sum(M.per_char(''.join(alpha[asg[i]] for i in l)) * len(l) for l in L) / sum(len(l) for l in L)
start = np.array([alpha.index(KEY[s].split('/')[0]) if s in KEY and KEY[s].split('/')[0] in alpha else 0 for s in signs])
base = score(start); print('key.json (first values):', round(base, 4))
best = start.copy(); bs = base
random.seed(1)
for rnd in range(3):
    cur = best.copy(); cs = bs
    improved = True
    while improved:
        improved = False
        for i in random.sample(range(len(signs)), len(signs)):
            for a in range(len(alpha)):
                if a == cur[i]: continue
                old = cur[i]; cur[i] = a; s = score(cur)
                if s > cs + 1e-6: cs = s; improved = True
                else: cur[i] = old
    if cs > bs: best, bs = cur.copy(), cs
print('annealed:', round(bs, 4))
for s, i in idx.items():
    if best[i] != start[i]:
        n = sum((l == i).sum() for l in L)
        print(f'{s}: {alpha[start[i]]} -> {alpha[best[i]]}  ({n} occurrences)')
