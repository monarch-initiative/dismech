# DRAFT — not yet preregistered

# Diagnostic retrodiction

Could the knowledge base have anticipated a diagnostic test before it existed?
Each case in this experiment is a disease and a blood, urine or CSF test that
became its diagnostic route after 1985: anti-PLA2R for membranous nephropathy,
for example. For each case, the disease is curated again using only literature
published before the test's discovery, and an arm then proposes tests from that
time-sliced entry. The question is how often the real test is among them.

## Status and next session

Status at 2026-11-12. The protocol below is a draft; nothing has been run on
any arm.

**Done today:**
- Negative controls (`negatives.tsv`) and decoys from one fixed PubMed query
  (`decoys.tsv`).
- Coverage audit of the negatives and the frame entries without an accessible
  test (`coverage_audit/`).
- Literature-check alias fix; stratified dev/test split, with the dev set now
  frozen at 5 cases.
- Draft protocol, with every placeholder filled; deny rules for the curation
  sessions.
- Agent C dated the 10 cases A and B disagreed on. 6 became MAJORITY_VERIFIED
  and received mechanistic-readiness judgments.
- Literature aliases for C001 and C052, both of which then passed the
  literature check.
- Human review sheet for the 10 cases still unresolved.

**Next, in order:**
1. Human review of the 10 cases in `dating_review_sheet.md`, recorded in
   `dating_human_review.tsv`.
2. Apply the review: settle each cutoff in `build_dating.py`, rerun the
   literature check, add readiness judgments, and rerun `make_split.py`. The
   dev set stays frozen.
3. Settle the open decisions:
   - how an LLM arm's 3 runs become one outcome per case;
   - which curation replicate feeds the arms;
   - what cutoff the negatives are curated and prompted as of;
   - whether to expand the negatives, since only 3 qualify for the primary
     H3 analysis;
   - Alzheimer disease, which is both a decoy (D009) and dev case C003;
   - the second model family.
4. Propagate the literature exclusion to `eligibility.tsv` and `cases.tsv`.
5. Write the rubrics and, from them, the banned-term lists.
6. Write `audit_transcript.py`, A1's node-type table and weights, the prompts,
   the candidate schema, and `DEVIATIONS.md`.
7. Tag prereg-v1 and register on OSF.

## Why retrodiction measures the KB without changing it

A prospective test of the KB would mean adding a prediction and waiting years
for the field to confirm or refute it. Retrodiction uses tests whose discovery
date is known, rebuilds the entry as it could have been written before that
date, and checks the proposals against what happened. Nothing is written to
`kb/`.
- **Frame source.** `kb/` is read once, at the commit in `PINNED_COMMIT`
  (`2a931df2ac7`), to build the sampling frame.
- **Where outputs go.** The time-sliced curations, packets and scores will
  live in this directory.
- **Guard.** `git diff --stat origin/main -- kb/ src/ references_cache/` is
  empty at every commit on this branch.

Sections headed "as done" describe work already carried out, with numbers from
the committed files. The remaining sections state the protocol as decided but
not yet run. Run parameters are in `RUN_CONFIG.yaml`.

## Hypotheses

- **H1.** A2 (graph + LLM) proposes the real test more often than A3
  (literature only).
- **H2.** Structure matters: A1 and A2 do better than A5 (scrambled graph),
  and A6 (path ablation) does worse than A2.
- **H3.** The arms' confidence separates real positives from negative controls.

## Endpoints

**Primary.** Top-10 tier-2 hit rate, A2 vs A3, by exact McNemar test on the
paired per-case outcomes. A case is a hit when the real test is among an arm's
top 10 proposals at tier T2 or better (see *Scoring*).

**Secondary.** Each is reported separately and none is used to rescue the
primary.
- **H2, confirmatory:** top-10 tier-2 hit rate, A2 vs A5, exact McNemar. This
  is the one confirmatory secondary test.
- **H2, exploratory** (labelled so wherever reported): A1 vs A5 and A2 vs A6,
  same metric and test. No multiplicity correction is applied to
  exploratory tests.
- **H3, confidence:** every arm gives each candidate a confidence from 0 to 1.
  - A case's confidence is the maximum over its candidates.
  - The metric is the AUROC of case confidence, positives vs negatives, with
    a 95% CI from a bootstrap over test groups. Each negative is its own
    cluster.
  - The primary H3 analysis uses only positive cases and negatives whose graph
    has at least one node passing the coverage audit's measurable-node rule
    (see *Coverage audit*). AUROC over all cases and negatives, and the
    results stratified by coverage, are also reported.
