# dismech curator — browser extension

A Manifest V3 Chrome/Edge extension: when you're on a **paper** or **disease**
page, click the toolbar button to file a pre-filled dismech curation **GitHub
issue**. Think "send to dismech" — Paperpile-style, but the destination is a
curation issue in `monarch-initiative/dismech`.

Full docs: [`docs/browser-extension.md`](../docs/browser-extension.md).

## Quick start

1. Open `chrome://extensions`, enable **Developer mode**.
2. **Load unpacked** → pick this `extension/` folder.
3. Open a paper (PubMed / DOI / bioRxiv) or disease page (Monarch / OMIM /
   Orphanet), click the *dismech curator* icon, review, and **Create issue**.

By default it opens GitHub's pre-filled issue form (no token needed). Optionally
add a fine-grained PAT in **Settings** for true one-click creation via the API.

## Recognized pages

| Kind | Detected via |
|------|--------------|
| Paper | `citation_pmid` / `citation_doi` / `citation_pmcid` meta tags; `pubmed.ncbi.nlm.nih.gov/<pmid>`; `doi.org/10.…`; `PMC…` in URL; `dc.identifier`/`prism.doi` |
| Disease | `MONDO:`/`MONDO_` in URL; `omim.org/entry/<id>`; `ORPHA:`/`Orphanet_`/`orpha.net?Expert=`; `DOID:` |

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
node extension/test/run.mjs        # run tests
python3 extension/icons/gen_icons.py   # regenerate icons
```

## Privacy

The page is read locally only when you click the button (`activeTab`). In
default mode nothing leaves your machine except opening a GitHub URL. In token
mode, the issue is sent only to `api.github.com`; the token is stored in
`chrome.storage.local`.
