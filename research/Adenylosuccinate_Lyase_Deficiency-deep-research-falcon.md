---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-03T00:00:55.090815'
end_time: '2026-05-03T00:09:50.380137'
duration_seconds: 535.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adenylosuccinate Lyase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adenylosuccinate Lyase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Adenylosuccinate Lyase Deficiency** covering all of the
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
- **Disease Name:** Adenylosuccinate Lyase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Adenylosuccinate Lyase Deficiency** covering all of the
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


# Adenylosuccinate Lyase Deficiency (ADSL deficiency / ASLD): Comprehensive Disease Characteristics Report

## Executive summary
Adenylosuccinate lyase deficiency (also called adenylosuccinase deficiency; ADSL deficiency; ASLD) is an ultra-rare, autosomal recessive inborn error of purine metabolism caused by biallelic pathogenic variants in **ADSL**, leading to reduced adenylosuccinate lyase activity in **de novo purine synthesis** and the **purine nucleotide cycle** and accumulation of the succinylpurine metabolites **SAICAr** and **succinyladenosine (S‑Ado)** in extracellular fluids. Clinical presentation is predominantly neurologic and includes developmental delay/intellectual disability, hypotonia, epilepsy (often intractable), microcephaly, and autistic features, with a spectrum from fatal neonatal encephalopathy to milder later-onset disease. (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, donti2016diagnosisofadenylosuccinate pages 1-2, cutillo2024electroclinicalfeaturesand pages 1-2)

## 1. Disease information
### 1.1 Definition and overview
A widely cited review defines the disorder as a purine metabolism defect with characteristic metabolite accumulation: **“Biochemically this defect manifests by the presence in the biologic fluids of two dephosphorylated substrates of ADSL enzyme: succinylaminoimidazole carboxamide riboside (SAICAr) and succinyladenosine (S-Ado).”** (Journal of Inherited Metabolic Disease, online 2014; print Aug 2015) (jurecka2015adenylosuccinatelyasedeficiency pages 1-3).

### 1.2 Key identifiers
| Identifier system | ID | Label | Notes/Source URL |
|---|---|---|---|
| MONDO | MONDO_0007068 | adenylosuccinate lyase deficiency | Disease-target association record identifies MONDO_0007068 as “adenylosuccinate lyase deficiency.” https://platform.opentargets.org/disease/MONDO_0007068 (jurecka2015adenylosuccinatelyasedeficiency pages 1-3) |
| OMIM | 103050 | Adenylosuccinate Lyase Deficiency | OMIM disease number explicitly cited in the literature and model-organism papers as “OMIM 103050” / “OMIM #103050.” https://omim.org/entry/103050 (donti2016diagnosisofadenylosuccinate pages 1-2, jurecka2015adenylosuccinatelyasedeficiency pages 1-3, moro2023adenylosuccinatelyasedeficiency pages 1-2) |
| MeSH (suggested) | Not confirmed in retrieved papers; clinical trial record uses disease label | Adenylosuccinate Lyase Deficiency | ClinicalTrials.gov record lists the condition/MeSH-linked term “Adenylosuccinate lyase deficiency.” Suggested MeSH label for indexing/search; verify exact MeSH UID in NLM MeSH Browser. https://clinicaltrials.gov/study/NCT03776656 (NCT03776656 chunk 2) |
| ClinicalTrials.gov condition label | NCT03776656 | Evaluation of a Treatment With Allopurinol in Adenylosuccinate Lyase Deficiency | Interventional phase II study naming the disease directly; useful practical identifier for recent clinical research. https://clinicaltrials.gov/study/NCT03776656 (NCT03776656 chunk 2, NCT03776656 chunk 1) |
| Synonym | — | ADSL deficiency | Common literature shorthand used throughout reviews and case reports. https://doi.org/10.1007/s10545-014-9755-y ; https://doi.org/10.1016/j.ymgmr.2016.07.007 (donti2016diagnosisofadenylosuccinate pages 1-2, jurecka2015adenylosuccinatelyasedeficiency pages 1-3) |
| Synonym | — | ASLD | Abbreviation used in 2023 mechanistic/model-organism literature for adenylosuccinate lyase deficiency. https://doi.org/10.1371/journal.pgen.1010974 ; https://doi.org/10.1016/j.ymgme.2023.107686 (moro2023adenylosuccinatelyasedeficiency pages 1-2, fenton2023acaenorhabditiselegans pages 1-3) |
| Synonym | — | Adenylosuccinase deficiency | Historical/alternate enzyme-based synonym seen in purine-metabolism literature and references discussing ASL deficiency. https://doi.org/10.1016/j.ymgme.2023.107686 (fenton2023acaenorhabditiselegans pages 15-16) |


*Table: This table summarizes the core disease identifiers and commonly used synonyms for adenylosuccinate lyase deficiency. It is useful for harmonizing nomenclature across OMIM, MONDO, clinical trial records, and literature sources.*

