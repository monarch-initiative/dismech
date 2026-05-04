"""Generate QC dashboard reports for uncurated disease link targets."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator

import yaml

from dismech.render import curie_to_url, slugify

UNCURATED_BLOCK_START = "<!-- DISMECH-UNCURATED-START -->"
UNCURATED_BLOCK_END = "<!-- DISMECH-UNCURATED-END -->"
CAPABILITY_BLOCK_START = "<!-- DISMECH-CAPABILITY-METRICS-START -->"
CAPABILITY_BLOCK_END = "<!-- DISMECH-CAPABILITY-METRICS-END -->"


def _normalize_mondo_id(term_id: str | None) -> str | None:
    if not isinstance(term_id, str):
        return None
    normalized = term_id.strip().upper()
    if not normalized.startswith("MONDO:"):
        return None
    return normalized


def _choose_label(counter: Counter[str], default: str) -> str:
    if not counter:
        return default
    # Prefer the most frequent non-empty label, then deterministic alphabetical tie-break.
    ranked = sorted(counter.items(), key=lambda item: (-item[1], item[0].casefold()))
    return ranked[0][0]


def _extract_mondo_terms(node: Any) -> Iterator[tuple[str, str | None]]:
    """Yield (MONDO CURIE, label) pairs from nested descriptor-like structures."""
    if isinstance(node, dict):
        term = node.get("term")
        if isinstance(term, dict):
            term_id = _normalize_mondo_id(term.get("id"))
            if term_id:
                label = next(
                    (
                        str(value).strip()
                        for value in (
                            node.get("preferred_term"),
                            term.get("label"),
                            node.get("name"),
                        )
                        if isinstance(value, str) and value.strip()
                    ),
                    None,
                )
                yield term_id, label

        for key, value in node.items():
            if key == "has_subtypes":
                # Cancer subtype facets are ontology grounding only and should not
                # create "not yet curated" disease-page debt.
                continue
            yield from _extract_mondo_terms(value)
        return

    if isinstance(node, list):
        for item in node:
            yield from _extract_mondo_terms(item)


def _iter_disorder_files(kb_dir: Path) -> Iterable[Path]:
    for disorder_path in sorted(kb_dir.glob("*.yaml")):
        if disorder_path.name.endswith(".history.yaml"):
            continue
        yield disorder_path


def _load_disorders(kb_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    disorders: list[tuple[Path, dict[str, Any]]] = []
    for disorder_path in _iter_disorder_files(kb_dir):
        disorder = yaml.safe_load(disorder_path.read_text(encoding="utf-8")) or {}
        if isinstance(disorder, dict):
            disorders.append((disorder_path, disorder))
    return disorders


def _extract_root_disease_mondo_id(disorder: dict[str, Any]) -> str | None:
    disease_term = disorder.get("disease_term")
    if not isinstance(disease_term, dict):
        return None
    term = disease_term.get("term")
    if not isinstance(term, dict):
        return None
    return _normalize_mondo_id(term.get("id"))


def collect_uncurated_disease_references(kb_dir: Path) -> list[dict[str, Any]]:
    """Find MONDO disease references that do not resolve to local DisMech pages."""
    disorders = _load_disorders(kb_dir)
    curated_mondo_ids: set[str] = set()

    for _disorder_path, disorder in disorders:
        root_id = _extract_root_disease_mondo_id(disorder)
        if root_id:
            curated_mondo_ids.add(root_id)

    links_by_term: dict[str, dict[str, str]] = defaultdict(dict)
    labels_by_term: dict[str, Counter[str]] = defaultdict(Counter)

    for disorder_path, disorder in disorders:
        page_name = str(disorder.get("name") or disorder_path.stem).strip()
        page_filename = f"{slugify(page_name)}.html"
        seen_targets_for_page: set[str] = set()

        for term_id, label in _extract_mondo_terms(disorder):
            if term_id in curated_mondo_ids:
                continue

            if term_id not in seen_targets_for_page:
                links_by_term[term_id][page_name] = page_filename
                seen_targets_for_page.add(term_id)

            if label:
                labels_by_term[term_id][label] += 1

    rows: list[dict[str, Any]] = []
    for term_id, page_map in links_by_term.items():
        page_items = sorted(page_map.items(), key=lambda item: item[0].casefold())
        linking_pages = [
            {"name": page_name, "href": f"../pages/disorders/{filename}"}
            for page_name, filename in page_items
        ]
        rows.append(
            {
                "disease_name": _choose_label(labels_by_term[term_id], term_id),
                "mondo_id": term_id,
                "mondo_url": curie_to_url(term_id),
                "linking_pages_count": len(linking_pages),
                "linking_pages": linking_pages,
            }
        )

    rows.sort(
        key=lambda row: (
            -row["linking_pages_count"],
            row["disease_name"].casefold(),
            row["mondo_id"],
        )
    )
    return rows


def _is_evidence_item(node: dict[str, Any]) -> bool:
    return isinstance(node.get("reference"), str) and any(
        key in node for key in ("supports", "snippet", "evidence_source", "explanation")
    )


def _iter_evidence_items(node: Any) -> Iterator[dict[str, Any]]:
    if isinstance(node, dict):
        if _is_evidence_item(node):
            yield node
        for value in node.values():
            yield from _iter_evidence_items(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_evidence_items(item)


def _iter_term_ids(node: Any) -> Iterator[str]:
    if isinstance(node, dict):
        term = node.get("term")
        if isinstance(term, dict):
            term_id = term.get("id")
            if isinstance(term_id, str) and ":" in term_id:
                yield term_id.strip()
        for value in node.values():
            yield from _iter_term_ids(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_term_ids(item)


def _count_causal_edges(disorder: dict[str, Any]) -> int:
    count = 0
    for pathophysiology in disorder.get("pathophysiology") or []:
        if not isinstance(pathophysiology, dict):
            continue
        downstream = pathophysiology.get("downstream") or []
        if isinstance(downstream, list):
            count += len(downstream)
        elif downstream:
            count += 1
    return count


def _percentage(part: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round((part / total) * 100, 1)


def _average(values: Iterable[float]) -> float | None:
    numeric_values = [value for value in values if isinstance(value, int | float)]
    if not numeric_values:
        return None
    return round(sum(numeric_values) / len(numeric_values), 1)


def _average_per_entry(total: int, entries: int) -> float:
    if entries == 0:
        return 0.0
    return round(total / entries, 1)


def _load_compliance_summary(reports_path: Path | None) -> dict[str, Any] | None:
    if reports_path is None or not reports_path.exists():
        return None

    reports = json.loads(reports_path.read_text(encoding="utf-8"))
    if not isinstance(reports, list):
        return None

    global_scores = [
        report.get("global_compliance")
        for report in reports
        if isinstance(report, dict) and isinstance(report.get("global_compliance"), int | float)
    ]
    weighted_scores = [
        report.get("weighted_compliance")
        for report in reports
        if isinstance(report, dict) and isinstance(report.get("weighted_compliance"), int | float)
    ]
    violations = [
        report.get("violations")
        for report in reports
        if isinstance(report, dict) and isinstance(report.get("violations"), int)
    ]

    return {
        "files_analyzed": len(reports),
        "average_global_compliance": _average(global_scores),
        "average_weighted_compliance": _average(weighted_scores),
        "total_violations": sum(violations),
    }


def _parse_date(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def collect_capability_metrics(
    kb_dir: Path,
    reports_path: Path | None = None,
) -> dict[str, Any]:
    """Aggregate public capability metrics from curated disorder YAML files."""
    disorders = _load_disorders(kb_dir)
    total_entries = len(disorders)
    category_counts: Counter[str] = Counter()
    evidence_source_counts: Counter[str] = Counter()
    term_prefix_counts: Counter[str] = Counter()
    month_created_counts: Counter[str] = Counter()
    month_updated_counts: Counter[str] = Counter()
    evidence_references: set[str] = set()

    entries_with_mondo = 0
    entries_with_phenotype_terms = 0
    entries_with_treatments = 0
    entries_with_clinical_trials = 0
    entries_with_module_conformance = 0
    total_evidence_items = 0
    total_phenotype_terms = 0
    total_go_terms = 0
    total_cl_terms = 0
    total_treatments = 0
    total_clinical_trials = 0
    total_pathophysiology_nodes = 0
    total_causal_edges = 0
    total_module_conformance_nodes = 0

    for _path, disorder in disorders:
        category = disorder.get("category")
        if isinstance(category, str) and category.strip():
            category_counts[category.strip()] += 1

        if _extract_root_disease_mondo_id(disorder):
            entries_with_mondo += 1

        evidence_items = list(_iter_evidence_items(disorder))
        total_evidence_items += len(evidence_items)
        for item in evidence_items:
            reference = item.get("reference")
            if isinstance(reference, str) and reference.strip():
                evidence_references.add(reference.strip())
            evidence_source = item.get("evidence_source") or "UNSPECIFIED"
            if isinstance(evidence_source, str) and evidence_source.strip():
                evidence_source_counts[evidence_source.strip()] += 1

        term_ids = list(_iter_term_ids(disorder))
        for term_id in term_ids:
            prefix = term_id.split(":", 1)[0].upper()
            term_prefix_counts[prefix] += 1

        phenotype_terms = {
            phenotype.get("phenotype_term", {}).get("term", {}).get("id")
            for phenotype in disorder.get("phenotypes") or []
            if isinstance(phenotype, dict)
        }
        phenotype_terms = {
            term_id
            for term_id in phenotype_terms
            if isinstance(term_id, str) and term_id.strip()
        }
        total_phenotype_terms += len(phenotype_terms)
        if phenotype_terms:
            entries_with_phenotype_terms += 1

        total_go_terms += _count_term_prefix(term_ids, "GO")
        total_cl_terms += _count_term_prefix(term_ids, "CL")

        treatments = disorder.get("treatments") or []
        if isinstance(treatments, list):
            treatment_count = len([item for item in treatments if isinstance(item, dict)])
            total_treatments += treatment_count
            if treatment_count > 0:
                entries_with_treatments += 1

        clinical_trials = disorder.get("clinical_trials") or []
        if isinstance(clinical_trials, list):
            clinical_trial_count = len(
                [item for item in clinical_trials if isinstance(item, dict)]
            )
            total_clinical_trials += clinical_trial_count
            if clinical_trial_count > 0:
                entries_with_clinical_trials += 1

        pathophysiology_nodes = [
            item
            for item in disorder.get("pathophysiology") or []
            if isinstance(item, dict)
        ]
        total_pathophysiology_nodes += len(pathophysiology_nodes)
        total_causal_edges += _count_causal_edges(disorder)
        module_nodes = [
            item
            for item in pathophysiology_nodes
            if isinstance(item.get("conforms_to"), str) and item["conforms_to"].strip()
        ]
        total_module_conformance_nodes += len(module_nodes)
        if module_nodes:
            entries_with_module_conformance += 1

        creation_month = _date_month(disorder.get("creation_date"))
        if creation_month:
            month_created_counts[creation_month] += 1
        updated_month = _date_month(disorder.get("updated_date"))
        if updated_month:
            month_updated_counts[updated_month] += 1

    compliance_summary = _load_compliance_summary(reports_path)

    summary = {
        "total_entries": total_entries,
        "entries_with_mondo_id": entries_with_mondo,
        "total_evidence_items": total_evidence_items,
        "unique_evidence_references": len(evidence_references),
        "entries_with_treatments": entries_with_treatments,
        "entries_with_clinical_trials": entries_with_clinical_trials,
        "total_pathophysiology_nodes": total_pathophysiology_nodes,
        "total_causal_edges": total_causal_edges,
        "total_ontology_terms": sum(term_prefix_counts.values()),
    }
    if compliance_summary is not None:
        summary.update(
            {
                "average_global_compliance": compliance_summary["average_global_compliance"],
                "average_weighted_compliance": compliance_summary["average_weighted_compliance"],
                "total_compliance_violations": compliance_summary["total_violations"],
            }
        )

    return {
        "summary": summary,
        "coverage": {
            "total_entries": total_entries,
            "entries_with_mondo_id": entries_with_mondo,
            "entries_with_mondo_id_percent": _percentage(entries_with_mondo, total_entries),
            "disease_category_counts": dict(sorted(category_counts.items())),
        },
        "evidence_quality": {
            "total_evidence_items": total_evidence_items,
            "unique_evidence_references": len(evidence_references),
            "average_evidence_items_per_entry": _average_per_entry(
                total_evidence_items, total_entries
            ),
            "evidence_source_counts": dict(sorted(evidence_source_counts.items())),
        },
        "ontology_richness": {
            "total_ontology_terms": sum(term_prefix_counts.values()),
            "term_prefix_counts": dict(sorted(term_prefix_counts.items())),
            "entries_with_phenotype_terms": entries_with_phenotype_terms,
            "entries_with_phenotype_terms_percent": _percentage(
                entries_with_phenotype_terms, total_entries
            ),
            "average_hpo_terms_per_entry": _average_per_entry(
                total_phenotype_terms, total_entries
            ),
            "average_go_terms_per_entry": _average_per_entry(total_go_terms, total_entries),
            "average_cl_terms_per_entry": _average_per_entry(total_cl_terms, total_entries),
        },
        "mechanistic_depth": {
            "total_pathophysiology_nodes": total_pathophysiology_nodes,
            "total_causal_edges": total_causal_edges,
            "average_pathophysiology_nodes_per_entry": _average_per_entry(
                total_pathophysiology_nodes, total_entries
            ),
            "average_causal_edges_per_entry": _average_per_entry(
                total_causal_edges, total_entries
            ),
            "entries_with_module_conformance": entries_with_module_conformance,
            "entries_with_module_conformance_percent": _percentage(
                entries_with_module_conformance, total_entries
            ),
            "total_module_conformance_nodes": total_module_conformance_nodes,
        },
        "treatment_coverage": {
            "total_treatments": total_treatments,
            "entries_with_treatments": entries_with_treatments,
            "entries_with_treatments_percent": _percentage(entries_with_treatments, total_entries),
            "total_clinical_trials": total_clinical_trials,
            "entries_with_clinical_trials": entries_with_clinical_trials,
            "entries_with_clinical_trials_percent": _percentage(
                entries_with_clinical_trials, total_entries
            ),
        },
        "completeness": compliance_summary,
        "curation_velocity": {
            "created_by_month": dict(sorted(month_created_counts.items())),
            "updated_by_month": dict(sorted(month_updated_counts.items())),
        },
    }


def _count_term_prefix(term_ids: Iterable[str], prefix: str) -> int:
    prefix = prefix.upper()
    return sum(1 for term_id in term_ids if term_id.split(":", 1)[0].upper() == prefix)


def _date_month(value: Any) -> str | None:
    parsed = _parse_date(value)
    if parsed is None:
        return None
    return parsed.strftime("%Y-%m")


def _build_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "total_uncurated_disease_terms": len(rows),
        "total_linking_pages": sum(row["linking_pages_count"] for row in rows),
    }


def _render_report_table_rows(rows: list[dict[str, Any]]) -> str:
    rendered_rows: list[str] = []
    for row in rows:
        page_links = ", ".join(
            f'<a href="{html.escape(page["href"], quote=True)}">'
            f"{html.escape(page['name'])}</a>"
            for page in row["linking_pages"]
        )
        rendered_rows.append(
            "<tr>"
            f"<td>{html.escape(row['disease_name'])}</td>"
            f'<td><a href="{html.escape(row["mondo_url"], quote=True)}" '
            'target="_blank" rel="noopener">'
            f"{html.escape(row['mondo_id'])}</a></td>"
            f"<td>{row['linking_pages_count']}</td>"
            f"<td>{page_links}</td>"
            "</tr>"
        )
    return "\n".join(rendered_rows)


def _render_uncurated_report_page(
    rows: list[dict[str, Any]],
    generated_at: str,
    summary: dict[str, Any],
) -> str:
    table_body = _render_report_table_rows(rows)
    if not table_body:
        table_body = '<tr><td colspan="4">No uncurated disease links found.</td></tr>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QC Dashboard - Not Yet Curated Disease Links</title>
    <style>
        :root {{
            --green: #2ecc71;
            --bg: #f5f6fa;
            --card-bg: #ffffff;
            --text: #2c3e50;
            --text-light: #7f8c8d;
            --border: #dcdde1;
            --accent: #2980b9;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 2rem;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        header {{ margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 2px solid var(--border); }}
        h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
        .subtitle {{ color: var(--text-light); }}
        .meta {{ margin-top: 0.4rem; color: var(--text-light); font-size: 0.9rem; }}
        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}
        .card {{
            background: var(--card-bg);
            border-radius: 8px;
            padding: 1.2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .card h3 {{ font-size: 0.85rem; color: var(--text-light); text-transform: uppercase; margin-bottom: 0.45rem; }}
        .card .value {{ font-size: 1.8rem; font-weight: 700; color: var(--accent); }}
        .table-card {{
            background: var(--card-bg);
            border-radius: 8px;
            padding: 1.2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; }}
        th, td {{ padding: 0.7rem; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }}
        th {{ background: var(--bg); font-weight: 600; }}
        tr:hover {{ background: #fafbfd; }}
        a {{ color: var(--accent); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .breadcrumb {{ margin-bottom: 1rem; font-size: 0.92rem; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="breadcrumb"><a href="index.html">Back to QC Dashboard</a></div>
        <header>
            <h1>Not Yet Curated Disease Links</h1>
            <p class="subtitle">
                MONDO disease references that do not currently resolve to local DisMech disorder pages.
            </p>
            <p class="meta">Generated: {html.escape(generated_at)}</p>
        </header>

        <section class="summary-cards">
            <div class="card">
                <h3>Uncurated Disease Terms</h3>
                <div class="value">{summary["total_uncurated_disease_terms"]}</div>
            </div>
            <div class="card">
                <h3>Total Linking Pages</h3>
                <div class="value">{summary["total_linking_pages"]}</div>
            </div>
        </section>

        <section class="table-card">
            <table>
                <thead>
                    <tr>
                        <th>Disease Name</th>
                        <th>MONDO ID</th>
                        <th>Linking Pages</th>
                        <th>Page Names</th>
                    </tr>
                </thead>
                <tbody>
                    {table_body}
                </tbody>
            </table>
        </section>
    </div>
</body>
</html>
"""


