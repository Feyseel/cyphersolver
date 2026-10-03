# Lanssac to Charles IX, Warsaw, 26 April 1573 — BnF fr. 4735 no. 51, f. 124 — NOTES

**Verdict: read; key carried to three sibling letters (section 8) and, in session 3 (section 9), to ff. 154r (97 %), 154v (92 %), 156r (97 %) and 156v (88 %), all read in part with gutter-blocked gaps; the 9 May letters ff. 182-189 are in clear.** Both cipher passages of the letter are recovered, 96 of the 100 signs. The key is a homophonic
letter cipher with two or three signs per common letter, a dozen syllable and word signs (*et, nt, st, de, ou,
car, Allemagne, pour, ns*), and the Court decipherer's marginal gloss, cut by the gutter on the microfilm, gives
fragments of both passages. Lanssac writes that, after the dangers French travellers now meet in Germany, the
obstacles in Thuringia, Meissen and the Mark of Brandenburg delayed him so much that he reached Poland
(Międzyrzecz) only on 25 February, and that without the escort of the King's pensioners Alexander von Miltitz and
Georg L(u)e(l)z he would "at the least have been detained or prevented from passing on". The rest of the letter
is in clear and refers to the *recueil* on the state of Polish affairs that follows it in the volume (no. 52,
ff. 126–127, "Deschiffrement du memoire"), which is why the catalogue lists a decipherment for the mémoire and
none for the letter.

Session 2026-09-17. Catalogue item 3 (class A). The catalogue entry gave f. 126; the BnF notice puts the folio
before the item number: no. 51 is f. 124 (canvas 242 of the Gallica scan btv1b9060724s), no. 52 (the mémoire in
clear, "Estat des affaires de Pollongne selon que le Sr de Lanssac y a peu aprendre") is ff. 126–127 (canvases
244–247). Confirmed on the images.

## 1. Prior art

- S. Tomokiyo, "French Ciphers during the Reigns of Charles IX and Henry III" (cryptiana, henryiii.htm), section
  "Ciphers of Monluc and Lansac, Sent to Poland (1573)": lists Lansac's cipher letters at ff. 124, 132, 138, 154,
  160, 164 and 331 and prints a reconstructed table (henryiii_Lansac.png, 689 × 285 px) with no transcription or
  reading of any letter. He notes that "a pair of symbols" seems "to delete symbols in-between" (ff. 154, 156).
  The letter is not on his unsolved page. His table is right for most of the first row and for the syllable
  signs, but its first row is **shifted by one letter from *m* onward** (his *ſ = m, L = n, ʒ = o, б = p, ⊨ = q,
  9 = r, ʓ = s, o+ = t* read here *ſ = n, L = o, б = qu, ⊨ = r, 9 = s, ʓ = t, o+ = u*), his row-3 *Γ = i* is *e*,
  his *‡ = h* is *d*, and his *pour* sign is the letter *h* in one of its two shapes. The differences are in
  key.tsv, column "Tomokiyo".
- Noailles, *Henri de Valois et la Pologne en 1572* (1867), vol. III (archive.org henridevaloisetl03noaiuoft):
  prints Monluc's and Lanssac's Polish correspondence selectively; the 26 April letter is not in it (OCR
  searched for "Lanssac", "26 avril", "Varsovie"). Monluc to Lanssac of 31 March 1573 and the "Avis de Varsovie"
  of 9 April are.
- DECODE: fr. 4735 does not appear in the French records harvested on 17 Sept 2026 (research/gallica_sweep/decode_France.html).

## 2. The documents

Gallica IIIF, `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060724s/f<N>/full/full/0/native.jpg`, 4417 × 6483 px
microfilm scans, all canvases labelled NP; canvas ≈ 1.76 × folio (rectos, and versos only when written). Fetched
with fetch_range.py one page at a time; Gallica answers 429 after some 25 requests and the script backs off.

