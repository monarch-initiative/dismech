# Juvenile Idiopathic Arthritis Deep Research Fallback

## Provider Attempts

No deep-research provider was invoked for this root-level entry. There
is no existing subtype dismech file for any ILAR category, so this
record was curated **directly from the verified literature already
cached in `references_cache/`** that addresses JIA at the umbrella level.

## Integrated Literature Synthesis

Juvenile idiopathic arthritis (JIA, `MONDO:0011429`) is an umbrella
term for the chronic arthritides of childhood beginning before
16 years of age and persisting for at least six weeks, after exclusion
of infective, traumatic, malignant, and other defined causes. The
International League of Associations for Rheumatology (ILAR) criteria
stratify JIA into seven clinically distinct categories — oligoarticular,
polyarticular rheumatoid-factor-negative, polyarticular rheumatoid-
factor-positive, systemic, psoriatic, enthesitis-related, and
undifferentiated. PMID:29848426 ("Spectrum of Joint Deformities in
Children with Juvenile Idiopathic Arthritis") cites the ILAR
criteria as the operational basis for cohort enrolment in JIA studies.

**Mechanistic axis: autoimmune vs autoinflammatory.** PMID:29037901
frames the heterogeneity directly: "Juvenile Idiopathic Arthritis (JIA)
is characterized with a variable pattern of articular involvement and
systemic symptoms and, thus, it has been classified in several
subtypes." Oligoarticular, polyarticular and RF-positive forms have an
adaptive-autoimmune flavour with HLA-class-II linkage (HLA-DRB1*08,
*01, *04 alleles depending on subset); systemic JIA is dominated by
innate-immune activation with prominent IL-1 and IL-6 signalling.

PMID:38756937 and PMID:39317417 establish the Still's disease continuum
between systemic JIA and adult-onset Still's disease, and define the
modern therapeutic strategy: "The optimal therapeutic strategy relies
on early use of interleukin (IL-1 or IL-6 inhibitors associated to
short duration glucocorticoid (GC)." This is captured here as a
separate `Systemic Autoinflammation (sJIA)` pathophysiology node.

**Synovial mechanism atomic decomposition.** Per the PR review feedback,
the original single `Synovial Inflammation` node has been decomposed
into three atomic nodes connected via `downstream` edges:

1. `Synovial Leukocyte Infiltration` — T-cell and macrophage
   recruitment to the synovial membrane (`UBERON:0002018`,
   `CL:0000235`, `GO:0006955` ABNORMAL).
2. `Synovial Hyperplasia` — synoviocyte proliferation
   (`CL:0000214`).
3. `Cytokine-Mediated Articular Damage` — TNF / IL-1 / IL-6 -driven
   cartilage and bone destruction (`GO:0001816` INCREASED).

**Chronic anterior uveitis** is the major extra-articular complication
of oligoarticular JIA and a leading cause of visual morbidity if
unscreened. It is now captured as a subtype-qualified phenotype
(`HP:0012122` Anterior uveitis, `temporality: CHRONIC`,
`subtype: Oligoarticular`). Acute symptomatic uveitis also occurs in
enthesitis-related JIA but is not the same phenotype.

**Treatment ladder.** NSAIDs (`MAXO:0000221`), intra-articular and
short-course systemic glucocorticoids, methotrexate as the conventional
synthetic DMARD of first choice for polyarticular / extended-
oligoarticular JIA, and biologic DMARDs targeting TNF (etanercept,
adalimumab), IL-1 (anakinra, canakinumab), and IL-6 (tocilizumab),
with IL-1 / IL-6 inhibitors moving earlier in the treatment paradigm
for systemic JIA per the EULAR/PReS recommendations.

## Out of scope for the root entry

- Subtype-specific molecular details and complication profiles
  (macrophage activation syndrome in sJIA, the full spectrum of
  drug-specific dosing and adverse effects, etc.). Scoped as
  follow-up dismech entries per ILAR category.
- Genetic-association detail beyond HLA-DRB1 — additional
  susceptibility loci (PTPN22, IL2RA, IL6, IL10) and the genetic
  overlap with adult rheumatoid arthritis are scoped as follow-up.
- The Still's-disease end of the continuum in adults (adult-onset
  Still's disease) — should be its own dismech entry rather than
  duplicated here.
