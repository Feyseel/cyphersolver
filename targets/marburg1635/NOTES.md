# Marburg 1635: cipher passage in a Thirty Years' War letter (DECODE R4500)

Status: read (≈97% of tokens; nine signs at the end of line 1 open)

- **Record.** DECODE R4500, Hessisches Staatsarchiv Marburg, HStAM 4 d Nr. 1218 no. 49 (arcinsys v1923393). One page,
  image `IMG_R4500_I26572_P.jpg` (git-ignored in `img/`). DECODE: "Partially decrypted", date span 1635–1652 (the
  volume's span, not the letter's date), sender/recipient not given.
- **What it is.** A German letter in clear text reporting troop movements (Rostock, companies marching, "Marche").
  From "noch nicht zu vernehmen," the rest (14 lines) is in cipher; the letter closes in clear with "... beygefügter
  Extract". A contemporary hand wrote a decipherment between cipher lines 1–4. That is why DECODE has it as partly
  decrypted. Lines 5–14 have no gloss.
- **Series.** R4452–R4577 are the same volume: about 120 key sheets (claves of Hesse-Kassel with officers and civil
  servants, 1635–52) and four ciphertexts (R4452–R4454, R4536 decrypted, R4546). None of the single-row alphabets checked
  (R4467, R4491, R4520, R4525) is this key. The key was rebuilt here from the text instead.

## Method

1. Token transcription `cipher_tokens.txt` (577 signs, word gaps kept).
2. Homophonic annealing against `lang` `de-1500s` (spaces, order 5). A free run gave near-German; seeding a few
   letters from "und"/"under" repeats (`9 0 1`, `6 1 2`) produced readable words: "entschuldigt", "damit ich",
   "underthenigst", "ermangelen möchte". These fixed the rest by hand.
3. The interlinear gloss is the control: "(zu)mahl nicht", "etwas tentiret werden", "dieses orths halber", "dagegen"
   come out of lines 3–5 with the rebuilt key unchanged, except that it fixes M = w and 8 = o.

## Key (signs → letters)

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 5, 8(o), A | a / o | 6 | e | 0 | n |
| 1 | d | 1 2 (joined, "iz") | r | 2 | s |
| 3 | g | 4 | h | 7 | i |
| 9 | u (also b once in "halber") | F (d-shaped) | s | W (w-sign) | t |
| T (theta) | c (`T4` = ch) | D (triangle) | l | q (4 with cross) | m |
| X (crossed t) | b | M (superscript w/m) | w | j | d |

So the table is a letter-for-letter substitution with a few homophones (a: 5, 8, A; s: 2, F), written mostly in digits.

## Reading (normalised; [..] = conjectural)

> ... noch nicht zu vernehmen, [die Landtschaft ...] ... [unleserlich] ..., das kann dieses orths halber observiren,
> dagegen den selben etwas tentiret werden solte, zumahl nicht unbewandt [was und ob] gebührend zur manutenirung dero
> Kays. Maj(estät) und des Reichs wie auch [bey diesen] ... [ungelegen]; dahero ich nicht unterlassen sollen, die
> notturft dieser Vestung so wol allerhöchst ihrer Kays. Maiestet als auch ihrer Churf. Durchl. in Bayern ohnlängst
> nochmals allerunderthenigst und underthenigst anzudeuten, damit ich aus allen fall entschuldigt sein und dessen,
> meinem gebührenden bericht an gehörigen ort, nicht ermangeln möchte.

The writer reports to Kassel that he has set out the needs of "this fortress" (dieser Vestung) to the Emperor and the
Elector of Bavaria, and asks to be held excused ("damit ich aus allen fall entschuldigt sein"), so he writes as an officer
or agent on the imperial side, from a fortress.

## Measurement

Second pass on lines 1–2 (22 Sept): line 2 `12 7 12 / 6 0 0 8 T 4 / 0 9 / 12 F / 6 7 W / 7 4 12 / 6 0 1 F F / 4 5 D 9 6 12`
= "(w)ir (d)ennoch nur seit ihr endes halber ... ursach" (an initial sign dropped in transcription on two words);
line 1 `1 7 6 / A 5 0 1 W F` = "die landts..." (first sign is 1 = d, not 7; A = l here). Unread: the last ~9 signs of
line 1 and ~6 blotted signs in lines 7 and 9, about 15 of 590 signs. 96.8% measured in `reading_tokens.txt` (538 signs, 17 unread). Class:
read; key recovered. After the line 9 correction of 30 Sept (below): 97.4% (538 signs, 14 unread: nine in line 1, one in
line 2, three in line 7, one in line 10).

## Remaining gaps

- End of line 1 (~9 signs, `W 5 ? 1 7 0 4 5 6`) - blocker: illegible; cramped under the faded gloss on the only scan.
- Line 7 "ueidiesen boni" - blocker: illegible; single signs blotted on the same scan. (Line 9 "serue st" was listed
  here until 30 Sept; its signs are clear and read "dieser Vestung", see the correction below.)

## Escalation
- [x] siblings: all 126 records R4452-R4577 of the volume downloaded; no clear copy of this letter
- [x] clear-pages: the interlinear gloss on lines 1-4 used as crib and control
- [x] known-keys: sign alphabets R4467, R4491, R4520, R4525 compared; none is this key
- [x] print: no edition of HStAM 4 d Nr. 1218 found; DECODE has no transcription
- [x] key-rebuild: homophonic anneal on de-1500s plus hand fixes; key recovered
- [x] retry: lines 1-2 and the doubtful signs re-viewed at 3-4x zoom; still open

## Corrections

- **30 Sept 2026 (reported while quotations were pulled for Lasry's list; checked on the scan).** Line 9: its first
  three signs `F 6 12`, marked unread as blotted, are clear on `IMG_R4500_I26572_P.jpg` (main checkout
  `marburg1635/img/R4500.jpg`, zoomed 3x) and give `s e r` with the key unchanged. With the end of line 8 (`1 7 6` die)
  and the rest of the run (`9 6 / F W / 9 0 3`) the text is "die|ser ue st ung" = "dieser Vestung" (9 = u/v), so the
  conjecture "dieser [sachen]" is withdrawn: "die notturft dieser Vestung", the needs of this fortress. Line 11: the
  "..." after "nochmals" hid `F 5 / D 6 12` = "s a / l er", and on the scan the triangle carries a doubling bar (ll), so
  the text is "nochmals allerunderthenigst und underthenigst" (allerunterthänigst for the Emperor, unterthänigst for
  the Elector); nothing is supplied. `reading_tokens.txt` updated (L09 signs read, L11 D = ll): 14 of 538 signs unread,
  97.4%. Changed: `docs/marburg1635.html` (reading, English, summary, uncertainty list), `docs/reveal/marburg1635.json`
  (caption, D = ll), this file, `profile.json`. Not changed (outside this folder): `papers/lasry/excerpts.json` still
  quotes both places with "...". Not re-checked: line 7, where the scan shows a clear-text insertion after "auch"
  (abbreviated "K. Chur...", then a struck-through group) that `cipher_tokens.txt` does not record.
