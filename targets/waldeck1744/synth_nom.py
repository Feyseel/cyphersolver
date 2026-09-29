"""Profile of a two-part nomenclator encoding (letters w/ homophones + syllables + words) vs the real text."""
import random, re, sys, collections
sys.path.insert(0, '../..')
from lang import lm
rnd = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
nw = int(sys.argv[2]) if len(sys.argv) > 2 else 300; ns = int(sys.argv[3]) if len(sys.argv) > 3 else 300; hl = int(sys.argv[4]) if len(sys.argv) > 4 else 3
corp = open('../../lang/corpora/de-dta-1720-1770.txt', encoding='utf8').read()
start = rnd.randrange(len(corp) - 20000)
text = lm.norm(corp[start:start + 20000], 'modern').split()
wc = collections.Counter(w for w in lm.norm(corp[:3000000], 'modern').split())
words = [w for w, c in wc.most_common(nw * 2) if len(w) >= 2][:nw]
sylc = collections.Counter()
for w in list(wc)[:20000]:
    for L in (2, 3):
        for i in range(0, len(w) - L + 1): sylc[w[i:i + L]] += wc[w]
syls = [s for s, c in sylc.most_common(ns)]
units = {}
for c in 'abcdefghijklmnopqrstuvwxyz': units[c] = hl
for s in syls: units.setdefault(s, 1)
for w in words: units.setdefault(w, 1)
nums = list(range(1, 1000)); rnd.shuffle(nums); k = 0; table = {}
for u, h in units.items():
    table[u] = nums[k:k + h]; k += h
    if k > 990: break
out = []
for w in text:
    if w in table: out.append(rnd.choice(table[w])); continue
    i = 0
    while i < len(w):
        for L in (3, 2, 1):
            s = w[i:i + L]
            if len(s) == L and s in table: out.append(rnd.choice(table[s])); i += L; break
        else: i += 1
    if len(out) >= 717: break
out = out[:717]
c = collections.Counter(out)
rep = sum(out[i] == out[i + 1] for i in range(len(out) - 1)); xyx = sum(out[i] == out[i + 2] for i in range(len(out) - 2))
print('table %d  types %d singletons %d top %s  repeats %d xyx %d  lt100 tokens %d' % (k, len(c), sum(v == 1 for v in c.values()), c.most_common(3), rep, xyx, sum(x < 100 for x in out)))
