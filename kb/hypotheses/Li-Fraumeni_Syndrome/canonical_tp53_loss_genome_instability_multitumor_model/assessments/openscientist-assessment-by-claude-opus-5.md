# OpenScientist hypothesis report review: canonical TP53 loss / genome instability / multi-tumor predisposition

**Provider:** openscientist · **Assessor:** claude-opus-5 · **Verdict:** SUPPORTED

## What the report got right

The central chain is correct and is not in doubt: a germline heterozygous TP53
pathogenic variant, somatic biallelic inactivation, genome instability, and an
early-onset multi-organ cancer spectrum. That chain was handed to the provider
as the seed hypothesis out of this knowledge base, so restating it is not new
support. The report's real contribution is quantitative and spectrum-related,
and four items in it were genuinely missing from the dismech entry:

- **Loss of heterozygosity across the whole spectrum, not one tumor type.**
  Paired tumor-normal sequencing of 17,922 cancer patients puts LOH of the
  germline variant at 96.0% in core LFS spectrum tumors against 45.5% in the
  other tumors of the same carriers (PMID:34240179). The entry's second-hit node
  previously rested entirely on pediatric adrenocortical tumors.
- **Blood-detected TP53 variants are frequently not germline.** In the same
  series, 12 of 50 pathogenic variants (24.0%) were clonal-hematopoiesis derived
  and 4 (8.0%) were mosaic, while 12 of 34 true germline carriers (35.3%) would
  not have been tested under phenotype-based criteria. Nothing in the entry
  recorded either failure mode.
- **Hypodiploid ALL.** Germline TP53 variants are enriched about fivefold in
  childhood B-cell ALL, and 65.4% of carrier cases are hypodiploid against 1.2%
  of non-carriers (PMID:29300620). The entry carried a generic Leukemia
  phenotype with no evidence at all.
- **Allele-specific phenotypes from knock-in mice.** p53R270H/+ and p53R172H/+
  animals develop tumor spectra that differ by allele and from p53+/- mice
  (PMID:15607980). This is the experimental basis for the entry's existing
  gain-of-function node, which previously rested on a human onset gradient and a
  review.

It also surfaced two useful non-canonical p53 arms. The ferroptosis arm was
already curated; the cGAS/STING innate immune arm (PMID:36638783) was not.

## Where it goes wrong

**It cites Petitjean 2007 for gain of function.** The report places
PMID:17401424 under a heading asserting that gain-of-function mutations produce
phenotypes beyond simple loss of function. That paper concludes the opposite:
mutation patterns and tumor phenotype are driven by intrinsic mutagenicity, loss
of transactivation and to a lesser extent dominant-negative activity, and it
states that gain-of-function data are "too scarce and heterogenous" to assess
any impact on tumor development or outcome. A correlation between age at onset
and *degree of transactivation lost* is evidence about the severity of loss of
function. Removing it leaves PMID:15607980 as the report's only real
gain-of-function support.

**Percentages without denominators.** The worst case is "in Brazil, 100% of CPCs
carry R337H", which is 2 of 2 choroid plexus carcinomas in a 57-tumor regional
series (PMID:32671623); the companion "100%" for adrenocortical tumors is 3 of
3. The report also reports 96% LOH and 36.4% germline TP53 in choroid plexus
carcinoma without noting that the denominators are small enough to make the
confidence intervals very wide (79.7–99.9% in the first case, 11 tested patients
in the second).

**A mislabelled cohort.** The evidence matrix records the TP53 PIN3 modifier
study (PMID:19542078) as "French LFS families". It is a Brazilian LFS/LFL series
of 135 patients, of whom 32 were TP53 carriers; the 19-year onset difference
compares 25 A1A1 carriers against 7 A1A2 carriers. The adjacent MDM2 haplotype
row (PMID:23884452) is the French one.

**An unreconciled spectrum boundary.** The report quietly moves lung cancer from
the seed's LFS-defining spectrum to an "extended spectrum" without saying so.
Its own key spectrum source found lung, colon, bladder, prostate, cervix and
ovary carcinomas not in excess (PMID:11498785), while the ascertainment-corrected
pedigree analysis already cited in the dismech entry reports elevated lung,
colorectal, gastric, pancreatic and ovarian risk. That is a live disagreement,
not a settled placement.

