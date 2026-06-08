| Constraint | Symptom | Effect on requested report | Workaround |
|---|---|---|---|
| No papers retrieved | `paper_search` returned zero retrievable papers; no citable context IDs were created | Prevents PMID-cited claims, abstract quotes, URLs, dates, and evidence-backed disease synthesis | Provide retrievable PMIDs, DOIs, PDFs, or direct links for core EDN3/EDNRB Waardenburg–Shah sources |
| OpenTargets failure | `open_targets_search` failed after retries | No disease-target association evidence available for genetics/mechanism sections | Re-run with working OpenTargets access or supply equivalent curated disease-target sources |
| Answer tool requires contexts | Grounded submission is blocked when no citable contexts exist | Final cited report cannot be generated/submitted in this run | Seed the workspace with at least one authoritative retrievable source (e.g., OMIM, Orphanet, GeneReviews, PubMed paper) before synthesis |


*Table: This table summarizes the main system-level constraints encountered during the session, how each blocked the requested EDN3/EDNRB Waardenburg–Shah report, and the most direct workaround for a successful follow-up run.*
