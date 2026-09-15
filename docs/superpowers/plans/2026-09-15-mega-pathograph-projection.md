---
title: Projecting Every Pathograph into One Cross-Disease Mega-Pathograph
status: PLAN
description: >-
  A design for collapsing all 3,152 dismech pathographs into a single
  cross-disease graph in which a mechanism curated once per disease becomes one
  node. Proposes a derived projection (not a KB mutation) over a five-rung
  identity ladder anchored on `conforms_to`, with the disease context preserved
  as instance provenance. Includes a measured prototype, the four merge failure
  modes it found, and the finding that edge-level convergence outside the module
  system is currently 54 edges.
tags: [PATHOGRAPH, GRAPH_PROJECTION, MODULES, CONFORMS_TO, PLAN]
---

# Projecting Every Pathograph into One Cross-Disease Mega-Pathograph

**Status: plan.** Nothing here changes `kb/` or the schema. The artifact is
derived, rebuildable, and throwaway by design.

Reproduce every number below with:

```bash
uv run python scripts/megagraph_prototype.py                    # summary JSON
uv run python scripts/megagraph_prototype.py --format tsv       # merged edges
```

Measured at `643d3e5ab` over `kb/disorders`, `kb/modules`, `kb/comorbidities`.

---

## 1. The problem, stated precisely

Every disorder entry carries its own pathograph, and a mechanism that recurs
across diseases is re-curated once per disease. Hepatic stellate cell activation
in cirrhosis and myofibroblast activation in pulmonary fibrosis are the same
mechanism wearing two organs. There are 80,639 node instances across 3,152
entries and, by the measurement in §5, roughly 33,000 distinct things being
described.

The request — one mega-pathograph where identical mechanisms are one node — is
blocked by the thing that makes each node trustworthy: **a pathograph node is not
a free-floating mechanism, it is a claim about a mechanism *in a disease*, and its
evidence, its modifier, its organ, and its position in that disease's cascade are
all part of what it asserts.** Merging two nodes discards whichever of those
differ. So the real design question is not "how do we match nodes" but "what
survives the match, and where does the rest go".

Three distinctions the projection has to keep apart, because collapsing any one
of them silently destroys content:

| Case | Example | Correct handling |
|---|---|---|
| Same mechanism, different substrate | `fibrotic_response#Mesenchymal Cell Activation` realized as hepatic stellate cell vs. pulmonary myofibroblast | **Merge.** Substrate is a qualifier of the instance, not a different mechanism. This is exactly what `conforms_to` already encodes. |
| Same name, different mechanism | *Mitochondrial Dysfunction* in 13 entries; *Immune Evasion* in 12 | **Do not merge on the name.** These are different claims that happen to share a label. |
| Same process term, different causal role | `GO:0006915` apoptosis as the driving lesion vs. as a terminal consequence | **Do not merge on the term alone.** Identity needs the cascade tier too, or the merge fuses a cause with its own effect. |

---

## 2. What already exists — build on it, do not rebuild it

Five pieces of this are already in the repo, and the plan is mostly about
connecting them.

- **`conforms_to` is the answer, already curated, for 3,014 nodes.** A disorder
  node declaring `conforms_to: "fibrotic_response#Mesenchymal Cell Activation"`
  *is* an assertion that this node and that module node are the same mechanism.
  The 174 modules in `kb/modules/` are, in the words of the overlap prototype,
  "the overlaps recurrent enough to be worth naming". The mega-pathograph does
  not need to invent a canonical-mechanism vocabulary; it needs to extend the
  one the KB has.
- **`dismech.graph.build_causal_graph`** already resolves bare-name targets
  across `pathophysiology`, `phenotypes`, `treatments`, `environmental`,
  `biochemical` and the model sections into one flat per-disease namespace, and
  reports what fails to resolve. Reuse it verbatim; a reimplementation loses
  52% of edges (measured — see §7).
- **`src/dismech/node_class_scan.py`** classifies nodes onto the nine-tier
  cascade (GENOMIC → … → OUTCOME) with 76.2% coverage and per-rule confidence.
  That tier is the missing discriminator for the third row of the table above.
- **`src/dismech/node_embeddings/`** already embeds each node as
  `name + term labels` and evaluates retrieval **against `conforms_to` as ground
  truth** — precisely the supervision signal a learned matcher needs. It is
  unwired: no recipe, no docs, no recorded numbers.
