"""
Export dismech disorder pathographs to CX2 for NDEx publication.
"""

from __future__ import annotations

import argparse
import html
import json
import logging
import os
import re
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import networkx as nx
import yaml
from ndex2.client import Ndex2
from ndex2.cx2 import CX2Network, CX2NetworkXFactory

from dismech.graph import (
    _build_section_lookup,
    _gene_lookup_keys,
    _iter_variant_items,
    _resolve_descriptor_target,
    build_causal_graph,
    graph_to_json,
)

logger = logging.getLogger(__name__)

DEFAULT_NDEX_VISIBILITY = "PUBLIC"
DEFAULT_SOURCE_REPO_URL = "https://github.com/monarch-initiative/dismech/blob/main"
_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "dismech.yaml"
IQUERY_GENE_SYMBOL_PATTERN = re.compile(
    r"^(?:hgnc\.symbol:)?(?:[A-Z][A-Z0-9-]*|C[0-9]+orf[0-9]+)$"
)
IQUERY_GENE_NODE_TYPE = "gene"
IQUERY_GENESET_NODE_TYPE = "proteinfamily"

NODE_TYPE_LABELS = {
    "pathophysiology": "Pathophysiology",
    "phenotype": "Phenotype",
    "environmental": "Environmental",
    "genetic": "Genetics / Variants",
    "treatment": "Treatment",
    "biochemical": "Biochemical",
    "experimental_model": "Experimental Model",
    "orphan": "Orphan",
    "unknown": "Unknown",
}

NODE_SORT_ORDER = {
    "genetic": 0,
    "treatment": 1,
    "environmental": 2,
    "pathophysiology": 3,
    "biochemical": 4,
    "phenotype": 5,
    "experimental_model": 6,
    "orphan": 7,
    "unknown": 8,
}


@dataclass(frozen=True)
class NodeStyle:
    fill_color: str
    border_color: str
    shape: str
    height: int
    min_width: int
    max_width: int
    label_font_size: int


@dataclass(frozen=True)
class EdgeStyle:
    color: str
    line_style: str
    target_arrow_shape: str
    width: int


NODE_STYLES = {
    "pathophysiology": NodeStyle(
        fill_color="#dbeafe",
        border_color="#93c5fd",
        shape="round-rectangle",
        height=48,
        min_width=150,
        max_width=260,
        label_font_size=12,
    ),
    "phenotype": NodeStyle(
        fill_color="#fef3c7",
        border_color="#fcd34d",
        shape="ellipse",
        height=48,
        min_width=140,
        max_width=240,
        label_font_size=12,
    ),
    "environmental": NodeStyle(
        fill_color="#dcfce7",
        border_color="#86efac",
        shape="diamond",
        height=58,
        min_width=150,
        max_width=240,
        label_font_size=11,
    ),
    "genetic": NodeStyle(
        fill_color="#f3e8ff",
        border_color="#c4b5fd",
        shape="hexagon",
        height=52,
        min_width=140,
        max_width=230,
        label_font_size=12,
    ),
    "treatment": NodeStyle(
        fill_color="#fce7f3",
        border_color="#f9a8d4",
        shape="rectangle",
        height=48,
        min_width=150,
        max_width=260,
        label_font_size=12,
    ),
    "biochemical": NodeStyle(
        fill_color="#e0e7ff",
        border_color="#a5b4fc",
        shape="ellipse",
        height=44,
        min_width=130,
        max_width=220,
        label_font_size=11,
    ),
    "experimental_model": NodeStyle(
        fill_color="#ccfbf1",
        border_color="#14b8a6",
        shape="round-rectangle",
        height=54,
        min_width=170,
        max_width=280,
        label_font_size=11,
    ),
    "orphan": NodeStyle(
        fill_color="#fee2e2",
        border_color="#dc2626",
        shape="round-rectangle",
        height=48,
        min_width=140,
        max_width=240,
        label_font_size=12,
    ),
    "unknown": NodeStyle(
        fill_color="#f3f4f6",
        border_color="#9ca3af",
        shape="round-rectangle",
        height=48,
        min_width=140,
        max_width=240,
        label_font_size=12,
    ),
}

EDGE_STYLE_BY_PREDICATE = {
    "causes": EdgeStyle(
        color="#6b7280",
        line_style="solid",
        target_arrow_shape="triangle",
        width=2,
    ),
    "leads_to": EdgeStyle(
        color="#92400e",
        line_style="solid",
        target_arrow_shape="triangle",
        width=2,
    ),
    "targets": EdgeStyle(
        color="#db2777",
        line_style="solid",
        target_arrow_shape="triangle",
        width=2,
    ),
    "treats": EdgeStyle(
        color="#db2777",
        line_style="dashed",
        target_arrow_shape="triangle",
        width=2,
    ),
    "models": EdgeStyle(
        color="#0f766e",
        line_style="dashed",
        target_arrow_shape="triangle",
        width=2,
    ),
    "contributes_to": EdgeStyle(
        color="#7c3aed",
        line_style="dashed",
        target_arrow_shape="triangle",
        width=2,
    ),
    "variant_of": EdgeStyle(
        color="#7c3aed",
        line_style="solid",
        target_arrow_shape="circle",
        width=2,
    ),
}

