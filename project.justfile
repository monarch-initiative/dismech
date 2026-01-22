## Add your own just recipes here. This is imported by the main justfile.

# Default schema path
schema_path := "src/dismech/schema/dismech.yaml"
kb_dir := "kb/disorders"

# Validate all disorder YAML files (schema + terms + references)
# Runs all validations and reports ALL errors at the end
[group('QC')]
validate-all:
    #!/usr/bin/env bash
    just fix-references-cache
    failed_files=()
    echo "Validating all disorder files..."
    for f in {{kb_dir}}/*.yaml; do
        echo "=== $(basename $f) ==="
        errors=""
        # Schema validation
        if ! uv run linkml-validate --schema {{schema_path}} --target-class Disease "$f" 2>&1 | grep -q "No issues found"; then
            errors+="  [SCHEMA] $(uv run linkml-validate --schema {{schema_path}} --target-class Disease "$f" 2>&1 | grep -v "^$")\n"
        fi
        # Term validation
        term_output=$(uv run linkml-term-validator validate-data "$f" -s {{schema_path}} -t Disease --labels -c {{oak_config}} 2>&1)
        if ! echo "$term_output" | grep -q "Validation passed"; then
            errors+="  [TERMS] $term_output\n"
        fi
        # Reference validation
        ref_output=$(uv run linkml-reference-validator validate data "$f" --schema {{schema_path}} --target-class Disease 2>&1)
        if echo "$ref_output" | grep -q "\[ERROR\]"; then
            errors+="  [REFERENCES]\n$(echo "$ref_output" | grep -A2 "\[ERROR\]")\n"
        fi
        if [ -n "$errors" ]; then
            failed_files+=("$f")
            echo -e "$errors"
        else
            echo "  ✓ OK"
        fi
    done
    echo ""
    echo "================================"
    if [ ${#failed_files[@]} -eq 0 ]; then
        echo "✓ All files validated successfully!"
    else
        echo "✗ ${#failed_files[@]} file(s) with errors:"
        for f in "${failed_files[@]}"; do
            echo "  - $f"
        done
        exit 1
    fi

# Full validation of a single disorder file (schema + terms + references)
[group('QC')]
validate file:
    #!/usr/bin/env bash
    set -e
    echo "Schema validation..."
    uv run linkml-validate --schema {{schema_path}} --target-class Disease {{file}}
    echo "Term validation..."
    uv run linkml-term-validator validate-data {{file}} -s {{schema_path}} -t Disease --labels --no-dynamic-enums -c {{oak_config}}
    echo "Reference validation..."
    just fix-references-cache
    uv run linkml-reference-validator validate data {{file}} --schema {{schema_path}} --target-class Disease
    echo "✓ All validations passed for {{file}}"

# Schema-only validation (fast, structure check)
[group('QC')]
validate-schema file:
    uv run linkml-validate --schema {{schema_path}} --target-class Disease {{file}}

# Schema validation for all files
[group('QC')]
validate-schema-all:
    #!/usr/bin/env bash
    set -e
    for f in {{kb_dir}}/*.yaml; do
        echo "Validating: $f"
        uv run linkml-validate --schema {{schema_path}} --target-class Disease "$f"
    done

# Run term validation on schema (checks dynamic enum definitions)
[group('QC')]
validate-terms-schema:
    @echo "Validating schema term references..."
    uv run linkml-term-validator validate-schema {{schema_path}}

# OAK config for ontology adapters
oak_config := "conf/oak_config.yaml"

# Run term validation on all data files (checks IDs exist and labels match)
# Uses linkml-term-validator with recursive binding validation
# Note: Requires local dev version from ../linkml-term-validator with recursive fix
[group('QC')]
validate-terms-all:
    #!/usr/bin/env bash
    set -e
    echo "Validating terms in all disorder files..."
    for f in {{kb_dir}}/*.yaml; do
        echo "Validating: $(basename $f)"
        uv run linkml-term-validator validate-data "$f" -s {{schema_path}} -t Disease --labels -c {{oak_config}}
    done
    echo "✓ All terms valid!"

# Validate terms in a single file
[group('QC')]
validate-terms file:
    uv run linkml-term-validator validate-data {{file}} -s {{schema_path}} -t Disease --labels -c {{oak_config}}

# Run legacy custom term validation (faster, but less thorough)
[group('QC')]
validate-terms-legacy:
    uv run python scripts/validate_terms.py

# Validate causal graph integrity for all disorders
[group('QC')]
validate-graphs:
    uv run python -m dismech.graph --validate {{kb_dir}}

# Run all QC checks (full validation on all files)
[group('QC')]
qc: validate-all
    @echo "All QC checks passed!"

# Analyze recommended field compliance for all disorder files
[group('QC')]
compliance-all:
    uv run linkml-data-qc {{kb_dir}} -s {{schema_path}} -t Disease -f text

# Analyze compliance for a single file
[group('QC')]
compliance file:
    uv run linkml-data-qc {{file}} -s {{schema_path}} -t Disease -f text

# Generate compliance report as JSON
[group('QC')]
compliance-report:
    uv run linkml-data-qc {{kb_dir}} -s {{schema_path}} -t Disease -f json -o compliance_report.json

# Generate compliance report as CSV
[group('QC')]
compliance-csv:
    uv run linkml-data-qc {{kb_dir}} -s {{schema_path}} -t Disease -f csv -o compliance_report.csv

# Analyze compliance with config file (weighted scoring and thresholds)
[group('QC')]
compliance-weighted:
    uv run linkml-data-qc {{kb_dir}} -s {{schema_path}} -t Disease -c conf/qc_config.yaml -f text

# Generate QC dashboard (HTML site with charts)
[group('QC')]
gen-dashboard:
    uv run linkml-data-qc {{kb_dir}} -s {{schema_path}} -t Disease -c conf/qc_config.yaml --dashboard-dir dashboard/
    @echo "Dashboard generated in dashboard/"

# Validate snippet/reference pairs against PubMed (checks that quotes appear in cited papers)
# Note: First run fetches from PubMed and caches; subsequent runs use cache
[group('QC')]
validate-references file:
    @just fix-references-cache
    uv run linkml-reference-validator validate data {{file}} --schema {{schema_path}} --target-class Disease

# Validate ALL snippet/reference pairs against PubMed across all disorder files
# Warning: First run may take a while as it fetches ~1400 uncached PMIDs from PubMed
[group('QC')]
validate-references-all:
    #!/usr/bin/env bash
    set -e
    just fix-references-cache
    echo "Validating references in all disorder files..."
    total_errors=0
    for f in {{kb_dir}}/*.yaml; do
        echo "Checking: $f"
        if ! uv run linkml-reference-validator validate data "$f" --schema {{schema_path}} --target-class Disease 2>&1 | grep -q "All validations passed"; then
            errors=$(uv run linkml-reference-validator validate data "$f" --schema {{schema_path}} --target-class Disease 2>&1 | grep -c "ERROR" || true)
            if [ "$errors" -gt 0 ]; then
                echo "  Found $errors errors in $f"
                total_errors=$((total_errors + errors))
            fi
        fi
    done
    if [ $total_errors -eq 0 ]; then
        echo "All reference validations passed!"
    else
        echo "Total reference validation errors: $total_errors"
        exit 1
    fi

# Fix YAML quoting issues in references cache (workaround for upstream bug)
[group('QC')]
fix-references-cache:
    #!/usr/bin/env python3
    import re
    from pathlib import Path
    cache_dir = Path("references_cache")
    if not cache_dir.exists():
        exit(0)
    for md_file in cache_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
        frontmatter, body = parts[1], parts[2]
        lines, new_lines, modified = frontmatter.split("\n"), [], False
        for line in lines:
            if not line.strip() or line.strip().startswith("-"):
                new_lines.append(line)
                continue
            match = re.match(r'^(\s*)([a-z_]+):\s+(.+)$', line, re.IGNORECASE)
            if match:
                indent, key, value = match.groups()
                needs_quoting = any(c in value or value.startswith(c) for c in [':', '[', '{', '*', '&', '!', '@', '#'])
                is_quoted = value.startswith('"') or value.startswith("'")
                if needs_quoting and not is_quoted:
                    new_lines.append(f'{indent}{key}: "{value.replace(chr(34), chr(92)+chr(34))}"')
                    modified = True
                    continue
            new_lines.append(line)
        if modified:
            md_file.write_text(f"---{chr(10).join(new_lines)}---{body}", encoding="utf-8")

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
    @echo "Disorders in the KB:"
    @ls -1 {{kb_dir}}/*.yaml | xargs -I {} basename {} .yaml | sort

# Count disorders
[group('KB')]
count-disorders:
    @echo -n "Number of disorders: "
    @ls -1 {{kb_dir}}/*.yaml 2>/dev/null | wc -l

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
    uv run python -c "from pathlib import Path; from dismech.export import BrowserExporter; BrowserExporter().export_to_js(sorted(Path('kb/disorders').glob('*.yaml')), Path('app/data.js'))"

# Serve the browser app locally
[group('Browser')]
serve-browser: gen-browser-data
    @echo "Starting local server at http://localhost:8000/app/"
    uv run python -m http.server 8000

# Deploy browser (generate data and open)
[group('Browser')]
deploy-browser: gen-browser-data
    @echo "Browser app ready at app/index.html"
    @echo "Data generated with $(ls -1 {{kb_dir}}/*.yaml | wc -l | tr -d ' ') disorders"

# Generate individual HTML pages for all disorders
[group('Pages')]
gen-pages:
    uv run python -m dismech.render --all

# Generate a single disorder page
[group('Pages')]
gen-page file:
    uv run python -m dismech.render {{file}}

# Generate all pages and browser data
[group('Pages')]
gen-all: gen-browser-data gen-pages
    @echo "Generated browser and $(ls -1 pages/disorders/*.html | wc -l | tr -d ' ') disorder pages"

# ============== KGX Export ==============

# Generate KGX edges from disorder knowledge base
[group('Export')]
export-kgx:
    mkdir -p output/kgx
    uv run koza transform src/dismech/export/kgx_export.py -i 'kb/disorders/*.yaml' -o output/kgx -f jsonl

# ============== Deep Research ==============

# Directory for deep research outputs
research_dir := "research"
templates_dir := "templates"

# Deep research on a disorder using specified provider
# Examples:
#   just research-disorder perplexity Marfan_Syndrome
#   just research-disorder openai Huntingtons_Disease --model gpt-4o
#   just research-disorder cborg Crohn_Disease
[group('Research')]
research-disorder provider disorder *args="":
    #!/usr/bin/env bash
    set -e
    mkdir -p {{research_dir}}
    yaml_file="{{kb_dir}}/{{disorder}}.yaml"
    if [ ! -f "$yaml_file" ]; then
        echo "Error: Disorder file not found: $yaml_file"
        ls -1 {{kb_dir}}/*.yaml | xargs -I {} basename {} .yaml | head -20
        exit 1
    fi
    disease_name=$(grep "^name:" "$yaml_file" | head -1 | sed 's/name: *//' | tr '_' ' ')
    category=$(grep "^category:" "$yaml_file" | head -1 | sed 's/category: *//' || echo "")
    output_file="{{research_dir}}/{{disorder}}-deep-research-{{provider}}.md"
    echo "Researching: $disease_name ({{provider}}) -> $output_file"
    provider_arg=$([[ "{{provider}}" == "cborg" ]] && echo "--use-cborg" || echo "--provider {{provider}}")
    uv run deep-research-client research \
        --template {{templates_dir}}/disease_pathophysiology_research.md \
        --var "disease_name=$disease_name" \
        --var "mondo_id=" \
        --var "category=$category" \
        $provider_arg \
        --output "$output_file" \
        --separate-citations "$output_file.citations.md" \
        {{args}}

# List available research providers
[group('Research')]
research-providers:
    uv run deep-research-client providers

# Fetch and cache a reference by PMID
[group('Research')]
fetch-reference pmid:
    uv run linkml-reference-validator cache reference {{pmid}}
