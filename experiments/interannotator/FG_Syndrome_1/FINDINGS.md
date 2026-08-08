# Inter-annotator consistency: FG syndrome 1 (MONDO:0010590)

Two independent curations of the same disease entry, compared to estimate how much
of a dismech entry is determined by the evidence and how much by the curator.

| | |
|---|---|
| **Disease** | FG syndrome 1 / Opitz-Kaveggia syndrome, `MONDO:0010590`, `MED12` p.Arg961Trp |
| **Curator A** | The entry merged in [PR #7254](https://github.com/monarch-initiative/dismech/pull/7254), commit `ba33465dd`. Three review rounds with `ai4c-reviewer`, approved. |
| **Curator B** | An independent re-curation run from scratch for this experiment. Never merged into `kb/`. |
| **Date** | 2026-08-01 |
| **Both agents** | Claude Code, same model, same `/curate` skill, same repository state |

## Files

| Path | Contents |
|---|---|
| `FG_Syndrome_1.curator-A.merged-pr7254.yaml` | A, verbatim at `ba33465dd` |
| `FG_Syndrome_1.curator-B.independent.yaml` | B, verbatim as validated |
| `metrics.txt` | `compare.py` output, as run |
| `../compare.py` | The metric script — regenerates every number below |

```bash
uv run python experiments/interannotator/compare.py \
  experiments/interannotator/FG_Syndrome_1/FG_Syndrome_1.curator-A.merged-pr7254.yaml \
  experiments/interannotator/FG_Syndrome_1/FG_Syndrome_1.curator-B.independent.yaml
```

**Both files are frozen snapshots, not live entries.** A was byte-identical to
`kb/disorders/FG_Syndrome_1.yaml` at `ba33465dd`; the live entry has since diverged as
the defects listed below were fixed, so a `diff` against `kb/` will no longer be empty
— that is expected. Neither snapshot is covered by `tests/test_data.py`, which globs
`kb/disorders/*.yaml` only (deliberately — two files named `FG Syndrome 1` would trip
the unique-name check). Both were validated clean against the schema as of
**2026-08-01**; that is a point-in-time statement and they may rot as the schema
evolves.

## Protocol, and how far it actually held

B ran the documented `/curate` pipeline end to end: a fresh falcon deep-research run
(484 s, 20 citations — A's was 459 s, 23 citations), an independent PubMed sweep, an
independent GeneReviews baseline, and independent OAK term lookups. B did not open
A's YAML or A's research report until B had passed schema, term, and reference
validation.

**Independence was partial, and the metrics must be read with that in mind.** Before
starting, B had read PR #7254's *description*, which named the three mechanistic arms
(REST/NRSF, GLI3-SHH, immediate-early genes) and roughly ten PMIDs.

| Dimension | Contaminated? | Trust the number? |
|---|---|---|
| Pathophysiology node structure | **Yes** — arms were named in the PR description | No |
| Reference set | **Partly** — ~10 PMIDs named | Weakly |
| Phenotype terms | No — B never saw A's phenotype list | **Yes** |
| Frequency bands | No | **Yes** |
| Treatment bindings | No | **Yes** |

So the three uncontaminated dimensions carry the result. The mechanism-graph
convergence below is reported for completeness but proves little.

B's entry passed all three validators independently: schema ✓, ontology terms ✓,
references **109/109 snippets verified exact** against the committed cache.

## Results

### Section cardinality

| Section | A | B |
|---|---:|---:|
| phenotypes | 47 | 48 |
| pathophysiology nodes | 9 | 9 |
| causal edges | 12 | 9 |
| treatments | 10 | 8 |
| diagnosis | 4 | 4 |
| differential_diagnoses | 4 | 4 |
| discussions | 1 | 1 |
| genetic / prevalence / inheritance | 1 / 1 / 1 | 1 / 1 / 1 |
| variants | 2 | 1 |
| progression | 3 | 1 |
| evidence snippets | 122 | 109 |
| distinct PMIDs | 14 | 11 |

Two curators working from the same literature independently produced entries of
near-identical shape. Nothing in the schema or skill prescribes 9 pathophysiology
nodes or ~47 phenotypes.

### Phenotype agreement (uncontaminated)

- **Strict HPO term identity:** Jaccard **0.484**, Dice/F1 **0.653** (31 shared of 64 union)
- **Subsumption-aware:** A **76.6%**, B **81.2%** (ancestor closure restricted to
  `is_a`; recomputing without that restriction gives the same eight pairs and the
  same figures, so the result does not depend on the predicate choice)

Strict identity substantially *understates* agreement. Eight apparent disagreements
are the same clinical concept bound at different granularity:

| A | B | Relationship |
|---|---|---|
| `HP:0001319` Neonatal hypotonia | `HP:0001252` Hypotonia | B broader |
| `HP:0012450` Chronic constipation | `HP:0002019` Constipation | B broader |
| `HP:0001371` Flexion contracture | `HP:0034392` Joint contracture | B broader |
| `HP:0001999` Abnormal facial shape | `HP:0000276` Long face | A broader |
| `HP:0000478` Abnormality of the eye | `HP:0000518` / `HP:0000541` / `HP:0000589` / `HP:0000639` | A broader (1→4 split) |

The last row is a systematic difference in strategy rather than an error: A bound one
roll-up ocular term; B split the four individually reported ocular findings into
separate phenotypes with their own bands. Both are defensible. A KB that wants
queryable phenotypes should probably prefer B's split; a KB that wants to avoid
implying denominators it doesn't have should prefer A's roll-up.

**Independent convergence on non-obvious term choices.** These were free decisions with
plausible wrong answers, and both curators landed identically:

- `HP:0400005` **Short ear** rather than `HP:0008551` Microtia. A reached this via
  reviewer correction in round 1; B reached it directly, reasoning that "ears measured
  below the 10th percentile" is a size claim, not an auricular-malformation claim.
- `HP:0007370` **Aplasia/Hypoplasia of the corpus callosum** rather than the
  agenesis-only term, because the source reports "agenesis *or* hypoplasia" as one count.
- `HP:0020206` Simple ear; `HP:0100025` Overfriendliness (rather than a directionless
  "abnormal social behavior").
- Both wrote a `HUMAN_MODEL_MISMATCH` discussion — not a generic `KNOWLEDGE_GAP` —
  about the lymphoblastoid basis of every mechanistic arm.
- Both scoped strictly to `MONDO:0010590`, explicitly excluded the historical umbrella
  `MONDO:0002010`, and cited the same <3% molecular-confirmation figure to justify it.
- Both corrected macrocephaly from the historical "universal" to `FREQUENT`.
- `NCIT:C15184` Behavioral Intervention for the behavioural arm — chosen independently
  by both, over the neighbouring `NCIT:C181743` Behavioral Counseling that `CLAUDE.md`
  uses as its example of a behavioural action term.

### Frequency band agreement (uncontaminated)

**25/31 = 80.6% exact** on shared terms. But only **10** terms were banded by both
(A banded 23/47, B banded 19/48), so most of that agreement is agreement *not to
band* — itself a real signal that both curators applied the "omit rather than
fabricate" rule from `docs/frequency-evidence-guidelines.md`.

All six disagreements, with an assessment:

| Term | A | B | Assessment |
|---|---|---|---|
| `HP:0001249` Intellectual disability | `OBLIGATE` | `VERY_FREQUENT` | **A internally inconsistent** — see below |
| `HP:0000739` Anxiety | `FREQUENT` | *(none)* | **A over-banded** — see below |
| `HP:0004482` Relative macrocephaly | *(none)* | `FREQUENT` | B recovers a band A left on the table |
| `HP:0002023` Anal atresia | *(none)* | `FREQUENT` | A bands the sibling roll-up `HP:0004378` instead; equivalent |
| `HP:0000028` Cryptorchidism | *(none)* | `OCCASIONAL` | B has a source A lacks (`PMID:17574621`) |
| `HP:0000023` Inguinal hernia | *(none)* | `OCCASIONAL` | Same |

### Treatment binding (uncontaminated)

A curated 10 treatments across 10 distinct NCIT ids; B curated 8 across 7 (B binds
`NCIT:C15747` Supportive Care twice). Every one of B's 7 ids also appears in A, giving
an id-level Jaccard of **0.700**.

**That 7 is agreement about term ids, not about interventions**, and the two come
apart. Reading the names behind each shared id:

| Shared id | A | B | Same intervention? |
|---|---|---|---|
| `NCIT:C121351` | Occupational therapy | Occupational therapy | yes |
| `NCIT:C15184` | Behavioral management | Individualized behavioral management | yes |
| `NCIT:C15240` | Genetic counseling and family testing | Genetic counseling | yes |
| `NCIT:C159273` | Speech and language therapy | Speech therapy | yes |
| `NCIT:C15329` | Surgical repair of congenital anomalies | Surgical repair of imperforate anus | partial — B narrower |
| `NCIT:C15747` | Ophthalmologic and audiologic surveillance | Management of chronic constipation; Annual audiology evaluation | partial — audiology overlaps, constipation does not |
| `NCIT:C15302` | Physical therapy | Early intervention and developmental therapies | **no** — a collision |

So the honest figure is **4 of 7 shared ids pair the same intervention**, 2 partially
overlap, and 1 is a pure collision: A curates early intervention separately under
`NCIT:C159524`, so B's use of `NCIT:C15302` for it is a different judgement that
happens to land on a term A used for something else.

Four unambiguous agreements out of eight possible bindings is still a real signal —
these were free choices from a large NCIT subtree — but it is a much weaker claim than
id-level Jaccard suggests, and the gap is instructive: **a coarse action vocabulary
lets two curators agree on the term while disagreeing about the treatment.**
`NCIT:C15747` Supportive Care absorbing both bowel management and audiology
surveillance is the clearest case.

A has three ids B lacks: Early Intervention (`NCIT:C159524`), Gastrostomy
(`NCIT:C52006`), and Pharmacotherapy for bowel management (`NCIT:C15986`).

### Reference set (partly contaminated)

Jaccard **0.471**; 8 shared of 17 union.

- **Shared (8):** `17334363` `18691967` `18805826` `19938245` `20301719` `28369444` `30729724` `33925166`
- **A only (6):** `17000779` `18973276` `20507344` `20981778` `24123922` `34670449`
- **B only (3):** `17574621` `20630950` `23091001`

### Pathophysiology graph (contaminated — interpret cautiously)

Both built 9 nodes: one molecular root, three mechanistic arms, and organ-level
terminals. Three terminal nodes carry effectively identical names in both
(Failure of Corpus Callosum Formation, Anorectal Malformation, Cardiac Septation
Defect).

The topology differs: **A fans the three arms directly onto five organ terminals
(12 edges); B routes them through two convergence hubs — a neural and a non-neural —
onto three terminals (9 edges).** A's is flatter and more directly queryable; B's
makes the neural/non-neural split explicit and states where the evidence stops.
Given the contamination, this is best read as "two ways to draw the same three arms,"
not as evidence of independent convergence.

## Defects in A surfaced by the comparison

Ranked by how confident the finding is.

### 1. The SHH arm has no variant-specific citation

A's `Derepression of GLI3-Dependent Sonic Hedgehog Target Transcription` node rests
on two references, both marked `SUPPORT`:

- `PMID:17000779` (2006) — Mediator–Gli3 interaction in general, not the FGS1 allele
- `PMID:30729724` (Srivastava 2019) — patient lymphoblasts, but from patients carrying
  **N898D, R1214C, R1295H**, not p.Arg961Trp

The paper that demonstrates this mechanism *for the FGS1 allele itself* is absent:

> `PMID:23091001` (Zhou 2012, *PNAS*) — "In FG/R961W and Lujan/N1007S patient-derived
> cells, we document enhanced SHH pathway activation and GLI3-target gene induction
> coincident with impaired recruitment of CDK8 onto promoters of GLI3-target genes,
> but not non-GLI3-target genes."

B cites `23091001` as the primary support for this arm and marks `30729724` as
`PARTIAL` with the variant mismatch stated. **Recommended fix:** add `23091001`;
downgrade `30729724` to `PARTIAL`. Cached at `references_cache/PMID_23091001.md`.

### 2. `Anxiety` is banded `FREQUENT` on evidence with no denominator

A's supporting quote (`PMID:18973276`) is *"they were at increased risk for maladaptive
behavior, with a propensity towards aggression, anxiety, and inattention."* A propensity
statement carries no proportion and cannot license a 30–79% band. The cohort paper's
only statement about anxiety is that it *"is present in both groups, is less
discriminatory"* — again no denominator. **Recommended fix:** drop the band, keep the
phenotype.

### 3. Two standards for the same denominator

A bands `Intellectual disability` **`OBLIGATE`**, justified as *"every fully assessed
mutation-positive male had cognitive impairment"* (13/13). A simultaneously bands three
other 13/13/23-denominator phenotypes **`VERY_FREQUENT`**, each explaining that
*"n=13 does not license an assertion of invariance."* Same denominator, opposite
conclusions, within one entry.

A definitional argument for `OBLIGATE` does exist — Clark makes intellectual disability
an inclusion criterion, so the cohort cannot contain an unaffected male — but that is
not the reason A gives, and if accepted it should be stated as such. **Recommended fix:**
either re-band to `VERY_FREQUENT` for consistency, or keep `OBLIGATE` and replace the
rationale with the definitional/ascertainment argument.

### 4. Recoverable quantitative data left unbanded

`Relative macrocephaly` is unbanded in A, supported only by GeneReviews naming it.
Clark's sentence — *"Absolute macrocephaly … was confirmed in fewer than half of
patients (7 of 18) as was relative macrocephaly"* — applies the same fraction to both
forms, yielding `FREQUENT`. A already quotes this sentence on the *absolute*
macrocephaly phenotype, so the datum is in the entry but unused on the relative one.

⚠️ **Related trap, worth recording:** the same paper reports *"15 of 18 had
macrocephaly"* for the **Italian MED12 mutation-NEGATIVE** comparison group. That
figure must never be applied to FGS1. Neither curator fell into it, but the two
"of 18" denominators sit close together in the text.

### 5. Genitourinary frequencies are absent

`PMID:17574621` (Smith 2007, *J Urol*) systematically evaluated 228 FG syndrome
patients: cryptorchidism 24%, hypospadias 14%, hernia/hydrocele 13%. A cites the
cohort paper's undifferentiated "were frequent" list and bands nothing; B adds
`OCCASIONAL` bands **marked `supports: PARTIAL`**, because the series predates routine
MED12 testing and is therefore drawn from the clinical population of which <3% is
molecularly confirmed. Cached at `references_cache/PMID_17574621.md`.

### 6. Phenotypes present in only one entry

**A has, B lacks** (genuine gaps in B — mostly behavioral depth): aggression,
compulsivity, impulsivity, hyperactivity, short attention span, sleep disturbance,
prominent fingertip pads, short stature, vertebral anomaly, delayed speech.

**B has, A lacks:** hypospadias, megacolon, gastroesophageal reflux, atrial septal
defect, dolichocephaly, open mouth, low-set ears, protruding ears, and a banded
limited forearm supination (6/23 = `OCCASIONAL`).

### 7. Missing evidence for "altered function, not loss of function"

A asserts that p.Arg961Trp is pathway-selective altered function rather than null.
`PMID:20630950` (Rocha 2010, *Development*) — Med12 hypomorphs are embryonic-lethal by
E10 with neural tube, somitogenesis and heart defects — turns that assertion into an
argument by contrast. Absent from A; B cites it as `MODEL_ORGANISM` / `PARTIAL`.
Cached at `references_cache/PMID_20630950.md`.

## Process findings

**A hallucination trap that no validator catches.** `PMID:21391746` (Neri 2011) is
titled *"The FG syndrome from a pathological perspective"* and surfaces high in any
FG syndrome search. Its abstract states: *"The propositus' phenotype did not suggest
involvement of the MED12 gene."* Quoting it for an FGS1 phenotype would pass snippet
validation, PMID validation, and term validation — it is a real paper, real quote,
real terms — while being about a MED12-negative patient. This is the Named Entity
Confusion failure mode at the level of an individual citation rather than a whole
report. B fetched it, read it, and deliberately did not cite it. It is cached
(`references_cache/PMID_21391746.md`) so the next curator meets the same decision.

**A documentation/schema contradiction (now fixed).** Following `CLAUDE.md` literally,
B bound seven MAXO treatment terms; all seven failed term validation, because
`TreatmentActionTerm` is `reachable_from NCIT:C25218` — NCIT only. At the time,
`CLAUDE.md` documented MAXO as a supported vocabulary with a worked example while the
schema rejected it. MAXO has since been excised from the repo; the guidance now reads
NCIT-only. Recorded because it shows that curation-guide drift produces confident,
schema-invalid output — a trap for any agent that trusts the guide over the schema.
B's independent NCIT remappings matched the official migration table exactly for
physical, speech, and occupational therapy.

**Cache churn as a side effect of QC.** Running `just check-reference-cache-frontmatter`
rewrote **7,613** `references_cache/*.md` files in the working tree — a cosmetic YAML
quoting change (`reference_id: DOI:… ` → `reference_id: "DOI:…"`) introduced by the
local validator version. Any curator running a cache-touching recipe and then
`git add -A` would commit all of it. This is the same churn PR #7254 excluded by hand.
It survives the MAXO removal and is unrelated to it.

## Conclusions

1. **Agreement is high where the evidence is quantitative and low where it is prose.**
   Both curators independently found the same denominators in Clark 2009 and assigned
   the same bands from them. Divergence concentrated exactly where the source says
   "were frequent" without a count — and there, both mostly declined to band.

2. **Strict term-identity Jaccard is the wrong metric for this KB.** It scored 0.484
   where subsumption-aware agreement was 0.77–0.81. Any future IAA measurement on
   dismech should compute agreement over the ontology, not over term strings.

3. **The residual disagreement is dominated by roll-up-vs-split strategy**, not by
   disagreement about what is true. Neither curator asserted anything the other
   contradicted; the differences are granularity, coverage, and how aggressively to
   band. Zero factual conflicts across 47 vs 48 phenotypes is the strongest single
   result here.

4. **A second pass finds real defects even after three review rounds and an approval.**
   Items 1 and 2 are defects by the project's own evidence rules, not preferences, and
   both survived `ai4c-reviewer`. The generalisable point: reviewers check whether a
   snippet supports its claim, but are less likely to notice that a *better and more
   specific* source exists and was not cited. Independent re-curation catches that
   class; review does not.

5. **The bottleneck is source selection, not extraction.** Both curators extracted
   near-identically from shared papers. Almost all substantive divergence traces to
   *which papers were found* — B's three unique references produced items 1, 5, and 7.
   That argues for pooling multiple deep-research runs before curating rather than
   curating harder from one.

## Suggested follow-up

Items 1 and 2 are defects and should be fixed in `kb/disorders/FG_Syndrome_1.yaml`.
Items 3–7 are improvements. All four supporting references are already cached on
branch `claude/curate-fg-syndrome-1-wumqiu` (commit `c955f4d57`), so the fix needs no
new fetches.

Worth considering for the wider KB:
- Add subsumption-aware agreement to any future IAA measurement (`compare.py` is reusable).
- Consider whether `frequency:` on a roll-up phenotype (`Abnormality of the eye`) is
  meaningful when the constituent findings have separate denominators.
- Investigate the 7,613-file cache churn independently of curation work.
