# SEPIO evidence model — experimental pilot

**Status: experimental.** Nothing here is required of curators, nothing existing has
changed, and this may be reverted. Tracking issue:
[#7439](https://github.com/monarch-initiative/dismech/issues/7439).

## What this is

An additive, partial implementation of the
[SEPIO](https://github.com/sepio-framework/sepio-linkml) (Scientific Evidence and
Provenance Information Ontology) evidence model, sitting alongside dismech's native
`EvidenceItem` model rather than replacing it.

The upstream SEPIO group drafted worked examples against dismech's own Cystic Fibrosis
entry — native form first, SEPIO form second — in
[`workspace/dismech-examples.yaml`](https://github.com/sepio-framework/sepio-linkml/blob/main/workspace/dismech-examples.yaml).
This pilot implements enough of that to run the round trip end to end: schema, snippet
validation, and rendering.

## The idea, in plain terms

A dismech evidence item is one flat object doing five jobs at once:

```yaml
evidence:
- reference: PMID:9922375          # where the words came from
  reference_title: "Structure and function of the CFTR chloride channel."
  supports: SUPPORT                # which way it cuts
  evidence_source: HUMAN_CLINICAL  # what kind of study it was
  snippet: "Dysfunction of CFTR causes the genetic disease cystic fibrosis."   # the words
  explanation: Review establishes CFTR as the channel whose loss causes CF.    # why we care
```

SEPIO separates the *information* from the *argument made with it*. A quoted sentence is
just a sentence; it only becomes evidence when someone interprets it as bearing on a
particular claim. So the structure grows a middle layer:

```yaml
has_evidence_lines:
- evidence_type: HUMAN_CLINICAL            # what kind of argument this is
  direction_of_evidence_provided: SUPPORT  # which way it cuts
  strength_of_evidence_provided: MODERATE  # how hard it cuts (new — see below)
  has_evidence_items:                      # the raw information being interpreted
  - data_type: TEXT_SPAN
    value: "Dysfunction of CFTR causes the genetic disease cystic fibrosis."
    reported_in:                           # where that information was published
      id: PMID:9922375
      document_type: REVIEW                # what kind of document (new)
      title: "Structure and function of the CFTR chloride channel."
  description: Review establishes CFTR as the channel whose loss causes CF.
```

Think of it the way an immunologist thinks about antigen versus epitope: the protein is
just a protein floating around until a receptor binds a particular patch of it and calls
it foreign. The snippet is the protein; the evidence line is the binding event that turns
it into a signal about a specific claim.

## What this buys us that the flat model can't say

Three things, and only three — this is not a general-purpose upgrade.

### 1. Grouping: several passages, one argument

Natively, two snippets supporting a claim are two sibling evidence items with no way to
say whether they are two independent arguments or one argument built from two sources.
An evidence line holds multiple evidence items, so the distinction becomes expressible.

The pilot's phenotype case is the worked example: a clinical review states that CF is
characterized by chronic endobronchial infection, and an Orphanet HPO annotation
independently records the same association at very-frequent. Neither is decisive alone;
the convergence is the argument. That is one line with two items, not two lines.

Contrast the CFTR Dysfunction case, where two snippets from the *same* paper say
different things — that CFTR is the channel, and what its domain architecture is. Same
paper, two arguments, two lines. Sharing a source does not make passages one argument,
and making different points does not make them separate arguments; the two axes are
genuinely independent and the flat model collapses them.

### 2. Document typing

dismech already weighs a primary study differently from a review differently from a row
out of Orphanet — curators do this in their heads constantly — but has had no slot to
record which is which. `Document.document_type` makes it explicit.

Note this is deliberately about the *document's editorial nature*, not about the study
design it reports. A review summarizing clinical trials is a `REVIEW` whose evidence line
is still typed `HUMAN_CLINICAL`. The two are separate facts and the model keeps them
separate.

### 3. Strength, separate from direction

`supports: SUPPORT` conflates "which way does this cut" with "how hard." SEPIO splits
them, so `direction_of_evidence_provided: SUPPORT` with
`strength_of_evidence_provided: WEAK` becomes sayable: *yes it points that way, no it
would not convince anyone on its own.*

This is the change most likely to matter downstream, and also the one most open to abuse.
`EvidenceStrengthEnum` is optional on purpose. **Omit it rather than guess.** A missing
strength means "no defensible call was made," which is honest; a fabricated `STRONG`
is worse than nothing.

## Mapping between the two forms

| Native `EvidenceItem` | SEPIO form | Notes |
|---|---|---|
| `reference` | `has_evidence_items[].reported_in.id` | same CURIE, same prefixes, same cache |
| `reference_title` | `has_evidence_items[].reported_in.title` | now actually validated — see below |
| `snippet` | `has_evidence_items[].value` | same exact-quote discipline, same validator |
| `supports` | `direction_of_evidence_provided` | **same enum**, deliberately |
| `evidence_source` | `evidence_type` | **same enum**, deliberately |
| `explanation` | `EvidenceLine.description` | |
| `images` | *(not mapped)* | out of scope for the pilot |
| — | `strength_of_evidence_provided` | new axis |
| — | `reported_in.document_type` | new axis |
| — | `data_type` | new; `TEXT_SPAN` for essentially all dismech evidence |

`direction_of_evidence_provided` reuses the existing `EvidenceItemSupportEnum` rather than
inventing a parallel SUPPORTS/DISPUTES/NEUTRAL vocabulary. That keeps the two forms
mechanically inter-convertible and means dismech's more specific members (`PARTIAL`,
`NO_EVIDENCE`, `WRONG_STATEMENT`) survive the trip instead of being flattened.

## Where it lives in the schema

`src/dismech/schema/dismech.yaml`:

- **Slot** `has_evidence_lines` — attached to `Pathophysiology`, `Phenotype`, and
  `MechanisticHypothesis` only, next to the existing `evidence` slot. 56 classes carry
  `evidence`; extending to the rest is mechanical and deliberately not done yet.
  `MechanisticHypothesis` is where the argument structure earns its keep most obviously —
  a `CANONICAL` / `ALTERNATIVE` / `EMERGING` status is a *summary of competing arguments*,
  which is exactly what evidence lines make explicit.
- **Classes** `EvidenceLine`, `DataItem`, `Document`.
- **Enums** `EvidenceStrengthEnum`, `DocumentTypeEnum`, `DataItemTypeEnum`.

The three classes declare their fields as class-local `attributes`, not global slots.
That is not a stylistic preference: SEPIO's field names collide head-on with existing
dismech slots that mean completely different things — `value` is a Qualifier filler,
`data_type` is a Dataset omics type, `id` is an ontology-term identifier. Class-local
attributes let the SEPIO vocabulary keep its own names without overloading any of them.

## Validation

Both validators handle the nested form, but for different reasons.

**`linkml-reference-validator` (upstream) works unchanged.** Its plugin already accepts a
reference field whose value is an *object* and reads `.id` and `.title` off it. Marking
`value` with `implements: [linkml:excerpt]` and `reported_in` with
`implements: [linkml:authoritative_reference]` is enough; snippet validation happens with
no upstream change at all.

**A side effect worth knowing about: the SEPIO form gets title checking the native form
silently skips.** The validator only checks a title when it can find one attached to the
reference. A bare `reference: ORPHA:586` string offers it nothing, so native
`reference_title` values are never verified. A `reported_in` Document *is* an object with
a title, so it gets checked — and it caught a wrong title on the very first run of this
pilot. That is a free correctness win, and also a warning: converting existing entries in
bulk will surface pre-existing title drift.

**`src/dismech/reference_snippet_audit.py` (ours) needed a change.** Its walker paired an
excerpt with a reference only when both were strings in the same object, so it walked
straight past every SEPIO evidence item and reported a confident zero for evidence it
never looked at — exactly the failure mode the audit exists to prevent (issue #7252). It
now extracts reference ids from objects too, mirroring upstream's `_extract_reference_id`.

Term validation is unaffected: the SEPIO classes bind no ontology terms.

## Rendering

`render_evidence_lines` in `src/dismech/templates/disorder.html.j2` is the sibling of the
existing `render_evidence` macro, wired into the pathophysiology and phenotype sections.
An evidence line renders as a container with its direction / type / strength badges, its
rationale, and its evidence items nested *inside* it — so the grouping described above is
visible on the page rather than only in the YAML.

Assertions with no `has_evidence_lines` render exactly as before; the macro emits nothing.

## The rendered examples

Three pages, each carrying **both** evidence forms on the same assertions so they can be
compared directly. Open the "Show evidence" and "Show SEPIO evidence" toggles side by
side. Each was picked to show something the others don't.

| Page | Attached to | What it shows |
|---|---|---|
| **[→ Cystic Fibrosis](../examples/sepio-pilot-Cystic_Fibrosis.html)** | pathophysiology, phenotype | The baseline mapping. One-to-one conversion; two quotes from one paper making two different points (two lines); two quotes from *different kinds of* document making one joint argument (one line, two items). |
| **[→ IgG4-Related Disease](../examples/sepio-pilot-IgG4-Related_Disease.html)** | mechanistic hypothesis | **Contested evidence.** Three arguments pointing three ways — SUPPORT from mouse and in vitro work, PARTIAL from human tissue, REFUTE from a phase 3 randomised trial — each carrying its own strength. The strongest argument on the page is the one against. |
| **[→ Timothy Syndrome](../examples/sepio-pilot-Timothy_Syndrome.html)** | mechanistic hypothesis | **An argument resting entirely on an animal model.** One line, `MODEL_ORGANISM`, `WEAK`, built from a premise plus a result in the same paper. Makes the existing "model-organism evidence must not be the sole support for a human claim" rule readable off the data. |

### Why these three

The Cystic Fibrosis page is the mapping proof: it shows the SEPIO form saying everything
the native form said, plus grouping and document typing.

The other two are the argument for the model actually being worth something.

**IgG4-RD** is a live dispute. Its `notes` field currently spends a paragraph of prose
adjudicating five references — *innate-first ordering is well supported but only in mouse,
the human data are correlational, B-cell depletion shows adaptive immunity is necessary,
therefore ALTERNATIVE not CANONICAL*. Natively the evidence block cannot carry any of
that: five siblings with differing `supports` values and no way to say which is heavier.
In SEPIO form the adjudication is structure — the refuting human trial is `STRONG`, the
supporting mouse work is `MODERATE`, the correlational human tissue is `WEAK` — and a
reader (or a query) can see why the status is what it is without parsing prose.

**Timothy Syndrome** is the opposite failure mode: an `EMERGING` hypothesis resting on a
single zebrafish paper, quoted twice. Natively those two quotes look like two independent
supports, because they are two sibling items with different `evidence_source` values. They
are in fact one syllogism — the biophysical premise plus the experiment — from one paper
in one species. One line, `WEAK`, says so. This matters more than usual here because this
hypothesis backs a computable EHR case-finding query
([hypothesis-based phenotype algorithms](../hypothesis-based-phenotype-algorithms.md));
when a query is going to be run against patient records on the strength of an argument,
being able to read that strength off the data is not cosmetic.

### About the snapshots

These are committed HTML, a deliberate exception to the repo's don't-commit-derived-HTML
rule: the pilot's argument is a visual one about structure and it does not survive being
described in prose. `just sepio-pilot` regenerates and re-copies all three, so `git diff`
after that recipe tells you whether a snapshot has drifted from its fixture.

Two caveats: the site-navigation links in each page's header point at `pages/…` paths that
do not exist under `docs/`, so they 404 — the evidence sections themselves are fully
functional. And these are static captures, not live pages.

## Trying it

```bash
just sepio-pilot          # validate (schema + terms + references) and render all fixtures,
                          # then refresh the committed snapshots
```

or piecewise:

```bash
just validate kb/experimental/Cystic_Fibrosis_SEPIO.yaml
just count-verified-snippets kb/experimental/Cystic_Fibrosis_SEPIO.yaml
uv run python -m dismech.render kb/experimental/Cystic_Fibrosis_SEPIO.yaml
# -> pages/disorders/Cystic_Fibrosis_SEPIO_evidence_pilot.html
```

The fixtures live in `kb/experimental/*_SEPIO.yaml`. Each carries **both** representations
of the same assertions, copied verbatim from the corresponding production entry — nothing
is newly curated and no new literature claims are introduced. They are fixtures, not
curation targets, and are deliberately outside `kb/disorders/`.

## What is deliberately left out

- **No SEPIO ids on evidence items.** They are inlined. Stable ids only start earning
  their keep when one evidence item is reused across assertions, which nothing here does.
- **No `Proposition` / `Statement` layer.** In SEPIO the thing evidence attaches to is a
  reified proposition. In dismech it is the pathograph node or edge itself. Reifying
  dismech assertions is a much larger change with consequences for the graph exports, and
  is not part of this.
- **No `targetProposition` on evidence lines.** The target is implicit in where the line
  is attached, exactly as native `evidence` works today.
- **No `EvidenceLine` nesting.** SEPIO allows evidence lines that take other evidence
  lines as input. Not modeled.
- **No migration and no converter.** Native `evidence` is untouched everywhere.
- **Enum values follow dismech's SCREAMING_SNAKE convention** (`TEXT_SPAN`), not the
  upstream example's `TextSpan`.

## Open questions for the SEPIO folks

1. **`explanation` → `EvidenceLine.description`.** The upstream example notes this is a
   reuse of a general-purpose field and that a dedicated rationale slot could be added.
   We agree — the curator's reasoning is a distinct thing from a description of the line,
   and overloading `description` will get confusing the moment a line needs both.
2. **Is `TextSpan` a `DataItem` subtype or a `data_type` value?** The example raises this.
   We used an enum value, on the grounds that dismech evidence is ~99% text spans and a
   class hierarchy would not earn its keep. If SEPIO makes it a class, we would follow.
3. **Strength vocabulary.** `STRONG`/`MODERATE`/`WEAK`/`VERY_WEAK` is our guess at a
   usable set. If SEPIO settles on a canonical strength value set we would rather adopt
   it than keep a local one.
4. **Structured-database sources.** dismech cites Orphanet, ClinGen, ICEES and NCIT rows
   as evidence alongside literature. We typed those `STRUCTURED_DATABASE` under
   `Document`, but a database row is arguably not a document at all. Is there a better
   SEPIO home for it?
