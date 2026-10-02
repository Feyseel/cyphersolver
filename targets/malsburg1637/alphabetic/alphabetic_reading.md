# Malsburg, 7/17 January 1637: alphabetic-block working edition

Larry Beck, with ChatGPT. 2 October 2026.

The ten-line alphabetic block can be read substantially with a repeating additive key of **4, 5, 3, 6, 2** over **abcdefghiklmnopqrstuwxyz**. This contribution preserves the inherited 523-position transcription and its literal output alongside a selected 510-position image-reading branch. The latter yields a connected discussion of command, Swedish generals, reciprocal joining of forces and requested authority. It is a working edition, not a claim that every sign or word has been settled. **43, 45 and the angular pair labelled LL remain unidentified.**

Daniel Bourdeau supplied the inherited provisional transcription, source presentation and prior decipherment of the surrounding numerical letters. Larry Beck directed this investigation with ChatGPT. Separate reading and computational passes were AI analyses, including source-image readings without the proposed plaintext or key. They are not review or endorsement by a human paleographer. Some targeted image questions were selected after inspection of residual decryption, so the entire process is not a blinded experiment.

## Run the compact verification

From the repository root:

```sh
python3 targets/malsburg1637/alphabetic/alphabetic_verify.py
```

The script uses the Python standard library and writes nothing by default. It works from any current directory. `--write-results` regenerates [alphabetic_verification.json](alphabetic_verification.json). It checks:

- The original and selected literal outputs, all 1,033 alignment rows, the 33-run transcript-difference ledger and phase effects.
- The original-source record against all ten inherited source lines in `../ct/hcp497_letters.txt`, without replacing that existing file.
- All 64 combinations of the six specified source alternatives, reconstructed from their declared changes, and the recorded literal outputs and counts.
- Re-encryption consistency and the effect of a proposed global key alteration at the two residual word defects.

Re-encryption checks internal consistency, not the historical truth of a reading. This compact script does not redo the earlier exhaustive key search, inspect handwriting, choose identities or score German. Earlier investigation logs report reproduction of all 7,962,624 five-shift keys against the unchanged first 112 letters with a frozen four-letter language model. That search and its corpus are not bundled here; this package reproduces the fixed-key and source-sensitivity results only.

## Inputs and phase rules

The alphabet uses zero-based indices. Decrypt by subtracting the key value modulo 24. The first ordinary sign uses shift 4, then 5, 3, 6 and 2. The phase continues across line boundaries.

Normalization maps ü to u, ÿ to y and the provisional j to i. No silent modern v is introduced in the literal output. The code labels 43, 45 and LL, punctuation and `[BLOT]` are outside the ordinary stream. Their selected advancement is zero. Earlier tests favored zero modulo five among 125 consistent treatments of the three code labels. That does not establish any group's meaning, expansion length or the number of deleted signs beneath the blot. It does not prove that LL is Latin initials, a number, a personal name or the same word at its other occurrence.

The original line 5 `?` records punctuation/doubt and does not consume phase. An explicit `?` in the line 7 alternative means one unknown alphabetic sign and **does** consume phase. These two conventions are distinguished in the JSON and code.

The legacy raw count **531** includes four letters from two `LL` labels and four letters from `[blot]`. Removing those label letters gives **523 ordinary positions**. The selected branch has **510**. Thus 531 to 510 is not a 21-sign repair count. The deterministic original-to-selected alignment gives 15 one-letter deletions, one insertion, one length-increasing `u` to `ii` replacement and 16 substitutions, a net reduction of 13 across 33 changed runs. With repeated strokes, alignment is not unique and does not count original scribal mistakes.

| Line | Original positions | Selected positions | Selected start phase |
|---:|---:|---:|---:|
| 1 | 53 | 53 | 0 |
| 2 | 59 | 59 | 3 |
| 3 | 64 | 63 | 2 |
| 4 | 57 | 53 | 0 |
| 5 | 51 | 50 | 3 |
| 6 | 54 | 52 | 3 |
| 7 | 53 | 51 | 0 |
| 8 | 52 | 50 | 1 |
| 9 | 53 | 52 | 1 |
| 10 | 27 | 27 | 3 |

## Text layers

