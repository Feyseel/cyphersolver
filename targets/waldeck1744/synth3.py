"""Hessian-style control: alphabetical table of letters, syllables and words numbered column-wise
(column c holds numbers = residue order[c] mod 10, step 10), 'a' etc. with two consecutive numbers.
usage: python synth3.py seed nwords nsyl"""
import random, re, sys, collections
sys.path.insert(0, '../..')
from lang import lm
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nw = int(sys.argv[2]) if len(sys.argv) > 2 else 300; ns = int(sys.argv[3]) if len(sys.argv) > 3 else 600
rnd = random.Random(seed)
corp = open('../../lang/corpora/de-dta-1720-1770.txt', encoding='utf8').read()
wc = collections.Counter(lm.norm(corp[:4000000], 'modern').split())
words = [w for w, c in wc.most_common(3 * nw) if 2 <= len(w) <= 9][:nw]
sylc = collections.Counter()
for w, c in wc.most_common(20000):
    for L in (2, 3):
        for i in range(0, len(w) - L + 1): sylc[w[i:i + L]] += c
syls = [s for s, c in sylc.most_common(ns)]
units = sorted(set(words) | set(syls) | set('abcdefghiklmnopqrstuvwxz'))
entries = []
for u in units:
    entries.append(u)
    if len(u) == 1 and u in 'aeinrst': entries.append(u)   # frequent letters twice, as 'a 5, 15'
order = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]
R = (len(entries) + 9) // 10
table = collections.defaultdict(list)
for p, u in enumerate(entries):
    col, row = divmod(p, R)
    table[u].append(row * 10 + order[col])
pt = open('synth_pt_long.txt', encoding='utf8').read().lower().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u')
out = []; plain = []
for w in re.findall('[a-z]+', pt):
    if w in table and len(w) > 1: out.append(rnd.choice(table[w])); plain.append(w); continue
    i = 0
    while i < len(w):
        for L in (3, 2, 1):
            s = w[i:i + L]
            if len(s) == L and s in table and (L == 1 or rnd.random() < 0.9):
                out.append(rnd.choice(table[s])); plain.append(s); i += L; break
        else: i += 1
out = [x if x > 0 else 1000 for x in out][:717]; plain = plain[:717]
c = collections.Counter(out)
print('entries', len(entries), 'rows', R, 'tokens', len(out), 'types', len(c), 'single', sum(v == 1 for v in c.values()), 'top', c.most_common(4),
      'lt100', sum(x < 100 for x in out), 'rep', sum(out[i] == out[i + 1] for i in range(len(out) - 1)), file=sys.stderr)
open('synth3_ct.txt', 'w').write(' '.join(map(str, out)) + '\n')
key = {}
for x, p in zip(out, plain): key[x] = p
open('synth3_key.tsv', 'w').write('\n'.join('%d\t%s' % (x, key[x]) for x in sorted(key)) + '\n')
