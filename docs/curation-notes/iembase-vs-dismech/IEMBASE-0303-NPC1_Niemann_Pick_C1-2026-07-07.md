# IEMbase 0303: NPC1-related Niemann-Pick disease type C1

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 303 |
| Nosology | 20.6.01.01 |
| Gene | NPC1 |
| External IDs | OMIM:257220; ORPHA:216981 |
| Generated mapping | MAPPED; `Niemann_Pick_Disease_Type_C.yaml#NPC1` |
| Candidate DisMech targets | `Niemann_Pick_Disease_Type_C.yaml#NPC1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents NPC1-related Niemann-Pick disease type C as a neurovisceral
lysosomal storage disorder. Characteristic rows include ataxia, behavioral
disorder, clumsiness, foam cells, gait disturbance, hepatosplenomegaly, language
difficulties, and sea-blue histiocytes. Additional clinical rows include action
dystonia, psychotic behavior, cognitive dysfunction, dysarthria, dystonia,
gelastic cataplexy, hemophagocytosis, cholestatic jaundice, hepatocellular
carcinoma or hepatoblastoma, oculomotor abnormalities, seizures, and vertical
gaze palsy.

The biochemical signal is diagnostic and storage-focused: markedly increased
plasma chitotriosidase, an abnormal filipin test row, and increased plasma
cholestane-3beta,5alpha,6beta-triol. Treatments in the cached record are
miglustat and intrathecal 2-hydroxypropyl-beta-cyclodextrin.

## DisMech phenotype coverage

`Niemann_Pick_Disease_Type_C.yaml` has explicit NPC1 and NPC2 subtypes, with
NPC1 as the correct generated target for this record. It covers the shared NPC
phenotype spectrum with vertical supranuclear gaze palsy, cerebellar ataxia,
dysarthria, dysphagia, progressive mental deterioration, dystonia, seizures,
gelastic cataplexy, hepatosplenomegaly, neonatal cholestasis, psychiatric
manifestations, hepatomegaly, splenomegaly, gait disturbance, jaundice,
progressive neurologic deterioration, bone-marrow foam cells, cognitive
impairment, dysphonia, and feeding difficulties.

Local biochemical coverage includes unesterified cholesterol accumulation,
plasma 24(S)-hydroxycholesterol, sphingosine accumulation, low cholesterol
esterification rate, and plasma phosphorylated-tau217. Treatments include
miglustat, intrathecal 2-hydroxypropyl-beta-cyclodextrin, levacetylleucine,
arimoclomol, supportive care, and genetic counseling.

## Concordance and completeness

Judgement: correct high-confidence subtype mapping to
`Niemann_Pick_Disease_Type_C.yaml#NPC1`.

Concordance is high for gene identity, NPC1 subtype placement, recessive NPC
biology, neurovisceral presentation, gaze palsy, ataxia, dystonia, seizures,
gelastic cataplexy, hepatosplenomegaly, cholestatic jaundice, foam-cell
pathology, cognitive/psychiatric involvement, and miglustat/HPbCD treatment
context. DisMech is richer for mechanism and for newer or broader treatment
coverage.

IEMbase adds review prompts for plasma chitotriosidase, plasma
cholestane-3beta,5alpha,6beta-triol, explicit filipin-test directionality,
language difficulty, hemophagocytosis, oculomotor abnormalities as a broader
row than vertical gaze palsy, sea-blue histiocytes, and the hepatocellular
carcinoma/hepatoblastoma row. The liver cancer row should be reviewed carefully
before import because it may represent rare complication or source-spectrum
noise rather than a core NPC1 phenotype.

## Curation actions

- Keep the generated NPC1 subtype mapping.
- Consider adding chitotriosidase and cholestane-triol diagnostic biomarkers if
  source-backed.
- Review filipin-test directionality before modeling it, since the cached row is
  not directly phrased as cholesterol accumulation.
- Treat hemophagocytosis, sea-blue histiocytes, and liver tumor rows as review
  prompts rather than automatic phenotype imports.
