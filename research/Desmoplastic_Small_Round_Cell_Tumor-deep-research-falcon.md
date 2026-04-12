---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T14:21:27.012014'
end_time: '2026-04-05T14:32:31.523095'
duration_seconds: 664.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Desmoplastic Small Round Cell Tumor
  mondo_id: ''
  category: ''
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
- **Disease Name:** Desmoplastic Small Round Cell Tumor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Desmoplastic Small Round Cell Tumor** covering all of the
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
- **Disease Name:** Desmoplastic Small Round Cell Tumor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Desmoplastic Small Round Cell Tumor** covering all of the
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


## Desmoplastic Small Round Cell Tumor (DSRCT): Disease Characteristics Research Report (2023–2024 prioritized)

### Target disease
- **Disease name:** Desmoplastic small round cell tumor (DSRCT)
- **Category:** Rare aggressive fusion-driven sarcoma / small round cell sarcoma (primitive “small round blue cell tumor”) (magrath2024desmoplasticsmallround pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2)
- **MeSH identifier:** ClinicalTrials.gov lists MeSH term **“Desmoplastic Small Round Cell Tumor” (MeSH: D058405)** (NCT04022213 chunk 1)
- **MONDO / Orphanet / ICD-10/ICD-11 / OMIM:** Not available in the retrieved evidence set; would require direct ontology lookup outside the currently retrieved documents.

### Executive overview (current understanding)
DSRCT is an extremely rare, highly aggressive sarcoma that most often presents with multifocal peritoneal/abdominopelvic disease in adolescents and young adults, with strong male predominance, and poor long-term survival despite intensive multimodal therapy (surgery + chemotherapy + radiation) (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2). The defining molecular lesion is a reciprocal t(11;22)(p13;q12) translocation generating an oncogenic chimeric transcription factor **EWSR1::WT1** (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2). Recent 2024 mechanistic studies demonstrate that EWSR1::WT1 is a potent chromatin activator, preferentially binding active distal regulatory elements and driving vulnerabilities such as the **cyclin D–CDK4/6–RB** axis, supporting clinical translation of CDK4/6 inhibition (e.g., palbociclib) (magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2).

---

## 1. Disease information

### 1.1 What is the disease?
DSRCT is a rare, highly aggressive sarcoma characterized histologically by **nests of small round cells** embedded in an **abundant desmoplastic/fibrous stroma** (magrath2024desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2). It most commonly originates in the **abdominal and pelvic peritoneum** and typically presents with disseminated peritoneal implants at diagnosis (magrath2024desmoplasticsmallround pages 1-2).

### 1.2 Key identifiers and synonyms
- **Name in literature:** “Desmoplastic small round cell tumor” (DSRCT) (magrath2024desmoplasticsmallround pages 1-2)
- **Also described as:** “desmoplastic small round blue cell tumor” in some pathology contexts (gaidzik2024desmoplasticsmallround pages 1-2)
- **ICD-O code:** DSRCT described with **ICD-O: 8806/3** in a 2024 clinical series (gaidzik2024desmoplasticsmallround pages 1-2)
- **MeSH term:** D058405 (ClinicalTrials.gov) (NCT04022213 chunk 1)

### 1.3 Data provenance
Evidence in this report is drawn from:
- Aggregated resources (reviews; retrospective cohorts; ClinicalTrials.gov records) and
- Primary research (mechanistic studies in xenografts/PDX; pathology case series).
This is not derived from EHR-only sources.

---

## 2. Etiology

### 2.1 Disease causal factors (genetic/mechanistic)
**Primary causal event:** DSRCT is caused/defined by a reciprocal chromosomal translocation **t(11;22)(p13;q12)** producing the **EWSR1::WT1** fusion oncogene/oncoprotein (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2).

**Mechanistic definition:** EWSR1::WT1 is an oncogenic fusion transcription factor combining EWSR1’s N-terminal low complexity/prion-like activation domain with WT1 zinc-finger DNA-binding domains (magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2).

### 2.2 Risk factors
No environmental, infectious, or inherited germline risk factors were identified in the retrieved evidence. The consistent defining lesion is somatic fusion-driven oncogenesis (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2).

### 2.3 Protective factors / gene–environment interactions
No protective factors or GxE interactions were identified in the retrieved evidence set.

---

## 3. Phenotypes (clinical features) + ontology suggestions

### 3.1 Core phenotype spectrum
**Typical presentation:** Extended abdominal mass with symptoms from mass effect such as pain, abdominal distension, acute abdomen, and organ obstruction (gaidzik2024desmoplasticsmallround pages 1-2). A retrospective abdominal series reported common symptoms including abdominal distension, abdominal pain, and constipation (wang2021clinicopathologicalfeaturesof pages 1-2).

**Metastatic pattern:** High rate of metastatic disease at diagnosis is emphasized in mechanistic/clinical literature; one 2021 series reported 7/8 patients developed metastases to distant organs or lymph nodes (wang2021clinicopathologicalfeaturesof pages 1-2), consistent with “high rate of metastasis at diagnosis” in mechanistic work (magrath2024comprehensivetranscriptomicanalysis pages 1-2).

### 3.2 Suggested HPO terms (examples; not exhaustive)
- Abdominal pain: **HP:0002027** (supported by symptom reports) (wang2021clinicopathologicalfeaturesof pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2)
- Abdominal distension: **HP:0003270** (wang2021clinicopathologicalfeaturesof pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2)
- Constipation: **HP:0002019** (wang2021clinicopathologicalfeaturesof pages 1-2)
- Intestinal obstruction (if present clinically): **HP:0002595** (symptom domain “organ obstruction”) (gaidzik2024desmoplasticsmallround pages 1-2)
- Peritoneal carcinomatosis / peritoneal implants: can be represented via HPO terms related to peritoneal neoplasm spread; specific HPO mapping may require ontology crosswalk beyond retrieved texts (magrath2024desmoplasticsmallround pages 1-2).

### 3.3 Quality-of-life impact
QoL is not systematically quantified in the retrieved published cohorts. However, an ongoing trial explicitly measures QoL using EORTC QLQ-C30 and pain inventory (NCT07328425) (NCT07328425 chunk 1).

---

## 4. Genetic / molecular information

