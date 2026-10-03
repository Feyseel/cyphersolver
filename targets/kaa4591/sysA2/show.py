"""Show lines of a System A' letter sign by sign, for reading rounds.
  python show.py REC [KEYTAG] [P1.03 P1.04 ...]      (KEYTAG default g: REC_g_key.json / REC_g_dec.txt)
For each line: the signs (sysA2/REC.tok), the machine decrypt, and under each sign its key values
(value:probability, best first) so alternative readings can be tried by hand.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
rec = sys.argv[1]
tag = 'g'; want = sys.argv[2:]
if want and not re.match(r'P\d+\.\d\d$', want[0]): tag = want[0]; want = want[1:]
key = json.load(open(os.path.join(HERE, f'{rec}_{tag}_key.json'), encoding='utf8'))
FIXED = {'ʀ': 'und', 'ꝁ': 'ck', 'ẽ': 'eur'}
dec = {}
for l in open(os.path.join(HERE, f'{rec}_{tag}_dec.txt'), encoding='utf8'):
    m = re.match(r'(P\d+\.\d\d) (.*)', l.rstrip('\n'))
    if m: dec[m.group(1)] = m.group(2)
for l in open(os.path.join(HERE, rec + '.tok'), encoding='utf8'):
    m = re.match(r'(P\d+\.\d\d) ?(.*)', l.rstrip('\n'))
    if not m or (want and m.group(1) not in want): continue
    no, s = m.groups()
    print(f'{no} signs : {s}')
    print(f'{no} decrypt: {dec.get(no, "")}')
    sig = [c for c in re.sub(r'\[[^\]]*\]|\|F\||\|K\||\|', ' ', s) if c != ' ']
    for c in sig:
        v = FIXED.get(c) or ' '.join(f'{k}:{p:.2f}' for k, p in list(key.get(c, {}).items())[:4]) or '(any)'
        print(f'      {c}  {v}')
    print()
