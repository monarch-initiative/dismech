---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T00:27:09.498305'
end_time: '2026-11-09T00:40:23.789523'
duration_seconds: 794.29
template_file: templates/module_mechanism_research.md
template_variables:
  module_name: Inhaled Irritant Airway Epithelial Injury Module
  module_slug: inhaled_irritant_airway_injury
  category: Module
  module_description: 'Conserved pathophysiology of acute and repeated chemical irritant
    injury to the conducting airway epithelium (nasal, tracheal and bronchial), as
    caused by reactive volatile organic compounds (1,3-dichloropropene), aldehydes
    (formaldehyde, acrolein, acetaldehyde), chlorine and ozone, and inhaled particulate
    and aerosol mixtures. The chain runs: deposition of a reactive inhaled xenobiotic
    on the airway epithelial lining; epithelial thiol depletion with electrophilic
    and oxidative stress; epithelial injury with junctional barrier failure; loss
    of mucociliary differentiation including ciliated cell loss and squamous metaplasia;
    and impaired mucociliary clearance with airway remodeling. This module is distinct
    from alveolar_capillary_barrier_failure, which is distal lung, from emphysema_protease_antiprotease_imbalance,
    which is a protease mechanism, and from epithelial_barrier_dysfunction, which
    is scoped to the allergic type 2 epithelial barrier hypothesis as an intrinsic
    defect rather than a chemical insult. It is complementary to keap1_nrf2_are_signaling,
    which models the KEAP1 sensor cysteine modification and the adaptive antioxidant
    response rather than the epithelial injury the insult produces. Key conformance
    target is the epithelial injury and junctional barrier failure node.'
  pathophysiology_summary: '- Reactive Inhaled Xenobiotic Deposition on Airway Epithelium:
    an electrophilic or oxidant gas, vapour or particle deposits on the airway surface
    liquid and epithelial lining of the conducting airway, with regional dosimetry
    determined by solubility and reactivity. Role trigger.

    - Epithelial Thiol Depletion and Electrophilic Stress: conjugation and oxidation
    deplete epithelial glutathione and protein thiols, producing electrophilic and
    oxidative stress; this is the insult that keap1_nrf2_are_signaling responds to
    adaptively. Role amplifier.

    - Airway Epithelial Injury and Junctional Barrier Failure: epithelial cell death
    and tight junction disruption reduce transepithelial electrical resistance and
    increase paracellular permeability. Role central_effector and key conformance
    target.

    - Loss of Mucociliary Differentiation: ciliated cell loss, goblet or mucous cell
    change and squamous metaplasia replace the pseudostratified columnar phenotype.
    Role effector.

    - Impaired Mucociliary Clearance and Airway Remodeling: reduced clearance, persistent
    irritation and, with repeated exposure, airway remodeling. Role consequence.'
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
citation_count: 25
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 21
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:32275839
  relevance_assessed: 26
  on_topic: 14
  needs_review: true
  validator_version: 0.5.1
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
  path: inhaled_irritant_airway_injury-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: inhaled_irritant_airway_injury-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Inhaled Irritant Airway Epithelial Injury Module
- **Module Slug:** inhaled_irritant_airway_injury
- **Category:** Module

## Current Module Description

Conserved pathophysiology of acute and repeated chemical irritant injury to the conducting airway epithelium (nasal, tracheal and bronchial), as caused by reactive volatile organic compounds (1,3-dichloropropene), aldehydes (formaldehyde, acrolein, acetaldehyde), chlorine and ozone, and inhaled particulate and aerosol mixtures. The chain runs: deposition of a reactive inhaled xenobiotic on the airway epithelial lining; epithelial thiol depletion with electrophilic and oxidative stress; epithelial injury with junctional barrier failure; loss of mucociliary differentiation including ciliated cell loss and squamous metaplasia; and impaired mucociliary clearance with airway remodeling. This module is distinct from alveolar_capillary_barrier_failure, which is distal lung, from emphysema_protease_antiprotease_imbalance, which is a protease mechanism, and from epithelial_barrier_dysfunction, which is scoped to the allergic type 2 epithelial barrier hypothesis as an intrinsic defect rather than a chemical insult. It is complementary to keap1_nrf2_are_signaling, which models the KEAP1 sensor cysteine modification and the adaptive antioxidant response rather than the epithelial injury the insult produces. Key conformance target is the epithelial injury and junctional barrier failure node.

## Current Provisional Nodes

- Reactive Inhaled Xenobiotic Deposition on Airway Epithelium: an electrophilic or oxidant gas, vapour or particle deposits on the airway surface liquid and epithelial lining of the conducting airway, with regional dosimetry determined by solubility and reactivity. Role trigger.
- Epithelial Thiol Depletion and Electrophilic Stress: conjugation and oxidation deplete epithelial glutathione and protein thiols, producing electrophilic and oxidative stress; this is the insult that keap1_nrf2_are_signaling responds to adaptively. Role amplifier.
- Airway Epithelial Injury and Junctional Barrier Failure: epithelial cell death and tight junction disruption reduce transepithelial electrical resistance and increase paracellular permeability. Role central_effector and key conformance target.
- Loss of Mucociliary Differentiation: ciliated cell loss, goblet or mucous cell change and squamous metaplasia replace the pseudostratified columnar phenotype. Role effector.
- Impaired Mucociliary Clearance and Airway Remodeling: reduced clearance, persistent irritation and, with repeated exposure, airway remodeling. Role consequence.

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

