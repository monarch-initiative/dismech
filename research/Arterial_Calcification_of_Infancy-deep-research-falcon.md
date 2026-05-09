---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T11:40:56.093112'
end_time: '2026-05-05T11:54:12.271865'
duration_seconds: 796.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arterial Calcification of Infancy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arterial Calcification of Infancy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arterial Calcification of Infancy** covering all of the
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
- **Disease Name:** Arterial Calcification of Infancy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arterial Calcification of Infancy** covering all of the
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


# Comprehensive Research Report: Arterial Calcification of Infancy (Generalized Arterial Calcification of Infancy, GACI)

## Executive summary
Arterial Calcification of Infancy—most often referred to in the biomedical literature as **Generalized Arterial Calcification of Infancy (GACI)**—is an ultra-rare, typically **autosomal recessive** ectopic mineralization disorder characterized by **calcification of medium/large arteries**, **arterial stenosis**, and high early mortality, with mechanistic convergence on **systemic deficiency of extracellular inorganic pyrophosphate (PPi)**, a key endogenous inhibitor of hydroxyapatite deposition. The predominant genetic causes are biallelic loss-of-function variants in **ENPP1** and, less commonly, **ABCC6** (ferreira2021ectopiccalcificationand pages 1-2, yao2023clinicalandmolecular pages 1-2). Recent 2023–2024 literature emphasizes (i) the disease continuum connecting infantile arteriopathy and later **FGF23-mediated hypophosphatemic rickets** in ENPP1 deficiency, and (ii) “bench-to-bedside” translation of **recombinant ENPP1 enzyme replacement** therapies aimed at restoring circulating PPi (ferreira2024enpp1inblood pages 24-26, davies2023futuretreatmentsfor pages 1-2).

## 1. Disease information
### 1.1 Disease overview (current understanding)
GACI is a life-threatening infantile arteriopathy with calcification (often along the **internal elastic lamina**) and associated intimal proliferation/stenosis of large and medium arteries, producing severe neonatal/infant cardiovascular compromise (e.g., hypertension, heart failure, ischemia). Affected infants may present prenatally (2nd trimester) or within the first weeks of life (ferreira2024enpp1inblood pages 1-2, ferreira2024enpp1inblood pages 2-4).

