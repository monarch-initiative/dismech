---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T03:40:49.871630'
end_time: '2026-10-16T03:42:07.996679'
duration_seconds: 78.13
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: Hepatic Gluconeogenesis Failure Module
  module_slug: hepatic_gluconeogenesis_failure
  category: Module
  module_description: 'A conserved mechanism module representing the final common
    pathway by which a loss-of-function lesion at any one of the rate-controlling
    gluconeogenic enzymes collapses de novo glucose synthesis in the liver and produces
    the shared biochemical signature of the gluconeogenic enzymopathies: fasting (and
    catabolic-stress) hypoglycemia together with lactic acidosis. The four classic
    enzyme blocks - pyruvate carboxylase (PC), cytosolic phosphoenolpyruvate carboxykinase
    (PEPCK/PCK1), fructose-1,6-bisphosphatase (FBP1), and glucose-6-phosphatase (G6PC)
    - sit at different points of the pathway but converge on one gene-agnostic step:
    the hepatocyte can no longer convert three-carbon precursors into glucose and
    release it into the circulation. Two consequences fan out from that convergence.
    On the output side, failed hepatic glucose production causes fasting hypoglycemia,
    which deprives the brain of its obligate fuel and produces neuroglycopenic manifestations
    (lethargy, seizures, coma). On the substrate side, the three-carbon precursors
    that cannot be consumed by gluconeogenesis (pyruvate, lactate, alanine, glycerol)
    accumulate, driving lactate overproduction and a high-anion-gap lactic acidosis.
    Conforming disorder entries substitute the specific blocked enzyme and its position
    on the pathway while preserving this core chain. Key conformance target: `hepatic_gluconeogenesis_failure#Failure
    of Hepatic De Novo Glucose Production`. Real and potential conformers already
    in kb that a curator would wire to this module: Fructose-1,6-Bisphosphatase_Deficiency
    (FBP1, the committed gluconeogenic step converting fructose-1,6-bisphosphate to
    fructose-6- phosphate), Pyruvate_Carboxylase_Deficiency_Disease (PC, the anaplerotic
    pyruvate-to-oxaloacetate entry step), Glycogen_Storage_Disease_Type_I (G6PC, the
    terminal glucose-6-phosphate dephosphorylation shared by gluconeogenesis and glycogenolysis),
    and the cytosolic PEPCK (PCK1) entry being curated in parallel. Complementary
    to, and deliberately distinct from, the respiratory-chain and bioenergetic modules.
    complex_i_deficiency and mitochondrial_dysfunction also terminate in lactic acidosis,
    but by a different mechanism - failed oxidative ATP synthesis forcing anaerobic
    glycolysis - and they do not primarily impair de novo glucose synthesis; this
    module''s lactic acidosis arises from unconsumed gluconeogenic substrate, not
    from a respiratory-chain block. peroxisomal_metabolic_failure and congenital_disorder_of_glycosylation
    are other hepatic/metabolic modules that act on entirely different substrates
    and do not converge on hepatic glucose output. Where a conformer carries both
    a gluconeogenic block and a secondary respiratory-chain phenotype (PC deficiency
    can show secondary complex IV deficiency), it may conform to this module and a
    respiratory-chain module at different nodes.'
  pathophysiology_summary: '- Gluconeogenic Flux Block: A loss-of-function lesion
    in one of the rate-controlling gluconeogenic enzymes - pyruvate carboxylase, cytosolic
    phosphoenolpyruvate carboxykinase, fructose-1,6-bisphosphatase, or glucose-6-phosphatase
    - interrupts carbon flux through the hepatic gluconeogenic pathway. Conforming
    entries substitute the specific enzyme and its position on the pathway.

    - Failure of Hepatic De Novo Glucose Production: With any committed step blocked,
    the hepatocyte can no longer synthesize new glucose from three-carbon precursors.
    This is the gene-agnostic, rate-limiting convergence every conforming disorder
    funnels through, whatever the specific enzyme lesion. PC, PEPCK, and FBP1 fail
    to build free glucose-6-phosphate, while G6PC fails to dephosphorylate it to glucose;
    both routes abolish net de novo glucose production.

    - Reduced Hepatic Glucose Output: The liver fails to release glucose into the
    circulation during fasting. Hepatic gluconeogenesis is one of the fluxes summed
    into net hepatic glucose production, so losing it lowers the glucose the liver
    can supply once dietary intake stops and glycogen stores are depleted.

    - Fasting Hypoglycemia: Once dietary glucose and glycogen stores are exhausted,
    the loss of hepatic glucose output causes blood glucose to fall during fasting
    or catabolic stress (fever, intercurrent illness, reduced intake).

    - Accumulation of Gluconeogenic Three-Carbon Substrates: Three-carbon precursors
    that would normally be consumed by gluconeogenesis - pyruvate, lactate, alanine,
    and glycerol - accumulate upstream of the enzyme block. The accumulation is most
    prominent for the enzymes nearest pyruvate (PC, PEPCK), where the entry steps
    of the pathway are blocked.

    - Lactate Overproduction: The accumulated pyruvate is reduced to lactate, elevating
    the circulating lactate concentration. Because the gluconeogenic sink for lactate
    is disabled, lactate generated by ongoing glycolysis is no longer recycled to
    glucose.

    - Lactic Acidosis: Elevated circulating lactate produces a high-anion-gap metabolic
    acidosis, the second cardinal biochemical feature of the gluconeogenic enzymopathies
    alongside hypoglycemia.

    - CNS Glucose Deprivation: The brain depends on blood glucose as its obligate
    fuel, so fasting hypoglycemia deprives neurons of their primary energy substrate.
    Prolonged or recurrent deprivation injures the central nervous system.

    - Neuroglycopenic Dysfunction: Neuronal energy failure from glucose deprivation
    produces the acute neuroglycopenic manifestations of the gluconeogenic enzymopathies:
    lethargy, seizures, and - in severe crises - coma.'
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
  num_turns: 8
  total_cost_usd: 0.6631384
  session_id: 6f407ab6-10d8-510b-8a76-b165dbc02479
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 2
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 7
  on_topic: 5
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
- **Module Name:** Hepatic Gluconeogenesis Failure Module
- **Module Slug:** hepatic_gluconeogenesis_failure
- **Category:** Module

