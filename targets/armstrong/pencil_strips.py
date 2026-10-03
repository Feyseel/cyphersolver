"""Cut a frame region into overlapping strips with the pencil interlinear brought up (autocontrast + gamma 3).
python pencil_strips.py <roll> <frame> <x0> <x1> <y0> <y1> [step] [height]   (fractions of the frame)"""
import sys
from PIL import Image, ImageOps
roll, fr = sys.argv[1], int(sys.argv[2])
x0, x1, y0, y1 = map(float, sys.argv[3:7])
step = int(sys.argv[7]) if len(sys.argv) > 7 else 150
hgt = int(sys.argv[8]) if len(sys.argv) > 8 else 200
src = f'img/M34-014-{fr:04d}.jpg' if roll == '14' else f'img13/M34-013-{fr:04d}.jpg'
im = Image.open(src).convert('L')
W, H = im.size
r = im.crop((int(W*x0), int(H*y0), int(W*x1), int(H*y1)))
i = 0
for y in range(0, r.size[1] - 40, step):
    s = r.crop((0, y, r.size[0], min(r.size[1], y + hgt)))
    s = ImageOps.autocontrast(s, cutoff=1).point(lambda v: int(255*((v/255)**3)))
    s.save(f'crops14/{roll}_{fr:04d}_{i:02d}.png'); i += 1
print(i, 'strips', r.size)
