---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T03:30:25.196154'
end_time: '2026-10-25T03:55:25.182224'
duration_seconds: 1499.99
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation
    2
  category: Mendelian
  hypothesis_group_id: coupling_versus_catalysis_allelic_split
  hypothesis_label: ATP5F1B variants split into a coupling-defect arm causing hypermetabolism
    and a catalytic-defect arm causing dystonia
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: coupling_versus_catalysis_allelic_split\n\
    hypothesis_label: ATP5F1B variants split into a coupling-defect arm causing hypermetabolism\
    \ and a catalytic-defect\n  arm causing dystonia\nstatus: EMERGING\ndescription:\
    \ 'Heterozygous ATP5F1B variants produce two clinically disjoint phenotypes, and\
    \ both arms\n  are reported as dominant-negative, so the dominance mode does not\
    \ separate them. The hypothesis is that\n  what differs is which function of the\
    \ beta subunit the mutant protein spoils. In the hypermetabolic\n  arm, p.Leu335Pro\
    \ leaves proton translocation and complex V assembly intact but loosens the coupling\n\
    \  between stalk rotation and ATP synthesis, so energy leaves as heat and respiration\
    \ rises. In the movement-disorder\n  arm, p.Thr334Pro and p.Val482Ala leave beta\
    \ subunit abundance intact but severely reduce complex V activity,\n  and a splice\
    \ variant lowers ATP5F1B mRNA and impairs ATPase activity, so the result is insufficient\n\
    \  ATP and a basal-ganglia-predominant phenotype. The prediction that distinguishes\
    \ them is the direction\n  of respiratory flux: the coupling arm should show elevated\
    \ oxygen consumption with low membrane potential,\n  while the catalytic arm should\
    \ show reduced complex V activity. Both arms report a low membrane potential,\n\
    \  so membrane potential alone does not discriminate. Two observations argue against\
    \ any simple structural\n  reading of the split. p.Thr334Pro and p.Leu335Pro are\
    \ proline substitutions at adjacent residues with\n  opposite clinical consequences,\
    \ which no published work explains or directly compares. And no study\n  has measured\
    \ respiration and complex V activity side by side across variants from both arms\
    \ in one assay,\n  so the flux contrast above is assembled across laboratories\
    \ rather than observed.'\nevidence:\n- reference: PMID:36239646\n  reference_title:\
    \ Congenital Hypermetabolism and Uncoupled Oxidative Phosphorylation.\n  supports:\
    \ SUPPORT\n  evidence_source: IN_VITRO\n  snippet: these results suggest the increased\
    \ oxygen consumption rate is caused by dissipation of the\n    proton motive force,\
    \ without a corresponding increase in ATP synthesis\n  explanation: 'Establishes\
    \ the coupling-defect arm: raised respiration attributable to dissipated proton\n\
    \    motive force rather than to ATP demand.'\n- reference: PMID:36860166\n  reference_title:\
    \ Variants in ATP5F1B are associated with dominantly inherited dystonia.\n  supports:\
    \ SUPPORT\n  evidence_source: IN_VITRO\n  snippet: Functional studies in mutant\
    \ fibroblasts revealed no decrease of ATP5F1B protein amount but\n    severe reduction\
    \ of complex V activity and impaired mitochondrial membrane potential, suggesting\
    \ a\n    dominant-negative effect.\n  explanation: Establishes the catalytic-defect\
    \ arm, and shows it is also dominant-negative with normal\n    subunit abundance,\
    \ which is why the hypothesis turns on which function is lost rather than on the\n\
    \    dominance mode.\n- reference: PMID:36860166\n  reference_title: Variants\
    \ in ATP5F1B are associated with dominantly inherited dystonia.\n  supports: SUPPORT\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: two different ATP5F1B missense\
    \ variants (c.1000A>C; p.Thr334Pro and c.1445T>C; p.Val482Ala)\n    segregating\
    \ with early-onset isolated dystonia in two families\n  explanation: Supplies\
    \ the dystonia-arm variant coordinates, including the p.Thr334Pro residue adjacent\n\
    \    to the hypermetabolism arm's p.Leu335Pro.\n- reference: PMID:40276935\n \
    \ reference_title: Expanding the Allelic and Clinical Heterogeneity of Movement\
    \ Disorders Linked to Defects\n    of Mitochondrial Adenosine Triphosphate Synthase.\n\
    \  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: A third heterozygous\
    \ variant, c.1074+1G>T, affected a canonical donor splice site of ATP5F1B\n  \
    \  and resulted in exon skipping with significantly diminished ATP5F1B mRNA levels,\
    \ as well as impaired\n    ATPase activity. The associated phenotype consisted\
    \ of cerebral palsy (CP) with prominent generalized\n    dystonia.\n  explanation:\
    \ A reduction-of-output allele, by a different molecular route from the missense\
    \ variants,\n    also produces a movement disorder, which supports grouping loss\
    \ of ATP synthase output with the dystonia\n    arm."
  artifact_dir: kb/hypotheses/Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2/coupling_versus_catalysis_allelic_split/openscientist_artifacts
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
term_validation:
  total_terms: 4
  verified: 3
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0015992
    ontology_label: GO_0015992
    replaced_by: GO:1902600
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
- filename: kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_gnomad_constraint_ATP5F1B.json
  path: openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_gnomad_constraint_ATP5F1B.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad constraint ATP5F1B
