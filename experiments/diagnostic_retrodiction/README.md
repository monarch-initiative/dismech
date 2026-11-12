# DRAFT — not yet preregistered

# Diagnostic retrodiction

Could the knowledge base have anticipated a diagnostic test before it existed?
Each case in this experiment is a disease and a blood, urine or CSF test that
became its diagnostic route after 1985: anti-PLA2R for membranous nephropathy,
for example. For each case, the disease is curated again using only literature
published before the test's discovery, and an arm then proposes tests from that
time-sliced entry. The question is how often the real test is among them.

This measures the KB without changing it. `kb/` is read, at the commit pinned in
`PINNED_COMMIT` (`2a931df2ac7`), to build the sampling frame and is never
written. Every artifact lives in this directory. The time-sliced curations will
also live here, not in `kb/`.

Everything below describes what has actually been done, with numbers from the
committed files. Items marked **[PLACEHOLDER]** are design decisions that no
committed file records yet.

## Hypotheses

- **H1.** A2 (graph + LLM) proposes the real test more often than A3
  (literature only).
- **H2.** Structure matters. A1 and A2 do better than A5 (scrambled graph),
  and A6 (path ablation) does worse than A2.
- **H3.** The arms' confidence separates real positives from negative controls.

## Endpoints

**Primary.** Top-10 tier-2 hit rate, A2 vs A3, compared with an exact McNemar
test on the paired per-case outcomes. A case is a hit when the real test is
among an arm's top 10 proposals at tier T2 or better (see *Scoring*).

**Secondary**, each reported separately and not used to rescue the primary:
- H2: the top-10 tier-2 hit rate for A1 vs A5, for A2 vs A5, and for A2 vs A6.
  **[PLACEHOLDER: which comparisons are confirmatory, and whether they are
  corrected for multiplicity.]**
- H3: separation of confidence between positives and negative controls.
  **[PLACEHOLDER: the metric, for example AUROC, and the confidence scale each
  arm reports.]**
- Hit rates at each tier T1–T4, and at top-1 and top-5.
  **[PLACEHOLDER: confirm which cut-offs are reported.]**
- A2′ vs A3′. **[PLACEHOLDER: depends on the definition of the primed arms.]**

## Arms

| Arm | Description |
|---|---|
| A1 | **[PLACEHOLDER]**, a structured-graph arm (H2 compares it with A5) |
| A2 | Time-sliced graph + LLM |
| A3 | Literature only: the same packet, no graph |
| A4 | **[PLACEHOLDER]** |
| A5 | A2 with the graph scrambled |
| A6 | A2 with a path ablation **[PLACEHOLDER: which paths are removed]** |
| A7 | **[PLACEHOLDER]** |
| A2′ | **[PLACEHOLDER]**, a variant of A2 |
| A3′ | **[PLACEHOLDER]**, a variant of A3 |

## Case selection, as done

### Sampling frame

`census.py` walks every `kb/disorders/` entry at the pinned commit and writes one
row per `diagnosis[]` and `biochemical[]` item to `frame.tsv`: **11,614 rows over
4,042 entries**. A row is flagged when its specimen resolves to blood, urine, CSF
or a dried blood spot and it is not a germline genetic test. **3,311 rows are
flagged.** `specimen_basis` records how each specimen was inferred: stated in
prose, from a LOINC code, or implicit from the analyte class.

### Recall check

`known_positives.tsv` lists 22 disease/test pairs the frame ought to contain.
`check_recall.py` finds **19/22 (86.4%)**, with no matcher misses
(`recall_report.tsv`). The three misses are KB gaps, not frame defects: no
dismech row records the VGCC antibody for Lambert-Eaton, CALR for essential
thrombocythemia, or EMA binding for hereditary spherocytosis.

### Specimen check

Of the 284 rows whose specimen was implicit, **59 (20.8%) were WRONG_SPECIMEN**:
the assay actually runs on fibroblasts, muscle, marrow, tumour tissue or an in
vitro system. By implicit class: ENZYME_ACTIVITY 40/61, FLOW_CYTOMETRY 9/42,
SOMATIC_HEME_DRIVER 6/18, AUTOANTIBODY 4/160, CIRCULATING_METABOLITE 0/3.

