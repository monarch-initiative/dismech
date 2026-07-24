# OpenScientist deep-research batch: 10 open hypotheses (2026-07-06)

Provenance note for a batch of OpenScientist deep-research runs launched against
ten genuinely *open* mechanistic hypotheses in the knowledge base. Outputs land
under `kb/hypotheses/<Disease>/<hypothesis_group_id>/openscientist.md` (plus the
`.citations.md` sidecar), produced by:

```bash
uv run python scripts/hypothesis_deep_research.py run openscientist <Disease> <hypothesis_group_id>
```

## Selection method

The candidate pool was the 103 disease-level `mechanistic_hypotheses` that carried
**no** existing OpenScientist run, enumerated with:

```bash
uv run python scripts/hypothesis_deep_research.py list --missing-provider openscientist
```

From that pool the batch deliberately favours hypotheses where the mechanism is
still contested — `ALTERNATIVE` and `EMERGING` status entries, and competing
origin models — because an adversarial multi-source synthesis adds the most value
where the literature has not converged. Canonical, well-settled mechanisms were
deprioritised. The ten span neurodegeneration, pulmonary fibrosis, post-viral
illness, dysautonomia, psychiatry, reproductive endocrinology, immunology, and
oncology so the batch is not concentrated in one subsystem.

## The ten selected hypotheses

| # | Disease | Hypothesis group | Status | Why it is worth investigating |
|---|---------|------------------|--------|-------------------------------|
| 1 | Parkinson's Disease | `body_first_enteric_alpha_synuclein_model` | ALTERNATIVE | The "body-first" (gut/vagal) vs "brain-first" origin debate is a live, high-stakes question in PD pathogenesis. |
| 2 | Parkinson's Disease | `brain_first_central_alpha_synuclein_model` | ALTERNATIVE | Paired counterpart to #1; running both sides lets OpenScientist adjudicate the competing origin models. |
| 3 | Idiopathic Pulmonary Fibrosis | `senescence_first_model` | ALTERNATIVE | Senescence-first vs injury-centric origin of fibrosis is unresolved and therapeutically consequential (senolytics). |
| 4 | Long COVID | `herpesvirus_reactivation_model` | EMERGING | EBV/herpesvirus reactivation as a driver of post-acute sequelae is topical and genuinely open. |
| 5 | Postural Orthostatic Tachycardia Syndrome | `neuropathic_denervation_model` | ALTERNATIVE | POTS has multiple competing subtype mechanisms; the neuropathic/autoimmune-denervation arm needs a rigorous evidence audit. |
| 6 | Schizophrenia | `complement_synaptic_pruning_hypothesis` | EMERGING | C4/complement-mediated excess synaptic pruning is a major emerging hypothesis with mixed human evidence. |
| 7 | Alzheimer's Disease | `ev_mediated_tau_propagation_model` | EMERGING | Extracellular-vesicle-mediated tau spread is an emerging propagation mechanism distinct from canonical trans-synaptic seeding. |
| 8 | Polycystic Ovary Syndrome | `neuroendocrine_lh_first_model` | ALTERNATIVE | The neuroendocrine (GnRH/LH-first) vs insulin-first origin debate is central to PCOS pathophysiology. |
| 9 | IgG4-Related Disease | `innate_first_bystander_model` | ALTERNATIVE | Whether IgG4-RD is innate-driven with IgG4 as a bystander, or antibody-driven, remains an open immunopathogenesis question. |
| 10 | Gorlin Syndrome | `gli_bypass_resistance_model` | EMERGING | SMO-independent GLI activation as a Hedgehog-inhibitor resistance mechanism is an emerging precision-oncology question. |

## Verification discipline

OpenScientist is a deep-research provider and its outputs are **leads, not ground
truth** (see the DR-verification and NEC sections of `CLAUDE.md`). Before any
snippet, PMID, or ontology term from these reports is promoted into a
`kb/disorders/` or `kb/modules/` entry, it must pass the standard anti-hallucination
workflow: `just fetch-reference` for each PMID, snippet-substring verification against
the cached abstract, and `just validate-terms-file`. This batch only *generates* the
research; promotion into curated YAML is a separate, verified step.