**Nothing is auditable.** The report asserts "20 confirmed findings, 37 evidence
items, 115+ papers reviewed across 5 investigative iterations" and embeds four
figures. The citation sidecar lists 34 PMIDs, the evidence matrix has 30 rows,
the numbered findings skip F011, F012 and F014, and no artifact bundle exists in
the hypothesis directory, so none of the figures can be inspected. No search log,
screening table, or exclusion list is committed, which also means the
negative-existence claim in knowledge gap 7 (that MILI is the only registered RCT
in LFS) cannot be reproduced.

## Integration into the disease YAML

Target: `kb/disorders/Li-Fraumeni_Syndrome.yaml`. All additions derive from
RETAINED or QUALIFIED claims, and every snippet was re-derived from the local
reference cache rather than copied from the report.

Added:

- `pathophysiology` → *Loss of Heterozygosity (Second Hit)*: PMID:34240179
  evidence (96.0% versus 45.5%), plus a description sentence recording that the
  second hit is spectrum-dependent rather than absolute.
- `pathophysiology` → *Mutant p53 Stabilization and Gain-of-Function*:
  PMID:15607980 evidence, graded MODEL_ORGANISM.
- `pathophysiology` → *Tumor Development*: PMID:11498785 evidence for the
  tissue-selectivity claim the node's description already made unsourced.
- `pathophysiology` → new node *Loss of cGAS/STING Innate Immune Activation*,
  bound to GO:0140896 with `modifier: DECREASED`, with a `downstream` edge from
  *TP53 Tumor Suppressor Loss* and to *Tumor Development*, evidence
  PMID:36638783 graded IN_VITRO. The description states that the arm was defined
  in cell and mouse systems and points at the discussion recording that gap.
- `phenotypes` → *Choroid Plexus Carcinoma*: PMID:21990040 evidence (this
  phenotype previously had none).
- `phenotypes` → *Leukemia*: PMID:29300620 evidence plus a description extension
  covering the hypodiploid subtype (this phenotype previously had none).
- `genetic` → *TP53*: PMID:19542078 evidence for the PIN3 and MDM2 modifier
  claims that the `notes` already asserted without a citation, with the Brazilian
  cohort and the subgroup sizes stated.
- `biochemical` → *TP53 Genetic Testing*: PMID:34240179 evidence and a `notes`
  extension on clonal-hematopoiesis and mosaic misclassification and on
  under-ascertainment by phenotype-based criteria.
- New `discussions` block (the entry had none) with four entries:
  `lfs_tissue_specificity_mechanism` (KNOWLEDGE_GAP),
  `lfs_blood_tp53_variant_interpretation` (KNOWLEDGE_GAP),
  `lfs_metformin_mechanism_unresolved` (KNOWLEDGE_GAP), and
  `lfs_cgas_sting_human_validity` (HUMAN_MODEL_MISMATCH).

Qualified in place:

- The *Choroid Plexus Carcinoma* description's unsourced "approximately 50% of
  CPC patients" became "roughly 36-50% of tested CPC patients across small
  single-centre series", which is what the available series support.

Deliberately not changed:

- **`mechanistic_hypotheses` status stays CANONICAL.** The report's own
  recommendation is to retain it, and its six qualifications concern
  elaborations rather than the central chain. Its `notes` already record the
  dominant-negative, modifier and non-canonical-effector refinements.
- **No ferroptosis change.** The entry already curates *Loss of Ferroptosis
  Surveillance* citing PMID:25799988. The report's stronger framing, that the
  canonical effectors "may be dispensable" and emphasising them is
  "mechanistically misleading", rests on a xenograft readout with a 3KR allele
  and is not a basis for demoting the canonical arms.
- **Nothing added for gain of function from PMID:17401424**, for the reason
  given above.
- **The Brazilian R337H proportions were not tightened.** The entry's existing
  hedged figures are better supported than the report's "100%".
- **No penetrance or surveillance edits.** PMID:27496084 and PMID:27501770 are
  already cited, with the same figures the report reports.
- **No metformin mechanism was removed.** The OXPHOS rationale has its own mouse
  and human evidence in the entry; the unresolved question is which of
  metformin's activities produces the chemopreventive effect, and that is now
  recorded as a discussion rather than by deleting curated content.
- **No lung-cancer spectrum edit.** The disagreement between PMID:11498785 and
  the pedigree analysis already cited in the entry is noted inside the
  tissue-specificity discussion; resolving it is a curation decision that needs
  its own sourcing pass, not a side effect of this review.
