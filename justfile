# ============ Hint for for Windows Users ============

# On Windows the "sh" shell that comes with Git for Windows should be used.
# If it is not on path, provide the path to the executable in the following line.
#set windows-shell := ["C:/Program Files/Git/usr/bin/sh", "-cu"]

# ============ Variables used in recipes ============

# Load environment variables from config.public.mk or specified file
set dotenv-load := true
# set dotenv-filename := env_var_or_default("LINKML_ENVIRONMENT_FILENAME", "config.public.mk")
set dotenv-filename := x'${LINKML_ENVIRONMENT_FILENAME:-config.public.mk}'

# Pass recipe arguments to shell recipes as real positional arguments ($1, $@)
# instead of only via {{...}} text interpolation. This lets recipes iterate file
# lists safely with `for f in "$@"`, so paths containing shell metacharacters
# (e.g. an apostrophe in `Bell's_Palsy.yaml`) no longer break the generated
# script. See issue #5525.
set positional-arguments := true

# Set shebang line for cross-platform Python recipes (assumes presence of launcher on Windows)
shebang := if os() == 'windows' {
  'py'
} else {
  '/usr/bin/env python3'
}

# Environment variables with defaults
schema_name := env_var_or_default("LINKML_SCHEMA_NAME", "_no_schema_given_")
source_schema_dir := env_var_or_default("LINKML_SCHEMA_SOURCE_DIR", "")
config_yaml := if env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "") != "" {
  "--config-file " + env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "")
} else {
  ""
}
gen_doc_args := env_var_or_default("LINKML_GENERATORS_DOC_ARGS", "")
gen_java_args := env_var_or_default("LINKML_GENERATORS_JAVA_ARGS", "")
gen_owl_args := env_var_or_default("LINKML_GENERATORS_OWL_ARGS", "")
gen_pydantic_args := env_var_or_default("LINKML_GENERATORS_PYDANTIC_ARGS", "")
gen_ts_args := env_var_or_default("LINKML_GENERATORS_TYPESCRIPT_ARGS", "")

# Directory variables
src := "src"
dest := "project"
pymodel := src / schema_name / "datamodel"
source_schema_path := source_schema_dir / schema_name + ".yaml"
docdir := "docs/schema"  # Directory for generated schema documentation
merged_schema_path := "docs/schema" / schema_name + ".yaml"

# ============== Project recipes ==============

# List all commands as default command. The prefix "_" hides the command.
_default: _status
    @just --list

# Initialize a new project (use this for projects not yet under version control)
[group('project management')]
setup: _check-config _git-init install _git-add && _setup_part2
  git commit -m "Initialise git with minimal project" -a

_setup_part2: gen-project gen-doc
  @echo
  @echo '=== Setup completed! ==='
  @echo 'Various model representations have been created under directory "project". By default'
  @echo 'they are ignored by git. You decide whether you want to add them to git tracking or'
  @echo 'continue to git-ignore them as they can be regenerated if needed.'
  @echo 'For tracking specific subfolders, add !project/[foldername]/* line(s) to ".gitignore".'

# Install project dependencies
[group('project management')]
install:
  uv sync --group dev
  @if [ -f package-lock.json ] || [ -f package.json ]; then \
    if ! command -v npm >/dev/null 2>&1; then \
      echo "npm is required to install browser search test dependencies."; \
      exit 1; \
    fi; \
    if [ -f package-lock.json ]; then \
      npm ci; \
    else \
      npm install; \
    fi; \
  fi

# Updates project template and LinkML package
[group('project management')]
update: _update-template _update-linkml

