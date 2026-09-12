"""Name a deep-research report after the provider that actually wrote it.

`deep-research-client` 0.2.11 can fall back to another provider when the one
you asked for has no credentials or no credit. That is useful here — a brief
asks for falcon, no ``EDISON_API_KEY`` is set, and today a curator substitutes
``claude_code`` by hand and writes a paragraph about it into the history record.

It is also unsafe on its own, because this repository encodes the provider in
the filename: every research recipe writes
``<name>-deep-research-<provider>.md`` using the provider that was *asked for*,
and ``scripts/deep_research_coverage.py`` reads the provider back out of that
filename. A silent fallback would leave a ``claude_code`` report named
``-falcon.md``, and ``just research-status`` would then report falcon coverage
that does not exist.

This module closes that gap: after a run, the report is renamed to the provider
named in its own frontmatter, along with its citations sidecar and artifacts
directory.

**The trigger is ``fell_back``, not a provider mismatch.** A filename slug that
differs from the frontmatter ``provider`` is normal and does not mean a fallback
happened: ``just research-disorder edison Foo`` writes ``-edison.md`` for a
report whose provider is ``falcon`` (an alias), and the cyberian-codex recipe
writes ``-cyberian-codex.md`` for a run whose provider is ``cyberian``. Renaming
on mismatch would rewrite both. ``fell_back`` is set only when a provider other
than the first choice produced the report, which is exactly the case that makes
the filename a lie.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from dismech.yaml_io import safe_load

FRONTMATTER_DELIMITER = "---"


class AlignmentError(RuntimeError):
    """A fallback happened but the report cannot be safely renamed.

    Raised rather than handled quietly: the file on disk is a report by one
    provider carrying another provider's name, which is the defect this module
    exists to prevent. A curator has to see it.
    """


@dataclass(frozen=True)
class Alignment:
    """What was done, or would be done, to one report.

    Attributes:
        report: The report path as it stands after alignment.
        renamed_from: The previous path, or None when nothing needed doing.
        requested_provider: The provider the run asked for.
        actual_provider: The provider that produced the report.
        moved: Paths that were moved, as ``(old, new)`` pairs.
    """

    report: Path
    renamed_from: Path | None
    requested_provider: str | None
    actual_provider: str | None
    moved: tuple[tuple[Path, Path], ...] = ()

    @property
    def fell_back(self) -> bool:
        """Whether the report had to be renamed.

        Not quite the same claim as the frontmatter flag of that name, which
        upstream sets whenever any attempt failed. A run that retried and then
        succeeded with the provider originally asked for sets the flag while
        leaving the filename true, so nothing moves and this reads False.
        """
        return self.renamed_from is not None


def read_frontmatter(path: Path) -> dict:
    """Return a report's YAML frontmatter as a dict.

    Args:
        path: The markdown report to read.

    Returns:
        The parsed frontmatter, or an empty dict when the file has none.

    Note:
        The frontmatter block ends at the first delimiter line *after* the
        opening one, which is how the report itself is written. A body
        containing ``---`` is therefore never mistaken for the end of the
        block, because the split stops at the closing delimiter first.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith(f"{FRONTMATTER_DELIMITER}\n"):
        return {}
    _, _, rest = text.partition(f"{FRONTMATTER_DELIMITER}\n")
    block, delimiter, _ = rest.partition(f"\n{FRONTMATTER_DELIMITER}\n")
    if not delimiter:
        return {}
    parsed = safe_load(block)
    return parsed if isinstance(parsed, dict) else {}


def provider_slug(actual: str) -> str:
    """Return a provider name usable as part of a filename.

    Args:
        actual: The provider named in the report's frontmatter.

    Returns:
        The name, stripped and lowercased. Lowercase because that is how the
        repository writes provider slugs (``hypothesis_deep_research`` lowercases
        when it builds an output path) and how it reads them back
        (``deep_research_coverage.normalize_provider``); a mixed-case rename
        would produce a path a later existence check would not find.

    Raises:
        AlignmentError: If the name is empty or contains a path separator.
            ``Path.with_name`` rejects a separator with a ``ValueError``, which
            would escape as a traceback rather than as one of this module's
            refusals.
    """
    slug = actual.strip()
    if not slug or "/" in slug or "\\" in slug or slug in {".", ".."}:
        raise AlignmentError(
            f"{actual!r} is not usable as a provider name in a filename, so the "
            "report cannot be renamed to it."
        )
    return slug.lower()


