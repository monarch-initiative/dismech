---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T08:57:53.202662'
end_time: '2026-05-07T09:20:03.345763'
duration_seconds: 1330.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Adrenal Hyperplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Adrenal Hyperplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Adrenal Hyperplasia** covering all of the
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
- **Disease Name:** Congenital Adrenal Hyperplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Adrenal Hyperplasia** covering all of the
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


# Congenital Adrenal Hyperplasia (CAH) — Disease Characteristics Research Report (Mendelian)

## Target disease and scope
Congenital adrenal hyperplasia (CAH) is a group of inherited disorders of adrenal steroidogenesis; **~95–99%** of CAH is due to **21-hydroxylase deficiency (21-OHD)** caused by pathogenic variants in **CYP21A2**, leading to **cortisol deficiency** with variable **aldosterone deficiency** and **androgen excess**. (concolino2025geneticsincongenital pages 1-2, gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6)

This report emphasizes 21-OHD CAH (classic salt-wasting/simple virilizing and nonclassic) while also summarizing rarer enzymatic etiologies.

---

## 1. Disease information
### 1.1 Concise overview
CAH (21-OHD) results from reduced 21-hydroxylase activity in the adrenal cortex. The defect decreases cortisol synthesis; reduced cortisol negative feedback increases ACTH drive, promoting adrenal hyperplasia and shunting steroid precursors into androgen pathways, causing prenatal virilization in some 46,XX fetuses and postnatal hyperandrogenism in both sexes. (concolino2025geneticsincongenital pages 1-2, uslar2023clinicalupdateon pages 3-6)

### 1.2 Key identifiers (available in retrieved evidence)
- **MONDO:** **MONDO_0018479** (“congenital adrenal hyperplasia”) via Open Targets disease record. (OpenTargets Search: Congenital adrenal hyperplasia)
- **ICD-10-CM:** **E25.0** used for administrative/claims identification of CAH in US datasets and Swedish national registers. (harasymiw2020attentiondeficithyperactivitydisorderamong pages 3-3, falhammar2019increasedriskof pages 2-3)

**Not found in retrieved full texts for this run (thus not evidence-backed here):** OMIM disease entry numbers, Orphanet ORPHA codes, MeSH headings, ICD-11 codes.

### 1.3 Common synonyms / alternative names
- “Adrenogenital syndrome” appears as a closely related disease term in Open Targets and in ICD coding contexts. (OpenTargets Search: Congenital adrenal hyperplasia, harasymiw2020attentiondeficithyperactivitydisorderamong pages 3-3)

### 1.4 Evidence provenance type
This report integrates:
- **Aggregated disease-level resources** (Open Targets MONDO mapping; reviews). (OpenTargets Search: Congenital adrenal hyperplasia, uslar2023clinicalupdateon pages 3-6, concolino2025geneticsincongenital pages 1-2)
- **Human clinical studies/registries/claims** (NEJM phase 3 trial; national cohort; multicenter surveys; newborn screening cohort). (auchus2024phase3trial pages 1-3, falhammar2019increasedriskof pages 1-2, righi2023longtermcardiometabolicmorbidity pages 1-2, verma2020newbornscreeningfor pages 1-2)
- **Model organism studies/reviews** (zebrafish, mouse; gene-therapy model reviews). (eachus2017geneticdisruptionof pages 1-2, thirumalasetty2024ahumanizedand pages 1-2, glazova2023modelsofcongenital pages 2-4)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause (genetic):** autosomal recessive pathogenic variation in steroidogenic enzymes, most commonly **CYP21A2** (21-hydroxylase). (concolino2025geneticsincongenital pages 1-2, gunes2025clinicalbiochemicaland pages 1-2)

**Genetic architecture of CYP21A2 locus:** The 2023 multidisciplinary review summarizes that CYP21A2 sits in the HLA region and that pathogenic variants frequently arise from recombination with the pseudogene (**microconversions ~75%**, unequal crossing-over **20–25%**, de novo **1–2%**), with >200 known variants but ~10 accounting for ~90% of cases. (uslar2023clinicalupdateon pages 6-7)

**Rare CAH etiologies:** include 11β-hydroxylase deficiency (CYP11B1), 3β-HSD deficiency (HSD3B2), 17-hydroxylase deficiency (CYP17A1), and lipoid CAH (STAR). (OpenTargets Search: Congenital adrenal hyperplasia)

### 2.2 Risk factors
- **Inheritance pattern:** CAH due to 21-OHD is **autosomal recessive**. (concolino2025geneticsincongenital pages 1-2, gunes2025clinicalbiochemicaland pages 1-2)
- **Carrier frequency (severe alleles):** one multidisciplinary program review reports **~1 in 60 (2%)** prevalence of severe allelic variants in the population. (uslar2023clinicalupdateon pages 9-10)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
The retrieved evidence emphasizes genetic causation and treatment-related complications rather than clear gene–environment interaction effects.

---

## 3. Phenotypes (clinical spectrum)
### 3.1 Current clinical classification
A widely used clinical framework divides 21-OHD into:
- **Classic salt-wasting (SW)**: typically **65–75% of classic cases**, residual activity **<1%**, neonatal adrenal insufficiency/salt-wasting crisis and 46,XX virilization. (uslar2023clinicalupdateon pages 3-6)
- **Classic simple virilizing (SV)**: **25–35% of classic**, residual activity ~**1–2%**, hyperandrogenism with less/minimal mineralocorticoid deficiency. (uslar2023clinicalupdateon pages 3-6)
- **Nonclassic (NCCAH)**: residual activity ~**20–50%**, later-onset hyperandrogenism (acne, hirsutism, oligomenorrhea/infertility), commonly considered in PCOS differential diagnosis. (uslar2023clinicalupdateon pages 3-6)

A 2025 pediatric endocrine review also emphasizes that phenotype likely represents a **continuum** rather than discrete bins. (gunes2025clinicalbiochemicaland pages 1-2)

### 3.2 Phenotype list with ontology suggestions
Key phenotype annotations (including quantitative frequencies where available) are summarized in the table artifact below.