[alphabetic_edition.csv](alphabetic_edition.csv) and [alphabetic_edition.json](alphabetic_edition.json) contain all ten manuscript lines with inherited source, original normalized source, original literal output, selected normalized source, selected literal output, editorial German, cautious English and local apparatus. Original and selected literal strings are unchanged from the preserved v2 edition. Editorial spacing is not claimed to be manuscript spacing. The supplied initial-transcription punctuation is retained in the literal layers; punctuation and capitalization in the German reading are editorial.

### Unchanged original literal output

```text
L01 der.[43].stehetitzoaufmsprungewoblen.[45].seinergernlosseinundihd
L02 entbehrenkonnedseistesnudzeitdas.[LL].schreibenweilsiesehendaserm
L03 itdenschwfgangpdgfpppbwyfmdefbtbpoifmeqebacgothdkkkbiwrfqhnbkbig
L04 uxohcm.[45].gpyyscyipdtcspfediqudbdsthcmgsdrtnwonifbeaaeghoeith
L05 edenunddieschwedenwiderbeysiestessen?mustengzxzm.[LL].ybwf
L06 sldufmkdpfykdtdidhghigkwmexyfqecpkgngppadkbhyerpksxdhd
L07 tibixrlfcuxghcupgogxcggbeskontensostelletensieesdahin
L08 wa[BLOT]sihmezuthungefelligwoltenihnauchgulaigotdkpbhdmgdf
L09 migfumkwxweichudeubocftkkgepfzalhiqcphuygkcodqxzutlgl
L10 pfimbiicmsddlxdosgudokygrfm
```

### Selected-branch literal output

```text
L01 der.[43].stehetitzoaufmsprungewollen.[45].seinergernlosseinundihn
L02 entbehrenkonnensoistesnunzeitdas.[LL]schreibenweilsiesehendaserm
L03 itdenschwedischengeneralendescommendohalbersichnichtuergleichen
L04 wurden.[45].estatabererfordertedatsieihretqouppenbeydieschw
L05 edenunddieschwedenwiderbeysiestossen,mustenauch.[LL]acti
L06 onesihmenitmergefielenunduberdasihmesolcheabsolutege
L07 waltwieerbegertenitgebenkontensostelletensieesdahin
L08 wa[BLOT]sihmezuthungefelligwoltenihnauchwiderseinegelege
L09 nheitnitaufhaltensondernihnnachihremitzigdnestatundm
L10 oglichkeitcontentirenlassen
```

### Editorial German, preserving uncertain forms

Square brackets mark uncertain signs or an interpretation; daggers mark unresolved literal forms. The colon after `schreiben` expresses one possible scope, not recovered punctuation.

Der [43] stehet itzo aufm Sprunge. Wollen [45] seiner gern los sein und ihn entbehren konnen, so ist es nun Zeit, das [LL] schreiben: weil sie sehen, das er mit den Schwedischen Generalen des Commendo halber sich nicht uergleichen †wurden†, [45] Estat aber erforderte, dat sie ihre †tqouppen† [Trouppen?] bey die Schweden und die Schweden wider bey sie stossen musten, auch [LL] actiones ihme nit mer gefielen, und uber das ihme solche absolute Gewalt, wie er begerte, nit geben konten, so stelleten sie es dahin, wa[BLOT]s ihme zu thun [gefellig/gefellng]; wolten ihn auch wider seine Gelegenheit nit aufhalten, sondern ihn nach [ihrem/khrem] †itzigdn† [itzigen?] Estat und Moglichkeit contentire[n?] lassen.

### English, under the possible proposed-letter interpretation

[43] is now on the point of making a move [perhaps departing]. If [45] wish to be rid of him and can do without him, now is the time for [LL] to write [perhaps to the following effect]: since they see that he would not reach agreement with the Swedish generals over command [the German has singular er with plural wurden], while the situation of [45] required the joining of their [troops?] to the Swedes and, reciprocally, of the Swedes to them; and the actions associated with [LL] no longer pleased him; and moreover [they] could not give him the absolute authority he demanded, they would leave the matter to what he found [pleasing?] to do. They would also not detain him against his convenience or circumstances, but would have him given satisfaction according to [their?] [present?] circumstances and ability [the final n in contentiren is uncertain].

The words following `schreiben` may alternatively be a recommendation followed by reported circumstances. Neither interpretation proves that [45] actually wanted him dismissed. The joining of forces is presented as necessary, not as a completed movement. The subject of `[they]` before `could not give` is supplied by syntax. Other plural pronouns might refer to one ruler through honorific usage, but this does not resolve the specific `er ... wurden` anomaly. Different code labels need not identify different people; 45 and LL might designate one party through different expressions.

