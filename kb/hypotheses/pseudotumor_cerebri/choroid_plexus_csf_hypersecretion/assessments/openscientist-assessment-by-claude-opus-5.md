# OpenScientist report assessment: choroid plexus CSF hypersecretion in pseudotumor cerebri

**Provider:** openscientist · **Assessor:** claude-opus-5 · **Assessed:** 2026-09-02
**Verdict:** PARTIALLY_SUPPORTED

## What the report gets right

The report does more than restate the seed. Its useful move is to stop treating
the hypothesis as one claim and split it into three hormonal arms that are
graded separately, because the evidence behind them is not remotely comparable.

The **GLP-1 arm** survives source checking intact and is the best supported.
The rat study demonstrates GLP-1R in choroid plexus by tissue section and cell
culture, shows agonist activation blocked by exendin 9-39, reports reduced
Na+/K+-dependent ATPase activity in choroid plexus cell culture, and shows a
receptor-mediated fall in ICP in hydrocephalic rats. The exenatide RCT lowers
ICP at 2.5 hours, far too fast for weight loss. The meta-analysis of 1,550
patients states plainly that no association was detected between GLP-1 receptor
agonists and body mass index, which is a cleaner statement of weight
independence than the report itself extracts from it.

The **androgen arm** has a real tissue-level mechanism that the disease entry
was missing entirely: human choroid plexus expresses the androgen receptor
alongside AKR1C3, and testosterone raises Na+/K+-ATPase activity in a rat
choroid plexus cell line.

The most valuable thing in the report is the finding that cuts *against* the
seed. In high-fat-diet rats, ICP rose 65% with outflow resistance up 50% and no
change in CSF secretion rate or choroid plexus gene expression. In obese Zucker
rats given testosterone, the secretion rate rose but ICP did not, because
drainage capacity absorbed it. Neither result was in the entry, and together
they are the sharpest available argument that hypersecretion is one arm rather
than the initiating event.

## Where the report misreads its sources

Two errors matter enough to change what gets curated.

**The NKCC1 substitution.** The report says chronic testosterone in lean rats
raised ICP and CSF secretion "associated with increased choroid plexus
Na⁺/K⁺-ATPase activity". The paper attributes it to the Na+,K+,2Cl-
cotransporter NKCC1. Na+/K+-ATPase is the transporter the seed hypothesis
names, so the substitution manufactures agreement between an independent rodent
result and the seed model. The curated evidence item quotes the NKCC1 sentence
as written, and the node description now records that the transporter
attribution is unsettled.

**Exendin-4 and rodent secretion.** The report has exendin-4 reducing
"Na⁺/K⁺-ATPase activity and CSF secretion in rats". The enzyme readout was in
cell culture and what was measured in rats was ICP; no rodent secretion rate
appears in that paper.

## Where the report is one-sided

On 11-beta-HSD1 the report reports the missed primary endpoint and stops. The
same abstract records significant in vivo enzyme inhibition, a significant
within-group fall in the AZD4017 arm, and a serum cortisol:cortisone reduction
that correlated with the fall in lumbar puncture pressure (P = 0.005, R = 0.70).
A negative endpoint in 31 women with demonstrated target engagement is an
underpowered trial, not the "most weakened" arm.

## Provenance

The declared evidence base of 91 papers across five iterations cannot be
reconstructed: the citation sidecar lists 41 PMIDs and the frontmatter records
citation_count 41. Six figures are referenced by placeholder and none is
committed; there is no `openscientist_artifacts/` directory. Three
absence claims (no GenCC/ClinGen entry, no IIH choroid plexus omics, no human
secretion measurement) are recorded as unverifiable rather than as documented
empty searches, because no query or log is committed. The underlying gaps are
credible; the searches behind them are not inspectable.

## Integration into the disease YAML

Changes to `kb/disorders/pseudotumor_cerebri.yaml`:

