---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-07T04:23:18.728059'
end_time: '2026-08-07T04:36:12.919399'
duration_seconds: 774.23
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Deregulated Nutrient Sensing Module
  category: Module
  hypothesis_group_id: rapamycin_distinct_from_dietary_restriction
  hypothesis_label: Rapamycin Extends Lifespan by a Route Distinct from Dietary Restriction
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: rapamycin_distinct_from_dietary_restriction\n\
    hypothesis_label: Rapamycin Extends Lifespan by a Route Distinct from Dietary\
    \ Restriction\nstatus: EMERGING\ndescription: Rapamycin is routinely described\
    \ as a dietary-restriction mimetic, on the reasoning that\n  both down-shift anabolic\
    \ nutrient signaling and both extend lifespan. This hypothesis holds that the\n\
    \  shared endpoint conceals distinct routes - that pharmacologic mTORC1 inhibition\
    \ and dietary restriction\n  produce materially different endocrine, metabolic\
    \ and hepatic transcriptional states, and therefore\n  converge on longevity without\
    \ being the same intervention. The distinction matters for this module because\n\
    \  it determines whether mTORC1 hyperactivation is the single hub through which\
    \ the whole hallmark acts,\n  or one of several partly independent routes to the\
    \ same consequence node.\nevidence:\n- reference: PMID:24341993\n  supports: SUPPORT\n\
    \  evidence_source: MODEL_ORGANISM\n  snippet: Some of the endocrine and metabolic\
    \ changes seen in diet-restricted mice are not seen in mice\n    exposed to rapamycin,\
    \ and the pattern of expression of hepatic genes involved in xenobiotic metabolism\n\
    \    is also quite distinct in rapamycin-treated and diet-restricted mice, suggesting\
    \ that these two interventions\n    for extending mouse lifespan differ in many\
    \ respects.\n  explanation: 'Molecular rather than inferential separation of the\
    \ two interventions: endocrine and metabolic\n    changes diverge, and hepatic\
    \ xenobiotic-metabolism expression is distinct. This is the primary evidence\n\
    \    the hypothesis rests on.'\nnotes: The module currently takes no position\
    \ on this question - the mTORC1 node describes rapamycin as\n  targeting the anabolic\
    \ hub without asserting equivalence to dietary restriction, and the AMPK node\
    \ cites\n  a review that groups caloric restriction, sirtuin activation and rapamycin\
    \ together as one longevity-promoting\n  arm. Those two framings are in mild tension\
    \ and this hypothesis names it. A single study comparing two\n  interventions\
    \ in one tissue is thin support for a claim this load-bearing; the hypothesis\
    \ is declared\n  EMERGING to mark it as open rather than resolved."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 8
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
- **Disease Name:** Deregulated Nutrient Sensing Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** rapamycin_distinct_from_dietary_restriction
- **Hypothesis Label:** Rapamycin Extends Lifespan by a Route Distinct from Dietary Restriction
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: rapamycin_distinct_from_dietary_restriction
hypothesis_label: Rapamycin Extends Lifespan by a Route Distinct from Dietary Restriction
status: EMERGING
description: Rapamycin is routinely described as a dietary-restriction mimetic, on the reasoning that
  both down-shift anabolic nutrient signaling and both extend lifespan. This hypothesis holds that the
  shared endpoint conceals distinct routes - that pharmacologic mTORC1 inhibition and dietary restriction
  produce materially different endocrine, metabolic and hepatic transcriptional states, and therefore
  converge on longevity without being the same intervention. The distinction matters for this module because
  it determines whether mTORC1 hyperactivation is the single hub through which the whole hallmark acts,
  or one of several partly independent routes to the same consequence node.
evidence:
- reference: PMID:24341993
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Some of the endocrine and metabolic changes seen in diet-restricted mice are not seen in mice
    exposed to rapamycin, and the pattern of expression of hepatic genes involved in xenobiotic metabolism
    is also quite distinct in rapamycin-treated and diet-restricted mice, suggesting that these two interventions
    for extending mouse lifespan differ in many respects.
  explanation: 'Molecular rather than inferential separation of the two interventions: endocrine and metabolic
    changes diverge, and hepatic xenobiotic-metabolism expression is distinct. This is the primary evidence
    the hypothesis rests on.'
