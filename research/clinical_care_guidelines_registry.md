# Clinical Care Guidelines Registry (seed)

**Tracking issue:** [#4878 — collect clinical care guidelines](https://github.com/monarch-initiative/dismech/issues/4878)

**Goal.** Scale the approach used for the **Fanconi Anemia** entry — deep integration of a
disease-specific clinical care guideline — to other disorders where comparable high-quality
guidelines exist. This file is the seed registry plus a reusable search / prioritization /
gap-assessment methodology. It is a *worklist*, not curated KB content.

> **Provenance & verification policy.** Every PMID in the "Verified guideline" tables below
> was checked with `just fetch-reference PMID:<id>` and its real PubMed title is reproduced
> verbatim. **Do not** add any PMID to a KB entry from this file without re-running
> `just fetch-reference` + `just validate-references` on the entry, per `CLAUDE.md`. The
> registry records *which guideline document to mine*, never a pre-validated snippet.

---

## The Fanconi Anemia reference model

`kb/disorders/Fanconi_Anemia.yaml` is the deepest entry in the KB (4,789 lines, ~246 PMID
references). It was built from the **5th edition Fanconi Anemia Clinical Care Guidelines**,
anchored on two verified sources:

| Source | PMID (verified title) |
|---|---|
| FA GeneReviews chapter | `PMID:20301575` — *Fanconi Anemia.* |
| FA endocrine screening recommendations | `PMID:25575015` — *Endocrine disorders in Fanconi anemia: recommendations for screening and treatment.* |

The guideline drove (a) phenotype coverage (screening-indicator tables → individual
phenotype entries) and (b) treatment/surveillance content (e.g. annual TSH/free-T4, biennial
cancer surveillance), with `notes:` fields tying phenotypes back to specific guideline tables.
That "guideline table → phenotype/surveillance rows + frequency data" pattern is the template
to replicate.

---

## ⚠️ Anti-hallucination audit of the auto-generated issue summary

The auto-summary on #4878 proposed a Tier-1 table of guideline PMIDs. **8 of the 10 suggested
PMIDs are hallucinated / misattributed** — they resolve to unrelated papers. This mirrors the
DR-failure pattern documented in `CLAUDE.md` (§2a) and the #4873 precedent (both PMIDs there
were also wrong). The verified replacements are in the next section. **Do not use any of the
debunked PMIDs below.**

| Disease (as claimed) | Suggested PMID | Actually resolves to | Verdict |
|---|---|---|---|
| Tuberous Sclerosis Complex | `PMID:24053983` | 2012 International TSC Consensus surveillance/management | ✅ correct |
| Ehlers-Danlos Syndrome | `PMID:28306229` | 2017 international classification of the EDS | ✅ correct |
| Duchenne Muscular Dystrophy | `PMID:29940086` | "Barriers… Long-Acting Reversible Contraceptives in Massachusetts Community Health Centers" | ❌ hallucinated |
| Spinal Muscular Atrophy | `PMID:28528957` | "Proteasomes in corneal epithelial cells…" | ❌ hallucinated |
| Spinal Muscular Atrophy | `PMID:29681584` | "Fate of Acute Heart Failure Patients With Mid-Range Ejection Fraction" | ❌ hallucinated |
| Neurofibromatosis type 1 | `PMID:33860374` | plant pathology (*Xylella fastidiosa* in *Spartium junceum*) | ❌ hallucinated |
| Turner Syndrome | `PMID:28049635` | "Cost… clinical decision support systems for cardiovascular disease prevention" | ❌ hallucinated |
| Prader-Willi Syndrome | `PMID:26483315` | "…21-Gene Recurrence Score Assay on Chemotherapy Delivery in Breast Cancer" | ❌ hallucinated |
| Phenylketonuria | `PMID:33808622` | "…Microbial Consortia for Improving Gluten Digestion…" | ❌ hallucinated |
| Marfan Syndrome | `PMID:28286880` | "The [5+5] route to the phenanthrene skeleton" (organic chemistry) | ❌ hallucinated |

**Takeaway:** auto-summary PMID suggestions for this issue ran ~80% hallucinated. Treat all
machine-suggested citations as *leads to verify*, never ground truth.

---

## Tier 1 — verified disease-specific foundation guidelines

Each PMID below was fetched and title-verified. The `dismech entry` and `cites guideline?`
columns were checked against `kb/disorders/` on `main` (this is the gap-assessment).