- filename: kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_residue_distances.csv
  path: openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_residue_distances.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist residue distances
- filename: kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_secondary_structure_and_constraint.csv
  path: openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_secondary_structure_and_constraint.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist secondary structure and constraint
- filename: kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_logs_pubmed_search_log.md
  path: openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_logs_pubmed_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** coupling_versus_catalysis_allelic_split
- **Hypothesis Label:** ATP5F1B variants split into a coupling-defect arm causing hypermetabolism and a catalytic-defect arm causing dystonia
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: coupling_versus_catalysis_allelic_split
hypothesis_label: ATP5F1B variants split into a coupling-defect arm causing hypermetabolism and a catalytic-defect
  arm causing dystonia
status: EMERGING
description: 'Heterozygous ATP5F1B variants produce two clinically disjoint phenotypes, and both arms
  are reported as dominant-negative, so the dominance mode does not separate them. The hypothesis is that
  what differs is which function of the beta subunit the mutant protein spoils. In the hypermetabolic
  arm, p.Leu335Pro leaves proton translocation and complex V assembly intact but loosens the coupling
  between stalk rotation and ATP synthesis, so energy leaves as heat and respiration rises. In the movement-disorder
  arm, p.Thr334Pro and p.Val482Ala leave beta subunit abundance intact but severely reduce complex V activity,
  and a splice variant lowers ATP5F1B mRNA and impairs ATPase activity, so the result is insufficient
  ATP and a basal-ganglia-predominant phenotype. The prediction that distinguishes them is the direction
  of respiratory flux: the coupling arm should show elevated oxygen consumption with low membrane potential,
  while the catalytic arm should show reduced complex V activity. Both arms report a low membrane potential,
  so membrane potential alone does not discriminate. Two observations argue against any simple structural
  reading of the split. p.Thr334Pro and p.Leu335Pro are proline substitutions at adjacent residues with
  opposite clinical consequences, which no published work explains or directly compares. And no study
  has measured respiration and complex V activity side by side across variants from both arms in one assay,
  so the flux contrast above is assembled across laboratories rather than observed.'
evidence:
- reference: PMID:36239646
  reference_title: Congenital Hypermetabolism and Uncoupled Oxidative Phosphorylation.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: these results suggest the increased oxygen consumption rate is caused by dissipation of the
    proton motive force, without a corresponding increase in ATP synthesis
  explanation: 'Establishes the coupling-defect arm: raised respiration attributable to dissipated proton
    motive force rather than to ATP demand.'
- reference: PMID:36860166
  reference_title: Variants in ATP5F1B are associated with dominantly inherited dystonia.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Functional studies in mutant fibroblasts revealed no decrease of ATP5F1B protein amount but
    severe reduction of complex V activity and impaired mitochondrial membrane potential, suggesting a
    dominant-negative effect.
  explanation: Establishes the catalytic-defect arm, and shows it is also dominant-negative with normal
    subunit abundance, which is why the hypothesis turns on which function is lost rather than on the
    dominance mode.
- reference: PMID:36860166
  reference_title: Variants in ATP5F1B are associated with dominantly inherited dystonia.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: two different ATP5F1B missense variants (c.1000A>C; p.Thr334Pro and c.1445T>C; p.Val482Ala)
    segregating with early-onset isolated dystonia in two families
  explanation: Supplies the dystonia-arm variant coordinates, including the p.Thr334Pro residue adjacent
    to the hypermetabolism arm's p.Leu335Pro.
- reference: PMID:40276935
  reference_title: Expanding the Allelic and Clinical Heterogeneity of Movement Disorders Linked to Defects
    of Mitochondrial Adenosine Triphosphate Synthase.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: A third heterozygous variant, c.1074+1G>T, affected a canonical donor splice site of ATP5F1B
    and resulted in exon skipping with significantly diminished ATP5F1B mRNA levels, as well as impaired
    ATPase activity. The associated phenotype consisted of cerebral palsy (CP) with prominent generalized
    dystonia.
  explanation: A reduction-of-output allele, by a different molecular route from the missense variants,
    also produces a movement disorder, which supports grouping loss of ATP synthase output with the dystonia
    arm.
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
result beneath `kb/hypotheses/Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2/coupling_versus_catalysis_allelic_split/openscientist_artifacts`. Do not create an empty bundle when no data
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
- **Disease:** Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2 (Mendelian)
- **Hypothesis ID:** `coupling_versus_catalysis_allelic_split`
- **Label:** *ATP5F1B variants split into a coupling-defect arm causing hypermetabolism and a catalytic-defect arm causing dystonia*
- **Status in KB:** EMERGING
- **Verdict reached here:** **Partially supported at the phenotype level; UNRESOLVED at its mechanistic core. Retain EMERGING.**

---

## Executive Judgment

**The hypothesis is PARTIALLY SUPPORTED.** The two clinical "arms" it posits are each independently well documented in primary literature, and the claim that the dominance mode cannot separate them is correct — both arms are reported as dominant-negative. However, the *decisive* claim of the hypothesis — that the arms differ specifically in *which* beta-subunit function is spoiled, and that this is readable as *opposite directions of respiratory flux* (elevated O₂ consumption in the coupling arm versus reduced complex V activity in the catalytic arm) — has **never been tested side-by-side in a single assay**, and a dedicated computational structural analysis conducted in this investigation finds **no simple positional basis for the split**.

