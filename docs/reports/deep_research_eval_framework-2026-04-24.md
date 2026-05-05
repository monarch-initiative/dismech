# Deep Research Evaluation Framework

## Purpose

dismech now has enough overlapping deep-research coverage to support
qualitative evaluation of deep-research outputs at the claim level instead of
only with coarse report-level impressions.

The intended evaluation setting is flexible: source `A` and source `B` can each
be any of the following:

- deep research report vs deep research report
- deep research report vs dismech YAML
- deep research report vs cached review article abstract

The core design principle is simple:

1. extract atomic claims from each source
2. align claims that are about the same disease fact
3. classify the relationship between them
4. aggregate those judgments into qualitative report-level scores

This is primarily a requirements and framework document, not a final pipeline
specification. The more generic pieces, especially citation normalization and a
reusable claim/alignment substrate, likely belong upstream in
`deep-research-client`; this doc tries to drive those requirements from the
artifacts we already have in dismech.

## Scope and unit of analysis

The main thing dismech contributes here is the comparison set: diseases where
we have multiple deep-research outputs and, in some cases, a curated YAML entry
or cached review article that can serve as a comparison target.

### Evaluation unit

The evaluation unit should be a single base research run:

- `research/<Disease>-deep-research-<provider>.md`

Do **not** double-count:

- `research/<Disease>-deep-research-<provider>.md.citations.md`

Those `*.citations.md` files are companion artifacts, not independent reports.
On this checkout:

- Base deep-research runs: `921`
- Citation-companion artifacts: `875`
- Total deep-research artifacts: `1796`

The provider totals in the user prompt match the artifact count, not the unique
base-run count. For evaluation, the base run should be primary and the
companion should be treated as optional citation-enrichment evidence.

### Minimal artifact normalization

Before claim extraction, only minimal repo-observable normalization is needed:

| Artifact kind | How to detect | Eval implication |
|---|---|---|
| `base_report` | Base `.md` report | Primary evaluation unit |
| `citation_companion` | Filename ends with `.md.citations.md` | Attach to the base run; do not benchmark separately |
| `source_provider_derived` | Frontmatter includes `source_providers` | Track separately from plain base reports because the artifact explicitly declares dependence on other providers |

Two distinctions are directly visible in this repo and matter immediately:

- `*.md` versus `*.md.citations.md`
- reports that explicitly declare `source_providers:` in frontmatter

The second case is common in `cyberian-codex` outputs. For this design doc,
that is mainly a caution for fair comparison, not a proposal to build a large
report-type ontology.

### Provider normalization

Provider identifiers are also not perfectly canonical. For example:

- `Long_COVID` has both `cyberian` and `cyberian-codex`
- there are small counts for `query`, `claudeweb`, and `curator`

The only normalization worth preserving in the data model is:

- `provider_raw`
- `provider_family`
- `report_mode`

so that comparisons can collapse aliases when appropriate without losing the
original provenance.

## Inventory of multi-provider diseases

Using normalized base runs only:

- `273` diseases have reports from `2+` providers
- `32` diseases have reports from `3+` providers
- those `273` diseases imply `346` pairwise provider comparisons before adding
  report-vs-YAML or report-vs-review evaluation

The `32` diseases with `3+` providers are the most useful initial benchmark set
because they support both pairwise and multi-way comparison.

| Disease | Providers |
|---|---|
| Achondroplasia | codex, cyberian-codex, falcon |
| Bardet-Biedl_Syndrome | cyberian-codex, falcon, openai |
| Botulism | cyberian-codex, falcon, perplexity |
| Breast_Fibroadenoma | cyberian-codex, falcon, perplexity |
| Costello_Syndrome | asta, cyberian-codex, falcon |
| Ehlers-Danlos_Syndrome | cyberian-codex, falcon, perplexity |
| Fanconi_Anemia | cyberian-codex, falcon, openai |
| Fibrodysplasia_Ossificans_Progressiva | cyberian-codex, falcon, perplexity |
| Galactosemia | asta, cyberian-codex, perplexity |
| Hemophilia_B | cyberian-codex, falcon, perplexity |
| Hereditary_von_Willebrand_Disease | cyberian-codex, falcon, perplexity |
| Hypochondrogenesis | asta, cyberian-codex, falcon, perplexity |
| Infectious_Disease | cyberian-codex, falcon, perplexity |
| Kniest_Dysplasia | asta, cyberian-codex, falcon, perplexity |
| Liver_Cirrhosis | asta, cyberian-codex, falcon |
| Long_COVID | cyberian, cyberian-codex, falcon |
| Lung_Carcinoma | cyberian-codex, falcon, perplexity |
| Lymphoma | cyberian-codex, falcon, perplexity |
| Myalgic_Encephalomyelitis_Chronic_Fatigue_Syndrome | cyberian-codex, falcon, perplexity |
| Neuromyelitis_Optica | cyberian-codex, falcon, perplexity |
| Osteoarthritis | asta, cyberian-codex, falcon |
| Osteosarcoma | cyberian-codex, falcon, perplexity |
| Primary_Lateral_Sclerosis | cyberian-codex, falcon, perplexity |
| Primary_Progressive_Aphasia | cyberian-codex, falcon, perplexity |
| Psoriatic_Arthritis | cyberian-codex, falcon, perplexity |
| Semantic_Dementia | cyberian-codex, falcon, perplexity |
| Spondyloepimetaphyseal_Dysplasia_Strudwick_Type | cyberian-codex, falcon, perplexity |
| Spondyloepiphyseal_Dysplasia_Congenita | asta, cyberian-codex, falcon, perplexity |
| Stiff_Person_Syndrome | cyberian-codex, falcon, perplexity |
| Thanatophoric_Dysplasia_Type_1 | asta, cyberian-codex, falcon |
| Thanatophoric_Dysplasia_Type_2 | asta, cyberian-codex, falcon |
| Transverse_Myelitis | cyberian-codex, falcon, perplexity |

