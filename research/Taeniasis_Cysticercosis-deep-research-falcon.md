---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T16:53:43.058419'
end_time: '2026-04-04T17:09:12.996470'
duration_seconds: 929.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Taeniasis/cysticercosis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 68
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Taeniasis/cysticercosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Taeniasis/cysticercosis** covering all of the
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
- **Disease Name:** Taeniasis/cysticercosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Taeniasis/cysticercosis** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Taeniasis/Cysticercosis (Taenia solium disease complex)

### Executive summary (2023–2024 emphasis)
Taeniasis/cysticercosis is a zoonotic, food- and fecal–oral–transmitted disease complex caused primarily by *Taenia solium* (pork tapeworm) in which humans act as definitive hosts (intestinal tapeworm; taeniasis) and can also become accidental intermediate hosts (tissue cysticercosis), including infection of the central nervous system (neurocysticercosis; NCC). The most important clinical burden arises from NCC-associated seizures/epilepsy and complications of extraparenchymal disease such as hydrocephalus. Recent (2023–2024) work highlights (i) persistent high community prevalence in parts of sub-Saharan Africa with many asymptomatic infections, (ii) improving but still limited diagnostic accessibility, with multiple high-performing immunodiagnostic platforms under validation, (iii) strong effectiveness signals for albendazole + praziquantel combination regimens in active disease, and (iv) increasing real‑world implementation evidence for mass treatment of taeniasis with niclosamide as a transmission-interruption tool. (zulu2023theepidemiologyof pages 1-2, larkins2023thechallengesof pages 1-2, acker2024accuracyofimmunological pages 7-10, stelzle2023efficacyandsafety pages 1-2, wardle2024masschemotherapywith pages 1-2, zulu2024neurocysticercosisprevalenceand pages 1-2)

| Domain | Key finding/statistic | Setting/population | Notes on methods | Source (author year journal) | URL/DOI |
|---|---|---|---|---|---|
| Definition | *Taenia solium* causes taeniosis in humans (adult intestinal tapeworm) and cysticercosis in humans and pigs; neurocysticercosis (NCC) is CNS infection by larval cysticerci and is a major cause of epilepsy in endemic regions (zulu2023theepidemiologyof pages 1-2, larkins2023thechallengesof pages 1-2, aderinto2024neurocysticercosisandthe pages 1-2) | Human and pig host cycle; endemic LMIC settings | Review/systematic-review definitions synthesizing host roles and transmission biology | Zulu 2023 *PLoS Negl Trop Dis*; Larkins 2023 *Trop Med Int Health* | https://doi.org/10.1371/journal.pntd.0011042 ; https://doi.org/10.1111/tmi.13870 |
| Epidemiology | In Sinda District, Zambia, cysticercosis seroprevalence was estimated at 20.1% and NCC prevalence at 13.5%; among people reporting epileptic seizures, NCC prevalence was 38.0% (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8) | 1,249 community participants with POC testing; 233 received CT | Cross-sectional study with TS POC screening followed by clinical evaluation and cerebral CT | Zulu 2024 *J Epidemiol Glob Health* | https://doi.org/10.1007/s44197-024-00271-z |
| Epidemiology | In Starr County, Texas, cysticercosis seroprevalence was 7.4% (45/605); calcified NCC-compatible lesions were found in 2/45 seropositive individuals (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8) | Mexican-American adults on the Texas–Mexico border | Cross-sectional serosurvey with follow-up brain imaging among seropositive participants | Duffey 2024 *Pathogens* | https://doi.org/10.3390/pathogens13110988 |
| Epidemiology | In Mbulu District, Tanzania, human cysticercosis prevalence was 7.67% (23/300); infection tended to be lower among prior anthelmintic users, though not statistically significant (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8) | Community participants aged 5–89 years | Baseline community study using Ag-ELISA plus household risk-factor assessment | Bandi 2024 *Zoonotic Diseases* | https://doi.org/10.3390/zoonoticdis4020013 |
| Epidemiology | Eastern and Southern Africa review found wide ranges: cysticercosis seroprevalence 0.7–40.8% by Ag-ELISA, 13.1–45.3% by Ab-ELISA; taeniosis prevalence by microscopy 0.1–14.7%; NCC-suggestive CT lesions 1.0–76% (zulu2023theepidemiologyof pages 1-2, zulu2023theepidemiologyof pages 9-10) | 16 of 27 countries in Eastern/Southern Africa | Systematic review of 113 reports (2000–2022 literature) highlighting large geographic heterogeneity and surveillance gaps | Zulu 2023 *PLoS Negl Trop Dis* | https://doi.org/10.1371/journal.pntd.0011042 |
| Phenotype | Seizures were the most frequent presentation in European NCC cases: 59% overall in abstracted cases; headache occurred in 52%; other neurological signs/symptoms in 54%; outcome favorable in 90% (stelzle2023clinicalcharacteristicsand pages 6-10) | 293 NCC cases diagnosed/treated in Europe (2000–2019) | Retrospective assessment of published and unpublished cases; all had neuroimaging | Stelzle 2023 *J Travel Med* | https://doi.org/10.1093/jtm/taac102 |
| Phenotype | Across updated 2008–2023 NCC literature, epileptic seizures and headache remained the most frequent manifestations; pooled headache frequency increased to 45.1% versus 36.2% in earlier review (figuet2024distributiondesmanifestations pages 85-90, figuet2024distributiondesmanifestationsa pages 85-90) | People diagnosed with NCC across 63 included studies | Systematic review/meta-analysis; mortality too heterogeneous to pool; limited longitudinal natural-history data | Figuet 2024 systematic review/meta-analysis | Not available in gathered evidence |
| Phenotype/Pathophysiology | In a large Peru calcified NCC cohort, 79.2% had previous seizures; median number of calcifications was 3 and frontal lobe location was most common (79%) (bustos2023calcifiedneurocysticercosisdemographic pages 2-4) | 524 hospital-based patients with calcified NCC in Peru | Cohort of CT-defined calcified NCC; combined clinical, imaging, EEG, and serology/antigen testing | Bustos 2023 *Pathogens* | https://doi.org/10.3390/pathogens13010026 |
| Diagnostics | Neuroimaging (CT/MRI) remains the definitive modality for NCC diagnosis; immunological tests are supportive, especially where imaging access is limited (toribio2024fromlaboratoryto pages 1-2, toribio2024fromlaboratoryto pages 11-12) | Endemic/resource-limited settings and specialty centers | 2024 diagnostic review summarizing clinical translation of immunologic and molecular tools | Toribio 2024 *Front Parasitol* | https://doi.org/10.3389/fpara.2024.1394089 |
| Diagnostics | LLGP Western blot showed high sensitivity for parenchymal active multiple cysts (81.1–100%) but much lower sensitivity for single cysts (<62.6%); specificity was 92.3–100% (acker2024accuracyofimmunological pages 7-10) | Studies mainly from South America and South/Southeast Asia | 2024 systematic review of 53 studies / 123 tests; major heterogeneity and risk-of-bias issues | Van Acker 2024 *PLoS Negl Trop Dis* | https://doi.org/10.1371/journal.pntd.0012643 |
| Diagnostics | A multi-antigen print immunoassay (MAPIA) reported 100% sensitivity for active single and multiple parenchymal cysts and 98.5% specificity, though based on small samples (acker2024accuracyofimmunological pages 10-11) | NCC diagnostic studies | Promising assay under evaluation; not yet established as routine standard | Van Acker 2024 *PLoS Negl Trop Dis* | https://doi.org/10.1371/journal.pntd.0012643 |
| Diagnostics | DOT-ELISA and urine-based tests showed promising performance: e.g., urine dipstick sensitivity 96.7% and specificity 100.0% in subarachnoid NCC controls, but further validation is needed (acker2024accuracyofimmunological pages 22-23) | Subarachnoid/extraparenchymal-focused diagnostic subsets | Review of rapid/POC and alternative-antigen assays; implementation evidence still limited | Van Acker 2024 *PLoS Negl Trop Dis* | https://doi.org/10.1371/journal.pntd.0012643 |
| Treatment | In rural Tanzania, albendazole monotherapy resolved or calcified 42% of 138 cysts by end of follow-up; among patients later receiving albendazole + praziquantel, 63 of 66 cysts (95%) resolved; seizure frequency declined significantly (p<0.001), with infrequent mild–moderate adverse events (stelzle2023clinicalcharacteristicsand pages 6-10) | 63 NCC patients in Tanzania; 17 completed albendazole-only follow-up, 8 received combination therapy | Prospective cohort, 2018–2022; antiparasitic therapy accompanied by corticosteroids and anti-seizure medication as indicated | Stelzle 2023 *Infection* | https://doi.org/10.1007/s15010-023-02021-y |
| Treatment | Pediatric systematic review found higher complete lesion resolution with albendazole + praziquantel than albendazole alone: 62% vs 26.3% at 6 months in one trial (dewi2024effectivenessofthe pages 4-5) | Children with NCC in randomized comparative studies | 2024 systematic review/meta-analysis of pediatric evidence; lesion resolution and calcification outcomes extracted | Dewi 2024 *Cureus* | https://doi.org/10.7759/cureus.64617 |
| Treatment/Surgery | For hydrocephalus in extraparenchymal NCC, endoscopic third ventriculostomy reported symptom resolution in 70–95%; shunt/endoscopy choice depends on anatomy and local expertise (filho2024currentroleof pages 4-6, filho2024currentroleof media 744e0baf) | Patients with hydrocephalus/intraventricular or extraparenchymal NCC | Narrative surgical review; figures illustrate VP shunt failure versus successful endoscopic cyst removal/ETV | Hamamoto Filho 2024 *Pathogens* | https://doi.org/10.3390/pathogens13030218 |
| Prevention/Control | Mass niclosamide chemotherapy was evaluated as a safe and effective population-based control strategy for *T. solium* transmission (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8) | Population-based control program in the Americas | 2024 field implementation study emphasizing taeniasis control to interrupt the life cycle | Wardle 2024 *Lancet Reg Health Am* | https://doi.org/10.1016/j.lana.2024.100876 |
| Prevention/Control | Community knowledge is often poor: in Thailand, 98.3% of respondents had less accurate knowledge despite many reporting generally correct preventive practices; older age and some municipal settings predicted poorer practice scores (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8) | 360 respondents in Pak Chong District, Thailand | Cross-sectional KAP survey supporting education as a prevention pillar | Phumrattanaprapin 2024 *PLoS One* | https://doi.org/10.1371/journal.pone.0307240 |
| Prevention/Control | The Vicious Worm educational tool significantly improved community health worker knowledge on *T. solium* cysticercosis in Rwanda (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8) | 207 community health workers in Nyamagabe District, Rwanda | Mixed-methods evaluation before, immediately after, and 4 weeks after training | Uwibambe 2024 *PLoS Negl Trop Dis* | https://doi.org/10.1371/journal.pntd.0012140 |
| Trials | NCT02612896 compared elimination vs control strategies in Zambia; elimination arm combined repeated human praziquantel MDA, health education, and pig treatment/vaccination; status completed; study completion Feb 2022 (NCT02612896 chunk 1, NCT02612896 chunk 2) | ~2,900 participants in Katete district, Zambia | Non-randomized parallel One Health community intervention with pig and human outcomes tracked over years | Institute of Tropical Medicine Belgium, ClinicalTrials.gov 2016 | https://clinicaltrials.gov/study/NCT02612896 |
| Trials | NCT02947581 (SANTO) tested albendazole + praziquantel vs albendazole + placebo for basal subarachnoid NCC; 107 enrolled; primary completion Aug 2020; terminated because placebo supply became unavailable (NCT02947581 chunk 2, NCT02947581 chunk 1) | Adults 18–65 with subarachnoid NCC in Peru/Brazil/Ecuador sites | Phase 3 double-blind randomized placebo-controlled trial; MRI parasite-volume reduction was the primary endpoint | Universidad Peruana Cayetano Heredia, ClinicalTrials.gov 2016 | https://clinicaltrials.gov/study/NCT02947581 |
| Trials | NCT01296958 evaluated targeted screening for intestinal *T. solium* tapeworm carriers plus niclosamide treatment versus community education; 1,811 enrolled; completed Jan 2013 (NCT01296958 chunk 1) | Community members in Peru | Non-randomized parallel screening/control strategy trial with porcine seroprevalence and tapeworm prevalence outcomes | Oregon Health & Science University, ClinicalTrials.gov 2011 | https://clinicaltrials.gov/study/NCT01296958 |


