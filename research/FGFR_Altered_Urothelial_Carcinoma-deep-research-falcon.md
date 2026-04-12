---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T14:57:54.406423'
end_time: '2026-04-05T15:10:29.547464'
duration_seconds: 755.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FGFR-Altered Urothelial Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FGFR-Altered Urothelial Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **FGFR-Altered Urothelial Carcinoma** covering all of the
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
- **Disease Name:** FGFR-Altered Urothelial Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **FGFR-Altered Urothelial Carcinoma** covering all of the
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


## Comprehensive Research Report: FGFR‑Altered Urothelial Carcinoma (FGFR‑altered UC)

### Scope and evidence basis
This report focuses on urothelial carcinoma (UC) in which tumors harbor clinically actionable **FGFR pathway alterations**, predominantly **FGFR3 activating mutations** and less commonly **FGFR2/3 fusions** (the alterations used to select patients for FGFR inhibitors such as erdafitinib). Evidence is drawn from recent primary studies and high-quality reviews, emphasizing 2023–2024 publications and ClinicalTrials.gov records.

---

## 1. Disease Information

### 1.1 Definition and overview
**FGFR‑altered urothelial carcinoma** is not a separate histopathologic diagnosis, but a **molecularly defined subset** of urothelial carcinoma characterized by oncogenic alterations in **FGFR2 and/or FGFR3** that can predict sensitivity to FGFR‑targeted therapy (notably **erdafitinib**). In a real‑world genomic/clinical cohort, Guercio et al. describe FGFR‑altered UC as tumors harboring **oncogenic FGFR3 mutations** or **FGFR2/3 fusions**, which are “established predictive biomarkers for erdafitinib.” (guercio2023clinicalandgenomic pages 2-4)

### 1.2 Key identifiers (availability in retrieved evidence)
* **ICD codes / MeSH / OMIM / Orphanet / MONDO**: A distinct “FGFR‑altered UC” code was **not identified in the retrieved evidence**. In practice, coding is typically done at the disease-site level (e.g., bladder cancer / urothelial carcinoma) with FGFR status stored as a biomarker attribute.

### 1.3 Synonyms and alternative names
Common usage in the literature includes:
* **FGFR2/3‑altered urothelial carcinoma** (testi2024targetedtherapiesand pages 11-13, benjamin2023treatmentapproachesfor pages 3-4)
* **FGFR3‑altered bladder cancer** (guercio2023clinicalandgenomic pages 6-7)
* **FGFR3‑mutant urothelial carcinoma** (bannier2024aiallowsprescreening pages 1-2)

### 1.4 Data provenance (patient-level vs aggregated)
Evidence includes:
* **Aggregated disease-level and biomarker-level resources** (e.g., cohort multi‑omics in metastatic UC; reviews) (antar2024theevolvingmolecular pages 3-5, shang2024landscapeoftargeted pages 3-5)
* **Patient-level institutional clinical genomics + outcomes** (real‑world erdafitinib outcomes, paired primary/metastasis discordance, cfDNA evolution) (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic pages 6-7)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
FGFR‑altered UC is driven by **somatic activating alterations** in FGFR signaling (primarily FGFR3), promoting urothelial tumor initiation/maintenance via pro‑proliferative and pro‑survival signaling (MAPK/PI3K/STAT) (shang2024landscapeoftargeted pages 3-5, shan2024moleculartargetingof pages 4-5).

### 2.2 Risk factors for urothelial carcinoma (UC)
Major risk factors for UC in general (not specific to FGFR subtype) include:
* **Tobacco smoking** (listed as a major UC risk factor) (mitiushkina2024useof3′ pages 1-2, ferreira2023epimarkersforbladder pages 19-26)
* **Occupational exposure to aromatic amines** (mitiushkina2024useof3′ pages 1-2)
* **Contaminated drinking water** (mitiushkina2024useof3′ pages 1-2)
* **Family history + lifestyle interactions**: in a population cohort, individuals with an affected first‑degree relative had elevated risk, and **smokers with positive family history** showed a strong interaction (HR 3.60; RERI 0.72), indicating gene–environment interplay at the level of familial susceptibility and smoking exposure (guercio2023clinicalandgenomic pages 1-2).

### 2.3 Protective factors
High-quality protective-factor evidence specific to FGFR‑altered UC was **not identified in the retrieved evidence**. For UC overall, prevention strategies generally focus on **risk-factor avoidance** (e.g., smoking cessation, reducing occupational carcinogen exposure), but quantitative protective estimates were not captured in the extracted evidence.

### 2.4 Gene–environment interactions
Direct GxE interactions tied specifically to **FGFR alterations** were not captured in the extracted 2023–2024 evidence. However, familial predisposition interacting with smoking for bladder cancer risk has been quantified (guercio2023clinicalandgenomic pages 1-2).

---

## 3. Phenotypes (clinical presentation)

### 3.1 Core clinical phenotypes of UC
Key presenting features of urothelial bladder cancer include:
* **Hematuria** (gross or microscopic) as the most common presenting sign; one source notes “the most common presenting sign is hematuria (gross or microscopic)” (ferreira2023epimarkersforbladder pages 26-29).
* **Dysuria** and **polyuria** also occur (ferreira2023epimarkersforbladder pages 26-29).
* Stage association: visible hematuria is described as being “usually associated with more advanced stage/grade.” (ferreira2023epimarkersforbladder pages 26-29)

Upper tract UC (UTUC) is not extensively phenotyped in the extracted symptom-focused evidence, but UTUC is described as more aggressive with high invasiveness at diagnosis (60% invasive at diagnosis) (mitiushkina2024useof3′ pages 1-2).

### 3.2 Age of onset and distribution
* Bladder cancer is predominantly a disease of older adults; one summary reports **~80% of patients are older than 65 years** (ferreira2023epimarkersforbladder pages 19-26).