Three considerations drive the "unresolved core" verdict. First, the respiratory-flux contrast that is supposed to distinguish the arms is assembled across different laboratories, cell lines, and assay conditions rather than observed in one isogenic experiment; a targeted PubMed search (2026-10-25) found no study measuring respiration and complex V activity side by side across variants from both arms. Second, structural mapping onto the bovine F₁-ATPase crystal structure (PDB 1BMF) shows that none of the three index residues (T334, L335, V482) contacts the catalytic nucleotide (all ≥13 Å away, versus ~2.7 Å for a validated P-loop control) or sits at the γ-rotor interface — and the two adjacent prolines with opposite clinical consequences, p.Thr334Pro (dystonia) and p.Leu335Pro (hypermetabolism), occupy near-identical microenvironments. Third, the key "loosened coupling of synthesis" step for p.Leu335Pro is demonstrated directly only in a yeast homolog; in human cells only the elevated-respiration phenotype is recapitulated.

A **more parsimonious competing model** also explains the dystonia arm without invoking a catalysis-versus-coupling axis: selective basal-ganglia vulnerability to *any* partial loss of complex V output. Movement disorders with reduced complex V output recur across at least three ATP synthase subunit genes (ATP5F1A, ATP5F1B, ATP5MC3), whereas the hypermetabolism/uncoupling presentation remains unique to ATP5F1B p.Leu335Pro. The most important caveat for curators is that one snippet cited in the seed YAML for PMID:36239646 ("these results suggest the increased oxygen consumption rate is caused by dissipation of the proton motive force…") was **not found verbatim in the NEJM abstract**; the human-level readout that *is* verifiable is "elevated oxygen consumption and decreased mitochondrial membrane potential." Status **EMERGING should be retained** pending a single isogenic experiment that measures respiration and complex V activity together across variants from both arms.

---

## Key Findings

### F001 — The coupling/hypermetabolism arm is supported (human + yeast evidence)

