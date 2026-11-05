"""Measure how one dismech entry grew, commit by commit.

For every commit that touched the entry, reads the file as it stood at that
commit (``git show <commit>:<path>``) and reports the size and wiring of its
pathograph: pathophysiology nodes, phenotypes, graph edges, phenotypes with a
causal in-edge, evidence items, unique PMIDs, and conformance to mechanism
modules. Each row also counts the kb/disorders/ files the commit changed, which
separates commits about this entry from sweeps across the knowledge base. Kept
in the repo so the numbers in each run's FINDINGS.md can be regenerated rather
than trusted.

Every commit is measured with the repository's current graph and QC code
(``dismech.graph.build_causal_graph`` and
``dismech.qc_plugins.causal_inlink_coverage``, the function behind
``just compliance-connectivity``), so the series is comparable across commits
even where older versions of those tools counted differently.

Usage:
    uv run python experiments/entry_growth/metrics.py \
        kb/disorders/Neuroblastoma.yaml --until <commit> \
        > experiments/entry_growth/Neuroblastoma/metrics.tsv

Pass --format markdown for the same rows as a Markdown table.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections.abc import Iterator
from typing import Any

from dismech.conformance import iter_conforms_to, module_stem
from dismech.graph import build_causal_graph
from dismech.qc_plugins import CAUSAL_PREDICATES, causal_inlink_coverage
from dismech.yaml_io import safe_load

COLUMNS = [
    "commit",
    "date",
    "pr",
    "disorder_files_changed",
    "lines",
    "pathophysiology_nodes",
    "phenotypes",
    "phenotype_nodes",
    "connected_phenotypes",
    "graph_edges",
    "causal_edges",
    "evidence_items",
    "unique_pmids",
    "unique_references",
    "conforming_nodes",
    "conformed_modules",
    "treatments",
    "differential_diagnoses",
    "discussions",
    "note",
    "subject",
]

PR_NUMBER = re.compile(r"\(#(\d+)\)")


def git(repo: str, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", repo, *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def commits_touching(repo: str, path: str, until: str) -> list[tuple[str, str, str]]:
    """(commit, date, subject) for every commit touching ``path``, oldest first."""
    log = git(
        repo,
        "log",
        "--reverse",
        "--date=short",
        "--format=%H%x09%cd%x09%s",
        until,
        "--",
        path,
    )
    rows = []
    for line in log.splitlines():
        commit, date, subject = line.split("\t", 2)
        rows.append((commit, date, subject))
    return rows


def disorder_files_changed(repo: str, commit: str) -> int:
    """How many kb/disorders/ files the commit changed, against its first parent.

    Separates a commit about this entry from a sweep across the knowledge base.
    """
    changed = git(
        repo, "diff", "--name-only", f"{commit}^", commit, "--", "kb/disorders/"
    )
    return len(changed.splitlines())


def mappings(node: Any) -> Iterator[dict[str, Any]]:
    """Every mapping in a parsed YAML document, depth first."""
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from mappings(item)


def section_length(entry: dict[str, Any], key: str) -> int:
    value = entry.get(key)
    return len(value) if isinstance(value, list) else 0


def measure(text: str) -> dict[str, Any]:
    """The metrics for one version of the entry."""
    entry = safe_load(text)
    if not isinstance(entry, dict):
        raise ValueError("the file does not parse to a mapping")

    evidence = [
        item for item in mappings(entry) if "reference" in item and "supports" in item
    ]
    references = {
        str(item["reference"]).strip() for item in evidence if item.get("reference")
    }

    conforming_nodes = 0
    modules: set[str] = set()
    for node in entry.get("pathophysiology") or []:
        refs = iter_conforms_to(node)
        if refs:
            conforming_nodes += 1
        modules.update(module_stem(ref) for ref in refs)

    graph = build_causal_graph(entry)
    causal_edges = sum(
        1
        for edge in graph.edges
        if edge.predicate in CAUSAL_PREDICATES and edge.source != edge.target
    )
    connected, phenotype_nodes, _ = causal_inlink_coverage(entry)

    return {
        "lines": len(text.splitlines()),
        "pathophysiology_nodes": section_length(entry, "pathophysiology"),
        "phenotypes": section_length(entry, "phenotypes"),
        "phenotype_nodes": phenotype_nodes,
        "connected_phenotypes": connected,
        "graph_edges": len(graph.edges),
        "causal_edges": causal_edges,
        "evidence_items": len(evidence),
        "unique_pmids": sum(1 for ref in references if ref.startswith("PMID:")),
        "unique_references": len(references),
        "conforming_nodes": conforming_nodes,
        "conformed_modules": len(modules),
        "treatments": section_length(entry, "treatments"),
        "differential_diagnoses": section_length(entry, "differential_diagnoses"),
        "discussions": section_length(entry, "discussions"),
    }


def rows(repo: str, path: str, until: str) -> Iterator[dict[str, Any]]:
    for commit, date, subject in commits_touching(repo, path, until):
        pr = PR_NUMBER.findall(subject)
        row: dict[str, Any] = {
            "commit": commit[:11],
            "date": date,
            "pr": pr[-1] if pr else "-",
            "disorder_files_changed": disorder_files_changed(repo, commit),
            "note": "",
            "subject": subject.replace("\t", " "),
        }
        try:
            row.update(measure(git(repo, "show", f"{commit}:{path}")))
        except subprocess.CalledProcessError:
            row["note"] = "file absent at this commit"
        except Exception as error:  # report the failure in the row, keep going
            row["note"] = f"not measured: {type(error).__name__}"
        yield row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="repo-relative path of the entry")
    parser.add_argument(
        "--until",
        default="HEAD",
        help="last commit to include (default HEAD); a run pins this",
    )
    parser.add_argument("--format", choices=["tsv", "markdown"], default="tsv")
    args = parser.parse_args()

    repo = git(".", "rev-parse", "--show-toplevel").strip()
    table = list(rows(repo, args.path, args.until))

    if args.format == "tsv":
        print("\t".join(COLUMNS))
        for row in table:
            print("\t".join(str(row.get(column, "")) for column in COLUMNS))
    else:
        print("| " + " | ".join(COLUMNS) + " |")
        print("|" + "---|" * len(COLUMNS))
        for row in table:
            cells = [str(row.get(column, "")).replace("|", "\\|") for column in COLUMNS]
            print("| " + " | ".join(cells) + " |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
