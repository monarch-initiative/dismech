# Assessment of the OpenScientist report

**Hypothesis:** Emerging Th17/IL-17 effector contribution
**Assessor:** Codex
**Verdict:** **PARTIALLY_SUPPORTED**

The report supports retaining an emerging Th17 contribution, but its proposed
IL-21/STAT3 replacement mechanism and anti-IL-17 contraindication are not
established. The key problem is context transfer: H. pylori infection studies
are repeatedly treated as direct tests of sterile AIG, and pathogen-specific
antibodies are relabeled as autoantibodies.

## Supported core

In the principal human tissue study, gastric cells from all eight tested AIG
patients responded to H+/K+-ATPase with IL-17A/F production. That is direct
antigen-responsive evidence, but “100%” refers to eight people, not a universal
population result, and it does not establish causality or disease-stage
dominance
([PMID:35911678](https://pubmed.ncbi.nlm.nih.gov/35911678/)).

The intrinsic-factor study reports that 94% of selected clones were Th17 **or**
Th1. It supports a mixed inflammatory compartment; it does not establish a
Th17-skewed or Th17-dominant pernicious-anemia compartment
([PMID:31080562](https://pubmed.ncbi.nlm.nih.gov/31080562/)).

Polarized Th17 transfer produced the most destructive gastritis among tested
conditions in an engineered immunodeficient mouse model
([PMID:18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/)). This is strong
model sufficiency, not evidence that Th17 dominates spontaneous human disease.
STAT3 perturbation also reduced TxA23 pathology
([PMID:40471463](https://pubmed.ncbi.nlm.nih.gov/40471463/)), but STAT3 is
pleiotropic and the experiment does not isolate Th17 or IL-21 mediation.

## Unsupported reframing

Epithelial IL-17RA deletion worsened inflammation during H. pylori infection
([PMID:38639570](https://pubmed.ncbi.nlm.nih.gov/38639570/)). This challenges a
simple cytotoxic narrative, but it is not a parietal-cell apoptosis experiment
in AIG and therefore does not “directly refute” that edge. The earlier global
Il17ra knockout study reported enhanced **H. pylori-specific** antibodies, not
AIG autoantibodies
([PMID:19812196](https://pubmed.ncbi.nlm.nih.gov/19812196/)).

Without that autoantibody premise, the report's IL-21 bridge is even more
indirect. Serum IL-21 and IL-21-producing clones make it a reasonable candidate
for testing, but no IL-21 blockade experiment in AIG exists. Anti-parietal-cell
antibodies are important biomarkers, and intrinsic-factor antibodies can
impair absorption; neither fact makes antibody production the established
terminal cause of parietal-cell destruction.

Likewise, no cited human or animal AIG intervention tests anti-IL-17. Infection
and cancer models raise a safety question, not a treatment contraindication.

The ontology candidates compound the curation risk:

- CL:0000163 is endocrine cell, not parietal cell (CL:0000162);
- GO:0032623 is interleukin-2 production, not interleukin-21 production;
- MONDO:0010156 is Troyer syndrome, not autoimmune gastritis;
- MONDO:0001061 is pylorus cancer, not pernicious anemia.

## Disease-YAML follow-up

This assessment does not edit `kb/disorders/Autoimmune_Gastritis.yaml`. Its
current Th17 notes, however, repeat nearly the entire unsupported reframing:
IL-17RA loss is said to increase autoantibody production and accelerate
carcinogenesis; IL-21/STAT3 is called the more likely pathogenic signal; and
anti-IL-17 is described as cautioned/contraindicated. Those statements should
be corrected in a separate disease-evidence PR.

The defensible disease-level conclusion is narrower: antigen-responsive human
IL-17 production and murine transfer experiments support an emerging Th17 arm;
human dominance, the terminal mediator, stage dependence, and therapeutic
direction remain unresolved.
