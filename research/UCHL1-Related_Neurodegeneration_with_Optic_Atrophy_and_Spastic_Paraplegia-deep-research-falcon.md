---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:29:46.892270'
end_time: '2026-08-01T18:42:15.477481'
duration_seconds: 748.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: UCHL1-Related Neurodegeneration with Optic Atrophy and Spastic Paraplegia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: UCHL1-Related_Neurodegeneration_with_Optic_Atrophy_and_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** UCHL1-Related Neurodegeneration with Optic Atrophy and Spastic Paraplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **UCHL1-Related Neurodegeneration with Optic Atrophy and Spastic Paraplegia** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** UCHL1-Related Neurodegeneration with Optic Atrophy and Spastic Paraplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **UCHL1-Related Neurodegeneration with Optic Atrophy and Spastic Paraplegia** covering all of the
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


# UCHL1-Related Neurodegeneration with Optic Atrophy and Spastic Paraplegia

## Executive summary

UCHL1-related neurodegeneration is an exceptionally rare Mendelian neurodegenerative spectrum caused by impaired **UCHL1**, a neuron-enriched ubiquitin-processing enzyme essential for long-term axonal integrity. The historically recognized disorder is biallelic, early-onset **SPG79**, characterized by progressive optic atrophy/blindness, cerebellar ataxia, spasticity, and peripheral neuropathy. A pivotal 2023 *Genetics in Medicine* study expanded the spectrum to heterozygous loss-of-function variants producing dominantly inherited spasticity, ataxia, neuropathy, and optic atrophy. Current databases therefore separate an early-onset recessive syndrome from dominant SPG79A, although these are best understood as an allelic UCHL1 loss-of-function spectrum. Open Targets recognizes both **MONDO:0014209** and **MONDO:0859363** and links them specifically to UCHL1 (ENSG00000154277). (genc2019complexityofgenerating pages 23-25, OpenTargets Search: -UCHL1)

The evidence base remains small: individual families, a limited multicenter case series, and animal or cellular experiments dominate. There are no reliable prevalence, penetrance, survival, quality-of-life, biomarker, or treatment-response estimates and no identified disease-specific interventional trial. Consequently, apparent phenotype frequencies must not be interpreted as population estimates.

