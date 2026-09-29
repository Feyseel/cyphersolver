"""Unigram word model from the 1740s corpus and a Viterbi segmentation score for unspaced text.
usage: python wordseg.py < decrypts.txt      (scores lines)
       python wordseg.py --export           (writes words1740.tsv for hsolve2/hgibbs/msolve2)"""
import math, collections, sys, os, pickle
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wordcounts.pkl')
def counts():
    if os.path.exists(CACHE): return pickle.load(open(CACHE, 'rb'))
    t = lm.norm(open(os.path.join(lm.HERE, 'corpora', 'de-dta-1720-1770.txt'), encoding='utf8').read(), 'modern')
    c = collections.Counter(t.split()); pickle.dump(c, open(CACHE, 'wb')); return c
C = counts(); TOT = sum(C.values())
MAXL = 16
LOGP = {w: math.log(v / TOT) for w, v in C.items() if v >= 2 and len(w) <= MAXL}
def unk(L): return math.log(1e-6) + L * math.log(0.05)
def seg(s):
    n = len(s); best = [0.0] + [-1e18] * n; bp = [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(max(0, j - MAXL), j):
            w = s[i:j]; p = LOGP.get(w)
            if p is None:
                if j - i > 3: continue
                p = unk(j - i)
            v = best[i] + p
            if v > best[j]: best[j] = v; bp[j] = i
    out = []; j = n
    while j > 0: out.append(s[bp[j]:j]); j = bp[j]
    return best[n], ' '.join(reversed(out))
if __name__ == '__main__':
    if sys.argv[1:] == ['--export']:     # words1740.tsv for the C# solvers: total, then word<TAB>count (count >= 3)
        with open('words1740.tsv', 'w') as f:
            f.write('%d\n' % TOT)
            for w, v in C.items():
                if v >= 3 and 1 <= len(w) <= 16 and w.isalpha(): f.write('%s\t%d\n' % (w, v))
        sys.exit()
    for line in sys.stdin:
        s = line.strip().split('\t')[-1].replace('|', '')
        if not s or s.startswith('KEY'): continue
        sc, t = seg(s); print('%.1f %.3f  %s' % (sc, sc / len(s), t[:150]))
