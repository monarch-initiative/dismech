# NAM Mining Research Template

## The single paper under study

- **Reference:** {reference}
- **Access:** {access}

{paper_summary}

**Confine the research to THIS paper's own findings.** Use other literature only to
judge validity or divergence, and when you do, cite it separately and say so. Do not
attribute another paper's result to this one.

## Goal

Decide, from this paper, **what each of its biological systems models, what it does
not, and how faithfully** — so that:

1. a mechanism knowledge base can link each system to the mechanism nodes it informs,
   with a relationship verb, a fidelity tier, the scale the system actually observes,
   and the translational caveats that must travel with each link; and
2. a method registry can hold each system as a method in its own right, with what it
   is used for and what it cannot show.

A system that supports no mechanism link is still a result. Say so plainly and give
the reason, rather than reaching for the nearest node.

## The biological systems, which must be kept separate in your answer

{systems}

Each system gets its own section. Do not merge them, and do not attribute a readout
taken in one system to another. Where one system is built from another (an organoid
grafted into an animal, a monoculture combined into a co-culture), the combination is
its own system and its readouts belong to it.

If the paper describes a system not listed above, add it with a note that it was not
in the brief. If a listed system turns out not to be in the paper, say so.

## The candidate mechanism nodes to test each system against

Report, for each system, which of these it bears on and how. Use these exact node
names:

{candidate_nodes}

**Anchors to avoid, and why:**

{anchors_to_avoid}

Do not select an anchor because its name resembles the paper's wording. A node is
right only if the paper's finding is the mechanism the node asserts. Where no listed
node fits a mechanism the paper does establish, report it under the gaps section
instead of forcing a link.

## What each pairing row must contain

Every (system → node) pairing you assert is one link object, and the definitions
below are that object's own, from the schema the answer has to land in. Fill each
field on its own terms: they are four different questions, not four chances to say
the same thing. In particular, note what the schema says about `limitations` and
`divergences` — the second is the typed form of the first, so a caveat belongs in
both as one account, not as two differently worded ones.

{link_slot_definitions}

### Also required on every pairing

- **a verbatim quote** — an exact substring of the paper that supports the pairing,
  with its PMID or DOI. Do not paraphrase. If a claim is supported only by the full
  text and not the abstract, say so. Never invent an identifier or a quote.
- **one line on why that relationship verb and not its neighbours.** The verbs are
  close together, and the reason you rejected the adjacent one is what a curator
  needs in order to check the choice.

A **FAILS_TO_RECAPITULATE** pairing is as valuable as a positive one, and so is a
**RESCUES** pairing where a system restores a node. Report both as first-class
findings rather than omitting them.

## What each system needs for a registry record

Separately from the pairings, and for every system whether or not it supports a
pairing, report:

- **what the system is** — its cells or organism, their species and source
  (pluripotent stem cell, adult tissue, cell line, primary cell, tumour tissue), its
  format, and the exposure or culture conditions that define it.
- **applications** — what the paper uses it to do, one entry per distinct use.
- **limitations** — what the system cannot show, in the paper's own terms where it
  states them.
- **characterization and validation readouts** — the assays run *on* the system.
  These are readouts, not systems of their own; keep them here rather than listing
  each as a model.
- **named variants** — where the paper describes variants of one protocol, say
  whether each is a variant of a single system or a system in its own right, and why.

## Specific claims from the paper to find, quote and verify

For each, give the exact supporting sentence and its location (abstract or full text):

{claims_to_verify}

## What the systems do NOT model

State these explicitly and attribute each to the right system:

{does_not_model}

Add any others the paper's own discussion or limitations section states. A caveat the
authors raise themselves is the most citable kind.

## Mechanisms with no candidate node

List every mechanism the paper establishes that none of the candidate nodes above
covers. For each: what the mechanism is, the quote establishing it, and what kind of
node would be needed to hold it. This list is the input to a knowledge-base gap
issue, so a mechanism omitted here is one that gets lost.

## Output

A structured report with:

1. One section per biological system, each containing its pairing rows as specified
   above, its registry-record fields, and a short "does not model" subsection.
2. A consolidated table of every pairing: system → node → relationship → fidelity →
   model_scale → readout direction → quote.
3. The mechanisms-with-no-node list.
4. An overall statement of which systems support a mechanism link and which do not,
   with the reason for each that does not.

Every factual claim carries a PMID or DOI and a verbatim quote.