VISUAL_PROPERTIES = {
    "default": {
        "edge": {
            "EDGE_CURVED": True,
            "EDGE_LABEL_AUTOROTATE": False,
            "EDGE_LABEL_BACKGROUND_COLOR": "#FFFFFF",
            "EDGE_LABEL_BACKGROUND_OPACITY": 0,
            "EDGE_LABEL_COLOR": "#111827",
            "EDGE_LABEL_FONT_FACE": {
                "FONT_FAMILY": "sans-serif",
                "FONT_NAME": "SansSerif",
                "FONT_STYLE": "normal",
                "FONT_WEIGHT": "normal",
            },
            "EDGE_LABEL_FONT_SIZE": 9,
            "EDGE_LABEL_MAX_WIDTH": 180,
            "EDGE_LABEL_OPACITY": 1,
            "EDGE_LINE_COLOR": "#6b7280",
            "EDGE_LINE_STYLE": "solid",
            "EDGE_OPACITY": 1,
            "EDGE_SOURCE_ARROW_SHAPE": "none",
            "EDGE_TARGET_ARROW_COLOR": "#6b7280",
            "EDGE_TARGET_ARROW_SHAPE": "triangle",
            "EDGE_TARGET_ARROW_SIZE": 8,
            "EDGE_VISIBILITY": "element",
            "EDGE_WIDTH": 2,
        },
        "network": {
            "NETWORK_BACKGROUND_COLOR": "#FFFFFF",
        },
        "node": {
            "NODE_BACKGROUND_COLOR": "#FFFFFF",
            "NODE_BORDER_COLOR": "#D1D5DB",
            "NODE_BORDER_OPACITY": 1,
            "NODE_BORDER_STYLE": "solid",
            "NODE_BORDER_WIDTH": 1.5,
            "NODE_HEIGHT": 48,
            "NODE_LABEL_COLOR": "#111827",
            "NODE_LABEL_FONT_FACE": {
                "FONT_FAMILY": "sans-serif",
                "FONT_NAME": "SansSerif",
                "FONT_STYLE": "normal",
                "FONT_WEIGHT": "normal",
            },
            "NODE_LABEL_FONT_SIZE": 12,
            "NODE_LABEL_MAX_WIDTH": 200,
            "NODE_LABEL_OPACITY": 1,
            "NODE_LABEL_POSITION": {
                "HORIZONTAL_ALIGN": "center",
                "HORIZONTAL_ANCHOR": "center",
                "JUSTIFICATION": "center",
                "MARGIN_X": 0,
                "MARGIN_Y": 0,
                "VERTICAL_ALIGN": "center",
                "VERTICAL_ANCHOR": "center",
            },
            "NODE_SELECTED": False,
            "NODE_SHAPE": "round-rectangle",
            "NODE_VISIBILITY": "element",
            "NODE_WIDTH": 160,
            "NODE_X_LOCATION": 0,
            "NODE_Y_LOCATION": 0,
            "NODE_Z_LOCATION": 0,
        },
    },
    "edgeMapping": {
        "EDGE_LABEL": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "name", "type": "string"},
        },
        "EDGE_LINE_COLOR": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "line_color", "type": "string"},
        },
        "EDGE_LINE_STYLE": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "line_style", "type": "string"},
        },
        "EDGE_TARGET_ARROW_COLOR": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "line_color", "type": "string"},
        },
        "EDGE_TARGET_ARROW_SHAPE": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "target_arrow_shape", "type": "string"},
        },
        "EDGE_WIDTH": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "width", "type": "integer"},
        },
    },
    "nodeMapping": {
        "NODE_BACKGROUND_COLOR": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "fill_color", "type": "string"},
        },
        "NODE_BORDER_COLOR": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "border_color", "type": "string"},
        },
        "NODE_BORDER_STYLE": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "border_style", "type": "string"},
        },
        "NODE_HEIGHT": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "height", "type": "integer"},
        },
        "NODE_LABEL": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "name", "type": "string"},
        },
        "NODE_LABEL_FONT_SIZE": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "label_font_size", "type": "integer"},
        },
        "NODE_SHAPE": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "shape", "type": "string"},
        },
        "NODE_WIDTH": {
            "type": "PASSTHROUGH",
            "definition": {"attribute": "width", "type": "integer"},
        },
    },
}

VISUAL_EDITOR_PROPERTIES = {
    "properties": {
        "nodeSizeLocked": False,
        "arrowColorMatchesEdge": True,
        "nodeCustomGraphicsSizeSync": True,
    }
}


def load_disorder(yaml_path: Path) -> dict[str, Any]:
    """Load a disorder YAML file."""
    with open(yaml_path) as stream:
        data = yaml.safe_load(stream)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {yaml_path}")
    return data


@lru_cache(maxsize=1)
def _load_prefix_map() -> dict[str, str]:
    """Load CURIE prefix mappings from the schema."""
    if not _SCHEMA_PATH.exists():
        return {}
    data = yaml.safe_load(_SCHEMA_PATH.read_text())
    prefixes = data.get("prefixes", {}) if isinstance(data, dict) else {}
    return {
        prefix: base
        for prefix, base in prefixes.items()
        if isinstance(prefix, str) and isinstance(base, str)
    }


def curie_to_url(curie: str) -> str:
    """Convert a CURIE to a stable URL."""
    if not curie:
        return "#"
    if curie.startswith(("http://", "https://")):
        return curie
    if ":" not in curie:
        return "#"

    prefix, local_id = curie.split(":", 1)
    prefix_map = _load_prefix_map()
    base = prefix_map.get(prefix)
    if base:
        if "{id}" in base:
            return base.format(id=local_id)
        return f"{base}{local_id}"
    return f"https://bioregistry.io/{curie}"


def _humanize_enum(value: str | None) -> str:
    if not value:
        return ""
    return str(value).replace("_", " ").title()


