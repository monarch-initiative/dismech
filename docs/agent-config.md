# Agent Model Config

[`.github/agent-config.yaml`](https://github.com/monarch-initiative/dismech/blob/main/.github/agent-config.yaml)
is the source of truth for **which Claude model each agentic workflow requests**.
Change model selections in that one file (issue #5218). The resolver passes the
configured strings through; it does not discover new releases or test whether
the account can access a model.

**Policy: follow the latest model in each task's family, without release-bump
PRs.** Use `opus`, `sonnet`, and `haiku` in the config. Every managed workflow
installs the latest Claude Code at the start of its agent job through
[the shared setup action](https://github.com/monarch-initiative/dismech/tree/main/.github/actions/setup-claude-code)
and explicitly passes that executable to `claude-code-action`.

## What does “latest” mean?

| Value passed to Claude Code | Meaning |
|---|---|
| `opus` | Moving Opus family alias, resolved by Claude Code |
| `sonnet` | Moving Sonnet family alias |
| `haiku` | Moving Haiku family alias |
| `claude-opus-5` | Fixed original Opus 5 release (5.0), not “latest 5.x” |
| `claude-opus-5-5` | Fixed Opus 5.5 release |

`claude-opus-5` is **not an alias**. It will not turn into 5.4 or 5.5. Anthropic
omits the minor segment for a major release, and newer releases get separate
IDs. See [model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

The family aliases do move. As of 2026-09-22, Anthropic documents `opus` as
Opus 5.5 on the Anthropic API. Subsequent mappings belong to
[Claude Code's model configuration](https://code.claude.com/docs/en/model-config#model-aliases),
so this repository does not maintain a second release registry. “Latest” means
the family version Claude Code selects for the provider/account, not a promise
that every newly announced model is available immediately. Access restrictions
or provider rollout can delay it.

## Keeping current with minimal churn

- **Models:** keep family aliases in `agent-config.yaml`. Normal model releases
  require no YAML, test, or documentation version bumps. Keep tier assignments
  explicit so a new release does not change which jobs use Haiku versus Opus.
- **Claude Code:** `setup-claude-code` installs the `latest` release channel on
  each fresh agent runner, logs `claude --version`, and adds it to the run
  summary. No committed CLI version or cache can strand an old alias mapping.
- **Workflow action:** retain the upstream action references and their existing
  monthly Dependabot maintenance. The action's orchestration code/SDK is a
  separate dependency from the CLI; its bundled runtime is bypassed through
  `path_to_claude_code_executable`.
- **Troubleshooting:** compare the recorded CLI version and actual model in run
  output. If a release regresses, temporarily pin the affected config model to
  a known-good full ID. For a CLI regression, change the shared setup action's
  `version` default to a known-good version (or `stable`). Record the reason and
  a date to revisit the pin in the PR, then return to aliases/`latest` when fixed.

This fixes an earlier inconsistency: the reviewer explicitly installed
`2.1.129`, while the scanner relied on the runtime bundled with its pinned
upstream action. Neither path guaranteed the latest CLI. Merely switching
model strings to aliases would have left that gap in place. The shared setup
uses Anthropic's documented [native release-channel installer](https://code.claude.com/docs/en/setup#install-a-specific-version).
An installation failure stops the job; it does not silently use an older CLI.

## The curation-scanner matrix

Every scheduled or manual run of
[`curation-scanner.yml`](https://github.com/monarch-initiative/dismech/blob/main/.github/workflows/curation-scanner.yml)
launches all configured rows as parallel jobs:

| Effort tier | Requested model | Candidate routing |
|---|---|---|
| `low_effort` | `haiku` | Items labelled `curation` and `low_effort` |
| `medium_effort` | `sonnet` | Items labelled `curation` and `medium_effort`, excluding `low_effort` |
| `high_effort` | `opus` | Items labelled `curation`, excluding both `low_effort` and `medium_effort` |

The high tier includes items with **no effort label**; it does not require a
`high_effort` label. All tiers search for open, unassigned issues and PRs. The
prompt additionally tells the agent to skip items with multiple effort labels
and choose only one item to work on **per tier job**. The low tier must route
new disease creation to the high tier. These effort names describe the task
queue and prompt; they do not set Claude Code's reasoning `--effort` option.
Concurrency is per tier with `cancel-in-progress: true`: a new manual or
scheduled run cancels an older in-flight job of the same tier.

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
particular, neither `curation-scanner` nor `claude-code-review` does, and the
`claude.yml` mention responder has no manual dispatch trigger.

Every currently configured workflow has explicit model values, including every
scanner row. **Changing `default_model` alone therefore changes none of the
current workflows.** It is a fallback for a single-model entry with no `model:`.

## Changing a task's model family

Edit the workflow's `model:` in `.github/agent-config.yaml`, or the relevant
scanner matrix row. For example, `model: opus` selects the Opus family for that
task. A temporary fixed ID in the same slot opts that task out of upgrades.
Merge to `main` for future scheduled runs; manual runs read the config from the
branch/ref selected for the dispatch.

Authentication is separate: the scanner prefers `ANTHROPIC_API_KEY` when set,
otherwise `CLAUDE_CODE_OAUTH_TOKEN`. This selects credentials and access, not
the configured model family.

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
Workflows using `agent-run-summary` also print these keys as `Models used:`
below the report. Missing usage data is left unreported, not inferred from the
requested alias. The final prose report alone is not a model/version record.

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
3. Before the agent step, add the shared CLI setup:
   ```yaml
   - name: Set up latest Claude Code
     id: setup-claude-code
     uses: ./.github/actions/setup-claude-code
   ```
4. On `anthropics/claude-code-action`, set
   `path_to_claude_code_executable: ${{ steps.setup-claude-code.outputs.executable }}`
   and use `--model ${{ env.AGENT_MODEL }}` in `claude_args`.

For a matrix workflow, follow the scanner's `setup` job pattern instead: add a
`matrix:` list, call the resolver with `--matrix`, and pass `matrix.model`.

`tests/test_agent_config.py` enforces the contract: every `workflows:` key maps
to a real workflow file that uses the composite action or matrix resolver, and
no workflow hardcodes a model inline. It also checks that every managed agent
uses the shared CLI setup and explicitly selects its executable.

## Scope and relationship to cron-profiles

This config covers the **AI model** only. Cron *cadence* stays in
[`.github/cron-profiles.yaml`](cron-profiles.md) because GitHub cannot
parameterize `schedule:` at run time. Per-workflow enable/disable and a provider
abstraction (`provider:` is reserved but not yet consumed) are planned follow-ups
under issue #5218.

`claude.yml` (the `@claude` mention responder) is also managed here (`claude:`
key → `opus`); it resolves `AGENT_MODEL` via the same
`resolve-agent-config` step and passes `--model ${{ env.AGENT_MODEL }}` in
`claude_args`, so its model lives in this file like every other agentic workflow.
