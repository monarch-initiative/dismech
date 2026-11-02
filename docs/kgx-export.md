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

## The causal graph (#2101)

Each pathophysiology node is exported as a node of category
`biolink:PathologicalProcess`, with the id the SEPIO sidecar mints for it:
`dismech:<Disease_Name>#<Node_Name>`. Three kinds of edge come out of the graph:

| Source slot | Edge | Predicate |
|---|---|---|
| `pathophysiology[]` | Disease → node | `biolink:disease_has_basis_in` |
| `pathophysiology[].downstream[]` | node → node, or node → phenotype term | `biolink:causes` |
| `phenotypes[].sequelae[]` | phenotype term → phenotype term (or node) | `biolink:causes` |

A bare `target` resolves to the pathophysiology node of that name, else to the
bound term of the phenotype of that name, the same lookup the pathograph uses.
A `downstream` edge carries its `causal_link_type` in `qualifiers`. An HP → HP
`sequelae` edge is a `PhenotypicFeatureToPhenotypicFeatureAssociation` with the
disease as `disease_context_qualifier`, because the two terms alone say nothing
about which disease the progression was curated for.

Node and `downstream` edges use the SEPIO statements' deterministic UUIDv5 ids
instead of random ones, so they are stable across releases and join to the
sidecar. The SEPIO statements keep their own predicates
(`dismech:has_pathophysiology`, `dismech:causally_upstream_of`) and the
hypothesis groups, which a KGX edge has no slot for.

The per-slot edges from a node's cell types, processes and locations to the
disease are unchanged. They now exist alongside the graph rather than instead of
it; routing them through the node is a separate decision with consumer impact.

## Diagnosis, datasets and trials (#2100, #2103)

| Source slot | Edge | Predicate |
|---|---|---|
| `differential_diagnoses[]` | Disease → Disease | `biolink:similar_to` |
| `diagnosis[].diagnosis_term` | Disease → `biolink:Procedure` | `biolink:is_diagnosed_by` |
| `datasets[]` | `biolink:Dataset` → Disease | `biolink:mentions` |
| `clinical_trials[]` | `biolink:ClinicalTrial` → Disease | `biolink:related_to_at_instance_level` |
| `clinical_trials[].target_phenotypes[]` | `biolink:ClinicalTrial` → PhenotypicFeature | `biolink:related_to_at_instance_level` |

None of these has an exact Biolink 4.4 predicate, so each is the closest
canonical one:

- **Differentials.** There is no differential-diagnosis predicate (the
  `disease_has_differential_diagnosis` proposed in #2100 does not exist).
  `similar_to` is symmetric and says the two diseases share features, which is
  why a differential is listed, and claims nothing more.
- **Diagnosis.** `is_diagnosed_by` declares the range `diagnostic aid`, "a
  device or substance". `diagnosis_term` binds NCIT procedures such as computed
  tomography, so the object is typed `biolink:Procedure` for what it is, outside
  the predicate's declared range.
- **Datasets.** `mentions` is Biolink's predicate for an information content
  entity, which `dataset` is, referring to a named thing when the context is not
  modelled. The node id is the `accession` CURIE with its prefix lowercased
  (`GEO:GSE1` and `geo:GSE1` are one node); the dataset's `publication` is added
  to the edge's `publications`. An accession that is a publication (`PMID:`,
  `PMC:`, `DOI:`), a URL, or a `clinicaltrials:` id is not exported as a
  dataset: a publication is already cited in edges' `publications`, a DOI does
  not say whether it names a paper or a dataset, a URL is not a CURIE, and a
  trial is exported from `clinical_trials`.
- **Trials.** Biolink models a trial's conditions as a node property, and its
  trial predicates take a chemical as subject, so the edge is the generic
  instance-level one. An NCT id becomes `clinicaltrials:NCT…`. A trial on
  another registry is keyed on the `ICTRP:` record the entry cites. A trial with
  neither gets no node, because the exporter does not extract registry ids from
  free text.

### One id, one category

`extract_nodes` writes a node the first time a record names its id, with that
section's category. An NCIT term curated as both a treatment and a diagnostic
procedure in one entry (`NCIT:C15240` Genetic Counseling, `NCIT:C15329` Surgical
Procedure) is therefore written as `biolink:Treatment`, while its
`is_diagnosed_by` edge says `object_category: biolink:Procedure`. Across entries
the node file carries both. This is the same first-section-wins behaviour that
already gives some CHEBI ids both `ChemicalEntity` and `MolecularEntity`, and is
not specific to the new sections.

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
- `diagnosis[].measurements` (LOINC). Only the NCIT `diagnosis_term` is exported.
- `datasets[].findings`. A dataset exports as one node and one edge.
- A causal `target` that resolves to nothing (`just check-causal-targets`), or
  to a phenotype with no bound term. The edge is skipped; it is never given an
  invented id. Its SEPIO statement is still written, so these are the sidecar
  statements with no matching edge (490 at the time of writing, all
  `pathophysiology.downstream`).