### 4.1 Causal genes and lesion
- **EWSR1::WT1** fusion gene from **t(11;22)(p13;q12)** is pathognomonic/defining (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2).
- Example breakpoint confirmation: **EWSR1 exon 7 – WT1 exon 8** fusion reported in a DSRCT case (hatanaka2019desmoplasticsmallround pages 1-2).

### 4.2 Pathogenic variants (somatic vs germline)
- DSRCT is primarily defined by the **somatic fusion**; broad DNA sequencing (WGS/WES/MSK-IMPACT) “failed to identify recurrent mutations” beyond the translocation in one mechanistic study, indicating few consistent cooperating point mutations (magrath2024comprehensivetranscriptomicanalysis pages 1-2).
- A 2024 clinical series used tumor-only NGS and found additional class 4/5 variants and copy-number changes (notably **CCND1 gain**) in some cases (gaidzik2024desmoplasticsmallround pages 1-2).

### 4.3 Fusion isoforms (+KTS / −KTS)
Two key 2024 studies emphasize that EWSR1::WT1 exists as two isoforms differing by inclusion/exclusion of three amino acids (KTS) between WT1 zinc fingers 3 and 4 (magrath2024desmoplasticsmallround pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2). Both isoforms appear required for tumor phenotypes resembling primary DSRCT (boulay2024ewswt1fusionisoforms pages 1-2). Another 2024 study found the **E-KTS isoform** plays a dominant role in transcription and directly binds the **CCND1** promoter (magrath2024comprehensivetranscriptomicanalysis pages 1-2).

### 4.4 Epigenetic/chromatin regulation
A 2024 Nature Communications study shows EWS-WT1 binding is enriched at distal regulatory elements (enhancers) marked by H3K4me1 and H3K27ac, consistent with a chromatin-activating role (boulay2024ewswt1fusionisoforms pages 1-2). In JN-DSRCT1, 91% of binding loci were distal regulatory elements (boulay2024ewswt1fusionisoforms pages 1-2).

### 4.5 Potential biomarkers / emerging diagnostics
- Traditional IHC can be nonspecific; molecular confirmation remains important (mohamed2017desmoplasticsmallround pages 4-5, gonzalez2024desmoplasticsmallround pages 6-7).
- A 2024 preprint proposes **CACNA2D2** as an EWSR1::WT1 signature gene with homogeneous membranous IHC expression as a potential single-marker diagnostic (needs prospective validation) (geyer2024superenhancerdrivencacna2d2is pages 39-44).

---

## 5. Environmental information
No non-genetic environmental, lifestyle, or infectious contributors were identified in the retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (fusion → transcriptional rewiring → aggressive phenotype)
1) **Initiating trigger:** t(11;22)(p13;q12) yields EWSR1::WT1 fusion (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2).
2) **Upstream mechanism:** EWSR1::WT1 acts as an aberrant transcription factor/chromatin activator; binding is concentrated at active enhancers and drives tumor-specific oncogenic gene expression programs (boulay2024ewswt1fusionisoforms pages 1-2).
3) **Downstream effectors/vulnerabilities:** Fusion-driven transcription upregulates the cyclin D–CDK4/6–RB axis via CCND1 promoter binding (magrath2024comprehensivetranscriptomicanalysis pages 1-2), generating sensitivity to CDK4/6 inhibitors (palbociclib) in xenograft/PDX models (magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2).

### 6.2 Key pathways and processes
- **Cell cycle regulation:** cyclin D–CDK4/6–RB axis is directly implicated as a key vulnerability (magrath2024comprehensivetranscriptomicanalysis pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2).
- **Chromatin/enhancer activation:** enhancer-centric binding and active histone marks at binding sites (boulay2024ewswt1fusionisoforms pages 1-2).

### 6.3 Suggested GO terms (biological process) and CL terms (cell types)
Evidence supports the following ontology suggestions (mapping requires curator verification):
- GO: **cell cycle** (GO:0007049), **positive regulation of transcription by RNA polymerase II** (GO:0045944), **chromatin organization** (GO:0006325) (mechanistically supported by fusion TF/chromatin activator role) (magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2).
- CL: likely mesenchymal-derived tumor cells; precise cell of origin is unknown and not resolved in the retrieved evidence (magrath2024desmoplasticsmallround pages 1-2).

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
- Primary: abdominal and pelvic peritoneum/abdominopelvic cavity; peritoneal surface with multiple nodules (magrath2024desmoplasticsmallround pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2).
- Frequent intra-abdominal sites include retroperitoneum, pelvis, omentum, mesentery (gaidzik2024desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2).
- Rare extra-abdominal primaries exist (e.g., parotid gland case report) (hatanaka2019desmoplasticsmallround pages 1-2).

### 7.2 Suggested UBERON terms (examples)
- Peritoneum: **UBERON:0002358** (site emphasized) (magrath2024desmoplasticsmallround pages 1-2)
- Omentum: **UBERON:0003688** and mesentery: **UBERON:0003692** (wang2021clinicopathologicalfeaturesof pages 1-2)
- Retroperitoneal region: **UBERON:0003684** (gaidzik2024desmoplasticsmallround pages 1-2)

---

## 8. Temporal development

### 8.1 Onset and progression
- Typical onset in adolescents/young adults (median ~mid-20s in series; often 20–30 years) (gaidzik2024desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2).
- Course is typically aggressive with early dissemination and high relapse risk even after trimodality therapy; one review notes that despite median OS ~60 months after induction + CRS/HIPEC + WART, median DFS was only 10 months (reijers2023intraabdominaldesmoplasticsmall pages 9-10).

---

## 9. Inheritance and population

### 9.1 Epidemiology
- **Incidence (U.S., sex-stratified):** 0.22 per million (males) and 0.05 per million (females) (magrath2024desmoplasticsmallround pages 1-2).
- **Sex ratio:** strong male predominance (magrath2024desmoplasticsmallround pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2).

### 9.2 Inheritance
DSRCT is not described as a Mendelian inherited disorder in the retrieved evidence; it is defined by a somatic fusion oncogene (magrath2024desmoplasticsmallround pages 1-2).

---

## 10. Diagnostics

### 10.1 Histopathology
- Nests of small round blue cells separated by marked desmoplastic stroma (wang2021clinicopathologicalfeaturesof pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2).

