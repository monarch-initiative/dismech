---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T11:05:31.692728'
end_time: '2026-05-11T11:22:38.251561'
duration_seconds: 1026.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: North Carolina Macular Dystrophy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** North Carolina Macular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **North Carolina Macular Dystrophy** covering all of the
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
- **Disease Name:** North Carolina Macular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **North Carolina Macular Dystrophy** covering all of the
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


# North Carolina Macular Dystrophy (NCMD) — Disease Characteristics Research Report (Mendelian)

## Executive summary (current understanding)
North Carolina macular dystrophy (NCMD; also referenced as MCDR1) is a rare, autosomal dominant, congenital macular malformation/developmental maculopathy with marked variable expressivity but (reported) complete/fully penetrant inheritance in many families. It is typically described as nonprogressive (i.e., lesions are present at birth/early infancy and do not usually advance in “grade”), although vision-threatening complications such as choroidal neovascularization (CNV) can occur and can be treatable with anti-VEGF therapy. Mechanistically, NCMD is now widely characterized as a “retinal enhanceropathy,” in which noncoding single-nucleotide variants (SNVs) and tandem duplications perturb cis-regulatory elements controlling developmental retinal transcription factors—most prominently PRDM13 (MCDR1, chr6) and IRX1 (MCDR3, chr5)—disrupting developmental programs and macula-centric retinal organization. (small2023newnoncodingbase pages 1-2, sompele2022multiomicsapproachdissects pages 1-3)

---

## 1. Disease information

### 1.1 Concise overview
NCMD is a congenital macular developmental disorder typically present at birth and usually described as stable/nonprogressive. A recent report states: “NCMD/MCDR1; OMIM #136550” and defines it as “autosomal dominant, fully penetrant, congenital, nonprogressive macular malformation with marked intrafamilial phenotypic variability.” (small2023newnoncodingbase pages 1-2)

A separate cohort paper states directly: “NCMD is present at birth and rarely progresses.” (green2021northcarolinamacular pages 1-6)

### 1.2 Key identifiers (available from retrieved evidence)
- **OMIM/MIM:** NCMD/MCDR1 **OMIM #136550** / **MIM: 136550** (small2023newnoncodingbase pages 1-2, sompele2022multiomicsprofilingin pages 25-27)
- **Locus designations (used in the literature):**
  - **MCDR1** (chr6q16 region; regulatory variants upstream of PRDM13) (small2023newnoncodingbase pages 1-2, small2016northcarolinamacular pages 1-2, wu2022anoveltandem pages 1-3)
  - **MCDR3** (chr5p15 region; duplications involving/downstream of IRX1) (small2023newnoncodingbase pages 1-2, small2016northcarolinamacular pages 1-2, bakall2021choroidalneovascularizationin pages 5-5)
- **Gene OMIM identifiers present in evidence:**
  - **PRDM13 (OMIM 616741)**; **IRX1 (OMIM 606197)**; **CCNC (OMIM 123838)**; **DHS OMIM 616842** referenced for the regulatory site (wu2022anoveltandem pages 1-3)

**Not retrieved in the tool-accessible full-text set:** MONDO ID, Orphanet ID, MeSH term, ICD-10/ICD-11 code. These identifiers likely exist in curated databases, but were not present in the retrieved primary/review texts and therefore cannot be stated with tool-derived evidence here. (wu2022anoveltandem pages 1-3, sompele2022multiomicsprofilingin pages 25-27)

### 1.3 Synonyms / alternative names
- North Carolina macular dystrophy (NCMD) (small2023newnoncodingbase pages 1-2)
- Macular developmental disorder / congenital macular malformation / macular hypoplasia/dysplasia framing (expert commentary emphasizing congenital dysplasia rather than “atrophy”) (small2023commentson“the pages 1-2)
- Locus-based nomenclature: **MCDR1**, **MCDR3** (small2023commentson“the pages 1-2, sompele2022multiomicsprofilingin pages 25-27)

### 1.4 Evidence provenance
Evidence in this report is derived from peer-reviewed primary studies (human family genetics; functional assays; case reports), a 2023 clinical electrophysiology review, and preprint computational analysis; it is not derived from EHR aggregation. (small2016northcarolinamacular pages 1-2, sompele2022multiomicsapproachdissects pages 13-14, chiang2023electrophysiologicalevaluationof pages 11-12)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause: inherited noncoding regulatory variation** that dysregulates key retinal developmental transcription factors.
- The 2022 AJHG multi-omics study summarizes the causal architecture: NCMD is caused by “non-coding single-nucleotide variants (SNVs) in two hotspot regions near PRDM13 and by duplications overlapping DNase I hypersensitive sites near PRDM13 or IRX1,” framing NCMD as a “retinal enhanceropathy.” (sompele2022multiomicsapproachdissects pages 1-3)
- A 2023 family study reinforces that the phenotype is consistent with a regulatory “mutational hotspot” upstream of PRDM13. (small2023newnoncodingbase pages 1-2)

**Inheritance pattern:** autosomal dominant (small2023newnoncodingbase pages 1-2, wu2022anoveltandem pages 1-3)

### 2.2 Risk factors
- **Genetic risk factors (causal):** Heterozygous noncoding SNVs in PRDM13 regulatory regions and heterozygous tandem duplications at PRDM13 (MCDR1) or IRX1-region cCREs (MCDR3) (sompele2022multiomicsapproachdissects pages 13-14, small2016northcarolinamacular pages 1-2)
- **Environmental/lifestyle risk factors:** No evidence in retrieved sources supports environmental, infectious, or lifestyle risk modifiers for NCMD; it is consistently treated as a congenital Mendelian retinal developmental disorder. (green2021northcarolinamacular pages 1-6, small2023newnoncodingbase pages 1-2)

### 2.3 Protective factors / GxE
No protective alleles or gene–environment interaction evidence was identified in the retrieved texts. (sompele2022multiomicsapproachdissects pages 1-3)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core phenotypic concept and grading
A 2023 clinical genetics report describes a **three-grade** spectrum and explicitly states approximate frequency distribution: “approximately one-third of affected individuals in each clinical grade.” (small2023newnoncodingbase pages 1-2)
- **Grade 1:** few central drusen / central drusen-like deposits (small2023newnoncodingbase pages 1-2)
- **Grade 2:** confluent drusen ± subretinal fibrosis (small2023newnoncodingbase pages 1-2)
- **Grade 3:** choroidal coloboma-like excavation/large central atrophic excavation with absent RPE/choroidal lacunae and surrounding fibrosis (small2023newnoncodingbase pages 1-2)

