"""Generate a static MONDO curation priority dashboard."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from string import Template
from typing import Any

from dismech.compare.mondo_priority import _extract_family_stem
from dismech.compare.mondo_priority import _grouping_term
from dismech.compare.mondo_priority import _likely_over_specific_leaf
from dismech.compare.mondo_priority import _normalize_text
from dismech.compare.mondo_priority import build_coverage_index
from dismech.compare.mondo_priority import load_candidates
from dismech.compare.mondo_priority import load_config
from dismech.compare.mondo_priority import score_candidates
from dismech.render import curie_to_url

PRIORITY_BLOCK_START = "<!-- DISMECH-PRIORITY-START -->"
PRIORITY_BLOCK_END = "<!-- DISMECH-PRIORITY-END -->"

_CATEGORY_FIELDS = (
    "category",
    "categories",
    "mondo_categories",
    "mondo_category_body_system",
    "mondo_category_developmental",
    "mondo_category_etiologic",
    "mondo_category_extrinsic",
    "mondo_category_genetic",
    "mondo_category_molecular",
    "hpo_high_level_categories",
)

_ACTION_ORDER = {
    "CURATE_ROOT_WITH_SUBTYPES": 0,
    "CURATE_ROOT": 1,
    "REVIEW_SERIES_FOR_PARENT_ROOT": 2,
    "REVIEW_AGAINST_PARENT": 3,
    "LUMP_INTO_PARENT": 4,
    "DROP_GROUPING_TERM": 5,
    "DROP_OBSOLETE": 6,
    "ALREADY_CURATED": 7,
}

_ROOT_ACTIONS = {"CURATE_ROOT", "CURATE_ROOT_WITH_SUBTYPES"}
_CURATED_ACTION = "ALREADY_CURATED"
_WEIGHT_LABELS = {
    "missing_from_dismech": "Missing from dismech",
    "has_definition": "Has MONDO definition",
    "synonym_count": "Synonym count",
    "xref_count": "Xref count",
    "clingen_definitive_count": "ClinGen definitive count",
    "clingen_strong_count": "ClinGen strong count",
    "subset_match_count": "Priority subset count",
    "orphanet_match_count": "Orphanet or ORDO xrefs",
    "broad_parent_bonus": "Broad parent bonus",
    "subtype_series_penalty": "Subtype series penalty",
    "grouping_term_penalty": "Grouping term penalty",
    "over_specific_leaf_penalty": "Over-specific leaf penalty",
    "obsolete_penalty": "Obsolete penalty",
    "already_curated_penalty": "Already curated penalty",
}


def _split_multi_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list | tuple | set):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, dict):
        return []

    text = str(value).strip()
    if not text:
        return []

    if text.startswith("[") and text.endswith("]"):
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            payload = None
        if isinstance(payload, list):
            return [str(item).strip() for item in payload if str(item).strip()]

    if "|" in text:
        parts = text.split("|")
    elif ";" in text:
        parts = text.split(";")
    else:
        parts = [text]

    return [part.strip() for part in parts if part.strip()]


def _dedupe(values: list[str]) -> list[str]:
    seen: dict[str, str] = {}
    for value in values:
        cleaned = " ".join(value.split())
        if not cleaned:
            continue
        seen.setdefault(cleaned.casefold(), cleaned)
    return list(seen.values())


def _extract_categories(raw: dict[str, Any]) -> list[str]:
    categories: list[str] = []
    for field in _CATEGORY_FIELDS:
        categories.extend(_split_multi_value(raw.get(field)))
    return _dedupe(categories)


def _action_tone(action: str) -> str:
    if action in _ROOT_ACTIONS:
        return "ready"
    if action.startswith("REVIEW_"):
        return "review"
    if action == "LUMP_INTO_PARENT":
        return "neutral"
    if action.startswith("DROP_"):
        return "drop"
    if action == _CURATED_ACTION:
        return "curated"
    return "neutral"


def _slugify_token(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def _build_rows(
    candidates_path: Path,
    kb_dir: Path,
    config_path: Path,
) -> list[dict[str, Any]]:
    candidates = load_candidates(candidates_path)
    coverage = build_coverage_index(kb_dir)
    config = load_config(config_path)
    scored = score_candidates(candidates, coverage=coverage, config=config)
    heuristics = dict(config.get("heuristics") or {})
    thresholds = dict(config.get("thresholds") or {})
    subtype_series_patterns = list(heuristics.get("subtype_series_patterns") or [])
    grouping_patterns = list(heuristics.get("grouping_term_patterns") or [])
    subtype_series_min_family_size = int(
        thresholds.get("subtype_series_min_family_size", 2)
    )
    broad_parent_min_children = int(thresholds.get("broad_parent_min_children", 4))
    over_specific_leaf_min_words = int(
        thresholds.get("over_specific_leaf_min_words", 8)
    )
    candidate_by_id = {candidate.mondo_id: candidate for candidate in candidates}
    known_labels = {
        _normalize_text(candidate.label): candidate.label for candidate in candidates
    }
    family_by_id: dict[str, str] = {}
    family_sizes: dict[str, int] = {}

    for candidate in candidates:
        stem = _extract_family_stem(candidate.label, subtype_series_patterns)
        if stem:
            normalized_stem = _normalize_text(stem)
            family_by_id[candidate.mondo_id] = stem
            family_sizes[normalized_stem] = family_sizes.get(normalized_stem, 0) + 1

    rows: list[dict[str, Any]] = []
    for item in scored:
        candidate = candidate_by_id[item.mondo_id]
        family_stem = family_by_id.get(candidate.mondo_id)
        normalized_family_stem = _normalize_text(family_stem)
        family_size = family_sizes.get(normalized_family_stem, 0)
        subtype_series = bool(
            family_stem and family_size >= subtype_series_min_family_size
        )
        parent_present = False
        if family_stem:
            normalized_stem = _normalize_text(family_stem)
            parent_present = (
                normalized_stem in known_labels
                or normalized_stem in coverage.curated_labels
            )
        if not parent_present:
            parent_present = any(
                _normalize_text(parent) in coverage.curated_labels
                or _normalize_text(parent) in known_labels
                for parent in candidate.parents
            )
        grouping_term = _grouping_term(candidate.label, grouping_patterns)
        broad_parent = (
            candidate.child_count >= broad_parent_min_children
            and not subtype_series
            and not grouping_term
        )
        over_specific_leaf = _likely_over_specific_leaf(
            candidate.label,
            candidate.child_count,
            over_specific_leaf_min_words,
        )
        rows.append(
            {
                "mondo_id": item.mondo_id,
                "mondo_url": curie_to_url(item.mondo_id),
                "label": item.label,
                "score": item.score,
                "recommended_action": item.recommended_action,
                "recommended_action_tone": _action_tone(item.recommended_action),
                "specificity_bucket": item.specificity_bucket,
                "curated_match": item.curated_match,
                "family_stem": family_stem,
                "family_size": family_size,
                "categories": _extract_categories(candidate.raw),
                "parents": candidate.parents,
                "features": {
                    "missing_from_dismech": item.curated_match is None,
                    "has_definition": bool(candidate.definition),
                    "synonym_count": len(candidate.synonyms),
                    "xref_count": len(candidate.xrefs),
                    "clingen_definitive_count": candidate.clingen_definitive_count,
                    "clingen_strong_count": candidate.clingen_strong_count,
                    "subset_match_count": candidate.subset_match_count,
                    "orphanet_match_count": candidate.orphanet_match_count,
                    "broad_parent": broad_parent,
                    "subtype_series": subtype_series,
                    "grouping_term": grouping_term,
                    "over_specific_leaf": over_specific_leaf,
                    "obsolete": candidate.is_obsolete,
                    "already_curated": item.curated_match is not None,
                    "child_count": candidate.child_count,
                    "parent_present": parent_present,
                },
            }
        )
    return rows


def _build_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total_candidates = len(rows)
    already_curated = sum(
        1 for row in rows if row["recommended_action"] == _CURATED_ACTION
    )
    remaining_candidates = total_candidates - already_curated
    root_action_candidates = sum(
        1 for row in rows if row["recommended_action"] in _ROOT_ACTIONS
    )
    coverage_percent = round(
        (already_curated / total_candidates) * 100 if total_candidates else 0.0,
        1,
    )

    top_remaining = next(
        (row for row in rows if row["recommended_action"] != _CURATED_ACTION),
        None,
    )

    return {
        "total_candidates": total_candidates,
        "already_curated": already_curated,
        "remaining_candidates": remaining_candidates,
        "root_action_candidates": root_action_candidates,
        "coverage_percent": coverage_percent,
        "top_remaining_label": top_remaining["label"] if top_remaining else None,
        "top_remaining_mondo_id": top_remaining["mondo_id"] if top_remaining else None,
        "top_remaining_score": top_remaining["score"] if top_remaining else None,
    }


def _build_action_breakdown(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = Counter(row["recommended_action"] for row in rows)
    if not counts:
        return []

    maximum = max(counts.values())
    total = len(rows)
    items: list[dict[str, Any]] = []
    for action, count in sorted(
        counts.items(),
        key=lambda item: (_ACTION_ORDER.get(item[0], 99), -item[1], item[0]),
    ):
        items.append(
            {
                "action": action,
                "tone": _action_tone(action),
                "count": count,
                "percent": round((count / total) * 100 if total else 0.0, 1),
                "bar_width": round((count / maximum) * 100 if maximum else 0.0, 1),
            }
        )
    return items


def _build_category_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for row in rows:
        for category in row["categories"]:
            key = category.casefold()
            bucket = grouped.setdefault(
                key,
                {
                    "category": category,
                    "rows": [],
                },
            )
            bucket["rows"].append(row)

    summaries: list[dict[str, Any]] = []
    for bucket in grouped.values():
        category_rows = bucket["rows"]
        remaining_rows = [
            row for row in category_rows if row["recommended_action"] != _CURATED_ACTION
        ]
        top_row = remaining_rows[0] if remaining_rows else None
        summaries.append(
            {
                "category": bucket["category"],
                "total_candidates": len(category_rows),
                "already_curated": len(category_rows) - len(remaining_rows),
                "remaining_candidates": len(remaining_rows),
                "top_candidate_label": top_row["label"] if top_row else None,
                "top_candidate_mondo_id": top_row["mondo_id"] if top_row else None,
                "top_candidate_score": top_row["score"] if top_row else None,
            }
        )

    summaries.sort(
        key=lambda row: (
            -row["remaining_candidates"],
            -(row["top_candidate_score"] or -1e9),
            row["category"].casefold(),
        )
    )
    return summaries


def _render_action_breakdown(items: list[dict[str, Any]]) -> str:
    if not items:
        return '<p class="empty-state">No action breakdown available.</p>'

    rendered: list[str] = []
    for item in items:
        rendered.append(
            '<div class="bar-row">'
            '<div class="bar-label">'
            f'<span class="pill pill-{item["tone"]}">{html.escape(item["action"])}</span>'
            f'<span class="bar-stat">{item["count"]} ({item["percent"]:.1f}%)</span>'
            "</div>"
            '<div class="bar-track">'
            f'<div class="bar-fill bar-fill-{item["tone"]}" style="width: {item["bar_width"]:.1f}%;"></div>'
            "</div>"
            "</div>"
        )
    return "\n".join(rendered)


def _render_category_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return ""

    rendered: list[str] = []
    for row in rows:
        top_candidate = "Fully covered"
        if row["top_candidate_label"] and row["top_candidate_mondo_id"]:
            top_candidate = (
                f'<a href="{html.escape(curie_to_url(row["top_candidate_mondo_id"]), quote=True)}" '
                'target="_blank" rel="noopener">'
                f"{html.escape(row['top_candidate_label'])}</a>"
                f' <span class="table-note">({row["top_candidate_score"]:.1f})</span>'
            )
        rendered.append(
            "<tr>"
            f"<td>{html.escape(row['category'])}</td>"
            f"<td>{row['remaining_candidates']}</td>"
            f"<td>{row['already_curated']}</td>"
            f"<td>{top_candidate}</td>"
            "</tr>"
        )
    return "\n".join(rendered)


def _render_priority_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return '<tr><td colspan="6">No uncurated MONDO candidates found.</td></tr>'

    rendered: list[str] = []
    for rank, row in enumerate(rows, start=1):
        badge = (
            f'<span class="priority-badge">#{rank}</span>' if rank <= 10 else str(rank)
        )
        rendered.append(
            "<tr>"
            f"<td>{badge}</td>"
            f'<td><a href="{html.escape(row["mondo_url"], quote=True)}" target="_blank" rel="noopener">'
            f"{html.escape(row['mondo_id'])}</a></td>"
            f"<td>{html.escape(row['label'])}</td>"
            f'<td class="score-cell">{row["score"]:.1f}</td>'
            f'<td><span class="pill pill-{row["recommended_action_tone"]}">{html.escape(row["recommended_action"])}</span></td>'
            f'<td><span class="subtle-pill subtle-pill-{_slugify_token(row["specificity_bucket"])}">'
            f"{html.escape(row['specificity_bucket'])}</span></td>"
            "</tr>"
        )
    return "\n".join(rendered)


def _render_weight_controls(weights: dict[str, Any]) -> str:
    rendered: list[str] = []
    for key, value in weights.items():
        label = _WEIGHT_LABELS.get(key, key.replace("_", " ").title())
        rendered.append(
            '<label class="weight-control">'
            f'<span class="weight-title">{html.escape(label)}</span>'
            f'<input type="number" step="0.5" value="{float(value):g}" data-weight-key="{html.escape(key, quote=True)}">'
            "</label>"
        )
    return "\n".join(rendered)


def _render_action_filter_options() -> str:
    options = ['<option value="ALL">All Actions</option>']
    for action, _ in sorted(_ACTION_ORDER.items(), key=lambda item: item[1]):
        options.append(
            f'<option value="{html.escape(action, quote=True)}">{html.escape(action)}</option>'
        )
    return "\n".join(options)


def _render_bucket_filter_options(rows: list[dict[str, Any]]) -> str:
    buckets = sorted({row["specificity_bucket"] for row in rows})
    options = ['<option value="ALL">All Buckets</option>']
    for bucket in buckets:
        options.append(
            f'<option value="{html.escape(bucket, quote=True)}">{html.escape(bucket)}</option>'
        )
    return "\n".join(options)


def _render_category_filter_options(rows: list[dict[str, Any]]) -> str:
    categories = sorted(
        {category for row in rows for category in row["categories"]},
        key=str.casefold,
    )
    options = ['<option value="ALL">All Categories</option>']
    for category in categories:
        options.append(
            f'<option value="{html.escape(category, quote=True)}">{html.escape(category)}</option>'
        )
    return "\n".join(options)


def _render_priority_report_page(payload: dict[str, Any]) -> str:
    rows = payload["rows"]
    summary = payload["summary"]
    category_summary = payload["category_summary"]
    scoring = dict(payload.get("scoring") or {})
    thresholds = dict(scoring.get("thresholds") or {})
    curated_width = summary["coverage_percent"]
    remaining_width = max(0.0, 100.0 - curated_width)
    weight_controls = _render_weight_controls(scoring.get("weights") or {})
    action_options = _render_action_filter_options()
    bucket_options = _render_bucket_filter_options(rows)
    category_filter_block = ""
    category_section = ""
    if category_summary:
        category_filter_block = f"""
                    <label class="filter-control">
                        <span>Category</span>
                        <select id="category-filter">
                            {_render_category_filter_options(rows)}
                        </select>
                    </label>
