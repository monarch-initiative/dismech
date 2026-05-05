---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T13:44:28.288074'
end_time: '2026-04-24T13:59:44.145076'
duration_seconds: 915.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ankylosing Spondylitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 60
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ankylosing Spondylitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Ankylosing Spondylitis** covering all of the
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
- **Disease Name:** Ankylosing Spondylitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Ankylosing Spondylitis** covering all of the
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


# Comprehensive Research Report: Ankylosing Spondylitis (AS) / Axial Spondyloarthritis (axSpA)

## Executive summary (current understanding; 2023–2024 emphasis)
Ankylosing spondylitis (AS) is the radiographic form of the axial spondyloarthritis (axSpA) spectrum, characterized by chronic inflammatory back pain with sacroiliac joint (SIJ) and spinal involvement and frequent extra-musculoskeletal manifestations (uveitis, psoriasis, inflammatory bowel disease) (harrison2023havetherapeuticsenhanced pages 1-2, zimba2024diagnosismonitoringand pages 1-2). Current mechanistic understanding centers on genetic predisposition (notably HLA-B27 with non-HLA loci such as ERAP1/2 and IL23R), immune activation dominated by TNF and IL-17 pathways at the enthesis and axial skeleton, and environmental influences including dysbiosis/infections, mechanical stress, smoking/oxidative stress and diet (fatica2023howhasmolecular pages 1-2, pasaran2024anactualinsight pages 5-7, bilski2024environmentalandgenetic pages 18-19). In 2023–2024, clinical progress includes formalizing a research definition of “early axSpA” (≤2 years of axial symptoms) (navarrocompan2024asasconsensusdefinition pages 2-2), biomarker guidance reinforcing HLA-B27 testing and CRP/ESR monitoring (liu2024aguidelineon pages 2-3), and pivotal/longer-term trial evidence for newer targeted therapies (bimekizumab, upadacitinib) with sustained response rates and quantified safety event rates (baraliakos2024efficacyandsafety pages 1-2, baraliakos2024bimekizumabtreatmentin pages 5-6, baraliakos2024bimekizumabtreatmentin pages 9-10).

## 1. Disease information

### 1.1 What is ankylosing spondylitis?
AS is a chronic inflammatory arthritis predominantly affecting the sacroiliac joints and spine, producing back pain, stiffness, and functional impairment; it sits within the broader axSpA spectrum (harrison2023havetherapeuticsenhanced pages 1-2, baraliakos2024bimekizumabtreatmentin pages 1-2). MRI enables identification of inflammatory lesions prior to structural changes visible on plain radiographs, which is why axSpA is commonly discussed as radiographic (AS) versus non-radiographic disease (harrison2023havetherapeuticsenhanced pages 1-2, zimba2024diagnosismonitoringand pages 1-2).

### 1.2 Key identifiers and ontology mappings (availability in retrieved evidence)
* **ICD-10**: M45 used to identify AS in national claims/registry analyses (South Korea NHID study) (nam2024epidemiologictrendsand pages 4-5). 
* **OpenTargets / ontology IDs (partial)**: Ankylosing spondylitis is indexed as **EFO_0003898** in the OpenTargets evidence output; related SpA concept **EFO_0000706** is listed, and a juvenile form appears as **MONDO_0020655** (juvenile ankylosing spondylitis) (OpenTargets output in tool state; not directly citable as a pqac evidence chunk beyond the retrieved text context, so not asserted as a primary identifier here).

Because the retrieved full-text evidence did not include authoritative ontology pages for **MONDO (AS)**, **MeSH**, **ICD-11**, **OMIM**, or **Orphanet**, these identifiers cannot be fully populated from tool-retrieved primary sources in this run.

### 1.3 Synonyms / alternative names
* **Radiographic axial spondyloarthritis (r-axSpA)** is used as a synonym for **ankylosing spondylitis** (harrison2023havetherapeuticsenhanced pages 1-2, zimba2024diagnosismonitoringand pages 1-2).
* **Axial spondyloarthritis (axSpA)** is the umbrella term including both radiographic AS (r-axSpA) and **non-radiographic axSpA (nr-axSpA)** (zimba2024diagnosismonitoringand pages 1-2).

### 1.4 Evidence source type
The information synthesized here is derived from aggregated disease-level resources: peer-reviewed reviews, consensus/guideline statements, clinical trial reports, and national registry/claims-based epidemiology (harrison2023havetherapeuticsenhanced pages 1-2, liu2024aguidelineon pages 2-3, nam2024epidemiologictrendsand pages 4-5).

## 2. Etiology

### 2.1 Disease causal factors (genetic + mechanistic)
AS is best modeled as a multifactorial, polygenic immune-mediated disease in which genetic predisposition interacts with environmental triggers to drive innate and adaptive immune activation at the enthesis and axial skeleton (fatica2023howhasmolecular pages 1-2, pasaran2024anactualinsight pages 5-7).

* **HLA-B27 and heritability:** HLA-B27 is a major genetic contributor; one 2023 review summarizes that “HLA-B27 contributes by 20.44% to axSpA heritability” (fatica2023howhasmolecular pages 1-2). The 2024 biomarker guideline notes ~85% of AS patients are HLA-B27 positive versus ~8% in the general population and that HLA-B27 is an indispensable element of ASAS classification criteria (liu2024aguidelineon pages 2-3).
* **Non-HLA loci and antigen processing:** ERAP1/2 and IL23R are highlighted among non-HLA genes implicated by GWAS; ERAP1 variants genetically interact with HLA-B27, consistent with a model where altered antigen processing/MHC-I peptide presentation contributes to disease (fatica2023howhasmolecular pages 1-2). 
* **Cytokine pathways:** The IL-23/Th17/IL-17 axis is central in mechanistic reviews; IL-23 supports Th17 differentiation and IL-17 production (fatica2023howhasmolecular pages 1-2). 

### 2.2 Risk factors (genetic)
* **HLA-B27**: strong association; high prevalence among AS patients and used clinically for classification (liu2024aguidelineon pages 2-3). 
* **ERAP1/2 and IL23R**: repeatedly cited susceptibility loci; ERAP1–HLA-B27 genetic interaction is emphasized (fatica2023howhasmolecular pages 1-2). 

### 2.3 Risk factors (environmental/lifestyle)
Recent 2024 reviews describe multiple plausible and/or observed environmental contributors:

* **Smoking and oxidative stress:** A 2024 review emphasizes that smoking increases oxidative stress via free radical production and disrupts pro-/antioxidant balance; it cites evidence that cigarette smoking status predicts spinal radiographic progression in early axSpA (bilski2024environmentalandgenetic pages 18-19). The same review discusses increased oxidative stress markers (e.g., MDA/TOS) and reduced antioxidant status in AS, supporting oxidative injury as a contributor/biological correlate (bilski2024environmentalandgenetic pages 6-8).
* **Environmental pollutants/heavy metals:** Heavy metals and environmental pollutants are highlighted as potential contributors via oxidative stress and inflammatory signaling (e.g., NF-κB activation by vanadate) (bilski2024environmentalandgenetic pages 18-19, bilski2024environmentalandgenetic pages 25-26).
* **Diet and lifestyle:** Low omega-3/fiber and high ultra-processed food intake are associated with higher SpA activity in cited studies; longer duration of physical exercise appears protective in Mendelian randomization; poor sleep/depression correlate with worse outcomes (bilski2024environmentalandgenetic pages 11-12, bilski2024environmentalandgenetic pages 12-14).

### 2.4 Infectious agents and microbiome-related triggers
Mechanistic synthesis from 2024 highlights intestinal dysbiosis, altered gut permeability, and candidate microbial triggers:

