---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-11-12T18:15:19.211780'
end_time: '2026-11-12T18:24:03.758812'
duration_seconds: 524.55
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: CMP-Sialic Acid Supply Deficiency Module
  module_slug: cmp_sialic_acid_supply_deficiency
  category: Module
  module_description: 'A conserved pathophysiology module for the inborn errors of
    the de novo sialic acid supply chain. The sialyltransferases of the Golgi lumen
    draw on a single activated donor, CMP-sialic acid (CMP-Neu5Ac), which is made
    by a linear pathway split across three compartments: in the cytosol, GNE (UDP-GlcNAc
    2-epimerase/ManNAc kinase), NANS (sialic acid 9-phosphate synthase) and NANP (sialic
    acid 9-phosphate phosphatase) convert UDP-GlcNAc into free sialic acid; in the
    nucleus, CMAS activates it to CMP-sialic acid; and the SLC35A1 antiporter imports
    the donor into the Golgi lumen. Loss of function at any one of these steps converges
    on reduced CMP-sialic acid availability in the Golgi lumen, the key conformance
    target ("Reduced Golgi CMP-Sialic Acid Availability"). Donor shortage then causes
    two parallel molecular lesions, hyposialylation of glycoproteins and a deficit
    in ganglioside sialylation, which surface as tissue-specific consequences that
    depend on which step fails and how severe the residual flux is: distal myofiber
    degeneration (GNE myopathy), accelerated clearance of hyposialylated platelets
    (GNE-related thrombocytopenia, SLC35A1-CDG), podocyte injury (shown in Gne and
    Cmas mouse models), impaired brain development (NANS, CMAS and SLC35A1 deficiency),
    and defective growth-plate skeletal growth (NANS spondyloepimetaphyseal dysplasia).
    Drug-target pattern: oral N-acetylmannosamine (ManNAc) or sialic acid supplementation
    BYPASSES a block in the cytosolic synthesis step and RESTORES the central donor-supply
    node; it cannot bypass a CMAS or SLC35A1 lesion, which sits downstream of where
    the supplements enter. Complementary to congenital_disorder_of_glycosylation,
    which models assembly and processing of the N-glycan itself (ER lipid-linked oligosaccharide
    assembly, Golgi branching and COG trafficking) and has no sialic acid supply arm:
    this module supplies the upstream donor-substrate limb that feeds the terminal
    capping step of both N- and O-glycans and of gangliosides. SLC35A1-CDG may conform
    to both modules.'
  pathophysiology_summary: '- Cytosolic De Novo Sialic Acid Synthesis Block: Trigger
    for the GNE and NANS disorders. In the cytosol, the bifunctional GNE enzyme epimerizes
    UDP-GlcNAc to N-acetylmannosamine (ManNAc) and phosphorylates it to ManNAc 6-phosphate,
    the rate-limiting and feedback-regulated committed step. NANS condenses ManNAc
    6-phosphate with phosphoenolpyruvate to sialic acid 9-phosphate, and a phosphatase
    step attributed to NANP releases free sialic acid (Neu5Ac). Biallelic hypomorphic
    variants in GNE or NANS reduce flux through this arm and lower the free sialic
    acid pool; the phosphatase step is not modelled as a lesion site, because knocking
    out NANP leaves CMP-sialic acid and cell-surface sialylation intact, implying
    an alternative phosphatase. Because exogenous ManNAc enters at the kinase step
    (and can be phosphorylated by GlcNAc kinase) and exogenous sialic acid enters
    below the phosphatase step, this is the only trigger that supplementation can
    bypass.

    - Nuclear Sialic Acid Activation Block: Trigger for CMAS deficiency. CMP-sialic
    acid synthetase (CMAS) is a nuclear enzyme that condenses free sialic acid with
    CTP to form CMP-sialic acid, the only form of sialic acid that the Golgi sialyltransferases
    can use. Loss or mislocalization of CMAS activity leaves the free sialic acid
    pool intact but fails to activate it, so the donor is never made. A lesion here
    lies downstream of where oral ManNAc or sialic acid enters the pathway, which
    is why supplementation that helps the cytosolic arm cannot rescue this one.

    - Golgi CMP-Sialic Acid Import Block: Trigger for SLC35A1-CDG. CMP-sialic acid
    is made outside the Golgi and must be carried across the Golgi membrane by the
    SLC35A1 antiporter before any sialyltransferase can use it. Loss-of-function or
    reduced-activity variants in SLC35A1 leave synthesis of the donor intact but strand
    it in the cytosol, so the luminal donor concentration falls. Like the CMAS lesion,
    and unlike the cytosolic one, this block cannot be bypassed by feeding precursor
    sugars.

    - Reduced Golgi CMP-Sialic Acid Availability: The rate-limiting central effector
    and the key conformance target. All three triggers converge here: whether the
    defect is in making free sialic acid, in activating it to CMP-sialic acid, or
    in carrying the donor across the Golgi membrane, the result is the same single
    state - too little CMP-sialic acid in the Golgi lumen for the resident sialyltransferases
    to work at normal rate. Because this one donor serves every sialyltransferase,
    the shortage is not restricted to one client or one glycan class, and the degree
    of shortage rather than the identity of the failed step sets how severe the downstream
    hyposialylation is.

    - Glycoprotein Hyposialylation: First of the two parallel molecular effectors.
    With the donor pool depleted, N- and O-glycans of secreted and membrane glycoproteins
    are assembled but left without their terminal sialic acid caps. The defect is
    general across clients, but its functional cost is not: it falls hardest on heavily
    sialylated proteins whose negative charge or sialic-acid-dependent recognition
    is load-bearing, such as podocalyxin and nephrin in the podocyte, platelet surface
    glycoproteins, and the sialyl-Lewis-x determinant on leukocytes. Plasma protein
    sialylation can look normal even when tissue sialylation is impaired, which is
    a documented diagnostic pitfall.

    - Ganglioside Sialylation Deficit: Second of the two parallel molecular effectors,
    and the glycolipid counterpart of glycoprotein hyposialylation. The same Golgi
    sialyltransferases and the same donor build gangliosides, the sialylated glycosphingolipids
    that dominate the neuronal surface. A donor shortage therefore limits ganglioside
    synthesis alongside protein sialylation, which matters disproportionately in the
    nervous system because gangliosides are the most abundant neuronal sialoglycans
    and support axon-myelin interactions, axon stability and nerve-cell excitability.

    - Distal Myofiber Degeneration: Skeletal muscle consequence arm, the one GNE myopathy
    runs. Hyposialylated myofibers degenerate progressively in adulthood with a characteristically
    distal, quadriceps-sparing distribution, producing muscle weakness and atrophy.
    Muscle free sialic acid is severely depleted in affected people while total muscle
    sialic acid falls much less, and normal quadriceps itself has a lower sialic acid
    requirement than other muscles - a candidate explanation for the sparing. Mouse
    work indicates that myofiber loss of the enzyme is not by itself sufficient to
    produce the pathology, so a non-myofiber contribution is likely.

    - Accelerated Clearance of Hyposialylated Platelets: Platelet consequence arm,
    the one GNE-related thrombocytopenia and the macrothrombocytopenia of SLC35A1-CDG
    run through. This node is the hepatic removal event itself: platelets whose surface
    glycoproteins have lost their terminal sialic acid are recognized by lectin receptors
    on liver macrophages and cleared from the circulation early. The resulting low
    platelet count and bleeding are phenotypes of the conforming disorders rather
    than part of this node, and whether platelet production is also impaired is contested
    - see the discussion below.

    - Podocyte Hyposialylation Injury: Kidney consequence arm: structural failure
    of the maturing glomerular filtration barrier. That barrier depends on densely
    sialylated podocyte surface proteins - podocalyxin and nephrin - whose negative
    charge keeps the foot processes apart and the slit diaphragm organized, so donor
    shortage during podocyte maturation leaves the foot processes effaced and the
    slit diaphragms absent. The resulting proteinuria and hematuria are phenotypes
    of the conforming entries, not part of this node. Two independent mouse models,
    one at the cytosolic step and one at the activation step, produce this arm; in
    humans proteinuria is reported in SLC35A1-CDG but kidney disease is not a feature
    of adult GNE myopathy, so the arm appears to be developmentally timed - see the
    discussion below.

    - Impaired Brain Development: Neurodevelopmental consequence arm, the dominant
    presentation when the block is severe or lies at the activation or import step.
    Both effector arms feed it: polysialic acid on the neural cell adhesion molecule
    and the neuronal ganglioside coat each require the donor, and both shape development,
    connectivity and excitability. Clinically this arm appears as infantile-onset
    developmental delay and intellectual disability, often with seizures and ataxia,
    in NANS, CMAS and SLC35A1 deficiency.

    - Growth Plate Chondrocyte Dysfunction: Skeletal consequence arm, the one NANS-related
    spondyloepimetaphyseal dysplasia runs. Donor shortage during endochondral growth
    disturbs the growth plate and produces short stature with epiphyseal and metaphyseal
    dysplasia. The arm is supported by loss and rescue in a model organism and by
    the skeletal dysplasia of the affected individuals themselves; the cartilage sialoproteins
    that carry the mechanism are not yet identified.'
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 1
  total_cost_usd: 5.9841581
  session_id: 6acbdd0a-c59e-4844-989b-36205f45743f
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 0
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 15
  validator_version: 0.5.1
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 14
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** CMP-Sialic Acid Supply Deficiency Module
- **Module Slug:** cmp_sialic_acid_supply_deficiency
- **Category:** Module

