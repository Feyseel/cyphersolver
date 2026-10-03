# Look-alike check at the images: R9408 `y`, R9408 `4`, R9409 `c+` (2 Oct 2026)

Images cropped with PIL (autocontrast, 1.8-3x upscale) from `../img/IMG_R9408_I44475_P1/P2.jpg` and
`../img/IMG_R9409_I44484_P1/P4/P6.jpg`. Line keys are the transcription line numbers (= the `.tok` keys); sign numbers
are positions in `../sysA2/REC.tok` (normalised codes, as in `lookalike.py`). "Value" is the hand reading's value
from `lookalike.py`. Every row below was seen on the image.

## 1. R9408 `y`: verdict TWO SIGNS, plus a ligature (three shapes in all)

Shapes:
- **ÿ, dotted** (two dots above a y with a tail curving left). Every occurrence read **t** has the dots.
- **γ, undotted** (the same y body, often heavier, with a looped or curled foot and no dots). Every occurrence read
  **r** is undotted. It is the γ already in the R9410 inventory as code `g`.
- **m + γ ligature**: an m whose last arch runs straight into an undotted γ tail without lifting the pen ("ɲ"-like,
  often only two arches visible). This is what is read **m** ("sigmund", "summa", "maister", "meinem"...). It is never
  m + dotted ÿ: where m is followed by a *dotted* ÿ the reading gives **t** ("nit" P1.22, "drithalb" P1.26), and
  where m is followed by a separate undotted γ and then ÿ the reading gives m + r + t (P2.03 "omyy").

Rule: dots = ÿ (t); no dots = γ (r); γ tail joined to the preceding m = the m-ligature (m). Dots are clear on this
hand (two strokes well above the body); in a few places they sit high and are easy to miss in a line crop, so check at
2x or more before recoding.

Proposed codes: keep `y` = dotted ÿ; **`g`** = undotted γ (as R9410); **`M`** = the m+γ ligature, replacing the
transcription's `my` (one sign, not two). `g` and `M` are unused in the R9408 cipher text (only `g` occurs, inside
bracketed clear text).

