#!/usr/bin/env bash
# Wrapper for linkml-term-validator that fails CI on warnings.
# Uses upstream strict/warning-fail flags when available; otherwise treats WARN output as fatal.
# Remove once linkml/linkml-term-validator#29 is available in the CLI.

set -euo pipefail

if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <linkml-term-validator subcommand> [args...]" >&2
    exit 2
fi

subcommand=$1
shift

if [[ "$subcommand" != "validate-data" ]]; then
    exec uv run linkml-term-validator "$subcommand" "$@"
fi

help_output="$(uv run linkml-term-validator validate-data --help 2>&1)"
strict_args=()

if grep -q -- "--strict" <<<"$help_output"; then
    strict_args+=(--strict)
elif grep -q -- "--fail-on-warnings" <<<"$help_output"; then
    strict_args+=(--fail-on-warnings)
fi

set +e
cmd=(uv run linkml-term-validator validate-data "$@")
if [[ ${#strict_args[@]} -gt 0 ]]; then
    cmd+=("${strict_args[@]}")
fi
output="$("${cmd[@]}" 2>&1)"
exit_code=$?
set -e

printf '%s\n' "$output"

if [[ $exit_code -ne 0 ]]; then
    exit "$exit_code"
fi

if grep -Eq '(^|[^[:alnum:]_])(WARN|WARNING)([^[:alnum:]_]|$)' <<<"$output"; then
    echo "Strict term validation failed: validator emitted warnings." >&2
    exit 1
fi

if ! grep -q "Validation passed" <<<"$output"; then
    echo "Strict term validation failed: validator did not report success." >&2
    exit 1
fi
