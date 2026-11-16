#!/usr/bin/env bash
# Wrapper for deep-research-client that applies dismech's Biomni opt-in policy.
#
# Usage: scripts/run_deep_research_client.sh [args...]
#   e.g.: scripts/run_deep_research_client.sh research --template t.md --provider falcon ...
#         scripts/run_deep_research_client.sh validate-references report.md --in-place
#
# Why this exists: the policy must be applied before provider discovery, so
# that Biomni is not offered as a fallback in a session that has not opted in.
#
# Biomni is unavailable, including as an automatic fallback, unless
# DISMECH_ENABLE_BIOMNI=1.
#
# It also applies the one surviving reference-validator patch, because
# deep-research-client resolves a report's references by calling
# linkml-reference-validator in-process, which reads and writes
# references_cache/. Those repairs are upstream now (dismech#11849).
#
# It also installs the Perplexity request patch (dismech#9357): the upstream
# provider holds one POST open while sonar-deep-research works, and the model
# sends no bytes for minutes (even when streaming, until its search phase ends),
# so a proxy idle timeout drops the request. The patch submits the request to
# Perplexity's async API and polls for the result instead;
# DISMECH_PERPLEXITY_TRANSPORT=stream selects the older streaming path.

set -euo pipefail

exec uv run python -c "
import sys


from dismech.deep_research_policy import (
    BIOMNI_DISABLED_DETAIL,
    configure_biomni_environment,
    requests_biomni_research,
)

biomni_opted_in = configure_biomni_environment()
if not biomni_opted_in and requests_biomni_research(sys.argv[1:]):
    print(BIOMNI_DISABLED_DETAIL, file=sys.stderr)
    raise SystemExit(2)

from deep_research_client.cli import app
from deep_research_client.providers.biomni import BiomniProvider

# Explain the opt-in policy wherever the client says why Biomni is unavailable.
if not biomni_opted_in:
    BiomniProvider.registration_requirement = BIOMNI_DISABLED_DETAIL

# Submit Perplexity requests as async jobs so an idle-timeout proxy does not
# drop a multi-minute sonar-deep-research request (dismech#9357).
from dismech.perplexity_streaming import install as install_perplexity_streaming

install_perplexity_streaming()

app()
" "$@"
