# SCDS OpenScientist Enrichment

Enrich `kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml` using the
OpenScientist artifact bundle (extracted at `/tmp/scds_artifacts/`, source zip
`3ff84dbd-ab0a-44e5-8141-4df927b50bf2_artifacts.zip` at repo root).
Single PR, executed across three context-clearing sessions on a shared branch.

## Ground rules (apply every session)

- Branch: `scds-openscientist-enrichment` (create from `main` in session 1, reuse after).
- **Never** hand-write `references_cache/*.md`. For every new PMID:
  `just fetch-reference PMID:XXXX` then `just validate-references kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml`.
- Snippets must be **exact substrings** of the cached abstract. The OpenScientist
  report paraphrases — re-quote from the real abstract before committing.
- If a PMID 404s on PubMed (some 2026 IDs in the report are unverified),
  drop the claim or move it to `notes:` rather than fabricate.
- Targeted `git add` only — never `git add .`. Stage `kb/disorders/`,
  `references_cache/`, and any new `research/` notes you create.
- Run after every session: `just validate kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml`,
  `just validate-references kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml`,
  `just validate-terms-file kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml`.
- End each session with a commit pushed to the branch so the next session can
  resume cold from `git log` + this plan.
- Do **not** open the PR until session 3.

## Source map (where the synthesis lives)

- `/tmp/scds_artifacts/final_report.md` — primary narrative, 21 findings, hypothesis table
- `/tmp/scds_artifacts/provenance/iter*_transcript.json` — per-iteration evidence trails
- `/tmp/scds_artifacts/provenance/scds_pathogenesis_model.json`,
  `comprehensive_driver_classification.json`, `scds_evidence_map.json` — structured findings
- Current entry: `kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml`

## Session 1 — Developmental pathophysiology + two-hit framing

Goal: add the congenital-thin-bone "first hit" mechanism and remodeling biology
as new `pathophysiology` nodes, and reframe the existing dehiscence node as the
intersection of Hit 1 + Hit 2.

- [ ] Create branch `scds-openscientist-enrichment` from `main`
- [ ] Fetch references (one `just fetch-reference` per ID, then verify abstract):
  - [ ] PMID:10680863 (Carey 2000 — postnatal SSC bone development)
  - [ ] PMID:25406876 (Jackson 2015 — pediatric prevalence 51%→11%)
  - [ ] PMID:21393404 (Nadgir 2011 — age-dissociation thinning vs dehiscence)
  - [ ] PMID:25998441 (Park 2015 — all canals thinner, pneumatization)
  - [ ] PMID:26738982 (Fraile Rodrigo 2016 — endochondral/intramembranous junction)
  - [ ] PMID:37777625 (tegmen-SSCD co-occurrence)
  - [ ] PMID:22429945 (spontaneous tegmen defect + SSCD)
  - [ ] PMID:15630389 (OPG in inner ear)
  - [ ] PMID:16467704 (OPG knockout otic capsule resorption)
  - [ ] PMID:8883642 (Nemzek — otic capsule ossification timeline) — only if quotable
  - [ ] PMID:41218633, PMID:41941208 — verify exist before adding; drop if not
- [ ] Add pathophysiology node **"Developmental Otic Capsule Bone Deficiency"**
  upstream of `Bony Dehiscence of Semicircular Canal`. Cell types: osteoblast
  (CL:0000062). Biological process: GO:0001958 (endochondral ossification) or
  GO:0030282 (bone mineralization) — pick whichever has a quotable evidence link.
  `downstream:` to `Bony Dehiscence of Semicircular Canal`.
- [ ] Add pathophysiology node **"Endochondral-Intramembranous Junction Vulnerability"**
  with tegmen co-occurrence evidence; `downstream:` to dehiscence node.
- [ ] Add pathophysiology node **"OPG-Mediated Otic Capsule Remodeling Suppression"**
  (cell types osteoclast/osteoblast, BP `bone remodeling` GO:0046849 with
  `modifier: DECREASED`); evidence from PMID:15630389, 16467704. Edge:
  `downstream` → `Bony Dehiscence of Semicircular Canal` describing how loss of
  OPG protection permits acquired erosion (Hit 2 amplifier).
- [ ] Update `pathophysiology[Bony Dehiscence...].description` to reference the
  two-hit framing without breaking existing evidence blocks.
- [ ] Update top-level `notes:` with the radiographic 3.6–11% adult / cadaveric
  0.5–1.4% prevalence dissociation and the Hit-1/Hit-2 summary (no evidence
  block needed — `notes` is free text).
- [ ] `just qc` — fix anything red.
- [ ] Commit: `feat(scds): add developmental bone deficiency pathophysiology and two-hit framing`
- [ ] Push branch.

## Session 2 — Genetic drivers

Goal: populate the empty `genetic:` section with three driver classes.

- [ ] `git fetch && git checkout scds-openscientist-enrichment && git pull`
- [ ] Re-read this plan + last commit on the branch.
- [ ] Fetch references:
  - [ ] PMID:27631835 (Noonan 2016 — CDH23, RR=10)
  - [ ] PMID:28484680 (Chung 2017 — EDS-HT bilateral SSCD)
  - [ ] PMID:30385359 (Preet 2019 — additional EDS-HT cases)
  - [ ] PMID:22936282 (Down syndrome inner ear, 8.8% SSCD)
  - [ ] PMID:31804144 (Cat Eye syndrome posterior SCD)
  - [ ] PMID:32526405 (Yu & Canalis — NOTCH2 osteoclastogenesis) — only if NOTCH2 added
  - [ ] PMID:32143606 / PMID:41326232 (Hajdu-Cheney / NOTCH2) — verify before use
  - [ ] PMID:10433909 (DLX5 KO) — for candidate-gene `notes` only, not as primary evidence
  - [ ] PMID:39837070 (NOG variants + inner ear) — same caveat
