# Loading the dismech KB into a normalized SQL schema — status & blockers

**Date:** 2026-07-13
**Question:** LinkML can compile a schema to SQL and load YAML as tables. Does it
work for dismech, targeting a *normalized* relational schema (table-per-class
with foreign keys)?

**Short answer:** DDL generation works. The data load does **not** work
end-to-end yet: `linkml-sqldb dump` hits a chain of six independent blockers on
this schema. Two are cleanly shimmable (`scripts/load_sqlite.py`); the other
four are structural mismatches between the schema and LinkML's SQLAlchemy
generator and need schema-level changes.

## What works

| Step | Tool | Result |
|------|------|--------|
| Schema → SQL DDL (normalized, 173 tables) | `gen-sqltables` | ✅ works |
| Schema → SQLAlchemy ORM source | `gen-sqla` | ✅ generates (but see #1) |
| YAML → pydantic datamodel | `PydanticGenerator` | ✅ loads cleanly |
| YAML → jsonschema validation | `linkml-validate` | ✅ (this is why CI is green) |
| YAML → **normalized rows** | `linkml-sqldb dump` | ❌ blocked (below) |

`linkml-store` + DuckDB loads the whole KB and is queryable, but it stores each
Disease as one row with nested blobs — it does **not** normalize into
table-per-class with FKs, so it does not answer this question.

## The blocker chain (`linkml-sqldb dump`, target class `Disease`)

Each was hit in sequence; fixing one exposes the next.

1. **`relationship` slot-name collision.** `BiomarkerReadout` / `GeneSetLink`
   carry a slot literally named `relationship`. `gen-sqla` emits it as a class
   attribute that shadows SQLAlchemy's `relationship()` builder in the same
   class body → `TypeError: 'Column' object is not callable`.
   *Shimmable* — alias the import to `relationship_`, rewrite call sites
   (`scripts/load_sqlite.py`). Durable fix: rename the slot
   (`relationship` → e.g. `readout_relationship`) across schema + the handful
   of KB records that use it.

2. **Inlined-as-list single-key normalization.** For a keyless inlined-list
   slot (`sequelae` / `downstream` → `CausalEdge`), LinkML uses the range's
   first slot (`target`) as `key_name`; a `{target: "..."}` list entry hits a
   bug in `linkml_runtime`'s `_normalize_inlined` that passes the dict
   positionally → `attribute target value ... does not match key`.
   *Shimmable* — pre-build those entries as range objects before delegating.

3. **`range: Any` polymorphic scalar slots.** `severity` (34 classes),
   `frequency` (7), and `percentage` are declared `range: Any` and emitted as
   `relationship("Any", ...)` FKs, but the data holds bare strings/numbers
   (`"Severe"`, `"Occasional"`, `0.1`) → `'extended_str' object has no
   attribute '_sa_instance_state'`. Rewriting them to `Text` columns in the ORM
   makes the ORM desync from the DDL — `SQLTableGenerator` is a *separate*
   generator — → `no such column: Pathophysiology.frequency`. **Not robustly
   shimmable.** Durable fix: give these slots concrete ranges (a string, or a
   single enum) instead of `Any`.

4. **Shared identified objects not deduped.** The same `Term` id (ontology
   CURIE, e.g. `MONDO:0004979`) is referenced many times across one disease;
   the dumper inserts a row per occurrence → `UNIQUE constraint failed:
   Term.id`. Needs identity-map dedup (`session.merge`) that the stock dumper
   does not do.

5. **Name-based cross-references are not FKs.** `target`, `conforms_to`,
   `subtype`, `attaches_to` are plain strings referencing other objects by
   name, not identifier-typed FKs. Even once loaded they do not form real joins
   in a normalized model — you would `JOIN ON CausalEdge.target = Phenotype.name`
   by string equality. Durable fix: model references with identifier-typed
   ranges so LinkML emits real FKs.

6. **Overlapping foreign keys.** Classes with several multivalued inlined
   collections of the same child class — `CriteriaSet` → `CriteriaItem` (×6),
   `Pathophysiology` → `BiologicalProcessDescriptor` (×2) — generate
   conflicting FK columns (7 SQLAlchemy `overlaps` warnings). Durable fix:
   disjoint child classes per collection, or `overlaps`/back-population in the
   schema.

## Recommendation

There are two viable routes to a genuinely queryable normalized DB:

- **A — Harden the schema for relational normalization** (preferred). Address
  #3 (concrete ranges), #5 (identifier-typed references), #6 (disjoint child
  collections), and fold in the #1 `relationship` rename. Then `linkml-sqldb`
  loads natively and the FKs are real. This is real but bounded schema work and
  is independent of day-to-day curation.

- **B — Custom ETL.** Use the pydantic datamodel (which parses the KB cleanly)
  to walk objects and INSERT into a `gen-sqltables` DDL with explicit term
  dedup and string-ref → FK resolution. More code, but full control and real
  joins without waiting on schema changes.

`scripts/load_sqlite.py` installs the two clean shims (#1, #2) and documents the
wall; it is diagnostic groundwork, not yet an end-to-end loader.
