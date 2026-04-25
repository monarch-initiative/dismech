---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:13:59.087692'
end_time: '2026-04-24T18:27:25.066888'
duration_seconds: 805.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: X-linked Hypohidrotic Ectodermal Dysplasia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked Hypohidrotic Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **X-linked Hypohidrotic Ectodermal Dysplasia** covering all of the
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
- **Disease Name:** X-linked Hypohidrotic Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **X-linked Hypohidrotic Ectodermal Dysplasia** covering all of the
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


# X-linked Hypohidrotic Ectodermal Dysplasia (XLHED): Disease Characteristics Research Report

## Executive summary
X-linked hypohidrotic ectodermal dysplasia (XLHED) is a rare developmental genetic disorder classically defined by the triad of hypotrichosis, hypohidrosis/anhidrosis, and hypodontia/oligodontia, reflecting abnormal formation of ectodermal appendages (hair follicles, eccrine sweat glands, teeth) due to deficiency of ectodysplasin A1 (EDA1) signaling. (aftab2023xlinkedhypohidroticectodermal pages 1-2, callea2022extendedoverviewof pages 2-4)

A key 2024 advance is improved molecular diagnostic strategy evidence supporting phenotype-guided targeted sequencing (EDA/EDAR) for “classical triad” presentations and exome-scale testing for atypical cases, with copy-number variation (CNV) detection as an important contributor to missed diagnoses. (kim2024geneticprofilingand pages 1-2, kim2024geneticprofilingand pages 7-8)

A major translational development is prenatal protein replacement for affected male fetuses using intra-amniotic delivery of an EDA1 replacement (Fc-EDA/EDI200; and a next-generation molecule ER004), with human compassionate-use data showing sustained restoration of sweating and ongoing multicenter trials (EDELIFE, NCT04980638). (schneider2018prenatalcorrectionof pages 3-5, NCT04980638 chunk 1)

---

## 1. Disease information
### 1.1 Concise overview (current understanding)
XLHED is a genetic ectodermal dysplasia in which deficiency of ectodysplasin A (EDA/EDA1) signaling disrupts epithelial–mesenchymal interactions required for appendage development, producing reduced/absent sweat glands (heat intolerance, risk of hyperthermia), sparse hair, and missing/abnormal teeth; additional recurrent respiratory, skin, and ocular complications are common. (aftab2023xlinkedhypohidroticectodermal pages 1-2, fete2014x‐linkedhypohidroticectodermal pages 2-4)

**Abstract-supported definition (direct quote):** XLHED is “diagnosed by the triad of decreased sweating, reduced hair, and hypodontia.” (fete2014x‐linkedhypohidroticectodermal pages 1-2)

### 1.2 Key identifiers and synonyms
| Disease name | Common synonyms / alternative names | MONDO | OMIM/MIM disease # | Causal gene OMIM IDs | ICD-10 | MeSH mapping noted in ClinicalTrials.gov |
|---|---|---|---|---|---|---|
| X-linked hypohidrotic ectodermal dysplasia (XLHED) | Christ-Siemens-Touraine syndrome; X-linked HED; anhidrotic/hypohidrotic ectodermal dysplasia (aftab2023xlinkedhypohidroticectodermal pages 1-2, callea2022extendedoverviewof pages 2-4, fete2014x‐linkedhypohidroticectodermal pages 1-2) | MONDO:0010585 / MONDO_0010585 (NCT04980638 chunk 2) | MIM/OMIM: 305100 (nguyennielsen2013theprevalenceof pages 1-2, callea2022extendedoverviewof pages 2-4, schneider2018prenatalcorrectionof pages 1-2) | EDA: MIM 300451; EDAR: MIM 604095; EDARADD: MIM 606603 (nguyennielsen2013theprevalenceof pages 1-2, callea2022extendedoverviewof pages 2-4) | Q82.4 “Ectodermal Dysplasia (Anhidrotic)” used in Danish registry study for clinically diagnosed HED/XLHED ascertainment (nguyennielsen2013theprevalenceof pages 1-2, nguyennielsen2013theprevalenceof pages 2-3) | “Ectodermal Dysplasia 1, Anhidrotic” (MeSH D053358) in NCT04980638 / EDELIFE record (NCT04980638 chunk 2) |


*Table: This table compiles the main nomenclature and database identifiers for X-linked hypohidrotic ectodermal dysplasia, including disease and gene OMIM numbers, MONDO, ICD-10, and MeSH. It is useful for harmonizing disease records across clinical, ontology, and literature sources.*

**Evidence source type note:** identifiers are derived from aggregated disease resources (registry-based epidemiology and patient registries), and trial registries (ClinicalTrials.gov), rather than individual EHR-only sources. (nguyennielsen2013theprevalenceof pages 1-2, fete2014x‐linkedhypohidroticectodermal pages 1-2, NCT04980638 chunk 1)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** pathogenic loss-of-function variants in **EDA** (ectodysplasin A; EDA1 isoform) causing deficiency of EDA1 signaling, inherited in an X-linked manner in XLHED. (schneider2022ectodermaldysplasiasnew pages 1-2, nguyennielsen2013theprevalenceof pages 1-2)

