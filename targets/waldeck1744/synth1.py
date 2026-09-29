"""One-part (alphabetical) control: random sorted table over a subset of the inventory, codes 1-999 in order."""
import random, re, sys, collections, json
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
pword = float(sys.argv[2]) if len(sys.argv) > 2 else 0.55
rnd = random.Random(seed)
inv = [l.strip() for l in open('inv_de.txt') if l.strip()]
pt = open('synth_pt_long.txt', encoding='utf8').read().lower()
pt = pt.replace('ä', 'a').replace('ö', 'o').replace('ü', 'u')
words = re.findall('[a-z]+', pt)
units = sorted(set(u for u in inv if len(u) == 1 or rnd.random() < pword))
codes = {}; c = 1
for u in units:
    codes[u] = [c]; c += 1
    if len(u) <= 2 and rnd.random() < 0.12: codes[u].append(c); c += 1
    c += int(rnd.random() < 0.15)
print('table', len(units), 'last code', c - 1, file=sys.stderr)
out = []
for w in words:
    i = 0
    while i < len(w):
        for L in range(min(9, len(w) - i), 0, -1):
            s = w[i:i + L]
            if s in codes and (L == 1 or rnd.random() < 0.9):
                out.append(str(rnd.choice(codes[s]))); i += L; break
cnt = collections.Counter(out)
print(len(out), 'tokens', len(cnt), 'types', sum(v == 1 for v in cnt.values()), 'singletons', cnt.most_common(5), file=sys.stderr)
out = out[:717]
open('synth1_ct.txt', 'w').write(' '.join(out) + '\n')
inv_code = {str(x): u for u, xs in codes.items() for x in xs}
open('synth1_key.tsv', 'w').write('\n'.join('%s\t%s' % (k, inv_code[k]) for k in sorted(set(out), key=int)) + '\n')
