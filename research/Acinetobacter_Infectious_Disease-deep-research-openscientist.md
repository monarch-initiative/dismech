---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T00:13:03.588785'
end_time: '2026-09-30T00:29:00.301088'
duration_seconds: 956.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acinetobacter Infectious Disease
  mondo_id: MONDO:0006635
  category: Infectious Disease
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 43
reference_validation:
  total_references: 44
  verified: 44
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 44
  on_topic: 39
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 28
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 6
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000010
    reported_labels:
    - UTI
    ontology_label: Recurrent urinary tract infections
  - term_id: HP:0001647
    reported_labels:
    - Endocarditis
    ontology_label: Bicuspid aortic valve
  - term_id: UBERON:0002048
    reported_labels:
    - Lung
    - Primary organ:** **Lung
    ontology_label: lung
  - term_id: UBERON:0000178
    reported_labels:
    - Blood/bloodstream
    - Secondary/other sites:** **Blood/bloodstream
    ontology_label: blood
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Acinetobacter_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Acinetobacter_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acinetobacter Infectious Disease
- **MONDO ID:** MONDO:0006635 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Acinetobacter Infectious Disease** covering all of the
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

# Acinetobacter Infectious Disease (MONDO:0006635): A Comprehensive Disease Characterization

## Summary

**Acinetobacter infectious disease** is an opportunistic, predominantly healthcare-associated bacterial infection caused chiefly by *Acinetobacter baumannii*, a non-fermenting, aerobic, Gram-negative coccobacillus. It is **not a heritable human disease**; it has no causal human gene, no Mendelian inheritance, and no germline/somatic variant basis. Instead, "disease characteristics" here describe an infectious syndrome whose genetics reside in the *pathogen's* genome (antibiotic-resistance and virulence loci) and whose "risk factors" are clinical and environmental exposures. The organism is one of the six **ESKAPE** pathogens and a **WHO critical-priority** target for new antibiotics. It strikes critically ill, ventilated, and immunocompromised patients—typically in intensive care units—causing ventilator-associated/hospital-acquired pneumonia (VAP/HAP), bloodstream infection (BSI)/sepsis, wound and skin/soft-tissue infection, urinary tract infection, and, less commonly, meningitis and endocarditis.

The clinical danger of *A. baumannii* arises from the convergence of three properties: (1) **extensive drug resistance**, dominated by carbapenem resistance via OXA-type carbapenemases (intrinsic *bla*<sub>OXA-51</sub> plus acquired *bla*<sub>OXA-23</sub>) and last-line colistin resistance via PmrCAB-mediated lipid A modification; (2) **exceptional environmental persistence** through resistance to desiccation and disinfectants, enabling survival on surfaces and medical devices and driving nosocomial transmission; and (3) **virulence effectors**, most notably outer membrane protein A (OmpA), which drives host-cell apoptosis via mitochondrial and nuclear targeting, alongside capsule, biofilm, motility, and serum resistance. Together these yield high mortality: in carbapenem-resistant *A. baumannii* (CRAB) nosocomial pneumonia, development of bacteremia raised in-hospital mortality from 45.9% to 68.3%.

Management centers on **combination therapy with ≥2 active agents**, anchored by **sulbactam–durlobactam** (prioritized in IDSA guidance) or **cefiderocol**, plus source control—although high-quality randomized evidence remains limited. Prevention relies on **infection prevention and control (IPC) bundles**—hand hygiene, contact precautions, environmental cleaning/disinfection, active surveillance, and antimicrobial stewardship—because the hospital environment is the primary CRAB reservoir and **no licensed human vaccine exists**. Experimental therapeutics under investigation include lytic bacteriophages, phage–antibiotic synergy, and anti-biofilm strategies.

---

## 1. Disease Information

**Overview.** Acinetobacter infectious disease is an opportunistic bacterial infection caused predominantly by *A. baumannii* (and closely related members of the *A. calcoaceticus–A. baumannii* [ACB] complex, including *A. nosocomialis* and *A. pittii*). It is a leading cause of healthcare-associated infection worldwide and a paradigm multidrug-resistant (MDR) organism.

**Key identifiers.**
- **MONDO:** MONDO:0006635 (Acinetobacter infectious disease)
- **MeSH:** Acinetobacter Infections (D000151); organism *Acinetobacter baumannii* (NCBI Taxonomy ID 470; genus *Acinetobacter* txid469)
- **ICD-10:** A curated code is not disease-specific; *Acinetobacter* is coded via site-specific infection codes plus B96.x ("as the cause of diseases classified elsewhere")
- **OMIM / Orphanet:** Not applicable — this is an acquired infectious disease, not a Mendelian/rare genetic disorder
- **Category:** Infectious disease

**Synonyms / alternative names.** Acinetobacter infection; *Acinetobacter baumannii* infection; CRAB (carbapenem-resistant *A. baumannii*) infection; MDR/XDR/PDR *Acinetobacter* infection; historically "*Bacterium anitratum*," "*Herellea vaginicola*," "*Mima polymorpha*."

**Data source type.** Information is derived from **aggregated disease-level resources** (surveillance datasets, GBD models, clinical cohorts, microbiological studies) rather than individual EHR-linked patient records.

---

## 2. Etiology

**Causal factor: infectious (bacterial).** The disease is caused by infection with *Acinetobacter* spp., chiefly *A. baumannii*. There is **no human genetic causation**; host genetic risk loci are not established for this infection.

