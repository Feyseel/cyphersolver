"""python zoom.py <roll> <frame> <x0> <y0> <x1> <y1> <out> [scale]  (fractions of the frame) -> enhanced, enlarged crop"""
import sys
from PIL import Image, ImageOps
roll, fr = sys.argv[1], int(sys.argv[2])
x0, y0, x1, y1 = map(float, sys.argv[3:7])
out = sys.argv[7]; sc = float(sys.argv[8]) if len(sys.argv) > 8 else 2
src = f'img/M34-014-{fr:04d}.jpg' if roll == '14' else f'img13/M34-013-{fr:04d}.jpg'
im = Image.open(src).convert('L'); W, H = im.size
r = im.crop((int(W*x0), int(H*y0), int(W*x1), int(H*y1)))
r = ImageOps.autocontrast(r, cutoff=0.5).point(lambda v: int(255*((v/255)**2.5)))
r = r.resize((int(r.size[0]*sc), int(r.size[1]*sc)), Image.LANCZOS)
r.save(out); print(r.size)
