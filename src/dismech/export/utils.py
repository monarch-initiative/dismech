"""Shared helpers for dismech export modules."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

try:  # libyaml C loader when available (see render.py)
    from yaml import CSafeLoader as _SafeLoader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as _SafeLoader

# Deep-research report filename pattern: ``<slug>-deep-research-<provider>.md``.
# Shared with render.py so the homepage report count and the research index page
# count the same files (issue #5567).
RESEARCH_REPORT_PATTERN = re.compile(
    r"^(?P<slug>.+)-deep-research-(?P<provider>[^.]+)\.md$",
    re.IGNORECASE,
)


def discover_disorder_files(input_dir: Path) -> list[Path]:
    """Return sorted disorder YAML files in ``input_dir``, excluding history files."""
    return [
        path
        for path in sorted(input_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    ]


def _count_kb_yaml(kb_dir: Path) -> int:
    """Count non-history ``*.yaml`` files directly under ``kb_dir``."""
    if not kb_dir.exists():
        return 0
    return sum(
        1
        for path in kb_dir.glob("*.yaml")
        if not path.name.endswith(".history.yaml")
    )


# Path convention for the count helpers below: ``research/``, ``kb/comorbidities``
# and ``kb/groupings`` are repo-root data (not shipped inside the package), so
# their defaults are relative and assume the current working directory is the
# repo root — which is how the export/render pipeline (and CI) always runs them;
# callers that need a specific location pass an explicit path (the tests do). By
# contrast ``count_classifications`` resolves ``schema/classifications`` via
# ``__file__`` because those YAMLs ship *inside* the package.
def count_research_reports(research_dir: Path = Path("research")) -> int:
    """Count deep-research report files (``*-deep-research-*.md``) under ``research/``.

    Matches the file set that ``render.py`` aggregates on the research index page.
    """
    if not research_dir.exists():
        return 0
    return sum(
        1 for path in research_dir.glob("*.md") if RESEARCH_REPORT_PATTERN.match(path.name)
    )


def count_comorbidities(comorbidity_dir: Path = Path("kb/comorbidities")) -> int:
    """Count comorbidity/trajectory-pair YAML files (one per disease-pair)."""
    return _count_kb_yaml(comorbidity_dir)


def count_groupings(grouping_dir: Path = Path("kb/groupings")) -> int:
    """Count disease-grouping YAML files."""
    return _count_kb_yaml(grouping_dir)


def count_classifications(
    classification_dir: Path | None = None,
) -> int:
    """Count classification enums defined under ``schema/classifications/*.yaml``.

    Matches the count shown on the classifications index page.
    """
    if classification_dir is None:
        classification_dir = (
            Path(__file__).resolve().parent.parent / "schema" / "classifications"
        )
    if not classification_dir.exists():
        return 0
    total = 0
    for path in classification_dir.glob("*.yaml"):
        data = yaml.load(path.read_text(), Loader=_SafeLoader) or {}
        total += len(data.get("enums") or {})
    return total
