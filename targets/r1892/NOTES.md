# R1892 — an Orange prince on the émigré "rassemblement", c. 1795 (KHA, Prins Willem V, inv. 339)

Status: read in part

Lasry review (25 Sept 2026): In private communications, Lasry wrote that he independently solved it in 2021 but his solution has not been published. Kept in the ciphertext-only list (outcome.first_break = 'unpublished prior').

DECODE R1892 ("unkmown (Germany) to Prince William V", dated 1 Jan 1795, Non-decrypted, 2 pp.). KHA The Hague,
Prins Willem V, bundel A18 nr. 339. The archivist's pencil note on page 1: "brief uit KHA bundel A18 nr 339 —
Onderdaad geen nomenclatuur" (no nomenclator found). Images: DECODE IMG_R1892_I9358_P1, IMG_R1892_I9359_P2
(photocopies, photographed sideways; login images, git-ignored in `img/`).

## System

A 6×6 digit square. Each letter is written as a vertical pair of digits 1–6, the top digit over the bottom one
(read here as a token TOP+BOTTOM). Monoalphabetic, one sign per letter, with a few extra graphic signs (circle
with a dot, Λ, Δ, γ, ⊣H, cross, etc.) that stand for frequent words or names and are not in the square. Clear
words are mixed in on page 2.

Key recovered (ciphertext-only, quadgram annealing on page 2's Dutch; page 1 then read straight off in French):

| token | 11 | 12 | 13 | 14 | 15 | 21 | 22 | 23 | 24 | 25 | 31 | 32 | 33 | 34 | 35 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| letter | t | w (Dutch) / z (French -ez) | y, ij | x | l | z | o | k | f | m | d | n | v | h | b |

| token | 41 | 42 | 43 | 44 | 45 | 51 | 52 | 54 | 55 | 65 |
|---|---|---|---|---|---|---|---|---|---|---|
| letter | g | u | a | s | p | c | r | q | i | e |

Rare tokens 53, 61, 62, 63, 64 occur 1–3 times and are probably misreadings of the photocopy.
The square is not in alphabetical order; no key sheet is known.

## What it says

**Page 1 (French, all cipher).** The writer's father ("mon père") is sending Nagel (A. W. C. van Nagell, the
Orange envoy in London) back to the ministers to press for an answer on the representations made about the
*rassemblement*. In case General Dundas ("le général Vundas" in the cipher) declares that the pay will stop or
that the troops must embark, "il faudroit y souscrire et vous borner uniquement à tâcher d'obtenir de pouvoir
donner une gratification à ceux qui ne voudroient se soumettre". The recipient is to tell the troops on what
footing they will enter the service of S.M.B. (His Britannic Majesty), using an adapted copy of the paper meant
for them "dans le premier moment où il étoit question de leur embarquement", which is among the writer's papers.
Finally: do not charge the expense of my lodging to the account; pay it from the money of mine you hold.

**Page 2 (Dutch postscript, "het volgende schrift ... in het hollandsch met cijffer").** If the troops stay
together, the rassemblement is to be kept together; volunteers and officers are to be named and employed; the
officers who will not serve are to be given a set number of days to choose; it is hardly possible that the
French have not offered them service; "ieder [1000?] man kunnen plaatsen". The writer has had no answer for
weeks to his first letter and would rather have stayed at "Nam..nburg"; the writer hopes the recipient can
engage no one further. Closing in French: "le prince [sign] me marque en outre ... vous aurez la bonté de
communiquer le contenu de ce chiffre à mon frère" (the last word is ciphered, `63 25 22 32 44? 54? 65 52 65`,
read as "à mon frère" with two uncertain pairs).

Decrypts: `decrypt_p1.txt`, `decrypt_p2.txt`; transcriptions `transcription_p1.txt`, `transcription_p2.txt`;
`solve.py` (annealer), `apply.py` (key).

## Who and when

A son of William V (the Hereditary Prince or Prince Frederick; "mon frère" is the other) writing to an officer
in charge of the Dutch émigré troops gathered in Germany under British pay, after the flight of January 1795.
Page 1 cites a letter "en date du ... décembre". Update 2 Oct 2026: the writer is Prince Frederick, in England,
c. late Nov - early Dec 1795 (see "R2242 values applied", Print and date). DECODE's 1 Jan 1795 is probably an archival date; the content
fits winter 1795/96, when the rassemblement's transfer to British service and embarkation were being negotiated.
The attribution "to William V" is the file's provenance, not the addressee.

