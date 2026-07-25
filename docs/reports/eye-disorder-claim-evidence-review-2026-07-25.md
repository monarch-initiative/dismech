# Eye Disorder Claim–Evidence Review (2026-07-25)

Correctness review of 10 eye-disorder entries, focused on **claim–evidence match**:
does each cited snippet actually support the claim it is attached to, at the
strength the `supports:` grade asserts?

## Scope

Ten entries spanning the main mechanistic classes of ocular disease:

| Entry | Class | Evidence items |
|---|---|---|
| `Age_Related_Macular_Degeneration` | Complex/degenerative | 68 |
| `Achromatopsia` | Inherited cone dysfunction | 105 |
| `Fuchs_Endothelial_Corneal_Dystrophy` | Corneal dystrophy | 58 |
| `Diabetic_Retinopathy` | Systemic microvascular | 34 |
| `RHO-Related_Retinopathy` | Inherited retinal dystrophy | 34 |
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

**Every finding below is therefore invisible to CI.** These are semantic
claim–evidence defects: the quote is genuine and correctly transcribed, but it
does not establish what the claim asserts. This is the failure mode the
validation stack structurally cannot catch.

---

## Tier 1 — Factual errors (fixed in this branch)

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
`reports_on.interpretation` corrected, PMID:30051303 fetched and cited as primary
evidence, and the existing G90D mouse citation re-explained to support the
phototransduction-level localization rather than the (wrong) inner-retinal one.

Note the original snippet — "profound loss of rod sensitivity without severe
retinal degeneration" — is a true quote that says nothing about a-wave or b-wave.
The wrong claim rode entirely in the `explanation` field, which no validator reads.

### 2. `Retinoblastoma` — pediatric restriction dropped from the source claim

`histopathology[0].description` read "Retinoblastoma is the most common intraocular
malignancy." The source says "the most common intraocular malignancy **in
children**" — and the snippet had been truncated at exactly `"...malignancy in"`,
which passes substring validation while cutting the qualifier that makes the claim
true. In adults, uveal melanoma is the most common primary intraocular malignancy.

**Fixed**: description scoped to children with the adult contrast stated, snippet
extended to include `in children.`, and `evidence_source: HUMAN_CLINICAL` added.

This is worth naming as a pattern: **truncating a snippet mid-clause to make it
match is a red flag**, because the dropped words are often the ones carrying the
scope limit.

---

## Tier 2 — Claim–evidence mismatches (recommended for curator follow-up)

Not fixed here, because each needs a replacement source rather than a rewording.

### `Diabetic_Retinopathy` — one guideline reference propping up three unrelated claims

`PMID:29776671` (ICO Diabetic Eye Care guidelines) is cited three times with generic
scope text that supports none of the attached claims:

| Location | Claim | Snippet |
|---|---|---|
| `has_subtypes[1]` | Severe NPDR 4-2-1 rule; "~50% progression to PDR within 1 year" | "Vision loss from DR can be prevented with broad-level public health strategies…" |
| `treatments[1]` | PRP is a cost-effective treatment | same snippet — never mentions laser |
| `treatments[2]` | Vitrectomy is among the options | "appropriate management of vision-threatening DR…" — never mentions vitrectomy |

All three are graded `SUPPORT`, and each `explanation` asserts guideline content
that is not in the quoted text. The 4-2-1 rule and the ~50%/1-year figure are
genuine ETDRS-derived facts but are currently **unsourced** in the entry.

Also in this entry:
- `phenotypes[2]` "Retinal Hemorrhage" describes intraretinal dot-blot/flame
  hemorrhages in NPDR but cites a snippet about **vitreous** haemorrhage in PDR.
- `treatments[0]` claims "18–45% of patients gaining ≥15 ETDRS letters" — not in
  any of its three snippets.
- `classifications.harrisons_chapter[0].evidence[1]` uses the article *title* as
  its snippet, which is a degenerate citation.

### `RHO-Related_Retinopathy` — generic snippet reuse

