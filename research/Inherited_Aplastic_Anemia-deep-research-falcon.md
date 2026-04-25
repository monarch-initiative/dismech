---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-22T22:08:06.639518'
end_time: '2026-04-22T22:24:43.409008'
duration_seconds: 996.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inherited Aplastic Anemia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inherited Aplastic Anemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Inherited Aplastic Anemia** covering all of the
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
- **Disease Name:** Inherited Aplastic Anemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Inherited Aplastic Anemia** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Inherited Aplastic Anemia (Inherited Bone Marrow Failure Syndromes presenting as aplastic anemia)

### Scope note
“Inherited aplastic anemia” is not a single monogenic disease but a clinical presentation (hypocellular marrow with cytopenias/pancytopenia) caused by multiple **inherited bone marrow failure syndromes (IBMFS)**. Therefore, this report treats inherited aplastic anemia as an **umbrella phenotype** across IBMFS and telomere biology disorders, emphasizing diagnostic differentiation from immune/acquired aplastic anemia. (gutierrezrodrigues2023whentoconsider pages 1-2, gutierrezrodrigues2023whentoconsider pages 4-6)

---

## 1. Disease Information

### 1.1 Concise overview
Inherited aplastic anemia refers to bone marrow failure due to **germline (inherited or de novo) variants** in genes essential for hematopoietic stem/progenitor cell (HSPC) maintenance. IBMFS are described as “heterogenous” germline disorders characterized by **bone marrow failure**, often **syndrome-specific organ involvement**, and usually **predisposition to malignancy**. (gutierrezrodrigues2023whentoconsider pages 1-2)

### 1.2 Key identifiers and controlled vocabulary
**Ontology / classification items retrievable in-tool:**
- **ICD-11 (WHO) context:** Fanconi anemia appears in the **ICD-11 Foundation** with entity URI `http://id.who.int/icd/entity/1500851497` and is placed under the broader MMS linearization label **“congenital aplastic anemia (3A70.0)”** in one example mapping. (chute2018therenderingof pages 2-4)
- **MeSH-style identifiers (example from ClinicalTrials.gov record used for terminology mapping):**
  - D000741: *Anemia, Aplastic*
  - D000080983: *Bone Marrow Failure Disorders*
  (NCT07102849 chunk 2)

**Identifiers not fully retrievable with current evidence:** MONDO IDs for the umbrella phenotype, Orphanet (ORPHA) codes, and OMIM series entries for all subtypes were not captured by the retrieved texts in this run. This is a limitation of the current tool retrieval set (see “Evidence gaps”). (chute2018therenderingof pages 2-4, NCT07102849 chunk 2)

### 1.3 Synonyms and alternative names
- Inherited bone marrow failure syndromes (IBMFS) (gutierrezrodrigues2023whentoconsider pages 1-2)
- Congenital marrow failure / congenital aplastic anemia (ICD-11 context) (chute2018therenderingof pages 2-4)
- Telomere biology disorders (TBD) / dyskeratosis congenita spectrum (niewisch2023clinicalmanifestationsof pages 1-1)

### 1.4 Evidence source type
Most disease-level information here is derived from **aggregated disease resources/reviews/consensus-type articles** and registry/cohort analyses (e.g., ASH Education Program review, EBMT registry analysis). (gutierrezrodrigues2023whentoconsider pages 1-2, pagliuca2023currentuseof pages 5-9)

---

## 2. Etiology

### 2.1 Disease causal factors (primary)
Inherited aplastic anemia arises from pathogenic germline variants across several mechanistic classes:
1. **DNA damage response/repair defects** (canonical example: Fanconi anemia) (kawashima2023themolecularand pages 1-2, kawashima2023themolecularand pages 2-4)
2. **Telomere maintenance defects** (telomere biology disorders / dyskeratosis congenita spectrum) (niewisch2023clinicalmanifestationsof pages 1-1, niewisch2019anupdateon pages 19-24)
3. **Ribosome biogenesis/structure defects** (e.g., Diamond–Blackfan anemia) (kawashima2023themolecularand pages 1-2, rakotopare2023p53inthe pages 11-12)
4. **Other germline predisposition syndromes with marrow failure** (e.g., GATA2 deficiency; SAMD9/SAMD9L-related conditions) (gutierrezrodrigues2023whentoconsider pages 4-6, rudelius2023theinternationalconsensus pages 7-9)

### 2.2 Risk factors
**Genetic risk factors (examples; non-exhaustive):**
- TBD genes found commonly in adult telomere-length screening cohorts include **TERC, TERT, RTEL1, CTC1, NHP2, DKC1, USB1**. In one prospective adult study, the most frequent pathogenic/likely pathogenic (P/LP) variants were in **TERC (9)** and **TERT (4)**, with additional P/LP findings in **RTEL1** and **NHP2**. (tometten2023identificationofadult pages 4-6)
- In “acquired” aplastic anemia populations, germline variants (including in TERT/TERC) may confer predisposition; a 2024 review summarizes that **~5%–30% of young AA patients** may carry IBMFS-associated germline variants. (wang2024germlinevariantsin pages 1-2)

**Environmental/triggering factors:**
For the inherited syndromes, environmental factors are generally not primary “causes,” but **exogenous stresses** (e.g., genotoxic stress) can interact with underlying defects to exacerbate HSPC loss, and infection/inflammation can be important triggers for progression in predisposition states. (rakotopare2023p53inthe pages 11-12, kawashima2023themolecularand pages 2-4)

### 2.3 Protective factors
No specific protective germline or environmental factors were identified in the retrieved evidence. This is an evidence gap for this run.

### 2.4 Gene–environment interactions
The retrieved evidence supports a framework in which **external stresses** and **inflammatory stimuli** interact with underlying germline defects to influence marrow failure severity and clonal evolution (e.g., via p53 activation and cytokine-mediated suppression), but the reportable details are largely mechanistic rather than quantitative GxE effect sizes. (kawashima2023themolecularand pages 2-4, rakotopare2023p53inthe pages 11-12)

