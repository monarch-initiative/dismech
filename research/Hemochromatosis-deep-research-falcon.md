---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-30T13:32:44.018421'
end_time: '2026-04-30T13:42:53.892011'
duration_seconds: 609.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hemochromatosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemochromatosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hemochromatosis** covering all of the
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
- **Disease Name:** Hemochromatosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hemochromatosis** covering all of the
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


# Hemochromatosis (Hereditary Hemochromatosis; HH) — Comprehensive Disease Characteristics Report (2024–2026 evidence emphasis)

## Executive summary
Hemochromatosis refers to a group of inherited iron-overload disorders in which insufficient hepcidin activity (or resistance to hepcidin) causes inappropriately increased intestinal iron absorption, elevated transferrin saturation (TSAT), generation of toxic non–transferrin-bound iron, and progressive iron deposition in multiple organs. The most common form is HFE-related hereditary hemochromatosis (classically HFE p.Cys282Tyr (C282Y) homozygosity), which is common in Northern European ancestry but has variable/low clinical penetrance; non‑HFE forms are rarer but often more penetrant and may present earlier with severe complications. Standard care is iron removal by phlebotomy with guideline-based ferritin targets; new pharmacologic approaches aim to replace/augment hepcidin signaling or inhibit ferroportin, potentially reducing phlebotomy burden. (girelli2024diagnosisandmanagement pages 1-2, girelli2024diagnosisandmanagement pages 2-4, szczerbinska2024hemochromatosis—hownotto pages 8-10)

---