**Related hypohidrotic ectodermal dysplasia genes (non-X-linked forms):** EDAR, EDARADD, WNT10A are frequently implicated in hypohidrotic ED broadly (with EDAR/EDARADD capable of dominant or recessive forms; WNT10A often recessive). (aftab2023xlinkedhypohidroticectodermal pages 1-2, kovalskaia2023molecularbasisand pages 1-2)

### 2.2 Risk factors
The principal risk factor is carriage of a pathogenic **EDA** variant in a family (X-linked inheritance), with males generally more severely affected and females showing variable expressivity. (aftab2023xlinkedhypohidroticectodermal pages 1-2, fete2014x‐linkedhypohidroticectodermal pages 2-4)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved primary sources.

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence (formal GxE) was not identified in the retrieved sources. Clinically, environmental heat exposure interacts with anhidrosis to precipitate hyperthermia risk (a clinically important interaction, though not studied as GxE). (schneider2018prenatalcorrectionof pages 1-2, nguyennielsen2013theprevalenceof pages 1-2)

---

## 3. Phenotypes
### 3.1 Core phenotypes, characteristics, and HPO mapping
Below are major phenotypes (symptoms/signs) with suggested HPO terms and evidence.

1) **Hypohidrosis/anhidrosis and heat intolerance**
- **Type:** clinical sign/functional deficit
- **Onset:** typically infancy/early childhood (early clinical recognition), though diagnosis may be delayed. (nguyennielsen2013theprevalenceof pages 1-2, aftab2023xlinkedhypohidroticectodermal pages 1-2)
- **Severity:** ranges from absent sweating to low residual sweating depending on genotype. (schneider2011sweatingabilityand pages 5-10)
- **Key complications:** life-threatening hyperthermia. (schneider2018prenatalcorrectionof pages 1-2)
- **Suggested HPO:** HP:0000973 (Anhidrosis), HP:0003214 (Hypohidrosis), HP:0002044 (Hyperthermia), HP:0004370 (Heat intolerance)
- **Quantitative biomarker data (sweat testing):** in controls, mean pilocarpine-stimulated sweat volume was **72 µL** (range 29–93 µL) and mean sweat pore density **455 pores/cm²** (294–900). In XLHED males, 14/31 had no pores/no inducible sweating; 7/31 produced **1–11 µL** (low sweating). (schneider2011sweatingabilityand pages 5-10, schneider2011sweatingabilityand pages 1-5)

2) **Hypodontia/oligodontia (abnormal or missing teeth)**
- **Type:** physical manifestation
- **Onset:** developmental (childhood; detection with tooth development)
- **Frequency (registry-reported):** hypodontia reported in **89% overall** of XLHED respondents in EDIR, and in 74% of male XLHED registrants in one registry analysis. (fete2014x‐linkedhypohidroticectodermal pages 1-2)
- **Suggested HPO:** HP:0000668 (Hypodontia), HP:0000674 (Oligodontia), HP:0006480 (Abnormality of dental morphology)

3) **Hypotrichosis / sparse scalp hair and eyebrows**
- **Type:** physical manifestation
- **Frequency (registry-reported):** reduced hair reported in **74% overall** in EDIR and **80%** of male XLHED registrants; in females, hair abnormalities still reported by the majority (63% in EDIR). (fete2014x‐linkedhypohidroticectodermal pages 1-2, fete2014x‐linkedhypohidroticectodermal pages 2-4)
- **Suggested HPO:** HP:0001006 (Hypotrichosis), HP:0000535 (Sparse eyebrow)

4) **Recurrent respiratory/nasal complications**
- **Type:** symptoms/clinical signs
- **Frequency (international patient registry, males):** foul-smelling nasal discharge **67%**, infections requiring antibiotics **52%**, recurrent pneumonias **19%**, wheeze **66%**, recurrent sinusitis **49%**, raspy/hoarse voice **67%**. (fete2014x‐linkedhypohidroticectodermal pages 2-4)
- **Suggested HPO:** HP:0002789 (Recurrent respiratory infections), HP:0001742 (Chronic sinusitis), HP:0002099 (Wheezing), HP:0001609 (Hoarse voice), HP:0011950 (Nasal discharge)

5) **Eczema / dry skin**
- **Type:** clinical sign
- **Frequency (EDIR):** eczema reported in **66% males** and **40% females** in registry summary excerpt. (fete2014x‐linkedhypohidroticectodermal pages 1-2)
- **Suggested HPO:** HP:0000964 (Eczema), HP:0000958 (Dry skin)

6) **Ocular surface disease / dry eye**
- **Type:** symptom/clinical sign
- **Frequency:** “nearly one-third” affected with ocular dry eye in registry excerpt. (fete2014x‐linkedhypohidroticectodermal pages 2-4)
- **Suggested HPO:** HP:0001097 (Dry eye), HP:0000508 (Photophobia) (frequently associated per ocular review context) (callea2022extendedoverviewof pages 2-4)

### 3.2 Quality-of-life impact
Quality of life is substantially impacted through heat avoidance/thermoregulation constraints, need for long-term dental rehabilitation, recurrent ENT/respiratory issues, and ocular surface disease requiring surveillance and ongoing supportive care. (aftab2023xlinkedhypohidroticectodermal pages 8-9, callea2022extendedoverviewof pages 2-4, fete2014x‐linkedhypohidroticectodermal pages 2-4)

---

