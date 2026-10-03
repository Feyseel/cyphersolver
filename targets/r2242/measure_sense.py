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


def load_apply(folder):
    spec = importlib.util.spec_from_file_location('apply_mod', os.path.join(folder, 'apply.py'))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
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
    ap = load_apply(folder); m = lm.load(model, spaces=False)
    T = S = 0
    for f in files:
        segs, cur = [], []                       # runs of read tokens: list of (text) ; None = unread
        toks = []
        for line in open(f, encoding='utf8'):
            for kind, lab, v in ap.tokens(line):
                if kind == 'note':
                    continue
                toks.append(lm.norm(v, spaces=False) if v else None)
        t = s = 0
        i = 0
        while i < len(toks):
            if toks[i] is None:
                t += 1; i += 1; continue
            j = i
            while j < len(toks) and toks[j] is not None:
                j += 1
            run_t = toks[i:j]; text = ''.join(run_t)
            lp = charlp(m, text) if text else np.zeros(0)
            pos = 0
            for tk in run_t:
                a, b = pos, pos + len(tk); pos = b
                lo, hi = max(0, a - W), min(len(text), b + W)
                win = lp[max(lo, m.order - 1 if lo == 0 else lo):hi]
                ok = len(win) > 0 and win.mean() > THRESH
                t += 1; s += ok
            i = j
        print(f'{f}: {s}/{t} = {s/t:.3f}')
        T += t; S += s
    print(f'total: {S}/{T} = {S/T:.3f}')


if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3:])
