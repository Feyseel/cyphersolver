# Ferdinand of Bavaria, Elector of Cologne, to Duke Maximilian I of Bavaria, Bonn, 22 December 1619

BayHStA, Kurbayern Äußeres Archiv 4591, ff. 281–286 (DECODE R9426, "Non-decrypted", 10 pp., numerical).
Catalogue entry 165 ("… to unknown recipient, 1619"). Work 22 September 2026, one session (Claude Opus 5).

Outcome: **read** (95.8% of cipher tokens measured, `python count.py`). Key state: rebuilt, letters complete;
the nomenclator (32 groups, 74 tokens) is open apart from 248 = *und*.

Images: DECODE, login only; the rights line on the record reads "The image is not in the public domain.
Publishing it is only possible with the permission of the Archive." No permission has been asked for, so the
images stay in the untracked `targets/kaa4591/img/` work folder (git-ignored) and the site page carries no figures.
Only text files are in this folder.

## Who wrote it, and to whom

DECODE gives no sender, no recipient and no place. The letter names itself on the last page:

> … Geben in meiner Statt **Bonn** den 22.ᵗᵉⁿ **Decembris Anno 1619**.
> … williger … und dienst … **Ferdinand**

and the ciphered text speaks throughout of "mein Thumb[capitel]", "meine Landtstendt", "meinen Landtag
auszuschreiben", "meinem … Ertz[stift]" and of Paderborn. The writer is therefore **Ferdinand of Bavaria**
(1577–1650), Elector-Archbishop of Cologne and Prince-Bishop of Paderborn, Münster, Hildesheim and Liège.
The clear opening addresses "mein hertzliebster herr Schwager … E. L.", and the file is Kurbayern's own
archive: the recipient is his elder brother **Duke Maximilian I of Bavaria**. Six weeks after Frederick V's
coronation in Prague, and weeks before the League's Munich resolutions, the two brothers are arranging the
quartering and paying of the Catholic League's troops in the Rhine–Westphalian circle.

Neither letter is in the printed record. *Briefe und Akten zur Geschichte des Dreißigjährigen Krieges* NF I/1
(ed. Franz, Munich 1966, Jan 1618 – Dec 1620) cites the Munich files by the old "Kasten schwarz" numbers, not
KAA numbers, and nothing in its searchable text for November–December 1619 matches this letter (Zwettl, Bonn
22 Dec, the Horn/Erwitte/Paderborn matter). Hurter viii, Wolf/Breyer iv and Pastor were checked and do not
have it. "KAA 4591" is cited nowhere.

## The cipher

A homophonic substitution on **even two-digit numbers**, written with dots, with a three-digit nomenclator and
two separator signs that mark word ends (transcribed `z` and `c`; the same two signs recur at every word
boundary and carry no letter value).

| | |
|---|---|
| a b c d e f | 10 12 14 16 18 20 |
| g h i l m n o p q r s t u x z | 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 |
| second series | a 60, 70 · e 62, 72 · i 64 · o 66, 76 · u 68 · k 74 · w 78 |

So the vowels have two or three homophones each and the consonants one, except k and w which live only in the
upper series. 22–28 do not occur. Single cipher letters also stand alone as initials ("E. L." is written 18 . 36).
Full table in `key.txt`.

The codes are three-digit groups (102, 122, 136, 142, 146, 154, 160, 165, 183, 200, 213, 215, 216, 221, 225,
232, 238, 239, 248, 258, 410, 412, 414, 415, 416, 417, 419) and a few two-digit odd numbers (33, 47, 49, 51, 57),
which cannot be confused with the even letter values. Only **248 = und** is established, from its own contexts
("Gwalt 248 Betrangnus", "Eifer 248 Ernst", "248 in kurzer Zeit"). 414 (12 occurrences) is a person or a title
and 232 recurs after the ciphered word "ertz", so it is probably *stift*, but neither is proved and neither is
counted as read. (2 Oct 2026: R9425 shows 414, 415, 416, 417 and 419 to be nulls, and makes 232 = *stift*
nearly certain; see the R9425 section below. The R9426 figures here are not yet recounted.)

## How it was solved

1. The ten images were read line by line into `transcription.txt` (clear passages in brackets, cipher as written).
2. `solve.py` annealed a homophonic key over the letter runs against `lang`'s `de-1500s` model
   (5-gram, 16th-century German). Six restarts of the first three pages already produced German
   ("gelegenen", "Landtag ausschreiben", "Quartiermeister"); ten restarts over all ten pages fixed the table.
3. `decode.py` re-decodes with the fixed key and flags every word the model dislikes; `repair.py` proposes
   single-token corrections among the digit pairs this hand blurs (0/6, 3/5, 1/4, 2/7, 5/8), and
   `wordfix.py`/`apply_fixes.py` apply the accepted ones. About sixty corrections were made this way; they are
   corrections of the **transcription**, not of the key, and a sample of them (catolischen, einzuquartiern,
   wolermelt, Erwitte) was re-checked against the images at full zoom.
