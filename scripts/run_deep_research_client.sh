#!/usr/bin/env bash
# Wrapper for deep-research-client that applies dismech's linkml-reference-validator
# patches, the same way scripts/run_reference_validator.sh does for the validator
# CLI itself.
#
# Usage: scripts/run_deep_research_client.sh [args...]
#   e.g.: scripts/run_deep_research_client.sh research --template t.md --provider falcon ...
#         scripts/run_deep_research_client.sh validate-references report.md --in-place
#
# Why this exists: since 0.2.9, `deep-research-client` can resolve a report's
# references itself, and it does so by calling linkml-reference-validator
# in-process. That makes it a path that both READS and WRITES references_cache/,
# so it needs the same three repairs every other reference fetch in this repo
# gets:
#
#   1. NCBI retry/backoff on PMIDSource network methods. Upstream catches
#      (OSError, ValueError) around validation and exits 3, so one transient
#      IncompleteRead mid-run discards the whole validation section.
#   2. The issue #7697 delimiter-aware frontmatter read. Without it, a cache file
#      whose frontmatter contains a literal '---' is truncated on read, which
#      surfaces as a FALSE "unresolved reference" -- and the curation guidance
#      says not to cite anything listed as unresolved. That turns a tooling
#      artifact into deleted evidence, which is the failure this wrapper exists
#      to prevent.
#   3. _save_to_disk author coercion and the ClinicalTrials get_cache_path
#      alignment, both of which affect committed data.
#
# Keep this in sync with scripts/run_reference_validator.sh: if a patch is added
# there that affects the fetch/read path, it applies here too (both go through
# dismech.patch_reference_validator, so importing it is all that is required).

set -euo pipefail

exec uv run python -c "
import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the patches
from deep_research_client.cli import app

app()
" "$@"
