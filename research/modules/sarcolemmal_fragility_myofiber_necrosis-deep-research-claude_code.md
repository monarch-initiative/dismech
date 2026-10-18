---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T03:58:15.916804'
end_time: '2026-10-15T04:01:06.285593'
duration_seconds: 170.37
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: Sarcolemmal Fragility and Myofiber Necrosis Module
  module_slug: sarcolemmal_fragility_myofiber_necrosis
  category: Module
  module_description: Loss of the dystrophin-glycoprotein complex mechanical link
    between the myofiber cytoskeleton and the basement membrane makes the sarcolemma
    fragile; contraction-induced membrane tears admit extracellular calcium, calcium
    overload activates calpains and mitochondrial permeability transition, and the
    myofiber undergoes necrosis followed by inflammation, failed regeneration, and
    fibro-adipose replacement.
  pathophysiology_summary: '- Dystrophin-Glycoprotein Complex Link Disruption: Loss
    of dystrophin, sarcoglycans, dystroglycan glycosylation or laminin-211 breaks
    the cytoskeleton to extracellular matrix link.

    - Contraction-Induced Sarcolemmal Tears: Eccentric contraction tears the unsupported
    sarcolemma.

    - Myofiber Calcium Overload: Calcium enters through membrane lesions and stretch-activated
    channels.

    - Myofiber Necrosis: Calpain activation and mitochondrial permeability transition
    kill the fiber.

    - Fibro-adipose Replacement of Muscle: Repeated degeneration exhausts regeneration
    and fibrosis and fat replace muscle.'
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
  web_search_requests: 5
  num_turns: 35
  total_cost_usd: 1.5224894000000002
  session_id: 6f407ab6-10d8-510b-8a76-b165dbc02479
  stop_reason: end_turn
  permission_denials: 9
  denied_tools:
  - Bash
  assistant_text_blocks: 5
citation_count: 5
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 30
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Sarcolemmal Fragility and Myofiber Necrosis Module
- **Module Slug:** sarcolemmal_fragility_myofiber_necrosis
- **Category:** Module

## Current Module Description

Loss of the dystrophin-glycoprotein complex mechanical link between the myofiber cytoskeleton and the basement membrane makes the sarcolemma fragile; contraction-induced membrane tears admit extracellular calcium, calcium overload activates calpains and mitochondrial permeability transition, and the myofiber undergoes necrosis followed by inflammation, failed regeneration, and fibro-adipose replacement.

## Current Provisional Nodes

- Dystrophin-Glycoprotein Complex Link Disruption: Loss of dystrophin, sarcoglycans, dystroglycan glycosylation or laminin-211 breaks the cytoskeleton to extracellular matrix link.
- Contraction-Induced Sarcolemmal Tears: Eccentric contraction tears the unsupported sarcolemma.
- Myofiber Calcium Overload: Calcium enters through membrane lesions and stretch-activated channels.
- Myofiber Necrosis: Calpain activation and mitochondrial permeability transition kill the fiber.
- Fibro-adipose Replacement of Muscle: Repeated degeneration exhausts regeneration and fibrosis and fat replace muscle.

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

I'll start by checking what the repo already has on this topic and loading the search tools.

I'm pulling candidate papers from the repo's local reference cache, so the quotes I use can be checked against real abstracts.

Fetching more abstracts through the repo's own reference tool, since the web fetcher won't return verbatim quotes.

Loops with variables get blocked, so I'll list the files explicitly.

# Research Report: Sarcolemmal Fragility and Myofiber Necrosis Module (`sarcolemmal_fragility_myofiber_necrosis`)

**Date:** 2026-10-15. **Target:** `kb/modules/sarcolemmal_fragility_myofiber_necrosis.yaml`.

**Evidence status.** I could not run `just fetch-reference` or call PubMed directly in this session. Both calls needed approval, which a non-interactive run can't give. The web fetcher also would not return verbatim abstracts.

- Every quoted snippet below was copied from a file already in `references_cache/`. Those are marked **[cached]**.
- Landmark papers not yet in the cache are marked **[NOT CACHED]**. They carry a PMID (or none) and a paraphrase only, with no quote. Run `just fetch-reference PMID:<id>` and pick a snippet before using them.
- Ontology IDs are not suggested. Labels only, to be resolved with `runoak` or the term caches.
- Gene-to-node assignments without a retrieved PMID come from background knowledge. They are marked *(background)*.

---

## 1. Executive recommendation

**Keep the name and slug.** The literature does support a scope change, though. The current description reads as one linear chain starting with DGC loss. The evidence supports a **convergent** structure:

- **Two upstream routes:** the mechanical-link route and the membrane-repair route.
- **A calcium hub:** calcium overload is the best-supported common effector.
- **Mitochondrial-dependent necrosis:** this is the best-supported route from calcium to fiber death.
- **Downstream:** inflammation, failed regeneration, and fibro-adipose replacement.

**Rewrite the description to say three things.**

1. The *tear* node is not obligatory. Calcium entry is sufficient to cause dystrophy without membrane fragility (Millay 2009), and stretch-activated and store-operated channels contribute (Burr 2015, García-Castañeda 2022). Tears are one source of the calcium load, not the only one.
2. The module has a repair-failure arm. In DYSF and ANO5 disease the DGC is intact but resealing of tears fails (Bansal 2003, Bolduc 2010).
3. The "mechanical" arm is solid for dystrophin, sarcoglycan, and dystroglycan. For laminin-α2 (LAMA2) it is **contested**. Papers report "the lack of documented membrane rupture in the laminin α2-chain deficient models" (PMID:26536238).

**Recommended core (required to conform):** Myofiber Calcium Overload → Myofiber Necrosis → Fibro-adipose Replacement of Muscle.

**Optional or gene-specific:**
- DGC link disruption
- Contraction-induced tears
- Failed membrane repair (new node)
- Inflammation and regeneration failure (new nodes)

---

## 2. Proposed DAG

| # | Node | Status | Scale |
|---|---|---|---|
| 1a | Dystrophin-Glycoprotein Complex Link Disruption (existing) | Optional, route A | MOLECULAR |
| 1b | **Sarcolemmal Repair Machinery Failure** (new) | Optional, route B | MOLECULAR |
| 2 | Contraction-Induced Sarcolemmal Tears (existing) | Optional | CELLULAR |
| 3 | Myofiber Calcium Overload (existing) | **Core** | CELLULAR |
| 4 | Myofiber Necrosis (existing) | **Core** | CELLULAR |
| 5 | **Inflammation and Regeneration Failure** (new) | Recommended | TISSUE |
| 6 | Fibro-adipose Replacement of Muscle (existing) | **Core** | TISSUE |

**Edges**
- 1a → 2: mechanical fragility. Supported for dystrophin, sarcoglycan, and α-dystroglycan hypoglycosylation.
- 1b → 2: tears that fail to reseal persist. Supported for DYSF and ANO5, with MICU1 contributing.
- 2 → 3: membrane lesions admit calcium.
- 1a → 3: direct, channel-mediated calcium entry that bypasses tears (TRPC, Orai1/SOCE, stretch-activated channels). This is the edge that makes node 2 optional.
- 3 → 4: mitochondrial permeability transition (cyclophilin D–dependent) and calpain. Strongest for the PTP; the calpain arm is weaker (§5).
- 4 → 5 → 6: necrosis, inflammation, exhausted regeneration, then fibrosis and fat.
- 6 → 2/3 feedback (fibrotic muscle is more vulnerable) is speculative; leave it out.

The node 3 → 4 edge also has non-DGC conformers. Collagen VI myopathy (extracellular matrix) shows cyclophilin D–dependent degeneration, so the module can convey conformance at node 4 without node 1a.

---

## 3. Gene-to-node mapping

| Gene(s) | Disease class | Node | Basis |
|---|---|---|---|
| DMD | Dystrophinopathy | 1a | PMID:15117830 [cached], PMID:8475120 [NOT CACHED] |
| SGCA, SGCB, SGCG, SGCD | Sarcoglycanopathy (LGMDR3–6) | 1a | PMID:34404573, PMID:26709803 [cached] |
| DAG1 (T192M) | LGMD with dystroglycan receptor defect | 1a | PMID:21388311 [cached] |
| POMGNT1, FKTN (and related glycosyltransferases) | α-Dystroglycanopathy | 1a | PMID:12140558 [cached]; ISPD/FKRP PMID:27194101 [cached]; DOLK, DPM2, DPM3 [cached] |
| LAMA2 | MDC1A | 1a (contested) | PMID:17389231, PMID:31308722 [cached]; caveat PMID:26536238 |
| DYSF | Dysferlinopathy (LGMDR2, Miyoshi) | 1b | PMID:12736685 [NOT CACHED]; PMID:20301480 [cached] |
| ANO5 | LGMDR12, MMD3 | 1b | PMID:20096397, PMID:36292621 [cached] |
| MICU1 | MICU1 myopathy | 1b / 3 | PMID:31665639 [cached] |
| TRPC3/6, ORAI1/STIM1 | Calcium-entry modifiers (not primary causes) | 3 | PMID:19864620, PMID:35939054 [cached] |
| PPIF (cyclophilin D) | Modifier, not a cause | 4 | PMID:18345011 [NOT CACHED]; PMID:19293339 [cached] |
| COL6A1–3 | Ullrich / Bethlem | 4 (PTP) | PMID:19293339, PMID:21037586 [cached] |
| CAPN3 | Calpainopathy (LGMDR1) | **Out of core** (§7) | PMID:19793101, PMID:20301490 [cached] |
| CAV3, CAVIN1 (PTRF) | Caveolinopathy | 1b / DGC-adjacent *(background)* | PMID:19726876 [cached], mechanism not verified |