## 4. Genetic / molecular information
### 4.1 Causal genes
- **EDA** (ectodysplasin A; EDA1 isoform critical): primary XLHED gene. (schneider2022ectodermaldysplasiasnew pages 1-2, nguyennielsen2013theprevalenceof pages 1-2)
- **EDAR / EDARADD**: receptors/adaptors in the same pathway; typically relevant to non-X-linked hypohidrotic ED, but central mechanistically. (callea2022extendedoverviewof pages 2-4)

### 4.2 Pathogenic variants and functional consequences
**Variant classes:** deletions, nonsense, frameshift, splice-site, and missense variants affecting key functional domains (furin cleavage site, TNF homology domain, collagen-like repeats) correlate with absent versus residual sweating. (schneider2011sweatingabilityand pages 5-10)

**Genotype–phenotype mapping (example evidence):** missense variants disrupting the furin recognition site (R153C/R155C/R156H) and certain TNF-domain mutations (e.g., Y304C) are linked to anhidrosis, whereas some variants (e.g., V262F, R276C, G299R, R69L) can be associated with residual sweating. (schneider2011sweatingabilityand pages 5-10)

### 4.3 Penetrance/expressivity and modifiers
Female heterozygotes can have clinically significant symptoms with high variability (variable expressivity). (fete2014x‐linkedhypohidroticectodermal pages 2-4)

Evidence for specific modifier genes was not identified in the retrieved sources; however, the 2024 Korean cohort emphasizes that phenotype (complete triad vs incomplete) strongly predicts detection of EDA/EDAR mutations, suggesting clinical heterogeneity may partly reflect genetic heterogeneity and structural variants (CNVs). (kim2024geneticprofilingand pages 7-8, kim2024geneticprofilingand pages 1-2)

### 4.4 Epigenetic information
Explicit epigenetic mechanisms for XLHED were not identified in the retrieved sources.

### 4.5 Chromosomal abnormalities
Large deletions/CNVs affecting EDA contribute to disease and can be missed without CNV-aware analysis (e.g., MLPA/WGS). In the 2024 Korean ED cohort, **23.1% (3/13) of EDA-positive cases** had CNVs. (kim2024geneticprofilingand pages 1-2)

---

## 5. Environmental information
No specific toxin/lifestyle/infectious causal factors were identified; the disease is primarily genetic. Key environmental management issue is **heat exposure**, which is clinically dangerous in anhidrotic patients. (schneider2018prenatalcorrectionof pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Core pathway (causal chain)
1) **Upstream trigger:** germline pathogenic EDA variant → deficiency of functional EDA1 ligand. (schneider2018prenatalcorrectionof pages 1-2)
2) **Signal transduction:** EDA1 binds EDAR, recruits EDARADD, and activates a TNF-like signaling cascade culminating in **NF-κB activation**. (callea2022extendedoverviewof pages 2-4)
3) **Developmental consequence:** impaired epithelial–mesenchymal signaling in placodes → failed/aborted development of ectodermal appendages (eccrine sweat glands, teeth, hair follicles, meibomian glands). (callea2022extendedoverviewof pages 2-4, schneider2018prenatalcorrectionof pages 1-2)
4) **Clinical manifestations:** anhidrosis/hypohidrosis → heat intolerance/hyperthermia risk; hypodontia/oligodontia → chewing/speech/esthetic impacts; hypotrichosis; frequent ENT/respiratory problems likely related to glandular/epithelial abnormalities. (fete2014x‐linkedhypohidroticectodermal pages 2-4, schneider2018prenatalcorrectionof pages 1-2)

### 6.2 Developmental timing (critical window)
Human eccrine sweat gland morphogenesis has a defined fetal window: “key developmental events” occur in **gestational weeks 20–30**, motivating prenatal replacement therapy to rescue sweat gland formation. (schneider2022ectodermaldysplasiasnew pages 2-4)

### 6.3 Crosstalk with WNT/β-catenin (emerging mechanistic synthesis)
Mechanistic synthesis from recent literature indicates reciprocal reinforcement between EDA–EDAR–NF-κB signaling and WNT/β-catenin activity during placode development (e.g., Wnt10b as an NF-κB target; Wnt signaling upregulating Edar). This is commonly inferred from mouse developmental and single-cell analyses and provides a plausible mechanism linking EDA deficiency to broader appendage patterning defects. (jakhar2025interplaybetweenedaedar pages 5-7, jakhar2025interplaybetweenedaedar pages 2-4)

### 6.4 Suggested ontology terms
- **GO biological processes (suggested):** ectodermal appendage development; sweat gland development; tooth development; hair follicle development; epithelial–mesenchymal signaling; NF-κB signaling
- **CL cell types (suggested):** keratinocyte (epidermal basal keratinocyte); odontogenic epithelial cell; dermal papilla cell; myoepithelial cell (sweat gland)

(These are ontology suggestions aligned with the mechanisms described in the cited sources. (callea2022extendedoverviewof pages 2-4, schneider2022ectodermaldysplasiasnew pages 2-4, jakhar2025interplaybetweenedaedar pages 2-4))

---

