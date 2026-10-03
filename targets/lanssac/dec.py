"""Plain decode of token lines with key.tsv first values (session 3). usage: python dec.py tokens_file [@section]"""
import sys,re
K={}
for l in open('key.tsv',encoding='utf-8'):
    if l.startswith('#') or l.startswith('label'): continue
    f=l.rstrip('\n').split('\t')
    if len(f)<3: continue
    v=f[2].split('/')[0].strip().split(' ')[0]
    K[f[0]]=v if v!='?' else '['+f[0]+']'
def dec(toks,K=K):
    return ''.join(K.get(t,'['+t+']') if t not in '|.,' else ' ' for t in toks)
if __name__=='__main__':
    sec=sys.argv[2] if len(sys.argv)>2 else None; on=sec is None
    for l in open(sys.argv[1],encoding='utf-8'):
        l=l.strip()
        if l.startswith('@'): on=(sec is None or l==sec); print(l) if on else None; continue
        if not l or l[0]=='#' or not on: continue
        print('  ',dec(l.split()))
