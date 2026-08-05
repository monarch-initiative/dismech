# IEMbase 0753: ABHD5-related acylglycerol acyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 753 |
| Nosology | 14.4.06.01 |
| Nosology code | IEM0660 |
| Gene | ABHD5 |
| External IDs | OMIM:275630; ORPHA:98907 |
| Generated mapping | AMBIGUOUS; exact alias match to Chanarin-Dorfman syndrome |
| Candidate DisMech targets | `Dorfman_Chanarin_Disease.yaml`; `Triglyceride_Storage_Disease_Type_1.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as ABHD5-related
1-acylglycerol-3-phosphate O-acyltransferase deficiency, with alternate names
Chanarin-Dorfman syndrome, abhydrolase D5 deficiency, and neutral lipid storage
disease with ichthyosis. The phenotype signal includes hepatomegaly, hepatic
steatosis, ichthyosis, short stature, intellectual disability, and neonatal
vacuolated lymphocytes.

## DisMech phenotype coverage

Local coverage exists, but the mapper correctly exposes ambiguity.
`Dorfman_Chanarin_Disease.yaml` is an exact local target for
Chanarin-Dorfman syndrome / neutral lipid storage disease with ichthyosis. It
models ABHD5 / CGI-58 deficiency, impaired ATGL coactivation, systemic
triacylglycerol droplet accumulation, and phenotypes including ichthyosis,
hepatic steatosis, hepatomegaly, myopathy, cataract, sensorineural hearing
loss, splenomegaly, and Jordans anomaly or leukocyte lipid vacuoles.

`Triglyceride_Storage_Disease_Type_1.yaml` also appears to cover the same
ABHD5-related neutral lipid storage disease type I identity, including
ichthyosis and hepatic disease. This creates duplicate or overlapping local
coverage rather than a true unmapped gap.

## Concordance and completeness

Judgement: exact local coverage with duplicate-target ambiguity.

The best current target for this IEMbase record is
`Dorfman_Chanarin_Disease.yaml`, with `Triglyceride_Storage_Disease_Type_1.yaml`
as synonymous or duplicate context. DisMech captures the core disease
mechanism and major phenotypes; IEMbase is sparser and adds a concise age-coded
signal for intellectual disability, short stature, and neonatal vacuolated
lymphocytes.

## Curation actions

- Treat `Dorfman_Chanarin_Disease.yaml` as the primary exact mapping for this
  IEMbase record.
- Review `Triglyceride_Storage_Disease_Type_1.yaml` for duplicate or
  overlapping disease identity and decide whether to merge, cross-link, or
  distinguish the two local entries.
- Preserve the IEMbase leukocyte vacuole, intellectual disability, and short
  stature prompts when refining phenotype coverage.