## Word signs and doubtful lines (second pass, 21 Sept 2026)

Every sign occurrence was listed with its decrypted context (`apply.py` now renders the circle sign as DE).

| sign | n | value | grade | evidence |
|---|---|---|---|---|
| circle with dot | 27 | **de** (French and Dutch) | H | d'aller *de* nouveau; d'obtenir *de* pouvoir; au service *de* S.M.B.; question *de* leur embarquement; op *de* volgen*de* wijze; bepaal*de* dagen; *de*n generaal |
| γ | 5 | zich | M | degene die *zich* vrijwillig; die hier *zich* … willen geëmployeerd |
| c-shaped sign | 5 | te | M | de keus *te* maken; in cijffer *te* vinde[n] |
| G | 7 | ik | M | *ik* wist wat in bovenstaande; *ik* mijn eerste [brief] |
| ⊣H | 9 | a verb auxiliary before *willen* (zouden?) | I | three times directly before *willen* |
| hook | 7 | a conjunction before G (dat?) | I | usually directly before G |

The other ~20 signs occur once to four times each; context does not fix them, and the transcriber's labels for them
may merge or split shapes. They stay unread.

- **Closing, re-read at full resolution:** top 4 2 2 3 2 5 6 5 6 over bottom 3 5 2 2 4 2 5 2 5 = 43 25 22 32 24 52 65
  52 65 = **à mon frère** (H). The first transcription's 44/54 were misreadings of 24/52. The group before
  "me marque" is 15 65 45 52 55 32 51 65 = **le prince** (H).
- **Page 2, line 1, re-read:** [de] 32 41 65 32 65 52 43 43 15 35 65 52 11 55 32 51 13 = "**den generaal Bertincy**",
  probably General Bentinck (C: n/r and k/y are each one stroke apart in this photocopy; the name is not certain).
- **Page 2, line 24:** re-examined; the two digit rows drift and several pairs are ambiguous (… *dert* … *gesteld is
  geweest*). Still read only in fragments.

## Open

- About 20 rare signs; the values proposed for γ, c, G above are probable, ⊣H and hook only guessed.
- Page 2 line 24 middle; page 1 line 1.
- Exact writer and addressee: "le prince" and "mon frère" are both named; "den generaal Bentinck" is mentioned.

## Prior art

DECODE status Non-decrypted; no decipherment on the record or images. Searched project notes: targets/fagel1804/NOTES.md
mentions R1892 only as "a dense two-digit/symbol system" unrelated to R2238. Key records R2240 (Orange name key,
four-digit) and R2233 do not apply.

## R2242 values applied to R1892's signs (2 Oct 2026)

R2242 (same key) gives word-sign values from its page-1 clear text and from context (`../r2242/NOTES.md`).
`apply.py` now carries a sign table (`SIGNS`, with grades) and `--measure`; `../r2242/measure_sense.py` scores the
result with the shared lang/ models. Each R2242 value was tried at every occurrence of the matching R1892 label:

| R1892 sign | R2242 value | result | contexts |
|---|---|---|---|
| bar-H | zoo | **adopted, M** | "in te neemen de[n], [zoo] het moogelyk ys" |
| gt (>) | als | **adopted, M** | "bepaalde dagen <hook> [ik] [als]dan" and "… [als]" twice: *alsdan* |
| lambda | dat | **adopted, M** | "op de volgende wyze [dat] alle heeren officieren"; "willen laaten, [dat] te laaten"; "kunnen [dat] weeten"; R2242 four times |
| parallelogram | brief | **adopted, H** | "myn eerste [brief]" (shape fixed by R2242 p1 clear text) |
| box (p1, the same parallelogram) | lettre | **adopted, M** | p1 l1 "… [lettre] du … en date du … décembre" (French counterpart of brief) |
| 8 | zijn | adopted, I | "noch hier te [zijn] en"; "die [zijn] … gedaan"; "maaken in [8] neemen" does not fit, so I only |
| perp | om | already adopted (M) | |
| phi | Frankrijk | ruled out | "alsdan [phi] dezelve de keus te maaken", "schryf <Y> [phi] naam": a short word (aan? hun?), not France |
| S | moeten | ruled out | "reeds [S] weeken" needs a number or "eenige"; R2242's long S is a different shape |
| Y-cross | zee | ruled out | four contexts ("gedaan <cf> [Y-cross] antwoord te laten") fit no "zee"; R1892's label covers a different sign |
| x | weinig | ruled out | "geeven tegen [x] bepaalde dagen" |
| cross | mogelyk | ruled out | "weeten [cross] de geene die hier zich …"; "ook [cross] gewenst" |
| check | zonder | ruled out | "naam [check] myn nader" |

