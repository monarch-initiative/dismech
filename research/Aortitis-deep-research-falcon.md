---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:13:52.374666'
end_time: '2026-05-05T23:44:14.822781'
duration_seconds: 1822.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aortitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aortitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Aortitis** covering all of the
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
- **Disease Name:** Aortitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Aortitis** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Aortitis

### Scope note and evidence constraints
Aortitis is an umbrella term covering multiple etiologies (infectious and noninfectious). The evidence retrieved for this run is strongest for (i) **large-vessel vasculitis (LVV)-associated aortitis** (GCA, Takayasu) and imaging guidance (EULAR 2023 systematic review/meta-analysis), (ii) **clinically isolated aortitis (CIA)** detected on surgical histology (single-center cohort 2024), (iii) **infectious aortitis** as a diagnostic/treatment “mimicker” (case-based review 2025), and (iv) **drug-induced aortitis** (G-CSF-associated, 2024 systematic case review). Explicit ICD-10/ICD-11, MeSH Unique IDs, MONDO and Orphanet identifiers were **not present** in the retrieved full texts; therefore, ontology coding in this report is limited to **ontology term suggestions** (HPO/GO/CL/UBERON/MAXO) rather than confirmed IDs from those ontologies. (staniforth2024aortitisincreasesthe pages 9-11, staniforth2024aortitisincreasesthe pages 2-4)

---

## 1. Disease Information

### 1.1 Overview / definition
**Aortitis** is explicitly defined as **“inflammation of the aorta”**. (staniforth2024aortitisincreasesthe pages 1-2)

Clinically, it is best conceptualized as a **syndrome** with divergent causes and management imperatives (e.g., immunosuppression for inflammatory aortitis vs antimicrobials ± surgery for infectious aortitis). (arcilla2025thegreatvasculitis pages 7-9, staniforth2024aortitisincreasesthe pages 1-2)

### 1.2 Key identifiers (requested: OMIM/Orphanet/ICD/MeSH/MONDO)
- **Not found in retrieved texts:** ICD-10/ICD-11 codes, MeSH headings/unique IDs, MONDO IDs, Orphanet IDs. (staniforth2024aortitisincreasesthe pages 9-11, staniforth2024aortitisincreasesthe pages 2-4)
- **Common literature labels/synonyms used in retrieved texts** (non-exhaustive):
  - Aortitis; **infectious aortitis**; **noninfectious aortitis**; **inflammatory aortitis**; **clinically isolated aortitis (CIA)**; “idiopathic aortitis”; “giant cell aortitis”. (staniforth2024aortitisincreasesthe pages 1-2, staniforth2024aortitisincreasesthe pages 9-11, staniforth2024aortitisincreasesthe pages 2-4)

### 1.3 Evidence sources
The information here is derived from **aggregated disease-level resources** (systematic reviews, narrative reviews, cohort studies) and **case-based reviews**; several sources are surgical-cohort based (histology from aortic resections) and thus reflect a selected population (patients undergoing major aortic surgery). (staniforth2024aortitisincreasesthe pages 1-2, bosch2023imagingindiagnosis pages 1-2, arcilla2025thegreatvasculitis pages 7-9)

---

## 2. Etiology

### 2.1 Major causal categories
1. **Noninfectious (immune-mediated) aortitis**
   - Large-vessel vasculitis: **Giant cell arteritis (GCA)**, **Takayasu arteritis (TAK)**, and variable-vessel vasculitis such as **Behçet disease** can involve the aorta/major branches. (popescu2024imaginginlarge pages 4-5)
   - **Clinically isolated aortitis (CIA)**: defined as aortitis **without systemic vasculitis or other inflammatory conditions**, often detected on histology after aortic surgery. (staniforth2024aortitisincreasesthe pages 1-2)
   - IgG4-related periaortitis/aortitis is a distinct fibro-inflammatory entity (review evidence retrieved is 2025). (wang2025unravelingthecomplexity pages 6-7)

2. **Infectious aortitis**
   - Pathogens include **Salmonella**, **Staphylococcus aureus**, **Streptococcus spp.**, **Enterococcus**, **Haemophilus influenzae**, **Mycobacterium tuberculosis**, **Treponema pallidum**, fungi, and others; infection can seed damaged aortic wall (e.g., atherosclerosis) with pseudoaneurysm formation and high rupture risk. (arcilla2025thegreatvasculitis pages 7-9, arcilla2025thegreatvasculitis pages 6-7)

3. **Drug-induced aortitis**
   - **G-CSF–induced aortitis** has been characterized through systematic case aggregation, particularly in chemotherapy settings. (zhao2024literaturereviewanalysis pages 1-2, zhao2024literaturereviewanalysis pages 5-7)

### 2.2 Risk factors
- **CIA/noninfectious surgical aortitis (surgical cohort):** increased age, female sex, current smoking, and prior inflammatory disease were associated with histologic aortitis; bicuspid aortic valve was associated with reduced odds in that cohort. (staniforth2024aortitisincreasesthe pages 6-8)
- **Infectious aortitis:** risk factors include trauma, atherosclerotic plaques, congenital malformations, immunosuppression, infections, and malignancy. (arcilla2025thegreatvasculitis pages 1-3)
- **G-CSF–induced:** predominantly older women; common setting is breast cancer chemotherapy; geographic clustering in East Asia reported in the case-review dataset. (zhao2024literaturereviewanalysis pages 1-2, zhao2024literaturereviewanalysis pages 2-3)

### 2.3 Protective factors
A bicuspid aortic valve was associated with **lower likelihood** of histologic aortitis in a surgical cohort (association, not necessarily causal protection). (staniforth2024aortitisincreasesthe pages 6-8)

### 2.4 Gene–environment interactions
Direct gene–environment interaction studies specific to “aortitis” were not retrieved. However, TAK genetic susceptibility (e.g., MLX variant; HLA associations) plausibly interacts with inflammatory triggers; infectious mimics can also induce autoantibodies and confound immune phenotyping. (tamura2018singlenucleotidepolymorphismof pages 6-7, arcilla2025thegreatvasculitis pages 7-9)

---

## 3. Phenotypes (with HPO suggestions)

Aortitis phenotypes vary by etiology and vascular territory involved. A curated phenotype-to-HPO mapping table is provided below.

