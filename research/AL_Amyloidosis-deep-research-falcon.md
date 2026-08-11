---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T23:29:13.500992'
end_time: '2026-06-18T23:40:01.612756'
duration_seconds: 648.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: AL Amyloidosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AL Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **AL Amyloidosis** covering all of the
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
- **Disease Name:** AL Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **AL Amyloidosis** covering all of the
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


Due to technical limitations encountered with the evidence gathering system, I am unable to provide the fully comprehensive research report as requested. However, I can provide a partial report based on the literature that was successfully retrieved.

# Comprehensive Research Report: AL Amyloidosis

## 1. Disease Information

### Overview and Definition

Immunoglobulin light chain (AL) amyloidosis is a systemic clonal plasma cell disorder characterized by the production and deposition of misfolded immunoglobulin light chains (LCs), resulting in multiorgan dysfunction (zvida‐bloch2025themolecularlandscape pages 1-2). AL amyloidosis represents the most frequently encountered systemic amyloidosis and is classified as a protein misfolding disease where small B-cell clones (mostly plasma cell clones) present in the bone marrow proliferate and secrete unstable monoclonal free light chains (FLCs), which form amyloid fibrils that deposit in the interstitial tissue, resulting in organ injury and dysfunction (ikura2022molecularmechanismof pages 1-2).

The term "amyloid" refers to extracellular deposition of protein fibrils, with upward of 30 different types of amyloid fibrils having been identified in humans. Systemic immunoglobulin light chain (AL) amyloidosis is a clonal plasma cell disorder arising from tissue deposition of insoluble β-pleated sheets of misfolded immunoglobulin light chains (zanwar2023immunoglobulinlightchain pages 1-2).

### Epidemiology

AL amyloidosis is an uncommon entity with an estimated incidence of approximately 1 patient per 100,000 person-years. This translates to 3,500 to 4,500 new patients with AL amyloidosis being diagnosed in the United States each year (zanwar2023immunoglobulinlightchain pages 1-2). The disease affects approximately 10 per million per year globally (more2024alamyloidosisan pages 1-2).

**MONDO ID:** Not available in retrieved sources
**ICD Classification:** Not specifically provided in retrieved sources
**MeSH Terms:** Not specifically provided in retrieved sources

### Synonyms and Alternative Names
- Primary amyloidosis
- Light-chain amyloidosis
- Immunoglobulin light-chain amyloidosis

## 2. Etiology

### Disease Causal Factors

**Molecular Basis:** AL amyloidosis arises from clonal expansion of either differentiated plasma cells or, less frequently, mature B cells, leading to the production of immunoglobulin free light chains (FLCs), or fragments thereof, which are excessively secreted (more2024alamyloidosisan pages 1-2). The adaptive immune system generates antibody diversity through V(D)J gene recombination and somatic hypermutation (SHM). However, in AL amyloidosis, somatic mutations in the variable domain reduce the thermodynamic stability of light chains, promoting misfolding and amyloid fibril formation (zvida‐bloch2025themolecularlandscape pages 1-2, pozoyauner2023roleofthe pages 1-2).

**Light Chain Type Distribution:** Of the two classes of light chains, κ and λ, lambda (λ) light chains are twice as likely to cause systemic AL amyloidosis compared to kappa chains (more2024alamyloidosisan pages 1-2).

### Risk Factors

**Genetic Risk Factors:**
- Germline gene mutations on the variable λ region that reduce the thermodynamic stability of the protein account for the propensity of λ light chains to form amyloid deposits (more2024alamyloidosisan pages 1-2)
- Only a small fraction of the 29–30 functional Vλ segments contributed significantly to the development of amyloidosis, with just five segments (IGLV1–44, 2–14, 3–21, 3–1, and 6–57) being collectively responsible for approximately 70% of the cases in AL amyloidosis (more2024alamyloidosisan pages 1-2)
- Expression of the IGVL1–44 gene increases five times the odds of developing cardiac amyloidosis (more2024alamyloidosisan pages 1-2)

**Age-Related Risk:** 
- MGUS (monoclonal gammopathy of undetermined significance) prevalence increases with age, reported to be 3.2% for individuals who are more than 50 years old, increasing to 5.3% in those 70 years or older (more2024alamyloidosisan pages 1-2)
- MGUS can be detected at least 4 years before AL amyloidosis diagnosis (more2024alamyloidosisan pages 1-2)

**Clonal Characteristics:**
- t(11;14) translocation is the most common cytogenetic abnormality in AL amyloidosis, seen in 40%–60% of patients, juxtaposing the IGH locus on chromosome 14 with the cyclin D1 (CCND1) oncogene on chromosome 11 (zvida‐bloch2025themolecularlandscape pages 1-2)
- Approximately 80% of patients display at least one chromosomal abnormality using fluorescence in situ hybridization (FISH) technique
- 50%–70% have immunoglobulin heavy chain (IGH) translocations, a higher proportion than in other plasma cell disorders (zvida‐bloch2025themolecularlandscape pages 1-2)

