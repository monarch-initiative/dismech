## Add your own just recipes here. This is imported by the main justfile.

# Default schema path
schema_path := "src/dismech/schema/dismech.yaml"
history_schema_path := "src/dismech/schema/history.yaml"
synthesis_schema_path := "src/dismech/schema/research_synthesis.yaml"
kb_dir := "kb/disorders"
modules_dir := "kb/modules"
comorbidity_dir := "kb/comorbidities"
history_dir := "history"
groupings_dir := "kb/groupings"
ref_validator_config := "conf/reference_validator_config.yaml"
mondo_db := env_var_or_default("MONDO_DB_PATH", x'${HOME}/.data/oaklib/mondo.db')
# Wrapper script that patches linkml-reference-validator for network resilience
ref_validator := "scripts/run_reference_validator.sh"
# Wrapper script that applies the SAME patches to deep-research-client, which
# since 0.2.9 calls linkml-reference-validator in-process to check a report's
# references -- so it too reads and writes references_cache/ and must not run
# unpatched. Notably it needs the issue #7697 delimiter-aware frontmatter read:
# a truncated read surfaces as a false "unresolved reference", and curators are
# told not to cite those.
dr_client := "scripts/run_deep_research_client.sh"
# Wrapper script that enforces warning-fail behavior for term validation
term_validator := "scripts/run_term_validator.sh"

# Validate all disorder YAML files (schema + terms + references)
# Runs each validator once over all files so in-memory schema, ontology, and
# reference caches are reused within that phase.
[group('QC')]
validate-all:
    #!/usr/bin/env bash
    set -u
    just check-enum-cache-offline

    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}} | sort)
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi

    just fix-references-cache "${files[@]}"

    exit_code=0
    echo "Validating ${#files[@]} disorder files (batched)..."
    echo "Schema validation (batch)..."
    uv run linkml-validate --schema {{schema_path}} --target-class Disease "${files[@]}" || exit_code=1
    echo ""

    echo "Term validation (batch)..."
    {{term_validator}} validate-data "${files[@]}" -s {{schema_path}} -t Disease --labels -c {{oak_config}} || exit_code=1
    echo ""

    echo "Reference validation (batch)..."
    {{ref_validator}} validate data "${files[@]}" --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}} || exit_code=1
    echo ""

    just normalize-cache || exit_code=1
    if [ $exit_code -ne 0 ]; then
        echo "✗ Validation completed with errors (see above)"
        exit $exit_code
    fi
    echo "✓ All files validated successfully!"

# Full validation of a single disorder file (schema + terms + references)
# Note: default validation runs only the offline enum-cache structural check.
# The full OAK-backed `check-enum-cache` audit re-derives membership for EVERY
# cached CURIE one at a time (see scan_enum_cache_dir -> is_value_in_enum), so
# run it explicitly only when refreshing/auditing enum cache membership.
#
# Cost, now that the ontologies are on `ols:`: that is 13,870 CURIEs across
# cache/enums/*.csv, each costing at least one OLS ancestors round trip at
# roughly 1.5-2 s, i.e. the better part of a day serialized. Note this audit was
# ALREADY mostly remote before the HP/CL/CHEBI/ENVO/FOODON migration — 8,138 of
# those CURIEs (59%) belong to enums backed by MONDO/GO/UBERON/NCIT/NCBITaxon,
# which moved to OLS in #5160. The migration took it from 59% to 99.3% remote
# (only 99 CURIEs, ECTO/XCO/OPL/ICD, still resolve locally); it made an already
# impractical full audit somewhat slower rather than newly expensive.
#
# If you genuinely need a fast full re-derivation, point the relevant prefixes
# at `sqlite:obo:*` in conf/oak_config.yaml for the duration and restore the
# file afterwards — the same escape hatch the note at the bottom of that file
# documents for OLS timeouts. Membership results are adapter-independent
# (verified before each migration), so the audit is equally valid either way.
[group('QC')]
validate file:
    #!/usr/bin/env bash
    set -e
    echo "Schema validation..."
    uv run linkml-validate --schema {{schema_path}} --target-class Disease {{file}}
    echo "Term validation..."
    {{term_validator}} validate-data {{file}} -s {{schema_path}} -t Disease --labels -c {{oak_config}}
    echo "Reference validation..."
    just fix-references-cache "{{file}}"
    {{ref_validator}} validate data {{file}} --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}}
    just normalize-cache
    echo "✓ All validations passed for {{file}}"

# Fast, non-mutating validation of a single disorder file, for the pre-edit hook
# (.claude/hooks/validate_disorder_hook.py). This runs on EVERY Edit/Write to
# kb/disorders, so it differs from `validate` in two deliberate ways (#8542):
#
# 1. It does not rewrite the caches. No `fix-references-cache`, no
#    `normalize-cache`, and `--no-full-text` so reference validation neither
#    downloads PDFs nor writes `full_text_attempted` back into cached records.
#    Cache normalization is a curator/CI step; an editor keystroke should not
#    leave the curator's worktree dirty. Measured on kb/disorders/Asthma.yaml
#    (193 snippets): `validate` takes ~8m25s and leaves 106 modified
#    references_cache/ files behind; this takes ~22s and leaves none. Keep it
#    that way — a step added here must not modify tracked files. (Validating a
#    newly cited reference still *creates* its cache record, which is wanted:
#    that is a new untracked file the curator should commit, not churn.)
#
# 2. Only schema and term validation are blocking. Those are deterministic and
#    offline, and cover what the hook exists to stop: malformed structure and
#    hallucinated ontology IDs. Snippet verification depends on what the cache
#    happens to hold — a quote from a paywalled paper's body is reported as
#    unverified, not wrong — so failing an in-progress edit on it strands the
#    curator mid-file. It is reported here as advisory and enforced for real by
#    `just validate`, `just qc`, and CI before anything merges.
[group('QC')]
validate-pre-edit file:
    #!/usr/bin/env bash
    set -e
    echo "Schema validation..."
    uv run linkml-validate --schema {{schema_path}} --target-class Disease {{file}}
    echo "Term validation..."
    {{term_validator}} validate-data {{file}} -s {{schema_path}} -t Disease --labels -c {{oak_config}}
    echo "Reference validation (advisory, cache-bound)..."
    if ! {{ref_validator}} validate data {{file}} --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}} --no-full-text; then
        echo "⚠ Reference validation reported issues (advisory here; run \`just validate\` before committing)"
    fi
    echo "✓ Pre-edit validation passed for {{file}}"

