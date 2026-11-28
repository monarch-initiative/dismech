# Module review

**Question.** Is each mechanism module in `kb/modules/` logically correct,
biologically useful, and coherent, both on its own and next to its sibling
modules?

Every other check on a module is mechanical: the schema validates, the terms
exist, the snippets are exact quotes, the causal targets resolve. None of them
asks whether the causal chain is right, whether the module earns its place, or
whether two modules describe one mechanism twice. This experiment is that
reading, done by a reviewer per thematic batch, at a pinned commit, to a fixed
rubric, with findings recorded in a format a script can tally.

A run reviews; it does not repair. Nothing under `kb/` is edited.

## Layout

| Path | What it is |
|---|---|
| `build_facts.py` | Computes the fact sheets: graph shape, bound terms, conformers, sibling candidates. No judgement. |
| `validate_findings.py` | Checks a findings file against the contract below. Reviewers run it before every commit. |
| `aggregate.py` | Tallies all findings files of a run into `FINDINGS.md` and a per-module appendix. |
| `<run>/batches.yaml` | Which modules each batch holds. A partition of `kb/modules/`. |
| `<run>/facts/<batch>.md` | Fact sheets for one batch. Start here. |
| `<run>/findings/<batch>.json` | One reviewer's output. |
| `<run>/FINDINGS.md` | What the run found, how, and the limits of the measurement. |

| Run | Commit reviewed | Batches |
|---|---|---|
| [`2026-11-28/`](2026-11-28/) | `247139d3a` | 26 |

## What a reviewer does

You are given one batch id. Work through these steps yourself, in order.

1. Read this file to the end, then `<run>/facts/<batch>.md`.
2. Read `docs/primers/modules-and-conformance.md` and
   `.claude/skills/create-module/SKILL.md`. They define what a module is for
   and the bar it has to clear. In `CLAUDE.md`, the sections *Mechanism
   Modules*, *Pathograph Targets Are Bare Names*, *Gain/Loss of Function: which
   slot?* and *Logical Rules* state conventions you will otherwise mistake for
   defects.
3. For each module in the batch, read the whole file. Do not review from the
   fact sheet alone; it lists structure, not meaning.
4. For each module, read enough of its surroundings to judge it:
   - the `description` and `notes` of every sibling the fact sheet names
     (`just list-modules <stem>` prints both in full), and the sibling's nodes
     where scopes look close;
   - two to four conforming nodes, chosen to include the most-used module node
     and, where the fact sheet shows `process_absent` or `cell_type_absent` on
     many links, some of those (`rg -n -B2 -A40 "conforms_to:.*<stem>#" kb/disorders`);
   - the cached abstract (`references_cache/PMID_<id>.md`) behind any claim you
     doubt.
5. Record a verdict and findings for every module, then the cross-module
   findings for the batch.
6. Validate, commit only your findings file, push. Do this after every three or
   four modules, not only at the end, so that a session that dies loses little.

Do the reading in your own context. Sibling overlap and contradiction are only
visible to a reviewer holding several modules at once, so do not hand modules
out to subagents.

### The four things being judged

**Logical correctness.** Is the causal model, as encoded, valid?

- Does every edge run from cause to effect? Look for reversed edges, and for
  edges that record co-occurrence or temporal order as causation.
- Does each edge follow from its two nodes without a missing step? An edge that
  needs an unstated intermediate is a leap.
- Is every cycle a real feedback loop that the text describes as one?
- Do the roots look like initiating events and the leaves like consequences? Is
  any node unreachable, isolated, or pointed at nothing?
- Does each node's `role` match where it sits in the graph? Is there one key
  conformance target, and is it the node the `description` says it is?
- Does each `modifier` agree with the node's claim? A node about loss of a
  function that marks that function `INCREASED` is wrong, as is a chain whose
  modifiers contradict each other.
- Do the bound terms denote what the node says? Check the cell type against the
  process, the process against the claim, and a term for normal development
  against a pathological event.
- Is each node one claim? A node that needs two roles, two scales or two
  unrelated processes is two nodes.
- For each treatment: does `target_mechanisms` point at the node the drug acts
  on, and is `treatment_effect` the right direction?
- Do `hypothesis_groups` on edges name defined hypotheses, and is a contested
  mechanism presented as contested?
- Do the `description`, `notes`, node descriptions and edges tell the same
  story? Count the nodes and edges the description names against the file.
- Does the quoted evidence support the specific node or edge it sits on? A true
  sentence about a neighbouring claim, another species, or the opposite
  direction is a mismatch.

**Biological correctness.** Is what the module says true?

- Is each mechanistic statement consistent with established biology? Where you
  doubt one, check a source before recording it.
- Is a finding from one disease, tissue or species stated as general?
- Is a superseded model presented as current, or a debated one as settled?
- Is a step missing that an expert would call essential, so that the chain as
  written misleads?

**Biological utility.** Does the module earn its place?

- Is this one conserved mechanism with a short chain and a rate-limiting node
  that conformers funnel through? Or is it a single disease's pathophysiology,
  a drug monograph, or an umbrella over unrelated routes to one label (which is
  a `Grouping`)?