### 10.2 Immunohistochemistry (IHC) and key marker patterns
- Polyphenotypic profile with epithelial markers (cytokeratins, EMA) plus mesenchymal/myogenic markers (desmin, vimentin) and WT1 positivity (gaidzik2024desmoplasticsmallround pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2).
- **Desmin** may show a characteristic **paranuclear dot-like** pattern (hatanaka2019desmoplasticsmallround pages 1-2).
- **WT1 antibody region matters:** strong nuclear staining with **C-terminal WT1** antibody but not N-terminal WT1 is demonstrated in a fusion-confirmed case, emphasizing use of C-terminal WT1 in differential diagnosis (hatanaka2019desmoplasticsmallround pages 1-2).

### 10.3 Molecular confirmation
- **FISH** for EWSR1 rearrangement and **RT-PCR** for EWSR1–WT1 fusion transcripts are established ancillary methods; FISH showed higher positivity than RT-PCR in one series (91.3% vs 72.2%) (mohamed2017desmoplasticsmallround pages 4-5).
- In an 8-patient series, EWSR1–WT1 fusion was detected in all patients and described as the “gold standard” for definitive diagnosis (wang2021clinicopathologicalfeaturesof pages 1-2).
- Contemporary practice includes NGS panels and copy-number arrays alongside FISH and IHC (gaidzik2024desmoplasticsmallround pages 1-2).

### 10.4 Differential diagnosis (high-level)
Because DSRCT resembles other small round cell tumors histologically and can occur at unusual sites, combined morphology + broad IHC + molecular fusion confirmation is emphasized to avoid misclassification (gaidzik2024desmoplasticsmallround pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2).

---

## 11. Outcome / prognosis

### 11.1 Survival statistics
- Reported **5-year survival** commonly cited ~15–30% (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2).
- A 2024 mechanistic paper states: “standard multimodal therapy is insufficient, leading to a **5-year survival rate of only 15% to 25%**” (quoted from abstract) (magrath2024comprehensivetranscriptomicanalysis pages 1-2).
- A 2024 mechanistic paper notes “five-year survival rate … remains **below 15%**” (quoted from article text/intro) (boulay2024ewswt1fusionisoforms pages 1-2).

### 11.2 Prognostic factors
- Completeness of cytoreduction and lower peritoneal cancer burden (PCI) influence outcomes in intra-abdominal disease; CC score impacts median OS after CRS+HIPEC (63.1 months for CC-2 or better vs 26.7 months for CC-3) (reijers2023intraabdominaldesmoplasticsmall pages 9-10).
- Surgical resection associated with improved OS in retrospective cohorts (sundaramoorthy2025managementandsurvival pages 4-5, sundaramoorthy2025managementandsurvival pages 1-2).

---

## 12. Treatment

### 12.1 Standard-of-care approach (current practice)
DSRCT is typically managed with **multimodal therapy**: intensive systemic chemotherapy plus cytoreductive surgery and radiotherapy when feasible (magrath2024comprehensivetranscriptomicanalysis pages 1-2, magrath2024desmoplasticsmallround pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2).

**MAXO suggestions (examples):**
- Surgical cytoreduction/debulking: MAXO term corresponding to surgical resection/cytoreductive surgery.
- Systemic antineoplastic chemotherapy.
- Radiation therapy (whole abdominopelvic radiation / IMRT).

### 12.2 Chemotherapy (selected quantitative data)
- **P6 regimen** (vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide): in a cited 14-patient series, first-line P6 achieved disease control rate 100%, ORR 57.1%, and median time-to-progression 9.9 months (95% CI 7.2–11.7) (gawash2025desmoplasticsmallround pages 2-4).
- **VAC-IE/VDC-IE-like regimens:** a 4-patient institutional series reported 100% response to VAC-IE with mean duration 9.8 months; temozolomide+irinotecan had 50% response with ~8–9 month duration; CRS-HIPEC associated with longer survival in two patients (30.6 vs 11.2 months) (jayakrishnan2021desmoplasticsmallroundcell pages 1-3).
- A 2014–2023 cohort reported median OS 22.0 months; VDC+IE was predominant first-line (84%) and had the longest median OS (25 months) (sundaramoorthy2025managementandsurvival pages 1-2).

### 12.3 Surgery and HIPEC (evidence and controversy)
- A 2023 dedicated review concludes: “**no clear survival benefit**” is established for adding HIPEC after cytoreductive surgery across available literature (reijers2023intraabdominaldesmoplasticsmall pages 1-2, reijers2023intraabdominaldesmoplasticsmall pages 9-10).
- Nonetheless, selected series show high intermediate-term survival: MDACC phase 2 (n=20) CRS + oxaliplatin HIPEC reported 3-year OS 79% and median OS 58.4 months, but later MDACC work did not show statistically significant benefit for HIPEC addition (reijers2023intraabdominaldesmoplasticsmall pages 9-10).
- Toxicity is substantial: grade III–IV morbidity 22–34%, 30-day mortality 0.8–4.1% in peritoneal malignancies; adding HIPEC increased postoperative morbidity (40% vs 10% surgery alone in one study) (reijers2023intraabdominaldesmoplasticsmall pages 9-10).

**Figure/Table evidence:** The 2023 review contains a detailed **Table 3 (“Publications of HIPEC in DSRCT”)** summarizing regimens, selection criteria, and outcomes across small series (reijers2023intraabdominaldesmoplasticsmall media 0abe3cc8, reijers2023intraabdominaldesmoplasticsmall media e3635690, reijers2023intraabdominaldesmoplasticsmall media bbec6d82).

### 12.4 Radiotherapy
Whole abdominopelvic radiotherapy (WART) is used for diffuse peritoneal involvement; IMRT approaches aim to reduce toxicity (reijers2023intraabdominaldesmoplasticsmall pages 9-10). One French Sarcoma Group study cited in the review improved 3-year OS from 37.6% to 61.2% (p=0.045) after adjuvant radiation (reijers2023intraabdominaldesmoplasticsmall pages 9-10).

### 12.5 Targeted therapy and emerging strategies (recent developments)

