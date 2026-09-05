# Coarse phenotype bindings

A phenotype bound to `HP:0000478` *Abnormality of the eye* validates, renders,
exports, and lands in the right browser facet — while saying almost nothing.
`Schaaf-Yang_Syndrome` named strabismus, esotropia and myopia in its
`description` and then discarded all three in the binding.

Usually that is a curator who stopped early. But three legitimate reasons for a
coarse binding exist, and the knowledge base already carried all three written as
prose that nothing could read. This page describes the slot that records which
one applies, and the guard that requires it.

The rule is **not** "prefer narrow terms". Manufacturing a specificity the source
does not support is a worse defect than a coarse binding, and the
[ontology term contract](../CLAUDE.md) forbids it outright. The rule is that a
coarse binding must say *why* it is coarse, which leaves the unexplained one as
the only thing that fails.

## What counts as coarse

The 23 direct children of `HP:0000118`, taken from the `meaning:` values of
`PhenotypeCategoryEnum` in `src/dismech/schema/classifications/phenotype_category.yaml`.
That is the same list the browser's *Phenotype Systems* facet is built from, so
there is one vocabulary rather than two, and `just validate-terms-schema` already
verifies its labels. A term in that set names a facet bucket; it cannot name a
finding.

There is deliberately no depth rule and no information-content metric. Depth is a
property of how HPO happens to be built, not of the claim:

| Term | Uses in `kb/` | Coarse? |
|---|---|---|
| `HP:0004322` Short stature | 290 | **No.** It is exactly as specific as the literature ever gets. |
| `HP:0001999` Abnormal facial shape | 178 | **No.** "Dysmorphic facies" is a real summary finding. |
| `HP:0001627` Abnormal heart morphology | 150 | **No.** It carries "Congenital heart defect" as an EXACT synonym, and *is* the concept when a paper says CHD. |
| `HP:0000478` Abnormality of the eye | 36 | **Yes.** |

Any metric that ranked the first three as vague would push curators into
asserting lesions their sources never named. Widening the set is a schema pull
request with an argument attached, not a threshold.

## The slot

`coarse_binding_basis` lives on `PhenotypeDescriptor`, so it sits next to the
`term:` it qualifies and is inherited by imaging findings and trial targets:

```yaml
phenotype_term:
  preferred_term: Eye abnormality
  term:
    id: HP:0000478
    label: Abnormality of the eye
  coarse_binding_basis: SPECTRUM_SUMMARY
```

Each value carries a requirement, checked wherever the value appears.

### `SPECTRUM_SUMMARY`

Many distinct findings, variable between patients, where one summary phenotype is
the honest grain. Record the constituents in `spectrum_terms` rather than leaving
them in prose. They carry HP terms but no frequency and no evidence of their own,
because the summary phenotype's evidence covers them — so the spectrum costs a
term lookup, not a fully curated phenotype per finding.

```yaml
  phenotype_term:
    preferred_term: Eye abnormality
    term:
      id: HP:0000478
      label: Abnormality of the eye
    coarse_binding_basis: SPECTRUM_SUMMARY
    spectrum_terms:
    - preferred_term: strabismus
      term:
        id: HP:0000486
        label: Strabismus
    - preferred_term: esotropia
      term:
        id: HP:0000565
        label: Esotropia
    - preferred_term: myopia
      term:
        id: HP:0000545
        label: Myopia
  frequency: FREQUENT
```

At least two constituents are required, none may itself be coarse, and none may
repeat the summary term. These terms **are** term-validated: `spectrum_terms` has
range `PhenotypeDescriptor`, whose `term` is enum-bound, so a fabricated label
there fails `just validate-terms` — unlike a term hidden in `qualifiers`.

Use a first-class `phenotypes` entry instead whenever a finding has its own
frequency or evidence. The spectrum list is for findings the source bundles.

Worked example: `Schaaf-Yang_Syndrome`, whose cited snippet reads "eye
abnormalities in the form of strabismus, esotropia, or myopia" — the three
constituents come from the quote itself.

### `SOURCE_UNSPECIFIED`

The cited source characterizes the finding no further, so a narrower term would
assert something the evidence does not. No companion slot: the evidence snippet
is the proof.

Worked example: `PAICS_Deficiency`, whose description already said "the specific
ocular finding is not characterized in the available abstract, so the binding is
deliberately at the general level".

This is the value for the case `PUS3-Related_Neurodevelopmental_Disorder` argues
at length in prose — a source saying only "congenital heart defect" with no named
lesion. Note that entry does not need the slot, because `HP:0001627` is not in
the coarse set; it is the pattern, not an instance.

### `NO_HPO_TERM`

The claim is narrower than any available HPO term and the coarse parent is the
best honest anchor. `preferred_term` must differ from the bound label — otherwise
nothing narrower was actually claimed and the value is wrong. Record what you
searched in `term_gap`, so a permanent gap becomes a term request rather than
folklore.

```yaml
  phenotype_term:
    preferred_term: Multiple primary malignant neoplasms
    term:
      id: HP:0002664
      label: Neoplasm
    coarse_binding_basis: NO_HPO_TERM
    term_gap: >-
      HPO has no term for neoplasm multiplicity as such. Searches of "multiple
      primary", "metachronous" and "second primary malignancy" return nothing;
      the closest descendants are anatomically restricted (see notes).
```

