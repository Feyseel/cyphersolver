"""dec.py file... : print each cipher line with its decipherment under the key in key.txt.
Two-digit groups -> letters (unknown '?'); signs and codes shown as [X]; clear words in CAPS."""
import re, sys
K = {}
for line in open('key.txt', encoding='utf8'):
    if not line.startswith('#'):
        for kv in line.split():
            k, v = kv.split('=')
            K[k] = v
def dec_line(line):
    out = []
    for m in re.finditer(r'\{([^}]*)\}|(\S+)', line):
        if m.group(1) is not None:
            out.append(' ' + m.group(1).upper() + ' ')
            continue
        t = m.group(2).rstrip("'?_")
        if re.fullmatch(r'\d\d', t):
            out.append(K.get(t, '?'))
        elif t.rstrip('#') in K and not t.endswith('#'):
            out.append(K[t].upper())
        else:
            out.append(f'[{m.group(2)}]')
    return ''.join(out)
if __name__ == "__main__":
  for f in sys.argv[1:]:
      print('=====', f)
      for line in open(f, encoding='utf8'):
          if line.startswith('#'):
              if 'letter-cipher' in line:
                  break
              continue
          print(dec_line(line.strip()))
  