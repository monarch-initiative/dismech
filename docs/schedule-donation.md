# Donate Your Instance to Curation (`/donate-curation`)

This is a plain-language guide to `/donate-curation` — a way to lend your Claude Code
instance to dismech disease curation during hours you choose (for example, every
evening while you're away from your desk). You say *when*; it does the curating.

You do **not** need to understand cron, UTC, or the code to use it. If you can
type a sentence like "8pm to midnight every weekday", you can run it.

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

## Before your first run (one-time)

You need to be signed in to GitHub in your terminal. Check with:

```bash
gh auth status
```

If that shows you're logged in, you're ready. (If not, run `gh auth login` and
follow the prompts.)

---

## The four things you can type

Type these in Claude Code while you're in the dismech project.

| You type | What happens |
|---|---|
| `/donate-curation` | Runs **once, right now.** Good for trying it out. |
| `/donate-curation 8pm-12am every weekday` | Sets up a **recurring** evening shift. |
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

Once set up, the shift runs in Anthropic's cloud on **your own subscription** —
your computer does **not** need to be awake or even switched on. Each evening in
your window, it wakes up, checks GitHub, and does exactly one thing: either
finish something that needs its attention, or start one new disease. Anything it
finishes is left for a reviewer; you'll see the proposals pile up on GitHub, get
reviewed, and merge on their own over the following days.

If it ever runs out of its usage allowance mid-task, it stops cleanly and saves
its place. The next evening it simply picks up where it left off.

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
- **To stop entirely:** type `/donate-curation stop`. In-progress work is allowed to
  finish saving; nothing is thrown away.
- **To remove it completely** (an extra, optional step): `/donate-curation stop` turns
  the shift *off*; to delete it from your account outright, open
  <https://claude.ai/code/routines> in a browser and remove it there. Claude
  will print that link for you.

---

## Frequently asked

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

The everyday commands above — the one-off `/donate-curation`, `status`, and `stop`, and
the GitHub check-in logic — work today. The **recurring cloud shift** has one
remaining setup step: a single test run in the cloud to confirm the curation
tools are all present there and that one disease fits in a session. Until that
test run is signed off, set up recurring shifts with a short "stop after" (e.g.
`for 1 day`) and check the results, rather than leaving a long unattended
schedule running.

For the technical details behind all of this — the exact scheduling API, the PR
classification rules, and the frozen instructions each cloud run follows — see
the `donate-curation` skill definition
(`.claude/skills/donate-curation/SKILL.md`) and issue
[#11657](https://github.com/monarch-initiative/dismech/issues/11657).
