# IEMbase 0107: FECH-related ferrochelatase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 107 |
| Nosology | 17.1.1.01 |
| Gene | FECH |
| External IDs | OMIM:177000 |
| Generated mapping | MAPPED |
| Candidate DisMech targets | `Inherited_Porphyria.yaml#Erythropoietic Protoporphyria` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as FECH-related ferrochelatase deficiency, with alternate
label erythropoietic protoporphyria (EPP). Treatability is marked yes, but the
cached JSON has no treatment rows.

The characteristic biochemical rows are normal-to-increased stool
protoporphyrin, increased free erythrocyte protoporphyrin, and low-to-normal
serum ferritin and iron. Clinical rows are anemia, liver dysfunction, and
microcytosis.

## DisMech phenotype coverage

The generated mapping to
`Inherited_Porphyria.yaml#Erythropoietic Protoporphyria` is correct at the
current local modeling level. The inherited-porphyria umbrella has an
erythropoietic protoporphyria subtype and a protoporphyria mechanism branch
covering reduced FECH expression, protoporphyrin IX accumulation, cutaneous
phototoxicity, and liver dysfunction risk.

DisMech also includes increased erythrocyte or plasma protoporphyrin as a
biochemical readout and afamelanotide pharmacotherapy for EPP/X-linked
protoporphyria light tolerance.

## Concordance and completeness

Judgement: correct subtype-level mapping with good mechanism concordance.

DisMech is richer for the defining phototoxicity mechanism and EPP/XLP treatment
context. IEMbase is more granular for the FECH-specific lab profile, especially
free RBC protoporphyrin, stool protoporphyrin, low/low-normal iron and ferritin,
microcytosis, and anemia. DisMech currently records anemia primarily under
congenital erythropoietic porphyria rather than FECH-related EPP.

## Curation actions

- Keep `Inherited_Porphyria.yaml#Erythropoietic Protoporphyria` as the current
  target.
- Consider a future standalone EPP entry if porphyria subtypes are split out of
  the umbrella.
- Review iron/ferritin, microcytosis, and anemia as possible FECH-EPP phenotype
  or biomarker additions before curating them locally.
