---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-27T13:35:03.817002'
end_time: '2026-10-27T13:37:54.271423'
duration_seconds: 170.45
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: Hepcidin Deficiency Iron Overload Module
  module_slug: hepcidin_deficiency_iron_overload
  category: Module
  module_description: The conserved systemic iron-overload pathway shared by hereditary
    hemochromatosis and the iron-loading anemias. Loss of hepatocyte iron sensing
    through the HFE/TFR2/HJV/BMP6 bone morphogenetic protein-SMAD pathway, or erythroid
    suppression of hepcidin by erythroferrone during ineffective erythropoiesis, leaves
    hepcidin inappropriately low for body iron stores; with too little hepcidin to
    internalize and degrade it (or with a hepcidin-resistant ferroportin), ferroportin
    exports iron unrestrained from duodenal enterocytes and macrophages; transferrin
    becomes saturated and non-transferrin-bound iron appears in plasma; parenchymal
    cells take it up and accumulate iron, causing oxidative injury, fibrosis and organ
    failure.
  pathophysiology_summary: '- Hepatocyte Iron-Sensing BMP-SMAD Signaling Loss: Loss
    of HFE, TFR2, hemojuvelin or BMP6 blunts hepatocyte BMP-SMAD signaling that induces
    hepcidin transcription.

    - Erythroferrone-Mediated Hepcidin Suppression: Expanded ineffective erythropoiesis
    releases erythroferrone, which sequesters BMPs and suppresses hepcidin.

    - Hepcidin Deficiency: Hepcidin is inappropriately low relative to body iron stores.

    - Hepcidin-Resistant Ferroportin: SLC40A1 gain-of-function variants block hepcidin
    binding or ferroportin internalization.

    - Unrestrained Ferroportin Iron Export: Ferroportin remains on enterocytes and
    macrophages and exports iron into plasma unchecked.

    - Transferrin Saturation and Non-Transferrin-Bound Iron: Plasma iron exceeds transferrin
    binding capacity and non-transferrin-bound iron appears.

    - Parenchymal Iron Deposition and Oxidative Injury: Hepatocytes, cardiomyocytes
    and endocrine cells take up non-transferrin-bound iron, generating reactive oxygen
    species, ferroptosis, fibrosis and organ failure.'
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
  - claude-sonnet-5-5
  web_search_requests: 2
  num_turns: 34
  total_cost_usd: 1.4270199000000001
  session_id: 365353bd-1c8b-55dd-9afa-fdb9e1b5ccf0
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 8
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 0
  off_topic: 1
  off_topic_references:
  - PMID:20301523
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 17
  verified: 17
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
- **Module Name:** Hepcidin Deficiency Iron Overload Module
- **Module Slug:** hepcidin_deficiency_iron_overload
- **Category:** Module

## Current Module Description

The conserved systemic iron-overload pathway shared by hereditary hemochromatosis and the iron-loading anemias. Loss of hepatocyte iron sensing through the HFE/TFR2/HJV/BMP6 bone morphogenetic protein-SMAD pathway, or erythroid suppression of hepcidin by erythroferrone during ineffective erythropoiesis, leaves hepcidin inappropriately low for body iron stores; with too little hepcidin to internalize and degrade it (or with a hepcidin-resistant ferroportin), ferroportin exports iron unrestrained from duodenal enterocytes and macrophages; transferrin becomes saturated and non-transferrin-bound iron appears in plasma; parenchymal cells take it up and accumulate iron, causing oxidative injury, fibrosis and organ failure.

## Current Provisional Nodes

- Hepatocyte Iron-Sensing BMP-SMAD Signaling Loss: Loss of HFE, TFR2, hemojuvelin or BMP6 blunts hepatocyte BMP-SMAD signaling that induces hepcidin transcription.
- Erythroferrone-Mediated Hepcidin Suppression: Expanded ineffective erythropoiesis releases erythroferrone, which sequesters BMPs and suppresses hepcidin.
- Hepcidin Deficiency: Hepcidin is inappropriately low relative to body iron stores.
- Hepcidin-Resistant Ferroportin: SLC40A1 gain-of-function variants block hepcidin binding or ferroportin internalization.
- Unrestrained Ferroportin Iron Export: Ferroportin remains on enterocytes and macrophages and exports iron into plasma unchecked.
- Transferrin Saturation and Non-Transferrin-Bound Iron: Plasma iron exceeds transferrin binding capacity and non-transferrin-bound iron appears.
- Parenchymal Iron Deposition and Oxidative Injury: Hepatocytes, cardiomyocytes and endocrine cells take up non-transferrin-bound iron, generating reactive oxygen species, ferroptosis, fibrosis and organ failure.

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