def _format_link(url: str, label: str) -> str:
    return (
        f'<a href="{html.escape(url)}" target="_blank" '
        f'rel="noopener noreferrer">{html.escape(label)}</a>'
    )


def _format_curie_link(curie: str | None, *, label: str | None = None) -> str:
    if not curie:
        return ""
    link_label = label or curie
    return _format_link(curie_to_url(curie), link_label)


def _format_text_lines(lines: list[str]) -> str:
    if not lines:
        return ""
    return "<br>".join(html.escape(line) for line in lines)


def _descriptor_entries(descriptors: Any) -> list[dict[str, str]]:
    """Extract stable label/id pairs from a descriptor list."""
    if not isinstance(descriptors, list):
        return []

    entries: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for descriptor in descriptors:
        if not isinstance(descriptor, dict):
            continue
        term = descriptor.get("term")
        term_id = (
            str(term.get("id")) if isinstance(term, dict) and term.get("id") else ""
        )
        label_value = descriptor.get("preferred_term")
        if not label_value and isinstance(term, dict):
            label_value = term.get("label")
        label = str(label_value or term_id).strip()
        if not label and not term_id:
            continue
        key = (label, term_id)
        if key in seen:
            continue
        seen.add(key)
        entry = {"label": label}
        if term_id:
            entry["id"] = term_id
        entries.append(entry)
    return entries


def _format_descriptor_links(entries: list[dict[str, str]]) -> str:
    if not entries:
        return ""

    formatted: list[str] = []
    for entry in entries:
        label = entry["label"]
        term_id = entry.get("id")
        if term_id:
            formatted.append(_format_curie_link(term_id, label=f"{label} [{term_id}]"))
        else:
            formatted.append(html.escape(label))
    return "<br>".join(formatted)


def _format_evidence_list(evidence_items: list[dict[str, Any]] | None) -> str:
    """Format evidence items as compact HTML for NDEx tables."""
    if not evidence_items:
        return ""

    formatted_items: list[str] = []
    for evidence_item in evidence_items:
        if not isinstance(evidence_item, dict):
            continue

        parts: list[str] = []
        reference = evidence_item.get("reference")
        if reference:
            parts.append(_format_curie_link(str(reference)))

        supports = evidence_item.get("supports")
        if supports:
            parts.append(f"<strong>{html.escape(str(supports))}</strong>")

        evidence_source = evidence_item.get("evidence_source")
        if evidence_source:
            parts.append(html.escape(_humanize_enum(str(evidence_source))))

        body: list[str] = []
        if parts:
            body.append(" | ".join(parts))

        snippet = evidence_item.get("snippet")
        if snippet:
            body.append(html.escape(str(snippet)))

        explanation = evidence_item.get("explanation")
        if explanation:
            body.append(f"<em>{html.escape(str(explanation))}</em>")

        if body:
            formatted_items.append(f"<li>{'<br>'.join(body)}</li>")

    if not formatted_items:
        return ""
    return f"<ul>{''.join(formatted_items)}</ul>"


def _extract_disorder_term_id(disorder: dict[str, Any]) -> str | None:
    disease_term = disorder.get("disease_term")
    if not isinstance(disease_term, dict):
        return None
    term = disease_term.get("term")
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    return str(term_id) if term_id else None


def _extract_node_represents(
    disorder_item: dict[str, Any],
    *,
    node_type: str,
) -> str | None:
    """Extract the best identifier to attach to a node."""
    descriptor_paths_by_type = {
        "phenotype": [("phenotype_term", "term", "id")],
        "treatment": [("treatment_term", "term", "id")],
        "experimental_model": [("namo_type",)],
        "genetic": [("gene", "term", "id"), ("gene_term", "term", "id")],
    }
    for path in descriptor_paths_by_type.get(node_type, []):
        current: Any = disorder_item
        for key in path:
            if not isinstance(current, dict) or key not in current:
                current = None
                break
            current = current[key]
        if isinstance(current, str) and current:
            return current
    return None


def _normalize_iquery_gene_symbol(value: Any) -> str | None:
    """Normalize a candidate HGNC-style symbol for NDEx iQuery."""
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    if text.lower().startswith("hgnc.symbol:"):
        text = text.split(":", 1)[1]
    if IQUERY_GENE_SYMBOL_PATTERN.fullmatch(text) is None:
        return None
    return text


def _iquery_gene_symbols(
    *,
    node_name: str,
    node_type: str,
    meta: dict[str, Any],
) -> list[str]:
    candidates: list[Any] = []

    if node_type == "genetic":
        candidates.append(node_name)

    genes = meta.get("genes")
    if isinstance(genes, list):
        candidates.extend(genes)

    symbols: list[str] = []
    for candidate in candidates:
        symbol = _normalize_iquery_gene_symbol(candidate)
        if symbol and symbol not in symbols:
            symbols.append(symbol)
    return symbols


def _iquery_node_attributes(
    *,
    node_name: str,
    node_type: str,
    meta: dict[str, Any],
) -> dict[str, Any]:
    """Add NDEx/iQuery-compatible typing for nodes that reference genes."""
    symbols = _iquery_gene_symbols(node_name=node_name, node_type=node_type, meta=meta)
    if not symbols:
        return {}

    attributes: dict[str, Any] = {"iquery_gene_symbols": symbols}
    node_symbol = _normalize_iquery_gene_symbol(node_name)
    if node_type == "genetic" and len(symbols) == 1 and node_symbol == symbols[0]:
        attributes["type"] = IQUERY_GENE_NODE_TYPE
    else:
        attributes["type"] = IQUERY_GENESET_NODE_TYPE
        attributes["member"] = symbols
    return attributes


