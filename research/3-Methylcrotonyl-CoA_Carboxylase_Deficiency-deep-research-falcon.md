---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-02T23:34:31.381749'
end_time: '2026-05-03T00:03:15.574470'
duration_seconds: 1724.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 3-Methylcrotonyl-CoA Carboxylase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3-Methylcrotonyl-CoA Carboxylase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3-Methylcrotonyl-CoA Carboxylase Deficiency** covering all of the
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
- **Disease Name:** 3-Methylcrotonyl-CoA Carboxylase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3-Methylcrotonyl-CoA Carboxylase Deficiency** covering all of the
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


# Comprehensive Disease Characteristics Report: 3‑Methylcrotonyl‑CoA Carboxylase Deficiency (3‑MCCD)

## Executive summary
3‑Methylcrotonyl‑CoA carboxylase deficiency (3‑MCCD; also “3‑methylcrotonyl‑CoA carboxylase (MCC) deficiency”) is an autosomal recessive inborn error of **leucine catabolism** caused by biallelic pathogenic variants in **MCCC1** (MCCα) or **MCCC2** (MCCβ). It is frequently detected by expanded newborn screening (NBS) via elevated **C5OH (3‑hydroxyisovalerylcarnitine)**, but penetrance is low and many screen‑identified individuals remain asymptomatic, generating ongoing controversy about screening utility and case definitions. Key confirmatory biochemical features include increased urinary **3‑hydroxyisovaleric acid (3‑HIVA)** and **3‑methylcrotonylglycine (3‑MCG)** and frequent **secondary carnitine deficiency**. Recent (2024) NBS cohorts provide updated incidence and predictive‑value statistics, while 2024 cryo‑EM structures provide a new mechanistic framework for interpreting enzyme dysfunction. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2, lin2024newbornscreeningand pages 4-5, zhou2024structuralinsightsinto pages 4-6)

| Topic | Key finding / quantitative detail | Source paper(s) | Context citation |
|---|---|---|---|
| Definition | Autosomal recessive defect of leucine metabolism caused by deficiency of mitochondrial 3-methylcrotonyl-CoA carboxylase; phenotype ranges from severe neonatal disease to asymptomatic adults. Quote: “phenotype is highly variable ranging from acute neonatal onset with fatal outcome to asymptomatic adults.” | Grünert et al., 2012; Lin et al., 2024 | (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2) |
| Genes | Disease genes are **MCCC1** (MCCα) and **MCCC2** (MCCβ). Lin 2024 reports MCCC1 at 3q25–27 and MCCC2 at 5q12-q13.1. | Grünert et al., 2012; Lin et al., 2024 | (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2) |
| OMIM IDs reported | Literature reports both **OMIM 210200** and **OMIM 210210** for isolated 3-MCCD/MCC deficiency; Morscher 2012 explicitly lists “OMIM ID: 210200 / 210210,” indicating historical inconsistency that should be reconciled against OMIM directly. | Forsyth et al., 2016; Lin et al., 2024; Morscher et al., 2012 | (forsyth2016outcomesofcases pages 1-2, lin2024newbornscreeningand pages 1-2, morscher2012asinglemutation pages 1-2) |
| Newborn screening ascertainment | In the 88-person international cohort, **53/88 (60%)** were identified by newborn screening, **26/88** by symptoms/family history, and **9** mothers after an abnormal infant screen. | Grünert et al., 2012 | (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, grunert20123methylcrotonylcoacarboxylasedeficiency pages 12-13) |
| Newborn screening incidence (Quanzhou, 2024) | **17 neonatal cases among 643,606 screened**, plus 2 maternal and 1 paternal cases; estimated incidence **1/37,859** newborns. | Lin et al., 2024 | (lin2024newbornscreeningand pages 1-2, lin2024newbornscreeningand pages 3-4) |
| Newborn screening incidence (Quanzhou, 2025 update) | In a later 10-year Quanzhou cohort, **18 3-MCCD cases among 693,797** screened; reported incidence **1/38,544**. | Lin et al., 2025 | (lin2025largescalenewbornscreening pages 6-7, lin2025largescalenewbornscreening pages 1-2) |
| NBS PPV / false positives | Quanzhou 2024: **2,487/643,606 (0.39%)** had elevated C5OH, but only **17** neonatal 3-MCCD diagnoses, giving **PPV 0.69%** and an implied false-positive rate among C5OH-positive screens of about **99.31%**. | Lin et al., 2024 | (lin2024newbornscreeningand pages 3-4, lin2024newbornscreeningand pages 4-5) |
| C5OH-positive disorder breakdown (Saudi cohort) | KAMC screened **110,787** newborns; **31** had initial elevated C5OH, **15 (48%)** were true positives, including **11 3-MCCD** and **4 HMG-CoA lyase deficiency**. | Al Mutairi et al., 2024 | (mutairi2024outcomesofcases pages 2-3) |
| Proportion asymptomatic | In the 88-individual cohort, **57%** were asymptomatic overall. Forsyth 2016 also notes that **>90%** of NBS-identified cases appear clinically asymptomatic. | Grünert et al., 2012; Forsyth et al., 2016 | (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, forsyth2016outcomesofcases pages 1-2) |
| Symptomatic frequency | Lin 2024 observed clinical symptoms in **11.8%** of identified patients; however, authors noted uncertainty whether all symptoms were attributable to 3-MCCD. | Lin et al., 2024 | (lin2024newbornscreeningand pages 1-2, lin2024newbornscreeningand pages 4-5) |
| Acute metabolic decompensation frequency | Grünert 2012: **12/88** had acute metabolic decompensations, including **5/53** detected by NBS. Italian 2025 follow-up: **1/9** screened children had decompensation during intercurrent illness. | Grünert et al., 2012; Gragnaniello et al., 2025 | (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, gragnaniello2025psychologicalimpactof pages 4-6) |
| Developmental outcomes | Forsyth 2016: among 25 NBS cases, **6** had developmental delay reports (2 later excluded for other diagnoses). Lin 2024 reported **1 untreated child** with global developmental delay by age 2. | Forsyth et al., 2016; Lin et al., 2024 | (forsyth2016outcomesofcases pages 4-6, lin2024newbornscreeningand pages 4-5) |
| Key biomarkers | Core markers are elevated **C5OH (3-hydroxyisovalerylcarnitine)** in dried blood and increased urinary **3-methylcrotonylglycine (3-MCG)** and **3-hydroxyisovaleric acid (3-HIVA)**. | Grünert et al., 2012; Lin et al., 2024 | (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2, grunert20123methylcrotonylcoacarboxylasedeficiency media b6f5c761) |
| Biomarker performance | Lin 2024: all affected neonates had elevated C5OH; **13/17 (76.5%)** had elevated urinary 3-MCG and 3-HIVA, while **23.5%** had normal urine organic acids despite diagnosis. | Lin et al., 2024 | (lin2024newbornscreeningand pages 1-2, lin2024newbornscreeningand pages 3-4) |
| Secondary carnitine deficiency | Lin 2024: **8 neonates** and **all adults** had secondary carnitine deficiency. In the Italian 2025 cohort, **5/9** followed children required carnitine supplementation for low free carnitine. | Lin et al., 2024; Gragnaniello et al., 2025 | (lin2024newbornscreeningand pages 1-2, lin2024newbornscreeningand pages 3-4, gragnaniello2025psychologicalimpactof pages 4-6) |
| Genotype distribution / variants | Lin 2024: **47.1%** had MCCC1 variants and **52.9%** had MCCC2 variants; **17 variants** identified total, including **6 novel**. Common variants were **MCCC1 c.1331G>A** and **MCCC2 c.351_353delTGG**. Grünert 2012 found **15 novel MCCC1** and **16 novel MCCC2** alleles. | Lin et al., 2024; Grünert et al., 2012 | (lin2024newbornscreeningand pages 1-2, lin2024newbornscreeningand pages 4-5, grunert20123methylcrotonylcoacarboxylasedeficiency pages 2-3) |
| Single-allele positive screens | Morscher 2012 found **21/22** individuals with partial enzyme reduction carried only a single mutant allele, showing that heterozygosity can cause biochemical/NBS positivity and potential over-diagnosis. | Morscher et al., 2012 | (morscher2012asinglemutation pages 1-2, morscher2012asinglemutation pages 2-3, morscher2012asinglemutation pages 3-4) |
| Non-specific phenotypes may reflect other disorders | Shepard 2015: among individuals with nonspecific phenotypes, **5/10** had a homozygous damaging mutation in another disease gene likely explaining symptoms; quote: “nonspecific phenotypes attributed to MCCD are associated with consanguinity and are likely not due to mutations in the MCC enzyme…” | Shepard et al., 2015 | (shepard2015consanguinityandrare pages 1-2, shepard2015consanguinityandrare pages 6-7, shepard2015consanguinityandrare pages 7-8) |
| Consanguinity signal | Shepard 2015 found **70%** of the nonspecific-phenotype group had runs of homozygosity consistent with at least second-cousin-level inbreeding. | Shepard et al., 2015 | (shepard2015consanguinityandrare pages 6-7) |
| Treatment / management reported | Common management includes **oral L-carnitine** and **modest leucine restriction**; evidence base remains limited. Grünert 2012 states management is mainly “supplementation with oral L-carnitine and a diet modestly restricted in leucine,” but efficacy is unproven. | Grünert et al., 2012; Forsyth et al., 2016 | (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, grunert20123methylcrotonylcoacarboxylasedeficiency pages 2-3, forsyth2016outcomesofcases pages 4-6) |
| Carnitine dosing used in practice | Lin 2024 recommended **oral L-carnitine 50–100 mg/kg, 2–3 times daily** for neonates with low C0; one hyperammonemic patient received **L-carnitine and arginine**. | Lin et al., 2024 | (lin2024newbornscreeningand pages 4-5) |
| Real-world treatment frequencies | Forsyth 2016: **18/25** NBS cases received carnitine supplementation and **10/25** were placed on a low-leucine diet. | Forsyth et al., 2016 | (forsyth2016outcomesofcases pages 4-6) |
| Carnitine trial data | Thomsen 2015 studied **13** Faroese adults (all homozygous for **MCCC1 c.1526delG**). Plasma free carnitine increased from **6.9** to **25.5** μmol/L and muscle free carnitine from **785** to **1,827 nmol/g wet weight** with supplementation; **7/13** reported fatigue and some symptomatic relief. Authors concluded a general recommendation could **not** yet be made. | Thomsen et al., 2015 | (thomsen2015islcarnitinesupplementation pages 1-2, thomsen2015islcarnitinesupplementation pages 4-5, thomsen2015islcarnitinesupplementation pages 7-8, thomsen2015islcarnitinesupplementation pages 8-9) |
| Emergency / illness management | Recent follow-up cohorts provide families with an **emergency protocol** for intercurrent illnesses; in the Italian program, one child with illness-associated decompensation responded to **glucose and increased carnitine**. | Gragnaniello et al., 2025 | (gragnaniello2025psychologicalimpactof pages 4-6) |
| False-negative / atypical diagnosis | Jagadish 2023 described a child diagnosed at **12 months** despite a normal newborn screen, with only borderline C5OH and atypical recurrent infections/GI symptoms; highlights that normal NBS does not exclude disease. | Jagadish et al., 2023 | (jagadish2023auniquepresentation pages 1-4, jagadish2023auniquepresentation pages 4-5) |
| Key structural/mechanistic insight (2024) | High-resolution cryo-EM solved human MCC holoenzyme structures at **2.29–2.85 Å**. A central finding was ligand-dependent movement of biotin from an **exo-site** to an **endo-site** upon acyl-CoA binding, supporting coordinated catalysis. Quote: “biotin is relocated from an exo-site to an endo-site upon acetyl-CoA binding.” | Zhou et al., 2024 | (zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 1-4, zhou2024structuralinsightsinto pages 7-9, zhou2024structuralinsightsinto pages 6-7) |


