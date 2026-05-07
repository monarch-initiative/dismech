---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T22:02:44.858206'
end_time: '2026-05-06T22:23:38.090035'
duration_seconds: 1253.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rheumatoid Vasculitis
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Rheumatoid Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Rheumatoid Vasculitis** covering all of the
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
- **Disease Name:** Rheumatoid Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Rheumatoid Vasculitis** covering all of the
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


## Comprehensive Research Report: Rheumatoid Vasculitis

### 1. Disease Information

#### 1.1 Overview / definition
Rheumatoid vasculitis (RV) is a rare but severe extra-articular manifestation of rheumatoid arthritis (RA), typically presenting as necrotizing or leukocytoclastic vasculitis involving small-to-medium-sized vessels and associated with high morbidity and mortality. (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2, makol2015rheumatoidvasculitisan pages 3-5)

#### 1.2 Synonyms and alternative names
Common alternative names in the clinical literature include **systemic rheumatoid vasculitis** and **vasculitis associated with rheumatoid arthritis**. (makol2014vasculitisassociatedwith pages 1-1, kishore2017rheumatoidvasculitisa pages 1-2)

#### 1.3 Key identifiers (ontology/coding)
In this tool run, authoritative ontology/coding identifiers (MONDO, Orphanet, ICD-10/ICD-11, MeSH) were **not successfully retrieved from the available sources** and therefore cannot be reliably asserted here. RV is represented in the current report using aggregated disease-level literature rather than a specific disease ontology entry. (makol2014vasculitisassociatedwith pages 1-1, makol2015rheumatoidvasculitisan pages 1-2)

#### 1.4 Evidence source type
Evidence in this report comes primarily from:
- **Human clinical observational cohorts and case-control studies** (e.g., Mayo Clinic series). (makol2014vasculitisassociatedwith pages 1-1, coffey2020rituximabtherapyfor pages 7-9)
- **Human clinical case series** (rituximab-treated cohorts). (coffey2020rituximabtherapyfor pages 2-3, coffey2020rituximabtherapyfor pages 7-9)
- **Narrative/clinical reviews** summarizing clinical and mechanistic understanding. (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2, makol2015rheumatoidvasculitisan pages 3-5)
- **Recent case-based reviews/case reports (2023–2024)** that reflect modern diagnostic challenges (including biopsy-negative presentations). (ahmad2024rheumatoidvasculitisin pages 5-6, ahmad2024rheumatoidvasculitisin media 15865f42)


### 2. Etiology

#### 2.1 Disease causal factors (mechanistic etiology)
RV is generally conceptualized as an immune-mediated vascular inflammatory process arising in the context of RA, with both **immune-complex/complement-mediated injury** and **cell-mediated vascular damage** contributing. (kishore2017rheumatoidvasculitisa pages 1-2, genta2006systemicrheumatoidvasculitis pages 2-3, kishore2017rheumatoidvasculitisa pages 2-4)

#### 2.2 Risk factors
RV is most strongly associated with **long-standing, severe, seropositive RA** (often erosive/nodular disease). (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2, makol2015rheumatoidvasculitisan pages 3-5)

In a Mayo Clinic case-control study (2000–2010), factors associated with RV included:
- **Current smoking at RA diagnosis** (OR 1.98). (makol2014vasculitisassociatedwith pages 1-1)
- **Peripheral vascular disease** (OR 3.98). (makol2014vasculitisassociatedwith pages 1-1)
- **Cerebrovascular disease** (OR 6.48). (makol2014vasculitisassociatedwith pages 1-1)
- **Severe RA** (OR 2.02). (makol2014vasculitisassociatedwith pages 1-1)
- **Use of biologics** (OR 2.80), noting important confounding by indication and the challenge of separating “drug-induced vasculitis” from RA-associated vasculitis. (makol2014vasculitisassociatedwith pages 1-1, makol2015rheumatoidvasculitisan pages 7-8)

Genetic associations described in review literature include enrichment of **KIR2DS2** (with relevant HLA ligands) and associations with shared-epitope HLA-DRB1 genotypes; these are best viewed as *susceptibility associations* rather than deterministic causes. (kishore2017rheumatoidvasculitisa pages 2-4)

#### 2.3 Protective factors
In the Mayo case-control study, **hydroxychloroquine** (OR 0.54) and **low-dose aspirin** (OR 0.42) were associated with decreased odds of RV. These findings are observational and do not prove causality. (makol2014vasculitisassociatedwith pages 1-1)

#### 2.4 Gene–environment interactions
Smoking is consistently implicated as a risk factor; reviews hypothesize that smoking may promote endothelial dysfunction and immune activation pathways (B- and T-cell–mediated damage), although direct gene–environment interaction quantification for RV was not available in retrieved sources. (kishore2017rheumatoidvasculitisa pages 2-4)


### 3. Phenotypes

#### 3.1 Clinical phenotype spectrum (typical manifestations)
RV most commonly affects the **skin** and **peripheral nervous system**.
- Reviews report **skin involvement ~90%** and emphasize a spectrum from nailfold infarcts to deep ulcers and digital ischemia. (kishore2017rheumatoidvasculitisa pages 1-2)
- Peripheral nervous system involvement (e.g., vasculitic neuropathy / mononeuritis multiplex) is a classic severe presentation. (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 3-5)