**Additional identifiers not confirmed in retrieved full-text**: Orphanet (ORPHA ID), ICD-10/ICD-11 codes, and MeSH Unique ID (UID) were not explicitly present in the retrieved literature text; these should be verified in Orphanet/ICD/MeSH browsers and then mapped to the knowledge base entry.

### 1.3 Common synonyms
- Adenylosuccinate lyase deficiency; ADSL deficiency (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, donti2016diagnosisofadenylosuccinate pages 1-2)
- ASLD (used in 2023 model-organism literature) (moro2023adenylosuccinatelyasedeficiency pages 1-2, fenton2023acaenorhabditiselegans pages 1-3)
- Adenylosuccinase deficiency (historical enzyme-based synonym) (fenton2023acaenorhabditiselegans pages 15-16)

### 1.4 Evidence source types
- Aggregated disease-level resources/reviews: JIMD 2015 review; Metabolites 2023 review (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, camici2023inbornerrorsof pages 9-11)
- Human clinical cohort/long-term follow-up: Epilepsia Open 2024 cohort + literature appraisal (cutillo2024electroclinicalfeaturesand pages 1-2, cutillo2024electroclinicalfeaturesand pages 2-4)
- Human diagnostic method papers: plasma metabolomics diagnosis paper (2016) (donti2016diagnosisofadenylosuccinate pages 1-2, donti2016diagnosisofadenylosuccinate pages 3-4)
- Interventional clinical research: allopurinol phase 2 trial registered at ClinicalTrials.gov (NCT03776656 chunk 1, NCT03776656 chunk 2)
- Model organism: C. elegans mechanistic disease models (2023) (moro2023adenylosuccinatelyasedeficiency pages 1-2, fenton2023acaenorhabditiselegans pages 1-3)

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause**: biallelic pathogenic variants in **ADSL** causing reduced adenylosuccinate lyase function and accumulation of succinylpurines. The disorder is described as “a rare autosomal recessive neurometabolic disorder” caused by loss of ADSL enzymatic activity (donti2016diagnosisofadenylosuccinate pages 1-2, jurecka2015adenylosuccinatelyasedeficiency pages 1-3).

**Molecular defect**: ADSL catalyzes two non-sequential steps in de novo purine synthesis; in a 2023 paper’s abstract, “Adenylosuccinate lyase is required for de novo purine biosynthesis, acting twice in the pathway at non-sequential steps.” (PLOS Genetics, Sep 2023) (moro2023adenylosuccinatelyasedeficiency pages 1-2).

### 2.2 Risk factors
- **Genetic**: autosomal recessive inheritance; consanguinity can increase risk (e.g., homozygous variants reported in consanguineous families) (donti2016diagnosisofadenylosuccinate pages 3-4).
- **Environmental**: no established environmental risk factors were identified in the retrieved evidence; disease is primarily Mendelian (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, camici2023inbornerrorsof pages 9-11).

### 2.3 Protective factors / gene–environment interactions
No validated protective alleles or gene–environment interactions were identified in the retrieved evidence. Supportive factors may include early diagnosis and optimized symptomatic management (e.g., seizure control), but these are not “protective factors” in a causal sense (cutillo2024electroclinicalfeaturesand pages 14-15).

## 3. Phenotypes
### 3.1 Core phenotype spectrum and subtypes
A foundational review describes three clinical groupings and gives hallmark neonatal and pediatric presentations, including: **“The fatal neonatal form has onset from birth… respiratory failure, and intractable seizures… early death within the first weeks of life.”** and later forms with severe neurodevelopmental features. (jurecka2015adenylosuccinatelyasedeficiency pages 1-3)

A 2024 long-term cohort + literature appraisal provides a quantitative view of the spectrum (n=88 total, including 7 new and 81 literature cases):
- **Type I**: 58% (51/88)
- **Type II**: 28% (25/88)
- **Neonatal**: 14% (12/88) (cutillo2024electroclinicalfeaturesand pages 1-2)

### 3.2 Epilepsy and electroclinical features (2024 update)
Epilepsy is common and often severe; the 2024 appraisal reports: **“Epilepsy is present in 81.8% of the patients, with polymorphic and often intractable seizures.”** (Epilepsia Open, Nov 2024) (cutillo2024electroclinicalfeaturesand pages 1-2).

The same paper summarizes typical EEG evolution: **“EEG features seem to display common patterns and developmental trajectories: (i) poor general back-ground organization with theta-delta activity; (ii) hypsarrhythmia with spasms, usually adrenocorticotropic hormone-responsive; (iii) generalized epileptic discharges with frontal or frontal temporal predominance; and (iv) epileptic discharge activation in sleep with an altered sleep structure.”** (cutillo2024electroclinicalfeaturesand pages 1-2).

