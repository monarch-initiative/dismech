---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-26T23:43:15.510620'
end_time: '2026-05-27T00:18:21.163476'
duration_seconds: 2105.65
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: COVID-19
  category: ''
  hypothesis_group_id: mac1_allosteric_pivot_model
  hypothesis_label: Mac1 Allosteric Conformational Pivot Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: mac1_allosteric_pivot_model\nhypothesis_label:\
    \ Mac1 Allosteric Conformational Pivot Model\nstatus: EMERGING\ndescription: The\
    \ conserved Mac1 fold across coronaviruses (SARS-CoV-2, SARS-CoV, MERS-CoV) supports\
    \ treating\n  Mac1 as a thermodynamic pivot point rather than only an active-site\
    \ target. Allosteric stabilization\n  of distinct Mac1 conformational states or\
    \ PROTAC-based physical degradation would rebalance the host\n  interactome toward\
    \ antiviral ADP-ribosylation, with potential broad anti-coronavirus activity that\
    \ active-site\n  inhibition alone may not achieve. Active drug-discovery programs\
    \ (including the third CACHE community\n  challenge) have established Mac1 as\
    \ a tractable structural target with hundreds of crystallographically\n  characterized\
    \ ligands, providing a strong starting point for conformational-pivot chemistry.\n\
    evidence:\n- reference: PMID:33158944\n  supports: SUPPORT\n  evidence_source:\
    \ IN_VITRO\n  snippet: SARS-CoV-2, SARS-CoV, and Middle East respiratory syndrome\
    \ coronavirus (MERS-CoV) Mac1 domains\n    exhibit similar structural folds, and\
    \ all 3 proteins bound to ADP-ribose with affinities in the low\n    micromolar\
    \ range\n  explanation: Structural conservation of Mac1 across coronaviruses supports\
    \ the feasibility of a pan-CoV\n    pivot-control strategy beyond active-site\
    \ inhibition.\n- reference: PMID:40964377\n  supports: SUPPORT\n  evidence_source:\
    \ COMPUTATIONAL\n  snippet: Significant efforts have been recently dedicated to\
    \ the discovery of small molecule inhibitors\n    against the Macrodomain 1 (Mac1)\
    \ of nonstructural protein 3 (NSP3) as potential antivirals for SARS-CoV-2.\n\
    \  explanation: Ban et al. and the CACHE3 challenge directly demonstrate that\
    \ Mac1 is an active drug-discovery\n    target with community-wide investment,\
    \ supporting the feasibility of allosteric and PROTAC-warhead\n    programs.\n\
    - reference: PMID:40964377\n  supports: SUPPORT\n  evidence_source: COMPUTATIONAL\n\
    \  snippet: Our results illustrate the effectiveness of ML-accelerated docking\
    \ to rapidly identify novel\n    chemical series and provide a strong foundation\
    \ for the development of SARS-CoV-2 NSP3 Mac1 inhibitors.\n  explanation: The\
    \ community-level chemistry infrastructure for Mac1 hit-finding lowers the experimental\n\
    \    barrier for the proposed Mac1 conformational pivot experiment."
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
citation_count: 29
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** COVID-19
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** mac1_allosteric_pivot_model
- **Hypothesis Label:** Mac1 Allosteric Conformational Pivot Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: mac1_allosteric_pivot_model
hypothesis_label: Mac1 Allosteric Conformational Pivot Model
status: EMERGING
description: The conserved Mac1 fold across coronaviruses (SARS-CoV-2, SARS-CoV, MERS-CoV) supports treating
  Mac1 as a thermodynamic pivot point rather than only an active-site target. Allosteric stabilization
  of distinct Mac1 conformational states or PROTAC-based physical degradation would rebalance the host
  interactome toward antiviral ADP-ribosylation, with potential broad anti-coronavirus activity that active-site
  inhibition alone may not achieve. Active drug-discovery programs (including the third CACHE community
  challenge) have established Mac1 as a tractable structural target with hundreds of crystallographically
  characterized ligands, providing a strong starting point for conformational-pivot chemistry.
evidence:
- reference: PMID:33158944
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: SARS-CoV-2, SARS-CoV, and Middle East respiratory syndrome coronavirus (MERS-CoV) Mac1 domains
    exhibit similar structural folds, and all 3 proteins bound to ADP-ribose with affinities in the low
    micromolar range
  explanation: Structural conservation of Mac1 across coronaviruses supports the feasibility of a pan-CoV
    pivot-control strategy beyond active-site inhibition.
- reference: PMID:40964377
  supports: SUPPORT
  evidence_source: COMPUTATIONAL
  snippet: Significant efforts have been recently dedicated to the discovery of small molecule inhibitors
    against the Macrodomain 1 (Mac1) of nonstructural protein 3 (NSP3) as potential antivirals for SARS-CoV-2.
  explanation: Ban et al. and the CACHE3 challenge directly demonstrate that Mac1 is an active drug-discovery
    target with community-wide investment, supporting the feasibility of allosteric and PROTAC-warhead
    programs.
- reference: PMID:40964377
  supports: SUPPORT
  evidence_source: COMPUTATIONAL
  snippet: Our results illustrate the effectiveness of ML-accelerated docking to rapidly identify novel
    chemical series and provide a strong foundation for the development of SARS-CoV-2 NSP3 Mac1 inhibitors.
  explanation: The community-level chemistry infrastructure for Mac1 hit-finding lowers the experimental
    barrier for the proposed Mac1 conformational pivot experiment.
