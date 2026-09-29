# Andrea del Burgo to Gattinara, 26 October 1527 — DECODE R9970

**Verdict (28 Sept 2026): not a cipher. R9970 is a clear Spanish minute, two drafts of a letter from the Emperor
Charles V "al príncipe" (Prince Philip), about an exchange (*cambio*) with Anton Fugger. It dates between 1543 and
1554, not 1527.** Catalogue entry 198 is resolved and removed; the DECODE correction is queued. The Andrea del
Burgo → Gattinara letter of 26 Oct 1527 that DECODE (after Galende 1994 p. 163) attaches to this shelfmark is not
on these scans and was not found elsewhere. See "Identification, 28 Sept 2026" below.

Earlier summary (22–23 Sept): *Attempt closed for now, target unread.* The four images attached to R9970 are accessible, but they show heavily revised Spanish financial drafts headed `al principe`, not an identifiable letter from Burgo to Gattinara. This is a probable metadata/image mismatch, not proof that the historically cited Burgo letter was not enciphered. Do not mark the Burgo letter solved or decrypted.

## Identification, 28 Sept 2026

Re-read the opening of both drafts from the full-resolution scans (crops in the write-up):

> Draft 1 (archive p. 1): *demás de los cambios que hasta aquí se an hecho por n[uest]ro mandado con Antonio
> Fucar, de que os hab[em]os avisado con los correos pasados, a convenido, por estar en lo que estamos, hazer este
> cambio de CX U DCC LXX d[ucad]os de a LXV gruesos …*
>
> Draft 2 (archive p. 2, second `al principe`): *demás de los cambios que hasta aquí se an hecho, a convenido hazer
> otro de CX U DCC LXX d[ucad]os de a LXV gruesos …*

Further down draft 2: the sums to be paid "el principal con intereses a los plazos", the cédulas to be "cumplidas,
guardadas y observadas", and a payment date "a los vj de …". This is the formula of an imperial minute ordering
the Prince's government in Spain to honour an asiento (exchange loan) made with the Fuggers: "por n[uest]ro
mandado", "os hab[em]os avisado" is the Emperor's plural, and the address "al príncipe" is Philip.

- **"Antonio Fucar"** = Anton Fugger (1493–1560), head of the Augsburg firm from 1525; the Spanish documents always
  write *Antonio Fúcar*.
- **The amount** is 110,770 ducats ("CX U DCC LXX", U = thousands) "de a LXV gruesos" (Flemish groats, reading of
  the unit tentative), i.e. reckoned in Flemish money: the loan was taken in the Low Countries or Germany and
  repaid in Spain.
- **Date.** Philip was born on 21 May 1527, so a letter to "the Prince" about Fugger exchanges cannot date from
  October 1527. Charles V wrote such minutes to Philip as regent of Spain in 1543–1548 and 1551–1554 (Philip was
  "príncipe" until he became King of Naples in July 1554). The year is not on these leaves, and the cambio was not
  matched to a specific asiento (Carande, *Carlos V y sus banqueros*, lists them; not consulted).
- **No cipher anywhere on the four surfaces.** The "alphabet, graphic signs, numerical" tags on DECODE fit the
  Roman-numeral amount and the U thousands sign, which are ordinary accounting notation.

PARES searches (28 Sept): `EST,LEG,1563,572` and neighbouring folios return no item-level records, so legajo 1563
is not itemised online; "Burgo Gattinara" finds only PTR leg. 56 no. 50 (Maximilian's 1509 power to Gattinara and
Andrés de Burgo); Burgo/Ferrara 1527 searches find nothing. Where the 26 Oct 1527 letter really is remains open:
Galende's list (drawn partly from Carmona 1894) has either an old or a wrong reference.

Shelfmark supplied: AGS, Estado, leg. 1563, fol. 572. Initial catalogue calls this Spanish, four pages, non-decrypted. Those are metadata, not yet verified against the manuscript.

## Research log

