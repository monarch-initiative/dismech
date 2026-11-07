# Citation Scan

The citation scan finds recent papers that cite the references a KB entry
already relies on. It runs weekly as the `citation-scan` job in
`.github/workflows/literature-scan.yml`, after the keyword-based literature
scan, and files at most a handful of `[citation-scan]` curation issues.

The two scans find different papers. The [literature scan](https://github.com/monarch-initiative/dismech/blob/main/scripts/literature_scan.py)
searches a fixed keyword profile and guesses which entry a paper is about from
its title. The citation scan starts from the entry: a paper that cites several
of the papers an entry is built on is very likely about that disease, whatever
words its title uses.

```bash
just citation-scan                         # whole KB, papers indexed in the last 7 days
just citation-scan 90 Alkaptonuria Asthma  # selected entries, longer window
uv run python scripts/citation_scan.py --help
```

The scan is report-only. It writes a packet (`output/citation_scan/citation_scan.{md,json}`)
and never edits `kb/`. In the workflow, an agent reads the packet and decides
which candidates are worth an issue.

## How a candidate is found and scored

1. Collect every PMID each entry cites.
2. Ask Europe PMC which papers first **indexed** in the window cite any of them,
   in chunks of 500 `CITES:<pmid>_MED` clauses. The window is on the index date,
   not the publication date, because Europe PMC often adds a paper's citation
   links after the paper is published. On a week tested before the scan was
   written, the index-date window found 35 citing papers where the
   publication-date window found 15.
3. Fetch each candidate's reference list and count, for every entry, how many of
   the entry's references it shares.
4. Score a (paper, entry) pair as the sum over shared references of
   `1 / log2(2 + n)`, where `n` is how often that reference is cited overall.
   Citing a 10-citation case series contributes 0.28; citing a 5,000-citation
   methods paper contributes 0.08.

Several rules then narrow the list:

| Rule | Why |
|---|---|
| At least 2 shared references | 81-82% of pairs share only one, and those are mostly noise. A picornavirus polymerase paper reached the ALS shortlist on a single shared reference. |
| At most 3 papers per entry | The score is a sum, so an entry citing 115 papers outscores one citing 10 on volume alone. In a test without the cap, ALS took 29 of the top 40 places. |
| One row per paper | A review of non-nutritional rickets shared references with four sibling rickets entries. It is shown once, under its best match, with the other entries listed. |
| GeneReviews and StatPearls chapters get a neutral weight | Europe PMC undercounts citations to Bookshelf chapters. It reports the GeneReviews Alkaptonuria chapter as cited once, which would make it look like a rare, highly informative reference. Chapters listed in `cache/bookshelf/` are weighted as moderately cited instead. |
| Notices are dropped | Errata, retraction notices and expressions of concern are about another paper. |
| Papers the entry already cites are dropped | |

Reviews are kept but labelled. They are useful for seeing what is new and weak
as evidence to quote, so the curator decides.

## Not proposing the same paper twice

The moving window does most of the work: a citing paper is fetched in the week
it is indexed and not again. The **issue ledger** covers the rest. Before
scoring, the workflow lists every open or closed issue titled `[lit-scan]`,
`[preprint]` or `[citation-scan]`, and the scan drops any (paper, entry) pair
that already has one.

Any closed issue counts as decided, whatever its close reason. Curators close
scanner issues as completed or duplicate whether or not anything was added (none
of the first 223 closed scanner issues used "not planned"), so the reason cannot
tell a rejection from an addition. A paper that was added drops out anyway,
because the entry now cites it.

Each `[citation-scan]` issue ends with a hidden marker:

```
<!-- citation-scan pmid=42780777 entry=kb/disorders/Alkaptonuria.yaml overlap=2 -->
```

A pair whose issue is closed is proposed again only if a later scan finds the
paper sharing at least two more of the entry's references than the marker
records. That happens when the entry has since gained references the paper also
cites. Older literature-scan issues carry no marker, so every PMID they mention
is treated as decided for good.

The literature and preprint scans apply the same closed-issue rule to their own
candidates.

## Scale

A whole-KB run over one week (3,784 entries, 48,464 distinct PMIDs) took 6
minutes 50 seconds and 538 Europe PMC requests. It found 438 citing papers and
779 (paper, entry) pairs, 137 of them sharing at least two references. Most of
the time goes on fetching reference lists, which runs four at a time
(`--workers`).

A longer window is a backfill. The scheduled run never does one; run it by hand
with `--days` and expect the candidate count to scale with the window.
`--reference-cache FILE` saves the fetched reference lists, so a backfill can be
re-scored with different settings without fetching them again.