| Phenotype (plain) | HPO term(s) suggestion | Evidence details (including onset/course, frequencies, quantitative lab values) | Major etiologies/subtypes where seen | Key citations (pqac ids) |
|---|---|---|---|---|
| Constitutional symptoms / malaise / fatigue / weight loss | HP:0012378 Fatigue; HP:0004305 Malaise; HP:0001824 Weight loss | Aortitis often presents nonspecifically with fatigue, feeling generally ill, and weight loss; GCA usually has gradual onset over weeks to months; TAK has a prodromal constitutional phase; IgG4-related PAO/PA also includes fatigue/weight loss/malaise; Behçet often relapsing-remitting | General aortitis, GCA, TAK, IgG4-related aortitis, Behçet disease | (staniforth2024aortitisincreasesthe pages 1-2, popescu2024imaginginlarge pages 4-5, wang2025unravelingthecomplexity pages 6-7) |
| Fever | HP:0001945 Fever | Fever is common in GCA and TAK constitutional phases; in G-CSF-induced aortitis, 68/72 (96%) were symptomatic, commonly with fever; mean temperatures around 38.6°C; infectious aortitis also commonly presents with systemic inflammatory illness | GCA, TAK, G-CSF-induced aortitis, infectious aortitis | (popescu2024imaginginlarge pages 4-5, zhao2024literaturereviewanalysis pages 5-7, arcilla2025thegreatvasculitis pages 7-9) |
| Pain (chest, back, abdominal, neck, sore throat) | HP:0100749 Chest pain; HP:0002027 Abdominal pain; HP:0003418 Back pain; HP:0003202 Cervical pain | G-CSF-induced aortitis commonly caused fever plus pain (chest, back, abdominal, neck, sore throat); IgG4-related PAO/PA commonly causes abdominal or back pain; thoracic involvement may cause chest pain and dyspnea | G-CSF-induced aortitis, IgG4-related aortitis/periaortitis | (zhao2024literaturereviewanalysis pages 5-7, wang2025unravelingthecomplexity pages 6-7) |
| Polymyalgia-type proximal stiffness | HP:0002829 Arthralgia; HP:0003326 Myalgia | Noninfectious aortitis may include polymyalgic symptoms with proximal shoulder/pelvic girdle stiffness; polymyalgia rheumatica co-occurs in 40–60% of GCA | Noninfectious aortitis, especially GCA-associated aortitis | (staniforth2024aortitisincreasesthe pages 1-2, popescu2024imaginginlarge pages 4-5) |
| Headache | HP:0002315 Headache | GCA cranial phenotype includes headache; onset usually gradual over weeks to months, though ~20% may be abrupt | GCA-associated aortitis/large-vessel GCA | (popescu2024imaginginlarge pages 4-5) |
| Jaw or tongue claudication | HP:0200044 Jaw claudication | Characteristic cranial ischemic symptom in GCA; occurs with chewing and supports cranial involvement in patients who may also have aortitis/large-vessel disease | GCA-associated aortitis | (popescu2024imaginginlarge pages 4-5) |
| Visual loss / ischemic optic neuropathy | HP:0000572 Visual loss; HP:0000648 Optic atrophy (suggestive downstream term if chronic) | In GCA, vascular occlusion can cause cranial ischemia and ischemic optic neuropathy; vision loss is typically painless and irreversible; ischemic optic neuropathy reported in ~14% in imaging review context | GCA-associated aortitis/large-vessel GCA | (popescu2024imaginginlarge pages 4-5) |
| Limb claudication / arm or leg claudication | HP:0004936 Intermittent claudication | Aortic or main-branch involvement in GCA can cause limb claudication; TAK vascular phase includes arm or leg claudication; IgG4 iliac/femoral disease can also cause claudication | GCA, TAK, IgG4-related aortitis | (popescu2024imaginginlarge pages 4-5, chan2025strokeaorticregurgitation pages 2-4, wang2025unravelingthecomplexity pages 6-7) |
| Pulseless vascular phase / pulse deficits | HP:0031808 Abnormality of peripheral pulse | TAK classically progresses from a constitutional “pre-pulseless” phase to a “pulseless” vascular phase with stenotic lesions in >90% | TAK-associated aortitis | (popescu2024imaginginlarge pages 4-5) |
| Hypertension | HP:0000822 Hypertension | Common in TAK (30–90%); IgG4-related renal artery involvement can also cause hypertension | TAK, IgG4-related aortitis | (popescu2024imaginginlarge pages 4-5, wang2025unravelingthecomplexity pages 6-7) |
| Stroke / transient ischemic attack | HP:0001297 Stroke; HP:0002326 Transient ischemic attack | TIAs/strokes occur in 2–7% of GCA and 10–20% of TAK; aortitis cohorts also report increased stroke risk during follow-up | GCA, TAK, general aortitis complications | (popescu2024imaginginlarge pages 4-5, staniforth2024aortitisincreasesthe pages 8-9) |
| Mucocutaneous ulcers | HP:0000197 Oral ulcer; HP:0000135 Genital ulcer | Behçet disease phenotype includes oral and genital ulcers with frequent relapses/remissions and potential large-vessel aortitis/aneurysm/thrombosis | Behçet disease-associated aortitis | (popescu2024imaginginlarge pages 4-5) |
| Uveitis / ocular inflammation | HP:0000554 Uveitis | Behçet disease includes uveitis as a key systemic phenotype accompanying possible large-vessel complications | Behçet disease-associated aortitis | (popescu2024imaginginlarge pages 4-5) |
| Thrombosis / occlusion | HP:0004930 Venous thrombosis; HP:0012393 Arterial thrombosis; HP:0004417 Vascular occlusion | Behçet large-vessel involvement may include thrombosis and occlusion; aortitis overall can cause stenosis/occlusion; infectious aortitis can present with pseudoaneurysm and occlusive thrombus | Behçet disease, infectious aortitis, general aortitis | (popescu2024imaginginlarge pages 4-5, staniforth2024aortitisincreasesthe pages 1-2, arcilla2025thegreatvasculitis pages 7-9) |
| Elevated CRP / ESR / inflammatory markers | HP:0011227 Elevated C-reactive protein level; HP:0003565 Increased erythrocyte sedimentation rate | Aortitis workup commonly shows high inflammatory markers; G-CSF-induced cases had CRP means ~26.06 ± 15.39 mg/dL (filgrastim), 24.81 ± 9.65 mg/dL (pegfilgrastim), 10.45 ± 9.91 mg/dL (lenograstim); giant cell aortitis case had CRP 82 mg/L and ESR 140 mm/h | General aortitis, G-CSF-induced aortitis, giant cell aortitis case, IgG4-related aortitis | (staniforth2024aortitisincreasesthe pages 1-2, zhao2024literaturereviewanalysis pages 5-7, chan2025strokeaorticregurgitation pages 2-4, wang2025unravelingthecomplexity pages 6-7) |
| Leukocytosis | HP:0001974 Leukocytosis | Reported as a common laboratory abnormality in infectious/inflammatory aortitis differential workup | Infectious aortitis and mimics | (arcilla2025thegreatvasculitis pages 7-9) |
| Thrombocytosis | HP:0001873 Thrombocytosis | Mild-to-moderate thrombocytosis reported in infectious/inflammatory aortitis differential workup | Infectious aortitis and mimics | (arcilla2025thegreatvasculitis pages 7-9) |
| Normocytic/normochromic anemia | HP:0001877 Abnormality of erythrocytes; HP:0001892 Normocytic anemia | Normochromic/normocytic anemia described among laboratory abnormalities in infectious/inflammatory aortitis evaluation | Infectious aortitis and mimics | (arcilla2025thegreatvasculitis pages 7-9) |
| Hypoalbuminemia | HP:0003073 Hypoalbuminemia | Reported among laboratory abnormalities in infectious/inflammatory aortitis differential workup | Infectious aortitis and mimics | (arcilla2025thegreatvasculitis pages 7-9) |
| Polyclonal hypergammaglobulinemia | HP:0003237 Hypergammaglobulinemia | Reported in inflammatory/infectious aortitis differential workup | Infectious/inflammatory aortitis | (arcilla2025thegreatvasculitis pages 7-9) |
| Aortic aneurysm | HP:0002617 Aortic aneurysm | A major downstream complication across aortitis subtypes. In surgical cohort, re-operations for new aneurysm formation were increased (14% with aortitis vs 3.8% without); GCA CT study reported >20% (12/54) developing aneurysm after 4–10 years; Behçet and infectious aortitis also associated with aneurysms | General aortitis, GCA, Behçet, infectious aortitis, IgG4-related aortitis | (staniforth2024aortitisincreasesthe pages 4-6, popescu2024imaginginlarge pages 7-9, popescu2024imaginginlarge pages 4-5, arcilla2025thegreatvasculitis pages 7-9, wang2025unravelingthecomplexity pages 6-7) |
| Aortic dissection | HP:0002647 Aortic dissection | Aortitis may present as dissection; G-CSF-induced review documented dissections among complications; giant cell aortitis case involved aneurysmal/root pathology; infectious/IgG4-related disease can also progress to dissection | General aortitis, G-CSF-induced, giant cell aortitis, IgG4-related aortitis | (staniforth2024aortitisincreasesthe pages 1-2, zhao2024literaturereviewanalysis pages 5-7, chan2025strokeaorticregurgitation pages 2-4, wang2025unravelingthecomplexity pages 6-7) |
| Stenosis / arterial narrowing / occlusion | HP:0005290 Arterial stenosis; HP:0004417 Vascular occlusion | Aortitis can cause wall thickening, loss of elasticity, stenosis, and occlusion; TAK has stenotic lesions in >90%; CTA shows luminal stenosis/narrowing | General aortitis, TAK, infectious aortitis | (staniforth2024aortitisincreasesthe pages 1-2, popescu2024imaginginlarge pages 4-5, popescu2024imaginginlarge pages 5-7) |
| Aortic regurgitation | HP:0001659 Aortic valve regurgitation | Case report of giant cell aortitis described severe aortic regurgitation with aortic root aneurysm and destructive transmural inflammation; MLX variant study in TAK linked severity with aortic regurgitation morbidity | Giant cell aortitis case, Takayasu arteritis | (chan2025strokeaorticregurgitation pages 2-4) |
| Dyspnea / compressive thoracic symptoms | HP:0002094 Dyspnea | Thoracic IgG4-related lesions may cause chest pain, dyspnea, and mediastinal compression; may reflect advanced local disease | IgG4-related aortitis/periaortitis | (wang2025unravelingthecomplexity pages 6-7) |
| Abdominal angina / bowel ischemia | HP:0031106 Intestinal ischemia; HP:0002574 Abdominal pain | Mesenteric involvement in IgG4-related disease may cause abdominal angina or bowel ischemia | IgG4-related aortitis/periaortitis | (wang2025unravelingthecomplexity pages 6-7) |
| Renal ischemia / hydronephrosis / renal injury | HP:0000105 Renal insufficiency; HP:0000126 Hydronephrosis | IgG4-related renal artery/periaortic involvement can cause ischemic nephropathy, post-obstructive hydronephrosis, and potentially permanent renal injury | IgG4-related aortitis/periaortitis | (wang2025unravelingthecomplexity pages 6-7) |


