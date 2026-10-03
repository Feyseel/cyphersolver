# Court informant to Nevers, Paris, 29 April 1588 — BnF fr. 3976 fol. 62 (DECODE R3705)

Catalogue entry "Unknown sender to Louis Gonzaga, duke of Nevers", DECODE R3705 ("1588-01-01", Non-decrypted,
1 p., graphic signs). Session of 22 September 2026.

Status: read. All 19 cipher runs of the letter read (350 of 353 plaintext letters, measured from `reading.tsv`);
two items tentative (the name in R01, one word in R18). **f. 131 (4 June 1588) read in full 2 Oct 2026**: 130/130
signs read by the key, all 8 runs matching the interlinear decipherment of the time (`f131/reading.md`).

## The document

* BnF fr. 3976 = Gallica `btv1b9060548h` (399 canvases, microfilm). **f. 62 = canvas 111** (pencil foliation
  checked on the leaf; f. 60 = c. 108, f. 72 = c. 124). IIIF `full/full` gives 4895 × 6440 px. Crops in `img/`
  (git-ignored).
* DECODE's date 1588-01-01 is a placeholder. The letter is dated at the foot "Ce 29e Avril" [1588], docket
  "29 avril 1588". The BnF notice (cc504266, cached `research/gallica_sweep/notice_cc504266_cd0e37708.html`) lists it as
  piece 30: *"Lettre, avec chiffre, adressée au duc de Nevers, contenant entre autres nouvelles, celle de la levée
  du siège de Sedan et de Jametz. Ce 29 avril 1588."* (The notice's "Fol. N" precedes the piece number; piece 29
  at f. 60 is the cardinal de Guise's cipher of 26 April.)
* One page: clear French in a court hand, with **19 cipher runs** set into the text, plus bare **code numbers**
  (9, 10, 11, 12, 20, 24, 28, 49, 70, 102) and one overlined 40 with m (= 40 000). Signed with a cipher
  monogram (the same "ꟿ"-like mark closes ff. 131 and 133). No decipherment on the leaf.
* The writer explains his method in the last lines: *"Il y a quelques motz au chiffre cy dessus que j'eusse plus
  aisement et briefvement mis par nombres, mais craignant que ne feussiez memoratif d'iceulx n'ayant ce chiffre,
  j'ay mieulx aymé estre plus long."* So the runs spell out names and words that the code numbers could have
  carried.

## Prior art

