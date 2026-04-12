---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T17:18:22.361799'
end_time: '2026-04-04T17:26:19.501346'
duration_seconds: 477.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Whipple Disease
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Whipple Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Whipple Disease** covering all of the
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
- **Disease Name:** Whipple Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Whipple Disease** covering all of the
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


## Comprehensive Research Report: Whipple Disease (Infectious)

### Executive summary (current understanding)
Whipple disease (WD) is a rare, potentially fatal, chronic multisystem infection caused by the Gram-positive intracellular bacterium *Tropheryma whipplei* (TW). It classically involves the small intestine (malabsorption/diarrhea/weight loss) but frequently presents first with extra-intestinal manifestations, particularly migratory/seronegative arthritis, and can involve the central nervous system (CNS), heart (e.g., culture-negative endocarditis), lungs, lymph nodes, and eyes. Diagnosis relies on a combination of histopathology (PAS-positive foamy macrophages), molecular detection (PCR), and/or immunohistochemistry; prolonged antimicrobial therapy is required, and immune reconstitution inflammatory syndrome (IRIS) can complicate treatment. (melas2021whipplesdiseasethe pages 1-2, song2023currentknowledgeof pages 1-2, mecklenburg2023thespectrumof pages 1-2)

| Title | Finding | Quantitative value | Notes | Citation |
|---|---|---:|---|---|
| Whipple disease: key quantitative findings | US inpatient prevalence | 4.6 per 1,000,000 hospitalizations | National Inpatient Sample, 2016–2018; 490 WD hospitalizations identified after exclusions | (ahmad2022whipple’sdiseasereview pages 1-2, ahmad2022whipple’sdiseasereview pages 2-3, ahmad2022whipple’sdiseasereview pages 2-2) |
| Whipple disease: key quantitative findings | US population prevalence (Explorys) | 9.8 per 1,000,000 | Population-based EHR study, 350 cases among 35,838,070 active individuals, 2012–2017 | (elchert2019epidemiologyofwhipple’s pages 5-6, elchert2019epidemiologyofwhipple’s pages 1-3, song2023currentknowledgeof pages 1-2) |
| Whipple disease: key quantitative findings | Age/sex pattern in NIS | Mean age 60.2 ± 1.6 years; males 67.3%; aRR 2.77 for males; aRR 7.42 for age 30–59 and 5.94 for age ≥60 vs <30 | Midwest overrepresented; older age and male sex increase inpatient risk | (ahmad2022whipple’sdiseasereview pages 1-2, ahmad2022whipple’sdiseasereview pages 2-3, ahmad2022whipple’sdiseasereview pages 2-2) |
| Whipple disease: key quantitative findings | T. whipplei carriage in stool/saliva | Stool: 1–11% healthy individuals, 12–26% sewage workers; saliva: 0.2% healthy individuals, 2.2% sewage workers | Carriage can be common despite rare clinical disease; one Senegal study found stool carriage up to 31% | (tison2021rheumatologicalfeaturesof pages 1-2, ahmad2022whipple’sdiseasereview pages 1-2) |
| Whipple disease: key quantitative findings | CNS involvement frequency | 22%–64% reported range; 63.9% (23/36) in Charité cohort | Neurologic disease is common and prognostically important | (mecklenburg2023thespectrumof pages 1-2, mecklenburg2023thespectrumof pages 1-1, vargasrodriguez2023whipplesdiseasea pages 3-5) |
| Whipple disease: key quantitative findings | CSF PCR positivity for T. whipplei | 48.6% of patients (17/35) positive at any time; 59.1% (13/22) with neurologic symptoms vs 30.8% (4/13) without, p=0.0496 | PCR positivity correlates imperfectly with neurologic symptoms | (mecklenburg2023thespectrumof pages 1-1, mecklenburg2023thespectrumof pages 4-5) |
| Whipple disease: key quantitative findings | Ischemic stroke frequency in CNS cohort | 27.7% (10/36) WD cohort vs 3.2% (10/360) matched controls | Suggests stroke is an underrecognized manifestation of CNS WD | (mecklenburg2023thespectrumof pages 1-1, mecklenburg2023thespectrumof pages 4-5) |
| Whipple disease: key quantitative findings | Diagnostic PCR performance (Tison 2021) | Stool PCR sensitivity: 100% classic WD, 75% non-classic WD; saliva PCR sensitivity: 100% classic WD, 75% non-classic WD; small-bowel biopsy PCR sensitivity: 89% classic WD, 60% non-classic WD; blood PCR sensitivity: 50% classic WD, 23% non-classic WD; urine PCR sensitivity: 33% classic WD, 13% non-classic WD | Supports multi-site PCR strategy; stool/saliva best noninvasive screening in this cohort | (tison2021rheumatologicalfeaturesof pages 3-4, tison2021rheumatologicalfeaturesof pages 1-2) |
| Whipple disease: key quantitative findings | Relapse rates | 32% (21/65) in Tison cohort; historically ~30%; recent controlled/prospective series reported no relapse in 73/74 patients over 85 months | Relapse estimates vary by cohort and treatment era | (tison2021rheumatologicalfeaturesof pages 3-4, marth2016tropherymawhippleiinfection pages 6-7, dolmans2017clinicalmanifestationstreatment pages 18-20, schiepatti2020longtermmorbidityand pages 6-7) |
| Whipple disease: key quantitative findings | Mortality | Inpatient mortality 3.1% in NIS; overall mortality 1.4% cited in 2023 IRIS review | CNS/systemic infection admissions had especially high mortality in inpatient data | (ahmad2022whipple’sdiseasereview pages 2-2, song2023currentknowledgeof pages 1-2) |


*Table: This table compiles high-yield quantitative findings for Whipple disease across epidemiology, neurologic involvement, diagnostics, relapse, and mortality. It is useful as a quick-reference evidence summary for knowledge base curation and report writing.*

---

## 1. Disease Information