Checking whether PubMed's API is reachable, so I can pull exact abstract quotes for the evidence table.

Direct shell access to PubMed needs approval, so I'll use the web fetch tool instead.

WebFetch only summarizes abstracts, so I can't get verbatim quotes that way. I'll use the repo's own reference fetcher, which caches the abstract text locally.

The cache gives verbatim abstract text, so I'll search it for other hepcidin and iron-overload papers I can quote.

Now pulling the abstracts for the most relevant cached papers.

Before drafting, I'll check what the existing Hemochromatosis and Beta_Thalassemia entries already cite for the ferroportin and NTBI branches, since those aren't in the cache by title.

Last lookup: the ontology terms already bound in the Hemochromatosis entry, so the suggestions in the report come from the repo's validated caches and not from memory.

# Hepcidin Deficiency Iron Overload Module: Mechanism Research Report

**Target:** `kb/modules/hepcidin_deficiency_iron_overload.yaml` (module slug `hepcidin_deficiency_iron_overload`)
**Date:** 2026-10-27

## Method and verification status

PubMed's API is blocked in this sandbox, and the fetch tool only returns paraphrased summaries. Every quote marked **[VERIFIED]** therefore comes from an abstract or full text already in `references_cache/`, or from a snippet already in `kb/disorders/Hemochromatosis.yaml` or `Beta_Thalassemia.yaml`. Those snippets were checked by the repo's own validators when they were merged. I did not re-run `just count-verified-snippets`.

Anything marked **[LEAD]** is recalled or secondhand. It has no quote and is not citable until `just fetch-reference` caches it and the quote is copied from the cache. I did not write any ontology ID from memory. Every GO, CL and CHEBI ID below is read from bindings already in `Hemochromatosis.yaml`. Anything else is given by label only.

---

## 1. Executive recommendation

**Keep the name** "Hepcidin Deficiency Iron Overload Module", and keep the scope as systemic iron overload caused by too little hepcidin activity for body iron. The scope is well supported. The Hemochromatosis entry already conforms to it, and `Beta_Thalassemia` carries the same hepcidin-suppression logic (see Section 7).

The module needs three refinements.

1. **Make the module explicitly branched.** There are three ways in to the hub node (Hepcidin Deficiency), and they are not interchangeable.
   - **Branch A, BMP-SMAD sensing loss.** This is HFE, TFR2, HJV, HAMP and BMP6 disease. Hepcidin falls because hepatocyte iron sensing fails.
   - **Branch B, erythroid suppression.** Here hepcidin is suppressed by erythroferrone (ERFE) during ineffective erythropoiesis.
   - **Branch C, hepcidin resistance.** Hepcidin is normal or high, but SLC40A1 gain-of-function variants make ferroportin unable to respond. This branch does not go through "Hepcidin Deficiency".
2. **Do not call "Hepcidin Deficiency" a universal required node.** For branch C it is false. The universal requirement is "hepcidin–ferroportin axis activity is insufficient to restrain ferroportin". Two ways to express this are listed in Section 2.
3. **Say in the description that the module covers iron hyperabsorption and release, not transfusional iron.** Transfusional siderosis feeds the same downstream nodes (NTBI and parenchymal loading) but bypasses the hepcidin and ferroportin nodes.

The "Left deliberately uncited" and "Deliberately lumped" conventions in CLAUDE.md apply to any node that ends up thin on direct evidence.

---

## 2. Proposed DAG: nodes and causal edges

### Core (required for conformance)

| # | Node | Status |
|---|---|---|
| C1 | **Insufficient hepcidin–ferroportin restraint** (hub; a conforming entry satisfies it via the hepcidin-low or the ferroportin-resistant path) | Required |
| C2 | Unrestrained Ferroportin Iron Export | Required |
| C3 | Transferrin Saturation and Non-Transferrin-Bound Iron | Required |
| C4 | Parenchymal Iron Deposition and Oxidative Injury | Required |

### Branch nodes (at least one of A, B or C required)

