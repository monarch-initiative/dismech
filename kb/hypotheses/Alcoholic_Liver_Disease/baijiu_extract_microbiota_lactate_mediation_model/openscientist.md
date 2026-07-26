---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T05:20:15.968350'
end_time: '2026-07-26T05:31:55.730715'
duration_seconds: 699.76
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Alcohol-Associated Liver Disease
  category: Complex
  hypothesis_group_id: baijiu_extract_microbiota_lactate_mediation_model
  hypothesis_label: Baijiu-extract microbiota-lactate mediation model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: baijiu_extract_microbiota_lactate_mediation_model\n\
    hypothesis_label: Baijiu-extract microbiota-lactate mediation model\nstatus: EMERGING\n\
    description: In the specific ethanol-exposed mouse model studied, one or more\
    \ non-ethanol Baijiu constituents\n  may reduce liver injury primarily by changing\
    \ intestinal microbial function, lowering gut-derived lactate\n  flux, and thereby\
    \ improving hepatic redox balance and oxidative stress. Whole-extract treatment\
    \ changed\n  microbial composition, lactate, hepatic NADH/NAD+ balance, and injury\
    \ concurrently, while lactate worsened\n  oxidative stress in cultured cells.\
    \ Candidate constituents were identified in the extract by GC-MS,\n  but no individual\
    \ constituent or combination was causally assigned to protection. These observations\n\
    \  do not establish a Ligilactobacillus strain as the relevant lactate source,\
    \ prove mediation, or support\n  a protective effect of Baijiu in humans.\nevidence:\n\
    - reference: PMID:42300615\n  reference_title: Non-ethanol components of Baijiu\
    \ alleviate ethanol-induced energy metabolism disorder\n    and gut microbiota\
    \ dysbiosis in mice.\n  supports: PARTIAL\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: Concurrently, they remodeled the gut microbial structure, restored\
    \ the Firmicutes/Bacteroidetes\n    (F/B) ratio, inhibited the abnormal proliferation\
    \ of g_Ligilactobacillus, and reduced lactate production.\n  explanation: The\
    \ mouse study links whole-extract exposure to concurrent microbiota and lactate\
    \ changes,\n    but does not establish that either change mediates hepatic protection.\n\
    - reference: PMID:42300615\n  reference_title: Non-ethanol components of Baijiu\
    \ alleviate ethanol-induced energy metabolism disorder\n    and gut microbiota\
    \ dysbiosis in mice.\n  supports: PARTIAL\n  evidence_source: IN_VITRO\n  snippet:\
    \ Cellular experiments confirmed that excessive lactate exacerbated oxidative\
    \ stress.\n  explanation: The cell assay supports lactate as a sufficient oxidative-stress\
    \ amplifier, but not its\n    microbial source, in-vivo flux, or necessity for\
    \ extract-mediated protection.\n- reference: PMID:42300615\n  reference_title:\
    \ Non-ethanol components of Baijiu alleviate ethanol-induced energy metabolism\
    \ disorder\n    and gut microbiota dysbiosis in mice.\n  supports: PARTIAL\n \
    \ evidence_source: OTHER\n  snippet: multiple active chemical constituents were\
    \ identified in this extract via GC-MS.\n  explanation: GC-MS nominates chemical\
    \ candidates in the extract, but does not causally assign the whole-extract\n\
    \    protection to an individual constituent or combination."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Alcohol-Associated Liver Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** baijiu_extract_microbiota_lactate_mediation_model
- **Hypothesis Label:** Baijiu-extract microbiota-lactate mediation model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: baijiu_extract_microbiota_lactate_mediation_model
hypothesis_label: Baijiu-extract microbiota-lactate mediation model
status: EMERGING
description: In the specific ethanol-exposed mouse model studied, one or more non-ethanol Baijiu constituents
  may reduce liver injury primarily by changing intestinal microbial function, lowering gut-derived lactate
  flux, and thereby improving hepatic redox balance and oxidative stress. Whole-extract treatment changed
  microbial composition, lactate, hepatic NADH/NAD+ balance, and injury concurrently, while lactate worsened
  oxidative stress in cultured cells. Candidate constituents were identified in the extract by GC-MS,
  but no individual constituent or combination was causally assigned to protection. These observations
  do not establish a Ligilactobacillus strain as the relevant lactate source, prove mediation, or support
  a protective effect of Baijiu in humans.
