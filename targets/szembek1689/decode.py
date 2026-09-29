"""Rebuild the key of the Szembek-papers cipher letter from its interlinear glosses and check every run.

Step 1 aligns each run with its gloss where the lengths agree and collects number -> letter pairs.
Step 2 deciphers every run with the resulting key (no gloss used) and compares with the gloss.
Writes key.tsv and prints the comparison and the measures used in NOTES.md.
"""
import collections, pathlib, re

HERE = pathlib.Path(__file__).parent


def norm(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('ae', 'e')
    return re.sub(r'[^a-z]', '', s)


def runs():
    for line in (HERE / 'runs.tsv').read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        f = line.split('\t')
        yield f[0], f[1].split(), f[2], (f[3] if len(f) > 3 else '')


def units(toks):
    """(token, is_cipher) with clear strings split into letters."""
    out = []
    for t in toks:
        if re.fullmatch(r'\d\d\??', t):
            out.append((t.rstrip('?'), True))
        elif re.fullmatch(r'\d{3}', t):
            out.append((t, 'code'))
        else:
            out.extend((c, False) for c in t)
    return out


pairs = collections.defaultdict(collections.Counter)
for fol, toks, gloss, note in runs():
    u = units(toks)
    g = norm(gloss)
    if gloss == '-' or any(k == 'code' for _, k in u) or len(u) != len(g):
        continue
    for (t, isc), ch in zip(u, g):
        if isc:
            pairs[t][ch] += 1

key = {t: c.most_common(1)[0][0] for t, c in pairs.items()}
with open(HERE / 'key.tsv', 'w', encoding='utf-8') as fh:
    fh.write('# number\tletter\toccurrences in aligned runs\tother letters seen\n')
    for t in sorted(pairs, key=int):
        c = pairs[t]
        other = ', '.join(f'{k}x{v}' for k, v in c.items() if k != key[t])
        fh.write(f'{t}\t{key[t]}\t{sum(c.values())}\t{other}\n')

print('key:', ' '.join(f'{t}={key[t]}' for t in sorted(key, key=int)))
by_letter = collections.defaultdict(list)
for t, ch in key.items():
    by_letter[ch].append(t)
print('letters with more than one number:', {k: v for k, v in by_letter.items() if len(v) > 1})

n_cipher = n_ok = n_code = 0
lines = []
for fol, toks, gloss, note in runs():
    u = units(toks)
    dec = ''
    for t, isc in u:
        if isc is True:
            n_cipher += 1
            dec += key.get(t, '?')
        elif isc == 'code':
            n_code += 1
            dec += '[' + t + ']'
        else:
            dec += t
    ok = norm(dec) == norm(gloss)
    lines.append(f'f.{fol}  {"OK " if ok else "DIF"}  {dec:<18} gloss {gloss:<16} {note}')
    if ok:
        n_ok += sum(1 for _, k in u if k is True)
print('\n'.join(lines))
difs = sum(1 for l in lines if ' DIF ' in l)
print(f'\nruns {len(lines)}, runs agreeing with gloss {len(lines) - difs}, differing {difs}')
print(f'two-digit cipher signs {n_cipher}; code groups {n_code}; distinct numbers {len(key)}')