---

## 4. Evidence table

**Human clinical**

| PMID | Exact quote | Claim |
|---|---|---|
| 34404573 [cached] | "Their four coded proteins, α-SG, ß-SG, λ-SG and δ-SG are part of the dystrophin-glycoprotein complex (DGC) present in muscle sarcolemma, which acts as a linker between the cytoskeleton of the muscle fiber and the extracellular matrix, providing mechanical support to the sarcolemma during myofiber contraction." | Node 1a: DGC as mechanical link (review). |
| 12140558 [cached] | "similar hypoglycosylation in the diseases directly abolishes binding activity of dystroglycan for the ligands laminin, neurexin and agrin" | Node 1a: glycosylation defects break the ECM link in patients. |
| 21388311 [cached] | "the mutation impairs the receptor function of dystroglycan in skeletal muscle and brain by inhibiting the post-translational modification, mediated by the glycosyltransferase LARGE, of the phosphorylated O-mannosyl glycans on α-dystroglycan that is required for high-affinity binding to laminin" | Node 1a: a DAG1 variant causes LGMD via loss of laminin binding. |
| 20096397 [cached] | "With the use of electron microscopy, multifocal sarcolemmal lesions were observed in both phenotypes." | Node 1b → 2: direct human sarcolemmal lesions in ANO5 disease. |
| 20096397 [cached] | "In one MMD3-affected individual, defective membrane repair was documented on fibroblasts by membrane-resealing ability assays, as observed in dysferlinopathies." | Node 1b: repair defect in a human patient. |
| 36292621 [cached] | "ANO5 functions predominantly in phospholipid scrambling (PLS)" | Node 1b: mechanism (review). Caveat: the review says chloride-channel activity looked normal in ANO5-deficient mice. |
| 31665639 [cached] | "MICU1 deficit compromises mitochondrial Ca2+ uptake during sarcolemmal injury, which causes ineffective repair of the damaged myofibers." | Node 1b/3: patient cells plus knockout mice. |
| 23620650 [cached] | "Originating from vulnerable myofibres, muscle cell necrosis and inflammatory processes are present in DMD." | Nodes 4 → 5. |
| 23620650 [cached] | "Muscular recovery is limited due to the limited number and capacity of satellite cells." | Node 5: regeneration failure. |
| 23620650 [cached; full text] | "Myofibre necrosis and inflammation lead to fibrotic tissue remodelling." | Nodes 4 → 5 → 6. The body text is not abstract, so full-text matching is needed. |

**Model organism**

| PMID | Exact quote | Claim |
|---|---|---|
| 19864620 [cached] | "These results demonstrate that calcium itself is sufficient to induce muscular dystrophy in vivo, and that TRPC channels are key disease initiators downstream of the unstable membrane that characterizes many types of muscular dystrophy." | Node 3 is core and sufficient. |
| 19864620 [cached] | "Here we demonstrate that calcium itself is sufficient to cause a dystrophic phenotype in skeletal muscle independent of membrane fragility." | Node 2 is not obligatory. |
| 26088163 [cached] | "models with artificially elevated calcium in skeletal muscle manifest fulminant dystrophic-like disease, whereas models with enhanced calcium clearance or inhibited calcium influx are resistant to myofiber death and MD" | Node 3 → 4. The review itself says the authors "propose" this has "mostly proven" the hypothesis. |
| 35939054 [cached] | "Orai1 deficiency improves muscle pathology by both normalizing Ca2+ homeostasis and promoting sarcolemmal integrity/stability" | Edge 1a → 3 via SOCE. Note the quote is a clause from a longer sentence ("these results indicate that enhanced Orai1-dependent SOCE exacerbates the dystrophic phenotype and that Orai1 deficiency improves…"). |
| 19293339 [cached] | "In the absence of Cyp-D, Col6a1(-/-) mice show negligible myofiber degeneration, rescue from mitochondrial dysfunction and ultrastructural defects, and normalized incidence of apoptosis." | Node 4: PTP dependence in a non-DGC (matrix) myopathy. |
| 26536238 [cached] | "The immobilization also significantly reduced the structural damage in the mutated strains, showing that muscle activity is an important pathological mechanism." | Activity dependence in zebrafish dystrophin- and laminin-α2-deficient larvae. |
| 26536238 [cached; full text] | "In view of the lack of documented membrane rupture in the laminin α2-chain deficient models, the precise pathological mechanism for the effects of immobilization/activity remains to be clarified." | Caveat on LAMA2 → tears. Full text, not abstract. |
| 17389231 [cached] | "Now we show that late-onset expression of mini-agrin still prolongs life span and improves overall health" | Node 1a: restoring the laminin–dystroglycan link helps at all stages of MDC1A. |
| 21920942 [cached] | "Autophagy is increased in laminin α2 chain-deficient muscle and its inhibition improves muscle morphology in a mouse model of MDC1A." (title) | Secondary mechanism in LAMA2 beyond tears. Title only; not a finding to cite. |

