import sys,re; sys.path.insert(0,'../..')
from lang import lm
m=lm.load('de-modern',order=5)
A='abcdefghiklmnopqrstuvwxyz';N=len(A)
ct=open('ct.txt').read().lower().replace('\n',' ')
ct=re.sub(r'[.?]',' ',ct); ct=re.sub(r' +',' ',ct).strip()
PEN=float(sys.argv[1]) if len(sys.argv)>1 else 6
alpha=m.alpha if hasattr(m,'alpha') else None
def lp(ctx,ch):
  return m.score(ctx[-4:]+ch)-m.score(ctx[-4:]) if len(ctx)>=4 else 0
beams=[(0.0,' ',0,[])]  # score, text, keypos, notes
for i,c in enumerate(ct):
  nb=[]
  for s,t,k,no in beams:
    if c==' ':
      nb.append((s+lp(t,' '),t+' ',k,no));continue
    for jump in (0,1,-1,2):
      kk=k+jump
      pen=0 if jump==0 else PEN
      if c in A:
        p=A[(A.index(c)-(2+kk%6))%N]
        nb.append((s-pen+lp(t,p),t+p,kk+1,no+([(i,jump)] if jump else [])))
      else:
        nb.append((s-pen-3,t+'#',kk+1,no+([(i,jump)] if jump else [])))
        if jump==0: nb.append((s-3,t+'#',kk,no))
  nb.sort(key=lambda x:-x[0]); beams=nb[:400]
s,t,k,no=beams[0]
print(t);print(no)