---

## 3. Phenotypes

### 3.1 Core phenotype (hematologic)
- Cytopenias that can be mono-, bi-, or trilineage, often with **hypocellular marrow** in many IBMFS presentations. (kawashima2023themolecularand pages 1-2, gutierrezrodrigues2023whentoconsider pages 4-6)
- In adults, distinguishing inherited from immune marrow failure may be challenging when presentation is atypical or cryptic. (gutierrezrodrigues2023whentoconsider pages 1-2)

**Suggested HPO terms (examples; not exhaustive):**
- Pancytopenia (HP:0001876)
- Aplastic anemia (HP:0001915)
- Bone marrow hypocellularity (HP:0005528)
- Macrocytosis (HP:0002151) (noted as a predictor/feature in inherited contexts) (gutierrezrodrigues2023whentoconsider pages 2-3)

### 3.2 Syndromic/extra-hematologic phenotypes that raise suspicion
From adult diagnostic guidance, syndrome clues include:
- **Fanconi anemia:** limb and renal abnormalities (gutierrezrodrigues2023whentoconsider pages 1-2)
- **Telomere biology disorders:** pulmonary and liver disease; adults may present with isolated pulmonary/liver/hematologic disease and may lack classic mucocutaneous findings (niewisch2023clinicalmanifestationsof pages 1-1, gutierrezrodrigues2023whentoconsider pages 1-2)
- **GATA2 deficiency:** recurrent atypical infections (gutierrezrodrigues2023whentoconsider pages 1-2)
- **Shwachman–Diamond syndrome:** pancreatic insufficiency (noted as targeted testing trigger) (gutierrezrodrigues2023whentoconsider pages 2-3)

**Suggested HPO terms (examples):**
- Pulmonary fibrosis (HP:0002206)
- Hepatic fibrosis/cirrhosis (HP:0001395)
- Recurrent infections (HP:0002719)
- Exocrine pancreatic insufficiency (HP:0001738)

### 3.3 Natural history and progression (selected quantitative data)
- **Fanconi anemia (FA):** reported bone marrow failure cumulative incidence **18–83%** (risk-group dependent); AML cumulative incidence **15–20% by age 40**; MDS cumulative incidence **40% by age 50**; markedly elevated relative risks versus general population; high-risk FA subgroup **FANCD1/BRCA2** shows AML cumulative incidence **80% by age 10**. (rudelius2023theinternationalconsensus pages 7-9)
- **Shwachman–Diamond syndrome (SDS):** registry data suggest ~**1% per year** progression with cumulative MDS/AML risk **~36% by age 30**; another summary notes ~**20%** clonal/myeloid evolution by age 18. (rudelius2023theinternationalconsensus pages 7-9)
- **Severe congenital neutropenia (SCN):** median MDS/AML incidence **~21% at 15 years** after starting G-CSF. (rudelius2023theinternationalconsensus pages 7-9)
- **Dyskeratosis congenita / TBD:** NCI cohort (n=197) cited cumulative leukemia incidence **2% by age 50** and solid cancer **11% by age 50**. (rudelius2023theinternationalconsensus pages 7-9)
- **SAMD9/SAMD9L:** germline mutations noted in up to **~18%** of non-FA suspected inherited marrow failure cases, often linked to monosomy 7 and MDS/AML progression. (rudelius2023theinternationalconsensus pages 7-9)

### 3.4 Quality of life impact
No disease-specific QoL instruments or quantitative QoL outcomes were present in the retrieved evidence. This is an evidence gap for this run.

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and inheritance patterns (high-level)
Inherited marrow failure can be autosomal recessive, autosomal dominant, X-linked, or de novo; autosomal dominant conditions often exhibit variable penetrance and later onset, complicating family-history-based screening. (gutierrezrodrigues2023whentoconsider pages 2-3)

**Key gene groups and representative genes (examples drawn from retrieved evidence):**
- Telomerase/shelterin/telomere replication: **TERC, TERT, RTEL1, CTC1, NHP2, DKC1, USB1** (tometten2023identificationofadult pages 4-6)
- DNA repair/FA pathway: multiple FANC genes; also BRCA2/FANCD1 high-risk subgroup (rudelius2023theinternationalconsensus pages 7-9)
- SAMD9/SAMD9L (gain-of-function; monosomy 7-associated “rescue” events) (rudelius2023theinternationalconsensus pages 7-9)
- GATA2 (immunodeficiency/infection-associated marrow failure spectrum) (gutierrezrodrigues2023whentoconsider pages 1-2)

### 4.2 Pathogenic variants and variant interpretation
- A practical adult workflow emphasizes combining **functional assays plus germline genetic testing**, and careful interpretation of variant allele frequency (VAF) in blood because **somatic genetic rescue** and clonal hematopoiesis can confound germline inference. Cultured skin fibroblasts are preferred germline tissue controls; buccal swabs are not recommended. (gutierrezrodrigues2023whentoconsider pages 6-7)
- In one adult TL-screening protocol, germline-calling cutoffs included **VAF >30%** (with absolute read thresholds) and ACMG-based variant classification. (tometten2023identificationofadult pages 2-3)

### 4.3 Modifier genes / epigenetics
Not specifically retrievable in the current evidence set.

---

## 5. Environmental Information
This category is generally secondary for inherited etiologies. The retrieved evidence emphasizes that **cellular stresses** (oxidative stress, UPR, mitochondrial dysfunction) and **inflammatory milieu** can modulate outcomes and clonal progression in IBMFS. (kawashima2023themolecularand pages 2-4, kawashima2023themolecularand pages 4-6)

---

## 6. Mechanism / Pathophysiology