*Table: This table summarizes key clinical, laboratory, and complication phenotypes reported for aortitis across major etiologic subtypes, with suggested HPO mappings. It is useful for disease knowledge-base curation because it links observed features to onset/course details, frequencies where available, and source-backed evidence.*

Key phenotype highlights with quantitative data (when available):
- **GCA:** gradual onset over weeks–months (≈20% abrupt), cranial/constitutional symptoms; polymyalgia rheumatica in **40–60%**; TIAs/strokes **2–7%**; aortic/major branch involvement **27%**. (popescu2024imaginginlarge pages 4-5)
- **TAK:** constitutional phase → pulseless vascular phase; stenotic lesions **>90%**; aneurysms ≈**25%**; hypertension **30–90%**; stroke/TIA **10–20%**. (popescu2024imaginginlarge pages 4-5)
- **Behçet:** large vascular involvement up to **40%**; mortality ≈**4%**; frequent relapsing course. (popescu2024imaginginlarge pages 4-5)
- **G-CSF–induced aortitis:** symptomatic in **96% (68/72)**; fever and pain common; CRP markedly elevated; blood cultures uniformly negative in the compiled case series. (zhao2024literaturereviewanalysis pages 5-7)

Quality-of-life measures (EQ-5D/SF-36/PROMIS) were not reported in the retrieved texts; QoL impact is inferred from chronicity/relapse and major vascular complications rather than quantified. (popescu2024imaginginlarge pages 4-5, staniforth2024aortitisincreasesthe pages 8-9)

---

## 4. Genetic / Molecular Information

### 4.1 Genetic susceptibility (human)
- **GCA:** HLA association reported with **HLA-DRB*04**; non-HLA polymorphisms noted in a narrative imaging review include **PTPN22, NOS2, ERAP1, REL, PRKQC**. (popescu2024imaginginlarge pages 4-5)
- **TAK:** persistent genetic risk at **HLA-B*52:01** and susceptibility loci (HLA-B/MICA; HLA-DQB1/HLA-DRB1) were reported in review; a mechanistic genetics study links **MLX rs665268 (Q139R)** to TAK severity and aortic regurgitation. (popescu2024imaginginlarge pages 4-5, tamura2018singlenucleotidepolymorphismof pages 2-3)
- **Behçet disease:** susceptibility at MHC class I, notably **HLA-B51**. (popescu2024imaginginlarge pages 4-5)

### 4.2 Mechanistic pathways and causal chains
- **TAK MLX-Q139R → inflammasome axis (primary research):** MLX-Q139R increases MondoA–MLX activity, upregulates **TXNIP**, and promotes **NLRP3 inflammasome** activation with increased IL-1β, oxidative stress, and impaired autophagy (mTOR axis), supporting a causal chain from genotype to macrophage-driven vascular inflammation. (tamura2018singlenucleotidepolymorphismof pages 6-7, tamura2018singlenucleotidepolymorphismof pages 2-3)
- **GCA vascular immunopathology (review evidence retrieved is 2026):** initiation includes activation of arterial-wall dendritic cells, T cell invasion enabled by monocyte-derived MMP-9, NETs, macrophage polarization, and tertiary lymphoid organ signals (CXCL13/BAFF/APRIL/LT-β), implicating innate and adaptive immune circuits and stromal remodeling. (muratore2026treatmentstrategiesin pages 29-33)

### 4.3 Suggested GO biological processes and CL cell types
(These are **suggested ontology mappings** based on mechanisms described in retrieved sources.)
- **GO terms (suggested):** inflammatory response; granulomatous inflammatory response; leukocyte migration; cytokine-mediated signaling pathway; inflammasome complex assembly; autophagy; extracellular matrix organization; angiogenesis/neovascularization. (popescu2024imaginginlarge pages 4-5, tamura2018singlenucleotidepolymorphismof pages 6-7, muratore2026treatmentstrategiesin pages 29-33)
- **CL terms (suggested):** macrophage / monocyte-derived macrophage; CD4-positive T cell; CD8-positive T cell; dendritic cell (arterial wall); neutrophil; B cell; vascular endothelial cell; vascular smooth muscle cell; fibroblast. (tamura2018singlenucleotidepolymorphismof pages 6-7, muratore2026treatmentstrategiesin pages 29-33)

---

## 5. Environmental Information

### 5.1 Infectious agents
Infectious aortitis pathogens frequently cited include **Salmonella**, **Staphylococcus aureus**, **Streptococcus spp.**, **Enterococcus**, **Haemophilus influenzae**, **Mycobacterium tuberculosis**, **Treponema pallidum**, fungi, and others. (arcilla2025thegreatvasculitis pages 7-9, arcilla2025thegreatvasculitis pages 6-7)

### 5.2 Drug exposure
G-CSF exposure (notably pegfilgrastim) is associated with rare aortitis, most commonly presenting within days after dosing in the compiled case series (agent-dependent mean onset times). (zhao2024literaturereviewanalysis pages 5-7)

Lifestyle/environmental risks (e.g., smoking) were associated with surgical-cohort aortitis risk. (staniforth2024aortitisincreasesthe pages 6-8)

---

## 6. Mechanism / Pathophysiology

