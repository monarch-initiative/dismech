# IEMbase 0289: GALC-related Beta-galactosylceramidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 289 |
| Nosology | 20.1.08.02 |
| Gene | GALC |
| External IDs | OMIM:245200; ORPHA:206448 |
| Generated mapping | UNMAPPED; weak candidate `Krabbe_Disease.yaml` |
| Candidate DisMech targets | `Krabbe_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Krabbe disease / globoid cell leukodystrophy due to
GALC-related beta-galactosylceramidase deficiency. Inheritance is autosomal
recessive, treatability is unknown, and prevalence is listed as 1:100,000.

The clinical rows emphasize infantile neurologic disease: ataxia in later
onset rows, deafness, feeding difficulties, fever, irritability, neurologic
deterioration, neuropathy, seizures, and spasticity. Biochemical rows list
elevated CSF protein and increased serum lysogalactosylceramide. The treatment
section includes hematopoietic stem cell transplant.

## DisMech phenotype coverage

`Krabbe_Disease.yaml` is the correct local target despite the generated
UNMAPPED status. The local entry models GALC deficiency,
galactosylsphingosine/psychosine accumulation, oligodendrocyte and Schwann-cell
toxicity, demyelination, neuroinflammation, and the canonical psychosine
toxicity model, while also discussing psychosine-independent disease biology.

Local phenotypes include leukodystrophy, spasticity, peripheral neuropathy,
irritability in infancy, seizures, developmental regression, optic atrophy, and
feeding difficulties. Local biochemical entries include psychosine
(galactosylsphingosine) and GALC enzyme activity. Treatments include
hematopoietic stem cell transplantation, investigational gene therapy,
supportive care, avoidance of disease-accelerating agents, and investigational
substrate reduction.

## Concordance and completeness

Judgement: false negative mapping; resolve to `Krabbe_Disease.yaml`.

IEMbase and DisMech agree on GALC/Krabbe disease identity, autosomal recessive
inheritance, lysogalactosylceramide/psychosine biology, infantile irritability,
feeding difficulty, neurologic deterioration, neuropathy, seizures, spasticity,
and HSCT. DisMech is much richer mechanistically, especially for psychosine,
glial toxicity, demyelination, biomarker use, and investigational treatment
directions.

IEMbase adds review prompts for deafness, fever, ataxia in later-onset disease,
and elevated CSF protein. Its lysogalactosylceramide row is concordant with the
local psychosine biomarker and could be cross-named more explicitly if future
biochemical cleanup is done.

## Curation actions

- Resolve this record to `Krabbe_Disease.yaml`.
- Treat the generated weak candidate as the real target; the low score is a
  mapping miss.
- Review deafness, fever, ataxia, and CSF protein for possible local phenotype
  or biomarker enrichment.
