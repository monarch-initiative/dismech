---
name: mapping-analysis
description: >
  Investigate dismech disease mappings, subtype and grouping alignment, and
  disagreements between MONDO and external ontologies. Use for Boomer runs,
  low-confidence or retracted mappings, ICD mapping scope and direction,
  curated proxy merges, source comparisons, and mapping-correction reports
  or upstream PRs. For binding a term or repairing a label/cache validation
  failure, use dismech-terms instead.
---

# Analyze mappings in dismech

Determine whether the mapped concepts have the same scope, explain the
alternatives, and identify the evidence for a correction. Boomer checks
consistency under supplied constraints and priors; it does not establish
clinical equivalence or infer gene associations.

This skill is self-contained for the dismech workflow. It does not require a
personal `pyboomer` skill. Paths in commands below are relative to the repo root
unless a command explicitly changes directory.

## Start with the question and saved evidence

Identify the disease entry, subtype, grouping, or cross-source mapping at issue.
Read its asserted mapping predicate and intended scope before treating a
different target as an error. A disease family, genetic subtype, phenotype,
susceptibility, and coding category may have similar names but different scopes.

Use the existing artifacts under [analyses/boomer](../../../analyses/boomer/README.md):

| Artifact | What to inspect |
|---|---|
| `index.tsv`, `mendelian.tsv` | Cohort membership, grounding, and saved status |
| `disorders/<slug>/kb.yaml` | Hard constraints, hypotheses, input priors, and labels |
| `disorders/<slug>/solution.yaml`, `solution.md`, `solve.json` | Chosen assignment, probabilities, timeout status, input hash, and solver revision |
| `disorders/<slug>/proxy-merges.json` | Annotation evidence and decisions, where generated |
| `remaining-low-confidence/` | Distinct alternatives, source context, and residual triage |
| `proxy-merges/` | Curated permissions, source catalog, original inputs, and migration manifests |
| `runs/` | Attempt records and comparisons, including failed or incomplete searches |
| `groupings/`, `cross-source/`, `icd10/` | Solver-free membership checks, direct mapping comparisons, and ICD coverage |

An index row or an old `solution.md` is not enough to establish a current
result. Check the input hash, solver revision, and completion status together.
Separate current completed searches, timeouts, stale results, and results from
older solvers when reporting counts or confidence distributions. Compute cohort
sizes from the artifacts; historical README totals are not permanent defaults.

## Establish source context

Collect canonical labels, definitions, relevant parents and children, mapping
qualifiers, and useful gene associations for the entities involved. Include a
sibling subtype when it demonstrates that a parent is broader. Cite the checked
records and relevant literature; label an unverified candidate as such.

- Use OAK for ontology labels and hierarchy. The Boomer analysis uses local
  semantic-sql snapshots, with `OAK_DIR` selecting their directory. Check their
  availability before opening adapters that might download missing builds.
- Keep analysis snapshots separate from `conf/oak_config.yaml`, which governs
  automated term validation and may use live OLS sources. Do not silently mix
  newer labels or hierarchy with older saved inputs.
- Preserve source URLs, versions or commits, and checksums. The MONDO xref
  annotation catalog may be newer than the OAK graph; record both provenances.
- Inspect source qualifiers, not just bare xrefs. A bare xref does not establish
  equivalence. Use the existing grammar-based qualifier extractor for MONDO.
- Keep WHO ICD-10 and ICD-10-CM distinct. Check broad/narrow mapping direction
  from the subject's perspective; do not infer it from labels alone.
- Do not use a mapping-derived `preferred_term` as independent lexical support
  for that same mapping. A bare acronym match also needs an independent signal.

The absence of a hierarchy path is not proof of a contradiction or an ontology
gap. Check definitions, mapping precision, source completeness, and scope before
proposing a retarget. Grouping descendant checks require the appropriate exact
mapping; a broad or narrow mapping does not license the same expectation.

## Use Boomer to expose the competing interpretations

Use the solver when alternative mapping assignments interact with constraints.
For straightforward source comparisons, the grouping and cross-source audits
may suffice. Boomer is loaded from a separate `boomer-py` source checkout via
`BOOMER_SRC`; it is not a dismech runtime dependency. See the
[solver provenance notes](../../../analyses/boomer/patches/README.md) for the
revision used by saved results. Use a clean checkout and record the revision
for new runs.

Distinguish these quantities when explaining a result:

| Quantity | Meaning |
|---|---|
| Input prior | Supplied probability for a mapping before consistency conditioning |
| True/False assignment | Whether one complete solution accepts that hypothesis |
| Mapping marginal posterior | Probability the mapping is true across consistent assignments |
| Whole-solution posterior | Probability of one complete assignment under the model |
| Confidence | `P(best) / (P(best) + P(next best))`, comparing distinct complete solutions |

A confidence of 0.5 means the two best distinct solutions tie. It does not mean
each has whole-solution posterior 0.5, or that an accepted mapping has a low
input prior. For low confidence, show at least the two best distinct solutions
when available and identify their differing mapping choices. Do not count
duplicate search paths as different solutions. For small cases, independently
enumerate complete Boolean assignments to verify solution counts, scores, and
marginals. The existing `investigate_ties.py` and `investigate_remaining.py`
provide examples; inspect their arguments and pinned fixtures before reuse.