```

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Mac1 Allosteric Conformational Pivot Model: Hypothesis Evaluation Report

> **Hypothesis ID:** mac1_allosteric_pivot_model | **Disease:** COVID-19 | **Status in KB:** EMERGING
> **Date:** 2026-05-27 | **Literature reviewed:** 59 papers | **Findings confirmed:** 15
> **Visualizations:** `mac1_bfactor_analysis.png`, `mac1_evidence_map.png`, `mac1_evidence_status_table.png`

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — Retain EMERGING status with upgraded confidence**

The Mac1 Allosteric Conformational Pivot Model proposes that the conserved SARS-CoV-2 Mac1 macrodomain should be treated as a thermodynamic pivot point amenable to allosteric stabilization or PROTAC-mediated degradation, rather than solely as an active-site drug target. After systematic evaluation against 59 papers and 15 confirmed findings, the hypothesis is **partially supported** with significant caveats.

The core premise — that Mac1 conformational dynamics matter beyond catalytic activity — has direct experimental support from the isoleucine gate mutation data ([PMID: 38260573](https://pubmed.ncbi.nlm.nih.gov/38260573/)) and from 153 co-crystal structures revealing unexpected ligand-mediated conformational changes ([PMID: 36598939](https://pubmed.ncbi.nlm.nih.gov/36598939/)). A validated allosteric site in the homologous PARP14 macrodomain 2 (GeA-69, [PMID: 28991428](https://pubmed.ncbi.nlm.nih.gov/28991428/)) provides structural precedent that macrodomain allosteric inhibition is chemically feasible. However, **no allosteric site has been experimentally demonstrated on any viral Mac1**, no Mac1 PROTAC exists, and three independent laboratories have now shown that active-site inhibitors alone can achieve antiviral activity in immune-competent models — substantially raising the bar for any allosteric approach to demonstrate added value. Furthermore, 15–25% of the most critical COVID-19 patients carry interferon deficiencies that would render any Mac1-targeting strategy ineffective, regardless of mechanism.

**Most important caveats:**
1. No allosteric site on Mac1 has been directly identified — the PARP14 MD2 allosteric site is selective for PARP14 and may not be structurally conserved in viral Mac1
2. The translational gap (Lee et al. 2024 vs. Suryawanshi et al. 2025) is resolvable by model selection rather than requiring allosteric approaches
3. No Mac1 PROTAC has been designed or tested; Mac1's context within the ~200 kDa nsp3 polyprotein introduces unique biological uncertainties
4. B-factor-based conformational coupling is suggestive but not proof of a druggable allosteric mechanism

---

## Summary

The Mac1 macrodomain of SARS-CoV-2 nsp3 is a genetically validated virulence factor whose loss renders the virus avirulent in vivo while barely affecting cell-culture replication. This makes Mac1 a compelling but unusual drug target: its therapeutic mechanism operates through immune restoration rather than direct antiviral inhibition, meaning efficacy depends on the patient's interferon competence and requires immune-competent assay systems for proper evaluation. The "allosteric pivot" hypothesis extends current Mac1 drug discovery by proposing that conformational control — through allosteric stabilization or physical degradation — could achieve broader and more resistance-resilient antiviral effects than active-site inhibition alone.

Our investigation identified strong supporting evidence for the conceptual foundation of this hypothesis. The isoleucine gate residue in the conserved GIF motif demonstrates that a single-residue change enhancing ADP-ribose binding (without impairing catalysis) severely attenuates MERS-CoV and SARS-CoV-2, proving that Mac1's conformational dynamics are functionally critical beyond its enzymatic activity. B-factor analysis of ultra-high-resolution crystal structures revealed that Mac1's C-terminal region (residues 155–169) shows 3.6-fold greater conformational coupling to the active site than the global average, at a topological position corresponding to the validated allosteric pocket in PARP14 MD2. These converging lines of evidence make the allosteric pivot model scientifically plausible.

However, the hypothesis faces three critical gaps: (1) no allosteric site has been identified or characterized on any viral macrodomain; (2) no PROTAC targeting a domain within a large viral polyprotein has been demonstrated; and (3) the recent success of active-site inhibitors (AVI-4206, pyrrolo-pyrimidines) in achieving pharmacological proof of concept means the allosteric approach must demonstrate clear superiority — in breadth, resistance profile, or efficacy — to justify additional development complexity. These gaps define the experimental path from EMERGING to SUPPORTED status.

---

## Key Findings

### Finding 1: Mac1 Is Genetically Validated as a Key Coronavirus Virulence Factor

Mac1 has been established through extensive reverse genetics as essential for coronavirus pathogenesis across multiple species. SARS-CoV-2 ΔMac1 replicates at near-wild-type levels in multiple cell lines but is rapidly cleared in mice with minimal pathology and no morbidity ([PMID: 37607224](https://pubmed.ncbi.nlm.nih.gov/37607224/)). This pattern — dispensable for replication, essential for virulence — is consistent across coronaviruses: SARS-CoV Mac1 mutants show attenuation and modest viral load reduction in mice despite normal cell-culture replication ([PMID: 27965448](https://pubmed.ncbi.nlm.nih.gov/27965448/)), while MHV and MERS-CoV ΔMac1 are entirely unrecoverable, indicating even greater dependence ([PMID: 37066301](https://pubmed.ncbi.nlm.nih.gov/37066301/)). Mac1 mutant viruses consistently elicit enhanced interferon and interferon-stimulated gene responses, confirming the immune evasion mechanism. This genetic validation is the bedrock upon which all Mac1 therapeutic strategies — active-site, allosteric, or degradation-based — rest.

### Finding 2: Active-Site Inhibition Shows Antiviral Activity — But Only in Immune-Competent Models

A pivotal discrepancy in the Mac1 field was resolved during this investigation. Lee et al. 2024 ([PMID: 39229055](https://pubmed.ncbi.nlm.nih.gov/39229055/)) reported that potent, selective, low-nanomolar Mac1 active-site inhibitors increase ADP-ribosylation but show **no** antiviral activity in standard cell culture or iPSC-derived pneumocytes, even in combination with IFN-γ, Mpro inhibitors, or PLpro inhibitors. This result initially cast doubt on Mac1 as a therapeutic target. However, three independent groups subsequently demonstrated that Mac1 active-site inhibitors *can* achieve antiviral activity: Suryawanshi et al. 2025 ([PMID: 41258893](https://pubmed.ncbi.nlm.nih.gov/41258893/)) showed AVI-4206 has antiviral activity in human airway organoids, macrophages, and in vivo; Pfannenstiel et al. 2024/2025 ([PMID: 39554145](https://pubmed.ncbi.nlm.nih.gov/39554145/), [PMID: 40407321](https://pubmed.ncbi.nlm.nih.gov/40407321/)) demonstrated pyrrolo-pyrimidine Mac1 inhibitors repress coronavirus replication; and Knapp et al. 2026 ([PMID: 41820535](https://pubmed.ncbi.nlm.nih.gov/41820535/)) developed a cell-based PARP15-foci assay demonstrating macrodomain inhibitor activity in living cells.

The key insight is that Mac1's immune-evasion mechanism requires immune-competent assay systems for proper evaluation. Lee et al. is now best interpreted as an outlier reflecting compound-specific or model-specific differences rather than a fundamental flaw in Mac1 targeting. This resolution both validates Mac1 as a target and **raises the bar for allosteric approaches**: they must demonstrate superiority over active-site inhibitors that already work.

### Finding 3: Conformational Dynamics — Not Just Catalysis — Are Critical for Mac1 Function

The strongest direct evidence supporting the allosteric pivot concept comes from Kerr et al. 2024 ([PMID: 38260573](https://pubmed.ncbi.nlm.nih.gov/38260573/)). Mutation of a conserved isoleucine in the GIF motif (I→A) enhances ADP-ribose binding without impairing catalytic activity, yet I-A mutant MERS-CoV and SARS-CoV-2 are highly attenuated in both cell culture and mice. This isoleucine acts as a conformational "gate" controlling ADP-ribose binding dynamics. The finding that enhanced binding is detrimental despite normal catalysis is direct evidence that Mac1's conformational landscape — not just its enzymatic output — is critical for viral fitness. This is precisely the mechanistic basis the allosteric pivot model requires: if conformational states matter independently of catalysis, then stabilizing an unproductive conformation could achieve antiviral effects that active-site inhibition alone cannot.

### Finding 4: Mac1 Has Multiple Functional Roles Beyond ADP-Ribose Hydrolysis

O'Connor et al. 2025 ([PMID: 40736256](https://pubmed.ncbi.nlm.nih.gov/40736256/)) demonstrated that different Mac1 mutations differentially affect binding versus hydrolysis and impact different stages of the viral life cycle. D1329A (adenine-binding defect) impairs viral RNA accumulation across all cell types, while N1347A (hydrolysis defect) allows normal RNA levels but reduces protein production specifically in IFN-competent macrophages. Deng et al. 2019 ([PMID: 30918076](https://pubmed.ncbi.nlm.nih.gov/30918076/)) further showed that Mac1 temperature-sensitive mutations enhance proteasome-mediated degradation of nsp3 and revealed Mac1–PLpro interaction, indicating Mac1 contributes to nsp3 protein stability. These multiple functions — binding, hydrolysis, and structural stabilization — are more consistent with Mac1 as a conformational "pivot" than as a simple enzyme, and they suggest that allosteric disruption or physical degradation could simultaneously compromise multiple Mac1 functions that active-site inhibition addresses only partially.

### Finding 5: Validated Allosteric Precedent Exists in Homologous PARP14 Macrodomain

Schuller et al. 2017 ([PMID: 28991428](https://pubmed.ncbi.nlm.nih.gov/28991428/)) and Moustakim et al. 2018 ([PMID: 29567296](https://pubmed.ncbi.nlm.nih.gov/29567296/)) identified and developed GeA-69 as a selective allosteric inhibitor of PARP14 macrodomain 2. Co-crystallization at 1.0 Å resolution (PDB: 5RSE) revealed the allosteric binding site involves residues topologically adjacent to but distinct from the ADP-ribose binding site. GeA-69 achieves selectivity for PARP14 MD2 over other human macrodomains precisely through its allosteric mechanism. This is the only validated allosteric inhibitor for any macrodomain protein, establishing that macrodomain allosteric chemistry is feasible and can achieve selectivity advantages over orthosteric approaches. Notably, this precedent was **not cited in the original hypothesis YAML** and represents a novel evidence contribution identified by this investigation.

### Finding 6: B-Factor Analysis Reveals Candidate Allosteric Communication in Mac1

{{figure:mac1_bfactor_analysis.png|caption=B-factor comparison between apo (7KQO, 0.85 Å) and ADP-ribose-bound (7KQP, 0.88 Å) Mac1 structures. The C-terminal region (residues 155–169) shows 3.6x average conformational coupling to the active site, at the topological equivalent of the PARP14 MD2 allosteric pocket.}}

Computational analysis of ultra-high-resolution Mac1 crystal structures (7KQO apo at 0.85 Å; 7KQP + ADP-ribose at 0.88 Å) revealed global rigidification upon ADP-ribose binding (mean ΔB = +2.27 Å²). The C-terminal region (residues 155–169) showed a mean ΔB of +8.27 Å², representing 3.6-fold the global average. This region is topologically distal from the ADP-ribose binding site yet shows the largest conformational response to ligand binding. Critically, this region's topological position corresponds to where the validated allosteric site resides in PARP14 MD2. While B-factor analysis alone cannot prove allostery, this conformational coupling is consistent with the hypothesis that Mac1 harbors exploitable allosteric communication pathways.

### Finding 7: 153 Co-Crystal Structures Confirm Mac1 Conformational Plasticity

Gahbauer et al. 2023 ([PMID: 36598939](https://pubmed.ncbi.nlm.nih.gov/36598939/)) determined 153 Mac1-ligand complex crystal structures at typically 1 Å resolution or better, covering 119 different scaffolds. They reported "unexpected ligand-mediated conformational changes within the active site." This is the largest crystallographic dataset for any macrodomain, providing extensive sampling of Mac1's conformational landscape. The observation that diverse small molecules can induce distinct conformational states supports the premise that Mac1 is a conformationally plastic protein amenable to allosteric or conformational-state-selective approaches.

### Finding 8: Mac1 Interactome Extends Beyond Immune Signaling

Cameron et al. 2025 ([PMID: 41279050](https://pubmed.ncbi.nlm.nih.gov/41279050/)) identified Mac1 substrates involved in DNA damage response, cytoskeletal components, cell cycle regulation, and the TRiC protein-folding complex. This broader interactome suggests that Mac1's role extends beyond simple IFN antagonism, potentially explaining why conformational dynamics (which could affect substrate selectivity) matter beyond catalytic rate. An allosteric approach that shifts Mac1's conformational ensemble might differentially affect different substrate interactions, offering therapeutic selectivity unavailable from active-site blockade.

### Finding 9: PROTAC Feasibility Is Structurally Favorable but Biologically Uncertain

Mac1's small domain size (~18.6 kDa), 15 surface lysines, and 153+ characterized ligand scaffolds make it structurally amenable to PROTAC design. The Deng et al. finding that Mac1 temperature-sensitive mutations enhance proteasome-mediated nsp3 degradation ([PMID: 30918076](https://pubmed.ncbi.nlm.nih.gov/30918076/)) provides indirect support that destabilizing Mac1 can trigger nsp3 degradation. However, critical biological uncertainties remain: Mac1 is a domain within the ~200 kDa nsp3 polyprotein, which is membrane-associated in replication organelles; no precedent exists for PROTAC targeting a domain within a larger viral polyprotein; and the timing relative to polyprotein processing is unknown. All published SARS-CoV-2 PROTACs target standalone viral proteins — Mpro ([PMID: 41780340](https://pubmed.ncbi.nlm.nih.gov/41780340/), [PMID: 41536548](https://pubmed.ncbi.nlm.nih.gov/41536548/)) or RdRp ([PMID: 41189073](https://pubmed.ncbi.nlm.nih.gov/41189073/)) — not domains within polyproteins.

### Finding 10: Patient Stratification — Mac1 Therapy Best Suited for IFN-Competent Patients

{{figure:mac1_evidence_status_table.png|caption=Comprehensive evidence status table showing the tiered classification of hypothesis claims from established through speculative, with knowledge gaps and required experiments.}}

Since Mac1's therapeutic mechanism operates through immune restoration — removing viral suppression of host ADP-ribosylation — efficacy inherently requires functional host IFN signaling. AVI-4206's antiviral effect is explicitly IFN-γ and Mac1-catalytic-activity dependent ([PMID: 41258893](https://pubmed.ncbi.nlm.nih.gov/41258893/)). However, 15–20% of critical COVID-19 patients over 70 have autoantibodies against type I IFN ([PMID: 36841740](https://pubmed.ncbi.nlm.nih.gov/36841740/), [PMID: 37196358](https://pubmed.ncbi.nlm.nih.gov/37196358/)), and 1–5% of critical cases under 60 have inborn errors of type I IFN immunity. These IFN-deficient patients — paradoxically the most severely ill — would be least likely to benefit from any Mac1-targeting strategy. This limitation applies equally to active-site, allosteric, and PROTAC approaches, but it is particularly relevant for the pivot model's claim of "broad anti-coronavirus activity."

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|--------------------------|-------------|---------|------------|
| 1 | [PMID: 38260573](https://pubmed.ncbi.nlm.nih.gov/38260573/) | In vitro + model organism | **SUPPORT** | Conformational dynamics matter beyond catalysis | I→A gate mutation enhances binding but attenuates virus | MERS-CoV, SARS-CoV-2 | **High** — strongest evidence for pivot concept |
| 2 | [PMID: 28991428](https://pubmed.ncbi.nlm.nih.gov/28991428/) | In vitro + structural | **SUPPORT** | Macrodomain allosteric sites exist | GeA-69 binds allosteric site on PARP14 MD2 (PDB:5RSE) | Human PARP14, not viral Mac1 | **High** for precedent; **uncertain** for transferability |
| 3 | [PMID: 29567296](https://pubmed.ncbi.nlm.nih.gov/29567296/) | In vitro | **SUPPORT** | Allosteric macrodomain chemistry is feasible | Sub-μM allosteric PARP14 MD2 inhibitors developed | Human PARP14 | **High** for chemistry; indirect for viral Mac1 |
| 4 | [PMID: 36598939](https://pubmed.ncbi.nlm.nih.gov/36598939/) | Structural | **SUPPORT** | Mac1 is conformationally plastic | 153 co-crystal structures show ligand-mediated conformational changes | SARS-CoV-2 Mac1 | **High** — largest macrodomain structural dataset |
| 5 | [PMID: 41258893](https://pubmed.ncbi.nlm.nih.gov/41258893/) | In vitro + model organism | **QUALIFIES** | Active-site inhibition is insufficient | AVI-4206 active-site inhibitor shows in vivo efficacy | SARS-CoV-2, immune-competent models | **High** — raises bar for allosteric approach |
| 6 | [PMID: 39229055](https://pubmed.ncbi.nlm.nih.gov/39229055/) | In vitro | **SUPPORTS** (indirectly) | Active-site inhibition alone is insufficient | Potent Mac1 inhibitors fail in standard cell culture | SARS-CoV-2, Vero/Calu-3 cells | **High** for data; now an outlier for conclusion |
| 7 | [PMID: 40736256](https://pubmed.ncbi.nlm.nih.gov/40736256/) | In vitro + model organism | **SUPPORT** | Mac1 has multiple functional modes | Binding vs. hydrolysis mutations affect different viral stages | MHV | **High** — clean genetic separation |
| 8 | [PMID: 30918076](https://pubmed.ncbi.nlm.nih.gov/30918076/) | In vitro | **SUPPORT** | Mac1 contributes to nsp3 stability | ts-mutations enhance proteasome-mediated nsp3 degradation | MHV | **Medium** — indirect PROTAC support |
| 9 | [PMID: 41279050](https://pubmed.ncbi.nlm.nih.gov/41279050/) | In vitro (proteomics) | **SUPPORT** | Mac1 interactome is broad | Substrates include DNA damage, cytoskeleton, TRiC complex | SARS-CoV-2 in A549 cells | **Medium** — co-IP, needs validation |
| 10 | [PMID: 33158944](https://pubmed.ncbi.nlm.nih.gov/33158944/) | In vitro + structural | **SUPPORT** | Pan-CoV Mac1 conservation | Similar folds and μM ADPr affinity across 3 CoVs | SARS-CoV-2, SARS-CoV, MERS-CoV | **High** — direct comparison |
| 11 | [PMID: 37607224](https://pubmed.ncbi.nlm.nih.gov/37607224/) | Model organism | **SUPPORT** (target validation) | Mac1 is essential for pathogenesis | ΔMac1 SARS-CoV-2 cleared rapidly in mice | SARS-CoV-2, K18-hACE2 mice | **High** — gold-standard reverse genetics |
| 12 | [PMID: 37196358](https://pubmed.ncbi.nlm.nih.gov/37196358/) | Human clinical/genetic | **QUALIFIES** | Mac1 therapy has broad applicability | 15–20% of critical elderly patients have anti-IFN-I autoAbs | Severe COVID-19 | **High** — limits patient population |
| 13 | [PMID: 34686999](https://pubmed.ncbi.nlm.nih.gov/34686999/) | Structural (NMR) | **SUPPORT** (tool) | CoV macrodomain dynamics can be measured | Backbone NMR assignments for SARS-CoV and MERS-CoV MDs | Free and ADPr-bound states | **Medium** — enables future studies |
| 14 | [PMID: 41565251](https://pubmed.ncbi.nlm.nih.gov/41565251/) | Community challenge | **SUPPORT** (tractability) | Mac1 is a tractable drug target | CACHE Challenge #3 — community-wide hit-finding | SARS-CoV-2 Mac1 | **High** |
| 15 | [PMID: 31095648](https://pubmed.ncbi.nlm.nih.gov/31095648/) | In vitro + model organism | **SUPPORT** (mechanism) | Mac1 counters PARP-mediated response | PARP12/14 specifically inhibit Mac1-mutant CoV | MHV in macrophages | **High** — direct mechanistic link |
| 16 | Literature search (2026) | Absence of evidence | **REFUTES** (allosteric site) | Allosteric site exists on Mac1 | No study identifies allosteric site on any viral Mac1 | Systematic search | **High** confidence in absence |
| 17 | Literature search (2026) | Absence of evidence | **REFUTES** (PROTAC) | Mac1 PROTAC is feasible | No Mac1 PROTAC designed, synthesized, or tested | Systematic search | **High** confidence in absence |
| 18 | Computational (this analysis) | B-factor analysis | **SUPPORT** (indirect) | Mac1 has allosteric communication | C-terminal res 155-169 shows 3.6x average conformational coupling | SARS-CoV-2 (7KQO/7KQP) | **Medium** — computational, not experimental |

{{figure:mac1_evidence_map.png|caption=Evidence map showing established (green), emerging (yellow), and speculative (red) tiers of the Mac1 allosteric pivot hypothesis, with connections between supporting and qualifying evidence.}}

---

## Mechanistic Causal Chain

The hypothesis implies the following causal chain from upstream infection to therapeutic intervention:

```
SARS-CoV-2 INFECTION
        │
        ▼
  nsp3 polyprotein expression → Mac1 domain active
  [ESTABLISHED: structural + genetic evidence]
        │
        ▼
  Mac1 HYDROLYZES host mono-ADP-ribose marks
  (placed by PARP9/10/12/14 as antiviral response)
  [ESTABLISHED: PMID:33158944, PMID:32511412]
        │
        ▼
  SUPPRESSION of IFN/ISG responses
  + broader interactome effects (DNA damage, cytoskeleton,
    protein folding via TRiC complex)
  [ESTABLISHED for IFN: PMID:37607224, PMID:31095648]
  [EMERGING for broader interactome: PMID:41279050]
        │
        ▼
  Enhanced viral replication + immune evasion IN VIVO
  (dispensable in standard cell culture)
  [ESTABLISHED: PMID:37607224, PMID:27965448]
        │
        ▼
  SEVERE COVID-19 PATHOGENESIS
  (pneumonia, hyperinflammation, organ damage)
        │
        ▼
  ═══════════════════════════════════════════════
  THERAPEUTIC INTERVENTION POINTS:
  ═══════════════════════════════════════════════
        │
        ├──► ACTIVE-SITE INHIBITION
        │    (AVI-4206, pyrrolo-pyrimidines)
        │    Blocks catalysis; requires IFN competence
        │    STATUS: EMERGING → VALIDATED (PMID:41258893)
        │
        ├──► ALLOSTERIC STABILIZATION
        │    Lock Mac1 in unproductive conformation
        │    Precedent: GeA-69 on PARP14 MD2 (PMID:28991428)
        │    Candidate region: C-terminal res 155-169
        │    Potential: affect multiple Mac1 functions
        │    STATUS: SPECULATIVE (no direct evidence)
        │
        └──► PROTAC-BASED DEGRADATION
             Degrade nsp3 via Mac1 warhead
             Support: ts-mutations degrade nsp3 (PMID:30918076)
             Challenge: nsp3 ~200 kDa, membrane-bound
             STATUS: SPECULATIVE (no Mac1 PROTAC exists)
