---
provider: claude_code
model: claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-11-12T18:15:34.739199'
end_time: '2026-11-12T18:20:15.031855'
duration_seconds: 280.29
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
  - claude-opus-5
  - claude-opus-5-5
  num_turns: 17
  total_cost_usd: 3.8557663999999994
  session_id: 14d85b06-a85e-43cf-9385-b6bf0214e017
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 2
citation_count: 0
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 19
  validator_version: 0.5.1
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 16
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

Let me read the files directly.

Ooh. The supply chain is one pipe with three valves, and the literature agrees. Here is the report.

---

# Mechanism Module Research Report
## CMP-Sialic Acid Supply Deficiency Module (`cmp_sialic_acid_supply_deficiency`)

**Prepared:** 2026-11-12 · **Scope:** dismech mechanism module, not a disease entry
**Evidence base:** 20 primary and review sources, all PMID-identified; every quote below is an exact substring of the cached `references_cache/` body for that PMID unless flagged as needing full-text verification.

---

## 1. Executive Recommendation: Name and Scope

**Keep the name. Keep the scope. Tighten one boundary and one node label.**

The literature supports the module as framed, and supports it unusually cleanly, because the biology has a genuine single bottleneck rather than a notional one. Every sialyltransferase in the Golgi lumen — the ones that cap N-glycans, the ones that cap O-glycans, and the ones that build gangliosides — draws on one activated donor, CMP-N-acetylneuraminic acid (CMP-Neu5Ac). That is stated as a prerequisite, not an inference, in the paper that cloned the mammalian synthetase (PMID:9689047): *"A prerequisite for the synthesis of sialylated glycoconjugates is the activated sugar-nucleotide cytidine 5'-monophosphate N-acetylneuraminic acid (CMP-Neu5Ac), which provides a substrate for Golgi sialyltransferases."* A module organized around the availability of that one molecule is therefore organized around a real rate-limiting state, which is what a mechanism module should be.

**The name is right, and better than the obvious alternatives.** Three candidate names were weighed:

| Candidate | Verdict |
|---|---|
| **CMP-Sialic Acid Supply Deficiency** (current) | **Keep.** Names the shared deficient state (the donor), not any one enzyme, and the word *supply* correctly covers synthesis, activation and transport without implying all three fail together. |
| "Sialic Acid Biosynthesis Deficiency" | Reject. *Biosynthesis* excludes the SLC35A1 transport lesion, which synthesizes the donor perfectly well and merely fails to deliver it. It would also wrongly invite sialuria (overproduction) and the lysosomal catabolic disorders as conformers, since both are "sialic acid metabolism". |
| "Hyposialylation Module" | Reject as the module name, though correct as an effector node name. Hyposialylation has causes outside this supply chain entirely — individual sialyltransferase deficiencies (ST3GAL3, ST3GAL5), Golgi pH and ion-homeostasis defects, loss of the sialyltransferases' acceptor substrate. Naming the module for the effector would make every one of those a conformer and dissolve the module's explanatory content. |

**One boundary to tighten.** The description's final sentence — "SLC35A1-CDG may conform to both modules" — is correct but soft. The literature supports stating this positively: SLC35A1-CDG *is* a CDG type II by its own defining publication (PMID:15576474: *"We conclude that this defect is a new type of congenital disorder of glycosylation (CDG) of type IIf affecting the transport of CMP-sialic acid into the Golgi apparatus."*), so dual conformance to `congenital_disorder_of_glycosylation` and to this module is the expected state for that entry, not an option. Recommend replacing *may conform* with *conforms*.

**One node label to reconsider.** "Impaired Brain Development" is the weakest node name in the set — it names an outcome rather than a mechanism, and it is doing double duty for prenatal neurogenesis failure (NANS, CMAS) and for postnatal neurological deterioration. See §9, open question 3.

---

## 2. Best-Supported Shared Mechanism (Question 1)

The conserved chain, stated at the level the evidence actually supports:

> A biallelic loss-of-function lesion at any one of three compartment-separated steps — cytosolic de novo synthesis of free Neu5Ac (GNE, NANS), nuclear activation of Neu5Ac to CMP-Neu5Ac (CMAS), or antiport of CMP-Neu5Ac across the Golgi membrane (SLC35A1) — lowers the concentration of CMP-Neu5Ac in the Golgi lumen below the requirement of the resident sialyltransferases. Because that one donor is shared across every sialyltransferase and every acceptor class, the shortage propagates to two parallel molecular effectors, hyposialylation of N- and O-glycans on glycoproteins and a deficit in ganglioside sialylation. Which tissue then fails is set not by the identity of the broken step but by residual flux through it and by that tissue's reliance on de novo synthesis rather than salvage.

Three features of that statement are load-bearing and each is independently evidenced.

