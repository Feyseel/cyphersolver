"""Build docs/reveal/hesse1824.json from decrypt.py (whole message)."""
import json, re
from decrypt import WRITTEN, SLIPS, C, P, KEY, SHIFT
slip = {a: b for a, b, _ in SLIPS}
toks, k = [], 0
for li, line in enumerate(WRITTEN.strip().split('\n')):
    if li: toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
    for part in re.findall(r'[a-z0-9]+|[^a-z0-9]+', line):
        if not part[0].isalnum():
            toks.append({'g': '', 'p': ' ' if part.strip() in ('.', '') else part.replace('.', ' '), 'cls': 'plain'}); continue
        want = slip.get(part, part)
        wi = 0
        for ch in want:
            i = C.index(ch) - SHIFT[KEY[k % 6]]; k += 1
            p = P[i]
            if len(want) > len(part) and (wi >= len(part) or part[wi] != ch) and part[wi:] == want[len(want) - len(part) + wi:]:
                toks.append({'g': '·', 'p': p, 'cls': 'unc'}); continue   # sign omitted by the copyist
            g = part[wi]; wi += 1
            t = {'g': g, 'p': p}
            if g != ch: t['cls'] = 'unc'
            toks.append(t)
d = {'slug': 'hesse1824', 'anchor': 'the-reading',
     'title': 'HStAM 9 a Nr. 259 f. 249: the whole message',
     'caption': 'All six lines of the cipher, deciphered with the key bcdefg repeated over the signs (b..g = +2..+7, the columns running on past z into 1 2 3 4).',
     'unit': 'letters',
     'key_note': 'Signs marked uncertain are copy slips: the sign as written decrypts wrongly and the reading shows the intended letter; a raised dot is the one sign the copyist left out (wo nicht).',
     'tokens': toks}
json.dump(d, open('../../docs/reveal/hesse1824.json', 'w', encoding='utf8'), indent=1, ensure_ascii=False)
print(''.join(t['p'] for t in toks)); print(sum(1 for t in toks if t.get('cls') == 'unc'), 'unc')