| line | group (tok) | value | shape seen |
|---|---|---|---|
| P1.01 #4 | Ow3[y]¿+4 | t | ÿ dotted |
| P1.02 #19 | 53¿[y]vy | t | ÿ dotted |
| P1.03 #36 | q6wq[y]43 | t | ÿ dotted |
| P1.04 #15 | 6w7[y]3v | t | ÿ dotted |
| P1.05 #13 | qn[y]34 | t | ÿ dotted |
| P1.06 #24 | E4[y]dm | t | ÿ dotted |
| P1.07 #1 | [y]3vꝁ | t | ÿ dotted |
| P1.09 #12, #15 | 5E[y]ʝ5[y]x | t, t | ÿ dotted (both) |
| P1.10 #6 | wE[y]q3 | t | ÿ dotted |
| P1.11 #8, #18, #25 | 6[y]U, v[y]v, v[y]E | t | ÿ dotted (all three) |
| P1.12 #27 | bx[y]O | t | ÿ dotted |
| P1.13 #12, #15 | 7[y]w, 3[y]x | t | ÿ dotted |
| P1.14 #32, #39 | wy[y]O, q[y] | t | ÿ dotted |
| P1.15 #16, #22, #33 | 4[y]6, v[y]3, x[y]5 | t | ÿ dotted |
| P1.17 #32 | R[y]b | t | ÿ dotted |
| P1.18 #25 | E[y]5 | t | ÿ dotted |
| P1.19 #30 | wy[y]w | t | ÿ dotted (after an undotted γ) |
| P1.20 #8 | E[y]wq | t | ÿ dotted |
| P1.21 #6, #26 | 3[y]x, 4[y]3 | t | ÿ dotted |
| P1.22 #33 | 8m[y]nn | t | m + separate **dotted** ÿ |
| P1.23 #30 | wy[y]7 | t | ÿ dotted |
| P1.24 #13 | q[y]3 | t | ÿ dotted |
| P1.26 #25, #30 | m[y]ʝ, n[y]5 | t | m + dotted ÿ; ÿ dotted |
| P2.03 #21, #25 | q[y]o, my[y]6 | t | ÿ dotted |
| P2.04 #19, #28 | x[y]w, d[y]E | t | ÿ dotted |
| P2.06 #14, P2.07 #1, #21 | x[y]w, [y]v, d[y]4 | t | ÿ dotted |
| P1.01 #37 | qw[y]D | r | γ undotted |
| P1.10 #32 | Ew[y]6 | r | γ undotted |
| P1.14 #15, #31 | Yw[y]4, Ew[y]y | r | γ undotted (big looped foot) |
| P1.17 #16, #37 | Q[y]w, w[y] | r | γ undotted |
| P1.19 #29 | 6w[y]y | r | γ undotted |
| P1.21 #22 | w[y]6 | r | γ undotted |
| P1.23 #15, #29 | w[y]q, w[y]y | r | γ undotted |
| P1.25 #24, #35 | w[y]6, 4[y]6 | r | γ undotted |
| P2.03 #24 | om[y]y | r | three-legged m, then separate undotted γ |
| P2.04 #6 | 9[y]Q | r | γ undotted |
| P1.10 #23 | #m[y]3 | m | m+γ ligature, no dots |
| P1.14 #22 | 7m[y]5 | m | m+γ ligature, no dots |
| P1.13 #39-40 | 5m[y][y] | m, t | plain m, then one m+γ ligature: the image has 2 signs where the transcription has 3 |
| P2.02 #19 | tm[y]4 | m | m+γ ligature |
| P2.04 #15 | 4m[y]5 | m | m+γ ligature |
| P2.05 #4 | om[y]d | m | m+γ ligature |
| P2.06 #10, #21 | qm[y]5, qm[y]w | m | m+γ ligature |
| P2.03 #9 | Em[y]4 | r | m+γ ligature (same shape as the m cases; this reading is probably wrong) |
| P1.18 #13 | Q[y]3 | _ | m+γ ligature coded as bare `y` (no m coded) |
| P1.02 #9 / #21 | #[y]x / v[y]5 | _ | ÿ dotted / γ undotted |
| P1.03 #7 / #15, #17 | x[y]w / w[y]c, c[y]m | _ | ÿ dotted / γ undotted (both) |
| P1.05 #27 / #42 | w[y]d / w[y] | _ | ÿ dotted / γ undotted |
| P1.06 #18, #28; P1.13 #27; P1.20 #24 | | _ | ÿ dotted |
| P1.02 #12 | w[y]4q | _ | **no sign here**: the image has ω + open ч only, so the `y` is spurious |
| P1.16 #21 | w[y]Q | _ | **not a y**: an open ч (the open 4 of question 2) |
| P1.22 #24-25 | 7m[y][y]9 | _, t | only one sign on the image, m + dotted ÿ, so one `y` is spurious |

The `_` (absorbed) cases split between the two shapes. Recoding them will give the second reading round values to
work with. Transcription slips found on the way: a spurious `y` at P1.02 #12 and P1.22 #24, an open ч coded `y`
at P1.16 #21, and the P1.13 `myy` = m + M.

## 2. R9408 `4`: verdict TWO SIGNS (closed 4 = e, open ч = i, as on R9407)

Shapes:
- **closed 4**: a numeral 4 whose diagonal meets the top of the stem, making a closed triangle; the stem often
  runs below the line (q-like in `48`).
- **open ч (ɥ)**: the left arm is a separate short vertical or curved stroke that does not meet the stem top. The
  crossbar runs across both, giving a "ч"/"ɥ"/"zt" look. Usually a little smaller and lighter.

Rule: if the left arm is joined to the stem at the top, it is the closed 4 (e). If it stands free, it is the open ч (i). At line-crop scale the open
form reads as "ч"; at 2-3x zoom the distinction is clear in nearly every case.

Proposed code: **`u`** for the open ч (the code R9407 `augurelio1535/pass2` uses for the same sign; `u` is unused in
R9408 cipher text). Keep `4` = closed 4.

Agreement: of the occurrences checked, i is open in 32 of 35, and e is closed in 23 of 25 (exceptions below).

