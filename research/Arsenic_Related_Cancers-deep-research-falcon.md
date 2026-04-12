---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T12:22:16.904551'
end_time: '2026-04-05T12:37:54.372154'
duration_seconds: 937.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arsenic-Related Cancers
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arsenic-Related Cancers
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Arsenic-Related Cancers** covering all of the
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
- **Disease Name:** Arsenic-Related Cancers
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Arsenic-Related Cancers** covering all of the
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


# Arsenic‑Related Cancers — Comprehensive Research Report (2023–2024 prioritized)

## Target disease
- **Disease name:** Arsenic‑Related Cancers (malignancies causally or strongly associated with chronic **inorganic arsenic (iAs)** exposure)
- **MONDO ID:** Not retrievable from the provided tool-accessible corpus (see “Identifiers gap” below)
- **Category:** Environmentally induced cancers / toxicant-associated cancers

### Executive summary
Chronic exposure to inorganic arsenic—most importantly through contaminated drinking water—is classified by IARC as **carcinogenic to humans (Group 1)** and is most consistently and causally linked to **lung, urinary bladder, and skin cancers**. Contemporary evidence also supports **kidney cancer** risk and provides mixed but concerning evidence for **digestive/hepatobiliary cancers**. A 2023 Bayesian meta-analysis update quantified increased bladder and kidney cancer risks at concentrations near the WHO guideline of **10 µg/L**, and real-world mitigation studies show cancer risks can decline after switching populations from arsenic-contaminated wells to municipal water supplies, albeit with long latency. Mechanistically, arsenic carcinogenesis is increasingly framed as a convergence of **oxidative stress**, **DNA damage response (DDR) disruption**, **epigenetic/epitranscriptomic reprogramming**, and **pro‑tumorigenic cellular senescence/SASP signaling**, with susceptibility influenced by arsenic metabolism efficiency (e.g., **AS3MT locus**) and tumor suppressor context (e.g., **TP53**) (issanov2023arsenicindrinking pages 1-2, gu2024researchprogresson pages 1-2, nail2023arsenicandhuman pages 6-8).

---

## 1. Disease information

### 1.1 What is the disease?
“Arsenic‑related cancers” is best treated as a **disease group**: cancers in which chronic iAs exposure (typically over years to decades) is a major etiologic contributor. The best-established cancer sites are **lung, bladder, and skin**, with additional sites under active investigation (kidney, hepatobiliary/digestive) (nuvolone2023longtermexposureto pages 1-2, kasmi2023carcinogeniceffectof pages 1-2, issanov2023arsenicindrinking pages 1-2).

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
- **MeSH terminology (available in corpus):** A 2023 systematic review update explicitly reports its search using MeSH/free-text terms including **“arsenic”, “bladder cancer”, “kidney cancer”, “urinary tract cancer”, “carcinoma, renal cell”** and water exposure terms (issanov2023arsenicindrinking pages 2-4).
- **ICD codes:** The same review states it extracted **International Classification of Diseases code** information when available, but the excerpted text does not list specific ICD‑10/ICD‑11 codes (issanov2023arsenicindrinking pages 2-4).
- **MONDO / OMIM / Orphanet:** Not available in the retrieved corpus; this is an **evidence gap** for knowledge-base population using only the current tools (issanov2023arsenicindrinking pages 2-4).

### 1.3 Common synonyms / alternative names
- Arsenic-induced cancers; arsenicosis-associated cancers; iAs-associated cancers.
- Site-specific: arsenic-associated **non‑melanoma skin cancer (NMSC)**; arsenic-associated bladder cancer; arsenic-associated lung cancer (jasmine2024molecularprofilingand pages 1-2, issanov2023arsenicindrinking pages 1-2).