- Is it used? Read the conformer counts per node. A module nobody conforms to
  has unproven utility; one whose conformers all cite the same node may only
  need that node; one whose conformers rarely share its terms is anchored too
  generically or cited as a label.
- Can conformance be checked against it? A key node that binds no GO process or
  cell type gives a conformer nothing to be compared with.
- Is the grain right: generic enough to be reused, specific enough to say
  something a conformer could get wrong?
- Would a curator choosing a conformance target find the right node from the
  `description` alone?

**Coherence.** Does it hang together, alone and among its siblings?

- Do the name, description, nodes and `module_categories` describe the same
  thing at the same scope?
- Does it overlap a sibling module? If two modules model one mechanism, do they
  agree, and does each say how it differs from the other? Is the complementarity
  the description claims real?
- Do two modules contradict each other about the same biology?
- Where would a conformer go that fits both? Is the boundary stated?
- Is a node an instance of another module's node without saying so?
- Is membership of a `kb/module_collections/` record consistent with the
  framework it names?

### What is not a finding

- **A module binding no CHEBI or MONDO term in a node.** Module nodes bind GO
  and CL (plus UBERON locations) by convention; chemistry is prose.
- **A conformer that does not share the module's GO term** (`process_absent`).
  Binding the specific process where the module binds the generic one is what
  conformance asks for. It is a lead about the module only when most conformers
  diverge.
- **`INCREASED` where you would have written `GAIN_OF_FUNCTION`**, unless the
  claim really is that the process has left normal regulatory control.
- **Edges without their own evidence.** Most module edges carry none; evidence
  sits on the nodes. Record it only where an edge makes a claim neither node's
  evidence covers.
- **An edge that runs against role order when it is a described feedback loop.**
- **Duplicated content between a module and its conformers.** Conformance is a
  consistency check, not inheritance.
- **`evidence_source: OTHER` on a review**, lowercase `hgnc:`, and the other
  conventions `CLAUDE.md` documents.
- **Style.** Record wording only where it changes what a reader would conclude.

A module with no findings is a legitimate and useful result. Do not pad.

### Severity, confidence, verification

| Severity | Meaning |
|---|---|
| `HIGH` | A reader would come away with something false, or the module's reason to exist fails: a reversed or invalid causal edge, a wrong-direction modifier, a term that changes the node's meaning, evidence that contradicts its claim, a factual error in the core mechanism, a module that duplicates another or is not one mechanism. |
| `MEDIUM` | A real defect that weakens the module without inverting it: an edge that needs a missing step, an over-general claim, a key node nothing can be checked against, an unacknowledged overlap, evidence that does not reach the claim it is attached to. |
| `LOW` | Worth a curator's minute and no more: a better term exists, a role label is off, the description has drifted from the nodes. At most five per module. |

`confidence` is yours in the finding, not in the module: `HIGH` when you
checked it against the file and a source, `MEDIUM` when it rests on the file
plus knowledge you did not look up, `LOW` when it is a question a domain expert
should answer. A low-confidence finding is worth recording; say that it is one.

`verification` says what you did: which cached abstract you read, which
ontology definition you fetched, which conformers you opened, or that it is
unverified reasoning. Three rules:

- **Re-read before recording.** Before a `HIGH` finding goes in, open the lines
  again and confirm they say what you think they say. Folded YAML scalars and
  long node lists make misreadings easy.
- **Look identifiers up.** Never write an ontology CURIE, label or PMID from
  memory, in a problem statement or a suggestion. Look it up in the same step
  (`cache/<prefix>/terms.csv`, or
  `curl -s "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0006954"`),
  and if you could not, say the suggestion is unverified. An agent's recalled
  CURIE is fluent and frequently wrong.
- **Quote the file.** `quote` is an exact span of the module file (any length
  that pins the place down; whitespace is normalised before comparing). The
  validator rejects a quote that is not in the file. Use `null` only for a
  finding about something absent.

## The findings file

`<run>/findings/<batch>.json`:

```json
{
  "batch": "B15",
  "reviewer": "the id of the reviewing session",
  "reviewed_commit": "247139d3a",
  "modules": [
    {
      "module": "gout_urate_crystal_inflammation",
      "verdict": "MINOR_ISSUES",
      "scores": {"logic": 4, "biology": 5, "utility": 4, "coherence": 3},
      "summary": "Two to four sentences: what the module models, whether the chain holds, what most needs attention.",
      "strengths": ["Short, specific; optional"],
      "findings": [
        {
          "id": "gout_urate_crystal_inflammation-01",
          "severity": "MEDIUM",
          "dimension": "COHERENCE",
          "category": "SIBLING_OVERLAP",
          "location": "pathophysiology[NLRP3 Inflammasome Activation]",
          "quote": "engage the caspase-1-activating NLRP3 inflammasome",
          "problem": "What is wrong, with the reasoning.",
          "suggestion": "The concrete change you would make.",
          "confidence": "HIGH",
          "verification": "Read nlrp3_inflammasome_activation in full; compared node terms.",
          "related_modules": ["nlrp3_inflammasome_activation"]
        }
      ],
      "evidence_spot_checks": 6,
      "conformers_read": ["Gout#NLRP3 Inflammasome Activation"]
    }
  ],
  "cross_module_findings": [
    {
      "id": "B15-X01",
      "severity": "MEDIUM",
      "category": "OVERLAP",
      "modules": ["cytokine_storm_hyperinflammation", "il6_hypercytokinemia"],
      "problem": "What the two modules say, and where they collide or duplicate.",
      "suggestion": "Merge, split, cross-reference, or redraw the boundary: say which.",
      "confidence": "MEDIUM",
      "verification": "Read both files in full."
    }
  ],
  "limitations": "What you could not check, and anything about the batch a reader of the tally should know."
}
```