**The convergence is real, not assumed.** The strongest single demonstration is the comparison of two independent mouse lesions at two different steps producing the same tissue arm. The cytosolic lesion (`Gne` M712T knock-in, PMID:17549255) gives *"segmental splitting of the glomerular basement membrane, effacement of podocyte foot processes, and reduced sialylation of the major podocyte sialoprotein, podocalyxin."* The activation-step lesion (`Cmas-nls` knock-in, PMID:22745475) gives *"podocyte foot process effacement, absence of slit diaphragms, and massive proteinuria."* Two different enzymes, two different compartments, one phenotype — that is the module's central claim tested and passed.

**The shortage is non-selective across glycan classes.** In SLC35A1-CDG patient material, *"Patient primary fibroblasts and serum showed a considerable decrease in the amount of N- and O-glycans terminating in sialic acid"* (PMID:28856833), and in an independent patient, *"combined N- and O-glycosylation abnormalities and specific reduction in sialylation in this patient"* (PMID:23873973). A client-specific or glycan-class-specific defect would not look like that. This is what justifies modelling a single donor-pool node upstream of two parallel effectors rather than separate per-client arms.

**Severity tracks residual flux, not step identity.** Complete loss is embryonic-lethal: *"inactivation of the UDP-GlcNAc 2-epimerase by gene targeting causes early embryonic lethality in mice"* (PMID:11929971). Every human disorder in this module is therefore hypomorphic by construction — a null at any step is not a disease, it is a failed pregnancy. That one fact explains the module's otherwise puzzling clinical range: adult-onset distal myopathy from mildly hypomorphic GNE alleles, infantile multisystem disease from more severe NANS or SLC35A1 alleles. NANS-CDG supplies the quantitative version: in a nine-patient cohort, *"elevated urinary excretion of N-acetylmannosamine (ManNAc) is pathognomonic, the concentrations of which show a significant correlation with clinical severity"* (PMID:34163424) — the metabolite immediately upstream of the block scales with how badly the patient is affected.

---

## 3. Proposed DAG: Nodes and Causal Edges

The current eleven-node structure is sound. Recommended as-is, with the tier assignments below.

```
TRIGGERS (three siblings; a conformer enters through exactly one)
  [T1] Cytosolic De Novo Sialic Acid Synthesis Block      GNE, NANS
  [T2] Nuclear Sialic Acid Activation Block               CMAS
  [T3] Golgi CMP-Sialic Acid Import Block                 SLC35A1
        │       │       │
        └───────┼───────┘   all three → DIRECT
                ▼
CENTRAL EFFECTOR (key conformance target)
  [C]  Reduced Golgi CMP-Sialic Acid Availability
                │
        ┌───────┴────────┐
        ▼                ▼
MOLECULAR EFFECTORS (two parallel arms)
  [E1] Glycoprotein      [E2] Ganglioside
       Hyposialylation        Sialylation Deficit
        │                      │
        ├──────────────────────┼──────────► [X5] Impaired Brain Development
        ├─► [X1] Distal Myofiber Degeneration
        ├─► [X2] Accelerated Clearance of Hyposialylated Platelets
        ├─► [X3] Podocyte Hyposialylation Injury
        └─► [X4] Growth Plate Chondrocyte Dysfunction
```

**Edge confidence, as curated and as the evidence warrants:**

| Edge | Link type | Basis |
|---|---|---|
| T1 → C | DIRECT | Patient fibroblasts cannot route precursor into sialylated glycoproteins (PMID:27213289). Note: the CMP-Neu5Ac pool itself was not measured; the edge rests on a sialylation readout. Honest as curated. |
| T2 → C | DIRECT | *"a critical shortage of CMP-sialic acid prevented sialylation of nephrin and podocalyxin"* (PMID:22745475) — the pool is named directly. Strongest of the three. |
| T3 → C | DIRECT | *"Direct measurement of CMP-sialic acid transport into the Golgi showed a substantial decrease in overall rate of transport"* (PMID:28856833). Direct measurement of the transport step in patient cells. |
| C → E1 | DIRECT | Combined N- and O-glycan sialylation loss in patients (PMID:23873973, PMID:28856833). |
| C → E2 | INDIRECT_KNOWN_INTERMEDIATES | **Correctly provisional.** Shared-biochemistry argument plus a background sentence; no direct ganglioside measurement in a supply-chain patient. See §9, open question 1. |
| E1 → X1 (muscle) | INDIRECT_UNKNOWN_INTERMEDIATES | **Correctly provisional.** The critical client sialoproteins are unidentified; authors infer *"a small subset of sialylation targets could be responsible for the pathogenesis of GNEM"* (PMID:28267778). |
| E1 → X2 (platelet) | DIRECT | Mouse clearance (PMID:32303557) plus patient lectin flow cytometry (PMID:42600696). Mechanistically the best-resolved arm in the module. |
| E1 → X3 (podocyte) | DIRECT | Named client protein (podocalyxin) with measured hyposialylation and the structural lesion in the same animals (PMID:17549255). |
| E1 → X4 (skeletal) | INDIRECT_UNKNOWN_INTERMEDIATES | **Correctly provisional.** Loss-and-rescue in zebrafish; cartilage client proteins unidentified. |
| E1/E2 → X5 (brain) | INDIRECT_KNOWN_INTERMEDIATES | Polysialic acid (glycoprotein arm) and gangliosides (glycolipid arm) are both named intermediates (PMID:24692354), and the organoid work now supplies a direct test — see below. |