- **H3, decoys:** scored separately. For each arm, the fraction of decoy
  diseases (`decoys.tsv`) where the decoy biomarker appears in the arm's top
  10.
- **Cut-offs:**
  - hit rates for each of T1–T4 at top-10;
  - T2 hit rates at top-1, top-3, top-5 and top-10;
  - mean reciprocal rank of the first T2 hit (0 when there is none in the
    top 10).
- **A2′ vs A3′:** a robustness check reported with the same exact McNemar
  test. Not confirmatory.

## Arms

| Arm | Input | Method |
|---|---|---|
| A1 | Time-sliced entry | Graph only, no LLM (below) |
| A2 | Time-sliced entry + packet | LLM proposes tests from the graph |
| A3 | Packet only | LLM proposes tests from the literature, no graph |
| A4 | Disease name and cutoff year only | LLM prompted "It is <cutoff year>…", same candidate schema |
| A5 | A2 with the causal edges scrambled | As A2 |
| A6 | A2 with a path ablated | As A2 |
| A7 | The entry at `PINNED_COMMIT`, with the test's own `diagnosis`/`biochemical` rows and every node or evidence item containing a banned term removed | As A2 |
| A2′ | A2's inputs and prompts | Run on a second model family |
| A3′ | A3's inputs and prompts | Run on a second model family |

The second model family is named in `RUN_CONFIG.yaml`.

**A1, the graph-only arm.**
- **Candidates:** every node of the time-sliced entry that passes
  `coverage_audit/audit.py`'s measurable-node rule.
- **Specificity:** 1 minus the fraction of comparison pathographs containing
  the node's term or a direct parent or child of it (OAK). It is computed
  twice: against the pathographs of the case's resolved differential
  diagnoses, and against all pathographs.
- **Score:** the mean of the two specificities, or the all-pathograph
  specificity alone when no differential resolves. That is multiplied by
  1 / (1 + causal distance from the root-cause node).
- **Mapping:** the top-scoring nodes are mapped to test candidates through a
  fixed table from node type to `analyte_type`.
- **Weights:** fixed before the dev set is run and never tuned on the test
  set.

**A5, scrambled graph.**
- **Scramble:** degree-preserving double-edge swaps of the causal edges, 10 ×
  the edge count, with node content unchanged.
- **Repeats:** three seeded scrambles per case, results averaged.

**A6, path ablation.**
- **Path:** the nodes on causal paths from the root cause to the node that
  matches the rubric's T1 mechanism.
- **Levels:** 25%, 50%, 75% and 100% of those nodes are removed, seeded,
  nearest to the target first.
- **No match:** if no node matches T1, A6 is NA for that case.

**LLM arms (A2–A7, A2′, A3′).** Each runs 3 times per case at temperature 0
where the model supports it (`RUN_CONFIG.yaml`). Each proposes up to k = 10
candidates, each with a confidence from 0 to 1.

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

Of the 284 flagged rows whose specimen was implicit, **59 (20.8%) were
WRONG_SPECIMEN**: the assay actually runs on fibroblasts, muscle, marrow,
tumour tissue or an in vitro system (`eligibility_work/wrong.txt`). By
implicit class:

| Implicit class | Wrong / total |
|---|---|
| ENZYME_ACTIVITY | 40/61 |
| FLOW_CYTOMETRY | 9/42 |
| SOMATIC_HEME_DRIVER | 6/18 |
| AUTOANTIBODY | 4/160 |
| CIRCULATING_METABOLITE | 0/3 |

### Eligibility rules, versions 1 to 3

The rules are in `eligibility_rules.md` (version 3), with `eligibility_rules.v1.md`
and `eligibility_rules.v2.md` kept. `eligibility_work/build_eligibility.py`
rebuilds `eligibility.tsv` from `frame.tsv` and the judgment tables;
`--check` confirms the result is byte-identical.

| Version | INCLUDE rows | Commit |
|---|---|---|
| 1 | 80 | `74eeed61936` |
| 2 | 32 | `70c47e11be0` |
| 2, after screener C | 28 | `ed61c89ef68` |
| 3 | 72 | `03b1f051556` |
| 3, after the B2 re-screen | **71** | `3b91da9d539` |

- **Version 1.** A row is INCLUDE when the test became the primary diagnostic
  route and can be dated to one primary report from 1985 on. "Primary route"
  means it replaced biopsy, invasive or specialist testing, or clinical
  criteria. Ten exclusion reasons apply.