Found while doing this: **f = aan** (M): "niet [aan]geboden hebben" (the French have not offered them service),
"[aan]geeven tegen … bepaalde dagen", "myn [aan]yomst" (aankomst, with the k/y confusion already seen in
"Bertincy"). Not R2242's script L (= uit), which is a different shape.

The other signs (⊣H 9, hook 7, slash 5, cf 4, Y 3, P 3, psi 2, 7 2, and the singletons) were retried with the
pooled values; none takes an R2242 value, and R2242's open signs (ψ, Δ, %) are open there too.

**Measured** (same transcription, `apply.py --measure` / `measure_sense.py`, fr-1750-nospace on p1 and nl-modern
on p2; `<struck>` and comment lines excluded):

| | tokens given a value | tokens read as sense |
|---|---|---|
| before (signs of 21 Sept: de, zich, te, ik) | 1,865/1,951 = 95.6% | 1,726/1,951 = 88.5% (p1 991/1,053, p2 735/898) |
| after (2 Oct) | 1,882/1,951 = 96.5% | 1,757/1,951 = 90.1% (p1 994/1,053, p2 763/898) |

The 21 Sept profile figure (94%, 1,848/1,958) used a scratchpad script that is gone and did not count zich/te/ik.

**Print and date (2 Oct 2026).** Colenbrander, *Gedenkstukken* II (1795–1798), full text on
resources.huygens.knaw.nl, searched for Dundas, Osnabrück, rassemblement, Nienburg/Nienbourg, Bentinck,
gratification, Banquier; GS II pp. 886–894 read. R1892 is not printed, but the volume fixes its setting:
- no. 724 (7 Oct 1795) is Prince Frederick writing to General Dundas *from Nienburg*, where he commanded the
  rassemblement; R1892 p2's writer "would much rather have stayed at Nam..nburg" — Nienburg (M). The writer is
  therefore **Prince Frederick**, by then in England (the Princess, 26 Nov 1795, GS II p. 893: "Mon fils cadet nous
  est arrivé … C'est aussi pour le rassemblement qu'il est venu"), and "mon frère" is the Hereditary Prince.
- no. 734 (Hereditary Prince to William V, 25–27 Dec 1795, pp. 893–894): General Dundas's new orders (Henry Dundas,
  Horse Guards, 8 Dec 1795) decided the rassemblement against it; the troops not taking British service were to go
  to Nassau. R1892 p1 anticipates exactly this ("au cas que le général Dundas vous déclare … que les troupes
  devroient se laisser embarquer"), so it was written before those orders reached the continent: late November or
  early December 1795. DECODE's 1 Jan 1795 is wrong (to queue separately; decode_updates not touched here).

## Remaining gaps
- about 20 rare word signs (1-4 occurrences each), plus ⊣H and hook - blocker: open-codes; retried 2 Oct 2026 with R2242's values (five adopted, six ruled out, table above); the rest occur only here, no key sheet, and the letter is not in print
- page 2 line 24 middle; page 1 line 1 - blocker: illegible; photocopy; the two digit rows drift and several pairs are ambiguous (re-examined 21 Sept at full resolution)

## Escalation
- [x] siblings: R2242 (same key) read; its sign values applied here 2 Oct 2026; R2240, R2233 checked, do not apply; R2236/R2237/R2239 use a different word list
- [x] clear-pages: no clear decipherment on the record; page 2 clear words used
- [x] known-keys: R2240 and R2233 tried, no fit
- [x] print: searched 2 Oct 2026 - Colenbrander, Gedenkstukken I-II full text (resources.huygens.knaw.nl retroboeken) for Dundas, Osnabrück, rassemblement, Nienburg/Nienbourg, Bentinck, gratification, Banquier, and GS II pp. 886-894 read: not printed; nos. 724, 733, 734 give the writer (Prince Frederick) and the date (late Nov - early Dec 1795)
- [x] key-rebuild: digit square rebuilt by quadgram annealing; sign values from context (de, zich, te, ik), then from R2242 (zoo, als, dat, brief/lettre, zijn) and f = aan, 2 Oct 2026
- [x] retry: 2 Oct 2026 - every sign occurrence rerun with R2242's values and regraded (table above); page 2 line 24 and page 1 line 1 were re-read at full resolution on 21 Sept and stay illegible
