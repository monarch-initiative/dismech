#!/usr/bin/env python3
"""Guard against NEW `environmental:` exposures with no evidence at all.

An `Environmental` entry is optional to cite (`evidence` is not required by the
schema), so a bare exposure -- just a `name` and usually a one-line `notes` --
passes `just validate`, `validate-terms`, and `count-verified-snippets`
untouched. Every one of those checks is structurally blind to it: an
uncited causation claim like

    environmental:
    - name: Smoking
      notes: Protective (unlike Crohn's)

is indistinguishable, to the whole validation stack, from a fully-evidenced
exposure. See dismech issue #8296.

This is deliberately *not* a curation tool: it only counts and gates, it never
invents a citation. Backfilling the pre-existing backlog is real literature
work (find a citable source, exact-quote snippet, `just fetch-reference` +
`count-verified-snippets`) that belongs in prioritized curation tranches, not
a mechanical sweep -- manufacturing citations for ~200 exposures in one pass is
exactly the fabrication risk the evidence SOP warns against elsewhere in this
repo.

Signal
------
An `environmental[]` entry whose `evidence` key is absent, ``None``, or an
empty list -- unless it carries a *waiver* (below).

Waivers
-------
Some exposures cannot be cited, and never will be. A curator searches, finds
no abstract that states the claim, and records that. Before this waiver
existed such an entry was indistinguishable here from one nobody had looked
at, so the backlog could never reach zero and an honest negative result read
as an outstanding task.

An entry is treated as *dispositioned* rather than uncited when its
``review_notes`` begins with::

    Left deliberately uncited.

The sentinel is deliberately narrow. It must be ``review_notes``, not
``notes``: a waiver any prose can trigger is not a waiver, and ``notes`` is
disease content while ``review_notes`` is the curation record. The convention
predates the check -- see the Gout "Dehydration" and Myasthenia_Gravis
"Stress" entries, which already opened their ``review_notes`` with exactly
this sentence.

Waived entries stay visible: ``--all`` lists them under their own heading and
``--count`` reports them on their own line. They are dispositioned, not
disappeared.

Baseline ratchet
-----------------
The pre-existing backlog is grandfathered, mirroring
``scripts/check_snippet_length.py`` exactly:

* ``--against-ref REF`` (env ``ENVIRONMENTAL_EVIDENCE_BASELINE_REF``) derives
  the grandfather set *live* from ``kb/`` at a git ref -- CI sets it
  to the base branch (``origin/main``). Nothing is stored, so the base branch
  is green by construction and parallel merges have nothing to clobber.
* ``tests/environmental_evidence_baseline.txt`` is the committed fallback used
  when no ref is given or the ref can't be read (local runs, shallow
  checkouts, forks). It is a best-effort snapshot: regenerate it with
  ``--update-baseline`` after intentionally changing the backlog (e.g. fixing
  entries in a curation tranche).

Usage
-----
    python scripts/check_environmental_evidence.py                       # gate: fail on NEW ones
    python scripts/check_environmental_evidence.py --against-ref origin/main
    python scripts/check_environmental_evidence.py --all                 # list every finding
    python scripts/check_environmental_evidence.py --count               # summary counts
    python scripts/check_environmental_evidence.py --waivers             # list dispositioned entries
    python scripts/check_environmental_evidence.py --update-baseline
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

from dismech.yaml_io import safe_load

# Scan all of kb/, not just kb/disorders/. `environmental:` only appears under
# kb/disorders/ today, so this is a no-op on current content (verified: 0
# environmental entries anywhere outside kb/disorders/, across all six
# subdirectories -- the finding count is identical either way), but kb/modules/
# and kb/comorbidities/ validate against the same `Disease` class and may carry
# `environmental:` in future -- scoping to disorders/ would make them a silent
# blind spot in a check whose whole point is that the gap is invisible.
# test_scan_covers_kb_beyond_disorders pins this so the scope cannot be
# narrowed back silently.
SCAN_DIR = ROOT / "kb"
BASELINE_PATH = ROOT / "tests" / "environmental_evidence_baseline.txt"

# When set (CI sets it to ``origin/main``), the grandfather baseline is derived
# live from that git ref instead of the committed snapshot file -- see
# baseline_from_ref(). Mirrors SNIPPET_BASELINE_REF in check_snippet_length.py.
BASELINE_REF_ENV = "ENVIRONMENTAL_EVIDENCE_BASELINE_REF"

# An exposure whose `review_notes` opens with this sentence is a recorded
# failed search, not an unexamined one. See the module docstring: the sentinel
# is matched on `review_notes` only, and only as a prefix, so it cannot be
# triggered by ordinary prose that happens to contain the words.
WAIVER_SENTINEL = "left deliberately uncited"


def _has_quoted_evidence(entry: dict) -> bool:
    """True if *entry* carries at least one evidence item with a real snippet.

    An `evidence:` block whose items all have an empty/whitespace-only
    `snippet` is not actually cited -- it is the same "structurally valid,
    substantively empty" shape dismech#8550 describes for evidence items in
    general, reachable here specifically because this check's original
    predicate (`if entry.get("evidence")`) only checked block *presence*, so
    an exposure could be silently "retired" from the #8296 backlog by an
    evidence item that quotes nothing.
    """
    evidence = entry.get("evidence")
    if not isinstance(evidence, list):
        return False
    for item in evidence:
        if not isinstance(item, dict):
            continue
        snippet = item.get("snippet")
        if isinstance(snippet, str) and snippet.strip():
            return True
    return False


def is_waived(entry: dict) -> bool:
    """True if *entry* records a deliberate, searched-for-and-not-found decision.

    Matched on ``review_notes`` only, and only as a prefix, so the waiver is a
    deliberate act rather than something ordinary prose can trip. ``notes`` is
    disease content and is not consulted: a claim that merely *mentions* being
    uncited is not the same as a curator recording a failed search.
    """
    review_notes = entry.get("review_notes")
    if not isinstance(review_notes, str):
        return False
    return review_notes.strip().lower().startswith(WAIVER_SENTINEL)


def _iter_environmental(data):
    entries = data.get("environmental") or []
    if not isinstance(entries, list):
        return
    for idx, entry in enumerate(entries):
        if isinstance(entry, dict):
            yield idx, entry


def find_violations(data):
    """Yield ``(location, name)`` for each evidence-free `environmental[]` entry.

    Waived entries are excluded -- they are reported separately by
    :func:`find_waivers` so they stay visible without counting as outstanding.
    """
    for idx, entry in _iter_environmental(data):
        if _has_quoted_evidence(entry) or is_waived(entry):
            continue
        name = entry.get("name") or "<unnamed>"
        yield (f"environmental[{idx}]", name)


def find_waivers(data):
    """Yield ``(location, name)`` for each waived, still-uncited entry.

    An entry that carries both a waiver and real evidence is not reported: the
    evidence supersedes the waiver, and leaving it here would suggest the claim
    is still unsourced.
    """
    for idx, entry in _iter_environmental(data):
        if _has_quoted_evidence(entry) or not is_waived(entry):
            continue
        name = entry.get("name") or "<unnamed>"
        yield (f"environmental[{idx}]", name)


def scan_repo(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return a sorted list of ``(relpath, location, name)`` findings.

    ``rel_to`` is the base the reported relative paths are computed against. It
    defaults to :data:`ROOT` for the working tree, but :func:`baseline_from_ref`
    scans an extracted copy of ``kb/`` under a temp dir and passes that
    dir so the reported paths still come out as ``kb/disorders/X.yaml`` --
    matching the working-tree keys the baseline is compared on.
    """
    return _scan(find_violations, scan_dir, rel_to)


