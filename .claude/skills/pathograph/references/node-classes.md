# Pathograph node classification tools

### Pathograph Node Classes (`kb/node_classes/`)

A curated vocabulary of *kinds of pathophysiology node*, ordered as a causal
cascade (genomic, environmental, molecular activity, molecular substance,
pathway, cellular, tissue/organ, systemic, outcome) plus cross-cutting classes
(disposition, compensation, intervention point). It lives in
`kb/node_classes/pathograph_node_classes.txt` as an indented plain-text tree.
Each line's kind is decided by its first non-space character: `#` comment,
`[Disease_Entry] Node name` a worked example (a real pathophysiology node),
`:key value` an attribute, `= expression` the class's logical definition, and
anything else a class with an optional ` -- gloss`. A definition is a
sufficient condition over the node's ontology-bound slots
(`biological_processes some GO:0008219 'cell death'`,
`chemical_entities some CHEBI modifier INCREASED`; grammar in
`src/dismech/node_class_definitions.py`); judgement classes (DISPOSITION,
OUTCOME, STILL UNPLACED …) deliberately carry none. A companion
`pathograph_node_class_go_seed.tsv` maps GO biological-process terms to
classes. There is **no schema slot yet**: no disorder entry names a class, and
the scanner applies the vocabulary read-only. Edit the tree by PR like any
other `kb/` content.

```bash
just node-classes --verify-kb              # grammar + every cited leaf resolves in kb/
just node-classes --check-definitions      # definition labels vs the term caches (--online: OLS)
just node-classes --evaluate               # each definition vs its examples and the KB (needs GO sqlite)
just node-class-scan                       # apply the seed table across kb/: coverage
just node-class-scan --format debundle     # nodes whose own GO terms span two classes
just node-role-audit                       # the free-text `role` slot against the edges
```

Design record: `docs/superpowers/specs/2026-08-16-pathograph-node-classification-brainstorm.md`.
