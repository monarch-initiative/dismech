# The Life of a Change

A change you make to DisMech does not go live when your pull request merges. It
goes live when a *second*, automatically generated pull request merges, and then
a third process rebuilds the website. Nothing in that chain needs you, but none
of it is visible from your own PR, which makes the usual question — *my PR
merged an hour ago, where is my page?* — surprisingly hard to answer from the
outside.

This page is the map. It covers the stable skeleton only: what the hops are, who
performs each one, roughly how long each takes, and where your work ends up. For
the mechanics of any individual hop, see
[Automation & Agents](automation-and-agents.md); for the disorder page build
specifically, see [Page Build](../page-build.md).

## The five hops

```
you curate  →  your PR  →  merge queue  →  regen PR  →  Pages build  →  live
   local      AI review     tests against   bot-authored   GitHub rebuilds
   gates      + your fixes   latest main    and approved    the site
```

### 1. You curate, and the local gates run

Curation happens on a branch in this repository — **not a fork**. GitHub does not
expose repository secrets to workflows triggered from a fork, so a fork PR gets
no automated review and simply sits there. If you do not have push access, open
an issue asking for it.

The fast loop after each file edit:

```bash
just validate kb/disorders/MyDisease.yaml
just count-verified-snippets kb/disorders/MyDisease.yaml
just validate-terms kb/disorders/MyDisease.yaml
```

Then once, before you open the PR, the batched sweep that CI itself runs:

```bash
just validate-disorders kb/disorders/MyDisease.yaml
```

Everything here is seconds-to-minutes and entirely in your hands. See
[Quality Control & Compliance](../quality-control.md) for the full gate set.

### 2. Your PR is reviewed

Opening the PR triggers an AI reviewer, which usually posts within a few
minutes. It either approves or requests changes, and it reads the actual files
rather than only the diff.

Two things about this hop surprise people:

- **Every push drops an existing approval.** The `main` branch has
  `dismiss_stale_reviews` enabled, so a two-line typo fix costs exactly the same
  review cycle as a rewritten pathophysiology section. Gather the whole round —
  blocking findings, the optional suggestions you intend to take, the
  `history/` record, any housekeeping the round exposed — and push it **once**.
- **A "changes requested" verdict is sticky.** Pushing a fix does not clear it;
  only a new review does. Branch protection auto-dismisses stale *approvals*,
  not stale rejections.

Expect one or two rounds for a substantial entry. This is the hop whose duration
depends on you.

### 3. The merge queue

Once your PR is approved, green, conflict-free, targeting `main`, **more than
three days old**, and **not assigned to a person**, an hourly sweep enqueues it
and GitHub merges it. Assigning the PR to yourself holds it indefinitely — that
is the intended way to say "still working on this".

In practice this is the slowest hop and the one with the widest spread. The
queue re-tests each candidate against the latest `main`, serially, so your wait
depends on what else is queued ahead of you. A candidate can also be *ejected*
if something ahead of it fails; a single ejection is routine and it is simply
re-enqueued on the next sweep.

The three-day minimum is deliberate: it is the window in which a human can look
at agent-curated work before it lands.

### 4. The page regeneration PR

**This is the hop that is invisible from your PR, and it is where the confusion
lives.** Your merge does not touch any rendered page. Instead, merging to `main`
triggers a workflow that re-renders the affected pages, commits them to a
long-lived `auto/...` branch, opens its own pull request, approves it, and
enables auto-merge. That PR then goes through the merge queue like any other.

There are three such lanes, by content type:

| You changed | Workflow | Daily backstop (UTC) |
|---|---|---|
| `kb/disorders/`, `kb/comorbidities/`, `kb/modules/`, `models/`, `research/`, templates, `docs/` | `generate-pages.yaml` | 06:00 |
| `kb/groupings/` | `generate-grouping-pages.yaml` | 07:00 |
| `projects/*.md` | `generate-project-pages.yaml` | 07:30 |

The daily schedules matter more than they look. Rendered pages resolve disease,
module and grouping slugs against the corpus *at render time*, so a page can go
stale because of a change made somewhere else entirely — a disease renamed in an
unrelated PR, for instance. The scheduled runs absorb that drift without anyone
editing a file. They are also the backstop: if a regeneration run fails or its
PR gets superseded, the next day's run picks the change up, so the worst case is
a delay rather than a change that never appears.