ATP5F1B **p.Leu335Pro** is a de novo heterozygous variant identified in monozygotic (identical) twins with congenital non-thyroidal hypermetabolism ([PMID: 36239646](https://pubmed.ncbi.nlm.nih.gov/36239646/), NEJM 2022). Patient fibroblasts show **"elevated oxygen consumption and decreased mitochondrial membrane potential"** — the signature of mitochondrial uncoupling, where respiration runs fast but the proton-motive force is dissipated rather than captured as ATP. The explicit mechanistic step — *loosened coupling between stalk rotation and ATP synthesis* — is demonstrated through homologous mutations in yeast, and the mutant allele expressed in human cell lines recapitulates the elevated-respiration phenotype. The direct human-level evidence is therefore the combination of raised oxygen consumption rate (OCR) with low membrane potential (ΔΨ); the "uncoupling of synthesis" mechanism itself is yeast-derived and only partially recapitulated in human cells. The clinical sample is small (n=2, monozygotic twins, a single de novo variant), which limits generalization but does not undermine the direction of the finding.

This finding is conceptually continuous with the historical prototype of "loose coupling" disease: **Luft's disease**, the first described mitochondrial disorder (non-thyroidal hypermetabolism), where isolated mitochondria showed "defective respiratory control and normal phosphorylation capacity ('loose coupling')" and basal ATPase activity seven-fold above normal ([PMID: 1249587](https://pubmed.ncbi.nlm.nih.gov/1249587/)). ATP5F1B p.Leu335Pro can be read as a molecularly defined, gene-level instance of the Luft phenotype.

### F002 — The catalytic/output-loss dystonia arm is supported (human + in vitro)

Two different ATP5F1B missense variants, **p.Thr334Pro and p.Val482Ala**, segregate with early-onset isolated dystonia across two autosomal-dominant families with incomplete penetrance ([PMID: 36860166](https://pubmed.ncbi.nlm.nih.gov/36860166/)). Crucially, functional studies in mutant fibroblasts revealed **"no decrease of ATP5F1B protein amount but severe reduction of complex V activity and impaired mitochondrial membrane potential, suggesting a dominant-negative effect."** This defines the catalytic arm: the mutant subunit is present in normal quantity but poisons the enzyme's catalytic output, consistent with a dominant-negative (poison-subunit) rather than a haploinsufficiency mechanism.

A third, mechanistically distinct allele extends the arm by a different molecular route. The splice variant **c.1074+1G>T** disrupts a canonical donor splice site, causing exon skipping with **"significantly diminished ATP5F1B mRNA levels, as well as impaired ATPase activity,"** and produces a cerebral-palsy phenotype with prominent generalized dystonia ([PMID: 40276935](https://pubmed.ncbi.nlm.nih.gov/40276935/)). Because a reduction-of-output allele (lower mRNA, impaired ATPase) also yields a movement disorder, loss of ATP synthase *output* — whether by catalytic poisoning or by reduced message — groups naturally with the dystonia arm.

### F003 — Structural-domain localization does NOT cleanly separate the arms (computational)

Mapping the variants onto human ATP5F1B (UniProt P06576, 529 aa; transit peptide 1–47), which is positionally 1:1 with the bovine beta subunit (P00829) used in the classic Abrahams F₁ crystal structure, places the functional landmarks as follows: the Walker A P-loop (GGAGVGKT) at 206–213, nucleotide-binding residues at 209–214/238–239, and the DELSEED motif at 444–450. The coupling-arm **L335P** and the catalytic-arm **T334P** are *immediately adjacent* in the same secondary-structure element (local context G-Y-Q-P-**T334**-**L335**-A-T-D-M) within the central nucleotide-binding domain, ~120 residues away from the P-loop. The catalytic-arm **V482A** lies in the C-terminal helical domain, just C-terminal to the DELSEED γ-rotor coupling loop. Paradoxically, the variant physically *closest* to the canonical mechanical-coupling interface (V482, DELSEED-adjacent) belongs to the *catalytic/dystonia* arm, while the *coupling-defect* variant (L335) sits in the nucleotide-binding domain. Thus a naïve "domain-to-phenotype" reading predicts the opposite of the observed assignment.

### F004 — 3D distances (PDB 1BMF) refute a simple structural basis for the split (computational)

A heavy-atom minimum-distance analysis on the bovine F₁-ATPase crystal structure 1BMF (β chains D/E/F representing three catalytic states; γ = chain G; ligands ADP/AMP-PNP) was validated with internal controls: a P-loop residue (UniProt 209) sits 2.7–3.0 Å from bound nucleotide in the closed βDP/βTP states, and DELSEED (UniProt 446) sits 6.5–11 Å from γ — both as expected. Against those benchmarks, the target residues (UniProt→PDB offset −50) are all far from both the catalytic nucleotide and the γ-rotor:

| Residue | Arm | Distance to γ (chain G) | Distance to nucleotide |
|---|---|---|---|
| **T334** | catalytic/dystonia | 12–13 Å | 19–20 Å |
| **L335** | coupling/hypermetabolism | 10–14 Å | 15–16 Å |
| **V482** | catalytic/dystonia | 28–33 Å | 13 Å |
| P-loop (209, control) | — | — | 2.7–3.0 Å |
| DELSEED (446, control) | — | 6.5–11 Å | — |

None of the three variant residues contacts the catalytic nucleotide (all ≥13 Å, versus 2.7 Å for the P-loop), and none sits at the γ interface. The adjacent residues **T334 and L335 share a near-identical microenvironment**, so the opposite clinical consequences of these two proline substitutions cannot be explained by proximity to catalysis or to the rotor. V482 is actually the *farthest* residue from γ (28–33 Å), correcting an earlier inference that its DELSEED sequence-adjacency implied γ-interface proximity.

### F005 — Output-loss dystonia is a convergent cross-subunit phenotype (competing model)

Dystonia/movement disorder with reduced complex V output is not specific to ATP5F1B. A dominant ATP5MC3 variant (p.Asn106Lys) causes autosomal-dominant spastic paraplegia/dystonia; patient fibroblasts show **"impaired complex V activity, ATP generation, and oxygen consumption,"** and transgenic Drosophila show movement phenotypes ([PMID: 34636445](https://pubmed.ncbi.nlm.nih.gov/34636445/)). The dystonia paper itself notes that **"movement disorders have been described in a subset of cases carrying autosomal dominant variants in structural subunits genes ATP5F1A and ATP5MC3"** ([PMID: 36860166](https://pubmed.ncbi.nlm.nih.gov/36860166/)). A 2025 preprint reports dominant-negative ATP5F1A variants disrupting OXPHOS and causing neurological disorders ([PMID: 40672495](https://pubmed.ncbi.nlm.nih.gov/40672495/)). Across at least three ATP synthase subunit genes, movement disorder co-occurs with *reduced* complex V output and *reduced* respiration — the catalytic-arm flux direction, opposite to the hypermetabolism arm. By contrast, the hypermetabolism/uncoupling presentation remains **unique to ATP5F1B p.Leu335Pro**. This convergence is the empirical foundation of the competing "selective basal-ganglia vulnerability" model.

### F006 — Variant-level refinement: different secondary-structure elements + gnomAD constraint (computational)

A secondary-structure parse of PDB 1BMF (β chain D; UniProt = PDB + 50) adds finer resolution than the near-identical 3D distances: catalytic-arm **T334 lies in a loop/coil**, whereas coupling-arm **L335 is the first residue (N-cap) of an α-helix** (PDB residues 285–293); V482 and DELSEED (446) are loop/coil; the P-loop control (206) is a β-strand. So although T334 and L335 are adjacent and share a microenvironment, the two prolines perturb *different local elements* (a loop versus a helix N-terminus) — the only structural distinction that tracks with the clinical split, and a weak one. gnomAD v4 constraint for ATP5F1B (ENSG00000110955) shows **strong missense constraint (missense Z = 4.70; observed/expected 0.57)** and only moderate LoF constraint (pLI = 0.80; LOEUF 0.556; 17 observed vs 46 expected LoF; synonymous Z = 1.43, model valid). The strong missense constraint is consistent with dominant-negative missense pathogenicity rather than simple haploinsufficiency, supporting the "poison subunit" reading of both arms.

### F007 — Final synthesis verdict

Integrating six findings across seven primary/preprint references: the **two arms exist and are each documented**, and both are dominant-negative, so dominance mode does not separate them (SUPPORTED). The mechanism is **UNRESOLVED/limited** because (1) the discriminating respiratory-flux contrast has never been measured side by side in one assay (PubMed negative search, 2026-10-25); (2) structural analysis finds no residue contacting the catalytic nucleotide or γ-rotor and near-identical microenvironments for the two adjacent prolines; (3) the L335P uncoupling-of-synthesis step is yeast-derived; and (4) the seed's cited snippet for PMID:36239646 is absent from the NEJM abstract. A parsimonious **competing** model (selective basal-ganglia vulnerability to any complex V output loss) is supported by cross-subunit convergence.

---

## Mechanistic Model / Interpretation

The hypothesis proposes a clean bifurcation of one gene's mutational spectrum into two mechanistically opposite diseases:

```
                         ATP5F1B (β subunit of F1-ATP synthase)
                                       |
          ┌────────────────────────────┴────────────────────────────┐
          |                                                          |
   COUPLING-DEFECT ARM                                      CATALYTIC-DEFECT ARM
   p.Leu335Pro (de novo)                           p.Thr334Pro, p.Val482Ala (missense)
                                                   c.1074+1G>T (splice, ↓mRNA)
          |                                                          |
  proton translocation &                               β-subunit abundance normal
  complex V assembly INTACT                            complex V ACTIVITY ↓↓ (poison)
  but stalk-rotation→synthesis                         or mRNA/ATPase output ↓
  COUPLING loosened                                                  |
          |                                                          |
  O2 consumption ↑ (respiration high)                 O2 consumption ↓ (output low)
  ΔΨ low   ← both arms share low ΔΨ →                  ΔΨ low
  energy lost as HEAT                                  insufficient ATP
          |                                                          |
   HYPERMETABOLISM                                      DYSTONIA / basal-ganglia phenotype
```

The literature is **strong on the two endpoints** (the clinical arms and their respective in-vitro readouts) and **strong on the shared dominant-negative dominance mode**, which correctly removes "mode of inheritance" as a discriminator. The literature is **weak-to-absent on the central causal edge** that the hypothesis hinges upon: that the *same* enzyme, perturbed at adjacent residues, is pushed in opposite flux directions by two distinct spoiled functions. That edge is **inferred, not observed** — it is assembled from a human uncoupling readout (L335P), a yeast coupling-loss mechanism, and separately measured complex V deficits (T334P/V482A), never co-measured.

The structural work performed here actively *weakens* a simple reading of the model: the uncoupling variant is not near the proton path or assembly interface in a way that is structurally privileged, the two adjacent prolines are structurally near-twins, and the variant nearest the DELSEED/γ coupling machinery (V482) is in the *catalytic* arm, not the coupling arm. The single structural distinction that survives — L335 N-caps a helix while T334 sits in a loop — is a plausible but untested lever for how two neighboring prolines might distort the fold differently.

The most important interpretive tension is between **two generative models for dystonia**:
- *Hypothesis model:* dystonia arises specifically from **catalytic insufficiency** (one of two distinct spoiled functions).
- *Competing model:* dystonia arises from **selective basal-ganglia vulnerability to any partial ATP synthase output loss**, regardless of which subunit or mechanism causes it.

The cross-subunit convergence (ATP5F1A/ATP5F1B/ATP5MC3 all producing movement disorder with reduced output and reduced respiration) is more parsimoniously explained by the competing model, because it requires only one principle (tissue vulnerability to energy deficit) rather than a gene-internal catalysis-versus-coupling axis.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies / Competing | Mechanistic claim tested | Key finding | Disease subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 36239646](https://pubmed.ncbi.nlm.nih.gov/36239646/) | Human clinical + in vitro | **Supports** (coupling arm) | p.Leu335Pro uncouples OXPHOS, raising respiration | "elevated oxygen consumption and decreased mitochondrial membrane potential" in patient fibroblasts; yeast homolog loosens coupling; recapitulated in human cells | Congenital hypermetabolism; identical twins, de novo | Moderate–high for phenotype; n=2, single variant; "uncoupling of synthesis" step is yeast-derived; seed's exact snippet not verbatim in NEJM abstract |
| [PMID: 36860166](https://pubmed.ncbi.nlm.nih.gov/36860166/) | In vitro | **Supports** (catalytic arm) | Missense variants poison complex V catalysis without reducing subunit amount | "no decrease of ATP5F1B protein amount but severe reduction of complex V activity and impaired mitochondrial membrane potential, suggesting a dominant-negative effect" | Early-onset isolated dystonia | High; dominant-negative mechanism directly shown |
| [PMID: 36860166](https://pubmed.ncbi.nlm.nih.gov/36860166/) | Human clinical | **Supports** (variant coordinates) | p.Thr334Pro, p.Val482Ala segregate with dystonia | "two different ATP5F1B missense variants (c.1000A>C; p.Thr334Pro and c.1445T>C; p.Val482Ala) segregating with early-onset isolated dystonia in two families" | Autosomal-dominant dystonia, incomplete penetrance | High for segregation; 2 families |
| [PMID: 36860166](https://pubmed.ncbi.nlm.nih.gov/36860166/) | Human clinical | **Competing** | Movement disorder recurs across other ATP synthase subunits | "Movement disorders have been described in a subset of cases carrying autosomal dominant variants in structural subunits genes ATP5F1A and ATP5MC3" | Cross-gene movement disorder | High; supports tissue-vulnerability model |
| [PMID: 40276935](https://pubmed.ncbi.nlm.nih.gov/40276935/) | Human clinical | **Supports / qualifies** (output-loss) | A splice allele lowering mRNA also causes movement disorder | "exon skipping with significantly diminished ATP5F1B mRNA levels, as well as impaired ATPase activity"; cerebral palsy with generalized dystonia | CP + generalized dystonia | Moderate–high; different molecular route to same arm |
| [PMID: 34636445](https://pubmed.ncbi.nlm.nih.gov/34636445/) | In vitro + model organism | **Competing** | Any subunit output loss → dystonia with reduced respiration | "impaired complex V activity, ATP generation, and oxygen consumption"; Drosophila movement phenotype | ATP5MC3 dystonia/spastic paraplegia | High; demonstrates reduced-respiration flux direction in a parallel gene |
| [PMID: 40672495](https://pubmed.ncbi.nlm.nih.gov/40672495/) | Human clinical (preprint) | **Competing** | Dominant-negative ATP5F1A disrupts OXPHOS → neurological disease | Dominant-negative ATP5F1A variants cause neurological disorders | ATP5F1A neurological disorder | Low–moderate; **preprint, no abstract available**, not peer-reviewed |
| [PMID: 1249587](https://pubmed.ncbi.nlm.nih.gov/1249587/) | Human clinical (historical) | **Qualifies / orientation** | "Loose coupling" hypermetabolism precedent | "defective respiratory control and normal phosphorylation capacity ('loose coupling')"; basal ATPase 7× normal | Luft's disease | Historical context; not ATP5F1B-genotyped |
| [PMID: 18003896](https://pubmed.ncbi.nlm.nih.gov/18003896/) | In vitro / structural | **Orientation** | βTP is the high-affinity catalytic site; γ position sets affinity | Identifies catalytic site geometry used to benchmark distance analysis | F₁-ATPase mechanism | Supports the structural method, not the clinical split |
| [PMID: 18579516](https://pubmed.ncbi.nlm.nih.gov/18579516/) | In vitro / structural | **Orientation** | βDP/αDP H-bond network couples catalysis to rotation | Coupling network exists but is distinct from the index residues | F₁-ATPase mechanism | Orientation only |
| PDB 1BMF (Abrahams 1994) | Computational (structure) | **Refutes simple structural split** | Do index residues contact catalysis/rotor? | T334/L335/V482 all ≥13 Å from nucleotide; adjacent prolines near-identical microenvironment | Structural basis of split | Method validated by P-loop/DELSEED controls; bovine homolog |
| gnomAD v4 (ENSG00000110955) | Computational (population) | **Supports dominant-negative** | Is ATP5F1B missense-constrained? | missense Z = 4.70; LoF pLI 0.80, LOEUF 0.556 | Population constraint | Strong missense constraint consistent with DN missense |

---

## Data and Tool Use

| Resource | Accession / URI | Access status | Query / filters / comparison | Resolved & relevant? |
|---|---|---|---|---|
| PubMed (literature) | eutils / search_pubmed | **Accessed**; 13 papers reviewed | ATP5F1B hypermetabolism; ATP5F1B dystonia; ATP synthase subunit movement disorder; side-by-side respiration + complex V (negative, 2026-10-25) | Yes; directly relevant |
| UniProt P06576 (human ATP5F1B) | https://www.uniprot.org/uniprotkb/P06576 | **Accessed** (sequence/feature mapping) | Transit peptide 1–47; P-loop 206–213; DELSEED 444–450 | Yes |
| UniProt P00829 (bovine β) | https://www.uniprot.org/uniprotkb/P00829 | **Accessed** (1:1 positional mapping) | Alignment to human β for PDB offset | Yes |
| PDB 1BMF (bovine F₁-ATPase) | https://www.rcsb.org/structure/1BMF | **Accessed & analyzed** | Heavy-atom min-distance of T334/L335/V482 to γ (chain G) and nucleotide; P-loop & DELSEED controls; secondary-structure parse | Yes; homolog structure |
| gnomAD v4 | ENSG00000110955 | **Accessed** (constraint lookup) | missense Z, pLI, LOEUF, observed/expected LoF & synonymous | Yes |
| GenCC / ClinGen | — | **Not verified** in this run | No structured GenCC/ClinGen query logged | Unverified — label as absence-not-checked |
| ClinVar variant records | — | **Not programmatically pulled** | Variant coordinates taken from primary papers | Partial; relevant |

**Analysis inventory (input → method → output):**

1. **Structural distance analysis** — *succeeded.* Input: PDB 1BMF + UniProt P06576/P00829 alignment (offset −50). Method: heavy-atom minimum-distance computation with P-loop (2.7–3.0 Å to nucleotide) and DELSEED (6.5–11 Å to γ) as positive controls. Output: distance table (F004) showing all three index residues ≥13 Å from nucleotide and ≥10 Å from γ. Limitation: bovine homolog, static crystal state; no molecular-dynamics perturbation of the proline substitutions.
2. **Secondary-structure parse** — *succeeded.* Input: PDB 1BMF β chain D. Method: DSSP-style assignment. Output (F006): T334 loop/coil, L335 helix N-cap, V482 loop, DELSEED loop, P-loop β-strand. Limitation: single chain/state.
3. **gnomAD constraint lookup** — *succeeded.* Output (F006): missense Z 4.70, pLI 0.80, LOEUF 0.556. Limitation: gene-level, not variant-specific functional prediction.
4. **Side-by-side respiration + complex V literature search** — *failed to find evidence (true negative).* PubMed, 2026-10-25. No study co-measures the two arms' flux in one assay. This is the central empirical gap.

**No patient-level or controlled data were accessed.** No wet-lab or isogenic cell experiment was performed; all mechanistic flux claims derive from the cited literature and the computational structural analysis above. No analysis was fabricated or described as performed that was not performed.

---

## Mechanistic Causal Chain — strength of each link

| Step | Link | Evidence strength |
|---|---|---|
| 1 | Heterozygous ATP5F1B variant present | **Strong** — segregation + de novo in named families (36860166, 36239646) |
| 2 | Mutant β subunit expressed at normal abundance (dominant-negative, not haploinsufficiency) | **Strong** — "no decrease of ATP5F1B protein amount" (36860166); gnomAD missense Z 4.70 |
| 3a (coupling arm) | L335P loosens stalk-rotation→synthesis coupling | **Inferred/partial** — mechanism shown in yeast; human cells show only elevated respiration |
| 4a | ↑O₂ consumption, ↓ΔΨ, heat loss → hypermetabolism | **Strong (human readout)** — "elevated oxygen consumption and decreased mitochondrial membrane potential" (36239646) |
| 3b (catalytic arm) | T334P/V482A poison complex V catalysis; splice allele ↓mRNA/ATPase | **Strong** — "severe reduction of complex V activity" (36860166); "diminished mRNA…impaired ATPase" (40276935) |
| 4b | ↓ATP output → basal-ganglia dystonia | **Moderate** — clinical correlation strong; *selective* neuronal vulnerability mechanism not established |
| 5 (the split itself) | Arms differ specifically by *which function* is spoiled, readable as opposite flux | **Missing/unobserved** — never co-measured; no structural correlate |

The chain is strong at both endpoints and at the dominance mode, inferred at the uncoupling-of-synthesis step, and **missing precisely at the junction the hypothesis is named for** (step 5).

---

## Limitations and Knowledge Gaps

1. **The discriminating flux contrast has never been co-measured (central gap).** No single assay has measured oxygen consumption and complex V activity side by side across coupling-arm and catalytic-arm variants. *Why it matters:* the entire hypothesis rests on an *opposite-direction* flux prediction. *Checked:* PubMed, 2026-10-25, negative. *Resolution:* one isogenic panel (below).
2. **No structural correlate for the split.** PDB 1BMF analysis shows the index residues are far from catalysis and rotor, and the two adjacent prolines are structural near-twins. *Why it matters:* the hypothesis explicitly concedes "no published work explains" the adjacent-proline paradox. *Resolution:* MD or cryo-EM of each variant.
3. **The L335P "uncoupling of synthesis" step is yeast-derived**; human cells recapitulate only respiration. *Resolution:* direct ΔΨ/ATP-synthesis coupling assay in human L335P cells.
4. **Small n and single variants per arm endpoint** (twins for hypermetabolism; two families for dystonia). Penetrance is incomplete in the dystonia families, implying modifiers.
5. **Citation integrity flag:** the seed YAML snippet for PMID:36239646 ("…dissipation of the proton motive force, without a corresponding increase in ATP synthesis") was **not located verbatim** in the NEJM abstract. The verifiable readout is "elevated oxygen consumption and decreased mitochondrial membrane potential." Curators should re-verify the snippet against full text.
6. **Preprint reliance:** the ATP5F1A competing evidence (PMID:40672495) is a preprint with **no abstract available**; treat as provisional.
7. **Source-level absences not fully checked:** no logged GenCC or ClinGen gene-disease validity query in this run — label **unverified**, not "absent."
8. **Mechanism of selective basal-ganglia vulnerability is unknown** for the dystonia arm — a gap shared by both the seed and the competing model.

---

## Alternative / Competing Models

1. **Selective basal-ganglia vulnerability to any complex V output loss (strongest competitor).** Parallel mechanism/alternative. Dystonia follows *reduced output* regardless of subunit (ATP5F1A, ATP5F1B, ATP5MC3) or molecular route (missense poison, reduced mRNA). More parsimonious than a gene-internal catalysis-vs-coupling axis. Supported by [PMID: 34636445](https://pubmed.ncbi.nlm.nih.gov/34636445/) (reduced O₂ consumption + dystonia) and [PMID: 36860166](https://pubmed.ncbi.nlm.nih.gov/36860166/).
2. **Local fold-perturbation model (refines the seed).** The only surviving structural distinction is that L335 N-caps a helix while T334 sits in a loop (F006); the split may reflect *different local misfolding* rather than loss of distinct catalytic vs coupling functions. A mechanistic alternative to the "which-function" framing.
3. **Assembly/stability gradient model.** A continuum in which severity of complex V destabilization — not a qualitative coupling-vs-catalysis switch — determines whether excess heat (mild, leaky) or output failure (severe) dominates. Downstream-consequence reframing.
4. **Historical "loose coupling" continuum (Luft's disease).** Upstream conceptual precedent ([PMID: 1249587](https://pubmed.ncbi.nlm.nih.gov/1249587/)); positions the hypermetabolism arm within a pre-genomic phenotype class.

---

## Discriminating Tests

1. **Isogenic side-by-side respiration + complex V assay (decisive).** Introduce L335P (coupling arm) and T334P / V482A (catalytic arm) into one isogenic background (e.g., CRISPR knock-in iPSC or patient-derived fibroblasts normalized by expression). Measure in the *same* run: Seahorse OCR (basal, coupled, uncoupled/maximal), oligomycin-sensitive respiration, ΔΨ (TMRM), complex V activity (spectrophotometric), and ATP synthesis rate. *Expected if seed is correct:* L335P → high OCR, low oligomycin sensitivity, low ΔΨ, near-normal complex V amount but reduced coupling; T334P/V482A → low complex V activity, low ATP synthesis, low OCR. *Expected if competing model is correct:* both arms show reduced net output, differing only in degree/leak.
2. **Direct ATP-synthesis coupling assay for L335P in human cells** to replace the yeast-derived inference (addresses gap 3).
3. **Molecular dynamics / cryo-EM of each variant** to test whether L335P vs T334P produce divergent local conformational effects (helix N-cap vs loop) despite identical microenvironments (addresses gap 2).
4. **Deep-mutational-scan or saturating variant panel** across the 334–335 region correlating in-vitro flux phenotype with position, to test whether coupling-vs-catalysis segregates by residue or is idiosyncratic.
5. **Cross-subunit meta-analysis of standardized respirometry** across ATP5F1A/ATP5F1B/ATP5MC3 dystonia cases to quantify whether reduced respiration is universal (supports competing model).

---

## Curation Leads (require curator verification)

- **Status:** Retain **EMERGING**. Phenotype-level split is supported; mechanistic core (opposite-flux, which-function) is unobserved and structurally unsupported.
- **Candidate evidence to verify:**
  - [PMID: 36239646](https://pubmed.ncbi.nlm.nih.gov/36239646/) — verify exact snippet; the verifiable abstract phrase is **"elevated oxygen consumption and decreased mitochondrial membrane potential."** Flag that the seed YAML snippet about "dissipation of the proton motive force…" was not found verbatim in the abstract.
  - [PMID: 36860166](https://pubmed.ncbi.nlm.nih.gov/36860166/) — **"no decrease of ATP5F1B protein amount but severe reduction of complex V activity…dominant-negative effect"** and **"Movement disorders have been described…in structural subunits genes ATP5F1A and ATP5MC3."**
  - [PMID: 40276935](https://pubmed.ncbi.nlm.nih.gov/40276935/) — **"exon skipping with significantly diminished ATP5F1B mRNA levels, as well as impaired ATPase activity."**
  - [PMID: 34636445](https://pubmed.ncbi.nlm.nih.gov/34636445/) — **"impaired complex V activity, ATP generation, and oxygen consumption"** (competing/parallel-subunit node).
- **Candidate pathophysiology nodes/edges:** add edge "dominant-negative β subunit → reduced complex V activity → basal-ganglia dystonia"; add competing node "selective basal-ganglia vulnerability to complex V output loss (cross-subunit)"; add node "proton-motive-force dissipation → hypermetabolism."
- **Candidate ontology terms:** oxidative phosphorylation uncoupling, proton motive force (GO:0015992), mitochondrial ATP synthesis coupled proton transport (GO:0042776); cell types: dermal fibroblast (CL:0002620), basal ganglia neuron; HPO: dystonia (HP:0001332), hypermetabolism-adjacent terms.
- **Candidate knowledge_gaps to add:** "No side-by-side respiration + complex V assay across both arms (PubMed negative 2026-10-25)"; "No structural correlate for adjacent-proline opposite phenotypes (PDB 1BMF)"; "L335P uncoupling-of-synthesis step yeast-derived only"; "GenCC/ClinGen gene-disease validity not verified in this run."

---

## Provider Artifact Bundle

An artifact bundle was constructed under
`kb/hypotheses/Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2/coupling_versus_catalysis_allelic_split/openscientist_artifacts`
during iterations 3–5, containing: the structural distance analysis code and output table (PDB 1BMF, UniProt offset mapping, P-loop/DELSEED controls), the secondary-structure parse, the gnomAD constraint record, the PubMed negative-search log (2026-10-25), and a `MANIFEST.yaml` with checksummed inputs/outputs and status/fallback flags. Large raw downloads (PDB, gnomAD) are recorded by stable external accession rather than bundled. No controlled or patient-level data are included.

---

## Bottom Line

The coupling-versus-catalysis allelic split is **real as a clinical dichotomy** and correctly identifies that **dominance mode cannot separate the arms**, but its defining mechanistic claim — opposite respiratory-flux directions driven by two distinct spoiled β-subunit functions — is **assembled across laboratories, never co-observed, and finds no structural correlate**. A simpler competing model (selective basal-ganglia vulnerability to any complex V output loss) explains the dystonia arm across multiple genes without a catalysis-vs-coupling axis. One isogenic experiment measuring respiration and complex V activity together across variants from both arms would resolve the question. **EMERGING should stand.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist gnomad constraint ATP5F1B](openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_gnomad_constraint_ATP5F1B.json)
- [OpenScientist residue distances](openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_residue_distances.csv)
- [OpenScientist secondary structure and constraint](openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_data_derived_secondary_structure_and_constraint.csv)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2_coupling_versus_catalysis_allelic_split_openscientist_artifacts_logs_pubmed_search_log.md)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0015992` (GO_0015992) (1 mention) - replaced by `GO:1902600`

3 of 4 terms resolved to a current term; the rest could not be looked up either way.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.