## 3. Phenotypes and Clinical Manifestations

### Common Clinical Presentations

**General Symptoms:**
Fatigue is the commonest symptom in AL amyloidosis. The heterogenous clinical phenotype for AL amyloidosis often leads to patients presenting with advanced disease after being evaluated in various specialties without a diagnosis. Delay in arriving at a diagnosis has been reported to range from 6 months to ≥2 years from time of symptom onset (zanwar2023immunoglobulinlightchain pages 1-2). Additional non-specific symptoms include weight loss, numbness, paresthesia, pain, enlarged tongue (macroglossia), and nephrotic syndrome (shafqat2024renalalamyloidosis pages 1-2).

### Organ-Specific Manifestations

**Cardiac Involvement (70-80% of patients):**
- Cardiac amyloidosis presents with signs and symptoms of heart failure
- Echocardiographic findings include concentric cardiac hypertrophy, increase in interventricular septal thickness, and normal-to-low voltage on electrocardiogram (ECG)
- Cardiac hypertrophy tends to be biventricular
- Abnormal strain pattern with a base-to-apex gradient is specific for cardiac amyloidosis
- Cardiac MRI demonstrates late gadolinium enhancement (LGE) due to disruption of tight junctions between myocytes from expanding interstitial amyloid
- Transmural LGE correlates to advanced cardiac involvement
- Electromechanical dissociation and ventricular arrhythmias are common causes of cardiac mortality
- Cardiac involvement represents the single most important prognostic marker (zanwar2023immunoglobulinlightchain pages 1-2)

**Renal Involvement (approximately 2/3 of patients):**
- Nephrotic range proteinuria without an obvious etiology
- Renal involvement occurs in about two-thirds of AL amyloidosis cases
- 25% of patients with renal involvement progress to end-stage renal disease (ESRD) requiring renal replacement therapy
- Consequences range from mild proteinuria to nephrotic-range proteinuria with associated manifestations (hyperlipidemia, peripheral edema, hypercoagulability, and increased susceptibility to infections) and progressive renal dysfunction (shafqat2024renalalamyloidosis pages 1-2)

**Neurological Involvement:**
- Symmetric distal painful peripheral neuropathy with or without an autonomic component
- Median delay of 21 months from symptom onset to diagnosis when peripheral neuropathy is the first manifestation (zanwar2023immunoglobulinlightchain pages 1-2)
- Small unmyelinated nerves are involved early and prominently
- Length-dependent sensory predominant neuropathy associated with generalized autonomic failure (zanwar2023immunoglobulinlightchain pages 1-2)

**Hepatic Involvement:**
- Hepatomegaly
- Elevated alkaline phosphatase
- Hepatic rupture, portal hypertension, or rarely Budd–Chiari syndrome (more2024alamyloidosisan pages 1-2)

**Gastrointestinal Involvement:**
- Diarrhea from malabsorption
- Constipation
- Early satiety
- Weight loss (zanwar2023immunoglobulinlightchain pages 1-2)

**Pulmonary Involvement:**
- Cough or dyspnea (more2024alamyloidosisan pages 1-2)

**Other Manifestations:**
- Musculoskeletal pathologies (arthralgias/arthritis, myopathy)
- Endocrinopathies (hypothyroidism, hypogonadism)
- Coagulopathy (bleeding diathesis) (zanwar2023immunoglobulinlightchain pages 1-2)

**Frequency Data:**
- At diagnosis, more than 69% of patients already have lesions in multiple organs (ikura2022molecularmechanismof pages 1-2)
- Approximately 69% of patients show multiorgan involvement (zvida‐bloch2025themolecularlandscape pages 1-2)

## 4. Mechanism / Pathophysiology

### Molecular Mechanisms

**Protein Misfolding and Fibril Formation:**

In AL amyloidosis, monoclonal free light chains with peculiar misfolding propensity are secreted by a clonal plasma cell clone, and they misfold and aggregate into amyloid fibrils in the interstitium of target organs (zvida‐bloch2025themolecularlandscape pages 1-2). The formation of amyloid fibrils requires multiple steps: protein unfolding, misfolding, nucleation, polymerization, fiber elongation, and tissue deposition (ikura2022molecularmechanismof pages 1-2).

**Protein Unfolding and Instability:**
Proteins must present a partially unfolded structure (so-called "partially unfolded intermediate") for amyloid fibril formation. Unfolded proteins usually return to their native structure naturally but are sometimes folded into a false structure that is different from the original conformation. Misfolded proteins are usually degraded and removed by the proteasome, but some are released extracellularly and reassembled into a three-dimensional conformation that is rich in β-sheets and polymerizable with each other to form amyloid fibrils (ikura2022molecularmechanismof pages 1-2).

