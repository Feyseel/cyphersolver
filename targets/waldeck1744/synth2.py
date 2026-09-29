"""Mixed control: letters with homophones in 1-99 (random), alphabetical syllables+words in 100-999.
usage: python synth2.py seed nwords nsyl"""
import random, re, sys, collections
sys.path.insert(0, '../..')
from lang import lm
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nw = int(sys.argv[2]) if len(sys.argv) > 2 else 250; ns = int(sys.argv[3]) if len(sys.argv) > 3 else 400
rnd = random.Random(seed)
corp = open('../../lang/corpora/de-dta-1720-1770.txt', encoding='utf8').read()
wc = collections.Counter(lm.norm(corp[:4000000], 'modern').split())
words = [w for w, c in wc.most_common(3 * nw) if 2 <= len(w) <= 8][:nw]
sylc = collections.Counter()
for w, c in wc.most_common(20000):
    for L in (2, 3):
        for i in range(0, len(w) - L + 1): sylc[w[i:i + L]] += c
syls = [s for s, c in sylc.most_common(ns)]
units = sorted(set(words) | set(syls))
# one-part numbering 100..999
step = 900 / len(units); table = {}
for k, u in enumerate(units): table[u] = [100 + int(k * step)]
lows = list(range(1, 100)); rnd.shuffle(lows); k = 0
F = dict(zip('abcdefghijklmnopqrstuvwxyz', [6.5,1.9,2.9,5.1,17.0,1.7,3.0,4.8,7.6,0.3,1.2,3.4,2.5,9.8,2.6,0.8,0.1,7.0,7.3,6.2,4.4,0.9,1.9,0.1,0.1,1.1]))
for c in F:
    h = max(1, round(F[c] / 100 * 90)); table[c] = lows[k:k + h]; k += h
pt = open('synth_pt_long.txt', encoding='utf8').read().lower().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u')
out = []; plain = []
for w in re.findall('[a-z]+', pt):
    if w in table and len(w) > 1: out.append(rnd.choice(table[w])); plain.append(w); continue
    i = 0
    while i < len(w):
        for L in (3, 2, 1):
            s = w[i:i + L]
            if len(s) == L and s in table and (L == 1 or rnd.random() < 0.85):
                out.append(rnd.choice(table[s])); plain.append(s); i += L; break
out = out[:717]; plain = plain[:717]
c = collections.Counter(out)
print('units', len(units), 'tokens', len(out), 'types', len(c), 'single', sum(v == 1 for v in c.values()), 'top', c.most_common(4),
      'lt100', sum(x < 100 for x in out), 'rep', sum(out[i] == out[i + 1] for i in range(len(out) - 1)), file=sys.stderr)
open('synth2_ct.txt', 'w').write(' '.join(map(str, out)) + '\n')
key = {}
for x, p in zip(out, plain): key[x] = p
open('synth2_key.tsv', 'w').write('\n'.join('%d\t%s' % (x, key[x]) for x in sorted(key)) + '\n')
open('synth2_plain.txt', 'w').write('.'.join(plain) + '\n')
