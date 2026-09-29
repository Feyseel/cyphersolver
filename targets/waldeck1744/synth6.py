"""R4680-style two-part control: letters with h homophones, nw words + ns syllables with one number each (1-999)."""
import random, re, sys, collections
sys.path.insert(0, '../..')
from lang import lm
seed = int(sys.argv[1]); h = int(sys.argv[2]); nw = int(sys.argv[3]); ns = int(sys.argv[4])
rnd = random.Random(seed)
corp = open('../../lang/corpora/de-dta-1720-1770.txt', encoding='utf8').read()
wc = collections.Counter(lm.norm(corp[:4000000], 'modern').split())
words = [w for w, c in wc.most_common(3 * nw) if 2 <= len(w) <= 10][:nw]
sylc = collections.Counter()
for w, c in wc.most_common(20000):
    for L in (2, 3):
        for i in range(len(w) - L + 1): sylc[w[i:i + L]] += c
syls = [s for s, c in sylc.most_common(ns + 200) if s not in words][:ns]
nums = list(range(1, 1000)); rnd.shuffle(nums); k = 0; table = {}
for c in 'abcdefghiklmnopqrstuvwxz': table[c] = nums[k:k + h]; k += h
for u in words + syls: table[u] = [nums[k]]; k += 1
start = rnd.randrange(len(corp) - 30000)
txt = lm.norm(corp[start:start + 30000], 'modern').split()
out = []
for w in txt:
    if w in table and len(w) > 1: out.append(rnd.choice(table[w][:1])); continue
    i = 0
    while i < len(w):
        for L in (3, 2, 1):
            s = w[i:i + L]
            if len(s) == L and s in table: out.append(rnd.choice(table[s])); i += L; break
        else: i += 1
    if len(out) >= 717: break
out = out[:717]; c = collections.Counter(out)
f3 = [x for x in c if c[x] >= 3]
print('table %d types %d single %d top %s  >=3: types %d tokens %d  rep %d lt100 %d' % (k, len(c), sum(v == 1 for v in c.values()), c.most_common(3), len(f3), sum(c[x] for x in f3), sum(out[i] == out[i+1] for i in range(len(out)-1)), sum(x < 100 for x in out)))
