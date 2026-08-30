"""Identify which revision of a research template produced a report.

A deep-research report records the prompt it was generated from as a bare path::

    template_file: templates/disease_pathophysiology_research.md

The file behind that path changes; the reference does not. So a report cannot
say what it was actually asked, and two reports for the same disease a year
apart may have been asked materially different questions with nothing recording
the difference (issue #10183). That is not hypothetical: the disease template
has four revisions in git, and the MAXO-to-NCIT commit changed what it asked
for without touching a single report.

This module closes that gap from both ends.

**Going forward**, :func:`stamp_report` writes a ``template_sha`` into new
reports at generation time. The value is the template's *git blob hash*, chosen
over a hand-maintained version string because it cannot drift out of sync with
the file, and over a bare content hash because git already indexes it --
``git log --find-object=<sha>`` names the commits that carried that content, so
the stamp is a pointer into history rather than an opaque digest.

**Looking back**, :func:`resolve_report` recovers the same answer for the
thousands of reports written before any of this existed, by matching the
report's ``start_time`` against the template's commit history. This is why no
backfill is needed and none is offered: rewriting the frontmatter of every
committed report would produce an enormous diff to record something already
derivable, and would still leave any report whose file cannot be rewritten
unanswered.

The two paths are deliberately distinguishable. A resolution carries a
:class:`Provenance` saying whether the answer was *stamped* (authoritative --
the generator recorded it), *inferred* (derived from timestamps, and only as
good as the assumption that the working tree matched HEAD at generation time),
or *unknown*. Never present an inferred answer as a recorded one.
"""

from __future__ import annotations

import hashlib
import subprocess
from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from functools import cache
from pathlib import Path

from dismech.research_reports import read_frontmatter

__all__ = [
    "Provenance",
    "Resolution",
    "TemplateRevision",
    "blob_sha",
    "iter_reports",
    "resolve_report",
    "stamp_report",
    "template_history",
]

#: Frontmatter key holding the template's git blob hash.
STAMP_KEY = "template_sha"

#: Where research reports live, relative to the repository root.
REPORTS_DIR = Path("research")

#: Where templates live, relative to the repository root.
TEMPLATES_DIR = Path("templates")


class Provenance(StrEnum):
    """How a report's template revision was determined.

    The distinction is the point of the class. ``STAMPED`` is a fact the
    generator recorded; ``INFERRED`` is a reconstruction that assumes the
    working tree matched a committed revision when the report was written.
    A caller that collapses the two is claiming more than it knows.
    """

    STAMPED = "stamped"
    INFERRED = "inferred"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class TemplateRevision:
    """One committed revision of a template."""

    blob: str
    commit: str
    committed_at: datetime

    @property
    def short_blob(self) -> str:
        """The blob hash abbreviated for display."""
        return self.blob[:12]


@dataclass(frozen=True)
class Resolution:
    """Which template revision a report was generated from."""

    report: Path
    template: str | None
    blob: str | None
    provenance: Provenance
    detail: str = ""

    @property
    def short_blob(self) -> str:
        """The blob hash abbreviated for display, or a placeholder."""
        return self.blob[:12] if self.blob else "-"

    def is_current(self, current_blob: str | None) -> bool | None:
        """Whether this report saw the template as it stands now.

        Args:
            current_blob: Blob hash of the template's present content.

        Returns:
            ``True`` or ``False`` when both hashes are known, and ``None``
            when either is missing. ``None`` means *undetermined*, which is
            not the same as stale -- a caller that treats it as stale will
            report every unresolvable report as out of date.
        """
        if not self.blob or not current_blob:
            return None
        return self.blob == current_blob


