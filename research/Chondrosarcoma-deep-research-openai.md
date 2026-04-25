# Chondrosarcoma Deep Research Notes

## Scope

- Target disease file: `kb/disorders/Chondrosarcoma.yaml`
- Disease anchor: `MONDO:0008977` chondrosarcoma
- Curation objective: one disease-level cancer mechanism graph for chondrosarcoma, with subtype facets grounded to ontology terms where available

## Modeling Decisions Applied From Issue #1198

- The dismech entry is the mechanism-graph unit, so this curation stays in a single `Chondrosarcoma.yaml` file rather than splitting conventional, dedifferentiated, mesenchymal, clear cell, periosteal, primary central, or secondary peripheral disease into separate pages.
- `disease_term` is MONDO-first: `MONDO:0008977` is the graph anchor.
- `subtype_term` is used only where MONDO offers the relevant subclass:
  - `MONDO:0005013` dedifferentiated chondrosarcoma
  - `MONDO:0006853` mesenchymal chondrosarcoma
  - `MONDO:0003684` clear cell chondrosarcoma
  - `MONDO:0003680` periosteal chondrosarcoma
- Subtypes are modeled as flat facet axes rather than as separate disease pages:
  - Histology: Conventional, Dedifferentiated, Mesenchymal, Clear Cell
  - Surface origin: Periosteal
  - Tumor origin / predisposition context: Primary Central, Secondary Peripheral
- NCIT was added routinely where the current schema can represent oncology specificity:
  - Disease/subtype-level grounding through `histopathology.finding_term`
  - Treatment grounding through `treatment_term`
- The current schema does not expose a disease-level or subtype-level `ncit_mappings` slot. Because of that schema constraint, NCIT specificity was carried in histopathology and treatment sections instead of an impossible direct mapping block.
- MAXO was not used for the core oncology interventions because NCIT provides materially better cancer-specific granularity here (`Definitive Surgical Resection`, `En Bloc Resection`, `Chemotherapy`, `Targeted Therapy`).

## Subtype Grounding Chosen For The Disease Slice

| Facet role | Dismech subtype | MONDO grounding | NCIT grounding used in file | Rationale |
| --- | --- | --- | --- | --- |
| Histology | Conventional | none exact used | general disease NCIT plus primary central context | common dominant pattern; kept as a facet, not a page |
| Histology | Dedifferentiated | `MONDO:0005013` | `NCIT:C6476` | distinct aggressive histology, but still inside one chondrosarcoma graph |
| Histology | Mesenchymal | `MONDO:0006853` | `NCIT:C3737` | distinct fusion-driven program; modeled with subtype-specific mechanism node |
| Histology | Clear Cell | `MONDO:0003684` | `NCIT:C6475` | low-grade epiphyseal subtype with distinctive morphology |
| Surface origin | Periosteal | `MONDO:0003680` | `NCIT:C7357` | rare surface-based subtype recognized in review literature |
| Tumor origin | Primary Central | none exact used | `NCIT:C7155` | common medullary conventional presentation; recurrent IDH program |
| Predisposition context | Secondary Peripheral | none exact used | `NCIT:C121882` | malignant transformation from osteochondroma / EXT predisposition |

## Mechanism Selection Rationale

The mechanism nodes were kept atomic rather than bundled:

1. `IDH1/IDH2 Neomorphic Enzyme Activity`
2. `D-2-Hydroxyglutarate Accumulation`
3. `IDH-Linked DNA Methylation Dysregulation`
4. `COL2A1 Matrix Gene Disruption`
5. `TP53 Dysfunction`
6. `Cell Cycle Activation`
7. `HEY1::NCOA2 Fusion Oncogenic Program`
8. `EXT1/EXT2 Heparan Sulfate Polymerization Failure`
9. `Secondary Peripheral Malignant Transformation`

This structure preserves causal order:

- mutant IDH enzymes -> 2-HG accumulation -> methylation dysregulation
- TP53 dysfunction -> proliferative progression / cell cycle activation
- EXT-associated heparan sulfate failure -> osteochondroma predisposition -> malignant peripheral transformation

## Key PMID Evidence Used

### Disease definition and subtype structure

- `PMID:34742483`
  - Quote: `Chondrosarcomas are heterogeneous matrix-producing cartilaginous neoplasms with variable clinical behavior.`
  - Quote: `Subtypes include conventional (75%), dedifferentiated (10%), clear cell (2%), mesenchymal (2%), and periosteal chondrosarcoma (<1%).`
  - Use: disease-level description and flat histologic subtype axis

### Primary central disease and IDH biology

- `PMID:30296521`
  - Quote: `Central conventional chondrosarcoma is the most common subtype and is associated with isocitrate dehydrogenase 1 and 2 (IDH1 and IDH2) gene mutations in 50% to 60% of cases.`
  - Use: `Primary Central` subtype plus `IDH1/IDH2 Neomorphic Enzyme Activity`

- `PMID:32208957`
  - Quote: `Mutations in the isocitrate dehydrogenase 1/2 (IDH1/2) enzymes occur in up to 65% of chondrosarcomas, resulting in accumulation of the oncometabolite D-2-hydroxyglutarate (2-HG).`
  - Quote: `Plasma 2-HG levels decreased substantially in all patients (range, 14%-94.2%), to levels seen in healthy individuals.`
  - Quote: `In patients with chondrosarcoma, ivosidenib showed minimal toxicity, substantial 2-HG reduction, and durable disease control.`
  - Use: IDH metabolic node chain plus targeted therapy