- **Version 2** followed the screener B comparison, which traced 15 of 31
  disagreements to wording (`eligibility_disagreements.tsv`). It added five
  rules:
  1. subset tests;
  2. a computed pre-test literature count;
  3. IMPROVEMENT only for a new analyte;
  4. combined rows judged on their accessible component;
  5. dating to the first primary research report.

  66 decisions changed (`eligibility_v2_changes.tsv`).
- **Version 3** removed rule 2's count.
  - **Why:** the count searched the entry's own name, so entries named after
    later or qualified terms failed regardless of their literature.
  - **Effect:** 44 decisions moved back (`eligibility_v3_changes.tsv`).
    DISEASE_DEFINED_BY_TEST is a judgment again.
  - **Replacement:** a computed literature check applied after dating (see
    *Dating*).

Final eligibility: **71 INCLUDE rows covering 48 entries**.

### Screeners

**Screener B** decided 453 rows blind (`screenerB_input.tsv`):
- **Input:** every row of the 52 diseases screener A had included (153 rows),
  plus 300 rows from 129 whole diseases drawn at random.
- **Agreement:** against A's version 1 decisions, **422/453 (93.2%), Cohen's
  kappa 0.726** (`compare_screeners.py`, which reproduces the comparison from
  commit `528cef7e51a`).
- **Disagreements:** of the 31, 15 were wording ambiguity, 15 were facts, and
  1 was A departing from its own written rule.

**Screener C** decided the 15 facts disagreements, and the 2-of-3 majority is
final. Recomputed under version 3, A was outvoted on 13 of them
(`eligibility_resolution.tsv`; `eligibility_work/ov9_resolution.txt`).

**Screener B2** re-screened rule 1 blind on 32 rows (`screenerB2_input.tsv`):
- **Input:** the 16 rows that were INCLUDE because of rule 1, plus 16 drawn
  from the 18 subset-type EXCLUDE rows.
- **Agreement:** **27/32 (84.4%), kappa 0.688**.
- **Tiebreak:** screener C2 decided the 5 disagreements in a fresh session,
  from `prompts/screenerC2.md`. B2 and C2 agreed every time, and A was
  outvoted on all 5 (`eligibility_rule1_rescreen.tsv`).

### Cases

`build_cases.py` collapses the 71 INCLUDE rows into **57 cases** (`cases.tsv`):
one per disease–test pair, 48 entries, 42 `test_group`s.
- **One case per entry:** a test recorded twice in one entry (a diagnosis and
  a biochemical row, or serum and CSF) is one case.
- **Linked by test_group:** the same test under several entries is one case
  per entry, sharing a `test_group`. For example, AQP4-IgG appears under
  NMOSD, optic neuritis and transverse myelitis.

Of the 22 known positives, 13 are cases (`known_positives_cases.tsv`). Six are
excluded by an eligibility rule and 3 are KB gaps.

## Dating, as done

- **Two agents.** Two dating agents each named a first primary report for every
  case, with a verbatim abstract quote (`dating.agentA.tsv`,
  `dating.agentB.tsv`).
- **Checks.** `check_dating.py` checked both against PubMed E-utilities
  (`dating_checks/`). For each case it:
  - confirms the quote appears in the abstract;
  - sets the publication date to the earlier of the issue and e-publication
    dates;
  - lists the five earliest PubMed records for the analyte and disease before
    that date.

  Every quote from both agents passed.
- **Cutoff rule.** A PMID is accepted only when both agents give the same PMID
  and both quotes pass. The cutoff is 31 December of the year before the
  discovery date.
  - A and B gave **41 ACCEPTED**, **6 ACCEPTED_FLAGGED** (an earlier paper
    looks like the real discovery report) and **10 NOT_ACCEPTED** (the
    agents disagree).
  - The 16 flagged and not-accepted cases are listed with written assessments
    in `dating_flags.tsv`.
- **Agent C majority.** A third agent dated the 10 NOT_ACCEPTED cases blind.
  Its input (`dating_agentC_input.tsv`) held only case_id, disease, test and
  subset, with no PMIDs, quotes or assessments. Its output is
  `dating.agentC.tsv`, checked into `dating_checks/agentC.checked.tsv`.
  - **Rule:** a PMID is MAJORITY_VERIFIED when at least two of A, B and C name
    it and all their quotes pass. Its cutoff comes from the
    `check_dating.py` record of that PMID.
  - **Result:** 6 cases became MAJORITY_VERIFIED: C001, C039, C042, C052, C054
    and C056. The other 4 remain NOT_ACCEPTED: C010, C018, C040 and C055.