*Table: This table condenses the most actionable identifiers, epidemiology, biochemical markers, genotype data, management findings, and a 2024 structural insight for 3-methylcrotonyl-CoA carboxylase deficiency. It is useful as a quick reference for drafting the full evidence-based disease report.*

## 1. Disease information
### 1.1 Overview (definition)
* **Definition:** Isolated 3‑MCC deficiency is an autosomal recessive defect of leucine metabolism caused by deficiency of mitochondrial 3‑methylcrotonyl‑CoA carboxylase due to variants in **MCCC1** or **MCCC2**. The clinical spectrum is broad; Grünert et al. describe the phenotype as “**ranging from acute neonatal onset with fatal outcome to asymptomatic adults**.” (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)
* **Typical biochemical signature:** Elevated **C5OH** in blood spots and increased urinary **3‑HIVA** and **3‑MCG**; low plasma free carnitine may occur and is common as a secondary effect. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2)

### 1.2 Key identifiers (knowledge-base cross references)
* **OMIM:** Multiple peer‑reviewed articles report both **OMIM 210200** and **OMIM 210210** for MCC deficiency/3‑MCCD, reflecting historical inconsistency; e.g., Morscher et al. explicitly list “**OMIM ID: 210200 / 210210**.” (morscher2012asinglemutation pages 1-2)
* **Other requested identifiers (Orphanet, MeSH, ICD‑10/ICD‑11, MONDO):** Not explicitly present in the retrieved full‑text evidence. These should be pulled directly from the authoritative registries (OMIM/Orphanet/MONDO/MeSH/ICD) during KB curation; this report cannot assert those codes without sourced evidence in the retrieved corpus.

### 1.3 Synonyms / alternative names
Common names used in the literature include:
* “3‑methylcrotonyl‑CoA carboxylase deficiency” (3‑MCCD) (lin2024newbornscreeningand pages 1-2)
* “3‑methylcrotonyl‑CoA carboxylase (MCC) deficiency” (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)
* “methylcrotonylglycinuria” (used historically; reflected by urinary 3‑MCG) (lee2018clinicalmanifestationsgene pages 1-3)