DECODE: Non-decrypted, no transcription. Not in Tomokiyo's Nevers page (no mention of fr. 3976). No print found
in this session (Gomberville's *Mémoires de Nevers* not searched for this letter). Nothing read before.

## The key: siblings in the same volume

* Tomokiyo's Nevers keys in fr. 3995 tried against R01 (`4kd3si4ti3`) and rejected: no. 16 (f. 32v), no. 11
  (f. 23v, the cardinal de Guise's key), no. 10 (f. 21v), no. 18 (f. 36v, Roman-numeral codes), the alphabet on
  canvas 45. The code numbers of this letter also do not fit the f. 18 name list.
* Two ciphertext-only anneals (`solve.py`, `solve2.py`/`solve3.py`: n-gram French, letter / null-i / i-as-space
  variants, unigram penalty) collapsed to e/n/t strings. Too little text for a transcription this noisy.
* **The same informant wrote ff. 131 (4 June 1588) and 133 (6 June 1588)** of the volume, same hand, same
  cipher, same monogram. **f. 131 (canvas 221) carries interlinear decipherments** of its runs: "quelques mutins
  d'entr'eux", "conte de Brissac", "que s'il perissoit" (first read here as "pouvoit"; corrected 2 Oct), "Roy", and the code numbers 24 = Nevers (gloss "nevers"; first misread as Navarre), 11 = le Roy.
  Aligning "7 i7 id i2 t 6 s 8 g p i3 f 2 X" = "c o n t e d e b r i s s a c" showed the unit: **a sign is one
  character, or "1" (a dotted i-like figure) plus a character.** The first gloss confirmed m=19, u=d, t=12, i=p,
  n=l, s=f.
* The rest came from reading f. 62 itself, one run at a time, with the partial key: Villeroy (`11pnot1417y`,
  after "larmes de 12 et"), Bellièvre, "du royaume", "n ce royaume" (9=a), "leur entreprise" (J=p), "a failly"
  (4=f), "resolu au conseil" (k=o, x=c, 11=u), "chancellier et d'O" (v=d), "ligueurs", "belles et fortes villes".

Key as recovered (`key.md`): homophonic with some polyphonic signs, e.g. δ (a curly figure 8) = b/u/v, 9 = a/h/r,
2 = a/h, 3 = g/j, f = s/f. Glyph traps: the hand's 2 looks like z, its 8 like a curly d, its 9 like g; the dotted
"1" was first read as i.

## Reading

The runs in their clear context (`reading.tsv`):

> J'ay communiqué a 28 la lettre de [monogram]. Suivant laquelle je diz qu'il ne faudra pas, si **Fougères(?)**
> est encore icy, de luy representer les pertinentes raisons contenues en icelles, par lesquelles se congnoist
> assez que les advertissements de 24 ne peuvent avoir esté cause de **leur ruyne** comme ilz disent, ny de quoy
> **leur entreprise a failly**. Aussi la pluspart de ceulx qui en ont parlé n'entendoyent pas que celle de 24
> feust semblable a l'autre, ny que ce que 24 feust venu eust esté a l'appetit de 9, ains seulement **a la ruyne
> de 10, assistée** de plusieurs **gens de bien et d'autorité** qui y estoyent fort disposez **et s'i disposent**
> encore tous les jours. Mais 28 et 70 estiment bien que 24 a assez de jugement pour n'embrasser **telle
> entreprise** que bien a propos. J'ay sceu que led. 28 a prié 70 d'advertir icelluy 24. [...] Il cuyda estre
> **resolu au conseil de prendre et jetter en l'eau cinq ou six des plus grans ligueurs de** 102, a quoy
> poussoyent fort a la Royne, **chancellier et d'O**. Et 11 n'en fut desmeu sinon par les remonstrances et
> grosses larmes de 12 et **Villeroy**, qui saigement remonstrerent que tout aussi tost que cela seroit executé,
> non seulement l'on perdroit entierement 102, mais encore 20 **des plus belles et fortes villes du royaume**. De
> cela 9 fut incontinent adverty, qui appela **Bellièvre** pour le luy dire, jurant et reniant que si **le moindre
> de la ville l'avoit mal**, il feroit aud. 49 pareil traitement, et qu'il le mandast hardiment a 11, et que si
> telle affaire s'entreprenoit et executoit, luy **avoit a son commandement 40 mil hommes**, avec lesquels il
> **remueroit tant de messages(?) en ce royaume** que led. 11 en auroit **la plus petite part**. Voila tout ce
> que j'ay peu scavoir de nouveau.

Code numbers, from f. 131's glosses and this context: 9 = the duc de Guise (glossed "guis[e]" on f. 131, 2 Oct), 11 = le Roy (glossed), 24 = the duc de Nevers (glossed "nevers" on f. 131; first misread as Navarre, corrected from ff. 133-134, see `targets/r3708/`),
102 = Paris (context), 9 = Guise also fits here (threatens the King's council, commands 40 000 men),
12 = probably the Queen Mother; 10, 20, 28, 49, 70 not identified (20 is a count, "20 des plus belles villes").

This is the Paris news of late April 1588, a fortnight before the Day of the Barricades: Henri III tempted to
have five or six League leaders of Paris drowned, talked out of it by Villeroy and (probably) Catherine, and
Guise's threat in reply.

## f. 131: the letter of 4 June 1588 (read 2 Oct 2026)

Folder `f131/`: `transcription.md` (whole page), `ciphertext.txt`, `reading.tsv`, `decode.py`, `reading.md`. One
page (canvas 222 = f. 132, blank). 8 runs, 130 signs; `decode.py` aligns each reading with the key of ff. 62/133/139
and finds no sign outside its candidates once three values are added. Every run and every code number (9 Guise,
10 Espernon, 11 le Roy, 24 Nevers, 72 Savoie, 73 ambassadeur) carries a gloss of the time, and all agree. Content:
the Hôtel de Ville assembly of 3 June moving to an apology to the King; rumours that Brissac was killed and Elbeuf
held the fort Sainte-Catherine at Rouen; Meulan invested by Biron and Aumont; Corbeil surrounded by Guise; Épernon
at Loches, saying "que s'il perissoit il vouloit que tout le Royaume perist avec luy"; postscript: Savoy arming to
take the marquisate of Saluzzo (done October 1588). Measured: 130/130 signs, 33/33 words as French, LM -1.56/char.

Key changes from f. 131 (`key.md`): a bare 1 = i; the old two-character signs "1n" and "1e" are bare 1 + n (l) and
1 + e (t), which also fits f. 62 "failly", "avoit", "remueroit" without changing those readings; b-like sign = y
(once, "Roy", glossed); h and 1s carry "qu"; codes 9, 72, 73 glossed.

## Remaining gaps

- R01 name: letters read (f-o-u-g/j-e-r-e-s), the person not identified. Blocker: none from outside;
  identification is a history question, not a cipher gap.
- R18 one word "mes?a?es": read as "messages" if the unique sign 1r = g. Blocker: too-short (the sign occurs once).
- f. 131: no cipher gap (130/130 signs, 8/8 code numbers glossed). The b-like sign = y rests on one occurrence
  (glossed). Blocker: too-short.
- Code numbers 28, 49, 70 (and 12 by context only): open-codes (10 = Épernon, glossed on f. 139, see `targets/r3708/`); the informant's number list is not in
  fr. 3995 as far as checked; f. 131 glosses 9, 10, 11, 24, 72, 73, f. 139 adds 10, 38, 98, 107, none of these.

## Escalation

- siblings: done — f. 131 transcribed and read in full 2 Oct 2026 (`f131/`), its code glosses add 9, 72, 73; ff. 131 and 133 (same hand, same key) give the key; f. 131's glosses are the crib. f. 139
  (9 June, "chiffrée avec déchiffrement") was checked in the r3708 work: its glosses give codes 10 (Épernon), 38, 98 and 107.
- clear pages: done — the letter's own clear text supplies the context for every run.
- known keys: done — Tomokiyo nos. 10, 11, 16, 18 and the c. 45 alphabet tried and rejected.
- print: not done — Gomberville's *Mémoires de Nevers* (1665) may print this letter; not searched.
- key rebuild: done — `key.md`.
- retry: done — second zoomed pass corrected z→2, curly d→8, g→9 misreadings. f. 131 at native resolution
  corrected the segmentation (bare 1 = i) and the G04 gloss ("perissoit", not "pouvoit").
