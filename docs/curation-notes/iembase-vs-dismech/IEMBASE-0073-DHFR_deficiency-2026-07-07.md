# IEMbase 0073: DHFR-related dihydrofolate reductase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 73 |
| Nosology | 21.8.05.01 |
| Gene | DHFR |
| External IDs | OMIM:126060 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Best fuzzy candidate `Tetrahydrobiopterin_Deficiency.yaml#DHPR Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive DHFR-related dihydrofolate
reductase deficiency, with alternate labels megaloblastic anemia due to DHFR
deficiency and DHFRD. Treatability is marked yes.

The characteristic biochemical signal includes abnormal CSF
5-methyltetrahydrofolic acid, abnormal plasma folate, abnormal blood
hemoglobin, and abnormal plasma LDH. Additional rows include urinary FIGLU,
plasma homocysteine, urinary methylmalonic acid, urinary orotic acid, CSF BH4,
and CSF biogenic amine metabolites.

Characteristic clinical rows include megaloblastic anemia and delayed
myelination. Additional clinical rows include ataxia, cerebral atrophy on MRI,
epilepsy, abnormal eye movements, failure to thrive, microcephaly, oculogyric
crisis, and pancytopenia. The treatment row is folinic acid.

## DisMech phenotype coverage

No valid local DisMech target was found for DHFR-related human dihydrofolate
reductase deficiency.

The best fuzzy candidate, `Tetrahydrobiopterin_Deficiency.yaml#DHPR Deficiency`,
is a false positive. DHPR deficiency is QDPR-related dihydropteridine reductase
deficiency in BH4 regeneration. DHFR deficiency is a distinct folate-cycle
enzyme defect. The local bacterial folate-synthesis module and antimicrobial
entries that mention DHFR are drug-mechanism contexts, not human DHFR deficiency.

## Concordance and completeness

Judgement: true local gap.

This is a treatable folate-metabolism disorder with a hematologic and
neurodevelopmental phenotype. It should not be mapped to DHPR/QDPR deficiency
or to antimicrobial DHFR target modules, despite the close acronyms and folate
terminology.

## Curation actions

- Keep this IEMbase record unmapped for now.
- Add a future standalone DHFR deficiency entry.
- If curated later, prioritize folate-cycle enzyme deficiency, megaloblastic
  anemia/pancytopenia, CSF 5-MTHF and folate markers, delayed myelination and
  epilepsy, and folinic-acid treatment.