## Current Module Description

A conserved mechanism module representing the final common pathway by which a loss-of-function lesion at any one of the rate-controlling gluconeogenic enzymes collapses de novo glucose synthesis in the liver and produces the shared biochemical signature of the gluconeogenic enzymopathies: fasting (and catabolic-stress) hypoglycemia together with lactic acidosis. The four classic enzyme blocks - pyruvate carboxylase (PC), cytosolic phosphoenolpyruvate carboxykinase (PEPCK/PCK1), fructose-1,6-bisphosphatase (FBP1), and glucose-6-phosphatase (G6PC) - sit at different points of the pathway but converge on one gene-agnostic step: the hepatocyte can no longer convert three-carbon precursors into glucose and release it into the circulation. Two consequences fan out from that convergence. On the output side, failed hepatic glucose production causes fasting hypoglycemia, which deprives the brain of its obligate fuel and produces neuroglycopenic manifestations (lethargy, seizures, coma). On the substrate side, the three-carbon precursors that cannot be consumed by gluconeogenesis (pyruvate, lactate, alanine, glycerol) accumulate, driving lactate overproduction and a high-anion-gap lactic acidosis. Conforming disorder entries substitute the specific blocked enzyme and its position on the pathway while preserving this core chain. Key conformance target: `hepatic_gluconeogenesis_failure#Failure of Hepatic De Novo Glucose Production`. Real and potential conformers already in kb that a curator would wire to this module: Fructose-1,6-Bisphosphatase_Deficiency (FBP1, the committed gluconeogenic step converting fructose-1,6-bisphosphate to fructose-6- phosphate), Pyruvate_Carboxylase_Deficiency_Disease (PC, the anaplerotic pyruvate-to-oxaloacetate entry step), Glycogen_Storage_Disease_Type_I (G6PC, the terminal glucose-6-phosphate dephosphorylation shared by gluconeogenesis and glycogenolysis), and the cytosolic PEPCK (PCK1) entry being curated in parallel. Complementary to, and deliberately distinct from, the respiratory-chain and bioenergetic modules. complex_i_deficiency and mitochondrial_dysfunction also terminate in lactic acidosis, but by a different mechanism - failed oxidative ATP synthesis forcing anaerobic glycolysis - and they do not primarily impair de novo glucose synthesis; this module's lactic acidosis arises from unconsumed gluconeogenic substrate, not from a respiratory-chain block. peroxisomal_metabolic_failure and congenital_disorder_of_glycosylation are other hepatic/metabolic modules that act on entirely different substrates and do not converge on hepatic glucose output. Where a conformer carries both a gluconeogenic block and a secondary respiratory-chain phenotype (PC deficiency can show secondary complex IV deficiency), it may conform to this module and a respiratory-chain module at different nodes.

