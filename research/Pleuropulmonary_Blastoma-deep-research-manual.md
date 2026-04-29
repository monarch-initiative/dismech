# Pleuropulmonary Blastoma Deep Research Notes

Date: 2026-04-12
Curator: Codex manual synthesis

## Scope

Disease: Pleuropulmonary blastoma (PPB)

Primary disease anchor:
- MONDO:0011014 `pleuropulmonary blastoma`

Cancer-modeling choices applied from dismech issue #1198:
- The dismech page is the disease-level mechanism graph for PPB, not a page per ontology child.
- `disease_term` stays MONDO-first.
- NCIT is added at disease mapping level and subtype mapping level for oncology grounding.
- Type I, Type Ir, Type II, and Type III are modeled as flat `histological` subtype facets inside one PPB entry.
- Type Ir is not split into its own disease file; it shares the same causal program and is represented as a subtype facet with NCIT grounding.
- No subtype is intended to imply a separate local page or "Not Yet Curated" debt.
- NCIT was preferred over MAXO only where it provided materially better oncology specificity, such as disease/subtype mapping and complete resection.
- MAXO remained appropriate for generic chemotherapy and radiation actions because NCIT did not provide an exact IVADo regimen term.

## Core Disease Summary

PPB is a rare pediatric intrathoracic mesenchymal malignancy that progresses along a cystic-to-solid continuum.

Key disease-defining points:
- Registry-scale natural history: PMID:25209242
  - "Pleuropulmonary blastoma (PPB) has 3 subtypes on a tumor progression pathway ranging from type I (cystic) to type II (cystic/solid) and type III (completely solid)."
  - "A germline mutation in DICER1 is the genetic cause in the majority of PPB cases."
- Familial predisposition discovery: PMID:19556464
  - "Here, we show that 11 multiplex PPB families harbor heterozygous germline mutations in DICER1..."
- Progressive tumor genomics: PMID:24909177
  - PPB cysts can "progress to high-grade sarcoma."
  - Tumors show compound DICER1 disruption plus frequent TP53 loss and occasional NRAS/BRAF mutation.

## Subtype Axis

Histologic subtype facet retained inside the single PPB entry:
- Type I
  - Purely cystic lesion with primitive small cells.
  - MONDO:0020555
  - NCIT:C45626
- Type Ir
  - Purely cystic lesion lacking primitive small cells.
  - No MONDO subtype located during curation.
  - NCIT:C211861
- Type II
  - Mixed cystic and solid PPB.
  - MONDO:0020556
  - NCIT:C45627
- Type III
  - Purely solid PPB.
  - MONDO:0020557
  - NCIT:C45628

Supporting subtype evidence:
- PMID:36541021
  - "Type I PPB is a purely cystic lesion that has a microscopic population of primitive small cells with or without rhabdomyoblastic features and may progress to type II or III PPB, whereas type Ir lacks primitive small cells."
- PMID:25209242
  - "Thirty-three percent of the 350 PPB cases were type I or type I regressed (type Ir), 35% were type II, and 32% were type III or type II/III."
  - "The median ages at diagnosis for type I, type II, and type III patients were 8, 35, and 41 months, respectively."

## Pathology and Natural History

Type I pathology:
- PMID:18223332
  - "Type I PPB is a delicate multilocular cyst with variable numbers of primitive mesenchymal cells beneath a benign epithelial surface."
  - "Rhabdomyoblasts and cartilage nodules are seen in 49% and 40% of cases, respectively."
  - "recognition of this lesion as a neoplasm with malignant potential rather than a developmental cystic malformation is vital..."

Progression and prognosis:
- PMID:25209242
  - "The 5-year overall survival (OS) rate for type I/Ir patients was 91%; all deaths in this group were due to progression to type II or III."
  - "Metastatic disease at the diagnosis of types II and III was also an independent unfavorable prognostic factor."
- PMID:36541021
  - "For young children with type I PPB, outcomes are favorable, but complete resection is indicated because of the risk for progression."

## Mechanism Synthesis

Atomic mechanism chain used in the YAML:

1. Germline DICER1 predisposition
- PMID:19556464
  - Heterozygous germline DICER1 mutations define familial PPB predisposition.

2. Compound DICER1 disruption
- PMID:24909177
  - Loss-of-function DICER1 allele plus somatic RNase IIIb missense mutation.

3. Aberrant 5p miRNA processing
- PMID:24909177
  - "5p-Derived microRNA (miRNA) transcripts retained abnormal precursor miRNA loop sequences normally removed by DICER1."

4. Epithelial FGF9 overexpression
- PMID:25978641
  - "FGF9 is overexpressed in lung epithelium in the initial multicystic stage of Type I PPB..."

