# WHO ICTRP: citing trials that are not on ClinicalTrials.gov

dismech's `clinical_trials` block grew up around ClinicalTrials.gov. The `name`
slot holds an `NCT…` identifier, evidence resolves against the ClinicalTrials.gov
API, and there are 995 NCT identifiers across the knowledge base. A trial
registered anywhere else had nowhere to go.

The **WHO International Clinical Trials Registry Platform (ICTRP)** is the
umbrella over every primary registry — ChiCTR (China), ISRCTN, EUCTR, jRCT/UMIN
(Japan), CTRI (India), ANZCTR, IRCT, DRKS, PACTR, and the rest. One prefix
(`ICTRP:`) and one fetch path therefore cover all of them, and ICTRP publishes a
*normalized* record (the 24-element WHO Trial Registration Data Set), so a ChiCTR
record and an ISRCTN record cache to the same shape.

## Why ICTRP rather than ChiCTR directly

Fetching ChiCTR itself was considered and rejected. `chictr.org.cn` answers `405`
to a plain GET from outside China and publishes no documented API, while the
ICTRP record for the same trial is a plain `GET` away. Supporting one registry at
a time would also mean writing a new fetcher and a new prefix for every registry
a curator eventually meets. ICTRP is the join point that already exists.

## Using it

```bash
# Cache a trial record (works for any ICTRP primary registry)
just ictrp-fetch ChiCTR2100045397
just ictrp-fetch ISRCTN67795930 CTRI/2021/05/033585

# Equivalently, through the normal reference-fetch entry point
just fetch-reference ICTRP:ChiCTR2100045397

# Refresh everything already cached, or list it
just ictrp-rebuild
just ictrp-list
```

Then key the trial on its ICTRP identifier and cite the record:

```yaml
clinical_trials:
- name: ISRCTN67795930
  phase: PHASE_III
  status: COMPLETED
  description: >-
    GEM3: a multicentre, double-blind, placebo-controlled randomised trial of
    combination methotrexate plus gefitinib versus methotrexate alone.
  evidence:
  - reference: ICTRP:ISRCTN67795930
    supports: SUPPORT
    evidence_source: OTHER
    snippet: "| Register | ISRCTN |"
    explanation: WHO ICTRP registration record establishing the trial's identity.
```

As with Orphanet and ICEES records, each `## Registration` table row is a stable
quotable substring, and a quoted snippet may include or omit the leading and
trailing pipes. Section prose (eligibility criteria, outcomes, interventions) is
quotable too.

`evidence_source: OTHER` is right for a registry record: it is a registration
document, not a report of human, animal, in-vitro, or computational evidence.

## What the cached record contains

`## Registration` (a table: register, main ID, registration and enrolment dates,
sponsor, target sample size, recruitment status, study type and design, phase,
countries, completion, results availability, source-register URL), `## Titles`,
then whichever free-text sections the registry populated — health conditions,
interventions, key inclusion and exclusion criteria, primary and secondary
outcomes, secondary IDs, funding — and a `## Source` provenance footer.

**Investigator contact details are deliberately dropped.** ICTRP records carry
names, postal addresses, telephone numbers, and personal email addresses. Those
are not evidence, and republishing them into a public git repository is not
something a curation cache should do.

## No bulk file

Every other structured source pins a bulk download in `data/<source>/MANIFEST.yaml`.
ICTRP does not: its full export is distributed under a separate data-use
agreement, so records are fetched **per identifier** on demand — the same posture
as ClinGen's report-page narrative. Consequently `just ictrp-rebuild` with no
`--id` refreshes what is already cached; a new trial is added by naming it.

## Auditing what is still stranded

```bash
just ictrp-audit                 # census by registry and placement
just ictrp-audit --format tsv
just ictrp-audit --strict        # exit 1 while any identifier is uncited
```

Every identifier is classified:

| Placement | Meaning |
|---|---|
| `CITED` | cited as `ICTRP:<TrialID>` with a cache file backing it — snippet-validated |
| `TRIAL_NAME` | the trial's `name`, bare or embedded in free text — queryable but unverified |
| `STRANDED` | present only in prose (`description:`, `notes:`, an evidence `snippet:`) — invisible to any query over trials |

The audit is advisory. **An identifier inside an evidence `snippet:` must not be
"corrected" in place** — that quote belongs to the cited paper, errors included.
Add an `ICTRP:` evidence item alongside it instead.

## Why this matters: the ChiCTR case

`Progressive_Supranuclear_Palsy` carried a trial named `ChiCTR-2100045397`. No
registry holds that identifier — ICTRP returns its "not found" shell for it — and
nothing in the validation stack could tell, because `name` is free text. The
identifier was transcribed faithfully from the publication (PMID:36969340), whose
abstract prints *"Clinicaltrials.gov identifier: ChiCTR-2100045397"* — wrong
twice over: ChiCTR is not ClinicalTrials.gov, and the canonical form carries no
hyphen.

The correct record, `ChiCTR2100045397`, is now cached and cited. Matching it to
the publication also surfaced something worth recording: the registered record
describes a single-arm phase 0 study of "movement disorders" with a healthy
control group, while the paper reports a randomised placebo-controlled phase 2
trial confined to PSP-RS. Sponsor, investigators, intervention, and dates line up;
the design does not. That discrepancy is recorded in the entry's `notes:` rather
than resolved — a registry record you can actually read is what makes such a
mismatch visible at all.

## Detecting absence

The portal serves its "record not found" page with **HTTP 200**, so the status
code cannot be used. The source detects the absent record by the missing main-ID
field and raises with a pointed message:

```
$ just ictrp-fetch ChiCTR-2100045397
  skipped ChiCTR-2100045397: "ICTRP has no record for trial identifier
  'ChiCTR-2100045397'. Check the identifier against https://trialsearch.who.int
  — a registry ID transcribed from a paper is often malformed (ChiCTR IDs carry
  no hyphen after the registry name)."
```

## Implementation

- `src/dismech/structured_sources/ictrp.py` — `ICTRPSource`, portal parsing, serialization
- `src/dismech/ictrp_audit.py` — the KB audit
- `tests/test_ictrp_source.py` — offline tests against saved `Trial2.aspx` fixtures
  (contact values in the fixture are placeholders, not the live record's)

Trials on the ICTRP search portal are not endorsed by WHO; they are provided as a
service. Each cached record repeats that disclaimer and links both the ICTRP
record and the source-register record.