### 3.3 Stage distribution at diagnosis (UC overall)
* **NMIBC predominates**: majority are NMIBC (70–80%), while MIBC accounts for ~20–30% at diagnosis (ferreira2023epimarkersforbladder pages 26-29).
* **Metastatic at diagnosis**: about **5%** of bladder cancers are metastatic at diagnosis (mitiushkina2024useof3′ pages 1-2).

### 3.4 Suggested HPO terms (examples)
* Hematuria — **HP:0000790**
* Dysuria — **HP:0100518**
* Polyuria — **HP:0000103**
* Urinary urgency — **HP:0000012** (common in bladder cancer symptom clusters; not directly quantified in extracted evidence)

### 3.5 Quality-of-life impact
Direct validated QoL instrument data (e.g., EQ‑5D/SF‑36) specific to FGFR‑altered UC were **not identified in extracted evidence**; however, urinary symptoms (hematuria, dysuria, polyuria) are clinically burdensome (ferreira2023epimarkersforbladder pages 26-29).

---

## 4. Genetic / Molecular Information (FGFR alterations)

### 4.1 Causal/driver genes
* **FGFR3** is the dominant driver in this subtype; **FGFR2** alterations occur but are comparatively rare in UC (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic pages 2-4).

### 4.2 Alteration types and prevalence (key statistics)
Guercio et al. reported stage-stratified frequencies of **FGFR3 alterations predictive of erdafitinib sensitivity**:
* **NMIBC:** 39% (199/504)
* **MIBC:** 14% (75/526)
* **Localized UTUC:** 43% (81/187)
* **Metastatic specimens:** 26% (59/228) (guercio2023clinicalandgenomic pages 1-2)

A complementary Japanese multi‑omics cohort similarly reported FGFR3 alterations (mutations + fusions) of **44% in NMIBC** and **15% in MIBC** (komura2023theimpactof pages 1-2).

Metastatic biopsy profiling showed **FGFR3 actionable targets in 26%** of metastatic biopsies and noted that “potential therapeutic targets” were found in **73%** overall (antar2024theevolvingmolecular pages 3-5).

A targeted RNA‑sequencing study found **FGFR2/3 activating point mutations or fusions in 23.2% (54/233)** of urothelial carcinomas, with enrichment in upper tract vs bladder (48% vs 20%) (mitiushkina2024useof3′ pages 2-3).

### 4.3 Pathogenic variants (examples; primarily somatic)
In a real-world metastatic erdafitinib-treated cohort, common FGFR3 alterations included:
* **S249C** (59%), **Y373C** (9%), **R248C** (9%)
* **FGFR3–TACC3 fusions** (13%) (guercio2023clinicalandgenomic pages 6-7)

### 4.4 Somatic vs germline
The evidence base here pertains to **tumor somatic alterations** and tumor-derived cfDNA evolution under therapy (guercio2023clinicalandgenomic pages 2-4). Germline FGFR2/3 causes of UC were not supported by extracted evidence.

### 4.5 Tumor heterogeneity and discordance
Clinically important sampling issue: among paired primary tumors and metachronous metastases, **26%** showed **discordant FGFR3 status**, raising concern about using archival primary tissue alone for selection (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic pages 2-4).

---

## 5. Mechanism / Pathophysiology

### 5.1 Molecular pathways downstream of FGFR3 alterations
FGFR3 activation can occur via missense mutations or FGFR3–TACC3 fusions:
* Fusions: FGFR3–TACC3 fusions drive constitutive activation of **MAPK**, **PI3K/AKT**, and **STAT3** signaling; altered TACC3 function may contribute to mitotic defects/aneuploidy (shang2024landscapeoftargeted pages 3-5).
* Missense mutations: gain‑of‑function missense mutations can drive **ligand-independent dimerization** and increased kinase activity (shan2024moleculartargetingof pages 4-5).

### 5.2 Molecular subtype context and tumor microenvironment (TME)
FGFR3 alterations are strongly associated with luminal biology:
* In a large Japanese cohort, FGFR3 alterations were linked to luminal papillary enrichment: “LumP was significantly more prevalent in aFGFR3” (komura2023theimpactof pages 1-2).
* FGFR3-altered tumors are often characterized as having reduced T‑cell infiltration and a “non–T cell–inflamed” microenvironment in multiple mechanistic discussions (okato2024fgfrinhibitionaugments pages 1-2, komura2023theimpactof pages 1-2).

### 5.3 Immune checkpoint inhibitor (ICI) response heterogeneity and proposed immune targets
Komura et al. reported clinically relevant response heterogeneity:
* In CPI-treated patients, **overall ORR** was similar between intact vs altered FGFR3: **20% vs 31%** (p=0.467) (komura2023theimpactof pages 1-2).
* In the **LumP subtype**, ORR differed markedly: **LumP/aFGFR3 50% vs LumP/iFGFR3 5%** (p=0.022) (komura2023theimpactof pages 1-2).
* Transcriptome analysis highlighted **TIM3** as the most upregulated immune-related gene in iFGFR3, and authors propose **TIM3** as a target for iFGFR3 and **IDO1/CCL24** for LumP/iFGFR3 (komura2023theimpactof pages 1-2).

### 5.4 Resistance mechanisms to FGFR inhibition
Evidence-supported resistance mechanisms include:
* **On-target second-site FGFR3 mutations** (e.g., kinase-domain mutations, including gatekeeper-like changes) emerging in cfDNA during erdafitinib therapy (guercio2023clinicalandgenomic pages 6-7).
* **Bypass/parallel pathway alterations**: emergent cfDNA alterations included **TP53**, **AKT1**, and second-site **FGFR3** mutations (guercio2023clinicalandgenomic pages 6-7, guercio2023clinicalandgenomic pages 2-4).
* A proposed metabolic/hypoxia-linked resistance program: upregulation of **P4HA2** via a **HIF1α feedback loop** reducing ROS and mediating acquired resistance to erdafitinib (shang2024landscapeoftargeted pages 3-5).

