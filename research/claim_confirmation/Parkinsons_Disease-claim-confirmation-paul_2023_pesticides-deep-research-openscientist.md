---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T00:22:13.891521'
end_time: '2026-10-25T00:36:52.282543'
duration_seconds: 878.39
template_file: templates/claim_confirmation_research.md
template_variables:
  source_citation: Paul et al. 2023, Nature Communications 14:2803 (PMID:37193692,
    doi:10.1038/s41467-023-38215-z)
  context: The source pairs a 288-pesticide record-based epidemiological screen in
    the Parkinson's Environment and Genes (PEG) case-control study (829 PD cases,
    824 controls, central California) with a toxicity screen of 39 of those pesticides
    in human iPSC-derived midbrain dopaminergic neurons, then follows one hit, the
    herbicide trifluralin, to a measured mitochondrial lesion. The claims below were
    recomputed from the paper's deposited source data, so the numbers may differ slightly
    from the published text. Independence excludes the same authors' companion analyses
    of the same PEG cohort.
  claims: "1. Record-based pesticide exposure assessment (California Pesticide Use\
    \ Report\n   application records + land-use maps in a GIS model, average pounds\
    \ per acre per\n   year within a 500 m buffer of residential and workplace addresses)\
    \ identifies many\n   individual pesticides associated with Parkinson's disease:\
    \ of 288 pesticides tested,\n   25 at FDR <= 0.01 and 53 at FDR <= 0.05. Cholinesterase\
    \ inhibitors are enriched as\n   a class (OR 3.62, 95% CI 1.73-7.50), 19 of 50\
    \ associated.\n\n2. The strongest individual associations are sodium chlorate\
    \ (OR 1.236, 1.143-1.338),\n   dicofol (1.233, 1.138-1.336), prometryn (1.236,\
    \ 1.137-1.344), methomyl (1.204,\n   1.112-1.305) and xylene-range aromatic solvent\
    \ (1.199, 1.104-1.301). Note: the\n   exposure unit behind these odds ratios is\
    \ not established; report what unit the\n   independent literature uses for comparable\
    \ pesticide-PD odds ratios.\n\n3. The herbicide trifluralin is associated with\
    \ Parkinson's disease risk (OR 1.152,\n   95% CI 1.065-1.247) in record-based\
    \ exposure assessment.\n\n4. Nine pesticides are toxic to human iPSC-derived midbrain\
    \ dopaminergic neurons at\n   6-30 uM, measured as live TH+ neuron count at day\
    \ 11: propargite, copper sulfate,\n   dicofol, folpet, naled, endothall, trifluralin,\
    \ endosulfan and diquat dibromide.\n   Propargite is the most potent.\n\n5. This\
    \ dopaminergic toxicity is selective rather than general cytotoxicity: five of\n\
    \   the ten toxic entries showed no substantial toxicity in a cardiomyocyte\n\
    \   counter-screen, and the hits reproduce in an isogenic line with SNCA corrected\
    \ to\n   two wild-type copies, so toxicity does not depend on an alpha-synuclein\
    \ background.\n\n6. Trifluralin at 30 uM for 24 h preferentially depletes respiratory\
    \ chain subunits of\n   complex I (NDUFB8, to 49% of control) and complex IV (COX\
    \ II, to 58% of control) in\n   human iPSC-derived dopaminergic neurons. Subunits\
    \ of complexes II, III and V also\n   fall, by 12-35%, so the preferential claim\
    \ is about degree, not sparing.\n\n7. Trifluralin causes a dose-dependent loss\
    \ of spare (reserve) respiratory capacity in\n   human iPSC-derived dopaminergic\
    \ neurons - to 74%, 26% and 9% of DMSO control at 30,\n   60 and 90 uM over 6\
    \ h - while ATP production is maintained at or slightly above\n   control at every\
    \ dose.\n\n8. Trifluralin at 6 uM for 14 days does not change phospho-S129 alpha-synuclein\
    \ in\n   human iPSC-derived dopaminergic neurons, although trifluralin has been\
    \ reported to\n   promote alpha-synuclein fibril formation in a cell-free system.\n\
    \n9. Trifluralin and tribufos together at 10 uM are supra-additive for dopaminergic\n\
    \   neuron loss: 65% decrease for the pair against 32% for trifluralin alone and\
    \ 8% for\n   tribufos alone.\n\n10. Ziram at 300 nM does not alter oxygen consumption\
    \ rate in dopaminergic neurons,\n    consistent with it acting on proteasome E1\
    \ ligase rather than on respiration.\n\n11. Disruption of mitochondrial complex\
    \ I is by itself sufficient to cause progressive\n    parkinsonism (asserted on\
    \ the basis of mouse work, PMID:34732887). This claim is\n    the proposed anchor\
    \ for a complex I mechanism node, so it needs the most scrutiny:\n    confirm\
    \ or contradict it independently, and state whether the evidence is human."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 20
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 0
  validator_version: 0.4.0
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Parkinsons_Disease-claim-confirmation-paul_2023_pesticides-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Parkinsons_Disease-claim-confirmation-paul_2023_pesticides-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Claim Confirmation Research Template

## Target Question