"""
        category_section = """
        <section class="chart-card" id="category-card">
            <h2>Category View</h2>
            <p class="priority-note">
                Category counts reflect the current filtered view. Categories are not mutually exclusive,
                so visible totals can exceed the number of visible candidates.
            </p>
            <table>
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Visible</th>
                        <th>Root Actions</th>
                        <th>Top Candidate</th>
                    </tr>
                </thead>
                <tbody id="category-table-body"></tbody>
            </table>
        </section>
"""
    payload_json = json.dumps(payload, separators=(",", ":")).replace("</", r"<\/")
    template = Template(
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curation Priority Dashboard</title>
    <style>
        :root {
            --teal: #0f766e;
            --teal-light: #14b8a6;
            --green: #2ecc71;
            --orange: #f39c12;
            --red: #e74c3c;
            --slate: #64748b;
            --bg: #f5f6fa;
            --card-bg: #ffffff;
            --text: #2c3e50;
            --text-light: #7f8c8d;
            --border: #dcdde1;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 2rem;
        }
        .container { max-width: 1480px; margin: 0 auto; }
        .breadcrumb { margin-bottom: 1rem; font-size: 0.92rem; }
        a { color: var(--teal); text-decoration: none; }
        a:hover { text-decoration: underline; }
        header {
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid var(--border);
        }
        h1 { font-size: 2rem; margin-bottom: 0.5rem; }
        .subtitle { color: var(--text-light); max-width: 980px; }
        .meta { margin-top: 0.5rem; color: var(--text-light); font-size: 0.9rem; word-break: break-word; }
        .summary-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        .card, .chart-card {
            background: var(--card-bg);
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }
        .chart-card { margin-bottom: 1.5rem; }
        .card h3 {
            font-size: 0.85rem;
            color: var(--text-light);
            text-transform: uppercase;
            margin-bottom: 0.45rem;
            letter-spacing: 0.04em;
        }
        .card .value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--teal);
        }
        .chart-card h2 {
            font-size: 1.1rem;
            margin-bottom: 0.9rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border);
        }
        .panel-heading {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }
        .priority-note {
            color: var(--text-light);
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }
        .progress-legend {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            font-size: 0.95rem;
            margin-bottom: 0.6rem;
            flex-wrap: wrap;
        }
        .progress-shell {
            width: 100%;
            height: 18px;
            border-radius: 999px;
            background: #e8ecef;
            overflow: hidden;
            display: flex;
        }
        .progress-curated {
            background: linear-gradient(90deg, var(--teal), var(--teal-light));
        }
        .progress-remaining {
            background: #cfd8dc;
        }
        .controls-grid,
        .insight-grid,
        .guide-grid {
            display: grid;
            gap: 1rem;
        }
        .controls-grid {
            grid-template-columns: minmax(260px, 0.9fr) minmax(380px, 1.4fr);
            align-items: start;
        }
        .insight-grid {
            grid-template-columns: minmax(260px, 0.8fr) minmax(420px, 1.4fr);
            margin-bottom: 1.5rem;
        }
        .guide-grid {
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        }
        .filter-grid,
        .weight-grid {
            display: grid;
            gap: 0.85rem;
        }
        .filter-grid {
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        }
        .weight-grid {
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        }
        .filter-control,
        .weight-control {
            display: grid;
            gap: 0.35rem;
        }
        .filter-control span,
        .weight-title {
            font-size: 0.85rem;
            font-weight: 700;
            color: #334155;
        }
        .filter-control input,
        .filter-control select,
        .weight-control input {
            width: 100%;
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 0.58rem 0.7rem;
            font: inherit;
            background: #fff;
            color: var(--text);
        }
        .toggle-row,
        .button-row {
            display: flex;
            gap: 0.8rem;
            flex-wrap: wrap;
            align-items: center;
        }
        .toggle {
            display: inline-flex;
            gap: 0.45rem;
            align-items: center;
            font-size: 0.92rem;
            color: #334155;
        }
        button {
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 0.55rem 0.9rem;
            background: #fff;
            color: var(--text);
            font: inherit;
            cursor: pointer;
        }
        button:hover {
            border-color: var(--teal-light);
            color: var(--teal);
        }
        .weight-note {
            display: inline-flex;
            align-items: center;
            width: fit-content;
            border-radius: 999px;
            padding: 0.15rem 0.5rem;
            font-size: 0.72rem;
            font-weight: 700;
        }
        .weight-note-varies {
            background: rgba(15, 118, 110, 0.1);
            color: var(--teal);
        }
        .weight-note-constant {
            background: rgba(100, 116, 139, 0.12);
            color: #475569;
        }
        .weight-note-inactive {
            background: rgba(231, 76, 60, 0.1);
            color: #b42318;
        }
        .view-stat-grid,
        .detail-stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 0.8rem;
            margin-bottom: 1rem;
        }
        .mini-stat {
            padding: 0.85rem;
            border-radius: 8px;
            background: #f8fafc;
            border: 1px solid #edf2f7;
        }
        .mini-stat .label {
            display: block;
            color: var(--text-light);
            font-size: 0.8rem;
            margin-bottom: 0.2rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .mini-stat .value {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text);
        }
        .detail-heading {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: flex-start;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }
        .detail-heading h3 {
            font-size: 1.2rem;
            margin-bottom: 0.25rem;
        }
        .detail-score {
            text-align: right;
        }
        .detail-score .value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--teal);
            line-height: 1;
        }
        .meta-inline {
            color: var(--text-light);
            font-size: 0.92rem;
        }
        .pill,
        .subtle-pill {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.25rem 0.65rem;
            font-size: 0.78rem;
            font-weight: 700;
            white-space: nowrap;
        }
        .pill-ready {
            background: rgba(15, 118, 110, 0.12);
            color: var(--teal);
        }
        .pill-review {
            background: rgba(243, 156, 18, 0.15);
            color: #b26d05;
        }
        .pill-neutral {
            background: rgba(100, 116, 139, 0.14);
            color: #475569;
        }
        .pill-drop {
            background: rgba(231, 76, 60, 0.12);
            color: #b42318;
        }
        .pill-curated {
            background: rgba(46, 204, 113, 0.16);
            color: #1f8b4c;
        }
        .subtle-pill {
            background: #eef2f7;
            color: #51606f;
            font-weight: 600;
        }
        .detail-chip-row {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1rem;
        }
        .score-list,
        .detail-list {
            display: grid;
            gap: 0.6rem;
            list-style: none;
            margin-top: 0.75rem;
        }
        .score-item,
        .detail-item {
            border: 1px solid #edf2f7;
            background: #f8fafc;
            border-radius: 8px;
            padding: 0.75rem 0.85rem;
        }
        .score-item strong,
        .detail-item strong {
            display: inline-block;
            margin-right: 0.35rem;
        }
        .score-value {
            font-weight: 700;
        }
        .score-value-positive { color: var(--teal); }
        .score-value-negative { color: #b42318; }
        .detail-grid {
            display: grid;
            gap: 1rem;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        }
        .bar-grid {
            display: grid;
            gap: 0.9rem;
        }
        .bar-row {
            display: grid;
            gap: 0.35rem;
        }
        .bar-label {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }
        .bar-stat {
            color: var(--text-light);
            font-size: 0.92rem;
        }
        .bar-track {
            background: #edf2f4;
            border-radius: 999px;
            height: 12px;
            overflow: hidden;
        }
        .bar-fill {
            height: 100%;
            border-radius: 999px;
        }
        .bar-fill-ready { background: linear-gradient(90deg, var(--teal), var(--teal-light)); }
        .bar-fill-review { background: var(--orange); }
        .bar-fill-neutral { background: var(--slate); }
        .bar-fill-drop { background: var(--red); }
        .bar-fill-curated { background: var(--green); }
        .table-shell {
            overflow-x: auto;
        }
        .table-toolbar {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            flex-wrap: wrap;
            margin-bottom: 0.85rem;
            color: var(--text-light);
            font-size: 0.92rem;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
        }
        th, td {
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
        }
        th {
            background: var(--bg);
            font-weight: 600;
            position: sticky;
            top: 0;
        }
        tbody tr {
            cursor: pointer;
        }
        tbody tr:hover {
            background: #fafbfd;
        }
        .selected-row {
            background: rgba(15, 118, 110, 0.07);
        }
        .priority-badge {
            display: inline-block;
            min-width: 3rem;
            text-align: center;
            background: var(--teal);
            color: white;
            padding: 0.16rem 0.45rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
        }
        .score-cell {
            font-weight: 700;
            color: var(--teal);
        }
        .delta-positive {
            color: var(--teal);
            font-weight: 700;
        }
        .delta-negative {
            color: #b42318;
            font-weight: 700;
        }
        .delta-neutral {
            color: var(--text-light);
            font-weight: 700;
        }
        .table-note {
            color: var(--text-light);
            font-size: 0.85rem;
        }
        .footer-note {
            color: var(--text-light);
            font-size: 0.9rem;
        }
        .empty-state {
            color: var(--text-light);
        }
        code {
            background: #eff6f6;
            border-radius: 4px;
            padding: 0.08rem 0.3rem;
        }
        @media (max-width: 980px) {
            .controls-grid,
            .insight-grid {
                grid-template-columns: 1fr;
            }
        }
        @media (max-width: 720px) {
            body { padding: 1rem; }
            .card, .chart-card { padding: 1rem; }
            th, td { padding: 0.55rem; }
            .detail-score { text-align: left; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="breadcrumb"><a href="index.html">Back to QC Dashboard</a></div>
        <header>
            <h1>Curation Priority Dashboard</h1>
            <p class="subtitle">
                Static MONDO candidate queue generated with the same prioritizer logic used by
                <code>dismech-mondo-prioritize</code>, with live browser-side reweighting so the score can be inspected and adjusted without regenerating the report.
            </p>
            <p class="meta">Generated: $generated_at</p>
            <p class="meta">Candidates: $candidates_path | Config: $config_path</p>
        </header>

        <section class="summary-cards">
            <div class="card">
                <h3>Candidates Analyzed</h3>
                <div class="value">$total_candidates</div>
            </div>
            <div class="card">
                <h3>Already Curated</h3>
                <div class="value">$already_curated</div>
            </div>
            <div class="card">
                <h3>Remaining</h3>
                <div class="value">$remaining_candidates</div>
            </div>
            <div class="card">
                <h3>Direct Root Actions</h3>
                <div class="value">$root_action_candidates</div>
            </div>
        </section>

        <section class="chart-card">
            <h2>Coverage Summary</h2>
            <p class="priority-note">
                $already_curated of $total_candidates candidates already have a local dismech root.
                Remaining candidates still include review and drop recommendations; the bar only reflects current root coverage.
            </p>
            <div class="progress-legend">
                <span><strong>$coverage_percent%</strong> already curated</span>
                <span>$remaining_candidates remaining</span>
            </div>
            <div class="progress-shell" aria-label="Curated coverage progress">
                <div class="progress-curated" style="width: $curated_width%;"></div>
                <div class="progress-remaining" style="width: $remaining_width%;"></div>
            </div>
        </section>

        <section class="chart-card">
            <h2>Explore the Ranking</h2>
            <p class="priority-note">
                Reweighting changes the score and rank in the browser. Recommended action and specificity bucket stay fixed because they come from the Python heuristics, not the weight sliders. Controls marked as constant or inactive will not change ordering within this export.
            </p>
            <div class="controls-grid">
                <div>
                    <h3 class="panel-heading">Filters</h3>
                    <div class="filter-grid">
                        <label class="filter-control">
                            <span>Search</span>
                            <input id="search-filter" type="search" placeholder="MONDO ID, label, parent, category">
                        </label>
                        <label class="filter-control">
                            <span>Action</span>
                            <select id="action-filter">
                                $action_options
                            </select>
                        </label>
                        <label class="filter-control">
                            <span>Specificity</span>
                            <select id="bucket-filter">
                                $bucket_options
                            </select>
                        </label>
$category_filter_block
                        <label class="filter-control">
                            <span>Visible Rows</span>
                            <select id="row-limit">
                                <option value="50">50</option>
                                <option value="100">100</option>
                                <option value="200" selected>200</option>
                                <option value="500">500</option>
                                <option value="1000">1000</option>
                                <option value="ALL">All</option>
                            </select>
                        </label>
                    </div>
                    <div class="toggle-row" style="margin-top: 1rem;">
                        <label class="toggle"><input id="show-curated" type="checkbox"> Show already curated</label>
                        <label class="toggle"><input id="root-only" type="checkbox"> Root actions only</label>
                    </div>
                    <div class="button-row" style="margin-top: 1rem;">
                        <button type="button" id="reset-filters">Reset Filters</button>
                        <button type="button" id="reset-weights">Reset Weights</button>
                    </div>
                </div>
                <div>
                    <h3 class="panel-heading">Weights</h3>
                    <p class="priority-note">
                        These inputs start from <code>conf/mondo_prioritizer.yaml</code>. The exported score remains visible in the table as the baseline for comparison.
                    </p>
                    <div class="weight-grid">
                        $weight_controls
                    </div>
                </div>
            </div>
        </section>

        <div class="insight-grid">
            <section class="chart-card">
                <h2>Current View</h2>
                <div id="view-summary"></div>
            </section>
            <section class="chart-card">
                <h2>Selected Candidate</h2>
                <div id="selected-candidate"></div>
            </section>
        </div>

        <section class="chart-card">
            <h2>Action Breakdown</h2>
            <div class="bar-grid" id="action-breakdown"></div>
        </section>

$category_section

        <section class="chart-card">
            <h2>Top Uncurated Diseases</h2>
            <p class="priority-note">
                The table starts with uncurated rows only. Click any row to inspect the current score contribution list and the fixed heuristics behind its action label.
            </p>
            <div class="table-toolbar" id="table-toolbar"></div>
            <div class="table-shell">
                <table>
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>MONDO ID</th>
                            <th>Label</th>
                            <th>Current Score</th>
                            <th>Delta vs Export</th>
                            <th>Recommended Action</th>
                            <th>Specificity Bucket</th>
                        </tr>
                    </thead>
                    <tbody id="priority-table-body"></tbody>
                </table>
            </div>
        </section>

        <section class="chart-card">
            <h2>Scoring Guide</h2>
            <div class="guide-grid">
                <div>
                    <p class="priority-note">
                        <strong>Broad parent</strong> means <code>child_count &gt;= $broad_parent_min_children</code> and the label is not treated as a subtype series or grouping term.
                        That heuristic can trigger <code>CURATE_ROOT_WITH_SUBTYPES</code>.
                    </p>
                    <p class="priority-note">
                        <strong>Subtype series</strong> means the label matches a configured family-stem pattern and that stem appears across at least
                        <code>$subtype_series_min_family_size</code> candidates. If a likely parent is present, the action drops to <code>LUMP_INTO_PARENT</code>.
                    </p>
                </div>
                <div>
                    <p class="priority-note">
                        <strong>Over-specific leaf</strong> only fires when <code>child_count == 0</code>, the label has at least
                        <code>$over_specific_leaf_min_words</code> words, and it contains multiple conjunctions or clause joins.
                    </p>
                    <p class="priority-note">
                        <strong>Missing from dismech</strong> and <strong>already curated</strong> are both kept in the generic scorer so mixed exports can rank curated and uncurated rows together. If one of those factors is constant or inactive in the current export, the weight controls call that out because changing it will not change the ordering.
                    </p>
                </div>
            </div>
        </section>

        <p class="footer-note">
            Powered by <code>dismech-mondo-prioritize</code> scoring heuristics. The HTML report is still static, but the ranking is now re-scored client-side from the exported raw feature counts.
        </p>
    </div>

    <script id="priority-dashboard-data" type="application/json">$payload_json</script>
    <script>
        (function () {
            const payload = JSON.parse(document.getElementById("priority-dashboard-data").textContent);
            const scoring = payload.scoring || {};
            const defaultWeights = Object.assign({}, scoring.weights || {});
            const thresholds = scoring.thresholds || {};
            const caps = scoring.caps || {};
            const weightLabels = scoring.weight_labels || {};
            const actionOrder = scoring.action_order || {};
            const rootActions = new Set(["CURATE_ROOT", "CURATE_ROOT_WITH_SUBTYPES"]);
            const rows = payload.rows || [];

            const state = {
                weights: Object.assign({}, defaultWeights),
                search: "",
                action: "ALL",
                bucket: "ALL",
                category: "ALL",
                showCurated: false,
                rootOnly: false,
                rowLimit: "200",
                selectedId: null,
            };

            const elements = {
                search: document.getElementById("search-filter"),
                action: document.getElementById("action-filter"),
                bucket: document.getElementById("bucket-filter"),
                category: document.getElementById("category-filter"),
                showCurated: document.getElementById("show-curated"),
                rootOnly: document.getElementById("root-only"),
                rowLimit: document.getElementById("row-limit"),
                resetFilters: document.getElementById("reset-filters"),
                resetWeights: document.getElementById("reset-weights"),
                viewSummary: document.getElementById("view-summary"),
                selectedCandidate: document.getElementById("selected-candidate"),
                actionBreakdown: document.getElementById("action-breakdown"),
                categoryBody: document.getElementById("category-table-body"),
                tableToolbar: document.getElementById("table-toolbar"),
                tableBody: document.getElementById("priority-table-body"),
            };

            function escapeHtml(value) {
                return String(value == null ? "" : value)
                    .replace(/&/g, "&amp;")
                    .replace(/</g, "&lt;")
                    .replace(/>/g, "&gt;")
                    .replace(/"/g, "&quot;")
                    .replace(/'/g, "&#39;");
            }

            function toNumber(value) {
                const numeric = Number(value);
                return Number.isFinite(numeric) ? numeric : 0;
            }

            function round2(value) {
                return Math.round((value + Number.EPSILON) * 100) / 100;
            }

            function formatNumber(value) {
                const fixed = round2(toNumber(value)).toFixed(2);
                if (fixed.endsWith(".00")) {
                    return fixed.slice(0, -1);
                }
                if (fixed.endsWith("0")) {
                    return fixed.slice(0, -1);
                }
                return fixed;
            }

            function formatInteger(value) {
                return String(Math.round(toNumber(value)));
            }

            function formatSigned(value) {
                const numeric = round2(toNumber(value));
                if (numeric > 0) {
                    return "+" + formatNumber(numeric);
                }
                return formatNumber(numeric);
            }

            function formatPercent(value) {
                return round2(toNumber(value)).toFixed(1);
            }

            function parseLimit(value) {
                if (value === "ALL") {
                    return Number.POSITIVE_INFINITY;
                }
                const parsed = parseInt(value, 10);
                return Number.isFinite(parsed) ? parsed : 200;
            }

            function capValue(name, count) {
                const numeric = Math.max(toNumber(count), 0);
                const cap = caps[name];
                if (cap == null) {
                    return numeric;
                }
                return Math.min(numeric, Math.max(toNumber(cap), 0));
            }

            rows.forEach(function (row) {
                const features = row.features || {};
                row.search_text = [
                    row.mondo_id,
                    row.label,
                    (row.parents || []).join(" "),
                    (row.categories || []).join(" "),
                    row.curated_match || "",
                ]
                    .join(" ")
                    .toLowerCase();
                row.score_inputs = {
                    missing_from_dismech: features.missing_from_dismech ? 1 : 0,
                    has_definition: features.has_definition ? 1 : 0,
                    synonym_count: capValue("synonym_count", features.synonym_count),
                    xref_count: capValue("xref_count", features.xref_count),
                    clingen_definitive_count: capValue(
                        "clingen_definitive_count",
                        features.clingen_definitive_count
                    ),
                    clingen_strong_count: capValue(
                        "clingen_strong_count",
                        features.clingen_strong_count
                    ),
                    subset_match_count: capValue(
                        "subset_match_count",
                        features.subset_match_count
                    ),
                    orphanet_match_count: capValue(
                        "orphanet_match_count",
                        features.orphanet_match_count
                    ),
                    broad_parent_bonus: features.broad_parent ? 1 : 0,
                    subtype_series_penalty: features.subtype_series ? 1 : 0,
                    grouping_term_penalty: features.grouping_term ? 1 : 0,
                    over_specific_leaf_penalty: features.over_specific_leaf ? 1 : 0,
                    obsolete_penalty: features.obsolete ? 1 : 0,
                    already_curated_penalty: features.already_curated ? 1 : 0,
                };
            });

            const scoreFactors = [
                {
                    key: "missing_from_dismech",
                    describe: function () {
                        return "No curated dismech root matched this MONDO term.";
                    },
                },
                {
                    key: "has_definition",
                    describe: function () {
                        return "MONDO definition present.";
                    },
                },
                {
                    key: "synonym_count",
                    describe: function (row, input, weight) {
                        return formatInteger(input) + " capped synonyms × " + formatNumber(weight);
                    },
                },
                {
                    key: "xref_count",
                    describe: function (row, input, weight) {
                        return formatInteger(input) + " capped xrefs × " + formatNumber(weight);
                    },
                },
                {
                    key: "clingen_definitive_count",
                    describe: function (row, input, weight) {
                        return formatInteger(input) + " capped ClinGen definitive counts × " + formatNumber(weight);
                    },
                },
                {
                    key: "clingen_strong_count",
                    describe: function (row, input, weight) {
                        return formatInteger(input) + " capped ClinGen strong counts × " + formatNumber(weight);
                    },
                },
                {
                    key: "subset_match_count",
                    describe: function (row, input, weight) {
                        return formatInteger(input) + " capped priority subset matches × " + formatNumber(weight);
                    },
                },
                {
                    key: "orphanet_match_count",
                    describe: function (row, input, weight) {
                        return formatInteger(input) + " capped Orphanet or ORDO matches × " + formatNumber(weight);
                    },
                },
                {
                    key: "broad_parent_bonus",
                    describe: function (row) {
                        return "child_count=" + formatInteger(row.features.child_count) + " meets the broad-parent threshold and the row was not flagged as subtype series or grouping term.";
                    },
                },
                {
                    key: "subtype_series_penalty",
                    describe: function (row) {
                        if (row.family_stem) {
                            return "Series stem '" + row.family_stem + "' appears across " + formatInteger(row.family_size) + " candidates.";
                        }
                        return "Subtype-series heuristic active.";
                    },
                },
                {
                    key: "grouping_term_penalty",
                    describe: function () {
                        return "Label matched a configured grouping-term pattern such as susceptibility or predisposition.";
                    },
                },
                {
                    key: "over_specific_leaf_penalty",
                    describe: function () {
                        return "Leaf label is long and conjunction-heavy.";
                    },
                },
                {
                    key: "obsolete_penalty",
                    describe: function () {
                        return "Candidate is marked obsolete.";
                    },
                },
                {
                    key: "already_curated_penalty",
                    describe: function (row) {
                        return row.curated_match ? "Already curated in " + row.curated_match + "." : "Already curated.";
                    },
                },
            ];

            function actionTone(action) {
                if (action === "CURATE_ROOT" || action === "CURATE_ROOT_WITH_SUBTYPES") {
                    return "ready";
                }
                if (action.indexOf("REVIEW_") === 0) {
                    return "review";
                }
                if (action === "LUMP_INTO_PARENT") {
                    return "neutral";
                }
                if (action.indexOf("DROP_") === 0) {
                    return "drop";
                }
                if (action === "ALREADY_CURATED") {
                    return "curated";
                }
                return "neutral";
            }

            function scoreRow(row) {
                let total = 0;
                const contributions = [];
                scoreFactors.forEach(function (factor) {
                    const input = toNumber(row.score_inputs[factor.key]);
                    const weight = toNumber(state.weights[factor.key]);
                    if (!input || !weight) {
                        return;
                    }
                    const amount = input * weight;
                    total += amount;
                    contributions.push({
                        key: factor.key,
                        label: weightLabels[factor.key] || factor.key,
                        amount: amount,
                        detail: factor.describe(row, input, weight),
                    });
                });
                return {
                    score: round2(total),
                    contributions: contributions,
                };
            }

            function weightStatus(key) {
                const values = rows.map(function (row) {
                    return toNumber((row.score_inputs || {})[key]);
                });
                const activeCount = values.filter(function (value) {
                    return value !== 0;
                }).length;
                if (!activeCount) {
                    return { label: "Inactive in this export", tone: "inactive" };
                }
                const uniqueCount = new Set(values).size;
                if (uniqueCount === 1) {
                    return { label: "Constant across export", tone: "constant" };
                }
                return { label: "Varies across export", tone: "varies" };
            }

            function annotateWeightControls() {
                document.querySelectorAll("[data-weight-key]").forEach(function (input) {
                    const key = input.getAttribute("data-weight-key");
                    const control = input.closest(".weight-control");
                    if (!control) {
                        return;
                    }
                    const meta = weightStatus(key);
                    let note = control.querySelector(".weight-note");
                    if (!note) {
                        note = document.createElement("span");
                        control.insertBefore(note, input);
                    }
                    note.className = "weight-note weight-note-" + meta.tone;
                    note.textContent = meta.label;
                });
            }

            function getScoredEntries() {
                return rows.map(function (row) {
                    const scored = scoreRow(row);
                    return {
                        row: row,
                        score: scored.score,
                        contributions: scored.contributions,
                    };
                });
            }

            function matchesFilters(entry) {
                const row = entry.row;
                if (!state.showCurated && row.recommended_action === "ALREADY_CURATED") {
                    return false;
                }
                if (state.rootOnly && !rootActions.has(row.recommended_action)) {
                    return false;
                }
                if (state.action !== "ALL" && row.recommended_action !== state.action) {
                    return false;
                }
                if (state.bucket !== "ALL" && row.specificity_bucket !== state.bucket) {
                    return false;
                }
                if (state.category !== "ALL" && !(row.categories || []).includes(state.category)) {
                    return false;
                }
                if (state.search && row.search_text.indexOf(state.search) === -1) {
                    return false;
                }
                return true;
            }

            function compareEntries(left, right) {
                if (right.score !== left.score) {
                    return right.score - left.score;
                }
                if (toNumber(right.row.score) !== toNumber(left.row.score)) {
                    return toNumber(right.row.score) - toNumber(left.row.score);
                }
                return String(left.row.label).localeCompare(String(right.row.label));
            }

            function renderViewSummary(entries) {
                if (!entries.length) {
                    elements.viewSummary.innerHTML = '<p class="empty-state">No candidates match the current filters.</p>';
                    return;
                }
                const topEntry = entries[0];
                const averageScore =
                    entries.reduce(function (sum, entry) {
                        return sum + entry.score;
                    }, 0) / entries.length;
                const rootCount = entries.filter(function (entry) {
                    return rootActions.has(entry.row.recommended_action);
                }).length;
                elements.viewSummary.innerHTML =
                    '<div class="view-stat-grid">' +
                    '<div class="mini-stat"><span class="label">Visible</span><span class="value">' + formatInteger(entries.length) + '</span></div>' +
                    '<div class="mini-stat"><span class="label">Root Actions</span><span class="value">' + formatInteger(rootCount) + '</span></div>' +
                    '<div class="mini-stat"><span class="label">Average Score</span><span class="value">' + formatNumber(averageScore) + '</span></div>' +
                    '</div>' +
                    '<p class="priority-note">Current top candidate: <strong>' +
                    escapeHtml(topEntry.row.label) +
                    '</strong> (' +
                    escapeHtml(topEntry.row.mondo_id) +
                    ') at <strong>' +
                    formatNumber(topEntry.score) +
                    '</strong>.</p>' +
                    '<p class="priority-note">Action labels stay fixed while you move the weights. The table rank and the detailed contribution list update immediately.</p>';
            }

            function renderSelectedCandidate(entry) {
                if (!entry) {
                    elements.selectedCandidate.innerHTML =
                        '<p class="empty-state">No selected candidate. Adjust the filters or choose a visible row.</p>';
                    return;
                }
                const row = entry.row;
                const features = row.features || {};
                const delta = round2(entry.score - toNumber(row.score));
                const contributions = entry.contributions
                    .slice()
                    .sort(function (left, right) {
                        return Math.abs(right.amount) - Math.abs(left.amount);
                    });
                const contributionsHtml = contributions.length
                    ? '<ul class="score-list">' +
                      contributions
                          .map(function (contribution) {
                              const tone = contribution.amount >= 0 ? "positive" : "negative";
                              return (
                                  '<li class="score-item">' +
                                  '<strong>' + escapeHtml(contribution.label) + '</strong>' +
                                  '<span class="score-value score-value-' + tone + '">' +
                                  formatSigned(contribution.amount) +
                                  '</span>' +
                                  '<div class="table-note">' + escapeHtml(contribution.detail) + '</div>' +
                                  '</li>'
                              );
                          })
                          .join("") +
                      '</ul>'
                    : '<p class="empty-state">No active score contributions at the current weights.</p>';
                const broadParentText = features.broad_parent
                    ? "Yes. child_count=" +
                      formatInteger(features.child_count) +
                      " meets the threshold of " +
                      formatInteger(thresholds.broad_parent_min_children || 4) +
                      " and the row was not flagged as subtype series or grouping term."
                    : "No. This heuristic requires child_count >= " +
                      formatInteger(thresholds.broad_parent_min_children || 4) +
                      " and no subtype-series or grouping-term flag.";
                const subtypeText = features.subtype_series
                    ? "Yes. Stem '" +
                      escapeHtml(row.family_stem || "") +
                      "' appears across " +
                      formatInteger(row.family_size) +
                      " candidates."
                    : "No. This heuristic needs a shared family stem across at least " +
                      formatInteger(thresholds.subtype_series_min_family_size || 2) +
                      " candidates.";
                const groupingText = features.grouping_term
                    ? "Yes. The label matched a configured grouping-term pattern."
                    : "No grouping-term pattern matched.";
                const leafText = features.over_specific_leaf
                    ? "Yes. The row is a childless term with a long, conjunction-heavy label."
                    : "No. This heuristic only applies to childless labels with at least " +
                      formatInteger(thresholds.over_specific_leaf_min_words || 8) +
                      " words and multiple conjunctions.";
                const curatedText = row.curated_match
                    ? "Already curated in " + row.curated_match + "."
                    : "No curated dismech root matched.";
                const parentsText = (row.parents || []).length
                    ? (row.parents || []).join(", ")
                    : "No parent labels supplied in the export.";
                const categoriesText = (row.categories || []).length
                    ? (row.categories || []).join(", ")
                    : "No categories supplied in the export.";

                elements.selectedCandidate.innerHTML =
                    '<div class="detail-heading">' +
                    '<div>' +
                    '<h3>' + escapeHtml(row.label) + '</h3>' +
                    '<p class="meta-inline"><a href="' + escapeHtml(row.mondo_url) + '" target="_blank" rel="noopener">' + escapeHtml(row.mondo_id) + '</a></p>' +
                    '</div>' +
                    '<div class="detail-score">' +
                    '<div class="value">' + formatNumber(entry.score) + '</div>' +
                    '<div class="table-note">current score</div>' +
                    '</div>' +
                    '</div>' +
                    '<div class="detail-chip-row">' +
                    '<span class="pill pill-' + escapeHtml(row.recommended_action_tone) + '">' + escapeHtml(row.recommended_action) + '</span>' +
                    '<span class="subtle-pill">' + escapeHtml(row.specificity_bucket) + '</span>' +
                    '</div>' +
                    '<div class="detail-stat-grid">' +
                    '<div class="mini-stat"><span class="label">Export Score</span><span class="value">' + formatNumber(row.score) + '</span></div>' +
                    '<div class="mini-stat"><span class="label">Delta</span><span class="value">' + formatSigned(delta) + '</span></div>' +
                    '<div class="mini-stat"><span class="label">Child Count</span><span class="value">' + formatInteger(features.child_count) + '</span></div>' +
                    '<div class="mini-stat"><span class="label">Family Size</span><span class="value">' + formatInteger(row.family_size) + '</span></div>' +
                    '</div>' +
                    '<div class="detail-grid">' +
                    '<div>' +
                    '<p class="priority-note">Current contribution list</p>' +
                    contributionsHtml +
                    '</div>' +
                    '<div>' +
                    '<p class="priority-note">Fixed heuristic context</p>' +
                    '<ul class="detail-list">' +
                    '<li class="detail-item"><strong>Broad parent:</strong> ' + broadParentText + '</li>' +
                    '<li class="detail-item"><strong>Subtype series:</strong> ' + subtypeText + '</li>' +
                    '<li class="detail-item"><strong>Grouping term:</strong> ' + groupingText + '</li>' +
                    '<li class="detail-item"><strong>Over-specific leaf:</strong> ' + leafText + '</li>' +
                    '<li class="detail-item"><strong>Curated status:</strong> ' + escapeHtml(curatedText) + '</li>' +
                    '<li class="detail-item"><strong>Parents:</strong> ' + escapeHtml(parentsText) + '</li>' +
                    '<li class="detail-item"><strong>Categories:</strong> ' + escapeHtml(categoriesText) + '</li>' +
                    '</ul>' +
                    '</div>' +
                    '</div>';
            }

            function renderActionBreakdown(entries) {
                if (!entries.length) {
                    elements.actionBreakdown.innerHTML =
                        '<p class="empty-state">No action breakdown available for the current filters.</p>';
                    return;
                }
                const counts = {};
                entries.forEach(function (entry) {
                    counts[entry.row.recommended_action] = (counts[entry.row.recommended_action] || 0) + 1;
                });
                const maximum = Math.max.apply(
                    null,
                    Object.values(counts)
                );
                const total = entries.length;
                const actionHtml = Object.keys(counts)
                    .sort(function (left, right) {
                        const leftOrder = Object.prototype.hasOwnProperty.call(actionOrder, left)
                            ? actionOrder[left]
                            : 999;
                        const rightOrder = Object.prototype.hasOwnProperty.call(actionOrder, right)
                            ? actionOrder[right]
                            : 999;
                        const orderDelta = leftOrder - rightOrder;
                        if (orderDelta) {
                            return orderDelta;
                        }
                        return right.localeCompare(left);
                    })
                    .map(function (action) {
                        const count = counts[action];
                        const tone = actionTone(action);
                        return (
                            '<div class="bar-row">' +
                            '<div class="bar-label">' +
                            '<span class="pill pill-' + tone + '">' + escapeHtml(action) + '</span>' +
                            '<span class="bar-stat">' + formatInteger(count) + ' (' + formatPercent((count / total) * 100) + '%)</span>' +
                            '</div>' +
                            '<div class="bar-track"><div class="bar-fill bar-fill-' + tone + '" style="width: ' + formatPercent((count / maximum) * 100) + '%;"></div></div>' +
                            '</div>'
                        );
                    })
                    .join("");
                elements.actionBreakdown.innerHTML = actionHtml;
            }

            function renderCategorySummary(entries) {
                if (!elements.categoryBody) {
                    return;
                }
                const grouped = {};
                entries.forEach(function (entry) {
                    (entry.row.categories || []).forEach(function (category) {
                        const key = category.toLowerCase();
                        if (!grouped[key]) {
                            grouped[key] = {
                                category: category,
                                entries: [],
                                rootCount: 0,
                            };
                        }
                        grouped[key].entries.push(entry);
                        if (rootActions.has(entry.row.recommended_action)) {
                            grouped[key].rootCount += 1;
                        }
                    });
                });
                const summaries = Object.values(grouped).sort(function (left, right) {
                    if (right.entries.length !== left.entries.length) {
                        return right.entries.length - left.entries.length;
                    }
                    return right.entries[0].score - left.entries[0].score;
                });
                if (!summaries.length) {
                    elements.categoryBody.innerHTML =
                        '<tr><td colspan="4">No category data available for the current filters.</td></tr>';
                    return;
                }
                elements.categoryBody.innerHTML = summaries
                    .map(function (summary) {
                        const topEntry = summary.entries[0];
                        return (
                            '<tr>' +
                            '<td>' + escapeHtml(summary.category) + '</td>' +
                            '<td>' + formatInteger(summary.entries.length) + '</td>' +
                            '<td>' + formatInteger(summary.rootCount) + '</td>' +
                            '<td><a href="' + escapeHtml(topEntry.row.mondo_url) + '" target="_blank" rel="noopener">' +
                            escapeHtml(topEntry.row.label) +
                            '</a> <span class="table-note">(' + formatNumber(topEntry.score) + ')</span></td>' +
                            '</tr>'
                        );
                    })
                    .join("");
            }

            function renderTable(entries) {
                const limit = parseLimit(state.rowLimit);
                const visibleEntries = entries.slice(0, limit);
                elements.tableToolbar.innerHTML =
                    '<span><strong>' + formatInteger(entries.length) + '</strong> rows match the current filters.</span>' +
                    '<span>Showing ' + formatInteger(visibleEntries.length) + (limit === Number.POSITIVE_INFINITY ? "" : " of " + formatInteger(entries.length)) + '.</span>';
                if (!visibleEntries.length) {
                    elements.tableBody.innerHTML =
                        '<tr><td colspan="7">No MONDO candidates match the current filters.</td></tr>';
                    return;
                }
                elements.tableBody.innerHTML = visibleEntries
                    .map(function (entry, index) {
                        const row = entry.row;
                        const delta = round2(entry.score - toNumber(row.score));
                        const deltaClass = delta > 0 ? "delta-positive" : delta < 0 ? "delta-negative" : "delta-neutral";
                        const badge = index < 10
                            ? '<span class="priority-badge">#' + formatInteger(index + 1) + '</span>'
                            : formatInteger(index + 1);
                        const selectedClass = state.selectedId === row.mondo_id ? ' class="selected-row"' : "";
                        return (
                            '<tr data-mondo-id="' + escapeHtml(row.mondo_id) + '"' + selectedClass + '>' +
                            '<td>' + badge + '</td>' +
                            '<td><a href="' + escapeHtml(row.mondo_url) + '" target="_blank" rel="noopener">' + escapeHtml(row.mondo_id) + '</a></td>' +
                            '<td>' + escapeHtml(row.label) + '</td>' +
                            '<td class="score-cell">' + formatNumber(entry.score) + '</td>' +
                            '<td class="' + deltaClass + '">' + formatSigned(delta) + '</td>' +
                            '<td><span class="pill pill-' + escapeHtml(row.recommended_action_tone) + '">' + escapeHtml(row.recommended_action) + '</span></td>' +
                            '<td><span class="subtle-pill">' + escapeHtml(row.specificity_bucket) + '</span></td>' +
                            '</tr>'
                        );
                    })
                    .join("");
            }

            function syncSelectedCandidate(entries) {
                if (!entries.length) {
                    state.selectedId = null;
                    return null;
                }
                const selected = entries.find(function (entry) {
                    return entry.row.mondo_id === state.selectedId;
                });
                if (selected) {
                    return selected;
                }
                state.selectedId = entries[0].row.mondo_id;
                return entries[0];
            }

            function render() {
                const entries = getScoredEntries()
                    .filter(matchesFilters)
                    .sort(compareEntries);
                const visibleEntries = entries.slice(0, parseLimit(state.rowLimit));
                renderViewSummary(entries);
                renderActionBreakdown(entries);
                renderCategorySummary(entries);
                const selectedEntry = syncSelectedCandidate(
                    visibleEntries.length ? visibleEntries : entries
                );
                renderSelectedCandidate(selectedEntry);
                renderTable(entries);
            }

            let renderQueued = false;
            function scheduleRender() {
                if (renderQueued) {
                    return;
                }
                renderQueued = true;
                window.requestAnimationFrame(function () {
                    renderQueued = false;
                    render();
                });
            }

            function bindEvents() {
                document.querySelectorAll("[data-weight-key]").forEach(function (input) {
                    input.addEventListener("input", function () {
                        const key = input.getAttribute("data-weight-key");
                        state.weights[key] = toNumber(input.value);
                        scheduleRender();
                    });
                });
                elements.search.addEventListener("input", function () {
                    state.search = String(elements.search.value || "").trim().toLowerCase();
                    scheduleRender();
                });
                elements.action.addEventListener("change", function () {
                    state.action = elements.action.value;
                    scheduleRender();
                });
                elements.bucket.addEventListener("change", function () {
                    state.bucket = elements.bucket.value;
                    scheduleRender();
                });
                if (elements.category) {
                    elements.category.addEventListener("change", function () {
                        state.category = elements.category.value;
                        scheduleRender();
                    });
                }
                elements.showCurated.addEventListener("change", function () {
                    state.showCurated = elements.showCurated.checked;
                    scheduleRender();
                });
                elements.rootOnly.addEventListener("change", function () {
                    state.rootOnly = elements.rootOnly.checked;
                    scheduleRender();
                });
                elements.rowLimit.addEventListener("change", function () {
                    state.rowLimit = elements.rowLimit.value;
                    scheduleRender();
                });
                elements.resetFilters.addEventListener("click", function () {
                    state.search = "";
                    state.action = "ALL";
                    state.bucket = "ALL";
                    state.category = "ALL";
                    state.showCurated = false;
                    state.rootOnly = false;
                    state.rowLimit = "200";
                    elements.search.value = "";
                    elements.action.value = "ALL";
                    elements.bucket.value = "ALL";
                    if (elements.category) {
                        elements.category.value = "ALL";
                    }
                    elements.showCurated.checked = false;
                    elements.rootOnly.checked = false;
                    elements.rowLimit.value = "200";
                    scheduleRender();
                });
                elements.resetWeights.addEventListener("click", function () {
                    state.weights = Object.assign({}, defaultWeights);
                    document.querySelectorAll("[data-weight-key]").forEach(function (input) {
                        const key = input.getAttribute("data-weight-key");
                        input.value = String(defaultWeights[key]);
                    });
                    scheduleRender();
                });
                elements.tableBody.addEventListener("click", function (event) {
                    const row = event.target.closest("tr[data-mondo-id]");
                    if (!row) {
                        return;
                    }
                    state.selectedId = row.getAttribute("data-mondo-id");
                    render();
                });
            }

            annotateWeightControls();
            bindEvents();
            render();
        })();
    </script>
</body>
</html>
"""
    )
    return template.substitute(
        generated_at=html.escape(str(payload["generated_at"])),
        candidates_path=html.escape(str(payload["candidates_path"])),
        config_path=html.escape(str(payload["config_path"])),
        total_candidates=str(summary["total_candidates"]),
        already_curated=str(summary["already_curated"]),
        remaining_candidates=str(summary["remaining_candidates"]),
        root_action_candidates=str(summary["root_action_candidates"]),
        coverage_percent=f"{summary['coverage_percent']:.1f}",
        curated_width=f"{curated_width:.1f}",
        remaining_width=f"{remaining_width:.1f}",
        action_options=action_options,
        bucket_options=bucket_options,
        category_filter_block=category_filter_block.rstrip(),
        category_section=category_section.rstrip(),
        weight_controls=weight_controls,
        broad_parent_min_children=str(
            int(thresholds.get("broad_parent_min_children", 4))
        ),
        subtype_series_min_family_size=str(
            int(thresholds.get("subtype_series_min_family_size", 2))
        ),
        over_specific_leaf_min_words=str(
            int(thresholds.get("over_specific_leaf_min_words", 8))
        ),
        payload_json=payload_json,
    )


