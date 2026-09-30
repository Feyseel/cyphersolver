# Charles I (Oxford) to Prince Rupert, 29 April 1645 — BL Add MS 18983 f. 14 — DECODE R4921 — NOTES

Status: read. Session 2026-09-21. Catalogue entry "King Charles I (Oxford) to Prince Rupert".

**Verdict: READ.** The cipher is the same system as the Henrietta Maria / Charles I key that George Lasry
reconstructed on DECODE as "TNA SP106-5" (on record R929, SP 106/10 f. 247, Jan 1646): a homophonic alphabet on
1–80 and a nomenclator of letter+digit groups (n1 = to, n3 = the, a1 = and, c5 = for, h1 = no, p6 = which ...).
Applied without change, it reads the King's letter at once. No decipherment was found in print. Warburton
(*Memoirs of Prince Rupert*, 1849, vol. 3) prints the Digby letters of 27 and 30 April on the same subject but not this one,
and neither Bromley (1787) nor a web search turned one up. DECODE marks the record Non-decrypted.

## Document

One page, holograph, clear opening and close, cipher in between (≈300 groups). "Duplicate" top right. The
endorsement on the dorse reads "From the King, Oxford Ap. 29 1645, Cypher". Transcription: `transcription.txt`
(from DECODE image IMG_R4921_I28579_P1; images git-ignored in `img/`).

## How it was found

1. The Richmond cipher of the sibling R4922 (31 July 1645, "This is in the D. of Richmond's Cypher", interlined)
   uses letter values above 100, which ours never does, so it was ruled out.
2. The Digby key R8724 (Digby–Walsingham) and the list of ciphers in Digby's papers (R8627) were checked: not this one.
3. R9116 (BL Add MS 32256 f. 5, "King Charles I to the Queen, Oxford 1642") is a period frequency tally in exactly
   this format (a1, d4, h3, k1, n5 ...). That pointed to the King–Queen family, and Lasry's SP106-5 key fitted.
4. A ciphertext-only homophonic anneal (`solve.py`, en-1640s) had earlier failed to converge (4 runs, no agreement).

## Reading (`reading.md`)

Groups 81–98 are not in the key. Most sit at phrase ends (nulls or stops). Two recur with meaning read from context:
95 = my, 98 = artillery. Letter+digit groups the key leaves open are read from context and marked [conj.].

> I very much like your opinion [61] for the present. Know [that] to [?]thow to follow it until I [211 186] enough to
> convoy, and draught [horses, 214] enough to transport my artillery to you; to which [end, c1] I have sent for
> Goring, who I hope (yet will not warrant) to be able to do both. But what [d4] can not [be done] if you do not
> [376] all our [148]s be in order: therefore I desire you to [march, 327] speedily for my assistance, that in case I
> can not bring my train of artillery to you, you [may] come and fetch it; assuring you that no time shall be lost,
> nor pains spared for doing of this, if it be possible, upon the word of your loving uncle.

Sense: the King, at Oxford and hemmed in by Cromwell's raids, cannot move his train (artillery) to Rupert without
horses and a convoy. He has sent for Goring and asks Rupert to march quickly to fetch it. This agrees with Digby's
letters of 27 and 30 April (Warburton iii 77–81) and with Rupert's march on Oxford in early May, which led to Naseby.

## Open

- Code groups 61, 211, 186, 214, 376, 148, 412 (412ant = warrant), 327, c1, d4, e4 (probably "if"), o1, 03, 05.
  Most are read from context only.
- A few letter slips: "eravght" (draught), "seaevgh" (…s enough), "thow". Either the King's slips or transcription.

## Corrections

- 30 Sept 2026: "you may come and fetch it" is now printed "you [may] come and fetch it". The check was prompted
  by an outside reading of the groups `68 4 | 75 86 93 11 44 26 3 e5 8 4 80 12 40 83 f2` with the key, which gives
  y-e-u [86][93] c-o-m-e IN f-e-t-c-h [83] IT. It was verified on the key (Lasry's SP106-5, R929) and on the
  image (`img/p1.jpg` in the rupert1645 worktree):
  - "you": 68 4 75 is y-e-u. The 4 stands at the torn right edge of the line, so it is probably 45 (o) with the 5
    lost.
  - "may": 86 and 93 are outside the key. Elsewhere they stand at phrase ends (86 after "to you", 93 after "I hope"),
    so "may" has no group and is supplied (the key's "may" is g3).
  - "and": the sign transcribed e5 (in) is not a cipher group. It is the King's clear "&", large and looped, the same
    form as in "friday & sonday" and "Oncle & most". His three other e5 groups (before "order", in "that in case",
    in "doing") are small "e5" with a flagged 5. `transcription.txt` now has "[&]" there, and `ciphertext.txt`
    drops the group: 304 tokens, 102 distinct.
  - The reading's "and" stands, as the King's own word. fraction_read is unchanged at 0.95 (289 of 304; 0.85 if
    groups 81-98 count unread).