## 7. Anatomical structures affected
### 7.1 Organ/tissue targets (with ontology suggestions)
- **Skin (UBERON:0002097)** with **eccrine sweat glands** and hair follicles affected (reduced/absent sweat glands; hypotrichosis). (aftab2023xlinkedhypohidroticectodermal pages 1-2, schneider2022ectodermaldysplasiasnew pages 2-4)
- **Dentition / tooth germs** (UBERON:0001759 tooth) with hypodontia/oligodontia. (fete2014x‐linkedhypohidroticectodermal pages 1-2, schneider2018prenatalcorrectionof pages 3-5)
- **Upper airway/nasal structures** with chronic nasal discharge/sinusitis and respiratory complications. (fete2014x‐linkedhypohidroticectodermal pages 2-4)
- **Eye and adnexa:** meibomian glands and ocular surface impacted (dry eye risk; meibomian gland endpoints included in EDELIFE). (NCT04980638 chunk 1, callea2022extendedoverviewof pages 2-4)

### 7.2 Subcellular localization
Not specifically addressed in the retrieved sources beyond EDA being a transmembrane TNF-family ligand that is cleaved and released (a secreted signaling moiety). (schneider2022ectodermaldysplasiasnew pages 2-4)

---

## 8. Temporal development
### 8.1 Onset
Clinical manifestations often begin in infancy/early childhood; one clinical summary reports symptom onset between “one month to 23 months.” (aftab2023xlinkedhypohidroticectodermal pages 1-2)

### 8.2 Progression and course
The disease is lifelong; some severe early-life risks (hyperthermia) can be mitigated with recognition and management. Registry data describe “life-long XLHED clinical complications” such as sinus infections, eczema, wheezing, and hoarse voice. (fete2014x‐linkedhypohidroticectodermal pages 1-2)

---

## 9. Inheritance and population
### 9.1 Inheritance
Predominantly **X-linked** (males more severely affected; females variably affected). (aftab2023xlinkedhypohidroticectodermal pages 1-2, fete2014x‐linkedhypohidroticectodermal pages 2-4)

### 9.2 Epidemiology (recent statistics from studies)
- **Denmark (nationwide registry ascertainment, prevalence as of Jan 1, 2011):** prevalence **1.6 per 100,000** for molecularly confirmed XLHED; broader HED/possible HED ascertainment yielded higher cumulative prevalence estimates (all categories 21.9 per 100,000). The study used ICD-10 Q82.4 for clinically diagnosed cases and confirmed XLHED by EDA mutation. (nguyennielsen2013theprevalenceof pages 1-2, nguyennielsen2013theprevalenceof pages 2-3)

**Expert interpretation:** the very large difference between molecularly confirmed prevalence and broader algorithm-defined HED prevalence implies substantial under-confirmation (genetic testing gaps) and/or misclassification when relying on administrative codes alone, supporting current emphasis on molecular confirmation and CNV-aware testing. (nguyennielsen2013theprevalenceof pages 1-2, kim2024geneticprofilingand pages 1-2)

---

## 10. Diagnostics
### 10.1 Clinical recognition
Diagnosis is often based on the triad (sweat, hair, teeth) and characteristic facies/complications. (fete2014x‐linkedhypohidroticectodermal pages 1-2, aftab2023xlinkedhypohidroticectodermal pages 1-2)

### 10.2 Functional sweating tests (quantitative biomarker)
Pilocarpine-induced sweat testing plus sweat pore density assessment is a quantifiable biomarker approach.
- In Schneider et al. (2011), sweat pore count sensitivity for identifying affected males was **94% in children** and **92% in adults**, with clear quantitative separation from controls. (schneider2011sweatingabilityand pages 5-10)
- Controls showed mean sweat volume **72 µL** and mean sweat pore density **455 pores/cm²**, whereas many XLHED males had absent pores and 0 sweat, and low-sweating males produced **1–11 µL**. (schneider2011sweatingabilityand pages 5-10, schneider2011sweatingabilityand pages 1-5)

### 10.3 Genetic testing approaches (2024 evidence-based strategy)
**2024 cohort evidence (Korea, Orphanet J Rare Dis; published 2024-09-?? per journal issue metadata):**
- Overall diagnostic yield: **74.1% (20/27)** mutation-positive. (kim2024geneticprofilingand pages 1-2)
- Among positives, **80% (16/20)** had EDA or EDAR mutations; **23.1% (3/13)** of EDA-positive cases had CNVs. (kim2024geneticprofilingand pages 1-2)
- Phenotype predicts yield: **94.1%** of patients with the complete triad (hair/skin/dental) had detectable **EDA/EDAR** mutations, vs **0%** when those three symptoms were not all present. (kim2024geneticprofilingand pages 7-8, kim2024geneticprofilingand pages 1-2)

**Direct abstract quote (diagnostic strategy conclusion):** “When conducting molecular diagnostics for ED, opting for targeted sequencing of EDA/EDAR mutations is advisable for cases with classical symptoms, while WES is deemed an effective strategy for cases in which these symptoms are absent.” (kim2024geneticprofilingand pages 1-2)

### 10.4 Prenatal diagnosis (emerging real-world implementation)
Prenatal ultrasound-based **tooth germ counting** can support non-invasive fetal assessment in at-risk pregnancies; this approach is used in trial screening and was part of the diagnostic workup for prenatal therapy. (schneider2022ectodermaldysplasiasnew pages 1-2, schneider2018prenatalcorrectionof pages 1-2)

