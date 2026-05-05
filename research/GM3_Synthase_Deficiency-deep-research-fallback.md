# GM3 Synthase Deficiency Deep Research Fallback

Date: 2026-05-04T13:48Z

## Provider Attempts

- `timeout 180 uv run deep-research-client research --template templates/disease_pathophysiology_research.md --var disease_name=GM3 synthase deficiency --var mondo_id=MONDO:0018274 --var category=Mendelian --provider falcon --output research/GM3_Synthase_Deficiency-deep-research-falcon.md --separate-citations research/GM3_Synthase_Deficiency-deep-research-falcon.md.citations.md`
  - Result: timed out after the bounded 180-second run.
  - Completed artifact: none.
- `timeout 180 uv run deep-research-client research --template templates/disease_pathophysiology_research.md --var disease_name=GM3 synthase deficiency --var mondo_id=MONDO:0018274 --var category=Mendelian --provider openai --output research/GM3_Synthase_Deficiency-deep-research-openai.md --separate-citations research/GM3_Synthase_Deficiency-deep-research-openai.md.citations.md`
  - Result: timed out after the bounded 180-second run.
  - Completed artifact: none.

No provider-generated deep-research narrative completed within the bounded
runtime. Curation therefore proceeded from regenerated structured Orphanet
evidence and sequentially fetched PubMed caches, without hand-editing any
`references_cache/*.md` files.

## Evidence Scope Used For Curation

### Structured Source

- `ORPHA:370933` GM3 synthase deficiency structured record
  - Exact MONDO cross-reference: `MONDO:0018274`
  - Exact OMIM cross-reference: `OMIM:609056`
  - Synonym: ST3GAL5-CDG
  - Inheritance: autosomal recessive
  - Gene assertion: `ST3GAL5`, disease-causing germline loss of function
  - Definition supports impaired complex ganglioside synthesis with early
    irritability, poor feeding, failure to thrive, refractory epilepsy, later
    growth impairment, developmental delay or regression, profound intellectual
    disability, deafness, abnormal skin pigmentation, visual impairment,
    choreoathetosis, and hypotonic tetraparesis.

### PubMed Records

- `PMID:15502825`
  - Original Amish infantile-onset symptomatic epilepsy syndrome report.
  - Supports autosomal recessive disease, truncating SIAT9/ST3GAL5 variant,
    GM3 synthase's role in complex ganglioside biosynthesis, absent GM3 synthase
    activity, absent GM3 ganglioside and derivatives, and increased upstream
    glycosphingolipid species.
- `PMID:18480157`
  - Patient fibroblast study.
  - Supports severe ganglioside depletion, lack of compensatory alternative
    ganglioside synthesis, reduced EGF-induced proliferation and migration,
    reduced EGFR binding, and dampened EGFR activation.
- `PMID:24026681`
  - Salt and pepper syndrome ST3GAL5 paper.
  - Supports severe intellectual disability, epilepsy, choreoathetosis,
    dysmorphic and pigmentation features, ST3GAL5 p.E332K, complete GM3 lack in
    patient fibroblasts, collateral glycolipid and glycoprotein glycosylation
    changes, and increased apoptosis in zebrafish brain regions after st3gal5
    knockdown.
- `PMID:30209782`
  - Human oral ganglioside supplementation study.
  - Supports absence of GM3 and downstream derivatives, severe irritability,
    intractable seizures, profound intellectual disability, oral ganglioside
    enriched dairy supplementation, improved growth and development, transient
    benefit, and need for endogenous ganglioside restoration strategies.
- `PMID:30576498`
  - Variant enzyme-assay paper.
  - Supports ST3GAL5-CDG as a GM3 synthase disorder, failure to thrive and
    severe hearing, visual, motor, and cognitive impairment in a reported
    patient, and complete loss of enzyme activity across pathogenic variants.
- `PMID:34906476`
  - Non-Amish patient cohort.
  - Supports biallelic ST3GAL5 loss of function, 16 affected non-Amish patients,
    severe to profound intellectual disability in all patients, hyperkinetic
    movement disorder in 14 of 16, epilepsy in 11 of 16, microcephaly in 9 of
    16, progressive skin pigmentation anomalies, optic atrophy or pale papillae,
    and hearing loss.
- `PMID:35628171`
  - Review of human disease and mouse models.
  - Supports ST3GAL5/GM3 synthase conversion of lactosylceramide to GM3, neural
    ganglioside biology, human progressive microcephaly, intellectual
    disability, dyskinetic movements, blindness, deafness, intractable seizures,
    pigment changes, and mouse-model limitations.
- `PMID:36833282`
  - Saudi family report.
  - Supports ST3GAL5-associated salt and pepper developmental regression
    syndrome with epilepsy, profound intellectual disability, choreoathetosis,
    scoliosis, pigmentation, dysmorphism, novel homozygous ST3GAL5 variant,
    speech delay, and developmental delay.
- `PMID:37676252`
  - Patient-derived iPSC/neural crest cell study.
  - Supports undetectable GM3 and GM3-derived gangliosides, elevated LacCer
    precursor, altered cell-surface proteome, O-GlcNAcylation, receptor tyrosine
    kinase abundance, increased apoptosis, and EGFR-inhibitor sensitivity in
    GM3SD neural lineage cells.
- `PMID:39119456`
  - Dietary ganglioside supplementation mouse study.
  - Supports absence of GM3 and downstream derivatives, clinical features in
    affected individuals, prior human supplementation improvements, improved
    cognitive function in supplemented GM3 synthase-deficient mice, and
    increased ganglioside levels plus hippocampal neurogenesis.

## Integration Notes

The YAML models GM3 synthase deficiency as a ST3GAL5 loss-of-function
glycosphingolipid biosynthesis disorder. ST3GAL5 encodes lactosylceramide
alpha-2,3-sialyltransferase activity, which produces ganglioside GM3 from
lactosylceramide. Loss of that enzyme depletes GM3 and downstream ganglioside
derivatives, alters broader glycosphingolipid and glycoprotein glycosylation,
and perturbs membrane and receptor signaling in patient-derived neural lineage
cells. The curated phenotype model emphasizes the severe infantile neurologic,
growth, sensory, movement, and pigmentation phenotype supported by Orphanet and
clinical cohorts.

Treatment evidence remains limited. The only disease-directed human treatment
evidence found in the bounded literature scope was oral ganglioside-enriched
dairy supplementation, which reported early growth and developmental
improvements that appeared transient. The YAML therefore avoids a broad
supportive-care treatment claim unless a direct management reference is added,
and records autosomal recessive genetic counseling separately.