A real-world rituximab-treated Mayo cohort (17 RV patients, 2000–2017) reported:
- Skin involvement in 47% (ulcers and/or leukocytoclastic vasculitis). (coffey2020rituximabtherapyfor pages 7-9)
- Mononeuritis multiplex in 12%. (coffey2020rituximabtherapyfor pages 7-9)
- Inflammatory ocular disease in 12%. (coffey2020rituximabtherapyfor pages 7-9)
- Multi-organ involvement in 29%. (coffey2020rituximabtherapyfor pages 7-9)

A 2024 case-based review notes that skin and peripheral nervous system involvement are common and also reports approximate frequencies for other systems (cardiovascular, eyes) in the broader RV literature. (ahmad2024rheumatoidvasculitisin media ab2cb492)

#### 3.2 Age of onset and course
RV usually arises after years of RA (reviewed mean ~10–14 years from RA diagnosis), but recent case literature highlights that RV can occasionally present early or even precede overt RA diagnosis. (makol2015rheumatoidvasculitisan pages 3-5, karra2024rheumatoidvasculitisinvolving pages 7-8)

#### 3.3 Suggested HPO terms (examples)
The following HPO concepts map well to commonly described RV manifestations (ontology IDs not retrieved in this run; labels provided):
- Cutaneous ulcer; Digital ischemia; Purpura; Skin vasculitis. (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 3-5)
- Mononeuritis multiplex; Peripheral neuropathy. (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 3-5)
- Scleritis / Episcleritis; Keratitis / Corneal melt. (coffey2020rituximabtherapyfor pages 7-9)
- Fever; Weight loss; Elevated inflammatory markers (ESR/CRP). (makol2015rheumatoidvasculitisan pages 5-7, ahmad2024rheumatoidvasculitisin media 15865f42)


### 4. Genetic / Molecular Information

#### 4.1 Causal genes
RV is not a monogenic disorder in the retrieved literature; it is best understood as a complex, multifactorial complication of RA with genetic susceptibility signals rather than a single causal gene. (kishore2017rheumatoidvasculitisa pages 2-4)

#### 4.2 Genetic susceptibility / associations (examples)
- **KIR2DS2** enrichment (in conjunction with appropriate HLA ligands) and shared-epitope HLA-DRB1 genotypes are described as associated with RV in review literature. (kishore2017rheumatoidvasculitisa pages 2-4)

Variant-level (ClinVar/gnomAD) data were not retrieved for RV in this run.


### 5. Environmental Information

#### 5.1 Environmental and lifestyle factors
**Smoking** is a consistent clinical risk factor supported by case-control evidence and review synthesis. (makol2014vasculitisassociatedwith pages 1-1, kishore2017rheumatoidvasculitisa pages 2-4)

Other environmental triggers (e.g., infections, drug exposures) are discussed in review literature primarily as potential triggers or confounders; distinguishing RA-associated RV from **drug-induced vasculitis** (notably anti-TNF-associated vasculitis) is emphasized as an ongoing clinical challenge. (makol2015rheumatoidvasculitisan pages 7-8, makol2015rheumatoidvasculitisan pages 5-7)


### 6. Mechanism / Pathophysiology

#### 6.1 Current mechanistic understanding (causal chain)
A commonly synthesized pathway is:
1) **Seropositive RA with high autoantibody burden** (RF and often ACPA/anti-CCP), associated with circulating immune complexes. (makol2015rheumatoidvasculitisan pages 3-5, bartels2010rheumatoidvasculitisvanishing pages 4-5)
2) **Immune complex deposition** in vessel walls with **complement activation** and Fc receptor engagement, leading to leukocyte activation and cytokine release. (kishore2017rheumatoidvasculitisa pages 1-2, genta2006systemicrheumatoidvasculitis pages 2-3)
3) **Endothelial activation/injury** (adhesion molecule expression such as ICAM-1 and E-selectin) and recruitment/activation of inflammatory cells. (kishore2017rheumatoidvasculitisa pages 1-2)
4) **Vessel wall necrosis and leukocytoclastic inflammation**, causing ischemia, ulceration, neuropathy, and end-organ injury depending on vascular territory. (makol2015rheumatoidvasculitisan pages 3-5)

#### 6.2 Key molecular mediators and pathways
- Cytokines and inflammatory mediators implicated include **TNF-α**, **IL-1**, and **IL-6** (reviewed as downstream of Fc/complement-triggered activation and contributors to adhesion molecule expression and vascular damage). (genta2006systemicrheumatoidvasculitis pages 2-3, kishore2017rheumatoidvasculitisa pages 1-2)

#### 6.3 Key cell types (suggested CL mappings by label)
- Neutrophils (leukocytoclastic vasculitis pattern). (makol2015rheumatoidvasculitisan pages 3-5)
- CD4+CD28null T cells implicated in vascular injury. (kishore2017rheumatoidvasculitisa pages 1-2, kishore2017rheumatoidvasculitisa pages 2-4)
- B cells / plasmablast-lineage cells as drivers of autoantibody and immune-complex biology (supporting rationale for B-cell depletion). (makol2015rheumatoidvasculitisan pages 3-5, bartels2010rheumatoidvasculitisvanishing pages 4-5)

