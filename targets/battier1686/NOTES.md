# Pieter Battier to Gaspar Fagel, Madrid, 1686–1688

Status: read in part; **read with known key**. Two focus letters pass the strict sense screen:
19 December 1686 and 8 April 1688. The volume is not a complete decipherment.
Decipherment by **Feyseel Nur (with Claude and Codex)**; 4 October 2026.

## Documents and key

- Nationaal Archief **3.01.18, inv. 401**, 109 scans: Pieter Battier, Dutch envoy extraordinary
  in Madrid, to Grand Pensionary Gaspar Fagel, 1686–1688.
  https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/401
- Key: Nationaal Archief **1.10.29 (Fagel), inv. 1209**, 86 scans, headed
  “Voor den Heer Extraord. Envoye Battier”.
  https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/1209
  DECODE **R2794** holds this key but cites “inv. nr. 5345”, which is absent from the current
  1.10.29 inventory. The correct inventory number is **1209**. This is application of an
  identified key, not recovery of an unknown cipher.
- Contemporary decipherments: 5 December 1686, scan **28R** (cipher 30R, 31L);
  30 January 1687, **42R–43R** (cipher 41R, 42L, 44R); interlinear **101R**, 26 February 1688.
- The States General set, NA **1.01.02, inv. 12588.120–125**, is not digitised.
- Manuscript images: Nationaal Archief, **CC0**. The site lead is inv. 401, scan 108, right page.

No edition was found; the letters are not in DECODE.
K. M. M. de Leeuw, *Cryptology and statecraft in the Dutch Republic* (University of Amsterdam,
2000), discusses Fagel codebooks but never Battier. See `evidence/prior_art.md` for the citation.
The prior-art search covered De Leeuw (2000), DECODE, Tomokiyo, editions and the
Nationaal Archief digitised series. This is a bounded finding, not proof that no unpublished
reading exists.

The transcriptions were made by LLMs from the Nationaal Archief scans and checked against
the key images. Uncertain digits, marks and dictionary readings remain identified below.

## System

The letter table, **2–98**, has eight homophones per vowel and three per consonant
(`key/letters.py`, key scans 3–6); vowel-substitute letters are also recorded there.
A one-part alphabetical Dutch codebook repeats **99–999** in fifteen blocks, selected by
a mark above the number: none, tilde, backslash, caret, slash, e, l, r, bar, two dots,
first/second/third digit struck, c/, reversed c/. Block 13 begins at 100. The transcriptions
use `block:number`; bare 2–98 are letters. Names include Spanish councils and grandees
on key scan 59, with places on scans 78–82 (transcription series 16).

Approximately 1,400 codebook values were read from the key images; Codex counts **1,393
distinct dictionary codes**. Sorted TSV files retain the dictionary override order, including
`zz_corrections`. The 365 alphabetical reversals (96 touching focus tokens) are **not 365
proven misreads**: inflection, thematic lists and historical spelling can break strict order.

## Conservative results

| Letter | Cipher scans | Tokens | Key-attested | Strict sense | Generous ceiling | Verdict |
|---|---|---:|---:|---:|---:|---|
| 19 Dec 1686 | 31R, 32L | 186 | 186 | 186/186 = 100% | 100% | passes |
| 4 Dec 1687 | 91R, 92L | 211 | 210 | 199/211 = 94.3% | 96.7% | below |
| 12 Feb 1688 | 99R, 100R | 271 | 268 | 250/271 = 92.3% | 96.7% | below |
| 8 Apr 1688 | 107R, 108L, 108R, 109L | 323 | 322 | 313/323 = 96.9% | 99.7% | passes |

These are the Codex review numbers, not the more generous original H+C totals. The strict
screen excludes unkeyed emendations and unresolved meanings in `codex_review/semantic_adjustments.tsv`;
semantic screening is judgment, not statistical confidence. Literal key attestation alone
does not establish meaningful text. Roughly **55% of the cipher in inv. 401** has been read
(estimated, not a measured volume-wide denominator). `inv/orch_letters.tsv` lists the unread
letters. Its legacy READ label means transcribed/decoded/graded, not a pass of the strict bar.

## Reading: 19 December 1686

The letter has 186 cipher tokens, all key-attested and accepted by the strict screen.
The ciphered stretches concern candidates for the Netherlands governorship and Madrid's
failure to organise defence. In the original Dutch, with editorial spacing:

> van de Graaf van Mansfeld, maar sedert het dese laatste eens gemanqueert heeft, is syn persoon
> weynigh geaestimeert, en syn credit hier aan 't hof seer geringh, en daarom ook voor hem weynigh apparentie.

> maar daarom werden de publicqe affairen niet gedaan en blyft alles traineren.

> maar soo men die helft vinden kost, soude haastelyk een ander gouverneur de reys na Vlaanderen aannemen.

> soo veel impressie, dat men dan soo voorts op geen defensie gedenckt; en wat noch meer is, men mach se
> ook soecken te desabuseren soo veel men kan, soo syn se soo seer gepersuadeert dat Engelandt en de Staat
> de Spaansche Nederlanden par raison d'interessen sullen moeten defenderen, dat se weynigh op andere middel gedenken.

The surrounding clear text explains the money request and negotiations; it is marked in
`readings/s031R_text.txt` and `s032L_text.txt`. Their provisional date headings predate the
inventory's identification of 19 December and are preserved as source history.

## Reading: 8 April 1688

The reviewed reconstruction is `codex_review/april_reading.md`; it supersedes the fluent
interpretations in `readings/s108-109_text.txt`. Representative cipher clauses:

