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
  - preferred_term: pancreatic acinar cell
    term:
      id: CL:0002064
      label: pancreatic acinar cell
```

That entry now derives **pancreatic acinar cell** as its cell of origin --
not the ductal cell its name might suggest, because *ductal* is the tumour's
histology and the entry's own lineage-tracing evidence places the lesion in the
acinar compartment, with the ductal phenotype acquired downstream through
acinar-to-ductal metaplasia.
`Pancreatic_Ductal_Adenocarcinoma` and `Chronic_Myeloid_Leukemia` are the
committed worked examples.

`allelic_hit_role: FIRST_HIT` is worth adding on a two-hit tumor suppressor,
where the first hit is the origin event and the second is progression.

**Do not mark a virally driven mechanism.** HPV E7 inactivating pRB, or HTLV-1
Tax activating NF-kB, is not a host genetic lesion: there is no variant for
`variant_origin` to describe, which is the case CLAUDE.md already rules on for
`functional_impact_category`. Those cancers record their origin through the
exposure rule below instead, and marking them `SOMATIC` actively breaks it,
because a recorded lesion suppresses the exposure rule.

## The two rules

Both read a structured claim the entry makes. Neither reads a naming convention,
and there is no fallback chain: an entry that does not say where it starts is
reported as not saying it, rather than guessed at.

1. **`SOMATIC_LESION`** — a node with `variant_origin: SOMATIC` or
   `GERMLINE_AND_SOMATIC`. Not restricted to root nodes: a transformation or
   second-hit lesion is still a somatic event.
2. **`ENVIRONMENTAL_TRIGGER`** — a node that an
   `environmental[].influences_mechanisms` link marks
   `environmental_effect: TRIGGERS`. This is non-mutational initiation, where
   there is no host lesion to mark: HPV in anal carcinoma, H. pylori in gastric
   adenocarcinoma, asbestos in mesothelioma, UV in cutaneous SCC. It is the same
   value the KGX exporter and compliance scoring already treat as causal, so it
   is not a cell-of-origin-specific convention.

**Rule 2 applies only when no lesion is recorded**, and that is a statement about
meaning rather than confidence. The cell of origin is the cell the transforming
event occurred in, so once the entry records that event, the exposure is upstream
context. Pancreatic ductal adenocarcinoma is where the difference shows: chronic
pancreatitis genuinely triggers its inflammation node, but that node binds
macrophage and pancreatic stellate cell, while the disease arises in the acinar
cell named on the KRAS lesion.

### What was removed, and why

An earlier version had a third rule that read an initiating-sounding `role`
string on a root node, plus a fallback chain so a stronger rule could not discard
a weaker rule's answer. Both existed to paper over entries that had not recorded
their origin, and both mis-fired — the role rule is what derived macrophage and
pancreatic stellate cell as the cell of origin of pancreatic cancer. There was
also a `CONTEXT_NODE_MARKED` finding whose only job was catching those mistakes,
and which false-positived on cancers that really are inflammation-initiated
(cholangiocarcinoma, hepatocellular carcinoma).

The records were marked instead, and all of it was deleted.

## Backfilling an entry

`just backfill-cancer-origin` proposes markings, and **invents nothing**: it only
marks a node whose own `name` already states a somatic lesion — mutation, fusion,
translocation, amplification, biallelic inactivation, loss of heterozygosity.
A node saying merely that a pathway is active is not a lesion. Nodes reading as
germline, as microenvironment, or as acquired resistance are excluded, the last
because "ESR1 Mutation-Driven Endocrine Resistance" is a real somatic event that
happens years after the disease starts.

`--bind-single-cell` additionally copies the entry's cell type onto the lesion
node when the entry names exactly one. Entries naming several are left alone:
choosing among them is a curator's call.

```bash
just backfill-cancer-origin                     # dry run
just backfill-cancer-origin --bind-single-cell  # dry run, wider
just backfill-cancer-origin --apply
```

Always re-validate afterwards — `just validate-disorders` on the changed files.

## Reading the findings

`MULTI_ORIGIN_CELL`
: More than one derived cell of origin. **This is what the check exists for,
  and it never gates**, because it means one of three quite different things
  and only a curator can say which:

    1. a pool wearing a Disease entry's clothes — `Non-Small_Cell_Lung_Cancer`
       derives alveolar type 2 cell *and* bronchial epithelial cell, which is
       what NSCLC is: adenocarcinoma plus squamous carcinoma. These are L1/L2
       pools on the granularity ladder and the remedy is a `Grouping` or a split;
    2. one disease with genuine cell-of-origin **subtypes** —
       `B-Lymphoblastic_Leukemia_Lymphoma_With_Recurrent_Genetic_Abnormality`
       (B-lymphoblast and precursor B cell across 19 subtypes),
       `GPR101-related_pituitary_adenoma_2` (somatotroph and mammotroph). The
       remedy is `has_subtypes`;
    3. an origin the literature has not settled —
       `Melanoma_in_Congenital_Melanocytic_Nevus` names melanocyte and neural
       crest cell on one node. Naming both is the honest answer, and the remedy
       is a note saying so.

  The seven current findings are all of these kinds, which is the point: the
  list is short enough to work through, and every row is a real modeling
  question. `Gastrointestinal_Lymphoma` is the clearest — B cell *and*
  intraepithelial lymphocyte, because the entry covers both MALT lymphoma and
  EATL. `Lung_Carcinoma` and `Non-Small_Cell_Lung_Cancer` now agree: the broad
  pool reports the same split its own subtype entry does.

**What the census prints.** The derived cell is shown by its `preferred_term`
when the binding has one, falling back to the ontology label. A curator uses
that slot to say something the label does not — `Epithelioid_Sarcoma` binds
`CL:0000134` under `mesenchymal cell of uncertain differentiation`, and printing
the label would have the census assert "mesenchymal stem cell", which the entry
is careful not to. Only the display name changes: the CURIE is what identifies
a cell, so de-duplication and multi-origin detection are unaffected. The TSV
column and JSON key are named `origin_cell_names` / `"name"` rather than
`label` for that reason — they hold what the entry calls the cell, which is
often not the ontology's label, so joining them against CL labels would miss
on exactly the hedged bindings. Where two origin nodes bind one CURIE under
different `preferred_term`s both wordings are kept, joined with ` / `: it is
still one cell, but the disagreement is the sort of thing this census exists
to show.

`scripts/backfill_cancer_origin.py` is the one caller that writes `_terms()`
output back into YAML, and it asks for the canonical label explicitly
(`display=False`). A borrowed binding reproduces both slots as the source
entry had them — the curator's wording in `preferred_term`, the ontology's
label in `term.label` — because `term.label` must match the ontology exactly.
Collapsing the two writes a label CL does not have, and `just validate-terms`
rejects it. That script writes YAML as text, so it emits every borrowed value
as a quoted scalar where a plain one would not survive -- the KB holds
`preferred_term`s like `EMG: myopathic abnormalities`, where an unquoted
colon-space would make a nested mapping instead of a string.

`ORIGIN_WITHOUT_CELL`
: An origin node was identified but binds no CL term. The cheapest class to fix,
  since the marking is already there.

`NO_ORIGIN`
: Neither marker is present. This is the remaining backlog: 122 of 245 assessed
  neoplasm entries, down from 220 before the backfill. Most are entries whose
  pathograph names no genetic lesion at all, or names one with no cell type
  anywhere in the entry — both need a curator, not a script.

```bash
just check-cancer-origin                  # summary + the multi-origin worklist
just check-cancer-origin --format list    # every entry, one line each
just check-cancer-origin --format tsv     # machine-readable
just check-cancer-origin --fail-on ORIGIN_WITHOUT_CELL # gate one class
just list-cancer-origin
```

It runs inside `just qc` as a report and exits 0 by default, because 122 entries
are still unmarked. `ORIGIN_WITHOUT_CELL` is currently at **zero**, though, so
that class is a candidate for a real gate: every entry that marks an origin
binds a cell there, and it would be a regression for one to stop doing so.

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

**Rebuild the cache before citing one of these rows.** The predicates are
declared in the manifest, but no `references_cache/NCIT_*.md` in the repository
carries them yet — generating those files needs the OAK-managed NCIT SQLite,
which is downloaded on demand and never committed. A snippet quoted against a
row that has not been generated fails reference validation:

```bash
just ncit-edges-refresh
just ncit-edges-rebuild --id NCIT:C8851
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
reads both and de-duplicates.

## Why not a `cell_of_origin:` slot

A dedicated slot would be a second place to say something the pathograph already
says, and the two would drift. Worse, it would sit at the disease level, where
it could not distinguish the origin of a subtype from the origin of the parent,
and it would invite curators to fill it in from the disease name rather than
from the mechanism. Deriving it keeps the claim attached to the node that
carries its evidence, and makes an unmarked entry visible as an unmarked entry
rather than as an empty field.
