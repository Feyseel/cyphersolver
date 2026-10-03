"""Session 3 control: LM score of the raw key decode (first value per sign, all tokens, no hand choices) of each new
letter vs the same tokens shuffled (3 shuffles). usage: python control3.py"""
import os, sys, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
from measure import parse, K, first
m=lm.load('fr-1600-letters', spaces=False)
for fn in ['ct_f154.txt','ct_f154v.txt','ct_f156.txt','ct_f156v.txt']:
    toks=[t for _,g,_ in parse(fn) for grp in g for t in grp]
    dec=lambda ts:''.join(first(K[t]) for t in ts if t in K and first(K[t]) not in ('?','(context)'))
    real=m.per_char(lm.norm(dec(toks),'early',spaces=False))
    sh=[]
    for s in range(3):
        r=toks[:]; random.Random(s).shuffle(r); sh.append(m.per_char(lm.norm(dec(r),'early',spaces=False)))
    print(f'{fn}: raw key decode {real:.2f}/char; shuffled {", ".join(f"{x:.2f}" for x in sh)}')