### 10.5 Differential diagnosis
A case-based review highlights the need to distinguish XLHED from other ectodermal dysplasias and syndromes (e.g., EEC syndrome) and acquired hypohidrosis causes, emphasizing clinical and molecular confirmation. (aftab2023xlinkedhypohidroticectodermal pages 8-9)

---

## 11. Outcome / prognosis
### 11.1 Key risks and complications
- Hyperthermia risk in infancy/childhood due to inability to sweat is emphasized as potentially life-threatening. (schneider2018prenatalcorrectionof pages 1-2, nguyennielsen2013theprevalenceof pages 1-2)
- Chronic ENT/respiratory morbidity is common (registry-based frequencies summarized above). (fete2014x‐linkedhypohidroticectodermal pages 2-4)

### 11.2 Registry-based mortality signal
In EDIR registry analysis, **21%** of XLHED registrants reported a family history of infant or childhood deaths, stated as consistent with published mortality data. (fete2014x‐linkedhypohidroticectodermal pages 1-2)

---

## 12. Treatment
### 12.1 Supportive and multidisciplinary care (current standard)
Current routine care is largely **supportive and preventive**, including thermoregulation/heat avoidance strategies, dental rehabilitation (prosthodontics/implants), dermatologic management (eczema/dry skin), ENT/pulmonary management for recurrent infections, and ophthalmic care for dry eye/ocular surface disease. (aftab2023xlinkedhypohidroticectodermal pages 8-9, callea2022extendedoverviewof pages 2-4)

**Suggested MAXO terms (examples):** supportive care; dental prosthesis placement; management of hyperthermia; skin emollient therapy; artificial tears / ocular surface lubrication; respiratory infection prevention.

### 12.2 Advanced therapeutics: EDA1 protein replacement
#### 12.2.1 Prenatal intra-amniotic Fc-EDA (EDI200) – human compassionate-use evidence
Schneider et al. (NEJM, 2018-04-26) reported intra-amniotic administration of Fc-EDA (EDI200) to 3 affected male fetuses.
- **Dosing (twins):** 100 mg/kg estimated fetal body weight at **gestational week 26** and again at **week 31**. (schneider2018prenatalcorrectionof pages 3-5)
- **Evidence of fetal uptake:** cord-blood Fc-EDA measurable 7 days after administration (**62.4 and 932 ng/mL**). (schneider2018prenatalcorrectionof pages 3-5)
- **Efficacy endpoints:** treated infants had normal sweat-duct density and “normal pilocarpine-induced sweating at 6 months,” with no hyperthermic episodes or respiratory-related hospitalizations over 22 months in the twin case. (schneider2018prenatalcorrectionof pages 3-5)
- **Quote (author conclusion):** “Prenatal treatment with Fc-EDA restored sustained sweating ability in human patients with EDA mutations that abrogate perspiration.” (schneider2018prenatalcorrectionof pages 5-7)

**Visual evidence:** Figure 1 from the NEJM report shows the contrast between untreated XLHED (no sweat pores/0 µL sweat) and treated infant vs healthy control for sweat pores and sweat volume outcomes. (schneider2018prenatalcorrectionof media 9c02cda0)

#### 12.2.2 Postnatal Fc-EDA trials (limited efficacy window)
A translational review notes that postnatal dosing in infants did not successfully induce sweat ducts or sweating, consistent with a restricted developmental window for eccrine gland morphogenesis. (schneider2022ectodermaldysplasiasnew pages 2-4)

#### 12.2.3 ER004 (prenatal intra-amniotic EDELIFE trial; ongoing)
ClinicalTrials.gov describes ER004 as an “EDA1 replacement” designed for high-affinity EDAR binding.
- **Design:** Phase 2, open-label, genotype-match controlled; **3 intra-amniotic injections** ~3 weeks apart starting **gestational week 26** at **100 mg/kg estimated fetal weight per injection**. (NCT04980638 chunk 1)
- **Primary endpoint:** mean sweat volume at 6 months (pilocarpine-induced). (NCT04980638 chunk 1)
- **Secondary endpoints include:** sweat pore density, dental development, meibomian glands, ocular outcomes, hospitalizations for hyperthermia/infections. (NCT04980638 chunk 1)

**Expert analysis:** the trial’s inclusion of objective sweating endpoints (sweat volume and pore density) and longer follow-up (to age 5) directly addresses prior limitations of early small compassionate-use series and aligns with validated sweat biomarkers (pilocarpine iontophoresis, pore counts) used in genotype–phenotype work. (NCT04980638 chunk 1, schneider2011sweatingabilityand pages 5-10)

---

## 13. Prevention
### 13.1 Primary prevention
No primary prevention exists for germline XLHED beyond reproductive options.

### 13.2 Secondary/tertiary prevention (complication avoidance)
Key complication prevention includes early diagnosis, anticipatory guidance for fever/heat exposure, and early dental/ENT/ophthalmic interventions to prevent downstream morbidity. (aftab2023xlinkedhypohidroticectodermal pages 8-9, callea2022extendedoverviewof pages 2-4)

### 13.3 Genetic counseling and reproductive options
Given X-linked inheritance and severe male phenotype, cascade testing and counseling are central. Prenatal ultrasound screening (tooth germ assessment) is used clinically and in trial screening as a non-invasive diagnostic tool in at-risk pregnancies. (schneider2022ectodermaldysplasiasnew pages 1-2, schneider2018prenatalcorrectionof pages 1-2)