| Row | Compact knowledge-base content | Evidence |
|---|---|---|
| Disease identifiers / names | **Primary disease concept:** UCHL1-related neurodegeneration with optic atrophy and spastic paraplegia; **related indexed entities:** **MONDO:0014209** early-onset progressive neurodegeneration-blindness-ataxia-spasticity syndrome; **MONDO:0859363** spastic paraplegia 79A, autosomal dominant, with ataxia; **Orphanet:352654** Early-onset progressive neurodegeneration - blindness - ataxia - spasticity; also placed within **spastic paraplegia / SPG79** disease space. Information is derived mainly from aggregated disease resources plus very small published case series/families. | (OpenTargets Search: -UCHL1, bishop2016ubiquitincterminalhydrolase pages 5-6, genc2019complexityofgenerating pages 23-25) |
| Gene / protein | **Gene:** UCHL1; **Ensembl:** **ENSG00000154277**; **Protein:** ubiquitin C-terminal hydrolase L1 (UCH-L1), a neuron-enriched deubiquitinase/ubiquitin-processing enzyme that is highly abundant in brain and required for axonal integrity maintenance. Suggested ontology: GO **deubiquitination / ubiquitin-dependent protein catabolic process**. | (OpenTargets Search: -UCHL1, bishop2016ubiquitincterminalhydrolase pages 6-7, ristic2014anoptimalubiquitinproteasome pages 6-7) |
| Inheritance / allelic spectrum | **Established recessive disease:** biallelic loss-of-function/function-impairing UCHL1 variants causing early-onset progressive neurodegeneration with blindness/optic atrophy, ataxia, and spasticity; includes autosomal recessive SPG79 reports. **Expanded dominant spectrum:** 2023 report established **heterozygous loss-of-function variants** causing a neurodegenerative disorder with spasticity, ataxia, neuropathy, and optic atrophy, consistent with dominant/haploinsufficient disease concept indexed as MONDO:0859363. | (genc2019complexityofgenerating pages 23-25, bishop2016ubiquitincterminalhydrolase pages 5-6, OpenTargets Search: -UCHL1) |
| Core phenotypes with suggested HPO terms | **Motor system:** spastic paraplegia/spasticity (**suggested HPO:** Spastic paraplegia, Spasticity, Hyperreflexia, Extensor plantar response); **cerebellar:** ataxia/gait ataxia (**suggested HPO:** Cerebellar ataxia, Gait ataxia); **optic/visual:** optic atrophy, progressive visual loss/blindness (**suggested HPO:** Optic atrophy, Decreased visual acuity, Blindness); **peripheral nerve:** sensory-motor or motor axonal neuropathy (**suggested HPO:** Peripheral neuropathy, Axonal neuropathy); **other reported in expanded spectrum:** upper motor neuron degeneration, neuromuscular junction denervation. Frequencies are not well defined because published human cohorts are extremely small. | (genc2019complexityofgenerating pages 23-25, bishop2016ubiquitincterminalhydrolase pages 5-6, genc2019complexityofgenerating pages 9-11, OpenTargets Search: -UCHL1) |
| Key pathogenic variants / reports | **p.Glu7Ala (E7A):** human missense variant with severely impaired ubiquitin hydrolysis; associated with early-onset neurodegeneration, blindness around childhood, and progressive ataxia/spasticity. **Novel splice-site variant in AR SPG79:** reported in an Indian family with autosomal recessive spastic paraplegia-79. **Heterozygous loss-of-function variants (2023 spectrum paper):** multiple LoF alleles causing dominant disorder with spasticity, ataxia, neuropathy, optic atrophy. Variant-level ACMG assertions and population frequencies should be checked in ClinVar/gnomAD per allele; not fully extractable from current evidence set. | (bishop2016ubiquitincterminalhydrolase pages 5-6, genc2019complexityofgenerating pages 23-25, OpenTargets Search: -UCHL1) |
| Mechanism with suggested GO terms | **Upstream defect:** impaired UCHL1 function disrupts ubiquitin recycling and neuronal proteostasis, reducing free monoubiquitin (mouse data ~30% reduction in UCHL1-deficient strains). **Cellular consequences:** accumulation of polyubiquitinated proteins, proteasomal stress/impairment, compensatory autophagy changes, increased ER stress, altered mTOR balance, synaptic vesicle/NMJ degeneration, axonal transport failure, and length-dependent axon degeneration. **Suggested GO terms:** ubiquitin-dependent protein catabolic process; protein deubiquitination; proteasome-mediated ubiquitin-dependent protein catabolic process; response to endoplasmic reticulum stress; regulation of TOR signaling; axon development/maintenance; synapse organization; neuromuscular junction development; autophagy. | (bishop2016ubiquitincterminalhydrolase pages 6-7, mi2021abolishinguchl1shydrolase pages 8-9, bishop2016ubiquitincterminalhydrolase pages 9-10, genc2019complexityofgenerating pages 6-9, bishop2016ubiquitincterminalhydrolase pages 8-8) |
| Anatomy / cell types with suggested UBERON / CL terms | **Primary systems:** central and peripheral nervous systems. **Anatomical sites:** optic nerve/retinal ganglion cell pathway (**suggested UBERON:** optic nerve, retina), corticospinal tract / motor cortex / spinal cord, peripheral axons, neuromuscular junction. **Cell types:** corticospinal motor neurons / upper motor neurons, spinal motor neurons, retinal ganglion cells, peripheral neurons/axons, dopaminergic neurons in fly PD models. **Suggested CL terms:** motor neuron, upper motor neuron, retinal ganglion cell, neuron, dopaminergic neuron. **Subcellular compartments:** synapse/presynaptic terminal, endoplasmic reticulum, lysosome/autophagy pathway, ubiquitin-proteasome system components. | (genc2019complexityofgenerating pages 9-11, bishop2016ubiquitincterminalhydrolase pages 6-7, tran2018drosophilaubiquitincterminal pages 1-2, genc2019complexityofgenerating pages 6-9) |
| Diagnostics | **Current practical diagnosis:** genomic testing in patients with complex HSP / optic atrophy / ataxia / neuropathy phenotype, typically via exome/genome or curated neurogenetic panels; confirmatory single-gene analysis of **UCHL1** where phenotype fits. Supportive workup may include neuro-ophthalmic examination, electrophysiology for neuropathy, and MRI/neurologic exam as indicated, but no disease-specific biomarker or standardized diagnostic criteria were found. Differential diagnosis includes other complicated HSP and optic atrophy disorders (e.g., mitochondrial/AFG3L2/SPG7/MFN2-related disorders). | (rossor2024theevolvingspectrum pages 12-13, maresca2021molecularmechanismsbehind pages 24-25, genc2019complexityofgenerating pages 23-25) |
| Treatment status | **No disease-modifying therapy established for UCHL1-related disease.** **No relevant disease-specific clinical trial identified** in repeated registry searches. Current care is supportive and extrapolated from HSP practice: oral baclofen or tizanidine for spasticity, intrathecal baclofen in severe cases, botulinum toxin, physiotherapy/orthotics, management of bladder urgency (e.g., oxybutynin), rehabilitation, and genetic counseling. UCHL1-targeted pharmacology exists only as experimental tool biology; not a clinical therapy for this disease. | (meyyazhagan2022hereditaryspasticparaplegia pages 18-20, OpenTargets Search: -UCHL1) |
| Model organisms / experimental systems | **gad mouse:** spontaneous exon 7-8 deletion; sensory ataxia then motor ataxia, hindlimb paralysis, axonal spheroids, death by ~6 months. **nm3419 mouse:** spontaneous intragenic deletion; progressive corticospinal motor neuron loss, dendrite/spine pathology, ER stress, motor impairment, NMJ denervation. **UCHL1 knockout mouse:** progressive paralysis, presynaptic terminal degeneration, loss of synaptic vesicles, premature death. **C152A knock-in:** models oxidative modification biology and partial neuroprotection after injury rather than inherited SPG79 phenotype. **Drosophila dUCH knockdown:** dopaminergic neurodegeneration, dopamine deficiency, locomotor dysfunction; useful for oxidative-stress and screening studies but does not specifically model optic atrophy/spastic paraplegia syndrome. | (genc2019complexityofgenerating pages 9-11, bishop2016ubiquitincterminalhydrolase pages 5-6, bishop2016ubiquitincterminalhydrolase pages 6-7, tran2018drosophilaubiquitincterminal pages 10-11, tran2018drosophilaubiquitincterminal pages 2-4) |
| Major evidence gaps | Disease is **ultra-rare** with very limited human numbers; no robust prevalence/incidence, penetrance, carrier frequency, sex ratio, survival statistics, validated natural-history staging, or genotype-phenotype frequency estimates. No disease-specific fluid biomarker, no validated omics signature, no single-cell/spatial transcriptomic data, no established modifier genes, no proven environmental/protective factors, no prevention strategy beyond genetic counseling/cascade testing, and no approved targeted therapy or interventional trial. Exact ontology IDs for several phenotypes/cell types should be finalized during curation. | (OpenTargets Search: -UCHL1, genc2019complexityofgenerating pages 23-25, meyyazhagan2022hereditaryspasticparaplegia pages 18-20) |