- [ ] Add `genetic:` entries (use schema's `GeneticFactor` shape — check existing
  disorder files like `Ehlers_Danlos_Syndrome.yaml` or any with populated
  `genetic:` for the canonical structure):
  - [ ] **CDH23** (`hgnc:1773`) — strongest single-gene association
  - [ ] **NOTCH2** (`hgnc:7882`) gain-of-function — progressive bone erosion via Hajdu-Cheney; mark evidence_source carefully
  - [ ] **COL5A1 / COL3A1 / EDS-HT** — connective-tissue pathway; bilateral pattern
  - [ ] **Trisomy 21** — chromosomal class; document via PMID:22936282
  - [ ] **Chr22 duplication / Cat Eye** — chromosomal class; PMID:31804144
- [ ] DLX5/HOXA1/NOG: do **not** add as `genetic:` entries (no human SCDS data).
  Add a paragraph under `notes:` listing them as untested candidate genes with
  links to the supporting mouse / non-SCDS clinical data.
- [ ] If the report's NOTCH2-PYK2 mechanistic chain (PMID:26829213, 25257302)
  is quotable, add as additional `evidence:` items on the NOTCH2 entry —
  otherwise omit.
- [ ] Run term validation specifically — every HGNC/MONDO ID must round-trip:
  `just validate-terms-file kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml`.
- [ ] `just qc` clean.
- [ ] Commit: `feat(scds): add genetic drivers (CDH23, NOTCH2, EDS, chromosomal)`
- [ ] Push.

## Session 3 — Environmental triggers, hormonal modifier, PR

Goal: expand the `environmental:` section, capture the female-predominance/
hormonal modifier signal, then ship the PR.

- [ ] `git fetch && git checkout scds-openscientist-enrichment && git pull`
- [ ] Fetch references:
  - [ ] PMID:41063339 (Wei 2026 — n=405 surgical cohort triggers) — verify exists
  - [ ] PMID:30928582 (Chen 2019 — head trauma → bilateral)
  - [ ] PMID:34424380 (Berkiten 2022 — IIH/SSC bone)
  - [ ] PMID:28833207 (Kuo 2018 — no IIH/SSCD association)
  - [ ] PMID:36573139 (selective SSC thinning women >45) — verify
  - [ ] PMID:19121641 (estrogen-OPG link)
  - [ ] PMID:31035843 (no sex difference in baseline thickness — used as a
        contrasting datapoint)
- [ ] Expand existing `Loud Sound and Pressure Changes` entry with the Wei 2026
  trigger-frequency breakdown (Valsalva 33% / trauma 32% / noise-pressure 27%).
- [ ] Add new `environmental:` entries:
  - [ ] **Chronic occupational noise / ambient pressure exposure** (`presence: Predisposing`).
  - [ ] **Elevated intracranial pressure / IIH** (`presence: Predisposing`,
        `supports: PARTIAL` on conflicting evidence). Capture both Berkiten and Kuo.
  - [ ] **Post-menopausal estrogen decline** (`presence: Modifying`) — bridges to
        OPG node from session 1 via `notes` cross-reference.
- [ ] Strengthen existing `Minor Head Trauma` with bilateral-association evidence
  from Chen 2019.
- [ ] Add to `notes:` a one-paragraph summary of female predominance
  (F:M = 1.36:1, four-cohort meta of n=785 in the report). Cite only PMIDs
  whose abstracts directly support the per-cohort numbers; meta-analysis numbers
  computed by the report itself can't be cited as a quote — describe in prose.
- [ ] Final QC sweep:
  - [ ] `just qc`
  - [ ] `just compliance-weighted` — confirm SCDS score moved up
  - [ ] `git diff --stat origin/main...HEAD` — sanity check scope
  - [ ] Confirm only `kb/disorders/Semicircular_Canal_Dehiscence_Syndrome.yaml`
        and `references_cache/PMID_*.md` are staged (no derived HTML, no
        unrelated files).
- [ ] Commit: `feat(scds): expand environmental triggers and hormonal modifier`
- [ ] Open PR via `/create-pr` skill (or `gh pr create` directly):
  - Title: `Enrich SCDS entry with two-hit pathogenesis, genetic drivers, and environmental triggers`
  - Body: summarize the three commits, link to source artifact bundle (zip
    filename + final_report.md provenance), list new PMIDs added.
- [ ] Mark this project file done; leave it in `projects/` as provenance.

## Out of scope (do not do here)

- GWAS / WES — none exist for SCDS (the report's largest gap); not curatable.
- New mechanism module (`kb/modules/`) — the developmental-bone pattern recurs
  across temporal-bone disorders, but extracting a module is a follow-up PR.
- DLX5/HOXA1/NOG as primary genetic entries — wait for human SCDS data.
- MorPhiC cellular phenotypes — not applicable to a structural disorder.
- Touching other disorder files even if cross-references seem useful.
