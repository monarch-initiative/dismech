# How diet is represented in dismech — audit, 2026-09-01

Diet enters a dismech entry two ways, and they are **separate claims that happen
to share an ontology**:

| | Where it lives | Grounded by | Reaches the pathograph via |
|---|---|---|---|
| **Causal** | `environmental[]` | `food_source` (FOODON/CHEBI), `exposure_term` (ECTO/XCO) | `influences_mechanisms` |
| **Intervention** | `treatments[].treatment_term` | `dietary_modifications` (action + FOODON/CHEBI food) | `target_mechanisms` |

Phenylketonuria already carries both against the same `FOODON:00001006`: meat as
an exposure, and `RESTRICT` meat as a prescription. That is not duplication to be
factored out — an exposure claim and a prescription claim are different
assertions with different evidence. The audit therefore never reconciles the two
tracks against each other.

Reproduce with `just diet-audit` (`--format tsv` for the per-entry table).
Figures below were last regenerated against `main` on 2026-09-05; the KB moves,
so re-run rather than quoting these.

## Headline

The gap that matters is **evidence-backed diet annotations that never reach the
mechanism graph**, not unbound terms.

| | Causal | Intervention |
|---|---|---|
| Diet-related entries | 191 in 139 files | 648 in 474 files |
| On the pathograph | 139 (72.8%) | 331 (51.1%) |
| **Cited but off the pathograph** | **50** (38 after dropping weak matches) | **282** |
| …of those, `CITED_HUMAN` | 36 | 223 |
| On the pathograph but uncited | 0 | 3 |
| Evidenced only by `REFUTE` | 1 | 10 |

The causal track is in good shape: nearly three quarters of its diet entries
already carry `influences_mechanisms`, and the residue is 38 entries — a
reviewable list, not a programme. The intervention track is the weaker half: half
of dietary treatments never link to a mechanism node, leaving 282
cited-but-unlinked treatments.

**Three entries are on the pathograph with no evidence anywhere** — the dietary
protein restriction in Chronic Kidney Disease, the ketogenic diet in Dravet
syndrome, and the threonine restriction in Inherited Threoninemia. All three are
interventions; the causal track has none. They already render as mechanism edges,
so they assert more than the KB can support.

An earlier draft of this report put that number at 19. It was wrong: the audit
graded only the entry's own `evidence:` block and never looked at the evidence on
the link itself, which is where CLAUDE.md says the claim "this exposure acts on
this node" belongs. Sixteen of the other entries carry snippet-backed `SUPPORT`
there, including all three `kb/modules/` entries the draft singled out as the
worst case. `--strict` would have sent a curator to fix entries that were already
right — the same failure mode as the `REFUTE_ONLY` bug below, one layer up. The
gap counts are unaffected, since an unlinked entry has no links to read.

`REFUTE_ONLY` is counted separately and is **not** a defect. NELABA's "Lipoic acid
supplementation (ineffective)" carries two snippet-backed `REFUTE` items against
the mechanism it targets: a treatment recorded as failing against a node is a
real, useful annotation, and an earlier draft of this audit wrongly flagged it as
uncited.

### The 38 strong causal candidates

Concentrated in entries where diet is central: Gout (beer, fructose-sweetened
soft drink, red/organ meat, shellfish — all `CITED_HUMAN`, none linked),
Phenylketonuria (dairy, meat, nuts), Celiac Disease (gluten, wheat, barley, rye),
plus alcohol across eleven carcinoma, hepatic and cardiovascular entries, and
single entries in Hyperlipidemia (high saturated fat), Obesity and Type 2
Diabetes (high-calorie diet), Osteoporosis (vitamin D deficiency), Scurvy
(vitamin C deficiency), Thyroid Follicular Carcinoma (iodine deficiency), and
Wilson Disease (dietary copper).

A `CITED_HUMAN` row is a candidate, not a verdict. Most of these citations are
observational cohort associations, and an association is not a mechanism — read
the snippet before drawing an edge. Gout's shellfish evidence, for instance,
measures *incident gout* in a cohort rather than precipitation of a flare, which
its own `explanation` already says.

## Ontology binding — the secondary axis

| State | Causal | Intervention |
|---|---|---|
| `BOUND` | 120 (62.8%) | 3 (0.5%) |
| `PARTIAL` (block present, no `term:`) | 5 | 2 |
| `FREE_TEXT` | 66 (34.6%) | 643 (99.2%) |

`dietary_modifications` is effectively unused: 5 files in the whole KB (Celiac,
ECHS1 Deficiency, Konzo, Lathyrism, Phenylketonuria), 11 modification records,
against 648 dietary treatments. Only 19 FOODON bindings exist KB-wide across 11
distinct terms.

**Free text is a legitimate outcome, not a backlog.** Two structural reasons, and
neither is a curation failure:

1. **`FoodTerm` excludes food components.** It is reachable only from
   `FOODON:00001002` (food product) and `CHEBI:33284` (nutrient). Gluten
   (`FOODON:03420177`) sits under `food material` instead and is correctly
   rejected. `conf/oak_config.yaml` confirms that exclusion is intended
   behaviour rather than an adapter artifact — it uses two other `food material`
   terms as worked examples of CURIEs both adapters agree are not `FoodTerm`
   values. So Celiac's three grain vehicles are bound while its actual trigger,
   "Gluten Exposure", cannot be. The same will apply to casein, purines, and
   oxalate.
