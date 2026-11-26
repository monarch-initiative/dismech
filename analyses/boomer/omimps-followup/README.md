# Five further OMIMPS mapping pilots

The broader Boomer investigation has already produced merged MONDO corrections
for **Gorlin syndrome** and **PRAAS**. The first five OMIMPS pilots introduced no
additional mapping corrections. This follow-up uses those two source repairs as
positive controls, tests the still-open TPMT proposal, repairs an analysis
compiler error exposed by FOXE3, and checks a susceptibility-series boundary in
Waldenström macroglobulinemia.

These are controlled interventions, **not pre/post-curation comparisons**.
Each pair holds the curated record fixed at its pinned PR commit. Gorlin and
PRAAS change the selected source DO mappings; TPMT tests a proposed source
change; FOXE3 changes compiler behavior; Waldenström weakens a source assertion
as a sensitivity experiment. The three new DisMech PS mappings are already
present on both sides of their respective comparisons.

## Cases and curation outcomes

| Case | Scope and classification rationale | Applied or proposed action |
|---|---|---|
| [Gorlin syndrome](gorlin/README.md) | A syndrome family containing PTCH1- and SUFU-related disorders; a gene-specific subtype is not the whole family. | Earlier Boomer-driven [MONDO correction merged](https://github.com/monarch-initiative/mondo/pull/10628). Existing [DisMech exact PS mapping](https://github.com/monarch-initiative/dismech/pull/18572) held fixed. |
| [PRAAS](praas/README.md) | Proteasome dysfunction unites an autoinflammatory family; PRAAS1 is one of six enumerated subtypes. | Earlier Boomer-driven [MONDO correction merged](https://github.com/monarch-initiative/mondo/pull/10629). New [exact PS mapping](https://github.com/monarch-initiative/dismech/pull/18678). |
| [TPMT deficiency](tpmt/README.md) | TPMT-related poor thiopurine metabolism belongs to a drug-response series that also includes NUDT15-related metabolism. | New [broad PS mapping](https://github.com/monarch-initiative/dismech/pull/18679). Existing [MONDO correction proposal remains open](https://github.com/monarch-initiative/mondo/pull/10630); the after model tests it without publishing or applying it upstream. |
| [FOXE3 spectrum](foxe3/README.md) | A gene-based spectrum intersects a phenotype-based series: aphakia is shared; the entry also includes cataract 34 and the series includes other genes. | New [related PS mapping](https://github.com/monarch-initiative/dismech/pull/18680). Fix the pilot compiler to honor the existing broad MONDO mapping instead of injecting an implicit equality. |
| [Waldenström macroglobulinemia](waldenstrom/README.md) | The malignancy and its somatic mechanisms are distinct classification scopes from numbered inherited-susceptibility records. | Keep the existing [related PS mapping](https://github.com/monarch-initiative/dismech/pull/18644). Removing MONDO's PS equivalence is a sensitivity experiment only, not an adjudicated upstream correction. |

This batch adds **three missing PS mappings and no new grouping records**.
PRAAS is already a disease umbrella with embedded subtypes. The TPMT and FOXE3
entries cover narrower or overlapping scopes, so forcing exact PS coverage would
misrepresent them. Waldenström demonstrates why a PS is not automatically a
Mendelian disease family. A related mapping is neither an equality nor a logical
assertion that equality is false.

## Source entities behind the family/subtype conflicts

Canonical labels below come from the pinned current OBO sources. Gene context
comes from DO definitions or the curated entry, not from Boomer inference.

| ID | Source label | Gene context / scope |
|---|---|---|
| MONDO:0007187 | nevoid basal cell carcinoma syndrome | Gorlin family |
| MONDO:0958174 | basal cell nevus syndrome 1 | PTCH1-related subtype |
| DOID:2512 | nevoid basal cell carcinoma syndrome | Family containing the two following subtypes |
| DOID:0070365 | nevoid basal cell carcinoma syndrome 1 | PTCH1; child of DOID:2512 |
| DOID:0070366 | nevoid basal cell carcinoma syndrome 2 | SUFU; child of DOID:2512 |
| MONDO:0009726 | proteosome-associated autoinflammatory syndrome | PRAAS family; source spelling retained |
| MONDO:0054698 | proteasome-associated autoinflammatory syndrome 1 | PRAAS1 subtype |
| DOID:0060913 | proteasome-associated autoinflammatory syndrome | Family |
| DOID:0050553 | proteasome-associated autoinflammatory syndrome 1 | PSMB8 and specified digenic forms; child of DOID:0060913 |
| MONDO:0012503 | thiopurine S-methyltransferase deficiency | TPMT-specific |
| MONDO:0000210 | thiopurine metabolic disease | Broader PS-aligned family |
| DOID:0061004 | poor metabolism of thiopurines 1 | TPMT; child of DOID:0080172 |
| DOID:0060996 | poor metabolism of thiopurines 2 | NUDT15; child of DOID:0080172 |
| DOID:0080172 | poor metabolism of thiopurines | Family containing TPMT and NUDT15 subtypes |
| MONDO:0019503 | anterior segment dysgenesis | Broad developmental eye-anomaly family; not a FOXE3-specific identity |
| MONDO:0100280 | Waldenstrom macroglobulinemia | Malignancy; numbered PS member labels explicitly concern susceptibility |

Definitions, parent links, complete selected stanzas, and current MONDO mapping
qualifiers are in [source-context.json](source-context.json). Each linked case
also lists every numbered PS member and its source label. The old Gorlin/PRAAS
models use the September 2026 MONDO SQL DO assertions; their after models use
explicit `MONDO:equivalentTo` qualifiers from the pinned current source.
The move from a family to its subtype follows source definitions and hierarchy,
not a preference for whichever branch the solver happens to retain in a tie.

## Surprises and remaining coverage

- **A consistent result can conceal a scope error.** The legacy FOXE3 compiler
  supplied primary-grounding equality at prior 0.90 even though curation
  explicitly said `broadMatch`. The corrected compiler lets that qualifier
  govern the grounding. It preserves broad/narrow direction and keeps related
  and close mappings non-entailing; incompatible qualifiers fail loudly.
  The first five pilots' logical inputs and audits reproduce unchanged; their
  frozen artifact files are untouched. Label serialization is now sorted so
  new builds also reproduce byte-for-byte across Python hash seeds.
- **Weak mappings do not veto source-derived identity.** Waldenström's curated
  related mapping can coexist with MONDO's PS equivalence. Testing removal of
  that equivalence demonstrates the limitation; it does not adjudicate the
  intended scope of the source series.
- **A family mapping does not fill member gaps.** In the pinned whole-KB audit,
  Gorlin has candidates for both members (two existing individual entries),
  PRAAS for all six (embedded subtypes), TPMT for one of two, FOXE3 for one of
  eight, and Waldenström for neither of its two susceptibility records.
  These are mapping-based candidates, not independently established clinical
  identities. The ten unmatched records are a review queue, not ten confirmed
  missing diseases: other entries may cover them without an exact grounding.
- **PRAAS6 remains a biological classification question.** The existing entry
  records the proposal to distinguish PRAAS-ID from classic PRAAS. Exact PS
  alignment describes the current six-member umbrella and does not settle that
  debate, impose one inheritance mode, or turn proteasome dysfunction into a
  sufficient diagnostic classifier.

## Solver results

All ten models completed exhaustive enumeration. Normal search completed eight;
the two 17-hypothesis PRAAS searches timed out and retain that status. Their
complete enumeration results supply the probabilities used here.

| Case | Before: best/next confidence | After: best/next confidence | Interpretation |
|---|---:|---:|---|
| Gorlin | 0.50 | 0.95 | Old family/subtype DO exact mappings compete; moving the subtype mapping to the subtype removes the conflict. |
| PRAAS | 0.50 | 0.90 | The same family/PRAAS1 conflation is resolved by the merged source change. |
| TPMT | 0.50 | 0.90 | Both current DO exact mappings cannot hold together; the proposed directional family mapping resolves this model. |
| FOXE3 | 0.90 | 0.90 | Both models are consistent, including the erroneous implicit equality. Respecting curated scope is necessary independently of consistency. |
| Waldenström | 0.90 | 0.90 | Both models are consistent; a related mapping does not prevent identity inferred through MONDO. |

In each of the three tied before models, the two best complete assignments reject
opposite DO exact mappings. Both hypotheses have prior 0.95. The solver cannot
choose the clinically correct branch from those equal priors alone. Each case
report names the differing hypotheses and records their marginal probabilities,
whole-assignment posteriors and complete alternatives. Every after model's
optimal assignment accepts all its hypotheses. Different model dimensions and
constraint sets mean their posterior scores are not curation-quality metrics.

The cheap all-true certificate cannot certify Gorlin's best runner-up: its sole
minimum-prior grounding cannot be flipped alone while both redundant exact paths
remain true. Full enumeration does find the next-best assignment, at confidence
0.95. That distinction is preserved rather than replacing the certificate with
a stronger claim than its algorithm proves.

## Modeling and reproducibility

[Sources](sources.json) records full SQL hashes (MONDO 2026-09-01; OMIM
2026-01-09), current MONDO and DO commit URLs and hashes, and the whole-KB
coverage base. Curation projections pin each original YAML blob and commit.
Current source annotations are deliberately separate from the older SQL
hierarchy. These are scoped mapping interventions, not full ontology refreshes.
Gorlin/PRAAS use historical versus current DO mappings; TPMT uses current DO
mappings versus the existing proposed repair. The family/subtype context and
all non-DO mapping hypotheses are held fixed within each of these pairs.

The common compiler follows the [first pilot assumptions](../omimps-pilots/README.md).
This extension adds selected DOID mappings and namespace non-equivalence for
DOID. Namespace non-equivalence is **not OWL disjointness**. The DO parent and
child pairs here are supported as distinct scopes by their definitions and
sibling context; no proxy exception is applied. Missing hierarchy paths never
become negative facts. Whole-KB coverage candidates are not automatically
imported as additional disease hypotheses.

Explicit qualifiers now govern the primary or subtype grounding at its usual
prior 0.90. Separate exact/directional mappings and source equivalences use
0.95; repeated logical assertions are deduplicated, not independent evidence.
For FOXE3 the legacy model has implicit equality at 0.90 and explicit subclass
at 0.95; the corrected model has one qualified grounding at 0.90. This is a
compiler-behavior comparison, not a claim that an improved probability measures
better biology. The standalone FOXE3/ICD analysis is not rerun here.

Use a clean Boomer checkout at
`744038e30741009930f57919ca2f03c6473ed198`:

```bash
export BOOMER_SRC=/path/to/clean/boomer-py/src
cd analyses
just boomer-omimps-followup build
just boomer-omimps-followup solve 60
just boomer-omimps-followup verify 120
just boomer-omimps-followup report
```

The frozen stages need no ontology databases or unmerged curation branches.
A separate `capture` operation requires the pinned git objects and SQL files,
plus `--source-dir` containing `mondo.obo`, `doid.obo`, and the manifest recorded
under `sources.json.current_obo`. It verifies the source-file hashes before
reading them. It is not part of simply reproducing the frozen experiment.

Normal search has a 60-second limit and a 75-second supervisor deadline.
Independent complete Boolean enumeration has a 120-second deadline per model
and an 18-hypothesis cap; the largest selected model has 17. No hypotheses are
pruned to get a decisive answer. Both procedures use the pinned Boomer reasoner.
Each result is linked to its input hash; timeouts retain their status and are
not reported as complete searches. Confidence compares the two best distinct
assignments; mapping marginals and whole-assignment posteriors are separate.
These are supplied model probabilities, not empirical clinical confidence.

Validation from the repository root:

```bash
BOOMER_SRC=/path/to/clean/boomer-py/src uv run pytest -q tests/test_boomer*.py
```

Tests rebuild frozen inputs, verify result hashes, check the actual reasoner's
all-true consistency before and after, and ensure source interventions hold
other hypotheses fixed. They also preserve the first five pilot fixtures.