### 3.3 Neurodevelopmental and neuromuscular phenotypes
A 2023 mechanistic/model-organism paper summarizes human features and emphasizes neuromuscular and neurobehavioral dysfunction; its abstract begins: **“Adenylosuccinate lyase deficiency is an ultrarare congenital metabolic disorder associated with muscle weakness and neurobehavioral dysfunction.”** (PLOS Genetics, Sep 2023) (moro2023adenylosuccinatelyasedeficiency pages 1-2).

Commonly described clinical features across reviews/cohorts include:
- Developmental delay/intellectual disability; severe psychomotor retardation (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, donti2016diagnosisofadenylosuccinate pages 1-2)
- Hypotonia; ataxia; dystonia (reported in clinical cohorts) (cutillo2024electroclinicalfeaturesand pages 2-4)
- Autistic features/contact disturbances (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, camici2023inbornerrorsof pages 9-11)
- Progressive cerebral/cerebellar atrophy and white matter changes on MRI in more severe phenotypes (cutillo2024electroclinicalfeaturesand pages 1-2, cutillo2024electroclinicalfeaturesand pages 2-4)

### 3.4 Suggested HPO terms (non-exhaustive; to be validated per case)
Based on phenotypes described in the cited literature (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, cutillo2024electroclinicalfeaturesand pages 1-2, cutillo2024electroclinicalfeaturesand pages 2-4):
- Seizures (HP:0001250)
- Epileptic spasms / Infantile spasms (HP:0012469)
- Hypsarrhythmia (HP:0012465)
- Global developmental delay (HP:0001263)
- Intellectual disability (HP:0001249)
- Hypotonia (HP:0001252)
- Microcephaly (HP:0000252)
- Autism (HP:0000717) / Autistic features
- Ataxia (HP:0001251)
- Dystonia (HP:0001332)
- Cerebral atrophy (HP:0002059)
- Cerebellar atrophy (HP:0001272)

### 3.5 Quality of life impact
No disease-specific QoL instruments were identified in the retrieved texts; however, long-term follow-up cases include severe disability (e.g., chronic refractory epilepsy, progressive neurodisability) implying major functional dependence (cutillo2024electroclinicalfeaturesand pages 2-4, cutillo2024electroclinicalfeaturesand pages 14-15).

## 4. Genetic / molecular information
### 4.1 Causal gene
- **Gene**: **ADSL** (adenylosuccinate lyase) (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, shi2025thediagnosisand pages 1-3)
- **Inheritance**: autosomal recessive (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, donti2016diagnosisofadenylosuccinate pages 1-2)

### 4.2 Variant spectrum and genotype–phenotype
The 2015 review notes: **“Over 50 ADSL mutations have been identified”** and the disorder is genetically heterogeneous (many private variants; frequent compound heterozygosity) (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, jurecka2015adenylosuccinatelyasedeficiency pages 4-6).

The 2024 appraisal reports the most frequently observed variants in compiled cases: **“p.R426H homozygous (19 patients), p.Y114H in compound heterozygo-sity (13 patients), and p.D430N homozygous (6 patients).”** (cutillo2024electroclinicalfeaturesand pages 1-2).

Genotype–phenotype relationships remain incomplete, but severity is suggested to track residual enzyme activity and certain variants are enriched in severe neonatal/type I phenotypes (cutillo2024electroclinicalfeaturesand pages 14-15).

### 4.3 Population data / carrier frequencies
From a 2016 diagnostic study referencing ExAC for ADSL p.Arg426His:
- p.Arg426His is reported as the most common ADSL variant in ExAC, present on 31 chromosomes heterozygously, with allelic frequency **0.000255** and estimated carrier frequency **~1/2000**; most carriers were non-Finnish European (28/31). (Molecular Genetics and Metabolism Reports, Sep 2016) (donti2016diagnosisofadenylosuccinate pages 3-4).

A 2015 review provided a broader, older estimate: an “estimated carrier (heterozygote) probability for a pathogenic ADSL allele of about **1:10,000**.” (jurecka2015adenylosuccinatelyasedeficiency pages 4-6). Differences likely reflect method/variant set and database updates; current carrier frequency should be re-estimated using contemporary gnomAD with careful pathogenicity filtering.

### 4.4 Functional consequences
Evidence across reviews and model-organism work supports a dual mechanism:
- **Toxic substrate accumulation** (SAICAR/SAICAr and related succinylpurines)
- **Reduced purine biosynthetic flux** and impaired purine homeostasis

The C. elegans neurobehavioral work explicitly argues that altered behavior likely arises from accumulated substrate toxicity rather than only purine shortage (moro2023adenylosuccinatelyasedeficiency pages 1-2, moro2023adenylosuccinatelyasedeficiency pages 9-11).

