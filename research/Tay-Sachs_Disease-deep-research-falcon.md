---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:43.912339'
end_time: '2026-04-25T22:35:19.387623'
duration_seconds: 1175.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tay-Sachs Disease
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tay-Sachs Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Tay-Sachs Disease** covering all of the
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
- **Disease Name:** Tay-Sachs Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Tay-Sachs Disease** covering all of the
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


# Tay–Sachs Disease (HEXA-related GM2 gangliosidosis variant B): Disease Characteristics Research Report

## Target Disease
- **Disease name:** Tay–Sachs disease (TSD) (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2)
- **Category:** Genetic; lysosomal storage disorder (GM2 gangliosidosis) (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2)

## 1. Disease information

### Concise overview (current understanding)
Tay–Sachs disease is an **autosomal recessive** GM2 gangliosidosis caused by deficiency of lysosomal **β-hexosaminidase A (HexA)**, leading to progressive **GM2 ganglioside accumulation in neurons** and neurodegeneration (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2). Tay–Sachs is classically subdivided into **infantile, juvenile, and late-/adult-onset** clinical forms that correlate with residual HexA activity (gonzalezsanchez2025advancesindiagnosis pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 2-4).

**Direct abstract quotes (examples)**
- From a fetal-brain transcriptomics study (Feb 2023): the authors state they identified “**dramatic changes in the transcriptome, suggesting a perturbation of normal development**” and that fetal transcriptomes were “**perturbed by 17 week’s gestation, suggesting abnormal neurodevelopment**” (han2023geneexpressionchanges pages 1-3).