### 6.1 Unifying causal chain (current understanding)
A convergent model across IBMFS:
1. **Primary germline defect** (DNA repair, ribosome biogenesis, telomere maintenance)
2. → **Cellular stress** (DNA damage, telomere attrition, ribosomal stress, oxidative stress)
3. → **TP53 (p53) activation** with growth arrest/senescence and apoptosis in HSC/HSPC compartments
4. → **Cytopenias and marrow failure**, with inflammatory cytokines further suppressing hematopoiesis
5. → **Clonal selection/evolution** under stress and inflammation, increasing risk of MDS/AML and other cancers

This is explicitly proposed as an overarching hypothesis for IBMFS with p53-dependent growth arrest/apoptosis of hematopoietic stem/progenitor/precursor cells. (kawashima2023themolecularand pages 1-2)

### 6.2 Inflammation and cytokines
A 2023 mechanistic review proposes a pathogenic role for pro-inflammatory cytokines in cytopenias and clonal evolution, explicitly naming **TGF-β, IL-1β, and IFN-α** as mediators and noting broader inflammatory signatures including **IL-6, IL-8, IP-10/CXCL10, IFN-γ, TNF-α**, among others, within SASP-like responses. (kawashima2023themolecularand pages 1-2, kawashima2023themolecularand pages 2-4)

### 6.3 p53 circuitry and cross-syndrome overlap
p53 activation can repress additional telomere- and DNA repair–related genes via promoter binding and DREAM complex-mediated repression, potentially creating positive feedback loops that blur phenotypes across distinct IBMFS categories. (rakotopare2023p53inthe pages 1-2)

### 6.4 Suggested ontology terms (mechanisms)
**GO Biological Process (examples):**
- DNA damage response (GO:0006974)
- Regulation of cell cycle arrest (GO:0071156)
- Apoptotic process (GO:0006915)
- Cellular senescence (GO:0090398)
- Inflammatory response (GO:0006954)

