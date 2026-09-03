# "Unclassified cardiomyopathy" (MONDO:0016343) — OUT_OF_SCOPE

**Date:** 2026-09-03
**Concept:** `MONDO:0016343` — *obsolete unclassified cardiomyopathy*
**Decision:** `OUT_OF_SCOPE`. No `kb/disorders/` entry, no `kb/groupings/` entry,
and no `stubs/` file.

## Why this note exists rather than an entry

A curation request came in for "obsolete unclassified cardiomyopathy". The
concept resolves to a real MONDO identifier, so it is not a hallucination, but
it is not curatable and should not be re-nominated. This note records the
determination so the next person to meet the term does not repeat the work.

## What MONDO says

`MONDO:0016343` is deprecated. Its metadata is unambiguous:

| Property | Value |
|---|---|
| `rdfs:label` | obsolete unclassified cardiomyopathy |
| `owl:deprecated` | `true` |
| obsolescence reason (`IAO:0000231`) | `OMO:0001000` — **out of scope** |
| `oio:consider` | `MONDO:0004994` (cardiomyopathy) |
| tracker (`IAO:0000233`) | monarch-initiative/mondo#2824 |
| `oio:inSubset` | `ordo_group_of_disorders`, `disease_grouping` |
| `skos:exactMatch` | `ORDO:217678` |

Two things follow. First, MONDO's own recorded reason for retiring the term is
*out of scope* — the same judgement this note is making, reached independently
by the ontology it would have been bound to. The MONDO ticket obsoleted it as a
"too general/non-specific grouping class". Second, the term was never a disease:
both of its subsets mark it as a group of disorders, inherited from the Orphanet
classification, where "unclassified cardiomyopathy" is the residual bucket for
forms that fit none of the morphofunctional categories.

The term is also structurally uncurateable here. Deprecated MONDO terms are
detached from the hierarchy:

```
$ runoak -i sqlite:obo:mondo ancestors MONDO:0016343
id              label
MONDO:0016343   obsolete unclassified cardiomyopathy
```

It has no ancestors, so it is not reachable from `MONDO:0000001`, so it cannot
satisfy the `DiseaseTerm` dynamic enum in `src/dismech/schema/dismech.yaml`.
Binding it as a `disease_term` fails `just validate-terms` outright.

## The repository already encodes this rule

Three existing mechanisms independently reject an obsolete term, which is worth
saying because it means this decision is not a new policy:

- `src/dismech/stubs/seed.py` skips any nomination whose label starts with
  `obsolete` — *"Nothing downstream should ever ask a curator to model one."*
- `src/dismech/stubs/model.py` reports such a stub as `obsolete_term`
  ("stale, tidy up"), and `just tidy-stubs --apply` deletes it.
- `docs/mondo-prioritizer.md` uses **this exact term** as its worked example of
  a candidate dropped as obsolete.

`StubEntryTypeEnum.OUT_OF_SCOPE` in `src/dismech/schema/curation_stub.yaml`
names "an obsolete concept" explicitly, so the vocabulary for this outcome
already exists.

That is also why there is no tombstone stub. A stub for a retired MONDO term is
exactly what `tidy-stubs` is built to sweep, so it would not survive as a
record. `docs/curation-notes/` is the durable home for the decision.

## Nothing is lost by declining it

The historical bucket's contents are already curated individually. Checked with
`dismech.compare.mondo_priority.iter_covered_mondo_ids` over `kb/`:

| Concept | MONDO | Entry |
|---|---|---|
| dilated cardiomyopathy | `MONDO:0005021` | `Dilated_Cardiomyopathy.yaml` |
| hypertrophic cardiomyopathy | `MONDO:0005045` | `Hypertrophic_Cardiomyopathy.yaml` |
| restrictive cardiomyopathy | `MONDO:0005201` | `Restrictive_Cardiomyopathy.yaml` |
| arrhythmogenic RV cardiomyopathy | `MONDO:0016587` | `Arrhythmogenic_Right_Ventricular_Cardiomyopathy.yaml` |
| left ventricular noncompaction | `MONDO:0018901` | `Left_Ventricular_Noncompaction.yaml` |
| Tako-tsubo cardiomyopathy | `MONDO:0019018` | `Takotsubo_Cardiomyopathy.yaml` |

The last two are the ESC "unclassified cardiomyopathies" category itself, so the
concept's actual clinical content is covered by name. Around fifty further
cardiomyopathy disorder entries, two groupings
(`Familial_Dilated_Cardiomyopathy`, `Familial_Hypertrophic_Cardiomyopathy`) and
the `cardiomyopathy_maladaptive_remodeling` module sit alongside them.

## Open gap this surfaced

`MONDO:0004994` (*cardiomyopathy*) — the term MONDO tells you to consider
instead — is **not covered** by any `kb/` entry. It is referenced only in the
prose description of `kb/modules/cardiomyopathy_maladaptive_remodeling.yaml`.

This is a separate question and is deliberately not settled here. Whether the
cardiomyopathy root deserves a `Grouping` (a curated union over the five
morphofunctional entries, in the shape of the two existing familial groupings)
or nothing at all is a lump/split call that should be argued on its own merits,
not carried in on the back of an obsoleted term. Flagging it, not deciding it.

## Deep research

Not run. The question this request turns on is whether the concept can be a
dismech entry, and MONDO answers that directly: the term is deprecated, detached
from the hierarchy, and retired as out of scope. A literature report on
cardiomyopathy cannot make a retired grouping term curatable, and the disease
content it would return is already in the entries listed above.
