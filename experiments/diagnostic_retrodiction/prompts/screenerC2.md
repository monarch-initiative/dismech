# Screener C prompt: rule-1 re-screen disagreements

This is the instruction given to screener C, as a fresh session with no
earlier context, to decide the rows on which screener A (`eligibility.tsv`) and
screener B2 (`eligibility.screenerB2.tsv`) disagreed. Screener C's procedure for
the first resolution (`eligibility.screenerC.tsv`) was not recorded. This
prompt reconstructs it from that file's format: blinded to the other
screeners, decided under the current rules, one decision and one reason per
row.

---

You are an independent eligibility screener for the diagnostic-retrodiction
experiment in `experiments/diagnostic_retrodiction/` of this repository.

**Your input** is `experiments/diagnostic_retrodiction/screenerC2_input.tsv`:
5 rows of the sampling frame, frame columns only.

**Your rules** are `experiments/diagnostic_retrodiction/eligibility_rules.md`
(version 3). Read all of it before deciding anything. Apply it as written. Where
it is genuinely silent or ambiguous for a row, decide, and mark the reason
`(ambiguous)`.

**You are blind to the other screeners.** Do not open, search or read these
files, or their git history:
- `eligibility.tsv`, `eligibility_review.tsv`
- `eligibility.screenerB.tsv`, `eligibility.screenerB2.tsv`, `eligibility.screenerC.tsv`
- `eligibility_disagreements.tsv`, `eligibility_resolution.tsv`
- `eligibility_v2_changes.tsv`, `eligibility_v3_changes.tsv`
- anything under `eligibility_work/`
- `compare_screeners.py`, `select_screenerB*.py`

You may read the rest of the repository, including the dismech entries under
`kb/disorders/`, and search PubMed through NCBI E-utilities (the `NCBI_API_KEY`
environment variable holds a key; never print it or write it to a file). Do not
cite any PMID you have not looked up in this session. If you cannot verify a
date or report, say so in the reason rather than guessing.

**For each row, decide:**
- `decision`: INCLUDE or EXCLUDE
- `reason`: `CODE: explanation [judged]`, using a code from the rules
  (`PRIMARY_ROUTE` for INCLUDE), with ` (ambiguous)` after the code when
  warranted. The reason should name the rule or section you applied.
- `first_or_improvement`: FIRST or IMPROVEMENT for INCLUDE, NA for EXCLUDE
- `subset`: for INCLUDE, the subset (rule 1) or ALL; NA for EXCLUDE
- `specimen_check`: CONFIRMED or WRONG_SPECIMEN if `specimen_basis` is
  IMPLICIT, otherwise NA

**Write** `experiments/diagnostic_retrodiction/eligibility.screenerC2.tsv`, tab
separated, with exactly these columns in this order:

`disease_name  row_type  row_name  decision  reason  first_or_improvement  subset  specimen_check`

One row per input row, with `disease_name`, `row_type` and `row_name` copied
exactly from the input. Do not modify any other file, and do not commit.

When finished, reply with the 5 decisions and, for each, one sentence on the
rule that decided it.
