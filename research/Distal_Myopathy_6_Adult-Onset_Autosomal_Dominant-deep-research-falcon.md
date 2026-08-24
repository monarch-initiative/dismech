---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-02T04:58:09.074604'
end_time: '2026-08-02T05:08:38.336855'
duration_seconds: 629.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Distal Myopathy 6, Adult-Onset, Autosomal Dominant
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Distal_Myopathy_6_Adult-Onset_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Distal Myopathy 6, Adult-Onset, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Distal Myopathy 6, Adult-Onset, Autosomal Dominant** covering all of the
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
- **Disease Name:** Distal Myopathy 6, Adult-Onset, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Distal Myopathy 6, Adult-Onset, Autosomal Dominant** covering all of the
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


# Distal Myopathy 6, Adult-Onset, Autosomal Dominant

## Executive summary

**Distal myopathy 6, adult-onset (MPD6)** is an exceptionally rare, dominantly inherited skeletal-muscle disorder caused by heterozygous variants in **ACTN2**, which encodes the sarcomeric Z-disc protein α-actinin-2. The defining reported phenotype is adult-onset, often asymmetric weakness and atrophy of the tibialis anterior/ankle dorsiflexors, followed by proximal spread; muscle biopsy may show rimmed vacuoles. The initial evidence involved four families—three from one village in northern Spain and one Swedish family—with full penetrance reported within those pedigrees. Only two disease-associated substitutions were firmly documented in the retrieved foundational evidence: **c.1459T>C (p.Cys487Arg)** and **c.392T>C (p.Leu131Pro)**. Population prevalence, long-term outcome rates, quantitative cardiac risk, and treatment-response data remain unavailable. There is no approved disease-modifying therapy or MPD6-specific clinical trial.

A crucial nomenclature warning is that **MPD6 (ACTN2; OMIM 618655) is not “myofibrillar myopathy 6,” the BAG3-related childhood disorder**. Older reviews may use “MFM6” for BAG3 disease, creating a serious risk of miscoding. The current neuromuscular gene table unambiguously assigns adult-onset distal myopathy 6 to ACTN2. (cohen2021the2022version pages 14-15, dimachkie2014distalmyopathies. pages 14-16, benarroch2024the2024version pages 14-15)

