# AGS Estado leg. 1394 no. 249: García de Toledo to Philip II, Messina, 16 July 1565 (duplicado)

PARES record 3576586 (dbCode 27138937), four images, fetched 2 Oct 2026 into `img/249_p1.jpg` … `249_p4.jpg`:
image 1 is the letter (one page), image 2 the blank verso (show-through only), image 3 a blank leaf, image 4 the
address leaf (*A la S. C. R. M. del Rey nuestro señor* · *En manos del señor Fran.co de Erasso*, sealed). Docketed
*Dupp.do* at top left. Written the same day as no. 247 and sent with it: the courier was already on board when
the Grand Master's latest letters reached Messina.

Read with the no. 247 key (figures 12–43 in alphabetical order, `key.json`) unchanged, plus two signs that occur
only here: a barred θ for *ll* (twice) and an M-like sign with an overline for *r* (once). The decoder is
`python decode.py transcription_249.txt`.

## Measurement

| | |
|---|---|
| cipher tokens | 150 (147 two-digit figures + 2 θ + 1 M-like sign) |
| runs | 25 runs, 32 words |
| tokens read as sense | **150 / 150 = 100 %**: every run divides into Spanish words or place names, no `?`, no odd run |
| language model | `es-golden-age`, word-divided decrypt **−1.67** per char (real text −1.1 to −1.8; the same letters shuffled −5.89); `lm.best_language` puts Spanish first |
| doubtful readings | one: the last group of *entrado* is written `17·0`, a small mark between 7 and 0; read 17 30 (*-do*). Read any other way the run turns odd. |

Script: the measurement was run from a scratch copy of the key and the word division below; the assertion that the
word division reproduces the decrypt letter for letter passed.

## Transcription

Figures digit for digit; clear text as written. The figures in `transcription_249.txt`.

```
Estando embarcado el Correo con este despacho he rescebido essas cartas
del Maestre las quales embio a V. M. para que pueda ver muy parti-
cularmente todo lo que scriue que es harto mas apretado de lo que yo pense
Sauiendole 18 29 37 35 12 17 30 20 27 36 30 16 30 35 35 30 , este que ha traido
estas ultimas cartas dize que oyo salua de Artilleria de las galeras del
Armada y deuia de ser 27 12 θ 18 22 13 17 13 17 18 27 30 36 Nauios que
comparescieron a 16 12 15 30 15 30 29 30 . que cre cierto son los de 14 35 22 18 27
y si huuiera embido 27 12 36 22 13 27 18 35 12 36 con la 22 18 29 37 19 12 la
22 30 27 19 37 12 huuiera llegado 12 28 13 27 37 24 18 29 33 30 19 27 12 36
de tenido hasta agora sperando M̄ 18 36 33 38 19 36 37 12 del 28 13 18 36
37 35 18 , porque si me scriuiera que hauia 21 30 35 28 12 de 33 30 29 18 θ 18
mas 22 18 29 37 20 33 30 35 tierra no quedara por 21 12 27 37 12 dellas pero
el 33 24 17 18 mas 17 19 27 12 que yo 12 22 30 35 14 le 33 38 18 17 30 dar y
ansi 33 12 35 37 24 35 12 29 las Galeras 28 12 29 12 29 14 / N. S.or
Guarde la Vida de V. M. por tan largos años como sus criados desseamos
y la Christiandad ha menester. de Micina a 16. de Jullio. 1565.
     [autograph] criado y vasallo de V. M. que sus reales pies y manos besa
                 don Garcia de Toledo
```

## Decipherment in context

Deciphered words in italics; editorial word division and punctuation.

> S. C. R. M.
>
> Estando embarcado el correo con este despacho, he rescebido essas cartas del Maestre, las quales embío a V. M.
> para que pueda ver muy particularmente todo lo que scrive, que es harto más apretado de lo que yo pensé,
> sabiéndole *entrado el socorro*. Este que ha traído estas últimas cartas dize que oyó salva de artillería de las
> galeras del Armada, y devía de ser *la llegada de los* navíos que comparescieron a *Cabo Bono*, que creo cierto
> son los de *Argel*. Y si huviera embiado *las galeras con la gente a la Goleta*, huviera llegado *a mal tiempo*.
> *(H)elas* detenido hasta agora esperando *respuesta del Maestre*, porque si me scriviera que havía *forma de ponelle
> más gente por* tierra, no quedara por *falta* dellas; pero él *pide más de la* que yo *agora le puedo* dar, y ansí
> *partirán* las galeras *mañana*. N. S. guarde la vida de V. M. por tan largos años como sus criados desseamos y la
> Christiandad ha menester. De Micina, a 16 de julio 1565.
>
> Criado y vassallo de V. M. que sus reales pies y manos besa, don García de Toledo.

Spelling as written in the figures: *tienpo* (n before p), *mañana* with a single n (28 12 29 12 29 14), *elas* for
*helas* ("I have kept them", h dropped). In `transcription_249.txt` the M-like sign is keyed as `μ` and the barred
theta as `θ`, so that `decode.py` can tell the sign from the clear *M.* of *V. M.*

## English summary

As the courier was already embarked with this despatch, García de Toledo received fresh letters from the Grand
Master, La Valette, and forwards them so that the king can see in detail how much worse the situation is than he
had thought, even knowing that the relief force (the *Piccolo Soccorso*) had got in. The bearer reports hearing an
artillery salute from the galleys of the Turkish fleet, which must have marked the arrival of the ships sighted off
Cape Bon, which Toledo is sure are the Algiers squadron. Had he sent the galleys with the troops to La Goletta they
would have arrived at a bad moment. He has held them back until now waiting for the Grand Master's answer: if La
Valette had written that there was a way to put more men into Malta overland, the galleys would not have been the
obstacle; but he asks for more men than Toledo can give him now, so the galleys will leave tomorrow.

The ciphered words are exactly the military content: the relief having entered, the Algerian arrival off Cape Bon,
the galleys and troops for La Goletta, the wait for La Valette's reply, the reinforcement question, and the
departure date. This is the same news as no. 247 (Cabo Bono, the Algiers squadron sighted by the wine ship bound for
La Goleta) in a short covering letter.

## Open groups

None unread. Points of doubt, each with what blocks settling it:

- `17·0` in *entrado*: read 17 30. The mark between 7 and 0 is a reduced 3 or a blot; only a higher-resolution image
  than PARES serves (~970×1390 px, zoom 10 is the maximum) would show which. The reading does not depend on it.
- The M-like sign with an overline (one occurrence, start of *respuesta*): read as *r*. It is not in the 12–43 table
  and occurs nowhere in no. 247, so a second example is needed to say whether it is a cipher sign for *r* or *re*
  (the latter would give *reespuesta*, so *r* is the better fit) or a clear capital R in this clerk's hand. Blocked
  on more material in the same key (Estado leg. 1395 siblings, not checked).
- The barred θ = *ll*: two occurrences, both certain from context (*la llegada*, *ponelle*); also absent from no. 247,
  which spells *ll* as 27 27. It is probably one of the extra signs of the full key sheet, which has not been found.