- **Human review.** `make_review_sheet.py` writes `dating_review_sheet.md` and
  `dating_human_review.tsv` for the 10 cases still unresolved. They are the 4
  NOT_ACCEPTED and the 6 ACCEPTED_FLAGGED cases. For each case the sheet
  lists every candidate PMID with its PubMed title, date and implied cutoff,
  and each agent's quote. The written assessment comes last.
- **Current dating status (57 cases):** 41 ACCEPTED (7 of them dropped by
  the literature check, below), 6 MAJORITY_VERIFIED, and 10 pending human
  review.
- **Mechanistic readiness.** `build_dating.py` writes `dating.tsv` and records
  a mechanistic-readiness judgment for every ACCEPTED, ACCEPTED_FLAGGED and
  MAJORITY_VERIFIED case. The judgment is "yes" with one PubMed paper dated on
  or before the cutoff that links the test's molecule to the disease
  mechanism, or "no" when the searches found none. The script checks each
  cited paper's date against the cutoff.
- **Literature sufficiency.** `check_pretest_era.py` counts PubMed records with
  an abstract published on or before each verified (ACCEPTED or
  MAJORITY_VERIFIED) cutoff. The query ORs
  together:
  - the disease's MeSH heading;
  - its MONDO label and exact synonyms, read with `runoak` from the local
    MONDO build;
  - its `literature_alias`, where one is set.

  A count below `RUN_CONFIG.yaml`'s `packet_minimum` (30) is
  INSUFFICIENT_PRE_CUTOFF_LITERATURE (`literature_check.tsv`).
- **Aliases.** MONDO labels for subtype entries are often catalogue forms no
  abstract uses, such as "diabetes insipidus, nephrogenic, X-linked". So the
  first run failed 17 cases.
  - `literature_recount.py` recounted those 17 under plain literature names
    (`literature_recount.tsv`), and each name became the case's
    `literature_alias` (column in `dating.tsv` and `literature_check.tsv`,
    with its source in `alias_source`).
  - For 4 cases the alias is a compound PubMed fragment rather than a phrase:
    anti-NMDAR, Immunodeficiency 18 and 19, MOGAD.
  - On the rerun, 10 of the 17 passed. The rerun reproduces
    `literature_check.tsv` byte for byte.
  - **C001 and C052.** Two MAJORITY_VERIFIED cases then failed on naming
    alone:
    - C001, acquired TTP: 0 records, because the query held only the
      "acquired" subtype names. Alias "thrombotic thrombocytopenic purpura".
    - C052, statin toxicity: 13 records. Aliases "statin myopathy" and
      "statin-associated myopathy".

    The experimenter specified both aliases after the check failed, and
    `literature_recount.py` did not test them. Each one's `alias_source`
    says so. With them, C001 counts 690 records and C052 counts 57, and both
    pass.

### Case counts

| test_class | Cases | Verified (PASS) | Dropped (insufficient) | Pending (unverified cutoff) |
|---|---|---|---|---|
| AUTOANTIBODY | 24 | 19 | 1 | 4 |
| METABOLITE | 12 | 5 | 1 | 6 |
| SECRETED_PROTEIN | 7 | 7 | 0 | 0 |
| OTHER | 7 | 4 | 3 | 0 |
| ENZYME_ACTIVITY | 5 | 3 | 2 | 0 |
| CELL_SURFACE_MARKER | 1 | 1 | 0 | 0 |
| SOMATIC_VARIANT | 1 | 1 | 0 | 0 |
| **Total** | **57** | **40** | **7** | **10** |

- **Dropped (7):** anti-NMDAR encephalitis, congenital TTP, Immunodeficiency 18,
  Immunodeficiency 19, MNGIE ×2 and Revesz syndrome. They stay listed in
  `literature_check.tsv`.
- **`dating.tsv`** holds the other 50, in 39 test groups.
- **Verified (40):** 34 ACCEPTED and 6 MAJORITY_VERIFIED, in 33 test groups.
  35 are FIRST and 5 IMPROVEMENT; 34 have mechanistic readiness "yes" and 6
  "no".
- **Pending (10):** listed in `pending_cases.txt`. They are the 6
  ACCEPTED_FLAGGED and 4 NOT_ACCEPTED cases awaiting human review, so their
  cutoff has not been literature-checked.

