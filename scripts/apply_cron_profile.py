#!/usr/bin/env python3
"""Apply a named cron *profile* to the scheduled GitHub Actions workflows.

Cron schedules in GitHub Actions are hard-coded inline in each workflow YAML
with no native parameterisation. This script makes them switchable from a single
source of truth (`.github/cron-profiles.yaml`): pick a profile, and every managed
workflow's ``on.schedule`` cron block is rewritten to match.

Only the cron entries inside the ``schedule:`` block are touched. Everything else
(``workflow_dispatch`` inputs, ``jobs``, comments outside the schedule block) is
left byte-for-byte intact. We deliberately do *not* round-trip the whole workflow
through a YAML parser — GitHub's ``on:`` key is parsed as the YAML 1.1 boolean
``True``, which corrupts naive re-dumps — so the rewrite is a surgical,
line-based replacement of the schedule's cron lines.

Usage:
    python scripts/apply_cron_profile.py <profile>            # rewrite + commit
    python scripts/apply_cron_profile.py <profile> --no-commit
    python scripts/apply_cron_profile.py <profile> --dry-run  # show diff only
    python scripts/apply_cron_profile.py --list               # profiles / active
"""

from __future__ import annotations

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / ".github" / "cron-profiles.yaml"
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"

SCHEDULE_RE = re.compile(r"^(?P<indent>\s*)schedule:\s*$")
CRON_LINE_RE = re.compile(r"^\s*-\s*cron:\s*")
COMMENT_LINE_RE = re.compile(r"^\s*#")


class ConfigError(RuntimeError):
    """Raised when the profile config is malformed."""


# --------------------------------------------------------------------------- #
# Config loading / validation
# --------------------------------------------------------------------------- #
def load_config(path: Path) -> dict:
    if not path.exists():
        raise ConfigError(f"config not found: {path}")
    data = yaml.safe_load(path.read_text()) or {}
    profiles = data.get("profiles")
    if not isinstance(profiles, dict) or not profiles:
        raise ConfigError("config must define a non-empty `profiles:` mapping")

    # Every profile must cover the same set of workflows so a profile can't be
    # silently half-configured.
    workflow_sets = {}
    for name, profile in profiles.items():
        wfs = (profile or {}).get("workflows")
        if not isinstance(wfs, dict) or not wfs:
            raise ConfigError(f"profile '{name}' has no `workflows:` mapping")
        workflow_sets[name] = set(wfs)
    reference_name, reference = next(iter(workflow_sets.items()))
    for name, wfs in workflow_sets.items():
        if wfs != reference:
            missing = reference - wfs
            extra = wfs - reference
            detail = []
            if missing:
                detail.append(f"missing {sorted(missing)}")
            if extra:
                detail.append(f"unexpected {sorted(extra)}")
            raise ConfigError(
                f"profile '{name}' workflow set differs from '{reference_name}': "
                + "; ".join(detail)
            )

    # Validate cron expressions up front.
    for name, profile in profiles.items():
        for wf, entries in profile["workflows"].items():
            if not isinstance(entries, list) or not entries:
                raise ConfigError(f"{name}/{wf}: expected a non-empty list of cron entries")
            for entry in entries:
                expr = (entry or {}).get("cron")
                if not isinstance(expr, str) or len(expr.split()) != 5:
                    raise ConfigError(
                        f"{name}/{wf}: invalid cron expression {expr!r} "
                        "(must be 5 space-separated fields)"
                    )
    return data


def resolve_workflow_file(stem: str) -> Path:
    candidates = [WORKFLOW_DIR / f"{stem}.yml", WORKFLOW_DIR / f"{stem}.yaml"]
    found = [c for c in candidates if c.exists()]
    if not found:
        raise ConfigError(f"no workflow file for '{stem}' (tried .yml/.yaml)")
    if len(found) > 1:
        raise ConfigError(f"ambiguous workflow stem '{stem}': {[f.name for f in found]}")
    return found[0]


# --------------------------------------------------------------------------- #
# Workflow rewriting
# --------------------------------------------------------------------------- #
def render_cron_lines(entries: list[dict], indent: str) -> list[str]:
    lines = []
    for entry in entries:
        line = f'{indent}- cron: "{entry["cron"]}"'
        comment = entry.get("comment")
        if comment:
            line += f"  # {comment}"
        lines.append(line + "\n")
    return lines