def blob_sha(path: Path) -> str:
    """Return the git blob hash of a file's current content.

    Computed directly rather than shelled out to ``git hash-object`` so this
    works on an uncommitted template and in a checkout without git available.
    The formula is git's own: SHA-1 over ``blob <bytelength>\\0`` followed by
    the content.

    Args:
        path: The file to hash.

    Returns:
        The 40-character hex blob hash.
    """
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@cache
def template_history(
    template: str, repo_root: str = "."
) -> tuple[TemplateRevision, ...]:
    """Return a template's committed revisions, newest first.

    Args:
        template: Repository-relative path of the template.
        repo_root: Repository root to run git in.

    Returns:
        One :class:`TemplateRevision` per commit that changed the file,
        newest first. Empty when the file has no history, git is unavailable,
        or the path was never committed -- all of which are ordinary states
        for a template added but not yet committed, so none of them raises.

    Note:
        ``--follow`` is used so a renamed template keeps its history. Commits
        whose tree no longer holds the path are skipped rather than failing;
        that happens at a rename boundary.
    """
    try:
        log = subprocess.run(
            ["git", "log", "--follow", "--format=%H %cI", "--", template],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        ).stdout
    except (subprocess.SubprocessError, OSError):
        return ()

    revisions: list[TemplateRevision] = []
    for line in log.splitlines():
        commit, _, stamp = line.partition(" ")
        if not commit or not stamp:
            continue
        try:
            blob = subprocess.run(
                ["git", "rev-parse", f"{commit}:{template}"],
                cwd=repo_root,
                capture_output=True,
                text=True,
                check=True,
                timeout=30,
            ).stdout.strip()
        except (subprocess.SubprocessError, OSError):
            continue
        try:
            committed_at = datetime.fromisoformat(stamp)
        except ValueError:
            continue
        revisions.append(
            TemplateRevision(blob=blob, commit=commit, committed_at=committed_at)
        )
    return tuple(revisions)


def _normalize_template_path(value: object) -> str | None:
    """Return a usable repository-relative template path, or ``None``.

    Args:
        value: The raw ``template_file`` frontmatter value.

    Returns:
        The path with backslashes folded to forward slashes, or ``None`` when
        the value is missing or blank.

    Note:
        Twenty committed reports record the disease template's path with
        Windows separators (``templates\\disease_pathophysiology_research.md``).
        That names the same template every other report names, so folding the
        separator resolves them instead of writing them off as unknown.

        The value is otherwise left alone -- several reports record a
        free-text label rather than a path (``manual_curation``,
        ``codex_supplement_local``), and inventing a path for those would be worse
        than reporting them undetermined.
    """
    if not isinstance(value, str):
        return None
    normalized = value.strip().replace("\\", "/")
    return normalized or None


def _as_utc(value: object) -> datetime | None:
    """Coerce a frontmatter timestamp to an aware UTC datetime."""
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError:
            return None
    else:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def resolve_report(report: Path, repo_root: str = ".") -> Resolution:
    """Determine which template revision produced a report.

    Prefers the recorded stamp. Falls back to matching the report's
    ``start_time`` against the template's commit history: the revision in
    effect is the newest one committed at or before the report ran.

    Args:
        report: The report to resolve.
        repo_root: Repository root, for reading git history.

    Returns:
        A :class:`Resolution`. Its ``provenance`` says which path produced the
        answer, and callers must not present an ``INFERRED`` result as a
        recorded fact -- inference assumes the working tree matched a committed
        revision, which an uncommitted local edit would break.
    """
    frontmatter = read_frontmatter(report)
    template = _normalize_template_path(frontmatter.get("template_file"))

    stamped = frontmatter.get(STAMP_KEY)
    if isinstance(stamped, str) and stamped.strip():
        return Resolution(
            report=report,
            template=template,
            blob=stamped.strip(),
            provenance=Provenance.STAMPED,
        )

    if not template:
        return Resolution(
            report=report,
            template=None,
            blob=None,
            provenance=Provenance.UNKNOWN,
            detail="no template_file in frontmatter",
        )

    started = _as_utc(frontmatter.get("start_time"))
    if started is None:
        return Resolution(
            report=report,
            template=template,
            blob=None,
            provenance=Provenance.UNKNOWN,
            detail="no usable start_time to date the report against",
        )

    history = template_history(template, repo_root)
    if not history:
        return Resolution(
            report=report,
            template=template,
            blob=None,
            provenance=Provenance.UNKNOWN,
            detail=f"no commit history for {template}",
        )

    for revision in history:  # newest first
        if revision.committed_at <= started:
            return Resolution(
                report=report,
                template=template,
                blob=revision.blob,
                provenance=Provenance.INFERRED,
                detail=f"in effect from {revision.committed_at.date()}",
            )

    return Resolution(
        report=report,
        template=template,
        blob=None,
        provenance=Provenance.UNKNOWN,
        detail="report predates the template's first commit",
    )