## 5. Environmental information
No specific toxins, lifestyle factors, or infectious triggers were identified in the retrieved evidence. The disorder is primarily genetic, and management focuses on symptomatic care and experimental metabolic interventions (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, camici2023inbornerrorsof pages 9-11).

## 6. Mechanism / pathophysiology
### 6.1 Pathway context
ADSL is required for **de novo purine biosynthesis** and acts twice at non-sequential steps (moro2023adenylosuccinatelyasedeficiency pages 1-2). A clinical review focused on epilepsy reiterates the enzymatic steps and toxic metabolite hypothesis in ADSL deficiency (shi2025thediagnosisand pages 1-3).

**Biochemical hallmark**: accumulation of **SAICAr** and **S‑Ado** in extracellular fluids (urine, CSF, plasma) (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, jurecka2015adenylosuccinatelyasedeficiency pages 8-9).

### 6.2 Proposed causal chain (integrated)
1) **Biallelic ADSL variants → reduced ADSL activity** (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, donti2016diagnosisofadenylosuccinate pages 1-2)
2) **Block at ADSL-catalyzed steps → accumulation of phosphorylated substrates → extracellular dephosphorylated succinylpurines (SAICAr, S‑Ado)** (jurecka2015adenylosuccinatelyasedeficiency pages 8-9, jurecka2015adenylosuccinatelyasedeficiency pages 1-3)
3) **Neurodevelopmental dysfunction** via a combination of toxic metabolite effects and purine imbalance; model-organism data show broader metabolic perturbations (e.g., neurotransmitter signaling disruption) downstream of purine pathway disruption (moro2023adenylosuccinatelyasedeficiency pages 1-2, moro2023adenylosuccinatelyasedeficiency pages 9-11)
4) **Clinical manifestations**: developmental delay/intellectual disability, hypotonia/ataxia, epilepsy with characteristic EEG patterns, and progressive neuroimaging abnormalities in severe phenotypes (cutillo2024electroclinicalfeaturesand pages 1-2, cutillo2024electroclinicalfeaturesand pages 2-4)

### 6.3 Mechanistic advances (2023–2024)
**Neurobehavioral mechanism in C. elegans (2023):** substrate accumulation due to adsl-1 deficiency perturbs tyrosine metabolism and tyramine signaling; behavioral phenotypes are rescued by tyramine supplementation and involve TYRA-2 receptor signaling (moro2023adenylosuccinatelyasedeficiency pages 1-2, moro2023adenylosuccinatelyasedeficiency pages 11-13, moro2023adenylosuccinatelyasedeficiency pages 9-11).

**Separability of phenotypic etiologies (2023):** a C. elegans model suggests neuromuscular defects associate with intermediate accumulation while reproductive defects are rescued by purine supplementation—supporting the concept that multiple downstream mechanisms contribute to phenotype heterogeneity (fenton2023acaenorhabditiselegans pages 1-3, fenton2023acaenorhabditiselegans pages 8-9).

### 6.4 Suggested ontology terms
**GO Biological Process (suggested):**
- de novo IMP biosynthetic process (purine biosynthesis)
- AMP biosynthetic process
- purine nucleotide metabolic process

**GO Molecular Function (suggested):**
- adenylosuccinate lyase activity

**Cell types (CL; suggested, based on neurologic phenotype/EEG patterns):**
- neurons (CL:0000540)
- astrocytes (CL:0000127)
- oligodendrocytes (CL:0000128)

**Anatomy (UBERON; suggested):**
- brain (UBERON:0000955)
- cerebellum (UBERON:0002037)
- cerebral cortex/frontal lobe (UBERON mapping; frontal predominance described on imaging) (cutillo2024electroclinicalfeaturesand pages 1-2)

## 7. Anatomical structures affected
Human cohorts and reviews emphasize CNS involvement with imaging showing cerebral/cerebellar atrophy and white matter abnormalities in many patients (cutillo2024electroclinicalfeaturesand pages 1-2, cutillo2024electroclinicalfeaturesand pages 2-4). Neuromuscular involvement (hypotonia, muscle weakness) is frequently noted (moro2023adenylosuccinatelyasedeficiency pages 1-2).

## 8. Temporal development
- **Onset** ranges from congenital/neonatal (fatal neonatal encephalopathy) to onset in the first years of life for type I and later onset in milder type II forms (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, cutillo2024electroclinicalfeaturesand pages 1-2).
- **Progression** varies: rapidly progressive neonatal/type I vs slower courses in type II; long-term follow-up documents persistent epilepsy and progressive neurodisability in some patients over decades (cutillo2024electroclinicalfeaturesand pages 2-4, cutillo2024electroclinicalfeaturesand pages 14-15).

