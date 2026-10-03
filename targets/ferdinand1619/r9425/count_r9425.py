"""Measure the reading of R9425: cipher tokens read as sense / all cipher tokens.

Letter words count as read token by token; DOUBTFUL names the words where one token is a misreading or an
illegible sign (that token is counted unread, the rest read). Nomenclator groups count as read only when
codes.txt marks them null or fixed; 'probable' values are not counted. Single key letters standing alone
(L., E., M.) are initials and count as read. Also prints a German language-model check on the decrypt.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..')); sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm
from solve import parse, is_code
from decode import dec, K
from decode_r9425 import load_codes

# word as decoded -> number of tokens in it not read
DOUBTFUL = {'gl': 1,            # P1.16 'ire gl': 30 where the formula is 'ire L.'
            'freundt?': 1,      # P1.18 illegible sign (XX)
            'koni?': 1,         # P3.05 unclear sign (XX)
            'ire?': 1,          # P2.31 sign lost in the gutter
            'deuntion': 1,      # P2.02-03 devotion: 40 where 66 is wanted
            'laisoen': 1,       # P2.19 laisten: 42 for 52
            'hinaufscticken': 1,  # P6.04 hinaufschicken: 52 for 32
            'befegch': 1,       # P3.26 befelch: 30 for 36
            'unuerhoafenden': 1,  # P2.30 unverhofenden: 70 for 20
            'ai': 2}            # P2.30 'da ai...' : word cut by the gutter

if __name__ == '__main__':
    C = load_codes()
    P = parse(os.path.join(HERE, 'transcription.txt'))
    tok = read = ctok = cread = 0; text = []; doubt = []; open_codes = {}
    for lid, items in P:
        for it in items:
            if it[0] != 'word': continue
            w = it[1]
            if is_code(w):
                for t in w:
                    if t in K and len(w) == 1: tok += 1; read += 1; continue
                    ctok += 1
                    if t in C and C[t][1] in ('null', 'fixed'):
                        cread += 1
                        if C[t][0] not in ('-', ''): text.append(C[t][0].split()[0])
                    else: open_codes[t] = open_codes.get(t, 0) + 1
            else:
                d = dec(w); tok += len(w); bad = DOUBTFUL.get(d, 0)
                read += len(w) - bad; text.append(d)
                if bad: doubt.append((lid, d))
    total, allread = tok + ctok, read + cread
    print(f'letter tokens {tok}, read {read}')
    print(f'code tokens   {ctok}, read {cread} (nulls and fixed values)')
    print(f'all tokens    {total}, read {allread}  = {allread / total:.1%}')
    print('doubtful words:', ', '.join(f'{l} {d}' for l, d in doubt))
    print('open groups:', ', '.join(f'{k}x{v}' for k, v in sorted(open_codes.items(), key=lambda x: -x[1])),
          f'({sum(open_codes.values())} tokens)')
    s = ' '.join(text)
    m = lm.load('de-1500s')
    print('lm de-1500s per_char', round(m.per_char(' ' + s + ' '), 3))
    try: print('best_language', lm.best_language(s))
    except Exception as e: print('best_language failed:', e)
