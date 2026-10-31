---
provider: openscientist
model: openscientist-autonomous
job_id: 2a29b55d-1b26-4de1-9bc4-600efa583abb
job_created_at: '2026-10-24T14:57:46.569824Z'
job_updated_at: '2026-10-24T17:13:16.335214Z'
fetched_at: '2026-10-24T17:14:35Z'
recovered_with: scripts/hypothesis_deep_research.py fetch
template_file: templates/hypothesis_deep_research.md
template_file_source: fetch-argument
template_sha: 1058b49f7af15426533f5808c12fcde757216952
report_member: final_report.md
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1O
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** katp_metabolic_gating_failure
- **Hypothesis Label:** Failure of KATP metabolic-stress gating as the CMD1O lesion
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: katp_metabolic_gating_failure
hypothesis_label: Failure of KATP metabolic-stress gating as the CMD1O lesion
status: EMERGING
description: 'The proposed model: a C-terminal ABCC9 variant displaces SUR2A''s catalytic cycle, the Kir6.2
  pore is consequently mis-gated, the cardiomyocyte cannot match electrical and contractile work to energetic
  demand under stress, calcium overload follows, and calcineurin-dependent remodeling converts that into
  a dilated, arrhythmogenic ventricle. The molecular arm is demonstrated in recombinant systems; the myocardial
  arm is supported by KATP-deficient animals but has never been shown for an ABCC9 catalytic-domain allele
  in a heart, human or otherwise. It is recorded as EMERGING rather than CANONICAL because the gene-disease
  relationship it explains is itself classified as Limited.'
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

When dataset or scientific-tool access is available, use it for questions that
can be tested computationally rather than limiting the run to literature search.
Preflight the required data lake, databases, packages, credentials, and tools
before claiming that an analysis can run. Never silently fall back from a failed
dataset/tool analysis to literature synthesis or model knowledge: report the
failure, the fallback, and the resulting limitation explicitly. A proposed
analysis must never be described as performed.

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

### Data and Tool Use

Inventory every dataset, database, API, supplementary file, or local input
material to the report. For each, state:

- stable accession or URI, repository/source, version or snapshot, and retrieval
  date where known;
- whether it was only cited/proposed, actually accessed, searched with no usable
  result, or could not be verified;
- the exact query, filters, cohort, sample subset, organism, tissue, assay, and
  comparison used where applicable;
- whether the accession resolved and whether its subject matter is genuinely
  relevant to this disease and hypothesis.

For accessed sources and negative searches, save a sanitized query response,
input manifest, or search log in the provider artifact bundle; prose alone does
not establish access or a negative result.

Inventory each attempted analysis separately. Trace input -> method -> output,
including software/model versions, material parameters, code or workflow,
environment, random seeds where relevant, output files, and limitations. Label
the execution outcome as succeeded, partial, failed, skipped, or reported-only.
Do not count a prose assertion without inspectable execution evidence as a
successful analysis.

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
evidence or experiment would resolve it. A negative database search must include
the database/version, query, filters, and search date; otherwise label it
unverified rather than claiming absence.

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

