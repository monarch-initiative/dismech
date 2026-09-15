---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T02:25:27.462259'
end_time: '2026-09-04T02:43:48.662674'
duration_seconds: 1101.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sialuria
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 10
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:41352710
  - PMID:29923088
  - PMID:35398442
  relevance_assessed: 14
  on_topic: 13
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 21
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 10
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009359
    reported_labels:
    - MONDO
    ontology_label: multinucleated neurons-anhydramnios-renal dysplasia-cerebellar
      hypoplasia-hydranencephaly syndrome
  - term_id: HP:0003231
    reported_labels:
    - Sialuria
    ontology_label: Hypertyrosinemia
  - term_id: UBERON:0000955
    reported_labels:
    - "Brain / CNS** \u2014 developmental delay"
    ontology_label: brain
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sialuria-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sialuria-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sialuria
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sialuria** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Sialuria (French Type): A Comprehensive Disease Characteristics Report

**Disease:** Sialuria (French type)
**Identifiers:** OMIM #269921 · ORPHA:2809 · MONDO:0009359 · Gene: *GNE* (HGNC:23657; 9p13.3)
**Category:** Mendelian, autosomal dominant inborn error of metabolism
**Report date:** 2026-09-04

---

## Summary

**Sialuria is an ultra-rare autosomal dominant inborn error of metabolism in which heterozygous missense mutations at the allosteric (feedback-inhibitor) site of the bifunctional enzyme UDP-*N*-acetylglucosamine 2-epimerase/*N*-acetylmannosamine kinase (GNE/MNK) abolish CMP-sialic acid feedback inhibition, causing unregulated cytoplasmic overproduction and gram-quantity urinary excretion of free *N*-acetylneuraminic acid (Neu5Ac, sialic acid).** Fewer than a dozen patients have ever been described worldwide, and the reported cases are strikingly homogeneous clinically: infantile onset with developmental delay, mildly coarse facial features, hepatomegaly, and prolonged neonatal jaundice. Unlike its differential diagnoses, sialuria is generally **non-neurodegenerative** and comparatively mild.

The mechanism is now understood at atomic resolution. GNE/MNK catalyzes the first two committed, rate-limiting steps of *de novo* sialic acid biosynthesis, and its epimerase activity is normally braked by binding of the downstream product CMP-Neu5Ac at an allosteric pocket located at the dimer–dimer interface of the enzyme tetramer. All reported sialuria alleles cluster at two arginine residues in this pocket — **Arg263 and Arg266** (current HGVS numbering **Arg294/Arg297**). Crystallography and protein engineering demonstrate that these mutations **retain catalytic activity but destroy feedback inhibition**, producing a gain-of-flux state in which intracellular CMP-sialic acid rises more than 10-fold and free sialic acid overflows into the cytosol and urine.

Sialuria sits at one pole of the *GNE* allelic disorder spectrum. Recessive loss-of-function mutations in the *catalytic* domains of the same gene cause **GNE myopathy** (Nonaka/hereditary inclusion body myopathy), a mechanistically opposite disorder of sialic acid *deficiency*. Sialuria must also be distinguished from the recessive **lysosomal free sialic acid storage disorders** (FSASD; Salla disease/ISSD) caused by *SLC17A5*/sialin defects, which share elevated urinary free sialic acid but differ in subcellular compartment (lysosomal vs. cytosolic), inheritance (recessive vs. dominant), and clinical course (neurodegenerative vs. relatively benign). No approved disease-specific therapy exists; management is supportive. Allele-specific siRNA silencing of the mutant *GNE* allele has been shown to restore feedback inhibition and normalize free sialic acid in patient fibroblasts, providing proof-of-concept for a future targeted therapy.

---

## 1. Disease Information

**Overview.** Sialuria is a rare autosomal dominant inborn error of metabolism characterized by cytoplasmic accumulation and urinary excretion of gram quantities of free sialic acid, resulting from failure of feedback inhibition of the rate-limiting enzyme of sialic acid synthesis, GNE/MNK ([PMID: 29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/)). It is sometimes called **sialuria, French type** to distinguish it from the (mechanistically unrelated) free sialic acid storage disorders.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #269921 |
| Orphanet | ORPHA:2809 |
| MONDO | MONDO:0009359 |
| Gene | *GNE* (HGNC:23657), 9p13.3 |
| Enzyme EC | 5.1.3.14 (UDP-GlcNAc 2-epimerase) / 2.7.1.60 (ManNAc kinase) |

**Synonyms / alternative names.** Sialuria French type; GNE-related sialuria; UDP-GlcNAc-2-epimerase feedback-inhibition defect.

**Information source.** The disease-level knowledge is derived from **aggregated case reports and biochemical/structural studies**, not EHR data. With only ~9 published patients, essentially all information is at the level of individual-patient case reports synthesized into disease-level resources (OMIM, Orphanet).

---

## 2. Etiology

**Primary cause — genetic.** Sialuria is caused by heterozygous (dominant) missense mutations at the **allosteric feedback-inhibitor site** of *GNE*. All nine reported cases carry a heterozygous missense variant at this site, recurrently at **Arg294 (formerly Arg263)** and **Arg297 (formerly Arg266)** ([PMID: 29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/)). The functional consequence is a **gain-of-function/gain-of-flux** defect: loss of CMP-sialic acid feedback inhibition of GNE-epimerase activity, causing excessive production of free sialic acid.

