# Cancer scope and cell of origin

### Cancer Entry Granularity

Somatic cancer entries follow the **granularity ladder** ratified in design
decisions §3a (`docs/explanation/design-decisions.md`) — consult it before
creating any new cancer/neoplasm entry. The short version:

- **Default level for a new cancer entry is the histologic entity** (the WHO
  blue-book / ICD-O morphology level: PDAC, SCLC, DLBCL), or the
  **WHO/ICC-defined molecular entity** where the field defines one
  (IDH-wildtype glioblastoma, NPM1-mutant AML).
- **Biomarker/therapy strata** (EGFR-mutant NSCLC, MSI-H CRC, TNBC) default to
  `has_subtypes` on the parent; promote to a separate entry only with ≥2
  stratum-specific pathophysiology nodes **and** a distinct first-line therapy
  or diagnostic pathway. A promoted stratum without its own MONDO term anchors
  to the parent term with `mapping_predicate: skos:narrowMatch` in
  `mappings.mondo_mappings` (never bare parent-term reuse), records overlap
  with non-disjoint sibling strata, and is covered by a `Grouping`.
- **Variant tiers** (exon 19 del vs L858R) are `has_subtypes` inside the
  stratum entry — unless therapy is variant-specific (KRAS G12C).
- **Stage is never an entry.** Metastatic/advanced disease is `stages:` on the
  parent plus `conforms_to` on the `invasion_and_metastasis` module — do not
  create `Metastatic_X` entries.
- **Pathways/hallmarks are never disease entries** — mechanisms live in
  `kb/modules/`; named multi-module frameworks live in
  `kb/module_collections/`.
- **Germline predisposition syndromes** (Li-Fraumeni, Lynch) follow the plain
  Mendelian lump/split rules; keep them separate from the somatic cancer
  entries they predispose to.

### Cancer Cell of Origin (derived, not a slot)

A neoplasm entry's **cell of origin is derived from its own pathograph** — there is
no `cell_of_origin:` slot and one should not be added (design decisions §3d). Mark
the node where the transforming lesion happened, and the cell of origin is that
node's `cell_types`:

```yaml
pathophysiology:
- name: KRAS Oncogene Activation
  genetic_context:
    variant_origin: SOMATIC          # <- this makes it the origin node
    functional_impact_category: GAIN_OF_FUNCTION
  cell_types:
  - preferred_term: pancreatic acinar cell
    term:
      id: CL:0002064
      label: pancreatic acinar cell
```

```bash
just check-cancer-origin                 # summary + the multi-origin worklist
just check-cancer-origin --format list   # every entry, one line each
just list-cancer-origin
```

Two rules identify the origin node, and both read a structured claim rather than
a naming convention: a somatic `genetic_context` (not restricted to root nodes —
a second-hit or transformation lesion is still a somatic event), or an
`environmental[].influences_mechanisms` link marking the node
`environmental_effect: TRIGGERS` for non-mutational initiation (HPV, H. pylori,
asbestos, UV). The exposure rule applies **only when no lesion is recorded**:
once the entry names the transforming event, the exposure is upstream context.

A **virally driven mechanism is not a lesion**: HPV E6/E7 or HTLV-1 Tax leaves
no host variant for `variant_origin` to describe (see the pathograph skill's
[activity-state guidance](../../pathograph/references/scale-and-state.md)), so those entries record the
initiating exposure instead — and marking them `SOMATIC` breaks the derivation,
since a recorded lesion suppresses the exposure rule.

There is deliberately **no fallback chain and no role-string reading**. An
earlier version had both, to cover entries that had not recorded their origin,
and they mis-fired — deriving macrophage and pancreatic stellate cell as the cell
of origin of pancreatic cancer from a chronic-inflammation node. The records were
marked instead (`just backfill-cancer-origin`), and an entry that does not say
where it starts is now reported as not saying it.

**Deriving more than one cell of origin is the lump/split signal**, reported and
never gated. It means a grouping wearing a Disease entry's clothes
(`Kidney_Sarcoma`, `Appendiceal_Neoplasm` — remedy a `Grouping`), a disease with
cell-of-origin subtypes (DLBCL's GCB/ABC — remedy `has_subtypes`), or an
unsettled origin (melanoma in congenital melanocytic nevus — remedy a note).

The check is **advisory** and runs inside `just qc`, exiting 0 because 128 of 252
assessed neoplasm entries are still unmarked; `--fail-on <CLASS>` or `--strict`
gates when you want one. `ORIGIN_WITHOUT_CELL` is currently at zero — every entry
that marks an origin binds a cell there — so that class is ready to become a real
gate.

**Backfilling.** `just backfill-cancer-origin [--bind-single-cell] [--apply]`
marks entries whose prose already states the lesion. It only marks a node whose
own **name** says mutation/fusion/translocation/amplification/inactivation —
never a pathway state, a germline variant, a microenvironment node, or an
acquired-resistance node ("ESR1 Mutation-Driven Endocrine Resistance" is a real
somatic event that happens years after the disease starts). Re-validate the
changed files with `just validate-disorders` afterwards.

**NCIT is a cross-check, never a binding target.** `NCIT:R104`
(Disease_Has_Normal_Cell_Origin), `NCIT:R112` and `NCIT:R105`
(Disease_Has_Abnormal_Cell, into the Abnormal Cell branch `NCIT:C12913`) are
ingested by `OntologyEdgeSource` into quotable `references_cache/NCIT_*.md` rows
— DLBCL is *Mature B-Lymphocyte* → *Neoplastic Large B-Lymphocyte*. `cell_types`
stays CL-only (`CellTypeTerm` is `reachable_from: CL:0000000`), and there is no
NCIT-to-CL mapping in the repo, so agreement is a curator's judgement rather than
a computed match. Worked examples: `Chronic_Myeloid_Leukemia`,
`Pancreatic_Ductal_Adenocarcinoma`. See
[`docs/cancer-cell-of-origin.md`](../../../../docs/cancer-cell-of-origin.md).