- 2026-09-22: Exact date, correspondents and shelfmark found in Galende Díaz, *La escritura cifrada durante el reinado de los Reyes Católicos*, p. 163. This is a citation, not a decipherment.
- Initial web searches of the exact date and correspondents and Tomokiyo references did not locate a reading. Direct web-tool access to DECODE, Cryptiana and British History Online failed; attempting the repository's existing authorized DECODE retrieval workflow.
- All four images downloaded successfully using the repository's existing authorized shared session. All inspected at page scale; both draft openings, amounts, middle and closing passages also inspected in enlarged crops.
- The scan banners and manuscript numbering establish archive order 1, 2, 3, 4, whereas DECODE presents them in order 3, 1, 2, 4. Image 4 is blank apart from show-through. There is no attached document or associated record on R9970.
- The apparent cipher line is a repeated monetary expression: `CX [thousands sign] DCC LXX [currency abbreviation] de a LXV [gruesos?]`. The draft version spells the intervening `de` clearly. The numeral interpretation is 110,770, but the currency abbreviation and following unit are not securely resolved. This is evidence for accounting notation, not a recovered substitution alphabet.
- British History Online was accessible through ordinary HTTP requests. Inspected *Calendar of State Papers, Spain*, III.2, October 26–31, 1527, pp. 432–449. No Burgo-to-Gattinara entry there. No. 225 (Sánchez, Venice, October 27) mentions reports from Burgo at Ferrara and instructing him to watch negotiations with the duke. It is a different letter; its historical context cannot be imported as this target's plaintext.
- Tomokiyo's live `spanish2.htm` returned 503. Checked the repository's previously retrieved `adrian1521/spanish2.htm` and `vasto1527/prior/spanish2C_now.htm` instead. They include Burgo in 1511 and numerous imperial ciphers, but no R9970 or matching 1527 letter/key was found. No claim of an exhaustive bibliography search.
- Searched the harvested DECODE record metadata for Burgo/Borgo, the shelfmark and Gattinara. R9970 was the only matching Burgo/shelfmark record; R9505 concerns Sánchez to Gattinara in 1522, not a demonstrated sibling.
- PARES exact-shelfmark search returned no extracted result. A direct request was rate limited; a later name search returned the site's explicit “Problema encontrado al realizar la búsqueda” page. These failures do not establish that the item is absent from PARES.
- The Galende Díaz PDF could not be retrieved for full inspection (connection closed / 502). Search-index text preserves the exact citation on p. 163. Whether another part of the article offers a plate or transcription remains unchecked; do not claim to have inspected the complete PDF.

## Follow-up source check, 2026-09-22

- Found the previously overlooked local article at `../esp318/lit/galende1994.pdf` (20 pages, printed pp. 159–178). Read the article text, visually verified the exact citation on p. 163, and inspected the appendix overview, pp. 167–177. The appendix contains seven cipher tables, not a plate or transcription of Burgo's letter; none is identified as a Burgo/Gattinara key. This supersedes the earlier PDF-access limitation above.
- The full title is *La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V*. Page 165, note 7, says the Simancas list drew partly on J. C. Carmona's *Tratado de Criptografía con aplicación especial al Ejército* (Madrid, 1894), without assigning the Burgo entry specifically to that source. This is a bibliographical lead, not a corrected shelfmark.
- Located a digitized Carmona link through Criptohistoria: `https://bdh-rd.bne.es/viewer.vm?id=0000238116&page=1`. Opening it returned HTTP 403; its contents have not been checked. No alternative matching reading emerged from exact-name/date/shelfmark searches.
- Independently re-inspected archive pages 1–3. The headings and financial-draft structure support the earlier identification warning. No authenticated ciphertext for the requested letter has emerged. The attempt is closed under the user's move-on instruction; resume on a corrected manuscript association, archive identification, or access to the older bibliographical source. This does not establish cryptographic impossibility.

## Recheck, 2026-09-23

- Reviewed the existing research and independently viewed all four retained scan previews. The two `al principe` headings, revisions, repeated financial opening and blank fourth surface support the source-identification warning. No newly authenticated Burgo/Gattinara ciphertext was found.
- Repeated web searches for the exact correspondents/date, shelfmark, and Carmona's 1894 treatise. No matching reading or corrected manuscript reference emerged in the returned results. The BNE viewer `https://bdh-rd.bne.es/viewer.vm?id=0000238116&page=1` again could not be opened by the web tool; this is an access limitation, not evidence about its contents.
- Move on under the renewed instruction. The named letter remains unread; excerpts from the attached financial drafts are not a partial decryption of that letter. Resume only with a corrected manuscript association or substantive new source evidence. No claim of cryptographic impossibility, and no solution page warranted.