| Domain | Established finding | Evidence type / strength | Key identifiers or quantitative facts |
|---|---|---|---|
| Disease identity | Distal myopathy 6, adult-onset is the ACTN2-related autosomal dominant distal myopathy phenotype designated MPD6 | Authoritative disease table + review-level confirmation; strong for nomenclature/assignment (cohen2021the2022version pages 14-15, benarroch2024the2024version pages 14-15) | OMIM phenotype **618655**; inheritance **AD**; locus **1q43**; gene **ACTN2**; protein **actinin alpha-2** |
| Causal gene | The causal gene is **ACTN2**, a sarcomeric Z-disc gene expressed in skeletal and cardiac muscle | Authoritative gene-disease table + functional review; strong for gene assignment, moderate for mechanistic interpretation (cohen2021the2022version pages 14-15, wadmore2021theroleof pages 2-4) | **ACTN2 OMIM 102573**; chromosome **1q43** |
| Key pathogenic variants | Reported MPD6-associated heterozygous missense variants are **c.1459T>C (p.Cys487Arg)** and **c.392T>C (p.Leu131Pro)** | Primary cohort abstract evidence + review synthesis; moderate-strong (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1, wadmore2021theroleof pages 4-5) | p.Cys487Arg in families 1-3; p.Leu131Pro in family 4 |
| Reported families / geography | Four families were reported: **three from the same village in northern Spain** and **one from Sweden** | Primary cohort abstract evidence; moderate (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1) | **4 families total**; clustering suggests possible local aggregation for p.Cys487Arg but no founder study established |
| Core phenotype | Clinical presentation is **adult-onset asymmetric distal weakness**, initially with **tibialis anterior atrophy** and **ankle dorsiflexion** involvement, later spreading proximally | Primary cohort abstract evidence; moderate (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1) | Pattern: distal lower-limb onset, **asymmetric**, then **proximal progression** |
| Pathology | Muscle biopsy showed **rimmed vacuolar pathology** | Primary cohort abstract evidence; moderate (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1) | Histopathology: **rimmed vacuoles** |
| Penetrance / segregation | Variants **co-segregated** with disease and showed **full penetrance** in the reported families | Primary cohort abstract evidence; moderate (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1) | **Full penetrance** reported in all 4 families |
| Protein/domain context | ACTN2 contains an **actin-binding domain (ABD)**, **4 spectrin repeats**, and **EF-hand region**; MPD6 variants map to the **ABD** (p.Leu131Pro) and **spectrin-repeat region** (p.Cys487Arg) | Functional/structural review evidence; moderate for domain mapping, indirect for MPD6 mechanism (wadmore2021theroleof pages 2-4, wadmore2021theroleof pages 4-5) | p.Leu131Pro: ABD; p.Cys487Arg: spectrin-like repeat region |
| Population frequency | In a 2021 ACTN2 review, both MPD6 variants were reported as **absent from gnomAD v3.1** | Review evidence; moderate (wadmore2021theroleof pages 4-5) | **Absent in gnomAD v3.1**: p.Leu131Pro, p.Cys487Arg |
| Mechanistic interpretation | Best-supported mechanism is disruption of **Z-disc / sarcomere integrity** with downstream myofibrillar degeneration; exact MPD6-specific causal mechanism remains incompletely defined | Indirect functional review + gene function data; moderate/limited for MPD6-specific causality (wadmore2021theroleof pages 2-4, wadmore2021theroleof pages 4-5) | ACTN2 is an actin cross-linker/scaffold at the Z-disc; **direct MPD6 functional assay evidence missing** |
| Cardiac association | ACTN2 is allelic to cardiomyopathy phenotypes, but direct, quantitative cardiac-risk data for MPD6 are not established in the retrieved MPD6 evidence | Strong for allelic relationship; limited for MPD6-specific risk (cohen2021the2022version pages 14-15, benarroch2024the2024version pages 14-15, OpenTargets Search: -ACTN2) | Allelic to **CMH23** and **CMD1AA**; pragmatic cardiac surveillance may be reasonable, but **MPD6-specific penetrance unknown** |
| Epidemiology | **No robust prevalence or incidence estimate** was identified for MPD6 | Evidence gap; weak/absent (benarroch2024the2024version pages 14-15) | Prevalence: **not established**; incidence: **not established** |
| Natural history granularity | Adult onset and progression from distal to proximal weakness are established, but detailed age-at-onset ranges, disease duration, respiratory outcomes, and survival are not well quantified in the retrieved evidence | Limited primary evidence; weak-moderate (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1) | Age-specific quantitative natural history: **missing/limited** |
| Diagnostics | Diagnosis currently relies on **clinical pattern recognition + muscle pathology + molecular testing** (multigene panel/WES/WGS in neuromuscular practice) rather than a disease-specific biomarker | General neuromuscular diagnostic review + direct disease genetics; moderate, partly extrapolated (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1) | No validated MPD6-specific biomarker, screening test, or diagnostic criteria set identified |
| Treatment | **No approved disease-modifying therapy** specific to MPD6 was identified | Evidence gap; weak/absent (findlay2024dominantlyinheritedmuscle pages 15-16, findlay2024dominantlyinheritedmuscle pages 16-16) | Management appears supportive/rehabilitative; ACTN2-specific pharmacotherapy: **none established** |
| Trials / implementation | **No relevant clinical trial** for ACTN2-related MPD6 was identified in the retrieved searches | Trial-search negative evidence; weak/absent (cohen2021the2022version pages 14-15, dimachkie2014distalmyopathies. pages 14-16) | Relevant interventional trial: **none found** |
| Missing evidence summary | No robust data were found for prevalence, incidence, sex ratio, quality of life metrics, prognosis/survival, founder effect confirmation, environmental modifiers, omics biomarkers, or validated animal/natural disease models specific to MPD6 | Evidence gap statement synthesized from available sources; weak/absent (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1, wadmore2021theroleof pages 4-5) | Clearly missing: epidemiology, QoL, survival, response rates, prevention trials, MPD6-specific model system validation |


*Table: This table summarizes the strongest currently retrievable evidence for ACTN2-related Distal Myopathy 6, including disease identity, causal variants, phenotype, pathology, and major evidence gaps. It is useful as a compact curation-ready snapshot for a disease knowledge base entry.*

## 1. Disease information

### Definition and identifiers

MPD6 is a **Mendelian, autosomal-dominant distal myopathy** characterized by primary skeletal-muscle degeneration beginning distally in adulthood. The 2024 neuromuscular gene table lists it as item 4.10, locus **1q43**, disease symbol **MPD6**, phenotype **OMIM 618655**, and causal gene **ACTN2** (gene OMIM **102573**). (benarroch2024the2024version pages 14-15)

Recommended identifiers and labels are:

