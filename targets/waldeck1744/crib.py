"""Place a crib at a token offset of ct.txt and write the implied code->letter fixes, if consistent.
usage: python crib.py offset crib [more offset crib ...] > fix.tsv"""
import sys, re
toks = [t for t in open('ct.txt').read().split() if t != '|']
fix = {}
args = sys.argv[1:]
for off, crib in zip(args[::2], args[1::2]):
    off = int(off); crib = re.sub('[^a-z]', '', crib.lower())
    for i, ch in enumerate(crib):
        c = toks[off + i]
        if fix.get(c, ch) != ch:
            sys.exit('conflict: code %s = %s and %s (crib %s at %d)' % (c, fix[c], ch, crib, off + i))
        fix[c] = ch
for c, ch in fix.items(): print('%s\t%s' % (c, ch))
print('%d codes fixed' % len(fix), file=sys.stderr)