#### CDK4/6 inhibition (2024 mechanistic + early clinical signal)
- Mechanism: EWSR1::WT1 upregulates CCND1 and drives growth via cyclin D–CDK4/6–RB axis; **palbociclib** reduced growth in two DSRCT xenograft models (abstract quote: “Treatment with the CDK4/6 inhibitor palbociclib successfully reduced growth in two DSRCT xenograft models.”) (magrath2024comprehensivetranscriptomicanalysis pages 1-2).
- PDX confirmation: palbociclib led to “marked tumor burden decrease” in DSRCT PDXs (boulay2024ewswt1fusionisoforms pages 1-2).
- Real-world series: cyclin D1 expression present in all seven tumors; palbociclib used in 4 patients with median time to progression 4.5 months (gaidzik2024desmoplasticsmallround pages 1-2).

#### Other candidate targets
A 2024 review highlights preclinical dependencies including NTRK3, EGFR, and immunotherapy strategies targeting B7-H3 (magrath2024desmoplasticsmallround pages 1-2). (These are mentioned as priorities but without outcome statistics in the retrieved excerpt.)

---

## 13. Prevention
No primary prevention or screening strategies are established in the retrieved evidence, consistent with a rare, non-hereditary, fusion-driven cancer.

---

## 14. Other species / natural disease
No naturally occurring DSRCT analogs in other species were identified in the retrieved evidence.

---

## 15. Model organisms / model systems
- Cell lines and xenograft/PDX models are central to current mechanistic work. A 2024 review notes that model scarcity has historically limited the field but that new tumor banks/cell lines are expanding research capacity (magrath2024desmoplasticsmallround pages 1-2).
- Preclinical evidence of targetability (palbociclib) derives from xenograft and PDX models (magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2).

---

## Recent developments and expert synthesis (2023–2024 emphasis)

1) **Chromatin-centric mechanism:** 2024 Nature Communications provides high-resolution evidence that EWS-WT1 acts as a chromatin activator with enhancer-dominant binding (91% distal elements) and active enhancer marks (H3K4me1/H3K27ac), supporting a model of fusion-driven enhancer reprogramming (boulay2024ewswt1fusionisoforms pages 1-2).
2) **Therapeutic vulnerability in cell cycle:** 2024 Cancer Research identifies CCND1 promoter binding and cyclin D–CDK4/6–RB axis dependence, providing a rationale for rapid clinical translation of CDK4/6 inhibitors in DSRCT (magrath2024comprehensivetranscriptomicanalysis pages 1-2).
3) **Clinical translation evidence:** A 2024 7-patient series reports CCND1 gains and cyclin D1 expression with use of palbociclib (median 4.5 months to progression), suggesting modest activity and supporting biomarker-driven trial development (gaidzik2024desmoplasticsmallround pages 1-2).
4) **HIPEC remains controversial:** 2023 systematic review concludes benefit is unproven and morbidity can be high; complete cytoreduction remains the dominant surgical determinant, with HIPEC potentially reserved to expert centers and selected patients (reijers2023intraabdominaldesmoplasticsmall pages 1-2, reijers2023intraabdominaldesmoplasticsmall pages 9-10).

---

## Current applications and real-world implementations (clinical trials)

| NCT ID | Title | Intervention(s) | Target / rationale | Phase | Status | Key eligibility (selected) | Primary endpoint | Start date | Last update post date | URL |
|---|---|---|---|---|---|---|---|---|---|---|
| NCT04022213 | A Study of the Drug I131-Omburtamab in People With Desmoplastic Small Round Cell Tumors and Other Solid Tumors in the Peritoneum | Intraperitoneal **131I-omburtamab**; Group A also receives **WAP-IMRT** (30 Gy in 20 fractions) | **B7-H3–directed radioimmunotherapy**; protocol includes immunohistochemistry to assess **B7H3** expression for eligibility in non-DSRCT assessment arm; intended to reduce recurrence/progression after cytoreduction (NCT04022213 chunk 1) | Phase 2 | Active, not recruiting | DSRCT confirmed at MSKCC; age >1 year; recovery from prior therapy; after surgery must have no definitive radiologic disease in liver/outside abdomen-pelvis or have had gross total resection; excludes prior progression, prior HIPEC, significant organ toxicities, mouse protein allergy, grade 4 hypersensitivity to radiolabeled iodine (NCT04022213 chunk 1) | Progression-free survival after RIT + WA/WAP-IMRT (NCT04022213 chunk 1) | 2019-07-15 | 2025-07-20 | https://clinicaltrials.gov/study/NCT04022213 |
| NCT04145349 | CAMPFIRE: A Study of Ramucirumab (LY3009806) in Children and Young Adults With Desmoplastic Small Round Cell Tumor | **Ramucirumab**, **cyclophosphamide**, **vinorelbine** (NCT04145349 chunk 3, NCT04145349 chunk 2) | **VEGFR2 inhibition** (ramucirumab) combined with chemotherapy for relapsed/recurrent/refractory DSRCT in children and young adults (inferred from intervention and known drug target; record title identifies ramucirumab study) (NCT04145349 chunk 2, NCT04145349 chunk 3) | Phase 1/2 | Active, not recruiting | Age 12 months to 29 years; relapsed/recurrent/refractory DSRCT; measurable disease by RECIST 1.1; at least one prior systemic therapy; not eligible for surgical resection; adequate cardiac, blood pressure, hematologic, renal, liver, and coagulation function; excludes active infection, recent major surgery, significant bleeding/thrombosis, CNS involvement, bowel obstruction, prior progression on cyclophosphamide+vinorelbine combination (NCT04145349 chunk 2) | Not available in retrieved chunk; record emphasizes efficacy/safety assessments with measurable disease requirements (NCT04145349 chunk 2) | 2020 (record year in retrieved trial summary) | Not available in retrieved chunk | https://clinicaltrials.gov/study/NCT04145349 |
| NCT07328425 | Clinical Study in Adult and Young Adult Patients With Advanced Desmoplastic Small Round Cell Tumor (DSRCT) ISG-TULIPS | **Lurbinectedin + irinotecan** | Molecularly selected advanced DSRCT (**EWSR1-WT1** translocation-positive); rationale is activity of combination in 2nd–4th line advanced disease after anthracycline-based chemotherapy, with optional biologic study to analyze tumor genes/molecules (NCT07328425 chunk 1) | Phase 2 | Recruiting | Histologically and molecularly confirmed DSRCT with documented **EWSR1-WT1** translocation; age ≥15 years; locally advanced or metastatic measurable disease; progression after last standard therapy; at least one prior anthracycline-based regimen and ≤3 prior chemotherapy lines; ECOG ≤2; adequate marrow/renal/hepatic/cardiac function; excludes prior lurbinectedin/trabectedin-related agents and significant uncontrolled comorbidity (NCT07328425 chunk 1) | Overall tumour response rate (ORR) by RECIST v1.1 (NCT07328425 chunk 1) | 2025-11-21 | 2026-04-03 | https://clinicaltrials.gov/study/NCT07328425 |