* **Dysbiosis and specific taxa:** Increased abundance of taxa including *Ruminococcus gnavus* and *Clostridium* spp. is reported in severe AS (pasaran2024anactualinsight pages 5-7).
* **Candidate enteric triggers and fungal associations:** Enteric bacteria (e.g., *Klebsiella, Yersinia, Shigella, Salmonella*, Enterobacteriaceae) are discussed in the context of molecular mimicry/arthritogenic peptides; *Candida albicans* is discussed via IL-17 induction and gut permeability mechanisms (pasaran2024anactualinsight pages 5-7).
* **Gut–joint axis cell trafficking model:** A proposed mechanism is gut-derived IL-23-driven trafficking of α4β7+ ILC3 to joints with IL-17/IL-22 production (pasaran2024anactualinsight pages 5-7).

### 2.5 Mechanical stress (gene–environment relevant trigger)
Mechanical stress at entheses is proposed to cause microtrauma with release of cartilage peptides (fibronectin, hyaluronate), local vascularization and inflammation—positioning mechanical factors as triggers interacting with immune/genetic predisposition (pasaran2024anactualinsight pages 5-7).

### 2.6 Protective factors
Evidence in retrieved 2024 reviews suggests:
* **Physical exercise** may be protective (Mendelian randomization evidence summarized) (bilski2024environmentalandgenetic pages 11-12).
* **Vitamin D**: a 2024 mechanistic review summarizes meta-analytic signals that vitamin D deficiency may be associated with AS and that vitamin D may have a protective role (pasaran2024anactualinsight pages 10-11).

## 3. Phenotypes (clinical manifestations)

### 3.1 Core axial manifestations
axSpA primarily affects the SIJs and spine with inflammatory back pain; stiffness and fatigue are emphasized in clinical trial background and reviews (harrison2023havetherapeuticsenhanced pages 1-2, baraliakos2024bimekizumabtreatmentin pages 1-2). MRI can identify spinal/SIJ inflammation before radiographic change (harrison2023havetherapeuticsenhanced pages 1-2).

### 3.2 Peripheral musculoskeletal features
Peripheral arthritis, enthesitis, and dactylitis occur in axSpA and are listed as key clinical features (harrison2023havetherapeuticsenhanced pages 1-2). Resolution of swollen joint count (SJC=0) is reported as an outcome in BE MOBILE trials (e.g., SJC=0 values at Week 52 are reported in excerpted evidence) (baraliakos2024bimekizumabtreatmentin pages 5-6).

### 3.3 Extra-musculoskeletal manifestations
Extra-musculoskeletal manifestations commonly include uveitis, psoriasis and inflammatory bowel disease (harrison2023havetherapeuticsenhanced pages 1-2). In BE MOBILE 1/2 at Week 52, uveitis and IBD events were observed (uveitis 1.2–2.1%; IBD 0.8–0.9%) (baraliakos2024bimekizumabtreatmentin pages 1-2). In longer-term upadacitinib data, uveitis incidence is quantified as 1.3 events/100 patient-years (baraliakos2024efficacyandsafety pages 7-10).

### 3.4 Age of onset / onset characteristics
Early axSpA is defined by symptom duration ≤2 years (for research), and ASAS entry criteria for classification focus on chronic back pain >3 months with onset before age 45 (navarrocompan2024asasconsensusdefinition pages 2-2, zimba2024diagnosismonitoringand pages 2-3).

### 3.5 Suggested HPO terms (non-exhaustive; concept mapping)
Because HPO mapping tables were not retrieved, the following are reasonable candidate mappings based on described phenotypes:
* Inflammatory back pain / chronic back pain (concept aligned with axSpA entry criteria) (zimba2024diagnosismonitoringand pages 2-3)
* Morning stiffness (accepted axial symptom in early axSpA definition) (navarrocompan2024asasconsensusdefinition pages 2-2)
* Buttock pain; thoracic pain; cervical pain (accepted axial symptom items) (navarrocompan2024asasconsensusdefinition pages 2-2)
* Enthesitis; arthritis; dactylitis (harrison2023havetherapeuticsenhanced pages 1-2)
* Uveitis; inflammatory bowel disease; psoriasis (harrison2023havetherapeuticsenhanced pages 1-2, baraliakos2024bimekizumabtreatmentin pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genes vs susceptibility genes
AS is not a monogenic disorder in the retrieved sources; instead, it is strongly polygenic with a major HLA association and multiple susceptibility loci (fatica2023howhasmolecular pages 1-2).

**Key susceptibility genes discussed in retrieved evidence:**
* **HLA-B27** (major risk allele; clinical biomarker) (liu2024aguidelineon pages 2-3)
* **ERAP1/ERAP2** (antigen processing; genetic interaction with HLA-B27; proposed therapeutic target) (fatica2023howhasmolecular pages 1-2)
* **IL23R** (Th17 axis; genetic polymorphism associated; elevated IL-23/IL-17 described) (pasaran2024anactualinsight pages 10-11, fatica2023howhasmolecular pages 1-2)

### 4.2 Functional consequences (current hypotheses)
* **Antigen processing and presentation:** ERAP1/2 trimming influences MHC-I peptide repertoire; ERAP1–HLA-B27 interaction supports an “arthritogenic peptide”/antigen-presentation model (fatica2023howhasmolecular pages 1-2).
* **Microbiome-mediated immune activation:** HLA-B27 may alter gut microbiota and gut permeability, contributing to aberrant immune responses (fatica2023howhasmolecular pages 1-2, pasaran2024anactualinsight pages 5-7).

### 4.3 Epigenetics
Epigenetic mechanisms are referenced as emerging contributors regulating gene expression in SpA pathogenesis, but specific methylation marks or histone modifications are not detailed in retrieved excerpts (fatica2023howhasmolecular pages 1-2).

## 5. Environmental information (expanded)
Environmental/lifestyle determinants summarized above include smoking, heavy metals/pollution, diet composition, sleep, alcohol, and microbial associations (bilski2024environmentalandgenetic pages 18-19, bilski2024environmentalandgenetic pages 11-12, bilski2024environmentalandgenetic pages 25-26). Mechanistically, oxidative stress markers are elevated and antioxidant capacity reduced in AS cohorts as summarized in 2024 review evidence, supporting a link between exposures that increase reactive oxygen species and inflammatory pathways (bilski2024environmentalandgenetic pages 6-8).

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (integrated model)
A plausible causal chain synthesized from 2023–2024 sources is:
1) **Genetic predisposition** (HLA-B27 with ERAP1/2, IL23R and other loci) establishes altered antigen processing/presentation and immune setpoints (fatica2023howhasmolecular pages 1-2). 
2) **Environmental triggers** (gut dysbiosis/infections, smoking/oxidative stress, pollutants; plus **mechanical microtrauma at entheses**) promote innate immune activation and barrier dysfunction (pasaran2024anactualinsight pages 5-7, bilski2024environmentalandgenetic pages 18-19). 
3) **Innate and adaptive immune activation** at entheses/SIJs/spine leads to cytokine production (TNF, IL-23/IL-17), recruiting inflammatory cells and sustaining inflammation (pasaran2024anactualinsight pages 10-11, pasaran2024anactualinsight pages 5-7). 
4) **Downstream tissue remodeling**: inflammation intersects with bone metabolism pathways yielding both bone loss/erosion and osteoproliferation/ankylosis over time (fatica2023howhasmolecular pages 1-2).

### 6.2 Key pathways and processes
* **TNF axis:** TNF is a pivotal cytokine with broad expression; it modulates innate immunity and Th1/Th17 signaling (harrison2023havetherapeuticsenhanced pages 1-2).
* **IL-23/Th17/IL-17 axis:** IL-23 supports Th17 differentiation and IL-17 production; elevated IL-23/IL-17 levels and IL23R polymorphism are reported (fatica2023howhasmolecular pages 1-2, pasaran2024anactualinsight pages 10-11). Mechanistic evidence highlights IL-23R+ entheseal lymphocytes and γδ T cells producing IL-17A in entheses (pasaran2024anactualinsight pages 5-7).
* **Enthesis biology:** Entheseal resident immune cells (including CD3+CD4−CD8− IL-23R+ lymphocytes and γδ T cells) are present in normal and affected human entheses and can produce IL-17A (pasaran2024anactualinsight pages 5-7).
* **Bone remodeling:** Reviews describe coexisting bone loss/osteoporosis and osteoproliferation as part of a complex bone metabolism disturbance, driving long-term structural damage (fatica2023howhasmolecular pages 1-2).
* **Gut–joint axis:** Dysbiosis, gut permeability, and trafficking of gut-primed immune cells (e.g., α4β7+ ILC3) to joints are proposed mechanisms (pasaran2024anactualinsight pages 5-7).

