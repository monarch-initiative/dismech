---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:34:13.021992'
end_time: '2026-08-01T18:42:53.895414'
duration_seconds: 520.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 93 and Hypertrophic Cardiomyopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Immunodeficiency_93_and_Hypertrophic_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 93 and Hypertrophic Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 93 and Hypertrophic Cardiomyopathy** covering all of the
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
- **Disease Name:** Immunodeficiency 93 and Hypertrophic Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 93 and Hypertrophic Cardiomyopathy** covering all of the
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


# Immunodeficiency 93 with hypertrophic cardiomyopathy: research report

## Executive summary and evidence scope

**Immunodeficiency 93 with hypertrophic cardiomyopathy** is an ultra-rare, autosomal-recessive inborn error of immunity caused by biallelic loss-of-function variants in **FNIP1** (*folliculin-interacting protein 1*). It is best understood as a syndromic early B-cell developmental disorder, usually producing profound B-cell lymphopenia or agammaglobulinemia, together with hypertrophic cardiomyopathy (HCM) and, in some patients, ventricular pre-excitation. Reviews available through 2023 report only **six affected individuals from five unrelated families**, underscoring the extremely limited natural-history evidence. The strongest mechanistic data come from Fnip1-deficient mice and B-cell progenitors rather than human tissue (siggs2016mutationoffnip1 pages 7-8, siggs2016mutationoffnip1 pages 7-7, redmond2022novelgeneticdiscoveries pages 10-11, ramirez2019folliculininteractingprotein pages 1-2).

