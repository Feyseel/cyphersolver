# Military news for Prince Carl August Friedrich of Waldeck, 1744 (HStAM 118 a Nr. 3954, ff. 3-4)

Status: attempted, not read (closed from the evidence, 28 Sept 2026). No key; ciphertext-only is shown infeasible
for this letter below; the key or more traffic would have to come from the undigitised 1744 volumes in Marburg.

Hessisches Staatsarchiv Marburg, HStAM 118 a (Waldeckisches Kabinett) Nr. 3954, ff. 3r-4r; HCPortal record 517
("Not solved"); catalogue 339. Archive title: "Militärische Nachrichten für Fürst Carl August Friedrich (in
Chiffre)", 1744. Recipient: Prince Carl August Friedrich of Waldeck-Pyrmont (1704-1763), Imperial
Feldzeugmeister and owner of an Imperial infantry regiment (later IR 35), Dutch general of infantry from 1742,
commander of the Dutch army from 1745. Sender unknown.

Images (git-ignored, `img/`): HCPortal media 1448 (f. 3r, 2908 x 3214) and 1449 (f. 4r, 2618 x 3044), the same
files as Arcinsys `https://digitalisate-he.arcinsys.de/hstam/118_a/3954/hstam_118_a_nr_3954_0003.jpg` and `_0004`;
the whole file is 8 images `_0001`-`_0008` (detail page https://arcinsys.hessen.de/arcinsys/detailAction?detailid=v4131421).

## The file

| image | leaf | what it is |
|---|---|---|
| 0001-0002, 0007-0008 | wrapper | a reused 1874 tax form, pencilled "Kabinet / Chiffrierter Brief / 1744" |
| 0003 | f. 3r | "1744" (later hand), calligraphic "Durchlauchtigster Fürst", then "Ew. H. Dl." in clear and 19 lines of dotted numbers |
| 0006 | f. 3v | docket "Schreiben an [name left blank] in Ziffern"; a pen trial of the flourished D |
| 0004 | f. 4r | a second, narrower leaf: 26 more lines; line 17 has "Ew. H. Dl." in clear inside the code; no signature, no date |
| 0005 | f. 4v | the prince's French draft reply, in clear, with corrections |

The draft on f. 4v (read from the scan; struck words in brackets): "Je viens de recevoir, Monsieur, votre lettre
du 18e Janv. Je vous remercie des [nouvelles] sentiments que vous me [donnez] témoignez [et de tout le bien que
vous me souhaitez] à l'occasion du renouvellement de l'année. Je vous souhaite pareillement toute sorte de
[prospérité] satisfaction ... les nouvelles de chez vous Monsieur seront sûrement intéressantes, et vous
m'obligerez de m'en donner le plus souvent qu'il vous sera possible. Selon ce que l'on me marque de Vienne le
Lieutenant Colonel quittera le régiment et comme par là il y aura des places vacantes vous pouvez compter que je
me souviendrai de vous ..." Because it is written on the back of the cipher leaf, the cipher letter is most
probably that letter of 18 January 1744: news and New Year wishes from a man hoping for a commission in the
prince's Imperial regiment. The body is German (the salutation and both clear addresses are German).

## Transcription

`trans_p1.txt` (f. 3r, 19 lines) and `trans_p2.txt` (f. 4r, 26 lines), one manuscript line per row, read here from
full-resolution crops; `ct.txt` is the solver input (`|` = the clear "Ew. H. Dl." on f. 4 l. 17). Writer's
corrections resolved: f. 4 l. 5 a struck "9x" with 7 written above -> 7; f. 4 l. 13 a struck "97" with 8 above -> 8.
Doubtful: f. 3 l. 3 320 (0 overwritten), l. 12 422 (blotted), l. 15 "78" (overwritten, maybe struck), f. 4 l. 12
555 (or 553). f. 4 writes 2 as a z-shaped figure and 5 with a hooked flag that looks like a colon; the dots,
dashes and spaces between groups carry no information (checked on every line). Line 1 of f. 3 ends "556.=",
the German hyphen: a word runs over the line, so some groups are parts of words.

## Statistics (`stats.py`, `repstats.py`)

717 groups (measured), 303 distinct, 144 used once; values 4-999 (19 one-digit, 133 two-digit, 565 three-digit).
Most frequent: 19 and 141 (14), 38 and 341 (13), 24 (11), 937 and 7 (10), 447 and 283 (9), 298 (8). Repeats:
33 bigrams, 5 trigrams (209.801.182 three times; 875.856.21, 329.309.422, 879.144.7, 144.7.126 twice), one
4-gram. No group follows itself and no X.Y.X pattern occurs. 879.144.X.126 occurs four times with X = 90, 7, 7,
924, and on f. 4 l. 5 the writer struck a "9" in that slot and wrote 7: 7, 90 and 924 are probably homophones.
Codes under 100 carry 21% of the tokens (1.5 per number, against 0.4-0.9 per number above 100).

## What the system is (and is not)

| hypothesis | test | result |
|---|---|---|
| letter-level homophonic cipher | 303 types need a table of 300+ letter homophones (Beale scale); period letter tables give a letter 3-6 numbers. No immediate repeats against 2-5 in letter-level controls | rejected as the main system |
| one-part (alphabetical) code, 1-999 | token mass along the codes against the alphabet profile of German syllabary usage (`cdf_test.py`): KS 0.192, random numbering median 0.077 | rejected |
| letters in 1-99, alphabetical 100-999 | the same for codes >= 100 (`cdf_test2.py`): KS 0.149 against random 0.077 (a true alphabetical control scores 0.067) | rejected |
| Hessian column numbering (units digit = column, as HStAM 4 d Nr. 1220 f. 12 of 1723 and Nr. 1231 of 1720-30) | best of the 20 cyclic column orders (`cdf_test3.py`): 0.057, random numberings' best median 0.047 | no support |
| multiplicative numbering n = a*p mod 1000 | best of 400 (`cdf_test4.py`): 0.038, random 0.036 | no support |
| two-part homophonic nomenclator (letters with about 4 scattered numbers, some 600 syllables and words with one each, as the Hessen-Kassel key HStAM 4 d Nr. 1229, DECODE R4680) | profile of a synthetic encoding (`synth6.py`): 310 types, 146 singletons, top 14, 93 types used 3+ times carrying 429 tokens | matches the real profile (303, 144, 14, 85 / 425); the low-number excess fits a clerk who took the first number of each entry |

So the letter is most probably in a two-part homophonic nomenclator of about a thousand numbers.

## What was tried (all ciphertext-only)

A 1740s German model was added to `lang/` for this target (`de-1740s`: 202 DTA texts of 1724-1767, newspapers
of Berlin 1737-41, the Hamburgischer Correspondent, military manuals, 23.6 M letters). Every solver was run first on a
synthetic control of the same size and profile whose key is known.

- `hsolve.cs`, letter-level homophonic annealer (5-gram): on the letter-level control, gibberish outscores the
  true plaintext under the modern model (-1234 vs -1408) and at best ties it under the 1740s model (-1090.5 vs
  -1094.4). Real text: best -1107.5, no two restarts agree (`runs/real_h1.txt`).
- `wordseg.py`, `hsolve2.cs`, `hgibbs.cs`: adding a unigram-word segmentation term puts the truth on top on
  the control (-2173 vs -2340 best found after 12 x 20 M moves; heat-bath sampling -2679): the objective is right
  but the search does not reach it at 2.4 tokens per type.
- `msolve.cs`, `msolve2.cs`, `msolve3.cs`, `gsolve.cs`: monotone (one-part) annealers after `swieten1757/msolve.py`,
  with free codes under 100, chained per units digit, remapped to Hessian column order, and as a heat-bath sampler.
  On alphabetical controls the truth scores highest only at a letter bonus of about 1.0 or less, and the searches
  stall below it (-1065 to -1173 vs -924 to -992). Real text: fragment soup (`runs/real_m1.txt`).
- `msolvefree.cs` on the two-part control (`synth6.py`): the true key scores -1934 (bonus 0.6) and -1284
  (bonus 1.0), and blind runs find gibberish at -1060 and -255. The language model prefers wrong keys by a wide
  margin at any length prior: 717 groups do not identify a two-part nomenclator key. This is why the letter is
  closed rather than left to more compute.
- Cribs: the New Year wish implied by the reply ("zu dem angetrete-nen neuen Jahre" fits the line-1 hyphen after
  14 groups if the groups were letters) cannot be placed in a two-part code, where the unit boundaries are unknown.

## Sibling traffic and keys searched

- Arcinsys, all Hessian archives: Chiffre, Chiffren, Chiffern, chiffriert, dechiffriert, Chiffrenschlüssel,
  Geheimschrift, Ziffern, "Chiffre Waldeck", Kundschafter. Nr. 3954 is the only cipher item in 118 a and in any
  Waldeck fonds after 1646 (115/01 Nr. 2602 of 1638 and Nr. 1290 of 1646 are unrelated letter ciphers; HCPortal
  key 135 is a letter substitution).
- The 1744 volumes in the same node are undigitised: 118 a Nr. 1973-1980 "Akten betr. den Feldzug von 1744" (Bd. 1,
  Jan-May 1744, is where the correspondence of January 1744 and a deciphered copy would be), Nr. 1969-1972 and 2044
  (Berlichingen, Daun and Traun, Cobenzl, second Silesian war, Prince Charles of Lorraine), Nr. 2047 (officers'
  applications 1745-50).
- HCPortal: records 494-523 (all Marburg) and all 319 keys: no Waldeck key of the 1740s.
- DECODE: all 112 Marburg key records dated 1710-1799 (Hessen-Kassel, 4 d Nr. 1220-1238) listed with their
  metadata; the German ones looked at do not fit: Nr. 1231 (1720-30, column-numbered syllabary: 24 = "ble"),
  Nr. 1229 / R4680 (1730, two-part, numbers to 2500), Nr. 1237 / R4742 (mid-18th c., one-part, about 2250 entries),
  R4741 (French letter code of the Seven Years' War). None is tied to Waldeck.

## Remaining gaps
- the whole letter, 717 groups - blocker: no-key-material; two-part nomenclator, no key in Marburg's online files, HCPortal or DECODE, and one letter is too little to rebuild it (the synthetic control shows the key is not identifiable at this length)
- further traffic or a deciphered copy in HStAM 118 a Nr. 1973 (Feldzug 1744 Bd. 1) and Nr. 1969-1972, 2044, 2047 - blocker: needs-physical-access; undigitised

## Escalation
- [x] siblings: the whole file (8 images) read; Arcinsys searched for cipher items in 118 a and every Waldeck fonds; the 1744 volumes are not online
- [x] clear-pages: f. 4v is the prince's reply in clear, not a decipherment; f. 3v is a docket
- [x] known-keys: HCPortal's Marburg keys and DECODE's 112 Marburg keys of 1710-1799 listed; the German ones checked do not fit
- [x] print: no edition of the prince's 1744 correspondence found; BLKÖ and Curtze give his career only
- [x] key-rebuild: letter-level, one-part, column-numbered and two-part solvers, each validated on a synthetic control; ciphertext-only shown infeasible for a two-part code of this size
- [n/a] retry: nothing was read to retry against

## Files

`stats.py` (statistics), `repstats.py`, `cdf_test*.py` (ordering tests), `synth*.py` (controls), `wordseg.py`,
`inventory.py`, `crib.py`, `remap.py`; C# solvers `hsolve.cs`, `hsolve2.cs`, `hgibbs.cs`, `msolve*.cs`,
`gsolve.cs` (compile with `csc -optimize+ -platform:x64`; the LM table is exported from `lang` with
`np.load('lang/cache/de-1740s.o5.ns.npy').astype('<f4').tofile('de1740_5.bin')`, the word list from the
`de-dta-1720-1770` corpus by `wordseg.py`).
