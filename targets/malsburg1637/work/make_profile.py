"""Write ../profile.json from the measured numbers (run from the target folder)."""
import json, re, sys
sys.argv = ['x']
sys.path.insert(0, '.')
import measure as M

SH = 'Hessisches Staatsarchiv Marburg, HStAM 4 h Nr. 1411'
DOCS = {  # record: (files, pages, date, route)
    '496': (['f003'], 'ff. 3-4', '5/15 Jan 1637', 'Otto von der Malsburg -> Landgrave Wilhelm V, Kassel'),
    '497': (['f012'], 'ff. 12-13', 'Wesel, 7/17 Jan 1637', 'Wesel -> Kassel'),
    '502': (['f014'], 'f. 14', 'Jan 1637', 'Westphalia -> Kassel'),
    '503': (['f015', 'f016'], 'ff. 15-17', 'Jan 1637', 'Westphalia -> Kassel'),
    '504': (['f018'], 'f. 18', '14/24 Feb 1637', 'Westphalia -> Kassel'),
    '505': (['f023', 'f024'], 'ff. 23-24', '7/17 Feb 1637', 'Westphalia -> Kassel'),
    '506': (['f025'], 'f. 25', '5 Mar / 23 Feb 1637', 'Westphalia -> Kassel'),
    '507': (['f028', 'f029'], 'ff. 28-29', '28 Mar 1637 (old style)', 'Westphalia -> Kassel'),
    '508': (['f030', 'f031'], 'ff. 30-31', '28 Mar 1637 (old style); duplicate of ff. 28-29', 'Westphalia -> Kassel'),
    '509': (['f032', 'f033'], 'ff. 32-33', '3 Apr 1637 (French letter signed 232) and news extracts of Mar 1637',
            'unknown -> Kassel'),
}
docs, T, R, OC = [], 0, 0, 0
for rec, (fs, pages, date, route) in DOCS.items():
    t = r = oc = 0
    for f in fs:
        a, b = M.measure(f'work/{f}.txt')
        t += a; r += b
        for run in M.runs(f'work/{f}.txt'):
            for tok, val in run:
                if val is None and not re.fullmatch(r'\d\d', tok.rstrip("'?_")):
                    oc += 1
    if rec != '508':
        T += t; R += r; OC += oc
    fr = r / t
    d = {'id': f'HCPortal {rec}', 'read': 'read' if fr >= 0.95 else 'read in part',
         'shelfmark': f'{SH}, {pages} (HCPortal cryptogram {rec})', 'date': date, 'year': 1637, 'country': 'Germany',
         'route': route, 'language': 'French and German' if rec == '509' else 'German', 'pages': len(fs),
         'cleartext_in_document': 'interspersed',
         'plaintext': {'location': ['none'],
                       'source': 'No contemporary decipherment on the leaves; clear text surrounds every cipher run.'},
         'length': {'tokens': t, 'unit': 'mixed', 'measured': True, 'file': f'ct/hcp{rec}.txt'},
         'transcription': {'by': 'llm from images', 'source': 'HCPortal originals, 2x line crops (lines.py)',
                           'image_quality': 'good',
                           'notes': f"{', '.join(f + '.txt' for f in fs)}; {r} of {t} tokens in words ({fr:.3f}), "
                                    f"{oc} code/sign tokens open. Unread spots re-checked against the scans "
                                    "(work/recheck_log*.tsv)."}}
    if rec == '508':
        d['transcription']['notes'] += ' Duplicate of HCPortal 507: a check copy, left out of the totals.'
    docs.append(d)
    print(rec, t, r, oc, round(fr, 3))
docs.insert(2, {
    'id': 'HCPortal 497, letter block', 'read': 'not read',
    'shelfmark': f'{SH}, f. 12, foot (margin "E: Sixt: cla:")', 'date': 'Wesel, 7/17 Jan 1637', 'year': 1637,
    'country': 'Germany', 'route': 'unknown', 'language': 'unknown', 'pages': 1,
    'cleartext_in_document': 'separate passages',
    'plaintext': {'location': ['none'], 'source': 'none found'},
    'length': {'tokens': 531, 'unit': 'letters', 'measured': True, 'file': 'ct/hcp497_letters.txt'},
    'transcription': {'by': 'llm from images', 'source': 'HCPortal original, f. 12', 'image_quality': 'fair',
                      'notes': 'Ten lines of lower-case letters with 43, 45 and an LL sign; measured with --letters. '
                               'Transcribed once; joined ascenders are ambiguous.'}})