### Eligibility rules, versions 1 to 3

The rules are in `eligibility_rules.md` (version 3), with `eligibility_rules.v1.md`
and `eligibility_rules.v2.md` kept. `eligibility_work/build_eligibility.py`
rebuilds `eligibility.tsv` from `frame.tsv` and the judgment tables, and
`--check` confirms the result is byte-identical.

- **Version 1** gave 80 INCLUDE rows. A row is INCLUDE when the test became the
  primary diagnostic route, replacing biopsy, invasive or specialist testing, or
  clinical criteria, and can be dated to one primary report from 1985 on. Ten
  exclusion reasons apply.
- **Version 2** followed the screener B comparison, which found 15 of 31
  disagreements came from wording (`eligibility_disagreements.tsv`). It added:
  - **rule 1:** subset tests;
  - **rule 2:** a computed pre-test literature count;
  - **rule 3:** IMPROVEMENT only for a new analyte;
  - **rule 4:** combined rows judged on their accessible component;
  - **rule 5:** dating to the first primary research report.

  Under version 2, 66 decisions changed (`eligibility_v2_changes.tsv`).
- **Version 3** removed rule 2's count. It searched the entry's own name, so
  entries named after later or qualified terms failed regardless of their
  literature. This moved 44 decisions back (`eligibility_v3_changes.tsv`).
  DISEASE_DEFINED_BY_TEST is a judgment again, and a computed literature check
  applied after dating replaced the count (see *Dating*).

### Screeners

- **Screener B** decided 453 rows blind: every row of the 52 diseases screener A
  had included, plus 300 rows from whole diseases drawn at random
  (`screenerB_input.tsv`).
  - Against A's version 1 decisions, agreement was **422/453 (93.2%)**, **Cohen's
    kappa 0.726** (`compare_screeners.py`). That script reproduces the comparison
    from commit `528cef7e51a`.
  - Of the 31 disagreements, 15 were wording ambiguity, 15 were facts, and 1 was
    screener A departing from its own written rule.
- **Screener C** decided the 15 facts disagreements, and the 2-of-3 majority
  is final. Recomputed under version 3, A was outvoted on 13 of them
  (`eligibility_resolution.tsv`; `eligibility_work/ov9_resolution.txt`).
- **Screener B2** re-screened rule 1 blind on 32 rows (`screenerB2_input.tsv`):
  - Those rows were the 16 INCLUDE because of rule 1, plus 16 drawn from 18
    subset-type EXCLUDE rows.
  - Agreement was **27/32 (84.4%)**, **kappa 0.688**.
  - Screener C2 decided the 5 disagreements in a fresh session, from
    `prompts/screenerC2.md`. B2 and C2 agreed every time and A was outvoted on
    all 5 (`eligibility_rule1_rescreen.tsv`).

Final eligibility: **71 INCLUDE rows covering 48 entries**.

### Cases

`build_cases.py` collapses the 71 INCLUDE rows into **57 cases** (`cases.tsv`):
one per disease–test pair, 48 entries, 42 `test_group`s.
- A test recorded twice in one entry (a diagnosis and a biochemical row, or
  serum and CSF) is one case.
- The same test under several entries is one case per entry, linked by
  `test_group`. For example, AQP4-IgG appears in NMOSD, optic neuritis and
  transverse myelitis.

Of the 22 known positives, 13 are cases (`known_positives_cases.tsv`): 6 are
excluded by an eligibility rule and 3 are KB gaps.

## Dating, as done

- **Two dating agents** each named a first primary report for every case, with a
  verbatim abstract quote (`dating.agentA.tsv`, `dating.agentB.tsv`).
  `check_dating.py` checked both against PubMed (`dating_checks/`).
  - It confirms the quote appears in the abstract.
  - It sets the publication date to the earlier of the journal issue date and
    the e-publication date.
  - It counts earlier PubMed hits for the analyte and disease.

  Every quote from both agents passed.
- **Cutoff rule.** A PMID is accepted only when both agents give the same PMID
  and both quotes pass. The cutoff is 31 December of the year before the
  discovery date.
  - The result: **41 ACCEPTED**, **6 ACCEPTED_FLAGGED** (an earlier paper looks
    like the real discovery report) and **10 NOT_ACCEPTED** (the agents
    disagree).
  - The 16 flagged and not-accepted cases are listed with written assessments in
    `dating_flags.tsv`.
  - `build_dating.py` writes `dating.tsv` and records a mechanistic-readiness
    judgment for each case with a cutoff.
