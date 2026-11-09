---
key: ontology-supplement-chebi-terms
identifiers:
  - CHEBI:64312
  - CHEBI:53289
  - CHEBI:3396
  - CHEBI:36005
  - CHEBI:143585
  - CHEBI:750271
  - CHEBI:18248
  - CHEBI:29034
  - CHEBI:758582
  - CHEBI:755635
  - https://www.ebi.ac.uk/ols4/
title: "EBI OLS4 ontology term lookup: CHEBI terms for CTE knowledge-base (ontology supplement)"
authors: "EMBL-EBI Ontology Lookup Service (OLS4) API, queried by retriever"
year: "2026"
journal: "Ontology Lookup Service (https://www.ebi.ac.uk/ols4/), ontology filter chebi"
url: https://www.ebi.ac.uk/ols4/api/search
source_url: https://www.ebi.ac.uk/ols4/api/search
sub_question: "ontology_supplement: IDs and labels for CHEBI terms named in the CTE disease knowledge-base template"
content: database record (verbatim fields)
---
title: "EBI OLS4 ontology term lookup: CHEBI terms for CTE knowledge-base (ontology supplement)"
authors: EMBL-EBI Ontology Lookup Service (OLS4) API, queried by retriever
year: 2026
journal: Ontology Lookup Service (https://www.ebi.ac.uk/ols4/), ontology filter chebi
identifiers: CHEBI:64312, CHEBI:53289, CHEBI:3396, CHEBI:36005, CHEBI:143585, CHEBI:750271, CHEBI:18248, CHEBI:29034, CHEBI:758582, CHEBI:755635, https://www.ebi.ac.uk/ols4/
url: https://www.ebi.ac.uk/ols4/api/search
sub_question: ontology_supplement: IDs and labels for CHEBI terms named in the CTE disease knowledge-base template

## Text
Queries: https://www.ebi.ac.uk/ols4/api/search?q=<term>&ontology=chebi&exact=true, then without exact=true when no exact label or synonym match was returned. Exact = a returned label or synonym equals the query (case-insensitive). Close = a returned label contains all query words but is not identical. None = no good match returned. Match type was assigned by the retriever from the API output.

ID | label | query | match type
--- | --- | --- | ---
CHEBI:64312 | memantine | memantine | exact
CHEBI:53289 | donepezil | donepezil | exact
CHEBI:3396 | Carbidopa-levodopa | levodopa | close
CHEBI:36005 | docosahexaenoic acid | docosahexaenoic acid | exact
CHEBI:143585 | cis-5,8,11,14,17-eicosapentaenoic acid methyl ester | eicosapentaenoic acid | close
CHEBI:750271 | florbetapir | florbetapir | exact
CHEBI:18248 | iron atom | iron atom | exact
CHEBI:29034 | iron(3+) | iron(3+) | exact
CHEBI:758582 | florquinitau | florquinitau | exact
— | — | MK-6240 | none
— | — | PI-2620 | none
CHEBI:755635 | flortaucipir | flortaucipir (MK-6240 not returned) | close

## Notes (retriever)
- eicosapentaenoic acid: methyl ester, not the free acid; treat with caution