### 1.4 Evidence source types
* **Aggregated disease-level resources** were not directly retrieved here (e.g., Orphanet/GeneReviews pages). The present report relies primarily on **peer‑reviewed cohorts**, NBS program reports, and mechanistic/structural primary studies. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2, mutairi2024outcomesofcases pages 2-3, zhou2024structuralinsightsinto pages 4-6)

## 2. Etiology
### 2.1 Disease causal factors
* **Genetic cause:** Biallelic variants in **MCCC1** or **MCCC2** cause enzymatic deficiency of MCC (a biotin‑dependent mitochondrial carboxylase). (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2)

### 2.2 Risk factors
* **Consanguinity and alternative recessive diagnoses:** In a whole‑exome sequencing study, Shepard et al. concluded that “**nonspecific phenotypes attributed to MCCD are associated with consanguinity and are likely not due to mutations in the MCC enzyme but result from rare homozygous mutations in other disease genes**,” finding that 5/10 individuals with nonspecific phenotypes carried a likely explanatory homozygous damaging variant in another disease gene. (shepard2015consanguinityandrare pages 1-2, shepard2015consanguinityandrare pages 6-7)

### 2.3 Protective factors / gene–environment interactions
* No explicit protective genetic variants or formal gene–environment interaction studies were identified in the retrieved evidence.

## 3. Phenotypes
### 3.1 Core clinical phenotype spectrum
* **Variable expressivity / low penetrance:** In an 88‑individual cohort, **57% were asymptomatic** and **43% had reported symptoms** (with potential ascertainment bias), while **12 individuals** experienced acute metabolic decompensation (including **5** identified by NBS). (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)
* **NBS‑identified cohorts are commonly asymptomatic:** The IBEM‑IS report notes **>90%** of NBS‑identified individuals appear asymptomatic, but a minority present with “traditional” metabolic illness (acidosis, hyperammonemia, lactic acidosis) or developmental concerns; importantly, NBS C5OH level did not correlate with outcomes. (forsyth2016outcomesofcases pages 1-2)
* **Frequency of symptoms in a recent NBS cohort:** In Quanzhou (China), Lin et al. observed symptoms in **11.8%** of diagnosed individuals, while emphasizing uncertainty about attribution. (lin2024newbornscreeningand pages 1-2)

### 3.2 Example phenotype elements (with suggested HPO terms)
Because frequency-by-phenotype was not consistently extractable across all studies, below are common/important phenotype types reported and suitable HPO suggestions:
* **Acute metabolic decompensation** (often illness/fasting associated): HP:0001942 (Metabolic acidosis), HP:0001987 (Hyperammonemia), HP:0001943 (Ketosis), HP:0003074 (Hypoglycemia). (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, forsyth2016outcomesofcases pages 1-2)
* **Seizures**: HP:0001250 (Seizures). (forsyth2016outcomesofcases pages 1-2)
* **Developmental delay / neurodevelopmental issues** (not always attributable): HP:0001263 (Global developmental delay), HP:0000750 (Delayed speech and language development), HP:0001252 (Muscular hypotonia). (forsyth2016outcomesofcases pages 4-6, lin2024newbornscreeningand pages 4-5, forsyth2016outcomesofcases pages 1-2)
* **Failure to thrive**: HP:0001508 (Failure to thrive). (forsyth2016outcomesofcases pages 1-2)

### 3.3 Laboratory abnormalities (with suggested HPO terms)
* **Elevated C5OH (3‑hydroxyisovalerylcarnitine)**: HP:0003355 (Abnormal acylcarnitine profile) / (no single HPO term perfectly captures C5OH; store as lab feature).
* **Elevated urinary organic acids (3‑HIVA, 3‑MCG)**: HP:0033216 (Increased urinary organic acids) (general) plus structured metabolite annotations. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 3-4)
* **Secondary carnitine deficiency (low free carnitine, C0)**: HP:0003302 (Carnitine deficiency). (lin2024newbornscreeningand pages 3-4, gragnaniello2025psychologicalimpactof pages 4-6)

### 3.4 Quality-of-life impact
* Adult Faroese cohort: **fatigue** was a prominent patient‑reported symptom (reported by ~54% in the studied group) with some improvement upon carnitine supplementation, suggesting a potential QoL domain for follow‑up even in “mild” cases. (thomsen2015islcarnitinesupplementation pages 7-8)

## 4. Genetic / molecular information
### 4.1 Causal genes
* **MCCC1** (MCCα subunit) and **MCCC2** (MCCβ subunit) are the causal genes. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2)

### 4.2 Pathogenic variants and variant spectrum
* **Large allelic heterogeneity:** Grünert et al. identified **15 novel MCCC1** and **16 novel MCCC2** mutant alleles in their cohort and concluded that genotype and biochemical phenotype were not useful in predicting clinical course. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 2-3, grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)
* **Recent NBS variant data (Quanzhou 2014–2022):** Lin et al. reported **17 variants** across MCCC1/MCCC2, including **six novel variants**; MCCC1 variants were seen in 47.1% and MCCC2 variants in 52.9% of cases, with population‑specific common alleles (e.g., MCCC1 c.1331G>A; MCCC2 c.351_353delTGG). (lin2024newbornscreeningand pages 3-4, lin2024newbornscreeningand pages 4-5)

### 4.3 Important interpretive caveat: heterozygous variants and screening positives
* Morscher et al. demonstrated that **a single deleterious allele** (carrier state) can be associated with biochemical abnormalities sufficient to trigger positive NBS/SMS results; in their group with only partially reduced MCC activity, **21/22** carried a single mutant allele (mostly in MCCC1). This supports careful confirmatory testing and avoidance of overdiagnosis. (morscher2012asinglemutation pages 1-2, morscher2012asinglemutation pages 2-3)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
* No specific modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities were identified in the retrieved evidence.

## 5. Environmental information
* No specific environmental toxin/infection risk factors were established in the retrieved evidence.
* **Triggering context for clinical crises:** Intercurrent illness/physiologic stress is repeatedly implicated as a context for metabolic decompensation in follow‑up protocols (e.g., emergency protocols for infections). (gragnaniello2025psychologicalimpactof pages 4-6)

## 6. Mechanism / pathophysiology
### 6.1 Biochemical pathway position and causal chain
* **Enzymatic step:** MCC is a mitochondrial biotin‑dependent carboxylase (EC 6.4.1.4) that catalyzes a key step in leucine catabolism—conversion of **3‑methylcrotonyl‑CoA to 3‑methylglutaconyl‑CoA**. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lee2018clinicalmanifestationsgene pages 1-3)
* **Metabolite diversion and diagnostic markers:** When MCC activity is impaired, accumulated 3‑methylcrotonyl‑CoA is diverted to alternative products including **3‑MCG** (glycine conjugate) and **3‑HIVA**; 3‑HIVA forms carnitine esters (C5OH), explaining the NBS marker. (lee2018clinicalmanifestationsgene pages 1-3)
* **Secondary carnitine deficiency mechanism (current understanding):** Elevated acylcarnitine formation and excretion is consistent with depletion of free carnitine pools; multiple cohorts report low C0/free carnitine in a subset and/or need for supplementation. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 3-4, gragnaniello2025psychologicalimpactof pages 4-6)

