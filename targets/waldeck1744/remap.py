"""Remap column-numbered codes to alphabetical positions: n -> pos(n % 10) * 1000 + n // 10.
usage: python remap.py ORDER in.txt out.txt [key_in.tsv key_out.tsv]   ORDER e.g. 5432109876"""
import sys
order = [int(c) for c in sys.argv[1]]
pos = {r: i for i, r in enumerate(order)}
f = lambda n: pos[n % 10] * 1000 + n // 10 + 1
toks = open(sys.argv[2]).read().split()
open(sys.argv[3], 'w').write(' '.join(t if t == '|' else str(f(int(t))) for t in toks) + '\n')
if len(sys.argv) > 5:
    lines = [l.split('\t') for l in open(sys.argv[4]).read().splitlines() if l]
    open(sys.argv[5], 'w').write('\n'.join('%d\t%s' % (f(int(a)), b) for a, b in lines) + '\n')
