# Malsburg 1637: Otto von der Malsburg's cipher letters to Landgrave Wilhelm V (HStAM 4 h Nr. 1411)

Status: read in part (the ten letters 95.9% of 9,736 cipher tokens, key recovered from the ciphertext alone; codes and the f. 12 letter block open)

- **Record.** Hessisches Staatsarchiv Marburg, HStAM 4 h Nr. 1411, "Korrespondenz in Chiffren mit dem
  Generalkommissar Otto v.d. Malsburg betr. Kriegführung in Münster und Westfalen", ff. 3-33. HCPortal cryptograms
  496, 497, 502-509 (all "Not solved" on HCPortal). Catalogue entry 338.
- **Images.** 18 HCPortal originals (ff. 3, 4, 12-18, 23-25, 28-33), fetched by `fetch_images.py` into `img/`
  (git-ignored), with the HCPortal record JSON.
- **What it is.** Letters from Otto von der Malsburg, Hesse-Kassel's General Commissary, to Landgrave Wilhelm V at
  Kassel ("Durchleuchtiger Hochgeborner Gnädiger Fürst und Herr"), January to March 1637, mostly from Wesel. Each is
  a clear letter with long cipher runs, and several are almost wholly cipher.

| folio | HCPortal | date | what |
|---|---|---|---|
| 3 (4 = address) | 496 | 5/15 Jan 1637 | signed Otto von der Malsburg; two cipher blocks |
| 12 (13 = address) | 497 | Wesel, 7/17 Jan 1637 | three cipher blocks, and a separate letter-cipher block (see below) |
| 14 | 502 | Jan 1637 | four cipher blocks |
| 15 | 503 | Jan 1637 | "Triplicat", one block |
| 16 (17 = address) | 503 | 30 Jan 1637 (HCPortal date) | two blocks; a clear list of officers on the right leaf |
| 18 | 504 | 14/24 Feb 1637 | subscribed "E. F. G. Dr:", Malsburg's hand |
| 23-24 | 505 | 7/17 Feb 1637 | signed "Otto von der Malsburgk"; nearly all cipher |
| 25 | 506 | 5 Mar / 23 Feb 1637 | signed |
| 28-29 | 507 | 28 Mar 1637 (old style) | nearly all cipher |
| 30-31 | 508 | the same | "Duplicat" of ff. 28-29; used as a check copy, not counted |
| 32-33 | 509 | 3 Apr 1637 and Mar 1637 | a French letter signed "232", and German news extracts in a second hand, both with cipher runs in the same key |

## The system

A German homophonic substitution written in two-digit groups (10-99, dots between), with letter signs for
common digraphs and a small code of three-digit groups for names and military nouns.

- **Two-digit table** (`key.txt`): 89 groups, 2-7 homophones per letter (e 7, u 7, a 6, o 6, n 5, i 5, t 5 ...).
  No regular pattern (unlike the Sixtinus key of Dec 1635, HCPortal key 5, which has the same layout).
- **Letter signs**: N, D = ch; Y, G = ei; Z, O = st; W, P = ss; L, A = tt; R, C, E, M = mm; X, j, J = sch; H, H# = ll;
  S, F, F# = au; T, B = ff. Single figures are plain numerals ("5 [tausend] reichsthaler").
