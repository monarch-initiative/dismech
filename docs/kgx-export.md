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

Several dismech slots carry a **direction** that the Biolink predicate alone
cannot express. The pinned `biolink_model` pydantic bindings expose typed
qualifier slots on only some association classes — `Association` and
`ExposureEventToOutcomeAssociation` both lack `subject_direction_qualifier` and
`object_direction_qualifier` — so direction is emitted as a string entry in the
generic `qualifiers` list.

| Qualifier | Emitted on | Source slot | Qualifies |
|---|---|---|---|
| `direction:<increased\|decreased>` | Disease→GO edges (biological process, molecular function, cellular component) | `Descriptor.modifier` | the **object** |
| `subject_direction:<increased\|decreased>` | Exposure→Disease edges | `exposure_term.modifier` | the **subject** |
| `causal_link_type` values (`DIRECT`, `INDIRECT_KNOWN_INTERMEDIATES`, …) | pathophysiology causal edges (SEPIO sidecar) | `downstream[].causal_link_type` | the edge |

**The bare `direction:` prefix means "object" by convention**, and only because
those edges predate the exposure case. On a Disease→GO edge the disease is
always the subject and the direction always describes the GO term, so the
prefix was never ambiguous in context. The exposure edge inverts that geometry —
the ECTO term is the *subject* — so it spells the end out. Normalizing the older
edges to `object_direction:` would be tidier but is a breaking change to
7,262 existing edges; see #9132.

### Why exposure direction matters

The exposure edge's subject is the ECTO term itself, so the direction is what
separates a deficiency from an exposure. Both of these curate `ECTO:9000123`
(exposure to folic acid) as the subject:

```
Anencephaly                 ECTO:9000123 --contributes_to-->                          MONDO:0000819
                            qualifiers: [subject_direction:decreased]
Ventricular_Septal_Defect   ECTO:9000123 --associated_with_decreased_likelihood_of--> MONDO:0002070
                            qualifiers: [subject_direction:increased]
```

Without the qualifier the first triple asserts that exposure to folate causes
anencephaly, which is the opposite of the curated claim (#8468). The direction
is carried **independently of the predicate** because the two axes are
orthogonal: the second entry is an *increased* exposure that is *protective*.

`ModifierEnum` values that assert no direction (`ABNORMAL`, `DYSREGULATED`) are
dropped rather than guessed at. `ABSENT` (`PATO:0000462`) is the exception on an
exposure — "not occurring or not present" is a statement about polarity, so it
maps to `decreased`, the closest value in Biolink's
`DirectionQualifierEnum` (`increased`/`upregulated`/`decreased`/`downregulated`,
which has no "absent"). That mapping is exposure-specific: on a Disease→GO edge
`ABSENT` qualifies a process rather than an exposure and is still dropped.

## What is not exported

- `Pathophysiology.triggers` — the *other* route an ECTO exposure term reaches a
  mechanism node. It has no KGX edge at all, so the exposure-polarity handling
  above does not apply to it.
- Model links (`experimental_models`, `animal_models`, `computational_models`)
  and their readouts. `kgx_export.py` has no model handling; these render in the
  HTML card only.
- `differential_diagnoses` / `diagnosis` (#2100), `datasets` / `clinical_trials`
  (#2103), and the `downstream`/`sequelae` causal edges in the node/edge files
  (#2101 — these *are* in the SEPIO sidecar).