2. **Dietary patterns have no ontology home at all.** FOODON describes food
   products, not eating patterns.

Where no term fits, free text is the right answer per `.claude/skills/dismech-terms`
— *no term beats a bad one*. The audit reports `FREE_TEXT` as a state to review,
never as an error.

Worth noting separately: **47 causal entries are pathograph-linked *and* free
text**, so they render as ungrounded nodes in an otherwise grounded graph. That
is the subset where a binding, if a good one exists, buys the most.

### Dietary-pattern CURIE scatter

The same pattern concept is bound inconsistently across entries:

```
alcohol:  ECTO:0001082 x12, ECTO:0300001 x1, ECTO:0000509 x1
dietary:  ECTO:0090010, ECTO:9000950, ECTO:9000084, FOODON:03303171, ECTO:0400019
diet:     ECTO:0090010 x3, XCO:0000013 x1, ECTO:9001347 x1
```

`XCO:0000013` is a bare "diet" catch-all used where a specific pattern was meant.
Alcohol is the healthy case — `ECTO:0001082` dominates, with `ECTO:0300001`
correctly reserved for the maternal route and a single `ECTO:0000509`.

Standardizing on one ECTO CURIE per named pattern is the cheap win here, and
needs no schema change.

## Treatment-side inconsistency

Dietary treatments scatter across NCIT action terms — `NCIT:C15747` (supportive
care), `NCIT:C15447` (dietary intervention), `NCIT:C15433` (nutritional support),
`NCIT:C15986` (pharmacotherapy) — and **235 of 648 carry no
`therapeutic_modality` at all**, with 244 `BEHAVIORAL` and 106 `SMALL_MOLECULE`.

Do not mechanically backfill this. CLAUDE.md already records that
`NCIT:C15433` names a specific vitamin or compound far more often than a diet
change, and that tagging it `BEHAVIORAL` was tried and reverted in 2026-07.

## Method and its limits

Entries are matched by keyword, so the census is recall-oriented and carries a
false-positive tail. Two mitigations, both visible in the output:

- **The two tracks read different fields.** An `environmental[]` entry is short
  and wholly about its exposure, so its description is signal. A `treatments[]`
  description is a clinical paragraph that mentions diet incidentally — searching
  it pulled in ACE inhibitors (on "sodium"), cleft palate repair (on "feeding"),
  and beta blockers. The intervention track therefore matches `name` only, which
  cut it from 1,244 entries to 648.
- **Match provenance is recorded** (`matched_in`: `food_source` / `name` /
  `term_label` / `description`). A causal entry matched only in description prose
  is the weak tail — 12 of the 50 causal gap rows, including Ependymoma
  ("high-dose ionizing radiation", whose description mentions diet) and CKD
  tobacco smoking (on "glycemic"). Filter with `--strong-only`.

Bare `sodium` was dropped from the keyword list: adding it back pulls in 40 more
entries that are almost all drugs (sodium channel blockers, sodium valproate,
sodium phenylbutyrate, sodium oxybate), and every genuinely dietary one carries
"diet"/"dietary"/"salt"/"intake" anyway.
`septal ablation`, `vitamin K antagonist`, and `radioactive iodine` are excluded
by name.

**Evidence tiers are structural, not a quality judgment.** The script cannot read
a paper; it reports the shape of the citation. `CITED_HUMAN` means a `SUPPORT`
item with a non-empty snippet graded `HUMAN_CLINICAL`. Snippet-backed `REFUTE`
evidence takes its own `REFUTE_ONLY` tier: it never counts toward the gap, since
refuting evidence is not a reason to draw an edge, but it is emphatically not an
uncited link either.

## Recommendations

Ordered by value per unit of work. None is started; all are decisions for a
curator, not automated fixes.

1. **Cite or unlink the three uncited pathograph edges** (Chronic Kidney Disease,
   Dravet syndrome, Inherited Threoninemia). They already render.
2. **Work the 38 strong causal candidates**, reading each snippet before adding
   `influences_mechanisms`. Gout, Phenylketonuria, and Celiac Disease alone are 11
   of them and are the natural pilot, since all three already model diet well on
   the other track. A first tranche is already proposed separately in
   [PR #10359](https://github.com/monarch-initiative/dismech/pull/10359), which
   works 42 candidates from an earlier run of this audit and adds 19 of them;
   merging it will shrink this list.
3. **Standardize the dietary-pattern CURIEs**, one ECTO term per named pattern,
   retiring the bare `XCO:0000013` catch-all.
4. **Widen the `FoodTerm` root** to admit the FOODON `food material` branch, so
   food components (gluten, casein) become bindable. This is a schema change with
   a cache rebuild, and needs its own decision-register entry. Note that *why*
   the root was drawn at `FOODON:00001002` is not recorded anywhere —
   `conf/oak_config.yaml` documents only that the resulting exclusion is
   intended, not the reasoning behind the root itself. That missing rationale is
   a reason to take the decision deliberately, not a licence to widen it.
5. **Leave `dietary_modifications` alone for now.** At 5 files it is barely load
   bearing, and populating it is only worth doing after item 4 settles what can be
   bound.
