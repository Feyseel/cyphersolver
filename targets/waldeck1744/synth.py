"""Synthetic control: German report enciphered with a random homophonic table whose profile
(types, singletons, top frequency) matches the real 717-group text.  usage: python synth.py seed [nhom]"""
import random, sys, re, collections
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nhom = int(sys.argv[2]) if len(sys.argv) > 2 else 520
bias = float(sys.argv[3]) if len(sys.argv) > 3 else 1.3
rnd = random.Random(seed)
PT = """Ew hochfürstliche Durchlaucht berichte ich unterthänigst dass die französische Armee unter dem Marschall von Coigny
die Winterquartiere im Elsass bezogen hat und dass man von Strassburg vernimmt wie der König im Frühjahr ein starkes
Corps an den Rhein zu schicken gesonnen sey. Die Bayerischen Trouppen stehen noch bey Frankfurt und werden durch
die Hessischen verstärckt. Man sagt dass der Printz Carl von Lothringen seine Armee in Bayern zusammenziehen und mit
den ersten Tagen des Mertzen gegen den Rhein marschiren werde. Die Magazine zu Heilbronn sind mit Mehl und Haber
angefüllet und die Artillerie ist von Wien abgegangen. Von Seiten des Königs von Preussen hört man nichts gewisses,
doch glaubt man dass er sich mit dem Kayser vereinigen werde. Ich werde nicht ermangeln Ew Durchlaucht von allem
was weiter vorgehet zu benachrichtigen und verharre mit tiefstem Respect"""
t = PT.lower().replace('ä','a').replace('ö','o').replace('ü','u')
t = re.sub('[^a-z]', '', t)[:717]
F = dict(zip('abcdefghijklmnopqrstuvwxyz',[6.5,1.9,2.9,5.1,17.0,1.7,3.0,4.8,7.6,0.3,1.2,3.4,2.5,9.8,2.6,0.8,0.1,7.0,7.3,6.2,4.4,0.9,1.9,0.1,0.1,1.1]))
nums = list(range(1, 1000)); rnd.shuffle(nums)
table = {}; k = 0
for c in F:
    n = max(1, round(F[c] / 100 * nhom))
    table[c] = nums[k:k+n]; k += n
out = []
for c in t:
    h = table[c]
    w = [1.0 / (i + 1) ** bias for i in range(len(h))]
    out.append(str(rnd.choices(h, w)[0]))
cnt = collections.Counter(out)
print(len(out), 'tokens', len(cnt), 'types', sum(v == 1 for v in cnt.values()), 'singletons', cnt.most_common(3), file=sys.stderr)
open('synth_ct.txt', 'w').write(' '.join(out) + '\n')
open('synth_pt.txt', 'w').write(t + '\n')
