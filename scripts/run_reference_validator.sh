#!/usr/bin/env bash
# Wrapper for linkml-reference-validator that applies the network resilience patch.
# This prevents crashes from transient NCBI network errors (IncompleteRead, etc.)
# Usage: scripts/run_reference_validator.sh [args...]
#   e.g.: scripts/run_reference_validator.sh validate data file.yaml --schema schema.yaml --target-class Disease

exec uv run python -c "
import dismech.patch_reference_validator
from linkml_reference_validator.cli import app
app()
" "$@"
