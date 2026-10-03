"""Share of cipher signs read as sense, from reading.txt (see its header). Checks the marks against dec2.py."""
import os, re, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
dec = {}
for page in (1, 2, 3):
    out = subprocess.run([sys.executable, os.path.join(HERE, 'dec2.py'), os.path.join(HERE, f'hand_p{page}.txt')],
                         capture_output=True, text=True, encoding='utf-8').stdout
    for line in out.splitlines():
        lab, txt = line.split(' ', 1) if ' ' in line else (line, '')
        dec[f'p{page}.{lab}'] = txt.strip()
tot = {}; ok = {}; bad = []
for line in open(os.path.join(HERE, 'reading.txt'), encoding='utf-8'):
    if line.startswith('#') or '|' not in line:
        continue
    lab, marked, _ = [x.strip() for x in line.split('|')]
    flat = re.sub(r'[\s<>]', '', marked)
    if flat != dec.get(lab, '').replace('[flap]', ''):
        bad.append((lab, flat, dec.get(lab)))
    unread = sum(len(re.sub(r'\s', '', m)) for m in re.findall(r'<([^>]*)>', marked))
    pg = lab.split('.')[0]
    tot[pg] = tot.get(pg, 0) + len(flat); ok[pg] = ok.get(pg, 0) + len(flat) - unread
for b in bad:
    print('MISMATCH', b)
T = sum(tot.values()); O = sum(ok.values())
for pg in sorted(tot):
    print(f'{pg}: {ok[pg]}/{tot[pg]} signs read as sense = {100*ok[pg]/tot[pg]:.1f}%')
print(f'all: {O}/{T} = {100*O/T:.1f}%')
