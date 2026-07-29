#!/bin/bash
# SessionStart hook: ensure `just` is installed and Python deps are synced with uv.
# Runs at the start of Claude Code on the web sessions so validators, linters, and
# tests are ready before the agent loop begins.
set -euo pipefail

# Only run in remote (Claude Code on the web) environments. Local dev machines
# manage their own toolchain via `just install`.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"
export PATH="$BIN_DIR:$HOME/.cargo/bin:$PATH"

# 1. Ensure `just` is installed (idempotent). Prefer the official prebuilt-binary
#    installer (fast, no compile); fall back to `cargo install` if that fails.
if ! command -v just >/dev/null 2>&1; then
  echo "just not found; installing to $BIN_DIR ..."
  if ! curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh \
      | bash -s -- --to "$BIN_DIR"; then
    echo "prebuilt install failed; falling back to cargo install just ..."
    cargo install just
  fi
fi
just --version

# 2. Sync Python dependencies (including the dev group used by tests/linters).
uv sync --group dev

# 3. Persist PATH for the session so `just` and uv-installed tools are found.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"$BIN_DIR:\$HOME/.cargo/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