| line | group (tok) | value | shape seen |
|---|---|---|---|
| P1.01 #12 | 5[4]U | i | open ч |
| P1.01 #21 | 3[4]m | i | closed (?), small; doubtful |
| P1.01 #26 | v[4]w | i | open ч |
| P1.02 #34 | w[4]q | i | open ч (zoomed) |
| P1.05 #9 | ʝ[4]w | i | open ч (zoomed) |
| P1.07 #8 | v[4]w | i | open ч |
| P1.09 #25 | w[4]6 | i | open ч |
| P1.10 #15 | 5[4]x | i | open ч |
| P1.11 #35 | 5[4]7 | i | open ч |
| P1.13 #4 | w[4]q | i | open ч |
| P1.14 #16 | y[4]q | i | open ч |
| P1.15 #15 | w[4]y | i | open ч |
| P1.17 #3 | 5[4]v | i | open ч |
| P1.18 #30 | w[4]q | i | open ч |
| P1.19 #16, #38 | 6[4]w, b[4]d | i | open ч |
| P1.20 #26 | 6[4]w | i | open ч |
| P1.23 #36 | n[4]x | i | open ч |
| P1.24 #30, #33 | w[4]q, 6[4]w | i | open ч |
| P1.25 #32 | w[4]q | i | open ч |
| P1.26 #19 | A[4]m | i | **closed 4** (zoomed); exception |
| P2.02 #6, P2.03 #13 | d[4]E, 5[4]8 | i | open ч |
| P2.04 #4 | D[4]9 | i | **closed 4** (zoomed); exception |
| P2.04 #13, #17 | w[4]m, 5[4]x | i | open ч |
| P2.05 #6; P2.06 #1, #12 | d[4]E, [4]m, 5[4]x | i | open ч |
| P2.07 #11, #14, #22, #28 | w[4]x, L[4]Q, y[4]q, w[4]q | i | open ч |
| P1.01 #6, #41 | +[4]q, v[4]q | e | closed 4 |
| P1.03 #37 | y[4]3 | e | closed 4 |
| P1.04 #26 | w[4]8 | e | closed 4 |
| P1.05 #15, #29 | 3[4]v, d[4]E | e | closed 4 (zoomed) |
| P1.06 #23 | E[4]y | e | closed 4 (zoomed) |
| P1.09 #1, #41 | [4]q, Q[4]v | e | closed 4 |
| P1.09 #35 | q[4]8 | e | **open ч**; exception |
| P1.10 #17 | x[4]v | e | closed 4 |
| P1.11 #16 | ʝ[4]v | e | closed 4 |
| P1.12 #12 | o[4]x | e | closed 4 |
| P1.15 #7 | L[4]8 | e | closed 4 |
| P1.20 #38 | m[4] | e | closed 4 |
| P1.21 #4, #25, #30 | d[4]3, m[4]y, ꝁ[4]q | e | closed 4 |
| P1.22 #5 | 3[4]8 | e | closed 4 |
| P1.24 #11 | o[4]q | e | closed 4 |
| P1.25 #34 | q[4]y | e | closed 4 |
| P2.02 #20, #27 | y[4]q, D[4]d | e | closed 4 |
| P2.03 #10 | y[4]v | e | **open ч** (zoomed); exception |
| P2.03 #29 | q[4]n | e | closed 4 |
| P1.02 #13, #25 | (y)[4]q, b[4]w | _ | open ч |
| P1.03 #5; P1.06 #17; P1.07 #17; P1.08 #26 | v[4]x, w[4]y, 7[4]Q, d[4]w | _ | open ч |
| P1.23 #20, #22 | w[4]5, 5[4]7 | _ | open ч |
| P1.01 #34; P1.06 #11, #19, #33 | d[4]q, Q[4]8, y[4]q, d[4]3 | _ | closed 4 |
| P1.16 #23; P1.22 #12 | Q[4]q, Q[4]q | _ | closed 4 |