### 6.2 Structural and mechanistic advances (2024)
* **High-resolution structures:** Zhou et al. (bioRxiv 2024) reported cryo‑EM structures of human MCC (and PCC) at ~2.29–3.38 Å resolution and highlighted coordinated catalysis; notably, in MCC “**biotin is relocated from an exo-site to an endo-site upon acetyl-CoA binding**,” suggesting coupling between acyl‑CoA binding and biotin positioning. (zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 1-4)

### 6.3 Tissue injury mechanisms (non-human experimental evidence)
* **Oxidative stress hypothesis:** In rat cerebral cortex preparations, exposure to accumulating metabolites (3‑MCG, 3‑methylcrotonic acid) increased lipid peroxidation (TBA‑RS) and protein carbonyls, and antioxidant scavengers prevented lipid damage, supporting oxidative injury as a plausible downstream mechanism for neurologic involvement in some cases. (zanatta2013neurochemicalevidencethat pages 1-2, zanatta2013neurochemicalevidencethat pages 7-8)

### 6.4 Suggested ontology mappings
**GO Biological Process (suggested):**
* “leucine catabolic process” (for MCCC1/MCCC2 role) (supported by pathway placement) (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lee2018clinicalmanifestationsgene pages 1-3)
* “mitochondrial carboxylation” / “biotin-dependent carboxylation” (mechanism) (zhou2024structuralinsightsinto pages 1-4)
* “cellular response to oxidative stress” (downstream hypothesis from metabolite toxicity studies) (zanatta2013neurochemicalevidencethat pages 1-2)

**GO Cellular Component (suggested):**
* “mitochondrion” (enzyme localization) (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)

**Cell Ontology (CL) (suggested):**
* “astrocyte” / “neuron” are plausible relevant cell types for neurologic manifestations; however, direct evidence in this retrieved corpus is limited to rat cortex preparations rather than human cell-type localization. (zanatta2013neurochemicalevidencethat pages 1-2)

## 7. Anatomical structures affected
* **Primary systems:** Metabolic decompensation phenotypes implicate systemic energy metabolism; clinically salient involvement often includes **central nervous system** (seizures, developmental issues), though causality can be confounded by ascertainment and co-morbid genetic diagnoses in consanguineous cases. (forsyth2016outcomesofcases pages 1-2, shepard2015consanguinityandrare pages 1-2)

**UBERON suggestions (for KB indexing):**
* UBERON:0000955 (brain), UBERON:0000178 (blood), UBERON:0002048 (liver) (as major metabolic organ; direct organ-specific data not quantified in the retrieved texts).

## 8. Temporal development
* **Onset variability:** Ranges from neonatal acute metabolic disease to asymptomatic adulthood. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)
* **Late/atypical identification:** A case report documented diagnosis at 12 months despite normal NBS, supporting that NBS can miss some affected individuals. (jagadish2023auniquepresentation pages 1-4)

## 9. Inheritance and population
### 9.1 Inheritance
* **Autosomal recessive** inheritance is consistently reported. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2, lin2024newbornscreeningand pages 1-2)

### 9.2 Epidemiology / incidence and prevalence (recent data emphasized)
* **Quanzhou, China (2014–2022):** 17 neonatal cases among 643,606 screened; incidence **1/37,859**. (lin2024newbornscreeningand pages 3-4)
* **Quanzhou, China (2014–2023):** 18 cases among 693,797 screened; incidence **1/38,544** (10‑year organic acidemia NBS report). (lin2025largescalenewbornscreening pages 6-7, lin2025largescalenewbornscreening pages 1-2)
* **Saudi cohort (2011–2023):** 110,787 screened; 31 initial C5OH positives; 15 true positives, including **11 3‑MCCD**. (mutairi2024outcomesofcases pages 2-3)
* **Reported prevalence range across screened populations:** IBEM‑IS summarizes literature prevalence ranging from **1:2,400 to 1:68,000** depending on population/screening context. (forsyth2016outcomesofcases pages 1-2)

### 9.3 Population genetics notes
* **Founder effect example:** Faroese cohort (all homozygous for MCCC1 c.1526delG in the studied group) illustrates population-specific variant enrichment and unusually high local prevalence. (thomsen2015islcarnitinesupplementation pages 1-2)

## 10. Diagnostics
### 10.1 Screening
* **Primary NBS marker:** elevated **C5OH** on dried blood spot acylcarnitine profiling by MS/MS. (lin2024newbornscreeningand pages 3-4, gragnaniello2025psychologicalimpactof pages 1-3)
* **High false-positive burden:** In the Quanzhou 2014–2022 program, 2,487 newborns had elevated C5OH (0.39%), but only 17 neonatal 3‑MCCD diagnoses (PPV **0.69%**), i.e., the vast majority of C5OH elevations were not neonatal 3‑MCCD. (lin2024newbornscreeningand pages 3-4, lin2024newbornscreeningand pages 4-5)

### 10.2 Confirmatory testing
* **Urine organic acids:** Elevation of **3‑MCG** and **3‑HIVA** supported diagnosis in 76.5% of Quanzhou neonatal cases, while ~23.5% had normal urine organic acids despite diagnosis, underscoring the need for genetic confirmation. (lin2024newbornscreeningand pages 3-4)
* **Genetic testing:** Definitive diagnosis relies on sequencing of **MCCC1/MCCC2**; Lin et al. emphasize the need for “definitive genetic testing.” (lin2024newbornscreeningand pages 2-3)
* **Enzyme assay:** Profoundly reduced fibroblast MCC activity can support diagnosis (e.g., <5% of controls in many lines in Grünert et al.). (grunert20123methylcrotonylcoacarboxylasedeficiency pages 12-13)

### 10.3 Differential diagnosis (C5OH is not specific)
* C5OH elevations overlap with other disorders (e.g., HMG‑CoA lyase deficiency), demonstrated by the Saudi cohort where true positives included both 3‑MCCD and HMG‑CoA lyase deficiency. (mutairi2024outcomesofcases pages 2-3, gragnaniello2025psychologicalimpactof pages 1-3)

## 11. Outcome / prognosis
* **Generally favorable in many NBS cohorts:** The Saudi cohort notes none of their 3‑MCCD cases had neonatal symptoms/complications and overall outcomes were benign in most. (mutairi2024outcomesofcases pages 2-3, mutairi2024outcomesofcases pages 3-4)
* **But severe events can occur:** Acute metabolic decompensation occurred in 12/88 individuals in Grünert et al., including NBS‑identified individuals. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)
* **Attribution challenges:** Exome sequencing evidence indicates that some nonspecific neurodevelopmental phenotypes may be due to other recessive disorders, especially in consanguineous families, complicating prognosis attribution. (shepard2015consanguinityandrare pages 1-2, shepard2015consanguinityandrare pages 6-7)