## Current Provisional Nodes

- Gluconeogenic Flux Block: A loss-of-function lesion in one of the rate-controlling gluconeogenic enzymes - pyruvate carboxylase, cytosolic phosphoenolpyruvate carboxykinase, fructose-1,6-bisphosphatase, or glucose-6-phosphatase - interrupts carbon flux through the hepatic gluconeogenic pathway. Conforming entries substitute the specific enzyme and its position on the pathway.
- Failure of Hepatic De Novo Glucose Production: With any committed step blocked, the hepatocyte can no longer synthesize new glucose from three-carbon precursors. This is the gene-agnostic, rate-limiting convergence every conforming disorder funnels through, whatever the specific enzyme lesion. PC, PEPCK, and FBP1 fail to build free glucose-6-phosphate, while G6PC fails to dephosphorylate it to glucose; both routes abolish net de novo glucose production.
- Reduced Hepatic Glucose Output: The liver fails to release glucose into the circulation during fasting. Hepatic gluconeogenesis is one of the fluxes summed into net hepatic glucose production, so losing it lowers the glucose the liver can supply once dietary intake stops and glycogen stores are depleted.
- Fasting Hypoglycemia: Once dietary glucose and glycogen stores are exhausted, the loss of hepatic glucose output causes blood glucose to fall during fasting or catabolic stress (fever, intercurrent illness, reduced intake).
- Accumulation of Gluconeogenic Three-Carbon Substrates: Three-carbon precursors that would normally be consumed by gluconeogenesis - pyruvate, lactate, alanine, and glycerol - accumulate upstream of the enzyme block. The accumulation is most prominent for the enzymes nearest pyruvate (PC, PEPCK), where the entry steps of the pathway are blocked.
- Lactate Overproduction: The accumulated pyruvate is reduced to lactate, elevating the circulating lactate concentration. Because the gluconeogenic sink for lactate is disabled, lactate generated by ongoing glycolysis is no longer recycled to glucose.
- Lactic Acidosis: Elevated circulating lactate produces a high-anion-gap metabolic acidosis, the second cardinal biochemical feature of the gluconeogenic enzymopathies alongside hypoglycemia.
- CNS Glucose Deprivation: The brain depends on blood glucose as its obligate fuel, so fasting hypoglycemia deprives neurons of their primary energy substrate. Prolonged or recurrent deprivation injures the central nervous system.
- Neuroglycopenic Dysfunction: Neuronal energy failure from glucose deprivation produces the acute neuroglycopenic manifestations of the gluconeogenic enzymopathies: lethargy, seizures, and - in severe crises - coma.

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

# Hepatic Gluconeogenesis Failure Module: mechanism research report

**Verification status.** I fetched PubMed records for the PMIDs in section 6 and checked their bibliographic details. The fetch tool returned only short excerpts, not full abstracts.

- Quotes marked "excerpt, fetched" were returned by the tool. Check them against the abstract before using them as snippets, because the tool may have trimmed or altered them.
- All other claims come from established biochemistry and my own knowledge. They have no PMID or quote here and need a literature pass.
- I did not search for or verify any ontology IDs. Section 5 gives labels only, to be looked up with `runoak` or the term caches.

