"""Session 3: decode ct_<folio>.txt with key.tsv, compare to the '=' reading line, measure the share of tokens read.
usage: python measure.py ct_f154.txt [-v]"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
K={}
for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'key.tsv'),encoding='utf-8'):
    if l.startswith('#') or l.startswith('label'): continue
    f=l.rstrip('\n').split('\t')
    if len(f)>=3: K[f[0]]=f[2]
def first(v): return v.split('/')[0].strip().split(' ')[0]
def parse(fn):
    out=[]; cur=None; toks=None
    for l in open(fn,encoding='utf-8'):
        l=l.rstrip('\n')
        if l.startswith('@'): cur=l[1:]; continue
        if not l.strip() or l.startswith('#'): continue
        if l.startswith('='):
            rd=[g.strip() for g in l[1:].split('|')]
            assert len(rd)==len(toks),(cur,len(rd),len(toks),l)
            out.append((cur,toks,rd))
        else: toks=[[x for x in g.split() if not x.endswith('~')] for g in l.split('|')]
    return out
def main(fn,verbose):
    lines=parse(fn); tot=rd_=0; text=[]; unk=set()
    for cur,toks,rd in lines:
        row=[]
        for g,r in zip(toks,rd):
            n=len(g); tot+=n
            unread=r.startswith('{')
            if not unread and r: rd_+=n; text.append(re.sub(r'\(.*?\)|[\[\]?\-~]','',r))
            dec=''.join(first(K[t]) if t in K and first(K[t])!='?' else '['+t+']' for t in g)
            for t in g:
                if t not in K: unk.add(t)
            row.append(f'{dec}={r}')
        if verbose: print(cur,' | '.join(row))
    from lang import lm
    m=lm.load('fr-1600-letters')
    s=' '.join(text).replace("'",' ')
    pc=m.per_char(lm.norm(s,'early'))
    print(f'{fn}: tokens {tot}, read {rd_} ({100*rd_/tot:.1f}%), LM per-char of reading {pc:.2f}; labels not in key: {sorted(unk)}')
    return tot,rd_
if __name__=='__main__':
    main(sys.argv[1],'-v' in sys.argv)
