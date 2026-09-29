import collections, sys, subprocess
def rs(t):
    t = [x for x in t if x != '|']
    out = []
    for n in (2, 3, 4):
        c = collections.Counter(tuple(t[i:i + n]) for i in range(len(t) - n + 1))
        out.append(sum(1 for v in c.values() if v > 1))
    c1 = collections.Counter(t)
    return 'types %d rep2 %d rep3 %d rep4 %d  repeats %d xyx %d' % (len(c1), out[0], out[1], out[2], sum(t[i] == t[i+1] for i in range(len(t)-1)), sum(t[i] == t[i+2] for i in range(len(t)-2)))
print('real       ', rs(open('ct.txt').read().split()))
for s in range(1, 6):
    subprocess.run([sys.executable, 'synth.py', str(s), '520', '1.0'], capture_output=True)
    print('letter  s%d ' % s, rs(open('synth_ct.txt').read().split()))
for s in range(1, 4):
    subprocess.run([sys.executable, 'synth2.py', str(s), '250', '400'], capture_output=True)
    print('mixed   s%d ' % s, rs(open('synth2_ct.txt').read().split()))