If the provider supports artifacts, produce a provider artifact bundle containing
canonical `MANIFEST.yaml` (schema version, status/fallback flags, checksummed
inputs/outputs, and replay verification), code/query/configuration, an
environment or package-version record,
sanitized execution logs, and small derived tables/figures needed to inspect the
result beneath `kb/hypotheses/Dilated_Cardiomyopathy_1O/katp_metabolic_gating_failure/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.

## Output

# Mechanistic Hypothesis Search — Dilated Cardiomyopathy 1O

## Hypothesis under evaluation
- **Disease:** Dilated Cardiomyopathy 1O (CMD1O), Mendelian
- **Hypothesis ID:** `katp_metabolic_gating_failure`
- **Hypothesis label:** Failure of KATP metabolic-stress gating as the CMD1O lesion
- **Status in KB:** EMERGING
- **Search date:** 2026-10-24

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — should remain EMERGING, not be promoted to CANONICAL.**

The KATP metabolic-stress gating-failure model is mechanistically coherent and each of its two "arms" has independent experimental support, but the two arms have never been joined in a single relevant system, and the genetic foundation of the gene–disease relationship it explains is weak and partly contradicted by newer evidence.

The **molecular arm** — that C-terminal ABCC9/SUR2A variants displace the intrinsic ATP-hydrolytic (catalytic) cycle of SUR2A and thereby mis-gate the Kir6.2 pore — is directly demonstrated, but only in **recombinant heterologous systems** ([PMID: 15034580](https://pubmed.ncbi.nlm.nih.gov/15034580/)). The **myocardial arm** — that loss of KATP metabolic decoding under stress produces Ca²⁺ overload and calcineurin-dependent maladaptive remodeling — is demonstrated **only in a pore-subunit (KCNJ11/Kir6.2) knockout mouse**, not in any animal or human heart carrying an ABCC9 catalytic-domain allele ([PMID: 16782803](https://pubmed.ncbi.nlm.nih.gov/16782803/)). The critical causal edge — *an ABCC9 catalytic allele causing the remodeling phenotype in a heart* — remains entirely inferred.

The most important caveats are genetic. ABCC9's validity as a monogenic DCM gene is **Limited**: it is absent from the robustly replicated set of 12 DCM genes in the largest curated cohort ([PMID: 31983221](https://pubmed.ncbi.nlm.nih.gov/31983221/)) and falls below high-evidence thresholds in the ClinGen DCM curation ([PMID: 33947203](https://pubmed.ncbi.nlm.nih.gov/33947203/)). No ABCC9 variant carries expert-panel ClinVar review. The original CMD1O founder allele **p.Ala1513Thr is present in gnomAD at ~5×10⁻⁵** and has been reclassified to "Conflicting classifications of pathogenicity," undercutting its status as a fully penetrant dominant cause. Finally, the broader ABCC9 allelic series argues against a simple "KATP-loss → DCM" model: **gain-of-function** ABCC9 variants cause Cantú syndrome, and **biallelic loss-of-function** variants cause ABCC9-related intellectual disability and myopathy syndrome (AIMS) — neither prominently a dilated cardiomyopathy. Population-genetics constraint (LoF-tolerant, strongly missense-intolerant) is most consistent with a **dominant-negative / conformational** mechanism rather than haploinsufficiency, but that specific mechanism is itself unproven for a heart allele.

In short: the hypothesis is a plausible, internally consistent synthesis whose molecular and physiological components are each supported in isolation, but whose central disease-specific claim (an ABCC9 catalytic allele mis-gating KATP in a cardiomyocyte to produce CMD1O) is untested and whose genetic premise is fragile.

---

## Key Findings

### F001 — The molecular arm is supported in recombinant systems

ABCC9/SUR2A C-terminal variants disrupt the catalytic ATPase cycle and mis-gate KATP. Bienengraeber et al. 2004 ([PMID: 15034580](https://pubmed.ncbi.nlm.nih.gov/15034580/)) identified two ABCC9 mutations (a missense and a frameshift) in idiopathic DCM patients, mapping to conserved domains adjacent to the SUR2A catalytic ATPase pocket. In recombinant expression, mutant SUR2A proteins showed *"aberrant redistribution of conformations in the intrinsic ATP hydrolytic cycle, translating into abnormal K(ATP) channel phenotypes with compromised metabolic signal decoding. Defective catalysis-mediated pore regulation is thus a mechanism for channel dysfunction and susceptibility to dilated cardiomyopathy."* This is the strongest direct evidence for the molecular arm of the hypothesis — but it is **in vitro / recombinant**, not myocardial, and it establishes *susceptibility*, not deterministic causation.

### F002 — The myocardial arm is supported only by a pore-subunit knockout, not an ABCC9 allele

Kane et al. 2006 ([PMID: 16782803](https://pubmed.ncbi.nlm.nih.gov/16782803/)) showed that in experimental hypertension, KCNJ11 (Kir6.2) knockout mice develop heart failure and death. *"Defective decoding of hypertension-induced metabolic distress signals in the K(ATP) channel knockout set in motion pathological calcium overload and aggravated cardiac remodeling through a calcium/calcineurin-dependent cyclosporine-sensitive pathway."* Rescue was achieved by controlling Ca²⁺ influx. This confirms the Ca²⁺/calcineurin remodeling arm in a KATP-deficient heart — but it uses **deletion of the pore-forming subunit (Kir6.2/KCNJ11)**, not an ABCC9/SUR2A catalytic-domain allele. The remodeling phenotype here is driven by complete loss of channel presence, which is mechanistically distinct from a conformationally mis-gating SUR2A mutant.

### F003 — ABCC9's gene–disease validity for DCM is Limited

Mazzarotto et al. 2020 ([PMID: 31983221](https://pubmed.ncbi.nlm.nih.gov/31983221/)), the largest sequenced DCM cohort (2,538 patients, 912 controls, ExAC reference), found robust disease association for only 12 genes; **ABCC9 was not among them.** The authors conclude that candidate genes outside this set *"will need to be rigorously evaluated in ongoing curation efforts to determine their validity as Mendelian DCM genes but have limited value in diagnostic testing in DCM at present."* Independently, the ClinGen-framework curation of 51 DCM genes ([PMID: 33947203](https://pubmed.ncbi.nlm.nih.gov/33947203/)) classified only 12 as definitive/strong and 7 as moderate; ABCC9 falls below these high-evidence tiers. This is the single most important external constraint on the hypothesis: the gene–disease relationship it explains is itself weakly supported.

### F004 — A competing allelic series complicates the loss-of-function → DCM model

The ABCC9 allelic series does not map cleanly onto "KATP loss → DCM":
- **Gain-of-function** ABCC9 variants cause **Cantú syndrome**, with cardiovascular phenotypes (cardiac enlargement, vascular tortuosity/dilation, low systemic vascular resistance) — e.g., [PMID: 41448431](https://pubmed.ncbi.nlm.nih.gov/41448431/), [PMID: 39031464](https://pubmed.ncbi.nlm.nih.gov/39031464/).
- **Biallelic loss-of-function** variants cause **ABCC9-related intellectual disability and myopathy syndrome (AIMS)** — periventricular leukomalacia, developmental delay, muscle weakness/fatigability — [PMID: 38217872](https://pubmed.ncbi.nlm.nih.gov/38217872/), [PMID: 42290677](https://pubmed.ncbi.nlm.nih.gov/42290677/). In AIMS, *"All variants are predicted to result in severe truncations or in-frame deletions within SUR2, leading to the generation of non-functional SUR2-dependent KATP channels"* — yet the conserved phenotype is neurodevelopmental/myopathic, **not** a dilated cardiomyopathy. Heterozygous carriers show intra-uterine fetal death in some reports but not a conserved cardiomyopathy.

That complete SUR2 loss-of-function produces a neuromuscular syndrome rather than DCM is a direct challenge to a simple KATP-gating-failure model and implies that, if CMD1O is real, it must operate via a specific allele class (likely dominant-negative missense) rather than generic loss of function.

### F005 — Population-genetics constraint favors a dominant-negative/conformational mechanism

gnomAD v2.1.1 constraint for ABCC9 (ENSG00000069431), retrieved 2026-10-24 via GraphQL:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 7.9×10⁻¹¹ (~0) | LoF-tolerant |
| oe_lof | 0.50 (obs 95 / exp 188) | Heterozygous LoF tolerated |
| LOEUF (oe_lof_upper) | 0.60 | Not LoF-constrained |
| mis_z | 7.62 | Strongly missense-constrained |
| oe_mis | 0.587 (obs 1102 / exp 1876) | Missense depletion |

Heterozygous loss-of-function is tolerated, which argues **against** haploinsufficiency as the CMD1O mechanism. In contrast, missense variation is strongly constrained, consistent with specific missense alleles exerting a **dominant-negative or conformational** effect — exactly the class to which the Bienengraeber catalytic-domain missense belongs. This refines (does not prove) the hypothesis toward a dominant-negative mis-gating model.

### F006 — The founding CMD1O alleles are low-confidence in ClinVar

ClinVar (NCBI eutils, accessed 2026-10-24):
- The original Bienengraeber 2004 allele **p.Ala1513Thr (c.4537G>A, VCV 8162)** is "Pathogenic" but with **"no assertion criteria provided"** (0-star legacy 2004 submission under condition *Dilated cardiomyopathy 1O*).
- The second founder allele is now represented as **c.4512+744_4512+746delinsAAAT (VCV 222477)** with **"Conflicting classifications of pathogenicity."**
- **Zero** ABCC9 variants are "reviewed by expert panel" or "practice guideline" (counts = 0).
- Among ABCC9 P/LP variants submitted under a "dilated cardiomyopathy" condition (n = 205), the inspected top entries are predominantly nonsense/frameshift/splice (LoF) truncations (e.g., p.Tyr193Ter, p.Ser93fs, c.285-1G>C) — i.e., **AIMS-type recessive LoF alleles**, all single-submitter (1-star) or conflicting.

The genetic anchor for CMD1O is therefore legacy, low-review, and partly displaced by a recessive-LoF variant landscape.

### F007 — Founder allele A1513T is population-present and reclassified

gnomAD (via GraphQL clinvar_variants join, retrieved 2026-10-24) for ABCC9 p.Ala1513Thr (c.4537G>A): exome AC/AN = 10/251,072 (3.98×10⁻⁵); genome AC/AN = 4/31,394 (1.27×10⁻⁴); combined 14/282,466 = **4.96×10⁻⁵** (~14 heterozygous carriers in ~141,000 individuals). The same amino-acid change carries two ClinVar records: legacy VCV 8162 "Pathogenic, no assertion criteria" (0 stars) and VCV 856369 "Conflicting classifications of pathogenicity" (1 star). A carrier frequency of ~5×10⁻⁵ is higher than expected for a fully penetrant dominant cause of a rare cardiomyopathy, and the reclassification to Conflicting undercuts A1513T's status as a definitive CMD1O allele.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports / refutes / qualifies / competing | Mechanistic claim tested | Key finding | Disease subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [15034580](https://pubmed.ncbi.nlm.nih.gov/15034580/) | In vitro / recombinant + human genetics | **Supports** (molecular arm) | C-terminal ABCC9 variants displace SUR2A catalytic cycle → Kir6.2 mis-gating | Mutant SUR2A shows aberrant conformational redistribution in ATP hydrolytic cycle, compromised metabolic signal decoding | Idiopathic DCM / CMD1O founder study | Moderate; recombinant only, susceptibility not causation, 2 index alleles |
| [16782803](https://pubmed.ncbi.nlm.nih.gov/16782803/) | Model organism (mouse) | **Supports** (myocardial arm) | KATP loss → Ca²⁺ overload → calcineurin remodeling under stress | KCNJ11(Kir6.2)-KO mice develop HF in hypertension via Ca²⁺/calcineurin, cyclosporine-sensitive | Hypertensive cardiac remodeling | Moderate; uses pore-subunit KO, NOT an ABCC9 allele |
| [31983221](https://pubmed.ncbi.nlm.nih.gov/31983221/) | Human clinical / cohort | **Qualifies / weakens** | Is ABCC9 a valid monogenic DCM gene? | Only 12 genes robustly associated; ABCC9 not among them | Large DCM cohort (2,538 cases) | High; defines the Limited-validity constraint |
| [33947203](https://pubmed.ncbi.nlm.nih.gov/33947203/) | Human curation (ClinGen) | **Qualifies / weakens** | ABCC9 gene–disease validity | 12 definitive/strong + 7 moderate of 51; ABCC9 below high evidence | Expert DCM gene curation | High; authoritative validity framework |
| [38217872](https://pubmed.ncbi.nlm.nih.gov/38217872/) | Human clinical | **Competing** | Biallelic ABCC9 LoF phenotype | Severe truncations/in-frame deletions → non-functional SUR2 → AIMS (neuro/myopathy), not DCM | AIMS | High; shows LoF ≠ DCM |
| [42290677](https://pubmed.ncbi.nlm.nih.gov/42290677/) | Human clinical + recombinant | **Competing** | Biallelic LoF → AIMS natural history | Leukomalacia, developmental delay, muscle weakness; biallelic LoF driven | AIMS cohort (5 cases) | Moderate-high; small cohort |
| [41448431](https://pubmed.ncbi.nlm.nih.gov/41448431/) | In vitro / model | **Competing** | ABCC9 GOF → Cantú | SUR2 GOF (reduced ATP sensitivity) → Cantú cardiovascular phenotype | Cantú syndrome | Moderate; opposite channel direction |
| [39031464](https://pubmed.ncbi.nlm.nih.gov/39031464/) | Human genetics | **Competing** | ABCC9 GOF (NBD1) → Cantú | SUR2B NBD1 GOF variant, multigenerational Cantú | Cantú syndrome | Moderate |
| gnomAD v2.1.1 (ENSG00000069431) | Computational / population genetics | **Qualifies** | Haploinsufficiency vs dominant-negative | LoF-tolerant (pLI~0, LOEUF 0.60); missense-constrained (mis_z 7.62) | Constraint landscape | High for constraint; mechanism inferred |
| ClinVar (VCV 8162, 222477, 856369) | Curation / database | **Qualifies / weakens** | Pathogenicity of founder alleles | A1513T = Pathogenic (no criteria) + Conflicting; 2nd allele Conflicting; 0 expert-panel ABCC9 variants | CMD1O founder alleles | High for curation status |
| gnomAD (A1513T) | Computational | **Qualifies / weakens** | Is A1513T a penetrant dominant allele? | Combined MAF ~5×10⁻⁵ (14 carriers); reclassified Conflicting | CMD1O founder allele | High |
| [20033705](https://pubmed.ncbi.nlm.nih.gov/20033705/) | Review | **Qualifies** (orientation) | KATP channelopathy spectrum incl. CMD1O; E23K risk | Places CMD1O among KATP channelopathies; E23K a remodeling risk factor | KATP channelopathies | Review-level; orientation only |

---

## Data and Tool Use

| Source | Accession / URI | Repository | Version / snapshot | Retrieval date | Access status | Query / filter | Resolved & relevant? |
|---|---|---|---|---|---|---|---|
| gnomAD constraint | ENSG00000069431 (ABCC9) | gnomAD GraphQL API | v2.1.1 | 2026-10-24 | **Accessed** | Gene constraint: pLI, oe_lof, LOEUF, mis_z, oe_mis | Yes — informs mechanism class |
| gnomAD variant | ABCC9 c.4537G>A / p.Ala1513Thr | gnomAD GraphQL API | v2.1.1 | 2026-10-24 | **Accessed** | Variant AC/AN, exome + genome, clinvar_variants join | Yes — tests founder allele penetrance |
| ClinVar | ABCC9 variants; VCV 8162, 222477, 856369 | NCBI E-utilities | live, 2026-10-24 | 2026-10-24 | **Accessed** | ABCC9 P/LP under "dilated cardiomyopathy" (n=205); review-status counts | Yes — tests founder-allele confidence |
| PubMed | 20 papers (see Evidence Base) | NCBI PubMed | live | iterations 1–5 | **Accessed** | KATP, ABCC9/SUR2A, CMD1O, DCM gene validity, Cantú, AIMS, calcineurin | Yes |
| ClinGen DCM gene validity | — (via PMID 33947203) | ClinGen (via publication) | as published 2021 | iteration 3 | **Cited via publication** | ABCC9 classification tier | Yes, accessed through the paper, not the live ClinGen API |

**Analyses attempted (input → method → output):**

1. **gnomAD constraint retrieval** — Input: ABCC9 Ensembl ID. Method: GraphQL query to gnomAD v2.1.1 constraint endpoint. Output: constraint metric table (F005). **Outcome: succeeded.**
2. **gnomAD variant frequency + ClinVar join for A1513T** — Input: c.4537G>A. Method: GraphQL variant query. Output: AC/AN per subset + ClinVar record IDs (F007). **Outcome: succeeded.**
3. **ClinVar review-status audit for ABCC9** — Input: ABCC9 gene + "dilated cardiomyopathy" condition. Method: NCBI E-utilities queries. Output: review-status counts (0 expert-panel), variant-type breakdown (F006). **Outcome: succeeded.**

**No patient-level, omics, or structural-biology (Phenix) analysis was run.** No cardiac transcriptomic/proteomic dataset or an ABCC9-allele cardiac model was identified or accessed; this is a genuine data absence (see Knowledge Gaps), not a silent fallback. All computational claims above rest on inspectable database queries; all mechanistic claims about the heart rest on the cited literature.

---

## Mechanistic Causal Chain

The hypothesis proposes the following chain. Annotations mark where the literature is strong, inferred, or missing.

```
[ C-terminal ABCC9 variant ]
          |  (STRONG in vitro: PMID 15034580 — recombinant)
          v