*Table: This table summarizes key interventional DSRCT trials retrieved from ClinicalTrials.gov, focusing on interventions, biologic rationale, eligibility, and endpoints. It is useful for quickly comparing current and recent real-world trial implementations in this rare sarcoma.*

Key examples:
- **Compartmental radioimmunotherapy**: NCT04022213 uses intraperitoneal **131I-omburtamab** (B7-H3-directed) with/without WAP-IMRT after cytoreduction (NCT04022213 chunk 1).
- **Anti-angiogenic strategy**: NCT04145349 evaluates **ramucirumab** plus chemotherapy backbone in relapsed/refractory pediatric/young adult DSRCT (NCT04145349 chunk 2).
- **Second-/later-line cytotoxic combinations**: NCT07328425 (ISG-TULIPS) tests **lurbinectedin + irinotecan** in molecularly confirmed EWSR1-WT1 DSRCT after anthracyclines, with ORR as primary endpoint and QoL as secondary endpoints (NCT07328425 chunk 1).

---

## Key facts table (quick reference)

| Item | Details | Source (with DOI/URL and publication year) |
|---|---|---|
| Disease definition | Rare, highly aggressive soft-tissue/pediatric sarcoma composed of nests of small round cells embedded in desmoplastic/fibrous stroma; often described as a small round blue cell tumor. (magrath2024desmoplasticsmallround pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2) | Magrath et al., 2024, *Front Cell Dev Biol*; DOI: 10.3389/fcell.2024.1442488; https://doi.org/10.3389/fcell.2024.1442488. Gaidzik et al., 2024, *Sarcoma*; DOI: 10.1155/2024/5036102; https://doi.org/10.1155/2024/5036102. Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6 |
| Hallmark genetic event | Defining lesion is t(11;22)(p13;q12) creating the **EWSR1::WT1** fusion oncogene/oncoprotein. (magrath2024comprehensivetranscriptomicanalysis pages 1-2, magrath2024desmoplasticsmallround pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2) | Magrath et al., 2024, *Cancer Research*; DOI: 10.1158/0008-5472.CAN-23-3334; https://doi.org/10.1158/0008-5472.CAN-23-3334. Magrath et al., 2024, *Front Cell Dev Biol*; DOI: 10.3389/fcell.2024.1442488; https://doi.org/10.3389/fcell.2024.1442488. Boulay et al., 2024, *Nat Commun*; DOI: 10.1038/s41467-024-51851-3; https://doi.org/10.1038/s41467-024-51851-3 |
| Canonical fusion breakpoint example | Example molecular confirmation reported as fusion between **EWSR1 exon 7** and **WT1 exon 8**. (hatanaka2019desmoplasticsmallround pages 1-2) | Hatanaka et al., 2019, *Diagnostic Pathology*; DOI: 10.1186/s13000-019-0825-1; https://doi.org/10.1186/s13000-019-0825-1 |
| Typical age | Predominantly affects children, adolescents, and young adults; median age in one 2024 series was **24.8 years**; commonly occurs in young men aged **20–30 years**. (gaidzik2024desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2) | Gaidzik et al., 2024, *Sarcoma*; DOI: 10.1155/2024/5036102; https://doi.org/10.1155/2024/5036102. Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6 |
| Sex distribution | Strong male predominance; incidence in the U.S. reported as **0.22 per million males** vs **0.05 per million females**; one review notes most cases occur in males. (magrath2024desmoplasticsmallround pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2) | Magrath et al., 2024, *Front Cell Dev Biol*; DOI: 10.3389/fcell.2024.1442488; https://doi.org/10.3389/fcell.2024.1442488. Hatanaka et al., 2019, *Diagnostic Pathology*; DOI: 10.1186/s13000-019-0825-1; https://doi.org/10.1186/s13000-019-0825-1 |
| Common primary sites | Most commonly arises in the **abdominal/pelvic peritoneum** and abdominopelvic cavity; frequent sites include **retroperitoneum, pelvis, omentum, mesentery/peritoneal surfaces**. (magrath2024desmoplasticsmallround pages 1-2, gaidzik2024desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2) | Magrath et al., 2024, *Front Cell Dev Biol*; DOI: 10.3389/fcell.2024.1442488; https://doi.org/10.3389/fcell.2024.1442488. Gaidzik et al., 2024, *Sarcoma*; DOI: 10.1155/2024/5036102; https://doi.org/10.1155/2024/5036102. Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6 |
| Tumor spread pattern | Often presents with **multiple peritoneal nodules/implants**, high metastatic burden, and high metastasis rate at diagnosis. (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2) | Magrath et al., 2024, *Front Cell Dev Biol*; DOI: 10.3389/fcell.2024.1442488; https://doi.org/10.3389/fcell.2024.1442488. Magrath et al., 2024, *Cancer Research*; DOI: 10.1158/0008-5472.CAN-23-3334; https://doi.org/10.1158/0008-5472.CAN-23-3334. Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6 |
| Key histopathology | Well-defined nests of small round blue cells separated by abundant/desmoplastic stroma. (wang2021clinicopathologicalfeaturesof pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2) | Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6. Hatanaka et al., 2019, *Diagnostic Pathology*; DOI: 10.1186/s13000-019-0825-1; https://doi.org/10.1186/s13000-019-0825-1 |
| Key diagnostic immunohistochemistry | Typical polyphenotypic profile includes epithelial markers (**cytokeratins, EMA**), mesenchymal/myogenic markers (**desmin, vimentin**), and **WT1 C-terminal** positivity; desmin may show **paranuclear dot-like** staining. (gaidzik2024desmoplasticsmallround pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2) | Gaidzik et al., 2024, *Sarcoma*; DOI: 10.1155/2024/5036102; https://doi.org/10.1155/2024/5036102. Hatanaka et al., 2019, *Diagnostic Pathology*; DOI: 10.1186/s13000-019-0825-1; https://doi.org/10.1186/s13000-019-0825-1. Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6 |
| Preferred WT1 antibody region | **C-terminal WT1** antibody is diagnostically informative; N-terminal WT1 may be negative in fusion-positive tumors. (hatanaka2019desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2) | Hatanaka et al., 2019, *Diagnostic Pathology*; DOI: 10.1186/s13000-019-0825-1; https://doi.org/10.1186/s13000-019-0825-1. Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6 |
| Molecular diagnostic tests | Molecular confirmation can be performed by **FISH** for EWSR1 rearrangement and/or **RT-PCR/NGS** for **EWSR1-WT1** fusion; fusion detection is described as the gold standard for definitive diagnosis. (gaidzik2024desmoplasticsmallround pages 1-2, hatanaka2019desmoplasticsmallround pages 1-2, wang2021clinicopathologicalfeaturesof pages 1-2) | Gaidzik et al., 2024, *Sarcoma*; DOI: 10.1155/2024/5036102; https://doi.org/10.1155/2024/5036102. Hatanaka et al., 2019, *Diagnostic Pathology*; DOI: 10.1186/s13000-019-0825-1; https://doi.org/10.1186/s13000-019-0825-1. Wang et al., 2021, *World J Surg Oncol*; DOI: 10.1186/s12957-021-02310-6; https://doi.org/10.1186/s12957-021-02310-6 |
| Incidence statistics | U.S. age-adjusted incidence reported as **0.22/million in males** and **0.05/million in females**. (magrath2024desmoplasticsmallround pages 1-2) | Magrath et al., 2024, *Front Cell Dev Biol*; DOI: 10.3389/fcell.2024.1442488; https://doi.org/10.3389/fcell.2024.1442488 |
| Survival statistics | Prognosis remains poor; reported **5-year survival ~15–30%**, with one 2024 mechanistic study citing **15–25%**. (magrath2024desmoplasticsmallround pages 1-2, magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2) | Magrath et al., 2024, *Front Cell Dev Biol*; DOI: 10.3389/fcell.2024.1442488; https://doi.org/10.3389/fcell.2024.1442488. Magrath et al., 2024, *Cancer Research*; DOI: 10.1158/0008-5472.CAN-23-3334; https://doi.org/10.1158/0008-5472.CAN-23-3334. Boulay et al., 2024, *Nat Commun*; DOI: 10.1038/s41467-024-51851-3; https://doi.org/10.1038/s41467-024-51851-3 |
| Recent biological vulnerability | 2024 studies identified **CCND1 / cyclin D–CDK4/6–RB axis** as an EWSR1::WT1-driven dependency; **palbociclib** reduced DSRCT growth in xenograft/PDX models. (magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2) | Magrath et al., 2024, *Cancer Research*; DOI: 10.1158/0008-5472.CAN-23-3334; https://doi.org/10.1158/0008-5472.CAN-23-3334. Boulay et al., 2024, *Nat Commun*; DOI: 10.1038/s41467-024-51851-3; https://doi.org/10.1038/s41467-024-51851-3 |
| Small clinical signal for CDK4/6 inhibition | In a 7-patient 2024 series, **Cyclin D1 expression** was seen in all tumors; **CCND1 gains** in 2 cases; **palbociclib** in 4 patients yielded median treatment duration to progression of **4.5 months**. (gaidzik2024desmoplasticsmallround pages 1-2) | Gaidzik et al., 2024, *Sarcoma*; DOI: 10.1155/2024/5036102; https://doi.org/10.1155/2024/5036102 |
| CRS/HIPEC outcome signal | HIPEC evidence is mixed: a 2023 review reported a phase 2 MDACC series with **3-year OS 79%** and median OS **58.4 months**, but concluded **no clear proven survival benefit** of adding HIPEC after complete cytoreductive surgery and noted higher morbidity. (reijers2023intraabdominaldesmoplasticsmall pages 9-10, reijers2023intraabdominaldesmoplasticsmall pages 1-2) | Reijers et al., 2023, *Current Oncology*; DOI: 10.3390/curroncol30040299; https://doi.org/10.3390/curroncol30040299 |


