"""HStAM 9 a Nr. 259 f. 249 (HCPortal 513), 1824: Vigenere table, key 'bcdefg' repeated.

Plain alphabet: 25 letters (no j). Key b..g encipher by +2..+7 along the cipher sequence
a..z (no j) followed by the signs 1 2 3 4 ..., i.e. the columns do not wrap: w under g = 21+7 = 28 = '4'.
The key runs continuously over every sign (letters and digits), word dots do not use a key letter.
"""
import re, sys
C = 'abcdefghiklmnopqrstuvwxyz123456789'
P = 'abcdefghiklmnopqrstuvwxyz'
KEY = 'bcdefg'
SHIFT = {k: 2 + i for i, k in enumerate(KEY)}

# as written on f. 249 (diplomatic; g/q and u/w/n as they look)
WRITTEN = open('ct.txt').read().lower()
# the slips, corrected: (written, intended, why)
SLIPS = [
    ('huslu', 'hnslu', 'u for n'),
    ('zsskkw', 'zsspkkw', 'p omitted (wo nicht); the only key-phase slip'),
    ('ntldkt', 'ntdlkt', 'd and l transposed'),
    ('zlogz', '2logq', 'z for 2 (sign after z), z for q'),
    ('1uw', '1uu', 'w for u'),
    ('ixkl', 'cxkl', 'i for c'),
    ('kqqrix', 'kqgvix', 'q for g, r for v'),
    ('vscqu', 'vscqw', 'u for w'),
    ('ktroqq', 'ktrogq', 'q for g'),
]

def decrypt(text):
    out, k = [], 0
    for ch in text:
        if ch in C:
            i = C.index(ch) - SHIFT[KEY[k % 6]]
            out.append(P[i] if 0 <= i < 25 else '?')
            k += 1
        else:
            out.append(ch)
    return ''.join(out)

if __name__ == '__main__':
    fixed = WRITTEN
    for a, b, _ in SLIPS:
        assert a in fixed, a
        fixed = fixed.replace(a, b, 1)
    print('as written:\n' + decrypt(WRITTEN))
    print('with the slips corrected:\n' + decrypt(fixed))
    n = len(re.findall(r'[a-z0-9]', WRITTEN))
    print(f'signs written: {n}; slips: {len(SLIPS)} words')
