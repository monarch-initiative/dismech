---
name: coarse-phenotype-bindings
description: >
  Choose, review, or repair the `coarse_binding_basis` on a phenotype bound to a
  coarse HPO term — an organ-system root or a whole-organ/region term. Use when
  `just check-coarse-phenotypes` reports a binding, when picking between
  VARIABLE_SPECTRUM, SOURCE_UNSPECIFIED, NO_HPO_TERM and PATHOGRAPH_HUB, when
  deciding whether to widen the coarse set, or when reviewing a PR that declares
  a basis. Not for ordinary term selection — see dismech-terms for that.
---

# Coarse phenotype bindings

A phenotype bound to a coarse HPO term — `HP:0000478` *Abnormality of the eye*,
`HP:0002664` *Neoplasm*, `HP:0000077` *Abnormality of the kidney* — passes every
other gate while saying almost nothing. `Schaaf-Yang_Syndrome` named strabismus,
esotropia and myopia in its `description` and then discarded all three in the
binding.

Such a binding is not forbidden. It must **say why**.

```bash
just check-coarse-phenotypes                  # gate (offline, in `just qc`)
just list-coarse-phenotypes                   # census, incl. hub convergence
just update-coarse-phenotype-baseline         # only ever to SHRINK
```

## The four values

| Value | Means | Companion requirement |
|---|---|---|
| `VARIABLE_SPECTRUM` | involvement varies in form between patients | none — a bare declaration |
| `SOURCE_UNSPECIFIED` | the cited source characterizes it no further | none — the snippet is the proof |
| `NO_HPO_TERM` | narrower than any HP term | `preferred_term` ≠ the bound label; record `term_gap` |
| `PATHOGRAPH_HUB` | a deliberately unqualified convergence node | ≥1 causal edge targets it; no `frequency` |

Two take no companion at all. That is the point: the guard asks you to state a
reason, not to do extra work proving it.

## This is not a rule to prefer narrow terms

Manufacturing a specificity the source does not support is a worse defect than a
coarse binding, and the term contract forbids it. There is deliberately no depth
or information-content metric: `HP:0004322` *Short stature* is the most-used HP
term in the KB, and `HP:0001627` *Abnormal heart morphology* carries "Congenital
heart defect" as an EXACT synonym — so any such metric would flag the two terms
most often exactly right.

The coarse set is 56 hand-reviewed terms across two `meaning:`-bound schema
enums: `PhenotypeCategoryEnum` (the 23 organ-system roots, which are also the
browser's facet vocabulary) and `CoarsePhenotypeTermEnum` (33 terms below those
roots that still name a system, organ or region). Widening it is a schema PR
with an argument, not a threshold. `coarse_phenotype_terms.yaml` records the
inclusion rule and why each near-miss was left out.

## Picking the right value

### The commonest confusion: spectrum vs. unspecified

**If you can list the findings, it is not a spectrum — they are phenotypes.**
`VARIABLE_SPECTRUM` is for involvement that is real but whose form varies with
no characteristic finding to bind, so there is nothing to list. That is why it
takes no companion slot. Where the source *does* name findings and you have a
quote, curate each as an ordinary `phenotypes` entry beside the coarse one —
`ALG12_Congenital_Disorder_of_Glycosylation` is the pattern: specific phenotypes
added *beside* the coarse node, not instead of it.

A `spectrum_terms` slot for listing them inside the binding was built and
removed before this shipped. It produced second-class annotations the phenotype
table, the facets and the exports could not see, and it inverted the value's
meaning by demanding enumeration of exactly the case where enumeration is
impossible. Do not reintroduce it.

`SOURCE_UNSPECIFIED` is the archetype of a review-article or GeneReviews **list
sentence**: *"Additional features include ocular abnormalities, hearing loss,
respiratory difficulties"*. The source names the finding and characterizes it no
further. If that is your snippet, this is almost always your value.

### `PATHOGRAPH_HUB`: a hub is defined by its INCOMING edges

Do **not** connect a hub to its constituent findings with `sequelae`. That slot
is a `CausalEdge`, and a coloboma is not *caused by* an eye abnormality — it
*is* one. Drawing subsumption as causation would corrupt the graph to satisfy a
guard. A hub reached by a mechanism is complete on its own; the specific
findings, where known, are ordinary phenotype entries beside it.

A hub is also **not** a "disruption of eye development" node — that belongs in
`pathophysiology`, binds GO, and asserts a process, where a hub binds HP and
asserts a system-level outcome. The two may sit in sequence.

A coarse node carrying a `frequency` is a `VARIABLE_SPECTRUM`, not a hub.

**An arriving edge proves nothing on its own — check it is convergence, not
fan-out.** This is the failure the guard cannot catch, and it reached review
once (#11922). In `Rubinstein-Taybi_Syndrome`, *Ocular abnormalities* was
declared a hub on the strength of one incoming edge — which turned out to be one
of **twenty** `INDIRECT_UNKNOWN_INTERMEDIATES` targets of a single upstream
node. *Short stature*, *Obesity* and *Broad thumb* satisfied the guard
identically and are plainly not hubs. Nothing converged: the entry contained no
cataract, coloboma, glaucoma or refractive error for a system-level node to
summarize, and the snippet was a GeneReviews list sentence. It was
`SOURCE_UNSPECIFIED`, and its structurally identical sibling *Renal
abnormalities* had been baselined rather than declared.

So before declaring a hub, ask three things the guard does not:

1. **Does the mechanism converge here, or does this node just happen to be one
   arm of a wide fan-out?** `just list-coarse-phenotypes` prints incoming-edge
   count and the widest fan-out among the sources, and flags a source fanning
   out past 3. That is advisory: a real hub can be reached from a node that also
   points elsewhere, and no threshold separates the two cases.
2. **Is the coarseness a property of the biology, or of the source?** If the
   source simply said no more, that is `SOURCE_UNSPECIFIED`.
3. **Is there anything for it to be a hub of?**

**Worked example: `Noonan_Syndrome` *Tumor Predisposition* (`HP:0002664`).**
`RASopathy Neoplastic Predisposition` — a mechanism node — targets it and
nothing else, so the mechanism converges there rather than fanning out. And the
coarseness is intrinsic: germline RAS/MAPK hyperactivation raises risk across
haematopoietic and solid lineages instead of producing one characteristic
tumour, and the reported tumours differ by genotype, so no narrower HP term is
right for the node the mechanism reaches.

## Worked examples, one per value

| Value | Entry |
|---|---|
| `VARIABLE_SPECTRUM` | `Schaaf-Yang_Syndrome` |
| `SOURCE_UNSPECIFIED` | `PAICS_Deficiency`, `Rubinstein-Taybi_Syndrome` |
| `NO_HPO_TERM` | `Li-Fraumeni_Syndrome` |
| `PATHOGRAPH_HUB` | `Noonan_Syndrome` |

## The baseline

The bindings predating the slot are grandfathered in
`tests/coarse_phenotype_baseline.txt`, which **may only shrink** — except when
the coarse set itself is deliberately widened, or when the snapshot is retaken
against a moved `main` (the baseline is a snapshot of the pre-existing backlog
at the moment the guard lands, so refreshing a long-lived branch retakes it).
Both exceptions are argued in the diff that takes them; see the docstring on
`test_baseline_only_shrinks`.

Clearing a row means a curator decided between the four values, or bound a
specific term instead. A companion-rule violation is never grandfathered,
because a declared basis can only come from content written after the slot
existed.

Reference: [`docs/coarse-phenotype-bindings.md`](../../../docs/coarse-phenotype-bindings.md).