| Branch | Node | Notes |
|---|---|---|
| A | Hepatocyte Iron-Sensing BMP-SMAD Signaling Loss | Gene-specific: HFE, TFR2, HJV, BMP6 |
| A/B | Hepcidin Deficiency | The shared hub for A and B only |
| B | Erythroferrone-Mediated Hepcidin Suppression | Needs ineffective erythropoiesis |
| C | Hepcidin-Resistant Ferroportin | SLC40A1 gain-of-function only |

### Edges

```
A: BMP-SMAD Signaling Loss ──► Hepcidin Deficiency
B: ERFE Hepcidin Suppression ──► Hepcidin Deficiency
Hepcidin Deficiency ──► Unrestrained Ferroportin Iron Export
C: Hepcidin-Resistant Ferroportin ──► Unrestrained Ferroportin Iron Export   (bypasses Hepcidin Deficiency)
Unrestrained Ferroportin Iron Export ──► Transferrin Saturation and NTBI
Transferrin Saturation and NTBI ──► Parenchymal Iron Deposition and Oxidative Injury
```

I recommend `hypothesis_groups` or similar so that C is not asserted to pass through the hepcidin node. Per the pathograph rules, all `downstream` targets are bare node names.

### Two design options for the hub

| Option | Description | Trade-off |
|---|---|---|
| (i) Keep "Hepcidin Deficiency" as the hub and make it **optional**. | Fewer renames. | Conformers on branch C skip it, so the hub is not in every conformer's chain. |
| (ii) Add a neutral parent node ("Insufficient Hepcidin–Ferroportin Restraint") that both Hepcidin Deficiency and Hepcidin-Resistant Ferroportin point to. | Every conformer passes through one node. | One extra node. |

I recommend option (ii).

---

## 3. Evidence

### 3.1 Key mechanistic claims

| PMID | Evidence type | Verbatim quote | Supports | Status |
|---|---|---|---|---|
| 15514116 (Nemeth 2004, *Science*) | In vitro | "Here we report that hepcidin bound to ferroportin in tissue culture cells. After binding, ferroportin was internalized and degraded, leading to decreased export of cellular iron." | Hepcidin–ferroportin mechanism (C1 to C2) | [VERIFIED] |
| 15514116 | In vitro (same abstract) | "Decreased hepcidin leads to tissue iron overload, whereas hepcidin overproduction leads to hypoferremia and the anemia of inflammation." | Hepcidin deficiency causes iron overload | [VERIFIED] |
| 16604073 (Babitt 2006, *Nat Genet*) | In vitro + mouse hepatocytes | "Here, we report that hemojuvelin is a BMP coreceptor and that hemojuvelin mutants associated with hemochromatosis have impaired BMP signaling ability." | Branch A: HJV is part of BMP signaling | [VERIFIED] |
| 16604073 | Same abstract | "Our data suggest a mechanism by which HFE2 mutations cause hemochromatosis: hemojuvelin dysfunction decreases BMP signaling, thereby lowering hepcidin expression." | A to Hepcidin Deficiency | [VERIFIED] |
| 26582087 (Daher 2016, *Gastroenterology*) | Human clinical + in vitro | "Serum levels of hepcidin were inappropriately low in patients." | Branch A: BMP6 variants and inappropriate hepcidin | [VERIFIED] |
| 26582087 | Same abstract | "In cell lines, the mutated residues in the BMP6 propeptide resulted in defective secretion of BMP6; reduced signaling via SMAD1, SMAD5, and SMAD8; and loss of hepcidin production." | BMP6 loss to SMAD loss to hepcidin | [VERIFIED] |
| 24880340 (Kautz 2014, *Nat Genet*) | Mouse | "ERFE expression is greatly increased in Hbb(th3/+) mice with thalassemia intermedia, where it contributes to the suppression of hepcidin and the systemic iron overload characteristic of this disease." | Branch B | [VERIFIED] |
| 24880340 | Mouse | "ERFE is produced by erythroblasts in response to erythropoietin." | ERFE source and trigger | [VERIFIED] |
| 24880340 | Mouse | "Ablation of ERFE in β-thalassemic mice (Fam132b−/−HbbTh3/+) raised hepcidin levels (Fig. 7D) and decreased hepatic iron overload compared to HbbTh3/+ mice (Fig. 7E)." | Causal edge B to Hepcidin Deficiency to overload (full text, not the abstract) | [VERIFIED] |
| 31949017 (Camaschella 2020 review) | Review | "Mutations of hemochro-matosis genes result in iron excess by downregulating the liver BMP-SMAD signaling pathway or by causing hepcidin-resistance. In iron-loading anemias, such as β-thalassemia, enhanced albeit ineffective ery-thropoiesis releases erythroferrone, which sequesters BMP receptor ligands, thereby inhibiting hepcidin." | All three branches in one statement | [VERIFIED]. The hyphenation is as cached. Normalise before use. |
| 41882292 (cited in `Hemochromatosis.yaml`) | Review | "In gain-of-function SLC40A1 mutations, ferroportin is resistant to hepcidin activity. This leads to unregulated iron export from enterocytes and macrophages and thus, systemic iron overload." | Branch C | [VERIFIED] (curated snippet) |
| 41882292 | Review | "Gain-of-function variants in the SLC40A1 gene affect the hepcidin binding site on ferroportin." | Branch C | [VERIFIED] (curated snippet) |
| 39644049 (cited in `Hemochromatosis.yaml`) | Review | "This results in the formation of toxic non-transferrin-bound iron, which ultimately accumulates in multiple organs, including the liver, heart, endocrine glands, and joints." | C3 to C4 | [VERIFIED] (curated snippet) |
| 40650208 | Review | "This unregulated uptake can lead to iron accumulation in vulnerable tissues such as the liver and the heart." | NTBI enters via routes not regulated by transferrin receptor or cellular iron | [VERIFIED] |
| 40650208 | Review | "Both NTBI and LPI contribute to oxidative stress by participating in free-radical-generating reactions." | NTBI to oxidative injury | [VERIFIED] |
| 21705976 (cited in `Beta_Thalassemia.yaml`) | Review | "erythropoiesis,anemia and hypoxia down-regulate hepcidin, the master regulator of iron homeostasis. Hepcidin deficiency in turn allows excessive duodenal iron absorption and development of systemic iron overload." | Branch B in human disease | [VERIFIED] (curated snippet) |
| 29620054 (cited in `Hemochromatosis.yaml`) | Review | "Mutations in SLC40A1 (also known as FPN1; encoding ferroportin) that prevent hepcidin-ferroportin binding also cause haemochromatosis." | Branch C | [VERIFIED] (curated snippet) |