**One edge is now better supported than its curated confidence suggests.** The E1 → X5 brain edge should be re-read against the human cortical organoid study (PMID:38000033), which is the only experiment in this corpus that goes from a supply-chain lesion to a neurodevelopmental cellular phenotype in human tissue: *"NANS mutation resulted in the absence of both sialic acid and protein polysialylation in the cortical organoids and notably reduced the proliferation and expansion of neural progenitors."* That identifies the intermediate (loss of protein polysialylation) and the cellular consequence (progenitor proliferation failure) in one human system, which is stronger than the review citation currently carrying the edge. Recommend adding it as a second evidence item on that edge, graded `IN_VITRO`, with the mouse arm of the same paper available separately as `MODEL_ORGANISM` (*"Nans heterozygous mice exhibited impaired cortical neurogenesis and neurobehavioral deficits"*).

---

## 4. Core vs Optional Nodes for Conformance (Question 3)

| Node | Status | Rationale |
|---|---|---|
| [C] Reduced Golgi CMP-Sialic Acid Availability | **Core — the key conformance target** | The one state every conformer shares. A disorder that does not reach this state is not in this module. |
| [T1]/[T2]/[T3] | **Core, but exactly one per conformer** | These are mutually exclusive siblings selected by the compartment of the lesion, not a chain. Conforming to two triggers would be a curation error. |
| [E1] Glycoprotein Hyposialylation | **Core in practice** | Every human disorder in the module demonstrates it. A conformer should carry it unless it has specifically shown otherwise. |
| [E2] Ganglioside Sialylation Deficit | **Optional** | Biochemically obligate, clinically unmeasured in these disorders. A conformer should carry it only where it has a reason to — effectively, the neurodevelopmental entries. |
| [X1] Distal Myofiber Degeneration | **Gene-specific: GNE** | No other gene in the module produces it. |
| [X2] Platelet clearance | **Optional: GNE, SLC35A1, NANS** | Present in GNE-related thrombocytopenia, in SLC35A1-CDG, and in 5/9 of the NANS cohort (PMID:34163424) — broader than first assumed. |
| [X3] Podocyte injury | **Optional, and species-weighted** | Two mouse models; in humans reported in SLC35A1-CDG but *not* a feature of adult GNE myopathy. See §9, open question 2. |
| [X4] Growth plate | **Gene-specific: NANS** | The skeletal dysplasia is the defining feature of NANS-CDG and is absent from the other entries. |
| [X5] Impaired Brain Development | **Optional: NANS, CMAS, SLC35A1** | Absent from adult-onset GNE myopathy, dominant in the other three. |

**The structural point for curators:** the three triggers and the single central node are the module's skeleton; the five tissue arms are a *menu*, not a sequence. An entry attaches the arms its disease shows and no others. This is why `just check-conformance-content` will report `edges_absent` on legitimate conformers here, and those reports are expected rather than defects.

---

## 5. Gene-to-Node Mapping

| Gene | Step | Compartment | Trigger | Tissue arms evidenced | Supplementation-rescuable? |
|---|---|---|---|---|---|
| **GNE** (UDP-GlcNAc 2-epimerase / ManNAc kinase) | Epimerase + kinase; rate-limiting, CMP-Neu5Ac feedback-regulated | Cytosol | T1 | X1 muscle, X2 platelet, X3 podocyte (mouse) | **Yes** — ManNAc enters below the epimerase; GlcNAc kinase can phosphorylate it if the kinase domain is lost |
| **NANS** (Neu5Ac-9-phosphate synthase) | Condenses ManNAc-6-P with PEP | Cytosol | T1 | X4 skeletal, X5 brain, X2 platelet (5/9) | **Yes** — sialic acid enters below the synthase |
| **NANP** (Neu5Ac-9-phosphatase) | Dephosphorylation | Cytosol | **Not a lesion site** | — | n/a |
| **CMAS** (CMP-Neu5Ac synthetase) | Activation with CTP | **Nucleus** | T2 | X5 brain (human), X3 podocyte (mouse) | **No** — lesion is downstream of where both supplements enter |
| **SLC35A1** (CMP-Neu5Ac antiporter) | Golgi import | Golgi membrane | T3 | X2 platelet, X5 brain, X3 podocyte (human proteinuria) | **No** — same reason |

**Two mapping decisions deserve their evidence stated.**

*NANP is correctly excluded as a lesion site.* The knockout result is unambiguous and is recorded in the module as a `REFUTE` item, which is the right grading: *"In agreement with normal cell surface sialylation, CMP-sialic acid levels in NANP KO were comparable to WT cells, even though sialic acid 9-phosphate, the substrate of NANP accumulated"* (PMID:31121216). Substrate accumulates, product is normal — an alternative phosphatase carries the step. No human NANP disease has been established. Do not route a conformer through NANP.