**Risk factors (clinical/environmental).** A review of severe *A. baumannii* infection identifies the principal risk factors for MDR acquisition as **previous antibiotic use, mechanical ventilation, length of ICU/hospital stay, severity of illness, and use of medical devices** [PMID: 36272902]. Additional cohort evidence flags **advanced age (>75 years)** and **venous catheter use** as independent risk factors for cross-infection in COVID-19 ICU patients, where *A. baumannii* was the dominant organism (53.9% of strains) [PMID: 40624469].

> *"The most common risk factors for the acquisition of MDR A. baumannii are previous antibiotic use, mechanical ventilation, length of ICU and hospital stay, severity of illness, and use of medical devices."* — [PMID: 36272902]

**Prognostic risk factor: bacteremia.** In a multicenter ICU study of CRAB nosocomial pneumonia, the development of pneumogenic bacteremia was an **independent mortality risk factor (adjusted HR = 2.399, P < 0.001)** [PMID: 38852767].

**Protective factors.** No genetic protective factors are defined (non-genetic disease). Protective factors are operational/environmental: effective **infection prevention and control**, **antimicrobial stewardship**, and avoidance/limitation of invasive devices. There is no established dietary or germline-variant protection.

**Gene–environment interactions.** Not applicable in the human-host sense. The relevant "gene–environment" interplay is at the **pathogen** level: antibiotic-selection pressure (environment) selects for resistance genes (OXA carbapenemases, *pmrCAB* mutations), and the built hospital environment selects for desiccation/disinfectant-tolerant clones.

---

## 3. Phenotypes (Clinical Manifestations)

Because this is an infectious disease, "phenotypes" are clinical syndromes and their signs/laboratory abnormalities rather than HPO-encoded heritable traits. HPO terms below are suggested as approximations for knowledge-base mapping.

| Syndrome / phenotype | Type | Onset / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Ventilator-associated / hospital-acquired pneumonia | Clinical sign + imaging | Acute, healthcare-onset | Most common syndrome; ~93% of ICU respiratory MDR-AB cases developed VAP [PMID: 36641839] | HP:0002090 (Pneumonia) |
| Bloodstream infection / sepsis / septic shock | Clinical + lab | Acute | Common; raises mortality markedly | HP:0100806 (Sepsis) |
| Wound / skin & soft-tissue infection | Clinical sign | Acute | Common, esp. trauma/burns | HP:0100658 (Cellulitis) |
| Urinary tract infection | Clinical + lab | Acute | Common (catheter-associated) | HP:0000010 (UTI) |
| Meningitis (post-neurosurgical) | Clinical + CSF | Acute | Uncommon | HP:0001287 (Meningitis) |
| Endocarditis (e.g., prosthetic-valve) | Clinical + imaging | Subacute | Rare | HP:0001647 (Endocarditis) |
| Fever | Symptom | Acute | Very frequent | HP:0001945 (Fever) |

*A. baumannii* causes a **spectrum of infections**: VAP/HAP, BSI/sepsis, wound/SSTI, UTI, and less commonly meningitis and endocarditis. A documented CRAB **prosthetic-valve endocarditis** case presented with "*fever, persistent bloodstream infection, cerebellar hemorrhage, and aortic valve vegetation*" [PMID: 42293986]. **Community-onset *A. baumannii* (COAB)** clones with high virulence also exist; 32 Taiwanese COAB isolates were characterized for capsular type, biofilm, motility, desiccation and serum resistance, with in vivo virulence confirmed in a *Galleria mellonella* model, KL49 being the predominant capsular type [PMID: 41402952].

**Severity / quality-of-life impact.** Infections are typically **severe** in the ICU, with high case-fatality (see §11) and prolonged hospitalization (median length of stay up to ~74 days in one tigecycline cohort [PMID: 22869481]); survivors of ICU sepsis/VAP frequently experience long-term functional impairment. Disease is **acute** rather than chronic, but biofilm-associated device infections may be persistent/relapsing.

---

## 4. Genetic / Molecular Information

**Not applicable to the human host.** There are **no causal human genes, pathogenic germline/somatic variants, modifier genes, human epigenetic changes, or chromosomal abnormalities** underlying susceptibility to *Acinetobacter* infection in any established sense. This section therefore describes the **pathogen's** clinically decisive genetic determinants.

**Resistance genes (pathogen).** Carbapenem resistance is driven predominantly by **OXA-type carbapenemases**. In 36 clinical isolates from Baghdad, PCR revealed *bla*<sub>OXA-51</sub> in 100% (intrinsic species marker), *bla*<sub>OXA-23</sub> in 86.1%, *bla*<sub>OXA-24</sub> in 69.4%, and *bla*<sub>OXA-58</sub> in 47.2%; carbapenem resistance reached 83.3% (imipenem) and 72.2% (meropenem) [PMID: 42675958].

> *"PCR screening revealed prevalence rates of 100% for bla<sub>OXA-51</sub>, 86.1% for bla<sub>OXA-23</sub>, 69.4% for bla<sub>OXA-24</sub>."* — [PMID: 42675958]