### 3.2 Evidence that bears on scope boundaries

| PMID | Type | Quote | Relevance |
|---|---|---|---|
| 24860871 (Fertrin 2014, *Am J Hematol*) | Human clinical | "Neither overall increased EPO,nor variable GDF-15 concentrations correlated with circulating hepcidin concentrations (P = 0.265 and P = 0.872)." | GDF15 should not be a core branch B node. |
| 24860871 | Human clinical | "Relative hepcidin deficiency was found in disorders presenting with concurrent elevation of GDF-15 and soluble transferrin receptor (sTfR), a biomarker of erythropoiesis, and sTfR had the strongest correlation with hepcidin (r(s) = 0.584, P < 0.0001)." | Erythropoietic drive, not GDF15 level, tracks hepcidin in humans. |
| 24880340 | Mouse | "Together, these data suggest that hepcidin suppression by increased erythropoietic activity occurs independently of the canonical BMP/Smad signaling pathway." (Full text; ERFE may act without changing the BMP/Smad pathway.) | Branch B may not converge on the same upstream node as branch A. |
| 24880340 | Mouse | "However, the evidence for the pathogenic role of these mediators in iron-loading anemias is not definitive and recent studies argue against their contribution in physiological hepcidin suppression after hemorrhage" (GDF15 and TWSG1.) | Same point. |

### 3.3 Evidence still needed [LEAD]

- **ERFE in humans.** The ERFE evidence cached here is mouse only. The Kautz full text itself says "Studies of human patients will be necessary to establish whether ERFE plays a role in hepcidin suppression and iron overload in anemias with ineffective erythropoiesis." I recall human ERFE measurement studies in thalassemia but could not verify any PMID.
- **Ferroportin disease versus gain-of-function.** Web search returned a review of 359 patients with 60 variants, and a 2024 study reporting variants with partial loss and partial hepcidin resistance. Neither is cached, so there are no PMIDs or quotes. Fetch them before fixing the C versus ferroportin-disease boundary.
- **Ferroptosis.** I found no cached primary paper tying ferroptosis to hepcidin-deficiency iron overload. The node text names it. Treat it as **speculative** until a source is cached.
- **TFR2 and HFE mechanism papers.** The GeneReviews chapters PMID:20301523 (TFR2) and PMID:20301613 (HFE) are cached. I did not read their text. They are baseline, not mechanism, sources.

