# Ormanetto / Clementino, Spain nunciature 1576-77 (ASV Segr. Stato Spagna 10; DECODE R117, R118). R118 READ (key from outside)

Catalogue no. 239 (DECODE refill, rule-scored class A, "noted"). Worked 21 Sept 2026.

Outcome (1 Oct 2026): **R118 read, R117 not a cipher.** R118 reads with the Spain nunciature's "cifra ordinaria" (key by Ajaydas Devadas, email of
1 Oct 2026; described in `../ormanetto1573/NOTES.md`, which it also reads). The 21 Sept result (attempted and closed) is the history below.

## R118 as read

Italian: *scrita ali 15 di otobre. Il nuntio a comunicato col secretario Perez tutto quello che V.S. Ill.ma scrive con la cifra di 19 di setembre; il quale segretario
a promeso di darne conto al Re, et di procurarne risposta, de la quale V.S. Ill.ma sara poi subito avisata* + six null signs (s t c z p l). "Written 15 October. The Nuncio
has communicated to Secretary Perez everything Your Lordship writes in the cipher of 19 September; the Secretary has promised to report it to the King and to procure
an answer, of which Your Lordship will shortly be advised." The clear Italian note on the leaf is the contemporary decifrato of this text, **minus the dateline**. Our 21 Sept
readings of the note ("trattato", "Sig.r", "buoni uffici", "sabbato") were abbreviations misread, which is why the crib test failed.

- `dec118.py`: AJ's token list for the six lines, decoded with the key and compared with his plaintext (12 lines consistent, 0 differ). **Compared with the scan here: lines 1-3 and 5**
  (`decode/L0.jpg`, `l1a/b`, `l3a`, `l5a`, git-ignored); lines 4 and 6 not compared by eye. The dateline "15" (overlined) and "19" are on the page. `--reveal` writes `docs/reveal/ormanetto1576.json`.
- Our `r118_cipher.txt` cannot carry the key: it has no dots, and writes the cross-stroke as 4 or X ("24" = 2+, "44" = 4+).
- Year open: Ormanetto died 18 June 1577 and Sega reached Madrid on 11 October 1577, so 15 October is Ormanetto in 1576 or Sega four days after arriving in 1577. The third person suggests
  nunciature staff wrote it; DECODE's "Clementino" is unidentified.
- Contamination: the reading came from outside on 1 Oct 2026. The leaf's note is the contemporary decipherment, which we took on 21 Sept for a plain message.

## Remaining gaps

- the year of the letter and the writer "Clementino" - blocker: needs-physical-access; the register of Como's ciphers to Spain or the Spagna 10 index would date it

## Escalation

- [x] siblings: R116 (ormanetto1573) reads with the same key
- [x] clear-pages: the note on the leaf is the decifrato, minus the dateline
- [x] known-keys: the cifra ordinaria key fits
- [x] print: Olarra-Larramendi not online
- [n/a] key-rebuild: key complete for the letters in R118
- [n/a] retry: nothing unread

## History: 21 Sept 2026 (before the key)

Outcome then: **attempted and closed.** R117 contains no cipher. R118 is a short numeric cipher with no key and no
decipherment; not read.

## What the two records are

**R117** (`ASV_i1025_SdS_Spain_10-1`, 2 images, ff. 245-246, stamped 247): a clear Spanish memorial, *Copia del
Memorial dado por parte del obispo de Pamplona*: an account of the fruits of the see of Pamplona during the vacancy
after Diego Ramírez (d. 27 Jan 1573) until Antonio Manrique's bulls (1575), and the claim that the nine months'
fruits held back by the Pope be paid to the bishop. The only "numerical" matter is sums of ducats in Roman numerals
with the Spanish thousands sign (e.g. `xbnUdn L-ix`, `xxxbjUdn - m`), repeated in the right-hand margin. There is
no cipher. DECODE's "Ciphers within cleartext" tag was triggered by the Roman-numeral sums.

**R118** (`ASV_i1025_SdS_Spain_10-2`, 1 image, f. 365, stamped 350): six lines of contiguous figures (389 digits
measured on `r118_cipher.txt`, plus the barred-4 sign `X` and dots over some digits), then in another hand and
ink a clear Italian note:

> Il Nuntio ha trattato col Sig.r Perez tutto quello che V.S. Ill.ma scrive con la cifra di 19 di sett.re, il qual
> Sig.r ha promesso di buoni uffici al Re, et di procurare risposta, de la quale V.S. Ill.ma sarà poi sabbato
> avvisata.

The letter is undated on the leaf. The note refers to a cipher from Rome of 19 September, and Perez is Antonio
Pérez, Philip II's secretary. The letter therefore dates from autumn 1576 or 1577. The DECODE record's range is
9 Jan 1576 to 2 Nov 1577; the catalogue's "9 Jan 1576" is only the start of that range.

## Is the note the decipherment? (DECODE: "possibly already deciphered on the same page")

The note is about the same length as the cipher (about 200 letters expanded; about 190 digit pairs), and it opens
the way the figures do: `20 70 53` recurs at the start of line 1 and the end of line 2. It was tested as a crib.
`crib_align.py` beam-searches a tokenisation of lines 1-2 into 1-3-symbol tokens aligned letter by letter with
the note, keeping the token→letter map functional and minimising distinct tokens:

- the note: 43 distinct tokens for 60 letters;
- three shuffles of the same letters (control): 47, 51, 48.

The gain is small and the best alignment is incoherent (tokens of mixed lengths, no stable pair structure). The
note does not fit as a crib. It reads as the nuncio's (or his secretary's) clear message in the third person,
added below the cipher, not a decifrato. Line 1 also breaks two structural keys: Lasry's key for the Como→Dandini
cipher of 1580 (DECODE R72; two-digit letter codes with an even second digit, 3 digits + mark for nomenclator
words) cannot apply, because this text has odd second digits throughout (53, 07, 03, 05).

## Keys and printed sources looked for

- DECODE: no key record for the Spain nunciature 1570-80. The only 1570-80 Spain records are R116 (Ormanetto 1573,
  non-decrypted, still in the catalogue as no. 259) and R5624 (Sega 1579, N/A).
- The Spain nunciature correspondence of these years is calendared by J. Olarra Garmendia and M. L. Larramendi,
  *Correspondencia entre la Nunciatura en España y la Santa Sede durante el reinado de Felipe II* (Rome, from
  1948; citation from memory, not checked here). Not found online. If this letter's decifrato survives in the registers, it
  is there. This is the lead for anyone continuing.

## Transcription

`r118_cipher.txt`: lines 1-2 read at 3x zoom, lines 3-6 at 2x and less secure. Dots over digits are not recorded.
The page images are git-ignored (`decode/`, DECODE login).

## What would move it

The Olarra-Larramendi volume (to date the letter and find its decifrato) or a Spain nunciature key of 1572-77.
Ciphertext-only: 389 digits in a homophonic two-digit system with marks is short for a blind attack.
