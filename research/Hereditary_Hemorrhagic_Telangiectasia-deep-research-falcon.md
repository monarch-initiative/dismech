---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T07:09:58.537416'
end_time: '2026-04-24T07:25:19.914350'
duration_seconds: 921.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Hemorrhagic Telangiectasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Hemorrhagic Telangiectasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hemorrhagic Telangiectasia** covering all of the
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
- **Disease Name:** Hereditary Hemorrhagic Telangiectasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hemorrhagic Telangiectasia** covering all of the
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


# Hereditary Hemorrhagic Telangiectasia (HHT) — Disease Characteristics Research Report

## 1. Disease information

### 1.1 Concise overview (current understanding)
Hereditary hemorrhagic telangiectasia (HHT) is an **inherited vascular disorder** characterized by **mucocutaneous telangiectases** and **visceral arteriovenous malformations (AVMs)**, with **recurrent epistaxis** as the most common clinical manifestation and a major cause of iron-deficiency anemia and reduced quality of life. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2, ahmad2024managingepistaxisin pages 1-2)

Authoritative definitions emphasize autosomal dominant inheritance and vascular malformations: a 2024 JCI review describes HHT as an “inherited vascular disorder” transmitted “in an autosomal dominant manner” and characterized by mucocutaneous telangiectases and visceral AVMs (lungs, liver, brain). (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

### 1.2 Key identifiers (as found in retrieved sources)
Because the current tool run focused on primary literature and trial registries (not OMIM/Orphanet/MeSH/ICD web records), only a subset of identifiers were explicitly present in retrieved texts.

- **Orphanet (ORPHA):** **ORPHA:774** (explicitly stated in a 2024 Orphanet Journal of Rare Diseases paper). URL: https://doi.org/10.1186/s13023-024-03493-3 (published Dec 2024). (villanueva2024minimalencephalopathyin pages 1-2)
- **OMIM disease subtype identifiers (explicit in retrieved review):**
  - HHT1: **OMIM 187300**
  - HHT2: **OMIM 600376**
  - Juvenile polyposis/HHT (JP-HHT): **OMIM 175050**
  - HHT5: **OMIM 615506**
  URL: https://doi.org/10.1172/jci176379 (published Feb 2024). (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)
- **OMIM gene identifiers (explicit in retrieved pediatric review):**
  - **ENG** (Endoglin; locus given as 9q34.11 with OMIM subtype context)
  - **ACVRL1** (12q13.13; **OMIM 601284**)
  - **SMAD4** (18q21.2; **OMIM 600993**)
  - **GDF2** (10q11.22; **OMIM 605120**)
  URL: https://doi.org/10.3390/pediatric15010011 (published Feb 2023). (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)

Not found explicitly in the retrieved text excerpts during this run (and therefore **not asserted here**): MONDO ID, MeSH Unique ID, ICD-10/ICD-11 codes.

### 1.3 Synonyms / alternative names
Synonyms supported by retrieved primary/review sources include:
- **Osler-Weber-Rendu syndrome** (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)
- **Rendu–Osler–Weber syndrome (ROW)** (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)

### 1.4 Evidence source type
The report integrates (i) **aggregated disease-level resources** (peer-reviewed reviews and cohort/registry analyses) and (ii) **patient-level/clinical study evidence**, including randomized controlled trial evidence (NEJM PATH-HHT) and observational studies. (alsamkari2024pomalidomideforepistaxis pages 1-3, alvarezhernandez2023tacrolimusasa pages 1-2, criscuolo2025hereditaryhemorrhagictelangiectasia pages 1-6)

### 1.5 Quick-reference identifiers/criteria table
| Category | Details |
|---|---|
| Disease name / synonyms | **Hereditary hemorrhagic telangiectasia (HHT)**; also **Osler-Weber-Rendu syndrome**, **Rendu-Osler-Weber syndrome**, **Rendu-Osler syndrome**, historical **Osler's disease** (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2, tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2, ahmad2024managingepistaxisin pages 1-2, gong2025quantifyingtheburden pages 1-2) |
| Key identifiers explicitly found | **HHT1**: OMIM **187300**; **HHT2**: OMIM **600376**; **JP-HHT**: OMIM **175050**; **HHT5**: OMIM **615506**; **Orphanet/ORPHA**: **774** (reported in an HHT Orphanet-linked 2024 source) (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2, ochiai2026acaseof pages 5-6, villanueva2024minimalencephalopathyin pages 1-2) |
| Main causal genes with OMIM gene IDs mentioned | **ENG** (Endoglin) — OMIM **131195**; **ACVRL1** — OMIM **601284**; **SMAD4** — OMIM **600993**; **GDF2** — OMIM **605120** (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2) |
| Gene-to-subtype mapping | **ENG → HHT1**; **ACVRL1 → HHT2**; **SMAD4 → juvenile polyposis/HHT overlap**; **GDF2 → HHT5 / HHT-like phenotype** (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2, tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2, jain2023pathogenicvariantfrequencies pages 2-4) |
| Core Curaçao criterion 1 | **Epistaxis** — spontaneous, recurrent nosebleeds (ahmad2024managingepistaxisin pages 1-2, ahmad2024managingepistaxisin media 4cb59254) |
| Core Curaçao criterion 2 | **Telangiectasia** — multiple, characteristic sites: lips, oral cavity, fingers, nose (ahmad2024managingepistaxisin pages 1-2, ahmad2024managingepistaxisin media 4cb59254) |
| Core Curaçao criterion 3 | **Visceral lesions** — gastrointestinal telangiectasia (with/without bleeding), pulmonary AVM, hepatic AVM, cerebral AVM, spinal AVM (ahmad2024managingepistaxisin pages 1-2, ahmad2024managingepistaxisin media 4cb59254) |
| Core Curaçao criterion 4 | **Family history** — first-degree relative with HHT according to these criteria (ahmad2024managingepistaxisin pages 1-2, ahmad2024managingepistaxisin media 4cb59254) |
| Diagnostic thresholds | **Definite HHT**: 3 criteria present; **Possible/Suspected HHT**: 2 criteria present; **Unlikely HHT**: fewer than 2 criteria present (ahmad2024managingepistaxisin pages 1-2, ahmad2024managingepistaxisin media 4cb59254) |


*Table: This table summarizes the core naming, identifiers, major causal genes, and clinical diagnostic criteria for hereditary hemorrhagic telangiectasia from the retrieved sources. It is useful as a compact reference for populating standardized disease knowledge-base fields.*

## 2. Etiology

### 2.1 Disease causal factors
HHT is primarily a **Mendelian autosomal dominant** disease caused by **heterozygous pathogenic variants** in genes encoding components of an endothelial BMP/TGF-β signaling axis:
- ENG (endoglin; HHT1)
- ACVRL1 (ALK1; HHT2)
- SMAD4 (JP-HHT)
- GDF2 (BMP9; HHT5 / HHT-like phenotype)
This etiology is summarized in 2023–2024 reviews, which describe HHT as caused by **loss-of-function mutations** in the **BMP9/BMP10–ENG–ALK1–SMAD4** signaling pathway in endothelial cells. (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2, tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

A 2024 JCI review explicitly attributes HHT to “loss-of-function mutations” in the “endothelial BMP9-10/ENG/ALK1/SMAD4 signaling pathway.” (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

### 2.2 Risk factors

#### Genetic risk factors (causal genes; relative frequency)
A 2023 pediatric-focused review reports that **>95%** of patients have causal variants in **ENG** or **ACVRL1**, with **SMAD4** in a minority (~2%) associated with a juvenile polyposis/HHT overlap, and **GDF2** causative in very rare reported cases. (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)

Variant classes in HHT include **missense**, **splice-site**, and **copy-number** (deletions/duplications) changes; the same review notes variant types including “missense, splice site, deletions, and duplications.” (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)

#### Environmental/physiologic triggers as “second hits”
While the germline mutation is present in every cell, HHT lesions are typically focal, implying local triggers. A key contemporary concept is that focal lesion formation may require **additional pro-angiogenic/pro-inflammatory triggers**. The 2024 JCI review notes that preclinical data support triggers such as **VEGF**, **LPS**, or **wounding**, which can promote AVM formation in susceptible (Eng+/– or Alk1+/–) settings, and that VEGF blockade can reduce AVMs in models. (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3)

### 2.3 Protective factors
This tool run did not retrieve primary evidence for protective factors (genetic or environmental) that reduce HHT risk itself; HHT is typically present from birth due to inherited pathogenic variants. (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2, tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

### 2.4 Gene–environment / gene–trigger interactions
Current mechanistic understanding supports a gene–trigger interaction framework where germline haploinsufficiency sets susceptibility, and local angiogenic/inflammatory stimuli contribute to lesion formation (“second hit” paradigm). (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3, whitehead2024investigationofthe pages 1-2)

## 3. Phenotypes

### 3.1 Core phenotype spectrum
HHT is clinically characterized by:
- **Recurrent spontaneous epistaxis** (often earliest and most common symptom)
- **Mucocutaneous telangiectases** (lips/oral cavity/tongue/fingers/nasal mucosa)
- **Visceral AVMs** (lungs, liver, brain; also GI and spinal lesions)
These are formalized in the Curaçao diagnostic criteria. (ahmad2024managingepistaxisin media 4cb59254, danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)

A 2024 narrative review reiterates that recurrent epistaxis occurs in “nearly all affected individuals.” (ahmad2024managingepistaxisin pages 1-2)

### 3.2 Phenotype characteristics (onset, frequency, progression)

#### Epistaxis
- Frequency: in a national registry cohort (Uruguay, 2025 preprint), **epistaxis affected 88.9%** of adults. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 1-6)
- Age of onset: in the Uruguay cohort, mean onset was **17.6 years**, with **61.3%** onset before age 20. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 23-28)
- Pediatric onset: a pediatric review reports epistaxis median onset **5 years** (range 0.25–15) in one series and that epistaxis is present in **~90% before age 30**. (danesino2023hereditaryhemorrhagictelangiectasia pages 2-4)

Suggested HPO terms:
- Epistaxis **HP:0000425** (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

#### Telangiectases
- In the Uruguay cohort, mucocutaneous telangiectasias were observed in **~90%**. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)
- Pediatric review: telangiectases appear at typical sites and “about one third of cases” report appearance **before age 20**. (danesino2023hereditaryhemorrhagictelangiectasia pages 4-6)

Suggested HPO terms:
- Telangiectasia **HP:0000954**; mucocutaneous telangiectasia (as concept) (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

#### Visceral AVMs (lung/brain/liver/GI)
The 2024 JCI review highlights lung/liver/brain as major visceral sites. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

Recent cohort data (Uruguay registry):
- Pulmonary AVMs: **20%**
- Cerebral AVMs: **15.7%**
- Hepatic AVMs: **18.9%**
- Gastrointestinal telangiectasias: upper GI **34.4%**, lower GI **15.6%**
(criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

Suggested HPO terms:
- Pulmonary arteriovenous malformation **HP:0002116** (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)
- Cerebral arteriovenous malformation **HP:0002501** (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)
- Hepatic arteriovenous malformation **HP:0011792** (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)
- Gastrointestinal hemorrhage **HP:0002104** and related GI telangiectasia concepts (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

#### Anemia and iron deficiency
In the Uruguay cohort, severe anemia was reflected by low hemoglobin values; overall **lowest median hemoglobin was 7 g/dL** (range 5–12), with correlation by epistaxis severity (e.g., severe epistaxis lowest Hb median **5.5 g/dL**). (criscuolo2025hereditaryhemorrhagictelangiectasia pages 23-28)

Suggested HPO terms:
- Iron deficiency anemia **HP:0002901** (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

### 3.3 Quality-of-life impact
HHT epistaxis is directly linked to reduced HRQoL; in the NEJM PATH-HHT trial, the abstract explicitly states epistaxis “results in iron deficiency anemia and reduced health-related quality of life (HRQoL).” (alsamkari2024pomalidomideforepistaxis pages 1-3)

In a large cross-sectional HRQoL study (Orphanet J Rare Dis, published Mar 2025), among respondents the most common symptoms were **epistaxis (92%)** and **fatigue (79%)**, and severe epistaxis was associated with higher depression/anxiety/fatigue measures. URL: https://doi.org/10.1186/s13023-025-03620-8. (gong2025quantifyingtheburden pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genes (and subtype mapping)
Core causal genes and subtype mapping (from 2023–2024 reviews):
- **ENG → HHT1** (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)
- **ACVRL1 (ALK1) → HHT2** (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)
- **SMAD4 → JP-HHT** (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)
- **GDF2 (BMP9) → HHT5 / HHT-like** (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

### 4.2 Pathogenic variant classes and functional consequences
- Disease mechanism is largely **loss of function**. The 2024 JCI review frames causal variants as “loss-of-function” in the BMP9/BMP10–ENG–ALK1–SMAD4 axis. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)
- Variant classes include missense, splice-site, frameshift/nonsense (premature termination), and copy-number variants (deletions/duplications). (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2, shovlin2020mutationalandphenotypic pages 9-10)
- A 2023 genetic analysis highlighted a subset of **ACVRL1 missense variants** that produce ALK1 protein that reaches the endothelial cell surface but “fails to signal” (kinase-inactive), suggesting functionally distinct pathogenic mechanisms within the same gene. (jain2023pathogenicvariantfrequencies pages 1-2)

Somatic vs germline and “two-hit” lesions:
- A 2024 tissue sequencing study reports very-low-level **somatic second-hit mutations** in nasal telangiectasias and solid organ AVMs, consistent with “somatic biallelic second-hit mutations” contributing to lesion formation. (whitehead2024investigationofthe pages 1-2)

### 4.3 Penetrance and expressivity
HHT shows age-dependent penetrance and variable expressivity.
- A 2023 review states penetrance is “above 95% after age 40” and notes underdiagnosis because full signs may appear later in life. (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)

### 4.4 Modifier genes
Evidence for modifier loci is emerging. A 2023 genetic review notes independent variants in **PTPN14** and **ADAM17** associated with pulmonary AVMs (as modifier associations), alongside broad variability and incomplete genotype–phenotype predictability for traits like epistaxis severity. (jain2023pathogenicvariantfrequencies pages 2-4)

### 4.5 Epigenetics and chromosomal abnormalities
No specific epigenetic signatures or recurrent chromosomal abnormalities were retrieved in this tool run.

## 5. Environmental information
HHT is not an infectious disease; no infectious triggers were retrieved.

Environmental/physiologic triggers are best conceptualized as lesion-promoting **angiogenic/inflammatory stimuli** (e.g., VEGF, wounding, LPS in models) superimposed on genetic susceptibility. (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3)

## 6. Mechanism / pathophysiology

### 6.1 Core pathway and causal chain
The mechanistic backbone is impaired endothelial signaling through the **BMP9/BMP10–ENG–ALK1–SMAD4** axis (vascular quiescence and stability). Loss-of-function variants reduce pathway signaling, predisposing to abnormal angiogenesis and AVM development. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

A 2024 review describes AVM morphogenesis as starting with “focal dilatations of postcapillary venules” that expand to include capillaries and connect to dilated arterioles, forming direct arteriovenous shunts. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

### 6.2 Two-hit/somatic mosaic model
Focal lesion distribution despite germline heterozygosity supports a two-hit concept:
- Reviews cite evidence of low-frequency somatic mutations in vascular lesions leading to biallelic loss of ENG/ACVRL1. (shovlin2020mutationalandphenotypic pages 23-24)
- A 2024 targeted tissue study provides direct support, reporting somatic second-hit mutations in **nasal telangiectasia** and **solid organ AVMs** at very low mosaic levels (down to ~1%). (whitehead2024investigationofthe pages 1-2, whitehead2024investigationofthe pages 2-3)

### 6.3 Angiogenic mediators and inflammation
The mutated BMP/ENG/ALK1/SMAD4 pathway crosstalks with pro-angiogenic pathways (notably **VEGF**), and anti-VEGF strategies can reduce lesions in models and improve bleeding clinically. (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3)

### 6.4 Cell types and ontology suggestions
Primary implicated cell type:
- **Endothelial cell** (CL:0000115) — central to ENG/ALK1/BMP9 signaling and lesion formation. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

Other relevant cell/tissue features:
- Perivascular lymphocytic infiltrates suggest immune involvement at lesions. (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3)

Suggested GO biological process terms (high-level, mechanism-aligned):
- angiogenesis (GO:0001525)
- blood vessel morphogenesis (GO:0048514)
- endothelial cell proliferation (GO:0001935)
- regulation of BMP signaling pathway (GO:0030510)
- regulation of TGF-β receptor signaling pathway (GO:0017015)

## 7. Anatomical structures affected

### 7.1 Organ level (primary sites)
Major anatomic targets include:
- **Nasal mucosa** (epistaxis)
- **Skin/oral mucosa** (telangiectases)
- **Lung, liver, brain** (visceral AVMs)
- **Gastrointestinal tract** (telangiectases/bleeding)
(tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2, ahmad2024managingepistaxisin media 4cb59254)

Suggested UBERON concepts (examples for knowledge base mapping):
- nasal mucosa (UBERON:0001826)
- lung (UBERON:0002048)
- liver (UBERON:0002107)
- brain (UBERON:0000955)
- gastrointestinal tract (UBERON:0001555)

### 7.2 Tissue/cell level
- Vascular endothelium is the key affected tissue; defective endothelial signaling leads to abnormal angiogenesis and shunting. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

## 8. Temporal development

### 8.1 Onset
- Epistaxis often begins in childhood/adolescence (mean onset ~17.6 years in one cohort; median 5 years in a pediatric series). (criscuolo2025hereditaryhemorrhagictelangiectasia pages 23-28, danesino2023hereditaryhemorrhagictelangiectasia pages 2-4)

### 8.2 Progression
- Penetrance is age-dependent and becomes essentially complete in adulthood (>95% after age 40). (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)
- Visceral lesions can be present early (including in children) and may cause sudden complications. (danesino2023hereditaryhemorrhagictelangiectasia pages 4-6)

## 9. Inheritance and population

### 9.1 Inheritance
Autosomal dominant inheritance is consistently reported across 2023–2024 sources. (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2, tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)

### 9.2 Epidemiology and population statistics
- General prevalence estimates in recent reviews: “up to 1 in 5,000 individuals” (JCI review, Feb 2024). (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2)
- A 2023 review states “a reasonable general estimate of the prevalence is 1 in 5000” and that HHT “affects at least one million people worldwide.” (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)
- Country-level registry estimate (Uruguay, Aug 2025 preprint): prevalence **3.83 per 100,000** (95% CI 3.26–4.61), female:male ratio **1.73:1**, mean age **48.2 ± 18.3 years**, diagnostic delay **5.7 ± 10.6 years**, and low screening adherence (complete screening ~21%). URL: https://doi.org/10.1101/2025.08.18.25333772. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

Founder effects are noted in reviews, including a founder effect reported in the Netherlands Antilles. (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2)

## 10. Diagnostics

### 10.1 Clinical criteria: Curaçao criteria
The Curaçao criteria and thresholds are explicitly laid out in a 2024 review’s Table 1 (cropped below). (ahmad2024managingepistaxisin media 4cb59254)

Key criteria:
1) recurrent spontaneous epistaxis
2) multiple telangiectases at characteristic sites
3) visceral lesions (GI telangiectasia; pulmonary/hepatic/cerebral/spinal AVMs)
4) first-degree family history
Definite: 3 criteria; Possible/Suspected: 2; Unlikely: <2. (ahmad2024managingepistaxisin media 4cb59254)

### 10.2 Genetic testing
Multiple sources state that identifying a heterozygous pathogenic variant in HHT genes is diagnostic/confirmatory.
- A 2024 epistaxis-focused review states that “identification of a heterozygous pathogenic variant in ACVRL1, ENG, GDF2, and SMAD4 genes is diagnostic.” (ahmad2024managingepistaxisin pages 1-2)

Pediatric considerations:
- Curaçao criteria sensitivity is lower in early childhood; a pediatric review reports sensitivity 42% in ages 0–5 vs 91% in 16–21, with high specificity, and notes nasal endoscopy improves sensitivity. (danesino2023hereditaryhemorrhagictelangiectasia pages 2-4)

### 10.3 Imaging and screening implementation (real-world)
Registry data provide real-world implementation gaps: in Uruguay, only ~21% completed recommended screening (bubble echocardiography + brain imaging + hepatic Doppler), and many had only partial imaging workups. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

## 11. Outcome / prognosis

### 11.1 Complications (morbidity)
Major complications arise from visceral AVMs:
- Pulmonary AVMs can lead to paradoxical emboli causing **stroke** and **brain abscess**; this is emphasized in mechanistic reviews and confirmed by cohort complication data. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2, criscuolo2025hereditaryhemorrhagictelangiectasia pages 23-28)
- In the Uruguay cohort, pulmonary AVM-related complications included ischemic stroke **12.2%**, TIA **11.1%**, brain abscess **2.2%**. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 23-28)