---

## 14. Other species / natural disease
Naturally occurring EDA-related hypohidrotic ectodermal dysplasia has been reported across species, supporting conserved biology.
- **Cat (first report, 2024-06):** a male cat with alopecia and tooth anomalies had a hemizygous EDA missense variant; the paper notes EDA loss-of-function variants cause HED in humans, mice, dogs, and cattle and extends this to cats. (rietmann2024edamissensevariant pages 1-2)
- **Cattle (historic):** evidence cited for bovine anhidrotic ED caused by deletion of exon 3 of the bovine ED1 gene (EDA ortholog). (rietmann2024edamissensevariant pages 2-4)

**NCBI Taxonomy identifiers** were not provided in the retrieved excerpts.

---

## 15. Model organisms
### 15.1 Tabby mouse (murine Eda model)
The Tabby mouse is a canonical model of EDA deficiency used to study ectodermal appendage development and therapeutic rescue by prenatal EDA replacement; mechanistic work in the NEJM report also used Eda-deficient mice to show neonatal Fc receptor–dependent fetal uptake after intra-amniotic therapy. (schneider2018prenatalcorrectionof pages 2-3, schneider2018prenatalcorrectionof pages 3-5)

### 15.2 Translational large-animal models
Dog models of XLHED have been used for prenatal recombinant EDA1 administration, with improvements reported across multiple ectodermal structures, supporting translational relevance to prenatal therapy. (aftab2023xlinkedhypohidroticectodermal pages 8-9)

---

## Notes on evidence gaps
- **Orphanet identifiers, ICD-11, and MeSH terms beyond those in ClinicalTrials.gov** were not directly extractable from the retrieved texts.
- **PMIDs** were not present in the excerpts provided for most papers (NEJM/Orphanet/Cureus); therefore, this report cites DOIs/URLs and publication month/year as available in-source.

---

## Key sources (with URLs and dates)
- Schneider H. *Prenatal Correction of X-Linked Hypohidrotic Ectodermal Dysplasia.* **N Engl J Med**. 2018-04-26. https://doi.org/10.1056/NEJMoa1714322 (schneider2018prenatalcorrectionof pages 1-2, schneider2018prenatalcorrectionof pages 3-5)
- Kim MJ et al. *Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in Korea.* **Orphanet J Rare Dis**. 2024 (volume 19:329; published 2024). https://doi.org/10.1186/s13023-024-03331-6 (kim2024geneticprofilingand pages 1-2)
- Nguyen-Nielsen M et al. *The prevalence of XLHED in Denmark, 1995–2010.* **Eur J Med Genet**. 2013-05. https://doi.org/10.1016/j.ejmg.2013.01.012 (nguyennielsen2013theprevalenceof pages 1-2)
- Fete M et al. *XLHED: Clinical and diagnostic insights from an international patient registry.* **Am J Med Genet A**. 2014-10. https://doi.org/10.1002/ajmg.a.36436 (fete2014x‐linkedhypohidroticectodermal pages 1-2)
- ClinicalTrials.gov. *EDELIFE: Intraamniotic Administrations of ER004…* **NCT04980638**. Updated 2025-04-30. https://clinicaltrials.gov/study/NCT04980638 (NCT04980638 chunk 1)
- Schneider H et al. *Sweating ability and genotype in individuals with XLHED.* **J Med Genet**. 2011-02. https://doi.org/10.1136/jmg.2010.084012 (schneider2011sweatingabilityand pages 5-10)


References

1. (aftab2023xlinkedhypohidroticectodermal pages 1-2): Hammad Aftab, Ivan A Escudero, and Fatin Sahhar. X-linked hypohidrotic ectodermal dysplasia (xlhed): a case report and overview of the diagnosis and multidisciplinary modality treatments. Cureus, Jun 2023. URL: https://doi.org/10.7759/cureus.40383, doi:10.7759/cureus.40383. This article has 10 citations.

2. (callea2022extendedoverviewof pages 2-4): Michele Callea, Stefano Bignotti, Francesco Semeraro, Francisco Cammarata-Scalisi, Jinia El-Feghaly, Antonino Morabito, Vito Romano, and Colin E. Willoughby. Extended overview of ocular phenotype with recent advances in hypohidrotic ectodermal dysplasia. Children, 9:1357, Sep 2022. URL: https://doi.org/10.3390/children9091357, doi:10.3390/children9091357. This article has 9 citations.

3. (kim2024geneticprofilingand pages 1-2): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

4. (kim2024geneticprofilingand pages 7-8): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

5. (schneider2018prenatalcorrectionof pages 3-5): Holm Schneider, Florian Faschingbauer, Sonia Schuepbach-Mallepell, Iris Körber, Sigrun Wohlfart, Angela Dick, Mandy Wahlbuhl, Christine Kowalczyk-Quintas, Michele Vigolo, Neil Kirby, Corinna Tannert, Oliver Rompel, Wolfgang Rascher, Matthias W. Beckmann, and Pascal Schneider. Prenatal correction of x-linked hypohidrotic ectodermal dysplasia. New England Journal of Medicine, 378:1604-1610, Apr 2018. URL: https://doi.org/10.1056/nejmoa1714322, doi:10.1056/nejmoa1714322. This article has 219 citations and is from a highest quality peer-reviewed journal.

