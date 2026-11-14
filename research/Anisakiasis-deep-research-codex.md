# Anisakiasis: cached-source completeness pass

This is a local literature sweep produced from the full-text PubMed references already cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:20804423 | CID review of anisakidosis. Used for Anisakidae family scope, raw or undercooked seafood transmission, Japan/coastal Europe/United States geography, gastric mucosal invasion, allergic anisakidosis, endoscopic diagnosis and removal, anti-*A. simplex* IgE serology, surgical removal for intestinal or ectopic disease, occasional albendazole use, and freezing/cooking prevention context. |
| PMID:30058531 | Full-text Italian retrospective review. Used for the marine-mammal → krill → fish/squid life cycle, humans as accidental hosts, worldwide incidence, Japan annual cases, Italian source foods, gastric/intestinal/ectopic distributions, abdominal-pain frequency, eosinophilic-granuloma histopathology, IgE-mediated allergic presentations, no-definitive-medicinal-therapy caveat for albendazole, and surgical-treatment frequency. |
| PMID:24441579 | Full-text CT series of 20 gastric and 21 intestinal anisakiasis cases. Used for larval wall invasion, eosinophilic granuloma and abscess pathophysiology, severe submucosal edema, ascites frequency, and characteristic CT diagnosis. |
| PMID:10629469 | Gastroscopy-confirmed gastro-allergic anisakiasis cohort. Used for the acute allergic phenotype spectrum of urticaria, angioedema, bronchospasm, anaphylaxis, abdominal pain, nausea, vomiting, and diarrhea after fish ingestion. |
| PMID:31529811 | Gastro-allergic anisakiasis case report and literature review. Used for the direct tissue injury plus immediate IgE-mediated hypersensitivity framing and for endoscopic extraction as effective therapy. |
| PMID:40974456 | 2025 small-bowel perforation case report and review. Used narrowly for rare complicated intestinal perforation requiring surgical intervention. |

## Completeness cross-check

- Pathophysiology now separates viable third-stage larva ingestion, larval gastrointestinal mucosal invasion with severe edema, eosinophil-rich granulomatous inflammation, and Anisakis IgE-mediated immediate hypersensitivity.
- Eosinophil cell-type and eosinophil-migration GO annotations live on the eosinophilic-granuloma node, and that node now carries the eosinophilic granuloma or abscess evidence from PMID:24441579 plus the pathology warning from PMID:30058531.
- The IgE branch connects to urticaria, angioedema, bronchospasm, and anaphylaxis, matching the confirmed gastro-allergic cohort in PMID:10629469.
- All phenotype leaves in the entry are causally connected: abdominal pain from larval mucosal invasion and eosinophilic granulomatous inflammation; intestinal perforation from eosinophilic granulomatous inflammation; nausea, vomiting, diarrhea, and ascites from larval mucosal invasion; urticaria, angioedema, bronchospasm, and anaphylaxis from the IgE-mediated branch.
- The `histopathology:` block records eosinophilic granulomas of the digestive tract, mesentery, or peritoneum as the key microscopic lesion without forcing the exact HPO eosinophilic-granuloma term into a histopathology enum that does not admit it.
- Epidemiology now includes the global Orphanet-derived annual-incidence estimate, a Japan annual-cases row, and the narrow Italian literature-case count.
- Treatment now binds surgical removal to `NCIT:C15329` and represents albendazole as an occasional small-molecule pharmacotherapy with the no-definitive-medicinal-therapy caveat.
- The life-cycle host set now lists krill as the intermediate host rather than only carrying crustaceans in prose.

## Deferred or bounded items

- Freezing or cooking prevention is quotable from PMID:20804423 and the −18 °C for 96 h domestic-freezing rule is present in PMID:30058531, but the disease entry models post-exposure infection and therapy rather than kitchen controls upstream of viable-larva ingestion.
- Occupational sensitization was not modeled as transmission. The entry is for active anisakid larval infection after seafood ingestion; allergy after fish-handling exposure can occur without a live larva penetrating the gastrointestinal mucosa.
