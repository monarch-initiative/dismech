# Pilocytic Astrocytoma Deep Research

## Modeling choices

- Curation unit: one disease-level dismech entry for the shared pilocytic astrocytoma mechanism graph, not separate pages for every MONDO/NCIT subclass.
- Disease anchor: `MONDO:0016691` pilocytic astrocytoma.
- Cancer mappings: retain disease-level NCIT mapping (`NCIT:C4047`) alongside the MONDO anchor.
- Subtypes are modeled as flat facet axes rather than new disease pages:
  - `Childhood` (`classification: age_group`) grounded to `MONDO:0004000` and `NCIT:C4048`
  - `Cerebellar` (`classification: anatomic_site`) grounded to `MONDO:0003168` and `NCIT:C6809`
  - `Pilomyxoid` (`classification: histology`) grounded to `MONDO:0016692` and `NCIT:C40315`
- Rationale: these refinements change age/site/histology framing and clinical behavior, but they do not justify splitting away from the core MAPK-driven pilocytic mechanism graph.

## Core disease facts

- `PMID:28448514`:
  - "Pilocytic astrocytoma (PA) is the most common pediatric brain tumor."
  - "A recurrent feature of PA is deregulation of the mitogen activated protein kinase (MAPK) pathway most often through KIAA1549-BRAF fusion, but also by other BRAF- or RAF1-gene fusions and point mutations (e.g. BRAFV600E)."
- `PMID:36786200`:
  - "Pilocytic astrocytoma (PA), a central nervous system (CNS) World Health Organization grade 1 tumor, is mainly seen in children or young adults aged 5-19."
- `PMID:16998597`:
  - "Pilocytic astrocytomas (PAs) are generally well circumscribed, slowly growing, cystic tumors, occurring in the pediatric age group."

## Pathophysiology

- Shared initiating program:
  - MAPK-pathway-activating lesions dominate disease biology; representative upstream lesion is `KIAA1549-BRAF`.
  - Genes used in the disease graph/genetics section: `BRAF`, `KIAA1549`, `NF1`, `RAF1`.
- Functional consequence:
  - `PMID:21636552`: "BRAF(V600E)-expressing cells subsequently stopped proliferating and induced markers of oncogene-induced senescence including acidic β-galactosidase, PAI-1, and p16(INK4a) whereas controls did not."
  - `PMID:21636552`: "Induction of senescence by BRAF may help explain the low-grade pathobiology of pilocytic astrocytoma"
- NF1 predisposition context:
  - `PMID:35945463`: "The first harbored biallelic NF1 inactivation only, occurred primarily during childhood, followed a more indolent clinical course, and had a unique epigenetic signature for which we propose the terminology "pilocytic astrocytoma, arising in the setting of NF1"."
  - This supports retaining NF1 in the genetics section and notes, not splitting a separate dismech page.
  - `PMID:38837168`: "the loss of the NF1 gene activates 3 distinct Ras effector pathways, including the PI3K/AKT/mTOR pathway, the MEK/ERK pathway, and the cAMP pathway, which mediate glioma tumorigenesis"
  - This supports adding explicit NF1-backed evidence to the MAPK-activation node, rather than relying only on BRAF/RAF1 evidence.

## Histopathology

- `PMID:16998597`:
  - "On histopathology, biphasic pattern (89.2%) along with Rosenthal fibers (66.7%) and eosinophilic granular bodies (60%) were present in the majority of cases."
- Ontology grounding chosen:
  - `NCIT:C35907` Biphasic Pattern
  - `NCIT:C41465` Rosenthal Fibers Present
  - `NCIT:C41463` Eosinophilic Granular Bodies Present

## Clinically important subtype/facet evidence

- Pilomyxoid histology:
  - `PMID:14683543`: "Hypothalamic/chiasmatic PMAs occurred in a significantly younger population and were associated with substantially shorter PFS and OS times than were typical PAs."
  - `PMID:14683543`: "Sixteen patients with PMAs (76%) experienced local recurrence, and three of those patients demonstrated evidence of cerebrospinal fluid dissemination."