**Cell Ontology (CL) terms (examples):**
- Hematopoietic stem cell (CL:0000037)
- Hematopoietic progenitor cell (CL:0008001)
- T cell (CL:0000084) (immune injury context when distinguishing acquired AA vs inherited; see diagnostics) (gutierrezrodrigues2023whentoconsider pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Primary site
- **Bone marrow hematopoietic compartment** (UBERON:0002371; conceptual mapping) with primary injury/exhaustion in **HSC/HSPC** populations. (kawashima2023themolecularand pages 1-2, rakotopare2023p53inthe pages 11-12)

### 7.2 Multi-organ involvement (not uniform; syndrome-dependent)
- Telomere biology disorders: lung and liver involvement common and may dominate adult phenotypes (niewisch2023clinicalmanifestationsof pages 1-1)

---

## 8. Temporal Development
- Onset can be **neonatal/infancy** (e.g., DBA/SCN), **childhood** (e.g., FA/DC), or **adult** (cryptic TBD, adult-onset IBMFS) depending on genetic architecture and penetrance. (kawashima2023themolecularand pages 1-2, niewisch2023clinicalmanifestationsof pages 1-1)
- Adult-onset TBD/IBMFS can be “cryptic” with limited organ involvement; incomplete penetrance, variable expressivity, and anticipation complicate recognition. (niewisch2023clinicalmanifestationsof pages 1-1)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (selected, from retrieved evidence)
A 2023 mechanistic review tabulated estimated incidence per 1,000,000 births/year:
- Fanconi anemia **11.4**
- Dyskeratosis congenita/telomere disorders **3.8**
- Diamond–Blackfan anemia **10.4**
- Shwachman–Diamond syndrome **8.5**
- Severe congenital neutropenia **4.7**
(kawashima2023themolecularand pages 1-2)

### 9.2 Inheritance patterns
IBMFS can be autosomal recessive, autosomal dominant, X-linked, or de novo; AR tends to earlier onset with higher penetrance, AD tends to later onset with variable penetrance. (gutierrezrodrigues2023whentoconsider pages 2-3)

### 9.3 How often “acquired” AA hides inherited causes
- In an adult-focused ASH Education review, most BMF is classified as immune (>90%), but a CIBMTR retrospective series found **~7%** of presumed immune severe aplastic anemia had an undiagnosed IBMFS (about one-third adults). (gutierrezrodrigues2023whentoconsider pages 1-2)
- For adult telomere screening: in the AA/PNH referral category, **P/LP TBD variants were found in 3/38 (7.9%)** NGS-screened individuals (selected after TL filtering). (tometten2023identificationofadult pages 3-4)
- A 2024 TBD review states: **“approximately 10% of adult patients with clinical BMF”** may have a congenital TBD origin, highlighting counseling and donor-selection implications. (rolles2024inheritedtelomerebiology pages 1-2)

---

## 10. Diagnostics

### 10.1 Diagnostic principles
A widely endorsed approach is **functional (disease-specific) assays plus germline genetic testing** for all new bone marrow failure patients, including adults, because immune aplastic anemia is a diagnosis of exclusion and inherited disorders may be cryptic. (gutierrezrodrigues2023whentoconsider pages 1-2, gutierrezrodrigues2023whentoconsider pages 6-7)

### 10.2 Specialized assays (high-yield)
Key functional tests and interpretation notes are summarized in the table below.

| Category | Item | Summary | Key thresholds / quantitative findings |
|---|---|---|---|
| Definition | Inherited aplastic anemia / IBMFS | Umbrella term for heterogeneous germline disorders characterized by bone marrow failure/cytopenias, syndrome-specific extrahematopoietic features, and usually elevated malignancy risk; distinction from immune marrow failure is essential because treatment response, transplant planning, and family counseling differ (gutierrezrodrigues2023whentoconsider pages 1-2) | In adults, all new-onset BMF patients should be assessed for inherited causes using clinical history, specialized assays, and germline testing (gutierrezrodrigues2023whentoconsider pages 6-7) |
| Diagnostic assay | Chromosome breakage test (DEB/MMC) | Functional assay for Fanconi anemia; increased chromosome fragility supports FA among inherited marrow failure syndromes (gutierrezrodrigues2023whentoconsider pages 4-6, wang2024germlinevariantsin pages 2-4) | False negatives can occur with somatic reversion or recent chemotherapy; if suspicion remains high, test non-hematopoietic tissue such as cultured fibroblasts (gutierrezrodrigues2023whentoconsider pages 4-6) |
| Diagnostic assay | Flow-FISH telomere length | Functional in vivo screen for telomere biology disorders/dyskeratosis congenita in patients with aplastic anemia or suggestive phenotypes (gutierrezrodrigues2023whentoconsider pages 4-6, gutierrezrodrigues2023whentoconsider pages 2-3) | TL <1st percentile for age is highly sensitive/specific for TBD; 1st-10th percentile is suggestive; one prospective adult screening study found P/LP TBD variants in 17/76 (22.4%) shortened-TL cases undergoing NGS (gutierrezrodrigues2023whentoconsider pages 4-6, wang2024germlinevariantsin pages 2-4) |
| Diagnostic assay | Erythrocyte adenosine deaminase (eADA) | Elevated eADA supports Diamond-Blackfan anemia in the differential diagnosis of inherited marrow failure (gutierrezrodrigues2023whentoconsider pages 4-6, gutierrezrodrigues2023whentoconsider pages 2-3) | Used as targeted functional testing when DBA is suspected; interpret with phenotype/genetics rather than as a stand-alone diagnostic test (gutierrezrodrigues2023whentoconsider pages 4-6) |
| Diagnostic assay | PNH clone testing | Presence of GPI-negative/PNH clone favors immune/acquired aplastic anemia rather than IBMFS (gutierrezrodrigues2023whentoconsider pages 1-2, wang2024germlinevariantsin pages 2-4) | PNH clones are common in immune BMF and very rare in IBMFS; detection of PNH clone >1% is used as a clue against IBMFS in differential diagnosis (gutierrezrodrigues2023whentoconsider pages 3-4, wang2024germlinevariantsin pages 2-4) |
| Diagnostic assay | 6p CN-LOH / 6pLOH | Somatic loss of heterozygosity in the HLA region is an immune-escape marker supporting acquired/immune AA over inherited syndromes (gutierrezrodrigues2023whentoconsider pages 1-2, wang2024germlinevariantsin pages 2-4) | Reported to have almost 100% positive predictive value for acquired AA in one review summary; presence argues against IBMFS as primary diagnosis (wang2024germlinevariantsin pages 2-4) |
| Epidemiology / diagnostic yield | Presumed immune SAA later found to have IBMFS | Retrospective CIBMTR series identified occult inherited disease among patients initially classified as immune severe aplastic anemia (gutierrezrodrigues2023whentoconsider pages 1-2) | ~7% of presumed immune SAA had undiagnosed IBMFS; about one-third of these occult IBMFS cases were adults (gutierrezrodrigues2023whentoconsider pages 1-2) |
| Treatment outcomes | Androgens in inherited BMF (EBMT cohort) | Largest recent international retrospective cohort of inherited/acquired BMF treated with androgens; inherited cohort mainly Fanconi anemia and dyskeratosis congenita (pagliuca2023currentuseof pages 1-2, pagliuca2023currentuseof pages 4-5) | In inherited BMF at 3 months: CR 8%, PR 29%; 5-year OS 78%, FFS 14%, transplant-free survival 17%; 5-year cumulative incidence of clonal evolution (AML/MDS) 8% (pagliuca2023currentuseof pages 5-9, pagliuca2023currentuseof pages 1-2) |
| Treatment outcomes | Danazol in telomere disease | Prospective danazol trial in telomere disease showed both hematologic benefit and telomere elongation, supporting androgen use in selected inherited marrow failure patients (nassani2023theroleof pages 4-5, calado2023bonemarrowfailure pages 1-3) | Danazol 800 mg/day: hematologic response in 19/24 (79%) and telomere elongation in all 12/12 evaluable patients at 24 months (nassani2023theroleof pages 4-5) |
| Practical diagnostic note | Germline confirmation | Blood-based sequencing can be confounded by somatic rescue/clonal hematopoiesis; variant interpretation must consider VAF, phenotype, inheritance, and tissue source (gutierrezrodrigues2023whentoconsider pages 4-6, gutierrezrodrigues2023whentoconsider pages 6-7) | Germline VAF is often ~50% or ~100%, but variants with VAF >30% may still require confirmation in cultured skin fibroblasts or relatives; buccal swabs are not preferred (gutierrezrodrigues2023whentoconsider pages 4-6, gutierrezrodrigues2023whentoconsider pages 6-7) |


*Table: This table condenses the most actionable concepts for inherited aplastic anemia/inherited bone marrow failure syndromes: umbrella definition, specialized diagnostic assays, and key recent quantitative outcome data. It is useful as a quick-reference summary for knowledge-base curation and clinical differentiation from acquired/immune aplastic anemia.*

### 10.3 Visual evidence: diagnostic algorithm
A diagnostic algorithm for specialized work-up of confirmed bone marrow failure (including chromosome fragility testing and flow-FISH telomere length) is available as Figure 2 in Gutierrez-Rodrigues et al. (ASH Education Program 2023). (gutierrezrodrigues2023whentoconsider media 4ef49e0b)

### 10.4 Differentiating inherited from immune/acquired AA
Markers that support immune/acquired AA rather than IBMFS include:
- **PNH clones** (GPI-negative cells) (gutierrezrodrigues2023whentoconsider pages 1-2, wang2024germlinevariantsin pages 2-4)
- **6p CN-LOH/6pLOH** (HLA-region immune escape) reported with very high PPV for acquired AA in one review summary (wang2024germlinevariantsin pages 2-4)

---

## 11. Outcome/Prognosis
Prognosis is syndrome- and treatment-dependent, with major determinants including transplant candidacy, organ involvement (TBD), and clonal evolution risk.

**Selected quantitative outcomes (therapy-related):**
- In inherited BMF patients treated with androgens (EBMT cohort), 5-year overall survival **78%** but failure-free survival **14%**, reflecting limited durability of androgen monotherapy in many inherited cases; 5-year cumulative incidence of AML/MDS clonal evolution **8%**. (pagliuca2023currentuseof pages 5-9)

---

## 12. Treatment

### 12.1 Curative therapy: hematopoietic cell transplantation (HCT)
In adult telomere biology disorders, “The only curative option for TBD-related lung, bone marrow, or hepatic disease is organ transplant.” (niewisch2023clinicalmanifestationsof pages 8-9)

Clinical application: accurate inherited diagnosis is critical for:
- transplant timing,
- reduced-intensity conditioning selection in susceptible syndromes,
- and **related-donor selection** to avoid donor carriers (explicitly emphasized for congenital TBD origin in adult BMF). (rolles2024inheritedtelomerebiology pages 1-2)

### 12.2 Androgens (real-world implementation)
**EBMT/European registry evidence (inherited BMF subgroup):**
- Early responses at 3 months: complete remission **8%**, partial remission **29%**. (pagliuca2023currentuseof pages 1-2)
- 5-year outcomes: OS **78%**, failure-free survival **14%**, transplant-free survival **17%**. (pagliuca2023currentuseof pages 5-9)

**Telomere disease (danazol prospective trial summary as cited in androgen review):**
- Danazol 800 mg/day: hematologic response **19/24 (79%) at 3 months**; “All evaluable 12 patients had a gain in telomere length at 24 months as compared with baseline.” (nassani2023theroleof pages 4-5)

**Expert synthesis:** an androgen-focused editorial notes that androgens can be considered in inherited cases as a bridge to transplant or when transplant is not possible, but toxicities can be substantial and careful selection is required. (calado2023bonemarrowfailure pages 1-3)

### 12.3 Emerging/experimental therapies
Clinical translation emphasis in the retrieved evidence includes gene therapy/editing broadly for inherited hematologic disease, but inherited aplastic anemia–specific gene therapy trial evidence was not retrieved as primary outcomes in this run (evidence gap). (No tool-retrieved primary trial outcome papers specific to IBMFS gene therapy were available in the current evidence set.)

### 12.4 Clinical trials and real-world research infrastructure
An example of an active observational programmatic study in marrow failure is:
- **NCT07102849** “Molecular and Clinical Analysis of Bone Marrow Failure: A Secondary Research Study” (NIH NHLBI), including MeSH-style controlled vocabulary entries (e.g., D000741 Anemia, Aplastic; D000080983 Bone Marrow Failure Disorders). (NCT07102849 chunk 2)

---

## 13. Prevention
Primary prevention of inherited aplastic anemia is not generally feasible because etiology is germline; prevention focuses on:
- **genetic counseling**, cascade testing in families,
- avoidance of ineffective or harmful therapies (e.g., misapplied immunosuppression in IBMFS),
- surveillance for malignancies and organ complications in specific syndromes.

The importance of recognition in adults is highlighted by the estimate that ~10% of adult clinical BMF may have a congenital TBD origin, affecting counseling and donor selection. (rolles2024inheritedtelomerebiology pages 1-2)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human disease analogs were retrieved in this run.

---

## 15. Model Organisms
The retrieved evidence provides limited, indirect model-organism detail:
- Mouse models with constitutively increased p53 activity have been reported to exhibit features of dyskeratosis congenita in the p53/BMFS mechanistic literature, supporting a p53-mediated causal chain, but explicit model descriptions and identifiers were not retrieved here. (rakotopare2023p53inthe pages 1-2)

---

## Recent developments (2023–2024 highlights prioritized)
1. **Adult IBMFS diagnostic emphasis:** ASH Education Program 2023 advocates routine consideration of inherited etiologies in adults and a combined functional + genetic approach, including interpretation pitfalls from somatic rescue and tissue selection for germline confirmation. (gutierrezrodrigues2023whentoconsider pages 1-2, gutierrezrodrigues2023whentoconsider pages 6-7)
2. **Quantitative androgen real-world outcomes:** EBMT registry analysis (2023) provides large-cohort response and survival estimates for inherited BMF treated with androgens, enabling benchmarking. (pagliuca2023currentuseof pages 5-9, pagliuca2023currentuseof pages 1-2)
3. **Adult telomere screening yields:** prospective flow-FISH TL screening with age-modified criteria demonstrates actionable yield of P/LP variants in telomere genes (TERC/TERT dominant), and clarifies referral thresholds and gene distributions. (tometten2023identificationofadult pages 1-2, tometten2023identificationofadult pages 4-6)
4. **Mechanistic consolidation around p53 + inflammatory cytokines:** 2023 mechanistic reviews synthesize gene-category convergence on TP53 and cytokine/SASP-mediated marrow suppression and leukemogenesis. (kawashima2023themolecularand pages 1-2, kawashima2023themolecularand pages 2-4)

---

## Evidence gaps and limitations of this tool run
- Comprehensive mapping to **OMIM IDs, Orphanet ORPHA codes, and MONDO IDs** for each specific inherited aplastic anemia entity was not fully retrievable from the obtained texts. (chute2018therenderingof pages 2-4)
- Variant-level details such as **ClinVar accessions, gnomAD allele frequencies, and specific recurrent pathogenic variants** were not available in the retrieved evidence.
- Detailed QoL metrics, comprehensive HPO frequency tables, and robust model organism resources were not retrieved.

---

## Key primary/authoritative sources cited (with publication dates and URLs where available)
- Gutierrez-Rodrigues F, Patel BA, Groarke EM. *When to consider inherited marrow failure syndromes in adults.* Hematology ASH Education Program. **Dec 2023**. https://doi.org/10.1182/hematology.2023000488 (gutierrezrodrigues2023whentoconsider pages 1-2, gutierrezrodrigues2023whentoconsider pages 4-6, gutierrezrodrigues2023whentoconsider pages 6-7)
- Wang P et al. *Germline variants in acquired aplastic anemia: current knowledge and future perspectives.* Haematologica. **Jul 2024**. https://doi.org/10.3324/haematol.2023.284312 (wang2024germlinevariantsin pages 1-2, wang2024germlinevariantsin pages 2-4)
- Pagliuca S et al. *Current use of androgens in bone marrow failure disorders (EBMT).* Haematologica. **May 2023**. https://doi.org/10.3324/haematol.2023.282935 (pagliuca2023currentuseof pages 5-9, pagliuca2023currentuseof pages 1-2)
- Tometten M et al. *Identification of adult patients with classical DC or cryptic TBD by TL screening.* HemaSphere. **Apr 2023**. https://doi.org/10.1097/hs9.0000000000000874 (tometten2023identificationofadult pages 1-2, tometten2023identificationofadult pages 3-4)
- Rolles B et al. *Inherited Telomere Biology Disorders: Pathophysiology, Clinical Presentation, Diagnostics, and Treatment.* Transfus Med Hemother. **Jul 2024**. https://doi.org/10.1159/000540109 (rolles2024inheritedtelomerebiology pages 1-2)
- Rudelius M et al. *ICC of hematologic neoplasms with germline predisposition…* Virchows Arch. **Nov 2023**. https://doi.org/10.1007/s00428-022-03447-9 (rudelius2023theinternationalconsensus pages 7-9)
- Kawashima N et al. *IBMFS mechanisms: role of inflammatory cytokines.* Biomolecules. **Aug 2023**. https://doi.org/10.3390/biom13081249 (kawashima2023themolecularand pages 2-4, kawashima2023themolecularand pages 1-2)
- Rakotopare J, Toledo F. *p53 in the molecular circuitry of BMFS.* Int J Mol Sci. **Oct 2023**. https://doi.org/10.3390/ijms241914940 (rakotopare2023p53inthe pages 1-2)
- Chute CG. *Rare diseases in ICD-11 (Fanconi anemia mapping example).* J Inherit Metab Dis. **Mar 2018**. https://doi.org/10.1007/s10545-018-0172-5 (chute2018therenderingof pages 2-4)


References

1. (gutierrezrodrigues2023whentoconsider pages 1-2): Fernanda Gutierrez-Rodrigues, Bhavisha A. Patel, and Emma M. Groarke. When to consider inherited marrow failure syndromes in adults. Hematology. American Society of Hematology. Education Program, 2023 1:548-555, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000488, doi:10.1182/hematology.2023000488. This article has 12 citations.

2. (gutierrezrodrigues2023whentoconsider pages 4-6): Fernanda Gutierrez-Rodrigues, Bhavisha A. Patel, and Emma M. Groarke. When to consider inherited marrow failure syndromes in adults. Hematology. American Society of Hematology. Education Program, 2023 1:548-555, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000488, doi:10.1182/hematology.2023000488. This article has 12 citations.

3. (chute2018therenderingof pages 2-4): Christopher G. Chute. The rendering of human phenotype and rare diseases in icd-11. Journal of Inherited Metabolic Disease, 41:563-569, Mar 2018. URL: https://doi.org/10.1007/s10545-018-0172-5, doi:10.1007/s10545-018-0172-5. This article has 23 citations and is from a peer-reviewed journal.

4. (NCT07102849 chunk 2):  Molecular and Clinical Analysis of Bone Marrow Failure: A Secondary Research Study. National Heart, Lung, and Blood Institute (NHLBI). 2025. ClinicalTrials.gov Identifier: NCT07102849

5. (niewisch2023clinicalmanifestationsof pages 1-1): Marena R. Niewisch, Fabian Beier, and Sharon A. Savage. Clinical manifestations of telomere biology disorders in adults. Hematology. American Society of Hematology. Education Program, 2023 1:563-572, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000490, doi:10.1182/hematology.2023000490. This article has 38 citations.

6. (pagliuca2023currentuseof pages 5-9): Simona Pagliuca, Austin G. Kulasekararaj, Dirk-Jan Eikema, Brian Piepenbroek, Raheel Iftikhar, Tariq Mahmood Satti, Morag Griffin, Marica Laurino, Alphan Kupesiz, Yves Bertrand, Bruno Fattizzo, Ibrahim Yakoub-Agha, Mahmoud Aljurf, Paola Corti, Erika Massaccesi, Bruno Lioure, Marisa Calabuig, Matthias Klammer, Emel Unal, Depei Wu, Patrice Chevallier, Edouard Forcade, John A. Snowden, Hakan Ozdogu, Antonio Risitano, and Régis Peffault De Latour. Current use of androgens in bone marrow failure disorders: a report from the severe aplastic anemia working party of the european society for blood and marrow transplantation. Haematologica, 109:765-776, May 2023. URL: https://doi.org/10.3324/haematol.2023.282935, doi:10.3324/haematol.2023.282935. This article has 18 citations.

7. (kawashima2023themolecularand pages 1-2): Nozomu Kawashima, Valentino Bezzerri, and Seth J. Corey. The molecular and genetic mechanisms of inherited bone marrow failure syndromes: the role of inflammatory cytokines in their pathogenesis. Biomolecules, 13:1249, Aug 2023. URL: https://doi.org/10.3390/biom13081249, doi:10.3390/biom13081249. This article has 13 citations.

8. (kawashima2023themolecularand pages 2-4): Nozomu Kawashima, Valentino Bezzerri, and Seth J. Corey. The molecular and genetic mechanisms of inherited bone marrow failure syndromes: the role of inflammatory cytokines in their pathogenesis. Biomolecules, 13:1249, Aug 2023. URL: https://doi.org/10.3390/biom13081249, doi:10.3390/biom13081249. This article has 13 citations.

9. (niewisch2019anupdateon pages 19-24): Marena R. Niewisch and Sharon A. Savage. An update on the biology and management of dyskeratosis congenita and related telomere biology disorders. Expert Review of Hematology, 12:1037-1052, Dec 2019. URL: https://doi.org/10.1080/17474086.2019.1662720, doi:10.1080/17474086.2019.1662720. This article has 205 citations and is from a peer-reviewed journal.

10. (rakotopare2023p53inthe pages 11-12): Jeanne Rakotopare and Franck Toledo. P53 in the molecular circuitry of bone marrow failure syndromes. International Journal of Molecular Sciences, 24:14940, Oct 2023. URL: https://doi.org/10.3390/ijms241914940, doi:10.3390/ijms241914940. This article has 8 citations.

11. (rudelius2023theinternationalconsensus pages 7-9): Martina Rudelius, Olga K. Weinberg, Charlotte M. Niemeyer, Akiko Shimamura, and Katherine R. Calvo. The international consensus classification (icc) of hematologic neoplasms with germline predisposition, pediatric myelodysplastic syndrome, and juvenile myelomonocytic leukemia. Virchows Archiv, 482:113-130, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03447-9, doi:10.1007/s00428-022-03447-9. This article has 79 citations and is from a peer-reviewed journal.

12. (tometten2023identificationofadult pages 4-6): Mareike Tometten, Martin Kirschner, Robert Meyer, Matthias Begemann, Insa Halfmeyer, Margherita Vieri, Kim Kricheldorf, Angela Maurer, Uwe Platzbecker, Markus Radsak, Philippe Schafhausen, Selim Corbacioglu, Britta Höchsmann, C. Matthias Wilk, Claas Hinze, Jörg Chromik, Michael Heuser, Michael Kreuter, Steffen Koschmieder, Jens Peter Panse, Susanne Isfort, Ingo Kurth, Tim Henrik Brümmendorf, and Fabian Beier. Identification of adult patients with classical dyskeratosis congenita or cryptic telomere biology disorder by telomere length screening using age-modified criteria. HemaSphere, Apr 2023. URL: https://doi.org/10.1097/hs9.0000000000000874, doi:10.1097/hs9.0000000000000874. This article has 23 citations and is from a peer-reviewed journal.

13. (wang2024germlinevariantsin pages 1-2): Peicheng Wang, Wanzhi Jiang, Tianyi Lai, Qi Liu, Yingying Shen, Baodong Ye, and Dijiong Wu. Germline variants in acquired aplastic anemia: current knowledge and future perspectives. Haematologica, 109:2778-2789, Jul 2024. URL: https://doi.org/10.3324/haematol.2023.284312, doi:10.3324/haematol.2023.284312. This article has 16 citations.

14. (gutierrezrodrigues2023whentoconsider pages 2-3): Fernanda Gutierrez-Rodrigues, Bhavisha A. Patel, and Emma M. Groarke. When to consider inherited marrow failure syndromes in adults. Hematology. American Society of Hematology. Education Program, 2023 1:548-555, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000488, doi:10.1182/hematology.2023000488. This article has 12 citations.

15. (gutierrezrodrigues2023whentoconsider pages 6-7): Fernanda Gutierrez-Rodrigues, Bhavisha A. Patel, and Emma M. Groarke. When to consider inherited marrow failure syndromes in adults. Hematology. American Society of Hematology. Education Program, 2023 1:548-555, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000488, doi:10.1182/hematology.2023000488. This article has 12 citations.

16. (tometten2023identificationofadult pages 2-3): Mareike Tometten, Martin Kirschner, Robert Meyer, Matthias Begemann, Insa Halfmeyer, Margherita Vieri, Kim Kricheldorf, Angela Maurer, Uwe Platzbecker, Markus Radsak, Philippe Schafhausen, Selim Corbacioglu, Britta Höchsmann, C. Matthias Wilk, Claas Hinze, Jörg Chromik, Michael Heuser, Michael Kreuter, Steffen Koschmieder, Jens Peter Panse, Susanne Isfort, Ingo Kurth, Tim Henrik Brümmendorf, and Fabian Beier. Identification of adult patients with classical dyskeratosis congenita or cryptic telomere biology disorder by telomere length screening using age-modified criteria. HemaSphere, Apr 2023. URL: https://doi.org/10.1097/hs9.0000000000000874, doi:10.1097/hs9.0000000000000874. This article has 23 citations and is from a peer-reviewed journal.

17. (kawashima2023themolecularand pages 4-6): Nozomu Kawashima, Valentino Bezzerri, and Seth J. Corey. The molecular and genetic mechanisms of inherited bone marrow failure syndromes: the role of inflammatory cytokines in their pathogenesis. Biomolecules, 13:1249, Aug 2023. URL: https://doi.org/10.3390/biom13081249, doi:10.3390/biom13081249. This article has 13 citations.

18. (rakotopare2023p53inthe pages 1-2): Jeanne Rakotopare and Franck Toledo. P53 in the molecular circuitry of bone marrow failure syndromes. International Journal of Molecular Sciences, 24:14940, Oct 2023. URL: https://doi.org/10.3390/ijms241914940, doi:10.3390/ijms241914940. This article has 8 citations.

19. (tometten2023identificationofadult pages 3-4): Mareike Tometten, Martin Kirschner, Robert Meyer, Matthias Begemann, Insa Halfmeyer, Margherita Vieri, Kim Kricheldorf, Angela Maurer, Uwe Platzbecker, Markus Radsak, Philippe Schafhausen, Selim Corbacioglu, Britta Höchsmann, C. Matthias Wilk, Claas Hinze, Jörg Chromik, Michael Heuser, Michael Kreuter, Steffen Koschmieder, Jens Peter Panse, Susanne Isfort, Ingo Kurth, Tim Henrik Brümmendorf, and Fabian Beier. Identification of adult patients with classical dyskeratosis congenita or cryptic telomere biology disorder by telomere length screening using age-modified criteria. HemaSphere, Apr 2023. URL: https://doi.org/10.1097/hs9.0000000000000874, doi:10.1097/hs9.0000000000000874. This article has 23 citations and is from a peer-reviewed journal.

20. (rolles2024inheritedtelomerebiology pages 1-2): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 20 citations and is from a peer-reviewed journal.

21. (wang2024germlinevariantsin pages 2-4): Peicheng Wang, Wanzhi Jiang, Tianyi Lai, Qi Liu, Yingying Shen, Baodong Ye, and Dijiong Wu. Germline variants in acquired aplastic anemia: current knowledge and future perspectives. Haematologica, 109:2778-2789, Jul 2024. URL: https://doi.org/10.3324/haematol.2023.284312, doi:10.3324/haematol.2023.284312. This article has 16 citations.

22. (gutierrezrodrigues2023whentoconsider pages 3-4): Fernanda Gutierrez-Rodrigues, Bhavisha A. Patel, and Emma M. Groarke. When to consider inherited marrow failure syndromes in adults. Hematology. American Society of Hematology. Education Program, 2023 1:548-555, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000488, doi:10.1182/hematology.2023000488. This article has 12 citations.

23. (pagliuca2023currentuseof pages 1-2): Simona Pagliuca, Austin G. Kulasekararaj, Dirk-Jan Eikema, Brian Piepenbroek, Raheel Iftikhar, Tariq Mahmood Satti, Morag Griffin, Marica Laurino, Alphan Kupesiz, Yves Bertrand, Bruno Fattizzo, Ibrahim Yakoub-Agha, Mahmoud Aljurf, Paola Corti, Erika Massaccesi, Bruno Lioure, Marisa Calabuig, Matthias Klammer, Emel Unal, Depei Wu, Patrice Chevallier, Edouard Forcade, John A. Snowden, Hakan Ozdogu, Antonio Risitano, and Régis Peffault De Latour. Current use of androgens in bone marrow failure disorders: a report from the severe aplastic anemia working party of the european society for blood and marrow transplantation. Haematologica, 109:765-776, May 2023. URL: https://doi.org/10.3324/haematol.2023.282935, doi:10.3324/haematol.2023.282935. This article has 18 citations.

24. (pagliuca2023currentuseof pages 4-5): Simona Pagliuca, Austin G. Kulasekararaj, Dirk-Jan Eikema, Brian Piepenbroek, Raheel Iftikhar, Tariq Mahmood Satti, Morag Griffin, Marica Laurino, Alphan Kupesiz, Yves Bertrand, Bruno Fattizzo, Ibrahim Yakoub-Agha, Mahmoud Aljurf, Paola Corti, Erika Massaccesi, Bruno Lioure, Marisa Calabuig, Matthias Klammer, Emel Unal, Depei Wu, Patrice Chevallier, Edouard Forcade, John A. Snowden, Hakan Ozdogu, Antonio Risitano, and Régis Peffault De Latour. Current use of androgens in bone marrow failure disorders: a report from the severe aplastic anemia working party of the european society for blood and marrow transplantation. Haematologica, 109:765-776, May 2023. URL: https://doi.org/10.3324/haematol.2023.282935, doi:10.3324/haematol.2023.282935. This article has 18 citations.

25. (nassani2023theroleof pages 4-5): Momen Nassani, Riad El Fakih, Jakob Passweg, Simone Cesaro, Hazzaa Alzahrani, Ali Alahmari, Carmem Bonfim, Raheel Iftikhar, Amal Albeihany, Constantijn Halkes, Syed Osman Ahmed, Carlo Dufour, and Mahmoud Aljurf. The role of androgen therapy in acquired aplastic anemia and other bone marrow failure syndromes. Frontiers in Oncology, May 2023. URL: https://doi.org/10.3389/fonc.2023.1135160, doi:10.3389/fonc.2023.1135160. This article has 18 citations.

26. (calado2023bonemarrowfailure pages 1-3): Rodrigo T. Calado. Bone marrow failure on steroids: when to use androgens? Haematologica, 109:695-697, Aug 2023. URL: https://doi.org/10.3324/haematol.2023.283564, doi:10.3324/haematol.2023.283564. This article has 3 citations.

27. (gutierrezrodrigues2023whentoconsider media 4ef49e0b): Fernanda Gutierrez-Rodrigues, Bhavisha A. Patel, and Emma M. Groarke. When to consider inherited marrow failure syndromes in adults. Hematology. American Society of Hematology. Education Program, 2023 1:548-555, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000488, doi:10.1182/hematology.2023000488. This article has 12 citations.

28. (niewisch2023clinicalmanifestationsof pages 8-9): Marena R. Niewisch, Fabian Beier, and Sharon A. Savage. Clinical manifestations of telomere biology disorders in adults. Hematology. American Society of Hematology. Education Program, 2023 1:563-572, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000490, doi:10.1182/hematology.2023000490. This article has 38 citations.

29. (tometten2023identificationofadult pages 1-2): Mareike Tometten, Martin Kirschner, Robert Meyer, Matthias Begemann, Insa Halfmeyer, Margherita Vieri, Kim Kricheldorf, Angela Maurer, Uwe Platzbecker, Markus Radsak, Philippe Schafhausen, Selim Corbacioglu, Britta Höchsmann, C. Matthias Wilk, Claas Hinze, Jörg Chromik, Michael Heuser, Michael Kreuter, Steffen Koschmieder, Jens Peter Panse, Susanne Isfort, Ingo Kurth, Tim Henrik Brümmendorf, and Fabian Beier. Identification of adult patients with classical dyskeratosis congenita or cryptic telomere biology disorder by telomere length screening using age-modified criteria. HemaSphere, Apr 2023. URL: https://doi.org/10.1097/hs9.0000000000000874, doi:10.1097/hs9.0000000000000874. This article has 23 citations and is from a peer-reviewed journal.