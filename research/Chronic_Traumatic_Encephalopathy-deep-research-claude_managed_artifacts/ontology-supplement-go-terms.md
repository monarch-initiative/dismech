---
key: ontology-supplement-go-terms
identifiers:
  - GO:0060856
  - GO:0035633
  - GO:0008017
  - GO:0031113
  - GO:0051402
  - GO:0043005
  - GO:0098883
  - GO:0006979
  - GO:0006879
  - GO:0060586
  - GO:0006954
  - GO:0001816
  - GO:0070098
  - GO:0014002
  - GO:0042552
  - GO:0140453
  - GO:0140454
  - https://www.ebi.ac.uk/ols4/
title: "EBI OLS4 ontology term lookup: GO terms for CTE knowledge-base (ontology supplement)"
authors: "EMBL-EBI Ontology Lookup Service (OLS4) API, queried by retriever"
year: "2026"
journal: "Ontology Lookup Service (https://www.ebi.ac.uk/ols4/), ontology filter go"
url: https://www.ebi.ac.uk/ols4/api/search
source_url: https://www.ebi.ac.uk/ols4/api/search
sub_question: "ontology_supplement: IDs and labels for GO terms named in the CTE disease knowledge-base template"
content: database record (verbatim fields)
---
title: "EBI OLS4 ontology term lookup: GO terms for CTE knowledge-base (ontology supplement)"
authors: EMBL-EBI Ontology Lookup Service (OLS4) API, queried by retriever
year: 2026
journal: Ontology Lookup Service (https://www.ebi.ac.uk/ols4/), ontology filter go
identifiers: GO:0060856, GO:0035633, GO:0008017, GO:0031113, GO:0051402, GO:0043005, GO:0098883, GO:0006979, GO:0006879, GO:0060586, GO:0006954, GO:0001816, GO:0070098, GO:0014002, GO:0042552, GO:0140453, GO:0140454, https://www.ebi.ac.uk/ols4/
url: https://www.ebi.ac.uk/ols4/api/search
sub_question: ontology_supplement: IDs and labels for GO terms named in the CTE disease knowledge-base template

## Text
Queries: https://www.ebi.ac.uk/ols4/api/search?q=<term>&ontology=go&exact=true, then without exact=true when no exact label or synonym match was returned. Exact = a returned label or synonym equals the query (case-insensitive). Close = a returned label contains all query words but is not identical. None = no good match returned. Match type was assigned by the retriever from the API output.

ID | label | query | match type
--- | --- | --- | ---
GO:0060856 | establishment of blood-brain barrier | establishment of blood-brain barrier | exact
GO:0035633 | maintenance of blood-brain barrier | maintenance of blood-brain barrier | exact
GO:0008017 | microtubule binding | microtubule binding | exact
GO:0031113 | regulation of microtubule polymerization | regulation of microtubule polymerization | exact
— | — | neuron death | none
GO:0043005 | neuron projection | neuron projection | exact
GO:0098883 | synapse pruning | synapse pruning | exact
— | — | synapse loss | none
GO:0006979 | response to oxidative stress | response to oxidative stress | exact
GO:0006879 | intracellular iron ion homeostasis | cellular iron ion homeostasis | close
GO:0006954 | inflammatory response | inflammatory response | exact
GO:0001816 | cytokine production | cytokine production | exact
GO:0070098 | chemokine-mediated signaling pathway | chemokine-mediated signaling pathway | exact
GO:0014002 | astrocyte development | astrocyte development | exact
— | — | axon degeneration | none
GO:0042552 | myelination | myelination | exact
GO:0140453 | protein aggregate center | protein aggregation (aggregat-label search) | close
GO:0140454 | protein aggregate center assembly | protein aggregation (aggregat-label search) | close

## Notes (retriever)
- neuron death: GO:0051402 neuron apoptotic process (returned)
- cellular iron ion homeostasis: GO:0060586 multicellular organismal-level iron ion homeostasis (returned)
