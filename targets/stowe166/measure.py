"""Share of cipher signs read, from reading.txt: letters a-z = read signs, {..} = person code signs, <..> = unread.

    PYTHONUTF8=1 python measure.py
"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
T = O = C = 0
for line in open(os.path.join(HERE, 'reading.txt'), encoding='utf-8'):
    if line.startswith('#') or '|' not in line:
        continue
    name, txt = [x.strip() for x in line.split('|', 1)]
    codes = len(re.findall(r'\{[^}]*\}', txt))
    unread = sum(len(re.sub(r'\s', '', m)) for m in re.findall(r'<([^>]*)>', txt))
    letters = len(re.sub(r'[^a-z]', '', re.sub(r'\{[^}]*\}|<[^>]*>', '', txt.lower())))
    t = letters + codes + unread
    print(f'{name}: {t} signs, {letters} read, {codes} code, {unread} unread')
    T += t; O += letters; C += codes
print(f'all: {O}/{T} signs read = {100*O/T:.1f}%; person code signs {C}; excluding them {O}/{T-C} = {100*O/(T-C):.1f}%')