def scan_waivers(scan_dir: Path = SCAN_DIR, rel_to: Path = ROOT):
    """Return a sorted list of ``(relpath, location, name)`` waived entries."""
    return _scan(find_waivers, scan_dir, rel_to)


def _scan(finder, scan_dir: Path, rel_to: Path):
    findings = []
    for path in sorted(scan_dir.rglob("*.yaml")):
        try:
            with path.open(encoding="utf-8") as handle:
                data = safe_load(handle)
        except Exception as exc:
            # Not this check's job to gate on malformed YAML (`validate-all`
            # does that), but skipping silently would make the file invisible
            # here rather than merely unchecked.
            print(
                f"warning: skipping unparseable {path.relative_to(rel_to).as_posix()}: "
                f"{exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        if not isinstance(data, dict):
            continue
        rel = path.relative_to(rel_to).as_posix()
        for location, name in finder(data):
            findings.append((rel, location, name))
    return findings


def _baseline_key(rel: str, name: str) -> str:
    # Keyed on (file, exposure name) rather than the YAML location, which
    # shifts whenever the environmental list above it grows or reorders.
    return f"{rel}\t{' '.join(name.split())}"


def count_by_key(findings) -> Counter:
    """How many times each ``(file, name)`` appears in *findings*."""
    return Counter(_baseline_key(rel, name) for rel, _, name in findings)


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    """Read the baseline as ``{key: grandfathered occurrence count}``.

    The count matters, the same way it does in ``check_snippet_length.py``: two
    distinct evidence-free exposures that happen to share a name in one file
    (e.g. two "Smoking" entries under different subtypes) must not let a third
    evidence-free "Smoking" slip through unnoticed.
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
        "# Grandfathered evidence-free `environmental:` exposures (see\n"
        "# scripts/check_environmental_evidence.py).\n"
        "# Each line is `count<TAB>path<TAB>name`, where count is how many\n"
        "# evidence-free entries share that (file, exposure name) pair. An\n"
        "# entry fails the guard if it is absent here OR appears MORE often\n"
        "# than the count recorded. Remove entries as the backlog is fixed by\n"
        "# curation (cite the exposure); do not add new ones. Regenerate with:\n"
        "#   just update-environmental-evidence-baseline\n"
    )
    lines = [f"{counts[key]}\t{key}" for key in sorted(counts)]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def baseline_from_ref(ref: str, root: Path = ROOT) -> Counter | None:
    """Grandfather baseline derived live from a git *ref* (e.g. ``origin/main``).

    Returns the per-``(file, name)`` occurrence counts of evidence-free
    exposures as they exist in ``kb/`` at *ref* -- i.e. exactly the
    backlog already on the base branch. Because the grandfather set is
    computed from the base branch rather than a committed snapshot, there is
    nothing to keep in sync and nothing for parallel merges to clobber: the
    base branch is green by construction, and a PR fails only on exposures it
    *adds* over the base with no evidence.

    Returns ``None`` if *ref* cannot be read (no git, ref absent in a shallow
    checkout, path missing at the ref, ...), so the caller can fall back to the
    committed baseline.
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
            f"environmental evidence baseline: git archive for {ref!r} could not run: {exc}",
            file=sys.stderr,
        )
        return None
    if proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", "replace").strip() or f"exit {proc.returncode}"
        print(
            f"environmental evidence baseline: git archive {ref!r} failed: {detail}",
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
                f"environmental evidence baseline: unreadable archive for {ref!r}: {exc}",
                file=sys.stderr,
            )
            return None
        findings = scan_repo(scan_dir=tmp_path / scan_rel, rel_to=tmp_path)
    return count_by_key(findings)


