# Evidence–claim adjudication

When the repository's evidence–claim checker flags an assertion in a dismech entry, how
often is there a defect a curator would repair — and what does the checker miss?

The checker is the Jev classifier behind `just jev-audit`
([`docs/jev-evidence-audit.md`](../../docs/jev-evidence-audit.md)), whose saved runs live in
`monarch-initiative/dismech-evals` under `analysis/classification/jev/<Entry>/`. It compares each
curated claim with the quotes cited for it and labels the match `MATCH`, `PARTIAL` or `MISMATCH`.
On `kb/disorders/Neuroblastoma.yaml` it flagged so much of the entry — issue #16981 reports how many
assertions carry a mismatch and how many a partial — that the question "how many of these are real?"
cannot be answered by reading the flags alone. Those two counts overlap rather than adding up, since
one assertion can carry both a mismatch and a partial aspect: they are two views of the flagged set,
not two parts of it. The counts themselves are not given here, so that this file holds no checker
count for an entry under adjudication. A run of this
experiment answers it by judging every pair of the entry **without seeing the checker's labels**,
freezing those verdicts, and only then joining them to the labels.

Judging blind, and judging the whole entry rather than only the flagged rows, buys two results for
the price of one: how many flags were false alarms, and what the checker passed that a curator would
not. One class of row is held back from judging altogether, and several further classes of pair are
counted separately rather than dropped — all declared in *What is left out*.

## Naming: a curator's adjudication, not an error rate

A run reports a **curator's adjudication**: one curating group's own count of its own work. That is
the name a run's tables use, and they do not call the result an error rate for the entry: such a
figure is what an audit by people outside the group would report, and this experiment is not one.

The group in question is whoever opens the pull requests a run's `FINDINGS.md` names — for the run
planned here, the curators of the `Neuroblastoma` family entries tracked in
[`projects/NEUROBLASTOMA.md`](../../projects/NEUROBLASTOMA.md). It is not the repository's
contributors at large, and a run that does not say which pull requests it covers has not said whose
count it is.

## Runs

One run has been started: its frame is built, and its results are not yet reported. The tooling
named below (`build_frame.py`, `worklist.py`, `tally.py`) was written with that frame, after this
protocol and rubric were merged.

| Run | Entry | Pin | Status |
|---|---|---|---|
| `Neuroblastoma/` | `kb/disorders/Neuroblastoma.yaml` | recorded in `FINDINGS.md` when the frame is built, as the commit and the entry's sha256 | frame built; results not yet reported |

## Layout

A run is a directory here holding only what can be published, plus a working folder kept outside
the repository because it contains claim and quote text keyed to verdicts.

```
evidence_claim_adjudication/
  README.md                 this protocol and rubric; frozen before judging begins
  build_frame.py            builds the frame from the checker's own extractor at a pinned commit,
                            and draws the second-pass and reviewer samples
  worklist.py               prints one assertion and its pairs for the judge
  tally.py                  lists the pairs the two passes disagree about, for the reviewer's
                            rulings; then, after the freeze, tables 1 to 5 (tables 6 and 7 are
                            added with the repairs they report on)
  Neuroblastoma/
    frame_keys.tsv          one row per pair: key, section, assertion path, evidence path,
                            reference, hash. No claim text, no quote text, no verdict, no label.
    FINDINGS.md             what was measured, the seven tables, and the limits of the measurement
```

**A complete run commits:** this file, the three scripts, `frame_keys.tsv` and `FINDINGS.md`. All
of them now exist; `Neuroblastoma/FINDINGS.md` so far records only the frame.

