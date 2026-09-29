"""KS of token mass along codes >= 100 (natural order) vs German alphabet usage; null = random numbering."""
import sys, collections, random
import numpy as np
exec(open('cdf_test.py').read().split("t = [int(x)")[0])      # reuse the reference CDF (ref, refcdf)
t = [int(x) for x in open(sys.argv[1] if len(sys.argv) > 1 else 'ct.txt').read().split() if x != '|']
t = [x for x in t if x >= 100]
c = collections.Counter(t)
def ks_items(items, lo, hi):
    pts = sorted(items); xs = (np.array([k for k, _ in pts]) - lo) / (hi - lo); ys = np.cumsum([v for _, v in pts]) / sum(v for _, v in pts)
    return np.max(np.abs(ys - refcdf(xs)))
print('codes>=100 natural KS %.3f  (tokens %d, types %d)' % (ks_items(c.items(), 100, 1000), len(t), len(c)))
rnd = random.Random(1); vals = list(c.values()); null = []
for _ in range(500):
    keys = rnd.sample(range(100, 1000), len(vals)); null.append(ks_items(zip(keys, vals), 100, 1000))
print('random numbering: median %.3f  5%% %.3f  1%% %.3f' % (np.median(null), np.percentile(null, 5), np.percentile(null, 1)))