## Minimal methodology

The near-term goal is not to build the full generic system. It is to get a
taste of how the methodology behaves on a few strong examples so that we can
write a better upstream request for `deep-research-client`.

The smallest useful methodology is:

1. pick a disease with `2+` provider reports and, if possible, a dismech YAML
   entry or cached review article
2. choose two sources `A` and `B`
3. manually or agentically extract a small set of salient claims from each
   source, typically `5-10`
4. align those claims and assign a relation label
5. write a short qualitative report-level judgment:
   - relevance
   - informativeness
   - accuracy / support
   - completeness relative to the comparison target
   - citation quality
6. note what generic functionality would have made the exercise easier,
   cleaner, or more reproducible

The output of each worked example should therefore be small and concrete:

- a source pair
- a claim table for `A`
- a claim table for `B`
- an alignment table
- a short rubric-style evaluation
- a short list of generic capability gaps

That is enough to inform an upstream feature request without pretending the
full scoring and extraction stack already exists.

## Claim extraction model

### Design goals

Claim extraction should produce atomic, alignable, evidence-linked assertions
that are:

- disease-anchored
- semantically typed
- ontology-grounded when possible
- traceable to a source span
- traceable to one or more citations

The extraction model should avoid counting boilerplate prompt text, duplicated
frontmatter, or repeated reference lists as disease claims.

### Canonical claim record

All source types should be mapped into a shared canonical record. The minimal
record should include:

| Field | Purpose |
|---|---|
| `claim_id` | Stable identifier for one extracted claim |
| `source_type` | `deep_research_report`, `dismech_yaml`, or `review_article` |
| `source_id` | Path or canonical reference id |
| `disease_name`, `disease_id` | Disease anchor |
| `provider`, `model`, `report_mode` | Provenance for reports |
| `section_path` | Heading path or structured slot |
| `claim_text` | Human-readable atomic assertion |
| `claim_frame` | Semantic family such as `disease_phenotype`, `gene_mechanism`, `treatment_outcome` |
| `subject`, `predicate`, `object` | Structured alignment anchors |
| `qualifiers` | Frequency, severity, onset, subtype, population, polarity, temporality, etc. |
| `ontology_anchors` | Normalized HP, GO, MONDO, HGNC, CL, UBERON, CHEBI, MAXO, NCIT ids |
| `citation_mentions_raw` | Raw citation strings as found in the source |
| `normalized_citation_ids` | Canonical PMIDs, DOIs, PMCIDs, URLs, NCT ids after normalization |
| `source_span_text` | Supporting sentence or paragraph from the source |
| `source_span_offsets` | Start/end offsets when available |
| `extraction_confidence` | Model or reviewer confidence |

### What counts as an atomic claim

An atomic claim should contain one independently alignable assertion. Examples:

- "SPS involves anti-GAD65-mediated impairment of GABA synthesis"
- "Kniest dysplasia is caused by heterozygous COL2A1 variants"
- "Fanconi anemia cells are hypersensitive to DNA crosslinking agents"

Conjunctions should usually be split:

- "bone marrow failure, congenital anomalies, and cancer predisposition"
  becomes three claims
- "anti-GlyR (~10-12%), amphiphysin (~5%), rare gephyrin"
  becomes three claims

Do **not** split when the specificity would be destroyed:

- "FANCL and UBE2T monoubiquitinate FANCD2-FANCI"

### Deep research markdown reports

Deep research reports are heterogeneous but structurally regular enough for a
two-stage extractor.

#### Stage 0: preprocess and segment

1. Parse YAML frontmatter and keep:
   - provider
   - model
   - timestamps
   - template file
   - citation count
   - `source_providers` if present
2. Remove prompt scaffolding that appears before the substantive report.
   Real examples in `research/` show repeated template sections before the true
   content, especially in `falcon` reports.
