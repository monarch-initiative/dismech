"""Reproduce the bounded senescence inventory; read only disorder/module YAML.

Run from the repository root:
  uv run python docs/reports/senescent-cell-representation/scan_kb.py
"""

from collections import Counter
import json
from pathlib import Path
import subprocess

from dismech.kb_cache import default_off, load_document


ROOT = Path(__file__).resolve().parents[3]
TERMS = {"GO:0090398", "GO:0090399", "GO:0090400", "GO:0090402", "GO:0090403"}
CRITERION = (
    "Pathophysiology name contains senesc (case-insensitive) OR biological_processes "
    "directly uses one of GO:0090398, GO:0090399, GO:0090400, GO:0090402, GO:0090403. "
    "Text mentions elsewhere and inferred ancestor closure excluded."
)


def main() -> None:
    default_off()
    summary, rows = {}, []
    for scope in ["disorders", "modules"]:
        paths = sorted((ROOT / "kb" / scope).glob("*.yaml"))
        counts = Counter(files=len(paths))
        matched_files = set()
        for path in paths:
            document = load_document(path) or {}
            for node in document.get("pathophysiology", []) or []:
                processes = [
                    x.get("term", {}).get("id")
                    for x in node.get("biological_processes", []) or []
                ]
                if "senesc" not in node.get(
                    "name", ""
                ).lower() and not TERMS.intersection(processes):
                    continue
                matched_files.add(path)
                cells = node.get("cell_types", []) or []
                labels = [cell.get("preferred_term", "") for cell in cells]
                counts["senescence_name_or_GO_nodes"] += 1
                counts["with_cell_types"] += bool(cells)
                counts["with_multiple_cell_types"] += len(cells) > 1
                counts["with_senescent_display_label"] += any(
                    "senesc" in label.lower() for label in labels
                )
                counts["with_locations"] += bool(node.get("locations"))
                counts["with_conforms_to"] += bool(node.get("conforms_to"))
                rows.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "node": node.get("name"),
                        "cell_terms": [
                            cell.get("term", {}).get("id") for cell in cells
                        ],
                        "cell_labels": labels,
                        "process_terms": processes,
                        "conforms_to": node.get("conforms_to"),
                    }
                )
        counts["matching_files"] = len(matched_files)
        summary[scope] = dict(counts)
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    print(
        json.dumps(
            {
                "base_commit": commit,
                "criterion": CRITERION,
                "summary": summary,
                "rows": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
