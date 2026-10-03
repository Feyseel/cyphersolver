# DECODE R1408, "Di Varsouia 24 Xbre 1627" (ÖStA HHStA Staatskanzlei Interiora, Chiffrenschlüssel Kt. 14 Fasc. 20 f. 176) — NOTES

**Verdict: read.** A homophonic substitution with an alphabet in plain order (odd figures 13–33 = *a b c d e f g h i l m*,
even figures 14–32 = *n o p q r s t u [x] z*), six letter-pair symbols standing for consonants, a dozen two-figure
syllables and particles in the ranges 01–09 and 40–50, the letters *a* and *m* as nulls, and thirteen three-figure
groups that are word codes. Every spelled word reads; two of the small groups and the ten word codes are glossed
from context, not read (95.2% of the 332 non-null tokens read, measured 2 Oct 2026, §3b). The letter asks its addressee to make good a promised canonry of Olmütz for one of the
sons of "this Most Serene [Queen]", i.e. of the Polish royal couple.\*

Session 2026-09-16. Ciphertext is Tomokiyo's transcription in [variable2.htm](http://cryptiana.web.fc2.com/code/variable2.htm)
("the numbers and letters are written without space in the original manuscript, but I believe my grouping into
two- or three-digit groups is fairly straightforward"). DECODE's public record: one page, *Non-decrypted*, cipher
type *Simple substitution, Homophonic substitution*, dates 1600–1799 placeholder, inline cleartext yes, transcription
exists, images and documents behind login. The image was fetched and checked on 2 Oct 2026 (§3b). The TARGETS.md
note called the letter pairs "syllables or nulls"; they are neither.

## 1. The ciphertext

[ct.txt](ct.txt): 509 tokens as Tomokiyo splits them; after joining his suggested pairs (ll zg fi pr lu th) 442
tokens: 295 two-figure groups (36 distinct), 13 three-figure groups (100 113 120 123 151 154 157 159 160 223),
56 *m*, 52 *a*, 7 ll, 5 zg, 4 fi, 3 lu, 2 pr, 2 th, and single *o*, *p*, *n*.

What gave the structure away before any solving:

- The figures 12–33 (30 absent) carry 265 of the 308 numeric tokens, and their frequency profile (29 and 16 at 35,
  21 at 29, 13 at 27, then 18, 17, 17, 15, 13, 10, 9, 9, 7, 7, 5, 4, 4, 2, 2, 1, 1) is monoalphabetic Italian
  (*e a i o* ≈ 30 each, *n l r t s c d* 10–18). IC of the numbers 0.058, dragged down by the rare groups.
- 01–09 (14 tokens) and 40–50 (15 tokens) are too rare to be letters and too even to be homophones of vowels.
- *a* and *m* are a quarter of all tokens. Treated as symbols, both anneal to the same vowel (run
  [solve2.py](solve2.py) `withletters`), which no Italian text allows, so they carry no letters. They fall mostly at
  word ends (see the marked decode below), which is the usual clerk's habit of dropping a null after each word.

## 2. Solving

1. **5-gram annealing on the numbers alone** ([solve.py](solve.py), Italian 5-gram model from `../lucca/it5.npy`,
   nulls dropped, text split at the three-figure codes): six seeds, no agreement, but seed 3 (−2.48 per 5-gram)
   already had *avere*, *questa*, *un caricato*, *aiuto*, *subito*, *bene*. Forcing distinct letters on the 19 core
   figures ([solve2.py](solve2.py)) did not help: at 253 5-grams the LM prefers *e t r s* soup.
2. **A unigram word-segmentation scorer** ([wordsolve.py](wordsolve.py)) degenerates into strings of *di la il*
   and also had a bug (swaps let core figures share a letter). Void.
3. **5-gram + dictionary coverage** ([combo.py](combo.py): LM score plus one nat per letter covered by a lexicon
   word of three letters or more, swaps only inside the core, free letters for the rare groups). From random keys,
   seeds 0 and 2 of six converge on the same key at −371 / −409; seeded from step 1's key, all three seeds land on
   it (−371, −374, −387). Reading at that point: *… un caricato d olmi. ad uno gli … suoi figlio hauendo io saputo
   in corte … uolonta di re … stata messa in esecutione … queste maesta ho stimato oficio … uoto seruitore io le so
   non suplicare … a uoler fare … prima … subito a me benigna risposta*.
4. **Controls.** The same objective annealed on three shufflings of the ciphertext tops out at −843, −865, −893
   against −371 on the real order.
5. **The alphabet is in order.** The converged core key is 13 a, 15 b, 17 c, 19 d, 21 e, 23 f, 25 g, 27 h, 29 i,
   31 l, 33 m on the odd figures and 14 n, 16 o, 18 p, 20 q, 22 r, 24 s, 26 t, 28 u on the even ones, which the
   annealer cannot have known. It fixes the two hapax figures as well: 32 = z (even series … u x z) and 12 as a
   symbol outside the alphabet. (2 Oct 2026: the image shows that "12" is the start of the code group 120, §3b.)
6. **Rare groups and letter pairs by context** (every occurrence listed by the script in the session; the readings
   below are the only ones that fit all occurrences of each symbol):
   - zg = r (*rico·rdo*, *Nicolspu·rg*, *Se·renissima*, *confe·rire*, *servito·re*); lu = d (*ricor·do*, *a·d uno*,
     *desi·derano*); fi = n (*ho·nori*, *inte·ntione*, *i·n* ×2); ll = t (*al·tri*, *in·tentione*, *tal*, *sta·ta*,
     *ques·te*, *stma·to*, *servi·tore*); th = l (*Nico·lspurg*, *ta·l*); pr = ff (*ffece*, *e·ffetuare*).
   - 01 si (*Serenis·sima*, *de·siderano*, *si degni*, *si [154]*); 05 non (*ca·non·icato*, *non è*); 06 ne
     (*intentio·ne*, *essecutio·ne*, *dar·ne*); 09 de (*de voler*, *de devoto*); 40 con (*con·fido*); 46 con
     (*con·ferire*); 41 al (*al·tri*); 42 la (*supplicar·la*); 43 di (*di supplicarla*); 44 de (*de li suoi figli*);
     45 da (*da·to*, *dar·ne*); 47 che (×3, all at clause openings); 50 se (*se·renissima*, *es·se·cutione*,
     *se·rvitore*).
   - Single *o*, *p*, *n* (one each) fall inside otherwise complete words (*che {12} o mi fece*, *hauer p dato*,
     *figli n*) and are read as nulls or transcription slips. (2 Oct 2026: the *o* is the 0 of code 120, §3b.)

## 3. The reading

[plaintext.txt](plaintext.txt); [decode.py](decode.py) regenerates it (`-n` marks the nulls, `-g` glosses the codes).

> Mi ricordo che, fra li altri honori che [120] mi fece in Nicolspurg, mi confido d'hauer dato intentione a questa
> Serenissima [100] [113] de uoler conferire un canonicato d'Olmiz ad uno de li [123] suoi figli; hauendo io {03}
> saputo in [160] corte che tal uolontà di [120] non è [151] stata messa in essecutione, sì [154] desiderano [157]
> queste Maestà, ho stimato oficio de deuoto seruitore, [154] io le sono, di suplicarla, [154] fo, a uoler far
> effetuare [160] [223] [159], prima {04} si degni darne subito a me benigna risposta.

Spellings as enciphered: *Seerenissima* (a doubled 21, confirmed in the image), *ffece*, *oficio*, *suplicarla*,
*effetuare*, *essecutione*, *Olmiz*, *Nicolspurg*. Single consonants and *essecutione* are ordinary for 1627. The
earlier *stmato* was a gap in the transcription: the image has the 29, *stimato* (§3b).

Glosses (inference, not reading): [154] ×3 = *come* (fits *sì come desiderano*, *come io le sono*, *come fo*);
[160] ×2 = *questa* (*in questa corte*, *effettuare questa …*); [151] = *ancora*; [120] = the addressee's title
(two contexts since §3b merged {12} into it); [100] [113] = the Queen's title; [123] = *Serenissimi*; {03}, {04},
[157], [223] [159] open.

**Alternative translation (30 Sept 2026).** Raised while quotations were pulled for Lasry's list. *confido* is
40 23 29 19 16 (con-f-i-d-o) in line 3 of `ct.txt`, followed by a null *m*; the system has no sign for an accent, so
the word may be *confidò* (passato remoto, 3rd person, like *fece* in the same sentence) as well as *confido*. With
*mi confidò*: "among the other honours [Your Lordship] did me at Nikolsburg, [you] confided to me that [you] had
given this Most Serene [Queen] to understand that [you] would confer a canonry of Olmütz on one of [her] sons". It
arguably fits better: whoever gave the Queen to understand that he would confer the canonry (*d'hauer dato
intentione ... de uoler conferire*, one subject for both infinitives) must be able to confer it, the Bishop; and the
confidence becomes one of the *honori*, which with *mi confido* have no object in the sentence. The figures do not
decide it, so the page keeps "I am confident" and gives *mi confidò* as an alternative (reading list, and a clause in
Context); the same alternative is added to `plaintext.txt` and to §4 below. Not changed here (outside this folder): `papers/lasry/excerpts.json` and `decode_updates/decryptions/R1408.txt`
carry only the *confido* translation or text.

## 3a. The code groups, tried again (30 Sept 2026)

Lasry asked for fewer gaps in the quoted text. Nothing new can be *read*: there is no image, key or sibling here, so
every code value stays a gloss (I). What was done:

- **A continuous conjectural reading** (added to `plaintext.txt` and the page): the glosses of §3 plus two new ones,
  {03} = *poi* ("hauendo io poi saputo", having since learned) and {04} = *però* ("prima però si degni", but first
  deign), and [223] [159] = *sua promessa* after [160] (*far effetuare questa sua promessa*). [157] stays open (an
  adverb: *sommamente*, *concordemente*). [100] [113] are two groups; the gloss *Regina* covers the first only.
- **The alphabetical-order hypothesis tested.** If the three-figure code were one-part alphabetical, *come* (154,
  the firmest gloss, three contexts) would put the *c*-words near 150, and *Regina* 100, *Serenissimi* 123, *ancora*
  151 and *questa* 160 would all be out of place. An alphabetical set exists: 160 *cotesta* (both contexts: *in
  cotesta corte*, *effetuare cotesta …*), 159 a *co*-word between *come* and *cotesta* (*concessione*, *cortesia*),
  157 a *con*-word (*concordemente*), 151 a *c*-word before *come*, 120/123 late *b*–early *c* (120 *Cardinale* fits
  "tal uolontà di [120]" if the addressee is not Dietrichstein himself; the letter is in the Imperial chancery's
  files, and "a uoler far effetuare" asks the addressee to make someone else carry the promise out, which would
  suit a letter to the Emperor, the Queen's brother), 100/113 *a*–*b* words. Against it: the two-figure syllables
  01–09 and 40–50 are not in alphabetical order, and no code value is confirmed. Undecided; both sets are on the page.
- **Leads for a real reading**, from the DECODE harvest (`catalogue_harvest/decode/list.json` in the main checkout):
  R1409 (Kt. 14 Fasc. 20 f. 178, four pages, cipher types 1,2 as R1408) may be a sibling letter in the same key;
  R1392–R1406 (ff. 142–169) and R1410 (f. 181) are key records. All behind DECODE's login.

## 3b. DECODE images, the sibling candidate and the key records (2 Oct 2026)

Fetched with the project cookie (`../bordeaux/decode/cookie.txt`, still valid) into [decode/](decode/): the R1408
image, R1409 (3 images and DECODE's transcription), R1410 (3 images) and the key records R1392–R1406 (45 images,
8 DECODE key transcriptions). Images and the logged-in record pages are git-ignored (`decode/.gitignore`).

**R1409 (f. 178) is not in this key.** It is a different system: dot-separated figures with long underlined runs,
1,328 tokens in DECODE's transcription (MEG, 2020; parsed to [r1409_ct.txt](r1409_ct.txt), `_` = underlined):
two-figure 12–37 (71%, 18 and 28 the commonest), three-figure 101–195 (about 70 distinct, 106 and 116 the
commonest), 96 ×28, a few 01–08 and 54–98, no letter nulls. [r1409_test.py](r1409_test.py): the R1408 alphabet gives
*ulauraqtobnqtaucnoau…*, −5.05 per character (it-cinquecento, order 4, no spaces) against −2.38 for R1408's own
figures under the same key, and ranks 67th of 500 random keys over the same figures (Latin, German, French, Spanish
the same). Ruled out. A ciphertext-only attempt on it ([r1409_solve.py](r1409_solve.py), [r1409_solve2.py](r1409_solve2.py):
homophonic letters, then letters or pairs for every symbol, Italian and German, shuffled control) did not converge
(Italian −2.61 real vs −2.85 shuffled; German degenerate); R1409 is outside this target and stays unread.

**No key record fits R1408.** None has an ordered numeric alphabet on 13–33 with letter nulls and codes 100–223:
R1392 German (1592); R1393, R1394, R1396, R1397, R1399, R1400 French keys of the Henri IV years (Biron, Montpensier,
Dombes); R1395 and R1405 Latin graphic-sign keys for the Turkish court; R1398 French (f. 153); R1402 *Cyphra in
Moscoviam*; R1403 a Latin/German Polish key in graphic signs; R1404 an alphabet sheet; R1406 a German place-name
nomenclator *pro Federico …*; R1401 a graphic-sign letter; R1410 a German letter with inserted code numbers. No
gloss for any open code.

**The image corrects Tomokiyo twice and confirms the addressee.**

- Line 2 *a 12 o m* is the code group **120**, written 1-2-0 exactly as on line 8 (the clerk's 0 and *o* are one
  shape). The hapax {12} and the stray null *o* disappear, and [120] now has two contexts, *fra li altri honori che
  [120] mi fece in Nicolspurg* and *tal uolontà di [120]*: the addressee's title (*V.S. Ill.ma*), still a gloss.
- Line 10: between 26 and 33, where Tomokiyo has a double space, stands a 29 (*i*): *stimato*, not *stmato*.
- *Seerenissima* (50 21 zg) is as enciphered.
- The null *a* (tall stem) and the figure 2 (flat base) are distinct shapes, so {03} and {04} are two-figure
  groups and not codes 203/204. The single *p* (line 3) and *n* (line 6) stand inside complete words as written.
- A docket at the foot of the page, faint, reads *… Card. Dietrichstein*; at the foot of an Italian letter that is
  the addressee, which confirms §4's inference.

[decode.py](decode.py) applies the two corrections (`-t` gives Tomokiyo's text as filed). Measured on its tokens:
442 tokens, 110 nulls, 332 significant, 16 unread (ten codes in 14 occurrences, plus {03} {04}) = **95.2% read**.
`lm.best_language` on the read words: Italian first.

## 4. What it says\*

Nikolsburg (Mikulov) was the seat of Cardinal Franz von Dietrichstein, Bishop of Olmütz 1599–1636, in whose gift
a canonry of Olmütz lay; the writer had been received there and had then told "this Most Serene [Queen]" in Warsaw
that the Cardinal meant to give one of her sons an Olmütz canonry (reading *mi confido*; with *mi confidò*, §3, the
Cardinal had given the Queen that hope himself and told the writer so at Nikolsburg). The Queen of Poland in December 1627 was
Constance of Austria, Ferdinand II's sister, whose younger sons (John Albert, Charles Ferdinand) were being placed
in church benefices in exactly these years. The letter, written from Warsaw to the Cardinal on 24 December 1627,
says the promise has not yet been carried out, that "these Majesties" (Sigismund III and Constance) want it, and
asks either that it be done or that he be given a prompt answer. The addressee is therefore Dietrichstein and not
the Emperor,\* which would explain why the piece sits in the Chiffrenschlüssel series rather than in a
correspondence. The writer is not named in the cipher; an Italian-writing agent moving between Nikolsburg and
Warsaw in 1627 is the profile.\*

\* Inference from the text and general history; nothing in the record names sender or addressee. The DECODE
cleartext frame (login) or the Dietrichstein papers would confirm it.

## Remaining gaps

- **[100] [113] [123] [151] [154]×3 [157] [159] [160]×2 [223]**: glossed from context (§3, §3a), not read.
  Blocker: no key material. There is no sibling in this key in Kt. 14 Fasc. 20 (R1409 ruled out) and no matching key
  in R1392–R1406 or R1410 (§3b). The Dietrichstein family archive at Brno (Moravský zemský archiv, I believe fond G 140)
  is where the received letter, a decipherment or the key would be; not online.
- **[120]×2**: the addressee's title from two contexts and the docket; blocker the same (no key material).
- **{03} {04}**: one occurrence each; glossed *poi*, *però*. Blocker: too short (hapax groups).
- Single *p* and *n*: inside complete words in the image; read as nulls. Nothing to read.
- Sender: not named in cipher or clear. R2179 from the same article (undelimited digits) is a different system and
  untouched.

## Escalation

- Siblings: R1409 (f. 178) tested and ruled out (different system, §3b); R1410 is German with different codes.
- Clear pages / known keys: the fifteen key records of the fascicle (R1392–R1406) checked, none fits (§3b).
- Image: fetched and read against the transcription; two corrections, one code merged, addressee docket found.
- Print: no edition of the letter known; the Dietrichstein correspondence (Brno) is the remaining source, offline.
- Key rebuild: the alphabetical-order test for the codes (§3a) stays undecided; with 16 tokens in twelve values the
  text cannot fix them.

## Files

- [ct.txt](ct.txt) — Tomokiyo's transcription, 509 tokens as he splits them.
- [solve.py](solve.py), [solve2.py](solve2.py) — 5-gram annealers (numbers only; with distinct core; with *a m* as symbols).
- [wordsolve.py](wordsolve.py) — lexicon loader and the word-segmentation scorer (the standalone solver in it is the failed step 2).
- [combo.py](combo.py) — the 5-gram + coverage annealer that converged; `key_combo_seeded.json`, `key_combo_rand.json`, `key_seed3.json` its outputs.
- [decode.py](decode.py) — final key and the two image corrections, writes the plaintext; [plaintext.txt](plaintext.txt).
- [decode/](decode/) — DECODE images (git-ignored), DECODE transcriptions `DOC_R*.txt` of R1408, R1409 and the key records.
- [r1409_test.py](r1409_test.py), [r1409_ct.txt](r1409_ct.txt) — R1409 parsed, the R1408 key against random keys.
- [r1409_solve.py](r1409_solve.py), [r1409_solve2.py](r1409_solve2.py), [r1409_solve2_it.txt](r1409_solve2_it.txt) — the failed R1409 annealing runs.
- Corpus and 5-gram table are `../lucca/corpus` and `../lucca/it5.npy` (not committed there either).

Checked: token counts, convergence from random and seeded starts, three shuffled controls, alphabet order, every
occurrence of every rare symbol against its reading, word-level Italian throughout, the manuscript image (2 Oct 2026),
R1409 and the key records. Not checked: sender, the word codes. User must verify: §4 before it is repeated anywhere; DECODE registration
and any note to Tomokiyo are Daniel's steps.