3. Ignore internal reasoning traces when present.
   `perplexity` reports may include `<think>...</think>` blocks that should not
   be extracted as disease claims.
4. Split the substantive body by heading path, paragraph, bullet, and table row.
5. Treat reference inventories as citation metadata, not claim-bearing prose.

#### Stage 1: extract candidate claims

For each content span, extract one or more disease-anchored atomic claims with:

- normalized claim text
- semantic frame
- candidate ontology anchors
- cited references attached to that span

#### Stage 2: normalize and deduplicate

Within one report:

- collapse exact duplicates
- collapse repeated boilerplate claims restated across overview and conclusion
- retain multiple claims if they differ in specificity or qualifiers

This matters because several reports restate the same core mechanism in an
introductory summary, a mechanistic section, and a conclusion.

### dismech YAML

This part should **reuse** the existing claim-extraction work from issue
`#1100`, not replace it.

The repo already has:

- `src/dismech/claims/extract.py`
- `src/dismech/claims/models.py`
- `uv run dismech extract-claims ...`

The current substrate flattens YAML assertions into `ClaimRow` records with:

- disease name and disease id
- claim type and class
- source path
- human-readable claim text
- subject / predicate / object labels and ids
- qualifier fields
- evidence reference, title, snippet, support value, and evidence source
- `is_subclaim`
- `qualifier_evidence_missing`

That substrate is already exactly the right gold-standard side for this eval.
The eval framework should therefore:

1. ingest `ClaimRow` output directly
2. map it into the canonical claim record above
3. preserve `qualifier_evidence_missing` because it is a useful accuracy signal
   for frequency/severity/onset claims

This is especially important because issue `#1100` explicitly models qualified
sub-claims such as:

- disease has phenotype X
- disease has phenotype X with frequency F

That same distinction should carry forward into report-vs-YAML alignment.

### Published review articles from `references_cache`

Cached references are useful comparators, but they come with an important
constraint: many are `abstract_only`.

Example cache structure in this repo:

- YAML frontmatter with `reference_id`, `title`, `authors`, `journal`, `year`,
  `doi`, and `content_type`
- markdown body containing the title and abstract text

Extraction rules for cached review articles:

1. Parse frontmatter and preserve `content_type`
2. Extract claims from abstract/body text only
3. Treat review-article claims as synthesis claims, not primary-study claims
4. Downweight completeness expectations when `content_type: abstract_only`

This makes review articles good comparison anchors for:

- high-level mechanism coverage
- phenotype/treatment summaries
- disease-definition claims

but less suitable as the sole gold standard for granular completeness.

### Ontology grounding

Ontology grounding is the backbone of scalable alignment.

Recommended anchors by claim family:

- disease and subtype: MONDO
- phenotypes: HP
- genes and proteins: HGNC
- biological processes: GO
- cell types: CL
- anatomy: UBERON
- chemicals and drugs: CHEBI
- interventions: MAXO or NCIT

Grounding strategy:

1. Prefer explicit ontology ids when the source already has them.
   YAML already does.
2. For reports and review abstracts, run entity linking over extracted claim
   spans.
3. Keep both:
   - `surface_form`
   - `normalized_id`
4. Preserve unresolved entities instead of dropping them.

Unresolved-but-important entities are common in free text:

- "cardiac defects"
- "failed cellular surveillance"
- "early immunotherapy"

These should still survive as claims with partial grounding.

## Claim alignment model

### What makes two claims "about the same thing"

Two claims should be considered candidate matches when they share:

- the same disease anchor
- the same semantic frame
- the same normalized object, or
- ontology-near objects, or
- the same citation-supported fact stated at different specificity levels

Practical matching examples:

| Example A | Example B | Why they are comparable |
|---|---|---|
| "Stiff person syndrome has anti-GAD65-mediated GABA loss" | "anti-GAD65 antibodies in SPS reduce GABA synthesis" | Same disease, same mechanism, same molecular anchor |
| "Kniest dysplasia causes cardiac defects" | "Kniest dysplasia causes ventricular septal defect" | Same disease, same phenotype family, different HP granularity |
| "IVIg is first-line immunotherapy in SPS" | "IVIg improves SPS symptoms in about 75% of patients after induction" | Same treatment node, different specificity and evidence form |
| "Fanconi anemia causes bone marrow failure" | "FA hematopoietic stem cells undergo attrition under aldehyde stress" | Same disease and progression chain; the second is a more mechanistic subclaim |

### Refined relationship taxonomy

The requested taxonomy is the right starting point. The following definitions are
recommended for annotation and scoring:

| Relation | Definition | Directional? |
|---|---|---|
| `IDENTICAL` | Same proposition and comparable specificity | No |
| `CONSISTENT` | Compatible claims with meaningful wording or evidence differences but no specificity hierarchy | No |
| `SUBSUMING` | Claim A is broader; claim B is a specific instance | Yes |
| `SUBSUMED` | Claim A is narrower; claim B is broader | Yes |
| `CLOSE` | Same topic and same likely fact, but wording or framing prevents stronger equivalence | No |
| `COMPLEMENTARY` | Same disease/topic cluster but non-overlapping facts that jointly extend understanding | No |
| `CONTRADICTORY` | Claims cannot both be true as stated | No |
| `UNSUPPORTED` | Claim in A has no usable counterpart in B | Yes |

