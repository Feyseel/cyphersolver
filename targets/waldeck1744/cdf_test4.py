"""Best KS over multiplicative orders p = n * a^-1 mod 1000 (a coprime to 1000), real vs random numberings."""
import collections, random, math
import numpy as np
exec(open('cdf_test.py').read().split("t = [int(x)")[0])
A_ = [a for a in range(1, 1000) if math.gcd(a, 1000) == 1]
inv = {a: pow(a, -1, 1000) for a in A_}
def best(items):
    items = list(items); out = []
    for a in A_:
        ai = inv[a]
        pts = sorted(((k * ai) % 1000, v) for k, v in items)
        xs = np.array([p for p, _ in pts]) / 1000.0; ys = np.cumsum([v for _, v in pts]) / sum(v for _, v in pts)
        out.append((np.max(np.abs(ys - refcdf(xs))), a))
    return min(out)
t = [int(x) for x in open('ct.txt').read().split() if x != '|']
c = collections.Counter(t); b = best(c.items())
rnd = random.Random(3); vals = list(c.values())
null = [best(zip(rnd.sample(range(1, 1000), len(vals)), vals))[0] for _ in range(60)]
print('real best %.3f (a=%d); null best: median %.3f 5%% %.3f' % (b[0], b[1], np.median(null), np.percentile(null, 5)))
