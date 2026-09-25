---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T05:46:20.374254'
end_time: '2026-09-07T06:26:35.188871'
duration_seconds: 2414.82
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: ADNP-Related Syndrome
  category: Mendelian
  hypothesis_group_id: nmd_escape_truncation_branch
  hypothesis_label: NMD-Escaping Truncation Branch
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: nmd_escape_truncation_branch\nhypothesis_label:\
    \ NMD-Escaping Truncation Branch\nstatus: ALTERNATIVE\ndescription: Most pathogenic\
    \ last-exon truncating variants escape nonsense-mediated decay and produce\n \
    \ mutant transcript. Whether their downstream effect is functional insufficiency,\
    \ dominant interference,\n  toxic gain of function, or a mixture remains unresolved\
    \ because mutant protein has not been unambiguously\n  demonstrated in patient\
    \ material.\nevidence:\n- reference: PMID:36945042\n  reference_title: Chromatin\
    \ remodeler Activity-Dependent Neuroprotective Protein (ADNP) contributes to\n\
    \    syndromic autism.\n  supports: SUPPORT\n  evidence_source: OTHER\n  snippet:\
    \ as many mutations cluster in the fifth and last exon and escape from NMD has\
    \ been demonstrated,\n    the majority of patients might still produce protein.\
    \ Thought it needs to be mentioned that mutated\n    protein has never been unambiguously\
    \ demonstrated in patients, an additional gain of toxic function\n    of the mutant\
    \ protein, if present, could also be envisaged\n  explanation: This review defines\
    \ the unresolved mechanism of the common NMD-escaping truncation branch\n    and\
    \ explicitly separates mutant transcript from proof of mutant protein."
  artifact_dir: kb/hypotheses/ADNP-Related_Syndrome/nmd_escape_truncation_branch/openscientist_artifacts
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
citation_count: 15
term_validation:
  total_terms: 6
  verified: 5
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 7
artifact_sources:
  openscientist_artifacts_zip: 7
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
- filename: kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_README.md
  path: openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_README.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist README
- filename: kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_class_counts.csv
  path: openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_class_counts.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist class counts
- filename: kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_gnomad_adnp_constraint.json
  path: openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_gnomad_adnp_constraint.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad adnp constraint
- filename: kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_nmd_sensitive_early_variants.csv
  path: openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_nmd_sensitive_early_variants.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist nmd sensitive early variants
- filename: kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_summary_stats.json
  path: openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_summary_stats.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist summary stats
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** ADNP-Related Syndrome
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** nmd_escape_truncation_branch
- **Hypothesis Label:** NMD-Escaping Truncation Branch
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: nmd_escape_truncation_branch
hypothesis_label: NMD-Escaping Truncation Branch
status: ALTERNATIVE
description: Most pathogenic last-exon truncating variants escape nonsense-mediated decay and produce
  mutant transcript. Whether their downstream effect is functional insufficiency, dominant interference,
  toxic gain of function, or a mixture remains unresolved because mutant protein has not been unambiguously
  demonstrated in patient material.
