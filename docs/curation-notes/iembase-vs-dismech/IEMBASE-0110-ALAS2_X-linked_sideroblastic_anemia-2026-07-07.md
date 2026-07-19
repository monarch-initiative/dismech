# IEMbase 0110: ALAS2-related erythroid 5-aminolevulinate synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 110 |
| Nosology | 17.1.01.01 |
| Gene | ALAS2 |
| External IDs | OMIM:300751; ORPHA:75563 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None for a disease entry; contextual mention in `Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` differential diagnosis |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ALAS2-related erythroid 5-aminolevulinate synthase
deficiency, with alternate labels X-linked recessive sideroblastic anemia type
1 and XLSA. Treatability is marked unknown, though the treatment table lists
hemin with low-level evidence.

The cached JSON has no characteristic biochemical rows. The non-characteristic
clinical rows are dysmorphic erythrocytes, liver dysfunction, and increased
bone-marrow sideroblasts, with adolescent/adult onset patterning.

## DisMech phenotype coverage

There is no curated DisMech disease entry for ALAS2-related sideroblastic
anemia. `Inherited_Porphyria.yaml` contains ALAS2-related X-linked
protoporphyria, but that is the opposite ALAS2 direction: erythroid ALAS2
superactivity/gain of function with protoporphyrin accumulation and
photosensitivity. It should not be reused for ALAS2 deficiency.

`Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` mentions X-linked
sideroblastic anemia only as a differential diagnosis for ALAS2-related pure
sideroblastic anemia without mitochondrial myopathy. That is useful context,
but it is not phenotype coverage for a standalone XLSA disease model.

## Concordance and completeness

Judgement: true unmapped disease gap.

The IEMbase record is sparse but points to a distinct hematologic heme-synthesis
disorder centered on ring sideroblasts and erythroid morphology, not a
porphyria. DisMech currently has related heme and sideroblastic-anemia context,
but no ALAS2-deficiency entry that could be assessed for concordant phenotypes.

## Curation actions

- Do not map this to ALAS2-related X-linked protoporphyria.
- Consider a future standalone X-linked sideroblastic anemia / ALAS2 deficiency
  entry if sideroblastic anemia scope is expanded.
- Reuse the MLASA differential-diagnosis note only as context, not as a
  canonical target.