notes: The module currently takes no position on this question - the mTORC1 node describes rapamycin as
  targeting the anabolic hub without asserting equivalence to dietary restriction, and the AMPK node cites
  a review that groups caloric restriction, sirtuin activation and rapamycin together as one longevity-promoting
  arm. Those two framings are in mild tension and this hypothesis names it. A single study comparing two
  interventions in one tissue is thin support for a claim this load-bearing; the hypothesis is declared
  EMERGING to mark it as open rather than resolved.
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

# Rapamycin Extends Lifespan by a Route Distinct from Dietary Restriction

**Hypothesis-Search Report for the Disorder Mechanisms Knowledge Base**

- **Module:** Deregulated Nutrient Sensing
- **Hypothesis ID:** `rapamycin_distinct_from_dietary_restriction`
- **Status in KB:** EMERGING
- **Search date:** 2026-08-07
- **Evidence base:** 31 papers reviewed; 7 confirmed findings across 3 model systems (mouse, fly, human/clinical)

---

## Executive Judgment

**Verdict: Partially supported, trending toward supported — best described as "distinct but partially overlapping routes."**

The seed hypothesis holds that rapamycin and dietary restriction (DR) converge on longevity while producing "materially different endocrine, metabolic and hepatic transcriptional states," and therefore reach the shared endpoint by distinct routes rather than being the same intervention. The current literature substantiates the **divergence** claim strongly and across multiple organisms and molecular modalities, while also revealing a genuine **convergence** at the mTORC1 entry point that the strictest reading of the hypothesis ("fully distinct routes") does not accommodate. The accurate framing that the evidence supports is intermediate: the two interventions **enter through a shared nutrient-sensing hub (mTORC1) and share several downstream effectors (autophagy, translational suppression, a subset of the hepatic hypermethylation signature), yet diverge sharply on endocrine and metabolic axes — most dramatically insulin sensitivity, which they move in opposite directions.**

