"""Compare the token-mass CDF along the code order with the CDF of German unit usage along the alphabet."""
import sys, collections, itertools, random, re
import numpy as np
sys.path.insert(0, '../..')
from lang import lm
inv = [l.strip() for l in open('inv_mix.txt') if l.strip()]
invs = set(inv)
corp = open('../../lang/corpora/de-dta-1720-1770.txt', encoding='utf8').read()
txt = lm.norm(corp[12000000:13500000], 'modern').split()
use = collections.Counter()
for w in txt:
    if w in invs and len(w) > 1: use[w] += 1; continue
    i = 0
    while i < len(w):
        for L in (3, 2, 1):
            s = w[i:i + L]
            if len(s) == L and s in invs: use[s] += 1; i += L; break
        else: i += 1
tot = sum(use.values())
ref = np.cumsum([use[u] for u in inv]) / tot            # CDF over table position (inventory order)
refx = np.arange(1, len(inv) + 1) / len(inv)
def refcdf(x): return np.interp(x, refx, ref)
t = [int(x) for x in open(sys.argv[1] if len(sys.argv) > 1 else 'ct.txt').read().split() if x != '|']
c = collections.Counter(t)
def ks(posfun, span):
    pts = sorted((posfun(k), c[k]) for k in c)
    xs = np.array([p for p, _ in pts]) / span; ys = np.cumsum([v for _, v in pts]) / len(t)
    return np.max(np.abs(ys - refcdf(xs)))
print('natural order KS %.3f' % ks(lambda k: k, 1000))
res = []
for perm in itertools.permutations(range(10)):
    pos = {r: i for i, r in enumerate(perm)}
    res.append((ks(lambda k: pos[k % 10] * 100 + k // 10, 1000), perm))
res.sort()
print('best column orders:', [('%.3f' % s, ''.join(map(str, p))) for s, p in res[:8]])
print('hessian 5432109876: %.3f' % [s for s, p in res if p == (5,4,3,2,1,0,9,8,7,6)][0])
print('ascending 0123456789: %.3f' % [s for s, p in res if p == tuple(range(10))][0])
# null: random two-part numbering of the same token counts
rnd = random.Random(1); vals = list(c.values()); null = []
for _ in range(200):
    keys = rnd.sample(range(1, 1000), len(vals)); cc = dict(zip(keys, vals))
    pts = sorted(cc.items()); xs = np.array([k for k, _ in pts]) / 1000; ys = np.cumsum([v for _, v in pts]) / len(t)
    null.append(np.max(np.abs(ys - refcdf(xs))))
print('random numbering KS: median %.3f, 5%% %.3f' % (np.median(null), np.percentile(null, 5)))
