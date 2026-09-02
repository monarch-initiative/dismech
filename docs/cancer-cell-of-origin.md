# Cell of origin: derived, not stored

The cell a cancer arises from is one of the strongest lump/split signals
oncology has. WHO's taxonomy is a histogenesis backbone with molecular
alterations promoted into it case by case (design decisions
[§3a](explanation/design-decisions.md)), and the
[cancer curation SOP](cancer-curation-sop.md) already names "different cell of
origin" as its first split criterion. Until now nothing in the KB recorded it
in a way you could query.

**There is no `cell_of_origin:` slot, and there should not be one.** The entry
already carries both halves of the statement:

| The question | The slot that already answers it |
|---|---|
| Which node is the origin? | `pathophysiology[].genetic_context.variant_origin: SOMATIC` |
| Which cell did it happen in? | that node's `cell_types` |

So the cell of origin is *derived*: find the node where the transforming lesion
occurred, then read its cell types. `just check-cancer-origin` implements that
derivation and reports where it fails.

## Marking the origin node

Put a `genetic_context` on the pathophysiology node that carries the initiating
somatic lesion. Nothing else changes; `cell_types` stays bound to CL as always.

```yaml
pathophysiology:
- name: KRAS Oncogene Activation
  genetic_context:
    gene:
      preferred_term: KRAS
      term:
        id: hgnc:6407
        label: KRAS
    variant_origin: SOMATIC
    functional_impact_category: GAIN_OF_FUNCTION
    description: >-
      Somatic activating KRAS codon-12 mutation, the initiating lesion of the
      PanIN-to-PDAC sequence.
  cell_types:
  - preferred_term: pancreatic ductal cell
    term:
      id: CL:0002079
      label: pancreatic ductal cell
```

That entry now derives **pancreatic ductal cell** as its cell of origin.
`Pancreatic_Ductal_Adenocarcinoma` and `Chronic_Myeloid_Leukemia` are the
committed worked examples.

`allelic_hit_role: FIRST_HIT` is worth adding on a two-hit tumor suppressor,
where the first hit is the origin event and the second is progression.

## The three rules, and why there are three

The checker applies these in order and reports which one fired, so a deliberate
marking is distinguishable from a lucky guess.

1. **`SOMATIC_LESION`** — a node with `variant_origin: SOMATIC` or
   `GERMLINE_AND_SOMATIC`. Prefer this. It is a structured claim about a
   mutational event rather than a naming convention, and it is the only rule
   that is unambiguous. It is not restricted to root nodes, because a
   transformation or second-hit lesion is still a somatic event.
2. **`INITIATING_ROLE`** — a root node whose free-text `role` reads as
   initiating (`trigger`, `driver`, `root`, `primary`, …). Weaker by
   construction: `role` is an unconstrained string and the KB holds around 90
   distinct values on pathophysiology nodes. Only root nodes count, because off
   a root node "trigger" names a step inside the cascade.
3. **`EXPOSURE_TRIGGER`** — a root node carrying `triggers`. This is
   non-mutational initiation, where there is no host lesion to mark at all:
   HTLV-1 in adult T-cell leukemia, EBV, a chemical carcinogen.

A stronger rule wins **only if it actually yields a cell**. A lesion node often
carries the gene and not the cell it occurred in, and letting rule 1 win
outright there would throw away a correct answer sitting one node over and
report the entry as unmarked.

## Reading the findings

`MULTI_ORIGIN_CELL`
: More than one derived cell of origin. **This is what the check exists for,
  and it never gates**, because it means one of three quite different things
  and only a curator can say which:

    1. a grouping wearing a Disease entry's clothes — `Kidney_Sarcoma` derives
       four mesenchymal lineages, `Appendiceal_Neoplasm` derives epithelial plus
       goblet plus enteroendocrine. These are L1 pools on the granularity ladder
       and the remedy is a `Grouping`;
    2. one disease with genuine cell-of-origin **subtypes** — DLBCL's centrocyte
       and centroblast, which WHO treats as GCB/ABC strata of a single entity.
       The remedy is `has_subtypes`;
    3. an origin the literature has not settled — Ewing sarcoma's mesenchymal
       stem cell versus neural crest cell. Naming both is the honest answer, and
       the remedy is a note saying so.

