"""Curation stub queue: the outstanding-work list under `stubs/`.

A stub is a one-file placeholder for a disease the project intends to curate.
Curating it means deleting the stub and adding the `kb/disorders/` entry in the
same pull request, so the stub directory *is* the queue and its size is the
remaining work. Anyone can add, re-prioritize, or retire a stub by PR.

This replaces reading a ranked score out of `dashboard/priority.json`. See
`docs/curation-stubs.md`.
"""

from .claims import (
    Claim,
    double_claims,
    index_claims,
    parse_claims,
    unkeyed_claims,
)
from .model import (
    CoverageIndex,
    Stub,
    StubIssue,
    build_coverage_index,
    check_stubs,
    default_repo_root,
    default_stub_dir,
    iter_stub_files,
    load_stub,
    load_stubs,
    load_stubs_reporting_errors,
    slugify_label,
    stub_filename,
)

__all__ = [
    "Claim",
    "CoverageIndex",
    "Stub",
    "StubIssue",
    "build_coverage_index",
    "check_stubs",
    "default_repo_root",
    "default_stub_dir",
    "double_claims",
    "index_claims",
    "iter_stub_files",
    "load_stub",
    "load_stubs",
    "load_stubs_reporting_errors",
    "parse_claims",
    "slugify_label",
    "stub_filename",
    "unkeyed_claims",
]