## 12. Treatment
### 12.1 Current management (real-world practice)
* **Dietary management:** Modest leucine restriction/low‑protein approaches are used in some cohorts. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 2-3, forsyth2016outcomesofcases pages 4-6)
* **Carnitine supplementation:** Commonly used when free carnitine is low; in an IBEM‑IS NBS cohort, **18/25** received carnitine supplementation and **10/25** were placed on restricted diet. (forsyth2016outcomesofcases pages 4-6)
* **Dose example from practice:** Lin et al. recommended **oral L‑carnitine 50–100 mg/kg, 2–3 times daily** for neonates with low C0/free carnitine. (lin2024newbornscreeningand pages 4-5)

### 12.2 Evidence on carnitine supplementation benefit
* **Intervention evidence (Faroese adults):** Supplementation increased plasma free carnitine from ~6.9 to ~25.5 μmol/L and muscle free carnitine from ~785 to ~1,827 nmol/g wet weight; some patients reported fatigue improvement, but authors concluded general supplementation recommendations remain premature and may be best targeted to symptomatic or carnitine‑deficient individuals. (thomsen2015islcarnitinesupplementation pages 1-2, thomsen2015islcarnitinesupplementation pages 4-5, thomsen2015islcarnitinesupplementation pages 8-9)

### 12.3 Acute illness / emergency protocols
* Follow‑up programs may provide an emergency protocol for intercurrent illness; in one cohort, metabolic decompensation during infection responded to glucose and increased carnitine. (gragnaniello2025psychologicalimpactof pages 4-6)

### 12.4 Suggested MAXO terms (examples)
* Dietary leucine restriction: MAXO term for “dietary restriction” (general; exact MAXO ID not in evidence).
* L‑carnitine supplementation: MAXO term for “dietary supplement therapy” / “carnitine supplementation” (exact MAXO ID not in evidence).
* Emergency protocol during illness: MAXO term for “emergency management protocol” (exact MAXO ID not in evidence).

## 13. Prevention
* **Primary prevention:** Not applicable (genetic disease), except via reproductive options.
* **Secondary prevention:** Newborn screening and confirmatory testing aim to prevent morbidity via early detection and management; however, high false‑positive rates and uncertain benefit for asymptomatic individuals are central policy concerns. (lin2024newbornscreeningand pages 3-4, gragnaniello2025psychologicalimpactof pages 1-3)

## 14. Other species / natural disease
* No naturally occurring veterinary (OMIA) cases were identified in the retrieved evidence.

## 15. Model organisms and experimental systems
### 15.1 Rat model (metabolite exposure)
* Rat cerebral cortex preparations exposed to accumulating metabolites showed oxidative damage markers, supporting a mechanistic hypothesis for neurologic injury. (zanatta2013neurochemicalevidencethat pages 1-2, zanatta2013neurochemicalevidencethat pages 2-4)

### 15.2 Human in vitro systems
* Fibroblast enzyme assays show severely reduced MCC activity in many patient cell lines and can be used for functional confirmation. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 12-13)

### 15.3 C. elegans leucine breakdown deficiency model (limitation)
* A 2024 Nature Metabolism paper on a C. elegans model of leucine breakdown deficiency was retrieved only as supplementary NMR spectra pages in the accessible text chunk; no extractable evidence about the actual model genotype/phenotype or host–microbe interaction findings was available in the retrieved content. (lee2024host–microbeinteractionsrewire pages 1-12)

## Recent developments (2023–2024 prioritized)
1. **Population NBS performance metrics (2024):** Quanzhou (China) reported incidence 1/37,859 with very low PPV (0.69%) for elevated C5OH as a 3‑MCCD screen, strengthening the evidence base for debates about second‑tier testing and reporting practices. (lin2024newbornscreeningand pages 3-4)
2. **C5OH-positive outcomes (2024):** A Saudi program report quantified true‑positive fractions and showed that C5OH elevation identifies both 3‑MCCD and other disorders (e.g., HMG‑CoA lyase deficiency), supporting careful differential diagnosis and possibly altered reporting strategies. (mutairi2024outcomesofcases pages 2-3)
3. **Structural biology advance (2024):** High-resolution MCC cryo‑EM structures and biotin exo→endo relocation provide a new framework for mechanistic interpretation of disease variants (preprint; not yet peer-reviewed at time of posting). (zhou2024structuralinsightsinto pages 4-6, zhou2024structuralinsightsinto pages 1-4)
4. **Clinical vigilance for false negatives (2023):** Case report of bi‑allelic MCCC2 disease with normal NBS highlights limitations of biochemical screening sensitivity. (jagadish2023auniquepresentation pages 1-4)

## Expert interpretation / analysis (evidence-based)
* **Why screening remains contentious:** High false-positive rates from C5OH and low penetrance mean that screening detects many individuals who may never develop clear disease manifestations, creating a benefit–harm tradeoff (medicalization, parental anxiety, follow-up burden). Quantitative evidence of PPV ~0.69% in one large program illustrates the scale of this issue. (lin2024newbornscreeningand pages 3-4, gragnaniello2025psychologicalimpactof pages 1-3)
* **Attribution problem for neurodevelopmental findings:** The exome study indicates that nonspecific phenotypes in some “3‑MCCD” individuals may be due to other recessive diagnoses enriched by consanguinity, suggesting that symptomatic individuals (especially with nonspecific features) may warrant broader genomic evaluation rather than assuming MCC causality. (shepard2015consanguinityandrare pages 1-2, shepard2015consanguinityandrare pages 6-7)

## URLs and publication dates (where available in retrieved evidence)
* Grünert et al., Orphanet J Rare Dis, **May 2012**. https://doi.org/10.1186/1750-1172-7-31 (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2)
* Lin et al., Mol Genet Metab Rep, **Sep 2024**. https://doi.org/10.1016/j.ymgmr.2024.101127 (lin2024newbornscreeningand pages 1-2)
* Al Mutairi et al., Mol Genet Metab Rep, **Dec 2024**. https://doi.org/10.1016/j.ymgmr.2024.101153 (mutairi2024outcomesofcases pages 2-3)
* Zhou et al., bioRxiv, **Aug 2024** (preprint). https://doi.org/10.1101/2024.04.30.591959 (zhou2024structuralinsightsinto pages 4-6)
* Jagadish et al., Cureus, **May 2023**. https://doi.org/10.7759/cureus.39401 (jagadish2023auniquepresentation pages 1-4)
* Shepard et al., Genetics in Medicine, **Aug 2015**. https://doi.org/10.1038/gim.2014.157 (shepard2015consanguinityandrare pages 1-2)
* Thomsen et al., JIMD Reports, **Jan 2015**. https://doi.org/10.1007/8904_2014_393 (thomsen2015islcarnitinesupplementation pages 1-2)
* ClinicalTrials.gov: Early Check **NCT03655223** (posted 2018; record accessed via retrieved chunks). (NCT03655223 chunk 2)
* ClinicalTrials.gov: Kazakhstan MS/MS screening **NCT05910151** (posted 2022; record accessed via retrieved chunks). (NCT05910151 chunk 1)

