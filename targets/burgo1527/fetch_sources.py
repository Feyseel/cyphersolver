"""Retrieve target sources without exposing the shared DECODE session."""
from pathlib import Path
import urllib.request, re, json
ROOT=Path(__file__).resolve().parent
(ROOT/'sources').mkdir(exist_ok=True)
(ROOT/'img').mkdir(exist_ok=True)
cookie_path=ROOT.parent/'bordeaux/decode/cookie.txt'
cookie=re.sub(r'^cookie:\s*','',cookie_path.read_text(encoding='utf-8').strip(),flags=re.I)
url='https://de-crypt.org/decrypt-web/RecordsView/9970'
def fetch(url,auth=False):
    headers={'User-Agent':'Mozilla/5.0'}
    if auth: headers['Cookie']=cookie
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=45) as r:
        data=r.read()
        if 'forbidden' in r.headers.get('Content-Disposition','').lower():
            raise RuntimeError('Access denied')
        return data
html=fetch(url,True)
(ROOT/'sources/record9970.html').write_bytes(html)
names=sorted(set(re.findall(r'filesrv/\?file=TH_([A-Za-z0-9_.]+)',html.decode('utf-8','replace'))))
print('Images:',names,flush=True)
for name in names:
    data=fetch('https://de-crypt.org/decrypt-custom/filesrv/?file='+name,True)
    (ROOT/'img'/name).write_bytes(data)
    print(name,len(data),flush=True)