## 1. Disease information
### 1.1 Definition and overview
- **Disease concept:** HH is a genetic iron overload syndrome characterized by hepcidin insufficiency (or hepcidin resistance) with normal erythropoiesis, leading to iron hyperabsorption, increased TSAT (diagnostic hallmark), formation of non–transferrin-bound iron, and iron deposition in organs (liver, heart, endocrine glands, joints). (girelli2024diagnosisandmanagement pages 1-2)
- **Authoritative definition (abstract quote):** “The term hemochromatosis refers to a group of genetic disorders characterized by hepcidin insufficiency… iron hyperabsorption… increased transferrin saturation, the diagnostic hallmark of the disease.” (Girelli et al., *Hematology* 2024; published Dec 2024; https://doi.org/10.1182/hematology.2024000568) (girelli2024diagnosisandmanagement pages 1-2)

### 1.2 Key identifiers (availability in retrieved sources)
The tool-retrieved corpus for this run did **not** include OMIM/Orphanet/ICD-10/ICD-11/MeSH pages, so those identifiers cannot be cited from primary source documents here.
- **MONDO ID:** not available from the citable evidence retrieved in this run.

### 1.3 Synonyms / alternative names
Common names used in contemporary literature include:
- **Hereditary hemochromatosis (HH)**, **HFE-hemochromatosis (HFE-H)**, **classic hemochromatosis**, **iron overload disease**. (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 1-2)

### 1.4 Evidence provenance
Evidence summarized here is derived from **aggregated disease-level resources** (peer-reviewed reviews/guideline syntheses) and **large population cohorts** (UK Biobank), plus **clinical trial registry** records; it is not derived from individual EHR case reports except where cohort outcomes were ascertained from routine care data linkages. (lucas2024hfegenotypeshaemochromatosis pages 4-5, NCT04202965 chunk 1)

---

## 2. Etiology
### 2.1 Primary causal factors
- **Genetic:**
  - **HFE-related HH** most commonly due to **HFE p.Cys282Tyr (C282Y) homozygosity**. (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hereditaryhemochromatosis–hownot pages 8-9)
  - **Non‑HFE HH** includes defects in **hepcidin synthesis/regulation** (e.g., HJV, HAMP, TFR2) and **hepcidin resistance** (e.g., SLC40A1/ferroportin). (szczerbinska2024hemochromatosis—hownotto pages 8-10, girelli2024diagnosisandmanagement pages 2-4)
- **Mechanistic:** dysregulation of the **hepcidin–ferroportin axis** is central, leading to increased iron export into plasma and increased intestinal absorption. (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 1-2)

### 2.2 Risk factors (genetic and environmental/lifestyle)
- **Sex** is a major modifier: HFE-H has “low penetrance, particularly in females.” (Girelli et al., *Hematology* 2024; Dec 2024; https://doi.org/10.1182/hematology.2024000568) (girelli2024diagnosisandmanagement pages 1-2)
- **Lifestyle/metabolic cofactors** modulate clinical expression; HFE-H can be considered “multifactorial” with “genetic and lifestyle cofactors (especially alcohol and dysmetabolic features)” influencing phenotypic expression. (girelli2024diagnosisandmanagement pages 1-2, girelli2024diagnosisandmanagement pages 2-4)

### 2.3 Protective factors
- A commonly cited physiologic protection in females is iron loss through menstruation/pregnancy; contemporary reviews emphasize lower penetrance in females, consistent with this biological mechanism. (girelli2024diagnosisandmanagement pages 1-2)

### 2.4 Gene–environment interactions
HFE-H is explicitly described as resembling a multifactorial condition because **environmental and metabolic factors** (e.g., alcohol, coexisting metabolic liver disease) interact with **HFE genotype** to determine penetrance and severity. (girelli2024diagnosisandmanagement pages 2-4)

---

## 3. Phenotypes (clinical features) and HPO mappings
### 3.1 Core phenotype spectrum (disease-level)
HH can cause multisystem iron deposition with manifestations in:
- **Liver:** iron overload, fibrosis/cirrhosis, hepatocellular carcinoma (HCC) risk in advanced fibrosis/cirrhosis. (girelli2024diagnosisandmanagement pages 2-4, marcon2024tsaturatedinsightsclarifying pages 16-17)
- **Musculoskeletal:** arthropathy and increased joint replacement incidence in p.C282Y homozygotes in community cohorts. (lucas2024hfegenotypeshaemochromatosis pages 4-5, lucas2024hfegenotypeshaemochromatosis pages 7-7)
- **Endocrine/metabolic:** diabetes risk increased in male p.C282Y homozygotes in UK Biobank outcomes. (lucas2024hfegenotypeshaemochromatosis pages 6-7)
- **Neurologic (association signals):** delirium/dementia/Parkinson’s disease associations reported in UK Biobank analyses (interpretation cautious due to multiple-testing). (lucas2024hfegenotypeshaemochromatosis pages 6-7)

### 3.2 Phenotype timing and progression
- **Typical onset:** adult-onset is typical for HFE-H; non-HFE forms can present earlier and more severely (e.g., juvenile forms). (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 8-10)

### 3.3 Quantitative phenotype frequencies / statistics (UK Biobank; BMJ Open 2024)
From a large prospective cohort with outcomes to age 80:
- **Male p.C282Y homozygotes:** cumulative incidence of **diagnosed hemochromatosis ~56.4%** by age 80, and **higher all-cause mortality** (HR 1.29; 95% CI 1.12–1.48) with **cumulative death incidence 33.1% vs 25.4%** in those without HFE variants. (Lucas et al., *BMJ Open*; published Mar 2024; https://doi.org/10.1136/bmjopen-2023-081926) (lucas2024hfegenotypeshaemochromatosis pages 4-5)
- **Women p.C282Y homozygotes:** cumulative incidence of **diagnosed hemochromatosis 40.5%** by age 80. (lucas2024hfegenotypeshaemochromatosis pages 6-7)
- **Genotypes with low penetrance:** p.C282Y/p.H63D and p.H63D+/+ showed low diagnosis cumulative incidences (~5.4% in men and ~2.7% in women for compound heterozygotes; ~1.9% for H63D homozygosity). (lucas2024hfegenotypeshaemochromatosis pages 7-7)

### 3.4 Suggested HPO terms (examples)
(These are ontology mapping suggestions for knowledge base normalization.)
- Elevated transferrin saturation: **HP:0012467** (Abnormal iron saturation) (map conceptually to TSAT elevation) (supported conceptually by TSAT as hallmark) (girelli2024diagnosisandmanagement pages 1-2)
- Hyperferritinemia: **HP:0003281** (supported by diagnostic role of ferritin) (girelli2024diagnosisandmanagement pages 2-4)
- Hepatic iron overload: **HP:0003280** (supported by MRI/LIC role and hepatic deposition) (szczerbinska2024hemochromatosis—hownotto pages 8-10)
- Liver fibrosis/cirrhosis: **HP:0001395** (supported by increased fibrosis/cirrhosis risk) (lucas2024hfegenotypeshaemochromatosis pages 6-7)
- Diabetes mellitus: **HP:0000819** (supported by increased diabetes incidence in male p.C282Y homozygotes) (lucas2024hfegenotypeshaemochromatosis pages 6-7)
- Arthropathy / joint disease: **HP:0002829** (supported by increased joint replacement risk) (lucas2024hfegenotypeshaemochromatosis pages 4-5)
- Fatigue: **HP:0012378** (supported by baseline fatigue signal in older male homozygotes) (lucas2024hfegenotypeshaemochromatosis pages 4-5)

### 3.5 Quality of life impact
Direct QoL instrument data (e.g., SF-36/EQ-5D) were not retrieved in the citable evidence set for this run; however, symptoms such as fatigue and joint disease are plausibly QoL-limiting, and fatigue associations were directly quantified in UK Biobank (baseline OR in older men). (lucas2024hfegenotypeshaemochromatosis pages 4-5)

---

## 4. Genetic / molecular information
### 4.1 Causal genes (major)
- **HFE** (type 1, classic), **HJV**, **HAMP**, **TFR2**, **SLC40A1** (non-HFE forms including juvenile hemochromatosis and ferroportin disease spectrum). (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 8-10, girelli2024diagnosisandmanagement pages 2-4)

### 4.2 Key pathogenic variants and genotype interpretation
- HFE-H is strongly linked to **HFE p.Cys282Tyr (C282Y) homozygosity**, which is common in Northern European ancestry but has variable clinical penetrance. (girelli2024diagnosisandmanagement pages 1-2)
- BIOIRON-aligned interpretation emphasizes **C282Y homozygosity** as the pathogenic HFE genotype for HFE-related HH, with substantial debate/variation in how other HFE genotypes should be managed. (marcon2024tsaturatedinsightsclarifying pages 1-2, marcon2024tsaturatedinsightsclarifying pages 16-17)

### 4.3 Modifier genetics (polygenic effects)
A recent UK Biobank analysis (preprint) suggests a **polygenic score for TSAT** modifies clinical penetrance among C282Y homozygotes, with higher genetically predicted TSAT increasing clinical outcome incidence; this requires peer-reviewed validation. (lucas2025geneticandlifestyle pages 12-15)

### 4.4 Functional consequences (current understanding)
Across HH types, the shared physiological consequence is **inappropriately low hepcidin effect** relative to body iron, leading to increased plasma iron and tissue deposition. (girelli2024diagnosisandmanagement pages 1-2, girelli2024diagnosisandmanagement pages 2-4)

### 4.5 Epigenetics / chromosomal abnormalities
No epigenetic or chromosomal-abnormality evidence specific to HH was retrieved in the citable set for this run.

---

## 5. Mechanism / pathophysiology
### 5.1 Causal chain (high-level)
1) **Genetic defect** (HFE or non-HFE hepcidin pathway genes) → 2) **Hepcidin insufficiency or resistance** → 3) **Increased ferroportin-mediated iron export + increased intestinal iron absorption** → 4) **High TSAT and non–transferrin-bound iron formation** → 5) **Parenchymal iron deposition** (liver, heart, endocrine glands, joints) → 6) **Oxidative injury and organ dysfunction**. (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 1-2)

