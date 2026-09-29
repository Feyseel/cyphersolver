"""Many-to-one substitution annealer for the f. 12 letter-cipher block (work/f012_letters.txt).
Each cipher letter (ü, ÿ distinct) maps to one plaintext letter; numbers and LL are breaks."""
import math, os, random, re, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
MODEL = os.environ.get('LMODEL', 'de-1640s')
CORP = os.environ.get('LCORP', 'de-dta-1630-1670.txt')
M = lm.load(MODEL, order=5, spaces=False)
A = M.alpha
t = open('work/f012_letters.txt', encoding='utf8').read()
if '--reverse' in sys.argv:
    t = t[::-1]
t = re.sub(r'\[blot\]|\?', '.', t)
t = re.sub(r'LL|\d+', '.', t)
segs = [s for s in re.split(r'[.\s]+', t.replace('\n', '')) if s]
syms = sorted(set(''.join(segs)))
sid = {s: i for i, s in enumerate(syms)}
X = [np.array([sid[c] for c in s]) for s in segs]
corpus = open([p for p in (os.path.join(os.path.dirname(os.path.abspath(lm.__file__)), 'corpora', CORP), 'C:/Users/dbour/cypher/lang/corpora/' + CORP) if os.path.exists(p)][0], encoding='utf8').read()[:3000000]
cx = M.encode(lm.norm(corpus, 'early', spaces=False))
UNI = (np.bincount(cx, minlength=len(A)) + 1.0) / (len(cx) + len(A))
W = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
ALLX = np.concatenate(X)
def score(k):
    s = sum(M.score_idx(k[x]) for x in X)
    c = np.bincount(k[ALLX], minlength=len(A)) + 0.01
    p = c / c.sum()
    return s - W * c.sum() * float((p * np.log(p / UNI)).sum())
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
rng = random.Random(seed)
best = None
for r in range(int(sys.argv[2]) if len(sys.argv) > 2 else 4):
    k = np.array([rng.randrange(len(A)) for _ in syms])
    sc = score(k)
    it = 80000
    for i in range(it):
        T = 8 * (0.1 / 8) ** (i / it)
        j = rng.randrange(len(syms)); o = k[j]; k[j] = rng.randrange(len(A))
        n = score(k)
        if n >= sc or rng.random() < math.exp((n - sc) / T): sc = n
        else: k[j] = o
    txt = ' '.join(''.join(A[c] for c in k[x]) for x in X)
    N = sum(len(x) for x in X)
    print(round(sc / N, 3), txt[:300], flush=True)
    if best is None or sc > best[0]: best = (sc, k.copy(), txt)
print({s: A[best[1][sid[s]]] for s in syms})
print(best[2])