### 6.1 Upstream-to-downstream causal chain (integrated)
Aortitis pathophysiology can be summarized as:
1. **Trigger/etiology** (autoimmune LVV, infection, drug-induced immune activation) →
2. **Aortic wall inflammation** (granulomatous inflammation in GCA/TAK; neutrophil-predominant infiltration in infection; IgG4+ lymphoplasmacytic infiltration with storiform fibrosis in IgG4-RD) →
3. **Structural remodeling** (intimal hyperplasia, neovascularization, fibrosis; medial degradation) →
4. **Clinical consequences**: aneurysm, dissection, stenosis/occlusion, ischemia, stroke, valve involvement (aortic regurgitation), rupture. (popescu2024imaginginlarge pages 4-5, arcilla2025thegreatvasculitis pages 7-9, wang2025unravelingthecomplexity pages 6-7, staniforth2024aortitisincreasesthe pages 1-2)

### 6.2 Tissue damage mechanisms
- **Stenosis/occlusion** and **aneurysm/dissection** arise from wall thickening, loss of elasticity, and inflammatory destruction/remodeling. (staniforth2024aortitisincreasesthe pages 1-2, popescu2024imaginginlarge pages 4-5)
- **Infectious aortitis** often produces pseudoaneurysm and saccular morphology, with rupture risk heightened by wall necrosis and gas/edema/fat stranding in periaortic tissues. (arcilla2025thegreatvasculitis pages 7-9)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- Primary: aorta and major branches (cardiovascular system). (staniforth2024aortitisincreasesthe pages 1-2, popescu2024imaginginlarge pages 4-5)
- Secondary/complications: heart valves (aortic regurgitation), brain (stroke), kidneys (renal ischemia/hydronephrosis in IgG4-related disease), bowel (mesenteric ischemia). (chan2025strokeaorticregurgitation pages 2-4, popescu2024imaginginlarge pages 4-5, wang2025unravelingthecomplexity pages 6-7)

### 7.2 Suggested UBERON terms (not exhaustive; suggestions)
- UBERON:0000947 (aorta), plus segment-level (thoracic aorta, abdominal aorta), and branch arteries (subclavian, axillary, carotid) depending on phenotype. Imaging reviews emphasize aorta and its branches. (popescu2024imaginginlarge pages 1-2, popescu2024imaginginlarge pages 7-9)

---

## 8. Temporal Development

- **GCA:** typically subacute onset over weeks–months; may be abrupt (~20%). (popescu2024imaginginlarge pages 4-5)
- **TAK:** constitutional “pre-pulseless” phase progressing to “pulseless” vascular phase with chronic stenosis/aneurysm complications. (popescu2024imaginginlarge pages 4-5)
- **CIA:** frequently asymptomatic until incidentally found on surgical pathology; requires prolonged surveillance due to late complications. (staniforth2024aortitisincreasesthe pages 1-2, staniforth2024aortitisincreasesthe pages 8-9)
- **G-CSF-induced:** onset typically within days after exposure (agent-specific mean onset times in case review). (zhao2024literaturereviewanalysis pages 5-7)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (selected quantitative data from retrieved sources)
- **Histology-confirmed aortitis in major aortic surgery:** prevalence **10.6% (57/537)** with **75% CIA**, in a single-center cohort with high sampling rate (88%). (staniforth2024aortitisincreasesthe pages 1-2)
- **GCA:** incidence about **44 per 100,000 persons >50** (Northern Europe) and prevalence estimates in another PET-focused review as 9–25 per 100,000 (>50). (popescu2024imaginginlarge pages 1-2, nassarmadji202318fluorodeoxyglucosepositronemission pages 1-2)
- **TAK:** annual incidence **0.4–3.4 per 1,000,000**. (popescu2024imaginginlarge pages 1-2)

### 9.2 Population/sex patterns
- CIA/surgical cohort aortitis associated with female sex. (staniforth2024aortitisincreasesthe pages 6-8)
- G-CSF-induced aortitis: ~81% female with mean age ~62 years in compiled case series. (zhao2024literaturereviewanalysis pages 1-2)

---

## 10. Diagnostics

### 10.1 Laboratory evaluation (common elements)
- In aortitis evaluation, inflammatory markers (ESR/CRP) are commonly used, but may be insensitive/nonspecific for vascular inflammation; infectious workup includes cultures and broad serologies. (ahlman2023advancedmolecularimaging pages 1-2, arcilla2025thegreatvasculitis pages 7-9)
- Infectious/inflammatory mimics: leucocytosis, thrombocytosis, normocytic anemia, hypoalbuminemia, polyclonal hypergammaglobulinemia. (arcilla2025thegreatvasculitis pages 7-9)

### 10.2 Imaging: current standards and performance
**EULAR 2023 evidence base (systematic review/meta-analysis) for GCA imaging**:
- Ultrasound, MRI, and FDG-PET have “good performance” for GCA diagnosis; in low risk-of-bias studies, ultrasound sensitivity/specificity **88% / 96%** and pooled LR+ **20.07**, LR− **0.13**. (bosch2023imagingindiagnosis pages 3-4)
- Ultrasound assessing both cranial and extracranial arteries improves sensitivity (**93% vs 80%**) with similar specificity. (bosch2023imagingindiagnosis pages 1-2)
- FDG-PET pooled sensitivity/specificity reported as **76% / 95%** (context: GCA imaging studies in the SLR). (bosch2023imagingindiagnosis pages 1-2)

**Practical CTA/MRI/PET criteria from narrative imaging review (2024):**
- Active inflammation suggested by wall thickening **>2 mm (aorta)** and **>1 mm (branch vessels)** on CTA/MRI. (popescu2024imaginginlarge pages 7-9)
- Arterial wall enhancement defined as **>20 HU** increase compared to unenhanced CT. (popescu2024imaginginlarge pages 7-9)
- PET positivity criterion: **segmental FDG uptake ≥ liver**. (popescu2024imaginginlarge pages 7-9)

**FDG-PET/CT in clinical practice (2023 review):**
- For cranial artery involvement (when performed before/≤72h after glucocorticoids), sensitivity **82–92%** and specificity **85–100%** reported. (nassarmadji202318fluorodeoxyglucosepositronemission pages 1-2)

### 10.3 Histopathology
- Surgical series highlight the importance of intra-operative sampling: aortitis diagnosis often relies on histology, and CIA may be missed without routine sampling. (staniforth2024aortitisincreasesthe pages 1-2)
- Infectious aortitis may show neutrophilic infiltration but biopsy may be risky in fragile walls. (arcilla2025thegreatvasculitis pages 7-9)

### 10.4 Differential diagnosis
A key diagnostic principle is to **exclude infection and malignancy** before immunosuppression; infectious aortitis can induce autoantibodies (ANCA/MPO/PR3), mimicking primary vasculitis. (arcilla2025thegreatvasculitis pages 6-7, arcilla2025thegreatvasculitis pages 7-9)

---

## 11. Outcome / Prognosis

- **Surgical cohort outcomes:** aortitis increased re-operation risk; re-operation rate was roughly doubled (17.5% vs 9.4%). (staniforth2024aortitisincreasesthe pages 1-2)
- **Long-term complications:** vascular stenosis, stroke risk, and new aneurysm formation are emphasized, with cited studies reporting 58% 5-year vascular complication rates in a French series and new aneurysm development in CIA cohorts (as cited in the surgical paper). (staniforth2024aortitisincreasesthe pages 8-9)
- **Infectious aortitis:** high mortality noted for thoracic infectious aortitis (reported up to 30–50% in a case-based review). (arcilla2025thegreatvasculitis pages 1-3)

---

## 12. Treatment