### 11.2 Quality-of-life outcomes
The 2024 NEJM PATH-HHT trial showed improvement in disease-specific QoL with reduced epistaxis (see Treatment). (alsamkari2024pomalidomideforepistaxis pages 1-3)

Mortality and formal survival statistics were not retrieved in the current tool run.

## 12. Treatment

### 12.1 Supportive and interventional care (core real-world approaches)
Treatment is typically symptom- and complication-directed: iron replacement and transfusion for chronic bleeding anemia; endoscopic/surgical management for epistaxis; and embolization or other interventions for AVMs depending on location and risk. A 2024 epistaxis review describes a “stepwise approach” escalating from conservative measures to more invasive procedures. (ahmad2024managingepistaxisin pages 1-2)

### 12.2 Pharmacotherapy and targeted/anti-angiogenic strategies (recent developments)

#### Pomalidomide (PATH-HHT; randomized placebo-controlled)
High-quality recent evidence is provided by the PATH-HHT trial (NEJM, Sep 2024):
- Design: randomized 2:1 pomalidomide 4 mg daily vs placebo for 24 weeks; n=144 randomized.
- Primary endpoint: change in Epistaxis Severity Score (ESS); ≥0.71 considered clinically significant.
- Result: mean ESS difference vs placebo at 24 weeks **−0.94** (95% CI −1.57 to −0.31; p=0.004).
- HRQoL: HHT-specific QoL score improved (mean difference **−1.4**; 95% CI −2.6 to −0.3).
- Safety: neutropenia, constipation, rash were more common; grade ≥3 adverse events 47% vs 24%; VTE 4% vs 2%.
URL: https://doi.org/10.1056/NEJMoa2312749 (published Sep 2024). (alsamkari2024pomalidomideforepistaxis pages 1-3, alsamkari2024pomalidomideforepistaxis pages 6-8)