**Review/synthesis and alternative hypothesis**

| PMID | Exact quote | Claim |
|---|---|---|
| 19793101 [cached] | "A defect in the expression of calpain-3 results in limb-girdle muscular dystrophy Type 2A." | Calpain boundary (§7). |
| 19793101 [cached] | "Calpain-3 is tightly bound in skeletal muscle fibres at the N2A line of the large elastic protein titin." | CAPN3 is a sarcomeric protease, not the necrosis effector. |
| 1497954 [cached] | "the observation that hypercontraction of the sarcomeres precedes membrane rupture" | Old (1992) alternative ordering: calcium before tears. Historical; use as a hypothesis only. |

**Not cached.** Run `just fetch-reference` on these before any curation use:
- PMID:8475120. Petrof 1993, PNAS 90:3710. mdx fibers show contraction-induced sarcolemmal rupture.
- PMID:12736685. Bansal 2003, Nature 423:168. Dysferlin-null muscle has an intact DGC and defective Ca²⁺-dependent resealing.
- PMID:18345011. Millay 2008, Nat Med 14:442. *Ppif* deletion reduces necrosis in *Sgcd*-null and *Lama2*-null mice, and Debio-025 helps mdx and *Sgcd*-null.
- Uezumi 2010, Nat Cell Biol (DOI 10.1038/ncb2014). PDGFRα+ interstitial progenitors, distinct from satellite cells, are the source of ectopic fat. PMID not confirmed.
- Bround 2023, Sci Adv (DOI 10.1126/sciadv.adi2767). ANT1 (*Slc25a4*) deletion plus *Ppif* deletion almost completely protects dystrophic mice from necrosis. PMID not confirmed.

---

## 5. Evidence for the causal edges

- **Calcium as hub (node 3).**
  - Strongest: sufficiency by TRPC3 overexpression (PMID:19864620) and rescue by genetic inhibition of calcium influx (PMID:26088163).
  - These are mouse genetic data. Resting calcium measurements in dystrophic fibers were "equivocal" (PMID:26088163).
  - The review's own open question is whether the load comes from "membrane ruptures or dysregulated ion channel and exchanger activity".
  - The module should not assert tears as the exclusive entry route.
- **Calcium → necrosis through the PTP (edge 3 → 4).**
  - Strongest for the cyclophilin D–dependent PTP: PMID:18345011 [NOT CACHED], PMID:19293339 [cached].
  - Direct human PTP evidence is absent from the cached set. The only patient-level link is the cyclosporin A response in UCMD mentioned in PMID:19293339.
- **Calpain (also edge 3 → 4).**
  - The existing description names calpain activation as a killing mechanism.
  - I found no cached primary study that isolates ubiquitous calpain (µ/m-calpain) as the effector in dystrophic necrosis.
  - Keep calpain as an annotation or hypothesis, not a required step.
- **Repair failure as an independent entry.**
  - Dysferlin (PMID:12736685, not cached): intact DGC, failed resealing.
  - ANO5 (PMID:20096397): lesions plus defective resealing.
  - MICU1 (PMID:31665639): repair compromised by mitochondrial calcium handling.
- **Downstream.** The literature cached here supports necrosis → inflammation → incomplete regeneration → fibrosis (PMID:23620650), but only as review prose. Fat origin from PDGFRα+ progenitors (Uezumi) is not cached.

---