### 12.1 Noninfectious/CIA and LVV-associated aortitis
- **Center practice regimen (CIA/noninfectious):** prednisolone **0.75–1 mg/kg** plus methotrexate **20–25 mg/week**; refractory cases may use pulsed IV cyclophosphamide **15 mg/kg**; tocilizumab **162 mg SC weekly** used for relapsing/refractory disease after failure of two conventional strategies. (staniforth2024aortitisincreasesthe pages 8-9)

- **Tocilizumab real-world effectiveness (extracranial GCA/LV-GCA and TAK; 2025 observational):** at 12 months, remission **74.5% (LV-GCA)** and **76.9% (TAK)**; imaging-complete resolution only **18.9%** and **21.1%**, respectively; severe infections led to discontinuation in 4 LV-GCA and 3 TAK patients. (lasateja2025tocilizumabinextracranial pages 1-2)

- **GC + TCZ RCT benchmark (GiACTA; summarized in 2024 trial protocol):** sustained remission at 52 weeks **56%/53%** (weekly/q2w TCZ) vs **14%/18%** (GC alone). (kreis2024themeteoriticstrial pages 1-2)

### 12.2 Infectious aortitis
- Early empiric broad-spectrum antibiotics covering Gram-positive cocci and Gram-negative rods; ampicillin/cephalosporins suggested empirically for Salmonella; prolonged therapy often required (≥6–8 weeks), especially with endovascular repair; surgery/endovascular (TEVAR/EVAR) indicated for rapid expansion/large aneurysm but with infection-related complication risk. (arcilla2025thegreatvasculitis pages 7-9)

### 12.3 MAXO term suggestions (examples)
- Glucocorticoid therapy; methotrexate therapy; cyclophosphamide therapy; IL-6 receptor antagonist therapy (tocilizumab); antimicrobial therapy; endovascular aortic repair; open surgical aortic repair; imaging surveillance. (staniforth2024aortitisincreasesthe pages 8-9, arcilla2025thegreatvasculitis pages 7-9, lasateja2025tocilizumabinextracranial pages 1-2)

---

## 13. Prevention

Evidence retrieved is limited. Practical prevention/mitigation approaches include:
- **Secondary prevention of complications** via long-term surveillance imaging (annual CT aortogram ≥5 years in one center protocol) and cardiovascular risk modification measures (statins, beta-blockers, ACE inhibitors, antithrombotics) used in clinical practice. (staniforth2024aortitisincreasesthe pages 8-9)
- For biologic therapy: **TB screening** (PPD/QuantiFERON, chest X-ray) and isoniazid prophylaxis for latent infection before biologics in one multicenter observational practice description. (lasateja2025tocilizumabinextracranial pages 2-4)

---

## 14. Other Species / Natural Disease

No retrieved evidence in this run addressed naturally occurring aortitis across non-human species or zoonotic considerations.

---

## 15. Model Organisms

No direct “aortitis model organism” papers were retrieved in this run. Mechanistic TAK genetics work used immune cell systems and vascular cells (e.g., PBMC-derived macrophages; human aortic smooth muscle cells) supporting in vitro mechanistic modeling. (tamura2018singlenucleotidepolymorphismof pages 6-7)

---

## Recent developments (priority 2023–2024)