*Table: This table condenses the key identifiers, genetics, phenotypes, mechanisms, diagnostics, treatments, models, and evidence gaps for UCHL1-related neurodegeneration. It is designed for direct reuse in a disease knowledge base while clearly separating established facts from current unknowns.*

## 1. Disease information

### Definition and scope

The disease is a progressive, complicated hereditary spastic paraplegia/neurodegeneration syndrome involving long central and peripheral axons, the cerebellar system, and the anterior visual pathway. Synonyms include:

- **Spastic paraplegia 79 / SPG79**;
- **SPG79A, autosomal dominant, with ataxia**;
- **early-onset progressive neurodegeneration–blindness–ataxia–spasticity syndrome**;
- **UCHL1-related neurodegeneration**;
- **UCHL1-related neurodegenerative disorder with spasticity, ataxia, neuropathy, and optic atrophy**.

### Identifiers

- **MONDO:0014209:** early-onset progressive neurodegeneration–blindness–ataxia–spasticity syndrome.
- **MONDO:0859363:** spastic paraplegia 79A, autosomal dominant, with ataxia.
- **Orphanet:352654:** early-onset progressive neurodegeneration–blindness–ataxia–spasticity.
- **Gene:** UCHL1; Ensembl **ENSG00000154277**; chromosome 4p13.
- A dedicated, disease-specific ICD-10, ICD-11, or MeSH code was not identified. Coding generally falls under hereditary spastic paraplegia, hereditary ataxia, optic atrophy, or other specified neurodegenerative disease. Open Targets associates UCHL1 with both MONDO disease entities and cites PMIDs **23359680**, **29735986**, **28007905**, and **35986737** among the supporting literature. (OpenTargets Search: -UCHL1)

The knowledge is primarily **aggregated disease-level information derived from published individual patients and families**, not longitudinal EHR cohorts or population registries.

## 2. Etiology

### Causal factors and genetic risk

The primary cause is a germline pathogenic variant impairing UCHL1 dosage or function. The foundational recessive phenotype involved homozygous **p.Glu7Ala (E7A)**; Glu7 is important for ubiquitin binding, and the mutant showed severely reduced ubiquitin-hydrolysis activity in vitro. A separate Indian family had a biallelic splice-site variant causing autosomal-recessive SPG79. The 2023 study established that heterozygous loss-of-function alleles can also cause disease, supporting haploinsufficiency in dominant SPG79A. (genc2019complexityofgenerating pages 23-25, bishop2016ubiquitincterminalhydrolase pages 5-6, OpenTargets Search: -UCHL1)

All established disease-causing variants are germline. No causal somatic UCHL1 mosaicism, repeat expansion, aneuploidy, or recurrent pathogenic structural rearrangement has been established. Variant classification and allele frequency should be checked individually in current ClinVar and gnomAD records; the retrieved evidence does not support assigning one frequency to the whole disorder.

The older **p.Ile93Met/PARK5** literature concerns a proposed dominant parkinsonism/toxic-gain-of-function allele and should not be conflated automatically with the optic-atrophy/SPG79 loss-of-function spectrum. Experimental transgenic evidence supports toxic effects of I93M, whereas SPG79 is principally a loss-of-function disorder. (bishop2016ubiquitincterminalhydrolase pages 7-8)

### Environmental, lifestyle, infectious, and protective factors

No environmental toxin, lifestyle exposure, diet, infectious agent, age/sex exposure, or gene–environment interaction has been shown to cause or materially modify human UCHL1-related SPG79. No human protective allele is established. Oxidative stress may aggravate UCHL1 dysfunction mechanistically, but this is experimental evidence—not a validated clinical risk factor. Vitamin C rescued neuronal and locomotor phenotypes in a *Drosophila* dUCH-knockdown model; this does **not** establish vitamin C as preventive or therapeutic in affected people. (bishop2016ubiquitincterminalhydrolase pages 7-8, tran2018drosophilaubiquitincterminal pages 1-2, tran2018drosophilaubiquitincterminal pages 10-11)

## 3. Phenotypes

The phenotype is multisystem neurologic and generally progressive. Published numbers are too small for defensible percentages.

- **Spastic paraplegia/pyramidal syndrome:** progressive lower-limb spasticity, weakness, gait impairment, hyperreflexia, clonus, and extensor plantar responses. Suggested HPO: **Spastic paraplegia**, **Spasticity**, **Lower-limb hyperreflexia**, **Babinski sign**, **Abnormal gait**.
- **Cerebellar dysfunction:** gait and limb ataxia and sometimes dysarthria. Suggested HPO: **Cerebellar ataxia**, **Gait ataxia**, **Dysmetria**, **Dysarthria**.
- **Optic neuropathy:** bilateral optic atrophy with progressive visual-acuity loss, potentially severe childhood blindness in recessive disease. The p.Glu7Ala report included blindness at approximately age five. Suggested HPO: **Optic atrophy**, **Decreased visual acuity**, **Progressive visual loss**, **Blindness**. (bishop2016ubiquitincterminalhydrolase pages 5-6)
- **Peripheral neuropathy:** motor or sensorimotor, generally axonal, adding distal weakness, wasting, sensory loss, and areflexia to the upper-motor-neuron syndrome. Suggested HPO: **Peripheral axonal neuropathy**, **Motor neuropathy**, **Sensory impairment**. (genc2019complexityofgenerating pages 23-25)
- **Motor-system degeneration:** experimental models demonstrate corticospinal motor-neuron loss, spinal motor-neuron involvement, distal motor-axon degeneration, and neuromuscular-junction denervation. These provide mechanistic support but should not be coded as universal human findings. (genc2019complexityofgenerating pages 9-11, bishop2016ubiquitincterminalhydrolase pages 6-7)

