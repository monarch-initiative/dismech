# Agent Model Config

`.github/agent-config.yaml` is the single source of truth for **which Claude
model backs each agentic workflow**. Before this config, the model was hardcoded
(and inconsistently) in ~8 workflow files, so a repo-wide model bump meant hand
editing each one. Now it is one edit (issue #5218).

## How it works

Each agent workflow resolves its model at run time via the composite action
[`.github/actions/resolve-agent-config`](https://github.com/monarch-initiative/dismech/tree/main/.github/actions/resolve-agent-config).
The action reads `agent-config.yaml`, resolves the effective model, and exports
it as the `AGENT_MODEL` environment variable for the following steps, which pass
it to `claude-code-action` as `--model ${{ env.AGENT_MODEL }}`.

Resolution order (highest priority first):

1. an explicit per-run override — a `workflow_dispatch` `model:` input, passed to
   the action as `model-override`;
2. the per-workflow `model:` in `agent-config.yaml`;
3. the top-level `default_model`.

So **scheduled runs use the config**; a manual dispatch may still pick a
different model from the dropdown (that selection overrides the config for that
run only).

## Changing a model

To change the model a workflow uses on its scheduled runs, edit its `model:` in
`.github/agent-config.yaml` — no workflow YAML changes needed. To bump every
workflow that has no explicit `model:`, change `default_model`.

```yaml
# .github/agent-config.yaml
default_model: claude-opus-4-8
workflows:
  literature-scan:
    model: claude-haiku-4-5-20251001
  pr-shepherd:
    model: claude-opus-4-8
  # ...
```

## The curation-scanner matrix

`curation-scanner` fans out across effort tiers in parallel, each tier bound to a
model and a GitHub label selector. Its full fan-out lives in `agent-config.yaml`
under a `matrix:` list; a `setup` job reads it with the resolver's `--matrix`
mode and feeds it to `strategy.matrix.include`:

```yaml
workflows:
  curation-scanner:
    matrix:
      - { effort: low_effort,    model: claude-haiku-4-5-20251001, selector: "..." }
      - { effort: medium_effort, model: claude-sonnet-4-6,         selector: "..." }
      - { effort: high_effort,   model: claude-opus-4-8,           selector: "..." }
```

## Adding a workflow

1. Add a `workflows.<stem>` entry with a `model:` (or a `matrix:`).
2. In the workflow, after checkout, add:
   ```yaml
   - name: Resolve agent config
     uses: ./.github/actions/resolve-agent-config
     with:
       workflow: <stem>
       model-override: ${{ inputs.model }}   # omit if no model input
   ```
3. Use `--model ${{ env.AGENT_MODEL }}` in the agent invocation.

`tests/test_agent_config.py` enforces the contract: every `workflows:` key maps
to a real workflow file that invokes the action, and no workflow hardcodes a
`--model claude-*` inline.

## Scope and relationship to cron-profiles

This config covers the **AI model** only. Cron *cadence* stays in
[`.github/cron-profiles.yaml`](cron-profiles.md) because GitHub cannot
parameterize `schedule:` at run time. Per-workflow enable/disable and a provider
abstraction (`provider:` is reserved but not yet consumed) are planned follow-ups
under issue #5218.

`claude.yml` (the `@claude` mention responder) intentionally leaves the model
unset and uses `claude-code-action`'s own default, so it is not managed here.