---

## 1. Executive recommendation

**Keep the module slug `hepatic_gluconeogenesis_failure`, but narrow what it claims.** The shared mechanism is well supported: loss of a rate-controlling gluconeogenic enzyme → failed hepatic de novo glucose synthesis → fasting hypoglycemia, plus lactic acidosis from unconsumed three-carbon substrate. Four points need adjusting.

1. **Lactic acidosis is not equally core across the four enzymes.**
   - Lactic acidosis is prominent in the enzyme blocks nearest pyruvate and in the fructose-1,6-bisphosphatase (FBP1) and glucose-6-phosphatase (G6PC) deficiencies.
   - In cytosolic phosphoenolpyruvate carboxykinase (PEPCK-C, PCK1) deficiency, lactic acidosis is variable. The Finnish cohort (PMID 34622459) is notable for deficient ketogenesis and a characteristic urinary organic acid pattern.
   - Make the substrate-accumulation branch (substrate accumulation → lactate overproduction → lactic acidosis) **core-but-variable**. Conformers should be allowed to say it is absent or episodic.
2. **G6PC is a boundary case.**
   - G6PC sits at the terminal step shared with glycogenolysis. The glycogen-store-depletion explanation for the hypoglycemia therefore does not apply, and glycogen accumulates.
   - Glycogen Storage Disease Type I (GSD I) has its own large phenotype: hepatomegaly, hyperuricemia and hypertriglyceridemia. The GeneReviews excerpt (PMID 20301489) does list the shared signature: "severe hypoglycemia with or without seizures, lactic acidosis, hyperuricemia, and hypertriglyceridemia."
   - Keep GSD I as a conformer at the "Failure of Hepatic De Novo Glucose Production" node only. Its glycogen-storage and metabolic-syndrome features belong in the disease entry or another module.
3. **Add an optional renal and intestinal gluconeogenesis note.** PEPCK, FBP1 and G6PC are also expressed in kidney cortex and intestine. This is from textbook knowledge, not from a source I checked here. It explains why patients can have kidney involvement and why blocking hepatic gluconeogenesis alone is not the whole picture. "Hepatic" is still the right scope for the primary node.
4. **Do not expand the name.** "Gluconeogenic enzymopathy" would be broader but would invite pulling in the pyruvate dehydrogenase and respiratory-chain disorders, which the module description deliberately excludes.

---

## 2. Proposed DAG: core versus optional

| Node | Status | Notes |
|---|---|---|
| Gluconeogenic Flux Block | **Core** (entry) | The conformer substitutes its specific enzyme and pathway position. |
| Failure of Hepatic De Novo Glucose Production | **Core** (key conformance target) | The gene-agnostic convergence point. |
| Reduced Hepatic Glucose Output | **Core** | Hepatic glucose output is the sum of gluconeogenesis and glycogenolysis. In G6PC deficiency both are blocked. |
| Fasting Hypoglycemia | **Core** | Present in every conformer. Triggers are fasting and catabolic stress. |
| Accumulation of Gluconeogenic Three-Carbon Substrates | **Core-but-variable** | Strongest for PC and PEPCK. Label it as pathway-position dependent. |
| Lactate Overproduction | **Core-but-variable** | Follows from the node above. |
| Lactic Acidosis | **Core-but-variable** | Episodic in FBP1 deficiency, with acute crises showing "lactic acidosis and ketotic hypoglycemia" (GeneReviews PMID 31804789, paraphrased from fetch). |
| CNS Glucose Deprivation | **Optional** | |
| Neuroglycopenic Dysfunction | **Optional** | Seizures, lethargy and coma. Supported by PCK1 case reports (PMID 33445193, PMID 37924129). |

**Causal edges**
- Flux Block → Failure of De Novo Glucose Production
- Failure of De Novo Glucose Production → Reduced Hepatic Glucose Output → Fasting Hypoglycemia
- Fasting Hypoglycemia → CNS Glucose Deprivation → Neuroglycopenic Dysfunction
- Flux Block → Substrate Accumulation → Lactate Overproduction → Lactic Acidosis

