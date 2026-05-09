---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T10:48:50.760920'
end_time: '2026-05-08T11:03:01.784709'
duration_seconds: 851.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cannabis Hyperemesis Syndrome
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Cannabis Hyperemesis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cannabis Hyperemesis Syndrome** covering all of the
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
- **Disease Name:** Cannabis Hyperemesis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cannabis Hyperemesis Syndrome** covering all of the
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


# Comprehensive Disease Characteristics Report: Cannabis Hyperemesis Syndrome (CHS)

**Target disease:** Cannabis Hyperemesis Syndrome (CHS) (also “cannabinoid hyperemesis syndrome”) (loganathan2024acomprehensivereview pages 1-2, sorensen2017cannabinoidhyperemesissyndrome pages 1-2)
**Category:** Complex disorder of gut–brain interaction (loganathan2024acomprehensivereview pages 1-2, perisetti2020cannabishyperemesissyndrome pages 5-6)

## Evidence summary artifacts
The following KB-ready table consolidates core definitions, phenotypes (with HPO suggestions), complications, epidemiology signals, and treatments (with MAXO suggestions):

| Domain | Item | KB-ready details | Suggested ontology terms | Reported frequency / quantitative detail | Best supporting citation IDs |
|---|---|---|---|---|---|
| Definition / criteria | CHS overview | Disorder of gut–brain interaction characterized by stereotypical episodic nausea/vomiting with chronic cannabis exposure; often associated with abdominal pain and relief with hot bathing; symptoms improve after cannabis cessation | MONDO: not clearly established in retrieved sources; MeSH: not confirmed in retrieved sources | First described in 2004; increasingly recognized in ED settings | (loganathan2024acomprehensivereview pages 1-2, perisetti2020cannabishyperemesissyndrome pages 5-6, sorensen2017cannabinoidhyperemesissyndrome pages 1-2) |
| Definition / criteria | Rome IV highlights | Onset at least 6 months before diagnosis; stereotypical vomiting episodes lasting <1 week; at least 3 episodes/year and at least 2 in 6 months; no vomiting between episodes; associated with chronic cannabis use; resolution after cessation supports diagnosis | HPO: Cyclic vomiting HP:0002572; Nausea HP:0002018 | Cannabis exposure preceding CHS reported from 6 months to 11 years in reviewed literature | (perisetti2020cannabishyperemesissyndrome pages 5-6, senderovich2022asystematicreview pages 1-2) |
| Phenotype | Cyclic nausea/vomiting | Core presenting symptom complex in chronic cannabis users | HP:0002018 Nausea; HP:0002572 Cyclic vomiting; HP:0002013 Vomiting | Regular cannabis use 100%; cyclic nausea/vomiting 100% in systematic review of reported cases | (sorensen2017cannabinoidhyperemesissyndrome pages 1-2) |
| Phenotype | Relief with hot bathing / hot showers | Characteristic supportive feature; often used by patients for temporary symptom relief; likely linked to TRPV1/thermoregulatory mechanisms | HP:0033836 Compulsive bathing behavior (suggested behavioral proxy); HP:0012531 Abnormality of temperature regulation (broad related term) | 92.3% of reported cases had compulsive hot baths/showers with relief | (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, stumpf2021managementofcannabinoid pages 2-3) |
| Phenotype | Abdominal pain | Common accompanying symptom during hyperemetic episodes | HP:0002027 Abdominal pain | 85.1% in systematic review of reported cases | (sorensen2017cannabinoidhyperemesissyndrome pages 1-2) |
| Phenotype | Weight loss | Often occurs with recurrent episodes and reduced intake | HP:0001824 Weight loss | Weight loss >5 kg listed as common diagnostic feature in review literature | (stumpf2021managementofcannabinoid pages 1-2, stumpf2021managementofcannabinoid pages 2-3) |
| Phenotype | Morning predominance | Symptoms often worse in the morning | HP:0012735 Morning sickness-like pattern (suggested related term); no exact CHS-specific HPO term identified | Qualitative; commonly reported, no pooled % in retrieved sources | (stumpf2021managementofcannabinoid pages 1-2, stumpf2021managementofcannabinoid pages 2-3) |
| Phenotype | Normal bowel habits between episodes | Helps distinguish from other GI disorders | HP:0002014 Diarrhea / HP:0001508 Constipation absent; no direct positive HPO term ideal | Qualitative diagnostic feature | (stumpf2021managementofcannabinoid pages 1-2, stumpf2021managementofcannabinoid pages 2-3) |
| Complication | Dehydration / volume depletion | Frequent consequence of prolonged emesis requiring IV fluids | HP:0001944 Dehydration | Major acute complication; no pooled frequency in retrieved sources | (perisetti2020cannabishyperemesissyndrome pages 5-6, moses2024exploringalternativetreatments pages 5-6) |
| Complication | Electrolyte abnormalities | Hypokalemia, hypomagnesemia, hypocalcemia can occur and worsen arrhythmia risk | HP:0002900 Hypokalemia; HP:0002917 Abnormal blood magnesium concentration | Potassium <3.0 mmol/L predicted QT prolongation >500 ms in cited retrospective study summarized by review | (merino2024mitigatingtherisk pages 1-2, merino2024mitigatingtherisk pages 4-5, merino2024mitigatingtherisk pages 6-7) |
| Complication | Acute kidney injury | May result from severe dehydration/rhabdomyolysis | HP:0001919 Acute kidney injury | Reported as serious morbidity; no pooled rate in retrieved sources | (perisetti2020cannabishyperemesissyndrome pages 5-6, moses2024exploringalternativetreatments pages 5-6, moses2024exploringalternativetreatments pages 1-3) |
| Complication | QTc prolongation / torsades risk | Risk increased by cannabis exposure, vomiting-related electrolyte loss, and QT-prolonging antiemetics such as haloperidol/ondansetron | HP:0005184 Prolonged QT interval; HP:0011675 Torsade de pointes | In >68,000 cannabis users aged 13–19, QTc prolongation reported at 513.1 per 100,000; literature review found 5 severe adolescent/young-adult cases with life-threatening QTc/TdP | (merino2024mitigatingtherisk pages 1-2, merino2024mitigatingtherisk pages 9-10) |
| Complication | Esophageal injury | Recurrent retching/vomiting can cause esophagitis, Mallory-Weiss tear, rarely rupture | HP:0100823 Hematemesis (related), HP:0012373 Esophagitis | Qualitative; rare but recognized | (perisetti2020cannabishyperemesissyndrome pages 5-6, senderovich2022asystematicreview pages 1-2, stumpf2021managementofcannabinoid pages 1-2) |
| Epidemiology | ED utilization trend | CHS-associated ED visits are increasing with legalization/commercialization | No disease ontology term needed | Nevada rate rose from 1.07 to 2.22 ED visits per 100,000 after recreational cannabis commercialization; largest age group 21–29 years (35.24%); female-predominant relative to comparator cannabis ED visits | (soh2024trendsofemergency pages 1-2, soh2024trendsofemergency pages 2-4, soh2024trendsofemergency pages 4-5) |
| Acute treatment | IV fluids / electrolyte correction | Supportive first-line acute care; monitor CMP, magnesium, ECG when indicated | MAXO: intravenous fluid administration; electrolyte supplementation; electrocardiographic monitoring | Standard supportive care; no comparative efficacy estimate | (moses2024exploringalternativetreatments pages 5-6, merino2024mitigatingtherisk pages 6-7) |
| Acute treatment | Haloperidol | Dopamine antagonist used for acute symptom control; superior to ondansetron in RCT, but monitor QTc risk | MAXO: antipsychotic administration; antiemetic therapy | RCT: less rescue antiemetic use (31% vs 59%) and shorter ED stay (3.1 h vs 5.6 h) vs ondansetron | (merino2024mitigatingtherisk pages 4-5) |
| Acute treatment | Topical capsaicin | TRPV1 agonist; may mimic hot-water relief and reduce need for additional medications | MAXO: topical medication administration | Pilot RCT: significant nausea improvement at 60 min; 29.4% complete nausea relief; retrospective series: ~55% needed no more than one additional medication; 67% of capsaicin-treated visits in one cohort required no further treatment before discharge | (merino2024mitigatingtherisk pages 7-9, stumpf2021managementofcannabinoid pages 1-2) |
| Acute treatment | Benzodiazepines / lorazepam | Frequently reported effective adjunct or alternative, especially when QT risk limits antidopaminergics | MAXO: benzodiazepine administration | Qualitative efficacy; in pediatric/adolescent reviews among most effective reported agents | (merino2024mitigatingtherisk pages 6-7, merino2024mitigatingtherisk pages 4-5) |
| Acute treatment | Aprepitant / fosaprepitant | NK1 antagonist option with low cardiac risk profile; emerging evidence for refractory or QT-risk cases | MAXO: neurokinin-1 receptor antagonist therapy | Adult series global response 71%; pediatric/CVS literature 81% prophylactic and 76% abortive response; CHS adolescent abstract 97% overall improvement | (merino2024mitigatingtherisk pages 7-9) |
| Acute treatment | Olanzapine | Considered when QT concern or refractory symptoms; limited CHS-specific evidence | MAXO: antipsychotic administration | Qualitative; described as rarely causing QT prolongation | (merino2024mitigatingtherisk pages 7-9, merino2024mitigatingtherisk pages 9-10) |
| Long-term treatment | Cannabis cessation | Definitive therapy; sustained abstinence is most successful strategy and supports diagnosis if symptoms resolve | MAXO: substance use cessation intervention; counseling | Symptom resolution after stopping cannabis reported in 96.8% of cases in systematic review | (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, senderovich2022asystematicreview pages 1-2, russo2024cannabinoidhyperemesissyndrome pages 4-6) |
| Long-term treatment | Behavioral / psychiatric support | Counseling, psychotherapy, relapse prevention, treatment of anxiety/depression/substance use disorder improve long-term outcomes | MAXO: counseling; psychotherapy; substance use disorder treatment | Qualitative; multimodal management recommended in 2024 review | (loganathan2024acomprehensivereview pages 11-12, senderovich2022asystematicreview pages 1-2) |
| Long-term treatment | Amitriptyline / chronic prophylaxis in selected patients | Used by some experts for remission/recurrence prevention, especially where CVS overlap is suspected; evidence is lower than for cessation | MAXO: tricyclic antidepressant therapy | Qualitative; one review notes tapering after 1 year without ED visits | (loganathan2024acomprehensivereview pages 11-12) |


