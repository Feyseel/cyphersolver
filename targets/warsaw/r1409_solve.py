"""R1409: ciphertext-only annealing of the two-figure groups as a homophonic (many-to-one) letter cipher.

Three-figure groups and the rare numbers are dropped (treated as words/codes), the two-figure groups are
concatenated, and each figure gets a free letter. Run for each candidate language; compare with the same run on
a shuffled ciphertext (control).  python r1409_solve.py [lang ...]
"""
import os, sys, random, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm
from r1409_test import parse, tokens

def run(m, seq, nsym, rng, iters=40000, uni=None):
    A = m.A
    key = np.array([rng.randrange(A) for _ in range(nsym)])
    cnt = np.bincount(seq, minlength=nsym).astype(float)
    N = len(seq)
    def sc(k):
        q = np.bincount(k, weights=cnt, minlength=A) / N
        nz = q > 0
        kl = float((q[nz] * np.log(q[nz] / uni[nz])).sum())
        return m.score_idx(k[seq]) - 2.0 * N * kl
    cur = sc(key); best, bk = cur, key.copy()
    T0 = 20.0
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.2
        s = rng.randrange(nsym); old = key[s]; key[s] = rng.randrange(A)
        new = sc(key)
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            cur = new
            if cur > best: best, bk = cur, key.copy()
        else:
            key[s] = old
    return best, bk

# letter frequencies (percent), standard tables
UNI = {
 'it-cinquecento': dict(e=11.8,a=11.7,i=11.3,o=9.8,n=6.9,l=6.5,r=6.4,t=5.6,s=5.0,c=4.5,d=3.7,u=3.0,p=3.0,m=2.5,h=1.5,g=1.6,f=1.0,b=0.9,q=0.5,z=0.5),
 'la': dict(e=11.4,i=11.0,a=8.9,u=8.5,t=8.0,s=7.6,r=6.7,n=6.3,o=5.4,m=5.4,c=3.9,l=3.1,p=3.0,d=2.8,q=1.5,b=1.6,g=1.2,f=0.9,h=0.7,x=0.6),
 'de-1640s': dict(e=16.0,n=9.8,i=7.5,r=7.0,s=6.6,t=6.2,a=6.0,h=4.8,d=5.1,u=4.4,l=3.4,c=3.1,g=3.0,m=2.5,o=2.5,b=1.9,w=1.9,f=1.7,k=1.2,z=1.1,p=0.8,v=0.8),
 'fr-1600-letters': dict(e=15.5,s=8.0,a=7.6,i=7.5,t=7.2,n=7.1,r=6.6,u=6.3,l=5.5,o=5.3,d=3.7,c=3.3,m=3.0,p=3.0,q=1.4,v=1.6,f=1.1,b=0.9,g=0.9,h=0.7,x=0.4,z=0.3),
 'es-golden-age': dict(e=13.7,a=12.5,o=8.7,s=8.0,n=6.7,r=6.9,i=6.2,l=5.0,d=5.9,u=3.9,t=4.6,c=4.7,m=3.2,p=2.5,q=1.0,b=1.4,g=1.0,y=0.9,h=0.7,f=0.7,z=0.5,x=0.2),
}

if __name__ == '__main__':
    langs = sys.argv[1:] or ['it-cinquecento', 'la', 'de-1640s', 'fr-1600-letters', 'es-golden-age']
    toks = tokens(parse())
    two = [t for t in toks if len(t) == 2 and t.isdigit()]
    syms = sorted(set(two)); sid = {s: i for i, s in enumerate(syms)}
    seq = np.array([sid[t] for t in two])
    shuf = seq.copy(); np.random.default_rng(0).shuffle(shuf)
    print(len(two), 'two-figure tokens,', len(syms), 'symbols')
    for mid in langs:
        m = lm.load(mid, order=4, spaces=False)
        n = len(seq) - 3
        uni = np.full(m.A, 1e-4)
        corpus_sample = UNI.get(mid)
        for ch, f in corpus_sample.items():
            if ch in m.index: uni[m.index[ch]] += f
        uni /= uni.sum()
        for label, s in [('real', seq), ('shuffled', shuf)]:
            res = [run(m, s, len(syms), random.Random(r), uni=uni) for r in range(3)]
            res.sort(key=lambda x: -x[0])
            b, k = res[0]
            pt = ''.join(m.alpha[i] for i in k[s])
            print('%-16s %-8s best %.3f/char  seeds %s' % (mid, label, b / n, ' '.join('%.3f' % (r[0] / n) for r in res)))
            if label == 'real':
                print('   ', pt[:240])
                print('   ', ' '.join('%s=%s' % (sy, m.alpha[k[i]]) for i, sy in enumerate(syms)))