MAXO suggestions:
- immunomodulatory drug therapy; treatment of epistaxis; treatment of chronic anemia (conceptual MAXO mapping).

#### Systemic tacrolimus (observational/off-label clinical evidence; translational rationale)
A 2023 observational study (J Clin Med, Nov 2023) reports 11 refractory HHT patients treated off-label with low-dose tacrolimus (0.5–2 mg/day): epistaxis decreased significantly and hemoglobin increased significantly, with discontinuation in 2 patients. URL: https://doi.org/10.3390/jcm12237410. (alvarezhernandez2023tacrolimusasa pages 1-2)

Mechanistic rationale described includes increased endoglin/ALK1 expression and stimulation of BMP9/TGF-β1/ALK1 signaling with SMAD4 translocation and downstream gene changes (e.g., ID1), supporting endothelial pathway restoration as a therapeutic strategy. (alvarezhernandez2023tacrolimusasa pages 2-4)

MAXO suggestions:
- calcineurin inhibitor therapy; treatment of epistaxis; treatment of gastrointestinal hemorrhage (conceptual).

#### Bevacizumab (anti-VEGF) — systemic and local
A 2024 epistaxis review summarizes evidence that systemic IV bevacizumab can yield clinically meaningful ESS improvements in large cohorts (e.g., in an analysis of 143 patients, mean ESS fell by **3.37 points** and **92%** had clinically meaningful ESS reduction), though adverse events can lead to discontinuation. (ahmad2024managingepistaxisin pages 3-3)

