---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T13:08:57.537851'
end_time: '2026-04-05T13:30:31.689756'
duration_seconds: 1294.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRAF V600 Mutant Melanoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** BRAF V600 Mutant Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600 Mutant Melanoma** covering all of the
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
- **Disease Name:** BRAF V600 Mutant Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600 Mutant Melanoma** covering all of the
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


## Disease Characteristics Research Report: BRAF V600–Mutant Melanoma

### Target Disease
- **Disease name:** BRAF V600–mutant cutaneous melanoma (localized, resectable, unresectable/metastatic) (marquezrodas2024seomgemclinicalguidelines pages 1-2, castellani2023brafmutationsin pages 1-2)
- **Category:** Neoplastic disease (cutaneous malignant melanoma defined by oncogenic BRAF V600 driver mutation)
- **MONDO ID:** Not identified in the retrieved primary/guideline sources in this run (marquezrodas2024seomgemclinicalguidelines pages 1-2, NCT02036086 chunk 2)

| Disease label | ICD-10 code | MeSH term / ID | Key molecular synonyms | Staging system referenced | Source (first author, year) | Publication date | URL / DOI |
|---|---|---|---|---|---|---|---|
| BRAF V600–mutant cutaneous melanoma | C43 (malignant melanoma of skin) (hoejberg2016trendsinmelanoma pages 1-3) | Melanoma / D008545 (NCT02036086 chunk 2) | BRAFmut; BRAFV600mut; BRAFV600E/K (marquezrodas2024seomgemclinicalguidelines pages 1-2, ghate2018healthcareresourceutilization pages 1-5) | AJCC 8th edition (marquezrodas2024seomgemclinicalguidelines pages 1-2, dixon2024primarycutaneousmelanoma—management pages 1-2) | Márquez-Rodas, 2024; Hoejberg, 2016; ClinicalTrials.gov NCT02036086 (marquezrodas2024seomgemclinicalguidelines pages 1-2, NCT02036086 chunk 2, hoejberg2016trendsinmelanoma pages 1-3) | May 2024; Jan 2016; trial record 2015 | https://doi.org/10.1007/s12094-024-03497-2 ; https://doi.org/10.3109/0284186x.2015.1114677 ; NCT02036086 |
| BRAF V600–mutant metastatic melanoma | C43 (used for malignant melanoma of skin in registry-based melanoma coding; metastatic subset not separately coded in retrieved texts) (hoejberg2016trendsinmelanoma pages 1-3) | Melanoma / D008545 (NCT02036086 chunk 2) | BRAF-mutant melanoma; BRAFV600-mutant melanoma; BRAFV600E/K–mutant advanced or metastatic melanoma (dummer2026exploratoryanalysisof pages 20-21) | AJCC 8th edition referenced in melanoma guidelines/management sources (marquezrodas2024seomgemclinicalguidelines pages 1-2, dixon2024primarycutaneousmelanoma—management pages 1-2) | Dummer, 2026; Ghate, 2018; ClinicalTrials.gov NCT02036086 (dummer2026exploratoryanalysisof pages 20-21, ghate2018healthcareresourceutilization pages 1-5, NCT02036086 chunk 2) | Jan 2026; Aug 2018; trial record 2015 | https://doi.org/10.1158/1078-0432.ccr-25-3262 ; https://doi.org/10.1080/03007995.2018.1501351 ; NCT02036086 |


*Table: This table summarizes the principal coded disease terms and naming conventions that can anchor a knowledge base entry for BRAF V600–mutant melanoma. It also notes the staging framework used in the retrieved guideline and trial sources.*

### 1. Disease Information
**Definition/overview.** Cutaneous melanoma is a malignant neoplasm derived from melanocytes and is the skin-cancer subtype responsible for most skin cancer deaths due to metastatic potential (belloni2025treatmentrelatedadverseevents pages 1-2, frantz2020fromtankto pages 1-3). “BRAF V600–mutant melanoma” is a molecularly defined subset characterized by an activating missense substitution at BRAF codon 600 (most commonly V600E; also V600K/R/D/M), which constitutively activates MAPK signaling and enables use of BRAF/MEK targeted therapies (castellani2023brafmutationsin pages 1-2, castellani2023brafmutationsin pages 2-4).

**Key identifiers and code systems (available in retrieved sources).** Melanoma was operationalized as **ICD-10 C43** in a Danish registry analysis (hoejberg2016trendsinmelanoma pages 1-3). A ClinicalTrials.gov record lists **MeSH “Melanoma” (MeSH ID D008545)** (NCT02036086 chunk 2).

**Common synonyms/alternative names used in the literature.** “Cutaneous melanoma,” “BRAF-mutant melanoma,” “BRAF V600E/K–mutant melanoma,” and shorthand “BRAFmut/BRAFV600mut” appear in clinical and review literature and guidelines (mohr2025updateonthe pages 2-3, marquezrodas2024seomgemclinicalguidelines pages 1-2, dummer2026exploratoryanalysisof pages 20-21).

**Evidence source type.** The evidence synthesized here is primarily aggregated disease-level knowledge (guidelines/reviews), augmented with randomized trials and observational/real-world cohorts (marquezrodas2024seomgemclinicalguidelines pages 1-2, bai2023dabrafenibplustrametinib pages 1-2, ascierto2024sequentialimmunotherapyand pages 1-2).

### 2. Etiology
**Causal and mechanistic factors.** Ultraviolet (UV) radiation (natural sunlight and artificial tanning) is consistently described as the leading environmental risk factor for melanoma development (florent2023brafv600mutatedmetastatic pages 1-2, mohr2025updateonthe pages 2-2). Molecularly, BRAF V600 mutations are common early driver events (including in nevi), but additional alterations are typically required for progression to melanoma (pelosi2024brafmutantmelanomasbiology pages 4-5, pelosi2024brafmutantmelanomasbiology pages 2-4).

**Risk factors (environmental/host/genetic).** Reported risks include high UV exposure, personal or family history of melanoma (florent2023brafv600mutatedmetastatic pages 1-2), and host pigmentation phenotypes (e.g., pale skin, freckles, light/red hair) associated with increased melanoma risk (castellani2023brafmutationsin pages 1-2). BRAF-mutant melanomas are reported to be more frequent in younger patients and those with intermittent (occasional) sun exposure compared with chronically sun-exposed individuals (castellani2023brafmutationsin pages 2-4). The V600K subtype is specifically linked to chronic sun damage/exposure (pelosi2024brafmutantmelanomasbiology pages 4-5, pelosi2024brafmutantmelanomasbiology pages 2-4).

**Protective factors.** Direct protective factors were not quantified in the retrieved melanoma/BRAF V600–specific sources; however, UV exposure is the leading modifiable driver, implying sun-protective behaviors as primary prevention (mohr2025updateonthe pages 2-2, manganelli2025skinphotodamageand pages 1-2).

**Gene–environment interaction (current understanding).** One mechanistic bridge between UV exposure and melanocyte biology is UV-triggered melanocortin signaling (e.g., α-MSH/MC1R → MITF via cAMP–PKA–CREB), linking environmental exposure to transcriptional programs that intersect with MAPK pathway biology (castellani2023brafmutationsin pages 4-6).