### Alignment workflow

#### 1. Candidate generation

Generate cheap candidate pairs first:

- exact ontology id overlap
- ontology ancestor/descendant overlap
- lexical similarity on canonical labels
- citation overlap
- section-type overlap

#### 2. Agent adjudication

Present candidate pairs to an evaluator agent with:

- both claim texts
- source spans
- ontology anchors
- normalized citations
- optionally the cited abstract snippets

The agent assigns:

- relationship label
- short rationale
- confidence
- whether the pair should be split further

#### 3. Human review

Route the following cases to human review:

- `CONTRADICTORY`
- low-confidence `CLOSE`
- unresolved ontology anchors
- missing or suspicious citations
- multi-claim paragraphs where atomization is uncertain

### Handling granularity differences

Granularity is the core difficulty in this eval and needs explicit rules.

#### Phenotype hierarchy

Example:

- A: "cardiac defects"
- B: "ventricular septal defect"

If HP grounding shows B is a descendant of A:

- A vs B = `SUBSUMING`
- B vs A = `SUBSUMED`

#### Mechanistic hierarchy

Example:

- A: "COL2A1 mutations disrupt type II collagen"
- B: "exon 24 skipping causes shortened alpha-1(II) chains that destabilize the triple helix"

These are comparable because they occupy the same disease-gene-mechanism chain.
Again, the more specific claim is `SUBSUMED` relative to the more general one.

#### Treatment hierarchy

Example:

- A: "IVIg is first-line immunotherapy"
- B: "IVIg is effective in up to 75% of patients after three monthly infusions"

These are not identical. They are usually `COMPLEMENTARY` or `CONSISTENT`
depending on whether the evaluation wants to cluster by the same treatment node
or only align near-identical propositions.

### Role of ontology grounding

Ontology grounding should not fully decide the label, but it should strongly
constrain candidate generation and directionality:

- HP and MONDO support phenotype and disease granularity
- GO supports process alignment
- HGNC supports gene/protein identity
- MAXO / NCIT helps keep treatment comparisons comparable

Ontology grounding is especially valuable for:

- parent-child phenotype relations
- synonymous phrasing across providers
- partial matches like "brainstem involvement" vs "brainstem/autonomic dysfunction"

### Alignment record

A stored alignment record should minimally include:

| Field | Purpose |
|---|---|
| `alignment_id` | Stable id for one judged pair |
| `claim_a_id`, `claim_b_id` | Pair members |
| `relation` | One taxonomy label |
| `shared_anchors` | Shared ontology ids or semantic anchors |
| `specificity_direction` | Helpful for `SUBSUMING` / `SUBSUMED` |
| `rationale` | Brief human-readable justification |
| `confidence` | Agent or reviewer confidence |
| `review_status` | `auto`, `human_confirmed`, `human_rejected` |
| `citation_support_delta` | Whether one side has better citation support |

## Report-level scoring rubrics

The framework should score reports on five dimensions, with claim-level
alignment as the substrate and citation verification as the trust anchor.

### 1. Relevance

Definition:

- how much of the report is truly about the target disease rather than generic
  background, prompt boilerplate, or disease-adjacent filler

Operationalization:

- numerator: weighted claims anchored to the target disease
- denominator: all extracted content claims after boilerplate removal

Suggested rubric:

| Score | Interpretation |
|---|---|
| `4` | Nearly all extracted claims are disease-specific and query-relevant |
| `3` | Mostly disease-specific, with some generic filler |
| `2` | Mixed disease-specific and generic content |
| `1` | Large amount of off-target or template-like material |
| `0` | Report is mostly irrelevant to the disease query |

Typical penalties:

- repeated prompt text
- generic oncology/autoimmunity background unrelated to the target disease
- treatment digressions not tied back to the disease

### 2. Informativeness

Definition:

- how much useful, specific, non-boilerplate information the report provides

Operationalization:

- reward specificity, mechanistic depth, and supported novel claims
- do not reward duplicated restatements or sheer length

Useful subfeatures:

- proportion of claims that are specific rather than generic
- number of distinct semantic frames covered
- number of claims that are more specific than the comparator or gold source

### 3. Accuracy

Definition:

- how often the report's claims are actually supported by evidence and align
  with trusted comparators

Operationalization:

- claim-level accuracy should combine:
  - alignment to comparator (`IDENTICAL`, `CONSISTENT`, `SUBSUMED`, `SUBSUMING`)
  - citation verification
  - contradiction rate

Suggested calculation:

```text
accuracy =
  supported_weight /
  (supported_weight + contradiction_weight + unsupported_false_weight)
```

