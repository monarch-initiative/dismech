#!/usr/bin/env bash
# Validate the LOINC codes in the given KB files against the Monarch KG and
# write the resulting rows into cache/loinc/terms.csv.
#
# TEMPORARY. This exists because the oaklib release in uv.lock cannot serve
# LOINC labels: its `monarch:` adapter reads the entity payload's `symbol`
# field, which only genes populate, so `label()` is None for every LOINC code
# (fixed in INCATools/ontology-access-kit#920). Until a release carrying that
# fix is pinned and `conf/oak_config.yaml` routes `LOINC: "monarch:"`, this
# script overlays the fixed oaklib in an ephemeral environment -- the project
# venv is not modified -- and routes LOINC to it through a generated copy of
# the oak config. Once the pin lands, delete this script and the `loinc-seed-cache`
# recipe; `just validate-terms` will do the same thing with no overlay.
#
# Why the rows are legitimate cache content: they are written by
# linkml-term-validator from the authority, exactly as `just validate-terms`
# writes every other prefix's rows. Nothing here types a label. A curation PR
# that adds a LOINC code runs this once and commits the rows it produced, and
# from then on the code validates offline, cache-first, for everyone.
#
# Usage: scripts/seed_loinc_cache.sh kb/disorders/Foo.yaml [more files...]
set -euo pipefail

if [ "$#" -eq 0 ]; then
    echo "usage: $0 <kb yaml file>..." >&2
    exit 2
fi

# Pinned to the commit under review in INCATools/ontology-access-kit#920.
OAKLIB_FIX_REF="${OAKLIB_FIX_REF:-7694331}"
OAKLIB_SPEC="oaklib @ git+https://github.com/INCATools/ontology-access-kit@${OAKLIB_FIX_REF}"

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

tmp_conf="$(mktemp --suffix=.yaml)"
trap 'rm -f "$tmp_conf" .gene_requests_cache.sqlite' EXIT

if grep -qE '^\s*LOINC:' conf/oak_config.yaml; then
    cp conf/oak_config.yaml "$tmp_conf"
else
    # Quoted on purpose: a bare `monarch:` is a YAML scanner error.
    { cat conf/oak_config.yaml; printf '\n  LOINC: "monarch:"\n'; } > "$tmp_conf"
fi

# Invoked as a module, NOT as the `linkml-term-validator` console script. That
# script's shebang hard-codes the project venv's interpreter, so running it
# under `uv run --with` silently bypasses the overlay and imports the pinned
# oaklib instead of the fixed one -- which is the exact bug the overlay exists
# to work around. `python -m` runs in the ephemeral environment, so the overlay
# applies. The symptom of getting this wrong is worth knowing: every code is
# reported as "not found in ontology", which reads as "this code does not
# exist" rather than "the adapter could not return a label".
uv run --with "$OAKLIB_SPEC" python -m linkml_term_validator.cli validate-data "$@" \
    -s src/dismech/schema/dismech.yaml -t Disease --labels -c "$tmp_conf"
status=$?

echo "LOINC rows now cached: $(($(wc -l < cache/loinc/terms.csv) - 1))"
echo "Run 'just normalize-cache' before committing cache/loinc/terms.csv."
exit "$status"