def _add_descriptor_link_attributes(
    attributes: dict[str, Any],
    disorder_item: dict[str, Any] | None,
) -> None:
    if not isinstance(disorder_item, dict):
        return

    field_specs = (
        ("cell_types", "cell_type_ids", "cell_type_urls", "cell_type_links"),
        (
            "biological_processes",
            "biological_process_ids",
            "biological_process_urls",
            "biological_process_links",
        ),
        (
            "molecular_functions",
            "molecular_function_ids",
            "molecular_function_urls",
            "molecular_function_links",
        ),
        ("locations", "location_ids", "location_urls", "location_links"),
    )

    for source_key, ids_key, urls_key, links_key in field_specs:
        entries = _descriptor_entries(disorder_item.get(source_key))
        if not entries:
            continue

        attributes.setdefault(source_key, [entry["label"] for entry in entries])

        term_ids = [entry["id"] for entry in entries if entry.get("id")]
        if term_ids:
            attributes[ids_key] = term_ids
            attributes[urls_key] = [curie_to_url(term_id) for term_id in term_ids]

        link_html = _format_descriptor_links(entries)
        if link_html:
            attributes[links_key] = link_html


def _node_width(style: NodeStyle, label: str) -> int:
    estimated = max(style.min_width, min(style.max_width, len(label) * 7 + 36))
    return estimated


def _guess_source_url(yaml_path: Path | None) -> str | None:
    if yaml_path is None:
        return None
    resolved = yaml_path.resolve()
    for parent in (resolved.parent, *resolved.parents):
        if (parent / ".git").exists():
            rel_path = resolved.relative_to(parent)
            return f"{DEFAULT_SOURCE_REPO_URL}/{rel_path.as_posix()}"
    return None


def _normalize_ndex_host(host: str | None) -> str | None:
    if not host:
        return None
    normalized = host.strip()
    if not normalized:
        return None
    if "://" not in normalized:
        normalized = f"https://{normalized}"
    return normalized.rstrip("/")


def _viewer_url_for_network(
    host: str | None, network_id: str, uploaded_url: str
) -> str:
    normalized_host = _normalize_ndex_host(host)
    if normalized_host:
        return f"{normalized_host}/viewer/networks/{network_id}"

    parsed = urlparse(uploaded_url)
    if parsed.scheme and parsed.netloc:
        return f"{parsed.scheme}://{parsed.netloc}/viewer/networks/{network_id}"
    return uploaded_url


def _append_unique(target: list[str], values: list[str] | None) -> None:
    if not values:
        return
    for value in values:
        if value and value not in target:
            target.append(value)


def _merge_edge_detail(
    target: dict[str, Any],
    source: dict[str, Any],
) -> None:
    if not target.get("description") and source.get("description"):
        target["description"] = source["description"]
    if not target.get("causal_link_type") and source.get("causal_link_type"):
        target["causal_link_type"] = source["causal_link_type"]
    if not target.get("treatment_effect") and source.get("treatment_effect"):
        target["treatment_effect"] = source["treatment_effect"]
    if not target.get("inference_basis") and source.get("inference_basis"):
        target["inference_basis"] = source["inference_basis"]

    if source.get("inferred"):
        target["inferred"] = True

    evidence = target.setdefault("evidence", [])
    for evidence_item in source.get("evidence") or []:
        if evidence_item not in evidence:
            evidence.append(evidence_item)

    hypothesis_groups = target.setdefault("hypothesis_groups", [])
    _append_unique(hypothesis_groups, source.get("hypothesis_groups"))

    intermediates = target.setdefault("intermediate_mechanisms", [])
    _append_unique(intermediates, source.get("intermediate_mechanisms"))