- **Preferred name:** Myopathy, distal, 6, adult-onset
- **Synonyms:** distal myopathy 6; MPD6; ACTN2-related adult-onset distal myopathy; α-actinin-2-related distal myopathy
- **OMIM phenotype:** 618655
- **Gene:** ACTN2; Ensembl **ENSG00000077522**; protein α-actinin-2
- **Chromosomal locus:** 1q43
- **MONDO:** a dedicated MPD6 identifier was not resolved in the retrieved resources; do not substitute the broader ACTN2 congenital-myopathy term **MONDO:0032852**
- **Orphanet:** no MPD6-specific identifier was resolved
- **ICD-10/ICD-11:** no unique disease-specific code was identified; coding generally falls under hereditary/other specified myopathy or muscular-dystrophy groupings, depending on local practice
- **MeSH:** no unique MPD6 descriptor; “Distal Myopathies”/“Muscular Diseases” are suitable broader indexing concepts.

The source evidence is **aggregated disease-level literature and family studies**, not individual EHR data. The foundational observations are patient-level pedigree data subsequently aggregated into OMIM-style and neuromuscular gene-table entries.

## 2. Etiology

### Causal and genetic risk factors

The established cause is a **germline heterozygous ACTN2 missense variant**. Three northern-Spanish families carried **c.1459T>C, p.Cys487Arg**, while the Swedish family carried **c.392T>C, p.Leu131Pro**. Both variants co-segregated with disease; the report described full penetrance in the studied families. (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1)

The 2021 Z-disc review reported both variants as absent from gnomAD v3.1, supporting rarity but not by itself proving pathogenicity. p.Leu131Pro lies in the actin-binding domain, whereas p.Cys487Arg lies in a spectrin-repeat region. (wadmore2021theroleof pages 4-5)

Family history is therefore the principal recognized risk factor. Each child of a heterozygous affected individual has a **50% transmission probability**, although phenotypic severity and exact age at onset cannot yet be predicted reliably.

### Environmental, protective, and gene–environment factors

No reproducible toxin, infection, occupation, diet, alcohol, smoking, activity, sex, or other environmental cause has been established. No protective ACTN2 allele, modifier gene, dietary factor, or pharmacologic prophylaxis has been demonstrated. Gene–environment interactions have not been systematically studied. Ordinary aging likely determines when an inherited vulnerability becomes clinically evident, but that is a natural-history inference rather than a proven interaction.

## 3. Phenotypes

The direct human evidence supports the following curation set. (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1)

| Phenotype | Characterization | Suggested HPO term |
|---|---|---|
| Adult-onset muscle weakness | Chronic/insidious onset; detailed age range unavailable | Adult onset, **HP:0003581** |
| Distal lower-limb weakness | Core manifestation; initially ankle dorsiflexors | Distal muscle weakness, **HP:0002460** |
| Ankle dorsiflexion weakness | Early/defining manifestation | Foot dorsiflexor weakness, **HP:0009053** |
| Tibialis anterior atrophy | Early objective sign | Tibialis anterior muscle atrophy; use muscular atrophy **HP:0003202** if a specific descendant is unavailable |
| Asymmetric weakness | Common defining pattern in the original families | Asymmetric muscle weakness, **HP:0031500** or current HPO equivalent |
| Proximal spread | Later manifestation; frequency and timing unquantified | Proximal muscle weakness, **HP:0003701** |
| Progressive course | Distal disease progresses into proximal muscles | Progressive muscle weakness, **HP:0003323** |
| Rimmed vacuoles | Histopathologic abnormality | Rimmed vacuoles, **HP:0003805** |

The report did not provide sufficiently robust frequencies beyond the pedigree-level description. “Full penetrance” should not be translated into 100% lifetime penetrance across all ACTN2 variants or populations because only four families were studied.

**Functional/QoL impact:** dorsiflexor weakness is expected to impair toe clearance, gait, stair climbing, balance, and community mobility and to increase falls; later proximal weakness may compromise transfers and endurance. No MPD6-specific EQ-5D, SF-36, PROMIS, employment, ambulation-loss, or caregiver-burden dataset was found.

Cardiac manifestations are biologically important because other ACTN2 variants cause hypertrophic and dilated cardiomyopathy, but a quantitative cardiac phenotype was not established for the two MPD6 variants in the retrieved primary evidence. ACTN2 is formally allelic to CMH23 and CMD1AA. (benarroch2024the2024version pages 14-15, OpenTargets Search: -ACTN2)

## 4. Genetic and molecular information

### Gene and variants

**ACTN2** encodes α-actinin-2, a Z-disc actin-crosslinking and scaffolding protein expressed in skeletal and cardiac striated muscle. Its architecture includes an N-terminal actin-binding domain, four central spectrin repeats, and a C-terminal EF-hand region. (wadmore2021theroleof pages 2-4)

