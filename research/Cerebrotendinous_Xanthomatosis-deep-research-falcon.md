---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-03T12:01:32.474561'
end_time: '2026-05-03T12:09:06.977396'
duration_seconds: 454.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cerebrotendinous xanthomatosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cerebrotendinous xanthomatosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cerebrotendinous xanthomatosis** covering all of the
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
- **Disease Name:** Cerebrotendinous xanthomatosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cerebrotendinous xanthomatosis** covering all of the
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


# Cerebrotendinous Xanthomatosis (CTX) — Disease Characteristics Research Report

## Target disease
- **Disease name:** Cerebrotendinous xanthomatosis (CTX) (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **Category:** Mendelian / inborn error of metabolism (bile acid synthesis disorder) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **MONDO ID:** **MONDO:0008948** (Open Targets disease mapping) (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview
Cerebrotendinous xanthomatosis (CTX) is a **rare, treatable, autosomal recessive** disorder of bile-acid biosynthesis and lipid storage caused by **biallelic pathogenic variants in *CYP27A1*** (sterol 27-hydroxylase). Enzyme deficiency impairs bile acid synthesis—especially **chenodeoxycholic acid (CDCA)**—and leads to accumulation of **cholestanol** and bile alcohols, with deposition in multiple tissues (brain, lenses, tendons), producing cataracts, tendon xanthomas, and progressive neurologic dysfunction (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, nobrega2022cerebrotendinousxanthomatosisa pages 1-2).

CTX is considered underdiagnosed because early manifestations can be nonspecific and symptom combinations vary across patients, contributing to long diagnostic delays (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, nobrega2022cerebrotendinousxanthomatosisa pages 1-2).

### 1.2 Key identifiers and synonyms
- **OMIM/MIM:** **#213700** (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **MONDO:** **MONDO:0008948** (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **MeSH:** condition mapped as **“Xanthomatosis, Cerebrotendinous”** in ClinicalTrials.gov metadata (NCT04270682 chunk 2)
- **Orphanet / ICD-10 / ICD-11 / MeSH ID numbers:** **not present in retrieved evidence** (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)

Embedded structured identifier summary:
| Identifier item | Value | Source (paper) | Publication year | DOI/URL | Evidence |
|---|---|---|---|---|---|
| Disease name | Cerebrotendinous xanthomatosis | Nóbrega et al., *Frontiers in Neurology* | 2022 | https://doi.org/10.3389/fneur.2022.1049850 | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |
| Abbreviation | CTX | Nóbrega et al., *Frontiers in Neurology* | 2022 | https://doi.org/10.3389/fneur.2022.1049850 | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |
| Alternative name mentioned | Xanthomatosis, Cerebrotendinous | ClinicalTrials.gov condition mapping (RESTORE, NCT04270682) | 2020 record, results metadata posted 2024 | https://clinicaltrials.gov/study/NCT04270682 | (NCT04270682 chunk 2) |
| MONDO ID | MONDO_0008948 | Open Targets disease-target association output | not dated in retrieved evidence | https://platform.opentargets.org | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |
| OMIM/MIM number | MIM #213700 | Nóbrega et al., *Frontiers in Neurology* | 2022 | https://doi.org/10.3389/fneur.2022.1049850 | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |
| Causal gene | CYP27A1 | Koyama et al., *Journal of Atherosclerosis and Thrombosis* | 2021 | https://doi.org/10.5551/jat.rv17055 | (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2) |
| Inheritance | Autosomal recessive | Koyama et al., *Journal of Atherosclerosis and Thrombosis* | 2021 | https://doi.org/10.5551/jat.rv17055 | (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2) |
| Orphanet identifier | not in retrieved evidence | — | — | — | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |
| ICD-10 identifier | not in retrieved evidence | — | — | — | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |
| ICD-11 identifier | not in retrieved evidence | — | — | — | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |
| MeSH identifier | not in retrieved evidence | — | — | — | (nobrega2022cerebrotendinousxanthomatosisa pages 1-2) |


*Table: This table summarizes the core disease identifiers and nomenclature for cerebrotendinous xanthomatosis using only retrieved evidence. It highlights what was directly supported in the evidence set and explicitly marks identifier systems not present in the retrieved materials.*

### 1.3 Synonyms and alternative names
Within retrieved sources, CTX is referenced as “cerebrotendinous xanthomatosis” and as the MeSH condition term “Xanthomatosis, Cerebrotendinous” (NCT04270682 chunk 2, nobrega2022cerebrotendinousxanthomatosisa pages 1-2).

### 1.4 Evidence source types
The information in this report is derived from:
- Aggregated disease-level reviews (practice/integrative reviews) (nobrega2022cerebrotendinousxanthomatosisa pages 1-2, ribeiro2023pathophysiologyandtreatment pages 10-12)
- Aggregated case series/cohort analyses of published cases (duell2018diagnosistreatmentand pages 8-12)
- Human clinical cohorts/case series (diagnosis/treatment outcomes) (duell2018diagnosistreatmentand pages 1-8)
- Recent mechanistic disease modeling using patient iPSCs (mou2023chenodeoxycholicacidrescues pages 1-2)
- ClinicalTrials.gov trial registry records (trial designs and posted dates) (NCT02638220 chunk 1, NCT04270682 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (primary causes)
CTX is primarily caused by **biallelic pathogenic variants in *CYP27A1***, encoding the mitochondrial enzyme **sterol 27-hydroxylase**, which is required for bile acid synthesis (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, koyama2021cerebrotendinousxanthomatosismolecular pages 2-4).

- Abstract-supported causal statement (quote): CTX is “**caused by mutations in the CYP27A1 gene, which encodes the mitochondrial enzyme sterol 27-hydroxylase**” (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

### 2.2 Risk factors
- **Genetic:** autosomal recessive inheritance; disease occurs with homozygous/compound heterozygous loss-of-function *CYP27A1* variants (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, nobrega2022cerebrotendinousxanthomatosisa pages 1-2).
- **Environmental:** no specific environmental causal triggers were identified in retrieved evidence; CTX is best characterized as a genetic inborn error of metabolism (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

### 2.3 Protective factors
No genetic protective variants or environmental protective factors were identified in retrieved evidence.

### 2.4 Gene–environment interactions
No CTX-specific gene–environment interaction evidence was identified in retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (human)
A large case series (43 cases) reports high frequencies of major CTX manifestations:
- **Neurologic disease:** 81% (broadly including progressive neurologic dysfunction) (duell2018diagnosistreatmentand pages 1-8)
- **Tendon xanthomas:** 77% (duell2018diagnosistreatmentand pages 1-8)
- **Cognitive impairment:** 74% (duell2018diagnosistreatmentand pages 1-8)
- **Premature cataracts:** 70% (duell2018diagnosistreatmentand pages 1-8)
- **Chronic diarrhea:** 53% (duell2018diagnosistreatmentand pages 1-8)
- **Premature cardiovascular disease:** 7% (duell2018diagnosistreatmentand pages 1-8)

Clinical features summarized in reviews include neonatal jaundice/cholestasis, refractory diarrhea, juvenile cataracts, tendon xanthomas, osteoporosis, coronary heart disease, and diverse neuropsychiatric manifestations (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

### 3.2 Temporal development / age of onset (natural history)
Across clinical syntheses:
- Typical early manifestations include **infantile/early childhood diarrhea**, with **cataracts** and school/learning difficulties often in childhood, and progressive neurologic disease later (duell2018diagnosistreatmentand pages 8-12, koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).
- In the 43-case series, the authors note that features may begin in infancy (chronic diarrhea) and cataracts in childhood/adolescence; tendon xanthomas often appear in the second–third decades; progressive neurologic disease may contribute to premature death in mid-adulthood if untreated (duell2018diagnosistreatmentand pages 8-12).

### 3.3 Phenotype characteristics and suggested HPO terms
Below are suggested HPO terms for knowledge-base encoding (ontology mapping is expert-derived; frequencies/onset are evidence-based where cited):
- **Chronic diarrhea** — HP:0002028 (often early) (duell2018diagnosistreatmentand pages 1-8)
- **Juvenile/early cataracts** — HP:0000519 (premature cataracts common) (duell2018diagnosistreatmentand pages 1-8, koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **Tendon xanthomas (e.g., Achilles)** — HP:0012066 / (xanthoma) HP:0000991 (duell2018diagnosistreatmentand pages 1-8)
- **Cerebellar ataxia** — HP:0001251 (listed among common neurologic manifestations) (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **Spasticity / pyramidal signs** — HP:0001257 (common neurologic manifestations) (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **Peripheral neuropathy** — HP:0009830 (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **Seizures/epilepsy** — HP:0001250 (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **Cognitive decline / intellectual disability** — HP:0001263 / HP:0001249 (cognitive impairment frequent) (duell2018diagnosistreatmentand pages 1-8, koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **Neuropsychiatric abnormalities** — HP:0000708 (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- **Osteoporosis** — HP:0000939 (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **Neonatal jaundice / cholestasis** — HP:0006579 / HP:0001402 (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)

### 3.4 Quality-of-life impact
CTX can produce progressive neurologic disability and multi-system involvement; bile acid replacement therapy can inhibit deterioration when instituted earlier, supporting major QoL implications of diagnostic delay and treatability (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, ejsmontsowała2024casereportcerebrotendinous pages 1-2).

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene(s)
- **Gene:** *CYP27A1* (sterol 27-hydroxylase) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **Mechanism class:** loss-of-function enzyme deficiency → impaired bile acid synthesis (koyama2021cerebrotendinousxanthomatosismolecular pages 2-4)

### 4.2 Pathogenic variant types and examples (from retrieved evidence)
The retrieved clinical evidence set did not provide a comprehensive variant catalog; however, it supports that **pathogenic *CYP27A1* mutations** (biallelic) cause CTX (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2). (Comprehensive variant spectrum and population allele frequencies would typically be obtained from ClinVar/gnomAD/HGMD; these were not retrieved here.)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No CTX modifier genes, epigenetic mechanisms, or chromosomal abnormalities were identified in retrieved evidence.

---

## 5. Environmental Information
CTX is primarily genetic. No specific toxins, lifestyle exposures, or infectious triggers were supported by retrieved evidence (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Core biochemical pathway defect (bile acid synthesis)
Sterol 27-hydroxylase deficiency impairs bile acid synthesis, particularly reducing CDCA, and results in increased production/accumulation of **cholestanol** and bile alcohols (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, koyama2021cerebrotendinousxanthomatosismolecular pages 2-4). A review describes that decreased sterol 27-hydroxylase activity leads to “**impaired bile acid synthesis, leading to reduced production of bile acids, especially chenodeoxycholic acid (CDCA), as well as elevated serum cholestanol and urine bile alcohols**” (quote) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

Loss of bile-acid negative feedback is associated with compensatory upregulation of bile acid synthetic enzymes and accumulation of intermediate biomarkers such as **7α-hydroxy-4-cholesten-3-one** (koyama2021cerebrotendinousxanthomatosismolecular pages 2-4, ribeiro2023pathophysiologyandtreatment pages 10-12).

### 6.2 Causal chain from gene defect to clinical manifestations
Evidence-supported causal chain:
1. **Biallelic *CYP27A1* variants → sterol 27-hydroxylase deficiency** (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).
2. **Reduced bile acid synthesis (notably CDCA) + dysregulated bile-acid pathway flux** (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, koyama2021cerebrotendinousxanthomatosismolecular pages 2-4).
3. **Increased cholestanol and bile alcohols** in blood/urine and accumulation in tissues (brain, lenses, tendons) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, koyama2021cerebrotendinousxanthomatosismolecular pages 2-4).
4. **Tissue deposition → cataracts, tendon xanthomas, progressive neurodegeneration/neurologic dysfunction** (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, duell2018diagnosistreatmentand pages 1-8).

### 6.3 Cellular processes and recent mechanistic modeling (2023)
**Human iPSC neuron models (2023):** Mou et al. generated patient-derived iPSCs and differentiated them to cortical projection neurons. They report that neurons “**recapitulated several disease-specific biochemical changes and axonal defects**” and that CDCA “**rescued axonal degeneration**” (quotes) (mou2023chenodeoxycholicacidrescues pages 1-2). This supports a mechanistic link between bile-acid/sterol pathway disruption and axonopathy in human neuronal cells.

### 6.4 Molecular profiling signals (human physiology; 2023)
**Postprandial bile acid and glucose-regulatory signaling (2023):** In a mixed-meal test study (7 CTX vs 7 matched controls), CTX patients had markedly low postprandial bile acids and altered glucose/insulin dynamics; GLP-1 responses were slightly higher and FGF19 lower (majait2023characterizationofpostprandial pages 1-2). This supports systemic endocrine consequences of impaired bile-acid signaling.

### 6.5 Suggested ontology terms
- **GO Biological Process (suggested):** bile acid biosynthetic process (GO:0006699); cholesterol metabolic process (GO:0008203)
- **GO Cellular Component (suggested):** mitochondrion (CYP27A1 is mitochondrial) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **Cell Ontology (suggested):** cortical projection neuron (CL:0000540; model system) (mou2023chenodeoxycholicacidrescues pages 1-2)
- **CHEBI (suggested):** chenodeoxycholic acid; cholestanol (mentioned as key metabolites/therapy targets) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, duell2018diagnosistreatmentand pages 1-8)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue systems (evidence-supported)
CTX involves deposition/accumulation in:
- **Central nervous system / brain** (neurologic dysfunction; deposition in brain) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **Eye lenses** (juvenile cataracts) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2)
- **Tendons (e.g., Achilles)** (tendon xanthomas) (duell2018diagnosistreatmentand pages 1-8)

### 7.2 Neuroimaging localization
A recent synthesis notes characteristic MRI findings: “**signal hyperintensities observed in T2-weighted and/or FLAIR imaging, particularly in the dentate nuclei and the surrounding cerebellar white matter**” (quote) (luo2024frontierandhotspot pages 6-9).

### 7.3 Suggested anatomy ontology terms
- **UBERON (suggested):** brain (UBERON:0000955), cerebellar dentate nucleus (UBERON term), Achilles tendon (UBERON:0010885), lens of eye (UBERON:0000962)

---

## 8. Temporal Development

### 8.1 Onset
CTX commonly has early-life manifestations (e.g., diarrhea, cataracts) preceding later neurologic disease; diagnostic delays into adulthood are common (duell2018diagnosistreatmentand pages 8-12, koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

### 8.2 Progression
Disease is progressive and potentially debilitating/fatal if untreated, particularly due to neurologic involvement; earlier bile acid replacement improves prognosis (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

### 8.3 Critical periods
Evidence supports a clinically important window: CDCA is effective, but “**the effect of CDCA treatment is limited once significant neuropsychiatric manifestations are established**” (quote) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2). This supports early detection initiatives in pediatrics/ophthalmology and early neurologic phases.

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal recessive** (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

### 9.2 Epidemiology and prevalence
Prevalence estimates in retrieved evidence vary across sources/populations:
- Practice review reports prevalence estimates **~1:72,000–1:150,000 in the United States**, and **“6 per 70,000” among Moroccan Sephardic Jews**; it also notes >400 cases reported worldwide (nobrega2022cerebrotendinousxanthomatosisa pages 1-2).
- Bibliometric review reports wide-ranging estimates across populations (e.g., **Asian 1 in 44,407–1 in 93,084; Finns 1 in 3,388,767; others 1 in 70,795–1 in 233,597**) (luo2024frontierandhotspot pages 1-2).

These estimates collectively support that CTX is rare and likely underdiagnosed (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, nobrega2022cerebrotendinousxanthomatosisa pages 1-2).

### 9.3 Population genetics / founder effects / carrier frequency
No founder mutations or carrier frequencies were extractable from retrieved evidence. (This would typically require gnomAD/ClinVar/ethnic-cohort papers.)

---

## 10. Diagnostics

### 10.1 Clinical and laboratory tests
Key biochemical diagnostic features:
- **Elevated plasma cholestanol** is a central diagnostic biomarker (duell2018diagnosistreatmentand pages 1-8, duell2018diagnosistreatmentand pages 32-32).
- Diagnostic threshold highlighted: plasma cholestanol **>10 mg/L** with confirmatory *CYP27A1* testing (duell2018diagnosistreatmentand pages 32-32).
- Reviews highlight additional biomarkers/precursors useful for suspicion/monitoring, including **7α-hydroxy-4-cholesten-3-one** and related ketosterols (koyama2021cerebrotendinousxanthomatosismolecular pages 2-4, ribeiro2023pathophysiologyandtreatment pages 10-12).

### 10.2 Imaging and other testing
- Neuroimaging commonly reveals cerebellar/dentate nucleus T2/FLAIR hyperintensities (luo2024frontierandhotspot pages 6-9).

### 10.3 Genetic testing
- Confirmatory testing relies on identifying biallelic pathogenic variants in ***CYP27A1*** (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, duell2018diagnosistreatmentand pages 32-32).

### 10.4 Differential diagnosis
Retrieved evidence emphasizes that elevated cholestanol can also be seen in other disorders and may confound interpretation, including **familial hypercholesterolemia** and **sitosterolemia** (duell2018diagnosistreatmentand pages 32-32). Reviews also mention distinguishing features/markers relative to **Smith–Lemli–Opitz syndrome** (ribeiro2023pathophysiologyandtreatment pages 10-12).

---

## 11. Outcome / Prognosis

### 11.1 Prognosis without treatment
Untreated CTX is progressive and can lead to severe disability and premature death, particularly due to neurologic involvement (duell2018diagnosistreatmentand pages 8-12, koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

### 11.2 Prognostic factors
Earlier diagnosis and earlier initiation of bile acid replacement are consistently tied to improved outcomes; one review states “**The age at diagnosis and initiation of CDCA treatment correlate with the prognosis**” (quote) (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

---

## 12. Treatment

### 12.1 Standard disease-modifying therapy: chenodeoxycholic acid (CDCA)
CDCA replacement is consistently described as first-line disease-modifying therapy (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2, ribeiro2023pathophysiologyandtreatment pages 10-12).

**Clinical outcomes (43-case series):**
- Mean pre-treatment cholestanol **32 mg/L** (normal <5) decreased to **6.0 mg/L (−81%)** on CDCA 250 mg three times daily; **63%** achieved normal cholestanol (<5 mg/L) (duell2018diagnosistreatmentand pages 1-8).
- Clinical trajectory: **57% improved/stabilized**, **23% stable**, **20% progressed** (progressors all diagnosed at ≥25 years in that series) (duell2018diagnosistreatmentand pages 8-12).

**Expert synthesis:** CDCA can “**dramatically alter the natural history**” when started early, but benefit is limited in advanced neurologic disease (duell2018diagnosistreatmentand pages 8-12, koyama2021cerebrotendinousxanthomatosismolecular pages 1-2).

**MAXO suggestions (expert mapping):**
- Chenodeoxycholic acid therapy (bile acid replacement)
- Pharmacotherapy

### 12.2 Alternative bile-acid replacement: cholic acid (CA)
A comprehensive review reports that FDA-approved **cholic acid** is an alternative for CTX, reducing cholestanol in CSF/blood and urine bile alcohol excretion, with outcomes described as indistinguishable from CDCA and fewer adverse effects (pasternack2025cholicacidas pages 1-3). (Note: this is a 2025 source; included for completeness regarding real-world alternative bile acid replacement.)

### 12.3 Recent developments (2023–2024)

**Mechanistic/therapeutic modeling (2023):** Mou et al. (2023) show that CDCA can rescue axonal degeneration in CTX patient iPSC-derived cortical projection neurons, supporting a direct neuronal mechanism responsive to bile-acid replacement (mou2023chenodeoxycholicacidrescues pages 1-2).

**Metabolic/endocrine characterization (2023):** Majait et al. (2023) describe altered postprandial bile acid profiles and glucose/insulin dynamics in CTX (7 patients vs 7 controls), emphasizing systemic consequences of bile-acid deficiency beyond neurology (majait2023characterizationofpostprandial pages 1-2).

**Clinical trial registry evidence (results posted 2024):**
- **RESTORE (NCT04270682):** Phase 3 interventional CDCA study (n=19), completed in 2023; results first posted **2024-10-28**. Primary endpoint: change in urine **23S-pentol**; key secondary endpoints include plasma cholestanol and 7αC4 (NCT04270682 chunk 1).

(Important limitation: the retrieved ClinicalTrials.gov text excerpts include design and posting dates but do not provide analyzable outcome values.)

### 12.4 Adverse effects / monitoring
CDCA generally has an acceptable safety profile in long-term cohorts (duell2018diagnosistreatmentand pages 8-12). Case-based synthesis describes adverse events such as constipation and hepatotoxicity requiring monitoring and potential dose adjustment (ejsmontsowała2024casereportcerebrotendinous pages 3-4).

---

## 13. Prevention

### 13.1 Secondary prevention (early detection)
Because early therapy improves prognosis and later neurologic disease may be less reversible, CTX prevention largely focuses on **early identification** in high-yield clinical entry points:

**Ophthalmology-based ascertainment (juvenile cataracts):**
- A large observational prevalence study (NCT02638220) screened patients with idiopathic bilateral cataracts (ages 2–21) using genetic testing; it completed enrollment (n=442) and posted results in 2024, representing a real-world implementation of “cataract-first” case finding for CTX (NCT02638220 chunk 1).

**MAXO suggestions (expert mapping):**
- Genetic screening / diagnostic genetic testing
- Cascade testing (not directly evidenced in retrieved text)

---

## 14. Other Species / Natural Disease
No naturally occurring CTX-like disease in non-human species was identified in the retrieved evidence set.

---

## 15. Model Organisms

### 15.1 Human cellular models (strong evidence in retrieved set)
- **Patient-derived iPSC cortical projection neurons** recapitulate biochemical abnormalities and axonal degeneration, which is rescued by CDCA (mou2023chenodeoxycholicacidrescues pages 1-2). This is currently the most concrete “model system” in the retrieved evidence.

### 15.2 Animal models
No specific CTX animal model descriptions were identified in the retrieved evidence set.

---

## Recent developments and authoritative expert perspectives (2023–2024 emphasis)
- 2023 mechanistic iPSC evidence supports a neuron-intrinsic axonopathy component and CDCA-rescuable phenotypes, strengthening mechanistic plausibility for early bile-acid replacement and offering a platform for drug discovery (mou2023chenodeoxycholicacidrescues pages 1-2).
- 2023 physiologic study highlights broader bile-acid signaling effects (GLP-1/FGF19 axis) and suggests metabolic phenotyping may reveal additional treatable consequences or biomarkers (majait2023characterizationofpostprandial pages 1-2).
- 2024 bibliometric analysis identifies “diagnosis” as a major hotspot and emphasizes early diagnosis/intervention as urgent priorities in the CTX literature (luo2024frontierandhotspot pages 1-2).

---

## Key limitations of this evidence packet
- **Orphanet, ICD-10/ICD-11, and MeSH numeric identifiers** were not retrievable in the provided evidence; only a MeSH condition name mapping was available from ClinicalTrials.gov metadata (NCT04270682 chunk 2).
- **Variant-level spectrum and allele frequencies** (ClinVar/gnomAD) were not included in retrieved texts.
- **Animal model evidence** and **non-human natural disease** evidence were not captured in retrieved sources.

---

## URLs and publication dates (examples from retrieved evidence)
- Nóbrega et al. *Frontiers in Neurology* (Dec 2022). https://doi.org/10.3389/fneur.2022.1049850 (nobrega2022cerebrotendinousxanthomatosisa pages 1-2)
- Ribeiro et al. *Brain Sciences* (Jun 2023). https://doi.org/10.3390/brainsci13070979 (ribeiro2023pathophysiologyandtreatment pages 10-12)
- Mou et al. *Orphanet Journal of Rare Diseases* (Apr 2023). https://doi.org/10.1186/s13023-023-02666-w (mou2023chenodeoxycholicacidrescues pages 1-2)
- Majait et al. *Nutrients* (Oct 2023). https://doi.org/10.3390/nu15214625 (majait2023characterizationofpostprandial pages 1-2)
- Luo et al. *Frontiers in Neurology* (Jul 2024). https://doi.org/10.3389/fneur.2024.1371375 (luo2024frontierandhotspot pages 1-2)
- ClinicalTrials.gov RESTORE NCT04270682 (results posted 2024-10-28). https://clinicaltrials.gov/study/NCT04270682 (NCT04270682 chunk 1)
- ClinicalTrials.gov CTX Prevalence Study NCT02638220 (results posted 2024-09-19). https://clinicaltrials.gov/study/NCT02638220 (NCT02638220 chunk 1)


References

1. (nobrega2022cerebrotendinousxanthomatosisa pages 1-2): Paulo Ribeiro Nóbrega, Anderson Moura Bernardes, Rodrigo Mariano Ribeiro, Sophia Costa Vasconcelos, David Augusto Batista Sá Araújo, Vitor Carneiro de Vasconcelos Gama, Helena Fussiger, Carolina de Figueiredo Santos, Daniel Aguiar Dias, André Luíz Santos Pessoa, Wladimir Bocca Vieira de Rezende Pinto, Jonas Alex Morales Saute, Paulo Victor Sgobbi de Souza, and Pedro Braga-Neto. Cerebrotendinous xanthomatosis: a practice review of pathophysiology, diagnosis, and treatment. Frontiers in Neurology, Dec 2022. URL: https://doi.org/10.3389/fneur.2022.1049850, doi:10.3389/fneur.2022.1049850. This article has 51 citations and is from a peer-reviewed journal.

2. (koyama2021cerebrotendinousxanthomatosismolecular pages 1-2): Shingo Koyama, Yoshiki Sekijima, Masatsune Ogura, Mika Hori, Kota Matsuki, Takashi Miida, and Mariko Harada-Shiba. Cerebrotendinous xanthomatosis: molecular pathogenesis, clinical spectrum, diagnosis, and disease-modifying treatments. Journal of Atherosclerosis and Thrombosis, 28:905-925, Sep 2021. URL: https://doi.org/10.5551/jat.rv17055, doi:10.5551/jat.rv17055. This article has 61 citations and is from a peer-reviewed journal.

3. (NCT04270682 chunk 2):  Study to Evaluate Patients With Cerebrotendinous Xanthomatosis (RESTORE). Mirum Pharmaceuticals, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04270682

4. (ribeiro2023pathophysiologyandtreatment pages 10-12): Rodrigo Mariano Ribeiro, Sophia Costa Vasconcelos, Pedro Lucas Grangeiro de Sá Barreto Lima, Emanuel Ferreira Coelho, Anna Melissa Noronha Oliveira, Emanuel de Assis Bertulino Martins Gomes, Luciano de Albuquerque Mota, Lucas Soares Radtke, Matheus dos Santos Carvalho, David Augusto Batista Sá Araújo, Maria Suelly Nogueira Pinheiro, Vitor Carneiro de Vasconcelos Gama, Renan Magalhães Montenegro Júnior, Pedro Braga Neto, and Paulo Ribeiro Nóbrega. Pathophysiology and treatment of lipid abnormalities in cerebrotendinous xanthomatosis: an integrative review. Brain Sciences, 13:979, Jun 2023. URL: https://doi.org/10.3390/brainsci13070979, doi:10.3390/brainsci13070979. This article has 19 citations.

5. (duell2018diagnosistreatmentand pages 8-12): P. Barton Duell, Gerald Salen, Florian S. Eichler, Andrea E. DeBarber, Sonja L. Connor, Lise Casaday, Suman Jayadev, Yasushi Kisanuki, Patamaporn Lekprasert, Mary J. Malloy, Ritesh A. Ramdhani, Paul E. Ziajka, Joseph F. Quinn, Kimmy G. Su, Andrew S. Geller, Margaret R. Diffenderfer, and Ernst J. Schaefer. Diagnosis, treatment, and clinical outcomes in 43 cases with cerebrotendinous xanthomatosis. Journal of clinical lipidology, 12 5:1169-1178, Sep 2018. URL: https://doi.org/10.1016/j.jacl.2018.06.008, doi:10.1016/j.jacl.2018.06.008. This article has 143 citations and is from a peer-reviewed journal.

6. (duell2018diagnosistreatmentand pages 1-8): P. Barton Duell, Gerald Salen, Florian S. Eichler, Andrea E. DeBarber, Sonja L. Connor, Lise Casaday, Suman Jayadev, Yasushi Kisanuki, Patamaporn Lekprasert, Mary J. Malloy, Ritesh A. Ramdhani, Paul E. Ziajka, Joseph F. Quinn, Kimmy G. Su, Andrew S. Geller, Margaret R. Diffenderfer, and Ernst J. Schaefer. Diagnosis, treatment, and clinical outcomes in 43 cases with cerebrotendinous xanthomatosis. Journal of clinical lipidology, 12 5:1169-1178, Sep 2018. URL: https://doi.org/10.1016/j.jacl.2018.06.008, doi:10.1016/j.jacl.2018.06.008. This article has 143 citations and is from a peer-reviewed journal.

7. (mou2023chenodeoxycholicacidrescues pages 1-2): Yongchao Mou, Ghata Nandi, Sukhada Mukte, Eric Chai, Zhenyu Chen, Jorgen E. Nielsen, Troels T. Nielsen, Chiara Criscuolo, Craig Blackstone, Matthew J. Fraidakis, and Xue-Jun Li. Chenodeoxycholic acid rescues axonal degeneration in induced pluripotent stem cell-derived neurons from spastic paraplegia type 5 and cerebrotendinous xanthomatosis patients. Orphanet Journal of Rare Diseases, Apr 2023. URL: https://doi.org/10.1186/s13023-023-02666-w, doi:10.1186/s13023-023-02666-w. This article has 9 citations and is from a peer-reviewed journal.

8. (NCT02638220 chunk 1):  Cerebrotendinous Xanthomatosis (CTX) Prevalence Study. Travere Therapeutics, Inc.. 2015. ClinicalTrials.gov Identifier: NCT02638220

9. (NCT04270682 chunk 1):  Study to Evaluate Patients With Cerebrotendinous Xanthomatosis (RESTORE). Mirum Pharmaceuticals, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04270682

10. (koyama2021cerebrotendinousxanthomatosismolecular pages 2-4): Shingo Koyama, Yoshiki Sekijima, Masatsune Ogura, Mika Hori, Kota Matsuki, Takashi Miida, and Mariko Harada-Shiba. Cerebrotendinous xanthomatosis: molecular pathogenesis, clinical spectrum, diagnosis, and disease-modifying treatments. Journal of Atherosclerosis and Thrombosis, 28:905-925, Sep 2021. URL: https://doi.org/10.5551/jat.rv17055, doi:10.5551/jat.rv17055. This article has 61 citations and is from a peer-reviewed journal.

11. (ejsmontsowała2024casereportcerebrotendinous pages 1-2): Karolina Ejsmont-Sowała, Tomasz Książek, Katarzyna Maciorowska-Rosłan, Joanna Rosłan, Agata Czarnowska, Anna Jakubiuk-Tomaszuk, Joanna Tarasiuk, Katarzyna Kapica-Topczewska, and Alina Kułakowska. Case report: cerebrotendinous xanthomatosis treatment follow-up. Frontiers in Neurology, Jun 2024. URL: https://doi.org/10.3389/fneur.2024.1409138, doi:10.3389/fneur.2024.1409138. This article has 1 citations and is from a peer-reviewed journal.

12. (majait2023characterizationofpostprandial pages 1-2): Soumia Majait, Emma C. E. Meessen, Frederic Maxime Vaz, E. Marleen Kemper, Samuel van Nierop, Steven W. Olde Damink, Frank G. Schaap, Johannes A. Romijn, Max Nieuwdorp, Aad Verrips, Filip Krag Knop, and Maarten R. Soeters. Characterization of postprandial bile acid profiles and glucose metabolism in cerebrotendinous xanthomatosis. Nutrients, 15:4625, Oct 2023. URL: https://doi.org/10.3390/nu15214625, doi:10.3390/nu15214625. This article has 3 citations.

13. (luo2024frontierandhotspot pages 6-9): Fei Luo, Yali Ding, Shanyun Zhang, Juanjuan Diao, and Bin Yuan. Frontier and hotspot evolution in cerebrotendinous xanthomatosis: a bibliometric analysis from 1993 to 2023. Frontiers in Neurology, Jul 2024. URL: https://doi.org/10.3389/fneur.2024.1371375, doi:10.3389/fneur.2024.1371375. This article has 2 citations and is from a peer-reviewed journal.

14. (luo2024frontierandhotspot pages 1-2): Fei Luo, Yali Ding, Shanyun Zhang, Juanjuan Diao, and Bin Yuan. Frontier and hotspot evolution in cerebrotendinous xanthomatosis: a bibliometric analysis from 1993 to 2023. Frontiers in Neurology, Jul 2024. URL: https://doi.org/10.3389/fneur.2024.1371375, doi:10.3389/fneur.2024.1371375. This article has 2 citations and is from a peer-reviewed journal.

15. (duell2018diagnosistreatmentand pages 32-32): P. Barton Duell, Gerald Salen, Florian S. Eichler, Andrea E. DeBarber, Sonja L. Connor, Lise Casaday, Suman Jayadev, Yasushi Kisanuki, Patamaporn Lekprasert, Mary J. Malloy, Ritesh A. Ramdhani, Paul E. Ziajka, Joseph F. Quinn, Kimmy G. Su, Andrew S. Geller, Margaret R. Diffenderfer, and Ernst J. Schaefer. Diagnosis, treatment, and clinical outcomes in 43 cases with cerebrotendinous xanthomatosis. Journal of clinical lipidology, 12 5:1169-1178, Sep 2018. URL: https://doi.org/10.1016/j.jacl.2018.06.008, doi:10.1016/j.jacl.2018.06.008. This article has 143 citations and is from a peer-reviewed journal.

16. (pasternack2025cholicacidas pages 1-3): Gary Pasternack, Jeff Courtney, and Gurdyal Kalsi. Cholic acid as a treatment for cerebrotendinous xanthomatosis: a comprehensive review of safety and efficacy. Orphanet Journal of Rare Diseases, Jul 2025. URL: https://doi.org/10.1186/s13023-025-03889-9, doi:10.1186/s13023-025-03889-9. This article has 2 citations and is from a peer-reviewed journal.

17. (ejsmontsowała2024casereportcerebrotendinous pages 3-4): Karolina Ejsmont-Sowała, Tomasz Książek, Katarzyna Maciorowska-Rosłan, Joanna Rosłan, Agata Czarnowska, Anna Jakubiuk-Tomaszuk, Joanna Tarasiuk, Katarzyna Kapica-Topczewska, and Alina Kułakowska. Case report: cerebrotendinous xanthomatosis treatment follow-up. Frontiers in Neurology, Jun 2024. URL: https://doi.org/10.3389/fneur.2024.1409138, doi:10.3389/fneur.2024.1409138. This article has 1 citations and is from a peer-reviewed journal.