Worldwide, "*OXA-type carbapenemases are the predominant mechanism of resistance; other mechanisms, including efflux pumps, porin mutations, and, rarely, metallo-β-lactamases, may contribute*" [PMID: 42549848]. **Colistin resistance** arises via chromosomal two-component-system mutations (*pmrCAB*) driving lipid A modification (see §6); plasmid *mcr-1–5* genes are **rare/absent** in *A. baumannii* [PMID: 40778526]. Horizontal gene transfer, including **outer membrane vesicle (OMV)-mediated transfer** of resistance determinants, contributes to dissemination.

---

## 5. Environmental Information

**Environmental factors.** *A. baumannii* survives on inanimate hospital surfaces, medical devices, and in moist niches. Its persistence is enabled by **exceptional resistance to disinfectants and desiccation**; compatible solutes contribute to desiccation resistance (studied in *A. baumannii* ATCC 19606) [PMID: 30277310].

> *"Acinetobacter baumannii is a nosocomial pathogen which can persist in the hospital environment not only due to the acquirement of multiple antibiotic resistances, but also because of its exceptional resistance against disinfectants and desiccation."* — [PMID: 30277310]

**Lifestyle factors.** Not directly applicable; the dominant "exposures" are healthcare-related (ICU admission, ventilation, devices, prior antibiotics). Community-acquired disease is associated in the literature with predisposing conditions (e.g., diabetes, alcohol use, chronic lung disease) in tropical settings, and COAB virulent clones are emerging [PMID: 41402952].

**Infectious agent.** *Acinetobacter baumannii* (NCBI:txid470), genus *Acinetobacter* (txid469); ACB-complex relatives *A. nosocomialis*, *A. pittii*, *A. calcoaceticus*. CHEBI-relevant chemical entities in pathogenesis include **lipopolysaccharide/lipid A** (CHEBI:16412), **phosphoethanolamine** (CHEBI:58190), and **4-amino-4-deoxy-L-arabinose**.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. **Colonization/exposure:** A critically ill, ventilated, or device-bearing patient is exposed to *A. baumannii* from a **desiccation/disinfectant-resistant environmental reservoir** (surfaces, devices) → **leads to** mucosal/wound colonization. *(Demonstrated; WGS ties clinical isolates to environmental reservoirs — [PMID: 34412693].)*
2. **Adhesion & biofilm:** Surface adhesins, capsule, pili, and **biofilm formation** on host tissue and devices → **result in** protected bacterial communities with reduced drug penetration and immune evasion. *(Demonstrated in vitro — [PMID: 42754003].)*
3. **Invasion & host-cell injury:** **OmpA** binds host epithelial cells; its N-terminal β-barrel mediates **mitochondrial invasion** → **triggers** a caspase cascade and mitochondrial damage; the C-terminus → **causes** DNA degradation; OmpA also **translocates to the nucleus** → **induces** apoptosis of epithelial cells. *(Demonstrated in vitro/in vivo — [PMID: 41260154]; [PMID: 17760880].)*
4. **OMV branch:** *A. baumannii* releases **OMVs containing OmpA** → **induce** mitochondrial fragmentation and deliver virulence/resistance cargo. *(Demonstrated — [PMID: 33436835].)*
5. **Inflammation & tissue damage:** Host innate recognition of LPS/OmpA → **drives** neutrophilic inflammation, cytokine release, and, in the lung, alveolar epithelial injury → **results in** pneumonia. In an OmpA-deficiency rat model, lung inflammatory damage was alleviated via downregulation of Beclin-1, JNK1, Drp-1, caspase-3/9 and upregulation of Bcl-2 [PMID: 41260154].
6. **Dissemination:** Breach of the epithelial/endothelial barrier → **leads to** bloodstream invasion (bacteremia) → **results in** sepsis/septic shock and secondary seeding (endocarditis, meningitis). Bacteremia independently raises mortality (aHR 2.399) [PMID: 38852767].
7. **Therapeutic failure branch:** Under antibiotic pressure, **OXA carbapenemases** (intrinsic *bla*<sub>OXA-51</sub> + acquired *bla*<sub>OXA-23</sub>) → **hydrolyze** carbapenems; **PmrCAB-driven lipid A modification** → **confers** colistin resistance → **results in** failure of last-line therapy and higher death. *(Demonstrated — [PMID: 42675958]; [PMID: 41890236].)*

### Detail by category

- **Molecular pathways / cellular processes:** Host **intrinsic (mitochondrial) apoptosis** (caspase-9/-3), **JNK signaling**, and **autophagy modulation** (Beclin-1, Drp-1-mediated mitochondrial fission) are engaged by OmpA [PMID: 41260154]. Relevant GO processes: **apoptotic process (GO:0006915)**, **mitochondrial fragmentation (GO:0090149)**, **inflammatory response (GO:0006954)**, **biofilm formation (GO:0042710)**.
- **Protein dysfunction (pathogen effectors):** OmpA (the most abundant surface protein) is the central virulence effector; its **nuclear translocation via a monopartite NLS induces cytotoxicity**, and nuclear microinjection into *Xenopus* embryos causes embryonic death [PMID: 17760880].
- **Metabolic changes (pathogen):** Integrated proteomics/metabolomics of an XDR-CRAB isolate showed **lipid A modification** and **membrane phospholipid remodeling** underpinning cationic antimicrobial peptide (CAMP)/colistin resistance, with upregulation of PmrA (4.2-fold), PmrB (2.9-fold), and PmrC (5.5-fold) [PMID: 41890236].
- **Immune involvement:** Innate LPS/TLR4 recognition drives inflammation; protective adaptive immunity in models is **Th1/Th17 + humoral** [PMID: 40726064].
- **Biofilm-driven tolerance:** restricted drug penetration, persister cells, efflux activity, quorum sensing and c-di-GMP signaling [PMID: 42754003].