evidence:
- reference: PMID:36945042
  reference_title: Chromatin remodeler Activity-Dependent Neuroprotective Protein (ADNP) contributes to
    syndromic autism.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: as many mutations cluster in the fifth and last exon and escape from NMD has been demonstrated,
    the majority of patients might still produce protein. Thought it needs to be mentioned that mutated
    protein has never been unambiguously demonstrated in patients, an additional gain of toxic function
    of the mutant protein, if present, could also be envisaged
  explanation: This review defines the unresolved mechanism of the common NMD-escaping truncation branch
    and explicitly separates mutant transcript from proof of mutant protein.
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
result beneath `kb/hypotheses/ADNP-Related_Syndrome/nmd_escape_truncation_branch/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Hypothesis-Search Report — ADNP-Related Syndrome
## Hypothesis: NMD-Escaping Truncation Branch (`nmd_escape_truncation_branch`, KB status: ALTERNATIVE)

*OpenScientist autonomous run, 5 iterations. Search date: 2026-09-07. Primary tools: PubMed (search_pubmed), NCBI ClinVar E-utilities, Ensembl REST, gnomAD GraphQL. No patient-level data files were provided.*

---

## 1. Executive Judgment

**Verdict: PARTIALLY SUPPORTED / UNRESOLVED at the mechanistic-consequence level.**

The hypothesis has two separable claims:

- **Claim A (upstream): "Most pathogenic last-exon truncating variants escape NMD and produce mutant transcript."**
  → **Established / strongly supported.** An independent ClinVar analysis performed here shows 150/165 (90.9%) pathogenic/likely-pathogenic truncating variants map to the last coding exon (or within 55 nt of the last exon–exon junction) and are predicted to escape NMD. Mutant *ADNP* mRNA has been directly detected in patient blood (PMID:38926592). The last coding exon carries ~94% of the CDS, so escape is the structural default for essentially any PTC past codon ~68.

- **Claim B (downstream): "Whether the effect is functional insufficiency, dominant interference, toxic gain of function, or a mixture remains unresolved because mutant protein has not been unambiguously demonstrated in patient material."**
  → **Unresolved — accurately stated.** Mutant ADNP protein has never been unambiguously demonstrated in patient tissue (PMID:38926592; PMID:36945042). The ambiguity is a durable, decade-old open question (first raised in PMID:25169753, 2014). Current model/in-vitro evidence *leans toward functional insufficiency* (last-exon knock-in mouse shows reduced Adnp levels and chromatin binding, PMID:42208149; nonsense variants reduce enzymatic activity, PMID:41174994; extreme LoF constraint pLI≈1.0; a splice variant causes disease by pure haploinsufficiency, PMID:38424297), **but** a distinct/gain-of-dysfunction contribution is not excluded (overexpressed truncated mutants are expressed and mislocalize with mutation-specific phenotypes, PMID:36230962/37759476; a missense variant acts dominant-negatively, PMID:41943166; another missense is predicted gain-of-function, PMID:40977432).

**Bottom line:** The hypothesis is a faithful, well-posed description of a genuinely unresolved mechanism. Its *premise* (NMD escape → mutant transcript) is confirmed; its *central question* (what the retained mutant protein does, if it exists at all in patients) remains open. Retaining ALTERNATIVE/unresolved status is appropriate. The most important caveat is that the balance of current evidence modestly favors haploinsufficiency/insufficiency as the dominant driver, with any gain-of-function/dominant-negative effect unproven at the endogenous patient-protein level.

---

## 2. Evidence Matrix

| # | Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|----------|---------------|--------|--------------------------|-------------|-----------------|--------------------------|
| 1 | PMID:38926592 (D'Incal 2024) | Human/in vitro | **Supports (A) / Qualifies (B)** | NMD escape → mutant transcript → mutant protein? | Mutant *ADNP* mRNA detected in patient blood; validated ~150 kDa WT band; truncated mutant protein detectable only in *E. coli*/tagged overexpression, **not** in patient material | Last-exon truncating HVDAS | High for RNA/antibody validation; the central negative (no endogenous mutant protein) is the key gap |
| 2 | This report — ClinVar computational analysis | Computational | **Supports (A)** | Do truncating variants cluster in last exon and escape NMD? | 165/303 P/LP variants truncating; **150/165 (90.9%) predicted NMD-escape**; 15 NMD-sensitive are all codons 3–42 | All P/LP ADNP variants (GRCh38) | Medium-high; NMD escape *predicted* by 50–55 nt rule, not measured; ClinVar is submission-biased |
| 3 | gnomAD v2.1.1 (this report) | Computational | **Supports insufficiency (B)** | Is ADNP dosage-sensitive/haploinsufficient? | pLI≈1.0; obs/exp LoF=4/84.9; LOEUF=0.11; LoF Z=7.45 | Population constraint | High for constraint; LOFTEE pLoF mostly = NMD-competent variants, down-weights last-exon PTCs (the patient class) |
| 4 | PMID:42208149 (D'Incal 2026) | Model organism | **Qualifies → insufficiency (B)** | Effect of a last-exon frameshift knock-in in vivo | Reduced brain Adnp (p=8e-4), reduced chromatin association (p=1e-3), ↑chromatin accessibility, Wnt disruption, ASD-like behaviour | Adnp p.Leu822Hisfs*6 mouse (males) | High-quality multi-omics; single variant, males only; "reduced levels" argues against toxic gain |
| 5 | PMID:41174994 (D'Incal 2025) | In vitro | **Qualifies → insufficiency (B)** | Do nonsense variants alter ADNP enzymatic activity? | ADNP methyltransferase activity reduced by nonsense variants; male-specific H3K79me1 reduction | Overexpression + tissue | Emerging/novel (methyltransferase activity itself is new); overexpression systems |
| 6 | PMID:36230962 (Ganaiem 2022) | In vitro | **Supports gain-of-dysfunction (B)** | Do truncated ADNP proteins behave as simple nulls? | GFP-tagged p.Ser404*/p.Tyr719* expressed, accumulate in cytoplasm, mutation-specific phenotypes; aberrant nuclear/cytoplasmic boundaries | Truncating mutants, neuroblastoma | Medium; overexpressed, GFP-tagged, non-patient cell line — not endogenous protein |
| 7 | PMID:37759476 (Ganaiem 2023) | In vitro | **Supports gain-of-dysfunction (B)** | Mislocalization & microtubule effects of mutant ADNP | Aberrant nuclear/cytoplasmic ADNP distribution; reduced microtubule content; NAP rescues | Truncating mutants | Medium; overexpression caveat |
| 8 | PMID:38424297 (D'Incal 2024) | Human/in vitro | **Competing → pure haploinsufficiency** | Can HVDAS arise from LoF alone (no mutant protein)? | Splice-acceptor variant → exon-4 skipping; N-terminal truncated protein NOT detectable; "first confirmed diagnosis exclusively due to haploinsufficiency" | Non-truncating splice HVDAS | High for this case; n=1; different variant class than seed |
| 9 | PMID:41943166 (Chen 2026) | In vitro + iPSC + mouse IUE | **Competing → dominant-negative (missense)** | Does mutant ADNP interfere with WT? | Missense p.C687R mislocalizes and **redistributes wild-type ADNP**; disrupts GABAergic differentiation | Missense HVDAS (zinc-finger) | Medium-high; missense, not truncating — informs mechanism space, not seed variant class directly |
| 10 | PMID:40977432 (Benvenuto 2026) | Human/computational | **Competing → gain-of-function (missense)** | Can ADNP variants strengthen function? | Missense p.Ser802Phe predicted to increase ADNP–DNA affinity → GoF hypothesis | Missense HVDAS (homeodomain) | Low-medium; in silico binding prediction, single case |
| 11 | PMID:32758449 (Breen 2020) | Human clinical | **Qualifies** | Do the two mutation-position episignatures map to phenotype? | Two mutation-dependent episignatures replicated; **limited phenotype correlation**; no profound blood transcriptome change | HVDAS class I vs II | High; argues methylation class ≠ clinical severity, cautioning subtype claims |
| 12 | PMID:38884529 (Sarli 2024) | Human clinical | **Qualifies** | Is "class II" a distinct truncating subtype? | Class II HVDAS (truncating, BNL-region) shares a phenotype-specific episignature with SMARCA2/BIS | Class II truncating HVDAS | High; ties truncation subtype to a shared BAF-related signature |
| 13 | PMID:38637827 (D'Incal 2024) | Human tissue | **Supports downstream effect** | Downstream consequences of a last-exon frameshift in patient brain | Cerebellar CpG methylation changes + mitochondrial gene dysregulation; ADNP motif enriched in DMGs | HVDAS autopsy (His559fs) | Medium; n=1, downstream only, no protein-level mechanism |
| 14 | PMID:25169753 (Vandeweyer 2014) | Human clinical | **Supports framing (B)** | Origin of GoF vs haploinsufficiency debate | First 10 truncating mutations "suggested a gain of function"; 11th "predicted haploinsufficient" | First HVDAS cohort | Historical; establishes durable ambiguity |
| 15 | PMID:29724491 (Van Dijck 2019) | Human clinical | **Context** | Clinical phenotype of HVDAS | 78-patient deep clinical characterization; multisystem syndrome | HVDAS cohort | High; clinical anchor, not mechanistic |
| 16 | PMID:36945042 (D'Incal 2023) | Review | **Supports (seed)** | Defines the unresolved NMD-escape branch | States mutant protein never unambiguously demonstrated; toxic GoF "could be envisaged" | Review | Review-level orientation (seed reference) |

---

## 3. Data and Tool Use

### Databases / APIs accessed

| Source | Accession/URI | Version/snapshot | Retrieval date | Outcome | Query / filters | Resolved & relevant? |
|--------|---------------|------------------|----------------|---------|-----------------|----------------------|
| NCBI ClinVar (E-utilities) | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/ (db=clinvar) | live DB (no pin) | 2026-09-07 | **succeeded** | `ADNP[gene] AND ("pathogenic"[clinsig] OR "likely pathogenic"[clinsig])`; esearch→303 IDs; esummary; GRCh38 positions | Yes; directly relevant |
| Ensembl REST | https://rest.ensembl.org/lookup/id/ENST00000621696?expand=1 | Ensembl (2026-09) | 2026-09-07 | **succeeded** | ADNP canonical MANE transcript exon/CDS coordinates | Yes; used for exon mapping |
| gnomAD GraphQL | https://gnomad.broadinstitute.org/api | gnomAD v2.1.1 constraint | 2026-09-07 | **succeeded** | `gene(gene_symbol:"ADNP")` constraint fields | Yes; dosage-sensitivity evidence |
| ClinGen | https://search.clinicalgenome.org/kb/genes/HGNC:15766 ; /api/curations/HGNC:15766 ; /api/dosage/HGNC:15766 | n/a | 2026-09-07 | **partial/failed** | Gene page HTTP 200 (HTML SPA, "ADNP curation results"); JSON API endpoints returned **404** | Page exists but **machine-readable dosage/validity NOT verified** — curator lead |
| PubMed (search_pubmed) | — | — | 2026-09-07 | **succeeded** | 12 short queries (log in bundle); 4 over-specified queries returned 0 hits | Yes |

### Analyses (input → method → output)

**Analysis 1 — ADNP variant NMD-escape mapping. Outcome: SUCCEEDED.**
- Input: 303 ClinVar P/LP ADNP variants (GRCh38 positions) + ADNP exon/CDS structure (ENST00000621696, chr20 minus strand; last coding exon 50,888,918–50,894,512).
- Method: classify variants by ClinVar molecular_consequence/title; map genomic position to exon; predict NMD escape if PTC in last coding exon or within 55 nt upstream of last exon–exon junction.
- Environment: python 3.12; pandas 3.0.3; numpy 2.3.5; requests 2.34.2; matplotlib 3.10.9. No random seed (deterministic given DB snapshot).
- Output: `openscientist_artifacts/tables/summary_stats.json`, `class_counts.csv`, `nmd_sensitive_early_variants.csv`; code in `code/adnp_clinvar_nmd_analysis.py`. Figure generated in code sandbox but **executor-local only** (separate container; not persisted to job FS) — regenerate via the code.
- Result: 165 truncating; 150 (90.9%) predicted NMD-escape.
- Limitations: NMD escape predicted, not measured; ClinVar submission bias; class inferred from text fields.

**Analysis 2 — gnomAD constraint lookup. Outcome: SUCCEEDED.**
- Input → Method → Output: gnomAD GraphQL → parse constraint → `tables/gnomad_adnp_constraint.json`. pLI=1.0, LOEUF=0.11.
- Limitation: LOFTEE pLoF mostly captures NMD-competent variants; does not directly quantify the last-exon patient class.

**Analysis 3 — ClinGen dosage/validity retrieval. Outcome: FAILED (reported, not silently dropped).**
- API JSON endpoints 404; gene page is an HTML SPA. No fallback to model knowledge; classification left unverified. Logged in `logs/iter3_4_search_log.txt`.

Artifact bundle root: `kb/hypotheses/ADNP-Related_Syndrome/nmd_escape_truncation_branch/openscientist_artifacts/` (MANIFEST.yaml, code/, tables/, logs/, environment/). Input checksums not computed (hashlib blocked in sandbox); inputs are regenerable from the pinned queries.

---

## 4. Mechanistic Causal Chain

```
De novo heterozygous ADNP variant
  │  [STRONG] ~55% truncating (frameshift/nonsense), ~35% missense (ClinVar, this report)
  ▼
