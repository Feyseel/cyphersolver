"""Apply the R1892 6x6 digit-pair key and R1892's word-sign table to a transcription.

usage: python apply.py transcription_p3.txt            -> decrypt, word signs in [brackets]
       python apply.py --measure transcription_p*.txt  -> token counts read / unread
Signs with no value are printed as <label>.
"""
import sys, re

K = {'11':'t','12':'w','13':'y','14':'x','15':'l','21':'z','22':'o','23':'k','24':'f','25':'m','31':'d','32':'n',
     '33':'v','34':'h','35':'b','41':'g','42':'u','43':'a','44':'s','45':'p','51':'c','52':'r','53':'y','54':'q',
     '55':'i','65':'e'}

# word signs: transcriber label -> (value, grade).  H = fixed by the p1 clear text (or R1892 'de');
# M = probable (several contexts agree, or a sibling occurrence agrees); I = from context only.
SIGNS = {
    '<theta>': ('de', 'H'),
    # R1892 second pass, 21 Sept 2026
    '<gamma>': ('zich', 'M'), '<c-symbol>': ('te', 'M'), '<G>': ('ik', 'M'),
    # 2 Oct 2026: R2242's values tried on R1892's signs (NOTES, "R2242 values applied")
    '<bar-H>': ('zoo', 'M'), '<gt>': ('als', 'M'), '<lambda>': ('dat', 'M'), '<parallelogram>': ('brief', 'H'), '<box>': ('lettre', 'M'),
    '<perp>': ('om', 'M'), '<8>': ('zijn', 'I'),
    # found while doing so: aan-geboden, aan-geeven, aan-komst
    '<f>': ('aan', 'M'),
    # 3 Oct 2026: alle de [voor]stellingen; my niet [voor]gesteld
    '<P>': ('voor', 'M'),
}
SKIP = {'<struck>'}
# Page 1 is French: the writer uses pair 12 (w in his Dutch) for the z of -ez (pourrez, avez); see the key table in
# NOTES. FRENCH is switched on for transcription_p1.txt (and by measure_sense.py for French models).
KFR = dict(K, **{'12': 'z'})
FRENCH = False
FRENCH_FILES = {'transcription_p1.txt'}

import os
STRICT = os.environ.get('STRICT') == '1'   # STRICT=1: I-grade (context-only) sign values count as unread

TOK = re.compile(r'\[[^\]]*\]|<[^>]*>|\([^)]*\)|\S+')


def tokens(line):
    if line.lstrip().startswith('#'):
        return
    for t in TOK.findall(line):
        u = t.rstrip('?')
        m = re.fullmatch(r'([1-6]{2})>([1-6]{2})', u)
        if m:                     # writer's slip, emended: 'written>read' (listed in NOTES, grade M)
            u = m.group(2)
        if re.fullmatch(r'[1-6]{2}', u):
            yield 'pair', u, (KFR.get(u) if FRENCH else K.get(u))
        elif t in SKIP:
            yield 'note', t, None
        elif t.startswith('[sign:') or (t.startswith('<') and t.endswith('>')):
            lab = t[6:-1] if t.startswith('[sign:') else t
            v = SIGNS.get(lab)
            if v and STRICT and v[1] == 'I':
                v = None
            yield 'sign', lab, (v[0] if v else None)
        elif re.fullmatch(r'[1-6?]{2}|\?\d|\d\?', u) or (t.startswith('[') and 'ink blot' in t):
            yield 'pair', u, None
        else:
            yield 'note', t, None


def decrypt(line):
    out = []
    for kind, lab, v in tokens(line):
        if kind == 'pair':
            out.append(v if v else '(' + lab + ')')
        elif kind == 'sign':
            out.append(' [' + v + '] ' if v else ' ' + (lab if lab.startswith('<') else '<' + lab + '>') + ' ')
        else:
            out.append(' ' + lab + ' ')
    return re.sub(' +', ' ', ''.join(out)).strip()


def measure(files):
    tot = read = 0
    for f in files:
        a = b = 0
        for line in open(f, encoding='utf8'):
            for kind, lab, v in tokens(line):
                if kind == 'note':
                    continue
                a += 1; b += v is not None
        print(f'{f}: {b}/{a}')
        tot += a; read += b
    print(f'total: {read}/{tot} = {read/tot:.3f}')


if __name__ == '__main__':
    import os as _os
    if sys.argv[1] != '--measure':
        FRENCH = _os.path.basename(sys.argv[1]) in FRENCH_FILES
    if sys.argv[1] == '--measure':
        measure(sys.argv[2:])
    else:
        for line in open(sys.argv[1], encoding='utf8'):
            print(line.rstrip() if line.lstrip().startswith('#') else decrypt(line))
