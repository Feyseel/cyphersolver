"""Walk Founders Online's 'Preceding / Next between these correspondents' chain for Armstrong <-> Madison through the
Wayback Machine (Founders itself serves a CloudFront challenge to scripts), save each page to fo/<id>.html and record
the documents that contain code groups.  Usage: python founders_crawl.py <start-id> [<start-id> ...]
Output: fo/index.json  {id: {title, ngroups, prev, next}}"""
import re, json, sys, os, time, urllib.request, html

os.makedirs('fo', exist_ok=True)
IDX = 'fo/index.json'
idx = json.load(open(IDX, encoding='utf-8')) if os.path.exists(IDX) else {}


def fetch(doc):
    path = f'fo/{doc}.html'
    if os.path.exists(path) and os.path.getsize(path) > 2000:
        return open(path, encoding='utf-8').read()
    for ts in ('2026', '2025', '2026', '2024', '2025', '2023'):
        url = f'https://web.archive.org/web/{ts}id_/https://founders.archives.gov/documents/Madison/{doc}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            t = urllib.request.urlopen(req, timeout=120).read().decode('utf-8', 'ignore')
        except Exception:
            time.sleep(20)
            continue
        if 'docbody' in t or 'Founders Online' in t:
            open(path, 'w', encoding='utf-8').write(t)
            return t
    return None


def body_text(t):
    m = re.search(r'<div class="docbody">(.*?)(?:<div class="(?:ptdoc|note)|Index Entries)', t, re.S)
    s = m.group(1) if m else t
    s = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)))


def links(t):
    pre = re.search(r'<dt>Preceding</dt><dd><a href="/documents/Madison/(\d\d-\d\d-\d\d-\d+)', t)
    nxt = re.search(r'<dt>Next</dt><dd><a href="/documents/Madison/(\d\d-\d\d-\d\d-\d+)', t)
    return (pre.group(1) if pre else None), (nxt.group(1) if nxt else None)


if __name__ == '__main__':
    queue = sys.argv[1:]
    limit = 200
    while queue and limit:
        doc = queue.pop(0)
        if doc in idx:
            continue
        limit -= 1
        t = fetch(doc)
        if not t:
            idx[doc] = {'ok': False}
            print(doc, 'MISSING', flush=True)
            continue
        title = re.search(r'<title>(.*?)</title>', t, re.S)
        title = html.unescape(title.group(1)).strip() if title else ''
        b = body_text(t)
        groups = re.findall(r'(?<![\d,$£])\b\d{1,4}\b(?![,\d]|th|st|d\b)', b)
        pre, nxt = links(t)
        idx[doc] = {'ok': True, 'title': title[:100], 'ngroups_rough': len(groups), 'prev': pre, 'next': nxt}
        print(doc, '|', title[:80], '| rough groups', len(groups), '|', pre, nxt, flush=True)
        json.dump(idx, open(IDX, 'w', encoding='utf-8'), indent=1)
        for l in (pre, nxt):
            if l and l not in idx and l not in queue:
                queue.append(l)
        time.sleep(1)