The mechanistic rationale for targeting VEGF is also supported by pathway crosstalk noted in mechanistic reviews. (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3)

MAXO suggestions:
- anti-VEGF therapy; treatment of epistaxis; treatment of gastrointestinal hemorrhage (conceptual).

### 12.3 Experimental/ongoing clinical trials (ClinicalTrials.gov)

#### Tacrolimus trial (NCT04646356)
- Phase II, open-label, single-group (Unity Health Toronto)
- Actual start: 2020-10-20; primary completion: 2024-01-15; completion: 2024-10-21; last update posted 2025-04-01
- Enrollment: 10
- Primary endpoint: weekly minutes of epistaxis over a long follow-up window with diary capture
URL: https://clinicaltrials.gov/study/NCT04646356 (registry-derived). (NCT04646356 chunk 1)

#### Pazopanib randomized trial (NCT03850964)
- Phase 2/3 randomized, quadruple-masked, placebo-controlled
- Start: 2023-05-08; primary completion: 2025-11-21; estimated completion: Jul 2026
- Enrollment: 70
- Primary endpoints include ≥50% decrease in epistaxis duration and ≥2 g/dL hemoglobin increase (weeks 19–24 vs baseline)
URL: https://clinicaltrials.gov/study/NCT03850964 (registry-derived). (NCT03850964 chunk 1)