## Controls

- **Negatives** (`negatives.tsv`): six diseases with no accepted
  accessible-specimen confirmatory test. Each row gives the disease, its
  `kb/disorders/` file and MONDO term. The six:
  - hypermobile EDS;
  - Kawasaki disease;
  - sarcoidosis;
  - Behçet's disease;
  - CRPS type 1;
  - Takayasu arteritis.
- **Decoys** (`decoys.tsv`): 11 disease–biomarker pairs, from 9 PubMed records,
  where a proposed diagnostic biomarker failed replication.
  - **Query:** one fixed query, recorded verbatim with its run date and 48
    hits in `decoy_query.txt` and run by `find_decoys.py`. Its phrases use
    PubMed's proximity form, because the quoted `[tiab]` form returns 0
    records through E-utilities.
  - **Screen:** every hit has a decision and reason in `decoy_screen.tsv`.
  - **Kept:** only accessible-specimen diagnostic biomarkers whose failure the
    abstract states. Each kept row's failure quote matches its abstract
    (`quote_ok`).
  - **Disease match:** 7 rows matched their kb file through MeSH and 4 by
    judgment (`disease_match`). Every disease exists in `kb/disorders/`.

  Caveats:
  - **Partial failures.** Some decoys did not fail outright: the bladder
    methylation assay kept AUC 0.73 and the prostate panel AUC 0.76.
  - **Subtype comparisons.** The heart-failure row is about separating HF-REF
    from HF-PEF, and the frontotemporal dementia row about separating bvFTD
    from psychiatric disorders, not disease from controls.
  - **No named analyte.** The endometriosis row names no single miRNA.
  - **Small set.** One query yields a small set, chosen for being fixed
    rather than complete.

## Dev/test split

**The dev set is frozen.** It was drawn once, in commit `e76ffea9ec2`, from
the 34 cases verified at the time, with seed 20261111. `make_split.py` now
reads `dev_set.txt` and never redraws it. The script fails if a dev case is no
longer verified, or if a dev case's test_group has gained other cases. Rerun
after agent C, `dev_set.txt` is byte-identical to the committed version.

**Dev set** (`dev_set.txt`): one case per test_class, drawn as follows:
- **Candidates:** only cases that are alone in their test_group across all
  dated cases. No dev case then shares a test with a test or pending case.
- **Eligible classes:** a class contributes only if it keeps at least one
  verified case for the test set. That left out SOMATIC_VARIANT (one
  verified case) and CELL_SURFACE_MARKER (none at the time; PNH, C042, has
  since been verified and is in the test set).
- **Draw:** one candidate per class.

| Case | test_class | Test | Disease |
|---|---|---|---|
| C003 | SECRETED_PROTEIN | CSF amyloid-beta 42 | Alzheimer Disease |
| C025 | AUTOANTIBODY | anti-GABAB receptor antibodies | Limbic Encephalitis |
| C038 | ENZYME_ACTIVITY | TPP1 enzyme activity | Neuronal Ceroid Lipofuscinosis 2 |
| C044 | METABOLITE | serum 7-alpha-hydroxy-4-cholesten-3-one | Primary Bile Acid Malabsorption |
| C050 | OTHER | TREC newborn screening | Severe Combined Immunodeficiency |

**Test set** (`test_set.txt`): every other verified case, **35** in 28 test
groups.

| test_class | Test cases |
|---|---|
| AUTOANTIBODY | 18 |
| SECRETED_PROTEIN | 6 |
| METABOLITE | 4 |
| OTHER | 3 |
| ENZYME_ACTIVITY | 2 |
| CELL_SURFACE_MARKER | 1 |
| SOMATIC_VARIANT | 1 |

**Pending** (`pending_cases.txt`): the **10** cases awaiting human review. Each
joins the test set once its cutoff is verified and passes the literature
check.

## Coverage audit

`coverage_audit/audit.py` writes `coverage.tsv` and asks one question of each
disease: does its pathograph (kb at the pinned commit) hold a node that is
both of these?
- measurable in an accessible specimen;
- absent from every differential diagnosis's pathograph.

It ran on the 6 negatives and the 2,548 frame entries that have no flagged
row. The definitions are in `coverage_audit/FINDINGS.md`.

| Status | Negatives | Frame entries |
|---|---|---|
| No measurable node | 3 | 2,316 |
| Measurable nodes, no differentials listed | 3 | 154 |
| Differentials listed, none a kb entry | 0 | 27 |
| Every measurable node shared with a differential | 0 | 9 |
| At least one unshared measurable node | 0 | 42 (2 spurious) |