def stamp_report(report: Path, repo_root: Path = Path(".")) -> str | None:
    """Record the template's blob hash in a report's frontmatter.

    Idempotent: a report already carrying a stamp is left untouched, so
    re-running a recipe over an existing report cannot rewrite provenance.

    Args:
        report: The report to stamp.
        repo_root: Root the report's ``template_file`` path is relative to.

    Returns:
        The blob hash written, or ``None`` when nothing was written -- the
        report has no frontmatter, names no template, already carries a stamp,
        or names a template that is not on disk. None of these is an error
        here: a missing template is normal for a report generated elsewhere,
        and refusing to stamp is the honest outcome.
    """
    frontmatter = read_frontmatter(report)
    if not frontmatter:
        return None
    if isinstance(frontmatter.get(STAMP_KEY), str) and frontmatter[STAMP_KEY].strip():
        return None

    template = _normalize_template_path(frontmatter.get("template_file"))
    if not template:
        return None

    template_path = repo_root / template
    if not template_path.is_file():
        return None

    sha = blob_sha(template_path)
    text = report.read_text(encoding="utf-8")
    marker = "template_file:"
    index = text.find(marker)
    if index == -1:
        return None
    line_end = text.find("\n", index)
    if line_end == -1:
        return None

    # Quoted deliberately. A blob hash is hex, so an all-digit one is possible
    # (rare, but ~1 in 10^9 rather than impossible), and YAML would load that
    # bare value as an int -- after which the leading zeros are gone and the
    # stamp cannot be read back as the hash that was written.
    report.write_text(
        f'{text[:line_end]}\n{STAMP_KEY}: "{sha}"{text[line_end:]}',
        encoding="utf-8",
    )
    return sha


#: Suffix marking a provider artifacts directory, whose contents are inputs
#: embedded beside a report rather than reports in their own right.
ARTIFACTS_DIR_SUFFIX = "_artifacts"


def iter_reports(reports_dir: Path = REPORTS_DIR):
    """Yield research report paths, skipping sidecars and provider artifacts.

    Args:
        reports_dir: Directory to scan.

    Yields:
        Each ``*.md`` report, in sorted order.

    Note:
        The scan **recurses**. Reports do not all sit at the top of
        ``research/`` -- ``modules/``, ``groupings/``, ``surrogacy/`` and
        ``datasets/`` hold their own, and a top-level-only glob reports a
        corpus census while silently omitting them.

        Two exclusions, both by construction rather than by name-guessing:
        citation sidecars, which are ``<report>.md.citations.md`` (a doubled
        ``.md``); and anything inside a ``*_artifacts/`` directory, which holds
        the tables and figures a provider returned alongside a report. Those
        artifacts are numerous -- 993 of the 1,023 nested markdown files at the
        time of writing -- and are not reports, so counting them would swamp the
        census with rows that can never carry a ``template_file``.
    """
    for path in sorted(reports_dir.rglob("*.md")):
        if path.name.endswith(".citations.md"):
            continue
        if any(part.endswith(ARTIFACTS_DIR_SUFFIX) for part in path.parts):
            continue
        yield path