### 3.2 Key signs/symptoms and characteristics (with candidate HPO terms)
Below, phenotype types are indicated and mapped to suggested **HPO** terms (ontology suggestions are not claims of curated mapping).

1) **Macular developmental lesions / drusen-like deposits** (clinical sign)
- Evidence: range from “central yellowish-white drusen-like deposits” to confluent drusen-like lesions (small2023newnoncodingbase pages 1-2, wu2022anoveltandem pages 1-3)
- Suggested HPO: **Macular dystrophy (HP:0000556)**; **Drusen (HP:0001132)**; **Macular coloboma / coloboma-like macular lesion** (candidate: **Coloboma (HP:0000589)** with localization qualifier)

2) **Macular excavation / chorioretinal atrophy-like appearance** (clinical sign)
- Grade 3 described as coloboma-like excavation with absent RPE/choroidal lacunae (small2023newnoncodingbase pages 1-2)
- Suggested HPO: **Chorioretinal atrophy (HP:0001130)**; **Abnormality of the macula (HP:0001103)**

3) **Reduced central vision / variable visual acuity** (symptom/function)
- Quantitative evidence: visual acuity range reported as **0.0–1.6 LogMAR** in one cohort (green2021northcarolinamacular pages 1-6)
- Suggested HPO: **Decreased visual acuity (HP:0007663)**; **Central scotoma (HP:0000603)** (central scotomata documented in one child) (audere2016geneticlinkagestudies pages 4-6)

4) **Peripheral retinal spots/drusen-like changes** (clinical sign)
- “Peripheral retinal spots were seen in all study subjects on widefield imaging.” (green2021northcarolinamacular pages 1-6)
- Suggested HPO: **Peripheral retinal degeneration (HP:0001133)** (approximate); **Retinal deposits** (candidate)

5) **Choroidal neovascularization (CNV/CNVM)** (complication)
- CNV can occur in childhood: “a 6-year-old patient developed choroidal neovascularization and required treatment with intravitreal bevacizumab injections.” (green2021northcarolinamacular pages 1-6)
- Suggested HPO: **Choroidal neovascularization (HP:0000559)**; **Subretinal fibrosis (HP:0007897)**

### 3.3 Quality of life impact
Direct QoL instruments (EQ-5D/SF-36) were not reported in the retrieved texts. Functional impact is inferred via central vision impairment and scotoma when present. (audere2016geneticlinkagestudies pages 4-6, green2021northcarolinamacular pages 1-6)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and loci
- **PRDM13 dysregulation (MCDR1, chr6):** foundational evidence: “North Carolina macular dystrophy is caused by dysregulation of the retinal transcription factor PRDM13.” (Ophthalmology 2016; publication date **2016-01**) (small2016northcarolinamacular pages 4-5)
- **IRX1 dysregulation (MCDR3, chr5):** disease-associated duplications include a 900 kb duplication including IRX1 (small2016northcarolinamacular pages 4-5)

### 4.2 Pathogenic variant classes and examples
**Noncoding SNVs (regulatory/DHS) upstream of PRDM13**
- Example coordinates cited in cohorts/analyses include **chr6:100,040,906G>T**, **chr6:100,040,974A>C**, **chr6:100,040,987G>C**, **chr6:100,041,040C>T**, **chr6:100,046,783A>C** (hg19/GRCh37 as specified in the original sources) (green2021northcarolinamacular pages 28-31)
- 2023 report notes a new base-pair mutation at the identical locus as the original, supporting a hotspot. (small2023newnoncodingbase pages 1-2)

**Tandem duplications (structural variants)**
- 2016 Ophthalmology describes duplications including a **123 kb tandem duplication containing PRDM13** and a **900 kb tandem duplication including IRX1** (small2016northcarolinamacular pages 4-5)
- 2022 Chinese family reports a **134.6 kb tandem duplication** with explicit coordinate interval: **g.99932464-100067110dup** (chr6) encompassing **CCNC, PRDM13, and a DHS** (publication date **2022-08**) (wu2022anoveltandem pages 1-3)

**Functional directionality (cis-regulatory output) — multi-omics 2022 AJHG**
Luciferase assays (in vitro) systematically showed allele-dependent effects:
- Hotspot-1 variants increased reporter expression **1.6–3.2-fold** (p<0.001), while hotspot-2 variants decreased expression to **~0.6–0.7-fold** (p<0.001). (sompele2022multiomicsapproachdissects pages 13-14)
- Tandem duplication constructs produced **~0.5-fold decreased** luciferase activity relative to single-copy constructs. (sompele2022multiomicsapproachdissects pages 13-14)

### 4.3 Modifier genes, epigenetics, chromosomal abnormalities
No modifier genes or disease-specific epigenetic signatures were identified in the retrieved evidence. Structural variants are tandem duplications rather than aneuploidy/translocations. (sompele2022multiomicsapproachdissects pages 13-14, wu2022anoveltandem pages 1-3)

---