*Table: This table summarizes core identifiers, clinicopathologic features, diagnostic markers, and headline epidemiology/survival data for desmoplastic small round cell tumor. It is limited to facts directly supported by the provided evidence snippets and includes source links and publication years for quick reference.*

---

## Notes on limitations and evidence quality
DSRCT is rare; most clinical evidence is retrospective, single-institution, and heterogeneous (small samples, variable selection for cytoreduction/HIPEC, variable systemic regimens), limiting definitive causal inference for many interventions (reijers2023intraabdominaldesmoplasticsmall pages 9-10, jayakrishnan2021desmoplasticsmallroundcell pages 1-3). Mechanistic evidence for targeted therapies (e.g., CDK4/6 inhibition) is strong in 2024 xenograft/PDX models, but prospective DSRCT-specific clinical trial outcomes were not available in the retrieved evidence set (magrath2024comprehensivetranscriptomicanalysis pages 1-2, boulay2024ewswt1fusionisoforms pages 1-2).

### URLs and publication dates (examples cited above)
- Magrath et al. *Frontiers in Cell and Developmental Biology* (Published **2024-07-30**): https://doi.org/10.3389/fcell.2024.1442488 (magrath2024desmoplasticsmallround pages 1-2)
- Magrath et al. *Cancer Research* (**2024-04**, issue 9): https://doi.org/10.1158/0008-5472.CAN-23-3334 (magrath2024comprehensivetranscriptomicanalysis pages 1-2)
- Boulay et al. *Nature Communications* (**2024-08**): https://doi.org/10.1038/s41467-024-51851-3 (boulay2024ewswt1fusionisoforms pages 1-2)
- Reijers et al. *Current Oncology* (**2023-03**): https://doi.org/10.3390/curroncol30040299 (reijers2023intraabdominaldesmoplasticsmall pages 9-10)
- ClinicalTrials.gov NCT04022213 (first posted **2019-07-17**, updated **2025-07-20**): https://clinicaltrials.gov/study/NCT04022213 (NCT04022213 chunk 1)
- ClinicalTrials.gov NCT07328425 (first posted **2026-01-09**, updated **2026-04-03**): https://clinicaltrials.gov/study/NCT07328425 (NCT07328425 chunk 1)



References

