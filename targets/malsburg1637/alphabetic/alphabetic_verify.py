#!/usr/bin/env python3
"""Replay the Malsburg alphabetic working edition using only Python's stdlib.

This checks transcription arithmetic, not the accuracy of the manuscript reading.
Run without arguments to verify. --write-results refreshes the saved result JSON.
No network access, key search, language scoring or silent text repairs are used.
"""
from __future__ import annotations

import argparse
import collections
import csv
import difflib
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ALPHABET = 'abcdefghiklmnopqrstuwxyz'
KEY = (4, 5, 3, 6, 2)
TOKENS = re.compile(r'\[BLOT\]|LL|43|45|.', re.DOTALL)
NORMALIZATION = str.maketrans({'ü': 'u', 'ÿ': 'y', 'j': 'i'})
ALIGN_FIELDS = ('absolute_zero_based', 'line', 'source_letter_position_one_based',
                'normalized_offset_zero_based', 'cipher', 'key_phase', 'shift', 'plaintext')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def normalize(source):
    return source.replace('[blot]', '[BLOT]').translate(NORMALIZATION)


def read_json(name):
    return json.loads((HERE / name).read_text(encoding='utf-8'))


def read_csv(name):
    with (HERE / name).open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream))


def decode(sources, *, count_unknown=False, key=KEY):
    """Keep annotations out of the stream; carry phase across all source lines.

    count_unknown is False for the inherited transcription, whose question mark
    is punctuation. In a source alternative, ? denotes one unknown cipher sign.
    """
    absolute = 0
    rows, alignment = [], []
    for line_no, source in enumerate(sources, 1):
        output, line_pos = [], 0
        phase_start = absolute % len(key)
        for match in TOKENS.finditer(source):
            token = match.group()
            if token in ('43', '45', 'LL'):
                output.append('[' + token + ']')
            elif len(token) == 1 and (token in ALPHABET or (token == '?' and count_unknown)):
                phase = absolute % len(key)
                plain = '?' if token == '?' else ALPHABET[(ALPHABET.index(token) - key[phase]) % len(ALPHABET)]
                line_pos += 1
                alignment.append(dict(zip(ALIGN_FIELDS, (absolute, line_no, line_pos,
                    match.start(), token, phase, key[phase], plain))))
                if token != '?':
                    require(ALPHABET[(ALPHABET.index(plain) + key[phase]) % len(ALPHABET)] == token,
                            f'Re-encryption mismatch at line {line_no}:{line_pos}')
                output.append(plain)
                absolute += 1
            else:
                require(not token.isalpha() or token == '[BLOT]', f'Unsupported token {token!r}')
                output.append(token)
        rows.append(dict(line=line_no, source=source, literal=''.join(output),
                         positions=line_pos, phase_start=phase_start, phase_end=absolute % len(key)))
    return rows, alignment


def compare_alignment(expected, actual, label):
    require(len(expected) == len(actual), f'{label}: alignment length')
    for number, (saved, computed) in enumerate(zip(expected, actual), 1):
        require(set(saved) == set(computed), f'{label}: alignment fields')
        require(all(saved[k] == str(v) for k, v in computed.items()),
                f'{label}: alignment row {number}')


