#!/usr/bin/env bash
# Wrapper for linkml-reference-validator that applies the network resilience patch.
# This prevents crashes from transient NCBI network errors (IncompleteRead, etc.)
# Usage: scripts/run_reference_validator.sh [args...]
#   e.g.: scripts/run_reference_validator.sh validate data file.yaml --schema schema.yaml --target-class Disease

set -euo pipefail

run_lrv() {
    set +e
    output="$(uv run python -c "
import dismech.patch_reference_validator
from linkml_reference_validator.cli import app
app()
" "$@" 2>&1)"
    exit_code=$?
    set -e

    printf '%s\n' "$output"

    if [[ $exit_code -eq 0 ]]; then
        return 0
    fi

    # linkml-reference-validator may exit nonzero when it emits warning
    # results. Keep warning-only results advisory so transient/unfetchable
    # references do not block validation.
    if grep -Eq '^[[:space:]]*\[WARN(ING)?\]' <<<"$output" \
        && ! grep -Eq '^[[:space:]]*\[ERROR\]|Traceback|^Error:' <<<"$output"; then
        return 0
    fi

    return "$exit_code"
}

run_lrv "$@"
