"""Morse re-division of the garbled tail (30 Sept 2026).
The received sheet is clear copperplate, so the tail's errors are in transmission. A telegram garbles in Morse:
letter spaces lost (two letters heard as one) or added (one letter heard as two). This re-divides the Morse
elements of a received string into letters, allowing up to MAX boundary changes, and keeps strings that parse
into consonant-vowel syllables and valid telegraph codes with the recovered table.
Usage: python morse_tail.py zpo 2      -> za no = 3263 港 among four valid codes at one change
       python morse_tail.py ngobunibai 4  (no sensible decoding)"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from family import code2ch, CONS, VOW, make_table
base = list(CONS); tbl = make_table(base[8:] + base[:8], list('eaiou'), 'vow', 1)
M = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-',
     'l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-',
     'w':'.--','x':'-..-','y':'-.--','z':'--..'}
R = {v: k for k, v in M.items()}
def divisions(rec, maxc):
    stream = ''.join(M[c] for c in rec); bounds, p = set(), 0
    for c in rec: p += len(M[c]); bounds.add(p)
    out = set()
    def go(pos, acc):
        if pos == len(stream):
            used, q = set(), 0
            for c in acc: q += len(M[c]); used.add(q)
            if len(bounds ^ used) <= maxc: out.add((''.join(acc), len(bounds ^ used)))
            return
        for L in range(1, 5):
            ch = R.get(stream[pos:pos + L])
            if ch and pos + L <= len(stream): go(pos + L, acc + [ch])
    go(0, []); return out
if __name__ == '__main__':
    out = open(os.path.join(here, 'morse_tail_out.txt'), 'a', encoding='utf-8')
    rec, maxc = sys.argv[1], int(sys.argv[2])
    for s, c in sorted(divisions(rec, maxc), key=lambda x: x[1]):
        if len(s) % 4: continue
        syl = [s[i:i + 2] for i in range(0, len(s), 2)]
        if not all(a in CONS and b in VOW for a, b in syl): continue
        codes = ['%02d%02d' % (tbl[syl[i]], tbl[syl[i + 1]]) for i in range(0, len(syl), 2)]
        if all(x in code2ch for x in codes):
            print(rec, c, s, ' '.join(codes), ''.join(code2ch[x] for x in codes), file=out)