## Current Module Description

A conserved pathophysiology module for the inborn errors of the de novo sialic acid supply chain. The sialyltransferases of the Golgi lumen draw on a single activated donor, CMP-sialic acid (CMP-Neu5Ac), which is made by a linear pathway split across three compartments: in the cytosol, GNE (UDP-GlcNAc 2-epimerase/ManNAc kinase), NANS (sialic acid 9-phosphate synthase) and NANP (sialic acid 9-phosphate phosphatase) convert UDP-GlcNAc into free sialic acid; in the nucleus, CMAS activates it to CMP-sialic acid; and the SLC35A1 antiporter imports the donor into the Golgi lumen. Loss of function at any one of these steps converges on reduced CMP-sialic acid availability in the Golgi lumen, the key conformance target ("Reduced Golgi CMP-Sialic Acid Availability"). Donor shortage then causes two parallel molecular lesions, hyposialylation of glycoproteins and a deficit in ganglioside sialylation, which surface as tissue-specific consequences that depend on which step fails and how severe the residual flux is: distal myofiber degeneration (GNE myopathy), accelerated clearance of hyposialylated platelets (GNE-related thrombocytopenia, SLC35A1-CDG), podocyte injury (shown in Gne and Cmas mouse models), impaired brain development (NANS, CMAS and SLC35A1 deficiency), and defective growth-plate skeletal growth (NANS spondyloepimetaphyseal dysplasia). Drug-target pattern: oral N-acetylmannosamine (ManNAc) or sialic acid supplementation BYPASSES a block in the cytosolic synthesis step and RESTORES the central donor-supply node; it cannot bypass a CMAS or SLC35A1 lesion, which sits downstream of where the supplements enter. Complementary to congenital_disorder_of_glycosylation, which models assembly and processing of the N-glycan itself (ER lipid-linked oligosaccharide assembly, Golgi branching and COG trafficking) and has no sialic acid supply arm: this module supplies the upstream donor-substrate limb that feeds the terminal capping step of both N- and O-glycans and of gangliosides. SLC35A1-CDG may conform to both modules.

## Current Provisional Nodes

