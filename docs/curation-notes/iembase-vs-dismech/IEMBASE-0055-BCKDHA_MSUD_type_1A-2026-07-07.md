# IEMbase 0055: BCKDHA-related MSUD type 1A

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 55 |
| Nosology | 1.3.02.01 |
| Gene | BCKDHA |
| External IDs | OMIM:248600 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Maple_Syrup_Urine_Disease.yaml` |
| Candidate DisMech targets | `Maple_Syrup_Urine_Disease.yaml#Type IA` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive BCKDHA-related branched-chain
ketoacid dehydrogenase E1-alpha deficiency, with alternate labels "Maple syrup
urine disease type 1a" and "MSUD". Treatability is marked yes and the listed
prevalence is 1:200,000 in Europe.

The biochemical signal is the expected MSUD intoxication profile: high to very
high plasma alloisoleucine, isoleucine, leucine, and valine; increased
branched-chain ketoacids in plasma and urine; low fibroblast BCKDC activity; and
possible hyperammonemia, positive anion gap, low to normal glucose, and low to
normal sodium/osmolality during crises. The record also includes ferric chloride
and 2,4-DNPH screening tests and decreased N-acetylaspartate peak on MRS during
crisis.

The characteristic clinical signal includes ataxia, brain edema on MRI, coma
during ketoacidotic episodes, acute encephalopathic crisis, feeding difficulty,
episodic irritability, lethargy during crisis, metabolic acidosis, maple syrup
odor, psychomotor delay, and episodic vomiting. Additional features include
apnea, neonatal seizures, cytotoxic and white-matter edema, delayed myelination,
dystonia, hypotonia or hypertonia, hypoglycemia, hypothermia during crisis,
ketoacidosis, pancreatitis, seizures, and vacuolating myelinopathy.

IEMbase treatments are avoidance of fasting, hemodialysis, peritoneal dialysis,
branched-chain amino acid restriction, sick-day management, thiamine,
isoleucine, valine, and liver transplantation.

## DisMech phenotype coverage

The generated `UNMAPPED` status is a false negative. DisMech models maple syrup
urine disease as a BCKDH-complex disorder with systemic accumulation of leucine,
isoleucine, valine, and their ketoacids. The local file explicitly includes a
Type IA subtype for E1-alpha subunit deficiency caused by BCKDHA.

DisMech captures the core intoxication mechanism, branched-chain amino acid and
ketoacid biomarkers, alloisoleucine, urine odor, poor feeding, lethargy,
encephalopathy, seizures, coma, cerebral edema, metabolic acidosis,
developmental delay, hypotonia, vomiting, and long-term neuropsychiatric
sequelae. It also includes BCKDHA-specific genetic coverage and treatments:
BCAA-restricted diet, BCAA-free medical formula, thiamine supplementation,
liver transplantation, IV BCAA-free solution, acute crisis management, and
preclinical or developing mechanism-directed therapies.

## Concordance and completeness

Judgement: false-negative generated mapping; high manual concordance with
`Maple_Syrup_Urine_Disease.yaml#Type IA`.

IEMbase adds granular diagnostic and crisis-detail fields that are not all
represented in DisMech: fibroblast BCKDC activity, specific bed-side screening
tests, MRS N-acetylaspartate change, detailed edema and myelination descriptors,
and explicit hemodialysis/peritoneal dialysis rows. DisMech is stronger for
mechanistic BCKDH-complex modeling, subtype structure, and treatment mechanism.

## Curation actions

- Update the crosswalk logic so BCKDHA-related MSUD type 1A resolves to
  `Maple_Syrup_Urine_Disease.yaml#Type IA` when subtype anchors are supported.
- Do not create a standalone BCKDHA disease file unless the project chooses to
  split MSUD gene subtypes into independent disorder entries.
- Consider IEMbase-only dialysis and acute diagnostic details as future
  phenotype or treatment enrichment candidates for the MSUD entry.