French service, a specific employer, payment, arrears, resignation and a formal discharge are **not established by the January block**. `Contentiren` is translated as giving satisfaction. Malsburg may be transmitting copied intelligence rather than speaking as its originator. The annotation `[E?]: Sixt: / cla:` has no established expansion or attribution.

## Source alternatives and limits

[alphabetic_alternatives.json](alphabetic_alternatives.json) records six binary choices: line 3 h/u, line 6 g/q, line 7 overlap counted zero/one, line 8 y/iy, line 8 n/r and line 9 m/n. Their 64 combinations yield 16 branches with 510 positions, 32 with 511 and 16 with 512. `schwedischengeneralen` and `descommendohalber` survive all 64. The ending `oglichkeitcontentirenlassen` survives 16. These anchors were already consulted; their survival is a sensitivity check, not independent validation or a numerical confidence estimate.

| Location | Selected reading or output | Remaining issue |
|---|---|---|
| Opening group | 43 | A further source-only AI comparison favors 43 over 45, using the clear 45 groups and numeral 3 in 1637. This does not decode it. |
| L3 h/u | nicht / nipht | h is selected; u remains a source alternative. |
| L4:37; global 212 | source w, shift 5, plaintext q in tqouppen | Trouppen is linguistic conjecture. It needs source x or a one-off shift 4; the source pass favored w. |
| L6 g/q | solche / solcho | g is selected; q remains an alternative. |
| L7 overlap | zero signs | A one-sign alternative shifts following phase. A separate h/? remains provisionally h. |
| L8 blot, y/iy, n/r | wa[BLOT]s, one y, gefellig | Deleted extent remains unknown; iy changes count; r yields gefellng. |
| L9:32 m/n | ihrem / khrem | m is selected; n remains an alternative. |
| L9:42; global 473 | source g, shift 3, plaintext d in itzigdn | itzigen is linguistic conjecture. It needs h or a one-off shift 2; the source pass favored g. |
| L10:21 t/? | final n in contentiren | t is favored but provisional; the edition marks contentire[n?]. |

The six binary choices do not exhaust paleographic uncertainty. Unknown blot extent, line 7 h/? and line 10 t/? are not fully enumerated. The groups retain unresolved graphic/provenance questions. Substitutions preserve phase; a net insertion or deletion changes it until compensated, while net changes of five preserve downstream phase. The two malformed words are local defects under the selected branch. Replacing the global key with 4,4,2,6,2 changes 204 positions, including 202 beyond those two targets. That does not establish the local restorations. No cipher text was changed to fit a historical candidate.

[alphabetic_original_alignment.csv](alphabetic_original_alignment.csv) and [alphabetic_selected_alignment.csv](alphabetic_selected_alignment.csv) give source position, normalized character offset, zero-based global position, key phase, shift and literal letter. [alphabetic_edit_ledger.csv](alphabetic_edit_ledger.csv) links the inherited and selected alphabetic positions and records each run's net count and phase effect. Its source-support classification reports the prior AI image analyses; the verifier does not itself validate that evidence.

## Historical findings and exclusions

No inspected document directly equates 43, 45 or LL with a named referent, and no inspected primary paragraph combines the January passage's distinctive clauses. The best specific lead is Melander, but it is not a code solution.