- Cytosolic De Novo Sialic Acid Synthesis Block: Trigger for the GNE and NANS disorders. In the cytosol, the bifunctional GNE enzyme epimerizes UDP-GlcNAc to N-acetylmannosamine (ManNAc) and phosphorylates it to ManNAc 6-phosphate, the rate-limiting and feedback-regulated committed step. NANS condenses ManNAc 6-phosphate with phosphoenolpyruvate to sialic acid 9-phosphate, and a phosphatase step attributed to NANP releases free sialic acid (Neu5Ac). Biallelic hypomorphic variants in GNE or NANS reduce flux through this arm and lower the free sialic acid pool; the phosphatase step is not modelled as a lesion site, because knocking out NANP leaves CMP-sialic acid and cell-surface sialylation intact, implying an alternative phosphatase. Because exogenous ManNAc enters at the kinase step (and can be phosphorylated by GlcNAc kinase) and exogenous sialic acid enters below the phosphatase step, this is the only trigger that supplementation can bypass.
- Nuclear Sialic Acid Activation Block: Trigger for CMAS deficiency. CMP-sialic acid synthetase (CMAS) is a nuclear enzyme that condenses free sialic acid with CTP to form CMP-sialic acid, the only form of sialic acid that the Golgi sialyltransferases can use. Loss or mislocalization of CMAS activity leaves the free sialic acid pool intact but fails to activate it, so the donor is never made. A lesion here lies downstream of where oral ManNAc or sialic acid enters the pathway, which is why supplementation that helps the cytosolic arm cannot rescue this one.
- Golgi CMP-Sialic Acid Import Block: Trigger for SLC35A1-CDG. CMP-sialic acid is made outside the Golgi and must be carried across the Golgi membrane by the SLC35A1 antiporter before any sialyltransferase can use it. Loss-of-function or reduced-activity variants in SLC35A1 leave synthesis of the donor intact but strand it in the cytosol, so the luminal donor concentration falls. Like the CMAS lesion, and unlike the cytosolic one, this block cannot be bypassed by feeding precursor sugars.
- Reduced Golgi CMP-Sialic Acid Availability: The rate-limiting central effector and the key conformance target. All three triggers converge here: whether the defect is in making free sialic acid, in activating it to CMP-sialic acid, or in carrying the donor across the Golgi membrane, the result is the same single state - too little CMP-sialic acid in the Golgi lumen for the resident sialyltransferases to work at normal rate. Because this one donor serves every sialyltransferase, the shortage is not restricted to one client or one glycan class, and the degree of shortage rather than the identity of the failed step sets how severe the downstream hyposialylation is.
- Glycoprotein Hyposialylation: First of the two parallel molecular effectors. With the donor pool depleted, N- and O-glycans of secreted and membrane glycoproteins are assembled but left without their terminal sialic acid caps. The defect is general across clients, but its functional cost is not: it falls hardest on heavily sialylated proteins whose negative charge or sialic-acid-dependent recognition is load-bearing, such as podocalyxin and nephrin in the podocyte, platelet surface glycoproteins, and the sialyl-Lewis-x determinant on leukocytes. Plasma protein sialylation can look normal even when tissue sialylation is impaired, which is a documented diagnostic pitfall.
- Ganglioside Sialylation Deficit: Second of the two parallel molecular effectors, and the glycolipid counterpart of glycoprotein hyposialylation. The same Golgi sialyltransferases and the same donor build gangliosides, the sialylated glycosphingolipids that dominate the neuronal surface. A donor shortage therefore limits ganglioside synthesis alongside protein sialylation, which matters disproportionately in the nervous system because gangliosides are the most abundant neuronal sialoglycans and support axon-myelin interactions, axon stability and nerve-cell excitability.
- Distal Myofiber Degeneration: Skeletal muscle consequence arm, the one GNE myopathy runs. Hyposialylated myofibers degenerate progressively in adulthood with a characteristically distal, quadriceps-sparing distribution, producing muscle weakness and atrophy. Muscle free sialic acid is severely depleted in affected people while total muscle sialic acid falls much less, and normal quadriceps itself has a lower sialic acid requirement than other muscles - a candidate explanation for the sparing. Mouse work indicates that myofiber loss of the enzyme is not by itself sufficient to produce the pathology, so a non-myofiber contribution is likely.
- Accelerated Clearance of Hyposialylated Platelets: Platelet consequence arm, the one GNE-related thrombocytopenia and the macrothrombocytopenia of SLC35A1-CDG run through. This node is the hepatic removal event itself: platelets whose surface glycoproteins have lost their terminal sialic acid are recognized by lectin receptors on liver macrophages and cleared from the circulation early. The resulting low platelet count and bleeding are phenotypes of the conforming disorders rather than part of this node, and whether platelet production is also impaired is contested - see the discussion below.
- Podocyte Hyposialylation Injury: Kidney consequence arm: structural failure of the maturing glomerular filtration barrier. That barrier depends on densely sialylated podocyte surface proteins - podocalyxin and nephrin - whose negative charge keeps the foot processes apart and the slit diaphragm organized, so donor shortage during podocyte maturation leaves the foot processes effaced and the slit diaphragms absent. The resulting proteinuria and hematuria are phenotypes of the conforming entries, not part of this node. Two independent mouse models, one at the cytosolic step and one at the activation step, produce this arm; in humans proteinuria is reported in SLC35A1-CDG but kidney disease is not a feature of adult GNE myopathy, so the arm appears to be developmentally timed - see the discussion below.
- Impaired Brain Development: Neurodevelopmental consequence arm, the dominant presentation when the block is severe or lies at the activation or import step. Both effector arms feed it: polysialic acid on the neural cell adhesion molecule and the neuronal ganglioside coat each require the donor, and both shape development, connectivity and excitability. Clinically this arm appears as infantile-onset developmental delay and intellectual disability, often with seizures and ataxia, in NANS, CMAS and SLC35A1 deficiency.
- Growth Plate Chondrocyte Dysfunction: Skeletal consequence arm, the one NANS-related spondyloepimetaphyseal dysplasia runs. Donor shortage during endochondral growth disturbs the growth plate and produces short stature with epiphyseal and metaphyseal dysplasia. The arm is supported by loss and rescue in a model organism and by the skeletal dysplasia of the affected individuals themselves; the cartilage sialoproteins that carry the mechanism are not yet identified.

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

Kurz gesagt: Ich lese gerade die zwischengespeicherten Abstracts, um daraus wörtliche Zitate für den Bericht zu gewinnen.

Kurz gesagt: Ich lese noch sieben weitere Abstracts, danach schreibe ich den Bericht.

Kurz gesagt: Das Modul ist in dieser Arbeitskopie bereits gebaut; der Bericht unten stützt es und benennt an drei Stellen eine Nachschärfung. Alle 29 Ontologie-Bindungen habe ich gegen die Caches geprüft. Zwei Zitate fehlen noch (siehe letzter Abschnitt) — das ist noch ungeprüft.

---

# Mechanism Module Research Report: CMP-Sialic Acid Supply Deficiency

**Module slug:** `cmp_sialic_acid_supply_deficiency`
**Date:** 2026-11-12
**Scope:** inborn errors of the de novo CMP-sialic acid supply chain (GNE, NANS, CMAS, SLC35A1)

---

## 1. Executive recommendation on name and scope

**Keep the name.** "CMP-Sialic Acid Supply Deficiency" is the correct level of abstraction, and it is better than the two obvious alternatives:

- *"Sialic acid biosynthesis defect"* would be too narrow at the top and too broad at the bottom: it excludes the SLC35A1 transporter, which makes no sialic acid at all, and it invites the lysosomal catabolic disorders (sialidoses, Salla disease) that have nothing to do with donor shortage.
- *"Hyposialylation"* names the **effector**, not the shared cause, and would license conformance from any disease with a sialylation phenotype — including acquired platelet desialylation in immune thrombocytopenia and pathogen-neuraminidase effects, which are not inborn supply failures.

The literature supports the module's central claim as a single biochemical state. Willems et al. established the chain and its compartmentalisation experimentally, knocking out each step in two independent cell lines: *"Biosynthesis of CMP-sialic acid, the essential substrate, comprises five enzymatic steps"* and *"Sialylation of cell surface glycans was reduced by KO of GNE … NANS … and CMAS … genes"* (PMID:31121216). SLC35A1 completes it at the membrane: *"Direct measurement of CMP-sialic acid transport into the Golgi showed a substantial decrease in overall rate of transport"* (PMID:28856833).

**Two scope refinements are supported and should be made explicit in the module's own prose (the current notes already do one of them):**