def verify():
    data = read_json('alphabetic_edition.json')
    require(data['alphabet'] == ALPHABET and data['encryption_shifts'] == list(KEY), 'Mechanism differs')
    require(len(data['lines']) == 10, 'Expected ten manuscript lines')
    edition_csv = read_csv('alphabetic_edition.csv')
    require(edition_csv == [{k: str(v) for k, v in r.items()} for r in data['lines']], 'CSV/JSON edition mismatch')
    for r in data['lines']:
        require(normalize(r['original_source']) == r['original_normalized_source'], 'Original normalization mismatch')
    raw_source = '\n'.join(r['original_source'] for r in data['lines'])
    raw_isalpha_count = sum(c.isalpha() for c in raw_source)
    require(raw_isalpha_count == 531, 'Inherited raw isalpha count mismatch')
    # Repository integration check, when this folder is beside the original ct/.
    # The package also remains usable as a standalone compact evidence bundle.
    repository_source = HERE.parent / 'ct' / 'hcp497_letters.txt'
    repository_source_match = 'not present in standalone location'
    if repository_source.is_file():
        require(repository_source.read_text(encoding='utf-8').splitlines() ==
                [r['original_source'] for r in data['lines']], 'Repository original source differs')
        repository_source_match = True
    originals = [r['original_normalized_source'] for r in data['lines']]
    selected = [r['selected_normalized_source'] for r in data['lines']]
    old_rows, old_align = decode(originals)
    new_rows, new_align = decode(selected, count_unknown=True)
    require(len(old_align) == 523 and len(new_align) == 510, 'Expected 523/510 ordinary positions')
    require([r['literal'] for r in old_rows] == [r['original_literal'] for r in data['lines']], 'Original literal mismatch')
    require([r['literal'] for r in new_rows] == [r['selected_literal'] for r in data['lines']], 'Selected literal mismatch')
    compare_alignment(read_csv('alphabetic_original_alignment.csv'), old_align, 'original')
    compare_alignment(read_csv('alphabetic_selected_alignment.csv'), new_align, 'selected')
    selected_letters = ''.join(r['cipher'] for r in new_align)
    require((HERE / 'alphabetic_selected_letters.txt').read_text().strip() == selected_letters, 'Selected letter stream mismatch')

    # Reproduce the saved deterministic alignment; its edit runs are not unique
    # when glyphs repeat, and they do not count actual scribal errors.
    ledger = read_csv('alphabetic_edit_ledger.csv')
    computed_edits, delta = [], 0
    for ln in range(1, 11):
        old = ''.join(r['cipher'] for r in old_align if r['line'] == ln)
        new = ''.join(r['cipher'] for r in new_align if r['line'] == ln)
        for tag, i, j, k, l in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
            if tag == 'equal':
                continue
            change = (l - k) - (j - i)
            computed_edits.append(dict(line=ln, operation=tag,
                original_start_one_based=i+1, original_end_inclusive=j,
                final_start_one_based=k+1, final_end_inclusive=l,
                original_normalized=old[i:j], final_normalized=new[k:l],
                net_alphabetic_change=change, phase_displacement_before=delta % 5,
                phase_displacement_after=(delta + change) % 5))
            delta += change
    require(len(ledger) == len(computed_edits) == 33 and delta == -13, 'Edit ledger size/count mismatch')
    for saved, computed in zip(ledger, computed_edits):
        require(all(saved[k] == str(v) for k, v in computed.items()), 'Edit ledger mismatch')

    alternatives = read_json('alphabetic_alternatives.json')
    require(len(alternatives['branches']) == 64, 'Expected 64 defined branches')
    lengths, anchors = collections.Counter(), collections.Counter()
    choice_names = ('L7_unknown_count', 'L8_y_vs_iy', 'L3_h_u', 'L6_g_q', 'L8_n_r', 'L9_m_n')
    choice_sets = set()
    for branch in alternatives['branches']:
        # Reconstruct each branch from exactly the six declared source choices.
        # Apply offsets right-to-left so insertions cannot move a later edit.
        expected_sources = selected.copy()
        edits = []
        for spec in alternatives['source_choices']:
            value = branch['choices'][spec['choice']]
            require(value in (spec['selected_value'], spec['alternative_value']), 'Undeclared choice value')
            if value == spec['alternative_value']:
                edits.extend(spec['source_edits'])
        for edit in sorted(edits, key=lambda e: (e['line'], e['normalized_offset_zero_based']), reverse=True):
            ln, start = edit['line']-1, edit['normalized_offset_zero_based']
            end = start + len(edit['original'])
            require(expected_sources[ln][start:end] == edit['original'], 'Source alternative location mismatch')
            expected_sources[ln] = expected_sources[ln][:start] + edit['alternative'] + expected_sources[ln][end:]
        require(expected_sources == branch['sources'], 'Branch contains undeclared source changes')
        branch_rows, branch_align = decode(branch['sources'], count_unknown=True)
        require([r['literal'] for r in branch_rows] == branch['expected_literals'], f"Branch {branch['branch']}: literal mismatch")
        require(len(branch_align) == branch['positions'], 'Branch count mismatch')
        lengths[str(len(branch_align))] += 1
        text = ''.join(r['literal'] for r in branch_rows)
        for anchor in alternatives['summary']['anchor_survival_reused_not_independent']:
            anchors[anchor] += int(anchor in text)
        choice_sets.add(tuple(branch['choices'][name] for name in choice_names))
    require(len(choice_sets) == 64, 'Branch choices are not 64 distinct combinations')
    require(dict(lengths) == {'510': 16, '511': 32, '512': 16}, 'Branch length distribution mismatch')
    require(dict(anchors) == alternatives['summary']['anchor_survival_reused_not_independent'], 'Anchor counts mismatch')
    require(alternatives['branches'][0]['sources'] == selected, 'Selected branch mismatch')

    # Diagnose two proposed local repairs without adopting either repair.
    t1 = next(r for r in new_align if r['line'] == 4 and r['source_letter_position_one_based'] == 37)
    t2 = next(r for r in new_align if r['line'] == 9 and r['source_letter_position_one_based'] == 42)
    require((t1['absolute_zero_based'], t1['cipher'], t1['plaintext'], t1['key_phase']) == (211, 'w', 'q', 1), 'First residual position mismatch')
    require((t2['absolute_zero_based'], t2['cipher'], t2['plaintext'], t2['key_phase']) == (472, 'g', 'd', 2), 'Second residual position mismatch')
    _, alternate_align = decode(selected, count_unknown=True, key=(4, 4, 2, 6, 2))
    changed = sum(a['plaintext'] != b['plaintext'] for a, b in zip(new_align, alternate_align))
    require(changed == 204, 'Global alternative key count mismatch')
    inputs = ('alphabetic_edition.json', 'alphabetic_edition.csv', 'alphabetic_original_alignment.csv',
              'alphabetic_selected_alignment.csv', 'alphabetic_edit_ledger.csv',
              'alphabetic_alternatives.json', 'alphabetic_selected_letters.txt', 'alphabetic_verify.py')
    return dict(status='PASS', alphabet=ALPHABET, encryption_shifts=list(KEY),
        repository_original_source_matches=repository_source_match,
        inherited_raw_isalpha_count=raw_isalpha_count,
        raw_count_explanation='531 includes four letters in the two LL labels and four letters in [blot]; excluding those gives 523 ordinary positions.',
        original_alphabetic_positions=len(old_align), selected_alphabetic_positions=len(new_align),
        original_line_counts=[r['positions'] for r in old_rows],
        selected_line_counts=[r['positions'] for r in new_rows],
        selected_line_start_phases=[r['phase_start'] for r in new_rows],
        original_literal_exact=True, selected_literal_exact=True,
        edition_csv_matches_json=True, original_and_selected_alignments_exact=True,
        re_encryption_consistent=True, deterministic_edit_runs=len(ledger), net_count_change=delta,
        defined_source_branches=64, branch_position_distribution=dict(lengths),
        reused_anchor_survival=dict(anchors),
        alternative_global_key_changes=changed, changes_beyond_two_conjectural_targets=changed-2,
        scope='Mechanical consistency only. No human paleographic review, identity proof, new key search, exhaustive source-space enumeration, or independent linguistic confirmation.',
        input_sha256={name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in inputs})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-results', action='store_true', help='replace alphabetic_verification.json with the current verified results')
    arguments = parser.parse_args()
    results = verify()
    if arguments.write_results:
        (HERE / 'alphabetic_verification.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(results, indent=2))
