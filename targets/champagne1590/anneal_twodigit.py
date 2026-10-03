"""Extend the two-digit alphabet of fr. 3623 nos. 24/25/60 ciphertext-only (3 Oct 2026).

    python targets/champagne1590/anneal_twodigit.py

The anchored values (NOTES, "Nos. 24, 25, 60") rise with the alphabet, so each unknown letter value is bracketed
between its known neighbours (52 between h 48 and i 53, 62 between l 58 and n 63, 92/94/95 above s 86 and at u 93).
The search space is small enough to enumerate exhaustively instead of annealing. Every combination is scored with the
French LM (fr-1600-letters, early normalisation) over all ten runs, with the code numbers (05 12 16 17 19 39 89 99)
left out. A value is accepted only if it gives sense in a SECOND occurrence as well.
"""
import itertools
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from lang import lm  # noqa: E402

KNOWN = {"30": "a", "32": "a", "33": "a", "34": "a", "35": "a", "37": "c", "38": "d", "42": "e", "43": "e", "45": "e",
         "46": "f", "47": "g", "48": "h", "53": "i", "54": "i", "56": "l", "58": "l", "63": "n", "64": "n", "67": "o",
         "74": "r", "75": "r", "82": "s", "83": "s", "84": "s", "86": "s", "93": "u"}
SLOTS = {"52": "hi", "62": "lmn", "92": "stuv", "94": "uv", "95": "uvxyz"}


def main():
    runs = [l.split() for l in (HERE / "ct_3623_twodigit.txt").read_text(encoding="utf-8").splitlines()
            if l[:1].isdigit()]
    m = lm.load("fr-1600-letters")
    res = []
    for combo in itertools.product(*SLOTS.values()):
        a = dict(zip(SLOTS, combo))
        texts = ["".join(KNOWN.get(t) or a.get(t) or "" for t in r) for r in runs]
        n = sum(len(x) for x in texts)
        res.append((sum(m.per_char(lm.norm(x, "early")) * len(x) for x in texts) / n, a, texts))
    res.sort(key=lambda r: -r[0])
    for sc, a, _ in res[:6]:
        print(round(sc, 4), a)
    print("best:", res[0][2])
    from collections import Counter
    occ = Counter(t for r in runs for t in r)
    print("occurrences of the bracketed values:", {k: occ[k] for k in SLOTS})


if __name__ == "__main__":
    main()
