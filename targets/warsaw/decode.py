"""Decode DECODE R1408 (Warsaw, 24 Dec 1627) with the recovered key.
Alphabet: odd 13-33 = a b c d e f g h i l m, even 14-32 = n o p q r s t u (x) z.
Letter pairs are consonant alternates; 01-09 and 40-50 are syllables/particles; a and m are nulls;
three-digit groups are nomenclator codes (glosses in brackets are inferred from context, not read)."""
import sys
ALPHA = {}
for k, ch in zip(range(13, 34, 2), 'abcdefghilm'): ALPHA['%02d' % k] = ch
for k, ch in zip(range(14, 33, 2), 'nopqrstuxz'): ALPHA['%02d' % k] = ch
PAIRS = {'ll': 't', 'th': 'l', 'zg': 'r', 'lu': 'd', 'fi': 'n', 'pr': 'ff'}
SYLL = {'01': 'si', '05': 'non', '06': 'ne', '09': 'de', '40': 'con', '41': 'al', '42': 'la', '43': 'di',
        '44': 'de', '45': 'da', '46': 'con', '47': 'che', '50': 'se',
        '03': '{03}', '04': '{04}'}
CODES = {'100': '[100]', '113': '[113]', '120': '[120]', '123': '[123]', '151': '[151]',
         '154': '[154]', '157': '[157]', '159': '[159]', '160': '[160]', '223': '[223]'}
GLOSS = {'100': 'Regina?', '113': '?', '120': 'V.S.Ill.ma (addressee)', '123': 'Ser.mi?', '151': 'ancora?',
         '154': 'come', '157': '?', '159': '?', '160': 'questa', '223': '?'}
NULLS = {'a', 'm', 'p', 'n'}

# Corrections to Tomokiyo's transcription from the DECODE image (decode/IMG_R1408_I6588_P1.png, checked 2 Oct 2026):
# line 2 'a 12 o m' is the code group 120 (the clerk's 0 and o are one shape; the same '1-2-0' as line 8's 120);
# line 10 has a symbol between 26 and 33 (Tomokiyo's double space), an i (29): 'stimato', not 'stmato'.
IMAGE_FIX = [('a 12 o m', 'a 120 m'), ('24 26  33 13', '24 26 29 33 13')]

def tokens(image=True):
    s = open('ct.txt').read()
    if image:
        for a, b in IMAGE_FIX:
            assert a in s, a
            s = s.replace(a, b)
    s = ' '.join(s.split())
    for pr in ['l l', 'z g', 'f i', 'p r', 'l u', 't h']: s = s.replace(pr, pr.replace(' ', ''))
    return s.split()

def decode(mark_nulls=False, gloss=False, image=True):
    out = []
    for t in tokens(image):
        if t in NULLS: out.append('|' if mark_nulls else ''); continue
        if t in PAIRS: out.append(PAIRS[t])
        elif t in CODES: out.append(' [' + t + (':' + GLOSS[t] if gloss else '') + '] ')
        elif t in SYLL: out.append(SYLL[t])
        elif t in ALPHA: out.append(ALPHA[t])
        else: out.append('<' + t + '>')
    return ''.join(out)

if __name__ == '__main__':
    print(decode(mark_nulls='-n' in sys.argv, gloss='-g' in sys.argv, image='-t' not in sys.argv))
