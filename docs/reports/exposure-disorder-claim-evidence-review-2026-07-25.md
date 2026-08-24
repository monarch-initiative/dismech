# Claim–Evidence Review: 10 Exposure-Related Disorders (2026-07-25)

## Scope

Correctness review of ten exposure/toxicology entries in `kb/disorders/`, with the
review lens set on **claim–evidence matching**: does each cited snippet actually
support the claim it is attached to, is the `supports`/`evidence_source` tagging
right, and are there claims asserted with no evidence at all?

Entries reviewed (three exposure families):

| Family | Entries |
|---|---|
| Heavy metals | `Arsenic_Poisoning`, `Lead_Poisoning`, `Mercury_Poisoning`, `Cadmium_Poisoning`, `Thallium_Poisoning` |
| Gases / chemicals | `Carbon_Monoxide_Poisoning`, `Methanol_Poisoning`, `Organophosphate_Poisoning` |
| Pneumoconioses | `Silicosis`, `Asbestosis` |

## Method

1. **Schema validation** — `linkml-validate` against the `Disease` class, all 10 files.
2. **Snippet fidelity** — every evidence item's `snippet` normalized (whitespace,
   Unicode dashes/quotes, case) and checked as an exact substring of the
   corresponding `references_cache/` body. 578 evidence items across all
   reference types (PMID, DOI, GEO, clinicaltrials).
3. **Semantic claim–evidence pass** — manual read of all 578
   `(claim, description, snippet, supports, evidence_source, explanation)` tuples,
   judging whether the snippet supports the specific proposition asserted.
4. **Coverage pass** — enumeration of top-level items in evidence-bearing sections
   carrying no `evidence` block; audit of every `frequency:` band against its
   snippets.

## Mechanical results: clean

- **Schema:** 10/10 `No issues found`.
- **Snippet fidelity:** **578/578 snippets are exact substrings of their cited
  cached source.** Zero fabricated or paraphrased quotes, zero missing cache
  entries, including the 14 DOI-keyed deep-research references. No evidence of the
  classic hallucination modes (invented PMIDs, invented quotes).

The anti-hallucination stack is doing its job on these entries. Every finding below
is a **semantic** issue that snippet-substring validation cannot catch.

## Overall assessment

| Entry | Claim–evidence quality | Notes |
|---|---|---|
| `Arsenic_Poisoning` | **Excellent** | Best in the set. Descriptions explicitly bound their own claims ("does not justify a universal sulfhydryl-enzyme blockade model", "cross-sectional associations do not by themselves establish fibrosis"). Same paper correctly split into `MODEL_ORGANISM` and `IN_VITRO` items by evidence type. Carries a `REFUTE`-flavored discussion citing the negative DMSA RCT. |
| `Methanol_Poisoning` | **Excellent** | Tight mechanistic chain, each step its own citation. No unevidenced items except one biochemical readout. |
| `Carbon_Monoxide_Poisoning` | **Very good** | Honest hedging where the snippet supports the consequence rather than the mechanism; `discussions` carries the *negative* HBO trial as `supports: REFUTE`. |
| `Thallium_Poisoning` | **Very good** | Minor review-vs-clinical tagging issue; one missing `explanation`. |
| `Organophosphate_Poisoning` | **Very good** | One poor snippet choice (below). |
| `Asbestosis` | **Good** | Exemplary handling of *conflicting* evidence (GSTM1: `SUPPORT` and `REFUTE` side by side). Two core mechanism nodes unevidenced. |
| `Silicosis` | **Good** | Explicitly annotates review-derived evidence as `OTHER` in `explanation` text. 9 unevidenced items including all three subtypes. |
| `Lead_Poisoning` | **Mixed** | Broad, well-cited backbone, but repeated use of generic background sentences to carry specific clinical claims; frequency bands largely unsupported. |
| `Cadmium_Poisoning` | **Weakest** | Most claim–evidence mismatches; systematic `evidence_source` misclassification; unevidenced quantitative thresholds; an unevidenced clinical contraindication; one questionable source. |
| `Mercury_Poisoning` | **Thinnest** | 9 evidence items from 3 unique references; declared scope not delivered; an unevidenced negative epidemiological claim. |

