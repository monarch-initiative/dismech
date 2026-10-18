---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T01:14:38.789026'
end_time: '2026-10-16T01:33:01.817800'
duration_seconds: 1103.03
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: MYH7-Related Skeletal Myopathy
  category: Mendelian
  hypothesis_group_id: myosin_inhibitor_rescue
  hypothesis_label: Myosin inhibitors that stabilize the relaxed state can improve
    skeletal muscle function in MYH7 rod myopathy
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: myosin_inhibitor_rescue\nhypothesis_label:\
    \ Myosin inhibitors that stabilize the relaxed state can improve skeletal muscle\
    \ function\n  in MYH7 rod myopathy\nstatus: EMERGING\ndescription: If the energetic\
    \ model holds, small molecules that shift heads back toward the relaxed state\n\
    \  should help. MYK-581 improved running capacity in R1500P mice and normalized\
    \ the DRX fraction in patient\n  myofibrils. Whether the approved cardiac myosin\
    \ inhibitors mavacamten and aficamten act on slow skeletal\n  muscle at tolerable\
    \ doses, and whether they help myosin storage alleles, is untested.\nevidence:\n\
    - reference: PMID:38690726\n  reference_title: A Laing distal myopathy-associated\
    \ proline substitution in the \u03B2-myosin rod perturbs\n    myosin cross-bridging\
    \ activity.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet:\
    \ oral administration of MYK-581, a small molecule that decreases the population\
    \ of heads in\n    the DRX configuration, significantly improved the limited running\
    \ capacity of the R1500P-transgenic\n    mice and corrected the increased DRX\
    \ state of the myofibrils from patients\n  explanation: Preclinical rescue motivating\
    \ the hypothesis."
  artifact_dir: kb/hypotheses/MYH7-Related_Skeletal_Myopathy/myosin_inhibitor_rescue/openscientist_artifacts
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
citation_count: 17
term_validation:
  total_terms: 11
  verified: 10
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0008050
    reported_labels:
    - target
    ontology_label: MYH7-related skeletal myopathy
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
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
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_environment.json
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_environment.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist environment
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_logs_clinicaltrials_gov_search.json
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_logs_clinicaltrials_gov_search.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist clinicaltrials gov search
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_logs_monarch_gencc_preflight.json
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_logs_monarch_gencc_preflight.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist monarch gencc preflight
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_tables_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_tables_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** MYH7-Related Skeletal Myopathy
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** myosin_inhibitor_rescue
- **Hypothesis Label:** Myosin inhibitors that stabilize the relaxed state can improve skeletal muscle function in MYH7 rod myopathy
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: myosin_inhibitor_rescue
hypothesis_label: Myosin inhibitors that stabilize the relaxed state can improve skeletal muscle function
  in MYH7 rod myopathy
status: EMERGING
description: If the energetic model holds, small molecules that shift heads back toward the relaxed state
  should help. MYK-581 improved running capacity in R1500P mice and normalized the DRX fraction in patient
  myofibrils. Whether the approved cardiac myosin inhibitors mavacamten and aficamten act on slow skeletal
  muscle at tolerable doses, and whether they help myosin storage alleles, is untested.
