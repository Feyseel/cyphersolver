# States General, 1629: "diverse briefjes in cijferschrift" from the Spanish invasion of the Veluwe (NA 1.01.02 inv. 12579.26)

Status: blocked (offline only: the packet is not digitised. The Nationaal Archief scans an inventory number on request for
EUR 16.75, up to 250 scans. Placing that order needs an NA account and a payment, so it is Daniel's decision. Reopen when the scans
are in hand.)

Session of 28 September 2026. Catalogue entry 347. Goal set by Daniel: solve it.

## What the target is

- **Nationaal Archief, 1.01.02 (Staten-Generaal), inv. 12579.26**: "Correspondentie met de gedeputeerden van de
  Staten-Generaal te Arnhem naar aanleiding van Spaanse inval in de Veluwe", 1629, *1 pak*. The inventory note reads:
  "Bevat diverse briefjes in cijferschrift. Zou zijn overgebracht naar 'cassa lit. A no.27 locquette E', maar berust
  nog onder oud nummer": the packet was to be moved to the Secret Cash (loket E) but is still filed under its old number.
- Section VI.C.1.1.5.c of the inventory (Loketkas and Secrete kas, *Stukken betreffende militaire zaken*).
- Handle `hdl.handle.net/10648/d2944105-cffb-9283-e053-6df0900aec3e` (from the EAD). The handle resolver returned 404
  on 28 Sept 2026.
- Context: the Imperial-Spanish invasion of the Veluwe, 21 July to late August 1629, under Hendrik van den Bergh and
  Ernesto Montecuccoli, took Amersfoort (14 Aug). It was a diversion to break Frederik Hendrik's siege of
  's-Hertogenbosch. The States General sent deputies to Arnhem, and the "briefjes" (small notes) in cipher are most
  likely spy or agent reports, or intercepts, sent to them. Neither the writers nor the language is known.

## Access (all checked 28 Sept 2026)

- **NA inventory page** (`nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/12579.26`): the embedded record has
  `scan_id: ""`, and the detail pane has no *Bekijk scans* link. A digitised sibling in the same subseries,
  inv. 12579.122, has `scan_id NL-HaNA_1.01.02_12579.122_0001` and serves its `.jpg` files; 12579.26 serves none.
- **NA EAD download** (1.01.02, 22.7 MB): 10,857 `<dao>` scan links in the inventory, none on 12579.26. So the packet
  is not digitised; the missing link is not a gap in the viewer.
- **Other cipher items in 1.01.02, 1600-1660** (EAD grep for *cijfer/chiffre/ontcijfer/dechiffr*): only 12561.142
  (1658-59 Sound casualty lists "met vertalingen"), 12572.16 (1644-45 envoys in Denmark and Sweden, partly in cipher)
  and 12557.2 (an unrelated false hit). No unit in the inventory holds a copy or decipherment of the 1629 notes. Units
  on the Veluwe/Amersfoort in 1629: only 12579.26.
- **Resolutions**: Huygens ING, *Resolutiën der Staten-Generaal 1626-1630* (online edition). Full-text searches for
  *cijfer, cyffer, ciffer, chiffre, caracter, karakter, characters, ontcijfer, desciffr, dechiffr* found nothing about
  the notes; the only *cijfer* hit (29 Aug 1629) is an editor's remark on a date.
- **DECODE** (full record list): no record of inv. 12579.26 or of any 1629 Low Countries cipher. The only
  Staten-Generaal records before 1649 are Cornelis Haga's despatches from Constantinople, 1620 (inv. 6894, target
  `haga1620`, key R2118), a diplomatic system unrelated to a Veluwe field cipher. The other 1620-40 records are Hessian,
  Transylvanian and Swedish.
- **Gelders Archief** (Arnhem), where the deputies' own papers might have stayed: its site-wide search for
  *cijferschrift* returns nothing relevant.
- **Web**: no article, edition or reading of these notes.

## What would read it

1. Order the scans: log in to the NA site, open inv. 12579.26 and use *Scans aanvragen / digitaliseren op verzoek*
   (EUR 16.75 per inventory number, up to 250 scans, delivered online). A reading-room visit is the free alternative.
2. Count the notes and systems, and separate cipher notes from the deputies' clear covering letters. Those letters
   usually say who sent a note and roughly what it reports, which gives a crib.
3. Transcribe, and measure each note (`docs/_check_profile.py --measure`).
4. Expect short Dutch (or French/Spanish) field ciphers of the 1620s: a small nomenclator or monoalphabetic
   substitution with a few code names. Pool notes that share a system; attack with the `lang/` Dutch model (or French)
   and cribs from the covering letters and the resolutions of July-August 1629 (Amersfoort, Hattem, Wesel, Van den
   Bergh, Montecuccoli, Isabella, 's-Hertogenbosch).

## Remaining gaps
- NA 1.01.02 inv. 12579.26, every cipher note - blocker: needs-physical-access; not digitised (NA scan-on-request order or reading-room visit)

## Escalation
- [x] siblings: NA 1.01.02 EAD searched for every cipher and Veluwe 1629 unit; none holds a copy or decipherment
- [n/a] clear-pages: no images of the packet to check (its clear covering letters are in the same undigitised packet)
- [x] known-keys: DECODE list searched for Dutch/States General keys of the 1620s-30s; only Haga 1620 (R2118, Constantinople), not a field key
- [x] print: Huygens RSG 1626-1630 full text, web search; no edition prints or deciphers the notes
- [n/a] key-rebuild: no ciphertext in hand
- [n/a] retry: no ciphertext in hand
