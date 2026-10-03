# -*- coding: utf-8 -*-
"""Resolve a transcribed Lope Hurtado token string against key_codes.tsv.
Only 'confirmed' values are applied; 'probable' ones are shown in <angle brackets>
so they can never be mistaken for evidence. Unknown tokens print as ?tok.

Letter mode (added 2026-10-02, for the transcriptions in 1524 notation):
  python decode.py --letter r9634          # decode r9634_cipher.txt line by line + coverage
  python decode.py --letter r9634 --probable   # count probable values as read too
Key priority in letter mode: key_1522_<letter>.tsv > key_1522_r9634.tsv (the 1522 hand, shared) > ../lopehurtado1523/key_merged.tsv
(which already folds in key_1522_from1524*.tsv) > key_1522_from1524_B.tsv > key_1522_from1524.tsv >
key_codes.tsv (codes only). A line is a comment when it starts with '# ' (hash + space); '#' alone is a sign.
Clear words in [brackets] are skipped. Lines starting with '#' are comments."""
import sys, csv, io, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
CONF, PROB = {}, {}
for r in csv.reader(io.open(os.path.join(HERE,'key_codes.tsv'), encoding='utf-8'), delimiter='\t'):
    if not r or r[0].startswith('#') or r[0] == 'code':
        continue
    (CONF if len(r) > 2 and r[2] == 'confirmed' else PROB)[r[0]] = r[1]

def one(t):
    if t in CONF: return CONF[t]
    if t in PROB: return '<%s>' % PROB[t]
    return '?' + t

def run(toks):
    out = [one(t) for t in toks]
    hit = sum(1 for o in out if not o.startswith('?'))
    return out, hit, len(out)


def load_letter_key(letter):
    """value table for letter mode: token -> (plain, confidence, source-label)"""
    srcs = [(os.path.join(HERE, 'key_1522_%s.tsv' % letter), letter),
            (os.path.join(HERE, 'key_1522_r9634.tsv'), 'r9634-hand'),  # the 1522 hand's values, shared
            (os.path.join(HERE, '..', 'lopehurtado1523', 'key_merged.tsv'), 'merged-1524'),
            (os.path.join(HERE, 'key_1522_from1524_B.tsv'), '1522-B'),
            (os.path.join(HERE, 'key_1522_from1524.tsv'), '1522-in-1524'),
            (os.path.join(HERE, 'key_codes.tsv'), '1522')]
    key = {}
    for fn, lab in srcs:
        if not os.path.exists(fn):
            continue
        for r in csv.reader(io.open(fn, encoding='utf-8'), delimiter='\t'):
            if not r or r[0].startswith('# ') or r[0] == 'code' or len(r) < 3:
                continue
            k = r[0].strip()
            if lab == '1522' and not re.match(r'^[a-zɣʃ][a-zɡɣᵹ]{1,3}$', k):
                continue  # 1522 single signs are in the old notation
            k = k.replace('ɣub', 'yub').replace('ɣuc', 'yuc').replace('ɣaf', 'yaf').replace('ɣof', 'yof')
            if k not in key:
                key[k] = (r[1].split(' (')[0].split(';')[0].strip(), r[2].strip(), lab)
    return key


def letter_mode(letter, count_probable):
    key = load_letter_key(letter)
    fn = os.path.join(HERE, '%s_cipher.txt' % letter)
    tot = hit = hitp = 0
    per_unknown = {}
    for line in io.open(fn, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        ref, _, body = line.partition(' ')
        body = re.sub(r'\[[^\]]*\]', ' ', body)
        toks = body.split()
        out = []
        for t in toks:
            t2 = t.replace('(?)', '')
            v = key.get(t2)
            tot += 1
            if v is None:
                out.append('?' + t2)
                per_unknown[t2] = per_unknown.get(t2, 0) + 1
            elif v[1] == 'confirmed':
                hit += 1; hitp += 1
                out.append(v[0] if len(v[0]) > 1 else v[0].upper())
            else:
                hitp += 1
                out.append('<%s>' % (v[0] if len(v[0]) > 1 else v[0].upper()))
        if toks:
            print('%-6s %s' % (ref, ' '.join(out)))
    print('\ntokens %d; confirmed values %d (%.0f%%); with probable %d (%.0f%%)' % (
        tot, hit, 100.0*hit/tot, hitp, 100.0*hitp/tot))
    print('unvalued:', ' '.join('%s×%d' % kv for kv in sorted(per_unknown.items(), key=lambda kv: -kv[1])))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--letter':
        letter_mode(a[1], '--probable' in a)
        sys.exit()
    toks = a or sys.stdin.read().split()
    out, hit, n = run(toks)
    print(' '.join(out))
    print('coverage: %d/%d tokens = %.0f%%' % (hit, n, 100.0*hit/n if n else 0))
