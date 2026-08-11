# IEMbase 0134: BCAT2-related Branched-chain aminotransferase 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 134 |
| Nosology | 1.3.01.01 |
| Gene | BCAT2 |
| External IDs | OMIM:238340; OMIM:113530 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No valid BCAT2 target found; generated ornithine aminotransferase candidate is false |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as BCAT2-related branched-chain aminotransferase 2
deficiency, with alternate labels hypervalinemia and
hyperleucine-isoleucinemia, BCAA transaminase, and BCAT2. Treatability is
marked unknown.

Characteristic biochemical rows include increased plasma isoleucine, leucine,
and valine. Non-characteristic biochemical rows include normal allo-isoleucine,
normal-to-increased arginine, normal-to-increased glycine, and normal total
plasma acylcarnitines. Clinical rows include alopecia/loss of hair, hypotonia,
ketoacidosis, metabolic acidosis, nystagmus, decreased spontaneous movement,
hyperkinesia, failure to thrive, feeding difficulties, psychomotor delay, and
episodic vomiting.

## DisMech phenotype coverage

No standalone BCAT2 branched-chain aminotransferase deficiency target was found.
`ornithine_aminotransferase_deficiency.yaml` is a false lexical neighbor:
ornithine aminotransferase deficiency is an OAT retinal disorder with
hyperornithinemia, not a branched-chain amino-acid transamination disorder.

`Maple_Syrup_Urine_Disease.yaml` is a pathway neighbor because it models
branched-chain amino acid toxicity downstream of BCKD-complex deficiency and
mentions BCAT2-mediated transamination. It is not a valid disease target for
primary BCAT2 deficiency.

## Concordance and completeness

Judgement: true unmapped local disease gap, with MSUD as context only.

The IEMbase record's elevated leucine, isoleucine, and valine profile overlaps
with MSUD biochemistry, but the causal lesion is different. BCAT2 deficiency
should not be collapsed into BCKD deficiency or OAT deficiency. Current DisMech
does not provide a disease-level target for the BCAT2 entity.

## Curation actions

- Keep this record unmapped.
- Do not map to ornithine aminotransferase deficiency.
- Treat MSUD as pathway context only; consider a future BCAT2 entry with BCAA
  elevations, ketoacidosis/metabolic acidosis, feeding/growth problems,
  psychomotor delay, hypotonia, and hair-loss/nystagmus signals.