A full `generate-pages.yaml` run takes roughly 30–60 minutes on its own, before
its PR reaches the queue.

### 5. GitHub Pages rebuilds

The site is served by GitHub Pages directly from the root of `main`, so once the
regeneration PR merges, Pages rebuilds and publishes within a few minutes. No
action, and nothing to watch.

## Where your work ends up

| Content | URL |
|---|---|
| Disorder | `https://dismech.monarchinitiative.org/pages/disorders/<Name>.html` |
| Grouping | `https://dismech.monarchinitiative.org/pages/groupings/<Name>.html` |
| Module | `https://dismech.monarchinitiative.org/pages/modules/<name>.html` |
| Model | `https://dismech.monarchinitiative.org/pages/models/<model_id>.html` |
| Project | `https://dismech.monarchinitiative.org/pages/projects/<SLUG>.html` |
| Browser app | `https://dismech.monarchinitiative.org/app/` |
| Documentation (this site) | `https://dismech.monarchinitiative.org/elements/<path>/` |

The slug is the filename without its extension, matching case exactly —
`kb/disorders/Asthma.yaml` becomes `pages/disorders/Asthma.html`, and
`projects/AOP_40_SKIN_SENSITIZATION.md` becomes
`pages/projects/AOP_40_SKIN_SENSITIZATION.html`.

Documentation is the exception: it is built by MkDocs rather than rendered from
YAML, so a page under `docs/` keeps its directory path, drops the `.md` and
gains a trailing slash — this page, `docs/explanation/change-lifecycle.md`, is
served at `/elements/explanation/change-lifecycle/`.

## A worked example, with real numbers

A project report added in PR
[#16305](https://github.com/monarch-initiative/dismech/pull/16305), on
2026-11-02:

| Event | Time (UTC) | Elapsed |
|---|---|---|
| PR merged | 13:23 | — |
| Regeneration PR [#16313](https://github.com/monarch-initiative/dismech/pull/16313) opened | 13:37 | +14 min |
| Regeneration PR merged | 15:07 | +1 h 44 min |
| Page live | ~15:10 | +1 h 47 min |

Nearly all of that was the regeneration PR waiting in the merge queue, not the
rendering. **Budget one to two hours from merge to live page, and treat anything
under four hours as normal if the queue is busy.** Those are also two full
merge-queue passes for one piece of work, which is worth knowing when you plan
a batch: five curation PRs do not cost five times the wait, because their
regeneration collapses into whichever `auto/...` PR is open at the time.

## If it seems stuck

Work backwards through the hops, and check the cheap thing first.

1. **Is your PR actually merged?** An approval is not a merge. It also needs to
   be green, conflict-free, unassigned, and three days old.
2. **Is it assigned to you?** That is a deliberate hold, and it is the single
   most common reason a finished PR sits.
3. **Did a regeneration PR open?** Look for an open or recently merged PR on the
   `auto/...` branch for your content type. If one is open, your change is in
   it, and it is waiting on the queue.
4. **Has a daily run happened since your merge?** If the push-triggered run was
   lost, the scheduled run will pick the change up. Check the times in the table
   above before concluding anything is broken.
5. **Is the page a 404 or stale?** A 404 means the regeneration has not landed.
   Content that is present but out of date usually means the page was rendered
   before your change, and the next scheduled run will refresh it.
6. **Is there a `🐑 PR Shepherd` comment on your PR?** This one is last
   because it is the least visible, not because it happens late. After two
   merge-queue ejections with no push in between, the shepherd stops
   re-enqueuing the PR and says so in a comment. The hold sets no label, no
   review and no assignee, so nothing else on the PR page shows it, and the PR
   still satisfies every condition in item 1. Any push to the branch clears the
   strike count.

Only after all six is it worth reading workflow logs.

## See also

- [Contributing to dismech](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md) — setup, tooling, and the pull request process
- [Automation & Agents](automation-and-agents.md) — review states, merge-queue
  mechanics, and the trust boundaries behind each workflow
- [Page Build: Full vs Incremental](../page-build.md) — how the disorder page
  build decides what to re-render
- [Curation Projects](../projects.md) — the `projects/*.md` format and its
  slug auto-linking
