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

## Repairs made

Every entry in scope was passed through a wiring repair: missing
mechanism-to-phenotype `downstream` edges, phenotype `sequelae`, `reports_on`
readouts for investigation and test-result phenotypes, treatment
`target_mechanisms`, environmental `influences_mechanisms` with an explicit
`environmental_effect`, model `modeled_mechanisms`, and biomarker `readouts`.

| Measure | Before | After |
|---|---|---|
| Phenotypes reached by a causal edge | 68/414 (16.4%) | 353/414 (85.3%) |
| Phenotypes touching the graph at all | — | 408/414 (98.6%) |
| Entries with no wired phenotype | 21 | 0 |
| Edges across the 40 entries | 568 | 1,126 |
| Grandfathered dangling targets, KB-wide | 126 | 123 |

The largest individual recoveries were `Kawasaki_Disease` (1/40 to 40/40),
`Congenital_Heart_Disease` (6/20 to 20/20), `Coronary_Artery_Congenital_Malformation`
(0/13 to 13/13), `Histiocytoid_Cardiomyopathy` (0/15 to 14/15) and
`Eisenmenger_Syndrome` (1/17 to 13/17).

Three dangling bare-name targets were repaired rather than baselined. In
`Idiopathic_Spontaneous_Coronary_Artery_Dissection` both were the same defect, one
edge bundling four phenotypes, now split into separate edges naming the real
phenotypes with the flow-limitation and regional-ischemia steps carried as
`intermediate_mechanisms`. In `Posterior_Myocardial_Infarction` the target was
retargeted to the ischemic cell-death node, which is what the curated claim says.

### The metric understates correct curation

`PhenotypeConnectivityPlugin` counts only `causes`, `leads_to`, `triggers` and
`exacerbates`. A `readout` edge does not count, by deliberate design. But an ECG
sign, an echo measurement or a troponin value **should** be modelled as a
`reports_on` readout, not as a consequence, so an entry rich in investigation
phenotypes cannot reach 100% by curating correctly. After this pass, 55 phenotypes
across the set are wired as readouts and score as unconnected.

`Posterior_Myocardial_Infarction` is the clearest case: it reads 1/5 while being
fully connected, because four of its five phenotypes are ECG signs and a troponin
level. The metric is not wrong, but it should not be read as a curation target.

### A correction to an earlier assumption

Unlinked treatments looked like a defect and are not. Restricted to therapeutic
actions, 105 of 206 treatments in scope carried `target_mechanisms` at baseline,
against 48% knowledge-base-wide, so the set was normal. The apparent gap came from
counting monitoring, screening and counselling actions, and **0 of 222 such actions
carry `target_mechanisms` anywhere in the knowledge base**. That is a consistent
convention: the graph has no monitoring predicate, and linking surveillance to a
mechanism would assert that surveillance acts on it.

## Deliberate non-fixes

These were found and left alone, with the reason recorded rather than the change
forced:

- **Node-name collisions** where one name is both a pathophysiology node and a
  phenotype, which the flat namespace merges (issue #9896). Found in
  `Pulmonary_hypertension` (Right Ventricular Hypertrophy), `Tetralogy_of_Fallot`
  (two), `Pericarditis` (Cardiac tamponade), `Rheumatic_Heart_Disease` and
  `Endomyocardial_Fibrosis` (Congestive heart failure), and `Myocardial_Infarction`
  (Elevated cardiac troponin, phenotype and biochemical entry). Renaming a curated
  node to satisfy the graph model would be the wrong direction of fix.
- **Isolated genetic nodes**, for the architectural reason in Finding 3.
- **Curator decisions recorded in `notes`.** `Ventricular_Septal_Defect` leaves two
  phenotypes unwired with a stated reason. `Eisenmenger_Syndrome` prostanoid therapy
  has an obvious mechanism target contradicted by the entry's own `REFUTE` evidence
  that pulmonary resistance did not improve. `Myocarditis` records that no
  `influences_mechanisms` link is asserted for exercise. `Histiocytoid_Cardiomyopathy`
  says the relationship between its two lesions is unresolved.
- **`Pulmonary_hypertension`'s remaining dangling target.** `Right Heart Failure`
  names no node, and no phenotype is a right-heart-failure node. Retargeting to
  `Edema` or `Fatigue` would downgrade a claim whose evidence is explicitly about
  right-sided failure. The correct fix is a new pathophysiology node.
- **A two-cycle in `Coronary_Vasospasm`.** The edge from smooth-muscle
  hyperreactivity to the nitric-oxide defect carries a description stating the
  reverse direction, and duplicates the reciprocal edge already curated at the
  nitric-oxide node. Either the edge is redundant or its description is wrong; a
  curator should decide.

## Entries where wiring is not the fix

- **`Kawasaki_Disease`** has 40 phenotypes hanging off 2 pathophysiology nodes. It is
  now fully connected but structurally a two-hub star, not a chain. It has no node
  for the unknown trigger, no inflammasome node despite curating anakinra and listing
  NLRP3 among susceptibility genes, no endothelial-activation node distinct from the
  arteritis, none of the standard three-stage arteritis histopathology, and no
  thrombosis or stenosis node between the aneurysm and infarction. It also carries two
  separate phenotypes bound to the same term, `HP:0002617`.
- **`Coronary_Arterial_Fistulas`** compresses steal physiology, chamber volume load,
  ischemia, arrhythmia and heart failure into a single node.
- **`Patent_Ductus_Arteriosus`** has no node for the diastolic-steal physiology its own
  intraventricular-haemorrhage and retinopathy evidence turns on, and no separation of
  functional constriction from anatomic remodelling.
- **`Pulmonary_hypertension`** has no thromboembolic-obstruction node despite curating
  both anticoagulation and balloon pulmonary angioplasty as treatments for chronic
  thromboembolic disease, and still uses the deprecated free-text `percentage` field
  for prevalence.
- **`Heritable_Pulmonary_Arterial_Hypertension`**, though Mendelian and out of scope,
  was found to be in the pre-repair state: 32 nodes, 8 edges, no phenotype reached by
  any causal edge. It needs the same pass.

## Follow-up worth filing

1. Decide what `Pathophysiology.consequences` and `consequence` are for. Either wire
   them into the graph or retire them and migrate the 27 nodes, starting with
   `Alzheimer_Disease`. Today they are a trap that validates.
2. Give genetic susceptibility loci a route into the pathograph that does not require
   a gene descriptor on a mechanism node.
3. Add module conformance where a module already exists, beginning with
   `Pulmonary_hypertension` and `Cor_Pulmonale` against `pulmonary_vascular_remodeling`.
   `Cor_Pulmonale` and `Pulmonary_hypertension` currently curate the same
   pulmonary-hypertension-to-right-ventricle biology twice under disjoint node names
   with no shared module and no cross-reference.
4. Bind an HPO term on the six free-text inheritance blocks, and consider whether an
   entry with no `inheritance:` block at all should be flagged.
5. Curate an acquired or drug-induced long QT entry, which would need a module of its
   own since `cardiac_ion_channel_repolarization` scopes itself to inherited syndromes.

## Validation

`just validate-disorders` over all 38 changed entries: schema, ontology terms and
references all pass, with 2,186 of 2,350 snippets verified against the cached
references and 164 skipped by prefix. The four ungated whole-knowledge-base gates
(`check_causal_targets`, `check_entity_refs`, `check_duplicate_yaml_keys`,
`check_enum_values`) and `check_snippet_grading` are clean. A history record was
added for each changed entry; `just validate-history-all` passes over all 8,010
records.

No PMID, snippet or reference title was invented anywhere in this pass. An evidence
block appears on a new edge only where an item already present in the same file
supports that specific edge; every other new edge carries `description` prose alone.
