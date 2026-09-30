"""Decode fresh image transcriptions of R902 (tr/) with the corrected R639 table of targets/rakoczi1704.

Usage: python decode_tr.py tr/R902_p278_l10-18.txt
Additions to the rakoczi1704 table, from R902 itself (30 Sept 2026):
  212 = Fa (the table's F row is the syllable series Fa fe fi fo fu, like Ba 139, Ca 149, Ga 222);
  93 = st (Stanislas here; 'O B 93 A . le' = obstacle in R912), grade C;
  an underlined number keeps only its first syllable: 342_ pren(dre), 123_ af(faire), 507_ Polo(gne),
  343_ pres(ent), 124_ Al(li), 160_ Com(me), 424_ tre(s), 344_ pro(pos).
"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "rakoczi1704"))
from decode_tr import key as KEY  # noqa: E402

key = dict(KEY)
key.update({"212": "Fa", "93": "st"})
TRUNC = {"342": "pren", "123": "af", "507": "Polo", "343": "pres", "124": "Al", "160": "Com",
         "424": "tre", "344": "pro"}


def decode(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        words = []
        for g in line.split():
            d = re.sub(r"\D", "", g)
            if "_" in g and d in TRUNC:
                v = TRUNC[d] + "_"
            elif d in key:
                v = key[d]
            else:
                v = f"[{d}]"
            words.append((v or "·") + ("?" if "?" in g else ""))
        out.append(" ".join(words))
    return "\n".join(out)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(decode(p))