4. `count.py` measures the result.

**Control.** The key was applied, unchanged, to the sibling record **R9425** (ff. 278–280, also 1619, which
DECODE marks "Decrypted" and which carries a decipherment summarised in red in its left margin). Its first
cipher line reads `60 36 12 48 18 14 32 52 | 54 42 40 | 30 66 52 52 18 50 | 30 40 10 16 18 40` →
**"[A]lbrecht von Gottes Gnaden"** (Archduke Albert, sovereign of the Spanish Netherlands). No value was
adjusted to make this read: see `control_r9425.txt`.

## What the letter says

Ferdinand has had Maximilian's letter of the 10th. On the frontier of the **county of Horn** and at
**Montfort** companies are to be accommodated; "our lord's" forces are not to be lent there. The levies
(*Werbungen*) are not *sufficient*; the agent, **Licentiat Morres**, reports. Companies are to be quartered in
the villages nearest the city and at **Deutz**, opposite Cologne, under a particular ordinance for the
quartermaster; the march (*Fortzug*) is to follow when the troops are ready. Pay is fixed at **two Kopfstück
or two Ort of a Königsthaler daily**. Ferdinand will not alienate his own Estates: he must keep his
**Domkapitel** and **Landstände** in good will and devotion, and is about to call a **Landtag**; he asks that
his territory not be overburdened. **Lintelo's** company is accommodated near the city; **Herberstorff** and
other recruitments are to have every possible support ("daran nichts erwinden lassen"). For **Paderborn** a
year's respite is asked, where troops are already levied and a contribution and a mustering-place granted.

The second half is the argument. If the other side is *reprimirt* and the adversary strengthened with so
considerable a reinforcement while Catholic power is diminished, then "den Catolischen ins gemein … in kurzer
Zeit" nothing will be left to secure them against "Einfal, Gwalt und Betrangnus". Against it he sets the common
union: "Ich vermeine, das die gemeine Zusammensetzung zu Conservation unser und in kurzer Zeit unser catolischer
Religion und Seelen Seligkeit … bei der Posteritet" (the conservation of us and soon of the Catholic religion and
the salvation of souls, for posterity); his agent's relation shows that a resolution is needed, and levies are to be feared "für dem
Frühling". A closing passage names **Alexandro**, the King, and "die Austilgung der ca[t]olischen Religion".

## R9425 (ff. 278–280), the sibling, read 2 October 2026

Status: **read** with the key unchanged (97.3% of 1567 enciphered tokens measured, `r9425/count_r9425.py`). It is
**Archduke Albert's written resolution for Licentiate Morreus**, the League agent, dated 15 December 1619 (clear line
f. 280r; endorsement f. 280v "Resolutio deß hertzogs Albrechts dem L. Morreo … ertailt"): Albert agrees on the
recovery of the kingdom [of Bohemia], has done good offices with the Emperor and the King of Spain, will send his
troops on foot to join the Catholic army if needed, cannot grant the muster place, regiment of foot and 500 horse
(his levies are for Luxembourg), writes to Oñate about Breisach and refers the 1000 cuirassiers to Ambrogio Spinola.
Transcription, decrypt, summary and code table: `r9425/` (`transcription.txt`, `decoded.txt`, `reading.md`,
`codes.txt`). Clear passages are a working reading only.

