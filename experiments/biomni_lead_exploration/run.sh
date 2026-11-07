#!/usr/bin/env bash
# Run one repurposing-hypothesis assessment through a deep-research provider.
# Usage (from the repository root):
#   experiments/biomni_lead_exploration/run.sh <disease_dir> <slug> "<disease name>" "<drug>" "<drug action>" "<mechanism>" [provider]
set -euo pipefail
dir=experiments/biomni_lead_exploration/$1
slug=$2
provider=${7:-openscientist}
out="$dir/reports/$slug-$provider.md"
mkdir -p "$dir/reports"
scripts/run_deep_research_client.sh research \
    --template experiments/biomni_lead_exploration/repurposing_template.md \
    --var "disease_name=$3" \
    --var "drug=$4" \
    --var "drug_action=$5" \
    --var "mechanism=$6" \
    --provider "$provider" \
    --output "$out" \
    --separate-citations "$out.citations.md" \
    --validate-references --validation-cache-dir references_cache