| folio | canvas | item |
|---|---|---|
| 121 | 238 | no. 49 (Latin arrêt against Coligny) |
| 124 | 242 | **no. 51, Lanssac to Charles IX, 26 April 1573** — 4½ lines in cipher, gloss in the left margin |
| 126–127 | 244–247 | no. 52, "Deschiffrement du memoire … Estat des affaires de Pollongne", clear |
| 152 | 292 | no. 58, Noailles to the King |
| 154, 154v | 294 (dup. 296), 297 | no. 60, Lanssac to Anjou, 24 April — 20 + 17 lines of cipher, marginal decipherment |
| 156–157 | 300–303 | no. 61, Lanssac to Catherine, 24 April — cipher blocks, marginal decipherment |
| 160, 164 | c. 307, 314 | nos. 63, 65, Lanssac to the King and to Anjou, 1 May (fetched, not used) |

The "déchiffrement" the catalogue notes for the siblings is not a separate leaf but a **decipherment written in
the outer margin**, line by line beside the cipher; the microfilm cuts it at the gutter so only the ends of its
lines survive (img/f154_margin*.png, img/f154v_margin*.png). f. 124 has the same kind of gloss beside its two
passages: "…es dangier", "…d'Allemagne", "…qui passent" beside ll. 1–3 and "moins esté retenu", "…ou oultre"
beside ll. 9–10.

## 3. The cipher

Signs are separate graphic symbols (crosses, bars, figures, letter-like forms), written continuously with commas,
points and short bars as word separators. Frequencies over the 741 tokens transcribed (f. 124, f. 154 block 1,
f. 156 block 1, f. 154v l. 1): e-signs 131 (17.6 %), r 65, a 54, s 50, n 49, u 44, t about 40, o 34 — a French
letter profile once the homophones are merged. Design, from the 47 signs met:

- **Letters:** a ⊤ π H · c 7 ⋔ · d ‡ · e ✕ ✱ Γ Δ · f o- · g ∞ · h + · i ⊢ ϙ · l 3 ⊥ · m 8 ᥙ · n ſ o-o · o ꞔ L ·
  p y N · qu ꞗ · r ϕ ⊨ · s 9 Lo IIII ттт · t ʓ ттт · u/v o+ ff o+o. (b, x, y, z not met with certainty; three
  signs — 4, ⊓, ʒ — occur 4–11 times in the siblings and are unread.)
- **Syllables and words:** *et* ♁ (a second form of it is *nt*; the transcription does not separate them), *nt* ꝸ,
  *st* 8 with a dot, *de* ᒐ and ꝛ, *ou* ᛏ, *ns* Λ, *car* Z, *Allemagne* Z with a lower curl, *pour* †.
- No nulls found in f. 124. The "deleting pair" Tomokiyo saw on f. 154 was not needed: the pairs of bars enclose
  single signs that read as letters (|ϕ| = *r* in *retenu*).

## 4. How the key was recovered

1. **Crib from the glossed sibling.** f. 154v l. 1 reads, beside the gloss "Car je n'ay pas cinquante escuz":
   Z ⊢✕ | ſπϙ | y⊤9 | 7⊢ſꞗπſʓ✕ = *car ie nai pas cinquante*. That fixed Z = car, ⊢ = i, ✕ = e, ſ = n, π ⊤ = a,
   ϙ = i, y = p, 9 = s, 7 = c, ꞗ = qu, ʓ = t, and showed that Tomokiyo's first row is off by one from *m*.
2. **Passage 2 of f. 124 by hand** against its gloss: † ⊥ ✕ . 8 ꞔ ⊢ o-o 9 . ✱ 8̣ Γ . ϕ ✕ ʓ ✱ ſ o+ = *pour le moins
   esté retenu* gave 8 = m, ꞔ = o, o-o = n, ✱ = e, 8̣ = st, Γ = e, ϕ = r, o+ = u; then ᛏ Γ ᥙ y ✕ 9 7 + ✱ . ᒐ =
   *ou empesché de*, y π 9 Lo ✕ ϕ ꞔ ff 3 ттт ⊨ Γ = *passer oultre*, ᥙ . π ꟿ Lo = *mais*.