---

## Findings

### 1. Unevidenced clinical contraindication — `Cadmium_Poisoning`

`treatments[Chelation Therapy].description` (`kb/disorders/Cadmium_Poisoning.yaml:1042`):

> "BAL (dimercaprol) **is contraindicated** as it may increase renal cadmium uptake."

This is an actionable, directive clinical claim. Neither attached evidence item
mentions dimercaprol or renal redistribution — one covers chelating agents
generically, the other covers long-term chelation toxicity. The claim is
well-established in the toxicology literature, so it is sourceable; it just is not
sourced here. **Highest-priority fix in the set**, because an unsourced
contraindication is the kind of claim a reader will act on.

### 2. Mechanism claims resting on clinical-observation evidence — `Cadmium_Poisoning`

`pathophysiology[Direct Osteoblast Toxicity]` (`:403`) asserts four mechanistic
propositions: cadmium directly inhibits osteoblast differentiation, does so
**independently of the renal phosphate wasting pathway**, inhibits alkaline
phosphatase, and promotes osteoclast-mediated resorption. The sole evidence is a
case report snippet: *"We will present a case of cadmium induced peripheral
neuropathy, nephropathy, and decreased bone density."*

A single case of decreased bone density in a patient who also had nephropathy
cannot establish direct osteoblast toxicity, and specifically cannot establish
*independence from the renal pathway* — the case has renal disease. The node also
carries `biological_processes: osteoblast differentiation / DECREASED` (`GO:0001649`),
a structured assertion with no in-vitro or animal osteoblast evidence behind it.
Tagged `supports: SUPPORT`; should be `PARTIAL` at most, and the node needs
cell-level evidence.

### 3. Histopathology nodes evidenced by non-histopathological sources — `Cadmium_Poisoning`

Three of five `histopathology` nodes assert specific microscopic findings that
none of their snippets document:

- **Diffuse Alveolar Damage** — claims hyaline membrane formation, alveolar edema,
  type II pneumocyte hyperplasia. Snippets: *"multiple organ damage was observed,
  involving brain, lung, liver, kidney…"* and a generic intro sentence
  (*"cadmium is more commonly known to cause acute lung injury"*). Neither
  describes lung histology.
- **Renal Tubulointerstitial Disease and Fibrosis** — the first snippet is again
  the generic "multiple organ damage" line. (A second citation does support the
  claim.)
- **Hepatocellular Degeneration** — claims degeneration and necrosis; the snippets
  document cadmium *accumulation* in liver, plus a NHANES epidemiological
  finding of hepatic fibrosis. Citing a cross-sectional biomarker study as
  histopathology evidence is a category error.

### 4. Unevidenced quantitative specifics carried in `description` fields — `Cadmium_Poisoning`

Descriptions assert precise numbers no snippet supports:

| Claim | Location | Snippet actually says |
|---|---|---|
| "Inhaled cadmium has 25-50% bioavailability; oral absorption 3-8%" | `pathophysiology[0]` | "long biological half-life" |
| "renal cortex concentrations above 200 mcg/g" | `pathophysiology[3]` | nothing quantitative |
| "Cd-MT… small molecular weight (~7 kDa)" | `pathophysiology[2]` | nothing quantitative |
| "Normal levels typically below 5 mcg/L; above 50 mcg/L indicate significant toxicity" | `diagnosis[0]` | a generic list of diagnostic modalities |
| "a single cigarette may contain 1-2 mcg cadmium; smokers have levels 4-5× non-smokers" | `environmental[2]` | "Common risk factors include smoking and alcohol consumption" |

The last two matter most: a diagnostic threshold and an exposure magnitude are
exactly the numbers a reader would reuse.

### 5. Systematic `evidence_source` misclassification — `Cadmium_Poisoning`, `Thallium_Poisoning`