def resolve_baseline(ref: str | None = None) -> Counter:
    """The grandfather baseline: live from *ref* when given, else the committed file.

    *ref* defaults to the ``ENVIRONMENTAL_EVIDENCE_BASELINE_REF`` environment
    variable, which CI sets to ``origin/main``. If the ref cannot be read, fall
    back to the committed baseline so local runs and shallow checkouts keep
    working.
    """
    if ref is None:
        ref = os.environ.get(BASELINE_REF_ENV) or None
    if ref:
        from_ref = baseline_from_ref(ref)
        if from_ref is not None:
            print(
                f"environmental evidence baseline: grandfathered against ref {ref!r} "
                f"({len(from_ref)} distinct exposure(s))",
                file=sys.stderr,
            )
            return from_ref
        print(
            f"environmental evidence baseline: could not read ref {ref!r}; "
            "falling back to the committed baseline",
            file=sys.stderr,
        )
    return load_baseline()


def new_findings(findings, baseline: Counter):
    """Findings not covered by *baseline*, including extra reuses of a known one."""
    seen: Counter = Counter()
    new = []
    for finding in findings:
        key = _baseline_key(finding[0], finding[2])
        seen[key] += 1
        if seen[key] > baseline.get(key, 0):
            new.append(finding)
    return new


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--check", action="store_true", help="(default) fail on non-baselined findings"
    )
    group.add_argument("--all", action="store_true", help="list every finding")
    group.add_argument("--count", action="store_true", help="print summary counts")
    group.add_argument(
        "--waivers",
        action="store_true",
        help="list entries dispositioned by a review_notes waiver",
    )
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
            "grandfather against the evidence-free exposures present in "
            "kb/ at this git ref instead of the committed baseline "
            f"(env: {BASELINE_REF_ENV}). CI uses origin/main so the base "
            "branch is green by construction."
        ),
    )
    args = parser.parse_args(argv)

    findings = scan_repo()

    if args.update_baseline:
        write_baseline(findings)
        print(
            f"Wrote baseline with {len(findings)} finding(s) to "
            f"{BASELINE_PATH.relative_to(ROOT)}"
        )
        return 0

    waivers = scan_waivers()

    if args.waivers:
        for rel, location, name in waivers:
            print(f"{rel}:{location}: {name!r}")
        files = {rel for rel, _, _ in waivers}
        print(
            f"\n{len(waivers)} exposure(s) dispositioned by a "
            f"'{WAIVER_SENTINEL.capitalize()}.' review_notes waiver "
            f"across {len(files)} file(s)."
        )
        return 0

    if args.all:
        for rel, location, name in findings:
            print(f"{rel}:{location}: {name!r}")
        files = {rel for rel, _, _ in findings}
        print(f"\n{len(findings)} evidence-free exposure(s) across {len(files)} file(s).")
        if waivers:
            print(
                f"({len(waivers)} further exposure(s) carry a review_notes waiver "
                "recording a failed search; see --waivers.)"
            )
        return 0

    if args.count:
        baseline = resolve_baseline(args.against_ref)
        files = {rel for rel, _, _ in findings}
        print(f"total findings: {len(findings)} across {len(files)} file(s)")
        print(
            f"baseline: {len(baseline)} distinct exposure(s), "
            f"{sum(baseline.values())} grandfathered occurrence(s)"
        )
        print(f"new (non-baselined): {len(new_findings(findings, baseline))}")
        print(f"dispositioned (review_notes waiver): {len(waivers)}")
        return 0

    baseline = resolve_baseline(args.against_ref)
    new = new_findings(findings, baseline)
    if new:
        print("New evidence-free `environmental:` exposure(s) detected.")
        print("Every environmental entry is an uncited causation claim until it")
        print("carries an `evidence:` block -- a citable PMID/DOI with a verified")
        print("snippet (or, for a non-citable source, provenance in `notes`).")
        print("See the evidence SOP in CLAUDE.md before adding a citation.\n")
        for rel, location, name in new:
            print(f"{rel}:{location}: {name!r}")
        print(f"\n{len(new)} new finding(s).")
        if args.against_ref or os.environ.get(BASELINE_REF_ENV):
            print("Grandfathering is unavailable when checking against a ref: add")
            print("an evidence block to the new exposure, or drop it. Findings are")
            print("keyed on (file, exposure name), so *renaming* a baselined")
            print("exposure also reads as a new finding here, and re-baselining")
            print("will not clear it -- cite it or revert the rename.")
        else:
            print("Note: findings are keyed on (file, exposure name), so *renaming* an")
            print("already-baselined exposure reads as a new finding even though no")
            print("uncited claim was added. If that is what happened, the fix is to")
            print("re-baseline, not to cite.")
            print("If a finding is genuinely unavoidable right now, run")
            print("--update-baseline to grandfather it.")
        return 1
    print(
        f"OK: no new evidence-free `environmental:` exposures "
        f"({sum(baseline.values())} occurrence(s) of {len(baseline)} distinct "
        "exposure(s) grandfathered in baseline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