#### 6.4 Suggested GO biological process terms (by label)
- Complement activation; Immune complex clearance; Leukocyte migration; Endothelial cell activation; Inflammatory response; Blood vessel remodeling. (kishore2017rheumatoidvasculitisa pages 1-2, genta2006systemicrheumatoidvasculitis pages 2-3)

#### 6.5 Molecular profiling (omics)
No RV-specific transcriptomic/proteomic/metabolomic profiling studies were retrieved in this run; this remains a gap relative to RA synovial tissue multi-omics literature.


### 7. Anatomical Structures Affected

#### 7.1 Organ and system involvement
Predominantly affected systems include:
- Skin (cutaneous small-vessel vasculitis, ulcers, digital ischemia). (kishore2017rheumatoidvasculitisa pages 1-2, coffey2020rituximabtherapyfor pages 7-9)
- Peripheral nervous system (vasculitic neuropathy, mononeuritis multiplex). (kishore2017rheumatoidvasculitisa pages 1-2, coffey2020rituximabtherapyfor pages 7-9)
- Eyes (scleritis/episcleritis, ulcerative keratitis). (coffey2020rituximabtherapyfor pages 7-9)

RV can be multi-organ and can involve GI tract, CNS, heart, kidney, and lung in severe disease (reviewed as possible severe organ targets even when absent in specific cohorts). (makol2015rheumatoidvasculitisan pages 3-5, makol2015rheumatoidvasculitisan pages 5-7)

#### 7.2 Suggested UBERON anatomical concepts (by label)
Skin; peripheral nerve; medium-sized artery; small blood vessel; eye; gastrointestinal tract. (makol2015rheumatoidvasculitisan pages 3-5, makol2015rheumatoidvasculitisan pages 5-7, coffey2020rituximabtherapyfor pages 7-9)


### 8. Temporal Development

#### 8.1 Onset
RV is usually **adult-onset** and most often occurs after prolonged RA duration (mean ~10–14 years in review literature), but early presentations have been reported. (makol2015rheumatoidvasculitisan pages 3-5, karra2024rheumatoidvasculitisinvolving pages 7-8)

#### 8.2 Progression and course
RV may be rapidly progressive when systemic/necrotizing arteritis is present, and it has high relapse risk in some cohorts. (makol2014vasculitisassociatedwith pages 1-1, makol2015rheumatoidvasculitisan pages 5-7)


### 9. Inheritance and Population

#### 9.1 Epidemiology
RV incidence has declined markedly over recent decades, likely reflecting improved RA control:
- Norfolk/Norwich trend cited in reviews: 9.1/million (1988–2000/2002) vs 3.9/million (2001–2010). (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2)
- Olmsted County cumulative incidence in RA reported to decline from 3.6% (1985–1994) to 0.6% (1995–2007). (kishore2017rheumatoidvasculitisa pages 1-2)

#### 9.2 Recent data relevant to the “modern era” (2023)
A large multicenter cohort of RA patients (Brazilian public rheumatology centers; data collection beginning 2015) reported **extra-articular manifestations prevalence 23.4%** overall, and reaffirmed that long-standing seropositive disease and disability/inflammatory activity are key correlates of extra-articular disease (the paper is not RV-specific but provides contemporary context that extra-articular disease remains common). (ahmad2024rheumatoidvasculitisin media ab2cb492)


### 10. Diagnostics

#### 10.1 Diagnostic approach (real-world implementation)
RV diagnosis is typically syndromic and clinicopathologic:
- **Biopsy with characteristic histopathology** is emphasized as important/often necessary when feasible; skin biopsy yields up to ~75% in review data. (makol2015rheumatoidvasculitisan pages 3-5)
- When biopsy is not feasible, **angiography** may be considered for suspected mesenteric or extremity ischemia and mimics should be excluded; treatment may be started on strong clinical suspicion. (makol2015rheumatoidvasculitisan pages 5-7)
- A 2024 case-based review stresses that a negative biopsy does not exclude RV and may reflect sampling limitations. (ahmad2024rheumatoidvasculitisin pages 5-6)

**Laboratory evaluation** is supportive rather than definitive:
- Elevated ESR/CRP and cytopenias/inflammation-associated CBC patterns are included in a review algorithm. (makol2015rheumatoidvasculitisan pages 5-7)
- RF and ACPA are commonly present but have modest positive predictive value; absence has good negative predictive value. (makol2015rheumatoidvasculitisan pages 3-5)

A rituximab-treated RV cohort also documents real-world diagnostic workup beyond clinical diagnosis, including biopsy, CT angiography, and EMG in subsets. (coffey2020rituximabtherapyfor pages 7-9)

A representative 2024 case workup table (RF/anti-CCP/ESR/CRP, etc.) is available as extracted Table 1. (ahmad2024rheumatoidvasculitisin media 15865f42)