### Key identifiers, synonyms, and alternative names
| Identifier system | ID/code | Preferred label | Notes/source |
|---|---|---|---|
| OMIM (disease) | 272800 | Tay–Sachs disease | Retrieved review explicitly lists OMIM 272800 for TSD; described as a rare autosomal recessive GM2 gangliosidosis caused by HEXA-related HexA deficiency (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2) |
| OMIM (gene) | 606869 | HEXA | Retrieved primary study gives HEXA (MIM# 606869) as the causal gene encoding the alpha subunit of β-hexosaminidase A (ibrahim2023biochemicalandmutational pages 1-2) |
| Orphanet | ORPHA:845 | Tay–Sachs disease | Retrieved review explicitly lists ORPHANET/Orphanet ORPHA845 for TSD (gonzalezsanchez2025advancesindiagnosis pages 1-2) |
| MeSH | not found in retrieved sources | Tay–Sachs disease | MeSH identifier was not present in the retrieved evidence set used here; disease overview and synonyms supported by retrieved literature (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2) |
| ICD-10 | not found in retrieved sources | Tay–Sachs disease | ICD-10 code not present in the retrieved evidence set used here (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2) |
| ICD-11 | not found in retrieved sources | Tay–Sachs disease | ICD-11 code not present in the retrieved evidence set used here (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2) |
| MONDO | not found in retrieved sources | Tay–Sachs disease | MONDO identifier was not present in the retrieved evidence set used here (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2) |
| Disease class / classification | GM2 gangliosidosis variant B | Tay–Sachs disease | Retrieved sources state TSD is also known as GM2 gangliosidosis variant B and belongs to the GM2 gangliosidoses; inheritance is autosomal recessive (ibrahim2023biochemicalandmutational pages 1-2, picache2022therapeuticstrategiesfor pages 1-2) |
| Synonym | — | Tay–Sachs disease | Common preferred disease name in all retrieved sources (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2, picache2022therapeuticstrategiesfor pages 1-2) |
| Synonym | — | GM2 gangliosidosis variant B | Explicit synonym in retrieved primary literature (ibrahim2023biochemicalandmutational pages 1-2) |
| Synonym | — | Hexosaminidase A deficiency | Functional disease descriptor supported by retrieved sources describing HexA deficiency as the defining biochemical defect (gonzalezsanchez2025advancesindiagnosis pages 1-2, picache2022therapeuticstrategiesfor pages 1-2) |


*Table: This table summarizes key retrieved identifiers and synonyms for Tay–Sachs disease, including disease and gene OMIM entries, Orphanet ID, classification, and supported alternative names. It also flags identifier systems not found in the retrieved evidence so the final report can clearly distinguish confirmed versus missing mappings.*

- **Synonyms/related labels used in the literature:** GM2 gangliosidosis variant B; hexosaminidase A deficiency (ibrahim2023biochemicalandmutational pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 1-2).
- **MONDO ID:** not found in the retrieved evidence set used for this report (artifact-00).

### Evidence provenance
Most content here is derived from **aggregated disease-level resources/reviews** plus **primary cohort studies** and **clinical trial registry records**. Examples include a 2023 infantile Tay–Sachs cohort study in Egypt (Orphanet Journal of Rare Diseases) (ibrahim2023biochemicalandmutational pages 1-2), fetal brain transcriptomics (Journal of Inherited Metabolic Disease) (han2023geneexpressionchanges pages 1-3), and ClinicalTrials.gov records (NCT04798235 chunk 1).

## 2. Etiology

### Disease causal factors
- **Primary cause:** biallelic pathogenic variants in **HEXA** (OMIM 606869) resulting in deficient **HexA** enzyme activity and **lysosomal GM2 accumulation** (ibrahim2023biochemicalandmutational pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 5-7).
- Tay–Sachs is one of the **GM2 gangliosidoses**, which also include Sandhoff disease (HEXB) and AB-variant disease (GM2A) (gonzalezsanchez2025advancesindiagnosis pages 7-9, ashiri2023usinganengineered pages 16-23).

### Risk factors
- **Genetic risk:** carrier status for pathogenic **HEXA** variants; risk is elevated in some founder populations. A 2023 cohort paper summarizes carrier frequency being substantially higher in Ashkenazi Jewish populations (reported ~1/25) compared with ~1/250–300 in many other populations (ibrahim2023biochemicalandmutational pages 1-2).
- **Consanguinity:** in a 2023 Egyptian infantile cohort, most affected children were born to consanguineous marriages (10/13) (ibrahim2023biochemicalandmutational pages 1-2).

### Protective factors
No validated **genetic** or **environmental** protective factors were identified in the retrieved evidence set. A biologic “protective” concept is that **higher residual HexA activity** is associated with later onset and milder disease (i.e., acts as a functional modifier), but this is not a protective variant per se (gonzalezsanchez2025advancesindiagnosis pages 2-4).

### Gene–environment interactions
No specific gene–environment interactions were identified in the retrieved evidence set; Tay–Sachs is best characterized as a monogenic disorder with phenotype strongly related to enzyme activity and variant class (gonzalezsanchez2025advancesindiagnosis pages 2-4).

## 3. Phenotypes

### Phenotype spectrum and HPO mapping
| Subtype (with typical onset) | Key clinical features (plain language) | Suggested HPO terms (IDs and labels) | Natural history/progression (including survival estimates) | Frequency data (if available) | Key sources |
|---|---|---|---|---|---|
| Infantile Tay–Sachs disease (typically 3–6 months) | Initially normal infant, then irritability, mild motor weakness, exaggerated startle/hyperacusis, inability to sit, developmental regression, cherry-red macular spot, visual loss/blindness, feeding difficulty/dysphagia, seizures, later spasticity, dyskinesia, macrocephaly, cognitive decline, vegetative state | HP:0001257 Spasticity; HP:0002376 Developmental regression; HP:0001344 Hyperreflexia; HP:0002072 Chorea/dyskinesia-related abnormal involuntary movements; HP:0001250 Seizure; HP:0000518 Cataract not appropriate / use HP:0010729 Cherry red spot of the macula; HP:0000407 Sensorineural hearing impairment / hyperacusis feature not directly matched here; HP:0002015 Dysphagia; HP:0000256 Macrocephaly; HP:0001252 Hypotonia | Progressive neurodegeneration begins in the first year; cherry-red spot is typically present by ~6 months; vision loss develops by 12–18 months and many patients are blind by ~30 months; rapid worsening between ~8–10 months; tonic–myoclonic seizures often by ~12 months; later refractory seizures, dysphagia, decerebrate posturing, vegetative state; death usually at 2–5 years despite supportive care | “More than two-thirds” require multiple anticonvulsants for seizure control; in one Egyptian cohort all 13/13 biochemically confirmed cases had infantile disease; Ashkenazi carrier frequency reported ~1/25 vs ~1/250–300 in many other populations | (gonzalezsanchez2025advancesindiagnosis pages 9-11, ibrahim2023biochemicalandmutational pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 2-4) |
| Juvenile / subacute Tay–Sachs disease (typically 2–10 years; some sources 3–5 years) | Speech difficulty, clumsiness, gait problems, limb weakness, progressive spasticity, seizures, optic atrophy/vision decline; often more variable than infantile disease and may lack an early cherry-red spot | HP:0002463 Speech impairment; HP:0002317 Unsteady gait; HP:0003324 Muscle weakness; HP:0001257 Spasticity; HP:0001250 Seizure; HP:0000648 Optic atrophy; HP:0002376 Developmental regression | Intermediate course between infantile and adult forms; gradual neurologic deterioration over years with loss of motor function and increasing dependency; death commonly in adolescence or by mid-adolescence | Specific phenotype frequencies were not provided in the retrieved juvenile-focused excerpts; review data cited elsewhere note limb weakness and ataxic gait as common, but no robust juvenile percentage table was available in retrieved primary evidence | (gonzalezsanchez2025advancesindiagnosis pages 2-4, ibrahim2023biochemicalandmutational pages 1-2, sheth2018identificationofdeletionduplication pages 1-2) |
| Late-onset / adult Tay–Sachs disease (adolescence to adulthood; often 20s–30s) | Slowly progressive muscle weakness, clumsy or ataxic gait, tremor, dysarthria/stuttering or other distinct speech changes, falls, difficulty climbing stairs, fatigue, cerebellar signs, triceps/quadriceps wasting, psychiatric symptoms including psychosis/delusions/impulsivity, mild cognitive or subcortical deficits | HP:0001324 Muscle weakness; HP:0002066 Gait ataxia; HP:0001337 Tremor; HP:0001260 Dysarthria; HP:0002521 Cerebellar atrophy; HP:0007018 Falls; HP:0012378 Fatigue; HP:0000709 Psychosis; HP:0000738 Hallucinations/delusions-related psychiatric disturbance; HP:0002354 Memory impairment | Chronic, slowly progressive course with prolonged survival; diagnostic delay is common; patients may first present to neuromuscular, movement-disorder, or psychiatric services; loss of ambulation may occur later and lifespan is variable | Patient/caregiver burden study: muscle weakness 19/20 (95%), difficulty walking 19/20 (95%), falling 17/20 (85%), climbing stairs 16/20 (80%), “clumsy” gait 12/20 (60%), fatigue 10/20 (50%), coughing fits 5/20 (25%), GI issues 4/20 (20%); psychiatric symptoms may be the initial manifestation in up to half of patients | (lyn2020patientandcaregiver pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 4-5, barritt2017lateonsettay–sachsdisease pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 2-4) |


*Table: This table summarizes Tay–Sachs disease manifestations across infantile, juvenile, and late-onset forms, linking clinical features to suggested HPO terms, natural history, and available frequency data. It is useful for phenotype curation, diagnostic support, and subtype-specific knowledge base entry development.*

### Quality-of-life impact (late-onset disease)
A qualitative study of late-onset GM2 gangliosidosis (including late-onset Tay–Sachs) quantified commonly reported symptoms and functional impacts. Frequently reported items included **muscle weakness (95%)**, **difficulty walking (95%)**, **falling (85%)**, and **difficulty climbing stairs (80%)**, emphasizing substantial impairment of mobility/independence and downstream psychosocial burden (lyn2020patientandcaregiver pages 1-2).

## 4. Genetic / molecular information

### Causal gene(s)
- **HEXA** is the causal gene for Tay–Sachs disease; HEXA encodes the α-subunit of HexA (ibrahim2023biochemicalandmutational pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 7-9).

### Pathogenic variants (examples and variant types)
- A 2023 infantile cohort study (Egypt; publication date Mar 2023; URL https://doi.org/10.1186/s13023-023-02637-1) reported multiple **novel likely pathogenic variants** and recurrent exon 13 variants, including missense and frameshift changes; mean HexA activity in affected children was severely reduced (ibrahim2023biochemicalandmutational pages 1-2).
- Exon-level **deletions/duplications** can cause disease and may be missed by exon sequencing alone; MLPA identified exon 1 deletions/duplications and exon 2–3 deletions in enzymatically confirmed cases (sheth2018identificationofdeletionduplication pages 2-3, sheth2018identificationofdeletionduplication pages 1-2).
- Late-onset presentations can involve combinations such as frameshift plus the common late-onset variant **c.805G>A (p.Gly269Ser)** in HEXA (barritt2017lateonsettay–sachsdisease pages 1-2).

### Functional consequences
Pathogenic HEXA variants generally produce **loss of function** by disrupting protein folding, heterodimer assembly, lysosomal trafficking, or catalytic function, ultimately preventing HexA-mediated hydrolysis of GM2 (ashiri2023usinganengineered pages 23-28, gonzalezsanchez2025advancesindiagnosis pages 7-9).

### Modifier genes / epigenetics / chromosomal abnormalities
No robust modifier genes, epigenetic drivers, or chromosomal abnormalities specific to Tay–Sachs were identified in the retrieved evidence set.

## 5. Environmental information
Tay–Sachs is not established as an environmentally triggered disorder; no non-genetic causal environmental factors were identified in the retrieved evidence set.

## 6. Mechanism / pathophysiology

### Core biochemical defect and causal chain
1. **HEXA loss-of-function** causes deficient lysosomal **HexA** activity (gonzalezsanchez2025advancesindiagnosis pages 5-7, gonzalezsanchez2025advancesindiagnosis pages 7-9).
2. HexA “**specifically hydrolyzes the N-acetylgalactosamine residue in GM2 ganglioside**,” and deficiency leads to “**accumulation of GM2 gangliosides within lysosomes**” (gonzalezsanchez2025advancesindiagnosis pages 7-9).
3. GM2 accumulation contributes to lysosomal dysfunction (including lysosomal disruption) and neurodegeneration, with neuronal loss and gliosis (gonzalezsanchez2025advancesindiagnosis pages 7-9, gonzalezsanchez2025advancesindiagnosis pages 5-7).
4. Downstream mechanisms include **ER stress** and **apoptosis** (neuron death) as well as **neuroinflammation** characterized by microglial activation and astrogliosis (gonzalezsanchez2025advancesindiagnosis pages 7-9, gonzalezsanchez2025advancesindiagnosis pages 9-11).

### Neuroinflammation and glial involvement
A 2025 review states “**astrogliosis has been identified as a critical component of GM2 gangliosidosis pathophysiology**” and highlights that “**astrocyte-microglia crosstalk is essential for amplifying neuroinflammatory responses**” (gonzalezsanchez2025advancesindiagnosis pages 9-11). Candidate CSF inflammatory biomarkers for infantile disease include ENA-78, MCP-1, MIP-1α, MIP-1β, and TNFR2 (gonzalezsanchez2025advancesindiagnosis pages 9-11).

### Myelin/oligodendrocyte involvement and biomarker data (large animal model)
In a sheep natural-history model (publication date Sep 2021; URL https://doi.org/10.1016/j.ymgme.2021.08.009), disease severity tracked with **CSF GM2**, MRI/MRS markers, and neuropathology including early oligodendrocyte loss and demyelination signatures (story2021naturalhistoryof pages 5-7). Reported MRS patterns included increased myoinositol (gliosis), increased taurine, increased choline-related markers (demyelination), and decreased NAA (neuronal/axonal integrity) (story2021naturalhistoryof pages 5-7).

### Developmental stage mechanisms (human fetal brain)
A 2023 RNA-seq study of human fetal Tay–Sachs brain found transcriptomes “**perturbed by 17 week’s gestation**” and a “**shift in the expression of the sphingolipid metabolic pathway away from production of the HEXA substrate, GM2 ganglioside**,” implying compensatory remodeling and that developmental perturbations may precede overt neurodegeneration (han2023geneexpressionchanges pages 1-3).

### Suggested ontology terms
- **GO (biological process) suggestions:** ganglioside catabolic process; sphingolipid metabolic process; lysosomal organization; response to endoplasmic reticulum stress; apoptotic process; microglial activation; astrocyte activation; neuroinflammatory response; myelination (supported conceptually by mechanistic and pathology evidence) (gonzalezsanchez2025advancesindiagnosis pages 7-9, gonzalezsanchez2025advancesindiagnosis pages 9-11, story2021naturalhistoryof pages 5-7).
- **CL (cell type) suggestions:** microglia; astrocyte; oligodendrocyte; radial glial cell; neuron (including cerebellar Purkinje neuron) (gonzalezsanchez2025advancesindiagnosis pages 7-9, gonzalezsanchez2025advancesindiagnosis pages 9-11, story2021naturalhistoryof pages 5-7).

## 7. Anatomical structures affected

### Organ/system level
- Primary system: **central nervous system** (progressive neurodegeneration) (gonzalezsanchez2025advancesindiagnosis pages 5-7, gonzalezsanchez2025advancesindiagnosis pages 2-4).
- Neuroanatomical involvement noted on imaging/pathology includes thalamus and cerebral atrophy patterns in clinical descriptions and animal models (gonzalezsanchez2025advancesindiagnosis pages 5-7, story2021naturalhistoryof pages 5-7).

### Tissue/cell level
- Neuronal lysosomal storage with gliosis (gonzalezsanchez2025advancesindiagnosis pages 5-7, gonzalezsanchez2025advancesindiagnosis pages 9-11).
- Oligodendrocyte/myelin abnormalities suggested by sheep natural history (story2021naturalhistoryof pages 5-7).

### Subcellular level
- **Lysosome** is the key compartment for substrate accumulation (gonzalezsanchez2025advancesindiagnosis pages 5-7, gonzalezsanchez2025advancesindiagnosis pages 7-9).

### Suggested anatomical ontology terms
- **UBERON suggestions:** brain; thalamus; cerebellum; cerebral cortex; white matter; spinal cord (supported by sampling sites and pathology descriptions across sources) (story2021naturalhistoryof pages 5-7, han2023geneexpressionchanges pages 1-3).

## 8. Temporal development

- **Infantile onset:** typically 3–6 months with early sensory hypersensitivity/startle, regression, and rapid progression; seizures often develop by ~12 months in one synthesis (gonzalezsanchez2025advancesindiagnosis pages 9-11).
- **Progression:** infantile disease progresses to severe disability, vegetative state, and death commonly in early childhood (2–5 years across sources) (ibrahim2023biochemicalandmutational pages 1-2, gonzalezsanchez2025advancesindiagnosis pages 2-4).
- **Late-onset:** chronic progression across years with variable lifespan and often long diagnostic delays; psychiatric symptoms may be initial in up to half of patients in one review (gonzalezsanchez2025advancesindiagnosis pages 4-5).

## 9. Inheritance and population

- **Inheritance pattern:** autosomal recessive (gonzalezsanchez2025advancesindiagnosis pages 1-2, ibrahim2023biochemicalandmutational pages 1-2).
- **Epidemiology (illustrative figures from recent secondary sources):** One review reports ~1 in 100,000 live births in the U.S. and carrier frequency ~1 in 250, with much higher incidence in Ashkenazi Jewish populations (~1 in 3,900 without screening; carrier ~1 in 29 in some studies) (gonzalezsanchez2025advancesindiagnosis pages 2-4). A 2023 cohort paper summarizes higher carrier frequency in Ashkenazi Jewish populations (~1 in 25) versus ~1/250–300 in many other populations (ibrahim2023biochemicalandmutational pages 1-2).

## 10. Diagnostics

| Test/approach | Specimen | What it measures | Interpretation pitfalls | Typical use case (diagnosis/carrier/prenatal) | Notes | Key sources |
|---|---|---|---|---|---|---|
| HexA/HexB enzyme activity assay using artificial substrates (e.g., MUG/MUGS with thermal differentiation) | Leukocytes, serum, cultured skin fibroblasts, chorionic villi, dried blood spots, other cells/tissues/biological fluids | Total hexosaminidase and HexA-specific activity; confirms biochemical deficiency | Pseudodeficiency alleles can lower **in vitro** activity on synthetic substrates without causing disease; carrier detection by enzyme assay alone can be unreliable | Primary diagnosis; confirmatory testing; prenatal when performed on fetal material | Gold-standard confirmatory specimens in retrieved sources are fibroblasts, chorionic villi, or leukocytes; infantile disease often shows very low/absent activity, juvenile higher residual activity (gonzalezsanchez2025advancesindiagnosis pages 4-5, ashiri2023usinganengineered pages 23-28, gonzalezsanchez2025advancesindiagnosis pages 2-4) | (gonzalezsanchez2025advancesindiagnosis pages 4-5, ashiri2023usinganengineered pages 23-28, gonzalezsanchez2025advancesindiagnosis pages 2-4) |
| Dried blood spot (DBS) HexA assay | Dried blood spots | Screening/initial biochemical detection of low HexA activity | Positive/abnormal DBS requires confirmatory enzyme and molecular testing; not sufficient alone for definitive molecular characterization | Early diagnosis; newborn/remote screening workflows; triage to confirmatory testing | Reported as practical standard-of-care style primary test in one study; can be paired with sequencing/WES follow-up (bibi2021taysachsdiseasetwo pages 5-8, gonzalezsanchez2025advancesindiagnosis pages 2-4) | (bibi2021taysachsdiseasetwo pages 5-8, gonzalezsanchez2025advancesindiagnosis pages 2-4) |
| Targeted HEXA variant analysis / common-variant panels | Blood or genomic DNA | Detects recurrent pathogenic alleles and selected adult-onset/pseudodeficiency alleles | Limited if patient carries rare/private variants or CNVs; founder-focused panels may miss non-founder mutations | Carrier screening; targeted diagnostic follow-up in high-risk populations | Retrieved review notes panels including common null alleles plus adult-onset p.Gly269Ser and pseudodeficiency alleles p.Arg247Trp / p.Arg249Trp (gonzalezsanchez2025advancesindiagnosis pages 4-5) | (gonzalezsanchez2025advancesindiagnosis pages 4-5) |
| Sanger sequencing of HEXA coding exons and splice junctions | Genomic DNA from blood | Single-nucleotide variants and small indels in coding/splice regions | Can miss deep intronic/regulatory variants and exon-level deletions/duplications; partial detection only in some cohorts | Diagnostic confirmation after low enzyme activity; family testing | In the Egyptian infantile cohort, bidirectional Sanger sequencing had ~62% detection (8/13), prompting recommendation for broader NGS/CNV-aware workup when unresolved (ibrahim2023biochemicalandmutational pages 1-2) | (ibrahim2023biochemicalandmutational pages 1-2) |
| Next-generation sequencing (targeted panels/WES; CNV-aware if possible) | Genomic DNA | Broad detection of HEXA variants, including rare/private pathogenic variants; may support broader differential diagnosis | Requires variant interpretation; may still miss some structural/regulatory defects if CNV calling is inadequate | Diagnosis of unresolved cases; family studies; carrier workup in diverse populations | Recommended when Sanger is negative or only one pathogenic allele is found; WES identified novel homozygous HEXA variants in Pakistani/Moroccan families (bibi2021taysachsdiseasetwo pages 5-8, ibrahim2023biochemicalandmutational pages 1-2) | (bibi2021taysachsdiseasetwo pages 5-8, ibrahim2023biochemicalandmutational pages 1-2) |
| MLPA (deletion/duplication analysis) | Genomic DNA from whole blood | Exon-level copy-number changes in HEXA | Not designed for SNVs/small indels; usually used after sequencing fails to identify both alleles | Diagnostic resolution of sequencing-inconclusive cases; family studies | Detected homozygous exon 2-3 deletions, exon 1 deletions with a missense variant, and exon 1 duplication with splice variant; specifically recommended when one/both alleles are missing by sequencing (sheth2018identificationofdeletionduplication pages 2-3, sheth2018identificationofdeletionduplication pages 1-2) | (sheth2018identificationofdeletionduplication pages 2-3, sheth2018identificationofdeletionduplication pages 1-2) |
| Prenatal enzyme testing on chorionic villi / chorionic villus sampling (CVS) | Chorionic villi (typically 10-12 weeks) | Fetal HexA activity and/or fetal genotype | Requires correct parental interpretation and awareness of pseudodeficiency alleles; invasive procedure | Prenatal diagnosis in at-risk pregnancies | Retrieved review explicitly identifies CVS as a prenatal option and chorionic villi as a gold-standard specimen type for enzyme testing (gonzalezsanchez2025advancesindiagnosis pages 4-5, gonzalezsanchez2025advancesindiagnosis pages 2-4) | (gonzalezsanchez2025advancesindiagnosis pages 4-5, gonzalezsanchez2025advancesindiagnosis pages 2-4) |
| Prenatal testing by amniocentesis | Amniotic fluid/fetal cells (typically 15-18 weeks) | Fetal genotype and/or biochemical testing depending laboratory workflow | Same interpretive issues as other prenatal tests; invasive procedure | Prenatal diagnosis in at-risk pregnancies | Retrieved review gives amniocentesis at 15-18 weeks as an option when parental carrier status/risk is established (gonzalezsanchez2025advancesindiagnosis pages 4-5) | (gonzalezsanchez2025advancesindiagnosis pages 4-5) |
| Carrier screening programs (premarital/preconception/community screening) | Blood/DBS/DNA depending program | Identifies heterozygous carriers to inform reproductive risk | Enzyme-based carrier screening can be confounded by pseudodeficiency; molecular confirmation improves specificity | Carrier screening; public health prevention | In Ashkenazi Jewish communities, premarital carrier screening was associated with an approximately 95% reduction in Tay-Sachs incidence in retrieved evidence; historical founder frequencies are much higher than general-population rates (gonzalezsanchez2025advancesindiagnosis pages 2-4, ashiri2023usinganengineered pages 23-28) | (gonzalezsanchez2025advancesindiagnosis pages 2-4, ashiri2023usinganengineered pages 23-28) |
| Integrated diagnostic workflow | Start with leukocytes/fibroblasts/DBS, then DNA-based testing | Combines biochemical confirmation with molecular definition of genotype | Overreliance on a single modality can miss carriers, pseudodeficiency, or CNVs | Best-practice diagnostic pathway | Practical pathway from retrieved evidence: low HexA activity -> sequencing -> del/dup analysis/NGS if unresolved; use prenatal testing when familial pathogenic variants are known (gonzalezsanchez2025advancesindiagnosis pages 4-5, ibrahim2023biochemicalandmutational pages 1-2, sheth2018identificationofdeletionduplication pages 2-3) | (gonzalezsanchez2025advancesindiagnosis pages 4-5, ibrahim2023biochemicalandmutational pages 1-2, sheth2018identificationofdeletionduplication pages 2-3) |


*Table: This table summarizes the main diagnostic and screening approaches for Tay-Sachs disease, including biochemical, molecular, prenatal, and carrier-screening methods. It highlights specimen types, what each test measures, common pitfalls such as pseudodeficiency alleles, and how these methods are used in real-world diagnostic pathways.*

### Real-world diagnostic implementation notes
- A practical approach in the retrieved evidence is biochemical confirmation (HexA activity) followed by genotyping and, if needed, del/dup analysis such as MLPA to detect exon-level CNVs (gonzalezsanchez2025advancesindiagnosis pages 4-5, sheth2018identificationofdeletionduplication pages 2-3).
- The first-in-human gene therapy case report highlights the clinical necessity for confirmed diagnosis and the use of CSF HexA activity as a pharmacodynamic readout in treated infants (flotte2022aavgenetherapy pages 1-6).

## 11. Outcome / prognosis

- **Infantile Tay–Sachs:** poor prognosis with death typically in early childhood despite supportive care; one review summarizes death usually by ~5 years (gonzalezsanchez2025advancesindiagnosis pages 2-4), and a 2023 cohort paper describes death at ~2–4 years for the classical infantile phenotype (ibrahim2023biochemicalandmutational pages 1-2).
- **Seizure burden:** one synthesis states “more than two-thirds” require multiple anticonvulsants for seizure control (gonzalezsanchez2025advancesindiagnosis pages 9-11).
- **Late-onset disease:** prolonged survival but high functional burden, with frequent falls and mobility limitations (lyn2020patientandcaregiver pages 1-2).

## 12. Treatment

| Modality | Example intervention | Mechanism/rationale | Evidence level (human/animal/in vitro) | Key quantitative results | Status/real-world use | ClinicalTrials.gov IDs if applicable | Key sources |
|---|---|---|---|---|---|---|---|
| In vivo gene therapy | AAVrh8-HEXA + AAVrh8-HEXB (expanded-access; AXO-AAV-GM2 platform) | Dual-vector replacement of both HexA subunits to restore CNS HexA activity; delivered intrathecally and/or intrathalamically because broad CNS distribution is required | Human clinical + supporting animal studies | In 2 infantile TSD patients, CSF HexA activity “nearly doubled from baseline and remained stable”; no vector-related AEs reported; one patient treated at 7 months showed MRI stabilization at 3 months but decline by 6 months; one older patient remained seizure-free at 4.5–5 years on same anticonvulsant regimen. Doses included 1×10^14 vg IT (75% cisterna magna, 25% thoracolumbar) and 4.2×10^13 vg combined thalamic+IT (flotte2022aavgenetherapy pages 1-6) | First-in-human proof-of-concept; not approved | Expanded access under IND 18225; follow-up study NCT06614569 | (flotte2022aavgenetherapy pages 1-6, gonzalezsanchez2025advancesindiagnosis pages 15-17) |
| Interventional clinical trial, gene therapy | AXO-AAV-GM2 dose-escalation study | Same dual-AAV gene replacement strategy for infantile GM2 gangliosidosis/Tay-Sachs or Sandhoff disease | Human clinical trial | Phase 1; enrollment 9; trial status reported as TERMINATED in retrieved registry results (no efficacy outcomes in retrieved context) | Clinical development program; not approved | NCT04669535 | (NCT04798235 chunk 1) |
| Interventional clinical trial, gene therapy | TSHA-101 (AAV9 carrying HEXA and HEXB) | One-time intrathecal AAV9 delivery of HEXA+HEXB to address HexA deficiency in infantile GM2 gangliosidosis | Human clinical trial | Active not recruiting; actual enrollment 3; outcomes include CSF/serum HexA activity, CHOP-INTEND, overall survival up to 5 years; quantitative efficacy not yet available in retrieved context | Ongoing early-phase clinical development; not approved | NCT04798235 | (NCT04798235 chunk 1) |
| Substrate reduction therapy | Miglustat | Inhibits glycosphingolipid synthesis upstream to reduce GM2 substrate burden | Animal + human clinical | In mouse models, reduced brain GM2 by up to 50% and prolonged survival; in a 24-month study of 5 juvenile patients, did not halt neurological deterioration (gonzalezsanchez2025advancesindiagnosis pages 14-15) | Off-label/experimental in GM2; not FDA-approved for Tay-Sachs | NCT00418847; NCT00672022; NCT03822013 | (gonzalezsanchez2025advancesindiagnosis pages 14-15, abidi2024metabolismofglycosphingolipids pages 85-90) |
| Next-generation substrate reduction therapy | Nizubaglustat (AZ-3102) | Small-molecule substrate reduction approach for GM2 gangliosidosis/NPC disease | Human clinical trial | Phase 2 recruiting; planned enrollment 21; no efficacy results yet in retrieved context | Investigational | NCT07399704 | (NCT04798235 chunk 1) |
| Pharmacological chaperone | Pyrimethamine | Mutation-dependent stabilization/folding rescue of residual HexA, with BBB penetration | In vitro + human clinical experience summarized in reviews | Induced up to a threefold increase in enzymatic activity in TSD fibroblasts, but neurological benefit in patients has been limited/mutation-dependent (gonzalezsanchez2025advancesindiagnosis pages 14-15) | Experimental/off-label; not standard disease-modifying therapy | not provided in retrieved context | (gonzalezsanchez2025advancesindiagnosis pages 14-15, ou2020anovelgene pages 11-11) |
| Enzyme replacement therapy | Engineered human HexA / rhHexA | Supplies exogenous enzyme to degrade stored GM2; major challenge is BBB/CNS delivery | Animal + in vitro | Engineered HexA degraded GM2 in Hexa-/- mouse-related systems and prevented severe storage in preclinical work; yeast-produced rhHexA reduced lysosomal mass and GM2 levels in patient fibroblasts/neuroglial cells after 72 h treatment (ashiri2023usinganengineered pages 23-28, abidi2024metabolismofglycosphingolipids pages 85-90) | Preclinical; no approved ERT for Tay-Sachs | not applicable | (ashiri2023usinganengineered pages 23-28, abidi2024metabolismofglycosphingolipids pages 85-90, picache2022therapeuticstrategiesfor pages 1-2) |
| Recombinant enzyme production / cell studies | Yeast-produced human recombinant lysosomal β-hexosaminidase A (rhHex-A) | Scalable recombinant enzyme for cellular rescue of GM2 storage | In vitro | In patient and murine cell systems, 100 nM rhHexA for 72 h reduced lysosomal mass and GM2/LAMP1 colocalization; authors concluded rhHex-A “can efficiently degrade GM2 ganglioside and rescue lysosomal accumulation” | Preclinical research only | not applicable | (abidi2024metabolismofglycosphingolipids pages 85-90) |
| Protein delivery across BBB | Dual trojan horse HEXA protein (HEXA linked to BBB-entry motifs) | Enzyme delivery strategy to shuttle HEXA across BBB, associate with HEXB, reach lysosomes, and reduce brain GM2 | Animal + in vitro | In adult LOTS-model mice, IV treatment reduced whole-brain GM2 by ~40% within 6 weeks and improved forelimb grip strength; also lowered GM2 in cultured human Tay-Sachs glial cells (osher2024treatinglateonsettay pages 1-2) | Preclinical; not approved | not applicable | (osher2024treatinglateonsettay pages 1-2) |
| Broad therapeutic category | HSCT / bone marrow transplantation | Cross-correction via donor-derived enzyme-producing cells | Human case series/reviewed clinical experience | Can increase systemic HexA; reported survival prolongation in some cases, but overall insufficient CNS correction and no consistent motor improvement (gonzalezsanchez2025advancesindiagnosis pages 14-15) | Not established as effective disease-modifying standard for Tay-Sachs CNS disease | not provided in retrieved context | (gonzalezsanchez2025advancesindiagnosis pages 14-15, gonzalezsanchez2025advancesindiagnosis pages 15-17) |
| Emerging pathway-targeted SRT | B4GALNT1 / GM2 synthesis inhibition (e.g., lead compound QT163) | Directly target GM2 synthesis pathway to reduce GM2 and lyso-GM2 production | Preclinical in vitro/drug discovery | Lead compound QT163 showed strongest inhibition with reported IC50 0.2 mM; lyso-GM2 proposed as biomarker for diagnosis/treatment monitoring (abidi2024metabolismofglycosphingolipids pages 85-90) | Experimental discovery-stage | not applicable | (abidi2024metabolismofglycosphingolipids pages 85-90) |


*Table: This table summarizes major therapeutic modalities and clinical-trial programs for Tay-Sachs/GM2 gangliosidosis, including current human gene-therapy studies, substrate-reduction approaches, pharmacological chaperones, and preclinical enzyme/protein-delivery strategies. It is useful for comparing mechanism, evidence maturity, quantitative outcomes, and current development status across the treatment landscape.*

### Key recent developments (prioritizing 2023–2024 sources)
- **2024 protein BBB-delivery strategy (late-onset model):** a “dual trojan horse” HEXA protein lowered whole-brain GM2 by ~40% within 6 weeks in an adult Tay–Sachs mouse model and improved grip strength (publication date Sep 2024; URL https://doi.org/10.1016/j.omtm.2024.101300) (osher2024treatinglateonsettay pages 1-2).
- **2023 fetal-stage mechanistic insight:** transcriptomic perturbations by 17 weeks’ gestation suggest a potentially earlier window for intervention than clinical onset (publication date Feb 2023; URL https://doi.org/10.1002/jimd.12596) (han2023geneexpressionchanges pages 1-3).

### Human gene therapy evidence (first-in-human)
A first-in-human expanded-access experience (Nature Medicine version published Feb 2022; preprint posted Feb 18, 2021; URL https://doi.org/10.1038/s41591-021-01664-4; preprint URL https://doi.org/10.21203/rs.3.rs-195847/v1) reported intrathecal and intrathalamic delivery of AAVrh8-HEXA plus AAVrh8-HEXB in two infantile Tay–Sachs patients, with no vector-related adverse events and increased CSF HexA activity; MRI and seizure outcomes suggested partial/temporary deviation from expected infantile natural history in the younger-treated child (flotte2022aavgenetherapy pages 1-6).

**Figure evidence:** the treatment-associated HexA activity trajectories and delivery-route imaging are shown in retrieved figure/table regions from the case report (flotte2022aavgenetherapy media 379a08f6, flotte2022aavgenetherapy media 8b29bbe4, flotte2022aavgenetherapy media 4f87ceb4, flotte2022aavgenetherapy media c9927c10).

### MAXO term suggestions (examples)
- Gene therapy (intrathecal/intracerebral AAV delivery) (flotte2022aavgenetherapy pages 1-6, NCT04798235 chunk 1)
- Enzyme replacement therapy / enzyme supplementation (preclinical) (gonzalezsanchez2025advancesindiagnosis pages 14-15)
- Substrate reduction therapy (miglustat; investigational agents) (gonzalezsanchez2025advancesindiagnosis pages 14-15, NCT04798235 chunk 1)
- Hematopoietic stem cell transplantation (selected contexts) (gonzalezsanchez2025advancesindiagnosis pages 14-15)

## 13. Prevention

- **Primary prevention via carrier screening:** in some Ashkenazi communities, premarital carrier screening is associated with an approximately **95% reduction in incidence** in a synthesis review (gonzalezsanchez2025advancesindiagnosis pages 2-4).
- **Secondary prevention / early detection:** biochemical screening using dried blood spots and molecular confirmation can enable earlier diagnosis; prenatal diagnosis is feasible via CVS (10–12 weeks) or amniocentesis (15–18 weeks) in at-risk pregnancies (gonzalezsanchez2025advancesindiagnosis pages 4-5, bibi2021taysachsdiseasetwo pages 5-8).

## 14. Other species / natural disease

- **Naturally occurring large-animal model:** Jacob sheep with a naturally occurring HEXA missense mutation develop progressive neurologic disease and GM2 accumulation; the model enables biomarker and therapeutic evaluation at a large-brain scale (story2021naturalhistoryof pages 1-2, story2021naturalhistoryof pages 5-7).
- Additional natural disease has been described in other species (e.g., cats/dogs; wild boar variants mentioned in a compilation), but detailed comparative pathology was not comprehensively extractable from the retrieved evidence set (ashiri2023usinganengineered pages 129-133).

## 15. Model organisms

- **Mouse models:** Hexa knockout mice show GM2 accumulation but may lack classical clinical phenotypes due to alternative GM2 catabolic pathways, limiting phenotypic fidelity for some questions (picache2022therapeuticstrategiesfor pages 6-8, gonzalezsanchez2025advancesindiagnosis pages 11-12).
- **Rabbit genome-edited model:** prime editing of a common Tay–Sachs insertion produced late-onset–like neurologic and muscle pathology features (picache2022therapeuticstrategiesfor pages 6-8).
- **Sheep model (natural history):** provides staged progression (mild symptoms at ~3 months; moderate at ~6 months; severe with humane endpoint around ~9 months), CSF GM2 biomarker utility, and MRI/MRS correlates (story2021naturalhistoryof pages 1-2, story2021naturalhistoryof pages 5-7).
- **Translational therapy testing:** A 5-year AAV gene therapy analysis in Tay–Sachs sheep reported long survival after multipoint CSF delivery, supporting large-animal evaluation of delivery routes, biomarkers, and durability (publication date Sep 2025; URL https://doi.org/10.1172/jci182942) (taghian2025fiveyearanalysisof pages 1-2).

## Limitations of this report (evidence availability)
- ICD-10/ICD-11/MeSH/MONDO identifiers were not present in the retrieved evidence set and therefore are explicitly not populated to avoid hallucination (artifact-00).
- Several key references in this area exist but were not retrievable within this tool run; consequently, some sections (e.g., global epidemiology by region, comprehensive variant frequency from gnomAD, formal clinical guidelines, and late-2024 Neurology Genetics diagnostic paper) could not be exhaustively covered.


References

1. (gonzalezsanchez2025advancesindiagnosis pages 1-2): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

2. (ibrahim2023biochemicalandmutational pages 1-2): Doaa M. A. Ibrahim, Ola S. M. Ali, Hala Nasr, Ekram Fateen, and Alice AbdelAleem. Biochemical and mutational analyses of hexa in a cohort of egyptian patients with infantile tay-sachs disease. expansion of the mutation spectrum. Orphanet Journal of Rare Diseases, Mar 2023. URL: https://doi.org/10.1186/s13023-023-02637-1, doi:10.1186/s13023-023-02637-1. This article has 13 citations and is from a peer-reviewed journal.

3. (gonzalezsanchez2025advancesindiagnosis pages 2-4): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

4. (han2023geneexpressionchanges pages 1-3): Sangwoo T. Han, Ashley Hirt, Elena‐Raluca Nicoli, Mari Kono, Camilo Toro, Richard L. Proia, and Cynthia J. Tifft. Gene expression changes in <scp>tay–sachs</scp> disease begin early in fetal brain development. Journal of Inherited Metabolic Disease, 46:687-694, Feb 2023. URL: https://doi.org/10.1002/jimd.12596, doi:10.1002/jimd.12596. This article has 10 citations and is from a peer-reviewed journal.

5. (picache2022therapeuticstrategiesfor pages 1-2): Jaqueline A. Picache, Wei Zheng, and Catherine Z. Chen. Therapeutic strategies for tay-sachs disease. Frontiers in Pharmacology, Jul 2022. URL: https://doi.org/10.3389/fphar.2022.906647, doi:10.3389/fphar.2022.906647. This article has 40 citations.

6. (NCT04798235 chunk 1): Dr. Anupam Sehgal. First-in-Human Study of TSHA-101 Gene Therapy for Treatment of Infantile Onset GM2 Gangliosidosis. Dr. Anupam Sehgal. 2021. ClinicalTrials.gov Identifier: NCT04798235

7. (gonzalezsanchez2025advancesindiagnosis pages 5-7): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

8. (gonzalezsanchez2025advancesindiagnosis pages 7-9): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

9. (ashiri2023usinganengineered pages 16-23): M Ashiri. Using an engineered human hexosaminidase as an enzyme replacement therapy to treat a mouse model of tay-sachs disease. Unknown journal, 2023.

10. (gonzalezsanchez2025advancesindiagnosis pages 9-11): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

11. (sheth2018identificationofdeletionduplication pages 1-2): Jayesh Sheth, Mehul Mistri, Lakshmi Mahadevan, Sanjeev Mehta, Dhaval Solanki, Mahesh Kamate, and Frenny Sheth. Identification of deletion-duplication in hexa gene in five children with tay-sachs disease from india. BMC Medical Genetics, Jul 2018. URL: https://doi.org/10.1186/s12881-018-0632-7, doi:10.1186/s12881-018-0632-7. This article has 11 citations and is from a peer-reviewed journal.

12. (lyn2020patientandcaregiver pages 1-2): Nicole Lyn, Ruth Pulikottil-Jacob, Camille Rochmann, Robert Krupnick, Chad Gwaltney, Nick Stephens, Julie Kissell, Gerald F. Cox, Tanya Fischer, and Alaa Hamed. Patient and caregiver perspectives on burden of disease manifestations in late-onset tay-sachs and sandhoff diseases. Orphanet Journal of Rare Diseases, Apr 2020. URL: https://doi.org/10.1186/s13023-020-01354-3, doi:10.1186/s13023-020-01354-3. This article has 19 citations and is from a peer-reviewed journal.

13. (gonzalezsanchez2025advancesindiagnosis pages 4-5): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

14. (barritt2017lateonsettay–sachsdisease pages 1-2): Andrew W Barritt, Stuart J Anderson, P Nigel Leigh, and Basil H Ridha. Late-onset tay–sachs disease. Practical Neurology, 17:396-399, Jul 2017. URL: https://doi.org/10.1136/practneurol-2017-001665, doi:10.1136/practneurol-2017-001665. This article has 38 citations and is from a peer-reviewed journal.

15. (sheth2018identificationofdeletionduplication pages 2-3): Jayesh Sheth, Mehul Mistri, Lakshmi Mahadevan, Sanjeev Mehta, Dhaval Solanki, Mahesh Kamate, and Frenny Sheth. Identification of deletion-duplication in hexa gene in five children with tay-sachs disease from india. BMC Medical Genetics, Jul 2018. URL: https://doi.org/10.1186/s12881-018-0632-7, doi:10.1186/s12881-018-0632-7. This article has 11 citations and is from a peer-reviewed journal.

16. (ashiri2023usinganengineered pages 23-28): M Ashiri. Using an engineered human hexosaminidase as an enzyme replacement therapy to treat a mouse model of tay-sachs disease. Unknown journal, 2023.

17. (story2021naturalhistoryof pages 5-7): Brett Story, Toloo Taghian, Jillian Gallagher, Jey Koehler, Amanda Taylor, Ashley Randle, Kayly Nielsen, Amanda Gross, Annie Maguire, Sara Carl, Siauna Johnson, Deborah Fernau, Elise Diffie, Paul Cuddon, Carly Corado, Sundeep Chandra, Miguel Sena-Esteves, Edwin Kolodny, Xuntian Jiang, Douglas Martin, and Heather Gray-Edwards. Natural history of tay-sachs disease in sheep. Molecular Genetics and Metabolism, 134:164-174, Sep 2021. URL: https://doi.org/10.1016/j.ymgme.2021.08.009, doi:10.1016/j.ymgme.2021.08.009. This article has 13 citations and is from a peer-reviewed journal.

18. (bibi2021taysachsdiseasetwo pages 5-8): Farah Bibi, Asmat Ullah, Thomas Bourinaris, Stephanie Efthymiou, Yamna Kriouile, Tipu Sultan, Shahzad Haider, Vincenzo Salpietro, Henry Houlden, and Ghazala Kaukab Raja. Tay-sachs disease: two novel rare hexa mutations from pakistan and morocco. Klinische Pädiatrie, 233:226-230, Apr 2021. URL: https://doi.org/10.1055/a-1371-1561, doi:10.1055/a-1371-1561. This article has 17 citations.

19. (flotte2022aavgenetherapy pages 1-6): Terence R. Flotte, Oguz Cataltepe, Ajit Puri, Ana Rita Batista, Richard Moser, Diane McKenna-Yasek, Catherine Douthwright, Gwladys Gernoux, Meghan Blackwood, Christian Mueller, Phillip W. L. Tai, Xuntian Jiang, Scot Bateman, Spiro G. Spanakis, Julia Parzych, Allison M. Keeler, Aly Abayazeed, Saurabh Rohatgi, Laura Gibson, Robert Finberg, Bruce A. Barton, Zeynep Vardar, Mohammed Salman Shazeeb, Matthew Gounis, Cynthia J. Tifft, Florian S. Eichler, Robert H. Brown, Douglas R. Martin, Heather L. Gray-Edwards, and Miguel Sena-Esteves. Aav gene therapy for tay-sachs disease. Nature Medicine, 28:251-259, Feb 2022. URL: https://doi.org/10.1038/s41591-021-01664-4, doi:10.1038/s41591-021-01664-4. This article has 155 citations and is from a highest quality peer-reviewed journal.

20. (gonzalezsanchez2025advancesindiagnosis pages 15-17): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

21. (gonzalezsanchez2025advancesindiagnosis pages 14-15): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

22. (abidi2024metabolismofglycosphingolipids pages 85-90): I Abidi. Metabolism of glycosphingolipids and targeting gm2 synthesis pathway to develop substrate reduction approach in tay-sachs and sandhoff disorders. Unknown journal, 2024.

23. (ou2020anovelgene pages 11-11): Li Ou, Michael J. Przybilla, Alexandru-Flaviu Tăbăran, Paula Overn, M. Gerard O’Sullivan, Xuntian Jiang, Rohini Sidhu, Pamela J. Kell, Daniel S. Ory, and Chester B. Whitley. A novel gene editing system to treat both tay–sachs and sandhoff diseases. Gene Therapy, 27:226-236, Jan 2020. URL: https://doi.org/10.1038/s41434-019-0120-5, doi:10.1038/s41434-019-0120-5. This article has 70 citations and is from a peer-reviewed journal.

24. (osher2024treatinglateonsettay pages 1-2): Esther Osher, Yossi Anis, Ruth Singer-Shapiro, Nataly Urshanski, Tamar Unger, Shira Albeck, Oren Bogin, Gary Weisinger, Fortune Kohen, Avi Valevski, Aviva Fattal-Valevski, Liora Sagi, Michal Weitman, Yulia Shenberger, Nadav Sagiv, Ruth Navon, Meir Wilchek, and Naftali Stern. Treating late-onset tay sachs disease: brain delivery with a dual trojan horse protein. Molecular Therapy - Methods &amp; Clinical Development, 32:101300, Sep 2024. URL: https://doi.org/10.1016/j.omtm.2024.101300, doi:10.1016/j.omtm.2024.101300. This article has 5 citations.

25. (flotte2022aavgenetherapy media 379a08f6): Terence R. Flotte, Oguz Cataltepe, Ajit Puri, Ana Rita Batista, Richard Moser, Diane McKenna-Yasek, Catherine Douthwright, Gwladys Gernoux, Meghan Blackwood, Christian Mueller, Phillip W. L. Tai, Xuntian Jiang, Scot Bateman, Spiro G. Spanakis, Julia Parzych, Allison M. Keeler, Aly Abayazeed, Saurabh Rohatgi, Laura Gibson, Robert Finberg, Bruce A. Barton, Zeynep Vardar, Mohammed Salman Shazeeb, Matthew Gounis, Cynthia J. Tifft, Florian S. Eichler, Robert H. Brown, Douglas R. Martin, Heather L. Gray-Edwards, and Miguel Sena-Esteves. Aav gene therapy for tay-sachs disease. Nature Medicine, 28:251-259, Feb 2022. URL: https://doi.org/10.1038/s41591-021-01664-4, doi:10.1038/s41591-021-01664-4. This article has 155 citations and is from a highest quality peer-reviewed journal.

26. (flotte2022aavgenetherapy media 8b29bbe4): Terence R. Flotte, Oguz Cataltepe, Ajit Puri, Ana Rita Batista, Richard Moser, Diane McKenna-Yasek, Catherine Douthwright, Gwladys Gernoux, Meghan Blackwood, Christian Mueller, Phillip W. L. Tai, Xuntian Jiang, Scot Bateman, Spiro G. Spanakis, Julia Parzych, Allison M. Keeler, Aly Abayazeed, Saurabh Rohatgi, Laura Gibson, Robert Finberg, Bruce A. Barton, Zeynep Vardar, Mohammed Salman Shazeeb, Matthew Gounis, Cynthia J. Tifft, Florian S. Eichler, Robert H. Brown, Douglas R. Martin, Heather L. Gray-Edwards, and Miguel Sena-Esteves. Aav gene therapy for tay-sachs disease. Nature Medicine, 28:251-259, Feb 2022. URL: https://doi.org/10.1038/s41591-021-01664-4, doi:10.1038/s41591-021-01664-4. This article has 155 citations and is from a highest quality peer-reviewed journal.

27. (flotte2022aavgenetherapy media 4f87ceb4): Terence R. Flotte, Oguz Cataltepe, Ajit Puri, Ana Rita Batista, Richard Moser, Diane McKenna-Yasek, Catherine Douthwright, Gwladys Gernoux, Meghan Blackwood, Christian Mueller, Phillip W. L. Tai, Xuntian Jiang, Scot Bateman, Spiro G. Spanakis, Julia Parzych, Allison M. Keeler, Aly Abayazeed, Saurabh Rohatgi, Laura Gibson, Robert Finberg, Bruce A. Barton, Zeynep Vardar, Mohammed Salman Shazeeb, Matthew Gounis, Cynthia J. Tifft, Florian S. Eichler, Robert H. Brown, Douglas R. Martin, Heather L. Gray-Edwards, and Miguel Sena-Esteves. Aav gene therapy for tay-sachs disease. Nature Medicine, 28:251-259, Feb 2022. URL: https://doi.org/10.1038/s41591-021-01664-4, doi:10.1038/s41591-021-01664-4. This article has 155 citations and is from a highest quality peer-reviewed journal.

28. (flotte2022aavgenetherapy media c9927c10): Terence R. Flotte, Oguz Cataltepe, Ajit Puri, Ana Rita Batista, Richard Moser, Diane McKenna-Yasek, Catherine Douthwright, Gwladys Gernoux, Meghan Blackwood, Christian Mueller, Phillip W. L. Tai, Xuntian Jiang, Scot Bateman, Spiro G. Spanakis, Julia Parzych, Allison M. Keeler, Aly Abayazeed, Saurabh Rohatgi, Laura Gibson, Robert Finberg, Bruce A. Barton, Zeynep Vardar, Mohammed Salman Shazeeb, Matthew Gounis, Cynthia J. Tifft, Florian S. Eichler, Robert H. Brown, Douglas R. Martin, Heather L. Gray-Edwards, and Miguel Sena-Esteves. Aav gene therapy for tay-sachs disease. Nature Medicine, 28:251-259, Feb 2022. URL: https://doi.org/10.1038/s41591-021-01664-4, doi:10.1038/s41591-021-01664-4. This article has 155 citations and is from a highest quality peer-reviewed journal.

29. (story2021naturalhistoryof pages 1-2): Brett Story, Toloo Taghian, Jillian Gallagher, Jey Koehler, Amanda Taylor, Ashley Randle, Kayly Nielsen, Amanda Gross, Annie Maguire, Sara Carl, Siauna Johnson, Deborah Fernau, Elise Diffie, Paul Cuddon, Carly Corado, Sundeep Chandra, Miguel Sena-Esteves, Edwin Kolodny, Xuntian Jiang, Douglas Martin, and Heather Gray-Edwards. Natural history of tay-sachs disease in sheep. Molecular Genetics and Metabolism, 134:164-174, Sep 2021. URL: https://doi.org/10.1016/j.ymgme.2021.08.009, doi:10.1016/j.ymgme.2021.08.009. This article has 13 citations and is from a peer-reviewed journal.

30. (ashiri2023usinganengineered pages 129-133): M Ashiri. Using an engineered human hexosaminidase as an enzyme replacement therapy to treat a mouse model of tay-sachs disease. Unknown journal, 2023.

31. (picache2022therapeuticstrategiesfor pages 6-8): Jaqueline A. Picache, Wei Zheng, and Catherine Z. Chen. Therapeutic strategies for tay-sachs disease. Frontiers in Pharmacology, Jul 2022. URL: https://doi.org/10.3389/fphar.2022.906647, doi:10.3389/fphar.2022.906647. This article has 40 citations.

32. (gonzalezsanchez2025advancesindiagnosis pages 11-12): María González-Sánchez, María Jesús Ramírez-Expósito, and José Manuel Martínez-Martos. Advances in diagnosis, pathological mechanisms, clinical impact, and future therapeutic perspectives in tay–sachs disease. Neurology International, 17:98, Jun 2025. URL: https://doi.org/10.3390/neurolint17070098, doi:10.3390/neurolint17070098. This article has 4 citations.

33. (taghian2025fiveyearanalysisof pages 1-2): Toloo Taghian, Jillian Gallagher, Stephanie Bertrand, William C. Baker, Kalajan Lopez Mercado, Hector R. Benatti, Erin Hall, Yvette Lopez, Abigail McElroy, John T. McCarthy, Sanjana Pulaparthi, Deborah Fernau, Samuel Mather, Sophia Esteves, Elise Diffie, Amanda Gross, Hannah G. Lahey, Xuntian Jiang, Elizabeth Parsley, Rachael Gately, Rachel Prestigiacomo, Siauna Johnson, Amanda Taylor, Lindsey Bierfeldt, Susan Tuominen, Jennifer Koehler, Guangping Gao, Jun Xie, Qin Su, Robert King, Matthew J. Gounis, Vania Anagnostakou, Ajit Puri, Ana Rita Batista, Miguel Sena-Esteves, Douglas R. Martin, and Heather Gray-Edwards. Five-year analysis of efficacy and safety of a bidirectional aav gene therapy in tay-sachs sheep. Journal of Clinical Investigation, Sep 2025. URL: https://doi.org/10.1172/jci182942, doi:10.1172/jci182942. This article has 0 citations and is from a highest quality peer-reviewed journal.