### 6.3 Suggested GO biological process terms (examples)
Based on mechanisms described:
* “inflammatory response”, “tumor necrosis factor production”, “interleukin-17 production”, “T helper 17 cell differentiation”, “antigen processing and presentation of peptide antigen via MHC class I”, “bone remodeling” (fatica2023howhasmolecular pages 1-2, pasaran2024anactualinsight pages 5-7).

### 6.4 Suggested CL (Cell Ontology) terms (examples)
* Th17 cell; γδ T cell; innate lymphoid cell (ILC3); macrophage; dendritic cell; natural killer cell—cell types explicitly referenced in inflammatory recruitment and entheseal biology (pasaran2024anactualinsight pages 10-11, pasaran2024anactualinsight pages 5-7).

## 7. Anatomical structures affected

### 7.1 Organ/system level (primary)
* **Axial skeleton**: sacroiliac joints and spine are primary sites (harrison2023havetherapeuticsenhanced pages 1-2, zimba2024diagnosismonitoringand pages 1-2).

### 7.2 Tissue/cell level
* **Entheses** (tendon/ligament attachment sites) are highlighted as initiating/propagating sites where mechanical stress and resident immune cells contribute to inflammation (pasaran2024anactualinsight pages 5-7).

### 7.3 Suggested UBERON terms (examples)
* sacroiliac joint; vertebral column; enthesis (conceptual mapping from anatomical descriptions) (harrison2023havetherapeuticsenhanced pages 1-2, pasaran2024anactualinsight pages 5-7).

## 8. Temporal development (onset and progression)

### 8.1 “Early axSpA” (2024 ASAS consensus)
ASAS defines early axSpA (for research) as axSpA with **≤2 years duration of axial symptoms**, defined as cervical/thoracic/back/buttock pain or morning stiffness, regardless of radiographic damage or syndesmophytes (navarrocompan2024asasconsensusdefinition pages 2-2).

### 8.2 Disease course and progression
Reviews emphasize that MRI can reveal inflammation before radiographic change; structural damage accumulates over time, with bone turnover abnormalities contributing to osteitis, erosions, osteosclerosis, and osteoproliferation (harrison2023havetherapeuticsenhanced pages 1-2, fatica2023howhasmolecular pages 1-2). Smoking is cited as predicting spinal radiographic progression in early axSpA (bilski2024environmentalandgenetic pages 18-19).

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
* **South Korea (nationwide NHID, 2010–2021):** age-standardized prevalence rose from **34.60/100,000 (2010)** to **91.01/100,000 (2021)**; age-standardized incidence rose from **4.41/100,000 person-years (2010)** to **8.33/100,000 person-years (2021)** (nam2024epidemiologictrendsand pages 4-5). Younger groups showed notable increases (e.g., ages 20–29: 6.38→13.72/100,000 PY) (nam2024epidemiologictrendsand pages 4-5).
* **Colombia (SISPRO registry, 2017–2021):** prevalence depends strongly on case definition. AS-code-defined prevalence **26.3/100,000** (12,684 cases) with male:female 1.2:1; broader axSpA coding yields **55–56/100,000**, and including sacroiliitis codes increases estimates to **244/100,000** (likely overestimation per authors) (barahonacorrea2024prevalenceofaxial pages 1-2, barahonacorrea2024prevalenceofaxial pages 2-5).

### 9.2 Sex ratio and demographics
Across epidemiologic framing, male predominance is often reported for AS; a review summarizes male:female ratio ~2–3:1 with more even distribution in nr-axSpA (zimba2024diagnosismonitoringand pages 1-2). Colombia registry AS-only coding suggests male:female 1.2:1, while broader coding including sacroiliitis skews female (barahonacorrea2024prevalenceofaxial pages 2-5).

## 10. Diagnostics

### 10.1 Classification criteria and diagnostic approach
* **ASAS classification entry condition:** chronic back pain >3 months, onset <45 years (zimba2024diagnosismonitoringand pages 2-3).
* **ASAS classification arms:** sacroiliitis on imaging + ≥1 SpA feature, **or** HLA-B27 positivity + ≥2 SpA features (zimba2024diagnosismonitoringand pages 2-3).
* **No single definitive test:** diagnosis requires integrating clinical, laboratory and imaging data (zimba2024diagnosismonitoringand pages 8-9).

### 10.2 Biomarkers (2024 guideline)
A 2024 evidence- and consensus-based biomarker guideline provides strong recommendations for:
* **HLA-B27 testing** in suspected axSpA (chronic low back pain >3 months, onset <45) (liu2024aguidelineon pages 2-3).
* **Regular-interval monitoring of CRP/ESR** (liu2024aguidelineon pages 2-3).
The guideline also notes HLA-B27 may relate to progression from nr-axSpA to radiographic disease at the SIJ but “has no value” in predicting spinal syndesmophyte formation/radiographic progression (liu2024aguidelineon pages 2-3).

### 10.3 Imaging and real-world implementation of imaging referrals (ASAS 2024)
ASAS 2024 recommendations focus on what clinical information must accompany imaging referrals for suspected/known axSpA. Required context includes age/sex, HLA-B27 status, pain duration/localization and inflammatory features, and symptom evolution for follow-up; prior imaging access is recommended (diekhoff2024clinicalinformationon pages 2-2, diekhoff2024clinicalinformationon pages 3-4). The recommendations highlight that clinical context is essential for protocol selection and interpretation, because mechanical strain and childbirth can produce MRI changes that mimic inflammation (diekhoff2024clinicalinformationon pages 4-4).

## 11. Outcome / prognosis

Direct mortality or long-term survival statistics were not retrieved in the evidence set. However, the disease is associated with substantial symptom burden (pain, stiffness, fatigue) and extra-musculoskeletal complications including uveitis and IBD (harrison2023havetherapeuticsenhanced pages 1-2, baraliakos2024bimekizumabtreatmentin pages 1-2). Smoking is associated with worse outcomes and radiographic progression in early axSpA (bilski2024environmentalandgenetic pages 18-19). Long-term trial extension data (upadacitinib) provide radiographic non-progression rates (>93% with mSASSS change <2 at 2 years) in a biologic-refractory population, supporting potential disease-control impacts on structural outcomes under effective therapy (baraliakos2024efficacyandsafety pages 1-2).

## 12. Treatment (current applications; 2023–2024 developments)

### 12.1 Standard-of-care classes (real-world implementation)
A 2023 review outlines stepwise management: **NSAIDs/COX-2 inhibitors** as first-line therapy, but ~one-third of patients fail or are intolerant; **TNF inhibitors** were first licensed for r-axSpA in 2003; additional approved options include **IL-17A inhibitors** and **JAK inhibitors** (harrison2023havetherapeuticsenhanced pages 1-2).

### 12.2 2023–2024 clinical trial evidence (key statistics)
Two pivotal 2024 publications provide longer-term outcomes for newer therapies:

* **Upadacitinib (JAK inhibitor), SELECT-AXIS 2 (AS, bDMARD-IR):** At Week 104, ASAS40 response was 64.9% (continuous upadacitinib) and 61.7% (placebo→upadacitinib). Radiographic progression was minimal: 94.9% and 93.8% had mSASSS change <2 at Week 104. Safety event rates included TEAEs 165.2/100 patient-years; MACE 0.3/100 PY and VTE 0.3/100 PY; serious infection 3.6/100 PY; herpes zoster 3.8/100 PY (baraliakos2024efficacyandsafety pages 1-2, baraliakos2024efficacyandsafety pages 7-10, baraliakos2024efficacyandsafety pages 4-7).
* **Bimekizumab (dual IL-17A/IL-17F inhibitor), BE MOBILE 1/2:** At Week 52, ASAS40 (NRI) was 60.9% (BKZ) vs 50.8% (PBO→BKZ) for nr-axSpA and 58.4% vs 68.5% for r-axSpA/AS. Safety through Week 52: any TEAE ~75% with exposure-adjusted incidence rates ~200/100 PY; serious TEAEs 3.7% (nr-axSpA) and 6.1% (r-axSpA); oral candidiasis 6.1–7.4% (baraliakos2024bimekizumabtreatmentin pages 5-6, baraliakos2024bimekizumabtreatmentin pages 9-10).

### 12.3 MAXO (Medical Action Ontology) term suggestions (examples)
* NSAID therapy; TNF inhibitor therapy; interleukin-17 inhibitor therapy; Janus kinase inhibitor therapy; physiotherapy/exercise therapy (based on treatment classes described) (harrison2023havetherapeuticsenhanced pages 1-2).

### 12.4 Ongoing / real-world trials and implementations
A ClinicalTrials.gov-registered real-world study of secukinumab effectiveness in biologic-naïve AS patients in Korea is recruiting (NCT06905288) (NCT06905288 chunk 2).

## 13. Prevention

No primary-prevention intervention specific to AS incidence is established in the retrieved evidence. Practical prevention is best framed as:
* **Secondary prevention**: reduce diagnostic delay by applying classification entry features (chronic back pain >3 months, onset <45) and using HLA-B27 testing and MRI when indicated (liu2024aguidelineon pages 2-3, zimba2024diagnosismonitoringand pages 2-3).
* **Tertiary prevention**: mitigate structural progression and disability by controlling inflammation with stepwise therapy (NSAIDs → biologics/targeted synthetics) and addressing modifiable factors such as smoking, exercise, sleep and diet (harrison2023havetherapeuticsenhanced pages 1-2, bilski2024environmentalandgenetic pages 18-19, bilski2024environmentalandgenetic pages 11-12).

## 14. Other species / natural disease
Direct veterinary natural-disease analogs were not retrieved. Mechanistic reviews discuss microbial triggers and immune pathways but do not provide naturally occurring animal epidemiology.

## 15. Model organisms / experimental models
The retrieved evidence provides general support for animal models implicating TNF and IL-23/IL-17 pathway dysfunction and entheseal immune cell biology but lacks detailed, named model descriptions (e.g., SKG mice) in the extracted pages (pasaran2024anactualinsight pages 5-7). Therefore, specific model organism characterization is incomplete in this evidence set.

## Summary artifacts
The following tables consolidate key structured facts for knowledge-base ingestion.

| Domain | Item | Key details | Source (year, URL) |
|---|---|---|---|
| Disease spectrum / classification | Radiographic axSpA (r-axSpA) / ankylosing spondylitis | r-axSpA is synonymous with ankylosing spondylitis and is defined by definite radiographic sacroiliac joint damage; axSpA is the umbrella term covering both radiographic and non-radiographic disease (harrison2023havetherapeuticsenhanced pages 1-2, zimba2024diagnosismonitoringand pages 1-2) | Harrison & Marzo-Ortega 2023, https://doi.org/10.1007/s11926-023-01097-7; Zimba et al. 2024, https://doi.org/10.1007/s00296-024-05615-3 |
| Disease spectrum / classification | Non-radiographic axSpA (nr-axSpA) | nr-axSpA refers to patients meeting axSpA classification concepts without definitive radiographic sacroiliac damage; MRI can detect inflammatory lesions before structural change on X-ray (harrison2023havetherapeuticsenhanced pages 1-2, zimba2024diagnosismonitoringand pages 1-2) | Harrison & Marzo-Ortega 2023, https://doi.org/10.1007/s11926-023-01097-7; Zimba et al. 2024, https://doi.org/10.1007/s00296-024-05615-3 |
| Disease spectrum / classification | Early axSpA definition | ASAS consensus: early axSpA = axial symptoms ≤2 years, regardless of presence/absence of radiographic SIJ damage or syndesmophytes; endorsed by 88% of ASAS members (navarrocompan2024asasconsensusdefinition pages 2-2) | Navarro-Compán et al. 2024, https://doi.org/10.1136/ard-2023-224232 |
| Disease spectrum / classification | Early axSpA symptom items | Axial symptoms accepted for early axSpA definition: cervical pain, thoracic pain, back pain, buttock pain, morning stiffness; shoulder pain and hip pain were rejected; symptoms should be judged by a rheumatologist (navarrocompan2024asasconsensusdefinition pages 2-2) | Navarro-Compán et al. 2024, https://doi.org/10.1136/ard-2023-224232 |
| Classification criteria | ASAS entry criteria | Entry condition: chronic/persistent back pain >3 months with onset before age 45 years (liu2024aguidelineon pages 2-3, zimba2024diagnosismonitoringand pages 2-3) | Liu et al. 2024, https://doi.org/10.3389/fimmu.2024.1394148; Zimba et al. 2024, https://doi.org/10.1007/s00296-024-05615-3 |
| Classification criteria | ASAS classification arms | Classification can be fulfilled by sacroiliitis on imaging plus ≥1 SpA feature, or HLA-B27 positivity plus ≥2 SpA features (zimba2024diagnosismonitoringand pages 2-3) | Zimba et al. 2024, https://doi.org/10.1007/s00296-024-05615-3 |
| Diagnostic biomarkers / tests | HLA-B27 testing | Guideline gives a strong recommendation for HLA-B27 testing in patients suspected of axSpA, especially chronic low back pain >3 months with onset <45 years; HLA-B27 is part of ASAS classification criteria; ~85% of AS patients are HLA-B27 positive vs ~8% of the general population (liu2024aguidelineon pages 2-3) | Liu et al. 2024, https://doi.org/10.3389/fimmu.2024.1394148 |
| Diagnostic biomarkers / tests | CRP/ESR monitoring | Biomarker guideline gives a strong recommendation for regular-interval monitoring of CRP/ESR in axSpA evaluation; acute-phase reactants may still be normal in many symptomatic patients, so labs must be integrated with clinical and imaging data (liu2024aguidelineon pages 2-3, zimba2024diagnosismonitoringand pages 1-2, zimba2024diagnosismonitoringand pages 8-9) | Liu et al. 2024, https://doi.org/10.3389/fimmu.2024.1394148; Zimba et al. 2024, https://doi.org/10.1007/s00296-024-05615-3 |
| Diagnostic biomarkers / tests | Imaging referral essentials | ASAS imaging-referral recommendations: include age, sex, HLA-B27 status, back pain duration/localisation/inflammatory features, symptom changes for follow-up, prior imaging, suspected diagnosis/differentials, and contraindications; MRI/X-ray/CT choice should be individualized and clinically contextualized (diekhoff2024clinicalinformationon pages 1-1, diekhoff2024clinicalinformationon pages 4-4, diekhoff2024clinicalinformationon pages 2-2, diekhoff2024clinicalinformationon pages 3-4) | Diekhoff et al. 2024, https://doi.org/10.1136/ard-2024-226280 |
| Epidemiology (2024 study) | South Korea prevalence trend | Age-standardized prevalence of AS increased from 34.60 per 100,000 in 2010 to 91.01 per 100,000 in 2021 (95% CIs 34.03–35.17 and 90.08–91.94, respectively) (nam2024epidemiologictrendsand pages 4-5, nam2024epidemiologictrendsand pages 1-2) | Nam et al. 2024, https://doi.org/10.3349/ymj.2024.0041 |
| Epidemiology (2024 study) | South Korea incidence trend | Age-standardized incidence increased from 4.41 per 100,000 person-years in 2010 to 8.33 per 100,000 person-years in 2021 (95% CIs 4.20–4.61 and 8.04–8.62); ages 20–29 rose from 6.38 to 13.72 per 100,000 person-years (nam2024epidemiologictrendsand pages 4-5, nam2024epidemiologictrendsand pages 1-2) | Nam et al. 2024, https://doi.org/10.3349/ymj.2024.0041 |
| Epidemiology (2024 study) | Colombia 5-year prevalence range | Using SISPRO registry data (2017–2021), 5-year adjusted prevalence estimates ranged from 26.3 to 244 per 100,000 inhabitants depending on case definition; inclusion of sacroiliitis code likely overestimates axSpA frequency (barahonacorrea2024prevalenceofaxial pages 1-2, barahonacorrea2024prevalenceofaxial pages 2-5) | Barahona-Correa et al. 2024, https://doi.org/10.1007/s10067-023-06799-y |
| Epidemiology (2024 study) | Colombia AS-specific prevalence | Ankylosing spondylitis-specific 5-year adjusted prevalence was 26.3 per 100,000 overall; sex-specific prevalence 29.2 per 100,000 in males and 23.5 per 100,000 in females; prevalence peaked at age 50–54 years (barahonacorrea2024prevalenceofaxial pages 1-2) | Barahona-Correa et al. 2024, https://doi.org/10.1007/s10067-023-06799-y |
| Epidemiology (2024 study) | Colombia broader axSpA definitions | Diagnoses compatible with axSpA excluding sacroiliitis: 55–56 per 100,000; including sacroiliitis: 244 per 100,000 (0.24%), with marked female predominance in the broadest coding approach (barahonacorrea2024prevalenceofaxial pages 2-5, barahonacorrea2024prevalenceofaxial pages 5-7) | Barahona-Correa et al. 2024, https://doi.org/10.1007/s10067-023-06799-y |