*CMAS is nuclear, and that is not a curiosity.* It was established at cloning (PMID:9689047 title: *"a nuclear protein with evolutionarily conserved structural motifs"*), and it is the reason the `Cmas-nls` mouse works as an experiment at all — the lesion in that model is forced nuclear retention, i.e. mislocalization rather than catalytic death. It is also the reason T2 must be a separate trigger from T1: the compartment boundary is exactly where the supplementation logic breaks.

---

## 6. Human Evidence Linking One Causal Factor to Multiple Manifestations (Question 6)

This is the question that most strongly justifies a module rather than separate per-gene chains, and the evidence is good.

**One SLC35A1 patient, three arms at once.** *"The primary neurologic presentation consisting of ataxia, intellectual disability, and seizures, in combination with bleeding diathesis and proteinuria"* (PMID:23873973). Brain, platelet and kidney in one individual with one transport defect. This is the module's thesis in a single sentence of a case description.

**One NANS cohort, five arms graded.** The nine-patient NANS-CDG series (PMID:34163424) reports intellectual developmental disorder 9/9, neurologic impairment 9/9, short stature 8/9, skeletal dysplasia 8/9, and — newly — *"thrombocytopenia (n = 5/9; 56%)"*. The platelet arm in NANS was not anticipated from the gene's reputation and emerged from systematic phenotyping. A second, independent series makes the same point from the other direction: a Japanese patient with *"marked hydrocephalus, spondyloepimetaphyseal dysplasia (SEMD), and thrombocytopenia"* (PMID:36224347).

**One GNE gene, two clinically separate diseases.** Distal myopathy and isolated severe congenital thrombocytopenia both arise from biallelic GNE variants (PMID:29941673, PMID:35052006, PMID:42600696), and the thrombocytopenia cases come with the mechanism measured on the cells: *"Lectin array showed decreased α-2,3-sialylation on platelets, consistent with loss of sialic acid synthesis and indicative of rapid platelet clearance"* (PMID:35052006). The variants in that patient sat *"in the nucleotide-binding site of the N-acetylmannosamin kinase domain"* — an allele-position-dependent arm selection within one gene, which the module's trigger-plus-menu structure accommodates and a per-disease chain would not.

---

## 7. Experimental Evidence Clarifying Molecular Lesion → Phenotype (Question 7)

Separated by evidence class, as required.

**Model organism.**
- *Mouse, complete null:* embryonic lethality bounds the entire module to hypomorphic alleles (PMID:11929971).
- *Mouse, cytosolic hypomorph:* the `Gne` M712T knock-in gives the podocyte arm with a named client protein, and ManNAc rescues it — *"Survivors exhibited improved renal histology, increased sialylation of podocalyxin, and increased Gne/Mnk protein expression and Gne-epimerase activities"* (PMID:17549255). Loss-and-rescue on the same arm is the strongest causal shape available.
- *Mouse, activation-step:* `Cmas-nls` reproduces the podocyte arm from a different step (PMID:22745475) — the convergence test.
- *Mouse, post-onset correction:* *"All three therapies markedly improved the muscle and renal hyposialylation, as evidenced by lectin histochemistry for overall sialylation status and immunoblotting of specific sialoproteins"* (PMID:23122659). The donor node is correctable after symptom onset, at least biochemically.
- *Mouse, cell-autonomy test:* myofiber-restricted deletion was insufficient — *"suggests induction of muscle disease requires loss of gene GNE expression in cell types beyond skeletal myofibers"* (PMID:41417753). This is an important negative and the module is right to carry it.
- *Mouse, platelet lineage:* *"an increased number of desialylated platelets was cleared by Küpffer cells in the liver"* and *"The number of bone marrow megakaryocytes in Plt Slc35a1-/- mice was reduced, and megakaryocyte maturation was also impaired"* (PMID:32303557).
- *Zebrafish:* *"Knockdown of nansa in zebrafish embryos resulted in abnormal skeletal development, and exogenously added sialic acid partially rescued the skeletal phenotype"* (PMID:27213289).

**In vitro / human cell.**
- *Cortical organoids (the most informative single experiment for the brain arm):* NANS mutation abolished sialic acid and protein polysialylation, reduced neural progenitor proliferation and expansion, *"dysregulated neural migration and differentiation, disturbed synapse formation, and weakened neuronal activity"* (PMID:38000033). Human tissue, defined lesion, graded cellular phenotypes.
- *NANP knockout cell lines:* the negative result excluding that step (PMID:31121216).
- *CMAS variant characterization:* *"Conservation analysis, structural prediction, and enzyme activity experiments demonstrated that (p.Arg188His) influences protein dimerization and alters CMAS enzyme activity"* (PMID:31495922).
- *Patient megakaryocyte culture:* normal biogenesis despite a profound sialylation defect (PMID:42600696) — see the controversy in §9.