**Suggested additions (judgement calls for the curator)**
- An optional **Impaired Ketogenesis / Hypoketotic Hypoglycemia** branch for PEPCK-C deficiency, which has a Finnish-cohort source (PMID 34622459). I would not make it core, since FBP1 deficiency presents with ketotic hypoglycemia.
- An optional **Hepatic Steatosis / Hepatomegaly** branch. FBP1 deficiency has an 18-patient series (PMID 34687058). It is not part of the convergent chain.

---

## 3. Gene-to-node mapping

| Gene (enzyme) | Entry node | Position | Distinctive features |
|---|---|---|---|
| PC (pyruvate carboxylase) | Gluconeogenic Flux Block | Mitochondrial pyruvate → oxaloacetate | Lactic acidosis; hyperammonemia and hypoglycemia (GeneReviews excerpt, PMID 20301764). Also anaplerotic, which is why PC fits the boundary note on respiratory-chain overlap. |
| PCK1 (PEPCK-C) | Gluconeogenic Flux Block | Oxaloacetate → phosphoenolpyruvate | Hypoglycemia, encephalopathy, seizures, vulnerability during intercurrent illness (PMID 37924129). |
| FBP1 (fructose-1,6-bisphosphatase) | Gluconeogenic Flux Block | Fructose-1,6-bisphosphate → fructose-6-phosphate | Lactic acidosis and ketotic hypoglycemia; fatty liver (PMID 34687058). Fructose challenge is hazardous (PMID 31804789). |
| G6PC1 (glucose-6-phosphatase) | Failure of Hepatic De Novo Glucose Production, plus Reduced Hepatic Glucose Output | Terminal step, shared with glycogenolysis | Also hepatomegaly, hyperuricemia and hypertriglyceridemia. |

PCK1 also has a mitochondrial paralog, PCK2. I did not research it, and the module says "cytosolic PEPCK".

---

## 4. Evidence table

Excerpts are short, as returned by the fetch tool. "Fetched" means the tool returned the text. The abstracts must be re-read before the text goes into a snippet.

### Human clinical and review evidence

| PMID | Type | Excerpt (fetched) | Supports |
|---|---|---|---|
| 20301489 | Review (GeneReviews) | "severe hypoglycemia with or without seizures, lactic acidosis, hyperuricemia, and hypertriglyceridemia." | G6PC block → hypoglycemia and lactic acidosis. |
| 20301764 | Review (GeneReviews) | "severe lactic acidosis, hyperammonemia, and often hypoglycemia." | PC block → lactic acidosis, with hypoglycemia as a common but not invariable feature. |
| 31804789 | Review (GeneReviews) | "Fructose tolerance testing (fructose challenge) to diagnose FBP1 deficiency can be hazardous and should not be performed." | A diagnostic boundary note. The lactic acidosis and ketotic hypoglycemia claim is paraphrased only. |
| 34687058 | Case series (18 patients) | "Interestingly, all 18 patients had liver abnormalities." | Optional hepatic steatosis branch in FBP1 deficiency. |
| 25246452 | Case report | "FDPase deficiency can be suspected using simple bedside tests such as glucometer." | FBP1 deficiency as a gluconeogenesis defect. |
| 35868242 | Systematic analysis, 32 individuals | "PEPCK-C deficiency is a recognizable cause of childhood hypoglycemia." | PCK1 block → hypoglycemia. |
| 34622459 | Cohort, 24 Finnish patients | Paraphrase only. Deficient ketogenesis was described as a novel finding. | Optional ketogenesis branch. |
| 37924129 | Family case series | "Patients become vulnerable during intercurrent illness." | Catabolic-stress trigger; neuroglycopenic presentation. |
| 33445193 | Case report | Paraphrase only. | Neuroglycopenic end of the chain: hypoglycemic seizure leading to cerebral edema and death. |
| 28368361 | Review | Paraphrase only. | Links inborn errors of fructose metabolism to hypoglycemia, lactic acidosis and hyperuricemia. |
| 23622387 | Review | Paraphrase only. | Pyruvate metabolism disorders. The FBP1 papers are not the right fit for it. |