def _build_edge_detail_lookup(
    disorder: dict[str, Any],
) -> dict[tuple[str, str, str], dict[str, Any]]:
    """Collect rich edge-level metadata aligned with build_causal_graph()."""
    edge_detail_lookup: dict[tuple[str, str, str], dict[str, Any]] = {}

    def add_detail(
        source_name: str,
        target_name: str,
        predicate: str,
        detail: dict[str, Any],
    ) -> None:
        key = (source_name, target_name, predicate)
        existing = edge_detail_lookup.setdefault(key, {})
        _merge_edge_detail(existing, detail)

    phenotype_lookup = _build_section_lookup(
        disorder.get("phenotypes", []) or [],
        descriptor_key="phenotype_term",
    )

    pathophysiology_by_gene_key: dict[str, set[str]] = defaultdict(set)
    for item in disorder.get("pathophysiology", []) or []:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not name:
            continue
        for gene_key in _gene_lookup_keys(item):
            pathophysiology_by_gene_key[gene_key].add(name)

    genetic_nodes_by_gene_key: dict[str, set[str]] = defaultdict(set)
    for item in disorder.get("genetic", []) or []:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not name:
            continue
        for gene_key in _gene_lookup_keys(item, allow_name_fallback=True):
            genetic_nodes_by_gene_key[gene_key].add(name)

    for item in disorder.get("pathophysiology", []) or []:
        if not isinstance(item, dict):
            continue
        source_name = item.get("name")
        if not source_name:
            continue
        parent_evidence = item.get("evidence")
        for edge_item in item.get("downstream", []) or []:
            if not isinstance(edge_item, dict) or "target" not in edge_item:
                continue
            add_detail(
                source_name,
                str(edge_item["target"]),
                "causes",
                {
                    "description": edge_item.get("description"),
                    "evidence": edge_item.get("evidence") or parent_evidence,
                    "causal_link_type": edge_item.get("causal_link_type"),
                    "hypothesis_groups": edge_item.get("hypothesis_groups"),
                    "intermediate_mechanisms": edge_item.get("intermediate_mechanisms"),
                },
            )

    for item in disorder.get("phenotypes", []) or []:
        if not isinstance(item, dict):
            continue
        source_name = item.get("name")
        if not source_name:
            continue
        parent_evidence = item.get("evidence")
        for edge_item in item.get("sequelae", []) or []:
            if not isinstance(edge_item, dict) or "target" not in edge_item:
                continue
            add_detail(
                source_name,
                str(edge_item["target"]),
                "leads_to",
                {
                    "description": edge_item.get("description"),
                    "evidence": edge_item.get("evidence") or parent_evidence,
                    "causal_link_type": edge_item.get("causal_link_type"),
                    "hypothesis_groups": edge_item.get("hypothesis_groups"),
                    "intermediate_mechanisms": edge_item.get("intermediate_mechanisms"),
                },
            )

    for item in disorder.get("treatments", []) or []:
        if not isinstance(item, dict):
            continue
        source_name = item.get("name")
        if not source_name:
            continue
        parent_evidence = item.get("evidence")
        for target_item in item.get("target_mechanisms", []) or []:
            if not isinstance(target_item, dict) or "target" not in target_item:
                continue
            add_detail(
                source_name,
                str(target_item["target"]),
                "targets",
                {
                    "description": target_item.get("description"),
                    "evidence": target_item.get("evidence") or parent_evidence,
                    "treatment_effect": target_item.get("treatment_effect"),
                },
            )

        for descriptor in item.get("target_phenotypes", []) or []:
            if not isinstance(descriptor, dict):
                continue
            target_name = _resolve_descriptor_target(descriptor, phenotype_lookup)
            if not target_name:
                continue
            add_detail(
                source_name,
                target_name,
                "treats",
                {
                    "description": descriptor.get("description")
                    or item.get("description"),
                    "evidence": parent_evidence,
                },
            )

    for item in disorder.get("experimental_models", []) or []:
        if not isinstance(item, dict):
            continue
        source_name = item.get("name")
        if not source_name:
            continue
        parent_evidence = item.get("evidence")
        for target_item in item.get("modeled_mechanisms", []) or []:
            if not isinstance(target_item, dict) or "target" not in target_item:
                continue
            add_detail(
                source_name,
                str(target_item["target"]),
                "models",
                {
                    "description": target_item.get("description"),
                    "evidence": target_item.get("evidence") or parent_evidence,
                },
            )

    for item in disorder.get("genetic", []) or []:
        if not isinstance(item, dict):
            continue
        source_name = item.get("name")
        if not source_name:
            continue
        mechanism_targets: set[str] = set()
        for gene_key in _gene_lookup_keys(item, allow_name_fallback=True):
            mechanism_targets.update(pathophysiology_by_gene_key.get(gene_key, set()))
        for target_name in sorted(mechanism_targets):
            add_detail(
                source_name,
                target_name,
                "contributes_to",
                {
                    "description": "Inferred from shared gene identifiers between the genetic factor and pathophysiology node.",
                    "evidence": item.get("evidence"),
                    "inferred": True,
                    "inference_basis": "shared_gene_identifier",
                },
            )

    for parent_name, variant in _iter_variant_items(disorder):
        source_name = variant.get("name")
        if not source_name:
            continue

        genetic_targets: set[str] = set()
        if parent_name:
            genetic_targets.add(parent_name)
        for gene_key in _gene_lookup_keys(variant):
            genetic_targets.update(genetic_nodes_by_gene_key.get(gene_key, set()))

        if genetic_targets:
            inference_basis = (
                "nested_variant" if parent_name else "shared_gene_identifier"
            )
            for target_name in sorted(genetic_targets):
                add_detail(
                    source_name,
                    target_name,
                    "variant_of",
                    {
                        "description": "Variant linked to its parent or matching genetic factor.",
                        "evidence": variant.get("evidence"),
                        "inferred": True,
                        "inference_basis": inference_basis,
                    },
                )
            continue

        mechanism_targets: set[str] = set()
        for gene_key in _gene_lookup_keys(variant):
            mechanism_targets.update(pathophysiology_by_gene_key.get(gene_key, set()))
        for target_name in sorted(mechanism_targets):
            add_detail(
                source_name,
                target_name,
                "contributes_to",
                {
                    "description": "Inferred from shared gene identifiers between the variant and pathophysiology node.",
                    "evidence": variant.get("evidence"),
                    "inferred": True,
                    "inference_basis": "shared_gene_identifier",
                },
            )

    return edge_detail_lookup