#### 10.2 Histopathology
Typical features include mononuclear or neutrophilic vessel wall infiltration with necrosis, leukocytoclasis, and disruption of elastic laminae; perivascular infiltrates without vessel-wall involvement do not meet criteria. (makol2015rheumatoidvasculitisan pages 3-5)

#### 10.3 Differential diagnosis
Key mimics include:
- Primary ANCA-associated vasculitis, especially when vasculitic neuropathy, skin lesions, or systemic features are present (ANCA patterns in RV can be atypical and MPO/PR3 often negative). (makol2015rheumatoidvasculitisan pages 3-5, bartels2010rheumatoidvasculitisvanishing pages 4-5)
- Drug-induced vasculitis (notably anti-TNF-associated vasculitis), which may be suggested by temporal relationship, resolution on withdrawal, and recurrence on rechallenge. (makol2015rheumatoidvasculitisan pages 7-8)


### 11. Outcomes / Prognosis

RV remains associated with substantial mortality:
- Mayo RA-vasculitis case-control cohort (86 RV cases, 2000–2010): 26% died by 5 years and 36% relapsed by 5 years. (makol2014vasculitisassociatedwith pages 1-1)
- Reviews cite registry-era mortality rates as high as **12% at 1 year and 60% at 5 years** in one cohort, with infection and active vasculitis/organ damage important causes of death. (makol2015rheumatoidvasculitisan pages 5-7)


### 12. Treatment

Treatment intensity is typically stratified by extent and organ-threatening involvement.

#### 12.1 Real-world treatment algorithm (review-based)
A pragmatic approach includes:
- Mild–moderate RV: oral glucocorticoids plus methotrexate or azathioprine. (makol2015rheumatoidvasculitisan pages 5-7)
- Severe RV: higher-dose glucocorticoids (± IV pulse) plus cyclophosphamide or rituximab; biologics (including anti-TNF) are discussed, with careful attention to possible drug-induced vasculitis. (makol2015rheumatoidvasculitisan pages 5-7)
- Refractory disease: switching biologic class (rituximab, anti-TNF, tocilizumab, abatacept, anakinra) and/or adjunctive plasmapheresis/IVIG may be considered. (makol2015rheumatoidvasculitisan pages 5-7)

#### 12.2 Rituximab outcomes (real-world evidence)
In a rituximab-treated systemic RV cohort (17 patients, Mayo Clinic, 2000–2017):
- RV presentations included skin (47%), mononeuritis multiplex (12%), ocular disease (12%), and multi-organ disease (29%); rituximab dose commonly 1 g two weeks apart. (coffey2020rituximabtherapyfor pages 7-9)
- Outcomes in the abstract: complete remission and partial responses accumulated over 3–12 months (e.g., 40% complete remission at 6 months, 62% complete remission at 12 months). (coffey2020rituximabtherapyfor pages 2-3)

#### 12.3 Suggested MAXO terms
See treatment artifact for suggested MAXO mappings by modality (systemic corticosteroid therapy, cyclophosphamide therapy, rituximab therapy, TNF inhibitor therapy, IVIG therapy, plasmapheresis, etc.). (makol2015rheumatoidvasculitisan pages 5-7, coffey2020rituximabtherapyfor pages 7-9)


### 13. Prevention
No RV-specific primary prevention interventions were identified in the retrieved sources. Given smoking’s association with RV risk, smoking cessation is biologically plausible as risk modification in RA, but RV-specific interventional prevention studies were not retrieved. (makol2014vasculitisassociatedwith pages 1-1, kishore2017rheumatoidvasculitisa pages 2-4)


### 14. Other Species / Natural Disease
No naturally occurring veterinary analogs or cross-species transmission issues were identified in the retrieved RV-focused sources.


### 15. Model Organisms
No RV-specific model organism systems were retrieved in this run; mechanistic discussion in reviews is largely based on human clinicopathologic observations and extrapolation from immune complex biology and vascular inflammation paradigms. (kishore2017rheumatoidvasculitisa pages 1-2, genta2006systemicrheumatoidvasculitis pages 2-3)


## Recent Developments (2023–2024 emphasis)

1) **Extra-articular RA remains common in contemporary cohorts**: A 2023 multicenter RA cohort found extra-articular manifestations in 23.4% of RA patients and associated extra-articular disease with longer disease duration, high RF titers, higher disease activity, and greater disability, reinforcing that severe systemic RA phenotypes persist despite modern RA therapeutics. (ahmad2024rheumatoidvasculitisin media ab2cb492)

2) **Diagnostic challenges persist in the modern era**: 2024 case-based literature emphasizes that negative biopsy does not exclude RV, highlighting sampling limitations and the need for multimodal assessment (clinical syndrome + targeted investigations). (ahmad2024rheumatoidvasculitisin pages 5-6)

3) **Contemporary practice continues to rely on extrapolation and observational evidence**: RV remains too rare for robust RV-specific randomized trials; modern practice increasingly uses biologics (notably rituximab) alongside glucocorticoids, with response data primarily from case series and single-center cohorts. (makol2015rheumatoidvasculitisan pages 5-7, coffey2020rituximabtherapyfor pages 7-9)