**Somatic Hypermutation Role:**
Somatic hypermutation (SHM) introduces changes in the variable domain of immunoglobulin light chains. While SHM normally increases antigen binding affinity, in AL amyloidosis, somatic mutations reduce thermodynamic stability of light chains, promoting misfolding and aggregation. The proliferating plasma cell clone may overproduce the light chain, which is then secreted into the bloodstream, placing the light chain out of the protective context provided by the quaternary structure of the antibody, increasing the risk of misfolding and aggregation due to destabilizing somatic mutations (pozoyauner2023roleofthe pages 1-2).

**Proteolytic Processing:**
Amyloidogenic light chains are more likely to undergo endoproteolysis, resulting in the release of amyloidogenic light-chain fragments prone to improper aggregation. Proteolysis occurs both on the LC variable and constant domains, generating a complex fragmentation pattern. Structural analysis indicates extensive remodeling by multiple proteases, largely taking place on poorly folded regions of the fibril surfaces (more2024alamyloidosisan pages 1-2).

### Mechanisms of Organ Damage

**Dual Mechanism of Toxicity:**
Organ dysfunction results from two mechanisms:
1. **Mass Effect:** Architectural damage from amyloid fibril deposition in the interstitial space
2. **Direct Proteotoxicity:** Amyloidogenic light chains induce cardiac dysfunction via direct proteotoxic effects (gustine2023predictorsoftreatment pages 1-2, ikura2022molecularmechanismof pages 1-2)

Pre-fibrillar light chain oligomers and misfolded proteins cause direct cytotoxicity to target organs. Both misfolded proteins and their oligomeric aggregates contribute to cellular and tissue damage (ikura2022molecularmechanismof pages 1-2).

### Cellular Processes

**Affected Pathways:**
- Disruption of cellular quality control mechanisms
- Protein folding pathway disruptions
- Cytokine and chemokine secretion abnormalities (zvida‐bloch2025themolecularlandscape pages 1-2)

**Structural Specificity:**
Amyloid fibrils are polymeric structures composed of β-sheet-rich structures. The cross-β amyloid motif is characteristic, with fibrils exhibiting a multiplicity of polymorphic structures (zvida‐bloch2025themolecularlandscape pages 1-2).

## 5. Anatomical Structures Affected

### Primary Organs
- **Heart** (most important prognostic determinant)
- **Kidneys**
- **Peripheral nervous system**
- **Liver**
- **Gastrointestinal tract**

### Organ-Level Pathology

The kidney and heart are the first two involved organs in AL amyloidosis (more2024alamyloidosisan pages 1-2). Cardiac involvement has a profound effect on the prognosis of patients with systemic amyloidosis (ikura2022molecularmechanismof pages 1-2). Amyloid deposition can affect any organ system, and the presenting symptoms are largely driven by the organ dysfunction caused by the amyloid deposition (zanwar2023immunoglobulinlightchain pages 1-2).

### Tissue and Cellular Level

Amyloid fibrils deposit in the endoneurium of peripheral nerves, often extensive in the dorsal root ganglia and sympathetic ganglia, leading to atrophy of Schwann cells in proximity to amyloid fibrils and blood–nerve barrier disruption (in neurological involvement) (zanwar2023immunoglobulinlightchain pages 1-2).

**Suggested UBERON Terms:**
- UBERON:0000948 (heart)
- UBERON:0002113 (kidney)
- UBERON:0000010 (peripheral nervous system)
- UBERON:0002107 (liver)
- UBERON:0005409 (gastrointestinal system)

## 6. Temporal Development

### Onset

**Age of Onset:**
The disease typically manifests in adults, with median age at diagnosis reported as 68 years (IQR 59-74 years) in one large cohort (porcari2024redefiningcardiacinvolvement pages 1-2).

**Onset Pattern:**
AL amyloidosis progresses much faster than other types of amyloidosis, with a slight delay in diagnosis leading to a marked exacerbation of cardiomyopathy. In some cases, the resulting heart failure is so severe that chemotherapy cannot be administered, and death sometimes occurs within a few months (ikura2022molecularmechanismof pages 1-2).

### Disease Course and Progression

**Diagnostic Delay:**
- Delay in arriving at a diagnosis ranges from 6 months to ≥2 years from time of symptom onset
- Approximately 37% of patients are diagnosed over 12 months post symptom onset
- 32% consult at least five doctors before receiving a diagnosis (shafqat2024renalalamyloidosis pages 1-2)
- Median time from symptom onset to diagnosis potentially extends between 2 and 4 years (shafqat2024renalalamyloidosis pages 1-2)

**Disease Progression:**
The disease is characterized by progressive organ dysfunction leading to organ failure. AL amyloidosis progresses much faster than other types of amyloidosis (ikura2022molecularmechanismof pages 1-2).

## 7. Inheritance and Population

### Epidemiology

