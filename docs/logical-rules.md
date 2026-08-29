# Logical Rules: Checking a Node Against Itself

Every validation gate in dismech checks one binding at a time. `linkml-validate`
asks whether the YAML has the right shape; `linkml-term-validator` asks whether
`CL:0000057` exists, is labelled `fibroblast`, and is in the `CellTypeTerm`
enum; `linkml-reference-validator` asks whether a snippet really appears in the
cited paper. Each answer is yes for this node:

```yaml
- name: Fibroblast activation and myofibroblast differentiation
  cell_types:
  - preferred_term: fibroblast
    term: {id: CL:0000057, label: fibroblast}
  biological_processes:
  - preferred_term: epithelial to mesenchymal transition
    term: {id: GO:0001837, label: epithelial to mesenchymal transition}
```

It is still wrong. A fibroblast is not an epithelial cell, so it is not the cell
that undergoes an epithelial-to-mesenchymal transition. Nothing in the repository
noticed, because the defect is not in either binding — it is in the pair.

Curators already catch these by hand, at some length.
`Hypoplastic_Left_Heart_Syndrome` carries a ten-line `notes` block explaining
why an earlier draft's `GO:0001837` was the wrong term for an endocardial node
and what would have to be true before `GO:0140074` could be used instead;
`Gastric_Adenocarcinoma` carries another explaining why its E-cadherin node
stops short of binding EMT at all. **Logical rules make that reasoning
executable.**

```bash
just check-logical-rules                              # whole KB, report-only
just check-logical-rules kb/disorders/Asthma.yaml     # one file
just check-logical-rules --strict                     # exit 1 on findings
just refresh-logical-rule-closures                    # after editing the rules
```

## What a rule says

A rule names a **process** and the cell classes that disqualify a node's cell
annotation from being that process's substrate. It fires when *every* annotated
cell type on a node carrying that process is disqualifying.

```yaml
- id: emt-without-epithelial-substrate
  processes: [GO:0001837]
  except_processes: [GO:0060317]
  disqualifying_cell_classes:
  - CL:0002320   # connective tissue cell -- covers fibroblast and myofibroblast
  - CL:0000115   # endothelial cell -- this is EndMT, a distinct process
  - CL:0000187   # muscle cell
  - CL:0008019   # mesenchymal cell
```