### 3. Phenotypes
#### 3.1 Core clinical phenotypes (primary disease)
- **Primary cutaneous melanoma subtypes:** superficial spreading melanoma (SSM) and nodular melanoma (NM) are the most common primary histologies (~70% and ~15%, respectively) (pelosi2024brafmutantmelanomasbiology pages 1-2). NM is described as particularly lethal and responsible for ~40% of melanoma deaths (pelosi2024brafmutantmelanomasbiology pages 1-2).
- **Progression pattern:** SSM is described as having radial growth followed by vertical growth and metastatic potential; NM rapidly enters vertical growth phase and tends to be thicker (pelosi2024brafmutantmelanomasbiology pages 1-2).

**Suggested HPO terms (examples).**
- Cutaneous neoplasm/skin lesion: **HP:0008069** (abnormality of skin morphology) / **HP:0008064** (skin neoplasm; if using disease-phenotype mapping)
- Ulceration: **HP:0001052**
- Increased Breslow thickness / deep invasion: not a single canonical HPO term; can map via “invasive melanoma” phenotype ontology in cancer-specific vocabularies (not retrieved here)

#### 3.2 Metastatic phenotypes and key sites
- **Brain metastases:** brain metastases occur in ~40–50% of patients with cutaneous melanoma and are highlighted as a major clinical problem (ascierto2024sequencingofcheckpoint pages 1-2). In SECOMBIT, new brain metastases occurred in 23/69 (targeted-first), 11/69 (immunotherapy-first), and 9/68 (sandwich) (ascierto2024sequencingofcheckpoint pages 1-2).

**Suggested HPO terms (examples).**
- Metastatic neoplasm: **HP:0003002**
- Lymph node metastasis: **HP:0012735**
- Brain metastasis: not a standard HPO term in all releases; often represented via “metastatic neoplasm of the brain” in oncology ontologies (mapping may require NCIt)

#### 3.3 Treatment-related symptom phenotypes (toxicity burden)
A meta-analysis reported pooled toxicity prevalences for commonly used BRAF/MEK inhibitor regimens:
- Vemurafenib: arthralgia 44% (95% CI 29–59%); rash 39% (95% CI 22–56%) (belloni2025treatmentrelatedadverseevents pages 1-2).
- Dabrafenib + trametinib: fatigue 47% (95% CI 38–56%); pyrexia 40% (95% CI 26–54%) (belloni2025treatmentrelatedadverseevents pages 1-2).

**Suggested HPO terms (examples).**
- Arthralgia: **HP:0002829**
- Rash: **HP:0000988**
- Pyrexia: **HP:0001945**
- Fatigue: **HP:0012378**

**Quality of life (QoL).** In the retrieved set, QoL evidence is largely indirect (treatment discontinuation/toxicity; patient narrative). A patient+oncologist perspective emphasizes long-term adverse effects and individualized decision-making over a decade-long course (finke2024brafv600emetastaticmelanoma pages 1-2).

### 4. Genetic/Molecular Information
#### 4.1 Causal gene(s) and driver variants
- **Causal/driver gene:** **BRAF** (HGNC:1097; OMIM *164757 referenced) (castellani2023brafmutationsin pages 2-4).
- **Variant spectrum and relative frequencies (melanoma):** somatic BRAF variants occur in ~50% of melanomas; most are codon-600 substitutions. V600E accounts for ~70–88% of BRAF-positive melanomas; V600K ~10–20%; non-V600 ~11% (castellani2023brafmutationsin pages 2-4).

#### 4.2 Functional consequences and pathways
- **MAPK activation:** BRAFV600 (class I) is a RAS-independent activating mutant that constitutively activates the RAS/RAF/MEK/ERK cascade (shang2026brafinhibitorresistance pages 2-3, cosci2025molecularbasisof pages 2-4). V600E is described as a phosphomimetic with ~480-fold increased kinase activity and associated with increased cell growth (cosci2025molecularbasisof pages 2-4).

**Suggested GO Biological Process terms (examples).**
- MAPK cascade: **GO:0000165**
- ERK1 and ERK2 cascade: **GO:0070371**
- Positive regulation of cell population proliferation: **GO:0008284**
- Epithelial to mesenchymal transition (phenotype switching analogue): **GO:0001837**

**Suggested Cell Ontology (CL) terms (examples).**
- Melanocyte: **CL:0000148**
- Regulatory T cell (immune evasion context): **CL:0000815** (supported by BRAF-driven Treg recruitment models in the broader literature base retrieved) (shang2026brafinhibitorresistance pages 2-3)

#### 4.3 Co-mutations / modifiers and resistance biology
Co-altered pathways/genes frequently implicated include **NRAS, NF1, PTEN, TP53, CDKN2A, TERT promoter**, and regulators of melanoma state such as **MITF** (pelosi2024brafmutantmelanomasbiology pages 1-2, castellani2023brafmutationsin pages 11-12).

Mechanisms of resistance to BRAF-targeted therapy include:
- **Primary resistance** in ~50% of treatment-naïve patients (reported) (castellani2023brafmutationsin pages 11-12).
- **Acquired resistance** frequently via **MAPK reactivation** (~80% of BRAFi-resistant tumors) and/or **PI3K/AKT/mTOR** pathway activation (castellani2023brafmutationsin pages 11-12).
- Adaptive resistance via loss of ERK negative feedback leading to RTK upregulation (e.g., PDGFRβ, EGFR) (castellani2023brafmutationsin pages 11-12).
- **Phenotype switching** involving MITF-high melanocyte-like vs MITF-low mesenchymal invasive states (AXL/EGFR/TEAD programs; WNT5A/ROR2 axis) (castellani2023brafmutationsin pages 11-12).

### 5. Environmental Information
Primary environmental driver is UV radiation exposure (sunlight; indoor tanning), with UVA/UVB causing DNA damage, oxidative stress, inflammation, and immunosuppression (castellani2023brafmutationsin pages 1-2, manganelli2025skinphotodamageand pages 1-2). No infectious etiology is indicated in the retrieved sources.

### 6. Mechanism / Pathophysiology
**Causal chain (simplified):** UV-induced DNA damage and mutagenesis in melanocytes + acquisition of activating BRAFV600 mutation → constitutive MAPK/ERK signaling → melanocyte proliferation/survival and tumor initiation (often as nevi) → additional cooperating alterations (e.g., PTEN loss, TERT promoter) enable escape from senescence and progression → invasion/metastasis and microenvironmental remodeling → therapy response followed by adaptive/acquired resistance (MAPK reactivation, phenotype switching, RTK/PI3K bypass, autophagy) (castellani2023brafmutationsin pages 4-6, pelosi2024brafmutantmelanomasbiology pages 2-4, castellani2023brafmutationsin pages 11-12).

**Immune involvement.** The tumor microenvironment contributes to resistance via stromal and immune components; CAF and immune remodeling are emphasized in resistance reviews (florent2023brafv600mutatedmetastatic pages 1-2). The early immune-modulating effects of oncogenic BRAF (e.g., Treg recruitment) are also supported by retrieved experimental literature (shang2026brafinhibitorresistance pages 2-3).

### 7. Anatomical Structures Affected
- **Primary:** skin (cutaneous melanoma; melanocytes in epidermal basal layer) (belloni2025treatmentrelatedadverseevents pages 1-2, saeed2024cutaneousoncologystrategies pages 1-2).
- **Regional spread:** lymph nodes (stage III) and lymphatic drainage, with EV-based detection in exudative seroma after lymphadenectomy (garciasilva2019useofextracellular pages 1-2).
- **Distant metastases:** brain is a common metastatic site (brain metastases in ~40–50% of cutaneous melanoma patients) (ascierto2024sequencingofcheckpoint pages 1-2).

