"""Bring the System A' v2 transcriptions to one code set and one token stream per letter.

Output sysA2/<rec>.tok: lines 'Pn.NN tokens', one character per sign; '|' separates runs (clear text, code
signs F.G. and K, page breaks are not joined across); clear text kept in [..].
Merges (one sign written as two codes): jo -> ʝ (ʒo, h), a+ -> β, mg -> ɱ, Ro -> ʀ ('und'); R9408 c# -> ꝁ ('ck');
w3v / wUv before the F.G. sign -> ẽ ('eur', the formula glossed on R9427).
R9409 has its own codes (r9409/signs.md); they are mapped to the R9410 codes where the shape is the same.
  python prep.py
"""
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = {
    'r9408': '../r9408/transcription_v3.txt',
    'r9409': '../r9409/transcription_v2.txt',
    'r9410': '../sysA/r9410_v2.txt',
    'r9413': '../r9413/transcription_v2.txt',
    'r9427': '../r9427/transcription_v2.txt',
    'r9410b': '../r9410/transcription_p3p6.txt',   # ff.246-247, the Latin letter (X and K kept as plain signs)
    'r9407': '../../augurelio1535/pass2/transcription.txt',
}
# R9409 code -> R9410 code (same shape); unique R9409 shapes get their own character
MAP9409 = {'V': 'v', 'Y': 'y', 'P': 'n', 'b': 'd', 'd': 'ð', 'c': 'ç', 'C': 'c', 'S': 'X', 'T': 'Ŧ',
           'z': 'j', 'g': 'ɣ', 'Q': 'Θ', 'O': 'ô', 'f': 'ʃ', 'u': 'ü', 'e': 'ę', 'l': 'ł', 'n': 'ň', 'k': 'ķ',
           'I': 'ı', 'R': 'ŗ', 'a': 'ą', 'y': 'ÿ', 's': 'ś', 'F': 'ƒ', 'K': 'K'}
CODE_FG = {'r9410b': '␀', 'r9408': 'X', 'r9409': 'X', 'r9410': 'X', 'r9413': 'X', 'r9427': 'X', 'r9407': 'Z'}
CODE_K = {'r9410b': '␁', 'r9408': 'K', 'r9409': 'K', 'r9410': 'K', 'r9413': '$', 'r9427': 'K', 'r9407': 'V'}

def lines_of(rec):
    page = 'P?'
    for l in open(os.path.join(HERE, SRC[rec]), encoding='utf8'):
        if l.startswith('=='):
            m = re.search(r'P(\d+)', l); page = 'P' + m.group(1) if m else page; continue
        m = re.match(r'(\d\d)\s+(.*)', l.rstrip('\n'))
        if m: yield page, m.group(1), m.group(2)

def tokenize(rec, s):
    parts = re.split(r'(\[[^\]]*\])', s)
    out = ''
    for p in parts:
        if p.startswith('['): out += ' ' + p + ' |'; continue
        if rec == 'r9409':
            p = re.sub(r'\.\d+\.', '¦', p)                     # clear numbers .24.
            p = p.replace('^', '').replace('-', '')
            p = ''.join(MAP9409.get(c, c) for c in p)
        p = re.sub(r'\([^)]*\)', '', p)                    # transcriber's notes, e.g. '(last four signs underlined)'
        if rec == 'r9427':
            p = re.sub(r'\{(?:left[- ]margin[^:]*): ([^}]*)\}', lambda m: m.group(1).replace(' ', ''), p)   # marginal insertions
            p = re.sub(r'\{signature[^}]*\}', '', p)
            p = p.replace('{A}', 'Å').replace('{', '').replace('}', '')
            p = p.replace('?', '')                            # '?' marks the sign before it as doubtful
        elif rec == 'r9407':
            p = p.replace('?', '')
        else:
            p = re.sub(r'\{[^}]*\}', '', p)                    # struck-through signs (R9413)
            p = p.replace('?', '¿')                           # an unread sign
        p = re.sub(r'[\s.:,;|\-"()=!*~>]', '', p) if rec != 'r9413' else re.sub(r'[\s.:,;|\-"()=~>]', '', p)
        if rec == 'r9408':
            p = p.replace('cX', 'c#')                         # split.md: the X after c is the slanted c#-type cross
            p = p.replace('c#', 'ꝁ')                          # c# = ck (44x; the # after c is never g)
        p = p.replace('jo', 'ʝ').replace('a+', 'β').replace('mg', 'ɱ').replace('Ro', 'ʀ')
        p = re.sub(r'w[3U]v(q?)' + re.escape(CODE_FG[rec]), 'ẽ' + r'\1' + CODE_FG[rec], p)   # 'eur(n) F.G.' (R9427 gloss: w3vX = ewr F.G.)
        p = p.replace(CODE_FG[rec], '|F|').replace(CODE_K[rec], '|K|')
        out += p.replace('¦', '|')
    return out

if __name__ == '__main__':
    from collections import Counter
    for rec in SRC:
        res, cnt = [], Counter()
        for page, no, s in lines_of(rec):
            t = tokenize(rec, s); res.append(f'{page}.{no} {t}')
            cnt.update(c for c in re.sub(r'\[[^\]]*\]|\|F\||\|K\|', '', t) if c not in ' |')
        open(os.path.join(HERE, rec + '.tok'), 'w', encoding='utf8').write('\n'.join(res) + '\n')
        print(rec, sum(cnt.values()), ' '.join(f'{k}{v}' for k, v in cnt.most_common()))