evidence:
- reference: PMID:38690726
  reference_title: A Laing distal myopathy-associated proline substitution in the β-myosin rod perturbs
    myosin cross-bridging activity.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: oral administration of MYK-581, a small molecule that decreases the population of heads in
    the DRX configuration, significantly improved the limited running capacity of the R1500P-transgenic
    mice and corrected the increased DRX state of the myofibrils from patients
  explanation: Preclinical rescue motivating the hypothesis.
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
result beneath `kb/hypotheses/MYH7-Related_Skeletal_Myopathy/myosin_inhibitor_rescue/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Final Report

## Hypothesis under evaluation
**Disease:** MYH7-Related Skeletal Myopathy (Mendelian; MONDO:0008050)
**Hypothesis ID:** `myosin_inhibitor_rescue`
**Hypothesis label:** *Myosin inhibitors that stabilize the relaxed state can improve skeletal muscle function in MYH7 rod myopathy*
**KB status (prior):** EMERGING
**Search date:** 2026-10-16

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (Emerging), subtype-restricted.**

The seed hypothesis rests on a single, coherent and mechanistically well-constructed preclinical/ex-vivo study and on a broader, generalizable energetic rationale, but it has **no human interventional evidence**, carries a **documented iatrogenic skeletal-myopathy safety signal**, and **does not explain the myosin-storage (aggregation) branch** of the MYH7 spectrum. The balance of evidence supports a *narrow, conditional* endorsement rather than a general one.

The strongest direct support comes from Buvoli et al. 2024 ([PMID:38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/)): in the first mouse model of MYH7 Laing distal myopathy (the R1500P proline substitution in the β-myosin coiled-coil **rod**), the mutation — despite not being in the motor domain — shifted myosin heads toward the **disordered-relaxed (DRX)** state, producing hypercontractility, faster actin–myosin detachment, and increased ATP consumption. Oral **MYK-581**, a DRX-depleting myosin modulator, significantly improved the limited running capacity of R1500P-transgenic mice and corrected the elevated DRX fraction in myofibrils isolated from patients. This is a direct demonstration of both functional rescue in vivo and correction of the candidate molecular biomarker in human tissue — a strong motivating result.

The hypothesis generalizes well at the level of *molecular rationale*: destabilization of the super-relaxed (SRX) state with resting ATP over-consumption is now documented across multiple genetic skeletal myopathies (nebulin nemaline myopathy, XLMTM/MTM1, MYH7/MYH2 light-meromyosin mutations), and myosin ATPase inhibition reverses the ATP over-consumption in vitro and partially restores the myofiber proteome in XLMTM mice and in heart-failure human skeletal myofibres. However, translation is **inconsistent in vivo**: four-week mavacamten failed to normalize the energy proteome in nebulin-KO mice, and in MYH7/MYH2 LMM mutants a reduced SRX did not alter contractility — indicating the energetic defect does not always drive a contractile phenotype. There are **zero registered clinical trials** of myosin inhibitors in MYH7 or skeletal myopathy (ClinicalTrials.gov v2, checked 2026-10-16), the approved cardiac inhibitors engage skeletal myosin but have produced generalized skeletal myopathy and myalgia in patients, and the three relevant inhibitors (MYK-581, mavacamten, aficamten) are **not mechanistically equivalent**. Finally, the **myosin storage myopathy (MSM)** alleles are driven by a *competing* mechanism — coiled-coil destabilization and protein aggregation — against which a relaxed-state modulator has no obvious target engagement.

**Bottom line:** the hypothesis is best scoped to the **DRX-hypercontractile rod/Laing distal subtype**, where it is promising but preclinical-only. It should be labeled *speculative-to-unknown* for myosin-storage alleles and *unresolved* for human efficacy and tolerability.

---

## Key Findings

### F001 — Direct preclinical rescue in the R1500P Laing model (strongest supporting evidence)

Buvoli et al. 2024 ([PMID:38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/)) generated the first mouse model of MYH7 Laing distal myopathy, carrying R1500P — a proline substitution in the β-myosin coiled-coil **rod**, outside the catalytic motor domain. The central and non-obvious finding is that a *structural rod* mutation nonetheless produces a *functional/energetic* defect: "a conformational shift of the myosin heads toward the more reactive disordered relaxed (DRX) state, causing hypercontractility and greater ATP consumption." Patient biopsies independently showed increased sarcomeric DRX content, establishing the DRX fraction as a candidate human biomarker.

The therapeutic result is the linchpin of the seed hypothesis: "oral administration of MYK-581, a small molecule that decreases the population of heads in the DRX configuration, significantly improved the limited running capacity of the R1500P-transgenic mice and corrected the increased DRX state of the myofibrils from patients." This couples an **in vivo functional endpoint** (running capacity) with **correction of the molecular biomarker in human tissue** — the single most direct piece of evidence available. Its limitations: one allele, one model, a transgenic (not knock-in) system, a surrogate behavioral endpoint, and a tool compound (MYK-581) rather than an approved drug.

### F002 — Myosin inhibitors engage skeletal myosin but carry a skeletal-myopathy safety signal

Target engagement in skeletal muscle is confirmed, which is necessary for the hypothesis to be actionable with approved drugs. Using small-angle X-ray diffraction, Kuehn/Hessel and colleagues showed mavacamten "facilitates myosin head ON-to-OFF transitions" and "reduced the proportion of ON myosin heads" in relaxed skeletal muscle ([PMID:39677804](https://pubmed.ncbi.nlm.nih.gov/39677804/)), with effects paralleling cardiac muscle. Critically, the same group states mavacamten "is not completely specific to cardiac myosin and can also affect skeletal muscle myosin … Indeed, emerging clinical reports indicate mavacamten-induced generalized skeletal myopathy in elderly patients" ([PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/)). A HOCM case report described myalgia without CK elevation under mavacamten ([PMID:41000531](https://pubmed.ncbi.nlm.nih.gov/41000531/)). This is a **double-edged finding**: it validates the pharmacologic premise (skeletal engagement) while flagging that the "tolerable dose on slow skeletal muscle" assumption embedded in the seed hypothesis is not safe to assume — the same engagement that could help a hypercontractile allele could **weaken otherwise-healthy slow muscle**.

### F003 — The energetic DRX/SRX model is shared across myopathies, but in vivo rescue is inconsistent (qualifier/partial refutation)

The relaxed-state energetic model is not idiosyncratic to MYH7: SRX destabilization with increased resting ATP consumption is documented in NEB nemaline myopathy ([PMID:36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/)), MYH7/MYH2 light-meromyosin mutations ([PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)), and XLMTM/MTM1 ([PMID:41196692](https://pubmed.ncbi.nlm.nih.gov/41196692/)). Myosin ATPase inhibition reverses ATP over-consumption in vitro and *partially* restores the myofiber proteome in XLMTM mice ([PMID:41196692](https://pubmed.ncbi.nlm.nih.gov/41196692/)) and in HFrEF human skeletal myofibres ([PMID:42089145](https://pubmed.ncbi.nlm.nih.gov/42089145/)).

But two results qualify the hypothesis materially. First, a **failed in vivo replication of the energetic-rescue concept**: in conditional nebulin-KO mice, "short-term Mavacamten treatment is not sufficient to properly counterbalance the metabolically dysregulated proteome of cNeb KO mice" ([PMID:39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/)). Second, a **dissociation between the molecular and contractile phenotype**: for MYH7/MYH2 LMM mutations, the "myosin super-relaxed state was decreased in vivo" yet "myofiber contractility was not affected" ([PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)). Together these show that (a) SRX/DRX changes do not always translate to a contractile deficit, and (b) correcting the energetic state pharmacologically does not reliably normalize downstream biology in vivo — a direct caution against assuming MYK-581's success will generalize.

### F004 — Myosin storage myopathy alleles act by coiled-coil destabilization and aggregation — a competing mechanism

The MYH7 spectrum contains a branch the seed hypothesis does not address. MSM is caused by MYH7 missense mutations concentrated in the rod/tail heptad repeat. In transgenic *Drosophila*, MSM mutations (L1793P, R1845W, E1883K) "frequently disrupt the tail's stabilizing heptad repeat motif," "significantly reduced [thick filament lengths] in all mutants," and provoke myofibrillar inclusions/aggregates ([PMID:39485824](https://pubmed.ncbi.nlm.nih.gov/39485824/)). A machine-learning/structural analysis found pathogenic variants "cluster in locally unwound regions of the coiled-coil dimer, suggesting that changes in these strained sites may promote dimer destabilization and aggregation" ([PMID:41780808](https://pubmed.ncbi.nlm.nih.gov/41780808/)). Recessive MYH7 cases show abnormal mutant myosin aggregation in COS-7 cells ([PMID:31130376](https://pubmed.ncbi.nlm.nih.gov/31130376/)), and the classic review frames MSM as a protein-aggregate myopathy with subsarcolemmal myosin accumulation ([PMID:22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/)). Because the primary lesion here is **thick-filament assembly/length and aggregation** — not DRX/SRX head energetics — a relaxed-state modulator has no clear mechanistic handle on MSM. This is the single most important scoping limitation.

### F005 — No registered clinical trial of myosin inhibitors in MYH7/skeletal myopathy (source-level absence, verified)

ClinicalTrials.gov API v2 was queried on 2026-10-16 with: `mavacamten skeletal myopathy` (0), `aficamten skeletal muscle` (0), `MYH7 myopathy myosin inhibitor` (0), `MYK-581` (0), `aficamten nonobstructive` (0), `myosin storage myopathy` (1 hit = NCT05099107, a salbutamol congenital-myopathy study, **not** a myosin inhibitor), and `Laing distal myopathy` (14 hits, all keyword-match artifacts unrelated to MYH7 or myosin inhibitors). The search log is saved in the artifact bundle (`logs/clinicaltrials_gov_search.json`). This confirms the hypothesis is **preclinical/ex-vivo only** at the human-interventional level as of the search date.

### F006 — The three relaxed-state inhibitors are mechanistically non-equivalent

MYK-581 and mavacamten (aminouracil class) stabilize both the structural OFF/interacting-heads motif and the super-relaxed state; mavacamten "facilitates myosin head ON-to-OFF transitions" and structurally sequesters heads along the thick filament ([PMID:39677804](https://pubmed.ncbi.nlm.nih.gov/39677804/), [PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/)). Aficamten (CK-274) is different: "In contrast to Mavacamten, Aficamten does not structurally sequester myosin heads along the thick filament. Aficamten inhibits ATPase activity by shifting myosin heads from higher to slower ATPase state, with the emergence of a super slow biochemical nucleotide turnover state" ([PMID:40463178](https://pubmed.ncbi.nlm.nih.gov/40463178/)). This matters for translation: a DRX-depleting / OFF-state-stabilizing mechanism (MYK-581, mavacamten) is the one shown to help R1500P, whereas aficamten achieves comparable contractile inhibition without OFF-state sequestration. The seed hypothesis lumps the three drugs together; the mechanisms predict they may **not** be interchangeable for a DRX-driven allele.

### F007 — MYH7 is a multi-entity Mendelian gene; the hypothesis maps to the DRX/distal subtype (ontology confirmed)

Monarch Initiative API v3 (HGNC:7577, 284 associations, queried 2026-10-16) returned gene–disease edges to MYH7-related skeletal myopathy (MONDO:0008050, the target), congenital myopathy 7A / autosomal-dominant myosin storage (MONDO:0008409), autosomal-recessive myosin storage myopathy (MONDO:0009708), classic multiminicore myopathy (MONDO:0017939), plus cardiac entities (DCM MONDO:0700335, LVNC MONDO:0018901). Associated skeletal HPO phenotypes include scapuloperoneal weakness (HP:0003704), toe extensor amyotrophy (HP:0011916), type 1 muscle fiber predominance (HP:0003803), and neck muscle weakness (HP:0000467). The **GenCC JSON API returned 404** (no programmatic access) — gene-disease validity classification remains unverified via API. This heterogeneity is exactly why the hypothesis must be subtype-scoped.

### F008 — Consolidated verdict

Across 7 recorded findings and 13 curated references: **SUPPORT** = [PMID:38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/). **Analog support** = [PMID:36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/), [PMID:41196692](https://pubmed.ncbi.nlm.nih.gov/41196692/), [PMID:42089145](https://pubmed.ncbi.nlm.nih.gov/42089145/), [PMID:39677804](https://pubmed.ncbi.nlm.nih.gov/39677804/). **Qualify/refute** = [PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/), [PMID:39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/), [PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/)/[PMID:41000531](https://pubmed.ncbi.nlm.nih.gov/41000531/), [PMID:40463178](https://pubmed.ncbi.nlm.nih.gov/40463178/). **Competing** = [PMID:39485824](https://pubmed.ncbi.nlm.nih.gov/39485824/), [PMID:41780808](https://pubmed.ncbi.nlm.nih.gov/41780808/), [PMID:31130376](https://pubmed.ncbi.nlm.nih.gov/31130376/). Source checks: ClinicalTrials.gov v2 = 0 relevant trials; Monarch v3 confirmed the MONDO map; GenCC API 404 (unverified).

---

## Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/) | Model organism + human ex vivo | **Supports** | DRX-depleting inhibitor rescues function in a rod mutant | MYK-581 improved running capacity in R1500P mice and corrected elevated DRX in patient myofibrils | Laing distal myopathy (R1500P rod) | High for this allele; single study, transgenic model, surrogate endpoint, tool compound |
| [PMID:39677804](https://pubmed.ncbi.nlm.nih.gov/39677804/) | In vitro (X-ray diffraction) | Qualifies/supports | Mavacamten shifts skeletal myosin ON→OFF | Reduced ON-head proportion in relaxed skeletal muscle; did not eliminate length-dependent activation | Skeletal (mouse) | High for engagement; not an MYH7-disease model |
| [PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/) | In vitro + clinical note | **Qualifies/refutes** | Cardiac inhibitor is skeletal-active and safe | Confirms skeletal engagement; flags mavacamten-induced generalized skeletal myopathy | Skeletal (safety) | High; safety signal from emerging reports |
| [PMID:41000531](https://pubmed.ncbi.nlm.nih.gov/41000531/) | Human clinical (case report) | Qualifies | Extracardiac/skeletal effects of mavacamten | Myalgia without CK elevation under mavacamten | HOCM patient | Low (n=1); hypothesis-generating |
| [PMID:36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/) | Human + model organism | Analog support | SRX loss → resting ATP over-consumption; drug rationale | SRX destabilized in NEB-NM; metabolic proteome remodeled | NEB nemaline myopathy | Moderate; different gene |
| [PMID:41196692](https://pubmed.ncbi.nlm.nih.gov/41196692/) | Human + canine/mouse | Analog support | Myosin ATPase inhibition rescues proteome in vivo | Mavacamten partially restored myofiber proteome in XLMTM mice | XLMTM/MTM1 | Moderate; partial rescue, different gene |
| [PMID:42089145](https://pubmed.ncbi.nlm.nih.gov/42089145/) | Human ex vivo | Analog support | Inhibitor reverses skeletal ATP over-consumption | Dose-dependent reduction of myosin ATP consumption in HFrEF myofibres | HFrEF skeletal muscle | Moderate; ex vivo, non-MYH7 |
| [PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) | Model organism / in vivo | **Qualifies** | SRX change necessarily alters contractility | SRX decreased in vivo but myofiber contractility unaffected | MYH7/MYH2 LMM mutations | Moderate; direct relevance to MYH7 rod alleles |
| [PMID:39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/) | Model organism / in vivo | **Refutes (partial)** | Short-term inhibitor normalizes energy proteome in vivo | 4-wk mavacamten did NOT counterbalance dysregulated proteome | Nebulin-KO mice | Moderate; different gene, short duration |
| [PMID:40463178](https://pubmed.ncbi.nlm.nih.gov/40463178/) | In vitro (single-molecule + mechanics) | Qualifies | The three inhibitors are interchangeable | Aficamten reduces force without OFF-state sequestration — distinct MoA | Cardiac myosin | High; predicts non-equivalence |
| [PMID:39485824](https://pubmed.ncbi.nlm.nih.gov/39485824/) | Model organism (Drosophila) + human filament | **Competing** | MSM driven by DRX energetics | MSM mutations disrupt tail heptad repeat; shorten thick filaments; cause aggregates | Myosin storage myopathy | High; defines competing mechanism |
| [PMID:41780808](https://pubmed.ncbi.nlm.nih.gov/41780808/) | Computational / structural | **Competing** | MSM driven by head energetics | Variants cluster in unwound coiled-coil regions → dimer destabilization/aggregation | MSM / rod variants | Moderate–high; in silico |
| [PMID:31130376](https://pubmed.ncbi.nlm.nih.gov/31130376/) | Human + in vitro | Competing | Recessive MYH7 mechanism | Recessive MYH7 variants → abnormal myosin aggregation in COS-7 | Recessive MYH7 myopathy | Moderate; rare cases |
| [PMID:22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) | Review | Competing (review-level) | Classification of myosinopathies | Frames MSM/Laing as protein-aggregate + LMM-assembly disorders | MYH7 myosinopathies | Orientation only |

---

## Mechanistic Causal Chain

The hypothesis implies the following chain. Annotations mark where literature is **strong**, **inferred**, or a **missing step**.

```
MYH7 rod/LMM mutation (e.g., R1500P)
        │  [STRONG: PMID:38690726]
        ▼
