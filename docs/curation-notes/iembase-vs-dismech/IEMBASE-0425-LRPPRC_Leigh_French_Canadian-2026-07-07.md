# IEMbase 0425: LRPPRC-related Leigh syndrome with French-Canadian ethnicity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 425 |
| Nosology | 7.4.08.02 |
| Gene | LRPPRC |
| External IDs | OMIM:220111; ORPHA:70472 |
| Generated mapping | UNMAPPED; low candidate `Leigh_Syndrome.yaml` |
| Candidate DisMech targets | `Leigh_Syndrome.yaml#French-Canadian` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents LRPPRC-related Leigh syndrome with French-Canadian ethnicity,
abbreviated LSFC. It records autosomal recessive inheritance. The biochemical
signal is markedly increased plasma lactate and low-to-normal glucose. Clinical
rows include Leigh-like MRI lesions, developmental delay, psychomotor
retardation, hypotonia, ataxia, encephalopathy, liver steatosis, feeding
difficulty, failure to thrive, seizures, tremor, perinatal death, and mild
facial dysmorphism with Saguenay/French-Canadian founder context.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local `Leigh_Syndrome.yaml`
has a `French-Canadian` subtype with MONDO congenital lactic acidosis,
Saguenay-Lac-Saint-Jean type, explicitly described as biallelic LRPPRC variants
causing complex IV-deficient Leigh syndrome. The same file also has an LRPPRC
genetic section linking biallelic LRPPRC variants to French-Canadian LSFC.

Local DisMech is stronger for the general Leigh syndrome pathophysiology and for
placing LRPPRC in the complex IV/cytochrome c oxidase deficient Leigh branch.
IEMbase adds a compact age-banded phenotype checklist, especially liver
steatosis, dysmorphism, EEG burst-suppression, tremor, and founder-population
clinical details.

## Concordance and completeness

Judgement: false negative; resolve to `Leigh_Syndrome.yaml#French-Canadian`.

The resources agree on LRPPRC, autosomal recessive LSFC, French-Canadian /
Saguenay-Lac-Saint-Jean context, complex IV-deficient Leigh syndrome, lactic
acidosis, hypotonia, ataxia, encephalopathy, Leigh-like lesions, and early
mortality risk.

## Curation actions

- Map this record to the French-Canadian subtype in `Leigh_Syndrome.yaml`.
- Consider adding IEMbase's liver steatosis, EEG burst-suppression, dysmorphic
  features, tremor, and low/normal glucose prompts after source verification.
- Preserve LSFC as a subtype within the broader Leigh syndrome entry unless a
  future split creates a dedicated LRPPRC LSFC file.
