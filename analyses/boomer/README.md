# boomer

Is dismech's curated structure logically consistent with MONDO's?

dismech grounds its entries in MONDO, and separately asserts its own hierarchy
through `has_subtypes` and `kb/groupings/`. Those are independent claims, and
they can disagree. Nothing in the validation stack checks that they don't:
`just validate-terms` confirms a term *exists* and that its label matches;
`linkml-reference-validator` checks quoted evidence. Neither asks whether two
terms stand in the relationship dismech's own structure implies.

This tree answers that question per disease, using
[`boomer-py`](https://github.com/monarch-initiative/boomer-py) — a Python
reimplementation of BOOMER, which resolves competing ontology mappings by finding
the most probable globally consistent assignment.

## Layout

```
analyses/boomer/
  index.tsv                     roll-up: one row per disorder
  disorders/<NAME>/
    README.md                   what was checked, per-subtype verdicts, what boomer did
    kb.yaml                     boomer input; `pyboomer solve kb.yaml -t 60 -C 6`
    solution.yaml               boomer output, machine-readable
    solution.md                 boomer output, rendered
  groupings/                    grouping membership vs MONDO (no solver needed)
  cross-source/                 direct ICD/NCIT mappings vs MONDO's own xrefs
  scripts/                      generators; nothing here is hand-written
```

One knowledge base per *disorder* rather than per subtype pair: an entry's
subtypes share a parent, so solving them together lets a conflict in one bear on
the others, and it matches how a curator reads the result.

## What each KB contains

| Source | Strength | Content |
|---|---|---|
| dismech | hard | `subtype ProperSubClassOf parent` for each grounded subtype; namespace disjointness so two distinct entries cannot collapse |
| MONDO | hard | subsumption edges and `owl:disjointWith` axioms relating the entry's term to each subtype's term |
| dismech→MONDO | probabilistic | one identity claim per grounded term (p=0.90), with the competing `ProperSubClassOf` readings in both directions (0.07 / 0.03) |
| MONDO→external | probabilistic | MONDO's `skos:exactMatch` links (p=0.95) into DOID, NCIT, ORDO, OMIM, ICD10CM, icd11f, MESH, EFO |
| external | hard | each of those ontologies' **own** subsumption edges among the mapped terms |

Ontologies are loaded as *hard* facts deliberately: the question is whether
dismech is consistent with them, not whether they are consistent with themselves.

**Only `skos:exactMatch` is used for the MONDO→external step.** MONDO also
carries `oio:hasDbXref` — 143,373 of them against 109,307 exactMatches — but a
dbxref asserts a cross-reference of unstated strength. Reading those as
equivalencies would inject identity claims MONDO never made into every KB.

### Why more than two sources matters

With only dismech and MONDO, most disagreements are unresolvable: MONDO either
has an opinion or it doesn't, and when it doesn't there is nothing to appeal to.
Each additional vocabulary MONDO confirms an equivalency into is an independent
opinion on the same subsumption, and that is what BOOMER is actually built for.

Concretely, of the 161 pairs where **MONDO is silent**:

| | n |
|---|---|
| **another ontology corroborates dismech** | **38** |
| shared vocabulary, but silent there too | 68 |
| no shared vocabulary to appeal to | 55 |
| another ontology contradicts dismech | **0** |

So a quarter of the apparent "MONDO gaps" are not open questions at all — they
are places where DOID, NCIT, ORDO, icd11f or MESH already assert the edge that
MONDO lacks. `Autoimmune_Encephalitis`' anti-NMDA subtype is the clean example:
NCIT (`NCIT:C94853`) and ORDO (`ORDO:217253`) both place it under autoimmune
encephalitis; MONDO has it only under *encephalitis*. That is a well-evidenced
enrichment proposal rather than a guess.

Nothing contradicts dismech in any source, which is worth stating as its own
result.

## Current results

371 disorders, 1,471 grounded parent/subtype pairs. Full roll-up in
[`index.tsv`](index.tsv).

| Per pair | n | | Per disorder | n |
|---|---|---|---|---|
| `AGREES` | 1,296 | | `ALL_MAPPINGS_CONSISTENT` | 318 |
| `SILENT` | 161 | | `RETRACTED` | 53 |
| `SAME_TERM` | 13 | | timed out | 0 |
| `REVERSED` | 1 | | | |

**88.1% of pairs agree.** Where a curator asserted a subtype relation and both
sides are grounded, MONDO independently corroborates it nearly nine times in ten.

Adding the external sources roughly tripled the retraction count when measured
on the same KB snapshot. The pair-level verdicts are unaffected — those only
involve dismech and MONDO — but many more disorders carry a constraint set that
cannot be satisfied, because there are more independent opinions available to
disagree.

### Four distinct things force a retraction

Solving a whole disorder at once — rather than each pair separately — is what
makes the second and third of these visible at all. Each pair looks fine in
isolation.

1. **A directional contradiction** — MONDO placing the entry's term *under* its
   own subtype's term, so the chain closes to `subtype < subtype`.

   The worked case, [`Adult_Refsum_Disease`](disorders/Adult_Refsum_Disease/),
   has since been **resolved and now reports consistent**, which is worth
   following as the intended workflow. MONDO defines `MONDO:0009958` clinically
   but axiomatizes it `is_a MONDO:0100258` phytanoyl-CoA hydroxylase deficiency,
   restricting adult Refsum disease to PHYH-caused disease — false, since
   GeneReviews gives *PHYH* >90% and *PEX7* <10%, and MONDO's own
   `MONDO:0100307` is defined as "an adult Refsum disease… caused by PEX7".
   MONDO tracks the fix in
   [mondo#10377](https://github.com/monarch-initiative/mondo/issues/10377).

   dismech's structure was correct; what was wrong was reading the grounding as
   identity. The entry now records `MONDO:0009958` as `skos:narrowMatch` — its
   own scope is broader than the MONDO class as axiomatized — and the
   contradiction dissolves. The pair verdict stays `REVERSED`, because MONDO's
   hierarchy genuinely is inverted; it is simply no longer unsatisfiable.

   **Curated predicates are respected.** Where an entry records a
   narrow/broad/relatedMatch on its own `disease_term`, that predicate sets the
   priors instead of the default identity assumption. Asserting identity over a
   curator who explicitly said otherwise manufactures contradictions out of
   correct curation. Relatedly, a rejected identity claim only counts as a
   retraction when it was asserted at prior ≥ 0.5 — rejecting a deliberately
   low-prior alternative is the expected outcome, not a conflict.

2. **A subtype grounded to its parent's term** (13 pairs). If both are identity
   claims, the subtype and the entry are the same thing — which contradicts the
   `has_subtypes` edge between them.

3. **Sibling subtypes grounded to the same term** — dismech drawing a distinction
   MONDO does not:
   - [`Juvenile_Idiopathic_Arthritis`](disorders/Juvenile_Idiopathic_Arthritis/):
     "Polyarticular RF-negative" and "RF-positive" both → `MONDO:0018456`
     *polyarticular juvenile idiopathic arthritis*. MONDO does not split on RF
     status.
   - [`Double_Outlet_Right_Ventricle`](disorders/Double_Outlet_Right_Ventricle/):
     "Subaortic VSD" and "Doubly committed VSD" both → `MONDO:0018498`, whose
     label is literally *"subaortic **or** doubly committed"*.
   - [`Malaria`](disorders/Malaria/): "Plasmodium vivax malaria" and "Recurrent
     vivax malaria" both → `MONDO:0005921`.

   Splitting more finely than MONDO is a legitimate curation choice. What it
   means is that the grounding cannot be an *identity* claim for every sibling —
   at most one can be `exactMatch`.

4. **A MONDO "proxy merge"** — one MONDO term claiming identity with several
   terms in the same external vocabulary. This class only appears once external
   sources are loaded, and is now the largest: 47 of the 66 retracted
   equivalences are MONDO↔external rather than dismech↔MONDO.

   It arises from merging. When MONDO merges two of its classes, the
   merged-away class's xrefs move to the survivor — so if the source ontology
   never merged the corresponding terms, MONDO ends up asserting an equivalence
   between them *by proxy*. MONDO tracks this as a known problem
   ([mondo#6331](https://github.com/monarch-initiative/mondo/issues/6331),
   which notes proxy merges are "playing havoc with our attempts to use
   boomer"; see also #6385, #6386, #6429).

   The worked case is `MONDO:0012215` *myofibrillar myopathy 3*, which absorbed
   `MONDO:0008032` (LGMD type 1A) and `MONDO:0008448` (spheroid body myopathy)
   after OMIM merged 182920 into 609200
   ([mondo#6203](https://github.com/monarch-initiative/mondo/issues/6203)). OMIM
   and DOID both merged, so their extra targets are obsolete; **Orphanet and
   MeSH did not**, leaving `ORDO:268129` + `ORDO:98911` and three MeSH terms all
   active and now implicitly equated.

   That obsolete/active split is MONDO's own discriminator — #6331 calls a
   conflict whose extra targets are obsolete a *fake* proxy merge. Applying it
   across the eight vocabularies with local builds:

   | | n |
   |---|---|
   | MONDO terms with >1 `exactMatch` into one checkable vocabulary | 326 |
   | **real proxy merge** (>1 target still active in source) | **300** |
   | "fake" (extra targets obsolete) | 26 |

   Real ones by vocabulary: DOID 114, MESH 65, NCIT 45, ORDO 43, icd11f 30,
   ICD10CM 18, OMIM 8. SCTID and UMLS/MEDGEN are excluded — no local build, so
   they cannot be checked either way.

   `build_analyses.py` skips obsolete equivalency targets for this reason. Worth
   being clear that **this changed none of the numbers above**: the retraction
   counts and the 50 retracted equivalences are byte-identical with and without
   the filter, because none of the 26 fake cases involve a dismech-grounded
   disorder. It is correct in principle and currently only makes the run faster.

   This is not a dismech defect at all — it is visible only because dismech
   grounds into MONDO and this analysis then follows MONDO outward. The 300-term
   list is probably more use to MONDO than to dismech.

The 118 `SILENT` pairs are a separate output: not errors, but places MONDO
asserts no relation where dismech does. Several are textbook — `MONDO:0021081`
*anti-NMDA receptor encephalitis* does not sit under `MONDO:0020640` *autoimmune
encephalitis*. They read as candidate MONDO enrichment proposals.

**Nothing in `kb/` has been changed on the strength of this tree.**

## Reading a verdict

Per subtype:

- **`AGREES`** — MONDO has the subtype's term as a descendant of the entry's term.
- **`SILENT`** — MONDO relates them in neither direction. Consistent but
  uncorroborated; usually a missing `is_a` edge in *MONDO*, not a dismech error.
- **`REVERSED`** — MONDO has the entry's term as a descendant of the subtype's,
  i.e. backwards from dismech. With both identity claims this is unsatisfiable.
- **`SAME_TERM`** — subtype and entry grounded to the same term.

Per disorder, boomer either accepts every mapping (`ALL_MAPPINGS_CONSISTENT`) or
retracts one to restore consistency (`RETRACTED`). **A retraction says the
assertions are jointly unsatisfiable, not that the retracted mapping is the wrong
one** — choosing which to give up is a curation decision, and none has been made
in the KB on the strength of this tree.

## Where the solver earns its place, and where it doesn't

Worth stating plainly, because it bounds how much to read into this tree.

dismech's `disease_term` is a **grounding**, not an identity claim — the schema
defines it as "The MONDO disease term for this disease", and `subtype_term` as
"The ontology term grounding this subtype… Prefer MONDO when available". Only
`mappings[].mapping_predicate` asserts a `skos:` relationship. Treating a shared
`disease_term` as a shared `skos:exactMatch` manufactures conflicts that are not
there: 136 MONDO terms are grounded by more than one entry, but that is correct
when MONDO has no more specific term (five NSCLC molecular-subtype entries all
ground to `MONDO:0005061` *lung adenocarcinoma*). Under the correct reading only
**one** term in the KB has two entries claiming `exactMatch` to it.

So the KB contains few jointly-unsatisfiable constraint sets, and most of what
this tree finds is not exotic. Of the three retraction causes above, two —
a subtype sharing its parent's term, and two siblings sharing a term — are
findable by a `groupby` over the grounded terms. Anyone can write those checks.

What the solver adds is two things. First, **reach**: the directional
contradiction in
[`disorders/Adult_Refsum_Disease/`](disorders/Adult_Refsum_Disease/) is not
findable that way. Every term exists, every label matches, each mapping is
individually plausible, and no two entities share a term. It only exists as the
composition of dismech's subtype edge, the two identity mappings, and MONDO's
`is_a` — and `ProperSubClassOf` being irreflexive. No amount of grouping surfaces
it.

Second, **uniformity**: all three causes fall out of one constraint set without
anyone having anticipated them. The sibling-collision class was not something
this analysis set out to look for; it appeared because the KB was solved per
disorder rather than per pair. A hand-written check finds the errors you thought
of.

That is a real but bounded benefit. It is not a case for taking on boomer as a
dependency, and none has been taken.

## Reproducibility

Regeneration is **partially** reproducible, and it is worth being precise about
which half:

| File | Stable across runs? |
|---|---|
| `kb.yaml` | **yes** — byte-identical; the generator's input assembly is deterministic |
| `README.md` | **yes** — byte-identical; every verdict and retraction is stable |
| `solution.yaml` / `solution.md` | **no** — posterior magnitudes and combination counts drift |

The drift is not rounding. Given the *same* `kb.yaml`, two boomer runs report
different totals — 668 versus 568 `number_of_combinations` for
`Adult_Refsum_Disease` — while both claim
`proportion_of_combinations_explored: 1.0`, and posteriors differ in the fourth
significant figure (0.919037 against 0.920144). Same input, different output:
the non-determinism is inside the solver's search, not in this generator.

**Every True/False verdict was identical across those runs.** The decisions are
reproducible; only the magnitudes are not. Since the verdicts are what
`README.md` and `index.tsv` carry, and what a curator acts on, the tree is
usable — but do not read a posterior difference between two regenerations as a
change in the analysis, and do not diff `solution.*` expecting a clean result.
`just boomer-check` therefore diffs only the solver-free outputs.

Floats are rounded to 12 decimal places and wall-clock timings dropped, which
removes a separate and purely cosmetic source of churn (last-bit float noise and
`time_started`/`time_finished`), but cannot address the search non-determinism
above.

## Limits

- **`SILENT` is not proof of a MONDO gap.** It is the absence of an asserted path.
  Some may be legitimately unrelated. Each needs a human before going upstream.
- **Consistency is not correctness.** That boomer accepts a mapping means nothing
  it was given contradicts it. MONDO carries only 533 `owl:disjointWith` axioms,
  so the constraint doing the work is weak.
- **Priors are uniform and uncalibrated** (0.90 per identity claim). Nothing here
  tests whether they discriminate; the `REVERSED` result rests on
  unsatisfiability, not on posterior ranking.
- **Partitioning is load-bearing.** boomer's `partition_initial_threshold`
  defaults to 200, which never triggers at this scale — and without it the search
  is exponential in pfacts, so even a 12-pfact entry (Alagille syndrome) times
  out at 25s and a 120-pfact one (Joubert) is hopeless. The generator sets it to
  6, which splits each KB into independent cliques and drops those same solves to
  under 0.05s. This is sound here because boomer partitions on connected
  components and a disorder's subtypes share only the parent — but it does mean
  the solver is not searching the whole KB jointly, and a genuine
  cross-subtype interaction outside a component would be missed. No entry times
  out at present; any that did would be marked `TIMED_OUT` in `index.tsv` and its
  own `README.md`, and its assignment treated as indicative only.

  **This leaks into reproduction.** `partition_initial_threshold` is a solver
  setting, not something serialised into `kb.yaml`, and the CLI has no flag for
  it — so a plain `pyboomer solve kb.yaml` runs at the default of 200 and times
  out. `--max-pfacts-per-clique` (`-C 6`) triggers the same partitioning and
  reproduces these results exactly, which is why every documented command here
  carries it.
- **Grounded pairs only.** Subtypes without a `subtype_term` are invisible here.
- **MONDO is a fixed snapshot** (`~/.data/oaklib/mondo.db`). Re-run before acting.

## No dependency was added

`build_analyses.py` takes `--boomer-src` pointing at a `boomer-py` checkout;
`grouping_audit.py` and `crosssource_audit.py` need no solver at all. **Nothing
in the repo imports boomer.** That is deliberate — boomer-py is early-stage, and
this analysis does not justify taking it on as a runtime dependency.

## Regenerating

```bash
uv run --with networkx python analyses/boomer/scripts/build_analyses.py \
    --out analyses/boomer/disorders --index analyses/boomer/index.tsv \
    --boomer-src ~/repos/boomer-py/src

uv run python analyses/boomer/scripts/grouping_audit.py \
    --out analyses/boomer/groupings/violations.tsv

uv run python analyses/boomer/scripts/crosssource_audit.py \
    --out analyses/boomer/cross-source/disagreements.tsv
```

All read a local semantic-sql MONDO build at `~/.data/oaklib/mondo.db`.

## Sibling analyses

Two further checks live here because they came from the same investigation, and
neither needs a solver:

- [`groupings/`](groupings/) — members of `exactMatch`-mapped `kb/groupings/`
  entries against the grouping's own MONDO term. 187/204 agree (91.7%), 2
  `SAME_TERM`, 15 violations, **zero contradictions**. The 8 are MONDO gaps again:
  nephronophthisis is not under `MONDO:0005308` *ciliopathy*; *lissencephaly due
  to TUBA1A mutation* is not under `MONDO:0100153` *tubulinopathy*. Only
  `exactMatch` groupings are checked — a `broadMatch` grouping is explicitly
  narrower than its term and a `narrowMatch` one wider, so neither licenses the
  descendant expectation; 52 of 65 are skipped on that basis.
- [`cross-source/`](cross-source/) — dismech's direct ICD/NCIT mappings against
  MONDO's own xrefs. **A negative result**: 8 disagreements, 6 of them
  granularity the `mapping_predicate` already records honestly
  (`ICD10CM:Q93.5` vs `ICD10:Q93.51` as `narrowMatch`). Nothing for a reasoner to
  resolve. Recorded so the check is not repeated expecting signal.

That the subtype (88.1%) and grouping (91.7%) checks land on comparable
agreement rates with the same failure mode, across two structurally independent parts of the
schema, is itself worth noting.

## Methodological notes

Two mistakes made and corrected while building this, recorded so they are not
repeated:

- **Circular lexical evidence.** An earlier specificity audit (which produced the
  regroundings in #8671) used `disease_term.preferred_term` as a lexical synonym
  when matching entries against MONDO labels. That string is *derived from the
  mapping under test*, so it corroborated the mapping with itself. Excluding it
  dropped the raw match count 6,091 → 4,299. Only curator-authored,
  mapping-independent labels are safe as evidence.
- **Bare-acronym lexical matches.** 789 of 2,958 subtype names are acronym-like.
  Matching on the bare acronym produces confident nonsense — `TBS` matched
  Townes-Brocks syndrome for a Temple-Baraitser subtype, `AD` matched Alzheimer
  disease for anauxetic dysplasia. Never propose a retarget from a synonym-only
  match on a bare acronym without a second signal.
