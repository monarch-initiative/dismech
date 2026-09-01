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

## Headline

The gap that matters is **evidence-backed diet annotations that never reach the
mechanism graph**, not unbound terms.

| | Causal | Intervention |
|---|---|---|
| Diet-related entries | 180 in 129 files | 605 in 442 files |
| On the pathograph | 122 (67.8%) | 308 (50.9%) |
| **Cited but off the pathograph** | **56** (42 after dropping weak matches) | **263** |
| …of those, `CITED_HUMAN` | 39 (32 strong) | 204 |
| On the pathograph but uncited | 1 | 18 |
| Evidenced only by `REFUTE` | 1 | 9 |

The causal track is in good shape: two thirds of its diet entries already carry
`influences_mechanisms`, and the residue is 42 entries — a reviewable list, not a
programme. The intervention track is the weaker half: half of dietary treatments
never link to a mechanism node, leaving 263 cited-but-unlinked treatments.

**The 19 entries on the pathograph with no evidence at all are the first thing to
fix** — 18 interventions plus `Shigellosis` → "Contaminated water or food". They
already render as mechanism edges, so they assert more than the KB can support.
Three sit in `kb/modules/`, so each is inherited by every conforming disorder.

`REFUTE_ONLY` is counted separately and is **not** a defect. NELABA's "Lipoic acid
supplementation (ineffective)" carries two snippet-backed `REFUTE` items against
the mechanism it targets: a treatment recorded as failing against a node is a
real, useful annotation, and an earlier draft of this audit wrongly flagged it as
uncited.

### The 42 strong causal candidates

Concentrated in entries where diet is central: Gout (beer, fructose-sweetened
soft drink, red/organ meat, shellfish — all `CITED_HUMAN`, none linked),
Phenylketonuria (dairy, meat, nuts), Celiac Disease (gluten, wheat, barley, rye),
plus alcohol across a dozen carcinomas and cardiovascular entries, and single
entries in Coronary Artery Disease (high-fat diet), Hyperlipidemia (high
saturated fat), Obesity and Type 2 Diabetes (high-calorie diet), Osteoporosis
(vitamin D deficiency), Thyroid Follicular Carcinoma (iodine deficiency).

A `CITED_HUMAN` row is a candidate, not a verdict. Most of these citations are
observational cohort associations, and an association is not a mechanism — read
the snippet before drawing an edge. Gout's shellfish evidence, for instance,
measures *incident gout* in a cohort rather than precipitation of a flare, which
its own `explanation` already says.

## Ontology binding — the secondary axis

| State | Causal | Intervention |
|---|---|---|
| `BOUND` | 113 (62.8%) | 3 (0.5%) |
| `PARTIAL` (block present, no `term:`) | 5 | 2 |
| `FREE_TEXT` | 62 (34.4%) | 600 (99.2%) |

`dietary_modifications` is effectively unused: 5 files in the whole KB (Celiac,
ECHS1 Deficiency, Konzo, Lathyrism, Phenylketonuria), 11 modification records,
against 605 dietary treatments. Only 18 FOODON bindings exist KB-wide across 10
distinct terms.

**Free text is a legitimate outcome, not a backlog.** Two structural reasons, and
neither is a curation failure:

1. **`FoodTerm` excludes food components.** It is reachable only from
   `FOODON:00001002` (food product) and `CHEBI:33284` (nutrient). Gluten
   (`FOODON:03420177`) sits under `food material` instead and is correctly
   rejected — as `conf/oak_config.yaml` documents deliberately. So Celiac's three
   grain vehicles are bound while its actual trigger, "Gluten Exposure", cannot
   be. The same will apply to casein, purines, and oxalate.
2. **Dietary patterns have no ontology home at all.** FOODON describes food
   products, not eating patterns.

Where no term fits, free text is the right answer per `.claude/skills/dismech-terms`
— *no term beats a bad one*. The audit reports `FREE_TEXT` as a state to review,
never as an error.

Worth noting separately: **42 causal entries are pathograph-linked *and* free
text**, so they render as ungrounded nodes in an otherwise grounded graph. That
is the subset where a binding, if a good one exists, buys the most.

### Dietary-pattern CURIE scatter

The same pattern concept is bound inconsistently across entries:

```
diet:     ECTO:0090010 x3, XCO:0000013 x1, ECTO:9001347 x1
dietary:  ECTO:0090010, ECTO:9000950, ECTO:9000084, ECTO:0400019, FOODON:03303171
alcohol:  ECTO:0001082 x12, ECTO:0300001 x1
```

`XCO:0000013` is a bare "diet" catch-all used where a specific pattern was meant.
Alcohol is the healthy case — `ECTO:0001082` dominates, with `ECTO:0300001`
correctly reserved for the maternal route.

Standardizing on one ECTO CURIE per named pattern is the cheap win here, and
needs no schema change.

## Treatment-side inconsistency

Dietary treatments scatter across NCIT action terms — `NCIT:C15747` (supportive
care), `NCIT:C15447` (dietary intervention), `NCIT:C15433` (nutritional support),
`NCIT:C15986` (pharmacotherapy) — and **235 of 605 carry no
`therapeutic_modality` at all**, with 232 `BEHAVIORAL` and 104 `SMALL_MOLECULE`.

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
  cut it from 1,262 entries to 605.
- **Match provenance is recorded** (`matched_in`: `food_source` / `name` /
  `term_label` / `description`). A causal entry matched only in description prose
  is the weak tail — 14 of the 56 causal gap rows, including Ependymoma
  ("high-dose ionizing radiation", whose description mentions diet) and CKD
  tobacco smoking (on "glycemic"). Filter with `--strong-only`.

Bare `sodium` was dropped from the keyword list: it matched 48 entries that were
almost all drugs (sodium channel blockers, sodium valproate, dantrolene sodium),
and every genuinely dietary one carries "diet"/"dietary"/"salt"/"intake" anyway.
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

1. **Cite or unlink the 19 uncited pathograph edges** (18 intervention, 1 causal).
   They already render, and three are in modules, so they propagate to conformers.
2. **Work the 42 strong causal candidates**, reading each snippet before adding
   `influences_mechanisms`. Gout, Phenylketonuria, and Celiac Disease alone are 11
   of them and are the natural pilot, since all three already model diet well on
   the other track.
3. **Standardize the dietary-pattern CURIEs**, one ECTO term per named pattern,
   retiring the bare `XCO:0000013` catch-all.
4. **Widen the `FoodTerm` root** to admit the FOODON `food material` branch, so
   food components (gluten, casein) become bindable. This is a schema change with
   a cache rebuild, and needs its own decision-register entry — the current narrow
   root is deliberate, and `conf/oak_config.yaml` explains why.
5. **Leave `dietary_modifications` alone for now.** At 5 files it is barely load
   bearing, and populating it is only worth doing after item 4 settles what can be
   bound.