**Suggested UBERON terms (examples).**
- Skin: **UBERON:0002097**
- Lymph node: **UBERON:0000029**
- Brain: **UBERON:0000955**

### 8. Temporal Development
- **Onset:** melanoma median age at diagnosis reported as ~57 years in an advanced melanoma treatment review (mohr2025updateonthe pages 2-2).
- **Progression:** stage IV disease historically had poor survival (reported 6–12 months historically; improved with modern therapies) (finke2024brafv600emetastaticmelanoma pages 1-2).

### 9. Inheritance and Population
BRAF V600–mutant melanoma is predominantly **somatic**. Hereditary melanoma (~10% of cases) is reported to lack BRAF mutations, implying BRAF V600 melanomas are primarily sporadic (castellani2023brafmutationsin pages 2-4).

**Burden statistics.** Global Cancer Observatory (GCO) 2022: 331,647 new melanoma cases and 58,645 deaths (imani2024theevolutionof pages 1-2). A 2025 meta-analysis summary cites similar 2022 global estimates and projects ~510,000 new cases and ~96,000 deaths by 2040 (belloni2025treatmentrelatedadverseevents pages 1-2).

**Survival statistics (general melanoma).** Europe-wide 5-year survival is cited at ~85% (mohr2025updateonthe pages 2-2). A melanoma screening review reports 5-year survival in most European countries is 80–90% with country-level variation (czerw2024newscreeningmethods pages 2-3).

### 10. Diagnostics
**Histopathology/biopsy.** The SEOM-GEM guideline states suspicious lesions should be confirmed by excisional biopsy and staged per AJCC (marquezrodas2024seomgemclinicalguidelines pages 1-2).

**IHC markers for melanoma.** Recommended markers include **S-100, SOX10, HMB-45, PRAME, MART-1** (marquezrodas2024seomgemclinicalguidelines pages 1-2).

**Molecular testing for BRAF.** SEOM-GEM: “Determination of BRAF V600 status is mandatory in patients with stage IV melanoma” (marquezrodas2024seomgemclinicalguidelines pages 1-2). In clinical trials and safety literature, BRAF V600 mutation detection has been performed using **PCR-based assays**, **NGS**, and **Sanger sequencing** (belloni2025treatmentrelatedadverseevents pages 7-8).

**Liquid biopsy / circulating biomarkers.** ctDNA (BRAF V600E) is described as prognostic and dynamic with treatment, and can detect emergent resistance mutations (NRAS, MAP2K1, AKT1, PIK3CA) (castellani2023brafmutationsin pages 17-18). Extracellular vesicle DNA from lymphatic drainage (exudative seroma) can detect BRAFV600E and was reported to correlate with relapse risk in stage III disease (garciasilva2019useofextracellular pages 1-2).

### 11. Outcome/Prognosis
**Metastatic sequencing outcomes (SECOMBIT).** 4-year OS differed by first-line sequencing: 46% (targeted→immunotherapy), 64% (immunotherapy→targeted), 59% (sandwich) (ascierto2024sequentialimmunotherapyand pages 1-2). Total PFS to second progression at 4 years was 29%, 55%, and 54% in Arms A/B/C, respectively (ascierto2024sequentialimmunotherapyand pages 1-2).

**Brain-metastasis outcomes (SECOMBIT analysis).** 60-month brain-metastases-free survival was 56% (targeted-first), 80% (immunotherapy-first; HR vs A 0.40), and 85% (sandwich; HR vs A 0.35) (ascierto2024sequencingofcheckpoint pages 1-2).

### 12. Treatment
#### 12.1 Targeted therapy (BRAF/MEK inhibitors)
Approved combinations are widely used in advanced disease; guideline notes include vemurafenib+cobimetinib, dabrafenib+trametinib, and encorafenib+binimetinib (marquezrodas2024seomgemclinicalguidelines pages 4-5).

**Adjuvant (stage III).** SEOM-GEM notes COMBI-AD supports 1 year dabrafenib+trametinib as a standard adjuvant option for completely resected stage III BRAF-mutated melanoma (marquezrodas2024seomgemclinicalguidelines pages 4-5). In a large multicenter retrospective cohort (n=598), adjuvant dabrafenib+trametinib had longer RFS than adjuvant anti–PD-1 monotherapy: median RFS 51.0 vs 44.8 months; multivariable HR 0.58 (P=0.007); OS similar (multivariable HR 0.90) (bai2023dabrafenibplustrametinib pages 1-2).

**MAXO suggestions (examples).**
- BRAF inhibitor therapy; MEK inhibitor therapy; combination targeted therapy (MAXO mapping not directly retrieved; recommended as action ontology entries).

#### 12.2 Immunotherapy and sequencing (metastatic)
SECOMBIT provides prospective evidence supporting immunotherapy-first (ipilimumab+nivolumab) as preferred first-line sequencing for many patients with BRAF V600–mutant metastatic melanoma (ascierto2024sequentialimmunotherapyand pages 1-2). The NEJM Evidence analysis further supports immunotherapy-first or sandwich sequences for reducing brain metastasis risk (ascierto2024sequencingofcheckpoint pages 1-2).

#### 12.3 Neoadjuvant (resectable stage III)
NeoTrio tested pembrolizumab alone vs addition of dabrafenib+trametinib sequentially or concurrently.
- **Abstract quote:** “The pathological response rate was 55% (11/20; including six pathological complete responses (pCRs)) with pembrolizumab, 50% (10/20; three pCRs) with sequential therapy and 80% (16/20; ten pCRs) with concurrent therapy…” (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2).
- **2-year outcomes:** event-free survival 60%, 80%, 71% (pembro, sequential, concurrent) (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2).
- **Safety quote:** “Treatment-related adverse events affected 75–100% of patients during neoadjuvant treatment, with seven early discontinuations (all in the concurrent arm).” (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2).

**Visual evidence (NeoTrio survival curves).** Kaplan–Meier curves and 12-/24-month landmark rates for EFS/RFS/OS are shown in Figure 2 (long2024neoadjuvantpembrolizumabdabrafenib media 7989da9e).

#### 12.4 Adverse events (real-world relevance)
Pooled prevalence estimates: vemurafenib-associated arthralgia 44% and rash 39%; dabrafenib+trametinib-associated fatigue 47% and pyrexia 40% (belloni2025treatmentrelatedadverseevents pages 1-2).

### 13. Prevention
**Primary prevention.** UVR is the principal modifiable driver; a recent comprehensive photodamage review states UVR is the leading environmental factor and accounts for an estimated 60–70% of cutaneous melanoma cases (manganelli2025skinphotodamageand pages 1-2).

**Secondary prevention/high-risk surveillance.** A systematic review of interventions to increase skin self-examination (SSE) in high-risk individuals found low-certainty evidence that interventions improve SSE practice; no evidence of effects on melanoma mortality was identified (gooley2025clinicaleffectivenessof pages 1-2). A 2024 management review emphasizes lifelong regular skin checks and considering total-body photography in patients with many nevi (dixon2024primarycutaneousmelanoma—management pages 1-2).

### 14. Other Species / Natural Disease
No robust, BRAF V600–specific naturally occurring veterinary melanoma evidence was retrieved in this run; thus, cross-species “natural disease” mapping is incomplete.