*Table: This table condenses the disease-spectrum definitions, core classification and diagnostic items, and recent registry-based epidemiology for ankylosing spondylitis/axial spondyloarthritis. It is useful as a quick-reference artifact for structured knowledge-base curation with source URLs and supporting context IDs.*

| Therapy | Trial / population | Key efficacy timepoint(s) | Main efficacy results | Key safety results | Trial ID / URL |
|---|---|---|---|---|---|
| Upadacitinib 15 mg | SELECT-AXIS 2, biologic-refractory active AS / r-axSpA | Week 14 primary endpoint | ASAS40: 45% with upadacitinib vs 18% with placebo, *p*<0.0001 (baraliakos2023efficacyandsafety pages 1-2) | No malignancies, MACE, VTE, or deaths reported in the 52-week report excerpt; more serious AEs, infections, hepatic disorders, and neutropenia than placebo noted qualitatively (baraliakos2023efficacyandsafety pages 1-2) | NCT04169373; https://clinicaltrials.gov/study/NCT04169373 ; https://doi.org/10.1186/s13075-023-03128-1 |
| Upadacitinib 15 mg | SELECT-AXIS 2, biologic-refractory active AS / r-axSpA | Week 52 | Continuous upadacitinib vs placebo→upadacitinib: ASAS40 66% vs 65%; ASDAS low disease activity 57% vs 55%; ASDAS inactive disease 26% vs 25%; mean change total back pain -4.5 vs -4.3; nocturnal back pain -4.6 vs -4.4; BASFI -3.6 vs -3.5 (baraliakos2023efficacyandsafety pages 1-2) | No new safety risks identified in 1-year OLE report (baraliakos2023efficacyandsafety pages 1-2) | NCT04169373; https://clinicaltrials.gov/study/NCT04169373 ; https://doi.org/10.1186/s13075-023-03128-1 |
| Upadacitinib 15 mg | SELECT-AXIS 2 open-label extension, biologic-refractory active AS / r-axSpA | Week 104 | Continuous upadacitinib vs placebo→upadacitinib: ASAS40 64.9% vs 61.7%; ASDAS change -2.1 vs -2.0; total back pain change -4.9 vs -4.6; >93% showed no radiographic progression (mSASSS change <2); more specifically 94.9% vs 93.8% had mSASSS change <2; LS mean mSASSS change 0.1 vs 0.2 (baraliakos2024efficacyandsafety pages 1-2, baraliakos2024efficacyandsafety pages 4-7, baraliakos2024efficacyandsafety pages 10-11) | TEAE rate 165.2 events/100 PY; serious AEs 8.7/100 PY; AEs leading to discontinuation 3.6/100 PY; serious infection 3.6/100 PY; herpes zoster 3.8/100 PY; malignancy excluding NMSC 0.3/100 PY; MACE 0.3/100 PY; VTE 0.3/100 PY; one death 0.1/100 PY; uveitis 1.3/100 PY; grade 3 neutrophil reduction 2.7%; grade 3 lymphocyte reduction 1.2%; grade 3 ALT and AST increases 1.5% each (baraliakos2024efficacyandsafety pages 1-2, baraliakos2024efficacyandsafety pages 7-10) | NCT04169373; https://clinicaltrials.gov/study/NCT04169373 ; https://doi.org/10.1186/s13075-024-03412-8 |
| Bimekizumab 160 mg Q4W | BE MOBILE 1, nr-axSpA | Week 52 | ASAS40 60.9% for BKZ vs 50.8% for placebo→BKZ; mean ASDAS change -1.8 vs -1.6; ASDAS low disease activity 61.6% vs 54.5%; ASDAS inactive disease 25.2% vs 28.0% (baraliakos2024bimekizumabtreatmentin pages 2-3, baraliakos2024bimekizumabtreatmentin pages 5-6) | Overall Weeks 0-52: any TEAE 183 patients (75.0%), EAIR 202.1/100 PY; serious TEAEs 9 (3.7%), EAIR 4.4/100 PY; SAEs 8/244 (3.3%), EAIR 3.9/100 PY; TEAEs leading to discontinuation 8 (3.3%), EAIR 3.9/100 PY; oral candidiasis 18 (7.4%); uveitis 3 (1.2%); IBD 2 (0.8%); no deaths (baraliakos2024bimekizumabtreatmentin pages 1-2, baraliakos2024bimekizumabtreatmentin pages 6-7, baraliakos2024bimekizumabtreatmentin pages 9-10) | BE MOBILE 1 / NCT03928704; https://clinicaltrials.gov/study/NCT03928704 ; https://doi.org/10.1136/ard-2023-224803 |
| Bimekizumab 160 mg Q4W | BE MOBILE 2, r-axSpA / AS | Week 52 | ASAS40 58.4% for BKZ vs 68.5% for placebo→BKZ; mean ASDAS change -1.7 vs -1.9; ASDAS low disease activity 57.1% vs 66.4%; ASDAS inactive disease 23.4% vs 37.1% (baraliakos2024bimekizumabtreatmentin pages 2-3, baraliakos2024bimekizumabtreatmentin pages 5-6) | Overall Weeks 0-52: any TEAE 249 patients (75.5%), EAIR 200.8/100 PY; drug-related TEAEs 135 (40.9%), EAIR 67.1/100 PY; serious TEAEs 20 (6.1%), EAIR 7.1/100 PY; SAEs 16/330 (4.8%), EAIR 5.6/100 PY; TEAEs leading to discontinuation 16 (4.8%), EAIR 5.6/100 PY; oral candidiasis 20 (6.1%); uveitis 7 (2.1%); IBD 3 (0.9%); no deaths (baraliakos2024bimekizumabtreatmentin pages 1-2, baraliakos2024bimekizumabtreatmentin pages 6-7, baraliakos2024bimekizumabtreatmentin pages 9-10) | BE MOBILE 2 / NCT03928743; https://clinicaltrials.gov/study/NCT03928743 ; https://doi.org/10.1136/ard-2023-224803 |


