#!/bin/bash
set -euo pipefail

# Only run in Claude Code on the web
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install Python dependencies with uv
echo "Installing dependencies..."
uv sync --group dev

# Make EDISON API key available if set in Claude Code environment
if [ -n "${EDISON_API_KEY:-}" ]; then
  echo "export EDISON_API_KEY=\"$EDISON_API_KEY\"" >> "$CLAUDE_ENV_FILE"
  echo "✓ EDISON_API_KEY configured"
else
  echo "⚠ EDISON_API_KEY not set in environment"
  echo "  Add it to Claude Code's environment variables to enable deep research queries"
fi

echo "✓ Session startup complete"
