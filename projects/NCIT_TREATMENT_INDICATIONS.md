---
title: NCIT P302 Treatment Indications (Accepted_Therapeutic_Use_For)
status: IN_PROGRESS
tags:
  - treatments
  - structured-sources
  - completeness
  - ncit
description: >-
  Use the NCI Thesaurus NCIT:P302 (Accepted_Therapeutic_Use_For) annotation as
  structured, citable evidence for dismech treatment sections, and as a
  completeness signal for which accepted drug therapies are missing from
  disorder entries (and which indications map to diseases not yet curated).
---

# NCIT P302 Treatment Indications

`NCIT:P302` = **`Accepted_Therapeutic_Use_For`**:

> *"A property representing a disease or condition for which this drug is an
> accepted treatment. Used in the Drug, Food, Chemical or Biomedical Material
> branch."* (range `xsd:string`)

It links a drug NCIT concept to a **free-text description of the disease /
condition it is an accepted treatment for** — e.g. Midostaurin (`NCIT:C1872`) →
*"acute myeloid leukemia (AML) who are FLT3 mutation-positive (FLT3+)"*. **796**
NCIT drug/chemical concepts carry it.

This is the *indication*, not the molecular target. The coded molecular-target
relation in NCIT is a separate predicate (`NCIT:A7` `Has_Target`, e.g.
Midostaurin → FLT3 / PKC / VEGFR2); it is not ingested here but is a natural
follow-on for the same generic source.

## Two uses

1. **Evidence for treatments.** P302 is a curated NCI assertion (no PMID), so it
   is ingested as a **structured-database reference source** (like `ORPHA:`,
   `CGGV:`, `ICEES:`) rather than the PMID-snippet path. Each drug becomes one
   `references_cache/NCIT_<Cxxxx>.md` cache file holding a unified edge table:

   ```
   | ID | LABEL | PRED | TARGET_ID | TARGET_LABEL | METADATA |
   ```

   A curator cites the assertion directly:

   ```yaml
   treatments:
   - name: Midostaurin
     treatment_term:
       preferred_term: Pharmacotherapy
       term: { id: NCIT:C15986, label: Pharmacotherapy }
       therapeutic_agent:
       - preferred_term: midostaurin
         term: { id: NCIT:C1872, label: Midostaurin }
     evidence:
     - reference: NCIT:C1872
       supports: SUPPORT
       evidence_source: OTHER
       snippet: "Midostaurin | Accepted_Therapeutic_Use_For | - | - | acute myeloid leukemia (AML) who are FLT3 mutation-positive (FLT3+)"
       explanation: NCI Thesaurus asserts accepted therapeutic use for FLT3+ AML.
   ```

   The reference validator substring-checks the snippet against the cache file
   exactly as it does for ORPHA/ClinGen rows (verified: a wrong snippet fails,
   the exact row passes).

2. **Completeness checking.** The P302 indication string is **left verbatim**
   as the evidence snippet — it is *not* parsed. `scripts/ncit_p302_audit.py`
   therefore does a pure **identifier join on the drug** (NCIT concept id, or
   its ChEBI cross-reference via NCIT `P368`) against dismech
   `therapeutic_agent` ids, flagging each P302 drug
   `PRESENT_WITH_EVIDENCE` / `PRESENT_NO_EVIDENCE` / `ABSENT`.

## How it is built

The generic, manifest-driven `OntologyEdgeSource`
(`src/dismech/structured_sources/ontology_edges.py`) selects predicate edges out
of the OAK-managed `sqlite:obo:ncit` database — **the ontology `.db` is never
committed**; only the 796 selectively generated cache files are. The NCIT
selection is pinned in `data/ncit-edges/MANIFEST.yaml` (ontology version
`26.02d`, predicate `NCIT:P302`).