- **`scripts/pathograph_overlap.py`** does the pairwise version of this
  (IDF-weighted term overlap between two pathographs) and already produced the
  most useful output of the family: high genetic-correlation pairs with zero
  mechanistic overlap are curation gaps (T2D ↔ CAD, rg ≈ 0.35, overlap 0.000).

---

## 3. Design: project, never mutate

The mega-pathograph is a **third object**, not an edit to the first two:

```
kb/disorders/Liver_Cirrhosis.yaml          kb/modules/fibrotic_response.yaml
  pathophysiology:                           pathophysiology:
  - name: Hepatic Stellate Cell Activation   - name: Mesenchymal Cell Activation
    conforms_to: fibrotic_response#Mesen…      …
          │                                          │
          │ INSTANCE_OF (curated)                    │ IS (definitional)
          ▼                                          ▼
     ┌──────────────────────────────────────────────────────┐
     │  MechanismConcept  fibrotic_response#Mesenchymal …    │
     │  instances: 99 nodes / 97 diseases                    │
     │  substrates: CL:0000057, CL:0000632, CL:0002138, …    │
     │  in-edges / out-edges carry `support` = n diseases    │
     └──────────────────────────────────────────────────────┘
```

Three rules make this safe:

1. **The disease-local node stays primary.** It keeps its evidence, modifier,
   scale, and organ. The concept node owns no evidence of its own.
2. **Every merged node and every merged edge carries its instance list.** A
   concept is a set of `(entry, node name)` pairs; an edge is a set of entries
   that asserted it. Nothing is aggregated without staying decomposable back to
   the entries that produced it — same contract as an evidence snippet.
3. **Context that differs across instances becomes a facet of the concept, not a
   deletion.** The substrate cell types of the 99 fibrotic-response instances are
   the interesting output, not noise to be collapsed.

This is the same shape as the `Grouping` design: an explicit curated union that
lists members rather than recreating a hierarchy — except here the union is
derived and rebuildable, so it can be wrong without costing anyone a PR.

---

## 4. The identity ladder

Five rungs, in descending confidence. Each node records **which rung fired**, so
a consumer can threshold on provenance rather than trusting the merge wholesale.

| Rung | Key | Nodes | Confidence |
|---|---|---:|---|
| 1. `module_node` | the module node itself, `stem#Name` | 861 | definitional |
| 2. `conforms_to` | the module node it declares | 3,014 | **curator-asserted** |
| 3. `hp_term` | the HP CURIE of a phenotype | 34,669 | high (HP *is* the shared vocabulary) |
| 4. `core_terms` | identity-bearing CURIEs (GO/CHEBI/HGNC/NCIT/ECTO) + CL/UBERON context | 30,941 | medium |
| 5. `name_only` | normalized name, within one node type | 11,154 | low — never merges across node types |

The load-bearing rule is the split between **core** and **context** prefixes.
`CL` and `UBERON` qualify an identity; they can never establish one. An earlier
run of the prototype that let a bare CL term key a node collapsed **207
unrelated nodes onto "neuron"** and manufactured self-loops out of causally
distinct events. A cell type says where a mechanism happens, not which mechanism
it is.

Rung 5 is a deliberate floor, not an aspiration: 11,154 nodes carry no
identity-bearing grounding at all (3,818 pathophysiology nodes have no ontology
term whatsoever). They join the graph as singletons under their own name rather
than being dropped, because a node missing from the projection is invisible,
while a node that merged with nothing is a visible curation gap.

**Rung 4 needs a sixth component it does not yet have: the cascade tier.** The
node-class scan supplies it, and adding `node_class` to the key is what keeps
`GO:0006915`-as-driver apart from `GO:0006915`-as-consequence. Phase 2.

---

## 5. What the projection yields today

| | raw | merged |
|---|---:|---:|
| entries | 3,152 | — |
| nodes (all types) | 80,639 | **33,014** (59.1% compression) |
| edges | 55,558 | 50,931 |
| orphan targets | 115 | — |

- **6,766 concepts span two or more entries.** That is the cross-disease glue,
  and it is real: this is where "curated once per disease" becomes "one node".
- **One giant component of 26,237 nodes.** The corpus is already a single
  connected object; it simply has not been drawn as one.
