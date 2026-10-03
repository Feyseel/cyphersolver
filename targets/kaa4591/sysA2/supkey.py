"""Supervised key from a hand reading (as augurelio1535/work/supkey.py): align the reading back onto the signs with
measure2.py's aligner and count each sign's values; write {sign: {value: share}} (values >= 5% and seen twice).
  python supkey.py REC            -> REC_sup.json   (reads sysA2/REC.tok and ../REC/reading.txt)
The result is a seed for run.py (--seed REC_sup.json --it 0): a re-decode under the key the reading implies.
"""
import io, json, os, runpy, sys, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
rec = sys.argv[1]
sys.argv = ['measure2.py', os.path.join(HERE, rec + '.tok'), os.path.join(HERE, '..', rec, 'reading.txt')]
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(os.path.join(HERE, 'measure2.py'))
P = g['P']; out = {}
for sign, c in P.items():
    n = sum(c.values())
    d = {v: round(k / n, 3) for v, k in c.most_common() if v and k >= 2 and k / n >= 0.05}
    if d: out[sign] = d
json.dump(out, open(os.path.join(HERE, rec + '_sup.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(rec, len(out), 'signs;', ' '.join(f'{s}={"/".join(list(d)[:3])}' for s, d in sorted(out.items(), key=lambda x: -sum(P[x[0]].values()))[:30]))