| Variant | Class/origin | Domain | Population observation | Evidence interpretation |
|---|---|---|---|---|
| ACTN2 c.392T>C; p.Leu131Pro | Heterozygous germline missense | Actin-binding domain | Absent from gnomAD v3.1 in the 2021 review | Co-segregated with fully penetrant disease in one Swedish family |
| ACTN2 c.1459T>C; p.Cys487Arg | Heterozygous germline missense | Spectrin-repeat region | Absent from gnomAD v3.1 in the 2021 review | Co-segregated with disease in three Spanish families |

These should be curated using current ClinVar assertions and transcript-specific HGVS normalization at implementation time; the retrieved literature did not supply a current ClinVar review status or ACMG evidence matrix. No somatic origin is implicated. (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1, wadmore2021theroleof pages 4-5)

### Allelic disorders and modifiers

ACTN2 alleles also cause hypertrophic cardiomyopathy, dilated cardiomyopathy and congenital myopathy with structured cores/Z-line abnormalities. Open Targets independently links ACTN2 to dilated cardiomyopathy 1AA and congenital myopathy with structured cores and Z-line abnormalities. These are **allelic disorders, not synonymous with MPD6**. (benarroch2024the2024version pages 14-15, OpenTargets Search: -ACTN2)

No validated modifier gene, protective allele, anticipation, germline-mosaicism series, epigenetic signature, pathogenic copy-number variant, translocation, or inversion specific to MPD6 was found.

## 5. Environmental information

MPD6 is not an infectious, toxic, radiation-induced, nutritional, or occupational disorder. No pathogen, pollutant, medication, toxin, or lifestyle exposure is known to initiate it. Avoiding prolonged immobility and maintaining safe activity may reduce secondary deconditioning, but these measures do not prevent inheritance or molecular disease onset. There is no evidence for vaccination, antimicrobial therapy, detoxification, smoking cessation, or a special diet as disease-specific prevention.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. A heterozygous ACTN2 missense substitution alters α-actinin-2 within either its actin-binding or spectrin-repeat region.
2. Mutant α-actinin-2 is incorporated into—or perturbs—the Z-disc, where normal α-actinin-2 crosslinks actin filaments and scaffolds mechanosignaling proteins.
3. Abnormal actin interaction, dimer/scaffold stability, or Z-disc integration compromises sarcomere organization and force transmission.
4. Repeated contraction produces cumulative myofibrillar stress and defective protein homeostasis.
5. Myofiber degeneration and rimmed-vacuole formation lead to selective tibialis-anterior atrophy, dorsiflexion weakness, and eventual proximal spread.

Steps 1 and the clinical endpoint are supported directly by human segregation/pathology; intermediate steps remain the leading Z-disc-based model rather than a completely demonstrated MPD6-specific pathway. Experiments on other ACTN2 variants show reduced thermal stability, impaired actin binding, weak Z-disc integration and aggregate formation, supporting the general plausibility of this mechanism but not proving identical effects for p.Leu131Pro or p.Cys487Arg. (wadmore2021theroleof pages 2-4, wadmore2021theroleof pages 4-5)

Suggested annotations include:

- **GO biological process:** actin filament organization (GO:0007015); sarcomere organization (GO:0045214); muscle contraction (GO:0006936); actin filament bundle assembly (GO:0051017); cellular response to mechanical stimulus (GO:0071260); protein stabilization (GO:0050821); autophagy/proteostasis terms only as downstream hypotheses
- **GO cellular component:** Z disc (GO:0030018); sarcomere (GO:0030017); myofibril (GO:0030016); actin cytoskeleton (GO:0015629)
- **GO molecular function:** actin binding (GO:0003779); structural constituent of muscle (GO:0008307); protein binding (GO:0005515)
- **Cell Ontology:** skeletal muscle fiber **CL:0000188**; skeletal muscle satellite stem cell **CL:0000596** only for secondary regenerative studies; cardiomyocyte **CL:0000746** for safety/allelic-phenotype surveillance.

No MPD6-specific transcriptomic, proteomic, metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omic signature was identified. Consequently, there is no validated molecular biomarker or metabolic abnormality. Immune-mediated inflammation is not an established primary mechanism.

## 7. Anatomical structures affected

The primary organ is **skeletal muscle**, especially distal lower-limb muscle. The earliest named muscle is the **tibialis anterior**, affecting the anterior compartment of the leg and ankle dorsiflexion. Disease later reaches proximal limb muscles. Weakness is often asymmetric, but it is not described as strictly unilateral. (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1)