1. (magrath2024desmoplasticsmallround pages 1-2): Justin W. Magrath, Madelyn Espinosa-Cotton, Dane A. Flinchum, Shruthi Sanjitha Sampath, Nai Kong Cheung, and Sean B. Lee. Desmoplastic small round cell tumor: from genomics to targets, potential paths to future therapeutics. Frontiers in Cell and Developmental Biology, Jul 2024. URL: https://doi.org/10.3389/fcell.2024.1442488, doi:10.3389/fcell.2024.1442488. This article has 18 citations.

2. (gaidzik2024desmoplasticsmallround pages 1-2): Verena I. Gaidzik, Regine Mayer-Steinacker, Mathias Wittau, Markus Schultheiß, Alexandra v. Baer, Kathrin Oehl-Huber, Sonja Dahlum, Anja Fischer, Uwe Gerstenmaier, Thomas Seufferlein, Andreas Buck, Ambros Beer, Wolfgang Thaiss, Peter Möller, Hartmut Döhner, Reiner Siebert, Ralf Marienfeld, and Thomas F. E. Barth. Desmoplastic small round cell tumors: clinical presentation, molecular characterization, and therapeutic approach of seven patients. Sarcoma, Jan 2024. URL: https://doi.org/10.1155/2024/5036102, doi:10.1155/2024/5036102. This article has 4 citations.

3. (NCT04022213 chunk 1):  A Study of the Drug I131-Omburtamab in People With Desmoplastic Small Round Cell Tumors and Other Solid Tumors in the Peritoneum. Memorial Sloan Kettering Cancer Center. 2019. ClinicalTrials.gov Identifier: NCT04022213

4. (magrath2024comprehensivetranscriptomicanalysis pages 1-2): Justin W. Magrath, Shruthi Sanjitha Sampath, Dane A. Flinchum, Alifiani B. Hartono, Ilon N. Goldberg, Julia R. Boehling, Suzana D. Savkovic, and Sean B. Lee. Comprehensive transcriptomic analysis of ewsr1::wt1 targets identifies cdk4/6 inhibitors as an effective therapy for desmoplastic small round cell tumors. Cancer Research, 84:1426-1442, Apr 2024. URL: https://doi.org/10.1158/0008-5472.can-23-3334, doi:10.1158/0008-5472.can-23-3334. This article has 18 citations and is from a highest quality peer-reviewed journal.

5. (boulay2024ewswt1fusionisoforms pages 1-2): Gaylor Boulay, Liliane C. Broye, Rui Dong, Sowmya Iyer, Rajendran Sanalkumar, Yu-Hang Xing, Rémi Buisson, Shruthi Rengarajan, Beverly Naigles, Benoît Duc, Angela Volorio, Mary E. Awad, Raffaele Renella, Ivan Chebib, G. Petur Nielsen, Edwin Choy, Gregory M. Cote, Lee Zou, Igor Letovanec, Ivan Stamenkovic, Miguel N. Rivera, and Nicolò Riggi. Ews-wt1 fusion isoforms establish oncogenic programs and therapeutic vulnerabilities in desmoplastic small round cell tumors. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51851-3, doi:10.1038/s41467-024-51851-3. This article has 9 citations and is from a highest quality peer-reviewed journal.

6. (wang2021clinicopathologicalfeaturesof pages 1-2): Ling-Ling Wang, Zhong-He Ji, Ying Gao, Hong Chang, Ping-Ping Sun, and Yan Li. Clinicopathological features of desmoplastic small round cell tumors: clinical series and literature review. World Journal of Surgical Oncology, Jun 2021. URL: https://doi.org/10.1186/s12957-021-02310-6, doi:10.1186/s12957-021-02310-6. This article has 25 citations and is from a peer-reviewed journal.

7. (NCT07328425 chunk 1):  Clinical Study in Adult and Young Adult Patients With Advanced Desmoplastic Small Round Cell Tumor (DSRCT) ISG-TULIPS. Italian Sarcoma Group. 2025. ClinicalTrials.gov Identifier: NCT07328425

8. (hatanaka2019desmoplasticsmallround pages 1-2): Kanako C. Hatanaka, Emi Takakuwa, Yutaka Hatanaka, Akira Suzuki, Satoshi IIzuka, Nayuta Tsushima, Tomoko Mitsuhashi, Shintaro Sugita, Akihiro Homma, Shojiroh Morinaga, Tadashi Hashegawa, and Yoshihiro Matsuno. Desmoplastic small round cell tumor of the parotid gland-report of a rare case and a review of the literature. Diagnostic Pathology, May 2019. URL: https://doi.org/10.1186/s13000-019-0825-1, doi:10.1186/s13000-019-0825-1. This article has 32 citations and is from a peer-reviewed journal.

9. (mohamed2017desmoplasticsmallround pages 4-5): Mustafa Mohamed, David Gonzalez, Karen J. Fritchie, John Swansbury, Dorte Wren, Charlotte Benson, Robin L. Jones, Cyril Fisher, and Khin Thway. Desmoplastic small round cell tumor: evaluation of reverse transcription-polymerase chain reaction and fluorescence in situ hybridization as ancillary molecular diagnostic techniques. Virchows Archiv, 471:631-640, Jul 2017. URL: https://doi.org/10.1007/s00428-017-2207-y, doi:10.1007/s00428-017-2207-y. This article has 33 citations and is from a peer-reviewed journal.

10. (gonzalez2024desmoplasticsmallround pages 6-7): Jeffrey Gonzalez, Stephanie Ocejo, Mercy Iribarren, Alvaro Abreu, Hisham F. Bahmad, and Robert Poppiti. Desmoplastic small round cell tumors of the gastrointestinal tract. Cancers, 16:4101, Dec 2024. URL: https://doi.org/10.3390/cancers16234101, doi:10.3390/cancers16234101. This article has 3 citations.

