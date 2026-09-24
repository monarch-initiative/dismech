#!/usr/bin/env bash
# Wrapper for linkml-reference-validator that keeps warning-only results
# advisory, so a transient or unfetchable reference does not block validation.
# The validator stays the sole authority on pass/fail for everything else.
#
# This wrapper applied eleven runtime patches over the validator. Ten are gone:
# their defects are fixed upstream (#66-74, #85, #87, #88). The one that remains
# sanitizes the raw HTML URLSource caches, tracked as
# linkml/linkml-reference-validator#92 and deleted when that lands.
#
# Usage: scripts/run_reference_validator.sh [args...]
#   e.g.: scripts/run_reference_validator.sh validate data file.yaml --schema schema.yaml --target-class Disease
#
# The validator reports its own `Snippets checked:` / `Issues found:` counts and
# says explicitly when no comparison was performed, so this wrapper no longer
# appends a count of its own (issue #7252, fixed upstream in
# linkml/linkml-reference-validator#72). For the fast offline count on its own,
# without a validation run, use `just count-verified-snippets`.

set -euo pipefail

# Set by run_lrv; the wrapper exits with this code.
lrv_exit=0

run_lrv() {
    set +e
    output="$(uv run python -c "
import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the patch
from linkml_reference_validator.cli import app
app()
" "$@" 2>&1)"
    exit_code=$?
    set -e

    printf '%s\n' "$output"

    if [[ $exit_code -eq 0 ]]; then
        lrv_exit=0
        return 0
    fi

    # linkml-reference-validator may exit nonzero when it emits warning
    # results. Keep genuine warning-only results advisory. Repository configs
    # classify unfetchable references as ERROR so unverified evidence fails.
    if grep -Eq '^[[:space:]]*\[WARN(ING)?\]' <<<"$output" \
        && ! grep -Eq '^[[:space:]]*\[ERROR\]|Traceback|^Error:' <<<"$output"; then
        lrv_exit=0
        return 0
    fi

    lrv_exit=$exit_code
    return 0
}

run_lrv "$@"

exit "$lrv_exit"