1. **NANP is correctly excluded as a lesion site, and the exclusion is experimentally grounded**, not merely a lack of reported patients. Willems et al. show the pathway routes around it (§4, §9).
2. **The module should not claim that donor-pool correction is therapeutically sufficient.** The strongest trial evidence is negative (PMID:31036580, PMID:37340906). The module's existing framing — mechanism claim in `target_mechanisms`, clinical outcome in the discussion — is the right separation and should be preserved against reviewer pressure to simplify it.

**One naming caveat worth recording:** the three triggers are not merely three locations of one block. They differ in *what accumulates upstream* (ManNAc in NANS deficiency, free sialic acid in CMAS deficiency, cytosolic CMP-sialic acid in SLC35A1-CDG) and therefore in which supplement can enter below them. That is the substantive reason to keep them as three sibling nodes rather than one parameterised trigger.

---

## 2. Proposed DAG: nodes and causal edges

The module's existing eleven-node structure is supported. Recommended core/optional assignment:

| Node | Role | Conformance status |
|---|---|---|
| Cytosolic De Novo Sialic Acid Synthesis Block | trigger | **Gene-specific** (GNE, NANS) — exactly one trigger per conformer |
| Nuclear Sialic Acid Activation Block | trigger | **Gene-specific** (CMAS) |
| Golgi CMP-Sialic Acid Import Block | trigger | **Gene-specific** (SLC35A1) |
| **Reduced Golgi CMP-Sialic Acid Availability** | central effector | **CORE — required.** The key conformance target |
| Glycoprotein Hyposialylation | effector | **CORE — required** (every conformer demonstrates it) |
| Ganglioside Sialylation Deficit | effector | **Optional** — inferred, not measured in any supply-chain patient (§9) |
| Distal Myofiber Degeneration | consequence | Optional, tissue arm |
| Accelerated Clearance of Hyposialylated Platelets | consequence | Optional, tissue arm |
| Podocyte Hyposialylation Injury | consequence | Optional, tissue arm (developmentally timed, §6) |
| Impaired Brain Development | consequence | Optional, tissue arm |
| Growth Plate Chondrocyte Dysfunction | consequence | Optional, tissue arm |

**Edges and their confidence:**

```
Cytosolic Block ──DIRECT──────────┐
Nuclear Activation Block ─DIRECT──┼──▶ Reduced Golgi CMP-Sialic Acid Availability
Golgi Import Block ──DIRECT───────┘            │
                                               ├──DIRECT──▶ Glycoprotein Hyposialylation
                                               └──INDIRECT_KNOWN──▶ Ganglioside Sialylation Deficit

Glycoprotein Hyposialylation ──DIRECT─────────────▶ Accelerated Platelet Clearance
                             ──DIRECT─────────────▶ Podocyte Hyposialylation Injury
                             ──INDIRECT_UNKNOWN───▶ Distal Myofiber Degeneration
                             ──INDIRECT_UNKNOWN───▶ Growth Plate Chondrocyte Dysfunction
                             ──INDIRECT_KNOWN─────▶ Impaired Brain Development   [via polysialic acid]
Ganglioside Sialylation Deficit ──INDIRECT_KNOWN──▶ Impaired Brain Development   [via ganglioside functions]
```

The two `INDIRECT_UNKNOWN_INTERMEDIATES` edges are correctly graded. For muscle, Chan et al. say so explicitly: *"suggesting a small subset of sialylation targets could be responsible for the pathogenesis of GNEM"* (PMID:28267778). For the growth plate, the rescue experiment establishes sialic-acid dependence without naming any cartilage client (PMID:27213289).

**Note on the central node's evidence structure.** Both edges *into* the central node from the CMAS and SLC35A1 triggers are supported by direct donor-pool or transport measurements. The edge from the cytosolic trigger rests on a **sialylation readout**, not a measured CMP-sialic acid pool, in the human material (PMID:27213289). The direct pool measurement for the cytosolic step exists but is in cell lines: *"CMP-sialic acid was dramatically reduced in GNE and NANS KO cells and undetectable in CMAS KO"* (PMID:31121216). Adding that as a second evidence item on the cytosolic→central edge would close the one soft spot in the convergence claim, and it is `IN_VITRO`.

---

## 3. Gene-to-node mapping

| Gene | HGNC | Step | Trigger node | Documented tissue arms | Supplement bypass possible? |
|---|---|---|---|---|---|
| GNE | `hgnc:4262` | cytosolic epimerase/kinase | Cytosolic Block | muscle, platelet, (kidney — mouse only) | **Yes** — ManNAc and Neu5Ac both enter below |
| NANS | `hgnc:19237` | sialic acid 9-P synthase | Cytosolic Block | brain, growth plate, (platelet — 56% in cohort) | **Yes** — Neu5Ac only; ManNAc accumulates upstream |
| CMAS | `hgnc:19989` | nuclear cytidylyltransferase | Nuclear Activation Block | brain; kidney in mouse | **No** — both supplements enter above the block |
| SLC35A1 | `hgnc:11032` | Golgi antiporter | Golgi Import Block | brain, platelet, kidney, heart | **No** |
| NANP | — | 9-phosphatase | **none (excluded)** | — | not applicable |

*HGNC identifiers above are written from memory and must be looked up before any binding is made — see §10.*

**The asymmetry in the GNE row is important and is a cross-check on the module's ManNAc logic.** ManNAc bypasses a GNE lesion because it is GNE's own product; it cannot bypass a NANS lesion, where ManNAc is the metabolite that accumulates: *"Patient body fluids showed an elevation in N-acetyl-D-mannosamine levels"* (PMID:27213289). So "the cytosolic trigger is the one supplementation can bypass" is true for both genes only if the supplement is sialic acid; for ManNAc it is true of GNE alone. The module's treatment block correctly pairs ManNAc with the cytosolic trigger and sialic acid with the central node, which already encodes this distinction — but the trigger node's description does not, and would read more precisely if it did.

---

## 4. Evidence table

### 4a. Human clinical

