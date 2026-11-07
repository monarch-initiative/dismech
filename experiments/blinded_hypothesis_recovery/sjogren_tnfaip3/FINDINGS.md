# Findings: Sjögren's disease, TNFAIP3 (A20)

Two OpenScientist runs (2026-11-05), one per blinding level, each asked for missing
mechanistic hypotheses for Sjögren's syndrome. Reports are in `reports/`. Scoring follows
the rubric in `README.md`, which was written before either run started.

## Result

Both runs ranked TNFAIP3/A20 as their **first** hypothesis.

| Rubric item | blind | semi |
|---|---|---|
| 1. Gene recovered (rank) | Yes (1 of 10) | Yes (1 of 9) |
| 2. A20 as NF-κB brake, loss → inflammation | Yes | Yes |
| 3. One hypothesis links gland pathology *and* lymphoma | Partly: germline A20 hypofunction in gland-resident B cells, then a somatic second hit, then MALT lymphoma. The salivary epithelium plays no part. | Yes, but the epithelial step is stated as inference with no citation. |
| 4. Reference PMIDs cited (of 4) | 0. Cites 24097066 (Han Chinese GWAS confirming TNFAIP3), 19006194 (somatic 6q23.3 A20 deletion in salivary MALT), 22382892. | 1 (24159176, the French cohort). Also cites 22207688, 27452667, 19608751. |
| 5. Therapeutic direction | Act downstream (BTK inhibition), explicitly *not* restoring A20 | Restore A20 or inhibit NF-κB downstream |
| 6. Citation validity | 22 of 22 PMIDs verified, confabulation rate 0.0 | 16 of 16 verified, confabulation rate 0.0 |

## What this does and does not show

- **The core hypothesis can be found in the literature without being told it.** A
  germline A20 hypomorph plus a somatic second hit, driving NF-κB-dependent MALT lymphoma,
  came out on top even with no direction. TNFAIP3 is a well-studied lymphoma gene in this
  disease, so recovering it is a low bar. This run cannot say whether a less-known
  hypothesis would be recovered.
- **Neither run found the piece Biomni adds:** that A20 loss *in salivary epithelium alone*
  causes gland disease in mice (PMID:30067782). The blind run says outright that no
  A20-conditional Sjögren's mouse was identified. The semi run proposes an epithelial role
  but does not cite this paper, so the epithelial half of the hypothesis is Biomni's
  contribution here.
- **Effect sizes.** The semi run quotes OR 3.36 from the larger cohort. Biomni's panel
  quoted OR ~6.0, which comes from the early-onset subgroup of a smaller cohort
  (`reference_claims_check.md`).
- **Direction differs between runs.** Restoring A20 versus acting downstream is a judgement
  about druggability, not a finding. Neither report treats it as established.
- **One disease and one run per level.** The semi hint (epithelium-driven inflammation plus
  MALT lymphoma) points strongly at this hypothesis; since the blind run reached the same
  rank-1 answer, the hint did not decide the outcome here.

## Leads not in dismech or the Biomni panel

These are candidates for the curation pilot, not checked findings: GTF2I (largest non-HLA
risk locus, OR ≈ 2.2), TNFSF13B/BAFF (BAFF-var lymphoma risk; transgenic mice reproduce
sialadenitis), MALT1 and BCL10 translocations (mutually exclusive with A20 loss in MALT
lymphoma), TNIP1/ABIN-1, GPR34, NCR3/NKp30, IL7/IL7R, CXCL13/CXCR5, TLR7, IKZF1, IL12B.
