#!/usr/bin/env bash
# Pre-provision the sqlite:obo:* ontology databases that dismech term validation
# needs, with resume + retry, so a flaky/blocked download does not abort a
# validation run mid-transfer.
#
# Background: `just validate-all` / `just qc` (and, historically, single-file
# `just validate`) can make OAK lazily fetch every `sqlite:obo:<name>` database
# referenced by conf/oak_config.yaml. The lazy OAK downloader has no
# resume/retry, so one interrupted fetch fails the whole run. This script
# fetches those DBs up front from the public bbop-sqlite S3 bucket using
# `curl -C -` (resume) with retries, then gunzips them into OAK's cache dir.
#
# The DBs that remain local are now all small (hgnc, geno, ecto, xco, opl,
# icd10cm, icd11f): every large ontology — ncbitaxon, chebi, ncit, hp, plus
# mondo/go/uberon/cl/pato/envo/foodon — has been moved to ols:. See issue #5160
# and the note at the bottom of conf/oak_config.yaml. This script is therefore
# far less load-bearing than it was, but is kept for constrained/offline
# environments and in case a prefix is ever moved back to a local build.
#
# Usage:
#   scripts/fetch_ontology_dbs.sh                 # fetch every DB in oak_config.yaml
#   scripts/fetch_ontology_dbs.sh hgnc geno       # fetch only the named ontologies
#   PYSTOW_HOME=/path scripts/fetch_ontology_dbs.sh   # canonical cache location
#
# IMPORTANT — where OAK actually looks: OAK resolves sqlite:obo:<name> to
#   ${PYSTOW_HOME:-$HOME/.data}/oaklib/<name>.db   (pystow.module("oaklib"))
# and reads ONLY PYSTOW_HOME. It does NOT honor OAK_DB_DIR. So PYSTOW_HOME is
# the canonical knob: set it (or leave it unset for the ~/.data default) and the
# DBs this script writes will be found by OAK. OAK_DB_DIR remains as an escape
# hatch for staging files to an arbitrary directory, but if it does not equal
# ${PYSTOW_HOME:-$HOME/.data}/oaklib, OAK will ignore what you fetched and
# re-download. The guard below warns when that mismatch is about to happen.
# See docs/explanation/oak-database-caching.md.
set -euo pipefail

BASE_URL="https://semanticsql.berkeleybop.io"
OAK_CONFIG="${OAK_CONFIG:-conf/oak_config.yaml}"
# The directory OAK will actually read from, derived exactly as pystow does.
OAK_READ_DIR="${PYSTOW_HOME:-$HOME/.data}/oaklib"
DB_DIR="${OAK_DB_DIR:-$OAK_READ_DIR}"
RETRIES="${FETCH_RETRIES:-5}"

if [[ "$DB_DIR" != "$OAK_READ_DIR" ]]; then
    echo "WARNING: fetching into '$DB_DIR' but OAK reads from '$OAK_READ_DIR'." >&2
    echo "         OAK ignores OAK_DB_DIR; set PYSTOW_HOME instead so the DBs" >&2
    echo "         you fetch are the ones OAK uses. See docs/explanation/oak-database-caching.md." >&2
fi

mkdir -p "$DB_DIR"

# Names to fetch: explicit args, else every distinct sqlite:obo:<name> in oak_config.
if [[ $# -gt 0 ]]; then
    names=("$@")
else
    # Strip YAML comments first: the config *discusses* adapters it no longer
    # uses (e.g. the note explaining why NCBITaxon was moved off
    # sqlite:obo:ncbitaxon). Grepping the raw file matched those mentions and
    # queued a 13.5 GB download for an ontology now served over OLS.
    #
    # Only treat '#' as a comment at start-of-line or after whitespace, so a '#'
    # inside a quoted scalar is not mistaken for one — which is also what YAML
    # itself does. (No adapter string contains '#' today; this keeps that from
    # silently mattering later.) `sed -E` because BRE `\|` alternation is a GNU
    # extension: under BSD/macOS sed the strip would silently no-op and re-queue
    # the very ncbitaxon download this exists to prevent.
    mapfile -t names < <(
        sed -E 's/(^|[[:space:]])#.*/\1/' "$OAK_CONFIG" \
            | grep -oE 'sqlite:obo:[a-z0-9_]+' \
            | sed 's|sqlite:obo:||' \
            | sort -u
    )
fi

if [[ ${#names[@]} -eq 0 ]]; then
    echo "No sqlite:obo:* ontologies found in $OAK_CONFIG" >&2
    exit 1
fi

echo "Provisioning ${#names[@]} ontology DB(s) into $DB_DIR"
echo "Source: $BASE_URL"
echo

failed=()
for name in "${names[@]}"; do
    db="$DB_DIR/$name.db"
    gz="$DB_DIR/$name.db.gz"

    if [[ -f "$db" ]]; then
        printf '  %-14s already present (%s)\n' "$name" "$(du -h "$db" | cut -f1)"
        continue
    fi

    printf '  %-14s downloading %s.db.gz ...\n' "$name" "$name"
    # curl: -C - resume, --retry with backoff, long connect timeout, keep partial.
    if ! curl -fSL -C - \
        --retry "$RETRIES" --retry-delay 2 --retry-all-errors \
        --connect-timeout 30 \
        -o "$gz" "$BASE_URL/$name.db.gz"; then
        echo "    ! download failed for $name (leaving partial $gz for resume)" >&2
        failed+=("$name")
        continue
    fi

    printf '  %-14s unpacking ...\n' "$name"
    if ! gunzip -f "$gz"; then
        echo "    ! gunzip failed for $name" >&2
        failed+=("$name")
        continue
    fi
    printf '  %-14s ready (%s)\n' "$name" "$(du -h "$db" | cut -f1)"
done

echo
echo "OAK DB cache footprint: $(du -sh "$DB_DIR" 2>/dev/null | cut -f1) in $DB_DIR"

if [[ ${#failed[@]} -gt 0 ]]; then
    echo "Failed: ${failed[*]} — re-run to resume the interrupted transfer(s)." >&2
    exit 1
fi
echo "All requested ontology DBs are provisioned."