| PMID | Study | Exact quote | Supported claim |
|---|---|---|---|
| 28267778 | GNEM patient cohort + mouse, LC/MS/MS | "These results show that serum and muscle free SA is severely reduced in GNEM, which is consistent with the biochemical defect in SA synthesis associated with GNE mutations." | Cytosolic block lowers the free sialic acid pool in affected people |
| 28267778 | same | "Normal quadriceps had significantly lower levels of free SA (reduced by 39%) and total SA (reduced by 53%) compared to normal gastrocnemius." | Regional sialic acid demand as candidate explanation for quadriceps sparing |
| 28267778 | same | "suggesting a small subset of sialylation targets could be responsible for the pathogenesis of GNEM" | Muscle edge has unknown intermediates |
| 27213289 | 9 individuals, biallelic NANS | "We identified biallelic mutations in NANS, the gene encoding the synthase for N-acetylneuraminic acid (NeuNAc; sialic acid), in nine individuals with infantile-onset severe developmental delay and skeletal dysplasia." | One causal factor → two arms (brain + skeleton) in the same people |
| 27213289 | same | "Patient body fluids showed an elevation in N-acetyl-D-mannosamine levels, and patient-derived fibroblasts had reduced NANS activity and were unable to incorporate sialic acid precursors into sialylated glycoproteins." | Synthase-step lesion; substrate accumulates above the block |
| 27213289 | same | "Normal sialylation of plasma proteins was observed in spite of NANS deficiency." | Diagnostic pitfall: plasma glycoform profile does not exclude the mechanism |
| 34163424 | 9 NANS-CDG patients, 6 countries | "Phenotyping confirmed the hallmark features including intellectual developmental disorder (IDD) (n = 9/9; 100%), facial dysmorphisms (n = 9/9; 100%), neurologic impairment (n = 9/9; 100%), short stature (n = 8/9; 89%), skeletal dysplasia (n = 8/9; 89%), and short limbs (n = 8/9; 89%)." | **Multi-arm human evidence with frequencies** — brain and skeletal arms co-occur in nearly all |
| 34163424 | same | "Newly identified features include ophthalmological abnormalities (n = 6/9; 67%), an abnormal septum pellucidum (n = 6/9; 67%), (progressive) cerebral atrophy and ventricular dilatation (n = 5/9; 56%), gastrointestinal dysfunction (n = 5/9; 56%), thrombocytopenia (n = 5/9; 56%)" | **Platelet arm occurs in NANS-CDG too** — currently not reflected in the module's gene-to-arm prose |
| 34163424 | same | "elevated urinary excretion of N-acetylmannosamine (ManNAc) is pathognomonic, the concentrations of which show a significant correlation with clinical severity" | Dose-dependence: degree of pathway blockade tracks severity |
| 23873973 | SLC35A1 patient, Neurology | "We performed biochemical analysis and found combined N- and O-glycosylation abnormalities and specific reduction in sialylation in this patient." | Donor shortage is glycan-class-general |
| 23873973 | same | "Functional analysis of mutant SLC35A1 showed normal Golgi localization but 50% reduction in transport activity of CMP-sialic acid in vitro." | Reduced import, not mislocalisation |
| 23873973 | same | "The primary neurologic presentation consisting of ataxia, intellectual disability, and seizures, in combination with bleeding diathesis and proteinuria" | **Three arms (brain, platelet, kidney) in one individual** |
| 28856833 | SLC35A1 patient, exome | "Patient primary fibroblasts and serum showed a considerable decrease in the amount of N- and O-glycans terminating in sialic acid." | Effector state in patient material |
| 28856833 | same | "Here we report the identification of the third patient with CMP-sialic acid transporter deficiency, who presented with severe neurological phenotype, but without hematological abnormalities." | **Arms are dissociable** — brain arm without platelet arm |
| 15576474 | SLC35A1 complementation, Blood | "We conclude that this defect is a new type of congenital disorder of glycosylation (CDG) of type IIf affecting the transport of CMP-sialic acid into the Golgi apparatus." | First human transporter deficiency; CDG-IIf nosology |
| 42600696 | 4 GNE-RT patients (3 families) | "In all individuals, platelet flow cytometry showed increased RCA-1 and ECL lectin binding and decreased MAL-II binding." | Loss of terminal sialic acid with galactose exposure on circulating platelets |
| 42600696 | same | "The profound megakaryocyte sialylation defect induced by GNE variants does not affect platelet biogenesis." | Argues against a production limb (§9) |
| 42600696 | same | "Sialylation of serum transferrin showed no clear alterations." | Independent replication of the plasma-normal pitfall, in the platelet arm |
| 35052006 | GNE compound het, severe congenital thrombocytopenia | "Lectin array showed decreased α-2,3-sialylation on platelets, consistent with loss of sialic acid synthesis and indicative of rapid platelet clearance." | Linkage-specific sialylation loss → clearance inference |
| 35052006 | same | "Hematopoietic stem cell transplantation (HSCT) normalized platelet counts." | Platelet arm is haematopoietic-cell-intrinsic |
| 34257421 | ManNAc phase 2, n=12 | "Increased plasma Neu5Ac (+2,159 nmol/L, p < 0.0001) and sarcolemmal sialylation (p = 0.0090) were observed at day 90 compared to baseline." | **On-mechanism target engagement in humans** |
| 31036580 | Ace-ER phase 3, n=89 | "Ace-ER was not superior to placebo in improving muscle strength and function in patients with GNE myopathy." | Donor correction ≠ clinical benefit |
| 37340906 | sialic acid in NANS-CDG, n=5 | "In postnatally treated patients, there was no significant improvement." | Same dissociation in the cytosolic/brain arm |
| 37340906 | same | "The effect of sialic acid treatment may depend on the timing, with prenatal treatment potentially benefiting neurodevelopmental outcomes." | Developmental-window hypothesis (weak; n=1 treated prenatally) |

### 4b. Model organism

| PMID | Model | Exact quote | Supported claim |
|---|---|---|---|
| 17549255 | `Gne` M712T knock-in mouse | "Renal findings included segmental splitting of the glomerular basement membrane, effacement of podocyte foot processes, and reduced sialylation of the major podocyte sialoprotein, podocalyxin." | Cytosolic block → podocyte arm, with the client protein named |
| 17549255 | same | "ManNAc administration yielded survival beyond P3 in 43% of the Gne(M712T/M712T) pups. Survivors exhibited improved renal histology, increased sialylation of podocalyxin, and increased Gne/Mnk protein expression and Gne-epimerase activities." | Causal: adding the bypass metabolite reverses both the molecular and the tissue lesion |
| 22745475 | `Cmas`-nls knock-in mouse | "a critical shortage of CMP-sialic acid prevented sialylation of nephrin and podocalyxin in the maturing podocyte where it is required during the formation of foot processes" | **Independent lesion, same arm** — donor shortage, not one enzyme, is the cause |
| 22745475 | same | "Although the Cmas(nls) mouse displayed normal sialylation in all organs including kidney … the sialylation defects progressed with time and paralleled the morphologic changes." | Arm is developmentally timed; global sialylation can look normal |
| 32303557 | Platelet-lineage `Slc35a1` KO | "an increased number of desialylated platelets was cleared by Küpffer cells in the liver of Plt Slc35a1–/– mice" | Import block → hepatic clearance arm |
| 32303557 | same | "The number of bone marrow megakaryocytes in Plt Slc35a1–/– mice was reduced, and megakaryocyte maturation was also impaired." | Production limb (contested, §9) |
| 41417753 | inducible `Gne` deletion, adult mice | "Skeletal myofiber-specific Gne deletion in tamoxifen-treated HSA-CreERT2/+Gnelox/lox mice had no bleeding and no muscle pathology at 60 or 270 days post-treatment." | **Muscle arm is not cell-autonomous to the myofiber** |
| 41417753 | same | "Systemic Gne gene deletion in tamoxifen-treated Rosa-CreERT2/Rosa-CreERT2Gnelox/lox mice caused uniform fatality within 30 days of gene deletion with spontaneous bleeding, thrombocytopenia, and anemia." | One lesion, multiple arms, in adult animals |
| 27213289 | `nansa` zebrafish knockdown | "Knockdown of nansa in zebrafish embryos resulted in abnormal skeletal development, and exogenously added sialic acid partially rescued the skeletal phenotype." | Loss-and-rescue for the growth-plate arm |
| 11929971 | `Gne` germline KO mouse | "inactivation of the UDP-GlcNAc 2-epimerase by gene targeting causes early embryonic lethality in mice" | Complete loss is lethal; all human disease is hypomorphic |
| 11929971 | same | "The need of UDP-GlcNAc 2-epimerase for a defined sialylation process is exemplified with the polysialylation of the neural cell adhesion molecule in embryonic stem cells." | Supply chain → polysialylation, the brain-arm intermediate |
| 23122659 | `Gne` M712T mouse, post-onset dosing | "All three therapies markedly improved the muscle and renal hyposialylation, as evidenced by lectin histochemistry for overall sialylation status and immunoblotting of specific sialoproteins." | Donor node is correctable after symptom onset |

