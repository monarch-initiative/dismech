---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:53.340535'
end_time: '2026-04-04T12:50:13.257622'
duration_seconds: 439.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: COL11A2-Related Hearing Loss
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COL11A2-Related Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COL11A2-Related Hearing Loss** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** COL11A2-Related Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COL11A2-Related Hearing Loss** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# COL11A2-Related Hearing Loss — Comprehensive Disease Characteristics Report

## Target disease
**Disease name:** COL11A2-Related Hearing Loss (Mendelian; spectrum includes nonsyndromic and syndromic presentations) (mcguirt1999mutationsincol11a2 pages 1-2, chen2005mutationofcol11a2 pages 2-5, iwasa2015nonocularsticklersyndrome pages 3-4).

**Note on identifiers:** In the evidence retrieved in this run, authoritative ontology/disease-resource identifiers (MONDO, Orphanet, ICD-10/11, MeSH, OMIM IDs) were not directly available; therefore this report anchors the condition to well-established *deafness locus* identifiers **DFNA13** (autosomal dominant) and **DFNB53** (autosomal recessive), and to COL11A2-related non-ocular Stickler syndrome / Stickler syndrome type 3 and OSMED as described in the clinical genetics literature (mcguirt1999mutationsincol11a2 pages 1-2, chen2005mutationofcol11a2 pages 2-5, iwasa2015nonocularsticklersyndrome pages 3-4, acke2022hearinglossin pages 4-6).

---

## 1. Disease information
### 1.1 Definition and current understanding
**COL11A2-related hearing loss** refers to hereditary hearing impairment caused by pathogenic variants in **COL11A2**, encoding the α2 chain of **type XI collagen**, an extracellular-matrix (ECM) fibrillar collagen that contributes to cochlear structures including the **tectorial membrane (TM)** (masaki2009col11a2deletionreveals pages 1-2, sellon2019thetectorialmembrane pages 1-3).

Clinically, COL11A2 pathogenic variants can cause:
- **Autosomal dominant nonsyndromic hearing loss (DFNA13)** (mcguirt1999mutationsincol11a2 pages 1-2, mcguirt1999mutationsincol11a2 pages 5-6).
- **Autosomal recessive nonsyndromic hearing loss (DFNB53)** (chen2005mutationofcol11a2 pages 2-5).
- **Syndromic disease with hearing loss**, including **COL11A2-related non-ocular Stickler syndrome (Stickler syndrome type 3)** and COL11A2-associated skeletal dysplasias (e.g., OSMED) in the broader disease spectrum (iwasa2015nonocularsticklersyndrome pages 3-4, acke2022hearinglossin pages 4-6, chen2005mutationofcol11a2 pages 2-5).

### 1.2 Common synonyms / alternative names
- **DFNA13** (COL11A2-related autosomal dominant nonsyndromic hearing loss) (mcguirt1999mutationsincol11a2 pages 1-2).
- **DFNB53** (COL11A2-related autosomal recessive nonsyndromic hearing loss) (chen2005mutationofcol11a2 pages 2-5).
- **Non-ocular Stickler syndrome / Stickler syndrome type 3 (COL11A2-related)** (iwasa2015nonocularsticklersyndrome pages 3-4, acke2022hearinglossin pages 4-6).
- **OSMED (otospondylomegaepiphyseal dysplasia)** in the COL11A2 phenotypic spectrum (chen2005mutationofcol11a2 pages 2-5, acke2022hearinglossin pages 4-6).

### 1.3 Evidence source type
The information summarized here is derived from **aggregated disease-level reviews** plus **individual/family-level primary clinical genetics reports**, and **animal model/mechanistic studies** (acke2022hearinglossin pages 4-6, acke2012hearingimpairmentin pages 10-10, mcguirt1999mutationsincol11a2 pages 1-2, chen2005mutationofcol11a2 pages 2-5, masaki2009col11a2deletionreveals pages 1-2).

---

## 2. Etiology
### 2.1 Disease causal factors (genetic)
**Primary cause:** germline pathogenic variants in **COL11A2** (mcguirt1999mutationsincol11a2 pages 1-2, chen2005mutationofcol11a2 pages 2-5, iwasa2015nonocularsticklersyndrome pages 3-4).

**Inheritance:**
- **Autosomal dominant (AD):** DFNA13; also AD non-ocular Stickler syndrome reported with COL11A2 variants (mcguirt1999mutationsincol11a2 pages 1-2, iwasa2015nonocularsticklersyndrome pages 3-4).
- **Autosomal recessive (AR):** DFNB53 (chen2005mutationofcol11a2 pages 2-5).

