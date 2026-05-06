---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T13:31:44.249206'
end_time: '2026-05-06T13:44:14.690996'
duration_seconds: 750.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Marchiafava-Bignami Disease
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Marchiafava-Bignami Disease
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Marchiafava-Bignami Disease** covering all of the
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
- **Disease Name:** Marchiafava-Bignami Disease
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Marchiafava-Bignami Disease** covering all of the
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


## Comprehensive Disease Characteristics Report: Marchiafava–Bignami Disease (MBD)

### Target Disease
- **Disease name:** Marchiafava–Bignami disease (MBD)  
- **Category:** Neurological disorder (toxic-metabolic demyelinating/necrotizing disease of the corpus callosum) (singer2023diagnosisandmanagement pages 1-2, liu2024clinicalanalysisof pages 1-2)

---

## 1) Disease Information

### 1.1 Overview (current understanding)
Marchiafava–Bignami disease (MBD) is a rare neurologic disorder characterized by **demyelination and necrosis of the corpus callosum**, sometimes extending into adjacent subcortical/extra-callosal white matter. It is most strongly associated with **chronic alcohol use disorder and malnutrition**, and often presents with nonspecific neuropsychiatric symptoms that can delay diagnosis. MRI (particularly DWI) enables antemortem diagnosis and earlier treatment. (singer2023diagnosisandmanagement pages 1-2, liu2024clinicalanalysisof pages 1-2, singer2023diagnosisandmanagement pages 4-6)