### 4c. In vitro / cellular

| PMID | System | Exact quote | Supported claim |
|---|---|---|---|
| 31121216 | GNE/NANS/CMAS/NANP KO in two cell lines | "CMP-sialic acid was dramatically reduced in GNE and NANS KO cells and undetectable in CMAS KO." | **Direct convergence evidence** on the central node |
| 31121216 | same | "In agreement with normal cell surface sialylation, CMP-sialic acid levels in NANP KO were comparable to WT cells, even though sialic acid 9-phosphate, the substrate of NANP accumulated." | NANP exclusion is positively grounded |
| 31121216 | same | "Our data provide evidence that NANP activity is not essential for de novo sialic acid production and point towards an alternative phosphatase activity, bypassing NANP." | Authors' own conclusion |
| 31121216 | same | "Genetic diseases in this pathway result in different and tissue-restricted phenotypes, which is poorly understood." | The module's own open question, stated by the field |
| 38000033 | NANS-mutant human cortical organoids + `Nans` het mice | "NANS mutation resulted in the absence of both sialic acid and protein polysialylation in the cortical organoids and notably reduced the proliferation and expansion of neural progenitors." | **Molecular perturbation → cellular brain phenotype, in human tissue** |
| 38000033 | same | "NANS mutation dysregulated neural migration and differentiation, disturbed synapse formation, and weakened neuronal activity." | Mechanistic content of the brain arm |
| 38000033 | same | "Similarly, Nans heterozygous mice exhibited impaired cortical neurogenesis and neurobehavioral deficits." | Cross-species corroboration |
| 31495922 | CMAS p.Arg188His, consanguineous ID pedigree | "Conservation analysis, structural prediction, and enzyme activity experiments demonstrated that (p.Arg188His) influences protein dimerization and alters CMAS enzyme activity." | Activation-step lesion in humans |
| 9689047 | murine CMAS cloning, CHO lec32 complementation | "Three potential nuclear localization signals were found in the murine synthetase, and immunofluorescence studies confirmed predominantly nuclear localization of an N-terminally Flag-tagged molecule." | Nuclear compartment of the activation step |
| 9689047 | same | "A prerequisite for the synthesis of sialylated glycoconjugates is the activated sugar-nucleotide cytidine 5'-monophosphate N-acetylneuraminic acid (CMP-Neu5Ac), which provides a substrate for Golgi sialyltransferases." | The module's founding premise |

### 4d. Review / synthesis

| PMID | Exact quote | Supported claim | Grading |
|---|---|---|---|
| 24692354 | "Gangliosides, sialylated glycosphingolipids, are the most abundant sialoglycans of nerve cells." | Why the glycolipid arm is neurally weighted | `OTHER` + `REVIEW_SYNTHESIS` |
| 24692354 | "Mouse genetic studies and human disorders of ganglioside metabolism implicate gangliosides in axon-myelin interactions, axon stability, axon regeneration, and the modulation of nerve cell excitability." | Ganglioside → brain intermediates | `OTHER` + `REVIEW_SYNTHESIS` |
| 24692354 | "Polysialic acid is essential for appropriate brain development, and polymorphisms in the human genes responsible for polysialic acid biosynthesis are associated with psychiatric disorders" | Glycoprotein → brain intermediate | `OTHER` + `REVIEW_SYNTHESIS` |
| 32303557 | "Sialic acid is a common terminal residue of glycans on proteins and acidic sphingolipids such as gangliosides and has important biological functions." | One donor caps both effector arms | `OTHER` + `BACKGROUND` (framing sentence of a mouse paper) |

---

## 5. Direct human evidence for one cause → multiple manifestations

This is the strongest argument that the module is a module and not four unrelated diseases. Three independent human lines:

1. **One individual, three arms.** The SLC35A1 patient of PMID:23873973 carried ataxia, intellectual disability and seizures *"in combination with bleeding diathesis and proteinuria"* — the brain, platelet and kidney arms in one person with one 50%-activity transporter variant.
2. **One cohort, arms with frequencies.** NANS-CDG (PMID:34163424): IDD 9/9, skeletal dysplasia 8/9, thrombocytopenia 5/9. The platelet arm is therefore **not confined to GNE and SLC35A1**, which the module's description currently implies.
3. **Dose-response within one gene.** In the same cohort, urinary ManNAc concentration *"show[s] a significant correlation with clinical severity"* — residual pathway flux, not lesion identity, sets severity, exactly as the central node asserts.

And one negative that sharpens the claim: the third SLC35A1 patient presented *"with severe neurological phenotype, but without hematological abnormalities"* (PMID:28856833). The arms are **dissociable**, so they are correctly modelled as optional siblings rather than an obligate set.

---

## 6. The kidney arm: a genuine human/model mismatch

Worth recording carefully, because the model evidence is stronger than the human evidence and in the opposite direction from the usual pattern.

- **Mouse, two independent lesions, florid phenotype.** `Gne` M712T: *"the first genetic model of podocyte injury and segmental glomerular basement membrane splitting due to hyposialylation"* (PMID:17549255). `Cmas`-nls: *"podocyte foot process effacement, absence of slit diaphragms, and massive proteinuria"* (PMID:22745475).
- **Human:** proteinuria is reported in SLC35A1-CDG (PMID:23873973) but renal disease is not a feature of adult GNE myopathy.
- **The reconciling observation is in the mouse data itself.** Weinhold et al.: *"sialylation is critical during the development of the glomerular filtration barrier"*, and the defect *"progressed with time and paralleled the morphologic changes"*. Both mouse models are **perinatal**; `Gne(M712T/M712T)` mice *"did not survive beyond P3"* and showed *"no myopathic features"*.

