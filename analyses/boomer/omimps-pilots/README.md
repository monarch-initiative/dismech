# OMIM phenotypic series: five joint mapping pilots

These pilots combine series membership with disease and subtype mappings while
keeping the clinical reason for each grouping explicit. They compare frozen
pre-curation records with the reviewed curation commits; they do not require the
curation PRs to be merged. The existing per-disease Boomer inputs and results are
unchanged.

## Findings

| Pilot | Representation and classification rationale | Member coverage in the pinned snapshots | Curation |
|---|---|---|---|
| [Bardet–Biedl syndrome](bbs/README.md) | One syndrome-level disease maps exactly to the PS. Four gene-level ciliopathy subtypes have narrower mappings to numbered BBS conditions. | 22 source members; four have broader-scope subtype coverage, 18 have no grounded or explicitly mapped candidate in this audit. No numbered member is covered by an exact primary/subtype grounding. The family mapping does not close those gaps. | [#18390](https://github.com/monarch-initiative/dismech/pull/18390) |
| [Lysosomal acid lipase deficiency](lal/README.md) | A grouping joins Wolman disease and cholesteryl ester storage disease. Shared LIPA deficiency explains the grouping; severity and onset distinguish the existing entries. This is not a series of different causal genes. | Both of the two source members already have individual entries. The grouping adds their shared spectrum. | [#18652](https://github.com/monarch-initiative/dismech/pull/18652) |
| [cblE/cblG/cblD-HC](cbl/README.md) | A grouping joins defects in the same remethylation pathway: MTRR-dependent reactivation, MTR catalysis, and MMADHC-dependent cofactor handling. Only the isolated-homocystinuria cblD-HC subtype belongs. | All three source members have candidates. The grouping resolves cblD-HC to MONDO:0700297, not the broader MMADHC entry or its methylmalonic-aciduria siblings. | [#18648](https://github.com/monarch-initiative/dismech/pull/18648) |
| [Maple syrup urine disease](msud/README.md) | The PS remains a **related** mapping. Its DLD member has a broader biochemical scope; the DisMech entry also includes a BCKDK-related biochemical phenotype. | Across the KB, primary/subtype grounding covers four of five source members before curation and five afterward, through the new PPM1K-related mild subtype. DLD is represented as E3 deficiency in the pyruvate dehydrogenase deficiency entry, not newly added as an MSUD subtype. | [#18649](https://github.com/monarch-initiative/dismech/pull/18649) |
| [Paroxysmal nocturnal hemoglobinuria](pnh/README.md) | A non-Mendelian family with distinct PIGA and PIGT mechanisms. Series membership does not impose a Mendelian inheritance model. | Before: two directional mappings. After: both numbered members have grounded subtypes, and PNH2 has a dedicated entry. Its `curated_in` pointer resolves to the same entity, avoiding duplicate PNH2 nodes. | [#18663](https://github.com/monarch-initiative/dismech/pull/18663) |

The five cases add **two groupings**, not five. They demonstrate why a PS coverage
target must distinguish family mappings, explicit grouping membership, scoped
subtype coverage and separate disease entries. The coverage totals are based on
the January 2026 OMIM snapshot, not a claim about today's entire OMIM catalog.

The grouping rationales and evidence are retained in each `projection.json`.
The necessary phenotype/gene criteria in the two grouping records are annotation
checks, not sufficient classifiers or patient diagnostic rules. Boomer does not
test those biological criteria; it tests the mapping and hierarchy consequences.

## What the solver can and cannot settle

Each linked case has before/after results, a named source-entity table, complete
mapping assertions and logical edge provenance, and independently enumerated
alternatives. **All ten models completed exhaustive Boolean enumeration and
accept every mapping hypothesis in their optimal assignment**, with confidence
0.90. The five normal-search timeouts (BBS before/after, cbl before/after, MSUD
after) remain visibly marked; their partial probability outputs are superseded
for interpretation by the complete `enumeration.json` results, not rewritten.
The other five normal searches agree with enumeration on every checked quantity.

This does not demonstrate a conflict resolved by the new PS mappings: the five
before models are also consistent. The concrete gains are explicit family/group
alignment, preserved subtype boundaries and the MSUD/PNH coverage improvements.
Different assignment counts or whole-solution posteriors across the before/after
models reflect their different hypotheses and are not measures of curation quality.

The new inputs deliberately cover **MONDO, numbered OMIM records and OMIMPS**.
All selected records' grounded subtypes participate jointly, including siblings
outside a grouping when they help preserve the parent's scope. All OMIM members
of the selected PS appear as structural context. External vocabularies such as
MeSH, ICD and DOID are outside this pilot solver scope; their historical results
are retained separately in [historical-baselines.json](historical-baselines.json).

Coverage scans primary/subtype groundings across the entire pinned KB, while the
solver includes the selected family/grouping records and their explicit member
or `curated_in` dependencies. For example, finding the DLD candidate elsewhere
does not import the whole pyruvate dehydrogenase deficiency entry into the MSUD
model or assert that DLD deficiency is a curated strict MSUD subtype.

In those saved, hash-checked inputs, **Wolman still has a MeSH tie** at confidence
0.5 ([alternatives](../remaining-low-confidence/Wolman_Disease-alternatives.md)).
The new LAL grouping does not resolve or retest that conflict. **cblE already
accepts its DOID proxy mappings**, at confidence 0.9, following the earlier
annotation-supported proxy migration
([alternatives](../proxy-merges/alternatives/Methylcobalamin_Deficiency_Type_cblE-alternatives.md)); that improvement is not attributable to
the new PS grouping. BBS has a completed saved result. MSUD lacks `solve.json`
and is treated as legacy output, while PNH and PNH2 have no saved per-disease
analysis. These are baselines of older inputs, not results on the new curation.

MONDO itself maps the MSUD family exactly to the PS. This source hypothesis is
visible alongside the curated `relatedMatch`, which contributes **no equivalence
axiom**. A weak SKOS mapping is not a logical negation of equivalence, so a
consistent assignment can still infer equivalence through MONDO. The compiler
does not silently strengthen the curated assertion, and solver consistency
cannot establish that the scopes are clinically interchangeable. This is a
scope-review flag, not sufficient evidence for an upstream correction.

## Modeling assumptions

- Primary disease/subtype term bindings are equality **hypotheses**, with prior
  0.90. Explicit exact mappings and MONDO snapshot `skos:exactMatch` assertions
  have prior 0.95. These are supplied assumptions, not measured probabilities.
- `broadMatch` means the curated subject is a subclass of the target;
  `narrowMatch` reverses that direction. Both use an ordinary subclass hypothesis
  at prior 0.95. `relatedMatch`, `closeMatch` and unspecified mappings are retained
  as annotations and do not entail equality, subclassing or non-equivalence.
- Repeated assertions of the same logical mapping retain all provenance but
  contribute one hypothesis. Different mapping paths can still be dependent
  (especially OMIM-derived MONDO PS mappings); their probabilities must not be
  interpreted as independent biological corroboration.
- Curated subtype edges are strict; grouping-member edges and source hierarchy
  edges are ordinary subclass assertions. A grouping's complete OWL union is
  not encoded: the solver tests the forward member-inclusion consequences only.
- Distinct records within each of MONDO, OMIM and OMIMPS receive namespace
  non-equivalence assumptions. These are not OWL class disjointness. OMIM and
  OMIMPS identifiers remain separate even when they share six digits. Explicit
  MONDO disjointness is retained where both terms occur in the input.
- Missing source hierarchy paths never become negative assertions. Coverage
  candidates come from explicit MONDO exact matches to numbered OMIM records;
  they do not establish clinical equivalence independently of those mappings.
  Directional mappings are displayed separately. Multiple candidate entries or
  embedded subtypes are retained rather than counted as multiple OMIM members.
- Confidence compares the best two **distinct complete assignments**. Mapping
  marginal probabilities and whole-assignment posterior probabilities are
  different quantities. Search outputs report all three; confidence is not a
  validation score for the grouping's biological rationale.

## Frozen sources and reproduction

[sources.json](sources.json) records full SQLite SHA-256 checksums and version
IRIs: MONDO **2026-09-01**, OMIM **2026-01-09**. These analysis snapshots are
separate from live term-validation sources. No MONDO xref proxy annotation
catalog or unqualified database cross-reference is imported into these inputs.

Each case's projection records the exact DisMech commits, source paths and full
original YAML blob SHA-256 hashes, selected curation fields, source labels,
mapping assertions and relevant hierarchy. BBS uses the parent and result of
its original merged pilot. The other four use the common pre-curation base
`bef670f17076625c96e5e8955a0a83d2d5108257` and the reviewed PR heads. The PNH
comparison therefore includes all review fixes, not just its final commit.

Use a **clean** Boomer checkout at
`744038e30741009930f57919ca2f03c6473ed198`, which includes the distinct-assignment
probability correction. From the repository root:

```bash
export BOOMER_SRC=/path/to/clean/boomer-py/src
cd analyses
just boomer-omimps build
just boomer-omimps solve 60
just boomer-omimps verify 60
just boomer-omimps report
```

These stages use the committed projections and do not need SQLite databases or
unmerged curation branches. `capture` is a separate source-refresh operation;
it needs the pinned source git objects and the two local databases selected by
`OAK_DIR`. It must not be confused with simply rerunning the frozen experiment.

Each solver worker has a 60-second search limit and a 75-second supervisor
deadline. Hypothesis, candidate and iteration caps do not truncate the search;
no hypotheses are dropped to obtain a result. Independent enumeration examines
every Boolean assignment for inputs with at most 15 hypotheses, under its own
60-second wall-clock deadline. It uses Boomer's same reasoner through a separate
enumeration procedure. For completed normal searches it compares solution counts,
optimal assignments, confidence, whole-solution posterior and every mapping
marginal with the saved result. For incomplete normal searches it records the
full enumerated result separately. All ten enumerations completed in this run.

An additional bounded check certifies the optimum and a distinct runner-up
without needing all marginals. All input priors exceed 1/2, so the all-true
assignment has the highest possible unconditioned weight. A satisfiable single
flip of a minimum-prior hypothesis attains the upper bound on the weight of any
different assignment. Both assignments are checked by the reasoner and saved in
`certificate.json`; the check declines to certify a runner-up if these sufficient
conditions do not hold. These certificates agree with enumeration in all ten
models. They alone do not compute marginal or whole-assignment probabilities.

Regression checks:

```bash
BOOMER_SRC=/path/to/clean/boomer-py/src uv run pytest -q tests/test_boomer_omimps.py
```

The compiler checks subtype scope, alias identity, mapping direction and
non-entailing related mappings. Artifact tests rebuild the frozen inputs and
check that result hashes match. Tests do not rerun expensive searches in CI;
the bounded `verify` stage records the actual-solver cross-checks separately.
