# A putative AOP derived from `Left_Ventricular_Noncompaction_8`

**Date:** 2026-09-10
**Source entry:** [`kb/disorders/Left_Ventricular_Noncompaction_8.yaml`](../../kb/disorders/Left_Ventricular_Noncompaction_8.yaml) (MONDO:0014152)
**Selection:** [`docs/reports/aop-derivable-measurable-chains-2026-09-10.md`](../../docs/reports/aop-derivable-measurable-chains-2026-09-10.md)
**AOP-Wiki snapshot compared against:** 2026-09-03 bulk XML export (1,598 Events)

## What this is, and what it is not

A **derivation exercise**: the dismech pathograph of one entry, re-expressed in AOP-Wiki's
v2.8 vocabulary, to see what a dismech-derived AOP actually contains and where it comes up
empty. It is working material for the AOP EMOD alignment project.

It is **not** a schema proposal — nothing here is a construct dismech should adopt, and no
`aop*:` CURIE is written into `kb/`. Whether a pathophysiology node should be able to carry a
Key Event cross-reference is
[open schema question 1](../AOP_EMOD_ALIGNMENT.md#1-should-a-pathophysiology-node-be-able-to-carry-a-key-event-cross-reference)
on the project page. It is also **not** an AOP-Wiki submission; the Event and KER numbering
below is local to this document.

## Maturity classification

**Putative** on the Villeneuve et al. 2014 scale ([PMID:25466378](https://pubmed.ncbi.nlm.nih.gov/25466378/),
Table 3) — "a hypothesized set of KEs and KERs supported primarily through biological
plausibility and/or statistical inference", with incomplete linkage at the initiating end.

It clears part of the qualitative bar and fails the rest. Every KE below is supported by a
description of how it can be measured, which qualitative AOP development requires; every KER
carries empirical support beyond plausibility, which it also requires. What is absent is any
weight-of-evidence evaluation, and — decisively — an MIE. It is nowhere near quantitative: no
KER in this chain carries a magnitude or duration relation between upstream and downstream
change.

## The finding: this chain has no MIE, and cannot have one

An AOP's molecular initiating event is a **molecular interaction between a stressor and a
biomolecule**. The initiating node here is `PRDM16 Loss-of-Function Variant` — molecular in
scale (`biological_scale: MOLECULAR`), and genuinely the head of the chain, with a fully
specified `genetic_context`:

```yaml
genetic_context:
  functional_impact_category: LOSS_OF_FUNCTION
  allele_type: SNV_INDEL
  variant_origin: GERMLINE
  zygosity: HETEROZYGOUS
```

That is a germline lesion, not an interaction with anything. There is no stressor, no dose,
and no exposure. So the gap is not the one the alignment page recorded for `Lead_Poisoning`,
where an MIE-shaped node existed but sat two hops downstream of the toxicokinetic nodes every
exposure targeted. Here the initiating node is exactly where an MIE would sit and is the
wrong *kind* of thing.

**This is a limitation of the selection, and it is worth stating plainly.** The census that
nominated this entry ranked on measurability, model multiplicity and AOP-Wiki novelty. It did
not ask whether the chain has a chemical entry point, and a monogenic disease does not. A
reader wanting an AOP that seeds a toxicology use case should start from a chemically
initiated entry — `Skeletal_Fluorosis` is the nearest one in the same census, with a 4-node
measurable chain headed by `Skeletal Fluoride Accumulation`.

**What the chain is still good for is the AOP network.** Villeneuve's founding principles
make Events the reusable unit and networks-of-shared-Events the functional unit of
prediction; an AOP with no MIE of its own still contributes KEs and KERs that a chemically
initiated AOP can converge onto. Three of the six Events below already exist in AOP-Wiki, and
one of them (`Increase, Transforming growth factor-beta signaling`) is carried by seven AOPs
— so the downstream half of this chain is a ready-made continuation for any stressor that
reaches TGF-beta.

## Events

`LoBO` is AOP-Wiki's level of biological organisation, read off dismech's `biological_scale`
without re-derivation. *How measured* is condensed from the `readouts` on the
`modeled_mechanisms` links that target the node; *taxa* from the models carrying those links.

| # | Event | LoBO | How measured (from readouts) | Taxa | AOP-Wiki counterpart |
|---|---|---|---|---|---|
| E1 | PRDM16 loss of function | Molecular | *(no readout — see above)* | Human, mouse, zebrafish | none |
| E2 | Loss of compact myocardium transcriptional identity | Cellular | Single-cell RNA-seq with spatial transcriptomics of LV compact myocardium, scored for compact- vs trabecular-identity genes (`ALTERED`) | Mouse | **none** — proposed new KE |
| E3 | Increased TGF-beta signalling in cardiomyocytes | Molecular | ChIP-PCR of PRDM16 occupancy at the *Tgfb3* promoter with H3K4me1/me3 state (`INCREASED`); myocardial TGF-beta ligand transcripts and phospho-Smad2 (`INCREASED`); myocardial TGF-beta expression (`DECREASED`, conflicting — see KER2) | Rat, mouse | **KE 1271** *Increase, Transforming growth factor-beta signaling* (Molecular; in 7 AOPs) |
| E4 | Decreased cardiomyocyte proliferation | Cellular | Proliferative and apoptotic indices in genotype-matched hiPSC-cardiomyocytes vs control (`DECREASED`) | Human, zebrafish | **none** — all 31 proliferation KEs in the export are increases, and none is cardiac. Proposed new KE |
| E5 | Failed ventricular compaction | Tissue | *(no readout; two models recapitulate the node without an instrumented measurement)* | Mouse | **none** — no `compaction` Event exists. Proposed new KE |
| E6 | Decreased left ventricular function with dilation | Organ | Ventricular chamber dimensions (`DECREASED`); systolic performance (`DECREASED`); sex-stratified contractile dysfunction (`DECREASED`) | Mouse, zebrafish | **KE 2215** *Decrease Left Ventricular function* (Organ; 2 AOPs), near-match; cf. KE 1532/1533 |
| E7 | Occurrence of cardiac arrhythmia | Organ | Postnatal cardiac electrophysiology (`ALTERED`); QRS duration and QTc (`INCREASED`); ventricular ion-channel transcripts (`ALTERED`) | Mouse | **KE 1106** *Occurrence, cardiac arrhythmia* (Organ; in 8 AOPs) |

Three reused, three proposed. E7 is the adverse outcome for this derivation; the entry also
carries `Congestive Heart Failure` downstream of E6, which would map to **KE 1535** *Heart
failure*, but no model links to it, so it is not measurable in this entry and is left out.

**An inversion worth recording.** The alignment page states that on the method axis there is
harvestable free text on the AOP side and an empty slot on the dismech side. That holds
corpus-wide — 601 of 1,598 Events (38%) carry non-empty `measured_or_detected`. It does not
hold for *these* Events: `measured_or_detected` is empty on KE 1271, KE 1106, KE 2215, KE
1532 and KE 1533, while dismech has an instrumented readout with a direction for every one of
E2, E3, E4, E6 and E7. On this chain the method flows dismech → AOP.

The caveat from the census report survives intact: a readout gives the measured quantity and
its direction, not the technique. The technique is present here only because curators wrote
it into the free-text `readout.description` ("ChIP-PCR of Myc-tagged PRDM16…", "single-cell
RNA sequencing with spatial transcriptomics"), where nothing types or validates it.
`Pathophysiology.assays` is the slot for it and holds nothing in this entry.

## Key Event Relationships

Each row is one `pathophysiology[].downstream[]` edge. *Empirical support* is the edge's own
`EvidenceItem` — a resolvable PMID with a snippet validated as an exact substring of the
cached source, which is precisely the unit a KER with no weight-of-evidence assessment needs.

| # | KER | Empirical support | Evidence type | Adjacency |
|---|---|---|---|---|
| KER1 | E1 → E2 | [PMID:34915728](https://pubmed.ncbi.nlm.nih.gov/34915728/) — *Prdm16cKO* LV compact cardiomyocytes shift to a trabecular-like transcriptomic signature | Model organism | Direct |
| KER2 | E2 → E3 | [PMID:38113297](https://pubmed.ncbi.nlm.nih.gov/38113297/) — PRDM16 binds the *TGFB3* promoter and represses its transcription (H9c2) | In vitro | Direct |
| KER3 | E3 → E4 | [PMID:27642787](https://pubmed.ncbi.nlm.nih.gov/27642787/) — "LVNC iPSC-CMs have decreased proliferative capacity due to abnormal activation of TGF-β signalling" | In vitro (human) | Direct |
| KER4 | E4 → E5 | [PMID:38113297](https://pubmed.ncbi.nlm.nih.gov/38113297/) — homozygous *Prdm16Q187X* mice show an underdeveloped compact myocardium | Model organism, `directness: INDIRECT` | Direct |
| KER5 | E5 → E6 | [PMID:34915728](https://pubmed.ncbi.nlm.nih.gov/34915728/) — cardiomyocyte-specific *Prdm16* ablation causes LV-specific dilation and dysfunction with biventricular noncompaction | Model organism, `directness: INDIRECT` | Direct |
| KER6 | E6 → E7 | [PMID:25443708](https://pubmed.ncbi.nlm.nih.gov/25443708/) — ventricular tachyarrhythmias in up to 47% of symptomatic LVNC patients; [PMID:31959004](https://pubmed.ncbi.nlm.nih.gov/31959004/) — ejection fraction, not trabeculation extent, drives incidence variability | Human clinical, `directness: INDIRECT` | Direct |

KER6 is the only relationship in the chain supported by human clinical data, and both of its
items are `INDIRECT`. KER3 is the only one whose supporting quote asserts the causal link
itself in human cells.

### KER2 carries a genuine uncertainties-and-inconsistencies payload

The v2.8 KER has `<uncertainties-or-inconsistencies>` as a first-class field, and this KER
would fill it from curation that already exists — the entry's `gap_lvnc8_tgfbeta_direction_conflict`
discussion, typed `HUMAN_MODEL_MISMATCH`:

> Does loss of PRDM16 raise or lower TGF-beta signaling in the myocardium, and which
> direction operates in human LVNC8?

Three systems disagree on the **direction** of E3:

| System | Direction | Link |
|---|---|---|
| Cardiac-specific *Prdm16* conditional knockout mouse | TGF-beta transcripts and phospho-Smad2 **up** | `RECAPITULATES`, `fidelity: MODERATE` |
| *Prdm16Q187X* heterozygous knock-in — the genotype-matched model | TGF-beta expression **down** with age | `FAILS_TO_RECAPITULATE`, `fidelity: LOW` |
| Proband hiPSC-cardiomyocytes | activation (proliferative deficit attributed to it) | `RECAPITULATES`, `fidelity: HIGH` |

The models differ in allele class, dose, Cre driver and age at measurement, and none has been
compared with another directly. The entry's own `limitations` prose states the constraint
this places on downstream use — the link "must not be used to infer the direction of the
TGF-beta change in patients at any given stage".

Two things follow for the derivation. The reuse of **KE 1271**, whose title asserts an
*increase*, is therefore provisional: the genotype-matched mammalian model moves the other
way. And a `FAILS_TO_RECAPITULATE` link is not an absence of evidence — CLAUDE.md requires
both `limitations` and `evidence` on one — so this is a substantiated negative claim arriving
pre-curated in the shape the KER field wants.

## What came out empty

| AOP construct | Result |
|---|---|
| MIE | **Absent and unobtainable** — germline lesion, no stressor. See above |
| Prototypical stressors | Absent, for the same reason |
| Quantitative understanding | Absent on all six KERs — no magnitude or duration relation anywhere in the entry |
| Weight-of-evidence grades | Absent — dismech has no ordinal grade on a causal edge. `fidelity` grades a *model's* faithfulness, not the strength of a KER, and conflating the two would be wrong |
| Key event essentiality | Absent — assessed at AOP level in v2.8, and nothing in dismech corresponds |
| Taxonomic applicability on Events and KERs | Derivable only via the models, per the alignment page's divergence table. E1–E7 above borrow taxa from the models that measure them, which is not the same claim as an Event being applicable to a taxon |
| Population-level Event | Not applicable here, but the enum gap stands: `BiologicalScaleEnum` stops at `ORGANISM` |
| `measured_or_detected` method text | Present only as untyped prose inside `readout.description`; `Pathophysiology.assays` is empty in this entry |

## What the exercise says about deriving AOPs from dismech generally

1. **The Event layer transfers almost for free.** LoBO comes from `biological_scale`, the
   measurement from `readouts`, the object/process terms from `cell_types` /
   `biological_processes` / `locations`. Nothing had to be invented for E2–E7.
2. **The KER layer transfers with its evidence attached**, and the validated-quote discipline
   means each empirical-support cell is checkable rather than asserted — the contribution the
   alignment page already nominates as flowing dismech → EMOD.
3. **The initiating end does not transfer**, and for a Mendelian entry it cannot. Chemically
   initiated entries are the ones to screen for if an MIE is required.
4. **Model disagreement is an asset, not noise.** `FAILS_TO_RECAPITULATE` plus a typed
   `HUMAN_MODEL_MISMATCH` discussion populates a KER field that 75% of the deployed corpus
   leaves empty — 1,774 of 2,369 KERs in the 2026-09-03 export carry no
   `uncertainties-or-inconsistencies` text at all.
5. **Nothing here required a schema change.** The one thing that would have improved the
   output most — a typed method on the node — is `Pathophysiology.assays`, which already
   exists and is unused.