5. Pulmonary mesenchymal hyperplasia
- PMID:25978641
  - Increased epithelial Fgf9 in mice "results in pulmonary mesenchymal hyperplasia and a multicystic architecture..."

6. TP53 loss
- PMID:24909177
  - Frequent biallelic TP53 loss is a recurrent cooperating lesion in progressive PPB.

7. RAS pathway activation
- PMID:24909177
  - NRAS or BRAF mutation occurs in some cases.

8. Sarcomatous progression
- PMID:24909177
  - PPB cysts can progress to high-grade sarcoma.
- PMID:25209242
  - Clinical registry data ties progression to worse survival.

Mechanistic interpretation:
- The key upstream distinction is between predisposition and lesion-level transformation.
- DICER1 is not modeled as a single bundled node; predisposition, second-hit disruption, miRNA processing failure, epithelial FGF9 dysregulation, and mesenchymal hyperplasia are split into separate causal steps.
- TP53 loss and RAS-pathway mutation are treated as additional cooperating progression lesions rather than as alternative root causes.

## Clinical Presentation

Useful phenotype-supporting references:
- PMID:16410110
  - "PPB must be included in the differential diagnosis of a fetus, neonate, or child with a cystic lung mass."
- PMID:37119756
  - "Clinical expression of PPB is nonspecific and variable. It ranges from a dry cough to respiratory distress."
- PMID:34345335
  - Type II case abstract includes fever, nonproductive cough, and dyspnea.
- PMID:32175165
  - Type III cases "presenting with pneumothorax" support that phenotype as a real but uncommon presentation.
- PMID:11002236
  - "Respiratory distress was the most common clinical symptom."

Phenotype terms selected for YAML:
- HP:0032445 `Pulmonary cyst`
- HP:0012735 `Cough`
- HP:0002094 `Dyspnea`
- HP:0002098 `Respiratory distress`
- HP:0002107 `Pneumothorax`

## Treatment Evidence

Surgery:
- PMID:33826235
  - "Complete tumor resection is a main prognostic factor..."
- PMID:36541021
  - Complete resection is indicated even in type I disease because of progression risk.

Chemotherapy:
- PMID:36137255
  - "Beginning in 2007, the IVADo regimen (ifosfamide, vincristine, actinomycin-D, and doxorubicin) was recommended..."
  - "Adjusted analyses suggest improved overall survival for children treated with IVADo..."

Radiotherapy:
- PMID:33826235
  - Chemotherapy and "in some cases radiotherapy" are included in multimodal treatment.

Modeling note:
- Exact NCIT regimen grounding for full IVADo was not available from the queried ontology results.
- The treatment entry therefore uses MAXO `chemotherapy` plus CHEBI agents rather than an inexact NCIT regimen approximation.

## Ontology Grounding Used

Disease and subtype grounding:
- MONDO:0011014 `pleuropulmonary blastoma`
- NCIT:C5669 `Pleuropulmonary Blastoma`
- MONDO:0020555 `pleuropulmonary blastoma type 1`
- MONDO:0020556 `pleuropulmonary blastoma type 2`
- MONDO:0020557 `pleuropulmonary blastoma type 3`
- NCIT:C45626 `Type I Pleuropulmonary Blastoma`
- NCIT:C211861 `Type Ir Pleuropulmonary Blastoma`
- NCIT:C45627 `Type II Pleuropulmonary Blastoma`
- NCIT:C45628 `Type III Pleuropulmonary Blastoma`

Representative histopathology terms:
- NCIT:C155651 `Primitive Mesenchymal Stroma Formation`
- NCIT:C35937 `Rhabdomyosarcomatous Differentiation`
- NCIT:C9118 `Sarcoma`

Representative biological process terms:
- GO:0035196 `miRNA processing`
- GO:0035195 `miRNA-mediated post-transcriptional gene silencing`
- GO:0008543 `fibroblast growth factor receptor signaling pathway`
- GO:0010463 `mesenchymal cell proliferation`
- GO:0030324 `lung development`

Representative anatomy and cell terms:
- CL:0000082 `epithelial cell of lung`
- CL:0008019 `mesenchymal cell`
- UBERON:0000115 `lung epithelium`
- UBERON:0004883 `lung mesenchyme`
- UBERON:0002048 `lung`

Representative gene terms:
- hgnc:17098 `DICER1`
- hgnc:3687 `FGF9`
- hgnc:11998 `TP53`
- hgnc:7989 `NRAS`
- hgnc:1097 `BRAF`

## References Used Directly in Curation

- PMID:11002236
- PMID:16410110
- PMID:18223332
- PMID:19556464
- PMID:24909177
- PMID:25209242
- PMID:25978641
- PMID:32175165
- PMID:33826235
- PMID:34345335
- PMID:36137255
- PMID:36541021
- PMID:37119756
- PMID:38671641
