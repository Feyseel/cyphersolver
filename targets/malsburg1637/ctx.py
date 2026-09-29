"""ctx.py files... : show each non-digit sign with 8 decoded chars either side."""
import re, sys, collections
from dec import K, dec_line
import io, contextlib
text = ''
for f in sys.argv[1:]:
    for line in open(f, encoding='utf8'):
        if line.startswith('#'):
            if 'letter-cipher' in line: break
            continue
        text += dec_line(line.strip())
C = collections.defaultdict(list)
for m in re.finditer(r'\[([^\]]+)\]', text):
    s = m.group(1)
    a = re.sub(r'\[[^\]]+\]', '*', text[max(0, m.start() - 20):m.start()])[-9:]
    b = re.sub(r'\[[^\]]+\]', '*', text[m.end():m.end() + 20])[:9]
    C[s.rstrip("'?_#")].append(f'{a}|{b}')
for s in sorted(C, key=lambda s: -len(C[s])):
    print(f'{s:5} {len(C[s]):3}  ' + '  '.join(C[s][:14]))
