# OpenScientist report assessment — wnt_beta_catenin_scc_model

**Disease:** Kindler Epidermolysis Bullosa
**Provider:** openscientist (run 2026-05-23)
**Assessor:** claude-opus-5, 2026-09-02
**Verdict:** PARTIALLY_SUPPORTED

## What the report gets right

The report's organising move — split the hypothesis into a TGF-β arm and a Wnt
arm, note that they have very different evidentiary standing, and argue that SCC
in Kindler syndrome is multi-hit rather than Wnt-initiated — is sound, and the
disease entry already records that reframing from an earlier pass.

Two of its findings are real, checkable, and were genuinely missing from the
entry:

- **The direction paradox.** Carrasco et al. (PMID:38982038) report in one paper
  that FERMT1 expression rises from normal skin through actinic keratosis to
  sporadic cSCC, *and* that kindlin-1 loss increases SCC growth in vivo and in
  spheroids. Because both halves come from the same study, this cannot be
  written off as cross-laboratory variation. Kindlin-1 is not a simple tumour
  suppressor, and the direction of its effect appears to depend on context or
  stage. The entry had cited this paper only for hypoxia and MMP13.
- **The TGF-β direction tension.** PMID:42091340 reports *increased* TGF-β
  signalling and dermal fibroblast activation after epidermal kindlin-1
  deletion, while the canonical model has kindlin-1 loss removing αvβ6-mediated
  TGF-β activation. The report proposes an autocrine-versus-paracrine
  reconciliation without asserting it, which is the right posture. The entry had
  cited this paper only for Gstp1 suppression.

Its structural criticism of the Wnt arm is also fair: Rognoni shows stem-cell
expansion alongside tumour susceptibility but never lineage-traces tumours to
the expanded compartment or shows that blocking Wnt prevents them.

## Where it overreaches

**One gap claim is simply wrong.** The report states that no human Kindler
transcriptomic, proteomic or single-cell dataset has been published. GSE47642 —
a human Kindler-versus-control skin microarray — is curated in the datasets
block of the very entry this report was generated for, and its linked
publication is PMID:24681597, the Rognoni study the report says lacks omics
validation. The narrower point survives (nobody has re-analysed it for Wnt
target signatures, and there is no single-cell study), but this is exactly the
kind of absence assertion that should not become a curated knowledge gap.

**The UniProt argument is an argument from silence, and could not be checked.**
The report leans on UniProt Q9BQL6 annotating the TGF-β role but not the Wnt
role as an "independent indicator" that the Wnt claim lacks consensus. UniProt
is not in this repository's reference cache, no release or retrieval record
accompanies the quoted annotation string, and function-annotation coverage of a
single 2014 mouse-genetics result is a curation-throughput matter rather than a
consensus signal.

**Four general Wnt-SCC citations are uncached and unverified**
(PMID:34345013, PMID:29662191, PMID:32881028, PMID:28945253), and their contexts
— HPV-driven cSCC, keratoacanthoma transition, Lgr6 knockout — are not this
disease.

**The status recommendation is not implementable.** "SUPPORTED" is not a value in
`MechanisticHypothesisStatusEnum`; the report's primary alternative, CANONICAL
with an explicit qualifier, is already what the entry records.

**Auditability is poor.** No `openscientist_artifacts` bundle exists, three
figure placeholders resolve to nothing, and "54 papers reviewed" sits against a
17-PMID manifest plus roughly 14 further PMIDs that appear only in a coverage
table and nowhere in the body.

## Integration into the disease YAML

Changed in `kb/disorders/Kindler_Epidermolysis_Bullosa.yaml` — two entries added
to the `discussions:` section created in the same pass:

1. **`gap_keb_fermt1_direction_paradox_in_scc`** (`kind: CONTROVERSY`), attached
   to this hypothesis and to `phenotypes#Squamous Cell Carcinoma Risk`. Cites the
   PMID:38982038 human-lesion sentence about rising FERMT1 in actinic keratosis
   and cSCC, and proposes a lesion-series experiment mapping kindlin-1 level
   against tumour stage in both settings with titration in a single line to test
   directionality.
2. **`gap_keb_tgf_beta_direction_autocrine_versus_paracrine`**
   (`kind: INTERPRETATION`), attached to this hypothesis. Cites the PMID:42091340
   increased-TGF-β/dermal-fibroblast sentence and proposes a
   compartment-resolved Smad2/3 measurement under germline versus adult-induced
   deletion, which distinguishes a compartmental split from a genuine reversal.

Deliberately **not** changed:

- **`status: CANONICAL`** and the hypothesis `notes`. The notes already state the
  arm asymmetry, the missing Wnt replication, the four parallel mechanisms, and
  the multi-hit reading of the clinical epidemiology. Nothing the report adds
  changes them, and no permissible enum value matches its recommendation.
- **No "no human omics data" knowledge gap.** The claim is contradicted by the
  entry's own `datasets:` block.
- **No new evidence from PMID:7958907 / PMID:18618014 / PMID:31340837 /
  PMID:30248333.** All four were already curated on this hypothesis or on the SCC
  phenotype before this assessment.
- **No UniProt evidence item, and no citation of the four uncached general
  Wnt-SCC papers.** Unverified against a cached source.
