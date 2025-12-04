#!/usr/bin/env bash
set -e
odk --help || true
#curl -LsSf https://astral.sh/uv/install.sh | sh
#uv pip install oaklib
npm install -g @anthropic-ai/claude-code
