# Cron cadence profiles for scheduled workflows

The scheduled "agent" GitHub Actions (curation scanner, PR shepherd, literature
scan, weekly compliance, …) each hard-code their `cron:` schedules inline.
Tuning them used to mean hand-editing several workflow files and remembering the
weekday/weekend split conventions. This is now driven from a single source of
truth.

## Quick start

```bash
just cron-profiles                 # list profiles, show the active one
just cron-profile-preview fast     # dry-run: show the diff, write nothing
just cron-profile fast             # apply 'fast' to all workflows + commit
git push -u origin <branch>        # publish (the apply step does not push)
```

## How it works

* **`.github/cron-profiles.yaml`** — the config. It defines named `profiles:`
  and an `active:` pointer. Each profile lists every managed workflow and either
  the exact cron entries it should have (with optional inline comments) or an
  empty list to remove that workflow's scheduled trigger.
* **`scripts/apply_cron_profile.py`** — the applier. It rewrites *only* each
  workflow's `on.schedule` block and updates `active:` in the config. Profiles
  with cron entries replace or add the block; empty workflow lists remove it.
  Everything else (workflow_dispatch inputs, jobs, comments outside the schedule
  block) is left untouched. The rewrite is line-based on
  purpose — round-tripping a workflow through a YAML dumper corrupts GitHub's
  `on:` key (YAML 1.1 parses it as the boolean `true`).

Each rewritten file is re-parsed as a sanity check, and the applier refuses to
run if any profile is missing a managed workflow (so a profile can't be
half-configured).

## The profiles

| Profile | Intent |
| --- | --- |
| `slow` | Conservative cadence — minimise API/compute spend. |
| `medium` | Baseline — mirrors the historical live schedules. |
| `fast` | Aggressive cadence — maximise responsiveness. |
| `fast-weekend` | Weekday cadence at the `medium` level, weekend boosted. |
| `off` | Kill switch — no scheduled agent runs at any time (manual dispatch still works). |

`medium` reproduces the cadence the repo ran historically, so applying it is
behaviour-preserving (cosmetic normalisation only). `slow`/`fast` dial the
high-frequency agents (curation scanner, PR shepherd, discussion scanner)
down/up. The low-frequency weekly/daily jobs (literature-scan,
knowledge-gap-scan, preprint-scan, weekly-compliance, stale-pr-reassign,
post-review-agent) are
intentionally the same across all profiles — they are not the cost driver. Edit
them in the config if you want a profile to move them too.

`off` disables *every* managed workflow's schedule at once by removing the
`on.schedule` block from each managed workflow. `workflow_dispatch` is untouched,
so you can still run any agent by hand from the Actions tab while `off` is
active. To turn the agents back on, apply another profile
(`just cron-profile medium`), and the applier will reinsert the schedule blocks.

Do not use impossible calendar dates such as February 30 as a "never" cron.
GitHub Actions may ignore invalid cron updates and keep the workflow's previous
valid schedule registered.

## Adding or editing a profile

Edit `.github/cron-profiles.yaml`. To add a profile, copy an existing block and
adjust the cron entries; every managed workflow must be present. Use an empty
list (`workflow-name: []`) only when that profile intentionally disables that
workflow's scheduled trigger. Weekday/weekend splits use two entries — `… 1-5`
(Mon–Fri) and `… 0,6` (Sun/Sat) — while a single entry runs every day. Preview
before committing:

```bash
just cron-profile-preview <name>
```

## Managed workflows

`curation-scanner`, `pr-shepherd`, `discussion-scanner`, `literature-scan`,
`knowledge-gap-scan`, `preprint-scan`, `weekly-compliance`, `stale-pr-reassign`,
`post-review-agent`.

The page/build crons (`generate-grouping-pages`, `generate-project-pages`,
`deploy-docs`, `kgx-release`, `pypi-publish`) are deliberately **not** managed —
they are derived-artifact builds, not agent cost.