## 9. Inheritance and population
- **Inheritance**: autosomal recessive (jurecka2015adenylosuccinatelyasedeficiency pages 1-3, donti2016diagnosisofadenylosuccinate pages 1-2)
- **Epidemiology**: incidence/prevalence remain uncertain; historical reviews noted “More than 80 individuals” identified by 2015 (jurecka2015adenylosuccinatelyasedeficiency pages 1-3), while the 2024 appraisal aggregated **88** patients (81 literature + 7 new) (cutillo2024electroclinicalfeaturesand pages 1-2).
- **Variant enrichment/founder effects**: p.Arg426His is repeatedly the most common variant in patient cohorts and appears enriched in Europeans; ExAC-based estimates are provided above (donti2016diagnosisofadenylosuccinate pages 3-4, jurecka2015adenylosuccinatelyasedeficiency pages 4-6).

## 10. Diagnostics
### 10.1 Biochemical testing (core real-world implementation)
The most established diagnostic hallmark is detecting elevated succinylpurines. The review states: **“Diagnosis is facilitated by demonstration of SAICAr and S-Ado in extracellular fluids such as plasma, cerebrospinal fluid…”** (jurecka2015adenylosuccinatelyasedeficiency pages 1-3).

Methods described include HPLC-UV/HPLC-MS and high-throughput HPLC-ESI-MS/MS approaches; urine is commonly used, with CSF and plasma also reported (jurecka2015adenylosuccinatelyasedeficiency pages 8-9).

### 10.2 Metabolomics-based diagnosis
A 2016 study demonstrated untargeted plasma metabolomics as an alternative route to diagnosis and phenotype expansion, describing ADSL deficiency as OMIM 103050 and emphasizing SAICAr/S‑Ado accumulation as the biochemical hallmark typically detected in urine (donti2016diagnosisofadenylosuccinate pages 1-2).

### 10.3 Genetic testing
Diagnostic confirmation includes genomic sequencing (single-gene testing, panels, WES/WGS) and sometimes functional enzyme assessment; WES is emphasized as valuable for atypical/mild phenotypes (macchiaiolo2017amildform pages 7-7, jurecka2015adenylosuccinatelyasedeficiency pages 8-9).

### 10.4 Differential diagnosis
Not comprehensively extracted from the retrieved texts. In practice, differential diagnosis includes other inborn errors of metabolism presenting with developmental epileptic encephalopathy; nucleotide metabolism epilepsy reviews discuss ADSL deficiency among other nucleic acid/nucleotide disorders (shi2025thediagnosisand pages 1-3).

### 10.5 Newborn screening
No evidence in retrieved texts confirms routine newborn screening implementation for ADSL deficiency; given the need for specialized metabolite testing and uncertain treatability, ADSL deficiency is not established as a standard NBS target in the retrieved evidence.

## 11. Outcomes / prognosis
Outcomes depend strongly on subtype. Neonatal forms can be fatal in weeks (jurecka2015adenylosuccinatelyasedeficiency pages 1-3). Long-term follow-up (10–34 years) demonstrates survival into adulthood for some patients, but with severe disability and often drug-resistant epilepsy in type I and neonatal phenotypes (cutillo2024electroclinicalfeaturesand pages 2-4, cutillo2024electroclinicalfeaturesand pages 14-15).

## 12. Treatment
### 12.1 Current standard-of-care (real-world)
There is no proven disease-modifying therapy; reviews emphasize symptomatic management. The 2015 review states: **“To date there is no specific and effective therapy for ADSL deficiency.”** (jurecka2015adenylosuccinatelyasedeficiency pages 1-3).

Supportive/standard management includes:
- Anti-seizure medications (ASM); some benefit in milder cases (cutillo2024electroclinicalfeaturesand pages 14-15)
- Developmental therapies and supportive care (implied; not detailed in retrieved texts)

### 12.2 Allopurinol (repurposing; clinical trial implementation)
**ClinicalTrials.gov NCT03776656** (Phase 2, single-group, n=8, completed) evaluated oral **allopurinol** for 12 months. Key details:
- Primary endpoint: Vineland II adaptive behavior composite score at 12 months (NCT03776656 chunk 1)
- Biochemical endpoints: serial urinary and plasma SAICAr and S‑Ado (NCT03776656 chunk 2, NCT03776656 chunk 1)
- Trial rationale notes the hypothesis that allopurinol reduces production of toxic SAICAr, and the protocol states the hypothesis “was validated in 3 minor patients with biological and clinical improvement” (NCT03776656 chunk 1).

The trial record also cites a linked publication (not retrievable here) titled: “Allopurinol Treatment Improves Cognitive Skills, Adaptive Behavior, and Biochemical Markers in Young Patients With Adenylosuccinate Lyase Deficiency” (PMID listed in the record) (NCT03776656 chunk 2). Interpretation should be cautious until full peer-reviewed results are examined.

