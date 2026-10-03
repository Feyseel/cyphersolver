"""List where a sign takes each of its values in a hand reading, for checking look-alike splits on the images.
  python lookalike.py REC SIGN [max per value]
Prints value, line key, the word of the reading, and the sign group around the sign.
Uses measure2.py's aligner (run on the whole reading)."""
import io, os, re, runpy, sys, contextlib
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
rec, sign = sys.argv[1], sys.argv[2]; mx = int(sys.argv[3]) if len(sys.argv) > 3 else 12
sys.argv = ['measure2.py', os.path.join(HERE, rec + '.tok'), os.path.join(HERE, '..', rec, 'reading.txt')]
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(os.path.join(HERE, 'measure2.py'))
P = g['P']; data = g['data']; align = g['align']; words_of = g['words_of']
out = defaultdict(list)
for rf, T, R in data:
    for no, r in R.items():
        real = [(w, d) for w, d in words_of(r) if w]
        al = align(T[no], real, P) if real else None
        if not al: continue
        s = T[no]
        for i, (gg, v, wi) in enumerate(al):
            if gg == sign: out[v].append((no, real[wi][0], s[max(0, i - 4):i] + '[' + gg + ']' + s[i + 1:i + 5], i, len(s)))
for v, L in sorted(out.items(), key=lambda x: -len(x[1])):
    print(f'{sign}={v or "_"}: {len(L)}')
    for no, w, ctx, i, n in L[:mx]: print(f'   {no} {w:14s} {ctx}  (sign {i+1} of {n})')
