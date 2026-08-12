# AOP / EMOD ↔ dismech: working notes toward Comment B on issue #8309

**Status:** working notes, not a finished position. Local branch `notes-8309-aop-emod`,
deliberately not pushed.
**Date:** 2026-08-12
**Purpose:** consolidate the AOP-side material gathered so far, so question 5 of
[#8309](https://github.com/monarch-initiative/dismech/issues/8309) can be drafted without
re-deriving it. Open questions are collected in one place at the end rather than scattered.

**Framing (per @gingin77):** the issue asks **to what extent** dismech's
environmental-exposure modeling aligns with the AOP framework — a graded description, not
an adopt/reject decision.

---

## 1. Provenance of everything below

Marking this explicitly, because the mix of sources is the main risk of getting it wrong.

| Source | What it is | How used |
|---|---|---|
| **@gingin77, in conversation** | Direct statements from an EMOD author | Treated as authoritative on EMOD's intent and status |
| **[Zenodo 21710805](https://zenodo.org/records/21710805)** slide 8 | "AOP-Wiki EMOD Tools", SCAHT webinar, Hench, 2026-07-07, CC-BY-4.0 | EMOD class inventory and topology |
| **[figshare 26390980](https://doi.org/10.6084/m9.figshare.26390980)** | BOSC 2024 poster, Hench / Edwards / Lynn / Villeneuve, CC-BY-4.0 | EC entity definitions, ontology bindings, data-object definitions |
| **dismech schema** (`src/dismech/schema/dismech.yaml`) | Verified by direct grep, not from prose docs | dismech-side claims |
| **`docs/explanation/design-decisions.md`**, `evidence-model.md` | The decision register | dismech's recorded positions |

Two caveats on the reading:

- Both PDFs were read via **text-layer extraction only** (poppler is not installed, so
  slides could not be rendered). Anything carried in an image — field lists, cardinality,
  a legend — was not seen.
- `PMID:26354708` is **excluded** per @gingin77's instruction on the issue; it originated
  as a Claude suggestion during preliminary exploration and has been struck through in the
  issue body and in the bot's research comment.

---

## 2. What I still need from AOP-Wiki, and why

Two pages, **evidence sections only**:

- `aopwiki.org/aops/17#evidence`
- `aopwiki.org/relationships/1765#evidence`

These cover the **classic, published handbook rubric** — the authored-grade half of the
comparison. Stable and citable, unlike EMOD.

| What to extract | What it decides |
|---|---|
| The value vocabulary (High/Moderate/Low? Strong/Weak?) | Whether this is an authored ordinal grade — the axis that bounds how far alignment can go |
| Which dimensions are actually scored per KER | The issue assumes biological plausibility / empirical support / essentiality; if the live page differs, the comparison table is wrong |
| **Where essentiality is assessed** — KER, KE, or AOP level | Whether it maps to a dismech *edge* or *node*. Highest-value single fact: essentiality is the dimension closest to the proposed `inference.role` |
| Whether scores carry rationale text, and whether that text cites references | How near AOP's grading sits to dismech's citation-anchored `evidence` |
| Whether inconsistencies / contradicting evidence are recorded | dismech has `supports: REFUTE` and §6a retain-and-mark; a parallel would be an easily-missed alignment |
| Whether quantitative understanding is a separate scored section | Confirms the qAOP boundary the issue puts out of scope is a real seam in the data model |

---

## 3. EMOD structure (Zenodo slide 8)

"EMOD = Evidence Model" (slide 2). On top of the existing AOP backbone
(`MIE → KE-1 → KE-2 → AO`, joined by KERs, with `Prototypical Stressors` attached), EMOD adds:

- **Observation** — one per event (`MIE Observation`, `KE-1/KE-2 Observation`, `AO Observation`)
- **Assay/NAM** — Observations are *measured by* it
- **Test Guideline** — attached to Assay
- **Regulatory Endpoint** — *relevant to* / *supported by*, on the AO side
- **Evidence for Causality between KEs** — attached to the **KER**

Slides 9–12 build the same diagram incrementally; 14 is Biological Targets; 15 is KER/AOP.

### Data-object definitions (BOSC 2024 poster, verbatim)

> **Reference:** Provides a minimal set of fields for holding citations for research publications.
>
> **Evidence:** Structures evidence for KERs and includes nested upstream and downstream
> Observation data objects that each link to the KER's respective upstream and downstream KEs.
>
> **Observation:** Holds instances of KE measurements that are obtained empirically.
> Observations always include an Experimental Effect property that indicates a direction of…
> *(text truncated in extraction)*

---

## 4. The Observation class

**Per @gingin77:** a KE can have **multiple** supporting Observations. At minimum an
Observation includes:

1. a **stressor** — a thing that triggers a change to the biology of the system
2. a **biological entity** that maps to the KE
3. a **direction of perturbation** that aligns with the KE

The poster shows a fuller set of Observation-associated properties (from M2AOP v1):
`Stressor`, `Sample`, `Assay`, `Experimental Effect`, `Study Design`, and
`Upstream (or Downstream) Observation`.

### Mapping to dismech

| EMOD Observation | dismech |
|---|---|
| stressor | `Experiment.perturbations` ("gene/chemical/exposure manipulations"); or `environmental[].exposure_term` (ECTO); or a model's `genotype` |
| biological entity mapping to the KE | `ExperimentalReadout.target`, grounded via `phenotype_term` / `biomarker_term` / `biological_processes` / `assays` |
| direction of perturbation | `ExperimentalReadout.direction`, or descriptor `modifier` — see §6 |

**Multiplicity matches.** dismech allows many readouts per link and many models/experiments
per node, so "multiple Observations per KE" needs no new construct.

**The seam:** no dismech object *requires* the three together. `Experiment` comes closest
(`perturbations` + `model_systems` + `readouts` in one place) but lives in
`Discussion.proposed_experiments`, so it is for experiments *proposed to close a knowledge
gap*, not the general record of a made observation. In `ModelMechanismLink.readouts` the
stressor is only implicit in the parent model's identity, and `direction` is explicitly
optional ("omit when the measurement was simply not made"). The triple is **assemblable but
never enforced**, where EMOD makes it the minimum bar for the class.

---

## 5. Event Component (EC) entities — poster definitions

**Core EC entities** (verbatim):

> **Object:** The biological subject of a perturbation in an EC.
> **Process:** The dynamics of the underlying biological system.
> **Action:** The perturbation of the normal biology, usually the direction of the
> perturbation (increased or decreased).
> **Phenotype:** *(listed as a proposed new EC entity)*

**Non-core EC entities** (verbatim):

> **Causal Agent:** Factors applied in experimental contexts that trigger an event,
> expanding beyond chemical stressors to include genetic mutations and biological entities.

---

## 6. The strongest concrete alignment: PATO

The poster gives EC ontology bindings; dismech's were verified by grep against the schema.

| AOP EC | Bound to | dismech | Bound to |
|---|---|---|---|
| `Object` | PRO, FMA, CHEBI, UBERON, GO, CL | descriptor `term` | CHEBI, UBERON, GO, CL (no PRO/FMA — §4 constrained set) |
| `Process` | GO, HP, MP, VT | `biological_processes`, `phenotype_term` | GO, HP (no MP/VT) |
| `Action` | **PATO** | `modifier` | **PATO** |

`ModifierEnum` in `dismech.yaml` (verified, lines 651–659):

```yaml
INCREASED:
  meaning: PATO:0002300
DECREASED:
  meaning: PATO:0002301
```

Same axis, same ontology, same two terms. This is a shared grounding rather than an
analogy, and it is checkable rather than argued — probably the single most defensible
alignment claim available for Comment B.

**It also resolves the direction-polarity question.** dismech carries *both* directions, in
different slots:

- descriptor `modifier` — the **biology's** direction (matches EC `Action`)
- `ExperimentalReadout.direction` — the **measured quantity's** direction

AOP's Observation folds these into one `Experimental Effect`. Worked example of the two
coming apart: dismech's canine ALS model records myelin content `DECREASED` as support for
a node called *Motor Neuron Degeneration*, which is itself increasing.

### Biological organization ladder

Poster: **Molecular / Cellular / Organ-System / Individual / Population** — five levels.
dismech `BiologicalScaleEnum`: `MOLECULAR` / `CELLULAR` / `TISSUE` / `ORGANISM` — four.
**No population level in dismech**, exactly as the issue body predicted.

---

## 7. Status of the EMOD Evidence class

**Per @gingin77:** the Evidence class is expected to involve Observations associated with
the upstream and downstream events on the KER, but **the precise properties are not
finalized — EMOD is still under development.**

Two consequences for Comment B:

1. **Do not attempt a field-level comparison.** There are no final fields. Asserting one
   would be exactly the confident-but-wrong claim this whole grounding exercise was about.
2. **The "authored vs derived" contrast needs splitting.** If KER evidence is *composed
   from* the Observations at each end, EMOD's evidence is **derived from typed measurement
   records**, not an authored expert grade. That contrast therefore holds only against the
   *classic handbook rubric* — and EMOD appears to be moving toward the same
   derived-from-structure position dismech committed to in §12. Comment B must treat
   "AOP's evidence model" as two reference points, not one:
   - the **published handbook rubric** — stable, authored
   - **EMOD** — in development, compositional

So the extent of alignment is not a fixed quantity: one side is mid-revision, and revising
*toward* dismech's direction.

---

## 8. Possible dismech → EMOD contribution

**Per @gingin77:** there is room for the AOP Evidence class to be influenced by dismech
schema patterns.

Split by what dismech can actually stand behind.

**Proven in practice (~2000 entries):**

| Pattern | Why it transfers |
|---|---|
| **Exact-snippet validation** (§6) | Evidence must quote the source verbatim, machine-checked; paraphrase fails validation. EMOD's stated purpose is agentic-AI support, and fabrication is the failure mode this exists to catch |
| **`supports` polarity incl. `REFUTE`** | Contradicting evidence is first-class; §6a keeps overturned models recorded with a verdict rather than deleted. An evidence class that can only express support cannot represent a contested KER |
| **Two evidence layers on a model link** | "This model is informative for this node" and "this measurement was made, in this direction" are separate claims with separate evidence — which maps onto EMOD's Observation vs Evidence-for-Causality split |
| **`causal_link_type`** | `DIRECT` / `INDIRECT_KNOWN_INTERMEDIATES` / `INDIRECT_UNKNOWN_INTERMEDIATES` — a KER between adjacent KEs still varies in directness |
| **`hypothesis_groups`** | Competing mechanistic models coexisting on one graph, edges opting into a named model, rather than forcing a single consensus chain. AOP networks have the same problem |

**Not proven — a proposal, and must be offered as one:** the §12 `experiment.design` /
`inference.role` block and the derived-not-authored argument behind it. One worked example
(FH), no schema change, no KB behind it. The *argument* is worth raising before a spec
freezes — "a freely-authored certainty grade reopens the fabrication surface the grounding
layer closed" — but presenting an unbuilt proposal as prior art would repeat the
"confirmed pathophysiology chain" error that started this thread.

**Handling:** this is outbound — a contribution to another project, not a dismech change —
so it is not a design-decision register entry and does not need the §12 route. It is
@gingin77's to raise; she is an EMOD author.

---

## 9. Pilot-comparator state (context)

`Lead_Poisoning` orphan-node defect found while grounding the pilot is filed as
[#8390](https://github.com/monarch-initiative/dismech/issues/8390) and fixed in
[PR #8392](https://github.com/monarch-initiative/dismech/pull/8392) — approved, awaiting
the auto-merge sweep.

After that fix: `Oxidative stress response` and `Mitochondrial dysfunction` are wired
**upstream** from `Systemic lead distribution` but remain **terminal** — no downstream
consequence could be evidenced (candidate sources were animal antioxidant-intervention
studies). The KB-wide backlog is reported on
[#7855](https://github.com/monarch-initiative/dismech/issues/7855): 92 files with no causal
edges at all, 192 with stray orphans.

**Relevance to AOP:** a terminal mechanism node is legal in dismech but would not sit in an
AOP at all — a Key Event needs KERs on both sides to be part of a pathway. That is a real
structural divergence, and it is now a *documented* one rather than an artifact of a broken
entry.

---

## 10. Open questions — all in one place

Nothing here blocks drafting Comment B against the stable half.

1. **AOP-Wiki evidence pages** (§2) — the only genuine blocker for the handbook-rubric half.
   Fetchable without help; flagged only because §7 says agent-authored summaries are not
   assumed verified, so the primary pages should be read rather than the bot's summary.
2. **Is `Causal Agent` genuinely dead**, or dormant/revivable? Recorded as "tried in a
   project, not adopted by the AOP community" — which is how it will be described unless
   corrected.
3. **Does `Phenotype` remain a proposed EC entity**, or has it since been adopted? The
   poster is from 2024 and marks it proposed. Bears on the HP-binding comparison.
4. **Is a two-reference-point structure the right shape for Comment B** (handbook rubric =
   stable/authored; EMOD = provisional/compositional), or should it address only the
   published rubric and leave EMOD out until the properties settle?

---

## Next step

Draft Comment B on #8309: a graded, per-dimension assessment of how far dismech's evidence
model already covers what AOP's KER weight-of-evidence covers — with the EMOD half marked
provisional and dated.