The five exceptions (P1.01 #21, P1.26 #19, P2.04 #4 read i but closed; P1.09 #35, P2.03 #10 read e but open) are
probably reading slips, given how consistent the other 55 are. They are worth a second look in the next reading
round. The `4` in R `4o` (`R` code) was not part of this check.

## 3. R9409 `+` after α (`c+`): verdict TWO SIGNS, split by the left loop and not by the cross

The cross itself looks the same throughout: a long horizontal stroke runs out of the left element and is crossed near
its right end by a short vertical that dips below the line. The difference is in the left element:

- **α+ (closed loop)**: a closed α/a-loop whose tail becomes the horizontal of the cross. It takes **da** and, in
  the same shape, **ch** ("durch", "wiligklich", "schartig"), **f** ("ferdinandischen", "abgefertigt", "aufrichten",
  "gefale") and **u** ("uersuecht"). No difference in the cross, curl, length or height separates the da, ch and f
  occurrences. As far as shape goes these are **one sign**, and the da/ch/f split is a key or reading question, not
  a transcription one.
- **ↄ+ (open hook)**: an open reversed-c / "ɔ"/"2"-like hook with no closed loop, joined by the horizontal to the
  cross. This is the sign in every **sch** occurrence checked ("schmaltz" ×5, "schreiben"). The transcription codes
  it three ways: `c+` (P6.10, P6.30, P6.36), bare `+` (P6.32, P6.33, P6.35, and P6.09 `wV+5D`, P6.20 `Pw+5p`), and
  **`E+`**. The `E+` "small plus with curl after E" of `signs.md` is the same ↄ+ (checked at P1.28 "ferdinandischen"
  `pE+w` and "turckisch" `pE+` at line end, P1.08 "schon" `E+9q`). That is why `E+` reads s + ch.

Rule: if the left element is a closed loop, it is α+ (one sign: da/ch/f/u). If it is an open hook with nothing closed, it is ↄ+ (sch).
Proposed code: **`ʃ`** (or any free ASCII letter such as `J`, if preferred) for ↄ+ as one sign, replacing `c+` where
the hook is open, bare `+` and `E+`. `c+` stays for α+, which should probably become one code too (e.g. `ç+` → `α`
single sign), since the + never occurs after a closed α without it.

Side finding: the transcription's `c` also covers an open ↄ outside the + groups (P6.04 line start `co5` = "ↄo5").
`co`/`zo` deserves the same open/closed check before the next key run.

| line | group (transcription) | value | shape seen |
|---|---|---|---|
| P1.13 #13 | Epwc+Aw | da | α+ closed |
| P1.14 #8 | Epwc+pw | da | α+ closed |
| P6.03 #15 | pVc+P9 | da | α+ closed |
| P1.12 #15 | E4Vc+w3 | ch (durch) | α+ closed |
| P6.04 #18 | bmEc+Vw | ch (wiligklich) | α+ closed |
| P6.12 #8 | S^E-c+5V | ch (schartig) | α+ closed (the coded `E` here is the tall barred sign) |
| P1.28 #24 | Epwc+wVE | f (ferdinandischen) | α+ closed |
| P4.10 #14 | #4c+wV | f (abgefertigt) | α+ closed |
| P6.04 #30 | 53c+VmE | f (aufrichten) | α+ closed |
| P6.21 #45 | #wc+5T | f (gefale) | α+ closed |
| P1.28 #9 | Epwc+wVx | u (uersuecht) | α+ closed |
| P6.10 #13 | w3VSc+Vw | sch (schreiben) | **ↄ+ open hook** |
| P6.30 #4 | 5qc+75 | sch (schmaltzen) | **ↄ+ open hook** |
| P6.32 #1 | +75bCT | sch | **ↄ+** (coded bare `+`) |
| P6.33 #33 | E47+75 | sch | **ↄ+** (coded bare `+`) |
| P6.35 #4 | E47+75 | sch | **ↄ+** (coded bare `+`) |
| P6.36 #21 | 9wVc+75 | sch | **ↄ+ open hook** |
| P6.09 | #wV+5DY | (ch) | ↄ+ (coded bare `+`) |
| P6.20 | Pw+5pb | (ch) | ↄ+ (coded bare `+`) |
| P1.28 | pE+wq | ch (ferdinandischen, s+ch) | ↄ+ (coded `E+`) |
| P1.28 end | cHpE+ | ch (turckisch) | ↄ+ (coded `E+`) |
| P1.08 | E+9qw | ch (schon) | ↄ+ (coded `E+`) |

Not checked at the image: the 23 `c+` read `_`, the remaining 47 da, P2.15/P4.11/P4.12 "durch", P4.35 "acht",
P5.27 "schwer", P7.04, P7.21, P7.24 "schon" (`çpç+`, which may be an ↄ+ coded `c+`), the u/g/h singletons.