**Example abstract-supported definition (direct quote):** the 2023 review describes MBD as “**characterized by… myelin degeneration and tissue necrosis**… [with]… **necrotic degeneration… in the corpus callosum**.” (published 2023-06-30; URL: https://doi.org/10.15190/d.2023.7) (singer2023diagnosisandmanagement pages 1-2)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
Authoritative ontology identifiers (e.g., Orphanet, ICD-10/ICD-11, MeSH, MONDO) were **not retrievable from the sources available in this tool run**, so they cannot be confirmed here.

### 1.3 Synonyms and alternative names
- **Marchiafava–Bignami disease** (MBD) (singer2023diagnosisandmanagement pages 1-2, liu2024clinicalanalysisof pages 1-2)
- **Primary degeneration of the corpus callosum** (used in imaging-oriented literature) (li2021diversemrifindings pages 1-3)

### 1.4 Evidence type (patient-level vs aggregated)
Most MBD knowledge is derived from **case reports/series and small retrospective cohorts**, rather than randomized clinical trials. A 2024 paper synthesized **33 cases** (3 institutional cases plus 30 published case reports) to summarize clinical characteristics. (published 2024-10; URL: https://doi.org/10.1186/s12883-024-03901-y) (liu2024clinicalanalysisof pages 1-2)

---

## 2) Etiology

### 2.1 Disease causal factors (current view)
The leading causal model is **toxic–metabolic injury** related to alcohol exposure and nutritional deficiency, particularly **thiamine (vitamin B1) depletion**, producing energy failure, cytotoxic edema, demyelination, and necrosis in myelin-rich callosal tissue. (singer2023diagnosisandmanagement pages 1-2, menrai2024anatypicalcase pages 1-2)

**Direct quote (abstract):** alcohol “**leads to thiamine depletion and disrupts various metabolic pathways**… [which] **hinders myelin synthesis**.” (Singer et al., 2023-06-30; https://doi.org/10.15190/d.2023.7) (singer2023diagnosisandmanagement pages 1-2)

### 2.2 Risk factors
**Major risk factors** include:
- **Chronic alcohol use disorder** and **malnutrition** (liu2024clinicalanalysisof pages 1-2, singer2023diagnosisandmanagement pages 1-2)
- **Thiamine/B-complex vitamin deficiency** (singer2023diagnosisandmanagement pages 1-2)

**Non-alcoholic triggers/associations** reported in reviews include diabetic ketoacidosis and osmolality shifts (“callosal myelinolysis”), post-bariatric malnutrition, sepsis, carbon monoxide poisoning, cerebral malaria, and sickle cell disease. (singer2023diagnosisandmanagement pages 2-4)

**Recent aggregated data (2017–2023 case reports):** “Most patients have a history of **alcohol consumption or malnutrition**.” (Liu et al., 2024-10; https://doi.org/10.1186/s12883-024-03901-y) (liu2024clinicalanalysisof pages 1-2)

### 2.3 Protective factors
No genetic or pharmacologic protective factors were identified in the retrieved evidence. Indirectly, **adequate nutrition** and **alcohol abstinence** are protective in the sense of removing major risk exposures. (singer2023diagnosisandmanagement pages 1-2)

### 2.4 Gene–environment interaction
No specific gene–environment interactions are established in the retrieved literature; one case report states the cause “may involve… **genetic predisposition**” but does not provide gene/variant evidence. (Conceição et al., 2024-11-06; https://doi.org/10.7759/cureus.73146) (conceicao2024marchiafavabignamidiseasea pages 1-3)

---

## 3) Phenotypes

### 3.1 Core phenotypes and frequency (human clinical evidence)
A 2024 retrospective synthesis of **33 cases** (2017–2023 case reports plus 3 institutional cases) quantified phenotype frequencies as follows (published 2024-10; https://doi.org/10.1186/s12883-024-03901-y): (liu2024clinicalanalysisof pages 2-4)
- **Movement disorder/dyskinesia:** 22/33 (66.7%) (e.g., ataxia, limb weakness) (liu2024clinicalanalysisof pages 2-4)
- **Speech disorders:** 19/33 (57.6%) (e.g., dysarthria, aphasia) (liu2024clinicalanalysisof pages 2-4)
- **Consciousness disorders:** 18/33 (54.5%) (e.g., coma, somnolence, agitation) (liu2024clinicalanalysisof pages 2-4)
- **Cognitive impairment:** 15/33 (45.5%) (liu2024clinicalanalysisof pages 2-4)
- **Emotional/personality change:** 10/33 (30.3%) (liu2024clinicalanalysisof pages 2-4)
- **Seizures:** 4/33 (12.1%) (liu2024clinicalanalysisof pages 2-4)

### 3.2 Onset age, severity, progression
- **Typical age/sex:** primarily affects **middle-aged men** in aggregated data (liu2024clinicalanalysisof pages 1-2)
- **Onset pattern:** often **acute or subacute** (liu2024clinicalanalysisof pages 1-2)
- **Temporal staging:** acute/subacute/chronic presentations are described in recent clinical literature; acute cases can include confusion/aggression/seizures, with chronic cases including progressive dementia-like syndromes. (conceicao2024marchiafavabignamidiseasea pages 3-4)

**Quantitative course distribution (33 cases):** acute 18/33 (54.5%), subacute 7/33 (21.2%), chronic 8/33 (24.2%). (liu2024clinicalanalysisof pages 2-4)

### 3.3 Suggested HPO terms (examples)
(These are ontology suggestions; exact mappings should be verified against HPO.)
- Altered level of consciousness (e.g., coma/somnolence): **HP:0001259** (common umbrella; exact term selection depends on case detail) (liu2024clinicalanalysisof pages 2-4)
- Ataxia: **HP:0001251** (liu2024clinicalanalysisof pages 2-4)
- Dysarthria: **HP:0001260** (liu2024clinicalanalysisof pages 2-4)
- Aphasia: **HP:0002381** (liu2024clinicalanalysisof pages 2-4)
- Cognitive impairment: **HP:0100543** (liu2024clinicalanalysisof pages 2-4)
- Seizures: **HP:0001250** (liu2024clinicalanalysisof pages 2-4)
- Apraxia: **HP:0002186** (liu2024clinicalanalysisof pages 2-4)
- Neuropsychiatric/behavioral abnormality (broad): consider **HP:0000708** (behavior abnormality) and/or more specific terms based on presentation (liu2024clinicalanalysisof pages 2-4)

### 3.4 Quality of life impact
Formal QoL instruments (EQ-5D/SF-36) were not identified in the retrieved literature. However, severe cases can lead to prolonged dependency and persistent deficits (e.g., neurogenic bladder, disorientation), indicating substantial functional impact. (menrai2024anatypicalcase pages 1-2)

---

## 4) Genetic / Molecular Information

### 4.1 Causal genes and pathogenic variants
MBD is **not established as a monogenic disease** in the retrieved evidence, and no causal genes/variants or ClinVar-style variant assertions were identified.

### 4.2 Mechanistic molecular pathways (non-genetic)
Mechanistic framing emphasizes metabolic and oxidative injury in callosal white matter, including:
- Thiamine depletion → impaired energy metabolism → cytotoxic edema (reflected by restricted diffusion/low ADC) → demyelination/necrosis (singer2023diagnosisandmanagement pages 4-6, singer2023diagnosisandmanagement pages 1-2)

Suggested GO biological process terms (examples; to validate in GO):
- **Myelination** (GO:0042552)
- **Axon ensheathment** (GO:0008366)
- **Response to oxidative stress** (GO:0006979)
- **Regulation of inflammatory response** (GO:0050727)

---

## 5) Environmental Information

### 5.1 Environmental/lifestyle factors
The dominant environmental/lifestyle drivers are:
- **Chronic heavy alcohol exposure** (liu2024clinicalanalysisof pages 1-2, zhang2023clinicoradiologicsubtypesand pages 1-2)
- **Malnutrition / inadequate intake** and associated vitamin deficiency (liu2024clinicalanalysisof pages 1-2)

A 2023 cohort described long drinking histories (12–29 years; ~200–250 mL/day of 40–50% liquor). (Zhang et al., 2023-10; https://doi.org/10.1038/s41598-023-45431-6) (zhang2023clinicoradiologicsubtypesand pages 1-2)

### 5.2 Infectious agents
Not a primary infectious disease; however, cerebral malaria is listed as a reported association/trigger in review literature. (singer2023diagnosisandmanagement pages 2-4)

---

## 6) Mechanism / Pathophysiology

### 6.1 Causal chain (integrated)
A clinically useful causal chain consistent with recent reviews and cohort imaging is:
1) Chronic alcohol use and/or malnutrition → thiamine depletion and metabolic disruption (singer2023diagnosisandmanagement pages 1-2)
2) Energy failure in myelin-rich callosal tracts → cytotoxic edema (restricted diffusion/low ADC on DWI) (singer2023diagnosisandmanagement pages 4-6, zhang2023clinicoradiologicsubtypesand pages 1-2)
3) Demyelination and necrosis within corpus callosum ± extracallosal white matter (singer2023diagnosisandmanagement pages 1-2, liu2024clinicalanalysisof pages 1-2)
4) Clinical syndrome: altered consciousness, dysarthria/aphasia, ataxia/weakness, cognitive and psychiatric changes, disconnection syndromes (liu2024clinicalanalysisof pages 2-4, singer2023diagnosisandmanagement pages 7-9)

### 6.2 Cell types (suggested CL terms)
Specific single-cell evidence was not found. Relevant cell types likely include:
- Oligodendrocyte (CL:0000128)
- Astrocyte (CL:0000127)
- Microglial cell (CL:0000129)

This is consistent with demyelinating pathology described in review literature (e.g., demyelination, decreased oligodendrocytes). (singer2023diagnosisandmanagement pages 4-6)

---

## 7) Anatomical Structures Affected

### 7.1 Organ/tissue localization
- **Primary:** corpus callosum (white matter commissure) (liu2024clinicalanalysisof pages 1-2, singer2023diagnosisandmanagement pages 1-2)
- **Common subregions:** splenium is frequently affected in case syntheses; anterior two-thirds and other callosal segments can be involved (liu2024clinicalanalysisof pages 1-2, conceicao2024marchiafavabignamidiseasea pages 1-3)
- **Secondary/extra-callosal involvement:** hemispheric white matter and other brain regions can be involved; extracallosal involvement correlates with severity and can be a poor prognostic feature. (singer2023diagnosisandmanagement pages 1-2, liu2024clinicalanalysisof pages 1-2, zhang2023clinicoradiologicsubtypesand pages 1-2)

Suggested UBERON terms (examples; verify in Uberon):
- Corpus callosum: **UBERON:0001877**
- Cerebral white matter: **UBERON:0016549** (or alternative white-matter term depending on ontology version)

### 7.2 Imaging illustration (MRI)
A 2024 case report provides representative MRI findings: T2/FLAIR hyperintensity of the anterior two-thirds of the corpus callosum with restricted diffusion on DWI/ADC consistent with acute edema/demyelination. (Conceição et al., 2024-11-06; https://doi.org/10.7759/cureus.73146) (conceicao2024marchiafavabignamidiseasea media 16521e3e, conceicao2024marchiafavabignamidiseasea media 7c11b093, conceicao2024marchiafavabignamidiseasea media 8bf57d9d)

---

## 8) Temporal Development

### 8.1 Onset
Commonly **acute or subacute**, though chronic forms occur. (liu2024clinicalanalysisof pages 1-2)

### 8.2 Progression and staging
Clinical literature commonly describes acute/subacute/chronic courses; the 2024 case report summarizes stage-associated symptom patterns (acute confusion/seizures; subacute dysarthria/apraxia/ataxia; chronic global dementia/behavioral changes). (conceicao2024marchiafavabignamidiseasea pages 3-4)

---

## 9) Inheritance and Population

### 9.1 Inheritance
No Mendelian inheritance pattern is established; disease is best characterized as **acquired/toxic-metabolic** in the retrieved evidence.

### 9.2 Epidemiology
Population prevalence/incidence estimates were not identified in the retrieved sources. The 2023 review notes rarity and describes a historical compilation of ~250 cases before 2001. (singer2023diagnosisandmanagement pages 2-4)

---

## 10) Diagnostics

### 10.1 Imaging
- **MRI is the diagnostic gold standard** for demonstrating callosal lesions in MBD. (singer2023diagnosisandmanagement pages 1-2, conceicao2024marchiafavabignamidiseasea pages 3-4)
- **DWI** is emphasized for early lesion detection and shows restricted diffusion with low ADC, supporting acute cytotoxic edema. (singer2023diagnosisandmanagement pages 4-6, zhang2023clinicoradiologicsubtypesand pages 1-2)
- The **“sandwich sign”** (central callosal lesion with sparing of dorsal and ventral layers) is described as a hallmark imaging pattern in acute disease. (menrai2024anatypicalcase pages 2-3, cm2017theimportanceof pages 1-3)

### 10.2 Laboratory testing / biomarkers
No validated disease-specific biomarker panel is established; labs often reflect nutritional and alcohol-related abnormalities and are used to evaluate deficiencies and exclude mimics. A 2024 case report found macrocytic anemia, folate deficiency, mild hypoalbuminemia, and elevated GGT. (conceicao2024marchiafavabignamidiseasea pages 1-3)

### 10.3 Differential diagnosis
A 2023 review provides a broad differential including Wernicke encephalopathy, vitamin B12/folate deficiency, metabolic/toxic etiologies, central myelinolysis, MS, infection/encephalitis, tumors, and systemic organ failure syndromes. (Singer et al., 2023-06-30; https://doi.org/10.15190/d.2023.7) (singer2023diagnosisandmanagement pages 7-9)

---

## 11) Outcome / Prognosis

### 11.1 Prognostic factors
Poor outcome predictors emphasized in reviews and recent cases include:
- **Severe consciousness disturbance/low GCS** (menrai2024anatypicalcase pages 1-2)
- **Extensive cerebral cortex or extracallosal involvement** (singer2023diagnosisandmanagement pages 1-2, zhang2023clinicoradiologicsubtypesand pages 1-2)
- Delayed treatment; earlier thiamine is associated with better outcomes in review literature (singer2023diagnosisandmanagement pages 7-9)

### 11.2 Quantitative outcome data from cohorts
- In a 2023 acute cohort (n=23), Heinrich Type A vs B differed in admission MoCA and extracallosal involvement, but authors concluded prognosis could still be favorable with combined treatment and lesions could resolve. (Zhang et al., 2023-10; https://doi.org/10.1038/s41598-023-45431-6) (zhang2023clinicoradiologicsubtypesand pages 1-2)
- In a 17-patient acute MRI cohort, neuropsychiatric sequelae were reported in 5 cases overall, with higher sequelae in the most focal diffusion subtype (Type III: 60%). (Li et al., accepted 2020-06-16, published 2021-07; https://doi.org/10.1177/0284185120943040) (li2021diversemrifindings pages 1-3)

### 11.3 Mortality statistic (from review literature)
A 2020 BMJ Case Reports review reports that MRI-enabled diagnosis and earlier thiamine treatment improved prognosis “from frequently fatal to a **mortality of less than 8%**,” and that thiamine administered within 14 days is associated with statistically better outcomes. (Kinsley et al., 2020-12; https://doi.org/10.1136/bcr-2020-238187) (singer2023diagnosisandmanagement pages 1-2)

---

## 12) Treatment

### 12.1 Core pharmacotherapy (real-world implementation)
There are no universally accepted treatment guidelines, but convergent expert consensus and practice patterns support:
- **Immediate high-dose parenteral thiamine** and **B-complex vitamin replacement** as first-line therapy (singer2023diagnosisandmanagement pages 1-2, conceicao2024marchiafavabignamidiseasea pages 3-4)
- **Nutritional rehabilitation** and **alcohol cessation/withdrawal management** (zhang2023clinicoradiologicsubtypesand pages 1-2)
- **Rehabilitation therapies** (physical/occupational/speech as indicated) (menrai2024anatypicalcase pages 1-2)

**Example thiamine dosing used in a 2023 cohort:** IV thiamine **500 mg/day** plus methylprednisolone pulse **500–1000 mg/day** for 3–5 days, then oral prednisone and compound B vitamins, with follow-up oral B vitamins and alcohol withdrawal. (Zhang et al., 2023-10; https://doi.org/10.1038/s41598-023-45431-6) (zhang2023clinicoradiologicsubtypesand pages 1-2)

**Example dosing in a 2024 case report:** IV thiamine **500 mg three times daily for 3 days**, then **250 mg IV daily for 5 days**, then **100 mg orally daily**, plus B6/B9/B12 and rehabilitation. (Conceição et al., 2024-11-06; https://doi.org/10.7759/cureus.73146) (conceicao2024marchiafavabignamidiseasea pages 3-4)

### 12.2 Corticosteroids (evidence status)
Corticosteroids are frequently co-administered to address edema/inflammation, but reviews emphasize heterogeneous evidence and confounding by simultaneous vitamin therapy; thiamine remains the most consistently recommended intervention. (singer2023diagnosisandmanagement pages 7-9, singer2023diagnosisandmanagement pages 4-6)

### 12.3 Suggested MAXO terms (examples)
(Verify exact MAXO identifiers in MAXO.)
- Thiamine supplementation / vitamin B supplementation (zhang2023clinicoradiologicsubtypesand pages 1-2, conceicao2024marchiafavabignamidiseasea pages 3-4)
- Corticosteroid therapy (zhang2023clinicoradiologicsubtypesand pages 1-2)
- Nutritional rehabilitation (liu2024clinicalanalysisof pages 1-2)
- Alcohol cessation counseling / substance use treatment (zhang2023clinicoradiologicsubtypesand pages 1-2)
- Rehabilitation therapy (menrai2024anatypicalcase pages 1-2)

---

## 13) Prevention

Primary prevention is largely exposure-based:
- Prevent chronic malnutrition and vitamin deficiency in high-risk populations (alcohol use disorder, poor intake, post-surgical malabsorption) (liu2024clinicalanalysisof pages 1-2)
- Early empiric thiamine in suspected deficiency states (modelled after Wernicke-Korsakoff practice patterns in reviews) (singer2023diagnosisandmanagement pages 4-6)

Secondary prevention is essentially **early recognition** (MRI use in appropriate presentations) to prevent irreversible injury. (singer2023diagnosisandmanagement pages 1-2)

---

## 14) Other Species / Natural Disease
No naturally occurring MBD analogs in non-human species were identified in the retrieved evidence.

---

## 15) Model Organisms
No validated disease-specific animal models were identified in the retrieved evidence. Mechanistic hypotheses largely extrapolate from thiamine deficiency and alcohol neurotoxicity biology rather than MBD-specific models.

---

## Recent Developments (2023–2024 highlight)
1) **Clinico-radiologic subtyping with treatment response**: a 2023 cohort (n=23) validated Heinrich Type A/B comparisons and reported complete clinico-radiologic recovery with combined therapy, emphasizing reversibility. (Zhang et al., 2023-10; https://doi.org/10.1038/s41598-023-45431-6) (zhang2023clinicoradiologicsubtypesand pages 1-2)
2) **Updated aggregated phenotype frequencies and onset distributions**: a 2024 synthesis of 33 cases quantified symptom frequencies and reinforced extracallosal lesion burden as a poor prognostic marker. (Liu et al., 2024-10; https://doi.org/10.1186/s12883-024-03901-y) (liu2024clinicalanalysisof pages 2-4)

---

## Current Applications / Real-World Implementations
- **Emergency and inpatient neurology**: MRI (especially DWI) to distinguish MBD from stroke and other toxic-metabolic encephalopathies, followed by empiric high-dose thiamine and supportive care. (singer2023diagnosisandmanagement pages 1-2, conceicao2024marchiafavabignamidiseasea pages 1-3)
- **Monitoring and prognosis**: DWI lesion extent and extracallosal involvement used as practical indicators of severity and potential outcome. (zhang2023clinicoradiologicsubtypesand pages 1-2, liu2024clinicalanalysisof pages 1-2)

---

## Clinical Trials (translation status)
No MBD-specific therapeutic trials were identified. One interventional trial relevant to corpus callosum demyelination is:
- **NCT06065670** (ClinicalTrials.gov): “Assessing Changes in Multi-parametric MRI in Patients With Acute Demyelinating Lesions Taking Clemastine Fumarate as a Myelin Repair Therapy” (UCSF). **Status:** Not yet recruiting; **estimated start:** 2026-09-15; **Phase:** 1/2; **n≈44**. The trial targets acute demyelinating lesions broadly (e.g., MS-related) with corpus callosum myelin MRI outcomes; MBD appears in condition taxonomy but the study is not clearly MBD-specific. URL (ClinicalTrials.gov): https://clinicaltrials.gov/study/NCT06065670 (NCT06065670 chunk 1, NCT06065670 chunk 4)

---

## Summary Table (evidence-synthesized)
| Domain | Key facts | Quantitative details / examples | Evidence |
|---|---|---|---|
| Definition | Rare neurologic disorder characterized by demyelination and necrosis of the corpus callosum, often with adjacent subcortical/extra-callosal white matter involvement; classically linked to chronic alcohol use and malnutrition. | Older literature cited in recent reviews suggests only ~250 published cases before 2001; a 2024 review article notes ~300 cases worldwide. | (singer2023diagnosisandmanagement pages 1-2, liu2024clinicalanalysisof pages 1-2, menrai2024anatypicalcase pages 1-2, conceicao2024marchiafavabignamidiseasea pages 1-3) |
| Disease context / data source | Evidence is largely from aggregated disease-level reviews plus retrospective analyses of published case reports and small hospital cohorts, rather than EHR-scale datasets or randomized trials. | 33-case retrospective synthesis (3 local + 30 published cases, 2017–2023); 23-patient acute MBD cohort; 17-patient MRI cohort. | (liu2024clinicalanalysisof pages 1-2, zhang2023clinicoradiologicsubtypesand pages 1-2, li2021diversemrifindings pages 1-3) |
| Typical triggers / risk factors | Chronic alcohol use disorder, malnutrition, thiamine/B-complex deficiency; also reported after GI surgery, anorexia, unbalanced diet, post-bariatric malnutrition, diabetic ketoacidosis/callosal myelinolysis, sepsis, carbon monoxide poisoning, cerebral malaria, and sickle cell disease. | In a 23-patient acute cohort, drinking history was 12–29 years with ~200–250 mL/day of 40–50% liquor; in a 17-patient cohort, 12–45 years with ~250–500 mL/day. | (liu2024clinicalanalysisof pages 1-2, singer2023diagnosisandmanagement pages 1-2, zhang2023clinicoradiologicsubtypesand pages 1-2, li2021diversemrifindings pages 1-3) |
| Pathophysiologic understanding | Leading mechanisms include alcohol neurotoxicity, oxidative stress, thiamine depletion with energy failure, impaired myelin synthesis, cytotoxic edema, blood-brain-barrier dysfunction, demyelination, and necrosis. Extra-callosal involvement likely reflects more severe diffuse injury. | Reviews emphasize low ADC/restricted diffusion as a marker of cytotoxic edema that may precede necrosis; poor outcome linked to widespread cortical/extra-callosal disease. | (singer2023diagnosisandmanagement pages 1-2, singer2023diagnosisandmanagement pages 4-6, menrai2024anatypicalcase pages 1-2) |
| Onset / course | Acute, subacute, or chronic presentations occur; acute/subacute onset is common in contemporary series. | In the 33-case synthesis: acute 18/33 (54.5%), subacute 7/33 (21.2%), chronic 8/33 (24.2%). | (liu2024clinicalanalysisof pages 2-4) |
| Core clinical phenotypes | Disturbance of consciousness, dysarthria/aphasia, cognitive impairment, psychiatric/behavioral change, ataxia, weakness, seizures, apraxia/neglect, and interhemispheric disconnection syndrome. | In 33 cases: dyskinesia 22/33 (66.7%), speech disorders 19/33 (57.6%), consciousness disorders 18/33 (54.5%), cognitive impairment 15/33 (45.5%), emotional/personality change 10/33 (30.3%), seizures 4/33 (12.1%), sensory disturbance 3/33, neglect 2/33, apraxia 4/33, callosal disconnection 2/33. Among acute-onset cases: consciousness disorders 14/18 (77.8%), speech disorders 12/18 (66.7%), movement disorders 11/18 (61.1%). | (liu2024clinicalanalysisof pages 1-2, liu2024clinicalanalysisof pages 2-4) |
| Common lesion locations | Symmetric corpus callosum lesions are typical; splenium is often most commonly affected in mixed case series, but genu/body and anterior two-thirds involvement also occur; lesions may extend to hemispheric white matter, internal capsule, basal ganglia, and other extra-callosal regions. | 2024 synthesis: splenium most commonly affected; broader lesion distribution associated with worse prognosis. Case imaging examples show anterior 2/3 callosal involvement with mild splenial involvement and DWI restriction. | (liu2024clinicalanalysisof pages 1-2, conceicao2024marchiafavabignamidiseasea pages 1-3, li2021diversemrifindings pages 1-3, singer2023diagnosisandmanagement pages 1-2) |
| Key MRI findings | MRI is the diagnostic gold standard. Typical findings are T1 hypointensity and T2/FLAIR hyperintensity in callosal lesions; DWI detects early lesions and shows restricted diffusion with low ADC in acute disease. | Restricted diffusion defined as DWI hyperintensity with ADC hypointensity; examples documented in anterior 2/3 of corpus callosum and splenium. | (singer2023diagnosisandmanagement pages 1-2, zhang2023clinicoradiologicsubtypesand pages 1-2, conceicao2024marchiafavabignamidiseasea pages 1-3, li2021diversemrifindings pages 1-3) |
| Signature imaging sign | “Sandwich sign”: central callosal lesion with sparing of dorsal and ventral layers, especially described in acute disease and often highlighted on sagittal imaging. | Recent and prior reviews describe it as a hallmark/pathognomonic sign of acute MBD. | (menrai2024anatypicalcase pages 2-3, cm2017theimportanceof pages 1-3, li2021diversemrifindings pages 1-3) |
| Imaging-based evolution | Acute lesions may show swelling and extensive diffusion restriction; follow-up can show radiologic resolution, but some cases evolve to callosal atrophy or cavitation, especially with more focal/heterogeneous callosal injury. | In the 17-patient MRI cohort, callosal atrophy/cavitation occurred in 0% of Type I, 20% of Type II, and 60% of Type III cases. | (li2021diversemrifindings pages 1-3) |
| Heinrich clinicoradiologic subtype A/B | Type A: diffuse/entire callosal involvement with more severe early presentation; Type B: focal callosal involvement with milder presentation. | In the 23-patient cohort: Type A n=12, Type B n=11; admission MoCA 16.50±1.73 vs 18.27±1.68 (P=0.021); extracallosal involvement 66.67% vs 18.18% (P=0.036); illness duration 18.3±2.1 vs 15.6±2.4 days (P=0.012); residual splenial lesion during treatment 58.33% vs 9.09% (P=0.027). Authors concluded subtype related to early severity, not final prognosis, with recovery possible in both. | (zhang2023clinicoradiologicsubtypesand pages 1-2) |
| MRI diffusion-range subtype I/II/III | Type I = complete callosal restricted diffusion; Type II = mostly involved; Type III = partial involvement. Greater diffusion extent was associated with more extracallosal lesions but fewer chronic sequelae, while more focal/heterogeneous lesions had more atrophy/cavitation and sequelae. | Extracallosal involvement: Type I 6/7 (86%), Type II 3/5 (60%), Type III 1/5 (20%). Neuropsychiatric sequelae at follow-up: Type I 1/7 (14%), Type II 1/5 (20%), Type III 3/5 (60%). | (li2021diversemrifindings pages 1-3) |
| Laboratory / ancillary findings | Routine labs may be normal or show nutritional/alcohol-related abnormalities; testing helps exclude mimics. Reported abnormalities include macrocytic anemia, folate deficiency, hypoalbuminemia, liver enzyme elevation. | Example case: Hb 10.7 g/dL, MCV 110.1 fL, folate <0.6 ng/mL, GGT 131 U/L, albumin 3.35 g/dL. | (conceicao2024marchiafavabignamidiseasea pages 1-3) |
| Differential diagnosis | Wernicke encephalopathy, vitamin B12/folate deficiency syndromes, multiple sclerosis, central pontine/extrapontine myelinolysis, encephalitis/meningitis, seizures/epilepsy-related lesions, metabolic/toxic encephalopathies, tumors, dementia syndromes, hepatic/renal/respiratory failure, sepsis, delirium. | Differentiation relies on alcoholism/malnutrition context, more persistent severe cognitive-motor syndrome, and characteristic callosal MRI lesions. | (singer2023diagnosisandmanagement pages 7-9, singer2023diagnosisandmanagement pages 1-2) |
| First-line treatment | Prompt parenteral thiamine/B-complex vitamin replacement is the mainstay; alcohol cessation, nutritional rehabilitation, and supportive multidisciplinary care are standard. | Example regimens reported: thiamine 500 mg/day IV for 3–5 days with steroids, then oral B vitamins; alternative review regimen 100–250 mg IV/IM daily for 3–5 days, then 100 mg PO TID for 1–2 weeks, then 100 mg daily maintenance; case regimen 500 mg IV three times daily for 3 days, then 250 mg IV daily for 5 days, then 100 mg PO daily. | (zhang2023clinicoradiologicsubtypesand pages 1-2, singer2023diagnosisandmanagement pages 4-6, conceicao2024marchiafavabignamidiseasea pages 3-4) |
| Corticosteroids / adjuncts | Corticosteroids are used in many reports to address edema, demyelination, and inflammation, but evidence is heterogeneous and confounded by concurrent vitamin therapy. Rehabilitation and nutritional support are commonly added. | Example steroid regimens: methylprednisolone 500–1000 mg/day for 3–5 days followed by oral prednisone 60 mg/day taper; dexamethasone 4 mg every 12 h in one severe case. | (zhang2023clinicoradiologicsubtypesand pages 1-2, singer2023diagnosisandmanagement pages 1-2, menrai2024anatypicalcase pages 1-2) |
| Treatment response | Improvement can be substantial and radiologically reversible when recognized early; however, partial recovery with chronic neuropsychiatric deficits also occurs. | In the 23-patient cohort, MoCA improved over time in both subtypes (P<0.001) and callosal/extracallosal lesions disappeared completely. A 2024 case regained coherent speech and independent walking after 1 month of treatment; another severe 2024 case had minimal improvement at 1 year. | (zhang2023clinicoradiologicsubtypesand pages 1-2, conceicao2024marchiafavabignamidiseasea pages 1-3, menrai2024anatypicalcase pages 1-2) |
| Prognostic factors | Worse prognosis is associated with extensive extra-callosal/cortical involvement, severe consciousness disturbance or low GCS, broader lesion burden, and delayed treatment. Earlier thiamine appears beneficial. | Review notes MBD co-occurs with Wernicke disease in ~15–20% of cases. Early thiamine reduced unfavorable outcomes; a BMJ review article cited mortality of <8% in the MRI era and better outcomes when thiamine was given within 14 days of symptom onset. | (singer2023diagnosisandmanagement pages 1-2, singer2023diagnosisandmanagement pages 4-6, menrai2024anatypicalcase pages 1-2) |
| Real-world implementation / recent developments | Current real-world practice is MRI-based diagnosis plus empiric high-dose thiamine, vitamins, alcohol withdrawal, and rehabilitation. Recent research includes retrospective clinico-radiologic subtype studies and exploratory AI/MRI detection work, but no disease-specific therapeutic trials were identified in the retrieved evidence. | 2023–2024 literature emphasizes MRI/DWI-guided diagnosis, subtype-outcome correlation, and reversibility with combined therapy. | (zhang2023clinicoradiologicsubtypesand pages 1-2, liu2024clinicalanalysisof pages 1-2, singer2023diagnosisandmanagement pages 1-2) |


*Table: This table summarizes clinically useful, literature-derived facts about Marchiafava-Bignami disease for a disease knowledge base, including phenotypes, MRI patterns, classifications, treatment, and prognosis. It prioritizes recent 2023–2024 evidence while incorporating key quantitative findings from small cohorts and case syntheses.*

---

## Notes on PMID requirement
Several key items above come from open-access journals and case reports where the **PMID was not available in the retrieved text** during this tool run; therefore, DOI/URL and publication dates are provided as stable identifiers instead. (singer2023diagnosisandmanagement pages 1-2, liu2024clinicalanalysisof pages 1-2, zhang2023clinicoradiologicsubtypesand pages 1-2)

References

1. (singer2023diagnosisandmanagement pages 1-2): Emad Singer, Kinal Bhatt, Adesh Prashad, Larri Rudman, Islam Gadelmoula, and George Michel. Diagnosis and management of marchiafava-bignami disease, a rare neurological complication of long-term alcohol abuse. Discoveries, 11:e168, Jun 2023. URL: https://doi.org/10.15190/d.2023.7, doi:10.15190/d.2023.7. This article has 11 citations.

2. (liu2024clinicalanalysisof pages 1-2): Cong Liu, Hualong Wang, Bingchuan Xie, Shujuan Tian, and Yan Ding. Clinical analysis of marchiafava-bignami disease. BMC Neurology, Oct 2024. URL: https://doi.org/10.1186/s12883-024-03901-y, doi:10.1186/s12883-024-03901-y. This article has 7 citations and is from a peer-reviewed journal.

3. (singer2023diagnosisandmanagement pages 4-6): Emad Singer, Kinal Bhatt, Adesh Prashad, Larri Rudman, Islam Gadelmoula, and George Michel. Diagnosis and management of marchiafava-bignami disease, a rare neurological complication of long-term alcohol abuse. Discoveries, 11:e168, Jun 2023. URL: https://doi.org/10.15190/d.2023.7, doi:10.15190/d.2023.7. This article has 11 citations.

4. (li2021diversemrifindings pages 1-3): Wei Li, Chao Ran, and Jun Ma. Diverse mri findings and clinical outcomes of acute marchiafava-bignami disease. Acta Radiologica, 62:904-908, Jul 2021. URL: https://doi.org/10.1177/0284185120943040, doi:10.1177/0284185120943040. This article has 11 citations and is from a peer-reviewed journal.

5. (menrai2024anatypicalcase pages 1-2): Devika Menrai, Shyam Kiran Gandam Venkata, Sudeep Chakravarthy Bhuram, and Sai Sruthi Bhuram. An atypical case of marchiafava-bignami disease in a young chronic alcoholic: challenges in diagnosis and prognosis. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75468, doi:10.7759/cureus.75468. This article has 1 citations.

6. (singer2023diagnosisandmanagement pages 2-4): Emad Singer, Kinal Bhatt, Adesh Prashad, Larri Rudman, Islam Gadelmoula, and George Michel. Diagnosis and management of marchiafava-bignami disease, a rare neurological complication of long-term alcohol abuse. Discoveries, 11:e168, Jun 2023. URL: https://doi.org/10.15190/d.2023.7, doi:10.15190/d.2023.7. This article has 11 citations.

7. (conceicao2024marchiafavabignamidiseasea pages 1-3): Paulo Conceição, Tânia Lopes, Vasco Abreu, and Ana Reinas. Marchiafava-bignami disease: a case report of a reversible cause of dementia. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73146, doi:10.7759/cureus.73146. This article has 0 citations.

8. (liu2024clinicalanalysisof pages 2-4): Cong Liu, Hualong Wang, Bingchuan Xie, Shujuan Tian, and Yan Ding. Clinical analysis of marchiafava-bignami disease. BMC Neurology, Oct 2024. URL: https://doi.org/10.1186/s12883-024-03901-y, doi:10.1186/s12883-024-03901-y. This article has 7 citations and is from a peer-reviewed journal.

9. (conceicao2024marchiafavabignamidiseasea pages 3-4): Paulo Conceição, Tânia Lopes, Vasco Abreu, and Ana Reinas. Marchiafava-bignami disease: a case report of a reversible cause of dementia. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73146, doi:10.7759/cureus.73146. This article has 0 citations.

10. (zhang2023clinicoradiologicsubtypesand pages 1-2): Yan-li Zhang, Chao Ran, Chao Xu, and Wei Li. Clinico-radiologic subtypes and therapeutic observation of acute marchiafava-bignami disease. Scientific Reports, Oct 2023. URL: https://doi.org/10.1038/s41598-023-45431-6, doi:10.1038/s41598-023-45431-6. This article has 8 citations and is from a peer-reviewed journal.

11. (singer2023diagnosisandmanagement pages 7-9): Emad Singer, Kinal Bhatt, Adesh Prashad, Larri Rudman, Islam Gadelmoula, and George Michel. Diagnosis and management of marchiafava-bignami disease, a rare neurological complication of long-term alcohol abuse. Discoveries, 11:e168, Jun 2023. URL: https://doi.org/10.15190/d.2023.7, doi:10.15190/d.2023.7. This article has 11 citations.

12. (conceicao2024marchiafavabignamidiseasea media 16521e3e): Paulo Conceição, Tânia Lopes, Vasco Abreu, and Ana Reinas. Marchiafava-bignami disease: a case report of a reversible cause of dementia. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73146, doi:10.7759/cureus.73146. This article has 0 citations.

13. (conceicao2024marchiafavabignamidiseasea media 7c11b093): Paulo Conceição, Tânia Lopes, Vasco Abreu, and Ana Reinas. Marchiafava-bignami disease: a case report of a reversible cause of dementia. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73146, doi:10.7759/cureus.73146. This article has 0 citations.

14. (conceicao2024marchiafavabignamidiseasea media 8bf57d9d): Paulo Conceição, Tânia Lopes, Vasco Abreu, and Ana Reinas. Marchiafava-bignami disease: a case report of a reversible cause of dementia. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73146, doi:10.7759/cureus.73146. This article has 0 citations.

15. (menrai2024anatypicalcase pages 2-3): Devika Menrai, Shyam Kiran Gandam Venkata, Sudeep Chakravarthy Bhuram, and Sai Sruthi Bhuram. An atypical case of marchiafava-bignami disease in a young chronic alcoholic: challenges in diagnosis and prognosis. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75468, doi:10.7759/cureus.75468. This article has 1 citations.

16. (cm2017theimportanceof pages 1-3): Pontes Cm, M. Cagy, R. Santos, and Soares Cn. The importance of brain mri in the diagnosis of marchiafava-bignami disease. Journal of Neurology and Neurological Disorders, Aug 2017. URL: https://doi.org/10.15744/2454-4981.3.201, doi:10.15744/2454-4981.3.201. This article has 1 citations.

17. (NCT06065670 chunk 1):  Assessing Changes in Multi-parametric MRI in Patients With Acute Demyelinating Lesions Taking Clemastine Fumarate as a Myelin Repair Therapy. University of California, San Francisco. 2026. ClinicalTrials.gov Identifier: NCT06065670

18. (NCT06065670 chunk 4):  Assessing Changes in Multi-parametric MRI in Patients With Acute Demyelinating Lesions Taking Clemastine Fumarate as a Myelin Repair Therapy. University of California, San Francisco. 2026. ClinicalTrials.gov Identifier: NCT06065670