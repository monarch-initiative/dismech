---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-03T08:20:21.224803'
end_time: '2026-04-03T08:30:10.819641'
duration_seconds: 589.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multiple Mitochondrial Dysfunctions Syndrome 9B
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 9B
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 9B** covering all of the
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
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 9B
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 9B** covering all of the
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


## Comprehensive Research Report: Multiple Mitochondrial Dysfunctions Syndrome 9B (MMDS9B)

### Executive summary
Multiple mitochondrial dysfunctions syndrome 9B (MMDS9B) is an autosomal recessive primary mitochondrial disease caused by biallelic variants in **FDXR** (ferredoxin–NADP(+) reductase/ferredoxin reductase). The contemporary clinical framing in 2023–2024 literature is **“FDXR-related mitochondriopathy (FRM)”** or **“FDXR-associated disease”**, with prominent **optic neuropathy/optic atrophy**, variable **auditory neuropathy/hearing loss**, **ataxia**, and **sensorimotor peripheral neuropathy**, often with infection-triggered exacerbations. A 2024 mechanistic-clinical study expanded the phenotype to include **adrenal insufficiency** and disorders of sexual development in severe early-onset cases, consistent with FDXR’s role in mitochondrial P450 electron transfer for steroidogenesis. (masnada2023fdxrassociateddiseasea pages 4-5, pignatti2024fdxrvariantscause pages 2-3)

| Domain | Key facts |
|---|---|
| Disease / synonyms | **Multiple mitochondrial dysfunctions syndrome 9B (MMDS9B)**; **FDXR-related mitochondriopathy (FRM)**; **FDXR-associated disease**; ocular presentations include **FDXR-associated oculopathy**, autosomal recessive optic atrophy with auditory neuropathy, congenital amaurosis/LCA-like disease, and early-onset severe retinal dystrophy (2023-2024) (yi2023fdxrassociatedoculopathycongenital pages 1-2, pignatti2024fdxrvariantscause pages 2-3) |
| Identifier(s) | **MONDO:** MONDO_0971174; **gene OMIM:** **FDXR OMIM 103270**; phenotype label reported in literature: **autosomal recessive optic atrophy and auditory neuropathy (ANOA), OMIM 617717** (2023) (yi2023fdxrassociatedoculopathycongenital pages 1-2) |
| Causal gene / biology | **FDXR** encodes mitochondrial **ferredoxin reductase / ferredoxin-NADP(+) reductase**, supporting electron transfer from NADPH to ferredoxin and linked to **iron-sulfur (Fe-S) cluster biogenesis**, mitochondrial respiration, redox balance, and steroidogenic mitochondrial P450 systems (2023-2024) (yi2023fdxrassociatedoculopathycongenital pages 1-2, pignatti2024fdxrvariantscause pages 2-3) |
| Inheritance | **Autosomal recessive / biallelic** pathogenic or likely pathogenic **FDXR** variants; reported cohorts include **44 patients** (2023 review) and **77 patients with 59 biallelic mutations** (2024 review) (masnada2023fdxrassociateddiseasea pages 1-2, pignatti2024fdxrvariantscause pages 2-3) |
| Hallmark phenotypes | Common core phenotype: **optic neuropathy/optic atrophy**, **auditory neuropathy/hearing loss**, developmental delay/regression, hypotonia, pyramidal/cerebellar signs, neuropathy, retinal degeneration, seizures; ocular triad in some patients: **optic disc pallor + attenuated/silver-wiring retinal vessels + generalized retinal degeneration** (2023) (masnada2023fdxrassociateddiseasea pages 4-5, yi2023fdxrassociatedoculopathycongenital pages 9-10, yi2023fdxrassociatedoculopathycongenital pages 1-2) |
| Phenotype frequencies | Review data: **optic neuropathy 93.2-93.5%**, **auditory/acoustic neuropathy 50.0%**, **ataxia 40.9-43.9%**, **sensorimotor peripheral polyneuropathy ~20.5-23.9%** (22.72% in one review summary), **retinal dystrophy 29.5%**, **nystagmus 18.2%**, **microcephaly 15.9%**, **movement disorders 13.6%**, **seizures 6.8%** (2023) (masnada2023fdxrassociateddiseasea pages 4-5, masnada2023fdxrassociateddiseasea pages 2-4, masnada2023fdxrassociateddiseasea pages 1-2) |
| Ocular presentation details | In one 2023 Chinese cohort, **11 unrelated patients** with biallelic FDXR variants had **4 congenital amaurosis/LCA-like** and **7 EOSRD** presentations; literature summary cited **42 optic atrophy** and **24 retinal dystrophy** cases, with **18 nystagmus** cases (2023) (yi2023fdxrassociatedoculopathycongenital pages 1-2, yi2023fdxrassociatedoculopathycongenital pages 9-10, yi2023fdxrassociatedoculopathycongenital pages 2-5) |
| Onset / course / triggers | Often **infantile or early-childhood onset**, but presentations can be acute-subacute; some cases first mimic inflammatory neuropathy. **Infection-triggered worsening/relapses** are important: **15/44 (34%)** had infection-associated relapses; 2024 review noted **20/77 (26%)** severe, often life-threatening events/deadly infections and **12 deaths** between **0.5-6 years** (2023-2024) (masnada2023fdxrassociateddiseasea pages 4-5, pignatti2024fdxrvariantscause pages 2-3) |
| Pathophysiology | Current model links **FDXR loss** to defective **Fe-S protein maturation**, impaired oxidative phosphorylation/respiratory chain function, **mitochondrial iron accumulation**, excess **ROS/lipid peroxidation**, and tissue injury in retina, optic nerve, peripheral nerve, brain, adrenal and other high-energy tissues; 2025 preclinical work adds **ferroptosis via NRF2/SLC7A11 disruption** (2023-2025) (masnada2023fdxrassociateddiseasea pages 1-2, campbell2025ferroptosisisa pages 11-11, tanaka2025hepaticferredoxinreductase pages 1-5) |
| Diagnostic modalities | Diagnosis relies on **genetic sequencing** (**WES/trio-WES**, increasingly WGS/panel-based testing), ACMG/AMP variant interpretation, and phenotype-guided workup. Key modalities: **ophthalmic exam/fundus/ERG**, **brain/spine MRI**, **neurophysiology** (**NCS/EMG**, BAEP/ABR, VEP, SEP), and broad metabolic/infectious/autoimmune testing, which may be unrevealing (2023-2025) (masnada2023fdxrassociateddiseasea pages 1-2, masnada2023fdxrassociateddiseasea pages 2-4, cao2025identificationofgenetic pages 16-16) |
| Imaging / electrophysiology clues | MRI may be normal early, or show **optic nerve atrophy**, **basal ganglia T2 hyperintensities**, **cerebellar/cerebral atrophy**, **thin corpus callosum**, delayed myelination, spinal cord atrophy, or posterior column signal changes. Nerve studies often suggest **primary axonal impairment**, sometimes with reversible conduction block (2023) (masnada2023fdxrassociateddiseasea pages 4-5, masnada2023fdxrassociateddiseasea pages 2-4) |
| Real-world management | No proven disease-specific standard therapy. Reported care includes **mitochondrial supplements** such as **coenzyme Q10, riboflavin, thiamine, lipoic acid**; supportive neurologic/ophthalmic/audiologic care; **cochlear implantation** may be used for auditory neuropathy in selected patients (2023-2025) (masnada2023fdxrassociateddiseasea pages 4-5, cao2025identificationofgenetic pages 16-16) |
| Misdiagnosis / empiric immunotherapy | Acute neuropathic presentations may be misdiagnosed as inflammatory neuropathy; reported empiric treatments include **IV methylprednisolone, IVIG, oral prednisone, azathioprine**, with **partial, transient, or unclear benefit** and no established efficacy for MMDS9B itself (2023) (masnada2023fdxrassociateddiseasea pages 1-2, masnada2023fdxrassociateddiseasea pages 2-4) |
| Emerging / experimental therapeutics | **AAV-Fdxr gene therapy** improved optic atrophy, sensory neuropathy, and mitochondrial dysfunction in an **Fdxr mouse model**; **omaveloxolone** (an **NRF2 activator**) reduced ferroptotic features in a **2025 preclinical Fdxr mouse/cell model**; authors also discuss antioxidants/iron-directed strategies as future avenues (2023-2025) (yi2023fdxrassociatedoculopathycongenital pages 9-10, campbell2025ferroptosisisa pages 11-11, yi2023fdxrassociatedoculopathycongenital pages 10-11) |