So the arm is plausibly **developmentally gated**: a donor shortage severe enough during glomerular maturation produces it, and an adult-onset hypomorph does not. That is an interpretation, not a demonstration — the module's existing `HUMAN_MODEL_MISMATCH`-shaped discussion is the right place for it, and it should not be upgraded to a claim.

---

## 7. Ontology recommendations

**All 29 bindings currently in the module resolve in the committed caches with exactly matching labels. Das habe ich selbst geprüft** (against `cache/go/terms.csv`, `cache/cl/terms.csv`, `cache/uberon/terms.csv`).

**GO — molecular function (trigger nodes):**

| CURIE | Label | Node |
|---|---|---|
| `GO:0008761` | UDP-N-acetylglucosamine 2-epimerase activity | Cytosolic Block |
| `GO:0009384` | N-acylmannosamine kinase activity | Cytosolic Block |
| `GO:0050462` | N-acetylneuraminate synthase activity | Cytosolic Block |
| `GO:0008781` | N-acylneuraminate cytidylyltransferase activity | Nuclear Activation Block |
| `GO:0005456` | CMP-N-acetylneuraminate transmembrane transporter activity | Golgi Import Block |

**GO — biological process:**

| CURIE | Label | Node |
|---|---|---|
| `GO:0046380` | N-acetylneuraminate biosynthetic process | Cytosolic Block |
| `GO:0006055` | CMP-N-acetylneuraminate biosynthetic process | Nuclear Activation Block |
| `GO:0015782` | CMP-N-acetylneuraminate transmembrane transport | Golgi Import Block |
| `GO:0046381` | CMP-N-acetylneuraminate metabolic process | **central node** |
| `GO:1990743` | protein sialylation | Glycoprotein Hyposialylation |
| `GO:0001574` | ganglioside biosynthetic process | Ganglioside Sialylation Deficit |
| `GO:0072015` | podocyte development | Podocyte arm |
| `GO:0007420` | brain development | Brain arm |
| `GO:0003417` | growth plate cartilage development | Growth-plate arm |

**GO — cellular component:** `GO:0005829` cytosol · `GO:0005634` nucleus · `GO:0000139` Golgi membrane · `GO:0005796` Golgi lumen. These four carry the compartmental logic that distinguishes the three triggers, and are the reason the module can state which lesion a supplement can bypass.

**CL:** `CL:0008002` skeletal muscle fiber · `CL:0000233` platelet · `CL:0000091` Kupffer cell · `CL:0000653` podocyte · `CL:0000540` neuron · `CL:0000138` chondrocyte.

**UBERON:** `UBERON:0001134` skeletal muscle tissue · `UBERON:0002107` liver · `UBERON:0000074` renal glomerulus · `UBERON:0000955` brain · `UBERON:0002516` epiphyseal plate.

**Gaps and judgement calls:**

- **The central node has no ideal GO term.** `GO:0046381` is a *metabolic process*, not a donor pool; GO has no class for "availability of a nucleotide-sugar donor in a compartment". `GO:0046381` with `modifier: DECREASED` plus `GO:0005796` Golgi lumen is the best available composition. Do not manufacture something narrower.
- **No ganglioside-specific sialyltransferase-activity term is needed**; the biosynthetic process term carries the claim at the right level.
- **No CHEBI or MONDO in nodes** (module convention). `CHEBI:63153` N-acetyl-D-mannosamine and `CHEBI:17012` N-acetylneuraminic acid appear only in `treatments[].therapeutic_agent`, which is the schema-sanctioned exception.
- **Candidate additions not currently bound, offered by label only:** a polysialylation process term for the brain-arm intermediate; a megakaryocyte CL term, *if and only if* the production controversy (§9) resolves toward a production limb. Neither should be added before the identifier is read from a lookup.

---

## 8. Out-of-scope boundary notes

These are conformance-blocking exclusions. Each has a positive reason, not merely an absence of evidence.

| Excluded | Why |
|---|---|
| **Sialuria (GNE allosteric GOF)** | Loss of CMP-sialic acid feedback inhibition → **over**production and cytosolic accumulation of free sialic acid. Same gene, opposite flux direction. A `GAIN_OF_FUNCTION` modifier on the same node would not rescue this — the downstream state is not donor shortage. |
| **Sialidoses (NEU1), galactosialidosis (CTSA)** | Lysosomal **catabolic** defects with storage of sialylated material. Donor supply is intact. |
| **Free sialic acid storage disease (SLC17A5): Salla and infantile forms** | Lysosomal **efflux** defect. Free sialic acid accumulates in the lysosome; the Golgi donor pool is not the lesion. Tempting because the metabolite and the neurodevelopmental picture overlap. |
| **NANP** | Excluded on positive experimental grounds (PMID:31121216), not for want of patients. Do not route a conformer through it without evidence overturning that result. |
| **Acquired platelet desialylation** (immune thrombocytopenia, pathogen neuraminidase, cold storage) | Terminal sialic acid is **removed** from a normally sialylated surface; no supply-chain lesion. Shares the hepatic-clearance node's biology but not its cause — this is the main false-positive risk if the module is ever renamed around hyposialylation. |
| **Sialyltransferase deficiencies** (e.g. ST3GAL/ST8SIA defects) | The donor is present and a specific transferase is missing. A plausible *sibling* module, not this one. |
| **Stage, severity, and clinical phenotypes** | Thrombocytopenia, bleeding, proteinuria, short stature, developmental delay are phenotypes of conforming **disease entries**; the nodes stop at the pathological event. |

**Relation to `congenital_disorder_of_glycosylation`:** complementary, not overlapping. That module models assembly and processing of the glycan (ER LLO assembly, Golgi branching, COG trafficking) and has no donor-supply arm; this one supplies the terminal-capping substrate for N-glycans, O-glycans and gangliosides alike. SLC35A1-CDG legitimately conforms to both — it is a CDG-II by nosology (PMID:15576474) and a donor-import failure by mechanism.

---

## 9. Speculative, weakly supported, or contested

**(a) The ganglioside arm is inferred, not measured.** No paper in this set measures ganglioside content in a patient or animal with a supply-chain lesion. The biochemistry is unimpeachable — *"Sialic acid is a common terminal residue of glycans on proteins and acidic sphingolipids such as gangliosides"* (PMID:32303557) — and the neuronal importance is review-grade (PMID:24692354), but the node currently rests on `OTHER`-graded background and review quotes. **Keep it optional, keep the `INDIRECT_KNOWN_INTERMEDIATES` grade, and record explicitly that no direct measurement exists.** Measuring gangliosides in NANS-CDG or SLC35A1-CDG fibroblasts is the obvious closing experiment.

