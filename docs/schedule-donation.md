# Donate Your Instance to Curation (`/donate-curation`)

This is a plain-language guide to `/donate-curation` — a way to lend your Claude
Code instance to dismech disease curation during hours you choose (for example,
every evening while you're away from your desk). You say *when*; it does the
curating.

You do **not** need to understand cron, UTC, or the code to use it. But there is
a short one-time setup, and the recurring version **cannot run at all** until you
do it — so start with **[Set-up you must do once](#set-up-you-must-do-once)**
below.

---

## What it actually does

Think of it as a volunteer shift you schedule for your Claude Code instance.

- It works on **one disease at a time.** It never juggles several at once.
- Each time it wakes up, it first **checks GitHub to see if anything it already
  started still needs its attention** — a reviewer asked for changes, a check
  failed, or a merge conflict appeared. If so, it fixes *that* and stops for the
  session.
- **Only when nothing it started needs work** does it pick up a brand-new
  disease, research it, and open a new proposal (a "pull request", or PR — the
  unit of proposed change on GitHub).
- It **hands finished work off** and leaves it alone. Work waiting for a
  reviewer, or approved and just waiting for the automatic merge, does **not**
  hold up the next disease.

### What it will never do

By design, it never:

- **merges** its own work,
- **approves** its own work, or
- **dismisses** a reviewer's request for changes.

A human (or the reviewer bot) always stays in the loop for those. The worst it
can do is open proposals and improve them — never publish them unreviewed.

---

## Set-up you must do once

There are **three** things to set up before scheduling. The easiest way to do
all of them is to just type `/donate-curation` and let Claude walk you through
what's missing — but here's what each one is and why it's needed.

### 1. Sign in to GitHub

The tool acts on GitHub as *you*, so you must be signed in. Check with:

```bash
gh auth status
```

If it says you're logged in, you're set. If not, run `gh auth login` and follow
the prompts.

### 2. Tell it your GitHub username

This is a **safety catch**, and it matters most for the scheduled (cloud)
version. Each run only claims a new disease when *your* in-progress work is all
clear. If a scheduled run ever signed in as the wrong account (a robot account,
say), it would see an empty to-do list and wrongly start a brand-new disease
*every hour*. Recording your username stops that: a run that isn't signed in as
you does nothing at all.

You set this once in the settings file `/.claude/schedule-config.yaml`, on the
line:

```yaml
github_login: null      # change null to your GitHub username, e.g. jsmith
```

It ships blank on purpose — **your** username is personal to you and must never
be committed as a shared default. If you'd rather not edit the file by hand, ask
Claude: *"set my github_login in the schedule config"*.

### 3. Set up the cloud environment (required for scheduled shifts)

This is the one people miss. A **recurring** shift runs in Anthropic's cloud —
not on your Mac — so it needs a **cloud environment**: a ready-to-go copy of the
dismech project in the cloud, with the tools and sign-ins the curation work
needs. **Without one, a scheduled shift cannot start.**

- If you already have a Claude Code cloud environment for dismech, put its id on
  the `environment_id:` line of `/.claude/schedule-config.yaml`.
- If you don't, create/connect one from the Claude Code cloud area at
  <https://claude.ai/code>, then copy its id into that line.
- Not sure? Ask Claude: *"help me set up the cloud environment for scheduling"* —
  it will point you at the right place and, when you register a shift, prompt you
  for the id if it's still blank.

Like your username, this line ships blank so nobody inherits one person's
environment by accident.

> **The run-once version needs only step 1.** Typing `/donate-curation` with no
> schedule runs immediately in your *current* session (not the cloud), so it
> needs GitHub sign-in but no cloud environment. Steps 2 and 3 are what unlock
> the recurring, unattended shifts.

---

## The four things you can type

Type these in Claude Code while you're in the dismech project.

| You type | What happens |
|---|---|
| `/donate-curation` | Runs **once, right now**, in this session. Good for trying it out (needs only step 1). |
| `/donate-curation 8pm-12am every weekday` | Sets up a **recurring** cloud shift (needs steps 1–3). |
| `/donate-curation status` | Shows what's scheduled and what it's working on. |
| `/donate-curation stop` | Ends the recurring shift. |

### Saying *when* (the recurring form)

You describe three things in plain words — the daily **window**, how **often**,
and (optionally) when to **stop**:

- **Window** — "8pm to midnight", "9am–5pm".
- **How often** — "every day", "every weekday", "weekends", or "once".
- **Stop after** (optional) — "for 1 week", "for 3 days", "until 2026-10-01". If
  you leave this off, it keeps running until you stop it.

Examples you can type as-is:

- `/donate-curation 8pm-12am every weekday`
- `/donate-curation 9am-11am every day for 2 weeks`
- `/donate-curation 8pm-11pm weekends until 2026-12-31`
- `/donate-curation 8pm-9pm once` (just tonight — see below)

"Once" (or "tonight") does **not** mean a single wake-up at 8pm. It means the
instance takes its shift **tonight only** — waking each hour across the window
just like a recurring shift, then switching itself off the next day. It's the
right choice for a one-evening trial.

Claude will read back the schedule it understood — including the exact clock
times, adjusted for daylight-saving — and ask you to confirm before setting
anything up. **Always glance at that read-back;** the time-zone conversion is
the one thing worth double-checking.

---

## What a scheduled shift looks like

Once set up, the shift runs in the cloud on **your own subscription** — your
computer does **not** need to be awake or even switched on. Each evening in your
window, it wakes up, checks GitHub, and does exactly one thing: either finish
something that needs its attention, or start one new disease. Anything it
finishes is left for a reviewer; you'll see the proposals pile up on GitHub, get
reviewed, and merge on their own over the following days.

If it ever runs out of its usage allowance mid-task, it stops cleanly and saves
its place. The next evening it simply picks up where it left off.

**The very first scheduled run is a test run.** Before trusting the nightly
rhythm, the tool does one cloud run to confirm the environment really has
everything the curation work needs. Until that test run is signed off, keep the
schedule short (e.g. `once`, or `for 1 day`) and check the result.

---

## Checking in on it

```
/donate-curation status
```

This tells you the schedule (window, how often, stop date) and the one thing
currently in hand — whether it's researching a disease, waiting on a reviewer,
or waiting to be merged.

---

## Changing or stopping it

- **To change the hours or frequency:** just type a new `/donate-curation <window> ...`
  — it replaces the old shift.
- **To stop entirely:** type `/donate-curation stop`. In-progress work is allowed
  to finish saving; nothing is thrown away.
- **To remove it completely** (an extra, optional step): `/donate-curation stop`
  turns the shift *off*; to delete it from your account outright, open
  <https://claude.ai/code/routines> in a browser and remove it there. Claude
  will print that link for you.

---

## Frequently asked

**Why does it need my GitHub username?**
As a safety catch. A scheduled run only starts a new disease when your
in-progress work is clear — so if it ever ran signed in as the wrong account, it
could misread an empty list and start new work every hour. Recording your
username means a run that isn't you does nothing.

**What is a "cloud environment" and why do I need one?**
It's a ready-made copy of the dismech project that lives in the cloud, with the
tools and sign-ins the curation needs. Recurring shifts run there (so your Mac
can be off), and they can't start without one. The run-*now* version doesn't
need it — it uses your current session.

**Will it curate a disease I don't know anything about?**
It picks from the shared queue of diseases waiting to be curated. Every proposal
it opens goes through the normal review before anything is accepted.

**Can two evenings' runs collide and do the same disease twice?**
No. Each run checks first, and if the previous night's run is somehow still
going, the new one simply steps aside.

**Does this cost the project money / use an org account?**
No — it runs on *your* personal Claude subscription, not the project's. There's
no external service involved.

**How many diseases at once?**
Exactly one, in this first version. Doing several in parallel is a planned future
improvement, not something this version does.

---

## Status of this feature

The run-once command (`/donate-curation` with no schedule) and the GitHub
check-in logic work today. The **recurring cloud shift** depends on the one-time
set-up above — chiefly the cloud environment — plus the first test run
described earlier. Until you've done that set-up and seen a test run succeed,
prefer a short `once` / `for 1 day` schedule and check the results rather than
leaving a long unattended shift running.

For the technical details behind all of this — the exact scheduling API, the PR
classification rules, and the frozen instructions each cloud run follows — see
the `donate-curation` skill definition
(`.claude/skills/donate-curation/SKILL.md`) and issue
[#11657](https://github.com/monarch-initiative/dismech/issues/11657).