## Notable data gaps (for KB completion)
* Authoritative codes for **Orphanet, MeSH, ICD‑10/ICD‑11, and MONDO** were not retrievable from the current tool evidence and should be imported directly from those registries.
* Detailed phenotype frequencies for specific HPO terms (beyond cohort-level symptomatic/asymptomatic rates) were not consistently extractable from the available text excerpts.
* No robust evidence for gene therapy/RNA therapy/CRISPR or disease-specific pharmacotherapy trials for 3‑MCCD was found in the retrieved evidence.



References

1. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 1-2): Sarah C Grünert, Martin Stucki, Raphael J Morscher, Terttu Suormala, Celine Bürer, Patricie Burda, Ernst Christensen, Can Ficicioglu, Jürgen Herwig, Stefan Kölker, Dorothea Möslinger, Elisabetta Pasquini, René Santer, K Otfried Schwab, Bridget Wilcken, Brian Fowler, Wyatt W Yue, and Matthias R Baumgartner. 3-methylcrotonyl-coa carboxylase deficiency: clinical, biochemical, enzymatic and molecular studies in 88 individuals. Orphanet Journal of Rare Diseases, 7:31-31, May 2012. URL: https://doi.org/10.1186/1750-1172-7-31, doi:10.1186/1750-1172-7-31. This article has 116 citations and is from a peer-reviewed journal.

2. (lin2024newbornscreeningand pages 1-2): Weihua Lin, Kunyi Wang, Yanru Chen, Zhenzhu Zheng, and Yiming Lin. Newborn screening and genetic diagnosis of 3-methylcrotonyl-coa carboxylase deficiency in quanzhou,china. Molecular Genetics and Metabolism Reports, 40:101127, Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101127, doi:10.1016/j.ymgmr.2024.101127. This article has 5 citations.

3. (lin2024newbornscreeningand pages 4-5): Weihua Lin, Kunyi Wang, Yanru Chen, Zhenzhu Zheng, and Yiming Lin. Newborn screening and genetic diagnosis of 3-methylcrotonyl-coa carboxylase deficiency in quanzhou,china. Molecular Genetics and Metabolism Reports, 40:101127, Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101127, doi:10.1016/j.ymgmr.2024.101127. This article has 5 citations.

4. (zhou2024structuralinsightsinto pages 4-6): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 9 citations.

5. (forsyth2016outcomesofcases pages 1-2): RaeLynn Forsyth, Catherine Walsh Vockley, Mathew J. Edick, Cynthia A. Cameron, Sally J. Hiner, Susan A. Berry, Jerry Vockley, and Georgianne L. Arnold. Outcomes of cases with 3-methylcrotonyl-coa carboxylase (3-mcc) deficiency - report from the inborn errors of metabolism information system. Molecular Genetics and Metabolism, 118:15-20, May 2016. URL: https://doi.org/10.1016/j.ymgme.2016.02.002, doi:10.1016/j.ymgme.2016.02.002. This article has 39 citations and is from a peer-reviewed journal.

6. (morscher2012asinglemutation pages 1-2): Raphael J. Morscher, Sarah Catharina Grünert, Céline Bürer, Patricie Burda, Terttu Suormala, Brian Fowler, and Matthias R. Baumgartner. A single mutation in mccc1 or mccc2 as a potential cause of positive screening for 3-methylcrotonyl-coa carboxylase deficiency. Molecular genetics and metabolism, 105 4:602-6, Apr 2012. URL: https://doi.org/10.1016/j.ymgme.2011.12.018, doi:10.1016/j.ymgme.2011.12.018. This article has 44 citations and is from a peer-reviewed journal.

7. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 12-13): Sarah C Grünert, Martin Stucki, Raphael J Morscher, Terttu Suormala, Celine Bürer, Patricie Burda, Ernst Christensen, Can Ficicioglu, Jürgen Herwig, Stefan Kölker, Dorothea Möslinger, Elisabetta Pasquini, René Santer, K Otfried Schwab, Bridget Wilcken, Brian Fowler, Wyatt W Yue, and Matthias R Baumgartner. 3-methylcrotonyl-coa carboxylase deficiency: clinical, biochemical, enzymatic and molecular studies in 88 individuals. Orphanet Journal of Rare Diseases, 7:31-31, May 2012. URL: https://doi.org/10.1186/1750-1172-7-31, doi:10.1186/1750-1172-7-31. This article has 116 citations and is from a peer-reviewed journal.

8. (lin2024newbornscreeningand pages 3-4): Weihua Lin, Kunyi Wang, Yanru Chen, Zhenzhu Zheng, and Yiming Lin. Newborn screening and genetic diagnosis of 3-methylcrotonyl-coa carboxylase deficiency in quanzhou,china. Molecular Genetics and Metabolism Reports, 40:101127, Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101127, doi:10.1016/j.ymgmr.2024.101127. This article has 5 citations.

9. (lin2025largescalenewbornscreening pages 6-7): Yiming Lin, Chunmei Lin, Zhenzhu Zheng, Yanru Chen, Faming Zheng, and Weihua Lin. Large-scale newborn screening for organic acidemias in quanzhou, china: a 10-year retrospective observational study. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-15625-1, doi:10.1038/s41598-025-15625-1. This article has 0 citations and is from a peer-reviewed journal.

10. (lin2025largescalenewbornscreening pages 1-2): Yiming Lin, Chunmei Lin, Zhenzhu Zheng, Yanru Chen, Faming Zheng, and Weihua Lin. Large-scale newborn screening for organic acidemias in quanzhou, china: a 10-year retrospective observational study. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-15625-1, doi:10.1038/s41598-025-15625-1. This article has 0 citations and is from a peer-reviewed journal.

11. (mutairi2024outcomesofcases pages 2-3): Fuad Al Mutairi, Randa Alkhalaf, Abdul Rafiq Khan, Ali Al Othaim, and Majid Alfadhel. Outcomes of cases with elevated 3-hydroxyisovaleryl carnitine report from the newborn screening program. Molecular Genetics and Metabolism Reports, 41:101153, Dec 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101153, doi:10.1016/j.ymgmr.2024.101153. This article has 4 citations.

12. (gragnaniello2025psychologicalimpactof pages 4-6): Vincenza Gragnaniello, Giacomo Gaiga, Chiara Cazzorla, Elena Porcù, Daniela Gueraldi, Andrea Puma, Christian Loro, Mara Doimo, Leonardo Salviati, and Alberto B. Burlina. Psychological impact of newborn screening for 3-methylcrotonyl-coa carboxylase deficiency: the parental experience. International Journal of Neonatal Screening, 11:115, Dec 2025. URL: https://doi.org/10.3390/ijns11040115, doi:10.3390/ijns11040115. This article has 0 citations.

