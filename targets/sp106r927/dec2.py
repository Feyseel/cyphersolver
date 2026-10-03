"""Decode the hand transcriptions (hand_p1/2/3.txt) with key.json.

Polyphonic signs (key value with '/') are resolved per occurrence by the French LM
(fr-1600-letters, no spaces): each choice is scored on a window of the decrypt around it.
Usage: python dec2.py hand_p1.txt [more files]   -> prints one decrypt line per column
"""
import os, sys, json, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = json.load(open(os.path.join(HERE, 'key.json')))
M = lm.load('fr-1600-letters', spaces=False)


def tokens(path):
    for line in open(path, encoding='utf-8'):
        line = line.split('#', 1)[0].strip()
        if ':' not in line:
            continue
        lab, t = line.split(':', 1)
        yield lab.strip(), [x for x in t.split() if x not in ('=', '/')]


def val(tok):
    t = tok.rstrip('?')
    if t.startswith('[') or t.startswith('<'):
        return None            # blot, flap, number, unread sign
    return KEY.get(t)


def decode_line(toks):
    vals = [val(t) for t in toks]
    opts = [(v.split('/') if v else ['_']) for v in vals]
    out = [o[0] for o in opts]
    for i, o in enumerate(opts):
        if len(o) > 1:
            best = None
            for c in o:
                trial = out[:i] + [c] + out[i + 1:]
                w = ''.join(trial[max(0, i - 6):i + 7]).replace('_', '')
                s = M.per_char(lm.norm(w, 'early', spaces=False)) if w else 0
                if best is None or s > best[0]:
                    best = (s, c)
            out[i] = best[1]
    return out


if __name__ == '__main__':
    for p in sys.argv[1:]:
        for lab, toks in tokens(p):
            print(lab, ''.join(decode_line(toks)))
