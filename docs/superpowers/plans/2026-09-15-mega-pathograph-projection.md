---
title: Projecting Every Pathograph into One Cross-Disease Mega-Pathograph
status: PLAN
description: >-
  A design for collapsing all 4,443 dismech pathographs into a single
  cross-disease graph in which a mechanism curated once per disease becomes one
  node. Revised 2026-11-23: dismech-owl already builds this as an OWL TBox and
  covers four of the five identity rungs by subsumption, so the plan is
  retargeted from a parallel projection to an aggregation layer over the
  reasoned TBox, plus a KGX profile for partners who consume nodes and edges.
tags: [PATHOGRAPH, GRAPH_PROJECTION, MODULES, CONFORMS_TO, OWL, KGX, PLAN]
---

# Projecting Every Pathograph into One Cross-Disease Mega-Pathograph

**Status: plan.** Nothing here changes `kb/` or the schema. The artifact is
derived, rebuildable, and throwaway by design.

Reproduce every number below with:

```bash
uv run python scripts/megagraph_prototype.py                    # summary JSON
uv run python scripts/megagraph_prototype.py --format tsv       # merged edges
```

Measured at `b53abfd9b3` over `kb/disorders`, `kb/modules`, `kb/comorbidities`.
**The figures in this plan were re-measured on 2026-11-23**; the first version
measured `643d3e5ab` (2026-09-15), when the corpus was 3,152 entries against
today's 4,443. Where the revision changes a conclusion rather than a number,
§6 says so.

---

## 1. The problem is not string matching

A pathograph node is not a mechanism. It is a claim about a mechanism **in one
disease**, and its evidence, its organ, its modifier and its position in that
disease's cascade are all part of what it asserts. Merging two nodes discards
whichever of those differ. So the design question is not "how do we match
nodes" but "what survives the match, and where does the rest go".

Three cases must be kept apart. Collapsing any one of them destroys content
silently.

| Case | Real example | Correct handling |
|---|---|---|
| Same mechanism, different substrate | `fibrotic_response#Mesenchymal Cell Activation` realized as hepatic stellate cell in cirrhosis, myofibroblast in pulmonary fibrosis | **Merge.** Substrate is a qualifier of the instance. This is what `conforms_to` already encodes. |
| Same name, different mechanism | *Mitochondrial Dysfunction*, *Immune Evasion*, *Neuroinflammation* each recur across a dozen-plus entries | **Never merge on the name.** Different claims sharing a label. |
| Same term, different causal role | `GO:0006915` apoptosis as the driving lesion vs. as a terminal consequence | **Never merge on the term alone.** Fuses a cause with its own effect — measurable as a self-loop. |

---

## 2. dismech-owl already builds this, in OWL