## 13. Prevention
Primary prevention is not generally applicable for a dominantly inherited Mendelian disorder, but secondary/tertiary prevention is central.

Key tertiary prevention strategy: systematic screening and management of visceral AVMs to prevent stroke/abscess/hemorrhage and high-output cardiac failure. Implementation gaps are documented by registry data showing low adherence to recommended screening in one national cohort. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11)

## 14. Other species / natural disease
No naturally occurring non-human HHT cases were retrieved in this tool run.

## 15. Model organisms

### 15.1 Genetic and induced models
Mechanistic reviews report that **Eng+/–** or **Alk1+/–** mouse models can develop AVMs in the presence of angiogenic/inflammatory triggers (e.g., wounding, VEGF, LPS), supporting a two-hit paradigm and providing platforms for testing anti-VEGF interventions. (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3)

### 15.2 Model utility and limitations
These models recapitulate key features of focal AVM formation and response to angiogenic modulation, but human lesion heterogeneity and multi-organ natural history remain incompletely modeled.

## Figure/Table evidence: Curaçao criteria (cropped from a 2024 review)
The following cropped table is direct evidence for diagnostic criteria and is suitable for knowledge-base encoding. (ahmad2024managingepistaxisin media 4cb59254)

---

# Notes on evidence gaps (limitations of this tool run)
- **ICD-10/ICD-11, MeSH Unique ID, MONDO ID** were not explicitly present in retrieved excerpts and therefore are not provided with citations.
- Some high-priority guideline sources (e.g., “Second International Guidelines for the Diagnosis and Management of HHT”) were not retrieved as full text in this run, limiting guideline-level specificity for screening intervals and prophylaxis recommendations.