*Table: This table summarizes Cannabis Hyperemesis Syndrome for knowledge-base use, including Rome IV diagnostic highlights, core phenotypes with suggested HPO terms, major complications, epidemiology signals, and acute versus long-term treatments with suggested MAXO mappings and supporting citation IDs.*

In addition, the Loganathan et al. 2024 review contains extracted tables comparing diagnostic criteria and management options (visual evidence): diagnostic criteria/comparison table (loganathan2024acomprehensivereview media 73dc557e) and management options table (loganathan2024acomprehensivereview media 15f1dbc6).

---

## 1. Disease Information

### 1.1 Concise overview
Cannabis hyperemesis syndrome (CHS) is characterized by stereotyped/cyclic episodes of severe nausea and vomiting (often with abdominal pain) occurring in the setting of chronic cannabis exposure and typically improving with cannabis cessation; a prominent supportive feature is symptomatic relief with compulsive hot bathing/showering. (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, perisetti2020cannabishyperemesissyndrome pages 5-6)

**Direct abstract quotes supporting definition**
- Sorensen et al. (2017) characterize CHS as “a syndrome of cyclic vomiting associated with cannabis use” (systematic review). (sorensen2017cannabinoidhyperemesissyndrome pages 1-2)
- Perisetti et al. (2020) describe CHS as “a form of functional gut-brain axis disorder characterized by bouts of episodic nausea and vomiting worsened by cannabis intake” (narrative review). (perisetti2020cannabishyperemesissyndrome pages 5-6)