*Table: This table summarizes the key 2023-2024 efficacy and safety outcomes for upadacitinib and bimekizumab in ankylosing spondylitis/axial spondyloarthritis using only retrieved evidence. It is useful as a quick-reference comparison of pivotal trial endpoints, radiographic outcomes, and adverse-event rates.*

## Notes on evidence gaps relative to requested template
* **Ontology identifiers (MONDO for AS, MeSH, OMIM, Orphanet, ICD-11)** were not directly retrievable in the provided corpus; this report therefore limits identifier assertions to ICD-10 usage (M45) and axSpA terminology supported by clinical literature (nam2024epidemiologictrendsand pages 4-5, zimba2024diagnosismonitoringand pages 1-2).
* **PMID-level citations**: the retrieved evidence is primarily DOI-addressed full texts; PubMed IDs were not present in the extracted passages. Where OpenTargets listed PubMed IDs, they were not returned as primary full-text evidence chunks and thus were not used for mechanistic claim substantiation.


References

1. (harrison2023havetherapeuticsenhanced pages 1-2): S. R. Harrison and H. Marzo-Ortega. Have therapeutics enhanced our knowledge of axial spondyloarthritis? Current Rheumatology Reports, 25:56-67, Jan 2023. URL: https://doi.org/10.1007/s11926-023-01097-7, doi:10.1007/s11926-023-01097-7. This article has 20 citations and is from a peer-reviewed journal.

2. (zimba2024diagnosismonitoringand pages 1-2): Olena Zimba, Burhan Fatih Kocyigit, and Mariusz Korkosz. Diagnosis, monitoring, and management of axial spondyloarthritis. Rheumatology International, 44:1395-1407, May 2024. URL: https://doi.org/10.1007/s00296-024-05615-3, doi:10.1007/s00296-024-05615-3. This article has 34 citations and is from a peer-reviewed journal.

3. (fatica2023howhasmolecular pages 1-2): Mauro Fatica, Arianna D’Antonio, Lucia Novelli, Paola Triggianese, Paola Conigliaro, Elisabetta Greco, Alberto Bergamini, Carlo Perricone, and Maria Sole Chimenti. How has molecular biology enhanced our undertaking of axspa and its management. Current Rheumatology Reports, 25:12-33, Oct 2023. URL: https://doi.org/10.1007/s11926-022-01092-4, doi:10.1007/s11926-022-01092-4. This article has 17 citations and is from a peer-reviewed journal.

4. (pasaran2024anactualinsight pages 5-7): Emilia-Daniela Păsăran, Andreea Elena Diaconu, Corina Oancea, Andra-Rodica Bălănescu, Sorina Maria Aurelian, and Corina Homentcovschi. An actual insight into the pathogenic pathways of ankylosing spondylitis. Current Issues in Molecular Biology, 46:12800-12812, Nov 2024. URL: https://doi.org/10.3390/cimb46110762, doi:10.3390/cimb46110762. This article has 11 citations.

5. (bilski2024environmentalandgenetic pages 18-19): Rafał Bilski, Piotr Kamiński, Daria Kupczyk, Sławomir Jeka, Jędrzej Baszyński, Halina Tkaczenko, and Natalia Kurhaluk. Environmental and genetic determinants of ankylosing spondylitis. International Journal of Molecular Sciences, 25:7814, Jul 2024. URL: https://doi.org/10.3390/ijms25147814, doi:10.3390/ijms25147814. This article has 37 citations.

6. (navarrocompan2024asasconsensusdefinition pages 2-2): Victoria Navarro-Compán, Diego Benavent, Dafne Capelusnik, Désirée van der Heijde, Robert BM Landewé, Denis Poddubnyy, Astrid van Tubergen, Xenofon Baraliakos, Filip E Van den Bosch, Floris A van Gaalen, Lianne Gensler, Clementina López-Medina, Helena Marzo-Ortega, Anna Molto, Rodolfo Pérez-Alamino, Martin Rudwaleit, Marleen van de Sande, Raj Sengupta, Ulrich Weber, and Sofia Ramiro. Asas consensus definition of early axial spondyloarthritis. Annals of the Rheumatic Diseases, 83:1093-1099, Sep 2024. URL: https://doi.org/10.1136/ard-2023-224232, doi:10.1136/ard-2023-224232. This article has 89 citations and is from a highest quality peer-reviewed journal.

7. (liu2024aguidelineon pages 2-3): Dong Liu, Ya Xie, Liudan Tu, Xianghui Wen, Qing Lv, Budian Liu, Mingcan Yang, Xinyu Wu, Xuqi Zheng, Xiqing Luo, Liuzhong Zhou, Jialing Wu, Bin Liu, Kun Wang, Ou Jin, Xiaohong Wang, Jie Qin, Lijun Wu, Dongbao Zhao, Dongyi He, Shanzhi He, Wenhui Huang, Shanhui Ye, Huiqiong Zhou, Jinyu Wu, Yongfu Wang, Shengyun Liu, Zhenbin Li, Zhiming Tan, Chiduo Xu, Youlian Wang, Donghui Zheng, Feng Zhan, Changsong Lin, Ya Wen, Jiayun Wu, Shenghui Wen, Zetao Liao, Yan Shen, Kehu Yang, and Jieruo Gu. A guideline on biomarkers in the diagnosis and evaluation in axial spondyloarthritis. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1394148, doi:10.3389/fimmu.2024.1394148. This article has 4 citations and is from a peer-reviewed journal.

8. (baraliakos2024efficacyandsafety pages 1-2): Xenofon Baraliakos, Désirée van der Heijde, Joachim Sieper, Robert Davies Inman, Hideto Kameda, Walter Peter Maksymowych, Ivan Lagunes-Galindo, Xianwei Bu, Peter Wung, Koji Kato, Anna Shmagel, and Atul Deodhar. Efficacy and safety of upadacitinib in patients with active ankylosing spondylitis refractory to biologic therapy: 2-year clinical and radiographic results from the open-label extension of the select-axis 2 study. Arthritis Research & Therapy, Nov 2024. URL: https://doi.org/10.1186/s13075-024-03412-8, doi:10.1186/s13075-024-03412-8. This article has 23 citations and is from a domain leading peer-reviewed journal.

9. (baraliakos2024bimekizumabtreatmentin pages 5-6): Xenofon Baraliakos, Atul Deodhar, Désirée van der Heijde, Marina Magrey, Walter P Maksymowych, Tetsuya Tomita, Huji Xu, Ute Massow, Carmen Fleurinck, Alicia M Ellis, Thomas Vaux, Julie Shepherd-Smith, Alexander Marten, and Lianne S Gensler. Bimekizumab treatment in patients with active axial spondyloarthritis: 52-week efficacy and safety from the randomised parallel phase 3 be mobile 1 and be mobile 2 studies. Annals of the Rheumatic Diseases, 83:1-15, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224803, doi:10.1136/ard-2023-224803. This article has 68 citations and is from a highest quality peer-reviewed journal.

10. (baraliakos2024bimekizumabtreatmentin pages 9-10): Xenofon Baraliakos, Atul Deodhar, Désirée van der Heijde, Marina Magrey, Walter P Maksymowych, Tetsuya Tomita, Huji Xu, Ute Massow, Carmen Fleurinck, Alicia M Ellis, Thomas Vaux, Julie Shepherd-Smith, Alexander Marten, and Lianne S Gensler. Bimekizumab treatment in patients with active axial spondyloarthritis: 52-week efficacy and safety from the randomised parallel phase 3 be mobile 1 and be mobile 2 studies. Annals of the Rheumatic Diseases, 83:1-15, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224803, doi:10.1136/ard-2023-224803. This article has 68 citations and is from a highest quality peer-reviewed journal.