## Image inventory

| DECODE file | Archive banner | Content observed |
|---|---|---|
| IMG_R9970_I46409_P2.jpg | AGS_EST_LEG_1563_0572_0001 | Shelfmark E.1563–572; `al principe`; first revised Spanish draft |
| IMG_R9970_I46409_P3.jpg | AGS_EST_LEG_1563_0572_0002 | End of first draft, then a second `al principe` draft with a repeated opening and amount |
| IMG_R9970_I46409_P1.jpg | AGS_EST_LEG_1563_0572_0003 | Continuation/end of second draft; no identified date or signature |
| IMG_R9970_I46409_P4.jpg | AGS_EST_LEG_1563_0572_0004 | Blank back with show-through |

The scans themselves carry the cited shelfmark, so this is not merely a filename typo. It remains unknown whether the error lies in the old citation, its interpretation, archive numbering, or the DECODE association. Do not silently substitute Charles V/Philip or a new year: neither is established here.

## Reading evidence

See `reading_evidence.md` for short, explicitly incomplete readings. These are **unciphered handwriting excerpts from the attached drafts**, not a partial decryption of the intended letter. Their role is to establish genre and test identity. A complete diplomatic edition of these unidentified drafts has not been made.

## Remaining gaps

- Burgo → Gattinara letter, Ferrara, 26 Oct 1527 - blocker: needs-physical-access; not on R9970, not itemised on PARES, not in CSP Spain III.2 or Tomokiyo; locating it needs the AGS inventory of Estado or Carmona 1894 (BNE, HTTP 403)
- the minute's year and the specific Fugger asiento - blocker: needs-physical-access; not on the leaves; needs Carande or the AGS Contaduría records
- full palaeographic edition of the two revised drafts - not a cipher gap; opening and key phrases read, the rest is heavily corrected clear text

## Escalation

- [x] siblings: searched harvested DECODE metadata; no matching Burgo sibling found. The live record lists zero associated records.
- [x] clear-pages: all four scans inspected; duplicate draft wording on archive pages 1–3, blank page 4; no separate decipherment.
- [x] known-keys: consulted cached imperial-cipher references; no confirmed ciphertext segment or securely identified correspondent on which to test a key. The numeral line is accounting notation.
- [x] print: exact-citation web searches and CSP Spain III.2 October 26–31 checked. Cached Galende Díaz article inspected in the follow-up, including the citation and appendix; no matching reading established. Carmona's BNE digitization returned HTTP 403.
- [n/a] key-rebuild: no authenticated ciphertext for the named target; guessing substitutions over clear handwriting would not be evidence.
- [n/a] retry: repeated amount checked against both draft versions at full resolution; archive search still needs external source verification.

## Sources and reproducibility

- DECODE R9970: https://de-crypt.org/decrypt-web/RecordsView/9970 (record and four scans retrieved; source HTML and images retained locally, git-ignored).
- Juan Carlos Galende Díaz, *La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V*, pp. 159–178, especially p. 163 and p. 165 n. 7: https://digibug.ugr.es/bitstream/handle/10481/30410/CEM-018-019-Art%C3%ADculo-009.pdf?sequence=1 . Cached PDF inspected in the follow-up at `../esp318/lit/galende1994.pdf`.
- CSP Spain III.2, pp. 432–449: https://www.british-history.ac.uk/cal-state-papers/spain/vol3/no2/pp432-449 . Local text: `sources/bho_oct26_31.txt`.
- Tomokiyo, *Ciphers during the Reign of Emperor Charles V*: https://cryptiana.web.fc2.com/code/spanish2.htm ; later archive additions: https://cryptiana.web.fc2.com/code/spanish2C.htm . Cached copies examined as specified above.
- `fetch_sources.py` retrieves the four record images without exposing the repository's shared session. `image_manifest.json` records file hashes and image ordering.

## Write-up

Written up 28 Sept 2026 as "not a cipher" (docs/burgo1527.html): the record's content is identified, the 1527
attribution disproved for these scans, and the DECODE correction queued. Before that (22–23 Sept) the folder was
kept as "no write-up" because the scans had not been identified.