**Incidence and Prevalence:**
- Incidence: approximately 1 patient per 100,000 person-years
- In the United States: 3,500 to 4,500 new patients diagnosed annually (zanwar2023immunoglobulinlightchain pages 1-2)
- Global incidence: approximately 10 per million per year (more2024alamyloidosisan pages 1-2)
- Described as an uncommon entity despite being the most frequently encountered systemic amyloidosis (zanwar2023immunoglobulinlightchain pages 1-2)

### Population Demographics

**Age Distribution:**
- Median age at diagnosis: 68 years (IQR 59-74 years) in one large cohort
- MGUS prevalence increases with age (3.2% for individuals >50 years old, 5.3% in those ≥70 years) (more2024alamyloidosisan pages 1-2)

**Sex Ratio:**
In one cohort of 560 patients: 346 male (61.8%) and 214 female (38.2%) (porcari2024redefiningcardiacinvolvement pages 1-2)

**Geographic Distribution:**
AL amyloidosis is described as the most prevalent type of diagnosed systemic amyloidosis in Western countries (zanwar2023immunoglobulinlightchain pages 1-2, more2024alamyloidosisan pages 1-2).

### Genetic Characteristics

AL amyloidosis is NOT a hereditary disease in the traditional sense. It arises from acquired somatic mutations in plasma cells. However, germline genetic factors influence susceptibility:
- Germline gene mutations on the variable λ region affect protein stability
- Specific V λ gene segments (IGLV1–44, 2–14, 3–21, 3–1, and 6–57) account for ~70% of cases
- Expression of IGVL1–44 increases odds of developing cardiac amyloidosis 5-fold (more2024alamyloidosisan pages 1-2)

## 8. Diagnostics

### Clinical Diagnostic Approach

**Initial Detection:**
For a diagnosis of AL amyloidosis, there must be:
1. Evidence of an amyloid-related syndrome
2. Positive Congo Red staining on biopsy (or detection of AL amyloid on mass spectrometry)
3. Presence of a plasma cell dyscrasia (shafqat2024renalalamyloidosis pages 1-2)

### Laboratory Tests

**Monoclonal Protein Detection:**
- Serum protein electrophoresis with immunofixation
- 24-hour urine protein electrophoresis
- Serum free light chain (FLC) assay - crucial tool for diagnosis, risk assessment, and management (zanwar2023immunoglobulinlightchain pages 1-2, shafqat2024renalalamyloidosis pages 1-2)

**Cardiac Biomarkers:**
- NT-proBNP (N-terminal probrain natriuretic peptide)
- BNP (brain natriuretic peptide)
- Cardiac troponin I (TnI) or troponin T
- These biomarkers drive existing staging systems (zanwar2023immunoglobulinlightchain pages 1-2, gustine2023predictorsoftreatment pages 1-2)

**Renal Biomarkers:**
- Estimated glomerular filtration rate (eGFR)
- Measures of proteinuria
- 24-hour urine protein (shafqat2024renalalamyloidosis pages 1-2)

### Histopathology and Tissue Diagnosis

**Biopsy Sites:**
- Bone marrow biopsy
- Fat pad aspirate - performed concurrently with bone marrow biopsy, have high sensitivity for diagnosis
- Organ biopsies (when needed)

A bone marrow biopsy and fat pad aspirate performed concurrently have a high sensitivity for the diagnosis of AL amyloidosis and negate the need for organ biopsies in most patients (zanwar2023immunoglobulinlightchain pages 1-2).

**Histological Staining:**
- Congo Red staining is the gold standard - amyloid fibrils bind Congo red and appear with characteristic apple-green birefringence under polarized light (more2024alamyloidosisan pages 1-2)

**Amyloid Typing:**
An accurate diagnosis requires amyloid typing via additional testing, including:
- Tissue mass spectrometry
- Immunohistochemistry (zanwar2023immunoglobulinlightchain pages 1-2, more2024alamyloidosisan pages 1-2)

### Imaging Studies

**Echocardiography:**
- Concentric cardiac hypertrophy
- Increased interventricular septal thickness
- Abnormal strain pattern with base-to-apex gradient (specific for cardiac amyloidosis) (zanwar2023immunoglobulinlightchain pages 1-2)

**Cardiac MRI:**
- Late gadolinium enhancement (LGE)
- Transmural LGE correlates to advanced cardiac involvement
- Extracellular volume (ECV) mapping provides quantitative measurement of amyloid burden and is a strong independent predictor of prognosis (porcari2024redefiningcardiacinvolvement pages 1-2)

**Electrocardiogram (ECG):**
- Normal-to-low voltage despite cardiac hypertrophy on imaging (classic finding) (zanwar2023immunoglobulinlightchain pages 1-2)

### Genetic/Molecular Testing

**Bone Marrow Evaluation:**
- Plasma cell percentage assessment
- Fluorescence in situ hybridization (FISH) for cytogenetic abnormalities including t(11;14)
- Approximately 80% of patients display at least one chromosomal abnormality (zanwar2023immunoglobulinlightchain pages 1-2, zvida‐bloch2025themolecularlandscape pages 1-2)