**Suggested cell types (CL):** alveolar epithelial cells (**CL:0000066** epithelial cell), pulmonary macrophages (**CL:0000235**), neutrophils (**CL:0000775**), vascular endothelial cells (**CL:0000115**).

---

## 7. Anatomical Structures Affected

- **Primary organ:** **Lung** (UBERON:0002048) — the leading site (VAP/HAP), with alveolar epithelium (UBERON:0002299) and lower respiratory tract injury.
- **Secondary/other sites:** **Blood/bloodstream** (UBERON:0000178) in bacteremia/sepsis; **skin & soft tissue** (UBERON:0002097) in wound infection; **urinary tract/bladder** (UBERON:0001255) in UTI; **meninges** (UBERON:0002360) in meningitis; **heart valves/endocardium** (UBERON:0002165) in endocarditis; **brain** secondary hemorrhage documented in a CRAB endocarditis case [PMID: 42293986].
- **Body systems:** respiratory, cardiovascular/hematologic, integumentary, urinary, nervous.
- **Tissue/cell level:** epithelial cells (target of OmpA), macrophages and neutrophils (inflammation), endothelium (dissemination).
- **Subcellular compartments (GO CC):** **mitochondrion (GO:0005739)** and **nucleus (GO:0005634)** are the intracellular targets of OmpA; bacterial **outer membrane (GO:0019867)** and **outer membrane vesicles** are key structures.
- **Lateralization:** pneumonia may be unilateral or bilateral; generally not lateralized as a defining feature.

---

## 8. Temporal Development

- **Onset:** **Acute**. Healthcare-associated disease typically develops after ICU admission/ventilation; in one COVID-ICU cohort the mean time to first cross-infection was 8 ± 5 days [PMID: 40624469]. Community-onset acute infection also occurs [PMID: 41402952].
- **Age of onset:** any age but **heaviest burden in the elderly** (see §9/§11); neonatal ICU cases occur.
- **Progression:** Can progress rapidly from localized infection (pneumonia) to **bacteremia → sepsis → septic shock → multiorgan failure**. In bacteremic CRAB VAP with COVID-19, 91.7% developed septic shock and 57.5% died by 14 days [PMID: 37088438].
- **Course pattern:** Predominantly **acute/monophasic**; device- and biofilm-associated infections may **relapse** or persist.
- **Remission:** Treatment-induced clearance is achievable with active antibiotics + source control; spontaneous clearance in colonized but non-infected patients occurs.
- **Critical period for intervention:** Early appropriate combination therapy and source control before/at the onset of bacteremia is the key window (bacteremia independently worsens survival, aHR 2.399) [PMID: 38852767].

---

## 9. Inheritance and Population (Epidemiology)

**Inheritance.** **Not applicable** — acquired infectious disease; no Mendelian inheritance, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency in the human-genetic sense.

**Epidemiology / burden.**
- *A. baumannii* is among the **most common Gram-negative nosocomial isolates** and is predominantly carbapenem-resistant. In an Ethiopian tertiary ICU it was the single most common Gram-negative pathogen (**31.5%** of Gram-negative isolates), predominantly carbapenem-resistant, with **80.1%** of isolates multidrug-resistant [PMID: 42219453].
- It is a **top-five bloodstream-infection death-causing pathogen** in China (GBD 2021), after *S. aureus*, *E. coli*, *S. pneumoniae*, and *P. aeruginosa* [PMID: 40264014].
- It is one of **six pathogens identified as the primary generators of AMR burden** in the WHO Eastern Mediterranean Region (with *S. pneumoniae*, *K. pneumoniae*, *E. coli*, *S. aureus*, *P. aeruginosa*) [PMID: 41082884].
- **Bloodstream and lower respiratory infections account for the majority of AMR-related mortality** globally [PMID: 42674241].

**Demographics.** Burden **increases with age**, heaviest in those **≥70 years** [PMID: 40264014]; associated deaths in adults ≥70 rose by ~85.7% (1990–2021) in the EMR [PMID: 41082884]. Male predominance is reported in respiratory-niche isolates (elderly male patients). Geographic distribution is **global**, with high CRAB prevalence in Asia, the Middle East, Latin America, and southern/eastern Europe; some settings show recent declines (Thailand: 12% decline in hospital-acquired CRAB BSI frequency per 100,000 admissions, 2022→2024) [PMID: 42202898].

---

## 10. Diagnostics

**Culture-based identification.** Diagnosis is **culture-based**, with species identification by **MALDI-TOF mass spectrometry**. Standard MALDI-TOF can misassign closely related ACB-complex species (*A. baumannii* vs *A. nosocomialis*), requiring optimized protocols (ferulic-acid matrix) for reliable differentiation [PMID: 24054697].

> *"this method suffers from the inability to differentiate reliably between some closely related bacterial species including those of the Acinetobacter calcoaceticus–Acinetobacter baumannii (ACB) complex, namely A. baumannii and Acinetobacter nosocomialis."* — [PMID: 24054697]