## Key Data and Statistics (selected)
- Declining incidence: 9.1/million (1988–2000/2002) vs 3.9/million (2001–2010). (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2)
- Mortality (Mayo 2000–2010 case-control cohort): 26% at 5 years; relapse 36% at 5 years. (makol2014vasculitisassociatedwith pages 1-1)
- Risk factor effect sizes (Mayo case-control): smoking at RA diagnosis OR 1.98; PVD OR 3.98; cerebrovascular disease OR 6.48. (makol2014vasculitisassociatedwith pages 1-1)
- Rituximab-treated cohort phenotype: skin 47%, mononeuritis multiplex 12%, ocular disease 12%, multi-organ 29%. (coffey2020rituximabtherapyfor pages 7-9)


## Embedded Evidence Artifacts

| Domain | Summary | Evidence/Citations |
|---|---|---|
| Definition | Rheumatoid vasculitis (RV) is a rare but severe extra-articular manifestation of rheumatoid arthritis, characterized by necrotizing or leukocytoclastic vasculitis affecting predominantly small-to-medium vessels and associated with high morbidity and mortality. | (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2, makol2015rheumatoidvasculitisan pages 3-5) |
| Synonyms / alternative names | Rheumatoid vasculitis; systemic rheumatoid vasculitis; vasculitis associated with rheumatoid arthritis. | (makol2014vasculitisassociatedwith pages 1-1, kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2) |
| Key identifiers / coding placeholders | ICD-10: not identified in retrieved context; ICD-11: not identified in retrieved context; MeSH: specific RV MeSH term not confirmed in retrieved context; MONDO: not identified in retrieved context; Orphanet: not identified in retrieved context. Retrieved evidence is disease-level literature/reviews and case series rather than ontology registry records. | (makol2014vasculitisassociatedwith pages 1-1, kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2) |
| Epidemiology: incidence/prevalence trends | Incidence has declined markedly in the modern treatment era. Reported Norfolk/Norwich trend: 9.1/million in 1988–2000/2002 vs 3.9/million in 2001–2010. Olmsted County 10-year cumulative incidence in RA reportedly fell from 3.6% (1985–1994) to 0.6% (1995–2007). Reviews consistently describe RV as “diminishing” or “vanishing,” likely related to better RA control and biologic-era management. | (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2) |
| Prognosis / mortality | Prognosis remains poor despite lower incidence. In the Mayo 2000–2010 case-control cohort, 26% died by 5 years and 36% relapsed by 5 years. A registry/cohort cited in reviews reported 12% mortality at 1 year and 60% at 5 years. Historical reviews note up to 40% mortality within 5 years. | (makol2014vasculitisassociatedwith pages 1-1, makol2015rheumatoidvasculitisan pages 7-8, makol2015rheumatoidvasculitisan pages 5-7) |
| Major risk factors | Long-standing, severe, seropositive, nodular/erosive RA; male sex; older age; smoking; extra-articular RA burden; vascular comorbidity. Effect sizes from Mayo case-control study: current smoking at RA diagnosis OR 1.98; peripheral vascular disease OR 3.98; cerebrovascular disease OR 6.48; severe RA OR 2.02; biologic use OR 2.80. High RF/ACPA titers are repeatedly associated with RV. | (makol2014vasculitisassociatedwith pages 1-1, kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2, makol2015rheumatoidvasculitisan pages 3-5) |
| Protective factors | Hydroxychloroquine and low-dose aspirin were associated with lower odds of RV in one case-control study: hydroxychloroquine OR 0.54; low-dose aspirin OR 0.42. | (makol2014vasculitisassociatedwith pages 1-1, kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2) |
| Common organ manifestations | Skin and peripheral nerves are the dominant targets. Approximate frequencies from review/case-based literature: skin ~90% of cases; peripheral nervous system ~40%; cardiovascular system ~30%; eye involvement ~15%. In the rituximab cohort: skin 47%, mononeuritis multiplex 12%, inflammatory ocular disease 12%, multi-organ involvement 29%; no renal or pulmonary vasculitis in that series. | (kishore2017rheumatoidvasculitisa pages 1-2, ahmad2024rheumatoidvasculitisin media ab2cb492, coffey2020rituximabtherapyfor pages 7-9) |
| Examples of cutaneous/neurologic phenotypes | Nail-fold infarcts, palpable purpura, deep/non-healing leg ulcers, pyoderma gangrenosum-like lesions, digital ischemia/gangrene; vasculitic neuropathy/mononeuritis multiplex are emphasized as classic presentations. | (kishore2017rheumatoidvasculitisa pages 1-2, makol2015rheumatoidvasculitisan pages 1-2, makol2015rheumatoidvasculitisan pages 3-5) |
| Diagnostic hallmarks (compact) | Diagnosis is primarily clinical-pathologic: biopsy showing necrotizing/leukocytoclastic vasculitis when feasible; skin biopsy yield up to ~75% in review data. Supportive labs include high RF/ACPA, elevated ESR/CRP, low complement; angiography may help in medium-vessel or ischemic disease; negative biopsy does not exclude RV if suspicion remains high. | (makol2015rheumatoidvasculitisan pages 3-5, makol2015rheumatoidvasculitisan pages 5-7, ahmad2024rheumatoidvasculitisin pages 5-6, ahmad2024rheumatoidvasculitisin media 15865f42) |


