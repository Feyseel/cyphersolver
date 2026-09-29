import re,collections,sys
def load(files=('trans_p1.txt','trans_p2.txt')):
    toks=[];lines=[]
    for f in files:
        for ln in open(f,encoding='utf8'):
            if not ln.startswith('L'): continue
            tag,rest=ln.split(':',1)
            rest=re.sub(r'\[.*?\]',' | ',rest)
            t=[x.rstrip('?') for x in rest.split() if x not in ('=',)]
            lines.append((f[6:8]+tag,t))
            toks+= [x for x in t]
    return toks,lines
if __name__=='__main__':
    toks,lines=load()
    toks=[t for t in toks if t!='|']
    c=collections.Counter(toks)
    print('tokens',len(toks),'distinct',len(c))
    print('singletons',sum(1 for v in c.values() if v==1))
    print(c.most_common(60))
    nums=sorted(int(x) for x in c)
    print('range',nums[0],nums[-1])
    # digit length distribution
    print(collections.Counter(len(t) for t in toks))
    # by hundreds
    h=collections.Counter(int(t)//100 for t in toks); print('by hundred (tokens)',sorted(h.items()))
    h=collections.Counter(int(t)//100 for t in c); print('by hundred (types)',sorted(h.items()))
    # repeats
    for n in range(6,1,-1):
        cc=collections.Counter(tuple(toks[i:i+n]) for i in range(len(toks)-n+1))
        rep=[(k,v) for k,v in cc.items() if v>1]
        print(n, len(rep), sorted(rep,key=lambda x:-x[1])[:40])
