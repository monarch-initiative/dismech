# dismech Maturity Evaluation: Draft for Group Feedback

*Draft of 2026-10-15. Author: Melissa Haendel, with AI assistance (Claude Code).*

## Purpose

We want one shared, repeatable answer to "how mature is dismech?", scored by dimension instead of one headline number. The draft below starts from the two public dashboards ([priority](https://dismech.monarchinitiative.org/dashboard/priority.html), [capability metrics](https://dismech.monarchinitiative.org/dashboard/capability_metrics.html)) and the QC gates already in the repo.

The evaluation has three readers: funders, the FDA, and ourselves. For us, it decides when dismech is ready for clinical use, so each dimension needs a threshold, not just a score.

**Scope.** This evaluates dismech only, not the wider Monarch Initiative. Monarch resources appear here only as dismech's inputs (MONDO, HPO, phenotype annotations) or as consumers of dismech data (the Monarch knowledge graph).

**Timely context.** On 14 October 2026 the FDA launched the [Rare Disease Framework Initiative](https://www.fda.gov/news-events/press-announcements/fda-launches-rare-disease-framework-initiative-develop-holistic-fit-purpose-framework-rare-disease), a "fit-for-purpose framework" for rare disease drug development. Two of its six commitments match what dismech offers: "Building shared resources" and "Championing the use of cutting-edge science, novel methods." A public meeting is on 28 October 2026, followed by roundtables and Requests for Information. This evaluation could be the evidence behind a dismech response.

The same day, the Rare Disease Congressional Caucus briefing (RARE Foundation, 14 October 2026) presented dismech against the **Cures in Care** discussion draft, *Next-Generation U.S. Clinical Development to Accelerate Cures* (Rep. Auchincloss; RARE Foundation community comments of 30 June 2026). Three of the draft's goals map onto dismech, and each one points at a rubric dimension that would have to be strong for the claim to hold:

| Draft goal | What dismech offers | Rubric dimension that must back it |
| --- | --- | --- |
| Non-animal methods (NAMs) for rare disease | Which models cover which disease mechanisms, and where the gaps are | Disease models |
| Rare Disease Innovation Hub; clinical outcome assessment validation | Mechanism evidence for candidate surrogate endpoints, including what an endpoint does not measure | Use: clinical trials; mechanistic connectivity |
| Plausible Mechanism Framework; shared reviewer knowledge (asked for in RARE Foundation's comments) | Computable, cited mechanisms anyone can reuse | Evidence integrity; correctness |

The worked example in the briefing is Fabry disease. Its FDA surrogate endpoint, GL-3 clearance from kidney peritubular capillaries, reads out the renal blood-vessel branch of the mechanism, while heart disease, the leading cause of death, sits on a different branch. The dismech entry (`kb/disorders/Fabry_Disease.yaml`) already records that surrogate link. The approach was presented at the FDA and Triangle CERSI workshop on rare disease surrogate endpoints on 18 May 2026.

How to give feedback: this file is the working copy. Edit it directly in a pull request, whether that is a changed draft score, a reworded rubric level, or an answer in the questions table, or leave a suggestion on the pull request that changes it. The questions in [Ten questions to settle](#ten-questions-to-settle) are the decisions we most need from the group.

## Foundations: what the dashboards measure today

The two dashboards measure breadth and coverage well, but neither measures correctness, use, or how sustainable the curation is. Figures are from the 2026-10-15 build.

| Dashboard | What it measures | Headline figures | What it is not evidence of |
| --- | --- | --- | --- |
| [Capability metrics](https://dismech.monarchinitiative.org/dashboard/capability_metrics.html) | Corpus size, section coverage, evidence counts, ontology richness, mechanistic depth, treatments, compliance score, creation velocity, MONDO coverage | 3,457 entries; 245,742 evidence items from 49,000 references; 24,543 pathophysiology nodes; 49,500 causal edges; 89.3% average compliance; 48.5% of MONDO human-disease terms have an exact or parent page | Whether claims are correct; whether anyone uses the KB; how stale an entry is |
| [Priority](https://dismech.monarchinitiative.org/dashboard/priority.html) | MONDO candidate queue with reweightable scores and recommended actions | 31,557 candidates; 5,880 already curated (18.6%); 3,067 uncurated candidates carry a name-confusion risk badge | What should be curated next. Its top-ranked rows are broad parent terms, which is why the hand-edited stub queue (2,551 stubs) replaced it as the work queue (issue #8969) |

Three readings matter for maturity:

- **Section coverage is uneven.** Phenotypes 100%, pathophysiology 99.9%, treatments 95.5%, genetics 87.2%; but differential diagnosis 41.2%, biochemical markers 31.6%, histopathology 16.6%, definitions 9.0%.
- **Velocity counts creation only.** `updated_date` is deprecated, so the dashboard shows 2,927 entries created since April 2026 and almost no updates. Re-curation is visible only through `just last-pass-report`.
- **Compliance is a completeness score, not a quality score.** An entry can score high with every phenotype disconnected from the pathograph; causal in-link coverage (about 54%) is tracked separately by `just compliance-connectivity`.

## Maturity models we borrow from

No existing model fits dismech whole, so the rubric borrows one idea from each of six. The two FDA documents matter most, because they say what a regulator would actually look for in a curated knowledge resource.

| Model | What it assesses | What dismech takes from it |
| --- | --- | --- |
| [FDA: public genetic variant databases](https://www.fda.gov/media/99200/download) (final guidance, 2018) | Whether a curated database can be FDA-recognized as valid scientific evidence | A ready-made checklist for governance: public, versioned SOPs reviewed at least annually; data preservation if the resource stops; standard nomenclature; documented evidence sources; tiered assertions using multiple lines of evidence; evaluation "by at least two qualified and trained professionals"; conflict-of-interest disclosure |
| [FDA: AI to support regulatory decision-making](https://www.fda.gov/media/184830/download) (draft guidance, January 2025) | Credibility of an AI model for a defined context of use, in seven steps | Score fitness per intended use, not in general. Risk combines model influence and decision consequence, so a diagnostic use needs more evidence than a research one. Fits our AI-curated pipeline directly |
| [NASA technology readiness levels](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/technology-readiness-levels/) | Nine stages from basic research to proven in operation | Level names tied to where the resource has been tested: lab, realistic simulation, real use. "Proven in operation" cannot be claimed before a clinical pilot |
| [ClinVar review status](https://www.ncbi.nlm.nih.gov/clinvar/docs/review_status/) | 0 to 4 stars per variant record, from no criteria to practice guideline | Per-entry maturity tiers, so users can filter: e.g. 0 = unreviewed, 1 = validated, 2 = independent agreement, 3 = expert reviewed, 4 = matches practice guidelines |
| [Kahn et al. data quality framework](https://pmc.ncbi.nlm.nih.gov/articles/PMC5051581/) (EHR data, 2016) | Conformance, completeness and plausibility; checked internally (verification) or against an outside standard (validation) | Separate what our CI gates verify from what only external comparison validates. Most dismech gates are verification |
| [RDA FAIR data maturity model](https://archive.rd-alliance.org/node/69063) (final version DOI 10.15497/rda00050) | FAIR indicators, each ranked essential, important or useful | Prioritize indicators instead of weighting them equally. A possible answer to question 3 on weighting |

One implication: per-entry tiers (ClinVar-style) and the corpus rubric are different things. A clinician needs to know how far to trust this entry; a funder or regulator needs the profile of the whole resource. We should report both.

## Proposed maturity model

Sixteen dimensions, each scored 1 to 5, plus downstream use, which is tracked but not scored. Draft scores are a starting point for discussion, not a verdict; they lean high on structure and low on correctness and use, where we have the least direct evidence.

| Dimension | Level 1: emerging | Level 3: established | Level 5: mature | Draft score |
| --- | --- | --- | --- | --- |
| Coverage: MONDO mechanisms | Hand-picked exemplar diseases | Most MONDO human-disease terms have an entry or parent entry with a mechanism | Every in-scope MONDO term has a mechanism, or is recorded as grouping, subtype or out of scope | 3 |
| Coverage: literature | Key papers cited | Each entry cites the core references for its disease type (for example GeneReviews for Mendelian, WHO classification for cancer, recent systematic reviews for complex disease) | Mechanism claims checked against a literature sample in every disease-type stratum, with recall reported per stratum and Mendelian broken out, not dominating | 3 |
| Coverage: clinical care guidelines | Not tracked | Guidelines found for most diseases that have them | Every current practice guideline is cited, and its diagnosis and treatment content is reflected in the entry | 1 |
| Content completeness | Phenotypes and a short mechanism | Sections that apply to the disease type are filled in most entries | Every applicable section is filled; sections that do not apply are never counted against an entry | 3 |
| Disease models | Few models recorded | Animal and cell models listed for most diseases that have them | Animal, cell and computational models linked to the mechanism nodes they reproduce, with how faithfully | 2 |
| Schema expressiveness | Much reference content fits only in free text | Most reference statements in the pilot fit a structured slot | Schema gaps are rare in the five-bin sample for every disease type | Not yet measured |
| Schema stability | Frequent breaking changes | Changes mostly additive, with migrations | New elements per month low and falling for three months; breaking changes announced and migrated | 2 |
| Evidence integrity | Citations exist | Every snippet verified against a cached source | Verified snippets plus graded directness and quote role across the corpus | 4 |
| Correctness | Unreviewed | AI review on every PR plus spot checks | Blinded expert review of a random sample shows an error rate below an agreed threshold; independent curators agree | 2 |
| Mechanistic connectivity | Mechanism as prose | Pathograph nodes with ontology bindings | Phenotypes and genes wired to mechanisms; modules reused across diseases | 3 |
| Ontology and interoperability | Free-text terms | Terms validated against ontologies | Stable exports (KGX, BioLink) consumed by external knowledge graphs | 4 |
| Governance and process | Ad hoc | CI gates, history records, design-decision register | Gates plus documented human oversight and contributor onboarding; meets the FDA variant-database recognition checklist | 4 |
| Freshness | One-time build | Re-curation tracked | Staleness bounded by policy; content survives model and staff turnover | 2 |
| Use: diagnostics and variant prioritization | Phenotypes and genes listed | Benchmarked on a public set of solved cases, with top-10 accuracy at least matching an HPO-annotation baseline; mechanism of disease (loss or gain of function) recorded for most disease genes | Evaluated prospectively in a diagnostic workflow, error rate reported, and per-entry tiers usable as a filter | 2 |
| Use: drug repurposing and development | Treatments listed | Most treatments linked to the mechanism they act on; approved-indication recall measured against NCIT | A time-split benchmark shows mechanism paths rank later-approved indications above chance, and developers use the results | 2 |
| Use: clinical trials | Some trials listed | Trial lists checked against ClinicalTrials.gov and kept current; natural history recorded for most rare disease entries | Endpoints, surrogate biomarkers, natural history and cohort definitions curated for priority rare diseases and used in trial design | 1 |
| Downstream use (tracked, not scored) | | | | Not scored |

## Candidate metrics per dimension

Most dimensions can be scored from existing tooling; guideline coverage, correctness and use need new measurement.

| Dimension | Candidate metric | Current value | Source |
| --- | --- | --- | --- |
| Coverage: MONDO mechanisms | Share of MONDO human-disease terms with an exact or parent entry that has at least one pathophysiology node | 48.5% have an exact or parent page | Capability dashboard (add the mechanism filter) |
| Coverage: MONDO mechanisms | Stub queue size; share of stubs with an `entry_type` decision | 2,551 stubs | `just stub-stats` |
| Coverage: literature | Core-reference citation rate per disease type; Mendelian (GeneReviews) reported as its own stratum | 49,000 unique references | `just check-genereviews` |
| Coverage: literature | Recall of mechanism claims against recent high-quality reviews, sampled equally from each disease-type stratum. Mendelian entries are 60% of the corpus (2,059 of 3,457), so an unstratified average would mostly measure them | Not measured | New benchmark |
| Coverage: clinical care guidelines | Share of diseases with a current practice guideline that cite it | Not measured | `collect-care-guidelines` skill, extended to a census |
| Content completeness | Applicable sections filled, scored against a per-disease-type template | Not reported; raw figures 9.0% to 100% by section | Capability dashboard (extend) |
| Disease models | Entries with animal, cell-based and computational models | 37.9% / 17.9% / 1.4% | Capability dashboard |
| Disease models | Model links that name the mechanism node they reproduce, with fidelity | Not reported | `just model-scale-audit` |
| Evidence integrity | Share of snippets verified against cache; size of each grandfathered backlog | Not reported corpus-wide | `just count-verified-snippets`, `tests/*_baseline.txt` |
| Correctness | Error rate per 100 claims in a blinded expert sample | Not measured | New audit (see below) |
| Correctness | Agreement between independent curations, strict and subsumption-aware | 2 diseases: phenotype agreement 0.48 to 0.53 strict, 0.77 to 0.84 subsumption-aware | `experiments/interannotator/` |
| Mechanistic connectivity | Phenotypes with a causal in-link; genes with a mechanism out-link | About 54% / 49% | `just compliance-connectivity` |
| Mechanistic connectivity | Entries conforming to at least one module | 38.4% | Capability dashboard |
| Ontology, governance and freshness | Term-validation pass rate; entries never re-curated or last passed by an older model | Not reported | `just validate-terms`, `just last-pass-report` |
| Use and impact | Downstream users found by code search (tracked, not scored) | Not tracked | New register |

## Blinded review design

Correctness gets two arms, both reusing the protocol in [`experiments/interannotator/`](https://github.com/monarch-initiative/dismech/tree/main/experiments/interannotator).

1. **Inter-curator consistency.** Curate a disease twice, independently, and compare with `compare.py`. Report strict and subsumption-aware agreement, record any leakage between curators before the results, and separate defects (rule violations) from differences (defensible choices).
2. **Blinded expert audit.** Clinical experts grade a random sample of claims against their own reading of the literature. They do not see who or what curated the entry. The sample is stratified by disease type and by section.

Both existing studies compared two AI-agent curations: FG syndrome 1 used the same model twice, and Rienhoff syndrome compared two different agents. They measure how consistent the pipeline is, not whether it agrees with human experts, so the next studies should add a human curator arm.

## Fitness for each intended use

Following the FDA AI guidance, dismech should be judged per context of use, not in general. Each use below gets its own question, its own measures, and a benchmark run against an outside answer key. The required bar rises with the consequence of a wrong answer, so diagnostics needs the strongest evidence.

| Use | Question it answers | Measures | Benchmark against an answer key | Where we are (2026-10-15) |
| --- | --- | --- | --- | --- |
| Diagnostics and variant prioritization | Given a patient's phenotypes and variants, which disease and gene are most likely? | Gene coverage against ClinGen definitive and strong pairs; mechanism of disease recorded per gene (loss of function, gain of function, dominant negative), which variant interpretation depends on; phenotype frequency bands; differential diagnoses | Agreement with ClinGen gene-disease validity and mechanism-of-disease calls; rank of the true diagnosis for published solved cases, top-1 and top-10, against an HPO-annotation baseline | No case-based benchmark yet. 795 of 3,022 entries with genetics record a functional-impact category; 1,429 of 3,466 entries list differential diagnoses |
| Drug repurposing and development | Which existing drugs act on this disease's mechanisms, and which mechanisms are untargeted? | Treatments linked to the mechanism node they act on; approved-indication recall against NCIT accepted therapeutic uses; druggable targets per mechanism; disease models linked to mechanism nodes | Time-split test: freeze the KB at a past date and check whether its mechanism paths rank drugs whose new indications were later approved or later succeeded in trials | 5,651 of 14,866 treatments (38%) name a target mechanism. `just ncit-p302-audit` measures indication recall |
| Clinical trials | Can a sponsor find patients, choose endpoints, and understand natural history from dismech? | Recall of active interventional trials per disease; trial status freshness; biomarkers tied to FDA surrogate endpoints, with the mechanism branches each endpoint measures and misses (the Fabry case); diseases sharing a mechanism module, as basket-trial candidates; natural history and progression; computable cohort definitions | Trials listed per entry compared with ClinicalTrials.gov for the same MONDO term; definitions checked against published validated phenotype algorithms | 693 entries list 1,635 trials. 15 entries link a biomarker to an FDA surrogate endpoint; progression is filled in 35% of entries and definitions in 9%. `just clinicaltrials-status-audit` checks status drift |

Our reading of the FDA Rare Disease Framework Initiative is that it raises the weight of the trials row. With small populations, natural history, mechanism and biomarker evidence matter more, and those are sections dismech already holds.

## Coverage and schema together

Proposal: measure both at once by taking statements from trusted external references and trying to encode each one in dismech. Every statement lands in one of five bins, which separates a schema gap (we cannot say it) from a curation gap (we can say it but have not).

| Bin | Meaning | Who fixes it |
| --- | --- | --- |
| Encoded | The KB already states it, in a structured slot | Nobody |
| Curation gap | A slot exists, but the entry does not fill it | Curators |
| Free-text only | It can be stated only in `description` or `notes`, so it cannot be queried | Schema (often a small extension) |
| Schema gap | There is nowhere to state it | Schema |
| Not applicable | Out of scope for dismech, or for this disease type | Nobody; excluded from the denominator |

The first four bins form a 2x2: whether the schema has a structured slot for the statement, against whether the entry states it.

| | Entry does not state it | Entry states it |
| --- | --- | --- |
| **Schema has a structured slot** | Curation gap (fixed by curators) | Encoded (counts toward content recall) |
| **Schema has no structured slot** | Schema gap (needs a schema change) | Free-text only (needs a schema change, often small) |

Two numbers per facet and disease type then come out of the same sample:

- **Schema expressiveness** = (encoded + curation gap) / applicable statements
- **Content recall** = encoded / applicable statements

**Reference set per facet** (one external source per row, to be agreed):

| Facet | Candidate reference | Existing tooling |
| --- | --- | --- |
| Disease scope | MONDO human disease | Capability dashboard, `just stub-stats` |
| Phenotypes | HPO annotations (OMIM, Orphanet); guideline-derived profiles | `just d2p-audit` |
| Genes and inheritance | ClinGen, GenCC | `just g2p-compare`, `just check-gene-validity` |
| Mechanisms | By disease type: GeneReviews for Mendelian; WHO classification and CIViC for cancer; recent systematic reviews for complex disease; CDC and WHO pathogen references for infectious disease | `just check-genereviews` |
| Diagnosis and treatment | Current clinical practice guidelines | `collect-care-guidelines` skill |
| Disease models | Alliance of Genome Resources / MGI models; Cellosaurus disease cell lines | None yet |
| Natural history, prevalence | Orphanet, GeneReviews | Orphanet structured source |

**What we already know.** Two partial runs show the method works and that recall is low where we have looked. The Fanconi anemia guideline-derived HPO profile had 264 terms; the dismech entry shared 61 of them at the start ([project](https://github.com/monarch-initiative/dismech/blob/main/projects/FANCONI_ANEMIA_GAP_ANALYSIS.md)). An audit of 514 dismech entries against OMIM and Orphanet phenotype annotations found 22,579 annotated phenotypes with no matching term in the entry. Both measured phenotypes only, so neither tells us anything about schema gaps.

**Suggested pilot.** Five diseases per disease type (Mendelian, infectious, cancer, complex, environmental), each with a current practice guideline. Encode every recommendation and every stated fact from the guideline, and report the five bins per facet. A guideline is the right first reference because it is what a clinician would check dismech against.

## Schema stability: how much change is still coming

The schema has not converged yet. Between December 2025 and mid-October 2026 it grew from 47 to 201 classes, 125 to 718 slots, and 34 to 1,493 enum values, and the busiest month was August 2026.

Schema elements added and removed per month, 2026 (classes, slots, enums, enum values and class attributes, counted across every file in `src/dismech/schema/` at each month end on `main`; October covers 1 to 15 October only):

| Month | Added | Removed |
| --- | ---: | ---: |
| Jan | 196 | 0 |
| Feb | 246 | 0 |
| Mar | 76 | 0 |
| Apr | 75 | 0 |
| May | 193 | 50 |
| Jun | 154 | 0 |
| Jul | 396 | 0 |
| Aug | 618 | 2 |
| Sep | 236 | 23 |
| Oct (to 15th) | 210 | 0 |

Three readings from the history (213 schema commits):

- **Growth is accelerating, not tapering.** Schema elements added per month: about 75 in March and April, then 396 in July, 618 in August, 236 in September, and 210 in the first half of October. A converging schema would show those additions falling month on month.
- **Change is almost entirely additive.** Only 75 elements were removed in ten months, in three episodes: the Harrison's chapter enum rework (50 values, May), retiring `PARTIAL` and `WRONG_STATEMENT` evidence grades (August), and generalizing the antisense-specific classes to oligonucleotides (23 elements, September). Existing entries are rarely broken; new capability keeps arriving.
- **Additions track coverage pushes.** Recent additions arrived with new kinds of content, such as drug delivery systems, LOINC measurements and ancestry. The five-bin sample above should predict where the next additions land.

Candidate maturity signal: new schema elements per month falls below an agreed level for three consecutive months, and the five-bin pilot finds few "schema gap" statements.

## Downstream use check (observational, not scored)

Impact is not scored yet, because the resource is not yet mature. A first look on 2026-10-15 found one consumer, the Monarch knowledge graph, and no confirmed outside repository that depends on dismech data or code.

| Project | Relationship to dismech | Status |
| --- | --- | --- |
| [Monarch knowledge graph](https://monarch-app.monarchinitiative.org/Sources/dismech/) | Lists dismech under "KG Data Sources" | Consumer of dismech data; the page does not say what is ingested |
| [SOMAMech](https://github.com/EHS-Data-Standards/somamech) | Describes itself as "dismech-style curation" of PM2.5 publications | Reuses dismech's approach; no data or code dependency seen |
| [CHARMPheno](https://github.com/oneilsh/CHARMPheno) | dismech cites its phenotype profiles | Upstream source, not a consumer |

This is a lower bound. The check used links in dismech's own docs plus a web search, not a GitHub-wide code search. A full scan would search GitHub code for `dismech` and `kb/disorders`, and check package dependents.

## Gaps the dashboards cannot answer

The largest gap is correctness: every current metric counts what exists, and none estimates how much of it is wrong.

- **Accuracy.** Verified snippets prove a quote exists, not that it supports the claim or that the claim is the field's consensus.
- **Stratified completeness.** A single section-coverage percentage mixes disease types; transmission at 5.3% is expected for a corpus that is mostly Mendelian. Templates per disease type are needed before completeness can be scored fairly.
- **Freshness.** No dashboard shows age since last real curation, so 3,000 entries created in six months will look current until they are not.
- **Human oversight.** Agents author, review and merge most PRs; the share with a human in the loop is not reported.
- **Use.** Downstream use is tracked, not scored, until the resource is mature. A first check found only the Monarch knowledge graph.
- **Comparison.** No benchmark of dismech against peer disease resources (Orphanet, GeneReviews, OMIM) on the same diseases.

## Ten questions to settle

Six are answered (first round, 2026-10-15); questions 3, 6, 8 and 10 still need group input.

| # | Question | Why it matters | Answer |
| --- | --- | --- | --- |
| 1 | Who is the evaluation for: the team, funders, prospective users, or a paper? | Sets how formal the scoring and evidence must be | Funders, the FDA, and us, to decide when dismech is ready for clinical use |
| 2 | Do the dimensions cover what "mature" means to us? What would you add, merge or drop? | The rubric is the backbone of every later score | The rubric can be as long as needed. Disease models, schema expressiveness and schema stability added; ontology, governance and freshness kept separate |
| 3 | Should dimensions be weighted, or reported as a profile with no overall score? | A single number invites gaming; a profile is harder to summarize | Open |
| 4 | Which disease populations count as in scope for coverage? | The 48.5% and 18.6% figures use different denominators | Mechanism coverage measured against all MONDO identifiers, plus coverage of the literature and of clinical care guidelines |
| 5 | Should we run a blinded expert review of a random sample of claims? | Correctness is currently unmeasured | Yes, building on the inter-curator studies in `experiments/`. Still open: sample size and who reviews |
| 6 | What error rate would we accept before clinical use? | Gives the correctness level a concrete threshold | Open |
| 7 | Should completeness be judged against a per-disease-type template? | Avoids penalizing entries for sections that do not apply | Yes: entries are not penalized for components that do not apply to their category |
| 8 | How should freshness be defined: time since last human pass, last model pass, or last source change? | Decides what `last-pass-report` must report | Open |
| 9 | Which downstream uses should count as impact? | Use is the dimension with the least data | Not scored yet, because the resource is not mature; downstream use is tracked for information only |
| 10 | How often should we re-score, and should the scores become a dashboard tab? | Turns a one-time review into a tracked trend | Open |

## Next steps

- [x] First-round answers on audience, coverage scope, blinded review, applicability and impact
- [ ] Group answers the open questions (3, 6, 8, 10) and comments on the rubric
- [ ] Define the clinical-use threshold for each dimension, and confirm which FDA framework applies
- [ ] Decide whether to attend the FDA Rare Disease Framework meeting on 28 October 2026 and respond to its Requests for Information
- [ ] Write the per-disease-type completeness templates
- [ ] Run the five-bin guideline pilot (five diseases per type) to measure coverage and schema together
- [ ] Choose the answer key for the diagnostics benchmark (published solved cases, ClinGen gene-disease calls)
- [ ] Design the time-split drug repurposing benchmark
- [ ] Design the blinded expert audit (sample size, reviewers, human curator arm)
- [ ] Map dismech governance against the FDA variant-database recognition checklist and list the gaps
- [ ] Run a full GitHub code search for downstream users, and repeat it each re-scoring
- [ ] Re-score and decide whether to publish scores as a dashboard tab