- `verdict`: `SOUND` (no `HIGH` or `MEDIUM` finding), `MINOR_ISSUES` (no
  `HIGH`; the chain stands), `MAJOR_ISSUES` (at least one `HIGH`; the chain
  needs repair but the module concept stands), `RESTRUCTURE` (the concept is
  the problem: split, merge, demote to a single entry, or replace with a
  grouping).
- `scores`: 1 to 5 per dimension. 5 nothing found, 4 minor, 3 real issues,
  2 major, 1 wrong at the root. They are for ranking across 242 modules, so use
  the whole range.
- `dimension`: `LOGIC`, `BIOLOGY`, `UTILITY` or `COHERENCE`.
- `category`: prefer one of these, or write your own in the same style.
  LOGIC: `EDGE_DIRECTION`, `EDGE_LEAP`, `DANGLING_TARGET`, `UNEXPLAINED_CYCLE`,
  `ORPHAN_NODE`, `ROLE_MISMATCH`, `MODIFIER_DIRECTION`, `TERM_CLAIM_MISMATCH`,
  `NODE_BUNDLING`, `TREATMENT_LOGIC`, `HYPOTHESIS_LOGIC`,
  `INTERNAL_CONTRADICTION`, `EVIDENCE_CLAIM_MISMATCH`.
  BIOLOGY: `FACTUAL_ERROR`, `OVERGENERALIZATION`, `OUTDATED`,
  `SPECIES_EXTRAPOLATION`, `MISSING_KEY_STEP`, `WRONG_CELL_OR_SITE`.
  UTILITY: `FAILS_MODULE_BAR`, `SINGLE_DISEASE`, `HETEROGENEOUS_UMBRELLA`,
  `NO_CONFORMERS`, `UNUSED_NODES`, `UNANCHORED_KEY_NODE`, `TOO_GENERIC_ANCHOR`,
  `GRANULARITY`, `DESCRIPTION_INSUFFICIENT`.
  COHERENCE: `NAME_SCOPE_MISMATCH`, `DESCRIPTION_NODE_MISMATCH`,
  `SIBLING_OVERLAP`, `SIBLING_CONTRADICTION`, `BOUNDARY_UNCLEAR`,
  `CATEGORY_PILL`, `COLLECTION_MEMBERSHIP`.
- A cross-module `category` is one of `OVERLAP`, `CONTRADICTION`, `BOUNDARY`,
  `GRANULARITY`, `NAMING`, `COLLECTION`, `MISSING_LINK`, `OTHER`. Record a
  cross-module finding once, there, and cite it from the per-module findings
  only if a module needs its own change. `modules` may name a module outside
  your batch.

```bash
uv run python experiments/module_review/validate_findings.py experiments/module_review/2026-11-28 B15            # complete batch
uv run python experiments/module_review/validate_findings.py experiments/module_review/2026-11-28 B15 --partial  # work in progress
```

## Reading a fact sheet

Each module's sheet gives, in order: the file and its size; category pills and
collections; sections beyond the node chain; the graph (nodes, edges, how many
edges carry their own evidence, roles); roots and leaves; then one line for each
structural oddity that is present, and nothing for the ones that are not.
`conformers` counts `conforms_to` links into the module and the files they come
from. `siblings` lists modules this file names, modules that name it, the
modules sharing most ontology terms (Jaccard over all bound term ids), and the
modules most often conformed to by the same files. Those four lists are where
to look for overlap; none of them says the overlap is a problem.

Under each node: its role, scale and class, how many evidence items it carries,
how many conformer links point at it, and `conformance_content`, the counts from
`just check-conformance-content` for links into that node (`process_absent`,
`anchor_no_process`, `cell_type_absent`, `edges_absent`). Then the bound terms
with their modifiers, each outgoing edge, and up to five conformers.

On an edge, `!DANGLING` means the target is not a node or phenotype in the
file, and `->phenotypes` that it resolves to a phenotype of the same file.

## Limits

The reviewer is a language model. Its biological judgement is not an expert
panel's, and it produces confident findings that are wrong. The contract above
is built around that: quotes are checked against the file, identifiers have to
be looked up, and every finding carries its own confidence and what was done to
check it. A finding is a lead for a curator to confirm, in the same way the
repository treats a term suggested by a deep-research report.

One reviewer reads each module once. Nothing here measures agreement between
reviewers, so the absence of a finding is weak evidence that a module is sound.
