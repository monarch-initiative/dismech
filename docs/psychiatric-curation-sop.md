# Psychiatric and Neurodevelopmental Curation SOP: Circuit-Level Mechanisms

Curator-facing SOP for representing psychiatric and neurodevelopmental
disorders in dismech using the existing pathophysiology model. Resolves
[#1448](https://github.com/monarch-initiative/dismech/issues/1448) — the
question of whether circuit-level disorders (e.g. ADHD) need a schema
extension.

**Short answer: no schema extension is needed.** Circuit-level mechanisms,
intermediate cognitive constructs, and observable behavioural phenotypes are
all expressible with the existing `pathophysiology` / `phenotypes` model plus
the standard ontology bindings (GO, CL, UBERON, HPO). This document captures
the recurring modeling decisions so future psychiatric entries converge on
the same patterns the ADHD prototype established.

The general curation mechanics (evidence, references, ontology terms) live in
`CLAUDE.md` and `.claude/skills/`. This document covers only the
**modeling-decision questions specific to circuit-level disease**: how to
express a "circuit," where to place an intermediate cognitive construct, and
when to keep an axis as a subtype facet rather than splitting into a separate
disease entry.

## Curation unit: one entry per disorder, not per circuit

A psychiatric dismech entry is a curation unit centered on **one disorder's
mechanism graph**, not one circuit per file. A single entry should be able to
chain from genetic liability → neurotransmitter signaling → circuit-level
dysregulation → cognitive/behavioural construct → clinical phenotype, all
within the same `pathophysiology` list.

**Keep as one entry** when the phenotypes and circuit findings share a single
diagnostic concept (DSM/ICD/MONDO disease class), even if multiple circuits
or neurotransmitter systems are involved. ADHD, schizophrenia, autism, and
Tourette syndrome are each one entry that internally chains across several
circuits and signaling axes.

**Split into separate entries** only when the causal program is genuinely
distinct — different diagnostic concept, different cell-of-origin or
neurotransmitter axis, different therapy program. ADHD vs. Tourette vs.
conduct disorder are separate files; ADHD's "Combined / Inattentive /
Hyperactive-Impulsive" presentations are subtype facets *within* the ADHD
entry, not separate files.

## Representing circuit-level mechanisms

Circuits are represented as ordinary `pathophysiology` nodes whose circuit
semantics come from the existing ontology-bound slots, chained via
`downstream` causal edges. The "circuit" is expressed three ways
simultaneously:

1. **Multi-region `locations`** on the node — e.g., a frontostriatal node
   carries both `UBERON:0000451` prefrontal cortex *and* `UBERON:0002435`
   striatum. The two regions on one node mean "this mechanism spans these
   anatomical structures."
2. **Cell types via `CL`** that participate in the circuit — e.g.,
   `CL:0000617` GABAergic neuron, `CL:1001474` medium spiny neuron,
   `CL:0008031` cortical interneuron, `CL:0000700` dopaminergic neuron,
   `CL:0008025` noradrenergic neuron.
3. **Biological processes via `GO`** that describe what's happening at the
   synaptic / signaling layer — e.g., `GO:0050804` modulation of chemical
   synaptic transmission (with `modifier: ABNORMAL`), `GO:0014046` dopamine
   secretion (`modifier: DECREASED`), `GO:0048243` norepinephrine secretion
   (`modifier: DECREASED`).

The circuit's *topology* (which region projects to which) is then expressed
through `downstream` edges between pathophysiology nodes, not by inventing a
"circuit" slot. The ADHD entry's worked chain:

```
Catecholaminergic Signaling Deficit in Prefrontal Cortex   (PFC; CL:0000700, CL:0008025)
  └─ downstream → Prefrontal Cortex Circuit Weakness        (PFC; CL:0008031)
       └─ downstream → Frontostriatal Circuit Dysregulation (PFC + striatum; CL:0000617)
            └─ downstream → Executive Function and Attention Regulation Impairment
                 └─ downstream → Short Attention Span / Hyperactivity / Impulsivity (phenotypes)
```

Tourette syndrome demonstrates the same pattern for the
cortico-striato-thalamo-cortical (CSTC) loop: one node carries
prefrontal cortex + striatum + dorsal-plus-ventral thalamus
(`UBERON:0001897`) as multi-region `locations` plus medium spiny neurons and
GABAergic interneurons, and chains downstream to `Dopamine-Modulated Tic
Circuit Output` and on to the tic phenotypes.

When you introduce a new circuit node, prefer reusing GO terms already in use
across the psychiatric entries (`GO:0050804` modulation of chemical synaptic
transmission and `GO:0007268` chemical synaptic transmission are the most
common substrates). Add a `modifier` (`ABNORMAL`, `INCREASED`, `DECREASED`)
rather than minting a new ontology term.

## Intermediate cognitive constructs: pathophysiology node *and* phenotype

A recurring question for psychiatric disorders is whether deficits like
*executive function*, *working memory*, or *salience attribution* should be
HPO phenotypes or pathophysiology nodes referencing GO.

**The worked answer is: both, at different layers.** The intermediate
cognitive construct is a *pathophysiology node referencing GO*, and it
carries `downstream` edges to the *observable behavioural phenotypes
referencing HPO*. The construct sits between circuit dysfunction and clinical
observation, where it belongs causally.

The ADHD entry is the canonical example:

```yaml
- name: Executive Function and Attention Regulation Impairment   # pathophysiology, not phenotype
  biological_processes:
  - preferred_term: cognition
    term: {id: GO:0050890, label: cognition}
    modifier: ABNORMAL
  - preferred_term: short-term memory
    term: {id: GO:0007614, label: short-term memory}
    modifier: DECREASED
  locations:
  - preferred_term: prefrontal cortex
    term: {id: UBERON:0000451, label: prefrontal cortex}
  downstream:
  - target: Short Attention Span        # HPO phenotype below
  - target: Hyperactivity and Impulsivity

phenotypes:
- name: Short Attention Span             # observable behaviour, not mechanism
  category: Behavioral
  phenotype_term:
    preferred_term: Short attention span
    term: {id: HP:0000736, label: Short attention span}
  diagnostic: true
```

Rules of thumb:

- **Pathophysiology + GO** when the construct is a *mechanism* — a process
  that can be increased/decreased/abnormal and that other circuit nodes can
  causally drive. Cognition, working memory, salience attribution, response
  inhibition, sensory gating, social cognition, reward processing — all
  pathophysiology nodes referencing GO.
- **Phenotypes + HPO** when the item is an *observable clinical sign* the
  patient or clinician reports — inattention, hyperactivity, impulsivity,
  motor/vocal tics, hallucinations, social communication deficits.
  `category: Behavioral` or `Cognitive` is appropriate on these phenotypes.

The cognitive-construct node should usually carry `locations` (the
substrate brain region) even though no cell-type or process change is unique
to it — this preserves the chain so the pathograph renders cleanly from
circuit → construct → phenotype.

If a phenotype itself has both mechanistic and observational facets
(e.g. *psychotic symptoms* is both a state of abnormal salience attribution
and a clinical observation), split it: keep the mechanism layer as a
pathophysiology node (with GO + UBERON), and keep the symptom as an HPO
phenotype downstream.

## Diagnostic-presentation subtypes vs. comorbidity entries

Psychiatric disorders frequently have DSM/ICD "presentations" (ADHD
Combined / Inattentive / Hyperactive-Impulsive; schizophrenia paranoid /
disorganized / catatonic) and frequent comorbid disorders (Tourette
syndrome ↔ ADHD ↔ OCD).

- **Presentations of one disorder** → `has_subtypes` within the entry.
  ADHD's three presentations are subtypes; they share the same mechanism
  graph and differ only in symptom weighting.
- **Distinct comorbid disorders** → separate entries, linked via
  `comorbidities` (and phenotype-level entries where comorbid features
  appear as phenotypes of the index disorder). Tourette syndrome lists
  ADHD, OCD, anxiety and depression as phenotype-level entries and as
  comorbidities, but each is also its own dismech file.

If you are unsure: prefer one entry with a subtype facet over a new file.
Splitting psychiatric entries by presentation will fragment the mechanism
graph without adding biology.

## Genetic factors: polygenic liability is a first-class node

Psychiatric and neurodevelopmental disorders are typically polygenic; large
GWAS, rare CNV, and de novo mutation contributions coexist. Use:

- A **`Polygenic Inherited Liability` pathophysiology node** at the top of
  the chain that summarises GWAS-supported liability and points downstream to
  the molecular and circuit nodes. ADHD, Tourette, autism, and schizophrenia
  all start their chains this way.
- A **`genetic_factors`** block (or `genetics`) for the gene-level details
  (DRD2, GRIN2A, SHANK3, NRXN1, CHD8, HDC, SLITRK1, etc.), each with
  HGNC term, association strength, and PMID evidence.
- A **`Brain Gene-Expression Regulation Effects`** node when bulk
  transcriptomic / splicing / methylation findings are part of the story,
  feeding into the circuit nodes.

Reserve the polygenic / liability framing for the disorder-level node;
individual genes belong in `genetic_factors`, not as standalone
pathophysiology nodes — unless the gene's product has its own well-defined
mechanistic role and direct downstream edges to circuit nodes.

## Evidence patterns for circuit-level claims

Circuit-level pathophysiology claims often draw from review articles,
neuroimaging meta-analyses, and TMS/MRI studies. Apply the standard evidence
SOP from `CLAUDE.md`, with these notes:

- **`evidence_source: HUMAN_CLINICAL`** for review articles, neuroimaging
  meta-analyses, and clinical neurobiology reviews (this is the default for
  most circuit-level evidence).
- **`supports: PARTIAL`** (with `evidence_source: HUMAN_CLINICAL`) when an
  imaging meta-analysis supports circuit dysconnectivity broadly but the
  abstract does not localize the exact tract the node names — this is common
  for white-matter findings; do not overclaim. Example:

  ```yaml
  evidence:
  - reference: PMID:XXXXXXXX
    supports: PARTIAL
    evidence_source: HUMAN_CLINICAL
    snippet: "..."
    explanation: "Meta-analysis supports broad frontostriatal dysconnectivity but does not localize to the specific tract named in this node."
  ```

  Note: `supports:` (`SUPPORT` / `PARTIAL` / `REFUTE` / `NO_EVIDENCE` /
  `WRONG_STATEMENT`) and `evidence_source:` (`HUMAN_CLINICAL` /
  `MODEL_ORGANISM` / `IN_VITRO` / `COMPUTATIONAL` / `OTHER`) are independent
  fields — `PARTIAL` is only valid on `supports:`.
- **Pharmacological-efficacy evidence** (e.g. "dopamine-blocking agents are
  effective for tics") is *indirect* mechanistic evidence — mark it
  `PARTIAL` or `SUPPORT` with `evidence_source: HUMAN_CLINICAL` and explain
  the inference in the `explanation` field. Don't treat treatment-response
  as direct circuit evidence.
- **Imaging-only evidence** is usually `HUMAN_CLINICAL`; **iPSC-derived
  neurons** and **patient-derived organoid** studies are `IN_VITRO`;
  **knockout mouse circuit findings** are `MODEL_ORGANISM`. Keep these on
  separate evidence items so each one carries a single `evidence_source`.

## Worked exemplars

When in doubt about a new psychiatric entry, mirror one of these:

| Disorder | Entry | What it demonstrates |
|---|---|---|
| ADHD | `kb/disorders/Attention_Deficit-Hyperactivity_Disorder.yaml` | Polygenic liability → catecholamine signaling → PFC weakness → frontostriatal → executive function → behavioural phenotypes; DSM presentations as subtypes |
| Schizophrenia | `kb/disorders/Schizophrenia.yaml` | Multiple parallel pathophysiology axes (dopamine / glutamate / GABA / complement-mediated pruning / oligodendrocyte / mitochondrial / BBB) feeding a shared symptom set |
| Autism spectrum disorder | `kb/disorders/Autism_Spectrum_Disorder.yaml` | E/I imbalance as integrating mechanism; neuroinflammation, gut-brain axis, synaptic scaffolding, chromatin remodeling as parallel contributors |
| Tourette syndrome | `kb/disorders/Tourette_Syndrome.yaml` | CSTC circuit modeled as multi-region pathophysiology node; dopamine-modulated tic output as proximal mechanism; tic phenotypes downstream |
| Conduct / oppositional defiant disorder | `kb/disorders/Conduct_Disorder.yaml`, `kb/disorders/Oppositional_Defiant_Disorder.yaml` | Behavioural-disorder framing alongside neurodevelopmental disorders |

## Related documents

- `CLAUDE.md` — repo-wide curation conventions (evidence SOP, ontology
  binding rules, MAXO/CHEBI treatment patterns)
- `docs/cancer-curation-sop.md` — analogous SOP for cancer entries (MONDO/NCIT
  anchoring, subtype axes)
- `docs/pathographs.md` — how `pathophysiology.downstream` edges and
  `phenotypes.sequelae` edges render as interactive graphs
- `docs/frequency-evidence-guidelines.md` — frequency-qualifier evidence
  patterns relevant to behavioural and cognitive phenotype frequencies
- [#1448](https://github.com/monarch-initiative/dismech/issues/1448) — this
  document
- [#1307](https://github.com/monarch-initiative/dismech/issues/1307) — sibling
  discussion on faceted subtypes vs. separate disease pages
