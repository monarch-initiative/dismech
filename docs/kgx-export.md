# KGX Export

`just export-kgx` projects `kb/disorders/*.yaml` into a Biolink-typed KGX graph
via [koza](https://github.com/monarch-initiative/koza):

```bash
just export-kgx        # -> output/kgx/kgx_export_{nodes,edges,sepio}.jsonl
```

The transform lives in
[`src/dismech/export/kgx_export.py`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/export/kgx_export.py).
The `_sepio` sidecar is a separate model documented in
[SEPIO Evidence Export](sepio-export.md); it joins to the edge file on `id`.

## Edge qualifiers

Several dismech slots carry a **modifier** that the Biolink predicate alone
cannot express. Biolink declares the `qualifiers` slot as:

```yaml
qualifiers:
  deprecated: true
  description: connects an association to qualifiers that modify or qualify the meaning of that association
  range: ontology class
  multivalued: true
```

`range: ontology class` — so every entry is a **CURIE naming a class**. A
free-text entry like `direction:increased` is not one, and its prefix claims a
namespace (`direction:`) that nothing can resolve. Both forms are gone; see
#9131.

Two honest caveats about this slot. Biolink marks it `deprecated: true` in the
same block, and it is used anyway because it is the only qualifier slot the
pinned bindings expose on these association classes — the typed direction
qualifiers are the eventual destination (#9132). And the `dismech:` CURIEs below
satisfy `range: ontology class` in form but not in substance: nothing publishes a
class at those IRIs. Both are conscious positions, not oversights.

| Source slot | Emitted on | Qualifies |
|---|---|---|
| `Descriptor.modifier` | Disease→process edges (biological process, molecular function, pathway) | the **object** |
| `exposure_term.modifier` | Exposure→Disease edges | the **subject** |
| `downstream[].causal_link_type` | pathophysiology causal edges (SEPIO sidecar) | the edge |

Note `pathway_to_edge` carries `object_category: biolink:Pathway` rather than a
GO category, even though the term is a GO biological process — a consumer
filtering qualifier-carrying edges by category has to include `biolink:Pathway`
alongside `biolink:BiologicalProcess` and `biolink:MolecularActivity`.

### The vocabulary comes from the schema

Values are not invented by the exporter. `ModifierEnum` already binds four of
its seven permissible values to PATO, and those export as the bound term:

| `ModifierEnum` | Emitted CURIE | Label |
|---|---|---|
| `INCREASED` | `PATO:0002300` | increased quality |
| `DECREASED` | `PATO:0002301` | decreased quality |
| `ABNORMAL` | `PATO:0000460` | abnormal |
| `ABSENT` | `PATO:0000462` | absent |
| `DYSREGULATED` | `dismech:ModifierEnum#DYSREGULATED` | — |
| `GAIN_OF_FUNCTION` | `dismech:ModifierEnum#GAIN_OF_FUNCTION` | — |
| `LOSS_OF_FUNCTION` | `dismech:ModifierEnum#LOSS_OF_FUNCTION` | — |

The last three carry no `meaning:` in the schema, so they fall back to the
**dismech namespace**, declared in the schema prefix map as
`https://w3id.org/monarch-initiative/dismech/` and set as `default_prefix`. These
are resolvable CURIEs pointing at our own model, which is the right answer when
dismech and Biolink do not align: refer to the dismech model by its own prefix
rather than minting a fictional one.

**The scope of that "no term" finding matters, so it is recorded precisely.** The
schema carries two different notes here, with different scopes: `DYSREGULATED` is
*"No PATO term exists — verified via OAK 2026-06-26"*, while `GAIN_OF_FUNCTION`
and `LOSS_OF_FUNCTION` are *"No suitable ontology term found across
PATO/GENO/GO/SO (verified 2026-06-26)"*. An OLS-wide recheck on 2026-08-20
confirmed the first and partly overturned the second:

- `DYSREGULATED` — **confirmed unbound**. Every "dysregulation" hit across PATO,
  GO, NCIT, OGMS and MPATH is a disease entity (IPEX, DMDD), not a quality. The
  nearest quality is `PATO:0000460` abnormal, which `ABNORMAL` already uses and
  which is a distinct curator choice.
- `GAIN_OF_FUNCTION` / `LOSS_OF_FUNCTION` — **candidates exist** that the original
  four-ontology search did not surface: `PATO:0001625` "increased functionality"
  and `PATO:0001624` "decreased functionality", in a PATO branch separate from the
  `increased quality`/`decreased quality` used for `INCREASED`/`DECREASED`. Not
  adopted: it is a schema question (they belong on the enum's `meaning:`, which
  this exporter only reads), and the fit is imperfect — `ModifierEnum`'s
  `GAIN_OF_FUNCTION` means escaping regulatory control rather than increased
  ability to perform a function. Note this **contradicts the schema note**, which
  says nothing suitable was found across PATO. Tracked in #9136; the export
  follows whatever the schema binds.

`CausalLinkTypeEnum` binds none of its four values, so all four take the same
route: `dismech:CausalLinkTypeEnum#DIRECT`, `#INDIRECT_KNOWN_INTERMEDIATES`,
`#INDIRECT_UNKNOWN_INTERMEDIATES`, `#UNKNOWN`.

**The fallback is qualified by its enum, not flat.** 18 permissible-value names
in this schema belong to more than one enum. `GAIN_OF_FUNCTION` and
`LOSS_OF_FUNCTION` are among them — they are `FunctionalImpactEnum` values too,
where they describe a *variant's consequence* rather than a *pathway's activity
state*, a distinction the schema keeps deliberately and which can co-occur on one
node. A flat `dismech:GAIN_OF_FUNCTION` would give both concepts one IRI. The
`dismech:{Enum}#{VALUE}` form matches `SchemaView.get_uri(ModifierEnum)` and the
fragment convention already used for pathophysiology node IDs.

`test_modifier_curies_match_schema_meanings` pins the map against
`src/dismech/schema/dismech.yaml`, so the exporter and the schema cannot drift;
`test_no_qualifier_is_a_bare_string` pins that every emitted value is a CURIE
under a declared prefix.

### Which end a qualifier applies to

The CURIE does not say whether it qualifies the subject or the object — it is a
quality, not a statement about edge geometry. It is recoverable from the edge:
a disease is never the end a `decreased quality` describes, so on an exposure
edge the qualifier can only be about the exposure, and on a Disease→process edge
only about the process.

Biolink's typed `subject_direction_qualifier` / `object_direction_qualifier`
would state it outright, but neither is present on `Association` or
`ExposureEventToOutcomeAssociation` in the pinned bindings (their only qualifier
slots are `qualifier`, `qualifiers`, and — on the exposure class —
`population_context_qualifier` and `temporal_context_qualifier`). Tracked in
#9132.

### Why exposure polarity matters

The exposure edge's subject is the ECTO term itself, so the qualifier is what
separates a deficiency from an exposure. Both of these curate `ECTO:9000123`
(exposure to folic acid) as the subject:

```
Anencephaly                 ECTO:9000123 --contributes_to-->                          MONDO:0000819
                            qualifiers: [PATO:0002301]     # decreased quality
Ventricular_Septal_Defect   ECTO:9000123 --associated_with_decreased_likelihood_of--> MONDO:0002070
                            qualifiers: [PATO:0002300]     # increased quality
```

Without the qualifier the first triple asserts that exposure to folate causes
anencephaly, the opposite of the curated claim (#8468). The qualifier is carried
**independently of the predicate** because the two axes are orthogonal: the
second entry is an *increased* exposure that is *protective*.

## What is not exported

- `cellular_components[].modifier` — `cellular_component_to_edge` never reads
  `modifier`, so 61 curated values across `kb/` are dropped. Pre-existing, and
  left alone here rather than quietly widening this change; wiring it would add
  qualifiers to edges that have never carried them.
- `Pathophysiology.triggers` — the *other* route an ECTO exposure term reaches a
  mechanism node. It has no KGX edge at all, so the exposure-polarity handling
  above does not apply to it.
- Model links (`experimental_models`, `animal_models`, `computational_models`)
  and their readouts. `kgx_export.py` has no model handling; these render in the
  HTML card only.
- `differential_diagnoses` / `diagnosis` (#2100), `datasets` / `clinical_trials`
  (#2103), and the `downstream`/`sequelae` causal edges in the node/edge files
  (#2101 — these *are* in the SEPIO sidecar).
