# f. 154r-v — Lanssac to the duc d'Anjou, Warsaw, 24 April 1573 (BnF fr. 4735 no. 60)

Gallica btv1b9060724s canvases 294 (f. 154r), 297 (f. 154v). Session 3, 2 Oct 2026. Transcription: ct_f154.txt (recto),
ct_f154v.txt (verso). Measured with `python measure.py ct_f154.txt` (measure.log).

**Status: read in part.** Recto 439 of 454 cipher tokens read as sense (96.7 %, after the pass-2 retry); verso 206 of
224 (92.0 %); together 645 of 678 (95.1 %). Key: key.tsv (session 1 key plus the session 3 rows). Control (control3.py): the raw first-value
decode scores -2.25 / -2.38 per char under `fr-1600-letters` (no spaces) against -4.4 to -4.7 for the same tokens shuffled.

Check against the contemporary decipherment: the recto gloss is in the inner margin and the gutter leaves only line
ends; every surviving fragment agrees with the reading ("…causé l'autre", "…[me tr]ouble beaucoup", "…est que j'ay",
"…[ch]efz desquelz nous", "…prendre que donner", "…doubte ou vous", "…sur la teste", "…recommandé", "…grand seigneur",
"…[q]u'il a faicte", "…l'estime", "…par le Vaynode de"). The verso gloss is in the outer margin and survives whole; it
reads the first cipher block word for word as below.

## Reading (cipher in italics; {…} unread)

Clear: *… Depuis la conclusion desquelz* — cipher:

> {*et su-e i nt*} j'ay aprins deux choses, l'une qui me donne gaing de cause, l'autre qui me trouble beaucoup. La
> premiere est que j'ay esté au devant des Lituans, les chefz desquelz m'ont promis ne donner leur voeu à aultre que à
> vous, [clear: *qui sera de telle importance que*] avec la bonne part que nous avons au royaume sans doubte ou[1] vous
> mettre ceste grant couronne sur la teste, si la recommandation du Grant Seigneur, laquelle il a faicte de vous comme
> j'estime avec ruse par le vaivode qui(?) de la Valaquie, qui est(?) {5 signs} ameine quelque inespéré changement, qui est
> le second poinct qui me donne une traverse, de laquelle avec l'aide {4 signs} de Dieu nous esperons neaumoins sortir.

[1] *ou* = *on* (the script-z sign 5, here as in *donne*). Sense: the Lithuanian lords have promised their vote to Anjou,
which with the party he has in the kingdom would make the crown certain — unless the Sultan's recommendation of Anjou,
made (Lanssac thinks) with guile through the voivode of Wallachia, brings some unexpected change; that is the second
point, a setback from which, with God's help, they hope to come out.

f. 154v, first block (clear before: *… ne pourroit faire sans l'argent*):

> Car je n'ay pas cinquante {es-}c{-us} [gloss "escuz"], combien que j'en ay emprunté plus de quinze cens. [clear:
> *Aussi estois je party*] bien belistre pour venir si loing et demeurer si longtemps {1 sign} et faire contrecarre à
> celuy qui [par] beaucoup de grans dons ne sçauront vaincre {8 signs} {3 signs} [i]nferieur? {2 signs}

Gloss: "Car je n'ay pas cinquante escuz et y ay emprunté plus de xvᶜ. Aussy estoit le party bien belistre pour venir si
loing demeurer si longtemps et faire contrecarre a celuy qui par beaucoup de grandz dons ne sçauroyt vaincre …".

Second block (clear before: *… plus de trois cens escus la piece*):

> Et espere que dans peu de jours tous ceulx-là avec beaucoup d'autres seront vos subjectz.

Gloss: "Je espere que dans peu de jours tous ceulx la avec beaucoup d'aultres seront voz [subjectz]".

## Unread groups and why

| place | signs | state |
|---|---|---|
| r l. 1-2 | de4 g ff X i sm | opening words after "desquelz"; gloss line cut to "…que nous" |
| r l. 15 | qq sh i X s | before "ameine"; gloss end "…nament" does not reach it |
| r l. 18 | de4 ff mm sm | after "l'aide"; no word under the key |
| v l. 1-2 | x2, x3 | "escus" across the gutter, signs half-lost on the microfilm |
| v l. 5 | x4 | one sign after "longtemps" (gutter) |
| v l. 7 | 3 G Y s c 8 F ast; Lo i F; Y de4 | after "vaincre"; the gloss line here is too faint on the scan to read past "les" |

Pass 2 retry (2 Oct 2026, extended key, full-scale check): Gf = *nous* before *avons* and before *esperons*; B ff i =
*qui* after *vaivode* (the sign after it is struck); Mu i G X st = *qui est*; T sm8 G q9 nn ast = *ameine*; the half-lost
first sign of l. 19 is the *e* of *Dieu*. f. 154v unchanged.

All gaps are on the microfilm gutter or in the faint lines of the recto gloss; nothing in the volume gives another
copy (see NOTES, Remaining gaps).
