#!/usr/bin/env bash
# Wrapper for linkml-term-validator that fails CI on warnings.
#
# Under linkml-term-validator 0.4.5 (the version in uv.lock; pyproject.toml
# declares >=0.4.5, not a pin) `validate-data` exits 1 whenever a file has any
# result at all, WARNING included: severity only picks the emoji. The WARN
# grep and the success-line grep below are therefore defence in depth. They
# exist so that a future version that downgrades warnings to a zero exit, or
# stops printing the success line, still fails CI here instead of passing
# quietly. Note the grep reads stdout and stderr together, so an unrelated
# WARNING line (a DeprecationWarning, an OAK message) will also fail a run.
#
# The wrapper used to probe `validate-data --help` on every call for a
# `--strict` or `--fail-on-warnings` flag. Upstream
# linkml/linkml-term-validator#29 (the request for such a flag) is still
# open, so the probe could only ever answer "unsupported" and cost a full
# interpreter start plus the linkml import tree on every validate-data call
# (dismech#11004). The probe is gone. When #29 ships and uv.lock resolves a
# version that has the flag, pass the flag and keep the greps; do not
# reinstate a per-call probe.

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

set +e
output="$(uv run linkml-term-validator validate-data "$@" 2>&1)"
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

# Accept single-file ("Validation passed") or multi-file ("N files passed validation") success
if ! grep -qE "(Validation passed|[0-9]+ files? passed)" <<<"$output"; then
    echo "Strict term validation failed: validator did not report success." >&2
    exit 1
fi