**Human clinical / interventional.**
- *ManNAc phase 2:* *"Increased plasma Neu5Ac (+2,159 nmol/L, p < 0.0001) and sarcolemmal sialylation (p = 0.0090) were observed at day 90 compared to baseline"* (PMID:34257421). On-mechanism target engagement in patients.
- *Sialic acid in NANS-CDG:* *"In postnatally treated patients, there was no significant improvement"*, with a single prenatally treated patient faring better than two genotype-matched comparators (PMID:37340906).
- *HSCT in GNE thrombocytopenia:* *"Hematopoietic stem cell transplantation (HSCT) normalized platelet counts"* (PMID:35052006) — a lineage-replacement cure for one arm, which independently confirms the platelet arm is hematopoietic-cell-autonomous even though the muscle arm is not.

**Full-text verification required before curation.**
- **PMID:29941673** — the cached record has `content_type: unavailable` and no abstract body (publisher-free access declined). **No snippet can be taken from this reference as cached.** Either upgrade the cache with `just fetch-reference PMID:29941673 --force` and re-check, or cite PMID:35052006 / PMID:42600696 instead for the same claim. Do not write a snippet for it from the title.
- **PMID:41417753** and **PMID:42600696** are recent; the quotes used are abstract-level and verified, but any claim about their *methods* (which deletion drivers, which 3-D marrow system) needs full text.
- **PMID:11929971** and **PMID:9689047** are `abstract_only`; the quotes used are within the abstract and verified.

---

## 8. Ontology Suggestions (Question 8)

The bindings already in the module are, on inspection, well chosen. Listed here with verification status so a curator can see what still needs a lookup. **Every CURIE below must be re-resolved at the moment it is written** — I have not re-run `runoak` on them in this report, so treat the IDs as *carried from the existing module file* rather than as independently verified here.

**GO — molecular function (trigger nodes):**

| Suggested label | Carried in module as | Node |
|---|---|---|
| UDP-N-acetylglucosamine 2-epimerase activity | GO:0008761 | T1 |
| N-acylmannosamine kinase activity | GO:0009384 | T1 |
| N-acetylneuraminate synthase activity | GO:0050462 | T1 |
| N-acylneuraminate cytidylyltransferase activity | GO:0008781 | T2 |
| CMP-N-acetylneuraminate transmembrane transporter activity | GO:0005456 | T3 |

**GO — biological process:**

| Suggested label | Carried as | Node |
|---|---|---|
| N-acetylneuraminate biosynthetic process | GO:0046380 | T1 |
| CMP-N-acetylneuraminate biosynthetic process | GO:0006055 | T2 |
| CMP-N-acetylneuraminate transmembrane transport | GO:0015782 | T3 |
| CMP-N-acetylneuraminate metabolic process | GO:0046381 | **C** |
| protein sialylation | GO:1990743 | E1 |
| ganglioside biosynthetic process | GO:0001574 | E2 |
| brain development | GO:0007420 | X5 |
| growth plate cartilage development | GO:0003417 | X4 |
| podocyte development | GO:0072015 | X3 |

**GO — cellular component:** cytosol (GO:0005829, T1); nucleus (GO:0005634, T2); Golgi membrane (GO:0000139, T3); Golgi lumen (GO:0005796, **C**).

*A note on the central node's process binding.* GO has no term for "the size of a donor-substrate pool", so `CMP-N-acetylneuraminate metabolic process` with `modifier: DECREASED` is a compromise — it names the metabolism, not the pool. This is the right call under the ontology-term contract (bind the most specific accurate term; do not manufacture a narrower match), and the module's `notes` already records the reasoning. A conformer that binds no process at the central node is still conforming.

**CL — cell types:** skeletal muscle fiber (CL:0008002, X1); platelet (CL:0000233) and Kupffer cell (CL:0000091, X2); podocyte (CL:0000653, X3); neuron (CL:0000540, X5); chondrocyte (CL:0000138, X4).

*Two candidate CL additions, by label only.* The megakaryocyte should be considered on X2 if the production limb of the controversy is ever modelled — the mouse evidence is explicitly about megakaryocyte number and maturation, and the node currently has no cell type to carry that claim. And a neural progenitor / radial glia type is now justifiable on X5 by the organoid result, which measured progenitor proliferation rather than mature neuronal function. Both need an actual CL lookup before binding.

**UBERON — anatomical sites:** skeletal muscle tissue (UBERON:0001134, X1); liver (UBERON:0002107, X2); renal glomerulus (UBERON:0000074, X3); brain (UBERON:0000955, X5); epiphyseal plate (UBERON:0002516, X4).

*Candidate additions, by label only:* cerebral cortex for X5 (the organoid and mouse neurogenesis evidence is cortical specifically, and `brain` is coarse for it); bone marrow for X2 if the production limb is modelled.