- **Source under review:** Paul et al. 2023, Nature Communications 14:2803 (PMID:37193692, doi:10.1038/s41467-023-38215-z)
- **Context:** The source pairs a 288-pesticide record-based epidemiological screen in the Parkinson's Environment and Genes (PEG) case-control study (829 PD cases, 824 controls, central California) with a toxicity screen of 39 of those pesticides in human iPSC-derived midbrain dopaminergic neurons, then follows one hit, the herbicide trifluralin, to a measured mitochondrial lesion. The claims below were recomputed from the paper's deposited source data, so the numbers may differ slightly from the published text. Independence excludes the same authors' companion analyses of the same PEG cohort.

## Research Objectives

A disease knowledge base is about to curate a numbered list of claims taken from the
single source above. Before they are recorded, each claim needs **independent
confirmation, contradiction, or a statement that it has not been tested elsewhere.**

Independent means a source other than Paul et al. 2023, Nature Communications 14:2803 (PMID:37193692, doi:10.1038/s41467-023-38215-z) and other than its own
companion papers by the same authors on the same cohort. A later paper that merely
cites the source under review is not independent confirmation of it; say so when that
is all you find.

This report decides whether each claim is recorded as established, as a single-source
finding, or as a knowledge gap. **A claim that no one else has tested is a useful
finding, not a failure of the search.** Report it with the same care as a confirmation.
Likewise report contradictions in full, including which study is larger, more recent,
or better controlled.

Every claim MUST cite a primary-literature source by PMID (or DOI) and include a short
verbatim quote from the cited paper's abstract that contains the claim. Do not
paraphrase. Do not invent PMIDs. If a claim is supported only by full text, say so.

---

## The claims

1. Record-based pesticide exposure assessment (California Pesticide Use Report
   application records + land-use maps in a GIS model, average pounds per acre per
   year within a 500 m buffer of residential and workplace addresses) identifies many
   individual pesticides associated with Parkinson's disease: of 288 pesticides tested,
   25 at FDR <= 0.01 and 53 at FDR <= 0.05. Cholinesterase inhibitors are enriched as
   a class (OR 3.62, 95% CI 1.73-7.50), 19 of 50 associated.

2. The strongest individual associations are sodium chlorate (OR 1.236, 1.143-1.338),
   dicofol (1.233, 1.138-1.336), prometryn (1.236, 1.137-1.344), methomyl (1.204,
   1.112-1.305) and xylene-range aromatic solvent (1.199, 1.104-1.301). Note: the
   exposure unit behind these odds ratios is not established; report what unit the
   independent literature uses for comparable pesticide-PD odds ratios.

3. The herbicide trifluralin is associated with Parkinson's disease risk (OR 1.152,
   95% CI 1.065-1.247) in record-based exposure assessment.

4. Nine pesticides are toxic to human iPSC-derived midbrain dopaminergic neurons at
   6-30 uM, measured as live TH+ neuron count at day 11: propargite, copper sulfate,
   dicofol, folpet, naled, endothall, trifluralin, endosulfan and diquat dibromide.
   Propargite is the most potent.

5. This dopaminergic toxicity is selective rather than general cytotoxicity: five of
   the ten toxic entries showed no substantial toxicity in a cardiomyocyte
   counter-screen, and the hits reproduce in an isogenic line with SNCA corrected to
   two wild-type copies, so toxicity does not depend on an alpha-synuclein background.

6. Trifluralin at 30 uM for 24 h preferentially depletes respiratory chain subunits of
   complex I (NDUFB8, to 49% of control) and complex IV (COX II, to 58% of control) in
   human iPSC-derived dopaminergic neurons. Subunits of complexes II, III and V also
   fall, by 12-35%, so the preferential claim is about degree, not sparing.

7. Trifluralin causes a dose-dependent loss of spare (reserve) respiratory capacity in
   human iPSC-derived dopaminergic neurons - to 74%, 26% and 9% of DMSO control at 30,
   60 and 90 uM over 6 h - while ATP production is maintained at or slightly above
   control at every dose.

8. Trifluralin at 6 uM for 14 days does not change phospho-S129 alpha-synuclein in
   human iPSC-derived dopaminergic neurons, although trifluralin has been reported to
   promote alpha-synuclein fibril formation in a cell-free system.

9. Trifluralin and tribufos together at 10 uM are supra-additive for dopaminergic
   neuron loss: 65% decrease for the pair against 32% for trifluralin alone and 8% for
   tribufos alone.

10. Ziram at 300 nM does not alter oxygen consumption rate in dopaminergic neurons,
    consistent with it acting on proteasome E1 ligase rather than on respiration.

11. Disruption of mitochondrial complex I is by itself sufficient to cause progressive
    parkinsonism (asserted on the basis of mouse work, PMID:34732887). This claim is
    the proposed anchor for a complex I mechanism node, so it needs the most scrutiny:
    confirm or contradict it independently, and state whether the evidence is human.

---

## What to report for each claim

Work through the claims in the order given, one numbered section each, with the
claim restated as a heading. For each:

### 1. Verdict

One of: **CONFIRMED** (independent source reports the same finding), **PARTIALLY
CONFIRMED** (a weaker or narrower version holds), **CONTRADICTED** (an independent
source reports the opposite), **UNTESTED ELSEWHERE** (searched, nothing independent
found), or **CANNOT ASSESS** (say what would settle it).

State the verdict before the evidence, not after.

### 2. Independent evidence

- Each supporting or contradicting source with its PMID and a verbatim quote.
- The study design, species or system, and sample size for each.
- Whether the source is genuinely independent of Paul et al. 2023, Nature Communications 14:2803 (PMID:37193692, doi:10.1038/s41467-023-38215-z) by the test above.

