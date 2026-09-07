# Does a Rhea reaction corroborate the biomarker dismech already curates? (2026-09-07)

**Question.** The [coverage run](../2026-09-07-coverage/FINDINGS.md) established what
*fraction* of dismech's GO annotation Rhea can reach. It could not say whether a reached
reaction is the *right* one for the claim it sits on — a census measures availability, never
appropriateness. This run tests appropriateness on the one axis where dismech already holds
an independent answer.

It also produces the shortlist @AO33 asked for on
[#973](https://github.com/monarch-initiative/dismech/issues/973): *"a handful of 'simple'
cases (monogenic and bonafied pathway information that includes biomarker evidence)."* That
turns out to be a query, not a curation exercise.

Measurement only. No schema file, `kb/` entry, cache, or `conf/` adapter was changed.

## The test

For an inborn error of metabolism, the deficient enzyme's substrate is usually the diagnostic
biomarker. dismech records those two facts through **separate** curation paths:

- a `molecular_functions` GO term on a pathophysiology node, and
- a `biochemical:` biomarker bound to ChEBI.

Rhea knows each reaction's ChEBI participants. So the two can be cross-checked with no new
curation at all:

> Does the entry's curated biomarker appear among the ChEBI participants of the Rhea
> reaction that its curated molecular-function term maps to?

Rhea states participants at pH 7.3, so `chebi_pH7_3_mapping.tsv` reconciles protonation
forms — without it, a biomarker bound to the neutral species misses a participant bound to
the zwitterion. That Rhea publishes this file is itself evidence the mismatch is systematic.

Regenerate with:

```bash
python3 experiments/rhea_reaction_grounding/concordance.py
```

Inputs and their checksums are in [`MANIFEST.yaml`](MANIFEST.yaml). One input, the ~1 GB OAK
Rhea build, is pinned but not committed.

## Results

| | |
|---|---|
| Entries with **both** a Rhea-mappable MF term and a ChEBI-bound biomarker | **107** |
| …where ≥1 biomarker is a participant of the mapped reaction | **42 (39.3%)** |
| …of those, monogenic | **35** |

Full table, monogenic-first then most-corroborated, in [`candidates.tsv`](candidates.tsv).

### The shortlist (@AO33's "simple cases")

| Entry | Reactions | Biomarkers | Corroborated |
|---|---|---|---|
| Acute_Intermittent_Porphyria | 2 | 4 | **4** — ALA, porphobilinogen |
| Arginase_Deficiency | 1 | 5 | **3** — arginine, ornithine |
| Guanidinoacetate_Methyltransferase_Deficiency | 1 | 3 | **3** — guanidinoacetate, creatine |
| Asparagine_Synthetase_Deficiency | 1 | 2 | **2** — plasma and CSF asparagine |
| Inherited_Threoninemia | 1 | 2 | **2** — plasma and urinary threonine |
| Phenylketonuria | 1 | 3 | **2** — phenylalanine, tyrosine |
| Alkaptonuria | 1 | 1 | **1** — homogentisic acid |

All monogenic, all with one or two mapped reactions (so no ambiguity to resolve), all with
the biomarker already ChEBI-bound. **Taking pilot cases off the top of this table rather than
hand-picking them removes the "you chose the easy ones" objection**, and the query re-runs as
the KB grows.

## 39.3% is a partition, not a grade

The number is only useful if both outcomes are read correctly.

**Concordant (42)** — Rhea independently corroborates a link dismech asserts through two
separate curation acts. Nobody curated the reaction; the agreement is genuine external
corroboration, and it is the strongest evidence so far that reaction-level identifiers would
carry real information rather than decoration.

**Non-concordant (65)** — diagnostic, not failure. Three distinguishable causes, and the
distinction matters:

1. **The biomarker is genuinely downstream.** `3-Hydroxy-3-Methylglutaric_Aciduria` carries
   six biomarkers against one mapped reaction; organic acidurias are diagnosed on a panel of
   metabolites, most of them several steps from the deficient enzyme. Correct curation, and
   no reaction should match.
2. **The wrong reaction was reached.** Where a GO term maps to many reactions, the union of
   participants is broad and a miss suggests the mapping is too coarse to pin the claim.
3. **The ChEBI binding is worth a look.** A miss on a one-reaction entry whose biomarker
   should be a direct participant is a curation lead.

Separating those three requires reading the entries and is not automated here. **The check
improves the KB whether or not a `reactions:` slot is ever built** — which is the strongest
argument for running it regardless of how #973 is decided.

## Bearing on @cmungall's comment

> *"We use GO MF for representing the individual perturbed reactions. We could easily show
> these next to the MFs on the page, maybe include the reaction participants."*

This run is evidence that the render-time option is the better first move, and it needs no
schema change:

- For the **75%** of Rhea-reachable MF terms that map 1:1 (from the coverage run), the
  reaction and its participants are *derivable* from what is already curated. Storing a
  derivable value in YAML is denormalization; rendering it is not.
- The participants are exactly what makes the display worth having — they are the metabolites
  a clinician recognizes, and for 42 entries at least one of them is already the entry's own
  curated biomarker, so the page could mark the agreement.
- For the ambiguous quarter the renderer can show the reaction count instead of asserting a
  choice — the display degrades honestly where a slot would have forced a curator to pick.

> *"In practice we often just represent the affected function and the process ('shortcut'), as
> we don't need to duplicate pathway curation work."*

The non-concordant bucket is that shortcut made visible. A biomarker several steps from the
mapped reaction is precisely an entry where intermediate steps were skipped deliberately.
Read that way, concordance is a **shortcut detector**: it separates entries whose mechanism
is one reaction deep from those standing in for a longer chain — without anyone curating the
chain.

> *"I'd like to explore using metabolomics data with dismech to explore whether there might be
> modifier genes affecting pathways."*

The join this run performs — KB biomarker ChEBI ↔ Rhea participant ChEBI — is the same join
a metabolomics integration needs, since metabolomics panels report ChEBI-resolvable
metabolites. The 107-entry table is a ready-made starting set: entries where a measured
metabolite already connects to an enzyme dismech has curated.

## Limits

- **Disorders only.** `kb/disorders/*.yaml`; modules and comorbidities are not scanned.
- **Union over reactions, not per-reaction.** An entry with several mapped reactions is
  scored against the union of their participants, so a many-mapped entry finds a hit more
  easily. This inflates concordance for exactly the ambiguous terms the coverage run flagged.
  A per-reaction variant would be stricter and is the obvious refinement.
- **Presence, not direction.** The test asks whether the biomarker participates, not whether
  it accumulates or is depleted. dismech records direction (`presence: Elevated`); Rhea's
  undirected master reactions cannot corroborate it. Checking substrate-versus-product
  against `presence` is a real follow-up and would be a sharper metric.
- **Cause of a miss is not classified.** The three causes above are separated by hand.
- **Both ontologies drift.** ChEBI and Rhea release independently; the pH mapping is pinned,
  the OAK build is not versioned upstream.