- **The negatives.** Five of the six list no differential diagnoses. CRPS-1's
  one differential has no kb entry. Their measurable nodes are blood counts
  and ESR.
- **The 42.** Mostly creatine kinase, IgE, lymphocyte counts and
  immunoglobulins. They are unshared because the differential's entry does
  not record them, not because they discriminate.

**What this implies for A1.** Its differential-specificity score cannot be
computed for any negative, because none has a differential that resolves.
Only its all-pathograph specificity applies to them. For positives the score
depends on how completely differentials are recorded, which is sparse: 1,035
of the 2,548 entries list any.

**What this implies for H3.** A negative can receive low confidence because its
graph has nothing measurable to propose, which is not the same as the arm
recognising there is no test. So the primary H3 analysis is restricted to
cases and negatives whose graph has at least one measurable node. Only the
three negatives with measurable nodes qualify: Kawasaki disease, sarcoidosis
and Takayasu arteritis. Unrestricted and stratified results are reported
alongside (see *Endpoints*).

The audit has not been run on the positive cases or on time-sliced entries.

## Curation protocol

Planned. None of this has been run, and no packet, banned-term list or
time-sliced entry is committed.

- **Packets.** For each case, `build_packet.py` builds a PubMed literature packet
  from a query and `--maxdate` (the cutoff). It keeps records with an abstract
  and a publication date (earliest of issue and e-publication) on or before the
  cutoff. The packet is the only literature the time-sliced curation may cite.
- **Gate.** `check_cutoff.py` fails a time-sliced entry that does any of these:
  - cites a PMID outside its packet;
  - cites a non-PMID reference;
  - contains a banned post-cutoff term;
  - keeps present-day `has_subtypes`;
  - has a pathophysiology node with no evidence.
- **Replicates.** Two independent curation replicates per case. Each runs in
  an isolated git worktree with the packet pre-loaded, and web tools and
  ad-hoc fetching denied (see *Enforcement*).
- **Answer-bearing files excluded** from each worktree:
  - every repository file outside `experiments/` that matches the case's
    banned terms;
  - all of `references_cache/` except the packet's PMIDs, which are
    pre-fetched before the session;
  - everything in `experiments/diagnostic_retrodiction/` except the case's
    run folder, `check_cutoff.py` and the packet.
- **Enforcement.** Excluded files are absent, by sparse checkout, and the
  session runs with these deny rules (kept in the local, git-excluded
  `.claude/curation-deny.json`):

  ```
  WebSearch, WebFetch, Bash(curl:*), Bash(wget:*), Bash(python -c:*),
  Bash(uv run python -c:*), Bash(just fetch-reference:*),
  Bash(just research-disorder:*), mcp__codex__codex, mcp__codex__codex-reply
  ```

  Prefix deny rules can be sidestepped (for example `python3 -c`), which is
  why the transcript audit below decides whether a replicate counts.
- **Transcript audit.** `audit_transcript.py` scans each session's JSONL
  transcript. It records an event for each of:
  - any web-tool call;
  - any command containing `http://`, `https://`, `curl`, `wget`, `urllib`,
    `requests` or `eutils`;
  - any read of an excluded path;
  - any PMID outside the packet.

  A replicate passes only with zero events. A failed replicate is discarded,
  rerun once, and logged in `DEVIATIONS.md`.

## Leakage measures

In place now:
- `build_packet.py` dates each record by the earlier of its issue and
  e-publication dates.
- `check_cutoff.py` enforces packet-only citation and the banned-term list.
- Screener inputs carried frame columns only (`select_screenerB.py`,
  `select_screenerB2.py`).
- No dev case shares a test_group with a test or pending case.

Planned: the isolated worktrees and transcript audit above.

Known and not yet closed:
- **Bookshelf dates.** PubMed dates Bookshelf chapters (GeneReviews) 1993, the
  start of the series, so they can pass a date filter they should fail. They
  appeared as false earlier hits in `check_dating.py` output.
- **Banned terms.** The lists are not written yet. Each will be generated per
  case, then checked by a human, from:
  - the rubric's T4 analyte: its term label and synonyms via OAK;
  - the analyte's gene symbol;
  - the names of subtypes defined by the analyte.

  `check_cutoff.py --banned` reads the list, one term per line.
- **Training data.** The LLM arms' training data post-dates every cutoff (see
  *Limitations*).

## Scoring and adjudication

