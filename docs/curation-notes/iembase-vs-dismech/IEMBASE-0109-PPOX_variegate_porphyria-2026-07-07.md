# IEMbase 0109: PPOX-related protoporphyrinogen oxidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 109 |
| Nosology | 17.1.09.01 |
| Gene | PPOX |
| External IDs | OMIM:176200 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Inherited_Porphyria.yaml#Variegate Porphyria` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as PPOX-related protoporphyrinogen oxidase deficiency,
with alternate labels porphyria variegata, South African porphyria, and PV.
Treatability is marked yes, but the cached JSON has no treatment rows.

The biochemical rows are increased urinary delta-ALA, increased stool
coproporphyrin III, increased urinary porphobilinogen, increased urinary total
porphyrins, increased stool protoporphyrin, low-to-normal plasma magnesium, and
decreased plasma sodium.

Clinical rows include psychotic behavior, blisters, coma, constipation,
hepatopathy, hyperesthesia, hypertension, hepatocellular carcinoma or
hepatoblastoma, motor neuropathy, nausea, renal failure, seizures, tachycardia,
and vomiting.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. `Inherited_Porphyria.yaml`
has a `Variegate Porphyria` subtype with PPOX loss-of-function variants,
autosomal dominant acute hepatic porphyria context, neurovisceral attack
susceptibility, cutaneous photosensitivity, and shared acute hepatic porphyria
biomarkers including urinary ALA and porphobilinogen.

The local entry covers acute hepatic porphyria features such as abdominal pain,
vomiting, peripheral neuropathy, and cutaneous photosensitivity at group/subtype
level. It also includes hemin and givosiran treatment context for acute hepatic
porphyrias, though not a variegate-porphyria-specific treatment section.

## Concordance and completeness

Judgement: false negative to existing subtype-level local coverage.

DisMech is stronger for pathway mechanism, PPOX gene anchoring, acute hepatic
porphyria modeling, and group-level treatment rationale. IEMbase is more
granular for variegate-porphyria-specific biochemical compartments and clinical
attack details, including stool coproporphyrin III/protoporphyrin, low sodium,
autonomic cardiovascular rows, neuropsychiatric rows, renal failure, and
hepatopathy/tumor rows.

## Curation actions

- Resolve to `Inherited_Porphyria.yaml#Variegate Porphyria` as the current
  canonical target.
- Consider a future standalone variegate porphyria entry if porphyria subtype
  curation is split from the umbrella.
- Review IEMbase-specific VP biomarkers and acute-attack phenotypes for future
  expansion, especially stool porphyrin pattern and hyponatremia/renal
  involvement.