11. (baraliakos2024bimekizumabtreatmentin pages 1-2): Xenofon Baraliakos, Atul Deodhar, Désirée van der Heijde, Marina Magrey, Walter P Maksymowych, Tetsuya Tomita, Huji Xu, Ute Massow, Carmen Fleurinck, Alicia M Ellis, Thomas Vaux, Julie Shepherd-Smith, Alexander Marten, and Lianne S Gensler. Bimekizumab treatment in patients with active axial spondyloarthritis: 52-week efficacy and safety from the randomised parallel phase 3 be mobile 1 and be mobile 2 studies. Annals of the Rheumatic Diseases, 83:1-15, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224803, doi:10.1136/ard-2023-224803. This article has 68 citations and is from a highest quality peer-reviewed journal.

12. (nam2024epidemiologictrendsand pages 4-5): Seoung Wan Nam, Jihye Lim, Dae Jin Park, Jun Young Lee, Jae Hyun Jung, and Dae Ryong Kang. Epidemiologic trends and socioeconomic disparities of ankylosing spondylitis in south korea: a nationwide population-based study, 2010–2021. Yonsei Medical Journal, 65:761-769, Sep 2024. URL: https://doi.org/10.3349/ymj.2024.0041, doi:10.3349/ymj.2024.0041. This article has 5 citations and is from a peer-reviewed journal.

13. (bilski2024environmentalandgenetic pages 6-8): Rafał Bilski, Piotr Kamiński, Daria Kupczyk, Sławomir Jeka, Jędrzej Baszyński, Halina Tkaczenko, and Natalia Kurhaluk. Environmental and genetic determinants of ankylosing spondylitis. International Journal of Molecular Sciences, 25:7814, Jul 2024. URL: https://doi.org/10.3390/ijms25147814, doi:10.3390/ijms25147814. This article has 37 citations.

14. (bilski2024environmentalandgenetic pages 25-26): Rafał Bilski, Piotr Kamiński, Daria Kupczyk, Sławomir Jeka, Jędrzej Baszyński, Halina Tkaczenko, and Natalia Kurhaluk. Environmental and genetic determinants of ankylosing spondylitis. International Journal of Molecular Sciences, 25:7814, Jul 2024. URL: https://doi.org/10.3390/ijms25147814, doi:10.3390/ijms25147814. This article has 37 citations.

15. (bilski2024environmentalandgenetic pages 11-12): Rafał Bilski, Piotr Kamiński, Daria Kupczyk, Sławomir Jeka, Jędrzej Baszyński, Halina Tkaczenko, and Natalia Kurhaluk. Environmental and genetic determinants of ankylosing spondylitis. International Journal of Molecular Sciences, 25:7814, Jul 2024. URL: https://doi.org/10.3390/ijms25147814, doi:10.3390/ijms25147814. This article has 37 citations.

16. (bilski2024environmentalandgenetic pages 12-14): Rafał Bilski, Piotr Kamiński, Daria Kupczyk, Sławomir Jeka, Jędrzej Baszyński, Halina Tkaczenko, and Natalia Kurhaluk. Environmental and genetic determinants of ankylosing spondylitis. International Journal of Molecular Sciences, 25:7814, Jul 2024. URL: https://doi.org/10.3390/ijms25147814, doi:10.3390/ijms25147814. This article has 37 citations.

17. (pasaran2024anactualinsight pages 10-11): Emilia-Daniela Păsăran, Andreea Elena Diaconu, Corina Oancea, Andra-Rodica Bălănescu, Sorina Maria Aurelian, and Corina Homentcovschi. An actual insight into the pathogenic pathways of ankylosing spondylitis. Current Issues in Molecular Biology, 46:12800-12812, Nov 2024. URL: https://doi.org/10.3390/cimb46110762, doi:10.3390/cimb46110762. This article has 11 citations.

18. (baraliakos2024efficacyandsafety pages 7-10): Xenofon Baraliakos, Désirée van der Heijde, Joachim Sieper, Robert Davies Inman, Hideto Kameda, Walter Peter Maksymowych, Ivan Lagunes-Galindo, Xianwei Bu, Peter Wung, Koji Kato, Anna Shmagel, and Atul Deodhar. Efficacy and safety of upadacitinib in patients with active ankylosing spondylitis refractory to biologic therapy: 2-year clinical and radiographic results from the open-label extension of the select-axis 2 study. Arthritis Research & Therapy, Nov 2024. URL: https://doi.org/10.1186/s13075-024-03412-8, doi:10.1186/s13075-024-03412-8. This article has 23 citations and is from a domain leading peer-reviewed journal.

19. (zimba2024diagnosismonitoringand pages 2-3): Olena Zimba, Burhan Fatih Kocyigit, and Mariusz Korkosz. Diagnosis, monitoring, and management of axial spondyloarthritis. Rheumatology International, 44:1395-1407, May 2024. URL: https://doi.org/10.1007/s00296-024-05615-3, doi:10.1007/s00296-024-05615-3. This article has 34 citations and is from a peer-reviewed journal.

20. (barahonacorrea2024prevalenceofaxial pages 1-2): Julián E. Barahona-Correa, Nancy M. Herrera-Leaño, Santiago Bernal-Macías, and Daniel G. Fernández-Ávila. Prevalence of axial spondyloarthritis in colombia: data from the national health registry 2017–2021. Clinical Rheumatology, 43:49-57, Nov 2024. URL: https://doi.org/10.1007/s10067-023-06799-y, doi:10.1007/s10067-023-06799-y. This article has 7 citations and is from a peer-reviewed journal.

21. (barahonacorrea2024prevalenceofaxial pages 2-5): Julián E. Barahona-Correa, Nancy M. Herrera-Leaño, Santiago Bernal-Macías, and Daniel G. Fernández-Ávila. Prevalence of axial spondyloarthritis in colombia: data from the national health registry 2017–2021. Clinical Rheumatology, 43:49-57, Nov 2024. URL: https://doi.org/10.1007/s10067-023-06799-y, doi:10.1007/s10067-023-06799-y. This article has 7 citations and is from a peer-reviewed journal.

22. (zimba2024diagnosismonitoringand pages 8-9): Olena Zimba, Burhan Fatih Kocyigit, and Mariusz Korkosz. Diagnosis, monitoring, and management of axial spondyloarthritis. Rheumatology International, 44:1395-1407, May 2024. URL: https://doi.org/10.1007/s00296-024-05615-3, doi:10.1007/s00296-024-05615-3. This article has 34 citations and is from a peer-reviewed journal.

23. (diekhoff2024clinicalinformationon pages 2-2): Torsten Diekhoff, Chiara Giraudo, Pedro M Machado, Michael Mallinson, Iris Eshed, Hildrun Haibel, Kay Geert Hermann, Manouk de Hooge, Lennart Jans, Anne Grethe Jurik, Robert GW Lambert, Walter Maksymowych, Helena Marzo-Ortega, Victoria Navarro-Compán, Mikkel Østergaard, Susanne Juhl Pedersen, Monique Reijnierse, Martin Rudwaleit, Fernando A Sommerfleck, Ulrich Weber, Xenofon Baraliakos, and Denis Poddubnyy. Clinical information on imaging referrals for suspected or known axial spondyloarthritis: recommendations from the assessment of spondyloarthritis international society (asas). Annals of the Rheumatic Diseases, 83:1636-1643, Dec 2024. URL: https://doi.org/10.1136/ard-2024-226280, doi:10.1136/ard-2024-226280. This article has 17 citations and is from a highest quality peer-reviewed journal.