```bash
just ncit-edges-refresh                 # ensure OAK NCIT db present, check version
just ncit-edges-rebuild                 # regenerate all references_cache/NCIT_*.md
just ncit-edges-rebuild --id NCIT:C1872 # one drug
just ncit-p302-audit --format summary             # per-drug coverage digest
just ncit-p302-audit --format summary --by-class  # rolled up by NCIT is-a class
just ncit-p302-audit --format tsv --out output/ncit_p302_audit.tsv
```

## Audit snapshot (NCIT 26.02d)

The join is on **drug identity only** (no parsing of the indication text), so
these counts are exact, not heuristic. A committed snapshot of all 796 rows
lives at `projects/NCIT_TREATMENT_INDICATIONS/audit.tsv`.

- P302 drug assertions: **796**
- `PRESENT_WITH_EVIDENCE`: **5** — first curated batch (Temozolomide/Glioblastoma,
  Avelumab/Merkel cell carcinoma, Gefitinib/EGFR-mutant NSCLC,
  Vorinostat/mycosis fungoides, Vandetanib/medullary thyroid carcinoma).
- `PRESENT_NO_EVIDENCE`: **171** — drug already used as a dismech
  `therapeutic_agent`, P302 evidence not yet cited. **Immediately actionable**:
  drop `reference: NCIT:<drug>` + the verbatim P302 snippet onto the matching
  treatment record(s). Curator must confirm the indication string matches the
  disorder — e.g. Arsenic Trioxide's string says "acute myelocytic leukemia",
  *not* promyelocytic, so it does **not** support the APL entry.
- `ABSENT`: **620** — drug carries an accepted-use assertion but is not a
  `therapeutic_agent` in any disorder (treatment/disorder curation leads).

### Rolled up by NCIT is-a drug class (`--by-class`)

The flat list is more actionable rolled up by the NCIT `rdfs:subClassOf` drug
class (transitive named ancestors; anonymous OWL restrictions and universal
roots dropped). `present` = used as a dismech `therapeutic_agent`. This turns
"796 drugs" into class-level coverage and aligns mechanism classes to existing
modules via an advisory `module_hint`. Full table:
`projects/NCIT_TREATMENT_INDICATIONS/class_audit.tsv`. Examples:

| NCIT class | total | present | absent | module hint |
|---|--:|--:|--:|---|
| Immune Checkpoint Inhibitor (`NCIT:C143250`) | 14 | 9 | 5 | `immune_checkpoint_blockade` |
| Monoclonal Antibody (`NCIT:C20401`) | 87 | 33 | 54 | |
| Protein Kinase Inhibitor (`NCIT:C1404`) | 89 | 22 | 67 | |
| Macrolide Antibiotic (`NCIT:C261`) | 3 | 2 | 1 | `bacterial_protein_synthesis_inhibition` |
| Beta-Lactam Antibiotic (`NCIT:C260`) | 4 | 0 | 4 | `bacterial_cell_wall_synthesis_inhibition` |

87 classes with ≥3 drugs have **zero** dismech coverage (e.g. radiopharmaceuticals,
5-HT3/serotonin antagonists, bisphosphonates, anthracyclines) — class-level gaps.
The is-a rollup is a completeness/grouping lens only; is-a is **not** added to the
evidence cache files (it is classification metadata, not a therapeutic-use
assertion).

## Goal / "be complete"

- [x] Ingest all 796 P302 assertions as citable `NCIT:` cache files.
- [x] Generic `OntologyEdgeSource` + manifest + CLI + justfile.
- [x] Identifier-join completeness audit (drug id / ChEBI xref, no NER).
- [~] Add the verbatim P302 evidence to the **PRESENT_NO_EVIDENCE** drugs'
      existing treatment records (5 done, 171 remaining; confirm each
      indication string matches the disorder before citing).
- [ ] Triage the **620 ABSENT** drugs against the priority dashboard for new
      treatment / disorder curation, prioritising by is-a class gaps.
- [ ] Use `module_hint` classes to suggest `conforms_to` / `therapeutic_modality`
      for the matching treatments.
- [ ] Follow-on: add the coded `NCIT:A7` `Has_Target` predicate to the manifest
      so drug→molecular-target edges back target-based modules.