Onset ranges from childhood in severe biallelic disease to later-onset presentations among heterozygous loss-of-function carriers. Severity and organ involvement are variable. The course is chronic and progressive rather than episodic or relapsing. Visual loss and impaired ambulation substantially compromise education, independence, mobility, fall risk, and activities of daily living, but no UCHL1-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was found.

## 4. Genetic and molecular information

**UCHL1** encodes ubiquitin C-terminal hydrolase L1, a 223-amino-acid protein reported to constitute approximately 1–5% of total neuronal protein. It contains a cysteine-protease catalytic triad and a restrictive crossover loop. UCHL1 appears particularly important for processing ubiquitin precursors and maintaining free monoubiquitin, rather than broadly removing ubiquitin chains from large substrates. (bishop2016ubiquitincterminalhydrolase pages 6-7, bishop2016ubiquitincterminalhydrolase pages 7-8, puri2024functionaldynamicsof pages 6-8)

Relevant variant classes include missense variants that impair ubiquitin interaction or catalysis, splice-disrupting variants, and heterozygous truncating/loss-of-function variants. Functional interpretation should assess transcript consequence, nonsense-mediated decay, protein abundance, ubiquitin binding, hydrolase activity, and segregation. No validated modifier gene, disease-specific methylation signature, pathogenic chromosomal abnormality, or recurrent copy-number syndrome is known.

For ACMG/AMP curation, strong evidence categories may include loss-of-function in a gene for which haploinsufficiency or biallelic loss is disease-causing, segregation, extreme rarity, and functional loss. However, inheritance model matters: a variant’s interpretation must distinguish dominant SPG79A from recessive SPG79 and from proposed gain-of-function parkinsonism alleles.

## 5. Environmental information

No disease-specific environmental, occupational, radiation, pollution, smoking, alcohol, dietary, or infectious determinant has been demonstrated. UCHL1’s Cys152 can be modified by reactive lipid products, destabilizing the protein and promoting aggregation in experimental systems; UCHL1-deficient mice are more vulnerable to lipid peroxidation and vitamin-E deficiency. These findings make oxidative injury biologically plausible as a modifier but do not justify exposure-avoidance rules or antioxidant prescriptions beyond general health guidance. (bishop2016ubiquitincterminalhydrolase pages 7-8, bishop2016ubiquitincterminalhydrolase pages 8-8)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic defect:** reduced UCHL1 quantity or function.
2. **Ubiquitin-homeostasis defect:** impaired ubiquitin processing/recycling lowers free monoubiquitin; UCHL1-deficient mouse strains show an approximately **30% reduction**, while acute in-vitro inhibition has produced an approximately **50% reduction**. (bishop2016ubiquitincterminalhydrolase pages 6-7, genc2019complexityofgenerating pages 6-9)
3. **Proteostasis stress:** ubiquitinated proteins accumulate, proteasomal efficiency falls, lysosomal/autophagic responses change, and energy demand increases. Catalytically impaired mice accumulate polyubiquitinated proteins and induce Beclin-1, consistent with compensatory autophagy. (mi2021abolishinguchl1shydrolase pages 8-9, genc2019complexityofgenerating pages 6-9)
4. **ER and growth-signaling dysregulation:** corticospinal neurons develop ER stress, dendritic vacuolation, and spine loss; UCHL1 loss is associated experimentally with increased mTORC1 activity and disturbed mTORC1/mTORC2 balance. (genc2019complexityofgenerating pages 6-9, genc2019complexityofgenerating pages 9-11)
5. **Synaptic and transport failure:** presynaptic terminals lose vesicles, neuromuscular junctions denervate, microtubule/axonal transport becomes defective, and spheroids containing ubiquitin-positive material develop. (bishop2016ubiquitincterminalhydrolase pages 6-7, bishop2016ubiquitincterminalhydrolase pages 5-6)
6. **Length-dependent axon degeneration:** long corticospinal, sensory, peripheral motor, cerebellar, and optic pathways are selectively vulnerable, producing spasticity, neuropathy, ataxia, and optic atrophy.

### Cells, pathways, and ontology suggestions

Relevant cells are upper/corticospinal motor neurons, spinal motor neurons, peripheral sensory and motor neurons, retinal ganglion cells, and their axons. Suggested CL terms: **motor neuron**, **upper motor neuron**, **retinal ganglion cell**, **sensory neuron**, and **neuron**. Retinal ganglion cells are the source of optic-nerve axons and are intrinsically vulnerable because of their long, energy-demanding axonal architecture, although UCHL1-specific retinal-cell mechanisms remain incompletely resolved.

Suggested GO biological processes include **protein deubiquitination**, **ubiquitin-dependent protein catabolic process**, **proteasome-mediated ubiquitin-dependent protein catabolic process**, **maintenance of protein location**, **response to endoplasmic-reticulum stress**, **autophagy**, **regulation of TOR signaling**, **axon maintenance**, **axonal transport**, and **synapse organization**. Suggested GO cellular components include **cytosol**, **axon**, **presynaptic terminal**, **neuromuscular junction**, **endoplasmic reticulum**, **proteasome complex**, and **lysosome**.

No disease-specific human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omic signature was found. General UCHL1 structural and chemoproteomic studies exist but are not diagnostic profiles. A 2024 structural review emphasizes that disease mutations and oxidation alter UCH-family conformational dynamics; UCHL1 has much lower generic DUB efficiency than UCHL3, reinforcing its specialized ubiquitin-processing role. (puri2024functionaldynamicsof pages 6-8)

## 7. Anatomical structures affected

Primary involvement is neurologic:

