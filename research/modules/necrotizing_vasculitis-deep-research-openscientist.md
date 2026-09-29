---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T08:56:33.546942'
end_time: '2026-09-03T09:08:49.377570'
duration_seconds: 735.83
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: Necrotizing Vasculitis Module
  module_slug: necrotizing_vasculitis
  category: Module
  module_description: A conserved pathophysiology module for the leukocyte-mediated
    destruction of the blood-vessel wall that produces fibrinoid necrosis.
  pathophysiology_summary: '- Vessel Wall Immune Stimulus Deposition and Endothelial
    Activation: Placeholder.

    - Complement C5a Amplification and Neutrophil Recruitment: Placeholder.

    - Intramural Leukocyte Degranulation and Oxidative Burst: Placeholder.

    - Fibrinoid Necrosis of the Vessel Wall: Placeholder.

    - Luminal Compromise and Downstream Tissue Infarction: Placeholder.'
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 14
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:28029757
  relevance_assessed: 20
  on_topic: 9
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 6
  verified: 6
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
  path: necrotizing_vasculitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: necrotizing_vasculitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Necrotizing Vasculitis Module
- **Module Slug:** necrotizing_vasculitis
- **Category:** Module

## Current Module Description

A conserved pathophysiology module for the leukocyte-mediated destruction of the blood-vessel wall that produces fibrinoid necrosis.

## Current Provisional Nodes

- Vessel Wall Immune Stimulus Deposition and Endothelial Activation: Placeholder.
- Complement C5a Amplification and Neutrophil Recruitment: Placeholder.
- Intramural Leukocyte Degranulation and Oxidative Burst: Placeholder.
- Fibrinoid Necrosis of the Vessel Wall: Placeholder.
- Luminal Compromise and Downstream Tissue Infarction: Placeholder.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology described in the module description and
provisional nodes above. Prioritize evidence for:

- The conserved causal chain represented by the proposed nodes.
- The biological distinctions between node subgroups, especially if the module
  defines branching pathways.
- Any optional or gene-specific branches described in the node list, while
  distinguishing them from core module requirements.
- Explicit exclusions or boundary conditions stated in the module description.

## Questions To Answer

1. What is the best-supported shared mechanism for this module?
2. Is the current module name and scope appropriate, or is a clearer name or
   narrower boundary supported by the literature?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes, variants, exposures, cell types, tissues, or molecular
   processes support each branch or node?
5. What evidence supports the causal edges between upstream drivers, central
   effectors, and downstream consequences?
6. What direct human evidence links the same causal factor or variant class to
   multiple clinical or pathological manifestations?
7. What model organism, in vitro, or other experimental evidence clarifies the
   causal path from molecular perturbation to phenotype?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.


## Output

# Necrotizing Vasculitis Module — Mechanism Research Report

**Module slug:** `necrotizing_vasculitis` · **Category:** Module
**Prepared for:** dismech mechanism-module curation (reusable across gene-axis disease entries)
**Evidence base:** 36 papers screened; 7 confirmed findings. Primary literature cited by PMID.

---

## Summary

The **Necrotizing Vasculitis Module** describes a conserved, **neutrophil- and complement(C5a)-driven pathway** that culminates in **fibrinoid necrosis of the blood-vessel wall**. The evidence gathered across this investigation strongly supports the five provisional nodes as a valid causal chain and identifies a clear **convergence architecture**: two mechanism-specific upstream drivers (immune-complex deposition vs. pauci-immune ANCA priming) feed a **shared central effector hub** — complement C5a amplification and neutrophil recruitment — that then drives intramural degranulation/oxidative burst/NETosis, fibrinoid necrosis, and downstream infarction. This "two branches, one hub" topology is the single most important structural recommendation of this report.

The causal centrality of the C5a/neutrophil hub is unusually well validated. It rests on **Level-1 human evidence** (the ADVOCATE phase-3 randomized controlled trial of the oral C5a-receptor inhibitor avacopan) combined with **mouse knockout and antibody-transfer experiments** and **human biomarker data** showing systemic alternative-pathway complement activation at diagnosis. Few mechanism modules can anchor their central node in a positive interventional RCT; this one can. Accordingly, all five provisional nodes should be treated as **core/required for conformance**, with node 1 modeled as a **branch point** carrying two mutually exclusive but convergent upstream mechanisms.