**Not committed, and outside the repository:** the verdict sheets of the judge, the second pass and
the human reviewer, the
sheet of excluded rows, the label file `build_frame.py` derives from the saved run published in
dismech-evals, `BLIND.txt` (the sha256 of the reviewer's blind sample, written when it is locked) and
`FREEZE.txt` (the sha256 of every verdict file). The sheets carry claim and quote
text beside verdicts; `FREEZE.txt` carries only hashes and is withheld with them so that the hashes
and the files they cover travel together. The per-pair join of verdicts to labels — the table behind
tables 1 to 5 — is held back while an independent audit of the same pinned text
is still possible, so that publishing it cannot shape one; `FINDINGS.md` reports counts and
publishes the hash of the frozen verdicts, so the table can be matched to them whenever it is
released, audit or no audit. When it is released it goes to `monarch-initiative/dismech-evals`,
beside the checker runs it is joined to, which is where this repository keeps corpus evaluation
history.

A repair pull request that follows a run touches curation-scope paths only — `kb/`, `history/`,
`references_cache/` and the term caches. The repository's curation scope check does not list
`experiments/` among those, so a run's own artefacts and the repairs they motivate do not travel in
one pull request without a `scope-override` label.

## The unit: two levels

| Level | The question it answers |
|---|---|
| **pair** — one claim and one quote cited for it (`assertion_path` + `evidence_path`) | Does this quote support what it is cited for? |
| **assertion** — one curated row, with all of its quotes | Is every factual clause of this row's own text covered by at least one of its quotes? |

The **frame** is the set of pairs a run judges: every pair the checker's own extractor finds in the
entry at the pinned commit, minus the excluded rows, each with a stable key.

Both levels are needed, and the second is where most defects are expected. A row can be built
entirely from pairs that each support something and still assert a number, a frequency band or a
qualifier that none of its quotes states. No gate in the repository sees prose that reaches past its
quotes.

The two levels also disagree in a way that matters for reading the tables. The checker grades a pair
against the whole row it belongs to, so a quote cited for one clause of a long row is marked "wrong"
about every other field of that row. That is an artefact of the unit, not a defect — worked examples
3 and 6.

## Who judges

- **The judge** is an agent session working through the frame in entry order, in batches by section,
  with the checker's labels withheld from it. It opens the cached source whenever the quote alone
  does not settle a question, records that it did so, and saves its verdicts as each assertion is
  finished.
- **The second pass** is a separate agent session that judges a stratified sample of the frame
  without seeing the first verdicts. Separate is not independent: if both passes run the same model,
  they share whatever that model is systematically wrong about, so their agreement is an upper bound
  on reliability rather than a measurement of it. A run records which model each pass used, and
  `FINDINGS.md` reads table 5 against that. The human reviewer's rulings are the only verdicts in
  the design that do not share the agents' bias, which is why table 5 reports agreement with them
  separately.
- **A human reviewer** judges a sample of that sample blind, judges the excluded rows, and rules on
  every pair where the two passes disagree. The human rulings are what the agreement table in
  `FINDINGS.md` is measured against.

A **confirmed defect** means the judge recorded one and nothing overturned it: where the second pass
or the reviewer saw the same pair, their verdict governs, and the reviewer's ruling settles a
disagreement. The tables count confirmed defects in that sense; `FINDINGS.md` reports beside them how
many pairs only one pass saw.

## The four questions

Asked of every pair, in this order. They are deliberately the same four an audit by people outside
the group would ask, so that the two sets of verdicts can be joined later rather than merely
compared. Who would conduct that audit is not settled.

1. **Is the claim right as the source states it?**
2. **Is the direction right?** — does the quote support what the row says, or argue against it?
3. **Does the quote bear on this claim, in this disease?**
4. **Is the ontology term at the right level?**

## Defect classes and severities

A **defect** is a breach of the project's own evidence rules. The classes come from
[`docs/reports/pediatric-cancer-claim-evidence-review-2026-07-25.md`](../../docs/reports/pediatric-cancer-claim-evidence-review-2026-07-25.md),
whose section 4 read snippets against their claims, part of a manual review of ten paediatric
cancer entries, and from
the repository's `evidence-claim-mismatch` skill and the repair pull requests that followed that
review. They do not come from this experiment's own calibration, which found no defect in any of
the 30 pairs it judged and one at the assertion level.

| Question | Defect class | What it looks like |
|---|---|---|
| Is the claim right? | **Reaches past its quotes** | a number, a frequency band or a qualifier that no quote on the row states |
| | **Contradicted by its source** | the source says otherwise |
| Is the direction right? | **Wrong direction** | a quote that argues against the claim, graded as support |
| Does the quote bear on this claim in this disease? | **Wrong quote** | about another finding, another node or another disease |
| | **Unusable quote** | cut mid-clause; an aim, a title or advice in place of a finding; cannot be read alone |
| Neither question, strictly | **Wrong grading** | a cell-line or animal result graded as a human clinical finding; a background sentence read as the paper's own result |
| | **Explanation misreads the quote** | the explanation says what the quote does not |
| Is the term at the right level? | **Wrong or misplaced term** | a term that names a different, or a far broader, concept than the row |
| (assertion level only) | **No quote at all** | a claim row with no evidence item |

The two classes under "neither question, strictly" are the reason that row is labelled so: one is
about the cited document's provenance and one about the curator's prose, and neither is a question
of whether the quote is relevant. They are recorded because the July review found them, not because
the four questions reach them.

| Severity | What changes when it is repaired |
|---|---|
| **1** | the entry's statement |
| **2** | only the evidence — a quote replaced, extended, moved or re-graded |
| **3** | only the wording of an explanation |

## What is not a defect

- The quote supports the claim.
- The quote supports one part of the row, and other quotes on the row cover the rest.
- A field a quote cannot speak to: an identifier, a cross-reference to another row, a modality, or a
  `notes` field recording a search or a decision.
- A deliberate negative or limiting item — a quote cited to bound a claim rather than to make it.
- An inference the row itself declares, in its `notes` or by grading its evidence item
  `directness: INDIRECT`. (This case is an addition to the list this protocol took from the July
  review and the `evidence-claim-mismatch` skill, made during calibration because two of the thirty
  pairs turned on it. It is flagged because the rubric freezes with the frame, so adding a
  not-a-defect case changes what the tables count.)
- A differential-diagnosis row is the standard case: a quote stating the *other* disease's
  diagnostic test supports one distinguishing feature, and the row is sound as long as another quote
  places the two diseases in one differential.

## Worked examples

Ten cases from the calibration described below, eight of them one pair each and two (examples 4 and
8) a whole row. Examples 1, 2, 4, 5 and 7 name the not-a-defect case they test; examples 3, 6, 8, 9
and 10 turn instead on the two levels or on a project rule named with them. Nine come out as no
defect at either level; example 8 is the one that does not. `/path` is the assertion path inside
`kb/disorders/Clear_Cell_Sarcoma_of_Kidney.yaml`.

1. **The other disease's quote, on a differential row.** `/differential_diagnoses/3`
   (Sarcoma with BCOR Genetic Alterations). The quote gives the site distribution of BCOR-ITD soft
   tissue sarcoma — trunk, abdomen, head and neck, sparing the extremities — which is the site half
   of the row's first distinguishing feature; the contrast that feature draws with CCSK's renal
   primary is the row's, not the sentence's. The checker labels the whole claim, the row name, the
   disease and the disease term MISMATCH, because the sentence is not about CCSK. **Not a defect**:
   the standard differential case, and another of the row's four quotes places the two diseases in
   one differential.
2. **A quote cited to bound a claim.** `/histopathology/3` (BCOR Immunoreactivity). The quote
   reports five renal or perirenal sarcomas in patients aged 30 to 62 with strong BCOR
   immunoreactivity that proved on sequencing to be solitary fibrous tumours. The row cites it for
   "strong BCOR staining is not confined to CCSK". The checker labels the whole claim MISMATCH —
   adults, and a different tumour. **Not a defect**: a deliberate limiting item.
3. **One quote against a list-valued field.** `/genetic/0` (BCOR). The quote supports
   `case_fractions/0` exactly — somatic internal tandem duplications in 23 of 27 tumours, 85%, two
   independent cohorts — and says nothing about `case_fractions/1` and `/2`, which carry their own
   evidence items. Of the eight fields under those two case fractions the checker labels seven
   MISMATCH and the eighth — the `population` of `case_fractions/1` — PARTIAL; across the whole pair,
   which carries 19 field answers, 10 are MATCH. **Not a defect**: the artefact of grading one pair against
   every field of its assertion.
4. **A structural cross-reference.** `/stages/3` (Stage IV) carries
   `pathophysiology: [{name: Distant Metastasis to Bone, Brain and Lung}]`, a link to another row of
   the same entry. Four of the row's six pairs are labelled MISMATCH on that field and the other two
   PARTIAL. **Not a defect**: a link between rows is not a quotable claim.
5. **A declared inference.** `/prevalence/0`. The quote gives an age-adjusted incidence of 0.205 per
   million; the row records `rate_per_100000: 0.0205`, the same number in the units the schema asks
   for, and `rate_denominator: POPULATION_PER_YEAR`, which the row's own `notes` say is inferred
   because the paper states no time unit. **Not a defect.** Without that note the denominator would
   be an undeclared inference — *Reaches past its quotes*, and severity 1, because repairing it means
   either sourcing the time unit or removing the field rather than changing a quote. The note is what
   makes the difference.
6. **Clause-by-clause coverage.** `/differential_diagnoses/0` (Wilms Tumor). The quote is the 1985
   series' conclusion that CCSK should be identified as a non-Wilms sarcoma. The checker labels the
   row's `distinguishing_features` MISMATCH and its `description` MATCH — correctly: the sentence
   supports the description, and the features are supported by the row's other quotes. **Not a
   defect at pair level**, and the reason the assertion level exists.
7. **The boundary between existence and causation.** `/pathophysiology/1/downstream/0`. The quote
   says YWHAE-NUTM2 family fusions occur in a minority (12%) of cases as the only recurrent somatic
   aberration. The edge's target is "Primary Renal Tumor Growth", so the quote establishes the lesion
   and not the step to growth. The edge declares that gap three times over: its `description` says
   the intervening steps are not characterised in the cited sources, its `causal_link_type` is
   `INDIRECT_UNKNOWN_INTERMEDIATES`, and its evidence item is graded `directness: INDIRECT`. **Not a
   defect, because the claim is scoped to what the quote carries.** The same quote under
   `directness: DIRECT` is a defect — *Wrong quote*, severity 2.
8. **A number the quote licenses only by addition.** `/treatments/5` (high-dose chemotherapy with
   autologous stem-cell rescue). The row says it was given to 14 of 37 relapsed patients; the quote
   gives 13 of 21 patients in second complete remission and 1 of 7 who did not reach it. The 14 is
   the sum, but 37 is not in this quote. **Not a pair-level defect; an assertion-level one.** None of
   the row's four quotes gives the 37, so the row does reach past them — *Reaches past its quotes*,
   severity 2, because the figure sits in the committed full-text cache of the paper the row already
   cites and the repair is to extend a quote. This is the one defect the calibration found.
9. **A `notes` field that still makes factual claims, and the assertion level settling it.**
   `/stages/0` (Stage I). Its `notes` record that one report gives 42% of 191 patients as stage I
   where another gives 39.5% (75 of 191), and that neither cited text explains the difference. The
   pair's quote, about radiotherapy omission in AREN0321, cannot speak to either figure, and the
   checker labels the notes MISMATCH. **Not a defect at either level**: two other evidence items on
   the same row carry the two percentages, one from each report. This is the worked case of the
   assertion level *clearing* a row the pair level could not.
10. **A term with no narrower class.** `/phenotypes/4` (Brain Metastases) binds
    `HP:0030692 Brain neoplasm` with `preferred_term: Brain metastases`. **Not a defect**: HPO has
    no brain-metastasis class — a label search of HP through OLS for `metastas`, run on 17 November
    2026, returns one term, `HP:0200059 Metastatic angiosarcoma`, which is a different disease — and
    the project's rule is that no term beats a bad one. Question 4 asks whether the term is at the
    right level, not whether a perfect term exists.

## The calibration, and what it found

The rubric was tried on 30 pairs of `kb/disorders/Clear_Cell_Sarcoma_of_Kidney.yaml`.

**That entry is this group's own work, and recent.** It is not on the project page the group is
defined by, which tracks the Neuroblastoma family; what ties it to the group is its own history —
it was created in #15880 on 29 October 2026 and
extended in #16917 and #16989 on 10 and 11 November. The two differential-diagnosis rows the worked
examples draw on were not written together: example 6's row came in with the entry itself, 18 days
before the checker run the calibration uses, and example 1's row was added in #16989, five days
before it. So the calibration is not an independent test of the entry: it is the same curators
reading their own work, in one case work less than a week old. What it does test is whether the
rubric's wording sorts cases the same way twice, which is what a rubric has to do before it is used
blind, and the pairs are disjoint from the frame
of the run planned here, so no pair used in calibration is a pair a run judges. A reader should
discount "no defect found" accordingly: it is evidence about the rubric, not about the entry, and
still less about the group.

The separation is of pairs, not of subject matter either: that entry's differential-diagnosis rows
include neuroblastoma, because cyclin D1 staining does not separate the two.

The pairs were drawn from the checker's saved run observed at `2026-11-16T21:46:35Z`. That run
records `inventory.source_revision` `09ce31cd7a38a03122f5e9a9869792b5b61c1f91` — the repository
commit it read, which does not itself touch this entry — and
`inventory.source_sha256`
`ef5a874ac801afb3d2da733b75210f0973c98bec8e6ca8b286d789f294d60c98`, which is the sha256 of the
entry file at that commit and so is what re-identifies the text judged
(`git show 09ce31cd7a3:kb/disorders/Clear_Cell_Sarcoma_of_Kidney.yaml | sha256sum`). Pairs were
taken proportionally by top-level section, seed `20261117`. The sampler was a one-off and is not
committed: `build_frame.py` draws a run's own samples the same way but does not reproduce these 30,
so they are not re-derivable from the repository alone;
the saved run's own sha256 is
`4a21f2aedcf830b4823791b1016ec2f87756edd05173774a0c0547d61d98dbe1`, which fixes the input the seed
was applied to.

The run holds 116 active pairs across 49 assertions, each with one assessment: whole-claim MATCH 72,
PARTIAL 42, MISMATCH 2. It carries 923 answers in all, of which 620 are MATCH, 180 PARTIAL and 123
MISMATCH; 116 of those are the whole-claim answers just given, so the field-level answers number 807
— 548 MATCH, 138 PARTIAL and 121 MISMATCH. The two levels have to be kept apart even in a total.

Its `inventory.complete` is `false`. That flag records extraction validity, not assessment coverage,
so it says nothing about whether every pair was judged — and here every active input was. It is
still a true warning, and the explanation in *What is left out* is consistent with it rather than
derived from it: the saved frame is one pair short of what the entry now yields, which an extractor
that raised on that row would account for, since the audit records such a failure as an invalid
input and that is what the flag reads. The saved file does not say which row it was.

Three things came out of the calibration.

**The rubric's hard work is rejecting false alarms, not finding defects.** No pair among the 30
carried a defect. Every MISMATCH among them — at the whole-claim level in examples 1 and 2, at the
field level in 3, 4, 6 and 9 — traced to one of five patterns, all of them cases *What is not a
defect* excludes: the other disease's quote on a differential row, a limiting quote, one quote judged
against a list-valued field, a structural cross-reference, and a quote that covers one clause of a
row whose other quotes cover the rest. (The "inference the row declares" case earns its place
differently: examples 5 and 7 turn on it, and neither carries a MISMATCH at any level, so it explains
no MISMATCH. Both are flagged all the same, their pairs being whole-claim PARTIAL, so what it
explains is why a PARTIAL pair can be sound.) So the defect classes above are inherited from
the July review and the earlier repair pull requests rather than from this calibration. For a run on
Neuroblastoma that is the useful direction: the judgement that costs effort is the one that says
"flagged, and sound".

**At the assertion level it found one, and a mild one.** Worked example 8 above is that finding: a
row whose every pair passed and whose stated denominator none of its quotes carries. It is severity
2 rather than 1 because the figure is one quote extension away, where the same class on example 5
would have been severity 1. So the assertion level found, on one row in thirty pairs, a gap the pair
level could not see, and what it bought was an evidence-layer repair rather than a corrected claim.

**A whole-claim MATCH does not mean every field matched.** 20 of the 72 whole-claim MATCH pairs
carry at least one field-level MISMATCH, and 18 of the 42 PARTIAL pairs do. So any count has to say
which level it is counting, which is why table 1 below counts per assertion and table 2 counts per
pair.


## What is left out, and how it is counted

- **Excluded rows.** A small set of rows in the entry is excluded from this group's own
  adjudication, and judged by a human reviewer instead. They are the entry's ALK-inhibitor
  treatment and trial rows and its chromosomal-lesion genetic rows, both already visible in
  `kb/disorders/Neuroblastoma.yaml`, so the count in `FINDINGS.md` can be audited against the
  entry. The reason is that the group does not curate those rows at all — they are excluded from
  its curation by a standing rule it works under — so it would be adjudicating work it has no
  part in and cannot repair, which is a different exercise from the one this experiment
  measures. They are counted separately in `FINDINGS.md` and never silently dropped; the sheet
  holding them is not opened by the judge or by the second pass. A run's `FINDINGS.md` says how
  many rows this covered and in which sections.
- **Pairs the checker's run did not assess.** Counted as "not assessed by the checker", and
  `FINDINGS.md` reports them as a share of the frame, so a flag count is never read against a
  different denominator.
- **Pairs the judge could not settle.** Recorded as "not judged", with the reason. Where the
  judging session's request is refused by an automated content filter mid-judgement, the whole
  assertion that request belonged to is recorded as "not judged: stopped" and no repair is
  proposed from it, rather than being judged on a partial reading. The stop holds the assertion
  and not merely the one pair, because what was interrupted is the reading the rest of that row's
  pairs would have shared.
- **Inactive inputs.** The checker marks superseded inputs inactive; only active ones enter the
  frame.
- **Rows with no evidence item.** The extractor returns these without a quote, so they form no
  pair. They are the *No quote at all* class, and a run counts them per assertion rather than
  letting them vanish between the two levels. On the calibration entry three rows are of this
  kind, and all three are structural — a nested cross-reference and two classification assignments
  — rather than defects.
- **Pairs an older extractor did not produce, or choked on.** The saved file does not distinguish
  the two, and a run should not pretend otherwise: a row the extractor never emitted and a row it
  raised on both leave the frame short, and only the second sets `inventory.complete` false. The
  saved run's frame is whatever its own extractor version yielded, which need not be what the
  current one yields from the same bytes: on the calibration entry the saved run holds 116 pairs
  over 49 assertion paths where today's extractor finds 117 over 50, the extra one being an
  effect-modifier row with a real quote. A run therefore reports its extractor version beside the
  pair count, and treats a pair the saved run never produced as not assessed rather than as
  passed.

## Filling in the sheets

Each reader writes only in the verdict columns of their own sheet; the other columns identify the
row and are not changed.

| Reader | File | One row per |
|---|---|---|
| judge | `judge_sheet.csv` | pair of the frame |
| judge | `assertion_sheet.csv` | assertion, the ones with no quote included |
| second pass | `second_look_verdicts.csv`, its own filled-in copy of `second_look_sheet.csv` | pair of its sample |
| human reviewer | `user_sample_sheet.csv` | pair of the blind sample |
| human reviewer | `fenced_sheet.csv` | pair of the excluded rows |
| human reviewer | `rulings.csv`, with the columns `key`, `defect_class`, `severity` and `note` | pair that `tally.py --disagreements` lists for a ruling |

**On a pair row:**

- `q1_claim_right`, `q2_direction_right`, `q3_quote_bears` and `q4_term_level` take the answers to
  *The four questions*, in that order: `yes`, `no`, `unsure` or `n/a`.
- `defect_class` takes the name of one class from *Defect classes and severities*; `none`, or
  nothing once the questions are answered, when the pair has no defect; or `not judged: <reason>`.
- `severity` is `1`, `2` or `3` on a defect, and empty otherwise.
- A question answered `no` or `unsure` needs a defect class or `not judged: <reason>`.
- A pair with a defect class or `none` has all four questions answered; `n/a` is an answer. A pair
  whose class is empty counts as judged only once all four are answered.
- `proposed_repair`, `opened_source` and `note` are free text. `opened_source` records that the
  cached source was opened for the pair.

**On a row of `assertion_sheet.csv`:**

- `clauses_covered` answers the assertion-level question of *The unit: two levels*. On a row with
  quotes it is `yes`, `no`, `partly` or `unsure`. `no` and `partly` need a defect class and a
  severity, and `uncovered_clauses` names the clauses. `yes` goes with no defect class. `unsure`
  needs `not judged: <reason>` as the defect class. On a row marked `not judged: <reason>` it may
  stay empty, and it is never `yes`.
- On a row with no quote (`pairs` is 0), `clauses_covered` is `n/a`, and `defect_class` is either
  `no quote at all`, with a severity, or `none`. An empty `defect_class` on such a row counts as
  not yet judged, never as "no defect".

**Not judged, and stops.** `not judged: <reason>` in `defect_class` records a pair or an assertion
the reader could not settle. A judge's `not judged: stopped`, on a pair or on its assertion row,
holds the whole assertion, as *What is left out* describes, and the judge's other rows of that
assertion may then stay empty. Another reader who is stopped writes `not judged: stopped` on each of
its rows of that assertion; `tally.py` checks this on the second reader's sheet and the reviewer's
blind sample. Every other row needs a verdict before the freeze.

A ruling takes a defect class, with its severity, or `none`.

`tally.py` refuses a sheet that breaks one of these rules; case is ignored, and `no defect` or `not
a defect` is read as `none`. Of the identifying columns it checks `key` on every sheet, and
`assertion_path` and `pairs` where the judge's sheets and the two samples carry them; of the
free-text columns it checks only that `uncovered_clauses` is not empty where it is needed. Before
the freeze it names the sheet, row and column at fault, and neither what the row holds nor which
rule it breaks. The reviewer's blind sample is locked once its sheet is complete and passes these
checks: its sha256 is written to `BLIND.txt`. The sha256 of `BLIND.txt` is then published outside
the run folder before the list is shown to any reader, and `tally.py` requires it, so a lock taken
again after the sheet has changed is refused. Until the lock, a problem on another reader's row is
reported without a row, a column or a number, and a blank row there is not counted, when the row is
of a sampled pair, of the same or a nested assertion, or of a row shown beside a sampled pair (the
rows its claim names: its parent rows, a subtype or hypothesis row, and an edge's endpoints and
scope), or when its key or assertion path is not in the frame.

## The blind procedure

1. The frame is built at a pinned commit of the entry, from the checker's own extractor, so that
   verdicts and flags refer to the same text. Each pair gets a key: its assertion path and evidence
   path at the pin, plus a hash of claim and quote. The key identifies a pair *within the pin*, and
   the hash is what makes it exact there. It is deliberately not stable across a repair — a repair
   changes the quote or the claim, which is the point of it — so the before-and-after join in table 6
   is made on assertion path and evidence path, with the hash recording which side changed.

   **A checker input is matched to a frame pair on assertion path, evidence path and quote text, not
   on the claim hash.** Hash matching is not structurally impossible — on the calibration entry 104
   of today's 117 input keys still equal the saved run's, over identical bytes — but it is unreliable
   across extractor versions: the twelve keys that moved there are all relationship-edge claims,
   whose canonical form has changed, and the thirteenth difference is the effect-modifier pair the
   saved run never produced at all. A run matching on hashes would therefore lose exactly the edges,
   and silently, so it matches on paths and quote text and reports how many inputs it placed.
2. The judge sees claim, quote, reference, explanation, `evidence_source`, `quote_role` and
   `directness` — and no label, no mismatch probability, nothing from the excluded rows, none of the
   examples in the body of the issue, and neither the saved run published in dismech-evals nor the
   dashboard the evaluation queue builds from it.
3. The judge works through the frame as described in *Who judges*.
4. The second pass judges its sample — drawn at random, stratified by top-level section — without
   seeing the first verdicts. The human reviewer then does the three jobs *Who judges* gives them:
   a blind sample of that sample, the excluded rows, and a ruling on every pair the two passes
   disagree about.
5. The verdict files are then frozen and hashed into `FREEZE.txt`. Only after that are the checker's
   labels joined and the tables computed, and `tally.py` refuses to run unless the hashes match.
6. Repairs are written after the count, never before: repairing first would remove the items the
   comparison needs.

Building the frame and judging it are separate jobs. The frame builder handles the checker's label
file, because it has to key the labels to the frame; it writes them to a file the judge never opens,
and passes none of them on.

The sample sizes are fixed in advance — 120 pairs for the second pass, 30 of those for the human
reviewer, and the top 50, 100 and 200 by mismatch probability for table 4. A run states the size of
its frame in `FINDINGS.md` beside them, because what those numbers are worth depends on it: table 4
says nothing if the frame is smaller than 200 pairs.

## The seven tables, and how each is computed

Tables 1 to 5 are computed by `tally.py` from the frozen verdict files joined to the checker's
labels, matched as step 1 of the blind procedure describes — on assertion path, evidence path and
quote text. Tables 6 and 7 need the repair pull requests and a checker run made after them, and are
added to the script with those.

1. **Per assertion, in the unit issue #16981 counts in.** Of the assertions the checker flagged
   MISMATCH on any field, how many have a confirmed defect, how many none, how many were not judged;
   the same rows for PARTIAL and for the unflagged. Counted over active inputs.
2. **Per pair, by the checker's whole-claim verdict.** The share with a confirmed defect among its
   MISMATCH pairs, its PARTIAL pairs and the pairs it passed.
3. **Defects by class, severity and section**, from the class and severity recorded on each confirmed
   defect.
4. **Does the checker's ranking put the real defects first?** Confirmed defects among its top 50, 100
   and 200 pairs by mismatch probability, against the base rate. Each cut-off is computed only where
   the frame is at least twice its size, so a frame under 400 pairs reports fewer of them and one
   under 100 reports none; `FINDINGS.md` says which were computed.
5. **Agreement**: the first verdicts against the second pass on its sample, and against the human
   reviewer's, both as plain agreement and as agreement on "defect or not".
6. **Before and after**: the checker's verdict on each repaired pair, joined on assertion path and
   evidence path and reporting which pairs could not be matched,
   and, before and after, the two counts issue #16981 reports: assertions flagged as mismatches and
   assertions flagged as partial.
7. **What was done**: fixed, kept with the reason recorded, not judged.

## What the pin means for an independent audit

A run pins the entry and judges it as it stood at that commit, before any repair, and an audit from
outside the group would sample that same pinned, unrepaired text. Neither therefore yields a figure
for the *repaired* entry. Getting one needs either a join on the paths from the pinned
pairs to their repaired counterparts, or a fresh sample drawn after the repairs have merged. A run
assumes neither, and its `FINDINGS.md` says which it used.