### 1.2 Key identifiers (ontology/coding)
- **Rome IV classification:** CHS is included within Rome IV disorders of gut–brain interaction / functional gastroduodenal disorders in review literature. (loganathan2024acomprehensivereview pages 1-2, perisetti2020cannabishyperemesissyndrome pages 5-6)
- **MONDO / MeSH / ICD-10 / ICD-11 / Orphanet / OMIM:** Not confirmed from the retrieved full-text evidence in this run; therefore not asserted here to avoid introducing uncited identifiers. (soh2024trendsofemergency pages 5-7, soh2024trendsofemergency pages 2-4)

### 1.3 Synonyms and alternative names
- Cannabis hyperemesis syndrome; cannabinoid hyperemesis syndrome; hyperemesis due to cannabis (common phrasing in ED trials). (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, merino2024mitigatingtherisk pages 4-5)

### 1.4 Source type (individual vs aggregated)
The evidence base is largely a combination of: (i) aggregated evidence from systematic reviews and narrative reviews; (ii) administrative/claims/EHR-derived epidemiology (e.g., state ED databases); and (iii) case series and a limited number of randomized or pilot randomized trials evaluating acute therapies. (soh2024trendsofemergency pages 1-2, sorensen2017cannabinoidhyperemesissyndrome pages 1-2, merino2024mitigatingtherisk pages 7-9)

---

## 2. Etiology

### 2.1 Primary causal factors
CHS is most consistently associated with **chronic, heavy cannabis exposure**, and symptom resolution after cessation is a key diagnostic feature, supporting a causal role for continued cannabinoid (CB1 agonist) exposure in susceptible individuals. (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, russo2024cannabinoidhyperemesissyndrome pages 3-4)

### 2.2 Risk factors
**Exposure-related risk context**
- Heavy/regular cannabis use is ubiquitous in reported CHS cases, with systematic review evidence showing history of regular cannabis use in 100% of included cases. (sorensen2017cannabinoidhyperemesissyndrome pages 1-2)
- CHS appears in the context of changing cannabis markets and legalization/commercialization. In Nevada, CHS ED visit rates increased from **1.07 per 100,000 (pre-commercialization) to 2.22 per 100,000 (post-commercialization)** after recreational commercialization (Q3 2017). (soh2024trendsofemergency pages 1-2, soh2024trendsofemergency pages 2-4)
- Synthetic cannabinoids are highlighted as potential higher-risk CB1 agonists in mechanistic discussions; ascertainment is limited in routine ED toxicology. (russo2024cannabinoidhyperemesissyndrome pages 2-3, soh2024trendsofemergency pages 5-7)

**Direct abstract quote supporting exposure link**
- Russo & Whiteley (2024) describe CHS as occurring “most typically in a heavy cannabis user” and discuss association with “escalating intake of high potency cannabis” (Frontiers in Toxicology). (russo2024cannabinoidhyperemesissyndrome pages 1-2)

### 2.3 Protective factors
The only consistently supported protective factor in the retrieved evidence is **cannabis cessation**, which is both diagnostic-supportive (resolution after cessation) and therapeutic. (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, russo2024cannabinoidhyperemesissyndrome pages 4-6)

