# Preprint scanning & full-text retrieval — empirical findings

Spike for a possible "preprint-scan" action, sibling to the literature-scan /
knowledge-gap-scan (kgscan) workflows. All numbers below were verified against
live services on 2026-06-28; see `scripts/preprint_fulltext_prototype.py` for the
working full-text fetcher.

## Question

Should dismech have a scanner like kgscan that covers preprints, and can we get
preprint **full text** (not just abstracts) for curation?

## The two preprint universes

The existing scanners query **Europe PMC `SRC:MED`** (PubMed/MEDLINE), which
excludes preprints. Preprints live in two distinct places that behave very
differently:

| | Europe PMC `SRC:PPR` | PubMed `"preprint"[Publication Type]` |
|---|---|---|
| Volume | 99,188 in 2026 alone | 64,055 total; 10,112 in 2026 |
| PMIDs | **none** (DOI-only, 0/500 sampled) | **yes** — real PMIDs (NIH Preprint Pilot) |
| Source | bioRxiv/medRxiv/Research Square/openRxiv | medRxiv/bioRxiv/arXiv, NIH-funded subset |
| Fits dismech PMID pipeline | no (needs DOI fetch path) | **yes** (`fetch-reference PMID:` works as-is) |

The existing `SRC:MED` scanners catch **none** of these
(`SRC:MED AND PUB_TYPE:preprint` = 0). So a preprint scanner is genuinely
additive, not a duplicate.

A PMID-route scanner (PubMed eutils, `"preprint"[Publication Type]`) is the
cleanest fit: every candidate is PMID-addressable and snippet-validatable by the
existing anti-hallucination stack, and the `Preprint` pubtype self-labels them as
not-yet-peer-reviewed.

## Full text: where it is and isn't

**Abstracts:** 100% available for every preprint PMID via PubMed efetch
(1,300–2,200 chars). Sufficient for the existing abstract-quote curation flow.

**Full-text body — routes tested:**

1. **PMC / Europe PMC APIs — mostly NOT the body.**
   - Only ~7% of preprint PMIDs have a PMCID, and even those PMC records contain
     `['ABSTRACT', 'SUPPL', 'TITLE']` sections only — no article body.
   - Europe PMC's REST `/{src}/{id}/fullTextXML` **404s for all preprints**, even
     the 60,098 flagged `HAS_FT:Y` / `inEPMC=Y`.

2. **Europe PMC `fulltextRepo` PDF — WORKS NOW (primary route).**
   - Each `SRC:PPR AND HAS_FT:Y` core record's `fullTextUrlList` carries a direct
     Europe-PMC-hosted PDF URL (`/api/fulltextRepo?pprId=...`). Downloads openly —
     no AWS, no Cloudflare. Verified: 3.5 MB / 24 pp and 0.94 MB / 36 pp PDFs →
     `pypdf` → 23–28k chars of real methods/results body text.
   - Caveats: only the EPMC-ingested subset (the newest openRxiv 2026 preprints,
     DOI prefix `10.64898`, are not in EPMC yet); a minority of records return a
     stale-filename error blob, so callers must validate `%PDF-` magic; output is
     PDF text (whitespace/hyphenation noise) not clean JATS, which matters for the
     exact-substring snippet validator.

3. **openRxiv S3 TDM bucket — bulk fallback, needs credentials.**
   - `s3://biorxiv-src-monthly/` and `s3://medrxiv-src-monthly/` are
     requester-pays MECA archives (JATS XML + PDF) — the sanctioned bulk channel,
     covering ALL bioRxiv/medRxiv incl. the freshest openRxiv content as clean
     JATS. Bucket existence confirmed (`403 AccessDenied`, not `NoSuchBucket`).
   - Not exercised here: the spike environment's AWS key is rejected
     (`InvalidAccessKeyId`). Also not DOI-addressable — monthly MECA dumps require
     a prefix sync + DOI→key index. Coded as a documented stub.

4. **Direct bioRxiv/openRxiv `.full.pdf` URLs — not viable for automation.**
   - Real and open to a browser, but behind a Cloudflare "Just a moment..." bot
     challenge (verified 403 challenge page, `server=cloudflare`). GitHub Actions
     datacenter IPs get challenged. Deliberately omitted.

## Migration note

bioRxiv/medRxiv moved to **openRxiv** (Crossref `publisher: openRxiv`, new DOI
prefix `10.64898`). This is why many 2026 preprints carry non-`10.1101` DOIs and
are not yet in PMC/Europe PMC.

## Recommendation

- **Scanner:** build the PubMed PMID route (`"preprint"[Publication Type]`),
  leads-only, `preprint` label — abstracts are universal and pipeline-native.
- **Full text:** use the Europe PMC `fulltextRepo` PDF route as the pragmatic 80%
  (`scripts/preprint_fulltext_prototype.py`); treat S3 JATS as phase 2 for full
  openRxiv coverage and cleaner snippet validation, once requester-pays creds are
  wired into the Action as secrets.
- **Evidence policy:** record the preprint stance in
  `docs/explanation/design-decisions.md` §6 — preprints are not peer-reviewed and
  should not be the sole support for a mechanism claim.
