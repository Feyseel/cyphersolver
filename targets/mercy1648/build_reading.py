"""Build reading.tsv (one row per cipher token) and reading.txt (the letter, words separated) from the verified
transcription ct_f22.tsv, the key key.tsv, the interpretive edits edits.tsv and the table of letters lost at the
trimmed right edge of f. 22v (lost_edge.tsv).

    python build_reading.py                    # word breaks need a Spanish word list: lang/corpora es-gutenberg + es-quijote
    python build_reading.py --vocab file.pkl   # or a pickled Counter of words

Grades (README Conventions): I = inferred from context (the key was rebuilt from the ciphertext alone), C = from adjacent
plaintext (the name sign, from the clear instructions on ff. 20r-21r), M = uncertain (a re-segmented token, a glyph
settled by sense), - = no value found. [..] marks letters the trimmed leaf has lost, restored by sense; they are not
counted as read. The spaces between words are put in by a word-frequency segmenter and are a convenience, not evidence."""
import csv, collections, math, pathlib, pickle, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
tsv = lambda n: list(csv.DictReader(open(HERE / n, encoding='utf8'), delimiter='\t'))

key = {r['code']: r for r in tsv('key.tsv')}
edits = {(r['line'], int(r['position'])): r for r in tsv('edits.tsv')}
lost = collections.defaultdict(list)
for r in tsv('lost_edge.tsv'): lost[r['line']].append(r)
openst = tsv('open_stretches.tsv')
lines = collections.OrderedDict()
for r in tsv('ct_f22.tsv'): lines.setdefault(r['line'], []).append(r)


def items_for(ln, toks):
    """-> list of ('plain', word) | ('c', letter, grade, token, flag) | ('lost', letters)"""
    out, ncipher = [], 0
    lostmap = {int(x['after']): x['letters'] for x in lost.get(ln, [])}
    for r in toks:
        t = r['token']
        if t.startswith('[PLAIN:'):
            out.append(('plain', t[7:-1])); continue
        ncipher += 1
        e = edits.get((ln, int(r['position'])))
        if e and e['op'] == 'skip':
            pass
        elif e and e['op'] in ('letters', 'merge'):
            for ch in e['value']: out.append(('c', ch, e['grade'], t, e['op']))
        elif e and e['op'] == 'letter':
            out.append(('c', e['value'], '-' if e['value'] == '?' else 'M', t, 'open'))
        elif t == 'BOX':
            out.append(('c', '<Santibal>', key['BOX']['grade'], t, ''))
        else:
            k = key[t]; v = k['value']; g = k['grade']
            if r['confidence'] == 'M' and r['note']: g = 'M'
            out.append(('c', v, '-' if v == '?' else g, t, 'glyph' if r['note'] else ''))
        if ncipher in lostmap:
            out.append(('lost', lostmap[ncipher]))
    return out


def load_vocab():
    if '--vocab' in sys.argv:
        cnt = pickle.load(open(sys.argv[sys.argv.index('--vocab') + 1], 'rb'))
    else:
        cnt = collections.Counter()
        for name in ('es-gutenberg', 'es-quijote'):
            p = HERE.parents[1] / 'lang' / 'corpora' / (name + '.txt')
            if not p.exists(): p = pathlib.Path('C:/Users/dbour/cypher/lang/corpora') / (name + '.txt')
            t = unicodedata.normalize('NFD', p.read_text(encoding='utf8', errors='ignore').lower())
            cnt.update(re.findall(r'[a-z]+', ''.join(c for c in t if unicodedata.category(c) != 'Mn')))

    for w in ('mercy cheureuse brandenburg burgstorf cleues camarero santibal campagna alandose os embian propondreis leuanten '
              'leuantada regimientos regimiento hombres sera conuenient pagandola della dellas consiguiese uos uenga uan informe cmarero copurad lon burgsto rf pasareis').split():
        cnt[w] += 5000                                     # names and the clerk's spellings
    tot = sum(cnt.values())
    short = set('y a o e u de la el en no se si su le lo un al me mi es ya ni que con por mas una sin los las del os nos vos'.split())
    V = {}
    for w, c in cnt.items():                     # the clerk wrote u for v and i for j
        w2 = w.replace('v', 'u').replace('j', 'i')
        if c >= 3 and (len(w2) >= 3 or w2 in short): V[w2] = max(V.get(w2, -1e9), math.log((c + .5) / tot))
    return V


def segment(chars, V):
    s = ''.join(c for c, _ in chars); n = len(s)
    best = [-1e9] * (n + 1); bp = [0] * (n + 1); best[0] = 0
    for i in range(1, n + 1):
        for j in range(max(0, i - 16), i):
            w = s[j:i]
            sc = V.get(w, -1e5 if len(w) > 2 else -30)
            if best[j] + sc > best[i]: best[i], bp[i] = best[j] + sc, j
    cuts, i = [], n
    while i > 0: cuts.append((bp[i], i)); i = bp[i]
    return cuts[::-1]


if __name__ == '__main__':
    V = load_vocab()
    rows, stats, events = [], collections.Counter(), []   # events: (line, kind, payload)
    for ln, toks in lines.items():
        for it in items_for(ln, toks):
            if it[0] == 'plain': events.append((ln, 'plain', it[1]))
            elif it[0] == 'lost':
                for ch in it[1]: events.append((ln, 'c', (ch, True))); stats['lost letters'] += 1
            else:
                _, ch, g, tok, flag = it
                rows.append((ln, tok, ch, g, flag)); stats['tokens'] += 1; stats['grade ' + g] += 1
                events.append((ln, 'plain', ch) if ch == '<Santibal>' else (ln, 'c', (ch, False)))
                if ch == '?': stats['unread'] += 1
    out = collections.OrderedDict((ln, []) for ln in lines)
    i = 0
    while i < len(events):
        ln, kind, p = events[i]
        if kind == 'plain': out[ln].append(p); i += 1; continue
        j = i
        while j < len(events) and events[j][1] == 'c': j += 1
        run = events[i:j]
        for a, b in segment([c for _, _, c in run], V):
            by_line = collections.OrderedDict()
            for k in range(a, b):
                l, _, (ch, lostflag) = run[k]
                by_line.setdefault(l, []).append('[' + ch + ']' if lostflag else ch)
            parts = list(by_line.items())
            for n, (l, chs) in enumerate(parts):
                out[l].append(''.join(chs).replace('][', '') + ('-' if n < len(parts) - 1 else ''))
        i = j
    with open(HERE / 'reading.tsv', 'w', encoding='utf8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['line', 'token', 'value', 'grade', 'flag']); w.writerows(rows)
    head = ('# BnF Espagnol 144 f. 22r-22v, instruction to the abbe (baron) de Mercy, Barneton 6 June 1648, read from ct_f22.tsv + key.tsv.\n'
            '# Clear words as written; cipher runs lower case, as read. [..] = letters lost at the trimmed edge, restored by sense;\n'
            '# ? = no value; a word ending in - continues on the next line. Word breaks are a convenience (see build_reading.py).\n')
    with open(HERE / 'reading.txt', 'w', encoding='utf8', newline='') as f:
        f.write(head)
        for ln, ws in out.items(): f.write(ln + '  ' + ' '.join(ws) + '\n')
    n_open = sum(int(o['to']) - int(o['from']) + 1 for o in openst)
    stats['open stretch tokens'] = n_open
    stats['read as sense'] = stats['tokens'] - n_open - 0
    stats['fraction read'] = round(stats['read as sense'] / stats['tokens'], 4)
    print(dict(stats))
    print(open(HERE / 'reading.txt', encoding='utf8').read())
