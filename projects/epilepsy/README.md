# Epilepsy Project

Started: 2026-04-05

This project reframes epilepsy work in dismech as a mechanism-first curation
program rather than a single catch-all disorder page. The current repo already
contains useful epilepsy anchors, but the umbrella [`kb/disorders/Epilepsy.yaml`](../../kb/disorders/Epilepsy.yaml)
still mixes multiple mechanistic lanes that should eventually be represented as
separate, coherent entries.

## Artifact Set

- [Project brief and repo context](README.md)
- [Mechanism landscape and literature map](mechanism-landscape.md)
- [Initial candidate disorder scope](scope.md)

## Why This Project Exists

The current KB state is promising but uneven:

| Current entry | Role in project | Observation |
| --- | --- | --- |
| [`kb/disorders/Epilepsy.yaml`](../../kb/disorders/Epilepsy.yaml) | Umbrella/index entry | Useful as a top-level disease page, but it currently contains TLE-specific, BBB-specific, and mTOR-specific mechanism content that should be moved downward. |
| [`kb/disorders/Dravet_syndrome.yaml`](../../kb/disorders/Dravet_syndrome.yaml) | Positive model | Already close to a coherent gene-to-cell-type-to-circuit epilepsy mechanism entry. |
| [`kb/disorders/Jeavons_Syndrome.yaml`](../../kb/disorders/Jeavons_Syndrome.yaml) | Positive but mixed model | Good electroclinical anchor, but mechanisms are still partly speculative and evidence quality is mixed. |
| [`kb/disorders/Tuberous_Sclerosis_Complex.yaml`](../../kb/disorders/Tuberous_Sclerosis_Complex.yaml) | Multisystem mTOR anchor | Important epilepsy-relevant mTOR disorder already in the KB. |
| [`kb/disorders/Menkes_Disease.yaml`](../../kb/disorders/Menkes_Disease.yaml) | Metabolic/mitochondrial seizure anchor | Shows that epilepsy mechanisms can live inside broader metabolic disorders when seizures are downstream of a clear biochemical lesion. |

## Working Thesis

For dismech purposes, "epilepsy" is not one mechanism. It is a family of
related disease processes that repeatedly converge on abnormal circuit
excitability. The useful split points are the ones where at least one of the
following changes materially:

| Split criterion | Why it matters in dismech |
| --- | --- |
| Core mechanism | Different causal chains deserve different pathophysiology graphs. |
| Cell types / anatomical substrate | Interneuron failure, dysmorphic cortical neurons, astrocyte-endothelial dysfunction, and metabolic energy failure should not be collapsed into one node set. |
| Treatment logic | mTOR inhibition, ketogenic diet, precision sodium-channel decisions, immunotherapy, and surgery point to different disorder families. |
| Disease course / prognosis | DEEs, acquired inflammatory epilepsies, and focal structural epilepsies diverge clinically even when they share seizure phenotypes. |

## Immediate Deliverable of This First Pass

This first artifact set is intentionally not a full curation wave. It does
three things needed before file-by-file YAML work accelerates:

1. It records the repo's current epilepsy anchors and gaps.
2. It maps the main mechanism families with primary literature support.
3. It proposes a first-pass disorder coverage list that can drive the next
   curation batch.

## Near-Term Execution Plan

1. Keep [`kb/disorders/Epilepsy.yaml`](../../kb/disorders/Epilepsy.yaml) as the
   umbrella/index entry.
2. Move clearly subtype-specific mechanisms into subtype-level entries,
   especially temporal lobe, mTOR/cortical malformation, and BBB/inflammatory
   focal epilepsy lanes.
3. Treat [`kb/disorders/Dravet_syndrome.yaml`](../../kb/disorders/Dravet_syndrome.yaml)
   and [`kb/disorders/Tuberous_Sclerosis_Complex.yaml`](../../kb/disorders/Tuberous_Sclerosis_Complex.yaml)
   as high-value templates for mechanistically coherent epilepsy modeling.
4. Use [`mechanism-landscape.md`](mechanism-landscape.md) and
   [`scope.md`](scope.md) to choose the next 3 to 5 entries for actual YAML
   creation or refactoring.

## Open Modeling Questions

| Question | Current view |
| --- | --- |
| Should temporal lobe epilepsy and mesial temporal lobe epilepsy with hippocampal sclerosis be one entry or two? | Likely two if the second is curated around hippocampal sclerosis, memory impairment, and surgery-relevant mesial temporal pathology. |
| Should mTOR-related epilepsies be represented only as gene disorders (TSC, DEPDC5, etc.) or also as a mechanism family entry? | Both are probably useful: family-level for the shared mTOR/dysmorphic-cell program, gene/disorder-level for clinical specificity. |
| Is BBB disruption a standalone disease family or a mechanism module reused across focal epilepsies? | Likely a disease family only in selected acquired or drug-resistant focal epilepsies; otherwise better treated as a reusable mechanism module. |
| How broad should autoimmune epilepsy coverage be in wave 1? | Probably narrow: start with well-defined immune epilepsies or encephalitides with strong seizure relevance rather than a vague "autoimmune epilepsy" lump. |