### 15. Model Organisms
**Murine models.** A widely used inducible genetic model combines melanocyte-specific BRAFV600E with PTEN loss (Tyr::CreERT2; BrafV600E; Ptenfl/fl) for preclinical testing of targeted therapy and immunotherapy combinations (hooijkaas2012targetingbrafv600ein pages 1-2).

**Zebrafish models.** Zebrafish are used to model melanoma initiation, metastasis, remission, and relapse due to conserved pathways and optical accessibility (frantz2020fromtankto pages 1-3). Transgenic BRAFV600E zebrafish models show that BRAFV600E alone can generate nevi and needs cooperating lesions for melanoma, paralleling human biology (frantz2020fromtankto pages 1-3).

### Expert opinions / guideline perspectives (authoritative sources)
- SEOM-GEM guideline positions BRAF testing as mandatory in stage IV and provides evidence-based recommendations for adjuvant targeted therapy and systemic therapy selection, with explicit levels of evidence/grades (marquezrodas2024seomgemclinicalguidelines pages 1-2, marquezrodas2024seomgemclinicalguidelines pages 4-5).
- SECOMBIT authors conclude their long-term data “confirm immunotherapy as the preferred first-line treatment approach for most patients with BRAFV600-mutant metastatic melanoma” (ascierto2024sequentialimmunotherapyand pages 1-2).

### Notes on evidence gaps in this run
- MONDO identifier and ICD-11 codes were not located in the retrieved texts.
- Many primary statements here are supported by DOIs/URLs rather than PMIDs because PubMed identifiers were not present in the retrieved excerpts.

| Study | Setting | Population | Interventions / arms | Key efficacy results with numbers | Key safety notes | Publication date | URL / DOI |
|---|---|---|---|---|---|---|---|
| SECOMBIT (Nature Communications 2024) | Metastatic, first-line sequencing | Untreated metastatic BRAFV600-mutant melanoma; 209 randomized, 206 treated across 37 sites in 9 countries (ascierto2024sequentialimmunotherapyand pages 1-2) | Arm A: encorafenib + binimetinib until PD → ipilimumab + nivolumab; Arm B: ipilimumab + nivolumab until PD → encorafenib + binimetinib; Arm C: 8-week encorafenib + binimetinib induction → ipilimumab + nivolumab (“sandwich”) (ascierto2024sequentialimmunotherapyand pages 1-2) | 4-year OS: 46% Arm A, 64% Arm B, 59% Arm C; 4-year TPFS: 29% Arm A, 55% Arm B, 54% Arm C. Authors concluded long-term benefit with first-line immunotherapy and exploratory biomarker trends for deleterious JAK mutations / low baseline IFNγ (ascierto2024sequentialimmunotherapyand pages 1-2, ascierto2024sequentialimmunotherapyand pages 4-6) | During treatment, deaths: 13 in Arm A, 11 in Arm B, 4 in Arm C; adverse events led to treatment discontinuation in 11, 10, and 11 patients in Arms A, B, and C, respectively (ascierto2024sequentialimmunotherapyand pages 1-2) | 2 Jan 2024 | https://doi.org/10.1038/s41467-023-44475-6 |
| SECOMBIT brain metastases-free survival analysis (NEJM Evidence 2024) | Metastatic sequencing; brain metastasis prevention analysis | Unresectable metastatic BRAFV600-mutant melanoma without brain metastases at baseline; 206 treated patients from SECOMBIT (ascierto2024sequencingofcheckpoint pages 1-2, ascierto2024sequencingofcheckpoint pages 2-3) | Same 3-arm SECOMBIT design: targeted→immuno, immuno→targeted, and short targeted induction→immuno→targeted (ascierto2024sequencingofcheckpoint pages 1-2) | New brain metastases: 23/69 Arm A, 11/69 Arm B, 9/68 Arm C. 60-month BMFS: 56% Arm A, 80% Arm B (HR vs A 0.40, 95% CI 0.23–0.58), 85% Arm C (HR vs A 0.35, 95% CI 0.16–0.76), favoring immunotherapy-first or sandwich approaches (ascierto2024sequencingofcheckpoint pages 1-2) | Safety details not the focus of this report excerpt; sequencing effect on brain metastasis-free survival was the principal finding (ascierto2024sequencingofcheckpoint pages 1-2) | 24 Sep 2024 | https://doi.org/10.1056/evidoa2400087 |
| NeoTrio (Nature Medicine 2024) | Neoadjuvant / perioperative | Resectable stage III BRAFV600-mutant melanoma; 60 patients randomized, 42% female; 82% V600E, 15% V600K, 3% V600R (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2) | Pembrolizumab alone (n=20); sequential dabrafenib + trametinib then pembrolizumab (n=20); concurrent pembrolizumab + dabrafenib + trametinib (n=20), followed by surgery and adjuvant therapy (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2) | Pathological response: 55% (11/20; 6 pCRs) pembrolizumab, 50% (10/20; 3 pCRs) sequential, 80% (16/20; 10 pCRs) concurrent. 24-month EFS: 60%, 80%, 71%; 24-month RFS: 66%, 80%, 75%; 24-month OS: 76%, 89%, 95% for pembrolizumab, sequential, and concurrent arms, respectively (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2, long2024neoadjuvantpembrolizumabdabrafenib pages 5-7, long2024neoadjuvantpembrolizumabdabrafenib media 7989da9e) | Neoadjuvant TRAEs affected 75–100% of patients; 9/60 discontinued early due to neoadjuvant TRAEs, including 8/20 in the concurrent arm; seven early discontinuations during neoadjuvant treatment were all in concurrent arm in abstract summary (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2) | 21 Jun 2024 | https://doi.org/10.1038/s41591-024-03077-5 |
| Real-world adjuvant D/T vs anti–PD-1 (eClinicalMedicine 2023) | Adjuvant | Resected stage III BRAF V600-mutant melanoma; 598 patients from 15 melanoma centers; D/T n=393, PD-1 n=205 (bai2023dabrafenibplustrametinib pages 1-2) | Adjuvant dabrafenib + trametinib vs adjuvant anti–PD-1 monotherapy after definitive surgery (bai2023dabrafenibplustrametinib pages 1-2) | Median follow-up 33 months. Median RFS: 51.0 months for D/T vs 44.8 months for PD-1; univariate HR 0.66 (95% CI 0.50–0.87; P=0.003), multivariate HR 0.58 (95% CI 0.39–0.86; P=0.007). OS comparable: multivariate HR 0.90 (95% CI 0.48–1.70; P=0.75). Among recurrences, distant metastases were more frequent with D/T (72% vs 58%) (bai2023dabrafenibplustrametinib pages 1-2, bai2023dabrafenibplustrametinib pages 5-6) | D/T had higher incidence of treatment modification due to adverse events but fewer persistent adverse events than PD-1 (bai2023dabrafenibplustrametinib pages 1-2) | Nov 2023 | https://doi.org/10.1016/j.eclinm.2023.102290 |
| BRAF/MEK inhibitor AE meta-analysis (Cancers 2025) | Treatment safety across advanced/unresectable disease | Adults with BRAF-mutant cutaneous melanoma, predominantly unresectable locally advanced or metastatic stage IIIC–IV across included trials (belloni2025treatmentrelatedadverseevents pages 7-8, belloni2025treatmentrelatedadverseevents pages 1-2) | Review/meta-analysis of approved BRAF/MEK regimens; pooled analysis feasible for vemurafenib monotherapy and dabrafenib + trametinib (belloni2025treatmentrelatedadverseevents pages 1-2) | Safety-focused study; no pooled OS/PFS efficacy endpoint reported in excerpt. Quantitative toxicity findings: vemurafenib musculoskeletal/connective-tissue disorders 24% (95% CI 6–41%), arthralgia 44% (95% CI 29–59%), rash 39% (95% CI 22–56%); dabrafenib + trametinib constitutional toxicities 25% (95% CI 14–37%), fatigue 47% (95% CI 38–56%), pyrexia 40% (95% CI 26–54%) (belloni2025treatmentrelatedadverseevents pages 1-2) | Grade ≥3 cutaneous AEs with vemurafenib included squamous cell carcinoma and keratoacanthoma; regimen-specific toxicity profiles emphasized for personalized care (belloni2025treatmentrelatedadverseevents pages 1-2) | Sep 2025 | https://doi.org/10.3390/cancers17193152 |


