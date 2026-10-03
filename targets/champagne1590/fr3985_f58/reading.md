# BnF fr. 3985 f. 58: La Verrière to Nevers, Poissy, 12 August 1593

Session of 2 October 2026. This is the letter Tomokiyo (cryptiana `code/nevers.htm`, entry for key no. 57) names as using
Laurière's/La Verrière's key: "a letter from Laveriere to the Duke of Nevers, Poissy, 12 August 1593 (BnF fr.3985
fol.58)". No other target reads it; `targets/nevers1593` works other items of the same volume.

## Access

Gallica `btv1b90606498` (fr. 3985, microfilm, 485 canvases, all labelled NP). **f. 58r = canvas 114** (pencil "58" top
right, docket "12 d'aoust 1593"), f. 58v = canvas 115 (address only: "A Monseigneur / Monseigneur le duc de
Nivernois"). Canvas 112 is f. 56 (Revol? 12 Aug, Gerzy), 116 is f. 59. Full size 4719 × 6676, fetched through IIIF
`full/full/0/native.jpg` with no throttling (two requests). The key sheet f. 103r (fr. 3995, `btv1b525085665` canvas
200) was fetched again at full size to read the whole word list (`words57.tsv`; key57.txt only had the words of
nos. 10 and 55). Images (full canvases c114_full.jpg, c115_full.jpg, the deskewed c114_deskew.jpg, key_c200.jpg, all crops) are in `../img/fr3985_f58/`, git-ignored.

## The leaf

One page in La Verrière's hand, signed "Laverriere", "A Poissy ce xij aoust 1593". Clear French with **two cipher
passages**: run A, nine lines in the middle (page lines 11–19, 223 cipher tokens, 207 read), and run B, short pieces in
lines 21–24 (25 tokens, 15 read). **The office's interlinear decipherment is
written over almost every cipher line**, in a lighter ink and a different hand, so the letter was read at the time.
The cipher is key no. 57 exactly as in nos. 10 and 55: two signs per letter, syllables row + 14 × vowel, words
99–353, overbarred places and v/z syllables, name signs.

Files: `ct.txt` (transcription of every run in the sign names of `../check_3625_10.py`, with the gloss as G lines),
`clear.txt` (the clear text), `words57.tsv` (key word list 99–353 and the province/town table, read off f. 103r),
`decode58.py` (applies the key, prints key value / reading per run, counts, runs the LM check).

## Result

**Run A reads; run B in part.** 222 of 248 cipher tokens (89.5%) are read as sense with key no. 57 as it stands on
the sheet, plus four slips of the writer that the context and the office gloss correct. Measured with `decode58.py`
(token counts exclude Laverrière's own clear words inside the runs). French LM (`fr-1600-letters`) on the run A
reading: −1.72 per character, best language French (`lm.best_language`: fr-1600-letters −1.72, fr-modern −2.00,
Latin −2.60). This is below the 95% read bar, so the target class stays *read in part*.

### Run A (after "… ce qui l'empesche c'est")

> pour le fait du [prince de Conty], qui desire de ritirer, mais il ne sait a qui le confier, estant la personne qui
> luy est de plus d'importance. Madame d'Angoulesme est a[…] du tout a la maison de [Messieurs de Montmorency], et le
> principal appuy qu'il ait, soit des catholiques, soit de ceux de la religion, soit de ceste maison, *qui
> s'acorderoit fort bien pour cela*, s'il y avoit quelque remuement. Vola pourquoy il desire faire election d'ung
> fidelle serviteur et tabour le [lieu?], ou il le pourra mettre, *et point*, l'oter, instruire, gagner monsieur de la
> Trimouille, pour ne donner aucung soubs son[…] a ceux de la religion, *estans tous* de nature defians.

(*italics* = Laverrière's own clear words inside the run.) The office's gloss agrees word for word except where noted
below; Tomokiyo's note on the entry (a Japanese comment in the page source) names the phrase **17 9 70 26 17 32 ω q n s
= "de nature defians"** as the one that let him identify the key, with **304 = pour** at the start: both are here, in
the last group of run A (`17 9 70 26 17 32 om venus pi`) and the first group (`304`).

### Run B (lines 21–24)

* B1 `om ? ? PAPE` — "a [?] [Pape]"; gloss "aux bas[…] du Pape" (ambassadeurs?). Two signs not decided.
* B2 `6 lam 344` — key "la a tout", no sense; gloss "la plus[…]".
* B3 `252_ PAPE 304 om 14 venus 28 ddag om beta lam` — "[?] [Pape] pour atanter a la"; 252 with an overbar is not on
  the sheet as read (plain 252 = lettre).
* B4 `28 25 203 NAME` (303 written and struck before 203) — key "te que fait [?]"; the gloss over it reads
  "po[ur] mo[…] du d[uc] de Lor[raine]", so the last sign is probably the duke of Lorraine's name sign; not read.
* B5 `300 17 NAME` — "personne de [Cardinal de Bourbon]" (gloss "La personne du Cardinal de Bourbon"; the name sign is
  taken from the gloss).

So: "… qu'il y a [?] du Pape pour attenter a la personne du Cardinal de Bourbon, et disent avoir les lettres, et je ne
croys qu'il amenera."

### Key changes and slips

* Word list completed: `words57.tsv` has every word 99–353, the overbarred 200–203 and the province/town numbers, read
  off f. 103r. New values used here: 160 desire, 183 estre, 200̄ plus, 243 importance, 245 instruire/instruction,
  300 personne, 309 quoy, 327 serviteur, 340 tabour (T column, as the office also read it), 344 tout, 159 donnee.
* **183 = estre** stands where the sense and the gloss need *estant* ("183 n t"): the writer used 183 as *est-* and
  spelled out the ending. Grade I.
* Name signs not on the f. 103r panel as checked: an R crossed with an X (gloss: *prince de Conty*), a looped
  o‡o-like sign (gloss: *Messieurs de Montmorency*), the sign in B5 (gloss: *Cardinal de Bourbon*), the sign at the end
  of B4 (probably *duc de Lorraine*). Grade C (from the gloss; the names panel f. 103v not re-checked for these).
* Writer's slips, each forced by context and agreeing with the gloss: `8 2 22` ma-*ca*-me for *madame* (3 = da);
  `caret 44 venus 30` p-*co*-n-ci for *princi-* (40 = ri); `334 tri` son-t for *soit* (335); `22 17 eps 20` *me*-delle
  for *fidelle* (32 = fi); `57` without its bar for *vo* in *vola*; `29_ sigma yi plus` a-*ve*-o-i-t for *avoit*.
* The scroll sign transcribed as xi (b) stands for *b* in *soub[s]* and for *u* in *ou* (run A, "ou il le pourra"):
  the writer's Vs (u) and xi (b) are not separable on this page.

### Where key and office differ

* A8 `lam 16 perp inf` is *a ceux* on the key; the office wrote *a cause*. Both give sense ("pour ne donner aucung
  [ombrage?] soubs son[…] a ceux / a cause de la religion"); the figures are *ceux*.
* A6 `Ep 20 sigma mu 42 f venus`: key "e-le-o-c-ti-o-n", office *election*; the sigma (o) is probably a second c.
* A7 the office's *gagner* over `5 varpi 23 plus` (ga-g-ne-t).

## Open (26 tokens)

* A2 two signs inside *s..t* (the word *sait* is read, the two signs are not decided on the image).
* A3 `lam ? plus plus` after *est*: the gloss starts "a m…" (*amie*?); the signs do not give it.
* A4 the sign between *pa* and *l* (principal), and the three middle signs of *c…e* (*ceste*).
* A6 `340 20 34 ye plus`: key "tabour le liet", gloss "tabour le lieu"; no sense established.
* A7 one sign in *monsieur*; A8 the sign after *l* in *de la*.
* B1 two signs, B2 all three, B3 the overbarred 252, B4 all four.

Blockers: the A-run gaps are single signs too damaged or too cursive to decide at the microfilm's resolution
(illegible); the B-run gaps are values not on the key sheet as read (overbarred 252, the B4 name sign) or groups whose
key values give no sense (open-codes). The original is not digitised in colour; a better image of f. 58 (BnF reading
room or a colour scan) is the step that could close the illegible ones.

## Context

Poissy, 12 Aug 1593, the fortnight after Henri IV's abjuration (25 July) and during the truce talks; the conference
was moving between Mantes and Andrésy. La Verrière reports to Nevers (who was preparing his embassy to Rome) on the
young prince de Conty, who wants to *retirer* someone but has no one to entrust it to; Madame d'Angoulême
(Diane de France) is wholly with the Montmorency house, his chief support among both Catholics and Protestants; hence
he wants to choose a faithful servant and to win over M. de La Trémoille, the Huguenot leader. Run B reports something
[letters?] of the Pope for an attempt on the person of the Cardinal de Bourbon (Charles de Bourbon-Vendôme). The clear
text deals with Revol, Fresne, Sancy, and the rest of a payment of 1000 écus.
