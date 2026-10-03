"""Share of cipher signs read as sense, from reading.txt (see its header). Checks the marks against dec2.py.

<...> = not read as sense; {...} = code signs and proper names (counted apart). [flap] signs are not counted.
    PYTHONUTF8=1 python measure.py
"""
import os, re, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
dec = {}
for page in (1, 2, 3):
    out = subprocess.run([sys.executable, os.path.join(HERE, 'dec2.py'), os.path.join(HERE, f'hand_p{page}.txt')],
                         capture_output=True, text=True, encoding='utf-8').stdout
    for line in out.splitlines():
        lab, txt = line.split(' ', 1) if ' ' in line else (line, '')
        dec[f'p{page}.{lab}'] = txt.strip()
tot = {}; ok = {}; cod = {}; bad = []
for line in open(os.path.join(HERE, 'reading.txt'), encoding='utf-8'):
    if line.startswith('#') or '|' not in line:
        continue
    lab, marked, _ = [x.strip() for x in line.split('|')]
    flat = re.sub(r'[\s<>{}]', '', marked)
    if flat != dec.get(lab, '').replace('[flap]', ''):
        bad.append((lab, flat, dec.get(lab)))
    unread = sum(len(re.sub(r'\s', '', m)) for m in re.findall(r'<([^>]*)>', marked))
    code = sum(len(re.sub(r'\s', '', m)) for m in re.findall(r'\{([^}]*)\}', marked))
    pg = lab.split('.')[0]
    tot[pg] = tot.get(pg, 0) + len(flat)
    ok[pg] = ok.get(pg, 0) + len(flat) - unread - code
    cod[pg] = cod.get(pg, 0) + code
for b in bad:
    print('MISMATCH', b)


def show(name, pages):
    t = sum(tot[p] for p in pages); o = sum(ok[p] for p in pages); c = sum(cod[p] for p in pages)
    print(f'{name}: {o}/{t} signs read as sense = {100*o/t:.1f}%; code/name signs {c}; '
          f'excluding them {o}/{t-c} = {100*o/(t-c):.1f}%')


for pg in sorted(tot):
    show(pg, [pg])
show('letter (p3+p1)', ['p3', 'p1'])
