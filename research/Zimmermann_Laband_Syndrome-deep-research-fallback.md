---
title: Zimmermann-Laband Syndrome Deep-Research Fallback
disorder: Zimmermann_Laband_Syndrome
date: 2026-05-09
status: provider_timeout_fallback
attempted_providers:
  - openai
---

# Zimmermann-Laband Syndrome Deep-Research Fallback

An automated deep-research provider was attempted after the initial
cache-backed YAML existed, but it stayed silent and was stopped by the bounded
timeout:

- `timeout 120s just research-disorder openai Zimmermann_Laband_Syndrome` returned 124.

The curation therefore used generated local caches plus direct PubMed searches
and fetched PubMed/Orphanet records. The reviewed disease scope is
Zimmermann-Laband syndrome as represented by ORPHA:3473 and MONDO:0000200,
including the molecularly solved KCNH1, KCNN3, and ATP6V1B2 genetic
heterogeneity.

## Scope Confirmation

- ORPHA:3473 supplied the definition, neonatal onset, cross-references,
  gene-disease rows, epidemiology, and all HPO phenotype rows.
- PMID:23994350 supplied the clinical literature review, developmental-delay
  and epilepsy frequencies, and inheritance interpretation.
- PMID:25915598 supplied the KCNH1 gain-of-function mechanism, ATP6V1B2
  recurrent de novo variation, and the core clinical feature summary.
- PMID:31155282 supplied KCNN3 de novo variants and patch-clamp gain-of-function
  evidence.
- PMID:33594261 supplied the broader syndromic neurodevelopmental potassium
  channelopathy framing for KCNH1/KCNN3-related disease.
- PMID:35639255 supplied KCNH1 ciliary localization and ciliogenesis/Sonic
  Hedgehog signaling perturbation evidence.
- PMID:39087232 and PMID:40604848 supplied oral-management evidence for
  gingival fibromatosis, delayed tooth eruption, gingivectomy, gingivoplasty,
  and supportive myofunctional/speech-language oral therapy.

## Coverage Notes

The YAML intentionally models the most evidence-backed mechanisms as a compact
pathograph: increased K+ conductance, ATP6V1B2 V-ATPase complex perturbation,
KCNH1-related ciliary signaling disruption, neurodevelopmental dysfunction,
gingival/dental overgrowth, and distal digital/nail developmental abnormality.
Temple-Baraitser syndrome and KCNK4-related FHEIG overlap clinically, but they
are kept as differential/overlap notes rather than merged into the ZLS disease
entry.