**Rapid molecular diagnostics.** Rapid molecular blood-culture identification panels (e.g., GenMark ePlex BCID-GN) detect *A. baumannii* and deliver results **~26.7 h earlier** than conventional workflows, with high concordance vs MALDI-TOF [PMID: 36688641]. **NGS/tNGS** improves detection of non-culturable and polymicrobial organisms and can predict AMR markers (KPC, NDM, OXA-48, mecA) with moderate accuracy [PMID: 42106793; PMID: 39328359].

**Resistance-gene / mechanism testing.** PCR for *bla*<sub>OXA-51/23/24/58</sub> characterizes carbapenemase content [PMID: 42675958]. Susceptibility testing follows **CLSI** guidelines; **MALDI-based lipid A ("MALDIxin") tests** can rapidly flag colistin resistance and distinguish chromosomal from *mcr*-mediated mechanisms [PMID: 31580426].

**Clinical criteria / differential diagnosis.** Diagnosis integrates culture positivity with a compatible syndrome (VAP/HAP, BSI, etc.). Differential diagnosis includes other Gram-negative nosocomial pathogens (*P. aeruginosa*, *K. pneumoniae*, *E. coli*) and, in polymicrobial LRTI, co-infection with *P. aeruginosa* is common [PMID: 42106793].

**Screening.** Active surveillance cultures (respiratory, rectal, environmental) are used for outbreak detection and cohorting, not population screening [PMID: 34412693].

---

## 11. Outcome / Prognosis

**Mortality.** High. In CRAB nosocomial pneumonia, **bacteremia raised in-hospital mortality from 45.9% to 68.3% (P < 0.001)** and was an independent risk factor (aHR = 2.399) [PMID: 38852767]. In bacteremic CRAB VAP in COVID-19 patients, **14-day mortality was 57.5% and 30-day mortality 80.8%**, with septic shock in 91.7% [PMID: 37088438]. A Saudi ICU MDR-AB respiratory cohort reported a **74% death rate** [PMID: 36641839]. In an MDR-AB tigecycline cohort, in-hospital mortality was **51.9%** [PMID: 22869481].

| Cohort / setting | Population | Mortality | PMID |
|---|---|---|---|
| Multicenter ICU, CRAB pneumonia | Bacteremic vs non-bacteremic | 68.3% vs 45.9% | 38852767 |
| COVID-ICU, bacteremic CRAB VAP | 73 patients | 57.5% (14 d); 80.8% (30 d) | 37088438 |
| Saudi ICU, MDR-AB respiratory | 115 ventilated | 74% | 36641839 |
| Tertiary hospital, MDR-AB, tigecycline | 27 patients | 51.9% in-hospital | 22869481 |

**Prognostic factors.** Bacteremia, septic shock, higher comorbidity index (Charlson), ICU status, ECMO, inappropriate empiric therapy (lacking colistin/tigecycline), and COVID-19 co-infection worsen outcomes [PMID: 38852767; PMID: 37088438; PMID: 36641839; PMID: 38634975]. **Morbidity** includes prolonged ventilation, extended ICU/hospital stay, and secondary complications (superinfection, organ failure). **Recovery** is achievable with early active therapy and source control.

---

## 12. Treatment

**Guideline framework.** IDSA (2024/2026) and ESCMID both address CRAB. A 2026 therapeutic review notes both societies support **combination therapy with ≥2 active agents** for severe CRAB despite limited RCT data [PMID: 42549848; PMID: 42570093; PMID: 39108079].

> *"provides treatment suggestions for infections caused by ... carbapenem-resistant Acinetobacter baumannii (CRAB) ..."* — IDSA 2026 [PMID: 42570093]

**Core / preferred agents.**
- **Sulbactam–durlobactam** — prioritized as the **core of treatment** in IDSA guidance [PMID: 42549848]. *(NCIT: sulbactam C47707.)*
- **Cefiderocol** — a novel siderophore cephalosporin suggested for **refractory/resistant infection or prior treatment failure** [PMID: 42549848]; clinically effective for CRAB BSI with higher clinical cure (66% vs 44.4% for colistin, P = 0.027) and fewer adverse events, and lower mortality/higher cure in bacteremic HAP/VAP [PMID: 38634975]; cefiderocol ± fosfomycin independently associated with 30-day survival in bacteremic CRAB VAP [PMID: 37088438].
- **High-dose ampicillin–sulbactam**, **polymyxins/colistin**, and **tetracyclines (tigecycline, minocycline, eravacycline)** remain combination components [PMID: 42549848]. Tigecycline monotherapy shows high microbiological eradication but lower clinical success and should be limited in critically ill VAP/BSI [PMID: 22869481; PMID: 21789524].

**Combination regimens.** Combination is the **preferred but evidence-limited** strategy for carbapenem-resistant Gram-negatives [PMID: 34107899]. A salvage regimen of **tigecycline + extended-infusion imipenem** outperformed sulbactam+imipenem in XDR-AB VAP bacteremia (mortality 14.3% vs 64.3%), correlating with in vitro synergy [PMID: 26341302].

> *"the combination of antibiotics has become the preferred treatment strategy for CR-GNB infection. However, robust evidence to support this approach is lacking."* — [PMID: 34107899]

**Pharmacogenomics.** Not applicable (no host-genotype-guided dosing established); colistin nephrotoxicity is a key adverse-event consideration [PMID: 38634975].

