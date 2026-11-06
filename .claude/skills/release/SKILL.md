---
name: release
description: Use when cutting a new DisMech GitHub release (a `v0.1.x` tag) — the action that rebuilds every bulk export and refreshes the Downloads page. Covers the mandatory origin/main sync, the version convention, the draft→review→publish order, every asset workflow that fires on publish (KGX JSONL+TSV, Mondo EMC, kb/pathographs/cx2/omex archives, manifest, maximal KGX), what the separate NDEx step does, and how the self-updating Downloads page consumes it.
---

# release

Cut a DisMech release. A release is a GitHub release on a `v0.1.x` tag. Publishing
it is what rebuilds the bulk exports and makes the Downloads page
(`https://dismech.monarchinitiative.org/downloads/index.html`) point at the new
files. There is no local build step and no version string to edit — the tag is
the version (`uv-dynamic-versioning`, `pyproject.toml`).

## When to use

- The user asks for a "fresh release", a version bump, or to refresh the
  Downloads page / bulk exports.
- New release artifacts have been added and need to ship.

Not for: NDEx publishing alone (that is a separate manual workflow, below), the
PyPI package in isolation (a release publishes it as a side effect), or the
website page build (the page is static and self-updating — see below).

## The one trap: never release from a stale checkout

The primary checkout drifts tens or hundreds of commits behind `origin/main`
between releases. A release tags a commit, so **always sync first** and tag
`origin/main`'s tip, never the local tip.

```bash
git fetch origin main
git rev-list --left-right --count main...origin/main   # expect "0  N": 0 local-ahead, N behind
```

If there are **0** local-ahead commits, fast-forward the primary checkout (it
must stay on `main`; the reflog makes this reversible):

```bash
# First confirm no untracked file collides with an incoming added file:
comm -12 <(git ls-files --others --exclude-standard | sort) \
         <(git diff --name-only --diff-filter=A main origin/main | sort)
# If that prints nothing, fast-forward:
git merge --ff-only origin/main
```

If the count shows local-ahead commits, stop and ask — do not force anything.
Either way, you can sidestep drift entirely by pinning the tag to an explicit
SHA with `--target <sha>` below.

## Pick the version

Next in sequence after the latest tag. These are plain increments, `v0.1.N`.

```bash
gh release list --limit 3          # read the latest tag, add 1 to the patch number
gh release view vX.Y.Z             # confirm the chosen tag does NOT already exist ("release not found")
```

## Draft, review, publish — in that order

**Draft first.** A draft creates no git tag and fires no workflow, so it is
fully reversible. `--target main` ties the (future) tag to main's tip; pass a
SHA instead if main may move before you publish.

```bash
gh release create vX.Y.Z --target main --draft --generate-notes --title "vX.Y.Z"
```

The URL comes back as `.../releases/tag/untagged-...` — that `untagged-` prefix
confirms no tag exists yet. Review the generated notes:

```bash
gh release view vX.Y.Z --json isDraft,tagName,targetCommitish,body
```

**Publish only on the user's explicit say-so.** Publishing is irreversible and
public: it creates the tag, publishes to PyPI, and triggers every asset
workflow. Mark it latest (not prerelease) or the Downloads page will not pick it
up — the page reads `releases/latest`, which the GitHub API resolves to the most
recent *published, non-prerelease* release.

```bash
gh release edit vX.Y.Z --draft=false --latest
```

To abandon a draft instead: `gh release delete vX.Y.Z`.

## What publishing fires (all on `release: published`)

Four independent workflows attach assets; a failure in one does not hold back
the others. Watch them:

```bash
gh run list --event release --limit 12
```

| Workflow | Assets attached |
|---|---|
| `pypi-publish.yaml` | the package to **PyPI** (a bare tag push with no release does **TestPyPI** only) |
| `kgx-release.yaml` | `dismech_nodes.jsonl`, `dismech_edges.jsonl`, `dismech_nodes.tsv`, `dismech_edges.tsv`, `dismech_sepio.jsonl`, `dismech_kgx_metadata.json` |
| `mondo-emc-release.yaml` | `mondo_emc.tsv` |
| `release-assets.yaml` | `kb.zip`, `pathographs.zip`, `pathographs_cx2.zip`, `dismech_models_omex.zip`, `release_manifest.json`, and the experimental `dismech_maximal_nodes.jsonl` / `dismech_maximal_edges.jsonl` / `dismech_maximal_metadata.json` |

The asset builders are `python -m dismech.export.release_assets <subcommand>` and
`python -m dismech.export.maximal_kgx_export`; the KGX pipeline lives in
`kgx-release.yaml`. When a new artifact is added, it is added to one of these
workflows and to the Downloads page table (`downloads/index.html`) — both, or
the page will show it as "not in this release".

**NDEx is separate and manual.** `publish-ndex.yml` is a `workflow_dispatch`; it
does not fire on release. Run it only when asked, and only after the CX2 archive
exists.

## The Downloads page needs no edit

`downloads/index.html` is static and self-updating. Every asset link already
points at `/releases/latest/download/<name>`, and a small script fetches
`api.github.com/repos/monarch-initiative/dismech/releases/latest` on load to fill
in the tag, date, and each file's size. So:

- Cutting a release requires **no change to the page**.
- A **draft** does not change the page (a draft is not "latest").
- After **publishing**, the page flips to the new release, but the size cells
  read "not in this release" and the direct links 404 until each asset workflow
  has finished uploading. Verify by loading the page, or:

```bash
gh release view vX.Y.Z --json assets -q '.assets[].name'   # all expected files present?
```

## Verify when done

- All four workflows green (`gh run list --event release`).
- Every expected asset name attached to the release.
- The Downloads page shows the new tag, a date, and real sizes (not em-dashes).
- `pip install dismech==X.Y.Z` resolves on PyPI (package publish can lag a few minutes).
