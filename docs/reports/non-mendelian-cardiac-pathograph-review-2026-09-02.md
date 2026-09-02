# Pathograph Review: Non-Mendelian Cardiac Disease (2026-09-02)

Review of every non-Mendelian cardiac entry in `kb/disorders/` and of the causal graph
each one builds. Covers scope definition, three systemic defects found, per-entry
repairs, and the follow-up work the review deliberately did not attempt.

## Scope

"Non-Mendelian cardiac disease" is not a slot in the schema, so the set was derived
rather than looked up. An entry is in scope when its subject is the heart, the great
vessels, or the pulmonary circulation acting on the right heart, **and** its curated
etiology is not single-gene Mendelian. That admits six etiologic classes:

| Class | Entries |
|---|---:|
| Acquired: infectious, immune-mediated, toxic, stress-induced | 16 |
| Complex, degenerative, or haemodynamic | 12 |
| Multifactorial or sporadic congenital | 9 |
| Acquired or idiopathic conduction disease | 2 |
| Maternally inherited mitochondrial | 2 |
| Idiopathic, cause unknown | 2 |
| **Total** | **43** |

Of 150 cardiac-adjacent entries, 107 were excluded as Mendelian. Three in-scope entries
were missed by a naive keyword sweep because they are named for pulmonary arterial
hypertension rather than for the heart.

### The etiology axis is frequently unfilled

The set had to be derived partly by reading prose because the machine-readable signal is
missing or unbound:

- **43 cardiac-adjacent entries carry no `inheritance:` block at all**, so Mendelian and
  non-Mendelian cannot be told apart from the data. Several are unambiguously Mendelian
  (hypertrophic cardiomyopathy, dilated cardiomyopathy, Brugada syndrome, short QT
  syndrome, left ventricular noncompaction).
- **Six carry free text with no HPO term bound**, which `CLAUDE.md` already names as the
  common gap. Two of those are explicit non-Mendelian assertions that should bind
  `HP:0001426` (multifactorial) or `HP:0003745` (sporadic): `Cardiac_Sarcoidosis`
  ("Multifactorial susceptibility") and `Double_Outlet_Right_Ventricle` ("Multifactorial
  and sporadic").

## Method

1. **Graph diagnostics** — `dismech.graph.build_causal_graph` per entry, recording node
   and edge counts, orphan targets, isolated nodes, and weakly connected components.
2. **The project's own QC metric** — `dismech.qc_plugins.causal_inlink_coverage`, which
   counts a phenotype as connected when at least one edge with predicate `causes`,
   `leads_to`, `triggers` or `exacerbates` targets it. Baselines were computed from
   `git HEAD` so before/after figures use one definition.
3. **Gates** — `check_causal_targets`, `check_entity_refs`, `check_duplicate_yaml_keys`,
   `check_enum_values`, and `linkml-validate` against the `Disease` class.
4. **Content review** — six parallel reviewers, one per cardiac subdomain, reading each
   chain for direction, missing intermediates, and module conformance.

## Finding 1: the phenotype layer is not wired into the graph

This is the dominant defect and it is much worse in this set than in the knowledge base
as a whole.

| Set | Phenotypes reached by a causal edge |
|---|---|
| Non-Mendelian cardiac (40 entries with phenotypes) | 68/414 (16.4%) |
| Whole knowledge base (2,506 entries) | 13,943/29,021 (48.0%) |

Twenty-one of the forty sat at exactly zero. The mechanism layer is not the problem:
only 6% of pathophysiology nodes were unconnected, against 51% of all nodes. The deficit
is specifically the mechanism-to-phenotype edge, so clinical manifestations were curated
as well-evidenced lists that never entered the causal graph and never reached the
rendered pathograph.

A plausible reason the acquired diseases fare worse than the Mendelian ones: a Mendelian
entry has a single obvious chain from gene to lesion, whereas an acquired disease
presents a broad symptom list with no single parent mechanism, so the wiring step is a
judgement call rather than a transcription.

## Finding 2: `Pathophysiology.consequences` is a dead schema slot

`consequences` (multivalued) and `consequence` (scalar) are real slots on
`Pathophysiology` that validate cleanly and are **ignored by every consumer**: the graph
builder in `src/dismech/graph.py`, the Jinja templates, all thirteen modules under
`src/dismech/export/`, and the claim extractor, which lists `consequence` among the
structural slots it skips. Content written there is invisible everywhere.

This is worse than a dangling bare-name target. A dangling target at least renders a red
phantom node and is caught by `check_causal_targets`; a `consequences` entry produces
nothing at all, and no gate looks for it.

Twenty-seven nodes across the knowledge base use it. The largest casualty is outside
this review's scope: **`Alzheimer_Disease` states its entire causal architecture this
way across 22 nodes**. Within scope, `Pulmonary_hypertension` used it for the
right-ventricular-hypertrophy to right-heart-failure step.

The schema itself records the ambivalence, carrying `todos: [unify consequences and
consequence]` on the slot. No GitHub issue covers this.

## Finding 3: two thirds of genetic nodes never reach the mechanism graph

`build_causal_graph` links a `genetic[]` item to a pathophysiology node only by matching
gene keys, drawn from the mechanism node's own `gene`/`genes` descriptors. A
susceptibility gene named only in a node's prose therefore stays isolated.

Across the in-scope entries, **75 of 116 genetic nodes (65%) were isolated** for this
reason. Worst affected were `Congenital_Heart_Disease` (13 of 13),
`Pulmonary_hypertension` (9 of 9), `Coronary_Artery_Congenital_Malformation` (6 of 6),
and `Tetralogy_of_Fallot` (5 of 5).

Closing this requires adding HGNC-bound gene descriptors to mechanism nodes, which is an
ontology-binding change rather than a wiring change, so it was left for follow-up.

## Finding 4: module conformance is largely absent, including where a module exists

Twenty-four of the forty entries declared no `conforms_to` on any node. The sharpest
case is that **`Pulmonary_hypertension` does not conform to the
`pulmonary_vascular_remodeling` module**, although nine other entries do, three of which
(`Eisenmenger_Syndrome`, `Ventricular_Septal_Defect`, `Rheumatic_Heart_Disease`) are
downstream consequences of the very condition the general entry describes.

Similar gaps, each where a sibling entry already conforms: `Cor_Pulmonale` to
`pulmonary_vascular_remodeling`; `Heart_Failure`, `Takotsubo_Cardiomyopathy` and
`Peripartum_Cardiomyopathy` to `cardiomyopathy_maladaptive_remodeling`.

Conformance is also uneven within the pulmonary arterial hypertension family:
`Idiopathic_Pulmonary_Arterial_Hypertension` declares it on five nodes,
`Heritable_Pulmonary_Arterial_Hypertension` on one, and
`Drug_or_Toxin-Induced_Pulmonary_Arterial_Hypertension` on none, despite all three
walking the same chain.

## Coverage gap: acquired long QT has no entry

`CLAUDE.md` notes that the `cardiac_ion_channel_repolarization` module scopes itself to
inherited arrhythmia syndromes in structurally normal hearts, and that drug-induced long
QT would need a separate module. There is currently no entry for acquired or
drug-induced long QT syndrome either, though the knowledge base curates other
drug-toxicity entities including `Anthracycline_Induced_Cardiomyopathy` and
`Drug_or_Toxin-Induced_Pulmonary_Arterial_Hypertension`.
