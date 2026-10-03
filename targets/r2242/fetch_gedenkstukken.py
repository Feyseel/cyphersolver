"""Fetch the OCR text of Colenbrander, Gedenkstukken I and II (1905-06, public domain) from
resources.huygens.knaw.nl into gs_corpus/ (git-ignored). Used by measure_sense.py as a 1795-spelling Dutch/French
word list. usage: python fetch_gedenkstukken.py"""
import json, os, re, html, urllib.request, concurrent.futures as cf
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gs_corpus')
os.makedirs(D, exist_ok=True)

def pages(src):
    f = os.path.join(D, f'pages{src}.json')
    if not os.path.exists(f):
        u = f'https://resources.huygens.knaw.nl/retroboeken/gedenkstukken/pages.json?source={src}'
        open(f, 'wb').write(urllib.request.urlopen(u, timeout=60).read())
    return json.load(open(f, encoding='utf8'))[src]

def get(p):
    out = os.path.join(D, f"gs{p['source']}_{int(p['page_index']):04d}.txt")
    if os.path.exists(out):
        return
    for _ in range(3):
        try:
            t = urllib.request.urlopen(p['html_url'], timeout=60).read().decode('utf8', 'replace')
            t = re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]*>', ' ', t)))
            open(out, 'w', encoding='utf8').write(t); return
        except Exception:
            pass

if __name__ == '__main__':
    todo = pages('1') + pages('2')
    with cf.ThreadPoolExecutor(6) as ex:
        list(ex.map(get, todo))
    print(len(os.listdir(D)) - 2, 'pages')