---

## 4. Gene-to-node mapping

| Gene | Node | Role | Core or optional | Evidence |
|---|---|---|---|---|
| HFE | BMP-SMAD Signaling Loss (A) | Iron-sensing upstream of BMP6/SMAD | Branch A | GeneReviews 20301613; mechanism paper needed [LEAD] |
| TFR2 | BMP-SMAD Signaling Loss (A) | Iron sensing | Branch A | GeneReviews 20301523; mechanism paper needed [LEAD] |
| HJV | BMP-SMAD Signaling Loss (A) | BMP coreceptor | Branch A | 16604073 [VERIFIED] |
| BMP6 | BMP-SMAD Signaling Loss (A) | BMP ligand | Branch A | 26582087 [VERIFIED] |
| HAMP | Hepcidin Deficiency | Hepcidin itself (loss of the hormone) | Branch A/B hub | GeneReviews 20301349 (not read) |
| TMPRSS6 | Cleaves HJV and inhibits hepcidin | Negative regulator; its loss causes iron-deficiency, so it is an opposing-direction gene, not a conformer | Out of scope (boundary) | 18976966 [VERIFIED]: matriptase-2 "cleaves hemojuvelin (HJV), a regulator of hepcidin, on plasma membrane" |
| ERFE (FAM132B) | ERFE-Mediated Hepcidin Suppression (B) | Hormone from erythroblasts | Branch B | 24880340 [VERIFIED], mouse |
| SLC40A1 | Hepcidin-Resistant Ferroportin (C) and Unrestrained Export | Gain-of-function only | Branch C | 41882292, 29620054 [VERIFIED] |
| HBB (beta-thalassemia) and other ineffective-erythropoiesis genes | Upstream driver of B | Not module nodes; the conforming disease carries them | Branch B driver | 21705976 [VERIFIED] |

---

## 5. Ontology suggestions

GO, CL and CHEBI IDs below are copied from existing, validated bindings in `kb/disorders/Hemochromatosis.yaml`. Use `just validate-terms` before reuse. UBERON IDs are not in that file, so I give labels only.

### GO biological process

| Suggested use | Label | ID |
|---|---|---|
| Hepcidin–ferroportin hub, broad | regulation of iron ion transport | GO:0034756 |
| Hepcidin inhibits export | negative regulation of iron ion transport | GO:0034757 |
| Unrestrained export (C2) | iron ion export across plasma membrane | GO:1903988 |
| Unrestrained export, positive direction | positive regulation of iron ion transport | GO:0034758 |
| Plasma iron expansion (C3) | iron ion transport | GO:0006826 |
| Parenchymal loading (C4) | intracellular iron ion homeostasis | GO:0006879 |
| Parenchymal injury (C4) | cellular response to oxidative stress | GO:0034599 |
| Parenchymal injury, cell death | intrinsic apoptotic signaling pathway in response to oxidative stress | GO:0008631 |
| Fibrosis (C4) | extracellular matrix organization | GO:0030198 |
| Iron exposure | response to iron ion | GO:0010039 |

Not in the repo: a GO term for BMP-SMAD signaling and one for ferroptosis. Search by label ("BMP signaling pathway", "cell surface receptor signaling pathway involving SMAD", "ferroptosis"). Do not bind from memory. The modifier convention is `modifier: DECREASED` for branch A BMP signaling.

### Cell Ontology

| Cell | Label | ID | Node |
|---|---|---|---|
| Hepatocyte | hepatocyte | CL:0000182 | A, C4 |
| Enterocyte | enterocyte | CL:0000584 | C2 |
| Macrophage | macrophage | CL:0000235 | C2 |
| Cardiomyocyte | cardiac muscle cell | CL:0000746 | C4 |
| Pancreatic beta cell | type B pancreatic cell | CL:0000169 | C4 |
| Endocrine cell | endocrine cell | CL:0000163 | C4 |

Branch B needs an erythroid precursor term (erythroblast). It is not bound in this repo, so look it up. The Kautz data point to basophilic and polychromatic erythroblasts, so a stage-specific term may be supportable but should not be asserted from a mouse finding.

### UBERON (labels only; look up IDs)

- liver
- duodenum, for enterocyte iron absorption
- spleen, for macrophage iron and ERFE induction in mice (24880340)
- bone marrow, for erythroblast ERFE production
- heart
- pancreas
- pituitary gland
- joint

