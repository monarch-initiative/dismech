---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-30T20:25:52.121539'
end_time: '2026-04-30T20:58:02.025209'
duration_seconds: 1929.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Striate Palmoplantar Keratoderma Type 2
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Striate Palmoplantar Keratoderma Type 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Striate Palmoplantar Keratoderma Type 2** covering all of the
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
- **Disease Name:** Striate Palmoplantar Keratoderma Type 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Striate Palmoplantar Keratoderma Type 2** covering all of the
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


## Comprehensive Research Report: Striate Palmoplantar Keratoderma Type 2 (SPPK2; DSP-related)

### Executive summary
Striate palmoplantar keratoderma type 2 (SPPK2) is a hereditary palmoplantar keratoderma characterized by linear ("striate") hyperkeratosis on palms/fingers and focal hyperkeratosis at trauma/pressure sites on the soles, caused by pathogenic variants in **DSP** (desmoplakin), classically via **haploinsufficiency**. While many individuals have a skin-limited phenotype, DSP variants can also present within a **cardiocutaneous spectrum** (hair abnormalities and dilated/arrhythmogenic cardiomyopathy), requiring integrated dermatology–cardiology care. (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, armstrong1999haploinsufficiencyofdesmoplakin pages 2-3, petrof2012desmosomalgenodermatoses pages 2-4, karvonen2022anoveldesmoplakin pages 1-1)

---

### Artifact: identifiers and normalization
| Disease name | Synonyms / alternative names | Key identifier(s) | Causal gene | Inheritance | Typical onset | Core clinical features | Key references |
|---|---|---|---|---|---|---|---|
| Striate palmoplantar keratoderma type II | SPPK2; Striate PPK type II; striate palmoplantar keratoderma; striate PPK; SPPK; PPKS2; desmoplakin-related striate palmoplantar keratoderma | OMIM 612908 | **DSP** (desmoplakin) | Autosomal dominant | Childhood to early adulthood; first or early second decade reported in classic kindreds | Linear hyperkeratosis on palms and palmar/flexor aspects of fingers; focal hyperkeratosis at trauma/pressure-prone plantar sites (heel, forefoot, great toe); fissuring may occur; phenotype often skin-limited but DSP-related disease can overlap with woolly/curly hair and cardiomyopathy in some families (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, guerra2018hereditarypalmoplantarkeratodermas. pages 40-43, armstrong1999haploinsufficiencyofdesmoplakin pages 1-2, armstrong1999haploinsufficiencyofdesmoplakin pages 2-3) | Guerra et al., 2018, JEADV, DOI: 10.1111/jdv.14902, https://doi.org/10.1111/jdv.14902 (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, guerra2018hereditarypalmoplantarkeratodermas. pages 40-43); Petrof et al., 2012, Br J Dermatol, DOI: 10.1111/j.1365-2133.2011.10640.x, https://doi.org/10.1111/j.1365-2133.2011.10640.x (petrof2012desmosomalgenodermatoses pages 2-4, petrof2012desmosomalgenodermatoses pages 1-2); Armstrong et al., 1999, Hum Mol Genet, DOI: 10.1093/hmg/8.1.143, https://doi.org/10.1093/hmg/8.1.143 (armstrong1999haploinsufficiencyofdesmoplakin pages 1-2, armstrong1999haploinsufficiencyofdesmoplakin pages 2-3) |


*Table: This table summarizes the canonical naming, OMIM identifier, gene, inheritance, onset, and defining clinical features of DSP-related striate palmoplantar keratoderma type II. It is useful as a compact normalization artifact for disease knowledge base mapping and curation.*

---

## 1. Disease information

### 1.1 What is the disease?
SPPK2 is an inherited disorder of keratinization with **persistent palmoplantar hyperkeratosis**, classically presenting as **linear hyperkeratosis** on the palms/palmar aspects of fingers and **focal hyperkeratosis** at trauma-prone plantar sites, often with **fissures** and a progressive course (“progrediens”). (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)

### 1.2 Key identifiers (from retrieved literature)
* **OMIM:** **612908** (explicitly listed for Striate PPK type II and also referred to as **PPKS2** in OMIM-oriented reviews). (petrof2012desmosomalgenodermatoses pages 2-4, guerra2018hereditarypalmoplantarkeratodermas. pages 37-40)
* **Gene:** **DSP (desmoplakin)**. (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)

**Not found in the retrieved sources:** Orphanet ID, ICD-10/ICD-11, MeSH, MONDO ID. The retrieved full texts did not include these mappings; they would require direct database lookup outside the present evidence set. (petrof2012desmosomalgenodermatoses pages 2-4, guerra2018hereditarypalmoplantarkeratodermas. pages 37-40)

### 1.3 Synonyms / alternative names
* Striate PPK type II (DSP-related) (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)
* Striate palmoplantar keratoderma (SPPK); striate PPK (petrof2012desmosomalgenodermatoses pages 2-4, petrof2012desmosomalgenodermatoses pages 1-2)
* **PPKS2** (OMIM label for DSP-related striate PPK) (petrof2012desmosomalgenodermatoses pages 2-4, petrof2012desmosomalgenodermatoses pages 1-2)

### 1.4 Evidence source type
The disease entity is defined in **aggregated disease-level resources and reviews** (clinicogenetic classifications) as well as **family-based primary genetic studies** identifying causal DSP variants. (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, armstrong1999haploinsufficiencyofdesmoplakin pages 2-3, petrof2012desmosomalgenodermatoses pages 2-4)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants in **DSP** (desmoplakin). SPPK2 is typically associated with **heterozygous loss-of-function** DSP variants causing **haploinsufficiency**. (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, guerra2018hereditarypalmoplantarkeratodermas. pages 8-12, armstrong1999haploinsufficiencyofdesmoplakin pages 2-3)

### 2.2 Risk factors
#### Genetic risk factors
* **DSP truncating variants** (nonsense/frameshift) are strongly implicated in striate/focal palmoplantar keratoderma and can also confer cardiomyopathy/arrhythmia risk depending on variant context. (karvonen2022anoveldesmoplakin pages 1-1, pigors2015desmoplakinmutationswith pages 1-2, gram2025clinicalandgenetic pages 5-6)

#### Environmental/physiologic modifiers
* Lesions localize to **mechanically stressed**/pressure areas, implicating **friction and repetitive trauma** as phenotype modifiers. (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3, guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)

### 2.3 Protective factors / gene–environment interactions
No protective genetic or environmental factors were identified in the retrieved evidence set for DSP-related striate PPK.

---

## 3. Phenotypes

