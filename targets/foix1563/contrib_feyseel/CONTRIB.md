# R9241 (Catherine de' Medici to Paul de Foix, 15 Jan 1563): the cipher is de Foix's own (partial)

Outside contribution, 4 Oct 2026 (Feyseel Nur, with Claude Opus 5.5 subagents; adversarial review by OpenAI Codex
in `codex_review/`). It addresses the R9241 gap in `../NOTES.md` ("no-key-material; … ciphertext-only annealing …
finds no language").

## Identification

The sign set matches **Paul de Foix's cipher** as reconstructed by S. Tomokiyo from de Foix's own letters of
11 Oct 1565 (cryptiana `henryiii.htm#Foix0`; BnF fr. 15971 ff. 21–22, with its contemporary decipherment on f. 25r
and a marginal one on f. 26r; Gallica ark btv1b105094409, view 2N+9 for f. Nr). This key is not on DECODE, which
is why the known-key search missed it.

Values confirmed on the 1565 decipherments:
- 50 = que. The transcription's "so" is the copyist's 50, so "so f so" = 50 f 50 = *quelque*.
- 82 = ceulx, 51 = qui, 37 = me or car, ny = n or z.
- g = s; f = s as well as l/u. Several signs are genuinely two-valued.
- Word signs also serve as syllables, e.g. 83 30 = Le-c-est-re.

## Evidence

**Unfitted published key versus shuffled signs**

| Language model | Real | Token-order shuffle | Sign-identity shuffle |
|---|---|---|---|
| Original LM | −1.517 | −1.759 ± 0.031 (7.8 SD, n=200) | |
| Codex's independent LM, trained on Montaigne, 215k characters | −1.582 | −1.894 ± 0.029 (10.7 SD) | −2.095 ± 0.118 (4.3 SD) |

The identification is solid.

**Reading coverage, v5, with a measure fixed in advance**

The measure is the share of the 1,026 tokens that fall in dictionary words of 4–14 letters, against 200 shuffles.

| Key layer | Real | Shuffled mean (max) |
|---|---|---|
| Frozen key (independent of R9241), grade A | 14.0% | 7.0% (10.2%) |
| Frozen key, grade A + B | 25.6% | 12.7% (17.1%) |
| + values fitted on R9241 that recur in ≥2 passages | 58.5% | 20.7% |
| + all fitted values | 69.6% | 24.3% |

The fitted layers flatter the real text, because those values were chosen on it.

## What can and cannot be claimed

- **No full sentence is forced by the independent key alone.** It yields fragments only: "pour le moins estre
  [m]e la partie", "aiant faict", "quelque traict", "tout ce qui est pa[s]é et toutesfois".
- **Phrases that need only recurring fitted values (C1), no letter edits:**
  - "pour le moins estre de la partie"
  - "la negotiation prend quelque traict"
  - "dexterité de son esperit" (Codex: 1 of 54 permitted paths)
  - "quelque deboursement de deniers"
- **Phrases that need letter edits (C3):**
  - "abondance de langaige" and "entre ces deux royaulmes" need 2 edits each.
  - "faire son proufit" is withdrawn: it needs 3 edits.
- **Subject (inference):** an English negotiator who visited the Queen Mother after Dreux, probably Throckmorton.
  Not proven.

## Blockers and next step

- Image crops of R9241 (BL Add MS 4136 ff. 148v–149; DECODE login) are needed. They would settle the conflicts
  between the chart and the fitted values: r (m against d), z (p against i), Yb (l against u), 3/Z3. Codex also
  asks for a glyph audit of the transcription.
- 80 and 93 do not occur in 1565. A de Foix letter of 1563–64 with a decipherment would fix them (try TNA SP 70).

## Files

| File | Contents |
|---|---|
| `reading.md` | graded reading: A plain, {B}, [C1], [[C2]] |
| `key_k0.json` | frozen key |
| `key_k1.json` | fitted layer, with the words that motivated each value |
| `v5_coverage.txt` | coverage measure and shuffles |
| `v5_phrases.json` | per-phrase path counts and edits |
| `v5_rendering.txt` | full rendering |
| `codex_review/` | the adversarial review |
