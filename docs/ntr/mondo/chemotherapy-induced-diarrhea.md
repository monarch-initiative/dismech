Title: Request for new term chemotherapy-induced diarrhea
Template: Add new term (generic)

### Label

chemotherapy-induced diarrhea

### Synonyms

chemotherapy-induced diarrhoea

### Synonym type

exact

### Definition

Diarrhea caused by cancer chemotherapy, especially fluoropyrimidines and irinotecan. It is associated with histological changes and inflammation of the intestinal mucosa arising from stem-cell apoptosis and disturbed cellular renewal, and it causes notable morbidity and mortality. [PMID:25186048, PMID:30739515, PMID:32170007, PMID:34017262]

### Parent term

MONDO:0800390 chemotherapy-induced toxicity; MONDO:0001673 diarrheal disease

### Children term(s)

None proposed.

### ORCID Identifier

https://orcid.org/0000-0001-5705-7831

### Website URL

https://github.com/monarch-initiative/dismech/blob/main/kb/disorders/Chemotherapy_Induced_Diarrhea.yaml

### Additional comments

**Why this term is needed.** Without this class, a resource must use `MONDO:0001673` diarrheal disease, which is misleading in practice. That class has inherited congenital diarrheas among its descendants, and dismech's earlier use of it led a knowledge-graph comparison to propose six of them as subtypes of a drug toxicity. These existing terms are classified under their organ-level disease rather than under `MONDO:0800390` chemotherapy-induced toxicity, so you may wish to review that branch.

**Evidence that the concept exists.**

- Management guidance describes it as common and inconsistently managed (PMID:25186048).
- Drug-specific mechanisms: irinotecan and bacterial β-glucuronidase (PMID:32170007); pharmacogenetic risk from UGT1A1*28 (PMID:11990381).

**Similar terms already in Mondo.**

- `MONDO:0005483` chemotherapy-induced alopecia
- `MONDO:0005588` chemotherapy-induced oral mucositis
- `MONDO:0100641` chemotherapy-induced neuropathy
- `MONDO:0005585` chemotherapy-induced hypertension
- `MONDO:0027675` irinotecan toxicity

**Search.** No matching label, synonym or cross-reference in Mondo release 2026-11-03, and no matching open or closed issue.

**Context.** Requested from curation of the [dismech](https://github.com/monarch-initiative/dismech) knowledge base, where `Chemotherapy_Induced_Diarrhea` currently has no `disease_term`.