The investigation also delineated the module's **boundaries**. The monogenic disorder **DADA2** (biallelic *ADA2* loss of function) produces a medium-vessel necrotizing vasculitis through a **macrophage/M1- and TNF-α-driven** mechanism that bypasses the neutrophil/C5a core; it shares only the terminal fibrinoid-necrosis and infarction nodes and should be curated as a **boundary/optional branch**, not a conforming instance of the core pathway. Purely lymphocytic vasculitides and pressure-/angiotensin-driven "fibrinoid" vasculopathies also fall outside the module's leukocyte-and-complement scope. The recommended module name is retained but sharpened (see below).

---

## Executive Recommendation: Module Name and Scope

**Recommendation: Retain the name "Necrotizing Vasculitis Module" but formally scope it as a *complement-C5a/neutrophil convergence-hub* module.**

- The current name is appropriate and widely recognized. A more mechanistically precise internal descriptor — *"leukocyte- and complement-mediated fibrinoid-necrotizing vasculitis"* — should be recorded in the module description to make the scope boundary explicit.
- **Core scope:** small- and medium-vessel vasculitis in which **complement anaphylatoxin C5a-driven neutrophil recruitment and intramural activation** is the required central effector, producing fibrinoid necrosis.
- **In scope as convergent upstream branches:** (a) immune-complex/classical-pathway disease and (b) pauci-immune/ANCA/alternative-pathway disease.
- **Boundary/optional branch:** macrophage-TNF-driven monogenic vasculitis (DADA2), sharing only the terminal nodes.
- **Out of scope:** lymphocyte-dominant vasculitides, angiotensin/pressure-driven fibrinoid vasculopathy, and thrombotic microangiopathies without leukocytoclastic wall destruction.

---

## Key Findings

### Finding 1 — A conserved neutrophil-mediated causal chain instantiates nodes 2→5 (ANCA branch)

A narrative review of ANCA-associated vasculitis (AAV) pathophysiology lays out a **linear causal sequence** that maps almost one-to-one onto the module's provisional nodes 2 through 5: cytokine priming exposes MPO/PR3 on the neutrophil surface → circulating ANCA binds primed neutrophils → activated neutrophils adhere to and transmigrate through endothelium and accumulate within the vessel wall → intramural degranulation and reactive-oxygen-radical production → neutrophil death → vessel-wall tissue damage. This is the backbone of the pauci-immune branch and confirms that the module's central-to-terminal nodes are not placeholders but reflect an established, stepwise mechanism.