**Experimental / advanced therapeutics.** Lytic **bacteriophages** and **phage–antibiotic synergy** are under active investigation; a novel lytic phage (vB_AbaM_EA1) infected 27.5% of MDR isolates, disrupted mature biofilms, and lacked toxin/lysogeny genes [PMID: 42469629; PMID: 42792069]. Phage efficacy can be undermined by **anti-phage antibodies** (fiber/nozzle-specific) [PMID: 42771684]. **Anti-biofilm strategies** (quorum-sensing inhibitors, matrix-degrading enzymes, nanoparticles, antimicrobial peptides) target biofilm-driven tolerance [PMID: 42754003].

**Suggested NCIT terms:** Antibiotic Therapy (C15370), Combination Chemotherapy, Cefiderocol, Sulbactam, Colistin, Tigecycline, Bacteriophage Therapy.

---

## 13. Prevention

**No human vaccine exists.** Prevention centers on **infection prevention and control (IPC)** and antimicrobial stewardship.

**IPC bundles.** Core interventions are **hand hygiene, targeted contact precautions, optimized environmental cleaning, and antimicrobial stewardship**, with active surveillance and cohorting in outbreaks [PMID: 42055841]. A **five-component IPC bundle** (hand hygiene, screening, universal contact precautions, environmental sampling, one-time radical environmental cleaning/disinfection) reduced ICU-CRAB incidence density **from 30.4 to 0 cases per 1000 patient-days**; WGS confirmed clinical isolates were clonally related to an **environmental reservoir**, establishing the environment as the primary route of spread [PMID: 34412693].

> *"nosocomial ICU-CRAB ID decreased from 30.4 CRAB cases per 1000 patients-days to zero cases per 1000 patients-days."* — [PMID: 34412693]

**Outbreak control.** Switching disinfectants to **sodium hypochlorite/phenolic compounds**, enhanced hand hygiene and PPE halted a COVID-ward CRAB outbreak; WGS showed clonal identity between patient and environmental isolates [PMID: 38686643; PMID: 39335042].

**Immunization.** Experimental only — OmpW-based multiepitope nanovaccines and OMV vaccines protect mice against pneumonia/bacteremia (see §15) [PMID: 40726064; PMID: 38773507]. **Prevention levels:** primary = IPC + stewardship; secondary = surveillance/early detection; tertiary = prompt combination therapy + source control to prevent bacteremia/complications.

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogen:** *Acinetobacter baumannii* (NCBI:txid470); genus *Acinetobacter* (txid469).
- **Host range / models:** Disease is modeled in **mice** (NCBI:txid10090; acute lethal pneumonia and bacteremia) and the invertebrate ***Galleria mellonella*** (greater wax moth) larva as a virulence model [PMID: 40726064; PMID: 38773507; PMID: 41402952].
- **Veterinary / natural disease:** *Acinetobacter* spp. are widespread environmental organisms and opportunistic pathogens; specific naturally occurring companion-animal disease was not a focus of this investigation (OMIA not queried; data gap).
- **Zoonotic potential:** *A. baumannii* is primarily environmental/nosocomial rather than a classical zoonosis; livestock/companion-animal reservoirs of MDR clones are an area of One-Health interest (not directly assessed here).

---

## 15. Model Organisms

- **Murine models:** acute lethal **pneumonia** and **bacteremia** models are standard for virulence and vaccine testing [PMID: 40726064; PMID: 38773507].
- **Invertebrate model:** ***Galleria mellonella*** larvae for rapid in vivo virulence assessment [PMID: 41402952].
- **Rat model:** SD rats used to show OmpA-dependent lung inflammatory damage (OmpA deficiency alleviated injury via Beclin-1/JNK1/Drp-1/caspase-3/9 down- and Bcl-2 up-regulation) [PMID: 41260154].
- **Xenopus embryo:** used to demonstrate OmpA nuclear cytotoxicity (nuclear microinjection causes embryonic death) [PMID: 17760880].
- **Vaccine models:** OmpW-based dendritic-cell-targeting **multiepitope nanovaccine** (Th1/Th17 + humoral, protective in pneumonia) [PMID: 40726064]; **OMV vaccines** (LOMV/nOMV) protective in pneumonia and bacteremia [PMID: 38773507]; heat-killed/heat-inactivated mucosal vaccination approaches [PMID: 41058705].
- **Phenotype recapitulation:** murine pneumonia/bacteremia models recapitulate acute lethal infection, host inflammation, and permit protective-immunity and phage-therapy testing; **limitations** include species differences in innate immunity and inability to fully model chronic device/biofilm infection and human ICU comorbidity.

---

## Mechanistic Model / Interpretation

```
 ENVIRONMENTAL RESERVOIR (desiccation/disinfectant-resistant)   [PMID:30277310]
        │  survives on surfaces & devices
        ▼
 COLONIZATION of ventilated/device-bearing ICU patient          [PMID:36272902]
        │  adhesins, capsule, pili
        ▼
 BIOFILM on tissue/devices → drug tolerance, immune evasion      [PMID:42754003]
        │
        ▼
 HOST-CELL INVASION & INJURY via OmpA
   ├─ N-terminus → mitochondrial damage → caspase cascade        [PMID:41260154]
   ├─ C-terminus → DNA degradation → apoptosis
   ├─ nuclear translocation (NLS) → cytotoxicity                 [PMID:17760880]
   └─ OMV-delivered OmpA → mitochondrial fragmentation           [PMID:33436835]
        │
        ▼
 INFLAMMATION & ALVEOLAR EPITHELIAL INJURY → PNEUMONIA (VAP/HAP) [PMID:36641839]
        │  barrier breach
        ▼
 BACTEREMIA → SEPSIS/SEPTIC SHOCK (mortality ↑, aHR 2.399)       [PMID:38852767]
        │
        ▼
 THERAPEUTIC FAILURE BRANCH
   ├─ OXA carbapenemases (OXA-51 intrinsic + OXA-23 acquired)    [PMID:42675958]
   └─ PmrCAB lipid A modification → colistin resistance          [PMID:41890236]
        │
        ▼
 HIGH MORTALITY (up to ~68–81% in bacteremic CRAB)              [PMID:37088438]
```