### 5.2 Pathways and processes (ontology suggestions)
- **Key pathway:** hepcidin–ferroportin axis / systemic iron homeostasis. (girelli2024diagnosisandmanagement pages 1-2)
- **Suggested GO biological process terms:**
  - Iron ion homeostasis (**GO:0055072**)
  - Cellular iron ion homeostasis (**GO:0006879**)
  - Regulation of hepcidin production (conceptual mapping; hepcidin insufficiency is central) (girelli2024diagnosisandmanagement pages 1-2)
- **Suggested cell types (Cell Ontology, CL) implicated by organ deposition and regulation discussions:**
  - Hepatocyte (**CL:0000182**) (hepcidin production context) (girelli2024diagnosisandmanagement pages 1-2)
  - Macrophage / Kupffer cell (**CL:0000235** / liver macrophage) (iron handling in liver; discussed as important in regulation frameworks) (girelli2024diagnosisandmanagement pages 2-4)
  - Enterocyte (**CL:0000584**) (intestinal absorption) (szczerbinska2024hemochromatosis—hownotto pages 1-2)

### 5.3 Immune/inflammation involvement
While ferritin is noted to be nonspecific and increased in inflammatory states (confounding differential diagnosis), direct immune-pathogenesis evidence was not central in the retrieved set beyond this diagnostic confounding. (girelli2024diagnosisandmanagement pages 2-4)

### 5.4 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic disease signatures were retrieved as citable evidence in this run.

---

## 6. Anatomical structures affected (UBERON suggestions)
- **Liver (primary):** **UBERON:0002107** (hepatic iron loading; fibrosis/cirrhosis/HCC surveillance considerations). (girelli2024diagnosisandmanagement pages 2-4, lucas2024hfegenotypeshaemochromatosis pages 6-7)
- **Heart:** **UBERON:0000948** (iron deposition cited as part of multisystem accumulation). (girelli2024diagnosisandmanagement pages 1-2)
- **Endocrine glands/pancreas:** **UBERON:0001264** (pancreas; diabetes association) (girelli2024diagnosisandmanagement pages 1-2, lucas2024hfegenotypeshaemochromatosis pages 6-7)
- **Joints/synovium:** **UBERON:0002206** (synovial joint) (girelli2024diagnosisandmanagement pages 1-2)

**Subcellular (GO cellular component suggestions):** lysosome (**GO:0005764**) and mitochondrion (**GO:0005739**) are plausible sites of iron-related oxidative injury, but specific subcellular localization evidence was not retrieved in the citable set.

---

## 7. Inheritance and population
### 7.1 Inheritance patterns
- **HFE-H (type 1):** typically **autosomal recessive**. (girelli2024diagnosisandmanagement pages 1-2)
- **Non-HFE juvenile forms (HJV/HAMP/TFR2):** **autosomal recessive**. (szczerbinska2024hemochromatosis—hownotto pages 8-10, girelli2024diagnosisandmanagement pages 2-4)
- **Ferroportin-related (SLC40A1):** often **autosomal dominant** with hepcidin resistance phenotypes described. (szczerbinska2024hemochromatosis—hownotto pages 8-10)