### 5.5 Suggested GO terms (examples)
* **FGFR signaling pathway** (e.g., GO:0008543 fibroblast growth factor receptor signaling pathway)
* **MAPK cascade** (GO:0000165)
* **PI3K/AKT signaling** (e.g., GO:0014065 phosphatidylinositol 3-kinase signaling)
* **STAT3 signaling** (e.g., GO:0046427 positive regulation of JAK-STAT cascade)
* **Regulation of T cell proliferation** (GO:0042129) (relevant to Treg expansion effects described) (okato2024fgfrinhibitionaugments pages 1-2)

### 5.6 Suggested Cell Ontology (CL) terms (examples)
* **Urothelial cell** (CL class; urothelium-derived carcinoma)
* **Regulatory T cell** (CL:0000815) (Treg expansion/abrogation under combined therapy in murine model) (okato2024fgfrinhibitionaugments pages 1-2)

---

## 6. Diagnostics

### 6.1 Standard UC diagnostics (brief)
Standard clinical diagnosis relies on cystoscopy, pathology, and staging. Molecular FGFR testing is added to identify candidates for FGFR-targeted therapy.

### 6.2 FGFR alteration testing approaches
**Tissue-based NGS and cfDNA**
* In real‑world practice, tumor sequencing (e.g., targeted panel NGS) was used to identify oncogenic FGFR alterations, and cfDNA was used for longitudinal monitoring under erdafitinib (guercio2023clinicalandgenomic pages 2-4).

**RNA-based approaches (fusion detection and breadth)**
* A targeted RNA-seq (3′ RACE) approach detected FGFR2/3 alterations in 23.2% overall and found that **8/11 FGFR3 rearrangements** were **undetectable by commonly used PCR kits**, highlighting fusion-detection limitations of some PCR strategies (mitiushkina2024useof3′ pages 1-2, mitiushkina2024useof3′ pages 2-3).

**Companion diagnostic / RT‑PCR**
* The **QIAGEN therascreen FGFR RGQ RT‑PCR** assay is referenced as the companion diagnostic used to select patients eligible for erdafitinib (bannier2024aiallowsprescreening pages 2-3, jain2024acomprehensiveoverview pages 8-10).

**AI-based prescreening on H&E slides (2024 development)**
A Nature Communications study developed a deep-learning H&E prescreening tool to triage FGFR3 mutation testing:
* Reported that the model achieved **sensitivity >93%** on advanced/metastatic cases while reducing molecular testing by **~40%** on average (bannier2024aiallowsprescreening pages 1-2).
* External performance included AUC values around **0.82–0.89** in independent cohorts (bannier2024aiallowsprescreening pages 1-2).

### 6.3 Practical implementation note
Because FGFR3 status can be discordant between primary and metastasis (26% discordance), **testing the most recent/metastatic specimen when feasible** is supported by real‑world evidence (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic pages 2-4).

---

## 7. Outcome / Prognosis

### 7.1 General UC outcomes by stage
A bladder-cancer biomarker resource summarized SEER-like stage survival gradients: ~**96%** 5‑year survival for mucosa‑confined disease and ~**7%** for distant metastasis (ferreira2023epimarkersforbladder pages 26-29). These are not FGFR‑specific.

### 7.2 FGFR-altered vs unselected prognosis
The extracted evidence is mixed and context-dependent:
* FGFR3 alterations are enriched in earlier-stage disease (NMIBC, papillary phenotypes), which often carries better prognosis, but metastatic FGFR‑altered UC remains lethal.
* In metastatic biopsies, FGFR3 is one of the most common actionable targets (26%), emphasizing clinical relevance in advanced disease (antar2024theevolvingmolecular pages 3-5).

### 7.3 Prognostic factors during FGFR inhibitor therapy
Real‑world erdafitinib outcomes were relatively short in a heavily pretreated cohort (median PFS 2.8 months; OS 6.6 months) and TP53 co-alterations were implicated as unfavorable in response analyses (guercio2023clinicalandgenomic pages 6-7).

---

## 8. Treatment (current applications and real‑world implementation)

### 8.1 Approved targeted therapy: erdafitinib
Erdafitinib is the only widely cited FDA-approved targeted therapy for metastatic UC with select FGFR2/3 alterations in the evidence base (guercio2023clinicalandgenomic pages 2-4, benjamin2023treatmentapproachesfor pages 3-4).

Key pivotal and real‑world outcomes are summarized in the table below.