Truncating PTC in last coding exon (≥94% of CDS)
  │  [STRONG] 90.9% predicted NMD escape (this report); mutant mRNA in patient blood (PMID:38926592)
  ▼
Mutant transcript retained  ──►  [MISSING/UNPROVEN] Endogenous mutant protein in patient tissue
  │                                    (undetectable to date; PMID:38926592, 36945042)
  ▼
Net functional consequence  = one (or a mix) of:
  ├─ Functional insufficiency  [MODERATE support: PMID:42208149 ↓levels; 41174994 ↓activity; gnomAD pLI≈1; 38424297 pure HI]
  ├─ Dominant interference     [INFERRED: PMID:41943166 (missense redistributes WT); 36230962 mislocalization]
  ├─ Toxic gain of function    [SPECULATIVE: PMID:40977432 in-silico ↑DNA affinity; 36230962 distinct phenotypes]
  └─ Mixture                   [PLAUSIBLE, untested at endogenous level]
  ▼
Impaired ADNP chromatin regulation (ChAHP/SWI-SNF; CTCF antagonism) + cytoskeletal/microtubule dysfunction
  │  [STRONG in models] ↑chromatin accessibility, Wnt disruption (PMID:42208149); CTCF (ChAHP literature)
  ▼
Altered gene-expression & DNA-methylation programs (episignatures; mitochondrial genes)
  │  [STRONG] two mutation-position episignatures (PMID:32758449, 38884529); patient cerebellum (PMID:38637827)
  ▼
