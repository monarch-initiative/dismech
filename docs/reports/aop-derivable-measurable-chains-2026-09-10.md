# Which dismech pathographs could seed AOPs: measurable node chains

**Date:** 2026-09-10
**Scope:** a census of `kb/disorders/` and `kb/modules/` (3,009 files) for causal chains
whose every node carries a model-system measurement. One such chain is the raw material for
one putative Adverse Outcome Pathway, so the census asks how many entries hold a chain long
enough to be worth deriving — not how many AOPs the knowledge base amounts to.
**Companion:** [`projects/AOP_EMOD_ALIGNMENT.md`](https://dismech.monarchinitiative.org/pages/projects/AOP_EMOD_ALIGNMENT.html),
which supplies the framework comparison this report screens against.
**Worked derivations:** two entries from the tables below are taken all the way through
into AOP form in
[`projects/AOP_EMOD_ALIGNMENT/putative-aops-from-dismech-2026-09-10.md`](https://github.com/monarch-initiative/dismech/blob/main/projects/AOP_EMOD_ALIGNMENT/putative-aops-from-dismech-2026-09-10.md).
**Illustrated summary:** [Pathographs to Pathways](https://claude.ai/code/artifact/7325e46d-c794-4ac4-a9a7-3cd077f4f784) — a web page summarising this
report and those derivations, with two chain diagrams neither document contains. It was
written by hand rather than generated, so the two Markdown files are the authority where
they disagree.

## Where the census started, and why that first cut failed

This began as a simpler question: which entries have at least two experimental model
systems attached? That is the obvious first cut, because an entry with several models
sounds like an entry whose mechanism has been measured. It returns 161 entries, and almost
none of them are usable. The reason is worth setting out before the counts, because it
governs how every table below should be read.

The alignment page records that an AOP Event is defined partly by *how it is measured* —
`Event.measured_or_detected` is a deployed, populated v2.8 field, present on all 1,598
Events in the 2026-08-06 export. dismech has the structural counterpart in the wrong place
for this purpose: `Pathophysiology.assays` mirrors `Event.assays` but is effectively unused
(as counted on the alignment page on 2026-09-07: 2 of 564 assay entries sit on a
pathophysiology node, and none bind an OBI term).

What *is* populated is measurement hanging off the model, not the node:
`ModelMechanismLink.readouts` on `experimental_models`, `animal_models` and
`computational_models`. So a node's measurability in dismech is a property of the links
pointing at it, and an entry-level count of models says nothing about whether those models
land on **consecutive** nodes.

That distinction is the finding. Counting models per entry returns a large, mostly unusable
set, because the models can all sit on one node or scatter across unconnected branches;
requiring them on *consecutive* nodes returns a small, directly usable one.

## KB totals

Every count below is from `just aop-chain-census`, run against `main` on 2026-09-16.
Regenerate it rather than trusting these figures: they move with every curation PR.

A *model block* is one entry in an `experimental_models:` / `animal_models:` /
`computational_models:` list. An entry can hold several, so blocks and entries are
different units and both are given:

| Model section | Model blocks | Blocks with `modeled_mechanisms` | Entries with one | Entries with a linked one |
|---|---|---|---|---|
| `experimental_models` (NAM) | 648 | 589 | 402 | 369 |
| `animal_models` | 1,682 | 1,254 | 913 | 694 |
| `computational_models` | 99 | 79 | 39 | 35 |

Entry-level filters, for the record:

- **161** entries carry ≥2 `experimental_models` blocks.
- **523** entries carry ≥2 pathograph-linked models of any kind.
- **881** entries carry at least one pathograph-linked model.

## The chain screen

For each entry, build the causal graph from `pathophysiology[].downstream[].target` (bare
names, matched verbatim — see CLAUDE.md, *Pathograph Targets Are Bare Names*), then find the
longest path in the subgraph induced by nodes that are a `modeled_mechanisms` target.

Two tightenings:

| Requirement on **every** node in the chain | ≥3 nodes | ≥4 nodes | ≥5 nodes |
|---|---|---|---|
| ≥1 model link carrying `readouts` (measured) | 97 | 21 | **5** |
| ≥2 distinct models linked | 13 | 4 | 1 |

A readout is what makes a node an Event rather than an assertion. Neither row says anything
about the arrows between nodes, which is the defect [The joint screen](#the-joint-screen)
below repairs.

## The five 5-node fully-measured chains

Entries in this table and the next link to their rendered dismech pages. The **Joint
screen** column is the result from [The joint screen](#the-joint-screen) below, which
requires evidence on every edge as well as a readout on every node — the screen that
actually selects derivable chains. Only one of these five survives it.

<details>
<summary>UI developer note — how these URLs are built</summary>

Two things govern them. They are absolute because this document is built by MkDocs into
`elements/`, which does not contain `pages/`, so a relative link would not resolve. And the
page slug comes from each entry's `name:` field, not its filename:

| KB file | Rendered page |
|---|---|
| `Chemotherapy_Induced_Diarrhea.yaml` | `Chemotherapy-Induced_Diarrhea.html` |
| `Mitochondrial_Complex_I_Deficiency_Nuclear_Type_1.yaml` | `Mitochondrial_Complex_I_Deficiency,_Nuclear_Type_1.html` |

Deriving a URL from the filename gives a dead link for both. Nothing in the repository
checks links in `docs/` against the files in `pages/`, so a renamed entry breaks these
silently.

</details>

| Entry | Linked models | Readouts on chain | Joint screen |
|---|---|---|---|
| [`Left_Ventricular_Noncompaction_8`](https://dismech.monarchinitiative.org/pages/disorders/Left_Ventricular_Noncompaction_8.html) | 2 NAM / 7 animal | 15 | **5 nodes** |
| [`Wiedemann-Rautenstrauch_Syndrome`](https://dismech.monarchinitiative.org/pages/disorders/Wiedemann-Rautenstrauch_Syndrome.html) | 5 NAM / 2 animal | 11 | 2 nodes (2/38 edges) |
| [`Mitochondrial_Complex_I_Deficiency_Nuclear_Type_1`](https://dismech.monarchinitiative.org/pages/disorders/Mitochondrial_Complex_I_Deficiency,_Nuclear_Type_1.html) | 2 NAM / 1 animal | 10 | 1 node (0/16 edges) |
| [`Autosomal_Dominant_Nonsyndromic_Hearing_Loss_25`](https://dismech.monarchinitiative.org/pages/disorders/Autosomal_Dominant_Nonsyndromic_Hearing_Loss_25.html) | 2 animal | 11 | 1 node (0/11 edges) |
| [`Liver_Cirrhosis`](https://dismech.monarchinitiative.org/pages/disorders/Liver_Cirrhosis.html) | 1 NAM | 6 | 2 nodes (3/8 edges) |

The chains themselves:

- **Left_Ventricular_Noncompaction_8** — Loss of Compact Myocardium Transcriptional Identity → TGF-beta Signaling Dysregulation → Impaired Cardiomyocyte Proliferation → Left Ventricular Dilation and Systolic Dysfunction → Arrhythmia and Ventricular Pre-excitation
- **Wiedemann-Rautenstrauch_Syndrome** — Aberrant POLR3A Transcript Processing → Reduced Wild-Type POLR3A Expression → RNA Polymerase III Transcriptional Hypofunction → Nucleolar Disruption, p53 Activation and Premature Senescence → Impaired Mesenchymal Progenitor Proliferation and Differentiation
- **Mitochondrial_Complex_I_Deficiency_Nuclear_Type_1** — Arrest of Complex I Assembly at the CI-830 Subcomplex → Isolated Complex I Deficiency → Reductive Stress and Bioenergetic Failure → Leukocyte-Mediated Neuroinflammation → Symmetric Necrotizing Brainstem and Basal Ganglia Lesions
- **Autosomal_Dominant_Nonsyndromic_Hearing_Loss_25** — Inner Hair Cell Stereocilia Bundle Disruption → Reduced Inner Hair Cell Receptor Potential → Synaptic Ribbon Enlargement and Altered Sustained Exocytosis → Failure of Auditory Nerve Activation with Preserved Cochlear Amplification → Secondary Deafferentation of the Inner Hair Cell
- **Liver_Cirrhosis** — Hepatocyte Injury and Death → Kupffer Cell Activation → Hepatic Pro-Inflammatory Mediator Release → TGF-beta Signaling in Fibrogenesis → Hepatic Stellate Cell Activation

`Liver_Cirrhosis` is the AOP 38 comparator already worked through on the alignment page, so
it validates the screen rather than producing anything new: the whole chain is instrumented
by one NAM, the Akura Twin microphysiological system, which its authors describe as
"mimicking the key events of the liver fibrosis AOP".

## The thirteen chains where every node has ≥2 independent models

Two models on one node is what a KER's empirical support wants, and — more usefully — what
makes a *disagreement* between models visible.

| Nodes | Entry | Linked models | Joint screen |
|---|---|---|---|
| 5 | [`Left_Ventricular_Noncompaction_8`](https://dismech.monarchinitiative.org/pages/disorders/Left_Ventricular_Noncompaction_8.html) | 2 NAM / 7 animal | **5 nodes** |
| 4 | [`Cystic_Fibrosis`](https://dismech.monarchinitiative.org/pages/disorders/Cystic_Fibrosis.html) | 3 NAM / 3 comp | 0 (34/55 edges) |
| 4 | [`cellular_senescence`](https://dismech.monarchinitiative.org/pages/modules/cellular_senescence.html) (module) | 1 NAM / 2 animal / 4 comp | 1 (0/6 edges) |
| 4 | [`genomic_instability_aging`](https://dismech.monarchinitiative.org/pages/modules/genomic_instability_aging.html) (module) | 2 animal / 2 comp | 1 (0/3 edges) |
| 3 | [`Chemotherapy_Induced_Diarrhea`](https://dismech.monarchinitiative.org/pages/disorders/Chemotherapy-Induced_Diarrhea.html) | 6 NAM | 0 (3/18 edges) |
| 3 | [`Hereditary_Spastic_Paraplegia_3A`](https://dismech.monarchinitiative.org/pages/disorders/Hereditary_Spastic_Paraplegia_3A.html) | 4 NAM / 4 animal | **3 nodes** |
| 3 | [`Intellectual_Developmental_Disorder_Autosomal_Recessive_67`](https://dismech.monarchinitiative.org/pages/disorders/Intellectual_Developmental_Disorder_Autosomal_Recessive_67.html) | 1 NAM / 2 animal | 1 (0/3 edges) |
| 3 | [`Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease`](https://dismech.monarchinitiative.org/pages/disorders/Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease.html) | 4 NAM / 3 animal | **3 nodes** |
| 3 | [`Primary_Ciliary_Dyskinesia`](https://dismech.monarchinitiative.org/pages/disorders/Primary_Ciliary_Dyskinesia.html) | 11 NAM / 4 animal / 1 comp | **3 nodes** |
| 3 | [`TRAPPC12-Related_Encephalopathy`](https://dismech.monarchinitiative.org/pages/disorders/TRAPPC12-Related_Encephalopathy.html) | 5 NAM / 1 animal | 0 (9/38 edges) |
| 3 | [`Type_2_Diabetes_Mellitus`](https://dismech.monarchinitiative.org/pages/disorders/Type_2_Diabetes_Mellitus.html) | 3 NAM / 1 animal / 1 comp | **3 nodes** |
| 3 | [`deregulated_nutrient_sensing`](https://dismech.monarchinitiative.org/pages/modules/deregulated_nutrient_sensing.html) (module) | 1 animal / 3 comp | 1 (0/12 edges) |
| 3 | [`epigenetic_alterations`](https://dismech.monarchinitiative.org/pages/modules/epigenetic_alterations.html) (module) | 1 animal / 3 comp | 1 (0/2 edges) |

`Primary_Ciliary_Dyskinesia` is the KB's most model-rich entry (11 NAMs, 16 linked models
total) and still yields only a 3-node chain — the models cluster rather than chain. That is
the entry-level-count failure in one line.

## Leading candidate: `Left_Ventricular_Noncompaction_8`

The only entry in the KB with a 5-node chain where every node carries ≥2 independent models,
and the strongest AOP-derivation target for three reasons beyond the count.

**It spans all four levels of biological organisation, already recorded.** Every node carries
`biological_scale` and every one of the nine linked models declares `model_scale` — the axis
AOP-Wiki calls LoBO, and the one construct both frameworks already carry. The ≥2-model chain
walks it cleanly:

| Node | `biological_scale` |
|---|---|
| TGF-beta Signaling Dysregulation | `MOLECULAR` |
| Impaired Cardiomyocyte Proliferation | `CELLULAR` |
| Failed Ventricular Compaction | `TISSUE` |
| Left Ventricular Dilation and Systolic Dysfunction | `ORGANISM` |
| Arrhythmia and Ventricular Pre-excitation | `ORGANISM` |

The readout-backed chain in the table above substitutes `Loss of Compact Myocardium
Transcriptional Identity` (`CELLULAR`) at the head and drops `Failed Ventricular Compaction`,
so it reaches three levels rather than four — that node is model-linked but carries no
readout. Which of the two is the better AOP skeleton is a real choice, not a technicality.

**It contains recorded model disagreement.** Two links are `FAILS_TO_RECAPITULATE`:

- the `Prdm16Q187X` knock-in mouse fails to recapitulate `TGF-beta Signaling Dysregulation`,
  which the cardiomyocyte-specific conditional knockout mouse *does* recapitulate
  (`fidelity: MODERATE`);
- the same knock-in fails on `Left Ventricular Dilation and Systolic Dysfunction`, where the
  `Prdm16cKO`, the systemic monoallelic mouse, the zebrafish model and the sex-stratified
  conditional knockout all report the node with fidelities from `HIGH` to `LOW`.

Per CLAUDE.md a `FAILS_TO_RECAPITULATE` link requires both `limitations` and `evidence`, so
these are substantiated negative claims. In AOP terms that is
`uncertainties-or-inconsistencies` material — a first-class KER field — arriving pre-curated.

**No AOP-Wiki counterpart.** Neither `PRDM16` nor `noncompaction`/`non-compaction` appears
anywhere in the AOP-Wiki export — no Event, KER or AOP — checked by string search of the
cached 2026-08-06 and 2026-09-03 snapshots (1,598 Events in both). The one `compaction` hit
is chromosome super-compaction in the Genomic Instability Event, unrelated. So a derivation
here would be a seeding candidate rather than a re-derivation of something AOP-Wiki already
holds. This is a statement about those two strings in that corpus, not a survey of cardiac
AOP coverage, which is substantial.

## Two gaps the screen exposed

**`model_scale` is set on 36 of the 134 links landing on the 20 four-plus-node chains.** The
node-side `biological_scale` is better at 68 of 84 chain nodes, but the four entries with no
scale on any chain node are `Myocardial_Infarction` and the `cellular_senescence`,
`loss_of_proteostasis` and `inflammaging` modules. The alignment page already found this axis
empty on almost every node the liver-fibrosis use case touched; it is still the cheapest,
schema-free thing to populate, and without it a derived Event has no LoBO.

**A readout is not an assay.** `ExperimentalReadout` gives the measured quantity and its
direction, which is enough to say an Event *was* measured. It does not give the method — the
alignment page's *How each model records the way a claim was measured* section records that
`Pathophysiology.assays` exists for this, binds to an `AssayTerm` enum rooted at
`OBI:0000070`, has no OAK adapter behind it, and holds no OBI CURIE anywhere in `kb/`. So a
dismech-derived Event can populate AOP's *what was measured* but not its
*how it was measured or detected*.

## Method

`scripts/aop_chain_census.py`, run as `just aop-chain-census`. Regenerable from the KB
alone; no network access is involved.

**Only one kind of arrow is counted.** "Causal edge" here means a
`pathophysiology[].downstream[]` entry — a mechanism node pointing at another mechanism
node. The rendered disorder page draws several other kinds of arrow into the same graph,
and none of them is in these counts:

| Arrow type | Counted? |
|---|---|
| `pathophysiology[].downstream[]` | **yes** |
| `environmental[].influences_mechanisms` | no |
| `treatments[].target_mechanisms` | no |
| `phenotypes[].sequelae` | no |
| `phenotypes[].reports_on` | no |
| `experimental_models[]` / `animal_models[]` / `computational_models[].modeled_mechanisms` | no |

The restriction is deliberate: a Key Event Relationship is a step from one mechanism to the
next, so an exposure link, a treatment link or a model link is not a KER. But it means an
entry's edge count here is lower than the arrow count on its page. `Chickenpox` has 3
node-to-node edges and 3 further `environmental` links, all six cited; it counts as 3/3.

**One node universe for every column.** A chain is a simple path (no repeated node) over
`pathophysiology` nodes only. A `downstream` target naming a phenotype ends the chain and
does not count toward its length — phenotypes carry no `downstream` edges of their own, so
admitting them would lengthen chains under one screen and not the other and make the
columns incomparable. Dangling targets — bare names matching no node — are excluded by
construction, so the counts are unaffected by the grandfathered backlog in
`tests/causal_target_baseline.txt`.

The four screens, each applied to that same universe:

| Column | A node qualifies when | An edge qualifies when |
|---|---|---|
| Every node measured | some `modeled_mechanisms` link targeting it has a non-empty `readouts` | always |
| ≥2 distinct models | ≥2 model blocks link to it | always |
| Every edge cited | always | its `downstream[]` entry has non-empty `evidence` |
| **Both** | as *measured* above | as *cited* above |

```python
measured = {link.target for model in models for link in model.modeled_mechanisms
            if link.readouts}
cited    = [(node.name, d.target) for node in doc.pathophysiology
            for d in node.downstream if d.evidence and d.target in patho_node_names]

# longest simple path in the subgraph induced by the chosen node set,
# over the chosen edge set
```

## The derivations, and what they say about this screen

Two entries from the table have been worked through in full as putative AOPs:
[`projects/AOP_EMOD_ALIGNMENT/putative-aops-from-dismech-2026-09-10.md`](https://github.com/monarch-initiative/dismech/blob/main/projects/AOP_EMOD_ALIGNMENT/putative-aops-from-dismech-2026-09-10.md).

`Left_Ventricular_Noncompaction_8` transfers its Event and KER layers nearly for free —
three of its seven Events already exist in AOP-Wiki, three are proposed new, and all six
relationships carry evidence — but **has no MIE and can have none**, because a germline
lesion is not a stressor-biomolecule interaction.

`Skeletal_Fluorosis` was then derived as the chemically initiated counterpart. It has two
MIE candidates, and its downstream Events join an OECD-endorsed radiation AOP (AOP 482)
whose stressor is entirely different — while fluoride appears in none of AOP-Wiki's 756
stressor records. But it also exposes a defect in the screen below.

**The screen measures Events and ignores KERs.** It ranks a chain by whether every node
carries a readout, because an AOP Event is defined partly by how it is measured. That says
nothing about the arrows. In `Skeletal_Fluorosis` the two run opposite ways: the entry
carries evidence on 16 of its 20 causal edges, and **all four that it does not are inside
the chain this screen selected**, so the chain first derived from it had 2 of 5
relationships supported. Re-deriving it along the entry's *evidenced* backbone instead — a
9-node path through the gut-microbiome arm — gives 8 of 8. The measurable nodes are the
ones models instrument, and models measure states rather than transitions.

## The joint screen

Requiring both — a readout on every node *and* evidence on every edge — is what actually
selects AOP-derivable chains.

| Longest chain | Every node measured | Every edge cited | **Both** |
|---|---|---|---|
| ≥2 nodes | 281 | 1,346 | 123 |
| ≥3 nodes | 97 | 1,047 | **38** |
| ≥4 nodes | 21 | 729 | **6** |
| ≥5 nodes | 5 | 435 | **1** |

36,938 `pathophysiology[].downstream[]` edges KB-wide, 15,768 carrying evidence (43%).
Restricted to the node-to-node subset these chains are built from — edges whose target
resolves to another `pathophysiology` node, excluding those terminating on a phenotype —
18,018 edges, 7,371 cited (41%). Fully-cited chains reach
**12 nodes**, where fully-measured ones stop at 5.

**Edge evidence is about thirty-five times more available than node measurability** — 729
entries carry a four-node chain cited at every step, against 21 measured at every node. So
the binding constraint on deriving an AOP from any one dismech entry is `modeled_mechanisms`
coverage, not literature. The 38 entries clearing the joint screen at three nodes are the
real candidate list — `just aop-chain-census --list-joint 3` prints them — and the two
candidate tables above are an upper bound.

`Left_Ventricular_Noncompaction_8` is the only entry in the knowledge base clearing both
requirements at five nodes, so the derivation nominated below survives the tightened
screen — by luck, since nothing in the original ranking looked at edges.

## What this report does not decide

Whether a derived AOP should be *recorded* anywhere in dismech — a `Pathophysiology`
cross-reference slot carrying `aop.events:` CURIEs, an AOP-Wiki structured reference source —
is open and belongs in its own issue. See *Open schema questions* on the alignment page.
