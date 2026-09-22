# Entity references and pathograph targets

### Entity References Are Foreign Keys

`attaches_to` — and the `would_support`, `would_refute`, and
perturbation/readout `target` slots that reuse its grammar — point at another
object in the same entry:

```
[<file>:]<kind>#<name>

pathophysiology#Amyloid Plaque Formation
phenotypes#Memory Loss
Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation
```

`check_entity_ref_foreign_keys` enforces these references across disorders,
modules, and comorbidities. Renaming or splitting a node is the common way to
break them, so search the file for the old name before committing.

Resolution lives in `src/dismech/entity_refs.py`; its `SECTION_KEYS` mapping is
the source of truth shared by validation and rendering. Important exceptions:

| Prefix | Resolves against |
|---|---|
| `disease#` | the entry's top-level `name` |
| `mechanistic_hypotheses#` | `hypothesis_group_id` or `hypothesis_label` |
| `prevalence#` | `population`; similarly `progression#` uses `phase`, `datasets#` uses `accession`, and `animal_models#` uses `species` |

`<kind>` is the schema slot name of the section — `phenotypes#`, not
`phenotype#`; `treatments#`, not `treatment#`; `has_subtypes#`, not `subtype#`.
The singular aliases still resolve and an entry carrying one is not a defect,
but `kb/` was normalised to the slot-name form (#9394) so the prefix is
derivable from the schema and `phenotypes#` greps every phenotype reference;
`check_entity_ref_prefixes_are_schema_slot_names` keeps it that way. Cross-file
references and prefixes absent from `SECTION_KEYS` are skipped rather than
failed; add a missing prefix to `SECTION_KEYS` instead of working around it.

An empty anchor names a whole section:

```yaml
attaches_to:
- clinical_burden#
- treatments#
```

Use this when there is no individual item to name, including a knowledge gap
attached to an intentionally empty section. A bare section name such as
`clinical_burden` is not valid entity-reference syntax.

**There are two independent `#`-anchor resolvers, and they are not equally
strict.** `entity_refs.py` resolves intra-entry `<kind>#<name>` refs and is
enforced as a hard foreign key. `groupings.py` resolves the cross-entry
`module_stem#Node Name` refs used by `conforms_to` and by grouping
`CONFORMS_TO_MODULE` criteria — and there the anchor is **checked as a foreign
key but not used as a membership verdict**: a criterion naming
`ciliopathy_dysfunction#Motile Cilia Beat Dysfunction` is satisfied by a member
that conforms to `ciliopathy_dysfunction` at *any* node. The mismatch is
reported rather than enforced (`just grouping-anchor-audit`; a "not at named
node" badge on the grouping page) because some of the live mismatches are
criteria that are too narrow rather than entries that are under-annotated.
Do not assume `entity_refs.py`'s guarantees extend to a module anchor. See
issue #9403.

### Pathograph Targets Are Bare Names, Not Entity References

**The causal graph does not use the `<kind>#<name>` grammar.** This is the one
place the two conventions sit next to each other, and mixing them up is silent.
`dismech.graph` builds edges by matching a `target` string *verbatim* against
another item's `name` — there is no resolution step, no prefix handling, and no
error when it fails to match:

| Slot | Target form |
|---|---|
| `pathophysiology[].downstream[].target` | **bare name** |
| `phenotypes[].sequelae[].target` | **bare name** |
| `phenotypes[].reports_on[].target` | **bare name** |
| `treatments[].target_mechanisms[].target` | **bare name** |
| `environmental[].influences_mechanisms[].target` | **bare name** |
| `attaches_to`, `would_support`, `would_refute` | `<kind>#<name>` |
| `discussions[].proposed_experiments[].{perturbations,readouts}[].target` | `<kind>#<name>` |

```yaml
pathophysiology:
- name: Failure of Primary Hemostatic Plug Formation
  downstream:
  - target: Bleeding tendency          # correct — bare name
  # - target: phenotypes#Bleeding tendency   # WRONG — draws a phantom node
```

Writing `phenotypes#Bleeding tendency` there is not a validation error, a term
error, or a rendering error. The entry validates and the page builds.

**The symptom is not a missing arrow, so do not go looking for one.** The edge is
still appended, so the edge count never moves. The unresolved target lands in
`orphan_targets`, and the renderer draws it as a *phantom duplicate node* — red
fill, dashed red border, labelled with the literal `phenotypes#Bleeding tendency`
string — while the real `Bleeding tendency` node drops out of the graph entirely.
So the chain is fragmented and carries a bogus node. Issue #10112 found 175 such
targets across 32 entries; one was left with 0 of 7 phenotypes connected.

The mirror-image failure is a **rename**: change a node's `name` and every bare
target pointing at it dangles, just as silently (#9697). Search the file for the
old name before committing a rename.

```bash
just check-causal-targets                              # gate (runs in `just qc`)
just check-causal-targets kb/disorders/MyDisease.yaml
just list-causal-targets                               # full census, exit 0
```

The pre-existing dangling backlog is grandfathered in
`tests/causal_target_baseline.txt`; new breakage fails. Only ever shrink that
file. A **self-referential** `downstream` target — a pathophysiology node
whose `downstream` names itself — is **gated** by `just check-entity-refs` and
`test_entity_ref_foreign_keys` (#9896). It is rarely a claim that a node
causes itself: in both cases found on `main`, the curator was linking a
pathophysiology node to a *phenotype of the same name*, which the flat node
namespace collapses into a single node. The remedy is to merge the edge's
description and evidence onto the real upstream edge — or delete it when it
is bare — not to rename a node to dodge the collapse. The same collision can
happen in the other four `BARE_TARGET_SLOTS` (`phenotypes[].sequelae`,
`phenotypes[].reports_on`, `treatments[].target_mechanisms`,
`environmental[].influences_mechanisms`); those are not covered by the
`downstream`-only gate above and still surface only through
`just check-causal-targets`' report.