### Model organism and in vitro evidence

I did not retrieve any. The curator should run a targeted search for liver-specific Pck1, Fbp1 and G6pc knockout mice. They would clarify the hepatic-versus-renal contribution and whether mouse hypoglycemia reproduces the human phenotype. That is a candidate `HUMAN_MODEL_MISMATCH` discussion.

### Not supported by anything retrieved
- The statement that gluconeogenesis is "one of the fluxes summed into net hepatic glucose production" has no source here.
- The high-anion-gap characterisation of the acidosis has no source here.
- The claim that CNS deprivation causes lasting injury, as distinct from acute neuroglycopenia, has no source here.
- Comparative statements about substrate accumulation by enzyme position are unsupported beyond textbook reasoning.

---

## 5. Ontology suggestions (labels only; IDs to be looked up)

**GO biological processes**
- gluconeogenesis
- glucose homeostasis
- cellular response to glucose starvation
- lactate metabolic process
- pyruvate metabolic process
- regulation of blood pH or pH reduction
- glycogen catabolic process (for the G6PC boundary)
- ketone body biosynthetic process (for the optional branch)

**GO molecular functions**
- pyruvate carboxylase activity
- phosphoenolpyruvate carboxykinase activity
- fructose-bisphosphatase activity
- glucose-6-phosphatase activity

**CL cell types**
- hepatocyte
- neuron (for the neuroglycopenic node)
- renal tubule epithelial cell (optional)

**UBERON anatomy**
- liver
- brain
- kidney cortex (optional)

For HP phenotypes, candidates are hypoglycemia, lactic acidosis, seizures, hepatomegaly and hepatic steatosis. Look the IDs up before binding.

---

## 6. Out-of-scope boundary notes

- **Respiratory-chain and bioenergetic lactic acidosis** (`complex_i_deficiency`, `mitochondrial_dysfunction`) is excluded. The mechanism there is anaerobic glycolysis from failed ATP synthesis.
- **PDH deficiency** also produces lactic acidosis but through a different step. A reviewer may be tempted to conform it here.
- **Glycogen storage disease beyond the G6PC step** (for example glycogenolysis defects) is excluded.
- **Fatty-acid oxidation and ketogenesis disorders** are excluded. Their hypoglycemia is hypoketotic, but it is a different primary lesion.
- **Hyperinsulinism and endocrine causes of hypoglycemia** are excluded.
- **Acquired gluconeogenic failure** (for example in liver failure, alcohol-related hypoglycemia, or biguanide-associated lactic acidosis) is not covered by the retrieved literature. Treat it as out of scope unless a curator decides otherwise.

---

## 7. Open questions for curator review

1. Should lactic acidosis be a required conformance node, or core-but-variable? I recommend core-but-variable. PEPCK-C and FBP1 deficiency are episodic and strongly state-dependent.
2. Should GSD I conform only at the production-failure node, or is its glycogen-storage phenotype enough to put it in a separate module? I lean toward the former.
3. Is a ketogenesis or fatty-liver branch worth adding? Both have a source above.
4. Is "hepatic" the right scope given the renal and intestinal contribution? This is unsourced here.
5. Which retrieved papers need full-text reading? Most of the series and cohort papers (PMIDs 34687058, 34622459, 37924129, 35868242), because the fetch returned only paraphrases and short excerpts.
6. Model-organism evidence was not searched. Do that before curating the `modeled_mechanisms` links.
7. Mitochondrial PCK2 and mitochondrial pyruvate transport were not examined. Decide whether they are in or out.

---

Sources (PubMed and NCBI Bookshelf records fetched via NCBI E-utilities):
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31804789,34687058,28368361,25246452,23622387,12013992,37924129,35868242,34622459,33445193&rettype=abstract&retmode=text
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=20301489,20301764&rettype=abstract&retmode=text

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.