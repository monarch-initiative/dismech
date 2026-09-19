# Eye Disorder Claim–Evidence Review (2026-07-25)

Correctness review of 10 eye-disorder entries, focused on **claim–evidence match**:
does each cited snippet actually support the claim it is attached to, at the
strength the `supports:` grade asserts?

## Scope

Ten entries spanning the main mechanistic classes of ocular disease (evidence-item
counts as of the current branch head, after the fixes described below):

| Entry | Class | Evidence items |
|---|---|---|
| `Age_Related_Macular_Degeneration` | Complex/degenerative | 68 |
| `Achromatopsia` | Inherited cone dysfunction | 105 |
| `Fuchs_Endothelial_Corneal_Dystrophy` | Corneal dystrophy | 58 |
| `Diabetic_Retinopathy` | Systemic microvascular | 34 |
| `RHO-Related_Retinopathy` | Inherited retinal dystrophy | 42 |
| `Glaucoma` | Optic neuropathy | 27 |
| `Cytomegalovirus_Retinitis` | Infectious | 17 |
| `Central_Retinal_Artery_Occlusion` | Vascular/ischemic | 16 |
| `Retinopathy_of_Prematurity` | Developmental/vascular | 14 |
| `Retinoblastoma` | Neoplastic | 5 |

## Automated validation: all clean

All ten pass the full stack — `linkml-validate` (schema), `linkml-term-validator`
(ontology IDs + labels), and `linkml-reference-validator` (snippet-in-source
substring matching). The reference validator was control-tested by corrupting a
snippet in a scratch copy of `Retinoblastoma.yaml`; it correctly flagged the
mismatch, confirming the "all validations passed" result is meaningful and not a
silent no-op.

**That control test earned its keep, and the reason is worth recording precisely.**
On a clean run against these entries the reference validator reports `Total checks:
0 / All validations passed` — which reads like a no-op and was flagged as one during
PR review. It is not: re-running the control test on the current branch (corrupt one
snippet in `RHO-Related_Retinopathy.yaml`, run, revert) produces `Total checks: 1`
and `Text part not found as substring` against the right PMID. So detection works;
what is broken is the **reported count**, which appears to tally only failures. The
practical consequence is the same either way — `Total checks: 0` carries no
information about how many snippets were actually compared, so a green line from
this validator cannot by itself substantiate a "snippets verified" claim. That
asymmetry is a tooling bug worth its own issue, separate from any content here.

Two DOI-based references in this entry set fail to download (403), so they are not
checked at all — a second, quieter reason the count is not a coverage measure.

Accordingly, snippet verification behind the later rounds of fixes was done by
direct whitespace-normalized substring comparison against `references_cache/`
(130 snippets across the five edited entries, zero mismatches) **in addition to**
the validator, with the control test re-run each round rather than assumed.

**Every finding below is therefore invisible to CI.** These are semantic
claim–evidence defects: the quote is genuine and correctly transcribed, but it
does not establish what the claim asserts. This is the failure mode the
validation stack structurally cannot catch.

---

## Tier 1 — Fixed in this branch

Items 1–2 are outright factual errors. Items 3–4 were promoted here from Tier 2
during PR review once it was clear they needed no new source — only a re-quote and
a grade correction. Items 5–6 were promoted in a second review round, on the
principle that a nav-linked document asserting a grade is wrong should not ship
alongside that grade: the regrades need no new literature, so parking them was
not defensible.

### 1. `RHO-Related_Retinopathy` — CSNBAD1 ERG waveform was backwards

The `Negative electroretinogram waveform` phenotype asserted that gain-of-function
RHO CSNB produces:

> a characteristic negative ERG waveform — **preserved a-wave with reduced b-wave**
> — reflecting **inner-retinal signal disruption**

This inverts the electrophysiology. CSNB splits into two ERG classes by the level
of the lesion:

- **Schubert–Bornschein ("negative") ERG** — large a-wave, minimal b-wave. Arises
  from a *photoreceptor-to-bipolar-cell transmission* defect (NYX, CACNA1F).
- **Riggs-type ERG** — loss of the rod a-wave *and* b-wave. Arises from a
  *phototransduction* abnormality.

RHO G90D/T94I CSNB is a phototransduction lesion — the entry's own upstream node
says so ("constitutive activity in darkness causing rod desensitization"). It is
therefore Riggs-type, and the node contradicted the mechanism it claims to be a
readout of.

Per PubMed, Marmor & Zeitz confirm the dichotomy explicitly
([DOI](https://doi.org/10.1007/s10633-018-9651-0), PMID:30051303): *"CSNB from
abnormalities in phototransduction can be recessive or dominant and is much less
common. This produces a Riggs type of ERG with loss of the rod a-wave as well as
the b-wave."* See also
[DOI](https://doi.org/10.1111/aos.14693) (PMID:33369259), which classes
phototransduction-dysfunction CSNB as Riggs type.

**Fixed**: node renamed to `Riggs-type electroretinogram`, description and
`reports_on.interpretation` corrected, and PMID:30051303 fetched and cited for the
class-level ERG dichotomy. The companion G90D citation (PMID:38743626) originally
quoted a generic CSNB definitional sentence; during PR review it was swapped for
the RHO-specific bridging sentence already present in the same cached abstract
("One well-studied rhodopsin point mutant, G90D-Rho, is thought to cause CSNB
because of its constitutive activity in darkness causing rod desensitization"),
so the disease-level step is now sourced rather than inferred. That division of
labour matters: PMID:30051303 is a *GNAT1* report and establishes only the class
dichotomy; without the swap, CSNBAD1's membership in the phototransduction class
would have been curator inference carrying a `SUPPORT` grade.

Note the original snippet — "profound loss of rod sensitivity without severe
retinal degeneration" — is a true quote that says nothing about a-wave or b-wave.
The wrong claim rode entirely in the `explanation` field, which no validator reads.

### 2. `Retinoblastoma` — pediatric restriction dropped from the source claim

`histopathology[0].description` read "Retinoblastoma is the most common intraocular
malignancy." The source says "the most common intraocular malignancy **in
children**" — and the snippet had been truncated at exactly `"...malignancy in"`,
which passes substring validation while cutting the qualifier that makes the claim
true. In adults, uveal melanoma is the most common primary intraocular malignancy.

**Fixed**: description scoped to children, snippet extended to the full sentence
(`Retinoblastoma is the most common intraocular malignancy in children.`), and
`evidence_source: HUMAN_CLINICAL` added. The adult contrast — that uveal melanoma
leads in adults — is **not** in the description: PR review correctly pointed out
that the first attempt at this fix stated it there, which made it an uncited claim
sitting above an `evidence:` block that does not cover it. It now lives in the
`notes:` slot on the `HistopathologyFinding`, explicitly labelled as an uncited
orienting note, per the CLAUDE.md "When Evidence Cannot Be Verified" rule.

This is worth naming as a pattern: **truncating a snippet mid-clause to make it
match is a red flag**, because the dropped words are often the ones carrying the
scope limit.

### 3. `RHO-Related_Retinopathy` — orphan snippet fragment for the 72-year figure

`pathophysiology[2].downstream[1]` claimed "median age to mild visual acuity
impairment is 72 years" while quoting only the dangling tail of the sentence:
*"whereas this could not be computed for lower acuities."* The full sentence
carrying the figure was **already correctly quoted elsewhere in the same file**
(`phenotypes[3]`, same PMID:32301896), so no new source was needed.

**Fixed**: snippet replaced with the complete sentence; explanation updated to
state what it now quantifies. This is itself an instance of the dangling-clause
pattern that recommendation #2 below proposes linting for.

### 4. `Retinopathy_of_Prematurity` — evidence graded against its own direction

`treatments[1].evidence[0]` was graded `SUPPORT` for preferring anti-VEGF over
laser, but the quoted result points the other way (RR 2.14, 95% CI 1.06–4.33 —
roughly *twice* the recurrence risk of laser). The explanation claimed the
meta-analysis "quantifies anti-VEGF efficacy"; it quantifies a disadvantage.

**Fixed**: regraded `PARTIAL`, explanation rewritten as the trade-off it actually
is. The residual unsourced claim in that treatment's `description` is a separate,
still-open item — see Tier 2 below.

### 5. `RHO-Related_Retinopathy` — the CSNBAD1 branch had no human RHO evidence

Both CSNBAD1 phenotype nodes (`Riggs-type electroretinogram`, `Congenital night
blindness`) rested solely on `PMID:38743626`, a G90D knock-in **mouse**. The
companion `PMID:30051303` is human but reports a *GNAT1* family, and its quoted
sentence is a class-level statement about phototransduction-defect CSNB — it
establishes the dichotomy, not the RHO patient ERG. CLAUDE.md is explicit that
model-organism evidence should not be the only support for a human phenotype, and
for the RHO-specific step it was.

**Fixed**: two human references fetched and added.

- `PMID:33669941` (Kobal 2021; 15 p.G90D patients from three families) states
  directly that RHO-related CSNB is of the Riggs type with loss of rod-specific ERG
  activity, a reduced dark-adapted a-wave and low b-wave, and largely preserved
  cone responses — the human counterpart of the mouse item, on exactly the
  a-wave/b-wave point.
- `PMID:9888392` (al-Jandal 1999) sources the **T94I** half of the subtype
  description from an Irish family segregating that variant, which previously had
  no human genetic support.

The same cohort also supplied *derived counts* for the two `VERY_FREQUENT` bands
that were previously unsourced assertions (3/3 CSNB patients with the typical
electrophysiology; 15/15 with lifelong non-worsening night blindness) — the
"derived counts" pattern in `docs/frequency-evidence-guidelines.md` rather than a
qualitative-term mapping.

**And it partly contradicted the entry, which is the more interesting outcome.**
In that cohort only 20% of p.G90D carriers were classified CSNB while **53.3%
developed classic RP**, and the authors caution against diagnosing CSNB in p.G90D
carriers without long follow-up into adulthood. The `Congenital night blindness`
description no longer asserts a flatly non-degenerative course; the caveat is
recorded in `notes:`, scoped to p.G90D (T94I, A292E, A295V are not associated with
progression). The CSNBAD1 subtype description is left as the nosological
definition. Going looking for human evidence to satisfy a discipline rule turned
up a phenotype-spectrum correction nobody had asked for.

### 6. Six grade-only corrections applied rather than parked

Every item below was documented in Tier 2 as a wrong `supports:` grade needing no
new source. Each is now regraded with an `explanation` stating what the snippet
does and does not license:

| Entry | Location | Was | Now |
|---|---|---|---|
| `Glaucoma` | `pathophysiology[3]` TM dysfunction (myocilin evidence) | `SUPPORT` | `PARTIAL` |
| `Glaucoma` | `treatments[2]` alpha agonist non-difference result | `SUPPORT` | `PARTIAL` |
| `Diabetic_Retinopathy` | `has_subtypes[1]` severe-NPDR staging | `SUPPORT` | `PARTIAL` |
| `Diabetic_Retinopathy` | `treatments[1]` PRP cost-effectiveness | `SUPPORT` | `PARTIAL` |
| `Diabetic_Retinopathy` | `treatments[2]` vitrectomy | `SUPPORT` | `PARTIAL` |
| `Central_Retinal_Artery_Occlusion` | `pathophysiology[1]` ischemic-injury mechanism | `SUPPORT` | `PARTIAL` |

CRAO is the one where a replacement source is genuinely still needed — the cached
abstract contains no mechanistic content at all — so its `explanation` now says so
outright instead of leaving `SUPPORT` standing while the gap is unfilled.

Also in this round: the `Retinopathy_of_Prematurity` `FREQUENT` band resting on a
denominator was dropped, with a `notes:` line recording why so it is not re-added
from the same snippet; and the two absent `evidence_source` values on the Glaucoma
items were filled (`PMID:10617907` → `IN_VITRO`, in situ hybridization on ex vivo
specimens; `PMID:37217093` → `OTHER`, a narrative review stating consensus rather
than primary data).

### 7. The remaining regrade-only items, applied

A later review round observed that this report was still shipping alongside seven
defects it documents as fixable without new literature — the same contradiction
item 6 addressed. They are now closed:

| Entry | Location | Was | Now |
|---|---|---|---|
| `RHO-Related_Retinopathy` | RP-definition snippet ×4 (night blindness edge, `phenotypes[0]`, `[2]`, `[4]`) | `SUPPORT` | `PARTIAL` |
| `RHO-Related_Retinopathy` | `phenotypes[4]` bone-spicule pigmentation | — | **+`SUPPORT`** from `PMID:33669941` |
| `RHO-Related_Retinopathy` | `phenotypes[5]` rod ERG | `SUPPORT` on a BCVA snippet | **+`SUPPORT`** from `PMID:33669941`; BCVA item → `PARTIAL` |
| `Diabetic_Retinopathy` | `phenotypes[2]` retinal hemorrhage (wrong compartment) | `SUPPORT` | `NO_EVIDENCE` |
| `Diabetic_Retinopathy` | `treatments[2]` vitrectomy | `PARTIAL` | `NO_EVIDENCE` |
| `Central_Retinal_Artery_Occlusion` | `phenotypes[1]` acuity (meta-analysis *aim*) | `SUPPORT` | `PARTIAL` |
| `Retinopathy_of_Prematurity` | `phenotypes[4]` myopia | `SUPPORT` + `FREQUENT` | `PARTIAL`, band dropped |
| `Glaucoma` | `genetic[1]` OPTN typing + 4 missing `evidence_source` | `Risk Factor`, untagged | `Causative`, tagged, item `PARTIAL` |

One flagged item was **not** changed after checking it: the fourth
`PMID:29776671` citation in `Diabetic_Retinopathy` quotes a different, apt sentence
on a `Visual Impairment` node. See that section for why reference reuse and
sentence reuse are different things.

---

## Tier 2 — Claim–evidence mismatches (recommended for curator follow-up)

Bulleted items below carry an explicit status marker — **[Open]**, **[Fixed]**, or a
split marker where a grade was corrected but the underlying source gap remains
(e.g. **[Fixed grade / Open source]**). Where an item is written as narrative prose
rather than a bullet (the `Diabetic_Retinopathy` and `RHO-Related_Retinopathy`
sections), the status is stated inline in bold instead. Read the status, not the
tense: this section drifted out of sync with the KB in four consecutive review
rounds while the fixes landed, which is what recommendation 8 is about — and the
mixed markup here is itself the residue of that drift, since the narrative sections
predate the marker convention.

What remains here needs a replacement source or new literature; the items that
needed only a re-quote or a grade change have all been promoted to Tier 1 across
two review rounds (items 3–4, then the six regrades in item 6 and the human-evidence
gap in item 5). The pattern worth carrying forward: **"needs new literature" is a
claim to check before it becomes a deferral.** In four separate cases here the
source was already in the repository — the 72-year sentence quoted elsewhere in the
same file, the G90D bridging sentence sitting in the same cached abstract — and in
six more the fix needed no source at all. Where a remaining item is similarly cheap,
that is noted inline.

### `Diabetic_Retinopathy` — one guideline reference propping up three unrelated claims

`PMID:29776671` (ICO Diabetic Eye Care guidelines) is cited three times with generic
scope text that supports none of the attached claims:

| Location | Claim | Snippet |
|---|---|---|
| `has_subtypes[1]` | Severe NPDR 4-2-1 rule; "~50% progression to PDR within 1 year" | "Vision loss from DR can be prevented with broad-level public health strategies…" |
| `treatments[1]` | PRP is a cost-effective treatment | same snippet — never mentions laser |
| `treatments[2]` | Vitrectomy is among the options | "appropriate management of vision-threatening DR…" — never mentions vitrectomy |

All three were graded `SUPPORT` with each `explanation` asserting guideline content
absent from the quoted text. **The grades are now `PARTIAL`** (Tier 1 item 6), which
is the honest reading of a generic scope sentence attached to a specific claim.

**Still open here**: the 4-2-1 rule and the ~50%/1-year figure are genuine
ETDRS-derived facts but remain **unsourced** in the entry — the regrade stopped the
entry from overstating its evidence, it did not supply the missing citation.

A fourth use of the same reference at `phenotypes[0]` was reviewed and **left as
`SUPPORT` deliberately**. It quotes a different sentence — "Diabetic retinopathy
(DR) is a major complication of DM and a leading cause of vision loss in working
middle-aged adults" — attached to a `Visual Impairment` phenotype, which it
supports directly. Reuse of one *reference* across many nodes is not the
anti-pattern; reuse of one generic *sentence* to carry specific claims is. Worth
stating, because a reviewer reading "fourth use of PMID:29776671" flagged it as
part of the same defect.

Also **fixed** (Tier 1 item 7): `phenotypes[2]` "Retinal Hemorrhage" described
intraretinal dot-blot and flame-shaped hemorrhages in NPDR while citing a snippet
about **vitreous** haemorrhage in PDR — a different compartment at a different
stage, and one already modeled by the `Vitreous Hemorrhage` node immediately below.
Regraded `NO_EVIDENCE`, since the sentence is silent on the claim rather than weakly
supportive of it. The NPDR intraretinal pattern still needs a source.

The vitrectomy item was also moved `PARTIAL` → `NO_EVIDENCE` on the same reasoning:
its explanation already said the snippet "never mentions vitrectomy", which is the
definition of `NO_EVIDENCE`, not `PARTIAL`.

Also in this entry, both **still open**:
- **[Open]** `treatments[0]` claims "18–45% of patients gaining ≥15 ETDRS letters" — not in
  any of its three snippets.
- **[Open]** `classifications.harrisons_chapter[0].evidence[1]` uses the article *title* as
  its snippet, which is a degenerate citation.

A third bullet here — `phenotypes[2]` "Retinal Hemorrhage" citing a vitreous
haemorrhage snippet — was **fixed** in Tier 1 item 7 and is described above; it is
removed from this list rather than left to contradict it. That duplication is the
hazard recommendation 8 below addresses.

### `RHO-Related_Retinopathy` — generic snippet reuse

Beyond the fixed ERG error, one sentence — "Inherited mutations in the rod visual
pigment, rhodopsin, cause the degenerative blinding condition, retinitis
pigmentosa (RP)" — is reused as `SUPPORT` for night blindness, rod-cone dystrophy
classification, and **bone-spicule pigmentation**, none of which it mentions. The
`explanation` fields do the actual work via curator inference ("RP is classically
defined by…"), which is reasoning, not evidence.

**Fixed** (Tier 1 item 7): all four instances — `pathophysiology[1].downstream[0]`,
`phenotypes[0]`, `phenotypes[2]`, `phenotypes[4]` — are now `PARTIAL`, each with an
`explanation` naming what the sentence does and does not say. The bone-spicule node
went further: `PMID:33669941` reports the finding directly in RHO patients ("Bone
spicule pigmentation was seen in all individuals with RP… and none of the patients
diagnosed with CSNB"), so it now carries a `SUPPORT` item alongside the downgraded
one — and the same sentence corroborates the phenotype's RP4 scoping.

Also **fixed**: `phenotypes[5]` "Reduced rod electroretinogram" cited a snippet about
BCVA and visual-field decline rates with no ERG content. The same Kobal cohort
supplies the observation directly ("The function of the rod system, as revealed by
dark-adapted (DA) full-field ERG (ffERG), was highly dysfunctional in all
patients."), so that is now the `SUPPORT` item and the natural-history snippet is
`PARTIAL` as corroboration of progressive functional loss.

Both are the third and fourth times in this review that a defect deferred as
"needs a replacement source" was closed by a source **already in the repository** —
in these two cases, a cached abstract fetched for an entirely different node.

Two items previously listed here are now **fixed**: the orphan 72-year fragment at
`pathophysiology[2].downstream[1]` (Tier 1 item 3), and the unsourced
`VERY_FREQUENT` band on the `Riggs-type electroretinogram` node together with the
absence of any human RHO ERG observation — both closed by `PMID:33669941` (Tier 1
item 5). The class-level CSNB definitional snippet on `Congenital night blindness`
was also regraded `PARTIAL`, since the RHO-specific human step is now carried by its
own citation rather than by inference from a definition.

### `Retinopathy_of_Prematurity`

- **[Fixed]** `phenotypes[0]` frequency `FREQUENT` rested on "141 550 infants received ROP
  screening in Germany" — a denominator, not a rate. **Fixed**: band dropped, with a
  `notes:` line recording why so it is not re-derived from the same snippet
  (cf. `docs/frequency-evidence-guidelines.md`, which says omit rather than justify).
- **[Open]** `treatments[1]`'s `description` still asserts anti-VEGF is "preferred over laser
  for Zone I and posterior Zone II ROP due to better structural outcomes." Neither
  remaining evidence item carries that: one is the recurrence-risk trade-off, the
  other a registry trend in treatment preference. The superlative needs a source or
  should be softened. (The evidence *grade* half of this item — `SUPPORT` on an
  opposite-direction result — was **fixed**; see Tier 1 item 4.)
- **[Fixed]** `phenotypes[4]` Myopia `FREQUENT` cited only "laser photocoagulation can lead to
  refractive errors" — supporting neither the frequency nor the "regardless of
  treatment" scope. **Fixed** (Tier 1 item 7): band dropped with a `notes:`
  rationale, description narrowed to what the evidence covers, item regraded
  `PARTIAL`. Leaving this while dropping the band on `phenotypes[0]` eighty lines
  earlier was the internal inconsistency worth catching.
- **[Open]** `treatments[2]` "fewer than 30% achieving ambulatory vision" in Stage 5 —
  unsupported by its snippet.

### `Central_Retinal_Artery_Occlusion`

- **[Fixed grade / Open source]** `pathophysiology[1]` "Inner Retinal Ischemic Injury" (retinal edema, neuronal
  injury) was `SUPPORT`ed by "CRAO has consistently been identified as a serious
  medical condition that leads to substantial visual impairment" — no mechanism
  content at all. **Grade fixed** to `PARTIAL` (Tier 1 item 6); the `explanation` now
  states that a mechanism source is still required. Reading the full cached abstract
  confirms there is no mechanistic content anywhere in it, so this one does still
  need a replacement citation — the regrade stops the overstatement, it does not
  close the gap.
- **[Fixed grade / Open band]** `phenotypes[1]` "Reduced Visual Acuity" `VERY_FREQUENT` cites a meta-analysis
  *aim* statement. **Grade fixed** to `PARTIAL` (Tier 1 item 7) — a statement of
  intent establishes that visual outcomes are the measured endpoint, but evidences
  neither the phenotype nor the band. The `VERY_FREQUENT` band remains unsourced.
- **[Open]** The THEIA phase 3 trial (PMID:41109232) is cited only for a background
  definition; its actual result is not recorded anywhere in the entry.

### `Glaucoma`

- **[Fixed grade / Open source]** `pathophysiology[3]` "Trabecular Meshwork Dysfunction" describes age-related
  change, oxidative stress, and ECM alteration, but both evidence items are about
  myocilin — a different (Mendelian *MYOC*) mechanism. **Fixed**: both are now
  `PARTIAL`, and both carry an `evidence_source`. The node still lacks evidence for
  the age/oxidative-stress mechanism it actually describes.
- **[Fixed]** `treatments[2]` Alpha Agonists: the snippet "IOP reduction was similar for both
  groups" is a *non-difference* result vs timolol (n=16); the explanation read it as
  evidence of "clinically meaningful intraocular pressure lowering." **Fixed**:
  regraded `PARTIAL`, explanation rewritten as non-inferiority to an established
  agent rather than a demonstrated absolute effect.
- **[Fixed]** `genetic[1]` OPTN was typed `Risk Factor` with notes scoping it to normal-tension
  glaucoma, but the cited snippet says only "associated with primary open angle
  glaucoma" and OPTN E50K is generally treated as causative-dominant. **Fixed**
  (Tier 1 item 7): retyped `Causative`, the association item regraded `PARTIAL`
  since "associated with" settles neither the NTG scope nor the typing, and the
  `notes:` now records that the NTG scoping comes from the wider OPTN literature
  rather than the cited paper. Both OPTN items are tagged `IN_VITRO` (cultured
  cells expressing mutant optineurin) and both MYOC items `OTHER` (review
  synthesis) — the `evidence_source` backfill this PR began one file section
  earlier, now finished.

### `Cytomegalovirus_Retinitis` and `Fuchs_Endothelial_Corneal_Dystrophy` — minor only

- **[Open]** CMV `pathophysiology[2]`: the characteristic morphology claim (yellow-white
  opacification, centrifugal advance) is not in its snippet, which covers only
  rapid progression to blindness.
- **[Open]** Fuchs `pathophysiology[5].evidence[2]`: a textbook statement of what mitochondria
  do in general, cited as a "mechanistic bridge" to FECD apoptosis.
- **[Open]** Fuchs `phenotypes[7]`: Nyctalopia `FREQUENT` comes from an Orphanet HPO
  annotation that primary FECD literature does not support. The curator flagged
  this transparently in the description — correct handling, but it likely reflects
  an **upstream Orphanet annotation defect** worth reporting to ORPHA:98974.

---

## What is working well

Three entries should be treated as reference examples of evidence discipline:

- **`Age_Related_Macular_Degeneration`** — the strongest of the ten. It records a
  disconfirming caveat as first-class evidence (drusen "might be no more than a
  biomarker… and not a cause", graded `PARTIAL`), keeps *protective* CFB/C2
  haplotypes rather than flattening the locus to risk-only, and records the
  complement-inhibitor **negative** BCVA result and the pegcetacoplan MNV safety
  signal alongside the positive lesion-growth result.
- **`Achromatopsia`** — grades all gene-therapy evidence `PARTIAL` and quotes the
  investigators' own limitation ("the absence of randomized concurrent control
  individuals precludes determining a cause-and-effect relationship"). It also
  holds the progressive-vs-stationary tension openly, citing both the OCT
  age-dependent thinning and the "predominantly stationary with respect to BCVA"
  cohort finding.
- **`Fuchs_Endothelial_Corneal_Dystrophy`** — quotes ORPHA rows with their exact
  frequency bands rather than restating them, so every frequency is traceable.

The common factor: **the `supports:` grade is used as a real signal.** Where
entries fall down, it is almost always because everything is graded `SUPPORT`.

## Cross-cutting recommendations

1. **`description` and `explanation` are unvalidated prose, and that is where wrong
   claims hide.** The two original Tier 1 errors lived there, behind
   correctly-transcribed snippets; any protocol that checks snippets without
   reading the surrounding prose will miss them. This cuts both ways, and did:
   PR review caught an *uncited* sentence introduced into the `Retinoblastoma`
   description by the fix itself (the true-but-unsourced uveal-melanoma contrast),
   which has since moved to `notes:`. Unevidenced context belongs in `notes:`,
   never in a `description` sitting above an `evidence:` block that does not
   cover it.
2. **Treat mid-clause snippet truncation as a lint target.** A snippet ending in a
   dangling preposition or conjunction (`"…malignancy in"`, `"…highly active
   antiretroviral"`, `"whereas this could not be computed for lower acuities."`) is
   a cheap, mechanically detectable signal of scope-dropping. This would be a
   useful advisory check in `just qc`.
3. **One generic snippet reused across many specific nodes is an anti-pattern.**
   The DR/ICO and RHO cases are both this shape. Reusing a definitional sentence
   as `SUPPORT` for a downstream specific claim should default to `PARTIAL`. The
   DR/ICO instances have been regraded (Tier 1 item 6) and one RHO instance with
   them; the four-way reuse of the RP-definition sentence in
   `RHO-Related_Retinopathy` is the remaining known case.
4. **Frequency bands still need their own evidence.** Several `FREQUENT` /
   `VERY_FREQUENT` values here rest on snippets that establish only the
   association, exactly the failure `docs/frequency-evidence-guidelines.md` warns
   about.
5. **A grade correction is not a citation.** Regrading `SUPPORT` → `PARTIAL` stops
   an entry overstating what it has, but the underlying claim stays unsourced —
   `Diabetic_Retinopathy`'s 4-2-1 rule and the CRAO ischemic-injury mechanism are
   both still gaps after their regrades. Regrade to stop the misrepresentation, then
   track the missing source separately; do not let the honest grade close the item.
6. **`PARTIAL` is not the default downgrade — distinguish it from `NO_EVIDENCE`.**
   The schema defines `PARTIAL` as "partially or indirectly supports" and
   `NO_EVIDENCE` as "does not contain evidence relevant to the claim". Downgrading
   everything to `PARTIAL` re-creates the original problem one notch lower, because
   it still reads as partial support. Working rule used here: if the snippet frames
   the claim but stops short of establishing it, `PARTIAL` (a meta-analysis *aim*
   statement about visual outcomes; a guideline scope sentence about the treatment
   area); if the snippet is simply silent on the claim, `NO_EVIDENCE` (a vitreous
   haemorrhage sentence under an intraretinal-hemorrhage node; a scope sentence that
   never mentions the procedure it is attached to). A snippet about a *different*
   entity is not weak evidence for this one.
7. **Reference reuse is fine; sentence reuse is the anti-pattern.** One paper can
   legitimately support many nodes when each cites the sentence that speaks to that
   node — this entry set has several such cases. The defect is one *generic
   definitional sentence* carrying specific downstream claims. Audit at the snippet
   level, not the reference level, or correct citations get regraded along with the
   bad ones.
8. **A findings document needs an explicit status marker per item, not prose tense.**
   This report drifted out of sync with the KB in four consecutive review rounds,
   and once contradicted itself inside a single section — a bullet describing a
   defect in the present tense sat nine lines below a paragraph announcing the same
   defect fixed. Marking every item **Fixed** or **Open** makes a stale entry
   visually obvious on the next pass, where "defect stated in past tense, then a
   *Fixed* note" does not. Any review artifact that ships alongside the data it
   describes will drift as the data is repaired; the format has to make the drift
   cheap to spot.

## Reproducing

```bash
just validate kb/disorders/RHO-Related_Retinopathy.yaml
just validate-references kb/disorders/Retinoblastoma.yaml
just validate-terms-file kb/disorders/RHO-Related_Retinopathy.yaml
```
