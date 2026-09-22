---
name: pathograph
description: >-
  Build, edit, or review dismech pathographs: atomic mechanism nodes, causal
  chains, phenotype sequelae, environmental links, treatment targets, entity
  references, biological scale, and activity state. Use for disconnected
  phenotypes, dangling or renamed targets, node bundling, and connectivity
  audits. Not for renderer/layout implementation or computational model execution.
---

# Curate a Pathograph

A pathograph states how a disease mechanism leads to observable features, and
where exposures or interventions act. Build a supported causal chain rather than
copying a report's thematic headings into a list of nodes.

## Decide the claims before drawing edges

- Keep each node to one mechanistic claim. Split when steps have separable
  evidence, different cell types/sites, or distinct downstream consequences.
- Branch where the biology branches. Parallel effectors are sibling nodes,
  not one pathway label simply because a report discussed them together.
- Do not expand textbook intermediates unless they add a disease-relevant
  claim, annotation, or target. See [granularity examples](../../../docs/pathographs.md#node-granularity-and-debundling-case-study-csan).
- Connect phenotypes when the source supports the mechanism-to-feature link.
  An unknown mechanism stays an explicit gap; never add edges to meet a score.
- Keep causal evidence, observation/readout links, susceptibility, and treatment
  effects distinct. A therapeutic target link does not explain the phenotype's cause.

Use `dismech-references` for every evidence decision and `dismech-terms` for
bindings. An edge makes its own claim; a citation supporting both endpoint nodes
does not automatically support the edge between them.

## Use the right reference grammar

Read [targets and foreign keys](references/targets.md) whenever adding, renaming,
splitting, or reviewing a referenced node. Two conventions coexist:

| Slot | Target form |
|---|---|
| `downstream`, `sequelae`, `reports_on`, `target_mechanisms`, `influences_mechanisms` | Bare node `name` |
| `attaches_to`, `would_support`, `would_refute`, experiment perturbation/readout targets | `<section>#<name>`, optionally qualified by file |
| `conforms_to` | `<module_stem>#<Node Name>` |

Search for every old name before a rename. A malformed bare target can draw a
phantom duplicate instead of the intended node; schema validation alone cannot
establish that the graph is connected.

## Read the detail relevant to this change

- [Connectivity](references/connectivity.md): disconnected phenotypes, attachment
  classes, corpus-level floors, and gene outlinks. Use when wiring an entry or
  interpreting a compliance finding.
- [Scale and activity state](references/scale-and-state.md): choose
  `biological_scale`; distinguish a variant's `functional_impact_category` from
  a descriptor's quantitative or qualitative `modifier`.
- [Environmental links](references/environment.md): distinguish initiation,
  exacerbation, susceptibility, protection, and modulation; evidence belongs on
  both the exposure record and the link that makes a separate claim.
- [Node classification](references/node-classes.md): use the curated node-class
  vocabulary and audit tools when classifying or debundling mechanisms. The
  vocabulary is not a schema slot to add to disease YAML.

Use `create-module` when choosing or reviewing `conforms_to`; it covers module
scope and disease-specific substitutions. Use `medical-action` for therapeutic
links and action categories: diagnosis, screening, monitoring, and informational
counseling must not be wired as treatments. Use `model-curation` for
`modeled_mechanisms`, model readouts, fidelity, and divergences.

## Preserve uncertainty and test the graph

Use the existing `mechanistic_hypotheses` and edge `hypothesis_groups` when a
chain belongs to a specific hypothesis. Record missing knowledge in `discussions`
with `kind: KNOWLEDGE_GAP`; use `HUMAN_MODEL_MISMATCH` when the open question is
model-to-human fidelity. Do not invent a `knowledge_gaps:` slot. Proposed
experiments use entity references for `would_support`/`would_refute` and prose
for `supporting_outcome`/`refuting_outcome`.

After a graph edit, run schema/term/evidence validation plus:

```bash
just check-entity-refs kb/disorders/MyDisease.yaml
just check-causal-targets kb/disorders/MyDisease.yaml
just list-disconnected-phenotypes kb/disorders/MyDisease.yaml
```

The first two check integrity; the last is a curation worklist, not a demand for
unsupported edges. Inspect the rendered graph when the change affects topology;
do not commit derived page output. Run the final batched validation before a PR.