## 9. Staging Systems

### Cardiac Staging

Prognostication for AL amyloidosis is largely driven by the organs impacted. Cardiac involvement represents the single most important prognostic marker, and existing staging systems are driven by cardiac biomarkers (zanwar2023immunoglobulinlightchain pages 1-2).

**Mayo 2004 Staging System:**
Uses cardiac biomarkers (NT-proBNP/BNP and cardiac troponin levels) to stratify patients into stages I-III (zanwar2023immunoglobulinlightchain pages 1-2, gustine2023predictorsoftreatment pages 1-2).

**Modified Mayo Staging:**
Further divides stage III into IIIa and IIIb based on NT-proBNP/BNP and troponin I thresholds:
- Stage IIIb: NT-proBNP > 8500 pg/mL (or BNP > 700 pg/mL) AND TnI > 0.1 ng/mL
- Stage IIIb represents a particularly high-risk group with high rates of early death and poor prognosis (historical median overall survival 4-6 months) (gustine2023predictorsoftreatment pages 1-2)

**Extracellular Volume (ECV) Mapping:**
Recent evidence indicates that ECV mapping on cardiac MRI is an independent predictor of prognosis and can help define the hematological response associated with better long-term outcomes for each patient. ECV provides direct measurement of cardiac amyloid infiltration (porcari2024redefiningcardiacinvolvement pages 1-2).

### Renal Staging

**Pavia Renal Staging Model:**
Stratifies patients based on their likelihood of progressing to dialysis (shafqat2024renalalamyloidosis pages 1-2).

### Prognostic Factors

Apart from organ involvement, important prognostic markers include:
- Plasma cell percentage on bone marrow biopsy
- Specific fluorescence in situ hybridization findings (e.g., t(11;14))
- Age at diagnosis
- Performance status (zanwar2023immunoglobulinlightchain pages 1-2)

## 10. Outcome/Prognosis

### Survival Outcomes

**Overall Survival:**
- Median overall survival varies dramatically by cardiac stage
- Stage IIIb disease: median overall survival of 9 months in one cohort; historical median of 4-6 months (gustine2023predictorsoftreatment pages 1-2)
- Two-year survival increased to 60% over the 2010–2014 period compared with 42% over 2000–2004 in one single-center review, reflecting therapeutic improvements (theodorakakou2022futuredevelopmentsin pages 1-3)
- Five-year survival improved to up to 77% with monoclonal antibodies and stem cell transplantation (zanwar2023immunoglobulinlightchain pages 1-2)

**Early Mortality:**
AL amyloidosis is associated with high early mortality. Stage IIIb disease has particularly high rates of early death, with 18% mortality at an early timepoint. Delay in diagnosis contributes to the high early mortality seen in this disease (zanwar2023immunoglobulinlightchain pages 1-2, gustine2023predictorsoftreatment pages 1-2).

### Factors Affecting Survival

**Baseline Prognostic Factors for Advanced Disease:**
Independent baseline factors associated with shorter overall survival in stage IIIb patients include:
- Symptom onset to diagnosis >6 months (HR 1.94)
- Bone marrow plasmacytosis ≥10% (HR 1.98)
- Troponin I > 0.635 ng/mL (HR 1.62)
- New York Heart Association class III or IV (HR 1.67)
- 6-minute walk test distance < 200 m (HR 1.85) (gustine2023predictorsoftreatment pages 1-2)

**Treatment Response and Survival:**
Early hematologic and cardiac responses during treatment are significantly associated with longer survival:
- In 1-month landmark analysis, patients with hematologic very good partial response (VGPR), partial response (PR), and no response had median OS of 47, 25, and 5 months, respectively
- Patients with cardiac response at 3 months had significantly longer OS (47 vs 11 months) (gustine2023predictorsoftreatment pages 1-2)

### Organ-Specific Outcomes

**Renal Outcomes:**
- 25% of patients with renal involvement progress to end-stage renal disease requiring renal replacement therapy (shafqat2024renalalamyloidosis pages 1-2)

**Cardiac Outcomes:**
- Cardiac involvement is the primary determinant of prognosis
- Electromechanical dissociation and ventricular arrhythmias are common causes of cardiac mortality, especially sudden cardiac death (zanwar2023immunoglobulinlightchain pages 1-2)

## 11. Treatment

### First-Line Therapy

**Current Standard of Care (2024):**

The combination of Daratumumab plus Cyclophosphamide, Bortezomib, and Dexamethasone (Dara-VCd or D-VCd) is currently the novel and preferred standard of care for newly diagnosed patients with AL amyloidosis and the only FDA and EMA-approved treatment for this disease (theodorakakou2022futuredevelopmentsin pages 1-3).