*Table: This table compiles the most decision-relevant 2023-2024 evidence on Taenia solium taeniasis/cysticercosis/neurocysticercosis across definitions, epidemiology, phenotype, diagnostics, treatment, prevention, and interventional trials. It is useful as a concise evidence map for building a disease knowledge base entry or research summary.*

---

## 1. Disease information

### 1.1 What is the disease? (definitions and scope)
**Taeniasis** is intestinal infection with the adult *Taenia* tapeworm in humans, acquired by eating raw/undercooked meat containing viable larval cysts (cysticerci). (larkins2023thechallengesof pages 1-2, aderinto2024neurocysticercosisandthe pages 8-9)

**Cysticercosis** is tissue infection with larval cysticerci acquired by ingestion of *Taenia* eggs; for *T. solium*, humans can become accidental intermediate hosts after ingesting eggs shed by a human tapeworm carrier. (aderinto2024neurocysticercosisandthe pages 1-2, aderinto2024neurocysticercosisandthe pages 8-9)

**Neurocysticercosis (NCC)** is cysticercosis involving the central nervous system (brain/spinal cord and associated spaces). NCC is emphasized as a leading (often preventable) cause of epilepsy in endemic regions. (zulu2023theepidemiologyof pages 1-2, larkins2023thechallengesof pages 1-2, aderinto2024neurocysticercosisandthe pages 7-8)

Direct abstract-supported statement (2024): “Neurocysticercosis (NCC) is caused by the invasion of *Taenia solium* larvae in the central nervous system (CNS) and stands as the predominant cause of epilepsy and other neurological disorders in many developing nations.” (toribio2024fromlaboratoryto pages 1-2)

### 1.2 Synonyms and alternative names
- “*Taenia solium* taeniasis/cysticercosis” (often abbreviated **TSTC**) (hossain2023insightsintothe pages 4-6)
- “Human cysticercosis (HC/HCC)” for non-CNS tissue cysticercosis (zulu2023theepidemiologyof pages 1-2)
- “Porcine cysticercosis (PCC)” for pig infection (hossain2023insightsintothe pages 4-6)

### 1.3 Key identifiers (ICD/MeSH/MONDO/Orphanet)
The retrieved full-text corpus used here did **not** include explicit ICD‑10/ICD‑11 codes, MeSH IDs, MONDO IDs, or Orphanet IDs in the accessible text excerpts. This is therefore a **current evidence gap in this tool-backed retrieval run** and should be supplemented from authoritative terminologies (WHO ICD-11 browser; NLM MeSH; MONDO/OBO Foundry; Orphanet) in a subsequent curation step. (zulu2023theepidemiologyof pages 1-2, toribio2024fromlaboratoryto pages 1-2)

### 1.4 Evidence source type
Information synthesized here is derived from **aggregated disease-level resources** (systematic reviews, narrative reviews, cohort/cross-sectional studies, and ClinicalTrials.gov registry records) rather than individual EHR-derived phenotyping. (zulu2023theepidemiologyof pages 1-2, acker2024accuracyofimmunological pages 7-10, NCT02947581 chunk 1)

---

## 2. Etiology

### 2.1 Causal factors
- Infectious cause: *Taenia solium* (pork tapeworm) is the principal cause of the taeniasis/cysticercosis complex with major neurologic disease burden from NCC. (aderinto2024neurocysticercosisandthe pages 1-2, larkins2023thechallengesof pages 1-2)

