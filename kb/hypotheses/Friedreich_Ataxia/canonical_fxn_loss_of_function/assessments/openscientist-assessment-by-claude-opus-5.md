# OpenScientist report on `canonical_fxn_loss_of_function` — assessment

**Disease:** Friedreich Ataxia · **Provider:** openscientist · **Assessor:** claude-opus-5
**Report:** `../openscientist.md` (569 lines, 31 citations, generated 2026-05-23)
**Verdict:** SUPPORTED

## What the report was asked, and what it could contribute

The seed was the knowledge base's own CANONICAL hypothesis entry, so a verdict of
"strongly supported" was the only plausible outcome and confirming it is not new
information. The report's real value lies in the qualifications it attaches to
that chain, and those are what this assessment concentrates on.

Twenty of the report's 31 citations were fetched into `references_cache/` and
compared against the cached abstract or full text. Every identifier resolved and
none of the quotations was fabricated. That is a better record than several other
reports in this sweep, and it is worth saying plainly.

## The three findings that changed the entry

**Dorsal root ganglion pathology is dual-phase, not purely degenerative.**
Koeppen's systematic neuropathology of 35 FRDA patients (PMID:23334592, full text
cached) states that the ganglion lesion combines developmental hypoplasia with
superimposed atrophy, and that size differences in short-survival cases are more
readily explained by hypoplasia than by loss. The curated DRG node described only
injury and destruction. This is the report's most useful genuinely new
contribution.

**Cardiac pathology is a mitophagy failure.** PMID:41628678 reports that in
heart-specific frataxin-knockout mice, mitochondrial respiration is markedly
impaired and iron aggregates accumulate while oxidative stress does not rise, with
p62 and Parkin accumulating and the lysosomal system dysregulated through the
mTOR-TFEB axis. This sat in the hypothesis `notes` prose but had no presence in
the pathograph.

**Ferroptosis is the DRG effector pathway.** PMID:39243573 and PMID:41579709 were
already cited on the hypothesis entry but nowhere in the causal graph, so the two
tissue-specific effector arms the report argues for were structurally invisible.

## Two places where the report overstated, and the entry had copied it

Both of these are cases where a previous curation pass lifted the report's prose
into the entry more confidently than the primary source allows.

The report says secretable-frataxin gene therapy "rescues both cardiac and
neurological phenotypes in mouse and non-human primate models". PMID:42157962
reports broad protein repletion in mouse and non-human primate, then says "In FA
mouse models, we observed rescue of cardiac and neurological phenotypes".
Phenotype rescue is a mouse result; the primate arm is biodistribution. The report
merges the clauses, and the entry's evidence explanation and hypothesis notes had
inherited the merge.

The report reads the deferiprone trial as demonstrating that Fe-S cluster
deficiency rather than iron excess is the primary neurological lesion.
PMID:25112865 is a 6-month randomized trial whose primary objective was safety and
whose own abstract states that the lack of deterioration in the placebo arm
impaired the ability to detect a protective effect. The dose-dependent worsening
is consistent with the Fe-S reading; it does not demonstrate it.

## One curation lead that is simply wrong

The report's Candidate Ontology Terms offers `CL:0011113` as "DRG proprioceptive
neuron". That CURIE is **spiral ganglion neuron**, a cochlear cell type. The entry
already carries the correct `CL:1001451` sensory neuron of dorsal root ganglion.
Every CURIE acted on here was re-derived from this repository's caches rather than
copied from the report.

## Where the report is internally inconsistent

Two places are worth a reviewer's attention.

Finding F002 presents PMID:26401053 (a transcription *elongation* defect past the
repeat) and PMID:26896803 (which states that deficient transcriptional
*initiation* is the predominant cause of the deficiency, and whose HDAC inhibitor
acts by improving initiation) as concordant support for one silencing model. They
are competing accounts of where the block sits.

Finding F005 is headed "Not Oxidative Stress" and then cites PMID:23169664, which
concludes that the mitochondrial biomineral iron aggregates "probably contribute
to the oxidative stress and pathology observed in the absence of frataxin". That
disagreement is now recorded as a knowledge gap rather than resolved by fiat in
either direction.

## Integration into the disease YAML

Target: `kb/disorders/Friedreich_Ataxia.yaml`.

**Added**

- `pathophysiology` → *Dorsal Root Ganglion Sensory Neuronopathy*: `ferroptosis`
  (`GO:0097707`, `INCREASED`) as a biological process; a description paragraph
  covering the hypoplasia-plus-atrophy dual phase and the ferroptotic effector
  pathway; evidence items PMID:23334592 (HUMAN_CLINICAL) and PMID:39243573
  (MODEL_ORGANISM).
- `pathophysiology` → *Cardiomyocyte Mitochondrial Injury*: `mitophagy`
  (`GO:0000423`, `DECREASED`); a description paragraph on the mTOR-TFEB lysosomal
  axis and the contested oxidative-stress status; evidence item PMID:41628678
  (MODEL_ORGANISM).
- `treatments` → *Omaveloxolone*: a second `target_mechanisms` link to the DRG
  node, with PMID:41579709 (IN_VITRO) for the near-complete rescue of lipid
  peroxidation. The drug previously touched only the shared mitochondrial node.
- Four `discussions` entries, all `KNOWLEDGE_GAP`/`OPEN`:
  `tissue_specific_effector_divergence_frda` (PMID:41628678 SUPPORT,
  PMID:23169664 REFUTE), `cardiac_neurologic_severity_dissociation_frda`
  (PMID:22379112), `neuroinflammation_primary_vs_secondary_frda` (PMID:38631900),
  `somatic_gaa_instability_tissue_selectivity_frda` (PMID:29261783).

**Corrected**

- The PMID:42157962 evidence `explanation` and the hypothesis `notes` no longer
  attribute phenotype rescue to the non-human primate arm.
- The PMID:25112865 evidence `explanation` no longer says the trial *demonstrates*
  that Fe-S cluster deficiency is the primary lesion, and now records the
  placebo-arm limitation the authors state.

**Deliberately not done**

- No `status` change. The report's own Candidate Status section says retain
  CANONICAL, and nothing here challenges it.
- No new `mechanistic_hypotheses` entry for the ferroptosis, mitophagy,
  neuroinflammation, blood-brain-barrier or developmental-hypoplasia "alternative
  models". Each is a downstream or parallel consequence of the same frataxin
  lesion rather than a competing account of the disease, and the first two are now
  represented where they belong, as processes on the tissue nodes they act in.
- No microglial or blood-brain-barrier pathophysiology node. The microglial
  evidence is one mouse single-cell dataset plus patient fibroblasts
  (PMID:38631900, PMID:40308559), and the barrier evidence is a single in vitro
  shRNA knockdown model (PMID:36798283). Both are recorded as gaps or left out
  rather than promoted to graph nodes.
- Nothing added for the FDX2/FXN competition lead. The cryo-EM structure
  (PMID:39632806) is solid, but the therapeutic extension rests on a perspective
  piece (PMID:42150975) with no compound and no in vivo data.
- No change from the NfL biomarker finding (PMID:40498047). The trajectory is
  verified and already curated with appropriately hedged wording; the
  developmental-hypoplasia interpretation is the report's inference, not the
  paper's.
- No change from the stale Cochrane trial-scarcity gap (PMID:27572719, 2016),
  which predates the MOXIe programme the entry already curates.