def _build_index_block(summary: dict[str, Any]) -> str:
    top_candidate = ""
    if summary["top_remaining_label"] and summary["top_remaining_score"] is not None:
        top_candidate = (
            " Top remaining candidate: "
            f"<strong>{html.escape(summary['top_remaining_label'])}</strong>"
            f" ({summary['top_remaining_score']:.1f})."
        )
    return f"""
        {PRIORITY_BLOCK_START}
        <section class="chart-card">
            <h2>MONDO Curation Priorities</h2>
            <p class="priority-note">
                <strong>{summary["remaining_candidates"]}</strong> of <strong>{summary["total_candidates"]}</strong>
                MONDO candidates remain after accounting for
                <strong>{summary["already_curated"]}</strong> already curated diseases.{top_candidate}
            </p>
            <p><a href="priority.html">View the curation priority dashboard</a></p>
        </section>
        {PRIORITY_BLOCK_END}
"""


def inject_priority_link(
    dashboard_index_path: Path,
    summary: dict[str, Any],
) -> bool:
    """Insert or update the priority-dashboard section in the dashboard index page."""
    if not dashboard_index_path.exists():
        return False

    content = dashboard_index_path.read_text(encoding="utf-8")
    block = _build_index_block(summary)
    pattern = re.compile(
        rf"{re.escape(PRIORITY_BLOCK_START)}.*?{re.escape(PRIORITY_BLOCK_END)}",
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


def generate_priority_dashboard_report(
    candidates_path: Path,
    kb_dir: Path,
    dashboard_dir: Path,
    config_path: Path,
    dashboard_index_path: Path | None = None,
) -> dict[str, Any]:
    """Build MONDO curation priority dashboard pages."""
    config = load_config(config_path)
    rows = _build_rows(
        candidates_path=candidates_path,
        kb_dir=kb_dir,
        config_path=config_path,
    )
    summary = _build_summary(rows)
    action_breakdown = _build_action_breakdown(rows)
    category_summary = _build_category_summary(rows)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    dashboard_dir.mkdir(parents=True, exist_ok=True)
    json_path = dashboard_dir / "priority.json"
    html_path = dashboard_dir / "priority.html"

    payload = {
        "generated_at": generated_at,
        "candidates_path": str(candidates_path),
        "config_path": str(config_path),
        "summary": summary,
        "action_breakdown": action_breakdown,
        "category_summary": category_summary,
        "scoring": {
            "weights": dict(config.get("weights") or {}),
            "caps": dict(config.get("caps") or {}),
            "thresholds": dict(config.get("thresholds") or {}),
            "weight_labels": dict(_WEIGHT_LABELS),
            "action_order": dict(_ACTION_ORDER),
        },
        "rows": rows,
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    html_path.write_text(
        _render_priority_report_page(payload),
        encoding="utf-8",
    )

    index_updated = False
    if dashboard_index_path is not None:
        index_updated = inject_priority_link(dashboard_index_path, summary)

    return {
        "json_path": json_path,
        "html_path": html_path,
        "summary": summary,
        "index_updated": index_updated,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate static MONDO curation priority dashboard pages."
    )
    parser.add_argument(
        "--candidates",
        default="examples/mondo_prioritizer_candidates.tsv",
        type=Path,
        help="Candidate export to score with the MONDO prioritizer.",
    )
    parser.add_argument("--kb-dir", default="kb/disorders", type=Path)
    parser.add_argument(
        "--config",
        default="conf/mondo_prioritizer.yaml",
        type=Path,
        help="Prioritizer config file.",
    )
    parser.add_argument("--dashboard-dir", default="dashboard", type=Path)
    parser.add_argument(
        "--dashboard-index",
        default="dashboard/index.html",
        type=Path,
        help="Dashboard index file to patch with a link to the priority dashboard.",
    )
    args = parser.parse_args()

    generate_priority_dashboard_report(
        candidates_path=args.candidates,
        kb_dir=args.kb_dir,
        dashboard_dir=args.dashboard_dir,
        config_path=args.config,
        dashboard_index_path=args.dashboard_index,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
