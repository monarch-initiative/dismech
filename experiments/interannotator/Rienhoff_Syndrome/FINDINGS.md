# Inter-annotator consistency: Rienhoff syndrome (MONDO:0014262)

Two independent curations of the same disease entry, compared to estimate how much
of a dismech entry is determined by the evidence and how much by the curator.

| | |
|---|---|
| **Disease** | Rienhoff syndrome / Loeys-Dietz syndrome type 5 (LDS5), `MONDO:0014262`, `TGFB3` |
| **Curator A** | Melissa Haendel, [PR #7345](https://github.com/monarch-initiative/dismech/pull/7345). Snapshot is the **post-#7228 NCIT form** of the merged entry at commit `0729e8e5b6` (byte-identical). |
| **Curator B** | Closed [PR #7322](https://github.com/monarch-initiative/dismech/pull/7322) tip `6059cda782` (Chris Mungall / Cursor agent curation). Never merged into `kb/`. Metrics use a mechanical MAXO→NCIT remap of that tip; the MAXO-era original is preserved alongside. |
| **Date** | 2026-08-08 |
| **Both agents** | Independent same-day curations (2026-07-31), not a planned IAA experiment |

## Files

| Path | Contents |
|---|---|
| `Rienhoff_Syndrome.curator-A.merged-pr7345-post7228.yaml` | A, verbatim at `0729e8e5b6` (merged #7345 after the #7228 MAXO→NCIT remap) |
| `Rienhoff_Syndrome.curator-B.closed-pr7322.maxo-original.yaml` | B tip `6059cda782`, verbatim (MAXO treatment/diagnosis terms) |
| `Rienhoff_Syndrome.curator-B.closed-pr7322.yaml` | B after mechanical MAXO→NCIT remap (`scripts/migrate_maxo_to_ncit.py` / `docs/superpowers/maxo_ncit_final_map.tsv`); zero MAXO ids remain. Remaps: `MAXO:0000004`→`NCIT:C15329`, `MAXO:0000077`→`NCIT:C181743`, `MAXO:0000079`→`NCIT:C15240`, `MAXO:0000127`→`NCIT:C15709`, `MAXO:0000186`→`NCIT:C15986`, `MAXO:0000950`→`NCIT:C15747` |
| `metrics.txt` | `compare.py` output, as run (ontology/subsumption on) |
| `../compare.py` | The metric script — regenerates every number below |

```bash
uv run python experiments/interannotator/compare.py \
  experiments/interannotator/Rienhoff_Syndrome/Rienhoff_Syndrome.curator-A.merged-pr7345-post7228.yaml \
  experiments/interannotator/Rienhoff_Syndrome/Rienhoff_Syndrome.curator-B.closed-pr7322.yaml
```

**Both files are frozen snapshots, not live entries.** A was byte-identical to
`kb/disorders/Rienhoff_Syndrome.yaml` at `0729e8e5b6`; the live entry has since
diverged (ISDS classification only at the time of this study). B was never merged.
Neither snapshot is covered by `tests/test_data.py`, which globs `kb/disorders/*.yaml`
only. This study does **not** enhance the live KB entry.

## Protocol, and how far it actually held

This was not a planned dual-curation experiment. Two PRs for the same disease landed
on the same calendar day:

| Event | UTC |
|---|---|
| #7322 opened (B) | 2026-07-31 05:48Z |
| #7345 opened (A) | 2026-07-31 13:43Z |
| #7345 merged | 2026-07-31 15:09Z |
| #7322 closed | 2026-07-31 20:28Z |

There is no evidence either curator opened the other's YAML before finishing. Timeline
and authorship argue for **near-complete independence** — stronger than the FG syndrome 1
study, where curator B had read A's PR description before starting.

**Shared scaffolding still exists and must be scored honestly.**

1. **GeneReviews baseline.** Both cite `PMID:20301312` (GeneReviews for TGFB3-related
   Loeys-Dietz / Rienhoff). Phenotype lists and management recommendations are partly
   anchored on that shared review, not pure curator invention.
2. **Shared mechanism module.** Both independently declared `conforms_to` edges into
   `aortopathy_tgfbeta_dysregulation` (A: four nodes including the signaling node named
   "Altered TGF-beta Signal Transduction"; B: four nodes including
   "TGF-beta Signaling Dysregulation"). The aortopathy arm of the pathograph is therefore
   **partly scaffolded by the module**, not a free graph-drawing exercise. Mechanism-graph
   metrics below are reported for completeness but should not be read as pure independent
   convergence.
3. **Ontology-era mismatch.** B was curated pre-#7228 with MAXO treatment/diagnosis terms;
   A is post-#7228 NCIT. For id-level treatment comparison we mechanically remapped B with
   the project's migration map and **kept** the maxo-original snapshot. Treatment id-level
   Jaccard is only meaningful on the remapped B; content-level comparison of intervention
   names still applies.

| Dimension | Contaminated? | Trust the number? |
|---|---|---|
| Pathophysiology node structure | **Partly** — both conform to `aortopathy_tgfbeta_dysregulation` | Weakly (module-scaffolded arm) |
| Reference set | **Partly** — shared GeneReviews `PMID:20301312`; otherwise independent | Moderately |
| Phenotype terms | No — no evidence either saw the other's list | **Yes** |
| Frequency bands | No | **Yes** |
| Treatment *content* | No — interventions chosen independently | **Yes** |
| Treatment *id* Jaccard | **Era-adjusted** — B remapped MAXO→NCIT for metrics | Yes for remapped ids; see content caveat |

So the uncontaminated dimensions (phenotypes, bands, treatment content) carry the
result. Pathograph convergence is real but not a clean test of free curator invention.

## Results

Quoted from `metrics.txt` as regenerated 2026-08-08 (ontology/subsumption enabled).

### Section cardinality

| Section | A | B |
|---|---:|---:|
| phenotypes | 25 | 24 |
| pathophysiology nodes | 8 | 7 |
| causal edges | 7 | 6 |
| treatments | 8 | 10 |
| diagnosis | 0 | 1 |
| differential_diagnoses | 5 | 3 |
| discussions | 4 | 2 |
| genetic / prevalence | 1 / 1 | 1 / 1 |
| inheritance | 2 | 1 |
| progression | 3 | 0 |
| histopathology | 1 | 0 |
| evidence snippets | 100 | 83 |
| distinct PMIDs (compare.py) | 10 | 14 |

Two same-day independent curations produced entries of similar shape (~25 phenotypes,
~7–8 pathophysiology nodes, ~8–10 treatments) without coordinating.

### Phenotype agreement (uncontaminated)

- **Strict HPO term identity:** Jaccard **0.531**, Dice/F1 **0.694** (17 shared of 32 union)
- **Subsumption-aware concept coverage:** A **84.0%** (21/25), B **83.3%** (20/24)

Strict identity again understates agreement. Parent/child / roll-up pairs reported by
`compare.py`:

| A | B | Relationship |
|---|---|---|
| `HP:0001633` Abnormal mitral valve morphology | `HP:0001634` Mitral valve prolapse | A broader |
| `HP:0002616` Aortic root aneurysm | `HP:0002617` Vascular dilatation | B broader |
| `HP:0002616` Aortic root aneurysm | `HP:0004942` Aortic aneurysm | B broader |
| `HP:0005112` Abdominal aortic aneurysm | `HP:0002617` Vascular dilatation | B broader |
| `HP:0005112` Abdominal aortic aneurysm | `HP:0004942` Aortic aneurysm | B broader |
| `HP:0012727` Thoracic aortic aneurysm | `HP:0002617` Vascular dilatation | B broader |
| `HP:0012727` Thoracic aortic aneurysm | `HP:0004942` Aortic aneurysm | B broader |

**Strategy difference, not factual conflict:** A splits the aortic phenotype space into
thoracic / abdominal / root aneurysm terms; B uses a broader `Aortic aneurysm` plus a
separate `Vascular dilatation` for extra-aortic arterial aneurysm. Both map the same
clinical territory at different granularity.

**True A-only (no counterpart):** `HP:0000218` High palate; `HP:0000766` Abnormal sternum
morphology; `HP:0001270` Motor delay; `HP:0001510` Growth delay.

**True B-only (no counterpart):** `HP:0000974` Hyperextensible skin; `HP:0001324` Muscle
weakness; `HP:0001508` Failure to thrive; `HP:0005116` Arterial tortuosity.

### Frequency band agreement (uncontaminated)

**14/17 = 0.824 exact** on shared terms (including both-unbanded). **Both assigned a band
on 0 shared terms** — A banded 6/25, B banded 5/24 — so most of the "agreement" is
agreement *not to band*, again consistent with the "omit rather than fabricate" rule.

Three band disagreements:

| Term | A | B | Assessment |
|---|---|---|---|
| `HP:0001166` Arachnodactyly | `FREQUENT` | *(none)* | Divergent banding aggressiveness on shared qualitative literature |
| `HP:0001382` Joint hypermobility | `FREQUENT` | *(none)* | Same |
| `HP:0002647` Aortic dissection | *(none)* | `OCCASIONAL` | B recovers a band A left unbanded |

### Treatment binding (era-adjusted ids; content still needs reading)

After remapping B to NCIT: A has 8 treatments / **5** distinct ids; B has 10 / **5**
distinct ids; **4 shared**, id-level Jaccard **0.667**.

Shared ids and the interventions behind them:

| Shared id | A | B | Same intervention? |
|---|---|---|---|
| `NCIT:C15240` | Genetic Counseling | Cascade Genetic Testing of At-Risk Relatives | yes (cascade focus in B) |
| `NCIT:C15329` | Prophylactic Aortic Surgery | Prophylactic Aortic Surgery; Peripheral Arterial Aneurysm Repair; Cervical Spine Management; Cleft Palate Repair | partial — surgery catch-all absorbs four B procedures |
| `NCIT:C15747` | Arterial-Tree Imaging Surveillance; Activity Restriction…; Pregnancy… Surveillance | Cardiovascular Surveillance Imaging; Pregnancy Management | partial — surveillance/pregnancy overlap; A also puts activity restriction here |
| `NCIT:C15986` | Beta-Adrenergic Blocker; ARB | Beta-Blocker; ARB | yes |

A-only id: `NCIT:C15302` Physical and Occupational Therapy.
B-only id: `NCIT:C181743` Activity and Agent Restrictions (A had folded activity
restriction into Supportive Care).

**Same FG warning applies:** catch-all `NCIT:C15747` Supportive Care, `NCIT:C15986`
Pharmacotherapy, and `NCIT:C15329` Surgical Procedure absorb different interventions
under one id. Id-level Jaccard **overstates** content agreement; the honest signal is
that both curators independently chose beta-blocker + ARB pharmacotherapy, prophylactic
aortic surgery, imaging surveillance, pregnancy management, and genetic counseling /
cascade testing.

### Reference set (partly scaffolded by GeneReviews)

Jaccard **0.412**; 7 shared of 17 union.

- **Shared (7):** `20301312` `23824657` `25835445` `26184463` `31898322` `32022420` `7493021`
- **A only (3):** `15639475` `29392890` `32603777`
- **B only (7):** `34549088` `36356561` `37719708` `39450604` `39653386` `40533122` `7493022`

**B-only modern cohorts / models** (the main reference-set story):

| PMID | Role (approx.) |
|---|---|
| `39653386` | Montalcino 2025 cohort |
| `37719708` | Belgian founder |
| `39450604` / `40533122` | Extra-aortic arterial phenotype |
| `34549088` | Carotid |
| `36356561` | iPSC model |
| `7493022` | Second mouse paper (alongside shared `7493021`) |

A's unique set is smaller and older (`15639475`, `29392890`, `32603777`). As in FG,
**source selection** drives much of the residual divergence: B's modern-cohort PMIDs
support extra-aortic aneurysm / tortuosity phenotype depth that A lacks as named terms.

### Pathophysiology graph (partly module-scaffolded — interpret cautiously)

Both build a TGFB3-ligand root → signaling dysregulation → aortic medial degeneration →
dilation/aneurysm → dissection/rupture chain, and both attach palatal / hypomyoplasia
side branches. Terminal aortopathy node names are nearly identical because both
`conforms_to` the same module nodes.

Differences that are still curator choices:

- A inserts an explicit `Impaired Mesenchymal Development` cellular hub (2 outgoing
  edges) between signaling and the developmental terminals; B fans the ligand-deficiency
  node directly (3 outgoing edges) onto signaling, palatogenesis, and myogenesis.
- Naming: A's "TGFB3 Ligand Variant" / "Altered TGF-beta Signal Transduction" vs B's
  "TGFB3 Ligand Deficiency" / "TGF-beta Signaling Dysregulation" (B's signaling node
  name matches the module node label exactly).
- Biological-scale tags differ on some shared-named terminals (A marks aneurysm /
  dissection nodes `ORGANISM`; B marks them `TISSUE`).

Given the shared module, this is best read as "two ways to specialize the same
aortopathy chain," not as proof of free graph convergence.

### Discussions — same open question, different framing

| Curator | Kinds | Framing |
|---|---|---|
| A | `CONTROVERSY` + 2× `KNOWLEDGE_GAP` + `HUMAN_MODEL_MISMATCH` | CONTROVERSY on how one gene yields reduced-signaling vs paradoxically increased aortic TGF-beta signaling; gaps on lifetime aortic risk and which gene-agnostic LDS features apply; mouse null vs human heterozygote mismatch |
| B | `KNOWLEDGE_GAP` + `HUMAN_MODEL_MISMATCH` | Gap on LoF vs GoF (including RKKR furin-motif alleles); mouse model fails to reproduce adult-onset incompletely penetrant aortopathy |

Both surface the **signaling-direction / LoF-vs-GoF** problem and the **mouse aortopathy
gap**. A packages the signaling question as `CONTROVERSY` plus separate lifetime-risk and
feature-scope gaps; B collapses the molecular question into one `KNOWLEDGE_GAP` and
centers the mouse mismatch on adult-onset aortopathy specifically. Similar scientific
question, different schema framing — a difference, not a defect.

## Defects

Ranked by how confidently they are defects under project rules (as opposed to taste).
This study does **not** patch the live KB; items are recorded for follow-up.

### 1. Frequency bands without a shared quantitative anchor

On the three shared terms where bands disagree, neither entry's banding is backed by a
denominator both curators extracted. A's `FREQUENT` on arachnodactyly and joint
hypermobility, and B's `OCCASIONAL` on aortic dissection, sit in the qualitative-prose
zone the frequency SOP warns about. **Follow-up:** re-check each band against the cited
snippet; drop bands that lack a count or an explicit qualitative→enum mapping.

### 2. Aortic phenotype granularity without a stated strategy

A's split (thoracic / abdominal / root) vs B's roll-up (`Aortic aneurysm` +
`Vascular dilatation`) is defensible either way, but leaving both strategies in the KB
without a convention makes cross-disease query brittle. Not a snippet defect — a
governance gap. **Follow-up:** prefer the more specific site terms when the source
supports them; keep a broader term only when the source does not localize.

### 3. Coverage gaps that are really missing phenotypes

True one-sided phenotypes that the other curator *and* the shared literature support
are closer to defects than to taste: B's `Arterial tortuosity` and extra-aortic
`Vascular dilatation` are backed by B-only modern cohorts A never cited; A's
`High palate` / sternum-morphology roll-up are GeneReviews-adjacent findings B omitted
as named terms (B has `Pectus excavatum` but not the broader sternum term). **Follow-up
for the live entry:** consider merging the stronger coverage from each side — without
turning this IAA PR into a KB enhancement.

## Differences

Defensible curator choices that are not rule violations.

1. **Aortic term strategy** — site-split (A) vs aneurysm + extra-aortic dilatation (B).
2. **Mitral valve** — morphology roll-up (A) vs prolapse (B).
3. **Pathograph topology** — mesenchymal hub (A) vs direct fan-out from ligand node (B);
   both specialize the same module chain.
4. **Discussion packaging** — `CONTROVERSY` vs `KNOWLEDGE_GAP` for the signaling-direction
   question; A adds lifetime-risk and LDS-feature-scope gaps B does not.
5. **Section completeness** — A has progression + histopathology; B has a diagnosis
   section and more treatment rows (surgical splits).
6. **Activity restriction binding** — A under `NCIT:C15747` Supportive Care; B under
   `NCIT:C181743` Behavioral Counseling after remap (was `MAXO:0000077`).
7. **Reference portfolio** — A thinner/older unique set; B heavier on 2021–2025 cohorts
   and a second mouse paper.

## Process findings

**Accidental dual curation is a strong natural experiment.** Unlike FG (where B was
commissioned and had read A's PR blurb), Rienhoff's two PRs crossed in flight on the
same day with no planned IAA protocol. Independence is correspondingly higher; the
main non-independence is *institutional* (shared GeneReviews + shared module), not
*social* (curator cross-reading).

**Ontology-era mismatch is a new IAA hazard.** Measuring treatment Jaccard on raw A vs
raw B would have been nonsense (NCIT vs MAXO). Keeping the maxo-original snapshot and
reporting metrics on a mechanical remap is the right pattern when a vocabulary
migration lands between two curations. Content-level reading remains mandatory because
the remap preserves ids, not intervention identity under catch-alls.

**Shared modules inflate pathograph agreement.** Both curators' aortopathy terminals
match because `conforms_to` copies module node names. Future IAA studies on
module-conformant diseases should score the module-scaffolded arm separately from
disease-specific nodes (here: ligand naming, mesenchymal hub, palatogenesis /
myogenesis branches).

## Conclusions

1. **Phenotype agreement is high once subsumption is allowed** (strict Jaccard 0.531 →
   concept coverage ~0.83–0.84). Residual disagreement is mostly aortic granularity and
   a handful of true one-sided terms.
2. **Band agreement is mostly agreement not to band** (0/17 shared terms banded by
   both). The three disagreements sit where the literature is qualitative.
3. **Treatment id Jaccard (0.667) again overstates content agreement** because
   Supportive Care / Pharmacotherapy / Surgical Procedure catch-alls absorb multiple
   interventions — same lesson as FG.
4. **Reference divergence is the largest substantive gap**, and it is asymmetric: B
   brings modern cohorts that justify extra-aortic phenotype depth A lacks.
5. **Independence was better than FG**, but pathograph metrics are still partly
   module-scaffolded and must be discounted accordingly.

## Suggested follow-up

- Optionally enrich the live `kb/disorders/Rienhoff_Syndrome.yaml` from B's modern
  cohorts and extra-aortic phenotypes — **in a separate PR**, not this study.
- When running IAA across a MAXO/NCIT (or similar) boundary, always keep the original
  snapshot and remap mechanically for id metrics.
- Consider scoring module-conforming pathograph nodes separately in `compare.py`.