The pathophysiology is best understood as a **pathogen-driven, host-injuring cascade** in which environmental hardiness and drug resistance determine *whether and how severely* infection occurs, while OmpA-centered virulence determines *how host cells are killed*. Upstream levers (environment, devices, antibiotic pressure) are the actionable prevention targets; downstream events (bacteremia, resistance) are the prognostic determinants.

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [42219453](https://pubmed.ncbi.nlm.nih.gov/42219453/) | Leading Gram-negative ICU pathogen (31.5%), 80.1% MDR | F001 |
| [42178970](https://pubmed.ncbi.nlm.nih.gov/42178970/) | ESKAPE priority classification | F001 |
| [42675958](https://pubmed.ncbi.nlm.nih.gov/42675958/) | OXA carbapenemase gene prevalence | F002 |
| [42549848](https://pubmed.ncbi.nlm.nih.gov/42549848/) | OXA predominant mechanism; sulbactam-durlobactam/cefiderocol | F002, F004 |
| [36272902](https://pubmed.ncbi.nlm.nih.gov/36272902/) | Risk factors for MDR acquisition | F003 |
| [38852767](https://pubmed.ncbi.nlm.nih.gov/38852767/) | Bacteremia independent mortality risk (aHR 2.399) | F003 |
| [42570093](https://pubmed.ncbi.nlm.nih.gov/42570093/) | IDSA 2026 CRAB guidance | F004 |
| [41402952](https://pubmed.ncbi.nlm.nih.gov/41402952/) | Community-onset virulent clones; Galleria model | F005 |
| [42293986](https://pubmed.ncbi.nlm.nih.gov/42293986/) | CRAB prosthetic-valve endocarditis | F005 |
| [30277310](https://pubmed.ncbi.nlm.nih.gov/30277310/) | Desiccation/disinfectant resistance | F006 |
| [40264014](https://pubmed.ncbi.nlm.nih.gov/40264014/) | Top-5 BSI death pathogen (China) | F007 |
| [42674241](https://pubmed.ncbi.nlm.nih.gov/42674241/) | BSI/LRTI dominate AMR mortality | F007 |
| [40726064](https://pubmed.ncbi.nlm.nih.gov/40726064/) | Murine pneumonia model; OmpW vaccine | F008 |
| [38773507](https://pubmed.ncbi.nlm.nih.gov/38773507/) | OMV vaccine; pneumonia + bacteremia models | F008 |
| [41260154](https://pubmed.ncbi.nlm.nih.gov/41260154/) | OmpA apoptosis mechanism | F009 |
| [17760880](https://pubmed.ncbi.nlm.nih.gov/17760880/) | OmpA nuclear cytotoxicity | F009 |
| [33436835](https://pubmed.ncbi.nlm.nih.gov/33436835/) | OMV-OmpA mitochondrial fragmentation | F009 |
| [24054697](https://pubmed.ncbi.nlm.nih.gov/24054697/) | MALDI-TOF ACB-complex differentiation | F010 |
| [36688641](https://pubmed.ncbi.nlm.nih.gov/36688641/) | Rapid molecular BCID panel (~26.7 h faster) | F010 |
| [41890236](https://pubmed.ncbi.nlm.nih.gov/41890236/) | PmrAB/PmrC lipid A modification | F011 |
| [40778526](https://pubmed.ncbi.nlm.nih.gov/40778526/) | mcr genes rare/absent | F011 |
| [34412693](https://pubmed.ncbi.nlm.nih.gov/34412693/) | 5-component IPC bundle eliminates CRAB | F012 |
| [42055841](https://pubmed.ncbi.nlm.nih.gov/42055841/) | Core IPC interventions | F012 |
| [42469629](https://pubmed.ncbi.nlm.nih.gov/42469629/) | Anti-biofilm lytic phage | F013 |
| [34107899](https://pubmed.ncbi.nlm.nih.gov/34107899/) | Combination therapy preferred but evidence-limited | F013 |

Supporting/context papers: [37088438](https://pubmed.ncbi.nlm.nih.gov/37088438/), [38634975](https://pubmed.ncbi.nlm.nih.gov/38634975/), [26341302](https://pubmed.ncbi.nlm.nih.gov/26341302/), [22869481](https://pubmed.ncbi.nlm.nih.gov/22869481/), [21789524](https://pubmed.ncbi.nlm.nih.gov/21789524/), [36641839](https://pubmed.ncbi.nlm.nih.gov/36641839/), [40624469](https://pubmed.ncbi.nlm.nih.gov/40624469/), [41082884](https://pubmed.ncbi.nlm.nih.gov/41082884/), [42202898](https://pubmed.ncbi.nlm.nih.gov/42202898/), [42106793](https://pubmed.ncbi.nlm.nih.gov/42106793/), [39328359](https://pubmed.ncbi.nlm.nih.gov/39328359/), [31580426](https://pubmed.ncbi.nlm.nih.gov/31580426/), [42754003](https://pubmed.ncbi.nlm.nih.gov/42754003/), [42771684](https://pubmed.ncbi.nlm.nih.gov/42771684/), [38686643](https://pubmed.ncbi.nlm.nih.gov/38686643/), [39335042](https://pubmed.ncbi.nlm.nih.gov/39335042/), [39108079](https://pubmed.ncbi.nlm.nih.gov/39108079/).

---

## Limitations and Knowledge Gaps

1. **Not a genetic human disease.** Sections designed for Mendelian disorders (causal genes, variants, inheritance, penetrance, epigenetics, chromosomal abnormalities, genetic counseling, newborn/carrier screening) are **not applicable**; host susceptibility genetics for *Acinetobacter* infection are not established.
2. **Species heterogeneity.** Most evidence concerns *A. baumannii*; other ACB-complex members (*A. nosocomialis*, *A. pittii*) and non-baumannii *Acinetobacter* differ in virulence and resistance and are under-characterized. MALDI-TOF misidentification may bias epidemiology [PMID: 24054697].
3. **Treatment evidence quality.** Combination-therapy superiority rests largely on observational/quasi-experimental data; **robust RCTs are lacking** [PMID: 34107899]. Newer agents (sulbactam-durlobactam, cefiderocol) have limited head-to-head CRAB-specific outcome trials.
4. **Geographic bias.** Surveillance is concentrated in Asia, the Middle East, and select high-income settings; low-income community-onset burden is under-measured.
5. **Model limitations.** Murine/Galleria models do not capture chronic device biofilm infection, human comorbidity, or ICU pharmacokinetics; no licensed human vaccine has emerged despite promising preclinical candidates.
6. **Veterinary/One-Health data** (OMIA, animal reservoirs, zoonotic transfer) were not systematically investigated — a genuine gap.

---

## Proposed Follow-up Experiments / Actions

1. **Randomized controlled trials** comparing sulbactam–durlobactam- vs cefiderocol-anchored combination regimens for CRAB bacteremia/VAP, powered for 28-day mortality.
2. **Host-susceptibility genomics:** GWAS/immunogenetic studies in ICU cohorts to test whether host innate-immune variants modulate *Acinetobacter* infection risk/outcome (currently absent).
3. **OmpA-targeted therapeutics:** evaluate OmpA-neutralizing antibodies or small molecules blocking mitochondrial/nuclear translocation as adjuncts, building on the OmpA-deficiency rat protection data [PMID: 41260154].
4. **Phage-therapy optimization:** engineer phage cocktails and mitigate anti-phage antibody-mediated failure (fiber/nozzle epitope engineering) demonstrated in mice [PMID: 42771684].
5. **Vaccine advancement:** move OmpW nanovaccine and OMV candidates toward first-in-human immunogenicity/safety studies [PMID: 40726064; PMID: 38773507].
6. **Environmental/One-Health surveillance:** integrate WGS-based environmental sampling (proven to trace reservoirs [PMID: 34412693]) with veterinary/community sampling to map transmission and MDR-clone reservoirs.
7. **Rapid diagnostics rollout:** deploy molecular BCID panels and MALDI lipid A testing to shorten time-to-appropriate therapy and detect colistin resistance early [PMID: 36688641; PMID: 31580426].

---

*Evidence source types represented: human clinical (cohorts, surveillance, guidelines), model organism (mouse, rat, Galleria, Xenopus), in vitro (isolate characterization, proteomics/metabolomics, phage assays), and computational/epidemiological (GBD modeling).*


## Artifacts

- [OpenScientist final report](Acinetobacter_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Acinetobacter_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 44 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 44 |
| On topic | 39 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000010` (1 mention) - the report calls it "UTI"; HP calls it **Recurrent urinary tract infections**
- `HP:0001647` (1 mention) - the report calls it "Endocarditis"; HP calls it **Bicuspid aortic valve**
- `UBERON:0002048` (1 mention) - the report calls it "Lung", "Primary organ:** **Lung"; UBERON calls it **lung**
- `UBERON:0000178` (1 mention) - the report calls it "Blood/bloodstream", "Secondary/other sites:** **Blood/bloodstream"; UBERON calls it **blood**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:16412` (1 mention) - the report calls it "lipopolysaccharide/lipid A"; CHEBI calls it **lipopolysaccharide**
- `CHEBI:58190` (1 mention) - the report calls it "phosphoethanolamine"; CHEBI calls it **O-phosphonatoethanaminium(1-)**, and lists "phosphoethanolamine" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "skin & soft tissue"; UBERON calls it **skin of body**
- `UBERON:0001255` (1 mention) - the report calls it "urinary tract/bladder"; UBERON calls it **urinary bladder**
- `UBERON:0002360` (1 mention) - the report calls it "meninges"; UBERON calls it **meninx**
- `UBERON:0002165` (1 mention) - the report calls it "heart valves/endocardium"; UBERON calls it **endocardium**, and lists "heart endocardium" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002048` - called "Lung", "Primary organ:** **Lung"
- `UBERON:0000178` - called "Blood/bloodstream", "Secondary/other sites:** **Blood/bloodstream"