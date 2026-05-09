# Cor Pulmonale Research Note

## Provider Attempts

Falcon was attempted twice with `just research-disorder falcon Cor_Pulmonale`
after exporting `EDISON_API_KEY` from `/home/harry/dismech/edison_tok`. Both
runs remained active without writing `research/Cor_Pulmonale-deep-research-falcon.md`
and were terminated after bounded waits. The generic cyberian fallback
(`just research-disorder cyberian Cor_Pulmonale`) likewise remained active
without producing a report. The repo-supported cyberian-codex fallback
(`just research-disorder-cyberian-codex Cor_Pulmonale`) started but exited with
code 137.

Because no provider report was available, curation used PubMed-backed references
fetched with `just fetch-reference`. Evidence snippets in
`kb/disorders/Cor_Pulmonale.yaml` were selected from the fetched cache files and
validated locally.

## Mechanistic Summary

Cor pulmonale is right ventricular hypertrophy, dilation, and/or right-sided
heart failure secondary to respiratory-system disease, pulmonary vascular
disease, or chronic gas-exchange impairment rather than primary left-heart
disease. The curated page treats it as a complex cardiopulmonary disorder.

The main mechanistic chain is:

1. Chronic lung or pulmonary vascular disease causes pulmonary vascular-bed
   loss, narrowing, remodeling, and fibrosis.
2. Hypoxemia drives hypoxic pulmonary vasoconstriction, and endothelial
   dysfunction shifts mediator balance toward vasoconstriction and vascular
   remodeling.
3. Pulmonary hypertension and increased pulmonary vascular resistance raise
   right ventricular afterload.
4. Persistent right ventricular loading leads to hypertrophy, dilation, and
   eventual right-sided failure with systemic congestion.

Treatment curation was limited to claims directly supported by cached evidence:
long-term oxygen therapy for hypoxemic COPD-related cor pulmonale; conditional
PH-specific vasodilator therapy where evidence is limited; and cautious diuretic
therapy for congestion.
