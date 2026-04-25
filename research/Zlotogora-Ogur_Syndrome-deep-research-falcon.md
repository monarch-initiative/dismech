---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:05:22.845997'
end_time: '2026-04-24T18:23:33.485768'
duration_seconds: 1090.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Zlotogora-Ogur Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Zlotogora-Ogur Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Zlotogora-Ogur Syndrome** covering all of the
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
- **Disease Name:** Zlotogora-Ogur Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Zlotogora-Ogur Syndrome** covering all of the
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


# Zlotogora–Ogur Syndrome (CLPED1) — Comprehensive Disease Characteristics Report

## Executive summary
Zlotogora–Ogur syndrome is now generally considered part of **cleft lip/palate–ectodermal dysplasia syndrome 1 (CLPED1)** (also historically called **Margarita Island ectodermal dysplasia / Margarita Island type**), a **rare autosomal recessive** disorder characterized by **orofacial clefting**, **ectodermal dysplasia** (hair/skin/teeth/nails/sweat gland abnormalities), and **limb anomalies (syndactyly)**, with **variable neurodevelopmental involvement**. The condition is caused by **biallelic loss-of-function variants in PVRL1 (NECTIN1)**, encoding the cell–cell adhesion molecule **nectin-1**. (suzuki2000mutationsofpvrl1 pages 1-1, zlotogora1994syndactylyectodermaldysplasia pages 2-3, suzuki2000mutationsofpvrl1 pages 1-3, yoshida2015novelhomozygousmutation pages 1-3)

---

## 1. Disease information

### 1.1 Disease overview (definition)
Clinically, the syndrome was delineated as a pleiotropic association of **cleft lip/palate, syndactyly, ectodermal dysplasia, and (in some reports) psychomotor retardation/intellectual disability**. A widely cited clinical synthesis reports: **“The summary of the clinical manifestations is based on 31 patients affected with the syndrome observed from the age of 4 months to 65 years”**. (zlotogora1994syndactylyectodermaldysplasia pages 1-2)

Molecularly, the disorder corresponds to **autosomal recessive cleft lip/palate–ectodermal dysplasia (CLPED1)** due to **PVRL1/NECTIN1** mutations. (suzuki2000mutationsofpvrl1 pages 1-1, suzuki2000mutationsofpvrl1 pages 1-3)

### 1.2 Key identifiers
* **OMIM (preferred, molecular-era):** **225060** is used for CLPED1 / Margarita Island type in later reviews and tables. (visinoni2009ectodermaldysplasiasclinical pages 2-3, ganske2021cleftlipand pages 1-2)
* **OMIM (historical / inconsistent in older literature):** Older sources cite **MIM 225000 / 22500 / 225060** for overlapping clinical entities; an ED review notes **reassignment** of the former Zlotogora–Ogur number. (zlotogora1994syndactylyectodermaldysplasia pages 3-4, visinoni2009ectodermaldysplasiasclinical pages 2-3)
* **Gene:** **PVRL1 (NECTIN1)** at 11q23.3. (suzuki2000mutationsofpvrl1 pages 1-1, ganske2021cleftlipand pages 1-2)
* **MONDO / MeSH / ICD-10/ICD-11 / Orphanet:** Not identified within the retrieved evidence set; mapping should be confirmed via MONDO/Orphanet/MeSH/ICD registries outside this corpus.

### 1.3 Synonyms and alternative names
Commonly used names in the literature include:
* **Zlotogora–Ogur syndrome**
* **Syndactyly, ectodermal dysplasia, and cleft lip/palate**
* **Cleft lip/palate–ectodermal dysplasia syndrome**
* **CLPED1**
* **Margarita Island ectodermal dysplasia / Margarita Island type**
These synonym relationships are made explicit in molecular-era CLPED1 work and ED reviews. (suzuki2000mutationsofpvrl1 pages 1-1, visinoni2009ectodermaldysplasiasclinical pages 2-3, ganske2021cleftlipand pages 1-2)