6. (NCT04980638 chunk 1):  Intraamniotic Administrations of ER004 to Male Subjects With X-linked Hypohidrotic Ectodermal Dysplasia. EspeRare Foundation. 2022. ClinicalTrials.gov Identifier: NCT04980638

7. (fete2014x‐linkedhypohidroticectodermal pages 2-4): Mary Fete, Julie Hermann, Jeffrey Behrens, and Kenneth M. Huttner. X‐linked hypohidrotic ectodermal dysplasia (xlhed): clinical and diagnostic insights from an international patient registry. American Journal of Medical Genetics Part A, 164:2437-2442, Oct 2014. URL: https://doi.org/10.1002/ajmg.a.36436, doi:10.1002/ajmg.a.36436. This article has 72 citations.

8. (fete2014x‐linkedhypohidroticectodermal pages 1-2): Mary Fete, Julie Hermann, Jeffrey Behrens, and Kenneth M. Huttner. X‐linked hypohidrotic ectodermal dysplasia (xlhed): clinical and diagnostic insights from an international patient registry. American Journal of Medical Genetics Part A, 164:2437-2442, Oct 2014. URL: https://doi.org/10.1002/ajmg.a.36436, doi:10.1002/ajmg.a.36436. This article has 72 citations.

9. (NCT04980638 chunk 2):  Intraamniotic Administrations of ER004 to Male Subjects With X-linked Hypohidrotic Ectodermal Dysplasia. EspeRare Foundation. 2022. ClinicalTrials.gov Identifier: NCT04980638

10. (nguyennielsen2013theprevalenceof pages 1-2): Mary Nguyen-Nielsen, Stine Skovbo, Dea Svaneby, Lars Pedersen, and Jon Fryzek. The prevalence of x-linked hypohidrotic ectodermal dysplasia (xlhed) in denmark, 1995-2010. European journal of medical genetics, 56 5:236-42, May 2013. URL: https://doi.org/10.1016/j.ejmg.2013.01.012, doi:10.1016/j.ejmg.2013.01.012. This article has 97 citations and is from a peer-reviewed journal.

11. (schneider2018prenatalcorrectionof pages 1-2): Holm Schneider, Florian Faschingbauer, Sonia Schuepbach-Mallepell, Iris Körber, Sigrun Wohlfart, Angela Dick, Mandy Wahlbuhl, Christine Kowalczyk-Quintas, Michele Vigolo, Neil Kirby, Corinna Tannert, Oliver Rompel, Wolfgang Rascher, Matthias W. Beckmann, and Pascal Schneider. Prenatal correction of x-linked hypohidrotic ectodermal dysplasia. New England Journal of Medicine, 378:1604-1610, Apr 2018. URL: https://doi.org/10.1056/nejmoa1714322, doi:10.1056/nejmoa1714322. This article has 219 citations and is from a highest quality peer-reviewed journal.

12. (nguyennielsen2013theprevalenceof pages 2-3): Mary Nguyen-Nielsen, Stine Skovbo, Dea Svaneby, Lars Pedersen, and Jon Fryzek. The prevalence of x-linked hypohidrotic ectodermal dysplasia (xlhed) in denmark, 1995-2010. European journal of medical genetics, 56 5:236-42, May 2013. URL: https://doi.org/10.1016/j.ejmg.2013.01.012, doi:10.1016/j.ejmg.2013.01.012. This article has 97 citations and is from a peer-reviewed journal.

13. (schneider2022ectodermaldysplasiasnew pages 1-2): Holm Schneider. Ectodermal dysplasias: new perspectives on the treatment of so far immedicable genetic disorders. Frontiers in Genetics, Sep 2022. URL: https://doi.org/10.3389/fgene.2022.1000744, doi:10.3389/fgene.2022.1000744. This article has 27 citations and is from a peer-reviewed journal.

14. (kovalskaia2023molecularbasisand pages 1-2): V. A. Kovalskaia, T. Cherevatova, A. V. Polyakov, and O. P. Ryzhkova. Molecular basis and genetics of hypohidrotic ectodermal dysplasias. Vavilov Journal of Genetics and Breeding, 27:676-683, Nov 2023. URL: https://doi.org/10.18699/vjgb-23-78, doi:10.18699/vjgb-23-78. This article has 6 citations.

15. (schneider2011sweatingabilityand pages 5-10): Holm Schneider, Johanna Hammersen, Sabine Preisler-Adams, Kenneth Huttner, Wolfgang Rascher, and Axel Bohring. Sweating ability and genotype in individuals with x-linked hypohidrotic ectodermal dysplasia. Journal of Medical Genetics, 48:426-432, Feb 2011. URL: https://doi.org/10.1136/jmg.2010.084012, doi:10.1136/jmg.2010.084012. This article has 70 citations and is from a domain leading peer-reviewed journal.

16. (schneider2011sweatingabilityand pages 1-5): Holm Schneider, Johanna Hammersen, Sabine Preisler-Adams, Kenneth Huttner, Wolfgang Rascher, and Axel Bohring. Sweating ability and genotype in individuals with x-linked hypohidrotic ectodermal dysplasia. Journal of Medical Genetics, 48:426-432, Feb 2011. URL: https://doi.org/10.1136/jmg.2010.084012, doi:10.1136/jmg.2010.084012. This article has 70 citations and is from a domain leading peer-reviewed journal.

