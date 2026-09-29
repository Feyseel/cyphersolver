"""German unit inventory for the monotone solver: letters, syllables and frequent words, sorted a-z."""
import itertools
V = ['a', 'e', 'i', 'o', 'u', 'ei', 'au', 'ie', 'eu', 'ey', 'ay']
C = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z', 'v', 'j', 'x', 'q',
     'ch', 'sch', 'st', 'sp', 'pf', 'bl', 'br', 'dr', 'fl', 'fr', 'gl', 'gr', 'kl', 'kr', 'pl', 'pr', 'tr', 'zw', 'str', 'qu', 'th', 'ph']
CODA = ['b', 'ch', 'ck', 'd', 'f', 'ff', 'g', 'h', 'k', 'l', 'll', 'm', 'mm', 'n', 'nn', 'nd', 'ng', 'nt', 'r', 'rr', 'rt',
        'rd', 'rn', 's', 'ss', 'st', 't', 'tt', 'tz', 'x', 'z', 'ls', 'lt', 'nck', 'ht', 'cht', 'ft', 'rst', 'rs', 'ns', 'ts']
def build(words=400, extra=()):
    s = set('abcdefghijklmnopqrstuvwxyz')
    for c in C:
        for v in V: s.add(c + v)
    for v in ['a', 'e', 'i', 'o', 'u', 'ei', 'au', 'ie', 'eu']:
        for c in CODA: s.add(v + c)
    for c in C: s.add(c)
    s |= {'en', 'er', 'es', 'em', 'et', 'ern', 'ent', 'end', 'ung', 'ungen', 'lich', 'isch', 'keit', 'heit', 'schaft',
          'chen', 'ten', 'gen', 'den', 'ben', 'men', 'nen', 'len', 'ren', 'sen', 'wer', 'ver', 'zer', 'ge', 'be'}
    top = [l.split()[0] for l in open('corpus_topwords.txt')][:words]
    s |= set(w for w in top if w.isalpha() and len(w) <= 9)
    s |= set(extra)
    return sorted(s)
MIL = """armee arme trouppen truppen regiment regimenter general generals feind feinde koenig kayser kaiser printz prinz
fuerst frantzosen franzosen frankreich preussen bayern oesterreich rhein feldmarschall bataillon battaillon escadron
escadrons cavallerie infanterie marsch marchiren lager quartier quartiere winterquartier winterquartiere magazin
magazine artillerie canonen canon festung belagerung corps commando officier officiers soldaten mann compagnie
compagnien husaren dragoner curassier grenadier recrouten werbung hanover hannover holland hollaender engellaender
england sachsen boehmen wien berlin munchen frankfurt mayntz strassburg elsass lothringen flandern niederlande
brabant italien spanien kriegs krieg friede frieden allianz tractat hof minister gesandte courier nachricht nachrichten
briefe schreiben woche monat januarii februarii mertz april may junii julii augusti september october november december
jahre jahr neue neuen glueck gluck wunsch gnade gnaden hohe hoechste unterthanigst unterthaenigst durchlaucht""".split()
if __name__ == '__main__':
    inv = build(extra=MIL)
    open('inv_de.txt', 'w').write('\n'.join(inv) + '\n')
    print(len(inv))
