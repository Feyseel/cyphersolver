"""Test AJ Devadas's 'cifra ordinaria' key (1 Oct 2026 email) on R116 / R118 from our own transcription.
Tokenisation: undotted 0 closes the digit before it (x0); dotted 0 opens the next (0x); strokes 2/4/5 + '1' = word end."""
import re, sys
KEY = {  # sign -> letter ; '.'-suffix = dotted single digit, '0.d' = dotted zero + d
 '40':'a','4.':'a','4':'b','0.2':'b','50':'c','7.':'c','0.4':'d','7':'d','60':'e','5.':'e','0.6':'f','5':'f',
 '7:':'g','3.':'g','3':'i','0.8':'i','80':'l','2.':'l','2':'m','0.1':'m','90':'n','6.':'n','0.3':'o','6':'o',
 '30':'p','8.':'p','0.5':'r','8':'r','20':'s','9.':'s','0.7':'t','9':'t','10':'u','1.':'u','0.9':'z'}
CODES = {'6.11':'tutto','2.44':'quello','66':'che','9.11':'V.S.Ill.ma','3.44':'Re','8.22':'quanto','4.88':'S.S.ta',
 '63':'Imperatore','97':'officii','87':'non','5.11':'tanto','1.44':'questo','77':'negotio','35':'lega','2.22':'pace',
 '76':'come','4.22':'perche','62':'canto','48':'essere','84':'bene','422':'ancora','47':'tutta','93':'tutta','3.22':'Italia'}
def parse(src):
    toks=[]
    for t in src.split():
        if t.startswith('#'): continue
        m=re.match(r'^([0-9?])(\.?)_?$',t)
        if m: toks.append((m.group(1),m.group(2)=='.'))
    return toks
def decode(toks, pairs=None):
    out=[];i=0;n=len(toks)
    def rec(t,a,b):
        if pairs is not None: pairs.append((sg(a,b),t))
    def sg(a,b): return ''.join(d+('.' if dt else '') for d,dt in toks[a:b])
    def key(i,k):  # signature of next k toks
        return ''.join(d+('.' if dt else '') for d,dt in toks[i:i+k])
    codekeys=sorted(CODES,key=lambda c:-len(c.replace('.','')))
    while i<n:
        d,dt=toks[i]
        # stroke separator
        if d in '245' and not dt and i+1<n and toks[i+1]==('1',False) and not (i+2<n and toks[i+2]==('0',False)):
            out.append(' ');rec(' ',i,i+2);i+=2;continue
        # dotted zero opens
        if d=='0' and dt and i+1<n:
            s='0.'+toks[i+1][0]; out.append(KEY.get(s,'<%s>'%s)); rec(out[-1],i,i+2); i+=2;continue
        # code group
        hit=None
        for c in codekeys:
            k=len(c.replace('.',''))
            if i+k<=n and key(i,k)==c: hit=c;break
        if hit and '.' not in hit and len(hit)==2 and hit[-1] in '245' and i+2<n and toks[i+2]==('1',False): hit=None  # the last digit is a word-end stroke, not part of a code
        if hit and not (i+len(hit.replace('.',''))<n and toks[i+len(hit.replace('.',''))]==('0',False) and not hit.startswith(('6.1','9.1'))): 
            out.append('['+CODES[hit]+']');rec(out[-1],i,i+len(hit.replace('.','')));i+=len(hit.replace('.',''));continue
        # x0
        if i+1<n and toks[i+1]==('0',False) and d!='0':
            s=d+'0'; out.append(KEY.get(s,'<%s>'%s)); rec(out[-1],i,i+2); i+=2;continue
        s=d+('.' if dt else '')
        out.append(KEY.get(s,'<%s>'%s)); rec(out[-1],i,i+1); i+=1
    return ''.join(out)
if __name__=='__main__':
    src=open(sys.argv[1],encoding='utf8').read()
    for part in re.split(r'^#.*$',src,flags=re.M):
        if part.strip(): print(decode(parse(part)));print()