Suggested anatomical annotations are skeletal muscle tissue (**UBERON:0001134**), lower limb segment (**UBERON:0002103**), leg (**UBERON:0000978**), tibialis anterior muscle, ankle joint (**UBERON:0001488**), and upper/proximal limb musculature for later disease. At cellular level, multinucleated skeletal myofibers are affected; subcellular disease centers on the sarcomeric Z-disc/myofibril. Cardiac muscle is a surveillance tissue because of ACTN2 allelism, not a proven obligatory MPD6 target.

## 8. Temporal development

Onset is **adult and insidious**, followed by a chronic progressive course. The apparent sequence is: asymmetric tibialis-anterior atrophy/dorsiflexion weakness → broader distal lower-limb involvement → proximal muscle involvement. Exact median onset, annual progression, time to assistive device, time to loss of ambulation, and respiratory trajectory were not available. (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1)

No relapsing-remitting course, spontaneous remission, acute attacks, or treatment-induced remission has been described. Disease is presumed lifelong after onset. The most plausible intervention window is early after molecular diagnosis, before fixed fatty replacement and contractures, but this has not been tested.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Full penetrance was reported in the original families, but penetrance may be age-dependent because onset is adult and the evidence base is small. Expressivity is insufficiently quantified; asymmetry itself indicates phenotypic variability. There is no evidence of repeat-expansion anticipation. (donkervoort2019o.18recessivemutationsin pages 1-1, amthor2019o.19pax7deficiencycauses pages 1-1)

Three p.Cys487Arg families originated from the same northern-Spanish village, which raises a founder hypothesis, but no haplotype or population study establishing a founder effect was retrieved. The fourth family was Swedish and carried p.Leu131Pro. No prevalence, incidence, carrier frequency, sex ratio, ethnic enrichment, or worldwide geographic distribution can be estimated responsibly from four pedigrees. Consanguinity is not etiologically relevant to a dominant disorder, although it does not preclude occurrence.

## 10. Diagnostics

### Recommended workflow

1. **Clinical examination:** document distal-versus-proximal pattern, asymmetry, tibialis-anterior bulk, ankle dorsiflexion strength, gait, reflexes, sensory findings and contractures.
2. **Serum tests:** CK, aldolase, AST/ALT and other routine myopathy studies. No MPD6-specific CK threshold is established.
3. **Electrophysiology:** EMG to demonstrate a myopathic process; nerve-conduction studies help exclude hereditary neuropathy/peroneal neuropathy.
4. **Muscle MRI:** characterize selective anterior-compartment involvement, quantify fatty replacement, choose a biopsy site, and provide a longitudinal outcome measure. Imaging is strongly recommended in modern myopathy workups. (wadmore2021theroleof pages 12-13)
5. **Genetic testing:** use a comprehensive distal-myopathy/myofibrillar-myopathy panel including ACTN2, or WES/WGS if panel testing is negative. Confirm candidate variants by an orthogonal method and perform segregation analysis.
6. **Biopsy:** now second-line when genetics is inconclusive or variant interpretation requires functional support. Histology may reveal myopathic change and rimmed vacuoles; frozen muscle is preferable to formalin-only tissue for neuromuscular diagnosis. (donkervoort2019o.18recessivemutationsin pages 1-1, wadmore2021theroleof pages 12-13)
7. **Cardiac baseline:** ECG, echocardiography and symptom/family-history review are prudent because ACTN2 also causes cardiomyopathy, although MPD6-specific screening intervals are not evidence-based. (benarroch2024the2024version pages 14-15, OpenTargets Search: -ACTN2)

Single-gene ACTN2 sequencing is efficient in a family with a known variant. WES/WGS is valuable for unresolved phenotypes and can detect competing diagnoses; WGS improves noncoding and structural-variant detection. CMA, karyotyping, FISH, mitochondrial-DNA sequencing and repeat-expansion testing are not first-line unless the phenotype or family history suggests an alternative diagnosis. RNA sequencing of muscle can support splice-variant interpretation but has no established role for the two missense MPD6 variants.

### Differential diagnosis

Important alternatives include TTN tibial muscular dystrophy, MYH7 Laing distal myopathy, FLNC distal myopathy, TIA1 Welander disease, MYOT myotilinopathy, GNE myopathy, ANO5/dysferlin disease, VCP multisystem proteinopathy, BAG3/MYOT/DES myofibrillar myopathy, hereditary motor neuropathy/Charcot–Marie–Tooth disease, inclusion-body myositis, and focal peroneal neuropathy. Preserved sensation and myopathic EMG favor myopathy; inheritance, onset age, MRI pattern, biopsy, and molecular testing provide final discrimination. The 2024 gene table distinguishes MPD6 from these numbered distal-myopathy entities. (benarroch2024the2024version pages 14-15)