*Table: This table summarizes major 2023–2024 clinical evidence and one recent safety meta-analysis relevant to BRAF V600-mutant melanoma across metastatic, adjuvant, and neoadjuvant settings. It highlights study design, populations, key efficacy numbers, and the main safety signals useful for comparative interpretation.*

References

1. (marquezrodas2024seomgemclinicalguidelines pages 1-2): Iván Márquez-Rodas, Eva Muñoz Couselo, Juan F. Rodríguez Moreno, Ana Mª Arance Fernández, Miguel Ángel Berciano Guerrero, Begoña Campos Balea, Luis de la Cruz Merino, Enrique Espinosa Arranz, Almudena García Castaño, and Alfonso Berrocal Jaime. Seom-gem clinical guidelines for cutaneous melanoma (2023). Clinical & Translational Oncology, 26:2841-2855, May 2024. URL: https://doi.org/10.1007/s12094-024-03497-2, doi:10.1007/s12094-024-03497-2. This article has 8 citations and is from a peer-reviewed journal.

2. (castellani2023brafmutationsin pages 1-2): Giorgia Castellani, Mariachiara Buccarelli, Maria Beatrice Arasi, Stefania Rossi, Maria Elena Pisanu, Maria Bellenghi, Carla Lintas, and Claudio Tabolacci. Braf mutations in melanoma: biological aspects, therapeutic implications, and circulating biomarkers. Cancers, 15:4026, Aug 2023. URL: https://doi.org/10.3390/cancers15164026, doi:10.3390/cancers15164026. This article has 206 citations.

3. (NCT02036086 chunk 2):  Study of Neo-adjuvant Use of Vemurafenib Plus Cobimetinib for BRAF Mutant Melanoma With Palpable Lymph Node Metastases. Sunnybrook Health Sciences Centre. 2015. ClinicalTrials.gov Identifier: NCT02036086

4. (hoejberg2016trendsinmelanoma pages 1-3): Lise Hoejberg, Dorte Gad, Niels Gyldenkerne, and Lars Bastholt. Trends in melanoma in the elderly in denmark, 1980–2012. Acta Oncologica, 55:52-58, Jan 2016. URL: https://doi.org/10.3109/0284186x.2015.1114677, doi:10.3109/0284186x.2015.1114677. This article has 14 citations and is from a peer-reviewed journal.

5. (ghate2018healthcareresourceutilization pages 1-5): Sameer R. Ghate, Raluca Ionescu-Ittu, Rebecca Burne, Briana Ndife, François Laliberté, Antonio Nakasato, and Mei Sheng Duh. Healthcare resource utilization in patients with metastatic melanoma receiving first-line therapy with dabrafenib + trametinib versus nivolumab or pembrolizumab monotherapy. Current Medical Research and Opinion, 34:2169-2176, Aug 2018. URL: https://doi.org/10.1080/03007995.2018.1501351, doi:10.1080/03007995.2018.1501351. This article has 10 citations and is from a peer-reviewed journal.

6. (dixon2024primarycutaneousmelanoma—management pages 1-2): Anthony Joseph Dixon, Michael Sladden, Christos C. Zouboulis, Catalin M. Popescu, Alexander Nirenberg, Howard K. Steinman, Caterina Longo, Zoe Lee Dixon, and Joseph Meirion Thomas. Primary cutaneous melanoma—management in 2024. Journal of Clinical Medicine, 13:1607, Mar 2024. URL: https://doi.org/10.3390/jcm13061607, doi:10.3390/jcm13061607. This article has 26 citations.

7. (dummer2026exploratoryanalysisof pages 20-21): Reinhard Dummer, Shibing Deng, Tao Xie, Nuzhat Pathan, Hedieh Saffari, Caroline Robert, Ana Arance, Jan Willem B. de Groot, Claus Garbe, Helen J. Gogas, Ralf Gutzmer, Ivana Krajsová, Gabriella Liszkay, Carmen Loquai, Mario Mandala, Dirk Schadendorf, Naoya Yamazaki, Paolo A. Ascierto, Craig B. Davis, Khyati Shah, Phineas Hamilton, Alessandra di Pietro, and Keith Flaherty. Exploratory analysis of biomarkers and treatment outcomes from the columbus study in braf v600e/k–mutant advanced or metastatic melanoma. Clinical Cancer Research, 32:1266-1276, Jan 2026. URL: https://doi.org/10.1158/1078-0432.ccr-25-3262, doi:10.1158/1078-0432.ccr-25-3262. This article has 0 citations and is from a highest quality peer-reviewed journal.

8. (belloni2025treatmentrelatedadverseevents pages 1-2): Silvia Belloni, Rosamaria Virgili, Rosario Caruso, Cristina Arrigoni, Arianna Magon, Gennaro Rocco, and Maddalena De Maria. Treatment-related adverse events in individuals with braf-mutant cutaneous melanoma treated with braf and mek inhibitors: a systematic review and meta-analysis. Cancers, 17:3152, Sep 2025. URL: https://doi.org/10.3390/cancers17193152, doi:10.3390/cancers17193152. This article has 0 citations.

9. (frantz2020fromtankto pages 1-3): William Tyler Frantz and Craig J Ceol. From tank to treatment: modeling melanoma in zebrafish. Cells, 9:1289, May 2020. URL: https://doi.org/10.3390/cells9051289, doi:10.3390/cells9051289. This article has 41 citations.

10. (castellani2023brafmutationsin pages 2-4): Giorgia Castellani, Mariachiara Buccarelli, Maria Beatrice Arasi, Stefania Rossi, Maria Elena Pisanu, Maria Bellenghi, Carla Lintas, and Claudio Tabolacci. Braf mutations in melanoma: biological aspects, therapeutic implications, and circulating biomarkers. Cancers, 15:4026, Aug 2023. URL: https://doi.org/10.3390/cancers15164026, doi:10.3390/cancers15164026. This article has 206 citations.

11. (mohr2025updateonthe pages 2-3): Peter Mohr, Inès Nakouri, Sylvie Pfersch, François Denjean, and Celeste Lebbé. Update on the treatment of brafmut metastatic melanoma and future perspectives. JEADV Clinical Practice, Oct 2025. URL: https://doi.org/10.1002/jvc2.544, doi:10.1002/jvc2.544. This article has 0 citations and is from a peer-reviewed journal.