### 2.2 Transmission and risk factors (gene–environment framing)
**Core transmission biology:**
- Taeniasis follows ingestion of cysticerci in undercooked meat; cysticercosis follows ingestion of eggs, including via contaminated water/vegetables/hands/fomites. Eggs are infectious immediately and can persist for months under favorable conditions. (aderinto2024neurocysticercosisandthe pages 3-4, aderinto2024neurocysticercosisandthe pages 8-9)
- Humans are definitive hosts for *T. solium* and can also act as intermediate hosts; pigs are key intermediate hosts for the zoonotic cycle. (aderinto2024neurocysticercosisandthe pages 1-2, zulu2023theepidemiologyof pages 1-2)

**Environmental/behavioral risk factors emphasized in recent literature** include inadequate sanitation, poor hygiene/handwashing infrastructure, unsafe water sources, and pig husbandry practices that permit pigs to access human feces/sewage—factors repeatedly invoked as drivers of household clustering and endemic persistence. (aderinto2024neurocysticercosisandthe pages 8-9, larkins2023thechallengesof pages 2-3, zulu2024neurocysticercosisprevalenceand pages 4-6)

**Epidemiologic risk-factor estimate (2024, Zambia):** small-scale farming was associated with higher odds of NCC (OR 5.28, 95% CI 1.56–17.86). (zulu2024neurocysticercosisprevalenceand pages 4-6)

### 2.3 Protective factors
Evidence in the retrieved texts supports protective effects of **breaking transmission** through:
- Safe cooking/freezing of meat to kill cysticerci (e.g., cooking to ~60–65°C, freezing schedules) (aderinto2024neurocysticercosisandthe pages 3-4, aderinto2024neurocysticercosisandthe pages 8-9)
- Treating human tapeworm carriers (taeniasis) and implementing One Health interventions targeting pigs and sanitation. (aderinto2024neurocysticercosisandthe pages 8-9, hossain2023insightsintothe pages 4-6)

A community study in Tanzania reported lower likelihood of cysticercosis among people who had taken anthelmintics, though this reduction was not statistically significant in that dataset. (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8)

### 2.4 Genetic risk/protective factors and GxE
No robust human susceptibility loci, protective variants, or gene–environment interaction evidence was present in the retrieved excerpts; for this disease complex, the dominant drivers are infectious exposure and socio-environmental determinants. This is an evidence gap for the requested template. (zulu2023theepidemiologyof pages 1-2)

---

## 3. Phenotypes

### 3.1 Major clinical phenotypes and frequencies (humans)
**Neurocysticercosis (NCC):**
- Seizures/epilepsy are the most frequent presentation. A large European retrospective assessment reported seizures as the initial presentation in 59% overall (and higher in children), with headache in 52% and other neurologic signs/symptoms in 54%; outcome was favorable in 90%. (stelzle2023clinicalcharacteristicsand pages 6-10)
- A 2024 systematic review/meta-analysis (2008–2023) reported that seizures and headaches remain the most frequent manifestations; headache frequency in pooled summaries increased to 45.1% compared with 36.2% in an earlier period. (figuet2024distributiondesmanifestations pages 85-90)

**Calcified NCC phenotype (Peru cohort):**
In a large hospital-based cohort of calcified NCC (n=524), 79.2% had previous seizures; calcifications were often frontal (79%); the cohort illustrates heterogeneity in burden and manifestations. (bustos2023calcifiedneurocysticercosisdemographic pages 2-4)

**Population-level symptomatic fraction (2024, Zambia):**
In a community-based study, NCC prevalence was 13.5%, but only 16% of people with NCC had ever experienced epileptic seizures, emphasizing frequent asymptomatic infection. (zulu2024neurocysticercosisprevalenceand pages 1-2)

### 3.2 Phenotype characteristics (age of onset, severity, progression)
Progression is dominated by parasite stage and location:
- Parenchymal cysts can be vesicular (often minimal inflammation) and later become degenerating lesions with inflammation/edema; eventual granuloma and calcification may persist lifelong and remain epileptogenic in some individuals. (singh2024seizuresandepilepsy pages 1-3, bustos2023calcifiedneurocysticercosisdemographic pages 1-2)
- Extraparenchymal disease (subarachnoid/ventricular) is associated with raised intracranial pressure and hydrocephalus, often requiring neurosurgical intervention. (filho2024currentroleof pages 4-6, stelzle2023clinicalcharacteristicsand pages 6-10)

### 3.3 Suggested HPO terms (examples; ontology IDs to be confirmed during curation)
Based on the reported phenotypes, suggested HPO concepts include:
- Seizures / Epileptic seizures; focal to bilateral tonic-clonic seizures (bustos2023calcifiedneurocysticercosisdemographic pages 2-4, stelzle2023clinicalcharacteristicsand pages 6-10)
- Headache (stelzle2023clinicalcharacteristicsand pages 6-10)
- Hydrocephalus / intracranial hypertension / papilledema (hydrocephalus is explicitly frequent in extraparenchymal disease; papilledema present in case descriptions) (stelzle2023clinicalcharacteristicsand pages 6-10, filho2024currentroleof pages 4-6)
- Perilesional edema (imaging phenotype) (stelzle2023clinicalcharacteristicsand pages 6-10, singh2024seizuresandepilepsy pages 1-3)
- Cognitive decline / higher brain function impairment (figuet2024distributiondesmanifestations pages 85-90, bustos2023calcifiedneurocysticercosisdemographic pages 1-2)

Because HPO IDs are not included in the retrieved texts, these are *conceptual mappings* requiring validation against the HPO database.

### 3.4 Quality-of-life impact
In a prospective Tanzania cohort, epilepsy-related quality of life (QOLIE-31) improved after treatment (median 87 to 95; p=0.02). (stelzle2023efficacyandsafety pages 7-10)

---

## 4. Genetic/Molecular information

### 4.1 Human causal genes and pathogenic variants
Not applicable in the classic Mendelian sense: taeniasis/cysticercosis is an infectious disease complex. No human causal genes/variants were provided in the retrieved evidence. (zulu2023theepidemiologyof pages 1-2)

### 4.2 Parasite molecular targets (contextual)
Recent diagnostics and control tools emphasize recombinant/synthetic antigens and monoclonal antibody targets for immunodiagnostics and vaccine development (e.g., pig vaccine TSOL18 is discussed in reviews), but specific gene symbols/IDs were not present in the retrieved excerpts. (hossain2023insightsintothe pages 4-6, toribio2024fromlaboratoryto pages 1-2)

---

## 5. Environmental information

Key environmental factors driving transmission are sanitation and water quality, and pig husbandry practices enabling fecal contamination of the environment and pig exposure. These factors are repeatedly cited as central to endemic persistence and a focus of One Health control. (aderinto2024neurocysticercosisandthe pages 8-9, zulu2024neurocysticercosisprevalenceand pages 4-6)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (upstream → downstream)
1. **Exposure:** ingestion of eggs (→ cysticercosis) or cysticerci (→ taeniasis). (aderinto2024neurocysticercosisandthe pages 8-9)
2. **CNS invasion (NCC):** larvae lodge in parenchyma, subarachnoid space, ventricles, or spinal cord. (singh2024seizuresandepilepsy pages 1-3)
3. **Stage-dependent host response:** vesicular stage may have minimal inflammation; immune attack drives **degeneration** with enhancement and perilesional edema. (singh2024seizuresandepilepsy pages 1-3)
4. **Clinical manifestations:** inflammatory edema and lesion location contribute to seizures; extraparenchymal disease contributes to arachnoiditis and CSF obstruction → hydrocephalus/intracranial hypertension. (singh2024seizuresandepilepsy pages 1-3, filho2024currentroleof pages 4-6)
5. **Long-term sequelae:** calcified nodules can persist lifelong and remain seizure foci; mechanisms proposed include gliosis, blood–brain barrier disruption, and axonal damage. (bustos2023calcifiedneurocysticercosisdemographic pages 1-2, bustos2023calcifiedneurocysticercosisdemographic pages 2-4)

