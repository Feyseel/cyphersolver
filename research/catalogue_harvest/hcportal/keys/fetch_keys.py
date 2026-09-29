"""Harvest HCPortal cipher-key records (api/cipher-keys/<id>) into keys/<id>.json."""
import json, os, sys, urllib.request, urllib.error
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36',
     'Origin': 'https://crypto.hcportal.eu', 'Referer': 'https://crypto.hcportal.eu/'}
miss = 0
for i in range(1, 2000):
    out = f'{i}.json'
    if os.path.exists(out):
        continue
    try:
        r = urllib.request.urlopen(urllib.request.Request(f'https://api.hcportal.eu/api/cipher-keys/{i}', headers=H), timeout=30)
        d = r.read()
        json.loads(d)
        open(out, 'wb').write(d)
        miss = 0
    except Exception as e:
        miss += 1
        if miss > 60:
            break
print('done', i)