*Table: This table condenses the most actionable disease-characteristics evidence for rheumatoid vasculitis from the retrieved context, including definition, coding gaps, epidemiology, prognosis, risk/protective factors, and organ manifestations.*

| Disease severity / scenario | Treatment option | Regimen components / typical dosing stated in sources | Key outcome data / use case | Suggested MAXO term(s) | Evidence |
|---|---|---|---|---|---|
| Mild–moderate RV (limited cutaneous disease, pericarditis, 0–1 extra-articular manifestations) | Glucocorticoids + methotrexate | Oral glucocorticoids 20–40 mg/day prednisone equivalent + methotrexate 10–25 mg/week (first-line oral DMARD) | Recommended empiric induction approach for limited disease; used because patients with primarily limited cutaneous disease may respond to lesser immunosuppression | MAXO: systemic corticosteroid therapy; methotrexate therapy; immunosuppressive therapy | (makol2015rheumatoidvasculitisan pages 5-7) |
| Mild–moderate RV when methotrexate unsuitable | Glucocorticoids + azathioprine | Oral glucocorticoids 20–40 mg/day prednisone equivalent + azathioprine 2 mg/kg/day (alternative oral DMARD) | Alternative induction regimen for limited disease in review-based treatment algorithm | MAXO: systemic corticosteroid therapy; azathioprine therapy; immunosuppressive therapy | (makol2015rheumatoidvasculitisan pages 5-7) |
| Severe/systemic RV (multi-organ disease, necrotizing arteritis, major end-organ involvement) | High-dose glucocorticoids + cyclophosphamide | Oral glucocorticoids 40–60 mg/day prednisone equivalent and/or IV pulse glucocorticoids 0.5–1 g/day for 3 days + cyclophosphamide (daily oral or monthly IV) for ~3–6 months in algorithm text | Historical standard for severe RV; still used for life-threatening disease, but toxicity remains substantial and mortality in older cohorts remained high | MAXO: intravenous methylprednisolone therapy; cyclophosphamide therapy; remission induction therapy | (makol2015rheumatoidvasculitisan pages 5-7, bartels2010rheumatoidvasculitisvanishing pages 4-5) |
| Severe/systemic RV | Rituximab-based induction | Rituximab 1 g IV 2 weeks apart in review algorithm; in Mayo series, 1 g 2 weeks apart in 13/15 treated with standard schedule, with 2 receiving 375 mg/m2 weekly ×4; often combined with glucocorticoids, sometimes DMARDs | Mayo 17-patient cohort: CR 13% and PR 67% at 3 months; CR 40% and PR 53% at 6 months; CR 62% and PR 38% at 12 months. French registry cited in review: 12/17 complete remissions at 6 months; 14/17 in remission at 12 months; severe infection rate 6.4/100 patient-years. | MAXO: rituximab therapy; B-cell depletion therapy; remission induction therapy | (coffey2020rituximabtherapyfor pages 2-3, makol2015rheumatoidvasculitisan pages 3-5, makol2015rheumatoidvasculitisan pages 5-7, coffey2020rituximabtherapyfor pages 7-9) |
| Maintenance after rituximab response / relapse prevention | Rituximab maintenance or conventional DMARD maintenance | Review algorithm suggests MTX/AZA/LEF/rituximab maintenance; in cited rituximab registry, some patients received additional rituximab between months 6 and 12 | In review-cited registry, no relapse among 6 patients who received maintenance rituximab between months 6 and 12, versus 3 relapses among 9 without it; remission reestablished after reintroduction in 2 cases | MAXO: maintenance immunotherapy; rituximab therapy; methotrexate therapy; azathioprine therapy; leflunomide therapy | (makol2015rheumatoidvasculitisan pages 5-7) |
| Severe or refractory RV | Anti-TNF therapy | Review algorithm lists anti-TNF agent as an option for severe RV; specific dosing not standardized in retrieved RV sources | Case reports/series describe successful use in refractory RV, but role is controversial because >200 cases of anti-TNF–associated vasculitis have also been reported; if drug-induced vasculitis suspected, stop and switch biologic | MAXO: TNF inhibitor therapy; biologic immunomodulator therapy | (makol2015rheumatoidvasculitisan pages 5-7, makol2015rheumatoidvasculitisan pages 7-8) |
| Refractory / relapsing RV | Tocilizumab | Listed in review as alternate biologic for refractory disease; dosing not specified in retrieved RV sources | Supported mainly by case reports/limited experience; reserved for refractory disease after standard agents | MAXO: tocilizumab therapy; interleukin-6 inhibitor therapy | (makol2015rheumatoidvasculitisan pages 7-8, makol2015rheumatoidvasculitisan pages 5-7) |
| Refractory / relapsing RV | Abatacept | Listed in review as alternate biologic for refractory disease; dosing not specified in retrieved RV sources | Supported mainly by case reports/limited experience; reserved for refractory disease after standard agents | MAXO: abatacept therapy; T-cell costimulation modulator therapy | (makol2015rheumatoidvasculitisan pages 7-8, makol2015rheumatoidvasculitisan pages 5-7) |
| Refractory / relapsing RV | Anakinra | Listed in review algorithm as possible alternate biologic; dosing not specified in retrieved RV sources | Very limited evidence/case-report level in RV | MAXO: anakinra therapy; interleukin-1 inhibitor therapy | (makol2015rheumatoidvasculitisan pages 5-7) |
| Refractory, relapsing, or life-threatening RV adjunctive therapy | IVIG and/or plasmapheresis | Review algorithm recommends addition of plasmapheresis or IVIG in refractory cases; dosing not specified in retrieved RV sources | Adjunctive/salvage role rather than standard first-line treatment | MAXO: intravenous immunoglobulin therapy; plasmapheresis | (makol2015rheumatoidvasculitisan pages 5-7) |
| Contemporary real-world treatment mix (Mayo 2000–2010 RV cohort) | Observed multimodal practice | 99% received glucocorticoids; 29% cyclophosphamide; 55% another DMARD (methotrexate, azathioprine, mycophenolate mofetil, hydroxychloroquine, minocycline); 28% biologic agent (anti-TNF, rituximab, abatacept, anakinra) | Demonstrates real-world heterogeneity and lack of controlled RV-specific trials; therapy individualized by organ involvement and severity | MAXO: immunosuppressive therapy; biologic therapy; glucocorticoid therapy | (makol2015rheumatoidvasculitisan pages 5-7) |