### 1.1 Definition / overview
WD is a rare systemic infectious disorder caused by TW with protean gastrointestinal, rheumatologic, neurologic, and other systemic manifestations. (ahmad2022whipple’sdiseasereview pages 1-2, melas2021whipplesdiseasethe pages 1-2)

### 1.2 Key identifiers (from retrieved sources)
- **ICD-10-CM:** **K90.81** (used for case ascertainment in a US National Inpatient Sample analysis). **Publication date:** Dec 2022. **URL:** https://doi.org/10.1097/MD.0000000000032231 (ahmad2022whipple’sdiseasereview pages 1-2)

### 1.3 Other identifiers requested but not recoverable from the available full-text evidence in this run
- **MONDO ID:** not available from retrieved evidence.
- **Orphanet (ORPHA) ID:** not available from retrieved evidence.
- **MeSH descriptor:** not available from retrieved evidence.
- **ICD-11 code:** not available from retrieved evidence.

*Note:* The retrieved ICD-11/Orphanet mapping papers were methodological and did not provide the WD-specific mappings in the accessible text chunks returned here. (ahmad2022whipple’sdiseasereview pages 1-2)

### 1.4 Synonyms and alternative names (from retrieved sources)
- **Whipple disease / Whipple’s disease** (standard names). (ahmad2022whipple’sdiseasereview pages 1-2)
- **Tropheryma whipplei infection** (used in clinical reviews/series). (hujoel2019tropherymawhippleiinfection pages 1-2)
- **Classic Whipple disease** vs **localized / non-classic disease** (clinical sub-phenotypes used in cohorts). (tison2021rheumatologicalfeaturesof pages 1-2, hujoel2019tropherymawhippleiinfection pages 1-2)

### 1.5 Evidence sources (individual vs aggregated)
- **Aggregated disease-level resources:** national inpatient database analysis (NIS) and national EHR aggregation (Explorys) for epidemiology and demographics. (ahmad2022whipple’sdiseasereview pages 2-2, elchert2019epidemiologyofwhipple’s pages 1-3)
- **Aggregated clinical cohorts:** multicenter rheumatology cohort; single-center CNS cohort. (tison2021rheumatologicalfeaturesof pages 3-4, mecklenburg2023thespectrumof pages 1-1)
- **Individual patient reports:** used mainly to illustrate atypical presentations and prolonged therapy. (ye2023whipple’sdiseasepresenting pages 2-5)

---

## 2. Etiology

### 2.1 Disease causal factors
- **Infectious agent:** WD is caused by systemic infection with **TW**, a Gram-positive actinobacterium that replicates intracellularly in macrophages and can disseminate. (dolmans2017clinicalmanifestationstreatment pages 1-3, dolmans2017clinicalmanifestationstreatment pages 7-8)

### 2.2 Risk factors
**Host susceptibility / immune context**
- WD occurs in a small fraction of exposed/carrier individuals, supporting a major role for **host susceptibility**. In a US inpatient study, TW carriage in stool is reported at **~1–11%** in healthy individuals while progression to WD is **<0.01%**. (ahmad2022whipple’sdiseasereview pages 1-2)
- **Immunosuppression** can worsen or unmask disease, including poor response/worsening under TNF inhibitors in a multicenter cohort. (tison2021rheumatologicalfeaturesof pages 1-2, dolmans2017clinicalmanifestationstreatment pages 18-20)

**Occupational/environmental exposure**
- In a multicenter cohort/review, TW detection in stool was higher in **sewage plant workers (12–26%)** vs healthy controls, supporting exposure/carriage risk in certain occupations. (tison2021rheumatologicalfeaturesof pages 1-2)

**Genetic susceptibility (risk alleles/polymorphisms)**
- HLA associations have been reported, including **HLA-DRB1*13** and **HLA-DQB1*06**, and cytokine-related polymorphisms such as **IL16**, proposed to impair antigen presentation and predispose to chronic relapsing disease. (marth2016tropherymawhippleiinfection pages 2-3, dolmans2017clinicalmanifestationstreatment pages 5-7)

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
A plausible interaction model is supported: environmental/occupational exposure leading to carriage interacts with host immune-genetic susceptibility (HLA/cytokine regulation) to permit intracellular persistence and dissemination. Direct quantitative GxE effect sizes were not identified in the retrieved evidence. (tison2021rheumatologicalfeaturesof pages 1-2, marth2016tropherymawhippleiinfection pages 2-3)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes and characteristics
**Gastrointestinal (classic WD)**
- Typical manifestations include chronic diarrhea, abdominal pain, weight loss, and malabsorption (classic intestinal involvement), with PAS-positive foamy macrophages in small-bowel lamina propria. (melas2021whipplesdiseasethe pages 1-2, song2023currentknowledgeof pages 1-2)

**Rheumatologic**
- Arthritis/arthralgia often precedes GI symptoms; in a diagnostic overview case series, the classic course included a prodromal stage where **arthritis is the first and most common manifestation (~75%)**. (melas2021whipplesdiseasethe pages 1-2)

**Neurologic/CNS**
- Neurologic involvement is common and prognostically important; a 2023 CNS cohort reported neurologic involvement in **63.9% (23/36)**. (mecklenburg2023thespectrumof pages 1-1)
- Frequent neurologic domains included cognitive, motor (pyramidal), and oculomotor dysfunction; specific signs such as oculomasticatory myorhythmia and supranuclear vertical gaze palsy are emphasized as WD-specific clues in CNS disease. (mecklenburg2023thespectrumof pages 1-1, mecklenburg2023thespectrumof pages 1-2)

**Other organ involvement**
- Cardiovascular manifestations include culture-negative endocarditis (discussed as part of systemic spectrum in reviews/cohorts). (tison2021rheumatologicalfeaturesof pages 1-2, dolmans2017clinicalmanifestationstreatment pages 10-12)
- Lymphadenopathy, fever, pleural/pericardial involvement, and uveitis are reported extraintestinal manifestations. (tison2021rheumatologicalfeaturesof pages 1-2)

