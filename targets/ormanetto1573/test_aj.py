import sys, random, re, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
import dec_aj as D
M = lm.load('it-modern')
# only the well-supported codes (graded c/p by AJ and fitting repeatedly); the g-graded and 2-digit-letter-pair codes are dropped
keep = ['66','2.44','6.11','9.11','3.44','8.22','4.88','63','97','87','5.11','1.44','77','35','2.22','76']
D.CODES = {k:v for k,v in D.CODES.items() if k in keep}
src = open('r116_cipher.txt', encoding='utf8').read()
toks = []
for part in re.split(r'^#.*$', src, flags=re.M):
    if part.strip(): toks += D.parse(part)
def score(key):
    D.KEY = key
    txt = D.decode(toks)
    txt = re.sub(r'\[[^\]]*\]|<[^>]*>', ' ', txt)
    w = [x for x in txt.split() if x]
    s = ' '.join(w)
    return M.per_char(lm.norm(s, 'modern')), txt
base = dict(D.KEY)
real, txt = score(base)
print('real key per-char', round(real,3), 'chars', len(re.sub(r'\s','',txt)))
letters = sorted(set(base.values()))
random.seed(1); ctl=[]
for _ in range(200):
    p = letters[:]; random.shuffle(p); mp = dict(zip(sorted(set(base.values())), p))
    ctl.append(score({k: mp[v] for k, v in base.items()})[0])
print('shuffled-letter controls: best', round(max(ctl),3), 'mean', round(sum(ctl)/len(ctl),3))