[ SUR2A catalytic ATP-hydrolytic cycle displaced ]
          |  (STRONG in vitro: PMID 15034580)
          v
[ Kir6.2 pore mis-gated / compromised metabolic decoding ]
          |  ===== MISSING EDGE: never shown for an ABCC9 allele in a heart =====
          v
[ Cardiomyocyte cannot match electrical/contractile work to energetic demand ]
          |  (INFERRED for ABCC9; demonstrated only via Kir6.2-KO: PMID 16782803)
          v
[ Ca2+ overload ]
          |  (STRONG in KATP-null heart: PMID 16782803 — pore-subunit KO, not ABCC9)
          v
[ Calcineurin-dependent maladaptive remodeling ]
          |  (STRONG in KATP-null heart: PMID 16782803; cyclosporine-sensitive)
          v
[ Dilated, arrhythmogenic ventricle (CMD1O) ]
          |  (INFERRED; gene-disease validity Limited: PMID 31983221, 33947203)
```

**Strong links:** variant → catalytic displacement → pore mis-gating (recombinant); and KATP-null → Ca²⁺ overload → calcineurin remodeling → heart failure (mouse pore-subunit KO).

**The decisive missing step** is the junction between the two strong segments: *no study has shown that an ABCC9 catalytic-domain allele mis-gates KATP in a cardiomyocyte and thereby produces the Ca²⁺/calcineurin remodeling phenotype in a heart (human or animal).* The two halves of the chain are demonstrated with different molecular lesions (conformational SUR2A missense vs. complete Kir6.2 deletion) in different systems (recombinant vs. mouse). The clinical endpoint (CMD1O) rests on a gene–disease relationship curated as Limited.

---

## Limitations and Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| **Untested gene→heart edge** | Core causal step | Whether an ABCC9 catalytic allele actually mis-gates KATP in a cardiomyocyte and drives remodeling | Literature search (PubMed, iterations 1–5); no ABCC9-allele cardiac model found | Knock-in mouse / iPSC-cardiomyocyte carrying a C-terminal ABCC9 allele with stress phenotyping |
| **Pore- vs regulatory-subunit discrepancy** | Mechanistic equivalence | PMID 16782803 uses Kir6.2 deletion, not an ABCC9 conformational mutant; effects may not transfer | Reviewed both papers | Side-by-side comparison of ABCC9-allele vs KCNJ11-KO hearts under identical stress |
| **LoF tolerated but LoF→AIMS, not DCM** | Mechanism class | Biallelic LoF causes neuromuscular syndrome, not DCM; haploinsufficiency tolerated in gnomAD | gnomAD constraint; AIMS literature (PMID 38217872, 42290677) | Functional classification of CMD1O alleles as dominant-negative vs LoF |
| **Founder allele penetrance** | Genetic premise | A1513T at ~5×10⁻⁵ MAF and reclassified Conflicting is too common/uncertain for a penetrant dominant cause | gnomAD + ClinVar (2026-10-24) | Segregation in multiplex families; case-control burden for ABCC9 missense in DCM |
| **No expert-panel ABCC9 classification** | Curation absence | Gene–disease validity never formally adjudicated at high tier | ClinVar review-status counts = 0 (2026-10-24); ClinGen DCM curation (PMID 33947203) placed ABCC9 below high evidence | ClinGen expert-panel re-curation of ABCC9–DCM |
| **No ABCC9-allele cardiac omics** | Data absence | No transcriptomic/proteomic evidence of calcineurin-pathway activation in an ABCC9-DCM heart | No relevant dataset identified in search | Cardiac RNA-seq/proteomics from ABCC9-allele model or patient myocardium |
| **Calcineurin step unproven for ABCC9** | Downstream edge | Cyclosporine-sensitivity shown only for Kir6.2-KO | PMID 16782803 reviewed | Calcineurin/NFAT readouts + cyclosporine rescue in an ABCC9-allele heart |

**Negative/absence searches (verifiable):**
- **ClinVar, 2026-10-24:** ABCC9 variants "reviewed by expert panel" or "practice guideline" = **0**. Founder alleles are 0-star legacy or Conflicting.
- **gnomAD v2.1.1, 2026-10-24:** ABCC9 is LoF-tolerant (pLI ~0), so haploinsufficiency is not favored.
- **PubMed, iterations 1–5:** No primary report of an ABCC9 catalytic-domain allele producing cardiomyopathy in an animal or human heart was found. Labeled as a checked absence, not an unverified assumption.

---

## Alternative Models

1. **Dominant-negative conformational mis-gating (refined version of the seed hypothesis).** *Parallel/refinement.* gnomAD constraint (LoF-tolerant, missense-intolerant; F005) suggests that if ABCC9 missense causes CMD1O it does so by a poison-subunit effect on the hetero-octameric channel, not haploinsufficiency. This is the most internally consistent version of the hypothesis but is itself unproven in a heart.

2. **ABCC9 is not a bona fide monogenic DCM gene (null model).** *Alternative.* Given Limited validity (F003), absent expert-panel classification (F006), and the founder allele's population presence and reclassification (F007), CMD1O may represent over-interpretation of rare variants of uncertain significance in a gene whose dominant disease association is actually Cantú (GOF) and whose recessive association is AIMS (LoF). This parsimoniously explains the allelic series (F004) without invoking a cardiac-specific gating lesion.

3. **Allele-class-specific pleiotropy.** *Upstream cause / competing framework.* The same gene produces Cantú (GOF), AIMS (biallelic LoF), and possibly CMD1O (dominant-negative missense). Under this model the determining variable is the biophysical direction of the variant's effect on channel open probability, and CMD1O occupies a narrow, specific niche — explaining why generic LoF produces AIMS rather than DCM.

4. **Modifier/risk-allele model rather than Mendelian cause.** *Downstream/complementary.* The Kir6.2 E23K polymorphism is a known risk factor for maladaptive cardiac remodeling (review-level, [PMID: 20033705](https://pubmed.ncbi.nlm.nih.gov/20033705/)). ABCC9 variants could act as susceptibility/remodeling modifiers that aggravate DCM triggered by other insults (hypertension, myocarditis), consistent with the ~5×10⁻⁵ carrier frequency of A1513T, rather than as deterministic monogenic causes.

5. **Classical sarcomeric/cytoskeletal DCM mechanisms.** *Competing, better-validated.* The robustly validated DCM genes (e.g., TTN, LMNA, and others in the definitive/strong tier; PMID 33947203) provide far better-established monogenic explanations for the dilated/arrhythmogenic phenotype; ABCC9 is not needed to explain most CMD cases.

---

## Discriminating Tests

| Test | Design | Stratification / biomarker | Model / sample | Perturbation | Expected result if hypothesis TRUE | Discriminates against |
|---|---|---|---|---|---|---|
| **ABCC9 catalytic-allele knock-in mouse** | Knock-in of a C-terminal ABCC9 missense (e.g., A1513T-equivalent); stress with pressure overload | Ca²⁺ transients, NFAT translocation, calcineurin activity | Mouse heart | Stress ± cyclosporine | Mis-gated cardiac KATP, Ca²⁺ overload, calcineurin activation, DCM; cyclosporine rescue | Closes the MISSING EDGE; vs null model (2) |
| **Patient iPSC-cardiomyocytes** | Isogenic correction of the ABCC9 allele | KATP current (pinacidil/ATP sensitivity), AP, contractile fatigue | Human iPSC-CM | Metabolic/energetic stress | Allele-specific KATP mis-gating + contractile/energetic failure corrected by gene editing | vs modifier model (4); establishes cell-autonomy |
| **Dominant-negative vs LoF classification** | Co-express mutant + WT SUR2A at defined ratios | KATP open probability, surface expression | Heterologous (CHO/HEK) + excised patch | Titrate mutant:WT | Dominant-negative suppression (poison subunit), not simple haploinsufficiency | Distinguishes refined model (1) from LoF/AIMS mechanism |
| **ClinGen expert-panel re-curation** | Formal gene–disease validity reassessment | Segregation, case-control burden | Curated human cohorts | — | Upgrade only if new segregation/burden evidence emerges | Resolves gene-validity gap; vs null model (2) |
| **Case-control burden of ABCC9 missense in DCM** | Rare missense burden vs gnomAD | Catalytic-domain missense specifically | Large DCM cohort | — | Enrichment of catalytic-domain missense in DCM cases | vs risk-allele model (4) |

The single most decisive, efficient experiment is the **ABCC9 catalytic-allele knock-in mouse (or isogenic iPSC-CM) with cyclosporine rescue**, because it simultaneously joins the two currently disconnected arms of the chain and tests the calcineurin dependence in the correct molecular context.

---

## Curation Leads (require curator verification)

**Candidate status / subtype restrictions:**
- Retain `status: EMERGING`. Do not promote to CANONICAL. Add explicit subtype restriction: the hypothesis, if valid, is restricted to **dominant-negative C-terminal/catalytic-domain ABCC9 missense alleles**, distinct from biallelic LoF (AIMS) and GOF (Cantú).
- Flag the founder allele **p.Ala1513Thr** as population-present (gnomAD combined MAF ~5×10⁻⁵) and ClinVar-Conflicting — candidate downgrade note on penetrance.

**Candidate evidence references with snippets to verify:**
- [PMID: 15034580](https://pubmed.ncbi.nlm.nih.gov/15034580/): *"Mutant SUR2A proteins showed aberrant redistribution of conformations in the intrinsic ATP hydrolytic cycle, translating into abnormal K(ATP) channel phenotypes with compromised metabolic signal decoding. Defective catalysis-mediated pore regulation is thus a mechanism for channel dysfunction and susceptibility to dilated cardiomyopathy."* (molecular arm)
- [PMID: 16782803](https://pubmed.ncbi.nlm.nih.gov/16782803/): *"Defective decoding of hypertension-induced metabolic distress signals in the K(ATP) channel knockout set in motion pathological calcium overload and aggravated cardiac remodeling through a calcium/calcineurin-dependent cyclosporine-sensitive pathway."* (myocardial arm — note: Kir6.2-KO, not ABCC9)
- [PMID: 31983221](https://pubmed.ncbi.nlm.nih.gov/31983221/): *"...have limited value in diagnostic testing in DCM at present."* (gene-validity caveat)
- [PMID: 38217872](https://pubmed.ncbi.nlm.nih.gov/38217872/): *"All variants are predicted to result in severe truncations or in-frame deletions within SUR2, leading to the generation of non-functional SUR2-dependent KATP channels."* (competing LoF→AIMS)

**Candidate pathophysiology nodes/edges:**
- Node: SUR2A catalytic ATP-hydrolytic cycle; Edge: catalytic displacement → Kir6.2 mis-gating (in vitro, verified).
- Edge (flag as UNCONFIRMED): ABCC9 catalytic allele → cardiomyocyte KATP mis-gating → Ca²⁺ overload (inferred; no direct cardiac evidence).
- Edge: KATP loss → Ca²⁺/calcineurin remodeling (verified only in Kir6.2-KO; annotate subunit discrepancy).

**Candidate ontology terms:** ATP-sensitive potassium channel complex / KATP channel activity (GO:0015272 inward rectifier K⁺ channel; GO:0008282); calcineurin-NFAT signaling; cardiomyocyte (CL:0000746); cardiac muscle contraction; cellular response to metabolic/energetic stress.

**Candidate `knowledge_gaps` prompts:** (1) No ABCC9-allele cardiac model demonstrates the gene→heart edge. (2) ABCC9 is LoF-tolerant yet founder alleles assumed dominant — mechanism class unresolved. (3) No expert-panel ABCC9–DCM classification exists (ClinVar counts = 0 as of 2026-10-24). (4) Calcineurin dependence shown only for pore-subunit KO.

**Provider artifact bundle:** A checksummed artifact bundle (gnomAD/ClinVar query logs, constraint and variant-frequency derived tables, MANIFEST) was produced in iterations 4–5 beneath `kb/hypotheses/Dilated_Cardiomyopathy_1O/katp_metabolic_gating_failure/openscientist_artifacts`. No patient-level, controlled-access, or large raw downloads are bundled; external identifiers (gnomAD v2.1.1 ENSG00000069431; ClinVar VCV 8162 / 222477 / 856369) are recorded instead. No structural-biology/Phenix artifacts were produced because no structural analysis was run.

---

## Evidence Base (literature orientation)

- **[PMID: 15034580](https://pubmed.ncbi.nlm.nih.gov/15034580/)** — *ABCC9 mutations identified in human dilated cardiomyopathy disrupt catalytic KATP channel gating.* Primary molecular-arm support; recombinant.
- **[PMID: 16782803](https://pubmed.ncbi.nlm.nih.gov/16782803/)** — *KCNJ11 gene knockout of the Kir6.2 KATP channel causes maladaptive remodeling and heart failure in hypertension.* Primary myocardial-arm support; pore-subunit KO.
- **[PMID: 31983221](https://pubmed.ncbi.nlm.nih.gov/31983221/)** — *Reevaluating the Genetic Contribution of Monogenic Dilated Cardiomyopathy.* Defines Limited validity constraint.
- **[PMID: 33947203](https://pubmed.ncbi.nlm.nih.gov/33947203/)** — *Evidence-Based Assessment of Genes in Dilated Cardiomyopathy (ClinGen).* ABCC9 below high evidence.
- **[PMID: 38217872](https://pubmed.ncbi.nlm.nih.gov/38217872/)** / **[PMID: 42290677](https://pubmed.ncbi.nlm.nih.gov/42290677/)** — Biallelic LoF → AIMS (competing allelic series).
- **[PMID: 41448431](https://pubmed.ncbi.nlm.nih.gov/41448431/)** / **[PMID: 39031464](https://pubmed.ncbi.nlm.nih.gov/39031464/)** — ABCC9 GOF → Cantú syndrome (competing allelic direction).
- **[PMID: 20033705](https://pubmed.ncbi.nlm.nih.gov/20033705/)** — Review: human KATP channelopathies; places CMD1O and the E23K risk allele in context (review-level orientation).
- **[PMID: 12565699](https://pubmed.ncbi.nlm.nih.gov/12565699/)** / **[PMID: 12939542](https://pubmed.ncbi.nlm.nih.gov/12939542/)** — Reviews on KATP subunit physiology and knockout phenotypes (orientation).

---

## Proposed Follow-up Actions

1. **Build the missing cardiac model** (knock-in mouse or isogenic iPSC-cardiomyocyte with a C-terminal ABCC9 allele) and test KATP mis-gating → Ca²⁺ overload → calcineurin activation under stress, with cyclosporine rescue — the single decisive experiment.
2. **Classify CMD1O alleles biophysically** as dominant-negative vs LoF via WT:mutant co-expression, reconciling the gnomAD constraint signal with mechanism.
3. **Quantify ABCC9 missense burden** (catalytic domain) in a large DCM case-control cohort; obtain segregation data for A1513T.
4. **Request ClinGen expert-panel re-curation** of ABCC9–DCM and ClinVar reclassification of the founder alleles.
5. **Seek/curate ABCC9-DCM cardiac omics** to test calcineurin-pathway activation; if none exists, record as a formal data absence.

---

*Report generated 2026-10-24. Verdict: PARTIALLY SUPPORTED; keep EMERGING. The hypothesis is mechanistically coherent with each arm independently supported, but the gene→heart causal edge is untested and the underlying ABCC9–DCM genetics are Limited and partly contradicted.*
