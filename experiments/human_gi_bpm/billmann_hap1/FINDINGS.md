# Findings: BPM mining on the Billmann 2026 HAP1 genetic interaction map

**Run date:** 2026-09-16.
**Inputs:** Billmann, Costanzo et al. Cell 2026 supplement (File_S4 qGI/FDR
matrices, File_S11 SAFE region assignments; CC BY 4.0), fetched 2026-09-16 via
`../fetch_billmann.py`. dismech gene sets extracted from the KB at commit
`6706fa11f`.
**Outputs:** [`bpms_annotated.tsv`](bpms_annotated.tsv) (the module pairs),
[`dismech_overlap.tsv`](dismech_overlap.tsv) (gene → disorder long form).
**Parameters:** as committed in `../bpm_search.py` (standard significance
|qGI|>0.3 & FDR<0.1; stringent seeds |qGI|>0.6 & FDR<0.01; profile-PCC floors
0.2/0.3; module size 3–25; Jaccard pruning 0.66).

## Headline numbers

- 9,186 stringent negative seed pairs → 1,664 raw module pairs → **105 BPMs**
  after Jaccard pruning; these collapse to **10 query-side families**
  (A-module Jaccard ≥ 0.66), so the diversity convention of the yeast papers
  substantially overstates distinct biology on a 222-query map.
- Functional coherence against the paper's own SAFE bioprocess regions
  (≥50% of a module's annotated genes in one region): **38/105 coherent on both
  sides** — 29 different-process (the compensatory-pathway signature), 9
  same-process. 45 coherent on one side, 22 neither.
- **94/105 BPMs contain at least one dismech-curated disease gene; 39 have
  curated genes on both sides.**

## Examples worth a curator's attention

**OXPHOS × mTORC1-suppressor machinery (BPM0058, and family).** The ATP
synthase / complex I module (ATP5J, ATP5L, ATPAF2, NDUFA2; SAFE
"Mitochondrial function" 1.0) sits opposite a module containing the GATOR1
complex (DEPDC5, NPRL2), SZT2 (KICSTOR), TSC2 and STK11 (SAFE "Cell
proliferation" 1.0): losing ATP production and losing an mTORC1 brake is
synthetic-sick in HAP1. The B-side genes map to the dismech mTORopathy family —
DEPDC5-Related Epilepsy, Familial Focal Epilepsy With Variable Foci,
SZT2-Related DEE, Focal Cortical Dysplasia Type II, Tuberous Sclerosis
Complex, Peutz-Jeghers syndrome — where mTORC1 hyperactivation is already the
curated mechanism. A human-cell energy-supply dependency of that mechanism is a
plausible `discussions` lead (`kind: KNOWLEDGE_GAP`) for those entries, not
evidence.

**OXPHOS × NGLY1–NFE2L1 axis (BPM0061).** The same OXPHOS module against a
module containing NGLY1 and NFE2L1 (plus VPS35, TIMM10B, SLC25A25). NGLY1
deglycosylates NFE2L1 to license proteasome bounce-back; a negative genetic
dependency between that axis and mitochondrial ATP supply is directly relevant
to the curated `NGLY1-congenital disorder of deglycosylation` entry, whose
mitochondrial phenotypes are an active research area.

**Anti-apoptotic paralog buffering (top family).** The highest-scoring family
pairs a GSK3A/GSK3B-containing query module against modules recurrently
containing BCL2, BCL2L2 and MCL1 plus mTORC1/Ragulator components (RRAGA/C,
LAMTOR4/5, RPTOR) and the CCC/retromer complexes — GSK3 paralogs on one side
and redundant anti-apoptotic BCL2-family members on the other are exactly the
paralog-compensation structure the BPM motif was defined to find.

**Mitochondrial disease genes both sides (BPM0086).** A CDKN2B/GSK3A/NDUFA2
module opposite a coherent mitochondrial gene-expression/CoQ module (COQ2,
TMEM70, MTFMT, FASTKD2, MRPS17, XPNPEP3) — COQ2 (Primary Coenzyme Q10
Deficiency) is curated; TMEM70 and MTFMT are established mito-disease genes.

**Coverage note.** The recurrent OXPHOS query module itself (NDUFA2 — complex I
deficiency; ATPAF2 — ATP synthase deficiency; TMEM70, MTFMT on library side)
consists largely of clinically established mitochondrial disease genes that are
**not yet dismech-curated** — candidate stubs surfaced incidentally.

## Limits of this measurement

- **One haploid cell line.** HAP1 fitness is the only phenotype; a
  compensation visible here may not operate in the disease-relevant tissue
  (the standing `HUMAN_MODEL_MISMATCH` caveat, one step better than yeast).
- **Bipartite bottleneck.** Module A can only draw on 222 query genes, so
  A-side "pathways" are fragments; the 10-family collapse is partly this.
  Within-library-module cohesion rests on profile correlation, not measured
  interactions — a structural assumption the yeast BPM definition does not need.
- **Greedy, not optimal.** No ILP; seeds anchor diversity (the GIDEON
  centering analog) but scores are not comparable to GIDEON's and no
  head-to-head with LocalCut/Liany-ILP was attempted. The DI reweighting was
  not reimplemented: qGI scores are already residuals against a
  wild-type-calibrated expectation, which occupies the same methodological
  slot.
- **Predictions, not evidence.** Same epistemic status as the yeast BPMs: leads
  for `discussions`/`proposed_experiments`, never `evidence:` items. Nothing
  here cites a publication; using a lead in the KB requires literature support
  through the normal reference workflow.

## Follow-ups this suggests

1. A `discussions` item on the mTORopathy-family entries (starting with
   `DEPDC5-Related_Epilepsy` or `Tuberous_Sclerosis_Complex`) recording the
   OXPHOS dependency lead, cited to Billmann 2026 (the *screen*, which is
   citable) rather than to this run.
2. Stub nominations for the uncurated mitochondrial disease genes above.
   **Resolved 2026-09-16:** all four are now curated — NDUFA2 (MC1DN13)
   independently upstream, and ATPAF2 (MC5DN1), TMEM70 (MC5DN2) and MTFMT
   (COXPD15) as full entries in the follow-up tranche to this pilot
   (issues #11924-#11926).
3. If BPM-style leads prove useful, revisit the `compensates_for` schema
   question flagged in the GIDEON assessment report.
