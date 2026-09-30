# R902 p. 278 (DECODE image 4844), lines 10-18: fresh transcription and continuous reading (30 Sept 2026)

Transcription: `tr/R902_p278_l10-18.txt`, read from the image `R902_p2.png` (main checkout, git-ignored; deskewed
-3.1 degrees and read line by line at 2-3x). Decoder: `python decode_tr.py tr/R902_p278_l10-18.txt` (the corrected
R639 table of `targets/rakoczi1704/decode_tr.py`, plus 212 = Fa, 93 = st and the underline rule below).

## Group-by-group

| line | groups (image) | values |
|---|---|---|
| 10 | 107 30 321 218 295 27 424_ 315 381 142 98 296 343 19 293 66 382 39 257 255 17 362 | · L Ont fait Na I tre_ On se bo R ne present E ment A se P La in D re |
| 11 | 125 173 257 161 428 407 174 435 124_ 407 83 380 66 258 228 181 123 44 173 257 507 582 | · de La Cond vi te de vostre Al_ te S se A le garde des affaire S de La Pologne · |
| 12 | 670 112 173 150 81 405 255 44 176 45 166 100 356 17 312 67 437 413 439 196 343_ 150 | · Et de ce R Ta in S di S Cour S quelle D Oit A voir ten(ir) us en pres_ ce |
| 13 | 113 173 223 114 351 196 321 371 439 160_ 39 407 135 130 356 129 312 176 102 349 119 | · de ge ns qui en Ont rend us Com_ P te asseur ant quelle au Oit di T que · |
| 14 | 107 342_ 35 130 264 252 174 257 507 129 411 67 152 192 98 350 14 194 175 257 517 587 | · pren_ N ant les interets de La Pologne au tant A co eu R que C eux de La Hongrie · |
| 15 | 99 195 197 312 372 18 173 381 379 14 363 214 205 195 292 83 248 258 212 30 75 | · elle est Oit resolu E de se Sa C ri fi er elle mesme S il le Fa L L |
| 16 | 312 339 123_ 360 77 14 236 81 257 260 140 98 406 507_ 90 313 18 37 94 79 363 275 18 | Oit pour af_ Ra N C hi R La li be R te Polo_ N Ois E O P P ri me E |
| 17 | 127 328 497 196 212 104 192 81 178 462 93 66 298 44 257 100 244 398 83 125 587 | · par les Svedois en Fa U eu R du Roy st A ni S La S je sui S avec · |
| 18 | 109 104 77 424 344_ 215 90 16 361 45 324 15 85? 107 4 129 567 103 113 5 609 563 | · U N tres pro_ fo N D re S pe C T? · [closing figures] |

· = filler. The odd nulls of the table (99, 107, 109, 113) and the groups that open a line with no sense in context
(125 in l. 11, 127 in l. 17, 670 in l. 12) or close it (5xx) are fillers, as in R912 and R922 (rakoczi1704 NOTES).
The last group of l. 13 is 119, a table null (the second figure is the curled 1, not the looped 2; DECODE also
read 119).

## Continuous text (lines 10-18)

… l'ont fait naître. On se borne présentement à se plaindre de la conduite de Vostre Altesse à l'égard des affaires
de la Pologne, et de certains discours qu'elle doit avoir tenus en présence de gens qui en ont rendu compte,
asseurant qu'elle avoit dit que, prenant les intérêts de la Pologne autant à cœur que ceux de la Hongrie, elle
estoit résolue de se sacrifier elle-mesme s'il le falloit pour affranchir la liberté polonoise opprimée par les
Suédois en faveur du Roy Stanislas. Je suis avec un très profond respect …

… [have] given rise to it. For the present they confine themselves to complaining of Your Highness's conduct with
regard to the affairs of Poland, and of certain remarks you are said to have made in the presence of people who
have reported them, asserting that you had said that, taking the interests of Poland as much to heart as those of
Hungary, you were resolved to sacrifice yourself if need be to free Polish liberty, oppressed by the Swedes in
favour of King Stanislas. I am, with a very deep respect, …

"elle" is Vostre Altesse (Rákóczi). In 1707 the anti-Swedish Polish confederates offered Rákóczi the Polish crown;
the Swedish side complains here of his remarks.

## Grades

- H: every value read from the R639 table on groups read from the image. Every group of ll. 10-17 that is not a
  filler (582, 587, 670 and the table nulls) has a table value: nothing in the passage is unread.
- C: 212 = Fa (the table's F row is the syllable series, cf. Ba 139, Ca 149, Ga 222; DECODE's key transcription
  has 'F'); 93 = st (St-a-ni-s-la-s here, and 'O B 93 A . le' = obstacle in R912); the underline rule: an
  underlined number keeps its first syllable only (342_ pren-ant, 123_ af-franchir, 507_ Polo-n-oise,
  343_ pres-ence, 124_ Al-tesse, 160_ Com-pte, 424_ tre-, 344_ pro-fond), eight cases, all giving French.
- I: the line-opening fillers 125 (l. 11) and 127 (l. 17); 413 tenir used as ten- in 'tenus'; 462 le Roy de read
  'Roy' before st-a-ni-s-la-s.

## What the fresh transcription changed against DECODE's digits

DECODE's '3^' is this hand's 5 (the long-s shaped figure), and its '1^.' the raised 1; read that way, most of its
digits for these lines are right. The old `decode.py` took '3^' as 3, which produced much of the noise. The real
differences, in the 196 groups of ll. 10-18, are the curled 1 before 7 or 0 read as 2, and a few single figures:

- 1 read as 2: l. 11 273 -> 173 (de); l. 12 273 -> 173, 276 -> 176 (di: discours); l. 13 273 -> 173, 276 -> 176;
  l. 14 274 -> 174, 275 -> 175 (de); l. 15 273 -> 173, 295 -> 195 (elle); l. 17 204 -> 104 (U: faveur),
  278 -> 178 (du).
- other figures: l. 10 325 -> 315 (On), 246 -> 296 (ne), 29 243 -> 19 293 (E ment); l. 11 404 -> 407 (te);
  l. 12 200 -> 100 (S), 27 -> 17 (D), 296 -> 196 (en); l. 13 124 -> 129 (au: avoit); l. 14 527 -> 517 (Hongrie,
  not Tekeli).
- joins: DECODE runs several groups together without a point (321218, 381142, 1611428, 181123, 351196, 321371439,
  41167, 381379, 81257, 81278, 36145); the image has points between them.