**(b) Platelet production versus clearance is genuinely open.** Mouse: *"The number of bone marrow megakaryocytes in Plt Slc35a1–/– mice was reduced, and megakaryocyte maturation was also impaired"* (PMID:32303557). Human: *"The profound megakaryocyte sialylation defect induced by GNE variants does not affect platelet biogenesis"* (PMID:42600696). The candidate explanations — species, complete-null versus hypomorph, and *in vitro* salvage from sialic-acid-containing medium — are not separable from the published data. Therapeutically live: the same human series reports that *"55% of GNE-RT patients respond to thrombopoietin mimetics"*, a production-side intervention in a mechanism modelled here as pure clearance. The module's existing `CONTROVERSY` discussion and paired-measurement experiment are the right treatment.

**(c) Target engagement without clinical benefit.** ManNAc raises plasma Neu5Ac and sarcolemmal sialylation (PMID:34257421); extended-release sialic acid did not beat placebo on muscle strength (PMID:31036580); oral sialic acid showed *"no significant improvement"* in postnatally treated NANS-CDG (PMID:37340906). Three readings are on the table and the data do not choose between them: (i) the therapeutic window is developmental, (ii) a measured bulk sialylation increase does not reach the small critical client subset, (iii) the donor-shortage model is incomplete for the muscle phenotype. **Do not let the module's `target_mechanisms` imply benefit.** `ACTIVATES` on the central node is a mechanism claim and is supported; clinical efficacy is a separate, currently negative, claim.

**(d) The quadriceps-sparing explanation is a hypothesis.** Chan et al. offer it as one: *"A lower SA requirement for quadriceps may be linked to the reported quadriceps sparing in GNEM."* It is a correlation between two measurements in normal muscle, and it does not explain the distal distribution.

**(e) The muscle arm's cell of action is unresolved.** PMID:41417753 shows myofiber-restricted deletion produces no pathology while broad deletion does, and concludes that disease *"requires loss of gene GNE expression in cell types beyond skeletal myofibers"*. Which cell type is unknown. The module should not name one.

**(f) Prenatal treatment benefit rests on n=1.** PMID:37340906 compares one prenatally treated patient with two genotypically identical patients. The authors say so themselves: *"Evidence is limited."* Do not strengthen this.

**(g) CMAS is the thinnest human arm.** One consanguineous pedigree with nonsyndromic intellectual disability and functional support for the variant (PMID:31495922). There is no CMAS-CDG cohort comparable to NANS-CDG. A targeted search for additional CMAS patients returned nothing usable this session. The trigger node is justified by the pathway's biochemistry plus the `Cmas`-nls mouse; the **human** disease arm is a single family and should be described that way.

---

## 10. Open questions and curator actions

**Verification required before curation:**

1. **Two references are identified but not quotable from this session.** `PMID:30171045` (Revel-Vilk et al., *Blood* 2018, "GNE variants causing autosomal recessive macrothrombocytopenia without associated muscle wasting") and `PMID:25257349` (Izumi et al., *Neuromuscul Disord* 2014, "GNE myopathy associated with congenital thrombocytopenia: a report of two siblings"). Titles come from a PubMed esummary lookup; **I have read no abstract text for either and have invented no quote.** Both are directly on the platelet-arm/muscle-arm dissociation and should be fetched (`just fetch-reference PMID:30171045`) before being cited.
2. **`references_cache/PMID_29941673.md` has an empty body.** The Futterer et al. *Blood* 2018 record caches as title and metadata only — it is a letter. Nothing can be quoted from it as cached; `--force` may or may not help, and it should not be cited until a curator has looked.
3. **`PMID:36224347`** (three Japanese NANS-CDG patients) is cached but I read only its title. Potentially useful for arm frequencies independent of the Radboudumc cohort; needs reading.
4. **Every HGNC identifier in §3 was written from memory and must be looked up** before any binding. `hgnc:4262`, `hgnc:19237`, `hgnc:19989`, `hgnc:11032` are offered as leads only, exactly as a deep-research CURIE is a lead.

**Substantive questions for a curator:**

5. **Should the platelet arm be listed for NANS?** PMID:34163424 reports thrombocytopenia in 5/9 NANS-CDG patients. The module's description currently attributes the platelet arm to GNE and SLC35A1. Either the description should add NANS, or the omission should be justified (the cohort does not report platelet sialylation, so the arm's *mechanism* in NANS is unestablished even where the phenotype is present).
6. **Should the cytosolic trigger's description distinguish ManNAc from sialic acid bypass?** It is true that the cytosolic arm is the one supplementation can bypass; it is not true that *ManNAc* bypasses a NANS lesion. See §3.
7. **Should the in-vitro donor-pool measurement be added to the cytosolic→central edge?** PMID:31121216's *"CMP-sialic acid was dramatically reduced in GNE and NANS KO cells"* is the only direct pool measurement for that trigger and would close the softest link in the convergence claim.
8. **Does a sialyltransferase-deficiency module belong beside this one?** If so, this module's central node becomes its upstream boundary, and the shared downstream effectors would need a decision about which module owns them.
9. **Ganglioside measurement in patient material** — the single experiment that would move the ganglioside node from inferred to demonstrated.

Kurz gesagt: Der Hintergrundprozess, der zusätzliche PubMed-Suchen laufen lassen sollte, ist mit Exit-Code 1 gescheitert — die Ausgabedatei ist leer geblieben. Für den Bericht ist das ohne Folgen: ich hatte dieselben Suchen danach einzeln und mit Wartepausen nachgeholt (PubMed hatte mit HTTP 429, also einer Ratenbegrenzung, geantwortet), und genau zwei Treffer kamen dabei heraus — `PMID:30171045` und `PMID:25257349`. Beide stehen im Bericht unter Punkt 10 als noch zu holende Referenzen, ausdrücklich ohne Zitat.

Ein schönes Wort dafür wäre: **Anfragenüberdruss** (the server's weariness of too many requests).

Was damit offen bleibt, und zwar unverändert offen: die dritte Suche, nach weiteren CMAS-Patienten, lieferte kein Ergebnis. Das heißt nicht, dass es keine gibt — eine Suche ohne Treffer ist Schweigen, keine Negativaussage. Der Bericht sagt das unter Punkt 9(g) so, und das sollte er auch sagen.

Der Bericht selbst steht vollständig in meiner vorigen Antwort. Die 29 Ontologie-Bindungen habe ich gegen die Caches geprüft; die vier HGNC-Kennungen in Abschnitt 3 habe ich aus dem Gedächtnis geschrieben und als solche gekennzeichnet — die müssen vor jeder Bindung nachgeschlagen werden.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 14 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.