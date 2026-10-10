#!/usr/bin/env python3
"""Guard the two path conventions that attach a hypothesis exploration to its entry.

A hypothesis exploration lives at ``kb/hypotheses/<slug>/<hypothesis_id>/`` and
reaches its disease page through ``render.collect_hypothesis_research_links``,
which does two verbatim lookups:

1. ``hypotheses_root / disorder_slug`` -- the directory name must equal the
   **filename stem of the kb entry**. If it does not, the function returns ``[]``
   and *every* report under that directory is invisible on the page.
2. ``hypothesis_lookup[hypothesis_dir.name]`` -- the subdirectory name must equal
   a ``mechanistic_hypotheses[].hypothesis_group_id`` declared by that entry. If
   it does not, the section still renders but with a label derived from the
   directory name and **no status**, detached from the hypothesis it explored.

``render_disorder`` softens the first of those with one retry: when the file-stem
lookup comes back empty *and* ``slugify(entry["name"]) != file_stem``, it calls
again with the slugified name (``render.py``, "if not hypothesis_research_links
and file_stem != disorder_slug"). So a directory named for the disease's ``name:``
rather than its filename does still render. That retry is why this checker
separates two outcomes rather than failing both: several hundred kb entries have
``slugify(name) != <file stem>``, and failing all of those would make the gate
stricter than the thing it is guarding. (Run ``--report`` for the live count
rather than trusting a number written here, which is stale by construction.)

A directory is therefore only UNREACHABLE when it matches neither name -- or when
it matches the slugified name while a canonical directory also exists, since the
retry only fires if the first lookup found nothing. A directory that renders
solely through the retry is reported as a naming inconsistency and does not fail
the check.

Both failures are silent everywhere else. The reports validate, the assessment
sidecars validate, the entry validates, the page builds, and `just qc` is green.
Nothing in the repo compares a hypothesis directory against a kb entry, so the
drift is only visible by rendering the page and noticing an absence.

It is drift by construction, because the directory is named once, at run time,
from the free-text ``disease_name`` the runner was invoked with, while the entry
filename and the hypothesis ids are curated afterwards and keep moving:

* The runner was invoked with the free text ``Huntington's Disease`` and wrote
  ``Huntingtons_Disease``; the entry is ``Huntington_Disease.yaml``. Four
  OpenScientist reports were unreachable. (Note ``slugify`` does not strip the
  apostrophe -- it returns ``Huntington's_Disease`` -- so that directory name
  came from the runner, not from ``slugify``, and the fallback never had a
  chance to rescue it.)
* ``Metastatic_Pancreatic_Adenocarcinoma`` was folded into
  ``Pancreatic_Ductal_Adenocarcinoma`` per design decisions section 3a, which
  moved the hypothesis ids to the parent and left the directory behind. Two more
  reports unreachable.
* ``canonical_hmgcs2_ketogenesis_failure_model`` was renamed to
  ``canonical_human_hmgcs2_ketogenesis_failure`` in the entry by PR #6565; the
  directory kept the old id and its report rendered detached.

So the natural lifecycle of an entry -- rename it, fold it into a parent, rename
one of its hypotheses -- breaks this link without touching the hypothesis tree at
all. That is why this runs whole-KB and ungated rather than as a path-filtered
test: the PR that breaks it is a PR that never opens ``kb/hypotheses/``.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from dismech.export.utils import slugify

KB_SUBDIRS = ("disorders", "modules", "comorbidities", "groupings")

# Only these kinds fail the gate; a non-canonical directory still renders.
BLOCKING_KINDS = ("no_entry", "shadowed", "undeclared_id")


@dataclass(frozen=True)
class Finding:
    kind: str  # "no_entry" | "shadowed" | "undeclared_id" | "non_canonical_slug"
    directory: str
    detail: str
    fix: str


def _entry_paths(kb_root: Path) -> dict[str, Path]:
    """Map every kb entry filename stem to its path."""
    entries: dict[str, Path] = {}
    for sub in KB_SUBDIRS:
        for path in sorted((kb_root / sub).glob("*.yaml")):
            entries.setdefault(path.stem, path)
    return entries


_NAME_LINE = re.compile(r"^name:[ \t]*(.+?)[ \t]*$", re.MULTILINE)


def _entry_name(path: Path) -> str | None:
    """Read the top-level ``name:`` without parsing the whole entry.

    A full ``yaml.safe_load`` of every kb entry costs minutes across the KB,
    which is too slow for a step that runs in ``just qc``. ``name:`` is a
    top-level scalar at column 0, so the first such line is it.
    """
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("name:"):
                match = _NAME_LINE.match(line.rstrip("\n"))
                if not match:
                    return None
                value = match.group(1).strip()
                # Decline anything this scan cannot read correctly, so the
                # caller falls back to a real parse. A folded/literal header
                # ("name: >-") continues on the next line, and a trailing
                # comment is not part of the value.
                if value[:1] in {">", "|", "&", "*"} or " #" in value:
                    return None
                return value.strip("\"'")
            if line.startswith(("pathophysiology:", "phenotypes:")):
                break  # past the header; no top-level name
    return None


def _slug_index(entries: dict[str, Path]) -> dict[str, list[Path]]:
    """Map ``slugify(entry["name"])`` to every entry reaching it by the retry.

    Only entries whose slug differs from their filename stem can be reached
    this way, because ``render_disorder`` guards the retry with
    ``file_stem != disorder_slug``.

    The value is a list because two entries can share a slug -- distinct files
    carrying the same ``name:``, or names differing only in a character
    ``slugify`` drops. Keeping one would make the directory look shadowed for
    whichever entry lost the tie, while that entry's page renders it.
    """
    index: dict[str, list[Path]] = {}
    for stem, path in entries.items():
        name = _entry_name(path)
        if name is None:
            # Falling back to the stem would be the one slug this entry cannot
            # need, since a slug equal to the stem is skipped below -- so the
            # entry would drop out of the index entirely and a directory the
            # renderer resolves would read as an orphan. Pay for a real parse
            # instead; no entry in kb/ reaches this path today.
            parsed = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            name = str(parsed.get("name") or stem)
        slug = slugify(name)
        if slug != stem:
            index.setdefault(slug, []).append(path)
    return index


def _declared_ids(entry_path: Path) -> set[str]:
    data = yaml.safe_load(entry_path.read_text(encoding="utf-8")) or {}
    return {
        str(h["hypothesis_group_id"])
        for h in (data.get("mechanistic_hypotheses") or [])
        if isinstance(h, dict) and h.get("hypothesis_group_id")
    }


def _has_report(hypothesis_dir: Path) -> bool:
    """A directory only reaches the page if it holds a non-citations report."""
    return any(
        not p.name.endswith(".citations.md") for p in hypothesis_dir.glob("*.md")
    )


def _classify(
    name: str,
    entries: dict[str, Path],
    by_slug: dict[str, list[Path]],
    present: set[str],
) -> tuple[Path | None, str]:
    """Resolve a hypothesis directory the way the renderer does.

    Returns the entry it reaches, and how:

    ``canonical``  named for the entry's filename stem; the primary lookup.
    ``retry``      named for ``slugify(entry["name"])``; reached only by
                   ``render_disorder``'s fallback, which is enough to render.
    ``shadowed``   names a disease whose canonical directory also exists. The
                   fallback only runs when the first lookup found nothing, so
                   this one is unreachable despite naming a real entry.
    ``orphan``     matches no entry at all.
    """
    if name in entries:
        return entries[name], "canonical"
    candidates = by_slug.get(name)
    if not candidates:
        return None, "orphan"
    # It renders if ANY candidate entry would fall through to the retry. Only
    # when every one of them already has its own populated directory is this
    # directory genuinely unreachable.
    for candidate in candidates:
        if candidate.stem not in present:
            return candidate, "retry"
    return candidates[0], "shadowed"


def collect(repo_root: Path) -> list[Finding]:
    kb_root = repo_root / "kb"
    hyp_root = kb_root / "hypotheses"
    if not hyp_root.is_dir():
        return []
    entries = _entry_paths(kb_root)
    by_slug = _slug_index(entries)
    # "Present" must mean what the renderer means. `collect_hypothesis_research_links`
    # returns [] both for a missing directory and for one whose subdirectories all
    # fail `if not reports: continue`, and `render_disorder` retries on either. A
    # canonical directory holding no report therefore does NOT shadow.
    present = {
        p.name
        for p in hyp_root.iterdir()
        if p.is_dir() and any(d.is_dir() and _has_report(d) for d in p.iterdir())
    }
    findings: list[Finding] = []
    id_cache: dict[Path, set[str]] = {}

    for disease_dir in sorted(p for p in hyp_root.iterdir() if p.is_dir()):
        name = disease_dir.name
        entry, how = _classify(name, entries, by_slug, present)
        reports = sum(1 for d in disease_dir.iterdir() if d.is_dir() and _has_report(d))

        if not reports:
            # A directory with no report cannot render for anyone, so it has no
            # reachability to lose. Reporting it would print "0 report
            # directory/ies are unreachable", which is not a finding.
            continue

        if how == "orphan":
            near = difflib.get_close_matches(name, entries, n=1, cutoff=0.8)
            hint = f" Closest entry: {near[0]!r}." if near else ""
            findings.append(
                Finding(
                    "no_entry",
                    f"kb/hypotheses/{name}/",
                    f"no kb entry named {name!r}; {reports} hypothesis report "
                    f"directory/ies are unreachable from any disease "
                    f"page.{hint}",
                    "rename the directory to the entry's filename stem, or "
                    "delete it if the entry was retired",
                )
            )
            continue

        assert entry is not None
        if how == "shadowed":
            findings.append(
                Finding(
                    "shadowed",
                    f"kb/hypotheses/{name}/",
                    f"names the disease of {entry.stem!r}, but that entry "
                    f"already has its own kb/hypotheses/{entry.stem}/ "
                    f"directory with reports in it. The renderer's fallback "
                    f"only runs when the first lookup yields nothing, so these "
                    f"{reports} report directory/ies are unreachable.",
                    f"merge this directory's contents into kb/hypotheses/{entry.stem}/",
                )
            )
            continue

        if how == "retry":
            findings.append(
                Finding(
                    "non_canonical_slug",
                    f"kb/hypotheses/{name}/",
                    f"named for this disease's `name:` rather than its "
                    f"filename stem {entry.stem!r}. It renders, but only "
                    f"through render_disorder's fallback retry, and it is "
                    f"invisible to anything keying on the entry filename.",
                    f"rename to kb/hypotheses/{entry.stem}/ so the primary "
                    f"lookup finds it",
                )
            )

        if entry not in id_cache:
            id_cache[entry] = _declared_ids(entry)
        declared = id_cache[entry]

        for hypothesis_dir in sorted(p for p in disease_dir.iterdir() if p.is_dir()):
            if not _has_report(hypothesis_dir):
                continue
            if hypothesis_dir.name in declared:
                continue
            listed = ", ".join(sorted(declared)) if declared else "(none declared)"
            findings.append(
                Finding(
                    "undeclared_id",
                    f"kb/hypotheses/{name}/{hypothesis_dir.name}/",
                    f"{entry.relative_to(repo_root).as_posix()} declares no "
                    f"hypothesis_group_id {hypothesis_dir.name!r}; the report "
                    f"renders detached, with a derived label and no status. "
                    f"Entry declares: {listed}",
                    "rename the directory to the entry's current "
                    "hypothesis_group_id (ids get renamed by curation)",
                )
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root", type=Path, default=Path("."), help="repository root"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="print findings but always exit 0 (census mode)",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    findings = collect(repo_root)
    blocking = [f for f in findings if f.kind in BLOCKING_KINDS]

    if args.report:
        entries = _entry_paths(repo_root / "kb")
        by_slug = _slug_index(entries)
        hyp_root = repo_root / "kb" / "hypotheses"
        dirs = (
            sum(1 for p in hyp_root.iterdir() if p.is_dir()) if hyp_root.is_dir() else 0
        )
        reachable = sum(len(paths) for paths in by_slug.values())
        collisions = sum(1 for paths in by_slug.values() if len(paths) > 1)
        print(
            f"{dirs} hypothesis directory/ies; {len(entries)} kb entries, of "
            f"which {reachable} have slugify(name) != <file stem> and so "
            f"could be reached by render_disorder's fallback "
            f"({len(by_slug)} distinct slug(s), {collisions} shared by more "
            f"than one entry).\n"
        )
    if not findings:
        print(
            "OK: every hypothesis directory resolves to a kb entry and a "
            "declared hypothesis_group_id."
        )
        return 0

    if blocking:
        print("Hypothesis exploration(s) disconnected from their kb entry.\n")
        print(
            "`render.collect_hypothesis_research_links` matches directory names\n"
            "verbatim against the entry filename stem and against the entry's\n"
            "declared hypothesis_group_id values, and `render_disorder` retries\n"
            "once with the slugified disease name. A mismatch that survives both\n"
            "is silent: reports, sidecars, the entry and the page all still\n"
            "validate. The symptom is an ABSENCE on the rendered page, so it is\n"
            "only found by looking for it.\n"
        )

    unreachable = [f for f in findings if f.kind in ("no_entry", "shadowed")]
    undeclared = [f for f in findings if f.kind == "undeclared_id"]
    advisory = [f for f in findings if f.kind == "non_canonical_slug"]

    if unreachable:
        print(f"-- {len(unreachable)} directory/ies no disease page can reach --")
        print("   Every report beneath these is invisible on every page.\n")
        for f in unreachable:
            print(f"  {f.directory}")
            print(f"     {f.detail}")
            print(f"     fix: {f.fix}\n")
    if undeclared:
        print(f"-- {len(undeclared)} directory/ies naming an undeclared hypothesis --")
        print("   These render, but detached from the hypothesis they explored.\n")
        for f in undeclared:
            print(f"  {f.directory}")
            print(f"     {f.detail}")
            print(f"     fix: {f.fix}\n")
    if advisory:
        print(f"-- {len(advisory)} non-canonical directory name(s) (advisory) --")
        print(
            "   These DO render, through render_disorder's fallback retry, so\n"
            "   they do not fail this check. Renaming them makes the primary\n"
            "   lookup work and keeps the tree keyed on entry filenames.\n"
        )
        for f in advisory:
            print(f"  {f.directory}")
            print(f"     {f.detail}")
            print(f"     fix: {f.fix}\n")

    if not blocking:
        print(f"{len(advisory)} advisory finding(s); nothing unreachable.")
        return 0

    print(f"{len(blocking)} blocking finding(s), {len(advisory)} advisory.")
    return 0 if args.report else 1


if __name__ == "__main__":
    sys.exit(main())
