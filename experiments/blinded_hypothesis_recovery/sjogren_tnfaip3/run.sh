#!/usr/bin/env bash
# Run one blinding level through OpenScientist.
# Usage (from the repository root):
#   experiments/blinded_hypothesis_recovery/sjogren_tnfaip3/run.sh blind
#   experiments/blinded_hypothesis_recovery/sjogren_tnfaip3/run.sh semi
set -euo pipefail
level=$1
provider=${2:-openscientist}
here=experiments/blinded_hypothesis_recovery/sjogren_tnfaip3
"$here/check_blinding.sh"
out="$here/reports/$level-$provider.md"
mkdir -p "$here/reports"
scripts/run_deep_research_client.sh research \
    --template experiments/blinded_hypothesis_recovery/template.md \
    --var "disease_name=Sjogren's Syndrome" \
    --var "mondo_id=MONDO:0010030" \
    --var "existing_mechanism=$(cat "$here/existing_mechanism.txt")" \
    --var "existing_genetics=$(cat "$here/existing_genetics.txt")" \
    --var "focus=$(cat "$here/focus_$level.txt")" \
    --provider "$provider" \
    --output "$out" \
    --separate-citations "$out.citations.md" \
    --validate-references --validation-cache-dir references_cache