Per CLAUDE.md, `evidence_source` classifies the *cited publication's* study type.
Several mechanistic reviews and in-vitro/analytical papers are tagged
`HUMAN_CLINICAL`:

| Reference | What it is | Tagged | Should be |
|---|---|---|---|
| `PMID:20204475` (*Biometals*) | review of cadmium transport in mammalian cells | `HUMAN_CLINICAL` | `IN_VITRO` / `OTHER` |
| `PMID:20354761` (*Biometals*) | review, cadmium and the kidney | `HUMAN_CLINICAL` | `OTHER` |
| `PMID:19106433` (*Indian J Med Res*) | review, nephrotoxicity of Cd & Pb | `HUMAN_CLINICAL` | `OTHER` |
| `PMID:31704329` (*Ecotox Environ Saf*) | analytical identification of Cd-binding proteins in plasma | `HUMAN_CLINICAL` | `IN_VITRO` |
| `PMID:41453694` (*Toxicol Lett*) | review, heavy-metal neurotoxicity | `HUMAN_CLINICAL` | `OTHER` |
| `PMID:14579545` (*Toxicol Rev*) | review, thallium + Prussian blue | `HUMAN_CLINICAL` (all ~30 uses) | `OTHER` |

Note the contrast: `Silicosis` and `Asbestosis` get this right and even annotate it
in prose ("Evidence source OTHER as this is a review article"), and `Arsenic_Poisoning`
correctly splits one paper's animal and enzyme data into separate items. The fix
is mechanical and the house style already exists.

### 6. Questionable source underpinning a diagnostic recommendation — `Cadmium_Poisoning`

`biochemical[Urinary Cadmium Level]` and `diagnosis[Urine Cadmium Level]` both rest
on `PMID:19364190`, *"The benefits of pre- and post-challenge urine heavy metal
testing: Part 1"*, published in **Alternative Medicine Review**, quoted as:
*"Conducting pre-flush testing is also currently the clinician's only means of
identifying cadmium toxicity."*

