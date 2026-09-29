"""lines.py <image> <x0> <y0> <x1> <y1> <tag> [nseg]: find text lines in a region by row ink profile and write
each line as nseg 2x-upscaled overlapping segments <tag>_<line>_<seg>.png to the scratchpad."""
import sys
import numpy as np
from PIL import Image
S = 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/5811e4e0-b0c6-4d49-aea6-59dbbb36f974/scratchpad/'
f, x0, y0, x1, y1, tag = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
nseg = int(sys.argv[7]) if len(sys.argv) > 7 else 4
im = Image.open(f).convert('L')
a = np.asarray(im.crop((x0, y0, x1, y1)), dtype=float)
ink = (a < a.mean() - 45).sum(1).astype(float)
k = 9
sm = np.convolve(ink, np.ones(k) / k, 'same')
# line centres = local maxima of the smoothed profile separated by >= 35 px
cent = []
for y in range(len(sm)):
    if sm[y] > 0.35 * sm.max() and sm[y] == sm[max(0, y - 25):y + 26].max():
        if not cent or y - cent[-1] > 35:
            cent.append(y)
gaps = [cent[i + 1] - cent[i] for i in range(len(cent) - 1)]
h = int(np.median(gaps)) if gaps else 60
full = Image.open(f)
W = x1 - x0
for li, c in enumerate(cent):
    top, bot = y0 + c - int(0.75 * h), y0 + c + int(0.6 * h)
    for s in range(nseg):
        a0 = x0 + int(s * W / nseg) - 40
        a1 = x0 + int((s + 1) * W / nseg) + 40
        seg = full.crop((max(0, a0), top, min(full.width, a1), bot))
        seg = seg.resize((seg.width * 2, seg.height * 2), Image.LANCZOS)
        seg.save(f'{S}{tag}_{li:02d}_{s}.png')
print(len(cent), 'lines at', [y0 + c for c in cent], 'spacing', h)