12. (bai2023dabrafenibplustrametinib pages 1-2): Xue Bai, Ahmed Shaheen, Charlotte Grieco, Paolo D. d’Arienzo, Florentia Mina, Juliane A. Czapla, Aleigha R. Lawless, Eleonora Bongiovanni, Umberto Santaniello, Helena Zappi, Dominika Dulak, Andrew Williamson, Rebecca Lee, Avinash Gupta, Caili Li, Lu Si, Martina Ubaldi, Naoya Yamazaki, Dai Ogata, Rebecca Johnson, Benjamin C. Park, Seungyeon Jung, Gabriele Madonna, Juliane Hochherz, Yoshiyasu Umeda, Yasuhiro Nakamura, Christoffer Gebhardt, Lucia Festino, Mariaelena Capone, Paolo Antonio Ascierto, Douglas B. Johnson, Serigne N. Lo, Georgina V. Long, Alexander M. Menzies, Kenjiro Namikawa, Mario Mandala, Jun Guo, Paul Lorigan, Yana G. Najjar, Andrew Haydon, Pietro Quaglino, Genevieve M. Boland, Ryan J. Sullivan, Andrew J.S. Furness, Ruth Plummer, and Keith T. Flaherty. Dabrafenib plus trametinib versus anti-pd-1 monotherapy as adjuvant therapy in braf v600-mutant stage iii melanoma after definitive surgery: a multicenter, retrospective cohort study. eClinicalMedicine, 65:102290, Nov 2023. URL: https://doi.org/10.1016/j.eclinm.2023.102290, doi:10.1016/j.eclinm.2023.102290. This article has 32 citations and is from a peer-reviewed journal.

13. (ascierto2024sequentialimmunotherapyand pages 1-2): Paolo A. Ascierto, Milena Casula, Jenny Bulgarelli, Marina Pisano, Claudia Piccinini, Luisa Piccin, Antonio Cossu, Mario Mandalà, Pier Francesco Ferrucci, Massimo Guidoboni, Piotr Rutkowski, Virginia Ferraresi, Ana Arance, Michele Guida, Evaristo Maiello, Helen Gogas, Erika Richtig, Maria Teresa Fierro, Celeste Lebbe, Hildur Helgadottir, Paola Queirolo, Francesco Spagnolo, Marco Tucci, Michele Del Vecchio, Maria Gonzales Cao, Alessandro Marco Minisini, Sabino De Placido, Miguel F. Sanmamed, Domenico Mallardo, Miriam Paone, Maria Grazia Vitale, Ignacio Melero, Antonio M. Grimaldi, Diana Giannarelli, Reinhard Dummer, Vanna Chiarion Sileni, and Giuseppe Palmieri. Sequential immunotherapy and targeted therapy for metastatic braf v600 mutated melanoma: 4-year survival and biomarkers evaluation from the phase ii secombit trial. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44475-6, doi:10.1038/s41467-023-44475-6. This article has 99 citations and is from a highest quality peer-reviewed journal.

14. (florent2023brafv600mutatedmetastatic pages 1-2): Laetitia Florent, Charles Saby, Florian Slimano, and Hamid Morjani. Braf v600-mutated metastatic melanoma and targeted therapy resistance: an update of the current knowledge. Cancers, 15:2607, May 2023. URL: https://doi.org/10.3390/cancers15092607, doi:10.3390/cancers15092607. This article has 44 citations.

15. (mohr2025updateonthe pages 2-2): Peter Mohr, Inès Nakouri, Sylvie Pfersch, François Denjean, and Celeste Lebbé. Update on the treatment of brafmut metastatic melanoma and future perspectives. JEADV Clinical Practice, Oct 2025. URL: https://doi.org/10.1002/jvc2.544, doi:10.1002/jvc2.544. This article has 0 citations and is from a peer-reviewed journal.

16. (pelosi2024brafmutantmelanomasbiology pages 4-5): Elvira Pelosi, Germana Castelli, and Ugo Testa. Braf-mutant melanomas: biology and therapy. Current Oncology, 31:7711-7737, Dec 2024. URL: https://doi.org/10.3390/curroncol31120568, doi:10.3390/curroncol31120568. This article has 12 citations.

17. (pelosi2024brafmutantmelanomasbiology pages 2-4): Elvira Pelosi, Germana Castelli, and Ugo Testa. Braf-mutant melanomas: biology and therapy. Current Oncology, 31:7711-7737, Dec 2024. URL: https://doi.org/10.3390/curroncol31120568, doi:10.3390/curroncol31120568. This article has 12 citations.

18. (manganelli2025skinphotodamageand pages 1-2): Michele Manganelli, Giorgio Stabile, Camila Scharf, Antonio Podo Brunetti, Giovanni Paolino, Roberta Giuffrida, Gianmarco Diego Bigotto, Giuseppe Damiano, Santo Raffaele Mercuri, Fabio Sallustio, Eleonora Mangano, Roberta Bordoni, Paola De Nardi, Gabriella Guida, Caterina Foti, Giuseppe Argenziano, Caterina Longo, Giovanni Pellacani, Nathalie Rizzo, Vincenzo Russo, Stefania Guida, and Franco Rongioletti. Skin photodamage and melanomagenesis: a comprehensive review. Cancers, 17:1784, May 2025. URL: https://doi.org/10.3390/cancers17111784, doi:10.3390/cancers17111784. This article has 15 citations.

19. (castellani2023brafmutationsin pages 4-6): Giorgia Castellani, Mariachiara Buccarelli, Maria Beatrice Arasi, Stefania Rossi, Maria Elena Pisanu, Maria Bellenghi, Carla Lintas, and Claudio Tabolacci. Braf mutations in melanoma: biological aspects, therapeutic implications, and circulating biomarkers. Cancers, 15:4026, Aug 2023. URL: https://doi.org/10.3390/cancers15164026, doi:10.3390/cancers15164026. This article has 206 citations.

20. (pelosi2024brafmutantmelanomasbiology pages 1-2): Elvira Pelosi, Germana Castelli, and Ugo Testa. Braf-mutant melanomas: biology and therapy. Current Oncology, 31:7711-7737, Dec 2024. URL: https://doi.org/10.3390/curroncol31120568, doi:10.3390/curroncol31120568. This article has 12 citations.

21. (ascierto2024sequencingofcheckpoint pages 1-2): Paolo A. Ascierto, Mario Mandalà, Pier Francesco Ferrucci, Massimo Guidoboni, Piotr Rutkowski, Virginia Ferraresi, Ana Arance, Michele Guida, Evaristo Maiello, Helen Gogas, Erika Richtig, Pietro Quaglino, Céleste Lebbé, Hildur Helgadottir, Paola Queirolo, Francesco Spagnolo, Marco Tucci, Michele Del Vecchio, Maria Gonzalez-Cao, Alessandro Marco Minisini, Sabino De Placido, Miguel F. Sanmamed, Milena Casula, Jenny Bulgarelli, Marina Pisano, Claudia Piccinini, Luisa Piccin, Antonio Cossu, Domenico Mallardo, Miriam Paone, Maria Grazia Vitale, Ignacio Melero, Antonio M. Grimaldi, Diana Giannarelli, Giuseppe Palmieri, Reinhard Dummer, and Vanna Chiarion Sileni. Sequencing of checkpoint or braf/mek inhibitors on brain metastases in melanoma. NEJM evidence, 3 10:EVIDoa2400087, Sep 2024. URL: https://doi.org/10.1056/evidoa2400087, doi:10.1056/evidoa2400087. This article has 12 citations and is from a peer-reviewed journal.