There are no standardized MPD6 clinical diagnostic criteria, newborn screening program, population screening test, or validated liquid-biopsy assay. Predictive testing should be offered only with genetics counseling because onset is adult and no preventive molecular therapy exists.

## 11. Outcome and prognosis

The disease is progressive and likely causes increasing gait disability, falls and reduced independence. However, no 5- or 10-year survival, life-expectancy, mortality, ambulation-loss, ventilation, cardiomyopathy penetrance, hospitalization, or standardized disability statistics were found. The original evidence did not establish respiratory failure as a defining feature. Prognostic biomarkers are unavailable.

Potential prognostic variables—still unvalidated—include age at onset, baseline dorsiflexion strength, MRI fat fraction, proximal involvement, falls, CK, and cardiac findings. Recovery of chronically replaced muscle is unlikely, but rehabilitation can improve safety, conditioning and use of remaining function. No evidence supports spontaneous reversal of the underlying myopathy.

## 12. Treatment

There is **no approved ACTN2/MPD6 disease-modifying treatment** and no MPD6-specific response-rate or adverse-event dataset.

Recommended supportive management is individualized:

- Physiotherapy emphasizing safe submaximal strengthening, range of motion, aerobic conditioning and avoidance of prolonged deconditioning or injurious eccentric overload.
- Occupational therapy and home/work adaptation.
- Ankle–foot orthoses for foot drop; cane, trekking poles, walker or wheelchair as function requires.
- Falls assessment, footwear review, and treatment of secondary pain.
- Monitoring for contractures and orthopedic complications; surgery only for standard functional indications, not to treat the molecular disorder.
- Respiratory evaluation if symptoms or advanced generalized weakness develop.
- Baseline and periodic cardiac assessment guided by findings and specialist judgment.

Suitable broad NCIt intervention concepts include **Physical Therapy (NCIT:C15308)**, **Occupational Therapy (NCIT:C15309)**, rehabilitation, orthotic device, genetic counseling, electrocardiography and echocardiography; exact NCIt codes should be verified against the deployment terminology release.

Dominant myopathies are challenging gene-therapy targets because simply adding a normal gene may not neutralize a toxic or dominant-negative allele. Contemporary expert analysis highlights allele-specific RNA interference, ASOs and editing as general strategies, but none has reached MPD6 clinical testing. (findlay2024dominantlyinheritedmuscle pages 15-16, findlay2024dominantlyinheritedmuscle pages 16-16)

Clinical-trial searches found no relevant ACTN2/MPD6 interventional study or NCT identifier. Pharmacogenomic guidance and combination-treatment algorithms are therefore not applicable.

## 13. Prevention

**Primary prevention:** no lifestyle or environmental measure prevents disease in a person carrying a pathogenic allele. Vaccination and antimicrobial prophylaxis are not disease-specific.

**Genetic/reproductive prevention:** genetic counseling should explain autosomal-dominant transmission, age-dependent uncertainty and the 50% transmission probability. Once a familial pathogenic variant is established, options include cascade testing, prenatal diagnosis and preimplantation genetic testing. Predictive testing of asymptomatic adults requires informed consent and discussion of uncertain onset/severity and insurance or psychosocial implications.

**Secondary prevention:** identify affected relatives before substantial disability; monitor gait/falls and obtain a cardiac baseline. There is no newborn or population screening program.

**Tertiary prevention:** preserve mobility, prevent falls and contractures, avoid deconditioning, and promptly manage cardiac, respiratory or orthopedic complications if they arise.

## 14. Other species and natural disease

No naturally occurring veterinary disease confidently equivalent to human ACTN2-MPD6 was identified. Therefore no breed, VBO identifier, veterinary prevalence or cross-species transmission issue can be assigned. The disorder is genetic and noncommunicable, with no zoonotic potential.

ACTN2 orthologs are evolutionarily conserved across vertebrates, reflecting the conserved role of α-actinin-2 in striated-muscle Z-discs. Relevant comparative species include **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Rattus norvegicus (10116)** and **Danio rerio (7955)**, but orthology alone does not establish a natural MPD6 phenotype.

## 15. Model organisms and research systems

No mature, independently validated model reproducing the complete human MPD6 phenotype was found in the retrieved literature. Suitable future systems include:

- CRISPR knock-in mouse models carrying Actn2 p.Leu131Pro or p.Cys487Arg, assessed longitudinally for asymmetric tibialis-anterior disease, rimmed vacuoles, force and cardiac phenotypes.
- Zebrafish knock-in or mosaic-expression models for rapid sarcomere and locomotor assays.
- Patient-derived myoblasts/myotubes and isogenic CRISPR-corrected controls.
- Patient iPSC-derived skeletal myotubes and cardiomyocytes to separate skeletal and cardiac allele effects.
- Engineered three-dimensional muscle for force, Z-disc organization and proteostasis assays.

Important limitations are species differences in lifespan, loading and muscle-use patterns; a model may show cardiac disease without the selective adult human tibialis-anterior phenotype. ACTN2 studies in cardiomyocyte systems demonstrate the feasibility of modeling variant-dependent Z-disc integration, calcium-channel interactions and drug response, but those findings concern other ACTN2 alleles and must not be treated as direct MPD6 therapeutic evidence. (wadmore2021theroleof pages 2-4)

## Recent developments and expert assessment

The **2024 neuromuscular gene table** retained MPD6 as an ACTN2 disorder, confirming that the 2019 gene–disease assignment remains current. (benarroch2024the2024version pages 14-15) A 2024 conference report described ACTN2 mutational screening and an apparent actin-binding-domain aggregation hotspot, indicating active expansion of the allelic spectrum, but full peer-reviewed patient-level evidence was not available in the retrieved corpus. More broadly, the 2024 review of dominant muscle disorders argues that dominant-negative or toxic mechanisms will require allele-selective suppression, editing, or combined suppression-and-replacement rather than conventional gene addition. (findlay2024dominantlyinheritedmuscle pages 15-16)

The authoritative interpretation is therefore cautious: MPD6 is a well-defined but **very sparsely characterized** ACTN2-related distal myopathy. Its gene assignment and core phenotype are credible; precise epidemiology, variant-specific mechanism, cardiac risk, natural history, biomarkers and therapy remain research gaps.

## Key source record and abstract wording

- **Savarese et al., 2019**, “Mutations in ACTN2 gene cause a novel form of adult-onset distal myopathy,” conference publication in *Neuromuscular Disorders* 29:S120. The retrievable abstract text reports “four families,” “adult-onset, asymmetric muscle weakness,” initial “atrophy of tibialis anterior” and progression to proximal muscles, with “full penetrance” and co-segregation. DOI-linked conference record: https://doi.org/10.1016/j.nmd.2019.06.298. (donkervoort2019o.18recessivemutationsin pages 1-1)
- **Cohen et al.**, published December 2021, *The 2022 version of the gene table of neuromuscular disorders*. DOI: https://doi.org/10.1016/j.nmd.2021.11.004. This identifies MPD6/OMIM 618655, ACTN2 and 1q43. (cohen2021the2022version pages 14-15)
- **Wadmore, Azad & Gehmlich**, published 18 March 2021, *The Role of Z-disc Proteins in Myopathy and Cardiomyopathy*. DOI: https://doi.org/10.3390/ijms22063058. Abstract wording: “The Z-disc acts as a protein-rich structure to tether thin filament in the contractile units” and functions as a “(bio-mechanical) signalling hub.” It reviews ACTN2 structure, variants and population frequencies. (wadmore2021theroleof pages 2-4, wadmore2021theroleof pages 4-5)
- **Benarroch et al.**, published January 2024, *The 2024 version of the gene table of neuromuscular disorders (nuclear genome)*. DOI: https://doi.org/10.1016/j.nmd.2023.12.007. (benarroch2024the2024version pages 14-15)
- **Findlay**, published October 2024, *Dominantly inherited muscle disorders: understanding their complexity and exploring therapeutic approaches*. DOI: https://doi.org/10.1242/dmm.050720. Its abstract emphasizes that gene replacement used for recessive loss-of-function disease is “not readily translatable to most dominant myopathies,” supporting the need for allele-directed strategies. (findlay2024dominantlyinheritedmuscle pages 15-16)

**Evidence limitations:** the foundational MPD6 report was available principally as a conference abstract, and exact PMID metadata for it was not resolved. Accordingly, detailed ages, CK values, MRI distributions, cardiac testing, respiratory outcomes and individual-level longitudinal data should remain null fields in a knowledge base until verified from a full primary publication or subsequent cohort.

References

1. (cohen2021the2022version pages 14-15): Enzo Cohen, Gisèle Bonne, François Rivier, and Dalil Hamroun. The 2022 version of the gene table of neuromuscular disorders (nuclear genome). Neuromuscular Disorders, 31:1313-1357, Dec 2021. URL: https://doi.org/10.1016/j.nmd.2021.11.004, doi:10.1016/j.nmd.2021.11.004. This article has 64 citations and is from a peer-reviewed journal.