- **Motor cortex and corticospinal tract**—upper-motor-neuron degeneration and spastic paraplegia;
- **Spinal cord and peripheral motor pathways**—distal axon and neuromuscular-junction degeneration;
- **Peripheral nerves**—axonal neuropathy;
- **Cerebellar pathways**—ataxia;
- **Retina/optic nerve**—presumed retinal-ganglion-cell axon loss causing bilateral optic atrophy.

Suggested UBERON annotations: **brain**, **motor cortex**, **spinal cord**, **corticospinal tract**, **peripheral nerve**, **cerebellum**, **retina**, and **optic nerve**. Visual disease is generally bilateral. No consistent non-neurologic organ phenotype is established in humans, despite UCHL1 expression or functional roles in some non-neural tissues.

## 8. Temporal development

Biallelic disease may begin in early childhood, with visual loss and evolving ataxic-spastic motor dysfunction; the original p.Glu7Ala syndrome included blindness at about five years. Dominant loss-of-function broadens onset into later life. The onset is generally insidious, followed by slow or variable progression. (bishop2016ubiquitincterminalhydrolase pages 5-6)

A practical—not formally validated—staging concept is:

1. **Early:** visual impairment, gait imbalance, subtle pyramidal or neuropathic signs;
2. **Intermediate:** definite spastic-ataxic gait, optic atrophy, electrophysiologic neuropathy, falls;
3. **Advanced:** severe visual disability, walking-aid or wheelchair dependence, distal weakness/wasting and contractures.

No remission pattern, acute crisis phenotype, validated progression scale, median disease duration, or intervention window has been established. Animal evidence suggests proteostasis and ER-stress abnormalities precede overt neuronal loss, making presymptomatic restoration of UCHL1 function a rational—but untested—therapeutic objective. (genc2019complexityofgenerating pages 18-20, genc2019complexityofgenerating pages 9-11)

## 9. Inheritance and population

Both **autosomal recessive** and **autosomal dominant** UCHL1 loss-of-function disease are recognized. Recessive recurrence risk is 25% for each pregnancy of two confirmed heterozygous carriers; dominant transmission risk is nominally 50% from an affected heterozygous parent, subject to variant-specific penetrance. Penetrance, age dependence, expressivity distributions, germline mosaicism rate, anticipation, and phenocopy rate have not been quantified.

No prevalence or incidence per 100,000, carrier frequency, founder effect, geographic concentration, ethnic enrichment, or sex ratio is known. Consanguinity can increase the probability of a recessive diagnosis but is not required. The few reports include unrelated families from different populations, so no ancestry-specific conclusion is justified. General HSP prevalence estimates—reported in reviews as roughly 0.1–9.6/100,000—must **not** be assigned to SPG79. 

## 10. Diagnostics

### Clinical evaluation

Suspect UCHL1 disease in a patient with otherwise unexplained combinations of progressive spasticity, ataxia, axonal neuropathy, and bilateral optic atrophy. Evaluation should document neurologic examination, gait and spasticity scales, visual acuity, color vision, visual fields, fundus examination, optical coherence tomography, and—when useful—visual evoked potentials. Nerve-conduction studies/EMG can classify peripheral neuropathy. Brain and spinal MRI are principally supportive and exclude structural, inflammatory, leukodystrophic, or mitochondrial mimics.

No diagnostic enzyme assay, blood chemistry, CSF biomarker, biopsy signature, or standardized clinical criteria have been validated. UCHL1 itself is used as a neuronal-injury biomarker in other disorders, but that does not make circulating UCHL1 a validated biomarker for inherited UCHL1 deficiency.

### Genetic testing

A broad **WES/WGS or ataxia–HSP–optic-atrophy panel** is generally preferable because phenocopies are numerous. Analysis must include single-nucleotide and indel variants, splice effects, and exon-level CNVs; segregation and parental testing are important for determining dominant versus recessive disease. WGS may identify noncoding splice or structural variants missed by exome testing. RNA studies are appropriate for suspected splice variants, and functional protein/hydrolase assays remain research tools.

CMA and karyotyping have low expected yield for an isolated single-gene phenotype unless syndromic copy-number disease is suspected. FISH, mitochondrial-DNA testing, and repeat-expansion testing are differential-diagnosis tools, not UCHL1 assays.

### Differential diagnosis

Important alternatives include **SPG7, AFG3L2, OPA1, MFN2, PNPT1, FDXR, WFS1, SACS, KIF1A, CAPN1**, mitochondrial disorders, Friedreich ataxia, and treatable metabolic HSPs. SPG7/AFG3L2/MFN2 disorders can combine spasticity or neuropathy with optic atrophy through mitochondrial mechanisms, whereas UCHL1 disease is primarily a neuronal ubiquitin/proteostasis disorder. (rossor2024theevolvingspectrum pages 12-13, maresca2021molecularmechanismsbehind pages 24-25)

Cascade testing is appropriate after identifying a familial pathogenic variant. Population or newborn screening is not established.

## 11. Outcome and prognosis

Human survival, mortality, life expectancy, and 5- or 10-year outcomes are unknown. The disorder can cause major lifelong morbidity through visual disability, progressive gait impairment, falls, neuropathic weakness, contractures, and loss of independence. No evidence supports spontaneous neurologic recovery.

Mouse null models have much more rapid courses—progressive paralysis and death at approximately 6–7 months—and should not be used to predict human life expectancy. (bishop2016ubiquitincterminalhydrolase pages 5-6, bishop2016ubiquitincterminalhydrolase pages 6-7)

No validated prognostic biomarker exists. Plausible prognostic variables include inheritance mode, residual UCHL1 function, age at onset, early visual involvement, axonal-neuropathy burden, and rate of gait decline, but none has been prospectively validated.

## 12. Treatment

