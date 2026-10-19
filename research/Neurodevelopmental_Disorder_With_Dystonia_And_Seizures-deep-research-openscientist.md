---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T18:25:42.017662'
end_time: '2026-10-16T19:08:04.852978'
duration_seconds: 2542.84
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder With Dystonia And Seizures
  mondo_id: MONDO:0859258
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Dystonia_And_Seizures-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Dystonia_And_Seizures-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Dystonia And Seizures
- **MONDO ID:** MONDO:0859258 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Dystonia And Seizures** covering all of the
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

# Neurodevelopmental Disorder With Dystonia And Seizures (MONDO:0859258): Comprehensive Disease Characterization Report

## Summary

**Neurodevelopmental Disorder With Dystonia And Seizures** (MONDO:0859258) is an **autosomal recessive Mendelian ribosomopathy** caused by **biallelic (compound heterozygous or homozygous) loss-of-function / hypomorphic variants in *SHQ1***, the gene encoding the cytoplasmic assembly chaperone of dyskerin (DKC1). It maps to **OMIM #619922**, UMLS:C5677004, MedGen:1804461, and carries the dystonia locus designation **DYT35**. This is a distinct disorder from the similarly named **KCNN2-related NEDDS (OMIM #619589)**, which is autosomal *dominant*; an early-iteration misattribution to *KCNN2* was corrected after ontology cross-referencing (EBI OLS4, Monarch) confirmed *SHQ1* as the single causal gene for MONDO:0859258.

Mechanistically, SHQ1 binds the pseudouridine synthase dyskerin (DKC1) in the cytoplasm and escorts it to the nucleus, where dyskerin is assembled into **H/ACA-class small nucleolar ribonucleoproteins (snoRNPs)** that catalyze pseudouridylation of rRNA/snRNA, mature pre-rRNA, and stabilize telomerase RNA. Pathogenic SHQ1 variants weaken dyskerin binding, destabilize H/ACA snoRNPs, cause accumulation of unprocessed pre-rRNAs, and reduce ribosome production — defining the disorder as a **ribosomopathy**. In the developing brain, SHQ1 depletion additionally impairs **neuronal migration and neurite outgrowth** and is accompanied by a **secondary central dopaminergic deficit** (low CSF homovanillic acid, reduced striatal dopamine-transporter uptake). A second, tumor-suppressor–like function involving the ER chaperone GRP78 (HSPA5/BiP) and pro-apoptotic ER/oxidative-stress signaling has also been implicated.

Clinically, affected children present in **early infancy (median onset ~3.5 months)** with **profound hypotonia, paroxysmal dystonia, brisk deep tendon reflexes, seizures, and progressive cerebellar atrophy**, with variable white-matter hypomyelination; a milder end of the spectrum includes choreiform movements with normal brain MRI. The disorder is **ultra-rare** (~5–25 reported individuals as of 2023–2026). Diagnosis is molecular (trio WES/WGS). Management is **purely symptomatic** — antiseizure medications, rehabilitation, and supportive care — with **no disease-modifying therapy**; a levodopa trial, despite the dopaminergic deficit, showed no clear benefit. Prognosis is severe lifelong neurodevelopmental disability.

---

## Key Findings

### Finding 1 — Causal gene is *SHQ1*, not *KCNN2* (critical ontology correction)

MONDO:0859258 ("neurodevelopmental disorder with dystonia and seizures") maps to **OMIM:619922**, UMLS:C5677004, MedGen:1804461, with **autosomal recessive inheritance (HP:0000007)**. Monarch's *CausalGeneToDiseaseAssociation* lists **HGNC:25543 *SHQ1*** as the single causal gene. This supersedes an initial misidentification of *KCNN2*. The *KCNN2*-related disorder — also abbreviated "NEDDS" — is a **different, autosomal dominant** disease (OMIM #619589) caused by heterozygous loss-of-function variants in the SK2 potassium channel, described in 11 patients with developmental delay, intellectual disability, cerebellar ataxia, and extrapyramidal movement disorders ([PMID: 33242881](https://pubmed.ncbi.nlm.nih.gov/33242881/)). The naming collision is a recurring source of confusion in the literature and knowledge bases; this report concerns the **recessive *SHQ1* disorder**.