Each case gets a rubric in `rubrics/`. None is written yet. The tiers are
judged against it:

| Tier | A candidate reaches it when |
|---|---|
| T1 | its mechanism class matches the rubric's, by ontology subsumption |
| T2 | its `analyte_type` equals the rubric's, its specimen is in the rubric's allowed set, and its target term is subsumed by the rubric's target class. This is the primary endpoint's threshold. |
| T3 | the discovery experiment it proposes matches the rubric's description (adjudicated) |
| T4 | it names the exact analyte, by ID or synonym. T4 on a case the rubric marks unreachable is a leakage alarm. |

**Adjudication.**
- **Automatic first.** Every candidate is first matched against the rubric by
  ontology.
- **LLM adjudicator.** Candidates that matching cannot resolve go to an LLM
  adjudicator blind to arm identity, in a fresh session.
- **Human check.** Two human adjudicators, blind to arm, score a seeded 20%
  sample of candidates, or all of them if there are fewer than 50. A third
  resolves their disagreements.
- **Agreement.** Human–human and human–model kappa are reported.

## Analysis plan

- **Unit.** The case. The primary analysis uses the test set; the dev set is
  for developing prompts and arms and is not scored for the endpoints.
- **Clustering.** Cases sharing a `test_group` are not independent: an arm
  that finds AQP4-IgG once will tend to find it for every entry carrying it.
  The primary McNemar test treats cases as independent. Two checks follow:
  - a sensitivity analysis keeping one case per test_group: the case with the
    earliest cutoff, ties broken by case_id;
  - a cluster bootstrap over test groups.
- **Sample size.** The test set holds 35 cases in 28 test groups now, and at
  most 45 if all 10 pending cases are verified and pass the literature
  check. Exact two-sided McNemar at
  α = 0.05 reaches significance only with enough discordant pairs:

  | Discordant pairs | Split needed |
  |---|---|
  | 5 or fewer | never significant |
  | 6 | 6:0 |
  | 10 | at least 9:1 |
  | 20 | at least 15:5 |

  The study can detect a large difference between A2 and A3. It is not powered
  for a moderate one, and a null result will not show the arms are equivalent.

## Pending before prereg-v1

- [ ] Verify the 10 unverified cutoffs: human review in
  `dating_human_review.tsv`, then rerun the literature check and
  `make_split.py`.
- [ ] Propagate the literature exclusion into `eligibility.tsv` and
  `cases.tsv`, which still count the 7 dropped cases as INCLUDE.
- [ ] Write the per-case rubrics and, from them, the banned-term lists.
- [ ] Write `audit_transcript.py`, A1's node-type → `analyte_type` table and
  A1's weights, and freeze them before the dev set is run.
- [ ] Finalise `RUN_CONFIG.yaml`: the second model family is TBD.
- [ ] Decide whether to expand the negatives, and how to handle Alzheimer
  disease as both a decoy and a dev case.
- [ ] Decide how an LLM arm's 3 runs become one hit or miss per case for
  McNemar.
- [ ] Decide which of the 2 curation replicates feeds the arms, or how both
  do.
- [ ] Decide what the negatives are curated and prompted as of. They have no
  test, so no cutoff date or cutoff year.
- [ ] Register on OSF.

## Limitations

- **Single-model eligibility judgments.** Screener A, one model, decided all
  3,311 rows. Of those reasons, 1,619 are individually judged, 675 come from
  pattern rules and 1,017 are a scanned default. Screeners B, C, B2 and C2 are
  further runs of models, not human review, and re-screened 453, 15, 32 and
  5 rows.
- **The implicit-specimen inference is not fully audited.** One in five of the
  284 implicit-specimen rows was wrong. Stated-specimen rows were not
  systematically checked. The frame labels CRPS type 1's three-phase bone
  scintigraphy as a blood test, which the coverage audit surfaced.
- **Screener B could see a row-count signal.** Its input mixed every row of the
  52 included diseases (median 3 rows per disease) with 129 random whole
  diseases (median 2). A disease with more rows was more likely to be from the
  included block.
- **Abstracts-only counts undercount early literature.** `hasabstract` drops
  most PubMed records before about 1975, so the literature check and packets
  under-represent the oldest literature. The 17 aliases are hand-written.
- **Dating uncertainty.** The discovery date is unverified for 10 cases. Even
  where both agents agree, 6 accepted PMIDs look later than the real report.
  Six cutoffs rest on a 2-of-3 agent majority rather than agreement of the
  first two.