There is no approved disease-modifying treatment, gene therapy, RNA therapy, cell therapy, or UCHL1-directed drug for SPG79. Repeated registry searches found no relevant disease-specific interventional study. Management is multidisciplinary and extrapolated from complicated HSP practice.

- **Spasticity:** oral baclofen or tizanidine; focal botulinum toxin; intrathecal baclofen for severe generalized spasticity after specialist assessment. Suggested NCIT concepts: **Baclofen**, **Tizanidine**, **Botulinum Toxin Therapy**, **Intrathecal Drug Administration**.
- **Mobility:** physical therapy, daily stretching, strengthening, balance work, ankle-foot orthoses, walking aids, wheelchair/seating assessment, and fall prevention. Suggested NCIT: **Physical Therapy**, **Occupational Therapy**, **Rehabilitation Therapy**, **Orthotic Device**.
- **Bladder dysfunction:** clinical assessment and agents such as oxybutynin when indicated.
- **Neuropathy and complications:** foot care, neuropathic-pain treatment, contracture prevention, nutrition and swallowing evaluation where clinically required.
- **Vision:** low-vision rehabilitation, assistive technology, educational/workplace adaptation, and ophthalmologic surveillance.
- **Genetic care:** counseling, cascade testing, and reproductive options.

General HSP literature reports oral baclofen/tizanidine, intrathecal baclofen, botulinum toxin plus stretching, orthotics, peroneal stimulation, exercise, and bladder treatment, but no UCHL1-specific response rate or adverse-event estimate exists. (meyyazhagan2022hereditaryspasticparaplegia pages 18-20)

Experimental concepts include restoring UCHL1 expression, preserving monoubiquitin, correcting proteostasis/ER stress, or preventing oxidative inactivation. UCHL1 inhibition would be mechanistically counterintuitive for loss-of-function disease. AAV-mediated UCHL1 overexpression has benefited Alzheimer-model mice, and vitamin C rescued a fly-knockdown phenotype, but neither constitutes SPG79 efficacy evidence. (tran2018drosophilaubiquitincterminal pages 1-2, tran2018drosophilaubiquitincterminal pages 10-11)

## 13. Prevention

Primary lifestyle prevention is not possible for a germline Mendelian disorder. No vaccine, medication, dietary supplement, or exposure intervention prevents disease.

Secondary prevention consists of familial variant identification, cascade testing, early neuro-ophthalmic and motor assessment, and prompt rehabilitation. Reproductive options include prenatal diagnosis and preimplantation genetic testing after a familial pathogenic variant is established. Tertiary prevention includes maintaining range of motion, preventing falls and contractures, protecting insensate feet, managing bladder complications, and providing low-vision and mobility support. Genetic counseling must explicitly address whether the family has dominant or recessive UCHL1 disease.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart or zoonotic form was identified. The condition is not infectious and has no zoonotic potential. UCHL1 is evolutionarily conserved; *Drosophila* dUCH shares approximately **43.7% sequence identity** with mammalian UCHL1 and preserves catalytic features. (tran2018drosophilaubiquitincterminal pages 2-4)

Suggested taxa for experimental annotations are *Mus musculus* (**NCBI Taxon 10090**) and *Drosophila melanogaster* (**NCBI Taxon 7227**). No breed-specific VBO annotation is applicable.

## 15. Model organisms

### Mouse

- **gad mouse:** spontaneous in-frame deletion of Uchl1 exons 7–8. Sensory ataxia appears around three months, motor ataxia around four months, followed by paralysis and death near six months. Axonal spheroids, ubiquitin-positive deposits, transport failure, and Wallerian degeneration are prominent and increase with axon length. (bishop2016ubiquitincterminalhydrolase pages 5-6)
- **Uchl1nm3419:** intragenic deletion involving exons 6–8. It reproduces motor impairment, progressive corticospinal-neuron loss, vacuolated apical dendrites, spine loss, ER stress, spinal-motor-neuron involvement, and NMJ denervation. (genc2019complexityofgenerating pages 9-11)
- **Targeted Uchl1 knockout:** progressive ataxia/paralysis, axon degeneration, presynaptic-terminal degeneration, loss of synaptic vesicles, and premature death. (bishop2016ubiquitincterminalhydrolase pages 6-7)
- **Catalytic C90A and oxidative-site C152A knock-ins:** dissect hydrolase and oxidative-injury functions. C90A worsens axonal and neuronal injury after trauma but does not reproduce the full null phenotype, indicating important non-hydrolase functions. (mi2021abolishinguchl1shydrolase pages 8-9)

A key limitation is that optic atrophy has not been consistently reproduced or systematically evaluated in all Uchl1-deficient mouse lines. Their rapid severe course also differs from many human heterozygous cases.

### Drosophila

TH-GAL4-driven dUCH RNAi causes progressive degeneration of defined dopaminergic-neuron clusters, chronic dopamine deficiency, and locomotor dysfunction. Vitamin C at **0.5 mM** rescued neuron loss and locomotor impairment. This is useful for high-throughput neuroprotection and oxidative-stress studies but models dopaminergic degeneration rather than the complete human optic-atrophy/spastic-ataxia syndrome. (tran2018drosophilaubiquitincterminal pages 10-11, tran2018drosophilaubiquitincterminal pages 2-4)

### Cellular systems

Patient-derived neuronal models remain underdeveloped. Existing primary-neuron, injury, glioblastoma, and other cell assays establish effects on ubiquitin abundance, proteostasis, oxidative injury, and aggregation but are not faithful disease-specific models. Patient iPSC-derived corticospinal motor neurons and retinal ganglion cells, organoids, and isogenic CRISPR-corrected lines are high-priority future resources.

## Recent developments and expert assessment

