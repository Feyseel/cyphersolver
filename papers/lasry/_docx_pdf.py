"""Print the solutions list (.docx, as edited by George Lasry in Google Docs) to PDF without Word or LibreOffice.

The .docx body is rendered to HTML with its own paragraph and run formatting (styles.xml, direct formatting, links,
bullets, the two-column source tables, the centred page-number footer) and printed with headless Chrome or Edge.

    python papers/lasry/_docx_pdf.py <in.docx> <out.pdf>
"""
import html
import pathlib
import re
import subprocess
import sys
import tempfile
import zipfile
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS = {'w': W}
BROWSERS = [r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe']


def q(tag):
    return '{%s}%s' % (W, tag)


def on(el):
    """A w:b / w:i style toggle: present and not switched off."""
    return el is not None and el.get(q('val'), '1') not in ('0', 'false')


def pt(twips):
    return float(twips) / 20


class Doc:
    def __init__(self, path):
        z = zipfile.ZipFile(path)
        self.body = etree.fromstring(z.read('word/document.xml')).find('w:body', NS)
        styles = etree.fromstring(z.read('word/styles.xml'))
        self.styles = {s.get(q('styleId')): s for s in styles.findall('w:style', NS)}
        dflt = styles.find('w:docDefaults/w:rPrDefault/w:rPr', NS)
        self.default_rpr = dflt if dflt is not None else etree.Element(q('rPr'))
        rels = etree.fromstring(z.read('word/_rels/document.xml.rels'))
        self.rels = {r.get('Id'): r.get('Target') for r in rels}
        numbering = etree.fromstring(z.read('word/numbering.xml'))
        abstract = {a.get(q('abstractNumId')): a for a in numbering.findall('w:abstractNum', NS)}
        self.lists = {}
        for n in numbering.findall('w:num', NS):
            a = abstract[n.find('w:abstractNumId', NS).get(q('val'))]
            self.lists[n.get(q('numId'))] = {l.get(q('ilvl')): l for l in a.findall('w:lvl', NS)}

    # --- run formatting -------------------------------------------------------------------------------------
    def run_css(self, rprs):
        """Merge rPr elements (lowest priority first) into CSS declarations."""
        css = {}
        for rpr in rprs:
            if rpr is None:
                continue
            f = rpr.find('w:rFonts', NS)
            if f is not None and f.get(q('ascii')):
                css['font-family'] = f"'{f.get(q('ascii'))}', Georgia, 'SimSun', serif"
            for tag, prop, yes, no in (('b', 'font-weight', 'bold', 'normal'), ('i', 'font-style', 'italic', 'normal')):
                el = rpr.find(f'w:{tag}', NS)
                if el is not None:
                    css[prop] = yes if on(el) else no
            u = rpr.find('w:u', NS)
            if u is not None:
                css['text-decoration'] = 'none' if u.get(q('val')) in ('none', None) else 'underline'
            s = rpr.find('w:strike', NS)
            if on(s):
                css['text-decoration'] = 'line-through'
            c = rpr.find('w:color', NS)
            if c is not None and c.get(q('val')) not in (None, 'auto'):
                css['color'] = '#' + c.get(q('val'))
            sz = rpr.find('w:sz', NS)
            if sz is not None:
                css['font-size'] = f"{int(sz.get(q('val'))) / 2}pt"
            va = rpr.find('w:vertAlign', NS)
            if va is not None and va.get(q('val')) in ('superscript', 'subscript'):
                css['vertical-align'] = 'super' if va.get(q('val')) == 'superscript' else 'sub'
                css['font-size'] = 'smaller'
            sc = rpr.find('w:smallCaps', NS)
            if on(sc):
                css['font-variant'] = 'small-caps'
        return css

    def style_chain(self, sid):
        chain = []
        while sid and sid in self.styles:
            chain.append(self.styles[sid])
            based = self.styles[sid].find('w:basedOn', NS)
            sid = based.get(q('val')) if based is not None else None
        return list(reversed(chain))

    def runs(self, p, para_rprs):
        out = []
        for child in p:
            if child.tag == q('r'):
                out.append(self.run(child, para_rprs))
            elif child.tag == q('hyperlink'):
                href = self.rels.get(child.get('{%s}id' % R)) or ('#' + (child.get(q('anchor')) or ''))
                inner = ''.join(self.run(r, para_rprs) for r in child.findall('w:r', NS))
                out.append(f'<a href="{html.escape(href, quote=True)}">{inner}</a>')
            elif child.tag in (q('ins'), q('smartTag'), q('customXml')):
                out.append(self.runs(child, para_rprs))
        return ''.join(out)

    def run(self, r, para_rprs):
        rpr = r.find('w:rPr', NS)
        rstyle = []
        if rpr is not None and rpr.find('w:rStyle', NS) is not None:
            rstyle = [s.find('w:rPr', NS) for s in self.style_chain(rpr.find('w:rStyle', NS).get(q('val')))]
        text = []
        for el in r:
            if el.tag == q('t'):
                text.append(html.escape(el.text or ''))
            elif el.tag == q('tab'):
                text.append('&emsp;')
            elif el.tag in (q('br'), q('cr')):
                text.append('<br>')
        if not text:
            return ''
        css = self.run_css(para_rprs + rstyle + [rpr])
        style = ';'.join(f'{k}:{v}' for k, v in css.items())
        return f'<span style="{style}">{"".join(text)}</span>'

    # --- paragraphs and tables ------------------------------------------------------------------------------
    def para(self, p):
        ppr = p.find('w:pPr', NS)
        sid = ppr.find('w:pStyle', NS).get(q('val')) if ppr is not None and ppr.find('w:pStyle', NS) is not None else 'Normal'
        chain = self.style_chain(sid)
        pprs = [s.find('w:pPr', NS) for s in chain] + [ppr]
        para_rprs = [self.default_rpr] + [s.find('w:rPr', NS) for s in chain]
        css = {'margin': '0'}
        keep = False
        numpr = None
        for x in pprs:
            if x is None:
                continue
            sp = x.find('w:spacing', NS)
            if sp is not None:
                if sp.get(q('before')) is not None:
                    css['margin-top'] = f"{pt(sp.get(q('before')))}pt"
                if sp.get(q('after')) is not None:
                    css['margin-bottom'] = f"{pt(sp.get(q('after')))}pt"
                line = sp.get(q('line'))
                if line and sp.get(q('lineRule'), 'auto') == 'auto' and int(float(line)) != 240:
                    css['line-height'] = f"{1.15 * int(float(line)) / 240:.3f}"
            ind = x.find('w:ind', NS)
            if ind is not None:
                for a, prop in (('left', 'margin-left'), ('start', 'margin-left'), ('right', 'margin-right'), ('end', 'margin-right')):
                    if ind.get(q(a)) is not None:
                        css[prop] = f"{pt(ind.get(q(a)))}pt"
                if ind.get(q('firstLine')) is not None:
                    css['text-indent'] = f"{pt(ind.get(q('firstLine')))}pt"
                if ind.get(q('hanging')) is not None:
                    css['text-indent'] = f"-{pt(ind.get(q('hanging')))}pt"
            jc = x.find('w:jc', NS)
            if jc is not None:
                css['text-align'] = {'both': 'justify', 'start': 'left', 'end': 'right'}.get(jc.get(q('val')), jc.get(q('val')))
            kn = x.find('w:keepNext', NS)
            if kn is not None:
                keep = on(kn)
            if x.find('w:numPr', NS) is not None:
                numpr = x.find('w:numPr', NS)
        bullet = ''
        if numpr is not None:
            lvl = self.lists.get(numpr.find('w:numId', NS).get(q('val')), {}).get(numpr.find('w:ilvl', NS).get(q('val'), '0'))
            if lvl is not None:
                ind = lvl.find('w:pPr/w:ind', NS)
                if ind is not None:
                    css['margin-left'] = f"{pt(ind.get(q('left')))}pt"
                    css['text-indent'] = f"-{pt(ind.get(q('hanging')))}pt"
                bullet = f'<span class="bullet">{html.escape(lvl.find("w:lvlText", NS).get(q("val")))}</span>'
        if keep:
            css['break-after'] = 'avoid'
        # the paragraph mark's own run properties set the height of an empty paragraph
        base = self.run_css(para_rprs)
        for k in ('font-size', 'font-family'):
            if k in base:
                css[k] = base[k]
        body = self.runs(p, para_rprs)
        tag = {'Title': 'h1', 'Heading1': 'h2', 'Heading2': 'h3', 'Heading3': 'h4'}.get(sid, 'p')
        style = ';'.join(f'{k}:{v}' for k, v in css.items())
        return f'<{tag} style="{style}">{bullet}{body or "&#8203;"}</{tag}>'

    def table(self, t):
        widths = [pt(g.get(q('w'))) for g in t.findall('w:tblGrid/w:gridCol', NS)]
        cols = ''.join(f'<col style="width:{w}pt">' for w in widths)
        rows = []
        for tr in t.findall('w:tr', NS):
            cells = ''.join('<td>' + ''.join(self.para(p) for p in tc.findall('w:p', NS)) + '</td>'
                            for tc in tr.findall('w:tc', NS))
            rows.append(f'<tr>{cells}</tr>')
        return f'<table style="width:{sum(widths)}pt"><colgroup>{cols}</colgroup>{"".join(rows)}</table>'

    def html(self, title):
        parts = []
        for el in self.body:
            if el.tag == q('p'):
                parts.append(self.para(el))
            elif el.tag == q('tbl'):
                parts.append(self.table(el))
        base = self.run_css([self.default_rpr])
        css = f"""
@page {{ size: A4; margin: 1in; @bottom-center {{ content: counter(page); font: 8pt Georgia, serif; color: #888888; }} }}
html, body {{ margin: 0; padding: 0; background: #fff; }}
body {{ font-family: {base.get('font-family', 'Georgia, serif')}; font-size: {base.get('font-size', '10.5pt')}; color: #000;
       line-height: normal; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
h1, h2, h3, h4, p {{ font-weight: normal; }}
a {{ color: inherit; text-decoration: none; }}
a span {{ text-decoration: underline; }}
.bullet {{ display: inline-block; width: 18pt; text-indent: 0; }}
table {{ border-collapse: collapse; table-layout: fixed; }}
tr {{ break-inside: avoid; }}
td {{ padding: 0 5.75pt; vertical-align: top; }}
"""
        return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
                f'<style>{css}</style></head><body>' + '\n'.join(parts) + '</body></html>')


def main(src, dst):
    doc = Doc(src)
    title = ''.join(t.text or '' for t in doc.body.find('w:p', NS).iter(q('t'))) or 'Document'
    out = pathlib.Path(dst).resolve()
    tmp = pathlib.Path(tempfile.mkdtemp()) / (out.stem + '.html')
    tmp.write_text(doc.html(title), encoding='utf-8')
    exe = next((b for b in BROWSERS if pathlib.Path(b).exists()), None)
    if not exe:
        sys.exit('no Chrome or Edge found; open ' + str(tmp) + ' and print it to PDF')
    # a throwaway profile, so a browser already open on this machine cannot hold the print job
    profile = tempfile.mkdtemp()
    subprocess.run([exe, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--user-data-dir={profile}',
                    f'--print-to-pdf={out}', tmp.as_uri()], check=True, capture_output=True, timeout=180)
    print(f'{out} ({out.stat().st_size // 1024} KB), from {tmp}')


if __name__ == '__main__':
    main(*sys.argv[1:3])
