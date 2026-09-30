"""Add a quotation from each decipherment to the solutions list, laid out as a letter (George Lasry, 30 Sept 2026).

George edits the list in Google Docs, so the sections are not regenerated: this script opens his exported .docx and
inserts a block under each numbered heading (the recipient, the quotation, an English translation when the original
is not English, and the signature line), leaving every other byte of document.xml as it was.

    python papers/lasry/_add_excerpts.py <edited.docx> papers/lasry/excerpts.json <out.docx>

excerpts.json holds one object per item: item (the heading number), to, excerpt, translation, from, place_date.
"""
import json
import re
import sys
import zipfile
from xml.sax.saxutils import escape

INDENT = 720          # twentieths of a point: half an inch either side of the quotation
GREY = '555555'
CJK = re.compile('[　-〿㐀-䶿一-鿿＀-￯]')


def run(text, italic=False, color=None, cjk=False):
    rpr = ''
    if cjk:
        rpr += '<w:rFonts w:eastAsia="SimSun" w:hint="eastAsia"/>'
    if italic:
        rpr += '<w:i w:val="1"/><w:iCs w:val="1"/>'
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    if cjk:
        rpr += '<w:lang w:eastAsia="zh-CN"/>'
    return f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def para(runs, before=0, after=20, jc=None):
    ppr = '<w:keepNext w:val="1"/>'
    ppr += f'<w:spacing w:before="{before}" w:after="{after}" w:lineRule="auto"/>'
    ppr += f'<w:ind w:left="{INDENT}" w:right="{INDENT}"/>'
    if jc:
        ppr += f'<w:jc w:val="{jc}"/>'
    return f'<w:p><w:pPr>{ppr}</w:pPr>{"".join(runs)}</w:p>'


def block(e):
    cjk = bool(CJK.search(e['excerpt']))
    out = []
    if e.get('to'):
        out.append(para([run(e['to'], italic=True, color=GREY)], before=100))
    out.append(para([run(f'“{e["excerpt"]}”', cjk=cjk)], before=0 if e.get('to') else 100))
    if e.get('translation'):
        out.append(para([run('Translation: ', color=GREY),
                         run(f'“{e["translation"]}”', italic=True, color=GREY)]))
    # the place and date wrap as one unit, so a long signature never leaves the year alone on a line
    sig = ', '.join(x for x in (e['from'], (e.get('place_date') or '').replace(' ', ' ')) if x)
    out.append(para([run(sig)], after=140, jc='right'))
    return ''.join(out)


def heading_number(p):
    if '<w:pStyle w:val="Heading3"/>' not in p:
        return None
    text = ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', p))
    m = re.match(r'\s*(\d+)\.\s', text)
    return int(m.group(1)) if m else None


def main(src, excerpts, dst):
    items = {e['item']: e for e in json.load(open(excerpts, encoding='utf-8'))}
    with zipfile.ZipFile(src) as z:
        xml = z.read('word/document.xml').decode('utf-8')
        done, pieces, pos = set(), [], 0
        for m in re.finditer(r'<w:p\b[^>]*>.*?</w:p>', xml, re.S):
            n = heading_number(m.group(0))
            if n in items:
                pieces += [xml[pos:m.end()], block(items[n])]
                pos = m.end()
                done.add(n)
        pieces.append(xml[pos:])
        missing = sorted(set(items) - done)
        if missing:
            sys.exit(f'no heading found for items {missing}')
        with zipfile.ZipFile(dst, 'w') as out:
            for info in z.infolist():
                data = ''.join(pieces).encode('utf-8') if info.filename == 'word/document.xml' else z.read(info)
                out.writestr(info, data, compress_type=info.compress_type)
    print(f'{len(done)} quotations inserted -> {dst}')


if __name__ == '__main__':
    main(*sys.argv[1:4])
