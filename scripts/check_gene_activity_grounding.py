#!/usr/bin/env python3
"""Ratchet: a gene wired into the pathograph must land on a molecular function.

GO names three levels between a gene and what a cell can no longer do --
**gene -> molecular function -> biological process**. A pathograph edge running
from a ``genetic:`` node to a ``pathophysiology`` node that carries
``biological_processes:`` but no ``molecular_functions:`` skips the middle one:
the graph states what the *cell* can no longer do without ever stating what the
*protein* can no longer do::

    - name: SLC25A20 transporter molecular function deficiency
      description: >-
        Biallelic SLC25A20 pathogenic variants reduce mitochondrial inner
        membrane carnitine-acylcarnitine translocase activity.
      genes: [{term: {id: hgnc:1421, label: SLC25A20}}]
      biological_processes:
      - term: {id: GO:0015879, label: carnitine transport}   # and nothing else

The node is *named* a molecular function deficiency and its description asserts
the activity; only the term is missing. That is the common shape, and it is
invisible to recommended-slot compliance, which asks whether a slot is filled on
an object and cannot ask what the object one edge away is annotated with.

This guard is the CI half of the ``genetic[].mechanism_activity_grounding``
metric in :mod:`dismech.qc_plugins`. The metric reports graded coverage (23.8%
KB-wide when it was added, so far too low to gate on an absolute threshold);
this ratchets it, failing only on genes a change *adds* over the base branch.

Scope: only genes already wired into the mechanism graph. An unwired gene is a
different defect, counted by ``genetic[].mechanism_outlink``, and charging it
here as well would report one problem twice.

**Not every finding wants a term.** Two cases where binding one would be wrong,
and the fix is elsewhere:

* **A landing node carrying many genes.** ``Primary_Ciliary_Dyskinesia`` /
  "Ciliary Dysfunction" collects 21 -- dynein motors, radial-spoke structural
  constituents, axonemal rulers, transcription factors. No single MF term is
  true of that set; the node wants splitting.
* **A class with no shared molecular function.**
  ``Autosomal_Recessive_Non-Syndromic_Intellectual_Disability`` has a node whose
  description states outright that the affected protein functions are very
  diverse. The absence of a term there is the finding.

Both are in the baseline. Adding a *new* node of either kind is the case for
grandfathering a line with ``--update-baseline`` and saying why in the PR --
never for binding a term that overstates what the node claims. The repo rule
holds: no term beats a bad one.

Usage::

    uv run python scripts/check_gene_activity_grounding.py
    uv run python scripts/check_gene_activity_grounding.py --all
    uv run python scripts/check_gene_activity_grounding.py --count
    uv run python scripts/check_gene_activity_grounding.py --update-baseline
"""

from __future__ import annotations

import argparse
import io
import os
import subprocess
import sys
import tarfile
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))

from dismech.qc_plugins import gene_activity_grounding_coverage  # noqa: E402
from dismech.yaml_io import safe_load  # noqa: E402

# Scan all of kb/, matching check_environmental_evidence.py: `genetic:` appears
# under kb/disorders/ today, but kb/modules/ and kb/comorbidities/ validate
# against the same `Disease` class and would otherwise be a silent blind spot.
SCAN_DIR = ROOT / "kb"
BASELINE_PATH = ROOT / "tests" / "gene_activity_grounding_baseline.txt"

# When set (CI sets it to ``origin/main``), the grandfather baseline is derived
# live from that git ref instead of the committed snapshot -- see
# baseline_from_ref(). Mirrors ENVIRONMENTAL_EVIDENCE_BASELINE_REF.
BASELINE_REF_ENV = "GENE_ACTIVITY_BASELINE_REF"


