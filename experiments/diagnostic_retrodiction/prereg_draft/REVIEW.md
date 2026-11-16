# Judgment calls for review before prereg-v1

One line each, in this order: A1 weights, design defaults, negatives, dating and readiness,
rubrics. Every item is open until confirmed. "Default" items are in effect and logged in
`DEVIATIONS.md`.

## A1 weights (`a1_config.yaml`)

- w_differential_specificity 0.5: equal weight with all-pathograph specificity, since there is no prior reason to favour either.
- w_all_specificity 0.5: guards against sparse differential lists.
- no_differential_all_weight 1.0: with no resolved differential, all-pathograph specificity carries the whole score.
- neighbourhood_radius 1: a term's direct parent or child counts as the same node.
- distance_decay_exponent 1: score × 1/(1+d), with no free shape parameter.
- unreachable_distance = longest path + 1: a node off every causal path ranks below every reachable one.
- confidence = score, with no recalibration.
- k = 10, the same cut as the LLM arms.
- tie_break: node name, ascending.
- node-type → analyte_type table: first matching rule wins; germline genetic nodes are never candidates.
- default_specimen per analyte_type, used when a node states no specimen.
- A1 ranking code: only the candidate rule is wired in `run_all.py`; the scoring itself is not implemented yet.

## Design defaults

- C036 excluded as NOT_NEW_ANALYTE: copeptin was in use for central DI by 2011.
- C047: phytanic acid is T1 only.
- C056 re-dated to PMID:15589308, cutoff 2003-12-31; readiness becomes "no".
- C022 display name: "adult-onset acid maltase deficiency".
- C009: the cutoff stays 1997-12-31.
- H3 AUROC is reported pooled and by packet-size tertile.
- "NMO" alone is no alarm for C037, C040 and C056.
- Temperature 0 cannot be set on claude-opus-5-5, so effort is fixed at high instead.
- Knowledge probe: once per display name, no cutoff, not scored; it is used to read T4 hits and alarms.
- Arm literature = the packet abstracts the replicate's entry cites (whole packets reach about 128k abstracts).
- A2 and A3 differ only in the material block: A2 gets entry + cited abstracts, A3 the cited abstracts only.
- A7 gets no literature, only the stripped pinned entry.
- A6 and A7 run per case, because they depend on the case's rubric; A1, A2, A3 and A5 run per unit.
- Negatives run with the test split only; dev has none.
- LLM arms run 6 times per case (3 runs × 2 replicate labels) even when the input does not depend on the replicate (A3, A4, A7).
- Tier ladder: T4 requires T2, and T3 requires T2; T1 is judged independently, by adjudication.
- A candidate flagged CLINICAL_T1_ONLY by the adjudicator is capped at T1.
- The adjudicator sees one arm output at a time and never the arm name.
- The human sample is 20% of positive-case candidates (seed 20261114), blinded by hashed item id.
- Packets are never refetched once built; a packet built for dev is reused if a unit recurs.
- The curation worktree excludes experiments/, references_cache/, research/, pages/, history/, the entry's own file, and every file naming a case's absent leakage term.

## Negatives

- Cutoff assignment: an unmatched seeded draw, pending a matching criterion.
- Screen judgments (`SCREEN_JUDGMENT`): aortitis (ESR in large-vessel vasculitis criteria).
- Screen judgments: Kearns-Sayre syndrome (CSF protein in its criteria).
- Screen judgments: melanotic neuroectodermal tumour of infancy (urinary VMA).
- Screen judgments: Wiskott-Aldrich syndrome (small platelets).
- Screen judgments: cocaine intoxication (urine toxicology).
- Screen judgments: Shiga-toxin HUS (blood smear, stool toxin).
- Screen judgments: primary hyperoxaluria type 1 (urinary oxalate).
- Screen judgments: *S. aureus* pneumonia (cultures).
- Screen judgments: chorea-acanthocytosis (acanthocytes).
- The screen applies to drawn negatives only; the original six are not screened (Kawasaki disease's entry lists blood tests).
- Usable: DIRA (nonspecific leukocytosis).
- Usable: lipoprotein glomerulopathy (supportive serum apoE).
- Usable: myofibrillar myopathy (CK); it later failed the literature check.
- Not usable: congenital hydrocephalus (now N17); its nodes are CSF processes, not assays.
- Not usable: soil-transmitted helminthiases (stool microscopy).
- Not usable: hereditary angioedema (C1-inhibitor).
- Not usable: choroid plexus neoplasm and the MKB-type syndrome.
- N10's display name ("autoinflammatory disease of infancy with pustulosis and osteomyelitis") is checked by component phrases, not as a whole.

## Dating and readiness

- C010 readiness yes, PMID:12752470 (absences in GLUT1 deficiency, 2003).
- C018 readiness yes, PMID:2709525 (PF4 release in HIT, 1989); the weakest yes, since PF4 is a marker there, not the target.
- C040 readiness no: before 2004 AQP4 appears only as a water channel.
- C055 readiness yes, PMID:10839351 (gephyrin autoantibodies in SMS, 2000).
- C054 readiness no: before 1993, amphiphysin appears only as a synaptic protein.

## Rubrics

- C001: T2 also accepts an anti-ADAMTS13 IgG or inhibitor (AUTOANTIBODY, serum or plasma).
- C002: plasma p-tau181 or total tau meets T2; CSF tau does not.
- C006: lavage fluid is excluded from T2; only serum and plasma are allowed.
- C008: "NAA" is not a leakage term (too generic).
- C009: endomysial antibody reaches T1 only, because it names a tissue, not tTG.
- C010, C041: CSF glucose and GLUT1 terms are pre-cutoff vocabulary, so the alarm has little to check.
- C010, C041: the subset text is kept out of prompts.
- C010, C041: CSF glucose was in clinical use for GLUT1 deficiency before 2007; not moved to T1 (re-scan list).
- C011, C012: T2 is the paranodal complex (NFASC, CNTN1, CNTNAP1).
- C015, C016, C021: T2 accepts any telomere-length method; T4 requires flow-FISH.
- C015, C016: every leakage term is in the packet, so the alarm cannot fire.
- C018: the functional HIT assays reach T1/T3 only.
- C023, C024: the VGKC-complex antibody is kept out of T2.
- C028, C039: anti-MOG ELISA counts at T2; T4 requires the native-MOG cell-based assay.
- C028: the display name is a pre-cutoff paediatric-demyelination name.
- C030: copper and ceruloplasmin reach T1 only; DOPA, DOPAC and noradrenaline are not leakage terms.
- C033: T2 includes LRP4.
- C037, C040, C056: T2 accepts an end-foot antigen named descriptively.
- C037: the display name is "neuromyelitis optica".
- C038: T2's specimens come from the case row, because the discovery paper used fibroblasts.
- C038: CLN2 is not a leakage term.
- C042: erythrocyte DAF meets T2 and is reachable pre-cutoff; T4 requires leukocytes or platelets.
- C043: only variant-specific names are leakage terms.
- C044: "C4" is not a leakage term.
- C047: phytanic acid is T1 only (default).
- C052: only antibody phrases are leakage terms; the enzyme's names are not.
- C053: "GAD" alone is not a leakage term.
- C055: gephyrin is kept out of T2.
- C036 (copeptin in use) is now excluded; C057 keeps copeptin at T2 with AVP at T1.
- Re-scan list, not changed: C056's NMO-IgG was clinically available in 2004–05. Since the re-date to 2003 the point is moot.
- Re-scan list, not changed: C047's phytanic acid; applied as a default.
- Re-scan list, not changed: C015, C016 and C021 telomere length (borderline).