**Direct abstract quote (mechanistic definition):** A foundational mechanistic summary from a disease-model paper states: “Generalized arterial calcification of infancy (GACI) is a rare, life-threatening disorder caused by loss-of-function mutations in the gene encoding ectonucleotide pyrophosphatase phosphodiesterase 1 (ENPP1), which normally hydrolyzes extracellular ATP into AMP and pyrophosphate (PPi).” (Disease Models & Mechanisms; 2018-10; URL https://doi.org/10.1242/dmm.035691) (khan2018enpp1enzymereplacement pages 1-3).

### 1.2 Key identifiers
- **OMIM (disease):** **GACI = OMIM 208000** (yao2023clinicalandmolecular pages 1-2).
- Imaging literature also references **GACI1 OMIM:208000** and **GACI2 OMIM:614473** (ramirezsuarez2022longitudinalassessmentof pages 8-9).
- **Causal gene OMIM IDs:** **ENPP1 OMIM 173335**; **ABCC6 OMIM 603234** (yao2023clinicalandmolecular pages 1-2).

**Not found in retrieved sources:** Orphanet ID, ICD-10/ICD-11 codes, MeSH ID, and a MONDO ID were not present in the retrieved full texts; these should be added from authoritative terminologies (e.g., Orphanet, MONDO, MeSH browser) during knowledge-base curation.

### 1.3 Synonyms / alternative names
Commonly used terms in recent and historical clinical literature:
- **Generalized arterial calcification of infancy (GACI)**
- **Arterial calcification of infancy**
- **Idiopathic infantile arterial calcification (IIAC)** (mulcahy2019antenataldiagnosisof pages 6-6, mulcahy2019antenataldiagnosisof pages 1-3)

### 1.4 Evidence sources
Evidence in the retrieved corpus derives from both aggregated disease-level resources (multi-country record reviews; prospective phenotyping cohorts) and individual case reports/series, spanning fetal ultrasound diagnosis through adult survivorship phenotypes (ferreira2021ectopiccalcificationand pages 1-2, ferreira2021prospectivephenotypingof pages 1-3, mulcahy2019antenataldiagnosisof pages 1-3).

## 2. Etiology
### 2.1 Disease causal factors
**Primary causal factors (genetic):**
- **ENPP1 deficiency:** biallelic inactivating variants account for ~67–75% of reported cases, depending on the dataset reviewed (ferreira2021ectopiccalcificationand pages 1-2, ferreira2021prospectivephenotypingof pages 1-3, yao2023clinicalandmolecular pages 1-2).
- **ABCC6 deficiency:** biallelic pathogenic variants account for ~9–10% of reported cases (ferreira2021ectopiccalcificationand pages 1-2, yao2023clinicalandmolecular pages 1-2).

### 2.2 Risk factors
- **Genetic risk:** autosomal recessive inheritance with biallelic pathogenic variants in ENPP1/ABCC6 (yao2023clinicalandmolecular pages 1-2, mulcahy2019antenataldiagnosisof pages 1-3).
- **Gene–environment interaction (prenatal detection context):** Prenatal ultrasound findings (hyperechogenic fetal vasculature, polyhydramnios, abnormal Dopplers) are described as key signals that can trigger early diagnosis and management, suggesting perinatal physiology and hemodynamics may influence clinical presentation, although the retrieved texts do not quantify specific environmental risk effect sizes (mulcahy2019antenataldiagnosisof pages 1-3).

### 2.3 Protective factors
The retrieved human clinical texts did not provide validated protective factors. A therapeutic review notes dietary magnesium as protective in mouse models of ENPP1/ABCC6-related ectopic calcification and reports a small PXE RCT with histological improvement, but this is not specific, validated prevention for GACI in humans (davies2023futuretreatmentsfor pages 3-4).

## 3. Phenotypes (clinical presentation)
### 3.1 Core phenotype spectrum
Across reviews and cohort analyses, GACI commonly includes:
- **Arterial calcification and stenosis** of large and medium arteries (aorta, coronary, pulmonary, renal and others), often with fibrointimal hyperplasia and luminal narrowing (khan2018enpp1enzymereplacement pages 1-3, boyce2020generalizedarterialcalcification pages 1-2).
- **Severe systemic hypertension** and **heart failure** in infancy (yao2023clinicalandmolecular pages 1-2, ferreira2024enpp1inblood pages 2-4).
- **Prenatal manifestations:** hydrops fetalis, polyhydramnios, fetal distress; ultrasound evidence of hyperechogenic vasculature/valves (boyce2020generalizedarterialcalcification pages 1-2, mulcahy2019antenataldiagnosisof pages 1-3).
- **Later manifestations among survivors (especially ENPP1 deficiency):** elevated intact FGF23 and phosphate-wasting hypophosphatemic rickets (ARHR2), enthesis calcification, hearing loss, and cervical spine fusion (ferreira2021prospectivephenotypingof pages 1-3).

**Quantitative distribution by onset (literature review):** In a review of 161 patients, 48% were categorized as early-onset (in utero/shortly after birth) and 52% late-onset (median 3 months) (boyce2020generalizedarterialcalcification pages 1-2).

### 3.2 Phenotype characteristics: onset, severity, progression
- **Onset:** as early as the **second trimester**; many infants present within the first week(s) of life with stroke, severe hypertension, and cardiac failure (ferreira2024enpp1inblood pages 1-2, ferreira2024enpp1inblood pages 2-4).
- **Progression/regression:** Imaging literature highlights that calcifications may diminish/disappear spontaneously or after treatment, whereas stenoses may persist or progress; CT/CTA is emphasized for longitudinal follow-up (ramirezsuarez2022longitudinalassessmentof pages 8-9).

### 3.3 Phenotype frequencies (selected statistics)
From a multi-country natural history record review of 247 individuals:
- Arterial calcification prevalence in ENPP1 vs ABCC6 deficiency: **77.2% vs 89.5%**
- Organ calcification: **65.8% vs 84.2%**
- Cardiovascular complications: **58.4% vs 78.9%**
- Rickets among survivors: **70.8%** (ENPP1) vs **11.8%** (ABCC6) (ferreira2021ectopiccalcificationand pages 1-2).

### 3.4 Quality of life impact
Formal QoL instruments (e.g., EQ-5D/SF-36) were not reported in the retrieved corpus. However, morbidity among long-term ENPP1-deficient survivors includes high rates of hearing loss and adult enthesis-related symptoms, implying substantial long-term functional impact (ferreira2021prospectivephenotypingof pages 1-3).

### 3.5 Suggested HPO terms (examples)
(Conceptual mapping based on described phenotypes; ontology IDs should be validated during curation)
- Hypertension; Heart failure; Cardiomegaly; Myocardial ischemia; Arterial stenosis; Vascular calcification; Pulmonary stenosis; Hydrops fetalis; Polyhydramnios; Hypophosphatemia; Hyperphosphaturia; Rickets; Hearing impairment; Enthesopathy; Cervical vertebral fusion (boyce2020generalizedarterialcalcification pages 1-2, ferreira2021prospectivephenotypingof pages 1-3, yao2023clinicalandmolecular pages 1-2, mulcahy2019antenataldiagnosisof pages 1-3).

## 4. Genetic / molecular information
### 4.1 Causal genes
- **ENPP1** (ectonucleotide pyrophosphatase/phosphodiesterase 1): key enzyme generating extracellular PPi from ATP; loss-of-function causes the predominant GACI subtype (khan2018enpp1enzymereplacement pages 1-3, yao2023clinicalandmolecular pages 1-2).
- **ABCC6** (ATP-binding cassette subfamily C member 6): liver-predominant transporter implicated upstream in ATP efflux needed for extracellular PPi generation; biallelic ABCC6 mutations can cause GACI and overlap with pseudoxanthoma elasticum (PXE) phenotypes (yao2023clinicalandmolecular pages 1-2, yao2023clinicalandmolecular pages 5-7).

### 4.2 Pathogenic variants: classes and examples
- **ENPP1:** nonsense/splice/frameshift variants are reported; a 2024 family study identified a novel splice-site variant (NM_006208 c.2230+5G>A) with exon skipping and loss of function, and showed patient fibroblasts with increased calcification and decreased ENPP1 activity (BMC Pediatrics; 2024-11; URL https://doi.org/10.1186/s12887-024-05123-0) (yao2023clinicalandmolecular pages 5-7).
- **ABCC6:** a 2023 clinical report identified biallelic ABCC6 variants including a frameshift duplication (c.4223_4227dupAGCTC) plus a multi-exon deletion detected via combined sequencing and CNV validation (J Pers Med; 2023-12; URL https://doi.org/10.3390/jpm14010054) (yao2023clinicalandmolecular pages 5-7, yao2023clinicalandmolecular pages 1-2).

**Variant classification and population frequencies:** ACMG classes and gnomAD allele frequencies were not extractable from the retrieved full texts and should be curated from ClinVar/gnomAD.

### 4.3 Modifier genes / oligogenicity
No GACI-specific validated modifier genes were identified in the retrieved corpus. A separate PXE study supports the concept of modifier variants in ectopic calcification disorders (not GACI-specific) (mulcahy2019antenataldiagnosisof pages 6-6).

## 5. Environmental information
GACI is primarily Mendelian. The retrieved sources emphasize prenatal ultrasound findings and perinatal clinical management; no specific toxins, infectious triggers, or lifestyle contributors were supported as causal for GACI in the retrieved texts (mulcahy2019antenataldiagnosisof pages 1-3).

## 6. Mechanism / pathophysiology
### 6.1 Core pathway: extracellular ATP → PPi/adenosine axis
Mechanistic consensus across reviews and experimental work:
- **ENPP1 hydrolyzes extracellular ATP → AMP + PPi**, where **PPi** inhibits hydroxyapatite crystal growth and thus inhibits ectopic calcification (khan2018enpp1enzymereplacement pages 1-3, ferreira2024enpp1inblood pages 1-2).
- **ABCC6** functions upstream, supporting ATP efflux into the circulation; reduced ABCC6 (or ENPP1) decreases extracellular PPi, shifting the Pi/PPi ratio toward mineral deposition (davies2023futuretreatmentsfor pages 2-3, yao2023clinicalandmolecular pages 1-2).
- Reduced AMP/adenosine signaling is implicated in **myointimal proliferation** and stenosis as an additional disease driver beyond calcification (boyce2020generalizedarterialcalcification pages 1-2, davies2023futuretreatmentsfor pages 4-5).

### 6.2 Causal chain (from trigger to clinical manifestation)
1) Biallelic ENPP1 (or ABCC6) loss-of-function → 2) reduced extracellular ATP metabolism to PPi (and reduced AMP/adenosine) → 3) low circulating/local PPi (loss of mineralization inhibition) → 4) hydroxyapatite deposition in arterial wall (often along internal elastic lamina) + intimal proliferation → 5) arterial stiffening, stenosis, impaired perfusion → 6) severe hypertension, cardiac failure, ischemic injury in neonates/infants; in survivors, compensatory endocrine shifts (FGF23 elevation) contribute to phosphate wasting and rickets (ferreira2024enpp1inblood pages 2-4, ferreira2021ectopiccalcificationand pages 1-2).

