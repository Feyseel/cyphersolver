"""R1409 (Kt. 14 Fasc. 20 f. 178): is it in the R1408 key?

Parses DECODE's transcription (decode/DOC_R1409_D3583_3583.txt, transcriber MEG, 2020) into r1409_ct.txt
(one line per manuscript line, tokens separated by spaces, '_' suffix = underlined in the MS), decodes the
two-figure groups with the R1408 alphabet, and scores the result against 2000 random keys over the same figures.
"""
import os, re, sys, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

def parse():
    t = open(os.path.join(HERE, 'decode', 'DOC_R1409_D3583_3583.txt'), encoding='utf-8').read()
    body = t.split('#IMAGE NAME: 6589.png', 1)[1]
    lines = []
    for line in body.splitlines():
        if line.startswith('#'):
            lines.append(line.strip()); continue
        if not line.strip(): continue
        toks = []
        for g in re.split(r'\s{2,}', line.strip()):
            u = '__' in g
            toks.append(g.replace('__', '').replace(' ', '') + ('_' if u else ''))
        lines.append(' '.join(toks))
    return lines

def tokens(lines):
    return [t.rstrip('_') for l in lines if not l.startswith('#') for t in l.split()]

ALPHA = {}
for k, ch in zip(range(13, 34, 2), 'abcdefghilm'): ALPHA['%02d' % k] = ch
for k, ch in zip(range(14, 33, 2), 'nopqrstuxz'): ALPHA['%02d' % k] = ch

def dec(toks, key):
    return ''.join(key.get(t, '') for t in toks)

if __name__ == '__main__':
    lines = parse()
    open(os.path.join(HERE, 'r1409_ct.txt'), 'w').write('\n'.join(lines) + '\n')
    toks = tokens(lines)
    c = collections.Counter(toks)
    print('tokens', len(toks), 'distinct', len(c))
    print('two-figure share', sum(v for k, v in c.items() if len(k) == 2) / len(toks))
    pt = dec(toks, ALPHA)
    print('R1408 key on R1409:', pt[:300])
    for mid in ['it-cinquecento', 'la', 'de-1640s', 'fr-1600-letters', 'es-golden-age']:
        m = lm.load(mid, order=4, spaces=False)
        norm = 'latin' if mid == 'la' else 'early'
        s = m.per_char(lm.norm(pt, norm))
        rnd = []
        rng = random.Random(1)
        figs = list(ALPHA); letters = [ALPHA[f] for f in figs]
        for _ in range(500):
            rng.shuffle(letters)
            rnd.append(m.per_char(lm.norm(dec(toks, dict(zip(figs, letters))), norm)))
        rnd.sort()
        print('%-16s R1408 key %.3f  random median %.3f  max %.3f  rank %d/500' % (
            mid, s, rnd[250], rnd[-1], sum(r >= s for r in rnd)))
    # same-key control: R1408 itself
    sys.path.insert(0, HERE); os.chdir(HERE)
    import decode as d8
    m = lm.load('it-cinquecento', order=4, spaces=False)
    t8 = [t for t in d8.tokens() if t in ALPHA]
    print('control R1408 own figures, R1408 key: %.3f' % m.per_char(lm.norm(dec(t8, ALPHA), 'early')))
    print('control R1408 full decode: %.3f' % m.per_char(lm.norm(re.sub(r'[\[\]{}0-9?:.A-Za-z]*[\[{][^\]}]*[\]}]', '', d8.decode()), 'early')))