1. **Imaging evidence synthesis informing EULAR 2023 update:** pooled diagnostic performance metrics for ultrasound/MRI/FDG-PET in GCA and evidence supporting inclusion of extracranial (axillary) ultrasound to increase sensitivity. (Aug 2023; https://doi.org/10.1136/rmdopen-2023-003379) (bosch2023imagingindiagnosis pages 1-2, bosch2023imagingindiagnosis pages 3-4)
2. **High-sampling surgical cohort redefining CIA prevalence and postoperative risk:** histology-sampled prevalence 10.6% with 75% CIA; higher re-operation risk and identified risk associations (age, female sex, smoking, inflammatory disease). (Dec 2024; https://doi.org/10.3390/jcdd11120405) (staniforth2024aortitisincreasesthe pages 1-2, staniforth2024aortitisincreasesthe pages 6-8, staniforth2024aortitisincreasesthe media bd38afdc)
3. **Drug-induced aortitis (G-CSF) systematic case synthesis:** 72-case dataset describing demographics, lesion distribution, complication rate (~4.2%), and recurrence on rechallenge, emphasizing diagnostic vigilance. (Dec 2024; https://doi.org/10.3389/fphar.2024.1487501) (zhao2024literaturereviewanalysis pages 1-2, zhao2024literaturereviewanalysis pages 5-7)

---

## Key quantitative summary table (etiology/risk statistics)

| Category | Typical patient profile | Key statistics | Diagnostic clues (labs/imaging) | Notes/quotes | Key citations |
|---|---|---|---|---|---|
| Noninfectious: overall surgically identified aortitis / clinically isolated aortitis (CIA) | Often older adults; more common in women; associated with smoking and prior inflammatory disease; many cases asymptomatic until aneurysm/dissection surgery | In a major aortic surgery cohort, histology-confirmed aortitis prevalence was **10.6% (57/537)**; **75%** of aortitis cases were CIA; CIA prevalence **8.0% (43/537)**; re-operation **17.5% vs 9.4%** in non-aortitis; multivariable associations: age OR **1.03**, female sex OR **4.10**, current smoking OR **3.43**, prior inflammatory disease OR **9.01**; bicuspid aortic valve associated with lower odds OR **0.34** | Elevated inflammatory markers; PET-CT to map inflammation; intra-operative histology is essential; annual CT aortogram suggested in follow-up | “**Aortitis, defined as inflammation of the aorta**”; “**75% were clinically isolated**” | (staniforth2024aortitisincreasesthe pages 1-2, staniforth2024aortitisincreasesthe pages 6-8, staniforth2024aortitisincreasesthe media bd38afdc) |
| Noninfectious: giant cell arteritis (GCA)-associated aortitis | Usually adults >50 years; Northern European populations higher incidence; can coexist with PMR; risk factors for aneurysmal complications include male sex, smoking, hypertension, hyperlipidemia/coronary disease | GCA incidence about **44/100,000 persons >50** in Northern Europe; aorta or major branch involvement in about **27%** of GCA; in large-vessel GCA, aortic involvement **45–65%**; thoracic aortic aneurysm/dissection incidence reported **8.2–33%**; meta-analysis suggests ~**3-fold** increased TAA risk; one cohort found **3.1%** TAA among 2,344 GCA patients; >**20% (12/54)** developed aortic aneurysm after 4–10 years in one CT study | CTA/MRA/PET-CT/US; CTA/MRI wall-thickness thresholds suggesting active disease: **>2 mm aorta**, **>1 mm branch vessels**; PET uptake may identify higher-risk patients for future aneurysm | “**a granulomatous vasculitis**”; “**Imaging is essential**”; “**The literature review disclosed an increased incidence and relative risk of TAA among patients with GCA**” | (popescu2024imaginginlarge pages 4-5, strachan2025thoracicaorticaneurysm pages 2-4, popescu2024imaginginlarge pages 7-9, popescu2024imaginginlarge pages 1-2) |
| Noninfectious: Takayasu arteritis (TAK)-associated aortitis | Typically younger individuals; often women; systemic large-vessel vasculitis affecting aorta and branches | Annual incidence **0.4–3.4 per 1,000,000**; TAK is “the primary cause of aortitis in younger individuals”; aorta/major branches involved in about **65%**; coronary arteries **44%**; pulmonary arteries **63%**; stenotic lesions in **>90%**; aneurysms in about **25%**; hypertension **30–90%**; stroke/TIA **10–20%** | MRI first-line in suspected TAK; CTA shows circumferential wall thickening in active disease, later stenosis/occlusion; PET-CT can complement luminal imaging by showing active inflammation | “**characterized by variable degrees of inflammation... of all arterial layers (panarteritis)**” | (popescu2024imaginginlarge pages 4-5, popescu2024imaginginlarge pages 7-9, popescu2024imaginginlarge pages 1-2) |
| Noninfectious: Behçet disease-associated aortitis/large-vessel vasculitis | Often younger to middle-aged adults; autoinflammatory/systemic vasculitis phenotype; HLA-B51 association noted in review | Up to **40%** may experience large vascular complications; mortality around **4%** | CTA/MRA/PET-CT/US depending territory; evaluate aneurysm, thrombosis, arterial wall inflammation | “**mainly considered an auto-inflammatory systemic vasculitis**” | (popescu2024imaginginlarge pages 4-5) |
| Noninfectious: drug-induced aortitis (G-CSF-associated) | Predominantly older women receiving chemotherapy; especially breast cancer; also reported in healthy stem-cell donors; majority reported from Asian populations | Review of **72** patients: **58 female/14 male (80.6% female)**, mean age **61.83 ± 10.30** years; pegfilgrastim implicated most often (**63.4%**); lesion distribution: aortic arch **36.11%**, abdominal aorta **26.39%**, thoracic aorta **22.22%**; **4/72** asymptomatic; complications in **3/72 (~4.2%)** including dissection/aneurysm; recurrence after rechallenge reported | Typically fever/pain with elevated CRP and negative blood cultures; CT most often identifies aortic arch/branch involvement | “**Most patients had a good prognosis, but 3 cases developed complications**”; “**G-CSF-induced aortitis was also found in 4 asymptomatic patients**” | (zhao2024literaturereviewanalysis pages 1-2, zhao2024literaturereviewanalysis pages 5-7, zhao2024literaturereviewanalysis pages 7-8, zhao2024literaturereviewanalysis pages 2-3) |
| Infectious aortitis: overall bacterial/fungal/mycobacterial/spirochetal | Often patients with atherosclerosis, damaged vessel wall, immunosuppression, infection, trauma, congenital abnormalities, or malignancy; may present with aneurysm, pseudoaneurysm, or sepsis-like syndrome | Thoracic aortitis mortality reported **30–50%**; blood cultures positive in only **50–82%**; mycotic aneurysms account for **0.6–2%** of all aortic aneurysms in Western populations; infectious aortitis more often abdominal (**56%** in cited series) | Labs: leukocytosis, thrombocytosis, normocytic anemia, elevated inflammatory markers/CRP (often >100 mg/L in cited review); imaging: CTA/MRA/PET-CT/US; infected aneurysm clues include saccular morphology, peri-aortic edema/fat stranding, wall thickening, loss of contour, gas in wall | “**Differentiating between infectious and inflammatory cases is crucial**”; “**blood cultures (positive in only 50% to 82%) are recommended**” | (arcilla2025thegreatvasculitis pages 7-9, arcilla2025thegreatvasculitis pages 1-3, arcilla2025thegreatvasculitis pages 6-7) |
| Infectious aortitis: common pathogens / microbiology | Bacterial predominance; consider bacteremia/endovascular seeding via vasa vasorum or damaged wall | Gram-positive organisms about **44%** in one review; Gram-negative rods **33%**; intracellular/fastidious organisms **43%**; Cox review notes Gram-positive bacteria account for about **60%** of thoracic infections; common pathogens include **Staphylococcus aureus, Streptococcus spp., Enterococcus, Salmonella, Haemophilus influenzae, Mycobacterium tuberculosis, Treponema pallidum**, fungi | Obtain repeated blood cultures, tissue culture/PCR/serologies; histology often shows neutrophilic infiltration; CTA/PET-CT used to define extent and plan intervention | “**Gram positive bacteria such as Staphylococcus, Enterococcus and Streptococcus accounting for approximately 60% of the infections**” | (arcilla2025thegreatvasculitis pages 7-9, arcilla2025thegreatvasculitis pages 6-7) |
| Infectious aortitis: management-relevant clues | Patients may initially mimic primary vasculitis; wrong early immunosuppression can be harmful | No large comparative trials; prolonged antibiotics typically **at least 6–8 weeks** with TEVAR/EVAR/open repair depending anatomy and infection control | Broad-spectrum bactericidal therapy first; defer steroids/biologics until infection excluded; CTA gives high-resolution 3D anatomy, PET may help distinguish infection/inflammation and occult extent | “**Steroids and biological therapy were held until comprehensive investigations were completed**”; “**optimal approach must be decided on a case-by-case basis**” | (arcilla2025thegreatvasculitis pages 7-9, arcilla2025thegreatvasculitis pages 6-7) |


*Table: This table summarizes major noninfectious and infectious aortitis categories, highlighting patient profiles, quantitative epidemiology, diagnostic clues, and brief source-supported notes from the current evidence set. It is designed as a compact reference for comparing causes of aortitis and the numbers most relevant to diagnosis and risk stratification.*

---

## Real-world implementations / workflows

- **Surgical pathology workflow:** routine intra-operative aortic sampling can uncover aortitis/CIA otherwise missed, changing follow-up intensity and rheumatology referral patterns. (staniforth2024aortitisincreasesthe pages 1-2)
- **Clinical imaging workflow:** many centers increasingly integrate FDG-PET with CTA/MRA/US for LVV/aortitis assessment; reimbursement changes (CMS 2021) and guideline incorporation have accelerated PET use in some health systems. (ahlman2023advancedmolecularimaging pages 1-2)
- **Long-term monitoring:** annual CT aortogram surveillance for at least 5 years after diagnosis is used in at least one specialized center pathway for CIA/noninfectious aortitis. (staniforth2024aortitisincreasesthe pages 8-9)

---

## Items requested but not fully retrievable in this run

- **MONDO/Orphanet/ICD-10/ICD-11/MeSH identifiers:** not present in retrieved full texts. (staniforth2024aortitisincreasesthe pages 9-11, staniforth2024aortitisincreasesthe pages 2-4)
- **PMIDs preferred:** Several retrieved items are identified by DOI within text extracts but PMIDs were not consistently present in the extracted evidence snippets; therefore, DOI-based URLs are provided where available.
- **Model organism literature and cross-species natural disease:** not retrieved.



References

1. (staniforth2024aortitisincreasesthe pages 9-11): Edward Staniforth, Shirish Dubey, Iakovos Ttofi, Vanitha Perinparajah, Jasmina Ttofi, Rohit Vijjhalwar, Raman Uberoi, Ediri Sideso, and George Krasopoulos. Aortitis increases the risk of surgical complications and re-operations after major aortic surgery. Journal of Cardiovascular Development and Disease, 11:405, Dec 2024. URL: https://doi.org/10.3390/jcdd11120405, doi:10.3390/jcdd11120405. This article has 1 citations.

2. (staniforth2024aortitisincreasesthe pages 2-4): Edward Staniforth, Shirish Dubey, Iakovos Ttofi, Vanitha Perinparajah, Jasmina Ttofi, Rohit Vijjhalwar, Raman Uberoi, Ediri Sideso, and George Krasopoulos. Aortitis increases the risk of surgical complications and re-operations after major aortic surgery. Journal of Cardiovascular Development and Disease, 11:405, Dec 2024. URL: https://doi.org/10.3390/jcdd11120405, doi:10.3390/jcdd11120405. This article has 1 citations.

3. (staniforth2024aortitisincreasesthe pages 1-2): Edward Staniforth, Shirish Dubey, Iakovos Ttofi, Vanitha Perinparajah, Jasmina Ttofi, Rohit Vijjhalwar, Raman Uberoi, Ediri Sideso, and George Krasopoulos. Aortitis increases the risk of surgical complications and re-operations after major aortic surgery. Journal of Cardiovascular Development and Disease, 11:405, Dec 2024. URL: https://doi.org/10.3390/jcdd11120405, doi:10.3390/jcdd11120405. This article has 1 citations.

4. (arcilla2025thegreatvasculitis pages 7-9): Cristine Kuzhuppilly Arcilla, Tomas Marek, and Gurjit Kaeley. The great vasculitis pretenders: mycotic pseudoaneurysm, aortitis with occlusive iliac thrombus, and paraneoplastic aortitis. a case-based review. Mediterranean Journal of Rheumatology, 36:488, Sep 2025. URL: https://doi.org/10.31138/mjr.220125.era, doi:10.31138/mjr.220125.era. This article has 0 citations.

5. (bosch2023imagingindiagnosis pages 1-2): Philipp Bosch, Milena Bond, Christian Dejaco, Cristina Ponte, Sarah Louise Mackie, Louise Falzon, Wolfgang A Schmidt, and Sofia Ramiro. Imaging in diagnosis, monitoring and outcome prediction of large vessel vasculitis: a systematic literature review and meta-analysis informing the 2023 update of the eular recommendations. RMD Open, 9:e003379, Aug 2023. URL: https://doi.org/10.1136/rmdopen-2023-003379, doi:10.1136/rmdopen-2023-003379. This article has 108 citations and is from a peer-reviewed journal.

6. (popescu2024imaginginlarge pages 4-5): Ioana Popescu, Roxana Pintican, Luminita Cocarla, Benjamin Burger, Irina Sandu, George Popa, Alexandra Dadarlat, Raluca Rancea, Alexandru Oprea, Alexandru Goicea, Laura Damian, Alexandru Manea, Ruben Mateas, and Simona Manole. Imaging in large vessel vasculitis—a narrative review. Journal of Clinical Medicine, 13:6364, Oct 2024. URL: https://doi.org/10.3390/jcm13216364, doi:10.3390/jcm13216364. This article has 6 citations.

7. (wang2025unravelingthecomplexity pages 6-7): Yan Wang, Feng Tian, and Hui Li. Unraveling the complexity of igg4-related aortitis and periarteritis: from pathogenesis to clinical practice. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1625456, doi:10.3389/fimmu.2025.1625456. This article has 0 citations and is from a peer-reviewed journal.

8. (arcilla2025thegreatvasculitis pages 6-7): Cristine Kuzhuppilly Arcilla, Tomas Marek, and Gurjit Kaeley. The great vasculitis pretenders: mycotic pseudoaneurysm, aortitis with occlusive iliac thrombus, and paraneoplastic aortitis. a case-based review. Mediterranean Journal of Rheumatology, 36:488, Sep 2025. URL: https://doi.org/10.31138/mjr.220125.era, doi:10.31138/mjr.220125.era. This article has 0 citations.

9. (zhao2024literaturereviewanalysis pages 1-2): Ting Zhao and Huanhuan Xu. Literature review analysis of aortitis induced by granulocyte-colony stimulating factor. Frontiers in Pharmacology, Dec 2024. URL: https://doi.org/10.3389/fphar.2024.1487501, doi:10.3389/fphar.2024.1487501. This article has 11 citations.

10. (zhao2024literaturereviewanalysis pages 5-7): Ting Zhao and Huanhuan Xu. Literature review analysis of aortitis induced by granulocyte-colony stimulating factor. Frontiers in Pharmacology, Dec 2024. URL: https://doi.org/10.3389/fphar.2024.1487501, doi:10.3389/fphar.2024.1487501. This article has 11 citations.

11. (staniforth2024aortitisincreasesthe pages 6-8): Edward Staniforth, Shirish Dubey, Iakovos Ttofi, Vanitha Perinparajah, Jasmina Ttofi, Rohit Vijjhalwar, Raman Uberoi, Ediri Sideso, and George Krasopoulos. Aortitis increases the risk of surgical complications and re-operations after major aortic surgery. Journal of Cardiovascular Development and Disease, 11:405, Dec 2024. URL: https://doi.org/10.3390/jcdd11120405, doi:10.3390/jcdd11120405. This article has 1 citations.

12. (arcilla2025thegreatvasculitis pages 1-3): Cristine Kuzhuppilly Arcilla, Tomas Marek, and Gurjit Kaeley. The great vasculitis pretenders: mycotic pseudoaneurysm, aortitis with occlusive iliac thrombus, and paraneoplastic aortitis. a case-based review. Mediterranean Journal of Rheumatology, 36:488, Sep 2025. URL: https://doi.org/10.31138/mjr.220125.era, doi:10.31138/mjr.220125.era. This article has 0 citations.

13. (zhao2024literaturereviewanalysis pages 2-3): Ting Zhao and Huanhuan Xu. Literature review analysis of aortitis induced by granulocyte-colony stimulating factor. Frontiers in Pharmacology, Dec 2024. URL: https://doi.org/10.3389/fphar.2024.1487501, doi:10.3389/fphar.2024.1487501. This article has 11 citations.

14. (tamura2018singlenucleotidepolymorphismof pages 6-7): Natsuko Tamura, Yasuhiro Maejima, Takayoshi Matsumura, Rick B. Vega, Eisuke Amiya, Yusuke Ito, Yuka Shiheido-Watanabe, Takashi Ashikaga, Issei Komuro, Daniel P. Kelly, Kenzo Hirao, and Mitsuaki Isobe. Single-nucleotide polymorphism of the mlx gene is associated with takayasu arteritis. Circulation: Genomic and Precision Medicine, 11:e002296, Oct 2018. URL: https://doi.org/10.1161/circgen.118.002296, doi:10.1161/circgen.118.002296. This article has 19 citations.

15. (chan2025strokeaorticregurgitation pages 2-4): Elizabeth Chan. Stroke, aortic regurgitation and aortic aneurysm in younger female: case of giant cell aortitis and discussion. Academic Medicine &amp; Surgery, Nov 2025. URL: https://doi.org/10.62186/001c.146456, doi:10.62186/001c.146456. This article has 0 citations.

16. (staniforth2024aortitisincreasesthe pages 8-9): Edward Staniforth, Shirish Dubey, Iakovos Ttofi, Vanitha Perinparajah, Jasmina Ttofi, Rohit Vijjhalwar, Raman Uberoi, Ediri Sideso, and George Krasopoulos. Aortitis increases the risk of surgical complications and re-operations after major aortic surgery. Journal of Cardiovascular Development and Disease, 11:405, Dec 2024. URL: https://doi.org/10.3390/jcdd11120405, doi:10.3390/jcdd11120405. This article has 1 citations.

17. (staniforth2024aortitisincreasesthe pages 4-6): Edward Staniforth, Shirish Dubey, Iakovos Ttofi, Vanitha Perinparajah, Jasmina Ttofi, Rohit Vijjhalwar, Raman Uberoi, Ediri Sideso, and George Krasopoulos. Aortitis increases the risk of surgical complications and re-operations after major aortic surgery. Journal of Cardiovascular Development and Disease, 11:405, Dec 2024. URL: https://doi.org/10.3390/jcdd11120405, doi:10.3390/jcdd11120405. This article has 1 citations.

18. (popescu2024imaginginlarge pages 7-9): Ioana Popescu, Roxana Pintican, Luminita Cocarla, Benjamin Burger, Irina Sandu, George Popa, Alexandra Dadarlat, Raluca Rancea, Alexandru Oprea, Alexandru Goicea, Laura Damian, Alexandru Manea, Ruben Mateas, and Simona Manole. Imaging in large vessel vasculitis—a narrative review. Journal of Clinical Medicine, 13:6364, Oct 2024. URL: https://doi.org/10.3390/jcm13216364, doi:10.3390/jcm13216364. This article has 6 citations.

19. (popescu2024imaginginlarge pages 5-7): Ioana Popescu, Roxana Pintican, Luminita Cocarla, Benjamin Burger, Irina Sandu, George Popa, Alexandra Dadarlat, Raluca Rancea, Alexandru Oprea, Alexandru Goicea, Laura Damian, Alexandru Manea, Ruben Mateas, and Simona Manole. Imaging in large vessel vasculitis—a narrative review. Journal of Clinical Medicine, 13:6364, Oct 2024. URL: https://doi.org/10.3390/jcm13216364, doi:10.3390/jcm13216364. This article has 6 citations.

20. (tamura2018singlenucleotidepolymorphismof pages 2-3): Natsuko Tamura, Yasuhiro Maejima, Takayoshi Matsumura, Rick B. Vega, Eisuke Amiya, Yusuke Ito, Yuka Shiheido-Watanabe, Takashi Ashikaga, Issei Komuro, Daniel P. Kelly, Kenzo Hirao, and Mitsuaki Isobe. Single-nucleotide polymorphism of the mlx gene is associated with takayasu arteritis. Circulation: Genomic and Precision Medicine, 11:e002296, Oct 2018. URL: https://doi.org/10.1161/circgen.118.002296, doi:10.1161/circgen.118.002296. This article has 19 citations.

21. (muratore2026treatmentstrategiesin pages 29-33): F Muratore, KJ Warrington, and C Dejaco. Treatment strategies in giant cell arteritis and polymyalgia rheumatica: beyond glucocorticoids. Unknown journal, 2026.

22. (popescu2024imaginginlarge pages 1-2): Ioana Popescu, Roxana Pintican, Luminita Cocarla, Benjamin Burger, Irina Sandu, George Popa, Alexandra Dadarlat, Raluca Rancea, Alexandru Oprea, Alexandru Goicea, Laura Damian, Alexandru Manea, Ruben Mateas, and Simona Manole. Imaging in large vessel vasculitis—a narrative review. Journal of Clinical Medicine, 13:6364, Oct 2024. URL: https://doi.org/10.3390/jcm13216364, doi:10.3390/jcm13216364. This article has 6 citations.

23. (nassarmadji202318fluorodeoxyglucosepositronemission pages 1-2): Kladoum Nassarmadji, Anthony Vanjak, Venceslas Bourdin, Karine Champion, Ruxandra Burlacu, Stéphane Mouly, Damien Sène, and Cloé Comarmond. 18-fluorodeoxyglucose positron emission tomography/computed tomography for large vessel vasculitis in clinical practice. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2023.1103752, doi:10.3389/fmed.2023.1103752. This article has 7 citations.

24. (ahlman2023advancedmolecularimaging pages 1-2): Mark A. Ahlman and Peter C. Grayson. Advanced molecular imaging in large-vessel vasculitis: adopting fdg-pet into a clinical workflow. Best practice & research. Clinical rheumatology, 37:101856, Jul 2023. URL: https://doi.org/10.1016/j.berh.2023.101856, doi:10.1016/j.berh.2023.101856. This article has 11 citations.

25. (bosch2023imagingindiagnosis pages 3-4): Philipp Bosch, Milena Bond, Christian Dejaco, Cristina Ponte, Sarah Louise Mackie, Louise Falzon, Wolfgang A Schmidt, and Sofia Ramiro. Imaging in diagnosis, monitoring and outcome prediction of large vessel vasculitis: a systematic literature review and meta-analysis informing the 2023 update of the eular recommendations. RMD Open, 9:e003379, Aug 2023. URL: https://doi.org/10.1136/rmdopen-2023-003379, doi:10.1136/rmdopen-2023-003379. This article has 108 citations and is from a peer-reviewed journal.

26. (lasateja2025tocilizumabinextracranial pages 1-2): Carmen Lasa-Teja, Javier Loricera, Diana Prieto-Peña, Fernando López-Gutiérrez, Pilar Bernabéu, María Mercedes Freire-González, Beatriz González-Alvarez, Roser Solans-Laqué, Mauricio Mínguez, Iván Ferraz-Amaro, Santos Castañeda, and Ricardo Blanco. Tocilizumab in extracranial giant-cell arteritis and takayasu arteritis: a multicentric observational comparative study. Sci, 7:12, Jan 2025. URL: https://doi.org/10.3390/sci7010012, doi:10.3390/sci7010012. This article has 0 citations.

27. (kreis2024themeteoriticstrial pages 1-2): Lena Kreis, Christian Dejaco, Wolfgang Andreas Schmidt, Robert Németh, Nils Venhoff, and Valentin Sebastian Schäfer. The meteoritics trial: efficacy of methotrexate after remission-induction with tocilizumab and glucocorticoids in giant cell arteritis—study protocol for a randomized, double-blind, placebo-controlled, parallel-group phase ii study. Trials, Jan 2024. URL: https://doi.org/10.1186/s13063-024-07905-4, doi:10.1186/s13063-024-07905-4. This article has 14 citations and is from a peer-reviewed journal.

28. (lasateja2025tocilizumabinextracranial pages 2-4): Carmen Lasa-Teja, Javier Loricera, Diana Prieto-Peña, Fernando López-Gutiérrez, Pilar Bernabéu, María Mercedes Freire-González, Beatriz González-Alvarez, Roser Solans-Laqué, Mauricio Mínguez, Iván Ferraz-Amaro, Santos Castañeda, and Ricardo Blanco. Tocilizumab in extracranial giant-cell arteritis and takayasu arteritis: a multicentric observational comparative study. Sci, 7:12, Jan 2025. URL: https://doi.org/10.3390/sci7010012, doi:10.3390/sci7010012. This article has 0 citations.

29. (staniforth2024aortitisincreasesthe media bd38afdc): Edward Staniforth, Shirish Dubey, Iakovos Ttofi, Vanitha Perinparajah, Jasmina Ttofi, Rohit Vijjhalwar, Raman Uberoi, Ediri Sideso, and George Krasopoulos. Aortitis increases the risk of surgical complications and re-operations after major aortic surgery. Journal of Cardiovascular Development and Disease, 11:405, Dec 2024. URL: https://doi.org/10.3390/jcdd11120405, doi:10.3390/jcdd11120405. This article has 1 citations.

30. (strachan2025thoracicaorticaneurysm pages 2-4): Sebastien Strachan, Mohammad A. Zafar, Sudhir Perincheri, Awab Ahmad, Nafiye Busra Celik, Mah I. Kan Changez, Bulat A. Ziganshin, and John A. Elefteriades. Thoracic aortic aneurysm and giant cell arteritis: clarifying the link. AORTA, 13:072-078, Jun 2025. URL: https://doi.org/10.1055/a-2765-8610, doi:10.1055/a-2765-8610. This article has 1 citations and is from a peer-reviewed journal.

31. (zhao2024literaturereviewanalysis pages 7-8): Ting Zhao and Huanhuan Xu. Literature review analysis of aortitis induced by granulocyte-colony stimulating factor. Frontiers in Pharmacology, Dec 2024. URL: https://doi.org/10.3389/fphar.2024.1487501, doi:10.3389/fphar.2024.1487501. This article has 11 citations.