*Table: This table compiles the main identifiers, genetics, clinical features, diagnostics, and emerging therapeutic concepts for MMDS9B/FDXR-related mitochondriopathy. It is designed as a quick-reference summary for a disease knowledge base entry, with context-ID citations for each major claim.*

---

## 1. Disease information

### 1.1 Definition and overview
MMDS9B (as used in disease ontologies) corresponds to **FDXR-associated disease/FDXR-related mitochondriopathy (FRM)**, a rare recessive mitochondriopathy due to biallelic **FDXR** variants, with neuro-ophthalmologic and neurodegenerative phenotypes and variable systemic involvement. (masnada2023fdxrassociateddiseasea pages 1-2, pignatti2024fdxrvariantscause pages 2-3)

**Recent abstract-supported definition (direct quote):** Masnada et al. (2023) describe: “**Mutations in FDXR gene, involved in mitochondrial pathway, cause a rare recessive neurological disorder with variable severity of phenotypes. The most common presentation includes optic and/or auditory neuropathy…**” (Neurological Sciences, April 2023; https://doi.org/10.1007/s10072-023-06790-0). (masnada2023fdxrassociateddiseasea pages 1-2)

### 1.2 Key identifiers
* **MONDO:** **MONDO_0971174** (“multiple mitochondrial dysfunctions syndrome 9b”) (from OpenTargets disease object). (masnada2023fdxrassociateddiseasea pages 1-2)
* **Gene (OMIM):** **FDXR OMIM 103270**. (yi2023fdxrassociatedoculopathycongenital pages 1-2)
* **Related phenotype label in OMIM (as used in ophthalmic genetics literature):** **Autosomal recessive optic atrophy and auditory neuropathy (ANOA), OMIM 617717**. (yi2023fdxrassociatedoculopathycongenital pages 1-2)

**Not found in retrieved texts:** Orphanet disease identifier, ICD-10/ICD-11, and MeSH terms were not explicitly stated in the retrieved full-text excerpts, although an **Orphanet gene page** for FDXR is referenced in later literature. (tafakhori2026homozygousfdxrvariant pages 6-6)

### 1.3 Synonyms / alternative names used in the literature
* **FDXR-related mitochondriopathy (FRM)** (2024). (pignatti2024fdxrvariantscause pages 2-3)
* **FDXR-associated disease** (2023). (masnada2023fdxrassociateddiseasea pages 1-2)
* Ophthalmology-facing labels (phenotype-first): **FDXR-associated oculopathy**, **congenital amaurosis/Leber congenital amaurosis-like**, **early-onset severe retinal dystrophy (EOSRD)**. (yi2023fdxrassociatedoculopathycongenital pages 1-2, yi2023fdxrassociatedoculopathycongenital pages 2-5)

### 1.4 Evidence source type
Most disease knowledge is derived from **aggregated literature case reports/series plus systematic reviews**, rather than EHR-scale observational cohorts, reflecting the disorder’s rarity. The 2023 neurologic paper includes a systematic review; the 2024 JCI Insight paper includes case descriptions plus patient-derived functional models. (masnada2023fdxrassociateddiseasea pages 1-2, pignatti2024fdxrvariantscause pages 2-3)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **FDXR** (autosomal recessive). (masnada2023fdxrassociateddiseasea pages 4-5, pignatti2024fdxrvariantscause pages 2-3)

**Functional role of FDXR:** FDXR is described as mitochondrial ferredoxin–NADP(+) reductase, transferring reducing equivalents from NADPH via ferredoxin to mitochondrial **cytochrome P450 enzymes** (steroid biosynthesis) and linked to mitochondrial redox/iron–sulfur biology. (yi2023fdxrassociatedoculopathycongenital pages 1-2, pignatti2024fdxrvariantscause pages 2-3)

**Direct abstract-supported statement (direct quote):** Pignatti et al. (JCI Insight, June 2024; https://doi.org/10.1172/jci.insight.179071) note: “**FDXR is characterized as the mitochondrial flavoprotein ferredoxin–NADP(+) reductase that accepts electrons from NADPH and transfers them via ferredoxin (FDX) to mitochondrial cytochrome P450 enzymes**” and frame disease as “**FDXR-related mitochondriopathy (FRM)**”. (pignatti2024fdxrvariantscause pages 2-3)

### 2.2 Risk factors
* **Genetic:** autosomal recessive inheritance; consanguinity can be relevant in individual families. Masnada et al. report a consanguineous family with homozygous **c.463C>T (p.Arg155Trp)**. (masnada2023fdxrassociateddiseasea pages 2-4)
* **Clinical trigger / modifier:** infections frequently precipitate worsening/relapses (see §8). (masnada2023fdxrassociateddiseasea pages 4-5, pignatti2024fdxrvariantscause pages 2-3)

### 2.3 Protective factors
No established genetic or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
The ocular cohort review discusses that phenotype variability may be influenced by **environmental/epigenetic** and **maternal factors** in addition to variant pathogenicity, but specific validated gene–environment interaction mechanisms are not established. (yi2023fdxrassociatedoculopathycongenital pages 9-10)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum (with frequencies from 2023 systematic review)
Masnada et al. summarize **44 patients from 35 families** and provide phenotype frequencies, including:
* **Optic neuropathy/optic atrophy:** ~**93%**. (masnada2023fdxrassociateddiseasea pages 4-5, masnada2023fdxrassociateddiseasea pages 2-4)
* **Auditory/acoustic neuropathy:** **50%**. (masnada2023fdxrassociateddiseasea pages 4-5, masnada2023fdxrassociateddiseasea pages 2-4)
* **Ataxia:** ~**41–44%**. (masnada2023fdxrassociateddiseasea pages 4-5, masnada2023fdxrassociateddiseasea pages 1-2)
* **Sensorimotor peripheral polyneuropathy:** ~**20–24%**. (masnada2023fdxrassociateddiseasea pages 4-5, masnada2023fdxrassociateddiseasea pages 1-2)
* **Retinal dystrophy:** **29.5%**. (masnada2023fdxrassociateddiseasea pages 2-4)
* **Nystagmus:** **18.2%**. (masnada2023fdxrassociateddiseasea pages 2-4)
* **Seizures:** **6.8%**. (masnada2023fdxrassociateddiseasea pages 2-4)

Other recurrent features include hypotonia, pyramidal signs, microcephaly, and movement disorders. (masnada2023fdxrassociateddiseasea pages 2-4)

**Direct abstract-supported statistics (direct quote):** Masnada et al. (2023) state their literature review found “**a significant incidence of sensorimotor peripheral polyneuropathy (22.72%) and ataxia (43.18%)**”. (masnada2023fdxrassociateddiseasea pages 1-2)

### 3.2 Ophthalmic phenotypes and real-world clinical presentation
A 2023 ophthalmic genetics cohort (Yi et al., Genes, April 2023; https://doi.org/10.3390/genes14040952) shows that biallelic FDXR variants are a **frequent cause of congenital/early-onset severe retinal dystrophy** in a Chinese WES dataset:
* **11 unrelated patients** were identified in a WES dataset of 6397 families with eye conditions. (yi2023fdxrassociatedoculopathycongenital pages 1-2)
* Presentations included **4** with congenital amaurosis/LCA-like onset and **7** with EOSRD. (yi2023fdxrassociatedoculopathycongenital pages 1-2, yi2023fdxrassociatedoculopathycongenital pages 5-6)
* A characteristic fundus “triad” described includes **optic disc pallor**, **silver-wiring/attenuated retinal vessels**, and **generalized retinal degeneration**, supported visually in the paper’s figures and tables. (yi2023fdxrassociatedoculopathycongenital pages 9-10, yi2023fdxrassociatedoculopathycongenital media 63ac4024)

### 3.3 Suggested HPO terms (non-exhaustive; mapped to reported features)
* Optic atrophy / optic neuropathy: **HP:0000648**
* Retinal dystrophy: **HP:0000556**
* Nystagmus: **HP:0000639**
* Auditory neuropathy / sensorineural hearing impairment: **HP:0000407** (hearing impairment); **HP:0008619** (auditory neuropathy; if using more specific term)
* Peripheral neuropathy: **HP:0000759**
* Ataxia: **HP:0001251**
* Hypotonia: **HP:0001252**
* Seizures: **HP:0001250**
* Developmental delay / regression: **HP:0001263** / **HP:0002376**
* Pyramidal signs / spasticity: **HP:0001257**
* Microcephaly: **HP:0000252**

### 3.4 Laboratory/biochemical abnormalities (clinical-level)
Routine metabolic/infectious/autoimmune testing may be unrevealing in some patients, contributing to diagnostic delay and misdiagnosis as inflammatory neuropathy. (masnada2023fdxrassociateddiseasea pages 2-4)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
* **Gene:** **FDXR** (ferredoxin reductase / ferredoxin–NADP(+) reductase), **OMIM 103270**. (yi2023fdxrassociatedoculopathycongenital pages 1-2)

### 4.2 Pathogenic variants and variant spectrum
* Predominantly **biallelic missense variants** are reported across cohorts; Yi et al. found **14 missense variants** among 11 unrelated patients, **10 novel**, with ACMG/AMP classifications including **pathogenic** and **likely pathogenic**. (yi2023fdxrassociatedoculopathycongenital pages 1-2, yi2023fdxrassociatedoculopathycongenital pages 2-5)
* A hotspot severe-phenotype variant **p.R386W** is referenced in the 2024 review. (pignatti2024fdxrvariantscause pages 2-3)
* Example family-level variant with population-frequency annotation: **c.463C>T (p.Arg155Trp)** with gnomAD MAF noted in Masnada et al. (2023). (masnada2023fdxrassociateddiseasea pages 2-4)

### 4.3 Functional consequences
Evidence across clinical and mechanistic studies supports that FDXR variants lead to impaired mitochondrial electron transfer (NADPH→FDX), mitochondrial dysfunction, and—in severe cases—impaired steroidogenesis consistent with disrupted mitochondrial P450 enzyme function. (pignatti2024fdxrvariantscause pages 2-3)

### 4.4 Modifier genes / epigenetics
No validated modifier genes were identified in retrieved sources. Phenotypic variability is noted and hypothesized to involve non-genetic modifiers, but specific epigenetic mechanisms are not established. (yi2023fdxrassociatedoculopathycongenital pages 9-10)

---

## 5. Environmental information
No specific environmental toxins, lifestyle factors, or infectious agents are identified as primary causes. Infections are described as **clinical triggers** for relapse/worsening rather than etiologic agents. (masnada2023fdxrassociateddiseasea pages 4-5, pignatti2024fdxrvariantscause pages 2-3)

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding (2023–2025 synthesis)
A coherent mechanistic chain supported by recent clinical-functional and preclinical work is:
1. **Upstream defect:** biallelic **FDXR loss-of-function** or functional impairment reduces electron transfer from **NADPH** through FDXR/ferredoxin to (a) mitochondrial Fe–S/iron/redox systems and (b) mitochondrial **cytochrome P450** enzymes. (pignatti2024fdxrvariantscause pages 2-3)
2. **Downstream mitochondrial consequences:** mitochondrial dysfunction with oxidative stress and dysregulated iron handling, leading to tissue vulnerability in high-energy systems (retina/optic nerve, peripheral nerve, brain; and adrenal in severe cases). (masnada2023fdxrassociateddiseasea pages 1-2, tanaka2025hepaticferredoxinreductase pages 1-5)
3. **Emerging cell-death mechanism:** a 2025 mechanistic study proposes that FDXR loss increases lipid peroxidation and susceptibility to **ferroptosis** via disrupted **NRF2 pathway** and **SLC7A11**, and demonstrates rescue of ferroptotic features with an NRF2 activator. (campbell2025ferroptosisisa pages 11-11)

### 6.2 Expert interpretations / authoritative analyses
* **Clinical expert synthesis (2023):** emphasizes a broad neurodegenerative phenotype with frequent optic/auditory neuropathy and clinically important peripheral neuropathy that can mimic inflammatory disorders. (masnada2023fdxrassociateddiseasea pages 1-2, masnada2023fdxrassociateddiseasea pages 4-5)
* **Mechanistic clinical expansion (2024, JCI Insight):** links FDXR dysfunction to steroidogenesis and documents adrenal insufficiency/DSD phenotypes, explaining clinical deterioration under stress/infection in some patients as potentially compounded by adrenal insufficiency. (pignatti2024fdxrvariantscause pages 2-3)
* **Therapeutic mechanistic hypothesis (2025):** positions NRF2 activation as an “immediate, viable treatment option” in preclinical context, while cautioning it may not address all enzymatic deficits intrinsic to FDXR loss. (campbell2025ferroptosisisa pages 11-11)

### 6.3 Suggested GO biological process terms (examples)
* **Iron–sulfur cluster assembly** (GO:0016226)
* **Mitochondrial electron transport, NADH to ubiquinone** (GO:0006120) (downstream OXPHOS impairment)
* **Response to oxidative stress** (GO:0006979)
* **Steroid biosynthetic process** (GO:0006694)
* **Regulation of ferroptosis** (GO term exists; depending on ontology version)

### 6.4 Suggested CL cell types and GO cellular components
* **Retinal ganglion cell** (CL:0000740) (optic neuropathy context)
* **Photoreceptor cell** (CL:0000210) (retinal dystrophy context)
* **Peripheral neuron / Schwann cell** (for neuropathy; exact CL terms depend on granularity)
* Cellular component: **mitochondrion** (GO:0005739), **mitochondrial inner membrane** (GO:0005743)

---

## 7. Anatomical structures affected

### 7.1 Primary organs/systems
* **Eye/visual system:** optic nerve/retinal degeneration is a dominant feature (optic disc pallor, retinal vessel attenuation, generalized degeneration). (yi2023fdxrassociatedoculopathycongenital pages 9-10, yi2023fdxrassociatedoculopathycongenital media 63ac4024)
* **Auditory system:** auditory neuropathy/hearing loss common. (masnada2023fdxrassociateddiseasea pages 4-5)
* **Central and peripheral nervous system:** cerebellar/ataxic features and peripheral neuropathy (often axonal). (masnada2023fdxrassociateddiseasea pages 4-5)
* **Endocrine/adrenal system:** adrenal insufficiency documented in severe FRM cases (2024). (pignatti2024fdxrvariantscause pages 2-3)

### 7.2 Suggested UBERON anatomical terms (examples)
* Optic nerve: **UBERON:0001890**
* Retina: **UBERON:0000966**
* Cochlea / inner ear: **UBERON:0001845**
* Peripheral nerve: **UBERON:0001021**
* Adrenal gland: **UBERON:0002369**

---

## 8. Temporal development

### 8.1 Onset
Typical onset is **infantile to early-childhood**, though subacute presentations occur; ophthalmic onset can be within months (nystagmus and severe visual impairment), consistent with congenital amaurosis/EOSRD presentations. (yi2023fdxrassociatedoculopathycongenital pages 1-2, yi2023fdxrassociatedoculopathycongenital pages 5-6)

### 8.2 Progression and triggers
* **Infection-triggered relapses/worsening:** Masnada et al. report infection-triggered relapses in **15/44 (34%)**. (masnada2023fdxrassociateddiseasea pages 4-5)
* **Severe early-life events and mortality:** Pignatti et al. (2024) report that in their review **20/77 (26%)** experienced severe, often life-threatening events/deadly infections, and **12 deaths** occurred between **0.5–6 years**, “mostly after infection”. (pignatti2024fdxrvariantscause pages 2-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
**Autosomal recessive** inheritance with **biallelic** pathogenic/likely pathogenic variants. (masnada2023fdxrassociateddiseasea pages 4-5, yi2023fdxrassociatedoculopathycongenital pages 2-5)

### 9.2 Epidemiology
No prevalence/incidence estimates were provided in the retrieved sources. Available quantitative disease frequency evidence is limited to **case counts in the literature**, including 44 reported patients summarized in 2023 and 77 summarized in 2024. (masnada2023fdxrassociateddiseasea pages 1-2, pignatti2024fdxrvariantscause pages 2-3)

### 9.3 Population genetics / variant frequencies
* A specific variant example includes a gnomAD minor allele frequency annotation for **p.Arg155Trp** in Masnada et al. (2023), illustrating that some pathogenic alleles can be extremely rare but present in reference databases. (masnada2023fdxrassociateddiseasea pages 2-4)
* In the 2023 Chinese ocular cohort, common alleles among identified mutant alleles included **p.R79C**, **p.R104C**, and **p.V314L**, with allele proportions reported within that cohort’s mutant allele set. (yi2023fdxrassociatedoculopathycongenital pages 2-5)

---

## 10. Diagnostics

### 10.1 Clinical tests and evaluations used in practice
* **Neurophysiology:** NCS/EMG often shows axonal impairment; BAEP/ABR and VEP/SEP can be informative. (masnada2023fdxrassociateddiseasea pages 1-2, masnada2023fdxrassociateddiseasea pages 4-5)
* **Imaging:** brain/spine MRI may be normal early, or show optic nerve atrophy and other neurodegenerative changes (e.g., cerebral/cerebellar atrophy, thin corpus callosum, delayed myelination, spinal cord/posterior column changes). (masnada2023fdxrassociateddiseasea pages 4-5, masnada2023fdxrassociateddiseasea pages 2-4)
* **Ophthalmic testing:** fundus photography and ERG; characteristic fundus triad is visually documented in the 2023 Genes paper figures/tables. (yi2023fdxrassociatedoculopathycongenital media 63ac4024)

### 10.2 Genetic testing (recommended approach)
* **Trio-WES/WES** is frequently diagnostic in published cases; ACMG/AMP interpretation is applied. (masnada2023fdxrassociateddiseasea pages 2-4, yi2023fdxrassociatedoculopathycongenital pages 2-5)
* For phenotype-first ophthalmic cohorts (LCA/EOSRD), inclusion of **FDXR** in IRD/optic neuropathy panels or exome re-analysis is supported by 2023 cohort evidence. (yi2023fdxrassociatedoculopathycongenital pages 1-2)

### 10.3 Differential diagnosis
* **Inflammatory neuropathies (GBS/CIDP-like):** acute/subacute peripheral neuropathy presentations can mimic inflammatory disease, leading to empiric immunotherapy and diagnostic delay. (masnada2023fdxrassociateddiseasea pages 1-2, masnada2023fdxrassociateddiseasea pages 2-4)
* **Inherited retinal dystrophies / hereditary optic neuropathies:** broad genetic heterogeneity necessitates multigene testing; FDXR is among recurrent genes in optic neuropathy diagnostics. (yi2023fdxrassociatedoculopathycongenital pages 1-2)

---

## 11. Outcomes / prognosis
Prognosis is **variable**, spanning slowly progressive neuro-ophthalmologic disease to severe early-onset multisystem disease with fatal infection-associated deterioration in a subset. (masnada2023fdxrassociateddiseasea pages 4-5, pignatti2024fdxrvariantscause pages 2-3)

Quantitative outcomes reported in 2024 synthesis: **12 deaths between 0.5–6 years** among the 77-patient literature summary, mostly after infection; **26%** experienced severe life-threatening events/deadly infections. (pignatti2024fdxrvariantscause pages 2-3)

---

## 12. Treatment

### 12.1 Current real-world management
There is **no established disease-specific therapy** in the retrieved clinical literature. Reported management includes supportive and empiric interventions:
* “Mitochondrial cocktails” such as **coenzyme Q10, riboflavin, thiamine, lipoic acid** are reported in cases/reviews. (masnada2023fdxrassociateddiseasea pages 4-5)
* For patients misdiagnosed with inflammatory neuropathy, empiric **IV methylprednisolone**, **IVIG**, and longer immunosuppression were used with partial/uncertain benefit and no proven disease-modifying efficacy. (masnada2023fdxrassociateddiseasea pages 2-4)

### 12.2 Emerging / experimental therapeutics (preclinical)
* **Gene therapy:** systemic **AAV-Fdxr** delivery improved optic atrophy, neuropathy, and mitochondrial dysfunction in an Fdxr mouse model, supporting feasibility of gene replacement strategies. (yi2023fdxrassociatedoculopathycongenital pages 10-11)
* **NRF2 activation (drug repurposing concept):** a 2025 mechanistic study reports mitigation of ferroptotic features in an Fdxr model with **omaveloxolone** (NRF2 activator; FDA-approved for Friedreich’s ataxia), proposing NRF2 activation as a candidate approach (preclinical; not yet established clinically for FRM). (campbell2025ferroptosisisa pages 11-11)

### 12.3 Suggested MAXO terms (examples)
* Supportive mitochondrial therapy: **MAXO:0000781** (mitochondrial disease treatment; if available) / **MAXO:0000646** (nutritional supplementation)
* Genetic counseling: **MAXO:0000075**
* Gene therapy: **MAXO:0000127**
* Cochlear implantation (for auditory neuropathy in selected cases): **MAXO:0000504**

---

## 13. Prevention
Primary prevention is not applicable for an inherited recessive disorder beyond reproductive options. Practical prevention focuses on:
* **Genetic counseling** for families and at-risk relatives. (yi2023fdxrassociatedoculopathycongenital pages 2-5)
* **Prenatal/embryo screening** suggested for couples with an affected child (as stated in the 2023 ophthalmic cohort discussion). (yi2023fdxrassociatedoculopathycongenital pages 10-11)

---

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs were identified in the retrieved sources.

---

## 15. Model organisms
Relevant models in 2023–2025 sources include:
* **Fdxr mouse models** used for proof-of-concept systemic AAV gene therapy improving ocular/neurologic phenotypes and mitochondrial dysfunction. (yi2023fdxrassociatedoculopathycongenital pages 10-11)
* **CRISPR/Cas9-engineered Fdxr mutant mouse** and corresponding cells used to test ferroptosis mechanism and pharmacologic rescue with **omaveloxolone**. (campbell2025ferroptosisisa pages 11-11)
* **Patient-derived fibroblasts** reprogrammed to adrenal-like cell models to demonstrate impaired steroidogenesis from FDXR variants (mechanistic link to adrenal insufficiency). (pignatti2024fdxrvariantscause pages 2-3)

---

## Notes on evidence gaps and constraints
* The retrieved corpus did not include explicit **ICD-10/ICD-11**, **Orphanet disease IDs**, or **MeSH** identifiers for MMDS9B, and did not provide population prevalence/incidence estimates; the report therefore relies on case-series totals and systematic review summaries without extrapolating population metrics. (masnada2023fdxrassociateddiseasea pages 1-2, pignatti2024fdxrvariantscause pages 2-3)



References

1. (masnada2023fdxrassociateddiseasea pages 4-5): Silvia Masnada, Roberto Previtali, Paola Erba, Elena Beretta, Anna Camporesi, Luisa Chiapparini, Chiara Doneda, Maria Iascone, Marco U. A. Sartorio, Luigina Spaccini, Pierangelo Veggiotti, Maurizio Osio, Davide Tonduti, and Isabella Moroni. Fdxr-associated disease: a challenging differential diagnosis with inflammatory peripheral neuropathy. Neurological Sciences, 44:1-7, Apr 2023. URL: https://doi.org/10.1007/s10072-023-06790-0, doi:10.1007/s10072-023-06790-0. This article has 8 citations and is from a peer-reviewed journal.

2. (pignatti2024fdxrvariantscause pages 2-3): Emanuele Pignatti, Jesse Slone, María Ángeles Gómez Cano, Teresa Margaret Campbell, Jimmy Vu, Kay Sauter, Amit Vikram Pandey, Francisco Martínez-Azorín, Marina Alonso-Riaño, Derek E Neilson, Nicola Longo, Therina du Toit, Clarissa Vögel, Taosheng Huang, and Christa Emma Flück Pandey. Fdxr variants cause adrenal insufficiency and atypical sexual development. JCI Insight, Jun 2024. URL: https://doi.org/10.1172/jci.insight.179071, doi:10.1172/jci.insight.179071. This article has 6 citations and is from a domain leading peer-reviewed journal.

3. (yi2023fdxrassociatedoculopathycongenital pages 1-2): Shutong Yi, Yuxiang Zheng, Zhen Yi, Yingwei Wang, Yi Jiang, Jiamin Ouyang, Shi-qiang Li, Xueshan Xiao, Wenmin Sun, Panfeng Wang, and Qingjiong Zhang. Fdxr-associated oculopathy: congenital amaurosis and early-onset severe retinal dystrophy as common presenting features in a chinese population. Genes, 14:952, Apr 2023. URL: https://doi.org/10.3390/genes14040952, doi:10.3390/genes14040952. This article has 11 citations.

4. (masnada2023fdxrassociateddiseasea pages 1-2): Silvia Masnada, Roberto Previtali, Paola Erba, Elena Beretta, Anna Camporesi, Luisa Chiapparini, Chiara Doneda, Maria Iascone, Marco U. A. Sartorio, Luigina Spaccini, Pierangelo Veggiotti, Maurizio Osio, Davide Tonduti, and Isabella Moroni. Fdxr-associated disease: a challenging differential diagnosis with inflammatory peripheral neuropathy. Neurological Sciences, 44:1-7, Apr 2023. URL: https://doi.org/10.1007/s10072-023-06790-0, doi:10.1007/s10072-023-06790-0. This article has 8 citations and is from a peer-reviewed journal.

5. (yi2023fdxrassociatedoculopathycongenital pages 9-10): Shutong Yi, Yuxiang Zheng, Zhen Yi, Yingwei Wang, Yi Jiang, Jiamin Ouyang, Shi-qiang Li, Xueshan Xiao, Wenmin Sun, Panfeng Wang, and Qingjiong Zhang. Fdxr-associated oculopathy: congenital amaurosis and early-onset severe retinal dystrophy as common presenting features in a chinese population. Genes, 14:952, Apr 2023. URL: https://doi.org/10.3390/genes14040952, doi:10.3390/genes14040952. This article has 11 citations.

6. (masnada2023fdxrassociateddiseasea pages 2-4): Silvia Masnada, Roberto Previtali, Paola Erba, Elena Beretta, Anna Camporesi, Luisa Chiapparini, Chiara Doneda, Maria Iascone, Marco U. A. Sartorio, Luigina Spaccini, Pierangelo Veggiotti, Maurizio Osio, Davide Tonduti, and Isabella Moroni. Fdxr-associated disease: a challenging differential diagnosis with inflammatory peripheral neuropathy. Neurological Sciences, 44:1-7, Apr 2023. URL: https://doi.org/10.1007/s10072-023-06790-0, doi:10.1007/s10072-023-06790-0. This article has 8 citations and is from a peer-reviewed journal.

7. (yi2023fdxrassociatedoculopathycongenital pages 2-5): Shutong Yi, Yuxiang Zheng, Zhen Yi, Yingwei Wang, Yi Jiang, Jiamin Ouyang, Shi-qiang Li, Xueshan Xiao, Wenmin Sun, Panfeng Wang, and Qingjiong Zhang. Fdxr-associated oculopathy: congenital amaurosis and early-onset severe retinal dystrophy as common presenting features in a chinese population. Genes, 14:952, Apr 2023. URL: https://doi.org/10.3390/genes14040952, doi:10.3390/genes14040952. This article has 11 citations.

8. (campbell2025ferroptosisisa pages 11-11): Teresa Campbell, Jesse Slone, Jimmy Vu, Wensheng Liu, Li Yang, Adam Dourson, Luis F. Queme, Michael P. Jankowski, and Taosheng Huang. Ferroptosis is a novel pathogenic mechanism of fdxr-related disease via disruption of the nrf2 pathway. Cell Death Discovery, Dec 2025. URL: https://doi.org/10.1038/s41420-025-02840-y, doi:10.1038/s41420-025-02840-y. This article has 0 citations and is from a peer-reviewed journal.

9. (tanaka2025hepaticferredoxinreductase pages 1-5): Tomoaki Tanaka, Ikki Sakuma, Rafael Gaspar, Panu Luukkonen, Brandon Hubbard, Daniel Vatner, Ali Nasiri, Sylvie Dufour, Mario Kahn, Mark Perelis, Yuki Taki, Akitoshi Nakayama, Masanori Fujimoto, Takashi Kono, Takashi Miki, Koutaro Yokote, Kitt Petersen, Varman Samuel, and Gerald Shulman. Hepatic ferredoxin reductase modulates mitochondrial function and iron homeostasis in metabolic dysfunction-associated steatotic liver disease. Research Square, Aug 2025. URL: https://doi.org/10.21203/rs.3.rs-7014857/v1, doi:10.21203/rs.3.rs-7014857/v1. This article has 0 citations.

10. (cao2025identificationofgenetic pages 16-16): Yang Cao, Xiaolong Zhang, Lan Lan, Danyang Li, Jin Li, Linyi Xie, Fen Xiong, Lan Yu, Xiaonan Wu, Hongyang Wang, and Qiuju Wang. Identification of genetic mechanisms of non-isolated auditory neuropathy with various phenotypes in chinese families. Orphanet Journal of Rare Diseases, Jan 2025. URL: https://doi.org/10.1186/s13023-025-03540-7, doi:10.1186/s13023-025-03540-7. This article has 3 citations and is from a peer-reviewed journal.

11. (yi2023fdxrassociatedoculopathycongenital pages 10-11): Shutong Yi, Yuxiang Zheng, Zhen Yi, Yingwei Wang, Yi Jiang, Jiamin Ouyang, Shi-qiang Li, Xueshan Xiao, Wenmin Sun, Panfeng Wang, and Qingjiong Zhang. Fdxr-associated oculopathy: congenital amaurosis and early-onset severe retinal dystrophy as common presenting features in a chinese population. Genes, 14:952, Apr 2023. URL: https://doi.org/10.3390/genes14040952, doi:10.3390/genes14040952. This article has 11 citations.

12. (tafakhori2026homozygousfdxrvariant pages 6-6): Abbas Tafakhori, Zahra Sarvestani, Ariana Kariminejad, Homa Tajsharghi, Go Hun Seo, Seung Woo Ryu, and Sanaz Heydari Havadaragh. Homozygous fdxr variant in twin sisters with spastic paraparesis followed by acute progressive flaccid quadriparesis. BMC Neurology, Feb 2026. URL: https://doi.org/10.1186/s12883-026-04752-5, doi:10.1186/s12883-026-04752-5. This article has 0 citations and is from a peer-reviewed journal.

13. (yi2023fdxrassociatedoculopathycongenital pages 5-6): Shutong Yi, Yuxiang Zheng, Zhen Yi, Yingwei Wang, Yi Jiang, Jiamin Ouyang, Shi-qiang Li, Xueshan Xiao, Wenmin Sun, Panfeng Wang, and Qingjiong Zhang. Fdxr-associated oculopathy: congenital amaurosis and early-onset severe retinal dystrophy as common presenting features in a chinese population. Genes, 14:952, Apr 2023. URL: https://doi.org/10.3390/genes14040952, doi:10.3390/genes14040952. This article has 11 citations.

14. (yi2023fdxrassociatedoculopathycongenital media 63ac4024): Shutong Yi, Yuxiang Zheng, Zhen Yi, Yingwei Wang, Yi Jiang, Jiamin Ouyang, Shi-qiang Li, Xueshan Xiao, Wenmin Sun, Panfeng Wang, and Qingjiong Zhang. Fdxr-associated oculopathy: congenital amaurosis and early-onset severe retinal dystrophy as common presenting features in a chinese population. Genes, 14:952, Apr 2023. URL: https://doi.org/10.3390/genes14040952, doi:10.3390/genes14040952. This article has 11 citations.