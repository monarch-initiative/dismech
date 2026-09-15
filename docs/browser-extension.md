# dismech curator (browser extension)

A small Manifest V3 Chrome/Edge extension that turns the paper or disease page
you are looking at into a dismech curation **GitHub issue** — one click, like a
"send to dismech" bookmarklet.

**[Download dismech curator (ZIP)](downloads/dismech-extension.zip)** ·
[Installation steps](#install-unpacked) ·
[Source code](https://github.com/monarch-initiative/dismech/tree/main/extension)

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

You need Chrome or Edge on a desktop computer. The extension is not yet on the
Chrome Web Store. Install it from the download below; no Git, terminal commands,
or repository checkout is needed. “Unpacked” means the folder you get after
extracting the ZIP file.

1. **[Download dismech-extension.zip](downloads/dismech-extension.zip)** and
   find it in your **Downloads** folder.
2. **Extract the ZIP:** on **Mac**, double-click it in Finder; on **Windows**,
   right-click it in File Explorer and choose **Extract All…**, then **Extract**.
   Open the extracted folder and find **dismech-extension**, containing
   `manifest.json`, `popup.html`, and an `icons` folder. Windows may put it inside
   another folder with the same name: use the inner folder containing those files.
3. **Move that dismech-extension folder to Documents** (or another permanent
   location). Keep it there while the extension is installed: the browser loads
   its files from this folder.
4. In a new browser tab, **paste `chrome://extensions` into the address bar**
   and press Enter. For Edge, use `edge://extensions`. Turn on **Developer mode**.
5. Click **Load unpacked**. In the folder picker, go to **Documents**, select
   **dismech-extension** (the folder containing `manifest.json`), and click
   **Select** / **Select Folder**. Select the folder, not the ZIP or an individual
   file. A **dismech curator** card should now appear on the extensions page.
6. Open the browser's **Extensions** menu (the puzzle-piece icon) and pin
   **dismech curator** to the toolbar. Open a PubMed paper, click the curator icon,
   review the preview, and choose **Create issue**. By default this opens a GitHub
   form for you to review and submit; sign in to GitHub if prompted.

The preview can take **1–2 seconds** to appear after clicking the toolbar icon
while the extension reads the page. Wait briefly before clicking again.

### If you are stuck in the folder picker

- **Only unrelated files in Downloads?** Click **Cancel**, then download and
  extract the ZIP using steps 1–3 above. Opening the source-code page on GitHub
  does not download the extension to your computer.
- **ZIP or files are greyed out?** That is expected: this dialog selects folders.
  Choose the extracted folder containing `manifest.json`.
- **“Manifest file is missing or unreadable”?** You selected the wrong folder.
  Open it in Finder/File Explorer and locate `manifest.json`; select its enclosing
  folder in **Load unpacked**.

### Updating

Download and extract a fresh ZIP, replace the files in your installed
**dismech-extension** folder, then click **Reload** on its card at
`chrome://extensions` (or `edge://extensions`). Unpacked installations do not
update automatically.

### If you already have the repository checked out

You can select the local repository's **extension** folder directly in
**Load unpacked**. It contains `manifest.json` and needs no build step. On Mac,
press **Command–Shift–G** in the folder picker to enter its full path, for example
`~/repos/dismech/extension`.

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