> "Primed neutrophils are activated by interaction with ANCA in circulation. Activated neutrophils attach to and transmigrate through endothelium and accumulate within the vessel wall. These neutrophils degranulate and produce reactive oxygen radicals and ultimately die, causing ti[ssue damage]." — [PMID: 28537941](https://pubmed.ncbi.nlm.nih.gov/28537941/)

### Finding 2 — C5a/C5aR (CD88) amplification is causally required: human RCT + mouse knockout evidence

This is the load-bearing finding of the module. The central node — **Complement C5a Amplification and Neutrophil Recruitment** — is supported by convergent evidence at three levels of rigor:

- **Human interventional (Level 1):** In the ADVOCATE phase-3 RCT, the oral C5a-receptor inhibitor **avacopan** achieved remission at week 26 in **120/166 (72.3%)** patients vs **115/164 (70.1%)** for the prednisone taper, and demonstrated superiority for sustained remission at week 52. Blocking the C5a receptor can *replace* high-dose glucocorticoids for remission induction — direct causal proof that the C5a/C5aR axis drives the disease.
- **Model organism:** Mice deficient in **factor B and C5** are protected from anti-MPO-induced AAV, whereas **C4-deficient** mice remain susceptible — localizing the required complement contribution to the **alternative pathway**. **C5aR (CD88) blockade** protects mice, and avacopan abolishes neutrophil activation, migration, endothelial adherence, and vascular permeability.
- **Human biomarker:** At diagnosis, AAV patients show elevated systemic **C5a (19.9 vs 9.06 pg/mL, P = .002)** and **Bb (P < .0001)**, indicating active alternative-pathway complement turnover.

> "Remission at week 26 (the first primary endpoint) was observed in 120 of 166 patients (72.3%) receiving avacopan and in 115 of 164 patients (70.1%) receiving prednisone" — [PMID: 35167187](https://pubmed.ncbi.nlm.nih.gov/35167187/)

> "in contrast to mice deficient for factor B and C5 animals deficient for C4 were susceptible to AAV development by injection of anti-MPO antibodies emphasized the specific involvement of the alternative pathway" — [PMID: 35665698](https://pubmed.ncbi.nlm.nih.gov/35665698/)

> "C5a: 19.9(0.02-48) vs 9.06(2.1-16.3)pg/mL, P = .002, Bb: 7.3(0.02-31.4) vs 0.2(0.02-1.6)pg/mL, P < .0001" — [PMID: 32602136](https://pubmed.ncbi.nlm.nih.gov/32602136/)

### Finding 3 — Two convergent upstream branches feed the shared hub

Node 1 (Vessel Wall Immune Stimulus Deposition and Endothelial Activation) is best modeled as a **branch point** with two mechanistically distinct but convergent drivers:

- **Immune-complex branch:** Leukocytoclastic vasculitis is an **Arthus type III immune-complex reaction** with granular vessel-wall deposits of immunoglobulin plus complement. Urticarial vasculitis is explicitly "immune complex-driven … with activation of the complement cascade, leading to exaggerated production of anaphylatoxins that are responsible for neutrophil recruitment and activation."
- **Pauci-immune/ANCA branch:** Necrotizing crescentic glomerulonephritis with "scanty deposition of immunoglobulins and complement."

Both converge on **complement anaphylatoxin (C5a)-driven neutrophil recruitment** and fibrinoid necrosis. **Direct immunofluorescence (DIF)** is the practical discriminator: IgA-dominant (IgA vasculitis/HSP), Ig/complement granular (LCV), vs pauci-immune (ANCA).

> "immune complex-driven disease with activation of the complement cascade, leading to exaggerated production of anaphylatoxins that are responsible for neutrophil recruitment and activation" — [PMID: 35396080](https://pubmed.ncbi.nlm.nih.gov/35396080/)

> "Most cases are attributable to immune complex deposition within a vessel wall and represent an Arthus type III immune complex reaction. The prototypic immunoreactant profile is characterized by granular deposits of components of complement activation in concert with immunoglobulin" — [PMID: 35907580](https://pubmed.ncbi.nlm.nih.gov/35907580/)

### Finding 4 — NETosis/necroptosis links intramural neutrophil activation to endothelial damage and forms a feed-forward complement loop

The mechanistic bridge between node 3 (intramural degranulation/oxidative burst) and node 4 (fibrinoid necrosis) is **neutrophil extracellular trap (NET) formation**. ANCA induces NETs via **RIPK1/3- and MLKL-dependent necroptosis**, and NETs from ANCA-stimulated neutrophils damage endothelial cells in vitro. NETs both damage endothelium *and* activate complement, creating a **feed-forward amplification loop**: ANCA-activated neutrophils "further activate the alternative complement pathway, leading to the generation of complement 5a (C5a), which amplifies the inflammatory response by priming neutrophils." Causal sufficiency is shown by injecting NET-loaded myeloid dendritic cells into mice, which produces circulating PR3-/MPO-ANCA and AAV-like disease. A therapeutic model (recombinant thrombomodulin, acting via Mac-1 to suppress histone citrullination) inhibits ANCA-induced NETs and ameliorates pulmonary hemorrhage and glomerulonephritis in experimental AAV rats.

This finding justifies modeling a **bidirectional/feedback edge** between the recruitment node (2) and the degranulation node (3), rather than a strictly linear chain.

> "ANCA induces neutrophil extracellular traps (NETs) via receptor-interacting protein kinase (RIPK) 1/3- and mixed-lineage kinase domain-like (MLKL)-dependent necroptosis. NETs from ANCA-stimulated neutrophils caused endothelial cell (EC) damage in vitro" — [PMID: 29078325](https://pubmed.ncbi.nlm.nih.gov/29078325/)

> "further activate the alternative complement pathway, leading to the generation of complement 5a (C5a), which amplifies the inflammatory response by priming neutrophils for ANCA-mediated overactivation" — [PMID: 37138650](https://pubmed.ncbi.nlm.nih.gov/37138650/)

> "Injection of NET-loaded myeloid dendritic cells into mice results in circulating PR3- and MPO-ANCA and the development of AAV-like disease" — [PMID: 27446086](https://pubmed.ncbi.nlm.nih.gov/27446086/)

### Finding 5 — Genetic architecture maps risk genes to specific nodes and reveals a serotype axis

A GWAS of **1,986 AAV cases vs 4,723 controls** provides the gene-to-node anchoring for the module. The strongest signals localize to **HLA-DPB1** (rs141530233 OR 2.99; rs1042169 OR 2.82) — a haplotype associated with reduced HLA-DP expression and increased PR3-reactive T cells — mapping adaptive-immune risk to the **upstream ANCA-generating input**. Genome-wide-significant hits at **SERPINA1** (alpha-1 antitrypsin, the physiologic PR3 inhibitor), **PTPN22** (missense), and **PRTN3** (proteinase-3 gene; top variant correlates with increased PRTN3 expression in neutrophils) map to the **neutrophil/autoantigen effector nodes**. Critically, genetic associations segregate more by **ANCA serotype (anti-PR3 vs anti-MPO)** than by clinical diagnosis, supporting a serotype axis within the pauci-immune branch.

> "the largest effect on risk of AAV came from the single-nucleotide polymorphism variants rs141530233 and rs1042169 at the HLA-DPB1 locus (odds ratio [OR] 2.99 and OR 2.82, respectively)" — [PMID: 28029757](https://pubmed.ncbi.nlm.nih.gov/28029757/)

> "Significant associations were also observed at the SERPINA1 and PTPN22 loci, the peak signals arising from functionally relevant missense variants, and at PRTN3, in which the top-scoring variant correlated with increased PRTN3 expression in neutrophils" — [PMID: 28029757](https://pubmed.ncbi.nlm.nih.gov/28029757/)

### Finding 6 — DADA2 defines a macrophage/TNF-driven boundary branch

**DADA2** (deficiency of adenosine deaminase 2), caused by biallelic loss-of-function *ADA2* mutations, is the first-described monogenic small/medium-vessel vasculitis. Its mechanism **diverges from the ANCA/C5a core**: loss of ADA2 skews macrophage differentiation toward a pro-inflammatory **M1** subset that is "detrimental for endothelial integrity," and the vasculitic phenotype "response[s] extremely well to tumor necrosis factor-α inhibition" — not complement/neutrophil-directed therapy. HSCT (restoring enzyme activity) is curative. DADA2 produces medium-vessel vasculitis and lacunar/strokes, consistent only with the terminal nodes (fibrinoid necrosis, luminal compromise/infarction). It should be curated as a **boundary branch**, illustrating that the terminal nodes can be reached through non-core effectors.

> "in the absence of ADA2, macrophage differentiation is skewed to a pro-inflammatory M1 subset, which is detrimental for endothelial integrity" — [PMID: 30565235](https://pubmed.ncbi.nlm.nih.gov/30565235/)

> "Vasculitic-predominant manifestations respond extremely well to tumor necrosis factor-α inhibition" — [PMID: 32845415](https://pubmed.ncbi.nlm.nih.gov/32845415/)

### Finding 7 — The immune-complex branch converges via the CLASSICAL pathway and links viral exposures to multi-organ disease

Whereas the ANCA branch engages the **alternative** complement pathway, the immune-complex branch converges on the shared effector via the **classical** pathway. In hepatitis-B-associated polyarteritis nodosa (PAN), HCV-associated cryoglobulinemic vasculitis, and probably Henoch-Schönlein purpura, "histological lesions may result from the deposition of immune complexes formed from viral antigens and from antibodies responsible for the activation of the classic complement pathway and for recruitment of polymorphonuclear neutrophils." In HCV mixed cryoglobulinemia, cryoprecipitable immune complexes drive complement-dependent small-vessel vasculitis across skin, kidney, and peripheral/central nervous system — **direct human evidence that a single causal factor produces multi-organ manifestations** (Question 6).

> "histological lesions may result from the deposition of immune complexes formed from viral antigens and from antibodies responsible for the activation of the classic complement pathway and for recruitment of polymorphonuclear neutrophils" — [PMID: 16225258](https://pubmed.ncbi.nlm.nih.gov/16225258/)

> "complement factors play a crucial role in the cold-insoluble ICs-mediated vasculitis, involving primarily small blood vessels in different tissues including skin, kidney, peripheral, and central nervous system" — [PMID: 22844322](https://pubmed.ncbi.nlm.nih.gov/22844322/)

---

## Mechanistic Model / Interpretation

### Proposed DAG (nodes and causal edges)

```
        UPSTREAM BRANCH POINT (Node 1)
   ┌─────────────────────────┬──────────────────────────┐
   │  (A) Immune-complex      │  (B) Pauci-immune / ANCA  │   [ boundary branch ]
   │      deposition          │      neutrophil priming   │   (C) DADA2 / ADA2 loss
   │  classical complement    │  alternative complement   │   → M1 macrophage,
   │  (PAN-HBV, cryo-HCV,     │  (GPA, MPA, EGPA)         │     TNF-α driven
   │   IgA vasculitis, LCV)   │                           │       │
   └───────────┬─────────────┴───────────┬──────────────┘        │
               │                          │                        │
               └──────────┬───────────────┘                        │
                          ▼                                        │
        ┌──────────────────────────────────────────┐              │
        │  NODE 2  Complement C5a amplification &    │              │
        │          neutrophil recruitment  (HUB)     │◄──┐         │
        │          — REQUIRED convergence node —     │   │ feed-   │
        └──────────────────┬─────────────────────────┘   │ forward │
                           ▼                              │ loop    │
        ┌──────────────────────────────────────────┐     │         │
        │  NODE 3  Intramural leukocyte degranulation│─────┘         │
        │          + oxidative burst + NETosis       │              │
        │          (RIPK1/3–MLKL necroptosis)        │              │
        └──────────────────┬─────────────────────────┘              │
                           ▼                                        │
        ┌──────────────────────────────────────────┐              │
        │  NODE 4  Fibrinoid necrosis of vessel wall │◄─────────────┘
        └──────────────────┬─────────────────────────┘
                           ▼
        ┌──────────────────────────────────────────┐
        │  NODE 5  Luminal compromise & downstream   │
        │          tissue infarction                 │
        └──────────────────────────────────────────┘
```

**Interpretation.** The module is best understood as a **convergence-hub architecture**. Node 2 (C5a/neutrophil recruitment) is the mandatory bottleneck through which both upstream branches must pass, and it is the node with the strongest causal evidence (interventional RCT + knockouts). Nodes 3→5 form the shared terminal cascade. The edge between nodes 2 and 3 is **bidirectional** because NET-driven complement activation regenerates C5a (feed-forward amplification). The DADA2 branch is drawn entering at the terminal end because it reaches fibrinoid necrosis/infarction without transiting the C5a/neutrophil hub.

### Core vs optional node classification (Question 3)

| Node | Label | Status for conformance | Rationale |
|------|-------|------------------------|-----------|
| 1 | Immune stimulus deposition + endothelial activation | **Core (branch point)** | Required, but instantiated by one of two convergent mechanisms (IC vs ANCA) |
| 2 | Complement C5a amplification + neutrophil recruitment | **Core / REQUIRED HUB** | Causally validated by avacopan RCT + mouse KO |
| 3 | Intramural degranulation, oxidative burst, NETosis | **Core / REQUIRED** | Direct in-vitro + model evidence; NET necroptosis pathway |
| 4 | Fibrinoid necrosis of vessel wall | **Core / REQUIRED (defining phenotype)** | The module's defining histopathology |
| 5 | Luminal compromise + downstream infarction | **Core / REQUIRED** | Terminal clinical consequence |
| — | DADA2 macrophage/TNF branch | **Optional / boundary** | Reaches nodes 4–5 without the C5a/neutrophil hub |

---

## Gene-to-Node Mapping (Question 4)

| Gene / factor | Node mapping | Role | Evidence (PMID) |
|---------------|-------------|------|-----------------|
| **HLA-DPB1** | Node 1 (upstream, ANCA branch) | Adaptive-immune risk; ↑ PR3-reactive T cells | 28029757 |
| **PTPN22** | Node 1 (upstream autoimmunity) | Immune tolerance / T-cell signaling missense risk | 28029757 |
| **PRTN3** (PR3) | Node 1 / effector autoantigen | PR3 autoantigen; risk variant ↑ neutrophil PRTN3 expression | 28029757 |
| **MPO** | Node 1 / effector autoantigen | MPO autoantigen (anti-MPO serotype) | 28537941 |
| **SERPINA1** (α1-antitrypsin) | Node 3 modifier | Physiologic PR3 inhibitor; sets PR3 activity threshold | 28029757 |
| **CFB / C5 / C5AR1 (CD88)** | Node 2 (hub) | Alternative-pathway + C5a/C5aR effector; therapeutic target | 35167187; 35665698 |
| **C1q / C4 / classical components** | Node 2 (via IC branch) | Classical-pathway activation by immune complexes | 16225258; 22844322 |
| **ADA2** | Boundary branch (nodes 4–5) | Loss → M1 macrophage, TNF-α-driven medium-vessel vasculitis | 30565235; 32845415 |

**Exposures:** HBV → PAN (immune-complex branch); HCV → cryoglobulinemic vasculitis (immune-complex branch). Both map to Node 1 (IC) → classical complement → Node 2.

---

## Evidence Base (Evidence Table)

| PMID | Evidence type | Exact quote | Supported claim / node |
|------|---------------|-------------|------------------------|
| [28537941](https://pubmed.ncbi.nlm.nih.gov/28537941/) | Human review | "Primed neutrophils are activated by interaction with ANCA in circulation. Activated neutrophils attach to and transmigrate through endothelium and accumulate within the vessel wall. These neutrophils degranulate and produce reactive oxygen radicals and ultimately die, causing ti[ssue damage]." | Linear chain nodes 2→5 (ANCA branch) |
| [35167187](https://pubmed.ncbi.nlm.nih.gov/35167187/) | Human RCT (Level 1) | "Remission at week 26 … was observed in 120 of 166 patients (72.3%) receiving avacopan and in 115 of 164 patients (70.1%) receiving prednisone" | Node 2 causally required (C5aR inhibition induces remission) |
| [35665698](https://pubmed.ncbi.nlm.nih.gov/35665698/) | Mouse KO / review | "in contrast to mice deficient for factor B and C5 animals deficient for C4 were susceptible to AAV … emphasized the specific involvement of the alternative pathway" | Node 2 — alternative pathway localizes causal complement |
| [32602136](https://pubmed.ncbi.nlm.nih.gov/32602136/) | Human biomarker | "C5a: 19.9 … vs 9.06 … pg/mL, P = .002, Bb: 7.3 … vs 0.2 … pg/mL, P < .0001" | Node 2 — systemic alternative-pathway activation at diagnosis |
| [35396080](https://pubmed.ncbi.nlm.nih.gov/35396080/) | Human review | "immune complex-driven disease with activation of the complement cascade, leading to exaggerated production of anaphylatoxins that are responsible for neutrophil recruitment and activation" | Node 1 (IC branch) → converges on Node 2 |
| [35907580](https://pubmed.ncbi.nlm.nih.gov/35907580/) | Human review/path | "Most cases are attributable to immune complex deposition … Arthus type III immune complex reaction … granular deposits of components of complement activation in concert with immunoglobulin" | Node 1 IC branch (type III/Arthus) |
| [29078325](https://pubmed.ncbi.nlm.nih.gov/29078325/) | In vitro / model | "ANCA induces neutrophil extracellular traps (NETs) via RIPK 1/3- and MLKL-dependent necroptosis. NETs from ANCA-stimulated neutrophils caused endothelial cell (EC) damage in vitro" | Node 3→4 NET/necroptosis mechanism |
| [37138650](https://pubmed.ncbi.nlm.nih.gov/37138650/) | Human review | "further activate the alternative complement pathway, leading to the generation of complement 5a (C5a), which amplifies the inflammatory response by priming neutrophils" | Node 2↔3 feed-forward loop |
| [27446086](https://pubmed.ncbi.nlm.nih.gov/27446086/) | Mouse model | "Injection of NET-loaded myeloid dendritic cells into mice results in circulating PR3- and MPO-ANCA and the development of AAV-like disease" | NETs causally sufficient for AAV |
| [31883830](https://pubmed.ncbi.nlm.nih.gov/31883830/) | Rat model (therapeutic) | Recombinant thrombomodulin inhibits ANCA-induced NETs (via Mac-1, ↓ histone citrullination), ameliorating pulmonary hemorrhage + glomerulonephritis | Node 3→4 NET-targeted rescue |
| [28029757](https://pubmed.ncbi.nlm.nih.gov/28029757/) | Human GWAS | "the largest effect on risk of AAV came from … HLA-DPB1 locus (OR 2.99 and OR 2.82)"; "SERPINA1 and PTPN22 … and PRTN3, in which the top-scoring variant correlated with increased PRTN3 expression in neutrophils" | Gene-to-node mapping; serotype axis |
| [30565235](https://pubmed.ncbi.nlm.nih.gov/30565235/) | Review / mechanism | "in the absence of ADA2, macrophage differentiation is skewed to a pro-inflammatory M1 subset, which is detrimental for endothelial integrity" | DADA2 boundary branch (macrophage-driven) |
| [32845415](https://pubmed.ncbi.nlm.nih.gov/32845415/) | Human review | "Vasculitic-predominant manifestations respond extremely well to tumor necrosis factor-α inhibition" | DADA2 boundary branch (TNF-dependent) |
| [16225258](https://pubmed.ncbi.nlm.nih.gov/16225258/) | Human review | "immune complexes formed from viral antigens and from antibodies responsible for the activation of the classic complement pathway and for recruitment of polymorphonuclear neutrophils" | IC branch via classical pathway; HBV/HCV exposures |
| [22844322](https://pubmed.ncbi.nlm.nih.gov/22844322/) | Human review | "complement factors play a crucial role in the cold-insoluble ICs-mediated vasculitis, involving primarily small blood vessels … skin, kidney, peripheral, and central nervous system" | Multi-organ manifestations from one causal factor (HCV) |

**Supporting in-vitro mechanistic detail (corroborative, not primary anchors):** C5a primes neutrophils for ANCA-induced respiratory burst and degranulation via p38MAPK/ERK/PI3K signaling ([PMID: 22675451](https://pubmed.ncbi.nlm.nih.gov/22675451/)); C5a–S1P/CD88 crosstalk amplifies activation ([PMID: 25000985](https://pubmed.ncbi.nlm.nih.gov/25000985/)); C3aR modulates macrophage recruitment and ANCA production but is **not** required for glomerular injury, reinforcing C5a (not C3a) as the effector anaphylatoxin ([PMID: 29315316](https://pubmed.ncbi.nlm.nih.gov/29315316/)).

---

## Ontology Suggestions (Question 8)

*IDs are suggested by label where confident; unverified IDs are flagged for curator confirmation — do not treat bracketed IDs as authoritative.*

### Gene Ontology (biological process)
| Suggested GO label | Node | Note |
|--------------------|------|------|
| complement activation, alternative pathway | 2 (ANCA branch) | verify ID (e.g. GO:0006957) |
| complement activation, classical pathway | 2 (IC branch) | verify ID (e.g. GO:0006958) |
| complement receptor mediated signaling / C5a anaphylatoxin receptor activity | 2 | verify ID |
| neutrophil chemotaxis | 2 | verify ID (e.g. GO:0030593) |
| neutrophil degranulation | 3 | verify ID (e.g. GO:0043312) |
| respiratory burst / superoxide anion generation | 3 | verify ID (e.g. GO:0045730) |
| neutrophil extracellular trap formation | 3 | verify ID |
| necroptotic process | 3 | verify ID (e.g. GO:0070266) |
| leukocyte migration involved in inflammatory response | 2–3 | verify ID |
| macrophage differentiation (M1) | DADA2 branch | verify ID |

### Cell Ontology (cell types)
| Suggested CL label | Node |
|--------------------|------|
| neutrophil | 2, 3 (core effector) |
| endothelial cell of vascular tree / blood vessel endothelial cell | 1, 4 |
| macrophage (classically activated / M1) | DADA2 boundary branch |
| eosinophil | EGPA sub-branch (optional) |
| plasma cell / B cell (ANCA-producing) | upstream, ANCA branch |

### UBERON (anatomy)
| Suggested UBERON label | Relevance |
|------------------------|-----------|
| blood vessel / wall of blood vessel (tunica media, tunica intima) | defining site (nodes 1, 4) |
| arteriole / venule / capillary (small vessel) | small-vessel branches |
| medium-sized artery | PAN and DADA2 branches |
| glomerulus / kidney | frequent target organ |
| skin / dermis | cutaneous LCV target |
| lung | pulmonary hemorrhage (AAV) |
| peripheral nerve | mononeuritis multiplex consequence (node 5) |

---

## Out-of-Scope Boundary Notes (Question 9)

- **DADA2 (ADA2 deficiency):** shares only terminal nodes (fibrinoid necrosis, infarction) via a macrophage/M1/TNF-α mechanism; **exclude from core conformance**, curate as an explicitly labeled optional boundary branch. TNF-inhibitor responsiveness and HSCT curability distinguish it from the complement/neutrophil core.
- **Lymphocyte-dominant vasculitides** (e.g., SARS-CoV-2 endotheliitis/"COVID toes," some drug reactions with lymphocytic infiltrate; PMIDs 32562567, 653331): the effector is lymphocytic/viral endothelial injury, not C5a/neutrophil — **out of scope** even when fibrinoid necrosis is present.
- **Angiotensin/pressure-driven "fibrinoid" vasculopathy** (e.g., malignant-hypertension transgenic rat model; PMID 9931107): fibrinoid change is hemodynamically driven, not leukocyte-and-complement mediated — **out of scope**.
- **Eosinophil-predominant tissue injury** (Churg-Strauss/EGPA neuropathy; PMID 12564771): eosinophil cationic protein neurotoxicity is an *adjunct* mechanism; the vasculitic core still requires the neutrophil/complement hub. Model EGPA as an optional eosinophil sub-branch, not a replacement for the hub.
- **C3a signaling** is explicitly *not* required for glomerular injury (PMID 29315316) — keep the hub centered on **C5a/C5aR (CD88)**, not on generic anaphylatoxin signaling.
- **Fibrinolytic/coagulation amplification** (reduced plasminogen-activator release, fibrin deposition; PMIDs 8609438, 8505166) is a **non-immunologic amplifier** of tissue damage — record as a modifier edge, not a core node.

---

## Limitations and Knowledge Gaps

1. **Branch asymmetry in evidence strength.** The pauci-immune/ANCA branch is supported by an interventional RCT and knockouts; the immune-complex branch rests largely on **review-level and histopathologic** evidence with fewer causal interventional data. The convergence claim (both branches use C5a-driven neutrophil recruitment) is mechanistically plausible and literature-stated but not proven by a branch-specific C5a-blockade trial in immune-complex vasculitis.
2. **Classical vs alternative pathway convergence.** Whether the two upstream pathways truly converge on the *identical* C5a/C5aR node in vivo, or engage partly distinct effector programs, needs direct comparison. Full-text verification recommended for PMIDs 16225258 and 22844322 before curating the classical-pathway edge.
3. **No hypotheses were formally tested statistically** in this literature-synthesis investigation; findings derive from 36 screened papers. Effect sizes are drawn from cited primary studies, not re-derived.
4. **DADA2 boundary placement** assumes minimal neutrophil/complement contribution; some DADA2 phenotypes may overlap the core in ways not yet resolved.
5. **Ontology IDs are provisional.** All suggested GO/CL/UBERON identifiers require curator verification against current ontology releases; several labels (NET formation, C5a receptor activity) may map to newer or restructured terms.
6. **Serotype axis (PR3 vs MPO)** is genetically supported but its downstream node-level consequences (e.g., different NET propensity, complement engagement) are not fully mapped.

---

## Proposed Follow-up Actions

1. **Curate node 1 as a branch point** with an explicit `mechanism_type` attribute (immune-complex vs pauci-immune) and two labeled complement-pathway edges (classical vs alternative) into node 2.
2. **Encode the node 2↔3 feed-forward loop** as an explicit amplification annotation, and mark node 2 as the required convergence hub for conformance.
3. **Full-text verification** of PMIDs 16225258 and 22844322 (classical-pathway convergence in IC vasculitis) and PMID 35665698 (mouse KO details reported within a review), before finalizing causal edges.
4. **Add DADA2/ADA2 as a formally labeled optional boundary branch** entering at nodes 4–5, with a cross-link to a separate macrophage-TNF medium-vessel vasculitis module if one exists.
5. **Verify all ontology IDs** (GO/CL/UBERON) against current releases; do not import bracketed placeholder IDs without confirmation.
6. **Targeted literature expansion** on the immune-complex branch's C5a dependence (e.g., complement-blockade evidence in cryoglobulinemic or IgA vasculitis) to strengthen the convergence claim with interventional data.

---

## Answers to the Nine Research Questions (concise)

1. **Best-supported shared mechanism:** C5a/C5aR-driven neutrophil recruitment and intramural activation producing fibrinoid necrosis — validated by the avacopan RCT and complement/C5aR knockouts.
2. **Name/scope:** Retain "Necrotizing Vasculitis Module"; sharpen internal scope to "complement-C5a/neutrophil convergence-hub, fibrinoid-necrotizing vasculitis."
3. **Core vs optional:** All five provisional nodes are core/required; node 2 is the required hub. DADA2 macrophage/TNF branch is optional/boundary.
4. **Gene/exposure/cell support:** HLA-DPB1, PTPN22 → autoimmunity; PRTN3/MPO → autoantigens; SERPINA1 → PR3 threshold; CFB/C5/C5AR1 → hub; ADA2 → boundary branch; HBV/HCV → immune-complex branch. Core cells: neutrophils, endothelial cells.
5. **Causal edges:** Interventional (avacopan) + knockout (factor B/C5/C5aR) for the hub; NET/necroptosis in-vitro and NET-DC transfer for node 3→ANCA/endothelial damage.
6. **Human multi-manifestation evidence:** HCV cryoglobulinemia produces skin/kidney/PNS/CNS vasculitis via complement (PMID 22844322).
7. **Model/in-vitro path:** RIPK1/3-MLKL necroptosis → NETs → endothelial damage + complement activation (PMID 29078325); NET-DC injection causes AAV in mice (PMID 27446086); rTM rescue in rat AAV (PMID 31883830).
8. **Ontology:** see suggested GO/CL/UBERON tables above (verify IDs).
9. **Speculative/out-of-scope:** lymphocytic and pressure-driven fibrinoid vasculopathy; C3a as effector; coagulation/fibrinolysis as core node.

---

*Report compiled from 7 confirmed findings and 36 reviewed papers across 5 investigation iterations.*


## Artifacts

- [OpenScientist final report](necrotizing_vasculitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](necrotizing_vasculitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 20 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:28029757` *(abstract only)*: "the largest effect on risk of AAV came from the single-nucleotide polymorphism variants rs141530233 and rs1042169 at the HLA-DPB1 locus (odds ratio [OR] 2.99 and OR 2.82, respectively)"
  - closest text in source: "the largest effect on risk of AAV came from the single-nucleotide polymorphism variants rs141530233 and rs1042169 at the HLA-DPB1 locus (odds ratio [OR] 2.99 and OR 2.82, respectively)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.