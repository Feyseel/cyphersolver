# BnF fr. 3976 f. 131r: the Paris informant, 4 June 1588

Gallica `btv1b9060548h` canvas 221 (f. 131r; canvas 222 is f. 132, blank, so the letter is one page). Not a DECODE
record. Same hand, cipher and monogram as f. 62 (R3705, this folder), ff. 133-134 (R3708) and f. 139
(`targets/r3708/`). Transcribed and read 2 Oct 2026.

Files: `transcription.md` (whole clear text with run markers), `ciphertext.txt` (8 runs G01-G08), `reading.tsv`
(reading, context, the contemporary gloss), `decode.py` (sign-by-sign check against the key, blind decode, LM score).
Images in `../img/` (git-ignored): `c221.jpg` full page, crops `z*`, `y*`, `p*`, `L*`.

## Measurement

`python targets/nevers1588/f131/decode.py`:

* 130 cipher signs in 8 runs (plus 1 sign struck by the writer and 1 code number inside a run): **130/130 read by
  the key**, every one consistent with the key of ff. 62/133/139 plus three single values new here (bare 1 = i,
  b-like sign = y, h carrying "qu"). No sign is read from context alone.
* Every run agrees with its interlinear decipherment of the time (8/8).
* Words of the runs: 33/33 read as French sense; 30/33 occur in the `fr-henri4` corpus vocabulary (Caterine,
  perissoit, perist do not; all three are glossed by the decipherer). `fr-1600-letters` LM: -1.56 per character
  over the runs as read (real text -1.1 to -1.8, gibberish about -6).
* Code numbers: 9, 10, 11 (twice), 24 (twice), 72 (inside G06), 73, all glossed above the line: **8/8 identified**.
* Read share of tokens: 100% (130 signs + 8 code tokens).

The blind decode (first key candidate for every sign, no reading used) already gives "quelques mbtipf dentreeblx",
"conte de bgisfac", "que sil perisfoit", "marquifat de salbce": the polyphonic d/δ (u or b), f (s or f) and g (r or g)
are what the reading resolves.

## The runs

| run | signs | reading | gloss of the time |
|---|---|---|---|
| G01 | 1s t n h s 13 19 d 12 p J f 6 t 1d 12 14 t 5 d o c | quelques mutins d'entre eulx | quelques mutins d'entr... |
| G02 | 7 17 1d 12 t 6 5 8 g p 13 f 2 X | conte de Brissac | conte de Brissac |
| G03 | 9 5 13 E t 12 d s t E h s v s n y t d f s f 12 9 d 4 k g E f z p l 7 E t 7 9 12 5 14 1 J t | a esté tué et que d'Elbeuf est au fort Saincte Caterine | est tué et que de l'Beuf est au fort St Catherine |
| G04 | h s 13 1 n 16 t 14 p 13 f 17 1 E | que s'il perissoit | que s'il perissoit |
| G05 | (struck sign) J t 14 1 f E 9 d 5 7 o d Q | perist avec luy | perist avec luy |
| G06 | <72> 13 9 14 19 5 | Savoie s'arme | Savoie s'arme |
| G07 | 14 17 b | Roy | Roy |
| G08 | 19 9 14 h p f z E 6 5 13 9 o d 7 5 | marquisat de Saluce | marquisat de / Saluces |

The 22 Sept notes gave the G04 gloss as "que s'il pouvoit"; the cipher has 14 (r) and 13 f (ss): the gloss is "que
s'il perissoit", which the next run ("perist avec luy") confirms.

## The letter

> 4 de Juin 1588. Hier se fit une assemblée en l'hostel de ville des capitaines d'icelle ou **quelques mutins
> d'entre eulx** proposerent plusieurs choses assez mal a propos comme l'on dit. Mais apres, aultres desd. capitaines
> du corps de la court de parlement prirent la parolle et firent de tresbelles remonstrances contenant en somme
> l'obeissance et recongnoissance deue au Roy [...] et que puis qu'il n'y avoit plus de Huguenotz dans Paris il
> failloit demourer tous uniz en la religion et au debvoir envers son prince [...] l'on ne peult moings que de luy en
> faire des excuses et le supplier de pardonner l'offence [...] Il fut resolu qu'il se feroit aultre plus notable
> assemblée tant des corps et cours que des bourgeois pour en resouldre. [...] Et sembleroit que sur ces entrefaictes
> 24 [Nevers] seroit bien a propos pres de 11 [le Roy].
>
> Le secretaire de la poste m'a asseuré que le Roy a ceste nuict couché a Vernon pour de la aller a Rouen. Aulcuns
> ont voulu faire courir le bruit ce matin que le **conte de Brissac a esté tué et que d'Elbeuf est au fort Saincte
> Caterine**. Vous avez sceu que celuy qui commandoit dans le fort de Meullan [...] avoit mandé a 9 [Guise] luy en
> envoyer d'aultres [...] sa magesté [...] fit incontinant investir la place par messrs les mareschaulx de Biron et
> d'Aumont. [...] Corbeil est tout environné des troupes de Monsr de Guise [...] On tient pour certain que Mr
> d'Espernon n'est allé qu'a Loches pour recevoir les forces de Lavardin et aultres de Poictou pour retourner trouver
> le Roy. Et ay ouy dire a gens de creance qu'ilz scavoyent que 10 [Épernon] avoit dit a aulcuns de ses amis **que
> s'il perissoit** il vouloit que tout le Royaume **perist avec luy**. [...] Ce 4 Juing. [monogram]
>
> Je croy que si 24 [Nevers] va veoir 11 [le Roy] il sera bon qu'il soit adverty que 72 [Savoie] **s'arme**, et que
> l'on a tiré par conjectures de son 73 [ambassadeur] qu'il est conseillé de ce faire en intention de tenir **Roy** en
> alarme et neantmoings luy offrir son ayde et service, mais a la charge de faire ses besongnes et praticquer s'il
> peult **marquisat de Saluce**. Partant seroit bon tenir les places bien pourveues. [monogram]

Paris three weeks after the Barricades: the Hôtel de Ville assembly of the militia captains moving to an apology to
Henri III (then at Vernon on his way to Rouen); rumours about Brissac and the duc d'Elbeuf at the fort Sainte-Catherine
of Rouen; the Meulan fort, invested by Biron and Aumont; Guise's troops round Corbeil; Épernon gone to Loches. The
postscript warns Nevers that the duke of Savoy is arming, under cover of offering help to the King, to take the
marquisate of Saluzzo, which Charles-Emmanuel did in October 1588.

## Gaps

None in the cipher. Two clear-text words are uncertain readings of the hand ("contenante", "praticquer"); they do
not affect the runs.
