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

        for value in node.values():
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
    disorders: list[tuple[Path, dict[str, Any]]] = []
    curated_mondo_ids: set[str] = set()

    for disorder_path in _iter_disorder_files(kb_dir):
        disorder = yaml.safe_load(disorder_path.read_text(encoding="utf-8")) or {}
        if not isinstance(disorder, dict):
            continue
        disorders.append((disorder_path, disorder))
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
        table_body = (
            '<tr><td colspan="4">No uncurated disease links found.</td></tr>'
        )

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


def inject_uncurated_link(
    dashboard_index_path: Path,
    summary: dict[str, Any],
) -> bool:
    """Insert or update the uncurated-links section in the dashboard index page."""
    if not dashboard_index_path.exists():
        return False

    content = dashboard_index_path.read_text(encoding="utf-8")
    block = _build_index_block(summary)
    pattern = re.compile(
        rf"{re.escape(UNCURATED_BLOCK_START)}.*?{re.escape(UNCURATED_BLOCK_END)}",
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


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate QC dashboard report of MONDO disease references that do not yet "
            "resolve to local DisMech pages."
        )
    )
    parser.add_argument("--kb-dir", default="kb/disorders", type=Path)
    parser.add_argument("--dashboard-dir", default="dashboard", type=Path)
    parser.add_argument(
        "--dashboard-index",
        default="dashboard/index.html",
        type=Path,
        help="Dashboard index file to patch with a link to the report.",
    )
    args = parser.parse_args()

    result = generate_uncurated_dashboard_report(
        kb_dir=args.kb_dir,
        dashboard_dir=args.dashboard_dir,
        dashboard_index_path=args.dashboard_index,
    )

    summary = result["summary"]
    print(
        "Generated uncurated disease link QC report:"
        f" {summary['total_uncurated_disease_terms']} terms,"
        f" {summary['total_linking_pages']} linking pages"
    )
    print(f"- HTML: {result['html_path']}")
    print(f"- JSON: {result['json_path']}")
    if args.dashboard_index.exists():
        print(
            "- Dashboard index link updated:"
            f" {'yes' if result['index_updated'] else 'no (already up to date)'}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