| Phenotype (plain) | Phenotype type | Typical onset | Frequency / notes | Suggested HPO term(s) | Supporting citations |
|---|---|---|---|---|---|
| Salt-wasting crisis with hyponatremia, hyperkalemia, hypovolemia/shock | Symptom/sign/laboratory abnormality | Neonatal / early infancy | Classic salt-wasting CAH accounts for **65–75% of classic cases**; residual 21-hydroxylase activity typically **<1%**; neonatal crises may be life-threatening if unrecognized | **Salt-wasting** HP:0002013; **Hyponatremia** HP:0002902; **Hyperkalemia** HP:0002153; **Shock** HP:0001278 | (uslar2023clinicalupdateon pages 3-6, gunes2025clinicalbiochemicaland pages 1-2, concolino2025geneticsincongenital pages 1-2) |
| Virilized / ambiguous external genitalia in 46,XX infants | Physical manifestation / sign | Prenatal, recognized at birth | Typical of classic CAH; females may show varying degrees of virilization (Prader 1–5) from fetal androgen excess | **Ambiguous genitalia** HP:0000062; **Clitoromegaly** HP:0000058; **Abnormality of the labia** HP:0000060 | (uslar2023clinicalupdateon pages 3-6, abalı2025antenataldiagnosisand pages 1-2, concolino2025geneticsincongenital pages 1-2) |
| Precocious pubarche / premature pubic hair | Sign | Early childhood | Characteristic of simple virilizing classic CAH and can occur in NCCAH due to androgen excess | **Precocious pubarche** HP:0000878 | (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6) |
| Accelerated linear growth | Sign | Childhood | Seen in classic CAH, especially simple virilizing disease; reflects chronic androgen excess | **Accelerated growth** HP:0001510 | (gunes2025clinicalbiochemicaland pages 1-2) |
| Advanced bone age | Laboratory / imaging-associated abnormality | Childhood | Common in simple virilizing CAH and progressive androgen excess states | **Advanced skeletal maturation** HP:0002750 | (gunes2025clinicalbiochemicaland pages 1-2) |
| Acne | Symptom / sign | Adolescence to adulthood; can occur earlier in NCCAH | Common hyperandrogenic presentation in nonclassic CAH | **Acne** HP:0001074 | (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6) |
| Hirsutism | Sign | Adolescence to adulthood | Common in nonclassic CAH; part of late-onset hyperandrogenism spectrum | **Hirsutism** HP:0001007 | (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 9-10) |
| Menstrual irregularity / oligomenorrhea / amenorrhea | Symptom / sign | Adolescence to adulthood | Common in nonclassic CAH women; important differential with PCOS | **Irregular menstruation** HP:0000858; **Oligomenorrhea** HP:0000879; **Amenorrhea** HP:0000141 | (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6) |
| Infertility / reduced fertility | Clinical outcome / symptom | Adolescence to adulthood | In untreated classic CAH, **up to 90%** of women may experience infertility; NCCAH infertility and miscarriage risk can improve with hydrocortisone, with conception rates reported close to **90%** under treatment in cited review | **Infertility** HP:0000789; **Female infertility** HP:0008209 | (uslar2023clinicalupdateon pages 9-10) |
| Testicular adrenal rest tumors (TARTs) | Physical manifestation / imaging finding | Childhood through adulthood | Prevalence reported as **~20% in children** and **50–80% in adults**; surveillance with testicular ultrasound from age 8 years every 2 years was recommended in one review | **Testicular adrenal rest tumor** HP:0034827; **Abnormal testicular morphology** HP:0000119 | (uslar2023clinicalupdateon pages 9-10) |
| Obesity / increased adiposity | Comorbidity / sign | Childhood through adulthood | Common long-term comorbidity; in one adult cohort obesity screening occurred in **97%** of centers; prevalence varied by country, e.g. **41%** in UK cohort, and all obese patients in one surveyed cohort had salt-wasting CAH | **Obesity** HP:0001513; **Increased body mass index** HP:0001956 | (righi2023longtermcardiometabolicmorbidity pages 4-5, righi2023longtermcardiometabolicmorbidity pages 2-3, righi2023longtermcardiometabolicmorbidity pages 1-2, zaric2025metabolicsyndromespectrum pages 1-2) |
| Hypertension / elevated systolic blood pressure | Comorbidity / sign | Childhood through adulthood | In adult cohort, **10/244** were treated for hypertension; pediatric review reported **58%** systolic hypertension and **24%** diastolic hypertension in one CCAH study, with loss of nocturnal dipping particularly in salt-wasting patients | **Hypertension** HP:0000822 | (righi2023longtermcardiometabolicmorbidity pages 1-2, zaric2025metabolicsyndromespectrum pages 12-14) |
| Osteoporosis / osteopenia | Comorbidity / sign | Adulthood (can emerge earlier with chronic treatment exposure) | Most common treated comorbidity in one adult survey: **43/73 (59%)** of treated comorbidity cases received therapy for osteoporosis/osteopenia; bone screening performed by **81%** of centers, mainly DXA | **Osteoporosis** HP:0000939; **Osteopenia** HP:0000938 | (righi2023longtermcardiometabolicmorbidity pages 4-5, righi2023longtermcardiometabolicmorbidity pages 2-3, righi2023longtermcardiometabolicmorbidity pages 1-2) |
| Type 2 diabetes / insulin resistance / abnormal glucose homeostasis | Comorbidity / laboratory abnormality | Childhood to adulthood | Adult cohort: **16/73 (22%)** of treated comorbidity cases had type 2 diabetes/hyperinsulinaemia; pediatric review found insulin resistance frequently increased in classic CAH | **Insulin resistance** HP:0000855; **Hyperinsulinemia** HP:0003074; **Type II diabetes mellitus** HP:0005978 | (righi2023longtermcardiometabolicmorbidity pages 1-2, zaric2025metabolicsyndromespectrum pages 1-2, zaric2025metabolicsyndromespectrum pages 12-14) |
| Autoimmune disorders increased risk | Comorbidity | Usually later childhood to adulthood | Swedish national cohort: autoimmune disorders in **7.4%** of 21OHD patients vs **5.1%** of controls; RR **1.47** (95% CI 1.13–1.91), with increased autoimmune endocrine and thyroid disease | **Autoimmunity** HP:0002960; **Autoimmune thyroiditis** HP:0002726 | (falhammar2019increasedriskof pages 1-2) |


*Table: This table summarizes major clinical phenotypes and comorbidities across classic salt-wasting, simple virilizing, and nonclassic 21-hydroxylase deficiency CAH. It includes suggested HPO mappings and recent quantitative frequencies where available to support knowledge-base phenotype annotation.*

Quality-of-life burdens are repeatedly linked to chronic androgen excess, adrenal crises, growth concerns, reproductive challenges, and long-term metabolic/bone outcomes, with the management goal framed as optimizing long-term health and daily functioning while avoiding glucocorticoid overtreatment. (uslar2023clinicalupdateon pages 3-6, harris2025congenitaladrenalhyperplasia pages 7-9)

---

## 4. Genetic / molecular information
### 4.1 Causal genes (human)
Primary genes supported in this evidence set:
- **CYP21A2** (21-hydroxylase deficiency; majority of CAH). (concolino2025geneticsincongenital pages 1-2, gunes2025clinicalbiochemicaland pages 1-2)
- Additional CAH-related steroidogenesis genes emphasized for rarer CAH forms include **CYP11B1, HSD3B2, CYP17A1, STAR**. (OpenTargets Search: Congenital adrenal hyperplasia)

Open Targets also associates CAH with these genes and additional steroidogenic components (e.g., CYP11A1, POR), reflecting broader steroidogenesis biology and variant databases. (OpenTargets Search: Congenital adrenal hyperplasia)

### 4.2 Pathogenic variants and functional consequence
- For 21-OHD, loss of 21-hydroxylase reduces conversion of **17-hydroxyprogesterone** to **11-deoxycortisol**, producing precursor accumulation and downstream androgen excess, and increased ACTH drive. (concolino2025geneticsincongenital pages 1-2)
- A practical genotype grouping used clinically links residual activity to phenotype: Group A (no activity → SW), Group B (1–10% → SV), Group C (20–60% → NCCAH). (uslar2023clinicalupdateon pages 6-7)

### 4.3 Modifier genes / contiguous gene syndromes
The retrieved evidence set does not include direct primary-data details on modifier genes, but highlights that complex HLA-locus recombination events contribute to genotypes and diagnostic complexity. (uslar2023clinicalupdateon pages 6-7)

### 4.4 Epigenetics and chromosomal abnormalities
No CAH-specific epigenetic signatures or recurrent chromosomal abnormalities were identified in the retrieved evidence set.

---

