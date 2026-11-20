# Prevalence versus incidence: analysis and staged remediation plan

**Status:** proposal, for maintainer review before any of it is undertaken
(issue #18487). Nothing in this document has been implemented.

**Goal:** make a `Prevalence` record say, in slots a program can read, which
occurrence measure it reports, what its rate is a rate of, and whether its
band and its rate agree; then repair the records that do not, without a bulk
rewrite and without losing information.

**Scope:** the `prevalence:` section of disease entries and the schema,
checks and documentation around it. The `epidemiology:` section is in scope
only where it holds occurrence figures that belong in `prevalence:`.

All counts below were taken on 2026-11-20 against `main` at `c513f825387`,
by parsing every `prevalence:` record in `kb/disorders/` (no module,
comorbidity or grouping file carries one). They are a snapshot: this
repository merges fast enough that they move within days, so each figure is
given with the rule that produces it, and the first step of the plan is a
script that reproduces them on demand.

## 1. What the confusion actually is

The project's own account of the problem is spread over seven issues and
one decision-register entry. Read together, it is not one defect but three,
and they need different remedies.

### 1a. A modelling problem, now mostly settled on paper

`Prevalence` was built for prevalence. Incidence, carrier frequency and
literature case-counts were added later as values of `measure_type`
(`PrevalenceMeasureEnum`), so the class, the section and the band slot all
still say "prevalence" while the records inside them do not (#8431). PR
#10758 (merged 2026-09-05) settled the semantics without touching the KB:

- `prevalence_class` is a **magnitude** band; `measure_type` says what is
  measured. `BAND_1_9_PER_100000` on an incidence record means 1-9 new cases
  per 100,000 per year, and the band is meaningless read alone
  (design decisions §8, 2026-09 amendment).
- `rate_denominator` (`RateDenominatorEnum`: `POPULATION`, `LIVE_BIRTHS`,
  `PERSON_YEARS`, `POPULATION_PER_YEAR`) pins the dimension of
  `rate_per_100000`. `ANNUAL_INCIDENCE` has deliberately no fallback.
- The qualitative tiers `COMMON`, `RARE`, `ULTRA_RARE` are prevalence-defined
  and presuppose no numeric estimate, so they are invalid on
  `ANNUAL_INCIDENCE` and `CARRIER_FREQUENCY` and should not sit beside a rate.
- The one consumer, the disorder-page template, now qualifies a numeric band
  with the measure ("per year", "(carriers)", "(births)") and renders the
  denominator.

That reading matches the upstream vocabulary. Orphanet bands annual
incidence with the same classes it uses for prevalence: the committed
`references_cache/ORPHA_*.md` epidemiology tables carry 212 "Annual
incidence" rows against 883 "Point prevalence" and 454 "Prevalence at
birth". Only `CARRIER_FREQUENCY` is a dismech extension with no Orphanet
counterpart, which is why it is the measure the bands fit worst (#9723).

What #10758 did **not** do, and said so: no check reads any of these rules,
no record was repaired, and three enum gaps it listed are still open.

### 1b. A data problem, largely untouched

Nothing gates the rules above, and the KB has drifted under them. The
figures that matter, with the rule behind each:

| Finding | Count | Rule |
|---|---:|---|
| Prevalence records (files) | 3,934 (2,885) | every `prevalence[]` item |
| `measure_type` absent | 250 | key missing |
| `measure_type: UNKNOWN` | 426 | |
| `UNKNOWN` records that nevertheless carry a rate | 41 | `rate_per_100000` or `rate_low` set |
| `ANNUAL_INCIDENCE` records | 263 | |
| of which no `rate_denominator` | 148 | the slot #10758 said to always set |
| of which no band and no rate at all | 13 | |
| Records still carrying deprecated `percentage` | 467 in 325 files | |
| of which also fully structured (redundant copy) | 411 | any of `measure_type`, band, rate present |
| of which `percentage` is the only content | 56 | see §1c |
| Qualitative tier on `ANNUAL_INCIDENCE` / `CARRIER_FREQUENCY` | 8 | all `ANNUAL_INCIDENCE`; the same 8 named in #8431 on 2026-09-03 |
| Qualitative tier beside a numeric rate | 22 records, 21 files | counting `rate_low`/`rate_high` |
| `rate_per_100000: 0.0` | 6 | 5 `CASES_IN_LITERATURE` placeholders; `Smallpox` is a real zero |
| Numeric band disagrees with the rate | 66 | `_band_from_rate()` boundaries |
| of which rate sits exactly on a boundary | 33 | 20 at 0.1, 10 at 100.0, 2 at 1.0, 1 at 10.0 |
| of which within 10% of a boundary | 3 | |
| of which a clean one-decade error | 30 | |

The band-versus-rate class is the one that is growing. #7005 found 3 genuine
errors on 2026-07-25, #10193 found 21 on 2026-08-30, and there are 30 today.
That is roughly ten new ones a month from ordinary curation, which is the
strongest single argument for a gate: the backlog is small, but it refills.

The `rate_denominator` slot has been adopted correctly where it is used (254
records; 87 `POPULATION_PER_YEAR` and 23 `PERSON_YEARS` on incidence), but 148
of 263 incidence records predate it. Their text gives a lead for most:
32 say "person-years", 90 say "per year" or "annual", 3 say "births", and 23
give no hint at all. A lead is not a value; each needs a source read (§4).

### 1c. Figures that are not population occurrence and have no home

The 56 records whose only content is the deprecated `percentage` are not a
unit problem. Reading them, roughly 40 are not population occurrence at all:

- **fraction of a clinical category** ("15-25% of all lymphomas",
  "30% of epilepsy patients", "26.5% of CMD cases", "40% of CNS neoplasms");
- **cohort-conditional rates** (33% of adults on parenteral nutrition get
  refeeding syndrome; 24.5% of chronic-otitis-media patients at one centre);
- **penetrance** ("~40% lifetime penetrance in females", "56.4% diagnosed by
  age 80 in C282Y homozygotes");
- **head-counts and absolute totals** ("7 genetically confirmed cases",
  "7.74 million people living with sickle cell disease");
- **prose** ("outbreak-dependent", "variable, higher where sanitation is poor").

These were stripped from the structured slots during the migration's three
review-correction batches precisely because converting them to a population
rate asserted something false (design decisions §8, migration-status row).
They have sat in `percentage` since, with no slot to move to. The same shape
appears on the structured side: the 41 `UNKNOWN`-with-a-rate records and the
38 "diagnostic-yield" records of #11726 are ascertained-cohort proportions
stored as if they were population rates, and #7003 records three more
missing measures (screen-positive rate, screen-detected incidence, proportion
of a clinical denominator). #11268 is the adjacent case where the denominator
is a superset disease.

Some of these already have a structured destination that was simply not used:
penetrance belongs on `Inheritance.penetrance_percentage`; a stage share
belongs on `stages:`; a per-gene share of a cohort is `Genetic.case_fractions`.
Survival and mortality figures have no slot anywhere (`ClinicalBurden` is a
burden tier, not a rate). Fraction-of-category and cohort-conditional
proportions have none either. Decision D3 below proposes the home.

### 1d. A second, free-form home for the same facts

`epidemiology:` (`EpidemiologyInfo`: name, numeric range, free-text `unit`,
factors, evidence) exists on 236 entries, and 207 of those mention prevalence
or incidence inside it. Its `unit` values include "cases per 100,000
population per year", "cases per 1,000,000 person-years" and "cases per year
(per ED dental infection evaluations)": the exact dimensions `rate_denominator`
was created to carry, written as prose next door. #7520 noted entries whose
only occurrence figures live there. Any rule enforced on `prevalence:` is
bypassed by writing the same figure in `epidemiology:`, so the plan has to
say what each section is for (D7).

## 2. What earlier attempts tried, and what to carry forward

There are no abandoned PRs on this topic. There is one merged schema PR, two
merged clean-up PRs, three agent dispatches that never produced a PR, one
dispatch that would have made things worse and was stopped by a comment, and
three issues proposing the same check. The lessons come from those.

1. **Three dispatches produced nothing.** The #7005 check (2026-07-25), the
   #7003 enum values (2026-07-25) and the #8431 check (2026-08-13) were each
   handed to an agent by an issue comment. None opened a PR, and the stall was
   noticed only when the next issue re-measured the backlog. A comment mention
   is not an owner. Every step below names a deliverable, and the tracker
   (Phase 0) records who holds it.

2. **The one dispatch that would have run was lossy, and it was caught by a
   person, not a gate.** #8431 step 3 asked an agent to replace the numeric
   band on ~96 incidence and carrier records with the nearest qualitative
   tier. That would have put `COMMON` beside `rate_per_100000: 21800` and left
   one file saying a disease is both common and 1-9 per million. The semantics
   had to be pinned first; the data work then collapsed from 96 records to 8.
   **Decide the rule, then write the check, then touch the data**, in that
   order, every phase.

3. **The one PR that landed (#10758) was schema, docs and template only, and
   took four review rounds to get right.** Its load-bearing premise, that the
   fields had no consumer, was false: the template had rendered them for ~1,100
   commits. The reviewer found it by re-running the grep on current `main`. A
   second stale-base error followed: two comments on #8431 (2026-09-06 and
   2026-09-09) reported `rate_denominator` absent from the schema and failing
   validation, four days after it had merged, from checkouts that had not
   pulled. **Every count and every premise is re-derived against current
   `main` before it is written down**, which is what the Phase 0 script is for.

4. **The migration scripts were additive and conservative and still produced
   three review-correction batches.** `scripts/migrate_prevalence.py` refused
   to infer measure type from `notes` and refused bare unit-less numbers, and
   it still converted fraction-of-category and penetrance figures to population
   rates when the qualifier lived in `notes` or in the `population` label,
   where no regex looks. Those were caught by PR review. **No step below infers
   a measure, a denominator or a number from prose.** Text is used to rank and
   route records to a person; the value comes from the source.

5. **A slot whose first value reads as a default gets filled with it.**
   #11987 recorded a 2.7% diagnostic yield with `rate_denominator: POPULATION`
   and a `notes` paragraph explaining why that was wrong, written seconds
   apart. The 38 cohort-yield records of #11726 had stayed clean only because
   the slot postdated them. An enum has to offer the value that is true (D3);
   a gate cannot read the `population` string well enough to catch this.

6. **The band key is a trap.** `BAND_1_5_PER_10000` is titled "1-9 / 10,000"
   and defined as 10-99 per 100,000; it merged two Orphanet classes and kept
   the first one's name. #9723 and #10193 both record curators mis-banding
   because of it. The check's message must quote the numeric range, never the
   key, and the description of `BAND_1_5_PER_10000` / `ABOVE_1_IN_1000` must
   close the gap at exactly 100 ("100 or more", not "more than 100").

7. **Documentation that describes schema state has twice described state that
   did not hold** (#10556 for `supports: PARTIAL`, #7524 for MAXO terms). A
   test that every slot named in a `CLAUDE.md` YAML example resolves in
   `dismech.yaml` costs little and closes the class;
   `tests/test_phenotype_distributions.py::test_claude_md_instructions_match_the_code`
   is the precedent.

8. **Three issues proposed the same check and a fourth asks for a plan.**
   #7005, #10193 and #8431 each specify a band check; #9723 and #11726 each
   raise a placement question those checks depend on. The plan consolidates
   them into one tracker rather than adding a fifth proposal.

## 3. Decisions to make before any KB file moves

Each is written so a reviewer can accept, reject or amend it in a sentence.
The recommendation is the planner's lean, not a ruling.

**D1. Band semantics.** Keep the §8 magnitude reading. It matches Orphanet,
it required no rewrite, and reopening it would reopen the 289 banded incidence
and carrier records (203 and 86 today) that were underspecified rather than
wrong.
*Recommend: closed; do not reopen.*

**D2. Where `CARRIER_FREQUENCY` lives.** Options: (a) stay on `Prevalence`;
(b) move to `Genetic` beside `case_fractions`; (c) stay, but no band. The fact
the earlier discussion missed: a carrier frequency is a property of the
disease's whole allele pool, and 18 of the 106 carrier records sit in entries
with more than one causal gene, where (b) has no single gene to attach to.
Bands on carrier records also discriminate nothing (78 of the 86 banded ones
are `ABOVE_1_IN_1000`, because carrier frequency is roughly the square root of
disease frequency).
*Recommend: (c) as an advisory, not a gate: keep the measure on `Prevalence`,
report a numeric band on a carrier record as a lead, and do not migrate the
86. Revisit (b) only if a per-gene carrier slot is wanted for its own sake.*

**D3. Give the homeless measures a home.** Add to `PrevalenceMeasureEnum`:
`SCREEN_POSITIVE_RATE` and `SCREEN_DETECTED_INCIDENCE` (#7003), and
`PROPORTION_OF_CASES` for "share of an ascertained clinical group that has this
disease" (#7003's second shape, #11726, #11268). Add `ASCERTAINED_COHORT` to
`RateDenominatorEnum`, required whenever `measure_type` is
`PROPORTION_OF_CASES`, with the cohort named in `population` and its size, when
reported, in a new optional `denominator_size` slot. A numeric band is invalid
with an `ASCERTAINED_COHORT` denominator, because the bands are read as
population rarity. The alternative, a separate `CohortProportion` class, is
more principled and is the pattern `GeneCaseFraction` set; it costs a new
section, a renderer block and a KGX decision, and would still leave
`rate_per_100000` on the records written so far.
*Recommend: the enum route now, as additive and reversible; record the class
route as the follow-up if proportion records multiply.*

**D4. Survival, mortality and penetrance.** Penetrance goes to
`Inheritance.penetrance_percentage` (exists, under-used). Survival and
case-fatality have no slot. They are outcome rates, not occurrence, so they do
not belong on `Prevalence` under any `measure_type`.
*Recommend: a small `outcomes:` or `survival:` slot is a separate schema
proposal; until it exists these figures stay in prose (`notes` on
`progression:` or `clinical_burden`) and are listed by the Phase 0 report as
`NO_HOME` so the count is visible.*

**D5. Names.** `Prevalence`, `prevalence:` and `prevalence_class` stay.
Renaming touches 2,885 files for no change in meaning, and §8 already records
the debt. A LinkML slot alias (`occurrence`) could be added later at no
migration cost if a consumer wants it.
*Recommend: no rename.*

**D6. Requiredness and removal.** End state: `measure_type` required on every
record; `rate_denominator` required when `measure_type` is `ANNUAL_INCIDENCE`
or `PROPORTION_OF_CASES`; `percentage` removed from the schema. The schema has
no LinkML `rules:` blocks today, so conditional requiredness is a repo check
until one is added, and `linkml-validate` carries only the unconditional part.
*Recommend: adopt as the end state; reach it in Phase 4, never before the
backfills are done.*

**D7. One home for occurrence figures.** `prevalence:` holds every population
or cohort occurrence measure. `epidemiology:` holds everything else about the
epidemiology of a disease (sex ratio, age at onset, geographic pattern, time
trend, mortality until D4 lands). An occurrence figure in `epidemiology:` is a
lead for relocation, never auto-moved.
*Recommend: adopt as a written rule in CLAUDE.md and §8; audit the 207 files
in Phase 3 as a worklist.*

**D8. Boundaries.** Bands are half-open intervals matching `_band_from_rate()`:
`[0.1, 1)`, `[1, 10)`, `[10, 100)`, `[100, ∞)`, `(0, 0.1)`. The enum
descriptions are corrected to say so. A rate sitting exactly on a boundary with
the band below it **is** a disagreement under the enum's own text (#10193's
triage), but it is reported as its own class because its fix runs two ways: a
source that says "less than 1 in a million" wants `rate_high: 0.1` and no point
rate; a source that says "1 in a million" wants the band relabelled.
*Recommend: adopt; the check never guesses the direction.*

## 4. Phases

Each phase is independently reviewable and leaves `main` in a consistent
state. KB tranches are small and path-scoped because 509 PRs are open against
this repository today, many of them touching `kb/disorders/`.

### Phase 0: inventory and tracker (code and issues only; no KB edits)

- [ ] **A report script**, provisionally `scripts/check_prevalence_records.py`
  with `just check-prevalence-records`, that walks every `prevalence:` record
  and classifies findings: `BAND_RATE_DECADE`, `BAND_RATE_BOUNDARY`,
  `BAND_RATE_NEAR`, `QUALITATIVE_ON_INCIDENCE_OR_CARRIER`,
  `QUALITATIVE_WITH_RATE`, `ZERO_RATE`, `INCIDENCE_NO_DENOMINATOR`,
  `NO_MEASURE_TYPE`, `UNKNOWN_WITH_RATE`, `PERCENTAGE_REDUNDANT`,
  `PERCENTAGE_ONLY`, `CARRIER_WITH_BAND` (advisory), `COHORT_LABEL`
  (advisory: `population` names a patient group). `--format summary|list|tsv`,
  `--strict`, and the `--against-ref origin/main` baseline mechanism of
  `scripts/check_snippet_length.py` so `just qc` and CI agree. Report-only
  at first; wired into `just qc` and as an ungated whole-KB CI step, the way
  `check-duplicate-keys` is, because a `kb/`-only PR skips the Python lane.
  The message for a band finding quotes the band's numeric range, not its key.
- [ ] **The CLAUDE.md example-slot guard** (lesson 7), as a test.
- [ ] **One tracker issue** absorbing #7005, #10193 (already labelled
  duplicate), #8431, #9723, #7003 and #11726, with #11268 linked as adjacent.
  Its body is the decision list in §3 with each item marked decided or open,
  and a row per phase naming the deliverable and its owner. Close the absorbed
  issues with a pointer once the tracker exists.
- [ ] Fix the two enum descriptions (D8) in the same schema-only PR as the
  script, since they change no value.

Code-only, no conflict surface; can be delegated to an agent under the
tracker's named owner.

### Phase 1: decide (one design-decisions amendment, one schema PR, no KB edits)

- [ ] Record D1-D8 as a second §8 amendment, with whatever the review changed.
- [ ] Schema PR: the new enum values and `denominator_size` (D3), the
  corrected descriptions, and the CLAUDE.md prose for D7 and the new values.
  Additive only; no existing record becomes invalid. Regenerate the datamodels.
- [ ] Extend the Phase 0 script with the rules the new values imply
  (`PROPORTION_WITHOUT_COHORT_DENOMINATOR`, `BAND_ON_COHORT_DENOMINATOR`).

Schema-only, no conflict surface; delegable in the same way, reviewed as
#10758 was.

### Phase 2: gate the deterministic classes and clear their backlog

The deterministic classes are the ones with no judgement in them: a decade
error, a qualitative tier on an incidence or carrier record, a qualitative tier
beside a rate, a zero rate on a case-count record. The classes overlap (the
five zero-rate `ULTRA_RARE` records are also qualitative-beside-a-rate; five of
the eight qualitative-on-incidence records are too), so the union is about 56
records today, plus the 33 exact-boundary and 3 near-boundary band findings.
Every one is fixable from the record's own `notes` and cached evidence with no
literature search.

- [ ] Flip `BAND_RATE_DECADE`, `QUALITATIVE_ON_INCIDENCE_OR_CARRIER`,
  `QUALITATIVE_WITH_RATE` and `ZERO_RATE` (excluding a documented true zero)
  to gating with the baseline, so new instances fail immediately while the
  backlog is worked.
- [ ] Clear the backlog in tranches of at most 25 files, each with history
  records, each listing the finding ids it retires, and each checked against
  the open-PR list for the files it touches before the branch is cut.
  Boundary cases (`BAND_RATE_BOUNDARY`, 33 today) go in their own tranche
  because each needs the D8 direction read from `notes`.
- [ ] Shrink the baseline to zero and remove the mechanism, as
  `check-environmental-evidence` and `check-folded-hyphens` did.

Tranches can be delegated to agents; the owner sequences them against the
open-PR list and the reviewer re-derives each fix from the record's own
evidence. This and every later phase is the long-running, person-overseen
work the issue describes, not a one-shot job.

### Phase 3: source-dependent backfills, owner-driven

Nothing in this phase may be inferred. Each record is read against its cached
source, and a record whose source does not state the value stays as it is,
with the gap named in `notes`.

- [ ] **Incidence denominators** (148 today), routed by the text lead:
  "person-years" (32), "per year"/"annual" (90), "births" (3), no lead (23).
  The lead chooses the tranche; the source chooses the value.
- [ ] **`measure_type` absent** (250), then **`UNKNOWN` with a rate** (41,
  mostly candidates for the D3 values), then the remaining `UNKNOWN` where the
  source does name a measure.
- [ ] **Redundant `percentage`** (411): delete mechanically **after** a
  per-record check that the parsed `percentage` agrees with the structured
  rate and band; a disagreement is routed to a person, not resolved by the
  script. This is the one bulk edit in the plan, and it removes a copy rather
  than changing a value.
- [ ] **`percentage`-only** (56): relocate by class under D3 and D4, delete the
  prose-only ones into `notes`, and leave the `NO_HOME` survival figures listed
  until D4 has a slot.
- [ ] **`epidemiology:` audit** (207 files): list occurrence figures held there
  and relocate them to `prevalence:` as a worklist.

### Phase 4: tighten and close

- [ ] `measure_type` required; `percentage` removed from the schema once the
  report shows zero; the conditional denominator requirement as a gating
  check (D6).
- [ ] Flip the remaining advisory classes that have reached zero to gating.
- [ ] Update §8 and CLAUDE.md without date-stamped counts; point readers at
  the script for figures.
- [ ] Close the tracker.

## 5. Risks

- **Conflicts with in-flight curation.** The mitigation is tranche size,
  the open-PR check per file, and never a whole-KB rewrite. The one bulk step
  (deleting redundant `percentage`) touches 325 files and should run in a quiet
  window as several path-scoped PRs.
- **A gate that is wrong is worse than none.** Every class is advisory first
  and gated only after a human has read its findings; the boundary class is
  kept apart so a correct `rate_high` is never flagged as an error.
- **Inference creeping back in.** The Phase 3 rule is absolute. A hint in
  `notes` routes a record; it never fills a slot.
- **Scope growth.** D4 (survival) and the `CohortProportion` class are
  recorded as follow-ups, not folded in. #11268 is adjacent and stays its own
  issue.

## 6. Reproducing the counts

Until the Phase 0 script exists, the table in §1b is reproduced by walking
`kb/disorders/*.yaml` with `dismech.yaml_io.safe_load_path`, taking each
`prevalence[]` item, and applying the rule in the table's third column, with
`_band_from_rate()` from `scripts/migrate_prevalence.py` as the band oracle.