Franz von Geyso, *Beiträge zur Politik und Kriegführung Hessens*, third part, *Zeitschrift des Vereins für hessische Geschichte und Landeskunde* 55 (1926), p.99 n.2, reports that Melander, through Malsburg, sought broad authority from the Landgrave, including power to reward and punish officers. The cited letter is **Malsburg, Wesel, 16 November 1636**, under the old reference **Kr. A. 1636, III**. The date and printed page were checked. This is Geyso's paraphrase, not inspection of the original, and `absolute Gewalt` may be Geyso's wording. It provides no named counterpart to the Swedish-generals clause. [Geyso PDF](https://www.vhghessen.de/inhalt/zhg/zhg_55/Geyso_Beitraege.pdf)

Geyso pp.115-117 describes Wilhelm's retention offers to Melander of 16 and 18 January 1637, including command and the vacant Statthalter post at Kassel. Hofmann, *Peter Melander, Reichsgraf zu Holzappel* (1882), pp.68-69, prints a related command offer and request not to leave, but Geyso expressly warns of departures from the original. These offers weigh against an accomplished-dismissal story. They do not contradict the conditional opening or authenticate this cipher. The January originals remain uninspected. [Hofmann pp.68-69](https://archive.org/details/petermelanderre00schagoog/page/n74/mode/2up)

Wilhelm's letters to Oxenstierna of 5 and 22 November 1636, *AOSB* II:7 (1895), letters 166-167, pp.645-650, discuss combining Hessian and Swedish forces. Reigersberch to Grotius, 27 January 1637, letter 2937, p.56 (receipt 19 February), reports news from Wesel of the Landgrave joining Leslie. These supply context, not a named parallel to the cipher paragraph. [AOSB](https://archive.org/details/rikskanslerenax01styfgoog) | [Grotius letter 2937](https://www.dbnl.org/tekst/groo001brie08_01/groo001brie08_01_0028.php)

Images of HStAM 4 d 1218 Teil 1, keys 5, 30 and 31, were inspected. Key 30's ordinary alphabet gives 43=P and 45=W while using separate three-digit names; it does not support expanding those letters to Peter and Wilhelm here. Key 31 gives Melander 200/500, Sixtinus 521 and Malsburg 523. No multiple independent correspondences establish nomenclature reuse. The earlier Sixtinus key lists both Wilhelm Burckhard and Nicolaus Sixtinus, so the annotation cannot choose one from the surname abbreviation alone. [Arcinsys 1923393](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails?archivalDescriptionId=1923393)

The February letter's French-service departure wording has an unresolved antecedent and a later date. March duplicate readings concerning Wartenberg and discharge cannot identify January's subject. The March passage containing a second LL-like group closes with `hoffuo[156]`, which motivates a Hoff comparison but establishes neither authorship nor the same meaning of LL. Matching numbers by themselves prove neither a shared code vocabulary nor a shared letter cipher.

## Smallest useful missing evidence

1. **LHA Koblenz, Bestand 47, Nr.4400**, cipher codes dated 1635-1641 in the catalogue's Melander affairs. No sheets were available for inspection. A useful match requires several independent entries and provenance, not just 43 or 45. [Catalogue](https://apertus.rlp.de/index.php?PLINK=1&ID=d5c14d42-f356-4ff4-8509-b39dc6dbbcbe)
2. **Malsburg's letter of 16 November 1636** cited above, and Wilhelm's **16/18 January 1637** originals. HStAM 4 h 2208 (late 1636) is only a possible modern route for the November citation; HStAM 4 h 2209, Bd.6/1 (January-March 1637), matches the framework of Geyso's `T.VI,P.1`. Specific folios and concordances are unproved. LHA Koblenz 47/15947 catalogues named 1637 Wilhelm and Malsburg letters without dating each leaf. [4 h 2208](https://arcinsys.hessen.de/arcinsys/detailAction.action?detailid=v2343475) | [4 h 2209](https://arcinsys.hessen.de/arcinsys/detailAction.action?detailid=v1018318) | [47/15947](https://apertus.rlp.de/index.php?PLINK=1&ID=714d7121-c08f-4788-a6e6-ff7fa49ea7bb)
3. For provenance of the other angular group, a **17/27 March 1637 Hoff report**, if present in HStAM 4 f Staaten F, Frankreich 1297 (Hoff reports 1636-1637). Catalogue coverage is verified; that exact letter's presence is not. [Catalogue](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails?archivalDescriptionId=2045812)

These references are retrieval targets, not proof that the documents contain this code. Calendar styles of the separately quoted November/January letters remain to be checked from their originals; writing, event and receipt dates have not been collapsed.

## Provenance and files

The authentic main image is **HStAM 4 h 1411, digital image 0012**, presented through [HCPortal](https://api.hcportal.eu/media/1395/79511677516420.jpg), **2834 x 4284 pixels**. Earlier reports use `f.12` for this digital-image index; it is not a verified physical folio number. No generated or reconstructed image detail was used. The image itself is not redistributed in this compact contribution.

[alphabetic_provenance.json](alphabetic_provenance.json) records the image hash and hashes of the investigation checkpoints used for this export. [alphabetic_selected_letters.txt](alphabetic_selected_letters.txt) contains exactly 510 ordinary cipher letters for profile counting. All ten lines and both literal versions are preserved in the edition files. Historical-source caches, correspondence, private review PDFs and large scans are excluded.