### 6.2 Mechanistic themes emphasized by authoritative 2023–2024 sources
- A 2024 Neurology review links seizure occurrence to evolutionary stage, highlighting inflammation/edema in degenerating lesions and ongoing seizure risk even with calcified lesions. (singh2024seizuresandepilepsy pages 1-3)
- Extraparenchymal NCC is increasingly recognized as proportionally more frequent and often more severe; medical therapy responses are variable and neurosurgical management is often required. (filho2024currentroleof pages 4-6)

### 6.3 Suggested GO biological process / CL cell types (conceptual)
The retrieved evidence points to inflammation and edema but does not enumerate specific immune pathways/cell subsets. Conceptual GO/CL mappings (requiring database validation) include:
- GO: inflammatory response; leukocyte migration; regulation of cytokine production; blood–brain barrier organization/disruption (bustos2023calcifiedneurocysticercosisdemographic pages 2-4)
- CL: microglia, astrocytes, endothelial cells, lymphocytes (inferred from “lymphocyte infiltration” and CNS inflammation discussions) (oliveira2024murineextraparenchymalneurocysticercosis pages 6-7)

No transcriptomics/proteomics/metabolomics signatures were available in the retrieved excerpts.

---

## 7. Anatomical structures affected

### 7.1 Organ-level and localization
- CNS sites: brain parenchyma, subarachnoid space, ventricles, spinal cord. (singh2024seizuresandepilepsy pages 1-3)
- Human cysticercosis can also involve muscle, subcutaneous tissue, eye, and other organs (reported as possible sites in reviews). (aderinto2024neurocysticercosisandthe pages 7-8)

**UBERON suggestions (conceptual):** brain, spinal cord, ventricular system, subarachnoid space/meninges, skeletal muscle, eye. (aderinto2024neurocysticercosisandthe pages 7-8, singh2024seizuresandepilepsy pages 1-3)

### 7.2 Subcellular localization
Not specified in retrieved excerpts.

---

## 8. Temporal development

- Prepatent period for taeniid cestodes is noted as ~1–3 months; adult worms may live years. (aderinto2024neurocysticercosisandthe pages 3-4)
- NCC lesion evolution over time follows vesicular → degenerating/colloidal with inflammation → granuloma → calcification; seizures may occur at any stage. (singh2024seizuresandepilepsy pages 1-3)

Detailed stage durations and longitudinal natural history remain poorly synthesized due to limited community-based longitudinal studies, as emphasized by a 2024 meta-analysis. (figuet2024distributiondesmanifestations pages 85-90)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
**Zambia (2024, community-based):**
- TS POC cysticercosis-positive: 14% (177/1249)
- Estimated cysticercosis seroprevalence: 20.1% (95% CI 14.6–27.0)
- NCC prevalence: 13.5% (95% CI 8.4–21.1)
- Active NCC prevalence: 1.1% (95% CI 0.6–2.0)
- NCC associated with higher odds of epileptic seizures: OR 3.98 (95% CI 1.34–11.78) (zulu2024neurocysticercosisprevalenceand pages 1-2, zulu2024neurocysticercosisprevalenceand pages 4-6)

**Eastern & Southern Africa evidence base (systematic review, 2023):**
Cysticercosis seroprevalence and CT-based NCC lesion prevalence vary widely (Ag-ELISA up to 40.8%; NCC-suggestive CT lesions up to 76% in selected populations), indicating extreme heterogeneity and surveillance gaps. (zulu2023theepidemiologyof pages 1-2, zulu2023theepidemiologyof pages 9-10)

**United States border community (2024):**
Cysticercosis seroprevalence 7.4% (45/605) in Starr County, Texas; calcified NCC-compatible lesions in 2/45 seropositive individuals. (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8)

