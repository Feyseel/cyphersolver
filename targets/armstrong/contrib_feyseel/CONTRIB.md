# Armstrong THE=972: remaining gaps, collated against M34 roll 14; and a known-code search on 20 Feb 1808

Outside contribution, 4 Oct 2026 (Feyseel Nur, with Claude Opus 5.5; the search was run by OpenAI Codex). It
addresses the "Remaining gaps" list in `../NOTES.md`.

The frames were fetched from `catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-014/M34-014-00NN.jpg`:
frame 0024 (15 Feb 1808) and frames 0033–0034 (22 Feb 1808). Both are fair copies in a clerk's hand.

## 1. Readings now attested on the frame (22 Feb 1808)

| Founders | MS (frame 0034 unless noted) | Reading | Note |
|---|---|---|---|
| 769 **803** | 769 **805** | "stating the **dread** of his government and the means taken by it to avert the introduction into Denmark of a general army" | 769 sits in the slot 765 does < dre < 771 du; 805 = ad(d). Together they give dre-ad. This closes the gap "the dress ac[count?]". |
| … him self **1245** suc ce d ing | **1225** (probable; the clerk loops his 2) | "consider himself **as** succeeding to dominion of her colonies" | 1225 = as (H). |
| 1086 723 **1357 755** 772 | **1337 255** (255 probable) | if **Bo-na-part-e** succeeds to the crown of Spain | 1337 = na (H), 255 = part (H). |
| 946 | **914** (frame 0033) | Gu-sta-v-us | Agrees with the repo's own correction. |
| 916 | **910** (frame 0033) | "Denmark cannot **go** very willingly" | |
| 631 (com-…-t-s) | **651** | com-**plain**-t-s | The first 631, in "her old and 631 course", really is 631 = *wise*, and reads as sense. |

The MS confirms the following as printed, so they stay open:
- `962 . 1354 968 1494 1244 1387` "of Hamburg waited in the antichamber". A candidate for 1244 1387 is *cou-rier*:
  1244 is next to 1245 *cou*, and *rier* fits the slot of 1387. Not settled.
- `972 406 1216 1440 418 1116 1354 174` "for ever the [406]-an-[1440]-ose-s of Europe". 418 *ose* is really there.
- `337` in "it has driven her 337 of her old and wise course". The 3 is clear, so a 3↔5 slip to 537 *out* is not
  supported.

## 2. 15 Feb 1808 (frame 0024)

- The MS writes **484** and **1**: "the most marked man-ner 484 1105 1116 ag-gres-s-ion-s on our 1".
  - Proposed: 484 → 1484 *it*, giving **its** aggressions. This is a dropped leading 1, the same slip as 555 for
    1555 in the 30 Aug postscript.
  - Proposed: 1 → 4 *commerce*.
  - Both are emendations of the MS, not misreadings by Founders. Meaning: high; mechanics: medium.
- The MS writes 962 in "de-x-962-it-y", with 1005 *de* added above the line by the copyist. It also writes 1177 in
  "im-1177-d-ence". These are writer slips, as the repo already notes.

## 3. 5 Mar 1808 (roll-14 transcript)

- `257 1338 1001 626`: "there are people **name-d** who perhaps would not like their master to know …". 1338 sits
  between 1337 *na* and 1340 *native*, and the clerk's pencil reads "[..]d who". Lafayette has just named Cretet,
  Fouché, Champagny and Talleyrand. Grade I, high.
- `669 1369 847 1116`: "to put **our** ships in requisition". 1369 is either an adjacent homophone of 1367 *our*
  or a 7↔9 slip. Grade I, medium.

## 4. 20 Feb 1808: known State Department codes with private transforms

**Result: no signal.** The full report is in `feb20_known_code_search/REPORT.md`.

- **What was tested.** WE028 (THE=1385; Tomokiyo's transcription) and the THE=972 table, each under shifts
  (direct and modular), digit reversal, 24 digit permutations, per-digit offsets, separate shifts for groups <100
  and ≥100, and affine maps: 19.6 M settings in all.
- **Controls.** Every search was repeated on 200 shuffled ciphertexts. The best real z is 1.83, and the
  family-corrected p is 0.403.
- **Frequent groups.** No transform maps the five frequent groups (17, 18, 38, 1, 14) to the/of/and/to/a.
- **Digit statistics, for the record.** Groups ≥100 end in 0 39% of the time and in 1 20%; 2, 3, 5 and 9 are
  almost absent. THE=972 is uniform. A "decade-family" (inflection-digit) reading of this skew does not beat a
  shuffle control: 45 multi-member decades observed, against 42.1 expected (95% bound 47).
- **Limitations.** Other Weber tables could not be fetched. The language model is a character bigram trained on
  Austen.