- `PMID:31604924`
  - Quote: `Here we use multi-omics molecular profiles from a series of cartilage tumors and find an mRNA classification that identifies two subtypes of chondrosarcomas defined by a balance in tumor differentiation and cell cycle activation.`
  - Quote: `Finally, DNA methylation is associated with IDH mutations.`
  - Use: cell-cycle and methylation nodes

### Matrix disruption and aggressive progression

- `PMID:23770606`
  - Quote: `We identified hypermutability of the major cartilage collagen gene COL2A1, with insertions, deletions and rearrangements identified in 37% of cases.`
  - Quote: `The patterns of mutation were consistent with selection for variants likely to impair normal collagen biosynthesis.`
  - Use: `COL2A1 Matrix Gene Disruption`

- `PMID:37747813`
  - Quote: `TP53 mutation was the next most prevalent (41.9%) and is associated with worse overall survival and metastasis-free survival in both univariate and multivariate analyses.`
  - Use: `TP53 Dysfunction`

- `PMID:41391500`
  - Quote: `Preclinical research and analyses of patient tumor samples have identified several molecular mechanisms driving chondrosarcoma development and progression, including mutations in isocitrate dehydrogenases types 1 and 2 (IDH1/2) and TP53, hyperactivation of protumorigenic signaling pathways, and programmed cell death ligand 1 (PD-L1) expression.`
  - Quote: `Wide surgical resection remains the standard treatment for localized disease and can be curative; however, effective therapies for unresectable or metastatic chondrosarcoma are needed.`
  - Use: disease overview, TP53 context, definitive surgery

### Mesenchymal subtype

- `PMID:35672279`
  - Quote: `Mesenchymal chondrosarcoma (MCS) is a rare translocation-associated sarcoma, driven by a canonical HEY1::NCOA2 fusion.`
  - Quote: `The tumors typically have a biphasic phenotype of primitive small blue round cells intermixed with hyaline cartilage.`
  - Use: mesenchymal subtype grounding plus fusion-driven mechanism

### Clear cell subtype

- `PMID:37805864`
  - Quote: `Clear cell chondrosarcoma (CCC), an extremely rare primary bone tumor, is currently classified by the World Health Organization as a low-grade malignant cartilaginous neoplasm.`
  - Quote: `Unlike conventional chondrosarcoma, CCC has a predilection for the epiphysis of long bones and often displays radiologic features reminiscent of chondroblastoma.`
  - Quote: `Histologically, the process is characterized by infiltrative lobules and sheets of round to oval cells with abundant cleared cytoplasm and well-defined cell borders associated with trabecula of osteoid and woven bone, scattered osteoclasts, and foci of conventional low-grade chondrosarcoma in about one-half of cases.`
  - Quote: `The recommended treatment is wide operative resection.`
  - Use: clear cell subtype grounding, morphology, surgery context

### Secondary peripheral transformation and EXT biology

- `PMID:18271966`
  - Quote: `The most important complication is malignant transformation of osteochondroma towards secondary peripheral chondrosarcoma, which is estimated to occur in 0.5-5%.`
  - Quote: `In almost 90% of MO patients germline mutations in the tumour suppressor genes EXT1 or EXT2 are found.`
  - Quote: `The EXT genes encode glycosyltransferases, catalyzing heparan sulphate polymerization.`
  - Quote: `For secondary peripheral chondrosarcoma, en-bloc resection of the lesion and its pseudocapsule with tumour-free margins, preferably in a bone tumour referral centre, should be performed.`
  - Use: `Secondary Peripheral` facet, EXT mechanism, malignant transformation node, and subtype-specific surgery

### Dedifferentiated subtype and clinical phenotype

- `PMID:34734747`
  - Quote: `Dedifferentiated chondrosarcomas are aggressive variants of chondrosarcoma, associated with poor outcomes.`
  - Quote: `Tumor biphasism is the norm.`
  - Quote: `Radiologically, large soft tissue masses with bony destruction predominate.`
  - Quote: `Surgical resection forms the standard of care for localized disease.`
  - Quote: `These rare tumors affect middle-aged individuals and present with pain and swelling in the affected site.`
  - Use: dedifferentiated subtype grounding, soft tissue mass phenotype, pain phenotype, surgery

### Systemic therapy heterogeneity

- `PMID:30082492`
  - Quote: `Patients diagnosed with mesenchymal chondrosarcoma were all treated with multidrug chemotherapy, and the mean PFS was 6.7 months.`
  - Quote: `Prospective studies need to be conducted based on preclinical work to develop a uniform regimen to treat advanced chondrosarcoma patients according to the diagnosed subtype and improve survival.`
  - Use: subtype-dependent chemotherapy context

## Open Limits / Known Constraints

- The current schema cannot express direct NCIT mappings on `disease_term` or `subtype_term`, so those oncology mappings were represented indirectly through histopathology and treatment slots.
- Conventional, primary central, and secondary peripheral classifications overlap in real tumors. They were kept as flat facets instead of nested subtype pages to avoid falsely implying separate mechanism graphs.
- No separate disease files were created for dedifferentiated, mesenchymal, clear cell, or periosteal variants because the curation target for issue `#1204` is the disease-level chondrosarcoma slice, with subtype-specific mechanisms embedded inside one graph.