[`monarch-initiative/dismech-owl`](https://github.com/monarch-initiative/dismech-owl)
builds a pathograph TBox from a pinned dismech checkout: every node in every
causal graph becomes an OWL class, placed under the node-class tree in
`kb/node_classes/pathograph_node_classes.txt`. It publishes weekly releases
(`dismech-pathograph.ofn.gz`, ~200 MB unpacked; a reasoned build merged with GO
and MONDO modules and classified with ELK, ~280 MB).

**It answers the identity question by subsumption rather than by merging.** Node
IRIs are `…/node/<entry>/<kind>/<slug>` — one class per disease-local node — and
there are **zero `EquivalentClasses` axioms in the whole build**. Nothing is ever
asserted to be the same thing as anything else. Two nodes are connected because
both are *kinds of* a shared parent.

That covers four of the five rungs this plan proposed, and covers them better:

| Rung (§4) | What dismech-owl does instead |
|---|---|
| 1–2 module / `conforms_to` | `conforms_to: module#Node` → `SubClassOf <module node>`. The module class **is** the canonical concept, and the multivalued slot is handled. |
| 3 HP term | `phenotype_term` → `SubClassOf <HP term>` directly, via `KIND_TERM_SLOTS`. Every disease's seizure node is a kind of `HP:0001250`. |
| 4 core terms | Descriptor restrictions `<slot> some (<term> and modifier value <M>)`, plus the node-class tree's 46 `= expression` **defined classes** — ELK finds the members. |
| 5 name-only | Not done, and rightly not. |

Its `tbox.py` even states the core-versus-context rule this plan derived
empirically, as a design decision: *"The node is a kind of its bound term where
the term names the same kind of thing (a disease-specific seizure is a seizure);
elsewhere the term is related by its slot (a genetic node is not a gene)."*
That is the rule whose absence collapsed 207 unrelated nodes onto *neuron* in
the first prototype (§6).

### Where it is better than this plan's original design

- **A named defined class beats a hashed term signature.** Rung 4 keyed on a
  hash of a node's CURIE set: opaque, unstable, and it manufactured self-loops.
  The tree's logical definitions do the same job as readable axioms that a
  curator can argue with, and the lift is measured: on dismech-owl's pinned ref,
  **2,378** pathophysiology nodes carry an asserted tree class and **10,497 of
  23,853 (44%)** do after ELK, with **1,839 in two or more tiers** — which is
  the debundle signal, found by reasoning rather than by a conflict heuristic.
- **Its IRIs are stable.** They derive from entry slug plus node name, not from
  annotations, so they do not churn when a curator adds a GO term. That is the
  identifier problem §7 has to solve, already solved.
- **It never asserts two curators' nodes are identical** — the claim rungs 4 and
  5 were least entitled to make.

### What OWL structurally cannot do

From 22 subclasses each asserting a local `causes` edge, no reasoner infers
*"the module node causes the other module node, with 22 diseases behind it"*.
That is induction over instances, not deduction. Every distinctive output of
this plan is therefore outside dismech-owl's reach, and none of them is a reason
to build a rival projection:

- edge aggregation with support counts, and the module-mediated vs. independent
  split (§5);
- the curation worklists that fall out of it (§8, phase 3);
- a flattened node-and-edge serialization for partners who do not ingest a
  200 MB OFN (§7).

---

## 3. Revised design: an aggregation layer over the reasoned TBox

The original design read `kb/` and minted its own concept per node. **Do that
only for what dismech-owl leaves undone.** The retargeted shape:

1. **Read the reasoned OFN**, not the YAML, for identity. A concept is a class
   in the inferred hierarchy — a module node, an HP term, a tree class, or a
   defined class — and its instances are its inferred subclasses. Rungs 1–4
   come for free, and they come auditable.
2. **Lift each entry-local edge to its parents and count.** For every asserted
   `src SubClassOf causes some tgt`, walk `src` and `tgt` up to their named
   ancestors and record one supported edge per ancestor pair, carrying the set
   of entries behind it. This is the induction OWL declines to perform, done
   explicitly and labelled as such.
3. **Keep the disease-local node primary.** It holds the evidence; the lifted
   edge holds only a count and the list of assertions it counted. Same
   decomposability contract as an evidence snippet.
4. **Emit nothing as a merge that the ontology calls a specialization.** The
   aggregate says "22 diseases drew an edge between descendants of these two
   classes", never "these nodes are the same node".

Two consequences worth stating plainly. The identity ladder stops being the
centre of the design and becomes a fallback for the nodes OWL leaves
unclassified. And the over-merge failure modes in §6 largely disappear, because
lifting to a *named* ancestor cannot invent a parent — where a lifted edge does
land on one class at both ends, that is a genuine debundle signal, which is the
same thing dismech-owl's 1,839 two-tier nodes are reporting.

---

## 4. The identity ladder, and what is left of it

Rungs in descending confidence, with current node counts. Every concept records
**which rung fired**, so a consumer can threshold on provenance rather than
trusting the merge wholesale.

| Rung | Key | Node instances | Confidence |
|---|---|---:|---|
| 1. `module_node` | the module node itself, `stem#Name` | 1,302 | definitional |
| 2. `conforms_to` | the module node it declares | 4,673 | **curator-asserted** |
| 2b. `conforms_to_multi` | the whole set, when several are declared | 33 | curator-asserted |
| 3. `hp_term` | the HP CURIE of a phenotype | 55,702 | high — HP *is* the shared vocabulary |
| 4. `core_terms` | identity-bearing CURIEs (GO, CHEBI, HGNC, NCIT, ECTO) keyed with CL/UBERON context | 45,143 | medium |
| 5. `name_only` | normalized name, within one node type | 19,201 | low — never merges across node types |

`conforms_to` became multivalued since the first draft: 33 nodes declare more
than one module anchor. They key on the **whole sorted set**, never on the first
anchor, because a node claiming two conserved mechanisms is exactly the
lump/split signal the module system exists to surface. dismech-owl handles the
same case by emitting both `SubClassOf` axioms, which is the better answer — the
node is a kind of both — and is another reason §3 prefers the TBox as the source
of identity.

**The load-bearing rule is the split between core and context prefixes.** `CL`
and `UBERON` qualify an identity and can never establish one. Rung 5 is a
deliberate floor: 19,201 nodes carry no identity-bearing grounding, and they
join as singletons rather than being dropped, because a node missing from the
projection is invisible while a node that merged with nothing is a visible
curation gap.

---

## 5. What the projection yields today

| | raw | merged |
|---|---:|---:|
| entries | 4,443 | — |
| nodes, all types | 126,054 | **50,044** (60.3% smaller) |
| edges | 100,319 | 90,686 |
| unresolved targets | 84 | — |

- **9,541 concepts span two or more entries.** That is where "curated once per
  disease" becomes one node, and it is the number worth quoting — not the 60%
  compression, which is dominated by phenotype and treatment bookkeeping.
- **One giant component of 44,132 nodes.** The corpus is already a single
  connected object; it has never been drawn as one.
- **No concept mixes node types.** 389 concepts swallowed both ends of a causal
  edge and show up as self-loops — the over-merge detector, not noise.

### Edge convergence

Of 90,686 merged edges, 3,863 carry two or more entries:

| Edge class (support ≥ 2) | Count |
|---|---:|
| touching a module node — asserted via `conforms_to` | 1,937 |
| touching a treatment node | 738 |
| **pathophysiology → pathophysiology, no module involved** | **127** |
| self-loops (over-merge artifacts) | 17 |

At support ≥ 3 the independent class is **21 edges**.

**Module-mediated edges are partly tautological**: diseases conforming to one
module reproduce its chain because conformance asks them to. Reporting 1,937 as
discovered convergence would be counting the curators' own instruction back to
them. Count them separately, always.

**The independent class is growing faster than the corpus.** In September it was
54 edges (7 at support ≥ 3) over 3,152 entries; it is now 127 (21 at ≥ 3) over
4,443 — entries up ~41%, independent convergent edges up ~135%. The original
draft's conclusion was that independent convergence is "genuinely rare"; the
honest revision is that it is **rare but superlinear in corpus size**, which is
what you would expect if convergence requires two curators to have independently
reached the same mechanism. It is still two orders of magnitude below the node
convergence figure.

So the framing stands: **the mega-pathograph is a curation instrument first and
a consensus map second.** Its highest-value outputs are the places where
convergence should exist and does not — concepts with many instances and no
module, nodes whose key matches a module node but which carry no `conforms_to`,
disease pairs with high genetic correlation and zero shared concepts, and the
ungrounded nodes ranked by how many neighbours grounding would join them to.

---

## 6. Four ways the merge goes wrong

Each was found by running the prototype, not predicted. Note that §3 removes the
first and fourth by construction, because lifting to a named ancestor cannot
invent a parent.

**1. Context used as identity.** Letting a bare `CL` term key a node collapsed
207 unrelated nodes onto *neuron* — among them *Olivopontocerebellar
Neurodegeneration* and *Cerebellar Purkinje Cell Circuit Dysfunction*, which
share a cell type and nothing else. Fix: `CL` and `UBERON` are context prefixes.

**2. Generic action terms as treatment identity.** Keyed on `treatment_term`,
`NCIT:C15747` (Supportive Care) merges 1,596 treatment nodes into one and
`NCIT:C15240` (Genetic Counseling) 1,407. Every path through those is an
artifact of shared vocabulary. Fix: treatment identity keys on
`therapeutic_agent` and `regimen_term`, never the action term.

**3. Names, in both directions.** Name identity is neither sufficient nor
necessary: one name covers many mechanisms (*Mitochondrial Dysfunction*), and
one mechanism wears many names — **27 distinct names across the 31
`fibrotic_response#Mesenchymal Cell Activation` conformers**.

**4. Same term, different position in the cascade.** A concept keyed on a
process term alone can swallow both ends of an edge: 389 self-loops in the
current build. Inflammation drives a lesion in one entry and is the lesion's
consequence in the next. The tree's `modifier`-aware defined classes are a
better discriminator than a term set, which is §3's point.

---

## 7. A KGX profile for partners who consume nodes and edges

A partner working at KGX abstraction — nodes and edges with metadata, merged
across sources on CURIE — cannot ingest a 200 MB OFN, and the obvious
flattening is wrong. Measured: expressing every concept as a bare ontology CURIE
drops the edges whose endpoints are ungrounded, and collapsing multi-term
concepts onto a single anchor term manufactures self-loops and conflates
distinct concepts. It is also semantically false: `GO:0007179` means the GO
class, not "TGF-beta signalling as it misfires with `modifier: INCREASED`".

The profile that works:

- **One node per concept, with its own identifier, joinable by `xref`.**
  Take the identifier from dismech-owl's IRI scheme
  (`…/node/<entry>/<kind>/<slug>` for a disease-local node, the module class for
  a conserved mechanism) rather than minting a hash: those are stable across
  rebuilds, which a hashed term signature is not. Carry the grounding CURIEs in
  multivalued `xref`, the Biolink class in `category`
  (`biolink:PathologicalProcess`, `biolink:PhenotypicFeature`, …), and the rung
  in `identity_rung`.
- **One edge row per disease assertion, pointing at merged nodes.** Do not ship
  aggregated edges with a nested provenance sidecar. Parallel edges are normal
  in KGX, so emitting the ~100,000 original assertions — each with its own
  disease, its own PMIDs, its own evidence count — gives cross-disease
  connectivity from the node layer, makes `support` a `GROUP BY` that can never
  disagree with the rows, and needs no reification. `original_subject` /
  `original_object` are real Biolink slots and carry the disease-local node
  names.
- **Metadata a ranking pipeline can use**: `publications` (the union of evidence
  PMIDs, a native Biolink slot); `agent_type` driven by the identity rung —
  `manual_agent` where the grouping came from `conforms_to` or a tree
  definition, `automated_agent` where it was machine-derived;
  `primary_knowledge_source: infores:dismech` with a separate
  `aggregator_knowledge_source` for the projection itself.
- Optionally a second, derived edges file with `support` and `support_class`
  pre-aggregated, for consumers who want the consensus view.

**What such a partner gains** is the interior of a path their graphs usually
lack. Translator-family KGs are rich in drug→target, gene→disease and
disease→phenotype and thin on mechanism→mechanism; merged concept nodes are what
make `drug → mechanism → mechanism → phenotype ← disease` traverse *between*
diseases instead of dead-ending inside one.

Two places this leaves Biolink, and both should be stated to the consumer rather
than left to fail validation quietly: the disease-context column on each
assertion edge (there is no clean Translator slot for "this causal edge holds in
the context of `MONDO:X`"), and `support`. Both are extra TSV columns, which KGX
tolerates.

---

## 8. Build plan

Each phase is independently shippable; none touches `kb/` or the schema.

| Phase | What ships | Why now |
|---|---|---|
| 0 | `src/dismech/megagraph/` reading the reasoned OFN: inferred-ancestor lookup, edge lifting, `just megagraph` writing uncommitted TSV/JSON plus a manifest pinning both the dismech and dismech-owl commits | The prototype runs; dismech-owl supplies the hierarchy |
| 1 | Provenance and facets on every lifted edge: the asserting entries, `support`, `support_class`, and the substrate/scale spread of each concept's instances | Without it a bad lift is invisible — curators see their own page, unchanged |
| 2 | Fallback identity for what the TBox leaves unclassified (rung 5, and rung 4 where no defined class matches), reported separately from the reasoned concepts | ~19,000 nodes have no grounding; they must be visible, not silently absent |
| 3 | Four report-only worklists: candidate modules, missing `conforms_to`, convergence gaps, grounding gaps | The actual payoff — see below |
| 4 | The KGX profile in §7, and CX2 → NDEx for the whole graph plus one subgraph per module | What partners can consume |
| 5 | Wire `dismech-node-embed`, evaluate against held-out `conforms_to`, suggestions only | Learned matching never enters the published projection |

**Phase 3 is the one to fund.** `megagraph-missing-conformance` — nodes whose
grounding already matches a module node but which carry no `conforms_to` —
proposes an annotation curators already have the vocabulary for, and each
acceptance converts a machine-guessed grouping into a curator-asserted one,
permanently, in both this projection and dismech-owl's TBox.

**A prerequisite for phase 0**: dismech-owl's `just reason` merges only GO and
MONDO. Exact-term grouping works today, but grouping by an HP, CL or UBERON
*ancestor* needs those merged, so either the aggregation layer resolves those
ancestors itself through OAK, or dismech-owl merges more modules first. Settle
this before building, since it decides where the hierarchy comes from.

### Deliberately out of scope

- **No new schema slot.** No `mechanism_id`, no canonical-concept class. If a
  concept deserves a name, the existing remedy is to promote it to a module and
  point `conforms_to` at it — which dismech-owl then turns into a real axiom.
- **No gate.** Nothing here blocks a curation PR; `just qc` is unchanged.
- **No KB rewriting**, and no merging of two curators' nodes on this layer's own
  authority.
- **No rival OWL build.** Where this plan and dismech-owl disagree about
  identity, dismech-owl wins; this layer only counts.

---

## 9. How we find out the merge is wrong

| Detector | Meaning | Now |
|---|---|---:|
| self-loops | a concept ate both ends of an edge | 389 |
| node-type mixing | a concept spans e.g. phenotype and treatment | 0 |
| `conforms_to` disagreement | two nodes conforming to *different* module nodes get one key | to measure |
| held-out `conforms_to` recall | the deterministic key vs. the curated answer | to measure |
| lifted-edge disagreement | a lifted edge whose direction contradicts the module's own chain | to measure (new in §3) |

The middle two are the real evaluation and both are free: 4,673 nodes already
carry a human's answer to exactly the question a key is guessing at. Any rung
that disagrees with a curator more than a few percent of the time is wrong and
should be demoted, not tuned until it agrees.

---

## 10. Risks and open questions

- **Hub concepts create false paths.** `HP:0001250` (Seizure) now appears in 939
  entries; `NCIT:C15747` merges 1,596 treatment nodes. Mitigation: an IDF-style
  specificity weight per concept, as `scripts/pathograph_overlap.py` already
  computes, so ubiquitous concepts self-decay.
- **The compression figure is seductive and nearly meaningless.** 60% is mostly
  phenotype and treatment bookkeeping. Quote 9,541; watch 127.
- **Over-merging is invisible to curators**, who see their own unchanged disease
  page. Phase 1's provenance is not polish.
- **Two moving upstreams.** This layer now depends on dismech `main` *and* on a
  dismech-owl release built from a pinned dismech commit. The manifest must pin
  both, and a lifted edge count is meaningless without saying which pair it came
  from.
- **Staleness.** The corpus gains entries daily — it grew 41% between this
  plan's two measurements. Rebuild in the nightly sweep, print the artifact's
  age, never gate on it.

Open questions:

1. Should a comorbidity entry's `association_signals` contribute edges between
   two diseases' concept sets? They are the only genuinely cross-disease edges
   the KB curates, and 58 entries is a small enough pilot to try.
2. Should `INCREASED` and `DECREASED` instances of one GO term be a single
   concept with a modifier facet, or two? The tree's defined classes already
   answer this per definition (`modifier DECREASED` is part of the expression),
   which suggests two — and supersedes the prototype's answer of one.
3. Is the 44,132-node giant component a finding or an artifact of hub concepts?
   Recompute after specificity weighting and see whether it survives.
4. Should this layer live in dismech-owl rather than dismech? It consumes that
   repo's release and nothing in `kb/` depends on it. Deciding this before
   phase 0 avoids a third place to look.
