# IEMbase 0304: NPC2-related Niemann-Pick disease type C2

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 304 |
| Nosology | 20.6.02.02 |
| Gene | NPC2 |
| External IDs | OMIM:607625; ORPHA:216981 |
| Generated mapping | MAPPED; `Niemann_Pick_Disease_Type_C.yaml#NPC2` |
| Candidate DisMech targets | `Niemann_Pick_Disease_Type_C.yaml#NPC2` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents NPC2-related Niemann-Pick disease type C with the same core
NPC neurovisceral signal as the NPC1 record: ataxia, behavioral disorder,
clumsiness, foam cells, hepatosplenomegaly, language difficulties, sea-blue
histiocytes, action dystonia, psychotic behavior, cognitive dysfunction,
dysarthria, dystonia, gait disturbance, gelastic cataplexy, hemophagocytosis,
cholestatic jaundice, oculomotor abnormalities, seizures, and vertical gaze
palsy.

Biochemical rows are the same diagnostic cluster seen in NPC1: markedly
increased plasma chitotriosidase, abnormal filipin testing, and increased
plasma cholestane-3beta,5alpha,6beta-triol. Miglustat is the only treatment
listed in the cached IEMbase record.

## DisMech phenotype coverage

`Niemann_Pick_Disease_Type_C.yaml` explicitly distinguishes NPC2 from NPC1 in
`has_subtypes`, `genetic`, and subtype term mappings. The file models the
shared NPC phenotype spectrum, including vertical supranuclear gaze palsy,
ataxia, dysarthria, dysphagia, progressive mental deterioration, dystonia,
seizures, gelastic cataplexy, hepatosplenomegaly, neonatal cholestasis,
psychiatric manifestations, hepatomegaly, splenomegaly, gait disturbance,
jaundice, progressive neurologic deterioration, bone-marrow foam cells,
cognitive impairment, dysphonia, and feeding difficulties.

Biochemical coverage includes unesterified cholesterol accumulation, plasma
24(S)-hydroxycholesterol, sphingosine accumulation, low cholesterol
esterification rate, and plasma phosphorylated-tau217. Treatment coverage is
broader than IEMbase, with miglustat, intrathecal cyclodextrin, levacetylleucine,
arimoclomol, supportive care, and genetic counseling.

## Concordance and completeness

Judgement: correct high-confidence subtype mapping to
`Niemann_Pick_Disease_Type_C.yaml#NPC2`.

The local entry covers the important disease identity, gene split, shared NPC
mechanism, and most clinical phenotypes. IEMbase is more granular for diagnostic
lab rows and for some clinical rows that are only implicit or absent locally:
plasma chitotriosidase, cholestane-triol, filipin test, language difficulties,
hemophagocytosis, sea-blue histiocytes, and broad oculomotor abnormalities.

Treatment concordance is strong for miglustat. IEMbase does not list
intrathecal cyclodextrin for NPC2, so the local HPbCD coverage should remain a
general NPC treatment entry unless future curation adds subtype-specific
treatment applicability.

## Curation actions

- Keep the generated NPC2 subtype mapping.
- Add NPC diagnostic biomarker prompts for chitotriosidase and
  cholestane-triol if source evidence supports them.
- Review whether filipin testing should be modeled as an abnormal diagnostic
  assay rather than as a simple decreased/increased marker.
- Avoid inferring NPC2-specific HPbCD treatment from the IEMbase record.