### 6.3 Suggested GO biological processes / CL cell types (examples)
(Conceptual mapping; IDs should be validated during curation)
- GO: extracellular nucleotide metabolic process; regulation of biomineral tissue development; negative regulation of calcification; vascular smooth muscle cell proliferation; regulation of phosphate metabolic process.
- CL: vascular smooth muscle cell; endothelial cell; fibroblast (supported by described arterial wall involvement and fibroblast functional assays in ENPP1 variant studies) (khan2018enpp1enzymereplacement pages 1-3, yao2023clinicalandmolecular pages 5-7).

### 6.4 Visual evidence (preclinical mechanism and rescue)
A seminal preclinical study demonstrated prevention of vascular calcification in ENPP1-deficient mice treated with ENPP1-Fc, including a pathway schematic and microCT/histology panels showing untreated vs treated arterial calcification (albright2015enpp1fcpreventsmortality media efff4671, albright2015enpp1fcpreventsmortality media 49e3e09b, albright2015enpp1fcpreventsmortality media e0d27b7a).

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
Primary: cardiovascular system—medium/large arteries (aorta, coronary, pulmonary, renal arteries; also hepatic artery depending on onset category) (boyce2020generalizedarterialcalcification pages 1-2).

Secondary/complications: heart (heart failure/cardiomyopathy/ischemia), kidneys (renovascular hypertension; renal involvement), and potentially multi-organ calcifications (yao2023clinicalandmolecular pages 1-2, ferreira2021ectopiccalcificationand pages 1-2).

### 7.2 Suggested UBERON mappings (examples)
Aorta; coronary artery; pulmonary artery; renal artery; hepatic artery; arterial wall/internal elastic lamina (boyce2020generalizedarterialcalcification pages 1-2).

## 8. Temporal development
### 8.1 Onset
- Prenatal (second trimester) to early infancy is typical (ferreira2024enpp1inblood pages 2-4).

### 8.2 Critical period and progression
- A major “critical period” is the first **6 months**, during which a large fraction of mortality occurs (ferreira2021ectopiccalcificationand pages 1-2).
- Longitudinal imaging suggests calcification may regress, but stenosis can persist/progress, motivating long-term surveillance (ramirezsuarez2022longitudinalassessmentof pages 8-9).

## 9. Inheritance and population
### 9.1 Inheritance
- **Autosomal recessive** (yao2023clinicalandmolecular pages 1-2, mulcahy2019antenataldiagnosisof pages 1-3).

