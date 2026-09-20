# The Evidence Model

Every mechanistic claim in DisMech — a pathophysiology node, a causal edge, a
phenotype association, a treatment-mechanism link — can carry `evidence`. This page
explains what an evidence item *is* today, what job the model actually performs, and
the direction in which we would like to extend it.

!!! tip "Slide deck"
    A companion walkthrough, worked on the Familial Hypercholesterolemia pathograph,
    is published as a slide deck:
    [**From evidence pointers to experiment-grounded evidence**](../slides/evidence-model-experiment-grounded.html).
    The full write-up is
    [the FH worked example report](../reports/fh-experiment-grounded-evidence-2026-07-30.md).

## What an evidence item is

An `EvidenceItem` is a **validated pointer into the literature**. Its nine fields are:

```yaml
evidence:
- reference: PMID:1301956            # a real, resolvable ID (PMID, DOI, NCT, ORPHA, CGGV, …)
  reference_title: "Molecular genetics of the LDL receptor gene …"
  supports: SUPPORT                  # direction: SUPPORT / REFUTE / NO_EVIDENCE
  directness: DIRECT                 # optional: DIRECT / INDIRECT / UNKNOWN
  quote_role: PRIMARY_RESULT         # optional: PRIMARY_RESULT / BACKGROUND / REVIEW_SYNTHESIS
  evidence_source: HUMAN_CLINICAL    # study type reported in the paper (see below)
  snippet: "…mediates the uptake and lysosomal degradation of plasma LDL…"
  explanation: "When LDLR function is impaired, the core hepatic LDL uptake step fails."
  images: [...]                      # optional figures from deep-research artifacts
```

Four of those fields carry the evidence *semantics*:

- **`supports`** records the **direction** the reference points relative to the claim —
  whether it supports it, contradicts it, or does not bear on it at all.
- **`directness`** (optional) records **how directly** the quoted text bears on the claim —
  whether the quote asserts the claim itself, or asserts something from which the claim
  follows by an inference step. It is not a strength grade.
- **`quote_role`** (optional) records **where in the cited paper's own argument** the
  quoted sentence sits: a finding that paper produced, background it restates from
  elsewhere, or its synthesis of a literature. It is a fact about the document, not a
  grade of the evidence.
- **`evidence_source`** records the **type of study reported in the publication** —
  `HUMAN_CLINICAL`, `MODEL_ORGANISM`, `IN_VITRO`, `COMPUTATIONAL`, or `OTHER`. It
  describes the cited paper, *not* how the entry was curated: an AI-assisted curation of a
  mouse-knockout paper is still `MODEL_ORGANISM`.

### Deciding `directness`: an inferential gap, not a small sample

The test that makes `directness` decidable is **what the quote is about**, not how much of
it there is:

> Is the quoted text about the *same thing* the claim asserts, or about something
> *adjacent*, from which the claim follows only by an inference step?

`INDIRECT` is for the adjacent case. A mouse deletion quoted for a human mechanism, a
transcript's presence quoted for a functional role, a class-level statement quoted for one
member of the class, a management recommendation quoted as evidence that a phenotype
occurs, co-occurrence quoted for a causal direction — in each the reader must take a step
the quote does not take for them.

**A small or uncontrolled study is not `INDIRECT`.** "An uncontrolled n-of-1 observation
cannot establish efficacy" and "five participants cannot establish safety" are statements
about *strength*, and the quote is squarely about the claim. Those items are already
correctly `SUPPORT`, and the model has no strength slot on purpose — see the appraisal
layer below, and design decisions §12. Reaching for `directness` to record a sample-size
caveat would quietly turn it into the strength grade it was defined not to be.

The two can co-occur — a single-animal study quoted for a human claim is `INDIRECT` *and*
weak — but only the first is recordable today. The second belongs in the `explanation`.

### Deciding `quote_role`: whose observation is this?

`reference` records provenance of the **sentence**. `quote_role` records provenance of the
**finding**, which is a different object:

> Did the paper I am citing *produce* this, or is it repeating somebody else's work?

The case that forced the slot is a chick-embryo study whose introduction states the human
clinical picture, perinatal mortality from an inadequate thorax, before reporting its
own bead-implantation experiments. Quote that sentence and no `evidence_source` value is
true. `MODEL_ORGANISM` says a chick measured human perinatal mortality. `HUMAN_CLINICAL`
says the paper ran a human study. `OTHER`, which review pressure tends to settle on, says
nothing, and files this case next to the unrelated "quoted from a review" one.

`HUMAN_CLINICAL` + `quote_role: BACKGROUND` is true and queryable, and that combination is
the point: the two fields answer different questions and neither substitutes for the other.

- **`PRIMARY_RESULT`**: the cited publication produced this observation, measurement,
  analysis, or conclusion.
- **`BACKGROUND`**: it is restating something established elsewhere, such as an introduction, a
  framing sentence, a motivation.
- **`REVIEW_SYNTHESIS`**: it is the publication's synthesis of work it did not perform, such as a
  review, commentary, editorial, or consensus statement.

**Leave it off unless you have assessed it**, exactly as with `directness`. There is no
`UNKNOWN`; absent already says nobody has judged it, which is the state of almost the whole
knowledge base.

**It is partly derivable, and that is why it is authorable.** The standing objection to new
evidence metadata in this project is that a freely-authored grade reopens the fabrication
surface the grounding layer closes. `quote_role` is not a grade, and for a reference whose
cached body carries NLM structured-abstract labels the answer is a string containment
rather than a judgement:

```bash
just list-background-citations                  # the worklist, three tiers
just list-background-citations --format tsv     # one row per candidate
just list-background-citations --tier A         # the deterministic tier alone
```

Report-only, and deliberately not an autofill. The deterministic tier covers a minority of
the corpus, a structured `BACKGROUND:` paragraph routinely closes with the authors' own
framing of what *they* did, and the MeSH tier is a heuristic whose count is a lower bound
on a narrow slice rather than a measure of the problem. Read the sentence.

Two things the enum deliberately does not cover. A quoted **aim** statement ("the aim of
the present study was to…") is neither a finding nor somebody else's fact; the report flags
those separately rather than the enum growing a value for them. And a quote taken from a
**full text**, such as a Discussion paragraph, a figure legend or a guideline recommendation box,
has no NLM labels to sit between, so the deterministic tier declines to classify it rather
than guessing. That is the `quoted_section` question in
[#9711](https://github.com/monarch-initiative/dismech/issues/9711), and it needs a section
parser this does not have.

## Two layers: grounding and appraisal

It helps to read the model as two layers.

**The grounding layer is strong.** The load-bearing machinery is `reference` + `snippet`
plus the `linkml-reference-validator` pipeline, which enforces that the reference resolves
and the quoted `snippet` is an *exact substring* of the cited text. This is DisMech's
primary defence against fabrication — see the
[Evidence & provenance policy](design-decisions.md#6-evidence-provenance-policy) in the decision register. The
supporting discipline lives across the project:

- **Exact-snippet rule** — paraphrase fails validation; only verbatim quotes pass.
- **Tool-generated cache** — `references_cache/*.md` files are created only by
  `just fetch-reference` or the validator, never hand-written.
- **Deep-research outputs are leads, not ground truth** — every PMID, snippet, and
  ontology term suggested by a DR tool is verified before commit, including a
  Named-Entity-Confusion preflight that the report describes the intended disease.

Together this answers a precise question: *"is this citation real, and does the quoted
text actually appear in it?"* That is **citation integrity**.

**The appraisal layer is thin.** What the model does *not* yet capture is how *strong* the
evidence is, *what experiment* produced it, and *how* the mechanistic claim was inferred
from that experiment. `supports` is direction, `directness` is inferential distance and
`quote_role` is document provenance; none is strength, so a single case report and a
human natural-knockout study both collapse to `SUPPORT`. `evidence_source` is a coarse
organism bucket — every human observation from an n=1 case report to a large randomised
trial is one value, and it says nothing about study design or inferential power.

So, candidly: the evidence model today is mostly a citation-integrity harness with a thin
polarity/provenance layer on top. That is a deliberate and defensible starting point — a
freely-authored "certainty" grade would reopen exactly the fabrication surface the
grounding layer was built to close — but it is not yet evidence *appraisal*.

## The direction of travel: experiment-grounded evidence

The gap is clearest on a well-studied mechanism. On the Familial Hypercholesterolemia
`PCSK9` entry, this already-validated snippet sits on the record:

> "Overexpression of PCSK9 in HepG2 cells caused a decrease in whole-cell and cell-surface
> LDLR levels. PCSK9 overexpression had no effect on LDLR synthesis but caused a dramatic
> increase in the degradation of the mature LDLR"

That single string already contains a whole experiment — a **system** (HepG2 cells), a
**perturbation** (PCSK9 overexpression, a gain-of-function manipulation), a **readout**
(LDLR level, synthesis, degradation), a **result** (LDLR down, synthesis unchanged,
degradation up), and an **inference** (PCSK9 acts post-translationally to drive LDLR
degradation — a *sufficiency* claim). The model stores all of it as an opaque `string`
with `supports: SUPPORT`, so none of it is queryable.

The proposed extension keeps the exact-snippet discipline but lets an evidence item
optionally decompose that micropublication: a structured `experiment` block
(`design`, `system`, `perturbation`, `readout`, `result`, `inference`) plus two small
closed enums — `experiment.design` (*how it was shown*) and `inference.role` (*what the
result licenses about the causal edge*: necessity, sufficiency, rescue, direct-physical,
therapeutic-rescue). Crucially, **strength stays derived, not authored** — read off the
typed, snippet-anchored `design` and `inference.role`, which mutually constrain each other
(an overexpression cannot establish necessity), rather than from a subjective grade.

This is why FH is the gold-standard mechanism: necessity (loss-of-function), sufficiency
(gain-of-function), direct mechanism, and therapeutic rescue all converge on the same
arrows — and that convergence is the actual evidence. The
[slide deck](../slides/evidence-model-experiment-grounded.html) and
[worked-example report](../reports/fh-experiment-grounded-evidence-2026-07-30.md) develop
this in full, including how it composes with `causal_link_type`, `target_mechanisms`, and
`association_signals`, and why a bespoke enum is preferred over ECO with SEPIO reserved for
the export layer.

## Related pages

- [Design Decisions §6 — Evidence & provenance policy](design-decisions.md#6-evidence-provenance-policy)
- [Frequency Evidence Guidelines](../frequency-evidence-guidelines.md) — why a phenotype
  `frequency:` band needs its own evidence, separate from the association
- [Pathographs](../pathographs.md) — the causal-graph structure that evidence attaches to
- [FH worked example](../reports/fh-experiment-grounded-evidence-2026-07-30.md) ·
  [slide deck](../slides/evidence-model-experiment-grounded.html)