- **Literature sufficiency.** `check_pretest_era.py` counts PubMed records with
  abstracts on or before each verified cutoff. The query ORs together:
  - the disease's MeSH heading;
  - its MONDO label and exact synonyms (read with `runoak` from the local MONDO
    build);
  - a `literature_alias` where one is set.

  A count below `RUN_CONFIG`'s `packet_minimum` (30) is
  INSUFFICIENT_PRE_CUTOFF_LITERATURE (`literature_check.tsv`).
  - **Alias fix.** MONDO labels for subtype entries are often catalogue forms no
    abstract uses, such as "diabetes insipidus, nephrogenic, X-linked". So the
    first run failed 17 cases. `literature_recount.py` recounted them under plain
    literature names (`literature_recount.tsv`), and those names became each
    case's `literature_alias`.
  - **Rerun.** On the rerun, 10 of the 17 passed.

### Final counts

| test_class | Cases | PASS | Dropped (insufficient) | Unverified cutoff |
|---|---|---|---|---|
| AUTOANTIBODY | 24 | 15 | 1 | 8 |
| METABOLITE | 12 | 5 | 1 | 6 |
| SECRETED_PROTEIN | 7 | 7 | 0 | 0 |
| OTHER | 7 | 4 | 3 | 0 |
| ENZYME_ACTIVITY | 5 | 2 | 2 | 1 |
| CELL_SURFACE_MARKER | 1 | 0 | 0 | 1 |
| SOMATIC_VARIANT | 1 | 1 | 0 | 0 |
| **Total** | **57** | **34** | **7** | **16** |

- **The 7 dropped:** anti-NMDAR encephalitis, congenital TTP, Immunodeficiency
  18, Immunodeficiency 19, MNGIE ×2 and Revesz syndrome. They stay listed in
  `literature_check.tsv`.
- **`dating.tsv`** holds the other 50: 34 PASS and 16 unverified, in 39 test
  groups. The 34 PASS cases are in 29 test groups. 30 of them are FIRST and 4
  are IMPROVEMENT; 29 have mechanistic readiness "yes" and 5 "no".

## Curation protocol

- **Packets.** For each case, `build_packet.py` builds a PubMed literature packet
  from a query and `--maxdate` (the cutoff). It keeps only records with an
  abstract and a publication date on or before the cutoff. The packet is the
  only literature the time-sliced curation may cite.
- **Gate.** `check_cutoff.py` fails a time-sliced entry that:
  - cites a PMID outside its packet;
  - cites a non-PMID reference;
  - contains a banned post-cutoff term;
  - keeps present-day `has_subtypes`;
  - has a pathophysiology node with no evidence.
- **Replicates.** Two independent curation replicates per case, each in an
  isolated git worktree, with web access denied. Answer-bearing files are
  excluded from the worktree: at least the disease's own `kb/` entry, and this
  directory's eligibility, case and dating files. **[PLACEHOLDER: the exact
  exclusion list, and how web denial is enforced.]**
- **Audit.** Each replicate's tool log and output are checked for access to
  excluded files or post-cutoff material. **[PLACEHOLDER: the audit procedure
  and pass criteria.]**

None of this has been run. No packet, banned-term list or time-sliced entry is
committed yet.

## Leakage measures

In place now:
- `build_packet.py` dates each record by the earliest of its issue and
  e-publication dates.
- `check_cutoff.py` enforces packet-only citation and the banned-term list.
- Screener inputs carried frame columns only (`select_screenerB.py`,
  `select_screenerB2.py`).

Planned: the isolated worktrees and the audit above. Two leakage routes are
known and not yet closed:
- PubMed dates Bookshelf chapters (GeneReviews) 1993, the start of the series,
  so they can pass a date filter they should fail. They appeared as false
  earlier hits in `check_dating.py` output.
- The banned-term lists are not yet written. **[PLACEHOLDER]**

## Scoring and adjudication