def rewrite_schedule(text: str, entries: list[dict], *, wf_name: str) -> str:
    """Replace the cron entries in the first ``schedule:`` block of *text*."""
    lines = text.splitlines(keepends=True)

    sched_idx = next((i for i, ln in enumerate(lines) if SCHEDULE_RE.match(ln)), None)
    if sched_idx is None:
        raise ConfigError(f"{wf_name}: no `schedule:` block found")

    # The managed region runs from the line after `schedule:` while lines are
    # either cron entries or comments; it stops at the first other line (a blank
    # line or the next key such as `workflow_dispatch:`).
    start = sched_idx + 1
    end = start
    saw_cron = False
    while end < len(lines):
        if CRON_LINE_RE.match(lines[end]):
            saw_cron = True
            end += 1
        elif COMMENT_LINE_RE.match(lines[end]):
            end += 1
        else:
            break
    if not saw_cron:
        raise ConfigError(f"{wf_name}: `schedule:` block has no `- cron:` entries to replace")

    # Preserve the existing cron-line indentation.
    indent = "    "
    for ln in lines[start:end]:
        if CRON_LINE_RE.match(ln):
            indent = ln[: len(ln) - len(ln.lstrip())]
            break

    new_lines = lines[:start] + render_cron_lines(entries, indent) + lines[end:]
    new_text = "".join(new_lines)

    # Sanity: the rewritten file must still parse as YAML.
    try:
        yaml.safe_load(new_text)
    except yaml.YAMLError as exc:  # pragma: no cover - defensive
        raise ConfigError(f"{wf_name}: rewrite produced invalid YAML: {exc}") from exc
    return new_text


def set_active(config_text: str, profile: str) -> str:
    new_text, n = re.subn(
        r"^active:.*$", f"active: {profile}", config_text, count=1, flags=re.MULTILINE
    )
    if n == 0:
        raise ConfigError("config has no top-level `active:` line to update")
    return new_text


# --------------------------------------------------------------------------- #
# Git
# --------------------------------------------------------------------------- #
def git_commit(paths: list[Path], profile: str) -> None:
    rel = [str(p.relative_to(REPO_ROOT)) for p in paths]
    subprocess.run(["git", "-C", str(REPO_ROOT), "add", *rel], check=True)
    msg = f"Apply '{profile}' cron profile to scheduled workflows"
    subprocess.run(["git", "-C", str(REPO_ROOT), "commit", "-m", msg], check=True)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def cmd_list(config: dict) -> int:
    active = config.get("active")
    print(f"active profile: {active}\n")
    for name, profile in config["profiles"].items():
        marker = "*" if name == active else " "
        desc = (profile or {}).get("description", "")
        print(f" {marker} {name:<14} {desc}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", nargs="?", help="profile name to apply")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--list", action="store_true", help="list profiles and exit")
    parser.add_argument("--dry-run", action="store_true", help="show diffs, write nothing")
    parser.add_argument("--no-commit", action="store_true", help="write files but do not commit")
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
    except ConfigError as exc:
        parser.error(str(exc))

    if args.list or not args.profile:
        return cmd_list(config)

    if args.profile not in config["profiles"]:
        parser.error(
            f"unknown profile '{args.profile}'. Available: "
            + ", ".join(config["profiles"])
        )

    workflows = config["profiles"][args.profile]["workflows"]

    changed: list[Path] = []
    try:
        for stem, entries in workflows.items():
            path = resolve_workflow_file(stem)
            original = path.read_text()
            updated = rewrite_schedule(original, entries, wf_name=stem)
            if updated != original:
                changed.append(path)
                if args.dry_run:
                    diff = difflib.unified_diff(
                        original.splitlines(keepends=True),
                        updated.splitlines(keepends=True),
                        fromfile=f"a/{path.relative_to(REPO_ROOT)}",
                        tofile=f"b/{path.relative_to(REPO_ROOT)}",
                    )
                    sys.stdout.writelines(diff)
                else:
                    path.write_text(updated)

        config_text = args.config.read_text()
        new_config_text = set_active(config_text, args.profile)
        config_changed = new_config_text != config_text
        if config_changed and not args.dry_run:
            args.config.write_text(new_config_text)
    except ConfigError as exc:
        parser.error(str(exc))

    if args.dry_run:
        print(
            f"\n[dry-run] profile '{args.profile}': "
            f"{len(changed)} workflow file(s) would change."
        )
        return 0

    if not changed and not config_changed:
        print(f"Profile '{args.profile}' already applied — nothing to do.")
        return 0

    commit_paths = changed + ([args.config] if config_changed else [])
    print(f"Applied profile '{args.profile}':")
    for p in changed:
        print(f"  rewrote {p.relative_to(REPO_ROOT)}")
    if config_changed:
        print(f"  set active: {args.profile} in {args.config.relative_to(REPO_ROOT)}")

    if args.no_commit:
        print("\n--no-commit: changes written to the working tree (unstaged) for your review.")
        return 0

    git_commit(commit_paths, args.profile)
    print("\nCommitted. Push with: git push -u origin <branch>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