print('TOTAL', T, R, OC, round(R / T, 4), round(R / (T - OC), 4))

prof = {
    'schema_version': 1, 'target': 'malsburg1637',
    'title': 'Otto von der Malsburg to Landgrave Wilhelm V of Hesse-Kassel: ten cipher letters on the war in '
             'Westphalia, Jan-Mar 1637 (HStAM 4 h Nr. 1411)',
    'documents': docs,
    'system': {
        'types': ['homophonic', 'nomenclator'],
        'summary': 'German homophonic substitution in two-digit groups 10-99 (2-7 homophones per letter), with '
                   'capital-letter signs for digraphs (ch, ei, st, ss, tt, mm, sch, ll, au, ff, ai) and three-digit '
                   'codes for names and military nouns.',
        'symbol_kind': 'digits and letters', 'distinct_symbols': 89,
        'digit_groups': {'separation': 'dots'},
        'diacritics': {'used': False}, 'homophones': {'used': True},
        'nomenclator': {'present': True}, 'nulls': {'present': False},
        'key_order': 'random', 'word_division': 'none',
        'sibling_key': 'none: 176 HCPortal key records of the Marburg key volumes checked; the Sixtinus key '
                       '(HCPortal key 5, Dec 1635) has the same layout but a different table',
        'notes': '89 two-digit groups, about 20 digraph signs, about 45 codes (151 tokens), a few name signs. '
                 'Single figures are plain numerals.'},
    'conditions': {
        'prior_solution': {'exists': 'no', 'where': 'HCPortal marks all ten records Not solved; no edition found',
                           'found': 'not found', 'used': False},
        'inputs': ['images', 'cleartext context'], 'attack': 'ciphertext-only',
        'human_role': 'Problem posed with /goal from catalogue entry 338, which suggested checking the 1635-52 key '
                      'sheets first. No target-specific intervention.',
        'tools': ['HCPortal API (cryptograms, cipher-keys)', 'PIL line crops',
                  'homophonic simulated annealing with lang de-1640s', 'dictionary segmentation measure'],
        'models': ['claude-opus-5-5'], 'sessions': 1, 'first_date': '2026-09-28', 'last_date': '2026-09-28'},
    'solution': [
        {'kind': 'access', 'what': 'Fetched the ten HCPortal records and 18 original scans of HStAM 4 h 1411 '
                                   'through api.hcportal.eu.', 'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'sibling key', 'what': 'Harvested all 176 HCPortal cipher-key records of the Marburg key volumes '
                                        'with their users; no Malsburg key. Keys 5 (Sixtinus 1635), 30, 38 and 49 '
                                        'compared with f. 3.', 'result': 'failed', 'date': '2026-09-28'},
        {'kind': 'transcription', 'what': 'f. 3 transcribed by hand from 2x line crops (455 groups).',
         'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'solver', 'what': 'Homophonic annealing of f. 3 alone against de-1640s, with and without a '
                                   'letter-frequency penalty.', 'result': 'failed', 'date': '2026-09-28'},
        {'kind': 'transcription', 'what': 'Remaining pages transcribed by two agents in the same format (about '
                                          '9,000 more groups); ff. 30-31 found to duplicate ff. 28-29.',
         'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'solver', 'what': 'Annealing ff. 3+12+18 (1,575 groups): all four restarts converged on the same '
                                   'key and German text (das ich auch noch nit weiss ... garnisonen ... '
                                   'contributiones vom platten lande).', 'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'hypothesis', 'what': 'Letter signs valued from context: N/D ch, Y/G ei, Z/O st, W/P ss, L/A tt, '
                                       'R/C/E/M mm, X/j/J sch, H ll, S/F au, T/B ff, Q ai; single figures are '
                                       'numerals.', 'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'solver', 'what': 'Digit table re-annealed and polished over all pages with the signs fixed: 23, '
                                   '40, 75 corrected; rare groups 14, 17, 20, 33, 85 assigned.',
         'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'control', 'what': 'Dictionary-segmentation measure; the same measure on shuffled keys gives '
                                    '50-58%.', 'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'verification', 'what': '236 unread groups re-checked against the scans: 24 misreads and 2 doubled '
                                         'groups corrected, 210 confirmed as written.',
         'result': 'worked', 'date': '2026-09-28'},
        {'kind': 'hypothesis', 'what': 'Codes valued from context: 128 Cöln, 130 Hamburg, 188 die Staaten, '
                                       '253 Regiment, 273 Compagnien (grade I).', 'result': 'partial',
         'date': '2026-09-28'},
        {'kind': 'solver', 'what': 'f. 12 letter-cipher block: many-to-one and null-allowing annealing in German, '
                                   'Latin, French, Italian and Dutch; periodic IC for periods 1-15; Caesar shifts; '
                                   'HCPortal letter keys 2 and 105.', 'result': 'failed', 'date': '2026-09-28'},
        {'kind': 'literature search', 'what': 'Web search for an edition of the Malsburg letters (Rommel, LAGIS); '
                                              'none found.', 'result': 'failed', 'date': '2026-09-28'},
        {'kind': 'reading', 'what': f'Reading measured: {R:,} of {T:,} cipher tokens in words ({R / T:.1%}); '
                                    f'{OC} code/sign tokens open; {R / (T - OC):.1%} of the non-code text.',
         'result': 'worked', 'date': '2026-09-28'}],
    'outcome': {
        'class': 'read in part', 'key': 'partial', 'method': 'key recovered from ciphertext-only',
        'method_basis': 'The two-digit table was recovered by homophonic annealing of the ciphertext against a '
                        '17th-century German model, with no key, crib or decipherment; the letter signs and codes '
                        'were then valued from context.',
        'contribution': ['transcription', 'key recovered', 'sender or date identified'],
        'parts': [
            {'label': 'The ten letters (ff. 3-33)', 'records': 'HCPortal 496-509',
             'method': 'key recovered from ciphertext-only', 'extent': 'complete',
             'basis': f'{R / T:.1%} of {T:,} cipher tokens read; codes counted apart'},
            {'label': 'Letter-cipher block at the foot of f. 12', 'records': 'HCPortal 497',
             'method': 'not solved', 'extent': 'none',
             'basis': '531 letters in a different system; no key among the 176 HCPortal key records'}],
        'first_break': True,
        'fraction_read': round(R / T, 3), 'fraction_read_method': 'measured',
        'fraction_read_source': f'measure.py over the transcriptions (reading_segmented.txt): {T:,} cipher tokens of '
                                'the letters, duplicate ff. 30-31 excluded; a token is read when all its letters fall '
                                f'in dictionary words; {OC} open code/sign tokens count as unread',
        'codes_open': {'open': 40, 'total': 45, 'tokens_open': OC},
        'verification': ['matched control', 'historical consistency'],
        'gaps': [
            {'item': 'letter-cipher block at the foot of f. 12 (531 letters)', 'blocker': 'no-key-material',
             'detail': 'a different system: not the Malsburg key, not a simple, homophonic, Caesar or periodic '
                       'cipher; no fitting key among the 176 HCPortal key records'},
            {'item': f'about 40 three-digit codes and name signs ({OC} tokens)', 'blocker': 'open-codes',
             'detail': 'mostly single occurrences; five valued from context (grade I)'}],
        'notes': 'Malsburg reports from Wesel on garrisons, contributions and recruiting, the siege of '
                 'Ehrenbreitstein (Hermannstein), Jan de Werth at Cologne, the peace talks at Cologne and Hamburg, '
                 'and plans with the States General.'}}
with open('profile.json', 'w', encoding='utf8') as fh:
    json.dump(prof, fh, indent=1, ensure_ascii=False)
    fh.write('\n')
