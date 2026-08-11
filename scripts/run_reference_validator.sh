#!/usr/bin/env bash
# Wrapper for linkml-reference-validator that applies the network resilience patch.
# This prevents crashes from transient NCBI network errors (IncompleteRead, etc.)
# Usage: scripts/run_reference_validator.sh [args...]
#   e.g.: scripts/run_reference_validator.sh validate data file.yaml --schema schema.yaml --target-class Disease
#
# After the validator runs, an advisory `Snippets checked: N/N verified` line is
# appended for `validate data` invocations (issue #7252): the validator's own
# "Total checks: 0" counts *issues found*, not checks performed, so a clean run
# is indistinguishable from a no-op. The audit is read-only, offline (it reads
# only references_cache/), and never affects the exit code -- the validator
# stays the sole authority on pass/fail. Set DISMECH_SKIP_SNIPPET_AUDIT=1 to
# suppress it.

set -euo pipefail

# Set by run_lrv; the wrapper exits with this code.
lrv_exit=0
# Set by run_lrv when the validator did not complete (traceback / hard error).
lrv_crashed=0

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
        lrv_exit=0
        return 0
    fi

    # linkml-reference-validator may exit nonzero when it emits warning
    # results. Keep warning-only results advisory so transient/unfetchable
    # references do not block validation.
    if grep -Eq '^[[:space:]]*\[WARN(ING)?\]' <<<"$output" \
        && ! grep -Eq '^[[:space:]]*\[ERROR\]|Traceback|^Error:' <<<"$output"; then
        lrv_exit=0
        return 0
    fi

    # A traceback or hard error means the validator never finished walking the
    # data. An affirmative snippet count is at best unrelated to what failed and
    # at worst reassuring about a run that did not happen, so flag it and let
    # the audit stay quiet.
    if grep -Eq 'Traceback|^Error:' <<<"$output"; then
        lrv_crashed=1
    fi

    lrv_exit=$exit_code
    return 0
}

# Print the affirmative snippet count for `validate data FILE... [options]`.
# Silent for any other subcommand shape, and never fatal.
run_snippet_audit() {
    if [[ "${DISMECH_SKIP_SNIPPET_AUDIT:-0}" == "1" ]]; then
        return 0
    fi
    if [[ $lrv_crashed -eq 1 ]]; then
        echo "  (snippet audit skipped: the validator did not complete)" >&2
        return 0
    fi
    if [[ "${1:-}" != "validate" || "${2:-}" != "data" ]]; then
        return 0
    fi
    shift 2

    local -a files=()
    local schema="" config=""
    local collecting=1
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --schema)
                schema="${2:-}"
                collecting=0
                shift
                shift || true
                ;;
            --schema=*)
                schema="${1#*=}"
                collecting=0
                shift
                ;;
            --config)
                config="${2:-}"
                collecting=0
                shift
                shift || true
                ;;
            --config=*)
                config="${1#*=}"
                collecting=0
                shift
                ;;
            -*)
                collecting=0
                shift
                ;;
            *)
                # Positional data files precede every option; once an option has
                # been seen, remaining bare words are option values, not files.
                if [[ $collecting -eq 1 ]]; then
                    files+=("$1")
                fi
                shift
                ;;
        esac
    done

    if [[ ${#files[@]} -eq 0 ]]; then
        # Every current call site puts data files first. If options were seen
        # but no leading positionals, the arg order is one this deliberately
        # simple parser cannot read -- say so rather than silently printing
        # nothing.
        if [[ $collecting -eq 0 ]]; then
            echo "  (snippet audit skipped: no data files found before the first option)" >&2
        fi
        return 0
    fi

    local -a cmd=(uv run python -m dismech.reference_snippet_audit)
    if [[ -n "$schema" ]]; then
        cmd+=(--schema "$schema")
    fi
    if [[ -n "$config" ]]; then
        cmd+=(--config "$config")
    fi
    "${cmd[@]}" "${files[@]}" || true
}

run_lrv "$@"
run_snippet_audit "$@"

exit "$lrv_exit"
