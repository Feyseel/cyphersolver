"""Apply an image-confirmed look-alike split to a token file, using the hand reading to say which occurrence is which
(sysA2/lookalike_check.md: the reading's value matched the shape in ~93-100% of the occurrences checked).
  python applysplit.py REC OUTREC 'y:r=g,y:m=M,4:i=u'     ->  OUTREC.tok
Each rule sign:value=newcode recodes the occurrences of `sign` whose aligned reading value is `value`
(value may be a substring, e.g. '+:sch=Ş')."""
import io, os, re, runpy, sys, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
rec, out, rules = sys.argv[1], sys.argv[2], sys.argv[3]
R = [(a.split(':')[0], a.split(':')[1].split('=')[0], a.split('=')[1]) for a in rules.split(',')]
sys.argv = ['measure2.py', os.path.join(HERE, rec + '.tok'), os.path.join(HERE, '..', rec, 'reading.txt')]
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(os.path.join(HERE, 'measure2.py'))
P = g['P']; data = g['data']; align = g['align']; words_of = g['words_of']
_, T, RD = data[0]
lines = open(os.path.join(HERE, rec + '.tok'), encoding='utf8').read().split('\n')
n = 0
for k, l in enumerate(lines):
    m = re.match(r'(P\d+\.\d\d) ?(.*)', l)
    if not m or m.group(1) not in RD: continue
    no, s = m.groups()
    real = [(w, d) for w, d in words_of(RD[no]) if w]
    al = align(T[no], real, P) if real else None
    if not al: continue
    # positions in s of the signs that toks() keeps
    keep = []; i = 0
    for piece in re.split(r'(\[[^\]]*\]|\|F\||\|K\||\|)', s):
        if piece and not piece.startswith(('[', '|')):
            keep += [i + j for j, c in enumerate(piece) if c not in ' ¿']
        i += len(piece)
    assert len(keep) == len(al), no
    s = list(s)
    for (gg, v, wi), pos in zip(al, keep):
        for sg, val, new in R:
            if gg == sg and v and (v == val or (len(val) > 1 and val in v)):
                s[pos] = new; n += 1; break
    lines[k] = no + ' ' + ''.join(s)
open(os.path.join(HERE, out + '.tok'), 'w', encoding='utf8').write('\n'.join(lines))
print(out, n, 'signs recoded')
