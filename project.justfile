## Add your own just recipes here. This is imported by the main justfile.

# Default schema path
schema_path := "src/dismech/schema/dismech.yaml"
kb_dir := "kb/disorders"
comorbidity_dir := "kb/comorbidities"

# Validate all disorder YAML files (schema + terms + references)
# Runs all validations and reports ALL errors at the end
[group('QC')]
validate-all:
    #!/usr/bin/env bash
    just fix-references-cache
    failed_files=()
    echo "Validating all disorder files..."
    for f in {{kb_dir}}/*.yaml; do
        if [[ "$f" == *.history.yaml ]]; then
            continue
        fi
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
[group('QC')]
validate-comorbidity file:
    #!/usr/bin/env bash
    set -e
    echo "Schema validation..."
    uv run linkml-validate --schema {{schema_path}} --target-class ComorbidityAssociation {{file}}
    echo "Term validation..."
    uv run linkml-term-validator validate-data {{file}} -s {{schema_path}} -t ComorbidityAssociation --labels --no-dynamic-enums -c {{oak_config}}
    echo "Reference validation..."
    just fix-references-cache
    uv run linkml-reference-validator validate data {{file}} --schema {{schema_path}} --target-class ComorbidityAssociation
    echo "✓ All validations passed for {{file}}"

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
    just fix-references-cache
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
        term_output=$(uv run linkml-term-validator validate-data "$f" -s {{schema_path}} -t ComorbidityAssociation --labels -c {{oak_config}} 2>&1 || true)
        if ! echo "$term_output" | grep -q "Validation passed"; then
            errors+="  [TERMS] $term_output\n"
        fi
        # Reference validation
        ref_output=$(uv run linkml-reference-validator validate data "$f" --schema {{schema_path}} --target-class ComorbidityAssociation 2>&1 || true)
        if echo "$ref_output" | grep -q "\[ERROR\]"; then
            errors+="  [REFERENCES]\n$(echo "$ref_output" | grep -A2 "\[ERROR\]")\n"
        elif ! echo "$ref_output" | grep -q "All validations passed"; then
            errors+="  [REFERENCES] $ref_output\n"
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
        echo "✓ All comorbidity files validated successfully!"
    else
        echo "✗ ${#failed_files[@]} comorbidity file(s) with errors:"
        for f in "${failed_files[@]}"; do
            echo "  - $f"
        done
        exit 1
    fi

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

# Run all QC checks (full validation + deep-research report checks)
[group('QC')]
qc: validate-all qc-deep-research
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
    echo "Dashboard generated in dashboard/"

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

# Serve the browser app locally
[group('Browser')]
serve-browser: gen-browser-data
    @echo "Starting local server at http://localhost:8000/app/"
    uv run python -m http.server 8000

# Deploy browser (generate data and open)
[group('Browser')]
deploy-browser: gen-browser-data
    @echo "Browser app ready at app/index.html"
    @echo "Data generated with $(find {{kb_dir}} -maxdepth 1 -type f -name '*.yaml' ! -name '*.history.yaml' | wc -l | tr -d ' ') disorders"

# Generate individual HTML pages for all disorders and comorbidities
[group('Pages')]
gen-pages:
    uv run python -m dismech.render --all
    @echo "Generated $(ls -1 pages/disorders/*.html 2>/dev/null | wc -l | tr -d ' ') disorder pages and $(ls -1 pages/comorbidities/*.html 2>/dev/null | wc -l | tr -d ' ') comorbidity pages"

# Generate a single disorder page
[group('Pages')]
gen-page file:
    uv run python -m dismech.render {{file}}

# Generate a single comorbidity page
[group('Pages')]
gen-comorbidity-page file:
    uv run python -m dismech.render --comorbidity {{file}}

# Generate all comorbidity pages
[group('Pages')]
gen-comorbidity-pages:
    uv run python -m dismech.render --comorbidity {{comorbidity_dir}}

# Generate all pages and browser data
[group('Pages')]
gen-all: gen-browser-data gen-pages
    @echo "Generated browser data, disorder pages, and comorbidity pages"

# ============== KGX Export ==============

# Generate KGX edges from disorder knowledge base
[group('Export')]
export-kgx:
    mkdir -p output/kgx
    uv run koza transform src/dismech/export/kgx_export.py -o output/kgx -f jsonl kb/disorders/*.yaml

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
	uv run deep-research-client research \
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
        ls -1 {{kb_dir}}/*.yaml | xargs -I {} basename {} .yaml | head -20
        exit 1
    fi
    disease_name=$(grep "^name:" "$yaml_file" | head -1 | sed 's/name: *//' | tr '_' ' ')
    category=$(grep "^category:" "$yaml_file" | head -1 | sed 's/category: *//' || echo "")
    output_file="{{research_dir}}/{{disorder}}-deep-research-cyberian-codex.md"
    echo "Researching: $disease_name (cyberian-codex) -> $output_file"
    uv run deep-research-client research \
        --template {{templates_dir}}/disease_pathophysiology_research.md \
        --var "disease_name=$disease_name" \
        --var "mondo_id=" \
        --var "category=$category" \
        --provider cyberian \
        --param agent_type=codex \
        --output "$output_file" \
        --separate-citations "$output_file.citations.md" \
        {{args}}

# List available research providers
[group('Research')]
research-providers:
    uv run deep-research-client providers

# Fetch and cache a reference by ID
# This may be a PMID, DOI, or other supported identifier
[group('Research')]
fetch-reference +identifiers:
    #!/usr/bin/env bash
    for identifier in {{identifiers}}; do
        echo "Fetching reference: $identifier"
        uv run linkml-reference-validator cache reference "$identifier"
    done

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

# Compare dismech phenotypes against OMIM/Orphanet for a single disease
[group('Analysis')]
d2p-compare disease:
    uv run python -m dismech.d2p_compare compare "{{disease}}"

# Compare all diseases in the KB against OMIM/Orphanet
[group('Analysis')]
d2p-compare-all:
    uv run python -m dismech.d2p_compare compare-all

# Compare with JSON output
[group('Analysis')]
d2p-compare-json disease:
    uv run python -m dismech.d2p_compare compare "{{disease}}" --format json