where "supported" means both semantically supported and citation-supported.

### 4. Completeness

Definition:

- how much of the known disease content a report covers

Operationalization:

- choose a gold source:
  - dismech YAML when available
  - cached review article claims for high-level disease summaries
  - adjudicated union-of-providers gold set for diseases without curated YAML
- compute weighted recall of gold claims

Completeness should be reported both:

- overall
- by claim family:
  - phenotype
  - mechanism
  - treatment
  - cell type
  - anatomy

### 5. Citation quality

Definition:

- whether cited identifiers are real, normalized, and genuinely support the
  claims they are attached to

Submetrics:

- identifier normalization success rate
- identifier resolvability rate
- real-publication verification rate
- claim-support verification rate
- mismatch rate

Suggested rubric:

| Score | Interpretation |
|---|---|
| `4` | Citations normalize cleanly and usually support the attached claims |
| `3` | Mostly good citations with a few unresolved or weak matches |
| `2` | Noticeable citation noise or many low-specificity citations |
| `1` | Many unresolved, wrong, or weakly supportive citations |
| `0` | Citation layer is largely unusable |

### Weighting and aggregation

A practical first aggregate score is a weighted sum:

```text
overall =
  0.20 * relevance +
  0.20 * informativeness +
  0.25 * accuracy +
  0.20 * completeness +
  0.15 * citation_quality
```

Rationale:

- `accuracy` gets the highest weight because confidently wrong reports are worse
  than incomplete ones
- `relevance` and `informativeness` matter because several reports are verbose
  but repetitive
- `citation_quality` should stay visible rather than being hidden inside
  accuracy

Later versions can introduce disease-specific weighting by claim type.

## Publication ID normalization

This belongs upstream in `deep-research-client`, not in dismech-specific eval
logic.

### Problem

Providers cite publications in heterogeneous formats:

- PMID
- DOI
- PMCID
- bare URLs
- title-only mentions
- partial bibliography strings
- local handles or numbered footnotes

Without a normalization layer, two reports may cite the same paper but appear
different, and citation quality metrics will be noisy.

### Recommended upstream capability

`deep-research-client` should expose a generic citation normalization substrate:

```text
normalize_publication_id(raw_citation) -> {
  canonical_id,
  id_type,
  resolved_title,
  resolved_authors,
  resolved_year,
  source_url,
  confidence
}
```

Required behaviors:

- normalize PMID / PMCID / DOI variants
- resolve URLs to canonical ids when possible
- parse partial citation strings
- preserve unresolved raw strings with confidence
- expose hooks for downstream verification

### Suggested upstream issue

Suggested issue title:

- `Normalize heterogeneous publication identifiers across deep research providers`

Suggested acceptance criteria:

- one canonical citation normalization API
- support for PMID, PMCID, DOI, NCT, URL, and partial reference strings
- deterministic output schema
- verification hooks for downstream evaluators
- tests covering cross-provider citation styles

Tracked upstream as:

- `monarch-initiative/deep-research-client#41`

The implementation belongs in `deep-research-client`, not in this repo change.

## Eval execution model

### End-to-end flow

1. Normalize artifacts
   - collapse citation companions
   - assign report mode
   - normalize provider ids
2. Extract claims
   - report claims
   - YAML claims
   - cached review claims
3. Normalize citations
4. Generate candidate alignments
5. Agent adjudicates relation labels
6. Human reviews low-confidence or contradictory cases
7. Aggregate report-level scores
8. Emit dataset-level dashboards and error buckets

### Agent-driven mode

In agent-driven mode, a Claude/Codex evaluator receives:

- two claim tables or two source documents
- candidate claim pairs
- citation metadata
- optional comparator claims from YAML or review articles

Expected output:

- alignment records with relation labels
- unsupported claims on each side
- contradictions flagged for review
- confidence and rationale per pair

This mode scales, but it should not be the only trust layer.

### Human-in-the-loop mode

Human review should sit on top of the agent output, not replace it.

Reviewer workflow:

1. inspect candidate pair
2. inspect source spans and citations
3. confirm / relabel / split / reject
4. mark issue type

Priority review queues:

- contradictions
- unsupported but high-salience claims
- low-confidence ontology grounding
- citation mismatches
- secondary-synthesis reports that appear to inherit claims from parents

### Batch mode

Batch mode should run over all `273` multi-provider diseases.

Recommended batch outputs:

- `claims/*.jsonl` or `claims/*.csv`
- `alignments/*.jsonl`
- `report_scores.csv`
- `disease_summary.csv`
- `review_queue.jsonl`

Recommended batch ordering:

1. start with the `32` diseases having `3+` providers
2. expand to the full `273`
3. add report-vs-YAML where curated YAML exists
4. add report-vs-review where cached reviews exist

### Fairness rules

The batch pipeline should explicitly avoid these mistakes:

