# Hessian polyalphabetic message, 1824 (HStAM 9 a Nr. 259, f. 249; HCPortal record 513)

Catalogue item 340. Opened and read 28 Sept 2026 (one session, claude-opus-5-5, set by `/goal`).

## The leaf

- Hessisches Staatsarchiv Marburg, Best. 9 a (Kurhessen, Ministerium der auswärtigen Angelegenheiten),
  Nr. 259, f. 249. HCPortal record 513 (`api.hcportal.eu/api/cryptograms/513`, created by Eugen Antal,
  20 Nov 2025): "Message encrypted with a polyalphabetic cipher", date 20 Feb 1824, language German, "Not solved".
  Image: `https://api.hcportal.eu/media/1439/17901677521692.jpg` (2928 × 4416), saved as `images/f249.jpg`
  (git-ignored, as are the crops). HCPortal records 511 and 512 (Nr. 258) are unrelated telegraph ciphers;
  no other leaf of Nr. 259 is on HCPortal.
- The leaf is a police or ministry copy, not the letter itself. Heading "Snell an A?ud" (the addressee's name is
  not read with confidence), six lines of cipher, then an **Anmerkung** by the decipherer, in Kurrent:

  > Auf diese Art sind zwey Seiten voll und zwar mit No. 1 der sympathetischen Tinte (extr. Sat.) wie ich glaube,
  > zwischen die Linien eines ganz gleichgültigen Briefs geschrieben. Ich habe das Concept der Chiffre schriftlich
  > copirt, allein noch war ich nicht im Stande, mittelst des nebenstehenden Schlüssels zur Auflösung zu gelangen,
  > bis ich dann endlich durch hundertfache Versuche entdeckte, daß bcdefg in der obersten Querlinie des Schlüssels
  > die Schlagbuchstaben sind, welche fortlaufend über die Chiffres gesetzt werden müssen, wonach am linken Rande
  > des Schlüssels der verborgene Buchstabe ausfällt; so z. B. nämlich

  followed by the worked pairs b/u = s, c/f = c, d/m = h, e/o = i, f/g = k, g/m = n (Kurrent e, which looks like
  n), b/v = t, i.e. the first word "schiket". So the letter was written in sympathetic ink ("extractum Saturni",
  lead acetate) between the lines of an innocent letter; the decipherer had the key table ("nebenstehender
  Schlüssel", not on this image) and found how to use it. His solution of the text is not on the leaf.
- Context: Wilhelm Snell (1789–1851), the radical jurist, fled to Basel in 1821, where Karl Follen and W. M. L. de
  Wette also taught; his brother Ludwig Snell was suspended as rector of the Wetzlar gymnasium in 1820 and
  dismissed in 1824. Paul Follen was Karl's brother in Giessen. Fries and Oken (Jena) and de Wette were the
  professors dismissed or prosecuted after 1819. The questions fit the Mainz Central Commission's demagogue
  investigations of 1824. The sender is Snell (which brother is not settled). "Lisching" is not identified.

## Transcription

`ct.txt`, from the full-resolution scan, line by line (crops `images/L1.jpg`–`L6.jpg`, zooms `z2`–`z6`,
`z3b`). Dots and spaces are the word separators of the copy. Glyph points:
- straight-tailed q and looped g are distinct in the hand but the copyist confuses them (three places);
- `r` and `v`, and `u`, `n` and `w`, are close;
- the ʒ-shaped z is z (it reads as z in "beantworte");
- `4`, `1` and `3` are cipher signs, not numbers (see below);
- line 2 word 3 begins with a long-s/f-like capital; it is f (d under b).
- 169 signs: 164 letters (`_check_profile.py --measure ct.txt --letters`) + 5 digit signs.

## The system

A Vigenère table without j (25 plaintext rows). The key letters b c d e f g are written continuously over the
signs (word dots do not take a key letter), and key b..g enciphers by +2..+7. The cipher columns do not wrap:
after z they run on into the signs 1 2 3 4 …, so w under g is 21+7 = 28 = `4`, z under d is 24+3 = 27 = `3`,
v under e is 20+5 = 25 = `1`. The digits in the text are exactly these (`4` three times, all w under g;
`3` = z; `1` = v). `decrypt.py` implements it.

## How it was read (steps, in order)

1. Fetched the HCPortal record and image; read the Anmerkung: key letters bcdefg, period 6, a table with the
   plaintext on the left edge, and seven worked pairs.
2. The pairs fit shifts +2, +3, +4, +5 for b, c, d, e in a 25-letter alphabet without j; +6 for f fits if the
   decipherer's "g" is the straight-tailed q; +7 for g gives e, which is his Kurrent e (read at first as n).
3. Decrypted everything with shifts +2..+7 cycling: line 1 reads straight through ("schiket lisching oder eqnen
   andern hierher"), the rest drifts.
4. Per-line and per-word phase search: "beantworte diese fragen", "was hat paul follen … america",
   "fries oken", "hatte die … indung", "merkliche folgen" at shifted phases.
5. A beam decoder with phase slips and the German model (`beam.py`) was noisy; dropped.
6. "de 4ette" = de Wette showed `4` = w under g, i.e. the columns run on past z into digits. With the digits
   counted as signs, the key phase is continuous from line 3 to the end.
7. The only real phase break is at the start of line 2: `zsskkw` = "wonicht" with one sign (p) left out
   (z s s [p] k k w). Everything else is copy slips: 11 wrong signs in 8 words (all 9 words listed in `decrypt.py`):
   u for n (einen), d/l transposed (fragen), z for 2 and z for q (wegen), w for u (von), i for c (Auffindung),
   q for g and r for v (dieses), u for w (Plans), q for g (folgen). "Wezlar" = `4g3 pfx`, with z → `3`.
8. Prior-art check: HCPortal "not solved"; NoAutopilot/cipher-lab (GitHub) has a notes folder for this leaf with
   Vigenère/Beaufort ruled out at periods 2–20 and running-key tests, and no reading (PR 35, closed 27 Sept 2026).
   Nothing in print found.

## Reading

`reading.txt`:

> Schicket Lisching oder einen andern hierher; wo nicht, beantworte diese Fragen. Was hat Paul Follen wegen
> America von Fries, Oken, de Wette gehört? Hatte die Auffindung dieses Plans in Wezlar merkliche Folgen?

All 169 signs have a value; every one of the 38 words reads. Of the signs, 158 decrypt as written and 11 need a
one-sign correction of a copy slip (93.5% as written, 100% with the slips corrected). Grades: the whole text
H except "Lisching" (C: reads cleanly, person not identified) and the heading's addressee (not read).

## Remaining gaps

None in the cipher. The heading's addressee ("A?ud", in clear, Kurrent) is not read with confidence, and the
decipherer's key table ("nebenstehender Schlüssel") is not on the HCPortal image; neither affects the reading.

## Escalation

- [x] siblings: HCPortal records 490–535 checked; only 513 is from Nr. 259
- [x] clear-pages: the Anmerkung on the leaf is the decipherer's method note with the first word worked; used
- [n/a] known-keys: the table was rebuilt from the text; no other Hessian key of the period was needed
- [x] print: web search for the leaf, Lisching, Snell and Wetzlar; nothing prints this text
- [x] key-rebuild: 25-letter table with the digit run-on, from the note and the text
- [x] retry: every word re-decrypted with the final table (decrypt.py)
