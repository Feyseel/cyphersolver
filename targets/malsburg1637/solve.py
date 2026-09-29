"""Homophonic annealer for the Malsburg 1637 two-digit cipher.

usage: python solve.py <restarts> <iters> <seed> file1.txt [file2.txt ...] [--fix 27=n,39=a ...]

Transcription files: one scan line per line, groups separated by spaces, '#' comments, {clear words}.
Two-digit groups (10-99) are the substitution symbols; letter signs, 3-digit codes and symbols (+, 4#) are treated
as breaks (the text restarts there); {clear} words are kept as fixed plaintext.  Scored with lang de-1640s,
order 5, no spaces, 'early' normalisation.
"""
import math, os, random, re, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

ORDER = 5
INIT = {}
SIGNS = {}
if os.path.exists('key.txt'):
    for _l in open('key.txt', encoding='utf8'):
        if not _l.startswith('#'):
            for _kv in _l.split():
                _k, _v = _kv.split('=')
                if not _k.isdigit():
                    SIGNS[_k] = _v
M = lm.load('de-1640s', order=ORDER, spaces=False)
ALPHA = M.alpha
IDX = M.index


def read_tokens(paths):
    """Return a list of items: ('n', '27') substitution symbol, ('c', 'und') clear text, ('b', 'N') break."""
    out = []
    for p in paths:
        for line in open(p, encoding='utf8'):
            if line.startswith('#'):
                continue
            for m in re.finditer(r'\{([^}]*)\}|(\S+)', line):
                if m.group(1) is not None:
                    out.append(('c', lm.norm(m.group(1), 'early', spaces=False)))
                    continue
                t = m.group(2).rstrip("'?_")
                if re.fullmatch(r'\d\d', t):
                    out.append(('n', t))
                elif t in SIGNS:
                    out.append(('c', SIGNS[t]))
                else:
                    out.append(('b', m.group(2)))
    return out


def build(items):
    """Split into segments at breaks; each segment is an int array where >=0 is a symbol id and <0 is -(letter+1)."""
    syms = sorted({t for k, t in items if k == 'n'})
    sid = {s: i for i, s in enumerate(syms)}
    segs, cur = [], []
    for k, t in items:
        if k == 'b':
            if cur:
                segs.append(cur)
            cur = []
        elif k == 'n':
            cur.append(sid[t])
        else:
            cur += [-(IDX[c] + 1) for c in t]
    if cur:
        segs.append(cur)
    flat = np.array([x for s in segs for x in s + [-10**6]], dtype=np.int64)  # sentinel between segments
    return syms, sid, segs, flat


def decode(flat, key):
    x = np.where(flat >= 0, key[np.clip(flat, 0, None)], -flat - 1)
    return x


UNI = None
WFREQ = 0.0


def score(flat, key, bounds):
    x = decode(flat, key)
    s = sum(M.score_idx(x[a:b]) for a, b in bounds)
    if WFREQ:
        c = np.bincount(np.concatenate([x[a:b] for a, b in bounds]), minlength=len(ALPHA)).astype(float) + 0.01
        p = c / c.sum()
        s -= WFREQ * c.sum() * float((p * np.log(p / UNI)).sum())
    return s


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    fix = {}
    if '--fix' in sys.argv:
        for kv in sys.argv[sys.argv.index('--fix') + 1].split(','):
            k, v = kv.split('=')
            fix[k] = v
        args = [a for a in args if a != sys.argv[sys.argv.index('--fix') + 1]]
    global UNI, WFREQ
    if '--wfreq' in sys.argv:
        WFREQ = float(sys.argv[sys.argv.index('--wfreq') + 1])
        args = [a for a in args if a != sys.argv[sys.argv.index('--wfreq') + 1]]
    uni = np.exp(M.lp[:len(ALPHA)]) if False else None
    corpus = open(os.path.join(os.path.dirname(os.path.abspath(lm.__file__)), 'corpora', 'de-dta-1630-1670.txt'), encoding='utf8').read()[:3000000]
    cx = M.encode(lm.norm(corpus, 'early', spaces=False))
    UNI = (np.bincount(cx, minlength=len(ALPHA)) + 1.0) / (len(cx) + len(ALPHA))
    global INIT
    INIT = {}
    if '--init' in sys.argv:
        for _l in open('key.txt', encoding='utf8'):
            if not _l.startswith('#'):
                for _kv in _l.split():
                    _k, _v = _kv.split('=')
                    if _k.isdigit():
                        INIT[_k] = _v
    restarts, iters, seed = int(args[0]), int(args[1]), int(args[2])
    items = read_tokens(args[3:])
    syms, sid, segs, flat = build(items)
    # segment bounds in flat (exclude sentinels)
    bounds, pos = [], 0
    for s in segs:
        bounds.append((pos, pos + len(s)))
        pos += len(s) + 1
    flat = flat.copy()
    flat[flat == -10**6] = -(IDX['e'] + 1)  # never read: sentinel positions fall outside every bound
    free = [i for i, s in enumerate(syms) if s not in fix]
    n_letters = sum(b - a for a, b in bounds)
    rng = random.Random(seed)
    freq = 'eeeeeeennnnniiiissssrrrrttttaaahhhdddduuulllcccggmmobwfkzp'
    best = None
    for r in range(restarts):
        key = np.array([IDX[rng.choice(freq)] for _ in syms], dtype=np.int64)
        if INIT:
            for s_, v_ in INIT.items():
                if s_ in sid:
                    key[sid[s_]] = IDX[v_]
        for s, v in fix.items():
            if s in sid:
                key[sid[s]] = IDX[v]
        sc = score(flat, key, bounds)
        T0, T1 = (2.0, 0.2) if INIT else (12.0, 0.3)
        for it in range(iters):
            T = T0 * (T1 / T0) ** (it / iters)
            i = rng.choice(free)
            old = key[i]
            if rng.random() < 0.2:
                j = rng.choice(free)
                key[i], key[j] = key[j], key[i]
                n = score(flat, key, bounds)
                if n >= sc or rng.random() < math.exp((n - sc) / T):
                    sc = n
                else:
                    key[i], key[j] = key[j], key[i]
                continue
            key[i] = rng.randrange(len(ALPHA))
            n = score(flat, key, bounds)
            if n >= sc or rng.random() < math.exp((n - sc) / T):
                sc = n
            else:
                key[i] = old
        txt = ''.join(ALPHA[c] for c in decode(flat, key)[:400])
        print(f'run {r} score/char {sc / n_letters:.3f}  {txt[:160]}', flush=True)
        if best is None or sc > best[0]:
            best = (sc, key.copy())
    sc, key = best
    print('BEST', round(sc / n_letters, 3))
    print(' '.join(f'{s}={ALPHA[key[sid[s]]]}' for s in syms))
    # readable output: tokens with breaks shown
    out = []
    for k, t in items:
        out.append(ALPHA[key[sid[t]]] if k == 'n' else (t.upper() if k == 'c' else f'[{t}]'))
    print(''.join(out))


if __name__ == '__main__':
    main()