- comparing a `source_provider_derived` report against its own
  `source_providers` as if all were independent
- double-counting `*.citations.md` companions
- comparing citation quality before citation ids are normalized
- treating `abstract_only` review caches as full-text completeness gold

## Pilot evaluation

The purpose of the pilot is not to produce final scores. It is to show, on a
few real diseases, what this methodology looks like in practice and which parts
should later become generic functionality in `deep-research-client`.

Counts below are from a manual first-pass extraction of the compared report
slices, not from a full automated report extractor.

### Pilot 1: `Stiff_Person_Syndrome`

- Providers: `cyberian-codex`, `falcon`, `perplexity`
- Compared here: `falcon` vs `perplexity`
- dismech YAML claim rows already available: `65` (from `uv run dismech extract-claims kb/disorders/Stiff_Person_Syndrome.yaml`)
- Manual pilot slice claim counts: `falcon 7`, `perplexity 9`

| Falcon claim | Perplexity claim | Relation | Notes |
|---|---|---|---|
| Anti-GAD65 autoimmunity impairs GABA synthesis and inhibitory signaling | High-titer anti-GAD65 antibodies impair GABA synthesis in 70-80% of classic SPS | `IDENTICAL` | Same core mechanism, different phrasing |
| Intrathecal B-cell activation with oligoclonal bands in 67% and elevated GAD65 index in 85% | Intrathecal GAD65 antibody production with 67% oligoclonal bands and 85% elevated index | `IDENTICAL` | Same quantitative CSF claim |
| Loss of reciprocal inhibition and continuous motor-unit activity drive stiffness/spasms | Disruption of reciprocal inhibition causes co-contraction and continuous motor activity | `IDENTICAL` | Same neurophysiologic claim |
| Anti-GlyR, amphiphysin, gephyrin, and GABARAP define important subsets | Additional targets include GABARAP, amphiphysin, gephyrin, GlyR, and DPPX | `CONSISTENT` | Same antibody landscape; Perplexity adds DPPX |
| Early immunotherapy improves outcomes | Early immunotherapy is associated with better outcomes in cohort data | `IDENTICAL` | Same management/prognosis claim |
| IVIg is first-line and can help about 75% after induction | IVIg is the preferred initial immunotherapy and rituximab is used for refractory disease | `CONSISTENT` | Same treatment lane; Perplexity is less quantitative in the sampled slice |
|  | HLA and KLK10 susceptibility loci may shape risk | `UNSUPPORTED` | Genetic susceptibility appears in Perplexity but not in the Falcon slice |

Interpretation:

- strong agreement on core mechanism
- meaningful asymmetry in depth: Perplexity contributes more immunogenetic detail
- no direct contradictions in the sampled slice

### Pilot 2: `Kniest_Dysplasia`

- Providers: `asta`, `cyberian-codex`, `falcon`, `perplexity`
- Compared here: `falcon` vs `perplexity`
- dismech YAML claim rows already available: `96`
- Manual pilot slice claim counts: `falcon 8`, `perplexity 8`

| Falcon claim | Perplexity claim | Relation | Notes |
|---|---|---|---|
| Heterozygous `COL2A1` variants disrupt type II collagen biosynthesis and ECM assembly | `COL2A1` mutations cause Kniest dysplasia by disrupting type II collagen structure and fibril assembly | `IDENTICAL` | Same disease-gene-mechanism claim |
| In-frame deletions and splice variants interrupt the triple helix and act dominantly | In-frame deletions and splice defects create abnormal alpha-1(II) chains with dominant-negative effects | `IDENTICAL` | Same molecular lesion |
| Mutant procollagen is retained intracellularly with dilated rough ER in chondrocytes | Misfolded type II collagen accumulates in the ER and triggers cell stress in chondrocytes | `IDENTICAL` | Same chondrocyte storage phenotype |
| Sparse, abnormal fibrils produce the classic "Swiss cheese" cartilage | Defective fibrils and matrix degeneration produce the pathognomonic Swiss cheese appearance | `IDENTICAL` | Same tissue-level pathology |
| ER storage is mutation-dependent; some 2024 iPSC models show ER storage without canonical UPR activation | ER stress and UPR activation are treated as a central Kniest mechanism | `CLOSE` | Same topic, but Falcon is more nuanced and mutation-specific |
| High myopia and retinal detachment follow vitreous collagen defects | Severe myopia and retinal detachment arise from abnormal vitreous architecture | `IDENTICAL` | Same ocular complication pathway |
| 2024 iPSC cartilage models suggest failed proteostasis surveillance for some variants |  | `UNSUPPORTED` | New mechanistic detail appears only in Falcon |
|  | Abnormal C-propeptide / chondrocalcin processing contributes to fibril defects | `UNSUPPORTED` | This sampled claim appears only in Perplexity |

Interpretation:

- agreement is strongest on COL2A1, ER retention, and Swiss cheese cartilage
- the important alignment challenge is not contradiction but granularity and
  mechanistic nuance