| Disease | Verified guideline PMID & title | dismech entry | Already cites guideline? |
|---|---|---|---|
| Duchenne Muscular Dystrophy | `PMID:29395989` — *Diagnosis and management of Duchenne muscular dystrophy, part 1…* | `Duchenne_Muscular_Dystrophy.yaml` | **No → mine** |
| Spinal Muscular Atrophy | `PMID:29290580` — *Diagnosis and management of spinal muscular atrophy: Part 1…* | `Spinal_Muscular_Atrophy.yaml` | **No → mine** |
| Tuberous Sclerosis Complex | `PMID:24053983` — *Tuberous sclerosis complex surveillance and management: recommendations of the 2012 International TSC Consensus Conference.* | `Tuberous_Sclerosis_Complex.yaml` | **No → mine** |
| Neurofibromatosis type 1 | `PMID:31010905` — *Health Supervision for Children With Neurofibromatosis Type 1.* | `Neurofibromatosis_Type_1.yaml` | **No → mine** |
| Marfan Syndrome | `PMID:37389507` — *2022 ACC/AHA guideline for the diagnosis and management of aortic disease…* | `Marfan_Syndrome.yaml` | **No → mine** |
| Phenylketonuria | `PMID:24385074` — *Phenylalanine hydroxylase deficiency: diagnosis and management guideline.* (ACMG) | `Phenylketonuria.yaml` | Yes (already integrated) |
| Ehlers-Danlos Syndrome | `PMID:28306229` — *The 2017 international classification of the Ehlers-Danlos syndromes.* | `Ehlers-Danlos_Syndrome.yaml` (+ 4 subtype entries) | **No → mine** |
| Turner Syndrome | `PMID:28705803` — *Clinical practice guidelines for the care of girls and women with Turner syndrome: proceedings from the 2016 Cincinnati International Turner Syndrome Meeting.* | **none — new-entry gap** | n/a |

**Gap summary:** 6 of 7 already-curated entries do **not** yet cite their disease's
foundation guideline (only PKU does). Turner syndrome has a high-quality guideline but **no
dismech entry at all** — the single new-entry opportunity in this seed batch.

### Leads needing confirmation (not yet verified — do not cite as-is)

- **Prader-Willi Syndrome** — `PMID:22237428` resolves only to the GeneReviews stub
  (*"Prader-Willi syndrome."*), not the management consensus. The true diagnosis/management
  consensus PMID still needs to be located and verified before use.

---

## Methodology (reusable)

### Search strategy (tiers, highest yield first)

1. **Tier 1 — disease-specific foundation/consensus guidelines.** Patient-foundation or
   international-consortium documents with tabular screening indicators and surveillance
   schedules (the FA model). Highest curation yield.
2. **Tier 2 — GeneReviews chapters.** Standardized *Management* / *Surveillance* sections
   across >900 chapters; the highest-coverage resource for inherited-disease management.
   Cross-reference existing dismech entries first.
3. **Tier 3 — Orphanet / European Reference Network (ERN) guidelines.** Best for rare
   diseases with little other structured guidance.

### Prioritization criteria

1. **HPOA density gap** — diseases whose canonical `phenotype.hpoa` annotations are sparse
   relative to what a guideline covers (cross-ref #3179, #3846).
2. **Entry-completeness gap** — diseases with a stub dismech entry but few phenotypes/treatments
   (compliance dashboard).
3. **Guideline richness** — explicit tabular screening indicators (like FA Table 1) map far
   more cleanly than narrative-only guidelines.
4. **Frequency data present** — guidelines with frequency columns ("80% of patients") directly
   address the HPOA frequency-annotation gap (#3179).
5. **Surveillance/treatment novelty** — content not otherwise capturable from individual papers.

### Gap-assessment procedure (deterministic, repeatable)

1. Verify a candidate guideline PMID with `just fetch-reference PMID:<id>`; confirm the title
   is the guideline (the anti-hallucination step — ~80% of unverified leads failed here).
2. Check `kb/disorders/` for an existing entry (`grep -ril <disease>`); if absent, route to a
   new-entry curation issue (high-effort tier).
3. If an entry exists, `grep <PMID>` it to see whether the guideline is already integrated.
4. Score with the criteria above; open a bounded per-disease child issue for the highest-ranked
   targets.

---

## Suggested next actions

- [ ] Confirm the Prader-Willi consensus-guideline PMID; extend the registry with verified
      Tier-1 rows for additional foundation guidelines (CF, sickle cell, MPS subtypes, etc.).
- [ ] Open bounded per-disease child issues to mine the 6 "No → mine" Tier-1 guidelines into
      their existing entries (start with the richest tabular guidelines: TSC, DMD, SMA).
- [ ] Route **Turner syndrome** to a new-entry curation issue (verified guideline available,
      no entry yet).
- [ ] Consider a schema follow-up to capture guideline provenance distinctly from individual
      PMID evidence items (e.g. a `[GuidelineCareRecommendation]` reference tag, mirroring the
      existing `[GeneReviews]` tag convention).