**ANDROMEDA Trial Results:**
This phase III randomized controlled trial compared VCd to Dara-VCd and demonstrated substantial improvement in complete hematologic response rates:
- After median follow-up of 20.3 months, hematologic CR rate was 59% in the daratumumab group vs. 19% in the control group
- At least VGPR was seen in 79% vs. 50%, respectively
- At 6-month landmark: CR rate 49.7% vs. 14%; cardiac response rate 41.5% vs. 22.2%; renal response rate 53% vs. 23.9%
- At 12-month landmark: organ responses improved further (57% vs. 28% and 57% vs. 27%, respectively) (theodorakakou2022futuredevelopmentsin pages 1-3)

**Asian Subgroup Analysis:**
Among 60 Asian patients from ANDROMEDA (Japan, Korea, China):
- Overall hematologic complete response rate was higher for D-VCd vs. VCd (58.6% vs. 9.7%)
- Six-month cardiac and renal response rates were higher with D-VCd vs. VCd (cardiac: 46.7% vs. 4.8%; renal: 57.1% vs. 37.5%)
- Major organ deterioration progression-free survival and event-free survival were improved with D-VCd
- Safety profile was generally consistent with the global study population (suzuki2023daratumumabplusbortezomib pages 1-2)

### Alternative First-Line Regimens

When daratumumab is not available or accessible, alternative options include:
- VCd (bortezomib/cyclophosphamide/dexamethasone)
- BMdex (Bortezomib-Melphalan-dexamethasone) - shown to improve overall survival over Mdex in a randomized study
- Bortezomib plus dexamethasone
- Mdex alone
- Lenalidomide-based therapy (for special patients) (theodorakakou2022futuredevelopmentsin pages 1-3)

### Advanced and Experimental Therapies

**Autologous Stem Cell Transplantation (ASCT):**
ASCT after daratumumab-based induction treatment is the cornerstone of therapy in younger and fit patients, with the goal of reaching a deep and rapid disease hematological and organ response (more2024alamyloidosisan pages 1-2). However, only 20% of AL amyloidosis patients are transplant-eligible at diagnosis (zanwar2023immunoglobulinlightchain pages 1-2).

**Venetoclax:**
For patients with t(11;14) translocation, venetoclax (anti-BCL2 therapy) shows promise. t(11;14) may be a positive indicator of therapy responses to venetoclax. Phase 1 and 2 trials are exploring venetoclax in both newly diagnosed and relapsed/refractory settings (shafqat2024renalalamyloidosis pages 1-2, theodorakakou2022futuredevelopmentsin pages 1-3).

**CAR T-Cell Therapy:**
Chimeric antigen receptor (CAR) cellular therapies directed against plasma cells are being investigated. Most trials of multiple myeloma have excluded AL amyloidosis patients, but there is growing interest in extending CAR T-cell therapy to AL amyloidosis, particularly for high-risk cases (theodorakakou2022futuredevelopmentsin pages 1-3).

**Anti-Fibril Antibodies:**
Novel immunotherapeutic approaches aim to clear AL amyloid fibrils from peripheral organs:
- Birtamimab (NEOD001) - monoclonal antibody targeting amyloid deposits
- These medications are still under investigation in clinical trials
- Studies focus primarily on advanced cardiac amyloidosis (shafqat2024renalalamyloidosis pages 1-2, theodorakakou2022futuredevelopmentsin pages 1-3)

**Other Emerging Therapies:**
- BCMA-directed bispecific antibodies in relapsed/refractory settings
- Teclistamab in relapsed or refractory AL amyloidosis
- Light chain stabilizers - small molecules that bind to the natively folded state of full-length light chains to act as pharmacological kinetic stabilizers (theodorakakou2022futuredevelopmentsin pages 1-3)

### Treatment Strategy by Disease Stage

**Stage IIIb Disease:**
Patients with stage IIIb disease were excluded from the ANDROMEDA trial, and Dara-VCd has not been approved for such high-risk patients. Management of these patients remains particularly challenging. On multivariable modeling, bortezomib use was associated with early hematologic and cardiac responses and longer OS (gustine2023predictorsoftreatment pages 1-2).

**Treatment Goals:**
The goal of treatment is to:
1. Reduce amyloid production by targeting the aberrant plasma cell clone in the bone marrow
2. Achieve rapid and deep hematological response
3. Obtain organ response (cardiac, renal, neurological)
4. Improve overall survival (shafqat2024renalalamyloidosis pages 1-2, theodorakakou2022futuredevelopmentsin pages 1-3)

### Treatment Efficacy Metrics

**Hematologic Response Criteria:**
- Complete Response (CR): absence of monoclonal protein by serum and urine immunofixation electrophoresis and normal free light chain ratio
- Very Good Partial Response (VGPR): difference between involved and uninvolved FLC (dFLC) < 40 mg/L
- Partial Response (PR): defined by dFLC reduction
- Rapid and deep hematologic responses are critical for optimal outcomes, especially in stage IIIb disease (gustine2023predictorsoftreatment pages 1-2)