- this disease is a good stress test for `CLOSE`, `SUBSUMING`, and
  `UNSUPPORTED`

### Pilot 3: `Fanconi_Anemia`

- Providers: `cyberian-codex`, `falcon`, `openai`
- Compared here: `falcon` vs `openai`
- dismech YAML claim rows already available: `592`
- Manual pilot slice claim counts: `falcon 8`, `openai 8`

| Falcon claim | OpenAI claim | Relation | Notes |
|---|---|---|---|
| FA is caused by biallelic defects in the FA/BRCA interstrand crosslink repair pathway | FA is an inherited DNA repair disorder driven by failure to repair DNA interstrand crosslinks | `IDENTICAL` | Same top-level pathogenesis |
| FANCL and UBE2T monoubiquitinate FANCD2-FANCI as the central activation step | The FA core complex monoubiquitinates FANCD2-FANCI through FANCL and UBE2T | `IDENTICAL` | Same pathway-activation claim |
| Endogenous aldehydes are major physiologic genotoxins, and ALDH2 modifies marrow-failure risk | Endogenous aldehydes are relevant stressors and FA cells accumulate damage from them | `CONSISTENT` | OpenAI is broader; Falcon is more specific on ALDH2 |
| HSC attrition under replication stress drives bone marrow failure and pancytopenia | Chromosomal fragility, checkpoint activation, and apoptosis deplete hematopoietic stem cells | `IDENTICAL` | Same bone-marrow-failure mechanism |
| Chronic inflammatory and oxidative environments worsen HSC depletion | Chronic inflammation and oxidative stress accelerate bone marrow failure | `IDENTICAL` | Same systems-level modifier |
| 2024 fetal-liver work links LT-HSC loss to inflammation-driven ER stress and shows TUDCA rescue in model systems |  | `UNSUPPORTED` | Falcon surfaces newer mechanistic detail not seen in the OpenAI slice |
| 2024 HNSCC work links `KMT2D` loss, glycolysis, and epigenetic suppression of FA genes |  | `UNSUPPORTED` | Falcon includes newer cancer-context mechanism |
|  | OpenAI provides broader congenital-anomaly and epithelial-cancer coverage | `COMPLEMENTARY` | OpenAI is more encyclopedic in the sampled slice |

Interpretation:

- the core FA/BRCA pathway is highly concordant across reports
- differences are mostly about recency and specificity, not contradiction
- this disease is a good pilot for comparing "broad review style" vs "recent,
  mechanism-heavy style"

### Loose comparison 4: `Kniest_Dysplasia` report vs dismech YAML

Compared here:

- source `A`: `research/Kniest_Dysplasia-deep-research-falcon.md`
- source `B`: `kb/disorders/Kniest_Dysplasia.yaml`

Loose observations:

- The overlap is strong on the core disease mechanism. The YAML already has
  structured pathophysiology nodes for:
  - defective type II collagen fibril assembly
  - intracellular procollagen retention and ER stress
  - premature chondrocyte apoptosis
  - growth plate dysgenesis
- The Falcon report covers the same mechanism stack in freer prose:
  `COL2A1`, dominant-negative disruption of the triple helix, dilated rough ER,
  Swiss-cheese cartilage, and growth-plate failure.
- In other words, this is not a case where the report and YAML disagree. It is
  a case where the report is more narratively expressive and more mechanistically
  expansive, while the YAML is more claim-atomic and easier to verify.
- The report adds details that look genuinely informative but would need
  explicit handling in any future extractor:
  - exon-specific examples such as exon 12, 15, and 24 effects
  - the distinction between ER storage and canonical UPR activation
  - newer iPSC/proteostasis observations
- The YAML is better on curation discipline. It cleanly separates:
  - pathophysiology nodes
  - phenotypes such as disproportionate short-trunk short stature and enlarged joints
  - evidence snippets attached to those claims
- A useful qualitative judgment here is:
  - relevance: high for both
  - informativeness: report > YAML for mechanistic nuance
  - accuracy/support: YAML easier to trust locally because every claim is already
    decomposed and evidence-linked
  - completeness: mixed; the report is broader mechanistically, the YAML is
    stronger as a structured disease summary

What this example teaches:

- report-to-YAML comparison is a very good testbed because the YAML supplies a
  stable, claim-atomic comparison target
- a future upstream claim extractor should be able to turn a mechanistic
  narrative into something closer to the YAML granularity
- future scoring should distinguish “more detailed than YAML” from “unsupported
  relative to YAML”

### Loose comparison 5: `Fanconi_Anemia` report vs cached review article

Compared here:

- source `A`: `research/Fanconi_Anemia-deep-research-falcon.md`
- source `B`: `references_cache/DOI_10.1186_s13023-025-03896-w.md`

Loose observations:

- The cached review article is `abstract_only`, which immediately changes how it
  should be used. It is a high-level comparator, not a full gold standard.