### 1.4 Evidence source type
This report is derived from **aggregated disease-level resources** (systematic reviews, cohorts, mechanistic studies), not from EHR-based individual patient narratives (issanov2023arsenicindrinking pages 1-2, nuvolone2023longtermexposureto pages 1-2, jasmine2024molecularprofilingand pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factor:** chronic **inorganic arsenic** exposure, especially via **drinking water**.
- Drinking water is repeatedly described as the “primary route of exposure” for highly exposed populations (issanov2023arsenicindrinking pages 1-2).
- iAs in drinking water is IARC Group 1 carcinogen (nuvolone2023longtermexposureto pages 1-2, issanov2023arsenicindrinking pages 1-2).

**Other exposure sources:** food, occupational inhalation/dermal exposure (mining/smelting/industrial), and tobacco as a co-exposure (kasmi2023carcinogeniceffectof pages 1-2, nuvolone2023longtermexposureto pages 1-2).

### 2.2 Risk factors

#### Environmental
- **Drinking water concentration:** A 2023 Bayesian meta-analysis update provides modeled dose–response RRs for bladder and kidney cancer incidence at **10, 50, 150 µg/L** (issanov2023arsenicindrinking pages 1-2, issanov2023arsenicindrinking pages 33-35). Visual dose–response summaries are provided in Table 7 / Figures 3–4 (issanov2023arsenicindrinking media 90db8dee, issanov2023arsenicindrinking media f21eb48e, issanov2023arsenicindrinking media a0cd84bc).
- **Geogenic high-arsenic groundwater regions** (e.g., Bangladesh/Taiwan/Chile/Argentina) repeatedly appear in modern evidence bases (nuvolone2023longtermexposureto pages 1-2, issanov2023arsenicindrinking pages 1-2).

#### Lifestyle / co-exposure
- **Cigarette smoking:** described as exacerbating urinary-tract cancer risks when combined with arsenic exposure (issanov2023arsenicindrinking pages 1-2).

#### Genetic susceptibility (selected)
- **Arsenic metabolism efficiency locus near AS3MT (10q24.32):** inherited variation near **AS3MT** is associated with urine-based measures of arsenic metabolism efficiency, which in turn is associated with arsenic-related toxicities (issanov2023arsenicindrinking pages 42-43).
- **TP53 context:** arsenite-induced methylation responses are strongly altered when p53 is knocked out/mutant in cell models (chung2024sodiumarseniteinduceddna pages 1-2).

### 2.3 Protective factors
Direct genetic “protective variants” are not established in the retrieved corpus. However, **exposure reduction** through mitigation is consistently protective at the population level (see Prevention section) (su2011reductioninarsenic pages 1-2, seow2012arsenicreductionin pages 1-1).

### 2.4 Gene–environment interactions
- **TP53 × arsenite:** p53 knockout in MCF7 cells markedly exacerbates arsenite-associated DNA methylation alterations, suggesting tumor suppressor status can modulate epigenetic responses to arsenic (chung2024sodiumarseniteinduceddna pages 1-2).
- **Smoking × arsenic:** co-exposure increases urinary-tract cancer risk beyond arsenic alone (issanov2023arsenicindrinking pages 1-2).

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Core cancer phenotypes by organ
- **Urinary tract cancers (bladder, kidney):** principal downstream phenotype of chronic iAs exposure, biologically plausible because most ingested arsenic is excreted in urine (issanov2023arsenicindrinking pages 1-2).
- **Lung cancer:** increased risk and hospitalization in populations exposed to iAs in drinking water (nuvolone2023longtermexposureto pages 1-2).
- **Non‑melanoma skin cancer (BCC/SCC):** explicitly associated with iAs exposure; cohort incidence reported in exposed adults (jasmine2024molecularprofilingand pages 1-2).

### 3.2 Precancerous and systemic arsenicosis phenotypes (important for screening)
Skin manifestations are repeatedly emphasized as early indicators and precursors of later cancers:
- “**Skin lesions are the first visible symptom**” of chronic arsenic exposure and are precursors to arsenic-induced skin cancers (seow2012arsenicreductionin pages 1-1).
- **Hyperpigmentation** (“raindrops on a dusty road” description), **palmoplantar hyperkeratosis/arsenical keratosis**, with progression to Bowen disease/SCC described (thankachan2023exploringtheinterplay pages 3-5, thankachan2023exploringtheinterplay pages 5-7).
- Quantitative examples: “raindrop pigmentation occurred in **71%** of 110 suspected patients” in one series; leukomelanosis ~1/3 (ganie2024arsenictoxicitysources pages 11-13).

### 3.3 Temporal development
- Early cutaneous changes can appear after “**six months to two years or more**” of continuous exposure (ganie2024arsenictoxicitysources pages 11-13).
- Longer latencies are reported for cancer development: skin changes and cancers may take decades (reports of **>20 years** for manifestation and up to **30 years** for skin cancer after exposure) (thankachan2023exploringtheinterplay pages 5-7).
- Elevated cancer mortality can persist for decades after exposure cessation (not quantified in detail here, but noted in mitigation-focused and review contexts) (pullella2024elucidatingtherelationshipa pages 24-28).

### 3.4 Suggested ontology mappings (examples)
**HPO (phenotypes):**
- Hyperpigmentation (HP:0000953)
- Hypopigmentation (HP:0001029)
- Palmoplantar keratoderma / hyperkeratosis (HP:0000972 / HP:0000962)
- Alopecia (HP:0001596)
- Mees lines (leukonychia striata; HP:0032434)
- Bladder carcinoma (HP:0030071)
- Lung carcinoma (HP:0012125)
- Basal cell carcinoma (HP:0006744)
- Squamous cell carcinoma (HP:0012129)

(These mappings are ontology suggestions; they are not explicitly enumerated in the retrieved papers.)

---

## 4. Genetic / molecular information

### 4.1 Key molecular concepts (current understanding)
Arsenic carcinogenesis is increasingly treated as a **multifactorial, largely non‑mutagenic (or weakly mutagenic) carcinogen** that drives cancer through:
- **Oxidative stress/ROS** → DNA damage and signaling dysregulation (jasmine2024molecularprofilingand pages 1-2, gu2024researchprogresson pages 2-3).
- **DNA repair inhibition / DDR disruption** and error-prone repair (e.g., arsenic can inhibit ATM autophosphorylation and CHEK2 signaling despite DSB accumulation) (nail2023arsenicandhuman pages 4-6).
- **Epigenetic and epitranscriptomic reprogramming** (DNA methylation changes; histone mark perturbations; noncoding RNA dysregulation; RNA m6A modifications) (nail2023arsenicandhuman pages 6-8, nail2023arsenicandhuman pages 4-6).
- **Cellular senescence and SASP** signaling (pro-inflammatory and tissue-remodeling secretome contributing to cancer progression) (gu2024researchprogresson pages 1-2, gu2024researchprogresson pages 2-3).

### 4.2 Causal/susceptibility genes and pathways (selected)
- **AS3MT region (10q24.32):** genetic variation near **AS3MT** influences arsenic metabolism efficiency in multiple exposed populations (issanov2023arsenicindrinking pages 42-43).
- **TP53:** (i) a key mutated gene in arsenic-associated SCC in NMSC profiling; (ii) modulates arsenite-driven methylation changes in experimental systems (jasmine2024molecularprofilingand pages 1-2, chung2024sodiumarseniteinduceddna pages 1-2).
- **Hedgehog signaling pathway genes (e.g., PTCH1):** frequently mutated in BCC from arsenic-exposed NMSC, with downstream pathway expression effects (jasmine2024molecularprofilingand pages 1-2).
- **NOTCH1:** top-mutated gene in BCC in arsenic-exposed NMSC (jasmine2024molecularprofilingand pages 1-2).

### 4.3 Somatic mutation / transcriptomic profiling in an exposed population (2024)
In a Bangladeshi arsenic-exposed cohort with 6-year follow-up (n≈7000), NMSC molecular profiling found top mutated genes (PTCH1, NOTCH1, SYNE1, PKHD1 in BCC; TP53 in SCC). Non-synonymous mutations influenced differential expression of pathways including hedgehog, NOTCH, IL‑17, p53, and Wnt signaling (jasmine2024molecularprofilingand pages 1-2).

### 4.4 Epigenetics and RNA modifications (2023–2024)
- **Cell senescence review (2024):** arsenic induces senescence via “epigenetic alterations,” SASP, telomere shortening, and mitochondrial dysfunction (gu2024researchprogresson pages 1-2).
- **p53-dependent methylation changes (2024):** arsenite exposure produces DNA methylation alterations that are “exacerbated by p53 knockout,” with CpG hypermethylation and LINE‑1 global demethylation patterns described (chung2024sodiumarseniteinduceddna pages 1-2).
- **Mechanistic review (2023):** highlights new molecular mechanisms including noncoding RNAs and m6A RNA modifications; DDR inhibition via ATM/CHEK2 suppression is emphasized (nail2023arsenicandhuman pages 4-6).

### 4.5 Suggested GO/CL ontology mappings (examples)
**GO biological process (examples):**
- Response to oxidative stress (GO:0006979)
- DNA repair (GO:0006281)
- Double-strand break repair via nonhomologous end joining (GO:0006303)
- Cellular senescence (GO:0090398)
- Inflammatory response (GO:0006954)
- Regulation of NF‑κB signaling (GO:0043122)

**Cell Ontology (examples):**
- Keratinocyte (CL:0000312)
- Melanocyte (CL:0000148)
- Urothelial cell (CL:0000454)
- Alveolar epithelial cell type II (CL:0002063)

(These are suggestions based on described tissues/cell types; not enumerated explicitly in the retrieved texts.)

---

## 5. Environmental information

### 5.1 Environmental factors
- **Inorganic arsenic in drinking water** is the dominant exposure route in high-burden settings; endemic regions include Bangladesh, Taiwan, Argentina, Chile and parts of the US (nuvolone2023longtermexposureto pages 1-2, issanov2023arsenicindrinking pages 1-2).

### 5.2 Lifestyle factors
- **Smoking** is an important co-risk factor that can amplify arsenic-associated urinary tract cancer risk (issanov2023arsenicindrinking pages 1-2).

### 5.3 Infectious agents
No infectious etiologies are required for arsenic-related carcinogenesis; infectious co-factors (e.g., HBV/HCV for liver cancer) are plausible confounders but not addressed in the retrieved excerpts.

---

## 6. Mechanism / pathophysiology (causal chain)

### 6.1 Canonical causal chain
1. **Exposure**: chronic ingestion of iAs via drinking water (issanov2023arsenicindrinking pages 1-2).
2. **Biotransformation & distribution**: hepatic metabolism and urinary excretion concentrate arsenic/metabolites in urinary tract; methylation can consume SAM (methyl donor) influencing epigenetic state (chung2024sodiumarseniteinduceddna pages 1-2, issanov2023arsenicindrinking pages 1-2).
3. **Molecular injury**:
   - ROS/oxidative stress and mitochondrial dysfunction (gu2024researchprogresson pages 2-3, jasmine2024molecularprofilingand pages 1-2).
   - DDR inhibition and misrepair (ATM/CHEK2 suppression; error-prone NHEJ shift) (nail2023arsenicandhuman pages 4-6, nail2023arsenicandhuman pages 6-8).
   - Epigenetic/epitranscriptomic reprogramming (DNA methylation, histone marks, miRNAs, m6A) (chung2024sodiumarseniteinduceddna pages 1-2, nail2023arsenicandhuman pages 6-8).
   - Senescence and SASP → chronic inflammation/tissue remodeling (GATA4–NF‑κB; p38/JNK; ERK/CEBPB) (gu2024researchprogresson pages 1-2, gu2024researchprogresson pages 2-3).
4. **Cellular/tissue remodeling**: altered proliferation, immune dysregulation, potential stem-cell reprogramming in bladder epithelium (issanov2023arsenicindrinking pages 1-2).
5. **Clinical outcomes**: site-specific cancers (bladder/kidney/lung/skin) often after long latency (su2011reductioninarsenic pages 1-2, thankachan2023exploringtheinterplay pages 5-7).

---

## 7. Anatomical structures affected

### 7.1 Organ level
- **Skin** (precancerous keratoses → Bowen disease/SCC/BCC) (thankachan2023exploringtheinterplay pages 5-7, jasmine2024molecularprofilingand pages 1-2)
- **Urinary bladder and kidney** (urinary tract cancers) (issanov2023arsenicindrinking pages 1-2)
- **Lung** (lung cancer; increased hospitalization risk in cohort) (nuvolone2023longtermexposureto pages 1-2)
- **Liver/hepatobiliary system** (emerging evidence for HPB malignancies) (kasmi2023carcinogeniceffectof pages 1-2)

### 7.2 Tissue/cell level
- **Epidermal keratinocytes** and melanocyte-related pigmentation pathways (jasmine2024molecularprofilingand pages 1-2, ganie2024arsenictoxicitysources pages 11-13)
- **Urothelium** (bladder epithelial targets; stem-cell reprogramming hypotheses) (issanov2023arsenicindrinking pages 1-2)

### 7.3 Subcellular level
- **Mitochondria**: arsenic-associated ROS, mitochondrial membrane potential disruption, cytochrome c release (gu2024researchprogresson pages 2-3).
- **Nucleus/chromatin**: arsenite-associated DNA methylation remodeling and LINE‑1 changes (chung2024sodiumarseniteinduceddna pages 1-2).

---

## 8. Temporal development

### 8.1 Onset pattern
- Chronic/insidious; precancerous skin phenotypes may appear after months to years of sustained exposure (ganie2024arsenictoxicitysources pages 11-13).

### 8.2 Progression and latency
- Cancer development often manifests after long latency (decades in some narratives); mitigation shows declines in lung/bladder risk over cohorts but persistent excess risk is possible (su2011reductioninarsenic pages 1-2, thankachan2023exploringtheinterplay pages 5-7).

---

## 9. Inheritance and population

### 9.1 Inheritance
Not a Mendelian disease; arsenic-related cancers are **multifactorial**, with genetic susceptibility (e.g., metabolism efficiency loci near AS3MT) modifying risk (issanov2023arsenicindrinking pages 42-43).

### 9.2 Population exposure burden (selected recent quantitative statements)
- A 2024 senescence systematic review notes “over **220 million** people worldwide” affected by harmful effects of long-term iAs exposure (gu2024researchprogresson pages 1-2).
- A 2023 digestive-cancer systematic review reports As-contaminated drinking water in **108 countries**, affecting ~**40 million** above WHO limits (kasmi2023carcinogeniceffectof pages 1-2).

---

## 10. Diagnostics

### 10.1 Exposure assessment (real-world practice)
- **Water testing** (tube wells/municipal supplies) is central to mitigation programs (seow2012arsenicreductionin pages 1-1).
- **Biomarkers**:
  - **Urinary arsenic** (often speciation-based) is emphasized as important because arsenic is predominantly excreted via urine (issanov2023arsenicindrinking pages 1-2).
  - **Toenail arsenic** used for longer-term exposure and shown to track lesion recovery in Bangladesh (seow2012arsenicreductionin pages 1-1).
  - **Hair/nail** arsenic as long-term exposure biomarkers; careful handling required due to external contamination (thankachan2023exploringtheinterplay pages 5-7).
  - **Urinary NAG** as marker of proximal tubular injury (ganie2024arsenictoxicitysources pages 11-13).

### 10.2 Guideline thresholds used in practice
- **WHO guideline / MAC:** **10 µg/L** arsenic in drinking water (issanov2023arsenicindrinking pages 1-2, seow2012arsenicreductionin pages 1-1).
- **Bangladesh standard:** **50 µg/L** (used to prioritize mitigation in Seow et al.) (seow2012arsenicreductionin pages 1-1).

### 10.3 Cancer diagnostics
Cancer diagnosis follows site-standard practice (histopathology, imaging, staging). No arsenic-specific diagnostic criteria were retrievable from the provided corpus.

---

## 11. Outcome / prognosis

### 11.1 Population-level outcomes (recent cohort data)
- Italy residential cohort: exposure **>10 µg/L** associated with malignant neoplasm hospitalization HR **1.10** (1.02–1.19) and lung cancer hospitalization HR **1.85** (1.14–3.02) (nuvolone2023longtermexposureto pages 1-2).

### 11.2 Precancerous lesion outcomes after exposure reduction
- Bangladesh follow-up: **41%** reduction in water arsenic; **65** lesion cases resolved; log10 decreases in exposure associated with improved recovery and severity scores (seow2012arsenicreductionin pages 1-1).

---

## 12. Treatment

### 12.1 Cancer treatment (current real-world implementation)
Treatment is **standard-of-care by cancer site** (e.g., surgery, radiotherapy, systemic therapy). The retrieved corpus does not provide arsenic-specific treatment algorithms for these solid tumors.

### 12.2 Supportive and preventive treatment of arsenicosis phenotypes
Primary “treatment” is **exposure cessation/reduction** and monitoring for premalignant lesions (seow2012arsenicreductionin pages 1-1, huang2015thehealtheffects pages 11-14).

### 12.3 Suggested MAXO terms (examples)
- Water quality intervention / safe drinking water provision (MAXO:0000930 – placeholder; exact MAXO IDs should be validated during ontology curation)
- Environmental exposure reduction (MAXO concept)
- Cancer screening (MAXO concept)

(MAXO IDs were not available in the retrieved texts and should be validated against the MAXO ontology.)

---

## 13. Prevention (current applications and real-world implementation)

### 13.1 Primary prevention: reduce exposure
- **Municipal tap water substitution** (Taiwan): Following municipal water installation in the 1970s, bladder cancer RR in an endemic region declined from ~20 to 5 across cohorts; lung cancer RR declined from ~8 to ~1.5–2, with registry-based analyses spanning 1979–2003 (su2011reductioninarsenic pages 1-2, su2011reductioninarsenic pages 2-4).
- **Community/household mitigation** (Bangladesh): tube-well testing/labeling, alternative safe sources, point-of-use filters, dug wells, and rainwater harvesting; associated with measurable exposure reductions and skin lesion improvement within ~10 years (seow2012arsenicreductionin pages 1-1).

### 13.2 Technology options (household/community)
A systematic review of 50 field technologies found heterogeneous effectiveness; adsorption and zero‑valent iron approaches showed more persuasive performance, often with **≥95%** effluent samples meeting WHO guideline in some studies, though evidence quality was generally weak (joneshughes2013areinterventionsto pages 1-2, joneshughes2013areinterventionsto pages 13-14).

### 13.3 Secondary prevention: screening and early detection
A geographic review emphasizes monitoring for early signs (skin problems) and organizing screening for high-risk diseases including **skin, bladder, lung cancer**, especially in vulnerable communities (huang2015thehealtheffects pages 11-14).

---

## 14. Other species / natural disease
Not addressed in the retrieved corpus.

---

## 15. Model organisms
Evidence in this corpus focuses primarily on human epidemiology and human cell models; detailed arsenic-cancer animal model summaries were not retrieved here. However, mechanistic reviews note reliance on human models due to species differences in arsenic metabolism (nail2023arsenicandhuman pages 1-3).

---

## Key quantitative evidence tables (for knowledge base ingestion)

| Cancer type | Evidence statement | Key quantitative estimate(s) | Study type/population | Publication (year, journal) | URL/DOI |
|---|---|---|---|---|---|
| Bladder cancer / urinary tract cancer | **IARC-established** human cancer site for inorganic arsenic; strongest evidence is for long-term ingestion via **drinking water**, with smoking noted as a co-exposure that can exacerbate risk (issanov2023arsenicindrinking pages 1-2, nuvolone2023longtermexposureto pages 1-2) | Bayesian meta-analysis: bladder cancer incidence RR **1.25** (0.92–1.73) at **10 µg/L**, **2.11** (1.18–4.22) at **50 µg/L**, **3.01** (1.31–8.17) at **150 µg/L**; bladder cancer mortality ratio **1.36** (0.35–6.39), **2.92** (1.24–7.82), **4.88** (2.83–9.03) at 10/50/150 µg/L, respectively (issanov2023arsenicindrinking pages 1-2, issanov2023arsenicindrinking pages 33-35) | 2023 systematic review update/meta-analysis of **34 studies**; highly exposed populations in Chile, Taiwan, Argentina, Bangladesh and others (issanov2023arsenicindrinking pages 1-2, issanov2023arsenicindrinking pages 33-35) | Issanov et al. **2023**, *Water* | https://doi.org/10.3390/w15122185 |
| Kidney cancer | **Limited-to-supportive human evidence** overall; urinary tract organs are biologically plausible targets because most ingested arsenic is excreted in urine; principal source is **drinking water** (issanov2023arsenicindrinking pages 1-2, nuvolone2023longtermexposureto pages 1-2) | Bayesian meta-analysis: kidney cancer RR **1.37** (1.07–1.77) at **10 µg/L**, **1.95** (1.44–2.65) at **50 µg/L**, **2.47** (1.74–3.52) at **150 µg/L**; case-control studies reported ORs rising from **1.37 to 6.0** across **50 to ≥300 µg/L** drinking-water categories in Bangladesh; subtype-specific ORs **5.49** and **10.35** for renal pelvis/ureter cancers at higher cumulative exposures (issanov2023arsenicindrinking pages 33-35, issanov2023arsenicindrinking pages 1-2) | Systematic review/meta-analysis of urinary tract cancers; case-control and cohort studies from Taiwan, Bangladesh, Chile and elsewhere (issanov2023arsenicindrinking pages 33-35, issanov2023arsenicindrinking pages 1-2) | Issanov et al. **2023**, *Water* | https://doi.org/10.3390/w15122185 |
| Lung cancer | **IARC-established** human cancer site for inorganic arsenic; dominant route in current evidence is **drinking water**, with additional historical evidence from occupational exposure and important interaction with smoking (nuvolone2023longtermexposureto pages 1-2, issanov2023arsenicindrinking pages 1-2) | Italian residential cohort: hospitalization HR for lung cancer **1.85** (1.14–3.02) for exposure **>10 µg/L** vs lower exposure (nuvolone2023longtermexposureto pages 1-2); review reported an additional **4.51 lung cancer cases per 100,000** associated with water contaminated up to **10 µg/L** arsenic (pal2024unravelingtherole pages 1-4); Taiwan mitigation study: RR in endemic area vs rest of Taiwan fell from **8** to about **1.5–2** after municipal water intervention (su2011reductioninarsenic pages 1-2) | Population-based residential cohort in Tuscany (**30,910 subjects; 407,213 person-years**) plus review and ecological/intervention evidence from Taiwan (nuvolone2023longtermexposureto pages 1-2, su2011reductioninarsenic pages 1-2, pal2024unravelingtherole pages 1-4) | Nuvolone et al. **2023**, *BMC Public Health*; Pal & Firdous **2024**, *Discover Oncology*; Su et al. **2011**, *Cancer Causes & Control* | https://doi.org/10.1186/s12889-022-14818-x; https://doi.org/10.1007/s12672-024-01417-y; https://doi.org/10.1007/s10552-010-9679-2 |
| Skin cancer / non-melanoma skin cancer (BCC, SCC) | **IARC-established** human cancer site for inorganic arsenic; chronic exposure is most often from **groundwater/drinking water**; mechanistic and cohort data strongly support risk, especially for NMSC (nuvolone2023longtermexposureto pages 1-2, jasmine2024molecularprofilingand pages 1-2) | In a 6-year cohort of **7000 adults** exposed to arsenic, incident **BCC** occurred in **2.2% of males** and **1.3% of females**; **SCC** in **0.4% of males** and **0.2% of females** (jasmine2024molecularprofilingand pages 1-2); review estimated global attributable cases from inorganic arsenic in food of **10,729–110,015** skin cancer cases (pal2024unravelingtherole pages 1-4) | Prospective follow-up of arsenic-exposed Bangladeshi adults with tumor molecular profiling; review-based attributable burden estimates (jasmine2024molecularprofilingand pages 1-2, pal2024unravelingtherole pages 1-4) | Jasmine et al. **2024**, *Cells*; Pal & Firdous **2024**, *Discover Oncology* | https://doi.org/10.3390/cells13121056; https://doi.org/10.1007/s12672-024-01417-y |
| Liver cancer / hepatobiliary cancers | **Limited evidence** in humans per IARC-style summaries; evidence is **emerging to moderate** for digestive/hepato-pancreatico-biliary cancers, mainly from **drinking water** and some environmental/occupational exposure (nuvolone2023longtermexposureto pages 1-2, kasmi2023carcinogeniceffectof pages 1-2) | Systematic review of digestive cancers: **43% (3/7)** of incidence studies and **48% (10/21)** of mortality studies reported associations with arsenic; one study reported higher liver-cancer mortality for drinking-water arsenic **>0.64 mg/L** (kasmi2023carcinogeniceffectof pages 1-2, kasmi2023carcinogeniceffectof pages 2-4) | 2023 systematic review of **35 human studies** (17 ecological, 13 case-control, 5 cohort), emphasizing HPB malignancies (kasmi2023carcinogeniceffectof pages 1-2, kasmi2023carcinogeniceffectof pages 2-4) | Kasmi et al. **2023**, *Environmental Health* | https://doi.org/10.1186/s12940-023-00988-7 |
| Esophageal cancer | **Emerging / mixed evidence**; not established by IARC for arsenic, but some regional studies suggest elevated risk in high-exposure endemic settings; main source is **drinking water/environmental exposure** (kasmi2023carcinogeniceffectof pages 2-4, kasmi2023carcinogeniceffectof pages 1-2) | No association in one analysis for men RR **1.02** (0.96–1.08); women RR **0.89** (0.80–1.00); however, BFD-endemic men had esophageal cancer SMR **1.67** (1.30–2.12) (kasmi2023carcinogeniceffectof pages 2-4) | Human systematic review of digestive cancers including ecological and case-control studies from Taiwan and other endemic settings (kasmi2023carcinogeniceffectof pages 2-4) | Kasmi et al. **2023**, *Environmental Health* | https://doi.org/10.1186/s12940-023-00988-7 |
| Gastric cancer | **Emerging / mixed evidence**; not established by IARC for arsenic, but several ecological studies suggest associations in contaminated regions; source primarily **drinking water/soil exposure** (kasmi2023carcinogeniceffectof pages 2-4) | Soil arsenic associated with gastric cancer in quasi-Poisson models: men RR **1.114** (1.063–1.168), women RR **1.105** (1.051–1.161); BFD-area gastric cancer mortality SMR **1.36** in men and **1.40** in women (kasmi2023carcinogeniceffectof pages 2-4) | Human systematic review of digestive cancers with ecological/regional studies (kasmi2023carcinogeniceffectof pages 2-4) | Kasmi et al. **2023**, *Environmental Health* | https://doi.org/10.1186/s12940-023-00988-7 |
| Gallbladder / biliary tract cancers | **Emerging evidence**; biologic plausibility is strong because arsenic is metabolized in the liver and toxic metabolites are excreted in bile; main source **drinking water** (kasmi2023carcinogeniceffectof pages 1-2, kasmi2023carcinogeniceffectof pages 10-11) | Recent systematic review did not provide pooled RR/HR in the extracted text, but concluded a substantial proportion of digestive-cancer studies suggested associations, particularly for **hepato-pancreatico-biliary malignancies** (kasmi2023carcinogeniceffectof pages 1-2) | 2023 systematic review of human studies on digestive cancers and arsenic exposure (kasmi2023carcinogeniceffectof pages 1-2, kasmi2023carcinogeniceffectof pages 10-11) | Kasmi et al. **2023**, *Environmental Health* | https://doi.org/10.1186/s12940-023-00988-7 |
| Prostate cancer | **Limited evidence** in humans; mentioned as a site with reported but not conclusive associations; sources include **drinking water** and possibly occupational exposure (nuvolone2023longtermexposureto pages 1-2, kasmi2023carcinogeniceffectof pages 10-11) | No robust pooled RR/HR extracted in the provided evidence; categorized as having **limited evidence of carcinogenesis** in the Nuvolone review summary (nuvolone2023longtermexposureto pages 1-2) | Review/background evidence summarizing human epidemiology (nuvolone2023longtermexposureto pages 1-2) | Nuvolone et al. **2023**, *BMC Public Health* | https://doi.org/10.1186/s12889-022-14818-x |
| Bladder and lung cancers after exposure reduction | Real-world mitigation evidence shows arsenic-related cancer burden can decline after **municipal tap-water substitution** for contaminated artesian wells (su2011reductioninarsenic pages 1-2, su2011reductioninarsenic pages 2-4) | In southwestern Taiwan, bladder cancer RR in the endemic area vs rest of Taiwan declined from **20 to 5** across cohorts after municipal water introduction; lung cancer RR declined from **8 to ~1.5–2**; bladder cancer SMR fell from **8.13 (1979)** to **4.26 (2003)** (su2011reductioninarsenic pages 1-2, su2011reductioninarsenic pages 2-4) | Ecological age-period-cohort analysis using Taiwan Cancer Registry, arseniasis-endemic population (su2011reductioninarsenic pages 1-2, su2011reductioninarsenic pages 2-4) | Su et al. **2011**, *Cancer Causes & Control* | https://doi.org/10.1007/s10552-010-9679-2 |


*Table: This table summarizes the main human cancers linked to inorganic arsenic exposure, especially from drinking water, and highlights the strongest quantitative risk estimates and real-world intervention evidence available in the retrieved sources.*

| Intervention type | Implementation level (household/community/municipal/regulatory) | Example location/study | Quantitative outcome (exposure reduction, lesion recovery, cancer RR/SMR changes) | Notes/limitations | Publication (year) | DOI/URL |
|---|---|---|---|---|---|---|
| Municipal tap-water substitution for high-arsenic well water | Municipal / regional infrastructure | Blackfoot disease endemic area (BFDEA), southwestern Taiwan; government-installed municipal water beginning early 1970s (su2011reductioninarsenic pages 1-2, su2011reductioninarsenic pages 2-4) | After intervention, bladder cancer RR for BFDEA vs rest of Taiwan fell from about **20** to **5** across cohorts; lung cancer RR fell from about **8** to **1.5-2**; bladder cancer SMR declined from **8.13 (1979)** to **4.26 (2003)** (su2011reductioninarsenic pages 1-2, su2011reductioninarsenic pages 2-4) | Strong real-world evidence that exposure reduction lowers long-latency cancer burden, but bladder cancer incidence remained elevated, suggesting long latency/residual risk or co-exposures (su2011reductioninarsenic pages 1-2, su2011reductioninarsenic pages 2-4) | Su et al. (2011) | https://doi.org/10.1007/s10552-010-9679-2 |
| Well testing, labeling, alternative safe-water installation, point-of-use filtration, dug wells, rainwater harvesting | Household + community program | Bangladesh arsenic mitigation programs; follow-up of skin lesion cases with village interventions including tube-well testing/labeling and installation of arsenic-safe sources (seow2012arsenicreductionin pages 1-1) | Water arsenic decreased by **41% overall**; **65** individuals with baseline skin lesions had no lesions at follow-up; each log10 decrease in water arsenic associated with lesion recovery OR **1.22** (95% CI 0.85-1.78); each log10 decrease in toenail arsenic OR **4.49** (95% CI 1.94-11.1); lesion severity improved by **-5.22** units (95% CI -8.61 to -1.82) per log10 toenail arsenic decrease (seow2012arsenicreductionin pages 1-1) | Outcome measured was skin lesion recovery, an early arsenicosis marker and precursor of later arsenic-related cancers rather than direct cancer incidence reduction (seow2012arsenicreductionin pages 1-1) | Seow et al. (2012) | https://doi.org/10.1289/ehp.1205381 |
| Activated alumina adsorption | Household / community treatment | Systematic review of field technologies in developing countries; strongest evidence from BRAC study in Bangladesh (joneshughes2013areinterventionsto pages 1-2) | Only intervention with “excellent” effectiveness in the review; **>=95%** of effluent samples met the WHO arsenic guideline **<=0.01 mg/L** in the strongest study (joneshughes2013areinterventionsto pages 1-2) | Evidence base overall weak/heterogeneous; most included studies were methodologically weak and did not directly report cancer outcomes (joneshughes2013areinterventionsto pages 1-2) | Jones-Hughes et al. (2013) | https://doi.org/10.1186/2047-2382-2-11 |
| Zero-valent iron / iron-based adsorption methods | Household / community treatment | Multiple developing-country field studies summarized in systematic review (joneshughes2013areinterventionsto pages 1-2, joneshughes2013areinterventionsto pages 13-14) | Review found adsorption and zero-valent iron interventions had the most persuasive performance, with many studies reporting **>=95%** of samples below **0.01 mg/L** (joneshughes2013areinterventionsto pages 1-2) | Effectiveness depended heavily on context, maintenance, acceptability, and ownership; health endpoints such as cancer reduction were generally not measured (joneshughes2013areinterventionsto pages 1-2, joneshughes2013areinterventionsto pages 13-14) | Jones-Hughes et al. (2013) | https://doi.org/10.1186/2047-2382-2-11 |
| Sono / three-kolshi / gagri / pitcher filters | Household treatment | Bangladesh-focused field evaluations in systematic review (joneshughes2013areinterventionsto pages 1-2) | Several household filters achieved **>=95%** of samples meeting national arsenic standards; some also performed well against WHO threshold **<=0.01 mg/L** (joneshughes2013areinterventionsto pages 1-2) | Performance varied by implementation context; most studies had weak designs and limited reporting on sustained use or health outcomes (joneshughes2013areinterventionsto pages 1-2) | Jones-Hughes et al. (2013) | https://doi.org/10.1186/2047-2382-2-11 |
| Community education, well labeling/painting, safe-well switching, screening for arsenic-related disease | Community / public health | Global mitigation recommendations summarized in geographic review (huang2015thehealtheffects pages 11-14) | Quantitative exposure or cancer reductions not pooled in the excerpt, but interventions are intended to prevent chronic exposure and support screening for skin, bladder, and lung cancers (huang2015thehealtheffects pages 11-14) | Review notes that reducing exposure alone may not immediately eliminate health risks in chronically exposed populations; ongoing surveillance and screening remain necessary (huang2015thehealtheffects pages 11-14) | Huang et al. (2015) | https://doi.org/10.1080/09603123.2014.958139 |
| Household sand filtration | Household treatment | Hanam Province, Vietnam (huy2014assessinghealthrisk pages 6-9) | Sand filters removed about **83%** of arsenic from water, but the majority of post-filtration samples still exceeded **10 ppb** because most systems were nonstandard and poorly maintained (huy2014assessinghealthrisk pages 6-9) | Illustrates that nominally low-cost filtration can underperform without aeration, adequate media thickness, and maintenance; no direct cancer outcome measured (huy2014assessinghealthrisk pages 6-9) | Huy et al. (2014) | https://doi.org/10.3390/ijerph110807575 |
| Regulatory tightening of drinking-water arsenic standard from 50 to 10 µg/L plus structural water-quality restoration works | Regulatory + municipal | Mt. Amiata area, Tuscany, Italy; EU Directive 98/83/EC and post-2010 restoration actions (nuvolone2023longtermexposureto pages 1-2) | Cohort found higher risks above **10 µg/L**: non-accidental mortality HR **1.07** (1.01-1.13), malignant neoplasm hospitalization HR **1.10** (1.02-1.19), lung cancer hospitalization HR **1.85** (1.14-3.02), supporting benefit of keeping concentrations below regulatory threshold (nuvolone2023longtermexposureto pages 1-2) | Study documents regulation and remediation context, but did not directly quantify post-remediation cancer decline; some excess risk appeared even below 10 µg/L (nuvolone2023longtermexposureto pages 1-2) | Nuvolone et al. (2023) | https://doi.org/10.1186/s12889-022-14818-x |


*Table: This table summarizes real-world interventions used to reduce arsenic exposure relevant to arsenic-related cancer prevention, from household filters to municipal water substitution and regulatory action. It highlights where quantitative outcomes are available, including exposure reduction, lesion recovery, and long-latency cancer incidence changes.*

---

## Visual evidence (dose–response)
Issanov et al. (Water, 2023) provide Table 7 and Figures 3–4 summarizing modeled dose–response for bladder and kidney cancer across arsenic concentrations, including 10/50/150 µg/L (issanov2023arsenicindrinking media 90db8dee, issanov2023arsenicindrinking media f21eb48e, issanov2023arsenicindrinking media a0cd84bc).

---

## Direct quotes from abstracts (supporting key claims)
1. **Dose–response at 10 µg/L and above (bladder/kidney cancer):**
   - “For bladder cancer incidence, the estimated posterior mean relative risks (RRs) were **1.25 (0.92–1.73), 2.11 (1.18–4.22) and 3.01 (1.31–8.17) at arsenic concentrations of 10, 50 and 150 µg/L**, respectively…” (issanov2023arsenicindrinking pages 1-2)

2. **Low-level drinking water exposure linked to lung cancer hospitalization:**
   - “Long-term exposure to arsenic concentrations > 10 µg/l resulted positively associated with… **lung cancer (HR = 1.85 95%CI:1.14–3.02)** …” (nuvolone2023longtermexposureto pages 1-2)

3. **Arsenic-induced senescence mechanisms:**
   - “Numerous studies have indicated that arsenic induces cellular senescence through various mechanisms, including triggering epigenetic alterations, inducing the senescence-associated secretory phenotype (SASP), promoting telomere shortening, and causing mitochondrial dysfunction.” (gu2024researchprogresson pages 1-2)

---

## Limitations and gaps (important for knowledge base curation)
- **Formal disease identifiers (MONDO, ICD-10/11 codes, Orphanet/OMIM)** were not extractable from the retrieved corpus; external ontology mapping is required (issanov2023arsenicindrinking pages 2-4).
- **Site-specific cancer treatment and prognosis** (e.g., 5-year survival) were not addressed in the retrieved arsenic-focused sources; these should be filled using cancer registry resources (e.g., SEER) and site-specific clinical guidelines.
- **Animal models and cross-species data** were not comprehensively retrieved in the current evidence set.

---

## Source list (URLs and publication dates)
- Issanov A. et al. “Arsenic in Drinking Water and Urinary Tract Cancers: A Systematic Review Update.” *Water*. Published **2023-06-09**. https://doi.org/10.3390/w15122185 (issanov2023arsenicindrinking pages 1-2)
- Nuvolone D. et al. “Long-term exposure to low-level arsenic in drinking water…” *BMC Public Health*. Published **2023-01**. https://doi.org/10.1186/s12889-022-14818-x (nuvolone2023longtermexposureto pages 1-2)
- Jasmine F. et al. “Molecular Profiling… in NMSC in a Population Exposed to Arsenic.” *Cells*. Published **2024-06-18**. https://doi.org/10.3390/cells13121056 (jasmine2024molecularprofilingand pages 1-2)
- Gu Y. et al. “Research progress on the regulatory mechanism of cell senescence in arsenic toxicity…” *Toxicology Research*. Published **2024-07**. https://doi.org/10.1093/toxres/tfae136 (gu2024researchprogresson pages 1-2)
- Nail A.N. et al. “Arsenic and Human Health: New Molecular Mechanisms For Arsenic-Induced Cancers.” *Current Pollution Reports*. Published **2023-08**. https://doi.org/10.1007/s40726-023-00278-3 (nail2023arsenicandhuman pages 1-3)
- Chung F.F.-L. et al. “Sodium arsenite-induced DNA methylation alterations exacerbated by p53 knockout…” *Heliyon*. Published **2024-11**. https://doi.org/10.1016/j.heliyon.2024.e39548 (chung2024sodiumarseniteinduceddna pages 1-2)
- Kasmi S. et al. “Carcinogenic effect of arsenic in digestive cancers: a systematic review.” *Environmental Health*. Published **2023-04**. https://doi.org/10.1186/s12940-023-00988-7 (kasmi2023carcinogeniceffectof pages 1-2)
- Su C.-C. et al. “Reduction in arsenic intake from water has different impacts on lung cancer and bladder cancer…” *Cancer Causes & Control*. Published **2011-11**. https://doi.org/10.1007/s10552-010-9679-2 (su2011reductioninarsenic pages 1-2)
- Seow W.J. et al. “Arsenic Reduction in Drinking Water and Improvement in Skin Lesions…” *Environmental Health Perspectives*. Published **2012-12**. https://doi.org/10.1289/ehp.1205381 (seow2012arsenicreductionin pages 1-1)



References

1. (issanov2023arsenicindrinking pages 1-2): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

2. (gu2024researchprogresson pages 1-2): Yun Gu, Ying Qiu, Yujian Li, and Weihua Wen. Research progress on the regulatory mechanism of cell senescence in arsenic toxicity: a systematic review. Toxicology research, 13 4:tfae136, Jul 2024. URL: https://doi.org/10.1093/toxres/tfae136, doi:10.1093/toxres/tfae136. This article has 4 citations.

3. (nail2023arsenicandhuman pages 6-8): Alexandra N. Nail, Manting Xu, Jonathan C. Bastick, Deep P. Patel, Max N. Rogers, and J. Christopher States. Arsenic and human health: new molecular mechanisms for arsenic-induced cancers. Current pollution reports, 9 4:784-797, Aug 2023. URL: https://doi.org/10.1007/s40726-023-00278-3, doi:10.1007/s40726-023-00278-3. This article has 11 citations and is from a peer-reviewed journal.

4. (nuvolone2023longtermexposureto pages 1-2): Daniela Nuvolone, Giorgia Stoppa, Davide Petri, and Fabio Voller. Long-term exposure to low-level arsenic in drinking water is associated with cause-specific mortality and hospitalization in the mt. amiata area (tuscany, italy). BMC Public Health, Jan 2023. URL: https://doi.org/10.1186/s12889-022-14818-x, doi:10.1186/s12889-022-14818-x. This article has 30 citations and is from a peer-reviewed journal.

5. (kasmi2023carcinogeniceffectof pages 1-2): Sophie Kasmi, Laureline Moser, Stéphanie Gonvers, Olivier Dormond, Nicolas Demartines, and Ismail Labgaa. Carcinogenic effect of arsenic in digestive cancers: a systematic review. Environmental Health, 22:1-11, Apr 2023. URL: https://doi.org/10.1186/s12940-023-00988-7, doi:10.1186/s12940-023-00988-7. This article has 31 citations and is from a peer-reviewed journal.

6. (issanov2023arsenicindrinking pages 2-4): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

7. (jasmine2024molecularprofilingand pages 1-2): Farzana Jasmine, Maria Argos, Yuliia Khamkevych, Tariqul Islam, Muhammad Rakibuz-Zaman, Mohammad Shahriar, Christopher R. Shea, Habibul Ahsan, and Muhammad G. Kibriya. Molecular profiling and the interaction of somatic mutations with transcriptomic profiles in non-melanoma skin cancer (nmsc) in a population exposed to arsenic. Cells, 13:1056, Jun 2024. URL: https://doi.org/10.3390/cells13121056, doi:10.3390/cells13121056. This article has 7 citations.

8. (issanov2023arsenicindrinking pages 33-35): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

9. (issanov2023arsenicindrinking media 90db8dee): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

10. (issanov2023arsenicindrinking media f21eb48e): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

11. (issanov2023arsenicindrinking media a0cd84bc): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

12. (issanov2023arsenicindrinking pages 42-43): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

13. (chung2024sodiumarseniteinduceddna pages 1-2): Felicia Fei-Lei Chung, Rita Khoueiry, Aurélie Sallé, Cyrille Cuenin, Maria Bošković, and Zdenko Herceg. Sodium arsenite-induced dna methylation alterations exacerbated by p53 knockout in mcf7 cells. Heliyon, 10:e39548, Nov 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e39548, doi:10.1016/j.heliyon.2024.e39548. This article has 0 citations.

14. (su2011reductioninarsenic pages 1-2): Che-Chun Su, Jia-Ling Lu, Kuo-Yang Tsai, and Ie-Bin Lian. Reduction in arsenic intake from water has different impacts on lung cancer and bladder cancer in an arseniasis endemic area in taiwan. Cancer Causes & Control, 22:101-108, Nov 2011. URL: https://doi.org/10.1007/s10552-010-9679-2, doi:10.1007/s10552-010-9679-2. This article has 43 citations and is from a peer-reviewed journal.

15. (seow2012arsenicreductionin pages 1-1): Wei Jie Seow, Wen-Chi Pan, Molly L. Kile, Andrea A. Baccarelli, Quazi Quamruzzaman, Mahmuder Rahman, Golam Mahiuddin, Golam Mostofa, Xihong Lin, and David C. Christiani. Arsenic reduction in drinking water and improvement in skin lesions: a follow-up study in bangladesh. Environmental Health Perspectives, 120:1733-1738, Dec 2012. URL: https://doi.org/10.1289/ehp.1205381, doi:10.1289/ehp.1205381. This article has 61 citations and is from a highest quality peer-reviewed journal.

16. (thankachan2023exploringtheinterplay pages 3-5): Mangalathettu Binumon Thankachan, Gayathri S. Kamath, Greeshma Sasikumar, and Sreejith Parameswara Panicker. Exploring the interplay between arsenic and cutaneous physiology, pathology, and regeneration. Arsenic in the Environment - Sources, Impacts and Remedies, Nov 2023. URL: https://doi.org/10.5772/intechopen.1001901, doi:10.5772/intechopen.1001901. This article has 2 citations.

17. (thankachan2023exploringtheinterplay pages 5-7): Mangalathettu Binumon Thankachan, Gayathri S. Kamath, Greeshma Sasikumar, and Sreejith Parameswara Panicker. Exploring the interplay between arsenic and cutaneous physiology, pathology, and regeneration. Arsenic in the Environment - Sources, Impacts and Remedies, Nov 2023. URL: https://doi.org/10.5772/intechopen.1001901, doi:10.5772/intechopen.1001901. This article has 2 citations.

18. (ganie2024arsenictoxicitysources pages 11-13): Shahid Yousuf Ganie, Darakhshan Javaid, Younis Ahmad Hajam, and Mohd Salim Reshi. Arsenic toxicity: sources, pathophysiology and mechanism. Toxicology research, 13 1:tfad111, Dec 2024. URL: https://doi.org/10.1093/toxres/tfad111, doi:10.1093/toxres/tfad111. This article has 152 citations.

19. (pullella2024elucidatingtherelationshipa pages 24-28): K Pullella. Elucidating the relationship between arsenic exposure and cancer risk in canada. Unknown journal, 2024.

20. (gu2024researchprogresson pages 2-3): Yun Gu, Ying Qiu, Yujian Li, and Weihua Wen. Research progress on the regulatory mechanism of cell senescence in arsenic toxicity: a systematic review. Toxicology research, 13 4:tfae136, Jul 2024. URL: https://doi.org/10.1093/toxres/tfae136, doi:10.1093/toxres/tfae136. This article has 4 citations.

21. (nail2023arsenicandhuman pages 4-6): Alexandra N. Nail, Manting Xu, Jonathan C. Bastick, Deep P. Patel, Max N. Rogers, and J. Christopher States. Arsenic and human health: new molecular mechanisms for arsenic-induced cancers. Current pollution reports, 9 4:784-797, Aug 2023. URL: https://doi.org/10.1007/s40726-023-00278-3, doi:10.1007/s40726-023-00278-3. This article has 11 citations and is from a peer-reviewed journal.

22. (huang2015thehealtheffects pages 11-14): Lei Huang, Haiyun Wu, and Tsering Jan van der Kuijp. The health effects of exposure to arsenic-contaminated drinking water: a review by global geographical distribution. International Journal of Environmental Health Research, 25:432-452, Jun 2015. URL: https://doi.org/10.1080/09603123.2014.958139, doi:10.1080/09603123.2014.958139. This article has 129 citations and is from a peer-reviewed journal.

23. (su2011reductioninarsenic pages 2-4): Che-Chun Su, Jia-Ling Lu, Kuo-Yang Tsai, and Ie-Bin Lian. Reduction in arsenic intake from water has different impacts on lung cancer and bladder cancer in an arseniasis endemic area in taiwan. Cancer Causes & Control, 22:101-108, Nov 2011. URL: https://doi.org/10.1007/s10552-010-9679-2, doi:10.1007/s10552-010-9679-2. This article has 43 citations and is from a peer-reviewed journal.

24. (joneshughes2013areinterventionsto pages 1-2): Tracey Jones-Hughes, Jaime Peters, Rebecca Whear, Chris Cooper, Hywel Evans, Michael Depledge, and Mark Pearson. Are interventions to reduce the impact of arsenic contamination of groundwater on human health in developing countries effective? a systematic review. Environmental Evidence, 2:1-32, May 2013. URL: https://doi.org/10.1186/2047-2382-2-11, doi:10.1186/2047-2382-2-11. This article has 21 citations.

25. (joneshughes2013areinterventionsto pages 13-14): Tracey Jones-Hughes, Jaime Peters, Rebecca Whear, Chris Cooper, Hywel Evans, Michael Depledge, and Mark Pearson. Are interventions to reduce the impact of arsenic contamination of groundwater on human health in developing countries effective? a systematic review. Environmental Evidence, 2:1-32, May 2013. URL: https://doi.org/10.1186/2047-2382-2-11, doi:10.1186/2047-2382-2-11. This article has 21 citations.

26. (nail2023arsenicandhuman pages 1-3): Alexandra N. Nail, Manting Xu, Jonathan C. Bastick, Deep P. Patel, Max N. Rogers, and J. Christopher States. Arsenic and human health: new molecular mechanisms for arsenic-induced cancers. Current pollution reports, 9 4:784-797, Aug 2023. URL: https://doi.org/10.1007/s40726-023-00278-3, doi:10.1007/s40726-023-00278-3. This article has 11 citations and is from a peer-reviewed journal.

27. (pal2024unravelingtherole pages 1-4): Sourav Pal and Sayed Mohammed Firdous. Unraveling the role of heavy metals xenobiotics in cancer: a critical review. Discover Oncology, Nov 2024. URL: https://doi.org/10.1007/s12672-024-01417-y, doi:10.1007/s12672-024-01417-y. This article has 15 citations.

28. (kasmi2023carcinogeniceffectof pages 2-4): Sophie Kasmi, Laureline Moser, Stéphanie Gonvers, Olivier Dormond, Nicolas Demartines, and Ismail Labgaa. Carcinogenic effect of arsenic in digestive cancers: a systematic review. Environmental Health, 22:1-11, Apr 2023. URL: https://doi.org/10.1186/s12940-023-00988-7, doi:10.1186/s12940-023-00988-7. This article has 31 citations and is from a peer-reviewed journal.

29. (kasmi2023carcinogeniceffectof pages 10-11): Sophie Kasmi, Laureline Moser, Stéphanie Gonvers, Olivier Dormond, Nicolas Demartines, and Ismail Labgaa. Carcinogenic effect of arsenic in digestive cancers: a systematic review. Environmental Health, 22:1-11, Apr 2023. URL: https://doi.org/10.1186/s12940-023-00988-7, doi:10.1186/s12940-023-00988-7. This article has 31 citations and is from a peer-reviewed journal.

30. (huy2014assessinghealthrisk pages 6-9): Tung Bui Huy, Tran Thi Tuyet-Hanh, R. Johnston, and H. Nguyen-Viet. Assessing health risk due to exposure to arsenic in drinking water in hanam province, vietnam. International Journal of Environmental Research and Public Health, 11:7575-7591, Jul 2014. URL: https://doi.org/10.3390/ijerph110807575, doi:10.3390/ijerph110807575. This article has 88 citations.