| Tier | Meaning |
|---|---|
| T1 | **[PLACEHOLDER]** |
| T2 | **[PLACEHOLDER]**: the primary endpoint's threshold |
| T3 | **[PLACEHOLDER]** |
| T4 | **[PLACEHOLDER]** |

Adjudicators blind to arm identity assign each proposed test a tier.
**[PLACEHOLDER: the rubric (`rubrics/` is empty), the number of adjudicators,
and the disagreement procedure.]**

## Analysis plan

- **Unit and clustering.** The unit is the case. Cases sharing a `test_group` are
  not independent: an arm that finds AQP4-IgG once will tend to find it for all
  three of its entries. The primary McNemar test treats cases as independent.
  A sensitivity analysis keeps one case per test_group, and a cluster bootstrap
  over test groups is also reported. **[PLACEHOLDER: the rule for choosing the
  representative case.]**
- **Sample size.** At most 50 cases, and currently 34 with a verified cutoff, in
  29 test groups. Exact two-sided McNemar at α = 0.05 can only reach
  significance on enough discordant pairs:
  - 5 or fewer: never;
  - 6: a 6:0 split;
  - 10: at least 9:1;
  - 20: at least 15:5.

  The study can detect a large difference between A2 and A3. It is not powered
  for a moderate one, and a null result will not show the arms are equivalent.

## Pending before prereg-v1

- [ ] Resolve the 16 UNVERIFIED_CUTOFF cases: human review of `dating_flags.tsv`.
- [ ] Propagate the literature exclusion into `eligibility.tsv` and `cases.tsv`.
  They still count the 7 dropped cases as INCLUDE.
- [ ] Negative controls and decoys for H3.
- [ ] The development/test split.
- [ ] The coverage audit (`coverage_audit/` is empty).
- [ ] Scoring rubrics (`rubrics/` is empty) and banned-term lists.
- [ ] Finalise `RUN_CONFIG`. It holds only `packet_minimum: 30`, marked provisional.
- [ ] Register on OSF.
- [ ] Define every **[PLACEHOLDER]** above: arms A1, A4, A7, A2′, A3′; tiers
  T1–T4; secondary metrics; adjudication; the exclusion list; the audit.

## Limitations

- **The frame is limited to what dismech records.** A test absent from the KB
  cannot be a case: 3 of 22 known positives are KB gaps.
- **Specimen and genetics flags are text heuristics** over curation prose. One
  in five implicit-specimen rows was wrong.
- **Most eligibility decisions are one screener's.**
  - Screener A decided all 3,311 rows.
  - 1,619 reasons are individually judged, 675 come from pattern rules, and
    1,017 are a scanned default, the least specific reason.
  - Screeners B and B2 re-screened 453 and 32 rows.
- **Most dates in the eligibility reasons are from memory and unverified.** Only
  the 57 cases were dated against PubMed.
- **The discovery date itself is uncertain** for 16 cases. Even where both agents
  agree, 6 accepted PMIDs look later than the real discovery report.
- **The aliases are hand-written** for the 17 cases that needed them, and
  `hasabstract` undercounts literature from before about 1975.
- **Mechanistic-readiness and flag assessments are one agent's judgment** from
  titles and abstracts. Some readiness calls rest on weak evidence.
- **Test groups cluster the cases**, and the sample is small (see *Analysis
  plan*).

## Files