**Deliberately not bound.** Sialic acid and CMP-sialic acid carry CHEBI identifiers but are described in prose throughout the nodes, because modules bind GO, CL and UBERON only. The single exception is the treatments block, where `therapeutic_agent` correctly carries CHEBI:63153 (N-acetyl-D-mannosamine) and CHEBI:17012 (N-acetylneuraminic acid) per the treatment schema. No MONDO bindings appear in nodes. This is consistent and should stay.

---

## 9. Out-of-Scope Boundary Notes (Question 9)

The module's exclusions are well drawn and each has a positive reason, not merely an absence.

**Excluded because the flux runs the other way.** *Sialuria* is a GNE disorder — same gene, same protein — in which an allosteric variant destroys CMP-sialic acid feedback inhibition, so free sialic acid is *overproduced* and accumulates. It is the mechanistic mirror image of this module and must never be a conformer. The shared gene makes this the single most likely curation error in the module's vicinity.

**Excluded because the lesion is catabolic or in efflux, not supply.** The sialidoses (NEU1), galactosialidosis (CTSA), and free sialic acid storage disease (SLC17A5 — Salla disease and the infantile form) all involve sialic acid and all cause disease, but they are lysosomal degradation or lysosomal efflux defects whose hallmark is *storage* of sialylated material or of free sialic acid. The donor pool is not the deficient quantity.

**Excluded because the module is upstream of them.** Individual sialyltransferase deficiencies (ST3GAL3, ST3GAL5) produce hyposialylation of specific clients with a normal donor supply. They belong downstream of this module's central node, not inside it — and modelling them here would destroy the module's distinguishing claim that the shortage is non-selective.

**Excluded by division of labour with a sibling module.** `congenital_disorder_of_glycosylation` models assembly and processing of the glycan itself — ER lipid-linked oligosaccharide assembly, Golgi branching, COG-complex trafficking — and has no sialic acid supply arm. This module supplies the donor-substrate limb feeding the terminal capping step of N-glycans, O-glycans and gangliosides alike. The two are complementary, not competing, and SLC35A1-CDG legitimately conforms to both.

**Not excluded, but not a conformer either.** GNE-related thrombocytopenia without myopathy is the *same* cytosolic arm presenting through a different tissue consequence. It conforms at X2, through T1. It is not a separate mechanism.

**Claims I judge speculative or weakly supported, and would keep out of the nodes:**

