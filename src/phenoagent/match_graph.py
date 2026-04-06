"""Render an augmented causal graph from a dismech model + matching report."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
from html import escape as html_escape
import json
import re
from pathlib import Path
from typing import Any

import yaml

from dismech.graph import build_causal_graph
from phenoagent.matching import resolve_disease_reference


@dataclass
class _PhenotypeRecord:
    name: str
    term_id: str | None
    labels_norm: set[str]


@dataclass
class _Node:
    node_id: str
    label: str
    class_name: str


_CORE_CLASS_BY_TYPE = {
    "pathophysiology": "core_pathophysiology",
    "environmental": "core_environmental",
    "genetic": "core_genetic",
    "treatment": "core_treatment",
    "biochemical": "core_biochemical",
}

_MODEL_STATUS_PRIORITY = {
    "model_unmatched": 1,
    "model_related": 2,
    "model_exact_absent": 3,
    "model_exact_present": 4,
}

_NO_EXPLANATION_ID = "NO_EXPLANATION"


def _normalize(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(str(value).casefold().split())


def _escape_label(value: str) -> str:
    return value.replace('"', "'")


def _safe_mermaid_id(raw: str) -> str:
    token = re.sub(r"[^A-Za-z0-9_]+", "_", raw.strip())
    token = token.strip("_")
    if not token:
        token = "node"
    if not token[0].isalpha():
        token = f"N_{token}"
    return token


def _trim(text: str | None, *, max_len: int = 100) -> str:
    if not text:
        return ""
    text = str(text).strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def _load_yaml_object(path: Path) -> dict[str, Any]:
    with open(path) as stream:
        data = yaml.safe_load(stream)
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML object at {path}")
    return data


def _summarize_matching_run(matching_run: dict[str, Any]) -> dict[str, int]:
    summary = {
        "total_rows": 0,
        "exact_present": 0,
        "exact_absent": 0,
        "related": 0,
        "unmatched": 0,
        "model_only": 0,
        "case_only": 0,
        "non_exact_total": 0,
        "non_exact_unresolved": 0,
        "temporary_explanation_rows": 0,
        "explanations_total": 0,
        "explanations_referenced": 0,
    }

    explanations = matching_run.get("explanations")
    if isinstance(explanations, list):
        summary["explanations_total"] = sum(1 for item in explanations if isinstance(item, dict))

    matches = matching_run.get("matches")
    if not isinstance(matches, list):
        return summary

    referenced_explanations: set[str] = set()

    for row in matches:
        if not isinstance(row, dict):
            continue
        summary["total_rows"] += 1

        has_case = bool(row.get("case_term_id") or row.get("case_label"))
        has_model = bool(row.get("model_term_id") or row.get("model_label"))
        if has_case and not has_model:
            summary["case_only"] += 1
        if has_model and not has_case:
            summary["model_only"] += 1

        exact = row.get("exact") is True
        if exact:
            if row.get("case_present") is False:
                summary["exact_absent"] += 1
            else:
                summary["exact_present"] += 1
            continue

        summary["non_exact_total"] += 1
        related = bool(row.get("case_is_broader")) or bool(row.get("case_is_narrower")) or bool(row.get("case_is_close"))
        if related:
            summary["related"] += 1
        else:
            summary["unmatched"] += 1

        pointer = row.get("explanation_for_no_match")
        if isinstance(pointer, str) and pointer:
            referenced_explanations.add(pointer)
            if pointer.startswith("TEMP_"):
                summary["temporary_explanation_rows"] += 1
        if not isinstance(pointer, str) or not pointer or pointer == _NO_EXPLANATION_ID:
            summary["non_exact_unresolved"] += 1

    summary["explanations_referenced"] = len(referenced_explanations)
    return summary


def _format_pr(value: Any) -> str:
    if value is None:
        return "NA"
    try:
        return f"{float(value):.6g}"
    except (TypeError, ValueError):
        return str(value)


def _extract_phenotype_records(disorder: dict[str, Any]) -> list[_PhenotypeRecord]:
    records: list[_PhenotypeRecord] = []
    for item in disorder.get("phenotypes", []) or []:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not isinstance(name, str) or not name.strip():
            continue

        term_id = None
        term_labels: list[str] = [name]
        descriptor = item.get("phenotype_term")
        if isinstance(descriptor, dict):
            preferred = descriptor.get("preferred_term")
            if isinstance(preferred, str) and preferred.strip():
                term_labels.append(preferred)
            term = descriptor.get("term")
            if isinstance(term, dict):
                tid = term.get("id")
                if isinstance(tid, str) and tid.strip():
                    term_id = tid.strip()
                tlabel = term.get("label")
                if isinstance(tlabel, str) and tlabel.strip():
                    term_labels.append(tlabel)

        records.append(
            _PhenotypeRecord(
                name=name,
                term_id=term_id,
                labels_norm={_normalize(label) for label in term_labels if label},
            )
        )
    return records


def _format_model_label(name: str, term_id: str | None) -> str:
    if term_id:
        return f"MODEL: {name}<br/>[{term_id}]"
    return f"MODEL: {name}"


def _format_case_label(row: dict[str, Any], fallback_idx: int) -> str:
    present = row.get("case_present")
    sign = "+" if present is True else "-" if present is False else "?"
    term_id = row.get("case_term_id")
    label = row.get("case_label") or term_id or f"row_{fallback_idx}"
    if term_id and label != term_id:
        return f"CASE {sign} {label}<br/>[{term_id}]"
    return f"CASE {sign} {label}"


def _format_explanation_label(explanation: dict[str, Any]) -> str:
    explanation_id = explanation.get("explanation_id") or "UNKNOWN_EXPLANATION"
    pr = explanation.get("estimated_probability")
    if pr is None:
        pr_text = "NA"
    else:
        try:
            pr_text = f"{float(pr):.3g}"
        except (TypeError, ValueError):
            pr_text = str(pr)
    summary = _trim(explanation.get("description"), max_len=90)
    if summary:
        return f"EXP: {explanation_id}<br/>Pr={pr_text}<br/>{summary}"
    return f"EXP: {explanation_id}<br/>Pr={pr_text}"


def _row_model_status(row: dict[str, Any]) -> str | None:
    if not row.get("model_term_id") and not row.get("model_label"):
        return None
    if row.get("exact") is True:
        if row.get("case_present") is False:
            return "model_exact_absent"
        return "model_exact_present"
    if bool(row.get("case_is_broader")) or bool(row.get("case_is_narrower")) or bool(row.get("case_is_close")):
        return "model_related"
    return "model_unmatched"


def _relation_edge_style(row: dict[str, Any]) -> str:
    if row.get("exact") is True:
        return "-->"
    return "-.->"


def _classify_case_node(row: dict[str, Any]) -> str:
    present = row.get("case_present")
    if present is True:
        return "case_present"
    if present is False:
        return "case_absent"
    return "case_unknown"


def _resolve_model_node_for_row(
    row: dict[str, Any],
    *,
    term_to_model_node: dict[str, str],
    label_to_model_node: dict[str, str],
    synthetic_model_nodes: dict[str, _Node],
) -> str | None:
    model_term_id = row.get("model_term_id")
    if isinstance(model_term_id, str) and model_term_id in term_to_model_node:
        return term_to_model_node[model_term_id]

    model_label = row.get("model_label")
    if isinstance(model_label, str):
        normalized = _normalize(model_label)
        if normalized in label_to_model_node:
            return label_to_model_node[normalized]

    if not model_term_id and not model_label:
        return None

    synthetic_key = f"{model_term_id or ''}|{model_label or ''}"
    if synthetic_key in synthetic_model_nodes:
        return synthetic_model_nodes[synthetic_key].node_id

    display = model_label or model_term_id or "Unknown model phenotype"
    if isinstance(model_term_id, str) and model_term_id:
        label = f"MODEL: {display}<br/>[{model_term_id}]"
    else:
        label = f"MODEL: {display}"
    node_id = f"model_extra_{_safe_mermaid_id(synthetic_key)}"
    synthetic_model_nodes[synthetic_key] = _Node(node_id=node_id, label=label, class_name="model_unmatched")
    return node_id


def generate_matching_causal_mermaid(disorder: dict[str, Any], matching_run: dict[str, Any]) -> str:
    """Generate Mermaid for disease causal graph overlaid with matching status."""
    graph = build_causal_graph(disorder)
    phenotypes = _extract_phenotype_records(disorder)

    phenotype_by_name = {record.name: record for record in phenotypes}
    term_to_model_node: dict[str, str] = {}
    label_to_model_node: dict[str, str] = {}

    core_nodes: dict[str, _Node] = {}
    model_nodes: dict[str, _Node] = {}
    orphan_nodes: dict[str, _Node] = {}
    case_nodes: dict[str, _Node] = {}
    explanation_nodes: dict[str, _Node] = {}
    synthetic_model_nodes: dict[str, _Node] = {}

    graph_name_to_node_id: dict[str, str] = {}
    model_status_by_node: dict[str, str] = {}

    for name, node_info in sorted(graph.nodes.items(), key=lambda item: item[0]):
        if node_info.node_type == "phenotype":
            node_id = f"model_{_safe_mermaid_id(name)}"
            phenotype_meta = phenotype_by_name.get(name)
            term_id = phenotype_meta.term_id if phenotype_meta else None
            model_nodes[node_id] = _Node(
                node_id=node_id,
                label=_format_model_label(name, term_id),
                class_name="model_unmatched",
            )
            if phenotype_meta:
                if phenotype_meta.term_id:
                    term_to_model_node[phenotype_meta.term_id] = node_id
                for label_norm in phenotype_meta.labels_norm:
                    if label_norm:
                        label_to_model_node[label_norm] = node_id
            else:
                label_to_model_node[_normalize(name)] = node_id
        else:
            class_name = _CORE_CLASS_BY_TYPE.get(node_info.node_type, "core_other")
            node_id = f"core_{_safe_mermaid_id(name)}"
            core_nodes[node_id] = _Node(node_id=node_id, label=name, class_name=class_name)
        graph_name_to_node_id[name] = node_id

    for orphan_name in sorted(graph.orphan_targets):
        node_id = f"orphan_{_safe_mermaid_id(orphan_name)}"
        orphan_nodes[node_id] = _Node(node_id=node_id, label=f"ORPHAN: {orphan_name}", class_name="orphan")
        graph_name_to_node_id[orphan_name] = node_id

    explanations = matching_run.get("explanations", [])
    if isinstance(explanations, list):
        for explanation in explanations:
            if not isinstance(explanation, dict):
                continue
            explanation_id = explanation.get("explanation_id")
            if not isinstance(explanation_id, str) or not explanation_id:
                continue
            node_id = f"exp_{_safe_mermaid_id(explanation_id)}"
            class_name = "explanation_default" if explanation_id == _NO_EXPLANATION_ID else "explanation"
            explanation_nodes[explanation_id] = _Node(
                node_id=node_id,
                label=_format_explanation_label(explanation),
                class_name=class_name,
            )

    matches = matching_run.get("matches", [])
    if not isinstance(matches, list):
        matches = []

    case_node_key_to_id: dict[str, str] = {}
    row_case_node_id: dict[int, str] = {}
    row_model_node_id: dict[int, str] = {}
    relation_edges: set[tuple[str, str, str]] = set()
    explanation_edges: set[tuple[str, str]] = set()

    for idx, row in enumerate(matches):
        if not isinstance(row, dict):
            continue

        case_term_id = row.get("case_term_id")
        case_label = row.get("case_label")
        case_present = row.get("case_present")
        if isinstance(case_term_id, str) or isinstance(case_label, str):
            key = f"{case_term_id or ''}|{case_present}|{case_label or ''}"
            if key not in case_node_key_to_id:
                case_id_fragment = case_term_id or case_label or f"row_{idx + 1}"
                node_id = f"case_{_safe_mermaid_id(str(case_id_fragment))}_{idx + 1}"
                case_nodes[node_id] = _Node(
                    node_id=node_id,
                    label=_format_case_label(row, idx + 1),
                    class_name=_classify_case_node(row),
                )
                case_node_key_to_id[key] = node_id
            row_case_node_id[idx] = case_node_key_to_id[key]

        model_node_id = _resolve_model_node_for_row(
            row,
            term_to_model_node=term_to_model_node,
            label_to_model_node=label_to_model_node,
            synthetic_model_nodes=synthetic_model_nodes,
        )
        if model_node_id:
            row_model_node_id[idx] = model_node_id
            status = _row_model_status(row)
            if status:
                current_status = model_status_by_node.get(model_node_id)
                if not current_status or _MODEL_STATUS_PRIORITY[status] > _MODEL_STATUS_PRIORITY[current_status]:
                    model_status_by_node[model_node_id] = status

        if idx in row_case_node_id and idx in row_model_node_id:
            relation_edges.add((row_model_node_id[idx], row_case_node_id[idx], _relation_edge_style(row)))

        explanation_id = row.get("explanation_for_no_match")
        if isinstance(explanation_id, str) and explanation_id:
            if explanation_id not in explanation_nodes:
                node_id = f"exp_{_safe_mermaid_id(explanation_id)}"
                class_name = "explanation_default" if explanation_id == _NO_EXPLANATION_ID else "explanation"
                explanation_nodes[explanation_id] = _Node(
                    node_id=node_id,
                    label=f"EXP: {explanation_id}<br/>Pr=NA",
                    class_name=class_name,
                )
            exp_node_id = explanation_nodes[explanation_id].node_id
            if idx in row_model_node_id:
                explanation_edges.add((row_model_node_id[idx], exp_node_id))
            if idx in row_case_node_id:
                explanation_edges.add((exp_node_id, row_case_node_id[idx]))

    for node_id, node in synthetic_model_nodes.items():
        resolved_status = model_status_by_node.get(node.node_id, node.class_name)
        model_nodes[node.node_id] = _Node(node_id=node.node_id, label=node.label, class_name=resolved_status)

    for node_id, node in list(model_nodes.items()):
        status = model_status_by_node.get(node_id, node.class_name)
        model_nodes[node_id] = _Node(node_id=node.node_id, label=node.label, class_name=status)

    lines: list[str] = ["graph LR", ""]

    def _emit_subgraph(graph_id: str, title: str, nodes: list[_Node]) -> None:
        if not nodes:
            return
        lines.append(f"    subgraph {graph_id}[{title}]")
        lines.append("        direction TB")
        for node in sorted(nodes, key=lambda n: n.node_id):
            lines.append(f'        {node.node_id}["{_escape_label(node.label)}"]')
        lines.append("    end")
        lines.append("")

    _emit_subgraph("CORE", "Mechanistic Core", list(core_nodes.values()) + list(orphan_nodes.values()))
    _emit_subgraph("MODEL_PHENOTYPES", "Disease Model Phenotypes", list(model_nodes.values()))
    _emit_subgraph("EXPLANATIONS", "Explanations", list(explanation_nodes.values()))
    _emit_subgraph("CASE_PHENOTYPES", "Case Phenotypes", list(case_nodes.values()))

    for edge in sorted(graph.edges, key=lambda e: (e.source, e.target, e.predicate)):
        source_id = graph_name_to_node_id.get(edge.source)
        target_id = graph_name_to_node_id.get(edge.target)
        if not source_id or not target_id:
            continue
        arrow = "-.->" if edge.target in graph.orphan_targets else "-->"
        lines.append(f"    {source_id} {arrow} {target_id}")

    if graph.edges:
        lines.append("")

    for source_id, target_id, arrow in sorted(relation_edges):
        lines.append(f"    {source_id} {arrow} {target_id}")
    if relation_edges:
        lines.append("")

    for source_id, target_id in sorted(explanation_edges):
        lines.append(f"    {source_id} -.-> {target_id}")
    if explanation_edges:
        lines.append("")

    lines.extend(
        [
            "    classDef core_pathophysiology fill:#dbeafe,stroke:#1e3a8a,stroke-width:1px",
            "    classDef core_environmental fill:#dcfce7,stroke:#166534,stroke-width:1px",
            "    classDef core_genetic fill:#f3e8ff,stroke:#6b21a8,stroke-width:1px",
            "    classDef core_treatment fill:#fce7f3,stroke:#9d174d,stroke-width:1px",
            "    classDef core_biochemical fill:#e0e7ff,stroke:#3730a3,stroke-width:1px",
            "    classDef core_other fill:#f3f4f6,stroke:#6b7280,stroke-width:1px",
            "    classDef orphan fill:#fee2e2,stroke:#dc2626,stroke-width:1px,stroke-dasharray:5 5",
            "    classDef model_exact_present fill:#86efac,stroke:#15803d,stroke-width:2px",
            "    classDef model_exact_absent fill:#fde047,stroke:#a16207,stroke-width:2px",
            "    classDef model_related fill:#93c5fd,stroke:#1d4ed8,stroke-width:2px",
            "    classDef model_unmatched fill:#fca5a5,stroke:#b91c1c,stroke-width:2px",
            "    classDef case_present fill:#bbf7d0,stroke:#166534,stroke-width:1px",
            "    classDef case_absent fill:#f3f4f6,stroke:#6b7280,stroke-width:1px,stroke-dasharray:5 3",
            "    classDef case_unknown fill:#e5e7eb,stroke:#6b7280,stroke-width:1px",
            "    classDef explanation fill:#ddd6fe,stroke:#5b21b6,stroke-width:1px",
            "    classDef explanation_default fill:#fee2e2,stroke:#b91c1c,stroke-width:1px,stroke-dasharray:5 3",
            "",
        ]
    )

    for node in sorted(core_nodes.values(), key=lambda n: n.node_id):
        lines.append(f"    class {node.node_id} {node.class_name}")
    for node in sorted(orphan_nodes.values(), key=lambda n: n.node_id):
        lines.append(f"    class {node.node_id} {node.class_name}")
    for node in sorted(model_nodes.values(), key=lambda n: n.node_id):
        lines.append(f"    class {node.node_id} {node.class_name}")
    for node in sorted(case_nodes.values(), key=lambda n: n.node_id):
        lines.append(f"    class {node.node_id} {node.class_name}")
    for node in sorted(explanation_nodes.values(), key=lambda n: n.node_id):
        lines.append(f"    class {node.node_id} {node.class_name}")

    return "\n".join(lines).rstrip() + "\n"


def render_matching_causal_mermaid(
    disorder_reference: str | Path,
    matching_report_path: str | Path,
    *,
    kb_dir: Path | None = None,
) -> str:
    """Resolve inputs and render Mermaid text for augmented matching visualization."""
    _, disorder_path = resolve_disease_reference(disorder_reference, kb_dir=kb_dir)
    disorder = _load_yaml_object(disorder_path)
    matching_run = _load_yaml_object(Path(matching_report_path))
    return generate_matching_causal_mermaid(disorder, matching_run)


def render_matching_causal_html(
    disorder: dict[str, Any],
    matching_run: dict[str, Any],
    mermaid: str,
    *,
    disorder_source: str | None = None,
    matching_source: str | None = None,
) -> str:
    """Render a standalone HTML page with metadata + embedded Mermaid diagram."""
    summary = _summarize_matching_run(matching_run)

    disease_name = disorder.get("name") or matching_run.get("disease_slug") or "Unknown disease"
    run_id = matching_run.get("run_id")
    case_id = matching_run.get("case_id")
    disease_slug = matching_run.get("disease_slug")
    generated_at = matching_run.get("generated_at")
    pr_is_diagnosis = matching_run.get("pr_is_diagnosis")

    rendered_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    graph_json = json.dumps(mermaid)

    metadata_rows = [
        ("Disease", disease_name),
        ("Disease slug", disease_slug),
        ("Case ID", case_id),
        ("Run ID", run_id),
        ("Generated at", generated_at),
        ("pr_is_diagnosis", _format_pr(pr_is_diagnosis)),
        ("Rendered at", rendered_at),
    ]
    if disorder_source:
        metadata_rows.append(("Disorder source", disorder_source))
    if matching_source:
        metadata_rows.append(("Matching report", matching_source))

    summary_rows = [
        ("Total rows", summary["total_rows"]),
        ("Exact present", summary["exact_present"]),
        ("Exact absent", summary["exact_absent"]),
        ("Related (broader/narrower/close)", summary["related"]),
        ("Unmatched", summary["unmatched"]),
        ("Model-only rows", summary["model_only"]),
        ("Case-only rows", summary["case_only"]),
        ("Non-exact rows", summary["non_exact_total"]),
        ("Non-exact unresolved", summary["non_exact_unresolved"]),
        ("Rows with TEMP_ explanations", summary["temporary_explanation_rows"]),
        ("Explanations total", summary["explanations_total"]),
        ("Explanations referenced", summary["explanations_referenced"]),
    ]

    metadata_table = "\n".join(
        f"                <tr><th>{html_escape(str(key))}</th><td>{html_escape(str(value) if value is not None else 'NA')}</td></tr>"
        for key, value in metadata_rows
    )
    summary_table = "\n".join(
        f"                <tr><th>{html_escape(str(key))}</th><td>{html_escape(str(value))}</td></tr>"
        for key, value in summary_rows
    )

    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html_escape(str(disease_name))} - Match-Aware Causal Graph</title>
    <style>
        :root {{
            --bg: #f8fafc;
            --panel: #ffffff;
            --border: #dbe3ee;
            --text: #0f172a;
            --muted: #475569;
            --accent: #0ea5e9;
        }}
        body {{
            margin: 0;
            padding: 24px;
            background: var(--bg);
            color: var(--text);
            font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, serif;
            line-height: 1.4;
        }}
        .wrap {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        .panel {{
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 16px 18px;
            margin-bottom: 14px;
        }}
        h1 {{
            margin: 0 0 8px 0;
            font-size: 1.7rem;
        }}
        p {{
            margin: 0;
            color: var(--muted);
        }}
        h2 {{
            margin: 0 0 10px 0;
            font-size: 1.05rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 14px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.95rem;
        }}
        th, td {{
            text-align: left;
            vertical-align: top;
            padding: 6px 8px;
            border-bottom: 1px solid #edf2f7;
        }}
        th {{
            width: 45%;
            color: #1e293b;
            font-weight: 600;
        }}
        .diagram {{
            overflow-x: auto;
        }}
        .mermaid {{
            min-height: 220px;
        }}
        details {{
            margin-top: 12px;
        }}
        pre {{
            white-space: pre;
            overflow-x: auto;
            padding: 12px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
            font-size: 0.82rem;
        }}
        a {{
            color: var(--accent);
        }}
    </style>
</head>
<body>
    <div class="wrap">
        <section class="panel">
            <h1>Match-Aware Causal Graph</h1>
            <p>{html_escape(str(disease_name))}</p>
        </section>

        <section class="grid">
            <article class="panel">
                <h2>Run Metadata</h2>
                <table>
                    <tbody>
{metadata_table}
                    </tbody>
                </table>
            </article>
            <article class="panel">
                <h2>Match Summary</h2>
                <table>
                    <tbody>
{summary_table}
                    </tbody>
                </table>
            </article>
        </section>

        <section class="panel diagram">
            <h2>Graph</h2>
            <div id="match-graph" class="mermaid"></div>
            <details>
                <summary>Raw Mermaid (.mmd)</summary>
                <pre>{html_escape(mermaid)}</pre>
            </details>
        </section>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
    <script>
        const graphDefinition = {graph_json};
        const graphElement = document.getElementById("match-graph");
        graphElement.textContent = graphDefinition;
        mermaid.initialize({{
            startOnLoad: false,
            securityLevel: "loose",
            flowchart: {{ htmlLabels: true, useMaxWidth: false }}
        }});
        mermaid.run({{ nodes: [graphElement] }});
    </script>
</body>
</html>
"""


def _default_output_path(matching_report_path: Path) -> Path:
    return Path("output") / "matching" / f"{matching_report_path.stem}.mermaid.html"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render dismech causal graph augmented with case matching and explanation nodes"
    )
    parser.add_argument(
        "disorder_reference",
        help="DisMech disease reference (path, slug, MONDO id, or disease name)",
    )
    parser.add_argument("matching_report", type=Path, help="Path to matching report YAML")
    parser.add_argument("--kb-dir", type=Path, default=None, help="Optional disorder directory override")
    parser.add_argument("--output", type=Path, default=None, help="Optional output .html file path")
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    _, disorder_path = resolve_disease_reference(args.disorder_reference, kb_dir=args.kb_dir)
    disorder = _load_yaml_object(disorder_path)
    matching_run = _load_yaml_object(args.matching_report)
    mermaid = generate_matching_causal_mermaid(disorder, matching_run)
    html = render_matching_causal_html(
        disorder,
        matching_run,
        mermaid,
        disorder_source=str(disorder_path),
        matching_source=str(args.matching_report),
    )

    output_path = args.output
    if output_path is None:
        output_path = _default_output_path(args.matching_report)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