**Pathogenic variant examples (from primary studies):**
- DFNA13 (AD): **p.Arg549Cys** and **p.Gly323Glu** (McGuirt et al., 1999; DOI: https://doi.org/10.1038/70516; publication month/year: Dec 1999) (mcguirt1999mutationsincol11a2 pages 1-2, mcguirt1999mutationsincol11a2 pages 4-5).
- DFNB53 (AR): **p.Pro621Thr** (Chen et al., 2005; DOI: https://doi.org/10.1136/jmg.2005.032615; Oct 2005) (chen2005mutationofcol11a2 pages 2-5).
- Non-ocular Stickler syndrome (AD) example: a COL11A2 frameshift deletion reported as **p.1312_1315del4** (Iwasa et al., 2015; DOI: https://doi.org/10.1177/0003489415575044; Mar 2015) (iwasa2015nonocularsticklersyndrome pages 3-4).

### 2.2 Variant type and functional consequences (current evidence)
- **Missense substitutions** in the collagen triple-helix domain are implicated in DFNA13 and DFNB53 (mcguirt1999mutationsincol11a2 pages 1-2, chen2005mutationofcol11a2 pages 2-5).
- A **frameshift** variant was reported in a family with AD non-ocular Stickler syndrome and hearing loss (iwasa2015nonocularsticklersyndrome pages 3-4).
- In a Col11a2-null mouse model, **loss of type XI collagen** perturbs TM collagen organization and TM mechanical anisotropy, consistent with a structural/biomechanical mechanism (masaki2009col11a2deletionreveals pages 1-2).

### 2.3 Risk factors / protective factors / gene–environment interactions
For this Mendelian disorder, **genotype** is the dominant determinant; the retrieved sources did not provide human data on environmental risk modifiers or protective factors specific to COL11A2-related hearing loss.

Nevertheless, recent experimental cochlear proteomics suggests that **noise exposure can perturb ECM/collagen proteins including COL11A2**, implicating ECM remodeling as a shared axis for genetic and environmental injury to hearing (Shi et al., 2023; DOI: https://doi.org/10.1007/s12033-022-00557-2; Oct 2023) (shi2023acutenoisecauses pages 1-4, shi2023acutenoisecauses pages 13-19).

---

## 3. Phenotypes
### 3.1 Core hearing phenotypes (human)

#### DFNA13 (COL11A2; AD nonsyndromic)
- **Onset:** congenital (mcguirt1999mutationsincol11a2 pages 1-2).
- **Progression:** reported as **non-progressive** (mcguirt1999mutationsincol11a2 pages 1-2, mcguirt1999mutationsincol11a2 pages 5-6).
- **Audiogram:** predominantly **mid-frequency** loss with a characteristic **“cookie-bite”** profile (mcguirt1999mutationsincol11a2 pages 1-2).
- **Severity:** mild to moderately severe in a reported family (mcguirt1999mutationsincol11a2 pages 1-2).
- **Extra-auditory features:** absent in the described nonsyndromic families.
  - Direct quote: “Specifically, no midface hypoplasia, cleft palate, precocious arthritis, or stature or ocular abnormalities were noted.” (mcguirt1999mutationsincol11a2 pages 1-2).

**Suggested HPO terms (core hearing):**
- Sensorineural hearing impairment (HP:0000407)
- Mid-frequency hearing loss (HP:0040117) *(if curated as audiogram phenotype)*
- Congenital onset (HP:0003577)
- Non-progressive (HP:0003680)

#### DFNB53 (COL11A2; AR nonsyndromic)
- **Onset:** **prelingual** (chen2005mutationofcol11a2 pages 2-5).
- **Severity:** **profound** sensorineural hearing loss (chen2005mutationofcol11a2 pages 2-5).
- **Progression:** described as **non-progressive** (chen2005mutationofcol11a2 pages 2-5).
- **Vestibular:** normal on clinical assessment (chen2005mutationofcol11a2 pages 2-5).
- **Extra-auditory:** in the reported family, no ocular/midface/palatal abnormalities or skeletal dysplasia, supporting a nonsyndromic diagnosis (chen2005mutationofcol11a2 pages 2-5).

**Suggested HPO terms:**
- Sensorineural hearing impairment (HP:0000407)
- Profound hearing impairment (HP:0000405)
- Prelingual onset (HP:0003623)

#### COL11A2-related non-ocular Stickler syndrome (Stickler type 3)
A Japanese family report and a Stickler-focused review indicate that COL11A2-related Stickler phenotypes are frequently associated with hearing loss:
- **Frequency in non-ocular Stickler (as stated in the family report):** “94.1% of non-ocular Stickler syndrome patients have hearing loss.” (iwasa2015nonocularsticklersyndrome pages 3-4).
- **Course:** in the reported family, **childhood-onset, slowly progressive, mild-to-moderate hearing loss** with good speech discrimination and benefit from hearing aids (iwasa2015nonocularsticklersyndrome pages 3-4).
- **Review-level audiogram pattern (Stickler type 2/3):** mild–moderate low/mid-frequency loss and moderate–severe high-frequency loss; U-shaped patterns reported in some cases (acke2022hearinglossin pages 4-6).

**Suggested HPO terms (Stickler-related):**
- Sensorineural hearing impairment (HP:0000407)
- Progressive hearing impairment (HP:0001730)
- Midface hypoplasia (HP:0000347)

### 3.2 Quality of life impact
Specific validated QoL instrument data (e.g., SF-36, EQ-5D, PROMIS) were not present in the retrieved evidence. However, because Stickler syndrome involves multisystem features (including vision impairment in many types), a 2012 systematic review emphasized the importance of auditory follow-up.
- Direct quote from abstract: “Hearing impairment in patients with Stickler syndrome is common. … Regular auditory follow-up is strongly advised, particularly because many Stickler patients are visually impaired.” (Acke et al., 2012; DOI: https://doi.org/10.1186/1750-1172-7-84; Oct 2012) (acke2012hearingimpairmentin pages 10-10).

---

## 4. Genetic / molecular information
### 4.1 Causal gene
- **COL11A2** (collagen type XI alpha 2 chain) (mcguirt1999mutationsincol11a2 pages 1-2, chen2005mutationofcol11a2 pages 2-5).

### 4.2 Pathogenic variants and genotype–phenotype correlation (evidence-based)
- **AD DFNA13** can be caused by heterozygous missense variants and presents as isolated nonsyndromic hearing loss with cookie-bite audiograms (mcguirt1999mutationsincol11a2 pages 1-2, mcguirt1999mutationsincol11a2 pages 4-5).
- **AR DFNB53** in one consanguineous family was caused by a homozygous missense variant **p.Pro621Thr** and caused profound prelingual nonsyndromic SNHL without skeletal/ocular findings (chen2005mutationofcol11a2 pages 2-5).
- In a **COL11A2-related non-ocular Stickler** family, massively parallel sequencing enabled detection of a novel variant, supporting broad use of NGS-based testing in heterogeneous hereditary hearing loss (iwasa2015nonocularsticklersyndrome pages 3-4).

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No COL11A2-specific modifier-gene or epigenetic-disease mechanisms were described in the retrieved evidence.

---

## 5. Environmental information
### 5.1 Noise exposure as an ECM perturbagen (relevant to hearing loss biology)
While not evidence for causation in COL11A2 Mendelian disease, a recent cochlear proteomics study provides mechanistic context for ECM vulnerability:
- In an acute impulse-noise guinea pig model, **COL11A2** (along with other ECM proteins) was among hearing-related proteins that changed after noise exposure (shi2023acutenoisecauses pages 1-4, shi2023acutenoisecauses pages 13-19).
- **ABR threshold shift (example statistic):** click threshold increased from **26.88 ± 8.08 dB** (pre) to **57.00 ± 6.78 dB** (day 1), with partial recovery by day 7 (shi2023acutenoisecauses pages 13-19).
- The authors conclude: “Impulse noise can affect the expression of differential proteins through focal adhesion pathways.” (shi2023acutenoisecauses pages 1-4).

**Implication:** ECM/focal-adhesion signaling changes provide a plausible intersection between ECM structural genes (e.g., COL11A2) and acquired cochlear injury pathways, though direct gene–environment interaction data in humans were not retrieved (shi2023acutenoisecauses pages 10-13, shi2023acutenoisecauses pages 1-4).

---

## 6. Mechanism / pathophysiology
### 6.1 Mechanistic concept: “cochlear conductive” / ECM-biomechanical hearing loss
A COL11A2-related non-ocular Stickler report emphasizes that COL11A2 is expressed in the **tectorial membrane**, and frames the impairment as potentially due to altered sound transmission within the cochlea (“cochlear conductive hearing loss”) rather than primary hair cell expression (iwasa2015nonocularsticklersyndrome pages 4-5).

### 6.2 Tectorial membrane (TM) mechanics and COL11A2
A key mechanistic study demonstrated that Col11a2 deletion changes TM collagen architecture and collapses mechanical anisotropy:
- **Functional impact:** DPOAE and ABR were reduced by approximately **30–50 dB** across frequencies (masaki2009col11a2deletionreveals pages 1-2).
- **Mechanical impact:** radial shear impedance decreased by **5.5 ± 0.8 dB** and longitudinal shear impedance by **3.3 ± 0.3 dB**; the radial-to-longitudinal impedance ratio fell from **1.8 ± 0.7** (WT) to **1.0 ± 0.1** (Col11a2−/−) (Masaki et al., 2009; DOI: https://doi.org/10.1016/j.bpj.2009.02.056; Jun 2009) (masaki2009col11a2deletionreveals pages 1-2, masaki2009col11a2deletionreveals media 7efb6948).

**Causal chain (evidence-backed):**
COL11A2 pathogenic variant or loss → abnormal type XI collagen contribution to TM radial collagen fibrils → altered TM anisotropy/coupling and cochlear micromechanics → elevated auditory thresholds and characteristic audiometric patterns (especially mid-frequency deficits in DFNA13) (masaki2009col11a2deletionreveals pages 1-2, mcguirt1999mutationsincol11a2 pages 1-2).

### 6.3 Developmental expression and implicated cochlear cell types
In situ hybridization in developing mouse cochlea localized **Col11a1/Col11a2 mRNA** primarily to epithelial ridge and lateral wall structures that contribute to TM and cochlear ECM:
- Greater epithelial ridge as main source contributing to TM; later localization includes **inner sulcus, Claudius’ cells, and Boettcher’s cells** (Shpargel et al., 2004; DOI: https://doi.org/10.1080/00016480410016162; Mar 2004) (shpargel2004col11a1andcol11a2 pages 1-3, shpargel2004col11a1andcol11a2 pages 3-4).
- No hybridization detected in hair cells (shpargel2004col11a1andcol11a2 pages 3-4).

**Suggested ontology mappings:**
- **GO Biological Process:** extracellular matrix organization (GO:0030198); collagen fibril organization (GO:0030199)
- **GO Cellular Component:** tectorial membrane (GO:0060089) *(if used in a curated set)*; extracellular matrix (GO:0031012)
- **Uberon anatomical structures:** cochlea (UBERON:0001767); tectorial membrane (UBERON:0004953)
- **Cell Ontology (examples aligned to cited structures):** epithelial cell (CL:0000066) for ridge/sulcus epithelia; fibroblast (CL:0000057) relevant to spiral ligament ECM production *(note: the retrieved expression study names specific cochlear epithelial regions but does not provide CL identifiers)* (shpargel2004col11a1andcol11a2 pages 3-4).

---

## 7. Anatomical structures affected
**Primary:** inner ear/cochlea, especially ECM structures controlling micromechanics: the **tectorial membrane** (masaki2009col11a2deletionreveals pages 1-2).

**UBERON suggestions:** cochlea (UBERON:0001767); organ of Corti (UBERON:0001890); tectorial membrane (UBERON:0004953).

---

## 8. Temporal development (natural history)
### DFNA13
Congenital onset and non-progressive course were reported in DFNA13 families (mcguirt1999mutationsincol11a2 pages 1-2).

### DFNB53
Prelingual onset and non-progressive course were described in DFNB53 family L622 (chen2005mutationofcol11a2 pages 2-5).

### COL11A2-related non-ocular Stickler syndrome
In one family: childhood-onset and slowly progressive hearing loss (iwasa2015nonocularsticklersyndrome pages 3-4). In Stickler type 2/3 review synthesis, onset is “early” and losses may be missed by newborn screening if mild (acke2022hearinglossin pages 4-6).

---

## 9. Inheritance and population
### 9.1 Inheritance patterns
- DFNA13: autosomal dominant (mcguirt1999mutationsincol11a2 pages 1-2).
- DFNB53: autosomal recessive (chen2005mutationofcol11a2 pages 2-5).

### 9.2 Population genetics / epidemiology
No prevalence/incidence estimates specific to COL11A2-related hearing loss were available in the retrieved evidence. However, a Stickler systematic review quantified hearing loss across Stickler syndrome case literature:
- Direct quote from abstract: “**Hearing loss was found in 62.9%** [of Stickler syndrome patients], mostly mild to moderate when reported.” (Acke et al., 2012; DOI: https://doi.org/10.1186/1750-1172-7-84; Oct 2012) (acke2012hearingimpairmentin pages 10-10).

---

## 10. Diagnostics
### 10.1 Clinical tests
- **Pure-tone audiometry** used to confirm and characterize hearing loss in DFNB53 and Stickler/non-ocular Stickler (chen2005mutationofcol11a2 pages 2-5, iwasa2015nonocularsticklersyndrome pages 3-4).
- **Speech discrimination testing** and observed benefit from amplification were reported in COL11A2-related non-ocular Stickler (iwasa2015nonocularsticklersyndrome pages 3-4).

### 10.2 Genetic testing
- **Massively parallel sequencing (NGS)** enabled diagnosis of non-ocular Stickler syndrome in a Japanese hearing-loss cohort/family and facilitated correct clinical classification (e.g., distinguishing from other craniofacial conditions) (iwasa2015nonocularsticklersyndrome pages 3-4).

### 10.3 Differential diagnosis
The non-ocular Stickler report describes clinical confusion with **Binder syndrome** due to orofacial appearance, highlighting the role of genomic testing for correct syndromic diagnosis (iwasa2015nonocularsticklersyndrome pages 3-4).

---

## 11. Outcome / prognosis
Human survival/mortality endpoints are not relevant/available in the retrieved evidence; the primary morbidity is hearing impairment and (in syndromic forms) connective-tissue manifestations. Prognosis for hearing stability varies by entity: non-progressive DFNA13 and DFNB53 in cited families vs slowly progressive hearing loss in a non-ocular Stickler family report (mcguirt1999mutationsincol11a2 pages 1-2, chen2005mutationofcol11a2 pages 2-5, iwasa2015nonocularsticklersyndrome pages 3-4).

---

## 12. Treatment
### 12.1 Current applications and real-world implementations
**Hearing rehabilitation (amplification):**
- In an AD COL11A2-related non-ocular Stickler family, patients used **hearing aids** with favorable speech discrimination outcomes, and the authors recommended hearing aids as appropriate management (Iwasa et al., 2015; DOI: https://doi.org/10.1177/0003489415575044; Mar 2015) (iwasa2015nonocularsticklersyndrome pages 3-4).

**Cochlear implantation:** No cochlear implant outcome data were present in the retrieved evidence for COL11A2-specific hearing loss.

**MAXO suggestions:**
- Hearing aid therapy (MAXO:0000605) *(term suggestion; MAXO ID may require verification in a MAXO browser)*.

### 12.2 Emerging / experimental therapies
No COL11A2-specific interventional clinical trials were identified in the retrieved clinical-trials search during this run.

A 2023 cochlear single-cell atlas emphasizes translational motivation for gene-specific targeted therapies in hereditary deafness generally:
- Direct quote from abstract/significance: “One major challenge is the implementation of these therapies for diverse isolated and syndromic forms of hearing loss, taking into account the spatial and temporal patterns of expression of the causal gene…” (Jean et al., 2023; DOI: https://doi.org/10.1073/pnas.2221744120; Jun 2023) (jean2023singlecelltranscriptomicprofiling pages 6-7).

---

## 13. Prevention
No COL11A2-specific prevention trials or environmental prevention strategies were described in the retrieved evidence. For Mendelian disease, prevention is typically via genetic counseling and reproductive options; however, detailed guidance documents were not retrieved in this run.

---

## 14. Other species / natural disease
No naturally occurring veterinary COL11A2 hearing-loss syndromes were retrieved.

---

## 15. Model organisms
**Mouse models:**
- Col11a2 knockout/deletion models show auditory threshold elevations and TM collagen disorganization (mcguirt1999mutationsincol11a2 pages 5-6, masaki2009col11a2deletionreveals pages 1-2).
- Mechanistic TM study quantified loss of anisotropy and associated ABR/DPOAE reductions (masaki2009col11a2deletionreveals pages 1-2).

**Zebrafish (non-hearing phenotype in retrieved evidence):**
- A 2023 study used CRISPR zebrafish col11a2 loss-of-function for vertebral development; it supports broader COL11A2 roles in cartilage/ECM but does not provide hearing phenotypes in the excerpted evidence (shi2023acutenoisecauses pages 10-13).

---

## Key recent developments (prioritizing 2023–2024 sources)
1. **ECM proteomics in noise injury implicates COL11A2 among hearing-relevant ECM proteins** and provides quantitative ABR threshold shifts and pathway enrichment (focal adhesion/ECM receptor interaction) (Shi et al., 2023; Oct 2023; https://doi.org/10.1007/s12033-022-00557-2) (shi2023acutenoisecauses pages 1-4, shi2023acutenoisecauses pages 13-19).
2. **Single-cell/single-nucleus cochlear atlases for targeted therapies** provide frameworks to map expression patterns of hereditary deafness genes (not COL11A2-specific in the excerpt) (Jean et al., 2023; Jun 2023; https://doi.org/10.1073/pnas.2221744120) (jean2023singlecelltranscriptomicprofiling pages 6-7).

---

## Expert synthesis / interpretation (grounded in retrieved sources)
The most coherent mechanistic model supported by both human genetics and animal biophysics is that many COL11A2-related hearing phenotypes arise from **ECM structural defects in the tectorial membrane**, altering cochlear mechanics rather than primary hair-cell dysfunction. This aligns: (i) with developmental expression patterns that do not localize Col11a2 mRNA to hair cells (shpargel2004col11a1andcol11a2 pages 3-4), (ii) with TM mechanical anisotropy collapse and large threshold shifts in Col11a2−/− mice (masaki2009col11a2deletionreveals pages 1-2), and (iii) with the characteristic mid-frequency “cookie-bite” audiograms in DFNA13 families (mcguirt1999mutationsincol11a2 pages 1-2).

---

## Structured summary table
| Entity/label | Inheritance | Key COL11A2 variant examples (HGVS protein) | Core hearing phenotype | Extra-auditory features | Key mechanistic note (tectorial membrane/ECM) | Key citations (DOI; year) |
|---|---|---|---|---|---|---|
| DFNA13 (COL11A2-related nonsyndromic hearing loss) | Autosomal dominant | p.Arg549Cys; p.Gly323Glu | Congenital, non-progressive, predominantly mid-frequency sensorineural loss with characteristic “cookie-bite” audiogram; severity mild to moderately severe in reported family (mcguirt1999mutationsincol11a2 pages 1-2, mcguirt1999mutationsincol11a2 pages 5-6) | No syndromic findings reported in the cited families; specifically no midface hypoplasia, cleft palate, precocious arthritis, short stature, or ocular abnormalities (mcguirt1999mutationsincol11a2 pages 1-2) | COL11A2 encodes type XI collagen in cochlear ECM; loss/disorganization of tectorial-membrane collagen fibrils is implicated, and Col11a2-null mice show threshold elevation with tectorial-membrane abnormalities (mcguirt1999mutationsincol11a2 pages 1-2, mcguirt1999mutationsincol11a2 pages 5-6, masaki2009col11a2deletionreveals pages 1-2) | McGuirt et al., 10.1038/70516; 1999 (mcguirt1999mutationsincol11a2 pages 1-2, mcguirt1999mutationsincol11a2 pages 5-6); Masaki et al., 10.1016/j.bpj.2009.02.056; 2009 (masaki2009col11a2deletionreveals pages 1-2) |
| DFNB53 (COL11A2-related nonsyndromic hearing loss) | Autosomal recessive | p.Pro621Thr | Prelingual, profound, sensorineural, non-progressive hearing loss in the reported family (chen2005mutationofcol11a2 pages 2-5) | No ocular abnormalities; no midface hypoplasia or palatal clefting; normal stature; no bone dysplasia on survey; vestibular function normal (chen2005mutationofcol11a2 pages 2-5) | Missense change in the collagen triple-helical repeat of type XI collagen; supports a cochlear ECM structural mechanism, consistent with COL11A2-related tectorial-membrane dysfunction (chen2005mutationofcol11a2 pages 2-5, masaki2009col11a2deletionreveals pages 1-2) | Chen et al., 10.1136/jmg.2005.032615; 2005 (chen2005mutationofcol11a2 pages 2-5); Masaki et al., 10.1016/j.bpj.2009.02.056; 2009 (masaki2009col11a2deletionreveals pages 1-2) |
| COL11A2-related Stickler syndrome type 3 / non-ocular Stickler syndrome | Autosomal dominant | p.1312_1315del4 | Childhood-onset, slowly progressive, mild-to-moderate hearing loss; relatively good speech discrimination; in Stickler type 2/3 generally early-onset, often mild-moderate at low/mid frequencies and moderate-severe at high frequencies, sometimes U-shaped audiogram (iwasa2015nonocularsticklersyndrome pages 3-4, acke2022hearinglossin pages 4-6) | Orofacial features including maxillary/midfacial hypoplasia; non-ocular Stickler by definition lacks ocular involvement (iwasa2015nonocularsticklersyndrome pages 3-4) | COL11A2 is a type XI collagen chain expressed in the otic vesicle/tectorial membrane; pathogenic variants likely alter cochlear mechanics and can produce a “cochlear conductive”/ECM-mediated phenotype (iwasa2015nonocularsticklersyndrome pages 3-4, acke2022hearinglossin pages 4-6) | Iwasa et al., 10.1177/0003489415575044; 2015 (iwasa2015nonocularsticklersyndrome pages 3-4); Acke & De Leenheer, 10.3390/genes13091571; 2022 (acke2022hearinglossin pages 4-6) |
| OSMED (otospondylomegaepiphyseal dysplasia), COL11A2-related | Usually autosomal recessive; biallelic pathogenic variants classically implicated in cited evidence | No specific OSMED variant example available in the allowed evidence set | Hearing impairment is part of the COL11A2 disease spectrum, but detailed onset/progression/audiogram data for OSMED are not provided in the allowed evidence set (chen2005mutationofcol11a2 pages 2-5) | Skeletal dysplasia/bone involvement defines OSMED; Chen et al. cite OSMED as a COL11A2-associated extra-auditory phenotype distinct from DFNB53, but the allowed evidence set does not provide phenotype granularity (chen2005mutationofcol11a2 pages 2-5) | Likely reflects more widespread type XI collagen dysfunction in cartilage and cochlear ECM than isolated nonsyndromic deafness; mechanistic consistency with tectorial-membrane collagen disruption is supported by Col11a2 model data (chen2005mutationofcol11a2 pages 2-5, masaki2009col11a2deletionreveals pages 1-2) | Chen et al., 10.1136/jmg.2005.032615; 2005 (chen2005mutationofcol11a2 pages 2-5); Masaki et al., 10.1016/j.bpj.2009.02.056; 2009 (masaki2009col11a2deletionreveals pages 1-2) |


*Table: This table summarizes the main COL11A2-associated hearing loss entities across nonsyndromic and syndromic presentations, highlighting inheritance, representative variants, phenotype patterns, extra-auditory findings, and cochlear ECM/tectorial membrane mechanisms. It is useful as a compact genotype-phenotype reference for knowledge-base curation.*

---

## Supporting figure (tectorial membrane anisotropy)
A cropped panel from Masaki et al. (2009) illustrates the shear impedance changes underlying the loss of TM anisotropy in Col11a2−/− mice (masaki2009col11a2deletionreveals media 7efb6948).

---

## Limitations of this report (evidence gaps in this run)
- MONDO/Orphanet/OMIM/ICD/MeSH identifiers were not retrieved via available tools in this run.
- Epidemiology (population prevalence/incidence), penetrance/expressivity estimates, carrier frequency (gnomAD), and comprehensive COL11A2 variant catalogs (ClinVar) were not available in the retrieved evidence set.
- Clinical management beyond hearing aids (e.g., cochlear implant outcomes) and formal QoL statistics were not retrieved.


References

1. (mcguirt1999mutationsincol11a2 pages 1-2): Wyman T. McGuirt, Sai D. Prasad, Andrew J. Griffith, Henricus P.M. Kunst, Glenn E. Green, Karl B. Shpargel, Christina Runge, Christy Huybrechts, Robert F. Mueller, Eric Lynch, Mary-Claire King, Han G. Brunner, Cor W.R.J. Cremers, Masamine Takanosu, Shi-Wu Li, Machiko Arita, Richard Mayne, Darwin J. Prockop, Guy Van Camp, and Richard J.H. Smith. Mutations in col11a2 cause non-syndromic hearing loss (dfna13). Nature Genetics, 23:413-419, Dec 1999. URL: https://doi.org/10.1038/70516, doi:10.1038/70516. This article has 347 citations and is from a highest quality peer-reviewed journal.

2. (chen2005mutationofcol11a2 pages 2-5): Wenjie Chen, K. Kahrizi, N. Meyer, Y. Riazalhosseini, Guy, Van Camp, H. Najmabadi, and R. J. Smith. Mutation of col11a2 causes autosomal recessive non-syndromic hearing loss at the dfnb53 locus. Journal of Medical Genetics, 42:e61-e61, Oct 2005. URL: https://doi.org/10.1136/jmg.2005.032615, doi:10.1136/jmg.2005.032615. This article has 106 citations and is from a domain leading peer-reviewed journal.

3. (iwasa2015nonocularsticklersyndrome pages 3-4): Yoh-ichiro Iwasa, Hideaki Moteki, Mitsuru Hattori, Ririko Sato, Shin-ya Nishio, Yutaka Takumi, and Shin-ichi Usami. Non-ocular stickler syndrome with a novel mutation in col11a2 diagnosed by massively parallel sequencing in japanese hearing loss patients. Annals of Otology, Rhinology & Laryngology, 124:111S-117S, Mar 2015. URL: https://doi.org/10.1177/0003489415575044, doi:10.1177/0003489415575044. This article has 10 citations.

4. (acke2022hearinglossin pages 4-6): Frederic R. E. Acke and Els M. R. De Leenheer. Hearing loss in stickler syndrome: an update. Genes, 13:1571, Sep 2022. URL: https://doi.org/10.3390/genes13091571, doi:10.3390/genes13091571. This article has 28 citations.

5. (masaki2009col11a2deletionreveals pages 1-2): Kinuko Masaki, Kinuko Masaki, J. Gu, J. Gu, R. Ghaffari, R. Ghaffari, Gary Chan, Richard J. H. Smith, D. M. Freeman, D. M. Freeman, and A. Aranyosi. Col11a2 deletion reveals the molecular basis for tectorial membrane mechanical anisotropy. Biophysical Journal, 96:4717-4724, Jun 2009. URL: https://doi.org/10.1016/j.bpj.2009.02.056, doi:10.1016/j.bpj.2009.02.056. This article has 35 citations and is from a domain leading peer-reviewed journal.

6. (sellon2019thetectorialmembrane pages 1-3): Jonathan B. Sellon, Roozbeh Ghaffari, and Dennis M. Freeman. The tectorial membrane: mechanical properties and functions. Cold Spring Harbor perspectives in medicine, 9:a033514, Oct 2019. URL: https://doi.org/10.1101/cshperspect.a033514, doi:10.1101/cshperspect.a033514. This article has 34 citations and is from a peer-reviewed journal.

7. (mcguirt1999mutationsincol11a2 pages 5-6): Wyman T. McGuirt, Sai D. Prasad, Andrew J. Griffith, Henricus P.M. Kunst, Glenn E. Green, Karl B. Shpargel, Christina Runge, Christy Huybrechts, Robert F. Mueller, Eric Lynch, Mary-Claire King, Han G. Brunner, Cor W.R.J. Cremers, Masamine Takanosu, Shi-Wu Li, Machiko Arita, Richard Mayne, Darwin J. Prockop, Guy Van Camp, and Richard J.H. Smith. Mutations in col11a2 cause non-syndromic hearing loss (dfna13). Nature Genetics, 23:413-419, Dec 1999. URL: https://doi.org/10.1038/70516, doi:10.1038/70516. This article has 347 citations and is from a highest quality peer-reviewed journal.

8. (acke2012hearingimpairmentin pages 10-10): Frederic R E Acke, Ingeborg J M Dhooge, Fransiska Malfait, and Els M R De Leenheer. Hearing impairment in stickler syndrome: a systematic review. Orphanet Journal of Rare Diseases, 7:84-84, Oct 2012. URL: https://doi.org/10.1186/1750-1172-7-84, doi:10.1186/1750-1172-7-84. This article has 127 citations and is from a peer-reviewed journal.

9. (mcguirt1999mutationsincol11a2 pages 4-5): Wyman T. McGuirt, Sai D. Prasad, Andrew J. Griffith, Henricus P.M. Kunst, Glenn E. Green, Karl B. Shpargel, Christina Runge, Christy Huybrechts, Robert F. Mueller, Eric Lynch, Mary-Claire King, Han G. Brunner, Cor W.R.J. Cremers, Masamine Takanosu, Shi-Wu Li, Machiko Arita, Richard Mayne, Darwin J. Prockop, Guy Van Camp, and Richard J.H. Smith. Mutations in col11a2 cause non-syndromic hearing loss (dfna13). Nature Genetics, 23:413-419, Dec 1999. URL: https://doi.org/10.1038/70516, doi:10.1038/70516. This article has 347 citations and is from a highest quality peer-reviewed journal.

10. (shi2023acutenoisecauses pages 1-4): Min Shi, Lei Cao, Daxiong Ding, Lei Shi, Yiyong Hu, Guowei Qi, Li Zhan, Yuhua Zhu, Wenxing Yu, Ping Lv, and Ning Yu. Acute noise causes down-regulation of ecm protein expression in guinea pig cochlea. Molecular Biotechnology, 65:774-785, Oct 2023. URL: https://doi.org/10.1007/s12033-022-00557-2, doi:10.1007/s12033-022-00557-2. This article has 5 citations and is from a peer-reviewed journal.

11. (shi2023acutenoisecauses pages 13-19): Min Shi, Lei Cao, Daxiong Ding, Lei Shi, Yiyong Hu, Guowei Qi, Li Zhan, Yuhua Zhu, Wenxing Yu, Ping Lv, and Ning Yu. Acute noise causes down-regulation of ecm protein expression in guinea pig cochlea. Molecular Biotechnology, 65:774-785, Oct 2023. URL: https://doi.org/10.1007/s12033-022-00557-2, doi:10.1007/s12033-022-00557-2. This article has 5 citations and is from a peer-reviewed journal.

12. (shi2023acutenoisecauses pages 10-13): Min Shi, Lei Cao, Daxiong Ding, Lei Shi, Yiyong Hu, Guowei Qi, Li Zhan, Yuhua Zhu, Wenxing Yu, Ping Lv, and Ning Yu. Acute noise causes down-regulation of ecm protein expression in guinea pig cochlea. Molecular Biotechnology, 65:774-785, Oct 2023. URL: https://doi.org/10.1007/s12033-022-00557-2, doi:10.1007/s12033-022-00557-2. This article has 5 citations and is from a peer-reviewed journal.

13. (iwasa2015nonocularsticklersyndrome pages 4-5): Yoh-ichiro Iwasa, Hideaki Moteki, Mitsuru Hattori, Ririko Sato, Shin-ya Nishio, Yutaka Takumi, and Shin-ichi Usami. Non-ocular stickler syndrome with a novel mutation in col11a2 diagnosed by massively parallel sequencing in japanese hearing loss patients. Annals of Otology, Rhinology & Laryngology, 124:111S-117S, Mar 2015. URL: https://doi.org/10.1177/0003489415575044, doi:10.1177/0003489415575044. This article has 10 citations.

14. (masaki2009col11a2deletionreveals media 7efb6948): Kinuko Masaki, Kinuko Masaki, J. Gu, J. Gu, R. Ghaffari, R. Ghaffari, Gary Chan, Richard J. H. Smith, D. M. Freeman, D. M. Freeman, and A. Aranyosi. Col11a2 deletion reveals the molecular basis for tectorial membrane mechanical anisotropy. Biophysical Journal, 96:4717-4724, Jun 2009. URL: https://doi.org/10.1016/j.bpj.2009.02.056, doi:10.1016/j.bpj.2009.02.056. This article has 35 citations and is from a domain leading peer-reviewed journal.

15. (shpargel2004col11a1andcol11a2 pages 1-3): Karl B. Shpargel, Tomoko Makishima, and Andrew J. Griffith. Col11a1 and col11a2 mrna expression in the developing mouse cochlea: implications for the correlation of hearing loss phenotype with mutant type xi collagen genotype. Acta Oto-Laryngologica, 124:242-248, Mar 2004. URL: https://doi.org/10.1080/00016480410016162, doi:10.1080/00016480410016162. This article has 46 citations and is from a peer-reviewed journal.

16. (shpargel2004col11a1andcol11a2 pages 3-4): Karl B. Shpargel, Tomoko Makishima, and Andrew J. Griffith. Col11a1 and col11a2 mrna expression in the developing mouse cochlea: implications for the correlation of hearing loss phenotype with mutant type xi collagen genotype. Acta Oto-Laryngologica, 124:242-248, Mar 2004. URL: https://doi.org/10.1080/00016480410016162, doi:10.1080/00016480410016162. This article has 46 citations and is from a peer-reviewed journal.

17. (jean2023singlecelltranscriptomicprofiling pages 6-7): Philippe Jean, Fabienne Wong Jun Tai, Amrit Singh-Estivalet, Andrea Lelli, Cyril Scandola, Sébastien Megharba, Sandrine Schmutz, Solène Roux, Sabrina Mechaussier, Muriel Sudres, Enguerran Mouly, Anne-Valérie Heritier, Crystel Bonnet, Adeline Mallet, Sophie Novault, Valentina Libri, Christine Petit, and Nicolas Michalski. Single-cell transcriptomic profiling of the mouse cochlea: an atlas for targeted therapies. Proceedings of the National Academy of Sciences of the United States of America, Jun 2023. URL: https://doi.org/10.1073/pnas.2221744120, doi:10.1073/pnas.2221744120. This article has 65 citations and is from a highest quality peer-reviewed journal.