def _node_attributes(
    node_payload: dict[str, Any],
    *,
    disorder_item: dict[str, Any] | None,
) -> dict[str, Any]:
    node_name = str(node_payload["id"])
    node_type = str(node_payload.get("node_type") or "unknown")
    is_orphan = bool(node_payload.get("is_orphan"))
    style = NODE_STYLES.get(node_type, NODE_STYLES["unknown"])

    border_color = "#dc2626" if is_orphan else style.border_color
    border_style = "dashed" if is_orphan else "solid"

    attributes: dict[str, Any] = {
        "name": node_name,
        "type": node_type,
        "dismech_type": node_type,
        "type_label": NODE_TYPE_LABELS.get(node_type, "Unknown"),
        "fill_color": node_payload.get("color") or style.fill_color,
        "border_color": border_color,
        "border_style": border_style,
        "shape": style.shape,
        "height": style.height,
        "width": _node_width(style, node_name),
        "label_font_size": style.label_font_size,
    }

    if is_orphan:
        attributes["is_orphan"] = True

    represents = (
        _extract_node_represents(disorder_item or {}, node_type=node_type)
        if disorder_item
        else None
    )
    if represents:
        attributes["represents"] = represents
        attributes["represents_url"] = curie_to_url(represents)

    description = node_payload.get("description")
    if description:
        attributes["description"] = description

    meta = node_payload.get("meta") or {}
    if not isinstance(meta, dict):
        meta = {}

    attributes.update(
        _iquery_node_attributes(node_name=node_name, node_type=node_type, meta=meta)
    )
    _add_descriptor_link_attributes(attributes, disorder_item)

    simple_list_fields = {
        "genes": "genes",
        "cell_types": "cell_types",
        "biological_processes": "biological_processes",
        "locations": "locations",
        "therapeutic_agents": "therapeutic_agents",
        "conditions": "conditions",
        "hypothesis_groups": "hypothesis_groups",
    }
    simple_scalar_fields = {
        "evidence_count": "evidence_count",
        "role": "role",
        "frequency": "frequency",
        "severity": "severity",
        "term_id": "term_id",
        "model_type": "model_type",
        "namo_type": "namo_type",
        "publication": "publication",
        "association": "association",
        "variant_count": "variant_count",
        "variant_type": "variant_type",
        "clinical_significance": "clinical_significance",
        "regulatory_category": "regulatory_category",
    }

    for source_key, target_key in simple_list_fields.items():
        value = meta.get(source_key)
        if isinstance(value, list) and value:
            attributes[target_key] = [str(item) for item in value if item is not None]

    for source_key, target_key in simple_scalar_fields.items():
        value = meta.get(source_key)
        if value is not None:
            attributes[target_key] = value

    if isinstance(meta.get("term_id"), str):
        attributes["term_url"] = curie_to_url(meta["term_id"])

    linked_models = meta.get("experimental_models")
    if isinstance(linked_models, list) and linked_models:
        attributes["linked_experimental_models"] = [
            str(item.get("name"))
            for item in linked_models
            if isinstance(item, dict) and item.get("name")
        ]

    pdb_structures = meta.get("pdb_structures")
    if isinstance(pdb_structures, list) and pdb_structures:
        attributes["pdb_ids"] = [
            str(item.get("pdb_id"))
            for item in pdb_structures
            if isinstance(item, dict) and item.get("pdb_id")
        ]

    return attributes


def _edge_style(
    predicate: str,
    detail: dict[str, Any],
    *,
    is_orphan: bool,
) -> EdgeStyle:
    if is_orphan:
        return EdgeStyle(
            color="#dc2626",
            line_style="dashed",
            target_arrow_shape="triangle",
            width=2,
        )

    style = EDGE_STYLE_BY_PREDICATE.get(
        predicate,
        EdgeStyle(
            color="#6b7280",
            line_style="solid",
            target_arrow_shape="triangle",
            width=2,
        ),
    )

    treatment_effect = str(detail.get("treatment_effect") or "")
    if predicate == "targets":
        if treatment_effect == "INHIBITS":
            return EdgeStyle(
                color="#dc2626",
                line_style="solid",
                target_arrow_shape="tee",
                width=2,
            )
        if treatment_effect in {"ACTIVATES", "RESTORES"}:
            return EdgeStyle(
                color="#16a34a",
                line_style="solid",
                target_arrow_shape="triangle",
                width=2,
            )
        if treatment_effect == "BYPASSES":
            return EdgeStyle(
                color="#2563eb",
                line_style="solid",
                target_arrow_shape="diamond",
                width=2,
            )

    causal_link_type = str(detail.get("causal_link_type") or "")
    if predicate in {"causes", "leads_to"} and causal_link_type.startswith("INDIRECT"):
        return EdgeStyle(
            color=style.color,
            line_style="dashed",
            target_arrow_shape=style.target_arrow_shape,
            width=style.width,
        )

    return style


def _edge_attributes(
    edge_payload: dict[str, Any],
    *,
    detail: dict[str, Any],
) -> dict[str, Any]:
    predicate = str(edge_payload["predicate"])
    style = _edge_style(
        predicate,
        detail,
        is_orphan=bool(edge_payload.get("is_orphan")),
    )
    attributes: dict[str, Any] = {
        "name": predicate.replace("_", " "),
        "predicate": predicate,
        "line_color": style.color,
        "line_style": style.line_style,
        "target_arrow_shape": style.target_arrow_shape,
        "width": style.width,
    }

    description = detail.get("description")
    if description:
        attributes["description"] = description

    evidence_html = _format_evidence_list(detail.get("evidence"))
    if evidence_html:
        attributes["Evidence"] = evidence_html

    causal_link_type = detail.get("causal_link_type")
    if causal_link_type:
        attributes["causal_link_type"] = causal_link_type

    treatment_effect = detail.get("treatment_effect")
    if treatment_effect:
        attributes["treatment_effect"] = treatment_effect

    hypothesis_groups = detail.get("hypothesis_groups")
    if hypothesis_groups:
        attributes["hypothesis_groups"] = hypothesis_groups

    intermediate_mechanisms = detail.get("intermediate_mechanisms")
    if intermediate_mechanisms:
        attributes["intermediate_mechanisms"] = intermediate_mechanisms

    if detail.get("inferred"):
        attributes["inferred"] = True
    if detail.get("inference_basis"):
        attributes["inference_basis"] = detail["inference_basis"]

    return attributes