2. (dimachkie2014distalmyopathies. pages 14-16): Mazen M. Dimachkie and Richard J. Barohn. Distal myopathies. Neurologic clinics, 32 3:817-42,x, Aug 2014. URL: https://doi.org/10.1016/j.ncl.2014.04.004, doi:10.1016/j.ncl.2014.04.004. This article has 26 citations and is from a peer-reviewed journal.

3. (benarroch2024the2024version pages 14-15): Louise Benarroch, Gisèle Bonne, François Rivier, and Dalil Hamroun. The 2024 version of the gene table of neuromuscular disorders (nuclear genome). Jan 2024. URL: https://doi.org/10.1016/j.nmd.2023.12.007, doi:10.1016/j.nmd.2023.12.007. This article has 39 citations and is from a peer-reviewed journal.

4. (wadmore2021theroleof pages 2-4): Kirsty Wadmore, Amar J. Azad, and Katja Gehmlich. The role of z-disc proteins in myopathy and cardiomyopathy. International Journal of Molecular Sciences, 22:3058, Mar 2021. URL: https://doi.org/10.3390/ijms22063058, doi:10.3390/ijms22063058. This article has 76 citations.

5. (donkervoort2019o.18recessivemutationsin pages 1-1): S. Donkervoort, Y. Hu, X. Lornage, C. Kutzner, M. Mroczek, S. Neuhaus, N. Kuntz, A. Töpf, S. Monges, F. Lubieniecki, K. Chao, J. Böhm, N. Romero, V. Straub, J. Laporte, A. Foley, C. Ottenheijm, T. Hoppe, and C. Bönnemann. O.18recessive mutations in the myosin chaperone unc-45b impair muscle myofibrillar integrity, manifesting as progressive myopathy with eccentric cores. Neuromuscular Disorders, 29:S120, Oct 2019. URL: https://doi.org/10.1016/j.nmd.2019.06.298, doi:10.1016/j.nmd.2019.06.298. This article has 0 citations and is from a peer-reviewed journal.

6. (amthor2019o.19pax7deficiencycauses pages 1-1): H. Amthor, A. Marg, H. Escobar, S. Grunwald, E. Metzler, J. Kieshauer, E. Malfatti, D. Mompoint, S. Quijano-Roy, R. Carlier, and S. Spuler. O.19pax7 deficiency causes mild congenital myopathy with rigid spine and respiratory insufficiency. Neuromuscular Disorders, 29:S120, Oct 2019. URL: https://doi.org/10.1016/j.nmd.2019.06.299, doi:10.1016/j.nmd.2019.06.299. This article has 0 citations and is from a peer-reviewed journal.

7. (wadmore2021theroleof pages 4-5): Kirsty Wadmore, Amar J. Azad, and Katja Gehmlich. The role of z-disc proteins in myopathy and cardiomyopathy. International Journal of Molecular Sciences, 22:3058, Mar 2021. URL: https://doi.org/10.3390/ijms22063058, doi:10.3390/ijms22063058. This article has 76 citations.

8. (OpenTargets Search: -ACTN2): Open Targets Query (-ACTN2, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (findlay2024dominantlyinheritedmuscle pages 15-16): Andrew R. Findlay. Dominantly inherited muscle disorders: understanding their complexity and exploring therapeutic approaches. Disease Models & Mechanisms, Oct 2024. URL: https://doi.org/10.1242/dmm.050720, doi:10.1242/dmm.050720. This article has 10 citations and is from a domain leading peer-reviewed journal.

10. (findlay2024dominantlyinheritedmuscle pages 16-16): Andrew R. Findlay. Dominantly inherited muscle disorders: understanding their complexity and exploring therapeutic approaches. Disease Models & Mechanisms, Oct 2024. URL: https://doi.org/10.1242/dmm.050720, doi:10.1242/dmm.050720. This article has 10 citations and is from a domain leading peer-reviewed journal.

11. (wadmore2021theroleof pages 12-13): Kirsty Wadmore, Amar J. Azad, and Katja Gehmlich. The role of z-disc proteins in myopathy and cardiomyopathy. International Journal of Molecular Sciences, 22:3058, Mar 2021. URL: https://doi.org/10.3390/ijms22063058, doi:10.3390/ijms22063058. This article has 76 citations.

## Artifacts

- [Edison artifact artifact-00](Distal_Myopathy_6_Adult-Onset_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-00.md)