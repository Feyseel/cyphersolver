"""Write docs/reveal/mercy1648.json (the "watch it decipher" passage) from the verified transcription and the key:
the cipher from "pas|areis a Cleues" (f. 22r line 13) to "que uan con esta y" (line 19), token by token, word spaces added
by the segmenter in build_reading.py."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.argv = [sys.argv[0]] + sys.argv[1:]
import build_reading as br

V = br.load_vocab()
first, last = 'r13', 'r19'
names = list(br.lines)
sel = names[names.index(first):names.index(last) + 1]
events = []                                   # (g, letter, grade)
for ln in sel:
    toks = br.lines[ln]
    its = br.items_for(ln, toks)
    started = ln != first
    for it in its:
        if it[0] == 'plain': started = True; continue
        if not started: continue
        if it[0] == 'c': events.append((it[3], it[1], it[2]))
tokens = [{'g': '', 'p': '... confiar della, ', 'cls': 'plain'}]
letters = [(e[1], False) for e in events]
cuts = br.segment(letters, V)
for n, (a, b) in enumerate(cuts):
    if n: tokens.append({'g': '', 'p': ' ', 'cls': 'plain'})
    for g, p, grade in events[a:b]:
        t = {'g': 'box' if g == 'BOX' else g, 'p': p}
        if grade == 'M': t['cls'] = 'unc'
        tokens.append(t)
tokens.append({'g': '', 'p': ' ...', 'cls': 'plain'})
out = {
    'slug': 'mercy1648', 'anchor': 'the-reading',
    'title': 'f. 22r, lines 13&ndash;19: to Cleves, to the Elector and his chief chamberlain',
    'caption': 'The run from &ldquo;pas-&rdquo; at the end of line 13 to &ldquo;que uan con esta y&rdquo; on f. 22r, number by number with the key recovered by NoAutopilot: pasareis a Cleues a veros con el elector de Brandenburg y con Conrad von Burgstorf su camarero mayor para quien se os embian cartas de creencia. 5 2 is r o, 4 8 is q u, 2 6 is o s (digits written together). Grey numbers are uncertain.',
    'unit': 'numbers',
    'key_note': 'Homophonic substitution of the numbers 2&ndash;34, one to three numbers per letter (a: 10, 17, 34; e: 18, 19, 33; i: 21, 26, 31; o: 2, 23, 29; u: 8, 25, 27), no word division. Word spaces are added here.',
    'tokens': tokens,
}
dest = HERE.parents[1] / 'docs' / 'reveal' / 'mercy1648.json'
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf8', newline='\n')
print(len(tokens), 'tokens;', ''.join(t['p'] for t in tokens))