### 1.4 Evidence source type (patient-level vs aggregated)
Evidence is derived from:
* **Patient-level case reports/series** (human clinical) describing multiple affected families and syndromic features (rodini1990autosomalrecessiveectodermal pages 3-4, rodini1990autosomalrecessiveectodermal pages 1-3)
* **Aggregated clinical synthesis** (human clinical summary of multiple reports; 31 cases across wide age range) (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* **Molecular genetics** (human genetic studies defining PVRL1/NECTIN1 as causal) (suzuki2000mutationsofpvrl1 pages 1-1, suzuki2000mutationsofpvrl1 pages 1-3, yoshida2015novelhomozygousmutation pages 1-3)
* **Experimental model systems** (mouse/in vitro) supporting a nectin–afadin developmental mechanism relevant to palate/periderm biology (lough2020disruptionofthe pages 1-3, lough2020disruptionofthe pages 3-5)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **PVRL1 (NECTIN1)**, encoding **nectin-1**, a cell–cell adhesion molecule.
* Molecular definition: CLPED1 is described as an **“autosomal recessive CL/P-ectodermal dysplasia (CLPED1; previously ED4)”** and the locus is identified as **PVRL1**, “encoding nectin-1”. (suzuki2000mutationsofpvrl1 pages 1-1)

### 2.2 Risk factors
#### Genetic risk factors (causal)
* **Autosomal recessive inheritance** is supported by repeated parental consanguinity in reported families: **“The occurrence of consanguinity in the 3 reported families is consistent with autosomal recessive inheritance.”** (rodini1990autosomalrecessiveectodermal pages 3-4)
* Multiple families show affected individuals **homozygous** for pathogenic PVRL1 alleles with heterozygous parents: **“In each case the affected patients were homozygous and their parents were heterozygous for the mutant alleles.”** (suzuki2000mutationsofpvrl1 pages 1-3)

#### Environmental risk factors
No established environmental risk factors for CLPED1/Zlotogora–Ogur syndrome were identified in the retrieved evidence.

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved corpus.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (human)
Across the clinical synthesis and primary reports, major features include:
* **Orofacial clefting:** “Cleft lip/palate is present in most patients.” (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* **Syndactyly:** “Cutaneous syndactyly is frequently present in fingers 2-3-4” and “In the feet syndactyly of toes 2-3 is usually present.” (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* **Ectodermal dysplasia:** sparse/short hair with structural defects (“pili torti” / “kinky hair”), dental anomalies, nail anomalies, hypohidrosis, and progressive palmoplantar hyperkeratosis. (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3)
* **Neurodevelopment:** variable impairment; “Mental status may be impaired” and family-to-family differences were noted. (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3)

The syndrome demonstrates marked variable expressivity: “The variability of the syndrome is evident…”. (zlotogora1994syndactylyectodermaldysplasia pages 1-2)

### 3.2 Phenotype characteristics (onset, severity, progression, frequency)
* **Onset:** structural anomalies (clefting, syndactyly) are **congenital**. (rodini1990autosomalrecessiveectodermal pages 1-3)
* **Progression:** **palmoplantar hyperkeratosis is progressive**, with specific appearance in childhood in at least one case. (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* **Neurodevelopmental severity:** ranges from normal cognition to intellectual disability depending on family/allele context. (zlotogora1994syndactylyectodermaldysplasia pages 2-3)
* **Mortality:** some sibships include **neonatal/early childhood deaths** of presumed affected individuals; “Some of the affected children died neonatally or at a young age” with cause “unknown.” (zlotogora1994syndactylyectodermaldysplasia pages 2-3)

### 3.3 Quality-of-life impact
Formal QoL instruments (EQ-5D/SF-36/PROMIS) were not identified in the retrieved evidence for CLPED1 specifically. However, the phenotype implies significant functional burden (feeding/speech/hearing/dental/dermatologic and surgical needs).

### 3.4 Suggested HPO terms
A curated phenotype-to-HPO mapping table is provided in Artifact-01.

| Phenotype / clinical description | Suggested HPO term(s) | Typical onset | Frequency / variability notes | Key supporting citations |
|---|---|---|---|---|
| Cleft lip and/or cleft palate; often bilateral, but some affected individuals may lack overt clefting and instead have philtrum/uvula anomalies | Cleft upper lip **HP:0000204**; Cleft palate **HP:0000175** | Congenital | Present in most patients; not fully penetrant across all reported families; neonatal deaths in some sibs with clefting were reported | (zlotogora1994syndactylyectodermaldysplasia pages 1-2, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Cutaneous syndactyly of fingers, especially 2-3-4; classic reports also note 2-3 finger involvement | 2-3 finger syndactyly **HP:0006101**; Cutaneous syndactyly of fingers **HP:0010709** | Congenital | Frequently present; variable severity and exact digits involved between families | (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Toe syndactyly, especially 2-3 toes | 2-3 toe syndactyly **HP:0001780** | Congenital | Usually present in reported cases, though variable and sometimes less emphasized than hand findings | (zlotogora1994syndactylyectodermaldysplasia pages 1-2, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Sparse, short, kinky hair; hair-shaft defects including pili torti; brittle/fine hair in later molecularly confirmed case | Sparse hair **HP:0008070**; Pili torti **HP:0003792**; Abnormal hair texture **HP:0011359** | Congenital / early childhood | Common ectodermal feature; one review noted progressive scalp involvement with complete alopecia by the fifth decade in some patients | (zlotogora1994syndactylyectodermaldysplasia pages 1-2, yoshida2015novelhomozygousmutation pages 1-3) |
| Hypohidrosis / reduced sweating with generally preserved heat tolerance | Hypohidrosis **HP:0000975** | Childhood or lifelong | Reported in most but not all patients; variable severity | (zlotogora1994syndactylyectodermaldysplasia pages 2-3, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Progressive palmar and plantar hyperkeratosis / palmoplantar keratoderma | Palmoplantar keratoderma **HP:0000982**; Hyperkeratosis **HP:0000962** | Childhood; may become more evident with age | Progressive feature; one report noted appearance around age 4 years; useful in differential diagnosis versus EEC in older patients | (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3) |
| Dental anomalies: delayed eruption, microdontia, hypodontia, anodontia | Hypodontia **HP:0000670**; Anodontia **HP:0000674**; Microdontia **HP:0000691**; Delayed eruption of teeth **HP:0000684** | Childhood | Very common ectodermal finding; severity ranges from delayed eruption to absent teeth in adults | (zlotogora1994syndactylyectodermaldysplasia pages 2-3, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Nail anomalies / brittle nails / onychodysplasia | Nail dysplasia **HP:0002164**; Brittle nails **HP:0001808** | Childhood | Variable; nails can be normal in some affected individuals | (zlotogora1994syndactylyectodermaldysplasia pages 2-3, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Intellectual disability / mental retardation and delayed psychomotor development | Intellectual disability **HP:0001249**; Global developmental delay **HP:0001263** | Infancy / childhood | Variable across families; initially thought obligatory, but later reports documented normal intelligence in some families; may reflect variable expressivity | (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Ear anomalies / malformed ears / preauricular pit | Abnormality of the ear **HP:0000598**; Preauricular pit **HP:0004467** | Congenital | Recurrent but variably reported; malformed ears emphasized in early descriptions | (rodini1990autosomalrecessiveectodermal pages 3-4, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Hearing loss / deafness | Hearing impairment **HP:0000365** | Childhood | Variable between families; present in some pedigrees but absent in others | (rodini1990autosomalrecessiveectodermal pages 3-4, zlotogora1994syndactylyectodermaldysplasia pages 2-3) |
| Genitourinary / renal anomalies | Genitourinary abnormality **HP:0000078**; Renal abnormality **HP:0000077** | Congenital | Inconsistent finding; reported in some families/case summaries, absent in others | (rodini1990autosomalrecessiveectodermal pages 3-4, zlotogora1994syndactylyectodermaldysplasia pages 2-3) |
| Accessory nipples / nipple anomalies | Supernumerary nipple **HP:0100807** | Congenital | Reported in several patients/families, but may represent a variable associated finding rather than a core feature | (rodini1990autosomalrecessiveectodermal pages 3-4, rodini1990autosomalrecessiveectodermal pages 1-3) |
| Dry skin / eczematous or dermatitis-like skin changes | Xerosis **HP:0000963**; Eczema **HP:0000964** | Infancy / childhood | Reported as part of ectodermal dysplasia spectrum; later molecularly confirmed case had treatment for eczematous skin/atopic dermatitis from infancy | (rodini1990autosomalrecessiveectodermal pages 3-4, yoshida2015novelhomozygousmutation pages 1-3) |
| Early death (neonatal death or death in early childhood) in some affected sibships | Neonatal death **HP:0003811**; Sudden death in infancy / early death **HP:0001522** | Neonatal / infancy | Not universal; several reports describe neonatal or early-childhood deaths among presumed affected sibs, with cause often unknown | (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3, rodini1990autosomalrecessiveectodermal pages 1-3) |


*Table: This table summarizes the core and variably reported phenotypes of Zlotogora-Ogur syndrome / CLPED1, with suggested HPO mappings, typical timing, and brief notes on expressivity. It is useful for knowledge-base curation and phenotype-to-ontology annotation.*

---

## 4. Genetic / molecular information

### 4.1 Causal gene
**PVRL1 (NECTIN1)** encodes **nectin-1**, an immunoglobulin superfamily adhesion protein.
* Molecular identification: “which we identify as **PVRL1, encoding nectin-1**, an immunoglobulin (Ig)-related transmembrane cell-cell adhesion molecule.” (suzuki2000mutationsofpvrl1 pages 1-1)

### 4.2 Pathogenic variants (examples with evidence)
From the gene-discovery study and subsequent case report:
* **Trp185Ter (W185X)**: “At codon Trp185 (TGG), a homozygous nonsense mutation (TAG) was found…” (suzuki2000mutationsofpvrl1 pages 1-3)
* **Frameshift at codon 185** (single-base deletion at Trp185): “a homozygous frameshift (TG–)…” (suzuki2000mutationsofpvrl1 pages 1-3)
* **Frameshift at Gly323** (single-base duplication): “At codon Gly323 (GGT), a homozygous frameshift (GGTT)…” (suzuki2000mutationsofpvrl1 pages 1-3)
* **c.400C>T (p.Arg134*)**: “Novel homozygous mutation, c.400C>T (p.Arg134*), in the PVRL1 gene…” (yoshida2015novelhomozygousmutation pages 1-3)

### 4.3 Functional consequences
The truncating variants are predicted to abrogate nectin-1’s intracellular interactions and adhesion signaling.
* Mechanism statement: the truncating mutations “would truncate…nectin-1…thereby abolishing interaction with 1-afadin and thus abrogating…cell-cell adhesion.” (suzuki2000mutationsofpvrl1 pages 1-3)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes or epigenetic signatures were identified in the retrieved CLPED1-specific evidence. Karyotype was reported normal in a classic clinical family. (rodini1990autosomalrecessiveectodermal pages 3-4)

---

## 5. Environmental information
No specific environmental/lifestyle/infectious contributors were identified in the retrieved evidence; CLPED1 is primarily a **monogenic Mendelian** disorder in the reviewed sources.

---

## 6. Mechanism / pathophysiology

### 6.1 Current understanding (nectin–afadin axis in epithelial morphogenesis)
A convergent theme is disruption of **adherens junction formation and epithelial adhesion** in craniofacial and ectodermal tissues.

* PVRL1/NECTIN1 is a cell–cell adhesion molecule; truncating variants disrupt interaction with afadin (the actin-binding scaffolding partner). (suzuki2000mutationsofpvrl1 pages 1-3)
* PVRL1 expression during development is reported in tissues relevant to CLPED1 phenotypes (palatal shelves, tooth buds, skin epithelium). (suzuki2000mutationsofpvrl1 pages 1-3)

### 6.2 Causal chain (conceptual)
1. **Biallelic PVRL1 loss-of-function** → truncated nectin-1 lacking proper intracellular signaling/anchoring. (suzuki2000mutationsofpvrl1 pages 1-3, yoshida2015novelhomozygousmutation pages 1-3)
2. **Loss of nectin–afadin linkage** → impaired adherens-junction assembly/maintenance and epithelial cohesion in developing palate/periderm and ectodermal appendage primordia. (suzuki2000mutationsofpvrl1 pages 1-3, lough2020disruptionofthe pages 3-5)
3. **Developmental morphogenesis failures** → palatal shelf fusion defects (clefting) and ectodermal derivative abnormalities (hair/teeth/nails/sweat glands), plus limb webbing/syndactyly. (zlotogora1994syndactylyectodermaldysplasia pages 1-2, rodini1990autosomalrecessiveectodermal pages 1-3)

### 6.3 Pathways and ontology suggestions
* **Cell adhesion / adherens junction organization:** GO:0034332 was invoked in 2024 protein-network analyses connecting afadin and nectins to adherens junction organization. (awotoye2024damagingmutationsin pages 9-13)
* Additional plausible GO terms for curation (not directly asserted in the texts but aligned with the described mechanism): “cell-cell adhesion” and “adherens junction assembly.”

### 6.4 Recent developments (prioritize 2023–2024)
Recent work does not primarily expand CLPED1 patient series, but refines mechanistic understanding of the **same junctional module**:

**(a) 2023 mechanobiology (preprint; protein–protein interaction under force):** Afadin PDZ–nectin-1 binding exhibits force-stabilized behavior. The preprint reports short solution lifetimes (“bond lifetimes of 1.2…s for the nectin-1…ICDs”) and concludes “PDZ domains can serve as force-responsive mechanical anchors at cell-cell adhesion complexes.” (vachharajani2023pdzdomainsfrom pages 1-3)

**(b) 2024 human genetics and network biology (peer-reviewed):** AFDN (afadin) damaging variants were proposed to contribute to nonsyndromic cleft risk, with analyses highlighting AFADIN’s direct interactions with nectins and a reported association of afadin–nectin interaction networks with CLPED biology (FDR reported in the paper). (awotoye2024damagingmutationsin pages 13-16, awotoye2024damagingmutationsin pages 9-13)

Evidence-type labeling:
* (a) computational + single-molecule biophysics; **preprint** (bioRxiv) (vachharajani2023pdzdomainsfrom pages 1-3)
* (b) human genetics cohorts + computational structural/network analyses; **peer-reviewed primary research** (awotoye2024damagingmutationsin pages 13-16, awotoye2024damagingmutationsin pages 9-13)

---

## 7. Anatomical structures affected
Based on the phenotype profile:
* **Craniofacial:** lip and palate (UBERON: lip/palate structures), dental primordia/teeth. (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3)
* **Integumentary system:** skin, hair follicles, sweat glands, nails. (zlotogora1994syndactylyectodermaldysplasia pages 1-2, zlotogora1994syndactylyectodermaldysplasia pages 2-3)
* **Limbs:** fingers/toes (cutaneous syndactyly). (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* **Potential additional systems:** auditory system (hearing loss), renal/genitourinary anomalies variably. (rodini1990autosomalrecessiveectodermal pages 3-4)

Cell types (CL suggestions) most directly implicated by the mechanism include **epithelial cells** of palatal shelves and epidermis/periderm (supported mechanistically by mouse epithelial perturbation studies). (lough2020disruptionofthe pages 3-5)

Subcellular components (GO Cellular Component) implicated: adherens junction complexes and associated cytoskeleton (supported conceptually; afadin/nectin are junctional/cytoskeletal linkers). (suzuki2000mutationsofpvrl1 pages 1-3, vachharajani2023pdzdomainsfrom pages 1-3)

---

## 8. Temporal development (onset and progression)
* **Congenital onset** of clefting and syndactyly is typical. (rodini1990autosomalrecessiveectodermal pages 1-3)
* **Progressive dermatologic manifestations** can emerge and worsen with age; palmoplantar hyperkeratosis is described as progressive, and alopecia can develop later in life in some individuals. (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* **Neurodevelopmental course** is variable (family-dependent). (zlotogora1994syndactylyectodermaldysplasia pages 2-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
Autosomal recessive inheritance is consistently supported:
* “The syndrome is inherited as an autosomal recessive trait.” (zlotogora1994syndactylyectodermaldysplasia pages 2-3)
* Multiple reports cite parental consanguinity: “In all the families reported up to now the parents of the affected children were related.” (zlotogora1994syndactylyectodermaldysplasia pages 2-3)

### 9.2 Epidemiology
Syndrome-specific prevalence/incidence was not identified in the retrieved evidence.

Available quantitative proxies:
* A clinical synthesis aggregated **31 patients** across reports. (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* In a large ED clinic cohort (not CLPED1-specific), **24/170 (14%)** ED patients had CL/P. (ganske2021cleftlipand pages 2-4)

### 9.3 Population genetics / founder effects
Repeated consanguinity suggests founder effects in reported families. (zlotogora1994syndactylyectodermaldysplasia pages 2-3)
Carrier frequency and population allele frequencies for specific PVRL1 pathogenic alleles were not available in the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Clinical recognition
A practical clinical definition is based on co-occurrence of:
1) CL/P, 2) ectodermal abnormalities (hair/teeth/nails/sweating/skin), 3) syndactyly.

In the ED-spectrum framing, “A diagnosis of ED requires defects in two or more ectodermal derivatives…”. (ganske2021cleftlipand pages 1-2)

### 10.2 Differential diagnosis
Zlotogora (1994) highlights distinction from **EEC syndrome**, noting differences in inheritance and features; it suggests palmoplantar hyperkeratosis in older patients can help distinguish the disorders. (zlotogora1994syndactylyectodermaldysplasia pages 2-3)

### 10.3 Genetic testing strategy (real-world implementation)
Evidence-supported approach:
* **Sequence PVRL1 (NECTIN1)** to confirm CLPED1 in suspected cases, especially in consanguineous families. (yoshida2015novelhomozygousmutation pages 1-3)
* Yoshida et al. performed direct sequencing of PVRL1 and family testing; parents were heterozygous carriers. (yoshida2015novelhomozygousmutation pages 1-3)

### 10.4 Ancillary testing
In the molecularly confirmed Japanese case, the work-up included:
* physiologic testing for hypohidrosis (sympathetic skin response)
* microscopy/SEM for hair-shaft abnormalities
* dermatologic evaluation and management for dermatitis. (yoshida2015novelhomozygousmutation pages 1-3)

---

## 11. Outcome / prognosis
Long-term prognosis is variable and not captured in prospective natural history studies in the retrieved corpus.

Observed outcomes include:
* Survival into adulthood (clinical synthesis includes patients up to 65 years). (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* Developmental disability can persist when present (classic family with affected brothers). (rodini1990autosomalrecessiveectodermal pages 1-3)
* Neonatal/early childhood deaths reported in some pedigrees, with unclear attribution. (zlotogora1994syndactylyectodermaldysplasia pages 2-3)

---

## 12. Treatment
No disease-modifying molecular therapy exists in the retrieved evidence; management is supportive and surgical.

### 12.1 Surgical and interventional
* **Cleft lip/palate repair**: historical clinical photos note repaired cleft lip; modern ED-CL/P care follows standard cleft protocols. (zlotogora1994syndactylyectodermaldysplasia pages 1-2, ganske2021cleftlipand pages 2-4)
* **Syndactyly repair**: surgical scars were described in a molecularly confirmed case, indicating real-world correction. (yoshida2015novelhomozygousmutation pages 1-3)

### 12.2 Supportive care
* Dermatologic treatment for dermatitis/eczema from infancy was reported in a molecularly confirmed case. (yoshida2015novelhomozygousmutation pages 1-3)
* ED-CL/P cohorts emphasize dental, otologic, ocular, and respiratory comorbidity management (though not specific to CLPED1 alone). (ganske2021cleftlipand pages 4-5, ganske2021cleftlipand pages 5-6)

### 12.3 Treatment outcomes and statistics (recent clinical data)
While not CLPED1-specific, ED-CL/P cohort outcomes provide real-world expectations for syndromic cleft care:
* In an ED cohort, **3/9 (33%)** older bilateral cases had velopharyngeal insufficiency; palatal fistula occurred (count reported). (ganske2021cleftlipand pages 2-4)
* Patients may have perioperative respiratory complications requiring ICU monitoring. (ganske2021cleftlipand pages 5-6)

### 12.4 MAXO term suggestions
* Cleft lip repair / cleft palate repair (MAXO: surgical repair of cleft lip/palate)
* Syndactyly surgical correction
* Genetic counseling
* Dental rehabilitation (prosthodontic/orthodontic management for hypodontia)
* Dermatologic therapy for eczema/keratoderma

### 12.5 Clinical trials
No CLPED1/Zlotogora–Ogur–specific therapeutic trials were identified; trials returned by broad searches primarily involved **NECTIN4 oncology targets** and are not relevant to treating CLPED1. (clinical-trials tool results; no relevant CLPED1 trials)

---

## 13. Prevention
Primary prevention is not applicable in the usual public-health sense for a monogenic Mendelian disorder. Prevention strategies are genetic:
* **Carrier testing and reproductive counseling** in affected families (supported by AR inheritance and consanguinity patterns). (zlotogora1994syndactylyectodermaldysplasia pages 2-3)
* **Prenatal / preimplantation genetic testing** is logically enabled when familial PVRL1 pathogenic variants are known (inference from established causality; family-based heterozygosity demonstrated). (suzuki2000mutationsofpvrl1 pages 1-3, yoshida2015novelhomozygousmutation pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.

---

## 15. Model organisms
Experimental systems show that disruption of the **nectin–afadin axis** can produce palatal fusion defects in mouse.

* Development 2020 supplementary evidence shows that epithelial afadin loss via in utero lentiviral Cre is sufficient to cause cleft palate, while a later keratin promoter Cre approach was insufficient in that context (“Afdn knockout via lenti-Cre is suffient to cause CP, while K14-Cre is insufficient”). (lough2020disruptionofthe pages 1-3)
* Dual knockdown of Nectin1 and Nectin4 produced delays in palatal shelf elevation and residual epithelial seam, and periderm abnormalities, supporting periderm/epithelium contributions to clefting. (lough2020disruptionofthe pages 3-5)

These models support a mechanistic bridge from PVRL1/NECTIN1 loss to impaired epithelial adhesion during palatogenesis.

---

## Structured identifier summary (artifact)
| Category | Details | Key reference(s) |
|---|---|---|
| Disease names / synonyms | **Zlotogora-Ogur syndrome**; **syndactyly, ectodermal dysplasia, and cleft lip/palate**; **cleft lip/palate-ectodermal dysplasia syndrome**; **CLPED1**; **Margarita Island ectodermal dysplasia / Margarita Island type**. Later reviews state Zlotogora-Ogur syndrome and Margarita Island type are considered the same condition within CLPED1. (suzuki2000mutationsofpvrl1 pages 1-1, zlotogora1994syndactylyectodermaldysplasia pages 1-2, visinoni2009ectodermaldysplasiasclinical pages 2-3) | Zlotogora 1994, *J Med Genet* 31:957-959, DOI: https://doi.org/10.1136/jmg.31.12.957; Suzuki et al. 2000, *Nat Genet* 25:427-430, DOI: https://doi.org/10.1038/78119 |
| Key identifiers (OMIM) | Historical OMIM usage in the literature is **inconsistent**. Primary molecular-era identifier for **CLPED1 / Margarita Island type** is **OMIM 225060**; reviews note the former Zlotogora-Ogur entry **OMIM 225000** was reassigned to **Rosselli-Gulienetti syndrome**, while older papers variably cited **225000/22500** for the cleft-ED-syndactyly phenotype. (zlotogora1994syndactylyectodermaldysplasia pages 3-4, visinoni2009ectodermaldysplasiasclinical pages 2-3, ganske2021cleftlipand pages 1-2) | Visinoni et al. 2009, *Am J Med Genet A* 149A:1980-2002, DOI: https://doi.org/10.1002/ajmg.a.32864; Ganske et al. 2021, *Cleft Palate Craniofac J* 58:237-243, DOI: https://doi.org/10.1177/1055665620949124 |
| Inheritance | **Autosomal recessive**; early case reports emphasized consanguinity in affected families and later molecular studies confirmed affected individuals were homozygous for pathogenic variants while parents were heterozygous carriers. (rodini1990autosomalrecessiveectodermal pages 3-4, zlotogora1994syndactylyectodermaldysplasia pages 2-3, suzuki2000mutationsofpvrl1 pages 1-3, yoshida2015novelhomozygousmutation pages 1-3, visinoni2009ectodermaldysplasiasclinical pages 2-3) | Rodini & Richieri-Costa 1990, *Am J Med Genet* 36:473-476, DOI: https://doi.org/10.1002/ajmg.1320360420 |
| Causal gene | **PVRL1** (also known as **NECTIN1**), encoding **nectin-1**, a cell-cell adhesion molecule/herpesvirus receptor. Loss-of-function variants truncate nectin-1 and are reported to abolish afadin-associated adhesion functions relevant to craniofacial and ectodermal development. (suzuki2000mutationsofpvrl1 pages 1-1, suzuki2000mutationsofpvrl1 pages 1-3, yoshida2015novelhomozygousmutation pages 1-3, ganske2021cleftlipand pages 1-2) | Suzuki et al. 2000, *Nat Genet* 25:427-430, DOI: https://doi.org/10.1038/78119 |
| Representative pathogenic variants | Reported homozygous **loss-of-function** variants include **Trp185Ter / W185X** (TGG→TAG), **frameshift at codon 185** (single-base deletion), **frameshift at Gly323** (GGT→GGTT), and **c.400C>T (p.Arg134\*)** in a Japanese patient. (suzuki2000mutationsofpvrl1 pages 1-3, yoshida2015novelhomozygousmutation pages 1-3, shu2015mutationanalysisof pages 3-7) | Suzuki et al. 2000, DOI: https://doi.org/10.1038/78119; Yoshida et al. 2015, *J Dermatol* 42:715-719, DOI: https://doi.org/10.1111/1346-8138.12882 |
| First clinical description / delineation | Early delineation came from families reported by **Zlotogora and Ogur** and by **Rodini & Richieri-Costa**, with core findings of cleft lip/palate, ectodermal dysplasia, syndactyly, and variable intellectual disability/psychomotor delay. (zlotogora1994syndactylyectodermaldysplasia pages 1-2, rodini1990autosomalrecessiveectodermal pages 3-4, freihofer1997ectodermaldysplasiacleft pages 5-5) | Rodini & Richieri-Costa 1990, *Am J Med Genet* 36:473-476, DOI: https://doi.org/10.1002/ajmg.1320360420; Zlotogora 1994 review, DOI: https://doi.org/10.1136/jmg.31.12.957 |
| Gene discovery milestone | Positional/molecular work showed that CLPED1, including Zlotogora-Ogur syndrome, is caused by **PVRL1/NECTIN1** mutations. (suzuki2000mutationsofpvrl1 pages 1-1, suzuki2000mutationsofpvrl1 pages 1-3) | Suzuki et al. 2000, *Nat Genet* 25:427-430, DOI: https://doi.org/10.1038/78119 |
| Later case report / phenotype expansion | A later Asian case confirmed **homozygous c.400C>T (p.Arg134\*)** in **PVRL1** and documented cleft lip/palate, hypohidrotic ectodermal dysplasia, cutaneous syndactyly, hypodontia, and hair-shaft abnormalities. (yoshida2015novelhomozygousmutation pages 1-3) | Yoshida et al. 2015, *J Dermatol* 42:715-719, DOI: https://doi.org/10.1111/1346-8138.12882 |


*Table: This table summarizes the main disease names, OMIM identifier history, inheritance, causal gene, and landmark references for Zlotogora-Ogur syndrome/CLPED1. It is useful for reconciling older clinical nomenclature with the later molecular definition based on PVRL1/NECTIN1.*

---

## Notes on evidence gaps (important for knowledge base curation)
* **MONDO/MeSH/ICD/Orphanet identifiers** were not retrieved here and should be cross-mapped externally.
* **Syndrome-specific prevalence/incidence**, **carrier frequency**, and **variant population allele frequencies** were not available in the retrieved full texts.
* **Standardized diagnostic criteria** (beyond phenotype and genetic confirmation) and **formal clinical guidelines** specific to CLPED1 were not identified.

---

## Key references (with publication dates and URLs)
* Rodini & Richieri-Costa. *Am J Med Genet*. **Aug 1990**. https://doi.org/10.1002/ajmg.1320360420 (rodini1990autosomalrecessiveectodermal pages 1-3)
* Zlotogora. *J Med Genet*. **Dec 1994**. https://doi.org/10.1136/jmg.31.12.957 (zlotogora1994syndactylyectodermaldysplasia pages 1-2)
* Suzuki et al. *Nat Genet*. **Aug 2000**. https://doi.org/10.1038/78119 (suzuki2000mutationsofpvrl1 pages 1-3)
* Visinoni et al. *Am J Med Genet A*. **Sep 2009**. https://doi.org/10.1002/ajmg.a.32864 (visinoni2009ectodermaldysplasiasclinical pages 2-3)
* Yoshida et al. *J Dermatol*. **Jul 2015**. https://doi.org/10.1111/1346-8138.12882 (yoshida2015novelhomozygousmutation pages 1-3)
* Ganske et al. *Cleft Palate Craniofac J*. **Aug 2021**. https://doi.org/10.1177/1055665620949124 (ganske2021cleftlipand pages 2-4)
* Vachharajani et al. bioRxiv. **Oct 2023**. https://doi.org/10.1101/2023.09.24.559210 (vachharajani2023pdzdomainsfrom pages 1-3)
* Awotoye et al. *Cleft Palate Craniofac J*. **Nov 2024**. https://doi.org/10.1177/10556656221135926 (awotoye2024damagingmutationsin pages 13-16)


References

1. (suzuki2000mutationsofpvrl1 pages 1-1): Koji Suzuki, Diane Hu, Tania Bustos, Joel Zlotogora, Antonio Richieri-Costa, Jill A. Helms, and Richard A. Spritz. Mutations of pvrl1, encoding a cell-cell adhesion molecule/herpesvirus receptor, in cleft lip/palate-ectodermal dysplasia. Nature Genetics, 25:427-430, Aug 2000. URL: https://doi.org/10.1038/78119, doi:10.1038/78119. This article has 437 citations and is from a highest quality peer-reviewed journal.

2. (zlotogora1994syndactylyectodermaldysplasia pages 2-3): J. Zlotogora. Syndactyly, ectodermal dysplasia, and cleft lip/palate. Journal of Medical Genetics, 31:957-959, Dec 1994. URL: https://doi.org/10.1136/jmg.31.12.957, doi:10.1136/jmg.31.12.957. This article has 30 citations and is from a domain leading peer-reviewed journal.

3. (suzuki2000mutationsofpvrl1 pages 1-3): Koji Suzuki, Diane Hu, Tania Bustos, Joel Zlotogora, Antonio Richieri-Costa, Jill A. Helms, and Richard A. Spritz. Mutations of pvrl1, encoding a cell-cell adhesion molecule/herpesvirus receptor, in cleft lip/palate-ectodermal dysplasia. Nature Genetics, 25:427-430, Aug 2000. URL: https://doi.org/10.1038/78119, doi:10.1038/78119. This article has 437 citations and is from a highest quality peer-reviewed journal.

4. (yoshida2015novelhomozygousmutation pages 1-3): Kazue Yoshida, Ryota Hayashi, Hideki Fujita, Masaya Kubota, Mai Kondo, Yutaka Shimomura, and Hironori Niizeki. Novel homozygous mutation, c.400c>t (p.arg134*), in the pvrl1 gene underlies cleft lip/palate‐ectodermal dysplasia syndrome in an asian patient. The Journal of Dermatology, 42:715-719, Jul 2015. URL: https://doi.org/10.1111/1346-8138.12882, doi:10.1111/1346-8138.12882. This article has 18 citations.

5. (zlotogora1994syndactylyectodermaldysplasia pages 1-2): J. Zlotogora. Syndactyly, ectodermal dysplasia, and cleft lip/palate. Journal of Medical Genetics, 31:957-959, Dec 1994. URL: https://doi.org/10.1136/jmg.31.12.957, doi:10.1136/jmg.31.12.957. This article has 30 citations and is from a domain leading peer-reviewed journal.

6. (visinoni2009ectodermaldysplasiasclinical pages 2-3): Átila F. Visinoni, Toni Lisboa‐Costa, Nina A.B. Pagnan, and Eleidi A. Chautard‐Freire‐Maia. Ectodermal dysplasias: clinical and molecular review. American Journal of Medical Genetics Part A, 149A:1980-2002, Sep 2009. URL: https://doi.org/10.1002/ajmg.a.32864, doi:10.1002/ajmg.a.32864. This article has 244 citations.

7. (ganske2021cleftlipand pages 1-2): Ingrid M. Ganske, Tim Irwin, Olivia Langa, Joseph Upton, Wen-Hann Tan, and John B. Mulliken. Cleft lip and palate in ectodermal dysplasia. The Cleft Palate-Craniofacial Journal, 58:237-243, Aug 2021. URL: https://doi.org/10.1177/1055665620949124, doi:10.1177/1055665620949124. This article has 11 citations.

8. (zlotogora1994syndactylyectodermaldysplasia pages 3-4): J. Zlotogora. Syndactyly, ectodermal dysplasia, and cleft lip/palate. Journal of Medical Genetics, 31:957-959, Dec 1994. URL: https://doi.org/10.1136/jmg.31.12.957, doi:10.1136/jmg.31.12.957. This article has 30 citations and is from a domain leading peer-reviewed journal.

9. (rodini1990autosomalrecessiveectodermal pages 3-4): Elaine S. O. Rodini and A. Richieri‐Costa. Autosomal recessive ectodermal dysplasia, cleft lip/palate, mental retardation, and syndactyly: the zlotogora-ogur syndrome. American journal of medical genetics, 36 4:473-6, Aug 1990. URL: https://doi.org/10.1002/ajmg.1320360420, doi:10.1002/ajmg.1320360420. This article has 26 citations.

10. (rodini1990autosomalrecessiveectodermal pages 1-3): Elaine S. O. Rodini and A. Richieri‐Costa. Autosomal recessive ectodermal dysplasia, cleft lip/palate, mental retardation, and syndactyly: the zlotogora-ogur syndrome. American journal of medical genetics, 36 4:473-6, Aug 1990. URL: https://doi.org/10.1002/ajmg.1320360420, doi:10.1002/ajmg.1320360420. This article has 26 citations.

11. (lough2020disruptionofthe pages 1-3): Kendall J. Lough, Danielle C. Spitzer, Abby J. Bergman, Jessica J. Wu, Kevin M. Byrd, and Scott E. Williams. Disruption of the nectin-afadin complex recapitulates features of the human cleft lip/palate syndrome clped1. Development, Jan 2020. URL: https://doi.org/10.1242/dev.189241, doi:10.1242/dev.189241. This article has 26 citations and is from a domain leading peer-reviewed journal.

12. (lough2020disruptionofthe pages 3-5): Kendall J. Lough, Danielle C. Spitzer, Abby J. Bergman, Jessica J. Wu, Kevin M. Byrd, and Scott E. Williams. Disruption of the nectin-afadin complex recapitulates features of the human cleft lip/palate syndrome clped1. Development, Jan 2020. URL: https://doi.org/10.1242/dev.189241, doi:10.1242/dev.189241. This article has 26 citations and is from a domain leading peer-reviewed journal.

13. (awotoye2024damagingmutationsin pages 9-13): Waheed Awotoye, Peter A Mossey, Jacqueline B Hetmanski, Lord J J Gowans, Mekonen A Eshete, Wasiu L Adeyemo, Azeez Alade, Erliang Zeng, Olawale Adamson, Olutayo James, Azeez Fashina, Modupe O Ogunlewe, Thirona Naicker, Chinyere Adeleke, Tamara Busch, Mary Li, Aline Petrin, Abimbola Oladayo, Sami Kayali, Joy Olotu, Veronica Sule, Mohaned Hassan, John Pape, Emmanuel T Aladenika, Peter Donkor, Fareed K N Arthur, Solomon Obiri-Yeboah, Daniel K Sabbah, Pius Agbenorku, Debashree Ray, Gyikua Plange-Rhule, Alexander Acheampong Oti, Daniah Albokhari, Nara Sobreira, Martine Dunnwald, Terri H Beaty, Margaret Taub, Mary L Marazita, Adebowale A Adeyemo, Jeffrey C Murray, and Azeez Butali. Damaging mutations in afdn contribute to risk of nonsyndromic cleft lip with or without cleft palate. The Cleft Palate Craniofacial Journal, 61:697-705, Nov 2024. URL: https://doi.org/10.1177/10556656221135926, doi:10.1177/10556656221135926. This article has 6 citations.

14. (vachharajani2023pdzdomainsfrom pages 1-3): Vipul T. Vachharajani, Matthew P. DeJong, Soumya Dutta, Jonathan Chapman, Eashani Ghosh, Abhishek Singharoy, and Alexander R. Dunn. Pdz domains from the junctional proteins afadin and zo-1 act as mechanosensors. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2023.09.24.559210, doi:10.1101/2023.09.24.559210. This article has 9 citations.

15. (awotoye2024damagingmutationsin pages 13-16): Waheed Awotoye, Peter A Mossey, Jacqueline B Hetmanski, Lord J J Gowans, Mekonen A Eshete, Wasiu L Adeyemo, Azeez Alade, Erliang Zeng, Olawale Adamson, Olutayo James, Azeez Fashina, Modupe O Ogunlewe, Thirona Naicker, Chinyere Adeleke, Tamara Busch, Mary Li, Aline Petrin, Abimbola Oladayo, Sami Kayali, Joy Olotu, Veronica Sule, Mohaned Hassan, John Pape, Emmanuel T Aladenika, Peter Donkor, Fareed K N Arthur, Solomon Obiri-Yeboah, Daniel K Sabbah, Pius Agbenorku, Debashree Ray, Gyikua Plange-Rhule, Alexander Acheampong Oti, Daniah Albokhari, Nara Sobreira, Martine Dunnwald, Terri H Beaty, Margaret Taub, Mary L Marazita, Adebowale A Adeyemo, Jeffrey C Murray, and Azeez Butali. Damaging mutations in afdn contribute to risk of nonsyndromic cleft lip with or without cleft palate. The Cleft Palate Craniofacial Journal, 61:697-705, Nov 2024. URL: https://doi.org/10.1177/10556656221135926, doi:10.1177/10556656221135926. This article has 6 citations.

16. (ganske2021cleftlipand pages 2-4): Ingrid M. Ganske, Tim Irwin, Olivia Langa, Joseph Upton, Wen-Hann Tan, and John B. Mulliken. Cleft lip and palate in ectodermal dysplasia. The Cleft Palate-Craniofacial Journal, 58:237-243, Aug 2021. URL: https://doi.org/10.1177/1055665620949124, doi:10.1177/1055665620949124. This article has 11 citations.

17. (ganske2021cleftlipand pages 4-5): Ingrid M. Ganske, Tim Irwin, Olivia Langa, Joseph Upton, Wen-Hann Tan, and John B. Mulliken. Cleft lip and palate in ectodermal dysplasia. The Cleft Palate-Craniofacial Journal, 58:237-243, Aug 2021. URL: https://doi.org/10.1177/1055665620949124, doi:10.1177/1055665620949124. This article has 11 citations.

18. (ganske2021cleftlipand pages 5-6): Ingrid M. Ganske, Tim Irwin, Olivia Langa, Joseph Upton, Wen-Hann Tan, and John B. Mulliken. Cleft lip and palate in ectodermal dysplasia. The Cleft Palate-Craniofacial Journal, 58:237-243, Aug 2021. URL: https://doi.org/10.1177/1055665620949124, doi:10.1177/1055665620949124. This article has 11 citations.

19. (shu2015mutationanalysisof pages 3-7): S.Y. Shu, M.J. Zhang, H.Q. Cheng, S.J. Tang, W.L. Chen, S.R. Wu, Y. Lin, and Q.S. Chen. Mutation analysis of pvrl1 in patients with non-syndromic cleft of the lip and/or palate in guangdong. Genetics and molecular research : GMR, 14 2:3400-8, Apr 2015. URL: https://doi.org/10.4238/2015.april.15.3, doi:10.4238/2015.april.15.3. This article has 5 citations.

20. (freihofer1997ectodermaldysplasiacleft pages 5-5): Hans Peter M. Freihofer, Sajjad Walji, and Han G. Brunner. Ectodermal dysplasia, cleft lip/palate, and severe cutaneous and osseous syndactyly in a mentally retarded girl: a new multiple malformation syndrome. American journal of medical genetics, 70 3:211-5, Jun 1997. URL: https://doi.org/10.1002/(sici)1096-8628(19970613)70:3<211::aid-ajmg1>3.0.co;2-z, doi:10.1002/(sici)1096-8628(19970613)70:3<211::aid-ajmg1>3.0.co;2-z. This article has 6 citations.