#!/usr/bin/env python3
"""Validate the Claude Code skill files under ``.claude/skills/``.

Nothing checked these until now, and one of them had been silently broken for
close to a month. ``.claude/skills/microbiome-curation/`` held ``skill.md`` in
lowercase; skills are discovered by looking for ``SKILL.md``, so Claude Code
loaded 21 of the 22 directories and said nothing about the 22nd. The only
symptom is a skill that never triggers, which looks exactly like a skill nobody
happened to need (issue #11758).

Why this is a whole-tree sweep rather than a changed-path one
-------------------------------------------------------------
Skill files arrive through PRs about something else. The lowercase filename
landed in #8651, a curation PR titled "Add CMT4, Intermediate CMT, and HSAN
entries" -- a skill file rode along with a batch of disorder entries and got the
attention the PR's subject got. CI selects pytest by changed path, and that PR
touched ``kb/``, so a changed-path check would have been skipped by the very
change that introduced the fault. Same reasoning already recorded in CLAUDE.md
for ``check-duplicate-keys`` and ``check-entity-refs``.

What is checked
---------------
* every skill directory holds a ``SKILL.md``, cased exactly that way;
* its YAML frontmatter parses;
* ``name`` is present, matches the directory name, and is in the
  lowercase-hyphen form skills are addressed by;
* ``description`` is present and non-empty -- it is the whole basis on which a
  skill is offered to a session, so an empty one is a skill that never fires;
* any ``.claude/skills/...`` path referenced from a justfile, workflow, or
  script still exists. ``project.justfile`` runs
  ``.claude/skills/projman/scripts/sync_epic.py``; renaming or dropping that
  file with the skill would otherwise surface as a failing recipe.

Description *length* is reported but never gated: the corpus tops out around 500
characters and no limit is documented in this repo, so a threshold here would be
invented rather than sourced.

Usage
-----
    python scripts/check_skill_files.py          # gate: fail on any finding
    python scripts/check_skill_files.py --list   # census, always exit 0
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"

SKILL_FILENAME = "SKILL.md"

# A skill is addressed by this name (`/<name>`, and the Skill tool's `skill`
# argument), so it follows the same lowercase-hyphen form as the directory.
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

# Files that *execute* something and could therefore break when a skill's
# supporting files move. Prose that mentions a skill path is not included: a
# stale path in documentation is worth fixing but is not a broken build.
REFERENCE_GLOBS = (
    "justfile",
    "project.justfile",
    ".github/workflows/*.yml",
    ".github/workflows/*.yaml",
    "scripts/*.py",
    "src/dismech/**/*.py",
)

REFERENCE_PATTERN = re.compile(r"\.claude/skills/[A-Za-z0-9_./-]+")


@dataclass(frozen=True)
class Finding:
    """One defect, keyed on the file or directory a reader should open."""

    location: str
    kind: str
    detail: str


def split_frontmatter(text: str) -> str | None:
    """Return the YAML frontmatter block, or None when there is no delimited one.

    Frontmatter is the leading ``---`` fence through the next ``---`` on its own
    line. Anything else -- no fence, or an unterminated one -- is not
    frontmatter, and the caller reports it as such.
    """
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[1:index])
    return None


def skill_directories() -> list[Path]:
    """Every immediate subdirectory of ``.claude/skills/``, sorted by name."""
    if not SKILLS_DIR.is_dir():
        return []
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:  # pragma: no cover - path outside the repo
        return str(path)


def check_skill(directory: Path) -> tuple[list[Finding], dict | None]:
    """Check one skill directory; return its findings and parsed frontmatter."""
    findings: list[Finding] = []
    expected = directory / SKILL_FILENAME

    if not expected.is_file():
        # Name the wrong-case file when there is one. "SKILL.md is missing" sends
        # a reader looking for a file they can see sitting right there.
        variants = [
            p.name
            for p in sorted(directory.iterdir())
            if p.is_file() and p.name.lower() == SKILL_FILENAME.lower()
        ]
        if variants:
            findings.append(
                Finding(
                    _display(directory),
                    "miscased_skill_file",
                    f"holds {', '.join(variants)}; the file must be named {SKILL_FILENAME}",
                )
            )
        else:
            findings.append(
                Finding(
                    _display(directory),
                    "missing_skill_file",
                    f"no {SKILL_FILENAME}; the skill will not be discovered",
                )
            )
        return findings, None

    location = _display(expected)
    text = expected.read_text(encoding="utf-8")
    block = split_frontmatter(text)
    if block is None:
        findings.append(
            Finding(location, "missing_frontmatter", "no delimited --- frontmatter block")
        )
        return findings, None

    try:
        frontmatter = yaml.safe_load(block)
    except yaml.YAMLError as exc:
        findings.append(
            Finding(location, "unparsable_frontmatter", f"frontmatter is not valid YAML ({exc})")
        )
        return findings, None

    if not isinstance(frontmatter, dict):
        findings.append(
            Finding(location, "unparsable_frontmatter", "frontmatter is not a YAML mapping")
        )
        return findings, None

    name = frontmatter.get("name")
    if not isinstance(name, str) or not name.strip():
        findings.append(Finding(location, "missing_name", "frontmatter has no non-empty name"))
    else:
        name = name.strip()
        if name != directory.name:
            findings.append(
                Finding(
                    location,
                    "name_mismatch",
                    f"name is {name!r} but the directory is {directory.name!r}",
                )
            )
        if not NAME_PATTERN.fullmatch(name):
            findings.append(
                Finding(
                    location,
                    "malformed_name",
                    f"name {name!r} is not lowercase-with-hyphens",
                )
            )

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        findings.append(
            Finding(
                location,
                "missing_description",
                "frontmatter has no non-empty description; nothing would offer this skill",
            )
        )

    return findings, frontmatter


def check_references(root: Path | None = None) -> list[Finding]:
    """Report `.claude/skills/...` paths referenced from code that no longer exist."""
    root = ROOT if root is None else root
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    for pattern in REFERENCE_GLOBS:
        for source in sorted(root.glob(pattern)):
            if not source.is_file():
                continue
            try:
                text = source.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):  # pragma: no cover - binary/unreadable
                continue
            for match in REFERENCE_PATTERN.findall(text):
                # Trailing punctuation from prose around the path, not part of it.
                referenced = match.rstrip(".,;:)\"'")
                key = (str(source), referenced)
                if key in seen:
                    continue
                seen.add(key)
                if not (root / referenced).exists():
                    findings.append(
                        Finding(
                            _display(source),
                            "missing_referenced_path",
                            f"references {referenced}, which does not exist",
                        )
                    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--list",
        action="store_true",
        help="print a census of every skill and exit 0, whatever it finds",
    )
    args = parser.parse_args()

    directories = skill_directories()
    if not directories:
        print(f"No skill directories found under {_display(SKILLS_DIR)}.", file=sys.stderr)
        return 1

    findings: list[Finding] = []
    census: list[tuple[Path, dict | None, int]] = []
    for directory in directories:
        skill_findings, frontmatter = check_skill(directory)
        findings.extend(skill_findings)
        census.append((directory, frontmatter, len(skill_findings)))

    findings.extend(check_references())

    if args.list:
        print(f"{len(directories)} skill(s) under {_display(SKILLS_DIR)}:\n")
        for directory, frontmatter, defect_count in census:
            description = (frontmatter or {}).get("description") or ""
            status = "OK" if defect_count == 0 else f"{defect_count} finding(s)"
            print(f"  {directory.name:<34} {len(description):>5} chars  {status}")
        if findings:
            print(f"\n{len(findings)} finding(s); run without --list for detail.")
        return 0

    if findings:
        print("Defective Claude Code skill file(s) under .claude/skills/.\n")
        print("A skill whose SKILL.md is missing, miscased, or missing its name or")
        print("description is simply never loaded -- there is no error, and the only")
        print("symptom is a skill that never triggers (issue #11758).\n")
        for finding in findings:
            print(f"{finding.location}: {finding.kind}: {finding.detail}")
        print(f"\n{len(findings)} finding(s) across {len(directories)} skill(s).")
        return 1

    print(f"OK: {len(directories)} skill(s) under {_display(SKILLS_DIR)} are well-formed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