17. (aftab2023xlinkedhypohidroticectodermal pages 8-9): Hammad Aftab, Ivan A Escudero, and Fatin Sahhar. X-linked hypohidrotic ectodermal dysplasia (xlhed): a case report and overview of the diagnosis and multidisciplinary modality treatments. Cureus, Jun 2023. URL: https://doi.org/10.7759/cureus.40383, doi:10.7759/cureus.40383. This article has 10 citations.

18. (schneider2022ectodermaldysplasiasnew pages 2-4): Holm Schneider. Ectodermal dysplasias: new perspectives on the treatment of so far immedicable genetic disorders. Frontiers in Genetics, Sep 2022. URL: https://doi.org/10.3389/fgene.2022.1000744, doi:10.3389/fgene.2022.1000744. This article has 27 citations and is from a peer-reviewed journal.

19. (jakhar2025interplaybetweenedaedar pages 5-7): Ajay Jakhar, Konrad Łukaszyk, Anna Pulawska-Czub, and Krzysztof Kobielak. Interplay between eda-edar and wnt signalling pathways in the development of skin appendages in hypohidrotic ectodermal dysplasia. Pediatria i Medycyna Rodzinna, 21:51-58, Apr 2025. URL: https://doi.org/10.15557/pimr.2025.0006, doi:10.15557/pimr.2025.0006. This article has 3 citations.

20. (jakhar2025interplaybetweenedaedar pages 2-4): Ajay Jakhar, Konrad Łukaszyk, Anna Pulawska-Czub, and Krzysztof Kobielak. Interplay between eda-edar and wnt signalling pathways in the development of skin appendages in hypohidrotic ectodermal dysplasia. Pediatria i Medycyna Rodzinna, 21:51-58, Apr 2025. URL: https://doi.org/10.15557/pimr.2025.0006, doi:10.15557/pimr.2025.0006. This article has 3 citations.

21. (schneider2018prenatalcorrectionof pages 5-7): Holm Schneider, Florian Faschingbauer, Sonia Schuepbach-Mallepell, Iris Körber, Sigrun Wohlfart, Angela Dick, Mandy Wahlbuhl, Christine Kowalczyk-Quintas, Michele Vigolo, Neil Kirby, Corinna Tannert, Oliver Rompel, Wolfgang Rascher, Matthias W. Beckmann, and Pascal Schneider. Prenatal correction of x-linked hypohidrotic ectodermal dysplasia. New England Journal of Medicine, 378:1604-1610, Apr 2018. URL: https://doi.org/10.1056/nejmoa1714322, doi:10.1056/nejmoa1714322. This article has 219 citations and is from a highest quality peer-reviewed journal.

22. (schneider2018prenatalcorrectionof media 9c02cda0): Holm Schneider, Florian Faschingbauer, Sonia Schuepbach-Mallepell, Iris Körber, Sigrun Wohlfart, Angela Dick, Mandy Wahlbuhl, Christine Kowalczyk-Quintas, Michele Vigolo, Neil Kirby, Corinna Tannert, Oliver Rompel, Wolfgang Rascher, Matthias W. Beckmann, and Pascal Schneider. Prenatal correction of x-linked hypohidrotic ectodermal dysplasia. New England Journal of Medicine, 378:1604-1610, Apr 2018. URL: https://doi.org/10.1056/nejmoa1714322, doi:10.1056/nejmoa1714322. This article has 219 citations and is from a highest quality peer-reviewed journal.

23. (rietmann2024edamissensevariant pages 1-2): Stefan J. Rietmann, Noëlle Cochet-Faivre, Helene Dropsy, Vidhya Jagannathan, Lucie Chevallier, and Tosso Leeb. Eda missense variant in a cat with x-linked hypohidrotic ectodermal dysplasia. Genes, 15:854, Jun 2024. URL: https://doi.org/10.3390/genes15070854, doi:10.3390/genes15070854. This article has 1 citations.

24. (rietmann2024edamissensevariant pages 2-4): Stefan J. Rietmann, Noëlle Cochet-Faivre, Helene Dropsy, Vidhya Jagannathan, Lucie Chevallier, and Tosso Leeb. Eda missense variant in a cat with x-linked hypohidrotic ectodermal dysplasia. Genes, 15:854, Jun 2024. URL: https://doi.org/10.3390/genes15070854, doi:10.3390/genes15070854. This article has 1 citations.

25. (schneider2018prenatalcorrectionof pages 2-3): Holm Schneider, Florian Faschingbauer, Sonia Schuepbach-Mallepell, Iris Körber, Sigrun Wohlfart, Angela Dick, Mandy Wahlbuhl, Christine Kowalczyk-Quintas, Michele Vigolo, Neil Kirby, Corinna Tannert, Oliver Rompel, Wolfgang Rascher, Matthias W. Beckmann, and Pascal Schneider. Prenatal correction of x-linked hypohidrotic ectodermal dysplasia. New England Journal of Medicine, 378:1604-1610, Apr 2018. URL: https://doi.org/10.1056/nejmoa1714322, doi:10.1056/nejmoa1714322. This article has 219 citations and is from a highest quality peer-reviewed journal.