# Van Dedem 1788–93 code: the codebook is alphabetical within 500-group blocks (partial break)

Outside contribution, 4 Oct 2026 (Feyseel Nur, with Claude Opus 5.5 subagents; adversarial review by OpenAI Codex
in `codex_review/`). It revisits the note in `../NOTES.md` that the code is "not alphabetical in any test".

## Finding

Within each block of 500 groups (thousands digit T, hundreds digit H), the code order follows the alphabetical
order of the Dutch/French words once the groups are re-indexed as:

    position = T·1000 + (H ≥ 5)·500 + line·5 + (H mod 5)     where line = the last two digits

In other words, the entries were filled row by row across five columns and numbered down each column.

- Frequent words fill whole rows: en = 541/641/741/841/941, and de = 85/185/285/385/485/86….
- A real stretch of the table reads 537 egter, 837 eindelijk, 541–941 en, 543 engagement, 643 engager, 644 entrer.

## Evidence (Codex's independent re-derivation)

| Test | Within-block Spearman |
|---|---|
| 95 independently re-aligned crib pairs, this layout | 0.799 |
| Same pairs, plain numeric order | 0.351 |
| Same pairs, 4-column layout | 0.567 |
| Same pairs, 6-column layout | 0.645 |
| Early unfiltered 95-pair list, this layout | 0.602 |
| Null: 10,000 permutations, maximum over 7 layouts | p99.9 = 0.368 |

- Five columns also wins globally: 0.874, against 0.828 for ten columns. Within a block, ten columns gives the same
  ranks as five.
- The alphabetical association is therefore strong and survives removing our own filtering.
- **Not established.** Physical sheets, a single bilingual list, and the boundary near 3150 where names and titles
  begin.
- **Caveat on our own validation.** Our earlier "94% leave-one-out" figure leaked: the rebuild restored held-out
  keys. Disregard it.

## Table and readings

- `dedem_alpha_table.tsv` has 354 values, graded A/B/C as defined in its header. It agrees with the first-pass
  table on 127 of 155 values and moves 39 that fall outside their slot (e.g. 2748 vijftig, 1768 op, 811 deze).
- `decoded_targets_v2.txt` gives R2122 and R2131 with each word graded, and the alphabetical bracket shown for
  every unknown group.
- Word verdicts from Codex: S = solid, P = plausible, X = speculative.
  - **R2131 (9 Feb 1793):** PORTA[S] … aan[S] [den][X] ENVOYÉ[P] verklaard[X] … heeft[P] om[S] gedurende[P]
    deze[P] **Oorlog[S] met[S] de[S]** Franschen[X] en[S] sig[P] in[P] … neutraliteit[X] te[S] houden[P].
    The tempting reading "the Porte's neutrality in the war with the French" is **not** established.
  - **R2122 (15 Jan 1789):** ENVOYÉ[P] het[S] verlangen[X] en[S] van[S] PORTA[S] ontrent[P] het[S] doen[P]
    een[S] -er[X] negociatie[X] … Republicq[P] niet[S] geheel[S] te[S] … ignoreren[S].
    "Negociatie" breaks its own lower bound; "negotiatie" would fit. The crib's loan discussion supports a
    financing theme.
- Independent witnesses for the key words: 1764 Oorlog (R2121 #486), 1518 met (R2121 #10), 86 de (R2053 #5),
  3373 Porta (R2121 #180), 3273 Porte Ottomanne (R1947 #42), 3610 the envoy title (R1947 #407, R2053 #9; possibly
  "de Prusse").

## Next step

1. More deciphered letters in this code (DECODE R1948–R1952, …) would test the layout on unseen documents.
2. A fixed tokenization and spelling.
3. A reader of 18th-century Dutch for the slots.
