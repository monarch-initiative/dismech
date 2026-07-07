# IEMbase 0051: SLC7A7-related lysinuric protein intolerance

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 51 |
| Nosology | 1.11.06.01 |
| Gene | SLC7A7 |
| External IDs | OMIM:222700 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None; fuzzy neighbor `Hartnup_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive SLC7A7-related lysinuric protein
intolerance, also named dibasic aminoaciduria type 2 or LPI. Treatability is
marked yes. The listed prevalence is 1:60,000 in Italy and Finland and less
than 1:1,000,000 in most other places.

The biochemical profile is broad and severe: increased blood ammonia, increased
urinary orotic acid, increased urinary lysine with increased urinary arginine
and ornithine, low-to-normal plasma arginine/lysine/ornithine after infancy,
increased plasma alanine, citrulline, glutamine, glycine, and proline, plus
normal-to-increased LDH and increased ferritin.

The characteristic clinical feature is possible hyperammonemic coma. Additional
clinical features include protein intolerance, vomiting, diarrhea,
hepatosplenomegaly, pulmonary alveolar proteinosis, interstitial chest
radiograph changes, respiratory insufficiency with muscle weakness or diaphragm
paralysis, hemophagocytic lymphohistiocytosis/macrophage activation syndrome,
hemophagocytosis, glomerulonephritis, hypertension, end-stage renal failure,
osteoporosis, impaired bone growth, combined hyperlipidemia, intellectual
disability, and sparse hair.

## DisMech phenotype coverage

There is no local DisMech entry for SLC7A7-related lysinuric protein
intolerance.

The fuzzy neighbor `Hartnup_Disease.yaml` is a false positive. Hartnup disease
is SLC6A19/B0AT1 neutral amino acid transport disease with a
tryptophan/nicotinamide and pellagra-like neurocutaneous mechanism. LPI is an
SLC7A7 cationic/dibasic amino acid transport disorder with systemic nitrogen
handling consequences, hyperammonemia, protein intolerance, pulmonary, immune,
renal, and bone complications.

This record also should not be folded into `Cystinuria.yaml` despite dibasic
amino-acid urinary abnormalities. Cystinuria is SLC3A1/SLC7A9 cystine/dibasic
amino-acid transport disease dominated by cystine stones, whereas IEMbase ID 51
is a systemic LPI phenotype with hyperammonemia and multisystem complications.

## Concordance and completeness

Judgement: true unmapped record and high-value future curation target.

The generated unmapped status is appropriate because local DisMech lacks an LPI
entry. The severity and treatability make this much more than a benign
aminoaciduria. Its distinguishing features are SLC7A7, cationic amino acid
transport, hyperammonemia, urinary orotic acid, protein intolerance, pulmonary
alveolar proteinosis, HLH/macrophage activation, and renal/bone involvement.

## Curation actions

- Keep the record unmapped for now.
- Do not map to Hartnup disease or cystinuria.
- Prioritize a future standalone lysinuric protein intolerance entry because
  the phenotype is severe, treatable, and mechanistically distinct from the
  local aminoaciduria entries.