## 6. Ontology suggestions (labels only; resolve IDs by lookup)

**GO biological process**
- plasma membrane repair
- calcium ion import across plasma membrane (check exact label)
- cellular response to calcium ion
- necrotic cell death
- regulation of mitochondrial membrane permeability involved in programmed necrotic cell death
- inflammatory response
- skeletal muscle tissue regeneration
- skeletal muscle satellite cell activation
- extracellular matrix organization
- collagen fibril organization
- fat cell differentiation

**GO molecular function and cellular component**
- calcium-dependent cysteine-type endopeptidase activity (for calpain annotation only)
- dystrophin-associated glycoprotein complex
- sarcolemma
- basement membrane

**CL**
- skeletal muscle fiber
- skeletal muscle satellite cell
- macrophage
- fibroblast
- adipocyte
- mesenchymal stem cell (as an approximate proxy for the fibro/adipogenic progenitor, which may not have a dedicated CL term; check, and if none exists, use `preferred_term` only per CLAUDE.md)

**UBERON**
- skeletal muscle tissue
- skeletal muscle organ
- diaphragm
- basal lamina (if distinct from the GO term)
- endomysium (if present)

---

## 7. Out of scope and boundary notes

- **Calpain-3 deficiency (CAPN3, LGMDR1):** not a conformer. Calpain-3 is a titin-bound sarcomeric protease, and the disease follows from its loss, not from calpain overactivation (PMID:19793101, PMID:20301490).
- **Collagen VI myopathies:** conform at node 4 only, via the PTP. Collagen VI is not a DGC component, and there is no tear evidence here. A defective autophagy contribution is also reported (PMID:21037586).
- **Dystrophic cardiomyopathy and smooth-muscle effects:** the cardiac arm belongs to `cardiomyopathy_maladaptive_remodeling`. This module should stay skeletal-muscle focused.
- **Sibling module `skeletal_muscle_mechanotransduction`:** that module covers absent or untransduced load signaling leading to atrophy. This module covers excess load on a fragile membrane leading to necrosis. State the contrast in the description to avoid overlap.
- **Generic fibrosis:** do not duplicate `fibrotic_response`. Use `conforms_to` for node 6.
- **Biomechanics at the tissue scale and therapy specifics** (exon skipping, gene therapy, steroids): out of scope; those belong in treatment entries.
- **Speculative, keep out:** the fibrosis-to-fragility feedback loop. Also keep out claims that hyperosmotic sodium or edema are required steps, because they rest on one review.

---

## 8. Open questions for curators

1. Should "Sarcolemmal Repair Machinery Failure" become a core-adjacent node, or should DYSF/ANO5 conform at node 2 with a note?
2. How should LAMA2 be handled? Options are `conforms_to` node 1a with a `HUMAN_MODEL_MISMATCH` discussion, or exclusion from node 2.
3. Does the module need a separate regeneration-failure node bound to satellite cell exhaustion, or should that stay in the sibling regeneration modules? Retrieve Uezumi and the satellite-cell literature first.
4. Should calpain stay in the node 4 description at all? If so, label it hypothesized, and add a discussion on calpain isoform specificity.
5. Modulators such as Orai1, TRPC, and PPIF are not disease genes. Encode them as `treatments[].target_mechanisms`-style drug-target patterns or experiment nodes, not `genes:` on pathophysiology.
6. Retrieve the NOT CACHED items with `just fetch-reference` and re-grade. Add `evidence_source: MODEL_ORGANISM` for the mouse and zebrafish items. Add `quote_role: REVIEW_SYNTHESIS` for the review quotes (PMID:26088163, PMID:34404573, PMID:23620650, PMID:19793101, PMID:36292621).
7. Add a `history/modules/sarcolemmal_fragility_myofiber_necrosis/` record when the module is expanded. The current file has five nodes with descriptions only, no edges, no evidence, and no `conforms_to` targets.

---

## Sources (retrieved this session)

- Petrof 1993 PNAS: https://pmc.ncbi.nlm.nih.gov/articles/PMC46371 (existence and finding only)
- Bansal 2003 Nature, PMID 12736685: https://www.qxmd.com/r/12736685 (existence only)
- Millay 2008 Nat Med: https://pmc.ncbi.nlm.nih.gov/articles/PMC2655270
- Uezumi 2010 Nat Cell Biol: https://www.nature.com/articles/ncb2014
- Bolduc 2010 AJHG: https://pmc.ncbi.nlm.nih.gov/articles/PMC2820170
- All other items come from the repo's `references_cache/` (PMID_*.md files).

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 30 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.