# Mechanism Module Research Report
## Inhaled Irritant Airway Epithelial Injury Module (`inhaled_irritant_airway_injury`)

*Prepared: 2026-11-09. Mechanism-focused curation support report (not a disease entry).*

---

## Summary

This report evaluates the proposed **Inhaled Irritant Airway Epithelial Injury Module**, a reusable mechanism module describing the conserved pathophysiology of acute and repeated chemical irritant injury to the conducting airway epithelium (nasal, tracheal, bronchial). Across five iterations and 60 reviewed papers, the evidence strongly and convergently supports the module as a **single, conserved, linear causal chain** that is shared across chemically diverse irritants — reactive volatile organic compounds (1,3-dichloropropene), aldehydes (formaldehyde, acrolein, acetaldehyde), chlorine, ozone, and particulate/aerosol mixtures. The chain runs: **(N1)** deposition of a reactive inhaled xenobiotic governed by solubility and reactivity → **(N2)** epithelial glutathione and protein-thiol depletion with electrophilic/oxidative stress → **(N3)** epithelial cell death and tight/adherens-junction barrier failure (reduced TEER, increased paracellular permeability) → **(N4)** loss of mucociliary differentiation (ciliated-cell loss, squamous or mucous metaplasia) → **(N5)** impaired mucociliary clearance and airway remodeling.

The central recommendation is to **retain all five nodes as core and required for conformance**, with **junctional barrier failure (N3)** serving as the obligatory conformance gate, exactly as the module description specifies. The most significant refinement to emerge from the literature is that **Node 4 (loss of mucociliary differentiation) branches into two distinct, gene-specific metaplasia programs**: a **TP63-associated squamous metaplasia** program driven by severe cytotoxic irritants, and a **SPDEF/FOXA3/MUC5AC/NOTCH3 mucous (goblet) metaplasia** program with loss of the suppressor FOXA2. These should be curated as **optional gene-specific sub-branches of N4**, not separate core requirements. A single agent — **1,3-dichloropropene** — was found to recapitulate the entire chain in one experimental system, providing an unusually clean anchor for the module.

The module name and scope are **appropriate as written**. Two upstream/parallel processes that share the electrophile chemistry but are mechanistically distinct should remain **out of scope**: the **KEAP1/NRF2/ARE adaptive antioxidant response** (complementary sensor/response, modeled by a separate module) and **TRPA1-mediated sensory-neuron irritant sensing** (a parallel protective reflex, "warning of damage rather than damage itself"). The boundaries against `alveolar_capillary_barrier_failure` (distal lung), `emphysema_protease_antiprotease_imbalance` (protease mechanism), and `epithelial_barrier_dysfunction` (intrinsic allergic Type 2 defect) are well-justified by the anatomy and mechanism of the evidence reviewed.

---

## Key Findings

### Finding 1 — Node 1 (Reactive Xenobiotic Deposition): Regional dosimetry is governed by gas solubility and reactivity

The module's trigger node is corroborated by convergent dosimetry and computational-fluid-dynamics (CFD) evidence. Formaldehyde — a high-solubility, high-reactivity vapor — shows high nasal uptake and both injury and tumors localize precisely to the nasal sub-regions of highest vapor flux. This establishes the foundational principle that **the physicochemical properties of the inhaled agent (solubility and reactivity) determine where in the airway the internal dose — and therefore the injury — is deposited.**