- **KB gaps.** The frame holds only tests dismech records: 3 of 22 known
  positives are missing.
- **Sparse differentials.** Most entries list no differential diagnoses, and
  five of the six negatives list none. This limits A1 and H3 (see *Coverage
  audit*).
- **LLM training-data leakage.** The models behind the LLM arms were trained
  on literature that post-dates every cutoff. Packets and worktree isolation
  limit what an arm can read, not what it already knows. A2 and A3 share this
  exposure, so the paired comparison is less affected than absolute hit rates.
- **Mechanistic-readiness and flag assessments are one agent's judgment** from
  titles and abstracts.

## Files

| File | What it is |
|---|---|
| `README.md` | this document |
| `PINNED_COMMIT` | the `kb/` commit the frame was built from |
| `RUN_CONFIG.yaml` | run parameters: packet minimum, models, temperature, runs per arm, k, MONDO build |
| `census.py` | builds `frame.tsv` from `kb/disorders/` |
| `frame.tsv` | the frozen sampling frame, one row per diagnosis/biochemical item |
| `known_positives.tsv` | 22 disease/test pairs the frame should contain |
| `check_recall.py` | measures frame recall against the known positives |
| `recall_report.tsv` | frozen per-pair recall result |
| `eligibility_rules.md` | eligibility rules, version 3 |
| `eligibility_rules.v1.md` | eligibility rules, version 1 |
| `eligibility_rules.v2.md` | eligibility rules, version 2 |
| `eligibility.tsv` | decision and reason for every flagged row, plus 3 KB gaps |
| `eligibility_review.tsv` | seeded INCLUDE sample plus ambiguous EXCLUDE rows, for review |
| `eligibility_v2_changes.tsv` | decisions changed by version 2 |
| `eligibility_v3_changes.tsv` | decisions changed by version 3 |
| `eligibility_work/build_eligibility.py` | rebuilds `eligibility.tsv` and `eligibility_review.tsv` |
| `eligibility_work/ov1.txt` … `ov7.txt` | version 1 judgment tables, in blocks |
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
| `compare_screeners.py` | A vs B comparison, reproduced from `528cef7e51a` |
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
| `dating_agentC_input.tsv` | agent C's blind input for the 10 NOT_ACCEPTED cases |
| `dating.agentC.tsv` | agent C's discovery PMIDs and quotes |
| `dating_checks/agentC.checked.tsv` | `check_dating.py` output for agent C |
| `build_dating.py` | merges the agents into `dating.tsv`; writes flags and spot-check |
| `dating.tsv` | the 50 dated cases not dropped by the literature check |
| `dating_flags.tsv` | the 16 cases A and B did not settle cleanly, with assessments and agent C's PMID |
| `make_review_sheet.py` | writes the human review sheet and its TSV |
| `dating_review_sheet.md` | the 10 unresolved cases, candidates first |
| `dating_human_review.tsv` | one row per unresolved case, for the reviewer's decision |
| `dating_spotcheck.tsv` | 8 unflagged accepted cases for spot-checking |
| `check_pretest_era.py` | counts pre-cutoff literature per case |
| `literature_check.tsv` | the literature check for all 57 cases, with aliases |
| `literature_recount.py` | recount under plain disease names |
| `literature_recount.tsv` | that recount, for the 17 cases that first failed |
| `negatives.tsv` | 6 negative-control diseases and their kb files |
| `find_decoys.py` | runs the fixed decoy query and maps hits to kb files |
| `decoy_query.txt` | the decoy query, run date and hit count |
| `decoy_candidates.tsv` | all 48 hits with MeSH, MONDO and kb matches |
| `decoy_screen.tsv` | decision and reason for each hit |
| `decoys.tsv` | the 11 decoy disease–biomarker pairs |
| `make_split.py` | checks the frozen dev set; writes the test and pending lists |
| `dev_set.txt` | 5 dev cases (frozen) |
| `test_set.txt` | 35 test cases |
| `pending_cases.txt` | 10 cases awaiting cutoff verification |
| `coverage_audit/audit.py` | the pathograph coverage audit |
| `coverage_audit/FINDINGS.md` | its definitions, results and review |
| `coverage.tsv` | one row per audited disease |
| `build_packet.py` | builds a date-limited PubMed packet |
| `check_cutoff.py` | gates a time-sliced entry against its packet |
| `prompts/`, `rubrics/`, `schemas/` | `prompts/` holds only `screenerC2.md`; the others are empty |
