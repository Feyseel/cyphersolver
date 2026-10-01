"""R118 (ASV Segr. Stato Spagna 10 f. 365) with the Spain 'cifra ordinaria' key.
The token list is A. Devadas's reading of the scan (email and report of 1 Oct 2026); lines 1-3 and 5 were compared with the image here
(targets/ormanetto1576/decode/l*.jpg). Each token is decoded with the key and compared with his plaintext, so a wrong token or a wrong key shows.
Notation: 'd.' dotted digit, '0d' dotted zero opening d, 'd0' undotted zero closing d, '7:' two dots, [x] code group, '|' word end (stroke)."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ormanetto1573'))
import dec_aj as D
KEY = dict(D.KEY)
fmt = lambda g: __import__('re').sub(r'(\d)\.', lambda m: m.group(1) + '̇', g.replace(':', '̈').replace('.', '.')) if '.' in g or ':' in g else g
LINES = [
 ("20 7. 05 3 07 40 | 4. 2. 08 | [15] | 04 3 | 03 07 03 02 05 60", "scrita ali 15 di otobre"),
 ("3 80 | 90 10 6. 07 3 03 | 40 | 7. 03 2 10 90 3 50 40 9 6 | 50 03 80", "il nuntio a comunicato col"),
 ("9. 60 50 05 60 9 40 05 3 03 | 30 60 05 60 09", "secretario perez"),
 ("[6.11] | [2.44] | [66] | [9.11]", "[tutto] [quello] [che] [V.S.Ill.ma]"),
 ("20 7. 05 3 10 60 50 03 90 | 2. 40 | 50 3 06 05 40", "scriue con la cifra"),
 ("04 3 | [19] | 04 3 | 9. 60 9 5. 01 4 05 60", "di 19 di setembre"),
 ("3 80 | [5.2.2] 80 60 | 20 60 7: 05 60 9 40 05 3 03", "il [qua]le segretario"),
 ("40 | 30 05 6 2 60 9. 03 | 04 3 | 04 40 05 90 60 | 50 6 90 9 6 | 40 80 | [3.44]", "a promeso di darne conto al [Re]"),
 ("[3] | 04 3 | 30 05 6 7. 10 05 40 05 90 60 | 05 3 9. 30 6 9. 07 40", "[et] di procurarne risposta"),
 ("7 60 2. 40 | [5.2.2] 80 60 | [9.11] | 9. 40 05 4.", "de la [qua]le [V.S.Ill.ma] sara"),
 ("30 03 08 | 9. 10 4 3 07 03 | 40 10 3 9. 40 07 40", "poi subito auisata"),
 ("20 07 50 09 30 2.", "nulls"),
]
def tok_letter(t):
    if t.startswith('[') : return None
    if t.startswith('0') and len(t) == 2: return KEY['0.' + t[1]]
    return KEY[t]
def main():
    ok = bad = 0; groups = []; reveal = []
    for toks, plain in LINES:
        got = ''
        for w in toks.split('|'):
            for t in w.split():
                if t.startswith('['): got += t; groups.append((t.strip('[]'), 'code'))
                else: got += tok_letter(t); groups.append((t, 'let'))
            got += ' '
        got = got.strip()
        want = plain
        # codes are compared by position only; letters compared exactly
        lt = ''.join(c for c in got if c.isalpha()); wt = ''.join(c for c in want if c.isalpha()) if '[' not in want else None
        for w in toks.split('|'):
            for t in w.split():
                if t.startswith('['):
                    c = t.strip('[]'); name = {'15': '15', '19': '19', '3': 'et', '5.2.2': 'qua'}.get(c) or D.CODES.get(c, '?')
                    reveal.append({'g': fmt(c.replace('15', '15̅').replace('19', '19̅')) if c in ('15', '19') else fmt(c), 'p': name, 'cls': 'code'})
                else:
                    reveal.append({'g': ('0̇' + t[1] if t[0] == '0' and len(t) == 2 else fmt(t)), 'p': tok_letter(t)})
            reveal.append({'g': '', 'p': ' ', 'cls': 'plain'}) if plain != 'nulls' else None
        print(('ok  ' if (wt is None or lt == wt or plain == 'nulls') else 'DIFF'), toks, '->', got)
        if wt is None or lt == wt or plain == 'nulls': ok += 1
        else: bad += 1
    print(ok, 'lines consistent,', bad, 'differ')
    if '--reveal' in sys.argv:
        # the last 6 groups are the final nulls
        for t in reveal[-6:]: t['cls'] = 'null'
        d = {'slug': 'ormanetto1576', 'anchor': 'the-reading', 'title': 'Madrid, 15 October: the whole cipher on f. 365',
             'caption': "The six lines of figures on f. 365 (Archivio Apostolico Vaticano, Segr. Stato Spagna 10, DECODE R118), read with the Spain nunciature's ordinary cipher. Tokens as read by A. Devadas; lines 1-3 and 5 compared with the scan here. The leaf's own Italian note is the contemporary decipherment, without the dateline.",
             'unit': 'signs', 'key_note': 'Two signs per letter; undotted 0 closes the digit before it, dotted 0 opens the next; no h, no double letters, u for v; groups with an overline are numbers; 6̇1 1, 2̇44, 66, 9̇11 and 3̇44 are code groups. The last six signs are nulls.',
             'tokens': reveal}
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'reveal', 'ormanetto1576.json')
        json.dump(d, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1); print(len(reveal), 'tokens')
if __name__ == '__main__': main()