### 12.3 Other attempted metabolic interventions (limited/experimental)
Across reviews and cohort appraisal, reported attempts include:
- Ketogenic diet trials with transient effects (camici2023inbornerrorsof pages 9-11)
- D-ribose (inconsistent/limited evidence) (camici2023inbornerrorsof pages 9-11, cutillo2024electroclinicalfeaturesand pages 14-15)
- S-adenosyl-L-methionine (limited success) (cutillo2024electroclinicalfeaturesand pages 14-15)
- Uridine (mentioned among attempted therapies in epilepsy-focused reviews) (shi2025thediagnosisand pages 1-3)

### 12.4 Suggested MAXO terms (examples)
- Allopurinol therapy (MAXO term to be mapped)
- Anticonvulsant therapy
- Ketogenic diet therapy
- Genetic counseling

## 13. Prevention
Primary prevention is not applicable beyond reproductive options because this is a Mendelian disorder.
- **Carrier screening / cascade testing** in families; **prenatal diagnosis** is described as limited to families with an affected child and relies on mutation testing (jurecka2015adenylosuccinatelyasedeficiency pages 8-9).
- **Secondary prevention**: earlier diagnosis to optimize seizure control and supportive interventions (jurecka2015adenylosuccinatelyasedeficiency pages 8-9).

## 14. Other species / natural disease
No naturally occurring veterinary syndrome was identified in the retrieved evidence.

## 15. Model organisms
### 15.1 C. elegans (2023): mechanistic and translational utility
Two 2023 studies establish and leverage a **C. elegans adsl-1** model:
- Neuromuscular and reproductive phenotypes with separable etiologies; some mobility defects reversible; fertility rescued by purine supplementation (fenton2023acaenorhabditiselegans pages 1-3, fenton2023acaenorhabditiselegans pages 8-9)
- Neurobehavioral phenotypes driven by disrupted tyramine signaling downstream of adsl-1 deficiency; tyramine supplementation rescues gustatory plasticity phenotype (moro2023adenylosuccinatelyasedeficiency pages 1-2, moro2023adenylosuccinatelyasedeficiency pages 11-13, moro2023adenylosuccinatelyasedeficiency pages 9-11)

**Applications:** pathway dissection (substrate toxicity vs purine deficiency), screening candidate interventions (e.g., pathway inhibitors or supplementation), and probing neurobehavioral mechanisms (fenton2023acaenorhabditiselegans pages 8-9, moro2023adenylosuccinatelyasedeficiency pages 9-11).

## Key recent developments (2023–2024) — highlights
- **Clinical natural history/electroclinical patterns (2024):** consolidated cohort of 88 patients, epilepsy prevalence 81.8%, and described EEG trajectories and imaging patterns (cutillo2024electroclinicalfeaturesand pages 1-2).
- **Mechanistic expansion (2023):** evidence that ADSL deficiency can perturb neurotransmitter pathways (tyramine signaling) in vivo in a genetic model, supporting wider metabolic effects beyond purine synthesis itself (moro2023adenylosuccinatelyasedeficiency pages 1-2).

## Limitations of this report (evidence gaps)
- Orphanet (ORPHA), ICD-10/ICD-11, and definitive MeSH UID were not directly extractable from the retrieved full text and should be added via dedicated database queries.
- The linked allopurinol results publication cited by ClinicalTrials.gov could not be retrieved in full text in this run; conclusions about efficacy should be treated as provisional until peer-reviewed results are reviewed (NCT03776656 chunk 2).


References

1. (jurecka2015adenylosuccinatelyasedeficiency pages 1-3): Agnieszka Jurecka, Marie Zikanova, Stanislav Kmoch, and Anna Tylki‐Szymańska. Adenylosuccinate lyase deficiency. Journal of Inherited Metabolic Disease, 38:231-242, Aug 2015. URL: https://doi.org/10.1007/s10545-014-9755-y, doi:10.1007/s10545-014-9755-y. This article has 158 citations and is from a peer-reviewed journal.

2. (donti2016diagnosisofadenylosuccinate pages 1-2): Taraka R. Donti, Gerarda Cappuccio, Leroy Hubert, Juanita Neira, Paldeep S. Atwal, Marcus J. Miller, Aaron L. Cardon, V. Reid Sutton, Brenda E. Porter, Fiona M. Baumer, Michael F. Wangler, Qin Sun, Lisa T. Emrick, and Sarah H. Elsea. Diagnosis of adenylosuccinate lyase deficiency by metabolomic profiling in plasma reveals a phenotypic spectrum. Molecular Genetics and Metabolism Reports, 8:61-66, Sep 2016. URL: https://doi.org/10.1016/j.ymgmr.2016.07.007, doi:10.1016/j.ymgmr.2016.07.007. This article has 66 citations.

