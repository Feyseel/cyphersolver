# Instruction to the abbé (baron) de Mercy, Barneton, 6 June 1648 (BnF Espagnol 144 f. 22r-22v)

Session of 1 October 2026. Target: the leaf BnF Espagnol 144 (formerly Supplément français 1257C, tome III of the
"Espagnol 142-144" volumes) f. 22r-22v, Gallica `btv1b10035717h` canvases 58-59. The finding aid lists it as item 11,
"Autre instruction chiffrée pour l'abbé de Mercy. Barneton, 6 juin 1648. Copie." It is **not** a catalogue item or a DECODE
record. It came in as GitHub issue 16 from NoAutopilot (cipher-lab), who had broken it ciphertext-only; this session
verified their transcription against the images, corrected it in eight places, identified the name sign and a named
official from the clear instructions of the same volume, and wrote it up.

## Result in one paragraph

**Read, with a few open places (98.5% of 529 cipher tokens; key recovered ciphertext-only by NoAutopilot).** A homophonic
substitution of the numbers 2-34 (one to three numbers per letter, no word division) in runs inside clear Spanish, plus
one name sign (a square with a dot). It is the third instruction of 1648 that Archduke Leopold Wilhelm, governor of the
Spanish Netherlands, gave his chaplain Mercy for the intrigue with the duchesse de Chevreuse and the comte de Saint-Ibal
(the Fronde plot): the armies are in the field; Mercy is to get a categorical answer from the duchess and have Santibal come
with him; then go to Cleves, see the Elector of Brandenburg and his chief chamberlain Konrad von Burgsdorff, and ask whether
**3,000 infantry in two or three regiments** can be raised in the Elector's lands, on what conditions, and whether the
chamberlain will take charge of the levy. The substance matches the one print source, Lonchay et al., *Correspondance de la
Cour d'Espagne* IV no. 183 (as the contributor cites it). Our additions: all four "codes above 34" in the contributor's table
(48, 52, 65, 72) are pairs of single digits, and two glued 26 are 2 6; the name sign is Saint-Ibal; the unreadable-looking run
before "camarero mayor" is the chamberlain's name. Open: eight tokens in v04 (code 15 twice, "t non"), and the letters lost
where the right edge of f. 22v is trimmed.

## Prior work checked