```

**Strength of causal links:**
- **Strong (established):** Mac1 hydrolyzes host ADP-ribose → suppresses innate immunity → promotes pathogenesis. Supported by genetics in 4+ coronavirus species, biochemistry, proteomics, and in vivo models.
- **Emerging:** Active-site inhibition restores ADP-ribosylation and achieves antiviral effects in immune-competent models. The isoleucine gate shows conformational dynamics matter beyond catalysis.
- **Missing causal steps (key gaps):**
  1. *Mac1 conformational dynamics → viral fitness*: Supported by isoleucine gate data but the molecular mechanism of how conformational gating promotes replication is unknown
  2. *Allosteric site existence on viral Mac1*: Inferred from PARP14 precedent and B-factor analysis; no direct evidence
  3. *Allosteric inhibition → antiviral effect*: Entirely speculative; no allosteric Mac1 compounds exist to test
  4. *PROTAC engagement of Mac1 within nsp3 polyprotein context*: No precedent; structurally plausible but biologically untested

---

## Patient Subtypes and Clinical Context

**Most likely to benefit from Mac1-targeting therapy:**
- **IFN-competent patients with moderate-to-severe COVID-19** whose immune response is being actively suppressed by viral Mac1
- **Patients in the early-to-mid disease course** where innate immune suppression is ongoing, before the cytokine storm phase
- **Immunocompetent individuals of any age** who develop symptomatic SARS-CoV-2 infection

**Least likely to benefit:**
- **Patients with anti-IFN autoantibodies** (15–20% of critical cases over 70; [PMID: 37196358](https://pubmed.ncbi.nlm.nih.gov/37196358/))
- **Patients with inborn errors of type I IFN immunity** (1–5% of critical cases under 60)
- **Late-stage ARDS/cytokine storm patients** where pathology is immune-driven rather than virus-driven

**Tissue and cell type relevance:**
- **Macrophages** — strongest AVI-4206 antiviral activity observed here ([PMID: 41258893](https://pubmed.ncbi.nlm.nih.gov/41258893/))
- **Airway epithelial cells** — organoid efficacy demonstrated
- **IFN-responsive tissues** generally

**Biomarker implications:**
- Pre-treatment IFN-α levels or anti-IFN autoantibody status could serve as companion diagnostics
- ADP-ribosylation status of Mac1 substrates could serve as pharmacodynamic biomarkers

---

## Knowledge Gaps

### Gap 1: No Allosteric Site Demonstrated on Viral Mac1
- **Scope:** Central to the hypothesis — the allosteric pivot model requires an exploitable allosteric site on viral Mac1
- **Why it matters:** Without a demonstrated allosteric site, the model remains extrapolation from PARP14 homology
- **What was checked:** Systematic PubMed searches for "macrodomain allosteric," "macrodomain cryptic pocket," "macrodomain conformational dynamics allosteric" — all returned zero results for viral macrodomains. However, PARP14 MD2 allosteric site (PDB:5RSE) and Mac1 B-factor analysis provide indirect structural evidence
- **What would resolve it:** (1) MD simulations with enhanced sampling to identify cryptic pockets; (2) Fragment screening targeting non-active-site regions; (3) NMR CPMG relaxation dispersion on SARS-CoV-2 Mac1 to detect conformational exchange; (4) Re-analysis of the 153 co-crystal structures for distal conformational changes

### Gap 2: No Mac1 PROTAC Designed or Tested
- **Scope:** One of the two proposed therapeutic modalities in the hypothesis
- **Why it matters:** Mac1 exists within the ~200 kDa membrane-associated nsp3; it is unknown whether a PROTAC warhead binding Mac1 can engage an E3 ligase to ubiquitinate and degrade the full nsp3
- **What was checked:** Literature on antiviral PROTACs ([PMID: 40871554](https://pubmed.ncbi.nlm.nih.gov/40871554/)) — existing viral PROTACs target standalone viral proteins, not domains within polyproteins
- **What would resolve it:** Design and test Mac1-recruiting PROTAC using existing active-site ligands as warheads; measure nsp3 protein levels by Western blot in infected cells

### Gap 3: Mechanism of Isoleucine Gate Attenuation Unknown
- **Scope:** The I→A mutation attenuates virus despite enhancing binding and preserving catalysis — but *why* is unknown
- **Why it matters:** Understanding this mechanism would reveal whether Mac1's conformational gating controls substrate selectivity, protein interactions, or processivity — informing allosteric drug design
- **What was checked:** [PMID: 38260573](https://pubmed.ncbi.nlm.nih.gov/38260573/) describes the phenotype but not the molecular mechanism
- **What would resolve it:** Comparative interactomics of WT vs. I-A Mac1; MD simulations of gating dynamics; NMR comparison of conformational ensembles

### Gap 4: No Clinical Trial Data for Any Mac1 Inhibitor
- **Scope:** All Mac1 inhibitor data are preclinical
- **Why it matters:** Human pharmacology, resistance evolution, and clinical efficacy are entirely unknown
- **What was checked:** No clinical trial entries found; AVI-4206 is the most advanced compound (in vivo mouse data only)
- **What would resolve it:** IND-enabling studies for AVI-4206 or CACHE3-derived leads

### Gap 5: Resistance Evolution Under Mac1 Inhibitor Pressure Not Studied
- **Scope:** No serial passage experiments with Mac1 inhibitors have been published
- **Why it matters:** The hypothesis claims allosteric approaches may resist escape mutations better than active-site inhibitors, but no resistance data exist for either approach
- **What was checked:** Resistance studies exist for Mpro inhibitors ([PMID: 40462918](https://pubmed.ncbi.nlm.nih.gov/40462918/), [PMID: 41279697](https://pubmed.ncbi.nlm.nih.gov/41279697/)) but not for Mac1 inhibitors
- **What would resolve it:** Serial passage of SARS-CoV-2 under Mac1 inhibitor selection pressure; whole-genome sequencing of escape mutants

### Gap 6: Lee et al. vs. Suryawanshi et al. Discrepancy Not Fully Resolved
- **Scope:** Lee et al. found no antiviral activity even with IFN-γ co-treatment, while Suryawanshi et al. found IFN-γ-dependent activity
- **Why it matters:** If the discrepancy reflects target-biology complexity rather than compound-specific differences, it affects the entire field
- **What was checked:** Compared compound structures, potencies, assay conditions, and cell models
- **What would resolve it:** Head-to-head comparison of all compound series in identical immune-competent models

### Gap 7: Mac1-PLpro Interaction Not Confirmed in SARS-CoV-2
- **Scope:** Mac1–PLpro interaction and structural stabilization demonstrated only in MHV ([PMID: 30918076](https://pubmed.ncbi.nlm.nih.gov/30918076/))
- **Why it matters:** If Mac1-PLpro interaction is not conserved in SARS-CoV-2, the PROTAC-triggered nsp3 degradation pathway may not apply
- **What would resolve it:** Co-IP or proximity ligation assay for Mac1-PLpro in SARS-CoV-2-infected cells

---

## Alternative Models

### 1. Active-Site Catalytic Inhibition Model (COMPETING)
- **Relationship:** Direct alternative to the allosteric pivot model
- **Description:** Conventional competitive inhibition of Mac1's ADP-ribosylhydrolase activity at the active site is sufficient for therapeutic benefit, provided the right biological model (immune-competent, IFN-primed) is used
- **Evidence:** AVI-4206 ([PMID: 41258893](https://pubmed.ncbi.nlm.nih.gov/41258893/)); pyrrolo-pyrimidine inhibitors ([PMID: 39554145](https://pubmed.ncbi.nlm.nih.gov/39554145/))
- **Strength:** Has pharmacological proof of concept; simpler medicinal chemistry
- **Weakness:** May be vulnerable to resistance; addresses only catalytic function

### 2. Mac1 as Structural Scaffold Model (COMPLEMENTARY)
- **Relationship:** Complementary — focuses on Mac1's structural role in nsp3
- **Description:** Mac1 functions primarily as a structural scaffold stabilizing the nsp3 multi-domain complex. Disrupting Mac1 structure causes nsp3 instability and proteasomal degradation
- **Evidence:** Deng et al. 2019 ([PMID: 30918076](https://pubmed.ncbi.nlm.nih.gov/30918076/)) — ts-mutations enhance nsp3 degradation
- **Strength:** Explains why Mac1 deletion is lethal for MHV/MERS-CoV; supports PROTAC rationale
- **Weakness:** Limited to MHV data; SARS-CoV-2 nsp3 dependence on Mac1 structure unclear

### 3. PARP-Specific Immune Restoration Model (UPSTREAM)
- **Relationship:** Upstream mechanism explaining why Mac1 inhibition works
- **Description:** Mac1's critical function is specifically countering PARP12 and PARP14-mediated ADP-ribosylation
- **Evidence:** Grunewald et al. 2019 ([PMID: 31095648](https://pubmed.ncbi.nlm.nih.gov/31095648/))
- **Strength:** Identifies specific molecular players; explains IFN-dependence
- **Weakness:** Doesn't address why active-site inhibition fails in some models

### 4. Multi-Target nsp3 Strategy (PARALLEL)
- **Relationship:** Parallel strategy targeting nsp3 broadly
- **Description:** PROTACs targeting other nsp3 domains (e.g., PLpro) could degrade the entire nsp3 polyprotein, eliminating Mac1 function along with other essential viral activities
- **Evidence:** PLpro inhibitors exist; PROTAC technology proven for Mpro/RdRp
- **Strength:** Eliminates multiple viral functions simultaneously
- **Weakness:** nsp3 PROTACs not demonstrated; very large target

### 5. Combination Therapy Model (COMPLEMENTARY)
- **Relationship:** Encompasses the allosteric pivot as one component
- **Description:** Mac1 inhibitors combined with direct-acting antivirals for synergistic effects and reduced resistance risk
- **Evidence:** Suryawanshi et al. explicitly propose this approach ([PMID: 41258893](https://pubmed.ncbi.nlm.nih.gov/41258893/))
- **Strength:** Independent mechanisms reduce cross-resistance probability
- **Weakness:** Polypharmacy complexity; PK/PD optimization challenges

---

## Discriminating Tests

### Test 1: Cryptic Pocket Discovery on SARS-CoV-2 Mac1
- **Method:** Gaussian accelerated MD (GaMD) or metadynamics simulations (>10 μs aggregate) on Mac1 apo structure; mixed-solvent MD with pharmacophore probes; fragment screening by X-ray crystallography targeting non-active-site regions
- **Focus region:** C-terminal residues 155–169 (identified by B-factor analysis)
- **Expected result if hypothesis correct:** ≥1 druggable pocket (>200 Å³) identified at topological equivalent of PARP14 MD2 allosteric site
- **Expected result if hypothesis incorrect:** No stable, druggable cryptic pockets outside the active site
- **Impact:** Would directly confirm or refute the structural foundation of the allosteric pivot model

### Test 2: NMR Conformational Dynamics Mapping
- **Method:** ¹⁵N CPMG relaxation dispersion and CEST on ¹⁵N-labeled SARS-CoV-2 Mac1 ± ADP-ribose ± active-site inhibitor
- **Expected result if correct:** μs–ms timescale conformational exchange in residues 155–169, modulated by active-site ligands
- **Expected result if incorrect:** No significant exchange outside active-site residues
- **Leverage:** Existing SARS-CoV/MERS-CoV NMR assignments ([PMID: 34686999](https://pubmed.ncbi.nlm.nih.gov/34686999/)) can guide SARS-CoV-2 studies

### Test 3: Mac1 PROTAC Proof of Concept
- **Method:** Design bifunctional molecule linking Mac1 warhead (CACHE3 hits or AVI-4206 scaffold) to CRBN/VHL E3 ligase ligand
- **Readouts:** (a) Isolated Mac1 degradation; (b) nsp3 degradation in transfection; (c) antiviral activity during SARS-CoV-2 infection
- **Model:** HEK293T for initial degradation; immune-competent macrophages/organoids for antiviral testing
- **Key control:** Non-degrading epimer control to distinguish degradation from inhibition

### Test 4: Resistance Evolution Comparison
- **Method:** Serial passage of SARS-CoV-2 under active-site inhibitor vs. allosteric inhibitor (once available) vs. combination; 20+ passages with escalating drug concentration
- **Readout:** Whole-genome sequencing of escape mutants; fitness cost of resistance mutations
- **Benchmark:** Nirmatrelvir resistance (L50F/R188G) for comparison ([PMID: 40462918](https://pubmed.ncbi.nlm.nih.gov/40462918/))
- **Impact:** Tests the resistance-advantage claim directly

### Test 5: Patient Stratification Biomarker Validation
- **Method:** Correlate IFN-I autoantibody status with Mac1 inhibitor response in clinical/preclinical cohorts
- **Biomarker:** Anti-IFN-α2/ω autoantibodies (ELISA); IFN-stimulated gene score
- **Impact:** Defines the clinically relevant patient population for any Mac1 therapy

### Test 6: Substrate-Specific Functional Validation
- **Method:** CRISPR knockout of candidate Mac1 substrates (Cameron et al. 2025) in A549 cells → test WT SARS-CoV-2 replication
- **Expected result if correct:** Specific substrate knockouts phenocopy Mac1 deletion, enabling targeted Mac1 modulation

---

## Evidence Tiering Summary

| Tier | Claims | Evidence Level |
|------|--------|---------------|
| **ESTABLISHED** | Mac1 is a CoV virulence factor; Mac1 counters PARP12/14-mediated ADP-ribosylation; Mac1 deletion attenuates SARS-CoV-2 in vivo; active-site inhibitors (AVI-4206) show in vivo efficacy | Multiple independent groups; genetic + pharmacological validation |
| **EMERGING** | Conformational dynamics matter beyond catalysis (Ile gate); Mac1 interactome extends beyond immune signaling; macrodomain fold CAN harbor allosteric sites (PARP14 MD2); Mac1 C-terminal region shows conformational coupling; 153 co-crystal structures confirm Mac1 plasticity | Strong but indirect support; requires direct validation on viral Mac1 |
| **SPECULATIVE** | Mac1 has a druggable allosteric site; allosteric stabilization restores host ADP-ribosylation; Mac1 PROTAC degrades nsp3; pan-CoV activity via conformational-pivot chemistry; resistance advantage over active-site drugs | No direct evidence; structurally precedented but experimentally unvalidated |

---

## Curation Leads

*The following are candidate updates for the Knowledge Base, requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 38260573](https://pubmed.ncbi.nlm.nih.gov/38260573/)** (Kerr et al. 2024) — Upgrade to **key mechanistic evidence**. Verified snippet: *"Despite increased ADP-ribose binding, I-A mutant MERS-CoV and SARS-CoV-2 were highly attenuated in both cell culture and mice, indicating that this isoleucine residue acts as a gate that controls ADP-ribose binding for efficient virus replication."* — Strongest support for conformational pivot concept.

2. **[PMID: 41258893](https://pubmed.ncbi.nlm.nih.gov/41258893/)** (Suryawanshi et al. 2025) — Add as **qualifying evidence** (not in seed YAML). Verified snippet: *"Standard cellular models indicate that AVI-4206 has high target engagement and can weakly inhibit viral replication in a gamma interferon- and Mac1 catalytic activity-dependent manner. However, a stronger antiviral effect for AVI-4206 is observed in human airway organoids and peripheral blood monocyte-derived macrophages."*

3. **[PMID: 28991428](https://pubmed.ncbi.nlm.nih.gov/28991428/)** (Schuller et al. 2017) — Add as **supporting evidence** for allosteric precedent. Verified snippet: *"Co-crystallization of a GeA-69 analogue with PARP14 MD2 revealed an allosteric binding mechanism explaining its selectivity over other human macrodomains."*

4. **[PMID: 40736256](https://pubmed.ncbi.nlm.nih.gov/40736256/)** (O'Connor et al. 2025) — Add as **supporting evidence** for multiple Mac1 functions. Verified snippet: *"D1329A displayed a large defect in the accumulation of viral RNA compared to WT or N1347A in all cells tested. Alternatively, N1347A infection produced normal levels of viral RNA but produced reduced levels of viral protein in interferon-competent bone marrow-derived macrophages."*

5. **[PMID: 41279050](https://pubmed.ncbi.nlm.nih.gov/41279050/)** (Cameron et al. 2025) — Add as **supporting evidence** for interactome breadth. Verified snippet: *"We identified interactions between Mac1 and ADP-ribosylated substrates involved in DNA damage response, cytoskeletal components, and cell cycle regulation."*

6. **[PMID: 30918076](https://pubmed.ncbi.nlm.nih.gov/30918076/)** (Deng et al. 2019) — Add as **supporting evidence** for structural scaffold role. Verified snippet: *"Expression studies of the macrodomain-PLP2 portion of nsp3 indicate that the ts mutations enhance proteasome-mediated degradation of the protein."*

7. **[PMID: 36598939](https://pubmed.ncbi.nlm.nih.gov/36598939/)** (Gahbauer et al. 2023) — Add as **supporting evidence** for conformational plasticity. Verified snippet: *"Our analyses discovered selective and cell-permeable molecules, unexpected ligand-mediated conformational changes within the active site, and key inhibitor motifs that will template future drug development against Mac1."*

8. **[PMID: 34686999](https://pubmed.ncbi.nlm.nih.gov/34686999/)** (Tsika et al. 2022) — Add as **enabling evidence**. Verified snippet: *"SARS-CoV and MERS-CoV Macro Domains (MDs) exhibit topological and conformational features that resemble the nsP3b macro (or "X") domain of SARS-CoV-2."*

9. **[PMID: 39229055](https://pubmed.ncbi.nlm.nih.gov/39229055/)** (Lee et al. 2024) — Add as **qualifying evidence**. Verified snippet: *"Using our inhibitors, we show that inhibition of nsp3-mac1 increases ADP-ribosylation, but surprisingly does not translate to demonstrable antiviral activity in cell culture and iPSC-derived pneumocyte models."*

10. **[PMID: 37196358](https://pubmed.ncbi.nlm.nih.gov/37196358/)** (Cobat et al. 2023) — Add as **qualifying evidence** for patient stratification. Verified snippet: *"Sequencing studies focusing on rare variants with a strong effect have been particularly successful, identifying inborn errors of type I interferon (IFN) immunity in 1-5% of unvaccinated patients with critical pneumonia, and their autoimmune phenocopy, autoantibodies against type I IFN, in another 15-20% of cases."*

### Candidate Pathophysiology Nodes/Edges

- **Node:** Mac1 conformational gating (Ile residue in GIF motif) → viral fitness
- **Edge:** Mac1 ⟶ [removes ADP-ribose from] ⟶ PARP12/PARP14 targets ⟶ [suppresses] ⟶ IFN-β production
- **Edge:** Mac1 ⟶ [stabilizes] ⟶ nsp3 protein (Mac1-PLpro interaction) ⟶ [enables] ⟶ replication complex assembly
- **Edge:** Mac1 ⟶ [removes ADP-ribose from] ⟶ TRiC complex / DNA damage response proteins (novel, [PMID: 41279050](https://pubmed.ncbi.nlm.nih.gov/41279050/))
- **Edge (negative):** IFN-I deficiency (autoAbs or inborn errors) ⟶ [reduces] ⟶ Mac1 inhibitor efficacy

### Candidate Ontology Terms

- **Cell types:** Bone marrow-derived macrophages (BMDMs), human airway organoid cells, peripheral blood monocyte-derived macrophages, A549, HEK293T
- **Biological processes:** Mono-ADP-ribosylation (GO:0140289), interferon-alpha/beta signaling (GO:0060337), viral immune evasion (GO:0030683), proteasome-mediated protein catabolism (GO:0043161)
- **Molecular functions:** ADP-ribosylhydrolase activity (GO:0140457), ADP-ribose binding (GO:0043522)

### Candidate Status Change

- **Current status:** EMERGING
- **Recommended status:** EMERGING (retain, with upgraded confidence)
- **Rationale:** The hypothesis correctly identifies Mac1 conformational dynamics as critical (isoleucine gate data is strong), the Mac1 interactome breadth supports the "pivot point" framing, and the PARP14 MD2 allosteric precedent provides structural rationale absent from the original hypothesis. However, the specific claims about allosteric druggability and PROTAC feasibility have no direct evidence. Consider splitting into sub-claims:
  - **Established:** Mac1 conformational dynamics (beyond catalysis) are critical for viral fitness
  - **Emerging:** Mac1 serves as a host interactome pivot point with diverse substrates
  - **Speculative:** Allosteric stabilization of Mac1 conformational states is therapeutically tractable
  - **Speculative:** Mac1-targeting PROTACs can achieve what active-site inhibitors cannot

### Candidate Knowledge Gaps for KB

1. **No allosteric site identified on Mac1** — Central gap; no MD or experimental evidence
2. **No Mac1 PROTAC exists** — No medicinal chemistry effort reported
3. **Unknown critical immune-evasion substrates** — Interactome broad but functional validation missing
4. **Lee et al. vs. Suryawanshi et al. discrepancy** — Model-dependent efficacy not fully explained
5. **No clinical data** — All evidence is preclinical; no Mac1 inhibitor in clinical trials
6. **Mac1-PLpro interaction in SARS-CoV-2** — Only demonstrated in MHV; unknown if conserved
7. **No resistance evolution data** — No serial passage with Mac1 inhibitors published

### Discussion Prompts for Curators

- Should the allosteric pivot model be split into two sub-hypotheses (allosteric inhibition vs. PROTAC degradation) given their very different evidence bases and feasibility profiles?
- Given that active-site inhibitors now show in vivo efficacy, should the KB add an explicit "active-site Mac1 inhibition" hypothesis at SUPPORTED status as the primary comparator?
- How should the IFN-dependence limitation be represented — as a qualifier on the Mac1 hypothesis generally, or as a separate patient-stratification node?
- The correction notice for Pfannenstiel et al. ([PMID: 41979330](https://pubmed.ncbi.nlm.nih.gov/41979330/)) should be reviewed — does it affect the core antiviral activity claim?
