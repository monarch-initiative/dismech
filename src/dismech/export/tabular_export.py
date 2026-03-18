"""
Generic tabular export of disorder YAML annotations/assertions.

The exporter flattens top-level list sections (for example, phenotypes,
pathophysiology, treatments) into relational-style TSV tables:

- disorders.tsv: one row per disorder file
- assertions.tsv: one row per section item
- descriptors.tsv: descriptor objects attached to assertions
- evidence.tsv: evidence items attached to assertions (including nested contexts)

Optional:
- per-section TSV tables under output/sections/<section>/
- DuckDB database with master tables and per-section tables
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

ASSERTION_BASE_COLUMNS = [
    "assertion_id",
    "disorder_id",
    "disorder_name",
    "source_file",
    "section",
    "section_index",
    "name",
    "description",
    "category",
    "frequency",
    "diagnostic",
    "context",
    "subtype",
    "role",
    "presence",
    "association",
]

DESCRIPTOR_COLUMNS = [
    "descriptor_id",
    "assertion_id",
    "disorder_id",
    "disorder_name",
    "source_file",
    "section",
    "section_index",
    "section_name",
    "section_description",
    "path",
    "root_field",
    "parent_path",
    "parent_name",
    "parent_description",
    "preferred_term",
    "term_id",
    "term_label",
    "description",
    "raw_json",
]

EVIDENCE_COLUMNS = [
    "evidence_id",
    "assertion_id",
    "disorder_id",
    "disorder_name",
    "source_file",
    "section",
    "section_index",
    "path",
    "evidence_index",
    "reference",
    "supports",
    "evidence_source",
    "snippet",
    "explanation",
    "raw_json",
]

POSTCOMPOSITION_COLUMNS = [
    "postcomposition_id",
    "descriptor_id",
    "assertion_id",
    "disorder_id",
    "disorder_name",
    "source_file",
    "section",
    "section_index",
    "section_name",
    "section_description",
    "descriptor_path",
    "descriptor_preferred_term",
    "descriptor_term_id",
    "descriptor_term_label",
    "relation_type",
    "relation_index",
    "relation_path",
    "predicate_preferred_term",
    "predicate_term_id",
    "predicate_term_label",
    "value_preferred_term",
    "value_term_id",
    "value_term_label",
    "value_literal",
    "raw_json",
]

DISORDER_COLUMNS = [
    "disorder_id",
    "disorder_name",
    "source_file",
    "category",
    "disease_term_id",
    "disease_term_label",
    "parents_json",
    "raw_json",
]


@dataclass
class LoadedDisorder:
    """In-memory representation of one disorder YAML file."""

    disorder_id: int
    source_file: str
    data: dict[str, Any]


@dataclass
class ExportSummary:
    """Summary counters returned by export operations."""

    disorder_count: int
    section_count: int
    assertion_count: int
    descriptor_count: int
    evidence_count: int
    postcomposition_count: int
    sections: list[str]


class TabularExporter:
    """Export disorder YAML content into generic tabular files."""

    def discover_disorder_files(self, input_dir: Path, include_history: bool = False) -> list[Path]:
        """Return disorder YAML files from input_dir."""
        files = sorted(input_dir.glob("*.yaml"))
        if include_history:
            return files
        return [path for path in files if not path.name.endswith(".history.yaml")]

    def load_disorders(self, disorder_files: list[Path]) -> list[LoadedDisorder]:
        """Parse YAML files into dictionaries."""
        loaded: list[LoadedDisorder] = []
        for disorder_id, file_path in enumerate(disorder_files, start=1):
            with open(file_path) as stream:
                data = yaml.safe_load(stream) or {}
            if not isinstance(data, dict):
                continue
            loaded.append(LoadedDisorder(disorder_id=disorder_id, source_file=file_path.name, data=data))
        return loaded

    def discover_sections(self, loaded_disorders: list[LoadedDisorder]) -> list[str]:
        """Detect top-level list-of-object sections (assertion collections)."""
        sections: set[str] = set()
        for loaded in loaded_disorders:
            for key, value in loaded.data.items():
                if isinstance(value, list) and any(isinstance(item, dict) for item in value):
                    sections.add(key)
        return sorted(sections)

    def export(
        self,
        disorder_files: list[Path],
        output_dir: Path,
        sections: list[str] | None = None,
        write_section_files: bool = True,
        duckdb_path: Path | None = None,
    ) -> ExportSummary:
        """Export disorders to TSV and optional DuckDB."""
        loaded_disorders = self.load_disorders(disorder_files)
        discovered_sections = self.discover_sections(loaded_disorders)
        if sections is None:
            selected_sections = discovered_sections
        else:
            unknown_sections = [section for section in sections if section not in discovered_sections]
            if unknown_sections:
                known = ", ".join(discovered_sections)
                unknown = ", ".join(unknown_sections)
                raise ValueError(f"Unknown section(s): {unknown}. Known sections: {known}")
            selected_sections = sections

        disorder_rows = [self._build_disorder_row(loaded) for loaded in loaded_disorders]
        assertion_rows, descriptor_rows, evidence_rows, postcomposition_rows = self._build_annotation_rows(
            loaded_disorders, selected_sections
        )
        self._apply_postcomposition_to_descriptors(descriptor_rows, postcomposition_rows)

        output_dir.mkdir(parents=True, exist_ok=True)

        assertions_fieldnames = self._build_assertion_fieldnames(assertion_rows)
        descriptor_fieldnames = self._build_descriptor_fieldnames(descriptor_rows)
        self._write_tsv(output_dir / "disorders.tsv", DISORDER_COLUMNS, disorder_rows)
        self._write_tsv(output_dir / "assertions.tsv", assertions_fieldnames, assertion_rows)
        self._write_tsv(output_dir / "descriptors.tsv", descriptor_fieldnames, descriptor_rows)
        self._write_tsv(output_dir / "evidence.tsv", EVIDENCE_COLUMNS, evidence_rows)
        self._write_tsv(output_dir / "descriptor_postcomposition.tsv", POSTCOMPOSITION_COLUMNS, postcomposition_rows)

        if write_section_files:
            self._write_section_files(
                output_dir=output_dir,
                sections=selected_sections,
                assertions=assertion_rows,
                assertions_fieldnames=assertions_fieldnames,
                descriptors=descriptor_rows,
                descriptor_fieldnames=descriptor_fieldnames,
                evidence=evidence_rows,
                postcomposition=postcomposition_rows,
            )

        if duckdb_path is not None:
            self._write_duckdb(output_dir=output_dir, duckdb_path=duckdb_path, sections=selected_sections)

        return ExportSummary(
            disorder_count=len(disorder_rows),
            section_count=len(selected_sections),
            assertion_count=len(assertion_rows),
            descriptor_count=len(descriptor_rows),
            evidence_count=len(evidence_rows),
            postcomposition_count=len(postcomposition_rows),
            sections=selected_sections,
        )

    def _build_disorder_row(self, loaded: LoadedDisorder) -> dict[str, Any]:
        disease_term = loaded.data.get("disease_term")
        term_id = ""
        term_label = ""
        if isinstance(disease_term, dict):
            term = disease_term.get("term")
            if isinstance(term, dict):
                term_id = term.get("id", "") or ""
                term_label = term.get("label", "") or ""

        return {
            "disorder_id": loaded.disorder_id,
            "disorder_name": loaded.data.get("name", "") or "",
            "source_file": loaded.source_file,
            "category": loaded.data.get("category", "") or "",
            "disease_term_id": term_id,
            "disease_term_label": term_label,
            "parents_json": self._json_dumps(loaded.data.get("parents", [])),
            "raw_json": self._json_dumps(loaded.data),
        }

    def _build_annotation_rows(
        self,
        loaded_disorders: list[LoadedDisorder],
        sections: list[str],
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
        assertions: list[dict[str, Any]] = []
        descriptors: list[dict[str, Any]] = []
        evidence_rows: list[dict[str, Any]] = []
        postcomposition_rows: list[dict[str, Any]] = []
        assertion_id = 1
        descriptor_id = 1
        evidence_id = 1
        postcomposition_id = 1

        for loaded in loaded_disorders:
            disorder_name = loaded.data.get("name", "") or ""

            for section in sections:
                section_items = loaded.data.get(section)
                if not isinstance(section_items, list):
                    continue

                for section_index, item in enumerate(section_items):
                    if not isinstance(item, dict):
                        continue

                    scalar_fields, complex_fields = self._split_assertion_fields(item)

                    assertion_row = {
                        "assertion_id": assertion_id,
                        "disorder_id": loaded.disorder_id,
                        "disorder_name": disorder_name,
                        "source_file": loaded.source_file,
                        "section": section,
                        "section_index": section_index,
                        "name": scalar_fields.get("name", "") or "",
                        "description": scalar_fields.get("description", "") or "",
                        "category": scalar_fields.get("category", "") or "",
                        "frequency": scalar_fields.get("frequency", "") or "",
                        "diagnostic": scalar_fields.get("diagnostic", ""),
                        "context": scalar_fields.get("context", "") or "",
                        "subtype": scalar_fields.get("subtype", "") or "",
                        "role": scalar_fields.get("role", "") or "",
                        "presence": scalar_fields.get("presence", "") or "",
                        "association": scalar_fields.get("association", "") or "",
                        "scalar_fields_json": self._json_dumps(scalar_fields),
                        "complex_fields_json": self._json_dumps(complex_fields),
                        "raw_json": self._json_dumps(item),
                        "_scalar_fields": scalar_fields,
                    }
                    for scalar_key, scalar_value in scalar_fields.items():
                        assertion_row[scalar_key] = scalar_value
                    assertions.append(assertion_row)

                    descriptor_hits: list[tuple[tuple[str | int, ...], dict[str, Any]]] = []
                    evidence_hits: list[tuple[tuple[str | int, ...], int, dict[str, Any]]] = []
                    self._walk_assertion(item, (), None, descriptor_hits, evidence_hits)

                    for path_tokens, descriptor in descriptor_hits:
                        term = descriptor.get("term")
                        if not isinstance(term, dict):
                            term = {}
                        parent_tokens, parent_obj = self._parent_context(item, path_tokens)
                        parent_name = parent_obj.get("name", "") if isinstance(parent_obj, dict) else ""
                        parent_description = parent_obj.get("description", "") if isinstance(parent_obj, dict) else ""
                        descriptor_path = self._format_path(path_tokens)
                        descriptor_preferred_term = descriptor.get("preferred_term", "") or ""
                        descriptor_term_id = term.get("id", "") or ""
                        descriptor_term_label = term.get("label", "") or ""
                        descriptors.append(
                            {
                                "descriptor_id": descriptor_id,
                                "assertion_id": assertion_id,
                                "disorder_id": loaded.disorder_id,
                                "disorder_name": disorder_name,
                                "source_file": loaded.source_file,
                                "section": section,
                                "section_index": section_index,
                                "section_name": assertion_row.get("name", "") or "",
                                "section_description": assertion_row.get("description", "") or "",
                                "path": descriptor_path,
                                "root_field": self._root_field(path_tokens),
                                "parent_path": self._format_path(parent_tokens),
                                "parent_name": parent_name or "",
                                "parent_description": parent_description or "",
                                "preferred_term": descriptor_preferred_term,
                                "term_id": descriptor_term_id,
                                "term_label": descriptor_term_label,
                                "description": descriptor.get("description", "") or "",
                                "raw_json": self._json_dumps(descriptor),
                            }
                        )

                        descriptor_context = {
                            "assertion_id": assertion_id,
                            "disorder_id": loaded.disorder_id,
                            "disorder_name": disorder_name,
                            "source_file": loaded.source_file,
                            "section": section,
                            "section_index": section_index,
                            "section_name": assertion_row.get("name", "") or "",
                            "section_description": assertion_row.get("description", "") or "",
                            "descriptor_path": descriptor_path,
                            "descriptor_preferred_term": descriptor_preferred_term,
                            "descriptor_term_id": descriptor_term_id,
                            "descriptor_term_label": descriptor_term_label,
                        }

                        created_rows = self._extract_postcomposition_rows(
                            start_id=postcomposition_id,
                            descriptor_id=descriptor_id,
                            descriptor=descriptor,
                            context=descriptor_context,
                        )
                        postcomposition_rows.extend(created_rows)
                        postcomposition_id += len(created_rows)
                        descriptor_id += 1

                    for path_tokens, evidence_index, evidence_item in evidence_hits:
                        evidence_rows.append(
                            {
                                "evidence_id": evidence_id,
                                "assertion_id": assertion_id,
                                "disorder_id": loaded.disorder_id,
                                "disorder_name": disorder_name,
                                "source_file": loaded.source_file,
                                "section": section,
                                "section_index": section_index,
                                "path": self._format_path(path_tokens),
                                "evidence_index": evidence_index,
                                "reference": evidence_item.get("reference", "") or "",
                                "supports": evidence_item.get("supports", "") or "",
                                "evidence_source": evidence_item.get("evidence_source", "") or "",
                                "snippet": evidence_item.get("snippet", "") or "",
                                "explanation": evidence_item.get("explanation", "") or "",
                                "raw_json": self._json_dumps(evidence_item),
                            }
                        )
                        evidence_id += 1

                    assertion_id += 1

        for row in assertions:
            row.pop("_scalar_fields", None)

        return assertions, descriptors, evidence_rows, postcomposition_rows

    def _split_assertion_fields(self, item: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
        scalar_fields: dict[str, Any] = {}
        complex_fields: dict[str, Any] = {}

        for key, value in item.items():
            if key == "evidence":
                continue

            if self._is_primitive(value):
                scalar_fields[key] = self._normalize_scalar(value)
                continue

            if self._is_descriptor(value, key):
                continue

            if isinstance(value, list) and value and all(self._is_descriptor(v, key) for v in value):
                continue

            complex_fields[key] = value

        return scalar_fields, complex_fields

    def _walk_assertion(
        self,
        value: Any,
        path_tokens: tuple[str | int, ...],
        key_hint: str | None,
        descriptor_hits: list[tuple[tuple[str | int, ...], dict[str, Any]]],
        evidence_hits: list[tuple[tuple[str | int, ...], int, dict[str, Any]]],
    ) -> None:
        if self._is_descriptor(value, key_hint):
            descriptor_hits.append((path_tokens, value))
            # Continue traversal to catch nested descriptors, but do not recurse into
            # the term object itself.
            for key, child in value.items():
                if key == "term":
                    continue
                child_path = path_tokens + (key,)
                self._walk_assertion(child, child_path, key, descriptor_hits, evidence_hits)
            return

        if isinstance(value, dict):
            for key, child in value.items():
                child_path = path_tokens + (key,)
                if key == "evidence":
                    if isinstance(child, list):
                        for evidence_index, evidence_item in enumerate(child):
                            if isinstance(evidence_item, dict):
                                evidence_hits.append((child_path, evidence_index, evidence_item))
                    elif isinstance(child, dict):
                        evidence_hits.append((child_path, 0, child))
                    continue
                self._walk_assertion(child, child_path, key, descriptor_hits, evidence_hits)
            return

        if isinstance(value, list):
            for index, child in enumerate(value):
                child_path = path_tokens + (index,)
                self._walk_assertion(child, child_path, key_hint, descriptor_hits, evidence_hits)

    def _build_assertion_fieldnames(self, assertions: list[dict[str, Any]]) -> list[str]:
        reserved = set(ASSERTION_BASE_COLUMNS) | {"scalar_fields_json", "complex_fields_json", "raw_json"}
        dynamic_scalar_keys: set[str] = set()
        for row in assertions:
            scalar_fields = json.loads(row.get("scalar_fields_json", "{}"))
            dynamic_scalar_keys.update(scalar_fields.keys())
        dynamic_columns = sorted(key for key in dynamic_scalar_keys if key not in reserved)
        return ASSERTION_BASE_COLUMNS + dynamic_columns + ["scalar_fields_json", "complex_fields_json", "raw_json"]

    def _write_section_files(
        self,
        output_dir: Path,
        sections: list[str],
        assertions: list[dict[str, Any]],
        assertions_fieldnames: list[str],
        descriptors: list[dict[str, Any]],
        descriptor_fieldnames: list[str],
        evidence: list[dict[str, Any]],
        postcomposition: list[dict[str, Any]],
    ) -> None:
        sections_root = output_dir / "sections"
        for section in sections:
            section_slug = self._slug(section)
            section_dir = sections_root / section_slug
            section_dir.mkdir(parents=True, exist_ok=True)

            assertion_subset = [row for row in assertions if row.get("section") == section]
            descriptor_subset = [row for row in descriptors if row.get("section") == section]
            evidence_subset = [row for row in evidence if row.get("section") == section]
            postcomposition_subset = [row for row in postcomposition if row.get("section") == section]

            self._write_tsv(section_dir / "assertions.tsv", assertions_fieldnames, assertion_subset)
            self._write_tsv(section_dir / "descriptors.tsv", descriptor_fieldnames, descriptor_subset)
            self._write_tsv(section_dir / "evidence.tsv", EVIDENCE_COLUMNS, evidence_subset)
            self._write_tsv(
                section_dir / "descriptor_postcomposition.tsv", POSTCOMPOSITION_COLUMNS, postcomposition_subset
            )

    def _build_descriptor_fieldnames(self, descriptors: list[dict[str, Any]]) -> list[str]:
        dynamic_keys: set[str] = set()
        base = set(DESCRIPTOR_COLUMNS)
        for row in descriptors:
            dynamic_keys.update(key for key in row.keys() if key not in base)
        return DESCRIPTOR_COLUMNS + sorted(dynamic_keys)

    def _apply_postcomposition_to_descriptors(
        self,
        descriptors: list[dict[str, Any]],
        postcomposition_rows: list[dict[str, Any]],
    ) -> None:
        by_descriptor_id: dict[int, list[dict[str, Any]]] = {}
        for row in postcomposition_rows:
            try:
                descriptor_id = int(row.get("descriptor_id", 0))
            except (TypeError, ValueError):
                continue
            by_descriptor_id.setdefault(descriptor_id, []).append(row)

        for descriptor in descriptors:
            try:
                descriptor_id = int(descriptor.get("descriptor_id", 0))
            except (TypeError, ValueError):
                continue
            rows = by_descriptor_id.get(descriptor_id, [])
            if not rows:
                continue
            self._apply_descriptor_postcomposition_values(descriptor, rows)

    def _apply_descriptor_postcomposition_values(
        self,
        descriptor: dict[str, Any],
        rows: list[dict[str, Any]],
    ) -> None:
        aggregated: dict[str, list[str]] = {}

        for row in rows:
            relation_type = str(row.get("relation_type", "") or "")
            value_label = str(row.get("value_term_label", "") or "")
            value_preferred = str(row.get("value_preferred_term", "") or "")
            value_literal = str(row.get("value_literal", "") or "")
            value_id = str(row.get("value_term_id", "") or "")
            value_text = value_label or value_preferred or value_literal

            if relation_type == "modifier":
                self._append_if_value(aggregated, "postcomp_modifier", value_text or value_literal)
            elif relation_type == "laterality":
                self._append_if_value(aggregated, "postcomp_laterality", value_text or value_literal)
            elif relation_type == "located_in":
                self._append_if_value(aggregated, "postcomp_located_in", value_text)
                self._append_if_value(aggregated, "postcomp_located_in_ids", value_id)
            elif relation_type == "therapeutic_agent":
                self._append_if_value(aggregated, "postcomp_therapeutic_agent", value_text)
                self._append_if_value(aggregated, "postcomp_therapeutic_agent_ids", value_id)
            elif relation_type == "qualifier":
                predicate_label = str(row.get("predicate_term_label", "") or row.get("predicate_preferred_term", "") or "")
                predicate_id = str(row.get("predicate_term_id", "") or "")
                if not predicate_label:
                    predicate_label = predicate_id or "unknown_predicate"
                predicate_slug = self._slug(predicate_label)
                value_col = f"qualifier_{predicate_slug}"
                value_id_col = f"{value_col}_ids"
                self._append_if_value(aggregated, value_col, value_text)
                self._append_if_value(aggregated, value_id_col, value_id)
                self._append_if_value(aggregated, f"{value_col}_predicate_ids", predicate_id)

        for key, values in aggregated.items():
            descriptor[key] = "; ".join(self._unique_preserve_order(values))

    @staticmethod
    def _append_if_value(aggregated: dict[str, list[str]], key: str, value: str) -> None:
        if value:
            aggregated.setdefault(key, []).append(value)

    @staticmethod
    def _unique_preserve_order(values: list[str]) -> list[str]:
        seen: set[str] = set()
        ordered: list[str] = []
        for value in values:
            if value not in seen:
                ordered.append(value)
                seen.add(value)
        return ordered

    def _write_tsv(self, path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fieldnames, delimiter="\t", extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                writer.writerow({field: self._to_tsv_cell(row.get(field, "")) for field in fieldnames})

    def _write_duckdb(self, output_dir: Path, duckdb_path: Path, sections: list[str]) -> None:
        try:
            import duckdb  # type: ignore
        except ImportError as error:
            raise RuntimeError(
                "DuckDB support requires the 'duckdb' package. "
                "Try running with the embeddings group: uv run --group embeddings ..."
            ) from error

        duckdb_path.parent.mkdir(parents=True, exist_ok=True)
        connection = duckdb.connect(str(duckdb_path))
        try:
            self._create_duckdb_table(connection, "disorders", output_dir / "disorders.tsv")
            self._create_duckdb_table(connection, "assertions", output_dir / "assertions.tsv")
            self._create_duckdb_table(connection, "descriptors", output_dir / "descriptors.tsv")
            self._create_duckdb_table(connection, "evidence", output_dir / "evidence.tsv")
            self._create_duckdb_table(
                connection, "descriptor_postcomposition", output_dir / "descriptor_postcomposition.tsv"
            )

            used_table_names: set[str] = set()
            for section in sections:
                section_table = self._unique_identifier(self._slug(section), used_table_names)
                section_literal = section.replace("'", "''")
                connection.execute(
                    f"CREATE OR REPLACE TABLE assertions__{section_table} AS "
                    f"SELECT * FROM assertions WHERE section = '{section_literal}'"
                )
                connection.execute(
                    f"CREATE OR REPLACE TABLE descriptors__{section_table} AS "
                    f"SELECT * FROM descriptors WHERE section = '{section_literal}'"
                )
                connection.execute(
                    f"CREATE OR REPLACE TABLE evidence__{section_table} AS "
                    f"SELECT * FROM evidence WHERE section = '{section_literal}'"
                )
                connection.execute(
                    f"CREATE OR REPLACE TABLE descriptor_postcomposition__{section_table} AS "
                    f"SELECT * FROM descriptor_postcomposition WHERE section = '{section_literal}'"
                )

            connection.execute(
                "CREATE OR REPLACE VIEW section_counts AS "
                "SELECT section, COUNT(*) AS assertion_count "
                "FROM assertions GROUP BY section ORDER BY assertion_count DESC"
            )
            connection.execute(
                "CREATE OR REPLACE VIEW descriptor_postcomposition_pivot AS "
                "SELECT "
                "descriptor_id, "
                "MIN(disorder_name) AS disorder_name, "
                "MIN(source_file) AS source_file, "
                "MIN(section) AS section, "
                "MIN(section_name) AS section_name, "
                "MIN(descriptor_path) AS descriptor_path, "
                "MIN(descriptor_term_id) AS descriptor_term_id, "
                "MIN(descriptor_term_label) AS descriptor_term_label, "
                "MIN(value_term_label) FILTER (WHERE relation_type = 'located_in') AS located_in_term_label, "
                "MIN(value_literal) FILTER (WHERE relation_type = 'laterality') AS laterality, "
                "MIN(value_literal) FILTER (WHERE relation_type = 'modifier') AS modifier, "
                "STRING_AGG(value_term_label, '; ' ORDER BY relation_index) FILTER (WHERE relation_type = 'therapeutic_agent') AS therapeutic_agents, "
                "STRING_AGG(predicate_term_label, '; ' ORDER BY relation_index) FILTER (WHERE relation_type = 'qualifier') AS qualifier_predicates, "
                "STRING_AGG(value_term_label, '; ' ORDER BY relation_index) FILTER (WHERE relation_type = 'qualifier') AS qualifier_values "
                "FROM descriptor_postcomposition "
                "GROUP BY descriptor_id"
            )
        finally:
            connection.close()

    def _extract_postcomposition_rows(
        self,
        start_id: int,
        descriptor_id: int,
        descriptor: dict[str, Any],
        context: dict[str, Any],
    ) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        next_id = start_id
        descriptor_path = context.get("descriptor_path", "")

        def descriptor_fields(value: Any) -> tuple[str, str, str]:
            if not isinstance(value, dict):
                return "", "", ""
            term = value.get("term")
            if not isinstance(term, dict):
                term = {}
            return (
                value.get("preferred_term", "") or "",
                term.get("id", "") or "",
                term.get("label", "") or "",
            )

        def add_row(
            relation_type: str,
            relation_index: int,
            relation_path: str,
            *,
            predicate_preferred_term: str = "",
            predicate_term_id: str = "",
            predicate_term_label: str = "",
            value_preferred_term: str = "",
            value_term_id: str = "",
            value_term_label: str = "",
            value_literal: str = "",
            raw_value: Any = None,
        ) -> None:
            nonlocal next_id
            rows.append(
                {
                    "postcomposition_id": next_id,
                    "descriptor_id": descriptor_id,
                    **context,
                    "relation_type": relation_type,
                    "relation_index": relation_index,
                    "relation_path": relation_path,
                    "predicate_preferred_term": predicate_preferred_term,
                    "predicate_term_id": predicate_term_id,
                    "predicate_term_label": predicate_term_label,
                    "value_preferred_term": value_preferred_term,
                    "value_term_id": value_term_id,
                    "value_term_label": value_term_label,
                    "value_literal": value_literal,
                    "raw_json": self._json_dumps(raw_value),
                }
            )
            next_id += 1

        modifier = descriptor.get("modifier")
        if modifier not in (None, ""):
            add_row(
                relation_type="modifier",
                relation_index=0,
                relation_path=f"{descriptor_path}.modifier",
                predicate_preferred_term="modifier",
                value_literal=str(modifier),
                raw_value=modifier,
            )

        laterality = descriptor.get("laterality")
        if laterality not in (None, ""):
            add_row(
                relation_type="laterality",
                relation_index=0,
                relation_path=f"{descriptor_path}.laterality",
                predicate_preferred_term="laterality",
                value_literal=str(laterality),
                raw_value=laterality,
            )

        located_in = descriptor.get("located_in")
        if isinstance(located_in, dict):
            located_pref, located_id, located_label = descriptor_fields(located_in)
            add_row(
                relation_type="located_in",
                relation_index=0,
                relation_path=f"{descriptor_path}.located_in",
                predicate_preferred_term="located_in",
                value_preferred_term=located_pref,
                value_term_id=located_id,
                value_term_label=located_label,
                raw_value=located_in,
            )

        therapeutic_agent = descriptor.get("therapeutic_agent")
        if isinstance(therapeutic_agent, dict):
            therapeutic_items = [therapeutic_agent]
        elif isinstance(therapeutic_agent, list):
            therapeutic_items = [value for value in therapeutic_agent if isinstance(value, dict)]
        else:
            therapeutic_items = []
        for index, therapeutic_value in enumerate(therapeutic_items):
            therapeutic_pref, therapeutic_id, therapeutic_label = descriptor_fields(therapeutic_value)
            add_row(
                relation_type="therapeutic_agent",
                relation_index=index,
                relation_path=f"{descriptor_path}.therapeutic_agent[{index}]",
                predicate_preferred_term="therapeutic_agent",
                value_preferred_term=therapeutic_pref,
                value_term_id=therapeutic_id,
                value_term_label=therapeutic_label,
                raw_value=therapeutic_value,
            )

        qualifiers = descriptor.get("qualifiers")
        if isinstance(qualifiers, list):
            for index, qualifier in enumerate(qualifiers):
                if not isinstance(qualifier, dict):
                    continue
                predicate = qualifier.get("predicate")
                value = qualifier.get("value")
                predicate_pref, predicate_id, predicate_label = descriptor_fields(predicate)
                value_pref, value_id, value_label = descriptor_fields(value)
                value_literal = ""
                if value in (None, ""):
                    value_literal = ""
                elif not isinstance(value, dict):
                    value_literal = str(value)
                add_row(
                    relation_type="qualifier",
                    relation_index=index,
                    relation_path=f"{descriptor_path}.qualifiers[{index}]",
                    predicate_preferred_term=predicate_pref,
                    predicate_term_id=predicate_id,
                    predicate_term_label=predicate_label,
                    value_preferred_term=value_pref,
                    value_term_id=value_id,
                    value_term_label=value_label,
                    value_literal=value_literal,
                    raw_value=qualifier,
                )

        return rows

    def _create_duckdb_table(self, connection: Any, table_name: str, tsv_path: Path) -> None:
        path_literal = str(tsv_path.resolve()).replace("\\", "/").replace("'", "''")
        connection.execute(
            f"CREATE OR REPLACE TABLE {table_name} AS "
            f"SELECT * FROM read_csv_auto('{path_literal}', delim='\\t', header=true, sample_size=-1)"
        )

    @staticmethod
    def _is_primitive(value: Any) -> bool:
        return value is None or isinstance(value, str | int | float | bool | date | datetime)

    @staticmethod
    def _normalize_scalar(value: Any) -> Any:
        if isinstance(value, datetime | date):
            return value.isoformat()
        return value

    @staticmethod
    def _is_descriptor(value: Any, key_hint: str | None) -> bool:
        if not isinstance(value, dict):
            return False
        if "preferred_term" in value:
            return True
        if any(key in value for key in ("modifier", "located_in", "laterality", "qualifiers", "therapeutic_agent")):
            return True
        if key_hint and key_hint.endswith("_term"):
            term = value.get("term")
            if isinstance(term, dict) and ("id" in term or "label" in term):
                return True
        return False

    @staticmethod
    def _format_path(path_tokens: tuple[str | int, ...]) -> str:
        if not path_tokens:
            return "$"
        parts: list[str] = []
        for token in path_tokens:
            if isinstance(token, int):
                if not parts:
                    parts.append(f"[{token}]")
                else:
                    parts[-1] = f"{parts[-1]}[{token}]"
            else:
                parts.append(token)
        return ".".join(parts)

    @staticmethod
    def _root_field(path_tokens: tuple[str | int, ...]) -> str:
        for token in path_tokens:
            if isinstance(token, str):
                return token
        return ""

    def _parent_context(self, item: dict[str, Any], path_tokens: tuple[str | int, ...]) -> tuple[tuple[str | int, ...], Any]:
        if not path_tokens:
            return (), item
        parent_tokens = path_tokens[:-1]
        return parent_tokens, self._resolve_path(item, parent_tokens)

    @staticmethod
    def _resolve_path(value: Any, path_tokens: tuple[str | int, ...]) -> Any:
        current = value
        for token in path_tokens:
            if isinstance(token, str):
                if isinstance(current, dict):
                    current = current.get(token)
                else:
                    return None
            elif isinstance(token, int):
                if isinstance(current, list) and 0 <= token < len(current):
                    current = current[token]
                else:
                    return None
        return current

    @staticmethod
    def _json_default(value: Any) -> str:
        if isinstance(value, datetime | date):
            return value.isoformat()
        return str(value)

    def _json_dumps(self, value: Any) -> str:
        return json.dumps(value, sort_keys=True, ensure_ascii=False, default=self._json_default)

    @staticmethod
    def _to_tsv_cell(value: Any) -> Any:
        if isinstance(value, datetime | date):
            return value.isoformat()
        return "" if value is None else value

    @staticmethod
    def _slug(value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9_]+", "_", value.strip().lower()).strip("_")
        if not slug:
            slug = "section"
        if slug[0].isdigit():
            slug = f"s_{slug}"
        return slug

    @staticmethod
    def _unique_identifier(base: str, used: set[str]) -> str:
        candidate = base
        suffix = 2
        while candidate in used:
            candidate = f"{base}_{suffix}"
            suffix += 1
        used.add(candidate)
        return candidate


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Export disorder YAML assertions as TSV and DuckDB")
    parser.add_argument("--input-dir", "-i", default="kb/disorders", help="Directory with disorder YAML files")
    parser.add_argument("--output-dir", "-o", default="output/tabular", help="Directory for TSV output")
    parser.add_argument(
        "--sections",
        nargs="+",
        help="Optional explicit section names (e.g. phenotypes treatments pathophysiology)",
    )
    parser.add_argument(
        "--include-history",
        action="store_true",
        help="Include *.history.yaml files (default: exclude)",
    )
    parser.add_argument(
        "--duckdb",
        help="Optional path to write a DuckDB database (e.g. output/tabular/dismech.duckdb)",
    )
    parser.add_argument(
        "--no-section-files",
        action="store_true",
        help="Do not create per-section TSV tables under output/sections/",
    )
    args = parser.parse_args()

    exporter = TabularExporter()
    disorder_files = exporter.discover_disorder_files(Path(args.input_dir), include_history=args.include_history)
    if not disorder_files:
        raise SystemExit(f"No YAML files found in {args.input_dir}")

    try:
        summary = exporter.export(
            disorder_files=disorder_files,
            output_dir=Path(args.output_dir),
            sections=args.sections,
            write_section_files=not args.no_section_files,
            duckdb_path=Path(args.duckdb) if args.duckdb else None,
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error

    print(f"Exported {summary.disorder_count} disorders from {args.input_dir}")
    print(
        "Generated "
        f"{summary.assertion_count} assertions, "
        f"{summary.descriptor_count} descriptors, "
        f"{summary.evidence_count} evidence rows, "
        f"{summary.postcomposition_count} postcomposition rows "
        f"across {summary.section_count} sections"
    )
    print(f"TSV output: {Path(args.output_dir)}")
    if args.duckdb:
        print(f"DuckDB output: {args.duckdb}")


if __name__ == "__main__":
    main()