**Organ Response:**
- Cardiac response rates at 6 months: 41.5% with D-VCd vs. 22.2% with VCd alone
- Renal response rates at 6 months: 53% with D-VCd vs. 23.9% with VCd alone
- Organ responses improve further at 12 months (theodorakakou2022futuredevelopmentsin pages 1-3)

## 12. Model Organisms

Based on the retrieved literature, there is limited specific information about AL amyloidosis animal models. The papers retrieved focused primarily on Alzheimer's disease animal models rather than AL amyloidosis models, indicating this is an area where additional research would be beneficial.

**Challenges in Disease Modeling:**
Despite therapeutic advancements, the disease's complexity challenges the development of effective biological models. Progressing towards personalized therapies requires the development of preclinical models (zvida‐bloch2025themolecularlandscape pages 1-2).

**SUGGESTED ONTOLOGY TERMS**

Based on the comprehensive review above, the following ontology terms are suggested for knowledge base annotation:

**Human Phenotype Ontology (HPO) Terms:**
- HP:0001635 (Congestive heart failure)
- HP:0000093 (Proteinuria)
- HP:0001903 (Anemia)
- HP:0002315 (Headache)
- HP:0001324 (Muscle weakness)
- HP:0001265 (Hyporeflexia)
- HP:0002459 (Dysautonomia)
- HP:0002017 (Nausea and vomiting)
- HP:0001639 (Hypertrophic cardiomyopathy)
- HP:0012622 (Chronic kidney disease)
- HP:0003077 (Hyperlipidemia)
- HP:0001873 (Thrombocytopenia)
- HP:0001701 (Pericarditis)
- HP:0011675 (Arrhythmia)

**Gene Ontology (GO) Terms:**
- GO:0006457 (protein folding)
- GO:0030163 (protein catabolic process)
- GO:0070842 (aggresome assembly)
- GO:0051260 (protein homooligomerization)
- GO:0034976 (endoplasmic reticulum stress response)

**Cell Ontology (CL) Terms:**
- CL:0000786 (plasma cell)
- CL:0000945 (lymphocyte of B lineage)
- CL:0000746 (cardiac muscle cell)

**UBERON Anatomical Terms:**
- UBERON:0000948 (heart)
- UBERON:0002113 (kidney)
- UBERON:0000010 (peripheral nervous system)
- UBERON:0002107 (liver)
- UBERON:0005409 (gastrointestinal system tract)

**ChEBI Chemical Terms:**
- CHEBI:17234 (glucose)
- CHEBI:16541 (protein)
- CHEBI:36080 (protein)

**MAXO Treatment Terms:**
- MAXO:0000058 (chemotherapy)
- MAXO:0000127 (stem cell transplantation)
- MAXO:0000750 (immunotherapy)

**MONDO Disease Terms:**
- Search recommended for: MONDO term for AL amyloidosis

## LIMITATIONS AND FUTURE RESEARCH NEEDS

This report is based on successfully retrieved literature; however, technical limitations prevented complete evidence gathering across all requested domains. Additional research would benefit from:

1. More comprehensive epidemiological data including geographic and ethnic variations
2. Detailed molecular profiling data (transcriptomics, proteomics, metabolomics)
3. Complete clinical trial database interrogation
4. Comprehensive animal model characterization
5. Quality of life assessment data
6. Prevention strategies and screening protocols
7. Comprehensive genetic variant databases with ACMG/AMP classifications

The field of AL amyloidosis continues to evolve rapidly, with significant advances in 2023-2024 including improved diagnostic methods (ECV mapping), novel therapeutics (anti-fibril antibodies, CAR-T cells), and refined staging systems. Continued research is essential to improve outcomes for patients with this challenging disease.

References

1. (zvida‐bloch2025themolecularlandscape pages 1-2): Tal Zvida‐Bloch, Eli Muchtar, Angela Dispenzieri, Ofer Shpilberg, and Oshrat Hershkovitz‐Rokah. The molecular landscape of al amyloidosis. British Journal of Haematology, 206:1297-1311, Apr 2025. URL: https://doi.org/10.1111/bjh.20070, doi:10.1111/bjh.20070. This article has 9 citations and is from a domain leading peer-reviewed journal.

2. (ikura2022molecularmechanismof pages 1-2): Hidehiko Ikura, Jin Endo, Hiroki Kitakata, Hidenori Moriyama, Motoaki Sano, and Keiichi Fukuda. Molecular mechanism of pathogenesis and treatment strategies for al amyloidosis. International Journal of Molecular Sciences, 23:6336, Jun 2022. URL: https://doi.org/10.3390/ijms23116336, doi:10.3390/ijms23116336. This article has 49 citations.

3. (zanwar2023immunoglobulinlightchain pages 1-2): Saurabh Zanwar, Morie A. Gertz, and Eli Muchtar. Immunoglobulin light chain amyloidosis: diagnosis and risk assessment. Journal of the National Comprehensive Cancer Network : JNCCN, 21 1:83-90, Jan 2023. URL: https://doi.org/10.6004/jnccn.2022.7077, doi:10.6004/jnccn.2022.7077. This article has 37 citations.

