Title: Request for new term Chlamydia pneumoniae pneumonia
Template: Add new term (generic)

### Label

Chlamydia pneumoniae pneumonia

### Synonyms

Chlamydophila pneumoniae pneumonia, TWAR pneumonia

### Synonym type

exact

### Definition

A pneumonia caused by the obligate intracellular bacterium Chlamydia pneumoniae. [PMID:2181028, PMID:15895932]

### Parent term

MONDO:0025598 pneumonia caused by chlamydia (see the problem described below)

### Children term(s)

None proposed.

### ORCID Identifier

https://orcid.org/0000-0001-5705-7831

### Website URL

https://github.com/monarch-initiative/dismech/blob/main/kb/disorders/Chlamydia_Pneumoniae_Pneumonia.yaml

### Additional comments

**Why this term is needed.** **There is a problem with the proposed parent.** `MONDO:0025598` is a subclass of `MONDO:0005701` chlamydia trachomatis infectious disease, so a child placed there would wrongly inherit a *C. trachomatis* parent. Its ICD-10-CM cross-reference, `J16.0`, is a genus-level code. I think `MONDO:0005701` should be replaced by `MONDO:0021697` chlamydia infectious disease on that term, and I can file that separately if you prefer.

**Evidence that the concept exists.**

- *C. pneumoniae* strain TWAR is described as a common cause of pneumonia and other acute respiratory tract infections (PMID:2181028).

**Similar terms already in Mondo.**

- `MONDO:0005867` Mycoplasma pneumoniae pneumonia
- `MONDO:0005824` Legionnaires' disease

**Search.** No matching label, synonym or cross-reference in Mondo release 2026-11-03, and no matching open or closed issue.

**Context.** Requested from curation of the [dismech](https://github.com/monarch-initiative/dismech) knowledge base, where `Chlamydia_Pneumoniae_Pneumonia` currently has no `disease_term`.
