# The parkinsonian AOPs against dismech pathographs: where the two meet

**Date:** 2026-10-25
**Scope:** AOP-Wiki AOPs 3, 587, 588, 589 and 593 — the five pathways ending in parkinsonian
motor deficits — cross-walked onto the 82 `kb/disorders/` entries that carry parkinsonism or
bradykinesia with a second cardinal sign. 12 Key Events, 13 Key Event Relationships.
**AOP-Wiki snapshot:** `aop-wiki-cli` 10-03-2026 export, read from the shared cache. The CLI
was run from commit `0bcc052` for the Key Event level screen; the entity reads are
snapshot-only and carry no code dependency.
**Reproduce:** `python scripts/aop_parkinsonism_crosswalk.py` (`--format json`, `--format tsv`).
The AOP side is transcribed into that script from the snapshot; the dismech side is read live.
**dismech KB state:** every number on the dismech side was computed against `021a80a0933`.
**Per-entry rows:** [`data/aop-parkinsonism-crosswalk-2026-10-25.tsv`](data/aop-parkinsonism-crosswalk-2026-10-25.tsv)

## The one-sentence version

dismech already holds the human-relevant core of AOP 3 — including the same post-mortem
complex I citation AOP 3 leans on — at a coarser granularity than AOP-Wiki uses; what it does
not hold is the *chemical* initiation arm, and that arm is evidenced in model systems rather
than in human disease for complexes I and III, and not evidenced at all in AOP-Wiki for
complexes II and IV.

So the gap is mostly representational, not evidential, and the part that is evidential cannot be
closed by porting anything across. For complexes II and IV it runs the other way, in two
different ways. For complex II, dismech's curated SDHA neurodegeneration chain is better
evidenced than AOP 588's, and it routes the lesion to optic nerve, cerebellum and muscle rather
than to the substantia nigra. For complex IV, the step AOP 589 asserts with no reference at all
is one dismech represents directly in five parkinsonism entries with cited human evidence,
including a quantified human measurement of chemical complex IV inhibition — but those entries
reach parkinsonism through basal ganglia necrosis and hypoxic injury, not through the selective
nigral degeneration AOP 589 inherits from AOP 3.

## What the five AOPs are, and why they are nearly the same AOP

All five end at KE896 *Parkinsonian motor deficits* and all five pass through
KE890 *Degeneration of dopaminergic neurons of the nigrostriatal pathway*. Four of the five
also share KE177 *Increase, Mitochondrial dysfunction*. What separates them is the entry point:

| AOP | Molecular Initiating Event | OECD status | Events | KERs |
|---|---|---|---|---|
| 3 | KE888 binding of inhibitor, complex I | **WPHA/WNT Endorsed** | 7 | 8 |
| 587 | KE1542 complex III inhibition | *(none)* | 4 | 3 |
| 588 | KE2118 succinate dehydrogenase (complex II) inhibited | *(none)* | 4 | 3 |
| 589 | KE1543 complex IV inhibition | *(none)* | 4 | 3 |
| 593 | KE2362 redox cycling of a chemical by mitochondria | *(none)* | 5 | 4 |

AOP 3 is the only one of the five that has been through OECD review, and it is also the only
one carrying a full record: AOPs 588 and 589 have **no references, no weight-of-evidence text
and no Key Event essentiality section at all**. Their respective MIE→KE177 relationships,
KER3554 and KER3555, both sit at `completion_score` exactly 29.41% — the value that, per the
`ker-evidence-triage` skill, is reachable only by a stub carrying endpoints and nothing else,
and which guarantees zero attached references. Two of the thirteen relationships in this
crosswalk are therefore assertions with no literature behind them on the wiki side.

An empty `oecd_status` is not a rejection — 447 of the 599 AOPs in this snapshot are empty,
meaning no review has happened. But the combination of no endorsement, no references and no
essentiality assessment on 588 and 589 means those two pathways contribute a hypothesis and
nothing else.

### The Key Events screen clean