11. (geyer2024superenhancerdrivencacna2d2is pages 39-44): Florian H. Geyer, Alina Ritter, Seneca Kinn-Gurzo, Tobias Faehling, Jing Li, Armin Jarosch, Carine Ngo, Endrit Vinca, Karim Aljakouch, Azhar Orynbek, Shunya Ohmura, Thomas Kirchner, Roland Imle, Laura Romero-Pérez, Stefanie Bertram, Enrique de Álava, Sophie Postel-Vilnay, Ana Banito, Martin Sill, Yvonne M.H. Versleijen-Jonkers, Benjamin F.B. Mayer, Martin Ebinger, Monika Sparber-Sauer, Sabine Stegmaier, Daniel Baumhoer, Wolfgang Hartmann, Jeroen Krijgsveld, David Horst, Olivier Delattre, Patrick J. Grohar, Thomas G. P. Grünewald, and Florencia Cidre-Aranaz. Super-enhancer-driven cacna2d2 is an ewsr1::wt1 signature gene encoding a diagnostic marker for desmoplastic small round cell tumor (dsrct). bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.17.603708, doi:10.1101/2024.07.17.603708. This article has 0 citations.

12. (reijers2023intraabdominaldesmoplasticsmall pages 9-10): Sophie J. M. Reijers, Caroline C. H. Siew, Niels F. M. Kok, Charles Honoré, and Winan J. van Houdt. Intra-abdominal desmoplastic small round cell tumor (dsrct) and the role of hyperthermic intraperitoneal chemotherapy (hipec): a review. Current Oncology, 30:3951-3963, Mar 2023. URL: https://doi.org/10.3390/curroncol30040299, doi:10.3390/curroncol30040299. This article has 14 citations.

13. (sundaramoorthy2025managementandsurvival pages 4-5): Senthamizhan Sundaramoorthy, George Abraham, Geetha Narayanan, Sreejith G. Nair, Prakash N. Purushothaman, Sugeeth Mangalapilly Thambi, Sherin P. Mathew, Deepa Susan Joy Philip, Sindhu Nair, and Thamizharuvi Muthukumarasamy. Management and survival outcomes of desmoplastic small round cell tumor: a retrospective cohort study from a tertiary cancer center. BMC Cancer, Dec 2025. URL: https://doi.org/10.1186/s12885-025-15390-4, doi:10.1186/s12885-025-15390-4. This article has 0 citations and is from a peer-reviewed journal.

14. (sundaramoorthy2025managementandsurvival pages 1-2): Senthamizhan Sundaramoorthy, George Abraham, Geetha Narayanan, Sreejith G. Nair, Prakash N. Purushothaman, Sugeeth Mangalapilly Thambi, Sherin P. Mathew, Deepa Susan Joy Philip, Sindhu Nair, and Thamizharuvi Muthukumarasamy. Management and survival outcomes of desmoplastic small round cell tumor: a retrospective cohort study from a tertiary cancer center. BMC Cancer, Dec 2025. URL: https://doi.org/10.1186/s12885-025-15390-4, doi:10.1186/s12885-025-15390-4. This article has 0 citations and is from a peer-reviewed journal.

15. (gawash2025desmoplasticsmallround pages 2-4): Ahmed Gawash, Alexa Simonetti, Brandon J. Goodwin, and Alissa Brotman O’Neill. Desmoplastic small round cell tumor: an update of current management practices. Journal of the Egyptian National Cancer Institute, 37 1:13, Apr 2025. URL: https://doi.org/10.1186/s43046-025-00276-0, doi:10.1186/s43046-025-00276-0. This article has 2 citations.

16. (jayakrishnan2021desmoplasticsmallroundcell pages 1-3): THEJUS JAYAKRISHNAN, RYAN MOLL, ARIEL SANDHU, ANGELA SANGUINO, GURVEEN KAUR, and SHIFENG MAO. Desmoplastic small round-cell tumor: retrospective review of institutional data and literature review. Anticancer Research, 41:3859-3866, Jul 2021. URL: https://doi.org/10.21873/anticanres.15179, doi:10.21873/anticanres.15179. This article has 24 citations and is from a peer-reviewed journal.

17. (reijers2023intraabdominaldesmoplasticsmall pages 1-2): Sophie J. M. Reijers, Caroline C. H. Siew, Niels F. M. Kok, Charles Honoré, and Winan J. van Houdt. Intra-abdominal desmoplastic small round cell tumor (dsrct) and the role of hyperthermic intraperitoneal chemotherapy (hipec): a review. Current Oncology, 30:3951-3963, Mar 2023. URL: https://doi.org/10.3390/curroncol30040299, doi:10.3390/curroncol30040299. This article has 14 citations.

18. (reijers2023intraabdominaldesmoplasticsmall media 0abe3cc8): Sophie J. M. Reijers, Caroline C. H. Siew, Niels F. M. Kok, Charles Honoré, and Winan J. van Houdt. Intra-abdominal desmoplastic small round cell tumor (dsrct) and the role of hyperthermic intraperitoneal chemotherapy (hipec): a review. Current Oncology, 30:3951-3963, Mar 2023. URL: https://doi.org/10.3390/curroncol30040299, doi:10.3390/curroncol30040299. This article has 14 citations.

19. (reijers2023intraabdominaldesmoplasticsmall media e3635690): Sophie J. M. Reijers, Caroline C. H. Siew, Niels F. M. Kok, Charles Honoré, and Winan J. van Houdt. Intra-abdominal desmoplastic small round cell tumor (dsrct) and the role of hyperthermic intraperitoneal chemotherapy (hipec): a review. Current Oncology, 30:3951-3963, Mar 2023. URL: https://doi.org/10.3390/curroncol30040299, doi:10.3390/curroncol30040299. This article has 14 citations.

20. (reijers2023intraabdominaldesmoplasticsmall media bbec6d82): Sophie J. M. Reijers, Caroline C. H. Siew, Niels F. M. Kok, Charles Honoré, and Winan J. van Houdt. Intra-abdominal desmoplastic small round cell tumor (dsrct) and the role of hyperthermic intraperitoneal chemotherapy (hipec): a review. Current Oncology, 30:3951-3963, Mar 2023. URL: https://doi.org/10.3390/curroncol30040299, doi:10.3390/curroncol30040299. This article has 14 citations.

21. (NCT04145349 chunk 3):  CAMPFIRE: A Study of Ramucirumab (LY3009806) in Children and Young Adults With Desmoplastic Small Round Cell Tumor. Eli Lilly and Company. 2020. ClinicalTrials.gov Identifier: NCT04145349

22. (NCT04145349 chunk 2):  CAMPFIRE: A Study of Ramucirumab (LY3009806) in Children and Young Adults With Desmoplastic Small Round Cell Tumor. Eli Lilly and Company. 2020. ClinicalTrials.gov Identifier: NCT04145349
