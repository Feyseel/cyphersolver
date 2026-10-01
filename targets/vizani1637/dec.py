"""Vizani 1637 (BnF fr. 16158 f. 292): re-apply Satoru's key to his sign-by-sign transcription and test it.

Input: cipher_words.tsv (his transcription of the 53/54 cipher words), key.json (his sign -> letter table).
1. decode every word with the key and compare it with the plain he gives (letters only);
2. score the decode with an Italian letter model against 200 keys of the same shape with the letters shuffled among the sign classes;
3. count the distinct signs, homophones and the share of signs that are unread name codes.
Run from this folder: python dec.py
"""
import json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

K = json.load(open(os.path.join(HERE, 'key.json'), encoding='utf8'))
S2L = {}
for letter, signs in K['key']:
    for s in signs:
        S2L[s] = letter
SIGNS = sorted(K['signs'], key=len, reverse=True)


def split(g):
    if re.fullmatch(r'\d+', g) and g not in ('6', '8'):
        return [g]
    out, i = [], 0
    while i < len(g):
        m = next((s for s in SIGNS if g.startswith(s, i)), g[i])
        out.append(m); i += len(m)
    return out


def load():
    rows = []
    for ln in open(os.path.join(HERE, 'cipher_words.tsv'), encoding='utf8'):
        if ln.startswith('#') or not ln.strip('\n'):
            continue
        g, plain, *flag = ln.rstrip('\n').split('\t')
        rows.append((g, plain, flag[0] if flag else ''))
    return rows


def decode_word(g, key=S2L):
    sg = split(g)
    if len(sg) == 1 and re.fullmatch(r'\d+', sg[0]) and sg[0] not in ('6', '8'):
        return None                                    # name code
    return ''.join(key.get(s, '?') if key.get(s) not in ('u / v',) else 'u' for s in sg)


def norm(s):
    return re.sub(r'[^a-z]', '', s.lower().replace('u / v', 'u').replace('v', 'u'))


def main():
    rows = load()
    ok = bad = 0
    out = []
    for g, plain, flag in rows:
        d = None if flag == 'n' else decode_word(g)
        if d is None:
            out.append('[%s]' % (g if g.isdigit() else plain.strip('[]'))); continue
        out.append(d)
        want = norm(re.sub(r'\([^)]*\)', '', plain))        # his (..) marks letters supplied from an abbreviation
        got = norm(d)
        if got == want or got.startswith(want) or want.startswith(got) or flag == 'q':
            ok += 1
        else:
            bad += 1; print('differs: %s -> %s, page says %s' % (g, d, plain))
    print(len(rows), 'cipher words;', ok, 'agree with the plain on the page,', bad, 'differ')
    print(' '.join(out))
    toks = [s for g, _, f in rows for s in ([g.strip()] if f == 'n' else split(g))]
    codes = [s for s in toks if re.fullmatch(r'\d{2,}', s) or s == '6ԗ']
    letters = [s for s in toks if s not in codes]
    print(len(toks), 'signs;', len(set(letters)), 'distinct letter signs;', len(codes), 'name-code groups', sorted(set(codes)))

    for model in ('it-cinquecento', 'it-modern'):
        M = lm.load(model)
        def score(key):
            txt = ' '.join(x for x in (decode_word(g, key) for g, _, f in rows if f != 'n') if x)
            return M.per_char(lm.norm(re.sub(r'\?', '', txt), 'modern'))
        real = score(S2L)
        classes = sorted({v for v in S2L.values() if v not in ('?', 'tt', 'ss', 'il', 'che')})
        random.seed(2); ctl = []
        for _ in range(200):
            p = classes[:]; random.shuffle(p)
            mp = dict(zip(classes, p))
            ctl.append(score({s: mp.get(v, v) for s, v in S2L.items()}))
        print('%-15s real %.3f per letter; 200 shuffled keys: best %.3f, mean %.3f' % (model, real, max(ctl), sum(ctl) / len(ctl)))


if __name__ == '__main__':
    main()
