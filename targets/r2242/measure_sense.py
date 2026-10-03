"""Share of cipher tokens read as sense, measured with a shared lang/ model.

usage: python measure_sense.py <folder-with-apply.py> <model> <transcription> [...]
Each cipher token (digit pair or word sign) is decrypted with that folder's apply.py. Unread tokens are not sense.
A read token counts as sense when the mean per-character log-prob of a 13-character window centred on it
is above THRESH; the window never crosses an unread token. THRESH is calibrated on R2242 p1, whose decrypt
is confirmed by the clear text under it (see NOTES).
"""
import os, sys, importlib.util
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

THRESH = -4.3   # p1 (confirmed by its clear text) passes ~99%; letter-shuffled p3/p4 controls pass ~5%
W = 6
WORDS = os.environ.get('WORDS', '1') == '1'   # WORDS=0: LM window only (the 2 Oct first measure)


# ---- word check (2 Oct 2026): the nl-modern corpus is small (1.5 MB of Gutenberg), so correct but rare or
# period-spelled words (alliansie, persisteeren, ambassadeurs) fail the LM window. A read token also counts as
# sense when it lies inside an attested word of MINLEN+ letters found in the decrypt run: words from the lang/
# corpus of the page's language plus Colenbrander, Gedenkstukken I-II (1789-1798 Dutch and French, fetched by
# fetch_gedenkstukken.py). The false-positive rate is measured on letter-shuffled controls (--control).
MINLEN = 6
_LEX = {}


def lexicon(model):
    lang = model.split('-')[0]
    if lang in _LEX:
        return _LEX[lang]
    import glob, collections, re as _re
    here = os.path.dirname(os.path.abspath(__file__))
    c = collections.Counter()
    src = os.path.join(here, '..', '..', 'lang', 'corpora', f'{lang}-gutenberg.txt')
    if os.path.exists(src):
        c.update(_re.findall(r'[a-z]+', lm.norm(open(src, encoding='utf8', errors='replace').read())))
    for g in glob.glob(os.path.join(here, 'gs_corpus', 'gs*_*.txt')):
        c.update(_re.findall(r'[a-z]+', lm.norm(open(g, encoding='utf8').read())))
    words = {w for w, n in c.items() if len(w) >= MINLEN and n >= 2}
    words |= {w.replace('ij', 'y') for w in words if 'ij' in w}
    _LEX[lang] = words
    return words


def covered(text, words):
    """Boolean per character: inside some attested word of MINLEN+ letters."""
    cov = [False] * len(text)
    L = max(map(len, words)) if words else 0
    for i in range(len(text)):
        for j in range(i + MINLEN, min(len(text), i + 25) + 1):
            if text[i:j] in words:
                for k in range(i, j):
                    cov[k] = True
    return cov


def nrm(v, model):
    """Token value as the model's alphabet. For Dutch, the cipher's y (pair 13) is the period spelling of ij
    (zyn, myn, gesonden zy); the nl-modern corpus spells ij, so y is scored as ij (3 Oct 2026)."""
    t = lm.norm(v, spaces=False)
    return t.replace('y', 'ij') if model.startswith('nl') else t


def load_apply(folder, model=''):
    spec = importlib.util.spec_from_file_location('apply_mod', os.path.join(folder, 'apply.py'))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    if hasattr(mod, 'FRENCH'):
        mod.FRENCH = model.startswith('fr')     # R1892 p1: pair 12 = z in French
    return mod


def charlp(m, s):
    """log-prob of each char of s given up to order-1 previous chars (padding with the unigram start)."""
    x = m.encode(s); k = m.order; out = np.zeros(len(x))
    for i in range(len(x)):
        lo = max(0, i - k + 1); seg = x[lo:i + 1]
        if len(seg) < k:      # short context: average of the full-order score is not available; use per-char
            out[i] = m.score_idx(x[max(0, i - k + 1):i + 1]) if len(seg) == k else -3.0
        else:
            out[i] = m.score_idx(seg)
    return out