- **0 concepts mix node types.** The type guard holds.
- **247 self-loops.** These are the over-merge detector, not a nuisance: each one
  is a concept that ate both ends of a causal edge.

---

## 6. The uncomfortable result, and what it means for the deliverable

Node convergence is large. **Edge convergence is not.** Of 50,931 merged edges,
1,771 carry two or more entries, and they break down as:

| | edges with support ≥ 2 |
|---|---:|
| touching a module node (curator-asserted by `conforms_to`) | 1,088 |
| touching a treatment node | 337 |
| **pathophysiology → pathophysiology, no module involved** | **54** |
| self-loops (over-merge artifacts) | 12 |

At support ≥ 3 the last class is **7 edges**, one of which is
`GO:0006954 → GO:0006954`.

Two readings, and both matter:

- **The module-mediated edges are partly tautological.** Diseases conforming to
  the same module reproduce that module's chain because conformance asks them
  to. Reporting 1,088 as "discovered convergence" would be counting the
  curators' own instruction back to them. Count them separately, always.
- **Independent convergence is genuinely rare right now.** Not because diseases
  do not share mechanism — the overlap prototype shows they do — but because two
  curators describing the same cascade pick different node boundaries, different
  GO terms at different depths, and different names. The merge exposes that;
  it cannot fix it.

So the honest framing of the deliverable: **the mega-pathograph is a curation
instrument first and a consensus map second.** Its highest-value outputs are the
places where convergence *should* exist and does not —

- concepts with many instances and no module (candidate modules to promote);
- nodes whose key matches a module node exactly but which carry no
  `conforms_to` (missing conformance annotations, one-line PRs);
- disease pairs with high genetic correlation and zero shared concepts (the
  T2D ↔ CAD finding, now computable corpus-wide instead of pairwise);
- the 3,818 ungrounded pathophysiology nodes, ranked by how many neighbours they
  would join if they were grounded.

Marketing it as "the consensus causal map of human disease" would be a claim the
data does not currently support, and the graph itself is the thing that says so.

---

## 7. Why edges must come from `build_causal_graph`

A first prototype indexed only `pathophysiology` nodes and resolved `downstream`
targets against that index. **19,300 of 37,212 targets (52%) failed to resolve** —
not because the KB is broken, but because `downstream` legitimately targets
phenotypes, treatments and biochemical nodes by bare name, in one flat namespace
(CLAUDE.md, *Pathograph Targets Are Bare Names*). Rebuilding that resolution is
re-deriving a solved, gated problem; the real orphan count through
`build_causal_graph` is **115 corpus-wide**.

The same applies downstream: the projection should emit through the existing
exporters (`kgx_export`, `cx2_export`, `ndex_publish`) rather than inventing a
serialization.

---

## 8. Implementation plan

Each phase is independently shippable and leaves the KB untouched.

### Phase 0 — `dismech.megagraph`, derived artifact (small)

Promote `scripts/megagraph_prototype.py` into `src/dismech/megagraph/` with the
identity ladder in `identity.py` (pure function: node → `(key, rung)`) and the
projection in `project.py`. Route the corpus walk through `kb_cache`; it walks
once, so call `kb_cache.default_off()` in `main()`.

```bash
just megagraph                     # summary
just megagraph --format tsv        # merged edges with support
just megagraph --min-support 2     # the backbone
```

Outputs, none committed: `exports/megagraph/{nodes,edges}.tsv` plus a
`manifest.json` pinning the commit and the rung counts.

### Phase 1 — provenance and facets

Every concept gains `instances` (entry + node name + rung), `substrates` (the
distinct CL/UBERON across instances), `scales` (the distinct
`biological_scale`), and `modifiers`. Every edge gains `support`, the entry
list, and the predicate set. This is what makes the artifact auditable rather
than impressive.

### Phase 2 — cascade tier in the key

Fold `node_class_scan`'s tier into rung 4, and re-measure. Expected effects, all
falsifiable: self-loops fall, the 54-edge class changes size, `CONFLICT`-classed
nodes (nodes whose own GO terms span two tiers) refuse to key and are reported
as debundle candidates. If self-loops do not fall, the tier is not doing the job
claimed for it and the rung should stay as it is.

### Phase 3 — the curation instrument