### 9.2 Epidemiology (recent quantitative data)
- **Minimal incidence estimate:** prospective survivor phenotyping estimated the minimal incidence of ENPP1 deficiency at **~1 in 200,000 pregnancies** (Genet Med; 2021-02; URL https://doi.org/10.1038/s41436-020-00983-0) (ferreira2021prospectivephenotypingof pages 1-3).
- A 2023 report similarly cites incidence about **1 in 200,000 pregnancies** and a **carrier rate ≈1 in 200** (yao2023clinicalandmolecular pages 1-2).

## 10. Diagnostics
### 10.1 Clinical and imaging diagnostics
- **Prenatal ultrasound:** hyperechogenic fetal vasculature/valves; ventricular dysfunction; pericardial effusion; polyhydramnios; abnormal Dopplers—supporting prenatal suspicion and enabling earlier counseling and molecular testing (mulcahy2019antenataldiagnosisof pages 1-3).
- **Postnatal imaging:** whole-body CT, non-contrast CT, and CT angiography are emphasized for detection and longitudinal assessment, including persistent/progressive stenoses even if calcifications regress (ramirezsuarez2022longitudinalassessmentof pages 8-9, yao2023clinicalandmolecular pages 5-7).

### 10.2 Laboratory/biomarker diagnostics
- **Plasma PPi deficiency** is central; historical low PPi values are described (e.g., ~0.6 μmol/L with normal 1–6 μmol/L in ENPP1 deficiency review excerpt) (ferreira2024enpp1inblood pages 2-4).
- In survivors with ENPP1 deficiency: **elevated intact FGF23** and evolving phosphate wasting/rickets are common (ferreira2021prospectivephenotypingof pages 1-3).

### 10.3 Genetic testing
- Genetic confirmation is typically via sequencing (gene panels/WES) and may require CNV detection and qPCR confirmation, as illustrated in ABCC6-related GACI (yao2023clinicalandmolecular pages 1-2).

### 10.4 Differential diagnosis
The retrieved corpus includes discussion of misdiagnosis (e.g., inflammatory arteriopathies) in ENPP1-related arterial stenoses outside infancy, emphasizing the value of genetic testing and imaging in atypical presentations (tanaka2024preterminfantwith pages 8-9).

## 11. Outcome / prognosis
### 11.1 Mortality statistics
A large record-based natural history study reported:
- **Overall mortality:** 54.7% (including 13.4% in utero/stillborn)
- **Probability of death before 6 months:** 50.4%
- **Higher mortality for ENPP1 vs ABCC6:** 40.5% vs 10.5% (p=0.0157) (JBMR; 2021-11; URL https://doi.org/10.1002/jbmr.4418) (ferreira2021ectopiccalcificationand pages 1-2).

Other sources report similar early mortality on the order of ~55–60% by 6 months (ferreira2021prospectivephenotypingof pages 1-3, yao2023clinicalandmolecular pages 1-2), and historical reports cite up to ~85% liveborn mortality within 6 months in older case series contexts (mulcahy2019antenataldiagnosisof pages 1-3).

### 11.2 Morbidity in long-term survivors
In a prospective cohort of 20 long-term survivors, ENPP1-deficient individuals showed substantial late morbidity:
- Lifetime risk of **hearing loss ~75%**
- Lifetime risk of **cervical spine fusion ~25%**
- Adult morbidity often related to **enthesis calcification** (ferreira2021prospectivephenotypingof pages 1-3).

## 12. Treatment
### 12.1 Current applications / real-world implementations
**Bisphosphonates (off-label):** Bisphosphonates are PPi analogs used in practice, including etidronate and IV pamidronate. A 2024 case report in a preterm infant emphasizes early diagnosis and bisphosphonate adjustments: the abstract states, “GACI causes severe hypertension and heart failure, and approximately 50% of patients die within the first 6 months… Bisphosphonates are effective in treating GACI; however, no standardized treatment regimen is available.” (Children; 2024-09; URL https://doi.org/10.3390/children11101176) (tanaka2024preterminfantwith pages 8-9).

**Evidence limitations:** In contrast to earlier impressions, a large natural history review found **no survival benefit** from bisphosphonates in a start-time matched analysis, with inconclusive benefit when initiated within 2 weeks of birth (ferreira2021ectopiccalcificationand pages 1-2). This discrepancy underscores the heterogeneity of retrospective clinical datasets and the need for controlled trials.

### 12.2 Disease-targeted and emerging therapies (2023–2024 priority)
**ENPP1 enzyme replacement / PPi restoration:**
- Expert review (2024) describes “bench-to-bedside development of a novel ENPP1 biologics designed to treat mineralization disorders” and notes preclinical and clinical development of recombinant ENPP1 therapies including INZ-701 (Annual Review of Pathology; 2024-01; URL https://doi.org/10.1146/annurev-pathmechdis-051222-121126) (ferreira2024enpp1inblood pages 24-26).
- A 2023 expert therapeutic review positions ENPP1 replacement as a leading strategy, supported by preclinical benefits on calcification and cardiovascular function in ENPP1-deficient mice and normalization of biomarkers; it also highlights the unmet need for therapies that **reverse established calcification** (davies2023futuretreatmentsfor pages 1-2, davies2023futuretreatmentsfor pages 4-5).

**TNAP inhibition / anti-calcification strategies:** A 2023 therapeutic review discusses TNAP inhibition as a PPi-preserving strategy but notes that as of March 2023 no human TNAP inhibitor trials in GACI were registered (in the reviewed context) and reports mixed preclinical results across models (davies2023futuretreatmentsfor pages 4-5).

**Chelator nanoparticle approaches (expert opinion):** Davies et al. (2023) highlight antibody-targeted nanoparticle delivery of chelators (e.g., EDTA) as a promising class that in animals can reverse established arterial calcification and restore arterial elasticity, potentially complementing PPi-restoring therapies (davies2023futuretreatmentsfor pages 1-2).

### 12.3 Clinical trials (INZ-701; ClinicalTrials.gov)
**ENERGY 2 (infants; Phase 3):** NCT07473973 is a Phase 3 single-arm open-label study of weekly subcutaneous INZ-701 in infants ≤1 year with genetically confirmed ENPP1 deficiency, with primary endpoints including **change in plasma PPi** and **overall survival** through Week 52. Dates: start 2025-03-26; first posted 2026-03-16; estimated primary completion 2028-09-11 (NCT07473973 chunk 1). URL: https://clinicaltrials.gov/study/NCT07473973 (NCT07473973 chunk 1).

**ADAPT (long-term safety; Phase 2):** NCT06462547 is an open-label Phase 2 long-term safety study for those previously treated with INZ-701, assessing TEAEs and anti-drug antibodies, with secondary PK/PD including plasma PPi change; first posted 2024-06-17; actual start 2024-06-19; estimated completion 2030-12 (NCT06462547 chunk 1). URL: https://clinicaltrials.gov/study/NCT06462547 (NCT06462547 chunk 1).

**Additional INZ-701 trials:** ENERGY (infants with ENPP1 or ABCC6 deficiency; NCT05734196) and ENERGY 3 (children with ENPP1 deficiency; NCT06046820) were retrieved but key endpoints/dates were not present in the extracted chunks and should be confirmed directly from the ClinicalTrials.gov record (NCT05734196 chunk 2, NCT06046820 chunk 2).

### 12.4 MAXO term suggestions (examples)
(Conceptual mapping; IDs should be validated during curation)
- Bisphosphonate therapy; Enzyme replacement therapy; Genetic testing; Computed tomography angiography; Prenatal ultrasonography; Antihypertensive therapy; Phosphate supplementation; Active vitamin D therapy (tanaka2024preterminfantwith pages 8-9, ramirezsuarez2022longitudinalassessmentof pages 8-9).

## 13. Prevention
No validated primary prevention strategies were reported for GACI in the retrieved corpus. Secondary prevention via **prenatal detection** (ultrasound) and early neonatal recognition is emphasized to enable early specialist management and genetic confirmation (mulcahy2019antenataldiagnosisof pages 1-3).

## 14. Other species / natural disease
The retrieved texts did not report naturally occurring veterinary analogs with NCBI Taxon IDs.

## 15. Model organisms
### 15.1 Mammalian models and utility
Mouse ENPP1-deficient models (e.g., Enpp1asj / related ENPP1-deficiency strains) are repeatedly used to model the arterial mineralization phenotype and evaluate ENPP1-Fc therapies (khan2018enpp1enzymereplacement pages 1-3, davies2023futuretreatmentsfor pages 4-5).

### 15.2 Preclinical therapeutic proof-of-concept
- ENPP1 enzyme replacement in ENPP1-deficient mice reduced aortic calcification by **>95%** in a prevention study and improved hemodynamics/cardiac function in longer dosing (khan2018enpp1enzymereplacement pages 1-3).
- Visual evidence from ENPP1-Fc treatment experiments shows marked calcification in untreated animals and absence of calcification with ENPP1-Fc therapy (albright2015enpp1fcpreventsmortality media efff4671, albright2015enpp1fcpreventsmortality media 49e3e09b, albright2015enpp1fcpreventsmortality media e0d27b7a).

### 15.3 Model limitations
Even in ENPP1 deficiency review contexts, authors note challenges: established calcification may be present at birth (in humans), implying that prevention models may not fully capture reversal needs; therapies may need to address both calcification and stenosis/intimal proliferation (davies2023futuretreatmentsfor pages 1-2, davies2023futuretreatmentsfor pages 4-5).

---

## Structured quick-reference table
| Topic | Summary |
|---|---|
| Identifiers | Generalized arterial calcification of infancy (GACI); OMIM 208000 for GACI, with GACI1 OMIM:208000 and GACI2 OMIM:614473 noted in imaging literature; causal genes include ENPP1 (OMIM 173335) and ABCC6 (OMIM 603234) (yao2023clinicalandmolecular pages 1-2, ramirezsuarez2022longitudinalassessmentof pages 8-9) |
| Synonyms | Arterial calcification of infancy, generalized arterial calcification of infancy, idiopathic infantile arterial calcification (IIAC); literature uses GACI and IIAC for the neonatal vascular calcification syndrome (yao2023clinicalandmolecular pages 1-2, mulcahy2019antenataldiagnosisof pages 6-6, mulcahy2019antenataldiagnosisof pages 1-3) |
| Inheritance/Epidemiology | Autosomal recessive disorder caused by biallelic pathogenic variants; estimated minimal incidence of ENPP1 deficiency is ~1 in 200,000 pregnancies, with carrier rate ~1 in 200 reported in one review/case report; just over ~200 cases have been described in the literature (ferreira2021prospectivephenotypingof pages 1-3, yao2023clinicalandmolecular pages 1-2, mulcahy2019antenataldiagnosisof pages 1-3) |
| Causal genes and proportions | ENPP1 accounts for ~67% to ~75% of reported cases, while ABCC6 accounts for ~9% to ~10%; ENPP1 is the predominant cause, with ABCC6 representing a smaller but important overlapping subtype (ferreira2021ectopiccalcificationand pages 1-2, ferreira2021prospectivephenotypingof pages 1-3, yao2023clinicalandmolecular pages 1-2) |
| Core pathophysiology | ENPP1 hydrolyzes extracellular ATP to AMP + inorganic pyrophosphate (PPi); PPi is a major inhibitor of hydroxyapatite deposition, so ENPP1 loss lowers PPi and promotes vascular calcification; reduced AMP/adenosine signaling may also contribute to intimal proliferation and stenosis. ABCC6 acts upstream by promoting ATP efflux needed for extracellular PPi generation, linking ABCC6 deficiency to the same low-PPi pathway (boyce2020generalizedarterialcalcification pages 1-2, ferreira2024enpp1inblood pages 1-2, yao2023clinicalandmolecular pages 1-2) |
| Key phenotypes | Hallmarks are calcification and stenosis of large/medium arteries with severe hypertension, heart failure, myocardial ischemia, cardiomegaly, respiratory distress, cyanosis, diminished pulses, and fetal findings such as hydrops fetalis/polyhydramnios. In a 161-patient review, 48% were early-onset and 52% late-onset (median 3 months); arterial calcification was reported in 77.2% of ENPP1 and 89.5% of ABCC6 cases, organ calcification in 65.8% and 84.2%, and cardiovascular complications in 58.4% and 78.9%, respectively (boyce2020generalizedarterialcalcification pages 1-2, ferreira2021ectopiccalcificationand pages 1-2, ferreira2024enpp1inblood pages 2-4) |
| Diagnostics | Prenatal ultrasound may show hyperechogenic fetal vasculature, echogenic valves, ventricular dysfunction, pericardial effusion, polyhydramnios, and abnormal Dopplers; postnatal whole-body CT/non-contrast CT and CT angiography are emphasized for detecting calcification and monitoring persistent/progressive stenoses. Molecular diagnosis uses WES/panel testing and CNV analysis with qPCR confirmation when needed (yao2023clinicalandmolecular pages 1-2, ramirezsuarez2022longitudinalassessmentof pages 8-9, mulcahy2019antenataldiagnosisof pages 1-3) |
| Treatments/Trials | Bisphosphonates (e.g., etidronate, pamidronate, zoledronic acid) are used off-label, but evidence is inconsistent and no standard regimen exists; one natural history study found no survival benefit in start-time matched analyses. ENPP1 replacement is the leading disease-targeted strategy: rhENPP1/ENPP1-Fc reduced aortic calcification by >95% in mouse studies and improved blood pressure/cardiac function; INZ-701 is in clinical development with completed adult phase 1/2 testing and recruiting/active pediatric studies including ENERGY (NCT05734196), ENERGY 3 (NCT06046820), ADAPT (NCT06462547), and infant phase 3 ENERGY 2 (NCT07473973) (khan2018enpp1enzymereplacement pages 1-3, ferreira2021ectopiccalcificationand pages 1-2, ferreira2024enpp1inblood pages 24-26, tanaka2024preterminfantwith pages 8-9) |
| Prognosis statistics | Prognosis is poor in infancy: overall mortality 54.7% in a 247-record natural history cohort, including 13.4% in utero/stillborn, with a 50.4% probability of death before 6 months; other sources report ~55% mortality within 6 months, ~60% dying within 6 months, and historical liveborn mortality up to ~85%. Infants often present within the first week of life or even in the second trimester prenatally (ferreira2021ectopiccalcificationand pages 1-2, ferreira2021prospectivephenotypingof pages 1-3, yao2023clinicalandmolecular pages 1-2, ferreira2024enpp1inblood pages 2-4, mulcahy2019antenataldiagnosisof pages 1-3) |
| Notes on ENPP1 vs ABCC6 | Mortality is higher with ENPP1 than ABCC6 variants (40.5% vs 10.5%, p=0.0157 in one cohort). Hypophosphatemic rickets is far more common in surviving ENPP1 deficiency than ABCC6 deficiency (70.8% vs 11.8%, p=0.0001), supporting a spectrum from infant vascular calcification to later ARHR2 in ENPP1 deficiency; ENPP1-deficient survivors also showed elevated FGF23, hearing loss risk ~75%, and cervical spine fusion risk ~25% (ferreira2021ectopiccalcificationand pages 1-2, ferreira2021prospectivephenotypingof pages 1-3) |


*Table: This table condenses the highest-yield evidence on Arterial Calcification of Infancy/Generalized Arterial Calcification of Infancy, including identifiers, genetics, mechanism, phenotype, diagnostics, treatment development, and prognosis. It is useful as a structured insert for a disease knowledge base entry.*

---

## Key recent sources (2023–2024 emphasized)
- Ferreira CR, Carpenter TO, Braddock DT. **Annual Review of Pathology** (2024-01-??). “ENPP1 in Blood and Bone…” https://doi.org/10.1146/annurev-pathmechdis-051222-121126 (ferreira2024enpp1inblood pages 24-26, ferreira2024enpp1inblood pages 1-2).
- Davies BM et al. **Frontiers in Drug Discovery** (2023-11-??). “Future treatments for the arteriopathy of ectopic calcification disorders” https://doi.org/10.3389/fddsv.2023.1249966 (davies2023futuretreatmentsfor pages 1-2, davies2023futuretreatmentsfor pages 4-5).
- Yao R et al. **Journal of Personalized Medicine** (2023-12-??). ABCC6-related GACI case/identifiers/epidemiology https://doi.org/10.3390/jpm14010054 (yao2023clinicalandmolecular pages 1-2, yao2023clinicalandmolecular pages 5-7).
- Tanaka M et al. **Children** (2024-09-??). Preterm GACI treated with bisphosphonates https://doi.org/10.3390/children11101176 (tanaka2024preterminfantwith pages 8-9).

## Limitations of this report
Several requested ontology identifiers (Orphanet, ICD-10/11, MeSH, MONDO) and variant-level population frequency details (ClinVar/gnomAD) were not present in the retrieved full texts and therefore could not be cited. These should be added from the respective authoritative databases during knowledge-base integration.

References

1. (ferreira2021ectopiccalcificationand pages 1-2): Carlos R Ferreira, Kristina Kintzinger, Mary E Hackbarth, Ulrike Botschen, Yvonne Nitschke, M Zulf Mughal, Genevieve Baujat, Dirk Schnabel, Eric Yuen, William A Gahl, Rachel I Gafni, Qing Liu, Pedro Huertas, Gus Khursigara, and Frank Rutsch. Ectopic calcification and hypophosphatemic rickets: natural history of enpp1 and abcc6 deficiencies. Journal of Bone and Mineral Research, 36:2193-2202, Nov 2021. URL: https://doi.org/10.1002/jbmr.4418, doi:10.1002/jbmr.4418. This article has 83 citations and is from a highest quality peer-reviewed journal.

2. (yao2023clinicalandmolecular pages 1-2): Ruen Yao, Fan Yang, Qianwen Zhang, Tingting Yu, Ying Yu, Guoying Chang, and Xiumin Wang. Clinical and molecular characterization of a patient with generalized arterial calcification of infancy caused by rare abcc6 mutation. Journal of Personalized Medicine, 14:54, Dec 2023. URL: https://doi.org/10.3390/jpm14010054, doi:10.3390/jpm14010054. This article has 5 citations.

3. (ferreira2024enpp1inblood pages 24-26): Carlos R. Ferreira, Thomas O. Carpenter, and Demetrios T. Braddock. Enpp1 in blood and bone: skeletal and soft tissue diseases induced by enpp1 deficiency. Annual Review of Pathology: Mechanisms of Disease, 19:507-540, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051222-121126, doi:10.1146/annurev-pathmechdis-051222-121126. This article has 43 citations and is from a domain leading peer-reviewed journal.

4. (davies2023futuretreatmentsfor pages 1-2): Benjamin M. Davies, Frank Rutsch, Naren Vyavahare, and Alexander Jones. Future treatments for the arteriopathy of ectopic calcification disorders. Frontiers in Drug Discovery, Nov 2023. URL: https://doi.org/10.3389/fddsv.2023.1249966, doi:10.3389/fddsv.2023.1249966. This article has 1 citations.

5. (ferreira2024enpp1inblood pages 1-2): Carlos R. Ferreira, Thomas O. Carpenter, and Demetrios T. Braddock. Enpp1 in blood and bone: skeletal and soft tissue diseases induced by enpp1 deficiency. Annual Review of Pathology: Mechanisms of Disease, 19:507-540, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051222-121126, doi:10.1146/annurev-pathmechdis-051222-121126. This article has 43 citations and is from a domain leading peer-reviewed journal.

6. (ferreira2024enpp1inblood pages 2-4): Carlos R. Ferreira, Thomas O. Carpenter, and Demetrios T. Braddock. Enpp1 in blood and bone: skeletal and soft tissue diseases induced by enpp1 deficiency. Annual Review of Pathology: Mechanisms of Disease, 19:507-540, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051222-121126, doi:10.1146/annurev-pathmechdis-051222-121126. This article has 43 citations and is from a domain leading peer-reviewed journal.

7. (khan2018enpp1enzymereplacement pages 1-3): Tayeba Khan, Kerstin W. Sinkevicius, Sylvia Vong, Arlen Avakian, Markley C. Leavitt, Hunter Malanson, Andre Marozsan, and Kim L. Askew. Enpp1 enzyme replacement therapy improves blood pressure and cardiovascular function in a mouse model of generalized arterial calcification of infancy. Disease Models & Mechanisms, Oct 2018. URL: https://doi.org/10.1242/dmm.035691, doi:10.1242/dmm.035691. This article has 48 citations and is from a domain leading peer-reviewed journal.

8. (ramirezsuarez2022longitudinalassessmentof pages 8-9): Karen I. Ramirez-Suarez, Sara A. Cohen, Christian A. Barrera, Michael A. Levine, David J. Goldberg, and Hansel J. Otero. Longitudinal assessment of vascular calcification in generalized arterial calcification of infancy. Pediatric Radiology, 52:2329-2341, Apr 2022. URL: https://doi.org/10.1007/s00247-022-05364-0, doi:10.1007/s00247-022-05364-0. This article has 19 citations and is from a peer-reviewed journal.

9. (mulcahy2019antenataldiagnosisof pages 6-6): C. H. Mulcahy, F. Mone, F. M. McAuliffe, E. Mooney, P. McParland, and C. J. Mc Mahon. Antenatal diagnosis of idiopathic infantile arterial calcification (iiac): a single centre experience and review of the literature. Journal of Congenital Cardiology, 3:1-6, Dec 2019. URL: https://doi.org/10.1186/s40949-018-0022-1, doi:10.1186/s40949-018-0022-1. This article has 13 citations.

10. (mulcahy2019antenataldiagnosisof pages 1-3): C. H. Mulcahy, F. Mone, F. M. McAuliffe, E. Mooney, P. McParland, and C. J. Mc Mahon. Antenatal diagnosis of idiopathic infantile arterial calcification (iiac): a single centre experience and review of the literature. Journal of Congenital Cardiology, 3:1-6, Dec 2019. URL: https://doi.org/10.1186/s40949-018-0022-1, doi:10.1186/s40949-018-0022-1. This article has 13 citations.

11. (ferreira2021prospectivephenotypingof pages 1-3): Carlos R. Ferreira, Mary E. Hackbarth, Shira G. Ziegler, Kristen S. Pan, Mary S. Roberts, Douglas R. Rosing, Margaret S. Whelpley, Joy C. Bryant, Ellen F. Macnamara, Sisi Wang, Kerstin Müller, Iris R. Hartley, Emily Y. Chew, Timothy E. Corden, Christina M. Jacobsen, Ingrid A. Holm, Frank Rutsch, Esra Dikoglu, Marcus Y. Chen, M. Zulf Mughal, Michael A. Levine, Rachel I. Gafni, and William A. Gahl. Prospective phenotyping of long-term survivors of generalized arterial calcification of infancy (gaci). Genetics in Medicine, 23:396-407, Feb 2021. URL: https://doi.org/10.1038/s41436-020-00983-0, doi:10.1038/s41436-020-00983-0. This article has 97 citations and is from a highest quality peer-reviewed journal.

12. (davies2023futuretreatmentsfor pages 3-4): Benjamin M. Davies, Frank Rutsch, Naren Vyavahare, and Alexander Jones. Future treatments for the arteriopathy of ectopic calcification disorders. Frontiers in Drug Discovery, Nov 2023. URL: https://doi.org/10.3389/fddsv.2023.1249966, doi:10.3389/fddsv.2023.1249966. This article has 1 citations.

13. (boyce2020generalizedarterialcalcification pages 1-2): Alison M. Boyce, Rachel I. Gafni, and Carlos R. Ferreira. Generalized arterial calcification of infancy: new insights, controversies, and approach to management. Current Osteoporosis Reports, 18:232-241, Mar 2020. URL: https://doi.org/10.1007/s11914-020-00577-4, doi:10.1007/s11914-020-00577-4. This article has 50 citations and is from a peer-reviewed journal.

14. (yao2023clinicalandmolecular pages 5-7): Ruen Yao, Fan Yang, Qianwen Zhang, Tingting Yu, Ying Yu, Guoying Chang, and Xiumin Wang. Clinical and molecular characterization of a patient with generalized arterial calcification of infancy caused by rare abcc6 mutation. Journal of Personalized Medicine, 14:54, Dec 2023. URL: https://doi.org/10.3390/jpm14010054, doi:10.3390/jpm14010054. This article has 5 citations.

15. (davies2023futuretreatmentsfor pages 2-3): Benjamin M. Davies, Frank Rutsch, Naren Vyavahare, and Alexander Jones. Future treatments for the arteriopathy of ectopic calcification disorders. Frontiers in Drug Discovery, Nov 2023. URL: https://doi.org/10.3389/fddsv.2023.1249966, doi:10.3389/fddsv.2023.1249966. This article has 1 citations.

16. (davies2023futuretreatmentsfor pages 4-5): Benjamin M. Davies, Frank Rutsch, Naren Vyavahare, and Alexander Jones. Future treatments for the arteriopathy of ectopic calcification disorders. Frontiers in Drug Discovery, Nov 2023. URL: https://doi.org/10.3389/fddsv.2023.1249966, doi:10.3389/fddsv.2023.1249966. This article has 1 citations.

17. (albright2015enpp1fcpreventsmortality media efff4671): Ronald A. Albright, Paul Stabach, Wenxiang Cao, Dillon Kavanagh, Isabelle Mullen, Alexander A. Braddock, Mariel S. Covo, Martin Tehan, Guangxiao Yang, Zhiliang Cheng, Keith Bouchard, Zhao-Xue Yu, Stephanie Thorn, Xiangning Wang, Ewa J. Folta-Stogniew, Alejandro Negrete, Albert J. Sinusas, Joseph Shiloach, George Zubal, Joseph A. Madri, Enrique M. De La Cruz, and Demetrios T. Braddock. Enpp1-fc prevents mortality and vascular calcifications in rodent model of generalized arterial calcification of infancy. Nature Communications, Dec 2015. URL: https://doi.org/10.1038/ncomms10006, doi:10.1038/ncomms10006. This article has 175 citations and is from a highest quality peer-reviewed journal.

18. (albright2015enpp1fcpreventsmortality media 49e3e09b): Ronald A. Albright, Paul Stabach, Wenxiang Cao, Dillon Kavanagh, Isabelle Mullen, Alexander A. Braddock, Mariel S. Covo, Martin Tehan, Guangxiao Yang, Zhiliang Cheng, Keith Bouchard, Zhao-Xue Yu, Stephanie Thorn, Xiangning Wang, Ewa J. Folta-Stogniew, Alejandro Negrete, Albert J. Sinusas, Joseph Shiloach, George Zubal, Joseph A. Madri, Enrique M. De La Cruz, and Demetrios T. Braddock. Enpp1-fc prevents mortality and vascular calcifications in rodent model of generalized arterial calcification of infancy. Nature Communications, Dec 2015. URL: https://doi.org/10.1038/ncomms10006, doi:10.1038/ncomms10006. This article has 175 citations and is from a highest quality peer-reviewed journal.

19. (albright2015enpp1fcpreventsmortality media e0d27b7a): Ronald A. Albright, Paul Stabach, Wenxiang Cao, Dillon Kavanagh, Isabelle Mullen, Alexander A. Braddock, Mariel S. Covo, Martin Tehan, Guangxiao Yang, Zhiliang Cheng, Keith Bouchard, Zhao-Xue Yu, Stephanie Thorn, Xiangning Wang, Ewa J. Folta-Stogniew, Alejandro Negrete, Albert J. Sinusas, Joseph Shiloach, George Zubal, Joseph A. Madri, Enrique M. De La Cruz, and Demetrios T. Braddock. Enpp1-fc prevents mortality and vascular calcifications in rodent model of generalized arterial calcification of infancy. Nature Communications, Dec 2015. URL: https://doi.org/10.1038/ncomms10006, doi:10.1038/ncomms10006. This article has 175 citations and is from a highest quality peer-reviewed journal.

20. (tanaka2024preterminfantwith pages 8-9): Masato Tanaka, Akira Kobayashi, Haruhiro Kuwabara, Jun Nirei, Junichi Ozawa, Kentaro Sawano, Nao Shibata, Keisuke Nagasaki, and Akihiko Saitoh. Preterm infant with generalized arterial calcification of infancy who survived due to early diagnosis and appropriate treatment with bisphosphonates: a case report. Children, 11:1176, Sep 2024. URL: https://doi.org/10.3390/children11101176, doi:10.3390/children11101176. This article has 5 citations.

21. (NCT07473973 chunk 1):  ENERGY 2: Evaluation of the Efficacy and Safety of INZ-701 in Infants With ENPP1 Deficiency. Inozyme Pharma. 2025. ClinicalTrials.gov Identifier: NCT07473973

22. (NCT06462547 chunk 1):  ADAPT Study: Long-term Safety Study of INZ-701 in Patients With ENPP1 Deficiency and ABCC6 Deficiency. Inozyme Pharma. 2024. ClinicalTrials.gov Identifier: NCT06462547

23. (NCT05734196 chunk 2):  The ENERGY Study: Evaluation of Safety and Tolerability of INZ-701 in Infants With ENPP1 Deficiency or ABCC6 Deficiency. Inozyme Pharma. 2023. ClinicalTrials.gov Identifier: NCT05734196

24. (NCT06046820 chunk 2):  The ENERGY 3 Study: Evaluation of Efficacy and Safety of INZ-701 in Children With ENPP1 Deficiency. Inozyme Pharma. 2023. ClinicalTrials.gov Identifier: NCT06046820