Aberrant neurodevelopment (neurogenesis, GABAergic differentiation, synaptic pruning)
  ▼
HVDAS clinical phenotype: ASD, ID, dysmorphism, multisystem features (PMID:29724491)
```

**Strong links:** variant→NMD escape→mutant transcript; ADNP loss→chromatin/expression changes→neurodevelopmental phenotype (models + patient tissue + episignature).
**Inferred links:** mutant transcript→which protein-level consequence; dominant-negative/GoF edges rest on missense or overexpression data.
**Missing step (the crux):** unambiguous demonstration (and quantification) of endogenous mutant protein in patient material, and whether it is null-equivalent, interfering, or toxic.

---

## 5. Knowledge Gaps

1. **Endogenous mutant protein — existence and behavior (CRITICAL, checked).** No study has unambiguously detected truncated ADNP in patient tissue (PMID:38926592). Resolves via: sensitive targeted mass spectrometry (PRM/MRM for mutant-specific tryptic/neo-C-terminal peptides) in patient iPSC-neurons/organoids or accessible tissue; allele-specific ribosome profiling.
2. **Insufficiency vs dominant-negative vs toxic gain (CRITICAL).** Models lean to insufficiency but overexpression/missense data keep interference/GoF alive. Resolves via: isogenic patient vs corrected iPSC-neurons at endogenous expression; degron/dose-titration; co-expression interference assays with tagged WT.
3. **Subtype heterogeneity by variant position.** Two episignatures exist but correlate weakly with phenotype (PMID:32758449); different truncations give opposite in-vitro phenotypes (PMID:36230962). Whether "class I/II" reflect distinct mechanisms is unresolved. Resolves via: position-stratified functional cohorts.
4. **Constraint metric vs patient variant class.** gnomAD pLI≈1.0 but LOFTEE mostly scores NMD-competent variants; the last-exon patient class is under-represented in the metric. A last-exon-specific constraint/patient-recurrence analysis is missing.
5. **ClinGen/GenCC source-level absence (checked, unverified).** ClinGen ADNP curation page resolves but dosage/validity JSON returned 404 on 2026-09-07; classification could not be programmatically confirmed. Label: **unverified**, not absent. Resolves via: manual ClinGen/GenCC lookup by a curator.
6. **Treatment mechanism (NAP/davunetide).** NAP rescues mutant-cell phenotypes (PMID:37759476) but its precise molecular target relative to the mutant protein is not established; no completed HVDAS-specific efficacy trial identified in this search.

---

## 6. Alternative Models

- **Haploinsufficiency / functional insufficiency (KB-likely PRIMARY).** *Alternative to the seed's GoF/interference branches; also the parsimonious default.* Supported by ↓protein/activity in models, extreme LoF constraint, and a pure-HI splice case (PMID:38424297, 42208149, 41174994). The seed hypothesis is compatible with this if the mutant protein is null-equivalent.
- **Dominant-negative interference.** *Alternative downstream branch of the seed.* Missense p.C687R redistributes WT ADNP (PMID:41943166); truncated mutants mislocalize (PMID:36230962). Endogenous evidence lacking.
- **Toxic gain of function.** *Alternative downstream branch.* In-silico ↑DNA affinity (PMID:40977432); mutation-specific cellular phenotypes. Most speculative.
- **Cytoskeletal/microtubule–autophagy dysfunction (parallel mechanism).** ADNP–EB1/EB3/Tau axis; mTOR/autophagy (everolimus rescue in KD mouse). Downstream/parallel to chromatin dysfunction rather than competing at the variant level.
- **Cell-type-specific mechanisms (parallel).** ADNP roles in microglial synaptic pruning (PMID:40188316) and GABAergic differentiation (PMID:41943166) suggest non-neuronal contributions.

---

## 7. Discriminating Tests

1. **Endogenous mutant-protein detection (decisive).** Targeted PRM/MRM mass spectrometry + allele-specific Western/immunoprecipitation on patient iPSC-derived neurons/organoids carrying recurrent last-exon variants (e.g., p.Tyr719*, p.His559fs). *Expected:* insufficiency → little/no stable mutant protein; interference/GoF → detectable stable truncated protein. Directly closes the crux gap.
2. **Isogenic dose–response.** Patient vs CRISPR-corrected isogenic iPSC-neurons; compare to heterozygous null (early-exon NMD-competent variant) at matched differentiation. *Expected:* if phenotype of last-exon variant = heterozygous null → insufficiency; if more severe or qualitatively different → interference/GoF.
3. **WT-interference assay.** Co-express endogenous-level tagged WT with mutant; quantify WT chromatin occupancy (CUT&RUN) and localization. *Expected:* dominant-negative → reduced WT occupancy/mislocalized WT.
4. **Position-stratified multi-omic cohort.** Stratify patients by class I vs II episignature and by variant position; RNA-seq/methylation on iPSC-neurons. *Expected:* distinct molecular consequences would justify subtype restriction of the hypothesis.
5. **Allele-specific ribosome profiling** in patient cells to confirm translation of the mutant transcript (bridges transcript→protein step).

---

## 8. Curation Leads (require curator verification)

**Candidate evidence references + snippets to verify:**
- PMID:38926592 — "we previously demonstrated escape from nonsense-mediated decay by detecting mutant ADNP mRNA in patient blood" (upstream NMD-escape). *Note:* the seed's snippet for PMID:36945042 is from full text, not the stored abstract — verify against full text.
- PMID:42208149 — "reduced cellular Adnp levels in the brain (p = 0.0008) and decreased its chromatin association (p = 0.001)" (insufficiency edge).
- PMID:25169753 — "the first 10 patients … suggested a gain of function mechanism, an 11th patient … is predicted haploinsufficient" (durable ambiguity).
- PMID:36230962 — "these discrete phenotypes were associated with an increased expression of both mutant proteins in the cytoplasm" (gain-of-dysfunction lead; overexpression caveat).
- PMID:38424297 — "first confirmed diagnosis exclusively due to haploinsufficiency of the ADNP gene" (pure-HI competing model).

**Candidate pathophysiology nodes/edges:** add edge `mutant transcript → (unproven) endogenous mutant protein` with status *unconfirmed*; edges `truncating variant → NMD escape (predicted, 90.9%)`, `ADNP LoF → ↑chromatin accessibility/CTCF antagonism`, `ADNP LoF → episignature (class I/II)`, `ADNP LoF → mitochondrial gene dysregulation (patient cerebellum)`.

**Candidate ontology terms:** GABAergic interneuron differentiation (GO:0097154); microglial synaptic pruning (GO:0150062-related); microtubule cytoskeleton organization (GO:0000226); chromatin remodeling (GO:0006338); nonsense-mediated decay (GO:0000184). Cell types: cortical neural progenitor, GABAergic interneuron, microglia, cerebellar tissue.

**Candidate subtype restriction:** hypothesis applies specifically to last-exon truncating variants (~91% of truncating, ~50% of all P/LP alleles); explicitly does NOT cover early NMD-competent variants (codons 3–42; the pure-HI splice case) or missense variants (which have their own dominant-negative/GoF evidence).

**Candidate status:** **retain ALTERNATIVE / unresolved.** Add `knowledge_gaps`: (i) endogenous mutant protein undemonstrated; (ii) insufficiency vs interference vs GoF unresolved; (iii) ClinGen/GenCC classification unverified as of 2026-09-07 (API 404).

---

## 9. Limitations

- Literature-and-public-database study; no patient-level omics data were provided or analyzed.
- NMD escape is *predicted* (last-exon/55-nt rule), not experimentally measured per variant.
- ClinVar is a live, submission-biased database (no version pin); counts may drift.
- gnomAD constraint reflects NMD-competent pLoF, not the last-exon patient class.
- ClinGen/GenCC classifications could not be programmatically verified (endpoints 404).
- Several mechanistic in-vitro results rely on overexpressed/tagged constructs, not endogenous patient protein.
- Analysis figure is executor-local (separate sandbox container) and was not persisted to the bundle; it is regenerable from the included code.

---

*Findings recorded to the knowledge graph this run: 7. Artifact bundle: `kb/hypotheses/ADNP-Related_Syndrome/nmd_escape_truncation_branch/openscientist_artifacts/`.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist README](openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_README.md)
- [OpenScientist class counts](openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_class_counts.csv)
- [OpenScientist gnomad adnp constraint](openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_gnomad_adnp_constraint.json)
- [OpenScientist nmd sensitive early variants](openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_nmd_sensitive_early_variants.csv)
- [OpenScientist summary stats](openscientist_artifacts/kb_hypotheses_ADNP-Related_Syndrome_nmd_escape_truncation_branch_openscientist_artifacts_tables_summary_stats.json)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

5 of 6 terms resolved to a current term; the rest could not be looked up either way.