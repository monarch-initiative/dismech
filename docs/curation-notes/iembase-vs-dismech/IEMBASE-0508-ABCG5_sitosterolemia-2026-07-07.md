# IEMbase 0508: ABCG5-related sitosterolemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 508 |
| Nosology | 15.1.08.01 |
| Gene | ABCG5 |
| External IDs | OMIM:210250; ORPHA:2882 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | No exact local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ABCG5-related sitosterolemia, also named
phytosterolemia. No treatments are listed. Biochemical rows include normal HDL
cholesterol, markedly increased neonatal/infant LDL cholesterol with persistent
LDL elevation later in life, normal serum triglyceride, and positive plasma
sitosterols. Clinical rows include xanthelasma, xanthomas, carotid bruits,
femoral bruits, and adult myocardial ischemia.

## DisMech phenotype coverage

No exact local target was found for sitosterolemia, ABCG5, ABCG8, or
phytosterolemia. `Hyperlipidemia.yaml` provides only generic dyslipidemia and
atherosclerotic context: it models elevated LDL and triglyceride-rich
lipoproteins, downstream vascular injury, coronary artery disease, and
lipid-lowering therapies, but it does not model plant sterol accumulation,
ABCG5/ABCG8 sterol transporter dysfunction, normal triglycerides with elevated
sitosterols, childhood xanthomas, or sitosterolemia as a distinct recessive
metabolic disorder.

## Concordance and completeness

Judgement: true local gap.

The IEMbase record is not merely broad hyperlipidemia; it is a sterol-transport
disorder with plasma sitosterols as a diagnostic biochemical marker and an
autosomal recessive ABCG5 gene anchor. The local KB lacks this mechanism and
should not use nonspecific hyperlipidemia coverage as a substitute.

## Curation actions

- Track ABCG5-related sitosterolemia / phytosterolemia as a local curation gap.
- Preserve IEMbase prompts for plasma sitosterols, early marked LDL elevation,
  normal triglycerides, xanthomas/xanthelasma, bruits, and myocardial ischemia.
- When the corresponding ABCG8 IEMbase record is reviewed, evaluate whether
  ABCG5 and ABCG8 should share one sitosterolemia entry with gene-specific
  branches rather than separate disease files.