### 3.1 Core cutaneous phenotype (SPPK2)
From a clinicogenetic classification table, DSP-related SPPK2 shows: (i) **linear palmar hyperkeratosis** affecting palms and palmar aspects of fingers; (ii) **focal plantar hyperkeratosis** at **trauma-prone sites**; (iii) **fissures**; (iv) progressive course (progrediens). Histology/EM correlates are summarized in the Mechanism section. (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)

### 3.2 Expanded DSP phenotype spectrum (cardiocutaneous overlap)
A 2022 multigenerational family with heterozygous DSP frameshift **c.2493delA (p.Glu831Aspfs*33)** presented with: variable **PPK** (mainly focal; 8/9 carriers affected), **aquagenic whitening** (5/9), occasional **hyperhidrosis** (2/9), frequent **wavy/curly hair** (13 family members), and **dilated cardiomyopathy (DCM)** with mostly mild arrhythmias. PPK onset ranged **1–30 years**, showing variable expressivity. (karvonen2022anoveldesmoplakin pages 4-4, karvonen2022anoveldesmoplakin pages 3-3)

### 3.3 Pain and quality-of-life impact
Hereditary PPKs commonly cause pain and functional limitation. A striate PPK case report described “longstanding pain” and activity-related worsening (sports, manual labor/farming), reflecting occupational impact. (fukaura2017striatepalmoplantarkeratoderma pages 1-2)

In broader inherited PPK management literature, plantar pain can have a **neuropathic component** and “can be severe enough to require ambulatory aids,” with disease exacerbated by weight-bearing and work demands. (thomas2020diagnosisandmanagement pages 5-6)

### 3.4 Suggested HPO terms (examples)
**Cutaneous:**
* Palmoplantar keratoderma (HP:0000982)
* Hyperkeratosis (HP:0000962)
* Fissure (skin fissures) (HP:0100782)
* Palmoplantar hyperhidrosis (HP:0007410)
* Aquagenic wrinkling/whitening of palms (often mapped as aquagenic keratoderma; term availability varies)

**Hair:**
* Woolly hair / abnormal hair texture (e.g., woolly/curly hair) (HP:0002222 for woolly hair; HP:0002283 for abnormal hair texture)

**Cardiac:**
* Dilated cardiomyopathy (HP:0001644)
* Cardiac arrhythmia (HP:0011675)

(Phenotype presence/attribution varies by variant and family; see Karvonen family frequencies above.) (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43, karvonen2022anoveldesmoplakin pages 4-4, thomas2020diagnosisandmanagement pages 5-6)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
**DSP (desmoplakin)** is the causal gene for SPPK2 (OMIM 612908/PPKS2). (petrof2012desmosomalgenodermatoses pages 2-4, guerra2018hereditarypalmoplantarkeratodermas. pages 37-40)

### 4.2 Pathogenic variant classes and examples
**Dominant SPPK2** is typically due to heterozygous **truncating** variants causing haploinsufficiency.
* Classic family: **DSP c.1323C>T, p.Gln331Ter (Q331X)**; mutant transcript absent (nonsense-mediated decay), consistent with haploinsufficiency. (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3)
* Cardiocutaneous family: **DSP c.2493delA, p.Glu831Aspfs*33**, AD segregation with PPK and DCM/arrhythmias. (karvonen2022anoveldesmoplakin pages 1-1, karvonen2022anoveldesmoplakin pages 4-4)
* PPK cohort (Denmark): truncating DSP variants **c.2821C>T (p.Arg941Ter)** (pathogenic) and **c.175dupA (p.Thr59Asnfs*34)** (likely pathogenic). (gram2025clinicalandgenetic pages 5-6)

### 4.3 Genotype–phenotype correlations
* **Skin-limited phenotype:** reported for early DSP haploinsufficiency families (SPPK only). (petrof2012desmosomalgenodermatoses pages 1-2)
* **Cardiocutaneous phenotype:** DSP variants can also produce woolly/curly hair and cardiomyopathy/arrhythmia (Carvajal/Naxos-related spectrum), with regular cardiac evaluation recommended. (pigors2015desmoplakinmutationswith pages 1-2, petrof2012desmosomalgenodermatoses pages 2-4)

### 4.4 Population genetics / recent quantitative data (cardiac risk)
In a 2023 multicenter cohort of individuals with **DSP truncating variants** (DSPtv) and any cardiac phenotype, **ventricular arrhythmia occurred in 56 (33%)**; variant location and proband status were independent risk factors. Case variants were enriched in regions predicted to trigger **nonsense-mediated decay** of both major DSP isoforms versus gnomAD control truncations (**83.6% vs 16.4%**, P<0.0001). This provides a quantitative basis for risk-stratified cardiac management in DSPtv carriers, including those identified initially by skin findings. (hoorntje2023variantlocationis pages 1-2)

---