## 5. Environmental information
No environmental, lifestyle, or infectious contributors were identified in the retrieved literature; NCMD is presented as a congenital genetic developmental malformation. (green2021northcarolinamacular pages 1-6, small2023newnoncodingbase pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic model: retinal enhanceropathy → transcription-factor dysregulation → macular maldevelopment
The strongest mechanistic synthesis is from the 2022 AJHG multi-omics study:
- **Upstream event:** noncoding SNVs in mutational hotspots and duplications spanning candidate cis-regulatory elements (cCREs) near PRDM13 and IRX1 alter enhancer activity and/or gene regulatory landscape. (sompele2022multiomicsapproachdissects pages 1-3, sompele2022multiomicsapproachdissects pages 13-14)
- **Regulatory wiring:** UMI-4C (adult human retina) plus integrated retina epigenomics nominated **18 cCREs**, and functional assays (luciferase; Xenopus enhancer assays) showed disease-associated variants change enhancer output. (sompele2022multiomicsapproachdissects pages 1-3)
- **Developmental timing/cell types:** single-nucleus RNA-seq indicates PRDM13 is predominantly expressed in **amacrine cells** (and some retinal progenitors/horizontal/ganglion cells) and IRX1 peaks in **retinal ganglion cells**, with developmental peaks around embryonic timepoints (e.g., e70). This supports the hypothesis that altered PRDM13/IRX1 expression impairs “amacrine–ganglion cell” interactions during retinogenesis. (sompele2022multiomicsapproachdissects pages 13-14, sompele2022multiomicsapproachdissects pages 1-3)

**Suggested ontology mappings (mechanism; non-exhaustive):**
- GO Biological Process: **retina development**; **neurogenesis**; **amacrine cell differentiation**; **synapse organization**
- Cell Ontology (CL) candidates: **amacrine cell**, **retinal ganglion cell**, **retinal progenitor cell** (supported by expression localization and developmental claims) (sompele2022multiomicsapproachdissects pages 13-14)

### 6.2 Model organism support (functional developmental biology)
A Xenopus study provides developmental mechanism support for PRDM13 function:
- prdm13 is expressed in retinal progenitors and **~40% of amacrine cells**, predominantly glycinergic; knockdown “prevents glycinergic cell genesis,” while overexpression biases toward amacrine fate with glycinergic preference. (publication date **2017-09**) (bessodes2017prdm13formsa pages 1-2, bessodes2017prdm13formsa pages 10-13)
These developmental roles align with the AJHG study’s cell-type timing (amacrine emergence and synapsing with ganglion cells) and support a plausible causal chain from regulatory dysregulation to disrupted macular/central retinal wiring. (sompele2022multiomicsapproachdissects pages 1-3, sompele2022multiomicsapproachdissects pages 13-14)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
- Primary: **Eye**, specifically **retina** and **macula/foveal region** (central retina). (green2021northcarolinamacular pages 1-6, small2023newnoncodingbase pages 1-2)

**Suggested UBERON terms (candidates):**
- **retina**, **macula lutea**, **fovea centralis**, **retinal pigment epithelium (RPE)**

### 7.2 Cell level
- RPE involvement is suggested by grade 3 descriptions (“absence of RPE”) and abnormal EOG ratios consistent with RPE dysfunction in some cases. (small2023newnoncodingbase pages 1-2, chiang2023electrophysiologicalevaluationof pages 11-12)
- Inner retinal neuron involvement is suggested by PRDM13/IRX1 developmental expression in amacrine and ganglion cells and mechanistic hypotheses about synaptic interactions. (sompele2022multiomicsapproachdissects pages 13-14)

---

## 8. Temporal development (natural history)

### 8.1 Onset
- Lesions are “congenital or present in early infancy” (wu2022anoveltandem pages 1-3), and are “present at birth” (green2021northcarolinamacular pages 1-6).

### 8.2 Progression
- NCMD is generally described as nonprogressive: “present at birth and rarely progresses” (green2021northcarolinamacular pages 1-6).
- A 2023 report asserts grade is fixed: affected individuals have “a fixed grade at birth and do not progress between grades.” (small2023newnoncodingbase pages 1-2)

### 8.3 Critical complications over time
- CNV can occur early (childhood) and can drive acute functional loss; multiple independent case-based sources describe CNV and treatment response. (green2021northcarolinamacular pages 1-6, bakall2021choroidalneovascularizationin pages 2-5)

---

## 9. Inheritance and population

### 9.1 Epidemiology (available statistics)
Formal prevalence/incidence rates were not identified in the retrieved texts.

However, several quantitative or semi-quantitative epidemiology statements are available:
- “NCMD is rare but reported worldwide in >50 families.” (small2023newnoncodingbase pages 1-2)
- “More than 2000 patients have been diagnosed worldwide.” (wu2022anoveltandem pages 1-3)
- Historical founder kindred: original pedigree described as **>500 individuals across seven generations** (green2021northcarolinamacular pages 1-6), and a “very large kindred (~2000 individuals)” is referenced in linkage-era literature (audere2016geneticlinkagestudies pages 1-2).

### 9.2 Inheritance, penetrance, expressivity
- Autosomal dominant inheritance is repeatedly stated. (small2023newnoncodingbase pages 1-2, wu2022anoveltandem pages 1-3)
- Complete/fully penetrant is reported in several sources (small2023newnoncodingbase pages 1-2, green2021northcarolinamacular pages 1-6).
- Marked intrafamilial variability / variable expressivity is consistent across cohorts. (small2023newnoncodingbase pages 1-2, green2021northcarolinamacular pages 1-6)

### 9.3 Founder effects / geographic distribution
- Founder effect is described for the original North Carolina pedigree, descended from two Irish brothers who emigrated in the 19th century. (green2021northcarolinamacular pages 1-6, audere2016geneticlinkagestudies pages 1-2)
- Multiple sources emphasize the “North Carolina” name is a misnomer due to global distribution (United States, Europe, Central America, Australia/New Zealand, Korea, China). (small2023newnoncodingbase pages 1-2, small2023commentson“the pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical/imaging tests (real-world implementation)
Multimodal ophthalmic evaluation is emphasized, including:
- **Fundus examination/photography** for drusen-like deposits, confluent changes, or excavation (wu2022anoveltandem pages 1-3)
- **OCT**: in mild grade 1 lesions can show RPE-level deposits with preserved ellipsoid zone; severe lesions can show “central intrachoroidal fluid-containing space with preserved retinal layers,” and CNV/subretinal fibrosis may be visible in advanced disease. (chiang2023electrophysiologicalevaluationof pages 11-12)
- **Widefield imaging**: peripheral spots “seen in all study subjects” can support recognition. (green2021northcarolinamacular pages 1-6)

### 10.2 Electrophysiology (ERG/EOG/mfERG)
The 2023 electrophysiology review provides test interpretation patterns:
- **Full-field ERG often normal** in NCMD (suggesting absence of generalized photoreceptor dysfunction). (chiang2023electrophysiologicalevaluationof pages 11-12)
- **mfERG abnormal** (delayed implicit times and reduced amplitudes localized to central lesion), helping detect macular dysfunction when ffERG is normal. (chiang2023electrophysiologicalevaluationof pages 11-12, chiang2023electrophysiologicalevaluationof pages 12-14)
- **EOG abnormal** with reduced LP:DT (Arden) ratios reported **1.4–1.6**, consistent with RPE dysfunction. (chiang2023electrophysiologicalevaluationof pages 11-12)

### 10.3 Genetic testing strategy
Evidence-supported approaches include:
- **Whole genome sequencing (WGS)** and targeted confirmation (Sanger) for noncoding SNVs and breakpoint characterization; CNV analysis for tandem duplications. (small2023newnoncodingbase pages 1-2)
- Long-read or genome sequencing can validate tandem duplications (reported in the Chinese family study). (wu2022anoveltandem pages 1-3)

### 10.4 Differential diagnosis (high-level)
- Mild NCMD can be misdiagnosed as early-onset macular drusen (asymptomatic cases identified in adulthood) (green2021northcarolinamacular pages 13-16).
- Electrophysiology (normal ffERG with abnormal mfERG; abnormal EOG) is used across macular dystrophy differentials and can help localize macular vs generalized retinal disease and indicate RPE involvement. (chiang2023electrophysiologicalevaluationof pages 7-9, chiang2023electrophysiologicalevaluationof pages 11-12)

---

## 11. Outcome / prognosis

### 11.1 Visual prognosis
- Vision can remain “relatively good” despite striking lesions; multiple sources report unexpectedly preserved acuity in some individuals (e.g., 20/20–20/50 in a Chinese pedigree). (wu2022anoveltandem pages 1-3)
- Conversely, severe grade 3 is associated with severe central vision loss, and CNV/subretinal fibrosis can worsen outcomes. (chiang2023electrophysiologicalevaluationof pages 11-12)

### 11.2 Prognostic factors
- **Disease grade** and **presence of CNV/CNVM** appear to be key drivers of visual outcome; CNVM is highlighted as a cause of vision decline and as treatable. (small2023newnoncodingbase pages 1-2, bakall2021choroidalneovascularizationin pages 2-5)

Mortality/survival outcomes are not applicable (ocular-limited disorder) and not reported in retrieved evidence.

---

## 12. Treatment

### 12.1 Pharmacotherapy / advanced therapeutics
No disease-modifying pharmacotherapy or gene therapy was identified for NCMD in the retrieved evidence. Current care is primarily monitoring and treating complications.

### 12.2 Treatment of CNV (evidence of real-world implementation)
- **Bevacizumab (anti-VEGF) intravitreal injection**: case-based evidence indicates improved fluid and vision with intravitreal **1.25 mg bevacizumab** in a pediatric case, with reduced cystic fluid after three monthly injections and stopping after stability. (Bakall et al., 2021-09; URL https://doi.org/10.1097/icb.0000000000000838) (bakall2021choroidalneovascularizationin pages 2-5)
- **Ranibizumab (anti-VEGF) intravitreal injection**: a familial maculopathy resembling NCMD reported type 2 CNV responsive to **three monthly ranibizumab** injections with “significant improvement” and no later CNV activity. (Nekolova et al., 2022-12; URL https://doi.org/10.5507/bp.2021.037) (nekolova2022moderndiagnosticand pages 2-6)

**Suggested MAXO terms (candidates):**
- **intravitreal injection**; **anti-VEGF therapy**; **optical coherence tomography** (diagnostic procedure); **low vision rehabilitation** (not explicitly described in retrieved texts, but relevant as supportive care)

### 12.3 Clinical trials
A tool-based clinicaltrials.gov search retrieved trials metadata but no specific, NCMD-targeted interventional clinical trials were identified in the retrieved evidence set.

---

## 13. Prevention
No primary prevention is described for NCMD (genetic congenital disorder). Secondary prevention is essentially **cascade screening and early ophthalmic monitoring** in affected families to detect CNV early and treat promptly. (small2023newnoncodingbase pages 1-2, green2021northcarolinamacular pages 13-16)

---

## 14. Other species / natural disease
No naturally occurring NCMD-equivalent disease in companion animals was identified in the retrieved evidence.

---

## 15. Model organisms

### 15.1 Key model systems and relevance
- **Xenopus retina (developmental model):** prdm13 gain/loss-of-function experiments demonstrate a causal role in amacrine subtype specification, with knockdown preventing glycinergic amacrine cell genesis and overexpression increasing amacrine fate. This supports developmental plausibility for PRDM13 dysregulation in NCMD. (bessodes2017prdm13formsa pages 1-2, bessodes2017prdm13formsa pages 10-13)
- **Mechanism-focused enhancer assays (in vivo):** AJHG 2022 reports Xenopus enhancer assays validating in vivo activity of an NCMD-associated cCRE that contacts the PRDM13 promoter and is active when central retinal progenitors exit mitosis. (sompele2022multiomicsapproachdissects pages 1-3)

### 15.2 Limitations
Non-human models do not possess a human-like macula, so they primarily model **retinal developmental circuitry and cis-regulatory logic**, not macula anatomy per se. The macula-predominant phenotype therefore requires careful cross-species interpretation and may be best modeled with human retinal organoids and human multi-omics integration (explicitly proposed as a future direction). (sompele2022multiomicsprofilingin pages 25-27)

---

## Key schematics (visual evidence)
Genetic schematics of the original variant set (V1–V5) and their locus contexts are shown in the cropped figures retrieved from Small et al. (Ophthalmology, 2016-01). These illustrate the PRDM13-region regulatory SNVs/duplication (V1–V4) and the IRX1-region duplication (V5). (small2016northcarolinamacular media 3981bb1f, small2016northcarolinamacular media deebfcdf)

---

## Curated summary table
The following evidence-grounded table consolidates identifiers, loci/genes, variant examples, inheritance, and hallmark phenotypes/complications.

| Item type | Detail | Evidence/Notes |
|---|---|---|
| Disease identifier | North Carolina macular dystrophy (NCMD); OMIM/MIM #136550 | Reported explicitly as “NCMD [MIM: 136550]” / “NCMD/MCDR1; OMIM #136550” in evidence; rare congenital macular disorder (small2023newnoncodingbase pages 1-2, sompele2022multiomicsprofilingin pages 25-27) |
| Locus name | MCDR1 | Chromosome 6 locus upstream of PRDM13; commonly used alternative locus-based identifier for NCMD (small2023newnoncodingbase pages 1-2, small2016northcarolinamacular pages 1-2, wu2022anoveltandem pages 1-3, sompele2022multiomicsprofilingin pages 25-27) |
| Locus name | MCDR3 | Chromosome 5 locus involving/downstream of IRX1; additional NCMD locus (small2023newnoncodingbase pages 1-2, small2016northcarolinamacular pages 1-2, wu2022anoveltandem pages 1-3, bakall2021choroidalneovascularizationin pages 5-5, sompele2022multiomicsprofilingin pages 25-27) |
| Gene | PRDM13 | Main disease-implicated transcription factor at MCDR1; NCMD is described as caused by dysregulation of PRDM13 rather than coding loss-of-function alone (small2016northcarolinamacular pages 4-5, small2016northcarolinamacular pages 1-2, sompele2022multiomicsapproachdissects pages 1-3) |
| Gene | IRX1 | Implicated at MCDR3 through downstream duplications or duplication including IRX1; proposed dysregulation mechanism (small2016northcarolinamacular pages 1-2, bakall2021choroidalneovascularizationin pages 5-5, sompele2022multiomicsapproachdissects pages 1-3) |
| Gene context | CCNC | Present in the MCDR1 region context; a novel chr6 tandem duplication encompassed CCNC, PRDM13, and a DNase I hypersensitive site. CCNC OMIM 123838 given in evidence, but causal role is less established than PRDM13 dysregulation (wu2022anoveltandem pages 1-3) |
| Inheritance | Autosomal dominant | Consistently described as autosomal dominant in multiple studies/reviews (small2023newnoncodingbase pages 1-2, wu2022anoveltandem pages 1-3, green2021northcarolinamacular pages 1-6) |
| Penetrance | Fully penetrant | Explicitly stated in 2023 evidence: “autosomal dominant, fully penetrant, congenital” with marked intrafamilial variability (small2023newnoncodingbase pages 1-2) |
| Expressivity | Marked intra- and interfamilial variability | Visual acuity and lesion severity vary widely despite shared familial variants; variable expressivity repeatedly emphasized (small2023newnoncodingbase pages 1-2, green2021northcarolinamacular pages 1-6) |
| Variant type | Noncoding SNV upstream of PRDM13: chr6:100,040,906G>T (hg19) | Original NCMD-associated regulatory variant in DNase hypersensitivity site upstream of PRDM13 (bakall2021choroidalneovascularizationin pages 5-5, green2021northcarolinamacular pages 28-31) |
| Variant type | Noncoding SNV upstream of PRDM13: chr6:100,040,974A>C (hg19) | Reported disease-associated variant within PRDM13 regulatory enhancer region (green2021northcarolinamacular pages 28-31) |
| Variant type | Noncoding SNV upstream of PRDM13: chr6:100,040,987G>C (hg19/GRCh37) | Detected in all affected members of one cohort/families; predicted to lie in enhancer interacting with PRDM13 (green2021northcarolinamacular pages 1-6, green2021northcarolinamacular pages 28-31) |
| Variant type | Noncoding SNV upstream of PRDM13: chr6:100,041,040C>T (hg19) | Additional NCMD-associated variant in same regulatory region (green2021northcarolinamacular pages 28-31) |
| Variant type | Noncoding SNV near PRDM13 enhancer: chr6:100,046,783A>C (hg19) | Candidate enhancer variant predicted functional in macular/retinal tissue (green2021northcarolinamacular pages 28-31) |
| Variant type | 123-kb tandem duplication containing PRDM13 | Structural variant reported at MCDR1 in a family; supports dosage/regulatory mechanism (small2016northcarolinamacular pages 4-5, bakall2021choroidalneovascularizationin pages 5-5) |
| Variant type | 134.6-kb tandem duplication at chr6 g.99932464-100067110dup | Novel duplication in a Chinese family; encompasses CCNC, PRDM13, and a DNase I hypersensitive site in MCDR1 (wu2022anoveltandem pages 1-3) |
| Variant type | 900-kb tandem duplication including entire IRX1 gene (V5) | Reported at MCDR3 locus on chromosome 5; segregated with disease (small2016northcarolinamacular pages 4-5, small2016northcarolinamacular pages 1-2) |
| Variant mechanism | Retinal enhanceropathy / cis-regulatory dysregulation | Pathogenic SNVs cluster in PRDM13 mutational hotspots/cCREs; duplications may duplicate one or more CREs or disturb gene regulatory landscape affecting PRDM13 or IRX1 expression (sompele2022multiomicsapproachdissects pages 13-14, sompele2022multiomicsapproachdissects pages 1-3, sompele2022multiomicsprofilingin pages 25-27) |
| Clinical phenotype | Congenital, usually nonprogressive macular developmental disorder | Present at birth; typically little progression, though phenotype severity is variable (small2023newnoncodingbase pages 1-2, wu2022anoveltandem pages 1-3, green2021northcarolinamacular pages 1-6) |
| Clinical phenotype | Grade 1 lesion | Central yellowish-white/drusen-like deposits; early OCT may show RPE-level deposits with intact ellipsoid zone (wu2022anoveltandem pages 1-3, chiang2023electrophysiologicalevaluationof pages 11-12) |
| Clinical phenotype | Grade 2 lesion | Larger confluent drusen-like/confluent macular changes, sometimes with subretinal fibrosis (small2023newnoncodingbase pages 1-2, wu2022anoveltandem pages 1-3) |
| Clinical phenotype | Grade 3 lesion | Large central atrophic excavation / choroidal coloboma-like lesion with absent RPE/choroidal lacunae in severe disease descriptions (small2023newnoncodingbase pages 1-2, wu2022anoveltandem pages 1-3) |
| Clinical phenotype | Peripheral retinal spots | Widefield imaging can reveal peripheral radial yellow-white/drusen-like spots; useful clinical clue (green2021northcarolinamacular pages 1-6, green2021northcarolinamacular pages 28-31) |
| Visual function | Visual acuity highly variable | Reported range 0.0 to 1.6 LogMAR in one series; acuity can remain relatively preserved despite large lesions (green2021northcarolinamacular pages 1-6, wu2022anoveltandem pages 1-3) |
| Complication | Choroidal neovascularization (CNV/CNVM) | Can occur in childhood/early life; one 6-year-old required treatment; advanced disease may show CNV and subretinal fibrosis (green2021northcarolinamacular pages 1-6, bakall2021choroidalneovascularizationin pages 5-5, chiang2023electrophysiologicalevaluationof pages 11-12) |
| Management note | Anti-VEGF response for CNV | Intravitreal bevacizumab reported beneficial / vision-improving in NCMD-associated CNV (green2021northcarolinamacular pages 1-6, bakall2021choroidalneovascularizationin pages 5-5) |


*Table: This table summarizes evidence-supported identifiers, loci, causal genes, variant classes, inheritance, and hallmark clinical features of North Carolina macular dystrophy. It is designed as a compact reference for disease knowledge base curation using only facts present in the retrieved evidence snippets.*

---

## Recent developments (emphasis 2023–2024)
1) **Expanded mutational spectrum and hotspot concept (2023):** identification of an additional noncoding base change at the same regulatory locus as the original MCDR1 family supports a mutational hotspot model and reiterates “autosomal dominant, fully penetrant, congenital, nonprogressive” disease framing. (Small et al., 2023-01; URL https://doi.org/10.1177/24741264221129432) (small2023newnoncodingbase pages 1-2)

2) **Expert clarification of developmental terminology (2023):** commentary emphasizes NCMD is better described as congenital macular hypoplasia/dysplasia, cautioning against misleading descriptors such as “atrophy” and reinforcing locus nomenclature (MCDR1/MCDR3). (Small, 2023-09; URL https://doi.org/10.1186/s12886-023-03100-2) (small2023commentson“the pages 1-2)

3) **Clinical electrophysiology integration (2023):** contemporary review consolidates the typical pattern (normal ffERG, abnormal mfERG, abnormal EOG with LP:DT ~1.4–1.6) and highlights how electrophysiology localizes dysfunction and supports differential diagnosis among macular dystrophies. (Chiang & Yu, 2023-02; URL https://doi.org/10.3390/jcm12041430) (chiang2023electrophysiologicalevaluationof pages 11-12)

---

## References (tool-retrieved; URLs and publication dates)
- Small KW et al. *Ophthalmology*. 2016-01. https://doi.org/10.1016/j.ophtha.2015.10.006 (small2016northcarolinamacular pages 1-2)
- Van de Sompele S et al. *Am J Hum Genet*. 2022-11. https://doi.org/10.1016/j.ajhg.2022.09.013 (sompele2022multiomicsapproachdissects pages 1-3)
- Small KW et al. *J VitreoRetinal Dis*. 2023-01. https://doi.org/10.1177/24741264221129432 (small2023newnoncodingbase pages 1-2)
- Chiang T-K, Yu M. *J Clin Med*. 2023-02. https://doi.org/10.3390/jcm12041430 (chiang2023electrophysiologicalevaluationof pages 11-12)
- Wu S et al. *Graefes Arch Clin Exp Ophthalmol*. 2022-08. https://doi.org/10.1007/s00417-021-05376-w (wu2022anoveltandem pages 1-3)
- Bakall B et al. *Retinal Cases & Brief Reports*. 2021-09. https://doi.org/10.1097/icb.0000000000000838 (bakall2021choroidalneovascularizationin pages 2-5)
- Nekolova J et al. *Biomedical Papers*. 2022-12. https://doi.org/10.5507/bp.2021.037 (nekolova2022moderndiagnosticand pages 2-6)
- Bessodes N et al. *Neural Development*. 2017-09. https://doi.org/10.1186/s13064-017-0093-2 (bessodes2017prdm13formsa pages 1-2)

---

## Notable evidence gaps (from tool-retrieved corpus)
- MONDO/Orphanet/MeSH/ICD identifiers were not present in retrieved documents.
- No robust population prevalence/incidence estimates were found.
- No NCMD-specific interventional clinical trials or disease-modifying therapies were identified.
- QoL instrument data were not found.


References

1. (small2023newnoncodingbase pages 1-2): Kent W. Small, Stijn Van de Sompele, Jessica Avetisjan, Nitin Udar, Steven Agemy, Elfride De Baere, and Fadi S. Shaya. New noncoding base pair mutation at the identical locus as the original ncmd/mcdr1 in a mexican family, suggesting a mutational hotspot. Journal of VitreoRetinal Diseases, 7:33-42, Jan 2023. URL: https://doi.org/10.1177/24741264221129432, doi:10.1177/24741264221129432. This article has 3 citations.

2. (sompele2022multiomicsapproachdissects pages 1-3): Stijn Van de Sompele, Kent W. Small, Munevver Burcu Cicekdal, Víctor López Soriano, Eva D’haene, Fadi S. Shaya, Steven Agemy, Thijs Van der Snickt, Alfredo Dueñas Rey, Toon Rosseel, Mattias Van Heetvelde, Sarah Vergult, Irina Balikova, Arthur A. Bergen, Camiel J.F. Boon, Julie De Zaeytijd, Chris F. Inglehearn, Bohdan Kousal, Bart P. Leroy, Carlo Rivolta, Veronika Vaclavik, Jenneke van den Ende, Mary J. van Schooneveld, José Luis Gómez-Skarmeta, Juan J. Tena, Juan R. Martinez-Morales, Petra Liskova, Kris Vleminckx, and Elfride De Baere. Multi-omics approach dissects cis-regulatory mechanisms underlying north carolina macular dystrophy, a retinal enhanceropathy. The American Journal of Human Genetics, 109:2029-2048, Nov 2022. URL: https://doi.org/10.1016/j.ajhg.2022.09.013, doi:10.1016/j.ajhg.2022.09.013. This article has 27 citations.

3. (green2021northcarolinamacular pages 1-6): David J. Green, Eva Lenassi, Cerys S. Manning, David McGaughey, Vinod Sharma, Graeme C. Black, Jamie M. Ellingford, and Panagiotis I. Sergouniotis. North carolina macular dystrophy: phenotypic variability and computational analysis of disease-implicated non-coding variants. MedRxiv, Mar 2021. URL: https://doi.org/10.1101/2021.03.05.21252975, doi:10.1101/2021.03.05.21252975. This article has 3 citations.

4. (sompele2022multiomicsprofilingin pages 25-27): Stijn Van de Sompele, Kent W. Small, Munevver Burcu Cicekdal, Víctor López Soriano, Eva D’haene, Fadi S. Shaya, Steven Agemy, Thijs Van der Snickt, Alfredo Dueñas Rey, Toon Rosseel, Mattias Van Heetvelde, Sarah Vergult, Irina Balikova, Arthur A. Bergen, Camiel J. F. Boon, Julie De Zaeytijd, Chris F. Inglehearn, Bohdan Kousal, Bart P. Leroy, Carlo Rivolta, Veronika Vaclavik, Jenneke van den Ende, Mary J. van Schooneveld, José Luis Gómez-Skarmeta, Juan J. Tena, Juan R. Martinez-Morales, Petra Liskova, Kris Vleminckx, and Elfride De Baere. Multi-omics profiling, in vitro and in vivo enhancer assays dissect the cis-regulatory mechanisms underlying north carolina macular dystrophy, a retinal enhanceropathy. bioRxiv, Jul 2022. URL: https://doi.org/10.1101/2022.03.08.481329, doi:10.1101/2022.03.08.481329. This article has 2 citations.

5. (small2016northcarolinamacular pages 1-2): Kent W. Small, Adam P. DeLuca, S. Scott Whitmore, Thomas Rosenberg, Rosemary Silva-Garcia, Nitin Udar, Bernard Puech, Charles A. Garcia, Thomas A. Rice, Gerald A. Fishman, Elise Héon, James C. Folk, Luan M. Streb, Christine M. Haas, Luke A. Wiley, Todd E. Scheetz, John H. Fingert, Robert F. Mullins, Budd A. Tucker, and Edwin M. Stone. North carolina macular dystrophy is caused by dysregulation of the retinal transcription factor prdm13. Ophthalmology, 123 1:9-18, Jan 2016. URL: https://doi.org/10.1016/j.ophtha.2015.10.006, doi:10.1016/j.ophtha.2015.10.006. This article has 143 citations and is from a highest quality peer-reviewed journal.

6. (wu2022anoveltandem pages 1-3): Shijing Wu, Zhisheng Yuan, Zixi Sun, Tian Zhu, Xing Wei, Xuan Zou, and Ruifang Sui. A novel tandem duplication of prdm13 in a chinese family with north carolina macular dystrophy. Graefe's Archive for Clinical and Experimental Ophthalmology, 260:645-653, Aug 2022. URL: https://doi.org/10.1007/s00417-021-05376-w, doi:10.1007/s00417-021-05376-w. This article has 11 citations.

7. (bakall2021choroidalneovascularizationin pages 5-5): MD Benjamin Bakall, †. J. Shepard, MD Bryan III, MD Edwin M. Stone, and MD Kent W. Small. Choroidal neovascularization in north carolina macular dystrophy responsive to anti–vascular endothelial growth factor therapy. RETINAL Cases &amp; Brief Reports, 15:509-513, Sep 2021. URL: https://doi.org/10.1097/icb.0000000000000838, doi:10.1097/icb.0000000000000838. This article has 19 citations and is from a peer-reviewed journal.

8. (small2023commentson“the pages 1-2): Kent W. Small. Comments on “the possible pathogenesis of macular caldera in patients with north carolina macular dystrophy”. BMC Ophthalmology, Sep 2023. URL: https://doi.org/10.1186/s12886-023-03100-2, doi:10.1186/s12886-023-03100-2. This article has 0 citations and is from a peer-reviewed journal.

9. (sompele2022multiomicsapproachdissects pages 13-14): Stijn Van de Sompele, Kent W. Small, Munevver Burcu Cicekdal, Víctor López Soriano, Eva D’haene, Fadi S. Shaya, Steven Agemy, Thijs Van der Snickt, Alfredo Dueñas Rey, Toon Rosseel, Mattias Van Heetvelde, Sarah Vergult, Irina Balikova, Arthur A. Bergen, Camiel J.F. Boon, Julie De Zaeytijd, Chris F. Inglehearn, Bohdan Kousal, Bart P. Leroy, Carlo Rivolta, Veronika Vaclavik, Jenneke van den Ende, Mary J. van Schooneveld, José Luis Gómez-Skarmeta, Juan J. Tena, Juan R. Martinez-Morales, Petra Liskova, Kris Vleminckx, and Elfride De Baere. Multi-omics approach dissects cis-regulatory mechanisms underlying north carolina macular dystrophy, a retinal enhanceropathy. The American Journal of Human Genetics, 109:2029-2048, Nov 2022. URL: https://doi.org/10.1016/j.ajhg.2022.09.013, doi:10.1016/j.ajhg.2022.09.013. This article has 27 citations.

10. (chiang2023electrophysiologicalevaluationof pages 11-12): Tsun-Kang Chiang and Minzhong Yu. Electrophysiological evaluation of macular dystrophies. Journal of Clinical Medicine, 12:1430, Feb 2023. URL: https://doi.org/10.3390/jcm12041430, doi:10.3390/jcm12041430. This article has 7 citations.

11. (audere2016geneticlinkagestudies pages 4-6): Mareta Audere, Katrina Rutka, Inna Inaskina, Raitis Peculis, Svetlana Sepetiene, Sandra Valeina, and Baiba Lāce. Genetic linkage studies of a north carolina macular dystrophy family. Medicina, 52 3:180-6, Jan 2016. URL: https://doi.org/10.1016/j.medici.2016.04.001, doi:10.1016/j.medici.2016.04.001. This article has 10 citations.

12. (small2016northcarolinamacular pages 4-5): Kent W. Small, Adam P. DeLuca, S. Scott Whitmore, Thomas Rosenberg, Rosemary Silva-Garcia, Nitin Udar, Bernard Puech, Charles A. Garcia, Thomas A. Rice, Gerald A. Fishman, Elise Héon, James C. Folk, Luan M. Streb, Christine M. Haas, Luke A. Wiley, Todd E. Scheetz, John H. Fingert, Robert F. Mullins, Budd A. Tucker, and Edwin M. Stone. North carolina macular dystrophy is caused by dysregulation of the retinal transcription factor prdm13. Ophthalmology, 123 1:9-18, Jan 2016. URL: https://doi.org/10.1016/j.ophtha.2015.10.006, doi:10.1016/j.ophtha.2015.10.006. This article has 143 citations and is from a highest quality peer-reviewed journal.

13. (green2021northcarolinamacular pages 28-31): David J. Green, Eva Lenassi, Cerys S. Manning, David McGaughey, Vinod Sharma, Graeme C. Black, Jamie M. Ellingford, and Panagiotis I. Sergouniotis. North carolina macular dystrophy: phenotypic variability and computational analysis of disease-implicated non-coding variants. MedRxiv, Mar 2021. URL: https://doi.org/10.1101/2021.03.05.21252975, doi:10.1101/2021.03.05.21252975. This article has 3 citations.

14. (bessodes2017prdm13formsa pages 1-2): Nathalie Bessodes, Karine Parain, Odile Bronchain, Eric J. Bellefroid, and Muriel Perron. Prdm13 forms a feedback loop with ptf1a and is required for glycinergic amacrine cell genesis in the xenopus retina. Neural Development, Sep 2017. URL: https://doi.org/10.1186/s13064-017-0093-2, doi:10.1186/s13064-017-0093-2. This article has 26 citations and is from a peer-reviewed journal.

15. (bessodes2017prdm13formsa pages 10-13): Nathalie Bessodes, Karine Parain, Odile Bronchain, Eric J. Bellefroid, and Muriel Perron. Prdm13 forms a feedback loop with ptf1a and is required for glycinergic amacrine cell genesis in the xenopus retina. Neural Development, Sep 2017. URL: https://doi.org/10.1186/s13064-017-0093-2, doi:10.1186/s13064-017-0093-2. This article has 26 citations and is from a peer-reviewed journal.

16. (bakall2021choroidalneovascularizationin pages 2-5): MD Benjamin Bakall, †. J. Shepard, MD Bryan III, MD Edwin M. Stone, and MD Kent W. Small. Choroidal neovascularization in north carolina macular dystrophy responsive to anti–vascular endothelial growth factor therapy. RETINAL Cases &amp; Brief Reports, 15:509-513, Sep 2021. URL: https://doi.org/10.1097/icb.0000000000000838, doi:10.1097/icb.0000000000000838. This article has 19 citations and is from a peer-reviewed journal.

17. (audere2016geneticlinkagestudies pages 1-2): Mareta Audere, Katrina Rutka, Inna Inaskina, Raitis Peculis, Svetlana Sepetiene, Sandra Valeina, and Baiba Lāce. Genetic linkage studies of a north carolina macular dystrophy family. Medicina, 52 3:180-6, Jan 2016. URL: https://doi.org/10.1016/j.medici.2016.04.001, doi:10.1016/j.medici.2016.04.001. This article has 10 citations.

18. (chiang2023electrophysiologicalevaluationof pages 12-14): Tsun-Kang Chiang and Minzhong Yu. Electrophysiological evaluation of macular dystrophies. Journal of Clinical Medicine, 12:1430, Feb 2023. URL: https://doi.org/10.3390/jcm12041430, doi:10.3390/jcm12041430. This article has 7 citations.

19. (green2021northcarolinamacular pages 13-16): David J. Green, Eva Lenassi, Cerys S. Manning, David McGaughey, Vinod Sharma, Graeme C. Black, Jamie M. Ellingford, and Panagiotis I. Sergouniotis. North carolina macular dystrophy: phenotypic variability and computational analysis of disease-implicated non-coding variants. MedRxiv, Mar 2021. URL: https://doi.org/10.1101/2021.03.05.21252975, doi:10.1101/2021.03.05.21252975. This article has 3 citations.

20. (chiang2023electrophysiologicalevaluationof pages 7-9): Tsun-Kang Chiang and Minzhong Yu. Electrophysiological evaluation of macular dystrophies. Journal of Clinical Medicine, 12:1430, Feb 2023. URL: https://doi.org/10.3390/jcm12041430, doi:10.3390/jcm12041430. This article has 7 citations.

21. (nekolova2022moderndiagnosticand pages 2-6): Jana Nekolova, Alexandr Stepanov, Bohdan Kousal, Marketa Stredova, and Nada Jiraskova. Modern diagnostic and therapeutic approaches in familial maculopathy with reference to north carolina macular dystrophy. Biomedical Papers, 166:418-427, Dec 2022. URL: https://doi.org/10.5507/bp.2021.037, doi:10.5507/bp.2021.037. This article has 4 citations.

22. (small2016northcarolinamacular media 3981bb1f): Kent W. Small, Adam P. DeLuca, S. Scott Whitmore, Thomas Rosenberg, Rosemary Silva-Garcia, Nitin Udar, Bernard Puech, Charles A. Garcia, Thomas A. Rice, Gerald A. Fishman, Elise Héon, James C. Folk, Luan M. Streb, Christine M. Haas, Luke A. Wiley, Todd E. Scheetz, John H. Fingert, Robert F. Mullins, Budd A. Tucker, and Edwin M. Stone. North carolina macular dystrophy is caused by dysregulation of the retinal transcription factor prdm13. Ophthalmology, 123 1:9-18, Jan 2016. URL: https://doi.org/10.1016/j.ophtha.2015.10.006, doi:10.1016/j.ophtha.2015.10.006. This article has 143 citations and is from a highest quality peer-reviewed journal.

23. (small2016northcarolinamacular media deebfcdf): Kent W. Small, Adam P. DeLuca, S. Scott Whitmore, Thomas Rosenberg, Rosemary Silva-Garcia, Nitin Udar, Bernard Puech, Charles A. Garcia, Thomas A. Rice, Gerald A. Fishman, Elise Héon, James C. Folk, Luan M. Streb, Christine M. Haas, Luke A. Wiley, Todd E. Scheetz, John H. Fingert, Robert F. Mullins, Budd A. Tucker, and Edwin M. Stone. North carolina macular dystrophy is caused by dysregulation of the retinal transcription factor prdm13. Ophthalmology, 123 1:9-18, Jan 2016. URL: https://doi.org/10.1016/j.ophtha.2015.10.006, doi:10.1016/j.ophtha.2015.10.006. This article has 143 citations and is from a highest quality peer-reviewed journal.