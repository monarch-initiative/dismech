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
#
# Ontology-service outages (dismech#12634). linkml-term-validator exits 2 and
# prints "ontology service unavailable" when an uncached term could not be
# looked up because OLS (or another network adapter) timed out or refused the
# connection. That means the terms were *not checked*, not that one is wrong.
# The wrapper re-reports that case as exit 75 (EX_TEMPFAIL) so a caller can
# tell it apart from a real validation failure (exit 1) and from a usage error
# (exit 2, which is also what click returns for a bad option; the message is
# checked as well as the code for that reason). Exit 75 is still non-zero, so
# every caller that only tests for success (`just validate`,
# `just validate-disorders`, `just qc`, CI) stays strict. Only
# `validate-pre-edit` treats it as a warning.

set -euo pipefail

# Keep in sync with the check in project.justfile's `validate-pre-edit`.
EXIT_SERVICE_UNAVAILABLE=75

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

if [[ $exit_code -eq 2 ]] && grep -qi 'ontology service unavailable' <<<"$output"; then
    echo "Term validation could not run: ontology service unavailable (exit $EXIT_SERVICE_UNAVAILABLE)." >&2
    exit "$EXIT_SERVICE_UNAVAILABLE"
fi

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
