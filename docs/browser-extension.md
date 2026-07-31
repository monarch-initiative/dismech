# dismech curator (browser extension)

A small Manifest V3 Chrome/Edge extension that turns the paper or disease page
you are looking at into a dismech curation **GitHub issue** — one click, like a
"send to dismech" bookmarklet. It lives in [`extension/`](https://github.com/monarch-initiative/dismech/tree/main/extension).

## What it does

When you are on a recognized page and click the toolbar button, the extension
reads the page's identifiers and metadata (never sending the page anywhere),
picks the right issue template, and lets you review and file the issue.

- **Papers** (PubMed, PMC, `doi.org`, bioRxiv/medRxiv, most publisher pages
  that emit `citation_*` meta tags) → a *"Curate from literature"* issue with the
  PMID/DOI/PMCID, journal, authors, and a curation checklist that reminds the
  curator to use **exact-quote** snippets and `just fetch-reference`.
- **Diseases** (Monarch, OMIM, Orphanet, OLS/`purl.obolibrary.org` MONDO pages) →
  a *"Curate <label> (MONDO:…)"* issue mirroring the
  [`claim-disease`](https://github.com/monarch-initiative/dismech/tree/main/.claude/skills/claim-disease)
  template, linked to the priority tracker (#1079).
- Any text you have **highlighted** on the page is captured into the issue as a
  blockquote.

## Two ways to file

Set in the extension's **Settings** page:

1. **Pre-filled issue form (default, no token).** Opens GitHub's
   `issues/new?title=…&body=…&labels=…` for `monarch-initiative/dismech`. You are
   already signed in to GitHub, so you just review and click *Submit*. Nothing
   but opening a URL — no credentials, no backend.
2. **One-click with a token.** Store a fine-grained GitHub PAT (Issues: read &
   write on the target repo, ideally with a short expiry) in the browser; the
   extension POSTs to `api.github.com` directly and opens the new issue. The
   token stays in `chrome.storage.local` — **plaintext on disk** — and is sent
   only to GitHub. If you would rather not persist a token, prefer the default
   form mode above, which needs no credentials. Selecting token mode on the
   Settings page requests the optional `api.github.com` host permission there
   (a stable context), so the popup only needs to check it at create time.

Owner/repo, labels, and the tracker issue number are all configurable, so the
extension also works against a fork or a different Monarch repo.

## Install (unpacked)

The extension is not (yet) on the Chrome Web Store, so you install it "unpacked"
from a local copy of the
[`extension/`](https://github.com/monarch-initiative/dismech/tree/main/extension)
directory. "Load unpacked" wants a **folder on your disk that contains
`manifest.json`** — so first get that folder, then point the browser at it.

### Option A — download the packaged zip (recommended)

No clone, no repo checkout:

1. Download `dismech-curator-<version>.zip` from the
   [latest release](https://github.com/monarch-initiative/dismech/releases/latest)
   (**Assets** section). If a release doesn't have the asset yet, see Option B or
   build it yourself with `just package-extension`.
2. **Unzip it** anywhere — it expands to a `dismech-curator-<version>/` folder
   containing `manifest.json`.
3. Open `chrome://extensions` (or `edge://extensions`) → enable **Developer
   mode** (top-right toggle) → **Load unpacked** → select the unzipped folder.
4. Pin *dismech curator*, open a paper/disease page, and click the toolbar icon.

You can also grab the zip from the **Package browser extension** GitHub Actions
run (it's uploaded as a workflow artifact on every `extension/` change), or build
it locally:

```bash
just package-extension      # writes dist/dismech-curator-<version>.zip
```

### Option B — from a repository checkout

GitHub can't download a single subfolder from the web UI, so you take the whole
repo and point at the subfolder:

1. On the [repo page](https://github.com/monarch-initiative/dismech), **Code →
   Download ZIP** and unzip it (or `git clone` if you prefer).
2. `chrome://extensions` → **Developer mode** → **Load unpacked** → select the
   `extension/` **subfolder** (the one containing `manifest.json`), *not* the
   repo root.
3. Pin it and click the toolbar icon on a paper/disease page.

After a `git pull`, click **Reload** under the extension card to pick up changes.

## Permissions

`activeTab` + `scripting` (read the current tab only when you click),
`storage` (settings), and the **optional** host permission
`https://api.github.com/*` (requested only if you turn on token mode).

## Development

Pure vanilla JS — no build step. Logic that can be unit-tested lives in
[`extension/issue.js`](https://github.com/monarch-initiative/dismech/tree/main/extension/issue.js)
(issue templates) and [`extension/extract.js`](https://github.com/monarch-initiative/dismech/tree/main/extension/extract.js)
(page metadata extraction). Run the tests with:

```bash
just test-extension   # or: node extension/test/run.mjs
```

These run in CI (`just test-extension`) whenever anything under `extension/`
changes.

Toolbar icons are generated (teal medical disc + cross) by
`python3 extension/icons/gen_icons.py`.