`CONTEXT_NODE_MARKED`
: The derivation landed on a node describing the setting rather than the
  origin: microenvironment remodeling, chronic inflammation, immune evasion.
  Binding macrophage, Treg and fibroblast there is correct curation; treating
  them as the cell of origin is not. This is the failure mode of rule 2, and the
  fix is to mark the transforming lesion so rule 1 wins. Pancreatic ductal
  adenocarcinoma was exactly this case before the marking was added: a "Chronic
  Pancreatic Inflammation" root node marked `role: trigger` derived macrophage
  plus pancreatic stellate cell.

  The test is on the node **name**, not on a list of stromal cell types, because
  no cell type is stromal everywhere: a T cell is microenvironment in a
  carcinoma and the cell of origin in a T-cell lymphoma.

`ORIGIN_WITHOUT_CELL`
: An origin node was identified but binds no CL term. The cheapest class to fix,
  since the marking is already there.

`NO_ORIGIN`
: No rule fired. This is most of the corpus, which is why the check is advisory.

```bash
just check-cancer-origin                  # summary + the multi-origin worklist
just check-cancer-origin --format list    # every entry, one line each
just check-cancer-origin --format tsv     # machine-readable
just check-cancer-origin --fail-on MULTI_ORIGIN_CELL   # gate one class
just list-cancer-origin
```

It runs inside `just qc` as a report. It exits 0 by default and is not wired
into CI as a gate: with most entries unmarked, a gating default would be noise
rather than signal.

## What NCIT contributes

NCIT already asserts a cell of origin per disease, inside its `owl:equivalentClass`
logical definitions:

| Relation | Says |
|---|---|
| `NCIT:R104` Disease_Has_Normal_Cell_Origin | the normal cell the disease arises from |
| `NCIT:R112` Disease_May_Have_Normal_Cell_Origin | the same, asserted weakly |
| `NCIT:R105` Disease_Has_Abnormal_Cell | the transformed cell state, from the Abnormal Cell branch (`NCIT:C12913`) |

For example DLBCL is `Mature B-Lymphocyte` → `Neoplastic Large B-Lymphocyte`,
and CML is `Pluripotent Bone Marrow Stem Cell`. These three predicates are
ingested by the existing manifest-driven `OntologyEdgeSource`
(`data/ncit-edges/MANIFEST.yaml`), which emits quotable rows into
`references_cache/NCIT_*.md`:

```yaml
evidence:
- reference: NCIT:C8851
  supports: SUPPORT
  evidence_source: OTHER
  snippet: "Disease_Has_Normal_Cell_Origin | NCIT:C12475 | Mature B-Lymphocyte"
  explanation: NCI Thesaurus asserts the normal cell of origin for this entity.
```

Two things this is **not**:

- **Not a binding target.** `CellTypeTerm` is reachable from `CL:0000000` alone,
  so `cell_types` stays CL-only and an NCIT code there fails term validation.
  NCIT names its own classes, so this is a cross-check and a lookup aid.
- **Not automatic agreement.** There is no NCIT-to-CL mapping in the repo, so
  comparing our derived CL term against NCIT's normal-cell class is a curator's
  judgement, not a computed match.

The Abnormal Cell branch does fill a real gap, though. CL has almost nothing at
the transformed-cell level — only the generic `CL:0001063` neoplastic cell and
`CL:0001064` malignant cell, which is why an entry needing "H3 K27M-mutant
glioma cell" has to bind the generic term. If that becomes worth binding
directly, the change is one source node on `CellTypeTerm`, with the convention
that CL carries the normal cell of origin and NCIT the transformed state — two
claims in two slots, never mixed into one `cell_types` list.

The NCIT relations live in semsql's `edge` table rather than in `statements`,
because they are asserted through existential restrictions. `OntologyEdgeSource`
reads both and de-duplicates. Rebuilding the cache needs the OAK-managed NCIT
SQLite, which is downloaded on demand and never committed:

```bash
just ncit-edges-refresh
just ncit-edges-rebuild --id NCIT:C8851
```

## Why not a `cell_of_origin:` slot

A dedicated slot would be a second place to say something the pathograph already
says, and the two would drift. Worse, it would sit at the disease level, where
it could not distinguish the origin of a subtype from the origin of the parent,
and it would invite curators to fill it in from the disease name rather than
from the mechanism. Deriving it keeps the claim attached to the node that
carries its evidence, and makes an unmarked entry visible as an unmarked entry
rather than as an empty field.
