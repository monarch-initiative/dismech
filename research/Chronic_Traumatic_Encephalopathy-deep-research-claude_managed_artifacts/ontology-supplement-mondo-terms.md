---
key: ontology-supplement-mondo-terms
identifiers:
  - MONDO:0004976
  - MONDO:0007488
  - MONDO:0019037
  - HP:0001300
  - MONDO:0005180
  - MONDO:0024257
  - MONDO:0020129
  - MONDO:0043264
  - MONDO:0001627
  - MONDO:0043512
  - MONDO:0019976
  - https://www.ebi.ac.uk/ols4/
title: "EBI OLS4 ontology term lookup: MONDO terms for CTE knowledge-base (ontology supplement)"
authors: "EMBL-EBI Ontology Lookup Service (OLS4) API, queried by retriever"
year: "2026"
journal: "Ontology Lookup Service (https://www.ebi.ac.uk/ols4/), ontology filter mondo"
url: https://www.ebi.ac.uk/ols4/api/search
source_url: https://www.ebi.ac.uk/ols4/api/search
sub_question: "ontology_supplement: IDs and labels for MONDO terms named in the CTE disease knowledge-base template"
content: database record (verbatim fields)
---
title: "EBI OLS4 ontology term lookup: MONDO terms for CTE knowledge-base (ontology supplement)"
authors: EMBL-EBI Ontology Lookup Service (OLS4) API, queried by retriever
year: 2026
journal: Ontology Lookup Service (https://www.ebi.ac.uk/ols4/), ontology filter mondo
identifiers: MONDO:0004976, MONDO:0007488, MONDO:0019037, HP:0001300, MONDO:0005180, MONDO:0024257, MONDO:0020129, MONDO:0043264, MONDO:0001627, MONDO:0043512, MONDO:0019976, https://www.ebi.ac.uk/ols4/
url: https://www.ebi.ac.uk/ols4/api/search
sub_question: ontology_supplement: IDs and labels for MONDO terms named in the CTE disease knowledge-base template

## Text
Queries: https://www.ebi.ac.uk/ols4/api/search?q=<term>&ontology=mondo&exact=true, then without exact=true when no exact label or synonym match was returned. Exact = a returned label or synonym equals the query (case-insensitive). Close = a returned label contains all query words but is not identical. None = no good match returned. Match type was assigned by the retriever from the API output.

ID | label | query | match type
--- | --- | --- | ---
MONDO:0004976 | amyotrophic lateral sclerosis | amyotrophic lateral sclerosis | exact
MONDO:0007488 | Lewy body dementia | Lewy body dementia | exact
— | — | primary age-related tauopathy | none
MONDO:0019037 | progressive supranuclear palsy | progressive supranuclear palsy | exact
HP:0001300 | Parkinsonism | parkinsonism | exact
MONDO:0005180 | Parkinson disease | Parkinson disease | exact
— | — | motor neuron disease | none
— | — | concussion | none
— | — | brain concussion | none
MONDO:0001627 | dementia | dementia | exact
MONDO:0043512 | traumatic encephalopathy | traumatic encephalopathy | exact
MONDO:0019976 | chronic traumatic encephalopathy | chronic traumatic encephalopathy | exact

## Notes (retriever)
- parkinsonism: returned by MONDO-filtered search; the ID prefix is HP
- motor neuron disease: MONDO:0024257 hereditary motor neuron disease (returned, narrower)
- motor neuron disease: MONDO:0020129 acquired motor neuron disease (returned, narrower)
- concussion: MONDO:0043264 post-traumatic epilepsy (returned, different concept)
