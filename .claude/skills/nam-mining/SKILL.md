---
name: nam-mining
description: >
  Take one paper, named by PMID or DOI, from an identifier to either a registry
  record or a committed deep-research spec and run. Use when asked to mine, mill
  or screen a NAM paper; when working a paper from the Complement-ARIE
  disease-paper corpus or the Toxicology NAMs special issue; when deciding
  whether a paper earns a full OpenScientist run or only a registry record; and
  when authoring a `templates/nam_mining/<slug>.yaml` spec. Covers the triage
  gate, which of the spec's fields can be derived and which cannot, how to find
  candidate mechanism anchors and the near-misses to warn a run away from, and
  the verification a returned report has to pass.
---

# NAM mining

One paper in, and one of three things out: a registry record, a spec plus a run,
or a recorded reason for neither. The deciding step is the triage gate below, and
it comes first because a full run costs about 16 minutes of provider time, a
provider call, and a curation pass afterwards. Most papers in the
Complement-ARIE corpus do not earn one.

What the user supplies is an identifier. Everything else in this procedure is
yours to derive, except the two judgements marked as theirs.

## The triage gate

**DisMech links a model to a mechanism node.** A method whose output is an apical
toxicity label, a dose metric, a classification, or an undifferentiated activity
call has no DisMech anchor by construction — however well established the method
is. That is the whole gate, and it is already the recorded position of
[projects/NAMS_SPECIAL_ISSUE.md](../../../projects/NAMS_SPECIAL_ISSUE.md), which
set five papers aside on exactly this ground, and of
[#16882](https://github.com/monarch-initiative/dismech/issues/16882).

Read the abstract and answer two questions in order.

**1. Does the paper assert a mechanism?** Not an endpoint, not a prediction, not
a potency ranking — a claim about what happens to a biological system and why.
Glutathione depletion is a mechanism. "Classified as a sensitizer" is not. A
benchmark dose is not. A QSAR's predicted NOAEL is not.

**2. If it does, is there a node that holds it?** Search the KB (see below).

| Mechanism asserted? | Node exists? | Outcome |
|---|---|---|
| No | — | **Registry only.** Write the record from the abstract. No run. |
| Yes | Yes | **Full run.** Author the spec and run it. |
| Yes | No | **Full run, gap-first.** The run's value is the gap it documents. Say so in the spec and open the gap issue from the result. |
| No method or model identifiable at all | — | **Set aside**, with the reason written down and whether the abstract alone decided it. |

Two rules this table must not be read against.

**A missing anchor never sets a paper aside.** It decides *where* the paper's NAMs
go, never whether they are kept. Every kind of method is a candidate for the
registry: in vitro, in silico, in chemico, bioanalytical, clinical,
epidemiological, animal, ecotoxicological. The only set-aside is "nothing to
extract at all" — an editorial, a policy piece, or a paper that cannot be
identified.

**Do not rule a model out of a mechanism before reading the evidence.** Several
models on one mechanism node is the point, not a duplication to avoid. A system
built from healthy donor lines can still carry mechanism evidence. State what the
evidence supports and put what it does not into `limitations`, `divergences` and
`fidelity`.

### Shapes already screened once — do not re-litigate these

The *Toxicology* round screened 25 papers and wrote up what it decided and what it
could not, in
[projects/NAMS_SPECIAL_ISSUE/open-questions.md](../../../projects/NAMS_SPECIAL_ISSUE/open-questions.md)
and thirteen per-paper rationales in the screening log. **Read the open questions
before triaging a paper that looks like any of these.** Each is a recurring shape,
not a one-off, and each already has an issue.

| Shape | Where it lands | Tracked as |
|---|---|---|
| Predicts or classifies a toxicity endpoint with no mechanism — read-across, QSAR/q-RASAR NOAEL, ML toxicity | Registry only; no DisMech anchor by construction | [#16882](https://github.com/monarch-initiative/dismech/issues/16882) |
| An IVIVE or PBPK dosimetry bridge | Registry only. It models exposure-to-internal-concentration, not a node; linking it to the mechanism the assay reads out would misstate what it computes | [#16887](https://github.com/monarch-initiative/dismech/issues/16887) |
| A docking or simulation run proposing a target with no wet confirmation | Unsettled, and the floor is the question. A model link asserts the model informs the node; a `KNOWLEDGE_GAP` discussion asserts something weaker and may be the honest record | [#16883](https://github.com/monarch-initiative/dismech/issues/16883) |
| Model-validation findings — normal mucociliary differentiation, rising barrier resistance, marker panels | No DisMech node, **by design**: DisMech models pathology and normal differentiation is not pathology. The registry row carries it, because it is the evidence the model is fit for purpose | [#16888](https://github.com/monarch-initiative/dismech/issues/16888) |
| A co-culture mixing species — a human line on a mouse feeder layer, a rabbit corneal line | Links are possible, but one `model_scale` and one `fidelity` cannot describe layers that differ in species, and a single `SPECIES_MISMATCH` loses which layer is affected | [#16889](https://github.com/monarch-initiative/dismech/issues/16889) |

A paper matching one of these does not need the gate re-derived. Cite the issue,
apply the decision, and if the paper genuinely pushes on the open part of the
question, say so in the spec and add the case to the issue rather than deciding
silently.

### Screen the registry's criteria first, DisMech's second

The *Toxicology* round ran one pass driven by DisMech's needs, and its own
conclusion was that this is the wrong order: "a screening pass driven from
dismech's needs will systematically under-nominate for the registry"
([#16882](https://github.com/monarch-initiative/dismech/issues/16882)). The
registry's inclusion criteria are strictly broader.

So ask the registry question first — *is this a method worth cataloguing?*, which
for a NAM paper is almost always yes — and the DisMech question second. The gate
above is written in that order for a reason: a "no" on the mechanism question
sends the paper to the registry, never to the bin.

### Access bounds the run, so check it during triage

No PMC full text means a run can only work from the abstract, cannot verify
pathway-level claims, and every snippet it returns must be an exact abstract
quote. For an abstract-only paper, prefer a registry record unless the abstract
itself carries the mechanism. Resolve this before authoring a spec, not after a
run comes back thin.

## Derive what can be derived

Two of the spec's eight fields come from metadata. Six need the paper read. None
of the six can be generated, which is why
[`scripts/nam_mining_vars.py`](../../../scripts/nam_mining_vars.py) collects them
by hand and refuses a spec that is missing one.

| Field | Source |
|---|---|
| `reference` | PubMed / Europe PMC metadata: PMID, DOI, PMC ID, journal, volume, pages, year |
| `access` | whether PMC full text exists, stated plainly |
| `paper_summary` | what kind of paper this is — a primary study, a methods review, a case study. Whether it studies a disease at all or only names one as motivation changes everything downstream |
| `systems` | one numbered entry per separable system |
| `candidate_nodes` | the KB search below |
| `anchors_to_avoid` | the near-misses from that same search |
| `claims_to_verify` | the findings worth quoting, with the paper's own numbers |
| `does_not_model` | per system; the authors' own caveats first |

The ninth variable, `link_slot_definitions`, is generated from the schema. Never
write it into a spec — `test_hand_written_and_generated_do_not_overlap` exists to
stop that.

### Cache the paper first

Cache it before drafting anything, so every quote in the spec and in the returned
report can be checked offline against `references_cache/PMID_<id>.md`. A run whose
quotes cannot be verified has to be redone.

## Finding the anchors, and the traps

Three commands, all offline, in this order:

```bash
just list-modules <substring>        # modules with every node anchor, as module#Node Name
just find-disorder <pattern>         # entries by name
grep -rl "<mechanism term>" kb/modules/ kb/disorders/
```

`just list-modules` is the one that matters: filtered by a substring it prints
each module with its nodes already in the `module_slug#Node Name` form a
`conforms_to` or a link target needs. Grep the paper's mechanism vocabulary — the
process, not the assay — across both directories, then read the candidates.

There is also `just embed-search "<query>" --space pathophysiology`, a semantic
search that would rank candidates better than grep. **It does not run in a stock
checkout:** it needs `uv sync --group embeddings`, and an index built with
`just embed-index`, which needs `OPENAI_API_KEY`. Do not reach for it mid-task
expecting it to work. Set it up deliberately or stay with the three commands
above.

**The near-misses are the product, not the noise.** A search returning ten hits
where three fit hands you the seven to warn the run away from. `anchors_to_avoid`
is the hardest field to author from scratch and a by-product of the search that
authors `candidate_nodes`. Record each one with the reason it does not fit, in the
spec, so the run cannot land there by name-matching.

Name-matching is the failure these runs actually produce. A module whose title
shares a word with the paper's wording, asserting a mechanism the paper never
measured. Real examples already recorded in the screening issues:

- `ciliopathy_dysfunction#Motile Cilia Beat Dysfunction` for a chemical that
  kills ciliated cells. The module is about inherited basal-body and axonemal
  defects; chemical loss of ciliated cells is a different claim.
- `retinoid_visual_cycle_disruption` for retinoic acid in a differentiation
  protocol. That is culture chemistry, not RPE retinoid recycling.
- `disabled_macroautophagy` for a stress-induced *increase* in autophagy. Read
  the module's description before linking; if it cannot hold an increase, record
  the gap instead.

**Every node name in a spec must resolve.** The template tells the run to use
exact node names, so a name that does not exist wastes the run. Check each one:

```bash
grep -n "^- name: <node>" kb/disorders/<Entry>.yaml
grep -rn "^- name: <node>" kb/modules/
```

A module anchor is written `module_slug#Node Name`. Confirm both halves.

### Choose the anchor *level* before the anchor

A model link lives in a disease entry or in a module, and the choice decides how
many entries the work reaches. Get this wrong toward the entry and the link
serves one disease when the mechanism it bears on is shared by a dozen.

Ask whether the node is shared:

```bash
grep -rl "<module_slug>#<Node Name>" kb/disorders/ | wc -l
```

More than one conforming entry means the mechanism is not that entry's own, and
the module is probably the right anchor. Seventeen modules already carry
`experimental_models:`, and they are mostly the NAM ones: the quadruple
co-culture liver spheroid went into four liver modules, the bronchial
tetraculture into `chemical_respiratory_allergy`. That is the established shape
for a NAM, not an exception.

**A module link is recorded once at the shared level; it is not inherited.**
Do not tell a reviewer that a module anchor makes the model visible to every
conforming entry, because it does not. `_annotate_model_links` builds the
"models informing this mechanism" back-link within one file, so a module's model
links draw on the module's own nodes and nowhere else. `Occupational_Asthma`
conforms to `chemical_respiratory_allergy`, that module holds two NAM models,
and the disorder file names neither. The module page lists its conforming
diseases, so the model is reachable *from* the module; nothing walks the other
way.

What the module anchor buys is therefore placement, not propagation: one record
of the model at the level its mechanism actually lives at, instead of the same
system re-described in each entry that could claim it. That the sharing is not
surfaced is a real gap, and part of the argument for
[#17015](https://github.com/monarch-initiative/dismech/issues/17015).

The test is what the model is specific *to*. A patient-derived or
genotype-corrected system is about that genotype and belongs on the entry. A
system built from healthy donor lines, or an exposure model, is usually about the
cell population and the process, which is the module. The hiPSC midbrain organoid
grafted into a 6-OHDA mouse carries no PD genotype at all, and fifteen entries
conform to `parkinsonism_dopaminergic_degeneration` — so an entry-level link
there privileges one disease over fourteen others with equal claim.

**Why this is a convention and not yet a structure.** Models are inlined in
disease entries today, which is why the module anchor is the only sharing
mechanism available. [#17015](https://github.com/monarch-initiative/dismech/issues/17015)
proposes a first-class `kb/models/` split into computational, experimental and
animal, for exactly this reason — "models are shared between diseases" — and
names the NAM registry as one of the registries it would formalize. Until that
lands, prefer the module: a module-level link is the closer approximation of a
shared model, so it is the choice that survives the migration.

Meanwhile the registry already *is* the cross-entry home for the method. The
registry record describes the system once, for every disease it ever serves; the
DisMech link asserts what it says about one mechanism. A genotype-agnostic model
should therefore end up as one registry record plus a module link, not as the
same system re-described in several entries.

**Read a module's own scope before conforming to it.** Several modules declare a
scope narrower than their title suggests — `epithelial_barrier_dysfunction` frames
itself around the allergic and type 2 barrier hypothesis, so a chemical irritant
may sit outside it. This question came up in two sibling issues independently;
decide it once and write the decision down.

## The procedure

1. **Triage** against the gate. If the answer is registry-only or set-aside, stop
   here, record the decision and its reason, and report it. Do not author a spec.
2. **Cache** the paper.
3. **Read** it. The abstract if that is all there is; the full text when there is
   one, and say which the spec's claims came from.
4. **Search** the KB with `just list-modules` and grep for anchors and their
   near-misses. Verify every node name resolves, and **settle the anchor level
   first** — count the conforming entries before deciding an entry node is the
   right target.
5. **Author** `templates/nam_mining/<slug>.yaml`. Slug is
   `<first_author>_<year>_<short_subject>`, as in `zheng_2023_hmo_graft`. `entry`
   is where the run's output will land; say in the spec when the real anchor is a
   module and how many entries conform to it, so the reviewer sees the reach of
   the link rather than inferring it.
6. **Preview** the prompt, which costs nothing:
   `just nam-mining-prompt <slug>`
7. **Stop and show the user the spec and the triage decision.** These are
   theirs: whether the paper earns a run, and whether the candidate nodes are the
   right ones. Do not start a run without that.
8. **Run** on approval: `just nam-mining openscientist <slug>`.
9. **Verify** the report before curating from it. Every verbatim quote has to be a
   genuine substring of the cached text. Check them yourself rather than trusting
   the report's own validation, which resolves identifiers and does not confirm
   that a quote says what it was attached to.
10. **Report** what the run produced, including its negatives and the mechanisms
    it found no node for. Those become gap issues; a mechanism dropped here is
    lost.

## What the run cannot be asked to settle

A returned report is a lead, not a curation decision. Three things stay with a
human and must be surfaced rather than resolved in the spec:

- **Granularity.** A single NAM with several endpoints is one record; a variant
  of a protocol that looks like its own system may be two. If a variant differs
  enough to look separable, say so rather than deciding silently.
- **Destination.** A paper can belong in the registry with no DisMech home. Say
  which, and why, per system.
- **A new schema property.** A record the schema cannot hold is still written and
  parked, not discarded. Open the schema issue and keep the record.

## Related skills

- `dismech-references` for the caching, snippet and quote machinery, and for the
  Named Entity Confusion preflight.
- `dismech-terms` when a record needs an ontology binding.
- `ker-evidence-triage` for the same prioritization question applied to AOP-Wiki
  Key Event Relationships, and `mie-ker-capture` for turning Key Events into
  edges. Both are the AOP-side analogue of this skill.
- `github-communication` before posting the triage decision or a gap issue.
