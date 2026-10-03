"""Decode R9425 with the R9426 key, unchanged, plus the nomenclator values fixed in this folder (codes.txt)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..')); sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm
from solve import parse, is_code
from decode import dec, K

def load_codes():
    C = {}
    for ln in open(os.path.join(HERE, 'codes.txt'), encoding='utf8'):
        if ln.startswith('#') or not ln.strip(): continue
        p = ln.rstrip('\n').split('\t')
        C[p[0]] = (p[1], p[2])          # value, status (null / fixed / probable)
    return C

if __name__ == '__main__':
    C = load_codes()
    P = parse(os.path.join(HERE, 'transcription.txt'))
    for lid, items in P:
        o = []
        for it in items:
            if it[0] == 'clear': o.append('[' + it[1] + ']')
            elif it[0] == 'word':
                w = it[1]
                if is_code(w):
                    for t in w:
                        if t in K and len(w) == 1: o.append(K[t].upper() + '.')
                        elif t in C: o.append('{' + (C[t][0] or '-') + '}' if C[t][1] != 'probable' else '{' + C[t][0] + '?}')
                        else: o.append('<' + t + '>')
                else: o.append(dec(w))
        print(lid, ' '.join(o))
