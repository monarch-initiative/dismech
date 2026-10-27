# How the Complement-ARIE Challenge winners fit dismech

Written 2026-10-14 against dismech `main` at commit `8fe34ebd4`, for issue
[#14176](https://github.com/monarch-initiative/dismech/issues/14176). Source: the
NIH Common Fund
[Complement-ARIE Challenge Prize winner summaries](https://commonfund.nih.gov/complementarie/challengewinnersummaries)
(page last reviewed 2025-11-21), which describe 20 winning proposals for
non-animal models.

This report sits beside [the assay and NAM inventory](nam-methods-inventory-2026-10-13.md)
and its companions. The inventory covers what has already been tried inside
dismech. This report covers one outside source of candidate models and asks,
for each, whether it has a dismech home.

## Summary

- **Four winners have a published model that could be curated into an existing
  entry now**: the miniJoint and the click-chemistry cartilage assay into
  Osteoarthritis, the orofacial epithelial-mesenchymal microplate into
  Cleft Lip/Palate, and the feto-maternal interface organ-on-chip into
  Chorioamnionitis or Preterm Premature Rupture of the Membranes. All four
  entries have no `experimental_models` today.
- **Three more have a published model that needs a decision first.** For the
  ABMACT agent-based model and the CAR T trial-on-chip, the full text has to
  settle which cancer entry they belong to (the published chip is leukaemia,
  not the pancreatic cancer the proposal describes). The OASIS Cell Painting
  hepatocyte screen is a preprint and is only partly disease-specific, which
  makes it fringe in the same way as the ToxCast endpoints.
- **Three have no published model yet** that matches the proposal: the
  Alzheimer blood-brain-barrier chip, the atherosclerosis tissue array, and the
  rheumatoid arthritis synovial organoids.
- **Ten do not fit a disease entry.** Three are not models (E-validation,
  ATHENA-N and the NAMKG registry). Five are platforms published without a
  disease (4D bioprinting, organoid intelligence, the skin equivalent, the
  multi-compartment lymph node chip, the engineered heart constructs). Two are
  disease-agnostic toxicology (DeTox and the canine testis organoid).

The proposals themselves are not citable evidence. Everything below that says a
model "fits" refers to the published paper named in that row, not to the
challenge summary.

## How the table was built

- **Published model.** PubMed was searched on 2026-10-14 by team-member names
  combined with the model's subject. Every PMID below was retrieved from PubMed
  and its abstract read. "None found" means these searches returned no paper
  describing the proposed model; it does not prove that none exists.
- **Target entry.** The `kb/disorders/` or `kb/modules/` file the model would
  attach to, with its count of `experimental_models` (or `computational_models`)
  at the commit above.
- **Type.** `experimental_model_type` (`ExperimentalModelTypeEnum`) or, for
  computational models, `model_type` (`ComputationalModelTypeEnum`). `namo_type`
  is a class in the current NAMO schema (56 classes), or "none" where no class
  fits.
- **Tie.** The row of the "what ties the model to the disease" table in
  [#13602](https://github.com/monarch-initiative/dismech/issues/13602): the
  cells carry the lesion; unaffected cells given the exposure that causes the
  disease; unaffected cells given a risk-factor exposure; unaffected cells given
  the treatment; a wild-type target with a chemical and no disease context.
  "No disease" marks a model published without any disease, which that table
  does not cover.

## The 20 winners

| # | Winner (team captain) | Published model | Target entry (models now) | Type / `namo_type` | Tie | Verdict |
|---|---|---|---|---|---|---|
| 1 | 4D Tissue Fabrication (Gartner, UCSF) | PMID:41807773, bioprinted organoids in a stress-relaxing granular matrix, several tissue types | none | `ORGANOID` / `namo:Organoid` | No disease | Does not fit |
| 2 | Sensor-Enhanced Isogenic Model of Alzheimer's (Barrile, Cincinnati) | None found for Alzheimer disease. PMID:31173718 is a co-authored iPSC blood-brain-barrier chip with patient lines from other neurological diseases | `Alzheimer_Disease` (1) | `ORGAN_ON_CHIP` / `namo:OrganOnChip` | Carries the lesion (patient iPSCs, per the proposal) | No paper yet. Recorded as a proposed experiment on `gap_ad_vascular_to_tau_causal_link`, not as an experimental model ([#14256](https://github.com/monarch-initiative/dismech/issues/14256)) |
| 3 | Agent-based Models for Adoptive Cell Therapy (K. Chen, MD Anderson) | PMID:41673469, ABMACT agent-based model of CAR-NK therapy | `computational_models` of a lymphoma entry; the abstract names no cancer type, the proposal names B-cell lymphoma | `AGENT_BASED` / none | Computational model | Fits, target needs full text |
| 4 | Cancer Immunotherapy Clinical Trials on a Chip (W. Chen, NYU) | PMID:40595437, immunocompetent leukaemia bone-marrow chip for CAR T screening. No pancreatic version found | A leukaemia entry; the abstract does not name the subtype | `ORGAN_ON_CHIP` / `namo:OrganOnChip` | Carries the lesion, plus the treatment | Fits, target needs full text |
| 5 | Click Chemistry Magic for Drug Screening (Lu, Delaware) | PMID:42011976, osteoarthritic human knee cartilage from knee replacements exposed to triamcinolone. Method: PMID:42120803 | `Osteoarthritis` (2, curated in [#14225](https://github.com/monarch-initiative/dismech/issues/14225)) | `OTHER` (ex vivo explant) / none | Carries the lesion | Fits; curated |
| 6 | DevTox (Tropsha, Predictive LLC) | PMID:40388119, DeTox QSAR models of developmental toxicity | none (no single disease) | `MACHINE_LEARNING` / `namo:QSARModel` | Chemical, no disease context | Does not fit |
| 7 | E-validation (Hartung, JHU CAAT) | PMID:39444208, a proposal for AI-planned validation studies | none | not a model | Not a model | Does not fit |
| 8 | Omics for Liver Toxicity Assessment (Singh, Broad) | PMID:39896617 (bioRxiv preprint), Cell Painting in primary human hepatocytes, 1,085 compounds. Consortium paper: PMID:40971841 | `drug_induced_liver_injury` module (4) | `PRIMARY_CELL_CULTURE` / `namo:TwoDCellCulture` | Exposure that causes the disease, for the hepatotoxic compounds only | Fringe |
| 9 | Facing the Future of Microphysiological Modeling (Johnson, MSU) | PMID:33634122, epithelium over ECM-embedded mesenchyme in a micromachined microplate; SHH signalling blocked by small molecules. Protocol: PMID:34913124 | `Cleft_Lip_Palate` (0) | `CO_CULTURE` / `namo:CoCulture` | Exposure that is a risk factor | Fits |
| 10 | Future Fertility: Mini-Testis (Yin, Reprotox Biotech) | None found for a human model. PMID:41318009 is a canine testicular organoid for environmental exposures | none (no male infertility entry; the spermatogenic failure entries are genetic) | `ORGANOID` / `namo:Organoid` | Chemical, no disease context | Does not fit |
| 11 | Interpreting Brains and Artificial Networks (Ponce, Harvard) | Not sought: the subject is an artificial neural network | none | not a model | Not a model | Does not fit |
| 12 | Machine Learning Assisted HTP Tissue Array (Tan, CU Boulder) | None found | `Coronary_Artery_Disease` (0); no Atherosclerosis entry | `CO_CULTURE` (expected) | Not known | No paper yet |
| 13 | NAMKG registry (Luechtefeld, Insilica) | None found | none | not a model | Not a model | Does not fit |
| 14 | Neuro-Immuno-Cutaneous Skin Equivalent (D. Kaplan, Tufts) | PMID:32627348, skin equivalent with epidermis, dermis, hypodermis, immune cells and induced neural stem cells. No disease or irritant tested in the abstract | `Contact_Dermatitis` (0), only once an irritant study exists | `PRIMARY_CELL_CULTURE` / `namo:ThreeDCellCulture` | No disease | Does not fit yet |
| 15 | Organ-on-a-Chip for Osteoarthritis Pain (H. Lin, Pittsburgh) | PMID:35436042 and PMID:36830751, the miniJoint: MSC-derived osteochondral, synovial-like and adipose tissues in a microfluidic bioreactor, inflamed with IL-1β. The neuron and immune-cell versions in the proposal were not found | `Osteoarthritis` (2, curated in [#14225](https://github.com/monarch-initiative/dismech/issues/14225)) | `ORGAN_ON_CHIP` / `namo:OrganOnChip` | Unaffected cells given an exposure (IL-1β) that stands in for the cause | Fits, with `CAUSE_UNREPRESENTED`; curated |
| 16 | Organoid Intelligence (Smirnova, JHU) | PMID:40819006, learning and memory building blocks in neural organoids | none | `IPSC_DERIVED_MODEL` / `namo:Organoid` | No disease | Does not fit |
| 17 | Organoid Modeling of RA Joints (Rao, Brigham and Women's) | None found | `Rheumatoid_Arthritis` (0) | `ORGANOID` / `namo:Organoid` | Carries the lesion (patient cells, per the proposal) | No paper yet. Recorded as a proposed experiment on the `Rheumatoid_Arthritis` treatment-response knowledge gap, `gap_ra_treatment_response_prediction` ([#14257](https://github.com/monarch-initiative/dismech/issues/14257)) |
| 18 | Population Diversity in Vaccine Responses (Pompano, UVA) | PMID:39661075, a multi-compartment chip with murine lymph node slices; no brain or adipose compartment, no infection | none | `OTHER` (ex vivo slice) / none | No disease | Does not fit yet |
| 19 | Pregnancy on Chip (Menon, UTMB) | PMID:33112317, four-chamber feto-maternal interface organ-on-chip (decidua, chorion, amnion) with LPS as ascending infection; PMID:37249377, same chip with cigarette smoke extract as oxidative stress. Also PMID:41106448, environmental chemicals linked to preterm birth. Curated in #14227 | `Chorioamnionitis` (1, LPS paper) and `Preterm_Premature_Rupture_of_the_Membranes` (1, oxidative-stress paper) | `ORGAN_ON_CHIP` / `namo:OrganOnChip` | Exposure that causes the disease (LPS for infection); risk-factor exposure for the chemicals paper | Fits |
| 20 | Pulse of the Future: AI-human MEHC (Yang, North Texas) | Only the image-analysis software (PMID:37672553, Organalysis) and a cardiomyocyte micropattern study (PMID:38699629). No disease model found | none | `IPSC_DERIVED_MODEL` / none | No disease | Does not fit yet |

## Notes on individual rows

**Osteoarthritis gets two different kinds of model.** The miniJoint (row 15)
builds joint tissues from healthy mesenchymal stem cells and adds IL-1β, so the
disease is imposed rather than present; a link from it needs a
`CAUSE_UNREPRESENTED` divergence. The cartilage explants in row 5 come from
knee replacements, so the tissue carries the disease, but dismech has no
`experimental_model_type` or NAMO class for an ex vivo explant and it would be
recorded as `OTHER` with no `namo_type`.

**The orofacial microplate repeats the Akura Twin problem.** Row 9 is a
micromachined plate with no perfusion, the same situation as the liver fibrosis
plate in [the NAMO vocabulary gaps note](data/namo-vocabulary-gaps-2026-10-13.md):
`MicrophysiologicalSystem` is abstract and assumes microfluidics, so
`namo:CoCulture` is the closest binding. The abstract does not say whether the
cells are human, which the curator will need from the full text.

**The pregnancy chip is split across two entries.** LPS on the decidua side
models ascending infection and is attached to `Chorioamnionitis`; cigarette smoke
extract models oxidative stress and is attached to
`Preterm_Premature_Rupture_of_the_Membranes`. There is no Preterm Birth entry.
Neither paper measures rupture, so the links target inflammation, senescence and
oxidative-stress nodes rather than the rupture itself (#14227).

**Two published models are not the proposed model.** In row 4 the team
published a leukaemia chip, not the pancreatic cancer organoid chip they
proposed. In row 10 the team published a canine testis organoid, not a human
one. A canine organoid would need `organism` set to dog, the same species
question the murine tissue slices raised in #9997.

**OASIS belongs with the ToxCast question.** Row 8 screens 1,085 compounds of
mixed toxicity on normal hepatocytes. Only the hepatotoxic compounds give it a
disease tie, so it falls between the "exposure that causes the disease" row and
the "chemical, no disease context" row of #13602, where the ToxCast endpoints in
#12858 also sit. The full study is a preprint.

## Where this agrees with the inventory, and what it adds

The inventory's [list of recurring blockers](nam-methods-inventory-2026-10-13.md#blockers-that-recur-across-the-inventory)
predicts most of the problems above:

| Blocker in the inventory | Winners that hit it |
|---|---|
| No NAMO class for non-perfused plates or ex vivo slices | 5 (cartilage explants), 9 (microplate), 18 (lymph node slices) |
| No structured exposure, dose or donor population on a model | 8 (1,085 compounds), 15 (IL-1β), 19 (LPS and four chemicals); the proposals for 2 (isogenic patient lines) and 18 (donors varying by sex, age, race and obesity) depend on donor information |
| No disease-agnostic assay record | 6, 8, 10 |

Two things here are not in the inventory:

- **Multi-tissue systems.** Rows 15, 18 and 19, and the proposal in row 2,
  couple several tissues in one device. `experimental_models` gives one
  `tissue_term` per model and `namo_type` is single-valued, so a chip with
  decidua, chorion and amnion, or a joint with bone, cartilage, synovium and
  fat, records one tissue.
- **Models with no disease.** Five winners published a platform with no
  disease in it (rows 1, 14, 16, 18 and 20). Under #13602's framing these are not fringe disease
  models; they are not disease models at all, which supports the suggestion in that thread of a
  verdict for "belongs somewhere other than a disease entry".

## Follow-up curation

Each "Fits" row is one curation issue, attaching the named paper's model to the
named entry with `modeled_mechanisms` links and quoted evidence:

1. [x] `Osteoarthritis`: the miniJoint (PMID:35436042, PMID:36830751) and the
   cartilage explants (PMID:42011976), curated in
   [#14225](https://github.com/monarch-initiative/dismech/issues/14225). Both
   link only `Cartilage Matrix Catabolism`: the papers report no macrophage or
   fibroblast crosstalk readouts and no bone readouts.
2. `Cleft_Lip_Palate`: the orofacial microplate (PMID:33634122).
3. [x] `Chorioamnionitis` and `Preterm_Premature_Rupture_of_the_Membranes`: the
   feto-maternal interface chip (PMID:33112317, PMID:37249377), #14227.
4. After a full-text check of the cancer type: ABMACT (PMID:41673469) and the
   leukaemia trial-on-chip (PMID:40595437).

The "No paper yet" rows are worth re-checking when those teams publish.
