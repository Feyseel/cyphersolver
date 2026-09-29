"""unread.py files... : list every two-digit group that measure.py leaves outside a word, with file, scan line and
position in that line (counting every token on the line, clear words included), for re-checking against the scans."""
import re, sys
sys.argv, files = sys.argv[:1], sys.argv[1:]
import measure as M
from lang import lm


def runs_pos(path):
    cur = []
    for ln, line in enumerate(open(path, encoding='utf8'), 1):
        if line.startswith('#'):
            if 'letter-cipher' in line: break
            continue
        line = re.sub(r'\{struck:[^}]*\}', ' ', line, flags=re.I)
        for k, m in enumerate(re.finditer(r'\{[^}]*\}|\S+', line), 1):
            t = m.group(0)
            u = t.rstrip("'?_")
            if t.startswith('{'):
                if cur: yield cur
                cur = []; continue
            if re.fullmatch(r'\d\d', u): v = M.K.get(u)
            elif u in M.K and not (u.isdigit() and len(u) == 2): v = M.K[u]
            elif u in M.CODES: v = M.CODES[u]
            else: v = None
            if v is None or v.isdigit() or v.startswith('='):
                if cur: yield cur
                cur = []; continue
            cur.append((t, lm.norm(v, 'early', spaces=False), ln, k))
    if cur: yield cur


for f in files:
    for run in runs_pos(f):
        s, owner = '', []
        for i, (t, v, ln, k) in enumerate(run):
            s += v; owner += [i] * len(v)
        cov, words = M.segment(s)
        bad = sorted({owner[p] for p, c in enumerate(cov) if not c})
        for i in bad:
            t, v, ln, k = run[i]
            if re.fullmatch(r'\d\d', t.rstrip("'?_")):
                ctx = ' '.join(x[0] for x in run[max(0, i - 3):i]) + ' <' + t + '> ' + ' '.join(x[0] for x in run[i + 1:i + 4])
                seg = ''.join(w if g else '[' + w + ']' for w, g in words)
                p = sum(len(x[1]) for x in run[:i])
                print(f'{f}\tline {ln}\tpos {k}\t{ctx}\t...{seg[max(0, p - 25):p + 30]}...')
