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
   write on the target repo) in the browser; the extension POSTs to
   `api.github.com` directly and opens the new issue. The token stays in
   `chrome.storage.local` and is sent only to GitHub.

Owner/repo, labels, and the tracker issue number are all configurable, so the
extension also works against a fork or a different Monarch repo.

## Install (unpacked)

The extension is not (yet) on the Chrome Web Store — load it unpacked:

1. `chrome://extensions` → enable **Developer mode**.
2. **Load unpacked** → select the `extension/` directory.
3. Pin *dismech curator*, open a paper/disease page, and click it.

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
node extension/test/run.mjs
```

Toolbar icons are generated (teal medical disc + cross) by
`python3 extension/icons/gen_icons.py`.
