# András Bay to Ferenc Rákóczi II, Jászvásár 8 March 1706 (DECODE R478)

Status: read

MNL OL G15 Caps. D. Fasc. 81. 5, 2 pp., DECODE R478 ("Non-decrypted", homophonic, numerical). Catalogue entry 38
("András Bay to Ferenc Rákóczi II"). Images are MNL OL copyright: fetched with the DECODE cookie into `img/`
(git-ignored), not published.

## Result

**Read.** The letter is enciphered in Rákóczi's syllabic key **DECODE R609** (G15 Caps. C. Fasc. 43. 56, a
Hungarian two-digit syllabary with a place/person nomenclator 149–293 and nulls 15–19, 200, 300, Ψ, +). DECODE never
linked the key to the letter. Found by decrypting R478 with each of the 94 G15 key transcriptions
(`score_keys.py`, Hungarian 4-gram score): R609 came first at once (R561, an earlier issue of the same table, second).
The key reads the letter unchanged. 414 cipher groups; 413 have a key value; one group (50, once) is
absent from R609 and reads *ba* from context (*barát*). Measured with `decode.py`: every group gives Hungarian in
context except about ten in the passage *tolmácsot ha az ha az tizéntee s. asséraltadé ö* (p. 2, l. 5–6), whose
letters are all read but whose sense is uncertain (2.4 %). Reading rate ≈ 97.6 % of groups.

Clear passages between the cipher runs are in plain Hungarian (DECODE's transcription of them is rough; the
dateline is *Jászvásár 8. Martii* [Iași, Moldavia], signed *Bay András*).

### Reading (normalised; cipher in plain type, clear passages in «»)

«Kegyelmes Uram! Valamint ez előtt negyed nappal küldött levelemben nyilván meg írtam,» Moszkva és lengyel
követek jöttek ide; az lengyel vissza is ment, a moszkva még itt vagyon. Az mint expiscálhattam, olyat
mondottak mind ketten: a moszkva békességre kéri a svédet, minden elvött várakat és ezen hadakozásban lött
expensáit a svédnek megígérvén, «[ha oly] conditióval, hogy a ki[rály]» ellene a moszkva hadát declarálja-é a svéd
«is, [ha nem]» colligatióban «légyen». Reményik(?), hogy szándékoznék; az moszkva követ «innét» Constantinápolyba
«vagy» Erdélybe megyen, én nem tudhatni; mért csak maga beszéllett az vajdával, görögül. «…» Tegnapi napon az vajda
tolmácsával conversatióban lévén, «… elő in discursu» Pekri uram általa olyat izent a vajdának, hogy csak
Nagyságod a magyar nemzet dolgát complanálhassa a némettel, … minden szándéka Nagyságodnak a török ellen való
hadakozás. «…» Az tolmácsot [? ha az … asseráltad-é ?] tudván az barát az Portának szemének és fülének lenni, még
nem mondotta; «nékem is» lelkemre kötötte, hogy ki ne adjam őtet. A svéd Vilnához szállott, mely Litvánia és
Moszkva-Oroszország között vagyon. «Továbbá is … Jászvásár 8. Martii … Bay András.»

English gist: As written four days ago, Muscovite and Polish envoys have come here [to the Moldavian court]; the
Pole has gone back, the Muscovite is still here. Both said the Tsar is asking the Swede for peace, promising him all
the fortresses he has taken and his war expenses, on condition that [Charles XII] declare against... [text uncertain];
whether the Muscovite envoy goes on to Constantinople or Transylvania I cannot tell; he talked with the voivode alone,
in Greek. Yesterday, in conversation with the voivode's interpreter: Pekri sent word to the voivode through him that
if only Your Highness can settle the Hungarian nation's affairs with the Germans [the Emperor] ..., Your Highness's
whole intention is war against the Turk. The interpreter,
knowing the friar to be the Porte's eyes and ears, has not told him; he made me swear not to give him away. The
Swede has moved to Vilna, between Lithuania and Muscovy.

## Transcription

`R478_transcription.txt` is DECODE's transcription (AJ, 2020) corrected against the images: *iv*→10 (*jöttek*),
0→clear *é*, 1257→127 (*tolmácsával*), *l, i, 86, i*→6, 1, 86, 5, 74 inserted (*fülének*), 63 restored (*lelkemre*),
the two crossed-out signs after 300, 16 marked struck, "neptune" = Ψ (null). `R478_read.txt` is the decrypt.

## Remaining gaps

- One ten-group stretch on p. 2 (*…tolmácsot ha az ha az tizéntee s. asséraltadé ö…*): every group has its key
  value; the sense is unresolved (possibly a slip by the encipherer). Not blocked; no better reading found.
- Group 50 is not on R609; *ba* from context (*barát*), single occurrence.
- Clear passages transcribed only as far as needed; a clean reading of them would need a Hungarian palaeographer.

## Escalation

- Siblings: all 94 G15 key records (R549–R646) tried; only R609/R561 fit.
- Known key: R609 unchanged; R561 variant checked (worse fit on nomenclator).
- Print: web search (Hungarian) for Bay's 1706 Moldavian despatches found no edition or decipherment.
- Key rebuild: not needed; 59 read as *ho* (R609 lists 59 both for U and *ho*).
- Retry: all images re-read line by line against DECODE's transcription.

## Corrections

- **30 Sept 2026 (reported while quotations were pulled for Lasry's list).** The normalised Hungarian above and on
  the page had drifted from `R478_read.txt` in five places. Each was checked group by group against the R609 values
  (`keys/DOC_R609_D2784_2784.txt`, as `decode.py` applies them) and on the images (main checkout
  `bay1706/img/IMG_R478_I3620_P1.png`, `IMG_R478_I3621_P2.png`):
  p. 1 l. 2 `146 25 7 9 85 94 81 86 70` vi-sz-a-i-s-mé-n-t-a = "vissza is ment, a" (was "viszaismét [elment?]": the
  81 = n rules out "ismét"); p. 1 l. 4-5 `95 81 73 63 86 125 81 7 231 156 115 63 116 70 270 8 86` = "mind kétten a
  [Mosqua] [Bekessey]-ré-ké-ri a [Svéed]-e-t", with no 13 (hogy): "a moszkva békességre kéri a svédet" (was "hogy a
  moszkva békességet kéri a svédtől"); p. 1 l. 5-6 `95 81 41 81 80 78 4 1 86 86 286 7 62 86` = "minden elvött
  várakat", all the fortresses taken, i.e. the Tsar offers the Swede back every fortress he took (was "mindenekelőtt
  várakat", above all fortresses); p. 1 last line to p. 2 l. 1 `105 77 116 282 / 70 78 124 67` = "Pekri uram általa", through him (the
  interpreter) (was "által"); p. 2 l. 3-4 `95 81 41 81 25 70 81 41 62` = "minden szándéka", his whole intention (was
  "mindenben; szándéka"). The English gist and the page's English were corrected to match: the Pole "has gone back";
  the Tsar promises the Swede "all the fortresses he has taken"; Pekri sent word "through him" that if only Rákóczi can
  settle with the Emperor, "Your Highness's whole intention is war against the Turk". Not changed: "a némettel" before
  that clause stands for `238 8 6 1 86 5` [Nemet] e-o-ö-t-u, whose last five groups are unresolved (shown as "...").
  Changed: `docs/bay1706.html` (reading, English, a dated line under What remains uncertain), this file, `profile.json`.