### 2.4 Gene–environment interactions
A current hypothesis is that CHS arises from **genetic susceptibility interacting with high cumulative cannabinoid exposure** (“toxic exposure”). A 2024 review reports statistically significant differences in several gene variants between CHS cases and heavy cannabis-using controls, consistent with a gene–environment model. (russo2024cannabinoidhyperemesissyndrome pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotypes and frequencies (with HPO suggestions)
The most quantitative phenotype frequencies available in the retrieved evidence come from Sorensen et al. (2017), which summarized case literature:
- **Cyclic nausea/vomiting:** 100% (HPO: **HP:0002018 Nausea**, **HP:0002013 Vomiting**, **HP:0002572 Cyclic vomiting**) (sorensen2017cannabinoidhyperemesissyndrome pages 1-2)
- **Compulsive hot bathing/showering with relief:** 92.3% (behavioral/relief feature; suggest HPO proxy **HP:0033836 Compulsive bathing behavior** and/or thermoregulation-related **HP:0012531 Abnormality of temperature regulation**) (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, stumpf2021managementofcannabinoid pages 2-3)
- **Abdominal pain:** 85.1% (HPO: **HP:0002027 Abdominal pain**) (sorensen2017cannabinoidhyperemesissyndrome pages 1-2)
- **Male predominance:** 72.9% in the compiled case literature (note more recent administrative data may show different sex distributions depending on comparator group and ascertainment). (sorensen2017cannabinoidhyperemesissyndrome pages 1-2, soh2024trendsofemergency pages 4-5)

**Additional commonly reported phenotype characteristics**
- Morning predominance and normal bowel patterns between episodes are repeatedly mentioned as typical clinical characteristics in reviews, though without pooled percentages in the retrieved evidence. (stumpf2021managementofcannabinoid pages 1-2, stumpf2021managementofcannabinoid pages 2-3)

### 3.2 Onset, severity, progression
CHS is typically episodic with phases (prodromal → hyperemesis → recovery/postdrome) described in reviews; hyperemetic episodes are commonly short (days) but recur over time if exposure persists. (stumpf2021managementofcannabinoid pages 1-2, perisetti2020cannabishyperemesissyndrome pages 5-6)

### 3.3 Quality-of-life impact
Although formal QoL instruments were not captured in the retrieved evidence snippets, frequent ED presentations and repeated negative workups are emphasized, indicating substantial functional burden. (stumpf2021managementofcannabinoid pages 1-2, soh2024trendsofemergency pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
CHS is not established as a single-gene disorder; instead, it is treated as complex with **emerging candidate susceptibility genes**.

### 4.2 Candidate susceptibility genes/variants (emerging evidence)
A 2024 review reports five statistically significant mutations differentiating CHS patients from heavy-cannabis-user controls, implicating:
- **TRPV1** (heat/capsaicin-responsive receptor) (p = 0.015)
- **CYP2C9** (THC-metabolizing enzyme) (p = 0.043)
- **COMT** (dopamine catabolism) (p = 0.012)
- **DRD2** (dopamine D2 receptor) (p = 0.031)
- **ABCA1** (ATP-binding cassette transporter) (p = 0.012)
(russo2024cannabinoidhyperemesissyndrome pages 1-2)

A contrasting point in the same review is that a CNR1 SNP associated with cyclic vomiting syndrome (CVS) was reported absent in tested CHS patients, supporting genetic distinction between CVS and CHS. (russo2024cannabinoidhyperemesissyndrome pages 3-4)

**Interpretation note:** these findings are presented as recent/innovative and should be treated as **hypothesis-generating** pending replication and variant-level validation. (russo2024cannabinoidhyperemesissyndrome pages 6-7)

### 4.3 Epigenetics / chromosomal abnormalities
No CHS-specific epigenetic or chromosomal abnormality evidence was identified in the retrieved sources. (russo2024cannabinoidhyperemesissyndrome pages 6-7)

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
- The dominant lifestyle exposure is **chronic cannabis use**; changes in product potency and market access are discussed as contextual contributors. (russo2024cannabinoidhyperemesissyndrome pages 1-2, stumpf2021managementofcannabinoid pages 1-2)
- Administrative epidemiology suggests system-level context: Nevada CHS ED visits increased after recreational commercialization, with notable increases also discussed during COVID-19 time periods. (soh2024trendsofemergency pages 4-5, soh2024trendsofemergency pages 1-2)

### 5.2 Infectious agents
No infectious etiology is suggested in the retrieved evidence. (perisetti2020cannabishyperemesissyndrome pages 5-6)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic understanding (hypothesis-supported)
Mechanistic models converge on dysregulation of the **endocannabinoid system (ECS)** and downstream emetic circuitry:
- **Biphasic cannabinoid effect:** anti-emetic at low doses and pro-emetic at high doses is emphasized in recent reviews as relevant to CHS pathophysiology. (loganathan2024acomprehensivereview pages 1-2, loganathan2024acomprehensivereview pages 2-4)
- **CB1 receptor biology in gut and brain:** CB1 receptors in the intestinal nerve plexus inhibit GI motility; chronic/high-dose exposure may lead to CB1 desensitization/internalization and paradoxical effects that increase emetogenic transmitter signaling (serotonin, dopamine, substance P). (loganathan2024acomprehensivereview pages 1-2, loganathan2024acomprehensivereview pages 2-4)
- **TRPV1/heat pathway:** TRPV1 involvement is used to explain symptomatic relief with hot bathing and responsiveness to topical capsaicin (a TRPV1 agonist). (stumpf2021managementofcannabinoid pages 2-3, russo2024cannabinoidhyperemesissyndrome pages 1-2)
- **Thermoregulatory contribution:** endocannabinoid thermoregulation is proposed to relate to compulsive hot bathing behavior. (loganathan2024acomprehensivereview pages 1-2)

### 6.2 Causal chain (KB-ready)
**Upstream trigger:** sustained exposure to cannabinoids (particularly high cumulative THC/CB1 agonism) in susceptible individuals → **ECS/CB1 dysregulation** (desensitization/internalization; altered feedback control) → **increased emetogenic neurotransmission** in gut–brain pathways and altered GI motility → **episodic hyperemesis** with abdominal pain → **behavioral compensation** (hot bathing, possibly via TRPV1-mediated symptom modulation) → **downstream complications** including dehydration, electrolyte derangements, AKI, and arrhythmia risk (QTc prolongation) exacerbated by vomiting and by some antiemetic drugs. (loganathan2024acomprehensivereview pages 2-4, perisetti2020cannabishyperemesissyndrome pages 5-6, merino2024mitigatingtherisk pages 1-2)

### 6.3 Suggested GO terms (biological processes) and CL terms (cell types)
These are ontology suggestions consistent with the mechanisms described in the cited reviews (not direct experimental annotations in CHS patients):
- **GO (biological process):** vomiting reflex; regulation of gastrointestinal motility; neurotransmitter secretion; response to heat; sensory perception of pain; response to xenobiotic stimulus. (loganathan2024acomprehensivereview pages 2-4, stumpf2021managementofcannabinoid pages 2-3)
- **Cell Ontology (CL):** enteric neurons; dorsal vagal complex/brainstem neurons (broadly “neurons” involved in emesis); sensory neurons expressing TRPV1. (loganathan2024acomprehensivereview pages 2-4, russo2024cannabinoidhyperemesissyndrome pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level (UBERON suggestions)
- Primary system: **gastrointestinal system** (e.g., stomach/intestine) and **central nervous system emesis circuitry**. (loganathan2024acomprehensivereview pages 2-4, perisetti2020cannabishyperemesissyndrome pages 5-6)
- Supportive observations implicate thermoregulatory systems. (loganathan2024acomprehensivereview pages 1-2)

Suggested UBERON terms (broad): stomach; small intestine; enteric nervous system; brainstem. (loganathan2024acomprehensivereview pages 2-4)

### 7.2 Tissue/cell level
- Enteric nervous system involvement is highlighted through CB1 receptor localization and GI motility regulation. (loganathan2024acomprehensivereview pages 1-2, loganathan2024acomprehensivereview pages 2-4)

### 7.3 Subcellular level
Not specifically addressed in the retrieved evidence (no CHS-specific organelle pathology described). (loganathan2024acomprehensivereview pages 2-4)

---

## 8. Temporal Development

- **Onset:** typically after prolonged cannabis use (months to years); exposure windows in reviewed literature ranged from 6 months to 11 years. (senderovich2022asystematicreview pages 1-2)
- **Course:** episodic/recurrent with phases; hyperemesis episodes often last days with inter-episodic relative well-being; recurrence is common if cannabis use continues. (stumpf2021managementofcannabinoid pages 1-2, perisetti2020cannabishyperemesissyndrome pages 5-6)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
High-quality prevalence estimates vary due to diagnostic inconsistency and coding limitations; nonetheless, administrative data demonstrate increasing healthcare utilization.

**Nevada ED interrupted time series (2013–2021)**
- CHS ED visits increased over time and rose after recreational commercialization: **1.07 per 100,000 pre-commercialization → 2.22 per 100,000 post-commercialization** (Nevada, Q3 2017). (soh2024trendsofemergency pages 1-2)
- Demographic characteristics included a largest age group of **21–29 years (35.24% of CHS visits; n = 5,284)** and a lower proportion of males among CHS visits than comparator ED visits. (soh2024trendsofemergency pages 4-5, soh2024trendsofemergency pages 2-4)

### 9.2 Inheritance
CHS is best described as **multifactorial/complex**, with emerging candidate genetic susceptibility loci rather than Mendelian inheritance. (russo2024cannabinoidhyperemesissyndrome pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria (Rome IV highlight)
Rome IV criteria are summarized in reviews and include chronic cannabis use with stereotypical episodic vomiting and improvement with cessation; diagnostic features are summarized in review tables extracted from Loganathan et al. (2024). (perisetti2020cannabishyperemesissyndrome pages 5-6, loganathan2024acomprehensivereview media 73dc557e)

A Rome IV–style criteria summary reported in Perisetti et al. (2020) includes: onset ≥6 months before diagnosis; stereotypical episodes <1 week; ≥3 episodes/year; no vomiting between episodes; association with cannabis use and improvement after cessation. (perisetti2020cannabishyperemesissyndrome pages 5-6)

### 10.2 Differential diagnosis
A key clinical differential is **cyclic vomiting syndrome (CVS)**. Recent genetic discussion notes a CNR1 SNP association in CVS but not in tested CHS patients, supporting distinction. (russo2024cannabinoidhyperemesissyndrome pages 3-4)

### 10.3 Laboratory/ECG evaluation for complications and safety
- Given vomiting-associated electrolyte losses and antiemetic QT effects, recent guidance emphasizes checking metabolic panels and magnesium and considering ECG monitoring, particularly when using haloperidol. (merino2024mitigatingtherisk pages 6-7, merino2024mitigatingtherisk pages 9-10)

---

## 11. Outcome / Prognosis

### 11.1 Prognosis with and without cannabis cessation
- Symptom resolution after stopping cannabis was reported in **96.8%** of compiled cases in a systematic review, supporting cessation as the major determinant of remission. (sorensen2017cannabinoidhyperemesissyndrome pages 1-2)
- Morbidity can be substantial: dehydration, electrolyte disturbances, AKI, and esophageal injury are repeatedly reported complications. (perisetti2020cannabishyperemesissyndrome pages 5-6, moses2024exploringalternativetreatments pages 5-6)

### 11.2 Complication-focused statistics
- QTc prolongation is highlighted as a clinically important risk in adolescents/young adults with cannabis exposure and vomiting-related electrolyte disturbances, with severe cases of torsades reported in the literature review summarized by Merino et al. (2024). (merino2024mitigatingtherisk pages 1-2, merino2024mitigatingtherisk pages 4-5)

---

## 12. Treatment

### 12.1 Real-world implementation context
CHS is frequently encountered in emergency departments, where misdiagnosis and repeated negative workups are common; supportive care and targeted antiemetics are applied acutely, while long-term resolution typically requires cannabis cessation and behavioral support. (stumpf2021managementofcannabinoid pages 1-2, loganathan2024acomprehensivereview pages 11-12)

### 12.2 Acute management (supportive)
- IV fluids and electrolyte correction are foundational; monitoring for dehydration and electrolyte abnormalities is emphasized. (moses2024exploringalternativetreatments pages 5-6, merino2024mitigatingtherisk pages 6-7)

### 12.3 Acute pharmacotherapy with direct evidence
**Haloperidol (dopamine antagonist)**
- A randomized controlled trial summarized in Merino et al. (2024) found IV haloperidol (0.05–0.1 mg/kg) superior to ondansetron 8 mg IV for acute CHS: **lower rescue antiemetic use (31% vs 59%)** and **shorter ED stays (3.1 h vs 5.6 h)**. (merino2024mitigatingtherisk pages 4-5)
- Safety: QTc prolongation risk requires attention, especially with electrolyte disturbances; ECG monitoring is recommended for at-risk patients. (merino2024mitigatingtherisk pages 9-10, merino2024mitigatingtherisk pages 6-7)

**Topical capsaicin (TRPV1 agonist)**
- Pilot randomized evidence (summarized by Merino et al. 2024) indicates 0.1% capsaicin improved nausea at 60 minutes, with **29.4% complete nausea relief**; retrospective studies indicate reduced need for additional medications in some cohorts. (merino2024mitigatingtherisk pages 7-9, stumpf2021managementofcannabinoid pages 1-2)

**Benzodiazepines (e.g., lorazepam)**
- Frequently reported as effective, especially in pediatric/adolescent literature, and recommended as an alternative when QT risk is a concern. (merino2024mitigatingtherisk pages 6-7, merino2024mitigatingtherisk pages 9-10)

**NK-1 antagonists (aprepitant/fosaprepitant)**
- Emerging evidence supports use as an alternative with low cardiac risk; Merino et al. summarize response rates from related vomiting disorders and CHS-focused reports, including an adolescent abstract reporting **97% overall improvement**. (merino2024mitigatingtherisk pages 7-9)

**Olanzapine**
- Discussed as an alternative with relatively low QTc prolongation risk; CHS-specific dosing/efficacy remains limited. (merino2024mitigatingtherisk pages 7-9, merino2024mitigatingtherisk pages 9-10)

### 12.4 Definitive and long-term management
**Cannabis cessation** is the only consistently “proven” intervention and is tightly linked to symptom resolution and diagnostic confirmation. (russo2024cannabinoidhyperemesissyndrome pages 4-6, sorensen2017cannabinoidhyperemesissyndrome pages 1-2)

**Behavioral health / relapse prevention**
Recent reviews emphasize multimodal treatment addressing psychiatric comorbidity and substance use, using psychotherapy plus pharmacotherapy when appropriate. (loganathan2024acomprehensivereview pages 11-12)

### 12.5 Suggested MAXO terms (examples)
- Substance use cessation intervention; counseling; psychotherapy; IV fluid administration; electrolyte supplementation; ECG monitoring; topical medication administration; antipsychotic administration; benzodiazepine administration; neurokinin-1 receptor antagonist therapy. (loganathan2024acomprehensivereview pages 11-12, merino2024mitigatingtherisk pages 6-7)

---

## 13. Prevention

### 13.1 Primary prevention
Primary prevention is principally **avoiding chronic/heavy cannabis exposure** and education about CHS risk, especially in high-risk populations and in regions with increased access/potency. (soh2024trendsofemergency pages 1-2, loganathan2024acomprehensivereview pages 11-12)

### 13.2 Secondary/tertiary prevention
- Earlier recognition in ED/clinical settings may reduce repeated diagnostic testing and mitigate dehydration/electrolyte complications. (stumpf2021managementofcannabinoid pages 1-2, merino2024mitigatingtherisk pages 6-7)

---

## 14. Other Species / Natural Disease
No naturally occurring CHS analogs in other species were identified in the retrieved evidence for this run. (russo2024cannabinoidhyperemesissyndrome pages 6-7)

---

## 15. Model Organisms
No validated model organism systems that recapitulate CHS (cyclic vomiting with hot-bathing relief in the setting of chronic cannabinoid exposure) were identified in the retrieved evidence, although the mechanistic literature references cannabinoid antiemetic/proemetic biology in animal models in general terms. (russo2024cannabinoidhyperemesissyndrome pages 6-7)

---

## Recent developments (2023–2024) emphasized

1. **Administrative epidemiology linking legalization/commercialization with increasing ED burden:** Nevada interrupted time-series shows increased CHS ED visit rates post-commercialization (1.07 → 2.22 per 100,000). (Publication: 2024-05; URL https://doi.org/10.1371/journal.pone.0303205) (soh2024trendsofemergency pages 1-2)
2. **Safety-focused ED management refinements:** 2024 review stresses QTc/TdP risk with haloperidol in the context of electrolyte abnormalities and recommends structured monitoring and alternatives (capsaicin, aprepitant/fosaprepitant, lorazepam, olanzapine). (Publication: 2024-12; URL https://doi.org/10.3390/jcm14010163) (merino2024mitigatingtherisk pages 1-2, merino2024mitigatingtherisk pages 9-10)
3. **Emerging genetic susceptibility candidates:** 2024 Frontiers in Toxicology review reports associations with TRPV1, CYP2C9, COMT, DRD2, ABCA1 and proposes genomic testing as a future diagnostic adjunct (hypothesis-generating). (Publication: 2024-10; URL https://doi.org/10.3389/ftox.2024.1465728) (russo2024cannabinoidhyperemesissyndrome pages 1-2)
4. **Updated synthesis of ECS mechanisms and multi-modal management:** 2024 Pharmaceuticals review discusses ECS receptor biology, CB1R modulators, and integrated psychiatric/addiction management approaches. (Publication: 2024-11; URL https://doi.org/10.3390/ph17111549) (loganathan2024acomprehensivereview pages 1-2, loganathan2024acomprehensivereview pages 11-12)

---

## Limitations of this report (evidence availability)
- This run could not confirm authoritative **MONDO/MeSH/ICD identifiers** from primary ontology resources within retrieved full text; identifiers are therefore left unspecified rather than inferred. (soh2024trendsofemergency pages 2-4, soh2024trendsofemergency pages 5-7)
- Several potentially important 2024 EHR prevalence papers were not obtainable in full text via the tools during this run; Nevada statewide ED data and systematic review case-frequency data were used as primary quantitative sources. (soh2024trendsofemergency pages 1-2, sorensen2017cannabinoidhyperemesissyndrome pages 1-2)


References

1. (loganathan2024acomprehensivereview pages 1-2): Priyadarshini Loganathan, Mahesh Gajendran, and Hemant Goyal. A comprehensive review and update on cannabis hyperemesis syndrome. Pharmaceuticals, 17:1549, Nov 2024. URL: https://doi.org/10.3390/ph17111549, doi:10.3390/ph17111549. This article has 28 citations.

2. (sorensen2017cannabinoidhyperemesissyndrome pages 1-2): Cecilia J. Sorensen, Kristen DeSanto, Laura Borgelt, Kristina T. Phillips, and Andrew A. Monte. Cannabinoid hyperemesis syndrome: diagnosis, pathophysiology, and treatment—a systematic review. Journal of Medical Toxicology, 13:71-87, Dec 2017. URL: https://doi.org/10.1007/s13181-016-0595-z, doi:10.1007/s13181-016-0595-z. This article has 461 citations.

3. (perisetti2020cannabishyperemesissyndrome pages 5-6): A. Perisetti, M. Gajendran, C. Dasari, P. Bansal, Muhammad Aziz, Sumant Inamdar, B. Tharian, and H. Goyal. Cannabis hyperemesis syndrome: an update on the pathophysiology and management. Annals of Gastroenterology, 33:571-578, Sep 2020. URL: https://doi.org/10.20524/aog.2020.0528, doi:10.20524/aog.2020.0528. This article has 101 citations.

4. (senderovich2022asystematicreview pages 1-2): Helen Senderovich, Preet Patel, Briam Jimenez Lopez, and Sarah Waicus. A systematic review on cannabis hyperemesis syndrome and its management options. Medical Principles and Practice, 31:29-38, Nov 2022. URL: https://doi.org/10.1159/000520417, doi:10.1159/000520417. This article has 50 citations and is from a peer-reviewed journal.

5. (stumpf2021managementofcannabinoid pages 2-3): Janice L. Stumpf and Lauren D. Williams. Management of cannabinoid hyperemesis syndrome: focus on capsaicin. Journal of Pharmacy Practice, 34:786-793, Jul 2021. URL: https://doi.org/10.1177/0897190020934289, doi:10.1177/0897190020934289. This article has 22 citations and is from a peer-reviewed journal.

6. (stumpf2021managementofcannabinoid pages 1-2): Janice L. Stumpf and Lauren D. Williams. Management of cannabinoid hyperemesis syndrome: focus on capsaicin. Journal of Pharmacy Practice, 34:786-793, Jul 2021. URL: https://doi.org/10.1177/0897190020934289, doi:10.1177/0897190020934289. This article has 22 citations and is from a peer-reviewed journal.

7. (moses2024exploringalternativetreatments pages 5-6): Tabitha E H Moses. Exploring alternative treatments for acute exacerbations of cannabis hyperemesis syndrome in patients who plan to continue using cannabis. Clinical Research In Practice: The Journal of Team Hippocrates, Nov 2024. URL: https://doi.org/10.22237/crp/1724285340, doi:10.22237/crp/1724285340. This article has 0 citations.

8. (merino2024mitigatingtherisk pages 1-2): Sandra Merino, Lissette Tordera, Allison Jun, and Sun Yang. Mitigating the risk of qtc prolongation when using haloperidol for acute treatment of cannabinoid hyperemesis syndrome in adolescents and young adults. Journal of Clinical Medicine, 14:163, Dec 2024. URL: https://doi.org/10.3390/jcm14010163, doi:10.3390/jcm14010163. This article has 4 citations.

9. (merino2024mitigatingtherisk pages 4-5): Sandra Merino, Lissette Tordera, Allison Jun, and Sun Yang. Mitigating the risk of qtc prolongation when using haloperidol for acute treatment of cannabinoid hyperemesis syndrome in adolescents and young adults. Journal of Clinical Medicine, 14:163, Dec 2024. URL: https://doi.org/10.3390/jcm14010163, doi:10.3390/jcm14010163. This article has 4 citations.

10. (merino2024mitigatingtherisk pages 6-7): Sandra Merino, Lissette Tordera, Allison Jun, and Sun Yang. Mitigating the risk of qtc prolongation when using haloperidol for acute treatment of cannabinoid hyperemesis syndrome in adolescents and young adults. Journal of Clinical Medicine, 14:163, Dec 2024. URL: https://doi.org/10.3390/jcm14010163, doi:10.3390/jcm14010163. This article has 4 citations.

11. (moses2024exploringalternativetreatments pages 1-3): Tabitha E H Moses. Exploring alternative treatments for acute exacerbations of cannabis hyperemesis syndrome in patients who plan to continue using cannabis. Clinical Research In Practice: The Journal of Team Hippocrates, Nov 2024. URL: https://doi.org/10.22237/crp/1724285340, doi:10.22237/crp/1724285340. This article has 0 citations.

12. (merino2024mitigatingtherisk pages 9-10): Sandra Merino, Lissette Tordera, Allison Jun, and Sun Yang. Mitigating the risk of qtc prolongation when using haloperidol for acute treatment of cannabinoid hyperemesis syndrome in adolescents and young adults. Journal of Clinical Medicine, 14:163, Dec 2024. URL: https://doi.org/10.3390/jcm14010163, doi:10.3390/jcm14010163. This article has 4 citations.

13. (soh2024trendsofemergency pages 1-2): Jaeseung Soh, Yonsu Kim, Jay Shen, Mingon Kang, Stefan Chaudhry, Tae Ha Chung, Seo Hyun Kim, Yena Hwang, Daniel Lim, Adam Khattak, Leora Frimer, and Ji Won Yoo. Trends of emergency department visits for cannabinoid hyperemesis syndrome in nevada: an interrupted time series analysis. PLOS ONE, 19:e0303205, May 2024. URL: https://doi.org/10.1371/journal.pone.0303205, doi:10.1371/journal.pone.0303205. This article has 12 citations and is from a peer-reviewed journal.

14. (soh2024trendsofemergency pages 2-4): Jaeseung Soh, Yonsu Kim, Jay Shen, Mingon Kang, Stefan Chaudhry, Tae Ha Chung, Seo Hyun Kim, Yena Hwang, Daniel Lim, Adam Khattak, Leora Frimer, and Ji Won Yoo. Trends of emergency department visits for cannabinoid hyperemesis syndrome in nevada: an interrupted time series analysis. PLOS ONE, 19:e0303205, May 2024. URL: https://doi.org/10.1371/journal.pone.0303205, doi:10.1371/journal.pone.0303205. This article has 12 citations and is from a peer-reviewed journal.

15. (soh2024trendsofemergency pages 4-5): Jaeseung Soh, Yonsu Kim, Jay Shen, Mingon Kang, Stefan Chaudhry, Tae Ha Chung, Seo Hyun Kim, Yena Hwang, Daniel Lim, Adam Khattak, Leora Frimer, and Ji Won Yoo. Trends of emergency department visits for cannabinoid hyperemesis syndrome in nevada: an interrupted time series analysis. PLOS ONE, 19:e0303205, May 2024. URL: https://doi.org/10.1371/journal.pone.0303205, doi:10.1371/journal.pone.0303205. This article has 12 citations and is from a peer-reviewed journal.

16. (merino2024mitigatingtherisk pages 7-9): Sandra Merino, Lissette Tordera, Allison Jun, and Sun Yang. Mitigating the risk of qtc prolongation when using haloperidol for acute treatment of cannabinoid hyperemesis syndrome in adolescents and young adults. Journal of Clinical Medicine, 14:163, Dec 2024. URL: https://doi.org/10.3390/jcm14010163, doi:10.3390/jcm14010163. This article has 4 citations.

17. (russo2024cannabinoidhyperemesissyndrome pages 4-6): Ethan B. Russo and Venetia L. Whiteley. Cannabinoid hyperemesis syndrome: genetic susceptibility to toxic exposure. Frontiers in Toxicology, Oct 2024. URL: https://doi.org/10.3389/ftox.2024.1465728, doi:10.3389/ftox.2024.1465728. This article has 11 citations.

18. (loganathan2024acomprehensivereview pages 11-12): Priyadarshini Loganathan, Mahesh Gajendran, and Hemant Goyal. A comprehensive review and update on cannabis hyperemesis syndrome. Pharmaceuticals, 17:1549, Nov 2024. URL: https://doi.org/10.3390/ph17111549, doi:10.3390/ph17111549. This article has 28 citations.

19. (loganathan2024acomprehensivereview media 73dc557e): Priyadarshini Loganathan, Mahesh Gajendran, and Hemant Goyal. A comprehensive review and update on cannabis hyperemesis syndrome. Pharmaceuticals, 17:1549, Nov 2024. URL: https://doi.org/10.3390/ph17111549, doi:10.3390/ph17111549. This article has 28 citations.

20. (loganathan2024acomprehensivereview media 15f1dbc6): Priyadarshini Loganathan, Mahesh Gajendran, and Hemant Goyal. A comprehensive review and update on cannabis hyperemesis syndrome. Pharmaceuticals, 17:1549, Nov 2024. URL: https://doi.org/10.3390/ph17111549, doi:10.3390/ph17111549. This article has 28 citations.

21. (soh2024trendsofemergency pages 5-7): Jaeseung Soh, Yonsu Kim, Jay Shen, Mingon Kang, Stefan Chaudhry, Tae Ha Chung, Seo Hyun Kim, Yena Hwang, Daniel Lim, Adam Khattak, Leora Frimer, and Ji Won Yoo. Trends of emergency department visits for cannabinoid hyperemesis syndrome in nevada: an interrupted time series analysis. PLOS ONE, 19:e0303205, May 2024. URL: https://doi.org/10.1371/journal.pone.0303205, doi:10.1371/journal.pone.0303205. This article has 12 citations and is from a peer-reviewed journal.

22. (russo2024cannabinoidhyperemesissyndrome pages 3-4): Ethan B. Russo and Venetia L. Whiteley. Cannabinoid hyperemesis syndrome: genetic susceptibility to toxic exposure. Frontiers in Toxicology, Oct 2024. URL: https://doi.org/10.3389/ftox.2024.1465728, doi:10.3389/ftox.2024.1465728. This article has 11 citations.

23. (russo2024cannabinoidhyperemesissyndrome pages 2-3): Ethan B. Russo and Venetia L. Whiteley. Cannabinoid hyperemesis syndrome: genetic susceptibility to toxic exposure. Frontiers in Toxicology, Oct 2024. URL: https://doi.org/10.3389/ftox.2024.1465728, doi:10.3389/ftox.2024.1465728. This article has 11 citations.

24. (russo2024cannabinoidhyperemesissyndrome pages 1-2): Ethan B. Russo and Venetia L. Whiteley. Cannabinoid hyperemesis syndrome: genetic susceptibility to toxic exposure. Frontiers in Toxicology, Oct 2024. URL: https://doi.org/10.3389/ftox.2024.1465728, doi:10.3389/ftox.2024.1465728. This article has 11 citations.

25. (russo2024cannabinoidhyperemesissyndrome pages 6-7): Ethan B. Russo and Venetia L. Whiteley. Cannabinoid hyperemesis syndrome: genetic susceptibility to toxic exposure. Frontiers in Toxicology, Oct 2024. URL: https://doi.org/10.3389/ftox.2024.1465728, doi:10.3389/ftox.2024.1465728. This article has 11 citations.

26. (loganathan2024acomprehensivereview pages 2-4): Priyadarshini Loganathan, Mahesh Gajendran, and Hemant Goyal. A comprehensive review and update on cannabis hyperemesis syndrome. Pharmaceuticals, 17:1549, Nov 2024. URL: https://doi.org/10.3390/ph17111549, doi:10.3390/ph17111549. This article has 28 citations.