def _network_description(
    disorder: dict[str, Any],
    *,
    disease_term_id: str | None,
    source_url: str | None,
) -> str:
    parts: list[str] = []
    description = disorder.get("description")
    if description:
        parts.append(f"<p>{html.escape(str(description))}</p>")
    meta_lines: list[str] = []
    if disease_term_id:
        meta_lines.append(f"Disease term: {_format_curie_link(disease_term_id)}")
    if source_url:
        meta_lines.append(_format_link(source_url, "Source YAML"))
    if meta_lines:
        parts.append(f"<p>{' | '.join(meta_lines)}</p>")
    return "".join(parts)


def _apply_layered_layout(cx2_network: CX2Network) -> None:
    """Apply a deterministic left-to-right layered layout without extra dependencies."""
    networkx_graph = CX2NetworkXFactory().get_graph(cx2_network)
    if not networkx_graph.nodes:
        return

    condensed = nx.condensation(networkx_graph)
    layer_nodes: dict[int, list[int]] = defaultdict(list)
    depth_by_component: dict[int, int] = {}

    for component in nx.topological_sort(condensed):
        predecessors = list(condensed.predecessors(component))
        if predecessors:
            depth_by_component[component] = max(
                depth_by_component[pred] + 1 for pred in predecessors
            )
        else:
            depth_by_component[component] = 0

        members = condensed.nodes[component].get("members", set())
        for node_id in members:
            layer_nodes[depth_by_component[component]].append(node_id)

    x_gap = 280
    y_gap = 120

    for layer, node_ids in layer_nodes.items():
        sorted_nodes = sorted(
            node_ids,
            key=lambda node_id: (
                NODE_SORT_ORDER.get(
                    str(
                        networkx_graph.nodes[node_id].get("dismech_type")
                        or networkx_graph.nodes[node_id].get("type")
                        or "unknown"
                    ),
                    99,
                ),
                str(networkx_graph.nodes[node_id].get("name") or node_id),
            ),
        )
        start_y = -((len(sorted_nodes) - 1) * y_gap) / 2
        for index, node_id in enumerate(sorted_nodes):
            node = cx2_network.get_node(node_id)
            node["x"] = layer * x_gap
            node["y"] = start_y + index * y_gap


def _apply_dot_layout(cx2_network: CX2Network) -> None:
    """Apply Graphviz dot layout if pydot/Graphviz are available."""
    networkx_graph = CX2NetworkXFactory().get_graph(cx2_network)
    if not networkx_graph.nodes:
        return

    networkx_graph.graph.clear()
    for node_id in networkx_graph.nodes:
        networkx_graph.nodes[node_id].clear()
    for edge_id in networkx_graph.edges:
        networkx_graph.edges[edge_id].clear()

    layout = nx.nx_pydot.pydot_layout(networkx_graph, prog="dot")
    if not layout:
        raise RuntimeError("Graphviz dot layout did not return node positions")

    x_scale = 2.0
    y_scale = 1.5
    max_x = max(position[0] for position in layout.values())
    max_y = max(position[1] for position in layout.values())

    for node_id, position in layout.items():
        node = cx2_network.get_node(node_id)
        node["x"] = (max_x - position[0]) * x_scale
        node["y"] = (max_y - position[1]) * y_scale


def _apply_layout(cx2_network: CX2Network, *, apply_dot_layout: bool) -> None:
    if apply_dot_layout:
        try:
            _apply_dot_layout(cx2_network)
            return
        except Exception as error:  # pragma: no cover - fallback path
            logger.warning(
                "Falling back to layered layout because dot layout failed: %s",
                error,
            )

    _apply_layered_layout(cx2_network)