3. (cutillo2024electroclinicalfeaturesand pages 1-2): Gianni Cutillo, Silvia Masnada, Gaetan Lesca, Dorothée Ville, Patrizia Accorsi, Lucio Giordano, Anna Pichiecchio, Marialuisa Valente, Paola Borrelli, Ottavia Eleonora Ferraro, and Pierangelo Veggiotti. Electroclinical features and phenotypic differences in adenylosuccinate lyase deficiency: long‐term follow‐up of seven patients from four families and appraisal of the literature. Epilepsia Open, 9:106-121, Nov 2024. URL: https://doi.org/10.1002/epi4.12837, doi:10.1002/epi4.12837. This article has 5 citations and is from a peer-reviewed journal.

4. (moro2023adenylosuccinatelyasedeficiency pages 1-2): Corinna A. Moro, Sabrina A. Sony, Latisha P. Franklin, Shirley Dong, Mia M. Peifer, Kathryn E. Wittig, and Wendy Hanna-Rose. Adenylosuccinate lyase deficiency affects neurobehavior via perturbations to tyramine signaling in caenorhabditis elegans. PLOS Genetics, 19:e1010974, Sep 2023. URL: https://doi.org/10.1371/journal.pgen.1010974, doi:10.1371/journal.pgen.1010974. This article has 8 citations and is from a domain leading peer-reviewed journal.

5. (NCT03776656 chunk 2):  Evaluation of a Treatment With Allopurinol in Adenylosuccinate Lyase Deficiency. Assistance Publique - Hôpitaux de Paris. 2019. ClinicalTrials.gov Identifier: NCT03776656

6. (NCT03776656 chunk 1):  Evaluation of a Treatment With Allopurinol in Adenylosuccinate Lyase Deficiency. Assistance Publique - Hôpitaux de Paris. 2019. ClinicalTrials.gov Identifier: NCT03776656

7. (fenton2023acaenorhabditiselegans pages 1-3): Adam R. Fenton, Haley N. Janowitz, Latisha P. Franklin, Riley G. Young, Corinna A. Moro, Michael V. DeGennaro, Melanie R. McReynolds, Wenqing Wang, and Wendy Hanna-Rose. A caenorhabditis elegans model of adenylosuccinate lyase deficiency reveals neuromuscular and reproductive phenotypes of distinct etiology. Molecular Genetics and Metabolism, 140:107686, Nov 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107686, doi:10.1016/j.ymgme.2023.107686. This article has 5 citations and is from a peer-reviewed journal.

8. (fenton2023acaenorhabditiselegans pages 15-16): Adam R. Fenton, Haley N. Janowitz, Latisha P. Franklin, Riley G. Young, Corinna A. Moro, Michael V. DeGennaro, Melanie R. McReynolds, Wenqing Wang, and Wendy Hanna-Rose. A caenorhabditis elegans model of adenylosuccinate lyase deficiency reveals neuromuscular and reproductive phenotypes of distinct etiology. Molecular Genetics and Metabolism, 140:107686, Nov 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107686, doi:10.1016/j.ymgme.2023.107686. This article has 5 citations and is from a peer-reviewed journal.

9. (camici2023inbornerrorsof pages 9-11): Marcella Camici, Mercedes Garcia-Gil, Simone Allegrini, Rossana Pesi, Giulia Bernardini, Vanna Micheli, and Maria Grazia Tozzi. Inborn errors of purine salvage and catabolism. Metabolites, 13:787, Jun 2023. URL: https://doi.org/10.3390/metabo13070787, doi:10.3390/metabo13070787. This article has 22 citations.

10. (cutillo2024electroclinicalfeaturesand pages 2-4): Gianni Cutillo, Silvia Masnada, Gaetan Lesca, Dorothée Ville, Patrizia Accorsi, Lucio Giordano, Anna Pichiecchio, Marialuisa Valente, Paola Borrelli, Ottavia Eleonora Ferraro, and Pierangelo Veggiotti. Electroclinical features and phenotypic differences in adenylosuccinate lyase deficiency: long‐term follow‐up of seven patients from four families and appraisal of the literature. Epilepsia Open, 9:106-121, Nov 2024. URL: https://doi.org/10.1002/epi4.12837, doi:10.1002/epi4.12837. This article has 5 citations and is from a peer-reviewed journal.

11. (donti2016diagnosisofadenylosuccinate pages 3-4): Taraka R. Donti, Gerarda Cappuccio, Leroy Hubert, Juanita Neira, Paldeep S. Atwal, Marcus J. Miller, Aaron L. Cardon, V. Reid Sutton, Brenda E. Porter, Fiona M. Baumer, Michael F. Wangler, Qin Sun, Lisa T. Emrick, and Sarah H. Elsea. Diagnosis of adenylosuccinate lyase deficiency by metabolomic profiling in plasma reveals a phenotypic spectrum. Molecular Genetics and Metabolism Reports, 8:61-66, Sep 2016. URL: https://doi.org/10.1016/j.ymgmr.2016.07.007, doi:10.1016/j.ymgmr.2016.07.007. This article has 66 citations.