### 3.2 Frequency data (available from retrieved sources)
- CNS involvement: **22–64%** reported range; **63.9%** in the Charité cohort. (mecklenburg2023thespectrumof pages 1-2, mecklenburg2023thespectrumof pages 1-1)
- Stroke in WD: **27.7% (10/36)** in the Charité cohort vs **3.2% (10/360)** matched controls, suggesting under-recognized vascular CNS involvement. (mecklenburg2023thespectrumof pages 1-1)

### 3.3 Suggested HPO terms (non-exhaustive, to support KB population)
(*Ontology IDs are provided conceptually; exact HP identifiers should be confirmed against the HPO browser during KB ingestion.*)
- Chronic diarrhea; abdominal pain; weight loss; malabsorption; lymphadenopathy. (melas2021whipplesdiseasethe pages 1-2, song2023currentknowledgeof pages 1-2)
- Arthralgia/arthritis (migratory/seronegative); fever. (tison2021rheumatologicalfeaturesof pages 1-2, melas2021whipplesdiseasethe pages 1-2)
- Cognitive impairment/dementia; supranuclear gaze palsy; myorhythmia; seizures (less common); stroke/ischemic cerebrovascular event. (mecklenburg2023thespectrumof pages 1-1, mecklenburg2023thespectrumof pages 1-2)

### 3.4 Quality of life impact
QoL instruments (SF-36/EQ-5D/PROMIS) and quantitative QoL estimates were not identified in the retrieved evidence. However, the long diagnostic delay and multisystem disability burden (arthritis, GI symptoms, cognitive impairment, stroke) imply substantial functional impact. (melas2021whipplesdiseasethe pages 1-2, mecklenburg2023thespectrumof pages 1-1)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
WD is **not a monogenic disorder** in the retrieved evidence; instead, susceptibility is associated with immune-related polymorphisms and HLA alleles. (marth2016tropherymawhippleiinfection pages 2-3, dolmans2017clinicalmanifestationstreatment pages 5-7)

### 4.2 Reported susceptibility loci / variants (from retrieved sources)
- **HLA-DRB1*13, HLA-DQB1*06** (susceptibility associations). (marth2016tropherymawhippleiinfection pages 2-3, dolmans2017clinicalmanifestationstreatment pages 5-7)
- **IL16 polymorphisms** (associated with susceptibility and impaired antigen presentation/immune regulation). (marth2016tropherymawhippleiinfection pages 2-3, dolmans2017clinicalmanifestationstreatment pages 7-8)

Variant-level details (HGVS nomenclature), population allele frequencies (gnomAD), and ClinVar classifications were not available in the retrieved evidence.

### 4.3 Epigenetics, chromosomal abnormalities, modifier genes
Not identified in the retrieved evidence.

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle factors
- Occupational exposure context is supported by higher carriage among sewage workers. (tison2021rheumatologicalfeaturesof pages 1-2)
- Specific lifestyle modifiers (diet, smoking, alcohol) were not identified in the retrieved evidence.

### 5.2 Infectious agent details
TW is an intracellular bacterium that can be difficult to culture and often requires molecular methods for detection; after entry, it survives within macrophages and can disseminate systemically. (dolmans2017clinicalmanifestationstreatment pages 1-3, dolmans2017clinicalmanifestationstreatment pages 7-8)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (integrated model)
1. **Exposure and carriage**: TW carriage in stool/saliva is relatively common in populations, including occupational groups. (tison2021rheumatologicalfeaturesof pages 1-2)
2. **Susceptible host immune state**: predisposition associated with HLA alleles and immune-regulatory polymorphisms plus immune skewing (e.g., increased IL-10/IL-16 and reduced IL-12/IFN-γ). (marth2016tropherymawhippleiinfection pages 2-3)
3. **Failure of macrophage killing**: TW is phagocytosed but persists intracellularly; impaired phagosome maturation and other macrophage defects enable replication and survival. (dolmans2017clinicalmanifestationstreatment pages 7-8)
4. **Dissemination**: infected macrophages/lymphatic-blood dissemination leads to multisystem involvement (GI, joints, CNS, heart, etc.). (dolmans2017clinicalmanifestationstreatment pages 7-8, dolmans2017clinicalmanifestationstreatment pages 10-12)

### 6.2 Key immune mechanisms (host)
- A central theme is impaired **Th1/IL-12/IFN-γ** responses with anti-inflammatory cytokine predominance (IL-10/TGF-β signatures) and enhanced regulatory T-cell activity, contributing to ineffective clearance. (marth2016tropherymawhippleiinfection pages 2-3, dolmans2017clinicalmanifestationstreatment pages 7-8)
- In WD-associated IRIS, exaggerated inflammatory responses during immune recovery are discussed; PCR can be negative and antibiotics often ineffective, consistent with immune-driven pathology rather than active bacterial relapse. (song2023currentknowledgeof pages 1-2)

### 6.3 Suggested GO terms (biological processes; conceptual mapping)
- Macrophage activation; phagocytosis; phagosome maturation; cytokine-mediated signaling pathway; interferon-gamma-mediated signaling pathway; regulation of T-helper 1 type immune response; epithelial apoptotic process (notably in IRIS discussion). (dolmans2017clinicalmanifestationstreatment pages 7-8, song2023currentknowledgeof pages 1-2)

### 6.4 Suggested CL (cell types; conceptual mapping)
- Macrophage (particularly intestinal lamina propria macrophages); CD4+ T cell (Th1, regulatory T cell). (dolmans2017clinicalmanifestationstreatment pages 7-8, marth2016tropherymawhippleiinfection pages 2-3)

### 6.5 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic datasets were captured in the retrieved evidence, though intestinal infiltrating cells were described as showing an alternatively activated macrophage transcriptional pattern in the IRIS review. (song2023currentknowledgeof pages 7-9)

---

## 7. Anatomical Structures Affected

