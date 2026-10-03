"""Apply the R1892 6x6 digit-pair key and the R2242 word-sign table to a transcription.

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
    'circle with dot': ('de', 'H'), '<theta>': ('de', 'H'),
    # page-1 clear text under the cipher
    '>': ('als', 'H'), '> angle': ('als', 'H'), 'parallelogram': ('brief', 'H'),
    'δ-like loop': ('genoomen', 'H'), 'H-bar': ('zoo', 'H'), 'long S': ('moeten', 'H'),
    'Y with cross-stroke': ('zee', 'H'), 'circle with cross on top ♁': ('erfprins', 'H'),
    '÷ bar with dots': ('zoo', 'H'), 'ɣ hook with long tail': ('zulks', 'H'), '§': ('maar', 'H'),
    'section mark §': ('maar', 'H'), 'v-like': ('tot', 'H'), 'crossed loop, 8 with bar': ('zijn', 'H'),
    'long slash/ʃ': ('zelfde', 'H'),
    # read from context 30 Sept 2026
    'script L': ('uit', 'I'), 'looped L/script ℒ': ('uit', 'I'), 'flagged D': ('van', 'M'), 'inverted triangle with stroke': ('van', 'M'),
    'phi/circle with stroke': ('frankrijk', 'I'), 'phi/circle with vertical stroke': ('frankrijk', 'I'),
    '⊥ inverted T': ('om', 'M'),
    # second pass 2 Oct 2026
    'Lambda/angle': ('dat', 'M'), 'Lambda': ('dat', 'M'), 'slashed Lambda': ('dat', 'I'),
    'crossed Lambda': ('dat', 'I'), 'infinity': ('daar', 'M'), '∞': ('daar', 'M'),
    '< angle': ('naar', 'I'), 'check-mark over bar': ('zonder', 'M'), 'crossed e with stroke': ('zijn', 'M'),
    'X/cross': ('weinig', 'I'), 'crossed diamond': ('voor', 'I'), 'Y with crossbar': ('ik', 'I'), 'crossed x/dagger': ('al', 'I'), '&': ('engeland', 'I'),
    '+ cross': ('mogelyk', 'I'), 'crossed Y/lambda': ('dez', 'I'),
}

TOK = re.compile(r'\[[^\]]*\]|<[^>]*>|\([^)]*\)|\S+')


def tokens(line):
    if line.lstrip().startswith('#'):
        return
    for t in TOK.findall(line):
        u = t.rstrip('?')
        if re.fullmatch(r'[1-6]{2}', u):
            yield 'pair', u, K.get(u)
        elif t.startswith('[sign:') or (t.startswith('<') and t.endswith('>')):
            lab = t[6:-1] if t.startswith('[sign:') else t
            v = SIGNS.get(lab)
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
            out.append(' [' + v + '] ' if v else ' <' + lab + '> ')
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
    if sys.argv[1] == '--measure':
        measure(sys.argv[2:])
    else:
        for line in open(sys.argv[1], encoding='utf8'):
            print(line.rstrip() if line.lstrip().startswith('#') else decrypt(line))