| Therapy/setting | Eligibility biomarker | Key outcomes (ORR, median PFS, median OS) | Key safety notes | Publication (journal, year) and URL |
|---|---|---|---|---|
| **BLC2001**: erdafitinib, phase 2, previously treated metastatic/advanced UC | Prespecified **FGFR2/3 alterations**; responses higher in **FGFR3 mutations** than **FGFR2/3 fusions** | **ORR 40%** (CR **3%**, PR **37%**); median **PFS 5.5 months**; median **OS 13.8 months**. In one summary, ORR was **49%** for FGFR3 mutations vs **16%** for FGFR2/3 fusions (testi2024targetedtherapiesand pages 11-13, benjamin2023treatmentapproachesfor pages 3-4, shang2024landscapeoftargeted pages 3-5) | Common AEs: **hyperphosphatemia**, **stomatitis**, **diarrhea**; ocular toxicity/**central serous retinopathy ~21–23%**; grade ≥3 AEs **46%**; **13%** discontinued due to AEs (testi2024targetedtherapiesand pages 11-13, benjamin2023treatmentapproachesfor pages 3-4) | *Frontiers in Immunology* (2023), Benjamin & Hsu. https://doi.org/10.3389/fimmu.2023.1258388 ; *Exploration of Targeted Anti-tumor Therapy* (2024), Testi et al. https://doi.org/10.37349/etat.2024.00279 |
| **THOR cohort 1**: erdafitinib vs chemotherapy after prior therapy, **NCT03390504** | Metastatic/advanced UC with **select FGFR alterations** | Median **OS 12.1 vs 7.8 months**; median **PFS 5.6 vs 2.7 months**; **ORR 46% vs 12%** for erdafitinib vs chemotherapy (benjamin2023treatmentapproachesfor pages 3-4, shang2024landscapeoftargeted pages 3-5) | Toxicities common; one summary states treatment-related AEs in all patients and **67% grade 3–4** with hyperphosphatemia frequent (shang2024landscapeoftargeted pages 3-5) | *Frontiers in Immunology* (2023), Benjamin & Hsu. https://doi.org/10.3389/fimmu.2023.1258388 ; *Exploration of Targeted Anti-tumor Therapy* (2024), Shang et al. https://doi.org/10.37349/etat.2024.00240 |
| **THOR Japanese subgroup**: erdafitinib vs chemotherapy | Metastatic UC with **FGFR alterations** in Japanese subgroup of THOR | Median **OS 25.4 vs 12.4 months**; median **PFS 8.4 vs 2.9 months**; **ORR 57.1% vs 15.4%** for erdafitinib vs chemotherapy (guercio2023clinicalandgenomic pages 1-2) | Any-grade treatment-related AEs occurred in **all** patients in both arms, but **grade 3/4 AEs** and discontinuations were lower with erdafitinib; **no new safety signals** (guercio2023clinicalandgenomic pages 1-2) | *International Journal of Clinical Oncology* (2024), Matsubara et al. https://doi.org/10.1007/s10147-024-02583-3 |
| **NORSE**: erdafitinib monotherapy vs erdafitinib + cetrelimab | **FGFR2/3-altered** UC | Monotherapy: **ORR 44.2%** (1 CR), median **PFS 5.62 months**. Combination: **ORR 54.5%** (**13.6% CR**), median **PFS 10.97 months**. Median OS not reported in current snippets (benjamin2023treatmentapproachesfor pages 3-4) | Safety details not quantified in current evidence snippets (benjamin2023treatmentapproachesfor pages 3-4) | *Frontiers in Immunology* (2023), Benjamin & Hsu. https://doi.org/10.3389/fimmu.2023.1258388 |
| **Real-world erdafitinib cohort** (Guercio 2023) | Metastatic **FGFR2/3-altered** UC; institutional tumor sequencing and cfDNA monitoring | **ORR 40%** (12/30); median **PFS 2.8 months**; median **OS 6.6 months**. In patients previously treated with immune checkpoint blockade, ORR **35%** (6/17) (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic pages 6-7, guercio2023clinicalandgenomic pages 2-4, guercio2023clinicalandgenomic media 250123eb) | Frequent AEs: **hyperphosphatemia 84%**, **fatigue 59%**, **mucositis 47%**; grade ≥3 mucositis **16%**, palmar-plantar erythrodysesthesia **9%**; dose reductions **38%**, interruptions **50%**, up-titration **16%** (guercio2023clinicalandgenomic pages 6-7) | *Clinical Cancer Research* (2023), Guercio et al. https://doi.org/10.1158/1078-0432.CCR-23-1283 |


*Table: This table summarizes the main FGFR-targeted therapy datasets currently available in the evidence snippets for FGFR-altered urothelial carcinoma. It highlights efficacy, biomarker-defined eligibility, and tolerability across pivotal trials and real-world use.*

**Real‑world implementation challenges**
* Dose reductions and interruptions were common in real-world practice (38% reductions; 50% interruptions) (guercio2023clinicalandgenomic pages 6-7).

### 8.2 Combination approaches (2023–2024 emphasis)
* Erdafitinib + anti–PD-1/PD-L1 approaches are under active study; the NORSE dataset suggests improved ORR and PFS with erdafitinib + cetrelimab compared with monotherapy (ORR 54.5% vs 44.2%; median PFS 10.97 vs 5.62 months) (benjamin2023treatmentapproachesfor pages 3-4).

### 8.3 Experimental FGFR inhibitors and trials (selected; with NCT IDs)
* **TYRA‑300 (FGFR3‑selective)**
  * **NCT06995677**: Phase 2; FGFR3 mutation/fusion; low‑grade intermediate‑risk NMIBC; primary endpoint complete response at 3 months (NCT06995677 chunk 1).
  * **NCT05544552** is described in a 2024 review as Phase I–II TYRA‑300 in advanced UC with activating FGFR3 alterations (~310 patients; endpoints include MTD/RP2D/ORR) (testi2024targetedtherapiesand pages 4-6).
* **Erdafitinib in recurrent non-invasive bladder cancer**
  * **NCT04917809**: oral erdafitinib in recurrent non‑invasive bladder cancer; exclusion criteria include prior FGFR inhibitors and ocular disorders; additional phase/endpoints were not present in the extracted trial text chunk (NCT04917809 chunk 2).
* **Erdafitinib pivotal THOR program**
  * **NCT03390504** is referenced as the THOR program comparing erdafitinib vs chemotherapy and/or pembrolizumab in advanced UC with FGFR alterations (guercio2023clinicalandgenomic pages 1-2, jain2024acomprehensiveoverview pages 8-10).

### 8.4 MAXO (treatment action) term suggestions
* **FGFR inhibitor therapy** (e.g., “treatment with fibroblast growth factor receptor inhibitor”)
* **Immune checkpoint inhibitor therapy** (for combination strategies)
* **Circulating tumor DNA monitoring** (during therapy) (guercio2023clinicalandgenomic pages 2-4)

---

## 9. Prevention / Epidemiology

### 9.1 Epidemiology and demographics
* Bladder cancer is common worldwide; one resource reports in 2020: **573,278 new cases** and **212,536 deaths**, and that bladder cancer is about **three times more frequent in men** and **~80% of patients are older than 65 years** (ferreira2023epimarkersforbladder pages 19-26).
* Urothelial carcinoma accounts for ~**90%** of bladder tumors (ferreira2023epimarkersforbladder pages 26-29, ferreira2023epimarkersforbladder pages 19-26).
* UTUC represents **~5–10% of UCs** and is more aggressive, with ~**60% invasive at diagnosis** (mitiushkina2024useof3′ pages 1-2).

### 9.2 Prevention relevance to FGFR-altered disease
Primary prevention is similar to UC overall because FGFR alterations are **somatic tumor events** arising in the context of UC carcinogenesis.

Primary prevention targets:
* Smoking cessation (major risk factor) (mitiushkina2024useof3′ pages 1-2, ferreira2023epimarkersforbladder pages 19-26)
* Minimizing occupational carcinogen exposure and contaminated water exposure (mitiushkina2024useof3′ pages 1-2)

---

## 10. Other Species / Natural Disease
No cross-species naturally occurring FGFR‑altered UC epidemiology was identified in the extracted evidence.

---

## 11. Model Organisms / Experimental Models

### 11.1 Genetically engineered mouse models (mechanistic and translational)
A 2024 JCI study used a genetically engineered murine model combining **FGFR3S249C activation** with **Trp53R270H** (UPFL) and reported that:
* Tumors “recapitulate papillary histology and LumP/UROMOL class 1 transcriptional states” and that co-alteration yields high-grade NMIBC (okato2024fgfrinhibitionaugments pages 1-2).
* The model showed ICI hyperprogression via Treg expansion, which was abrogated by FGFR inhibition; combined erdafitinib + ICI yielded strong efficacy in mice (okato2024fgfrinhibitionaugments pages 1-2).

### 11.2 Model limitations
Animal models may not capture the full molecular heterogeneity, prior treatment exposures, and sampling discordance seen in human metastatic disease (highlighted in real-world primary vs metastasis discordance) (guercio2023clinicalandgenomic pages 1-2).

---

## 12. Recent developments and expert analysis (2023–2024 emphasis)

### 12.1 Key 2023–2024 advances
1. **Randomized phase III evidence** for erdafitinib vs chemotherapy in FGFR‑altered metastatic UC (THOR) with improved OS, PFS, and ORR (benjamin2023treatmentapproachesfor pages 3-4).
2. **Real‑world genomic/clinical datasets** highlighting short durability, toxicity-driven dose modification, and frequent primary/metastasis discordance (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic pages 6-7).
3. **TME heterogeneity and subtype-specific immunotherapy responses** (e.g., LumP/aFGFR3 showing ORR 50% vs LumP/iFGFR3 5%) and new proposed immune targets (TIM3, IDO1, CCL24) (komura2023theimpactof pages 1-2).
4. **Deployment of AI prescreening** on routine histology to reduce molecular testing burden while maintaining high sensitivity for FGFR3 mutation detection (bannier2024aiallowsprescreening pages 1-2).
5. **RNA-based panels** expanding detection of FGFR3 rearrangements missed by common PCR kits, supporting broader adoption of RNA sequencing for fusion detection (mitiushkina2024useof3′ pages 2-3).

### 12.2 Expert opinions and analysis (authoritative sources)
* Reviews stress that erdafitinib benefit can be **transient**, and overcoming acquired resistance is a major research priority (noeraparast2024fgfr3alterationsin pages 1-2).
* Mechanistic work supports a rationale for combining FGFR inhibition with immunotherapy by modulating immunosuppression (Treg expansion) in FGFR3-mutant contexts (okato2024fgfrinhibitionaugments pages 1-2).

---

## Visual summary: FGFR alteration frequencies across disease settings
The following table consolidates key stage-specific FGFR alteration frequencies from multiple cohorts.

| Setting/stage | Reported FGFR alteration frequency | Alteration types mentioned | Data source (author, journal, year) | Notes |
|---|---:|---|---|---|
| NMIBC | 39% FGFR3-altered; 44% aFGFR3 in Japanese cohort | Recurrent FGFR3 mutations and fusions; FGFR3-mutant disease common in non-invasive/early-stage tumors | Guercio et al., *Clinical Cancer Research*, 2023 (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic media 250123eb); Komura et al., *Molecular Cancer*, 2023 (guercio2023clinicalandgenomic pages 13-14); Bannier et al., *Nature Communications*, 2024 (bannier2024aiallowsprescreening pages 1-2) | Bannier notes FGFR3 mutations can reach up to 80% in non-invasive papillary low-grade tumors, emphasizing strong enrichment in early-stage disease (bannier2024aiallowsprescreening pages 1-2). |
| MIBC | 14% FGFR3-altered; 15% aFGFR3 in Japanese cohort; broadly 10–15% FGFR3-mutant in MIBC/mUC | FGFR3 mutations and fusions | Guercio et al., *Clinical Cancer Research*, 2023 (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic media 250123eb); Komura et al., *Molecular Cancer*, 2023 (guercio2023clinicalandgenomic pages 13-14); Bannier et al., *Nature Communications*, 2024 (bannier2024aiallowsprescreening pages 1-2) | Frequency drops substantially versus NMIBC; Bannier highlights 10–15% average distribution in muscle-invasive and metastatic disease (bannier2024aiallowsprescreening pages 1-2). |
| Localized UTUC | 43% FGFR3-altered in localized upper tract specimens; FGFR2/3 alterations enriched in upper tract vs bladder (48% vs 20% in one RNA-panel cohort) | Predominantly FGFR3 alterations; FGFR2/3 activating point mutations or fusions; FGFR3 rearrangements/fusions detectable by RNA methods | Guercio et al., *Clinical Cancer Research*, 2023 (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic media 250123eb); Mitiushkina et al., *International Journal of Molecular Sciences*, 2024 (mitiushkina2024useof3′ pages 2-3, mitiushkina2024useof3′ pages 1-2) | Upper tract disease appears particularly enriched for FGFR pathway alterations compared with bladder UC in some cohorts (mitiushkina2024useof3′ pages 2-3, mitiushkina2024useof3′ pages 1-2). |
| Metastatic UC | 26% FGFR3-altered metastatic specimens; 10–15% FGFR3-mutant in MIBC/mUC by pathology/AI study | Oncogenic FGFR3 mutations and occasional FGFR2/3 fusions | Guercio et al., *Clinical Cancer Research*, 2023 (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic media 250123eb); Bannier et al., *Nature Communications*, 2024 (bannier2024aiallowsprescreening pages 1-2) | Guercio found 26% positivity in metastatic specimens overall, but paired-sample analysis showed 26% discordance between primary and metachronous metastasis, cautioning against reliance on archival primary tissue alone (guercio2023clinicalandgenomic pages 1-2, guercio2023clinicalandgenomic pages 2-4). |
| mUC metastatic biopsy cohort | FGFR3 actionable target in 26% of metastatic biopsies | FGFR3 most common actionable target; includes mutations and at least some fusions in metastatic profiling studies | Loriot et al., *Nature Communications*, 2024 (antar2024theevolvingmolecular pages 3-5) | In a metastatic biopsy multi-omics cohort, potential therapeutic targets were found in 73% overall, with FGFR3 the most common at 26%, supporting routine metastatic-site profiling when feasible (antar2024theevolvingmolecular pages 3-5). |


*Table: This table summarizes reported FGFR alteration frequencies across urothelial carcinoma disease settings using only the cited evidence. It highlights stage dependence, upper-tract enrichment, and the clinically important discordance between primary and metastatic tumors.*

---

## Key limitations of this evidence package (important for KB curation)
* A dedicated **MONDO/MeSH/ICD identifier** for “FGFR‑altered UC” was not established in the retrieved evidence; the subtype is best represented as **urothelial carcinoma** with a **biomarker attribute**.
* Several guideline-level resources (e.g., NCCN/EAU) and FDA label documents were not directly retrieved here; companion diagnostic claims are therefore cited from peer‑reviewed sources that mention therascreen as the companion diagnostic (bannier2024aiallowsprescreening pages 2-3, jain2024acomprehensiveoverview pages 8-10).
* Symptom frequencies specifically in **FGFR‑altered** vs **FGFR‑wildtype** UC were not available in extracted evidence; phenotypes are described at the UC level.


References

1. (guercio2023clinicalandgenomic pages 2-4): Brendan J. Guercio, Michal Sarfaty, Min Yuen Teo, Neha Ratna, Cihan Duzgol, Samuel A. Funt, Chung-Han Lee, David H. Aggen, Ashley M. Regazzi, Ziyu Chen, Michael Lattanzi, Hikmat A. Al-Ahmadie, A. Rose Brannon, Ronak Shah, Carissa Chu, Andrew T. Lenis, Eugene Pietzak, Bernard H. Bochner, Michael F. Berger, David B. Solit, Jonathan E. Rosenberg, Dean F. Bajorin, and Gopa Iyer. Clinical and genomic landscape of fgfr3-altered urothelial carcinoma and treatment outcomes with erdafitinib: a real-world experience. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4586-4595, Sep 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1283, doi:10.1158/1078-0432.ccr-23-1283. This article has 62 citations.

2. (testi2024targetedtherapiesand pages 11-13): Irene Testi, Giulia Claire Giudice, Giuseppe Salfi, Martino Pedrani, Sara Merler, Fabio Turco, Luigi Tortola, and Ursula Vogl. Targeted therapies and molecular targets in the therapeutic landscape of advanced urothelial carcinoma: state of the art and future perspectives. Exploration of Targeted Anti-tumor Therapy, 5:1326-1364, Nov 2024. URL: https://doi.org/10.37349/etat.2024.00279, doi:10.37349/etat.2024.00279. This article has 3 citations.

3. (benjamin2023treatmentapproachesfor pages 3-4): David J. Benjamin and Robert Hsu. Treatment approaches for fgfr-altered urothelial carcinoma: targeted therapies and immunotherapy. Frontiers in Immunology, Aug 2023. URL: https://doi.org/10.3389/fimmu.2023.1258388, doi:10.3389/fimmu.2023.1258388. This article has 18 citations and is from a peer-reviewed journal.

4. (guercio2023clinicalandgenomic pages 6-7): Brendan J. Guercio, Michal Sarfaty, Min Yuen Teo, Neha Ratna, Cihan Duzgol, Samuel A. Funt, Chung-Han Lee, David H. Aggen, Ashley M. Regazzi, Ziyu Chen, Michael Lattanzi, Hikmat A. Al-Ahmadie, A. Rose Brannon, Ronak Shah, Carissa Chu, Andrew T. Lenis, Eugene Pietzak, Bernard H. Bochner, Michael F. Berger, David B. Solit, Jonathan E. Rosenberg, Dean F. Bajorin, and Gopa Iyer. Clinical and genomic landscape of fgfr3-altered urothelial carcinoma and treatment outcomes with erdafitinib: a real-world experience. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4586-4595, Sep 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1283, doi:10.1158/1078-0432.ccr-23-1283. This article has 62 citations.

5. (bannier2024aiallowsprescreening pages 1-2): Pierre-Antoine Bannier, Charlie Saillard, Philipp Mann, Maxime Touzot, Charles Maussion, Christian Matek, Niklas Klümper, Johannes Breyer, Ralph Wirtz, Danijel Sikic, Bernd Schmitz-Dräger, Bernd Wullich, Arndt Hartmann, Sebastian Försch, and Markus Eckstein. Ai allows pre-screening of fgfr3 mutational status using routine histology slides of muscle-invasive bladder cancer. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55331-6, doi:10.1038/s41467-024-55331-6. This article has 20 citations and is from a highest quality peer-reviewed journal.

6. (antar2024theevolvingmolecular pages 3-5): Ryan Michael Antar, Christopher Fawaz, Diego Gonzalez, Vincent Eric Xu, Arthur Pierre Drouaud, Jason Krastein, Faozia Pio, Andeulazia Murdock, Kirolos Youssef, Stanislav Sobol, and Michael J. Whalen. The evolving molecular landscape and actionable alterations in urologic cancers. Current Oncology, 31:6909-6937, Nov 2024. URL: https://doi.org/10.3390/curroncol31110511, doi:10.3390/curroncol31110511. This article has 5 citations.

7. (shang2024landscapeoftargeted pages 3-5): Shihao Shang, Lei Zhang, Kepu Liu, Maoxin Lv, Jie Zhang, Dongen Ju, Di Wei, Zelong Sun, Pinxiao Wang, Jianlin Yuan, and Zheng Zhu. Landscape of targeted therapies for advanced urothelial carcinoma. Exploration of Targeted Anti-tumor Therapy, 5:641-677, Jun 2024. URL: https://doi.org/10.37349/etat.2024.00240, doi:10.37349/etat.2024.00240. This article has 5 citations.

8. (guercio2023clinicalandgenomic pages 1-2): Brendan J. Guercio, Michal Sarfaty, Min Yuen Teo, Neha Ratna, Cihan Duzgol, Samuel A. Funt, Chung-Han Lee, David H. Aggen, Ashley M. Regazzi, Ziyu Chen, Michael Lattanzi, Hikmat A. Al-Ahmadie, A. Rose Brannon, Ronak Shah, Carissa Chu, Andrew T. Lenis, Eugene Pietzak, Bernard H. Bochner, Michael F. Berger, David B. Solit, Jonathan E. Rosenberg, Dean F. Bajorin, and Gopa Iyer. Clinical and genomic landscape of fgfr3-altered urothelial carcinoma and treatment outcomes with erdafitinib: a real-world experience. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4586-4595, Sep 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1283, doi:10.1158/1078-0432.ccr-23-1283. This article has 62 citations.

9. (shan2024moleculartargetingof pages 4-5): Khine S. Shan, Shivani Dalal, Nyein Nyein Thaw Dar, Omani McLish, Matthew Salzberg, and Brian A. Pico. Molecular targeting of the fibroblast growth factor receptor pathway across various cancers. International Journal of Molecular Sciences, 25:849, Jan 2024. URL: https://doi.org/10.3390/ijms25020849, doi:10.3390/ijms25020849. This article has 24 citations.

10. (mitiushkina2024useof3′ pages 1-2): Natalia V. Mitiushkina, Vladislav I. Tiurin, Aleksandra A. Anuskina, Natalia A. Bordovskaya, Ekaterina A. Nalivalkina, Darya M. Terina, Mariya V. Berkut, Anna D. Shestakova, Maria V. Syomina, Ekaterina Sh. Kuligina, Alexandr V. Togo, and Evgeny N. Imyanitov. Use of 3′ rapid amplification of cdna ends (3′ race)-based targeted rna sequencing for profiling of druggable genetic alterations in urothelial carcinomas. International Journal of Molecular Sciences, 25:12126, Nov 2024. URL: https://doi.org/10.3390/ijms252212126, doi:10.3390/ijms252212126. This article has 1 citations.

11. (ferreira2023epimarkersforbladder pages 19-26): MFS Ferreira. Epimarkers for bladder cancer diagnosis and monitoring (epiblac). Unknown journal, 2023.

12. (ferreira2023epimarkersforbladder pages 26-29): MFS Ferreira. Epimarkers for bladder cancer diagnosis and monitoring (epiblac). Unknown journal, 2023.

13. (komura2023theimpactof pages 1-2): Kazumasa Komura, Kensuke Hirosuna, Satoshi Tokushige, Takuya Tsujino, Kazuki Nishimura, Mitsuaki Ishida, Takuo Hayashi, Ayako Ura, Takaya Ohno, Shogo Yamazaki, Keita Nakamori, Shoko Kinoshita, Ryoichi Maenosono, Masahiko Ajiro, Yuki Yoshikawa, Tomoaki Takai, Takeshi Tsutsumi, Kohei Taniguchi, Tomohito Tanaka, Kiyoshi Takahara, Tsuyoshi Konuma, Teruo Inamoto, Yoshinobu Hirose, Fumihito Ono, Yuichi Shiraishi, Akihide Yoshimi, and Haruhito Azuma. The impact of fgfr3 alterations on the tumor microenvironment and the efficacy of immune checkpoint inhibitors in bladder cancer. Molecular Cancer, Nov 2023. URL: https://doi.org/10.1186/s12943-023-01897-6, doi:10.1186/s12943-023-01897-6. This article has 50 citations and is from a highest quality peer-reviewed journal.

14. (mitiushkina2024useof3′ pages 2-3): Natalia V. Mitiushkina, Vladislav I. Tiurin, Aleksandra A. Anuskina, Natalia A. Bordovskaya, Ekaterina A. Nalivalkina, Darya M. Terina, Mariya V. Berkut, Anna D. Shestakova, Maria V. Syomina, Ekaterina Sh. Kuligina, Alexandr V. Togo, and Evgeny N. Imyanitov. Use of 3′ rapid amplification of cdna ends (3′ race)-based targeted rna sequencing for profiling of druggable genetic alterations in urothelial carcinomas. International Journal of Molecular Sciences, 25:12126, Nov 2024. URL: https://doi.org/10.3390/ijms252212126, doi:10.3390/ijms252212126. This article has 1 citations.

15. (okato2024fgfrinhibitionaugments pages 1-2): Atsushi Okato, Takanobu Utsumi, Michela Ranieri, Xingnan Zheng, Mi Zhou, Luiza D. Pereira, Ting Chen, Yuki Kita, Di Wu, Hyesun Hyun, Hyojin Lee, Andrew S. Gdowski, John D. Raupp, Sean Clark-Garvey, Ujjawal Manocha, Alison Chafitz, Fiona Sherman, Janaye Stephens, Tracy L. Rose, Matthew I. Milowsky, Sara E. Wobker, Jonathan S. Serody, Jeffrey S. Damrauer, Kwok-Kin Wong, and William Y. Kim. Fgfr inhibition augments anti–pd-1 efficacy in murine fgfr3-mutant bladder cancer by abrogating immunosuppression. The Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci169241, doi:10.1172/jci169241. This article has 32 citations.

16. (bannier2024aiallowsprescreening pages 2-3): Pierre-Antoine Bannier, Charlie Saillard, Philipp Mann, Maxime Touzot, Charles Maussion, Christian Matek, Niklas Klümper, Johannes Breyer, Ralph Wirtz, Danijel Sikic, Bernd Schmitz-Dräger, Bernd Wullich, Arndt Hartmann, Sebastian Försch, and Markus Eckstein. Ai allows pre-screening of fgfr3 mutational status using routine histology slides of muscle-invasive bladder cancer. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55331-6, doi:10.1038/s41467-024-55331-6. This article has 20 citations and is from a highest quality peer-reviewed journal.

17. (jain2024acomprehensiveoverview pages 8-10): Nem Kumar Jain, Mukul Tailang, Neelaveni Thangavel, Hafiz A. Makeen, Mohammed Albratty, Asim Najmi, Hassan Ahmad Alhazmi, Khalid Zoghebi, Muthumanickam Alagusundaram, Hemant Kumar Jain, and Balakumar Chandrasekaran. A comprehensive overview of selective and novel fibroblast growth factor receptor inhibitors as a potential anticancer modality. Acta Pharmaceutica, 74:1-36, Mar 2024. URL: https://doi.org/10.2478/acph-2024-0005, doi:10.2478/acph-2024-0005. This article has 7 citations and is from a peer-reviewed journal.

18. (guercio2023clinicalandgenomic media 250123eb): Brendan J. Guercio, Michal Sarfaty, Min Yuen Teo, Neha Ratna, Cihan Duzgol, Samuel A. Funt, Chung-Han Lee, David H. Aggen, Ashley M. Regazzi, Ziyu Chen, Michael Lattanzi, Hikmat A. Al-Ahmadie, A. Rose Brannon, Ronak Shah, Carissa Chu, Andrew T. Lenis, Eugene Pietzak, Bernard H. Bochner, Michael F. Berger, David B. Solit, Jonathan E. Rosenberg, Dean F. Bajorin, and Gopa Iyer. Clinical and genomic landscape of fgfr3-altered urothelial carcinoma and treatment outcomes with erdafitinib: a real-world experience. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4586-4595, Sep 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1283, doi:10.1158/1078-0432.ccr-23-1283. This article has 62 citations.

19. (NCT06995677 chunk 1):  Efficacy and Safety of TYRA-300 in Participants With FGFR3 Altered Low Grade, Intermediate Risk Non-Muscle Invasive Bladder Cancer. Tyra Biosciences, Inc. 2025. ClinicalTrials.gov Identifier: NCT06995677

20. (testi2024targetedtherapiesand pages 4-6): Irene Testi, Giulia Claire Giudice, Giuseppe Salfi, Martino Pedrani, Sara Merler, Fabio Turco, Luigi Tortola, and Ursula Vogl. Targeted therapies and molecular targets in the therapeutic landscape of advanced urothelial carcinoma: state of the art and future perspectives. Exploration of Targeted Anti-tumor Therapy, 5:1326-1364, Nov 2024. URL: https://doi.org/10.37349/etat.2024.00279, doi:10.37349/etat.2024.00279. This article has 3 citations.

21. (NCT04917809 chunk 2):  A Study of Oral Erdafitinib in People With Recurrent Non-Invasive Bladder Cancer. Memorial Sloan Kettering Cancer Center. 2022. ClinicalTrials.gov Identifier: NCT04917809

22. (noeraparast2024fgfr3alterationsin pages 1-2): Maxim Noeraparast, Katarina Krajina, Renate Pichler, Dora Niedersüß‐Beke, Shahrokh F Shariat, Viktor Grünwald, Sascha Ahyai, and Martin Pichler. Fgfr3 alterations in bladder cancer: sensitivity and resistance to targeted therapies. Cancer Communications, 44:1189-1208, Aug 2024. URL: https://doi.org/10.1002/cac2.12602, doi:10.1002/cac2.12602. This article has 26 citations.

23. (guercio2023clinicalandgenomic pages 13-14): Brendan J. Guercio, Michal Sarfaty, Min Yuen Teo, Neha Ratna, Cihan Duzgol, Samuel A. Funt, Chung-Han Lee, David H. Aggen, Ashley M. Regazzi, Ziyu Chen, Michael Lattanzi, Hikmat A. Al-Ahmadie, A. Rose Brannon, Ronak Shah, Carissa Chu, Andrew T. Lenis, Eugene Pietzak, Bernard H. Bochner, Michael F. Berger, David B. Solit, Jonathan E. Rosenberg, Dean F. Bajorin, and Gopa Iyer. Clinical and genomic landscape of fgfr3-altered urothelial carcinoma and treatment outcomes with erdafitinib: a real-world experience. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:4586-4595, Sep 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1283, doi:10.1158/1078-0432.ccr-23-1283. This article has 62 citations.