The four worklists from §6, as recipes, report-only, exit 0:

```bash
just megagraph-module-candidates   # big concepts with no module
just megagraph-missing-conformance # key matches a module node, no conforms_to
just megagraph-convergence-gaps    # high-rg / zero-shared-concept disease pairs
just megagraph-grounding-gaps      # ungrounded nodes ranked by joinable neighbours
```

`megagraph-missing-conformance` is the highest-yield and lowest-risk: it proposes
an annotation a curator already has the vocabulary for, and each acceptance moves
a node from rung 4 to rung 2 permanently.

### Phase 4 — publish

CX2 → NDEx for the whole graph and per-module subgraphs; a browsable HTML index
under `pages/` built by the existing page-build workflow (derived, so never
committed from a hand-authored PR). Default view thresholded at support ≥ 2 with
module-mediated edges visually distinguished from independent ones.

### Phase 5 — learned matching, suggestion-only

Wire `dismech-node-embed`, evaluate against held-out `conforms_to` (precision@k
is already implemented), and record the numbers in the docs where there are
currently none. Embedding proposals **never** enter the published projection;
they enter a worklist. This is the same line `dismech-terms` draws for ontology
suggestions and `list-background-citations` draws for `quote_role`: a lead is not
an annotation.

### Deliberately not in scope

- **No new schema slot.** No `mechanism_id`, no canonical-concept class. The
  projection is derived; if a concept deserves to be named, the existing remedy
  is to promote it to a module and let `conforms_to` point at it. Revisit only
  if Phase 3 shows curators wanting to assert an identity that modules cannot
  express.
- **No gate.** Nothing about this blocks a curation PR. `just qc` stays as it is.
- **No KB rewriting.** The projection never edits a disorder file, and in
  particular never merges two curators' nodes on its own authority.

---

## 9. How we know the merge is wrong

Four detectors, all cheap, all already computable:

| Detector | Meaning | Current value |
|---|---|---:|
| self-loops | a concept ate both ends of a causal edge | 247 |
| node-type mixing | a concept spans e.g. phenotype and treatment | 0 |
| `conforms_to` disagreement | two nodes conforming to *different* module nodes get the same key | to measure |
| held-out `conforms_to` recall | the deterministic key's agreement with the curated answer | to measure |

The third and fourth are the real evaluation, and both are free: 3,014 nodes
carry a human's answer to exactly the question the key is guessing at. Any rung
that disagrees with a curator's `conforms_to` more than a few percent of the
time is wrong and should be demoted, not tuned until it agrees.

---

## 10. Risks

- **Hub nodes create false paths.** `NCIT:C15747` (Supportive Care) merges 1,251
  treatment nodes into one; `HP:0001250` (Seizure) has degree 405. Any path
  through these is an artifact of shared vocabulary, not shared biology.
  Mitigation: treatment identity must key on `therapeutic_agent` / `regimen_term`,
  never the generic action term; and the published graph should carry an IDF-style
  specificity weight per concept, as `pathograph_overlap.py` already does, so
  ubiquitous concepts self-decay.
- **The compression figure is seductive and nearly meaningless.** 59% is
  dominated by phenotype and treatment merging, which is bookkeeping. The number
  worth quoting is 6,766 multi-entry concepts, and the number worth watching is
  54.
- **Over-merging is invisible to curators.** A curator sees their own disease
  page, which is unchanged. Nobody will notice a bad merge unless the artifact is
  reviewed, so Phase 1's provenance is not optional polish.
- **Staleness.** The projection is derived from a corpus that gains entries
  daily. Rebuild it in the nightly sweep, print its age, and never gate on it.

---

## 11. Open questions

1. Should a comorbidity entry's `association_signals` contribute edges between
   two diseases' concept sets? They are the only genuinely *cross-disease* edges
   the KB curates today, and 26 entries is a small enough pilot to try.
2. Does the merge want directionality-aware keys — should `INCREASED` and
   `DECREASED` instances of the same GO term be one concept with a modifier
   facet, or two concepts? Current prototype says one; the `GAIN_OF_FUNCTION`
   vs `INCREASED` distinction in CLAUDE.md suggests it may need to be two.
3. Is the giant component a finding or an artifact of hub nodes? Recompute after
   the specificity weighting in §10 and see whether it survives.