The most important recent development is the **2023 expansion from a purely recessive childhood syndrome to heterozygous loss-of-function disease**, changing genetic counseling and variant interpretation. The paper’s title summarizes its principal conclusion: “**Heterozygous UCHL1 loss-of-function variants cause a neurodegenerative disorder with spasticity, ataxia, neuropathy, and optic atrophy**” (*Genetics in Medicine*, October 2023; DOI: https://doi.org/10.1016/j.gim.2023.100961). Open Targets now indexes the dominant entity separately as MONDO:0859363. (OpenTargets Search: -UCHL1)

Recent 2024 reviews place UCHL1 among genes crossing traditional boundaries between hereditary neuropathy, spastic paraplegia, and cerebellar ataxia. This is clinically appropriate: diagnostic classification by the leading symptom alone risks missing the multisystem syndrome. The authoritative mechanistic view remains that UCHL1 is “absolutely required for the maintenance of axonal integrity,” while its complete substrate repertoire and the cause of selective neuronal vulnerability remain unresolved. (bishop2016ubiquitincterminalhydrolase pages 6-7, bishop2016ubiquitincterminalhydrolase pages 8-8)

## Evidence gaps and curation cautions

1. Do not merge dominant SPG79A, recessive SPG79, and PARK5 without preserving inheritance and molecular-mechanism qualifiers.
2. Do not infer phenotype percentages from a handful of reported families.
3. No reliable prevalence, incidence, penetrance, sex ratio, survival, natural-history scale, or quality-of-life statistic exists.
4. No validated human biomarker, disease-specific omics profile, protective factor, modifier gene, or targeted treatment exists.
5. Model-organism rescue by antioxidants or UCHL1 expression is hypothesis-generating only.
6. Variant-level ClinVar, gnomAD, transcript, HGVS, and ACMG assertions should be refreshed at the time of database ingestion.

### Key literature links

- Foundational human recessive disease: PMID **23359680**; *PNAS* (2013), “Recessive loss of function of the neuronal ubiquitin hydrolase UCHL1 leads to early-onset progressive neurodegeneration.”
- Indian AR SPG79 splice variant: PMID **29735986**; *Journal of Human Genetics* (2018), DOI: https://doi.org/10.1038/s10038-018-0463-6.
- Dominant loss-of-function spectrum: *Genetics in Medicine* (October 2023), DOI: https://doi.org/10.1016/j.gim.2023.100961.
- UCHL1 structure/function review: *Biochemical Journal* (August 2016), DOI: https://doi.org/10.1042/BCJ20160082. (bishop2016ubiquitincterminalhydrolase pages 6-7)
- Mouse upper-motor-neuron models: *International Journal of Molecular Sciences* (August 2019), DOI: https://doi.org/10.3390/ijms20163848. (genc2019complexityofgenerating pages 18-20, genc2019complexityofgenerating pages 9-11)
- Drosophila dUCH knockdown: *Scientific Reports* (March 2018), DOI: https://doi.org/10.1038/s41598-018-22804-w. (tran2018drosophilaubiquitincterminal pages 1-2, tran2018drosophilaubiquitincterminal pages 10-11)
- General HSP management review: *International Journal of Molecular Sciences* (February 2022), DOI: https://doi.org/10.3390/ijms23031697. (meyyazhagan2022hereditaryspasticparaplegia pages 18-20)

References

1. (genc2019complexityofgenerating pages 23-25): Baris Genc, Oge Gozutok, and P. Hande Ozdinler. Complexity of generating mouse models to study the upper motor neurons: let us shift focus from mice to neurons. International Journal of Molecular Sciences, 20:3848, Aug 2019. URL: https://doi.org/10.3390/ijms20163848, doi:10.3390/ijms20163848. This article has 37 citations.

2. (OpenTargets Search: -UCHL1): Open Targets Query (-UCHL1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (bishop2016ubiquitincterminalhydrolase pages 5-6): Paul Bishop, Dan Rocca, and Jeremy M. Henley. Ubiquitin c-terminal hydrolase l1 (uch-l1): structure, distribution and roles in brain function and dysfunction. Biochemical Journal, 473:2453-2462, Aug 2016. URL: https://doi.org/10.1042/bcj20160082, doi:10.1042/bcj20160082. This article has 389 citations and is from a domain leading peer-reviewed journal.

4. (bishop2016ubiquitincterminalhydrolase pages 6-7): Paul Bishop, Dan Rocca, and Jeremy M. Henley. Ubiquitin c-terminal hydrolase l1 (uch-l1): structure, distribution and roles in brain function and dysfunction. Biochemical Journal, 473:2453-2462, Aug 2016. URL: https://doi.org/10.1042/bcj20160082, doi:10.1042/bcj20160082. This article has 389 citations and is from a domain leading peer-reviewed journal.

5. (ristic2014anoptimalubiquitinproteasome pages 6-7): Gorica Ristic, Wei-Ling Tsou, and Sokol V. Todi. An optimal ubiquitin-proteasome pathway in the nervous system: the role of deubiquitinating enzymes. Frontiers in Molecular Neuroscience, Aug 2014. URL: https://doi.org/10.3389/fnmol.2014.00072, doi:10.3389/fnmol.2014.00072. This article has 107 citations.

6. (genc2019complexityofgenerating pages 9-11): Baris Genc, Oge Gozutok, and P. Hande Ozdinler. Complexity of generating mouse models to study the upper motor neurons: let us shift focus from mice to neurons. International Journal of Molecular Sciences, 20:3848, Aug 2019. URL: https://doi.org/10.3390/ijms20163848, doi:10.3390/ijms20163848. This article has 37 citations.

7. (mi2021abolishinguchl1shydrolase pages 8-9): Zhiping Mi, Hao Liu, Marie E. Rose, Xiecheng Ma, Daniel P. Reay, Jie Ma, Jeremy Henchir, C. Edward Dixon, and Steven H. Graham. Abolishing uchl1's hydrolase activity exacerbates tbi-induced axonal injury and neuronal death in mice. Feb 2021. URL: https://doi.org/10.1016/j.expneurol.2020.113524, doi:10.1016/j.expneurol.2020.113524. This article has 27 citations and is from a peer-reviewed journal.

8. (bishop2016ubiquitincterminalhydrolase pages 9-10): Paul Bishop, Dan Rocca, and Jeremy M. Henley. Ubiquitin c-terminal hydrolase l1 (uch-l1): structure, distribution and roles in brain function and dysfunction. Biochemical Journal, 473:2453-2462, Aug 2016. URL: https://doi.org/10.1042/bcj20160082, doi:10.1042/bcj20160082. This article has 389 citations and is from a domain leading peer-reviewed journal.

9. (genc2019complexityofgenerating pages 6-9): Baris Genc, Oge Gozutok, and P. Hande Ozdinler. Complexity of generating mouse models to study the upper motor neurons: let us shift focus from mice to neurons. International Journal of Molecular Sciences, 20:3848, Aug 2019. URL: https://doi.org/10.3390/ijms20163848, doi:10.3390/ijms20163848. This article has 37 citations.

10. (bishop2016ubiquitincterminalhydrolase pages 8-8): Paul Bishop, Dan Rocca, and Jeremy M. Henley. Ubiquitin c-terminal hydrolase l1 (uch-l1): structure, distribution and roles in brain function and dysfunction. Biochemical Journal, 473:2453-2462, Aug 2016. URL: https://doi.org/10.1042/bcj20160082, doi:10.1042/bcj20160082. This article has 389 citations and is from a domain leading peer-reviewed journal.

11. (tran2018drosophilaubiquitincterminal pages 1-2): Hiep H. Tran, Suong N. A. Dang, Thanh T. Nguyen, Anh M. Huynh, Linh. M. Dao, Kaeko Kamei, Masamitsu Yamaguchi, and Thao T. P. Dang. Drosophila ubiquitin c-terminal hydrolase knockdown model of parkinson’s disease. Scientific Reports, Mar 2018. URL: https://doi.org/10.1038/s41598-018-22804-w, doi:10.1038/s41598-018-22804-w. This article has 34 citations and is from a peer-reviewed journal.

12. (rossor2024theevolvingspectrum pages 12-13): Alexander M. Rossor, Saif Haddad, and Mary M. Reilly. The evolving spectrum of complex inherited neuropathies. Current Opinion in Neurology, 37:427-444, Jul 2024. URL: https://doi.org/10.1097/wco.0000000000001307, doi:10.1097/wco.0000000000001307. This article has 12 citations and is from a peer-reviewed journal.

13. (maresca2021molecularmechanismsbehind pages 24-25): Alessandra Maresca and Valerio Carelli. Molecular mechanisms behind inherited neurodegeneration of the optic nerve. Biomolecules, 11:496, Mar 2021. URL: https://doi.org/10.3390/biom11040496, doi:10.3390/biom11040496. This article has 21 citations.

14. (meyyazhagan2022hereditaryspasticparaplegia pages 18-20): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 197 citations.

15. (tran2018drosophilaubiquitincterminal pages 10-11): Hiep H. Tran, Suong N. A. Dang, Thanh T. Nguyen, Anh M. Huynh, Linh. M. Dao, Kaeko Kamei, Masamitsu Yamaguchi, and Thao T. P. Dang. Drosophila ubiquitin c-terminal hydrolase knockdown model of parkinson’s disease. Scientific Reports, Mar 2018. URL: https://doi.org/10.1038/s41598-018-22804-w, doi:10.1038/s41598-018-22804-w. This article has 34 citations and is from a peer-reviewed journal.

16. (tran2018drosophilaubiquitincterminal pages 2-4): Hiep H. Tran, Suong N. A. Dang, Thanh T. Nguyen, Anh M. Huynh, Linh. M. Dao, Kaeko Kamei, Masamitsu Yamaguchi, and Thao T. P. Dang. Drosophila ubiquitin c-terminal hydrolase knockdown model of parkinson’s disease. Scientific Reports, Mar 2018. URL: https://doi.org/10.1038/s41598-018-22804-w, doi:10.1038/s41598-018-22804-w. This article has 34 citations and is from a peer-reviewed journal.

17. (bishop2016ubiquitincterminalhydrolase pages 7-8): Paul Bishop, Dan Rocca, and Jeremy M. Henley. Ubiquitin c-terminal hydrolase l1 (uch-l1): structure, distribution and roles in brain function and dysfunction. Biochemical Journal, 473:2453-2462, Aug 2016. URL: https://doi.org/10.1042/bcj20160082, doi:10.1042/bcj20160082. This article has 389 citations and is from a domain leading peer-reviewed journal.

18. (puri2024functionaldynamicsof pages 6-8): Sarita Puri and Shang-Te Danny Hsu. Functional dynamics of human ubiquitin c-terminal hydrolases. Frontiers in Biophysics, Nov 2024. URL: https://doi.org/10.3389/frbis.2024.1479898, doi:10.3389/frbis.2024.1479898. This article has 5 citations.

19. (genc2019complexityofgenerating pages 18-20): Baris Genc, Oge Gozutok, and P. Hande Ozdinler. Complexity of generating mouse models to study the upper motor neurons: let us shift focus from mice to neurons. International Journal of Molecular Sciences, 20:3848, Aug 2019. URL: https://doi.org/10.3390/ijms20163848, doi:10.3390/ijms20163848. This article has 37 citations.

## Artifacts

- [Edison artifact artifact-00](UCHL1-Related_Neurodegeneration_with_Optic_Atrophy_and_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-00.md)