**Feedback to R9426 (not yet applied to its files, count.py or the site page):**
- **414, 415, 416, 417, 419 are nulls.** R9425 forces it ("Kön. 414 M. und L." beside "Kön. 165 und L."; "unsers 414
  hochlöblichen"; "zu gedachtem 419 End"; "iren L. 414 L." / "ire L. 415 L."). In R9426 these are 23 of the 74 open
  nomenclator tokens (414 12×, 416 4×, 419 5×, 415, 417); the contexts fit ("mit 414 dem Doctor", "ermeltem Erwite 414
  zu mir"). 410 and 412 (one each in R9426) are probably nulls of the same run but are not seen in R9425. Counting the
  five as read raises R9426 from 95.8% to 96.7% ((2504 + 23) / 2614).
- With 416 a null, R9426's "ertz 232 416" and "zu meinem 416 232" make **232 = stift** close to forced.
- **242 = und** (homophone of 248), **165 = Mt.**, **2 = Ambrosio [Spinola]** (red margin "Ambr."). 165 occurs once in
  R9426 ("gegen 414 160 als 165 in"). Probable values that also occur in R9426: 216 = Pferd/Reiter ("seine 216",
  "obbesagter 216", "Boninckhausen 216"), 154 = Haus ("Conservation ires 154 und"), 47 = Mt.

## Corrections

- **30 Sept 2026 (while filling the gaps in the quotation for Lasry's list).** P8.15-P8.20 re-checked on the image
  (`kaa4591/img/IMG_R9426_I44572_P8.jpg`, rotated 180). The clear words before the cipher on P8.15 are "Ich
  vermeine, das die" (one descender, not the three of "hoffe"); "Ich hoffe" was a slip of the first transcription,
  corrected in `transcription.txt`, `reading.txt`, the reveal file and the page. The words the quotation cut between
  "Conservation unser" and "catolischer" are P8.17-18 `54 40 50 18 48 | 248 | [in kurzer zeit] | 54 40 50 18 48`
  = "unser und in kurzer Zeit unser" (the clear words are written "in kurtzer zeit" run together; 248 = und as
  established). The sentence reads without a cut: "Ich vermeine, das die gemeine Zusammensetzung zu Conservation
  unser und in kurzer Zeit unser catolischer Religion und Seelen Seligkeit darab bei der Posteritet bis dahin hier
  nötig erachtet werden" (*unser* is the genitive "of us"). No key value changed.

## Remaining gaps

Each gap carries its blocker. R9426:

- **open-codes** (no-key-material): 32 nomenclator groups, 74 tokens (2.8% of the text), chiefly 414 (12×), 232 (6×),
  122, 216, 419 (5× each), 221, 416 (4× each). No key for this cipher survives: KAA 4591's own key records were
  checked (below) and none is it. R9425 (2 Oct 2026) shows 414/415/416/417/419 to be nulls (23 tokens; see the R9425
  section), not yet applied to R9426's count; the rest stay open.
- **unidentified names** (left open): three words read as proper names whose bearers are not identified — "leicker"
  (Doctor Leicker, Ferdinand's negotiator), "dernersen" (with Herberstorff), "marreo"/"morres" (the agent).
- (illegible) Four words (37 tokens) still do not read: `tarceen` (P1.22), `situs` (P2.05), `unaerherschaffen` (P3.05),
  `gegainer` (P4.23). Each is a single-token misreading somewhere in a word; the digits are genuinely
  ambiguous at this resolution.

R9425:
- **open-codes** (no-key-material): 32 tokens, 2.0%: 45, 149, 225 (2× each), 160, 219, 153, 15, 215, 155, 221, 136,
  140, 249 and the probable-only values 41, 218, 154, 169, 47, 216, 31, 157. Single contexts; no key survives.
- **gutter loss** (needs-physical-access): two or three signs on f. 278v lines 30–31 run into the binding.
- **illegible** single signs: P1.18, P3.05, the gloss over 155 and the gloss over 221; five single-token slips in
  words whose sense is clear are counted unread.
- **clear text** (left open): the clear passages are transcribed as a working reading with gaps; they are not
  cipher and do not enter the measurement.

## Escalation

- [x] siblings: R9425 (ff. 278–280), the same cipher and correspondence — used as the control; its red margin
  was contrast- and channel-enhanced and is an abstract ("hochvermelts Herrn Schwagers …", "angelegen Sachen"),
  not a decipherment of the groups.
- [x] clear pages: pp. 9–11 of R9426 are clear text and were read; there is no key sheet with the letter.
- [x] known keys / the volume: KAA 4591 is the Bavarian chancery's key-book, and DECODE lists 102 key records
  from it (R9277–R9423). The numerical ones were looked at: R9419 (f. 267) is a Latin nomenclator on 1–99
  (Caesar, Rex Catholicus, Saxonia) — a different cipher; R9420–R9423 are 1530s–1583 alphabets already worked
  through in `../kaa4591/`. None is the 1619 cipher.
- [x] print: *Briefe und Akten* NF I/1, Hurter viii, Wolf/Breyer iv, Pastor, and a web/Google Books/archive.org
  sweep for "Äußeres Archiv 4591" — no edition and no decipherment of either letter.
- [x] R9425's four cipher pages transcribed and deciphered (2 Oct 2026, `r9425/`): read 97.3%; nulls 414–419,
  242 = und, 165 = Mt., 2 = Ambrosio fixed from its contexts and its margin.
- [x] retry of the open groups against both letters together: the nulls and 232 = stift follow; the remaining
  groups have one or two contexts each and stay open.
- [ ] not done: the Munich archive's own "Kasten schwarz" concordance, which would say where Franz's NF I/1 cites
  these folios (needs-physical-access or correspondence with BayHStA); a full-resolution re-read of R9425's clear
  passages.

## Files

| file | what it is |
|---|---|
| `transcription.txt` | the ten pages, line by line: cipher tokens, clear passages in brackets |
| `key.txt` | the recovered key |
| `solve.py` | the homophonic annealer (lang `de-1500s`) |
| `decode.py` | decode with the fixed key, flag words the model dislikes |
| `repair.py`, `apply_fixes.py`, `wordfix.py` | the transcription-correction pass |
| `count.py` | the measurement quoted above |
| `reading.txt` | the reading, line by line |
| `control_r9425.txt` | the sibling control |
| `r9425/` | R9425 transcription, decode (`decode_r9425.py`, `decoded.txt`), measure (`count_r9425.py`), `codes.txt`, `reading.md` |
| `solve_out1.txt`, `solve_out2.txt` | the two annealer runs, kept for the record |
