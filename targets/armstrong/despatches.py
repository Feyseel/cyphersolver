"""Decode every Armstrong despatch in the THE=972 code that is in hand (Founders Online early-access texts saved in fo/,
checked against the M34 roll 13/14 frames), and measure the share of groups read.

Groups come from the Founders transcription (fo/<id>.html) with the corrections listed in FIX (each checked against
the manuscript frame named there).  Readings come from decode972.py (pencil H, known-plaintext C, pencil-uncertain M,
inferred '?'), extended by additions972.tsv (new groups forced by context in these despatches, with evidence).

Usage: python despatches.py [key ...]      decode the named despatches (default: all), print text + share
       python despatches.py --summary      one line per despatch
       python despatches.py --unread KEY   list the unread groups of a despatch with their neighbours in the table
"""
import re, sys, json, html, os
from collections import Counter
import decode972 as D

# key: (founders id, date, frames, note)
DESPATCHES = {
    'dec1807':  ('99-01-02-2472', '27/29 Dec 1807', 'roll 13/14', ''),
    'feb15':    ('99-01-02-2703', '15 Feb 1808', 'roll 14', ''),
    'feb22':    ('99-01-02-2733', '22 Feb 1808', 'roll 14 frames 0033-0034', ''),
    'mar05':    ('99-01-02-2780', '5/9 Mar 1808', 'roll 14', ''),
    'aug13':    ('99-01-02-3414', '13 Aug 1808', 'roll 14', ''),
    'aug30':    ('99-01-02-3466', '30 Aug 1808', 'roll 14', 'postscript; read in NOTES'),
    'mar26':    ('99-01-02-2871', '26 Mar 1808', 'roll 14', 'one word'),
    'may31':    ('99-01-02-3139', '31 May 1808', 'roll 14', 'one name'),
    'jun06':    ('99-01-02-3164', '6 Jun 1808', 'roll 14', 'one phrase'),
    'oct25':    ('99-01-02-3642', '25 Oct 1808', 'roll 14', 'short runs'),
    'jan1810':  ('tr:jan1810', '20 Jan 1810', 'roll 14 frames 0476-0477', 'to R. Smith; pencil decode'),
    'feb1810a': ('tr:feb1810a', '2 Feb 1810', 'roll 14 frame 0494', 'to R. Smith; pencil decode'),
    'feb1810b': ('tr:feb1810b', '17 Feb 1810', 'roll 14 frame 0495', 'to R. Smith; pencil decode'),
}

# Corrections to the Founders group lists, checked against the frames: key -> list of (index, founders, manuscript, frame)
FIX = {}
if os.path.exists('fix972.json'):
    FIX = json.load(open('fix972.json', encoding='utf-8'))