All 12 Key Events were put through `event-content-internal-alignment` against the EMOD LinkML
level definitions. **Zero flags, zero notes, zero unchecked** — every one has a description,
and every description carries vocabulary consistent with its assigned level. No model review
was needed, and none of these Key Events belongs in the AOP-Wiki data-error inventory that
issue [#10773](https://github.com/monarch-initiative/dismech/issues/10773) collects. The levels
can be inherited as assigned: Molecular for the five MIEs, Cellular for KE887/KE2363/KE177/KE889,
Tissue for KE188, Organ for KE890, Individual for KE896.

## How a node was matched to a Key Event

Structure first, words second, and the basis is recorded either way:

- **`conforms_to`** into a module node that is itself the right mechanism (a whole-module
  prefix only counts when the conformed node's own name also fits the Key Event);
- **a GO, CL or UBERON binding** that the Key Event's own Event Components imply — for
  example KE1543's `GO:0004129` cytochrome-c-oxidase activity, or KE890 matching only a node
  binding `CL:0000700` *and* `UBERON:0002038` *and* naming degeneration;
- **a name or description cue**, as fallback.

Match counts below mix these, so a reader should discount name-only matches. The per-entry
TSV and `--format json` carry the basis for every match. KE896 is matched not on a node but on
the entry's own parkinsonian HPO phenotypes, since that is where dismech puts the adverse
outcome.

## Finding 1 — the MIE layer is the gap, and it is the whole difference between the five AOPs

| Key Event | Level | Entries (of 82) |
|---|---|---|
| KE888 binding of inhibitor, complex I | Molecular | **0** |
| KE2362 redox cycling of a chemical by mitochondria | Molecular | **0** |
| KE1542 complex III inhibition | Molecular | 1 |
| KE2118 complex II / SDH inhibition | Molecular | 1 |
| KE887 complex I inhibition | Cellular | 3 |
| KE1543 complex IV inhibition | Molecular | 6 |
| KE2363 elevated mitochondrial ROS | Cellular | 9 |
| KE188 neuroinflammation | Tissue | 16 |
| KE177 mitochondrial dysfunction | Cellular | 20 |
| KE889 proteostasis, impaired | Cellular | 36 |
| KE890 nigrostriatal DA degeneration | Organ | 14 |
| KE896 parkinsonian motor deficits | Individual | 82 |

The shape is the finding. The shared tail is well populated; the five entry points are
present on 0, 0, 1, 1 and 6 entries respectively. Since the MIE is the only thing
distinguishing these five AOPs, dismech currently cannot tell them apart — it holds one
mitochondrial-dysfunction-to-parkinsonism chain where AOP-Wiki holds five chemically distinct
initiations converging on it.

The two zeroes are absences of a node, not of a capability — which is worth establishing,
because a framework difference is the natural assumption and would be the wrong one. Whether
either absence should be filled is a separate question, answered under
*Does the evidence support the upstream chains* below.

**KE888** is inhibitor *binding* to complex I — a molecular target-engagement event, the kind
of thing a pathograph might be expected not to carry. It would be wrong to write it off that
way. A scan of all 27,493 pathophysiology nodes in `kb/disorders/` and `kb/modules/` finds 199
whose names denote binding or occupancy, including `Diphtheria Toxin Binding to the proHB-EGF
Receptor` — a toxicant binding its molecular target, structurally the same event type as
KE888. The Parkinson's Disease entry itself carries one: `Postsynaptic D2/D3 Receptor Occupancy
by Agonist Therapy`, bound to `GO:0001591` with `DRD2`/`DRD3`. So dismech models ligand
engagement as a node where a curator has judged it worth separating; for complex I inhibitor
binding, none exists.

**KE2362** (redox cycling) is the other zero. It is the one with a specific chemical attached
already in the PD entry — paraquat — which is why it gets its own section (Finding 3); but its
supporting evidence is in vitro and rat, not human.

## Finding 2 — the Parkinson's Disease entry holds the tail and fuses the front

`Parkinsons_Disease.yaml` matches 7 of the 12 Key Events, the most of any entry: KE887, KE2363,
KE177, KE889, KE188, KE890 and KE896. Its KE890 match is the strongest kind available —
`conforms_to parkinsonism_dopaminergic_degeneration#Nigrostriatal Dopaminergic Neurodegeneration`,
plus `CL:0000700` with `UBERON:0002038`, plus the name.

But its single `Mitochondrial Dysfunction` node matched **both** KE887 (complex I inhibition)
and KE177 (mitochondrial dysfunction), and the KE887 match came only from the name of the
module node it conforms to. The node's own binding is `GO:0007005` mitochondrion
organization — the general term. Its description says "particularly complex I deficiency" and
its genes are the mitochondrial-quality-control set (PINK1, PRKN, FBXO7, VPS13C, CHCHD2), which
is a different mechanism from respiratory-chain inhibition.

So the entry fuses AOP 3's KER934 (complex I inhibition → mitochondrial dysfunction) into one
node. That is a legitimate modelling choice, and it is the reason this crosswalk records match
bases: read as a Key Event mapping, the KE887 hit would wrongly suggest the entry represents
complex I inhibition as a distinct, bound event.

### The respiratory-chain vocabulary exists in dismech — in other entries

This is the most actionable thing in the crosswalk, and it only appears once you stop looking at
the parkinsonism entries. Each AOP's entry point was swept across all of `kb/disorders/`, by GO
term, and for complex II also by SDH subunit gene, because "succinate dehydrogenase" is what
dismech mostly calls it:

| Entry point | Nodes KB-wide | Entries | Overlap with the 82 |
|---|---|---|---|
| complex I (AOP 3) | 94 | 53 | **0** |
| complex II / SDH (AOP 588) | 18 | 14 | **0** |
| complex II by SDHx gene | 10 | 7 | **0** |
| complex III (AOP 587) | 5 | 4 | **0** |
| complex IV (AOP 589) | 76 | 44 | 6 |

Complex IV is the exception: six parkinsonism entries bind it, which is the same six that match
KE1543 above. Those six turn out to matter, because five of them carry AOP 589's otherwise
unevidenced causal edge — see *What dismech holds against those two empty edges* below. For
complexes I, II and III the overlap is zero. dismech curates respiratory-chain
inhibition in depth — the `Mitochondrial_Complex_I_Deficiency_Nuclear_Type_*` series, MELAS,
Leigh syndrome, the Leber optic neuropathies, ACAD9 deficiency, the complex II deficiency
entries, `Pheochromocytoma_Paraganglioma`, `Carney-Stratakis_Syndrome` — and
`Propofol_Infusion_Syndrome` models *xenobiotic* respiratory-chain inhibition directly
(`Mitochondrial Respiratory Chain Inhibition by Propofol`, bound to `GO:0006120`), which is
structurally KE887 with a different chemical. None of that work is attached to a parkinsonism
entry for complexes I, II or III.

**But this is a gap in bindings, not in knowledge, and it would be easy to over-read.** The
Parkinson's Disease entry's `Mitochondrial Dysfunction` node already cites
[PMID:2154550](https://pubmed.ncbi.nlm.nih.gov/2154550/) *Mitochondrial complex I deficiency in
Parkinson's disease*, classified `HUMAN_CLINICAL`, with the verified snippet "These results
indicated a specific defect of Complex I activity in the substantia nigra of patients with
Parkinson's disease." That is the same body of human post-mortem work AOP 3's own KER934
weight-of-evidence names as its human corroboration (Parker 1989, Schapira 1989, Greenamyre
2001, Sherer 2003).

dismech therefore already holds the human complex I claim for Parkinson's disease, with
evidence, at the level of a fused node. What it lacks is (a) the finer granularity that would
separate complex I inhibition from mitochondrial dysfunction as distinct events, and (b) the
chemical initiation arm upstream of both. Neither is a missing fact; the first is a modelling
choice and the second is the subject of the next section.

### For complex II the gap runs the other way

AOP 588 asserts complex II inhibition → mitochondrial dysfunction → nigrostriatal degeneration
with no evidence for its own first step. dismech holds a curated chain of exactly that shape,
better evidenced, that lands somewhere else.
`SDHA-Related_Neurodegeneration_With_Ataxia_And_Optic_Atrophy` runs:

> heterozygous SDHA missense at a conserved arginine → failure of covalent FAD attachment to the
> SDHA flavoprotein → catalytically inert SDHA competing for complex II assembly → approximately
> half-normal succinate dehydrogenase activity → bioenergetic failure in cells with low metabolic
> reserve → retinal ganglion cell and optic nerve degeneration / cerebellar degeneration and
> ataxia / striated muscle and myocardial energy failure

The target tissues are optic nerve, cerebellum and muscle. The entry's phenotypes are optic
atrophy, ataxia, myopathy and cardiomyopathy, and it binds no parkinsonian phenotype, which is
why it falls outside the 82. `Mitochondrial_Complex_II_Deficiency_Nuclear_Type_1` and `_Type_3`
route complex II loss to encephalopathy and cardiomyopathy, again not to the substantia nigra.

That is a substantive observation about AOP 588's unevidenced step rather than a bookkeeping
one. Selective nigrostriatal vulnerability is not generic to respiratory-chain inhibition:
AOP 3's own KER908 argues it from properties specific to SNpc dopaminergic neurons — autonomous
pacemaking activity, broad action potentials, calcium load. AOP 588 inherits that relationship
wholesale while supplying nothing for the complex II step that would reach it, and the dismech
complex II content that does exist routes the same lesion to other tissues. The combinatorial
assumption behind the AOP family — one AOP per respiratory complex, all ending in parkinsonism
— is exactly what needs the evidence that AOPs 588 and 589 do not carry.

## Does the evidence support the upstream chains, and could they be added?

This is the question the Key Event counts above invite and do not answer, so it is worth
answering directly: **no, these upstream nodes cannot be added by porting them across**, and the
reason differs by pathway.

Per-step evidence as AOP-Wiki holds it, read off the four evidence blocks on each relationship:

| Step | Biol. plausibility | Empirical support | Weight of evidence | Species basis |
|---|---|---|---|---|
| KER933 complex I binding → inhibition (AOP 3) | 1,398 ch | 6,391 ch | *(empty)* | isolated mitochondria, cells, in vivo |
| KER934 complex I inhibition → mito dysfunction (AOP 3) | 1,107 ch | 39,455 ch | "strong" | in vitro + in vivo + **human post-mortem** |
| KER3637 complex III → mito dysfunction (AOP 587) | 4,037 ch | 14,555 ch | "strong" | **in vitro only** (LUHMES, HepG2 Seahorse) |
| KER3554 complex II → mito dysfunction (AOP 588) | **0** | **0** | **0** | **none — no references at all** |
| KER3555 complex IV → mito dysfunction (AOP 589) | **0** | **0** | **0** | **none — no references at all** |
| KER3629 redox cycling → mito ROS (AOP 593) | 3,334 ch | 5,116 ch | "strong" | in vitro + rat ex vivo |

Every figure in that table is AOP-Wiki's own record of its own edge. For KER3555 the zeroes say
what the wiki holds, not what is known: dismech carries that step with cited human evidence, as
*What dismech holds against those two empty edges* sets out below.

Three distinct situations, and they call for different answers.

**AOP 3's complex I chain is genuinely well evidenced, and dismech already has its human core.**
KER934 cites human post-mortem PD brain, KER908 rests partly on "analysis of mitochondria from
PD patients" and impaired complex I activity in patient substantia nigra, muscle and platelets,
and KER910 draws on human clinical observation. AOP 3's taxonomic applicability is human and
rat. As the previous section shows, the PD entry already carries that human citation. There is
no evidence to go and find here for the human claim — the open question is whether to split one
fused node into two, which is a modelling decision, not a literature task.

**AOP 587 and 593 are evidenced in model systems, not in human disease.** AOP 587's empirical
support is explicitly NAM assay data — permeabilised LUHMES and HepG2 cells on Seahorse, read
for complex III inhibition — with quantitative understanding derived by qAOP modelling. AOP
593's support is in vitro paraquat work in rat primary mesencephalic cells and the N27 line,
plus rat ex vivo mitochondria, with in vivo evidence resting on lipid peroxidation and oxidised
protein accumulation. These are real experiments, and they are not human disease evidence. An
upstream node asserted in a human disease entry on this basis would be making a stronger claim
than the cited work supports, which is precisely the gap the PD entry's own `exposure_route`
notes already flag: the human pesticide data are chronic and low-dose associations, while the
mechanistic experiments are acute and high-dose.

**AOP 588 and 589 have no evidence whatsoever.** Not thin evidence — four empty evidence blocks
and zero references on KER3554 and KER3555, at the 29.41% stub value. The causal step those two
AOPs are named for is unevidenced on the wiki. Anything derived from them would be sourced
entirely from scratch, and the AOPs give no starting bibliography to do it from. These two are
not merely under-documented: they are unfilled slots, and the next section sets out the evidence
for saying so.

## AOPs 588 and 589 are unfilled slots in a network expansion

These two deserve stating on their own, because a graph view of either one looks like a
four-event pathway from a chemical to a human motor syndrome, and almost none of it is theirs.

**What is unique to each AOP, and what it borrowed.** Each has three Key Event Relationships.
Two of the three are inherited from the OECD-endorsed AOP 3 and are substantially evidenced;
the third is the only one that is theirs, and it is empty:

| AOP 588 | Status | Evidence text | References |
|---|---|---|---|
| KER3554 complex II → mito dysfunction | **unique to AOP 588** | **0 ch** | **0** |
| KER908 mito dysfunction → DA degeneration | inherited (AOP 3, 587, 589) | 49,571 ch | 18,738 ch |
| KER910 DA degeneration → motor deficits | inherited (AOP 3, 587, 589, 593) | 31,814 ch | 15,552 ch |

AOP 589 is identical in shape: KER3555 (complex IV → mitochondrial dysfunction) is unique to it
and carries zero evidence text and zero references, while KER908 and KER910 are the same
inherited, well-evidenced edges. So in both cases **the one causal step the AOP exists to
assert is the one step with nothing behind it.** The rest is AOP 3's evidence, reused.

Their Molecular Initiating Events are real, developed Key Events — KE2118 (succinate
dehydrogenase, inhibited) scores 100% complete and is used in four other AOPs, mostly liver
toxicity; KE1543 (complex IV inhibition) scores 41.67% and appears in AOP 273. Neither is the
problem. The missing thing is any stated basis for connecting them to nigrostriatal
degeneration.

**Where they came from.** The provenance is legible in fields the CLI does not expose, read
directly from the XML export:

| AOP | Created | Last modified | Developed after creation? | XML size |
|---|---|---|---|---|
| 587 (cIII) | 2025-08-01 | 2025-12-08 | yes, over ~4 months | 106,728 ch |
| **588 (cII)** | 2025-08-01 | **2025-08-01** | **no — same day, never since** | **7,800 ch** |
| **589 (cIV)** | 2025-08-01 | **2025-08-01** | **no — same day, never since** | **7,800 ch** |
| 593 (redox) | 2025-08-20 | 2025-10-03 | yes, over ~6 weeks | 111,327 ch |
| 3 (cI) | 2016-11-29 | 2025-10-04 | yes, over ~9 years | 246,475 ch |

All three complex-variant AOPs were created on 2025-08-01. The complex III one was developed
over the following four months. The complex II and complex IV ones carry a last-modification
date equal to their creation date and have not been edited in the fourteen months between then
and the 2026-10-03 snapshot this report reads, so
nothing was added after the record was opened. Their XML representations are 7,800 characters
each, identical in size to one another and about 7% the size of their developed sibling, which
is what a structural clone looks like.

Only dates are reported here. The export also carries each record's editing times and its named
point of contact; those identify individual people's working patterns, are not needed for any
finding in this report, and are deliberately left out.

AOP 587's own abstract states the intent: it "is developed upon the previously endorsed AOP3
(focused on complex I inhibition) and expands the AOP network to include cIII as a molecular
initiating event." The background on 587 and 593 attributes the work to an EFSA project
following the pesticide–parkinsonism literature. So the family is deliberate: take the endorsed
complex I pathway and extend it to the other respiratory complexes. Four slots were opened; two
were filled.

**Are they hypotheses?** Two senses of the word, and they give different answers.

Every AOP is a hypothesis in the framework's own terms — a structured, evidence-weighted
proposal about a causal chain, which is exactly why weight-of-evidence assessment and OECD
endorsement exist. Nobody should read any AOP, endorsed or not, as settled fact.

But 588 and 589 are not hypotheses in that sense either, because an AOP-as-hypothesis carries a
stated rationale and some weight-of-evidence judgement, however provisional. These have no
abstract, no background, no named authors, no overall assessment, no Key Event essentiality, no
weight-of-evidence summary, no quantitative considerations, no potential applications and no
stressors — nine empty free-text fields, and 26.32% completeness. They assert a title. The
right reading is a placeholder: a slot opened to complete a combinatorial set, where the
scientific case was never made and may never have been intended to be made by these records.

**The practical warning.** AOP-Wiki has no field that distinguishes a placeholder from a
finished pathway. The `status` field carries the license and, for AOP 3, the endorsement
("BY-SA WPHA/WNT Endorsed") — it does not carry a development stage, and 587, 588, 589 and 593
all read simply "BY-SA". An empty `oecd_status` means no review has happened, which is true of
447 of the 599 AOPs in this snapshot and says nothing about whether a record was ever worked on.
So a consumer of this data who filters on endorsement, or on event and relationship counts, or
on a rendered graph, will see AOPs 588 and 589 as four-event chemical-to-disease pathways
indistinguishable in shape from AOP 587. Completeness score, per-KER evidence blocks and the
last-modification date are what separate them, and only the first of those is exposed by the
CLI. Exposing the modification *date* would add real screening value; the sub-day editing times
in the same records should stay out, since they describe individual contributors rather than the
state of the science.

### What dismech holds against those two empty edges

The symmetry stops here. "Neither knowledge base has it" would be the tidy conclusion, and it is
true for AOP 588 and false for AOP 589.

For **AOP 588's** unique edge (KER3554, succinate dehydrogenase → mitochondrial dysfunction),
one of the 82 entries has the upstream end and no route to the downstream one: Manganism, whose
`Microglial Complex II-Dependent Reactive Oxygen Species Production` matched on its name alone.
Nothing else in the parkinsonism set touches it. That edge is unevidenced in AOP-Wiki and
unrepresented in dismech.

For **AOP 589's** unique edge (KER3555, complex IV inhibition → mitochondrial dysfunction),
dismech covers it directly in five entries, each as two distinct nodes with a causal edge between
them, and all five bind `HP:0001300` parkinsonism:

| Entry | Upstream node → downstream node | Lesion | Strongest cited evidence |
|---|---|---|---|
| Carbon_Monoxide_Poisoning | Cytochrome c oxidase inhibition → Cellular energy failure | chemical inhibition | `PMID:9584335` **HUMAN_CLINICAL** — "76% inhibition compared to controls during acute poisoning (P < 0.01) and 48% at day 3" |
| Cyanide_Poisoning | Cytochrome c Oxidase Inhibition → Oxidative Phosphorylation Failure and ATP Depletion | chemical inhibition | `PMID:41204534` HUMAN_CLINICAL on the edge; `PMID:17906319` IN_VITRO on the node |
| Methanol_Poisoning | Cytochrome c oxidase inhibition by formate → Cellular energy failure | chemical inhibition by a metabolite | `PMID:12216995` — formate as the proximate inhibitor |
| FASTKD5-Related_COX_Deficiency | Reduced complex IV activity → Impaired mitochondrial respiration | assembly defect | muscle-biopsy OXPHOS assay, HUMAN_CLINICAL; `PMID:34748562` IN_VITRO respirometry |
| Autosomal_Dominant_Progressive_External_Ophthalmoplegia | Threshold-Dependent Mosaic Respiratory Chain Deficiency → Skeletal and Bulbar Mitochondrial Myopathy | mtDNA-maintenance failure | `PMID:20479361` HUMAN_CLINICAL — COX-deficient fibres in skeletal muscle |

A sixth entry, `Parkinson_Disease_Mitochondrial`, matches **both** ends of the edge on a single
node — `Respiratory Chain (Oxidative Phosphorylation) Deficiency`, bound to `GO:0006119` and
`GO:0004129` together — so the crosswalk scores it `same node` and it is not one of the five.
`PMID:11079536` records reduced cytochrome c oxidase activity in the proband's lymphocytes.

**Only three of the five are complex IV inhibition in the sense AOP 589's molecular initiating
event means it.** Carbon monoxide, cyanide and formate inhibit the enzyme. FASTKD5 deficiency
impairs its assembly. adPEO's lesion is clonal mtDNA deletion crossing a threshold, past which
none of the thirteen mtDNA-encoded oxidative phosphorylation subunits can be made, so
COX-negative fibres are its readout rather than its mechanism — the same shape of lesion as
`Parkinson_Disease_Mitochondrial`'s. Those three chemical entries are the stressor class the AOP
framework exists to serve, and the carbon monoxide entry carries a quantified, time-resolved
human measurement of chemical complex IV inhibition. **The causal step AOP 589 asserts without a single reference is
one dismech already represents with cited human evidence.** For this edge the AOP contributes the
chain shape and dismech contributes the evidence, which is the reverse of the pattern everywhere
else in this report.

**Two limits, and the second is the substantive one.**

First, KE890 — nigrostriatal dopaminergic degeneration — is absent from four of the five, so in
those four the chain from the complex IV lesion to the motor outcome is broken in the middle.
adPEO is the exception: it carries a `Nigrostriatal Dopaminergic Degeneration` node and reaches it
from the respiratory-chain lesion in three hops, via `Multisystem PEO-Plus Extension`. It is also
the entry whose lesion is least like complex IV inhibition, so the one case that completes the
chain is the one that fits the molecular initiating event worst.

Second, and more interesting than a gap: where these entries *do* reach parkinsonism, they do not
reach it the way AOP 589 assumes. Cyanide_Poisoning carries a complete chain —

```
Cytochrome c Oxidase Inhibition → Oxidative Phosphorylation Failure and ATP Depletion
  → Cerebral Energy Failure → Excitotoxic Neuronal Injury → Basal Ganglia Necrosis → Parkinsonism
```

— and it routes through **basal ganglia necrosis**, not selective nigral dopaminergic loss.
Methanol_Poisoning has a `Basal ganglia injury` node and Carbon_Monoxide_Poisoning has
`Cerebral hypoxic-ischemic injury`, `Delayed demyelination` and `Delayed neuronal injury`; in
both, the bound parkinsonism phenotype has no causal inlink at all.

AOP 589 inherits KER908 (mitochondrial dysfunction → dopaminergic degeneration) from AOP 3, where
the supporting evidence is about complex I, rotenone and MPTP acting on the substantia nigra.
Applying that inherited edge to complex IV inhibition assumes the same selective nigral route,
while the three human chemical presentations dismech records instead describe basal ganglia
necrosis and delayed hypoxic injury. So the unevidenced edge is the fillable one, and the
well-evidenced inherited edge is the one whose transfer to a different complex needs an argument
that no AOP 589 field makes. That argument is exactly what the missing weight-of-evidence and Key
Event essentiality fields would have had to contain.

### And AOP-Wiki can never be the citation

Independently of all of the above: there is no `AOP:` prefix in `references_cache/`, no fetcher
and no cacheable body for a snippet to match, so an AOP, Key Event or KER page cannot be an
evidence `reference:` in dismech. Every edge needs its own primary literature and a verified
exact snippet regardless of how strong the wiki record looks. What the AOP records give is a
starting bibliography — and for AOP 3 a good one, naming specific fetchable human papers, one
of which the PD entry already cites.

So, to answer the question in order: the evidence behind AOP 3's chain is strong and partly
human; the evidence behind AOPs 587 and 593 is solid but model-system only; and the evidence
behind the edges unique to AOPs 588 and 589 does not exist *in AOP-Wiki*. For AOP 588's edge it
does not appear to exist anywhere in this corpus. For AOP 589's edge it exists in dismech, cited
and partly human, which makes that one a candidate for the opposite exercise — AOP-Wiki taking
evidence from dismech rather than the other way round. None of it can be cited from AOP-Wiki
itself. And the one chain whose human claim is well supported is the one dismech already
represents, only more coarsely.

## Finding 3 — paraquat is named without its mechanism

The PD entry is the **only one of the 82** that names any of these AOPs' prototypical
stressors. Its `environmental` block names rotenone and paraquat; across the other 81 entries,
MPP+/MPTP, deguelin, pyrimidifen, fenpyroximate, tebufenpyrad, antimycin A and picoxystrobin
appear nowhere (MPTP does appear in PD evidence snippets as a model system, which is a
different role from an exposure).

Paraquat is the specific case worth noting. It sits in the PD `chemicals` list, and the entry's
sole `influences_mechanisms` edge for pesticide exposure targets `Mitochondrial Dysfunction`.
AOP 593 — the one AOP whose MIE is paraquat's actual stressor entry — routes it differently:
KE2362 redox cycling → KE2363 mitochondrial ROS → KE889 impaired proteostasis → KE890. dismech
has the destination and not the route, so paraquat currently enters the pathograph through the
same single edge as every other pesticide.

Two guardrails on acting on this. AOP-Wiki is not a citable reference in dismech — there is no
`AOP:` prefix in `references_cache/` and no fetcher — so a redox-cycling node would need its own
primary literature. KER3629 does carry a substantial reference list (≈12,000 characters, 68
year-bearing entries, opening on paraquat oxidative-stress papers), which is a starting
bibliography for that work rather than a substitute for it. And the entry's own `exposure_route` notes already
record that the human pesticide evidence is chronic and low-dose while the mechanistic
experiments are acute and high-dose; adding a mechanism does not close that gap.

## Finding 4 — KER910 is the step dismech splits, and sometimes drops

KER910 (KE890 → KE896) is the one relationship carried by **all five** AOPs. Across the 82:
6 entries assert it directly, 4 reach it indirectly, 4 have both ends and no causal path,
and 68 lack one end.

The 4 indirect cases are not defects. dismech routinely models the step at higher resolution
than the AOP does — PD goes `Dopaminergic Neuron Loss → Striatal Dopamine Deficiency → Basal
Ganglia Circuit Dysfunction → Resting Tremor`, three edges where AOP-Wiki draws one. The
crosswalk tracks the striatal-dopamine and basal-ganglia bridge nodes separately so that this
reads as finer granularity rather than a missing edge.

The 4 both-ends-no-path cases are different, and they are the ones worth a look, because each
has a terminal nigrostriatal-degeneration node and parkinsonian phenotypes with nothing joining
them: **PARK7-Related Early-Onset Parkinson Disease**, **PRKN-Related Juvenile Parkinson
Disease**, **Infantile Parkinsonism-Dystonia** and **Machado-Joseph Disease**.

## Finding 5 — AOP 3's neuroinflammation feedback loop is one-directional in dismech

AOP 3 carries both KER907 (KE890 → KE188) and KER906 (KE188 → KE890): degeneration drives
neuroinflammation, which drives further degeneration. dismech holds the second direction and
not the first. Across the 82, KER906 has 1 direct assertion and KER907 has **none**.

The PD entry is a clean instance: `Neuroinflammation → Dopaminergic Neuron Loss` and
`Reactive Astrogliosis → Dopaminergic Neuron Loss` are both asserted, and no edge runs from
`Dopaminergic Neuron Loss` back to any of its three glial nodes. Whether the feed-back arm is
worth asserting is a curation question this report does not answer — but the asymmetry is
currently implicit rather than decided.

Separately: `kb/modules/neuroinflammation_glial_activation.yaml` was created specifically to
close the KE 188 gap (issue [#10368](https://github.com/monarch-initiative/dismech/issues/10368)),
and the PD entry's own `Neuroinflammation` node does **not** conform to it. Of the 16 entries
matching KE188, the module conformance is what several of them are missing.

## Finding 6 — the adverse outcome is stranded on 39 of 82 entries

This is a slice of an already-tracked problem, not a new one. `causal_inlink_coverage` — the
metric behind `just list-disconnected-phenotypes` (issue
[#11935](https://github.com/monarch-initiative/dismech/issues/11935)) and the gating
`compliance-connectivity` score — supplies the connectivity here, so these numbers cannot
disagree with those recipes. Over the 82 entries, 927 of 1,528 phenotypes are causally
connected (60.67%).

What the corpus view cannot show is that the stranded phenotype is often *the adverse outcome
itself*. **39 of the 82 entries leave at least one parkinsonian phenotype with no causal edge
explaining it**, which means KE896 has no anchor in the pathograph on half this set.

The sharp subset is the entries that clearly do wire phenotypes and still leave parkinsonism
dangling — where this is unlikely to be a deliberate "mechanism genuinely unknown" judgement:

| Entry | Entry-level connectivity | Stranded |
|---|---|---|
| CANVAS | 94.4% | Parkinsonism |
| Huntington Disease | 83.7% | Juvenile-Onset Parkinsonism |
| Striatal Degeneration, Autosomal Dominant 2 | 75.0% | Parkinsonism |
| Spinocerebellar Ataxia 27A | 73.3% | Parkinsonism |
| Dravet syndrome | 68.0% | Parkinsonism, Rigidity, Bradykinesia, Cogwheel Rigidity |
| ATP6V0C-Related Epilepsy | 67.9% | Parkinsonism |
| Dihydropyrimidinase Deficiency | 64.3% | Parkinsonism |

At the other end, four entries named for parkinsonism have **0%** phenotype connectivity —
PARK7, PRKN, Infantile Parkinsonism-Dystonia and Corticobasal Syndrome. Three of those four are
the entries Finding 4 surfaces from the other direction; the two lists differ in the fourth, which
is Machado-Joseph Disease in Finding 4 and Corticobasal Syndrome here. "Named for parkinsonism"
means the entry's own label carries parkinsonism or an equivalent, which is what makes a missing
mechanism notable; other entries also sit at 0% — Methanol and Carbon Monoxide Poisoning, Chronic
Traumatic Encephalopathy and several spinocerebellar ataxias among them — without parkinsonism
being what they are named for.

As the `check_disconnected_phenotypes` docstring argues, an edge added to clear a report is
worse than no edge, and some of these may be legitimate. Triage, not a backlog.

## Where the richest overlap already is

Entries holding 5 or more of the 12 Key Events, i.e. where a cross-framework mapping would
have the most to attach to:

| Entry | KEs | Which |
|---|---|---|
| Parkinson's Disease | 7 | 887, 2363, 177, 889, 188, 890, 896 |
| Manganism | 6 | 2118, 2363, 177, 889, 188, 896 |
| Carbon Monoxide Poisoning | 5 | 1543, 2363, 177, 188, 896 |
| FASTKD5-Related COX Deficiency | 5 | 887, 1542, 1543, 177, 896 |
| Huntington Disease | 5 | 2363, 177, 889, 188, 896 |
| Multiple System Atrophy | 5 | 177, 889, 188, 890, 896 |
| PARK7-Related Early-Onset PD | 5 | 887, 2363, 177, 890, 896 |
| PRKN-Related Juvenile PD | 5 | 2363, 177, 889, 890, 896 |

Two of these are worth singling out. **Manganism** is the only entry matching KE2118
(complex II / SDH inhibition), through its `Microglial Complex II-Dependent Reactive Oxygen
Species Production` node — and it reaches the adverse outcome through
`Basal Ganglia Output Failure`, which conforms to the parkinsonism module. It is the closest
thing in the KB to a complete toxicant-initiated parkinsonism chain, and it is the natural
counterpart to AOP 588, the skeletal one. **FASTKD5-Related COX Deficiency** is the only entry
matching three different respiratory-complex Key Events at once, which makes it the natural
counterpart to AOPs 587 and 589 — though its parkinsonism phenotype is stranded (17.6%
connectivity).

## Caveats

- **AOP-Wiki is not a dismech reference.** No `AOP:` prefix, no fetcher, no cacheable body for
  a snippet. Anything curated from this crosswalk needs primary literature and a verified exact
  snippet, per the `dismech-references` skill. The `references` blobs on these AOPs and KERs are
  a starting bibliography, and AOP-level citations cannot be attributed to a specific edge.
- **AOP ontology terms are leads, not bindings.** KE `cell_term`/`organ_term` mix UBERON with
  plain strings, and Event Components draw on MESH, GO, CHEBI, PR, HP and MP. Every one needs
  re-resolving under the `dismech-terms` rules.
- **An AOP is a hypothesis about a causal chain.** For four of these five, nobody external has
  reviewed it, and for two there is no attached literature at all.
- **Match counts mix structured and name-only bases.** Discount accordingly; the JSON and TSV
  carry the basis per match.
- **The respiratory-complex sweep is a binding sweep, not a content search.** It finds nodes
  carrying the relevant GO terms, plus SDH subunit genes for complex II. An entry discussing a
  complex in prose without binding it is not counted, so the KB-wide figures are a floor.
- **The placeholder reading of AOPs 588 and 589 is an inference from metadata**, not a statement
  from their authors. The empty fields, the 29.41% stub relationships and the creation and
  modification dates are facts in the export; "a slot opened to complete a combinatorial
  set" is the most economical explanation of those facts, and AOP 587's abstract supports it by
  describing the family as a network expansion. It remains an inference, and the records may yet
  be developed. Dates are as the 10-03-2026 export reports them.
- **The 82-entry selection is phenotype-driven** (parkinsonism, or bradykinesia with a second
  cardinal sign, by HPO descendant closure). An entry with parkinsonian pathophysiology but no
  bound parkinsonian phenotype is outside it.

## What this report does not do

It proposes no nodes, files no issues, and asserts no edges. It does not judge whether any Key
Event is the right one for a dismech entry — the level screen checks each Event against itself,
and the crosswalk checks what is already present. The curation questions it raises — the
disjunction between the complex I entries and the parkinsonism entries, the redox cycling route
for paraquat, the neuroinflammation feedback arm, the 39 stranded adverse outcomes, the missing
module conformances — are for triage item by item, not a backlog to work through.