- **`pathophysiology#Choroid plexus CSF hypersecretion`** — description
  rewritten from two hormonal arms to three, adding the androgen arm and
  recording the unsettled Na+/K+-ATPase versus NKCC1 attribution. Added
  `molecular_functions` bound to `GO:0005391`. Six evidence items added:
  GLP-1R expression and exendin-4 Na+/K+-ATPase suppression (PMID:28835515,
  both IN_VITRO); human choroid plexus AR/AKR1C3 expression and testosterone
  raising Na+/K+-ATPase in a rat choroid plexus cell line (PMID:30753168, both
  IN_VITRO); the in vivo testosterone result quoted as NKCC1 (PMID:37328884,
  MODEL_ORGANISM); and hydrocortisone raising CSF secretion in rats, which is
  the step the 11-beta-HSD1 arm posits (PMID:32036786, MODEL_ORGANISM).
- **`pathophysiology#Metabolic risk background`** — added the insulin- and
  leptin-resistant phenotype in excess of obesity (PMID:33848268) and the IIH
  androgen excess signature distinct from PCOS and simple obesity
  (PMID:30753168).
- **`mechanistic_hypotheses#choroid_plexus_csf_hypersecretion`** — added one
  SUPPORT item (no BMI association in the GLP-1 meta-analysis, PMID:40937960)
  and two REFUTE items (obesity raising ICP via drainage not secretion,
  PMID:37328884; raised secretion without raised ICP when drainage compensates,
  PMID:38273331). `notes` extended to say that the claim of primacy is the
  weakest part of the model. **`status` left at EMERGING**, as the report itself
  recommends.
- **New `mechanistic_hypotheses` entry `glymphatic_isf_dyshomeostasis`**
  (`status: ALTERNATIVE`) — the competing model was named only inside the prose
  of a discussion rationale. Two evidence items: the unifying-model review
  (PMID:41472646) and human DTI-ALPS imaging in 55 patients (PMID:39585390).
  `notes` records that the same imaging study also found choroid plexus volume
  rising with the pressure marker, so it does not discriminate between the two
  models.
- **New discussion `gap_iih_human_csf_secretion_rate_unmeasured`**
  (`kind: HUMAN_MODEL_MISMATCH`) — the secretory arm rests entirely on rodent
  and cell-culture secretion measurements, and the rodent evidence does not
  point one way. Carries a proposed noninvasive CSF production imaging
  experiment with `would_support` / `would_refute` and outcome prose, plus
  evidence from the Zucker-rat study's own fidelity statement and the imaging
  method paper.
- **Existing discussion `gap_iih_venous_stenosis_cause_or_consequence`** —
  rationale extended with the intrinsic/extrinsic split, and two evidence items
  added (the 63/37 split, PMID:30219791; the reversibility criterion,
  PMID:37410913).

Deliberately **not** changed:

- **No inflammatory pathophysiology node.** The human study reports only that
  "distinct inflammatory alterations were observed", with no direction, effect
  size, or analyte in the abstract. The rodent link is narrower than the report
  implies: TNF-alpha raised CSF secretion in control-diet rats only, not in
  high-fat-diet rats. The hydrocortisone half of that result is on-hypothesis
  and was curated; the cytokine half is not yet a node.
- **No intrinsic/extrinsic split of the venous stenosis node.** The
  non-reversal of intrinsic stenosis comes from a review's background sentence,
  not from a measured cohort, and the 63/37 figure is incidental to a study
  about vein of Labbé drainage after stenting. That belongs in the open
  cause-versus-consequence discussion, which is where it went.
- **No status change**, and no scope qualifier for non-obese, male, or
  pediatric IIH — `gap_iih_sex_and_nonobese_predilection` already covers it.
- **The 1991 CSF steroid contradiction (PMID:2061573) was not curated.** Five
  mixed-sex patients by radioimmunoassay, with the authors stating their data
  support no definitive conclusion and no correlation between pressure and
  steroid pattern. It is a real conflict in direction but too thin to place
  against a matched mass-spectrometry cohort.
- **The IIH GWAS (PMID:38528581) was not curated.** Fourteen patients and 30
  controls from one consanguineous village, with the association analysis run
  on 22 people at uncorrected p < 0.01. The CA5A hit is interesting given
  acetazolamide, but this is not evidence.