References

1. (tabosh2024hereditaryhemorrhagictelangiectasia pages 1-2): Tala Al Tabosh, Mohammad Al Tarrass, Laura Tourvieilhe, Alexandre Guilhem, Sophie Dupuis-Girod, and Sabine Bailly. Hereditary hemorrhagic telangiectasia: from signaling insights to therapeutic advances. Journal of Clinical Investigation, Feb 2024. URL: https://doi.org/10.1172/jci176379, doi:10.1172/jci176379. This article has 67 citations and is from a highest quality peer-reviewed journal.

2. (ahmad2024managingepistaxisin pages 1-2): Youssef El Sayed Ahmad, S. Kajal, and Akaber M. Halawi. Managing epistaxis in hereditary haemorrhagic telangiectasia: a comprehensive narrative review of therapeutic horizons. The Journal of Laryngology & Otology, 139:389-394, Nov 2024. URL: https://doi.org/10.1017/s0022215124002093, doi:10.1017/s0022215124002093. This article has 1 citations.

3. (villanueva2024minimalencephalopathyin pages 1-2): B. Villanueva, A. Cañabate, R. Torres-Iglesias, P. Cerdà, E. Gamundí, Q. Ordi, E. Alba, L. A. Sanz-Astier, A. Iriarte, J. Ribas, J. Castellote, X. Pintó, and A. Riera-Mestre. Minimal encephalopathy in hereditary hemorrhagic telangiectasia patients with portosystemic vascular malformations. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03493-3, doi:10.1186/s13023-024-03493-3. This article has 2 citations and is from a peer-reviewed journal.

4. (danesino2023hereditaryhemorrhagictelangiectasia pages 1-2): Cesare Danesino, Claudia Cantarini, and Carla Olivieri. Hereditary hemorrhagic telangiectasia in pediatric age: focus on genetics and diagnosis. Pediatric Reports, 15:129-142, Feb 2023. URL: https://doi.org/10.3390/pediatric15010011, doi:10.3390/pediatric15010011. This article has 23 citations.

5. (alsamkari2024pomalidomideforepistaxis pages 1-3): Hanny Al-Samkari, Raj S. Kasthuri, Vivek N. Iyer, Allyson M. Pishko, Jake E. Decker, Clifford R. Weiss, Kevin J. Whitehead, Miles B. Conrad, Marc S. Zumberg, Jenny Y. Zhou, Joseph Parambil, Derek Marsh, Marianne Clancy, Lauren Bradley, Lisa Wisniewski, Benjamin A. Carper, Sonia M. Thomas, and Keith R. McCrae. Pomalidomide for epistaxis in hereditary hemorrhagic telangiectasia. New England Journal of Medicine, 391:1015-1027, Sep 2024. URL: https://doi.org/10.1056/nejmoa2312749, doi:10.1056/nejmoa2312749. This article has 38 citations and is from a highest quality peer-reviewed journal.

6. (alvarezhernandez2023tacrolimusasa pages 1-2): Paloma Álvarez-Hernández, José Luis Patier, Sol Marcos, Vicente Gómez del Olmo, Laura Lorente-Herraiz, Lucía Recio-Poveda, Luisa María Botella, Adrián Viteri-Noël, and Virginia Albiñana. Tacrolimus as a promising drug for epistaxis and gastrointestinal bleeding in hht. Journal of Clinical Medicine, 12:7410, Nov 2023. URL: https://doi.org/10.3390/jcm12237410, doi:10.3390/jcm12237410. This article has 9 citations.

7. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 1-6): Z. Criscuolo, C. Chiesa, G. Losada, B. Marsiglia, L. Matta, R. Nogara, H. Pereira, S. Rodriguez, R. Mezzano, and S. Ruiz. Hereditary hemorrhagic telangiectasia in uruguay: epidemiologic and clinical features of the evaluated population. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.18.25333772, doi:10.1101/2025.08.18.25333772. This article has 0 citations.