def disorder_to_cx2(
    disorder: dict[str, Any],
    *,
    source_path: Path | None = None,
    apply_dot_layout: bool = False,
) -> list[dict[str, Any]]:
    """
    Convert a dismech disorder record into a CX2 network.
    """
    graph = build_causal_graph(disorder)
    if not graph.edges:
        raise ValueError("Disorder does not contain any pathograph edges to export")

    graph_payload = json.loads(graph_to_json(graph, disorder))
    edge_detail_lookup = _build_edge_detail_lookup(disorder)

    disease_term_id = _extract_disorder_term_id(disorder)
    source_url = _guess_source_url(source_path)

    cx2_network = CX2Network()
    network_name = str(
        disorder.get("name") or (source_path.stem if source_path else "dismech")
    )
    network_attributes = {
        "name": network_name,
        "description": _network_description(
            disorder,
            disease_term_id=disease_term_id,
            source_url=source_url,
        ),
    }
    if source_path:
        network_attributes["source_file"] = str(source_path)
    if disease_term_id:
        network_attributes["disease_term_id"] = disease_term_id
    if disorder.get("category"):
        network_attributes["category"] = disorder["category"]
    if disorder.get("creation_date"):
        network_attributes["creation_date"] = disorder["creation_date"]
    if disorder.get("updated_date"):
        network_attributes["updated_date"] = disorder["updated_date"]
    if source_url:
        network_attributes["prov:wasDerivedFrom"] = source_url

    cx2_network.set_network_attributes(network_attributes)
    cx2_network.add_network_attribute(
        "node_count", len(graph_payload["nodes"]), "integer"
    )
    cx2_network.add_network_attribute(
        "edge_count", len(graph_payload["edges"]), "integer"
    )
    if disease_term_id:
        cx2_network.add_network_attribute("labels", [disease_term_id], "list_of_string")

    item_lookup: dict[str, dict[str, Any]] = {}
    section_keys = [
        "pathophysiology",
        "phenotypes",
        "environmental",
        "genetic",
        "treatments",
        "biochemical",
        "experimental_models",
        "variants",
    ]
    for section_key in section_keys:
        for item in disorder.get(section_key, []) or []:
            if isinstance(item, dict) and item.get("name"):
                item_lookup[str(item["name"])] = item
    for _parent_name, variant in _iter_variant_items(disorder):
        if isinstance(variant, dict) and variant.get("name"):
            item_lookup[str(variant["name"])] = variant

    cx2_node_ids: dict[str, int] = {}
    for node_payload in graph_payload["nodes"]:
        node_name = str(node_payload["id"])
        cx2_node_ids[node_name] = cx2_network.add_node(
            attributes=_node_attributes(
                node_payload,
                disorder_item=item_lookup.get(node_name),
            )
        )

    for edge_payload in graph_payload["edges"]:
        source_name = str(edge_payload["source"])
        target_name = str(edge_payload["target"])
        predicate = str(edge_payload["predicate"])
        edge_key = (source_name, target_name, predicate)
        cx2_network.add_edge(
            source=cx2_node_ids[source_name],
            target=cx2_node_ids[target_name],
            attributes=_edge_attributes(
                edge_payload,
                detail=edge_detail_lookup.get(edge_key, {}),
            ),
        )

    cx2_network.set_visual_properties(VISUAL_PROPERTIES)
    cx2_network.set_opaque_aspect(
        "visualEditorProperties",
        [VISUAL_EDITOR_PROPERTIES],
    )
    _apply_layout(cx2_network, apply_dot_layout=apply_dot_layout)
    return cx2_network.to_cx2()


def dump_cx2(
    disorder_path: Path,
    *,
    output_path: Path | None = None,
    apply_dot_layout: bool = False,
) -> list[dict[str, Any]]:
    """Convert a disorder YAML file to CX2 and optionally write it to disk."""
    disorder = load_disorder(disorder_path)
    cx2 = disorder_to_cx2(
        disorder,
        source_path=disorder_path,
        apply_dot_layout=apply_dot_layout,
    )
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(cx2, indent=2))
    return cx2


def upload_cx2_to_ndex(
    cx2: list[dict[str, Any]],
    *,
    host: str | None = None,
    username: str | None = None,
    password: str | None = None,
    visibility: str = DEFAULT_NDEX_VISIBILITY,
) -> str:
    """Upload a CX2 network to NDEx and return the network URL."""
    resolved_host = _normalize_ndex_host(host or os.getenv("NDEX_HOST"))
    client = Ndex2(
        host=resolved_host,
        username=username or os.getenv("NDEX_USERNAME"),
        password=password or os.getenv("NDEX_PASSWORD"),
    )
    url = client.save_new_cx2_network(cx2, visibility=visibility)
    network_id = url.rsplit("/", 1)[-1]
    try:
        client.set_network_system_properties(network_id, {"index_level": "META"})
    except Exception as error:
        logger.warning(
            "Uploaded network %s but failed to set NDEx index_level=META: %s",
            network_id,
            error,
        )
    return _viewer_url_for_network(resolved_host, network_id, url)


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert a dismech disorder pathograph to NDEx CX2"
    )
    parser.add_argument("path", help="Input disorder YAML file")
    parser.add_argument(
        "--output",
        "-o",
        help="Output CX2 JSON path. Defaults to stdout when not uploading.",
    )
    parser.add_argument(
        "--dot-layout",
        action="store_true",
        help="Use Graphviz dot layout when available; otherwise fall back to layered layout.",
    )
    parser.add_argument(
        "--skip-empty",
        action="store_true",
        help="Exit successfully and print a skip message when the disorder has no pathograph edges.",
    )
    parser.add_argument(
        "--ndex-upload",
        action="store_true",
        help="Upload the converted CX2 network to NDEx.",
    )
    parser.add_argument(
        "--visibility",
        default=DEFAULT_NDEX_VISIBILITY,
        help=f"NDEx visibility for uploads (default: {DEFAULT_NDEX_VISIBILITY})",
    )
    parser.add_argument("--ndex-host", help="Override NDEX_HOST for uploads.")
    parser.add_argument("--ndex-username", help="Override NDEX_USERNAME for uploads.")
    parser.add_argument("--ndex-password", help="Override NDEX_PASSWORD for uploads.")
    args = parser.parse_args()

    disorder_path = Path(args.path)
    output_path = Path(args.output) if args.output else None
    try:
        cx2 = dump_cx2(
            disorder_path,
            output_path=output_path,
            apply_dot_layout=args.dot_layout,
        )
    except ValueError as error:
        if (
            args.skip_empty
            and str(error) == "Disorder does not contain any pathograph edges to export"
        ):
            print(f"Skipping {disorder_path}: {error}")
            return
        raise

    if args.ndex_upload:
        url = upload_cx2_to_ndex(
            cx2,
            host=args.ndex_host,
            username=args.ndex_username,
            password=args.ndex_password,
            visibility=args.visibility,
        )
        print(url)
        return

    if output_path is None:
        print(json.dumps(cx2, indent=2))
    else:
        print(f"Wrote CX2 to {output_path}")


if __name__ == "__main__":
    main()