def run(folder, model, files):
    """Lines starting with {model-id} (e.g. a French closing on a Dutch page) are scored with that model."""
    import re as _re
    models, lexs, aps = {}, {}, {}

    def get(mid):
        if mid not in models:
            models[mid] = lm.load(mid, spaces=False)
            lexs[mid] = lexicon(mid) if WORDS else None
            aps[mid] = load_apply(folder, mid)
        return models[mid], lexs[mid], aps[mid]
    T = S = 0
    for f in files:
        toks = []                                   # (text or None, model-id)
        for line in open(f, encoding='utf8'):
            mm = _re.match(r'\s*\{([a-z0-9-]+)\}', line)
            mid = mm.group(1) if mm else model
            if mm:
                line = line[mm.end():]
            m, LEX, ap = get(mid)
            for kind, lab, v in ap.tokens(line):
                if kind == 'note':
                    continue
                toks.append((nrm(v, mid) if v else None, mid))
        t = s = 0
        i = 0
        while i < len(toks):
            if toks[i][0] is None:
                t += 1; i += 1; continue
            j = i
            while j < len(toks) and toks[j][0] is not None and toks[j][1] == toks[i][1]:
                j += 1
            m, LEX, ap = get(toks[i][1])
            run_t = [x[0] for x in toks[i:j]]; text = ''.join(run_t)
            lp = charlp(m, text) if text else np.zeros(0)
            cov = covered(text, LEX) if LEX is not None else [False] * len(text)
            pos = 0
            for tk in run_t:
                a_, b_ = pos, pos + len(tk); pos = b_
                lo, hi = max(0, a_ - W), min(len(text), b_ + W)
                win = lp[max(lo, m.order - 1 if lo == 0 else lo):hi]
                ok = (len(win) > 0 and win.mean() > THRESH) or (b_ > a_ and all(cov[a_:b_]))
                t += 1; s += ok
            i = j
        print(f'{f}: {s}/{t} = {s/t:.3f}')
        T += t; S += s
    print(f'total: {S}/{T} = {S/T:.3f}')


def failing(folder, model, f):
    """Print each line with tokens that fail the sense test marked [[..]] (unread as <..>)."""
    ap = load_apply(folder, model); m = lm.load(model, spaces=False)
    LEX = lexicon(model) if WORDS else None
    rows = []
    for ln, line in enumerate(open(f, encoding='utf8'), 1):
        for kind, lab, v in ap.tokens(line):
            if kind != 'note':
                rows.append((ln, lab, nrm(v, model) if v else None))
    ok = [False] * len(rows); i = 0
    while i < len(rows):
        if rows[i][2] is None:
            i += 1; continue
        j = i
        while j < len(rows) and rows[j][2] is not None:
            j += 1
        text = ''.join(r[2] for r in rows[i:j]); lp = charlp(m, text); pos = 0
        cov = covered(text, LEX) if LEX is not None else [False] * len(text)
        for k in range(i, j):
            a, b = pos, pos + len(rows[k][2]); pos = b
            lo, hi = max(0, a - W), min(len(text), b + W)
            win = lp[max(lo, m.order - 1 if lo == 0 else lo):hi]
            ok[k] = (len(win) > 0 and win.mean() > THRESH) or (b > a and all(cov[a:b]))
        i = j
    cur = None; out = []
    for (ln, lab, v), g in zip(rows, ok):
        if ln != cur:
            if out: print(cur, ''.join(out))
            cur, out = ln, []
        out.append(v if g else ('[[' + (v or '<' + lab + '>') + ']]'))
    if out: print(cur, ''.join(out))


def control(folder, model, files, seeds=5):
    """Pass rate of the same test on letter-shuffled decrypts (token lengths and unread positions kept)."""
    import random
    ap = load_apply(folder, model); m = lm.load(model, spaces=False)
    LEX = lexicon(model) if WORDS else None
    toks = []
    for f in files:
        for line in open(f, encoding='utf8'):
            for kind, lab, v in ap.tokens(line):
                if kind != 'note':
                    toks.append(nrm(v, model) if v else None)
    letters = [c for t in toks if t for c in t]
    rates = []
    for sd in range(seeds):
        random.Random(sd).shuffle(letters); it = iter(letters)
        sh = [''.join(next(it) for _ in t) if t else None for t in toks]
        t = s = 0; i = 0
        while i < len(sh):
            if sh[i] is None:
                i += 1; continue
            j = i
            while j < len(sh) and sh[j] is not None:
                j += 1
            text = ''.join(sh[i:j]); lp = charlp(m, text); pos = 0
            cov = covered(text, LEX) if LEX is not None else [False] * len(text)
            for tk in sh[i:j]:
                a, b = pos, pos + len(tk); pos = b
                lo, hi = max(0, a - W), min(len(text), b + W)
                win = lp[max(lo, m.order - 1 if lo == 0 else lo):hi]
                t += 1; s += (len(win) > 0 and win.mean() > THRESH) or (b > a and all(cov[a:b]))
            i = j
        rates.append(s / t)
    print(f'control (letter-shuffled, {seeds} seeds): pass rate {np.mean(rates):.3f} (max {max(rates):.3f})')


if __name__ == '__main__':
    if sys.argv[1] == '--control':
        control(sys.argv[2], sys.argv[3], sys.argv[4:])
    elif sys.argv[1] == '--show':
        failing(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        run(sys.argv[1], sys.argv[2], sys.argv[3:])

