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
#
# After `cache reference ID`, a WARNING is printed to stderr when the cache file
# just written carries `content_type: unavailable` (issue #9825): the fetcher
# reports "Successfully cached" for a record with no quotable text, and nothing
# else says so. Advisory only; the exit code is unchanged. Set
# DISMECH_SKIP_EMPTY_CACHE_WARNING=1 to suppress it.

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

# Warn when `cache reference ID...` wrote a record with no quotable text.
# Silent for any other subcommand shape, and never fatal.
run_empty_cache_warning() {
    if [[ "${DISMECH_SKIP_EMPTY_CACHE_WARNING:-0}" == "1" ]]; then
        return 0
    fi
    if [[ $lrv_exit -ne 0 ]]; then
        return 0
    fi
    if [[ "${1:-}" != "cache" || "${2:-}" != "reference" ]]; then
        return 0
    fi
    shift 2

    local -a ids=()
    local cache_dir="references_cache"
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --cache-dir|-c)
                cache_dir="${2:-$cache_dir}"
                shift
                shift || true
                ;;
            --cache-dir=*)
                cache_dir="${1#*=}"
                shift
                ;;
            --config)
                shift
                shift || true
                ;;
            -*)
                shift
                ;;
            *)
                ids+=("$1")
                shift
                ;;
        esac
    done

    if [[ ${#ids[@]} -eq 0 ]]; then
        return 0
    fi
    uv run python -m dismech.reference_cache_frontmatter fetch-warning \
        --cache-dir "$cache_dir" "${ids[@]}" || true
}

run_lrv "$@"
run_empty_cache_warning "$@"

exit "$lrv_exit"
