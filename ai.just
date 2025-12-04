claude:
  [ -f CLAUDE.md ] || ln -s AGENTS.md CLAUDE.md

goosehints:
  [ -f .goosehints ] || ln -s AGENTS.md .goosehints

copilot-instructions:
  [ -f .github/copilot-instructions.md ] || cd .github && ln -s ../AGENTS.md copilot-instructions.md

setup-ai: setup-ai-instructions setup-gh

setup-ai-instructions: claude goosehints copilot-instructions

setup-gh: gh-add-topics gh-add-secrets

gh-add-topics:
  gh repo edit --add-topic "monarchinitiative,ai4curation"

gh-add-secrets:
  #!/usr/bin/env bash
  set -euo pipefail

  # Function to set secret if env var exists
  set_secret_if_exists() {
    local secret_name="$1"
    local gh_var="GH_$secret_name"
    local plain_var="$secret_name"

    if [ -n "${!gh_var:-}" ]; then
      echo "Setting $secret_name from $gh_var"
      gh secret set "$secret_name" --body "${!gh_var}"
    elif [ -n "${!plain_var:-}" ]; then
      echo "Setting $secret_name from $plain_var"
      gh secret set "$secret_name" --body "${!plain_var}"
    else
      echo "Skipping $secret_name (neither $gh_var nor $plain_var is set)"
    fi
  }

  # Set each secret if the corresponding env var exists
  set_secret_if_exists "PAT_FOR_PR"
  set_secret_if_exists "ANTHROPIC_API_KEY"
  set_secret_if_exists "OPENAI_API_KEY"
  set_secret_if_exists "CBORG_API_KEY"
  set_secret_if_exists "CLAUDE_CODE_OAUTH_TOKEN"

gh-invite-dragon-ai:
  gh api repos/:owner/:repo/collaborators/dragon-ai-agent --method PUT --field permission=write > /dev/null