Perturbed coiled-coil / head sequestration
        │  [STRONG for R1500P; genotype-specific]
        ▼
Shift of heads from SRX/OFF → DRX/ON  (↑ reactive heads)
        │  [STRONG molecular: 38690726, 36528760, 37788100, 41196692]
        ▼
Hypercontractility + ↑ resting ATP consumption (energetic burden)
        │  [INFERRED → CLINICAL: the ATP-burden → weakness/exercise-
        │   intolerance link is NOT directly established in MYH7 patients;
        │   37788100 shows SRX loss WITHOUT contractile deficit = MISSING STEP]
        ▼
Skeletal muscle weakness / reduced exercise capacity (clinical)
        │
        ▼   therapeutic arm
Myosin inhibitor (DRX-depleting / OFF-stabilizing) → restore SRX/OFF
        │  [STRONG preclinical for MYK-581 in R1500P: 38690726]
        │  [INCONSISTENT in vivo: 39216086 failure; 37788100 no contractile change]
        │  [SAFETY LIABILITY: 41144950, 41000531 — drug can itself cause myopathy]
        ▼
Improved running capacity / normalized DRX (preclinical endpoint)
        │  [MISSING: human functional endpoint — 0 trials, F005]
```

**Where the literature is strong:** the upstream genotype→DRX-shift→energetic-burden molecular links, and the MYK-581 rescue in the single R1500P model.

**Where links are inferred:** the energetic-burden→clinical-weakness step in MYH7 patients; the generalization from R1500P to other rod/Laing alleles; the extrapolation from MYK-581 to approved drugs.

**Missing causal steps:** (1) a demonstrated ATP-burden→weakness causal edge in MYH7 muscle; (2) any human functional endpoint; (3) a tolerability window separating therapeutic inhibition of the mutant from harmful inhibition of healthy slow skeletal myosin; (4) any mechanistic bridge from relaxed-state modulation to the **aggregation** pathology of MSM alleles (there is none — it is a parallel mechanism).

---

## Evidence Base (how each pillar supports or challenges the hypothesis)

- **Primary support:** [PMID:38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/) is the only study that tests the actual intervention in the actual disease context (albeit one allele). It supplies both an in vivo functional endpoint and correction of a human-tissue biomarker.
- **Mechanistic plausibility / analog support:** [PMID:36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/), [PMID:41196692](https://pubmed.ncbi.nlm.nih.gov/41196692/), [PMID:42089145](https://pubmed.ncbi.nlm.nih.gov/42089145/), and [PMID:39677804](https://pubmed.ncbi.nlm.nih.gov/39677804/) show the SRX/energetic framework and skeletal target engagement are real and reversible — but in *other* genes/contexts, so they support plausibility rather than MYH7-specific efficacy.
- **Challenges / qualifiers:** [PMID:39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/) (in vivo failure), [PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) (SRX loss without contractile deficit), [PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/) + [PMID:41000531](https://pubmed.ncbi.nlm.nih.gov/41000531/) (iatrogenic skeletal myopathy), and [PMID:40463178](https://pubmed.ncbi.nlm.nih.gov/40463178/) (inhibitor non-equivalence) collectively constrain the hypothesis to a conditional claim.
- **Competing mechanism:** [PMID:39485824](https://pubmed.ncbi.nlm.nih.gov/39485824/), [PMID:41780808](https://pubmed.ncbi.nlm.nih.gov/41780808/), [PMID:31130376](https://pubmed.ncbi.nlm.nih.gov/31130376/) establish the aggregation/assembly model for MSM — a branch the hypothesis cannot address.
- **Review orientation (clearly labeled):** [PMID:22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) and HCM reviews ([PMID:36225299](https://pubmed.ncbi.nlm.nih.gov/36225299/)) frame hypercontractility and the myosin-inhibitor paradigm but are not MYH7-skeletal primary evidence.

---

## Data and Tool Use

| Source | Accession / URI | Access status | Query / filters | Resolved & relevant? |
|---|---|---|---|---|
| PubMed/MEDLINE | — | **Accessed** | ~36 papers across MYH7 myopathy, DRX/SRX, mavacamten/aficamten/MYK-581, myosin storage myopathy | Yes — primary evidence base |
| ClinicalTrials.gov | API v2, queried 2026-10-16 | **Accessed, negative (verified)** | 7 queries (see F005); 0 relevant interventional trials | Yes; log saved `logs/clinicaltrials_gov_search.json` |
| Monarch Initiative | API v3, HGNC:7577, queried 2026-10-16 | **Accessed** | 284 gene associations; `gene_associated_with_condition` edges | Yes — confirmed MONDO disease map |
| GenCC | JSON API | **Could not be verified (404)** | Attempted programmatic gene–disease validity query | No API access; classification **unverified** |

**Analysis inventory (input → method → outcome):**

1. **Literature synthesis** — Input: PubMed abstracts; Method: manual curation of support/refute/qualify/competing stance per citation; Outcome: **succeeded** (evidence matrix above). Limitation: abstract-level only for some papers; no full-text meta-analysis.
2. **ClinicalTrials.gov negative search** — Input: API v2; Method: 7 keyword queries; Outcome: **succeeded (negative result, verified)**; log artifact saved.
3. **Monarch ontology mapping** — Input: API v3 HGNC:7577; Method: edge enumeration; Outcome: **succeeded**.
4. **GenCC gene–disease validity** — Input: GenCC JSON API; Method: HTTP GET; Outcome: **failed (404)**; no silent fallback — classification explicitly left **unverified**.

No patient-level omics, structural refinement, or computational docking was performed. **No new wet-lab or in-silico perturbation analysis was run**; all mechanistic claims derive from published studies, not new computation. This is stated explicitly so that no proposed analysis is mis-reported as performed.

---

## Limitations and Knowledge Gaps

1. **No human interventional evidence (verified absence).** ClinicalTrials.gov v2 (2026-10-16) returned 0 relevant trials. *Resolution:* a first-in-disease trial or compassionate-use series with a muscle functional endpoint.
2. **Single-allele, single-model support.** Only R1500P has been tested; generalization to other rod/Laing and LMM alleles is inferred. *Resolution:* knock-in models of additional alleles (e.g., K1729del-type Laing variants) tested with MYK-581.
3. **Unconfirmed ATP-burden → weakness causal edge.** [PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) shows SRX loss without contractile deficit; the downstream clinical consequence of the energetic burden in MYH7 muscle is not directly demonstrated. *Resolution:* longitudinal energetics-to-function studies in patient-derived myofibers/iPSC myotubes.
4. **Inconsistent in vivo rescue.** [PMID:39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/) is a failed in vivo replication in a related model. *Resolution:* dose/duration-controlled in vivo studies in MYH7 knock-in mice.
5. **Safety / tolerability unknown.** Mavacamten causes iatrogenic skeletal myopathy/myalgia ([PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/), [PMID:41000531](https://pubmed.ncbi.nlm.nih.gov/41000531/)); the therapeutic window on slow skeletal muscle is uncharacterized. *Resolution:* dose-ranging tolerability with CK, muscle MRI, and strength endpoints.
6. **Inhibitor non-equivalence.** [PMID:40463178](https://pubmed.ncbi.nlm.nih.gov/40463178/) shows aficamten ≠ mavacamten mechanistically; "myosin inhibitors" cannot be treated as one class. *Resolution:* head-to-head ex vivo comparison on MYH7-mutant myofibrils.
7. **Myosin storage alleles unexplained.** MSM is an aggregation/assembly disorder ([PMID:39485824](https://pubmed.ncbi.nlm.nih.gov/39485824/), [PMID:41780808](https://pubmed.ncbi.nlm.nih.gov/41780808/)); relaxed-state modulators have no obvious target. *Resolution:* test whether DRX correction has any effect on aggregate load in MSM models (expected null).
8. **GenCC classification unverified.** API returned 404; gene–disease validity not programmatically confirmed. *Resolution:* manual GenCC/ClinGen lookup by a curator.

A negative-search caveat: the ClinicalTrials.gov absence is documented with database/version (API v2), the seven exact queries, and search date (2026-10-16), so it is reported as a **verified absence**. The GenCC absence is labeled **unverified** because the API did not resolve.

---

## Alternative / Competing Models

| Model | Relationship to seed hypothesis | Core claim | Key support |
|---|---|---|---|
| **Coiled-coil destabilization / aggregation (MSM)** | **Competing** (for storage alleles) | Rod/tail heptad mutations destabilize the coiled-coil, shorten thick filaments, and cause subsarcolemmal myosin aggregates | [PMID:39485824](https://pubmed.ncbi.nlm.nih.gov/39485824/), [PMID:41780808](https://pubmed.ncbi.nlm.nih.gov/41780808/), [PMID:31130376](https://pubmed.ncbi.nlm.nih.gov/31130376/), [PMID:22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) |
| **Thick-filament assembly / LMM dysfunction** | **Upstream cause** (could drive the DRX shift) | Impaired light-meromyosin assembly alters filament structure, which may be the real primary lesion | [PMID:22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/), [PMID:34053846](https://pubmed.ncbi.nlm.nih.gov/34053846/) |
| **Energetic/metabolic remodeling** | **Downstream consequence** (shared) | SRX loss remodels the metabolic proteome; weakness is partly a metabolic phenotype | [PMID:36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/), [PMID:42089145](https://pubmed.ncbi.nlm.nih.gov/42089145/) |
| **Protein-quality-control / degradation failure** | **Parallel mechanism** | Defective turnover of misfolded myosin contributes to aggregate myopathy | [PMID:22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) |
| **Fiber-type disproportion / developmental** | **Parallel / stage-specific** | Some MYH7 alleles present as congenital fiber-type disproportion before storage features appear | [PMID:21288719](https://pubmed.ncbi.nlm.nih.gov/21288719/) |

The seed hypothesis is the leading explanation **only for the DRX-hypercontractile rod/Laing subtype**. For storage alleles, the aggregation model is more parsimonious and is directly supported.

---

## Discriminating Tests

1. **Allele panel ex vivo myofibril assay.** Sample: patient- or knock-in-derived myofibrils spanning Laing/rod (R1500P-type), LMM, and MSM alleles. Perturbation: MYK-581 vs mavacamten vs aficamten. Readout: DRX fraction (Mant-ATP chase), resting ATP consumption, force/Ca²⁺ sensitivity, aggregate load. *Expected:* DRX correction and functional gain in rod alleles; **no aggregate reduction** in MSM alleles — directly separating the two mechanisms and the three drugs.
2. **Knock-in mouse dose-ranging in vivo study.** Model: MYH7 R1500P (or additional rod) knock-in, not transgenic. Perturbation: MYK-581/mavacamten across doses and durations (addressing the [PMID:39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/) short-duration failure). Readout: running capacity, grip, muscle MRI, energy proteome. *Expected:* dose-dependent rescue with a definable therapeutic-vs-toxic window.
3. **Tolerability/safety study on healthy slow skeletal muscle.** To quantify the iatrogenic-myopathy risk ([PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/)): CK, strength, fatigue, and histology under chronic dosing in wild-type and heterozygous animals.
4. **Biomarker-stratified first-in-disease human study.** Stratify patients by **elevated myofibril DRX fraction** (the F001 biomarker) and rod/Laing genotype; exclude MSM/aggregation genotypes. Endpoint: 6-minute walk / quantitative myometry. *Expected:* benefit concentrated in high-DRX, hypercontractile-subtype patients.
5. **Causal-edge test for ATP-burden→weakness.** Longitudinal pairing of resting ATP consumption with contractile output in patient myofibers to confirm or refute the inferred causal step highlighted by [PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/).

---

## Curation Leads (require curator verification)

**Candidate status:** Retain **EMERGING**, but add an explicit **subtype restriction**: the hypothesis applies to the *DRX-hypercontractile rod/Laing distal* subtype; mark it *speculative/unknown* for myosin-storage alleles.

**Candidate evidence references & snippets to verify:**
- [PMID:38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/) — "oral administration of MYK-581 … significantly improved the limited running capacity of the R1500P-transgenic mice and corrected the increased DRX state of the myofibrils from patients" (SUPPORT).
- [PMID:41144950](https://pubmed.ncbi.nlm.nih.gov/41144950/) — "mavacamten is not completely specific to cardiac myosin … emerging clinical reports indicate mavacamten-induced generalized skeletal myopathy in elderly patients" (QUALIFY/REFUTE — safety).
- [PMID:39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/) — "short-term Mavacamten treatment is not sufficient to properly counterbalance the metabolically dysregulated proteome" (REFUTE — in vivo failure).
- [PMID:37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) — "the myosin super-relaxed state was decreased in vivo" / "myofiber contractility was not affected" (QUALIFY — dissociation).
- [PMID:40463178](https://pubmed.ncbi.nlm.nih.gov/40463178/) — "In contrast to Mavacamten, Aficamten does not structurally sequester myosin heads along the thick filament" (QUALIFY — non-equivalence).
- [PMID:39485824](https://pubmed.ncbi.nlm.nih.gov/39485824/) — "MSM missense mutations frequently disrupt the tail's stabilizing heptad repeat motif" (COMPETING).
- [PMID:41780808](https://pubmed.ncbi.nlm.nih.gov/41780808/) — "pathogenic variants cluster in locally unwound regions of the coiled-coil dimer … promote dimer destabilization and aggregation" (COMPETING).

**Candidate pathophysiology nodes/edges:** `MYH7 rod mutation → DRX shift → hypercontractility → ↑ resting ATP consumption` (supported); `↑ ATP consumption → skeletal weakness` (**mark as inferred/unconfirmed**); `MYH7 rod/tail mutation → coiled-coil destabilization → thick-filament shortening/aggregation → MSM` (competing branch, supported); `myosin inhibitor ⊣ DRX fraction` (supported); `myosin inhibitor → skeletal myopathy (adverse)` (safety edge).

**Candidate ontology terms:** disease MONDO:0008050 (target), MONDO:0008409, MONDO:0009708, MONDO:0017939; phenotypes HP:0003704 (scapuloperoneal weakness), HP:0011916 (toe extensor amyotrophy), HP:0003803 (type 1 fiber predominance), HP:0000467 (neck muscle weakness); process: regulation of myosin super-relaxed state / ATP metabolic process in muscle contraction.

**Candidate knowledge_gaps / discussion prompts:**
- No registered human trial of any myosin inhibitor in MYH7/skeletal myopathy (ClinicalTrials.gov v2, 2026-10-16).
- Unconfirmed ATP-burden→weakness causal step; conflicting in vivo rescue results.
- GenCC gene–disease validity **unverified** (API 404) — flag for manual lookup.
- Mechanism-of-action divergence among MYK-581/mavacamten/aficamten unresolved for slow skeletal myosin.

**Artifact bundle:** `kb/hypotheses/MYH7-Related_Skeletal_Myopathy/myosin_inhibitor_rescue/openscientist_artifacts/` should contain `MANIFEST.yaml`, `logs/clinicaltrials_gov_search.json`, and the Monarch query log. Note explicitly: the GenCC query artifact records a **404 (failed access)**, not an empty negative result; no patient-level or large raw downloads are bundled — external identifiers and checksums are recorded instead.

---

## Conclusion

The `myosin_inhibitor_rescue` hypothesis is **partially supported and appropriately EMERGING**. It is strongly motivated for the DRX-hypercontractile rod/Laing subtype by one well-constructed preclinical/ex-vivo study and a generalizable energetic rationale, but it lacks human interventional evidence, faces an iatrogenic skeletal-myopathy safety signal, shows inconsistent in vivo rescue in related models, cannot be assumed uniform across the three mechanistically distinct inhibitors, and does not address the competing aggregation mechanism that drives myosin-storage alleles. The most decisive next steps are an allele-panel ex vivo myofibril comparison of the three inhibitors and a biomarker-stratified (DRX-high, rod-genotype) first-in-disease human study.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist environment](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_environment.json)
- [OpenScientist clinicaltrials gov search](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_logs_clinicaltrials_gov_search.json)
- [OpenScientist monarch gencc preflight](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_logs_monarch_gencc_preflight.json)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_myosin_inhibitor_rescue_openscientist_artifacts_tables_evidence_matrix.csv)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 11 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008050` (3 mentions) - the report calls it "target"; MONDO calls it **MYH7-related skeletal myopathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003803` (2 mentions) - the report calls it "type 1 fiber predominance"; HP calls it **Type 1 muscle fiber predominance**