22. (finke2024brafv600emetastaticmelanoma pages 1-2): Carsten Finke and Peter Mohr. Brafv600e metastatic melanoma journey: a perspective from a patient and his oncologist. Advances in Therapy, 41:2576-2585, May 2024. URL: https://doi.org/10.1007/s12325-024-02883-0, doi:10.1007/s12325-024-02883-0. This article has 2 citations and is from a peer-reviewed journal.

23. (shang2026brafinhibitorresistance pages 2-3): Yan Shang, Tingping Cao, Junyan Li, Juan Li, Lingnan Zhang, Qiqi Ma, Lanyan Feng, and Hailong Zhao. Braf inhibitor resistance in melanoma: from resistance mechanisms to therapeutic innovations. Molecular Biomedicine, Mar 2026. URL: https://doi.org/10.1186/s43556-026-00425-4, doi:10.1186/s43556-026-00425-4. This article has 0 citations and is from a peer-reviewed journal.

24. (cosci2025molecularbasisof pages 2-4): Ilaria Cosci, Valentina Salizzato, Paolo Del Fiore, Jacopo Pigozzo, Valentina Guarneri, Simone Mocellin, Alberto Ferlin, Sara Mathlouthi, Luisa Piccin, and Mariangela Garofalo. Molecular basis of braf inhibitor resistance in melanoma: a systematic review. Pharmaceuticals, 18:1235, Aug 2025. URL: https://doi.org/10.3390/ph18081235, doi:10.3390/ph18081235. This article has 10 citations.

25. (castellani2023brafmutationsin pages 11-12): Giorgia Castellani, Mariachiara Buccarelli, Maria Beatrice Arasi, Stefania Rossi, Maria Elena Pisanu, Maria Bellenghi, Carla Lintas, and Claudio Tabolacci. Braf mutations in melanoma: biological aspects, therapeutic implications, and circulating biomarkers. Cancers, 15:4026, Aug 2023. URL: https://doi.org/10.3390/cancers15164026, doi:10.3390/cancers15164026. This article has 206 citations.

26. (saeed2024cutaneousoncologystrategies pages 1-2): Wajeeha Saeed, Esha Shahbaz, Quratulain Maqsood, Shinawar Waseem Ali, and Muhammada Mahnoor. Cutaneous oncology: strategies for melanoma prevention, diagnosis, and therapy. Cancer Control : Journal of the Moffitt Cancer Center, Jan 2024. URL: https://doi.org/10.1177/10732748241274978, doi:10.1177/10732748241274978. This article has 21 citations.

27. (garciasilva2019useofextracellular pages 1-2): Susana García-Silva, Alberto Benito-Martín, Sara Sánchez-Redondo, Alberto Hernández-Barranco, Pilar Ximénez-Embún, Laura Nogués, Marina S. Mazariegos, Kay Brinkmann, Ana Amor López, Lisa Meyer, Carlos Rodríguez, Carmen García-Martín, Jasminka Boskovic, Rocío Letón, Cristina Montero, Mercedes Robledo, Laura Santambrogio, Mary Sue Brady, Anna Szumera-Ciećkiewicz, Iwona Kalinowska, Johan Skog, Mikkel Noerholm, Javier Muñoz, Pablo L. Ortiz-Romero, Yolanda Ruano, José L. Rodríguez-Peralto, Piotr Rutkowski, and Héctor Peinado. Use of extracellular vesicles from lymphatic drainage as surrogate markers of melanoma progression and brafv600e mutation. The Journal of Experimental Medicine, 216:1061-1070, Apr 2019. URL: https://doi.org/10.1084/jem.20181522, doi:10.1084/jem.20181522. This article has 148 citations.

28. (imani2024theevolutionof pages 1-2): Saber Imani, Ghazaal Roozitalab, Mahdieh Emadi, Atefeh Moradi, Payam Behzadi, and Parham Jabbarzadeh Kaboli. The evolution of braf-targeted therapies in melanoma: overcoming hurdles and unleashing novel strategies. Frontiers in Oncology, Nov 2024. URL: https://doi.org/10.3389/fonc.2024.1504142, doi:10.3389/fonc.2024.1504142. This article has 45 citations.

29. (czerw2024newscreeningmethods pages 2-3): Aleksandra Czerw, Andrzej Deptała, Olga Partyka, Monika Pajewska, Anna Badowska-Kozakiewicz, Michał Budzik, Katarzyna Sygit, Zygmunt Kopczyński, Piotr Czarnywojtek, Elżbieta Cipora, Magdalena Konieczny, Tomasz Banaś, Elżbieta Grochans, Szymon Grochans, Anna Maria Cybulska, Daria Schneider-Matyka, Ewa Bandurska, Weronika Ciećko, Jarosław Drobnik, Piotr Pobrotyn, Urszula Grata-Borkowska, Joanna Furtak-Pobrotyn, Aleksandra Sierocka, Michał Marczak, and Remigiusz Kozlowski. New screening methods in melanoma. Cancers, 16:4186, Dec 2024. URL: https://doi.org/10.3390/cancers16244186, doi:10.3390/cancers16244186. This article has 0 citations.

30. (belloni2025treatmentrelatedadverseevents pages 7-8): Silvia Belloni, Rosamaria Virgili, Rosario Caruso, Cristina Arrigoni, Arianna Magon, Gennaro Rocco, and Maddalena De Maria. Treatment-related adverse events in individuals with braf-mutant cutaneous melanoma treated with braf and mek inhibitors: a systematic review and meta-analysis. Cancers, 17:3152, Sep 2025. URL: https://doi.org/10.3390/cancers17193152, doi:10.3390/cancers17193152. This article has 0 citations.

31. (castellani2023brafmutationsin pages 17-18): Giorgia Castellani, Mariachiara Buccarelli, Maria Beatrice Arasi, Stefania Rossi, Maria Elena Pisanu, Maria Bellenghi, Carla Lintas, and Claudio Tabolacci. Braf mutations in melanoma: biological aspects, therapeutic implications, and circulating biomarkers. Cancers, 15:4026, Aug 2023. URL: https://doi.org/10.3390/cancers15164026, doi:10.3390/cancers15164026. This article has 206 citations.

32. (marquezrodas2024seomgemclinicalguidelines pages 4-5): Iván Márquez-Rodas, Eva Muñoz Couselo, Juan F. Rodríguez Moreno, Ana Mª Arance Fernández, Miguel Ángel Berciano Guerrero, Begoña Campos Balea, Luis de la Cruz Merino, Enrique Espinosa Arranz, Almudena García Castaño, and Alfonso Berrocal Jaime. Seom-gem clinical guidelines for cutaneous melanoma (2023). Clinical & Translational Oncology, 26:2841-2855, May 2024. URL: https://doi.org/10.1007/s12094-024-03497-2, doi:10.1007/s12094-024-03497-2. This article has 8 citations and is from a peer-reviewed journal.