Worked example: `Li-Fraumeni_Syndrome`. Multiplicity of primaries is the
characteristic feature of the syndrome and HPO has no term for it; the closest
descendants (`HP:0007606` Multiple cutaneous malignancies, `HP:0033714` Multiple
meningiomas) are anatomically restricted.

### `PATHOGRAPH_HUB`

A deliberately unqualified convergence point in the causal graph: a mechanism
disrupts a system, and the system-level disruption is where several specific
findings converge. It carries no clinical claim of its own, so it takes no
`frequency`, and at least one causal edge in the same entry must target it.

```yaml
pathophysiology:
- name: CREBBP haploinsufficiency
  downstream:
  - target: Ocular abnormalities        # bare name, per the pathograph rule
    causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES

phenotypes:
- name: Ocular abnormalities
  phenotype_term:
    preferred_term: Ocular abnormalities
    term:
      id: HP:0000478
      label: Abnormality of the eye
    coarse_binding_basis: PATHOGRAPH_HUB
```

Worked example: `Rubinstein-Taybi_Syndrome`.

Two things about hubs are easy to get wrong.

**A hub is defined by its incoming edges, not its outgoing ones.** An early draft
of this design required outgoing `sequelae` into the specific findings. That is
wrong: `sequelae` is a `CausalEdge`, and a coloboma is not *caused by* an eye
abnormality — it *is* one. Requiring those edges would have had curators drawing
an is-a hierarchy as a causal chain to satisfy a guard, corrupting the graph. If
a hub's constituents are worth naming, put them in `spectrum_terms`, which
asserts no causation. Outgoing `sequelae` remain fine where they are genuinely
causal.

**A hub is not a "disruption of eye development" node.** That node belongs in
`pathophysiology`, binds GO (`GO:0001654` with a `modifier:`), and asserts a
*process*. A hub is a phenotype, binds HP, and asserts a system-level *outcome*.
The two can sit in sequence, and should not be merged. Do not add an HP slot to
`Pathophysiology` to accommodate hubs. Watch the flat node namespace too: a hub
and a pathophysiology node sharing one name collapse into a single graph node
([#9896](https://github.com/monarch-initiative/dismech/issues/9896)), so phrase
hub names as outcomes rather than processes.

**A hub with a frequency is a `SPECTRUM_SUMMARY`.** Frequency is a claim about
patients, and a hub makes none.

## The guard

```bash
just check-coarse-phenotypes                              # gate, whole KB
just check-coarse-phenotypes kb/disorders/MyDisease.yaml
just list-coarse-phenotypes                               # census, exit 0
just update-coarse-phenotype-baseline                     # only ever to shrink
```

Offline, ungated by changed paths, and part of `just qc` — for the same reason
`check-entity-refs` and `check-causal-targets` are: CI selects pytest by changed
path, and a curation PR touches only `kb/`, matching neither the `python` nor the
`schema` filter. The checks written to protect knowledge-base content are exactly
the ones a content-only PR skips.

The 164 bindings that predate the slot are grandfathered in
`tests/coarse_phenotype_baseline.txt`. **That file may only shrink.** Clearing a
row means a curator decided between the four values, or bound a specific term
instead. A companion-rule violation is never grandfathered, because a declared
basis can only come from content written after the slot existed.

Companion rules apply wherever a basis is declared, including on terms outside
the coarse set. That is deliberate: it lets a curator declare a basis on a
second-tier term such as `HP:0000924` *Abnormality of the skeletal system*
before anyone decides whether to widen the subset, without the declaration going
unchecked.

## Burning down the backlog

The census sorts the remaining work by term:

```bash
just list-coarse-phenotypes | head -30
```

`HP:0002664` Neoplasm (47) and `HP:0000478` Abnormality of the eye (36) are half
of it. Neoplasm is the best place to start: in cancer-predisposition entries the
specific tumour types are usually already curated as sibling phenotypes, so the
decision is `SPECTRUM_SUMMARY` versus `PATHOGRAPH_HUB` rather than new research.

Do not clear a row by picking a narrower term the source does not support. If
none of the four values fits and no specific term is defensible, leave the row
and say so in the pull request.

## Deliberately out of scope

- **GO and `biological_processes`.** The same design would work — a closed
  coarse set, one basis slot — and GO ships its own `goslim_*` subsets as a
  starting list. Nothing here is HP-specific except the vocabulary. Not now.
- **The second tier.** `HP:0000924`, `HP:0012372`/`HP:0012373`,
  `HP:0012638`/`HP:0012639` and the other organisational split terms are
  candidates, but the tier is not uniform (see the table above), so it would
  have to be enumerated by hand and lived with. Deferred.
- **`phenotypes.category`.** The open register item about binding
  `PhenotypeCategoryEnum` to that free-text slot is independent; this guard only
  reads the enum's `meaning:` values.

Background: [the design brainstorm](superpowers/specs/2026-09-05-coarse-hpo-bindings-brainstorm.md).