13. (forsyth2016outcomesofcases pages 4-6): RaeLynn Forsyth, Catherine Walsh Vockley, Mathew J. Edick, Cynthia A. Cameron, Sally J. Hiner, Susan A. Berry, Jerry Vockley, and Georgianne L. Arnold. Outcomes of cases with 3-methylcrotonyl-coa carboxylase (3-mcc) deficiency - report from the inborn errors of metabolism information system. Molecular Genetics and Metabolism, 118:15-20, May 2016. URL: https://doi.org/10.1016/j.ymgme.2016.02.002, doi:10.1016/j.ymgme.2016.02.002. This article has 39 citations and is from a peer-reviewed journal.

14. (grunert20123methylcrotonylcoacarboxylasedeficiency media b6f5c761): Sarah C Grünert, Martin Stucki, Raphael J Morscher, Terttu Suormala, Celine Bürer, Patricie Burda, Ernst Christensen, Can Ficicioglu, Jürgen Herwig, Stefan Kölker, Dorothea Möslinger, Elisabetta Pasquini, René Santer, K Otfried Schwab, Bridget Wilcken, Brian Fowler, Wyatt W Yue, and Matthias R Baumgartner. 3-methylcrotonyl-coa carboxylase deficiency: clinical, biochemical, enzymatic and molecular studies in 88 individuals. Orphanet Journal of Rare Diseases, 7:31-31, May 2012. URL: https://doi.org/10.1186/1750-1172-7-31, doi:10.1186/1750-1172-7-31. This article has 116 citations and is from a peer-reviewed journal.

15. (grunert20123methylcrotonylcoacarboxylasedeficiency pages 2-3): Sarah C Grünert, Martin Stucki, Raphael J Morscher, Terttu Suormala, Celine Bürer, Patricie Burda, Ernst Christensen, Can Ficicioglu, Jürgen Herwig, Stefan Kölker, Dorothea Möslinger, Elisabetta Pasquini, René Santer, K Otfried Schwab, Bridget Wilcken, Brian Fowler, Wyatt W Yue, and Matthias R Baumgartner. 3-methylcrotonyl-coa carboxylase deficiency: clinical, biochemical, enzymatic and molecular studies in 88 individuals. Orphanet Journal of Rare Diseases, 7:31-31, May 2012. URL: https://doi.org/10.1186/1750-1172-7-31, doi:10.1186/1750-1172-7-31. This article has 116 citations and is from a peer-reviewed journal.

16. (morscher2012asinglemutation pages 2-3): Raphael J. Morscher, Sarah Catharina Grünert, Céline Bürer, Patricie Burda, Terttu Suormala, Brian Fowler, and Matthias R. Baumgartner. A single mutation in mccc1 or mccc2 as a potential cause of positive screening for 3-methylcrotonyl-coa carboxylase deficiency. Molecular genetics and metabolism, 105 4:602-6, Apr 2012. URL: https://doi.org/10.1016/j.ymgme.2011.12.018, doi:10.1016/j.ymgme.2011.12.018. This article has 44 citations and is from a peer-reviewed journal.

17. (morscher2012asinglemutation pages 3-4): Raphael J. Morscher, Sarah Catharina Grünert, Céline Bürer, Patricie Burda, Terttu Suormala, Brian Fowler, and Matthias R. Baumgartner. A single mutation in mccc1 or mccc2 as a potential cause of positive screening for 3-methylcrotonyl-coa carboxylase deficiency. Molecular genetics and metabolism, 105 4:602-6, Apr 2012. URL: https://doi.org/10.1016/j.ymgme.2011.12.018, doi:10.1016/j.ymgme.2011.12.018. This article has 44 citations and is from a peer-reviewed journal.

18. (shepard2015consanguinityandrare pages 1-2): Peter J. Shepard, Bruce A. Barshop, Matthias R. Baumgartner, John-Bjarne Hansen, Kristen Jepsen, Erin N. Smith, and Kelly A. Frazer. Consanguinity and rare mutations outside of mccc genes underlie nonspecific phenotypes of mccd. Genetics in Medicine, 17:660-667, Aug 2015. URL: https://doi.org/10.1038/gim.2014.157, doi:10.1038/gim.2014.157. This article has 19 citations and is from a highest quality peer-reviewed journal.

19. (shepard2015consanguinityandrare pages 6-7): Peter J. Shepard, Bruce A. Barshop, Matthias R. Baumgartner, John-Bjarne Hansen, Kristen Jepsen, Erin N. Smith, and Kelly A. Frazer. Consanguinity and rare mutations outside of mccc genes underlie nonspecific phenotypes of mccd. Genetics in Medicine, 17:660-667, Aug 2015. URL: https://doi.org/10.1038/gim.2014.157, doi:10.1038/gim.2014.157. This article has 19 citations and is from a highest quality peer-reviewed journal.

20. (shepard2015consanguinityandrare pages 7-8): Peter J. Shepard, Bruce A. Barshop, Matthias R. Baumgartner, John-Bjarne Hansen, Kristen Jepsen, Erin N. Smith, and Kelly A. Frazer. Consanguinity and rare mutations outside of mccc genes underlie nonspecific phenotypes of mccd. Genetics in Medicine, 17:660-667, Aug 2015. URL: https://doi.org/10.1038/gim.2014.157, doi:10.1038/gim.2014.157. This article has 19 citations and is from a highest quality peer-reviewed journal.

21. (thomsen2015islcarnitinesupplementation pages 1-2): Jákup Andreas Thomsen, Allan Meldgaard Lund, Jess Have Olesen, Magni Mohr, and Jan Rasmussen. Is l-carnitine supplementation beneficial in 3-methylcrotonyl-coa carboxylase deficiency? JIMD reports, 21:79-88, Jan 2015. URL: https://doi.org/10.1007/8904\_2014\_393, doi:10.1007/8904\_2014\_393. This article has 23 citations and is from a peer-reviewed journal.

22. (thomsen2015islcarnitinesupplementation pages 4-5): Jákup Andreas Thomsen, Allan Meldgaard Lund, Jess Have Olesen, Magni Mohr, and Jan Rasmussen. Is l-carnitine supplementation beneficial in 3-methylcrotonyl-coa carboxylase deficiency? JIMD reports, 21:79-88, Jan 2015. URL: https://doi.org/10.1007/8904\_2014\_393, doi:10.1007/8904\_2014\_393. This article has 23 citations and is from a peer-reviewed journal.

23. (thomsen2015islcarnitinesupplementation pages 7-8): Jákup Andreas Thomsen, Allan Meldgaard Lund, Jess Have Olesen, Magni Mohr, and Jan Rasmussen. Is l-carnitine supplementation beneficial in 3-methylcrotonyl-coa carboxylase deficiency? JIMD reports, 21:79-88, Jan 2015. URL: https://doi.org/10.1007/8904\_2014\_393, doi:10.1007/8904\_2014\_393. This article has 23 citations and is from a peer-reviewed journal.

24. (thomsen2015islcarnitinesupplementation pages 8-9): Jákup Andreas Thomsen, Allan Meldgaard Lund, Jess Have Olesen, Magni Mohr, and Jan Rasmussen. Is l-carnitine supplementation beneficial in 3-methylcrotonyl-coa carboxylase deficiency? JIMD reports, 21:79-88, Jan 2015. URL: https://doi.org/10.1007/8904\_2014\_393, doi:10.1007/8904\_2014\_393. This article has 23 citations and is from a peer-reviewed journal.

