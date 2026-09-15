# dismech curator — browser extension

A Manifest V3 Chrome/Edge extension: when you're on a **paper** or **disease**
page, click the toolbar button to file a pre-filled dismech curation **GitHub
issue**. Think "send to dismech" — Paperpile-style, but the destination is a
curation issue in `monarch-initiative/dismech`.

Full docs: [`docs/browser-extension.md`](../docs/browser-extension.md).

## Quick start

1. **[Download dismech-extension.zip](https://dismech.monarchinitiative.org/elements/downloads/dismech-extension.zip)**
   to your computer. This GitHub page is source code; visiting it does not download
   the extension. No Git or terminal is needed.
2. Extract the ZIP: **Mac:** double-click in Finder. **Windows:** right-click →
   **Extract All…**. Find the **dismech-extension** folder containing
   `manifest.json` (Windows may put it inside another folder of the same name).
   Move that folder to **Documents** and keep it there while installed.
3. Paste `chrome://extensions` into Chrome's address bar (Edge:
   `edge://extensions`), press Enter, and enable **Developer mode**.
4. Click **Load unpacked** → **Documents** → select **dismech-extension** →
   **Select** / **Select Folder**. Choose the folder containing `manifest.json`,
   not the ZIP or an individual file. A **dismech curator** card should appear.
5. Pin **dismech curator** from the browser's Extensions (puzzle-piece) menu.
   Open a paper (PubMed / DOI / bioRxiv) or disease page (Monarch / OMIM /
   Orphanet), click the curator icon, review, and **Create issue**.

[Full installation guide and troubleshooting](https://dismech.monarchinitiative.org/elements/browser-extension/#install-unpacked).
If you already have a local checkout, you can load its `extension/` folder
directly; no build step is needed.

By default it opens GitHub's pre-filled issue form (no token needed). Optionally
add a fine-grained PAT in **Settings** for true one-click creation via the API.

## Recognized pages

| Kind | Detected via |
|------|--------------|
| Paper | `citation_pmid` / `citation_doi` / `citation_pmcid` meta tags; `pubmed.ncbi.nlm.nih.gov/<pmid>`; `doi.org/10.…`; `PMC…` in URL; `dc.identifier`/`prism.doi` |
| Disease | `MONDO:`/`MONDO_` in URL; `omim.org/entry/<id>`; `ORPHA:`/`Orphanet_`/`orpha.net/en/disease/detail/<id>`/legacy `orpha.net?Expert=`; `DOID:` |

Falls back to an *unknown* "curation lead" issue capturing the URL, title, and
any highlighted text.

## Files

| File | Role |
|------|------|
| `manifest.json` | MV3 manifest (`activeTab`, `scripting`, `storage`; optional `api.github.com` host) |
| `extract.js` | Injected into the active tab; scrapes identifiers + metadata |
| `issue.js` | Pure issue-template builder (unit-tested; no DOM/chrome) |
| `popup.html/.css/.js` | Toolbar popup: preview & edit the issue, then create |
| `options.html/.js` | Settings: repo, labels, tracker, URL-vs-token mode, PAT |
| `icons/` | Generated PNG icons + `gen_icons.py` generator |
| `test/run.mjs` | `node extension/test/run.mjs` — extractor + template tests |

## Develop

No build step. After edits, reload the extension from `chrome://extensions`.

```bash
just test-extension                    # run tests (or: node extension/test/run.mjs)
python3 extension/icons/gen_icons.py   # regenerate icons
```

CI runs `just test-extension` whenever `extension/` changes.

## Privacy

The page is read locally only when you click the button (`activeTab`). In
default mode nothing leaves your machine except opening a GitHub URL. In token
mode, the issue is sent only to `api.github.com`; the token is stored in
`chrome.storage.local`.

## Download packaging

MkDocs builds the ZIP from the runtime files using
`scripts/package_extension.py`. Run `python3 scripts/package_extension.py` to
produce `docs/downloads/dismech-extension.zip` locally. The archive contains a
`dismech-extension` folder and excludes tests and development scripts.
