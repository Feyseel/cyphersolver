"""measure.py files... : how much of the cipher reads as German words under key.txt (and codes.txt).

Each cipher run (the text between clear words) is decoded and segmented into words by dynamic programming over a
vocabulary: every word form seen at least twice in the lang DTA corpora (1470-1610, 1630-1670), plus extra.txt
(names, loanwords and spellings of these letters).  A cipher token counts as read when every letter it produces lies
inside a vocabulary word of the best segmentation.  Three-digit codes and signs count as read only when codes.txt or
key.txt gives them a value.  Prints per-file and total shares, and with --show the segmented text with unread
stretches in [brackets].
"""
import collections, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm
os.chdir(HERE)
from dec import K

CODES = {}
if os.path.exists('codes.txt'):
    for line in open('codes.txt', encoding='utf8'):
        if line.strip() and not line.startswith('#'):
            k, v = line.split('\t')[:2]
            CODES[k.strip()] = v.strip()

CACHE = os.path.join(HERE, 'work', 'vocab.txt')
if os.path.exists(CACHE):
    VOC = set(open(CACHE, encoding='utf8').read().split())
else:
    cnt = collections.Counter()
    for c in ('de-dta-1630-1670.txt', 'de-dta-1470-1610.txt'):
        p = os.path.join(HERE, '..', '..', 'lang', 'corpora', c)
        if not os.path.exists(p):
            p = os.path.join('C:/Users/dbour/cypher/lang/corpora', c)
        cnt.update(lm.norm(open(p, encoding='utf8').read(), 'early').split())
    VOC = {w for w, n in cnt.items() if n >= 2 and (len(w) > 1 or w in 'aeo')}
    open(CACHE, 'w', encoding='utf8').write('\n'.join(sorted(VOC)))
if os.path.exists('extra.txt'):
    for line in open('extra.txt', encoding='utf8'):
        if not line.startswith('#'):
            VOC.update(lm.norm(line, 'early').split())
SHORT = set('an am im in zu so da ob er es wo ab um nu ia e o'.split())
VOC = {w for w in VOC if len(w) >= 3 or w in SHORT}
MAXW = 24
if '--control' in sys.argv:          # shuffle the digit table: what does noise score?
    import random
    ks = [k for k in K if k.isdigit()]
    vs = [K[k] for k in ks]
    random.Random(int(sys.argv[sys.argv.index('--control') + 1])).shuffle(vs)
    K.update(dict(zip(ks, vs)))


def segment(s):
    """Best cover of s by vocabulary words: maximise covered letters, then prefer fewer, longer words."""
    n = len(s)
    best = [(0, 0, None)] * (n + 1)  # (covered, -words, backpointer)
    for i in range(1, n + 1):
        cand = (best[i - 1][0], best[i - 1][1], (i - 1, False))
        for j in range(max(0, i - MAXW), i):
            if s[j:i] in VOC:
                c = (best[j][0] + (i - j), best[j][1] - 1, (j, True))
                if c[:2] > cand[:2]:
                    cand = c
        best[i] = cand
    covered = [False] * n
    words, i = [], n
    while i > 0:
        j, ok = best[i][2]
        if ok:
            for k in range(j, i):
                covered[k] = True
        words.append((s[j:i], ok))
        i = j
    return covered, words[::-1]


def runs(path):
    """Yield runs: lists of (token, plaintext-or-None) between clear words."""
    cur = []
    for line in open(path, encoding='utf8'):
        if line.startswith('#'):
            if 'letter-cipher' in line:
                break
            continue
        line = re.sub(r'\{struck:[^}]*\}', ' ', line, flags=re.I)
        for m in re.finditer(r'\{([^}]*)\}|(\S+)', line):
            if m.group(1) is not None:
                if cur:
                    yield cur
                cur = []
                continue
            raw = m.group(2)
            t = raw.rstrip("'?_")
            if re.fullmatch(r'\d\d', t):
                cur.append((raw, K.get(t)))
            elif t in K and not (t.isdigit() and len(t) == 2):
                cur.append((raw, K[t]))
            elif t in CODES:
                cur.append((raw, CODES[t]))
            else:
                cur.append((raw, None))
    if cur:
        yield cur


FRVOC = None


def french_vocab():
    global FRVOC
    if FRVOC is None:
        p = os.path.join('C:/Users/dbour/cypher/lang/corpora', 'fr-henri4.txt')
        c = collections.Counter(lm.norm(open(p, encoding='utf8').read(), 'early').split())
        FRVOC = {w for w, n in c.items() if n >= 3 and len(w) >= 3}
    return FRVOC


def measure(path, show=False):
    global VOC
    saved = VOC
    if 'f032' in path:                  # the French letter signed 232: its runs are French
        VOC = VOC | french_vocab()
    try:
        return _measure(path, show)
    finally:
        VOC = saved


def _measure(path, show=False):
    tot = rd = 0
    out = []
    for run in runs(path):
        # decode; unknown tokens break the text
        pieces, cur = [], []
        for tok, val in run:
            if val is None or '?' in tok and False:
                if cur:
                    pieces.append(cur)
                cur = []
                pieces.append([(tok, None)])
            else:
                if val.isdigit():
                    val = '=' + val                 # a clear numeral: read, not segmented
                cur.append((tok, lm.norm(val, 'early', spaces=False) if not val.startswith('=') else val))
        if cur:
            pieces.append(cur)
        for pc in pieces:
            if pc[0][1] is None:
                tot += 1
                out.append(f'<{pc[0][0]}>')
                continue
            s, owner = '', []
            names = []
            for k, (tok, val) in enumerate(pc):
                if val.startswith('='):          # a code with a name: counts as read, not segmented
                    names.append(k)
                    continue
                s += val
                owner += [k] * len(val)
            cov, words = segment(s)
            ok = [True] * len(pc)
            for p, c in enumerate(cov):
                if not c:
                    ok[owner[p]] = False
            tot += len(pc)
            rd += sum(ok)
            out.append(' '.join(w if good else f'[{w}]' for w, good in words))
            for k in names:
                out.append(pc[k][1][1:].upper())
    if show:
        print('=====', path)
        print(' | '.join(out))
    return tot, rd


if __name__ == '__main__':
    show = '--show' in sys.argv
    T = R = 0
    for f in [a for a in sys.argv[1:] if not a.startswith('--') and not a.isdigit()]:
        t, r = measure(f, show)
        T += t
        R += r
        print(f'{f}: {r}/{t} tokens read = {r / max(1, t):.3f}')
    print(f'TOTAL {R}/{T} = {R / max(1, T):.3f}')