* **NoAutopilot, cipher-lab** (https://github.com/noautopilot/cipher-lab/tree/main/ciphers/espagnol142-mercy-1648; issue 16):
  transcription, key, per-token grades, search log. They record "no prior decipherment and no print of the plaintext located
  after three logged searches (25-28 Sept 2026)", read 496 of 522 tokens at grade S and 26 at M. Copies of the files we used are in `cl/`.
* **BnF finding aid** (archivesetmanuscrits.bnf.fr/ark:/12148/cc347546, Espagnol 144): items 7-11. Item 8, "Memoire de ce qui est negocie ... au voyage de l'abbe de Mercy en Olande, entre luy, le comte St Ibal et Madame la duchesse de Chevreuse", 27 Sept 1647 (French, with Galarreta's Spanish notes of 27 Oct 1647), items 9-10, "Deux instructions ... Bruxelles, 8 fevrier et 13 avril 1648. Copies", item 11 = our leaf.
* **Print**: Lonchay, Cuvelier, Lefevre, *Correspondance de la Cour d'Espagne sur les affaires des Pays-Bas* IV (1933) no. 183, p. 71 (a calendar of Leopold Wilhelm's dispatch to Philip IV, June 1648; not seen here, cited by the contributor); Lonchay, *La rivalite de la France et de l'Espagne aux Pays-Bas* (1896) p. 445 n. 2 cites an instruction to Mercy of 15 April 1648 (Brussels S.E.E. t. LXIV f. 16) without printing it: the one of 13 April, our f. 21r. The text of f. 22 itself is in neither.
* **Konrad von Burgsdorff** (1595-1652): Oberkammerherr (chief chamberlain) of Elector Friedrich Wilhelm from 1642, the Elector's confidant (ADB; Wikipedia; 30jaehrigerkrieg.de).
* No key for this office is known (the contributor ruled out DECODE's Brussels "chiffres 1647-98", R958-R965).

## Access

Gallica IIIF: canvas = 2 x folio + 14 (f. 22r = canvas 58, f. 22v = 59, f. 20r = 54, f. 21r = 56). Full resolution 3454 x 5261.
Images are git-ignored (`img/`). The leaf is an unsigned copy; the right edge of f. 22v is trimmed (the clear lines are cut
too: "no con[venga]", "encargar p[ara]").

## The sibling instructions on ff. 20r and 21r (clear Spanish)

* **f. 20r, 8 Feb 1648, signed Leopoldo Guillermo and Juan de Galarreta**: "Instrucion de lo que vos el Abad de Merzi mi
  Sumillier de Cortina Sabeis de executar en el viaxe que de mi orden hazeis la buelta de Bruxas para avocaros (si pareciere)
  con el Duque de Longeville": Longueville has left Münster for France via L'Écluse and Bruges; "el Conde de S. Ibal" may come
  with him; Mercy is to see the duke, hear the negotiations, and bring a detailed account of what stands with the Prince de Condé, his brother-in-law.
* **f. 21r, 13 Apr 1648**: "... en la jornada que de mi orden hazeis a Kerpen para avocaros con la Duquessa de Cheurossa y el
  Conde de Sant Ibal": the duchess's intelligences in France, the governors of "Samalo" and "Persona" (Saint-Malo and Péronne?);
  "Despues de oydo a la Duquessa con Santibal, desearia si fuese possible que este viniese con Vos incognito, (si pareciere) para
  que me hiciese relacion de las noticias que hubieren traydo las personas que despacho a Francia ... en procurar que Santibal venga aqui y que la Duquessa ajuste con sus amigos la forma y medios con que piensan adherir a este partido."

So by 6 June the instruction in cipher is the third in the series, written from the field (Barneton) when the army was moving
(the archduke took the field in June). The clear instructions name Saint-Ibal in clear; the cipher uses a sign for him.

## The cipher

A homophonic substitution on the numbers 2-34: 33 distinct signs in 529 tokens, 20 letters (a e i o u have three numbers each,
q two, the others one), no letter for j k ñ v w x z (u stands for v), no word division, no nulls found, doubled letters
written twice; one name sign. Clear Spanish carries the opening, the connecting phrases and the close; the cipher carries the
names and the business. Index of coincidence 0.052. The key was rebuilt by NoAutopilot (anneal on Spanish n-grams, then the
words); the values are `key.tsv` (grades I; the name sign C).

## Transcription: checked against the images (1 Oct 2026)

Both leaves were read line by line from full-resolution Gallica images (crops at native resolution for every doubtful glyph) and
compared with `cl/ciphertext.tsv`. All cipher tokens agree except:

| where | contributor | image | reason |
|---|---|---|---|
| r24 | 65 | 6 5 | digits touching: s r in "t**r**e**s r**egimientos" |
| r17 | 52 | 5 2 | r o: "came**r o**", with "camarero mayor" |
| r17, r20 | 48 | 4 8 | q u: "para **qu**ien se os embian", "**qu**e si se permitira" |
| r16 | 72 | 7 2 | t o: "burgs**to**rf" |
| r18, r24 | 26 | 2 6 | o s: "se **os** embian", "regimient**os** y" |
| v01 | 19 | 14 | an open 14, c: "y al **c**amarero" (the contributor had five of these already: r06, r14, r16 x2, r17) |

The key has values 2-34 only, so a token above 34 can only be two digits written together. The four "M" codes of the contributor's
table (48, 52, 65, 72) are not codes. The same argument says the writer sometimes closes up 2 and 6 (or 4 and 8) without a gap;
26 stays a letter (i) where it reads ("propondreis", "pais", "permitira", "que si se"). Two more places are read by sense, both graded M: in
r10 the tight 25 is read 2 5 (o r: "informe", it gives "infume" as 25 = u), and a 2 and an 8 that stand apart are read as one
28 (l: "della y", it gives "oulay"). The count is 529 tokens (522 + 7 splits). `ct_f22.tsv` has them with notes; `edits.tsv`
the two sense edits.

**The trimmed edge.** Every line of f. 22v is cut at the right, by about four or five digits. Where the loss falls inside a word the sense restores it
(`lost_edge.tsv`): v01 camare[ro], v02 encarga[r s]e, v03 su [ma]no, v07 pag[an]dola, v08 leua[nt]ar, v11 cons[ig]uiese, v12 tener [tan]ta
gente. At v05/v06 and v06/v07 ("conuenient[e ?] ar otra", "tanta gente de [?] que") the loss is not recoverable, and v04
ends in a half-cut 15. These 18 restored letters (and the unrestored ones) are not counted as read.

## Names and the unknown codes

* **The box.** A square with a dot, twice: "y del [box]" (r07) and "que el [box] uenga con uos para que nos informe della" (r09).
  A name sign, not a letter; the same sign twice. f. 21r asks for exactly this: "que este [Santibal] viniese con Vos incognito para que me
  hiciese relacion". It stands for **the Conde de Saint-Ibal** (grade C: adjacent plaintext). The Duke of Longueville, the subject of f. 20r,
  is not named in this instruction at all.
* **Camarero mayor** and the name before it. After "el Elector de Brandenburg y con" the cipher gives `copurad lon burgsto rf su cmarero mayor`
  (with 5 2 = r o): "co p u r a d l o n b u r g s t o r f su camarero mayor" is **Conrad von Burgstorf (Burgsdorff), his chief chamberlain**:
  "burgstorf" is exact apart from d written t, "rad" and "on" are exact, the part before is two letters off (copu for con, l for v), and
  the writer drops an a in "cmarero". Burgsdorff was Oberkammerherr (= camarero mayor) from 1642 and the Elector's confidant; "para quien
  se os embian cartas de creencia" is the letters of credence for the Elector and him. The same title comes back at v01-v02: "y al camare[ro] mayor si querra encargarse della". Grade I.
* **Cheureuse** (the clerk's spelling of Chevreuse, as on f. 21r), **Cleues** (Cleves), **Brandenburg** are spelled out.

## The reading (`reading.txt`, `reading.tsv`)

The cipher runs are in lower case, [..] marks lost letters. Spanish as the clerk wrote it:

> Baron de Mercy mi Sumiller de Cortina deseo tener Resolucion de la negociacion que fuisteis por lo que conviene saver lo que se puede
> esperar della Respeto de las operaciones que se deven saver: 24. **(h)alandose estas armas en campagna** y asi Holgare me digais lo que en
> esta razon saueis entendido **de la duquesa de Cheureuse y del [Santibal]**, y porque qualquiera ora de tardanca en la coyuntura presente
> es de summo perjuicio procuraveis sacar Respuesta Cathegorica en la materia. Y **que el [Santibal] uenga con uos para que nos informe della y
> sepamos** Con fundamento lo que nos podemos prometer y Caso de no estar en estado y que es necesario esperar algun tiempo para poder dezir
> determinadamente el que tiene esta negociacion y lo que se puede confiar della, **pasareis a Cleues a veros con el elector de Brandenburg y con
> Conrad von Burgstorf su camarero mayor para quien se os embian cartas de creencia que uan con esta y les propondreis que si se permitira se
> leuanten en aquel pais tres mil hombres de infanteria en dos o tres regimientos y con que condiciones y al camarero mayor si querra encargarse della
> y que corra por su mano** no la dire?t non y si i u? a sera mas conuenient[e ...]ar otra tanta gente de [...] que a leuantada pag[an]dola y en su
> lugar leua[nt]ar otra. Y Caso que le paresca que esta materia no convenga Corra por su mano le preguntareis a que persona se podria encargar
> para que se pudiese caminar en ello sin perder tiempo, **y se cons[ig]uiese el fruto de tener [tan]ta gente**. En todo os encargo la brevedad porque
> qualquiera dilacion que aya es summamente danosa y de nuestro zelo fio aten[deis] a ello con el Cuydado que Conviene vos encargo. Barneton a seis Junio de 1648.

English: *Baron de Mercy, my chaplain: I want a decision on the negotiation you went on, because it matters to know what can be
expected of it in respect of the operations ... The armies being in the field, I shall be glad if you tell me what you have heard on this matter of the Duchess of Chevreuse and of Saint-Ibal; and because any hour's delay at the present juncture is highly damaging,
get a categorical answer on the subject, and that Saint-Ibal come with you so that he may inform us about it and we may know with a firm basis what we can promise ourselves, and if [it is] not in a state and one must wait some time to be able to say what this negotiation holds and what
can be trusted of it, go to Cleves to see the Elector of Brandenburg and Konrad von Burgsdorff his chief chamberlain, for whom letters of credence go with this; and put to them whether it
would be allowed to raise in that country three thousand foot in two or three regiments, and on what conditions; and the chief chamberlain, whether he will take charge of it and have it run through his hands ...
[and if it is more convenient to ... as many people again as the ones he has raised, paying them, and raise others in their place]. And in case it seems to him that this matter does not suit, to have it run through his hands, you will ask him to whom it could be entrusted, so that one can go ahead without losing time, and the fruit of having so many people be got. In everything I charge you with haste, because any delay is extremely harmful, and I trust to your zeal that you will see to it with the care it needs. Barneton, 6 June 1648.*

(The second half of the cipher is the least secure: v04-v08 reads in pieces.)

## Counts (`build_reading.py`, 1 Oct 2026)

529 cipher tokens: grade I 498, M 27, C 2 (the two box signs), no value 2 (code 15). 8 tokens are open (v04: 9-13, 17-19), so
**521 of 529 (98.5%) read as sense**; 27 of them are graded M (a glyph read by sense or a re-segmented token). 18 lost letters restored by sense, not counted.
Contributor's own count: 496 of 522 at S, 26 at M.

## Remaining gaps

- v04 pos. 9-13 and 17-19, "no la dire?t non y si i u?": code 15 occurs twice and has no value, "t non" does not read, and an extra i stands before "una" - blocker: open-codes; the word-frequency search over one digit re-segmentation, one substituted or deleted token and 15 = any letter finds "no la direct- ... y si una sera mas conveniente" at best (15 = c, one 32 read as 31, the extra i dropped), which moves two glyphs and is not accepted
- v05/v06 "conuenient[e ?]ar otra tanta gente" and v06/v07 "gente de [?] que a leuantada": two to three letters lost at the trimmed edge at each - blocker: illegible; the right edge of the leaf is cut, no other copy of this instruction is known
- the letters lost at the edge elsewhere (v01, v02, v03, v07, v08, v11, v12), restored by sense and not counted as read - blocker: illegible; same trimmed edge

## Escalation

- [x] siblings: the two clear instructions on ff. 20r and 21r (items 9-10) read from the images: they give the cast, the clerk's spellings and the sentence that identifies the name sign; items 7-8 (f. 17-19, French memoir of 1647) seen on the contact sheet, not transcribed
- [x] clear-pages: ff. 20r and 21r are clear Spanish of the same series; no clear or deciphered copy of f. 22 itself exists in the volume
- [x] known-keys: no key for the Brussels Secretaria in 1648 is known (the contributor checked DECODE R958-R965, mixed alphabets and nomenclators of more than 20 entries); none of the Fronde-period French keys applies to Spanish
- [x] print: Lonchay 1896 p. 445 n. 2 (instruction of 15 April cited, not printed), Lonchay-Cuvelier-Lefevre IV no. 183 (calendar only, per the contributor); web searches for the passage found nothing
- [x] key-rebuild: the contributor's anneal; here the digit-pair splits, the name sign and the camarero mayor from the siblings and the sense; the v04 values searched with a Spanish word model and not found
- [x] retry: every run re-decoded after the corrections; r10, r16-r20, r24, v01 now read; v04 and the junctions v05-v07 remain

## Files

* `ct_f22.tsv` (token level, with notes) and `ct_f22.txt` (cipher tokens only, one line per manuscript line) — the verified transcription.
* `key.tsv` — the key (33 signs); `edits.tsv`, `lost_edge.tsv`, `open_stretches.tsv` — the interpretive edits, the trimmed-edge restorations, the open tokens.
* `decode.py` (plain decode) and `build_reading.py` (reading and counts) -> `reading.txt`, `reading.tsv`.
* `cl/` — the contributor's `ciphertext.tsv`, `key.tsv`, `exceptions.tsv`, `corrections.tsv`, `reading.txt` as fetched on 1 Oct 2026 (their repository has the rest).
* Images in `img/` (git-ignored): f. 22r-v (canvases 58-59), ff. 20r-v, 21r-v (54-57).
