"""Download the HCPortal scans of HStAM 4 h Nr. 1411 (records 496-509) into img/ (git-ignored)."""
import json, glob, os, urllib.request
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120', 'Origin': 'https://crypto.hcportal.eu',
     'Referer': 'https://crypto.hcportal.eu/'}
for f in sorted(glob.glob('img/rec*.json')):
    d = json.load(open(f, encoding='utf8'))['data']
    for g in d['datagroups']:
        for item in g['data']:
            if item.get('type') != 'image':
                continue
            im = item['image']
            url = im.get('original') or im.get('large') or im.get('big')
            out = f"img/{item['title'].replace('__', '_')}_{g['description'][:4]}.jpg"
            if os.path.exists(out):
                continue
            req = urllib.request.Request(url, headers=H)
            open(out, 'wb').write(urllib.request.urlopen(req).read())
            print(d['id'], g['description'], item['title'], url, os.path.getsize(out))