### 7.2 Population frequency and penetrance (recent synthesis)
- **Prevalence of genetic risk genotype:** HFE C282Y homozygosity is described as present in “nearly 1 in 200 people of Northern European descent.” (Girelli et al., *Hematology* 2024; Dec 2024; https://doi.org/10.1182/hematology.2024000568) (girelli2024diagnosisandmanagement pages 1-2)
- **Clinical penetrance is variable/low:** review syntheses emphasize variable penetrance and diagnostic complexity. (marcon2024tsaturatedinsightsclarifying pages 1-2, girelli2024diagnosisandmanagement pages 1-2)

---

## 8. Diagnostics
### 8.1 Core laboratory hallmarks
- **TSAT** is the “diagnostic hallmark” in HH definitions; thresholds around **>45–50%** are commonly used to trigger evaluation. (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 8-10)
- **Ferritin** is used to quantify iron burden but is nonspecific and can be elevated in inflammation, cytolysis, or metabolic conditions. (girelli2024diagnosisandmanagement pages 2-4)

### 8.2 Guideline elements and algorithms (visual evidence from a 2024 guideline synthesis)
The Marcon et al. 2024 review provides comparative tables and an algorithm that summarize guideline differences for diagnosis and phlebotomy targets:
- **Table comparing diagnostic elements (TSAT/SF cutoffs) across guidelines** and **Table comparing treatment targets** (including induction and maintenance serum ferritin goals). (marcon2024tsaturatedinsightsclarifying media 39ab28d3, marcon2024tsaturatedinsightsclarifying media 7ecf4a95)
- **Diagnostic/management algorithm (figure)** for HFE-related HH and **differential diagnosis approach to hyperferritinemia**. (marcon2024tsaturatedinsightsclarifying media f71af5e5, marcon2024tsaturatedinsightsclarifying media 8a05bd9e)

### 8.3 Imaging and biopsy
- **MRI** is highlighted as a reference/essential technique for hepatic iron quantification and staging in contemporary practice; liver biopsy is described as rarely required in modern workups except selected cases. (marcon2024tsaturatedinsightsclarifying pages 16-17, szczerbinska2024hemochromatosis—hownotto pages 8-10)

### 8.4 Genetic testing strategy
- HFE accounts for the vast majority of hereditary cases; genetic testing is described as the “gold standard diagnostic test,” with initial biochemical screening by TSAT and ferritin. (nogueyra2024thegeneticdiagnostics pages 3-4)
- If C282Y is absent but iron overload is present, reviews recommend considering **gene panels** for non‑HFE etiologies after excluding common secondary causes (e.g., metabolic liver disease, alcohol-associated liver disease). (szczerbinska2024hemochromatosis—hownotto pages 8-10, szczerbinska2024hereditaryhemochromatosis–hownot pages 9-11)

### 8.5 Differential diagnosis (high level)
- Hyperferritinemia with **normal TSAT** is often not HH and may reflect metabolic/inflammatory etiologies; specialist evaluation is recommended in such patterns. (girelli2024diagnosisandmanagement pages 2-4)

---

## 9. Outcomes / prognosis
### 9.1 Prognosis with early treatment
- Reviews emphasize that contemporary HFE-H is “mostly diagnosed before organ damage and is easily treated by phlebotomy, with an excellent prognosis.” (Girelli et al., *Hematology* 2024; Dec 2024; https://doi.org/10.1182/hematology.2024000568) (girelli2024diagnosisandmanagement pages 1-2)

### 9.2 Morbidity and mortality statistics (UK Biobank)
- Male p.C282Y homozygotes showed **increased all-cause mortality** (HR 1.29; cumulative deaths 33.1% vs 25.4% by age 80) and increased liver/joint/other outcomes. (lucas2024hfegenotypeshaemochromatosis pages 4-5)
- These outcome signals were also seen among individuals **undiagnosed at baseline**, supporting under-recognition in routine care. (lucas2024hfegenotypeshaemochromatosis pages 4-5)

---

## 10. Treatment
### 10.1 Standard-of-care: phlebotomy (venesection)
- **First-line therapy:** repeated therapeutic phlebotomy (venesection), commonly ~450–500 mL per session. (marcon2024tsaturatedinsightsclarifying pages 16-17, szczerbinska2024hereditaryhemochromatosis–hownot pages 9-11)
- **Example induction/maintenance targets from cited EASL-aligned summaries:** ferritin targets often include **<50 µg/L during induction** and **<100 µg/L during maintenance**; TSAT is not necessarily a treatment target in some guidelines. (szczerbinska2024hereditaryhemochromatosis–hownot pages 9-11)
- A 2024 synthesis includes comparative guideline tables for phlebotomy targets (induction and maintenance) and a diagnostic/treatment algorithm. (marcon2024tsaturatedinsightsclarifying media 39ab28d3, marcon2024tsaturatedinsightsclarifying media 7ecf4a95, marcon2024tsaturatedinsightsclarifying media f71af5e5)

### 10.2 Blood donation as real-world implementation
After iron depletion, maintenance phlebotomy “can be usefully transformed into a blood donation program,” representing a practical implementation pathway in suitable health systems. (girelli2024diagnosisandmanagement pages 1-2)

### 10.3 Chelation therapy (selected indications)
Chelation is generally reserved for patients who cannot undergo phlebotomy or are refractory/intolerant, due to toxicity and limited evidence relative to phlebotomy. (nogueyra2024thegeneticdiagnostics pages 3-4, marcon2024tsaturatedinsightsclarifying pages 31-31)

### 10.4 Emerging / investigational therapies (2023–2026)
#### Hepcidin mimetic / hepcidin-pathway augmentation
- **Rusfertide (PTG‑300):** ClinicalTrials.gov describes a **Phase 2**, open-label, single-arm study in adults with HFE-related HH (**NCT04202965**), **completed**, with **results first posted 2023‑06‑15**. Primary endpoints included change in **TSAT and serum iron** to Week 24, and a key secondary endpoint was **change in phlebotomy frequency** over 24 weeks pre vs on treatment. (ClinicalTrials.gov; posted results 2023-06-15; https://clinicaltrials.gov/study/NCT04202965) (NCT04202965 chunk 1)

#### Ferroportin inhibition
- **Vamifeport:** A Phase 2 interventional trial record exists for HFE-related HH (**NCT07332091**, CSL Behring) with a record version date **2026‑04‑30** and multiple European sites listed as not yet recruiting in the extracted chunk; additional registry chunks are needed for endpoints/dosing. (ClinicalTrials.gov; https://clinicaltrials.gov/study/NCT07332091) (NCT07332091 chunk 4)

### 10.5 MAXO term suggestions
- Therapeutic phlebotomy / venesection: **MAXO:0000449** (therapeutic phlebotomy; conceptual mapping)
- Iron chelation therapy: **MAXO:0000755** (chelation therapy; conceptual mapping)
- Genetic counseling/cascade testing: **MAXO:0000079** (genetic counseling; conceptual mapping)

---

## 11. Prevention
### 11.1 Secondary prevention: early detection and intervention
- The disease evolves over decades and is highly amenable to preventing complications via early recognition and venesection, motivating screening discussions. (delatycki2024populationscreeningfor pages 1-2, girelli2024diagnosisandmanagement pages 1-2)

### 11.2 Screening strategies (2024 expert analyses)
- **Population screening (expert argument in favor):** Delatycki & Allen (2024) argue HH is a strong candidate for population genetic screening because early intervention is simple and effective, and may expand the blood donor pool; they discuss genotype vs phenotype screening tradeoffs and conclude it is timely to reconsider genotype-based strategies focusing on C282Y. (Delatycki & Allen, *Genes*; Jul 2024; https://doi.org/10.3390/genes15080967) (delatycki2024populationscreeningfor pages 1-2, delatycki2024populationscreeningfor pages 4-5, delatycki2024populationscreeningfor pages 5-6)
- **Caution/targeted screening:** Another 2024 review emphasizes underdiagnosis but suggests targeted screening (e.g., higher-risk ancestry/sex subgroups) rather than universal screening, partly due to lower-than-expected penetrance. (szczerbinska2024hemochromatosis—hownotto pages 13-14)

### 11.3 Cascade screening and counseling
- Family screening for first-degree relatives is repeatedly recommended/implicit in diagnostic frameworks because of the inherited nature and actionable intervention. (szczerbinska2024hereditaryhemochromatosis–hownot pages 9-11)

---

## 12. Other species / natural disease
No veterinary/natural disease evidence (OMIA/VetCompass) was retrieved in the citable set for this run.

---

## 13. Model organisms
No model organism-specific primary studies were retrieved in the citable set for this run.

---

## 14. Structured summary artifact (genes/types)
The following table summarizes major HH types, genes, inheritance, and mechanistic class.

| Hemochromatosis type | Major causal gene(s) | Usual inheritance | Core mechanistic defect | Typical onset / severity | Key notes |
|---|---|---|---|---|---|
| Type 1 (classic HFE-related hemochromatosis) | **HFE**; most commonly p.Cys282Tyr (C282Y) homozygosity | Autosomal recessive | Relative **hepcidin deficiency** causing increased intestinal iron absorption, increased transferrin saturation, and parenchymal iron loading | Usually **adult-onset**; common in Northern European ancestry; often **low clinical penetrance**, especially in females, but strong biochemical penetrance (girelli2024diagnosisandmanagement pages 1-2, girelli2024diagnosisandmanagement pages 2-4, szczerbinska2024hemochromatosis—hownotto pages 1-2) | Most common form; diagnostic hallmark is elevated TSAT; phlebotomy is standard treatment; BIOIRON classification emphasizes C282Y homozygosity as the pathogenic HFE genotype for HFE-related HH (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hereditaryhemochromatosis–hownot pages 8-9) |
| Type 2A (juvenile hemochromatosis) | **HJV** | Autosomal recessive | Severe **hepcidin deficiency** | **Juvenile or early adult onset**; typically **severe**, with early endocrine, hepatic, and cardiac complications (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 8-10, girelli2024diagnosisandmanagement pages 2-4) | Non-HFE form; much rarer but more penetrant than HFE-H; can present with very low/undetectable hepcidin (girelli2024diagnosisandmanagement pages 1-2, girelli2024diagnosisandmanagement pages 2-4) |
| Type 2B (juvenile hemochromatosis) | **HAMP** | Autosomal recessive | Direct **hepcidin deficiency** due to hepcidin gene defects | **Juvenile or early adult onset**; typically **severe** and rapidly progressive (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 8-10, girelli2024diagnosisandmanagement pages 2-4) | Rare non-HFE HH; often grouped with HJV-related juvenile disease because both produce profound hepcidin deficiency (girelli2024diagnosisandmanagement pages 1-2, girelli2024diagnosisandmanagement pages 2-4) |
| Type 3 | **TFR2** | Autosomal recessive | **Hepcidin deficiency** due to impaired iron sensing/signaling | Often **adult or earlier-than-HFE onset**; can be **severe** (szczerbinska2024hemochromatosis—hownotto pages 8-10, girelli2024diagnosisandmanagement pages 2-4) | Rare non-HFE HH; included in gene-panel testing when C282Y is absent and iron overload is present after secondary causes are excluded (szczerbinska2024hemochromatosis—hownotto pages 8-10, szczerbinska2024hereditaryhemochromatosis–hownot pages 8-9) |
| Type 4 / ferroportin disease (non-classic hemochromatosis spectrum) | **SLC40A1** | Usually autosomal dominant | Either defective ferroportin export phenotype or **hepcidin resistance**; hemochromatosis phenotype classically linked to **hepcidin resistance** | Variable; can be **adult-onset**; severity varies by subtype (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 8-10) | Distinct from classic HFE-H; SLC40A1-related disease may present differently from hepcidin-deficiency states and should be considered in non-HFE evaluation (girelli2024diagnosisandmanagement pages 1-2, szczerbinska2024hemochromatosis—hownotto pages 8-10) |
| Rare/expanded non-HFE differential within iron-overload workup | Rare **HFE** variants and broader iron genes in panels (e.g., CP, BMP6, TF, FTL in some diagnostic panels) | Variable | Variable; may affect hepcidin regulation or mimic HH | Variable; depends on gene and context (szczerbinska2024hereditaryhemochromatosis–hownot pages 9-11, szczerbinska2024hemochromatosis—hownotto pages 8-10) | Not all genes in expanded panels define classical hereditary hemochromatosis; testing is generally recommended only after exclusion of common secondary causes and common HFE genotypes (szczerbinska2024hereditaryhemochromatosis–hownot pages 9-11, szczerbinska2024hemochromatosis—hownotto pages 8-10, szczerbinska2024hereditaryhemochromatosis–hownot pages 8-9) |


*Table: This table summarizes the major hereditary hemochromatosis subtypes, their causal genes, inheritance patterns, core pathophysiology, and typical clinical presentation. It is useful as a compact reference for distinguishing classic HFE-related disease from rarer, often more penetrant non-HFE forms.*

---

## 15. Notes on evidence gaps in this run
- **Ontology identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO)** were not retrievable as citable sources in this run; a follow-up retrieval targeting those databases would be required to populate identifiers with citations.
- **Detailed omics, epigenetic findings, animal models**, and **QoL instrument-based outcomes** were not retrieved in the citable evidence set for this run.

---

## Key recent sources (with URLs and publication dates)
- Girelli D, Marchi G, Busti F. *Diagnosis and management of hereditary hemochromatosis: lifestyle modification, phlebotomy, and blood donation*. **Hematology**. **Dec 2024**. https://doi.org/10.1182/hematology.2024000568 (girelli2024diagnosisandmanagement pages 1-2, girelli2024diagnosisandmanagement pages 2-4)
- Lucas MR et al. *HFE genotypes, haemochromatosis diagnosis and clinical outcomes at age 80 years: a prospective cohort study in the UK Biobank*. **BMJ Open**. **Mar 2024**. https://doi.org/10.1136/bmjopen-2023-081926 (lucas2024hfegenotypeshaemochromatosis pages 4-5)
- Marcon C et al. *TSAT-Urated Insights: Clarifying the Complexities of Hereditary Hemochromatosis and Its Guidelines*. **Hemato**. **Dec 2024**. https://doi.org/10.3390/hemato5040035 (marcon2024tsaturatedinsightsclarifying pages 16-17, marcon2024tsaturatedinsightsclarifying media 39ab28d3, marcon2024tsaturatedinsightsclarifying media 7ecf4a95, marcon2024tsaturatedinsightsclarifying media f71af5e5, marcon2024tsaturatedinsightsclarifying media 8a05bd9e, marcon2024tsaturatedinsightsclarifying pages 1-2)
- Delatycki MB, Allen KJ. *Population Screening for Hereditary Haemochromatosis—Should It Be Carried Out, and If So, How?* **Genes**. **Jul 2024**. https://doi.org/10.3390/genes15080967 (delatycki2024populationscreeningfor pages 1-2, delatycki2024populationscreeningfor pages 4-5)
- ClinicalTrials.gov. **NCT04202965** (rusfertide/PTG‑300), results first posted **2023‑06‑15**. https://clinicaltrials.gov/study/NCT04202965 (NCT04202965 chunk 1)
- ClinicalTrials.gov. **NCT07332091** (vamifeport), record version **2026‑04‑30**. https://clinicaltrials.gov/study/NCT07332091 (NCT07332091 chunk 4)


References

1. (girelli2024diagnosisandmanagement pages 1-2): Domenico Girelli, Giacomo Marchi, and Fabiana Busti. Diagnosis and management of hereditary hemochromatosis: lifestyle modification, phlebotomy, and blood donation. Hematology, 2024:434-442, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000568, doi:10.1182/hematology.2024000568. This article has 22 citations and is from a peer-reviewed journal.

2. (girelli2024diagnosisandmanagement pages 2-4): Domenico Girelli, Giacomo Marchi, and Fabiana Busti. Diagnosis and management of hereditary hemochromatosis: lifestyle modification, phlebotomy, and blood donation. Hematology, 2024:434-442, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000568, doi:10.1182/hematology.2024000568. This article has 22 citations and is from a peer-reviewed journal.

3. (szczerbinska2024hemochromatosis—hownotto pages 8-10): Agnieszka Szczerbinska, Beata Kasztelan-Szczerbinska, Anna Rycyk-Bojarzynska, Janusz Kocki, and Halina Cichoz-Lach. Hemochromatosis—how not to overlook and properly manage “iron people”—a review. Journal of Clinical Medicine, 13:3660, Jun 2024. URL: https://doi.org/10.3390/jcm13133660, doi:10.3390/jcm13133660. This article has 14 citations.

4. (szczerbinska2024hemochromatosis—hownotto pages 1-2): Agnieszka Szczerbinska, Beata Kasztelan-Szczerbinska, Anna Rycyk-Bojarzynska, Janusz Kocki, and Halina Cichoz-Lach. Hemochromatosis—how not to overlook and properly manage “iron people”—a review. Journal of Clinical Medicine, 13:3660, Jun 2024. URL: https://doi.org/10.3390/jcm13133660, doi:10.3390/jcm13133660. This article has 14 citations.

5. (lucas2024hfegenotypeshaemochromatosis pages 4-5): Mitchell R Lucas, Janice L Atkins, Luke C Pilling, Jeremy D Shearman, and David Melzer. Hfe genotypes, haemochromatosis diagnosis and clinical outcomes at age 80 years: a prospective cohort study in the uk biobank. BMJ Open, 14:e081926, Mar 2024. URL: https://doi.org/10.1136/bmjopen-2023-081926, doi:10.1136/bmjopen-2023-081926. This article has 42 citations and is from a peer-reviewed journal.

6. (NCT04202965 chunk 1):  PTG-300 in Subjects With Hereditary Hemochromatosis. Protagonist Therapeutics, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04202965

7. (szczerbinska2024hereditaryhemochromatosis–hownot pages 8-9): A Szczerbinska and B Kasztelan-Szczerbinska. Hereditary hemochromatosis–how not to overlook and properly manage “iron people”-a critical overview. Unknown journal, 2024.

8. (marcon2024tsaturatedinsightsclarifying pages 16-17): Chiara Marcon, Marta Medeot, Alessio Michelazzi, Valentina Simeon, Alessandra Poz, Sara Cmet, Elisabetta Fontanini, Anna Rosa Cussigh, Marianna Chiozzotto, and Giovanni Barillari. Tsat-urated insights: clarifying the complexities of hereditary hemochromatosis and its guidelines. Hemato, 5:459-489, Dec 2024. URL: https://doi.org/10.3390/hemato5040035, doi:10.3390/hemato5040035. This article has 2 citations.

9. (lucas2024hfegenotypeshaemochromatosis pages 7-7): Mitchell R Lucas, Janice L Atkins, Luke C Pilling, Jeremy D Shearman, and David Melzer. Hfe genotypes, haemochromatosis diagnosis and clinical outcomes at age 80 years: a prospective cohort study in the uk biobank. BMJ Open, 14:e081926, Mar 2024. URL: https://doi.org/10.1136/bmjopen-2023-081926, doi:10.1136/bmjopen-2023-081926. This article has 42 citations and is from a peer-reviewed journal.

10. (lucas2024hfegenotypeshaemochromatosis pages 6-7): Mitchell R Lucas, Janice L Atkins, Luke C Pilling, Jeremy D Shearman, and David Melzer. Hfe genotypes, haemochromatosis diagnosis and clinical outcomes at age 80 years: a prospective cohort study in the uk biobank. BMJ Open, 14:e081926, Mar 2024. URL: https://doi.org/10.1136/bmjopen-2023-081926, doi:10.1136/bmjopen-2023-081926. This article has 42 citations and is from a peer-reviewed journal.

11. (marcon2024tsaturatedinsightsclarifying pages 1-2): Chiara Marcon, Marta Medeot, Alessio Michelazzi, Valentina Simeon, Alessandra Poz, Sara Cmet, Elisabetta Fontanini, Anna Rosa Cussigh, Marianna Chiozzotto, and Giovanni Barillari. Tsat-urated insights: clarifying the complexities of hereditary hemochromatosis and its guidelines. Hemato, 5:459-489, Dec 2024. URL: https://doi.org/10.3390/hemato5040035, doi:10.3390/hemato5040035. This article has 2 citations.

12. (lucas2025geneticandlifestyle pages 12-15): Mitchell R Lucas, João Delgado, Robin N Beaumont, Gareth Hawkes, Andrew R Wood, Caroline F Wright, Jeremy Shearman, Janice L Atkins, and Luke C Pilling. Genetic and lifestyle modifiers of haemochromatosis-related clinical outcomes in hfe c282y homozygotes: prospective cohort study in uk biobank. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.22.25334187, doi:10.1101/2025.08.22.25334187. This article has 0 citations.

13. (marcon2024tsaturatedinsightsclarifying media 39ab28d3): Chiara Marcon, Marta Medeot, Alessio Michelazzi, Valentina Simeon, Alessandra Poz, Sara Cmet, Elisabetta Fontanini, Anna Rosa Cussigh, Marianna Chiozzotto, and Giovanni Barillari. Tsat-urated insights: clarifying the complexities of hereditary hemochromatosis and its guidelines. Hemato, 5:459-489, Dec 2024. URL: https://doi.org/10.3390/hemato5040035, doi:10.3390/hemato5040035. This article has 2 citations.

14. (marcon2024tsaturatedinsightsclarifying media 7ecf4a95): Chiara Marcon, Marta Medeot, Alessio Michelazzi, Valentina Simeon, Alessandra Poz, Sara Cmet, Elisabetta Fontanini, Anna Rosa Cussigh, Marianna Chiozzotto, and Giovanni Barillari. Tsat-urated insights: clarifying the complexities of hereditary hemochromatosis and its guidelines. Hemato, 5:459-489, Dec 2024. URL: https://doi.org/10.3390/hemato5040035, doi:10.3390/hemato5040035. This article has 2 citations.

15. (marcon2024tsaturatedinsightsclarifying media f71af5e5): Chiara Marcon, Marta Medeot, Alessio Michelazzi, Valentina Simeon, Alessandra Poz, Sara Cmet, Elisabetta Fontanini, Anna Rosa Cussigh, Marianna Chiozzotto, and Giovanni Barillari. Tsat-urated insights: clarifying the complexities of hereditary hemochromatosis and its guidelines. Hemato, 5:459-489, Dec 2024. URL: https://doi.org/10.3390/hemato5040035, doi:10.3390/hemato5040035. This article has 2 citations.

16. (marcon2024tsaturatedinsightsclarifying media 8a05bd9e): Chiara Marcon, Marta Medeot, Alessio Michelazzi, Valentina Simeon, Alessandra Poz, Sara Cmet, Elisabetta Fontanini, Anna Rosa Cussigh, Marianna Chiozzotto, and Giovanni Barillari. Tsat-urated insights: clarifying the complexities of hereditary hemochromatosis and its guidelines. Hemato, 5:459-489, Dec 2024. URL: https://doi.org/10.3390/hemato5040035, doi:10.3390/hemato5040035. This article has 2 citations.

17. (nogueyra2024thegeneticdiagnostics pages 3-4): Sol Villa Nogueyra, María F Trujillo Rodríguez, María L Garcia Oliva, Andrea Vidal-Gallardo, Amanda Ramírez Leal, Jose Beltran Hernandez, Andres Manuel Vargas Beltran, José D Guillen Sandoval, David Arriaga Escamilla, and Marily Martinez Ramirez. The genetic diagnostics of hemochromatosis: disparities in low- versus high-income countries. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.64074, doi:10.7759/cureus.64074. This article has 3 citations.

18. (szczerbinska2024hereditaryhemochromatosis–hownot pages 9-11): A Szczerbinska and B Kasztelan-Szczerbinska. Hereditary hemochromatosis–how not to overlook and properly manage “iron people”-a critical overview. Unknown journal, 2024.

19. (marcon2024tsaturatedinsightsclarifying pages 31-31): Chiara Marcon, Marta Medeot, Alessio Michelazzi, Valentina Simeon, Alessandra Poz, Sara Cmet, Elisabetta Fontanini, Anna Rosa Cussigh, Marianna Chiozzotto, and Giovanni Barillari. Tsat-urated insights: clarifying the complexities of hereditary hemochromatosis and its guidelines. Hemato, 5:459-489, Dec 2024. URL: https://doi.org/10.3390/hemato5040035, doi:10.3390/hemato5040035. This article has 2 citations.

20. (NCT07332091 chunk 4):  Efficacy and Safety of Vamifeport in Adult Participants With Homeostatic Iron Regulator Gene (HFE)-Related Hereditary Hemochromatosis. CSL Behring. 2026. ClinicalTrials.gov Identifier: NCT07332091

21. (delatycki2024populationscreeningfor pages 1-2): Martin B. Delatycki and Katrina J. Allen. Population screening for hereditary haemochromatosis—should it be carried out, and if so, how? Genes, 15:967, Jul 2024. URL: https://doi.org/10.3390/genes15080967, doi:10.3390/genes15080967. This article has 5 citations.

22. (delatycki2024populationscreeningfor pages 4-5): Martin B. Delatycki and Katrina J. Allen. Population screening for hereditary haemochromatosis—should it be carried out, and if so, how? Genes, 15:967, Jul 2024. URL: https://doi.org/10.3390/genes15080967, doi:10.3390/genes15080967. This article has 5 citations.

23. (delatycki2024populationscreeningfor pages 5-6): Martin B. Delatycki and Katrina J. Allen. Population screening for hereditary haemochromatosis—should it be carried out, and if so, how? Genes, 15:967, Jul 2024. URL: https://doi.org/10.3390/genes15080967, doi:10.3390/genes15080967. This article has 5 citations.

24. (szczerbinska2024hemochromatosis—hownotto pages 13-14): Agnieszka Szczerbinska, Beata Kasztelan-Szczerbinska, Anna Rycyk-Bojarzynska, Janusz Kocki, and Halina Cichoz-Lach. Hemochromatosis—how not to overlook and properly manage “iron people”—a review. Journal of Clinical Medicine, 13:3660, Jun 2024. URL: https://doi.org/10.3390/jcm13133660, doi:10.3390/jcm13133660. This article has 14 citations.