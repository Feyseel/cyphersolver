"""crop.py <image> <x0> <y0> <x1> <y1> [out] [scale]: crop a scan region (original pixels) to the scratchpad."""
import sys
from PIL import Image
S = 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/5811e4e0-b0c6-4d49-aea6-59dbbb36f974/scratchpad/'
f, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
out = sys.argv[6] if len(sys.argv) > 6 else 'crop.png'
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(f).crop((x0, y0, x1, y1))
if sc != 1.0:
    im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
im.save(S + out)
print(S + out, im.size)
