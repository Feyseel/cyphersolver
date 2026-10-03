"""Pass 16 (2026-10-02): apply the values fixed from R9898's marginal decipherments, CSP Spain ii 636-638 and
cross-letter context to the (b) lines of r9873_cipher.txt and r9898_cipher.txt. Idempotent."""
import re
VALUES = {  # group: value  (evidence in key_working.md, pass 16)
    'ruc': 'dicho', 'rus': 'dicho', 'hay': 'aunque', 'v em': 'cierto', 'li': 'mi', 'net': 'halla',
    'lec': 'mos', 'doh': 'sabe', 'cuq': 'tengo', 'tig': 'contra', 'gat': 'esto', 'yod': 'amigo',
    'quf': 'enemigo', 'kuc': 'liga', 'fed': 'rey de Francia', 'xir': 'cardenal', 'lot': 'nuncio',
    'pof': 'exercito', 'cex': 'trata', 'ges': 'embaxador', 'lin': 'necesidad', 'nuh': 'grande',
    'Jus': 'pasa', 'sus': 'pasa', 'him': 'poco', 'Jac': 'obliga', 'hoz': 'dich', 'cap': 'tem',
    'kin': 'manda', 'qus': 'este', 'guf': 'puede', 'vih': 'cerca', 'lef': 'parece', 'noh': 'grand',
    'sud': 'datario', 'yol': 'aqui', 'nah': 'govierno', 'bun': 'visorrey', 'pand': 'buena', 'Jur': 'parte', 'kch': 'mal', 'dug': 'sabi',
}
FIX = [  # whole-phrase corrections forced by the new values
    ('[li] c-e-r-a-g-os t-r-i-u-n-f-o h-e-t-a', '[li=Mi]-c-e-r A-g-os-t-i-n-o F-o-y-e-t-a'),
    ('a [li] c-e-r-a-g-os t-i-d-f-o y e-t-a', 'a [li=Mi]-c-e-r A-g-os-t-i-n-o F-o-y-e-t-a'),
    ('a [li] c-e-r-a-g-os t-i-d ¶', 'a [li=Mi]-c-e-r A-g-os-t-i-n-o ¶'),
    ('despues a g-os t-i-d-f-o y e-t-a', 'despues a-g-os-t-i-n-o F-o-y-e-t-a'),
    ('al [kam] de su c-a-s-a', 'al [kam] de su c-a-s-a'),
]
for path in ('r9873_cipher.txt', 'r9898_cipher.txt'):
    out = []
    for ln in open(path, encoding='utf-8').read().splitlines():
        if re.match(r'\s*\d+[bd]\s', ln):
            for a, b in FIX:
                ln = ln.replace(a, b)
            def sub(m):
                g = m.group(1)
                if '=' in g or g not in VALUES:
                    return m.group(0)
                return '[' + g + '=' + VALUES[g] + ']'
            ln = re.sub(r'\[([^\]]+)\]', sub, ln)
        out.append(ln)
    open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('ok')