# Clean all generated files
[group('project management')]
clean: _clean_project
  rm -rf tmp
  rm -rf {{docdir}}/*.md {{docdir}}/classes {{docdir}}/slots {{docdir}}/enums {{docdir}}/types

# (Re-)Generate project and documentation locally
[group('model development')]
site: gen-project gen-doc

# Deploy documentation site to Github Pages
[group('deployment')]
deploy: site
  mkd-gh-deploy

# Run all tests (fast code/logic checks + the whole-KB conformance sweep)
[group('model development')]
test: test-code test-kb

# Fast code/logic tests: everything except the whole-KB `kb_data` conformance sweep
[group('model development')]
test-code: _test-schema _test-python-code _test-examples test-search test-extension

# Schema generator smoke test.
[group('model development')]
test-schema: _test-schema

# Python code/logic tests, excluding the whole-KB `kb_data` sweep.
[group('model development')]
test-python-code: _test-python-code

# Validate a provider-by-assessor hypothesis report review sidecar.
[group('data validation')]
validate-hypothesis-assessment file:
  uv run linkml-validate --schema src/dismech/schema/hypothesis_assessment.yaml --target-class HypothesisAssessment {{file}}
  uv run python -m dismech.hypothesis_assessment {{file}}

# LinkML valid/invalid example round-trip tests.
[group('model development')]
test-examples: _test-examples

# Whole-KB schema-conformance sweep (parametrized over every KB file), parallelized.
# In CI this is gated on schema / conformance-test changes; run on demand locally.
[group('model development')]
test-kb: _test-python-kb

# Run linting
[group('model development')]
lint:
  uv run linkml-lint {{source_schema_dir}}

# Generate md documentation for the schema
#
# PYTHONHASHSEED=0 is load-bearing, not hygiene. LinkML renders union/any_of
# members by iterating a set, so their order follows Python's per-process hash
# randomisation: two runs of this recipe on the same input emit e.g.
#   "[Any] or [FrequencyQuantity] or [FrequencyEnum]"
#   "[FrequencyEnum] or [FrequencyQuantity] or [Any]"
# and ~129 of the generated files churn. elements/ is committed and CI requires
# a fresh render to match it byte for byte, so without a fixed seed that check
# can never pass. See the note on gen-schema-docs in project.justfile.
[group('model development')]
gen-doc: _gen-yaml
  PYTHONHASHSEED=0 uv run gen-doc --subfolder-type-separation {{gen_doc_args}} -d {{docdir}} {{source_schema_path}}

# Build docs and run test server
[group('model development')]
testdoc: gen-doc _serve

# Generate the Python data models (dataclasses & pydantic)
gen-python:
  uv run gen-project -d  {{pymodel}} -I python {{source_schema_path}}
  uv run gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py

# Generate project files including Python data model
[group('model development')]
gen-project:
  uv run gen-project {{config_yaml}} -d {{dest}} {{source_schema_path}}
  mv {{dest}}/*.py {{pymodel}}
  uv run gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py
  uv run gen-java {{gen_java_args}} --output-directory {{dest}}/java/ {{source_schema_path}}
  @if [ ! ${{gen_owl_args}} ]; then \
    mkdir -p {{dest}}/owl && \
    uv run gen-owl {{gen_owl_args}} {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
  fi
  @if [ ! ${{gen_ts_args}} ]; then \
    uv run gen-typescript {{gen_ts_args}} {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
  fi

# ============== Migrations recipes for Copier ==============

# Hidden command to adjust the directory layout on upgrading a project
# created with linkml-project-copier v0.1.x to v0.2.0 or newer.
# Use with care! - It may not work for customized projects.
_post_upgrade_v020: && _post_upgrade_v020py
  mv docs/*.md docs/schema

_post_upgrade_v020py:
    #!{{shebang}}
    import subprocess
    from pathlib import Path
    # Git move files from folder src to folder dest
    tasks = [
        (Path("src/docs/files"), Path("docs")),
        (Path("src/docs/templates"), Path("docs/templates-linkml")),
        (Path("src/data/examples"), Path("tests/data/")),
    ]
    for src, dest in tasks:
        for path_obj in src.rglob("*"):
            if not path_obj.is_file():
                continue
            file_dest = dest / path_obj.relative_to(src)
            if not file_dest.parent.exists():
                file_dest.parent.mkdir(parents=True)
            print(f"Moving {path_obj} --> {file_dest}")
            subprocess.run(["git", "mv", str(path_obj), str(file_dest)])
    print(
        "Migration to v0.2.x completed! Check the changes carefully before committing."
    )

# ============== Hidden internal recipes ==============

# Show current project status
_status: _check-config
  @echo "Project: {{schema_name}}"
  @echo "Source: {{source_schema_path}}"

# Check project configuration
_check-config:
    #!{{shebang}}
    import os
    schema_name = os.getenv('LINKML_SCHEMA_NAME')
    if not schema_name:
        print('**Project not configured**:\n - See \'.env.public\'')
        exit(1)
    print('Project-status: Ok')

# Update project template
_update-template:
  copier update --trust --skip-answered

# Update LinkML to latest version
_update-linkml:
  uv add linkml --upgrade-package linkml

# Test schema generation
_test-schema:
  uv run gen-project {{config_yaml}} -d tmp {{source_schema_path}}

# Run the fast Python unit tests (excludes the whole-KB `kb_data` sweep)
_test-python-code: gen-python
  uv run python -m pytest -m "not kb_data"

# Run the whole-KB schema-conformance sweep (`kb_data`), parallelized with xdist
_test-python-kb: gen-python
  uv run python -m pytest -m "kb_data" -n auto

# Run example tests
_test-examples: _ensure_examples_output
  uv run linkml-run-examples \
    --input-formats json \
    --input-formats yaml \
    --output-formats json \
    --output-formats yaml \
    --counter-example-input-directory tests/data/invalid \
    --input-directory tests/data/valid \
    --output-directory examples/output \
    --schema {{source_schema_path}} > examples/output/README.md

# Generate merged model
#
# The merged schema is copied into elements/ and committed, so two wall-clock
# stamps LinkML writes unconditionally (it honours neither --no-metadata nor
# SOURCE_DATE_EPOCH) would otherwise make a fresh render differ from the
# committed copy. Both are pinned to the same constant the MkDocs build uses:
#
#   generation_date  — when gen-yaml ran. Differs on every run.
#   source_file_date — the **mtime of the source schema file**. This one is
#     nastier: it is stable on a working copy, so it looks fine locally, but a
#     fresh `git clone` sets mtimes to checkout time — so it differs on every
#     CI run, and between CI and any developer machine. It is what kept
#     deploy-docs red after the first four fixes landed (#8025).
#
# `source_file_size` is content-derived and needs no pinning. Both stamps
# record provenance git already records more accurately.
# Generated to a temp file and rewritten in place rather than piped through
# sed: `just` runs recipes with `sh -cu`, where a pipeline's exit status is the
# LAST command's, so `gen-yaml ... | sed > out` would report sed's success even
# when gen-yaml crashed — silently publishing an empty merged schema. `set -o
# pipefail` is NOT an option here: /bin/sh is dash on the CI runners, which
# rejects it outright ("Illegal option -o pipefail").
_gen-yaml:
  -mkdir -p docs/schema
  PYTHONHASHSEED=0 uv run gen-yaml {{source_schema_path}} > {{merged_schema_path}}.tmp
  sed -e "s/^generation_date: .*/generation_date: '2025-01-01T00:00:00'/" \
      -e "s/^source_file_date: .*/source_file_date: '2025-01-01T00:00:00'/" \
    {{merged_schema_path}}.tmp > {{merged_schema_path}}
  rm -f {{merged_schema_path}}.tmp

# Run documentation server
_serve:
  uv run mkdocs serve

# Initialize git repository
_git-init:
  git init

# Add files to git
_git-add:
  git add .

# Commit files to git
_git-commit:
  git commit -m 'chore: just setup was run' -a

# Show git status
_git-status:
  git status

_clean_project:
    #!{{shebang}}
    import shutil, pathlib
    # remove the generated project files
    for d in pathlib.Path("{{dest}}").iterdir():
        if d.is_dir():
            print(f'removing "{d}"')
            shutil.rmtree(d, ignore_errors=True)
    # remove the generated python data model
    for d in pathlib.Path("{{pymodel}}").iterdir():
        if d.name == "__init__.py":
            continue
        print(f'removing "{d}"')
        if d.is_dir():
            shutil.rmtree(d, ignore_errors=True)
        else:
            d.unlink()

_ensure_examples_output:  # Ensure a clean examples/output directory exists
  -mkdir -p examples/output
  -rm -rf examples/output/*.*

# ============== Include project-specific recipes ==============

import "project.justfile"
