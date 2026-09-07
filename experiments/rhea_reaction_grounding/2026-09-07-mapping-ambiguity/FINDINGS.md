# Which GO molecular-function terms map to more than one Rhea reaction? (2026-09-07)

**Question.** The [coverage run](../2026-09-07-coverage/FINDINGS.md) reported that 70 of the
284 Rhea-reachable molecular-function terms (24.6%) map to several reactions, so the reaction
is not derivable from the GO term. That headline treats every ambiguous term alike, and it
should not: a term mapping to 67 reactions across different substrates is a different problem
from one mapping to two reactions that differ by a cofactor. This run enumerates all 70 and
separates the two.

Measurement only. No schema file, `kb/` entry, cache, or `conf/` adapter was changed.

## Method

For each MF term used in `kb/` that maps to ≥2 Rhea reactions, take the ChEBI participants of
every mapped reaction, drop the ubiquitous cofactors (water, protons, ATP/ADP/AMP, NAD(P)(H),
O₂, CO₂, phosphate, diphosphate, CoA, FAD — otherwise everything looks related), and intersect
what remains:

- **`SHARED_CORE`** — some non-cofactor participant is common to *every* mapped reaction. The
  reactions are variants on one transformation.
- **`DISJOINT`** — nothing is common to all of them. The mapped reactions are genuinely
  different chemistry and only a curator can choose.

```bash
python3 experiments/rhea_reaction_grounding/ambiguity.py
```

Full table in [`ambiguous_terms.tsv`](ambiguous_terms.tsv) — every term with its reaction
count, KB usage, classification, shared core, and the entries that use it.

## Results

| | Terms | Annotation instances |
|---|---|---|
| `SHARED_CORE` | 36 | 58 |
| `DISJOINT` | 33 | 45 |
| `UNKNOWN` (one reaction had no participants) | 1 | 1 |
| **Total ambiguous** | **70** | **104** |

### The headline number overstates the problem

24.6% is a share of *distinct terms*. Weighted by how often those terms are actually used,
the ambiguous set accounts for **104 of 1,358 molecular-function annotation instances — 7.7%**.
Restricted to the genuinely hard cases, `DISJOINT` covers **45 instances, 3.3%**.

Distinct-term counts overweight rare terms. Most ambiguous terms are used once or twice, while
the terms curators reach for repeatedly tend to be the unambiguous ones. Either denominator is
defensible, but for "how much curator work would this create" the instance count is the one
that matters, and it is about a third of what the term-level figure suggests.

### The tail is thin

| Reactions per term | Terms |
|---|---|
| 2 | 19 |
| 3–5 | 26 |
| 6–10 | 12 |
| 12–23 | 6 |
| 33–67 | 7 |

Over half the ambiguous terms map to 2–3 reactions. Only 7 map to more than 23, and those 7
account for 12 annotation instances between them.

### The most ambiguous terms, and how they split

| GO term | Label | Rxn | Uses | Class |
|---|---|---|---|---|
| `GO:0004022` | alcohol dehydrogenase (NAD+) activity | 67 | 3 | `DISJOINT` |
| `GO:0015020` | glucuronosyltransferase activity | 65 | 4 | `SHARED_CORE` |
| `GO:0003988` | acetyl-CoA C-acyltransferase activity | 47 | 1 | `SHARED_CORE` |
| `GO:0004046` | aminoacylase activity | 42 | 1 | `DISJOINT` |
| `GO:0019166` | trans-2-enoyl-CoA reductase (NADPH) activity | 36 | 1 | `DISJOINT` |
| `GO:0004029` | aldehyde dehydrogenase (NAD+) activity | 34 | 3 | `DISJOINT` |
| `GO:0004806` | triacylglycerol lipase activity | 33 | 2 | `DISJOINT` |
| `GO:0010945` | coenzyme A diphosphatase activity | 23 | 1 | `SHARED_CORE` |
| `GO:0003997` | acyl-CoA oxidase activity | 17 | 1 | `DISJOINT` |
| `GO:0003857` | (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity | 14 | 2 | `DISJOINT` |

The top two are the instructive contrast, and they show the classification is not just
counting.

**`GO:0015020` glucuronosyltransferase, 65 reactions, `SHARED_CORE`.** Every one of the 65
shares `CHEBI:58052` (UDP-alpha-D-glucuronate) and `CHEBI:58223` (UDP). The donor is fixed;
the 65 reactions differ only in the acceptor being glucuronidated. So the shared chemistry —
glucuronosyl transfer from UDP-glucuronate — is stateable without choosing a reaction at all.

**`GO:0004022` alcohol dehydrogenase, 67 reactions, `DISJOINT`.** Once NAD+/NADH and protons
are set aside, nothing is common. The 67 reactions are 67 different alcohols. There is no
shared chemistry to state, and any single reaction would misrepresent the node.

Other shared cores are equally concrete: `GO:0003988` acetyl-CoA C-acyltransferase on
`CHEBI:57288` (acetyl-CoA), and both `GO:0017040` and `GO:0050291` on `CHEBI:57756`
(sphingosine).

## What this means for the design

**A renderer can show more than the coverage run implied.** cmungall's suggestion — display
the reaction and its participants beside the MF term — was defensible for the 75% that map
1:1. This run extends it: for the 36 `SHARED_CORE` terms the shared participants can be
displayed too, without asserting a choice. Concretely, `GO:0015020` renders as glucuronosyl
transfer from UDP-glucuronate across 65 acceptors, which is both true and useful. Only the 33
`DISJOINT` terms need to fall back to a bare count.

That puts the display's honest coverage at **214 unambiguous + 36 shared-core = 250 of 284
reachable terms (88%)**, with 33 showing a count and 1 unclassifiable.

**If a slot is built, `DISJOINT` is its real scope.** The earlier suggestion was to scope a
`reactions:` slot to the ambiguous quarter. This run narrows that further: `SHARED_CORE` terms
do not need a curator, because the informative part is common to all their reactions. The
slot would earn its place on 33 terms covering 45 annotation instances — a very small,
well-defined target, and one worth weighing against the cost of a new prefix, a 163 MB OAK
build, and equations as `term.label`.

## Limits

- **The cofactor list is a judgement call.** 17 ChEBI identifiers are treated as ubiquitous.
  Reasonable people would add or remove a few, and a term sitting on the boundary could flip
  class. The list is at the top of `ambiguity.py` and the classification re-runs if it changes.
- **`SHARED_CORE` does not mean the reactions are interchangeable.** It means they share a
  participant. Whether the shared part is the mechanistically interesting one is a
  curator's call — for glucuronosyltransferase it clearly is; that will not always hold.
- **Intersection is strict.** A term whose reactions fall into two coherent families with no
  single common participant is scored `DISJOINT`, even though a clustering approach would
  find structure. Clustering would be the next refinement.
- **Scope is `kb/**/*.yaml`**, so modules and comorbidities are included here, unlike the
  concordance run which covered disorders only.
- **One `UNKNOWN`** — a term where fewer than two of its reactions had participants recorded.
