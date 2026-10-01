"""docs/reveal/ormanetto1573.json: the opening of passage B (f. 304r) decoded sign by sign with the Spain 'cifra ordinaria' key (dec_aj.py)."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dec_aj as D
DOT = '\u0307'
def show(g):
    return re.sub(r'(\d)\.', lambda m: m.group(1) + DOT, g.replace('.', DOT) if False else g).replace('0' + '.', '0' + DOT)
def fmt(g):
    out = ''; i = 0
    while i < len(g):
        out += g[i]
        if i + 1 < len(g) and g[i + 1] == '.': out += DOT; i += 1
        i += 1
    return out
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r116_cipher.txt'), encoding='utf8').read()
parts = [p for p in re.split(r'^#.*$', src, flags=re.M) if p.strip()]
pr = []; D.decode(D.parse(parts[1]), pr)
toks = []; text = ''
for g, p in pr:
    if p == ' ':
        toks.append({'g': g[0] + '+', 'p': '\u00b7', 'cls': 'null'}); text += ' '
    elif p.startswith('['):
        toks.append({'g': fmt(g), 'p': p.strip('[]'), 'cls': 'code'}); text += p
    else:
        toks.append({'g': fmt(g), 'p': p}); text += p
    if text.rstrip().endswith('pitigliano'): break
d = {'slug': 'ormanetto1573', 'anchor': 'the-reading',
     'title': 'Madrid, spring 1573: the opening of passage B',
     'caption': "Passage B of Philip II's letter copied for the Cardinal of Como, f. 304r, Archivio Apostolico Vaticano (DECODE R116), decoded from our transcription with the Spain nunciature's ordinary cipher. Spelling is as enciphered: no h, no double letters, et written as a single sign.",
     'unit': 'signs', 'key_note': 'Two signs per letter (a: 40, 4\u0307; b: 4, 0\u03072 ...), undotted 0 closes the digit before it, dotted 0 opens the next; 2, 4 or 5 with a cross-stroke ends a word; a few code groups for common words. Key reconstructed by A. Devadas (Oct 2026) and checked here.',
     'tokens': toks}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'reveal', 'ormanetto1573.json')
json.dump(d, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(toks), text)
