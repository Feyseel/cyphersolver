"""Does G. G. Butler, The Edmondes Papers (Roxburghe Club, 1913), print the Stowe MS 166 cipher passages?

HathiTrust (mdp.39015083993017) blocks this machine, so this uses the HathiTrust Research Center Extracted
Features 2.0 file: per-page word counts from the OCR, no word order. For each passage read here it counts how many
of its words stand on the Butler page that prints that letter, and how many stand on any other page (baseline).
Pages were identified from Butler's running heads and his "Stowe MS. 166, f. ..." source notes (NOTES.md,
"Print check"). Page number = seq - 48 for pp. 44-70 and seq - 52 for pp. 133-158.

    PYTHONUTF8=1 python targets/stowe166/butler1913_check.py
"""
import bz2
import json
import pathlib
import urllib.request

URL = 'https://data.analytics.hathitrust.org/features-2020.03/mdp/31891/mdp.39015083993017.json.bz2'
CACHE = pathlib.Path(__file__).parent / 'img' / 'butler1913_ef.json.bz2'     # img/ is git-ignored

if not CACHE.exists():
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_bytes(urllib.request.urlopen(URL, timeout=180).read())
# the file holds one bz2 stream followed by padding, so bz2.decompress() refuses it
pages = json.loads(bz2.BZ2Decompressor().decompress(CACHE.read_bytes()))['features']['pages']


def words(p):
    out = set()
    for sec in ('header', 'body', 'footer'):
        for w in ((p.get(sec) or {}).get('tokenPosCount') or {}):
            out.add(w.lower())
    return out


BAGS = {int(p['seq']): words(p) for p in pages}

# passage -> (Butler seqs, {word: accepted spellings}); Butler modernises some deciphered words, and the OCR of his
# italics gives "vendz ble" for vendible, "t/zat" for that, "clamonr" for clamour
PASSAGES = {
    'R7770 f. 50, Butler XVIII pp. 46-47': ([94, 95], {
        'breake': ['breake', 'break'], 'marriage': ['marriage'], 'betwene': ['betwene', 'betweene', 'between'],
        'resolued': ['resolued', 'resolved'], 'permitt': ['permitt', 'permit'], 'geive': ['geive', 'geiue', 'give'],
        'hope': ['hope'], 'render': ['render'], 'religion': ['religion', 'relligion'], 'enraged': ['enraged'],
        'extreemelie': ['extreemelie', 'extremely'], 'discontented': ['discontented']}),
    'R7771 f. 57, Butler XXI p. 53': ([101], {
        'glad': ['glad'], 'hoping': ['hoping', 'hopinge'], 'further': ['further'], 'troubled': ['troubled'],
        'clamor': ['clamor', 'clamour', 'clamonr'], 'catholikes': ['catholikes', 'catholiques', 'catholics'],
        'seekinge': ['seekinge', 'seeking']}),
    'R7772 f. 58v, Butler XXII p. 56': ([104], {
        'secretelie': ['secretelie', 'secretly'], 'learne': ['learne', 'learn'],
        'montmorancy': ['montmorancy', 'montmorency', 'memorancy'], 'instance': ['instance'],
        'condition': ['condition'], 'required': ['required'], 'performance': ['performance'],
        'yong': ['yong', 'young'], 'prince': ['prince'], 'conde': ['condé', 'conde'],
        'deliuered': ['deliuered', 'delivered'], 'handes': ['handes', 'hands'], 'madame': ['madame'],
        'angolesme': ["d'angolesme", "d'angoulesme"], 'sister in law': ['sister-in-law', 'sister'],
        'vnder': ['vnder', 'under'], 'custodie': ['custodie', 'custody']}),
    'R7773 f. 60v, Butler XXIII p. 58': ([106], {
        'faith': ['faith'], 'vendible': ['vendible', 'vendz'], 'ble (vendible split)': ['ble'],
        'that (italic OCR)': ['t/zat']}),
    'R7775 f. 112, Butler LXVI p. 150': ([202], {
        'execute': ['execute', 'execut'], 'enterprise': ['enterprise'], 'rheins': ['rheins', 'rheims'],
        'carrying': ['carryinge', 'carrying'], 'place': ['place']}),
    'R7774 f. 109v, not printed (Laon pp. 148-152 tested)': ([200, 202, 204], {
        'choise': ['choise', 'choice'], 'negotiate': ['negotiate', 'negociate'], 'difficulties': ['difficulties'],
        'empeachement': ['empeachement', 'impeachment'], 'interest': ['interest'],
        'pretending': ['pretending', 'pretendinge'], 'champaigne': ['champaigne', 'champagne'],
        'renewed': ['renewed'], 'intelligences': ['intelligences', 'intelligence'], 'amiens': ['amiens'],
        'rheins': ['rheins', 'rheims']}),
}

for name, (seqs, vocab) in PASSAGES.items():
    def hits(bag):
        return {k for k, forms in vocab.items() if any(f in bag for f in forms)}
    found = set().union(*(hits(BAGS[s]) for s in seqs))
    others = sorted((len(hits(b)) for s, b in BAGS.items() if s not in seqs), reverse=True)
    print(f'{name}: {len(found)}/{len(vocab)} words; missing {sorted(set(vocab) - found) or "none"}; '
          f'best other page {others[0]}/{len(vocab)}')
for s in (46, 53, 56, 58, 150):
    seq = s + 48 if s < 100 else s + 52
    print(f'p. {s} (seq {seq}): "cypher" on the page: {"cypher" in BAGS[seq]}')