def scan_repo(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return a sorted list of ``(relpath, gene_node_name)`` findings.

    ``rel_to`` is the base the reported relative paths are computed against, so
    :func:`baseline_from_ref` can scan an extracted copy of ``kb/`` under a temp
    dir and still report ``kb/disorders/X.yaml`` keys.
    """
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception as exc:
            # Not this check's job to gate on malformed YAML (`validate-all`
            # does that), but skipping silently would make the file invisible
            # rather than merely unchecked.
            print(
                f"warning: skipping unparseable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        if not isinstance(data, dict):
            continue
        _grounded, _total, ungrounded = gene_activity_grounding_coverage(data)
        rel = path.relative_to(rel_to).as_posix()
        findings.extend((rel, name) for name in ungrounded)
    return sorted(findings)


def _baseline_key(rel: str, name: str) -> str:
    # Keyed on (file, genetic-entry name) rather than a YAML location, which
    # shifts whenever the list above it grows or reorders.
    return f"{rel}\t{' '.join(name.split())}"


def count_by_key(findings) -> Counter:
    """How many times each ``(file, gene name)`` appears in *findings*."""
    return Counter(_baseline_key(rel, name) for rel, name in findings)


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    """Read the baseline as ``{key: grandfathered occurrence count}``.

    The count matters: one file may carry two `genetic:` entries with the same
    name (a gene and its variant-specific sibling), and grandfathering one must
    not silently admit a third.
    """
    counts: Counter = Counter()
    if not path.exists():
        return counts
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        count, tab, key = line.partition("\t")
        if tab and count.isdigit():
            counts[key] = int(count)
        else:  # tolerate a pre-count baseline
            counts[line] = counts.get(line, 0) + 1
    return counts


def write_baseline(findings, path: Path = BASELINE_PATH) -> None:
    counts = count_by_key(findings)
    header = (
        "# Grandfathered genes wired into the pathograph whose landing node\n"
        "# names no molecular function (see\n"
        "# scripts/check_gene_activity_grounding.py).\n"
        "# Each line is `count<TAB>path<TAB>genetic entry name`. A gene fails\n"
        "# the guard if it is absent here OR appears MORE often than the count\n"
        "# recorded. Remove lines as the backlog is fixed by curation (bind\n"
        "# molecular_functions: on the node the gene lands on); add one only\n"
        "# for a node that genuinely has no single molecular function -- a\n"
        "# many-gene bundle, or a class whose members share none -- and say so\n"
        "# in the PR. Regenerate with:\n"
        "#   just update-gene-activity-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def baseline_from_ref(ref: str, root: Path = ROOT) -> Counter | None:
    """Grandfather baseline derived live from a git *ref* (e.g. ``origin/main``).

    Because the grandfather set is computed from the base branch rather than a
    committed snapshot, there is nothing to keep in sync and nothing for
    parallel merges to clobber: the base branch is green by construction, and a
    PR fails only on ungrounded genes it *adds* over the base.

    Returns ``None`` if *ref* cannot be read (no git, ref absent in a shallow
    checkout, ...), so the caller can fall back to the committed baseline.
    """
    scan_rel = SCAN_DIR.relative_to(ROOT).as_posix()
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "archive", "--format=tar", ref, "--", scan_rel],
            capture_output=True,
            check=False,
        )
    except (FileNotFoundError, OSError) as exc:
        print(
            f"gene activity baseline: git archive for {ref!r} could not run: {exc}",
            file=sys.stderr,
        )
        return None
    if proc.returncode != 0:
        detail = (
            proc.stderr.decode("utf-8", "replace").strip() or f"exit {proc.returncode}"
        )
        print(
            f"gene activity baseline: git archive {ref!r} failed: {detail}",
            file=sys.stderr,
        )
        return None
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        try:
            with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tar:
                tar.extractall(tmp_path, filter="data")
        except tarfile.TarError as exc:
            print(
                f"gene activity baseline: unreadable archive for {ref!r}: {exc}",
                file=sys.stderr,
            )
            return None
        findings = scan_repo(scan_dir=tmp_path / scan_rel, rel_to=tmp_path)
    return count_by_key(findings)


def resolve_baseline(ref: str | None = None) -> Counter:
    """The grandfather baseline: live from *ref* when given, else the committed file."""
    if ref is None:
        ref = os.environ.get(BASELINE_REF_ENV) or None
    if ref:
        from_ref = baseline_from_ref(ref)
        if from_ref is not None:
            print(
                f"gene activity baseline: grandfathered against ref {ref!r} "
                f"({len(from_ref)} distinct gene(s))",
                file=sys.stderr,
            )
            return from_ref
        print(
            f"gene activity baseline: could not read ref {ref!r}; "
            "falling back to the committed baseline",
            file=sys.stderr,
        )
    return load_baseline()


def new_findings(findings, baseline: Counter):
    """Findings not covered by *baseline*, including extra reuses of a known one."""
    seen: Counter = Counter()
    new = []
    for finding in findings:
        key = _baseline_key(*finding)
        seen[key] += 1
        if seen[key] > baseline.get(key, 0):
            new.append(finding)
    return new


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--check", action="store_true", help="(default) fail on non-baselined findings"
    )
    group.add_argument("--all", action="store_true", help="list every finding")
    group.add_argument("--count", action="store_true", help="print summary counts")
    group.add_argument(
        "--update-baseline",
        action="store_true",
        help="rewrite the baseline from current findings",
    )
    parser.add_argument(
        "--against-ref",
        metavar="REF",
        default=None,
        help=(
            "grandfather against this git ref's kb/ instead of the committed "
            f"baseline (default: ${BASELINE_REF_ENV}, else the committed file)"
        ),
    )
    args = parser.parse_args(argv)

    findings = scan_repo()

    if args.update_baseline:
        write_baseline(findings)
        print(f"wrote {BASELINE_PATH.relative_to(ROOT)} ({len(findings)} finding(s))")
        return 0

    if args.all:
        for rel, name in findings:
            print(f"{rel}: {name}")
        return 0

    if args.count:
        files = {rel for rel, _ in findings}
        baseline = load_baseline()
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(f"baseline: {len(baseline)} distinct gene(s)")
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        return 0

    baseline = resolve_baseline(args.against_ref)
    new = new_findings(findings, baseline)
    if new:
        print("Gene(s) newly wired into the pathograph with no molecular function")
        print("on the node they land on. GO puts a molecular function between a")
        print("gene and a biological process; without it the graph says what the")
        print("cell can no longer do but not what the protein can no longer do.\n")
        for rel, name in new:
            print(f"{rel}: {name}")
        print(
            f"\n{len(new)} new finding(s). Bind `molecular_functions:` on the "
            "pathophysiology\nnode the gene reaches."
        )
        if args.against_ref or os.environ.get(BASELINE_REF_ENV):
            # A ref baseline (CI) never reads the committed file, so
            # --update-baseline would pass locally and still fail CI.
            print("Grandfathering is unavailable when checking against a ref.")
        else:
            print("If the node genuinely has no single molecular function -- a")
            print("many-gene bundle, or a class whose members share none -- then")
            print("grandfather it with --update-baseline and say why in the PR.")
        return 1
    print(
        f"OK: no newly ungrounded genes ({sum(baseline.values())} "
        "grandfathered in baseline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