The principal human report is Niehues et al., **“Mutations of the gene FNIP1 associated with a syndromic autosomal recessive immunodeficiency with cardiomyopathy and pre-excitation syndrome,”** published April 2020, DOI: [10.1002/eji.201948504](https://doi.org/10.1002/eji.201948504). A further human case was reported by Ulaş et al. in May 2024, DOI: [10.1097/MPH.0000000000002862](https://doi.org/10.1097/MPH.0000000000002862). Full patient-level tables and exact HGVS variants from those reports were not retrievable in the searched corpus; consequently, they are not reconstructed or guessed here.

| domain | established finding | evidence type | confidence/limitations |
|---|---|---|---|
| Inheritance / causal gene | Disease is resolved as an autosomal-recessive inborn error of immunity caused by biallelic loss-of-function variants in **FNIP1**; authoritative reviews/classifications describe FNIP1 deficiency as a syndromic predominantly antibody/B-cell defect with cardiomyopathy/pre-excitation features (redmond2022novelgeneticdiscoveries pages 10-11, tangye2023inbornerrorsof pages 13-13) | Human disease reviews/classification; mechanistic support from mouse genetics | Moderate-high confidence for gene-disease relationship; exact OMIM/MONDO row and full primary human case details were not directly retrievable in available evidence |
| Hallmark immune phenotype | Core immune phenotype is **B-cell deficiency/agammaglobulinemia or severe antibody deficiency**, with an early block in B-cell development inferred from human disease reviews and directly demonstrated in Fnip1-deficient mice (redmond2022novelgeneticdiscoveries pages 10-11, tangye2023inbornerrorsof pages 13-13, ramirez2019folliculininteractingprotein pages 1-2, siggs2016mutationoffnip1 pages 3-4, siggs2016mutationoffnip1 pages 1-3) | Human reviews plus primary mouse/in vitro mechanistic studies | High confidence for B-cell developmental defect; frequencies, infection spectrum, and exact immunoglobulin values in humans unavailable from retrieved primary human text |
| Cardiac phenotype | Human FNIP1 deficiency is repeatedly summarized as associated with **hypertrophic cardiomyopathy** and sometimes **pre-excitation syndrome**; mouse Fnip1 loss causes left-ventricular hypertrophy/cardiomyopathy with glycogen accumulation, supporting biological plausibility (siggs2016mutationoffnip1 pages 7-8, siggs2016mutationoffnip1 pages 7-7, siggs2016mutationoffnip1 pages 1-1, siggs2016mutationoffnip1 pages 4-5) | Human review summaries; primary mouse cardiovascular phenotype | Moderate confidence for human HCM association; patient-level echocardiographic/ECG details were not available in accessible case reports |
| Mechanism / pathophysiology | FNIP1 is a regulator within the **FLCN–FNIP1–AMPK–mTORC1** network; in B-cell progenitors, Fnip1 deficiency causes inappropriate mTOR lysosomal localization, increased apoptosis under amino-acid deprivation, increased nuclear **TFE3**, increased lysosome function, and increased autophagic flux. Mouse data also support elevated AMPK activity and tissue-specific metabolic dysregulation in heart and skeletal muscle (siggs2016mutationoffnip1 pages 7-8, backe2022emerginglinkbetween pages 2-4, hasumi2015folliculininteractingproteinsfnip1 pages 1-2, ramirez2019folliculininteractingprotein pages 1-2) | Primary mouse and cell-mechanistic studies; review synthesis | High confidence for pathway involvement in model systems; direct human tissue validation remains limited |
| Diagnosis | Practical diagnosis is by **genetic testing identifying biallelic FNIP1 variants** in a patient with severe B-cell/antibody deficiency plus syndromic features such as HCM/pre-excitation; classification papers recognize FNIP1 among novel monogenic IEIs (redmond2022novelgeneticdiscoveries pages 10-11, tangye2023inbornerrorsof pages 13-13) | Human classification/review evidence | Moderate confidence; no disease-specific diagnostic criteria, biomarker thresholds, or validated screening algorithm were retrieved |
| Management / trials | No disease-specific interventional trials were found. Management in the literature base is supportive and extrapolated from phenotype: immunoglobulin replacement/infection prevention for antibody deficiency and standard cardiology surveillance/management for HCM or conduction disease (supported indirectly by disease classification and absence of trials) (redmond2022novelgeneticdiscoveries pages 10-11, tangye2023inbornerrorsof pages 13-13) | Review/classification evidence plus negative clinical-trial search | Low-moderate confidence for disease-specific efficacy because direct outcome studies were not retrieved |
| Epidemiology | Condition appears **ultra-rare**, reported only in a very small number of families/patients in reviews; no prevalence or incidence estimates were available from the retrieved evidence (redmond2022novelgeneticdiscoveries pages 10-11, tangye2023inbornerrorsof pages 13-13) | Human review summaries | Low confidence for numeric epidemiology because exact counts and denominators were not available in accessible primary sources |
| Mouse model | Fnip1 mutant/knockout mice recapitulate major disease axes: **early B-cell developmental arrest**, reduced/absent peripheral B cells, marginal-zone B-cell sensitivity, **cardiomyopathy/LV hypertrophy**, glycogen accumulation, and altered skeletal-muscle metabolism/AMPK signaling (siggs2016mutationoffnip1 pages 7-8, siggs2016mutationoffnip1 pages 7-7, hasumi2015folliculininteractingproteinsfnip1 pages 4-5, siggs2016mutationoffnip1 pages 1-1, siggs2016mutationoffnip1 pages 3-4, siggs2016mutationoffnip1 pages 4-5, siggs2016mutationoffnip1 pages 1-3) | Primary animal model evidence | High confidence; strong mechanistic relevance, though murine phenotypes cannot substitute for full human natural-history data |
| Evidence gaps | Exact patient variants, ages, sex distribution, penetrance, prognosis, and treatment responses were not established in the retrieved accessible evidence and should not be inferred without the primary human case series/case reports (redmond2022novelgeneticdiscoveries pages 10-11, tangye2023inbornerrorsof pages 13-13) | Evidence-quality assessment | High confidence that these are current evidence gaps in the accessible corpus |


*Table: This table summarizes the strongest currently retrievable evidence for Immunodeficiency 93 with hypertrophic cardiomyopathy, focusing on established findings and explicit limitations. It is useful as a compact knowledge-base scaffold when primary human case details are sparse or inaccessible.*

## 1. Disease information

### Definition and classification

The disorder is a **Mendelian, predominantly antibody-deficiency syndrome** in which deficient FNIP1 function disrupts the metabolic checkpoints required for early B-cell development and also perturbs cardiomyocyte energy sensing. Recent authoritative reviews classify FNIP1 deficiency among monogenic inborn errors affecting B-cell development; the 2024 IUIS update emphasizes that IEIs are classified according to the most consistently reported phenotype and now encompasses more than 500 causal genes (redmond2022novelgeneticdiscoveries pages 10-11, tangye2023inbornerrorsof pages 13-13).

**Preferred name:** Immunodeficiency 93 with hypertrophic cardiomyopathy.  
**Synonyms:** FNIP1 deficiency; FNIP1-related immunodeficiency; syndromic agammaglobulinemia due to FNIP1 deficiency; autosomal-recessive immunodeficiency with cardiomyopathy and pre-excitation syndrome; B-cell deficiency with cardiomyopathy.  
**OMIM:** commonly catalogued as **Immunodeficiency 93 with hypertrophic cardiomyopathy**; the exact phenotype accession should be verified directly in OMIM before database import because an accessible OMIM record was not retrieved.  
**MONDO/Orphanet:** no confidently verified disease-specific accession was recovered. A parent mapping to *inborn error of immunity* and *predominantly antibody deficiency* is appropriate until a dedicated MONDO record is confirmed.  
**ICD-10/ICD-11/MeSH:** no unique code exists. Component coding would use congenital/predominantly antibody immunodeficiency and hypertrophic cardiomyopathy codes rather than a disease-specific code.

Evidence is **aggregated disease-level literature**, not EHR-derived. The tiny human evidence base consists of individual case reports/series.

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is **germline biallelic FNIP1 loss of function**, inherited autosomal recessively. FNIP1 encodes a cytoplasmic protein that binds folliculin (FLCN), FNIP2, AMPK subunits, and the Hsp90 chaperone machinery. Mouse studies demonstrate that a recessive splice-donor mutation generating aberrant transcripts and loss of detectable FNIP1 protein causes B-cell deficiency and cardiomyopathy (backe2022emerginglinkbetween pages 2-4, hasumi2015folliculininteractingproteinsfnip1 pages 1-2, siggs2016mutationoffnip1 pages 4-5, siggs2016mutationoffnip1 pages 1-3).

### Genetic and environmental risk

* **Genetic risk:** two pathogenic or likely pathogenic FNIP1 alleles in trans. Consanguinity increases the probability of homozygosity for a rare recessive allele but is not itself causal.
* **Susceptibility loci/modifiers:** none established in humans. Fnip2 expression is tissue-dependent and can partly compensate for Fnip1 in mice, making **FNIP2** a plausible modifier, but not a validated human modifier (hasumi2015folliculininteractingproteinsfnip1 pages 1-2, hasumi2015folliculininteractingproteinsfnip1 pages 4-4).
* **Environmental causes:** none known. Infections expose the consequences of antibody deficiency rather than initiating the Mendelian disease.
* **Protective variants or exposures:** none established.
* **Gene–environment interaction:** nutrient and energetic stress are mechanistically relevant. Fnip1-deficient pre-B cells show abnormal mTOR localization and increased apoptosis during lysine or arginine deprivation, suggesting that cellular nutrient availability modifies survival downstream of the genetic defect; this has not been quantified clinically (ramirez2019folliculininteractingprotein pages 1-2).

## 3. Phenotypes

Human frequencies cannot be estimated reliably from six or slightly more reported patients. “Frequent” below means recurrent across reports/reviews, not a population percentage.

| Phenotype | Type and course | Suggested HPO term |
|---|---|---|
| Profound reduction/absence of circulating B cells | Laboratory abnormality; childhood presentation; severe and persistent | **B-cell lymphopenia** (HP:0010976) |
| Agammaglobulinemia or marked hypogammaglobulinemia | Laboratory abnormality; chronic; predisposes to infection | **Agammaglobulinemia** (HP:0004432), **Hypogammaglobulinemia** (HP:0004313) |
| Recurrent infections, especially respiratory | Symptom/clinical course; episodic on chronic susceptibility | **Recurrent respiratory infections** (HP:0002205), **Recurrent bacterial infections** (HP:0002718) |
| Hypertrophic cardiomyopathy/LV hypertrophy | Clinical and imaging sign; childhood onset reported; severity variable | **Hypertrophic cardiomyopathy** (HP:0001639), **Left ventricular hypertrophy** (HP:0001712) |
| Ventricular pre-excitation | ECG abnormality; reported in the defining human series | **Ventricular preexcitation** (HP:0005136) |
| Neutropenia | Laboratory finding in some later cases; prevalence unresolved | **Neutropenia** (HP:0001875) |
| Altered skeletal-muscle phenotype | Strong in mice; insufficiently characterized in humans | **Skeletal muscle abnormality** (HP:0003011), if clinically demonstrated |

The mouse phenotype directly demonstrates an early developmental block: homozygotes lacked peripheral and splenic B cells and bone marrow IgM⁺/IgD⁺ cells, while B220-low progenitors remained. Heterozygotes had reduced marginal-zone B cells, indicating gene-dose sensitivity (siggs2016mutationoffnip1 pages 3-4, siggs2016mutationoffnip1 pages 4-5, siggs2016mutationoffnip1 pages 1-3).

**Quality of life:** no disease-specific EQ-5D, SF-36, PROMIS, or pediatric quality-of-life study exists. Expected burdens include recurrent infection, lifelong replacement therapy, repeated cardiac surveillance, exercise restrictions where clinically indicated, arrhythmia anxiety, and possible heart-failure symptoms. These are clinically reasonable consequences, not measured FNIP1-specific outcomes.

## 4. Genetic and molecular information

### Gene

* **Gene:** **FNIP1**, folliculin-interacting protein 1.
* **Molecular role:** FLCN-binding protein, AMPK regulator, Hsp90 co-chaperone, and regulator of mTORC1/TFE3-dependent lysosomal and autophagic programs.
* **Origin:** pathogenic disease alleles are germline; there is no evidence that somatic FNIP1 mutation causes this immunodeficiency.
* **Mechanism:** recessive loss of function. The disease architecture and null/near-null mouse phenotypes support haplosufficiency for the major syndrome, although heterozygous mice show subtle marginal-zone B-cell effects (backe2022emerginglinkbetween pages 2-4, siggs2016mutationoffnip1 pages 3-4).

### Variants

The defining literature reports homozygous or compound-heterozygous variants, including truncating alleles; a review notes that one disease-associated missense change lies in a region important for Hsp90 interaction and FNIP1 stability. Exact patient-level HGVS expressions, ClinVar accessions, ACMG classifications, and gnomAD frequencies could not be validated from accessible full text and should be imported only after direct ClinVar/primary-paper review (backe2022emerginglinkbetween pages 2-4, redmond2022novelgeneticdiscoveries pages 10-11).

No pathogenic chromosomal rearrangement, repeat expansion, mitochondrial-DNA variant, epigenetic signature, anticipation, or established germline mosaicism has been reported. No validated modifier gene or disease-specific methylation/proteomic/metabolomic biomarker is available.

## 5. Environmental and infectious information

There is no evidence that toxins, pollution, radiation, smoking, alcohol, diet, occupation, or exercise causes FNIP1 deficiency. Pathogens are **secondary opportunists or recurrent infectious challenges**, not causal agents. Published summaries support infection susceptibility resulting from severe humoral deficiency, but the retrieved evidence does not permit a reliable organism-by-organism infection spectrum.

Exercise down-regulates muscle FNIP1 in experimental systems, and myofiber-specific Fnip1 loss enhances PGC-1α-dependent macrophage recruitment and angiogenesis in mice. This is mechanistically interesting but does not establish exercise as protective or harmful in affected humans; exercise advice must instead follow individualized HCM assessment.

## 6. Mechanism and pathophysiology

### Causal chain in B cells

1. **Biallelic FNIP1 loss** disrupts the FLCN–FNIP metabolic/chaperone complex.
2. Nutrient and energy sensing through **AMPK and mTORC1** becomes improperly coordinated.
3. In Fnip1-deficient pre-B cells, mTOR remains inappropriately localized at lysosomes during nutrient deprivation; AMPK and mTORC1 can both appear activated.
4. **TFE3** accumulates in nuclei, increasing lysosomal target-gene expression, lysosome number/function, and autophagic flux.
5. Developing B cells are unusually vulnerable to metabolic stress and apoptosis, producing a block around the pre-B-cell stage.
6. The downstream clinical result is profound B-cell lymphopenia, agammaglobulinemia, and recurrent infection (backe2022emerginglinkbetween pages 2-4, ramirez2019folliculininteractingprotein pages 1-2).

An important experimental caution is that neither genetic AMPK inhibition, pharmacologic mTORC1 inhibition, BCL-xL-mediated survival restoration, nor BCL2 overexpression fully corrected B-cell development. Thus, the mechanism is not reducible to a single linear “AMPK high” or “mTOR high” lesion (siggs2016mutationoffnip1 pages 7-7, ramirez2019folliculininteractingprotein pages 1-2).

### Cardiac chain

Fnip1 loss increases activity of γ2-containing AMPK complexes in neonatal mouse myocardium, accompanied by cardiomyocyte glycogen accumulation and left-ventricular hypertrophy resembling PRKAG2-associated metabolic cardiomyopathy. FNIP1 therefore appears to restrain cardiac energy-sensing pathways in a tissue- and AMPK-complex-specific manner (siggs2016mutationoffnip1 pages 7-8, siggs2016mutationoffnip1 pages 7-7, siggs2016mutationoffnip1 pages 1-1).

### Suggested ontology annotations

* **GO biological process:** B-cell differentiation (GO:0030183); B-cell homeostasis (GO:0001782); cellular response to nutrient levels (GO:0031669); AMPK signaling; TOR signaling (GO:0031929); autophagy (GO:0006914); lysosome organization (GO:0007040); mitochondrial biogenesis; cardiac muscle-cell hypertrophy.
* **GO cellular component:** lysosome (GO:0005764); cytosol (GO:0005829); AMPK complex; mTORC1 complex; mitochondrion (GO:0005739).
* **Cell Ontology:** B-cell progenitor (CL:0000826); precursor B cell (CL:0000817); mature B cell (CL:0000785); cardiomyocyte (CL:0000746); skeletal muscle fiber (CL:0000187); macrophage (CL:0000235).

No human single-cell, spatial-transcriptomic, multi-omic, lipidomic, or disease-specific iPSC-cardiomyocyte dataset was identified. A 2024 CRISPR/Cas9 HL-60 abstract investigated neutropenia, but conference-abstract evidence is insufficient to define a mature granulopoietic mechanism.

## 7. Anatomical structures affected

**Primary systems:** immune/hematopoietic and cardiovascular systems.

* **Bone marrow**—early B-cell progenitor compartment; UBERON:0002371.
* **Peripheral blood, spleen, lymphoid tissue**—markedly depleted mature B-cell compartment; spleen UBERON:0002106.
* **Heart/myocardium**, particularly left ventricular muscle—hypertrophy and metabolic/glycogen abnormalities; heart UBERON:0000948, myocardium UBERON:0002349, left ventricle UBERON:0002084.
* **Skeletal muscle**—altered oxidative-fiber and mitochondrial phenotype is well demonstrated in mice but incompletely defined clinically.
* **Subcellular sites:** cytoplasm, lysosome, mitochondria, nucleus of TFE3-responsive cells, and the AMPK/mTOR complexes.

The cardiac and immune abnormalities are systemic rather than lateralized.

## 8. Temporal development and natural history

The recognized syndrome is predominantly **pediatric and chronic/lifelong**. Immunodeficiency may become evident after loss of maternally acquired antibody or during recurrent childhood infections. Cardiac hypertrophy and pre-excitation may be detected concurrently or through syndromic screening. Onset and progression vary, and there are insufficient longitudinal data to define stages, median age at onset, annual progression, remission, or critical treatment windows.

There is no evidence of spontaneous genetic remission. Immunoglobulin therapy can reduce infection burden but does not restore endogenous B-cell development. Cardiac disease requires continued surveillance because HCM and conduction abnormalities can evolve independently of infectious control.

## 9. Inheritance and population

* **Inheritance:** autosomal recessive.
* **Penetrance:** probably high for severe biallelic loss of function, but cannot be quantified.
* **Expressivity:** variable, particularly for cardiomyopathy, conduction disease, neutropenia, and residual immune function.
* **Prevalence/incidence:** unknown; no cases-per-100,000 estimate exists. The literature base of approximately six individuals in five families through early reviews supports classification as ultra-rare (redmond2022novelgeneticdiscoveries pages 10-11).
* **Sex ratio, ancestry distribution, carrier frequency, founder effects:** not established.
* **Consanguinity:** relevant to recurrence of rare homozygous alleles but no universal requirement.
* **Anticipation:** not expected and not reported.
* **Recurrence risk:** when both parents are confirmed carriers, each pregnancy has a 25% probability of an affected child, 50% probability of a heterozygous carrier, and 25% probability of inheriting neither familial allele.

## 10. Diagnostics

### Recommended clinical work-up

1. **Immune evaluation:** CBC with differential; absolute lymphocyte subsets including CD19/CD20 B cells; IgG, IgA, IgM and IgE; vaccine-specific antibody titers where safe and interpretable; infection history; and assessment for bronchiectasis or chronic lung injury when indicated.
2. **Cardiac evaluation:** ECG for pre-excitation or conduction abnormalities; echocardiography for wall thickness, outflow obstruction and systolic/diastolic function; ambulatory rhythm monitoring; cardiac MRI when echocardiography is insufficient; biomarkers such as BNP/troponin only as clinically indicated.
3. **Genetic confirmation:** sequencing plus deletion/duplication analysis of **FNIP1**, with parental phasing to demonstrate biallelic variants in trans. A comprehensive IEI/agammaglobulinemia panel, WES, or WGS is preferable when the phenotype is atypical or single-gene testing is negative.
4. **Variant interpretation:** ACMG/AMP criteria, population frequency, predicted loss of function, segregation, RNA studies for splice variants, and protein/functional assays where available.

WES/WGS is particularly useful because the combined immune–cardiac phenotype can be mistaken for two independent disorders. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless other findings suggest those mechanisms.

### Differential diagnosis

Important alternatives include **BTK-related X-linked agammaglobulinemia**, autosomal-recessive agammaglobulinemias involving IGHM, CD79A/B, BLNK, PIK3R1, TCF3 and SLC39A7/ZIP7, combined immunodeficiencies, PRKAG2 glycogen-storage cardiomyopathy with pre-excitation, Danon disease, Pompe disease, mitochondrial cardiomyopathy, RASopathy-associated HCM, and sarcomeric HCM. The combination of severe early B-cell deficiency plus HCM/pre-excitation and biallelic FNIP1 variants is the key discriminator.

There are no validated standardized clinical criteria, newborn-screening analyte, liquid biopsy, or diagnostic metabolomic signature.

## 11. Outcome and prognosis

No reliable survival curve, mortality rate, median life expectancy, or five-/ten-year outcome is available. Principal morbidity risks are severe or recurrent infection, chronic pulmonary damage, arrhythmia, progressive HCM, heart failure, and potentially sudden cardiac death by extrapolation from HCM—not from quantified FNIP1-specific cohorts.

Prognosis is likely influenced by residual B-cell/antibody function, infection burden before immunoglobulin replacement, ventricular wall thickness and function, outflow obstruction, arrhythmia/pre-excitation, and access to multidisciplinary care. None is validated as an FNIP1-specific prognostic biomarker.

## 12. Treatment and real-world implementation

There is **no approved FNIP1-directed therapy and no relevant disease-specific interventional trial was found**.

### Current management

* **Immunoglobulin replacement**—intravenous or subcutaneous—to maintain protective IgG exposure and reduce bacterial infections. Suggested NCIT concepts: *Intravenous Immunoglobulin Therapy* and *Subcutaneous Immunoglobulin Therapy*.
* **Prompt antimicrobial treatment** and, for recurrent infections despite adequate replacement, individualized antibacterial prophylaxis. Live vaccines are generally avoided in profound immunodeficiency until immune competence is defined.
* **Pulmonary care:** surveillance for bronchiectasis, airway clearance where required, and culture-directed treatment.
* **HCM management:** pediatric/adult cardiology follow-up; beta blocker or nondihydropyridine calcium-channel blocker when clinically indicated; conventional management of heart failure or outflow obstruction; exercise advice based on HCM risk assessment.
* **Pre-excitation/arrhythmia:** electrophysiology evaluation, ambulatory monitoring, and catheter ablation when indicated by pathway properties or clinical arrhythmia.
* **Advanced cardiac interventions:** implantable cardioverter-defibrillator, septal reduction, or transplantation only under standard HCM indications; no FNIP1-specific outcome data exist.

Hematopoietic stem-cell transplantation has no established evidence base for this disorder and would not be expected to correct cardiomyocyte-intrinsic FNIP1 deficiency. Likewise, mTOR inhibitors, AMPK modulators, gene replacement, CRISPR editing, RNA therapy, and Hsp90-directed treatment remain experimental concepts. Failure of simple AMPK or mTOR manipulation to rescue murine B-cell development argues against premature pathway-targeted clinical use (siggs2016mutationoffnip1 pages 7-7, ramirez2019folliculininteractingprotein pages 1-2).

## 13. Prevention

Primary prevention by lifestyle change is impossible because the condition is germline. Effective prevention is genetic and complication-focused:

* **Genetic counseling**, carrier testing of at-risk relatives, and cascade testing.
* **Reproductive options:** prenatal diagnosis and preimplantation genetic testing for a known familial variant pair.
* **Secondary prevention:** early immune and cardiac assessment of genetically affected siblings, ideally before serious infection or cardiac symptoms.
* **Tertiary prevention:** immunoglobulin replacement, antimicrobial prophylaxis when indicated, pulmonary surveillance, ECG/echocardiographic follow-up, rhythm management, and individualized HCM precautions.
* **Vaccination:** household contacts should be appropriately immunized; patient vaccine decisions require immunology review. Inactivated vaccines are generally safe but may be poorly immunogenic; live vaccines may be contraindicated depending on the breadth of immune dysfunction.

No population newborn or carrier-screening program is currently justified by prevalence data, although targeted familial screening is appropriate.

## 14. Other species and natural disease

No naturally occurring veterinary FNIP1-deficiency syndrome was identified in companion animals, livestock, or wildlife, and there is no zoonotic or cross-species transmission. Relevant orthologues are evolutionarily conserved, particularly mouse **Fnip1**, but model-organism phenotypes are experimentally induced rather than naturally transmitted disease.

## 15. Model organisms and experimental systems

### Mouse models

The best-characterized models are constitutive Fnip1-null mice and the recessive ENU-induced **hamel** splice allele. They reproduce the two defining disease axes:

* nearly absent peripheral B cells and developmental arrest before mature IgM⁺/IgD⁺ stages;
* left-ventricular hypertrophy/cardiomyopathy with cardiomyocyte glycogen accumulation;
* elevated γ2-containing AMPK activity in neonatal myocardium;
* altered skeletal-muscle fiber composition and mitochondrial metabolism (siggs2016mutationoffnip1 pages 7-8, siggs2016mutationoffnip1 pages 7-7, siggs2016mutationoffnip1 pages 1-1, siggs2016mutationoffnip1 pages 3-4, siggs2016mutationoffnip1 pages 4-5).

The accessible primary mouse paper’s central conclusion is accurately captured by its title: **“Mutation of Fnip1 is associated with B-cell deficiency, cardiomyopathy, and elevated AMPK activity.”** Published June 2016, DOI: [10.1073/pnas.1607592113](https://doi.org/10.1073/pnas.1607592113) (siggs2016mutationoffnip1 pages 1-1).

A second primary study provides the following abstract-level statement: **“constitutive disruption of Fnip1 in mice resulted in a lack of peripheral B cells because of a block in B cell development at the pre–B cell stage.”** It further reports increased nuclear TFE3, lysosome number/function, and autophagic flux. Published November 1, 2019, DOI: [10.4049/jimmunol.1900395](https://doi.org/10.4049/jimmunol.1900395) (ramirez2019folliculininteractingprotein pages 1-2).

### Strengths and limitations

These models have excellent face validity for B-cell deficiency and cardiomyopathy and are suitable for studying metabolic checkpoints, lineage-specific AMPK complexes, lysosomal signaling, autophagy, and candidate rescue strategies. Limitations include species differences in immunoglobulin biology and cardiac physiology, incomplete replication of the human infection history, and the inability of constitutive null models to separate developmental from adult maintenance functions.

## Recent developments, 2023–2024

1. A 2023 synthesis of human B-cell IEIs continued to recognize FNIP1 deficiency as an early B-cell developmental defect and emphasized that human bone-marrow evidence remains limited (tangye2023inbornerrorsof pages 13-13).
2. Recent metabolic work has expanded FNIP1 biology beyond AMPK alone, implicating FLCN/FNIP chaperoning, TFE3/TFEB, lysosomal function, mitochondrial homeostasis, PGC-1α and tissue-specific responses. These findings refine—but do not yet change—clinical care (backe2022emerginglinkbetween pages 2-4, ramirez2019folliculininteractingprotein pages 1-2).
3. A new homozygous-FNIP1 patient report appeared in May 2024, confirming continued expansion of the phenotype, but accessible evidence did not support reliable recalculation of frequencies or genotype–phenotype relationships.
4. A 2024 CRISPR/Cas9 HL-60 conference study began investigating neutropenia, representing functional-genomics follow-up rather than validated clinical evidence.
5. The 2024 IUIS classification update, published in 2025, describes a rapidly expanding IEI landscape of **508 genes and 17 phenocopies**, reinforcing the need to interpret FNIP1 through expert IEI frameworks rather than as nonspecific CVID (poli2025humaninbornerrors pages 29-30).

## Knowledge-base conclusions

The highest-confidence annotations are: **biallelic FNIP1 loss of function → disturbed FLCN/AMPK/mTORC1/TFE3 metabolic control → early pre-B-cell developmental failure → profound B-cell/antibody deficiency**, with a parallel cardiomyocyte metabolic defect producing **HCM and sometimes pre-excitation**. Human case numbers remain too small for dependable phenotype frequencies, penetrance, epidemiology, prognosis, or treatment-response statistics. Exact HGVS variants, MONDO/OMIM accessions, and ClinVar classifications should be verified directly against the primary case reports and current databases before automated ingestion.

References

1. (siggs2016mutationoffnip1 pages 7-8): Owen M. Siggs, Alexander Stockenhuber, Mukta Deobagkar-Lele, Katherine R. Bull, Tanya L. Crockford, Bethany L. Kingston, Greg Crawford, Consuelo Anzilotti, Violetta Steeples, Sahar Ghaffari, Gabor Czibik, Mohamed Bellahcene, Hugh Watkins, Houman Ashrafian, Benjamin Davies, Angela Woods, David Carling, Arash Yavari, Bruce Beutler, and Richard J. Cornall. Mutation of fnip1 is associated with b-cell deficiency, cardiomyopathy, and elevated ampk activity. Proceedings of the National Academy of Sciences, 113:E3706-E3715, Jun 2016. URL: https://doi.org/10.1073/pnas.1607592113, doi:10.1073/pnas.1607592113. This article has 65 citations and is from a highest quality peer-reviewed journal.

2. (siggs2016mutationoffnip1 pages 7-7): Owen M. Siggs, Alexander Stockenhuber, Mukta Deobagkar-Lele, Katherine R. Bull, Tanya L. Crockford, Bethany L. Kingston, Greg Crawford, Consuelo Anzilotti, Violetta Steeples, Sahar Ghaffari, Gabor Czibik, Mohamed Bellahcene, Hugh Watkins, Houman Ashrafian, Benjamin Davies, Angela Woods, David Carling, Arash Yavari, Bruce Beutler, and Richard J. Cornall. Mutation of fnip1 is associated with b-cell deficiency, cardiomyopathy, and elevated ampk activity. Proceedings of the National Academy of Sciences, 113:E3706-E3715, Jun 2016. URL: https://doi.org/10.1073/pnas.1607592113, doi:10.1073/pnas.1607592113. This article has 65 citations and is from a highest quality peer-reviewed journal.

3. (redmond2022novelgeneticdiscoveries pages 10-11): Margaret T. Redmond, Rebecca Scherzer, and Benjamin T. Prince. Novel genetic discoveries in primary immunodeficiency disorders. Clinical Reviews in Allergy & Immunology, 63:55-74, Jan 2022. URL: https://doi.org/10.1007/s12016-021-08881-2, doi:10.1007/s12016-021-08881-2. This article has 30 citations and is from a peer-reviewed journal.

4. (ramirez2019folliculininteractingprotein pages 1-2): Julita A. Ramírez, Terri Iwata, Heon Park, Mark Tsang, Janella Kang, Katy Cui, Winnie Kwong, Richard G. James, Masaya Baba, Laura S. Schmidt, and Brian M. Iritani. Folliculin interacting protein 1 maintains metabolic homeostasis during b cell development by modulating ampk, mtorc1, and tfe3. The Journal of Immunology, 203:2899-2908, Dec 2019. URL: https://doi.org/10.4049/jimmunol.1900395, doi:10.4049/jimmunol.1900395. This article has 25 citations.

5. (tangye2023inbornerrorsof pages 13-13): Stuart G. Tangye, Tina Nguyen, Elissa K. Deenick, Vanessa L. Bryant, and Cindy S. Ma. Inborn errors of human b cell development, differentiation, and function. The Journal of Experimental Medicine, Jun 2023. URL: https://doi.org/10.1084/jem.20221105, doi:10.1084/jem.20221105. This article has 72 citations.

6. (siggs2016mutationoffnip1 pages 3-4): Owen M. Siggs, Alexander Stockenhuber, Mukta Deobagkar-Lele, Katherine R. Bull, Tanya L. Crockford, Bethany L. Kingston, Greg Crawford, Consuelo Anzilotti, Violetta Steeples, Sahar Ghaffari, Gabor Czibik, Mohamed Bellahcene, Hugh Watkins, Houman Ashrafian, Benjamin Davies, Angela Woods, David Carling, Arash Yavari, Bruce Beutler, and Richard J. Cornall. Mutation of fnip1 is associated with b-cell deficiency, cardiomyopathy, and elevated ampk activity. Proceedings of the National Academy of Sciences, 113:E3706-E3715, Jun 2016. URL: https://doi.org/10.1073/pnas.1607592113, doi:10.1073/pnas.1607592113. This article has 65 citations and is from a highest quality peer-reviewed journal.

7. (siggs2016mutationoffnip1 pages 1-3): Owen M. Siggs, Alexander Stockenhuber, Mukta Deobagkar-Lele, Katherine R. Bull, Tanya L. Crockford, Bethany L. Kingston, Greg Crawford, Consuelo Anzilotti, Violetta Steeples, Sahar Ghaffari, Gabor Czibik, Mohamed Bellahcene, Hugh Watkins, Houman Ashrafian, Benjamin Davies, Angela Woods, David Carling, Arash Yavari, Bruce Beutler, and Richard J. Cornall. Mutation of fnip1 is associated with b-cell deficiency, cardiomyopathy, and elevated ampk activity. Proceedings of the National Academy of Sciences, 113:E3706-E3715, Jun 2016. URL: https://doi.org/10.1073/pnas.1607592113, doi:10.1073/pnas.1607592113. This article has 65 citations and is from a highest quality peer-reviewed journal.

8. (siggs2016mutationoffnip1 pages 1-1): Owen M. Siggs, Alexander Stockenhuber, Mukta Deobagkar-Lele, Katherine R. Bull, Tanya L. Crockford, Bethany L. Kingston, Greg Crawford, Consuelo Anzilotti, Violetta Steeples, Sahar Ghaffari, Gabor Czibik, Mohamed Bellahcene, Hugh Watkins, Houman Ashrafian, Benjamin Davies, Angela Woods, David Carling, Arash Yavari, Bruce Beutler, and Richard J. Cornall. Mutation of fnip1 is associated with b-cell deficiency, cardiomyopathy, and elevated ampk activity. Proceedings of the National Academy of Sciences, 113:E3706-E3715, Jun 2016. URL: https://doi.org/10.1073/pnas.1607592113, doi:10.1073/pnas.1607592113. This article has 65 citations and is from a highest quality peer-reviewed journal.

9. (siggs2016mutationoffnip1 pages 4-5): Owen M. Siggs, Alexander Stockenhuber, Mukta Deobagkar-Lele, Katherine R. Bull, Tanya L. Crockford, Bethany L. Kingston, Greg Crawford, Consuelo Anzilotti, Violetta Steeples, Sahar Ghaffari, Gabor Czibik, Mohamed Bellahcene, Hugh Watkins, Houman Ashrafian, Benjamin Davies, Angela Woods, David Carling, Arash Yavari, Bruce Beutler, and Richard J. Cornall. Mutation of fnip1 is associated with b-cell deficiency, cardiomyopathy, and elevated ampk activity. Proceedings of the National Academy of Sciences, 113:E3706-E3715, Jun 2016. URL: https://doi.org/10.1073/pnas.1607592113, doi:10.1073/pnas.1607592113. This article has 65 citations and is from a highest quality peer-reviewed journal.

10. (backe2022emerginglinkbetween pages 2-4): Sarah J. Backe, Rebecca A. Sager, Katherine A. Meluni, Mark R. Woodford, Dimitra Bourboulia, and Mehdi Mollapour. Emerging link between tsc1 and fnip co-chaperones of hsp90 and cancer. Biomolecules, 12:928, Jul 2022. URL: https://doi.org/10.3390/biom12070928, doi:10.3390/biom12070928. This article has 9 citations.

11. (hasumi2015folliculininteractingproteinsfnip1 pages 1-2): Hisashi Hasumi, Masaya Baba, Yukiko Hasumi, Martin Lang, Ying Huang, HyoungBin F. Oh, Masayuki Matsuo, Maria J. Merino, Masahiro Yao, Yusuke Ito, Mitsuko Furuya, Yasuhiro Iribe, Tatsuhiko Kodama, Eileen Southon, Lino Tessarollo, Kunio Nagashima, Diana C. Haines, W. Marston Linehan, and Laura S. Schmidt. Folliculin-interacting proteins fnip1 and fnip2 play critical roles in kidney tumor suppression in cooperation with flcn. Proceedings of the National Academy of Sciences, 112:E1624-E1631, Mar 2015. URL: https://doi.org/10.1073/pnas.1419502112, doi:10.1073/pnas.1419502112. This article has 127 citations and is from a highest quality peer-reviewed journal.

12. (hasumi2015folliculininteractingproteinsfnip1 pages 4-5): Hisashi Hasumi, Masaya Baba, Yukiko Hasumi, Martin Lang, Ying Huang, HyoungBin F. Oh, Masayuki Matsuo, Maria J. Merino, Masahiro Yao, Yusuke Ito, Mitsuko Furuya, Yasuhiro Iribe, Tatsuhiko Kodama, Eileen Southon, Lino Tessarollo, Kunio Nagashima, Diana C. Haines, W. Marston Linehan, and Laura S. Schmidt. Folliculin-interacting proteins fnip1 and fnip2 play critical roles in kidney tumor suppression in cooperation with flcn. Proceedings of the National Academy of Sciences, 112:E1624-E1631, Mar 2015. URL: https://doi.org/10.1073/pnas.1419502112, doi:10.1073/pnas.1419502112. This article has 127 citations and is from a highest quality peer-reviewed journal.

13. (hasumi2015folliculininteractingproteinsfnip1 pages 4-4): Hisashi Hasumi, Masaya Baba, Yukiko Hasumi, Martin Lang, Ying Huang, HyoungBin F. Oh, Masayuki Matsuo, Maria J. Merino, Masahiro Yao, Yusuke Ito, Mitsuko Furuya, Yasuhiro Iribe, Tatsuhiko Kodama, Eileen Southon, Lino Tessarollo, Kunio Nagashima, Diana C. Haines, W. Marston Linehan, and Laura S. Schmidt. Folliculin-interacting proteins fnip1 and fnip2 play critical roles in kidney tumor suppression in cooperation with flcn. Proceedings of the National Academy of Sciences, 112:E1624-E1631, Mar 2015. URL: https://doi.org/10.1073/pnas.1419502112, doi:10.1073/pnas.1419502112. This article has 127 citations and is from a highest quality peer-reviewed journal.

14. (poli2025humaninbornerrors pages 29-30): M. Cecilia Poli, Ivona Aksentijevich, Ahmed Aziz Bousfiha, Charlotte Cunningham-Rundles, Sophie Hambleton, Christoph Klein, Tomohiro Morio, Capucine Picard, Anne Puel, Nima Rezaei, Mikko R.J. Seppänen, Raz Somech, Helen C. Su, Kathleen E. Sullivan, Troy R. Torgerson, Isabelle Meyts, and Stuart G. Tangye. Human inborn errors of immunity: 2024 update on the classification from the international union of immunological societies expert committee. Journal of Human Immunity, Apr 2025. URL: https://doi.org/10.70962/jhi.20250003, doi:10.70962/jhi.20250003. This article has 398 citations.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_93_and_Hypertrophic_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md)