- The abstract covers the broad claims very cleanly:
  - FA is caused by defects in DNA interstrand crosslink repair
  - this produces genome instability
  - clinically it leads to bone marrow failure, congenital abnormalities, and malignancy risk
- The Falcon report clearly supports and expands those same themes. On the core
  pathogenesis, the report is effectively a `SUBSUMING` source relative to the
  abstract: it includes the broad review claims and then goes deeper into
  pathway structure, aldehydes, ALDH2, fetal HSC biology, and newer mechanistic work.
- This is a good example of why `UNSUPPORTED` has to be interpreted carefully.
  Relative to the abstract, many of Falcon’s extra details have no counterpart,
  but that does not make them suspicious. It just means the comparison target is
  intentionally coarse.
- Citation quality is also different in kind:
  - the review abstract is compact and high-precision
  - the report is much more ambitious and therefore creates more opportunities
    for citation formatting inconsistency, citation overreach, or partial support
- A useful qualitative judgment here is:
  - relevance: high for both
  - informativeness: report >> abstract
  - accuracy/support: abstract is easier to validate at a glance
  - completeness: abstract should not be treated as complete beyond broad disease themes

What this example teaches:

- cached review abstracts are useful sanity-check comparators for high-level
  disease framing
- they are not appropriate as the only target for fine-grained completeness
  scoring
- upstream tooling should explicitly distinguish:
  - broad review alignment
  - fine-grained claim alignment

## What the examples teach us

These three examples are enough to surface the main reusable requirements.

### 1. Claim extraction has to be lightweight but disciplined

The worked examples are possible without a full formal parser, but they are
much cleaner if an upstream library can:

- strip prompt/template scaffolding
- segment a report into candidate claim-bearing spans
- attach nearby citations to those spans
- emit a small canonical claim table

### 2. Alignment is mostly about semantic proximity, not exact string match

Across the examples, the hard cases are:

- same fact, different specificity
- same topic, different framing
- one report being more mechanistically specific than another

That means upstream support should focus on:

- claim pair presentation
- optional ontology anchors
- lightweight relation labeling

not only on lexical similarity.

### 3. Rubric judgment is naturally qualitative first

The examples do support eventual quantitative aggregation, but the first useful
output is a short qualitative judgment:

- what each report gets right
- what it adds
- what it misses
- whether the citations feel trustworthy

That is a better initial target than trying to produce a single definitive
score too early.

### 4. Citation normalization is clearly upstream

Even in these few examples, the same paper may appear as a DOI, URL, PMCID,
footnote, or citation text. That is generic library work, not dismech-specific
logic.

### 5. dismech is best used to supply requirements and benchmarks

What dismech contributes right now is:

- the comparison set
- real reports from multiple providers
- structured YAML comparators
- cached review abstracts
- concrete examples that expose failure modes

That makes it a good place to define the requirements, but not necessarily the
right long-term home for all reusable implementation pieces.

## Upstream recommendations for `deep-research-client`

The eval framework depends on upstream capabilities that should live outside
dismech-specific code.

### 1. Publication ID normalization

Required upstream because it is provider-agnostic and useful for every consumer.

### 2. Standardized claim extraction interface

`deep-research-client` should expose a common claim-extraction contract for
research reports:

- parse frontmatter
- segment body
- extract atomic claims
- attach citations
- emit canonical JSONL

That avoids reimplementing report parsing in every downstream repo.

### 3. Standard report metadata

The current reports already carry useful metadata in frontmatter, but the
library should standardize these fields:

- provider
- provider family
- model
- report mode
- query / disease name
- disease id if known
- timestamp
- citation count
- `source_providers`
- template version
- run id

### 4. Citation verification hooks

The library should expose hooks so downstream evaluators can:

- resolve normalized ids to metadata
- fetch abstracts or cache entries
- run support checks between claim text and cited abstract/title

### 5. Companion-artifact awareness

The library should explicitly model:

- base report
- citation companion
- secondary synthesis

so downstream evaluation can avoid accidental double counting or unfair
benchmarking.

## Recommended implementation sequence

1. Normalize report artifacts and provider/report-mode metadata
2. Build report claim extraction to the same conceptual level as the existing
   YAML `ClaimRow` substrate
3. Add citation normalization upstream
4. Run the three-disease pilot above with human review
5. Expand to the full `32` diseases with `3+` providers
6. Add report-vs-YAML completeness scoring where curated YAML exists
7. Add report-vs-review comparisons for high-level sanity checking

## Summary

The strongest part of the current repo for this eval is already in place:

- a large overlapping multi-provider dataset
- structured YAML gold data
- an existing YAML claim-extraction substrate from issue `#1100`
- cached review abstracts

The main missing layer is a canonical claim-and-alignment substrate for
unstructured reports plus citation normalization upstream. Once that exists,
dismech can move from ad hoc report comparison to reproducible claim-level
evaluation across providers, diseases, and gold standards.
