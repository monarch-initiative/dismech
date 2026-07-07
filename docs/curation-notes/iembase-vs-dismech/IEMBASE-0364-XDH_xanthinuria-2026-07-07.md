# IEMbase 0364: XDH-related xanthinuria type I

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 364 |
| Nosology | 16.2.1.01 |
| Gene | XDH |
| External IDs | OMIM:278300; OMIM:607633; ORPHA:93601 |
| Generated mapping | UNMAPPED; low candidate `Chronic_Granulomatous_Disease.yaml` |
| Candidate DisMech targets | No exact local target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents XDH-related xanthine oxidase deficiency, also listed as
xanthinuria type I, an autosomal recessive purine-metabolism disorder.
Characteristic rows include plasma hypoxanthine, urine hypoxanthine, acute
renal failure, plasma uric acid, urine uric acid, urolithiasis, xanthine
stones, plasma xanthine, and urine xanthine.

Additional clinical rows include impaired allopurinol to oxipurinol conversion
and myopathy. Biochemical rows include plasma and urine hypoxanthine, plasma and
urine uric acid, and plasma and urine xanthine. No treatment rows are present.

## DisMech phenotype coverage

The low chronic granulomatous disease candidate is a false neighbor and should
be rejected. Chronic granulomatous disease is a phagocyte NADPH oxidase primary
immunodeficiency, not an XDH xanthine oxidase/xanthinuria disorder.

No exact DisMech disease file for XDH-related xanthinuria type I was identified.
The correct disease concept would need xanthine oxidase deficiency, reduced uric
acid production, xanthine/hypoxanthine accumulation, and kidney-stone or renal
failure consequences.

## Concordance and completeness

Judgement: true local gap; reject the generated chronic granulomatous disease
candidate.

IEMbase supplies a coherent xanthinuria profile: XDH identity, autosomal
recessive inheritance, high xanthine/hypoxanthine, low uric acid, xanthine
stones, urolithiasis, acute renal failure, impaired allopurinol-to-oxipurinol
conversion, and possible myopathy.

## Curation actions

- Do not map this record to `Chronic_Granulomatous_Disease.yaml`.
- Create or prioritize a future XDH/xanthinuria type I target if this disease
  enters active DisMech curation.
- Treat specimen-specific xanthine, hypoxanthine, and uric-acid rows as
  high-value biochemical prompts for future source-backed curation.