### 9.2 Demographics
In a large calcified NCC cohort in Peru, mean age at enrollment was ~40 years and symptom onset ~29 years; women comprised 56.3%. (bustos2023calcifiedneurocysticercosisdemographic pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical criteria and imaging
- **Neuroimaging (CT/MRI) is fundamental/definitive** for NCC diagnosis; immunologic tests are supportive and may be limited by stage and access. (toribio2024fromlaboratoryto pages 1-2)
- A 2024 Zambia community study applied **revised Del Brutto criteria** and staged lesions as active (vesicular/degenerating) vs inactive (calcified). (zulu2024neurocysticercosisprevalenceand pages 2-4)

### 10.2 Immunodiagnostics (2024 systematic review)
A 2024 systematic review synthesized 53 studies with 123 tests; major points include:
- LLGP Western blot sensitivity 81.1–100% for parenchymal active multiple cysts, but <62.6% for single cysts; specificity 92.3–100%. (acker2024accuracyofimmunological pages 7-10)
- A multi-antigen print immunoassay (MAPIA) reported 100% sensitivity for active single/multiple parenchymal cysts and 98.5% specificity (small-sample evidence). (acker2024accuracyofimmunological pages 10-11)
- Antigen detection tests (including urine-based assays) showed high sensitivity for extraparenchymal disease in some studies (e.g., urine dipstick sensitivity 96.7%, specificity 100% in a small evaluation). (acker2024accuracyofimmunological pages 22-23)

### 10.3 Molecular diagnostics
Recent reviews describe exploration of molecular diagnostics, but quantitative performance data were not provided in the retrieved excerpts. (toribio2024fromlaboratoryto pages 11-12, toribio2024fromlaboratoryto pages 13-13)

### 10.4 Screening
Population screening strategies include point-of-care serology followed by targeted CT, as implemented in the Zambia study. (zulu2024neurocysticercosisprevalenceand pages 1-2)

---

## 11. Outcome / prognosis

- In a European retrospective compilation, outcomes were favorable in 90% of cases. (stelzle2023clinicalcharacteristicsand pages 6-10)
- Prognosis varies strongly by lesion location (parenchymal vs extraparenchymal), stage (active vs calcified), and complication burden (e.g., hydrocephalus). (filho2024currentroleof pages 4-6, singh2024seizuresandepilepsy pages 1-3)

Mortality estimates were too heterogeneous for pooling in a 2024 meta-analysis, underscoring gaps in standardized outcome reporting. (figuet2024distributiondesmanifestations pages 85-90)

---

## 12. Treatment

### 12.1 Pharmacotherapy (active NCC)
**Albendazole ± praziquantel:**
- Tanzania prospective cohort (2023): albendazole monotherapy (15 mg/kg/day for 10 days) led to 58/138 cysts (42%) disappearing or calcifying by follow-up; median seizure frequency decreased from 4/year to 0/year (p<0.001). In those requiring escalation, albendazole + praziquantel (50 mg/kg/day) resolved 63/66 cysts (95%) and was generally well tolerated; combination therapy headaches occurred in 3/8 patients, with otherwise stable vitals/labs. (stelzle2023efficacyandsafety pages 1-2, stelzle2023efficacyandsafety pages 6-7)
- Pediatric evidence synthesis (2024): in one trial summarized in a meta-analysis, complete lesion resolution at 6 months was 62% with albendazole + praziquantel versus 26.3% with albendazole monotherapy. (dewi2024effectivenessofthe pages 4-5)

**Taeniasis treatment and preventive chemotherapy:**
Niclosamide is commonly used to treat intestinal tapeworm carriage and can be deployed at scale (see prevention/control). (NCT01296958 chunk 1, wardle2024masschemotherapywith pages 1-2)

### 12.2 Anti-inflammatory and supportive care
Corticosteroids are commonly paired with cysticidal therapy to mitigate inflammatory reactions; the Tanzania cohort used dexamethasone with albendazole and maintained/optimized anti-seizure medications. (stelzle2023efficacyandsafety pages 2-4)

### 12.3 Surgery and interventional management
Extraparenchymal NCC with hydrocephalus may require VP shunting or neuro-endoscopic procedures.
- A 2024 surgical review reports endoscopic third ventriculostomy (ETV) symptom resolution in 70–95% and highlights the role of endoscopy for cyst removal when feasible; VP shunting remains important where endoscopy is unavailable. (filho2024currentroleof pages 4-6)

Visual evidence of shunt failure and endoscopic approaches is available from the same review. (filho2024currentroleof media 744e0baf, filho2024currentroleof media 298e5ac1)

### 12.4 Clinical trials (registry evidence)
Representative interventional trials include:
- **NCT02947581 (SANTO)**: Phase 3 randomized trial of albendazole + praziquantel vs albendazole + placebo for subarachnoid NCC; terminated due to drug unavailability; primary endpoint was MRI parasite-volume reduction. (NCT02947581 chunk 1)
- **NCT02612896**: Completed community One Health intervention in Zambia comparing “elimination” vs “control” strategies with repeated praziquantel MDA plus pig interventions and education; completion Feb 2022. (NCT02612896 chunk 1)
- **NCT01296958**: Completed targeted screening for tapeworm carriers with niclosamide treatment vs education in Peru. (NCT01296958 chunk 1)

### 12.5 MAXO (Medical Action Ontology) suggestions (conceptual)
- Anthelmintic therapy (albendazole, praziquantel, niclosamide)
- Corticosteroid therapy
- Antiseizure medication therapy
- Ventriculoperitoneal shunt placement
- Neuroendoscopic cyst removal / endoscopic third ventriculostomy
These mappings require MAXO term ID validation outside the retrieved corpus.

---

## 13. Prevention

### 13.1 Primary prevention (One Health)
- Safe meat preparation and sanitation/hand hygiene reduce both taeniasis and cysticercosis risk. (aderinto2024neurocysticercosisandthe pages 8-9)
- Treating tapeworm carriers is central to interrupting egg shedding into the environment. (aderinto2024neurocysticercosisandthe pages 8-9, wardle2024masschemotherapywith pages 1-2)

### 13.2 Real-world implementation: mass niclosamide chemotherapy (2024)
A 2024 implementation study in Tumbes, Peru delivered three niclosamide rounds at 4‑month intervals to 77,397 eligible residents (68,751 treated at least once). Active follow-up captured adverse events in 65,551 people: AE prevalence 1.5% (988/65,551), 99.2% mild, 0 severe; most common symptoms were abdominal discomfort (56.4%), headache (24.6%), tongue numbness (14.3%), and diarrhea (13.8%). Programmatic treatment effectiveness against confirmed taeniasis was 75.0% cure at ~30 days (141/188). (wardle2024masschemotherapywith pages 1-2, wardle2024masschemotherapywith pages 4-5)

### 13.3 Health education and behavior change tools
- A Rwanda evaluation found “The Vicious Worm” education tool significantly improved community health worker knowledge about *T. solium* cysticercosis and maintained gains at 4 weeks, though implementation barriers included digital illiteracy and lack of smartphones. (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8)
- A Thailand KAP study identified widespread knowledge gaps (98.3% categorized as less accurate knowledge), supporting need for targeted education to complement structural interventions. (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8)

---

## 14. Other species / natural disease

### 14.1 Zoonosis and cross-species susceptibility
Humans are the definitive host for *T. solium* and pigs are key intermediate hosts; humans can also become accidental intermediate hosts (cysticercosis/NCC) after egg ingestion, making this a zoonotic One Health disease complex. (aderinto2024neurocysticercosisandthe pages 1-2, zulu2023theepidemiologyof pages 1-2)

### 14.2 Veterinary and control relevance
Pig-directed interventions (vaccination + deworming) are discussed as efficient methods to reduce exposure and transmission, though detailed country-specific deployment and commercial availability vary. (hossain2023insightsintothe pages 4-6)

NCBI Taxon IDs for relevant species were not provided in the retrieved excerpts and require supplementation from NCBI Taxonomy.

---

## 15. Model organisms

A 2024 experimental model paper describes **murine/rat extraparenchymal NCC modeling** using *Taenia crassiceps* inoculated into the subarachnoid space to reproduce features relevant to human extraparenchymal NCC and to evaluate albendazole ± dexamethasone schedules, including changes in ventricular size and inflammatory markers (e.g., IL-6 immunopositivity). (oliveira2024murineextraparenchymalneurocysticercosis pages 6-7)

This model is positioned as useful for studying the inflammation–treatment tradeoff in extraparenchymal disease. (oliveira2024murineextraparenchymalneurocysticercosis pages 6-7)

---

## Recent developments and expert analysis (2023–2024)

1. **Diagnostics are moving from parasite-derived antigens toward recombinant/synthetic platforms and point-of-care formats**, motivated by limited neuroimaging access in endemic areas; 2024 systematic review evidence highlights high accuracy for LLGP western blot in multi-cyst disease but limited sensitivity in single-cyst presentations, reinforcing the need for multi-antigen or antigen-detection strategies. (acker2024accuracyofimmunological pages 7-10, toribio2024fromlaboratoryto pages 1-2, acker2024accuracyofimmunological pages 10-11)

2. **Combination antiparasitic therapy is increasingly supported by real-world cohort and pediatric meta-analysis evidence**, with high lesion-resolution rates after albendazole + praziquantel and acceptable short-term tolerability when paired with anti-inflammatory regimens and close supervision. (stelzle2023efficacyandsafety pages 1-2, stelzle2023efficacyandsafety pages 6-7, dewi2024effectivenessofthe pages 4-5)

3. **Implementation science is emerging for taeniasis MDA**: large-scale niclosamide MDA in Peru demonstrated strong safety and moderate single-dose effectiveness, with identified predictors of failure (age, high coproantigen), providing concrete parameters for program optimization. (wardle2024masschemotherapywith pages 4-5)

4. **Population studies underscore that many infections are asymptomatic**, even in high-prevalence settings, and that epilepsy linkage is strong at the population level but not universal at the individual level—important for screening and cost-effectiveness modeling. (zulu2024neurocysticercosisprevalenceand pages 1-2)

---

## Key limitations of this report (evidence gaps in retrieved corpus)
- Formal ontology identifiers (ICD‑10/11, MeSH IDs, MONDO, Orphanet) were not present in the retrieved excerpts and therefore could not be tool-cited here.
- Human genetic susceptibility, epigenetic mechanisms, and multi-omics profiling evidence were not captured in the accessible texts.
- Some guideline algorithms and certain diagnostic accuracy studies were referenced (e.g., a 2024 Lancet Infectious Diseases POC test paper) but were unobtainable within this run; the report therefore emphasizes sources available in full-text excerpts. (toribio2024fromlaboratoryto pages 13-13)

---

## Primary URLs (publication dates as captured in metadata)
- Zulu et al. 2024-07, *Journal of Epidemiology and Global Health* (Zambia community NCC prevalence): https://doi.org/10.1007/s44197-024-00271-z (zulu2024neurocysticercosisprevalenceand pages 1-2)
- Stelzle et al. 2023-03, *Infection* (Tanzania cohort therapy): https://doi.org/10.1007/s15010-023-02021-y (stelzle2023efficacyandsafety pages 1-2)
- Van Acker et al. 2024-11, *PLOS Neglected Tropical Diseases* (diagnostic accuracy systematic review): https://doi.org/10.1371/journal.pntd.0012643 (acker2024accuracyofimmunological pages 7-10)
- Wardle et al. 2024-10, *The Lancet Regional Health – Americas* (niclosamide MDA): https://doi.org/10.1016/j.lana.2024.100876 (wardle2024masschemotherapywith pages 1-2)
- Hamamoto Filho et al. 2024-02, *Pathogens* (surgery review): https://doi.org/10.3390/pathogens13030218 (filho2024currentroleof pages 4-6)
- ClinicalTrials.gov NCT02612896: https://clinicaltrials.gov/study/NCT02612896 (NCT02612896 chunk 1)
- ClinicalTrials.gov NCT02947581: https://clinicaltrials.gov/study/NCT02947581 (NCT02947581 chunk 1)


References

1. (zulu2023theepidemiologyof pages 1-2): Gideon Zulu, Dominik Stelzle, Kabemba E. Mwape, Tamara M. Welte, Hilde Strømme, Chishimba Mubanga, Wilbroad Mutale, Annette Abraham, Alex Hachangu, Veronika Schmidt, Chummy S. Sikasunge, Isaac K. Phiri, and Andrea S. Winkler. The epidemiology of human taenia solium infections: a systematic review of the distribution in eastern and southern africa. PLOS Neglected Tropical Diseases, 17:e0011042, Mar 2023. URL: https://doi.org/10.1371/journal.pntd.0011042, doi:10.1371/journal.pntd.0011042. This article has 30 citations and is from a domain leading peer-reviewed journal.

2. (larkins2023thechallengesof pages 1-2): Andrew Larkins, Sarah Keatley, Bounnaloth Insisiengmay, Rattanaxay Phetsouvanh, Mieghan Bruce, and Amanda Ash. The challenges of detecting <i>taenia solium</i> and neurocysticercosis in low and middle‐income countries: a scoping review of lao people's democratic republic. Tropical Medicine &amp; International Health, 28:344-356, Mar 2023. URL: https://doi.org/10.1111/tmi.13870, doi:10.1111/tmi.13870. This article has 9 citations and is from a peer-reviewed journal.

3. (acker2024accuracyofimmunological pages 7-10): Lisa Van Acker, Luz Toribio, Mkunde Chachage, Hang Zeng, Brecht Devleesschauwer, Héctor H. Garcia, and Sarah Gabriël. Accuracy of immunological tests on serum and urine for diagnosis of taenia solium neurocysticercosis: a systematic review. PLOS Neglected Tropical Diseases, 18:e0012643, Nov 2024. URL: https://doi.org/10.1371/journal.pntd.0012643, doi:10.1371/journal.pntd.0012643. This article has 4 citations and is from a domain leading peer-reviewed journal.

4. (stelzle2023efficacyandsafety pages 1-2): D. Stelzle, C. Makasi, V. Schmidt, C. Trevisan, I. Van Damme, C. Ruether, P. Dorny, P. Magnussen, G. Zulu, K. E. Mwape, E. Bottieau, C. Prazeres da Costa, U. F. Prodjinotho, H. Carabin, E. Jackson, A. Fleury, S. Gabriël, B. J. Ngowi, and A. S. Winkler. Efficacy and safety of antiparasitic therapy for neurocysticercosis in rural tanzania: a prospective cohort study. Infection, 51:1127-1139, Mar 2023. URL: https://doi.org/10.1007/s15010-023-02021-y, doi:10.1007/s15010-023-02021-y. This article has 18 citations and is from a peer-reviewed journal.

5. (wardle2024masschemotherapywith pages 1-2): Melissa T. Wardle, Samantha E. Allen, Ricardo Gamboa, Percy Vilchez, Seth E. O'Neal, Claudio Muro, Andrés G. Lescano, Luz M. Moyano, Guillermo E. Gonzalvez, Armando E. González, Robert H. Gilman, Héctor H. García, Manuela R. Verastegui, Javier A. Bustos, Mirko Zimic, Isidro Gonzales, Herbert Saavedra, Sofia S. Sanchez, Manuel Martinez, Yesenia Castillo, Luz Toribio, Gianfranco Arroyo, Miguel A. Orrego, Nancy Chile, Holger Mayta, Monica Pajuelo, Saul Santivañez, Eloy Gonzalez-Gustavson, Luis Gomez-Puerta, Cesar M. Gavidia, Ana Vargas-Calla, Maria T. Lopez, Theodore E. Nash, Sukwan Handali, John Noh, and Jon Friedland. Mass chemotherapy with niclosamide for the control of taenia solium: population-based safety profile and treatment effectiveness. The Lancet Regional Health - Americas, 38:100876, Oct 2024. URL: https://doi.org/10.1016/j.lana.2024.100876, doi:10.1016/j.lana.2024.100876. This article has 7 citations.

6. (zulu2024neurocysticercosisprevalenceand pages 1-2): Gideon Zulu, Dominik Stelzle, Sarah Gabriël, Chiara Trevisan, Inge Van Damme, Chishimba Mubanga, Veronika Schmidt, Bernard J. Ngowi, Tamara M. Welte, Pascal Magnussen, Charlotte Ruether, Agnes Fleury, Pierre Dorny, Emmanuel Bottieau, Isaac K. Phiri, Kabemba E. Mwape, and Andrea S. Winkler. Neurocysticercosis prevalence and characteristics in communities of sinda district in zambia: a cross-sectional study. Journal of Epidemiology and Global Health, 14:1180-1190, Jul 2024. URL: https://doi.org/10.1007/s44197-024-00271-z, doi:10.1007/s44197-024-00271-z. This article has 10 citations and is from a peer-reviewed journal.

7. (aderinto2024neurocysticercosisandthe pages 1-2): Nicholas Aderinto, Gbolahan Olatunji, Emmanuel Kokori, Ismaila Ajayi Yusuf, Chimezirim Ezeano, Muili Abdulbasit, and Timilehin Isarinade. Neurocysticercosis and the central nervous system: advancements in diagnosis, treatment, and future prospects. Infectious Diseases, Jun 2024. URL: https://doi.org/10.5772/intechopen.1004554, doi:10.5772/intechopen.1004554. This article has 4 citations and is from a peer-reviewed journal.

8. (omeragic2024epidemiologyoftaeniosiscysticercosis pages 6-8): Jasmin Omeragić, Davor Alagić, Sabina Šerić-Haračić, and Naida Kapo. Epidemiology of taeniosis/cysticercosis in humans and animals. Infectious Diseases, Jan 2024. URL: https://doi.org/10.5772/intechopen.110727, doi:10.5772/intechopen.110727. This article has 0 citations and is from a peer-reviewed journal.

9. (zulu2023theepidemiologyof pages 9-10): Gideon Zulu, Dominik Stelzle, Kabemba E. Mwape, Tamara M. Welte, Hilde Strømme, Chishimba Mubanga, Wilbroad Mutale, Annette Abraham, Alex Hachangu, Veronika Schmidt, Chummy S. Sikasunge, Isaac K. Phiri, and Andrea S. Winkler. The epidemiology of human taenia solium infections: a systematic review of the distribution in eastern and southern africa. PLOS Neglected Tropical Diseases, 17:e0011042, Mar 2023. URL: https://doi.org/10.1371/journal.pntd.0011042, doi:10.1371/journal.pntd.0011042. This article has 30 citations and is from a domain leading peer-reviewed journal.

10. (stelzle2023clinicalcharacteristicsand pages 6-10): Dominik Stelzle, Annette Abraham, Miriam Kaminski, Veronika Schmidt, Robert De Meijere, Javier A Bustos, Hector Hugo Garcia, Priyadarshi Soumyaranjan Sahu, Branko Bobić, Carmen Cretu, Peter Chiodini, Veronique Dermauw, Brecht Devleesschauwer, Pierre Dorny, Ana Fonseca, Sarah Gabriël, Maria Ángeles Gómez Morales, Minerva Laranjo-González, Achim Hoerauf, Ewan Hunter, Ronan Jambou, Maja Jurhar-Pavlova, Ingrid Reiter-Owona, Smaragda Sotiraki, Chiara Trevisan, Manuela Vilhena, Naomi F Walker, Lorenzo Zammarchi, and Andrea Sylvia Winkler. Clinical characteristics and management of neurocysticercosis patients: a retrospective assessment of case reports from europe. Journal of travel medicine, Oct 2023. URL: https://doi.org/10.1093/jtm/taac102, doi:10.1093/jtm/taac102. This article has 35 citations and is from a domain leading peer-reviewed journal.

11. (figuet2024distributiondesmanifestations pages 85-90): O Figuet. Distribution des manifestations cliniques parmi les personnes ayant un diagnostic de neurocysticercose: revue systématique et méta-analyse (2008-2023) et mise à …. Unknown journal, 2024.

12. (figuet2024distributiondesmanifestationsa pages 85-90): O Figuet. Distribution des manifestations cliniques parmi les personnes ayant un diagnostic de neurocysticercose: revue systématique et méta-analyse (2008-2023) et mise à …. Unknown journal, 2024.

13. (bustos2023calcifiedneurocysticercosisdemographic pages 2-4): Javier A. Bustos, Gianfranco Arroyo, Oscar H. Del Brutto, Isidro Gonzales, Herbert Saavedra, Carolina Guzman, Sofia S. Sanchez-Boluarte, Kiran T. Thakur, Christina Coyle, Seth E. O’Neal, and Hector H. Garcia. Calcified neurocysticercosis: demographic, clinical, and radiological characteristics of a large hospital-based patient cohort. Pathogens, 13:26, Dec 2023. URL: https://doi.org/10.3390/pathogens13010026, doi:10.3390/pathogens13010026. This article has 10 citations.

14. (toribio2024fromlaboratoryto pages 1-2): Luz M. Toribio, Javier A. Bustos, and Hector H. Garcia. From laboratory to clinical practice: an update of the immunological and molecular tools for neurocysticercosis diagnosis. Frontiers in Parasitology, Jul 2024. URL: https://doi.org/10.3389/fpara.2024.1394089, doi:10.3389/fpara.2024.1394089. This article has 12 citations.

15. (toribio2024fromlaboratoryto pages 11-12): Luz M. Toribio, Javier A. Bustos, and Hector H. Garcia. From laboratory to clinical practice: an update of the immunological and molecular tools for neurocysticercosis diagnosis. Frontiers in Parasitology, Jul 2024. URL: https://doi.org/10.3389/fpara.2024.1394089, doi:10.3389/fpara.2024.1394089. This article has 12 citations.

16. (acker2024accuracyofimmunological pages 10-11): Lisa Van Acker, Luz Toribio, Mkunde Chachage, Hang Zeng, Brecht Devleesschauwer, Héctor H. Garcia, and Sarah Gabriël. Accuracy of immunological tests on serum and urine for diagnosis of taenia solium neurocysticercosis: a systematic review. PLOS Neglected Tropical Diseases, 18:e0012643, Nov 2024. URL: https://doi.org/10.1371/journal.pntd.0012643, doi:10.1371/journal.pntd.0012643. This article has 4 citations and is from a domain leading peer-reviewed journal.

17. (acker2024accuracyofimmunological pages 22-23): Lisa Van Acker, Luz Toribio, Mkunde Chachage, Hang Zeng, Brecht Devleesschauwer, Héctor H. Garcia, and Sarah Gabriël. Accuracy of immunological tests on serum and urine for diagnosis of taenia solium neurocysticercosis: a systematic review. PLOS Neglected Tropical Diseases, 18:e0012643, Nov 2024. URL: https://doi.org/10.1371/journal.pntd.0012643, doi:10.1371/journal.pntd.0012643. This article has 4 citations and is from a domain leading peer-reviewed journal.

18. (dewi2024effectivenessofthe pages 4-5): Dian Andriani Ratna Dewi, Lila Irawati Tjahjo Widuri, Arohid Allatib, Adristi A Athallah, Alessandro I Balga, Nabila Arkania, Farrasila Nadhira, Ni Made Wiliantari, and Farida Ulfa. Effectiveness of the antiparasitic combination of albendazole and praziquantel as compared with albendazole monotherapy in the treatment of neurocysticercosis in children: a systematic review and meta-analysis. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.64617, doi:10.7759/cureus.64617. This article has 4 citations.

19. (filho2024currentroleof pages 4-6): Pedro Tadao Hamamoto Filho, Luiz Fernando Norcia, Agnès Fleury, and Marco Antônio Zanini. Current role of surgery in the treatment of neurocysticercosis. Pathogens, 13:218, Feb 2024. URL: https://doi.org/10.3390/pathogens13030218, doi:10.3390/pathogens13030218. This article has 14 citations.

20. (filho2024currentroleof media 744e0baf): Pedro Tadao Hamamoto Filho, Luiz Fernando Norcia, Agnès Fleury, and Marco Antônio Zanini. Current role of surgery in the treatment of neurocysticercosis. Pathogens, 13:218, Feb 2024. URL: https://doi.org/10.3390/pathogens13030218, doi:10.3390/pathogens13030218. This article has 14 citations.

21. (NCT02612896 chunk 1):  Taenia Solium Elimination Versus Control: What is the Best Way Forward for Sub-Saharan Africa?. Institute of Tropical Medicine, Belgium. 2016. ClinicalTrials.gov Identifier: NCT02612896

22. (NCT02612896 chunk 2):  Taenia Solium Elimination Versus Control: What is the Best Way Forward for Sub-Saharan Africa?. Institute of Tropical Medicine, Belgium. 2016. ClinicalTrials.gov Identifier: NCT02612896

23. (NCT02947581 chunk 2):  Sub Arachnoid Neurocysticercosis Treatment Outcome (SANTO). Universidad Peruana Cayetano Heredia. 2016. ClinicalTrials.gov Identifier: NCT02947581

24. (NCT02947581 chunk 1):  Sub Arachnoid Neurocysticercosis Treatment Outcome (SANTO). Universidad Peruana Cayetano Heredia. 2016. ClinicalTrials.gov Identifier: NCT02947581

25. (NCT01296958 chunk 1): Seth E O'Neal, MD MPH. Targeted Screening for Taenia Solium Tapeworms. Oregon Health and Science University. 2011. ClinicalTrials.gov Identifier: NCT01296958

26. (aderinto2024neurocysticercosisandthe pages 8-9): Nicholas Aderinto, Gbolahan Olatunji, Emmanuel Kokori, Ismaila Ajayi Yusuf, Chimezirim Ezeano, Muili Abdulbasit, and Timilehin Isarinade. Neurocysticercosis and the central nervous system: advancements in diagnosis, treatment, and future prospects. Infectious Diseases, Jun 2024. URL: https://doi.org/10.5772/intechopen.1004554, doi:10.5772/intechopen.1004554. This article has 4 citations and is from a peer-reviewed journal.

27. (aderinto2024neurocysticercosisandthe pages 7-8): Nicholas Aderinto, Gbolahan Olatunji, Emmanuel Kokori, Ismaila Ajayi Yusuf, Chimezirim Ezeano, Muili Abdulbasit, and Timilehin Isarinade. Neurocysticercosis and the central nervous system: advancements in diagnosis, treatment, and future prospects. Infectious Diseases, Jun 2024. URL: https://doi.org/10.5772/intechopen.1004554, doi:10.5772/intechopen.1004554. This article has 4 citations and is from a peer-reviewed journal.

28. (hossain2023insightsintothe pages 4-6): Md. Shahadat Hossain, Shafqat Shabir, Philip Toye, Lian F. Thomas, and Franco H. Falcone. Insights into the diagnosis, vaccines, and control of taenia solium, a zoonotic, neglected parasite. Parasites & Vectors, Oct 2023. URL: https://doi.org/10.1186/s13071-023-05989-6, doi:10.1186/s13071-023-05989-6. This article has 37 citations and is from a peer-reviewed journal.

29. (aderinto2024neurocysticercosisandthe pages 3-4): Nicholas Aderinto, Gbolahan Olatunji, Emmanuel Kokori, Ismaila Ajayi Yusuf, Chimezirim Ezeano, Muili Abdulbasit, and Timilehin Isarinade. Neurocysticercosis and the central nervous system: advancements in diagnosis, treatment, and future prospects. Infectious Diseases, Jun 2024. URL: https://doi.org/10.5772/intechopen.1004554, doi:10.5772/intechopen.1004554. This article has 4 citations and is from a peer-reviewed journal.

30. (larkins2023thechallengesof pages 2-3): Andrew Larkins, Sarah Keatley, Bounnaloth Insisiengmay, Rattanaxay Phetsouvanh, Mieghan Bruce, and Amanda Ash. The challenges of detecting <i>taenia solium</i> and neurocysticercosis in low and middle‐income countries: a scoping review of lao people's democratic republic. Tropical Medicine &amp; International Health, 28:344-356, Mar 2023. URL: https://doi.org/10.1111/tmi.13870, doi:10.1111/tmi.13870. This article has 9 citations and is from a peer-reviewed journal.

31. (zulu2024neurocysticercosisprevalenceand pages 4-6): Gideon Zulu, Dominik Stelzle, Sarah Gabriël, Chiara Trevisan, Inge Van Damme, Chishimba Mubanga, Veronika Schmidt, Bernard J. Ngowi, Tamara M. Welte, Pascal Magnussen, Charlotte Ruether, Agnes Fleury, Pierre Dorny, Emmanuel Bottieau, Isaac K. Phiri, Kabemba E. Mwape, and Andrea S. Winkler. Neurocysticercosis prevalence and characteristics in communities of sinda district in zambia: a cross-sectional study. Journal of Epidemiology and Global Health, 14:1180-1190, Jul 2024. URL: https://doi.org/10.1007/s44197-024-00271-z, doi:10.1007/s44197-024-00271-z. This article has 10 citations and is from a peer-reviewed journal.

32. (singh2024seizuresandepilepsy pages 1-3): Gagandeep Singh, Hector H. Garcia, Oscar H. Del Brutto, Christina Coyle, and Josemir W. Sander. Seizures and epilepsy in association with neurocysticercosis. Neurology, Nov 2024. URL: https://doi.org/10.1212/wnl.0000000000209865, doi:10.1212/wnl.0000000000209865. This article has 18 citations and is from a highest quality peer-reviewed journal.

33. (bustos2023calcifiedneurocysticercosisdemographic pages 1-2): Javier A. Bustos, Gianfranco Arroyo, Oscar H. Del Brutto, Isidro Gonzales, Herbert Saavedra, Carolina Guzman, Sofia S. Sanchez-Boluarte, Kiran T. Thakur, Christina Coyle, Seth E. O’Neal, and Hector H. Garcia. Calcified neurocysticercosis: demographic, clinical, and radiological characteristics of a large hospital-based patient cohort. Pathogens, 13:26, Dec 2023. URL: https://doi.org/10.3390/pathogens13010026, doi:10.3390/pathogens13010026. This article has 10 citations.

34. (stelzle2023efficacyandsafety pages 7-10): D. Stelzle, C. Makasi, V. Schmidt, C. Trevisan, I. Van Damme, C. Ruether, P. Dorny, P. Magnussen, G. Zulu, K. E. Mwape, E. Bottieau, C. Prazeres da Costa, U. F. Prodjinotho, H. Carabin, E. Jackson, A. Fleury, S. Gabriël, B. J. Ngowi, and A. S. Winkler. Efficacy and safety of antiparasitic therapy for neurocysticercosis in rural tanzania: a prospective cohort study. Infection, 51:1127-1139, Mar 2023. URL: https://doi.org/10.1007/s15010-023-02021-y, doi:10.1007/s15010-023-02021-y. This article has 18 citations and is from a peer-reviewed journal.

35. (oliveira2024murineextraparenchymalneurocysticercosis pages 6-7): Vinícius Tadeu Oliveira, Tatiane de Camargo Martins, Renato Tavares Conceição, Diego Generoso, Vânia Maria de Vasconcelos Machado, Sabrina Setembre Batah, Alexandre Todorovic Fabro, Marco Antônio Zanini, Edda Sciutto, Agnès Fleury, and Pedro Tadao Hamamoto Filho. Murine extraparenchymal neurocysticercosis: appropriate model for evaluating anthelminthic and anti-inflammatory treatment schedules. Tropical Medicine and Infectious Disease, 9:215, Sep 2024. URL: https://doi.org/10.3390/tropicalmed9090215, doi:10.3390/tropicalmed9090215. This article has 3 citations.

36. (zulu2024neurocysticercosisprevalenceand pages 2-4): Gideon Zulu, Dominik Stelzle, Sarah Gabriël, Chiara Trevisan, Inge Van Damme, Chishimba Mubanga, Veronika Schmidt, Bernard J. Ngowi, Tamara M. Welte, Pascal Magnussen, Charlotte Ruether, Agnes Fleury, Pierre Dorny, Emmanuel Bottieau, Isaac K. Phiri, Kabemba E. Mwape, and Andrea S. Winkler. Neurocysticercosis prevalence and characteristics in communities of sinda district in zambia: a cross-sectional study. Journal of Epidemiology and Global Health, 14:1180-1190, Jul 2024. URL: https://doi.org/10.1007/s44197-024-00271-z, doi:10.1007/s44197-024-00271-z. This article has 10 citations and is from a peer-reviewed journal.

37. (toribio2024fromlaboratoryto pages 13-13): Luz M. Toribio, Javier A. Bustos, and Hector H. Garcia. From laboratory to clinical practice: an update of the immunological and molecular tools for neurocysticercosis diagnosis. Frontiers in Parasitology, Jul 2024. URL: https://doi.org/10.3389/fpara.2024.1394089, doi:10.3389/fpara.2024.1394089. This article has 12 citations.

38. (stelzle2023efficacyandsafety pages 6-7): D. Stelzle, C. Makasi, V. Schmidt, C. Trevisan, I. Van Damme, C. Ruether, P. Dorny, P. Magnussen, G. Zulu, K. E. Mwape, E. Bottieau, C. Prazeres da Costa, U. F. Prodjinotho, H. Carabin, E. Jackson, A. Fleury, S. Gabriël, B. J. Ngowi, and A. S. Winkler. Efficacy and safety of antiparasitic therapy for neurocysticercosis in rural tanzania: a prospective cohort study. Infection, 51:1127-1139, Mar 2023. URL: https://doi.org/10.1007/s15010-023-02021-y, doi:10.1007/s15010-023-02021-y. This article has 18 citations and is from a peer-reviewed journal.

39. (stelzle2023efficacyandsafety pages 2-4): D. Stelzle, C. Makasi, V. Schmidt, C. Trevisan, I. Van Damme, C. Ruether, P. Dorny, P. Magnussen, G. Zulu, K. E. Mwape, E. Bottieau, C. Prazeres da Costa, U. F. Prodjinotho, H. Carabin, E. Jackson, A. Fleury, S. Gabriël, B. J. Ngowi, and A. S. Winkler. Efficacy and safety of antiparasitic therapy for neurocysticercosis in rural tanzania: a prospective cohort study. Infection, 51:1127-1139, Mar 2023. URL: https://doi.org/10.1007/s15010-023-02021-y, doi:10.1007/s15010-023-02021-y. This article has 18 citations and is from a peer-reviewed journal.

40. (filho2024currentroleof media 298e5ac1): Pedro Tadao Hamamoto Filho, Luiz Fernando Norcia, Agnès Fleury, and Marco Antônio Zanini. Current role of surgery in the treatment of neurocysticercosis. Pathogens, 13:218, Feb 2024. URL: https://doi.org/10.3390/pathogens13030218, doi:10.3390/pathogens13030218. This article has 14 citations.

41. (wardle2024masschemotherapywith pages 4-5): Melissa T. Wardle, Samantha E. Allen, Ricardo Gamboa, Percy Vilchez, Seth E. O'Neal, Claudio Muro, Andrés G. Lescano, Luz M. Moyano, Guillermo E. Gonzalvez, Armando E. González, Robert H. Gilman, Héctor H. García, Manuela R. Verastegui, Javier A. Bustos, Mirko Zimic, Isidro Gonzales, Herbert Saavedra, Sofia S. Sanchez, Manuel Martinez, Yesenia Castillo, Luz Toribio, Gianfranco Arroyo, Miguel A. Orrego, Nancy Chile, Holger Mayta, Monica Pajuelo, Saul Santivañez, Eloy Gonzalez-Gustavson, Luis Gomez-Puerta, Cesar M. Gavidia, Ana Vargas-Calla, Maria T. Lopez, Theodore E. Nash, Sukwan Handali, John Noh, and Jon Friedland. Mass chemotherapy with niclosamide for the control of taenia solium: population-based safety profile and treatment effectiveness. The Lancet Regional Health - Americas, 38:100876, Oct 2024. URL: https://doi.org/10.1016/j.lana.2024.100876, doi:10.1016/j.lana.2024.100876. This article has 7 citations.