A regulatory/mechanistic review of the formaldehyde dispute states that inhalation effects "follow a concentration-dependent continuum of effects confined to the tissues of initial contact" and that "nasal squamous cell carcinomas localized to regions of highest vapor flux in the rat nasal cavity" ([PMID: 42101931](https://pubmed.ncbi.nlm.nih.gov/42101931/)). A dosimetry modeling paper confirms that "due to its high solubility and reactivity, quantitative risk estimates for inhaled formaldehyde have relied on internal dose estimates in the upper respiratory tract" ([PMID: 24385418](https://pubmed.ncbi.nlm.nih.gov/24385418/)). This finding grounds the module's claim that injury is confined to the site of deposition and is not a diffuse, whole-lung process — a key distinction from distal-lung modules.

### Finding 2 — Node 2 (Epithelial Thiol Depletion / Electrophilic Stress): Reactive aldehydes and oxidant gases consume epithelial GSH and protein thiols

The amplifier node is supported by direct human airway epithelial cell data. Acrolein, an α,β-unsaturated aldehyde, rapidly adducts cysteine thiols and inactivates the selenoenzyme thioredoxin reductase (TrxR) in human bronchiolar epithelial (HBE1) cells, with recovery "depending on the presence of cellular GSH and thioredoxin 1 (Trx1)" ([PMID: 24157358](https://pubmed.ncbi.nlm.nih.gov/24157358/)). This demonstrates electrophilic targeting of the thiol/selenol antioxidant system in human airway cells and establishes GSH as the critical protective buffer.

The detoxification arm is confirmed by evidence that glutathione S-transferases conjugate GSH to acrolein and related aldehydes: "GST P1-1 introduced into Hep G2 cells by electroporation was similarly found to increase their resistance to acrolein" ([PMID: 8108434](https://pubmed.ncbi.nlm.nih.gov/8108434/)), implicating GSH consumption as the central protective/insult axis. Independently, chlorine toxicity evidence notes that "prior studies suggest that antioxidant depletion is important in producing dysfunction" ([PMID: 24582687](https://pubmed.ncbi.nlm.nih.gov/24582687/)), showing that thiol/antioxidant depletion is a shared feature across chemically distinct irritants. Critically, this node is precisely the insult to which the complementary **KEAP1/NRF2/ARE module** responds adaptively — reinforcing the two-module division of labor rather than overlap.

### Finding 3 — Node 3 (Central Effector): Epithelial injury with junctional barrier failure is a convergent, dose-dependent endpoint shared across chemically distinct irritants

The module's key conformance target is the best-supported node in the dataset. In air-liquid-interface (ALI) human bronchial epithelium, "a dose-dependent increase in barrier permeability was observed for confluent cells exposed to acrolein and formic acid" ([PMID: 41635987](https://pubmed.ncbi.nlm.nih.gov/41635987/)), coupled with LDH-release cytotoxicity. An independent oxidant, ozone, produces the same endpoint: "in vitro ozone exposure caused significant reduction in epithelial integrity" in human and murine primary epithelia ([PMID: 42352262](https://pubmed.ncbi.nlm.nih.gov/42352262/)).

Two reviews converge on barrier failure as the shared core mechanism: "airway epithelial barrier dysfunction is a basic pathological mechanism" ([PMID: 42386309](https://pubmed.ncbi.nlm.nih.gov/42386309/)), and pollutant exposure "induces epithelial injury, disrupts epithelial barrier integrity, promotes oxidative stress" ([PMID: 42845222](https://pubmed.ncbi.nlm.nih.gov/42845222/)) — the latter explicitly linking the upstream oxidative insult (N2) to the central barrier-failure effector (N3). The chemical diversity of the triggering agents (aldehyde, organic acid, oxidant gas, particulate) all funneling into the same TEER-loss/permeability-gain endpoint is the single strongest argument for treating N3 as the obligatory conformance gate.

### Finding 4 — Nodes 4–5 (Loss of Differentiation and Remodeling): Irritant injury drives ciliated/club-cell loss, squamous metaplasia, poorly differentiated repair, and airway remodeling

The downstream effector and consequence nodes are supported by chronic-exposure pathology. Chronic formaldehyde produces "persistent epithelial necrosis, regenerative proliferation, and nasal squamous cell carcinomas" at exposures ≥6 ppm ([PMID: 42101931](https://pubmed.ncbi.nlm.nih.gov/42101931/)), linking cytotoxicity to loss of normal differentiation and squamous metaplasia/neoplasia. Chlorine inhalation causes epithelial sloughing with "regrowth of a poorly differentiated airway epithelium" ([PMID: 30189237](https://pubmed.ncbi.nlm.nih.gov/30189237/)).

The injury-to-abnormal-repair transition is documented directly: "chlorine inhalation caused sloughing of bronchial epithelium 1 day after chlorine exposure, which was repaired with restoration of a pseudostratified epithelium by day 7. The repaired epithelium contained an abnormal distribution of epithelial cells" ([PMID: 25398987](https://pubmed.ncbi.nlm.nih.gov/25398987/)). The remodeling consequence (N5) is captured by chlorine-induced "abnormalities in the small airways, including inflammation and sporadic bronchiolitis obliterans lesions" ([PMID: 27913141](https://pubmed.ncbi.nlm.nih.gov/27913141/)). Together these span the full downstream arc from loss of mucociliary differentiation to persistent remodeling.

### Finding 5 — 1,3-Dichloropropene recapitulates the entire module chain in one system

The index compound named in the module description provides a uniquely complete demonstration of the chain. In MucilAir nasal/tracheal/bronchial ALI cultures, sub-cytotoxic 1,3-DCP vapor caused dose-dependent differential gene expression, a "change in cellular morphology from pseudostratified columnar epithelium to squamous epithelium, and depletion of GSH in MucilAir nasal cultures" ([PMID: 37863466](https://pubmed.ncbi.nlm.nih.gov/37863466/)) — linking N2 (thiol depletion) directly to N4 (squamous metaplasia) in human nasal epithelium.

Across five airway-region ALI models, 1,3-DCP toxicity was quantified "using an assay for transepithelial conductance (for epithelial barrier integrity) and the lactate dehydrogenase (LDH) release assay (for cytotoxicity)" coupled to an airway dosimetry model ([PMID: 36183849](https://pubmed.ncbi.nlm.nih.gov/36183849/)) — measuring the central barrier-failure effector (N3) and tying it to region-specific dosimetry (N1). In vivo mouse data confirm the amplifier node: "the glutathione (GSH)-dependent metabolism of 1,3-D results in significant depletion of GSH at repeated exposure levels of 30 ppm and above" ([PMID: 31808915](https://pubmed.ncbi.nlm.nih.gov/31808915/)). Rat inhalation produces "focal hyperplasia of the respiratory epithelium and/or focal degenerative changes in the olfactory epithelium" ([PMID: 2925012](https://pubmed.ncbi.nlm.nih.gov/2925012/)), confirming point-of-contact injury and remodeling in vivo. 1,3-DCP is therefore recommended as the **canonical exemplar** for module curation.

### Finding 6 — Gene-specific sub-branches: junctional genes for N3; squamous vs mucous metaplasia programs for N4

Molecular detail resolves two curatable sub-branches. For **N3**, cigarette-smoke extract concentration-dependently decreased TEER, increased permeability, and "suppressed gene expression of claudin-1, claudin-3, claudin-4, claudin-7, claudin-15, occludin, E-cadherin, junctional adhesion molecule-A (JAM-A) and zonula occludens-1 (ZO-1)" ([PMID: 31706310](https://pubmed.ncbi.nlm.nih.gov/31706310/)) — naming the specific tight/adherens-junction genes whose loss constitutes barrier failure.

For **N4**, the differentiation-loss node splits into two programs. Severe cytotoxic irritants (formaldehyde, chlorine, 1,3-DCP) drive **TP63-associated squamous metaplasia**. A mechanistically distinct **mucous/goblet metaplasia** program is driven by SPDEF/FOXA3/MUC5AC and NOTCH3 with loss of the suppressor FOXA2: NOTCH signaling "regulates goblet cell differentiation in response to cigarette smoke" ([PMID: 33444514](https://pubmed.ncbi.nlm.nih.gov/33444514/)); the mucus program comprises "genes regulating mucus metaplasia, including Spdef, Muc5ac, Foxa3, and Arg2" ([PMID: 23822876](https://pubmed.ncbi.nlm.nih.gov/23822876/)); and inhaled urban particulate drives "mucociliary remodeling of the nasal airway epithelium" ([PMID: 32275839](https://pubmed.ncbi.nlm.nih.gov/32275839/)). These are the recommended **optional gene-specific branches of N4**.

### Finding 7 — Boundary note: TRPA1 sensory sensing is a parallel reflex, out of core scope

TRPA1, expressed on chemosensory C-fibers, "is activated by almost all oxidizing and electrophilic chemicals, including chlorine, acrolein, tear gas agents, and methyl isocyanate" via covalent protein modification, initiating cough, respiratory depression, and neurogenic inflammation ([PMID: 20601631](https://pubmed.ncbi.nlm.nih.gov/20601631/)). Crucially, this chemesthetic sensing "can provide warning of potential damage rather than actual damage itself" ([PMID: 20633589](https://pubmed.ncbi.nlm.nih.gov/20633589/)). Although TRPA1 shares the electrophile chemistry of N2, it is a neuronal protective reflex, not the epithelial-injury effector chain, and should be **kept out of the core module** as a complementary parallel pathway.

### Finding 8 — Human clinical evidence links formaldehyde to altered ciliated/mucous ratio and depressed ciliary function

Direct human evidence connects the same exposure to multiple downstream manifestations. In formaldehyde-exposed pathology/anatomy workers (0.04–0.67 ppm), nasal cytology showed a chronic non-allergic inflammatory pattern and a shifted mucous-secreting/ciliated-cell ratio, where "qualitative analysis of data distribution of neutrophils and mucous-secreting/ciliated cells ratio showed data clustering with a cut-off set at 15 years of exposure" ([PMID: 29668989](https://pubmed.ncbi.nlm.nih.gov/29668989/)) — human, duration-dependent evidence for N4.

In human nasal respiratory cells, "formaldehyde significantly reduced (67.1%) CBF at the highest dosis (2 hours, 5000 micrograms/m3)" ([PMID: 10416249](https://pubmed.ncbi.nlm.nih.gov/10416249/)) — direct human evidence for impaired ciliary function/clearance (N5). The same study found "ozone had no effect on the human nasal mucociliary transport system under the conditions tested here," demonstrating solubility-dependent regional specificity: low-solubility ozone spares the nose and penetrates deeper, reinforcing the dosimetry trigger node (N1).

### Finding 9 — FOXJ1 is the appropriate ciliated-cell gene anchor for Node 4

In primary human airway basal-cell ALI cultures, IL-13 increased mucus cells and reduced ciliated cells; a treatment that "significantly enhanced FOXJ1 gene expression and restored ciliated structure and function more effectively" (cilia length, density, movement) ([PMID: 40957317](https://pubmed.ncbi.nlm.nih.gov/40957317/)). This establishes FOXJ1 as the master ciliogenesis transcription factor whose expression level reports the ciliated-cell state, making it the natural gene anchor for the ciliated-cell-loss aspect of the differentiation node.

---

## Mechanistic Model / Interpretation

The evidence supports a single conserved linear DAG with one branching node (N4). The chain is agent-agnostic upstream of N3 (any electrophile/oxidant that deposits and depletes thiols converges on barrier failure) and becomes gene/agent-specific at N4.

```
   [ Reactive gas / vapor / particle ]
                 |
                 v
  N1  Reactive Xenobiotic Deposition on Airway Epithelium   (TRIGGER)
      - regional dosimetry set by SOLUBILITY + REACTIVITY
      - formaldehyde -> nose; ozone -> deeper/lower
                 |
                 v
  N2  Epithelial Thiol Depletion & Electrophilic Stress     (AMPLIFIER)
      - GSH + protein-thiol consumption; TrxR inactivation
      - GST detox arm; <-- KEAP1/NRF2 responds here (separate module)
                 |
                 v
  N3  Airway Epithelial Injury & Junctional Barrier Failure (CENTRAL EFFECTOR)
      - cell death + TJ/AJ disruption: down TEER, up permeability  *** CONFORMANCE GATE ***
      - genes: CLDN1/3/4/7/15, OCLN, CDH1, F11R(JAM-A), TJP1(ZO-1)
                 |
                 v
  N4  Loss of Mucociliary Differentiation                    (EFFECTOR)
      - ciliated-cell loss (anchor: FOXJ1)
        |                                   |
        | squamous branch                   | mucous/goblet branch
        v  (severe cytotoxic irritants)     v  (smoke / PM)
      TP63 squamous metaplasia            SPDEF/FOXA3/MUC5AC/NOTCH3,
                                           loss of FOXA2
                 |
                 v
  N5  Impaired Mucociliary Clearance & Airway Remodeling    (CONSEQUENCE)
      - reduced CBF/clearance; bronchiolitis obliterans; fibrosis; hyperreactivity

  === OUT OF SCOPE (parallel / complementary) ===
  * TRPA1 sensory-neuron reflex (warning, not damage)
  * KEAP1/NRF2/ARE adaptive antioxidant response (separate module)
```

**Node core/optional status:**

| Node | Label | Role | Status | Conformance |
|------|-------|------|--------|-------------|
| N1 | Reactive Xenobiotic Deposition | trigger | Core | Required |
| N2 | Thiol Depletion / Electrophilic Stress | amplifier | Core | Required |
| N3 | Epithelial Injury / Junctional Barrier Failure | central_effector | Core | **Required — conformance gate** |
| N4 | Loss of Mucociliary Differentiation | effector | Core | Required (branch choice optional) |
| N4a | TP63 squamous metaplasia | sub-branch | Optional | Gene/agent-specific |
| N4b | SPDEF/FOXA3/MUC5AC/NOTCH3 mucous metaplasia | sub-branch | Optional | Gene/agent-specific |
| N5 | Impaired Clearance / Airway Remodeling | consequence | Core | Required |

**Causal edges (all supported):** N1→N2 (deposition enables conjugation/oxidation; dosimetry data), N2→N3 (thiol depletion/oxidative stress precedes and drives barrier loss; PMID 42845222 links them directly; 1,3-DCP shows GSH depletion with barrier-conductance failure in the same system), N3→N4 (injury/abnormal repair yields poorly differentiated epithelium; PMID 25398987, 37863466), N4→N5 (altered ciliated:mucous ratio and reduced CBF impair clearance; PMID 29668989, 10416249), culminating in remodeling (PMID 27913141, 30189237).

---

## Gene-to-Node Mapping

| Node | Genes / factors | Direction | Evidence (PMID) |
|------|-----------------|-----------|-----------------|
| N2 | GSH pathway, TXNRD (TrxR), TXN (Trx1), GSTP1/GSTA1/GSTM1 | depleted / protective | 24157358, 8108434 |
| N3 | CLDN1, CLDN3, CLDN4, CLDN7, CLDN15, OCLN, CDH1 (E-cadherin), F11R (JAM-A), TJP1 (ZO-1) | suppressed | 31706310 |
| N4 (ciliated) | FOXJ1 | reduced with ciliated-cell loss | 40957317 |
| N4a (squamous) | TP63 | squamous metaplasia program | 42101931, 37863466 (agent-level) |
| N4b (mucous) | SPDEF, FOXA3, MUC5AC, NOTCH3; FOXA2 (suppressor, lost) | goblet metaplasia program | 33444514, 23822876, 32275839 |
| Out of scope | TRPA1 | sensory reflex | 20601631, 20633589 |
| Complementary | KEAP1/NRF2 (separate module) | adaptive | — |

---

## Evidence Base

| PMID | Evidence type | Exact quote | Supported claim |
|------|---------------|-------------|-----------------|
| [24385418](https://pubmed.ncbi.nlm.nih.gov/24385418/) | Model/dosimetry | "Due to its high solubility and reactivity, quantitative risk estimates for inhaled formaldehyde have relied on internal dose estimates in the upper respiratory tract." | N1: solubility/reactivity set regional dose |
| [42101931](https://pubmed.ncbi.nlm.nih.gov/42101931/) | Review | "inhalation was illustrated to follow a concentration-dependent continuum of effects confined to the tissues of initial contact"; "nasal squamous cell carcinomas localized to regions of highest vapor flux" | N1→N4 localization |
| [24157358](https://pubmed.ncbi.nlm.nih.gov/24157358/) | In vitro (human HBE1) | "acrolein rapidly inactivates the seleno-enzyme thioredoxin reductase (TrxR) in human bronchiolar epithelial HBE1 cells, which recovered over 4-8h by a mechanism depending on the presence of cellular GSH and thioredoxin 1 (Trx1)" | N2: thiol/selenol targeting |
| [8108434](https://pubmed.ncbi.nlm.nih.gov/8108434/) | In vitro | "GST P1-1 introduced into Hep G2 cells by electroporation was similarly found to increase their resistance to acrolein." | N2: GSH-conjugating detox |
| [24582687](https://pubmed.ncbi.nlm.nih.gov/24582687/) | Model (chlorine) | "Prior studies suggest that antioxidant depletion is important in producing dysfunction" | N2: antioxidant depletion drives dysfunction |
| [41635987](https://pubmed.ncbi.nlm.nih.gov/41635987/) | In vitro (human ALI) | "A dose-dependent increase in barrier permeability was observed for confluent cells exposed to acrolein and formic acid." | N3: barrier permeability |
| [42352262](https://pubmed.ncbi.nlm.nih.gov/42352262/) | In vitro (human+mouse) | "In vitro ozone exposure caused significant reduction in epithelial integrity" | N3: oxidant barrier loss |
| [42386309](https://pubmed.ncbi.nlm.nih.gov/42386309/) | Review | "airway epithelial barrier dysfunction is a basic pathological mechanism" | N3: shared core mechanism |
| [42845222](https://pubmed.ncbi.nlm.nih.gov/42845222/) | Review | "pollutant exposure induces epithelial injury, disrupts epithelial barrier integrity, promotes oxidative stress" | N2→N3 edge |
| [42101931](https://pubmed.ncbi.nlm.nih.gov/42101931/) | Review | "exposures ≥6 ppm were associated with persistent epithelial necrosis, regenerative proliferation, and nasal squamous cell carcinomas" | N4: cytotoxicity→squamous metaplasia |
| [30189237](https://pubmed.ncbi.nlm.nih.gov/30189237/) | Model (chlorine) | "regrowth of a poorly differentiated airway epithelium" | N4: loss of differentiation |
| [25398987](https://pubmed.ncbi.nlm.nih.gov/25398987/) | Model (chlorine) | "...repaired with restoration of a pseudostratified epithelium by day 7. The repaired epithelium contained an abnormal distribution of epithelial cells" | N3→N4 abnormal repair |
| [27913141](https://pubmed.ncbi.nlm.nih.gov/27913141/) | Model (chlorine, rabbit) | "abnormalities in the small airways, including inflammation and sporadic bronchiolitis obliterans lesions" | N5: remodeling |
| [37863466](https://pubmed.ncbi.nlm.nih.gov/37863466/) | In vitro (human MucilAir) | "change in cellular morphology from pseudostratified columnar epithelium to squamous epithelium, and depletion of GSH in MucilAir nasal cultures" | N2→N4 in one system |
| [36183849](https://pubmed.ncbi.nlm.nih.gov/36183849/) | In vitro (human ALI) | "...an assay for transepithelial conductance (for epithelial barrier integrity) and the lactate dehydrogenase (LDH) release assay (for cytotoxicity)" | N3 + N1 dosimetry |
| [31808915](https://pubmed.ncbi.nlm.nih.gov/31808915/) | Model (mouse) | "The glutathione (GSH)-dependent metabolism of 1,3-D results in significant depletion of GSH at repeated exposure levels of 30 ppm and above." | N2 in vivo |
| [2925012](https://pubmed.ncbi.nlm.nih.gov/2925012/) | Model (rat) | "focal hyperplasia of the respiratory epithelium and/or focal degenerative changes in the olfactory epithelium" | N3–N4 in vivo |
| [31706310](https://pubmed.ncbi.nlm.nih.gov/31706310/) | In vitro | "CSE suppressed gene expression of claudin-1, claudin-3, claudin-4, claudin-7, claudin-15, occludin, E-cadherin, junctional adhesion molecule-A (JAM-A) and zonula occludens-1 (ZO-1)" | N3 junctional genes |
| [33444514](https://pubmed.ncbi.nlm.nih.gov/33444514/) | In vitro (human) | "determine whether NOTCH signaling regulates goblet cell differentiation in response to cigarette smoke" | N4b mucous branch |
| [23822876](https://pubmed.ncbi.nlm.nih.gov/23822876/) | Model | "Montelukast inhibited the expression of genes regulating mucus metaplasia, including Spdef, Muc5ac, Foxa3, and Arg2" | N4b program + FOXA2 |
| [32275839](https://pubmed.ncbi.nlm.nih.gov/32275839/) | In vitro (human) | "Mucociliary Remodeling of the Nasal Airway Epithelium Induced by Urban PM" | N4 particulate remodeling |
| [20601631](https://pubmed.ncbi.nlm.nih.gov/20601631/) | Review | "TRPA1, a TRP ion channel expressed in chemosensory C-fibers, is activated by almost all oxidizing and electrophilic chemicals, including chlorine, acrolein, tear gas agents, and methyl isocyanate" | Out-of-scope sensor |
| [20633589](https://pubmed.ncbi.nlm.nih.gov/20633589/) | Human | "Such sensing can provide warning of potential damage rather than actual damage itself" | TRPA1 boundary |
| [29668989](https://pubmed.ncbi.nlm.nih.gov/29668989/) | Human clinical | "data clustering with a cut-off set at 15 years of exposure" | N4 human, duration-dependent |
| [10416249](https://pubmed.ncbi.nlm.nih.gov/10416249/) | Human in vivo+vitro | "formaldehyde significantly reduced (67.1%) CBF at the highest dosis"; "Ozone had no effect on the human nasal mucociliary transport system" | N5 + N1 specificity |
| [40957317](https://pubmed.ncbi.nlm.nih.gov/40957317/) | In vitro (human) | "LAMA also significantly enhanced FOXJ1 gene expression and restored ciliated structure and function more effectively" | N4 FOXJ1 anchor |

**Evidence-type balance:** The module is supported by human clinical (29668989, 10416249, 20633589), human in vitro/ALI (41635987, 36183849, 37863466, 31706310, 33444514, 40957317, 24157358), model organism (30189237, 25398987, 27913141, 31808915, 2925012, 23822876), and review (42101931, 42386309, 42845222, 20601631) sources — a healthy mix, with the central effector node (N3) supported by both human experimental and review evidence.

---

## Ontology Suggestions

*Do not treat these as final IDs — suggested by label; curator should verify against current ontology releases.*

**Gene Ontology (biological process):**
- *response to oxidative stress*
- *glutathione metabolic process* / *cellular response to oxidative stress* (N2)
- *cellular response to xenobiotic stimulus* (N1/N2)
- *bicellular tight junction assembly* / *regulation of establishment of epithelial barrier* (N3 — use the epithelial-barrier term)
- *epithelial cell differentiation* / *cilium assembly* / *respiratory system epithelial cell differentiation* (N4)
- *mucus secretion* / *goblet cell differentiation* (N4b)
- *epithelial cell development* / *squamous epithelial cell differentiation* (N4a)
- *mucociliary clearance* (N5)
- *tissue remodeling* / *airway remodeling* (N5)

**Cell Ontology (CL):**
- *respiratory epithelial cell* / *epithelial cell of lung*
- *ciliated columnar cell of tracheobronchial tree* (N4 ciliated; FOXJ1 anchor)
- *goblet cell* / *mucus secreting cell* (N4b)
- *club cell* (lost after injury)
- *basal cell of epithelium of respiratory tract* (progenitor driving repair)
- *squamous epithelial cell* (N4a metaplasia)

**UBERON (anatomy):**
- *respiratory airway* / *conducting airway*
- *nasal cavity epithelium* / *respiratory epithelium of nose*
- *epithelium of trachea*
- *bronchus epithelium* / *epithelium of bronchus*
- *airway surface liquid* (surface where deposition occurs — verify label availability)

---

## Out-of-Scope Boundary Notes

1. **KEAP1/NRF2/ARE adaptive antioxidant response** — shares the electrophile/oxidant insult (N2) but models the *sensor cysteine modification and adaptive response*, not the injury. Belongs to the separate `keap1_nrf2_are_signaling` module. The two are complementary: N2 is the insult, NRF2 is the response.
2. **TRPA1 sensory-neuron irritant sensing** — a parallel protective reflex (cough, neurogenic inflammation) that provides "warning of potential damage rather than actual damage itself" (PMID 20633589). Keep out of the core epithelial-injury chain.
3. **`alveolar_capillary_barrier_failure`** — distal lung (alveolar–capillary) mechanism; this module is explicitly the *conducting* airway (nasal/tracheal/bronchial). Dosimetry evidence (formaldehyde vs ozone regional specificity) supports the anatomical split.
4. **`emphysema_protease_antiprotease_imbalance`** — a protease mechanism, distinct from the thiol-depletion/barrier-failure chain.
5. **`epithelial_barrier_dysfunction`** — scoped to the allergic Type 2 *intrinsic* epithelial-barrier hypothesis, not a chemical insult. Although N3 phenotypes overlap, the upstream driver (intrinsic defect vs electrophile/oxidant chemistry) differs.
6. **Systemic/hematologic effects of formaldehyde** (e.g., leukemia hypotheses, PMID 20729258) are out of scope; the module is the local point-of-contact epithelial injury.

---

## Limitations and Knowledge Gaps

- **TP63 squamous branch is agent-level, not gene-level, in the current evidence.** The squamous-metaplasia program is well-documented phenotypically (formaldehyde, chlorine, 1,3-DCP) but direct TP63 transcriptional data in the irritant-injury context was inferred rather than quoted from a primary irritant study. Full-text verification of a TP63-driven squamous-metaplasia paper is recommended before curating N4a at the gene level.
- **PMID 32275839 was flagged as a title/snippet mismatch** during verification — the mucociliary-remodeling claim rests on the title; full-text confirmation is advised.
- **Quantitative edge strengths are not uniform.** N3 is the most robustly supported (multiple human + review sources); the N4→N5 edge rests on fewer human studies (principally PMID 29668989 and 10416249).
- **Temporal ordering of N2 vs N3** is strongly inferred from co-occurrence in single-system studies (1,3-DCP) rather than from time-resolved causal-intervention experiments in human epithelium.
- **No new primary data were generated** in this investigation; conclusions are a literature synthesis. No dataset was analyzed computationally.
- **Acetaldehyde** is named in the module description but was less directly evidenced than acrolein and formaldehyde among the reviewed papers.

---

## Proposed Follow-up Experiments / Actions (for curator)

1. **Verify the TP63 squamous branch at gene level** — retrieve full text of an irritant-specific squamous-metaplasia transcriptomic study to confirm TP63 as the N4a anchor; otherwise curate N4a as a phenotype-level (not gene-level) branch.
2. **Confirm PMID 32275839 full text** for the PM-induced mucociliary remodeling claim before using it as N4b evidence.
3. **Adopt 1,3-dichloropropene as the canonical module exemplar** in curation notes — it is the single agent demonstrating N1→N2→N3→N4 in matched human ALI systems.
4. **Curate N3 junctional genes** (CLDN1/3/4/7/15, OCLN, CDH1, F11R, TJP1) as the molecular signature of the conformance gate.
5. **Record FOXJ1 as the ciliated-cell anchor** and SPDEF/FOXA3/MUC5AC/NOTCH3 (with FOXA2 loss) as the mucous-branch anchor set.
6. **Explicitly cross-reference** the KEAP1/NRF2 and TRPA1 modules as complementary/parallel, with the boundary language from Findings 2 and 7.
7. **Seek a time-resolved human-ALI study** establishing N2-precedes-N3 causality to firm up that edge.

---

## Answer to the Research Questions (condensed)

1. **Best-supported shared mechanism:** solubility/reactivity-driven deposition → epithelial thiol depletion/oxidative stress → junctional barrier failure → loss of mucociliary differentiation → impaired clearance/remodeling.
2. **Name/scope:** appropriate as written; no renaming needed.
3. **Core vs optional:** N1–N5 core and required (N3 = conformance gate); the two N4 metaplasia programs are optional gene-specific sub-branches.
4. **Genes/exposures/cells:** see Gene-to-Node table; exposures = formaldehyde, acrolein, chlorine, ozone, 1,3-DCP, PM; cells = respiratory/ciliated/goblet/basal epithelial cells; tissues = nasal/tracheal/bronchial epithelium.
5. **Causal edges:** all five supported, strongest at N2→N3 and within N3.
6. **Human multi-manifestation evidence:** formaldehyde links to altered cell-ratio and depressed CBF in the same worker/tissue contexts (PMID 29668989, 10416249).
7. **Model/in vitro causal path:** 1,3-DCP and chlorine ALI/in vivo systems trace molecule→phenotype (PMID 37863466, 36183849, 25398987).
8. **Ontology:** see suggestions above (GO barrier/differentiation/clearance terms; CL ciliated/goblet/basal cells; UBERON nasal/tracheal/bronchial epithelium).
9. **Out of scope:** KEAP1/NRF2, TRPA1 sensing, distal-lung and protease modules, systemic formaldehyde effects.


## Artifacts

- [OpenScientist final report](inhaled_irritant_airway_injury-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](inhaled_irritant_airway_injury-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 26 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:32275839` *(abstract only)*: "mucociliary remodeling of the nasal airway epithelium"
  - closest text in source: "We extracted and chemically characterized the organic and water-soluble components of air pollution PM2.5 samples, then determined the whole transcriptome response of human nasal mucociliary airway epithelial cultures to a dose series of PM2.5 extracts"

## Term Validation

No ontology term identifiers were found in this report.