33. (long2024neoadjuvantpembrolizumabdabrafenib pages 1-2): Georgina V. Long, Matteo S. Carlino, George Au-Yeung, Andrew J. Spillane, Kerwin F. Shannon, David E. Gyorki, Edward Hsiao, Rony Kapoor, Jake R. Thompson, Iris Batula, Julie Howle, Sydney Ch’ng, Maria Gonzalez, Robyn P. M. Saw, Thomas E. Pennington, Serigne N. Lo, Richard A. Scolyer, and Alexander M. Menzies. Neoadjuvant pembrolizumab, dabrafenib and trametinib in brafv600-mutant resectable melanoma: the randomized phase 2 neotrio trial. Nature Medicine, 30:2540-2548, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03077-5, doi:10.1038/s41591-024-03077-5. This article has 38 citations and is from a highest quality peer-reviewed journal.

34. (long2024neoadjuvantpembrolizumabdabrafenib media 7989da9e): Georgina V. Long, Matteo S. Carlino, George Au-Yeung, Andrew J. Spillane, Kerwin F. Shannon, David E. Gyorki, Edward Hsiao, Rony Kapoor, Jake R. Thompson, Iris Batula, Julie Howle, Sydney Ch’ng, Maria Gonzalez, Robyn P. M. Saw, Thomas E. Pennington, Serigne N. Lo, Richard A. Scolyer, and Alexander M. Menzies. Neoadjuvant pembrolizumab, dabrafenib and trametinib in brafv600-mutant resectable melanoma: the randomized phase 2 neotrio trial. Nature Medicine, 30:2540-2548, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03077-5, doi:10.1038/s41591-024-03077-5. This article has 38 citations and is from a highest quality peer-reviewed journal.

35. (gooley2025clinicaleffectivenessof pages 1-2): Kieran Gooley, Deonna Ackermann, Ellie Medcalf, and Katy Bell. Clinical effectiveness of interventions to increase self‐surveillance in people at high risk of melanoma: a systematic review. JEADV Clinical Practice, Jun 2025. URL: https://doi.org/10.1002/jvc2.70108, doi:10.1002/jvc2.70108. This article has 3 citations and is from a peer-reviewed journal.

36. (hooijkaas2012targetingbrafv600ein pages 1-2): Anna I. Hooijkaas, Jules Gadiot, Martin van der Valk, Wolter J. Mooi, and Christian U. Blank. Targeting brafv600e in an inducible murine model of melanoma. The American journal of pathology, 181 3:785-94, Sep 2012. URL: https://doi.org/10.1016/j.ajpath.2012.06.002, doi:10.1016/j.ajpath.2012.06.002. This article has 90 citations.

37. (ascierto2024sequentialimmunotherapyand pages 4-6): Paolo A. Ascierto, Milena Casula, Jenny Bulgarelli, Marina Pisano, Claudia Piccinini, Luisa Piccin, Antonio Cossu, Mario Mandalà, Pier Francesco Ferrucci, Massimo Guidoboni, Piotr Rutkowski, Virginia Ferraresi, Ana Arance, Michele Guida, Evaristo Maiello, Helen Gogas, Erika Richtig, Maria Teresa Fierro, Celeste Lebbe, Hildur Helgadottir, Paola Queirolo, Francesco Spagnolo, Marco Tucci, Michele Del Vecchio, Maria Gonzales Cao, Alessandro Marco Minisini, Sabino De Placido, Miguel F. Sanmamed, Domenico Mallardo, Miriam Paone, Maria Grazia Vitale, Ignacio Melero, Antonio M. Grimaldi, Diana Giannarelli, Reinhard Dummer, Vanna Chiarion Sileni, and Giuseppe Palmieri. Sequential immunotherapy and targeted therapy for metastatic braf v600 mutated melanoma: 4-year survival and biomarkers evaluation from the phase ii secombit trial. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44475-6, doi:10.1038/s41467-023-44475-6. This article has 99 citations and is from a highest quality peer-reviewed journal.

38. (ascierto2024sequencingofcheckpoint pages 2-3): Paolo A. Ascierto, Mario Mandalà, Pier Francesco Ferrucci, Massimo Guidoboni, Piotr Rutkowski, Virginia Ferraresi, Ana Arance, Michele Guida, Evaristo Maiello, Helen Gogas, Erika Richtig, Pietro Quaglino, Céleste Lebbé, Hildur Helgadottir, Paola Queirolo, Francesco Spagnolo, Marco Tucci, Michele Del Vecchio, Maria Gonzalez-Cao, Alessandro Marco Minisini, Sabino De Placido, Miguel F. Sanmamed, Milena Casula, Jenny Bulgarelli, Marina Pisano, Claudia Piccinini, Luisa Piccin, Antonio Cossu, Domenico Mallardo, Miriam Paone, Maria Grazia Vitale, Ignacio Melero, Antonio M. Grimaldi, Diana Giannarelli, Giuseppe Palmieri, Reinhard Dummer, and Vanna Chiarion Sileni. Sequencing of checkpoint or braf/mek inhibitors on brain metastases in melanoma. NEJM evidence, 3 10:EVIDoa2400087, Sep 2024. URL: https://doi.org/10.1056/evidoa2400087, doi:10.1056/evidoa2400087. This article has 12 citations and is from a peer-reviewed journal.

39. (long2024neoadjuvantpembrolizumabdabrafenib pages 5-7): Georgina V. Long, Matteo S. Carlino, George Au-Yeung, Andrew J. Spillane, Kerwin F. Shannon, David E. Gyorki, Edward Hsiao, Rony Kapoor, Jake R. Thompson, Iris Batula, Julie Howle, Sydney Ch’ng, Maria Gonzalez, Robyn P. M. Saw, Thomas E. Pennington, Serigne N. Lo, Richard A. Scolyer, and Alexander M. Menzies. Neoadjuvant pembrolizumab, dabrafenib and trametinib in brafv600-mutant resectable melanoma: the randomized phase 2 neotrio trial. Nature Medicine, 30:2540-2548, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03077-5, doi:10.1038/s41591-024-03077-5. This article has 38 citations and is from a highest quality peer-reviewed journal.

40. (bai2023dabrafenibplustrametinib pages 5-6): Xue Bai, Ahmed Shaheen, Charlotte Grieco, Paolo D. d’Arienzo, Florentia Mina, Juliane A. Czapla, Aleigha R. Lawless, Eleonora Bongiovanni, Umberto Santaniello, Helena Zappi, Dominika Dulak, Andrew Williamson, Rebecca Lee, Avinash Gupta, Caili Li, Lu Si, Martina Ubaldi, Naoya Yamazaki, Dai Ogata, Rebecca Johnson, Benjamin C. Park, Seungyeon Jung, Gabriele Madonna, Juliane Hochherz, Yoshiyasu Umeda, Yasuhiro Nakamura, Christoffer Gebhardt, Lucia Festino, Mariaelena Capone, Paolo Antonio Ascierto, Douglas B. Johnson, Serigne N. Lo, Georgina V. Long, Alexander M. Menzies, Kenjiro Namikawa, Mario Mandala, Jun Guo, Paul Lorigan, Yana G. Najjar, Andrew Haydon, Pietro Quaglino, Genevieve M. Boland, Ryan J. Sullivan, Andrew J.S. Furness, Ruth Plummer, and Keith T. Flaherty. Dabrafenib plus trametinib versus anti-pd-1 monotherapy as adjuvant therapy in braf v600-mutant stage iii melanoma after definitive surgery: a multicenter, retrospective cohort study. eClinicalMedicine, 65:102290, Nov 2023. URL: https://doi.org/10.1016/j.eclinm.2023.102290, doi:10.1016/j.eclinm.2023.102290. This article has 32 citations and is from a peer-reviewed journal.
