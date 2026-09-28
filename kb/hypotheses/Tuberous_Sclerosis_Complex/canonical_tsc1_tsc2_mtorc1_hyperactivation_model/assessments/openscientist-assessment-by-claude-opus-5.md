# OpenScientist report assessment — canonical TSC1/TSC2/mTORC1 hyperactivation model

**Assessor:** claude-opus-5 · **Assessed:** 2026-09-02
**Report:** `../openscientist.md` (564 lines, 41 cited PMIDs, run 2026-05-25)
**Verdict:** PARTIALLY_SUPPORTED

## What the report is, and is not

The core axis — TSC1/TSC2 loss of function → Rheb-GTP → constitutive mTORC1
activation → hamartomas — is the seed hypothesis handed to the provider. The run
returned it unchanged. Nothing about the axis is newly supported by this report,
and treating its confident language ("among the most thoroughly validated
monogenic disease mechanisms in human genetics") as new evidence would be
circular.

What the run did produce is the boundary of that axis: seven qualifications,
each attached to a real paper, most of which the dismech entry did not carry.
Those are the reason the report is worth reading, and they are what I checked.

## Source verification

I re-fetched and read 19 of the 41 cited PMIDs against the local reference
cache. Every PMID I checked resolves, and the titles match what the report says
they contain — including the high-numbered 2025–2026 identifiers that looked
suspicious at first glance. The quantitative claims are, with one class of
exception, accurate: 94% biallelic loss and median 4 other somatic mutations
(PMID:27494029), −5.6 IQ points with 95% CI −12.3 to 1.0 (PMID:31217257), 31%
ASD irrespective of treatment arm (PMID:41061327), 20% pre-seizure trajectory
abnormalities and 21% seizure-free ASD risk (PMID:32705817), 72% yield with
10/13 mosaic (PMID:39352229).

The exception is the Phase III trial table, where three rows attach the right
numbers to the wrong trial names:

| Report says | The cited paper actually is |
|---|---|
| EXIST-2, angiomyolipoma, PMID:24729041 | the angiomyolipoma **subgroup of EXIST-1** (NCT00789828). EXIST-2 is NCT00790400. |
| EXIST-1, SEGA 65–79%, PMID:23325902 | the open-label extension of **phase 1-2 trial NCT00411619** |
| EXIST-1, 35% vs 0%, PMID:23231513 | a **drug-profile review**, not a trial report |

Nothing is fabricated — the figures are correct for their real sources — but a
curator copying "EXIST-2" out of that table would cite the wrong study. This is
the one claim I marked REJECTED.

Two further overreaches, both marked QUALIFIED rather than rejected because the
underlying results are real:

- **"Rapalogues are cytostatic, not curative … traceable to paradoxical
  autophagy induction."** PMID:30192751 does show angiomyolipoma volume
  rebounding off drug (median −70.6% at discontinuation → −50.6% a year later,
  5/16 evaluable patients progressing). But the same abstract concludes "there
  was no evidence of rapid regrowth", and no citation anywhere in the report
  supports the autophagy attribution. The cytostatic conclusion survives; the
  mechanism is provider inference.
- **"mTORC2 drives LAM-specific pathology … insensitive to rapamycin."**
  PMID:24395886 establishes rapamycin-insensitive, Rictor-dependent COX-2
  regulation in cultured TSC2-null cells and xenografts. That is a molecular
  finding about COX-2 expression, not a disease-level claim about LAM
  progression — sirolimus does stabilise lung function in LAM.

## Process auditability

The directory contains only the report and its citations sidecar. There is no
`openscientist_artifacts/` bundle, so the "182 papers reviewed, 17 confirmed
findings across 5 investigative iterations" tally, the claim that all citations
were "verified against PubMed abstracts", and the two inline figures
(`plot_2.png`, `plot_3.png`) have no committed execution record. Both analyses
are recorded as `REPORTED_ONLY` / `UNVERIFIABLE`, and the GenCC/ClinGen negative
under "Gap 6" is recorded as `UNVERIFIABLE` rather than `SEARCHED_NO_RESULT`
because no query or date is committed — a report asserting a negative is not the
same as a logged search that returned nothing.

## Integration into the disease YAML

`kb/disorders/Tuberous_Sclerosis_Complex.yaml`. The entry's
`mechanistic_hypotheses` notes already narrated the report's seven
qualifications in prose, carrying one citation for the whole block. The work was
to attach that prose to sources and put each qualification on the node it bears
on. 16 evidence items added, all snippet-verified against the local cache
(154 → 170 verified snippets); no ontology CURIE was added anywhere.

| Where | Added |
|---|---|
| `mechanistic_hypotheses` (canonical model) | PMID:31217257 **REFUTE** (no IQ/autism benefit; refutes the pharmacologic-validation corollary for the neuropsychiatric arm only); PMID:26837766 **REFUTE** (mTOR inactive in half of human mesenchymal tumours; refutes "nearly every organ system") |
| `pathophysiology#Somatic Second Hit at TSC Locus` | PMID:27494029 SUPPORT; PMID:26837766 REFUTE; description scoped to the classic hamartoma classes |
| `pathophysiology#Pulmonary Lymphangioleiomyomatosis Growth` | PMID:24395886 SUPPORT; description records the mTORC2 arm |
| `pathophysiology#mTOR-Driven Gliopathy and Neurovascular Unit Dysfunction` | PMID:26003087 SUPPORT (pre-seizure IL-1beta/CXCL10); PMID:24948799 SUPPORT (oligodendrocyte TSC1 ablation is sufficient for hypomyelination) |
| `pathophysiology#Neuroglial Dysplasia and Cortical Network Disorganization` | PMID:38714540 SUPPORT (SST+ interneuron immaturity in patient tissue) |
| `phenotypes#Cerebral Hypomyelination` | PMID:32954437 SUPPORT — the human IQ/ASD correlate the description already asserted without a source |
| `treatments#Vigabatrin for Infantile Spasms` | PMID:41061327 and PMID:32705817 both REFUTE, against the entry's own prevention rationale, plus a `notes` block separating that failed rationale from the intact infantile-spasms indication |
| `treatments#mTOR Inhibitor Therapy (Everolimus)` | PMID:30192751 SUPPORT for the previously uncited "cytostatic rather than curative" note, quoting the sentence that carries the authors' own limit |
| `inheritance#Somatic Mosaicism` | PMID:39352229 SUPPORT — upgrades "postulated" to a measured 72% yield with 10/13 mosaic |
| new `discussions:` block | `gap_tsc_tand_not_reversible_by_mtorc1_inhibition` and `gap_tsc_mtorc1_independent_arms`, each with evidence and a discriminating experiment |

### Deliberately not changed

- **`status:` stays CANONICAL.** The report recommends retaining it, and the
  qualifications narrow the model's scope rather than displacing it.
- **The EXIST trial table was not used at all.** See above.
- **The autophagy attribution** for rapalogue cytostasis was dropped; only the
  rebound observation was curated, with its own limits.
- **PMID:41789478 (DEPDC5 mosaic organoids)** was not added. Real and as
  described, but it is focal cortical dysplasia, not TSC; promoting it to
  cross-disease validation of the TSC model is provider inference.
- **No proposed ontology term was bound.** The report suggests `CL:0000254` for
  SST+ interneurons, which does not denote one. Following the sweep's cache-only
  constraint and the repo's "no term beats a bad one" rule, the SST+ finding is
  carried as evidence prose instead.
- **No new pathophysiology node** for the RHOA, HMGA2, or mTORC2 arms. Each rests
  on a single study in a model system, none has a human effect-size estimate, and
  a node asserts a mechanism the entry is prepared to defend. They are curated as
  an open knowledge gap instead, which is what the evidence currently supports.
