---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-05-31T05:15:00Z'
end_time: '2026-05-31T05:53:00Z'
duration_seconds: 2280.0
citation_count: 25
notes: >
  Manual deep research was performed from PubMed, PubMed-indexed GeneReviews,
  and local PR/issue context because the provider run did not return an output
  artifact in this environment. No references_cache files were created or
  hand-edited. This file is a curation audit and source map for the existing
  ADCA-I parent scaffold.
---

## Question

Assess the evidence base for a parent dismech entry for autosomal dominant
cerebellar ataxia type I (ADCA-I, `MONDO:0019792`) with `has_subtypes` for SCA1,
SCA2, SCA4, SCA8, SCA17, and SCA36, focusing on nosology, shared mechanism,
diagnosis, management, and content gaps that should be handled in follow-up
subtype curation.

## Output

# Autosomal Dominant Cerebellar Ataxia Type I Manual Deep-Research Note

## Scope

- Parent disease term: `MONDO:0019792` autosomal dominant cerebellar ataxia type I.
- Curation frame: historical Harding clinical class for dominantly inherited
  cerebellar ataxia with extracerebellar features, not a single-gene disorder.
- PR scope: SCA1, SCA2, SCA4, SCA8, SCA17, and SCA36, matching issue #1675.
- Out of scope for this scaffold: SCA3/Machado-Joseph disease and ADCA-II/SCA7,
  which are handled separately in the repo issue set and are not listed in the
  requested `has_subtypes` for PR #2755.

## Search Strategy

Manual PubMed searches checked the following literature groups:

- Harding classification and genetic counseling: `Harding autosomal dominant
  cerebellar ataxias`, `late onset autosomal dominant cerebellar ataxias`.
- Shared repeat-expansion mechanism: `CAG polyglutamine repeat diseases`,
  `spinocerebellar ataxia transcriptional dysregulation`, `polyglutamine
  autosomal dominant spinocerebellar ataxias`.
- Subtype anchors: `Spinocerebellar Ataxia Type 1 GeneReviews`, `Spinocerebellar
  Ataxia Type 2 GeneReviews`, `SCA4 ZFHX3 GGC repeat`, `SCA8 ATXN8OS CTG CAG`,
  `SCA17 TBP CAG repeat`, and `SCA36 NOP56 GGCCTG repeat`.

Two issue/review-suggested PMIDs were corrected during verification:

- `PMID:7181479` is not Harding 1982; it is an antibiotic susceptibility paper.
  The Harding classification article is `PMID:7066668`.
- The review suggestion `PMID:20301489` is not SCA1 GeneReviews; it is glycogen
  storage disease type I. SCA1 GeneReviews is `PMID:20301363`.

## Core Conclusion

ADCA-I is best modeled as a parent-level clinical/mechanistic class. The
existing YAML scaffold is conceptually aligned with the literature: it centers
the class on autosomal dominant repeat-expansion SCAs with progressive
cerebellar degeneration plus extracerebellar involvement. It should remain a
parent scaffold until subtype-level entries can carry detailed repeat thresholds,
phenotype frequencies, diagnostic nuances, and treatment/surveillance detail.

The current PR's minimal shared pathophysiology - repeat expansion, misfolded
protein/proteostatic stress, transcriptional dysregulation, Purkinje-cell
degeneration, and extracerebellar neurodegeneration - is supported by the
literature. SCA4 should be treated as a recently solved ZFHX3 GGC-repeat /
poly-glycine disease, not as an unresolved 16q locus, because multiple 2024
papers and the 2024 GeneReviews entry now support the assignment.

## Curation-Relevant Findings

### Nosology and inheritance

Harding's 1982 clinical classification remains the source of the ADCA-I/II/III
clinical grouping. The Harding paper proposed "a simple classification of the
autosomal dominant cerebellar ataxias" and described extracerebellar associated
features including "dementia, supranuclear ophthalmoplegia, extrapyramidal
dysfunction" (`PMID:7066668`). A companion genetic paper supports autosomal
dominant segregation and counseling logic (`PMID:7334501`).

For the PR scaffold, the parent should not imply one founder mutation or one
uniform phenotype. It should state autosomal dominant inheritance, repeat
instability/anticipation where applicable, and reduced penetrance in specific
subtypes such as SCA8 and lower-range SCA17 alleles.

### Shared repeat-expansion mechanism

The broader polyglutamine/repeat-expansion literature supports a convergent
mechanism across SCA1, SCA2, SCA17, and related SCAs. Stoyas and La Spada list
SCA1, SCA2, and SCA17 among the CAG-polyglutamine disease family and identify
"protein aggregation" and "transcription dysregulation" among recurring
pathologic processes (`PMID:29325609`). Orr and Zoghbi similarly frame unstable
repeat expansion as a cause of inherited ataxias and emphasize altered protein
conformation in neuronal survival (`PMID:17417937`).