### 7.1 Organ-level involvement
- **Primary**: small intestine (classical intestinal WD). (song2023currentknowledgeof pages 1-2)
- **Common extraintestinal**: joints, CNS/brain, cardiovascular system (endocarditis), lymph nodes. (tison2021rheumatologicalfeaturesof pages 1-2, mecklenburg2023thespectrumof pages 1-2, dolmans2017clinicalmanifestationstreatment pages 10-12)

### 7.2 Tissue/cell-level
- Lamina propria infiltrates with **PAS-positive foamy macrophages** containing bacilli. (song2023currentknowledgeof pages 1-2)

### 7.3 Suggested UBERON terms (conceptual mapping)
- Small intestine; duodenum; jejunum; brain; thalamus/hypothalamus/periaqueductal gray (predilection reported in CNS cohort); heart valve; synovial joint. (mecklenburg2023thespectrumof pages 8-9, mecklenburg2023thespectrumof pages 2-3)

---

## 8. Temporal Development

### 8.1 Onset
- Often **adult onset**; national inpatient data show mean age ~60 among hospitalized cases. (ahmad2022whipple’sdiseasereview pages 2-2)
- The course can include a prolonged prodrome (e.g., years of arthritis before GI disease), contributing to major diagnostic delays. (melas2021whipplesdiseasethe pages 1-2)

### 8.2 Progression / course patterns
- Chronic, progressive, multisystem course if untreated; neurologic involvement can drive worse prognosis. (mecklenburg2023thespectrumof pages 1-2)
- Relapse can occur; historic relapse estimates ~30% but appear lower in more recent controlled/prospective series with prolonged CNS-penetrating regimens and IRIS recognition. (marth2016tropherymawhippleiinfection pages 6-7, schiepatti2020longtermmorbidityand pages 6-7)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **US population prevalence (Explorys, 2012–2017):** **9.8 per 1,000,000**. **Publication date:** Nov 2019. **URL:** https://doi.org/10.1007/s10620-018-5393-9 (elchert2019epidemiologyofwhipple’s pages 1-3)
- **US inpatient prevalence (NIS, 2016–2018):** **4.6 per 1,000,000 hospitalizations**. **Publication date:** Dec 2022. **URL:** https://doi.org/10.1097/MD.0000000000032231 (ahmad2022whipple’sdiseasereview pages 2-2)
- Incidence is cited as ~1 per 1,000,000 in prior literature. (tison2021rheumatologicalfeaturesof pages 1-2, song2023currentknowledgeof pages 1-2)

### 9.2 Population demographics
- NIS (2016–2018): male predominance (~67%), older age distribution (mean ~60), and higher risk in the US Midwest. (ahmad2022whipple’sdiseasereview pages 2-2)
- Explorys (2012–2017): similar prevalence in men and women, higher prevalence in Caucasians vs African Americans, and higher prevalence in non-Hispanics; prevalence increases markedly with age, peaking at ages 80–84 (39.2/million). (elchert2019epidemiologyofwhipple’s pages 5-6)

### 9.3 Inheritance pattern
Not Mendelian; evidence supports **complex susceptibility** (HLA/cytokine polymorphisms) rather than single-gene inheritance. (marth2016tropherymawhippleiinfection pages 2-3)

---

## 10. Diagnostics

### 10.1 Histopathology
- Classic diagnosis relies on small-bowel biopsy showing **PAS-positive foamy macrophages** in lamina propria; PAS has limited specificity because similar PAS-positive macrophages can occur with other infections and can be negative in some patients or localized infection. (dolmans2017clinicalmanifestationstreatment pages 13-17, song2023currentknowledgeof pages 1-2)

