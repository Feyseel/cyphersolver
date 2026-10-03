"""R1409, second attempt: every symbol (two- and three-figure) is free to stand for one letter or one common
letter pair (syllable), annealed under an order-4 no-space LM with a unigram KL penalty. Control: shuffled tokens.
python r1409_solve2.py <model> [iters]
"""
import os, sys, random, math, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm
from r1409_test import parse, tokens
from r1409_solve import UNI

def main():
    mid = sys.argv[1]; iters = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
    m = lm.load(mid, order=4, spaces=False)
    toks = [t for t in tokens(parse()) if t.replace('?', '').isdigit()]
    toks = [t.replace('?', '') for t in toks]
    letters = list(UNI[mid])
    pairs = {'it-cinquecento': 'di de la le il al el er re ra ar or ro on no in ni an na en ne co ch che per'.split(),
             'de-1640s': 'en er ch ei ie in un nd de te es ge be st an ss sch ich und der die das'.split(),
             'la': 'us um is it et er re in ti nt qu am em es ur ae'.split()}[mid]
    vocab = letters + pairs
    uni = np.array([UNI[mid].get(c, 0.01) for c in m.alpha]) + 1e-3; uni /= uni.sum()
    syms = sorted(set(toks)); sid = {s: i for i, s in enumerate(syms)}
    for label, order in [('real', toks), ('shuffled', random.Random(5).sample(toks, len(toks)))]:
        seq = [sid[t] for t in order]
        best_all = None
        for seed in range(2):
            rng = random.Random(seed)
            key = [rng.choice(letters) if len(s) == 2 else rng.choice(vocab) for s in syms]
            def sc(k):
                s = ''.join(k[i] for i in seq)
                x = m.encode(s)
                q = np.bincount(x, minlength=m.A) / len(x)
                nz = q > 0
                return m.score_idx(x) - 2.0 * len(x) * float((q[nz] * np.log(q[nz] / uni[nz])).sum()), len(x)
            cur, _ = sc(key); best, bk = cur, key[:]
            for it in range(iters):
                T = 20.0 * (1 - it / iters) + 0.2
                i = rng.randrange(len(syms)); old = key[i]; key[i] = rng.choice(vocab)
                new, _ = sc(key)
                if new >= cur or rng.random() < math.exp((new - cur) / T):
                    cur = new
                    if cur > best: best, bk = cur, key[:]
                else:
                    key[i] = old
            n = sc(bk)[1]
            print('%s %s seed %d: %.3f/char' % (mid, label, seed, best / n), flush=True)
            if best_all is None or best > best_all[0]: best_all = (best, bk)
        if label == 'real':
            bk = best_all[1]
            print('   ', ' '.join(bk[i] for i in seq[:200]))
            print('   ', ' '.join('%s=%s' % (s, bk[i]) for i, s in enumerate(syms)))

if __name__ == '__main__':
    main()