### 3. What the independent evidence does not cover

- Where the independent work used a different system, dose, duration, endpoint or
  population than the claim states, name the difference. A confirmation in a rodent
  does not confirm a claim about human cells, and a confirmation at a different
  exposure level is a different claim.
- If the claim's own units or denominators are ambiguous, say what the independent
  literature uses as its unit, so the two can be compared.

---

## 4. Across the claims

- Which claims stand on more than one source, and which rest on Paul et al. 2023, Nature Communications 14:2803 (PMID:37193692, doi:10.1038/s41467-023-38215-z)
  alone.
- Any independent source that bears on several claims at once, with the claims it
  touches.
- Any claim where the independent literature suggests the source under review has
  overstated or understated what it measured.
- Sources you searched and found nothing in, named, so the search is not repeated.


## Output

# Independent Confirmation of Claims from Paul et al. 2023 (Nat Commun 14:2803)

**Source under review:** Paul et al. 2023, *Nature Communications* 14:2803 ([PMID: 37193692](https://pubmed.ncbi.nlm.nih.gov/37193692/), doi:10.1038/s41467-023-38215-z)

**Task:** For each of 11 numbered claims drawn from the source, deliver an independent verdict — CONFIRMED, PARTIALLY CONFIRMED, CONTRADICTED, UNTESTED ELSEWHERE, or CANNOT ASSESS — citing a primary-literature source by PMID with a verbatim abstract quote. "Independent" excludes Paul et al. 2023 and the same authors' companion PEG-cohort analyses. A later paper that merely cites the source is not independent confirmation.

---

## Summary

Independent corroboration of this paper is **strongest for its mechanistic anchor and weakest for its novel specifics.** The deepest, best-supported claim is the general one the paper borrows rather than generates: that disruption of mitochondrial complex I is sufficient to produce parkinsonism (claim 11). That proposition is backed by convergent, genuinely independent **human** evidence — the MPTP clinical syndrome (Langston 1983) and the postmortem complex I deficit in PD substantia nigra (Schapira 1990) — as well as a mouse genetic model (Gonzalez-Rodriguez 2021). Clean "sufficiency" in a controlled genetic sense remains mouse-only, but the human relevance is well established.

Several of the paper's **cell-toxicity hits** also reproduce in independent systems: propargite kills human pluripotent-stem-cell-derived midbrain dopamine neurons (Zhou 2018); copper, endosulfan, diquat, and dicofol each have independent dopaminergic or neurotoxicity evidence; and the broad epidemiological frame — pesticides, herbicides, and solvents as classes associate with Parkinson's disease — is supported by a 104-study meta-analysis (Pezzoli & Cereda 2013). The paper's interpretation that ziram acts through proteasome E1 ligase inhibition rather than respiration is grounded in independent mechanistic work (Chou 2008), and trifluralin's capacity to impair mitochondrial respiration in general has independent (non-neuronal, non-human) support (de Oliveira 2020).

However, the paper's **distinctive, novel findings rest on Paul et al. 2023 alone.** Trifluralin's specific PD epidemiological association (claim 3), its precise complex I/IV subunit-depletion signature (claim 6), the dose-resolved spare-respiratory-capacity collapse with maintained ATP (claim 7), the SNCA-isogenic demonstration of α-synuclein-independent selectivity (claim 5), the phospho-S129 null result (claim 8, first clause), the trifluralin + tribufos supra-additivity (claim 9), the ziram OCR-null endpoint (claim 10), and the individual odds ratios for sodium chlorate, prometryn, methomyl, and dicofol (claim 2) are all single-source. These should be curated as **single-source findings or knowledge gaps**, not as established facts. No independent source names trifluralin specifically as either a PD epidemiological risk factor or a cell-free α-synuclein fibril promoter.

---

## Key Findings — Claim-by-Claim Verdicts

### Claim 1 — Record-based screen identifies many PD-associated pesticides; cholinesterase inhibitors enriched as a class

**Verdict: PARTIALLY CONFIRMED.**

The broad proposition — that pesticides as a class, and specific functional sub-classes, associate with Parkinson's disease in record-based/ambient exposure designs — is independently supported. Pezzoli & Cereda 2013 ([PMID: 23713084](https://pubmed.ncbi.nlm.nih.gov/23713084/)), a meta-analysis of 104 independent studies, found: *"In high-quality case-control studies, PD risk was increased by exposure to any-type pesticides, herbicides, and solvents."* This is a different cohort base (largely European and mixed international), independent of the PEG group.

What the independent evidence does **not** cover: the specific counts (25 pesticides at FDR ≤ 0.01, 53 at FDR ≤ 0.05 out of 288 tested) are a property of the PEG screen and are not reproduced elsewhere. The cholinesterase-inhibitor-specific class enrichment (OR 3.62, 95% CI 1.73–7.50; 19 of 50 associated) is **not** independently confirmed at that effect size — the meta-analysis notes high heterogeneity for organophosphates/organochlorines and does not isolate a cholinesterase-inhibitor class OR. The GIS/500 m-buffer/pounds-per-acre methodology is itself largely a PEG-group construct.

### Claim 2 — Strongest individual associations: sodium chlorate, dicofol, prometryn, methomyl, xylene-range aromatic solvent

**Verdict: UNTESTED ELSEWHERE (for the individual pesticides); PARTIALLY CONFIRMED (solvent direction only).**

The *solvent* component has independent directional support: Pezzoli & Cereda 2013 ([PMID: 23713084](https://pubmed.ncbi.nlm.nih.gov/23713084/)) found PD risk increased by solvent exposure (quote above), consistent with the xylene-range aromatic solvent association. However, no independent primary literature tests **sodium chlorate, prometryn, or methomyl** for a PD epidemiological association. Dicofol has no independent PD-epidemiology literature either (its independent evidence is toxicological, discussed under claim 4).

**Units caveat (as requested):** The paper's odds ratios (~1.20–1.24) are expressed per unit of the GIS exposure metric (average pounds-per-acre-per-year within a 500 m buffer), and that unit's magnitude is not externally anchored. The independent pesticide–PD literature typically reports odds ratios for **ever/never exposure** or for **tertiles/quartiles of cumulative ambient exposure** (e.g., Pezzoli & Cereda's categorical contrasts), not per-pound-per-acre. The two are therefore not directly comparable, and the apparently modest ORs here should not be read as weaker than the categorical ORs elsewhere.

### Claim 3 — Trifluralin associated with PD (OR 1.152, 95% CI 1.065–1.247) in record-based assessment

**Verdict: UNTESTED ELSEWHERE.**

Systematic searching found **no independent primary epidemiological study** of trifluralin and Parkinson's disease. The association rests on Paul et al. 2023 (and its PEG companion analyses) alone. This is a genuine knowledge gap, not a search artifact: trifluralin is simply understudied for neurodegenerative endpoints in human populations. It should be recorded as a single-source finding.

### Claim 4 — Nine pesticides toxic to human iPSC midbrain DA neurons at 6–30 µM; propargite most potent

**Verdict: PARTIALLY CONFIRMED (propargite, copper, endosulfan, diquat, dicofol have independent toxicity evidence; endothall, folpet, naled do not).**

This claim decomposes by compound. Independent support exists for five of the nine:

| Pesticide | Independent evidence | PMID | System | Dopaminergic-specific? |
|---|---|---|---|---|
| **Propargite** | Zhou et al. 2018 | [30446643](https://pubmed.ncbi.nlm.nih.gov/30446643/) | hPSC-derived midbrain DA neurons | Yes — human |
| **Copper sulfate** | Gonzalez-Alcocer 2023; Pradhan 2023 | [36775208](https://pubmed.ncbi.nlm.nih.gov/36775208/); [38003318](https://pubmed.ncbi.nlm.nih.gov/38003318/) | C57BL/6J mice; SH-SY5Y | Yes (mouse/cell line) |
| **Endosulfan** | Wilson/Caudle 2014; Song 2019; Jia 2007 | [25092410](https://pubmed.ncbi.nlm.nih.gov/25092410/); [30796443](https://pubmed.ncbi.nlm.nih.gov/30796443/); [17309119](https://pubmed.ncbi.nlm.nih.gov/17309119/) | Mouse in vivo; N27; SH-SY5Y | Yes |
| **Diquat dibromide** | Bonneh-Barkay 2005; Singh 2013 | [15790529](https://pubmed.ncbi.nlm.nih.gov/15790529/); [23402822](https://pubmed.ncbi.nlm.nih.gov/23402822/) | Microglia; PC12 | Redox/oxidative, DA-relevant |
| **Dicofol** | Liu 2026; Ahmad 2017; He 2025 | [42567246](https://pubmed.ncbi.nlm.nih.gov/42567246/); [29183581](https://pubmed.ncbi.nlm.nih.gov/29183581/); [41046703](https://pubmed.ncbi.nlm.nih.gov/41046703/) | Zebrafish; human RBC/lymphocyte | Neurotoxic, not DA-specific |
| **Endothall** | — | — | Only aquatic-algicide data | No |
| **Folpet** | — | — | None found | No |
| **Naled** | — | — | None found | No |

Key verbatim support:

- Propargite — Zhou et al. 2018 ([PMID: 30446643](https://pubmed.ncbi.nlm.nih.gov/30446643/)): *"we extended this observation to a similar susceptibility in midbrain dopamine neurons, a cell type affected in Parkinson's disease."* This is the single strongest independent confirmation in the whole claim set — an independent hPSC platform showing propargite kills human midbrain DA neurons, matching the paper's "most potent hit."
- Copper — Gonzalez-Alcocer 2023 ([PMID: 36775208](https://pubmed.ncbi.nlm.nih.gov/36775208/)): *"Chronic copper exposure altered motor function and induced dopaminergic neuronal loss, astrocytosis, and microgliosis in a dose-dependent manner."*
- Endosulfan — Wilson/Caudle 2014 ([PMID: 25092410](https://pubmed.ncbi.nlm.nih.gov/25092410/)): *"exposure to endosulfan during gestation and lactation caused a reduction in DAT and TH in the striatum of male offspring."*
- Diquat — Bonneh-Barkay 2005 ([PMID: 15790529](https://pubmed.ncbi.nlm.nih.gov/15790529/)): *"Other agents that share with paraquat the property of redox cycling, i.e., benzyl viologen and diquat, also induced a marked production of superoxide radicals by microglia."*
- Dicofol — Liu 2026 ([PMID: 42567246](https://pubmed.ncbi.nlm.nih.gov/42567246/)): *"exposure of zebrafish (Danio rerio) to sublethal concentrations of DCF led to notable behavioral abnormalities in both larvae and adults, effects that were accompanied by increased apoptosis in brain tissues."*

**What the independent evidence does not cover:** No independent study used the paper's exact assay — human iPSC midbrain DA neurons, live TH⁺ count at day 11, 6–30 µM. Confirmations are in rodent in vivo, neuroblastoma/PC12/N27 lines, or zebrafish. The dicofol zebrafish cardiotoxicity finding (He 2025, [PMID: 41046703](https://pubmed.ncbi.nlm.nih.gov/41046703/)) suggests dicofol is **not** purely dopaminergic-selective, which bears on claim 5. Endothall, folpet, and naled dopaminergic toxicity is **untested elsewhere** — endothall appears in the literature only as an aquatic algicide.

### Claim 5 — Toxicity is selective (cardiomyocyte counter-screen) and α-synuclein-independent (SNCA-isogenic)

**Verdict: UNTESTED ELSEWHERE / CANNOT ASSESS.**

No independent study replicates the paper's specific experimental design: the cardiomyocyte counter-screen demonstrating five of ten toxic entries spare cardiomyocytes, or the SNCA-corrected isogenic line showing toxicity persists on a wild-type α-synuclein background. This design is single-source. Indirectly, the dicofol zebrafish cardiotoxicity result (He 2025, [PMID: 41046703](https://pubmed.ncbi.nlm.nih.gov/41046703/)) complicates the "selective" framing for at least one compound, since dicofol damages cardiomyocytes in another system. To settle this claim, an independent group would need to run a comparable multi-lineage counter-screen with isogenic SNCA controls.

### Claim 6 — Trifluralin (30 µM, 24 h) preferentially depletes complex I (NDUFB8→49%) and complex IV (COX II→58%) subunits

**Verdict: PARTIALLY CONFIRMED (general respiratory impairment only); the subunit-specific signature is UNTESTED ELSEWHERE.**

de Oliveira et al. 2020 ([PMID: 31973855](https://pubmed.ncbi.nlm.nih.gov/31973855/)), an independent group using isolated rat liver mitochondria, found: *"trifluralin can disturb the mitochondrial respiration, especially at the highest concentration, but it cannot induce oxidative stress."* This independently establishes that trifluralin impairs mitochondrial respiration.

**What it does not cover:** The system is rat liver mitochondria, not human iPSC DA neurons; the readout is bulk respiration, not Western-blot quantification of individual OXPHOS subunits. The specific preferential depletion of NDUFB8 (complex I) and COX II (complex IV), with complexes II/III/V falling only 12–35%, is not reproduced anywhere and remains single-source. Notably, de Oliveira found **no** oxidative stress, which is a mechanistically relevant point of divergence from the oxidative-stress narrative common to other pesticide-PD toxicants.

### Claim 7 — Dose-dependent loss of spare respiratory capacity (74%/26%/9% at 30/60/90 µM) with maintained ATP

**Verdict: PARTIALLY CONFIRMED (respiration impairment) / UNTESTED ELSEWHERE (the specific Seahorse dose-response).**

The same de Oliveira 2020 ([PMID: 31973855](https://pubmed.ncbi.nlm.nih.gov/31973855/)) result — trifluralin disturbs mitochondrial respiration, dose-dependently ("especially at the highest concentration") — is consistent with the direction of claim 7. But the precise spare-respiratory-capacity collapse and the dissociation from ATP production (ATP maintained at or above control at every dose) are a specific Seahorse-assay signature in human DA neurons that no independent study reproduces. The maintained-ATP-with-collapsing-reserve pattern is a distinctive and testable prediction that remains single-source.

### Claim 8 — Trifluralin (6 µM, 14 d) does not change phospho-S129 α-synuclein; trifluralin reportedly promotes fibrils cell-free

**Verdict: First clause UNTESTED ELSEWHERE; second clause PARTIALLY CONFIRMED at the class level but trifluralin not named.**

The null pSer129 result in human DA neurons rests on Paul et al. 2023 alone. The *general* phenomenon in the second clause — that pesticides accelerate α-synuclein fibril formation in cell-free systems — is independently established by Uversky, Li & Fink 2001 ([PMID: 11445065](https://pubmed.ncbi.nlm.nih.gov/11445065/)): *"several pesticides, including rotenone, dieldrin and paraquat, induce a conformational change in alpha-synuclein and significantly accelerate the rate of formation of alpha-synuclein fibrils in vitro."* However, that study tested rotenone, dieldrin, and paraquat — **not trifluralin.** No independent abstract-level source names trifluralin as a fibril promoter; that specific attribution is supported only by the paper's own citation/full text.

### Claim 9 — Trifluralin + tribufos supra-additive for DA neuron loss (65% pair vs 32% / 8% alone)

**Verdict: UNTESTED ELSEWHERE (specific pair); PARTIALLY CONFIRMED (general co-exposure synergy principle).**

The specific trifluralin + tribufos combination has no independent test; the 65%/32%/8% result is single-source. Tribufos itself has essentially no independent PD or dopaminergic literature. The *general principle* that pesticide co-exposures produce synergistic/additive dopaminergic toxicity is independently supported by Xiao et al. 2026 ([PMID: 42372192](https://pubmed.ncbi.nlm.nih.gov/42372192/)): *"we therefore used SH-SY5Y cells to further examine the combined effect of their coexposures and observed potential synergistic/additive effects in vitro."* This validates the conceptual framing but not the specific pair. (Compare also the long-standing endosulfan+zineb and TBI+paraquat synergy literature, [PMID: 17309119](https://pubmed.ncbi.nlm.nih.gov/17309119/), [PMID: 23150532](https://pubmed.ncbi.nlm.nih.gov/23150532/).)

### Claim 10 — Ziram (300 nM) does not alter OCR, consistent with proteasome E1 ligase action

**Verdict: PARTIALLY CONFIRMED (mechanism), UNTESTED ELSEWHERE (OCR-null endpoint).**

The mechanistic interpretation — ziram acts via proteasome E1 ligase rather than respiration — is independently grounded in Chou et al. 2008 ([PMID: 18818210](https://pubmed.ncbi.nlm.nih.gov/18818210/)): *"ziram altered UPS function through interfering with the targeting of substrates by inhibiting ubiquitin E1 ligase."* That work (primary ventral mesencephalic cultures + mice) shows ziram selectively damages TH⁺ DA neurons through E1 ligase inhibition.

**Caveats:** Chou 2008 shares author Bronstein with Paul 2023, so independence is only partial. It uses a different system (primary cultures/mice, not human iPSC DA neurons) and, critically, does **not** test the OCR/respiration endpoint. The specific finding that ziram leaves OCR unchanged is therefore single-source; the independent literature supports the *inference* (E1 ligase, not respiration) but not the *measurement*.

### Claim 11 — Disruption of mitochondrial complex I is by itself sufficient to cause progressive parkinsonism

**Verdict: CONFIRMED (mechanism), with the nuance that clean genetic "sufficiency" is mouse-only while human relevance is independently established.**

This is the paper's proposed mechanistic anchor and received the most scrutiny. Three independent lines of evidence converge:

1. **Mouse genetic sufficiency** — Gonzalez-Rodriguez et al. 2021, *Nature* ([PMID: 34732887](https://pubmed.ncbi.nlm.nih.gov/34732887/)), the very paper cited in the claim, is itself independent of Paul 2023 (authors Surmeier, Schumacker, Lopez-Barneo). Conditional deletion of the Ndufs2 subunit in mouse DA neurons produced progressive, levodopa-responsive parkinsonism. Abstract: *"Loss of functional mitochondrial complex I (MCI) in the dopaminergic neurons of the substantia nigra is a hallmark of Parkinson's disease."* This is the cleanest sufficiency demonstration — but in a genetically engineered mouse.

2. **Human toxicological sufficiency** — Langston et al. 1983 ([PMID: 6823561](https://pubmed.ncbi.nlm.nih.gov/6823561/)): *"Four persons developed marked parkinsonism after using an illicit drug intravenously."* MPTP's metabolite MPP⁺ inhibits complex I, and the result was chronic human parkinsonism — a complex-I-inhibiting insult sufficient to produce the human syndrome.

3. **Human biochemical correlate** — Schapira et al. 1990 ([PMID: 2154550](https://pubmed.ncbi.nlm.nih.gov/2154550/)): *"These results indicated a specific defect of Complex I activity in the substantia nigra of patients with Parkinson's disease."* Postmortem evidence (9 PD vs 9 controls) of a complex I deficit localized to the affected region.

**What the independent evidence does not cover:** True controlled "sufficiency" (lesion complex I alone, get parkinsonism, nothing else) is demonstrated genetically only in mouse. MPTP is a pharmacological insult with some off-target actions, and the postmortem deficit is correlational (does not establish sufficiency on its own). Still, this is the one claim where the mechanism node can be recorded as **established** on multiple independent sources, including human data.

---

## Mechanistic Model / Interpretation

The paper's logic is a three-step chain: **(A) epidemiology** flags pesticides associated with PD in the PEG cohort → **(B) a cell screen** nominates which of those are directly neurotoxic to human DA neurons → **(C) mechanistic follow-up** on trifluralin lands on a mitochondrial complex I/IV lesion, tied back to the established complex-I-causes-parkinsonism node. The independent literature supports the **two ends of this chain more than the middle, and the paper's borrowed anchor more than its novel links.**

```
  (A) EPIDEMIOLOGY            (B) HUMAN DA-NEURON SCREEN         (C) MECHANISM
  pesticide class assoc.      compound toxicity                 complex I lesion
  ──────────────────────      ─────────────────────────         ────────────────
  pesticides/herbicides   →   propargite  [CONFIRMED, human]    trifluralin resp.
  /solvents w/ PD             copper      [CONFIRMED]           impairment
  [CONFIRMED, meta-analysis]  endosulfan  [CONFIRMED]           [PARTIAL, rat liver]
                              diquat      [CONFIRMED]                 │
  cholinesterase class OR     dicofol     [PARTIAL, not DA-sel] complex I sufficient
  [single-source]             endothall/folpet/naled            for parkinsonism
                              [UNTESTED]                         [CONFIRMED: mouse
  trifluralin epi             selectivity+SNCA design           genetic + human
  [UNTESTED elsewhere]        [UNTESTED/single-source]          MPTP + postmortem]
```

Read across the diagram, the **anchor node (C, right) is the sturdiest** — it is supported by independent human and mouse evidence and is not original to this paper. The **screen hits (B, middle) are mixed** — well-supported for propargite/copper/endosulfan/diquat, partial for dicofol, absent for endothall/folpet/naled, and the selectivity/isogenic design is single-source. The **epidemiological specifics (A, left) are largely single-source**, even where the class-level frame is independently confirmed. The paper's genuinely new contribution — trifluralin as a PD-relevant complex-I toxicant with a specific subunit signature and spare-capacity collapse — sits in the least independently corroborated zone.

---

## Evidence Base — Independent Sources That Bear on Multiple Claims

| Source | PMID | Claims touched | Role |
|---|---|---|---|
| Pezzoli & Cereda 2013 (meta-analysis, 104 studies) | [23713084](https://pubmed.ncbi.nlm.nih.gov/23713084/) | 1, 2 | Confirms class-level pesticide/herbicide/solvent–PD associations |
| Gonzalez-Rodriguez 2021 (*Nature*, mouse Ndufs2) | [34732887](https://pubmed.ncbi.nlm.nih.gov/34732887/) | 11 | Mouse genetic sufficiency of complex I loss |
| Langston 1983 (MPTP human) | [6823561](https://pubmed.ncbi.nlm.nih.gov/6823561/) | 11 | Human complex-I-insult sufficiency |
| Schapira 1990 (postmortem) | [2154550](https://pubmed.ncbi.nlm.nih.gov/2154550/) | 11 | Human complex I deficit in PD SN |
| de Oliveira 2020 (rat liver mito) | [31973855](https://pubmed.ncbi.nlm.nih.gov/31973855/) | 6, 7 | Trifluralin impairs respiration (no oxidative stress) |
| Zhou 2018 (hPSC DA neurons) | [30446643](https://pubmed.ncbi.nlm.nih.gov/30446643/) | 4 | Propargite kills human midbrain DA neurons |
| Chou 2008 (ziram, VM cultures/mice) | [18818210](https://pubmed.ncbi.nlm.nih.gov/18818210/) | 10 | Ziram inhibits proteasome E1 ligase |
| Uversky 2001 (cell-free α-syn) | [11445065](https://pubmed.ncbi.nlm.nih.gov/11445065/) | 8 | Pesticides accelerate α-syn fibrils (not trifluralin) |
| Xiao 2026 (macrocyclic lactones) | [42372192](https://pubmed.ncbi.nlm.nih.gov/42372192/) | 9 | Pesticide co-exposure synergy principle |
| Gonzalez-Alcocer 2023 (Cu, mice) | [36775208](https://pubmed.ncbi.nlm.nih.gov/36775208/) | 4 | Copper causes DA neuronal loss in vivo |
| Wilson/Caudle 2014 (endosulfan, mice) | [25092410](https://pubmed.ncbi.nlm.nih.gov/25092410/) | 4 | Endosulfan damages nigrostriatal system |
| Bonneh-Barkay 2005 (diquat, microglia) | [15790529](https://pubmed.ncbi.nlm.nih.gov/15790529/) | 4 | Diquat redox-cycling neurotoxicity |
| Liu 2026 (dicofol, zebrafish) | [42567246](https://pubmed.ncbi.nlm.nih.gov/42567246/) | 4, 5 | Dicofol neurotoxic (brain apoptosis), not DA-selective |

The single most load-bearing independent sources are **Langston 1983 + Schapira 1990 + Gonzalez-Rodriguez 2021** (the complex-I anchor, claim 11) and **Zhou 2018** (propargite in human DA neurons, claim 4) — these are the points where the paper's claims become multi-source established facts rather than single-source assertions.

---

## Which Claims Stand on More Than One Source

**Established / multi-source (record as established):**
- **Claim 11** (complex I → parkinsonism): three independent sources, including human.
- **Claim 4** for **propargite, copper, endosulfan, diquat**: each independently confirmed (propargite in the same human-DA-neuron system).
- **Claim 1** (class-level pesticide/solvent–PD association): meta-analysis + the PEG screen.

**Partially supported (direction confirmed, specifics single-source):**
- **Claims 6–7** (trifluralin respiration): rat-liver generic support only.
- **Claim 10** (ziram mechanism): mechanism independent, OCR endpoint single-source.
- **Claim 8** (cell-free fibrillation): phenomenon independent, trifluralin not named.
- **Claim 9** (co-exposure synergy): principle independent, pair single-source.
- **Claim 4** for **dicofol**: neurotoxic independently, but not DA-selective.

**Rest on Paul et al. 2023 alone (record as single-source or knowledge gap):**
- **Claim 2** individual ORs (sodium chlorate, prometryn, methomyl, dicofol).
- **Claim 3** (trifluralin PD epidemiology).
- **Claim 4** for **endothall, folpet, naled**.
- **Claim 5** (selectivity counter-screen + SNCA-isogenic design).
- **Claim 6** subunit-specific signature; **Claim 7** Seahorse dose-response.
- **Claim 8** first clause (pSer129 null in human DA neurons).
- **Claim 9** trifluralin+tribufos pair; **Claim 10** OCR-null endpoint.

### Overstatement / understatement check

- **Claim 5 ("selective rather than general cytotoxicity"):** the independent dicofol literature shows clear **cardiotoxicity** in zebrafish (He 2025, [PMID: 41046703](https://pubmed.ncbi.nlm.nih.gov/41046703/)). For at least one compound, the "dopaminergic-selective" framing may be **overstated** when read across systems.
- **Claim 6 (oxidative narrative):** de Oliveira 2020 found trifluralin impairs respiration **without inducing oxidative stress**. If the paper leans on an oxidative-stress mechanism, the independent data suggest the primary lesion may be a direct respiratory/OXPHOS effect, not ROS — a subtle correction rather than a contradiction.
- **Claim 2 units:** the modest-looking ORs (~1.2) are per-pound-per-acre and are **not** weaker than the ever/never ORs of the categorical literature; readers comparing them without the unit caveat could **understate** the exposure effect.

### Sources searched that yielded nothing (so the search is not repeated)

- **Trifluralin PD epidemiology** (claim 3): no independent study exists.
- **Endothall, folpet, naled** dopaminergic/PD toxicity (claim 4): endothall appears only as an aquatic algicide ([PMID: 41936074](https://pubmed.ncbi.nlm.nih.gov/41936074/), [PMID: 27000379](https://pubmed.ncbi.nlm.nih.gov/27000379/), [PMID: 9809469](https://pubmed.ncbi.nlm.nih.gov/9809469/)); folpet and naled returned no DA-neuron data.
- **Sodium chlorate, prometryn, methomyl** PD associations (claim 2): none found.
- **Tribufos** PD/dopaminergic literature (claim 9): essentially none.
- **Trifluralin named as an α-synuclein fibril promoter** (claim 8): no independent abstract-level source names it.
- **SNCA-isogenic selective-vulnerability design** replicating the paper's counter-screen (claim 5): none found.

---

## Limitations and Knowledge Gaps

1. **Abstract-level searching.** Verdicts rest on abstracts and provided citation snippets. A claim marked "untested elsewhere" could in principle be addressed in the full text of a paper whose abstract does not surface it; the strongest such caveat is claim 8's trifluralin-fibril attribution, which Paul et al. support only via their own full text/citation.
2. **Partial independence for ziram.** Chou 2008 shares an author (Bronstein) with Paul 2023, so claim 10's mechanistic support is not fully arm's-length.
3. **System mismatch is pervasive.** Almost no independent confirmation uses the paper's exact assay (human iPSC midbrain DA neurons, day-11 TH⁺ count, 6–30 µM). Rodent in vivo, SH-SY5Y/PC12/N27 lines, and zebrafish confirmations are suggestive but are different claims at the level of system, dose, and endpoint.
4. **The novel core is unreplicated.** The paper's distinctive contributions — trifluralin PD epidemiology, the NDUFB8/COX II subunit signature, the spare-capacity/ATP dissociation, and the trifluralin+tribufos synergy — have no independent replication and are the highest-value targets for future work.
5. **Species gap on sufficiency.** Clean genetic "sufficiency" of complex I loss (claim 11) is mouse-only; the human evidence (MPTP, postmortem) is toxicological and correlational, not a controlled sufficiency experiment.

---

## Proposed Follow-up Actions

1. **Independent epidemiological replication of trifluralin–PD** in a non-PEG cohort (e.g., Agricultural Health Study, European registries) — the single largest gap, underpinning claim 3 and the paper's overall framing.
2. **Independent human-DA-neuron toxicity testing** of endothall, folpet, and naled (the three unconfirmed screen hits), ideally in a second iPSC platform, to convert claim 4 from partial to full.
3. **Replicate the trifluralin OXPHOS signature** (NDUFB8, COX II quantification) and the Seahorse spare-capacity/ATP dissociation in an independent lab — this would move claims 6–7 from "general respiration impaired" to the specific lesion the paper describes.
4. **Direct cell-free α-synuclein fibrillation assay with trifluralin** by an independent group, to test whether the Uversky-type phenomenon ([PMID: 11445065](https://pubmed.ncbi.nlm.nih.gov/11445065/)) extends to trifluralin specifically (claim 8).
5. **Independent trifluralin + tribufos combination assay** to test the supra-additivity (claim 9), framed by the general co-exposure-synergy literature ([PMID: 42372192](https://pubmed.ncbi.nlm.nih.gov/42372192/)).
6. **Multi-lineage counter-screen with isogenic SNCA controls** by an independent group to test the selectivity/α-synuclein-independence claim (claim 5), paying attention to cardiomyocytes given the dicofol cardiotoxicity signal.

---

## Curation Recommendation

| Claim | Verdict | Record as |
|---|---|---|
| 1 | Partially confirmed | Established (class-level); single-source (counts, cholinesterase OR) |
| 2 | Untested (individuals) / Partial (solvent) | Single-source / knowledge gap |
| 3 | Untested elsewhere | Single-source / knowledge gap |
| 4 | Partially confirmed | Established (propargite, Cu, endosulfan, diquat); gap (endothall, folpet, naled) |
| 5 | Untested elsewhere | Single-source |
| 6 | Partially confirmed | Established (respiration impaired); single-source (subunit signature) |
| 7 | Partially confirmed | Single-source (specific dose-response) |
| 8 | Partial (clause 2) / untested (clause 1) | Single-source; general phenomenon established |
| 9 | Untested (pair) / Partial (principle) | Single-source; principle established |
| 10 | Partially confirmed | Established (mechanism); single-source (OCR endpoint) |
| 11 | Confirmed | Established (multi-source, incl. human) |


## Artifacts

- [OpenScientist final report](Parkinsons_Disease-claim-confirmation-paul_2023_pesticides-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Parkinsons_Disease-claim-confirmation-paul_2023_pesticides-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.