25. (jagadish2023auniquepresentation pages 1-4): Ashwin Jagadish, Kaitlin Sclater, Taylor Lapinski, Karen Adkins, and Lauren Selzer. A unique presentation of 3-methylcrotonyl-coa carboxylase deficiency. Cureus, May 2023. URL: https://doi.org/10.7759/cureus.39401, doi:10.7759/cureus.39401. This article has 0 citations.

26. (jagadish2023auniquepresentation pages 4-5): Ashwin Jagadish, Kaitlin Sclater, Taylor Lapinski, Karen Adkins, and Lauren Selzer. A unique presentation of 3-methylcrotonyl-coa carboxylase deficiency. Cureus, May 2023. URL: https://doi.org/10.7759/cureus.39401, doi:10.7759/cureus.39401. This article has 0 citations.

27. (zhou2024structuralinsightsinto pages 1-4): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 9 citations.

28. (zhou2024structuralinsightsinto pages 7-9): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 9 citations.

29. (zhou2024structuralinsightsinto pages 6-7): Fayang Zhou, Yuanyuan Zhang, Yuyao Zhu, Qiang Zhou, Yigong Shi, and Qiuyu Hu. Structural insights into human propionyl-coa carboxylase (pcc) and 3-methylcrotonyl-coa carboxylase (mcc). bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.04.30.591959, doi:10.1101/2024.04.30.591959. This article has 9 citations.

30. (lee2018clinicalmanifestationsgene pages 1-3): HanByul Lee, Bomi Lee, So Yoon Jung, Jeongho Lee, Yong Hee Hong, and Dong Hwan Lee. Clinical manifestations, gene analysis of patients with 3-methylcrotonyl-coa carboxylase deficiency. Soonchunhyang Medical Science, 24:55-58, Jun 2018. URL: https://doi.org/10.15746/sms.18.009, doi:10.15746/sms.18.009. This article has 0 citations.

31. (zanatta2013neurochemicalevidencethat pages 1-2): Ângela Zanatta, Alana Pimentel Moura, Anelise Miotti Tonin, Lisiane Aurélio Knebel, Mateus Grings, Vannessa Araújo Lobato, César Augusto João Ribeiro, Carlos Severo Dutra-Filho, Guilhian Leipnitz, and Moacir Wajner. Neurochemical evidence that the metabolites accumulating in 3-methylcrotonyl-coa carboxylase deficiency induce oxidative damage in cerebral cortex of young rats. Cellular and Molecular Neurobiology, 33:137-146, Sep 2013. URL: https://doi.org/10.1007/s10571-012-9879-2, doi:10.1007/s10571-012-9879-2. This article has 15 citations and is from a peer-reviewed journal.

32. (zanatta2013neurochemicalevidencethat pages 7-8): Ângela Zanatta, Alana Pimentel Moura, Anelise Miotti Tonin, Lisiane Aurélio Knebel, Mateus Grings, Vannessa Araújo Lobato, César Augusto João Ribeiro, Carlos Severo Dutra-Filho, Guilhian Leipnitz, and Moacir Wajner. Neurochemical evidence that the metabolites accumulating in 3-methylcrotonyl-coa carboxylase deficiency induce oxidative damage in cerebral cortex of young rats. Cellular and Molecular Neurobiology, 33:137-146, Sep 2013. URL: https://doi.org/10.1007/s10571-012-9879-2, doi:10.1007/s10571-012-9879-2. This article has 15 citations and is from a peer-reviewed journal.

33. (gragnaniello2025psychologicalimpactof pages 1-3): Vincenza Gragnaniello, Giacomo Gaiga, Chiara Cazzorla, Elena Porcù, Daniela Gueraldi, Andrea Puma, Christian Loro, Mara Doimo, Leonardo Salviati, and Alberto B. Burlina. Psychological impact of newborn screening for 3-methylcrotonyl-coa carboxylase deficiency: the parental experience. International Journal of Neonatal Screening, 11:115, Dec 2025. URL: https://doi.org/10.3390/ijns11040115, doi:10.3390/ijns11040115. This article has 0 citations.

34. (lin2024newbornscreeningand pages 2-3): Weihua Lin, Kunyi Wang, Yanru Chen, Zhenzhu Zheng, and Yiming Lin. Newborn screening and genetic diagnosis of 3-methylcrotonyl-coa carboxylase deficiency in quanzhou,china. Molecular Genetics and Metabolism Reports, 40:101127, Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101127, doi:10.1016/j.ymgmr.2024.101127. This article has 5 citations.

35. (mutairi2024outcomesofcases pages 3-4): Fuad Al Mutairi, Randa Alkhalaf, Abdul Rafiq Khan, Ali Al Othaim, and Majid Alfadhel. Outcomes of cases with elevated 3-hydroxyisovaleryl carnitine report from the newborn screening program. Molecular Genetics and Metabolism Reports, 41:101153, Dec 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101153, doi:10.1016/j.ymgmr.2024.101153. This article has 4 citations.

36. (zanatta2013neurochemicalevidencethat pages 2-4): Ângela Zanatta, Alana Pimentel Moura, Anelise Miotti Tonin, Lisiane Aurélio Knebel, Mateus Grings, Vannessa Araújo Lobato, César Augusto João Ribeiro, Carlos Severo Dutra-Filho, Guilhian Leipnitz, and Moacir Wajner. Neurochemical evidence that the metabolites accumulating in 3-methylcrotonyl-coa carboxylase deficiency induce oxidative damage in cerebral cortex of young rats. Cellular and Molecular Neurobiology, 33:137-146, Sep 2013. URL: https://doi.org/10.1007/s10571-012-9879-2, doi:10.1007/s10571-012-9879-2. This article has 15 citations and is from a peer-reviewed journal.

37. (lee2024host–microbeinteractionsrewire pages 1-12): Yong-Uk Lee, Bennett W. Fox, Rui Guo, Brian J. Curtis, Jingfang Yu, Sookyung Kim, Shivani Nanda, Victor Baumann, L. Safak Yilmaz, Cole M. Haynes, Frank C. Schroeder, and Albertha J. M. Walhout. Host–microbe interactions rewire metabolism in a c. elegans model of leucine breakdown deficiency. Nature Metabolism, 6:1584-1600, Aug 2024. URL: https://doi.org/10.1038/s42255-024-01098-5, doi:10.1038/s42255-024-01098-5. This article has 6 citations and is from a domain leading peer-reviewed journal.

38. (NCT03655223 chunk 2):  Early Check: Expanded Screening in Newborns. RTI International. 2018. ClinicalTrials.gov Identifier: NCT03655223

39. (NCT05910151 chunk 1): Zharmakhanova Gulmira. Selective Screening of Children for Hereditary Metabolic Diseases by Tandem Mass Spectrometry in Kazakhstan. West Kazakhstan Medical University. 2022. ClinicalTrials.gov Identifier: NCT05910151
