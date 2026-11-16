# Deviations log

Every change to the protocol since the first README draft (commit `e76ffea9ec2`,
"alias fix, stratified split, draft README"). Status is one of:
- **decided:** by the experimenter;
- **default, pending Chris:** applied as a default, awaiting confirmation;
- **forced:** by a tool or model constraint.

Run-time deviations, such as a failed curation replicate or an invalid arm
output, are logged per run in `runs/<split>/deviations.log` and copied here
when a run is reported.

## Design

| # | Date | Change | Status |
|---|---|---|---|
| 1 | 2026-11-12 | Placeholders filled: H2/H3 endpoints, cut-offs, A1–A7 definitions, H3 coverage restriction, worktree exclusions, deny rules, transcript audit, tiers, adjudication, representative case. | decided |
| 2 | 2026-11-16 | Single model family. A2′ and A3′ and their robustness check were removed; leakage is checked within the family by A4 and the T4 alarm. | decided |
| 3 | 2026-11-16 | Run aggregation. A case is a hit when T2 is reached in ≥4 of 6 runs (3 runs × 2 replicates); A1 must hit in both replicates. Any-hit and the mean are also reported. | decided |
| 4 | 2026-11-16 | Both curation replicates feed every arm, and replicate agreement is reported. | decided |
| 5 | 2026-11-16 | Each negative takes the cutoff of a seeded (20261114) test case. No matching criterion is defined yet, so the assignment is an unmatched seeded draw. It was frozen in `draw_negatives.py` (SLOT_CASE) on 2026-11-16 so that test-set changes do not reshuffle it. | decided (draw); matching criterion pending |
| 6 | 2026-11-16 | Negatives expanded by a seeded draw from `coverage.tsv`. H3 becomes exploratory if fewer than 10 negatives are usable. | decided |
| 7 | 2026-11-16 | Decoy D009 (Alzheimer disease) dropped because it overlaps dev case C003. | decided |
| 8 | 2026-11-16 | C048 and C049 stay dropped; no literature aliases are added. | decided |
| 9 | 2026-11-16 | Power note: 42 (now 41) test cases in 33 clusters. Effect sizes are reported with CIs for every comparison. | decided |
| 10 | 2026-11-16 | Banned terms renamed leakage_terms and never stripped from packets. A leakage term absent from the packet that appears in a curated entry or an arm output is an alarm. | decided |
| 11 | 2026-11-16 | Every case and negative gets an arm_display_name: a pre-cutoff name with no test or analyte in it. Subset text never reaches an arm. | decided |
| 12 | 2026-11-16 | T2 rule: an analyte in clinical diagnostic use for the disease at the cutoff reaches T1 only. Applied to C022, C036, C045 and C057. C027 (VEGF-C) and C051 (cholesterol) were removed from T2. C001's anti-ADAMTS13 IgG or inhibitor was added to T2. | decided |
| 13 | 2026-11-16 | T2's target class is an anchor plus an explicit member list, not ontology subsumption. Gene-to-GO subsumption cannot be computed offline. | decided (drafting) |
| 14 | 2026-11-16 | Negatives N12 and N13 replaced by the next seeded draws. Each negative gets a literature check at its cutoff, and drawn negatives below packet_minimum are redrawn. | decided |
| 15 | 2026-11-16 | C036 excluded as NOT_NEW_ANALYTE: copeptin was in use for central DI by 2011 (PMID:21367924). The exclusion is propagated through post_dating_exclusions, eligibility.tsv and cases.tsv; case_ids are kept. | default, pending Chris |
| 16 | 2026-11-16 | C047: phytanic acid moved from T2 to T1. | default, pending Chris |
| 17 | 2026-11-16 | C056 re-dated to PMID:15589308, cutoff 2003-12-31, HUMAN_VERIFIED, aligned with C040. Readiness becomes "no", because PMID:16087714 postdates the new cutoff. The literature check passes (453 records). Negative N11, which takes C056's cutoff, moves to 2003-12-31 and still passes (31 records). | default, pending Chris |
| 18 | 2026-11-16 | C022 arm_display_name changed to "adult-onset acid maltase deficiency" (185 pre-cutoff hits, no collision). | default, pending Chris |
| 19 | 2026-11-16 | Negatives N10, N13 and N17 replaced. A screen in `draw_negatives.py` now rejects draws whose standard criteria include an accessible-specimen test, with reasons in `negatives_replaced.tsv`. It runs as a second phase, so the first phase reproduces the earlier slots exactly. | default, pending Chris |
| 20 | 2026-11-16 | H3 AUROC is reported pooled and by packet-size tertile. | default, pending Chris |
| 21 | 2026-11-16 | "NMO" alone is no leakage alarm for C037, C040 or C056. Terms match whole and exact, so only "NMO-IgG" and the like match. | default, pending Chris |
| 22 | 2026-11-16 | C009's cutoff stays 1997-12-31. | default, pending Chris |
| 23 | 2026-11-16 | Knowledge probe added. It is not an arm: once per display name, with no cutoff and no material, it records what the model knows today, against which T4 hits and leakage alarms are read. | default, pending Chris |
| 24 | 2026-11-16 | Arm literature: A2, A3, A5, A6 and A7 receive the packet abstracts the replicate's curated entry cites, not the whole packet. Whole packets reach about 128,000 abstracts (Alzheimer disease, 2019). | default, pending Chris |
| 25 | 2026-11-16 | Negatives run with the test split only. Dev has no negatives. | default, pending Chris |
| 26 | 2026-11-16 | A6 and A7 run per case, not per unit, because the A6 ablation target and the A7 stripping depend on the case's rubric. A1, A2, A3 and A5 run per unit. | default, pending Chris |

## Forced by tools or models

| # | Date | Change | Status |
|---|---|---|---|
| F1 | 2026-11-16 | Temperature 0 cannot be set. claude-opus-5-5 rejects every sampling parameter (400) on the API, and `claude -p` exposes none. The protocol's temperature 0 is therefore not applied on any path; effort is fixed at high instead (RUN_CONFIG.yaml). | forced |
| F2 | 2026-11-16 | Structured output instead of forced tool use: forced tool_choice returns a 400 on claude-opus-5-5. | forced |
| F3 | 2026-11-16 | No server-side refusal fallback on batch runs (the Batches API rejects `fallbacks`). A refused request is recorded as invalid and retried once. | forced |
| F4 | 2026-11-16 | `build_packet.py` sends E-utilities parameters by POST. The API key had been in the GET URL, against the project's key-handling rule. `--email` is now optional, and no personal address is sent by default. | forced (security) |
| F5 | 2026-11-16 | PubMed counts for multi-word terms use the proximity form [tiab:~0]. A quoted phrase in [tiab] returns 0 for phrases outside PubMed's phrase index. | forced |