evidence:
- reference: PMID:42300615
  reference_title: Non-ethanol components of Baijiu alleviate ethanol-induced energy metabolism disorder
    and gut microbiota dysbiosis in mice.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: Concurrently, they remodeled the gut microbial structure, restored the Firmicutes/Bacteroidetes
    (F/B) ratio, inhibited the abnormal proliferation of g_Ligilactobacillus, and reduced lactate production.
  explanation: The mouse study links whole-extract exposure to concurrent microbiota and lactate changes,
    but does not establish that either change mediates hepatic protection.
- reference: PMID:42300615
  reference_title: Non-ethanol components of Baijiu alleviate ethanol-induced energy metabolism disorder
    and gut microbiota dysbiosis in mice.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: Cellular experiments confirmed that excessive lactate exacerbated oxidative stress.
  explanation: The cell assay supports lactate as a sufficient oxidative-stress amplifier, but not its
    microbial source, in-vivo flux, or necessity for extract-mediated protection.
- reference: PMID:42300615
  reference_title: Non-ethanol components of Baijiu alleviate ethanol-induced energy metabolism disorder
    and gut microbiota dysbiosis in mice.
  supports: PARTIAL
  evidence_source: OTHER
  snippet: multiple active chemical constituents were identified in this extract via GC-MS.
  explanation: GC-MS nominates chemical candidates in the extract, but does not causally assign the whole-extract
    protection to an individual constituent or combination.
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

# Mechanistic Hypothesis-Search Report

## Hypothesis: Baijiu-extract microbiota–lactate mediation model
**Disease:** Alcohol-Associated Liver Disease (ALD) · **Category:** Complex
**KB hypothesis ID:** `baijiu_extract_microbiota_lactate_mediation_model` · **KB status:** EMERGING
**Search date:** 2026-07-26

---

## 1. Executive Judgment

**Verdict: PARTIALLY SUPPORTED / UNRESOLVED — the model is mechanistically plausible but rests almost entirely on a single, correlational mouse study, and its distinctive causal claims are unproven while stronger competing mediators remain unexcluded.**

The seed model proposes a linear mediation chain: *non-ethanol Baijiu constituents → altered intestinal microbial function → lower gut-derived lactate flux → improved hepatic NADH/NAD⁺ redox → reduced oxidative stress → reduced liver injury.* Evaluating each edge against the current literature:

