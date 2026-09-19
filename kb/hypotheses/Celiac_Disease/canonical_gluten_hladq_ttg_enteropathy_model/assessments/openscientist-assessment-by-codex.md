# Assessment of the OpenScientist canonical celiac-disease report

## Overall assessment

**Verdict on the scoped core mechanism: supported.**

The durable core is the gluten-triggered, TG2-modified,
HLA-DQ-restricted CD4 T-cell response. Human intestinal T-cell work shows that
TG2 deamidation increases DQ2 binding and T-cell recognition
[PMID:10684852](https://pubmed.ncbi.nlm.nih.gov/10684852/), tetramer studies
identify disease-associated gluten-reactive CD4 T cells
[PMID:23775608](https://pubmed.ncbi.nlm.nih.gov/23775608/), and randomized
TG2 inhibition attenuates gluten-challenge mucosal injury
[PMID:34192430](https://pubmed.ncbi.nlm.nih.gov/34192430/).

That support does not validate the report's five proposed expansions as a
package. Several are useful leads, but their demonstrated scope ranges from
human biopsy association to epithelial monolayers and engineered mice. Two of
the most consequential conclusions—that IgA-CD71 transport is dominant and
that no anti-IL-15 human trial had been published—are untenable.

## What should be retained

ZED1227 is meaningful human interventional evidence. All three doses attenuated
the primary villus-height-to-crypt-depth endpoint during a six-week gluten
challenge, and follow-up work supports luminal enterocyte target localization
and broad transcriptomic effects
[PMID:37445994](https://pubmed.ncbi.nlm.nih.gov/37445994/) and
[PMID:38914866](https://pubmed.ncbi.nlm.nih.gov/38914866/). The result supports
a causal contribution from TG2 and its therapeutic tractability.

The report is also right that a linear, purely Th1 description is incomplete.
Human tissue studies support IL-17A and IL-21 production alongside IFN-gamma
[PMID:20061410](https://pubmed.ncbi.nlm.nih.gov/20061410/),
[PMID:21206487](https://pubmed.ncbi.nlm.nih.gov/21206487/), and
[PMID:22785229](https://pubmed.ncbi.nlm.nih.gov/22785229/). RCDII is a useful
boundary condition: persistent clonal IEL disease and its TCR repertoire
support expansion independent of ongoing gluten stimulation
[PMID:28188172](https://pubmed.ncbi.nlm.nih.gov/28188172/).

## Material corrections and qualifications

### ZED1227 did not prove dose dependence or strict necessity

The report calls the response dose-dependent and says it confirms TG2 as a
necessary node. The primary differences from placebo were 0.44 at 10 mg, 0.49
at 50 mg, and 0.48 at 100 mg. That is not monotonic. Injury was attenuated, not
abolished. The trial supports causal contribution; it does not prove an
exceptionless requirement across genotypes and disease contexts.

### The three-signal rule is a model result

IL-15 in epithelium and lamina propria, gluten, and HLA-DQ8 were jointly
required in a deliberately engineered mouse model
[PMID:32051586](https://pubmed.ncbi.nlm.nih.gov/32051586/). Human studies add
strong plausibility for IL-15 and synergy between epithelial stress and
adaptive immunity
[PMID:15357948](https://pubmed.ncbi.nlm.nih.gov/15357948/) and
[PMID:26001928](https://pubmed.ncbi.nlm.nih.gov/26001928/). They do not make
the exact mouse configuration a demonstrated universal rule for human villous
atrophy. The disease YAML should distinguish model-organism perturbation from
human co-requirement.

### Individual mechanisms do not establish three chronicity loops

The three components have evidence at different levels:

- IgA-CD71 transport was shown with patient biopsy localization and peptide
  flux across epithelial monolayers
  [PMID:22750506](https://pubmed.ncbi.nlm.nih.gov/22750506/).
- IFN-gamma-induced monocyte thioredoxin activated extracellular TG2 in a
  fibroblast/monocyte system and intestinal cryosections
  [PMID:21908620](https://pubmed.ncbi.nlm.nih.gov/21908620/).
- Epitope-dependent T-B collaboration supports selected TG2-reactive B cells as
  candidate antigen-presenting cells
  [PMID:31285344](https://pubmed.ncbi.nlm.nih.gov/31285344/).

No cited study tested the three as an integrated dynamical system. The
histologic follow-up cohorts document slow or incomplete recovery
[PMID:12219789](https://pubmed.ncbi.nlm.nih.gov/12219789/) and
[PMID:3170777](https://pubmed.ncbi.nlm.nih.gov/3170777/), but do not attribute
that recovery pattern to these loops. The report's chronicity explanation is a
testable synthesis, not an established causal result.

### ATI/TLR4 is a plausible preclinical amplifier

ATIs activate TLR4-responsive cell systems and increase intestinal inflammation
in mice [PMID:27993525](https://pubmed.ncbi.nlm.nih.gov/27993525/). The cited
humanized-mouse study concerns allergic colitis and airway inflammation, not
celiac disease [PMID:29574077](https://pubmed.ncbi.nlm.nih.gov/29574077/).
These papers do not directly demonstrate that ATIs initiate or amplify human
celiac enteropathy.

### Nexvax2 failure is not a pathway ablation experiment

The terminated RESET CeD trial found no reduction in acute symptoms after bolus
gluten challenge [PMID:36898393](https://pubmed.ncbi.nlm.nih.gov/36898393/).
It did not assess mucosal injury, despite the report saying otherwise. Failure
of one dose-escalation and tolerization strategy cannot distinguish insufficient
epitope coverage from dose, schedule, immune deviation, or other product-level
explanations. It therefore does not prove that the adaptive axis is
mechanistically insufficient.

### The transport-route ranking is unsupported

The CD71 experiment establishes that a transcellular mechanism can operate; it
does not measure its share of gluten flux in patients. The HLA-DQ8 mouse paper
measured bacterial translocation, not gluten peptides
[PMID:21822909](https://pubmed.ncbi.nlm.nih.gov/21822909/). Larazotide studies
reported mixed permeability, serology, and symptom outcomes
[PMID:23163616](https://pubmed.ncbi.nlm.nih.gov/23163616/) and
[PMID:34339872](https://pubmed.ncbi.nlm.nih.gov/34339872/); they did not compare
the two routes. “Dominant” should not be curated.

### A published anti-IL-15 phase 2a trial was missed

AMG 714 was tested in a randomized, double-blind, placebo-controlled phase 2a
trial in 64 adults with celiac disease undergoing gluten challenge, published in
2019 [PMID:31494096](https://pubmed.ncbi.nlm.nih.gov/31494096/). It did not
protect the primary villus-height-to-crypt-depth endpoint. A smaller IEL
increase at 300 mg and symptom signals were secondary findings. This directly
contradicts the report's May 2026 statement that no phase 2 or later human
anti-IL-15 trial had been published and supplies material negative evidence the
report omitted.

### Subtype observations support narrower conclusions

Potential celiac disease cohorts show progression in some children and loss of
seropositivity in others
[PMID:30978358](https://pubmed.ncbi.nlm.nih.gov/30978358/). Positive serology
does not demonstrate activation and later resolution of every step in the
report's adaptive cascade. Similarly, the cited seronegative cohort selected
cases partly by HLA-DQ2/DQ8 positivity and gluten-free-diet response but did not
measure gluten-specific T cells
[PMID:27352981](https://pubmed.ncbi.nlm.nih.gov/27352981/). Those observations
are consistent with the report's interpretation, not direct confirmation.

The dermatitis-herpetiformis conclusion is also too strong. One source is a
review [PMID:22811741](https://pubmed.ncbi.nlm.nih.gov/22811741/), one describes
DH-like dermatitis in a rhesus macaque
[PMID:22214930](https://pubmed.ncbi.nlm.nih.gov/22214930/), and the DQ8 NOD
model examined bowel pathology in only three blistering mice
[PMID:15489956](https://pubmed.ncbi.nlm.nih.gov/15489956/). These sources do
not prove enteropathy-independent humoral causation in humans.

Finally, HLA-DQ2/DQ8 has overwhelming prevalence and high exclusionary value,
but “necessary” is too absolute. Rare DQ2/DQ8-negative cohorts and possible DQ7
or single-chain risk have been reported
[PMID:9548076](https://pubmed.ncbi.nlm.nih.gov/9548076/) and
[PMID:26398634](https://pubmed.ncbi.nlm.nih.gov/26398634/).

## Citation, ontology, and provenance audit

The report identifies PMID:31593953 as the prospective TEDDY birth-cohort
analysis. It is a narrative review. The relevant primary TEDDY paper is
[PMID:25601977](https://pubmed.ncbi.nlm.nih.gov/25601977/), which found that
age at first gluten introduction was not an independent risk factor in the
studied range.

The ontology block should not be copied as written. OAK resolves `CL:0000492`
to **CD4-positive helper T cell**, not a gluten-specific T cell, and
`CL:0000084` to generic **T cell**, not intraepithelial lymphocyte;
`CL:0002496` is the direct IEL class. `GO:0002224` is **toll-like receptor
signaling pathway**, and the complete label for `GO:0002291` ends with “on
antigen presenting cell.” `GO:0006968` is correctly labeled **cellular defense
response**.

The claimed 130-paper systematic evaluation is not reconstructable from the
46-identifier citation manifest. No search strings, screening log, exclusion
list, iteration state, or complete corpus is deposited. Four figure tokens are
also unresolved: `final_causal_model.png`, `evidence_dashboard.png`,
`causal_chain.png`, and `knowledge_gaps.png` are absent from the hypothesis
directory. The assertion that all citations were verified is contradicted by
the TEDDY misclassification, the unmeasured Nexvax2 mucosal endpoint, and the
wrong title assigned to PMID:38914866 in the embedded seed metadata.

## Curation implication

Retain the high-level canonical gluten/TG2/HLA-DQ/CD4 T-cell mechanism. Preserve
IL-15 synergy, cytokine complexity, CD71 transport, T-B collaboration, and ATI
signaling as evidence-graded components or hypotheses at their demonstrated
taxonomic and experimental scope. Do not curate TG2 as proven strictly
necessary, the engineered three-signal configuration as a universal human rule,
the three loops as an established explanation of chronicity, ATI as a proven
human celiac adjuvant, or transcellular transport as dominant. Replace the
anti-IL-15 knowledge gap with the published negative primary-endpoint result.

Citations in this assessment are review context only. Any disease-YAML change
still requires the normal reference-cache and evidence-validation workflow.