8. (gong2025quantifyingtheburden pages 1-2): Anna J. Gong, Marisabel Linares Bolsegui, Emerson E. Lee, Matthew R. Tan, Yong Zeng, Jianqiao Ma, Prateek C. Gowda, Tushar Garg, and Clifford R. Weiss. Quantifying the burden of hereditary hemorrhagic telangiectasia on quality of life and psychological health: a cross-sectional study. Orphanet Journal of Rare Diseases, Mar 2025. URL: https://doi.org/10.1186/s13023-025-03620-8, doi:10.1186/s13023-025-03620-8. This article has 2 citations and is from a peer-reviewed journal.

9. (ochiai2026acaseof pages 5-6): Sawako Ochiai, Reimon Yamaguchi, Kiminobu Takeda, Naoto Oishi, Sumihito Togi, Hiroki Ura, Yo Niida, and Akira Shimizu. A case of hereditary hemorrhagic telangiectasia with &lt;i&gt;acvrl1&lt;/i&gt; gene variant. Dermatology Reports, Mar 2026. URL: https://doi.org/10.4081/dr.2026.10582, doi:10.4081/dr.2026.10582. This article has 0 citations.

10. (jain2023pathogenicvariantfrequencies pages 2-4): Kinshuk Jain, Sarah C. McCarley, Ghazel Mukhtar, Anna Ferlin, Andrew Fleming, Deborah J. Morris-Rosendahl, and Claire L. Shovlin. Pathogenic variant frequencies in hereditary haemorrhagic telangiectasia support clinical evidence of protection from myocardial infarction. Journal of Clinical Medicine, 13:250, Dec 2023. URL: https://doi.org/10.3390/jcm13010250, doi:10.3390/jcm13010250. This article has 9 citations.

11. (ahmad2024managingepistaxisin media 4cb59254): Youssef El Sayed Ahmad, S. Kajal, and Akaber M. Halawi. Managing epistaxis in hereditary haemorrhagic telangiectasia: a comprehensive narrative review of therapeutic horizons. The Journal of Laryngology & Otology, 139:389-394, Nov 2024. URL: https://doi.org/10.1017/s0022215124002093, doi:10.1017/s0022215124002093. This article has 1 citations.

12. (tabosh2024hereditaryhemorrhagictelangiectasia pages 2-3): Tala Al Tabosh, Mohammad Al Tarrass, Laura Tourvieilhe, Alexandre Guilhem, Sophie Dupuis-Girod, and Sabine Bailly. Hereditary hemorrhagic telangiectasia: from signaling insights to therapeutic advances. Journal of Clinical Investigation, Feb 2024. URL: https://doi.org/10.1172/jci176379, doi:10.1172/jci176379. This article has 67 citations and is from a highest quality peer-reviewed journal.

13. (whitehead2024investigationofthe pages 1-2): Kevin J. Whitehead, Doruk Toydemir, Whitney Wooderchak-Donahue, Gretchen M. Oakley, Bryan McRae, Angelica Putnam, Jamie McDonald, and Pinar Bayrak-Toydemir. Investigation of the genetic determinants of telangiectasia and solid organ arteriovenous malformation formation in hereditary hemorrhagic telangiectasia (hht). International Journal of Molecular Sciences, 25:7682, Jul 2024. URL: https://doi.org/10.3390/ijms25147682, doi:10.3390/ijms25147682. This article has 16 citations.

14. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 23-28): Z. Criscuolo, C. Chiesa, G. Losada, B. Marsiglia, L. Matta, R. Nogara, H. Pereira, S. Rodriguez, R. Mezzano, and S. Ruiz. Hereditary hemorrhagic telangiectasia in uruguay: epidemiologic and clinical features of the evaluated population. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.18.25333772, doi:10.1101/2025.08.18.25333772. This article has 0 citations.

15. (danesino2023hereditaryhemorrhagictelangiectasia pages 2-4): Cesare Danesino, Claudia Cantarini, and Carla Olivieri. Hereditary hemorrhagic telangiectasia in pediatric age: focus on genetics and diagnosis. Pediatric Reports, 15:129-142, Feb 2023. URL: https://doi.org/10.3390/pediatric15010011, doi:10.3390/pediatric15010011. This article has 23 citations.

16. (criscuolo2025hereditaryhemorrhagictelangiectasia pages 6-11): Z. Criscuolo, C. Chiesa, G. Losada, B. Marsiglia, L. Matta, R. Nogara, H. Pereira, S. Rodriguez, R. Mezzano, and S. Ruiz. Hereditary hemorrhagic telangiectasia in uruguay: epidemiologic and clinical features of the evaluated population. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.18.25333772, doi:10.1101/2025.08.18.25333772. This article has 0 citations.

17. (danesino2023hereditaryhemorrhagictelangiectasia pages 4-6): Cesare Danesino, Claudia Cantarini, and Carla Olivieri. Hereditary hemorrhagic telangiectasia in pediatric age: focus on genetics and diagnosis. Pediatric Reports, 15:129-142, Feb 2023. URL: https://doi.org/10.3390/pediatric15010011, doi:10.3390/pediatric15010011. This article has 23 citations.

