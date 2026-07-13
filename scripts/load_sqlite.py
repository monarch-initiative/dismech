#!/usr/bin/env python
"""Partial shim toward a NORMALIZED relational load of the dismech KB.

Goal: compile the dismech schema to a normalized SQL schema (table-per-class
with foreign keys, as ``gen-sqltables`` produces) and load the KB YAML into
those tables via ``linkml-sqldb`` (``linkml.utils.sqlutils:main``).

Status: ``gen-sqltables`` (schema -> 173-table DDL) works, but the
``linkml-sqldb dump`` path (YAML -> rows) hits a *chain* of independent
blockers on this schema. Two are cleanly shimmable here (below); the rest are
structural mismatches between the schema and LinkML's SQLAlchemy generator
that a monkeypatch cannot robustly fix. This module installs the two clean
shims and documents the wall for the follow-up schema work.

Shimmed here (correct, low-risk):
  1. ``relationship`` slot-name collision. ``BiomarkerReadout`` / ``GeneSetLink``
     carry a slot literally named ``relationship``; ``gen-sqla`` emits it as a
     class attribute that shadows SQLAlchemy's ``relationship()`` builder in
     the same class body -> ``TypeError: 'Column' object is not callable``.
     Fixed by aliasing the import to ``relationship_`` and rewriting the call
     sites in the generated ORM source (DB column name ``relationship`` kept).
  2. Inlined-as-list single-key normalization. For a keyless inlined-list slot
     (``sequelae`` / ``downstream`` -> ``CausalEdge``), LinkML uses the range's
     first slot (``target``) as ``key_name``; a ``{target: "..."}`` entry hits
     a bug in ``_normalize_inlined`` that passes the dict positionally ->
     ``attribute target value ... does not match key``. Fixed by pre-building
     those entries as range objects before delegating.

NOT shimmable robustly (needs schema-level work -- see docs/reports):
  3. ``range: Any`` polymorphic scalar slots (``severity`` x34, ``frequency``
     x7, ``percentage``) are emitted as ``relationship("Any", ...)`` FKs but
     hold bare strings -> ``'extended_str' has no _sa_instance_state``. Can be
     rewritten to ``Text`` columns in the ORM, but then the ORM desyncs from
     the DDL (``SQLTableGenerator`` is a *separate* generator) ->
     ``no such column: Pathophysiology.frequency``. Both generators would have
     to be patched in lockstep.
  4. Shared identified objects. The same ``Term`` id (ontology CURIE) is
     referenced many times; the dumper inserts one row per occurrence ->
     ``UNIQUE constraint failed: Term.id``. Needs identity-map dedup
     (``session.merge`` direction) that the stock dumper does not do.
  5. Name-based cross-references (``target``, ``conforms_to``, ``subtype``,
     ``attaches_to``) are plain strings, not identifier FKs, so even once
     loaded they do not form real joins in a normalized model.
  6. Overlapping FKs: classes with several multivalued inlined collections of
     the same child class (``CriteriaSet`` -> ``CriteriaItem`` x6,
     ``Pathophysiology`` -> ``BiologicalProcessDescriptor`` x2) generate
     conflicting FK columns (7 SQLAlchemy ``overlaps`` warnings).

The durable fix for 3-6 is to harden the schema for relational normalization
(concrete ranges instead of ``Any``; identifier-typed references; disjoint
child collections) -- which also subsumes the ``relationship`` rename (1).

Usage mirrors ``linkml-sqldb`` (installs shims 1-2, then delegates)::

    uv run python scripts/load_sqlite.py dump \
        -s src/dismech/schema/dismech.yaml -C Disease \
        -D dismech.db --no-validate kb/disorders/Asthma.yaml

Note: with only shims 1-2, the dump still fails on blocker 3+; this module is
diagnostic groundwork, not yet a working end-to-end normalized loader.
"""

from __future__ import annotations

import sys

from jsonasobj2 import JsonObj, as_dict
from linkml.generators.sqlalchemygen import SQLAlchemyGenerator
from linkml_runtime.utils.yamlutils import YAMLRoot

# Original import line emitted by gen-sqla, and its de-shadowed replacement.
_ORIG_IMPORT = "from sqlalchemy.orm import relationship\n"
_ALIASED_IMPORT = "from sqlalchemy.orm import relationship as relationship_\n"


def _deshadow_relationship(code: str) -> str:
    """Rewrite generated ORM source so a ``relationship`` column attribute no
    longer shadows SQLAlchemy's ``relationship()`` builder.

    ``generate_sqla`` emits column attributes as ``relationship = Column(...)``
    and every relationship builder as ``<name> = relationship(...)``. Aliasing
    the import and rewriting the ``= relationship(`` call sites is unambiguous:
    the column declaration is ``relationship = Column(``, never a call.
    """
    if _ORIG_IMPORT not in code:
        # gen-sqla changed its import layout; fail loudly rather than silently
        # emitting broken code.
        raise RuntimeError(
            "load_sqlite shim: expected import line not found in generated "
            "SQLAlchemy code; the gen-sqla output format may have changed."
        )
    code = code.replace(_ORIG_IMPORT, _ALIASED_IMPORT)
    code = code.replace("= relationship(", "= relationship_(")
    return code


def _install_relationship_patch() -> None:
    """Blocker #1: de-shadow the ``relationship`` slot in generated ORM code."""
    _original = SQLAlchemyGenerator.generate_sqla

    def _patched(self, *args, **kwargs):
        return _deshadow_relationship(_original(self, *args, **kwargs))

    SQLAlchemyGenerator.generate_sqla = _patched


def _install_inlined_list_patch() -> None:
    """Blocker #2: fix inlined-as-list normalization of single-key entries.

    ``linkml-sqldb`` loads YAML through LinkML's legacy dataclass runtime
    (``YAMLRoot``). For an inlined-as-list slot whose range class has no
    identifier (e.g. ``sequelae`` / ``downstream`` -> ``CausalEdge``), LinkML
    uses the range's first slot as ``key_name`` (here ``target``). A list entry
    written as a single-key mapping ``{target: "..."}`` then hits a bug in
    ``linkml_runtime.utils.yamlutils._normalize_inlined``::

        order_up(list_entry[lek], slot_type(list_entry))   # dict passed positionally

    which builds ``CausalEdge(target={'target': '...'})`` and raises
    ``attribute target value ... does not match key``. We pre-convert those
    ambiguous single-key entries into fully constructed range objects before
    delegating, so the original method takes its unambiguous
    ``isinstance(list_entry, slot_type)`` path. Multi-key entries and other
    forms are left untouched.
    """
    _original = YAMLRoot._normalize_inlined

    def _patched(self, slot_name, slot_type, key_name, keyed, is_list):
        raw = self[slot_name]
        if isinstance(raw, list):
            fixed = []
            for entry in raw:
                if isinstance(entry, (dict, JsonObj)):
                    d = as_dict(entry)
                    if (
                        len(d) == 1
                        and key_name in d
                        and not isinstance(d[key_name], (list, dict, JsonObj))
                    ):
                        fixed.append(slot_type(**d))
                        continue
                fixed.append(entry)
            self[slot_name] = fixed
        return _original(self, slot_name, slot_type, key_name, keyed, is_list)

    YAMLRoot._normalize_inlined = _patched


def _install_patch() -> None:
    _install_relationship_patch()
    _install_inlined_list_patch()


def main() -> None:
    _install_patch()
    # Delegate to the real linkml-sqldb click group with argv untouched.
    from linkml.utils.sqlutils import main as sqldb_main

    sqldb_main()


if __name__ == "__main__":
    sys.exit(main())