The single strongest piece of evidence for partly independent routes is an epistasis result in *Drosophila*: rapamycin further extends the lifespan of flies whose lifespan has already been maximized by DR ([PMID: 20074526](https://pubmed.ncbi.nlm.nih.gov/20074526/)). If the two interventions acted through one identical pathway, this additivity should not occur. Complementing it, the metabolic divergence is now triangulated across three systems — mouse ([PMID: 31577953](https://pubmed.ncbi.nlm.nih.gov/31577953/)), human/clinical ([PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/)), and hepatic proteome ([PMID: 25807975](https://pubmed.ncbi.nlm.nih.gov/25807975/)) — with rapamycin being diabetogenic (β-cell toxicity, mTORC2-driven insulin resistance) while DR is insulin-sensitizing.

**The most important caveats are:** (1) the shared-hub competing model is not refuted — TOR down-shift is a real point of convergence and mediates part of DR's longevity effect ([PMID: 21130151](https://pubmed.ncbi.nlm.nih.gov/21130151/)); (2) convergence exists even at the epigenetic level, where DR, rapamycin, and Ames dwarfism share a hepatic gene-body hypermethylation signature ([PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/)); and (3) the decisive experiment — a lifespan-matched, multi-omic head-to-head of DR vs. rapamycin vs. the combination in a single mouse cohort — has not been located as of the search date. Because the hypothesis is load-bearing for the module (it decides whether mTORC1 is *the* single hub or *one of several* routes), and because the divergence evidence is now multi-organism and mechanistic rather than inferential, I recommend upgrading the KB status from **EMERGING** toward **partially supported**, with an explicit subtype restriction to "distinct-but-overlapping" rather than "fully distinct."

---

## Key Findings

### F001 — Rapamycin and DR diverge molecularly in liver, supporting distinct routes

Multiple independent mouse studies show that the two interventions are not molecular equivalents. The seed evidence (Miller et al. 2014, [PMID: 24341993](https://pubmed.ncbi.nlm.nih.gov/24341993/)) reported that endocrine and metabolic changes seen in diet-restricted mice are not reproduced in rapamycin-treated mice, and that the hepatic expression pattern of xenobiotic-metabolism genes is distinct between the two. This was reinforced by a simultaneous measurement of translation, protein turnover, and abundance in liver (Karunadharma et al. 2015, [PMID: 25807975](https://pubmed.ncbi.nlm.nih.gov/25807975/)), which found that calorie restriction (CR) and rapamycin had **opposite** effects in the mitochondrial-dysfunction and eIF2-signaling canonical pathways. Verbatim: *"Surprisingly, the effects of RP and CR on protein turnover and abundance differed greatly between canonical pathways, with opposite effects in mitochondrial (mt) dysfunction and eIF2 signaling pathways."* Furthermore, the two interventions reduced protein synthesis by **distinct mechanics**: *"Polysome profiles indicated that CR reduced polysome loading while RP increased polysome loading in young and old mice, suggesting distinct mechanisms of reduced protein synthesis."* A review-level synthesis (Unnikrishnan et al. 2020, [PMID: 30854544](https://pubmed.ncbi.nlm.nih.gov/30854544/)) concluded that *"dietary restriction and rapamycin have different effects on many pathways and molecular processes"* and, decisively, that *"rapamycin is likely not a true dietary restriction mimetic."* This finding provides the molecular, rather than inferential, backbone of the hypothesis.

### F002 — Insulin sensitivity dissociates the two interventions: opposite direction, and dispensable for CR longevity

Yu et al. 2019 ([PMID: 31577953](https://pubmed.ncbi.nlm.nih.gov/31577953/)) demonstrated a striking dissociation using a canonical metabolic biomarker. Rapamycin extends mouse lifespan *yet* induces insulin resistance by disrupting mTORC2 — *"These include rapamycin, which extends mouse lifespan yet induces insulin resistance by disrupting mTORC2 (mechanistic target of rapamycin complex 2)"* — whereas CR improves insulin sensitivity. Using an adipose-specific Rictor knockout (AQ-RKO) that blocks CR's insulin-sensitizing effect, the authors showed mice still gained the same fitness and lifespan benefit from CR: *"We conclude that the CR-induced improvement in insulin sensitivity is dispensable for the effects of CR on fitness and longevity."* This is doubly informative: the two interventions move insulin sensitivity in **opposite directions**, and CR's canonical metabolic signature is causally decoupled from its longevity effect — proving that a shared longevity endpoint does not require a shared metabolic mechanism.

### F003 — Partial epigenetic convergence qualifies the "fully distinct" claim

Hahn et al. 2018 ([PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/)) performed whole-genome bisulfite sequencing of aged mouse liver across three longevity interventions (DR, rapamycin, Ames dwarfism) and found a **shared** signature of gene-body hypermethylation that was not merely a byproduct of slowed aging. This is a convergence result. However, the target genes partly diverged: *"DR causes a similar hypermethylation in lipid biosynthesis genes, while rapamycin treatment increases methylation signatures in genes coding for growth factor and growth hormone receptors."* This finding is the clearest reason the hypothesis should be framed as "distinct but partially overlapping" rather than "fully distinct" — the epigenetic layer shows both a shared axis and intervention-specific targets.

### F004 — Rapamycin extends already-DR-maximized fly lifespan (additivity/epistasis)

Bjedov et al. 2010 ([PMID: 20074526](https://pubmed.ncbi.nlm.nih.gov/20074526/)) fed rapamycin to adult *Drosophila* and showed lifespan extension specifically via the TORC1 branch through altered autophagy and translation. The pivotal result is an epistasis test: *"Rapamycin could increase life span of weak insulin/Igf signaling (IIS) pathway mutants and of flies with life span maximized by dietary restriction, indicating additional mechanisms."* If rapamycin and DR operated through one identical pathway, rapamycin could not extend a lifespan already saturated by DR. This additivity is the single most direct evidence for partly independent routes and the clearest discriminator against the strict shared-hub model.

### F005 — Competing view: TOR partly mediates DR longevity (shared-hub model)

Katewa & Kapahi 2011 ([PMID: 21130151](https://pubmed.ncbi.nlm.nih.gov/21130151/)) synthesize the classical "DR-mimetic" position: *"the nutrient-sensing TOR pathway appears to be critically important for mediating the longevity effects of dietary restriction,"* with *Drosophila* being the first organism where nutrient-dependent TOR effects on lifespan were uncovered. This underpins the competing model: if DR extends lifespan largely by down-shifting TOR, pharmacologic mTORC1 inhibition (rapamycin) would recapitulate DR's core longevity mechanism. This is not refuted by the divergence findings; it identifies the genuine convergence point and is the reason the seed hypothesis cannot be graded "supported" in its strict form.

### F006 — Human/clinical evidence: rapamycin is diabetogenic, opposite to DR

Barlow, Nicholson & Herbert 2013 ([PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/)) synthesize clinical (islet/renal transplant, oncology) and experimental evidence that rapamycin harms glucose homeostasis: *"these studies provide evidence that rapamycin has significant detrimental effects on β-cell function and survival and peripheral insulin resistance."* Rapamycin is implicated in new-onset diabetes after transplantation. This is the human-level counterpart to the mouse finding (Yu 2019), extending the metabolic-divergence axis into clinical data: rapamycin worsens glucose control while DR/CR characteristically improves insulin sensitivity and glucose tolerance.

### F007 — Overall synthesis: distinct-but-partially-overlapping routes

Triangulating across three organisms and multiple modalities yields a consistent picture:

- **Divergent axes:** insulin sensitivity opposite in mouse ([PMID: 31577953](https://pubmed.ncbi.nlm.nih.gov/31577953/)) and human ([PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/)); hepatic proteome eIF2/mitochondrial pathways opposite with distinct translational mechanics ([PMID: 25807975](https://pubmed.ncbi.nlm.nih.gov/25807975/)); endocrine and hepatic xenobiotic transcription distinct ([PMID: 24341993](https://pubmed.ncbi.nlm.nih.gov/24341993/)); partly distinct methylation targets ([PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/)).
- **Additivity:** rapamycin extends already-DR-maximized fly lifespan ([PMID: 20074526](https://pubmed.ncbi.nlm.nih.gov/20074526/)).
- **Convergent axes:** shared mTORC1 down-shift ([PMID: 21130151](https://pubmed.ncbi.nlm.nih.gov/21130151/), [PMID: 20074526](https://pubmed.ncbi.nlm.nih.gov/20074526/)); shared autophagy/translational suppression; shared subset of hepatic hypermethylation ([PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/)).
- **Review synthesis:** *"rapamycin is likely not a true dietary restriction mimetic"* ([PMID: 30854544](https://pubmed.ncbi.nlm.nih.gov/30854544/)).

**Key gap:** no lifespan-matched, multi-omic DR-vs-rapamycin-vs-combination mouse study was located as of the search date.

---

## Mechanistic Model / Interpretation

The two interventions can be modeled as sharing an entry node and a small set of downstream effectors, while diverging on the endocrine/metabolic branch that the strict "mimetic" model assumed was shared.

```
        DIETARY RESTRICTION                    RAPAMYCIN (pharmacologic)
        (reduced nutrient intake)              (direct mTORC1 inhibition)
                 │                                        │
                 │  reduces amino-acid / insulin          │  binds FKBP12 →
                 │  / IGF-1 signaling to TOR              │  inhibits mTORC1
                 ▼                                        ▼
        ┌─────────────────────  SHARED HUB  ─────────────────────┐
        │                    ↓ mTORC1 activity                    │  (F005, F004)
        └──────────────────────────┬──────────────────────────────┘
                                    │
             ┌──────────────────────┼───────────────────────┐
             ▼                      ▼                        ▼
    SHARED EFFECTORS         PARTIALLY SHARED         DIVERGENT BRANCH
    • ↑ autophagy            • hepatic gene-body      • mTORC2 handling:
    • ↓ translation            hypermethylation         DR spares / RAPA
      (F004)                   (shared signature,       disrupts mTORC2
                               distinct gene targets     → INSULIN RESISTANCE
                               F003)                      (F002, F006)
                                                        • hepatic proteome:
                                                          OPPOSITE eIF2 / mito
                                                          effects; opposite
                                                          polysome loading (F001)
                                                        • endocrine + xenobiotic
                                                          transcription distinct
                                                          (F001, seed)
                                    │
                                    ▼
                        CONVERGENT ENDPOINT: extended lifespan
                        (but ADDITIVE in flies → additional
                         non-DR mechanisms in rapamycin, F004)
```

**Where the literature is strong.** The divergent branch is well supported by direct molecular measurements: opposite insulin-sensitivity direction (three systems), opposite/distinct hepatic proteome and translational mechanics, and additivity in flies. The shared-hub entry node is also well established (decades of TOR-genetics work).

**Where links are inferred.** The claim that the divergent endocrine/metabolic states are *causally relevant to the distinct longevity routes* (rather than merely being side effects) is partly inferred. The fly additivity result (F004) is the strongest causal bridge, but its generalization to mammalian lifespan is an extrapolation.

**Missing causal steps.** (1) In mammals, whether rapamycin's "additional mechanisms" translate into additive lifespan on top of maximal DR has not been demonstrated. (2) Whether the shared hepatic hypermethylation is causal for longevity or a correlate of slowed aging is unresolved. (3) The mTORC2/insulin-resistance axis is clearly a divergence point, but whether it *subtracts* from rapamycin's longevity benefit (a healthspan cost) versus being neutral is unknown.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Context / subtype | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 24341993](https://pubmed.ncbi.nlm.nih.gov/24341993/) (Miller 2014) | Model organism (mouse) | **Support** | RAPA and DR produce different endocrine/metabolic and hepatic transcriptional states | Endocrine/metabolic changes and hepatic xenobiotic-metabolism gene expression distinct between RAPA and DR mice | Mouse liver | Moderate; single tissue, seed study, descriptive |
| [PMID: 25807975](https://pubmed.ncbi.nlm.nih.gov/25807975/) (Karunadharma 2015) | Model organism (mouse) | **Support** | RAPA and CR act on liver proteome by the same route | **Opposite** effects in mito-dysfunction & eIF2 pathways; CR ↓ polysome loading vs RAPA ↑ — distinct translational mechanisms | Mouse liver, subacute | High for divergence; subacute (not lifespan-matched) |
| [PMID: 30854544](https://pubmed.ncbi.nlm.nih.gov/30854544/) (Unnikrishnan 2020) | Review | **Support** | Is rapamycin a DR mimetic? | *"rapamycin is likely not a true dietary restriction mimetic"*; differ on many pathways | Mouse-focused synthesis | Review-level; orientation, not primary data |
| [PMID: 31577953](https://pubmed.ncbi.nlm.nih.gov/31577953/) (Yu 2019) | Model organism (mouse) | **Support / qualifies** | Insulin sensitivity mediates CR longevity | RAPA induces insulin resistance via mTORC2; CR-induced insulin sensitivity is **dispensable** for CR lifespan | Mouse adipose (AQ-RKO) | High; elegant genetic decoupling |
| [PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/) (Barlow 2013) | Human clinical + experimental (review) | **Support** | RAPA effect on glucose homeostasis | RAPA has detrimental effects on β-cell function/survival + peripheral insulin resistance; NODAT | Human transplant/oncology | Moderate; review synthesizing clinical data |
| [PMID: 20074526](https://pubmed.ncbi.nlm.nih.gov/20074526/) (Bjedov 2010) | Model organism (fly) | **Support (strongest)** | RAPA and DR act through one identical pathway | RAPA extends lifespan of **already DR-maximized** flies → "additional mechanisms"; acts via TORC1/autophagy/translation | *Drosophila* | High for additivity; invertebrate |
| [PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/) (Hahn 2018) | Model organism (mouse) | **Qualifies (partial convergence)** | Shared vs distinct epigenetic signatures | **Shared** hepatic gene-body hypermethylation across DR/RAPA/Ames; distinct gene targets (lipid vs GF/GH receptors) | Mouse liver, aged | High; both convergent & divergent evidence |
| [PMID: 21130151](https://pubmed.ncbi.nlm.nih.gov/21130151/) (Katewa & Kapahi 2011) | Review | **Competing (shared hub)** | TOR mediates DR longevity | TOR "critically important for mediating the longevity effects of DR" | *Drosophila*/general | Review-level; basis of DR-mimetic model |

---

## Limitations and Knowledge Gaps

**1. No lifespan-matched, multi-omic head-to-head in mammals (decisive gap).**
*Scope:* mouse. *Why it matters:* comparisons to date use different tissues, timepoints (e.g., subacute in [PMID: 25807975](https://pubmed.ncbi.nlm.nih.gov/25807975/)), and doses, so molecular divergence could partly reflect design rather than intrinsic mechanism. *What was checked:* the literature set of 31 papers; no such combined-cohort study located as of 2026-08-07. *Resolution:* a single cohort with DR, rapamycin, DR+rapamycin, and control arms, matched for lifespan extension, profiled by multi-tissue transcriptomics/proteomics/metabolomics with survival readout.

**2. Mammalian additivity untested.**
*Scope:* the strongest additivity evidence (F004) is in flies. *Why it matters:* additivity is the cleanest discriminator between "distinct routes" and "shared hub," but has not been demonstrated for mammalian lifespan. *Resolution:* the DR+rapamycin combination arm in experiment (1); expected result if hypothesis correct: combination exceeds either alone.

**3. Causality of shared hepatic hypermethylation unknown.**
*Scope:* mouse liver epigenetics ([PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/)). *Why it matters:* it is unclear whether the shared signature drives longevity or is a passive correlate of slowed aging. *Resolution:* targeted epigenetic-editing (dCas9-DNMT/TET) at shared loci with lifespan/healthspan readout.

**4. Mechanism of rapamycin's diabetogenic effect vs. longevity benefit.**
*Scope:* mouse + human. *Why it matters:* rapamycin disrupts mTORC2 → insulin resistance ([PMID: 31577953](https://pubmed.ncbi.nlm.nih.gov/31577953/), [PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/)); whether this is a healthspan cost that partly offsets its lifespan benefit, and whether intermittent dosing avoids it, is unresolved. *Resolution:* intermittent vs. continuous rapamycin with paired glucose-homeostasis and survival endpoints.

**5. Source/data absences.**
No human longevity RCT of rapamycin vs. DR was located. No omics cohort directly comparing the two interventions in matched human tissue was found. The clinical evidence for rapamycin's metabolic harm derives from transplant/oncology populations ([PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/)), not from longevity-intent dosing — a population-transferability caveat.

---

## Alternative Models

1. **Shared-hub / DR-mimetic model ([PMID: 21130151](https://pubmed.ncbi.nlm.nih.gov/21130151/)).** *Relationship:* direct alternative. Holds that DR extends lifespan primarily by down-shifting TOR, so rapamycin recapitulates the core mechanism. Not refuted; correctly identifies the convergence node. Weakened — but not eliminated — by fly additivity (F004) and mammalian metabolic divergence (F001, F002).

2. **mTORC2-disruption-as-liability model ([PMID: 31577953](https://pubmed.ncbi.nlm.nih.gov/31577953/), [PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/)).** *Relationship:* parallel/downstream. Rapamycin's off-target mTORC2 inhibition is a *distinct* branch from DR, producing insulin resistance. This is a mechanistic instantiation of "distinct routes" and directly supports the seed hypothesis while also naming a healthspan cost DR lacks.

3. **Convergent-effector model (autophagy + translational suppression).** *Relationship:* complementary. Both interventions upregulate autophagy and suppress translation (F004); these shared effectors may carry the longevity signal even when upstream endocrine states differ — reconciling divergence upstream with convergence at the endpoint.

4. **Epigenetic-convergence model ([PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/)).** *Relationship:* complementary/downstream. A shared hepatic hypermethylation program could be a common longevity mechanism despite distinct upstream signaling — again reconciling the two framings.

---

## Discriminating Tests / Proposed Follow-up Experiments

1. **Lifespan-matched combination trial in mice (highest priority).** Arms: control, DR, rapamycin, DR+rapamycin. Match doses so DR and rapamycin monotherapies produce equal lifespan extension. *Discriminating readout:* if DR+rapamycin exceeds either monotherapy → distinct routes (seed supported); if not additive → shared hub. Pair with multi-tissue transcriptomics/proteomics/metabolomics.

2. **mTORC2-preserving rapalog vs. classic rapamycin.** Compare a third-generation mTOR modulator that spares mTORC2 against rapamycin for lifespan and insulin sensitivity. *Expected if seed correct:* mTORC2-sparing agent removes the insulin-resistance divergence but may reduce lifespan differently, isolating which divergence axes are causal.

3. **Epigenetic editing at shared hypermethylated loci.** dCas9-DNMT/TET perturbation of the shared DR/RAPA/Ames loci ([PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/)) with survival readout to test whether epigenetic convergence is causal.

4. **Human biomarker stratification.** In longevity-intent low-dose rapamycin cohorts, stratify by baseline insulin sensitivity and track HOMA-IR, IGF-1, and hepatic transcriptomic proxies against DR cohorts. *Expected:* opposite HOMA-IR trajectories, confirming the human-level divergence beyond transplant populations.

---

## Curation Leads (require curator verification)

**Candidate status change.** Consider upgrading `rapamycin_distinct_from_dietary_restriction` from **EMERGING** toward **partially supported**, with an explicit subtype restriction: **"distinct but partially overlapping routes"** (not "fully distinct"). Rationale: divergence now multi-organism and mechanistic; convergence at mTORC1 hub and shared effectors documented.

**Candidate evidence references + snippets to verify:**
- [PMID: 25807975](https://pubmed.ncbi.nlm.nih.gov/25807975/): *"the effects of RP and CR on protein turnover and abundance differed greatly between canonical pathways, with opposite effects in mitochondrial (mt) dysfunction and eIF2 signaling pathways."*
- [PMID: 25807975](https://pubmed.ncbi.nlm.nih.gov/25807975/): *"Polysome profiles indicated that CR reduced polysome loading while RP increased polysome loading in young and old mice, suggesting distinct mechanisms of reduced protein synthesis."*
- [PMID: 30854544](https://pubmed.ncbi.nlm.nih.gov/30854544/): *"rapamycin is likely not a true dietary restriction mimetic"*
- [PMID: 31577953](https://pubmed.ncbi.nlm.nih.gov/31577953/): *"rapamycin, which extends mouse lifespan yet induces insulin resistance by disrupting mTORC2"* and *"the CR-induced improvement in insulin sensitivity is dispensable for the effects of CR on fitness and longevity."*
- [PMID: 23881200](https://pubmed.ncbi.nlm.nih.gov/23881200/): *"rapamycin has significant detrimental effects on β-cell function and survival and peripheral insulin resistance."*
- [PMID: 20074526](https://pubmed.ncbi.nlm.nih.gov/20074526/): *"Rapamycin could increase life span of ... flies with life span maximized by dietary restriction, indicating additional mechanisms."*
- [PMID: 30462643](https://pubmed.ncbi.nlm.nih.gov/30462643/): *"DR causes a similar hypermethylation in lipid biosynthesis genes, while rapamycin treatment increases methylation signatures in genes coding for growth factor and growth hormone receptors."*

**Candidate pathophysiology nodes/edges:**
- Add edge: `rapamycin → mTORC2 disruption → peripheral insulin resistance` (divergent branch; absent in DR).
- Add edge: `DR/rapamycin/Ames → shared hepatic gene-body hypermethylation` (convergent epigenetic node, distinct gene targets).
- Annotate `mTORC1` node: shared entry point but not sole determinant of downstream state; flag additivity (fly) evidence.
- Resolve the noted mTORC1-node vs. AMPK-node tension: the AMPK-node review grouping CR/sirtuin/rapamycin as one arm should be qualified with the "not a true DR mimetic" evidence.

**Candidate ontology terms:** insulin resistance (biomarker); mTORC2 complex; autophagy (biological process); DNA gene-body methylation; hepatic xenobiotic metabolism; pancreatic β-cell function.

**Candidate knowledge_gaps entries:** (1) no lifespan-matched multi-omic DR-vs-rapamycin-vs-combination mouse study; (2) mammalian additivity untested; (3) causality of shared hepatic hypermethylation unknown; (4) no human longevity RCT comparing the two; (5) transferability of transplant-population rapamycin metabolic-harm data to longevity dosing.

---

## Conclusion

As of 2026-08-07, the hypothesis that **rapamycin extends lifespan by a route distinct from dietary restriction** is **partially supported and trending toward supported.** The divergence is real, mechanistic, and multi-organism — most decisively the opposite direction of insulin-sensitivity change and the fly additivity over maximal DR. But the two interventions genuinely converge at the mTORC1 hub and share downstream effectors and part of the hepatic epigenetic program. The correct KB framing is **"distinct but partially overlapping routes"** rather than fully independent interventions, and the decisive lifespan-matched, multi-omic mouse experiment remains to be done.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)