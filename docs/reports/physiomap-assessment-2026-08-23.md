# PhysioMap: assessment and relevance to dismech (2026-08-23)

**Subject.** Hoehndorf R, Schofield PN, Gkoutos GV. *PhysioMap: an ontology-grounded causal
knowledge graph of human physiology.* bioRxiv preprint, posted 2026-08-07.
[doi:10.64898/2026.08.03.742471](https://doi.org/10.64898/2026.08.03.742471) ·
[code + OWL release](https://github.com/bio-ontology-research-group/physiomap/) ·
[interactive demo](https://bio2vec.net/physiomap/). Code BSD-3-Clause; map, benchmark
data, and docs CC BY 4.0. To appear in a PSB-style proceedings volume (© 2027).

**Scope of this document.** What PhysioMap is, how it differs structurally from the dismech
pathograph, and which of its ideas are worth importing. This is an analysis of an external
resource, not a curation change. No KB entry, schema file, or cache is modified by it.

**Bottom line.** PhysioMap and dismech are close to *structural duals*, and the difference
is not subject matter — it is what an edge means and what a node names. dismech has ~10×
PhysioMap's edge count but cannot run PhysioMap's central inference, because dismech causal
edges carry **directness without polarity** and dismech nodes are **file-scoped strings
rather than a shared variable namespace**. Those are two separable gaps, and the first is
much cheaper to close than the second.

---

## 1. What PhysioMap is

An OWL 2 EL knowledge base of *contextualized physiological traits*, plus a versioned
projection into a typed causal knowledge graph (CKG), plus a solver that answers
qualitative intervention queries over that graph.

**Trait semantics.** A trait is the entity–quality (EQ) pattern used by HPO/MP: a PATO
quality borne by an entity or process in a recorded context —
`Trait ⊓ ∃hasPart.(E ⊓ ∃κ.C ⊓ ∃hasQuality.Qᴱ)`, with `κ` being `contextPartOf` for
continuants and `occursIn` for processes. Entity classes come from ChEBI, PR, CL, Uberon,
GO; qualities from PATO.

**Five relation types, each with a distinct structural-causal-model (SCM) reading** — this is
the paper's core claim, that typing the relation determines what an intervention replaces:

| Relation | What an intervention replaces | Enters causal Jacobian? |
|---|---|---|
| Causal influence | a causal mechanism | yes |
| Production | a source/production term | yes |
| Quantitative identity | a defining equation (e.g. MAP = CO × TPR) | yes |
| Constitution | a part→whole determination | **no** — separate acyclic graph `Gκ` |
| Modulation | a mixed partial (node, edge) pair | **no** — retained but unread by the first-order solver |

Causal claims are asserted type-level via the *collection pattern*
(`T_tᵃˡˡ ⊑ ∃hasMember.(∃causedBy.T_s)`) rather than `T_t ⊑ ∃causedBy.T_s`, precisely to avoid
claiming every instance of the target is so caused — and to stay in OWL 2 EL. Worth noting
for anyone tempted by an "obvious" OWL encoding of causation: the naive subclass axiom is
the *wrong claim*, not merely an expensive one.

**Inference.** Signs are an explicitly *derived abstraction* of the quantitative
constraints, not the model itself. The solver takes the first-order derivative-sign
abstraction, cuts incoming edges at the intervention target, decomposes into strongly
connected components, and processes the condensation in topological order — using sign
algebra over `{+, -, 0, ?}` on singletons and, inside feedback components, the
Cramer's-rule determinant test `sign(dx*ᵢ/dθ) = sign(det J⁽ⁱ⁾_S / det J_S)`. Exact expansion
is capped at 16 traits per component (an engineering bound fixed before evaluation); larger
components get a conservative fixed-point algorithm. **Both abstain — return `?` — when the
sign is not determined.** That abstention is the paper's most transferable design decision.

### 1.1 Reported scale and results

v1.1.1 holds **1,699 traits** and 2,270 causal-influence, 85 production, 4 constitution,
9 quantitative-identity, and 19 modulation axioms; the projection yields 1,699 nodes and
**2,387 relation instances**. Largest strongly connected component: 213 traits.

- **Expert review** (P.N.S., stratified fixed-seed sample of 83 relations across all five
  types): 69 accepted, 12 flagged for further investigation, 2 rejected (both causal). The
  authors state that unequal sampling rates preclude a map-wide accuracy estimate.
- **Forward prediction** vs. an HPOA-derived reference (release 2026-02-16): before
  exclusions, 175 determinate predictions, 171 agreeing (97.7%). Discrepancy review found
  3 of the 4 disagreements conflicted with the cited primary literature and 1 varied across
  studies; all 4 were dropped *uniformly for every method*, leaving 866 adjudicated pairs.
  On that set the solver returned 171 determinate directions, **171 correct, 0 wrong —
  100% precision at 19.7% coverage**, abstaining on 695. Excluding the 15 genes with the
  most curation overlap left 151 determinate directions, all concordant.
- **Baselines.** Shortest signed path: 375 directions, 292 correct, 83 wrong (77.9%).
  Signed diffusion (α = 0.85) retained errors at matched prediction counts.
- **The abstention result.** On the 171 pairs where the solver committed, the path rule
  returned the *same* direction — 0% error. On 204 further pairs where the solver abstained,
  the path rule got 121 right (59.3%), a 40.7% error rate. An exact within-gene conditional
  permutation test rejected independence (P = 2.05 × 10⁻⁷). So abstentions *concentrated
  the hard cases* rather than being scattered.
- **Abduction** (163 genes, closed pool of 175 single-lesion hypotheses): solver unique
  top-1 40, best-tied top-3 127, top-10 161, MRR 0.707; shortest path 30/94/105/0.535;
  diffusion 30/99/110/0.558; chance 1/3/9/0.033. The true lesion was uniquely first for only
  40/163 — the profiles narrow the pool far better than they pin it down.

### 1.2 Honest reading of the limits

The authors are unusually forthright, and the caveats should not be softened in
retelling:

- **100% precision is at 19.7% coverage, on an adjudicated reference.** Four reference
  directions were removed post hoc after review against primary literature. The exclusion
  was applied uniformly to all methods and reported as post hoc, which is the right
  procedure — but the headline number is not "PhysioMap is never wrong."
- **The reference is not independent.** PhysioMap curation and HPOA may draw on the same
  literature. The 15-gene overlap-exclusion analysis mitigates but does not remove this.
- **Abduction used a closed pool always containing the true lesion**, and top-*k*/MRR use
  the best position within a tie — optimistic for every rule compared.
- **Relation typing barely mattered on these two tasks.** Adding production, quantitative
  identity, and constitution to causal influence changed 4 of 866 forward calls (no sign
  flip) and 12 of 163 inverse ranks, with no aggregate improvement. The richer typing is
  justified by semantics and by what it *will* enable, not by measured benchmark gain here.
- The paper says plainly: proof of concept, **not clinical readiness**.

---

## 2. Structural comparison with dismech

Counts below are measured from this repo at commit `4b2f90c` (2,071 KB files: 1,928
disorders, 123 modules, 20 comorbidities).

| | PhysioMap v1.1.1 | dismech (2026-08-23) |
|---|---|---|
| Organizing axis | one shared physiology, disease-agnostic | per-disease entries + reusable modules |
| Nodes | 1,699 traits | **11,923** pathophysiology nodes |
| Causal edges | 2,387 projected relations | **22,564** `downstream` edges |
| Node identity | global EQ-pattern OWL class | free-text `name`, **scoped to its file** |
| Edge polarity | signed (`+`/`-`/`0`/`?`), semantically load-bearing | **absent** |
| Edge typing | 5 SCM-distinct types | `causal_link_type` = *directness* only |
| Feedback | first-class; SCC + Cramer's rule; largest SCC 213 | not represented as feedback |
| Inference | intervention prediction + abduction, abstains | rendering, compliance, export; no sign propagation |
| Evidence model | 6 classes, admission-gating, **not** used by solver | per-edge `EvidenceItem`, snippet-verified against cached sources |
| Cross-scale composition | `constitution` in a separate acyclic graph | `conforms_to` module anchors (manual, per-node) |

Two asymmetries deserve attention.

### 2.1 dismech signs *treatment* and *environmental* edges but not mechanism→mechanism edges

This is the concrete finding of this review. dismech already commits to edge polarity in two
places:

- `TreatmentMechanismTarget.treatment_effect` → `INHIBITS`, `ACTIVATES`, `MODULATES`,
  `BYPASSES`, `RESTORES`
- `EnvironmentalMechanismTarget.environmental_effect` → `TRIGGERS`, `EXACERBATES`,
  `PREDISPOSES`, `PROTECTS_AGAINST`, `MODULATES`

But `CausalEdge` — the 22,564-edge backbone — carries only
`target`, `description`, `evidence`, `hypothesis_groups`, `causal_link_type`,
`intermediate_mechanisms`. There is no slot for whether A *raises* or *lowers* B.

So a drug edge into a node is signed, an exposure edge into the same node is signed, and
the mechanism edge out of it is not. Any signed traversal of a dismech pathograph dies at
the first `downstream` hop.

Polarity is not absent from the KB, it is just not in a queryable slot. Node-level
descriptors carry `modifier` heavily — **DECREASED 3,520, INCREASED 3,394, ABNORMAL 2,355,
DYSREGULATED 715** (plus ABSENT 23, GAIN_OF_FUNCTION 5, LOSS_OF_FUNCTION 4) — and
`INCREASED`/`DECREASED` are already bound to `PATO:0002300`/`PATO:0002301`, *the exact two
terms PhysioMap uses for its `+`/`-`*. A crude regex over edge `description` text
(inhibit|suppress|decreas|reduc|block|impair|loss of|deplet|antagoni) matches 4,124 of
22,564 edges (18.3%). Treat that only as evidence that polarity language is pervasive in
the prose — the regex cannot distinguish "A inhibits B" from "A causes impaired B", and the
two imply *opposite* edge signs. It is a reason to look, not a measurement.

Note the modifier counts describe *node states*, not edge signs, and the two are not
interchangeable: a node marked `DECREASED` tells you nothing about whether its outgoing edge
raises or lowers its target. This is why the information cannot simply be derived.

### 2.2 The deeper gap is the namespace, not the sign

`CausalEdge.target` is `range: string`, resolved by convention within the same file.
"Hepatic Stellate Cell Activation" in `Liver_Cirrhosis.yaml` and the corresponding node in
`fibrotic_response.yaml` are related only through a hand-authored `conforms_to` anchor, and
CLAUDE.md is explicit that conformance is *not* inheritance — disorder entries fully
duplicate module content.

PhysioMap's traits, by contrast, are globally identified classes in one namespace, which is
what lets 1,699 nodes form a single coupled system with a 213-trait feedback component.

Consequence: **dismech's 22,564 edges do not compose into one graph.** They are ~2,000
disjoint per-disease graphs joined by manual anchors. Signing the edges would make each
*entry* traversable; it would not by itself produce a whole-body physiology. That is a much
larger undertaking and should not be smuggled in as a side effect of adding a sign slot.

### 2.3 dismech pathographs are almost entirely acyclic — which makes signing them *easier*

PhysioMap's solver is as elaborate as it is because feedback is unavoidable in whole-body
physiology: its largest strongly connected component holds 213 traits, which is what forces
the Cramer's-rule determinant test and the 16-trait expansion cap. It is worth asking
whether dismech would inherit that complexity. Measured over the 2,045 KB files that have a
`pathophysiology` block, resolving `downstream` targets within each file:

| | Count | Share |
|---|---:|---:|
| Files with a genuine multi-node feedback cycle | **29** | 1.4% |
| Self-loop edges (a node listing itself as `downstream`) | **2** | — |
| Files whose pathograph is acyclic | 2,014 | 98.6% |

The 29 cyclic files are exactly where you would expect real feedback to be curated —
`Alzheimer_Disease`, `Chronic_Kidney_Disease`, `Idiopathic_Pulmonary_Fibrosis`,
`Abdominal_Aortic_Aneurysm`, `Aortic_Valve_Stenosis`, `Epilepsy`, `Alopecia_Areata` — i.e.
self-amplifying vicious circles, not modeling accidents.

This substantially strengthens R1. For 98.6% of entries, signed propagation is plain
topological sign algebra over `{+, -, 0, ?}` — no Jacobian, no SCC decomposition, no
determinant test. PhysioMap's hard machinery would be needed only for a couple of dozen
entries, and its conservative fallback (abstain when unresolved) is a perfectly acceptable
answer for those in a first implementation.

The two self-loops are almost certainly curation errors rather than modeling claims and are
worth fixing independently of anything else here:

- `Periventricular_Nodular_Heterotopia.yaml` — "Progressive Lung Disease" → itself
- `Autoimmune_Polyendocrine_Syndrome_Type_1.yaml` — "Chronic Mucocutaneous Candidiasis" → itself

Nothing currently rejects a node that lists itself as its own `downstream` target; a
one-line assertion in `tests/test_data.py` would close that. Flagged here as an observation
from this analysis, not fixed in it.

---

## 3. Recommendations

Ordered by value-to-cost. Only the first is proposed as near-term work.

### R1 — Add an optional polarity slot to `CausalEdge` (recommended)

The smallest change that unlocks the most. Sketch, deliberately mirroring the existing
effect enums rather than inventing a new vocabulary:

```yaml
CausalEdge:
  slots:
    - target
    - causal_effect        # NEW: INCREASES | DECREASES | MODULATES | UNKNOWN
    - causal_link_type     # unchanged: directness
    ...
```

Design notes drawn from the paper:

- **Keep it optional and default to absent, not to `UNKNOWN`.** PhysioMap's `?` means
  "non-constant dependence with no sign constraint" — a *positive claim* that a dependence
  exists but its sign is undetermined. That is not the same as "nobody has curated this
  yet." Conflating them is how a coverage gap turns into a false knowledge claim.
- **Do not derive it from the target node's `modifier`.** As above, node state and edge sign
  are different quantities.
- **Sign is a separate claim, so it takes separate evidence** — the same discipline dismech
  already applies to phenotype `frequency:` and to model-link vs. readout evidence.
- Retrofitting 22,564 edges is not proposed. Curate forward and backfill opportunistically;
  a mechanically-inferred backfill from description text would be exactly the kind of
  plausible-looking fabrication the repo's evidence SOP exists to prevent.

Before implementing, someone should confirm no existing issue covers this. My GitHub
semantic search for it returned zero results on two phrasings, which I read as
*inconclusive* (the queries also failed to surface anything adjacent) rather than as
confirmation that none exists.

### R2 — Adopt principled abstention wherever dismech infers a direction

The most valuable *result* in the paper is not the 100% precision, it is that abstentions
were provably concentrated on cases a naive path rule got wrong 40.7% of the time. Any
future dismech feature that propagates direction along the pathograph — a signed-traversal
query, a treatment-response predictor, a compliance heuristic — should be able to return
"undetermined" and should be evaluated on precision *and* coverage, never precision alone.

### R3 — Reuse the HPO-EQ directional reference construction (methodology, no schema change)

PhysioMap builds its evaluation reference by decomposing directional HPO classes into
(variable, direction) via the EQ pattern and PATO:0002300/0002301, propagating annotations
*only upward* through the subclass hierarchy, and retaining a gene–variable direction only
when the resulting set is a singleton. dismech already binds those two PATO terms and
already relates model variables to HP terms with `threshold_direction`. If dismech ever
wants to validate a signed pathograph against HPOA, this recipe is directly reusable —
including its two guardrails (upward-only propagation; drop non-singletons). Note they had
to hand-block two deoxycortisol terms whose asserted HPO ancestry would have mis-mapped
them to cortisol, which is a warning that the recipe needs spot-checking, not blind trust.

### R4 — Watch, do not adopt: constitution, quantitative identity, modulation

These are semantically well-motivated but, on the paper's own evidence, changed almost
nothing on the two evaluated tasks (§1.2). dismech has no solver that would read them.
Adding four more relation types to `CausalEdge` now would add curation burden with no
consumer. Revisit if and when R1 lands and a signed-traversal consumer exists.

The exception worth flagging: **quantitative identity** (MAP = CO × TPR) is the one type
with an obvious dismech analogue already in the tree — `ComputationalModel` /
`ModelVariable` / `ModelVariableDescriptor`, where variables carry units, LOINC/CHEBI
mappings, and thresholds. If dismech ever links a pathograph node to a model variable, that
link is closer to PhysioMap's quantitative identity than to a causal edge, and should not be
recorded as one.

### R5 — Not recommended: mirroring PhysioMap content into dismech

PhysioMap is CC BY 4.0 and technically ingestible, but its content is *normal* physiology,
disease-agnostic. dismech entries are disease-scoped pathographs with per-edge, snippet-
verified evidence against cached references. There is no clean way to import a PhysioMap
trait into a dismech disorder file without either inventing disease-specific evidence for a
disease-agnostic claim, or creating nodes that no entry owns. If a bridge is ever wanted,
the right shape is a **mapping** (dismech node ↔ PhysioMap trait IRI), not a copy — and that
presupposes R1 and the §2.2 namespace work.

---

## 4. Open questions

1. Is edge polarity already tracked in an issue? (search inconclusive — needs a human check)
2. Would `causal_effect` be better on `CausalEdge`, or as a fourth mechanism-link class
   alongside `TreatmentMechanismTarget` / `EnvironmentalMechanismTarget` /
   `ModelMechanismLink`? The existing three all sign their edges; `CausalEdge` is the odd
   one out, which weakly argues for putting it on `CausalEdge` itself.
3. ~~Does the dismech pathograph have feedback cycles today?~~ **Answered in §2.3:** 29 of
   2,045 files (1.4%), plus 2 self-loops that look like curation errors. Sign propagation
   would be plain topological sign algebra for 98.6% of entries.
4. Should a self-loop `downstream` edge be a test failure? (§2.3 — two exist today.)
5. `conforms_to` anchors are the only existing cross-file node identity. Are they dense
   enough to seed a shared trait namespace, or is §2.2 genuinely a from-scratch effort?

---

## 5. Provenance

Source PDF supplied by the user (bioRxiv full text, 16 pp.); text extracted locally with
pypdf and read in full. Repository counts computed at commit `4b2f90c` by walking
`kb/{disorders,modules,comorbidities}/*.yaml`; the §2.3 cycle analysis resolves each
`downstream` target against `pathophysiology[].name` within the same file (cross-file and
unresolved targets are ignored, so it measures intra-entry structure only). Schema claims
verified against
`src/dismech/schema/dismech.yaml` (`CausalEdge`, `TreatmentEffectEnum`,
`EnvironmentalEffectEnum`, `CausalLinkTypeEnum`, `ModifierEnum`, `ModelVariableDescriptor`).
No supplementary material was retrieved; statements attributed to Suppl. sections are as
described in the main text. Numbers quoted from the paper are as printed in the preprint and
were not independently recomputed.
