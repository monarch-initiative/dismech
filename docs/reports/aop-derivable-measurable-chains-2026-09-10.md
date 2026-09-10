# Which dismech pathographs could seed an AOP: measurable node chains

**Date:** 2026-09-10
**Scope:** a census of `kb/disorders/` and `kb/modules/` (3,009 files) for causal chains
whose every node carries a model-system measurement, as candidate material for deriving a
putative Adverse Outcome Pathway from dismech.
**Companion:** [`projects/AOP_EMOD_ALIGNMENT.md`](../../projects/AOP_EMOD_ALIGNMENT.md),
which supplies the framework comparison this report screens against.

## Why "two model systems on the entry" is the wrong screen

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

That distinction is the finding. Screening by "entry has ≥2 experimental models" returns a
large, mostly unusable set; screening by chain connectivity returns a small, directly usable
one.

## KB totals

Counted 2026-09-10 across `kb/disorders/` and `kb/modules/`:

| Model section | Entries | Pathograph-linked (`modeled_mechanisms` present) |
|---|---|---|
| `experimental_models` (NAM) | 619 | 557 |
| `animal_models` | 1,542 | 1,108 |
| `computational_models` | 103 | 79 |

Entry-level filters, for the record:

- **154** entries carry ≥2 `experimental_models` blocks.
- **473** entries carry ≥2 pathograph-linked models of any kind.
- **797** entries carry at least one pathograph-linked model.

## The chain screen

For each entry, build the causal graph from `pathophysiology[].downstream[].target` (bare
names, matched verbatim — see CLAUDE.md, *Pathograph Targets Are Bare Names*), then find the
longest path in the subgraph induced by nodes that are a `modeled_mechanisms` target.

Three tightenings, from loosest to strictest:

| Requirement on **every** node in the chain | ≥3 nodes | ≥4 nodes | ≥5 nodes |
|---|---|---|---|
| ≥1 model linked | 161 | 45 | 12 |
| ≥1 model link carrying `readouts` (measurable) | 90 | 20 | **4** |
| ≥2 distinct models linked | 12 | 4 | 1 |

The middle row is the AOP-relevant one: a readout is what makes the node an Event rather
than an assertion.

## The four 5-node fully-measurable chains

| Entry | Linked models | Readouts on chain | Chain |
|---|---|---|---|
| `Left_Ventricular_Noncompaction_8` | 2 NAM / 7 animal | 15 | Loss of Compact Myocardium Transcriptional Identity → TGF-beta Signaling Dysregulation → Impaired Cardiomyocyte Proliferation → Left Ventricular Dilation and Systolic Dysfunction → Arrhythmia and Ventricular Pre-excitation |
| `Wiedemann-Rautenstrauch_Syndrome` | 5 NAM / 2 animal | 11 | Aberrant POLR3A Transcript Processing → Reduced Wild-Type POLR3A Expression → RNA Polymerase III Transcriptional Hypofunction → Nucleolar Disruption, p53 Activation and Premature Senescence → Impaired Mesenchymal Progenitor Proliferation and Differentiation |
| `Mitochondrial_Complex_I_Deficiency_Nuclear_Type_1` | 2 NAM / 1 animal | 10 | Arrest of Complex I Assembly at the CI-830 Subcomplex → Isolated Complex I Deficiency → Reductive Stress and Bioenergetic Failure → Leukocyte-Mediated Neuroinflammation → Symmetric Necrotizing Brainstem and Basal Ganglia Lesions |
| `Liver_Cirrhosis` | 1 NAM | 6 | Hepatocyte Injury and Death → Kupffer Cell Activation → Hepatic Pro-Inflammatory Mediator Release → TGF-beta Signaling in Fibrogenesis → Hepatic Stellate Cell Activation |

`Liver_Cirrhosis` is the AOP 38 comparator already worked through on the alignment page, so
it validates the screen rather than producing anything new: the whole chain is instrumented
by one NAM, the Akura Twin microphysiological system, whose authors built it "to quantify
the key events of the liver fibrosis AOP".

## The twelve chains where every node has ≥2 independent models

Two models on one node is what a KER's empirical support wants, and — more usefully — what
makes a *disagreement* between models visible.

| Nodes | Entry | Linked models |
|---|---|---|
| 5 | `Left_Ventricular_Noncompaction_8` | 2 NAM / 7 animal |
| 4 | `cellular_senescence` (module) | 1 NAM / 2 animal / 4 comp |
| 4 | `genomic_instability_aging` (module) | 2 animal / 2 comp |
| 4 | `Cystic_Fibrosis` | 3 NAM / 3 comp |
| 3 | `Chemotherapy_Induced_Diarrhea` | 6 NAM |
| 3 | `TRAPPC12-Related_Encephalopathy` | 5 NAM / 1 animal |
| 3 | `Intellectual_Developmental_Disorder_Autosomal_Recessive_67` | 1 NAM / 2 animal |
| 3 | `Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease` | 4 NAM / 3 animal |
| 3 | `Primary_Ciliary_Dyskinesia` | 11 NAM / 4 animal / 1 comp |
| 3 | `Type_2_Diabetes_Mellitus` | 3 NAM / 1 animal / 1 comp |
| 3 | `deregulated_nutrient_sensing` (module) | 1 animal / 3 comp |
| 3 | `epigenetic_alterations` (module) | 1 animal / 3 comp |

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

Numbers are regenerable from the KB alone; no network access is involved.

```python
# for each file in kb/disorders/ and kb/modules/
edges = [(node.name, d.target)
         for node in doc.pathophysiology
         for d in node.downstream]

covered = {link.target
           for section in ("experimental_models", "animal_models", "computational_models")
           for model in doc[section]
           for link in model.modeled_mechanisms}

measurable = {link.target for ... if link.readouts}          # tightening 2
multi_model = {t for t in covered if len(models_targeting[t]) >= 2}   # tightening 3

# longest simple path in the subgraph of `edges` induced by the chosen node set
```

Chains are simple paths (no repeated node) over `pathophysiology` nodes only; a
`downstream` target naming a phenotype terminates the chain, since phenotypes carry no
`downstream` edges of their own. Dangling targets — bare names matching no node — are
excluded by construction, so the counts are unaffected by the grandfathered backlog in
`tests/causal_target_baseline.txt`.

## The derivation

`Left_Ventricular_Noncompaction_8` has been worked through in full as a putative AOP:
[`projects/AOP_EMOD_ALIGNMENT/lvnc8-putative-aop-2026-09-10.md`](../../projects/AOP_EMOD_ALIGNMENT/lvnc8-putative-aop-2026-09-10.md).

Headline result: the Event and KER layers transfer nearly for free — three of its six Events
already exist in AOP-Wiki and three are new — but **the chain has no MIE and cannot have one**,
because a germline lesion is not a stressor-biomolecule interaction. That is a limitation of
this screen, which ranked on measurability and never asked whether a chain has a chemical
entry point. `Skeletal_Fluorosis` is the chemically initiated alternative in the same table.

## What this report does not decide

Whether a derived AOP should be *recorded* anywhere in dismech — a `Pathophysiology`
cross-reference slot carrying `aop.events:` CURIEs, an AOP-Wiki structured reference source —
is open and belongs in its own issue. See *Open schema questions* on the alignment page.