Always set a timeout. A timed-out search is provisional, including any reported
confidence. Do not lower clique limits just to obtain a decisive answer:
pruning can discard interacting hypotheses. Report search limitations and
unavailable alternatives instead of implying an exhaustive result.

## Distinguish curated proxy merges from mapping errors

Follow the [implemented proxy policy](../../../analyses/boomer/proxy-merges/README.md).
Automatic exceptions require a live MONDO record, explicit equivalence
annotations on the selected targets, and exactly one preferred external target
among that record's equivalents in the vocabulary, present in the input.
Preference chooses a representative; it does not increase its mapping prior.

In this pipeline, `MemberOfDisjointGroup` supplies non-equivalence, not OWL
class disjointness. Ordinary external `SubClassOf` edges and namespace
non-equivalence are separate constraints. Older saved inputs may encode their
combination as `ProperSubClassOf`; removing a group alone can therefore leave a
strict edge that still prevents a merge.

Keep exceptions specific to supported pairs. Permissions for A/B and B/C do
not imply permission for A/C. Preserve explicit disjointness, curated strict
subtype assertions, unrelated constraints, and mapping priors. Missing preferred
annotations call for review; they are not evidence that the concepts are
biologically distinct. Conversely, a higher score after relaxing a constraint
is not evidence that a disease family should merge with a subtype.

## Report the entities before the IDs dominate the explanation

Lead with the substantive finding in language suited to the reader. For disease
mapping corrections, write for a clinical geneticist. Introduce the entities in
a compact table before discussing individual mappings:

| ID | Source label | Gene context, when useful | Relevant parent or scope |
|---|---|---|---|
| Verified identifier | Canonical label | Checked association or clearly identified subtype context | Named parent or scope distinction |

Use disease names or unambiguous short labels in the prose after the table;
leave IDs available for lookup. Preserve canonical source labels in the table.
Distinguish direct gene annotations from context inferred through child terms,
and make clear that examples of genes in a family are not exhaustive. Mark
missing context as not retrieved, rather than implying no association exists.

Explain three layers separately:

1. **Source context:** what the named records mean and how their scopes differ.
2. **Solver finding:** which named mappings compete, with a small table of the
   choices that differ between distinct solutions and their scores.
3. **Curation judgment:** why the independent source or biological evidence
   supports a particular correction, or what remains unresolved.

For example: TPMT deficiency matches the TPMT-specific poor-metabolism subtype.
The broader category also includes NUDT15-related disease, so equating that whole
category with TPMT deficiency loses a genetic distinction. Check the records for
each investigation; this example illustrates reasoning, not a standing rule.

For PRs, keep the finding, entity table, and proposed correction visible. Put
detailed assignments, priors, marginal and whole-solution probabilities,
constraints, source versions, and validation in an expandable
`<details><summary>Boomer evidence and validation</summary>` section. A multi-case
summary should compare the named cases and link directly to their entity tables.
Use [github-communication](../github-communication/SKILL.md) before posting.

## Regenerate only the necessary artifacts

Recipes live in [analyses/justfile](../../../analyses/justfile), not the root
justfile. Run `cd analyses` before these commands; inspect `just --show` for the
exact invocation and `just check-deps` for required local sources.

| Intent | Recipe | Effect |
|---|---|---|
| Inspect one saved input with a bounded solve | `just boomer-solve <slug> 60` | Prints an analysis without regenerating saved inputs |
| Fill missing labels | `just boomer-labels` | Preserves facts, priors, and saved solutions |
| Regenerate one disease | `just boomer-one <slug>` | Rebuilds its input and result from current sources |
| Add Mendelian inputs | `just boomer-expand-mendelian` | Adds inputs marked `NOT_RUN`, preserving existing indexed results |
| Solve pending saved inputs | `just boomer-solve-pending 60 2` | Checkpoints `NOT_RUN` and `STALE_INPUT` results |
| Summarize confidence or ICD coverage | `just boomer-confidence`, `just boomer-icd10-coverage` | Refreshes the respective summaries |
| Check grouping or direct mapping alignment | `just boomer-groupings`, `just boomer-cross-source` | Regenerates solver-free audit reports |

Full regeneration can change thousands of files as KB entries, source graphs,
annotations, and serialization evolve. Prefer one case or a scoped migration
for a focused investigation. Label-only enrichment is idempotent against fixed
snapshots. Input migrations must retain baselines and mark old solutions stale;
never rewrite historical hashes to conceal changes. Follow the proxy and ICD
migration READMEs before invoking their recipes. Historical retry recipes name
specific cohorts and are not generic next-run commands.

Validate changed code with the applicable `tests/test_boomer*.py` tests. Supply
`BOOMER_SRC` to exercise actual-solver checks; otherwise report those skips.
For content-only investigations, verify source identities, scores, artifact
hashes, and the scope of the diff rather than adding tests for prose.

Keep proposed corrections separate from applied changes. When upstream fixes
are requested, start from a fresh upstream checkout, follow that repository's
editing instructions, and make independent PRs for independent cases. A dismech
binding change also uses [dismech-terms](../dismech-terms/SKILL.md); a grouping
edit uses [curate-grouping](../curate-grouping/SKILL.md). Analysis findings alone
do not authorize publishing upstream changes.
