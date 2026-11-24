# Build log

## Candidates

1. **Committee hearing** — Lawmakers can subpoena the cloud, regulate crypto, and summon AI to a hearing; ask them to turn the hearing's .docx into a PDF, and their only motion is to adjourn. **164 characters; 164 UTF-8 bytes**
2. **Save As dialog** — They draft rules for AI, crypto, and every corner of the internet, then stare down Word's “Save As” menu like it's the one bill they can't get through committee. **161 characters; 165 UTF-8 bytes**
3. **.docx vs .pdf** — The lawmakers who decide how AI, crypto, and the internet behave can pass a .docx full of rules, but converting it to PDF is where their authority becomes read-only. **165 characters; 165 UTF-8 bytes**
4. **Print to PDF** — They regulate AI, crypto, and the internet by the page, yet when the page is a .docx, “Print to PDF” is the one order their office can't enforce. **145 characters; 149 UTF-8 bytes**
5. **Wrong-format attachment** — Lawmakers can regulate every byte of the internet, but their constituent-facing AI rules arrive attached as FinalRules.docx—because apparently the PDF is still under negotiation. **178 characters; 180 UTF-8 bytes**
6. **Fax machine** — They write binding rules for AI, crypto, and the internet, then fax the unconverted .docx to the committee; at least one machine in the building still knows how to produce a page. **179 characters; 179 UTF-8 bytes**
7. **400-page bill** — They can draft a 400-page bill governing AI, crypto, and the internet, but if the file won't open as a PDF, the only thing in session is the loading wheel. **155 characters; 155 UTF-8 bytes**
8. **Amendment in Word** — They amend the rules for AI, crypto, and the internet in Word with solemn authority, then submit the amendment as .docx and call the missing PDF a bipartisan compromise. **169 characters; 169 UTF-8 bytes**
9. **The cloud** — They claim power over AI, crypto, and the internet, yet the moment a .pages file reaches the cloud, the cloud returns it untouched—apparently even technology has separation of powers. **183 characters; 185 UTF-8 bytes**
10. **final_FINAL_v2** — Lawmakers can regulate AI, crypto, and the internet, but after three rounds of edits the public gets final_FINAL_v2.docx, because “Export” remains outside their jurisdiction. **174 characters; 178 UTF-8 bytes**

## Pick

Candidate 1 is the entry. The hearing and subpoena establish lawmakers' authority, while the .docx-to-PDF failure undercuts it; “motion is to adjourn” is a clean legislative double meaning that leaves the punch on the final words.

## Verification

Ran `python3 main.py` twice, removing `/output/entry.txt` before each run. Both runs wrote byte-identical UTF-8 output with no trailing newline.

| Run | SHA-256 | Characters | Sentences |
|---|---|---:|---:|
| 1 | `253f70fdb0a34f860027698189ab6b10bd38384424144be1739719373876869d` | 164 | 1 |
| 2 | `253f70fdb0a34f860027698189ab6b10bd38384424144be1739719373876869d` | 164 | 1 |

Both outputs were valid UTF-8 and within the 1–320 character limit. All 10 candidates' character and UTF-8 byte counts were verified with Python 3.

## Tournament note (coordinator, 2026-11-24 ~17:00 WIB)
- 3 builders x 10-12 candidates = 32 lines total; 2 independent blind judges (Kilo-Pollinations + Copilot), Stage A per-criterion + Stage B pairwise (28 pairs x 2 orders each).
- Judge 1 top 3: C23 (0.864), C07 (0.664), C24 (0.650). Judge 2 top 3: C29 (0.7429), C26 (0.6429), C23 (0.6429). Combined top 3: C23 (0.7535), C29, C07.
- Revision round: top 3 revised (R23 140B, R29 164B, R07 158B), re-judged vs originals by both judges. Combined re-judge: X04/C29-original 0.605, X01/R29 0.570, X02/C07-original 0.490, X03/R23 0.490, X06/C23-original 0.435, X05/R07 0.410.
- WINNER: candidate #10 (C29), 178 bytes. LINE swapped from candidate #1 to candidate #10 by the coordinator after the blind tournament. Verified: 2 runs byte-identical, sha256 606b7b63632ecf8f. BACKUP: R29 (164 bytes).