- **Codes** (`codes.txt`): about 45 three-digit groups (115-269), 151 tokens. Five inferred from context: 128 Cöln,
  130 Hamburg, 188 die Staaten, 273 Compagnien, 253 Regiment. The rest are open. A few more signs (V triangle,
  K, Q, f, m, 4#, +, XX) behave as codes and are open.

## Verify first: the Hesse-Kassel key sheets

- HCPortal holds 176 key records for the Marburg key volumes (`research/catalogue_harvest/hcportal/keys/`, index
  `keys_index.txt`, harvested 28 Sept 2026 through `api/cipher-keys/<id>`), each with its named users. None is
  Malsburg's key. Key 31's name list gives "Otto v. der Malßburg - 523", so he appears in other keys only as a name code.
- Key 5 (Sixtinus, Dec 1635) and key 30 ("1637 or before") are the same family: a two-digit homophonic table,
  letter signs and codes from 111. Key 5's addenda share several code numbers with Malsburg's (193, 201, 210, 212),
  but its table does not decode f. 3. Keys 38 and 49 do not fit either.

## Method

1. Transcription: f. 3 by hand from 2x line crops (`lines.py`, `crop.py`); the other pages by two transcription
   agents in the same format (`f0NN.txt`). The duplicate (ff. 30-31) was used to correct ff. 28-29.
2. Homophonic annealing (`solve.py`, lang `de-1640s`, order 5, no spaces, letter signs and codes as breaks, a
   letter-frequency penalty): f. 3 alone (455 groups) gave noise; ff. 3+12+18 (1,575 groups) converged in all four
   restarts on the same key and German text ("das ich auch noch nit weiss ... die garnisonen ... die contributiones
   vom platten lande").
3. Letter signs read from context (noch, möglich = N; lassen = W; geschlossen = X; Statthalter Nesselrode = L, P;
   Stettin = A), then fixed in the solver; the digit table re-annealed and polished over all pages.
4. Reading measure (`measure.py`): each cipher run decoded and segmented into words from the DTA 1470-1670
   vocabulary plus `extra.txt` (names and spellings confirmed in context). A shuffled-key control scores 50-58%.
5. Re-check of the unread spots against the scans (`unread.py`, `work/unread_spots.tsv`, `work/recheck_log.tsv`).

## The letter-cipher block on f. 12

At the foot of f. 12, after "... Churf. in Beyern salvo geschehen werden;", ten lines (about 530 letters, with the
numbers 43, 45 and the sign LL) are written in lower-case letters, marked in the margin "E: Sixt: cla:" (perhaps
"ex Sixtini clave"). It is not the Malsburg key. Tried: monoalphabetic and homophonic annealing in German, Latin,
French, Italian and Dutch; homophonic with nulls; periodic IC for periods 1-15 (flat, 0.050-0.060); all Caesar
shifts; the MORITZ reciprocal alphabet (key 105); the Reuschenberg alphabet (key 2). Nothing reads. IC 0.052.

## Reading (summary; the measured text is `reading_segmented.txt`)

Spelling as the cipher gives it (u/v, i/j merged); [..] = unread; codes in <>.

- **f. 3, 5/15 Jan 1637.** "... das ich auch noch nit weiss, wo hervor unsere garnisonen hiernechst der unterhalt ...
  genommen werden soll, da die contributiones vom platten lande sowol alhier als in <239> ein ende haben; und wirt man
  nunmehr alle monat auf [..] man <193> ... zwolf viertel casselische viertel, weil die unterofficirer duppelt commis
  bekommen." Then: "es ist noch zeit, das man sich beim konig von Ungern ... [wegen] der friedenstractaten und salvum
  conductum vor die gesanten nach <128 Cöln> sollicitire; <176> wirt one <140> nit anfangen zu tractiren."
- **f. 12, Wesel 7/17 Jan.** He does not know whether to go to <148> or to the army; the recruits and Dalwig's
  Verehrungsgelder; Eberstein's <253 Regiment>; travel "durch Friesslant mit wagen und pferden zu gehen ist
  unmöglich". "Es ist von guter hant avisiret, dass man zu Regenspurg geschlossen, [den] gesanten nach <128> keinen
  salvum conductum zu erteilen"; Statthalter Nesselrode reports that the Bishop of Würzburg wrote in August; the
  Roman King; talks "apart zu <130 Hamburg> oder Lübeck".
- **f. 14, Jan.** Hermannstein (Ehrenbreitstein) and its provisioning; Obrist Hoffman's troops; marches by Marburg,
  Corbach, Brilon, the "rechte strasse von <128> auf <189>"; Jan de Werth at Cologne (clear).
- **ff. 15-16, Jan.** No audience yet; notice of the end of the Stillstand; companies and dragoons, recruiting
  patents already issued; the ambassador of <188 die Staaten>; money and horses; no chance yet to come to <129>.
- **f. 18, 14/24 Feb.** "Es seint aber die <212> ein teils so erfroren, das auch etliche zu kruppeln worden";
  the obligation over the loss before Hermannstein; the new recruiters.
- **ff. 23-24, 7/17 Feb.** The dispute over whether Hermannstein was "effectivement proviandiret"; ransom and
  "Verehrungen" for the commanders; Reichsthaler owed "auf rechnung"; "befinden nun in der that, das wir mit einem
  Frantzosen gehandelt haben"; peace talks in Picardy, nobody sent to <128>; Marggraf Sigmund of Brandenburg's
  commission; a separate peace with the imperial commissioners; "unsere garnisonen seint also verderbet".
- **f. 25, 5 Mar / 23 Feb.** <120> has resolved to content the Reuter; ransom for prisoners; letters of exchange.
- **ff. 28-29, 28 Mar.** The journey by the Watten; twelve-pound cannon and constables; Jan de Werth between Ruhr
  and <268>; the States' alliance and a muster place in Cleves; the conjunction at Cloppenburg, Quakenbrück,
  Minden, Vechta, Wildeshausen, Diepholz; the obristen Uffeln and Carpf.
- **ff. 32-33.** A French letter signed "232", 3 Apr 1637 ("par la lettre de n[ost]re ambassadeur extraordinaire ...
  à Londres ... copie"; "audict ambassadeur"; "ledict Sengell"), and German news extracts from London of 16/26 Mar
  ("<129> der Pfalz der nechst", "Printz Robert"), in the same key; paired large capitals (AA, GG, OO, XX, CC, KK)
  are name signs.

## Measurement

`measure.py` segments each decoded run into words from the DTA 1470-1670 vocabulary (forms seen at least twice,
three letters or more, plus a short list of real two-letter words) and `extra.txt` (names, spellings and French
words, each checked in context); for f. 32 the French `fr-henri4` vocabulary is added. A token is read when every
letter it gives lies in a word. Result (duplicate ff. 30-31 left out): **9,338 of 9,736 cipher tokens (95.9%)**;
193 tokens are open codes or name signs, so 97.9% of the non-code text reads. Per record: 496 96.5%, 497 96.9%,
502 92.8%, 503 95.0%, 504 96.9%, 505 97.6%, 506 97.5%, 507 96.0%, 509 88.1% (second hands). Shuffled-key control:
50-58%. The f. 12 letter block (531 letters) is not counted: it is another system.

## Remaining gaps
- letter-cipher block at the foot of f. 12 (531 letters) - blocker: no-key-material; a different system, not the Malsburg key, not simple, homophonic, Caesar or periodic; no fitting key among the 176 HCPortal key records
- about 40 three-digit codes and name signs (193 tokens: 120, 122, 129, 140, 148, 176, 193, 212 ... V, K, f, 4#, +, AA, GG ...) - blocker: open-codes; mostly single occurrences, five valued from context (128, 130, 188, 253, 273, grade I)

## Escalation
- [x] siblings: all ten records of HStAM 4 h 1411 transcribed; ff. 30-31 duplicate ff. 28-29 and served as a check copy
- [x] clear-pages: no decipherment on any leaf; the address sides (ff. 4, 13, 17) carry no cipher
- [x] known-keys: all 176 HCPortal key records of the Marburg key volumes harvested; keys 5, 30, 38, 49 tried on the digits and 2, 105 on the letter block; none fits
- [x] print: web and LAGIS search for an edition of the letters; none found
- [x] key-rebuild: digit table annealed from the ciphertext and polished over all pages; signs and five codes valued from context
- [x] retry: 236 unread groups re-checked against the scans (24 misreads, 2 doubled groups corrected, 210 confirmed)
