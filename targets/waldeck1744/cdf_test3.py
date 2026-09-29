"""Best KS over the 20 cyclic column orders (ascending/descending, any start), real vs random numberings."""
import sys, collections, random
import numpy as np
exec(open('cdf_test.py').read().split("t = [int(x)")[0])
perms = []
for s in range(10):
    perms.append([(s + i) % 10 for i in range(10)]); perms.append([(s - i) % 10 for i in range(10)])
def best(items, lo):
    items = list(items)
    out = []
    for pm in perms:
        pos = {r: i for i, r in enumerate(pm)}
        pts = sorted((pos[k % 10] * 100 + k // 10, v) for k, v in items)
        xs = np.array([p for p, _ in pts]) / 1000.0; ys = np.cumsum([v for _, v in pts]) / sum(v for _, v in pts)
        out.append((np.max(np.abs(ys - refcdf(xs))), ''.join(map(str, pm))))
    return min(out)
for lo in (1, 100):
    t = [int(x) for x in open('ct.txt').read().split() if x != '|' and int(x) >= lo]
    c = collections.Counter(t)
    b = best(c.items(), lo)
    rnd = random.Random(2); vals = list(c.values())
    null = [best(zip(rnd.sample(range(lo, 1000), len(vals)), vals), lo)[0] for _ in range(300)]
    print('codes>=%d: real best %.3f (%s); null best: median %.3f 5%% %.3f 1%% %.3f' % (lo, b[0], b[1], np.median(null), np.percentile(null, 5), np.percentile(null, 1)))