- **Plausible and partly established:** Two endpoints of the chain are individually well grounded. Lactate/lactylation is a **causally validated** driver of metabolic liver injury (lactate–H4K16la–PDK4 loop; MCT1–Arid1a lactylation; PMID:41329453, 42499162), and gut microbiota is **causally sufficient** to modulate ALD (FMT transmits susceptibility; PMID:27890791). So the "microbiota matters" and "lactate can be injurious" bookends are real.
- **Weak / unproven (the model's novel core):** The *specific* claims — that a Baijiu constituent acts **primarily** through microbiota, that the relevant lactate is **gut-derived** and fluxes to the liver, that this **mediates** (is necessary for) protection, and that a *Ligilactobacillus* strain is the **source** — are each unsupported. The source study reports only **concurrent, correlational** changes with **no formal mediation analysis, no causal constituent assignment, no strain isolation, and no gut→liver flux measurement**.
- **Contradicted sub-claim:** Framing alcohol-driven *g_Ligilactobacillus* proliferation as the pathogenic lactate source conflicts with a large literature in which *Lactobacillus* is **protective** and **depleted** in alcohol dysbiosis (PMID:41543328). (Hypothesis H003 rejected.)
- **Unexcluded competitors:** Canonical intrahepatic mechanisms (CYP2E1→acetaldehyde/ROS; ADH→NADH/NAD⁺ shift; NOX4) and gut-linked mechanisms (LPS/TLR4 leaky gut; tryptophan→AhR metabolites) explain the same redox/oxidative endpoints at least as parsimoniously and were neither measured nor ruled out.
- **Scope caveat correctly self-limited:** Human data (no safe alcohol dose; PMID:32135583, 38971533) confirm the seed's own disclaimer that this does **not** imply human Baijiu benefit; observed protection is a within-model *extract-vs-matched-ethanol* contrast.

**Most important caveat:** In severe human ALD, lactate is a **mortality marker** most parsimoniously explained by impaired hepatic clearance/hypoperfusion (PMID:41137971) — i.e., a **downstream consequence** of liver failure. This raises a live **reverse-causation** risk for the model's "lactate → injury" direction that the mouse data do not resolve.

---

## 2. Evidence Matrix

| # | Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 42300615 | Model organism (mouse) + in vitro | **Supports (partial)** | Whole extract → microbiota + lactate + NADH/NAD⁺ + injury change concurrently; lactate worsens oxidative stress in cells | Concurrent remodeling of microbiota, restored F/B, suppressed *g_Ligilactobacillus*, reduced lactate; lactate exacerbated oxidative stress in vitro | Ethanol-exposed mouse; extract vs ethanol | Single study; correlational; no mediation test; no causal constituent; no strain isolated |
| 2 | 41329453 | Model organism + human tissue | **Supports (edge: lactate→injury)** | Lactate/lactylation drives liver injury | Lactate–H4K16la–PDK4 feedback loop drives MAFLD; genetic/pharmacologic inhibition reduced lactate, lipid, and liver injury | MAFLD/MASH (not ALD) | Intrahepatic glycolytic lactate, not gut-derived; not alcohol |
| 3 | 42499162 | Model organism + in vitro | **Supports (edge: lactate→injury)** | Lactate-dependent lactylation drives steatosis | MCT1-mediated Arid1a K391 lactylation drives hepatic lipid accumulation; double-KO restores it | MAFLD | Non-ALD; non-histone lactylation; not gut-derived lactate |
| 4 | 41479511 | Review | **Qualifies** | Lactylation in steatohepatitis | Lactate→H3K18la promotes pro-inflammatory/fibrogenic genes; **"a direct demonstration of histone lactylation in ASH has not yet been reported"** | MASH/ASH | Review-level; explicitly flags ALD-specific evidence gap |
| 5 | 40421024 / 39809380 | Review | Qualifies | Lactate/lactylation as liver-disease targets | Lactylation implicated across fibrosis, NAFLD, HCC | General liver disease | Orientation only; ALD not central |
| 6 | 27890791 | Model organism (FMT) | **Competing/supports microbiota causality** | Microbiota is causal in ALD | FMT from alcohol-resistant donors + pectin prevent alcohol liver injury; Bacteroides lower in sensitive mice | ALD (Lieber-DeCarli) | Establishes microbiota sufficiency but not the lactate effector |
| 7 | 33004548 | Model organism (humanized) + KO | **Competing** | Tryptophan→AhR metabolites mediate microbiota protection | Bacterial tryptophan metabolites improve ALD via AhR; benefit lost in AhR-KO | Human-microbiota-associated ALD mice | Strong causal competitor to lactate axis |
| 8 | 34082111 | Model organism + human tissue | **Competing (redox)** | AhR–NQO1 protects via redox | AhR activation counteracts alcohol-induced NAD(P) redox stress; AhR-KO worsens injury | ALD + alcoholic hepatitis tissue | Redox endpoint explained without gut lactate |
| 9 | 41543328 | Model organism (mouse) | **Refutes (H003) / competing** | Lactobacillus role + F/B ratio | *L. plantarum* NXU0014 is **protective**; alcohol raised F/B and **depleted** Lactobacillus/Bifidobacterium; acts via Nrf2/HO-1 + barrier | Chronic alcohol-liquor mouse | Contradicts pathogenic-Ligilactobacillus framing; near-identical model |
| 10 | 39832564 | Review | **Competing** | Gut-barrier/LPS→TLR4→oxidative stress | Dysbiosis → barrier loss → LPS translocation → TLR4 → NADPH-oxidase ROS | MASLD/gut-liver axis | Review-level but mechanistically explicit; dominant competitor |
| 11 | 24400890 | Review | **Competing** | LPS/Kupffer-cell axis in ALD | Enhanced gut permeability → LPS → Kupffer-cell TNF-α → alcoholic liver injury | ALD | Review; classical, heavily replicated pathway |
| 12 | 30641601 | Review | **Competing (intrahepatic)** | CYP2E1→acetaldehyde/ROS | CYP2E1 oxidizes ethanol to acetaldehyde and generates ROS; inhibition improves ALD | ALD, fibrosis, HCC | Canonical intrahepatic oxidative mechanism |
| 13 | 29025729 | In vitro / imaging | **Competing (redox)** | ADH→NADH/NAD⁺ shift | Cytosolic ADH oxidation of ethanol generates NADH and raises NADH/NAD⁺ | Fatty liver / hepatocytes | Explains seed's redox endpoint intrinsically |
| 14 | 27634671 | Model organism + in vitro | **Competing (redox)** | NOX4→mitochondrial ROS | NOX4 inhibition ameliorates alcohol liver injury and oxidative stress | ALD (Lieber-DeCarli) | Alternative ROS source independent of lactate |
| 15 | 42349181 | In vitro (fish hepatocytes) | Supports (weak, edge) | Lactate→histone lactylation→pyroptosis | Elevated lactate enhances histone lactylation, triggers pyroptosis | Herbicide toxicity, grass carp | Non-alcohol, non-mammalian; low transferability |
| 16 | 41137971 | **Human clinical** (n=2,096) | **Qualifies** | Lactate–ALD outcome link in humans | Serum lactate independently predicts 90-day mortality in alcohol-related ACLF (HR 1.187/mmol/L) | Severe ALD / alcoholic hepatitis ACLF | Severity/clearance marker; reverse-causation risk |
| 17 | 32135583 | **Human meta-analysis** | **Qualifies (scope)** | Alcohol dose vs liver harm | >low alcohol raises liver-disease mortality (OR 3.22) and liver cancer (OR 1.42) | General population | Bounds human Baijiu-benefit extrapolation |
| 18 | 38971533 | **Human cohort** | **Qualifies (scope)** | Low/moderate alcohol vs fibrosis | Low-moderate alcohol independently associated with fibrosis/at-risk MASH | MASLD/MetALD | No safe dose; supports seed's human disclaimer |

---

## 3. Mechanistic Causal Chain (edge-by-edge)

```
Non-ethanol Baijiu constituents (GC-MS candidates)
        │  [EDGE A: constituent → effect]  ── INFERRED (whole extract only; no constituent causally assigned)
        ▼
Altered intestinal microbial composition/function
        │  [EDGE B: microbiota → lactate]  ── WEAK (correlational; direction & key taxa unproven; Lactobacillus role contradicted)
        ▼
Lower GUT-DERIVED lactate flux to liver
        │  [EDGE C: gut lactate → hepatic exposure]  ── MISSING (no flux/tracer/portal-vein data; not measured in ALD)
        ▼
Improved hepatic NADH/NAD⁺ redox balance
        │  [EDGE D: lactate → redox]  ── CONFOUNDED (ADH/CYP2E1 set hepatic redox intrinsically; PMID:29025729, 30641601)
        ▼
Reduced hepatic oxidative stress
        │  [EDGE E: redox → ROS]  ── PLAUSIBLE but non-specific (NOX4, LPS/TLR4, AhR all converge here)
        ▼
Reduced liver injury (clinical manifestation)
```

- **Strong links:** the terminal biology (lactate/lactylation *can* injure hepatocytes; PMID:41329453/42499162) and the upstream principle (microbiota *can* causally modulate ALD; PMID:27890791).
- **Inferred links:** Edge A (whole-extract → specific constituent) and Edge B (microbiota → lactate) are correlational.
- **Missing links (the crux):** **Edge C** — gut-derived lactate actually reaching and acting on the liver — was never demonstrated; **mediation** (necessity) was never tested; and **Edge D** is confounded by intrinsic ethanol metabolism that independently sets hepatic NADH/NAD⁺.

---

## 4. Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | Resolving evidence/experiment |
|---|---|---|---|---|
| **G1 — No mediation test** | Whole chain | "Primarily mediates" is the core claim; concurrency ≠ mediation | Read seed abstract (PMID:42300615); no formal mediation reported | Formal causal mediation analysis; or lactate add-back that abolishes protection |
| **G2 — Gut→liver lactate flux unverified (CHECKED ABSENCE)** | Edge C | Distinguishes gut-derived vs intrahepatic glycolytic lactate; the model's pivotal edge | **Two independent PubMed queries (2026-07-26) returned zero papers** — "intestinal microbial lactate portal vein hepatic uptake gut-liver axis" and "D-lactate gut microbiota liver disease serum biomarker translocation" | Portal-vein vs systemic lactate; ¹³C-lactate/isotope tracing; germ-free/gnotobiotic add-back |
| **G3 — Ligilactobacillus source unconfirmed & contradicted** | Edge B/source | Names a specific pathogenic source at odds with probiotic literature | Searched Lactobacillus/ALD → PMID:41543328 shows protective/depleted | Isolate strain; mono-colonize; measure D/L-lactate output and injury |
| **G4 — No causal constituent** | Edge A | GC-MS nominates but does not assign causation | Seed abstract | Fractionation + single-compound dosing vs whole extract |
| **G5 — Redox endpoint confounded** | Edge D | ADH/CYP2E1 set NADH/NAD⁺ and ROS intrinsically | PMID:29025729, 30641601, 27634671 | Hold ethanol metabolism constant; test lactate's marginal redox effect |
| **G6 — ALD/ASH-specific lactylation absent** | Terminal edge | Lactylation causality shown in MASH, not ASH | PMID:41479511 explicitly states this | H3K18la/H4K16la ChIP + lactylation inhibitor (DCA) in alcohol models |
| **G7 — Competitors unexcluded** | Model selection | LPS/TLR4 and Trp→AhR explain same endpoints | PMID:39832564, 24400890, 33004548 | Co-measure endotoxin, barrier markers, indole metabolites, AhR targets |
| **G8 — Reverse causation in humans** | Human relevance | Lactate may be consequence, not cause | PMID:41137971 | Longitudinal/early-stage lactate vs injury; lactate-lowering trial |
| **G9 — No human/clinical or trial evidence** | Source/data absence | Model is mouse-only; no cohort/omics/trial | Searched human alcohol-liver literature | Human ALD cohort with paired stool metagenomics + serum lactate + AhR/LPS panels |

---

## 5. Alternative Models

1. **LPS/endotoxin → TLR4 → Kupffer-cell → NADPH-oxidase oxidative stress** (PMID:39832564, 24400890). *Parallel/competing* microbiota-linked mechanism; the dominant, heavily replicated gut-liver axis in ALD. Not measured by the seed.
2. **Microbiota tryptophan/indole metabolites → hepatic AhR (→NQO1)** (PMID:33004548, 34082111). *Competing* microbiota mediator with **direct causal (KO) evidence** in ALD and convergence on the same redox endpoint — arguably more parsimonious than gut lactate.
3. **Intrahepatic CYP2E1→acetaldehyde/ROS and ADH→NADH/NAD⁺ shift** (PMID:30641601, 29025729). *Upstream/parallel* hepatocyte-intrinsic drivers that explain the seed's redox and oxidative endpoints **without any gut lactate**.
4. **NOX4-driven mitochondrial ROS** (PMID:27634671). *Parallel* intrahepatic ROS source.
5. **Intrahepatic (glycolytic) lactate → lactylation → fibro-inflammatory transcription** (PMID:41329453, 42499162). *Complementary but re-attributes the source* — same terminal lactylation biology, but lactate is hepatocyte-derived rather than gut-derived; would preserve the "lactate matters" idea while refuting "gut-derived."
6. **Probiotic/barrier-restoration model** (PMID:41543328). *Competing directionality* — restoring (not suppressing) Lactobacillus/Bifidobacterium and repairing the barrier via Nrf2/HO-1 protects.

---

## 6. Discriminating Tests

1. **Gut-vs-hepatic lactate origin (resolves G2/Edge C).** Alcohol + extract mice; measure **portal-vein vs systemic lactate** and run **¹³C-glucose/lactate tracing**; use **germ-free/antibiotic** mice ± defined lactate producers. *Seed predicts:* extract lowers portal (gut-derived) lactate and protection is lost in germ-free/lactate-add-back. *Competitors predict:* hepatic lactate tracks intrahepatic glycolysis, unchanged portal flux.
2. **Mediation by lactate (resolves G1).** In extract-protected mice, **restore colonic/portal lactate** (or feed D-lactate) to the protected level. *Seed predicts:* protection abolished. *If injury unchanged:* lactate is a bystander.
3. **Strain causality (resolves G3).** **Isolate the expanded *Ligilactobacillus***, mono-colonize gnotobiotic alcohol-fed mice, quantify D/L-lactate and injury; compare to *L. plantarum* NXU0014. *Seed predicts:* the isolate raises lactate and worsens injury (against the protective-genus prior).
4. **Constituent deconvolution (resolves G4).** Activity-guided fractionation of the GC-MS candidates; single-compound and combination dosing vs whole extract, with microbiota readout.
5. **Competitor co-measurement (resolves G7).** In the same animals, panel **serum endotoxin/LBP, intestinal ZO-1/occludin, indole/AhR-target genes (Cyp1a1), CYP2E1, NOX4** alongside lactate; use **structural equation / mediation modeling** to rank mediators. Add **AhR-KO** and **TLR4-KO** arms to test necessity of competitors.
6. **Lactylation-in-ALD (resolves G6).** Quantify hepatic **H3K18la/H4K16la** in alcohol models ± extract; test **DCA/PDK inhibition** or **MCT inhibition**. *Seed/lactate axis predicts:* extract lowers lactylation and lactylation inhibition mimics protection.
7. **Human anchoring (resolves G8/G9).** Prospective ALD cohort with **paired stool metagenomics + portal/systemic lactate + AhR/LPS biomarkers** across stages; test whether **early-stage** lactate precedes injury (causal) or only rises with decompensation (consequence).

---

## 7. Curation Leads *(require curator verification)*

**Candidate evidence references + exact snippets to verify:**
- PMID:41543328 — *"alcohol intake induced gut microbiota dysbiosis, characterized by an increased Firmicutes/Bacteroidetes ratio and decreased abundance of probiotics (e.g., Lactobacillus and Bifidobacterium)"* → **conflicts** with seed's pathogenic-*Ligilactobacillus* framing.
- PMID:41479511 — *"Although a direct demonstration of histone lactylation in ASH has not yet been reported"* → ALD-specific gap for the lactate→injury terminal edge.
- PMID:33004548 — *"High production of bacterial tryptophan metabolites was associated with an improvement of liver injury"* → competing microbiota mediator (Trp→AhR).
- PMID:27890791 — *"fecal microbiota transplantation which resulted in an IM very close to that of resistant donor mice in the sensitive recipient mice"* → microbiota causal sufficiency in ALD.
- PMID:41329453 — *"Genetic or pharmacologic inhibition reduced lactate, lipid accumulation, and liver injury. We identify a lactate-H4K16la-PDK4 axis..."* → lactate→injury edge (MASH).
- PMID:41137971 — *"elevated serum lactate (HR 1.187 per mmol/L, p < 0.001)"* → human lactate as severity marker (reverse-causation caveat).
- PMID:32135583 — *"pooled OR for liver disease-related mortality ... was 3.220 (95% CI, 2.116 to 4.898)"* → bounds human Baijiu-benefit claims.

**Candidate pathophysiology nodes/edges (leads):**
- Add competing edges: `microbiota → LPS translocation → TLR4 → NADPH-oxidase → hepatic oxidative stress`; `microbiota → tryptophan/indoles → hepatic AhR → NQO1 → redox protection`; `ethanol → CYP2E1 → acetaldehyde/ROS`; `ethanol → ADH → NADH/NAD⁺`; `intrahepatic glycolysis → lactate → histone lactylation (H3K18la/H4K16la) → fibro-inflammatory transcription`.
- Flag seed edge `gut-derived lactate → liver` as **UNVERIFIED (source-to-target)** and edge `whole extract → specific constituent` as **INFERRED**.

**Candidate ontology terms:**
- Cell types: hepatocyte (CL:0000182), Kupffer cell (CL:0000091), hepatic stellate cell (CL:0000632).
- Processes: response to oxidative stress (GO:0006979), NAD metabolic process (GO:0019674), protein lactylation (GO:0140838 / histone lactylation), lipopolysaccharide-mediated signaling / TLR4 (GO:0034142), aryl hydrocarbon receptor signaling (GO:0140986), lactate metabolic process (GO:0006089-adjacent).
- Disease context: alcoholic steatohepatitis; alcohol-related acute-on-chronic liver failure.

**Candidate subtype restrictions / status:**
- Keep **status = EMERGING**; restrict scope to **single ethanol-exposed mouse model, extract-vs-ethanol contrast**. Explicitly annotate **no human evidence** and **no net human Baijiu benefit**.
- Add subtype note: terminal lactate/lactylation causality is demonstrated in **MASH/MAFLD**, **not ASH**.

**Candidate `knowledge_gaps` / discussion prompts:** G1–G9 above (mediation untested; gut→liver lactate flux unverified; Ligilactobacillus source contradicted; no causal constituent; redox confounded by ADH/CYP2E1; ASH-specific lactylation absent; competitors unexcluded; human reverse-causation; no cohort/trial/omics data).

---

## 8. Limitations of this search
- Literature-only assessment (no primary data provided); PubMed access with a backend indexing error that dropped a few abstract-less hits (queries were re-run).
- The seed source (PMID:42300615) abstract was available but its full methods/mediation details could not be inspected; mediation-absence is inferred from the abstract.
- Competing-mechanism reviews (PMID:39832564, 24400890, 30641601) are labeled review-level; their underlying primary claims are long-established.

*Report generated Iteration 4 of 5.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