Two problems. The source is not a mainstream clinical-toxicology venue, and
provoked/post-challenge urine metal testing is specifically discouraged by
mainstream toxicology practice. The `diagnosis` node's description propagates this
("Post-chelation challenge testing reflects total body stores and helps guide
treatment decisions"). The underlying point — that unstimulated urinary cadmium
indexes body burden — is uncontroversial and better sourced elsewhere in the same
file; the challenge-testing framing should go.

### 7. Snippet whose sentence points the other way — `Organophosphate_Poisoning`

`phenotypes[Miosis]` (`:454`) asserts miosis as "a classic sign of cholinergic
toxicity", tagged `supports: SUPPORT`. The snippet:

> "The classic muscarinic and nicotinic signs of intoxication including increased
> secretions, bradycardia, fasciculations, and miosis **were less common in our
> patient population**."

The sentence names miosis among classic signs but its assertion is a *negative*
finding for that cohort. Using it as unqualified `SUPPORT` for a phenotype claim
inverts the source's point; a better snippet exists in the same corpus
(`PMID:32626615` lists miosis among OP poisoning signs and is already cited for
bradycardia and fasciculations).

### 8. Description asserts a nerve-fiber pattern its evidence contradicts — `Lead_Poisoning`

`phenotypes[Peripheral neuropathy]` (`:636`) — "Lead neuropathy is classically
**motor-predominant** and may present with wrist drop or radial palsy":

- Evidence 1 (`PMID:17405745`) describes a **"sensitive polyneuropathy to the four
  limbs"** — a *sensory* neuropathy, i.e. the opposite pattern.
- Evidence 2 (`PMID:20142857`) is the right paper (radial neuropathy from
  occupational lead exposure, five patients) but the chosen snippet is the
  content-free *"Neuropathy is one complication of lead poisoning."*

The motor-predominance and wrist-drop claims are correct and the second paper
supports them — the snippet just needs to be re-drawn from that abstract.

### 9. Generic background sentences carrying specific clinical claims — `Lead_Poisoning`

`PMID:37478813` is a laboratory ICP-MS methods/trends study. Its introductory
sentence — *"Exposure to lead may cause severe adverse effects such as anemia,
neurologic damage, developmental disorders, and reproductive disorders"* — is used
as `HUMAN_CLINICAL` evidence for both `phenotypes[Anemia]` and
`phenotypes[Developmental delay]`. Likewise `PMID:40981357`'s single sentence about
contamination sources ("mining activities, battery manufacturing, electronic waste
recycling…") is reused verbatim for three separate `environmental` nodes. Not
false, but a review's throwaway framing sentence is thin support for a curated
phenotype, and better primary sources are already in the file.

### 10. Frequency bands mostly unsupported — 4 entries

Per `docs/frequency-evidence-guidelines.md`, a `frequency:` value is a separate
quantitative claim needing its own evidence. Audit of all 36 bands in the four
entries that use them:

| Entry | Bands | Bands whose snippets contain no quantitative or explicit qualitative frequency statement |
|---|---|---|
| `Cadmium_Poisoning` | 9 | **8** |
| `Lead_Poisoning` | 12 | **9** |
| `Carbon_Monoxide_Poisoning` | 10 | **5** |
| `Thallium_Poisoning` | 5 | **2** |
| **Total** | **36** | **24 (67%)** |

Worst cases are `VERY_FREQUENT` (schema: *80-99% of patients*) claims in
`Cadmium_Poisoning` supported only by single case reports —
`Renal Tubular Dysfunction` and `Low-Molecular-Weight Proteinuria` are cited to a
one-patient itai-itai report and a one-patient Fanconi report. The domain claim is
right (LMW proteinuria is near-universal in chronic cadmium nephropathy); the
citation cannot carry the band. Per the guidelines, omit the band or cite a
prevalence figure.

The other five entries use no `frequency:` values at all, which is the compliant
choice when a quantitative source is not at hand.

### 11. Declared scope not delivered; unevidenced negative claim — `Mercury_Poisoning`

The entry is the thinnest in the set: 228 lines, 9 evidence items, **3 unique
references**, and only `pathophysiology`, `environmental`, and `phenotypes`
sections — no `treatments`, `diagnosis`, `biochemical`, `histopathology`,
`prevalence`, or `genetic`. The absence of `treatments` is conspicuous for a metal
poisoning where chelation is a standard intervention.

Two specific claim–evidence problems:

- **Scope mismatch.** The `description` commits to "elemental, inorganic, or
  organic forms, each with a distinct clinical profile" and asserts that
  "inorganic and elemental mercury, by contrast, classically cause peripheral
  neuropathy and the neuropsychiatric syndrome of erethism." The pathograph,
  phenotypes, and environmental sections model **only** the methylmercury /
  Minamata arm. The inorganic arm appears solely as one passing snippet about the
  felt-hat industry. Either the entry should be scoped to methylmercury poisoning
  or the inorganic arm needs curating.
- **Unevidenced negative claim.** "Unlike lead, mercury exposure from dietary fish
  or dental amalgam **has not been associated with** amyotrophic lateral
  sclerosis" appears twice (`:31`, `:137`) with zero supporting citations anywhere
  in the file. A negative epidemiological claim needs a source as much as a
  positive one.

Also, `pathophysiology[0]` asserts three converging molecular mechanisms
(glutathione/NPSH depletion, calcium dyshomeostasis, NMDA-receptor excitotoxicity)
on the strength of one in-vitro rat-cortical-neuron memantine study; the
`explanation` acknowledges this ("the same study implicates…"), but two of the
three mechanisms have no snippet of their own.

### 12. Unevidenced items — `Silicosis`, `Asbestosis`

Both entries leave 9 top-level items without any `evidence`:

- **`Silicosis`** — all three `has_subtypes` (`Chronic`, `Accelerated`, `Acute`),
  which is where the latency and exposure-intensity claims live ("developing after
  10-30 years of relatively low-level exposure", nodule size cutoffs); phenotypes
  `Dyspnea`, `Cough`, `Respiratory Insufficiency`; treatments
  `Silica Exposure Cessation and Dust Control`, `Whole-Lung Lavage`,
  `Lung Transplantation`.
- **`Asbestosis`** — two **core mechanism** nodes,
  `Pro-fibrotic mediator release` (asserts TGF-beta, PDGF, IGF-1, fibronectin as
  the inflammation→fibrosis bridge) and
  `Excessive extracellular matrix deposition`; phenotypes `Chronic cough`,
  `Bibasilar inspiratory crackles`, `Abnormal pulmonary interstitial morphology`,
  `Digital clubbing`; treatments `Supplemental oxygen therapy`,
  `Lung transplantation`, `Vaccination`.

Unevidenced *mechanism* nodes are the more serious of the two, since the pathograph
edges through them are load-bearing. For the clinical items, per CLAUDE.md the
options are a quotable source or moving the claim to `notes`.

### 13. Minor

- `Thallium_Poisoning` `pathophysiology[3].downstream[0]` has no `explanation`
  (every other evidence item in the file has one).
- `Cadmium_Poisoning` `pathophysiology[Hepatic Glutathione Depletion]` asserts
  glutathione *depletion*, but its snippets report reduced **GSH-Px enzyme
  activity** (not glutathione), and one (`PMID:41188353`) states cadmium "triggered
  a hepatic antioxidant **response**" — arguably the opposite direction. A second
  citation (`PMID:40164036`) reports the *exercise* arm's effect and is being read
  backwards to infer cadmium's effect.
- `Cadmium_Poisoning` `biochemical[Hepatic Transaminases (ALT/AST)]` is a human
  laboratory readout sourced only to a mouse exercise study.
- `Cadmium_Poisoning` reuses one systematic-review snippet (a generic list of
  diagnostic modalities) across five separate `diagnosis` nodes.

## Recommended fixes, in priority order

1. Source or remove the BAL contraindication in `Cadmium_Poisoning` (finding 1).
2. Drop the `PMID:19364190` challenge-testing framing from `Cadmium_Poisoning`
   diagnosis/biochemical; reanchor on the existing mainstream citations (finding 6).
3. Re-tag the misclassified `evidence_source` values (finding 5) — mechanical, and
   house style already exists in `Silicosis`/`Asbestosis`.
4. Downgrade `Cadmium_Poisoning` `Direct Osteoblast Toxicity` to `PARTIAL` and
   either add in-vitro osteoblast evidence or drop the independence-from-renal
   claim and the `DECREASED` process modifier (finding 2).
5. Strip or source the unevidenced quantitative thresholds in `Cadmium_Poisoning`
   descriptions (finding 4).
6. Re-draw the `Lead_Poisoning` neuropathy snippet from `PMID:20142857` (finding 8);
   swap the `Organophosphate_Poisoning` miosis snippet to `PMID:32626615`
   (finding 7).
7. Audit the 24 unsupported `frequency:` bands; omit where no quantitative source
   exists (finding 10).
8. Fix `Cadmium_Poisoning` histopathology nodes — either add real histology
   citations or relax the claims to what the autopsy snippets say (finding 3).
9. Decide `Mercury_Poisoning`'s scope, remove or source the ALS negative claim, and
   add the missing `treatments`/`diagnosis` sections (finding 11).
10. Add evidence to the two `Asbestosis` mechanism nodes and the three `Silicosis`
    subtypes (finding 12).

## Reproducing this review

```bash
# schema
uv run linkml-validate --schema src/dismech/schema/dismech.yaml \
  --target-class Disease kb/disorders/Cadmium_Poisoning.yaml

# snippet fidelity + coverage: see scripts described in Method above
just validate-terms-file kb/disorders/Cadmium_Poisoning.yaml
just validate-references kb/disorders/Cadmium_Poisoning.yaml
```

Note: `just validate-references` reported `Total checks: 0` on these files in this
environment (several publisher PDF fetches returned HTTP 403 behind the proxy), so
snippet fidelity here was established by direct normalized-substring comparison
against `references_cache/` bodies rather than by the validator.

---

## Resolution (applied 2026-07-25)

All ten recommended fixes were applied in the same branch. Post-fix state:

- **Schema:** 10/10 `No issues found`.
- **Snippet fidelity:** **602/602** snippets exact substrings (578 before; net +24
  evidence items added, none removed except the two retired `PMID:19364190` items).
- **Frequency bands:** 36 → 7. A follow-up audit of the 13 bands left by the
  first pass found that only some were genuinely supported, so a second sweep
  dropped 6 more (Lead `Anemia`; CO `Syncope`, `Coma`, `Chest pain`; Cadmium
  `Acute Respiratory Distress Syndrome`; Thallium `Constipation`) whose snippets
  carried no frequency signal, and re-banded 3 that contradicted their own
  snippet (Lead `Hypertension` and `Gout` `OCCASIONAL` → `FREQUENT`, per the
  source's "frequently presents"; CO `Headache` `VERY_FREQUENT` → `FREQUENT`).
  Of the **7** bands that remain: 4 are quantitatively supported (Pattern A —
  CO `Cognitive impairment` 15–40%, CO `Myocardial injury` ~one-third of
  moderate-to-severe cases, Thallium `Alopecia` 68%, Thallium `Abdominal pain`
  51%), 2 rest on a qualitative literature term mapped to a band (Pattern C —
  Lead `Hypertension`, `Gout`), and 1 is a documented clinical estimate
  (Pattern D — CO `Headache`). Every remaining band names its pattern in the
  evidence `explanation`.
- **Unevidenced top-level items:** 21 → 12, with all *mechanism* nodes and all
  disease *subtypes* now evidenced.

Four new references were fetched via the cache pipeline (never hand-written):
`PMID:6734559`, `PMID:25191413`, `PMID:30053129`, `PMID:30558238`.

| # | Finding | Resolution |
|---|---|---|
| 1 | BAL contraindication unevidenced | Rewritten and sourced to `PMID:6734559`. The blanket "is contraindicated" is replaced with what the evidence actually shows: BAL given ~30 min after cadmium exposure increased renal cadmium deposition in rats, but the same study found no renal increase when BAL was given at 24 h after metallothionein induction. Both directions cited, `supports: PARTIAL`, `evidence_source: MODEL_ORGANISM`, and the text now states plainly this is an animal-derived caution rather than a demonstrated human contraindication. |
| 2 | Challenge-testing source | `PMID:19364190` (*Altern Med Rev*) **removed entirely** from both the `biochemical` and `diagnosis` nodes. Reanchored on `PMID:20354761` (LMW proteinuria as the sensitive screening measure) and `PMID:41000307`. Both nodes now state explicitly that provoked/post-chelation urine testing is not accepted practice and has no validated thresholds. |
| 3 | `evidence_source` misclassification | **49 values re-tagged** — 17 in Cadmium (`PMID:20204475`, `20354761`, `19106433`, `31704329`, `41453694`), 32 in Thallium (`PMID:14579545`). Reviews → `OTHER`, cell-transport/analytical papers → `IN_VITRO`. |
| 4 | Direct Osteoblast Toxicity | Downgraded to `supports: PARTIAL`; the unsupported `biological_processes: osteoblast differentiation / DECREASED` assertion **removed**; description rewritten to say the direct arm is *not* established by the curated evidence and that the independence-from-renal claim is unsupported. New `KNOWLEDGE_GAP` discussion (`gap_cadmium_direct_osteoblast_toxicity`) with two proposed experiments — osteoblast/osteoclast culture, and an animal comparison with vs without renal phosphate wasting. |
| 5 | Unevidenced quantitative specifics | All five removed (bioavailability percentages, 200 mcg/g cortex threshold, ~7 kDa, the 5/50 mcg/L blood cut-offs in both `biochemical` and `diagnosis`, and the per-cigarette / smoker-ratio figures). Replaced with qualitative statements plus an explicit note that numeric cut-offs are laboratory- and population-specific and are deliberately not asserted. |
| 6 | Two misleading snippets | Lead `phenotypes[Peripheral neuropathy]`: snippet re-drawn from `PMID:20142857` to the sentence describing five battery-factory workers with electrophysiologically characterised radial neuropathy; the description now says motor-predominance is a tendency not an exclusive pattern, and the sensory-polyneuropathy case's `explanation` flags the discrepancy rather than hiding it. OP `phenotypes[Miosis]`: the "were less common in our patient population" snippet **replaced** with the positive sign list from `PMID:32626615`. |
| 7 | Unsupported frequency bands | **23 bands dropped** in the first pass (9 Lead, 8 Cadmium, 4 CO, 2 Thallium), including both Cadmium `VERY_FREQUENT` bands that rested on single case reports. A second sweep (see the Resolution note above) dropped **6 more** and re-banded **3**, leaving **7**. |
| 8 | Histopathology nodes | Claims relaxed to what the sources show and the three "multiple organ damage" citations downgraded to `PARTIAL` with corrected explanations. Descriptions now state which features (hyaline membranes, type II pneumocyte hyperplasia, hepatocellular necrosis) are the *expected* pattern rather than an observed finding in the curated sources. |
| 9 | Mercury scope, ALS claim, missing sections | ALS negative claim **sourced** to `PMID:30558238`, with the explanation noting the design limit (online self-report case-control, 401 vs 452) — absence of an observed association, not proof of no effect. Added `diagnosis` (blood/hair/toenail mercury, `PARTIAL`, carrying the source's own caveat that these matrices may not reflect remote injury; plus umbilical-cord methylmercury for prenatal exposure) and `treatments` (exposure cessation; supportive care, cited to "There is no effective treatment."). Added a `SCOPE NOTE` to the description and a `KNOWLEDGE_GAP` (`gap_mercury_inorganic_arm_not_curated`) recording that the elemental/inorganic arm is named but not modelled. Mercury evidence items 9 → 15. |
| 10 | Silicosis subtypes / Asbestosis mechanism nodes | All three Silicosis subtypes evidenced with `PMID:25191413` (the three-way acute/chronic/accelerated classification by exposure intensity and symptom onset) and `PMID:30053129` (accelerated silicosis after ~2 years of intense sandblasting). Both Asbestosis mechanism nodes evidenced: `Pro-fibrotic mediator release` with `PMID:12444030` (pulmonary TGF-beta1 alone is sufficient to produce fibroproliferative disease) and `PMID:37569765`; `Excessive extracellular matrix deposition` with `PMID:38192052` and `PMID:32553000`. Both descriptions now flag which sub-claims come from the wider literature rather than the curated sources. |

Minor findings also fixed: the missing Thallium `explanation`; the Cadmium
hepatic-glutathione node's direction-of-effect overreach (now states the readout
is antioxidant *enzyme* activity, not glutathione stores, and that one source
reports an antioxidant *response*); and the mouse-only hepatic transaminase
readout downgraded to `PARTIAL`.

**Deliberately not fixed** (recorded so the remaining gap is visible, not silent):
12 clinical `phenotypes`/`treatments` items still carry no evidence — 3 in
Silicosis (`Respiratory Insufficiency`, `Silica Exposure Cessation and Dust
Control`, `Whole-Lung Lavage`), 6 in Asbestosis (`Chronic cough`, `Bibasilar
inspiratory crackles`, `Abnormal pulmonary interstitial morphology`, `Digital
clubbing`, `Lung transplantation`, `Vaccination`), 2 in Carbon Monoxide, 1 in
Methanol. These are uncontroversial clinical facts with no quotable sentence in
the currently cached sources; per CLAUDE.md the options are a new citation or a
move to `notes`, and neither was in scope for this pass.

Finding 9 in the list above (Lead's use of generic background sentences from a
laboratory methods paper to carry the `Anemia` and `Developmental delay`
phenotype claims) was also left in place: the claims are correct and the snippets
are honest, they are simply thinner support than better primary sources already
present in the file would give.