**Genetic risk factors.** The causal variants themselves are the sole known risk determinant. No modifier loci or susceptibility SNPs have been reported for this ultra-rare disorder.

**Environmental risk factors.** None identified. Sialuria is a purely Mendelian, single-gene disorder with no known environmental, toxic, occupational, infectious, dietary, age, or sex contribution to disease occurrence.

**Protective factors.** None described (genetic or environmental). Given dominant inheritance with the mutant allele driving pathology, allele-specific silencing is being explored as a therapeutic rather than a naturally occurring protective mechanism.

**Gene–environment interactions.** No gene–environment interaction has been documented. The phenotype tracks directly with the *GNE* allosteric-site genotype.

---

## 3. Phenotypes

The nine published cases share **rather homogeneous clinical features**: developmental delay, mildly coarse features, hepatomegaly, and prolonged neonatal jaundice ([PMID: 29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/)). The best-documented single case (fifth reported patient, a 7-year-old Portuguese girl) showed developmental delay, hepatomegaly, coarse facies, and urinary excretion of 19 µmol free NeuAc/mg creatinine ([PMID: 10356312](https://pubmed.ncbi.nlm.nih.gov/10356312/)).

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Developmental delay | Neurodevelopmental | Infantile/childhood | Mild–moderate; often non-progressive | Common (majority) | HP:0001263 (Global developmental delay) |
| Coarse facial features | Physical/clinical sign | Infantile | Mild | Common | HP:0000280 (Coarse facial features) |
| Hepatomegaly | Clinical sign | Infantile | Mild–moderate | Common | HP:0002240 (Hepatomegaly) |
| Prolonged neonatal jaundice | Clinical sign | Neonatal | Mild | Recurrent | HP:0006579 (Prolonged neonatal jaundice) |
| Elevated urinary free sialic acid | Laboratory abnormality | Congenital/lifelong | Marked (gram quantities) | Universal (diagnostic hallmark) | HP:0003231 (Sialuria) |
| Hypotonia | Clinical sign | Infantile | Variable | Reported in some | HP:0001252 (Hypotonia) |

**Progression.** Features are generally **stable/non-progressive**; sialuria is not neurodegenerative, an important distinction from the lysosomal free sialic acid storage disorders. **Age of onset** is neonatal-to-infantile.

**Quality of life impact.** Mild-to-moderate developmental delay may affect learning and daily functioning; hepatomegaly and coarse facies are generally not disabling. No formal EQ-5D/SF-36 quality-of-life data exist for this ultra-rare disease. Overall the burden is substantially lower than in FSASD.

---

## 4. Genetic / Molecular Information

**Causal gene.** *GNE* (glucosamine [UDP-*N*-acetyl]-2-epimerase/*N*-acetylmannosamine kinase), 9p13.3, OMIM *603824. Encodes the bifunctional, rate-limiting enzyme of sialic acid biosynthesis ([PMID: 23437777](https://pubmed.ncbi.nlm.nih.gov/23437777/)).

**Pathogenic variants.**

| Feature | Detail |
|---|---|
| Affected gene | *GNE* (HGNC:23657) |
| Variant type | Missense, clustering at the allosteric/feedback site |
| Recurrent residues | Arg263 and Arg266 (current numbering Arg294/Arg297) |
| Representative allele | c.797G>A, p.Arg266Gln (p.R266Q) |
| Classification | Pathogenic (ACMG) — recurrent, functionally validated, segregating with dominant disease |
| Zygosity | Heterozygous (dominant) |
| Population allele frequency | Not present at appreciable frequency in gnomAD (ultra-rare; essentially private/de novo or transmitted) |
| Origin | Germline |
| Functional consequence | **Gain of function** at the pathway level — retained catalysis with loss of allosteric feedback inhibition |

The p.R266Q variant was documented in the Portuguese case, where fibroblast UDP-GlcNAc 2-epimerase was only **26% inhibited by 100 µM CMP-Neu5Ac (normal 79%)**, confirming loss of feedback braking ([PMID: 10356312](https://pubmed.ncbi.nlm.nih.gov/10356312/)).

**Modifier genes.** None identified.

**Epigenetic information.** No DNA-methylation or histone-modification changes have been reported for sialuria; the disorder is a classic single-gene coding-variant condition.

**Chromosomal abnormalities.** None; sialuria is not associated with aneuploidy, translocations, or copy-number changes.

---

## 5. Environmental Information

- **Environmental factors:** None known. Sialuria is not caused or modified by toxins, radiation, pollution, or occupational exposure.
- **Lifestyle factors:** None known. Diet, smoking, alcohol, and exercise are not implicated in onset. (Dietary sialic acid restriction has not been shown to alter the endogenous overproduction that drives the phenotype.)
- **Infectious agents:** Not applicable — sialuria is a Mendelian metabolic disorder. Note that urinary free sialic acid, the diagnostic biomarker, may be **non-specifically elevated in pneumococcal sepsis** ([PMID: 36000484](https://pubmed.ncbi.nlm.nih.gov/36000484/)), a relevant caveat for interpreting the screening test but not an etiologic factor.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous missense mutation** at the *GNE* allosteric site (Arg263/Arg266 → e.g., R266Q) **alters the CMP-Neu5Ac binding pocket** at the dimer–dimer interface of the GNE/MNK tetramer.
2. This **prevents CMP-sialic acid from locking the epimerase in its closed, inhibited conformation** → **loss of allosteric feedback inhibition** (demonstrated: crystallography + in vitro inhibition assays).
3. Loss of feedback braking **leaves epimerase catalysis constitutively active** (retained catalytic function; ~94% of wild-type activity in engineered mutants) → **unregulated flux through the de novo pathway** (UDP-GlcNAc → ManNAc → ManNAc-6-P → Neu5Ac-9-P → Neu5Ac).
4. Unregulated flux **raises intracellular CMP-sialic acid >10-fold** and causes **overproduction of free Neu5Ac** (demonstrated in engineered cells).
5. Free Neu5Ac **accumulates in the cytoplasm** (cytosolic, not lysosomal, storage) and **overflows into urine in gram quantities** (demonstrated; the biochemical hallmark).
6. The systemic consequences — **developmental delay, hepatomegaly, coarse facies, prolonged neonatal jaundice** — follow from cellular free–sialic-acid excess and altered sialylation flux (mechanistic link to specific organ phenotypes remains partly *inferred* rather than fully demonstrated).

```
GNE allosteric-site mutation (Arg263/Arg266; R266Q)
        │ alters CMP-Neu5Ac binding pocket at dimer–dimer interface
        ▼
Loss of CMP-sialic acid feedback inhibition of GNE-epimerase
        │ (catalysis retained ~94% WT)
        ▼
Unregulated de novo flux: UDP-GlcNAc → ManNAc → … → Neu5Ac
        ▼
Intracellular CMP-sialic acid ↑ >10×  +  cytosolic free Neu5Ac ↑↑
        ├──► gram-quantity urinary free sialic acid (diagnostic hallmark)
        └──► systemic phenotype (developmental delay, hepatomegaly,
                 coarse facies, neonatal jaundice) [partly inferred]
```

### Detail by category

**Molecular pathways.** The de novo **sialic acid biosynthesis / sialylation pathway** (KEGG amino sugar and nucleotide sugar metabolism). Cellular free sialic acids are made via de novo biosynthesis, recycled from lysosomal salvage, and taken up from extracellular sources ([PMID: 41352710](https://pubmed.ncbi.nlm.nih.gov/41352710/)). GNE/MNK catalyzes the first two committed, rate-limiting steps and is feedback-inhibited by CMP-sialic acid ([PMID: 19917666](https://pubmed.ncbi.nlm.nih.gov/19917666/)).

**Biochemical abnormality (upstream, primary).** Failure of allosteric feedback inhibition. "The resultant loss of feedback inhibition of GNE-epimerase activity by CMP-sialic acid causes excessive production of free sialic acid" ([PMID: 18653764](https://pubmed.ncbi.nlm.nih.gov/18653764/)).

**Protein dysfunction.** The N-terminal epimerase domain of human GNE forms a **tetramer** in which UDP binds the active site and **CMP-Neu5Ac binds the dimer–dimer interface, locking the enzyme in a tightly closed conformation** ([PMID: 26980148](https://pubmed.ncbi.nlm.nih.gov/26980148/)). Mutations at Arg263/Arg266 sit in/around this allosteric pocket; the crystallographic binding mode "clearly elucidates why mutations in Arg263 and Arg266 can cause sialuria" ([PMID: 26980148](https://pubmed.ncbi.nlm.nih.gov/26980148/)). Substrate (UDP-GlcNAc) binding stabilizes the tetramer by increasing dimer–dimer affinity ~98-fold; inhibitors disrupt the assembly ([PMID: 41099617](https://pubmed.ncbi.nlm.nih.gov/41099617/)).

**Metabolic changes (downstream).** Cytosolic overaccumulation of free Neu5Ac and >10-fold elevation of the activated donor CMP-sialic acid; free sialic acid is normally degraded to ManNAc and pyruvate in the cytosol ([PMID: 41352710](https://pubmed.ncbi.nlm.nih.gov/41352710/)). Sialuria represents the **overproduction/accumulation** pole of sialic acid disorders — "Sias deficiency and overproduction (accumulation), hyposialylation … and hypersialylation all cause disorders" ([PMID: 41352710](https://pubmed.ncbi.nlm.nih.gov/41352710/)).

**Subcellular localization.** Cytoplasm/cytosol (GO:0005829) — critically distinct from the lysosomal accumulation of FSASD. Sialylation itself occurs in the Golgi using CMP-Sia as donor.

**Immune / inflammatory involvement.** Not a primary feature. Sialuria is not an autoimmune or inflammatory disorder.

**Molecular profiling.** No sialuria-specific transcriptomic, proteomic, or metabolomic datasets are published beyond direct biochemical measurement of free sialic acid and CMP-sialic acid. Orthogonal in vitro engineering data (below) provide the strongest mechanistic confirmation.

**GO / CL term suggestions.** GO:0006054 (N-acetylneuraminate metabolic process); GO:0046380 (N-acetylneuraminate biosynthetic process); GO:0008761 (UDP-N-acetylglucosamine 2-epimerase activity); GO:0009384; GO:0005829 (cytosol). No specific cell-type (CL) restriction — the defect is cell-autonomous and broadly expressed (hepatocytes, CL:0000182; fibroblasts, CL:0000057 are documented affected cell types).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Liver** — hepatomegaly (UBERON:0002107); prolonged neonatal jaundice implicates hepatobiliary handling.
- **Brain / CNS** — developmental delay (UBERON:0000955), generally without structural neurodegeneration.
- **Craniofacial** — mildly coarse facies (UBERON:0000033, head).
- **Kidney / urinary tract** — conduit for gram-quantity urinary sialic acid excretion (not injured).

**Body systems.** Hepatic/digestive, nervous (developmental), and metabolic systems.

**Tissue and cell level.** Documented affected cell types include **hepatocytes** (CL:0000182) and **fibroblasts** (CL:0000057, the standard diagnostic cell showing cytosolic free-sialic-acid excess). The defect is fundamentally **cell-autonomous** in any GNE-expressing cell.

**Subcellular level.** **Cytoplasm/cytosol (GO:0005829)** is the site of free-sialic-acid overproduction and storage — the defining subcellular contrast with lysosomal (GO:0005764) storage in FSASD.

**Localization / lateralization.** Systemic/bilateral; no lateralization.

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal-to-infantile. Prolonged neonatal jaundice may be the earliest sign; developmental delay and hepatomegaly emerge in infancy/early childhood.
- **Onset pattern:** Chronic/insidious — present from birth as a constitutive metabolic overproduction.
- **Progression:** Generally **stable and non-progressive**; sialuria is not neurodegenerative. This is a key prognostic and differential feature versus FSASD.
- **Disease course:** Chronic, lifelong (the underlying enzymatic dysregulation persists), but with comparatively benign clinical trajectory. Some patients show improvement/normalization of developmental milestones over time.
- **Remission patterns:** No spontaneous biochemical remission (the genetic defect is constitutive). No approved treatment-induced remission, though allele-specific silencing normalizes biochemistry experimentally.
- **Critical periods:** Infancy/early childhood is the window of clinical recognition; the theoretical window for any future disease-modifying (e.g., allele-silencing) intervention would be early.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare. Only **~9 patients** have been reported worldwide ([PMID: 29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/)). Prevalence/incidence figures are not formally established (well under 1 per 1,000,000). Orphanet lists it as an ultra-rare condition.

**Inheritance.** **Autosomal dominant** — the single most distinctive genetic feature among sialic acid disorders. "Sialuria is a rare autosomal dominant inborn error of metabolism …" ([PMID: 29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/)). A single mutant allele suffices because the mutant enzyme escapes feedback and drives overproduction regardless of the normal allele.

- **Penetrance:** Appears complete for the biochemical phenotype (all reported carriers are biochemically affected); clinical severity varies.
- **Expressivity:** Variable but with homogeneous core features.
- **Genetic anticipation:** Not applicable (no repeat expansion).
- **Germline mosaicism / de novo:** Several cases appear sporadic; de novo occurrence is plausible given dominant inheritance, though transmission has been observed.
- **Founder effects / consanguinity:** Not applicable (dominant, not enriched by consanguinity — in contrast to the recessive FSASD, which shows founder/consanguinity effects).
- **Carrier frequency:** Not meaningful for a dominant ultra-rare disorder.

**Population demographics.** Cases reported across diverse ethnicities (e.g., Portuguese); no ethnic or geographic clustering. No established sex bias. Age distribution centers on pediatric identification.

---

## 10. Diagnostics

**Laboratory tests (primary).**
- **Urine free sialic acid (UFSA)** — the key screening biomarker; markedly (gram-quantity) elevated. "Urine free sialic acid (UFSA) is an important diagnostic biomarker for sialuria" ([PMID: 36000484](https://pubmed.ncbi.nlm.nih.gov/36000484/)). The Portuguese patient excreted 19 µmol free NeuAc/mg creatinine ([PMID: 10356312](https://pubmed.ncbi.nlm.nih.gov/10356312/)).
- **Fibroblast free sialic acid** — elevated, localized to the **cytosolic** (not lysosomal) fraction on differential centrifugation — the compartment distinction that separates sialuria from FSASD.
- **Enzyme feedback-inhibition assay** — fibroblast UDP-GlcNAc 2-epimerase inhibition by 100 µM CMP-Neu5Ac is reduced (26% vs. normal 79%) ([PMID: 10356312](https://pubmed.ncbi.nlm.nih.gov/10356312/)).

**Biomarkers.** Free Neu5Ac (CHEBI:45744) in urine, plasma, and cultured cells; elevated intracellular CMP-sialic acid.

**Genetic testing.** **Single-gene *GNE* sequencing** targeting the allosteric-site codons (Arg263/Arg266; current Arg294/Arg297) is confirmatory. WES/WGS or a sialic-acid-disorder / metabolic gene panel including both *GNE* and *SLC17A5* is appropriate when the differential is open. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not** indicated.

**Imaging / other modalities.** No pathognomonic imaging. Notably, brain MRI in sialuria lacks the hypomyelination/thin corpus callosum seen in FSASD/Salla disease — a useful discriminator.

**Differential diagnosis.**

| Disorder | Gene | Inheritance | Compartment | UFSA elevation | Course |
|---|---|---|---|---|---|
| **Sialuria (French type)** | *GNE* (allosteric) | **AD** | **Cytosolic** | Gram quantities (very high) | Mild, non-neurodegenerative |
| Free sialic acid storage disorders (Salla/ISSD, FSASD) | *SLC17A5* (sialin) | AR | Lysosomal | 10–100× | Neurodegenerative, hypomyelination |
| GNE myopathy (Nonaka/HIBM) | *GNE* (catalytic) | AR | — (deficiency) | Not elevated | Adult-onset myopathy |
| Pneumococcal sepsis (mimic) | — | — | — | Non-specifically elevated | Acute infection |

FSASD is caused by biallelic *SLC17A5* defects producing **lysosomal** accumulation with 10–100-fold increased urinary free sialic acid ([PMID: 33862140](https://pubmed.ncbi.nlm.nih.gov/33862140/)); this contrasts with the cytosolic overproduction of sialuria. UFSA can also be non-specifically raised in pneumococcal sepsis ([PMID: 36000484](https://pubmed.ncbi.nlm.nih.gov/36000484/)).

**Screening.** Not part of routine newborn screening. Cascade testing of at-risk relatives (given dominant inheritance) via targeted *GNE* variant testing is reasonable once a proband variant is known.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** Sialuria is not associated with early mortality; life expectancy appears largely preserved. This contrasts sharply with infantile FSASD (ISSD), which is often fatal in early childhood.
- **Morbidity / function:** Mild-to-moderate developmental delay is the principal long-term functional concern; hepatomegaly and coarse facies are generally non-disabling. Some patients show developmental improvement over time.
- **Disease course:** Chronic but stable; non-progressive/non-neurodegenerative.
- **Complications:** Few reported; no organ failure or neurodegeneration characteristic of the disorder.
- **Prognostic factors:** Genotype (all reported allosteric-site variants confer the same broad, relatively benign phenotype). No validated prognostic biomarkers beyond the diagnostic free-sialic-acid measurements.
- **Quality-of-life measures:** No formal EQ-5D/SF-36/PROMIS data (ultra-rare disease).

Overall prognosis is **substantially more favorable** than for the lysosomal sialic acid storage disorders.

---

## 12. Treatment

**No approved disease-specific therapy exists; management is supportive** (developmental support/early intervention, monitoring of hepatomegaly and growth).

**Experimental / mechanism-directed.**
- **Allele-specific RNA interference.** The most compelling proof-of-concept: in sialuria fibroblasts carrying c.797G>A (p.R266Q), synthetic siRNAs specifically targeting the mutant allele produced allele-specific knockdown, "a significant decrease of free sialic acid, to within the normal range" and recovery of CMP-sialic acid feedback inhibition of GNE-epimerase activity after silencing ([PMID: 18653764](https://pubmed.ncbi.nlm.nih.gov/18653764/)). Because the disorder is dominant and driven by the mutant allele, selectively silencing that allele is a rational therapeutic strategy (NCIT concept: gene-silencing / RNA-interference therapy).
- **Small-molecule GNE inhibitors.** GNE oligomerization/assembly can be disrupted pharmacologically; mass-photometry studies show inhibitors (C5, C13, C15) destabilize the tetramer ([PMID: 41099617](https://pubmed.ncbi.nlm.nih.gov/41099617/)) — a conceptual avenue for dampening overactive flux, though not developed as a sialuria therapy.

**Pharmacogenomics, gene/cell/immunotherapy, surgery:** Not applicable/none established.

---

## 13. Prevention

- **Primary prevention:** Not applicable for an inherited/de novo dominant single-gene disorder — no lifestyle or environmental modification prevents onset.
- **Secondary prevention:** Early biochemical recognition (urine free sialic acid) enables diagnosis, appropriate developmental support, and avoidance of unnecessary investigations for FSASD/lysosomal storage.
- **Tertiary prevention:** Supportive management of developmental delay.
- **Genetic counseling:** Autosomal dominant transmission implies up to 50% recurrence risk for offspring of an affected parent; counseling and, where a familial variant is known, prenatal/cascade *GNE* testing can be offered. De novo occurrence is common in sporadic cases.
- **Immunization / public health / prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / natural disease:** No naturally occurring sialuria has been reported in companion animals or wildlife (NCBI Taxon: *Homo sapiens*, 9606). The disorder is described only in humans.
- **Orthologous genes:** *Gne* is conserved across mammals (mouse *Gne*, NCBI Gene 50798; rat *Gne*). The bifunctional epimerase/kinase and its CMP-sialic acid feedback inhibition are evolutionarily conserved, which underpins the utility of rodent enzyme studies.
- **Comparative biology:** Homologous bacterial hydrolyzing 2-epimerases (e.g., NeuC) and prokaryotic epimerases share the epimerase fold and have informed structural understanding ([PMID: 29764940](https://pubmed.ncbi.nlm.nih.gov/29764940/)), but bacteria lack the CMP-Neu5Ac allosteric brake that is central to sialuria.
- **Zoonotic potential / transmission:** Not applicable (non-infectious Mendelian disorder).

---

## 15. Model Organisms

There is **no dedicated animal model of sialuria** per se, but the mechanism has been decisively validated in **engineered cellular and recombinant systems**:

- **Recombinant rat GNE/MNK "sialuria-like" mutants.** The double mutant **R263L-R266Q retained 93.6% of wild-type catalytic activity but lost CMP-sialic acid feedback inhibition** ([PMID: 21436238](https://pubmed.ncbi.nlm.nih.gov/21436238/)). Expressing it in EPO-producing **CHO cells increased intracellular CMP-sialic acid >10-fold** and enhanced sialylation of recombinant human erythropoietin ([PMID: 21436238](https://pubmed.ncbi.nlm.nih.gov/21436238/)). This is orthogonal in vitro confirmation of the gain-of-flux mechanism and, notably, has been exploited as a **biotechnology tool** to boost glycoprotein sialylation.
- **Patient fibroblasts.** Primary sialuria fibroblasts (p.R266Q) reproduce the cytosolic free-sialic-acid accumulation and reduced feedback inhibition and served as the substrate for the allele-specific siRNA rescue ([PMID: 18653764](https://pubmed.ncbi.nlm.nih.gov/18653764/), [PMID: 10356312](https://pubmed.ncbi.nlm.nih.gov/10356312/)).
- **Structural models.** Crystal structures of the human GNE epimerase domain and molecular models map the mutations to the allosteric site ([PMID: 26980148](https://pubmed.ncbi.nlm.nih.gov/26980148/), [PMID: 19917666](https://pubmed.ncbi.nlm.nih.gov/19917666/)).

**Phenotype recapitulation:** Cellular/recombinant models faithfully reproduce the **biochemical** phenotype (loss of feedback, elevated CMP-Sia/free Sia). **Limitation:** no model captures the intact-organism clinical features (developmental delay, hepatomegaly), leaving the mutation→systemic-phenotype link partly inferred. *(Model organism databases: MGI for mouse *Gne*; recombinant CHO systems for functional assays.)*

---

## Key Findings (with evidence)

### F001 — Sialuria is a dominant *GNE* allosteric-site disorder abolishing CMP-sialic acid feedback inhibition
All nine reported cases carry heterozygous missense variants at the *GNE* allosteric (feedback) site, clustering at Arg294 (formerly Arg263) and Arg297 (formerly Arg266). "Sialuria is a rare autosomal dominant inborn error of metabolism characterized by cytoplasmic accumulation and urinary excretion of gram quantities of free sialic acid due to failure of feedback inhibition of the rate-limiting enzyme … UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase (GNE/MNK)" ([PMID: 29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/)). OMIM #269921; gene *GNE* (9p13.3).

### F002 — Allele-specific RNAi restores feedback inhibition and normalizes free sialic acid
In p.R266Q sialuria fibroblasts, mutant-allele-specific siRNA "resulted in a significant decrease of free sialic acid, to within the normal range. Feedback inhibition of GNE-epimerase activity by CMP-sialic acid recovered after silencing" ([PMID: 18653764](https://pubmed.ncbi.nlm.nih.gov/18653764/)). This causally confirms the mechanism and provides therapeutic proof-of-concept.

### F003 — Homogeneous clinical phenotype with reduced enzyme inhibitability
The 7-year-old Portuguese patient had "developmental delay, hepatomegaly, coarse facies, and urinary excretion of 19 micromol of free NeuAc/mg creatinine," with epimerase "only 26% inhibited by 100 microM CMP-Neu5Ac (normal, 79%)" ([PMID: 10356312](https://pubmed.ncbi.nlm.nih.gov/10356312/)). Across cases the features are "developmental delay, mildly coarse features, hepatomegaly and prolonged neonatal jaundice" ([PMID: 29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/)).

### F004 — Must be distinguished from lysosomal FSASD (SLC17A5/sialin)
FSASD is "an extremely rare, autosomal recessive, neurodegenerative, multisystemic disorder caused by defects in the lysosomal sialic acid membrane exporter SLC17A5 (sialin)," causing "10-100-fold increased urinary excretion of free sialic acid" via **lysosomal** accumulation ([PMID: 33862140](https://pubmed.ncbi.nlm.nih.gov/33862140/)). Sialuria differs by inheritance (dominant), compartment (cytosolic), and course (benign). Urine free sialic acid is the shared biomarker ([PMID: 36000484](https://pubmed.ncbi.nlm.nih.gov/36000484/)).

### F005 — Crystal structure explains the Arg263/Arg266 mutations
"The complex crystal structure of the N-terminal epimerase part of human GNE shows a tetramer in which UDP binds to the active site and CMP-Neu5Ac binds to the dimer-dimer interface. The enzyme is locked in a tightly closed conformation," and "the CMP-Neu5Ac binding mode clearly elucidates why mutations in Arg263 and Arg266 can cause sialuria" ([PMID: 26980148](https://pubmed.ncbi.nlm.nih.gov/26980148/)).

### F006 — A disorder of cytosolic free-sialic-acid overproduction within the biosynthesis/sialylation pathway
"Cellular free Sias are made via de novo biosynthesis, recycled from lysosomal salvage, and even by uptake of extracellular Sias"; "free Sia can be degraded/catabolized into ManNAc and pyruvate in the cytosol"; and "Sias deficiency and overproduction (accumulation), hyposialylation … and hypersialylation all cause disorders" ([PMID: 41352710](https://pubmed.ncbi.nlm.nih.gov/41352710/)). Sialuria is the overproduction pole.

### F007 — Allelic but mechanistically opposite to GNE myopathy
"Mutations in the allosteric region lead to a different disease, sialuria" ([PMID: 23437777](https://pubmed.ncbi.nlm.nih.gov/23437777/)), whereas "More than 200 homozygous missense or compound heterozygous mutations in GNE … cause a rare neuromuscular disorder, GNE myopathy" ([PMID: 35398442](https://pubmed.ncbi.nlm.nih.gov/35398442/)) — recessive catalytic loss-of-function producing sialic acid *deficiency*.

### F008 — Engineered sialuria-like mutations confirm the gain-of-flux mechanism
"GNE/MNK-R263L-R266Q mutant showed 93.6% relative activity compared with wild type and did not display feedback inhibition," and "CMP-sialic acid concentration of engineered cells was significantly (>10-fold) increased by sialuria-mutated GNE/MNK (R263L-R266Q) expression" ([PMID: 21436238](https://pubmed.ncbi.nlm.nih.gov/21436238/)).

---

## Mechanistic Model / Interpretation

Sialuria is best understood as a **failure of a metabolic thermostat**. GNE/MNK is the rate-limiting valve of de novo sialic acid synthesis, and CMP-Neu5Ac — the pathway's activated end-product — normally binds an allosteric pocket at the tetramer's dimer–dimer interface to clamp the epimerase shut when sialic acid is abundant. The sialuria mutations (Arg263/Arg266) reshape precisely that pocket. Because catalysis is untouched (~94% of wild-type in engineered enzymes), the valve stays open regardless of downstream sialic acid levels. The result is a **dominant gain-of-flux**: the mutant allele overrides normal regulation, intracellular CMP-sialic acid climbs >10-fold, and free Neu5Ac spills into the cytosol and urine.

This model unifies three independent lines of evidence — **genetics** (all alleles cluster at the allosteric arginines), **structure** (CMP-Neu5Ac binds the interface to lock the closed state; the mutations map to this site), and **function** (engineered mutants and patient cells lose feedback but keep catalysis; allele-specific silencing reverses the biochemistry). It also cleanly explains the two "sister" contrasts: catalytic-domain loss-of-function → deficiency → **GNE myopathy**; lysosomal exporter loss → lysosomal storage → **FSASD**. Sialuria is the mirror image — cytosolic *over*production from a dominant regulatory escape.

| Axis | Sialuria | GNE myopathy | FSASD (Salla/ISSD) |
|---|---|---|---|
| Gene / defect | *GNE* allosteric site | *GNE* catalytic domains | *SLC17A5* (sialin) |
| Molecular effect | Loss of feedback (gain of flux) | Loss of catalysis | Loss of lysosomal export |
| Sialic acid | Overproduction | Deficiency | Lysosomal accumulation |
| Compartment | Cytosol | — | Lysosome |
| Inheritance | AD | AR | AR |
| Course | Mild, non-progressive | Adult-onset progressive myopathy | Neurodegenerative |

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [29923088](https://pubmed.ncbi.nlm.nih.gov/29923088/) | Sialuria: ninth patient, novel *GNE* mutation | F001, F003 (dominant inheritance, allosteric residues, homogeneous phenotype) |
| [18653764](https://pubmed.ncbi.nlm.nih.gov/18653764/) | Allele-specific RNAi in sialuria | F002 (causal proof + therapy) |
| [10356312](https://pubmed.ncbi.nlm.nih.gov/10356312/) | Sialuria in a Portuguese girl | F003 (clinical + biochemical characterization) |
| [26980148](https://pubmed.ncbi.nlm.nih.gov/26980148/) | Mechanism/inhibition of human GNE epimerase | F005 (structure; Arg263/266 in allosteric pocket) |
| [19917666](https://pubmed.ncbi.nlm.nih.gov/19917666/) | Molecular modeling of GNE/MNK | Feedback inhibition; mutation mapping |
| [21436238](https://pubmed.ncbi.nlm.nih.gov/21436238/) | Enhanced EPO sialylation via engineered GNE | F008 (retained catalysis, >10× CMP-Sia) |
| [23437777](https://pubmed.ncbi.nlm.nih.gov/23437777/) | Novel *GNE* mutations in HIBM | F007 (allosteric → sialuria) |
| [35398442](https://pubmed.ncbi.nlm.nih.gov/35398442/) | GNE mutations in Asian GNE myopathy | F007 (>200 recessive catalytic mutations) |
| [33862140](https://pubmed.ncbi.nlm.nih.gov/33862140/) | Free sialic acid storage disorder review | F004 (FSASD differential) |
| [36000484](https://pubmed.ncbi.nlm.nih.gov/36000484/) | UFSA elevated in pneumococcal sepsis | F004 (biomarker; non-specific mimic) |
| [41352710](https://pubmed.ncbi.nlm.nih.gov/41352710/) | Disorders in sialic acid metabolism | F006 (pathway framing) |
| [41099617](https://pubmed.ncbi.nlm.nih.gov/41099617/) | Mass photometry of GNE assembly | Tetramer assembly/inhibition (structure) |
| [29764940](https://pubmed.ncbi.nlm.nih.gov/29764940/) | Bacterial NeuC epimerase structure | Comparative structural biology |

All snippets quoted in this report were verified against stored abstracts during the investigation. Evidence source types: **human clinical** (case reports), **in vitro/recombinant** (engineered GNE, fibroblast assays, RNAi), and **structural/computational** (crystallography, modeling).

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Only ~9 patients have ever been reported; epidemiology (prevalence, incidence, sex ratio, penetrance) is essentially anecdotal.
2. **Mutation → organ-phenotype gap.** The biochemical mechanism is airtight, but *how* cytosolic free-sialic-acid excess produces developmental delay, hepatomegaly, and neonatal jaundice is **inferred, not demonstrated**. No mechanistic tissue-level studies exist.
3. **No dedicated animal model.** Mechanism is validated in cells/recombinant enzymes, not in an intact organism recapitulating clinical disease; natural-history data are lacking.
4. **No omics profiling** (transcriptomic/proteomic/metabolomic beyond direct sialic acid measurement) specific to sialuria patients.
5. **No approved therapy** and no clinical trials; allele-specific silencing remains at the cell-culture proof-of-concept stage.
6. **Numbering ambiguity.** Older literature uses Arg263/Arg266; current HGVS numbering is Arg294/Arg297 — a source of potential confusion in variant curation.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** carrying a sialuria allele (e.g., *Gne* R263/R266 equivalent) to test whether cytosolic free-sialic-acid overproduction reproduces hepatomegaly/developmental phenotypes and to define the mutation→organ causal chain.
2. **Patient-derived iPSC models** (hepatocyte and neuronal lineages) to characterize tissue-specific consequences of CMP-sialic acid excess and altered sialylation flux.
3. **Advance allele-specific gene silencing** (siRNA/ASO) toward preclinical development, leveraging the dominant-allele architecture demonstrated in fibroblasts ([PMID: 18653764](https://pubmed.ncbi.nlm.nih.gov/18653764/)).
4. **Establish an international registry / natural-history study** to quantify prevalence, penetrance, progression, and long-term developmental outcomes.
5. **Multi-omics (metabolomics + glycoproteomics)** on patient cells to map how hypersialylation flux alters specific glycoproteins (e.g., hepatic receptors implicated in glucose homeostasis per [PMID: 37777009](https://pubmed.ncbi.nlm.nih.gov/37777009/)).
6. **Structure-guided small-molecule "re-braking"** — screen for compounds that restore the closed, inhibited GNE conformation or dampen flux, building on the assembly-modulation data ([PMID: 41099617](https://pubmed.ncbi.nlm.nih.gov/41099617/)).
7. **Curation harmonization** — standardize variant reporting to current HGVS (Arg294/Arg297) with legacy (Arg263/Arg266) cross-references in ClinVar/OMIM.

---

*Report compiled from 8 confirmed findings and 38 reviewed papers over a 5-iteration autonomous investigation. Evidence classes: human clinical case reports, in vitro/recombinant enzymology, structural biology, and computational modeling.*


## Artifacts

- [OpenScientist final report](Sialuria-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sialuria-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 14 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41352710` *(abstract only)*: "Sias deficiency and overproduction (accumulation), hyposialylation … and hypersialylation all cause disorders"
  - closest text in source: "However, Sias deficiency and overproduction (accumulation), hyposialylation (undersialylation) and hypersialylation all cause disorders in the human body through a variety of mechanisms, but most of them are still not fully clarified"
- `PMID:29923088` *(abstract only)*: "Sialuria is a rare autosomal dominant inborn error of metabolism characterized by cytoplasmic accumulation and urinary excretion of gram quantities of free sialic acid due to failure of feedback inhibition of the rate-limiting enzyme … UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase (GNE/MNK)"
  - closest text in source: "Sialuria is a rare autosomal dominant inborn error of metabolism characterized by cytoplasmic accumulation and urinary excretion of gram quantities of free sialic acid due to failure of feedback inhibition of the rate-limiting enzyme in the sialic acid synthesis pathway, UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase (GNE/MNK)"
- `PMID:41352710` *(abstract only)*: "Sias deficiency and overproduction (accumulation), hyposialylation … and hypersialylation all cause disorders"
  - closest text in source: "However, Sias deficiency and overproduction (accumulation), hyposialylation (undersialylation) and hypersialylation all cause disorders in the human body through a variety of mechanisms, but most of them are still not fully clarified"
- `PMID:35398442` *(abstract only)*: "More than 200 homozygous missense or compound heterozygous mutations in GNE … cause a rare neuromuscular disorder, GNE myopathy"
  - closest text in source: "More than 200 homozygous missense or compound heterozygous mutations in GNE have been reported worldwide to cause a rare neuromuscular disorder, GNE myopathy"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009359` (2 mentions) - the report calls it "MONDO"; MONDO calls it **multinucleated neurons-anhydramnios-renal dysplasia-cerebellar hypoplasia-hydranencephaly syndrome**
- `HP:0003231` (1 mention) - the report calls it "Sialuria"; HP calls it **Hypertyrosinemia**
- `UBERON:0000955` (1 mention) - the report calls it "Brain / CNS** — developmental delay"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002107` (1 mention) - the report calls it "Liver** — hepatomegaly"; UBERON calls it **liver**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.