### CHEBI

- iron atom, CHEBI:18248. Already bound in the repo.

---

## 6. Core versus optional, and boundary notes

### Core
C1 to C4. Branches A, B and C are alternatives, and at least one must be present.

### Optional or gene-specific
- BMP-SMAD Signaling Loss (HFE, TFR2, HJV, BMP6).
- ERFE suppression, which needs an erythropoietic-expansion driver.
- Hepcidin-resistant ferroportin.

### Out of scope or weakly supported
- **Ferroportin disease (SLC40A1 loss of function).** Per `Hemochromatosis.yaml` it gives macrophage iron retention with normal to low transferrin saturation. It does not follow the hepcidin-deficiency pathway and should not conform. Note that the 2024 literature suggests a mixed class exists, so decide per variant.
- **Transfusional iron overload.** It skips the first three steps.
- **TMPRSS6-related iron-refractory iron deficiency.** The hepcidin axis runs in the opposite direction.
- **FTH1 iron-responsive-element variants.** The Hemochromatosis entry treats these as a different route (11389486 is cached).
- **Iron-handling disorders that are not hepcidin-mediated.** Examples are aceruloplasminemia, DMT1 microcytic anemia with iron overload, and hypotransferrinemia. Some of these also reduce hepcidin through secondary routes (cached papers 20956801 and 17768112 on transferrin and hepcidin). They are mechanistically different, and conformance would be speculative.
- **Hypoxia-driven hepcidin suppression.** The VHL R200W (Chuvash) study (21876117) found lower hepcidin in homozygotes "independent of increased erythropoietin levels and increased RBC counts". It may be a fourth, HIF-mediated way into the hub, but it does not cause iron overload as far as the abstract shows. Leave it out.
- **GDF15 and TWSG1 as core branch B nodes.** The Section 3.2 evidence argues against it.
- **Ferroptosis** as a named mechanism. Keep it in `description` text only until a source is cached.

---

## 7. Open questions for curator review

1. **Hub design:** option (i) or (ii) in Section 2? I recommend (ii).
2. **Are branches A and B really independent?** The Kautz paper says ERFE suppression of hepcidin may not use canonical BMP/Smad signaling. The Camaschella review says ERFE "sequesters BMP receptor ligands." These conflict. Do not draw B as a child of A. Check a more recent ERFE mechanism paper [LEAD].
3. **Should HAMP loss be its own node?** It is both a gene (loss of the hormone) and the hub.
4. **Is ERFE a core node in human disease?** The only cached ERFE evidence is from mouse. A human paper would let you raise the evidence level.
5. **What replaces "ferroptosis"?** Without a cached source, decide whether to drop the word from node 7 or add an explicit `Left deliberately uncited` waiver.
6. **Does `Beta_Thalassemia` conform?** It has the hepcidin-suppression logic in its description and pathophysiology (lines 168, 268, 297), but I did not check whether it carries `conforms_to`. Dependency to resolve before registering branch B as a worked conformer.
7. **Conformance wording for branch C.** Should the module require "Hepcidin Deficiency" for all conformers? If so, it excludes SLC40A1 gain-of-function disease, which the Hemochromatosis entry already treats as an in-scope subtype.
8. **Is the TFR2 or HFE mechanism paper missing?** HFE and TFR2 rows cite only GeneReviews as cached. Run `just fetch-reference` for a primary study of each before curating edges.

---

## Sources

All evidence above comes from the local reference cache under `/home/user/dismech/references_cache/` (PMID_15514116, PMID_16604073, PMID_24880340, PMID_26582087, PMID_31949017, PMID_24860871, PMID_40650208, PMID_18976966, PMID_21876117) and from snippets already present in `kb/disorders/Hemochromatosis.yaml` and `kb/disorders/Beta_Thalassemia.yaml`. Secondary web search results on SLC40A1 variant classes were used only to flag leads. No external page was relied on for any quote.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 0 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:20301523` (1 mention) - TFR2-Related Hemochromatosis.
  - shared terms: iron

Weighed against this report's own most characteristic terms: `hepcidin`, `branch`, `node`, `iron`, `ferroportin`, `deficiency`, `erfe`, `suppression`, `loss`, `hub`, `signaling`, `slc40a1`, `core`, `lead`, `mechanism`, `mouse`, `quote`, `bmp-smad`, `disease`, `hfe`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.