## 5. Environmental information
SPPK2 is primarily genetic. The most consistent non-genetic contributor evidenced here is **mechanical stress** (friction/pressure) as a modifier of lesion distribution and severity. (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3, guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (genotype → tissue defect → phenotype)
**DSP encodes desmoplakin**, a key desmosomal plaque protein that links desmosomes to **keratin intermediate filaments**. Heterozygous truncating variants can yield **haploinsufficiency** (via NMD), weakening desmosome–keratin anchoring. Under high mechanical load in palms/soles, reduced adhesion resilience promotes epidermal micro-separation and compensatory hyperkeratosis, producing striate/focal keratoderma and fissuring. (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3, armstrong1999haploinsufficiencyofdesmoplakin pages 3-5)

### 6.2 Histopathology / ultrastructure
In DSP haploinsufficiency striate PPK, reported findings include:
* Histology: **hyperkeratosis, acanthosis**, **widened intercellular spaces**/loosening of cell–cell connections, and “abnormal bunching of the keratin.” (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3)
* EM: **desmosomes lacking inner plaques**, abnormal keratin filament connections, and other desmosome–IF linkage abnormalities. (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3, armstrong1999haploinsufficiencyofdesmoplakin pages 3-5)

A clinicogenetic classification of DSP striate PPK II lists: histology with “**hyperkeratosis, widening of intercellular spaces and condensation of the keratin filament network**” and EM with “**markedly reduced desmosome number**… dense perinuclear tonofilament bundles.” (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)

### 6.3 Cardiocutaneous extension
DSP is also essential in the heart; recessive or certain truncating variants can cause syndromes with PPK + woolly hair + DCM (Carvajal spectrum). Mechanistically, truncations that ablate the **tail domain essential for intermediate filament binding** can disrupt desmosome anchoring in both epidermis and myocardium. (norgett2000recessivemutationin pages 1-2, lee2021mutationsingenes pages 6-6)

### 6.4 Suggested ontology terms
**GO Biological Process (examples):**
* Cell–cell adhesion (GO:0098609)
* Desmosome organization (GO:0031581)
* Keratinocyte differentiation (GO:0030216)

**GO Cellular Component (examples):**
* Desmosome (GO:0030057)
* Intermediate filament (GO:0005882)

**Cell Ontology (examples):**
* Keratinocyte (CL:0000312)

(These ontology terms are proposed as mechanistically relevant; the retrieved sources support desmosome–IF anchoring and keratinocyte adhesion defects.) (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3, lee2021mutationsingenes pages 6-6)

---

## 7. Anatomical structures affected

**Primary:**
* Palmar skin and plantar skin (palmoplantar epidermis). (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)

**Secondary/possible extracutaneous (variant-dependent):**
* Hair shaft/hair follicles (woolly/curly hair). (karvonen2022anoveldesmoplakin pages 4-4, thomas2020diagnosisandmanagement pages 5-6)
* Heart (dilated cardiomyopathy/arrhythmias). (karvonen2022anoveldesmoplakin pages 1-1, thomas2020diagnosisandmanagement pages 5-6)

**Suggested UBERON terms (examples):** palm skin; sole of foot; epidermis; heart left ventricle.

---

## 8. Temporal development

* **Onset:** childhood to early adulthood for classic SPPK2; in a DSP frameshift family, onset ranged **1–30 years**. (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, karvonen2022anoveldesmoplakin pages 4-4)
* **Course:** progressive (“progrediens”) with fissuring. (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)
* **Cardiac manifestations:** may occur later than skin findings; in the Karvonen family, dermatologic signs preceded adult-onset cardiac symptoms. (karvonen2022anoveldesmoplakin pages 1-1)

---

## 9. Inheritance and population

### 9.1 Inheritance
* **Autosomal dominant** inheritance for striate PPK type II (DSP-related) in clinicogenetic classifications and classic DSP families. (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, armstrong1999haploinsufficiencyofdesmoplakin pages 2-3)

### 9.2 Epidemiology
Robust population-based prevalence/incidence for hereditary PPK—and specifically striate PPK—was not found in the retrieved evidence set.
* A 2021 cohort study states: “**The exact incidence and prevalence of hereditary PPK is not known**.” In that clinical series (n=64), striate PPK was not observed. (harjama2021hereditarypalmoplantarkeratoderma pages 1-4)
* A 2004 report describes striated PPK as “very rare” but provides no numeric rate. (rubegni2004acralmalignantmelanoma pages 1-3)

---

## 10. Diagnostics

### 10.1 Clinical diagnosis
Diagnosis begins with pattern recognition (diffuse vs focal/striate vs punctate) and assessment of associated features (pain/blistering, sweating, infection, hair/nails/teeth, and systemic features). (thomas2020diagnosisandmanagement pages 1-2)

### 10.2 Histopathology
DSP/DSG1-related striate PPKs can show widening of intercellular spaces/acantholysis (disadhesion) in suprabasal layers and characteristic EM changes in desmosomes/tonofilaments. (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43, guerra2018hereditarypalmoplantarkeratodermas. pages 8-12)

### 10.3 Genetic testing
Next-generation sequencing panels spanning PPK genes (including DSP) with Sanger confirmation are used in practice and are recommended in reviews because of clinical overlap among PPK subtypes. (karvonen2022anoveldesmoplakin pages 1-1, karvonen2022anoveldesmoplakin pages 2-2)

### 10.4 Cardiac evaluation (critical in DSP-associated disease)
Because DSP mutations can underlie cardiocutaneous syndromes, PPK may be an early marker. One study emphasizes: **PPK should trigger genetic testing** to reveal mutations “with possible related cardiac disease,” with family evaluation by echocardiography, ECG, Holter, and cardiac MRI. (karvonen2022anoveldesmoplakin pages 1-1)

A management review states: patients with **striate keratoderma/PPK and woolly hair should have cardiac investigations**, and family members should be screened (recognizing both AR and AD patterns in related syndromes). (thomas2020diagnosisandmanagement pages 5-6)

### 10.5 Differential diagnosis (examples)
Differentials include other inherited PPKs (DSG1-, KRT1-, KRT9-related) and acquired palmoplantar hyperkeratoses (psoriasis/eczema), and histologic differentials for acantholysis (e.g., pemphigus) where clinical blistering patterns differ. (metze2026desmosomaltypeacantholysis—anew pages 18-19)

---

## 11. Outcomes / prognosis
SPPK2 is typically chronic and skin-limited, but prognosis changes substantially if DSP variants confer cardiomyopathy risk.
* DSPtv cardiomyopathy cohorts show substantial arrhythmic burden (ventricular arrhythmia 33%), supporting the importance of surveillance. (hoorntje2023variantlocationis pages 1-2)

No survival estimates specific to SPPK2 skin-only disease were identified in the retrieved evidence set.

---

## 12. Treatment

### 12.1 Current applications (real-world management)
Management is largely symptomatic and focused on mechanical load reduction and hyperkeratosis control:
* **Emollients + keratolytics + mechanical debridement/paring** are core measures. (thomas2020diagnosisandmanagement pages 2-2, has2016palmoplantarkeratodermasclinical pages 15-17)
* **Footwear modification/custom insoles** to off-load pressure and reduce pain. (thomas2020diagnosisandmanagement pages 5-6)
* **Oral retinoids** (e.g., acitretin/isotretinoin) used for hyperkeratosis, with variable benefit and potential worsening of pain/erythema; histopathologic subtype matters for retinoid tolerability. (has2016palmoplantarkeratodermasclinical pages 15-17, thomas2020diagnosisandmanagement pages 3-4)
* **Botulinum toxin** may help when hyperhidrosis contributes to symptoms and can reduce pain in some patients. (thomas2020diagnosisandmanagement pages 5-6)
* Treat **secondary bacterial/fungal infections** when present. (has2016palmoplantarkeratodermasclinical pages 15-17)

A practical, MAXO-mapped management summary is provided in artifact-02.

| Domain | Intervention / Recommendation | Purpose / Notes | MAXO term suggestion | Evidence citation |
|---|---|---|---|---|
| Symptomatic skin care | Emollients | Regular topical emollients reduce scaling/thickness and help prevent painful fissures; supportive rather than curative. | MAXO: topical skin barrier/emollient therapy | (has2016palmoplantarkeratodermasclinical pages 13-15, has2016palmoplantarkeratodermasclinical pages 15-17) |
| Symptomatic skin care | Topical keratolytics | Routine keratolytics are standard symptomatic care to reduce hyperkeratosis; often combined with emollients. | MAXO: keratolytic topical therapy | (thomas2020diagnosisandmanagement pages 2-2, has2016palmoplantarkeratodermasclinical pages 13-15, has2016palmoplantarkeratodermasclinical pages 15-17) |
| Symptomatic skin care | Mechanical debridement / paring / podiatry | Mechanical reduction of callus burden is a core management measure; often performed by podiatry/professional foot care. | MAXO: mechanical debridement procedure | (thomas2020diagnosisandmanagement pages 2-2, thomas2020diagnosisandmanagement pages 5-6, has2016palmoplantarkeratodermasclinical pages 15-17) |
| Symptomatic skin care | Footwear modification / customized insoles / pressure off-loading | Reduces pressure-related pain and recurrent plantar thickening at trauma-prone sites. | MAXO: orthotic support / pressure off-loading | (thomas2020diagnosisandmanagement pages 5-6, has2016palmoplantarkeratodermasclinical pages 15-17) |
| Pharmacotherapy | Oral retinoids (acitretin, isotretinoin; sometimes alitretinoin) | Main systemic option for hyperkeratosis; benefit is variable and may worsen pain/erythema. Histopathologic subtype matters because epidermolytic PPK can worsen with retinoids. | MAXO: systemic retinoid therapy | (thomas2020diagnosisandmanagement pages 2-2, thomas2020diagnosisandmanagement pages 5-6, thomas2020diagnosisandmanagement pages 4-5, has2016palmoplantarkeratodermasclinical pages 15-17, thomas2020diagnosisandmanagement pages 3-4) |
| Pharmacotherapy | Topical retinoids / calcipotriol | Used in some inherited PPKs as adjunctive topical therapy; response variable. | MAXO: topical retinoid therapy / topical vitamin D analog therapy | (thomas2020diagnosisandmanagement pages 2-2) |
| Supportive treatment | Botulinum toxin for hyperhidrosis / plantar pain | Used when sweating contributes to maceration, pain, or worsening plantar symptoms. | MAXO: botulinum toxin injection | (thomas2020diagnosisandmanagement pages 2-2, thomas2020diagnosisandmanagement pages 5-6) |
| Infection management | Treat bacterial or fungal superinfection | Microbiologic assessment and targeted antibiotics/antifungals are recommended because infection commonly complicates fissured/scaly keratoderma. | MAXO: antimicrobial therapy | (thomas2020diagnosisandmanagement pages 2-2, has2016palmoplantarkeratodermasclinical pages 13-15, has2016palmoplantarkeratodermasclinical pages 15-17, thomas2020diagnosisandmanagement pages 3-4) |
| Procedural treatment | Surgical or laser treatment for recalcitrant focal lesions | Reserved for severe/refractory focal keratoderma; outcomes variable and case-dependent. | MAXO: surgical excision / laser ablation | (thomas2020diagnosisandmanagement pages 2-2, thomas2020diagnosisandmanagement pages 4-5, has2016palmoplantarkeratodermasclinical pages 15-17) |
| Genetic diagnostics | Multigene NGS panel including DSP and other PPK genes, with Sanger confirmation | Recommended for clinically suspected inherited PPK because subtype overlap is common; DSP testing is especially important when hair changes or cardiomyopathy risk is suspected. | MAXO: multigene panel testing / confirmatory Sanger sequencing | (karvonen2022anoveldesmoplakin pages 2-2, karvonen2022anoveldesmoplakin pages 1-1) |
| Genetic diagnostics | Cascade family testing for relatives of a DSP-variant carrier | Enables early identification of at-risk relatives for dermatologic and cardiac monitoring. | MAXO: familial cascade genetic testing | (karvonen2022anoveldesmoplakin pages 4-4, karvonen2022anoveldesmoplakin pages 1-1) |
| Cardiac risk assessment | Baseline cardiology evaluation for DSP variant carriers | DSP-associated PPK can precede cardiomyopathy/arrhythmia; baseline evaluation should not wait for cardiac symptoms. | MAXO: cardiovascular system evaluation | (pigors2015desmoplakinmutationswith pages 1-2, karvonen2022anoveldesmoplakin pages 1-1) |
| Cardiac surveillance | ECG and ambulatory Holter monitoring | Used to detect conduction disease, extrasystoles, and arrhythmias in DSP carriers. | MAXO: electrocardiographic monitoring | (karvonen2022anoveldesmoplakin pages 1-1, karvonen2022anoveldesmoplakin pages 2-2) |
| Cardiac surveillance | Echocardiography | Standard structural/functional surveillance for dilated or arrhythmogenic cardiomyopathy in DSP carriers. | MAXO: echocardiography | (karvonen2022anoveldesmoplakin pages 1-1, karvonen2022anoveldesmoplakin pages 2-2) |
| Cardiac surveillance | Cardiac MRI (CMR) | Useful for ventricular structure/function and arrhythmogenic/dilated cardiomyopathy characterization. | MAXO: cardiac magnetic resonance imaging | (karvonen2022anoveldesmoplakin pages 4-4, karvonen2022anoveldesmoplakin pages 1-1, karvonen2022anoveldesmoplakin pages 2-2) |
| Long-term management | Ongoing/lifelong cardiac follow-up for DSP truncating-variant carriers | Supported by cardiocutaneous case series and broader DSP truncating-variant data showing substantial ventricular arrhythmia burden. | MAXO: longitudinal cardiac surveillance | (lin2026aframeshiftvariation pages 4-6, hoorntje2023variantlocationis pages 1-2) |
| Counseling | Genetic counseling regarding autosomal dominant transmission and cardiocutaneous risk | Important for reproductive counseling, family screening, and explaining variable expressivity (skin, hair, heart). | MAXO: genetic counseling | (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40, karvonen2022anoveldesmoplakin pages 1-1) |


*Table: This table summarizes practical diagnostic and management actions for DSP-related striate palmoplantar keratoderma, including skin-directed therapies, genetic testing, and cardiac surveillance. It is useful because DSP-associated disease can extend beyond the skin to arrhythmia and cardiomyopathy, so management must integrate dermatology and cardiology.*

### 12.2 Recent developments / emerging therapies (evidence in retrieved set)
The 2020 review notes early promise for targeted approaches (e.g., rapamycin, siRNA in related keratin disorders), but these were not specific, established therapies for DSP-related SPPK2 in the retrieved passages and remain investigational. (thomas2020diagnosisandmanagement pages 5-6)

No DSP-specific gene therapy or RNA therapy trials for SPPK2 were identified in the retrieved clinical trial search results.

---

## 13. Prevention
No primary prevention is available for a dominantly inherited genodermatosis. Prevention focuses on:
* **Genetic counseling** and **cascade testing** in families. (karvonen2022anoveldesmoplakin pages 1-1)
* **Tertiary prevention**: prevention of fissures/pain via skin care and off-loading; prevention of sudden cardiac events via cardiology surveillance and management in at-risk DSP variant carriers. (hoorntje2023variantlocationis pages 1-2, has2016palmoplantarkeratodermasclinical pages 15-17)

---

## 14. Other species / natural disease
No naturally occurring veterinary DSP striate PPK analogs were identified in the retrieved evidence set.

---

## 15. Model organisms / experimental systems
Although DSP-specific keratoderma models were not directly retrieved as full texts here, multiple **desmosome perturbation** models support the mechanistic framework:
* **Epidermis-restricted plakoglobin (Jup) knockout mice** “largely recapitulated” human palmoplantar keratoderma with overcornification/thickening and disrupted desmosomes. (li2012lackofplakoglobin pages 1-1)
* **Epidermis-specific iASPP deficiency** causes palmoplantar abnormalities resembling keratoderma with incomplete penetrance and provides evidence linking desmosome stability pathways to keratoderma. (dedeic2018cellautonomousrole pages 2-4)

These models support the concept that impaired desmosome assembly/stability and keratinocyte adhesion is sufficient to drive keratoderma-like phenotypes.

---

## Key recent/authoritative sources (with URLs and publication dates)
* Guerra et al., *JEADV* (May 2018): classification of non-syndromic PPKs including Striate PPK type II with OMIM 612908 and DSP, plus histology/EM features. https://doi.org/10.1111/jdv.14902 (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43)
* Karvonen et al., *JEADV* (May 2022): DSP c.2493delA family; quantified cutaneous and cardiac features, onset range, and recommendation for genetic testing with cardiac evaluation. https://doi.org/10.1111/jdv.18164 (karvonen2022anoveldesmoplakin pages 4-4, karvonen2022anoveldesmoplakin pages 1-1)
* Hoorntje et al., *Circulation: Genomic and Precision Medicine* (Feb 2023): DSP truncating variants cardiomyopathy cohort; ventricular arrhythmia 33%; variant location and NMD enrichment vs gnomAD controls. https://doi.org/10.1161/circgen.121.003672 (hoorntje2023variantlocationis pages 1-2)
* Gram et al., *JAMA Dermatology* (Feb 2025; online 2024): large PPK cohort with DSP truncating variants and cardiocutaneous clues (woolly/curly hair) and symptom improvement statistic (3/5). https://doi.org/10.1001/jamadermatol.2024.4824 (gram2025clinicalandgenetic pages 5-6)

---

## Limitations of this report
* Orphanet/ICD/MeSH/MONDO identifiers were not present in the retrieved full-text sources and therefore cannot be provided with evidence-based citations here.
* Some therapy and epidemiology elements for SPPK2 specifically remain based on broader inherited PPK management literature and small DSP family series; no RCT-level DSP-specific treatment evidence was found in the retrieved set.

---

### Artifact: DSP variants & phenotype spectrum
| Study (first author, year) | PMID | Variant (cDNA, protein) | Zygosity | Phenotype (PPK pattern, hair findings, cardiomyopathy/arrhythmia) | Notable quantitative data | URL/DOI |
|---|---|---|---|---|---|---|
| Armstrong, 1999 |  | c.1323C>T, p.Gln331Ter (Q331X) | Heterozygous | Classic DSP-related striate palmoplantar keratoderma: linear hyperkeratosis on flexor fingers/palms, focal plantar hyperkeratosis at pressure sites; phenotype restricted to skin in reported kindred; no frank blistering | Autosomal dominant pedigree; maximum LOD 10.67; onset in first or early second decade; mutant transcript not detected, supporting haploinsufficiency (armstrong1999haploinsufficiencyofdesmoplakin pages 1-2, armstrong1999haploinsufficiencyofdesmoplakin pages 2-3) | https://doi.org/10.1093/hmg/8.1.143 |
| Karvonen, 2022 |  | c.2493delA, p.Glu831Aspfs*33 | Heterozygous | Focal/striate-spectrum PPK as early sign; curly/wavy hair in family; dilated cardiomyopathy and arrhythmias in carriers | Variant in 9/21 tested relatives; PPK onset range 1-30 years; aquagenic whitening in 5/9; palmoplantar hyperhidrosis in 2/9; dermatologic signs preceded adult-onset cardiac symptoms (karvonen2022anoveldesmoplakin pages 4-4, karvonen2022anoveldesmoplakin pages 1-1) | https://doi.org/10.1111/jdv.18164 |
| Pigors, 2015 |  | c.7566_7567delAAinsC, p.Arg2522Serfs*39 |  | Palmoplantar keratoderma with woolly hair/hypotrichosis and cardiac manifestations in DSP cardiocutaneous spectrum | Example case developed hypotrichosis and striate PPK from age 5; review notes >120 DSP mutations reported and emphasizes regular cardiac examinations (pigors2015desmoplakinmutationswith pages 1-2) | https://doi.org/10.2340/00015555-1974 |
| Pigors, 2015 |  | c.7756C>T, p.Arg2586Ter |  | Palmoplantar keratoderma with woolly hair/hypotrichosis and cardiomyopathy/arrhythmogenic overlap | Cardiac disease may progress to severe left ventricular failure; genotype-phenotype correlation noted as complex (pigors2015desmoplakinmutationswith pages 1-2) | https://doi.org/10.2340/00015555-1974 |
| Pigors, 2015 |  | c.2131_2132delAG plus c.1067C>A, p.Thr356Lys | Compound / biallelic context reported | Palmoplantar keratoderma with hair abnormalities and cardiac involvement in syndromic DSP disease | Report highlights variable expression and need for early diagnosis with regular cardiac follow-up (pigors2015desmoplakinmutationswith pages 1-2) | https://doi.org/10.2340/00015555-1974 |
| Gram, 2025 |  | c.2821C>T, p.Arg941Ter |  | PPK with cardiocutaneous overlap; woolly/curly hair noted as diagnostic clue in DSP-variant families | In Danish cohort, DSP-variant participants small in number; 3/5 (60%) reported symptom improvement; striate subtype represented by 3 cases overall (gram2025clinicalandgenetic pages 5-6) | https://doi.org/10.1001/jamadermatol.2024.4824 |
| Gram, 2025 |  | c.175dupA, p.Thr59Asnfs*34 |  | PPK with risk of associated disease, including cardiomyopathy overlap in DSP-related cases | Same cohort context as above; supports DSP as a “PPK with risk of associated diseases” gene (gram2025clinicalandgenetic pages 5-6) | https://doi.org/10.1001/jamadermatol.2024.4824 |
| Hoorntje, 2023 |  | Multiple DSP truncating variants (DSPtv), location-dependent risk | Mostly heterozygous truncating | DSP truncating variants associated with cardio-cutaneous spectrum including striate palmoplantar keratoderma; cardiac phenotype includes arrhythmogenic cardiomyopathy/ventricular arrhythmia | Multicenter cohort: 98 probands + 72 family members; 146 clinically affected; ventricular arrhythmia in 56/170 (33% of all included individuals); case variants enriched in NMD-competent regions affecting both isoforms: 148/177 (83.6%) vs 29/124 gnomAD control variants (16.4%), P<0.0001 (hoorntje2023variantlocationis pages 1-2) | https://doi.org/10.1161/CIRCGEN.121.003672 |
| Pantou, 2023 |  | c.8586delC, p.Ser2863Hisfs*20 | Homozygous in proband | Arrhythmogenic left ventricular cardiomyopathy without typical dermatologic signs; included here as DSP cardiocutaneous-spectrum comparator highlighting C-terminal functional importance | Brother died suddenly at 18 during exercise; heterozygous mother had mild arrhythmic phenotype; no classic PPK in proband despite DSP C-terminal truncation (hoorntje2023variantlocationis pages 1-2) | https://doi.org/10.1186/s12920-023-01527-6 |
| Lin, 2026 |  | c.6218_6219dup, p.Ala2074Ter | Heterozygous | Atypical epidermolytic/acantholytic PPK distinct from classic striate PPK; prior literature summary in same paper includes woolly hair, DCM, ACM in truncating DSP cases | Variant absent from gnomAD; paper tabulates recent DSP-PPK cases including Karvonen 2022 family (9 cases) and recommends lifelong ECG/echocardiographic surveillance for DSP carriers (lin2026aframeshiftvariation pages 4-6) | https://doi.org/10.3389/fmed.2025.1728762 |


*Table: This table summarizes reported DSP variants relevant to striate palmoplantar keratoderma type II and the broader DSP cardiocutaneous spectrum, including cutaneous, hair, and cardiac findings. It highlights variant-specific phenotype patterns and recent quantitative risk data useful for diagnosis and surveillance.*

References

1. (guerra2018hereditarypalmoplantarkeratodermas. pages 37-40): L. Guerra, Marco Castori, B. Didona, D. Castiglia, and Giovanna Zambruno. Hereditary palmoplantar keratodermas. part i. non‐syndromic palmoplantar keratodermas: classification, clinical and genetic features. Journal of the European Academy of Dermatology and Venereology, 32:704-719, May 2018. URL: https://doi.org/10.1111/jdv.14902, doi:10.1111/jdv.14902. This article has 92 citations and is from a domain leading peer-reviewed journal.

2. (armstrong1999haploinsufficiencyofdesmoplakin pages 2-3): D. Armstrong, K. Mckenna, P. Purkis, K. Green, R. Eady, I. Leigh, and A. Hughes. Haploinsufficiency of desmoplakin causes a striate subtype of palmoplantar keratoderma. Human molecular genetics, 8 1:143-8, Jan 1999. URL: https://doi.org/10.1093/hmg/8.1.143, doi:10.1093/hmg/8.1.143. This article has 361 citations and is from a domain leading peer-reviewed journal.

3. (petrof2012desmosomalgenodermatoses pages 2-4): G. Petrof, Jemima E. Mellerio, and John A. McGrath. Desmosomal genodermatoses. British Journal of Dermatology, 166:36-45, Jan 2012. URL: https://doi.org/10.1111/j.1365-2133.2011.10640.x, doi:10.1111/j.1365-2133.2011.10640.x. This article has 89 citations and is from a highest quality peer-reviewed journal.

4. (karvonen2022anoveldesmoplakin pages 1-1): V. Karvonen, L. Harjama, K. Heliö, K. Kettunen, O. Elomaa, J.W. Koskenvuo, J. Kere, S. Weckström, M. Holmström, J. Saarela, A. Ranki, T. Heliö, and K. Hannula‐Jouppi. A novel desmoplakin mutation causes dilated cardiomyopathy with palmoplantar keratoderma as an early clinical sign. Journal of the European Academy of Dermatology and Venereology, 36:1349-1358, May 2022. URL: https://doi.org/10.1111/jdv.18164, doi:10.1111/jdv.18164. This article has 11 citations and is from a domain leading peer-reviewed journal.

5. (guerra2018hereditarypalmoplantarkeratodermas. pages 40-43): L. Guerra, Marco Castori, B. Didona, D. Castiglia, and Giovanna Zambruno. Hereditary palmoplantar keratodermas. part i. non‐syndromic palmoplantar keratodermas: classification, clinical and genetic features. Journal of the European Academy of Dermatology and Venereology, 32:704-719, May 2018. URL: https://doi.org/10.1111/jdv.14902, doi:10.1111/jdv.14902. This article has 92 citations and is from a domain leading peer-reviewed journal.

6. (armstrong1999haploinsufficiencyofdesmoplakin pages 1-2): D. Armstrong, K. Mckenna, P. Purkis, K. Green, R. Eady, I. Leigh, and A. Hughes. Haploinsufficiency of desmoplakin causes a striate subtype of palmoplantar keratoderma. Human molecular genetics, 8 1:143-8, Jan 1999. URL: https://doi.org/10.1093/hmg/8.1.143, doi:10.1093/hmg/8.1.143. This article has 361 citations and is from a domain leading peer-reviewed journal.

7. (petrof2012desmosomalgenodermatoses pages 1-2): G. Petrof, Jemima E. Mellerio, and John A. McGrath. Desmosomal genodermatoses. British Journal of Dermatology, 166:36-45, Jan 2012. URL: https://doi.org/10.1111/j.1365-2133.2011.10640.x, doi:10.1111/j.1365-2133.2011.10640.x. This article has 89 citations and is from a highest quality peer-reviewed journal.

8. (guerra2018hereditarypalmoplantarkeratodermas. pages 8-12): L. Guerra, Marco Castori, B. Didona, D. Castiglia, and Giovanna Zambruno. Hereditary palmoplantar keratodermas. part i. non‐syndromic palmoplantar keratodermas: classification, clinical and genetic features. Journal of the European Academy of Dermatology and Venereology, 32:704-719, May 2018. URL: https://doi.org/10.1111/jdv.14902, doi:10.1111/jdv.14902. This article has 92 citations and is from a domain leading peer-reviewed journal.

9. (pigors2015desmoplakinmutationswith pages 1-2): M. Pigors, A. Schwieger-Briel, R. Cosgarea, A. Diaconeasa, L. Bruckner-Tuderman, T. Fleck, and C. Has. Desmoplakin mutations with palmoplantar keratoderma, woolly hair and cardiomyopathy. Acta dermato-venereologica, 95 3:337-40, Mar 2015. URL: https://doi.org/10.2340/00015555-1974, doi:10.2340/00015555-1974. This article has 47 citations and is from a domain leading peer-reviewed journal.

10. (gram2025clinicalandgenetic pages 5-6): Stine Bjørn Gram, Klaus Brusgaard, Ulrikke Lei, Mette Sommerlund, Gabrielle Randskov Vinding, Sondre Olai Kjellevold Sleire, Alex Hørby Christensen, Sanne Pedersen Fast, Rasmus Bach, Anette Bygum, and Lilian Bomme Ousager. Clinical and genetic findings in patients with palmoplantar keratoderma. JAMA Dermatology, 161:157, Feb 2025. URL: https://doi.org/10.1001/jamadermatol.2024.4824, doi:10.1001/jamadermatol.2024.4824. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (karvonen2022anoveldesmoplakin pages 4-4): V. Karvonen, L. Harjama, K. Heliö, K. Kettunen, O. Elomaa, J.W. Koskenvuo, J. Kere, S. Weckström, M. Holmström, J. Saarela, A. Ranki, T. Heliö, and K. Hannula‐Jouppi. A novel desmoplakin mutation causes dilated cardiomyopathy with palmoplantar keratoderma as an early clinical sign. Journal of the European Academy of Dermatology and Venereology, 36:1349-1358, May 2022. URL: https://doi.org/10.1111/jdv.18164, doi:10.1111/jdv.18164. This article has 11 citations and is from a domain leading peer-reviewed journal.

12. (karvonen2022anoveldesmoplakin pages 3-3): V. Karvonen, L. Harjama, K. Heliö, K. Kettunen, O. Elomaa, J.W. Koskenvuo, J. Kere, S. Weckström, M. Holmström, J. Saarela, A. Ranki, T. Heliö, and K. Hannula‐Jouppi. A novel desmoplakin mutation causes dilated cardiomyopathy with palmoplantar keratoderma as an early clinical sign. Journal of the European Academy of Dermatology and Venereology, 36:1349-1358, May 2022. URL: https://doi.org/10.1111/jdv.18164, doi:10.1111/jdv.18164. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (fukaura2017striatepalmoplantarkeratoderma pages 1-2): Ryo Fukaura, T. Takeichi, Y. Okuno, D. Kojima, M. Kono, K. Sugiura, Y. Suga, and M. Akiyama. Striate palmoplantar keratoderma showing transgrediens in a patient harbouring heterozygous nonsense mutations in both dsg1 and serpinb7. Acta dermato-venereologica, 97 3:399-401, Jan 2017. URL: https://doi.org/10.2340/00015555-2553, doi:10.2340/00015555-2553. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (thomas2020diagnosisandmanagement pages 5-6): BR Thomas and EA O'TOOLE. Diagnosis and management of inherited palmoplantar keratodermas. Acta Dermato-Venereologica, 100:adv00094-176, Mar 2020. URL: https://doi.org/10.2340/00015555-3430, doi:10.2340/00015555-3430. This article has 50 citations and is from a domain leading peer-reviewed journal.

15. (hoorntje2023variantlocationis pages 1-2): Edgar T. Hoorntje, Charlotte Burns, Luisa Marsili, Ben Corden, Victoria N. Parikh, Gerard J. te Meerman, Belinda Gray, Ahmet Adiyaman, Richard D. Bagnall, Daniela Q.C.M. Barge-Schaapveld, Maarten P. van den Berg, Marianne Bootsma, Laurens P. Bosman, Gemma Correnti, Johan Duflou, Ruben N. Eppinga, Diane Fatkin, Michael Fietz, Eric Haan, Jan D.H. Jongbloed, Arnaud D. Hauer, Lien Lam, Freyja H.M. van Lint, Amrit Lota, Carlo Marcelis, Hugh J. McCarthy, Anneke M. van Mil, Rogier A. Oldenburg, Nicholas Pachter, R. Nils Planken, Chloe Reuter, Christopher Semsarian, Jasper J. van der Smagt, Tina Thompson, Jitendra Vohra, Paul G.A. Volders, Jaap I. van Waning, Nicola Whiffin, Arthur van den Wijngaard, Ahmad S. Amin, Arthur A.M. Wilde, Gijs van Woerden, Laura Yeates, Dominica Zentner, Euan A. Ashley, Matthew T. Wheeler, James S. Ware, J. Peter van Tintelen, and Jodie Ingles. Variant location is a novel risk factor for individuals with arrhythmogenic cardiomyopathy due to a desmoplakin ( <i>dsp</i> ) truncating variant. Circulation: Genomic and Precision Medicine, Feb 2023. URL: https://doi.org/10.1161/circgen.121.003672, doi:10.1161/circgen.121.003672. This article has 36 citations.

16. (armstrong1999haploinsufficiencyofdesmoplakin pages 3-5): D. Armstrong, K. Mckenna, P. Purkis, K. Green, R. Eady, I. Leigh, and A. Hughes. Haploinsufficiency of desmoplakin causes a striate subtype of palmoplantar keratoderma. Human molecular genetics, 8 1:143-8, Jan 1999. URL: https://doi.org/10.1093/hmg/8.1.143, doi:10.1093/hmg/8.1.143. This article has 361 citations and is from a domain leading peer-reviewed journal.

17. (norgett2000recessivemutationin pages 1-2): E. Norgett, S. Hatsell, L. Carvajal-Huerta, Juan-Carlos Ruiz Cabezas, J. Common, P. Purkis, N. Whittock, I. Leigh, H. Stevens, and D. Kelsell. Recessive mutation in desmoplakin disrupts desmoplakin-intermediate filament interactions and causes dilated cardiomyopathy, woolly hair and keratoderma. Human Molecular Genetics, 9:2761-2766, Nov 2000. URL: https://doi.org/10.1093/hmg/9.18.2761, doi:10.1093/hmg/9.18.2761. This article has 1040 citations and is from a domain leading peer-reviewed journal.

18. (lee2021mutationsingenes pages 6-6): J.Y.W. Lee and J.A. McGrath. Mutations in genes encoding desmosomal proteins: spectrum of cutaneous and extracutaneous abnormalities*. British Journal of Dermatology, 184:596-605, Aug 2021. URL: https://doi.org/10.1111/bjd.19342, doi:10.1111/bjd.19342. This article has 42 citations and is from a highest quality peer-reviewed journal.

19. (harjama2021hereditarypalmoplantarkeratoderma pages 1-4): L. Harjama, V. Karvonen, K. Kettunen, O. Elomaa, E. Einarsdottir, H. Heikkilä, S. Kivirikko, P. Ellonen, J. Saarela, A. Ranki, J. Kere, and K. Hannula-Jouppi. Hereditary palmoplantar keratoderma – phenotypes and mutations in 64 patients. Journal of the European Academy of Dermatology and Venereology, 35:1874-1880, May 2021. URL: https://doi.org/10.1111/jdv.17314, doi:10.1111/jdv.17314. This article has 16 citations and is from a domain leading peer-reviewed journal.

20. (rubegni2004acralmalignantmelanoma pages 1-3): Pietro Rubegni, Sara Poggiali, Aldo Cuccia, Maurizio Biagioli, and Michele Fimiani. Acral malignant melanoma and striated palmoplantar keratoderma (brunauer‐fohs‐siemens syndrome): a fortuitous association? Dermatologic Surgery, 30:1539–1542, Dec 2004. URL: https://doi.org/10.1111/j.1524-4725.2004.30564.x, doi:10.1111/j.1524-4725.2004.30564.x. This article has 13 citations and is from a peer-reviewed journal.

21. (thomas2020diagnosisandmanagement pages 1-2): BR Thomas and EA O'TOOLE. Diagnosis and management of inherited palmoplantar keratodermas. Acta Dermato-Venereologica, 100:adv00094-176, Mar 2020. URL: https://doi.org/10.2340/00015555-3430, doi:10.2340/00015555-3430. This article has 50 citations and is from a domain leading peer-reviewed journal.

22. (karvonen2022anoveldesmoplakin pages 2-2): V. Karvonen, L. Harjama, K. Heliö, K. Kettunen, O. Elomaa, J.W. Koskenvuo, J. Kere, S. Weckström, M. Holmström, J. Saarela, A. Ranki, T. Heliö, and K. Hannula‐Jouppi. A novel desmoplakin mutation causes dilated cardiomyopathy with palmoplantar keratoderma as an early clinical sign. Journal of the European Academy of Dermatology and Venereology, 36:1349-1358, May 2022. URL: https://doi.org/10.1111/jdv.18164, doi:10.1111/jdv.18164. This article has 11 citations and is from a domain leading peer-reviewed journal.

23. (metze2026desmosomaltypeacantholysis—anew pages 18-19): Dieter Metze, Kira Süßmuth, Clemens Metze, Vinzenz Oji, and Heiko Traupe. Desmosomal-type acantholysis—a new histologic pattern related to mutations of genes for desmosomal proteins. Dermatopathology, 13:17, Apr 2026. URL: https://doi.org/10.3390/dermatopathology13020017, doi:10.3390/dermatopathology13020017. This article has 0 citations.

24. (thomas2020diagnosisandmanagement pages 2-2): BR Thomas and EA O'TOOLE. Diagnosis and management of inherited palmoplantar keratodermas. Acta Dermato-Venereologica, 100:adv00094-176, Mar 2020. URL: https://doi.org/10.2340/00015555-3430, doi:10.2340/00015555-3430. This article has 50 citations and is from a domain leading peer-reviewed journal.

25. (has2016palmoplantarkeratodermasclinical pages 15-17): Cristina Has and Kristin Technau‐Hafsi. Palmoplantar keratodermas: clinical and genetic aspects. JDDG: Journal der Deutschen Dermatologischen Gesellschaft, 14:123-140, Feb 2016. URL: https://doi.org/10.1111/ddg.12930, doi:10.1111/ddg.12930. This article has 103 citations.

26. (thomas2020diagnosisandmanagement pages 3-4): BR Thomas and EA O'TOOLE. Diagnosis and management of inherited palmoplantar keratodermas. Acta Dermato-Venereologica, 100:adv00094-176, Mar 2020. URL: https://doi.org/10.2340/00015555-3430, doi:10.2340/00015555-3430. This article has 50 citations and is from a domain leading peer-reviewed journal.

27. (has2016palmoplantarkeratodermasclinical pages 13-15): Cristina Has and Kristin Technau‐Hafsi. Palmoplantar keratodermas: clinical and genetic aspects. JDDG: Journal der Deutschen Dermatologischen Gesellschaft, 14:123-140, Feb 2016. URL: https://doi.org/10.1111/ddg.12930, doi:10.1111/ddg.12930. This article has 103 citations.

28. (thomas2020diagnosisandmanagement pages 4-5): BR Thomas and EA O'TOOLE. Diagnosis and management of inherited palmoplantar keratodermas. Acta Dermato-Venereologica, 100:adv00094-176, Mar 2020. URL: https://doi.org/10.2340/00015555-3430, doi:10.2340/00015555-3430. This article has 50 citations and is from a domain leading peer-reviewed journal.

29. (lin2026aframeshiftvariation pages 4-6): Chunli Lin, Huaqing Chen, Shuqin Lai, Shan Huang, Zimeng Guo, Lang Xie, Wei Zheng, Jing-Fa Lu, Zhaolin Zeng, Chunlei Wan, and Longnian Li. A frameshift variation in the dsp gene causes a novel subtype of atypical epidermolytic palmoplantar keratoderma: case report. Frontiers in Medicine, Jan 2026. URL: https://doi.org/10.3389/fmed.2025.1728762, doi:10.3389/fmed.2025.1728762. This article has 0 citations.

30. (li2012lackofplakoglobin pages 1-1): Deqiang Li, Wenjun Zhang, Ying Liu, Laura S. Haneline, and Weinian Shou. Lack of plakoglobin in epidermis leads to keratoderma. Journal of Biological Chemistry, 287:10435-10443, Mar 2012. URL: https://doi.org/10.1074/jbc.m111.299669, doi:10.1074/jbc.m111.299669. This article has 51 citations and is from a domain leading peer-reviewed journal.

31. (dedeic2018cellautonomousrole pages 2-4): Zinaida Dedeić, Gopinath Sutendra, Ying Hu, Kathryn Chung, Elizabeth A. Slee, Michael J. White, Felix Y. Zhou, Robert D. Goldin, David J. P. Ferguson, Debra McAndrew, Jurgen E. Schneider, and Xin Lu. Cell autonomous role of iaspp deficiency in causing cardiocutaneous disorders. Cell Death & Differentiation, 25:1289-1303, Jan 2018. URL: https://doi.org/10.1038/s41418-017-0039-6, doi:10.1038/s41418-017-0039-6. This article has 20 citations and is from a domain leading peer-reviewed journal.