More explicit SCA1 work supports transcriptional dysregulation as a strong
follow-up evidence target: `PMID:20628574` reports shared gene-expression
changes in SCA1 model cerebella, `PMID:32964235` links regional Purkinje-neuron
vulnerability to ion-channel gene dysregulation, and `PMID:32306062` summarizes
SCA mechanisms around "ion channel dysfunction and transcriptional
dysregulation."

### Subtype source map

| Subtype | Gene/locus | Source-supported curation notes |
|---|---|---|
| SCA1 | `ATXN1` CAG/polyQ | GeneReviews states SCA1 has progressive cerebellar ataxia, dysarthria, bulbar dysfunction, anticipation, and molecular diagnosis by abnormal ATXN1 CAG expansion (`PMID:20301363`). |
| SCA2 | `ATXN2` CAG/polyQ | GeneReviews supports progressive cerebellar ataxia, slow saccades, pyramidal findings, molecular diagnosis by ATXN2 CAG expansion, supportive management, and autosomal dominant inheritance (`PMID:20301452`). |
| SCA4 | `ZFHX3` GGC/poly-glycine | 2024 studies report SCA4 is caused by repeat expansions in ZFHX3 (`PMID:38035881`, `PMID:38197134`, `PMID:38684900`); GeneReviews supports AD inheritance, ZFHX3 GGC testing, sensory neuropathy, motor-neuron involvement, dysautonomia, and multidisciplinary supportive care (`PMID:39666847`). |
| SCA8 | `ATXN8OS/ATXN8` CTG/CAG | GeneReviews supports slow progression, dysarthria/gait instability, overlapping `ATXN8OS/ATXN8` repeat expansion, reduced penetrance, repeat instability, and supportive care (`PMID:20301445`). Cohort/pathology literature supports variable extracerebellar manifestations (`PMID:31471687`, `PMID:36703300`, `PMID:29916049`). |
| SCA17 | `TBP` CAG/CAA/polyQ | Existing PR evidence uses `PMID:30532692` and `PMID:15989694`. The UK cohort supports TBP CAG-repeat causation, dementia/psychiatric/chorea associations, repeat-size/age-at-onset complexity, and variable penetrance. |
| SCA36 | `NOP56` intronic GGCCTG | The Galician Costa da Morte paper supports NOP56 GGCCTG expansion, late-onset progressive ataxia, sensorineural hearing loss, tongue denervation, and pyramidal signs (`PMID:22492559`). Japanese and UK cohorts support regional frequency and variable motor-neuron/hearing findings (`PMID:22753339`, `PMID:37810464`). Mechanism reviews/model papers support RNA/RAN-translation mechanisms (`PMID:35309140`, `PMID:32375043`). |

### Phenotypes

The parent-level phenotype block should stay conservative. Progressive
cerebellar ataxia and dysarthria are safe parent-level features. Additional
parent-level candidates for later curation include cerebellar atrophy, abnormal
saccadic eye movements, pyramidal signs/spasticity, dysphagia, peripheral
neuropathy, extrapyramidal signs, cognitive impairment, psychiatric symptoms,
and sensorineural hearing loss. These should preferably be subtype-scoped rather
than asserted uniformly at the parent level.

### Diagnosis

The literature consistently supports a clinical-neurologic suspicion followed by
molecular repeat-expansion testing:

- SCA1 GeneReviews: diagnosis by characteristic clinical findings and abnormal
  ATXN1 CAG expansion (`PMID:20301363`).
- SCA2 GeneReviews: molecular genetic testing for abnormal ATXN2 CAG expansion
  (`PMID:20301452`).
- SCA4 GeneReviews: heterozygous abnormal ZFHX3 GGC expansion (`PMID:39666847`).
- SCA8 GeneReviews: heterozygous abnormal `ATXN8OS/ATXN8` repeat expansion
  (`PMID:20301445`).
- SCA17/SCA36: repeat-primed PCR, Southern blot, long-read sequencing, or
  targeted repeat analysis may be needed depending on the locus and local test
  availability (`PMID:30532692`, `PMID:22492559`, `PMID:37810464`).

Parent YAML can mention molecular repeat-expansion testing in a future
diagnosis section, but subtype entries should carry locus-specific thresholds
and methodology.

### Management and treatments

No disease-modifying therapy is established for the ADCA-I parent class. The
most defensible treatment frame is supportive, multidisciplinary management:
physical therapy, occupational therapy, speech-language therapy, fall
prevention/adaptive devices, swallowing assessment for dysphagia, nutrition
support, psychiatric/neuropsychologic support when needed, avoidance of alcohol
or medications that worsen cerebellar function, and genetic counseling.

SCA1, SCA2, SCA4, and SCA8 GeneReviews each support supportive care and
surveillance rather than curative treatment (`PMID:20301363`, `PMID:20301452`,
`PMID:39666847`, `PMID:20301445`). SCA36 review literature discusses emerging
mechanistic therapeutic directions but does not establish an accepted
disease-modifying treatment (`PMID:35309140`).

### Prevalence