24. (diekhoff2024clinicalinformationon pages 3-4): Torsten Diekhoff, Chiara Giraudo, Pedro M Machado, Michael Mallinson, Iris Eshed, Hildrun Haibel, Kay Geert Hermann, Manouk de Hooge, Lennart Jans, Anne Grethe Jurik, Robert GW Lambert, Walter Maksymowych, Helena Marzo-Ortega, Victoria Navarro-Compán, Mikkel Østergaard, Susanne Juhl Pedersen, Monique Reijnierse, Martin Rudwaleit, Fernando A Sommerfleck, Ulrich Weber, Xenofon Baraliakos, and Denis Poddubnyy. Clinical information on imaging referrals for suspected or known axial spondyloarthritis: recommendations from the assessment of spondyloarthritis international society (asas). Annals of the Rheumatic Diseases, 83:1636-1643, Dec 2024. URL: https://doi.org/10.1136/ard-2024-226280, doi:10.1136/ard-2024-226280. This article has 17 citations and is from a highest quality peer-reviewed journal.

25. (diekhoff2024clinicalinformationon pages 4-4): Torsten Diekhoff, Chiara Giraudo, Pedro M Machado, Michael Mallinson, Iris Eshed, Hildrun Haibel, Kay Geert Hermann, Manouk de Hooge, Lennart Jans, Anne Grethe Jurik, Robert GW Lambert, Walter Maksymowych, Helena Marzo-Ortega, Victoria Navarro-Compán, Mikkel Østergaard, Susanne Juhl Pedersen, Monique Reijnierse, Martin Rudwaleit, Fernando A Sommerfleck, Ulrich Weber, Xenofon Baraliakos, and Denis Poddubnyy. Clinical information on imaging referrals for suspected or known axial spondyloarthritis: recommendations from the assessment of spondyloarthritis international society (asas). Annals of the Rheumatic Diseases, 83:1636-1643, Dec 2024. URL: https://doi.org/10.1136/ard-2024-226280, doi:10.1136/ard-2024-226280. This article has 17 citations and is from a highest quality peer-reviewed journal.

26. (baraliakos2024efficacyandsafety pages 4-7): Xenofon Baraliakos, Désirée van der Heijde, Joachim Sieper, Robert Davies Inman, Hideto Kameda, Walter Peter Maksymowych, Ivan Lagunes-Galindo, Xianwei Bu, Peter Wung, Koji Kato, Anna Shmagel, and Atul Deodhar. Efficacy and safety of upadacitinib in patients with active ankylosing spondylitis refractory to biologic therapy: 2-year clinical and radiographic results from the open-label extension of the select-axis 2 study. Arthritis Research & Therapy, Nov 2024. URL: https://doi.org/10.1186/s13075-024-03412-8, doi:10.1186/s13075-024-03412-8. This article has 23 citations and is from a domain leading peer-reviewed journal.

27. (NCT06905288 chunk 2):  Real-world Study on Secukinumab Effectiveness in Biologic-naïve Ankylosing Spondylitis (AS) Patients in Korea.. Novartis Pharmaceuticals. 2025. ClinicalTrials.gov Identifier: NCT06905288

28. (diekhoff2024clinicalinformationon pages 1-1): Torsten Diekhoff, Chiara Giraudo, Pedro M Machado, Michael Mallinson, Iris Eshed, Hildrun Haibel, Kay Geert Hermann, Manouk de Hooge, Lennart Jans, Anne Grethe Jurik, Robert GW Lambert, Walter Maksymowych, Helena Marzo-Ortega, Victoria Navarro-Compán, Mikkel Østergaard, Susanne Juhl Pedersen, Monique Reijnierse, Martin Rudwaleit, Fernando A Sommerfleck, Ulrich Weber, Xenofon Baraliakos, and Denis Poddubnyy. Clinical information on imaging referrals for suspected or known axial spondyloarthritis: recommendations from the assessment of spondyloarthritis international society (asas). Annals of the Rheumatic Diseases, 83:1636-1643, Dec 2024. URL: https://doi.org/10.1136/ard-2024-226280, doi:10.1136/ard-2024-226280. This article has 17 citations and is from a highest quality peer-reviewed journal.

29. (nam2024epidemiologictrendsand pages 1-2): Seoung Wan Nam, Jihye Lim, Dae Jin Park, Jun Young Lee, Jae Hyun Jung, and Dae Ryong Kang. Epidemiologic trends and socioeconomic disparities of ankylosing spondylitis in south korea: a nationwide population-based study, 2010–2021. Yonsei Medical Journal, 65:761-769, Sep 2024. URL: https://doi.org/10.3349/ymj.2024.0041, doi:10.3349/ymj.2024.0041. This article has 5 citations and is from a peer-reviewed journal.

30. (barahonacorrea2024prevalenceofaxial pages 5-7): Julián E. Barahona-Correa, Nancy M. Herrera-Leaño, Santiago Bernal-Macías, and Daniel G. Fernández-Ávila. Prevalence of axial spondyloarthritis in colombia: data from the national health registry 2017–2021. Clinical Rheumatology, 43:49-57, Nov 2024. URL: https://doi.org/10.1007/s10067-023-06799-y, doi:10.1007/s10067-023-06799-y. This article has 7 citations and is from a peer-reviewed journal.

31. (baraliakos2023efficacyandsafety pages 1-2): Xenofon Baraliakos, Désirée van der Heijde, Joachim Sieper, Robert D. Inman, Hideto Kameda, Yihan Li, Xianwei Bu, Anna Shmagel, Peter Wung, In-Ho Song, and Atul Deodhar. Efficacy and safety of upadacitinib in patients with ankylosing spondylitis refractory to biologic therapy: 1-year results from the open-label extension of a phase iii study. Arthritis Research & Therapy, Sep 2023. URL: https://doi.org/10.1186/s13075-023-03128-1, doi:10.1186/s13075-023-03128-1. This article has 33 citations and is from a domain leading peer-reviewed journal.

32. (baraliakos2024efficacyandsafety pages 10-11): Xenofon Baraliakos, Désirée van der Heijde, Joachim Sieper, Robert Davies Inman, Hideto Kameda, Walter Peter Maksymowych, Ivan Lagunes-Galindo, Xianwei Bu, Peter Wung, Koji Kato, Anna Shmagel, and Atul Deodhar. Efficacy and safety of upadacitinib in patients with active ankylosing spondylitis refractory to biologic therapy: 2-year clinical and radiographic results from the open-label extension of the select-axis 2 study. Arthritis Research & Therapy, Nov 2024. URL: https://doi.org/10.1186/s13075-024-03412-8, doi:10.1186/s13075-024-03412-8. This article has 23 citations and is from a domain leading peer-reviewed journal.

33. (baraliakos2024bimekizumabtreatmentin pages 2-3): Xenofon Baraliakos, Atul Deodhar, Désirée van der Heijde, Marina Magrey, Walter P Maksymowych, Tetsuya Tomita, Huji Xu, Ute Massow, Carmen Fleurinck, Alicia M Ellis, Thomas Vaux, Julie Shepherd-Smith, Alexander Marten, and Lianne S Gensler. Bimekizumab treatment in patients with active axial spondyloarthritis: 52-week efficacy and safety from the randomised parallel phase 3 be mobile 1 and be mobile 2 studies. Annals of the Rheumatic Diseases, 83:1-15, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224803, doi:10.1136/ard-2023-224803. This article has 68 citations and is from a highest quality peer-reviewed journal.

34. (baraliakos2024bimekizumabtreatmentin pages 6-7): Xenofon Baraliakos, Atul Deodhar, Désirée van der Heijde, Marina Magrey, Walter P Maksymowych, Tetsuya Tomita, Huji Xu, Ute Massow, Carmen Fleurinck, Alicia M Ellis, Thomas Vaux, Julie Shepherd-Smith, Alexander Marten, and Lianne S Gensler. Bimekizumab treatment in patients with active axial spondyloarthritis: 52-week efficacy and safety from the randomised parallel phase 3 be mobile 1 and be mobile 2 studies. Annals of the Rheumatic Diseases, 83:1-15, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224803, doi:10.1136/ard-2023-224803. This article has 68 citations and is from a highest quality peer-reviewed journal.