> Den Grand Maestre aan syn agent geordonneert de oude Koninginne te verseekeren …

> Ondertusschen soo formeert sich een gesworen partye tegen den selven: Connestable van Castille,
> Os[t]una en Mon[i→t]ere [Monterey?] brouwen wat met malkander.

> de Nederlandse toestemminge, gelyk in tyt van Grana is geschiedt, door syn handen niet veel sullen passeren.

The instruction to the agent and faction formation are solid within the transcription.
The Holsteyn project and Monterey's presidency ambitions are plausible; Osuna, pronoun referents
and the administrative meaning of *toestemminge* are speculative. Read **“Grana is geschiedt”**,
not “Grana's geschiedt”. Troop and money figures in the project's description are clear text.
The unfilled viceroyalty on 108L is **12:6?0**; it is not identified here.

## Other letters and validation

The 4 December 1687 and 12 February 1688 readings are retained with their token tables,
but neither passes the strict sense threshold. The reading corpus, including
29 January and the partial 26 February 1688 check, is supporting material, not a set of new
complete-reading claims. Every difficult token in the four focus letters remains traceable
through the TSV notes and the review's semantic adjustments.

The validation letters contain **369** tokens (5 December 1686) and **781** (30 January 1687).
Agreement with contemporary decipherments where comparable is **1113/1132 = 98.3%**;
key-alone agreement is **94.7%**. Eighteen positions are not comparable. The source filename
`validation_1687-01-16.txt` is a legacy misdate: the inventory and validation summary identify
the letter as **30 January**. Comparison used the existing decipherments, so this is not a blind
holdout claim. In the shuffle control run with `scripts/control.py`, **72%** of spelled runs segment into Dutch,
versus mean **1.2%**, maximum **4.1%**, for **300** permuted tables. Segmentation tests structure,
not correctness of names or syntax; the fixed lexicon and names list influence this result.

## Grades and review limits

Repository grades: H = primary-key support, C = contemporary-plaintext support, M = uncertain,
I = inferred. The reading TSVs instead use H = secure key/sense, C = contextual digit/mark
choice, M = conjectural, I = unread/no sense. **Those legacy grades are preserved, not silently
converted into repository grades or used as the headline result.** Literal decoding and the
strict review screen take precedence. Context-only repairs are inferred (I), uncertain glyphs
are M; no aggregate repository-grade counts are claimed.

The alleged **81=e habit** comprises 17 occurrences: 14 contextual e, 3 retained i. The key
has **81=i**. Neither fully validated letter contains 81, so they do **not** confirm this habit.
`getwist` is the key reading where the contextual interpretation proposes **Turck(en)**; that
inference remains open. The Codex review is independent **software re-decoding, not paleography**.
Shifted annotations, dictionary variants and mark choices still require image checks.

## Remaining gaps
- Focus-letter unresolved groups and sense: 12:6?0; getwist versus inferred Turck(en); Novelli/Hofmeester, gesoubconneert gouverneren and Sex.; name repairs, 81 and other emendations in semantic_adjustments.tsv - blocker: open-codes; key lookup alone does not settle the meaning or mark choices
- Unread volume letters listed individually in inv/orch_letters.tsv, including 102L and the untranscribed cipher on 95R - blocker: open-codes; not yet transcribed; workable with the same key
- States General parallel set NA 1.01.02 inv. 12588.120–125 - blocker: needs-physical-access; not digitised

## Escalation
- [x] siblings: all 109 scans inventoried; unread letters listed in inv/orch_letters.tsv are not yet transcribed; workable with the same key
- [x] clear-pages: 28R and 42R–43R compared to validation letters; 101R has an interlinear check
- [x] known-keys: Battier's named inv. 1209 key applied; DECODE R2794 shelfmark discrepancy recorded
- [x] print: De Leeuw (2000), DECODE, Tomokiyo, editions and NA digitised series searched; no Battier edition found; see evidence/prior_art.md
- [x] key-rebuild: dictionary transcription and correction overrides preserved; Codex identifies remaining variants and alphabetical reversals
- [x] retry: four focus letters re-decoded and screened for sense; unresolved readings recorded in semantic_adjustments.tsv; unread letters not yet transcribed; workable with the same key

## Files and reproduction

- `key/letters.py`, `key/dict/*.tsv`, `key/colindex*.txt`: transcribed key and column locators.
- `tokens/`: line-labelled cipher tokens; `readings/`: legacy graded tables and texts.
- `codex_review/`: review.md, audit_notes.md, april_reading.md, metrics.tsv and semantic_adjustments.tsv copied verbatim.
- `scripts/decode.py`: key-only decoding; run `python3 targets/battier1686/scripts/decode.py targets/battier1686/tokens/s031R.txt`.
  Do not use `--write` on preserved readings: it overwrites grades.
- `scripts/measure.py`: legacy grade totals, **not** the conservative review's semantic screen.
- `scripts/control.py`: permutation control used for the reported results; requires the original
  OpenTaal word list via `BATTIER_OPENTAAL=/path/to/opentaal.txt`. The lexicon is not bundled.
- `scripts/build_reveal.py`: decodes the continuous 59-token passage on 31R and compares it to the reading table.
- `scripts/build_site.py`: scoped use of the repository builder for this page and shared indexes;
  does not rewrite other target pages or their replay files.

The thesis PDF and full manuscript scans are not included.
No DECODE letter update is applicable: the letters have no DECODE records; the R2794 key
shelfmark correction is documented here without making an external edit.
