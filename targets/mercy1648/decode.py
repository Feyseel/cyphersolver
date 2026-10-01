"""Decode BnF Espagnol 144 f. 22r-22v (Barneton, 6 June 1648) with key.tsv from the verified transcription ct_f22.tsv.

    python decode.py            # one line per manuscript line: clear words in lower case, cipher runs in UPPER CASE
    python decode.py --runs     # the cipher runs only, one per line, with their token counts

A two-digit token that cannot be a letter (values above 34) was split in ct_f22.tsv into the two digits it is made
of; the notes column says where. BOX is the name sign. '?' is a code with no value."""
import csv, collections, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent

def load():
    key = {r['code']: r for r in csv.DictReader(open(HERE / 'key.tsv', encoding='utf8'), delimiter='\t')}
    lines = collections.OrderedDict()
    for r in csv.DictReader(open(HERE / 'ct_f22.tsv', encoding='utf8'), delimiter='\t'):
        lines.setdefault(r['line'], []).append(r)
    return key, lines

def decode_line(toks, key):
    out, run = [], []
    def flush():
        if run: out.append(''.join(run).upper()); run.clear()
    for r in toks:
        t = r['token']
        if t.startswith('[PLAIN:'):
            flush(); out.append(t[7:-1])
        elif t == 'BOX':
            flush(); out.append('<Santibal>')
        else:
            v = key[t]['value'] if t in key else '#'
            run.append(v)
    flush()
    return ' '.join(out)

if __name__ == '__main__':
    key, lines = load()
    for ln, toks in lines.items():
        s = decode_line(toks, key)
        if '--runs' in sys.argv:
            n = sum(1 for r in toks if not r['token'].startswith('[PLAIN'))
            if n: print(ln, n, s)
        else:
            print(ln, s)