Rules live in [`conf/logical_rules.yaml`](https://github.com/monarch-initiative/dismech/blob/main/conf/logical_rules.yaml),
the evaluator in `src/dismech/logical_rules.py`. Anyone can add a rule by pull
request; two things about the formulation are load-bearing and are easy to get
backwards.

### 1. Rules assert what the cells *are*, never what they are not

The natural way to write the EMT rule is "EMT requires an epithelial cell; flag
any node that has none". That formulation does not survive contact with the Cell
Ontology.

`CL:0000646 basal cell` and `CL:0008036 extravillous trophoblast` are textbook
EMT substrates, and neither is an asserted subclass of `CL:0000066 epithelial
cell` — basal cell sits under `CL:0000036 epithelial fate stem cell`, and
extravillous trophoblast under `CL:0000351 trophoblast cell`. A requires-rule
reports both as defects, and every future thin spot in CL's `is_a` graph adds
another false accusation to a check curators are being asked to trust.

Naming the *disqualifying* classes inverts the failure mode. The claim becomes
positive — these cells are connective-tissue cells, and a connective-tissue cell
is not epithelium — so an ontology gap costs a **missed finding** rather than a
wrong one. On the KB as it stands the inverted rule reports nine EMT nodes and
none of them is a false positive; the requires-rule formulation adds four.

### 2. A rule fires only when *every* cell type is disqualifying

A node that annotates both ends of a transition — the alveolar epithelial cell
that starts it and the myofibroblast it becomes — is good curation.
`Paraquat_Poisoning`, `Proliferative_Vitreoretinopathy` and one of the two
`Adenomyosis` EMT nodes all look like this. An any-match rule would flag them
all.

### `except_processes` is for where the ontology disagrees with the rule

`GO:0060317 cardiac epithelial to mesenchymal transition` and its five children
classify an *endocardial endothelial* substrate under EMT. That is GO's own
placement, not a curation error, so a node bound to one of those terms is making
the claim GO sanctions and the rule steps aside. Note that a node bound to the
bare `GO:0001837` is still reported even in a cardiac context — rebinding to the
specific term is the fix, and it is an improvement in its own right.

## Closures are committed, not computed

The rules need to know that `CL:0000186 myofibroblast` is a connective tissue
cell, on every CI run, on a runner with no ontology build and no reason to reach
the network. So the `is_a` closure of each root is precomputed and committed
under `cache/closure/`, one file per root, sorted by CURIE — the same bargain
`cache/enums/*.csv` strikes for dynamic-enum membership.

`just refresh-logical-rule-closures` regenerates them through the adapters
`conf/oak_config.yaml` names, so the rules stay on the same ontology sources as
term validation. Run it after editing `processes`, `except_processes` or
`disqualifying_cell_classes`, and commit the result;
`--check` reports drift without rewriting. As with every other cache under
`cache/`, **do not hand-edit a closure file.**

Only `is_a` is traversed: `part_of` would pull in terms that are *parts of* a
connective tissue cell rather than *kinds of* one, and the rules ask about kinds.

A term whose closure is not cached is reported as unresolved and exits non-zero
even without `--strict` — a rule that cannot run is a broken check, not a clean
one.

## Report-only, and how to answer a finding

The check never fails the build by default. `--strict` exists, and `just qc`
runs it advisory, in the same posture as `check-source-defect-claims`: biology
has exceptions that an `is_a` graph cannot express, so a finding is a question
for a curator rather than a proven defect.

Answer it in one of two ways.

**Repair the annotation.** Usually one of:

| The node really means | Bind |
|---|---|
| fibroblast → myofibroblast conversion | `GO:0036446` myofibroblast differentiation |
| endothelium acquiring a mesenchymal phenotype | `GO:0140074` cardiac endothelial to mesenchymal transition |
| endocardial cushion formation | `GO:0003198`, or another `GO:0060317` descendant |
| loss of cell–cell adhesion, short of a full mesenchymal programme | `GO:0098609` cell-cell adhesion, `DECREASED` |

or add the epithelial cell that undergoes the transition, if the cells listed are
its product.

**Or record why the pairing is correct**, on the node, in `review_notes`:

```yaml
- name: Some Node
  review_notes: >-
    Logical rule waived: emt-without-epithelial-substrate. The epithelial
    substrate is named in the description and deliberately not annotated,
    because the cited source establishes only the mesenchymal endpoint.
```

The sentinel must be the **first** thing in `review_notes`, name the rule id,
and be followed by at least 20 words of reasoning — the floor
`check-environmental-evidence` uses, for the same reason: the sentence alone
does not waive, the argument does. `notes:` cannot waive; it is disease content.
A waiver naming a different rule does not transfer.

This is deliberately not a baseline file. A baseline records that a finding was
seen; `review_notes` records *why a curator decided it was fine*, in the place
the next curator will read it.

## Adding a rule

1. Add it to `conf/logical_rules.yaml` with a `summary` and a `remediation` that
   tells a curator what to actually do.
2. `just refresh-logical-rule-closures` and commit `cache/closure/`.
3. `just check-logical-rules` and read every finding. If the rule reports
   correct curation, the rule is wrong — reformulate it before proposing it.
4. If the ontology cannot support the rule at all, say so in the config comment
   rather than shipping a rule that needs a waiver on half its hits.

The engine currently expresses one rule shape: process × cell-type-class
incompatibility. Other genres — a node both `INCREASED` and `DECREASED` for the
same term, an anatomical location incompatible with a cell type — would each
need their own predicate, and the seam for them is the `Rule` dataclass in
`src/dismech/logical_rules.py`.
