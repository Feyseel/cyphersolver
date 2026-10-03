"""Word count of a reading (the R9407 pass-2 convention, augurelio1535 NOTES): every plaintext word is a token;
{?} is an unread word; [F.G.] and [K] code signs and the writer's clear text in [..] are not counted; a word with
a supplied letter (herr[n]) counts as read but is tallied separately.
  python count.py reading.txt [...]
"""
import re, sys
for f in sys.argv[1:]:
    tot = unread = emend = 0; pages = {}
    for l in open(f, encoding='utf8'):
        m = re.match(r'\s*(P\d+)\.\d\d\s+(.*)', l)
        if not m: continue
        s = re.sub(r'(^|\s)\[[^\]]*\](?=\s|$)', ' ', ' ' + m.group(2) + ' ')    # clear text, [F.G.], [K]
        for w in s.split():
            if not re.search(r'[A-Za-zäöüß?]', w): continue
            tot += 1; pg = pages.setdefault(m.group(1), [0, 0])
            pg[0] += 1
            if '{?}' in w or w.startswith('{'): unread += 1; pg[1] += 1
            elif '[' in w: emend += 1
    print(f'{f}: {tot - unread}/{tot} words read = {(tot - unread) / max(tot, 1):.3f} ({unread} unread, {emend} with a supplied letter)')
    for p, (t, u) in pages.items(): print(f'   {p}: {t - u}/{t} = {(t - u) / max(t, 1):.3f}')