def retarget_path(path: Path, requested: str, actual: str) -> Path:
    """Return the path this report should have, given who really wrote it.

    The provider slug is replaced where the recipe put it: the last occurrence
    of the requested slug in the filename stem. That covers every layout in
    this repo without needing to know any of them --
    ``Foo-deep-research-falcon.md``, ``Foo-datasets-falcon.md``,
    ``Foo-surrogacy-egfr-deep-research-falcon.md``, and the hypothesis layout
    ``kb/hypotheses/<disease>/<group>/falcon.md``, where the stem is the slug.

    Args:
        path: The report as written.
        requested: The provider slug the run asked for, as it appears in the name.
        actual: The provider that produced the report.

    Returns:
        The path the report should carry.

    Raises:
        AlignmentError: If the requested slug does not appear in the filename.
            Guessing where the provider belongs in a name we do not recognise
            would be worse than stopping.

    Examples:
        >>> retarget_path(Path("research/Foo-deep-research-falcon.md"), "falcon", "claude_code")
        PosixPath('research/Foo-deep-research-claude_code.md')
        >>> retarget_path(Path("kb/hypotheses/Long_COVID/g/falcon.md"), "falcon", "openai")
        PosixPath('kb/hypotheses/Long_COVID/g/openai.md')
    """
    actual = provider_slug(actual)
    stem = path.stem
    index = stem.rfind(requested)
    if index == -1:
        raise AlignmentError(
            f"{path.name} does not contain the requested provider "
            f"{requested!r}, so there is no way to tell which part of the name "
            f"is the provider. The report was produced by {actual!r} and is "
            f"named for something else; rename it by hand."
        )
    new_stem = stem[:index] + actual + stem[index + len(requested) :]
    return path.with_name(new_stem + path.suffix)


def _sidecars(report: Path, new_report: Path) -> list[tuple[Path, Path]]:
    """Return the ``(old, new)`` pairs for a report's companion files.

    The citations sidecar and the artifacts directory are named after the
    report, so they move with it.
    """
    pairs: list[tuple[Path, Path]] = []
    citations = report.with_name(f"{report.name}.citations.md")
    if citations.exists():
        pairs.append(
            (citations, new_report.with_name(f"{new_report.name}.citations.md"))
        )
    artifacts = report.with_name(f"{report.stem}_artifacts")
    if artifacts.is_dir():
        pairs.append((artifacts, new_report.with_name(f"{new_report.stem}_artifacts")))
    return pairs


def _rewrite_artifact_links(path: Path, old_stem: str, new_stem: str) -> None:
    """Point a moved report's artifact links at the moved artifacts directory.

    Reports link their artifacts by directory name, in the body
    (``[Edison artifact](Foo-deep-research-falcon_artifacts/artifact-00.md)``)
    and in the frontmatter ``artifacts:`` block. Renaming the directory without
    rewriting these leaves every link broken.

    Only ``<stem>_artifacts`` is rewritten, never the bare stem: the bare stem
    can appear in prose the provider wrote, and rewriting that would be editing
    the report's content.
    """
    text = path.read_text(encoding="utf-8")
    updated = text.replace(f"{old_stem}_artifacts", f"{new_stem}_artifacts")
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def align_report_provider(
    report: Path, requested: str, *, dry_run: bool = False
) -> Alignment:
    """Rename a report to the provider that produced it, if a fallback happened.

    Args:
        report: The report the run just wrote.
        requested: The provider slug the run asked for, as it appears in the name.
        dry_run: Report what would move without moving anything.

    Returns:
        An :class:`Alignment` describing the outcome. ``renamed_from`` is None
        when no fallback happened, which is the common case and not an error.

    Raises:
        AlignmentError: If the report is missing, if the provider cannot be
            located in its filename, or if any destination is already taken.
    """
    if not report.is_file():
        raise AlignmentError(f"No report at {report}")

    frontmatter = read_frontmatter(report)
    actual = frontmatter.get("provider")
    if not frontmatter.get("fell_back"):
        return Alignment(
            report=report,
            renamed_from=None,
            requested_provider=frontmatter.get("requested_provider") or requested,
            actual_provider=actual if isinstance(actual, str) else None,
        )

    if not isinstance(actual, str) or not actual:
        raise AlignmentError(
            f"{report.name} records a fallback but names no provider, so the "
            "report cannot be renamed to whoever wrote it."
        )

    actual = provider_slug(actual)
    new_report = retarget_path(report, requested, actual)
    if new_report == report:
        return Alignment(
            report=report,
            renamed_from=None,
            requested_provider=frontmatter.get("requested_provider") or requested,
            actual_provider=actual,
        )

    moves = [(report, new_report), *_sidecars(report, new_report)]
    taken = [str(new) for _, new in moves if new.exists()]
    if taken:
        raise AlignmentError(
            f"{report.name} was produced by {actual!r} after {requested!r} "
            f"failed, but its correct name is already taken: {', '.join(taken)}. "
            "Both reports are still on disk; decide which to keep rather than "
            "letting one overwrite the other."
        )

    if dry_run:
        return Alignment(
            report=new_report,
            renamed_from=report,
            requested_provider=frontmatter.get("requested_provider") or requested,
            actual_provider=actual,
            moved=tuple(moves),
        )

    for old, new in moves:
        shutil.move(str(old), str(new))

    for moved_path in (
        new_report,
        new_report.with_name(f"{new_report.name}.citations.md"),
    ):
        if moved_path.is_file():
            _rewrite_artifact_links(moved_path, report.stem, new_report.stem)

    return Alignment(
        report=new_report,
        renamed_from=report,
        requested_provider=frontmatter.get("requested_provider") or requested,
        actual_provider=actual,
        moved=tuple(moves),
    )