- Cerebellar site:
  - `PMID:37021292`: "79 patients had hydrocephalus at diagnosis and 48% required preoperative treatment."
  - `PMID:16998597`: "demonstrated predilection for posterior fossa (61.7%)."
- Optic pathway / hypothalamic morbidity:
  - `PMID:38837168`: "OPGs in individuals with NF1 primarily affect the optic pathway and lead to visual disturbance."
  - `PMID:37033188`: "The main risks are to threaten vision loss by progressive tumor damage to optic pathways; furthermore, invasion of the hypothalamus can lead to diencephalic syndrome in infancy and hypopituitarism later in life."
  - Because this establishes association rather than a quantitative rate, hypopituitarism is modeled without a frequency band.

## Treatments

- Surgery:
  - `PMID:26351221`: "Surgical resection remains the first-line treatment with complete removal of the tumor the goal."
  - `PMID:37021292`: "Early treatment with the intention of GTR should be considered, opting, if this is not possible, to leave a tumor residue over neurological damage."
  - Chosen term: `NCIT:C131672` Gross Total Resection.
- Conventional chemotherapy:
  - `PMID:22665535`: "Previously untreated children younger than age 10 years with progressive or residual LGGs were eligible. Children were randomly assigned to receive carboplatin and vincristine (CV) or thioguanine, procarbazine, lomustine, and vincristine (TPCV)."
  - Chosen treatment grounding: `MAXO:0000647` chemotherapy with `CHEBI:31355` carboplatin and `CHEBI:28445` vincristine as therapeutic agents.
- MEK inhibition:
  - `PMID:40241281`: "Selumetinib provided stability and responses across many pLGG subgroups, and some patients achieved prolonged disease control without additional therapy."
  - `PMID:33631016`: "Selumetinib was tolerable and led to responses and prolonged disease stability in children with recurrent/progressive OPHGs based upon radiographic response, PFS, and visual outcomes."
- RAF inhibition:
  - `PMID:39412085`: "On 23 April 2024, the U.S. FDA approved a new type II RAF inhibitor, tovorafenib (OJEMDATM), previously known as DAY101, for the treatment of patients aged 6 months and older with relapsed or refractory (R/R) pLGG harboring a BRAF fusion or rearrangement, or BRAF V600E mutation."

## Term set used

- Disease:
  - `MONDO:0016691` pilocytic astrocytoma
  - `NCIT:C4047` Pilocytic Astrocytoma
- Subtypes:
  - `MONDO:0004000` childhood pilocytic astrocytoma / `NCIT:C4048`
  - `MONDO:0003168` cerebellar pilocytic astrocytoma / `NCIT:C6809`
  - `MONDO:0016692` pilomyxoid astrocytoma / `NCIT:C40315`
- Histopathology:
  - `NCIT:C35907` Biphasic Pattern
  - `NCIT:C41465` Rosenthal Fibers Present
  - `NCIT:C41463` Eosinophilic Granular Bodies Present
- Phenotypes:
  - `HP:0000238` Hydrocephalus
  - `HP:0000505` Visual impairment
  - `HP:0040075` Hypopituitarism
- Mechanisms:
  - `GO:0000165` MAPK cascade
  - `GO:0090398` cellular senescence
  - `GO:0008285` negative regulation of cell population proliferation
- Genetics:
  - `hgnc:1097` BRAF
  - `hgnc:22219` KIAA1549
  - `hgnc:9829` RAF1
  - `hgnc:7765` NF1
- Treatments:
  - `NCIT:C131672` Gross Total Resection
  - `MAXO:0000647` chemotherapy + `CHEBI:31355` carboplatin + `CHEBI:28445` vincristine
  - `NCIT:C93352` Targeted Therapy
  - `NCIT:C66939` Selumetinib
  - `NCIT:C106254` Tovorafenib