12. (cutillo2024electroclinicalfeaturesand pages 14-15): Gianni Cutillo, Silvia Masnada, Gaetan Lesca, Dorothée Ville, Patrizia Accorsi, Lucio Giordano, Anna Pichiecchio, Marialuisa Valente, Paola Borrelli, Ottavia Eleonora Ferraro, and Pierangelo Veggiotti. Electroclinical features and phenotypic differences in adenylosuccinate lyase deficiency: long‐term follow‐up of seven patients from four families and appraisal of the literature. Epilepsia Open, 9:106-121, Nov 2024. URL: https://doi.org/10.1002/epi4.12837, doi:10.1002/epi4.12837. This article has 5 citations and is from a peer-reviewed journal.

13. (shi2025thediagnosisand pages 1-3): Yuqing Shi, Zihan Wei, Yan Feng, Ya-Jing Gan, Guo-Yan Li, and Yanchun Deng. The diagnosis and treatment of disorders of nucleic acid/nucleotide metabolism associated with epilepsy. Acta Epileptologica, Apr 2025. URL: https://doi.org/10.1186/s42494-025-00201-x, doi:10.1186/s42494-025-00201-x. This article has 3 citations.

14. (jurecka2015adenylosuccinatelyasedeficiency pages 4-6): Agnieszka Jurecka, Marie Zikanova, Stanislav Kmoch, and Anna Tylki‐Szymańska. Adenylosuccinate lyase deficiency. Journal of Inherited Metabolic Disease, 38:231-242, Aug 2015. URL: https://doi.org/10.1007/s10545-014-9755-y, doi:10.1007/s10545-014-9755-y. This article has 158 citations and is from a peer-reviewed journal.

15. (moro2023adenylosuccinatelyasedeficiency pages 9-11): Corinna A. Moro, Sabrina A. Sony, Latisha P. Franklin, Shirley Dong, Mia M. Peifer, Kathryn E. Wittig, and Wendy Hanna-Rose. Adenylosuccinate lyase deficiency affects neurobehavior via perturbations to tyramine signaling in caenorhabditis elegans. PLOS Genetics, 19:e1010974, Sep 2023. URL: https://doi.org/10.1371/journal.pgen.1010974, doi:10.1371/journal.pgen.1010974. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (jurecka2015adenylosuccinatelyasedeficiency pages 8-9): Agnieszka Jurecka, Marie Zikanova, Stanislav Kmoch, and Anna Tylki‐Szymańska. Adenylosuccinate lyase deficiency. Journal of Inherited Metabolic Disease, 38:231-242, Aug 2015. URL: https://doi.org/10.1007/s10545-014-9755-y, doi:10.1007/s10545-014-9755-y. This article has 158 citations and is from a peer-reviewed journal.

17. (moro2023adenylosuccinatelyasedeficiency pages 11-13): Corinna A. Moro, Sabrina A. Sony, Latisha P. Franklin, Shirley Dong, Mia M. Peifer, Kathryn E. Wittig, and Wendy Hanna-Rose. Adenylosuccinate lyase deficiency affects neurobehavior via perturbations to tyramine signaling in caenorhabditis elegans. PLOS Genetics, 19:e1010974, Sep 2023. URL: https://doi.org/10.1371/journal.pgen.1010974, doi:10.1371/journal.pgen.1010974. This article has 8 citations and is from a domain leading peer-reviewed journal.

18. (fenton2023acaenorhabditiselegans pages 8-9): Adam R. Fenton, Haley N. Janowitz, Latisha P. Franklin, Riley G. Young, Corinna A. Moro, Michael V. DeGennaro, Melanie R. McReynolds, Wenqing Wang, and Wendy Hanna-Rose. A caenorhabditis elegans model of adenylosuccinate lyase deficiency reveals neuromuscular and reproductive phenotypes of distinct etiology. Molecular Genetics and Metabolism, 140:107686, Nov 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107686, doi:10.1016/j.ymgme.2023.107686. This article has 5 citations and is from a peer-reviewed journal.

19. (macchiaiolo2017amildform pages 7-7): Marina Macchiaiolo, Sabina Barresi, Francesco Cecconi, Ginevra Zanni, Marcello Niceta, Emanuele Bellacchio, Giacomo Lazzarino, Angela Maria Amorini, Enrico Silvio Bertini, Salvatore Rizza, Benedetta Contardi, Marco Tartaglia, and Andrea Bartuli. A mild form of adenylosuccinate lyase deficiency in absence of typical brain mri features diagnosed by whole exome sequencing. Italian Journal of Pediatrics, Aug 2017. URL: https://doi.org/10.1186/s13052-017-0383-7, doi:10.1186/s13052-017-0383-7. This article has 16 citations and is from a peer-reviewed journal.