4. (more2024alamyloidosisan pages 1-2): Sonia Morè, Valentina Maria Manieri, Laura Corvatta, Erika Morsia, Antonella Poloni, and Massimo Offidani. Al amyloidosis: an overview on diagnosis, staging system, and treatment. Frontiers in Hematology, May 2024. URL: https://doi.org/10.3389/frhem.2024.1378451, doi:10.3389/frhem.2024.1378451. This article has 4 citations.

5. (pozoyauner2023roleofthe pages 1-2): Luis Del Pozo-Yauner, Guillermo A. Herrera, Julio I. Perez Carreon, Elba A. Turbat-Herrera, Francisco J. Rodriguez-Alvarez, and Robin A. Ruiz Zamora. Role of the mechanisms for antibody repertoire diversification in monoclonal light chain deposition disorders: when a friend becomes foe. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1203425, doi:10.3389/fimmu.2023.1203425. This article has 26 citations and is from a peer-reviewed journal.

6. (shafqat2024renalalamyloidosis pages 1-2): Areez Shafqat, Hassan Elmaleh, Ali Mushtaq, Zaina Firdous, Omer S. Ashruf, Debduti Mukhopadhyay, Maheen Ahmad, Mahnoor Ahmad, Shahzad Raza, and F. Anwer. Renal al amyloidosis: updates on diagnosis, staging, and management. Journal of Clinical Medicine, 13:1744, Mar 2024. URL: https://doi.org/10.3390/jcm13061744, doi:10.3390/jcm13061744. This article has 17 citations.

7. (gustine2023predictorsoftreatment pages 1-2): Joshua N. Gustine, Andrew Staron, Lisa Mendelson, Tracy Joshi, Deepa M. Gopal, Omar K. Siddiqi, Frederick L. Ruberg, and Vaishali Sanchorawala. Predictors of treatment response and survival outcomes in patients with advanced cardiac al amyloidosis. Blood Advances, 7:6080-6091, Oct 2023. URL: https://doi.org/10.1182/bloodadvances.2023010324, doi:10.1182/bloodadvances.2023010324. This article has 34 citations and is from a peer-reviewed journal.

8. (porcari2024redefiningcardiacinvolvement pages 1-2): Aldostefano Porcari, Ambra Masi, Ana Martinez-Naharro, Yousuf Razvi, Rishi Patel, Adam Ioannou, Muhammad U. Rauf, Giulio Sinigiani, Brendan Wisniowski, Stefano Filisetti, Jasmine Currie-Cathey, Sophie O’Beara, Tushar Kotecha, Dan Knight, James C. Moon, Gianfranco Sinagra, Ruta Virsinskaite, Janet Gilbertson, Lucia Venneri, Aviva Petrie, Helen Lachmann, Carol Whelan, Peter Kellman, Sriram Ravichandran, Oliver Cohen, Shameem Mahmood, Charlotte Manisty, Philip N. Hawkins, Julian D. Gillmore, Ashutosh D. Wechalekar, and Marianna Fontana. Redefining cardiac involvement and targets of treatment in systemic immunoglobulin al amyloidosis. JAMA Cardiology, 9:982, Nov 2024. URL: https://doi.org/10.1001/jamacardio.2024.2555, doi:10.1001/jamacardio.2024.2555. This article has 25 citations and is from a highest quality peer-reviewed journal.

9. (theodorakakou2022futuredevelopmentsin pages 1-3): Foteini Theodorakakou, Despina Fotiou, Meletios A. Dimopoulos, and Efstathios Kastritis. Future developments in the treatment of al amyloidosis. Hemato, 3:131-152, Feb 2022. URL: https://doi.org/10.3390/hemato3010012, doi:10.3390/hemato3010012. This article has 11 citations.

10. (suzuki2023daratumumabplusbortezomib pages 1-2): Kenshi Suzuki, Ashutosh D. Wechalekar, Kihyun Kim, Chihiro Shimazaki, Jin Seok Kim, Takayuki Ikezoe, Chang-Ki Min, Fude Zhou, Zhen Cai, Xiaonong Chen, Shinsuke Iida, Nagaaki Katoh, Tomoaki Fujisaki, Ho-Jin Shin, NamPhuong Tran, Xiang Qin, Sandra Y. Vasey, Brenda Tromp, Brendan M. Weiss, Raymond L. Comenzo, Efstathios Kastritis, and Jin Lu. Daratumumab plus bortezomib, cyclophosphamide, and dexamethasone in asian patients with newly diagnosed al amyloidosis: subgroup analysis of andromeda. Annals of Hematology, 102:863-876, Mar 2023. URL: https://doi.org/10.1007/s00277-023-05090-z, doi:10.1007/s00277-023-05090-z. This article has 16 citations and is from a peer-reviewed journal.