Do not add a single global parent prevalence for ADCA-I. The term is a
historical clinical class, and prevalence varies by subtype and founder
population. SCA36 is enriched in specific Japanese, Galician/Spanish, and
British cohorts (`PMID:22492559`, `PMID:22753339`, `PMID:37810464`); SCA17 fully
penetrant alleles were rare in the UK ataxia cohort (`PMID:30532692`); and SCA8
frequency varies with testing strategy, repeat thresholds, and penetrance
interpretation (`PMID:20301445`, `PMID:31471687`). Prevalence should be
subtype-scoped.

## YAML Integration Notes

- The PR's current `has_subtypes` list matches issue #1675 and should remain as
  SCA1, SCA2, SCA4, SCA8, SCA17, and SCA36.
- The SCA4 text should keep `ZFHX3` as the causative gene and describe the
  variant as a GGC repeat/poly-glycine expansion. Older issue comments calling
  the gene unresolved are now obsolete.
- The current pathophysiology graph is directionally sound after prior review
  fixes: extracerebellar degeneration should remain parallel downstream of
  repeat/protein/transcriptional toxicity, not downstream of Purkinje-cell loss.
- Future evidence improvement: replace the current implicit TBP-based evidence
  for transcriptional dysregulation with explicit SCA1/SCA mechanism evidence
  from `PMID:20628574`, `PMID:32964235`, or `PMID:32306062`, after fetching
  caches with `just fetch-reference`.
- Future content expansion: add subtype-scoped phenotypes, a parent diagnosis
  section, and supportive treatment/genetic counseling sections only after the
  relevant PMIDs are cached and exact evidence snippets are verified.
- Do not add a parent prevalence claim unless it is explicitly framed as
  unknown/not estimable and supported by a suitable review; subtype/regional
  prevalence is safer.

## Exact Short Quotes Checked

- `PMID:7066668`: "A simple classification of the autosomal dominant cerebellar ataxias"
- `PMID:20301363`: "SCA1 is characterized by progressive cerebellar ataxia"
- `PMID:20301452`: "slow saccadic eye movements"
- `PMID:20301445`: "SCA8 is inherited in an autosomal dominant manner with reduced penetrance."
- `PMID:39666847`: "SCA4 is inherited in an autosomal dominant manner."
- `PMID:38035881`: "SCA4 is caused by repeat expansions in ZFHX3."
- `PMID:29325609`: "protein aggregation, proteolytic cleavage, transcription dysregulation"
- `PMID:32306062`: "ion channel dysfunction and transcriptional dysregulation"
- `PMID:22492559`: "caused by a GGCCTG repeat expansion in intron 1 of NOP56"
- `PMID:35309140`: "motor neuron-related symptoms like muscular atrophy"
- `PMID:30532692`: "dementia, psychiatric symptoms"

## PMID Set Used

- `PMID:7066668` - Harding 1982 ADCA clinical classification
- `PMID:7334501` - Harding 1981 genetic counseling/aspects of AD late-onset ataxia
- `PMID:17417937` - trinucleotide repeat disorders review
- `PMID:29325609` - CAG-polyglutamine disease nosology
- `PMID:32306062` - SCA1/common SCA pathogenic mechanisms review
- `PMID:20628574` - SCA1 transcriptional dysregulation / ATXN1 function
- `PMID:32964235` - SCA1 Purkinje vulnerability and ion-channel gene dysregulation
- `PMID:20301363` - SCA1 GeneReviews
- `PMID:20301452` - SCA2 GeneReviews
- `PMID:20301445` - SCA8 GeneReviews
- `PMID:39666847` - SCA4 GeneReviews
- `PMID:38035881` - ZFHX3 exonic repeat expansion in SCA4
- `PMID:38197134` - long-read sequencing ZFHX3/SCA4
- `PMID:38684900` - ZFHX3 GGC expansion impairs autophagy
- `PMID:38973251` - SCA4 dysautonomia and motor-neuron signs
- `PMID:31471687` - SCA8 cohort in mainland China
- `PMID:36703300` - SCA8 neuropathology
- `PMID:29916049` - SCA8 PSP/parkinsonism phenotype review
- `PMID:30532692` - SCA17 UK cohort
- `PMID:15989694` - SCA17 reduced penetrance / unstable TBP allele
- `PMID:22492559` - SCA36 Costa da Morte / NOP56 expansion
- `PMID:22753339` - SCA36 Japanese cohort
- `PMID:37810464` - SCA36 British cohort
- `PMID:35309140` - SCA36 review
- `PMID:32375043` - SCA36 repeat toxicity model

## Follow-Up Curation Checklist

- Fetch and cache any new PMIDs before adding them to YAML evidence.
- Add a diagnosis section only with subtype-aware repeat-testing language.
- Add treatments as supportive/multidisciplinary care, not disease-modifying
  therapy.
- Add phenotype expansions as subtype-scoped when possible.
- Revisit SCA17 consolidation as a content-modeling decision; this research
  note does not resolve whether the existing standalone SCA17 YAML should be
  duplicated into the ADCA-I parent or kept as a linked sibling.