| File | What it is |
|---|---|
| `PINNED_COMMIT` | the `kb/` commit the frame was built from |
| `RUN_CONFIG` | run parameters (YAML); currently `packet_minimum` only |
| `census.py` | builds `frame.tsv` from `kb/disorders/` |
| `frame.tsv` | the frozen sampling frame, one row per diagnosis/biochemical item |
| `known_positives.tsv` | 22 disease/test pairs the frame should contain |
| `check_recall.py` | measures frame recall against the known positives |
| `recall_report.tsv` | frozen per-pair recall result |
| `eligibility_rules.md` | eligibility rules, version 3 |
| `eligibility_rules.v1.md` | eligibility rules, version 1 |
| `eligibility_rules.v2.md` | eligibility rules, version 2 |
| `eligibility.tsv` | the decision and reason for every flagged row, plus 3 KB gaps |
| `eligibility_review.tsv` | seeded INCLUDE sample plus ambiguous EXCLUDE rows, for review |
| `eligibility_v2_changes.tsv` | decisions changed by version 2 |
| `eligibility_v3_changes.tsv` | decisions changed by version 3 |
| `eligibility_work/build_eligibility.py` | rebuilds `eligibility.tsv` and `eligibility_review.tsv` |
| `eligibility_work/ov1.txt` | version 1 judgments, rows 0–405 |
| `eligibility_work/ov2.txt` | version 1 judgments, second block |
| `eligibility_work/ov3.txt` | version 1 judgments, third block |
| `eligibility_work/ov4.txt` | version 1 judgments, fourth block |
| `eligibility_work/ov5.txt` | version 1 judgments, fifth block |
| `eligibility_work/ov6.txt` | version 1 judgments, sixth block |
| `eligibility_work/ov7.txt` | version 1 judgments, rule-flagged groups |
| `eligibility_work/ov8_v2.txt` | judgments for rules 1, 3, 4 and 5 |
| `eligibility_work/ov9_resolution.txt` | screener-majority decisions on the facts disagreements |
| `eligibility_work/ov10_rule1_rescreen.txt` | screener-majority decisions from the rule-1 re-screen |
| `eligibility_work/subset_v2.txt` | the subset of each rule-1 INCLUDE row |
| `eligibility_work/wrong.txt` | the 59 WRONG_SPECIMEN rows |
| `eligibility_work/infectious_names.txt` | KB entries that declare an infectious agent |
| `eligibility_work/resolve_facts.py` | majority resolution for the facts disagreements |
| `eligibility_work/resolve_rule1_rescreen.py` | majority resolution for the rule-1 re-screen |
| `eligibility_work/version_changes.py` | writes the v2 and v3 change lists |
| `select_screenerB.py` | selects screener B's blinded input |
| `screenerB_input.tsv` | screener B's 453 input rows |
| `eligibility.screenerB.tsv` | screener B's decisions |
| `compare_screeners.py` | A vs B comparison, reproduced from 528cef7e51a |
| `eligibility_disagreements.tsv` | the 31 A/B disagreements, with cause and note |
| `eligibility.screenerC.tsv` | screener C's decisions on the facts disagreements |
| `eligibility_resolution.tsv` | decisions the facts resolution changed |
| `select_screenerB2.py` | selects the rule-1 re-screen input |
| `screenerB2_input.tsv` | screener B2's 32 input rows |
| `eligibility.screenerB2.tsv` | screener B2's decisions |
| `prompts/screenerC2.md` | the instruction given to screener C2 |
| `screenerC2_input.tsv` | screener C2's 5 input rows |
| `eligibility.screenerC2.tsv` | screener C2's decisions |
| `eligibility_rule1_rescreen.tsv` | the 5 re-screen disagreements and outcomes |
| `build_cases.py` | collapses INCLUDE rows into cases |
| `cases.tsv` | the 57 cases |
| `known_positives_cases.tsv` | which known positives are cases, and why not |
| `dating.agentA.tsv` | agent A's discovery PMIDs and quotes |
| `dating.agentB.tsv` | agent B's discovery PMIDs and quotes |
| `check_dating.py` | verifies a dating file against PubMed |
| `dating_checks/agentA.checked.tsv` | `check_dating.py` output for agent A |
| `dating_checks/agentB.checked.tsv` | `check_dating.py` output for agent B |
| `build_dating.py` | merges the agents into `dating.tsv`, flags and spot-check |
| `dating.tsv` | the 50 dated cases that pass or await the literature check |
| `dating_flags.tsv` | 16 cases needing review, with assessments |
| `dating_spotcheck.tsv` | 8 unflagged accepted cases for spot-checking |
| `check_pretest_era.py` | counts pre-cutoff literature per case |
| `literature_check.tsv` | the literature check for all 57 cases |
| `literature_recount.py` | advisory recount under plain disease names |
| `literature_recount.tsv` | that recount, for the 17 cases that first failed |
| `build_packet.py` | builds a date-limited PubMed packet |
| `check_cutoff.py` | gates a time-sliced entry against its packet |
| `prompts/`, `rubrics/`, `schemas/`, `coverage_audit/` | `prompts/` holds only `screenerC2.md`; the others are empty |
