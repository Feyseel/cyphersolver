# Erving to Madison, Madrid, 10 Aug 1807: the code transcribed and decoded with a rebuilt Pinckney key

Outside contribution, 4 Oct 2026 (Feyseel Nur, with Claude Opus 5.5 subagents). This answers the "Not done" item in
`../NOTES.md`: *"Erving to Madison, 10 Aug 1807, M31 reel 12 frames 0362-0366: several pages of this code with no decode
on the NARA copy … This is the next target for a rebuilt Pinckney key."*

## Results

- **Founders prints a decode, but not of this copy.** Early-access document 99-01-02-1993 gives a deciphered text
  with about 20 editorial gaps ⟨ ⟩. The NARA duplicate (M31 reel 12 frames 0362–0367) carries the code and has no
  decode. It also differs in its header ("In Mr Pinkneys Cypher, the Cypher of ye Legation") and in the clear text.
- **Code transcribed.** The duplicate holds 1,145 code groups, in `transcription.txt`. Uncertain digits are marked.
- **Key rebuilt.** `key_pinckney.tsv` has 414 entries (395 distinct numbers). It was built by aligning every group
  with its context and the Founders text.
- **Independent check against Wagner.** Jacob Wagner's 1803 decode of Pinckney's own despatch (reel 7, frame 0348)
  shares 47 groups with this letter, and 46 agree: for example 217 would, 1218 some, 872 then, 748.887 au-tho,
  1402 wor, 1598 tain, 301 give. Only 943 is unresolved. The pairs are in `wagner_pairs.txt`.
- **How the code is laid out.** The numbers fall in partly alphabetical runs, for example 870–887
  their/them/then/there/therefore/these/they/thin/thing/this/tho', 1340/41/43 an/ance/and, 742–745
  at/ate/ated/ation. A caret after a group marks a plural.
- **Erving's own slips.** He wrote 66 for "in" three times, 943 for 934 in one "Hanover", and 665 for 605 in
  "change".
- **Measure.** 99.2% of groups read as sense, or 98.3% without conjectures. 80.5% of tokens rest on a value that
  recurs or matches Wagner.

## Founders gaps filled from the code

| Founders | Code reading | Groups |
|---|---|---|
| ⟨ ⟩ has been informed | THAT GOVERNMENT | 1578.1010.284 |
| flattered with ⟨ ⟩ | EXPECTATIONS | 176.979.1593 |
| begins to ⟨see⟩ | NOW BEGINS TO SEE | 429 |
| deceive him ⟨ ⟩ | AND | 1343 |
| understanding with France ⟨ ⟩ to England | HOSTILE | 1544.251 |
| as a dernier ⟨ ⟩ | RESORT | 1154.691.111 |
| his troops ⟨ ⟩ has no expectation | TO HANOVER AND | |
| tranquillize ⟨ ⟩ the alarm ⟨or⟩ | THESE ALARMS, TO CONCEAL | |
| troops to ⟨be⟩ employed | SO EMPLOYED | 1219 |

Disagreements with Founders: "very best informed ⟨persons⟩" against code "VERY [368] AUTHORITY", and "vast costs
brought about by the war" against "vast [767.679.378] SPAIN BY THE WAR".

## What it says

Godoy (the Prince of Peace) paid for the Hanover deal "OUT OF HIS OWN FUNDS". Once peace came, Hanover went to
Westphalia, and he "believes that he has been DECEIVED AND is FURIOUS". A KINGDOM OF EBRO (Catalonia, Navarre,
Biscay) was being planned, and the invasion of Portugal "IS NOW seriously RENEWED with a view to ACTUAL CONQUEST".
Godoy's counter-project was a separate peace with England through Russia, and "as a DERNIER RESORT HE WILL MAKE AN
ALLIANCE … WITH ENGLAND!" There is also a portrait of Ambassador Beauharnais.

## Remaining gaps

- 632.849.1147.455.1482 ("destitute of p-r-i-?-?"), 633, 767.679.378, one group hidden in the binding, and 916 in
  the postscript. Blocker: open-codes; each occurs once.
- 943, 368, and the "narrow low" split 586/1424 are uncertain.
- The copy Founders used was not located.

## Files

| File | Contents |
|---|---|
| `transcription.txt` | groups as read from frames 0362–0367 |
| `aligned.txt` | group → value, in order |
| `key_pinckney.tsv` | the key |
| `wagner_pairs.txt` | the 1803 check pairs |
| `reading.txt` | the full decoded letter and the gap table |