## 5. Environmental information
CAH is principally monogenic. Environmental exposures are not described as causal in the retrieved sources; most “environmental” relevance is via **stressors triggering adrenal crisis** in cortisol-deficient individuals and via **treatment-related** adverse effects (chronic supraphysiologic glucocorticoid exposure). (harris2025congenitaladrenalhyperplasia pages 7-9, righi2023longtermcardiometabolicmorbidity pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (21-OHD)
1. **CYP21A2 deficiency → impaired 21-hydroxylation** of progesterone/17-hydroxyprogesterone. (concolino2025geneticsincongenital pages 1-2)
2. **Reduced cortisol ± aldosterone** production → loss of negative feedback on hypothalamic–pituitary axis. (concolino2025geneticsincongenital pages 1-2)
3. **ACTH elevation** → adrenal cortical hyperplasia and increased flux through androgen synthesis pathways. (concolino2025geneticsincongenital pages 1-2, uslar2023clinicalupdateon pages 3-6)
4. **Clinical manifestations**: adrenal insufficiency (including neonatal salt-wasting crisis in SW), prenatal virilization in some 46,XX fetuses, postnatal hyperandrogenism (precocious pubarche, acne, hirsutism, menstrual irregularity, fertility issues), and long-term metabolic/bone comorbidity partly mediated by both disease and treatment exposure. (uslar2023clinicalupdateon pages 3-6, gunes2025clinicalbiochemicaland pages 1-2, righi2023longtermcardiometabolicmorbidity pages 1-2)

### 6.2 Pathway visualization evidence
The steroidogenesis pathway and the CYP21A2 step are shown in a recent genetics review figure (including 17-hydroxyprogesterone and the 21-hydroxylase-catalyzed conversion). (concolino2025geneticsincongenital media e874a3ec)

### 6.3 Suggested ontology terms (mechanism annotation)
*Suggestions (not exhaustively evidenced in the retrieved texts):*
- **GO biological process:** steroid biosynthetic process; glucocorticoid biosynthetic process; mineralocorticoid biosynthetic process; androgen biosynthetic process; response to corticotropin.
- **Cell Ontology (CL):** adrenal cortical cell; zona fasciculata cell; zona glomerulosa cell.
- **UBERON:** adrenal gland; adrenal cortex.

---

## 7. Anatomical structures affected
**Primary:** adrenal cortex (site of impaired steroidogenesis and hyperplasia). (concolino2025geneticsincongenital pages 1-2, uslar2023clinicalupdateon pages 3-6)

**Secondary / complications:**
- **Gonads/reproductive axis:** infertility, menstrual dysfunction; **TARTs** (testicular adrenal rest tumors) in males. (uslar2023clinicalupdateon pages 9-10)
- **Cardiometabolic and skeletal systems:** obesity, hypertension, dyslipidemia, abnormal glucose homeostasis, osteoporosis/osteopenia. (righi2023longtermcardiometabolicmorbidity pages 1-2, zaric2025metabolicsyndromespectrum pages 12-14)

---

## 8. Temporal development
- **SW classic:** onset at birth/early infancy with risk of life-threatening salt-wasting crisis if unrecognized. (uslar2023clinicalupdateon pages 3-6, gunes2025clinicalbiochemicaland pages 1-2)
- **SV classic:** typically recognized in infancy/childhood via hyperandrogenic signs (accelerated growth, advanced bone age, early pubic hair). (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6)
- **NCCAH:** later onset (childhood/adolescence/adulthood) with hyperandrogenism (acne, hirsutism, menstrual irregularities/infertility). (uslar2023clinicalupdateon pages 3-6, gunes2025clinicalbiochemicaland pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology (selected recent/representative statistics)
- **Classic CAH frequency (US, literature estimate in claims paper):** ~**1:16,000** children. (harasymiw2020attentiondeficithyperactivitydisorderamong pages 2-3)
- **Nonclassic CAH prevalence (literature estimate in claims paper):** ~**1:500**. (harasymiw2020attentiondeficithyperactivitydisorderamong pages 2-3)
- **Administrative prevalence in US insured populations (MarketScan/Medicaid, ages 5–18):** **10.1 per 100,000** (Commercial) and **7.2 per 100,000** (Medicaid). (harasymiw2020attentiondeficithyperactivitydisorderamong pages 1-2)
- **Newborn screening cohort (North India hospital program; 2008–2017; n=13,376):** confirmed CAH birth prevalence **~1:2,500**, with sensitivity **100%** and specificity **99.9%** for the CAH screening protocol using dried-blood-spot 17-OHP. (verma2020newbornscreeningfor pages 3-4, verma2020newbornscreeningfor pages 1-2)

### 9.2 Inheritance and recurrence
- **Autosomal recessive inheritance** is consistently stated for 21-OHD CAH. (concolino2025geneticsincongenital pages 1-2, gunes2025clinicalbiochemicaland pages 1-2)
- A prenatal diagnosis/screening review notes a **1 in 4** recurrence risk for any child of carrier parents and **1 in 8** risk for an affected female child (reflecting sex-limited virilization concern). (abalı2025antenataldiagnosisand pages 1-2)

### 9.3 Population genetics
Severe-allele carrier prevalence is summarized as ~**2% (1 in 60)** in a multidisciplinary review. (uslar2023clinicalupdateon pages 9-10)

---

## 10. Diagnostics
Biochemical diagnosis is anchored in 17-hydroxyprogesterone (17-OHP) measurement, assay-aware thresholds, ACTH stimulation testing, and molecular confirmation when indicated.

| Test/biomarker | Specimen & timing | Decision thresholds/cutoffs | Interpretation/use | Supporting citation |
|---|---|---|---|---|
| Basal **17-hydroxyprogesterone (17-OHP)** by immunoassay *(suggested LOINC-style concept: 17-hydroxyprogesterone [Mass/volume] in Serum or Plasma)* | Fasting blood/plasma, **before 9:00 AM**; in menstruating women, sample in **early follicular phase** | **>2 ng/mL** suspicious; **>7–10 ng/mL** considered diagnostic by consensus in reviewed clinical update | First-line biochemical screen for suspected 21-hydroxylase deficiency; values in indeterminate range should prompt ACTH stimulation or additional testing | (uslar2023clinicalupdateon pages 3-6) |
| Basal **17-hydroxyprogesterone (17-OHP)** by LC-MS/MS *(suggested LOINC-style concept: 17-hydroxyprogesterone [Mass/volume] in Serum or Plasma by LC-MS/MS)* | Fasting blood/plasma, **before 9:00 AM**; early follicular phase if cycling | **>0.8 ng/mL** suspicious | Preferred analytical method in the 2023 multidisciplinary review because of improved specificity; used as the main basal threshold before confirmatory ACTH stimulation | (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7) |
| Basal **17-hydroxyprogesterone (17-OHP)**, conventional diagnostic threshold from 2025 review *(suggested LOINC-style concept: 17-hydroxyprogesterone [Mass/volume] in Serum)* | **Early morning** blood sample | **>1000 ng/dL** supports diagnosis of 21-OHD | High morning basal 17-OHP strongly supports CAH due to 21-hydroxylase deficiency; lower borderline values require ACTH stimulation | (gunes2025clinicalbiochemicaland pages 1-2) |
| Borderline basal **17-hydroxyprogesterone (17-OHP)** range requiring ACTH test *(suggested LOINC-style concept: 17-hydroxyprogesterone [Mass/volume] in Serum)* | **Early morning** blood sample | **200–1000 ng/dL** = borderline range | Borderline basal results should be followed by **ACTH stimulation testing** to clarify nonclassic or less severe 21-OHD | (gunes2025clinicalbiochemicaland pages 1-2) |
| **ACTH stimulation test** with 17-OHP readout by LC-MS/MS *(suggested LOINC-style concepts: Corticotropin stimulation panel; 17-hydroxyprogesterone [Mass/volume] in Serum or Plasma post stimulation)* | **250 µg ACTH** (i.m. or i.v.); stimulated blood sampling after standard ACTH test | **Stimulated 17-OHP >3 ng/mL** confirms diagnosis in cited LC-MS/MS framework | Recommended confirmatory test for intermediate/borderline cases and to assess cortisol response in NCCAH | (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7) |
| **ACTH stimulation test** (procedure detail) | **250 µg ACTH** intramuscular or intravenous | Procedure threshold not itself diagnostic; used when basal 17-OHP is indeterminate or ACTH reserve/cortisol response is questioned | Confirms CAH/NCCAH in equivocal cases and helps assess adrenal cortisol reserve; genotype testing is recommended when stimulated 17-OHP is nondiagnostic or ACTH testing is unavailable | (uslar2023clinicalupdateon pages 6-7) |
| **Genotype testing (CYP21A2)** *(suggested LOINC-style concept: CYP21A2 gene targeted mutation analysis / full gene analysis)* | Blood or DNA sample; no timing requirement | No numeric cutoff; indicated when biochemical profile is suspicious, ACTH testing is incomplete/unavailable, or for recurrence-risk interpretation | Supports molecular confirmation, genotype–phenotype interpretation, parental carrier assessment, and counseling | (gunes2025clinicalbiochemicaland pages 1-2, abalı2025antenataldiagnosisand pages 1-2, uslar2023clinicalupdateon pages 6-7) |
| **Newborn screening 17-OHP** on dried blood spot, term infant *(suggested LOINC-style concept: 17-hydroxyprogesterone [Moles/volume] in Dried blood spot)* | Newborn **dried blood specimen** | **<30 nmol/L normal; 30–90 nmol/L intermediate; >90 nmol/L positive** | Population screening for severe CAH; intermediate/positive samples in the India cohort were repeated on a separate blood spot before reporting | (verma2020newbornscreeningfor pages 1-2, verma2020newbornscreeningfor pages 2-3) |
| **Newborn screening 17-OHP** on dried blood spot, preterm infant *(suggested LOINC-style concept: 17-hydroxyprogesterone [Moles/volume] in Dried blood spot)* | Newborn **dried blood specimen** | **<60 nmol/L normal; 60–90 nmol/L intermediate; >90 nmol/L positive** | Adjusted newborn-screening interpretation for prematurity in the India cohort protocol | (verma2020newbornscreeningfor pages 1-2, verma2020newbornscreeningfor pages 2-3) |
| **Newborn screening program performance** (India cohort) | 13,376 newborns screened, dried blood 17-OHP | **15 screen-positive**, **5 true positive**, **10 false positive**; false-positive rate **0.07%**; PPV **33.3%**; NPV **100%**; sensitivity **100%**; specificity **99.9%**; birth prevalence **0.04% (5/13,376) ≈ 1:2,500** | Illustrates real-world performance of newborn screening for CAH using 17-OHP in a hospital-based Indian cohort | (verma2020newbornscreeningfor pages 1-2, verma2020newbornscreeningfor pages 3-4) |
| Confirmatory steroid panel after positive newborn screen *(suggested LOINC-style concepts: 17-hydroxyprogesterone [Mass/volume] in Serum; Cortisol [Mass/volume] in Serum; Dehydroepiandrosterone [Mass/volume] in Serum)* | Fresh **serum/blood draw** after recall; serum cortisol measured at **8 AM and 4 PM** in cited cohort | No single universal cutoff provided in extracted text | Used to confirm abnormal dried-blood-spot screening results after recall of screen-positive newborns | (verma2020newbornscreeningfor pages 2-3) |


*Table: This table summarizes diagnostic tests and cutoffs for congenital adrenal hyperplasia due to 21-hydroxylase deficiency, including basal and stimulated 17-OHP thresholds, assay-specific interpretation, and newborn screening metrics. It is useful as a compact reference for comparing immunoassay, LC-MS/MS, ACTH stimulation, and screening-based approaches.*

Key points from a 2023 multidisciplinary program review include: (i) **LC–MS/MS** is recommended to improve steroid specificity; (ii) basal sampling should be **fasting before 9 AM**, and for cycling women in the **early follicular phase**; (iii) **ACTH stimulation (250 µg i.m./i.v.)** is used to confirm intermediate cases; and (iv) genotype testing is recommended when biochemical evaluation is suspicious or incomplete. (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7)

**Newborn screening implementation (real-world program example):** A decade-long North Indian hospital screening program used dried-blood-spot 17-OHP with term/preterm cutoffs, identified 15 screen positives with 5 true positives (PPV 33.3%), and reported sensitivity 100% and specificity 99.9%. (verma2020newbornscreeningfor pages 3-4, verma2020newbornscreeningfor pages 1-2)

---

## 11. Outcomes / prognosis
### 11.1 Cardiometabolic and bone morbidity (recent data)
A 2023 multicentre specialist survey of **244 adults** with classic 21-OHD CAH (median age 33 years) found **30% (73/244)** were treated for ≥1 of six major comorbidity domains; among treated comorbidities, osteoporosis/osteopenia treatment was most frequent (**59%**), followed by hyperlipidaemia (**23%**), type 2 diabetes/hyperinsulinaemia (**22%**), hypertension (**14%**), cardiovascular disease (**11%**), and obesity (**4%**). (righi2023longtermcardiometabolicmorbidity pages 1-2)

A 2025 pediatric systematic review synthesizing studies through 2024 reports increased cardiometabolic risk factors in children with classic CAH; one included dataset reported **58% systolic hypertension** and **24% diastolic hypertension** with additional abnormalities in nocturnal dipping and subclinical vascular markers. (zaric2025metabolicsyndromespectrum pages 12-14)

### 11.2 Autoimmune comorbidity
A Swedish national cohort study (n=714 21-OHD; 71,400 controls) found autoimmune disorders in **7.4% vs 5.1%** of controls (RR **1.47**, 95% CI 1.13–1.91), with increased autoimmune endocrine and thyroid disorders. (falhammar2019increasedriskof pages 1-2)

---

## 12. Treatment
Standard of care focuses on replacing deficient hormones and limiting androgen excess, balanced against harms of chronic supraphysiologic glucocorticoid exposure.

| Intervention | Mechanism/goal | Typical use case | Key quantitative data | Safety/limitations | MAXO term suggestions | Citations |
|---|---|---|---|---|---|---|
| Hydrocortisone replacement (children) | Replace cortisol deficiency; suppress excess ACTH-driven adrenal androgen production while minimizing hypercortisolism | First-line long-term therapy in pediatric classic 21-hydroxylase deficiency | Preferred regimen **10–15 mg/m²/day divided every 8 h** (uslar2023clinicalupdateon pages 6-7) | Conventional dosing does not reproduce physiologic circadian cortisol rhythm; excess exposure is linked to obesity, hypertension, osteoporosis, and adverse cardiometabolic profile (righi2023longtermcardiometabolicmorbidity pages 1-2) | MAXO: glucocorticoid replacement therapy; hydrocortisone administration | (uslar2023clinicalupdateon pages 6-7, righi2023longtermcardiometabolicmorbidity pages 1-2) |
| Hydrocortisone replacement (adults) | Cortisol replacement with partial androgen control | Standard maintenance therapy in adults with classic CAH | Suggested regimen **15–25 mg/day**, with last dose **≥6 h before bedtime** (uslar2023clinicalupdateon pages 6-7) | Undertreatment leaves androgen excess uncontrolled; overtreatment increases metabolic and bone morbidity (uslar2023clinicalupdateon pages 6-7, righi2023longtermcardiometabolicmorbidity pages 1-2) | MAXO: glucocorticoid replacement therapy; hydrocortisone administration | (uslar2023clinicalupdateon pages 6-7, righi2023longtermcardiometabolicmorbidity pages 1-2) |
| Stress-dose glucocorticoids / sick-day management | Prevent adrenal crisis during physiological stress | Major illness, surgery, trauma, childbirth; also emphasized as lifelong emergency management in severe CAH | Review evidence notes lifelong need for “**sick day**” dosing in response to stressors (harris2025congenitaladrenalhyperplasia pages 7-9) | Required because impaired stress response persists despite routine replacement; inadequate stress dosing risks adrenal crisis (harris2025congenitaladrenalhyperplasia pages 7-9) | MAXO: stress-dose steroid therapy; adrenal crisis prophylaxis | (harris2025congenitaladrenalhyperplasia pages 7-9) |
| Neonatal salt-wasting crisis hydrocortisone regimen | Emergency glucocorticoid rescue in adrenal crisis / severe SW-CAH | Neonates with salt-wasting presentation or adrenal insufficiency | Initial **hydrocortisone bolus 5 mg/kg**, then **25 mg/24 h infusion** or divided doses (uslar2023clinicalupdateon pages 6-7) | Requires urgent electrolyte/fluid management and specialist care; delay can be life-threatening (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 6-7) | MAXO: emergency hydrocortisone therapy; adrenal crisis treatment | (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 6-7) |
| Mineralocorticoid replacement (fludrocortisone) | Replace aldosterone deficiency; maintain sodium balance and blood pressure | Classic salt-wasting CAH; many adults continue combined GC+MC therapy | In one adult cohort, **174/244 (71%)** received fludrocortisone with glucocorticoids (righi2023longtermcardiometabolicmorbidity pages 2-3) | Requires monitoring of **plasma renin** and **electrolytes**; annual renin monitoring is recommended with target at the upper normal limit (uslar2023clinicalupdateon pages 6-7, uslar2023clinicalupdateon pages 9-10) | MAXO: mineralocorticoid replacement therapy; fludrocortisone administration | (uslar2023clinicalupdateon pages 6-7, righi2023longtermcardiometabolicmorbidity pages 2-3, uslar2023clinicalupdateon pages 9-10) |
| Monitoring during glucocorticoid/mineralocorticoid therapy | Optimize replacement and avoid over/undertreatment | Routine follow-up in classic and selected nonclassic CAH | Recommended monitoring includes **plasma renin, electrolytes, cortisol, aldosterone, androstenedione, DHEAS**; annual **BP** and **BMI** monitoring advised (uslar2023clinicalupdateon pages 6-7, uslar2023clinicalupdateon pages 9-10) | Biomarkers vary by assay, timing, age, and medication schedule; standardization remains challenging (uslar2023clinicalupdateon pages 9-10) | MAXO: therapeutic drug monitoring; endocrine laboratory monitoring | (uslar2023clinicalupdateon pages 6-7, uslar2023clinicalupdateon pages 9-10) |
| Combined oral contraceptives (OCPs) for NCCAH hyperandrogenism | Suppress ovarian androgen production and improve hirsutism/acne/cycle control | First-line adjunct in women with NCCAH-related hirsutism/acne | Identified as **first-line** androgen-management option in NCCAH (uslar2023clinicalupdateon pages 9-10) | Symptomatic treatment; does not correct underlying adrenal enzyme defect (uslar2023clinicalupdateon pages 9-10) | MAXO: oral contraceptive therapy; anti-hyperandrogenism management | (uslar2023clinicalupdateon pages 9-10) |
| Spironolactone adjunct | Antiandrogen therapy for persistent hirsutism/acne | Add-on when OCPs alone are insufficient in NCCAH | Suggested dose **50–100 mg/day** (uslar2023clinicalupdateon pages 9-10) | Adjunctive/symptomatic rather than disease-modifying; standard antiandrogen precautions apply (uslar2023clinicalupdateon pages 9-10) | MAXO: antiandrogen therapy; spironolactone administration | (uslar2023clinicalupdateon pages 9-10) |
| Flutamide adjunct | Androgen receptor blockade to improve hyperandrogenic symptoms | Alternative add-on antiandrogen in NCCAH | Suggested dose **62.5–125 mg/day** (uslar2023clinicalupdateon pages 9-10) | Adjunctive/symptomatic therapy; use limited by known antiandrogen safety concerns (not detailed in excerpt) (uslar2023clinicalupdateon pages 9-10) | MAXO: antiandrogen therapy; flutamide administration | (uslar2023clinicalupdateon pages 9-10) |
| Crinecerfont | **CRF1 receptor antagonist** that lowers ACTH drive, enabling androgen control with lower glucocorticoid doses | Emerging adjunct for classic CAH with need to reduce supraphysiologic glucocorticoid exposure | Phase 3 adults: glucocorticoid dose change **−27.3% vs −10.3% placebo**; **62.7% vs 17.5%** achieved physiologic GC dose; week-4 androstenedione **−299 ng/dL vs +45.5 ng/dL**; **P<0.001** for primary comparisons (auchus2024phase3trial pages 1-3) | Most common adverse events were **fatigue** and **headache**; intended as adjunct, not replacement for mandatory steroid therapy (auchus2024phase3trial pages 1-3) | MAXO: corticotropin-releasing hormone receptor antagonist therapy; glucocorticoid-sparing therapy | (auchus2024phase3trial pages 1-3) |
| Tildacerfont | Investigational **CRF1 receptor antagonist** to reduce ACTH-driven androgen excess | Experimental adjunct in adults/children with CAH | Adult Phase 2b trials **NCT04457336** and **NCT04544410**; pediatric Phase 2 **NCT05128942**; listed statuses were **terminated** in retrieved ClinicalTrials.gov summaries (NCT04457336 chunk 3) | Development status uncertain/limited by trial termination in retrieved records; no phase 3 efficacy data in current evidence set | MAXO: corticotropin-releasing hormone receptor antagonist therapy | (NCT04457336 chunk 3) |
| Gene therapy (BBP-631 / gene-transfer approaches) | Deliver functional **CYP21A2** to restore steroidogenesis | Experimental treatment for classic CAH | Review notes **BBP-631 (AAV5 carrying wild-type CYP21A2)** in **phase 1/2** and cites preclinical rescue of steroidogenesis in Cyp21-deficient mice/non-human primates; ClinicalTrials.gov lists **NCT04783181** as an active-not-recruiting phase 1/2 gene therapy study with planned enrollment **8** (glazova2023modelsofcongenital pages 2-4) | Experimental; long-term durability, adrenal targeting, and safety remain under investigation (glazova2023modelsofcongenital pages 2-4) | MAXO: gene replacement therapy; adeno-associated viral gene therapy | (glazova2023modelsofcongenital pages 2-4) |
| Ultradian subcutaneous hydrocortisone infusion | More physiologic cortisol delivery pattern than conventional oral dosing | Experimental/selected use in adrenal insufficiency and CAH | Clinical trial **NCT02096510** completed; phase 1/2 interventional study with **8** participants in Addison disease and CAH (clinical trial summary) (NCT02096510 chunk 2) | Limited evidence base and specialized delivery burden; not routine standard-of-care in retrieved evidence | MAXO: continuous subcutaneous hydrocortisone infusion | (NCT02096510 chunk 2) |


*Table: This table summarizes standard, adjunctive, emerging, and experimental interventions for congenital adrenal hyperplasia due to 21-hydroxylase deficiency, with quantitative dosing or trial data where available. It is designed to support rapid comparison of treatment goals, use cases, limitations, and ontology-aligned action terms.*

### 12.1 Standard pharmacotherapy (real-world implementation)
- **Glucocorticoid replacement:** hydrocortisone is preferred; one review provides typical dosing ranges (children **10–15 mg/m²/day**, adults **15–25 mg/day**) and an emergency neonatal regimen (bolus + infusion). (uslar2023clinicalupdateon pages 6-7)
- **Mineralocorticoid replacement:** fludrocortisone and monitoring of renin/electrolytes are emphasized for SW-CAH; in one adult cohort, **71%** received fludrocortisone. (righi2023longtermcardiometabolicmorbidity pages 2-3, uslar2023clinicalupdateon pages 9-10)
- **Adjunct hyperandrogenism therapy in NCCAH:** OCPs as first-line, with antiandrogens (spironolactone, flutamide) as add-ons when needed. (uslar2023clinicalupdateon pages 9-10)

### 12.2 Recent developments (2023–2024 prioritized)
**Crinecerfont (CRF1 receptor antagonist):** In a randomized phase 3 trial (NEJM, Aug 2024; ClinicalTrials.gov **NCT04490915**), crinecerfont enabled clinically meaningful glucocorticoid dose reduction while maintaining androstenedione control: **−27.3%** dose reduction vs **−10.3%** placebo (P<0.001), and **62.7%** vs **17.5%** achieved physiologic glucocorticoid doses. Androstenedione fell by **−299 ng/dL** at week 4 vs an increase with placebo; fatigue and headache were the most common adverse events. (auchus2024phase3trial pages 1-3)

### 12.3 Experimental / pipeline approaches
- **Gene therapy:** A 2023 model-and-translation review describes an AAV5 gene therapy candidate (BBP-631, CYP21A2) in **phase 1/2**, and ClinicalTrials.gov lists a CAH gene therapy study **NCT04783181** (planned enrollment 8). (glazova2023modelsofcongenital pages 2-4)
- **Physiologic replacement strategies:** ultradian subcutaneous hydrocortisone infusion has been studied in a completed phase 1/2 trial including CAH (NCT02096510). (NCT02096510 chunk 2)

---

## 13. Prevention
### 13.1 Primary prevention
Not applicable in the traditional exposure-avoidance sense for a monogenic, autosomal recessive condition.

### 13.2 Secondary prevention: newborn screening
Multiple reviews advocate newborn screening for early detection of severe forms to reduce mortality and improve management/sex assignment; a large hospital-based India cohort demonstrates feasibility and quantifies performance. (uslar2023clinicalupdateon pages 3-6, abalı2025antenataldiagnosisand pages 1-2, verma2020newbornscreeningfor pages 3-4)

### 13.3 Genetic counseling / reproductive options
Accurate molecular diagnosis (e.g., CYP21A2 sequencing plus MLPA in certified laboratories) is emphasized for counseling; prenatal diagnosis and management remain technically and ethically complex. (abalı2025antenataldiagnosisand pages 1-2)

---

## 14. Other species / natural disease
CAH-like syndromes and enzyme deficiencies have been reported in domestic animals (e.g., cats; dogs), and non-traditional models (ferrets, pigs, spiny mice) are reviewed as potentially useful for adrenal biology due to closer adrenal anatomy/steroidogenesis than rodents. (bilyalova2024nonclassicalanimalmodels pages 2-4)

---

## 15. Model organisms
### 15.1 Zebrafish (in vivo 21-OHD modeling)
A TALEN-generated zebrafish **cyp21a2** null model showed reduced cortisol, increased 17-OHP and 21-deoxycortisol, HPI-axis upregulation, and interrenal hyperplasia, supporting use for systemic consequences of glucocorticoid deficiency; the paper cites CAH incidence ~**1 in 10,000–1 in 15,000**. (eachus2017geneticdisruptionof pages 1-2)

### 15.2 Mouse models (including humanized CYP21A2)
A 2024 paper reports a viable humanized mouse model carrying the clinically relevant **CYP21A2 p.R484Q** variant that develops adrenal hyperplasia and steroid abnormalities and displays sex-specific reproductive phenotypes (female infertility). (thirumalasetty2024ahumanizedand pages 1-2)

A 2022 study established a **humanized CYP21A2** mouse platform (Cyp21a1 replaced by human CYP21A2) that is phenotypically normal, intended as a base for introducing pathogenic mutations. (schubert2022cyp21a2geneexpression pages 1-2)

### 15.3 Model limitations (expert analysis)
A review of adrenal genetic disorder models emphasizes that rodent adrenal steroidogenesis differs from humans (e.g., lack of adrenal 17-hydroxylase and androgen production), limiting recapitulation of human virilization/hyperandrogenism phenotypes. (beuschlein2023animalmodelsof pages 2-4)

---

## Direct abstract quotes (selected, for anchoring key claims)
- Uslar et al. (2023) describe CAH as “**characterized by the overproduction of androgen, along with variable degrees of cortisol and aldosterone deficiency**.” (uslar2023clinicalupdateon pages 3-6)
- Auchus et al. (NEJM 2024) conclude: “**crinecerfont permitted reduction of supraphysiological glucocorticoid doses, including to physiological range**…” (auchus2024phase3trial pages 1-3)
- Verma et al. (2020) report: “**From January 2008 through December 2017, 13,376 newborns were screened… by measuring… 17-hydroxyprogesterone…**” and report CAH birth prevalence **1:2,500** with “**100% sensitivity and >99% specificity**.” (verma2020newbornscreeningfor pages 1-2)

---

## Evidence-backed subtype summary table
| CAH subtype / etiology | Causal gene(s) | Key biochemical hallmarks | Typical onset | Key reference(s) |
|---|---|---|---|---|
| 21-hydroxylase deficiency, classic salt-wasting (SW) | **CYP21A2** | Cortisol deficiency with aldosterone deficiency; excess adrenal androgens; neonatal salt-wasting crisis with electrolyte disturbance; residual enzyme activity typically **<1%** (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7, concolino2025geneticsincongenital pages 1-2) | Neonatal / early infancy (uslar2023clinicalupdateon pages 3-6, concolino2025geneticsincongenital pages 1-2) | Uslar et al., 2023, J Clin Med, https://doi.org/10.3390/jcm12093128 (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7); Concolino & Falhammar, 2025, J Endocrine Soc, https://doi.org/10.1210/jendso/bvaf018 (concolino2025geneticsincongenital pages 1-2) |
| 21-hydroxylase deficiency, classic simple virilizing (SV) | **CYP21A2** | Cortisol deficiency with preserved mineralocorticoid function; androgen excess with virilization / precocious pubarche / accelerated growth; residual activity about **1–2%** or **1–10%** depending on grouping scheme (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7) | Infancy / childhood (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6) | Uslar et al., 2023, J Clin Med, https://doi.org/10.3390/jcm12093128 (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7); Güneş et al., 2025, JCRPE, https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-6-s (gunes2025clinicalbiochemicaland pages 1-2) |
| 21-hydroxylase deficiency, nonclassic (NCCAH) | **CYP21A2** | Mild cortisol impairment with hyperandrogenism; morning **17-OHP** often elevated, ACTH-stimulated increase used diagnostically; residual activity about **20–50%** (or **20–60%** in mutation grouping) (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7) | Late childhood, adolescence, or adulthood (gunes2025clinicalbiochemicaland pages 1-2, uslar2023clinicalupdateon pages 3-6) | Uslar et al., 2023, J Clin Med, https://doi.org/10.3390/jcm12093128 (uslar2023clinicalupdateon pages 3-6, uslar2023clinicalupdateon pages 6-7); Güneş et al., 2025, JCRPE, https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-6-s (gunes2025clinicalbiochemicaland pages 1-2) |
| 11β-hydroxylase deficiency | **CYP11B1** | Inability to produce cortisol and aldosterone with excessive adrenal androgen production; laboratory/clinical features can resemble 21-OHD but **mineralocorticoid deficiency findings are not observed** (OpenTargets Search: Congenital adrenal hyperplasia) | Childhood / early life (not further specified in extracted evidence) (OpenTargets Search: Congenital adrenal hyperplasia) | İsakoca et al., 2025, JCRPE, https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-21-s (OpenTargets Search: Congenital adrenal hyperplasia) |
| 17α-hydroxylase deficiency | **CYP17A1** | Impaired sex steroid synthesis; **46,XY DSD** in boys and estrogen deficiency with immature puberty / primary amenorrhea in girls (OpenTargets Search: Congenital adrenal hyperplasia) | Childhood to adolescence / puberty (OpenTargets Search: Congenital adrenal hyperplasia) | İsakoca et al., 2025, JCRPE, https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-21-s (OpenTargets Search: Congenital adrenal hyperplasia) |
| 3β-hydroxysteroid dehydrogenase deficiency | **HSD3B2** | Early impairment of adrenal and gonadal steroid biosynthesis; inadequate virilization in boys, variable virilization in girls; may present with **salt-wasting crisis** (OpenTargets Search: Congenital adrenal hyperplasia) | Neonatal / infancy, sometimes delayed puberty (OpenTargets Search: Congenital adrenal hyperplasia) | İsakoca et al., 2025, JCRPE, https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-21-s (OpenTargets Search: Congenital adrenal hyperplasia) |
| Lipoid CAH | **STAR** | Near-complete deficiency of adrenal and gonadal steroid hormones with progressive accumulation of cholesterol esters in adrenal gland; severe salt wasting (OpenTargets Search: Congenital adrenal hyperplasia) | First year of life (OpenTargets Search: Congenital adrenal hyperplasia) | İsakoca et al., 2025, JCRPE, https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-21-s (OpenTargets Search: Congenital adrenal hyperplasia) |


*Table: This table compacts the main congenital adrenal hyperplasia etiologies discussed in the gathered evidence, linking each subtype to its causal gene, core biochemical pattern, and typical onset. It is useful as a quick-reference map for differentiating common 21-hydroxylase deficiency forms from rarer enzyme defects.*

---

## Notes on evidence gaps for this run
- Specific OMIM, Orphanet (ORPHA), MeSH, and ICD-11 identifiers were not retrieved as full-text evidence in this tool run; the report therefore does not assert them.
- Detailed ClinVar-style variant lists (HGVS nomenclature, allele frequencies in gnomAD) and epigenetic studies were not present in retrieved evidence and are not enumerated.

---

## Key source URLs (with publication dates)
- Uslar T et al. *Journal of Clinical Medicine* **2023-04**. https://doi.org/10.3390/jcm12093128 (uslar2023clinicalupdateon pages 3-6)
- Auchus RJ et al. *New England Journal of Medicine* **2024-08**. https://doi.org/10.1056/NEJMoa2404656 (auchus2024phase3trial pages 1-3)
- Concolino P, Falhammar H. *Journal of the Endocrine Society* **2025-01**. https://doi.org/10.1210/jendso/bvaf018 (concolino2025geneticsincongenital pages 1-2)
- Righi B et al. *Endocrine* **2023-03**. https://doi.org/10.1007/s12020-023-03330-w (righi2023longtermcardiometabolicmorbidity pages 1-2)
- Verma J et al. *Journal of Pediatric Intensive Care* **2020-10**. https://doi.org/10.1055/s-0039-1698424 (verma2020newbornscreeningfor pages 1-2)



References

1. (concolino2025geneticsincongenital pages 1-2): Paola Concolino and Henrik Falhammar. Genetics in congenital adrenal hyperplasia due to 21-hydroxylase deficiency and clinical implications. Journal of the Endocrine Society, Jan 2025. URL: https://doi.org/10.1210/jendso/bvaf018, doi:10.1210/jendso/bvaf018. This article has 7 citations and is from a peer-reviewed journal.

2. (gunes2025clinicalbiochemicaland pages 1-2): Sevinç Odabaşı Güneş, Havva Nur Peltek Kendirci, Edip Ünal, Ayşe Derya Buluş, İsmail Dündar, and Zeynep Şıklar. Clinical, biochemical and molecular characteristics of congenital adrenal hyperplasia due to 21-hydroxylase deficiency. Journal of Clinical Research in Pediatric Endocrinology, 17:3-11, Dec 2025. URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-6-s, doi:10.4274/jcrpe.galenos.2024.2024-6-6-s. This article has 16 citations.

3. (uslar2023clinicalupdateon pages 3-6): Thomas Uslar, Roberto Olmos, Alejandro Martínez-Aguayo, and René Baudrand. Clinical update on congenital adrenal hyperplasia: recommendations from a multidisciplinary adrenal program. Journal of Clinical Medicine, 12:3128, Apr 2023. URL: https://doi.org/10.3390/jcm12093128, doi:10.3390/jcm12093128. This article has 43 citations.

4. (OpenTargets Search: Congenital adrenal hyperplasia): Open Targets Query (Congenital adrenal hyperplasia, 24 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (harasymiw2020attentiondeficithyperactivitydisorderamong pages 3-3): Lauren A Harasymiw, Scott D Grosse, and Kyriakie Sarafoglou. Attention-deficit/hyperactivity disorder among us children and adolescents with congenital adrenal hyperplasia. Journal of the Endocrine Society, Oct 2020. URL: https://doi.org/10.1210/jendso/bvaa152, doi:10.1210/jendso/bvaa152. This article has 9 citations and is from a peer-reviewed journal.

6. (falhammar2019increasedriskof pages 2-3): Henrik Falhammar, Louise Frisén, Angelica Linden Hirschberg, Agneta Nordenskjöld, Catarina Almqvist, and Anna Nordenström. Increased risk of autoimmune disorders in 21-hydroxylase deficiency: a swedish population-based national cohort study. Journal of the Endocrine Society, 3:1039-1052, Apr 2019. URL: https://doi.org/10.1210/js.2019-00122, doi:10.1210/js.2019-00122. This article has 26 citations and is from a peer-reviewed journal.

7. (auchus2024phase3trial pages 1-3): Richard J. Auchus, Oksana Hamidi, Rosario Pivonello, Irina Bancos, Gianni Russo, Selma F. Witchel, Andrea M. Isidori, Patrice Rodien, Umasuthan Srirangalingam, Florian W. Kiefer, Henrik Falhammar, Deborah P. Merke, Nicole Reisch, Kyriakie Sarafoglou, Gordon B. Cutler, Julia Sturgeon, Eiry Roberts, Vivian H. Lin, Jean L. Chan, and Robert H. Farber. Phase 3 trial of crinecerfont in adult congenital adrenal hyperplasia. New England Journal of Medicine, 391:504-514, Aug 2024. URL: https://doi.org/10.1056/nejmoa2404656, doi:10.1056/nejmoa2404656. This article has 63 citations and is from a highest quality peer-reviewed journal.

8. (falhammar2019increasedriskof pages 1-2): Henrik Falhammar, Louise Frisén, Angelica Linden Hirschberg, Agneta Nordenskjöld, Catarina Almqvist, and Anna Nordenström. Increased risk of autoimmune disorders in 21-hydroxylase deficiency: a swedish population-based national cohort study. Journal of the Endocrine Society, 3:1039-1052, Apr 2019. URL: https://doi.org/10.1210/js.2019-00122, doi:10.1210/js.2019-00122. This article has 26 citations and is from a peer-reviewed journal.

9. (righi2023longtermcardiometabolicmorbidity pages 1-2): Beatrice Righi, Salma R. Ali, Jillian Bryce, Jeremy W. Tomlinson, Walter Bonfig, Federico Baronio, Eduardo C. Costa, Guilherme Guaragna-Filho, Guy T’Sjoen, Martine Cools, Renata Markosyan, Tania A. S. S. Bachega, Mirela C. Miranda, Violeta Iotova, Henrik Falhammar, Filippo Ceccato, Marianna R. Stancampiano, Gianni Russo, Eleni Daniel, Richard J. Auchus, Richard J. Ross, and S. Faisal Ahmed. Long-term cardiometabolic morbidity in young adults with classic 21-hydroxylase deficiency congenital adrenal hyperplasia. Endocrine, 80:630-638, Mar 2023. URL: https://doi.org/10.1007/s12020-023-03330-w, doi:10.1007/s12020-023-03330-w. This article has 14 citations and is from a peer-reviewed journal.

10. (verma2020newbornscreeningfor pages 1-2): Jyotsna Verma, Papai Roy, Divya C. Thomas, Geetu Jhingan, Azad Singh, Sunita Bijarnia-Mahay, and Ishwar C. Verma. Newborn screening for congenital hypothyroidism, congenital adrenal hyperplasia, and glucose-6-phosphate dehydrogenase deficiency for improving health care in india. Journal of Pediatric Intensive Care, 09:040-044, Oct 2020. URL: https://doi.org/10.1055/s-0039-1698424, doi:10.1055/s-0039-1698424. This article has 19 citations.

11. (eachus2017geneticdisruptionof pages 1-2): Helen Eachus, Andreas Zaucker, James A Oakes, Aliesha Griffin, Meltem Weger, Tülay Güran, Angela Taylor, Abigail Harris, Andy Greenfield, Jonathan L Quanson, Karl-Heinz Storbeck, Vincent T Cunliffe, Ferenc Müller, and Nils Krone. Genetic disruption of 21-hydroxylase in zebrafish causes interrenal hyperplasia. Endocrinology, 158:4165-4173, Sep 2017. URL: https://doi.org/10.1210/en.2017-00549, doi:10.1210/en.2017-00549. This article has 36 citations and is from a domain leading peer-reviewed journal.

12. (thirumalasetty2024ahumanizedand pages 1-2): Shamini Ramkumar Thirumalasetty, Tina Schubert, Ronald Naumann, Ilka Reichardt, Marie-Luise Rohm, Dana Landgraf, Florian Gembardt, Mirko Peitzsch, Michaela F. Hartmann, Mihail Sarov, Stefan A. Wudy, Nicole Reisch, Angela Huebner, and Katrin Koehler. A humanized and viable animal model for congenital adrenal hyperplasia–cyp21a2-r484q mutant mouse. International Journal of Molecular Sciences, 25:5062, May 2024. URL: https://doi.org/10.3390/ijms25105062, doi:10.3390/ijms25105062. This article has 5 citations.

13. (glazova2023modelsofcongenital pages 2-4): Olga Glazova, Asya Bastrich, Andrei Deviatkin, Nikita Onyanov, Samira Kaziakhmedova, Liudmila Shevkova, Nawar Sakr, Daria Petrova, Maria V. Vorontsova, and Pavel Volchkov. Models of congenital adrenal hyperplasia for gene therapies testing. International Journal of Molecular Sciences, 24:5365, Mar 2023. URL: https://doi.org/10.3390/ijms24065365, doi:10.3390/ijms24065365. This article has 10 citations.

14. (uslar2023clinicalupdateon pages 6-7): Thomas Uslar, Roberto Olmos, Alejandro Martínez-Aguayo, and René Baudrand. Clinical update on congenital adrenal hyperplasia: recommendations from a multidisciplinary adrenal program. Journal of Clinical Medicine, 12:3128, Apr 2023. URL: https://doi.org/10.3390/jcm12093128, doi:10.3390/jcm12093128. This article has 43 citations.

15. (uslar2023clinicalupdateon pages 9-10): Thomas Uslar, Roberto Olmos, Alejandro Martínez-Aguayo, and René Baudrand. Clinical update on congenital adrenal hyperplasia: recommendations from a multidisciplinary adrenal program. Journal of Clinical Medicine, 12:3128, Apr 2023. URL: https://doi.org/10.3390/jcm12093128, doi:10.3390/jcm12093128. This article has 43 citations.

16. (abalı2025antenataldiagnosisand pages 1-2): Zehra Yavaş Abalı, Erdal Kurnaz, and Tülay Güran. Antenatal diagnosis and treatment in congenital adrenal hyperplasia due to 21-hydroxylase deficiency and congenital adrenal hyperplasia screening in newborns. Journal of Clinical Research in Pediatric Endocrinology, 17:33-43, Dec 2025. URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-6-10-s, doi:10.4274/jcrpe.galenos.2024.2024-6-10-s. This article has 1 citations.

17. (righi2023longtermcardiometabolicmorbidity pages 4-5): Beatrice Righi, Salma R. Ali, Jillian Bryce, Jeremy W. Tomlinson, Walter Bonfig, Federico Baronio, Eduardo C. Costa, Guilherme Guaragna-Filho, Guy T’Sjoen, Martine Cools, Renata Markosyan, Tania A. S. S. Bachega, Mirela C. Miranda, Violeta Iotova, Henrik Falhammar, Filippo Ceccato, Marianna R. Stancampiano, Gianni Russo, Eleni Daniel, Richard J. Auchus, Richard J. Ross, and S. Faisal Ahmed. Long-term cardiometabolic morbidity in young adults with classic 21-hydroxylase deficiency congenital adrenal hyperplasia. Endocrine, 80:630-638, Mar 2023. URL: https://doi.org/10.1007/s12020-023-03330-w, doi:10.1007/s12020-023-03330-w. This article has 14 citations and is from a peer-reviewed journal.

18. (righi2023longtermcardiometabolicmorbidity pages 2-3): Beatrice Righi, Salma R. Ali, Jillian Bryce, Jeremy W. Tomlinson, Walter Bonfig, Federico Baronio, Eduardo C. Costa, Guilherme Guaragna-Filho, Guy T’Sjoen, Martine Cools, Renata Markosyan, Tania A. S. S. Bachega, Mirela C. Miranda, Violeta Iotova, Henrik Falhammar, Filippo Ceccato, Marianna R. Stancampiano, Gianni Russo, Eleni Daniel, Richard J. Auchus, Richard J. Ross, and S. Faisal Ahmed. Long-term cardiometabolic morbidity in young adults with classic 21-hydroxylase deficiency congenital adrenal hyperplasia. Endocrine, 80:630-638, Mar 2023. URL: https://doi.org/10.1007/s12020-023-03330-w, doi:10.1007/s12020-023-03330-w. This article has 14 citations and is from a peer-reviewed journal.

19. (zaric2025metabolicsyndromespectrum pages 1-2): Sanja Panic Zaric, Tatjana Milenkovic, Sladjana Todorovic, Katarina Mitrovic, Dimitrije Cvetkovic, Maja Cehic, Jelena Vekic, Katja Dumic, and Rade Vukovic. Metabolic syndrome spectrum in children with classic congenital adrenal hyperplasia—a comprehensive review. Metabolites, 15:89, Feb 2025. URL: https://doi.org/10.3390/metabo15020089, doi:10.3390/metabo15020089. This article has 4 citations.

20. (zaric2025metabolicsyndromespectrum pages 12-14): Sanja Panic Zaric, Tatjana Milenkovic, Sladjana Todorovic, Katarina Mitrovic, Dimitrije Cvetkovic, Maja Cehic, Jelena Vekic, Katja Dumic, and Rade Vukovic. Metabolic syndrome spectrum in children with classic congenital adrenal hyperplasia—a comprehensive review. Metabolites, 15:89, Feb 2025. URL: https://doi.org/10.3390/metabo15020089, doi:10.3390/metabo15020089. This article has 4 citations.

21. (harris2025congenitaladrenalhyperplasia pages 7-9): David E. Harris. Congenital adrenal hyperplasia: a clinical review. Universal Library of Clinical Nursing, 02:08-17, Feb 2025. URL: https://doi.org/10.70315/uloap.ulcnu.2025.0201002, doi:10.70315/uloap.ulcnu.2025.0201002. This article has 1 citations.

22. (concolino2025geneticsincongenital media e874a3ec): Paola Concolino and Henrik Falhammar. Genetics in congenital adrenal hyperplasia due to 21-hydroxylase deficiency and clinical implications. Journal of the Endocrine Society, Jan 2025. URL: https://doi.org/10.1210/jendso/bvaf018, doi:10.1210/jendso/bvaf018. This article has 7 citations and is from a peer-reviewed journal.

23. (harasymiw2020attentiondeficithyperactivitydisorderamong pages 2-3): Lauren A Harasymiw, Scott D Grosse, and Kyriakie Sarafoglou. Attention-deficit/hyperactivity disorder among us children and adolescents with congenital adrenal hyperplasia. Journal of the Endocrine Society, Oct 2020. URL: https://doi.org/10.1210/jendso/bvaa152, doi:10.1210/jendso/bvaa152. This article has 9 citations and is from a peer-reviewed journal.

24. (harasymiw2020attentiondeficithyperactivitydisorderamong pages 1-2): Lauren A Harasymiw, Scott D Grosse, and Kyriakie Sarafoglou. Attention-deficit/hyperactivity disorder among us children and adolescents with congenital adrenal hyperplasia. Journal of the Endocrine Society, Oct 2020. URL: https://doi.org/10.1210/jendso/bvaa152, doi:10.1210/jendso/bvaa152. This article has 9 citations and is from a peer-reviewed journal.

25. (verma2020newbornscreeningfor pages 3-4): Jyotsna Verma, Papai Roy, Divya C. Thomas, Geetu Jhingan, Azad Singh, Sunita Bijarnia-Mahay, and Ishwar C. Verma. Newborn screening for congenital hypothyroidism, congenital adrenal hyperplasia, and glucose-6-phosphate dehydrogenase deficiency for improving health care in india. Journal of Pediatric Intensive Care, 09:040-044, Oct 2020. URL: https://doi.org/10.1055/s-0039-1698424, doi:10.1055/s-0039-1698424. This article has 19 citations.

26. (verma2020newbornscreeningfor pages 2-3): Jyotsna Verma, Papai Roy, Divya C. Thomas, Geetu Jhingan, Azad Singh, Sunita Bijarnia-Mahay, and Ishwar C. Verma. Newborn screening for congenital hypothyroidism, congenital adrenal hyperplasia, and glucose-6-phosphate dehydrogenase deficiency for improving health care in india. Journal of Pediatric Intensive Care, 09:040-044, Oct 2020. URL: https://doi.org/10.1055/s-0039-1698424, doi:10.1055/s-0039-1698424. This article has 19 citations.

27. (NCT04457336 chunk 3):  A Ph2b to Evaluate Clinical Efficacy and Safety of Tildacerfont in Adult CAH. Spruce Biosciences. 2020. ClinicalTrials.gov Identifier: NCT04457336

28. (NCT02096510 chunk 2):  Ultradian Subcutaneous Hydrocortisone Infusion in Addison Disease and Congenital Adrenal Hyperplasia. Haukeland University Hospital. 2014. ClinicalTrials.gov Identifier: NCT02096510

29. (bilyalova2024nonclassicalanimalmodels pages 2-4): Alina Bilyalova, Airat Bilyalov, Nikita Filatov, Elena Shagimardanova, Andrey Kiyasov, Maria Vorontsova, and Oleg Gusev. Non-classical animal models for studying adrenal diseases: advantages, limitations, and implications for research. Laboratory Animal Research, Jun 2024. URL: https://doi.org/10.1186/s42826-024-00212-8, doi:10.1186/s42826-024-00212-8. This article has 4 citations.

30. (schubert2022cyp21a2geneexpression pages 1-2): Tina Schubert, Nicole Reisch, Ronald Naumann, Ilka Reichardt, Dana Landgraf, Friederike Quitter, Shamini Ramkumar Thirumalasetty, Anne-Kristin Heninger, Mihail Sarov, Mirko Peitzsch, Angela Huebner, and Katrin Koehler. Cyp21a2 gene expression in a humanized 21-hydroxylase mouse model does not affect adrenocortical morphology and function. Journal of the Endocrine Society, Apr 2022. URL: https://doi.org/10.1210/jendso/bvac062, doi:10.1210/jendso/bvac062. This article has 8 citations and is from a peer-reviewed journal.

31. (beuschlein2023animalmodelsof pages 2-4): Felix Beuschlein. Animal models of adrenal genetic disorders. ArXiv, pages 323-329, Jan 2023. URL: https://doi.org/10.1016/b978-0-12-416006-4.00026-0, doi:10.1016/b978-0-12-416006-4.00026-0. This article has 2 citations.