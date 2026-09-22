# Agent Model Config

[`.github/agent-config.yaml`](https://github.com/monarch-initiative/dismech/blob/main/.github/agent-config.yaml)
is the source of truth for **which Claude model each agentic workflow requests**.
Change model selections in that one file (issue #5218). The resolver passes the
configured strings through; it does not discover new releases or test whether
the account can access a model.

**New Opus releases are not picked up automatically by the current config.**
For example, `claude-opus-5` selects Opus 5, not the newest Opus. The scanner
selects a separate model for each of its three effort tiers, and changing
`default_model` does not change any of those selections.

## The curation-scanner matrix

Every scheduled or manual run of
[`curation-scanner.yml`](https://github.com/monarch-initiative/dismech/blob/main/.github/workflows/curation-scanner.yml)
launches all three configured rows as parallel jobs:

| Effort tier | Requested model | Candidate routing |
|---|---|---|
| `low_effort` | `claude-haiku-4-5-20251001` | Items labelled `curation` and `low_effort` |
| `medium_effort` | `claude-sonnet-5` | Items labelled `curation` and `medium_effort`, excluding `low_effort` |
| `high_effort` | `claude-opus-5` | Items labelled `curation`, excluding both `low_effort` and `medium_effort` |

The high tier includes items with **no effort label**; it does not require a
`high_effort` label. All tiers search for open, unassigned issues and PRs. The
prompt additionally tells the agent to skip items with multiple effort labels
and choose only one item to work on **per tier job**. The low tier must route
new disease creation to the high tier. These effort names describe the task
queue and prompt; they do not set Claude Code's reasoning `--effort` option.

The model reaches Claude Code in four steps:

1. The `setup` job checks out the repository and calls
   `.github/actions/resolve-agent-config/resolve_agent_config.py` with
   `--workflow curation-scanner --matrix`.
2. The resolver reads `workflows.curation-scanner.matrix` from
   `.github/agent-config.yaml` and prints its rows as JSON.
3. `needs.setup.outputs.matrix` feeds `strategy.matrix.include`, producing one
   job per row with `matrix.effort`, `matrix.selector`, and `matrix.model`.
4. `Run Curation Scanner` passes `--model ${{ matrix.model }}` to Claude Code.

**Matrix mode has no model fallback or override.** Every row must supply
`model:`; a missing model is an error. It does not use the workflow-level
`model:`, `default_model`, or the single-model resolver's `--override` argument.
The scanner's manual dispatch exposes only `note`, so a manual run uses the
same matrix as a scheduled run. The note is prompt text, not a model control.

## Single-model workflows

The other managed agent workflows resolve their model via the composite action
[`.github/actions/resolve-agent-config`](https://github.com/monarch-initiative/dismech/tree/main/.github/actions/resolve-agent-config).
The action reads `agent-config.yaml`, resolves the effective model, and exports
it as the `AGENT_MODEL` environment variable for the following steps, which pass
it to `claude-code-action` as `--model ${{ env.AGENT_MODEL }}`.

Resolution order (highest priority first):

1. an explicit per-run override — a `workflow_dispatch` `model:` input, passed to
   the action as `model-override`;
2. the per-workflow `model:` in `agent-config.yaml`;
3. the top-level `default_model`.

Scheduled runs use the config. Where a workflow exposes a manual `model` input,
it is an optional **text field**: leave it blank to use the config or enter a
model ID/alias for that run. Not every workflow exposes this input. In
particular, neither `curation-scanner` nor `claude-code-review` does.

Every currently configured workflow has explicit model values, including every
scanner row. **Changing `default_model` alone therefore changes none of the
current workflows.** It is a fallback for a single-model entry with no `model:`.

## Do new model releases take effect automatically?

There are two different kinds of model selection:

| Config value | Meaning | Follows future releases? |
|---|---|---|
| `claude-opus-5` | The Opus 5 release | No |
| `claude-opus-5-5` | The Opus 5.5 release | No |
| `claude-haiku-4-5-20251001` | A dated Haiku 4.5 snapshot | No |
| `opus` | Claude Code's Opus family alias | As Claude Code updates its mapping, subject to provider and account restrictions |

An ID without a date can still be pinned: Anthropic's
[model versioning documentation](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
specifies that IDs from the 4.6 generation onward identify fixed releases.

As of **2026-09-22**, Anthropic lists
[Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview) as released
under `claude-opus-5-5`. This repository still requests `claude-opus-5` for its
Opus jobs. Anthropic's
[Claude Code model configuration](https://code.claude.com/docs/en/model-config#model-aliases)
documents the `opus` alias's updated mapping and requires Claude Code
**v2.1.280 or later** for Opus 5.5. Verify the runtime version when upgrading;
changing the model string does not upgrade the installed runtime.

The `anthropics/claude-code-action@<commit>` reference pins the action code,
while `--model` selects the requested model. Updating the action alone does not
replace a versioned model ID in our config. Likewise, API-key versus OAuth
authentication determines credentials and access, not the configured model
string. The scanner prefers `ANTHROPIC_API_KEY` when set and otherwise uses
`CLAUDE_CODE_OAUTH_TOKEN`.

## Changing a model

To change only the scanner's high tier, edit the `model:` on the `high_effort`
row in `.github/agent-config.yaml`. For example, adopting Opus 5.5 explicitly
would change that row to:

```yaml
workflows:
  curation-scanner:
    matrix:
      # Keep the existing low_effort and medium_effort rows.
      - effort: high_effort
        model: claude-opus-5-5
        selector: "label:curation -label:low_effort -label:medium_effort"
```

For a repository-wide Opus upgrade, change every intended Opus value in the
config, including the default, the scanner row, and explicit per-workflow
models. Update config-specific expectations in `tests/test_agent_config.py`
and model examples in this page. Merge the config change to `main` for future
scheduled runs; manual runs read the config from the branch/ref selected for
the dispatch.

To deliberately follow Claude Code's Opus alias instead, use `model: opus` at
the relevant config locations. That trades an explicit release choice for a
mapping that can change with the runtime/provider. It is an opt-in change;
none of the current entries uses a family alias.

## Checking what a run requests and uses

Preview the resolved scanner rows locally without calling Claude or launching
a workflow:

```bash
uv run python .github/actions/resolve-agent-config/resolve_agent_config.py \
  --config .github/agent-config.yaml --workflow curation-scanner --matrix
```

For a single-model workflow, omit `--matrix`; optionally supply `--override`:

```bash
uv run python .github/actions/resolve-agent-config/resolve_agent_config.py \
  --config .github/agent-config.yaml --workflow pr-shepherd

uv run pytest tests/test_agent_config.py
```

In Actions, the scanner's `setup` → `Resolve curation matrix from agent config`
step logs `curation matrix: [...]`. Single-model jobs log
`resolve-agent-config: '<workflow>' -> <model>` in `Resolve agent config`.
Those lines establish the **requested** model. To confirm what actually ran,
inspect the Claude execution output in `Run Curation Scanner` (full output is
enabled), especially the result event's `modelUsage` keys. A family alias, a
runtime fallback, or a subagent can make that differ from the config string.
The final prose report alone is not a model/version record.

## Adding a workflow

For a single-model workflow:

1. Add a `workflows.<stem>` entry with a `model:`.
2. In the workflow, after checkout, add:
   ```yaml
   - name: Resolve agent config
     uses: ./.github/actions/resolve-agent-config
     with:
       workflow: <stem>
       model-override: ${{ inputs.model }}   # omit if no model input
   ```
3. Use `--model ${{ env.AGENT_MODEL }}` in the agent invocation.

For a matrix workflow, follow the scanner's `setup` job pattern instead: add a
`matrix:` list, call the resolver with `--matrix`, and pass `matrix.model`.

`tests/test_agent_config.py` enforces the contract: every `workflows:` key maps
to a real workflow file that uses the composite action or matrix resolver, and
no workflow hardcodes a `--model claude-*` inline.

## Scope and relationship to cron-profiles

This config covers the **AI model** only. Cron *cadence* stays in
[`.github/cron-profiles.yaml`](cron-profiles.md) because GitHub cannot
parameterize `schedule:` at run time. Per-workflow enable/disable and a provider
abstraction (`provider:` is reserved but not yet consumed) are planned follow-ups
under issue #5218.

`claude.yml` (the `@claude` mention responder) is also managed here (`claude:`
key → `claude-opus-5`); it resolves `AGENT_MODEL` via the same
`resolve-agent-config` step and passes `--model ${{ env.AGENT_MODEL }}` in
`claude_args`, so its model lives in this file like every other agentic workflow.