3. **Annealer over the whole transcription** (solve.py: French 5-gram model targets/sp53/fr5.npy, 24-letter alphabet,
   symbol → letter or short code, the crib letters pinned). Seeds agree on the free signs to within 2–8 rare ones
   and return ‡ = d, Lo = s, ⊥ = l, L = o, ᥙ = m, 3 = l, ттт = t, which read gloss words never used as cribs in
   the siblings: *les dangiers*, *l'autre* (gloss "causé l'autre"), *causé*, *beaucoup*, *grant seigniur*
   (gloss "grand seigneur"), *du monde* (gloss "que du monde"), *changement*, *sur la teste* (gloss "sur la
   teste"), *recommandé*, *doubte ou vous mettre*. The transcription of the siblings (tokens.txt) is a first pass
   with known glyph conflations (plain 3 vs hooked ʓ, three vs four strokes, the two cross forms, the two *et*
   forms) and is not offered as a reading of ff. 154–156.
4. **Lattice decode of f. 124** (lattice.py): each sign given its candidate values, beam search on the 5-gram
   score; the two passages come out as in reading.txt, with the choices listed there sign by sign.
5. **Controls** (controls.py, controls.log, 741 tokens). Pinned run, real order: −2193 to −2198 over three seeds.
   Pinned run on three shufflings of the same tokens: −2924, −2973, −3009. Blind run (nothing pinned): one seed
   reaches −2033, a *better* score than the pinned key, but recovers only 6 of the 21 crib letters; the other two
   seeds recover 0 and 4. So the language model alone does not find this key from a transcription this noisy;
   the cribs and the glosses do, and the model then fills the remaining signs consistently with words the cribs
   never touched.

## 5. Reading

reading.txt has the full letter with the clear text. The two passages:

> Sire, [despuis? les dangiers qu'encontrent en Allemagne les françois qui passent, et vostre ser{o r h e}] Les
> empeschementz et les plus grandes causes qui ayent esté depuis deux {ans} … toute la Turinge, Misnie et Marche
> de Brandebourg m'ont tellement retardé que je n'arrivay en Polongne à Mezeritz que le vingt-cinquiesme de
> febvrier. Et sans la faveur que j'ay receue d'aulcuns des serviteurs et pensionnaires de vostre Majesté,
> principalement des Sieurs Alexandre de Militiz et George Luelz(?), qui me y ont accompagné avec bonne et forte
> troupe de leurs amis et assisté de leurs moyens, j'eusse sans doubte [pour le moins esté retenu ou empesché de
> passer oultre. Mais], la grace à Dieu, je me suis rendu il y a desjà long temps avec Monsieur de Valence …

The Miltitz were Saxon nobles in French pay; Mezeritz (Międzyrzecz) is the first Polish town on the road from
Frankfurt an der Oder to Poznań. The "dangers" are the hostility to Frenchmen in Protestant Germany after
St Bartholomew's Day, which is why this passage is in cipher and the itinerary is not. Lanssac reached Monluc
in Warsaw in time for the election Diet (opened 5 April); Anjou was elected on 11 May.

## 6. What remains uncertain

- Passage 1, first word: ꝛ 9 N ff ϙ IIII is read *despuis* (ꝛ = *de* and N = *p* on this one occurrence each);
  the gloss end "…es dangier" is compatible with "…uis les dangiers" but the gutter takes the start.
- *françois*: o- ⊨ ⊤ ſ ⋔ ꞔ ϕ 9 gives *fran-c-o-r-s*; the seventh sign must be the *i* sign ϙ (P with a loop),
  which this hand writes close to the *r* sign ϕ, or the word is not *françois*. *qui* rests on the gloss; the
  cipher has ꟿ Γ, and ꟿ reads *i* in *mais*.
- Passage 1, end: *et vostre ser* + four signs ꞔ ϕ + ✱ (*o r h e* under the key), probably *service* with a
  misread sign; left in braces.
- The two forms of the *et* sign (*et* / *nt*) and of the cross (*h* / *pour*) are told apart by context here,
  not by the transcription.
- Passage 2 is read in full and agrees with both gloss fragments.
- Not done: reading ff. 154–164 in full (they carry their own decipherments in the margin, so nothing new is
  locked in them), and the f. 331 letter Tomokiyo lists in the same cipher, which has no decipherment noted.

## 8. The other Lanssac letters, read with the same key (second session, 17 Sept 2026)

The "déchiffrement" the catalogue credits to nos. 60, 61, 63, 65 and 70 is the gutter-cut marginal gloss, so their
cipher passages had never been readable from the scan. With the key the three letters that matter for the election
read in substance (reading_siblings.txt; tokens in f160_tokens.txt, f164_tokens.txt, f174_tokens.txt):

- **f. 160, to the King, 1 May** (canvas 307): *Car je veoy que ceste nation est autant vénale et sujette à se laisser
  gaigner par argent comme sont les Allemans leurs voisins.* Every word but "et" and "par" is sign-by-sign; the gloss
  has "autant", "gaigner", "comme son[t]", "[voi]sins".
- **f. 164, to Anjou, 1 May** (canvas 313): the opposing party *a despendu … ensemble … en ceste négotiation;
  l'Empereur en y a despendu plus de trois cens mil …, si faict … riens qu'il vaille …; seulement il le trouble …,
  faisant le pis qu'il peult contre vous.* Firm words: despendu (twice), ensemble, ceste négotiation, plus de trois
  cens mil, faict, riens qu'il vaille, seulement, trouble, desseing, faisant, le pis qu'il peult, contre vous. Four
  runs of 3–7 signs unread; the sign o- is the letter f in *faict* and *faisant* and the word-sign *l'Empereur* before
  *en y a despendu* (two signs conflated, or a variant).
- **f. 174, to the King, Płock, 9 May** (canvas 329), the letter announcing the election: *… qui est reüssy tant
  heureusement [contre la volunté et menées du Grand Seigneur, de l'Empereur, des princes de l'Empire, du Roy
  d'Espaigne, du Moscovite et du Roy de Suède, qui tous estoient bandez contre vostre Majesté].* Firm: contre la
  volunté et, seigneur, des princes, du Roy d'Espaigne, Moscovite, et du Roy de Suède, bandez, contre. From the gloss
  and sign count: Grand, de l'Empire, estoient, vostre. The gloss beside it has "la volunté et", "du Grand", "de
  l'Empereur", "de l'Empire", "de Spaigne", "et du", "Suède, qui tout", "bandez contr[e]", "Majesté", and it puts
  "l'Empereur" beside the o- sign, which is what fixes that word-sign.

New sign values from these leaves: 4 = b (*bandez*, *trouble*, Tomokiyo's value); three strokes = z (*bandez*) as well
as t (*oultre*) and s; the tailed 4 (Tomokiyo's Ꝝ) = p (*Empire*); Λ = ns (*riens*, *cens*); the C with hook = qu
(*qu'il*, twice); the 6-like sign = o (*trouble*, *volunté*); Δ = g (*seigneur*, *gaigner*, *négotiation*, *desseing*);
the plain cross with curl = t in *négotiation* and h in *empesché* (two forms not separated); the o with cross below =
et (*volunté et*, *et du Roy*), which makes f. 124's *retenu ou empesché* rather *retenu et empesché*.

Controls for this session: none beyond the glosses. The joint annealer over all six leaves (1,140 tokens, pins as
before) keeps every pinned value and agrees across three seeds on the frequent free signs (Γ = e, ✱ = e, ꟿ = i,
2 = l) but not on the rare ones (4, the 6-like sign, ⊓, o-, ff-with-bar differ or come out as vowels), so those rest
on the words above. Not done in session 2 (done in session 3, section 9): ff. 156v–157 (rest of the letter to Catherine), f. 154 in full, the 9 May letters to
Anjou, Catherine, Brulart and Lanssac père (ff. 182 ff.). Still not done (outside this target's letters): Monluc's cipher, which is another system. Tomokiyo's
"f. 331" is not a Lanssac item in the BnF notice (f. 330 is Crosne, 1587; f. 334 Brulart, 1586).

## 9. Session 3 (2 Oct 2026): ff. 154, 156-157 and the 9 May letters

Per-letter status (tokens read as sense / cipher tokens, `python measure.py ct_<folio>.txt`, measure.log):

| letter | file | read | status |
|---|---|---|---|
| f. 154r, to Anjou, 24 Apr | ct_f154.txt, read_f154.md | 439 / 454 = 96.7 % | read in part (15 tokens, gutter) |
| f. 154v, same letter | ct_f154v.txt, read_f154.md | 206 / 224 = 92.0 % | read in part (18 tokens, gutter) |
| f. 156r, to Catherine, 24 Apr | ct_f156.txt, read_f156.md | 307 / 316 = 97.2 % | read in part (9 tokens, gutter) |
| f. 156v, same letter | ct_f156v.txt, read_f156.md | 569 / 645 = 88.2 % | read in part (pass 2, full scale) |
| f. 157r, same letter | — | clear | no cipher |
| ff. 182, 184, 186, 188 (9 May, to Anjou, Catherine, Brulart, Lanssac père) | read_f182.md | — | **no cipher, no gloss**: all four are in clear |

All four cipher pages together: 1,521 of 1,639 tokens (92.8 %). Pass 1 of f. 156v (reduced scale, 346 / 515 = 67.2 %)
is kept as ct_f156v_pass1.txt; pass 2 re-read every line at full scale, found 130 more signs (whole lines had been
merged or skipped), and drops the 9 signs the writer struck through (marked ~).

The session-1 tokens of ff. 154/156 (tokens.txt) were redone from the full-size scans (img/c294, c297, c300, c301,
deskewed with strips.py) with word groups aligned to the plaintext, so that each group can be scored read or unread.
Content: Lanssac tells Anjou the Lithuanian lords have promised him their vote, which with his party in the kingdom makes
the crown sure unless the Sultan's recommendation, made "avec ruse" through the voivode of Wallachia, brings a change;
he has not fifty écus left and has borrowed 1,500; and expects all of them soon to be Anjou's subjects. He tells
Catherine that by Monday next she will be "mere des deux plus grans roys du monde", advises sending someone to the King
of Denmark (not to ask passage, but to tell him what the Imperialists are doing), fears the Emperor and Denmark at the
Sound, rules out the Italian road as too long and costly, and asks for money and galleys so the Polish embassy that
brings the crown is not kept waiting.

Key changes (key.tsv, session-3 rows): Gf = *me / nous* (a pronoun sign: "qui me donne", "qui me trouble", "m'ont",
"que nous avons", "Dieu nous esperons", "ne nous donnast"); Ng = *qu* (qui, quelque, quinze); Nb = *il* ("laquelle il a
faicte", "il me semble", "ilz seront", "il n'y en a"); obul = *bien*; Pi2 = *x/y* (ceulx, imperiaulx, celuy); Co (6-like)
= *o*; vo = *l'Empereur* (second form of o-); 4 = *b* confirmed (eleven words); 5 = *n*; Mx (footed n-shape), sq = *x*
(deux, chefz, ceulx); Mu (plain n-shape) = *u / qu* (vers, vous, que; Tomokiyo's *u*); 6 = *qu*; Ne (barred N with a
loop) = *est* (d'estroit); Gq = *qu* (embarquement); qq = *par* (par terre); Bf (second B form) = *f* (mon frere);
sm8 = *m* (recommandation, ameine). Pass 2 also shows the hand writes "mectre", "ameine", "neaumoins", "nommé".

Recheck of *despuis* (f. 124, first word): re-read on img/c242.jpg. The third sign is a barred N with a loop above, not
the plain barred N that reads *il* on ff. 154-156. Read *il* the word gives *de-s-il-u-i-s*, no French; read *p* it gives
*despuis*, which fits the gloss end "…es dangier" (… les dangiers). *despuis* stands. The barred-N signs are at least
three graphic forms (Nb *il*, Ne *est*, the f. 124 form *p*) that the transcription does not yet separate reliably; f. 160's
*autant* (N = a) is a fourth occurrence and should be rechecked on its image.

The ff. 182 ff. letters were expected (section 8, catalogue) to be in the same key with a marginal decipherment. The
images (canvases 341-353) show four letters entirely in clear, with addresses on 183v, 185v, 187v, 189v.

Controls: control3.py scores the raw first-value decode of each new letter (no hand choices) under
`fr-1600-letters` without spaces: −2.25 (f. 154r), −2.38 (154v), −1.93 (156r), −2.60 (156v, pass 2; −3.00 in pass 1)
per char, against −4.4 to −4.7 for three shufflings of the same tokens. The hand readings score −1.50 to −1.61 per char with spaces, in the range of real French.

## Remaining gaps

118 tokens on the four pages are unread. All of them have an outside blocker; none is a key gap the text could still
close (each was retried with the extended key in pass 2, below).

- f. 154r ll. 1-2 (6 tokens: the group after "desquelz", gloss line cut to "…que nous") - blocker: illegible; the inner-margin decipherment is lost in the microfilm gutter and the six signs give no word under the key.
- f. 154r l. 15 (5 tokens before "ameine") and l. 18 (4 tokens after "l'aide") - blocker: illegible; gutter-cut gloss ("…nament", "…qui nous") does not reach them, and no value set from the key gives a word.
- f. 154v ll. 1-2, 5, 7 (18 tokens: "escus" half-lost at the line end, one sign after "longtemps", three groups after "vaincre") - blocker: illegible; signs lost in the gutter and the outer gloss too faint on the scan at l. 7.
- f. 156r (9 tokens: opening group with a struck sign, one sign before "inopinée", "ff G" at a line end, one sign after "quelqu'ung") - blocker: too-short; single signs at gutter-cut line ends, no gloss left for them.
- f. 156v (76 tokens in 24 groups: the "cependant" group, "le" before "roy", "de large", the 8-sign "estoit ennemy" group, the opening of the Car-j'estime sentence, "ensemble afin", "a Monseigneur", the words after "ung roy … nommé", "de ceste nation", "quatre", and a few single signs) - blocker: illegible; most sit at the line ends against the gutter or under the decipherer's overwriting, and the gloss paraphrases there (e.g. "ne nous surprenne" for cipher "n'y soit prevenu") so it does not fix the signs.

## Escalation

- [x] siblings - every Lanssac letter of 24 Apr-9 May 1573 in fr. 4735 opened (ff. 124, 154, 156-157, 160, 164, 174, 182, 184, 186, 188); the four 9 May letters ff. 182-189 are in clear, no key material.
- [x] clear-pages - f. 157r (postscript) and the clear leaves ff. 126-127, 182-189 checked; the verso glosses of ff. 154v and 156v are the decipherment and were used as cribs.
- [x] known-keys - key.tsv of sessions 1-2 applied unchanged first; Tomokiyo's table compared (his M = u confirmed as Mu).
- [x] print - Noailles 1867 vol. III searched in session 1 (prints neither 24 April letter nor the 9 May ones); Tomokiyo's cryptiana page gives no reading.
- [x] key-rebuild - key extended from context and the glosses (Gf, Ng, Nb, Ne, Mu, Mx, Gq, Bf, obul, Pi2, vo, qq; see section 9); LM control (control3.py) against shuffles.
- [x] retry - pass 2 (2 Oct 2026): f. 156v re-transcribed at full scale and every unread group of ff. 154r, 154v, 156r, 156v retried with the extended key; f. 154r rose from 92.5 % to 96.7 % (nous ×2, qui, qui est, ameine), f. 156v from 67.2 % to 88.2 %; f. 154v and 156r unchanged; f. 124 *despuis* rechecked (stands).

## 7. Files

fetch_range.py (Gallica IIIF fetch with back-off) · strips.py (deskew a block, cut one strip per line) ·
tokens.txt (741 tokens: f. 124, f. 154, f. 154v l. 1, f. 156) · f124_tokens.txt · solve.py (annealer) ·
lattice.py (candidate-set beam decode) · controls.py, controls.log · key.tsv · reading.txt ·
session 3: ct_f154.txt, ct_f154v.txt, ct_f156.txt, ct_f156v.txt (word-aligned transcriptions; ct_f156v_pass1.txt = first pass) and their token-only copies f154_tokens3.txt etc. · measure.py, measure.log ·
control3.py · dec.py · read_f154.md, read_f156.md, read_f182.md ·
Tomokiyo’s table at cryptiana.web.fc2.com/code/henryiii_Lansac.png (not copied here). Page images and crops (img/, 177 MB) are not committed;
docs/lanssac_f124.jpg is the cipher block of f. 124.