1. *That the quadriceps-sparing of GNE myopathy is explained by regional sialic acid demand.* The observation is real and quantified — *"Normal quadriceps had significantly lower levels of free SA (reduced by 39%) and total SA (reduced by 53%) compared to normal gastrocnemius"* (PMID:28267778) — but the inference from lower baseline demand to clinical sparing is a hypothesis, and arguably runs counter to intuition (a muscle needing less might be expected to tolerate shortage *better*, which is in fact the authors' reading, but the alternative reading is available). The module's description correctly hedges this as "a candidate explanation". Keep that hedge.
2. *That ganglioside deficiency is demonstrated in any of these disorders.* It is not. The C → E2 edge is a biochemical expectation, properly marked provisional.
3. *That supplementation cannot help CMAS or SLC35A1 lesions.* This is a mechanistic prediction from pathway topology, and the module states it as such — *"that prediction has not been tested in those disorders"*. Keep it as a prediction. The topology is sound; the clinical claim is untested.
4. *That the module's central node is therapeutically correctable in humans.* ManNAc raises plasma Neu5Ac and sarcolemmal sialylation (PMID:34257421), but extended-release aceneuramic acid failed its placebo-controlled phase 3 endpoint in GNE myopathy, and postnatal oral sialic acid showed no significant improvement in NANS-CDG (PMID:37340906). The `target_mechanisms` claims recorded in the module are donor supply, not clinical benefit, and that distinction is correctly drawn. Do not let it blur.

---

## 10. Open Questions for Curator Review

**1. Should the ganglioside arm exist as a node at all, given no direct measurement?** My recommendation is yes, keep it: the sialyltransferases building gangliosides are the same enzymes drawing on the same donor, so an entry describing only the glycoprotein arm would understate what the shortage does, and the node's provisional edge confidence already tells a reader what is and is not measured. But a curator who prefers to model only what has been assayed has a defensible position, and this should be a deliberate decision rather than inherited.

**2. Why is the kidney arm prominent in two mouse models and nearly absent in human GNE myopathy?** The module's answer — that the arm is developmentally timed, hitting the *maturing* podocyte — is consistent with the `Cmas-nls` paper's own framing (*"maturing podocyte where it is required during the formation of foot processes"*) and with proteinuria appearing in the congenital human disorder (SLC35A1-CDG) but not the adult-onset one. It is a good hypothesis and it is recorded as a discussion rather than asserted in the node. Worth a curator's eye on whether the `Podocyte Hyposialylation Injury` node should carry an explicit developmental-window qualifier in its description, so a reader does not expect proteinuria in an adult GNE myopathy entry.

**3. Should "Impaired Brain Development" be split?** The organoid and mouse neurogenesis data (PMID:38000033) describe a *prenatal neurogenesis* failure — progenitor proliferation, migration, synaptogenesis. The NANS-CDG cohort additionally reports *"(progressive) cerebral atrophy and ventricular dilatation (n = 5/9; 56%)"* and some patients suffer *"progressive intellectual neurologic deterioration (PIND)"* (PMID:37340906). Those are two different things: a developmental failure that is finished by birth, and an ongoing degenerative process. One node is currently carrying both. This also has a therapeutic edge — the prenatal-versus-postnatal supplementation signal in PMID:37340906 only makes sense if the arms are distinguishable. **This is the single structural change I would most recommend considering**, and I have not audited whether a split would break existing conformers.

**4. The platelet production-versus-clearance controversy is correctly left open.** The mouse says production is impaired (PMID:32303557); the human series says *"The profound megakaryocyte sialylation defect induced by GNE variants does not affect platelet biogenesis"* (PMID:42600696). The module records this as a `CONTROVERSY` discussion with a proposed paired-measurement experiment, and models only the clearance limb. That is the honest state. I would add one observation to the discussion's rationale: the HSCT result (PMID:35052006), where replacing the hematopoietic compartment normalized platelet counts, is compatible with either limb and so does not break the tie — but it does establish the arm as cell-autonomous to the hematopoietic lineage, which the proposed experiment could exploit.

**5. Does PMID:29941673 need to stay cited?** As cached it carries no retrievable body, so nothing can be quoted from it. Either force a re-fetch or drop it in favour of PMID:35052006 and PMID:42600696, which cover the same claim with verifiable abstracts.

---

### Evidence Table

| PMID | Type | Exact quote (verified against cache) | Claim supported |
|---|---|---|---|
| 9689047 | In vitro / foundational | "A prerequisite for the synthesis of sialylated glycoconjugates is the activated sugar-nucleotide cytidine 5'-monophosphate N-acetylneuraminic acid (CMP-Neu5Ac), which provides a substrate for Golgi sialyltransferases." | The donor is the single shared substrate — the module's organizing premise |
| 11929971 | Model organism | "inactivation of the UDP-GlcNAc 2-epimerase by gene targeting causes early embryonic lethality in mice" | Every human conformer is hypomorphic; nulls are lethal |
| 17549255 | Model organism | "Renal findings included segmental splitting of the glomerular basement membrane, effacement of podocyte foot processes, and reduced sialylation of the major podocyte sialoprotein, podocalyxin." | E1 → X3 with a named client protein |
| 17549255 | Model organism | "Survivors exhibited improved renal histology, increased sialylation of podocalyxin, and increased Gne/Mnk protein expression and Gne-epimerase activities." | ManNAc rescue reaches the tissue arm |
| 22745475 | Model organism | "a critical shortage of CMP-sialic acid prevented sialylation of nephrin and podocalyxin in the maturing podocyte" | T2 → C, naming the pool directly |
| 22745475 | Model organism | "The Cmas(nls) mouse exhibited podocyte foot process effacement, absence of slit diaphragms, and massive proteinuria" | Convergence: a second step gives the same arm |
| 23122659 | Model organism | "All three therapies markedly improved the muscle and renal hyposialylation, as evidenced by lectin histochemistry for overall sialylation status and immunoblotting of specific sialoproteins." | The central node is correctable post-onset |
| 23873973 | Human clinical | "The primary neurologic presentation consisting of ataxia, intellectual disability, and seizures, in combination with bleeding diathesis and proteinuria" | One lesion, three arms in one person |
| 23873973 | Human clinical | "Functional analysis of mutant SLC35A1 showed normal Golgi localization but 50% reduction in transport activity of CMP-sialic acid in vitro." | T3 is reduced import, not mislocalization |
| 24692354 | Review | "Gangliosides, sialylated glycosphingolipids, are the most abundant sialoglycans of nerve cells." | Why E2 is weighted to the nervous system |
| 24692354 | Review | "Polysialic acid is essential for appropriate brain development, and polymorphisms in the human genes responsible for polysialic acid biosynthesis are associated with psychiatric disorders" | Named intermediate on E1 → X5 |
| 27213289 | Human clinical | "Patient body fluids showed an elevation in N-acetyl-D-mannosamine levels, and patient-derived fibroblasts had reduced NANS activity and were unable to incorporate sialic acid precursors into sialylated glycoproteins." | T1 block at the synthase step |
| 27213289 | Model organism | "Knockdown of nansa in zebrafish embryos resulted in abnormal skeletal development, and exogenously added sialic acid partially rescued the skeletal phenotype." | E1 → X4, loss and rescue |
| 27213289 | Human clinical | "Normal sialylation of plasma proteins was observed in spite of NANS deficiency." | The diagnostic pitfall on E1 |
| 28267778 | Human clinical | "These results show that serum and muscle free SA is severely reduced in GNEM, which is consistent with the biochemical defect in SA synthesis associated with GNE mutations." | T1 output measured in patients |
| 28267778 | Human clinical | "suggesting a small subset of sialylation targets could be responsible for the pathogenesis of GNEM" | Why E1 → X1 has unknown intermediates |
| 28856833 | Human clinical | "Direct measurement of CMP-sialic acid transport into the Golgi showed a substantial decrease in overall rate of transport." | T3 → C, directly measured |
| 28856833 | Human clinical | "Patient primary fibroblasts and serum showed a considerable decrease in the amount of N- and O-glycans terminating in sialic acid." | The shortage is non-selective across glycan classes |
| 31121216 | In vitro | "In agreement with normal cell surface sialylation, CMP-sialic acid levels in NANP KO were comparable to WT cells, even though sialic acid 9-phosphate, the substrate of NANP accumulated." | **REFUTE** — NANP is not a lesion site |
| 31495922 | In vitro | "Conservation analysis, structural prediction, and enzyme activity experiments demonstrated that (p.Arg188His) influences protein dimerization and alters CMAS enzyme activity." | T2 lesion characterized |
| 32303557 | Model organism | "an increased number of desialylated platelets was cleared by Küpffer cells in the liver" | E1 → X2, the clearance event |
| 32303557 | Model organism | "The number of bone marrow megakaryocytes in Plt Slc35a1-/- mice was reduced, and megakaryocyte maturation was also impaired." | Mouse side of the production controversy |
| 34163424 | Human clinical | "elevated urinary excretion of N-acetylmannosamine (ManNAc) is pathognomonic, the concentrations of which show a significant correlation with clinical severity" | Residual flux sets severity |
| 34163424 | Human clinical | "thrombocytopenia (n = 5/9; 56%)" | X2 occurs in NANS-CDG too — broader than assumed |
| 34257421 | Human clinical | "Increased plasma Neu5Ac (+2,159 nmol/L, p < 0.0001) and sarcolemmal sialylation (p = 0.0090) were observed at day 90 compared to baseline." | ManNAc engages the central node in patients |
| 35052006 | Human clinical | "Lectin array showed decreased α-2,3-sialylation on platelets, consistent with loss of sialic acid synthesis and indicative of rapid platelet clearance." | GNE thrombocytopenia runs the X2 arm |
| 35052006 | Human clinical | "Hematopoietic stem cell transplantation (HSCT) normalized platelet counts." | X2 is hematopoietic-cell-autonomous |
| 36224347 | Human clinical | "Patient 1 exhibited a unique constellation of clinical features including marked hydrocephalus, spondyloepimetaphyseal dysplasia (SEMD), and thrombocytopenia" | Multi-arm NANS presentation, independent series |
| 37340906 | Human clinical | "In postnatally treated patients, there was no significant improvement." | Donor-supply correction ≠ clinical benefit |
| 38000033 | In vitro (human organoid) | "NANS mutation resulted in the absence of both sialic acid and protein polysialylation in the cortical organoids and notably reduced the proliferation and expansion of neural progenitors." | Strongest support for E1 → X5; names the intermediate |
| 38000033 | Model organism | "Nans heterozygous mice exhibited impaired cortical neurogenesis and neurobehavioral deficits." | X5 corroborated in vivo |
| 41417753 | Model organism | "suggests induction of muscle disease requires loss of gene GNE expression in cell types beyond skeletal myofibers" | X1 is not cell-autonomous to the myofiber |
| 42600696 | Human clinical | "In all individuals, platelet flow cytometry showed increased RCA-1 and ECL lectin binding and decreased MAL-II binding." | The platelet surface change in patients |
| 42600696 | Human clinical | "The profound megakaryocyte sialylation defect induced by GNE variants does not affect platelet biogenesis." | **REFUTE** — human side of the production controversy |
| 15576474 | Human clinical | "We conclude that this defect is a new type of congenital disorder of glycosylation (CDG) of type IIf affecting the transport of CMP-sialic acid into the Golgi apparatus." | T3 as a defining CDG; grounds dual conformance |
| 29941673 | — | **No quotable content.** Cache carries `content_type: unavailable`; publisher-free full text declined. | Re-fetch or substitute before citing |

---

**Summary of recommended changes:** keep the name and the eleven-node DAG; harden *"may conform to both modules"* to *"conforms"*; add the cortical-organoid evidence (PMID:38000033) to the brain edge in both its in-vitro and model-organism forms; consider splitting `Impaired Brain Development` into a prenatal neurogenesis arm and a progressive deterioration arm; add megakaryocyte and neural-progenitor cell types by lookup if those arms are extended; and resolve or drop PMID:29941673. Everything else in the module is supported as curated.

I audited each quote above against its cached file. The CURIEs I did not re-resolve, and say so — those are carried from the module, not verified here. That part is only an idea until a lookup confirms it.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 19 |
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
| Terms whose name was checked | 16 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.