18. (shovlin2020mutationalandphenotypic pages 9-10): Claire L. Shovlin, Ilenia Simeoni, Kate Downes, Zoe C. Frazer, Karyn Megy, Maria E. Bernabeu-Herrero, Abigail Shurr, Jennifer Brimley, Dilipkumar Patel, Loren Kell, Jonathan Stephens, Isobel G. Turbin, Micheala A. Aldred, Christopher J. Penkett, Willem H. Ouwehand, Luca Jovine, and Ernest Turro. Mutational and phenotypic characterization of hereditary hemorrhagic telangiectasia. Blood, 136:1907-1918, Oct 2020. URL: https://doi.org/10.1182/blood.2019004560, doi:10.1182/blood.2019004560. This article has 78 citations and is from a highest quality peer-reviewed journal.

19. (jain2023pathogenicvariantfrequencies pages 1-2): Kinshuk Jain, Sarah C. McCarley, Ghazel Mukhtar, Anna Ferlin, Andrew Fleming, Deborah J. Morris-Rosendahl, and Claire L. Shovlin. Pathogenic variant frequencies in hereditary haemorrhagic telangiectasia support clinical evidence of protection from myocardial infarction. Journal of Clinical Medicine, 13:250, Dec 2023. URL: https://doi.org/10.3390/jcm13010250, doi:10.3390/jcm13010250. This article has 9 citations.

20. (shovlin2020mutationalandphenotypic pages 23-24): Claire L. Shovlin, Ilenia Simeoni, Kate Downes, Zoe C. Frazer, Karyn Megy, Maria E. Bernabeu-Herrero, Abigail Shurr, Jennifer Brimley, Dilipkumar Patel, Loren Kell, Jonathan Stephens, Isobel G. Turbin, Micheala A. Aldred, Christopher J. Penkett, Willem H. Ouwehand, Luca Jovine, and Ernest Turro. Mutational and phenotypic characterization of hereditary hemorrhagic telangiectasia. Blood, 136:1907-1918, Oct 2020. URL: https://doi.org/10.1182/blood.2019004560, doi:10.1182/blood.2019004560. This article has 78 citations and is from a highest quality peer-reviewed journal.

21. (whitehead2024investigationofthe pages 2-3): Kevin J. Whitehead, Doruk Toydemir, Whitney Wooderchak-Donahue, Gretchen M. Oakley, Bryan McRae, Angelica Putnam, Jamie McDonald, and Pinar Bayrak-Toydemir. Investigation of the genetic determinants of telangiectasia and solid organ arteriovenous malformation formation in hereditary hemorrhagic telangiectasia (hht). International Journal of Molecular Sciences, 25:7682, Jul 2024. URL: https://doi.org/10.3390/ijms25147682, doi:10.3390/ijms25147682. This article has 16 citations.

22. (alsamkari2024pomalidomideforepistaxis pages 6-8): Hanny Al-Samkari, Raj S. Kasthuri, Vivek N. Iyer, Allyson M. Pishko, Jake E. Decker, Clifford R. Weiss, Kevin J. Whitehead, Miles B. Conrad, Marc S. Zumberg, Jenny Y. Zhou, Joseph Parambil, Derek Marsh, Marianne Clancy, Lauren Bradley, Lisa Wisniewski, Benjamin A. Carper, Sonia M. Thomas, and Keith R. McCrae. Pomalidomide for epistaxis in hereditary hemorrhagic telangiectasia. New England Journal of Medicine, 391:1015-1027, Sep 2024. URL: https://doi.org/10.1056/nejmoa2312749, doi:10.1056/nejmoa2312749. This article has 38 citations and is from a highest quality peer-reviewed journal.

23. (alvarezhernandez2023tacrolimusasa pages 2-4): Paloma Álvarez-Hernández, José Luis Patier, Sol Marcos, Vicente Gómez del Olmo, Laura Lorente-Herraiz, Lucía Recio-Poveda, Luisa María Botella, Adrián Viteri-Noël, and Virginia Albiñana. Tacrolimus as a promising drug for epistaxis and gastrointestinal bleeding in hht. Journal of Clinical Medicine, 12:7410, Nov 2023. URL: https://doi.org/10.3390/jcm12237410, doi:10.3390/jcm12237410. This article has 9 citations.

24. (ahmad2024managingepistaxisin pages 3-3): Youssef El Sayed Ahmad, S. Kajal, and Akaber M. Halawi. Managing epistaxis in hereditary haemorrhagic telangiectasia: a comprehensive narrative review of therapeutic horizons. The Journal of Laryngology & Otology, 139:389-394, Nov 2024. URL: https://doi.org/10.1017/s0022215124002093, doi:10.1017/s0022215124002093. This article has 1 citations.

25. (NCT04646356 chunk 1):  Tacrolimus Trial for Hereditary Hemorrhagic Telangiectasia (HHT). Unity Health Toronto. 2020. ClinicalTrials.gov Identifier: NCT04646356

26. (NCT03850964 chunk 1):  Effects of Pazopanib on Hereditary Hemorrhagic Telangiectasia Related Epistaxis and Anemia (Paz). Cure HHT. 2023. ClinicalTrials.gov Identifier: NCT03850964