# Full validation of one or more disorder files, batched by validator phase.
# This is intended for CI changed-file validation, where a PR may touch hundreds
# of disorder YAMLs but still should avoid full-corpus validation. Reference
# validation stays cache-bound (`--no-full-text`) so CI does not expand the
# reference cache or download PDFs.
[group('QC')]
validate-disorders *files:
    #!/usr/bin/env bash
    set -u
    existing=()
    # Iterate real positional args (see `set positional-arguments` in justfile) so
    # filenames with shell metacharacters (e.g. Bell's_Palsy.yaml) are safe (#5525).
    for f in "$@"; do
        if [[ "$f" == {{kb_dir}}/*.yaml && "$f" != *.history.yaml && -f "$f" ]]; then
            existing+=("$f")
        elif [[ ! -f "$f" ]]; then
            echo "Skipping deleted/missing file: $f"
        else
            echo "Skipping non-disorder file: $f"
        fi
    done
    if [ ${#existing[@]} -eq 0 ]; then
        echo "No existing disorder YAML files to validate."
        exit 0
    fi

    exit_code=0
    echo "Validating ${#existing[@]} disorder file(s) (batched)..."
    echo "Schema validation (batch)..."
    uv run linkml-validate --schema {{schema_path}} --target-class Disease "${existing[@]}" || exit_code=1
    echo ""

    echo "Term validation (batch)..."
    {{term_validator}} validate-data "${existing[@]}" -s {{schema_path}} -t Disease --labels -c {{oak_config}} || exit_code=1
    echo ""

    echo "Reference validation (batch)..."
    just fix-references-cache "${existing[@]}"
    {{ref_validator}} validate data "${existing[@]}" --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}} --no-full-text || exit_code=1
    echo ""

    just normalize-cache || exit_code=1
    if [ $exit_code -ne 0 ]; then
        echo "✗ Validation failed for one or more disorder files (see above)"
        exit $exit_code
    fi
    echo "✓ All ${#existing[@]} disorder file(s) passed validation."

# Schema-only validation (fast, structure check)
[group('QC')]
validate-schema file:
    uv run linkml-validate --schema {{schema_path}} --target-class Disease {{file}}

# Scaffold a new append-only history record (pass-through to scripts/new_history.py).
# Run `just new-history --help` for all options. Prints the created path.
# Example:
#   just new-history --kind disorder --slug Asthma --event CREATE --outcome changed \
#     --summary "Create: Asthma" --agent-tool claude-code --pr 5123 --details "..."
[group('QC')]
new-history *ARGS:
    uv run python scripts/new_history.py {{ARGS}}

# Validate a single history record
[group('QC')]
validate-history file:
    uv run linkml-validate --schema {{history_schema_path}} --target-class HistoryRecord {{file}}

# Validate all history records
[group('QC')]
validate-history-all:
    #!/usr/bin/env bash
    set -e
    if [[ ! -d "{{history_dir}}" ]]; then
        echo "No history directory found."
        exit 0
    fi
    files=()
    while IFS= read -r f; do
        files+=("$f")
    done < <(find "{{history_dir}}" -type f -name '*.yaml' | sort)
    if [ ${#files[@]} -eq 0 ]; then
        echo "No history YAML files found in {{history_dir}}."
        exit 0
    fi
    printf 'Validating %s history record(s).\n' "${#files[@]}"
    uv run linkml-validate --schema {{history_schema_path}} --target-class HistoryRecord "${files[@]}"

# Validate a single cross-provider research synthesis (research/*-research-synthesis.yaml)
[group('QC')]
validate-synthesis file:
    uv run linkml-validate --schema {{synthesis_schema_path}} --target-class ResearchSynthesis {{file}}
    uv run python -m dismech.research_synthesis {{file}}

# Validate all cross-provider research syntheses
[group('QC')]
validate-synthesis-all:
    #!/usr/bin/env bash
    set -e
    if [[ ! -d "{{research_dir}}" ]]; then
        echo "No research directory found."
        exit 0
    fi
    files=()
    while IFS= read -r f; do
        files+=("$f")
    done < <(find "{{research_dir}}" -type f -name '*-research-synthesis.yaml' | sort)
    if [ ${#files[@]} -eq 0 ]; then
        echo "No research synthesis YAML files found in {{research_dir}}."
        exit 0
    fi
    printf 'Validating %s research synthesis file(s).\n' "${#files[@]}"
    uv run linkml-validate --schema {{synthesis_schema_path}} --target-class ResearchSynthesis "${files[@]}"
    uv run python -m dismech.research_synthesis "${files[@]}"

# Schema validation for all files (batched: one process startup for all files)
[group('QC')]
validate-schema-all:
    #!/usr/bin/env bash
    set -e
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}})
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    echo "Validating ${#files[@]} disorder files (schema)..."
    uv run linkml-validate --schema {{schema_path}} --target-class Disease "${files[@]}"

# Schema validation for all comorbidity YAML files
[group('QC')]
validate-comorbidities:
    #!/usr/bin/env bash
    set -e
    shopt -s nullglob
    files=({{comorbidity_dir}}/*.yaml)
    if [ ${#files[@]} -eq 0 ]; then
        echo "No comorbidity files found in {{comorbidity_dir}}"
        exit 0
    fi
    for f in "${files[@]}"; do
        echo "Validating comorbidity: $f"
        uv run linkml-validate --schema {{schema_path}} --target-class ComorbidityAssociation "$f"
    done

# Full validation of a single comorbidity file (schema + terms + references)
# Skips `check-enum-cache` (whole-cache OAK re-derivation); see `validate`.
[group('QC')]
validate-comorbidity file:
    #!/usr/bin/env bash
    set -e
    echo "Schema validation..."
    uv run linkml-validate --schema {{schema_path}} --target-class ComorbidityAssociation {{file}}
    echo "Term validation..."
    {{term_validator}} validate-data {{file}} -s {{schema_path}} -t ComorbidityAssociation --labels -c {{oak_config}}
    echo "Reference validation..."
    just fix-references-cache "{{file}}"
    {{ref_validator}} validate data {{file}} --schema {{schema_path}} --target-class ComorbidityAssociation --config {{ref_validator_config}}
    echo "✓ All validations passed for {{file}}"

# Full validation of one or more comorbidity files, batched by validator phase.
# This is intended for CI changed-file validation. Reference validation stays
# cache-bound (`--no-full-text`) so CI does not expand the reference cache or
# download PDFs.
[group('QC')]
validate-comorbidity-batch *files:
    #!/usr/bin/env bash
    set -u
    existing=()
    # Use real positional args rather than interpolating {{files}} as shell text.
    for f in "$@"; do
        if [[ "$f" == {{comorbidity_dir}}/*.yaml && -f "$f" ]]; then
            existing+=("$f")
        elif [[ ! -f "$f" ]]; then
            echo "Skipping deleted/missing file: $f"
        else
            echo "Skipping non-comorbidity file: $f"
        fi
    done
    if [ ${#existing[@]} -eq 0 ]; then
        echo "No existing comorbidity YAML files to validate."
        exit 0
    fi

    exit_code=0
    echo "Validating ${#existing[@]} comorbidity file(s) (batched)..."
    echo "Schema validation (batch)..."
    uv run linkml-validate --schema {{schema_path}} --target-class ComorbidityAssociation "${existing[@]}" || exit_code=1
    echo ""

    echo "Term validation (batch)..."
    {{term_validator}} validate-data "${existing[@]}" -s {{schema_path}} -t ComorbidityAssociation --labels -c {{oak_config}} || exit_code=1
    echo ""

    echo "Reference validation (batch)..."
    just fix-references-cache "${existing[@]}" || exit_code=1
    {{ref_validator}} validate data "${existing[@]}" --schema {{schema_path}} --target-class ComorbidityAssociation --config {{ref_validator_config}} --no-full-text || exit_code=1
    echo ""

    if [ $exit_code -ne 0 ]; then
        echo "✗ Validation failed for one or more comorbidity files (see above)"
        exit $exit_code
    fi
    echo "✓ All ${#existing[@]} comorbidity file(s) passed validation."

# Full validation of all comorbidity YAML files (schema + terms + references)
[group('QC')]
validate-comorbidities-all:
    #!/usr/bin/env bash
    shopt -s nullglob
    files=({{comorbidity_dir}}/*.yaml)
    if [ ${#files[@]} -eq 0 ]; then
        echo "No comorbidity files found in {{comorbidity_dir}}"
        exit 0
    fi
    just fix-references-cache "${files[@]}"
    just check-enum-cache-offline
    failed_files=()
    echo "Validating all comorbidity files..."
    for f in "${files[@]}"; do
        echo "=== $(basename $f) ==="
        errors=""
        # Schema validation
        if ! uv run linkml-validate --schema {{schema_path}} --target-class ComorbidityAssociation "$f" 2>&1 | grep -q "No issues found"; then
            errors+="  [SCHEMA] $(uv run linkml-validate --schema {{schema_path}} --target-class ComorbidityAssociation "$f" 2>&1 | grep -v "^$")\n"
        fi
        # Term validation
        term_output=$({{term_validator}} validate-data "$f" -s {{schema_path}} -t ComorbidityAssociation --labels -c {{oak_config}} 2>&1 || true)
        if ! echo "$term_output" | grep -q "Validation passed"; then
            errors+="  [TERMS] $term_output\n"
        fi
        # Reference validation
        ref_output=$({{ref_validator}} validate data "$f" --schema {{schema_path}} --target-class ComorbidityAssociation --config {{ref_validator_config}} 2>&1 || true)
        if echo "$ref_output" | grep -q "\[ERROR\]"; then
            errors+="  [REFERENCES]\n$(echo "$ref_output" | grep -A2 "\[ERROR\]")\n"
        elif ! echo "$ref_output" | grep -q "All validations passed"; then
            errors+="  [REFERENCES] $ref_output\n"
        fi
        if [ -n "$errors" ]; then
            failed_files+=("$f")
            echo -e "$errors"
        else
            # Surface the wrapper's affirmative snippet count (issue #7252):
            # without it this loop prints a wall of "✓ OK" that is
            # indistinguishable from having checked nothing.
            snippet_line=$(echo "$ref_output" | grep -o 'Snippets checked:.*' || true)
            echo "  ✓ OK${snippet_line:+ ($snippet_line)}"
        fi
    done
    echo ""
    echo "================================"
    if [ ${#failed_files[@]} -eq 0 ]; then
        echo "✓ All comorbidity files validated successfully!"
    else
        echo "✗ ${#failed_files[@]} comorbidity file(s) with errors:"
        for f in "${failed_files[@]}"; do
            echo "  - $f"
        done
        exit 1
    fi

# Validate all surrogate endpoint collection YAML files
[group('QC')]
validate-surrogate-endpoints:
    #!/usr/bin/env bash
    set -e
    shopt -s nullglob
    files=(kb/surrogate_endpoints/*.yaml)
    if [ ${#files[@]} -eq 0 ]; then
        echo "No surrogate endpoint collection files found."
        exit 0
    fi
    for f in "${files[@]}"; do
        echo "=== $(basename "$f") ==="
        uv run linkml-validate --schema {{schema_path}} --target-class FDASurrogateEndpointCollection "$f"
    done

# Validate all mechanism module YAML files (schema + terms + references)
[group('QC')]
validate-modules:
    #!/usr/bin/env bash
    shopt -s nullglob
    files=({{modules_dir}}/*.yaml)
    if [ ${#files[@]} -eq 0 ]; then
        echo "No module files found in {{modules_dir}}"
        exit 0
    fi
    just fix-references-cache "${files[@]}"
    just check-enum-cache-offline
    failed_files=()
    echo "Validating all mechanism module files..."
    for f in "${files[@]}"; do
        echo "=== $(basename $f) ==="
        errors=""
        # Schema validation (modules use the Disease class)
        if ! uv run linkml-validate --schema {{schema_path}} --target-class Disease "$f" 2>&1 | grep -q "No issues found"; then
            errors+="  [SCHEMA] $(uv run linkml-validate --schema {{schema_path}} --target-class Disease "$f" 2>&1 | grep -v "^$")\n"
        fi
        # Term validation
        term_output=$({{term_validator}} validate-data "$f" -s {{schema_path}} -t Disease --labels -c {{oak_config}} 2>&1)
        if ! echo "$term_output" | grep -q "Validation passed"; then
            errors+="  [TERMS] $term_output\n"
        fi
        # Reference validation
        ref_output=$({{ref_validator}} validate data "$f" --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}} 2>&1)
        if echo "$ref_output" | grep -q "\[ERROR\]"; then
            errors+="  [REFERENCES]\n$(echo "$ref_output" | grep -A2 "\[ERROR\]")\n"
        fi
        if [ -n "$errors" ]; then
            failed_files+=("$f")
            echo -e "$errors"
        else
            # Surface the wrapper's affirmative snippet count (issue #7252):
            # without it this loop prints a wall of "✓ OK" that is
            # indistinguishable from having checked nothing.
            snippet_line=$(echo "$ref_output" | grep -o 'Snippets checked:.*' || true)
            echo "  ✓ OK${snippet_line:+ ($snippet_line)}"
        fi
    done
    echo ""
    echo "================================"
    if [ ${#failed_files[@]} -eq 0 ]; then
        echo "✓ All module files validated successfully!"
    else
        echo "✗ ${#failed_files[@]} module file(s) with errors:"
        for f in "${failed_files[@]}"; do
            echo "  - $f"
        done
        exit 1
    fi

# Validate a single mechanism module file
# Skips `check-enum-cache` (whole-cache OAK re-derivation); see `validate`.
[group('QC')]
validate-module file:
    #!/usr/bin/env bash
    set -e
    echo "Schema validation..."
    uv run linkml-validate --schema {{schema_path}} --target-class Disease {{file}}
    echo "Term validation..."
    {{term_validator}} validate-data {{file}} -s {{schema_path}} -t Disease --labels -c {{oak_config}}
    echo "Reference validation..."
    just fix-references-cache "{{file}}"
    {{ref_validator}} validate data {{file}} --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}}
    echo "✓ All validations passed for {{file}}"

# Validate a single disease grouping file (schema + terms + references)
# Skips `check-enum-cache` (whole-cache OAK re-derivation); see `validate`.
[group('QC')]
validate-grouping file:
    #!/usr/bin/env bash
    set -e
    echo "Schema validation..."
    uv run linkml-validate --schema {{schema_path}} --target-class Grouping {{file}}
    echo "Term validation..."
    {{term_validator}} validate-data {{file}} -s {{schema_path}} -t Grouping --labels -c {{oak_config}}
    echo "Reference validation..."
    just fix-references-cache "{{file}}"
    {{ref_validator}} validate data {{file}} --schema {{schema_path}} --target-class Grouping --config {{ref_validator_config}}
    echo "✓ All validations passed for {{file}}"

# Validate all disease grouping files (schema + terms + references)
[group('QC')]
validate-groupings:
    #!/usr/bin/env bash
    shopt -s nullglob
    files=({{groupings_dir}}/*.yaml)
    if [ ${#files[@]} -eq 0 ]; then
        echo "No grouping files found in {{groupings_dir}}"
        exit 0
    fi
    just fix-references-cache "${files[@]}"
    just check-enum-cache-offline
    failed_files=()
    echo "Validating all disease grouping files..."
    for f in "${files[@]}"; do
        echo "=== $(basename $f) ==="
        errors=""
        # Schema validation (groupings use the Grouping class)
        if ! uv run linkml-validate --schema {{schema_path}} --target-class Grouping "$f" 2>&1 | grep -q "No issues found"; then
            errors+="  [SCHEMA] $(uv run linkml-validate --schema {{schema_path}} --target-class Grouping "$f" 2>&1 | grep -v "^$")\n"
        fi
        # Term validation
        term_output=$({{term_validator}} validate-data "$f" -s {{schema_path}} -t Grouping --labels -c {{oak_config}} 2>&1)
        if ! echo "$term_output" | grep -q "Validation passed"; then
            errors+="  [TERMS] $term_output\n"
        fi
        # Reference validation
        ref_output=$({{ref_validator}} validate data "$f" --schema {{schema_path}} --target-class Grouping --config {{ref_validator_config}} 2>&1)
        if echo "$ref_output" | grep -q "\[ERROR\]"; then
            errors+="  [REFERENCES]\n$(echo "$ref_output" | grep -A2 "\[ERROR\]")\n"
        fi
        if [ -n "$errors" ]; then
            failed_files+=("$f")
            echo -e "$errors"
        else
            # Surface the wrapper's affirmative snippet count (issue #7252):
            # without it this loop prints a wall of "✓ OK" that is
            # indistinguishable from having checked nothing.
            snippet_line=$(echo "$ref_output" | grep -o 'Snippets checked:.*' || true)
            echo "  ✓ OK${snippet_line:+ ($snippet_line)}"
        fi
    done
    echo ""
    echo "================================"
    if [ ${#failed_files[@]} -eq 0 ]; then
        echo "✓ All grouping files validated successfully!"
    else
        echo "✗ ${#failed_files[@]} grouping file(s) with errors:"
        for f in "${failed_files[@]}"; do
            echo "  - $f"
        done
        exit 1
    fi

# Lint and audit disease grouping membership criteria (structural + advisory).
# Structural lint is enforced in pytest; this report also evaluates whether
# listed members satisfy NECESSARY criteria (advisory — criteria may be
# aspirational). Pass a file to scope to one grouping; --strict to gate.
# Use `--overlaps` to report all pairwise disease-member overlaps.
[group('QC')]
check-groupings *args="":
    uv run python -m dismech.groupings {{args}}

# Run term validation on schema (checks dynamic enum definitions)
[group('QC')]
validate-terms-schema:
    @echo "Validating schema term references..."
    uv run linkml-term-validator validate-schema {{schema_path}} -c {{oak_config}}

# OAK config for ontology adapters
oak_config := "conf/oak_config.yaml"

# Run term validation on all data files (checks IDs exist and labels match)
# Uses linkml-term-validator with recursive binding validation
# Note: Requires local dev version from ../linkml-term-validator with recursive fix
[group('QC')]
validate-terms-all:
    #!/usr/bin/env bash
    set -e
    just check-enum-cache-offline
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}})
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    echo "Validating terms in ${#files[@]} disorder files (batched)..."
    {{term_validator}} validate-data "${files[@]}" -s {{schema_path}} -t Disease --labels -c {{oak_config}}

# Validate terms in a single file
# Skips `check-enum-cache` (whole-cache OAK re-derivation); see `validate`.
[group('QC')]
validate-terms file:
    {{term_validator}} validate-data {{file}} -s {{schema_path}} -t Disease --labels -c {{oak_config}}

# Run legacy custom term validation (faster, but less thorough)
[group('QC')]
validate-terms-legacy:
    uv run python scripts/validate_terms.py

# Validate causal graph integrity for all disorders
[group('QC')]
validate-graphs:
    uv run python -m dismech.graph --validate {{kb_dir}}

# Report graph-derived pathograph-wiring coverage (QC metrics): phenotype
# causal-connectivity (fraction of phenotype nodes reached by a causal edge) and
# gene-to-mechanism wiring (fraction of causal genes wired into a mechanism).
# Pass --list-unconnected to see floating phenotype / unwired gene names per file.
[group('QC')]
compliance-connectivity *ARGS:
    uv run python -m dismech.qc_plugins {{kb_dir}} -c conf/qc_config.yaml {{ARGS}}

# Validate dynamic enum membership caches against current schema definitions.
# Re-derives every dynamic enum from OAK, so it may pull large sqlite:obo:* DBs
# (run `just fetch-ontology-dbs` first in constrained environments).
[group('QC')]
check-enum-cache:
    uv run python -m dismech.enum_cache --schema {{schema_path}} --cache-dir cache --oak-config {{oak_config}}

# Offline structural check of the enum caches (no OAK / no downloads): catches
# stale files, malformed headers, and duplicate rows while trusting the
# committed cache/*.csv for membership. Use in network-constrained environments.
[group('QC')]
check-enum-cache-offline:
    uv run python -m dismech.enum_cache --schema {{schema_path}} --cache-dir cache --oak-config {{oak_config}} --offline

# Report non-canonical CURIE ordering in enum and ontology term caches.
# Phase 0 is advisory/read-only: warnings do not fail until the coordinated
# cache normalization cutover enables strict ordering.
[group('QC')]
check-cache-order:
    uv run python -m dismech.enum_cache --cache-dir cache --check-order

# Pre-provision the sqlite:obo:* ontology DBs (with resume/retry) that term
# validation needs, so a flaky/blocked download does not abort validation
# mid-run. Fetch all, or only the named ontologies:
#   just fetch-ontology-dbs
#   just fetch-ontology-dbs hgnc geno
[group('QC')]
fetch-ontology-dbs *names="":
    OAK_CONFIG={{oak_config}} bash scripts/fetch_ontology_dbs.sh {{names}}

# --- Curation stub queue (stubs/) ------------------------------------------
# The outstanding curation queue: one YAML per disease we intend to curate but
# have not. Anyone can add, re-prioritize, or retire a stub by pull request; a
# curation PR deletes the stub and adds the kb/ entry. See docs/curation-stubs.md.

# Gates only on a malformed file: unparseable YAML, a bad MONDO ID, a duplicate,
# a bad enum value. Staleness (the disease got curated elsewhere, the term was
# retired) is an advisory and never gates — stubs are informative, not curated
# content, and an unrelated curation PR must not turn stub PRs red.
# Check that each stub file is well formed
[group('Curation')]
check-stubs *args="":
    uv run dismech-stubs check {{args}}

# Deletes stubs whose disease has since been curated, and stubs naming a MONDO
# term that has since been retired. Leaves possible_kb_duplicate advisories
# alone — those are a judgement call between two MONDO IDs. Run periodically.
# Sweep stale stubs out of the queue (--apply to delete)
[group('Curation')]
tidy-stubs *args="":
    uv run dismech-stubs tidy {{args}}

# Schema-validate every stub file against the CurationStub class.
[group('Curation')]
validate-stubs:
    uv run linkml-validate -s src/dismech/schema/curation_stub.yaml -C CurationStub stubs/*.yaml

# Ordering is the hand-set priority band, then an arbitrary but stable spread —
# not a computed score. Pick one you know something about, not the first row.
# Show the next stub(s) to curate
[group('Curation')]
next-stubs count="5" *args="":
    uv run dismech-stubs next {{count}} {{args}}

# Summarize the queue by status, entry type, and priority.
[group('Curation')]
stub-stats:
    uv run dismech-stubs stats

# Fetch every open claim issue in one list-API call (immediately consistent,
# unlike a search) and write it where the other recipes can read it.
# Fetch the open curation claims
[group('Curation')]
fetch-claims out="tmp/claims.json":
    #!/usr/bin/env bash
    set -euo pipefail
    if ! command -v gh >/dev/null 2>&1; then
      echo "fetch-claims needs the gh CLI, which is not installed in this environment." >&2
      echo >&2
      echo "Claude Code web/remote sessions have no gh, and cannot reach api.github.com" >&2
      echo "directly either -- the agent proxy denies it even though GH_TOKEN is set." >&2
      echo "Use the GitHub MCP server instead: see 'No gh CLI (web and remote sessions)'" >&2
      echo "in .claude/skills/claim-disease/SKILL.md for the exact fallback, including" >&2
      echo "the minimal titles-only claims file that is enough to pick from." >&2
      exit 127
    fi
    mkdir -p "$(dirname {{out}})"
    gh issue list --repo monarch-initiative/dismech --label claim --state open \
      --json number,title,assignees,url,createdAt,closedByPullRequestsReferences \
      --limit 1000 > {{out}}
    echo "wrote {{out}}"

# Reports double-claims, claims with no MONDO ID in the title (they lock
# nothing), and stale claims — old with no PR. An open PR is never stale.
# Cross-check open claim issues against the stub queue
[group('Curation')]
check-claims claims="tmp/claims.json" *args="":
    uv run dismech-stubs claims {{claims}} {{args}}

# The two-phase pick: open claim issues, then the stub queue.
# Show the next unclaimed stub(s) to curate
[group('Curation')]
next-unclaimed count="5" claims="tmp/claims.json" *args="":
    uv run dismech-stubs next {{count}} --claims {{claims}} {{args}}

# Never overwrites an existing stub. Default source format is the Monarch
# rare-disease-identification prioritised list.
# Add stubs for nominated diseases that are neither curated nor already stubbed
[group('Curation')]
seed-stubs source *args="":
    uv run dismech-stubs seed {{source}} {{args}}

# Adds MONDO parents, subclass descendants (+ total), and causal genes to each
# stub, so the lump/split call can be made from the file. Needs the MONDO
# database (`just fetch-ontology-dbs mondo`). Idempotent; preserves hand edits.
# Add MONDO context to the stub files
[group('Curation')]
enrich-stubs *args="":
    uv run python scripts/enrich_curation_stubs.py {{args}}

# Run all QC checks (cache contracts + validation + modules + deep-research report checks)
[group('QC')]
qc: check-stubs check-duplicate-keys check-reference-cache-frontmatter check-term-cache-integrity check-not4curation check-folded-hyphens check-snippet-length check-title-snippets check-empty-snippets check-environmental-evidence validate-all validate-modules validate-groupings validate-synthesis-all qc-deep-research
    @echo "All QC checks passed!"

# Deep research QC: provider coverage + citation/reference coverage
[group('QC')]
qc-deep-research *args="":
    uv run python scripts/qc_deep_research.py {{args}}

# Strict deep research QC (non-zero on provider/ref coverage gaps)
[group('QC')]
qc-deep-research-strict:
    uv run python scripts/qc_deep_research.py \
      --fail-on-second-provider \
      --fail-on-missing-reference \
      --fail-on-unresolved-cache \
      --fail-on-holder-bucket

# Census of ECTO/XCO exposure_term coverage on environmental[] entries, with the
# pathograph-linked ones (influences_mechanisms) called out as the priority gap.
# Advisory by default; --strict exits non-zero on any linked-but-unbound entry.
# --format tsv writes a per-entry table carrying reuse candidates. See #8430.
[group('QC')]
environmental-term-audit *args="":
    uv run python scripts/environmental_exposure_term_audit.py {{args}}

# Analyze recommended field compliance for all disorder files
[group('QC')]
compliance-all:
    #!/usr/bin/env bash
    set -e
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}})
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    uv run linkml-data-qc "${files[@]}" -s {{schema_path}} -t Disease -f text

# Analyze compliance for a single file
[group('QC')]
compliance file:
    uv run linkml-data-qc {{file}} -s {{schema_path}} -t Disease -f text

# Generate compliance report as JSON
[group('QC')]
compliance-report:
    #!/usr/bin/env bash
    set -e
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}})
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    uv run linkml-data-qc "${files[@]}" -s {{schema_path}} -t Disease -f json -o compliance_report.json

# Generate compliance report as CSV
[group('QC')]
compliance-csv:
    #!/usr/bin/env bash
    set -e
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}})
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    uv run linkml-data-qc "${files[@]}" -s {{schema_path}} -t Disease -f csv -o compliance_report.csv

# Analyze compliance with config file (weighted scoring and thresholds)
[group('QC')]
compliance-weighted:
    #!/usr/bin/env bash
    set -e
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}})
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    uv run linkml-data-qc "${files[@]}" -s {{schema_path}} -t Disease -c conf/qc_config.yaml -f text

# Generate QC dashboard (HTML site with charts)
[group('QC')]
gen-dashboard:
    #!/usr/bin/env bash
    set -e
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}})
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    uv run linkml-data-qc "${files[@]}" -s {{schema_path}} -t Disease -c conf/qc_config.yaml --dashboard-dir dashboard/
    uv run python scripts/qc_uncurated_disease_links.py --kb-dir {{kb_dir}} --dashboard-dir dashboard/ --dashboard-index dashboard/index.html
    just gen-priority-dashboard
    echo "Dashboard generated in dashboard/"

# Generate MONDO curation priority dashboard
[group('QC')]
gen-priority-dashboard candidates='tmp/mondo_priority_candidates_full.tsv' config='conf/mondo_prioritizer.yaml':
    #!/usr/bin/env bash
    set -euo pipefail
    candidates="{{candidates}}"
    if [ "$candidates" = "tmp/mondo_priority_candidates_full.tsv" ] || [ ! -f "$candidates" ]; then
        mkdir -p "$(dirname "$candidates")"
        uv run python scripts/export_mondo_priority_candidates.py --mondo-db {{mondo_db}} --output "$candidates" --kb-dir {{kb_dir}}
    fi
    uv run python scripts/generate_priority_dashboard.py --candidates "$candidates" --kb-dir {{kb_dir}} --config {{config}} --dashboard-dir dashboard/ --dashboard-index dashboard/index.html
    echo "Priority dashboard generated in dashboard/"

# Generate a local-only all-MONDO priority dashboard under tmp/ (gitignored)
[group('QC')]
gen-priority-dashboard-all-mondo:
    #!/usr/bin/env bash
    set -e
    out_dir="tmp/priority-dashboard-all-mondo"
    mkdir -p "$out_dir"
    uv run python scripts/export_mondo_priority_candidates.py --mondo-db {{mondo_db}} --output "$out_dir"/all_mondo_candidates.tsv --kb-dir {{kb_dir}}
    uv run python scripts/generate_priority_dashboard.py --candidates "$out_dir"/all_mondo_candidates.tsv --kb-dir {{kb_dir}} --config conf/mondo_prioritizer.yaml --dashboard-dir "$out_dir" --dashboard-index "$out_dir"/index.html
    echo "Local-only all-MONDO priority dashboard generated at $out_dir/priority.html"
    echo "Outputs are under tmp/ and are gitignored; do not commit them."

# Reconcile Epic #1079 checkboxes against kb/disorders/ (root + has_subtypes + mondo_mappings).
# Marks curated diseases as [x] and updates per-section counts.
# Pass --dry-run to preview changes without writing to GitHub.
[group('Dashboard')]
sync-epic-checkboxes *args:
    uv run python scripts/sync_epic_checkboxes.py --kb-dir {{kb_dir}} {{args}}

# Validate snippet/reference pairs against PubMed (checks that quotes appear in cited papers)
# Note: First run fetches from PubMed and caches; subsequent runs use cache
# Note: linkml-reference-validator's "Total checks: 0" counts *issues found*, not
# checks performed (issue #7252) -- read the "Snippets checked: N/N verified"
# line the wrapper appends for the affirmative count.
[group('QC')]
validate-references file:
    @just fix-references-cache "{{file}}"
    {{ref_validator}} validate data {{file}} --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}}

# Count reference/snippet pairs and re-verify each against references_cache/,
# without running the (network-touching) validator. Advisory only: it reports
# "Snippets checked: N/N verified" and never gates. Pass --strict to exit 1 on a
# snippet that is not present in its cached reference text. See issue #7252.
[group('QC')]
count-verified-snippets *args:
    uv run python -m dismech.reference_snippet_audit --schema {{schema_path}} --config {{ref_validator_config}} {{args}}

# Deterministically validate reference cache frontmatter against the
# linkml-reference-validator cache contract before the heavier data validators.
[group('QC')]
check-reference-cache-frontmatter:
    uv run python -m dismech.reference_cache_frontmatter references_cache

# Catches the ad-hoc-seeding corruption in #7682: a row built by string
# concatenation whose label contains a comma parses to >3 fields and is
# silently truncated at that comma, and a later "repair" pass cements the
# truncation as clean-looking data that `just validate-terms` then reports as
# ontology truth. Also covers cache/enums/*.csv, the dynamic-enum membership
# caches, which stand in for an authority the same way. Structural facts only
# -- it does NOT re-derive labels from OAK, so `just validate-terms` remains
# the last line of defence. Runs in `qc` before the heavier data validators.
# Deterministically validate the structure of cache/*/terms.csv + enums (#7682).
[group('QC')]
check-term-cache-integrity:
    uv run python -m dismech.term_cache_integrity cache

# Guard against binding a term its own ontology flags `Not4Curation` (#8472).
# RGD ontologies (XCO and siblings) mark terms they keep for hierarchy but do
# not want annotated with a related synonym reading `Not4Curation`. That is a
# synonym, not an obsoletion axiom, so such a term exists, matches its label and
# is reachable from its enum roots -- it passes every check `just validate-terms`
# performs. Three reached the #8430 tranches on exactly that basis. Checks the
# prefixes with a LOCAL (sqlite:) adapter, which answer an alias query per term
# offline; OLS-served prefixes are reported as skipped rather than silently
# dropped (`--include-remote` opts in, at one network round trip per term).
# Also reports, as a non-gating note, flagged CURIEs sitting in cache/ but
# unused -- do NOT hand-delete those rows; the gate is the fix.
# Reject ontology bindings flagged Not4Curation by their own ontology (#8472).
[group('QC')]
check-not4curation *args:
    uv run python scripts/not4curation_audit.py "$@"

# Apply the candidate node-class tree across kb/ (the executable half of the
# pathograph node-classification design). `--format summary` reports coverage;
# `tsv` emits per-node assignments; `debundle` lists nodes whose own GO
# annotations span two classes -- each one a node making two claims; and
# `conformance` compares every conforms_to edge's two sides, which is an
# INDEPENDENT check on the classes because conforming pairs are curated as
# "same kind of thing" by an unrelated process. Conformance is gated on both
# sides being HIGH confidence by default -- letting the gene/CL/UBERON fallbacks
# in multiplies the mismatch rate several times over; pass --include-low to see
# the rest, or `--format conformance-gates` for the current rate under each gate.
# Design artifact -- nothing in kb/ or the schema depends on it.
[group('QC')]
node-class-scan *args:
    uv run python -m dismech.node_class_scan {{args}}

# Parse and check the compact pathograph node-class tree
# (docs/superpowers/pathograph_node_classes.txt). The tree is a DESIGN artifact
# -- nothing in kb/ or the schema depends on it -- but its leaves are real
# (node, disease) pairs, and a tree whose leaves have drifted from the KB is
# worse than no tree because it still looks grounded. Bare invocation checks the
# grammar only (instant); --verify-kb also resolves every cited leaf against
# kb/ (slow: parses the whole KB). --format yaml|json|text emits the tree,
# `text` being a stable round-trip of the compact form.
[group('QC')]
node-classes *args:
    uv run python -m dismech.node_classes {{args}}

# Guard against duplicated mapping keys anywhere in kb/ (#8623). PyYAML keeps
# the last value silently, so a duplicate is invisible to every test and
# renderer here, while the ruamel-based reference validator rejects the file
# outright. Duplicates arrive by MERGE -- two concurrent curation PRs adding the
# same block at different points in one file merge without a git conflict -- so
# this sweeps the whole KB rather than only the files a PR changed.
[group('QC')]
check-duplicate-keys *files:
    uv run python scripts/check_duplicate_yaml_keys.py "$@"

# Guard against NEW YAML folded-scalar compound-word splits in kb/ (e.g. a
# '>-' scalar line ending in 'relapsing-' folds to 'relapsing- remitting').
# A baseline grandfathers the pre-existing backlog; this fails only on new ones.
[group('QC')]
check-folded-hyphens:
    uv run python scripts/check_folded_hyphens.py

# Regenerate the folded-scalar hyphen baseline after intentionally changing the
# set (e.g. fixing backlog entries). Review the diff before committing.
[group('QC')]
update-folded-hyphen-baseline:
    uv run python scripts/check_folded_hyphens.py --update-baseline

# Guard against NEW degenerate evidence snippets in kb/ -- bare terms too short
# to carry a claim (e.g. snippet: 'Strabismus'), which support nothing and are
# usually lifted from a table that never survives text extraction (#7450).
# Pipe-delimited structured-source rows are exempt; the pre-existing backlog is
# grandfathered against origin/main (like CI), so this fails only on new ones.
# resolve_baseline() falls back to the committed baseline if origin/main is not
# present locally, so `just qc` and CI agree.
[group('QC')]
check-snippet-length:
    uv run python scripts/check_snippet_length.py --against-ref origin/main

# List every short snippet, baselined or not (triage view).
[group('QC')]
list-short-snippets:
    uv run python scripts/check_snippet_length.py --all

# Regenerate the short-snippet baseline after intentionally changing the set
# (e.g. fixing backlog entries). Review the diff before committing.
[group('QC')]
update-snippet-length-baseline:
    uv run python scripts/check_snippet_length.py --update-baseline

# Guard against NEW evidence-free `environmental:` exposures in kb/ --
# an entry with no `evidence:` block is an uncited causation claim that
# `just validate`/`validate-terms`/`count-verified-snippets` cannot see, since
# `evidence` is optional on the class (#8296). The pre-existing backlog is
# grandfathered against origin/main (like CI), so this fails only on new ones.
[group('QC')]
check-environmental-evidence:
    uv run python scripts/check_environmental_evidence.py --against-ref origin/main

# List every evidence-free `environmental:` exposure, baselined or not (triage view).
[group('QC')]
list-environmental-evidence-gaps:
    uv run python scripts/check_environmental_evidence.py --all

# Regenerate the environmental-evidence baseline after intentionally changing
# the backlog (e.g. citing exposures in a curation tranche). Review the diff.
[group('QC')]
update-environmental-evidence-baseline:
    uv run python scripts/check_environmental_evidence.py --update-baseline

# Guard against evidence snippets that merely quote the cited paper's title,
# which records that a question was examined rather than what was found (#8374).
# Grandfathered against origin/main the same way the length check is.
[group('QC')]
check-title-snippets:
    uv run python scripts/check_title_snippets.py --against-ref origin/main

# List every title-quoting snippet, baselined or not (triage view).
[group('QC')]
list-title-snippets:
    uv run python scripts/check_title_snippets.py --all

# Regenerate the title-snippet baseline after intentionally changing the set.
# Review the diff before committing.
[group('QC')]
update-title-snippet-baseline:
    uv run python scripts/check_title_snippets.py --update-baseline

# Guard against evidence items with an empty/whitespace-only `snippet`, which
# pass `linkml-reference-validator`/`count-verified-snippets` vacuously
# (#8550). `supports: NO_EVIDENCE` items are exempt (checked, not relevant --
# no baseline needed today, since the repo-wide backlog is zero).
[group('QC')]
check-empty-snippets:
    uv run python scripts/check_empty_snippets.py

# List every empty snippet, including NO_EVIDENCE-exempt ones (triage view).
[group('QC')]
list-empty-snippets:
    uv run python scripts/check_empty_snippets.py --all

# Validate ALL snippet/reference pairs across all disorder files.
# Warning: First run may take a while if references are not already cached.
[group('QC')]
validate-references-all:
    #!/usr/bin/env bash
    set -e
    if command -v rg >/dev/null 2>&1; then
        mapfile -t files < <(rg --files -g '*.yaml' -g '!*.history.yaml' --no-ignore {{kb_dir}} | sort)
    else
        mapfile -t files < <(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | sort)
    fi
    if [ ${#files[@]} -eq 0 ]; then
        echo "No disorder YAML files found in {{kb_dir}} (after excluding *.history.yaml)."
        exit 1
    fi
    just fix-references-cache "${files[@]}"
    echo "Validating references in ${#files[@]} disorder files (batched)..."
    {{ref_validator}} validate data "${files[@]}" --schema {{schema_path}} --target-class Disease --config {{ref_validator_config}}

# Fix YAML quoting issues in references cache (workaround for upstream bug).
# With data-file arguments, only normalize caches cited by those files. Omit
# arguments only for an explicit whole-cache maintenance pass (issues #7844,
# #8203). The quoting predicate is intentionally a no-op on valid bare CURIEs.
[group('QC')]
fix-references-cache *files:
    #!/usr/bin/env bash
    set -e
    uv run python -m dismech.reference_cache_quote references_cache "$@"

# Warm the reference cache's full-text-attempt state (stops repeated PDF
# re-downloads during `just validate`). Idempotent + resumable: only touches
# records that still lack `full_text_attempted`, so a bounded LIMIT drains the
# backlog incrementally and steady-state runs only warm newly-added references.
# LIMIT defaults to 0 (no cap); pass a number for a bounded/periodic sweep.
warm-reference-cache limit="0":
    uv run python scripts/warm_reference_cache.py --config {{ref_validator_config}} --limit {{limit}}

# Preview which reference-cache records the warm sweep would process, no network.
warm-reference-cache-preview limit="0":
    uv run python scripts/warm_reference_cache.py --config {{ref_validator_config}} --limit {{limit}} --dry-run

# Run browser search tests (JavaScript, uses Node.js + MiniSearch)
[group('QC')]
test-search:
    node --test tests/js/*.test.mjs

# Run dismech-curator browser-extension tests (pure Node, no dependencies)
[group('QC')]
test-extension:
    node extension/test/run.mjs

# Run pytest tests (with verbose output)
[group('QC')]
pytest-all:
    uv run pytest tests/ -v

# Run a quick validation test
[group('QC')]
quick-test:
    uv run pytest tests/test_data.py -v -k "test_schema_validity or test_disorder_count"

# List all disorders in the KB
[group('KB')]
list-disorders:
    @for f in {{kb_dir}}/*.yaml; do basename "$f" .yaml; done | sort

# Count disorders
[group('KB')]
count-disorders:
    @echo -n "Number of disorders: "
    @ls -1 {{kb_dir}}/*.yaml 2>/dev/null | wc -l

# Run ai-blame annotation on all disorder YAML files
[group('AI')]
ai-blame-annotate-all:
    #!/usr/bin/env bash
    set +e
    failures=0
    for f in {{kb_dir}}/*.yaml; do
        echo "Annotating: $f"
        if ! uvx ai-blame annotate "$f"; then
            echo "  ! Failed: $f"
            failures=$((failures + 1))
        fi
    done
    if [ "$failures" -gt 0 ]; then
        echo "Completed with $failures failures (ignored)."
    else
        echo "Completed without errors."
    fi

# Lint the schema
[group('QC')]
lint-schema:
    uv run linkml-lint {{schema_path}}

# Generate JSON Schema from LinkML
[group('Schema')]
gen-jsonschema:
    uv run gen-json-schema {{schema_path}} > project/jsonschema/dismech.json

# Generate documentation for the schema
[group('Schema')]
schema-doc:
    uv run gen-doc -d docs/schema {{schema_path}}

# Generate browser data.js from knowledge base
[group('Browser')]
gen-browser-data:
    uv run python -c "from pathlib import Path; from dismech.export import BrowserExporter; files=[p for p in sorted(Path('kb/disorders').glob('*.yaml')) if not p.name.endswith('.history.yaml')]; BrowserExporter().export_to_js(files, Path('app/data.js'))"

# Verify every page_url in app/data.js points at a rendered page (no dead links).
# data.js is always rebuilt from the whole KB while pages may build incrementally,
# so the two can drift apart — this is the gate that catches it (see PR #7903).
[group('Browser')]
check-browser-links:
    uv run python scripts/check_browser_data_links.py

# Generate discussions browser data.js from disorder + module discussions
[group('Browser')]
gen-discussions-data:
    uv run python -m dismech.export.discussions_export

# Generate computational-models browser data.js from disorder + module models
[group('Browser')]
gen-models-data:
    uv run python -m dismech.export.models_export

# Generate Mondo-keyed pathograph JSON artifact (for runtime embedding, e.g. Monarch pages)
[group('Browser')]
gen-pathographs:
    uv run python -m dismech.export.pathograph_export -i kb/disorders -o pathographs

# Serve the browser app locally
[group('Browser')]
serve-browser: gen-browser-data gen-discussions-data gen-models-data
    @echo "Starting local server at http://localhost:8000/app/"
    uv run python -m http.server 8000

# Deploy browser (generate data and open)
[group('Browser')]
deploy-browser: gen-browser-data
    @echo "Browser app ready at app/index.html"
    @echo "Data generated with $(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | wc -l | tr -d ' ') disorders"

# Generate individual HTML pages for all disorders, comorbidities, and modules
# (Grouping pages are intentionally excluded — they re-parse every disorder and
# are generated by their own, less-frequent workflow. Run `just gen-grouping-pages`
# explicitly, or `just gen-all` to include them locally.)
# Being a FULL build, this also prunes pages left behind by renamed/deleted
# entries (issue #7426); the incremental recipes below never prune.
[group('Pages')]
gen-pages:
    uv run python -m dismech.render --all
    @echo "Generated $(ls -1 pages/disorders/*.html 2>/dev/null | wc -l | tr -d ' ') disorder pages, $(ls -1 pages/comorbidities/*.html 2>/dev/null | wc -l | tr -d ' ') comorbidity pages, and $(ls -1 pages/modules/*.html 2>/dev/null | wc -l | tr -d ' ') module pages"

# Incremental page build (issue #5507): render only the given changed
# kb/disorders/*.yaml pages, plus the always-regenerated disorder-dependent
# aggregate/index pages (comorbidities, modules, classification pages). The
# expensive research pass runs only if a research report is among the args. Use
# ONLY when no global input (template, render.py, schema, styles) changed — those
# need a full `just gen-pages`. The generate-pages workflow's classifier decides.
[group('Pages')]
gen-pages-changed *files:
    uv run python -m dismech.render --changed {{files}}

# Incremental page build reading the changed paths from a newline-delimited file
# (robust to any characters in filenames). Used by the generate-pages workflow.
[group('Pages')]
gen-pages-changed-from file:
    uv run python -m dismech.render --changed-from {{file}}

# Generate a single disorder page
[group('Pages')]
gen-page file:
    uv run python -m dismech.render {{file}}

# Generate all shared module pages
[group('Pages')]
gen-module-pages:
    uv run python -m dismech.render --module {{modules_dir}}
    @echo "Generated $(ls -1 pages/modules/*.html 2>/dev/null | wc -l | tr -d ' ') module pages"

# Generate a single disease grouping page
[group('Pages')]
gen-grouping-page file:
    uv run python -m dismech.render --grouping {{file}}

# Generate all disease grouping pages
[group('Pages')]
gen-grouping-pages:
    uv run python -m dismech.render --grouping {{groupings_dir}}
    @echo "Generated $(ls -1 pages/groupings/*.html 2>/dev/null | wc -l | tr -d ' ') grouping pages"

# Generate deep-research index page plus a standalone page per report
[group('Pages')]
gen-research-index:
    uv run python -m dismech.render --research
    @echo "Generated pages/research/index.html and $(ls -1 pages/research/*.html 2>/dev/null | grep -v '/index.html$' | wc -l | tr -d ' ') per-report pages"

# Regenerate the deep-research provider table in details/index.html from the registry
[group('Pages')]
gen-provider-docs:
    uv run python -m dismech.render --provider-docs

# Generate a single comorbidity page
[group('Pages')]
gen-comorbidity-page file:
    uv run python -m dismech.render --comorbidity {{file}}

# Generate all comorbidity pages
[group('Pages')]
gen-comorbidity-pages:
    uv run python -m dismech.render --comorbidity {{comorbidity_dir}}

# Generate a single curation-project page
[group('Pages')]
gen-project-page file:
    uv run python -m dismech.render --project {{file}}

# Generate all curation-project pages plus the project index
[group('Pages')]
gen-project-pages:
    uv run python -m dismech.render --project projects
    @echo "Generated $(ls -1 pages/projects/*.html 2>/dev/null | wc -l | tr -d ' ') project pages"

# Generate the NIH funding-topic coverage summary page (pages/nih-topics/index.html)
[group('Pages')]
gen-nih-topics-page:
    uv run python scripts/gen_nih_topics_summary.py

# Generate static schema docs site via MkDocs (served at /elements/)
#
# SOURCE_DATE_EPOCH pins the build clock (reproducible-builds.org). Without it
# MkDocs stamps every page's `update_date` with *today*, which lands in
# elements/sitemap.xml as ~2,950 <lastmod> lines. elements/ is committed and
# `deploy-docs` fails the build unless a fresh render matches it byte for byte,
# so a date-stamped sitemap makes that check fail on every push made on a
# different day from the last regeneration — which is exactly what happened
# (red on main from 2026-08-03 onward, 3013 insertions / 3013 deletions).
#
# The value is an arbitrary fixed constant, not a real modification time. That
# loses nothing: MkDocs stamps every page with the *build* date, so `lastmod`
# never carried per-page modification info to begin with — it was uniformly
# wrong, and is now uniformly stable. Do not change it to something that varies
# (git commit time, `date`), or the check starts failing again.
[group('Pages')]
gen-schema-docs:
    just gen-doc
    # Normalize LinkML-generated mermaid cardinalities (e.g., "* _recommended_")
    # that break Mermaid v11 parsing in class diagrams.
    uv run python scripts/fix_schema_mermaid.py
    SOURCE_DATE_EPOCH=1735689600 uv run mkdocs build --clean
    @echo "Generated schema docs in elements/"

# Generate all pages and browser data
[group('Pages')]
gen-all: gen-browser-data gen-pathographs gen-discussions-data gen-models-data gen-pages gen-grouping-pages gen-project-pages gen-nih-topics-page gen-schema-docs
    @echo "Generated browser data, pathographs, disorder/comorbidity/grouping/project pages, and schema docs"

# ============== KGX Export ==============

# Generate derived disease-to-ontology context score tables
[group('Export')]
export-context-scores output_dir="output/context_scores":
    mkdir -p {{output_dir}}
    uv run dismech-context-scores -i {{kb_dir}} -o {{output_dir}}

# Generate KGX edges from disorder knowledge base.
# Emits three files: kgx_export_nodes.jsonl, kgx_export_edges.jsonl, and the
# SEPIO evidence sidecar kgx_export_sepio.jsonl (joins to the edges on `id`).
# See docs/sepio-export.md.
[group('Export')]
export-kgx:
    mkdir -p output/kgx
    uv run koza transform src/dismech/export/kgx_export.py -o output/kgx -f jsonl kb/disorders/*.yaml

# Project disorder YAMLs to a MONDO-anchored, HPOA-extended TSV plus a disease-disease comorbidity sidecar.
[group('Export')]
export-hpoa:
    uv run python -m dismech.export.hpoa_export --kb-dir kb/disorders --out-dir output/hpoa

# Export a flat CSV census of every disease + subtype and its MONDO mapping (or lack thereof).
[group('Export')]
export-disease-inventory output="output/disease_inventory.csv":
    uv run dismech-disease-inventory -i {{kb_dir}} -o {{output}}

# Generate a Mondo EMC (Externally Managed Content) TSV for downstream Mondo ingest.
# One row per disorder with a MONDO CURIE in disease_term.term.id; columns: mondo_id,
# mondo_label, dismech_url, dismech_definition, dismech_exact_synonyms, dismech_pmids.
# The output is committed to exports/mondo_emc.tsv so Mondo can pin to a release tag.
[group('Export')]
export-mondo-tsv output="exports/mondo_emc.tsv":
    uv run python -m dismech.export.mondo_emc_export --kb-dir {{kb_dir}} --output {{output}}

# ============== CX2 Export ==============

cx2_output_dir := "output/cx2"
ndex_test_host := "https://test.ndexbio.org"

# Export a single disorder pathograph to CX2 JSON for spot-checking.
# Examples:
#   just export-cx2 kb/disorders/Stargardt_Disease.yaml
#   just export-cx2 kb/disorders/Stargardt_Disease.yaml --dot-layout
[group('Export')]
export-cx2 file *args="":
    uv run dismech-cx2 {{file}} {{args}}

# Export all disorder pathographs to CX2 JSON files under output/cx2/.
# Examples:
#   just export-cx2-all
#   just export-cx2-all -o /tmp/cx2
#   just export-cx2-all --output /tmp/cx2 --dot-layout
[group('Export')]
export-cx2-all *args="":
    #!/usr/bin/env bash
    set -euo pipefail
    out_dir="{{cx2_output_dir}}"
    passthrough_args=()
    set -- {{args}}
    while (($#)); do
        case "$1" in
            -o|--output)
                if (($# < 2)); then
                    echo "Missing value for $1" >&2
                    exit 2
                fi
                out_dir="$2"
                shift 2
                ;;
            *)
                passthrough_args+=("$1")
                shift
                ;;
        esac
    done
    mkdir -p "$out_dir"
    shopt -s nullglob
    count=0
    skipped=0
    for f in {{kb_dir}}/*.yaml; do
        if [[ "$f" == *.history.yaml ]]; then
            continue
        fi
        stem="$(basename "$f" .yaml)"
        out="$out_dir/${stem}.cx2.json"
        echo "Exporting: $f -> $out"
        if [[ ${#passthrough_args[@]} -gt 0 ]]; then
            output=$(uv run dismech-cx2 "$f" -o "$out" --skip-empty "${passthrough_args[@]}" 2>&1) && status=0 || status=$?
        else
            output=$(uv run dismech-cx2 "$f" -o "$out" --skip-empty 2>&1) && status=0 || status=$?
        fi
        echo "$output"
        if [[ $status -ne 0 ]]; then
            exit $status
        fi
        if [[ "$output" == Skipping* ]]; then
            skipped=$((skipped + 1))
            continue
        fi
        count=$((count + 1))
    done
    echo "Exported $count CX2 network(s) to $out_dir/"
    if [[ $skipped -gt 0 ]]; then
        echo "Skipped $skipped disorder(s) with no pathograph edges"
    fi

# Upload a single disorder pathograph to the NDEx test server as a public network.
# Requires NDEX_USERNAME and NDEX_PASSWORD to be set.
# Examples:
#   just upload-cx2-test kb/disorders/Stargardt_Disease.yaml
#   just upload-cx2-test kb/disorders/Stargardt_Disease.yaml --dot-layout
[group('Export')]
upload-cx2-test file *args="":
    NDEX_HOST="${NDEX_TEST_HOST:-{{ndex_test_host}}}" uv run dismech-cx2 {{file}} --ndex-upload --ndex-replace-existing {{args}}

# Upload all disorder pathographs to the NDEx test server as public networks.
# Requires NDEX_USERNAME and NDEX_PASSWORD to be set.
# Examples:
#   just upload-cx2-test-all
#   just upload-cx2-test-all --dot-layout
[group('Export')]
upload-cx2-test-all *args="":
    #!/usr/bin/env bash
    set -euo pipefail
    : "${NDEX_USERNAME:?Set NDEX_USERNAME before running upload-cx2-test-all}"
    : "${NDEX_PASSWORD:?Set NDEX_PASSWORD before running upload-cx2-test-all}"
    export NDEX_HOST="${NDEX_TEST_HOST:-{{ndex_test_host}}}"
    shopt -s nullglob
    count=0
    skipped=0
    for f in {{kb_dir}}/*.yaml; do
        if [[ "$f" == *.history.yaml ]]; then
            continue
        fi
        echo "Uploading: $f -> $NDEX_HOST"
        output=$(uv run dismech-cx2 "$f" --ndex-upload --ndex-replace-existing --skip-empty {{args}} 2>&1) && status=0 || status=$?
        echo "$output"
        if [[ $status -ne 0 ]]; then
            exit $status
        fi
        if [[ "$output" == Skipping* ]]; then
            skipped=$((skipped + 1))
            continue
        fi
        count=$((count + 1))
    done
    echo "Uploaded $count CX2 network(s) to $NDEX_HOST"
    if [[ $skipped -gt 0 ]]; then
        echo "Skipped $skipped disorder(s) with no pathograph edges"
    fi

# ============== Deep Research ==============

# Directory for deep research outputs
research_dir := "research"
templates_dir := "templates"

# Reference validation applied to a deep-research report as it is generated
# (needs deep-research-client >= 0.2.10, which pulls in linkml-reference-validator
# through its `validation` extra -- the same library the KB validators use).
# Every PMID/DOI the report cites is resolved against PubMed/Crossref/DataCite,
# and every quote attributed to one of them is checked against that source. Since
# 0.2.10 each resolved reference is also weighed against the report's own
# characteristic vocabulary, flagging citations that exist but look off topic --
# free, since it re-reads records the existence check already fetched, and on by
# default (turn it off with `--validation-no-relevance`). An off-topic flag is a
# clue and not a verdict: it sets `needs_review` in the frontmatter but is
# deliberately NOT a confabulation and does NOT affect the exit code. The
# results are written into the report itself: a `## Reference Validation` section
# at the end of the body, and a `reference_validation:` summary in the YAML
# frontmatter. Lookups are cached into the same `references_cache/` the KB
# validators read, so a reference checked here does not need re-fetching when it
# is later cited from a `kb/` entry.
#
# The report is written to disk BEFORE validation runs, so a network failure
# during validation costs you the validation section, never the report.
#
# THEREFORE: a non-zero exit from a research recipe does NOT mean the research
# failed. Validation problems exit 3 with the report already saved. Do not re-run
# the provider (a falcon run is ~20 minutes and costs real money) -- recover with
#   just validate-research-reference <the report that was written>
#
# To skip it (quick iteration, or no network):
#   just dr_validation='' research-disorder falcon Marfan_Syndrome
dr_validation := "--validate-references --validation-cache-dir references_cache"

# Deep research to find public datasets (GEO/SRA/dbGaP/PRIDE/...) for a disorder.
# The report is a source of *candidate* accessions only: every accession it
# returns must be resolved against the repository API with
# `just verify-datasets --accession <acc>` before it is curated into a
# `datasets:` block. See `just discover-datasets` for the deterministic
# NCBI-search-based candidate generator that complements this.
# Examples:
#   just research-datasets openscientist Marfan_Syndrome
#   just research-datasets openscientist Asthma -- --param max_iterations=1
[group('Research')]
research-datasets provider disorder *args="":
    #!/usr/bin/env bash
    set -e
    mkdir -p {{research_dir}}/datasets
    yaml_file="{{kb_dir}}/{{disorder}}.yaml"
    if [ ! -f "$yaml_file" ]; then
        echo "Error: Disorder file not found: $yaml_file"
        exit 1
    fi
    disease_name=$(grep "^name:" "$yaml_file" | head -1 | sed 's/name: *//' | tr '_' ' ')
    category=$(grep "^category:" "$yaml_file" | head -1 | sed 's/category: *//' || echo "")
    mondo_id=$(grep -A3 "^disease_term:" "$yaml_file" | grep -o "MONDO:[0-9]*" | head -1 || echo "")
    output_file="{{research_dir}}/datasets/{{disorder}}-datasets-{{provider}}.md"
    echo "Dataset discovery: $disease_name ({{provider}}) -> $output_file"
    provider_arg=$([[ "{{provider}}" == "cborg" ]] && echo "--use-cborg" || echo "--provider {{provider}}")
    {{dr_client}} research \
        --template {{templates_dir}}/disease_datasets_research.md \
        --var "disease_name=$disease_name" \
        --var "mondo_id=$mondo_id" \
        --var "category=$category" \
        $provider_arg \
        --output "$output_file" \
        --separate-citations "$output_file.citations.md" \
        {{dr_validation}} \
        {{args}}

# Verify that datasets[].accession values resolve to real repository records.
# Nothing else in the validation stack checks dataset accessions, so run this
# before committing any new `datasets:` block.
# Examples:
#   just verify-datasets --all
#   just verify-datasets kb/disorders/Asthma.yaml
#   just verify-datasets --accession geo:GSE67472
[group('Research')]
verify-datasets *args="":
    @uv run python scripts/verify_dataset_accessions.py {{args}}

# Deterministically generate candidate datasets for a disorder by searching the
# NCBI GEO DataSets index (and optionally EBI repositories). Every candidate it
# emits is real by construction -- the metadata comes back from the repository.
# Examples:
#   just discover-datasets Asthma
#   just discover-datasets Asthma --limit 10 --json /tmp/asthma.json
[group('Research')]
discover-datasets disorder *args="":
    @uv run python scripts/discover_datasets.py {{disorder}} {{args}}

# Report which KB entries have no datasets yet (the dataset-curation worklist).
[group('Research')]
datasets-coverage *args="":
    @uv run python scripts/discover_datasets.py --coverage {{args}}

# Find EGA studies naming the disease in their own title. EGA holds the
# controlled-access human cohorts GEO cannot index.
#   just discover-ega --refresh
#   just discover-ega Cystic_Fibrosis
[group('Research')]
discover-ega *args="":
    @uv run python scripts/discover_ega.py {{args}}

# Find ArrayExpress NATIVE submissions (E-GEOD GEO re-imports are excluded:
# 73.6% of the collection, and curating them duplicates GEO accessions).
[group('Research')]
discover-arrayexpress *args="":
    @uv run python scripts/discover_arrayexpress.py {{args}}

# Find datasets via OmicsDI, restricted to repositories with no other route
# here (Metabolomics Workbench, MassIVE, dbGaP). 89% of OmicsDI duplicates
# sources already covered and is filtered out.
[group('Research')]
discover-omicsdi *args="":
    @uv run python scripts/discover_omicsdi.py {{args}}

# Find PRIDE (proteomics) and MetaboLights (metabolomics) datasets naming the
# disease in their own title. These assay types matter most for metabolic and
# rare disease, which transcriptomic archives cover poorly.
[group('Research')]
discover-ebi-omics *args="":
    @uv run python scripts/discover_ebi_omics.py {{args}}

# Deep research on a disorder using specified provider
# Examples:
#   just research-disorder perplexity Marfan_Syndrome
#   just research-disorder asta Liver_Cirrhosis
#   just research-disorder openai Huntingtons_Disease --model gpt-4o
#   just research-disorder cborg Crohn_Disease
#   just research-disorder claude_code Sarcoidosis   # no extra key; reuses Claude Code creds
[group('Research')]
research-disorder provider disorder *args="":
    #!/usr/bin/env bash
    set -e
    mkdir -p {{research_dir}}
    yaml_file="{{kb_dir}}/{{disorder}}.yaml"
    if [ ! -f "$yaml_file" ]; then
        echo "Error: Disorder file not found: $yaml_file"
        for f in {{kb_dir}}/*.yaml; do basename "$f" .yaml; done | sort | head -20
        exit 1
    fi
    disease_name=$(grep "^name:" "$yaml_file" | head -1 | sed 's/name: *//' | tr '_' ' ')
    category=$(grep "^category:" "$yaml_file" | head -1 | sed 's/category: *//' || echo "")
    output_file="{{research_dir}}/{{disorder}}-deep-research-{{provider}}.md"
    template_file=$([[ "{{provider}}" == "asta" ]] && echo "{{templates_dir}}/disease_pathophysiology_research_asta.md" || echo "{{templates_dir}}/disease_pathophysiology_research.md")
    echo "Researching: $disease_name ({{provider}}) -> $output_file"
    provider_arg=$([[ "{{provider}}" == "cborg" ]] && echo "--use-cborg" || echo "--provider {{provider}}")
    {{dr_client}} research \
        --template "$template_file" \
        --var "disease_name=$disease_name" \
        --var "mondo_id=" \
        --var "category=$category" \
        $provider_arg \
        --output "$output_file" \
        --separate-citations "$output_file.citations.md" \
        {{dr_validation}} \
        {{args}}

# Deep research on a shared mechanism module using specified provider
# Examples:
#   just research-module falcon meiotic_prophase_failure --param max_tokens=12000
[group('Research')]
research-module provider module *args="":
    #!/usr/bin/env bash
    set -e
    mkdir -p {{research_dir}}/modules
    yaml_file="{{modules_dir}}/{{module}}.yaml"
    if [ ! -f "$yaml_file" ]; then
        echo "Error: Module file not found: $yaml_file"
        for f in {{modules_dir}}/*.yaml; do basename "$f" .yaml; done | sort
        exit 1
    fi
    module_name=$(uv run python - "$yaml_file" <<'PY'
    import sys
    from pathlib import Path
    import yaml

    data = yaml.safe_load(Path(sys.argv[1]).read_text())
    print(data.get("name", ""))
    PY
    )
    category=$(uv run python - "$yaml_file" <<'PY'
    import sys
    from pathlib import Path
    import yaml

    data = yaml.safe_load(Path(sys.argv[1]).read_text())
    print(data.get("category", ""))
    PY
    )
    module_description=$(uv run python - "$yaml_file" <<'PY'
    import sys
    from pathlib import Path
    import yaml

    data = yaml.safe_load(Path(sys.argv[1]).read_text())
    print(" ".join(str(data.get("description", "")).split()))
    PY
    )
    pathophysiology_summary=$(uv run python - "$yaml_file" <<'PY'
    import sys
    from pathlib import Path
    import yaml

    data = yaml.safe_load(Path(sys.argv[1]).read_text())
    for node in data.get("pathophysiology") or []:
        name = node.get("name", "")
        desc = " ".join(str(node.get("description", "")).split())
        print(f"- {name}: {desc}")
    PY
    )
    output_file="{{research_dir}}/modules/{{module}}-deep-research-{{provider}}.md"
    template_file="{{templates_dir}}/module_mechanism_research.md"
    echo "Researching module: $module_name ({{provider}}) -> $output_file"
    provider_arg=$([[ "{{provider}}" == "cborg" ]] && echo "--use-cborg" || echo "--provider {{provider}}")
    {{dr_client}} research \
        --template "$template_file" \
        --var "module_name=$module_name" \
        --var "module_slug={{module}}" \
        --var "category=$category" \
        --var "module_description=$module_description" \
        --var "pathophysiology_summary=$pathophysiology_summary" \
        $provider_arg \
        --output "$output_file" \
        --separate-citations "$output_file.citations.md" \
        {{dr_validation}} \
        {{args}}

# Deep research on a comorbidity using specified provider
# Examples:
#   just research-comorbidity perplexity com_Type_2_Diabetes_Mellitus__Lichen_Simplex_Chronicus__Prurigo_Nodularis
#   just research-comorbidity openai com_Type_2_Diabetes_Mellitus__Lichen_Simplex_Chronicus__Prurigo_Nodularis --model gpt-4o
[group('Research')]
research-comorbidity provider comorbidity *args="":
	#!/usr/bin/env bash
	set -e
	mkdir -p {{research_dir}}
	yaml_file="{{comorbidity_dir}}/{{comorbidity}}.yaml"
	if [ ! -f "$yaml_file" ]; then
	    echo "Error: Comorbidity file not found: $yaml_file"
	    ls -1 {{comorbidity_dir}}/*.yaml | xargs -I {} basename {} .yaml | head -20
	    exit 1
	fi
	tmpfile="$(mktemp)"
	uv run python - <<-'PY' > "$tmpfile"
	import yaml
	from pathlib import Path

	data = yaml.safe_load(Path("{{comorbidity_dir}}/{{comorbidity}}.yaml").read_text())

	def fmt_label(d):
	    slug = d.get("slug")
	    if slug:
	        return slug.replace("_", " ")
	    comp = d.get("composition")
	    comps = d.get("components", []) or []
	    comp_slugs = [c.get("slug", "") for c in comps if c.get("slug")]
	    if comp and comp_slugs:
	        return f"{comp.title()} of " + ", ".join(comp_slugs)
	    return "UNKNOWN"

	disease_a = data.get("disease_a", {}) or {}
	disease_b = data.get("disease_b", {}) or {}

	disease_a_label = fmt_label(disease_a)
	disease_b_label = fmt_label(disease_b)

	disease_a_slug = disease_a.get("slug", "")
	disease_b_slug = disease_b.get("slug", "")

	components = disease_b.get("components", []) or []
	component_slugs = [c.get("slug", "") for c in components if c.get("slug")]
	disease_b_components = ", ".join(component_slugs)
	disease_b_composition = disease_b.get("composition", "")

	print("\\t".join([disease_a_label, disease_b_label, disease_a_slug, disease_b_slug, disease_b_components, disease_b_composition]))
	PY
	IFS=$'\\t' read -r disease_a_label disease_b_label disease_a_slug disease_b_slug disease_b_components disease_b_composition < "$tmpfile"
	rm -f "$tmpfile"
	output_file="{{research_dir}}/{{comorbidity}}-deep-research-{{provider}}.md"
	echo "Researching: $disease_a_label ↔ $disease_b_label ({{provider}}) -> $output_file"
	provider_arg=$([[ "{{provider}}" == "cborg" ]] && echo "--use-cborg" || echo "--provider {{provider}}")
	{{dr_client}} research \
	    --template {{templates_dir}}/comorbidity_deep_research.md.j2 \
	    --var "disease_a_label=$disease_a_label" \
	    --var "disease_b_label=$disease_b_label" \
	    --var "disease_a_slug=$disease_a_slug" \
	    --var "disease_b_slug=$disease_b_slug" \
	    --var "disease_b_components=$disease_b_components" \
	    --var "disease_b_composition=$disease_b_composition" \
	    $provider_arg \
	    --output "$output_file" \
	    --separate-citations "$output_file.citations.md" \
	    {{dr_validation}} \
	    {{args}}

# Deep research on Class A surrogacy evidence for a (disease, surrogate, clinical_outcome) triple.
# Asks the deep-research provider for trial-level R^2, PTE, STE, joint-model,
# regulatory qualification, and negative/refuting evidence linking the surrogate
# to the clinical outcome. Output mirrors research-disorder shape.
# Examples:
#   just research-surrogacy openscientist Chronic_Kidney_Disease "estimated glomerular filtration rate" "end-stage kidney disease"
#   just research-surrogacy perplexity Osteoporosis "bone mineral density" "vertebral fracture"
[group('Research')]
research-surrogacy provider disease surrogate clinical_outcome *args="":
	#!/usr/bin/env bash
	set -e
	mkdir -p {{research_dir}}/surrogacy
	yaml_file="{{kb_dir}}/{{disease}}.yaml"
	if [ ! -f "$yaml_file" ]; then
	    echo "Error: Disorder file not found: $yaml_file"
	    for f in {{kb_dir}}/*.yaml; do basename "$f" .yaml; done | sort | head -20
	    exit 1
	fi
	disease_name=$(grep "^name:" "$yaml_file" | head -1 | sed 's/name: *//' | tr '_' ' ')
	# Filename-safe slug from the surrogate label
	surrogate_slug=$(echo "{{surrogate}}" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/_/g; s/^_+|_+$//g' | cut -c1-60)
	output_file="{{research_dir}}/surrogacy/{{disease}}-surrogacy-${surrogate_slug}-deep-research-{{provider}}.md"
	echo "Researching surrogacy: $disease_name | {{surrogate}} -> {{clinical_outcome}} ({{provider}}) -> $output_file"
	provider_arg=$([[ "{{provider}}" == "cborg" ]] && echo "--use-cborg" || echo "--provider {{provider}}")
	{{dr_client}} research \
	    --template {{templates_dir}}/disease_surrogacy_research.md \
	    --var "disease_name=$disease_name" \
	    --var "surrogate={{surrogate}}" \
	    --var "clinical_outcome={{clinical_outcome}}" \
	    $provider_arg \
	    --output "$output_file" \
	    --separate-citations "$output_file.citations.md" \
	    {{dr_validation}} \
	    {{args}}

# Deep research on a disorder using cyberian with codex agent
[group('Research')]
research-disorder-cyberian-codex disorder *args="":
    #!/usr/bin/env bash
    set -e
    mkdir -p {{research_dir}}
    yaml_file="{{kb_dir}}/{{disorder}}.yaml"
    if [ ! -f "$yaml_file" ]; then
        echo "Error: Disorder file not found: $yaml_file"
        for f in {{kb_dir}}/*.yaml; do basename "$f" .yaml; done | sort | head -20
        exit 1
    fi
    disease_name=$(grep "^name:" "$yaml_file" | head -1 | sed 's/name: *//' | tr '_' ' ')
    category=$(grep "^category:" "$yaml_file" | head -1 | sed 's/category: *//' || echo "")
    output_file="{{research_dir}}/{{disorder}}-deep-research-cyberian-codex.md"
    echo "Researching: $disease_name (cyberian-codex) -> $output_file"
    {{dr_client}} research \
        --template {{templates_dir}}/disease_pathophysiology_research.md \
        --var "disease_name=$disease_name" \
        --var "mondo_id=" \
        --var "category=$category" \
        --provider cyberian \
        --param agent_type=codex \
        --output "$output_file" \
        --separate-citations "$output_file.citations.md" \
        {{dr_validation}} \
        {{args}}

# List available research providers
[group('Research')]
research-providers:
    {{dr_client}} providers

# Reference-check a deep-research report that already exists on disk -- the
# retro-fit counterpart of the `dr_validation` flags baked into the recipes
# above, for the reports generated before deep-research-client 0.2.9.
#
# Rewrites each report in place, replacing any previous `## Reference Validation`
# section, so it is safe to re-run. Lookups land in `references_cache/` like every
# other reference fetch.
#
# NOTE the asymmetry with generation-time validation: this adds the markdown
# section but NOT a `reference_validation:` frontmatter block. Upstream only
# *refreshes* a frontmatter summary that is already there, deliberately, so that
# a tool asked to check citations never reformats a file's frontmatter. On a
# retro-fitted report, read the section at the bottom.
#
# Examples:
#   just validate-research-reference research/Marfan_Syndrome-deep-research-falcon.md
#   # existence checks only, no quote checking (much faster on long bibliographies):
#   just validate-research-reference research/Foo-deep-research-falcon.md --no-check-quotes
#   # non-destructive preview to stdout, or JSON for tooling:
#   scripts/run_deep_research_client.sh validate-references research/Foo.md
#   scripts/run_deep_research_client.sh validate-references research/Foo.md --json out.json
#
# Accepts a glob, but prefer one report at a time, as you come to curate it: a
# tree-wide run rewrites ~1400 committed files and re-resolves tens of thousands
# of references against PubMed for reports nobody is reading today.
#
# Reference-check a deep-research report that already exists on disk.
[group('Research')]
validate-research-reference +args:
    {{dr_client}} validate-references \
        --cache-dir references_cache \
        --in-place \
        {{args}}

# Named Entity Confusion (NEC) preflight: verify a deep-research report is about
# the disease entity you intend to curate, by cross-checking the report's
# gene-mention frequencies and OMIM IDs against the MONDO term's canonical gene
# (issue #3889). Run this BEFORE using any DR content.
# Verdicts: PASS / WARN (contamination or OMIM mismatch) / FAIL (wrong entity —
# discard the report, do not cherry-pick) / SKIP (MONDO records no causal gene).
# Exits non-zero on FAIL, or on WARN too with --strict.
# Examples:
#   just preflight-dr research/Marfan_Syndrome-deep-research-falcon.md MONDO:0007947
#   just preflight-dr research/Foo-deep-research-falcon.md MONDO:0014572 --strict
[group('Research')]
preflight-dr report mondo *args="":
    uv run python -m dismech.preflight_dr "$1" "$2" {{args}}

# One TSV row per disorder summarizing deep-research provider coverage.
# Summary lines are prefixed with "#" so the table stays easy to grep/awk.
# Examples:
#   just research-status
#   just research-status --provider openscientist
#   just research-status --missing-provider openscientist
[group('Research')]
research-status *args="":
    @uv run python scripts/deep_research_coverage.py status {{args}}

# Launch deep research for every disorder missing the requested provider.
# Use provider slugs from deep-research-client, e.g. falcon or openscientist.
# Examples:
#   just research-missing-provider openscientist --dry-run
#   just research-missing-provider openscientist --max-disorders 5 -- --param max_iterations=1
[group('Research')]
research-missing-provider provider *args="":
    @uv run python scripts/deep_research_coverage.py run-missing {{provider}} {{args}}

# List hypothesis-search coverage for mechanistic_hypotheses in disorder YAML.
# Examples:
#   just research-hypotheses
#   just research-hypotheses --disorder Long_COVID
#   just research-hypotheses --missing-provider openscientist
[group('Research')]
research-hypotheses *args="":
    @uv run python scripts/hypothesis_deep_research.py list {{args}}

# Focused deep research on one mechanistic_hypotheses entry.
# Provider slugs follow deep-research-client; edison is accepted as an alias for falcon.
# Output: kb/hypotheses/<Disorder>/<hypothesis_group_id>/<provider>.md
# Examples:
#   just research-hypothesis openscientist Long_COVID canonical_persistence_immune_model --dry-run
#   just research-hypothesis falcon Long_COVID canonical_persistence_immune_model
#   just research-hypothesis openscientist Long_COVID canonical_persistence_immune_model -- --param max_iterations=1
[group('Research')]
research-hypothesis provider disorder hypothesis_group_id *args="":
    @uv run python scripts/hypothesis_deep_research.py run {{provider}} {{disorder}} {{hypothesis_group_id}} {{args}}

# Run hypothesis-search jobs for hypotheses missing a provider.
# Examples:
#   just research-hypotheses-missing-provider openscientist --disorder Long_COVID --dry-run
#   just research-hypotheses-missing-provider falcon --max-hypotheses 3
[group('Research')]
research-hypotheses-missing-provider provider *args="":
    @uv run python scripts/hypothesis_deep_research.py run-missing {{provider}} {{args}}

# Rehydrate an existing Edison trajectory into a full research report with its
# recovered artifacts and a separate citations file using deep-research-client.
#
# Example:
#   just rehydrate-edison-trajectory 784d73d5-da42-402e-9701-6c5b44beab14 \
#       research/Alcoholic_Liver_Disease-deep-research-falcon.md
[group('Research')]
rehydrate-edison-trajectory trajectory_id output_file:
    #!/usr/bin/env bash
    set -e
    export EDISON_API_KEY="${EDISON_API_KEY:-$(cat edison_tok 2>/dev/null || true)}"
    if [ -z "$EDISON_API_KEY" ]; then
        echo "Error: EDISON_API_KEY is not set and no edison_tok file found." >&2
        exit 1
    fi
    {{dr_client}} edison-trajectory "{{trajectory_id}}" \
        --output "{{output_file}}" \
        --separate-citations "{{output_file}}.citations.md"

# Legacy helper to backfill artifacts into an existing report file while keeping
# the current report body intact.
#
# Examples:
#   just fetch-research-artifacts 0ab9e2d2-7601-4bbe-ba01-e26bfce94cfd \
#       research/Dimethylglycine_Dehydrogenase_Deficiency-deep-research-falcon.md
#   just fetch-research-artifacts <trajectory_id> research/<Disorder>-deep-research-falcon.md
[group('Research')]
fetch-research-artifacts trajectory_id research_file:
    #!/usr/bin/env bash
    set -e
    export EDISON_API_KEY="${EDISON_API_KEY:-$(cat edison_tok 2>/dev/null || true)}"
    if [ -z "$EDISON_API_KEY" ]; then
        echo "Error: EDISON_API_KEY is not set and no edison_tok file found." >&2
        exit 1
    fi
    uv run python scripts/fetch_edison_artifacts.py "{{trajectory_id}}" "{{research_file}}"

# Build an index of all deep-research artifact files across the research/ directory.
# Produces research/artifact_index.yaml and warns about any filename collisions.
[group('Research')]
index-research-artifacts:
    uv run python scripts/index_research_artifacts.py

# Fetch and cache a reference by ID
# This may be a PMID, DOI, or other supported identifier
[group('Research')]
fetch-reference +identifiers:
    #!/usr/bin/env bash
    for identifier in {{identifiers}}; do
        echo "Fetching reference: $identifier"
        case "$identifier" in
            CIViC_EID:*|CIVIC_EID:*|civic_eid:*|CIViC_ASSERTION:*|CIVIC_ASSERTION:*|civic_assertion:*)
                if [ ! -f data/civic/accepted_assertion_summaries.tsv ] || [ ! -f data/civic/accepted_clinical_evidence_summaries.tsv ]; then
                    uv run python -m dismech.structured_sources.cli refresh civic
                fi
                uv run python -m dismech.structured_sources.cli rebuild civic --id "$identifier"
                ;;
            ICTRP:*|ictrp:*)
                uv run python -m dismech.structured_sources.cli rebuild ictrp --id "$identifier"
                ;;
            *)
                scripts/run_reference_validator.sh cache reference "$identifier"
                ;;
        esac
    done

# Tag top-level PublicationReference entries with authoritative-source labels
# (e.g. GeneReviews).  Detects GeneReviews PMIDs from local references_cache
# and writes `tags: [GeneReviews]` onto the matching reference entry.
# Run after adding new GeneReviews citations or to refresh all tags.
#   just tag-references                   # tag all disorder files
#   just tag-references --dry-run         # preview without writing
#   just tag-references kb/disorders/Noonan_Syndrome.yaml
[group('Curation')]
tag-references *args="":
    uv run python scripts/tag_references.py {{args}}

# Backfill missing publication titles on KB references and evidence items
# (`reference_title` on EvidenceItem, `title` on top-level PublicationReference).
# Titles are read verbatim from references_cache/ frontmatter — nothing is
# fabricated, and references with no cached title are reported, not guessed.
# Fetch any missing cache entry first with `just fetch-reference <ID>`.
#   just backfill-reference-titles                 # all of kb/
#   just backfill-reference-titles --dry-run       # preview without writing
#   just backfill-reference-titles --check         # exit 1 if any title is missing
#   just backfill-reference-titles kb/disorders/Asthma.yaml
[group('Curation')]
backfill-reference-titles *args="":
    uv run python scripts/backfill_reference_titles.py {{args}}

# Generate a COHD-based association_signals YAML block for a concept pair.
# Examples:
#   just cohd-signal --concept-a 436672 --concept-b 80502
#   just cohd-signal --query-a "disorder of copper metabolism" --query-b "osteoporosis" --show-candidates
[group('Research')]
cohd-signal *args="":
    uv run python scripts/cohd_pair_to_signal.py {{args}}

# Add a COHD association signal directly into a comorbidity YAML file.
# Examples:
#   just cohd-add-signal kb/comorbidities/com_Wilsons_Disease__Osteoporosis.yaml --concept-a 436672 --concept-b 80502 --replace-existing
#   just cohd-add-signal kb/comorbidities/com_Wilsons_Disease__Osteoporosis.yaml --query-a "disorder of copper metabolism" --query-b "osteoporosis" --show-candidates
[group('Research')]
cohd-add-signal file *args="":
    uv run python scripts/cohd_add_signal_to_comorbidity.py {{file}} {{args}}

# ============== Structured-database reference sources ==============
#
# Structured sources (e.g. Orphanet) ingest a knowledge base and emit
# deterministic, line-oriented markdown into references_cache/ so curators
# can cite individual rows as evidence snippets. See
# src/dismech/structured_sources/ for the framework and CLAUDE.md for usage.

# Refresh bulk Orphadata XML files (pinned by data/orphadata/MANIFEST.yaml)
[group('Research')]
refresh-orphadata:
    uv run python -m dismech.structured_sources.cli refresh orphanet

# Refresh ClinGen Gene-Disease Validity CSV (pinned by data/clingen/MANIFEST.yaml)
[group('Research')]
clingen-refresh:
    uv run python -m dismech.structured_sources.cli refresh clingen

# Refresh ClinGen Dosage Sensitivity TSV (pinned by data/clingen-dosage/MANIFEST.yaml)
[group('Research')]
clingen-dosage-refresh:
    uv run python -m dismech.structured_sources.cli refresh clingen-dosage

# Refresh CIViC accepted assertion/evidence TSVs (pinned by data/civic/MANIFEST.yaml)
[group('Research')]
civic-refresh:
    uv run python -m dismech.structured_sources.cli refresh civic

# Refresh curated gene-set GO interpretations + membership (pinned by data/genesets/MANIFEST.yaml)
[group('Research')]
genesets-refresh:
    uv run python -m dismech.structured_sources.cli refresh mygeneset

# Rebuild every references_cache/ORPHA_*.md from current bulk XML
# Use --id to limit to specific ORPHA codes.
[group('Research')]
structured-rebuild-orphanet *args="":
    uv run python -m dismech.structured_sources.cli rebuild orphanet {{args}}

# Rebuild every references_cache/CGGV_*.md from current ClinGen CSV
# Use --id to limit to specific CGGV assertion IDs.
[group('Research')]
clingen-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild clingen {{args}}

# Rebuild every references_cache/CGDS_*.md from current ClinGen Dosage TSV
# Use --id to limit to specific CGDS or HGNC identifiers.
[group('Research')]
clingen-dosage-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild clingen-dosage {{args}}

# Rebuild every references_cache/CIVIC_*.md from current CIViC TSVs
# Use --id to limit to specific CIVIC_EID or CIVIC_ASSERTION identifiers.
[group('Research')]
civic-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild civic {{args}}

# Rebuild every references_cache/MYGENESET_*.md from current interpretations + membership
# Use --id to limit to specific gene-set ids (e.g. KEGG_ASTHMA or MYGENESET:KEGG_ASTHMA).
[group('Research')]
genesets-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild mygeneset {{args}}

# List the first N gene-set identifiers available to ingest
[group('Research')]
genesets-list limit="50":
    uv run python -m dismech.structured_sources.cli list mygeneset --limit {{limit}}

# Align a gene set's curated BPs to a disorder's pathograph BPs (hierarchy-aware, role-weighted)
# e.g. `just genesets-align Asthma KEGG_ASTHMA`
[group('Research')]
genesets-align disease gene_set:
    uv run python -m dismech.structured_sources.cli align {{disease}} {{gene_set}}

# Align every disease-context gene set to its dismech disorder (by MONDO) — catalog-wide audit
[group('Research')]
genesets-align-all *args="":
    uv run python -m dismech.structured_sources.cli align-all {{args}}

# Refresh ICEES KG node/edge JSON-Lines (pinned by data/icees-kg/MANIFEST.yaml)
[group('Research')]
icees-refresh:
    uv run python -m dismech.structured_sources.cli refresh icees

# Pre-fetch raw IEMbase browse + per-disease JSON into data/iembase/ (gitignored).
[group('Research')]
iembase-prefetch *args="":
    uv run python scripts/fetch_iembase_diseases.py {{args}}

# Map cached IEMbase disease JSON to local DisMech disease/subtype entries.
[group('Research')]
iembase-map *args="":
    uv run python scripts/map_iembase_to_dismech.py {{args}}

# Rebuild every references_cache/ICEES_*.md from the current ICEES KG snapshot.
# Use --id to limit to a specific ICEES pair id or a "CURIE,CURIE" disease pair.
[group('Research')]
icees-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild icees {{args}}

# List the first N ICEES KG disease-pair identifiers
[group('Research')]
icees-list limit="20":
    uv run python -m dismech.structured_sources.cli list icees --limit {{limit}}

# Refresh STRchive loci JSON (pinned by data/strchive/MANIFEST.yaml)
[group('Research')]
strchive-refresh:
    uv run python -m dismech.structured_sources.cli refresh strchive

# Rebuild every references_cache/STRCHIVE_*.md from the current STRchive snapshot.
# Use --id STRCHIVE:<locus> (e.g. STRCHIVE:SCA3_ATXN3) to limit to one locus.
[group('Research')]
strchive-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild strchive {{args}}

# List the first N STRchive tandem-repeat locus identifiers
[group('Research')]
strchive-list limit="20":
    uv run python -m dismech.structured_sources.cli list strchive --limit {{limit}}
# Fetch WHO ICTRP trial registration record(s) into references_cache/.
# Covers every ICTRP primary registry (ChiCTR, ISRCTN, EUCTR, JPRN, CTRI, ...)
# so a non-ClinicalTrials.gov trial can be cited as ICTRP:<TrialID>.
#   just ictrp-fetch ChiCTR2100045397 ISRCTN67795930
[group('Research')]
ictrp-fetch +identifiers:
    #!/usr/bin/env bash
    set -euo pipefail
    for identifier in "$@"; do
        uv run python -m dismech.structured_sources.cli rebuild ictrp --id "$identifier"
    done

# Refresh every cached references_cache/ICTRP_*.md from the ICTRP portal.
# Use --id to restrict to specific trial identifiers.
[group('Research')]
ictrp-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild ictrp {{args}}

# List the trial identifiers already cached from WHO ICTRP
[group('Research')]
ictrp-list limit="20":
    uv run python -m dismech.structured_sources.cli list ictrp --limit {{limit}}

# Report non-ClinicalTrials.gov registry identifiers in the KB and whether each
# is citable as ICTRP:<TrialID>. Add --strict to fail on uncited identifiers.
[group('Research')]
ictrp-audit *args="":
    uv run python -m dismech.ictrp_audit {{args}}

# List the first N ClinGen Gene-Disease Validity assertion IDs
[group('Research')]
clingen-list limit="20":
    uv run python -m dismech.structured_sources.cli list clingen --limit {{limit}}

# List the first N ClinGen Dosage Sensitivity gene IDs
[group('Research')]
clingen-dosage-list limit="20":
    uv run python -m dismech.structured_sources.cli list clingen-dosage --limit {{limit}}

# Audit ClinGen Gene-Disease Validity coverage in disorder YAML
[group('Research')]
clingen-audit-yaml *args="":
    uv run python -m dismech.structured_sources.cli clingen-audit-yaml {{args}}

# List the first N identifiers from a structured source
[group('Research')]
structured-list source="orphanet" limit="20":
    uv run python -m dismech.structured_sources.cli list {{source}} --limit {{limit}}

# Ensure the OAK-managed NCIT SQLite is present and check pinned version
# (data/ncit-edges/MANIFEST.yaml). The .db is downloaded by OAK, never committed.
[group('Research')]
ncit-edges-refresh:
    uv run python -m dismech.structured_sources.cli refresh ncit

# Rebuild every references_cache/NCIT_*.md from selected NCIT predicate edges
# (NCIT:P302 Accepted_Therapeutic_Use_For). Use --id NCIT:Cxxxx to limit.
[group('Research')]
ncit-edges-rebuild *args="":
    uv run python -m dismech.structured_sources.cli rebuild ncit {{args}}

# List the first N NCIT subjects carrying a selected predicate edge
[group('Research')]
ncit-edges-list limit="20":
    uv run python -m dismech.structured_sources.cli list ncit --limit {{limit}}

# Audit NCIT P302 (Accepted_Therapeutic_Use_For) treatment-indication coverage
# against dismech disorders. Writes a TSV; --format summary for a digest.
[group('Research')]
ncit-p302-audit *args="":
    uv run python scripts/ncit_p302_audit.py {{args}}

# ============== Classification Schemas ==============

classifications_dir := "src/dismech/schema/classifications"

# Validate all classification schemas (checks ontology term meanings)
[group('QC')]
validate-classifications:
    #!/usr/bin/env bash
    set -e
    echo "Validating classification schemas..."
    for f in {{classifications_dir}}/*.yaml; do
        echo "Validating: $(basename $f)"
        uv run linkml-term-validator validate-schema "$f" -c {{oak_config}}
    done
    echo "✓ All classification schemas valid!"

# Validate a single classification schema
[group('QC')]
validate-classification file:
    uv run linkml-term-validator validate-schema {{file}} -c {{oak_config}}

# Semantic YAML diff between two git refs
# Example: just sdiff main my-branch --dir kb/disorders --summary
[group('QC')]
sdiff ref_old ref_new *args="":
    uv run python -m dismech.diff git {{ref_old}} {{ref_new}} {{args}}

# ============== Epic Issue Sync ==============

# Project files are in projects/ with ALL_CAPS names (e.g., CANCER.md, NTD.md)
projects_dir := "projects"
epic_sync_script := ".claude/skills/projman/scripts/sync_epic.py"

# Push markdown project to GitHub epic issue
# Example: just epic-push NTD
[group('Projects')]
epic-push project:
    python3 {{epic_sync_script}} push {{projects_dir}}/{{project}}.md

# Pull GitHub epic issue state to markdown
# Example: just epic-pull CANCER
[group('Projects')]
epic-pull project:
    python3 {{epic_sync_script}} pull {{projects_dir}}/{{project}}.md

# Show sync status between markdown and GitHub epic
# Example: just epic-status AUTOIMMUNE
[group('Projects')]
epic-status project:
    python3 {{epic_sync_script}} status {{projects_dir}}/{{project}}.md

# List all project files
[group('Projects')]
list-projects:
    @echo "Projects in {{projects_dir}}/:"
    @ls -1 {{projects_dir}}/*.md 2>/dev/null | xargs -I {} basename {} .md | sort

# ============== Embedding Analysis ==============

embed_dir := "cache/embeddings"

# Default groups for parent-based categorization (based on actual parent values in KB)
default_parent_groups := "Autoimmune Disease,Cardiovascular Disease,Gastrointestinal Disease,Neurological Disease,Neurodegenerative Disease,Respiratory Disease,Metabolic Disease,Bacterial Infection,Musculoskeletal Disease,Liver Disease"

# Index all disorders with embeddings (requires OPENAI_API_KEY)
# Install deps first: uv sync --group embeddings
[group('Analysis')]
embed-index recreate="":
    uv run python -m dismech.embed index --output {{embed_dir}} {{ if recreate != "" { "--recreate" } else { "" } }}

# Index with parent-based grouping (for visualization)
[group('Analysis')]
embed-index-grouped:
    uv run python -m dismech.embed index --output {{embed_dir}} --recreate \
        --group-by parents \
        --groups "{{default_parent_groups}}"

# Index with custom grouping
[group('Analysis')]
embed-index-custom group_by groups:
    uv run python -m dismech.embed index --output {{embed_dir}} --recreate \
        --group-by {{group_by}} \
        --groups "{{groups}}"

# Reindex all disorders (recreate from scratch)
[group('Analysis')]
embed-reindex:
    uv run python -m dismech.embed index --output {{embed_dir}} --recreate

# Semantic search for disorders matching a query
[group('Analysis')]
embed-search query space="pathophysiology":
    uv run python -m dismech.embed search "{{query}}" --space {{space}}

# Find disorders similar to a specific disorder
[group('Analysis')]
embed-similar disorder space="pathophysiology":
    uv run python -m dismech.embed similar "{{disorder}}" --space {{space}}

# Compare pathophysiology vs phenotype similarity correlation
[group('Analysis')]
embed-compare:
    uv run python -m dismech.embed compare --output {{embed_dir}}/correlation.json

# Export pathophysiology similarity matrix to CSV
[group('Analysis')]
embed-export:
    uv run python -m dismech.embed export --output {{embed_dir}}/patho_similarities.csv --space pathophysiology

# Export phenotype similarity matrix to CSV
[group('Analysis')]
embed-export-pheno:
    uv run python -m dismech.embed export --output {{embed_dir}}/pheno_similarities.csv --space phenotypes

# Export both similarity matrices
[group('Analysis')]
embed-export-all: embed-export embed-export-pheno
    @echo "Exported similarity matrices to {{embed_dir}}/"

# Interactive UMAP/TSNE plot with proper color coding (uses dismech.embed plotly)
# This handles categorical colors correctly unlike linkml-store's plot command
[group('Analysis')]
embed-plotly method="umap" color_field="_group":
    uv run python -m dismech.embed plotly \
        --space pathophysiology \
        --method {{method}} \
        --color-field {{color_field}} \
        --output {{embed_dir}}/patho_{{method}}_{{color_field}}.html
    @echo "Plot saved to {{embed_dir}}/patho_{{method}}_{{color_field}}.html"

# Interactive UMAP plot using linkml-store (has bug with categorical colors)
# Use color_field="_group" after running embed-index-grouped
[group('Analysis')]
embed-plot method="umap" color_field="_group":
    uv run linkml-store -d {{embed_dir}}/disorders.duckdb plot multi-collection-embeddings \
        -c pathophysiology \
        -i patho_index \
        -m {{method}} \
        --color-field {{color_field}} \
        --hover-fields name,_group,category,parents \
        --width 1400 \
        --height 1000 \
        --n-neighbors 15 \
        --limit-per-collection 500 \
        -o {{embed_dir}}/patho_{{method}}.html
    @echo "Plot saved to {{embed_dir}}/patho_{{method}}.html"

# Interactive phenotype space plot with proper color coding
[group('Analysis')]
embed-plotly-pheno method="umap" color_field="_group":
    uv run python -m dismech.embed plotly \
        --space phenotypes \
        --method {{method}} \
        --color-field {{color_field}} \
        --output {{embed_dir}}/pheno_{{method}}_{{color_field}}.html
    @echo "Plot saved to {{embed_dir}}/pheno_{{method}}_{{color_field}}.html"

# Interactive UMAP plot for phenotype space using linkml-store
[group('Analysis')]
embed-plot-pheno method="umap" color_field="_group":
    uv run linkml-store -d {{embed_dir}}/disorders.duckdb plot multi-collection-embeddings \
        -c phenotypes \
        -i pheno_index \
        -m {{method}} \
        --color-field {{color_field}} \
        --hover-fields name,_group,category \
        --width 1400 \
        --height 1000 \
        --n-neighbors 15 \
        --limit-per-collection 500 \
        -o {{embed_dir}}/pheno_{{method}}.html
    @echo "Plot saved to {{embed_dir}}/pheno_{{method}}.html"

# Plot both spaces side by side
[group('Analysis')]
embed-plot-both method="umap" color_field="_group":
    uv run linkml-store -d {{embed_dir}}/disorders.duckdb plot multi-collection-embeddings \
        -c pathophysiology,phenotypes \
        -m {{method}} \
        --color-field {{color_field}} \
        --hover-fields name,_group,category \
        --width 1600 \
        --height 1000 \
        --n-neighbors 15 \
        --limit-per-collection 500 \
        -o {{embed_dir}}/combined_{{method}}.html
    @echo "Plot saved to {{embed_dir}}/combined_{{method}}.html"

# Open the interactive plot in browser (uses the properly color-coded version)
[group('Analysis')]
embed-view color_field="_group":
    open {{embed_dir}}/patho_umap_{{color_field}}.html

# Generate data for the embedding explorer app (requires embeddings to be indexed first)
[group('Analysis')]
embed-app-data:
    uv run python -m dismech.embed app-data --output app/embeddings/data.js
    @echo "App data generated at app/embeddings/data.js"

# Open the embedding explorer app in browser
[group('Analysis')]
embed-app:
    open app/embeddings/index.html

# Serve the embedding explorer app locally (with live reload)
[group('Analysis')]
embed-serve:
    @echo "Starting local server at http://localhost:8001/app/embeddings/"
    uv run python -m http.server 8001

# Rebuild everything for the embedding explorer app (run when YAML files change)
# Requires OPENAI_API_KEY for embedding generation
[group('Analysis')]
embed-all:
    @echo "=== Rebuilding embedding explorer ==="
    @echo "Step 1: Re-indexing embeddings (this calls OpenAI API)..."
    just embed-index-grouped
    @echo "Step 2: Generating app data..."
    just embed-app-data
    @echo "=== Done! Open app/embeddings/index.html ==="

# Index individual pathophysiology mechanisms (for mechanism comparison browser)
[group('Analysis')]
embed-index-mechanisms:
    uv run python -m dismech.embed index-mechanisms --output {{embed_dir}} --recreate \
        --group-by parents \
        --groups "{{default_parent_groups}}"

# Export data for mechanisms comparison browser
[group('Analysis')]
embed-mechanisms-data:
    uv run python -m dismech.embed mechanisms-data --output app/embeddings/mechanisms_data.js

# Open mechanisms comparison browser
[group('Analysis')]
embed-mechanisms-app:
    @echo "Open app/embeddings/mechanisms.html in your browser"
    @echo "Or start server: just embed-serve"

# Rebuild mechanisms browser (index + export data)
[group('Analysis')]
embed-mechanisms-all:
    @echo "=== Building mechanism comparison browser ==="
    @echo "Step 1: Indexing individual mechanisms..."
    just embed-index-mechanisms
    @echo "Step 2: Generating browser data..."
    just embed-mechanisms-data
    @echo "=== Done! Open app/embeddings/mechanisms.html ==="

# ============== Reactome Pathways ==============

reactome_dir := "pathways/reactome"

# Fetch Reactome disease pathway data for a single disease
# Examples:
#   just reactome-fetch "cystic fibrosis"
#   just reactome-fetch DOID:13636
#   just reactome-fetch "chronic myeloid leukemia" --format md
[group('Reactome')]
reactome-fetch query *args="":
    uv run python scripts/fetch_reactome_disease.py "{{query}}" {{args}}

# Fetch Reactome data for all diseases overlapping with dismech KB
[group('Reactome')]
reactome-fetch-all:
    uv run python scripts/fetch_reactome_disease.py --all-overlap

# List cached Reactome disease files
[group('Reactome')]
reactome-list:
    @echo "Cached Reactome disease pathways:"
    @ls {{reactome_dir}}/*.yaml 2>/dev/null | grep -q . \
      && ls -1 {{reactome_dir}}/*.yaml | xargs -I {} basename {} .yaml | sort \
      || echo "  (none yet — run 'just reactome-fetch-all')"

# Show Reactome summary for a disease (prints to stdout)
[group('Reactome')]
reactome-show query:
    uv run python scripts/fetch_reactome_disease.py "{{query}}" --format md -o /dev/stdout

# Normalize all term and enum cache files for deterministic diffs
# Sorts term caches by CURIE (via linkml-term-validator migrate-cache)
# and sorts enum membership caches by CURIE.
# See: https://github.com/linkml/linkml-term-validator/issues/15
[group('QC')]
normalize-cache:
    #!/usr/bin/env bash
    set -e
    echo "Normalizing term caches..."
    uv run linkml-term-validator migrate-cache --cache-dir cache --sort-only
    echo "Normalizing enum caches..."
    mkdir -p tmp
    tmp_dir=$(mktemp -d tmp/dismech_enum_cache.XXXXXX)
    trap 'rm -rf "$tmp_dir"' EXIT
    for f in cache/enums/*.csv; do
        header=$(head -1 "$f")
        tmp="$tmp_dir/$(basename "$f")"
        tail -n+2 "$f" | grep -E '^[A-Za-z][A-Za-z0-9_.-]*:[A-Za-z0-9_./-]+$' | LC_ALL=C sort -u > "$tmp"
        echo "$header" > "$f"
        cat "$tmp" >> "$f"
    done
    echo "✓ All caches normalized"
# Compare dismech phenotypes against OMIM/Orphanet for a single disease
[group('Analysis')]
d2p-compare disease:
    uv run python -m dismech.compare.d2p compare "{{disease}}"

# Compare all diseases in the KB against OMIM/Orphanet
[group('Analysis')]
d2p-compare-all:
    uv run python -m dismech.compare.d2p compare-all

# Compare with JSON output
[group('Analysis')]
d2p-compare-json disease:
    uv run python -m dismech.compare.d2p compare "{{disease}}" --format json

# Audit one disease for source-backed phenotype gaps, evidence gaps, and pathograph-link gaps
[group('Analysis')]
d2p-audit disease:
    uv run python -m dismech.compare.d2p audit "{{disease}}"

# Audit genetic diseases for phenotype completeness; use ARGS for --limit/--audit-dir/--resume/--format/--output
[group('Analysis')]
d2p-audit-genetic *ARGS:
    uv run python -m dismech.compare.d2p audit-all --genetic-only {{ARGS}}

# Compare G2P gene assertions against dismech for a single gene
[group('Analysis')]
g2p-compare gene:
    uv run python -m dismech.compare.g2p compare "{{gene}}"

# Compare multiple G2P genes against dismech
[group('Analysis')]
g2p-compare-all *genes:
    uv run python -m dismech.compare.g2p compare-all {{genes}}

# Compare the full current G2P release against dismech
[group('Analysis')]
g2p-compare-release:
    uv run python -m dismech.compare.g2p compare-all --all-genes

# Export actionable row-level triage for the full current G2P release
[group('Analysis')]
g2p-compare-release-triage:
    uv run python -m dismech.compare.g2p compare-all --all-genes --format tsv --actionable-only

# Compare G2P with JSON output
[group('Analysis')]
g2p-compare-json gene:
    uv run python -m dismech.compare.g2p compare "{{gene}}" --format json

# Run causal perturbation analysis on a disorder
# Examples:
#   just perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --gene CASR --effect LoF
#   just perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --all
[group('Analysis')]
perturb file *args="":
    uv run python -m dismech.perturb {{file}} {{args}}

# Export dismech-perturb model configs as SED-ML / COMBINE archives, so any
# SED-ML-capable engine (COPASI, tellurium, VCell, runBioSimulations, ...) can
# run a dismech scenario. Writes exports/sedml/<model_id>/ (committed) and,
# with --omex, the zipped exports/sedml/<model_id>.omex (derived, gitignored).
# Examples:
#   just sedml-export
#   just sedml-export --id urate_homeostasis --omex
[group('Analysis')]
sedml-export *args="":
    uv run python -m dismech.perturb.sedml_export {{args}}

# Run every dismech-perturb scenario and persist the results (final observable
# values, fold change vs baseline, and the HP phenotypes the curated thresholds
# activate) to exports/model_runs/<model_id>.json. Derived artifact, committed
# so the disorder pages can render it; regenerate rather than hand-edit.
# Requires tellurium: uv pip install tellurium
[group('Analysis')]
gen-model-results *args="":
    uv run python -m dismech.perturb.results_export {{args}}

# Check the exported archives reproduce dismech-perturb's own numbers by
# running each .omex through tellurium's SED-ML interpreter and diffing.
# Requires tellurium: uv pip install tellurium
[group('Analysis')]
verify-sedml-export *args="":
    uv run python scripts/verify_sedml_export.py {{args}}

# ============== Agent Helper Commands ==============
# These commands help Claude Code agents explore the KB without requiring
# manual permission approvals for common lookup patterns.

# Check if a disorder exists (case-insensitive partial match)
# Example: just find-disorder kleefstra
[group('KB')]
find-disorder pattern:
    @for f in {{kb_dir}}/*.yaml; do basename "$f" .yaml; done | grep -i "{{pattern}}" || echo "No match found for '{{pattern}}'"

# Show how a specific YAML field is used across existing disorder files
# Example: just show-field-pattern genetic gene_term
#          just show-field-pattern treatments treatment_term
[group('KB')]
show-field-pattern section field:
    #!/usr/bin/env bash
    echo "Pattern for '{{field}}' in '{{section}}' section:"
    count=0
    for f in {{kb_dir}}/*.yaml; do
        # Extract lines from the target section (top-level key) then grep within it
        section_text=$(sed -n '/^{{section}}:/,/^[a-z_]*:/{ /^[a-z_]*:/!p; /^{{section}}:/p; }' "$f" 2>/dev/null)
        match=$(echo "$section_text" | grep -FA6 "{{field}}:" 2>/dev/null | head -7)
        if [ -n "$match" ]; then
            echo "--- $(basename $f) ---"
            echo "$match"
            echo ""
            count=$((count+1))
            if [ $count -ge 3 ]; then
                break
            fi
        fi
    done

# Find cached references matching a pattern (PMID, DOI, keyword)
# Example: just find-cached-refs kleefstra
#          just find-cached-refs 16826528
[group('Research')]
find-cached-refs pattern:
    @ls -1 references_cache/*.md 2>/dev/null | grep -i "{{pattern}}" || echo "No cached refs matching '{{pattern}}'"

# Check if deep research exists for a disorder
# Example: just check-research Kleefstra_Syndrome
[group('Research')]
check-research disorder:
    @ls -1 research/{{disorder}}* 2>/dev/null || echo "No research files found for '{{disorder}}'"

# List all available deep research files
[group('Research')]
list-research:
    @for f in research/*-deep-research-*.md; do [ -f "$f" ] && basename "$f"; done | grep -v '\.citations\.md$$' | sort || echo "No research files found"

# Generate a deterministic Europe PMC literature-scan packet for recent papers
[group('Research')]
literature-scan days='7' max_records='100':
    uv run python scripts/literature_scan.py --days {{days}} --max-records {{max_records}}

# Generate a deterministic Europe PMC mechanistic knowledge-gap scan packet
[group('Research')]
knowledge-gap-scan days='7' max_records='200':
    uv run python scripts/knowledge_gap_scan.py --days {{days}} --max-records {{max_records}}

# Generate a mechanistic knowledge-gap scan packet for an explicit publication-date range
[group('Research')]
knowledge-gap-scan-range date_from date_to max_records='200':
    uv run python scripts/knowledge_gap_scan.py --date-from {{date_from}} --date-to {{date_to}} --max-records {{max_records}}

# Generate a disorder review report (markdown + PDF) for expert review
# Example: just disorder-report kb/disorders/Kleefstra_Syndrome.yaml
# Output: Kleefstra_Syndrome_review.md and Kleefstra_Syndrome_review.pdf
[group('Pages')]
disorder-report file:
    #!/usr/bin/env bash
    set -e
    mkdir -p reports
    stem=$(basename "{{file}}" .yaml)
    md_out="reports/${stem}_review.md"
    pdf_out="reports/${stem}_review.pdf"
    echo "Generating review report for {{file}}..."
    uv run python scripts/render_review_pdf.py "{{file}}" --md-only -o "$md_out"
    echo "  Markdown: $md_out"
    if command -v pandoc >/dev/null 2>&1; then
        pandoc "$md_out" -o "$pdf_out" --pdf-engine=xelatex \
            -V geometry:margin=2.5cm -V geometry:bottom=3cm -V fontsize=11pt \
            -V mainfont="Palatino" -V monofont="Menlo" \
            --include-in-header=scripts/pdf_header.tex 2>/dev/null
        echo "  PDF: $pdf_out"
    else
        echo "  (pandoc not found — skipping PDF generation)"
    fi

# ============== Scheduled-workflow cron profiles ==============

# List the available cron cadence profiles and show the active one.
[group('Cron profiles')]
cron-profiles:
    uv run python scripts/apply_cron_profile.py --list

# Show what a profile would change without writing anything.
# Example: just cron-profile-preview fast
[group('Cron profiles')]
cron-profile-preview name:
    uv run python scripts/apply_cron_profile.py {{name}} --dry-run

# Apply a cron cadence profile to the scheduled workflows and commit.
# Example: just cron-profile slow
[group('Cron profiles')]
cron-profile name:
    uv run python scripts/apply_cron_profile.py {{name}}

# ============== Deterministic PR auto-merge (pr-shepherd closing step) ==============

# Report which open PRs the pr-shepherd auto-merge sweep would squash-merge:
# approved, unassigned, conflict-free, green, and older than `days`.
# Example: just auto-merge-preview 3
[group('Auto-merge')]
auto-merge-preview days='3':
    uv run --no-project python scripts/auto_merge_ready_prs.py \
        --repo "$(gh repo view --json nameWithOwner -q .nameWithOwner)" \
        --min-age-days {{days}} --dry-run

# ============== Phenoagent: case-to-disease matching ==============

# Step 1 - Deterministic init: build an initial matching YAML from a phenopacket
# and a single dismech disease (slug, MONDO id, name, or YAML path).
# Example: just matching-init tests/phenoagent/data/phenopackets/PMID_35451551_proband.min.json Fanconi_Anemia
[group('Phenoagent')]
matching-init phenopacket disease *flags:
    uv run python -m phenoagent.matching_cli {{phenopacket}} {{disease}} {{flags}}

# Step 2 - Agentic explanation loop: run init, then drive cyberian + Claude to
# fill explanations for every non-exact row (requires cyberian + a running agent
# server on --host/--port). Add --dry-run to print the cyberian command only.
# Example: just matching-agent tests/phenoagent/data/phenopackets/PMID_35451551_proband.min.json Fanconi_Anemia --dry-run
[group('Phenoagent')]
matching-agent phenopacket disease *flags:
    uv run python -m phenoagent.cyberian_wrapper {{phenopacket}} {{disease}} {{flags}}

# Step 3 - Match-aware causal graph: render an HTML report (embedded Mermaid +
# metadata) from a dismech disease model and a matching report YAML.
# Example: just matching-graph Fanconi_Anemia output/matching/<case>__Fanconi_Anemia.yaml
[group('Phenoagent')]
matching-graph disease matching_report *flags:
    uv run python -m phenoagent.match_graph {{disease}} {{matching_report}} {{flags}}

# Step 4 - Deterministic phenopacket match-quality eval against dismech disorders.
# Defaults to the bundled fixtures; pass a phenopacket-store checkout to scale up.
# Example: just phenopacket-eval
# Example: just phenopacket-eval projects/PHENOPACKETS/files/phenopacket-store
[group('Phenoagent')]
phenopacket-eval paths="tests/phenoagent/data/phenopackets":
    uv run python -m phenoagent.eval {{paths}} --json workdirs/eval/phenopacket-eval.json --markdown workdirs/eval/phenopacket-eval.md