def _format_metric_value(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.1f}"
    if isinstance(value, int):
        return f"{value:,}"
    return html.escape(str(value))


def _render_count_rows(counts: dict[str, int]) -> str:
    if not counts:
        return '<tr><td colspan="2">No values found.</td></tr>'
    rows = []
    for label, value in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        rows.append(
            "<tr>"
            f"<td>{html.escape(str(label))}</td>"
            f"<td>{_format_metric_value(value)}</td>"
            "</tr>"
        )
    return "\n".join(rows)


def _render_velocity_rows(
    created_by_month: dict[str, int],
    updated_by_month: dict[str, int],
    limit: int = 12,
) -> str:
    months = sorted(set(created_by_month) | set(updated_by_month), reverse=True)[:limit]
    if not months:
        return '<tr><td colspan="3">No timestamped curation activity found.</td></tr>'

    rows = []
    for month in months:
        rows.append(
            "<tr>"
            f"<td>{html.escape(month)}</td>"
            f"<td>{_format_metric_value(created_by_month.get(month, 0))}</td>"
            f"<td>{_format_metric_value(updated_by_month.get(month, 0))}</td>"
            "</tr>"
        )
    return "\n".join(rows)


def _render_capability_metrics_page(
    metrics: dict[str, Any],
    generated_at: str,
) -> str:
    summary = metrics["summary"]
    evidence = metrics["evidence_quality"]
    ontology = metrics["ontology_richness"]
    mechanisms = metrics["mechanistic_depth"]
    treatments = metrics["treatment_coverage"]
    completeness = metrics.get("completeness") or {}
    velocity = metrics["curation_velocity"]

    card_values = [
        ("Curated Entries", summary.get("total_entries"), "Disorder YAML files analyzed"),
        ("Evidence Items", summary.get("total_evidence_items"), "Cited evidence blocks"),
        ("Ontology Terms", summary.get("total_ontology_terms"), "Grounded descriptor terms"),
        ("Pathophysiology Nodes", summary.get("total_pathophysiology_nodes"), "Mechanism events"),
        ("Causal Edges", summary.get("total_causal_edges"), "Downstream mechanism links"),
        (
            "Avg Weighted Compliance",
            completeness.get("average_weighted_compliance"),
            "From linkml-data-qc reports",
        ),
    ]
    cards = "\n".join(
        """
            <div class="card">
                <h3>{title}</h3>
                <div class="value">{value}</div>
                <p>{detail}</p>
            </div>
        """.format(
            title=html.escape(title),
            value=_format_metric_value(value),
            detail=html.escape(detail),
        )
        for title, value, detail in card_values
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QC Dashboard - Capability Metrics</title>
    <style>
        :root {{
            --bg: #f5f6fa;
            --card-bg: #ffffff;
            --text: #2c3e50;
            --text-light: #6b7280;
            --border: #dcdde1;
            --accent: #2980b9;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 2rem;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        header {{ margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 2px solid var(--border); }}
        h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
        h2 {{ font-size: 1.2rem; margin-bottom: 0.8rem; }}
        .subtitle, .meta, .card p {{ color: var(--text-light); }}
        .meta {{ margin-top: 0.4rem; font-size: 0.9rem; }}
        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}
        .card, .panel {{
            background: var(--card-bg);
            border-radius: 8px;
            padding: 1.2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .card h3 {{ font-size: 0.82rem; color: var(--text-light); text-transform: uppercase; margin-bottom: 0.4rem; }}
        .card .value {{ font-size: 1.8rem; font-weight: 700; color: var(--accent); }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 1rem;
        }}
        .metric-list {{ display: grid; gap: 0.45rem; margin-bottom: 1rem; }}
        .metric-list div {{ display: flex; justify-content: space-between; gap: 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.35rem; }}
        .metric-list dt {{ color: var(--text-light); }}
        .metric-list dd {{ font-weight: 700; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; }}
        th, td {{ padding: 0.65rem; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }}
        th {{ background: var(--bg); font-weight: 600; }}
        a {{ color: var(--accent); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .breadcrumb {{ margin-bottom: 1rem; font-size: 0.92rem; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="breadcrumb"><a href="index.html">Back to QC Dashboard</a></div>
        <header>
            <h1>DISMECH Capability Metrics</h1>
            <p class="subtitle">
                Aggregate QA/QC metrics showing DISMECH coverage, evidence depth, ontology grounding,
                mechanistic modeling, and treatment coverage.
            </p>
            <p class="meta">Generated: {html.escape(generated_at)}</p>
        </header>

        <section class="summary-cards">
            {cards}
        </section>

        <section class="grid">
            <div class="panel">
                <h2>Evidence Quality</h2>
                <dl class="metric-list">
                    <div><dt>Unique evidence references</dt><dd>{_format_metric_value(evidence["unique_evidence_references"])}</dd></div>
                    <div><dt>Average evidence items per entry</dt><dd>{_format_metric_value(evidence["average_evidence_items_per_entry"])}</dd></div>
                </dl>
                <table>
                    <thead><tr><th>Evidence Source</th><th>Items</th></tr></thead>
                    <tbody>{_render_count_rows(evidence["evidence_source_counts"])}</tbody>
                </table>
            </div>

            <div class="panel">
                <h2>Ontology Richness</h2>
                <dl class="metric-list">
                    <div><dt>Entries with HPO phenotype terms</dt><dd>{_format_metric_value(ontology["entries_with_phenotype_terms_percent"])}%</dd></div>
                    <div><dt>Average HPO terms per entry</dt><dd>{_format_metric_value(ontology["average_hpo_terms_per_entry"])}</dd></div>
                    <div><dt>Average GO terms per entry, all sections</dt><dd>{_format_metric_value(ontology["average_go_terms_per_entry"])}</dd></div>
                    <div><dt>Average CL terms per entry, all sections</dt><dd>{_format_metric_value(ontology["average_cl_terms_per_entry"])}</dd></div>
                </dl>
                <table>
                    <thead><tr><th>Ontology Prefix</th><th>Terms</th></tr></thead>
                    <tbody>{_render_count_rows(ontology["term_prefix_counts"])}</tbody>
                </table>
            </div>

            <div class="panel">
                <h2>Mechanistic Depth</h2>
                <dl class="metric-list">
                    <div><dt>Average pathophysiology nodes per entry</dt><dd>{_format_metric_value(mechanisms["average_pathophysiology_nodes_per_entry"])}</dd></div>
                    <div><dt>Average causal edges per entry</dt><dd>{_format_metric_value(mechanisms["average_causal_edges_per_entry"])}</dd></div>
                    <div><dt>Entries using mechanism modules</dt><dd>{_format_metric_value(mechanisms["entries_with_module_conformance_percent"])}%</dd></div>
                    <div><dt>Module-conforming nodes</dt><dd>{_format_metric_value(mechanisms["total_module_conformance_nodes"])}</dd></div>
                </dl>
            </div>

            <div class="panel">
                <h2>Treatment Coverage</h2>
                <dl class="metric-list">
                    <div><dt>Total treatments</dt><dd>{_format_metric_value(treatments["total_treatments"])}</dd></div>
                    <div><dt>Entries with treatments</dt><dd>{_format_metric_value(treatments["entries_with_treatments_percent"])}%</dd></div>
                    <div><dt>Total clinical trials</dt><dd>{_format_metric_value(treatments["total_clinical_trials"])}</dd></div>
                    <div><dt>Entries with clinical trials</dt><dd>{_format_metric_value(treatments["entries_with_clinical_trials_percent"])}%</dd></div>
                </dl>
            </div>

            <div class="panel">
                <h2>Curation Velocity</h2>
                <table>
                    <thead><tr><th>Month</th><th>Created</th><th>Updated</th></tr></thead>
                    <tbody>{_render_velocity_rows(velocity["created_by_month"], velocity["updated_by_month"])}</tbody>
                </table>
            </div>
        </section>
    </div>
</body>
</html>
"""


def _build_index_block(summary: dict[str, Any]) -> str:
    return f"""
        {UNCURATED_BLOCK_START}
        <section class="chart-card">
            <h2>Not Yet Curated Disease Links</h2>
            <p class="priority-note">
                Found <strong>{summary["total_uncurated_disease_terms"]}</strong> referenced MONDO disease terms without local pages
                across <strong>{summary["total_linking_pages"]}</strong> linking page references.
            </p>
            <p><a href="not_yet_curated.html">View the uncurated disease link report</a></p>
        </section>
        {UNCURATED_BLOCK_END}
"""


def _build_capability_index_block(summary: dict[str, Any]) -> str:
    weighted = summary.get("average_weighted_compliance")
    weighted_text = (
        f" Average weighted compliance is <strong>{_format_metric_value(weighted)}%</strong>."
        if weighted is not None
        else ""
    )
    return f"""
        {CAPABILITY_BLOCK_START}
        <section class="chart-card">
            <h2>DISMECH Capability Metrics</h2>
            <p class="priority-note">
                Tracking <strong>{_format_metric_value(summary["total_entries"])}</strong> curated entries,
                <strong>{_format_metric_value(summary["total_evidence_items"])}</strong> evidence items,
                <strong>{_format_metric_value(summary["total_ontology_terms"])}</strong> ontology-grounded terms,
                and <strong>{_format_metric_value(summary["total_pathophysiology_nodes"])}</strong> pathophysiology nodes.
                {weighted_text}
            </p>
            <p><a href="capability_metrics.html">View the capability metrics report</a></p>
        </section>
        {CAPABILITY_BLOCK_END}
"""


def inject_uncurated_link(
    dashboard_index_path: Path,
    summary: dict[str, Any],
) -> bool:
    """Insert or update the uncurated-links section in the dashboard index page."""
    return _inject_block(
        dashboard_index_path,
        start_sentinel=UNCURATED_BLOCK_START,
        end_sentinel=UNCURATED_BLOCK_END,
        block=_build_index_block(summary),
    )


def _inject_block(
    dashboard_index_path: Path,
    *,
    start_sentinel: str,
    end_sentinel: str,
    block: str,
) -> bool:
    """Insert or update a sentinel-delimited section in the dashboard index page."""
    if not dashboard_index_path.exists():
        return False

    content = dashboard_index_path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(start_sentinel)}.*?{re.escape(end_sentinel)}",
        flags=re.DOTALL,
    )

    if pattern.search(content):
        updated = pattern.sub(block.strip("\n"), content, count=1)
    elif "<footer" in content:
        updated = content.replace("<footer", f"{block}\n        <footer", 1)
    elif "</body>" in content:
        updated = content.replace("</body>", f"{block}\n</body>", 1)
    else:
        updated = f"{content.rstrip()}\n{block}\n"

    if updated == content:
        return False

    dashboard_index_path.write_text(updated, encoding="utf-8")
    return True


def inject_capability_metrics_link(
    dashboard_index_path: Path,
    summary: dict[str, Any],
) -> bool:
    """Insert or update the capability-metrics section in the dashboard index page."""
    return _inject_block(
        dashboard_index_path,
        start_sentinel=CAPABILITY_BLOCK_START,
        end_sentinel=CAPABILITY_BLOCK_END,
        block=_build_capability_index_block(summary),
    )


def generate_uncurated_dashboard_report(
    kb_dir: Path,
    dashboard_dir: Path,
    dashboard_index_path: Path | None = None,
) -> dict[str, Any]:
    """Build uncurated disease link report pages for the QC dashboard."""
    rows = collect_uncurated_disease_references(kb_dir)
    summary = _build_summary(rows)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    dashboard_dir.mkdir(parents=True, exist_ok=True)
    json_path = dashboard_dir / "not_yet_curated.json"
    html_path = dashboard_dir / "not_yet_curated.html"

    payload = {
        "generated_at": generated_at,
        "summary": summary,
        "rows": rows,
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    html_path.write_text(
        _render_uncurated_report_page(rows, generated_at, summary), encoding="utf-8"
    )

    index_updated = False
    if dashboard_index_path is not None:
        index_updated = inject_uncurated_link(dashboard_index_path, summary)

    return {
        "json_path": json_path,
        "html_path": html_path,
        "summary": summary,
        "index_updated": index_updated,
    }


def generate_capability_metrics_report(
    kb_dir: Path,
    dashboard_dir: Path,
    reports_path: Path | None = None,
    dashboard_index_path: Path | None = None,
) -> dict[str, Any]:
    """Build aggregate DISMECH capability metrics for the QC dashboard."""
    metrics = collect_capability_metrics(kb_dir=kb_dir, reports_path=reports_path)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    dashboard_dir.mkdir(parents=True, exist_ok=True)
    json_path = dashboard_dir / "capability_metrics.json"
    html_path = dashboard_dir / "capability_metrics.html"

    payload = {
        "generated_at": generated_at,
        **metrics,
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    html_path.write_text(
        _render_capability_metrics_page(metrics, generated_at), encoding="utf-8"
    )

    index_updated = False
    if dashboard_index_path is not None:
        index_updated = inject_capability_metrics_link(
            dashboard_index_path, metrics["summary"]
        )

    return {
        "json_path": json_path,
        "html_path": html_path,
        "summary": metrics["summary"],
        "index_updated": index_updated,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate supplemental QC dashboard reports for DISMECH capability metrics "
            "and MONDO disease references that do not yet resolve to local pages."
        )
    )
    parser.add_argument("--kb-dir", default="kb/disorders", type=Path)
    parser.add_argument("--dashboard-dir", default="dashboard", type=Path)
    parser.add_argument(
        "--reports-json",
        default=None,
        type=Path,
        help=(
            "Optional linkml-data-qc reports JSON. Defaults to "
            "<dashboard-dir>/reports.json when present."
        ),
    )
    parser.add_argument(
        "--dashboard-index",
        default="dashboard/index.html",
        type=Path,
        help="Dashboard index file to patch with a link to the report.",
    )
    args = parser.parse_args()

    reports_path = args.reports_json
    if reports_path is None:
        default_reports_path = args.dashboard_dir / "reports.json"
        reports_path = default_reports_path if default_reports_path.exists() else None

    capability_result = generate_capability_metrics_report(
        kb_dir=args.kb_dir,
        dashboard_dir=args.dashboard_dir,
        reports_path=reports_path,
        dashboard_index_path=args.dashboard_index,
    )
    uncurated_result = generate_uncurated_dashboard_report(
        kb_dir=args.kb_dir,
        dashboard_dir=args.dashboard_dir,
        dashboard_index_path=args.dashboard_index,
    )

    capability_summary = capability_result["summary"]
    print(
        "Generated DISMECH capability metrics report:"
        f" {capability_summary['total_entries']} entries,"
        f" {capability_summary['total_evidence_items']} evidence items,"
        f" {capability_summary['total_ontology_terms']} ontology terms"
    )
    print(f"- HTML: {capability_result['html_path']}")
    print(f"- JSON: {capability_result['json_path']}")

    summary = uncurated_result["summary"]
    print(
        "Generated uncurated disease link QC report:"
        f" {summary['total_uncurated_disease_terms']} terms,"
        f" {summary['total_linking_pages']} linking pages"
    )
    print(f"- HTML: {uncurated_result['html_path']}")
    print(f"- JSON: {uncurated_result['json_path']}")
    if args.dashboard_index.exists():
        print(
            "- Dashboard index capability link updated:"
            f" {'yes' if capability_result['index_updated'] else 'no (already up to date)'}"
        )
        print(
            "- Dashboard index uncurated link updated:"
            f" {'yes' if uncurated_result['index_updated'] else 'no (already up to date)'}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