*Table: This table summarizes rheumatoid vasculitis treatments by disease severity, including dosing details reported in the retrieved sources, outcome data where available, and suggested MAXO mappings. It is useful for converting narrative review evidence into a structured treatment knowledge-base artifact.*


## URLs and publication dates (from retrieved sources)
- Makol A, Matteson EL, Warrington KJ. *Rheumatoid vasculitis: an update*. Current Opinion in Rheumatology. **Jan 2015**. https://doi.org/10.1097/BOR.0000000000000126 (makol2015rheumatoidvasculitisan pages 3-5, makol2015rheumatoidvasculitisan pages 5-7)
- Kishore S, Maher L, Majithia V. *Rheumatoid vasculitis: a diminishing yet devastating menace*. Current Rheumatology Reports. **Jun 2017**. https://doi.org/10.1007/s11926-017-0667-3 (kishore2017rheumatoidvasculitisa pages 1-2, kishore2017rheumatoidvasculitisa pages 2-4)
- Coffey CM et al. *Rituximab Therapy for Systemic Rheumatoid Vasculitis: Indications, Outcomes, and Adverse Events*. The Journal of Rheumatology. **Apr 2020**. https://doi.org/10.3899/jrheum.181397 (coffey2020rituximabtherapyfor pages 2-3, coffey2020rituximabtherapyfor pages 7-9)
- Bonfiglioli KR et al. *Extra-articular manifestations of rheumatoid arthritis remain a major challenge: data from a large, multi-centric cohort*. Advances in Rheumatology. **Jul 2023**. https://doi.org/10.1186/s42358-023-00318-y (ahmad2024rheumatoidvasculitisin media ab2cb492)
- Ahmad A et al. *Rheumatoid Vasculitis in Modern Era: A Case Report and Comprehensive Literature Review*. Cureus. **Jun 2024**. https://doi.org/10.7759/cureus.62783 (ahmad2024rheumatoidvasculitisin pages 5-6, ahmad2024rheumatoidvasculitisin media 15865f42)


## Limitations and gaps
- RV-specific **2023–2024 comprehensive reviews** (e.g., Autoimmunity Reviews 2023 “Rheumatoid vasculitis in 2023: changes and challenges since the biologics era”) were identified by search but **unobtainable** in this run, limiting the ability to cite the most recent narrative syntheses.
- Ontology identifiers (MONDO/Orphanet/MeSH/ICD) were not recovered from the available documents; these should be sourced directly from MONDO/Orphanet/NCBI MeSH/WHO ICD browser in a follow-on curation pass.
- No RV-specific multi-omics profiling studies were retrieved.


References

1. (kishore2017rheumatoidvasculitisa pages 1-2): Shweta Kishore, Lisa Maher, and Vikas Majithia. Rheumatoid vasculitis: a diminishing yet devastating menace. Current Rheumatology Reports, 19:1-7, Jun 2017. URL: https://doi.org/10.1007/s11926-017-0667-3, doi:10.1007/s11926-017-0667-3. This article has 85 citations and is from a peer-reviewed journal.

2. (makol2015rheumatoidvasculitisan pages 1-2): Ashima Makol, Eric L. Matteson, and Kenneth J. Warrington. Rheumatoid vasculitis: an update. Current Opinion in Rheumatology, 27:63–70, Jan 2015. URL: https://doi.org/10.1097/bor.0000000000000126, doi:10.1097/bor.0000000000000126. This article has 158 citations and is from a peer-reviewed journal.

3. (makol2015rheumatoidvasculitisan pages 3-5): Ashima Makol, Eric L. Matteson, and Kenneth J. Warrington. Rheumatoid vasculitis: an update. Current Opinion in Rheumatology, 27:63–70, Jan 2015. URL: https://doi.org/10.1097/bor.0000000000000126, doi:10.1097/bor.0000000000000126. This article has 158 citations and is from a peer-reviewed journal.