> "Here, we report two sibling pairs from unrelated families with compound heterozygous variants in *SHQ1*." — [PMID: 34542157](https://pubmed.ncbi.nlm.nih.gov/34542157/)

### Finding 2 — SHQ1 is a dyskerin (DKC1) chaperone essential for H/ACA snoRNP assembly and ribosome biogenesis

SHQ1 binds the pseudouridine synthase **dyskerin (DKC1)** in the cytoplasm and escorts the enzyme to the nucleus, where dyskerin is incorporated into **H/ACA-class snoRNPs**. These snoRNPs catalyze **pseudouridylation of rRNA and snRNA**, participate in **pre-rRNA maturation**, and **stabilize the telomerase RNA component**. Loss of SHQ1 function therefore undermines ribosome biogenesis, making the disorder a **ribosomopathy**.

> "SHQ1 is an essential chaperone that binds the pseudouridine synthase dyskerin in the cytoplasm and escorts the enzyme to the nucleus, where dyskerin is assembled into small nucleolar RNPs (snoRNPs) of the H/ACA class." — [PMID: 37818102](https://pubmed.ncbi.nlm.nih.gov/37818102/)

Yeast complementation experiments directly demonstrate the consequence of pathogenic variants: expressing human variants in Shq1-depleted yeast caused progressive loss of H/ACA snoRNAs, accumulation of unprocessed pre-rRNAs, reduced Cbf5 (yeast dyskerin), and decreased ribosome production.

> "yeast cells progressively lost H/ACA snoRNAs and accumulated unprocessed pre-rRNAs, which led to reduced production of ribosomes" — [PMID: 37818102](https://pubmed.ncbi.nlm.nih.gov/37818102/)

In a neurodevelopmental context, SHQ1 knockdown in the embryonic mouse cortex (in utero electroporation) and in SH-SY5Y cells impaired neuronal migration and neurite growth, increased glutamate toxicity, and perturbed dopaminergic function.

> "SHQ1 knockdown impaired the migration and neurite morphology of cortical neurons during brain development." — [PMID: 39326821](https://pubmed.ncbi.nlm.nih.gov/39326821/)

### Finding 3 — Core clinical phenotype: infantile hypotonia, paroxysmal dystonia, seizures, cerebellar atrophy, low CSF HVA

In the largest cohort (Chi 2023; 8 individuals, 7 families), **median onset was 3.5 months**. All individuals had **profound hypotonia, paroxysmal dystonia, brisk deep tendon reflexes, and autonomic dysfunction**; most had **cerebellar atrophy** (often progressive on follow-up); **all 7 tested had low CSF homovanillic acid (HVA)**; and **4/4 with 99mTc-TRODAT-1 DAT-SPECT showed moderate-to-severe decreased striatal dopamine uptake**. A recurrent variant, **c.997C>G (p.Leu333Val)**, accounted for 56% of alleles.

> "All eight individuals exhibited normal eye contact, profound hypotonia, paroxysmal dystonia, and brisk deep tendon reflexes at the first visit." — [PMID: 36847845](https://pubmed.ncbi.nlm.nih.gov/36847845/)

> "Seven individuals who underwent cerebral spinal fluid analysis all had a low level of homovanillic acid in neurotransmitter metabolites." — [PMID: 36847845](https://pubmed.ncbi.nlm.nih.gov/36847845/)

A milder/different presentation (AlHargan 2023) involved homozygous **c.833T>C (p.Ile278Thr)** with global developmental delay, seizures, and **diffuse white-matter hypomyelination**. Sleiman 2022 described early-onset dystonia with neurodegeneration and abnormal CSF dopamine metabolism.

### Finding 4 — Genetic landscape: locus 3p13, LoF-tolerant recessive gene, ultra-rare pathogenic alleles

*SHQ1* (HGNC:25543; gene MIM 613663; ENSG00000144736; UniProt Q6PI26; aliases DYT35, GRIM-1, NEDDS, Shq1p) maps to **chromosome 3p13** (GRCh38 chr3:72,749,275–72,861,914, minus strand). gnomAD v4 constraint metrics indicate the gene is **not loss-of-function constrained** (pLI≈0; observed/expected LoF o/e=0.91, 90% CI 0.72–1.16; LOEUF upper 1.16; 167 observed pLoF alleles), **consistent with recessive inheritance** in which heterozygous carriers are tolerated. ClinVar lists 169 SHQ1 records (38 pathogenic, 8 likely pathogenic). Reported pathogenic variants are ultra-rare:

| Variant (cDNA) | Protein | Zygosity reported | gnomAD AF |
|---|---|---|---|
| c.997C>G | p.Leu333Val | recurrent (56% of alleles, Chi 2023) | 6.6×10⁻⁶ |
| c.833T>C | p.Ile278Thr | homozygous (AlHargan) | absent |
| c.195T>A | p.Tyr65Ter | compound het | 2.6×10⁻⁵ |
| c.1003C>T | p.Arg335Cys | functional null-like | 3.3×10⁻⁵ |
| c.1277C>T | p.Ala426Val | temperature-sensitive | absent |
| c.828_831del | p.Asp277SerfsTer27 | recurrent carrier LoF | 7.2×10⁻⁴ (AC=110) |

> "9 alleles (56%) were c.997C > G (p.L333V)" — [PMID: 36847845](https://pubmed.ncbi.nlm.nih.gov/36847845/)

> "revealed full segregation of the missense variant (SHQ1:c.833 T > C; p.I278T) in both families" — [PMID: 36810590](https://pubmed.ncbi.nlm.nih.gov/36810590/)

### Finding 5 — Protein architecture and variant clustering in the dyskerin-binding region

SHQ1 (UniProt Q6PI26) is a **577-aa chaperone** with an N-terminal **CS (CHORD/Sti1-like, HSP20-like) domain** (residues ~1–89), a central SHQ1-specific domain, and disordered C-terminal regions. Its function is "required for the quantitative accumulation of H/ACA ribonucleoproteins (RNPs), including telomerase, probably through the stabilization of DKC1." Subcellular localization spans **cytoplasm/cytosol (GO:0005829)** and **nucleus/nucleoplasm (GO:0005654)**. Relevant GO biological processes include **box H/ACA snoRNP assembly (GO:0000493)**, **protein-RNA complex assembly (GO:0022618)**, and **telomerase RNA localization to Cajal body (GO:0090671)**.

Reported pathogenic missense variants (p.Val271Glu, p.Asp277fs, p.Ile278Thr, p.Leu333Val, p.Arg335Cys, p.Ala426Val) **cluster in the central dyskerin-binding region**, and functional studies confirm they **attenuate SHQ1–DKC1/Cbf5 binding**.

> "Most SHQ1 variants attenuated their binding ability toward DKC1" — [PMID: 39326821](https://pubmed.ncbi.nlm.nih.gov/39326821/)

### Finding 6 — Expanded mechanism (GRP78/apoptosis/ER-oxidative stress) and broadened phenotype

Beyond ribosome biogenesis, SHQ1 interacts with the **ER chaperone GRP78 (HSPA5/BiP)** and **promotes apoptosis**. In SH-SY5Y cells, wild-type SHQ1 enhanced caspase-3 cleavage, TUNEL signal, ER-stress protein expression, and reactive oxygen species, whereas three neurodevelopmental variants (p.Tyr65Ter, p.Val271Glu, p.Leu333Val) showed **reduced apoptosis and lower ER-stress proteins** despite unchanged GRP78 binding (Lee 2025).

> "SHQ1 has been implicated in tumor suppression by interacting with the endoplasmic reticulum (ER) chaperone glucose-regulated protein 78 (GRP78), thereby promoting apoptosis" — [PMID: 40967470](https://pubmed.ncbi.nlm.nih.gov/40967470/)

The phenotypic spectrum has broadened: a milder case (Ly 2026) with compound heterozygous **c.523G>T (p.Gly175Cys)** and the recurrent **c.828_831del** frameshift presented with **choreiform movements, oromotor hypotonia, feeding difficulties, and NORMAL brain MRI but reduced CSF HVA**, diagnosed only after WES reanalysis.

> "whole exome sequencing (WES) in 2022 was nondiagnostic, and supportive measures were continued. In 2024, WES reanalysis identified compound heterozygous variants in SHQ1" — [PMID: 41885709](https://pubmed.ncbi.nlm.nih.gov/41885709/)

---

## Full Section-by-Section Report

### 1. Disease Information

**Overview.** Neurodevelopmental Disorder with Dystonia and Seizures (SHQ1-related) is a rare, autosomal recessive, early-infantile-onset neurodevelopmental and movement disorder. It is characterized by global developmental delay, profound hypotonia, paroxysmal dystonia, seizures, and (in most) progressive cerebellar atrophy, with a secondary central dopaminergic deficit.

**Key identifiers.**
- **MONDO:** 0859258
- **OMIM:** #619922 (phenotype); gene MIM 613663 (*SHQ1*)
- **Locus designation:** DYT35
- **UMLS:** C5677004 · **MedGen:** 1804461
- **HGNC (gene):** 25543 · **Ensembl:** ENSG00000144736 · **UniProt:** Q6PI26
- **ICD-11:** Best mapped under neurodevelopmental / hereditary movement disorder categories (no disease-specific code); ICD-10 proxies include G24 (dystonia) + G40 (epilepsy) + F79/F89. MeSH has no dedicated descriptor.
- **Orphanet:** Covered under genetic dystonia–neurodevelopmental entities; no stable disease-specific code was confirmed.

**Synonyms / alternative names.** NEDDS (SHQ1-type); SHQ1-related neurodevelopmental disorder; SHQ1-related dystonia (DYT35); "SHQ1-related hypomyelinating leukodystrophy" (used in a 2025 radiology case framing). Note the abbreviation **NEDDS is shared** with the unrelated *KCNN2* dominant disorder.

**Information source.** Aggregated disease-level resources (OMIM, MONDO, Monarch, ClinVar, gnomAD) combined with individual-patient case series (Sleiman 2022; Chi 2023; AlHargan 2023; Ly 2026). The evidence base is small-N case reports/series, not EHR-scale or registry data.

### 2. Etiology

**Primary cause — genetic.** Biallelic (compound heterozygous or homozygous) pathogenic variants in *SHQ1*. The disorder is monogenic and Mendelian; no environmental or infectious cause is implicated.

**Genetic risk factors.** The only established risk factor is inheriting two pathogenic *SHQ1* alleles. Recurrent alleles include **c.997C>G (p.Leu333Val)** (founder-like enrichment in the Chi 2023 cohort), homozygous **c.833T>C (p.Ile278Thr)** (consanguineous families), and the recurrent frameshift **c.828_831del (p.Asp277SerfsTer27)**, which is comparatively common as a carrier allele (gnomAD AF 7.2×10⁻⁴). **Consanguinity** increases risk of homozygous presentations.

**Environmental risk / protective factors.** None identified — consistent with a fully penetrant monogenic recessive disorder. No dietary, lifestyle, occupational, or toxin exposures are known to modify risk.

**Protective genetic factors.** None identified. Heterozygous carriers are unaffected (gene is LoF-tolerant in heterozygosity).

**Gene–environment interactions.** None established. Phenotypic variability appears to derive from allele-specific residual function (hypomorphic vs null) rather than environmental modifiers.

### 3. Phenotypes

| Phenotype | HPO term | Type | Onset | Frequency | Severity/course |
|---|---|---|---|---|---|
| Global developmental delay | HP:0001263 | Clinical sign | Infantile | ~All | Severe, stable/progressive |
| Intellectual disability | HP:0001249 | Clinical sign | Childhood | ~All | Severe |
| Profound hypotonia | HP:0001319 (neonatal) / HP:0001252 | Clinical sign | Neonatal/infantile | ~All | Severe |
| Dystonia (paroxysmal) | HP:0001332 / HP:0007199 | Clinical sign | Infantile | ~All | Severe, episodic/paroxysmal |
| Seizures | HP:0001250 | Clinical sign | Infantile–childhood | Common | Variable |
| Cerebellar atrophy | HP:0001272 | Imaging | Infantile | Most | Often progressive |
| Chorea | HP:0002072 | Clinical sign | Infantile | Milder subset | Variable |
| Brisk deep tendon reflexes | HP:0001347 | Clinical sign | Infantile | ~All (Chi cohort) | Stable |
| Autonomic dysfunction | HP:0002459 | Clinical sign | Infantile | Common | Variable |
| Decreased CSF homovanillic acid | HP:0003785 (neurotransmitter abnl.) | Lab abnormality | Infantile | 7/7 tested | — |
| White-matter hypomyelination | HP:0012762 | Imaging | Infantile | Subset | Variable |
| Feeding difficulties / oromotor hypotonia | HP:0011968 | Clinical sign | Infantile | Common | Variable |
| Microcephaly | HP:0000252 | Physical | Congenital/infantile | Subset | — |

**Age of onset.** Neonatal–early infantile; median ~3.5 months (Chi 2023). **Severity.** Generally severe, but a milder end of the spectrum exists (normal MRI, choreiform movements). **Progression.** Variable: some patients show neurodegeneration with progressive cerebellar atrophy; others are comparatively stable/non-progressive. **Quality-of-life impact.** Profound — affected children have severe motor and communication impairment, require full assistance with daily activities, and often need augmentative and alternative communication (AAC) and feeding support. No formal EQ-5D/SF-36 data exist for this ultra-rare disorder.

### 4. Genetic / Molecular Information

- **Causal gene:** *SHQ1* (HGNC:25543; MIM 613663), chromosome **3p13**.
- **Variant classes:** nonsense (p.Tyr65Ter), frameshift (p.Asp277SerfsTer27), missense (p.Gly175Cys, p.Val271Glu, p.Ile278Thr, p.Leu333Val, p.Arg335Cys, p.Ala426Val). Splice variants are possible but less documented.
- **Classification (ACMG/AMP):** Recurrent variants are Pathogenic/Likely Pathogenic (38 P + 8 LP in ClinVar); functional data (yeast complementation, DKC1-binding assays) provide PS3-level support.
- **Allele frequencies:** Ultra-rare in gnomAD (see Finding 4 table). The gene is LoF-tolerant (LOEUF upper 1.16; o/e 0.91), fitting recessive inheritance.
- **Origin:** Germline; biallelic.
- **Functional consequences:** Loss-of-function / hypomorphic — reduced dyskerin binding, destabilized H/ACA snoRNPs, impaired ribosome biogenesis. Variants behave along a null (R335C) to temperature-sensitive/hypomorphic (A426V) spectrum.
- **Modifier genes:** None established; residual allele activity is the main determinant of severity.
- **Epigenetics:** No disease-specific methylation signature reported.
- **Chromosomal abnormalities:** None characteristic; this is a single-gene disorder (not a CNV/microdeletion syndrome), though CMA may incidentally detect larger *SHQ1*-spanning deletions.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributors are implicated. This is a purely genetic, monogenic recessive disorder. (CTD, TOXNET, NHANES-type exposures: not applicable.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic hypomorphic/LoF variants in *SHQ1* **result in** reduced levels/function of SHQ1 chaperone protein (patient fibroblasts show dramatic loss of SHQ1 protein).
2. Reduced SHQ1 **leads to** weakened binding to dyskerin (DKC1/Cbf5) — pathogenic missense variants cluster in and disrupt the dyskerin-binding region.
3. Impaired dyskerin chaperoning **leads to** failure of cytoplasm-to-nucleus escort and **defective assembly of H/ACA-class snoRNPs**.
4. Loss of functional H/ACA snoRNPs **results in** loss of H/ACA snoRNAs, **defective rRNA pseudouridylation**, accumulation of unprocessed pre-rRNAs, and reduced telomerase RNA stabilization.
5. These defects **lead to** reduced ribosome production — a **ribosomopathy** (demonstrated in yeast).
6. In parallel (branch), SHQ1 loss **impairs neuronal migration and neurite outgrowth** during cortical development (demonstrated by in utero electroporation and SH-SY5Y migration assays) and increases glutamate toxicity.
7. A second branch: SHQ1 normally interacts with ER chaperone **GRP78** and promotes **ER-stress/ROS-mediated apoptosis**; variants dysregulate this (reduced apoptosis/ER-stress proteins in vitro) — *inferred* contribution to abnormal neurodevelopment.
8. Downstream, there is a **central dopaminergic deficit** (reduced CSF HVA, decreased striatal DAT uptake) — mechanism *inferred* to involve dopaminergic neuron dysfunction rather than a primary biosynthetic enzyme defect.
9. The combined ribosomal, migratory, and neurotransmitter defects **result in** the clinical phenotype: global developmental delay, profound hypotonia, paroxysmal dystonia, seizures, and progressive cerebellar atrophy.

```
 SHQ1 biallelic variants
          │ (reduced/hypomorphic SHQ1 protein)
          ▼
 Weakened SHQ1–DKC1 (dyskerin) binding
          │
          ├──────────────► Defective H/ACA snoRNP assembly
          │                 → loss of snoRNAs, rRNA pseudouridylation defect,
          │                   pre-rRNA accumulation → REDUCED RIBOSOMES (ribosomopathy)
          │
          ├──────────────► Impaired neuronal migration & neurite growth
          │                 (cortical/cerebellar development) + glutamate toxicity
          │
          └──────────────► Dysregulated GRP78/ER-stress/ROS apoptosis (inferred)
                                          │
                                          ▼
                    Central dopaminergic deficit (low CSF HVA, low striatal DAT)
                                          │
                                          ▼
     Global developmental delay · hypotonia · paroxysmal dystonia ·
                 seizures · progressive cerebellar atrophy
```

**Molecular pathways / processes:** H/ACA snoRNP assembly (GO:0000493), rRNA pseudouridine synthesis, ribosome biogenesis, neuronal migration (GO:0001764), neuron projection development (GO:0031175), apoptotic process (GO:0006915), response to ER stress (GO:0034976). **Cellular compartments:** cytosol (GO:0005829), nucleus/nucleoplasm (GO:0005654), nucleolus, Cajal body, endoplasmic reticulum. **Cell types (CL):** cerebellar/cortical neurons, dopaminergic neurons (CL:0000700), neural progenitor cells (CL:0011020). **Upstream vs downstream:** the SHQ1–dyskerin interaction and snoRNP/ribosome defect are **upstream**; neuronal migration failure, dopaminergic deficit, and clinical signs are **downstream**.

### 7. Anatomical Structures Affected

- **Primary organ/system:** Central nervous system (UBERON:0001017) — predominantly **cerebellum (UBERON:0002037)** (atrophy), cerebral cortex (UBERON:0000956), basal ganglia/striatum (UBERON:0002435) (dopaminergic deficit), and cerebral white matter (UBERON:0002316) (hypomyelination).
- **Secondary involvement:** Autonomic nervous system (dysautonomia); feeding/oromotor apparatus.
- **Tissue/cell level:** Nervous tissue; neurons (especially cerebellar and dopaminergic), neural progenitors, and oligodendrocyte-dependent myelin in the hypomyelinating subset.
- **Subcellular:** Nucleolus and Cajal body (snoRNP/ribosome biogenesis), nucleus, cytosol, ER (GRP78 interaction).
- **Localization / lateralization:** Bilateral, symmetric CNS involvement (cerebellar atrophy and striatal dopaminergic changes are bilateral).

### 8. Temporal Development

- **Onset:** Congenital-to-early-infantile; median ~3.5 months; insidious-to-subacute.
- **Progression:** Variable — a progressive/neurodegenerative course with worsening cerebellar atrophy in many, versus a more static course in milder cases. Seizures and dystonia are persistent.
- **Course pattern:** Chronic, lifelong; dystonia is paroxysmal/episodic superimposed on a chronic baseline.
- **Critical periods:** Early brain development (neuronal migration window) is the key period of vulnerability; this also narrows the plausible window for any future disease-modifying intervention.
- **Remission:** No spontaneous remission reported.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (HP:0000007); biallelic compound heterozygous or homozygous.
- **Penetrance:** Appears complete in biallelic individuals; **carriers (heterozygotes) are unaffected**.
- **Expressivity:** Variable (severe early-infantile encephalopathy to milder GDD/chorea with normal MRI), largely driven by residual allele function.
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity:** Recurrent c.997C>G and homozygous c.833T>C in consanguineous families suggest founder-like enrichment; consanguinity elevates risk.
- **Carrier frequency:** The recurrent frameshift c.828_831del reaches gnomAD AF ~7.2×10⁻⁴ (AC=110), indicating a measurable carrier pool for at least one LoF allele; most pathogenic missense alleles are ultra-rare.
- **Epidemiology:** Ultra-rare — approximately **5–25 individuals reported** worldwide (2021–2026). No reliable prevalence/incidence estimates exist.
- **Sex ratio / geography:** No strong sex bias reported; cases span multiple populations (reported from East Asian, Middle Eastern/consanguineous, and other ancestries).

### 10. Diagnostics

- **Molecular (definitive):** Trio **whole-exome (WES)** or **whole-genome sequencing (WGS)** identifying biallelic *SHQ1* variants (Chi 2023 used WGS; Sleiman 2022 used WES + MatchMaker Exchange). **WES reanalysis** can be diagnostic in previously undiagnosed cases (Ly 2026). Gene panels for dystonia/epileptic encephalopathy/leukodystrophy that include *SHQ1* are useful; single-gene testing is appropriate once *SHQ1* is suspected.
- **Supportive investigations:**
  - **Brain MRI:** cerebellar atrophy (often progressive); diffuse white-matter hypomyelination in a subset; **MRI may be normal** in milder cases.
  - **CSF neurotransmitter metabolites:** low **homovanillic acid (HVA)** — a consistent biomarker of reduced dopamine turnover.
  - **Dopamine-transporter imaging:** 99mTc-TRODAT-1 SPECT showing decreased striatal uptake.
  - **EEG:** for seizure characterization.
- **Clinical criteria / differential diagnosis:** No standardized clinical criteria; diagnosis is genotype-driven. Differentials include dopa-responsive dystonia and other inborn neurotransmitter disorders (distinguished by *SHQ1* genotype and lack of clear levodopa response), other early-infantile epileptic encephalopathies, hypomyelinating leukodystrophies, and crucially the **autosomal dominant *KCNN2* NEDDS** (OMIM #619589).
- **Screening:** No newborn screening exists; cascade carrier testing within families and preconception carrier screening are the relevant strategies.

### 11. Outcome / Prognosis

- **Prognosis:** Severe lifelong neurodevelopmental disability with profound hypotonia, persistent paroxysmal dystonia, and epilepsy. A subset shows neurodegeneration (progressive cerebellar atrophy); others are comparatively static or milder.
- **Mortality/survival:** No formal survival statistics in this ultra-rare disorder; morbidity is dominated by severe motor and communication impairment, seizure burden, feeding difficulties, and dependence on caregivers.
- **Morbidity/function:** Severe disability across motor, cognitive, and communication domains; many patients are non-ambulatory and non-verbal.
- **Prognostic factors:** Allele type (null vs hypomorphic), presence/progression of cerebellar atrophy, and severity of white-matter involvement appear to track with outcome. Low CSF HVA is a consistent biomarker but its prognostic value is unquantified.

### 12. Treatment

**No disease-modifying therapy exists.** Management is symptomatic and multidisciplinary (NCIT: Supportive Care; Symptomatic Treatment).

- **Antiseizure medications** for epilepsy (standard ASMs; NCIT: Anticonvulsant Agent). A single case observed that **adjunctive cannabidiol** reduced prolonged nocturnal tonic seizures.
- **Levodopa/L-DOPA** was trialed given the dopaminergic deficit but **showed no clear response** (Sleiman 2022) — distinguishing this disorder from classic dopa-responsive dystonia.

  > "a trial of levodopa replacement therapy was started but no clear response was noted" — [PMID: 34542157](https://pubmed.ncbi.nlm.nih.gov/34542157/)

- **Dystonia management:** anticholinergics, baclofen, and other standard dystonia pharmacotherapy (inferred from general dystonia care; NCIT: Muscle Relaxant / Anticholinergic Agent).
- **Supportive/rehabilitative:** physical, occupational, and speech therapy; augmentative and alternative communication; nutritional/feeding support (gastrostomy where needed).
- **Pharmacogenomics / targeted / gene / cell / RNA therapies:** None established or in trials for this disorder.
- **Treatment outcomes:** No systematic response-rate data; care is individualized and palliative of symptoms.

### 13. Prevention

- **Primary prevention:** Not applicable beyond reproductive genetic counseling — the disorder is monogenic with no modifiable environmental component.
- **Genetic counseling:** 25% recurrence risk for carrier couples; cascade testing of relatives; discussion of consanguinity.
- **Reproductive options:** Prenatal diagnosis and preimplantation genetic testing (PGT-M) are feasible once familial variants are known.
- **Screening:** No population newborn or carrier screening program exists; carrier screening is targeted/familial.
- **Secondary/tertiary prevention:** Early seizure control, physical therapy to prevent contractures, nutritional optimization, and surveillance for complications.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *SHQ1* is evolutionarily conserved — mouse *Shq1* (NCBI Gene 72171), rat (297483), zebrafish *shq1* (567601), *C. elegans* (176997), and budding yeast *SHQ1/YIL104C* (854702).
- **Natural animal disease:** No naturally occurring *SHQ1* disease is recorded in OMIA (no companion-animal or wildlife counterpart reported).
- **Comparative biology:** The H/ACA snoRNP/ribosome-biogenesis function of SHQ1 is conserved from yeast to human, underpinning the yeast complementation disease model. *Shq1* is an essential gene; constitutive knockout is expected to be lethal.
- **Zoonotic potential:** Not applicable (non-infectious, genetic disorder).

### 15. Model Organisms

| Model | System | Key findings | Reference |
|---|---|---|---|
| *S. cerevisiae* conditional strain | Shq1-depleted yeast expressing human SHQ1 WT/variants | WT complements; R335C (null-like) and A426V (temperature-sensitive) fail — loss of H/ACA snoRNAs, pre-rRNA accumulation, reduced Cbf5 & ribosomes | [PMID: 34542157](https://pubmed.ncbi.nlm.nih.gov/34542157/); [PMID: 37818102](https://pubmed.ncbi.nlm.nih.gov/37818102/) |
| Embryonic mouse cortex | In utero electroporation with *Shq1* shRNA ± variant cDNA | Impaired neuronal migration and neurite morphology; variants reduce DKC1 binding | [PMID: 39326821](https://pubmed.ncbi.nlm.nih.gov/39326821/) |
| SH-SY5Y neuroblastoma | Human cells expressing variants | Retarded neuronal migration; altered GRP78/ER-stress/apoptosis | [PMID: 36847845](https://pubmed.ncbi.nlm.nih.gov/36847845/); [PMID: 40967470](https://pubmed.ncbi.nlm.nih.gov/40967470/) |
| Patient-derived fibroblasts | Primary cells | Dramatic loss of SHQ1 protein | [PMID: 34542157](https://pubmed.ncbi.nlm.nih.gov/34542157/) |

> "we used a conditional yeast strain that can be depleted of the endogenous Shq1 protein while constitutively expressing human SHQ1 (wild-type or variants)" — [PMID: 37818102](https://pubmed.ncbi.nlm.nih.gov/37818102/)

**Model types:** yeast (unicellular), mouse (in vivo developmental), human cell lines (in vitro). **Genetic model types:** knockdown (shRNA), complementation/humanization (yeast expressing human SHQ1), variant overexpression. **Phenotype recapitulation:** yeast captures the ribosome-biogenesis/snoRNP defect well; mouse electroporation captures the neuronal migration defect. **Limitations:** no dedicated germline knockout mouse disease model exists (essential gene → constitutive KO lethal); no model yet integrates the full ribosomal + dopaminergic + behavioral phenotype.

---

## Mechanistic Model / Interpretation

The unifying interpretation is that **SHQ1-related NEDDS is a neurodevelopmental ribosomopathy with a secondary dopaminergic phenotype**. The upstream lesion — reduced SHQ1-mediated chaperoning of dyskerin — compromises H/ACA snoRNP assembly and thereby ribosome biogenesis, a function conserved from yeast to human and directly demonstrated by complementation assays. Because developing neurons (particularly migrating cortical and cerebellar neurons) are highly sensitive to translational capacity, the ribosomopathy manifests as impaired neuronal migration/neurite growth, producing developmental delay, hypotonia, and cerebellar atrophy. A partly separate branch — dysregulated GRP78/ER-stress/ROS-dependent apoptosis — may further perturb neuronal survival/differentiation. The consistent **low CSF HVA and reduced striatal DAT uptake** indicate a downstream central dopaminergic deficit that likely drives the dystonia/movement phenotype, yet the **absence of a clear levodopa response** argues this is not a simple dopamine-biosynthesis defect but rather dysfunction/loss of dopaminergic circuitry. Allele severity (null vs hypomorphic/temperature-sensitive) explains the phenotypic spectrum from severe early-infantile encephalopathy to milder chorea with normal MRI.

| Disorder | Gene | OMIM | Inheritance | Mechanism |
|---|---|---|---|---|
| **NEDDS (this report, MONDO:0859258)** | ***SHQ1*** | #619922 | **Autosomal recessive** | Ribosomopathy (H/ACA snoRNP/dyskerin) |
| NEDDS (name collision) | *KCNN2* | #619589 | Autosomal dominant | SK2 channel loss-of-function |

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|---|---|---|
| [34542157](https://pubmed.ncbi.nlm.nih.gov/34542157/) (Sleiman 2022) | Original description: biallelic SHQ1, recessive; fibroblast SHQ1 loss; levodopa trial without response | Human clinical + in vitro |
| [36847845](https://pubmed.ncbi.nlm.nih.gov/36847845/) (Chi 2023) | Largest cohort (8 individuals): clinical features, low CSF HVA, DAT-SPECT, recurrent p.L333V | Human clinical |
| [36810590](https://pubmed.ncbi.nlm.nih.gov/36810590/) (AlHargan 2023) | Homozygous p.I278T; GDD, seizures, hypomyelination; segregation | Human clinical |
| [37818102](https://pubmed.ncbi.nlm.nih.gov/37818102/) (Alidou-D'Anjou 2023) | Yeast complementation; defines snoRNP/ribosome-biogenesis mechanism | Model organism (yeast) |
| [39326821](https://pubmed.ncbi.nlm.nih.gov/39326821/) (Chang 2024) | Mouse cortical knockdown; migration/neurite defects; variants reduce DKC1 binding | Model organism (mouse) + in vitro |
| [40967470](https://pubmed.ncbi.nlm.nih.gov/40967470/) (Lee 2025) | GRP78/ER-stress/apoptosis second function; variant effects | In vitro |
| [41885709](https://pubmed.ncbi.nlm.nih.gov/41885709/) (Ly 2026) | Milder phenotype (chorea, normal MRI); WES reanalysis diagnostic value | Human clinical |
| [33242881](https://pubmed.ncbi.nlm.nih.gov/33242881/) (KCNN2 NEDDS) | Defines the **distinct** dominant *KCNN2* disorder (name-collision disambiguation) | Human clinical + electrophysiology |

The evidence consistently supports a recessive *SHQ1* ribosomopathy. The clinical series (Chi, Sleiman, AlHargan, Ly) and the mechanistic models (yeast, mouse, cell lines) converge on the same gene and pathway, strengthening confidence. The *KCNN2* paper is included specifically to flag the nomenclature hazard.

---

## Limitations and Knowledge Gaps

1. **Very small N.** The entire literature comprises a handful of case reports/series (~5–25 individuals). Frequency estimates, penetrance, prognosis, and genotype–phenotype correlations are therefore preliminary.
2. **No epidemiology.** Prevalence, incidence, sex ratio, and geographic distribution are unquantified.
3. **Dopaminergic mechanism unresolved.** Why low CSF HVA/striatal DAT occurs — and why levodopa fails — is not mechanistically established; the link between the ribosomopathy and dopaminergic deficit is inferred.
4. **No dedicated in vivo disease model.** The essential nature of *Shq1* precludes constitutive knockout; a conditional/humanized mouse recapitulating the full phenotype is lacking.
5. **GRP78/apoptosis branch** is in-vitro only and its in-vivo contribution to neurodevelopment is uncertain.
6. **Ontology/nomenclature confusion** between *SHQ1* and *KCNN2* "NEDDS" risks misannotation in knowledge bases.
7. **No therapeutic data.** No disease-modifying therapy or trials; treatment evidence is anecdotal (e.g., single-case cannabidiol observation).
8. **Several supporting citation snippets remain "unchecked"** against stored abstracts in the knowledge state and should be verified before final database ingestion.

## Proposed Follow-up Experiments / Actions

1. **Establish a conditional/hypomorphic mouse model** (neural-specific *Shq1* reduction or knock-in of recurrent human alleles, e.g., p.Leu333Val) to test whether the ribosomopathy produces cerebellar atrophy, dystonia, and dopaminergic deficit in vivo.
2. **Mechanistically link ribosome biogenesis to the dopaminergic deficit** — e.g., ribosome profiling / selective translational readout in dopaminergic neurons derived from patient iPSCs.
3. **Patient iPSC-derived neurons/organoids** to characterize cortical/cerebellar/dopaminergic differentiation, migration, and ER-stress/apoptosis under patient genotypes.
4. **Genotype–phenotype registry** aggregating all reported cases (allele type vs MRI findings, progression, seizure burden, CSF HVA) to formalize correlations.
5. **Standardize nomenclature/ontology** — ensure MONDO:0859258 ↔ OMIM:619922 ↔ *SHQ1* mapping is propagated and clearly separated from *KCNN2* OMIM:619589 across databases.
6. **Therapeutic exploration** — evaluate agents that enhance residual SHQ1/dyskerin function or boost ribosome biogenesis, and systematically assess dopaminergic/symptomatic therapies (including the anecdotal cannabidiol signal) in prospective, even n-of-1, designs.
7. **Verify all citation snippets** against source abstracts and upgrade "unchecked" evidence items before knowledge-base entry.

---

*Report compiled from 9 confirmed findings and 13 reviewed papers across 5 investigation iterations. Evidence sources span human clinical case series, yeast and mouse model organisms, and in-vitro cellular assays.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Dystonia_And_Seizures-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Dystonia_And_Seizures-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 14 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859258` (7 mentions) - the report calls it "if available", "Neurodevelopmental Disorder With Dystonia And Seizures", "neurodevelopmental disorder with dystonia and seizures"; MONDO calls it **neurodevelopmental disorder with dystonia and seizures**
- `HP:0002459` (1 mention) - the report calls it "Autonomic dysfunction"; HP calls it **obsolete Dysautonomia**
- `HP:0003785` (1 mention) - the report calls it "neurotransmitter abnl"; HP calls it **Decreased CSF homovanillic acid concentration**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002459` (obsolete Dysautonomia) (1 mention) - replaced by `HP:0012332`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001347` (1 mention) - the report calls it "Brisk deep tendon reflexes"; HP calls it **Hyperreflexia**, and lists "Increased deep tendon reflexes" among its other names
- `HP:0012762` (1 mention) - the report calls it "White-matter hypomyelination"; HP calls it **Cerebral white matter atrophy**
- `HP:0011968` (1 mention) - the report calls it "Feeding difficulties / oromotor hypotonia"; HP calls it **Feeding difficulties**
- `UBERON:0001017` (1 mention) - the report calls it "Primary organ/system:** Central nervous system"; UBERON calls it **central nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0859258` - called "if available", "Neurodevelopmental Disorder With Dystonia And Seizures", "neurodevelopmental disorder with dystonia and seizures"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `UMLS`, `OMIM`.