def load_additions():
    add = {}
    if os.path.exists('additions972.tsv'):
        for line in open('additions972.tsv', encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            n, r, where, ev = (line.rstrip('\n').split('\t') + ['', ''])[:4]
            add[int(n)] = r
    return add


ADD = load_additions()   # readings prefixed '!' override even an H/C value (the old value is kept in NOTES)

# multi-group contexts where a group takes a second value (the clerk's pencil or the word forces it)
CONTEXT = {
    (1078, 368): ['dri', 'ven'],          # pencil 'driven' over 1078.368, roll 14 frame 0024; 22 Feb 'it has driven her'
    (664, 1078, 781): ['pro', 'je', 'ct'],  # 15 Feb 'the pro-je-ct-ed alliance'
    (1415, 1116, 1131): ['ble', 's', 'sin'],  # 15 Feb 'ble-s-sin-g-s', pencil 'blessings'
    (619, 1260, 1484, 808): ['un', 'chari', 't', 'able'],  # 17 Feb 1810 pencil 'uncharitable' (1260 = dou in 22 Feb 1808)
    (1179, 460): ['po', 'licy'],          # 17 Feb 1810 pencil 'Policy'
    (946, 985, 608, 899): ['Gu', 'sta', 'v', 'us'],  # 22 Feb Gustavus (946 is 'on' in the 1806 known plaintext)
}


def body(doc):
    if doc.startswith('tr:'):
        txt = open('transcripts14.txt', encoding='utf-8').read()
        sec = txt.split('== ' + doc[3:] + chr(10), 1)[1].split(chr(10) + '== ', 1)[0]
        return ' '.join(l for l in sec.splitlines() if not l.startswith('#'))
    t = open(f'fo/{doc}.html', encoding='utf-8').read()
    m = re.search(r'<div class="docbody">(.*?)(?:DNA\s*:|<div class="(?:ptdoc|note))', t, re.S)
    s = m.group(1) if m else t
    s = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    s = re.sub(r'\s+', ' ', s)
    i = s.find('Tweet')
    s = s[i + 5:] if i >= 0 else s
    j = s.find('DNA :')
    return s[:j] if j >= 0 else s


def segments(text):
    """Split into ('c', [groups]) runs and ('t', clear) pieces.  A run is >= 2 bare numbers (<= 4 digits, no comma,
    no ordinal suffix) separated only by dots, spaces and a stray clear 's'."""
    toks = re.findall(r'\d+(?:,\d+)*(?:th|st|nd|rd|d)?\.?|[^\s\d]+|\s+', text)
    out, run, clear = [], [], []

    def flush_run():
        nonlocal run, clear
        nums = [t for t in run if t[0] == 'n']
        if len(nums) >= 2:
            if clear:
                out.append(('t', ''.join(clear).strip())); clear = []
            out.append(('c', [t[1] for t in run]))
        else:
            clear.extend(t[2] for t in run)
        run = []

    for tok in toks:
        m = re.fullmatch(r'(\d{1,4})\.?', tok)
        if m and not re.fullmatch(r'1[78]\d\d', m.group(1)) or (m and run):
            run.append(('n', int(m.group(1)), tok))
        elif tok.isspace() or tok in ('.', 's', 's.'):
            if run:
                run.append(('x', tok.strip(' .') if tok.strip(' .') else None, tok))
            else:
                clear.append(tok)
        else:
            flush_run()
            clear.append(tok)
    flush_run()
    if clear:
        out.append(('t', ''.join(clear).strip()))
    # keep only the numbers and clear 's' inside runs
    res = []
    for kind, v in out:
        if kind == 'c':
            res.append(('c', [x for x in v if x is not None]))
        else:
            res.append((kind, v))
    return res


def groups_of(key):
    doc = DESPATCHES[key][0]
    segs = segments(body(doc))
    for fv, nth, ms, note in FIX.get(key, []):
        seen = 0
        done = False
        for k, v in segs:
            if k != 'c' or done:
                continue
            for p, g in enumerate(v):
                if g == fv:
                    seen += 1
                    if seen == nth:
                        v[p] = ms; done = True; break
        assert done, (key, fv, nth)
    return segs


def reading(n):
    b = D.best(n)
    if n in ADD:
        r = ADD[n]
        if r.startswith('!') or b is None or b[1] in 'M?' or r != b[0] and b[1] not in 'HC':
            return r.lstrip('!'), 'A'
    if b is None:
        return None, None
    return b


def render(key, mark=True):
    segs = groups_of(key)
    out, stats = [], Counter()
    for k, v in segs:
        if k == 't':
            out.append(v)
            continue
        words = []
        ctx = {}
        ints = [(p, g) for p, g in enumerate(v) if isinstance(g, int)]
        for q in range(len(ints)):
            for pat, vals in CONTEXT.items():
                if tuple(g for _, g in ints[q:q + len(pat)]) == pat:
                    for t, (p, _) in enumerate(ints[q:q + len(pat)]):
                        ctx[p] = vals[t]
        for p, g in enumerate(v):
            if p in ctx:
                stats['n'] += 1; stats['inferred'] += 1
                words.append(ctx[p] + '*'); continue
            if isinstance(g, str):  # a clear letter written after a group, e.g. 741s
                words.append('+' + g)
                continue
            r, c = reading(g)
            stats['n'] += 1
            if r is None:
                words.append(f'[{g}]')
                stats['unread'] += 1
            else:
                if c in 'HC':
                    stats['known'] += 1
                elif c == 'A':
                    stats['added'] += 1
                elif c == 'M':
                    stats['uncertain'] += 1
                else:
                    stats['inferred'] += 1
                words.append(r + ('' if c in 'HC' else ('?' if c == 'M' else ('+' if c == 'A' else '*'))) if mark else r)
        out.append('«' + ' '.join(words) + '»')
    return '\n'.join(out), stats


def unread(key):
    segs = groups_of(key)
    c = Counter(g for k, v in segs if k == 'c' for g in v if isinstance(g, int) and reading(g)[0] is None)
    ks = sorted(D.tab)
    for g, m in sorted(c.items()):
        lo = [n for n in ks if n < g][-2:]
        hi = [n for n in ks if n > g][:2]
        print(g, 'x%d' % m, ' | ', ' '.join(f'{n}={D.best(n)[0]}' for n in lo), '<>', ' '.join(f'{n}={D.best(n)[0]}' for n in hi))


def summary_line(key, st):
    n = st['n'] or 1
    read = st['known'] + st['uncertain'] + st['inferred'] + st['added']
    return (f"{key:8s} {DESPATCHES[key][1]:16s} groups {st['n']:4d}  known(H/C) {st['known']:4d} {100*st['known']/n:5.1f}%"
            f"  new(+) {st['added']:3d}  read incl. M/inferred/new {read:4d} {100*read/n:5.1f}%  unread {st['unread']:3d}")


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--unread':
        unread(args[1]); sys.exit()
    keys = [a for a in args if not a.startswith('--')] or list(DESPATCHES)
    for key in keys:
        txt, st = render(key)
        if '--summary' not in args:
            print(f'== {key} {DESPATCHES[key][1]} (Founders {DESPATCHES[key][0]}) ==')
            print(txt)
        print(summary_line(key, st))
        print()
