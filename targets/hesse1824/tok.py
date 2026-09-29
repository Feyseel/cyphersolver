import re
C='abcdefghiklmnopqrstuvwxyz123456789'
P='abcdefghiklmnopqrstuvwxyz'
ct=open('ct.txt').read().lower()
def d(ch,s):
  i=C.index(ch)-s
  return P[i] if 0<=i<25 else '?'
for line in ct.split('\n'):
  for t in re.findall(r'[a-z0-9]+',line):
    print(f'{t:11s}',' '.join(f'{p}:'+''.join(d(c,2+(p+i)%6) for i,c in enumerate(t)) for p in range(6)))
  print('--')