**Direct abstract quote (diagnostic histology):**
- “typical foamy macrophages with granular diastase-resistant inclusions presenting a strong positive PAS reaction.” (Cureus case report/review; Jan 2023; https://doi.org/10.7759/cureus.34029) (viegas2023whyiswhipples pages 7-7)

### 10.2 PCR diagnostics (specimen-specific performance)
A large multicenter cohort reported the following **sensitivities** (classic WD vs non-classic WD):
- Stool PCR: **100% vs 75%**
- Saliva PCR: **100% vs 75%**
- Small-bowel biopsy PCR: **89% vs 60%**
- Blood PCR: **50% vs 23%**
- Urine PCR: **33% vs 13%** (tison2021rheumatologicalfeaturesof pages 3-4, tison2021rheumatologicalfeaturesof pages 1-2)

A case review additionally reported performance estimates and interpretive thresholds, including stool specificity ~97.6% and improved PPV when stool+saliva are both positive or fecal load exceeds >32,200 copies/mL. (viegas2023whyiswhipples pages 7-7)

### 10.3 CNS diagnostics (CSF and neuroimaging)
- In a 2023 CNS cohort, TW DNA was detected in CSF more often in neurologically symptomatic patients (**59.1%**) than asymptomatic (**30.8%**), but PCR positivity did not perfectly match clinical syndromes. (mecklenburg2023thespectrumof pages 1-1)
- Neuroimaging often implicated deep midline structures (e.g., hypothalamus, thalamus, periaqueductal region); aqueductal stenosis/hydrocephalus can occur and may require shunting. (mecklenburg2023thespectrumof pages 8-9)

### 10.4 Differential diagnosis (examples supported by evidence)
- Inflammatory bowel disease, lymphoma, and other causes of chronic malabsorption/arthritis due to nonspecific, long prodromal course; PAS false positives can occur with mycobacteria. (melas2021whipplesdiseasethe pages 1-2, hujoel2019tropherymawhippleiinfection pages 1-2)

### 10.5 Advanced molecular diagnostics (recent developments)
- Targeted/metagenomic sequencing approaches (e.g., NGS from bronchoalveolar lavage) are increasingly used to detect TW in respiratory specimens, though colonization vs causation remains a concern in some pneumonia presentations. (ye2023whipple’sdiseasepresenting pages 2-5)

---

## 11. Outcome / Prognosis

### 11.1 Mortality
- US inpatient mortality for WD admissions: **3.1%** (NIS 2016–2018). (ahmad2022whipple’sdiseasereview pages 2-2)
- A 2023 IRIS-focused review cited an overall mortality of **1.4%**. (song2023currentknowledgeof pages 1-2)
- CNS disease is associated with worse outcomes; one review cites ≈25% mortality within 4 years for CNS WD. (marth2016tropherymawhippleiinfection pages 6-7)

### 11.2 Morbidity and complications
- IRIS can occur during treatment and may be severe/fatal; obstructive hydrocephalus and stroke were notable CNS complications in the 2023 CNS cohort. (mecklenburg2023thespectrumof pages 6-7, mecklenburg2023thespectrumof pages 1-1)

### 11.3 Relapse
- A multicenter cohort reported relapse in **32% (21/65)**. (tison2021rheumatologicalfeaturesof pages 3-4)
- Historic relapse estimates ~30% have been cited, but more recent controlled/prospective series reported no relapses over 85 months in 73/74 patients, highlighting likely era/regimen effects. (marth2016tropherymawhippleiinfection pages 6-7, schiepatti2020longtermmorbidityand pages 6-7)

---

## 12. Treatment

### 12.1 Standard antimicrobial therapy (current practice patterns)
- **Induction therapy:** IV ceftriaxone (e.g., 2 g/day for 2 weeks in a major review; meropenem as alternative). (marth2016tropherymawhippleiinfection pages 6-7)
- **Maintenance/eradication therapy (12 months typical):**
  - Co-trimoxazole (TMP-SMX) 960 mg BID for 1 year (historic regimen). (marth2016tropherymawhippleiinfection pages 6-7)
  - Doxycycline plus hydroxychloroquine (e.g., doxycycline 200 mg/day + hydroxychloroquine 600 mg/day) for 1 year; some propose prolonged/lifelong doxycycline suppression in selected patients. (marth2016tropherymawhippleiinfection pages 6-7, zhou2024shorttermamoxicillinclavulanate pages 1-2)

**Important expert analysis (antibiotic resistance/choice):**
- A major microbiology review notes genomic/in vitro evidence consistent with TMP-SMX failure (intrinsic trimethoprim resistance mechanisms) and reports a series in which “all 14 patients who were first treated with co-trimoxazole failed treatment,” supporting doxycycline+hydroxychloroquine as an alternative bactericidal regimen. (dolmans2017clinicalmanifestationstreatment pages 18-20)

### 12.2 Management of WD-associated IRIS
- IRIS occurs in ~10% of classic cases after antibiotic therapy; first-line therapy is oral corticosteroids, and thalidomide is an option for steroid-resistant cases. (dolmans2017clinicalmanifestationstreatment pages 18-20)
- Mechanistic framing: Th1 reconstitution and inflammatory cytokines can drive barrier dysfunction and systemic inflammation; PCR may be negative and antibiotics ineffective during IRIS, emphasizing immune modulation rather than escalation of antimicrobials. (song2023currentknowledgeof pages 1-2)

### 12.3 Real-world implementation examples (recent)
- A 2023 case report (China) used ceftriaxone induction followed by prolonged doxycycline+hydroxychloroquine with radiologic lymph node regression over **44 months**, illustrating long durations sometimes used in practice and the need for monitoring for inflammatory flares (suspected IRIS). **Publication date:** May 2023. **URL:** https://doi.org/10.1186/s12879-023-08276-y (ye2023whipple’sdiseasepresenting pages 2-5)

### 12.4 Suggested MAXO terms (conceptual mapping)
- Antibiotic therapy; intravenous antibiotic administration; long-term oral antibiotic therapy; hydroxychloroquine therapy; corticosteroid therapy; immunomodulatory therapy (thalidomide) for IRIS; ventriculoperitoneal shunt (for hydrocephalus when needed). (marth2016tropherymawhippleiinfection pages 6-7, dolmans2017clinicalmanifestationstreatment pages 18-20, mecklenburg2023thespectrumof pages 8-9)

### 12.5 Clinical trials
No WD-specific interventional clinical trials were retrieved in this run.

---

## 13. Prevention

- No vaccine or established primary prevention strategy was identified in the retrieved evidence.
- Practical prevention in susceptible contexts is mainly **secondary/tertiary**: early recognition in patients with chronic seronegative arthritis plus GI/systemic features; avoidance/caution with immunosuppressive therapy (especially TNF inhibitors) until WD is excluded in suspicious cases; and long-term follow-up for relapse/late CNS disease. (tison2021rheumatologicalfeaturesof pages 1-2, dolmans2017clinicalmanifestationstreatment pages 18-20)

---

## 14. Other Species / Natural Disease
No natural disease in non-human species, zoonotic transmission, or animal reservoirs were identified in the retrieved evidence.

---

## 15. Model Organisms
No in vivo animal models were identified in the retrieved evidence. Mechanistic work emphasized human mucosal immunology and macrophage biology and historical advances in TW culture, implying **in vitro macrophage infection systems** as a key experimental platform. (dolmans2017clinicalmanifestationstreatment pages 1-3, dolmans2017clinicalmanifestationstreatment pages 7-8)

---

## Recent developments (prioritizing 2023–2024)

1. **CNS spectrum refined with cohort-level CSF + imaging analysis (2023):** A 36-patient series reported neurologic involvement in 63.9% and highlighted underrecognized ischemic stroke (27.7%) and imperfect correlation between CSF PCR positivity and neurologic symptoms, emphasizing the need for integrated clinical–CSF–imaging diagnosis and careful interpretation of PCR timing relative to antibiotics. **Publication date:** Aug 2023. **URL:** https://doi.org/10.1111/ene.15511 (mecklenburg2023thespectrumof pages 1-1)
2. **IRIS conceptual updates (2023):** A dedicated review summarized IRIS pathophysiology, highlighting immune-driven inflammation with potential negative PCR and limited antibiotic responsiveness, and discussed corticosteroids and thalidomide for management. **Publication date:** Oct 2023. **URL:** https://doi.org/10.3389/fimmu.2023.1265414 (song2023currentknowledgeof pages 1-2)
3. **Expanded molecular diagnostics and atypical presentations (2023):** A case report highlighted atypical symptoms and very prolonged antibiotic courses with imaging follow-up, and cautioned that TW detection by sequencing alone (especially in pneumonia) may represent colonization rather than disease. **Publication date:** May 2023. **URL:** https://doi.org/10.1186/s12879-023-08276-y (ye2023whipple’sdiseasepresenting pages 2-5)

---

## Limitations of this report (evidence gaps due to tool-retrieved sources)
- Specific **MONDO, Orphanet, MeSH, and ICD-11 identifiers** could not be extracted from the retrieved full texts; only ICD-10 K90.81 was explicitly available. (ahmad2022whipple’sdiseasereview pages 1-2)
- Variant-level genetic details (HGVS, allele frequencies), formal QoL statistics, and robust prevention studies were not present in the retrieved evidence set.

---

## References (retrieved within this run; URLs and dates)
Key 2023–2024 sources highlighted above:
- Song X et al. *Front Immunol.* Oct 2023. “Current knowledge of the immune reconstitution inflammatory syndrome in Whipple disease: a review.” https://doi.org/10.3389/fimmu.2023.1265414 (song2023currentknowledgeof pages 1-2)
- Mecklenburg J et al. *Eur J Neurol.* Aug 2023. “The spectrum of central nervous system involvement in Whipple's disease.” https://doi.org/10.1111/ene.15511 (mecklenburg2023thespectrumof pages 1-1)
- Ye H et al. *BMC Infect Dis.* May 2023. “Whipple’s disease presenting as weight gain and constipation in a Chinese woman.” https://doi.org/10.1186/s12879-023-08276-y (ye2023whipple’sdiseasepresenting pages 2-5)

High-authority background reviews used for mechanisms/diagnostics/treatment:
- Dolmans RAV et al. *Clin Microbiol Rev.* Apr 2017. https://doi.org/10.1128/CMR.00033-16 (dolmans2017clinicalmanifestationstreatment pages 13-17, dolmans2017clinicalmanifestationstreatment pages 18-20, dolmans2017clinicalmanifestationstreatment pages 7-8)
- Marth T et al. *Lancet Infect Dis.* Mar 2016. https://doi.org/10.1016/S1473-3099(15)00537-X (marth2016tropherymawhippleiinfection pages 6-7, marth2016tropherymawhippleiinfection pages 2-3)

Epidemiology:
- Ahmad AI et al. *Medicine.* Dec 2022. https://doi.org/10.1097/MD.0000000000032231 (ahmad2022whipple’sdiseasereview pages 2-2)
- Elchert JA et al. *Dig Dis Sci.* Nov 2019. https://doi.org/10.1007/s10620-018-5393-9 (elchert2019epidemiologyofwhipple’s pages 1-3)


References

1. (melas2021whipplesdiseasethe pages 1-2): Nikolaos Melas, Rasjan Amin, Paula Gyllemark, Amil Haji Younes, and Sven Almer. Whipple's disease: the great masquerader—a high level of suspicion is the key to diagnosis. BMC Gastroenterology, Mar 2021. URL: https://doi.org/10.1186/s12876-021-01664-1, doi:10.1186/s12876-021-01664-1. This article has 31 citations and is from a peer-reviewed journal.

2. (song2023currentknowledgeof pages 1-2): Xiangyi Song, Ruifeng Duan, Liwei Duan, and Lijuan Wei. Current knowledge of the immune reconstitution inflammatory syndrome in whipple disease: a review. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1265414, doi:10.3389/fimmu.2023.1265414. This article has 10 citations and is from a peer-reviewed journal.

3. (mecklenburg2023thespectrumof pages 1-2): Jasper Mecklenburg, Verena Moos, Annette Moter, Eberhard Siebert, Alexander Heinrich Nave, Thomas Schneider, Klemens Ruprecht, and Philipp Euskirchen. The spectrum of central nervous system involvement in whipple's disease. European Journal of Neurology, 30:3417-3429, Aug 2023. URL: https://doi.org/10.1111/ene.15511, doi:10.1111/ene.15511. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (ahmad2022whipple’sdiseasereview pages 1-2): Akram I. Ahmad, Colin Wikholm, Ioannis Pothoulakis, Claire Caplan, Arielle Lee, Faith Buchanan, and Won Kyoo Cho. Whipple’s disease review, prevalence, mortality, and characteristics in the united states: a cross-sectional national inpatient study. Medicine, 101:e32231, Dec 2022. URL: https://doi.org/10.1097/md.0000000000032231, doi:10.1097/md.0000000000032231. This article has 18 citations and is from a peer-reviewed journal.

5. (ahmad2022whipple’sdiseasereview pages 2-3): Akram I. Ahmad, Colin Wikholm, Ioannis Pothoulakis, Claire Caplan, Arielle Lee, Faith Buchanan, and Won Kyoo Cho. Whipple’s disease review, prevalence, mortality, and characteristics in the united states: a cross-sectional national inpatient study. Medicine, 101:e32231, Dec 2022. URL: https://doi.org/10.1097/md.0000000000032231, doi:10.1097/md.0000000000032231. This article has 18 citations and is from a peer-reviewed journal.

6. (ahmad2022whipple’sdiseasereview pages 2-2): Akram I. Ahmad, Colin Wikholm, Ioannis Pothoulakis, Claire Caplan, Arielle Lee, Faith Buchanan, and Won Kyoo Cho. Whipple’s disease review, prevalence, mortality, and characteristics in the united states: a cross-sectional national inpatient study. Medicine, 101:e32231, Dec 2022. URL: https://doi.org/10.1097/md.0000000000032231, doi:10.1097/md.0000000000032231. This article has 18 citations and is from a peer-reviewed journal.

7. (elchert2019epidemiologyofwhipple’s pages 5-6): Jamie Ann Elchert, Emad Mansoor, Mohannad Abou-Saleh, and Gregory S. Cooper. Epidemiology of whipple’s disease in the usa between 2012 and 2017: a population-based national study. Digestive Diseases and Sciences, 64:1305-1311, Nov 2019. URL: https://doi.org/10.1007/s10620-018-5393-9, doi:10.1007/s10620-018-5393-9. This article has 73 citations and is from a peer-reviewed journal.

8. (elchert2019epidemiologyofwhipple’s pages 1-3): Jamie Ann Elchert, Emad Mansoor, Mohannad Abou-Saleh, and Gregory S. Cooper. Epidemiology of whipple’s disease in the usa between 2012 and 2017: a population-based national study. Digestive Diseases and Sciences, 64:1305-1311, Nov 2019. URL: https://doi.org/10.1007/s10620-018-5393-9, doi:10.1007/s10620-018-5393-9. This article has 73 citations and is from a peer-reviewed journal.

9. (tison2021rheumatologicalfeaturesof pages 1-2): Alice Tison, Pauline Preuss, Clémentine Leleu, François Robin, Adrien Le Pluart, Justine Vix, Guillaume Le Mélédo, Philippe Goupille, Elisabeth Gervais, Grégoire Cormier, Jean-David Albert, Aleth Perdriger, Béatrice Bouvard, Jean-Marie Berthelot, Nathan Foulquier, and Alain Saraux. Rheumatological features of whipple disease. Scientific Reports, Jun 2021. URL: https://doi.org/10.1038/s41598-021-91671-9, doi:10.1038/s41598-021-91671-9. This article has 39 citations and is from a peer-reviewed journal.

10. (mecklenburg2023thespectrumof pages 1-1): Jasper Mecklenburg, Verena Moos, Annette Moter, Eberhard Siebert, Alexander Heinrich Nave, Thomas Schneider, Klemens Ruprecht, and Philipp Euskirchen. The spectrum of central nervous system involvement in whipple's disease. European Journal of Neurology, 30:3417-3429, Aug 2023. URL: https://doi.org/10.1111/ene.15511, doi:10.1111/ene.15511. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (vargasrodriguez2023whipplesdiseasea pages 3-5): LJ Vargas-Rodríguez and JL Ruiz-Muñoz. Whipple's disease: a systematic review of the literature. Unknown journal, 2023.

12. (mecklenburg2023thespectrumof pages 4-5): Jasper Mecklenburg, Verena Moos, Annette Moter, Eberhard Siebert, Alexander Heinrich Nave, Thomas Schneider, Klemens Ruprecht, and Philipp Euskirchen. The spectrum of central nervous system involvement in whipple's disease. European Journal of Neurology, 30:3417-3429, Aug 2023. URL: https://doi.org/10.1111/ene.15511, doi:10.1111/ene.15511. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (tison2021rheumatologicalfeaturesof pages 3-4): Alice Tison, Pauline Preuss, Clémentine Leleu, François Robin, Adrien Le Pluart, Justine Vix, Guillaume Le Mélédo, Philippe Goupille, Elisabeth Gervais, Grégoire Cormier, Jean-David Albert, Aleth Perdriger, Béatrice Bouvard, Jean-Marie Berthelot, Nathan Foulquier, and Alain Saraux. Rheumatological features of whipple disease. Scientific Reports, Jun 2021. URL: https://doi.org/10.1038/s41598-021-91671-9, doi:10.1038/s41598-021-91671-9. This article has 39 citations and is from a peer-reviewed journal.

14. (marth2016tropherymawhippleiinfection pages 6-7): Thomas Marth, Verena Moos, Christian Müller, Federico Biagi, and Thomas Schneider. Tropheryma whipplei infection and whipple's disease. The Lancet. Infectious diseases, 16 3:e13-22, Mar 2016. URL: https://doi.org/10.1016/s1473-3099(15)00537-x, doi:10.1016/s1473-3099(15)00537-x. This article has 251 citations.

15. (dolmans2017clinicalmanifestationstreatment pages 18-20): Ruben A. V. Dolmans, C. H. Edwin Boel, Miangela M. Lacle, and Johannes G. Kusters. Clinical manifestations, treatment, and diagnosis of tropheryma whipplei infections. Clinical Microbiology Reviews, 30:529-555, Apr 2017. URL: https://doi.org/10.1128/cmr.00033-16, doi:10.1128/cmr.00033-16. This article has 245 citations and is from a highest quality peer-reviewed journal.

16. (schiepatti2020longtermmorbidityand pages 6-7): Annalisa Schiepatti, Maria Luisa Nicolardi, Piero Marone, and Federico Biagi. Long-term morbidity and mortality in whipple's disease: a single-center experience over 20 years. Future microbiology, 15:847-854, Jul 2020. URL: https://doi.org/10.2217/fmb-2019-0315, doi:10.2217/fmb-2019-0315. This article has 12 citations and is from a peer-reviewed journal.

17. (hujoel2019tropherymawhippleiinfection pages 1-2): Isabel A. Hujoel, David H. Johnson, Benjamin Lebwohl, Daniel Leffler, Sonia Kupfer, Tsung-Teh Wu, Joseph A. Murray, and Alberto Rubio-Tapia. Tropheryma whipplei infection (whipple disease) in the usa. Digestive Diseases and Sciences, 64:213-223, Mar 2019. URL: https://doi.org/10.1007/s10620-018-5033-4, doi:10.1007/s10620-018-5033-4. This article has 62 citations and is from a peer-reviewed journal.

18. (ye2023whipple’sdiseasepresenting pages 2-5): Haiyan Ye, Xiao Hu, Tommy Richard Sun-Wing Tong, Shuang Chen, Tao Li, Fanfan Xing, Jasper Fuk-Woo Chan, Kwok-Yung Yuen, and Kelvin Hei-Yeung Chiu. Whipple’s disease presenting as weight gain and constipation in a chinese woman. BMC Infectious Diseases, May 2023. URL: https://doi.org/10.1186/s12879-023-08276-y, doi:10.1186/s12879-023-08276-y. This article has 2 citations and is from a peer-reviewed journal.

19. (dolmans2017clinicalmanifestationstreatment pages 1-3): Ruben A. V. Dolmans, C. H. Edwin Boel, Miangela M. Lacle, and Johannes G. Kusters. Clinical manifestations, treatment, and diagnosis of tropheryma whipplei infections. Clinical Microbiology Reviews, 30:529-555, Apr 2017. URL: https://doi.org/10.1128/cmr.00033-16, doi:10.1128/cmr.00033-16. This article has 245 citations and is from a highest quality peer-reviewed journal.

20. (dolmans2017clinicalmanifestationstreatment pages 7-8): Ruben A. V. Dolmans, C. H. Edwin Boel, Miangela M. Lacle, and Johannes G. Kusters. Clinical manifestations, treatment, and diagnosis of tropheryma whipplei infections. Clinical Microbiology Reviews, 30:529-555, Apr 2017. URL: https://doi.org/10.1128/cmr.00033-16, doi:10.1128/cmr.00033-16. This article has 245 citations and is from a highest quality peer-reviewed journal.

21. (marth2016tropherymawhippleiinfection pages 2-3): Thomas Marth, Verena Moos, Christian Müller, Federico Biagi, and Thomas Schneider. Tropheryma whipplei infection and whipple's disease. The Lancet. Infectious diseases, 16 3:e13-22, Mar 2016. URL: https://doi.org/10.1016/s1473-3099(15)00537-x, doi:10.1016/s1473-3099(15)00537-x. This article has 251 citations.

22. (dolmans2017clinicalmanifestationstreatment pages 5-7): Ruben A. V. Dolmans, C. H. Edwin Boel, Miangela M. Lacle, and Johannes G. Kusters. Clinical manifestations, treatment, and diagnosis of tropheryma whipplei infections. Clinical Microbiology Reviews, 30:529-555, Apr 2017. URL: https://doi.org/10.1128/cmr.00033-16, doi:10.1128/cmr.00033-16. This article has 245 citations and is from a highest quality peer-reviewed journal.

23. (dolmans2017clinicalmanifestationstreatment pages 10-12): Ruben A. V. Dolmans, C. H. Edwin Boel, Miangela M. Lacle, and Johannes G. Kusters. Clinical manifestations, treatment, and diagnosis of tropheryma whipplei infections. Clinical Microbiology Reviews, 30:529-555, Apr 2017. URL: https://doi.org/10.1128/cmr.00033-16, doi:10.1128/cmr.00033-16. This article has 245 citations and is from a highest quality peer-reviewed journal.

24. (song2023currentknowledgeof pages 7-9): Xiangyi Song, Ruifeng Duan, Liwei Duan, and Lijuan Wei. Current knowledge of the immune reconstitution inflammatory syndrome in whipple disease: a review. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1265414, doi:10.3389/fimmu.2023.1265414. This article has 10 citations and is from a peer-reviewed journal.

25. (mecklenburg2023thespectrumof pages 8-9): Jasper Mecklenburg, Verena Moos, Annette Moter, Eberhard Siebert, Alexander Heinrich Nave, Thomas Schneider, Klemens Ruprecht, and Philipp Euskirchen. The spectrum of central nervous system involvement in whipple's disease. European Journal of Neurology, 30:3417-3429, Aug 2023. URL: https://doi.org/10.1111/ene.15511, doi:10.1111/ene.15511. This article has 11 citations and is from a domain leading peer-reviewed journal.

26. (mecklenburg2023thespectrumof pages 2-3): Jasper Mecklenburg, Verena Moos, Annette Moter, Eberhard Siebert, Alexander Heinrich Nave, Thomas Schneider, Klemens Ruprecht, and Philipp Euskirchen. The spectrum of central nervous system involvement in whipple's disease. European Journal of Neurology, 30:3417-3429, Aug 2023. URL: https://doi.org/10.1111/ene.15511, doi:10.1111/ene.15511. This article has 11 citations and is from a domain leading peer-reviewed journal.

27. (dolmans2017clinicalmanifestationstreatment pages 13-17): Ruben A. V. Dolmans, C. H. Edwin Boel, Miangela M. Lacle, and Johannes G. Kusters. Clinical manifestations, treatment, and diagnosis of tropheryma whipplei infections. Clinical Microbiology Reviews, 30:529-555, Apr 2017. URL: https://doi.org/10.1128/cmr.00033-16, doi:10.1128/cmr.00033-16. This article has 245 citations and is from a highest quality peer-reviewed journal.

28. (viegas2023whyiswhipples pages 7-7): Ana Filipa Viegas, Andreia M Lopes, Gabriela Venade, Pedro Rodrigues, and João Tavares. Why is whipple's disease still a challenging diagnosis? a case report and brief review of literature. Cureus, Jan 2023. URL: https://doi.org/10.7759/cureus.34029, doi:10.7759/cureus.34029. This article has 7 citations.

29. (mecklenburg2023thespectrumof pages 6-7): Jasper Mecklenburg, Verena Moos, Annette Moter, Eberhard Siebert, Alexander Heinrich Nave, Thomas Schneider, Klemens Ruprecht, and Philipp Euskirchen. The spectrum of central nervous system involvement in whipple's disease. European Journal of Neurology, 30:3417-3429, Aug 2023. URL: https://doi.org/10.1111/ene.15511, doi:10.1111/ene.15511. This article has 11 citations and is from a domain leading peer-reviewed journal.

30. (zhou2024shorttermamoxicillinclavulanate pages 1-2): Hongyuan Zhou and Jian Zhang. Short-term amoxicillin clavulanate in the treatment of pulmonary abscess caused by tropheryma whipplei infection diagnosed by targeted next-generation sequencing: a case report and literature review. Infection and Drug Resistance, 17:4607-4616, Oct 2024. URL: https://doi.org/10.2147/idr.s488740, doi:10.2147/idr.s488740. This article has 6 citations and is from a peer-reviewed journal.
