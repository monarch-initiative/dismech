---
title: Coarse HPO Bindings Must Say Why
status: ENACTED
description: >-
  A phenotype bound to a top-level HPO organ-system term ("Abnormality of the
  eye") is usually a curator who stopped early, but three legitimate reasons
  exist: a pleiotropic spectrum not worth enumerating, a source that genuinely
  says no more, and a narrower concept HPO lacks. Proposes a closed,
  schema-declared "coarse term" subset (the same 23 terms that drive the UI
  facets), one explicit slot recording which of the three applies, a fourth
  value for deliberately unqualified hub nodes in the pathograph, and an
  offline baseline-grandfathered gate. No information content, no depth
  thresholds, no reward for specificity.
tags: [SCHEMA_EVOLUTION, PHENOTYPES, HPO, ONTOLOGY_BINDING, BRAINSTORM]
---

# Coarse HPO Bindings Must Say Why

**Status: enacted, 2026-09-05.** This is the design record; the reference
documentation is [`docs/coarse-phenotype-bindings.md`](../../coarse-phenotype-bindings.md)
and the decision is registered as §4b of the
[decision register](../../explanation/design-decisions.md). Read this file for
*why*, that one for *how*.

**Two things changed between this proposal and what was built**, recorded here
rather than edited away:

1. **The `PATHOGRAPH_HUB` rule inverted.** Part 3 below requires a hub to have
   outgoing `sequelae` into its specific findings. That is wrong. `sequelae` is
   a `CausalEdge`, and a coloboma is not *caused by* an eye abnormality — it *is*
   one, so the requirement would have had curators drawing an is-a hierarchy as a
   causal chain to satisfy a guard. As built, a hub is defined by its **incoming**
   edges (something in the entry must target it) plus the absence of a
   `frequency`; constituents go in `spectrum_terms`, which asserts no causation.
2. **`spectrum_terms` is allowed on a hub too**, optionally, for the same reason.

Numbers below are the 2026-09-05 census taken before enactment: 168 unexplained
bindings, of which four became the worked examples, leaving the 164 now
grandfathered in `tests/coarse_phenotype_baseline.txt`. Regenerate with
`just list-coarse-phenotypes` rather than trusting them.

## The problem, precisely

A phenotype like this validates, renders, exports, and derives the correct
facet — and says almost nothing:

```yaml
- category: Ophthalmologic
  name: Eye Abnormalities
  description: >-
    Ocular findings are common in SYS and take the form of strabismus,
    esotropia, or myopia.
  phenotype_term:
    preferred_term: Eye abnormality
    term:
      id: HP:0000478
      label: Abnormality of the eye
  frequency: FREQUENT
```

(`Schaaf-Yang_Syndrome`.) The description names three HPO-coded findings
(`HP:0000486` Strabismus, `HP:0000565` Esotropia, `HP:0000545` Myopia). The
binding discards all three. Every tool downstream sees "eye".

The `dismech-terms` skill already says *"choose the most specific term that
accurately represents the curated claim"* and the term contract lets
`preferred_term` carry specificity the ontology lacks. Neither is checkable, so
neither is enforced, and the top-level bindings accumulate. The point of this
proposal is to make the **legitimate** reasons for a coarse binding explicit
and machine-readable, so that the unexplained coarse binding — the one that
means "didn't look" — becomes the thing a gate can see.

### What the KB does today

Direct children of `HP:0000118` bound as `phenotype_term.term` in
`kb/disorders/` (the 23 terms in `HPO_TOP_LEVEL_CATEGORIES` /
`PhenotypeCategoryEnum`):

| Term | Label | Uses |
|---|---|---|
| `HP:0002664` | Neoplasm | 47 |
| `HP:0000478` | Abnormality of the eye | 36 |
| `HP:0000119` | Abnormality of the genitourinary system | 19 |
| `HP:0033127` | Abnormality of the musculoskeletal system | 12 |
| `HP:0000707` | Abnormality of the nervous system | 9 |
| `HP:0001626` | Abnormality of the cardiovascular system | 9 |
| `HP:0040064` | Abnormality of limbs | 5 |
| `HP:0002086` | Abnormality of the respiratory system | 5 |
| `HP:0001871`, `HP:0000598`, `HP:0000818`, `HP:0001939`, `HP:0025031` | Blood / Ear / Endocrine / Metabolism / Digestive | 4 each |
| `HP:0001197` | Abnormality of prenatal development or birth | 3 |
| `HP:0002715`, `HP:0001608`, `HP:0001507` | Immune / Voice / Growth | 1 each |
| the other 5 | Breast, Head and neck, Integument, Thoracic cavity, Cellular, Constitutional | 0 |

About 190 bindings across roughly 130 files. Reading the eye cases, they
sort cleanly into the three reasons plus the default:

- **Spectrum summary** (`Schaaf-Yang_Syndrome`, `Rubinstein-Taybi_Syndrome`,
  `FG_Syndrome_1`, most of them): the description lists several specific
  findings; the coarse term stands in for a variable set.
- **Source says no more** (`PAICS_Deficiency`: *"The specific ocular finding
  is not characterized in the available abstract, so the binding is
  deliberately at the general level."*; `Adams-Oliver_Syndrome` DOCK6 subtype).
  The prose idiom already exists — `PUS3-Related_Neurodevelopmental_Disorder`
  carries a full paragraph arguing that `HP:0001627` is *"the right binding
  rather than a mere fallback parent"* — but it lives in `notes:` and `description:`
  where nothing can read it.
- **Narrower concept, no HPO term**: rare at this tier, because HPO's eye
  branch is deep. It is the common case one tier down and in newer
  disorders (a named dysmorphic gestalt, an EEG pattern, a retinal OCT
  appearance).
- **Nothing recorded** — the majority. Indistinguishable from the above.

The one thing the census cannot tell apart is what the proposal fixes.

## Why not measure specificity

Three approaches are explicitly rejected, so that nobody re-proposes them:

1. **Information content / term depth.** Depth is a property of how HPO
   happens to be built, not of the claim. `HP:0004322` Short stature is the
   most-used HP term in the KB (290 bindings) and sits only a few steps below
   `HP:0001507`; it is exactly as specific as the literature ever gets.
   An IC threshold would penalise it and reward `HP:0008857` "Neonatal short-trunk
   short stature" whether or not the paper said that.
2. **Rewarding specificity in compliance scoring.** `qc_plugins` scores
   coverage, not grain. A score gradient towards narrower terms is precisely the
   pressure that manufactures bindings the source does not support, which the
   term contract (*"do not manufacture a narrower ontology match"*) forbids.
3. **Category-gated rules.** Design register §10 already records why
   *category = X ⇒ term under X* is circular: the category is derived from the
   term. The same holds here — nothing about the derived facet can tell you
   whether the coarse binding was deliberate.

What is left is a **closed list**: a small, reviewed set of terms that name an
organ system and nothing else, declared in the schema, where binding one of
them obliges the curator to say which of the legitimate reasons applies.

## Part 1: the subset

### 1a. Which terms are "coarse"

**Tier 0 (recommended starting point): the 23 direct children of `HP:0000118`.**
These already exist as `PhenotypeCategoryEnum` in
`schema/classifications/phenotype_category.yaml`, each with a `meaning:` CURIE,
and as `HPO_TOP_LEVEL_CATEGORIES` in `browser_export.py` driving the
*Phenotype Systems* facet. Zero new vocabulary, one source of truth, and
`just validate-terms-schema` already verifies the `meaning:` labels. A term in
this set names a facet bucket; it cannot name a finding.

**Tier 1 (defer; enumerate by hand if ever):** HPO's organisational second
tier — the morphology/physiology split terms (`HP:0012372` Abnormal eye
morphology, `HP:0012373` Abnormal eye physiology, `HP:0012638`/`HP:0012639`
for the nervous system, `HP:0011842`/`HP:0011843` for the musculoskeletal system) and
the system-part umbrellas (`HP:0000924` Abnormality of the skeletal system,
18 uses; `HP:0000079` Abnormality of the urinary system; `HP:0000951`
Abnormality of the skin; `HP:0000271` Abnormality of the face). These also
name no clinical concept. But the tier is not uniform, which is why it must be
a **curated list and never a depth rule**:

| Tier-1-looking term | Uses | Verdict |
|---|---|---|
| `HP:0001627` Abnormal heart morphology | 150 | **Not coarse.** Carries "Congenital heart defect" as an EXACT synonym; it *is* the clinical concept when a paper says "CHD" (see the `PUS3` note). |
| `HP:0001999` Abnormal facial shape | 178 | **Not coarse.** "Dysmorphic facies" is a real summary finding in dysmorphology. |
| `HP:0012443` Abnormal brain morphology | 28 | Borderline; the neuroimaging equivalent of the above. |
| `HP:0000924` Abnormality of the skeletal system | 18 | Coarse. |

The subset lives in the schema, is `meaning:`-bound, and is edited by PR with
a reason. That is the whole specificity model: membership in a list somebody
argued for.

### 1b. Where the subset is declared

Options, in order of preference:

- **Reuse `PhenotypeCategoryEnum` directly.** The gate reads its `meaning:`
  values. Tier 1, if ever adopted, becomes a second enum
  (`CoarsePhenotypeTermEnum`) that is a superset, so tier 0 stays the facet
  vocabulary untouched. Advantage: the facet subset and the "coarse" subset
  are the same object until someone deliberately makes them differ.
- **A dedicated enum from the start**, `CoarsePhenotypeTermEnum`, whose tier-0
  values are copied from `PhenotypeCategoryEnum` and kept in sync by a test.
  Cleaner separation of concerns; one more thing to drift.
- **An HPO subset.** HPO ships slim subsets (`hposlim_core` and the LOINC/
  ORDO-related ones), but none is "organisational terms only", the OLS adapter
  does not surface subset membership through the cache layer, and an
  externally-maintained list would change under us. Rejected for now; noted
  because GO's `goslim_*` subsets are the natural analogue if this extends to
  `biological_processes` later.

## Part 2: saying why — one slot, four values

### 2a. The slot

Add one optional enum slot to `PhenotypeDescriptor` (so it sits next to the
`term:` it qualifies, like `modifier` and `severity` do):

```yaml
phenotype_term:
  preferred_term: Eye abnormality
  term:
    id: HP:0000478
    label: Abnormality of the eye
  coarse_binding_basis: SPECTRUM_SUMMARY   # or SOURCE_UNSPECIFIED / NO_HPO_TERM / PATHOGRAPH_HUB
```

Name candidates: `coarse_binding_basis`, `term_granularity_basis`,
`binding_rationale`. The name should make clear it is *why the term is coarse*,
not a grade of the term. Slot on `Phenotype` rather than the descriptor is the
alternative; the descriptor wins because `ImagingFinding.phenotype_term` and
`ClinicalTrial.target_phenotypes` reuse the same descriptor and inherit the
slot for free.

### 2b. The values

**`SPECTRUM_SUMMARY` — case (a), pleiotropy and variability.** The disease
produces many distinct findings in this system with variable expressivity,
and one summary phenotype is the honest grain. This is the value that needs
the most design, because "generalized" on its own is still lazy if the
spectrum is only in prose. Options, from cheapest to most structured:

1. *Prose only.* The `description` must name the findings. Not checkable.
2. *`spectrum_terms:` — a multivalued `PhenotypeDescriptor` list on the
   summary phenotype* carrying the constituent HP terms with **no frequency
   and no per-term evidence required**. The evidence sits on the summary
   phenotype, as it does today. This keeps HPO specificity without demanding
   a fully-curated phenotype per finding, which is exactly the cost the
   curator was avoiding:

   ```yaml
   - name: Eye Abnormalities
     phenotype_term:
       preferred_term: Eye abnormality
       term: {id: HP:0000478, label: Abnormality of the eye}
       coarse_binding_basis: SPECTRUM_SUMMARY
       spectrum_terms:
       - preferred_term: strabismus
         term: {id: HP:0000486, label: Strabismus}
       - preferred_term: esotropia
         term: {id: HP:0000565, label: Esotropia}
       - preferred_term: myopia
         term: {id: HP:0000545, label: Myopia}
     frequency: FREQUENT
     evidence: [...]
   ```

   The gate can then require `len(spectrum_terms) >= 2` for this value, and
   term validation covers the constituent CURIEs because they bind the same
   `PhenotypeTerm` enum. This is the recommended shape. It is also the shape
   HPOA/OMIM cannot express, which is a small argument for dismech carrying it.
3. *Bind HPO's own variability modifiers.* `HP:0003812` Phenotypic
   variability and `HP:0003828` Variable expressivity exist, and HPO's
   clinical-modifier branch has `HP:0012837` Generalized. But those are
   modifiers of the *disease* or of *spatial extent*, not of a binding's
   grain, and `qualifiers` is deprecated. Not recommended as the primary
   mechanism; could ride along in `spectrum_terms` if a reader wants the HPO
   term for "this varies".

**`SOURCE_UNSPECIFIED` — case (b), it genuinely cannot be narrowed.** The
cited source says "ocular involvement" and nothing more, or the finding is
heterogeneous at the individual level with no named lesion. The proof is the
evidence snippet, which already exists, so this value needs **no companion
slot** — it is a declaration that the curator looked and the source stopped
here. It is the value `PAICS_Deficiency` and the `PUS3` paragraph are
reaching for in prose. Distinct from `SPECTRUM_SUMMARY`: there the specifics
are known and deliberately summarised; here they are unknown.

**`NO_HPO_TERM` — case (c), a narrower concept HPO lacks.** The description or
`preferred_term` names something more specific than any HP term, and the coarse
parent is the best available anchor. The term contract already licenses
`preferred_term` to be narrower than `term.label`; this value makes that
explicit and adds a place to record the gap:

```yaml
phenotype_term:
  preferred_term: peripapillary retinal pigment mottling
  term: {id: HP:0000479, label: Abnormal retinal morphology}   # tier-1 example
  coarse_binding_basis: NO_HPO_TERM
  term_gap: https://github.com/obophenotype/human-phenotype-ontology/issues/NNNN
```

`term_gap` (optional string, URL or free text) is the same idea as the
"searched, found nothing" record the environmental-evidence waiver requires:
it turns a permanent gap into a lead for an HPO term request. A gate rule
that suggests itself: for this value `preferred_term` must differ from
`term.label` — otherwise nothing narrower was claimed and the value is wrong.

**`PATHOGRAPH_HUB` — the fourth case, deliberately unqualified.** See Part 3.

### 2c. Cheaper alternatives, kept for the record

- **A `review_notes:` sentinel** on the lines of `Left deliberately uncited.`
  (`check-environmental-evidence`): a phenotype whose `review_notes` begins
  `Bound deliberately coarse.` followed by ≥20 words is dispositioned. Works
  today with no schema change, and could be the **migration bridge** for the
  190 existing bindings. It is prose, though, and the user's ask was for
  something explicit and queryable; the sentinel should be a stopgap at most.
- **Derive it.** `preferred_term != term.label` ⇒ case (c); ≥2 HP-coded
  concepts recognisable in `description` ⇒ case (a). The first half is a
  reasonable *lint hint*; the second is NER over prose and is not.
- **Three separate slots** (`spectrum_terms`, `source_limited: true`,
  `term_gap`) with no enum. Loses the one thing the enum gives: a single
  place for the gate to look, and a single "none of these" state to flag.

## Part 3: coarse terms in the pathograph, unqualified on purpose

The pathograph is where a coarse HP term is sometimes the *right* node, and
where the current KB uses it wrong.

### 3a. What the KB does now: coarse terms as leaves

`Rubinstein-Taybi_Syndrome` has a pathophysiology node whose `downstream`
fans out to eleven targets with `causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES`,
two of which are `Ocular abnormalities` and `Renal abnormalities` —
phenotypes bound to `HP:0000478` and `HP:0000119` with no `sequelae` of their
own. `Donnai-Barrow_syndrome` and `Basel-Vanagaite-Smirin-Yosef_Syndrome` do
the same. **No coarse-bound phenotype in the KB has outgoing `sequelae`.**
So every coarse term in every pathograph today is a terminal node: the graph
ends at "eye", which is the graph-level version of the same laziness.

### 3b. The hub pattern

A coarse term earns its place in the pathograph when it is a **convergence
point**: one mechanism produces system-level disruption, which then resolves
into several specific findings. Model it as a phenotype that is a source of
`sequelae`, not a sink:

```yaml
pathophysiology:
- name: Disrupted neural crest migration
  downstream:
  - target: Ocular developmental abnormality      # the hub
    causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES

phenotypes:
- name: Ocular developmental abnormality
  phenotype_term:
    preferred_term: ocular developmental abnormality
    term: {id: HP:0000478, label: Abnormality of the eye}
    coarse_binding_basis: PATHOGRAPH_HUB
  sequelae:                                       # bare names, per the pathograph rule
  - target: Coloboma
  - target: Microphthalmia
  - target: Cataract
- name: Coloboma
  phenotype_term: {term: {id: HP:0000589, label: Coloboma}}
  frequency: FREQUENT
  evidence: [...]
```

What "unqualified" means for a hub, and what the gate should require:

- **It carries no clinical claim of its own.** No `frequency` (the children
  have theirs), and `evidence` is optional — the edges carry the evidence. A
  hub with a frequency is a `SPECTRUM_SUMMARY`, not a hub.
- **It must have ≥1 outgoing `sequelae` to a non-coarse phenotype**, and
  ideally every child should roll up to the hub's facet category — checkable
  offline against `app/hpo_category_cache.json`, which already maps every
  bound HP term to its top-level categories.
- **It is not a `SPECTRUM_SUMMARY` with edges.** The difference is what the
  node asserts: a summary asserts "patients have eye findings, at this
  frequency, of these kinds"; a hub asserts "this mechanism's effect on the
  eye branches here". One entry may reasonably have both, and the hub should
  not be the one the disorder page's phenotype table shows with a frequency.

### 3c. Why this is not the "disruption of eye development" node

That node is `pathophysiology`, binds GO (`GO:0001654` eye development with
`modifier: DECREASED` or `ABNORMAL`), and asserts a **process**. The hub binds
HP and asserts a **system-level outcome**. They can sit in sequence —
process → hub → findings — and they should not be merged. Two consequences:

- Do **not** add an HP slot to `Pathophysiology` to make room for hubs. The
  HP/GO split by section is a load-bearing convention (design register §4,
  §10) and the hub is a phenotype.
- Watch the flat node namespace: a hub named `Abnormality of the eye` and a
  pathophysiology node with the same name collapse into one node (#9896).
  Hub names should be phrased as outcomes ("Ocular developmental abnormality"),
  not as processes.

### 3d. Rendering

A hub should look different from a finding, or readers will take it for one.
Cheap options: dashed outline plus the facet colour; label suffix "(system)";
or collapse hubs into the existing category grouping the renderer already
computes from HPO ancestry. The graph model does not need to change — the
node type is still `phenotype`, and `coarse_binding_basis` is one more
attribute `graph.py` already knows how to pass through for `severity`.

`Neoplasm` (`HP:0002664`, 47 uses, mostly cancer-predisposition syndromes) is
the best first candidate for hub conversion: the specific tumour types are
almost always already curated as sibling phenotypes, so the hub adds edges
rather than nodes.

## Part 4: the gate

`just check-coarse-phenotypes` — offline, whole-KB, in `just qc`, ungated by
changed-path filtering (for the reason `check-entity-refs` is: a `kb/`-only PR
skips pytest). Rule:

> A `phenotypes[]` entry (or any `PhenotypeDescriptor`) whose `term.id` is in
> the coarse subset must carry `coarse_binding_basis`; the value's companion
> requirement must hold (`SPECTRUM_SUMMARY` ⇒ ≥2 `spectrum_terms`;
> `NO_HPO_TERM` ⇒ `preferred_term ≠ label`; `PATHOGRAPH_HUB` ⇒ ≥1 `sequelae`,
> no `frequency`). `SOURCE_UNSPECIFIED` has no companion requirement.

The ~190 existing bindings go into `tests/coarse_phenotype_baseline.txt`,
which may only shrink, exactly like `causal_target_baseline.txt`. New coarse
bindings without a basis fail. Nothing scores anything; a coarse binding *with*
a basis is fully compliant, which is the point — the rule rewards saying why,
not narrowing.

Advisory only, not gated: a `NO_HPO_TERM` whose `preferred_term` has an exact
HP synonym (cache-first label match) is probably a missed term, and a
`SOURCE_UNSPECIFIED` whose own `description` names a finding with an HP label
is probably a `SPECTRUM_SUMMARY`.

## What this deliberately does not do

- Touch `biological_processes` / GO. The same design applies (a closed
  `CoarseBiologicalProcessTermEnum`; GO's own slims as a lead), and nothing
  here is HP-specific except the subset. Out of scope now.
- Extend to tier 1 before tier 0 has been lived with.
- Change `phenotypes.category`. The open register item about wiring
  `PhenotypeCategoryEnum` to that slot is independent; this proposal only
  reads the enum's `meaning:` values.
- Bulk-migrate. The 190 rows are a worklist for the sentinel bridge or the
  slot, one entry at a time, by someone who can read the evidence.

## Open questions for the maintainer

1. Tier 0 only, or seed tier 1 with the handful of clear cases
   (`HP:0000924`, `HP:0012372`, `HP:0012373`, `HP:0012638`)?
2. Does `SPECTRUM_SUMMARY` get the structured `spectrum_terms` list, or is
   prose acceptable for a first version?
3. Slot on `PhenotypeDescriptor` (inherited by imaging and trial phenotypes)
   or on `Phenotype` only?
4. Should a `PATHOGRAPH_HUB` be allowed `evidence` at all, or is the edge
   evidence the only place it belongs?
5. Is `Neoplasm` a coarse term for this purpose, or is the neoplasm branch
   different enough (it is a disease-like-phenotype family, §4) to exempt?

## Appendix: regenerating the census

```bash
# top-level bindings per term
for id in $(grep -o '"HP:[0-9]*"' src/dismech/export/browser_export.py | tr -d '"'); do
  printf '%s %s\n' "$id" "$(grep -rh "id: $id\b" kb/disorders | wc -l)"
done

# every coarse-bound phenotype with its name/description/notes
grep -rn -B12 -A3 "id: HP:0000478" kb/disorders | grep -E "name:|description:|notes:|frequency:"

# do any coarse-bound phenotypes have sequelae? (none, as of 2026-09-05)
grep -rl "id: HP:0000478" kb/disorders | xargs -I{} python3 -c '
import sys,yaml; d=yaml.safe_load(open("{}"))
for p in d.get("phenotypes") or []:
    t=((p.get("phenotype_term") or {}).get("term") or {}).get("id")
    if t=="HP:0000478" and p.get("sequelae"): print("{}", p["name"])'
```