4. (makol2014vasculitisassociatedwith pages 1-1): A. Makol, C. S. Crowson, D. A. Wetter, O. Sokumbi, E. L. Matteson, and K. J. Warrington. Vasculitis associated with rheumatoid arthritis: a case-control study. Rheumatology, 53:890-899, Jan 2014. URL: https://doi.org/10.1093/rheumatology/ket475, doi:10.1093/rheumatology/ket475. This article has 155 citations and is from a peer-reviewed journal.

5. (coffey2020rituximabtherapyfor pages 7-9): Caitrin M. Coffey, Michael D. Richter, Cynthia S. Crowson, Matthew J. Koster, Kenneth J. Warrington, Steven R. Ytterberg, and Ashima Makol. Rituximab therapy for systemic rheumatoid vasculitis: indications, outcomes, and adverse events. The Journal of Rheumatology, 47:518-523, Apr 2020. URL: https://doi.org/10.3899/jrheum.181397, doi:10.3899/jrheum.181397. This article has 30 citations.

6. (coffey2020rituximabtherapyfor pages 2-3): Caitrin M. Coffey, Michael D. Richter, Cynthia S. Crowson, Matthew J. Koster, Kenneth J. Warrington, Steven R. Ytterberg, and Ashima Makol. Rituximab therapy for systemic rheumatoid vasculitis: indications, outcomes, and adverse events. The Journal of Rheumatology, 47:518-523, Apr 2020. URL: https://doi.org/10.3899/jrheum.181397, doi:10.3899/jrheum.181397. This article has 30 citations.

7. (ahmad2024rheumatoidvasculitisin pages 5-6): Anam Ahmad, Farina Tariq, and Muhammad Zaheer. Rheumatoid vasculitis in modern era: a case report and comprehensive literature review. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62783, doi:10.7759/cureus.62783. This article has 1 citations.

8. (ahmad2024rheumatoidvasculitisin media 15865f42): Anam Ahmad, Farina Tariq, and Muhammad Zaheer. Rheumatoid vasculitis in modern era: a case report and comprehensive literature review. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62783, doi:10.7759/cureus.62783. This article has 1 citations.

9. (genta2006systemicrheumatoidvasculitis pages 2-3): Marcia S. Genta, Robert M. Genta, and Cem Gabay. Systemic rheumatoid vasculitis: a review. Seminars in arthritis and rheumatism, 36 2:88-98, Oct 2006. URL: https://doi.org/10.1016/j.semarthrit.2006.04.006, doi:10.1016/j.semarthrit.2006.04.006. This article has 262 citations and is from a peer-reviewed journal.

10. (kishore2017rheumatoidvasculitisa pages 2-4): Shweta Kishore, Lisa Maher, and Vikas Majithia. Rheumatoid vasculitis: a diminishing yet devastating menace. Current Rheumatology Reports, 19:1-7, Jun 2017. URL: https://doi.org/10.1007/s11926-017-0667-3, doi:10.1007/s11926-017-0667-3. This article has 85 citations and is from a peer-reviewed journal.

11. (makol2015rheumatoidvasculitisan pages 7-8): Ashima Makol, Eric L. Matteson, and Kenneth J. Warrington. Rheumatoid vasculitis: an update. Current Opinion in Rheumatology, 27:63–70, Jan 2015. URL: https://doi.org/10.1097/bor.0000000000000126, doi:10.1097/bor.0000000000000126. This article has 158 citations and is from a peer-reviewed journal.

12. (ahmad2024rheumatoidvasculitisin media ab2cb492): Anam Ahmad, Farina Tariq, and Muhammad Zaheer. Rheumatoid vasculitis in modern era: a case report and comprehensive literature review. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62783, doi:10.7759/cureus.62783. This article has 1 citations.

13. (karra2024rheumatoidvasculitisinvolving pages 7-8): Nanditha Karra, Sumith Mustyala, Sritej Reddy Meghi, FNU Safa, Siri Sanmayi Medicherla, Ajay Goud Nattala, Jai Hind Reddy Nalla, and Rajendraprasad Saligommula. Rheumatoid vasculitis involving gastrointestinal tract pre-dating rheumatoid arthritis: a case study and literature review. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.67346, doi:10.7759/cureus.67346. This article has 2 citations.

14. (makol2015rheumatoidvasculitisan pages 5-7): Ashima Makol, Eric L. Matteson, and Kenneth J. Warrington. Rheumatoid vasculitis: an update. Current Opinion in Rheumatology, 27:63–70, Jan 2015. URL: https://doi.org/10.1097/bor.0000000000000126, doi:10.1097/bor.0000000000000126. This article has 158 citations and is from a peer-reviewed journal.

15. (bartels2010rheumatoidvasculitisvanishing pages 4-5): Christie M. Bartels and Alan J. Bridges. Rheumatoid vasculitis: vanishing menace or target for new treatments? Current Rheumatology Reports, 12:414-419, Sep 2010. URL: https://doi.org/10.1007/s11926-010-0130-1, doi:10.1007/s11926-010-0130-1. This article has 107 citations and is from a peer-reviewed journal.