Beyond the fixed ERG error, one sentence — "Inherited mutations in the rod visual
pigment, rhodopsin, cause the degenerative blinding condition, retinitis
pigmentosa (RP)" — is reused as `SUPPORT` for night blindness, rod-cone dystrophy
classification, and **bone-spicule pigmentation**, none of which it mentions. The
`explanation` fields do the actual work via curator inference ("RP is classically
defined by…"), which is reasoning, not evidence.

Two further specifics:
- `pathophysiology[2].downstream[1]` claims "median age to mild visual acuity
  impairment is 72 years" but its snippet is the orphan fragment "whereas this
  could not be computed for lower acuities." The full sentence containing the
  72-year figure *is* quoted correctly at `phenotypes[3]` — this is a bad split of
  a good source.
- `phenotypes[5]` "Reduced rod electroretinogram" cites a snippet about BCVA and
  visual-field decline rates, with no ERG content.

### `Retinopathy_of_Prematurity`

- `phenotypes[0]` frequency `FREQUENT` rests on "141 550 infants received ROP
  screening in Germany" — a denominator, not a rate. The frequency band is
  unsupported (cf. `docs/frequency-evidence-guidelines.md`).
- `treatments[1]` describes anti-VEGF as "preferred over laser… due to better
  structural outcomes", but its `SUPPORT` snippet reports the *opposite-direction*
  finding (RR 2.14 higher recurrence vs laser). The `explanation` claims the
  meta-analysis "quantifies anti-VEGF efficacy"; it quantifies recurrence risk.
  Should be `PARTIAL` with the trade-off stated.
- `phenotypes[4]` Myopia `FREQUENT` cites only "laser photocoagulation can lead to
  refractive errors" — supports neither the frequency nor the
  "regardless of treatment" scope.
- `treatments[2]` "fewer than 30% achieving ambulatory vision" in Stage 5 —
  unsupported by its snippet.

### `Central_Retinal_Artery_Occlusion`

- `pathophysiology[1]` "Inner Retinal Ischemic Injury" (retinal edema, neuronal
  injury) is `SUPPORT`ed by "CRAO has consistently been identified as a serious
  medical condition that leads to substantial visual impairment" — no mechanism
  content at all.
- `phenotypes[1]` "Reduced Visual Acuity" `VERY_FREQUENT` cites a meta-analysis
  *aim* statement.
- The THEIA phase 3 trial (PMID:41109232) is cited only for a background
  definition; its actual result is not recorded anywhere in the entry.

### `Glaucoma`

- `pathophysiology[3]` "Trabecular Meshwork Dysfunction" describes age-related
  change, oxidative stress, and ECM alteration, but both evidence items are about
  myocilin — a different mechanism. The `PARTIAL` grade on one is honest; the
  `SUPPORT` on the other is not.
- `treatments[2]` Alpha Agonists: the snippet "IOP reduction was similar for both
  groups" is a *non-difference* result vs timolol; the explanation reads it as
  evidence of "clinically meaningful intraocular pressure lowering."
- `genetic[1]` OPTN is typed `Risk Factor` with notes scoping it to normal-tension
  glaucoma, but the cited snippet says only "associated with primary open angle
  glaucoma" and OPTN E50K is generally treated as causative-dominant.

### `Cytomegalovirus_Retinitis` and `Fuchs_Endothelial_Corneal_Dystrophy` — minor only

- CMV `pathophysiology[2]`: the characteristic morphology claim (yellow-white
  opacification, centrifugal advance) is not in its snippet, which covers only
  rapid progression to blindness.
- Fuchs `pathophysiology[5].evidence[2]`: a textbook statement of what mitochondria
  do in general, cited as a "mechanistic bridge" to FECD apoptosis.
- Fuchs `phenotypes[7]`: Nyctalopia `FREQUENT` comes from an Orphanet HPO
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

1. **`explanation` is unvalidated prose and is where wrong claims hide.** Both
   Tier 1 errors lived there, behind correctly-transcribed snippets. Any review
   protocol that checks snippets without reading explanations will miss them.
2. **Treat mid-clause snippet truncation as a lint target.** A snippet ending in a
   dangling preposition or conjunction (`"…malignancy in"`, `"…highly active
   antiretroviral"`, `"whereas this could not be computed for lower acuities."`) is
   a cheap, mechanically detectable signal of scope-dropping. This would be a
   useful advisory check in `just qc`.
3. **One generic snippet reused across many specific nodes is an anti-pattern.**
   The DR/ICO and RHO cases are both this shape. Reusing a definitional sentence
   as `SUPPORT` for a downstream specific claim should default to `PARTIAL`.
4. **Frequency bands still need their own evidence.** Several `FREQUENT` /
   `VERY_FREQUENT` values here rest on snippets that establish only the
   association, exactly the failure `docs/frequency-evidence-guidelines.md` warns
   about.

## Reproducing

```bash
just validate kb/disorders/RHO-Related_Retinopathy.yaml
just validate-references kb/disorders/Retinoblastoma.yaml
just validate-terms-file kb/disorders/RHO-Related_Retinopathy.yaml
```
