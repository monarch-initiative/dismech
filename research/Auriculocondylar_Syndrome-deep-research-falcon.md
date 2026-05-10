---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T11:08:07.743996'
end_time: '2026-05-10T11:28:33.205786'
duration_seconds: 1225.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Auriculocondylar Syndrome
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
- **Disease Name:** Auriculocondylar Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Auriculocondylar Syndrome** covering all of the
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
- **Disease Name:** Auriculocondylar Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Auriculocondylar Syndrome** covering all of the
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


## Auriculocondylar Syndrome (ARCND/ACS): Comprehensive Disease Characteristics Report

### Executive summary
Auriculocondylar syndrome (ARCND; historically “auriculocondylar syndrome/ACS”) is an ultra-rare congenital craniofacial malformation of first and second pharyngeal arch derivatives, classically presenting with **micrognathia**, **mandibular condyle hypoplasia**, and a characteristic external ear anomaly termed the **question-mark ear (QME)**. Current genetic understanding centers on disruption of **EDN1–EDNRA signaling** and downstream cranial neural crest patterning (DLX5/6), with additional genetic heterogeneity including a regulatory duplication affecting **TWIST1** expression. Recent (2024) reports emphasize multidisciplinary, technology-assisted craniofacial care (3D planning, distraction osteogenesis, orthognathic surgery) with measurable functional improvement. (clouthier2013understandingthebasis pages 1-3, rieder2012ahumanhomeotic pages 1-2, shi2024novelgnai3mutation pages 2-6)

---

## 1. Disease information

### 1.1 Definition and current understanding
ARCND/ACS is a rare congenital craniofacial disorder affecting development of the **outer ear and mandible**, and is best recognized as a disorder of **pharyngeal arch (branchial arch) development** with a characteristic “homeotic” patterning disturbance of the jaw in severe cases. The core/typical triad is consistently described as **micrognathia**, **mandibular condyle hypoplasia**, and a **QME** defect at the helix–lobule junction. (clouthier2013understandingthebasis pages 1-3, gordon2013heterogeneityofmutational pages 1-2)

Primary literature definition examples:
- Rieder et al. (2012) describe ACS as “a rare, autosomal-dominant craniofacial malformation syndrome” with micrognathia and a distinctive QME, and report additional features including TMJ ankylosis and cleft palate. (https://doi.org/10.1016/j.ajhg.2012.04.002; May 2012) (rieder2012ahumanhomeotic pages 1-2)
- Clouthier et al. (2013) define the “core triad” as “micrognathia, mandibular condyle hypoplasia, and a unique ear malformation” (QME/Cosman ear). (https://doi.org/10.1002/ajmg.c.31376; Nov 2013) (clouthier2013understandingthebasis pages 1-3)

### 1.2 Key identifiers (available in retrieved evidence)
A subset of identifiers could be extracted directly from retrieved sources (others were not present in the evidence captured in this run).

| Disease / concept | Synonyms / related names in evidence | Identifiers in evidence | Prevalence / epidemiology note in evidence | Source year | URL | Citation |
|---|---|---|---|---|---|---|
| Auriculocondylar syndrome | Auriculocondylar syndrome; ACS; ARCND | MONDO: MONDO_0000107 | Open Targets lists MONDO_0000107 for “auriculocondylar syndrome” | n/a | n/a | (OpenTargets Search: Auriculocondylar syndrome) |
| Auriculocondylar syndrome | “question mark ear syndrome”; “dysgnathia complex” | OMIM #602483, #614669, #615706 | Rare / prevalence not given in this excerpt | 2013 | https://doi.org/10.1002/ajmg.c.31376 | (clouthier2013understandingthebasis pages 1-3) |
| Auriculocondylar syndrome (general ARCND) | ARCND; “question mark ear syndrome” | OMIM #602483, #614669, #615706 | Orphanet prevalence stated as under 1 in 1,000,000 | 2022 | https://doi.org/10.1136/jmedgenet-2021-107825 | (tavares2022newlocusunderlying pages 1-2) |
| Auriculocondylar syndrome (general ARCND) | ARCND | OMIM #602483, #614669, #615706 | Prevalence stated as less than 1 in 1,000,000; fewer than 100 cases reported | 2024 | https://doi.org/10.1186/s12903-024-04575-1 | (shi2024novelgnai3mutation pages 1-2) |
| Auriculocondylar syndrome | ARCND; dysgnathia complex; question mark ear syndrome | ARCND1 OMIM #602483; ARCND2A OMIM #614669; ARCND2B OMIM #620458; ARCND3 OMIM #615706; ARCND4 OMIM #620457 | Orphanet prevalence stated as under 1/1,000,000 | 2024 | https://doi.org/10.1002/mgg3.2441 | (zhang2024auriculocondylarsyndrome2 pages 1-2) |
| Auriculocondylar syndrome 1 | ARCND1 | OMIM #602483 | Subtype listed in review-style case report evidence | 2024 | https://doi.org/10.1002/mgg3.2441 | (zhang2024auriculocondylarsyndrome2 pages 1-2) |
| Auriculocondylar syndrome 2A | ARCND2A | OMIM #614669 | Subtype listed in review-style case report evidence | 2024 | https://doi.org/10.1002/mgg3.2441 | (zhang2024auriculocondylarsyndrome2 pages 1-2) |
| Auriculocondylar syndrome 2B | ARCND2B | OMIM #620458; MONDO_0957544 | Subtype listed; Open Targets includes MONDO_0957544 | 2024 / n/a | https://doi.org/10.1002/mgg3.2441 | (zhang2024auriculocondylarsyndrome2 pages 1-2, OpenTargets Search: Auriculocondylar syndrome) |
| Auriculocondylar syndrome 3 | ARCND3 | OMIM #615706 | Subtype listed in review-style case report evidence | 2024 | https://doi.org/10.1002/mgg3.2441 | (zhang2024auriculocondylarsyndrome2 pages 1-2) |
| Auriculocondylar syndrome 4 | ARCND4 | OMIM #620457; MONDO_0957543 | Subtype listed; Open Targets includes MONDO_0957543 for auriculocondylar syndrome 4 | 2024 / n/a | https://doi.org/10.1002/mgg3.2441 | (zhang2024auriculocondylarsyndrome2 pages 1-2, OpenTargets Search: Auriculocondylar syndrome) |
| Isolated question-mark ear | Isolated QME; isolated question-mark ears; IQME | OMIM #612798 | May occur as isolated anomaly distinct from syndromic ACS | 2013 | https://doi.org/10.1002/ajmg.c.31376 | (clouthier2013understandingthebasis pages 1-3) |


*Table: This table summarizes disease names, synonyms, and identifiers for auriculocondylar syndrome and related entities using only the evidence retrieved in the session. It highlights subtype OMIM numbers, available MONDO mappings, and prevalence statements useful for a knowledge-base entry.*

**MONDO:** OpenTargets maps “auriculocondylar syndrome” to **MONDO_0000107**, and includes MONDO entries for ARCND subtypes (e.g., auriculocondylar syndrome 4). (OpenTargets Search: Auriculocondylar syndrome)

**OMIM (disease):** OMIM IDs commonly cited include **602483**, **614669**, **615706**, and for ARCND subtype breakdown: **ARCND1 #602483; ARCND2A #614669; ARCND2B #620458; ARCND3 #615706; ARCND4 #620457**. (zhang2024auriculocondylarsyndrome2 pages 1-2, clouthier2013understandingthebasis pages 1-3, tavares2022newlocusunderlying pages 1-2)

**OMIM (related phenotype):** Isolated question-mark ear (IQME) OMIM **612798**. (clouthier2013understandingthebasis pages 1-3)

**Orphanet:** Multiple sources cite **Orphanet** as the prevalence source and provide the Orphanet homepage URL (http://www.orpha.net). (tavares2022newlocusunderlying pages 1-2, zhang2024auriculocondylarsyndrome2 pages 1-2)

**ICD-10/ICD-11 and MeSH:** Specific ICD-10/ICD-11 codes and MeSH headings were **not present** in the retrieved text evidence and therefore cannot be asserted here.

### 1.3 Synonyms and alternative names
Common synonyms in the retrieved literature include:
- **“question mark ear syndrome”** (clouthier2013understandingthebasis pages 1-3, tavares2022newlocusunderlying pages 1-2)
- **“dysgnathia complex”** (zhang2024auriculocondylarsyndrome2 pages 1-2, clouthier2013understandingthebasis pages 1-3)

### 1.4 Evidence sources (individual vs aggregated)
Evidence in this report derives from:
- **Aggregated disease-level resources and synthesis:** a Seminars review integrating human, mouse, and zebrafish genetics (Clouthier et al., 2013). (clouthier2013understandingthebasis pages 1-3)
- **Primary human genetics (families/case series):** e.g., Rieder et al. 2012 (exome + functional assays), Gordon et al. 2013 (EDN1), Tavares et al. 2017 (molecular cohort statistics), Tavares et al. 2022 (CNV + iPSC modeling). (rieder2012ahumanhomeotic pages 1-2, gordon2013mutationsinendothelin pages 1-2, tavares2017targetedmolecularinvestigation pages 4-6, tavares2022newlocusunderlying pages 5-6)
- **Recent individual clinical implementations (case reports):** 2024 ARCND management with orthodontics + distraction + orthognathic surgery and 5-year outcomes. (shi2024novelgnai3mutation pages 2-6)

---

## 2. Etiology

### 2.1 Disease causal factors (primary causes)
ARCND is primarily a **genetic (Mendelian) craniofacial developmental disorder**, caused by pathogenic variants that disrupt **endothelin signaling in cranial neural crest** and related patterning programs. (clouthier2013understandingthebasis pages 1-3, rieder2012ahumanhomeotic pages 1-2)

Major established causal genes/loci in retrieved evidence:
- **PLCB4** (ARCND2; most common cause in molecular cohorts) (tavares2017targetedmolecularinvestigation pages 4-6)
- **GNAI3** (ARCND1) (tavares2015novelvariantsin pages 1-2, shi2024novelgnai3mutation pages 2-6)
- **EDN1** (ARCND3; ligand-level defect) (gordon2013mutationsinendothelin pages 1-2)
- **430 kb tandem duplication at HDAC9/TWIST1 regulatory landscape** (ARCND4; regulatory mechanism) (tavares2022newlocusunderlying pages 5-6, tavares2022newlocusunderlying pages 4-4)

### 2.2 Risk factors

#### Genetic risk factors (causal variants)
Molecular cohort data: In a cohort of **28 molecularly investigated index patients**, **16/28 (57.1%)** carried **PLCB4** variants, **6/28 (21.4%)** carried **GNAI3** variants, **4/28 (14.3%)** carried **EDN1** variants, and **2/28 (7.1%)** were unsolved. (Tavares et al., 2017; https://doi.org/10.1002/ajmg.a.38101; Apr 2017) (tavares2017targetedmolecularinvestigation pages 4-6)

EDN1 can cause **recessive ACS** and **dominant isolated QME** depending on the mutation and residual EDN1 activity. (Gordon et al., 2013; https://doi.org/10.1016/j.ajhg.2013.10.023; Dec 2013) (gordon2013mutationsinendothelin pages 1-2)

Representative variants are summarized in the genetics table artifact below. 

| ARCND subtype (if known) | Gene/locus | Inheritance patterns reported | Variant examples (HGVS when available) | Proposed mechanism | Key functional evidence | Primary sources with year/URL |
|---|---|---|---|---|---|---|
| ARCND1 | **GNAI3** | AD; incomplete penetrance reported in some families | c.118G>C, p.Gly40Arg; p.Ser47Arg; p.Gly45Val; p.Thr48Asn; p.Asn269Tyr; c.140G>A, p.Ser47Asn; c.144_145insCATTGTGAAACAGATGAA, p.T48_I49insHCETDE (rieder2012ahumanhomeotic pages 3-5, tavares2016identificaçãodenovas pages 67-68, liu2021prenataldiagnosisof pages 1-3, shi2024novelgnai3mutation pages 2-6) | Predominantly **dominant-negative** disruption of GTP/GDP-binding region in the G1/G4 motifs, impairing downstream endothelin signaling (gordon2013heterogeneityofmutational pages 11-12, tavares2015novelvariantsin pages 1-2) | Structural modeling placed pathogenic residues in the nucleotide-binding pocket; p.Gly40Arg predicted to stabilize aberrant active conformation and inhibit MAPK/Rap signaling; patient-derived osteoblast assays in ACS showed reduced **DLX5/DLX6** expression consistent with EDN1-pathway disruption (rieder2012ahumanhomeotic pages 3-5, rieder2012ahumanhomeotic pages 1-2, tavares2015novelvariantsin pages 1-2) | Rieder et al., 2012, https://doi.org/10.1016/j.ajhg.2012.04.002; Tavares et al., 2015, https://doi.org/10.1038/ejhg.2014.132; Liu et al., 2021, https://doi.org/10.1186/s12884-021-04238-x; Shi et al., 2024, https://doi.org/10.1186/s12903-024-04575-1 (rieder2012ahumanhomeotic pages 3-5, tavares2015novelvariantsin pages 1-2, liu2021prenataldiagnosisof pages 1-3, shi2024novelgnai3mutation pages 2-6) |
| ARCND2A | **PLCB4** | AD | c.986A>C, p.Asn329Ser; p.Arg621His; p.Arg621Cys; p.Tyr623Cys; p.Asn650His; c.1072G>C, p.Glu358Gln; c.983A>G, p.His328Arg; c.1928C>T, p.Ser643Phe; p.Asp360Asn; p.Arg621Leu (rieder2012ahumanhomeotic pages 3-5, tavares2017targetedmolecularinvestigation pages 4-6, tavares2016identificaçãodenovas pages 67-68, zhang2024auriculocondylarsyndrome2 pages 2-5) | Mostly **dominant-negative** catalytic-domain dysfunction rather than simple haploinsufficiency (gordon2013heterogeneityofmutational pages 11-12) | Variants cluster in X/Y catalytic domains; structural modeling predicted impaired PLC catalytic activity and disturbed IP3 generation without gross protein destabilization; ACS osteoblasts showed reduced **DLX5/DLX6** expression; PLCB4 accounts for ~57.1% of molecularly solved index cases in one cohort (16/28) (rieder2012ahumanhomeotic pages 3-5, rieder2012ahumanhomeotic pages 1-2, tavares2017targetedmolecularinvestigation pages 4-6) | Rieder et al., 2012, https://doi.org/10.1016/j.ajhg.2012.04.002; Gordon et al., 2013, https://doi.org/10.1136/jmedgenet-2012-101331; Tavares et al., 2017, https://doi.org/10.1002/ajmg.a.38101; Zhang et al., 2024, https://doi.org/10.1002/mgg3.2441 (rieder2012ahumanhomeotic pages 3-5, gordon2013heterogeneityofmutational pages 11-12, tavares2017targetedmolecularinvestigation pages 4-6, zhang2024auriculocondylarsyndrome2 pages 2-5) |
| ARCND2B | **PLCB4** | AR | Intragenic homozygous deletion; compound heterozygous splice variants c.854-1G>A and c.1238+1G>C; homozygous loss-of-function PLCB4 alleles also reported in review tables (tavares2016identificaçãodenovas pages 67-68, tavares2016identificaçãodenovas pages 68-72) | **Loss-of-function** / splice-null mechanism (tavares2016identificaçãodenovas pages 68-72, gordon2013heterogeneityofmutational pages 11-12) | Human recessive cases demonstrate that complete PLCB4 loss can produce classical ACS craniofacial features, contrasting with lack of craniofacial phenotype in some mouse null models; 13.3% (2/15) of PLCB4 variants in one summary were homozygous predicted LoF (gordon2013heterogeneityofmutational pages 11-12, tavares2016identificaçãodenovas pages 68-72) | Gordon et al., 2013, https://doi.org/10.1136/jmedgenet-2012-101331; Tavares thesis, 2016, https://doi.org/10.11606/t.41.2016.tde-14072016-142513 (gordon2013heterogeneityofmutational pages 11-12, tavares2016identificaçãodenovas pages 68-72, tavares2016identificaçãodenovas pages 67-68) |
| ARCND3 | **EDN1** | AR for syndromic ACS; AD for isolated question-mark ears | Homozygous proprotein cleavage-site substitutions in ACS; AD EDN1 variants reported include p.Val64Asp and p.Tyr83*; homozygous c.271A>G, p.Lys91Glu reported in consanguineous ACS cases (gordon2013mutationsinendothelin pages 1-2, tavares2016identificaçãodenovas pages 67-68) | Reduced or altered **EDN1 ligand activity** with mutation-dependent residual function; upstream endothelin-pathway defect (gordon2013mutationsinendothelin pages 1-2) | Mouse data show Edn1/Ednra/Ece1 loss causes severe mandibular defects; human EDN1 mutations establish ligand-level causation upstream of PLCB4/GNAI3; differing inheritance for ACS vs isolated QME likely reflects residual EDN1 activity (gordon2013mutationsinendothelin pages 1-2) | Gordon et al., 2013, https://doi.org/10.1016/j.ajhg.2013.10.023 (gordon2013mutationsinendothelin pages 1-2) |
| ARCND4 | **7p locus involving HDAC9/TWIST1 regulatory elements** | AD in reported pedigree | Tandem duplication NC_000007.14:g.18437239_18867540dup (430,302 bp), telomeric to **TWIST1** and covering most of **HDAC9** (tavares2022newlocusunderlying pages 4-4) | **Regulatory** mechanism: altered cis-regulation of **TWIST1** and disruption/duplication of HDAC9 isoforms rather than coding mutation in known ARCND genes (tavares2022newlocusunderlying pages 1-1, tavares2022newlocusunderlying pages 4-4) | Capture-C showed duplicated region contacts the **TWIST1** promoter; patient iPSC-derived neural crest cells had increased **HDAC9** (3.15-fold) and **TWIST1** (2.03-fold), ~4.3-fold reduced NCC migration, and impaired osteogenic differentiation with ~20.3-fold reduced ALP activity and reduced matrix mineralization; linkage LOD 2.88 (tavares2022newlocusunderlying pages 5-6, tavares2022newlocusunderlying pages 6-7, tavares2022newlocusunderlying pages 4-4) | Tavares et al., 2022, https://doi.org/10.1136/jmedgenet-2021-107825 (tavares2022newlocusunderlying pages 1-1, tavares2022newlocusunderlying pages 5-6, tavares2022newlocusunderlying pages 6-7, tavares2022newlocusunderlying pages 4-4) |
| Unsolved / residual ARCND fraction | Unknown locus/loci | Likely mixed | No pathogenic variants found in known genes in 2/28 index patients in one cohort; historical reports also noted unsolved families before discovery of the HDAC9/TWIST1 duplication (tavares2017targetedmolecularinvestigation pages 4-6, tavares2022newlocusunderlying pages 1-1) | Genetic heterogeneity; additional loci remain plausible (tavares2017targetedmolecularinvestigation pages 4-6) | Cohort data: 16/28 PLCB4, 6/28 GNAI3, 4/28 EDN1, and 2/28 unexplained; discovery of ARCND4 reduced but did not eliminate unsolved disease fraction (tavares2017targetedmolecularinvestigation pages 4-6, tavares2022newlocusunderlying pages 1-1) | Tavares et al., 2017, https://doi.org/10.1002/ajmg.a.38101; Tavares et al., 2022, https://doi.org/10.1136/jmedgenet-2021-107825 (tavares2017targetedmolecularinvestigation pages 4-6, tavares2022newlocusunderlying pages 1-1) |


*Table: This table summarizes the currently reported genetic causes and loci for auriculocondylar syndrome, linking subtypes to representative variants, inheritance, and proposed molecular mechanisms. It is useful for quickly comparing coding-gene causes in the EDN1 pathway with the newer regulatory ARCND4 locus involving TWIST1/HDAC9.*

#### Environmental risk factors
No validated environmental risk factors were identified in the retrieved evidence for ARCND. Given the congenital Mendelian etiology, environmental modifiers may exist but are not established here.

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved materials.

---

## 3. Phenotypes

### 3.1 Core phenotype (triad)
The core clinical triad is consistently stated as:
- **Question-mark ears (QME)**
- **Mandibular condyle hypoplasia**
- **Micrognathia**

This is explicitly stated in a 2024 clinical report: “The typical triad manifestations of ARCND include question mark ears (QMEs), mandibular condyle hypoplasia, and micrognathia.” (Shi et al., 2024; https://doi.org/10.1186/s12903-024-04575-1; Jul 2024) (shi2024novelgnai3mutation pages 1-2)

### 3.2 Additional phenotypes and frequencies/statistics
ARCND shows broad inter- and intra-familial variability and incomplete penetrance in some dominant families. (clouthier2013understandingthebasis pages 1-3, rieder2012ahumanhomeotic pages 3-5)

**Features beyond the triad** reported across sources include: microstomia/narrow mouth, prominent/full cheeks, glossoptosis, palatal anomalies (including cleft palate), facial asymmetry, pre/postauricular tags, hearing loss, feeding difficulties, respiratory distress/airway obstruction, dental crowding/malocclusion, and TMJ pathology (including ankylosis). (clouthier2013understandingthebasis pages 1-3, rieder2012ahumanhomeotic pages 1-2, tavares2017targetedmolecularinvestigation pages 4-6)

**Phenotype frequencies/statistics from retrieved cohort tables and analyses**:
- Full cheeks and QME association: In one study, **full cheeks were significantly overrepresented** (P = 0.0026) and **QME was strongly associated** with ACS (P = 0.0001). (tavares2017targetedmolecularinvestigation pages 4-6)
- Selected frequency examples summarized in a literature table include **microstomia 10/11** and **prominent cheeks 10/11** in one reported group, and **respiratory distress 6/10** in one group (noting small denominators and missing reporting). (tavares2016identificaçãodenovas pages 67-68)

### 3.3 Age of onset, severity, progression
- **Onset:** congenital / prenatal developmental.
- **Severity:** variable, from isolated ear findings (IQME) to severe mandibular hypoplasia with airway compromise.
- **Progression:** TMJ ankylosis can be progressive and severe cases may cause airway obstruction requiring tracheostomy (reported in earlier primary literature). (rieder2012ahumanhomeotic pages 1-2)

### 3.4 Quality-of-life impact
Quantitative QOL instruments were not found in retrieved evidence. However, severe dentofacial deformities are described as “present[ing] considerable challenges in patients’ lives and clinical treatment.” (shi2024novelgnai3mutation pages 1-2)

### 3.5 Suggested HPO terms (non-exhaustive)
Based on phenotypes described in retrieved evidence:
- Question mark ear / auricular clefting: **HP:0009907** (Question mark ear; commonly used HPO term for QME)
- Micrognathia: **HP:0000347**
- Mandibular condyle hypoplasia: **HP:0009119** (Mandibular condyle hypoplasia)
- Microstomia: **HP:0000174**
- Glossoptosis: **HP:0000162**
- Cleft palate: **HP:0000175**
- Hearing impairment: **HP:0000365**
- Facial asymmetry: **HP:0000324**
- Malocclusion/crowded teeth: **HP:0000689** (Crowding of teeth), **HP:0000688** (Malocclusion)

(These HPO identifiers are standard ontology mappings; the evidence for the underlying phenotypes is in the cited papers.) (clouthier2013understandingthebasis pages 1-3, tavares2017targetedmolecularinvestigation pages 4-6, shi2024novelgnai3mutation pages 2-6)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and loci
Causal genes/locus in retrieved evidence include PLCB4, GNAI3, EDN1, and a 7p duplication affecting regulatory elements interacting with TWIST1 (HDAC9/TWIST1 region). (tavares2017targetedmolecularinvestigation pages 4-6, gordon2013mutationsinendothelin pages 1-2, tavares2022newlocusunderlying pages 5-6)

### 4.2 Pathogenic variants: types and functional consequences
- **PLCB4:** predominantly **missense variants** in catalytic domains (X/Y), with evidence suggesting **dominant-negative** action for many heterozygous missense alleles; additionally, **biallelic loss-of-function** (deletions/splice) can cause recessive disease (ARCND2B). (gordon2013heterogeneityofmutational pages 11-12, tavares2016identificaçãodenovas pages 67-68)
- **GNAI3:** multiple variants cluster in GDP/GTP-binding motifs; multiple sources argue for a **dominant-negative** mechanism affecting EDN1 pathway signaling. (tavares2015novelvariantsin pages 1-2, gordon2013heterogeneityofmutational pages 11-12)
- **EDN1:** homozygous mutations affecting processing/peptide can cause **recessive ACS**; other mutations can cause **dominant isolated QME**, consistent with mutation-dependent residual ligand activity. (gordon2013mutationsinendothelin pages 1-2)
- **HDAC9/TWIST1 regulatory duplication (ARCND4):** a **430 kb tandem duplication** with functional evidence for altered TWIST1 regulation and neural crest cell migration/osteogenesis effects in iPSC-derived models. (tavares2022newlocusunderlying pages 5-6, tavares2022newlocusunderlying pages 4-4)

### 4.3 Allele frequencies
Population-database frequency statements were limited in retrieved excerpts. Example: GNAI3 p.Gly40Arg was “not observed in 10,758 control chromosomes” in Rieder et al. (2012). (rieder2012ahumanhomeotic pages 3-5)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes or epigenetic signatures specific to ARCND were found in retrieved evidence.

---

## 5. Environmental information
No ARCND-specific environmental, lifestyle, or infectious contributors were identified in retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Molecular pathway: EDN1–EDNRA–(GNAI3/PLCB4)–DLX5/6 craniofacial patterning
A central mechanistic model supported by human genetics, functional assays, and animal studies is disruption of **endothelin-1 signaling** in cranial neural crest:
- **EDN1** is a ligand critical for patterning the mandibular portion of the first pharyngeal arch via **EDNRA** signaling; murine deletion of Edn1/Ednra/Ece1 causes severe mandibular defects. (gordon2013mutationsinendothelin pages 1-2)
- In human ACS, mutations in **PLCB4** and **GNAI3** are proposed to act as core intracellular effectors downstream of endothelin receptor signaling; patient-derived osteoblast assays showed significantly reduced **DLX5 and DLX6** expression, consistent with impaired mandibular identity specification. (rieder2012ahumanhomeotic pages 1-2)
- Clouthier et al. (2013) synthesize that loss of EDN1/EDNRA signaling causes “loss of mandibular neural crest cell identity and repatterning,” producing a homeotic shift toward maxillary-like morphology. (clouthier2013understandingthebasis pages 1-3)

### 6.2 Regulatory mechanism: TWIST1 dosage and neural crest migration (ARCND4)
Tavares et al. (2022) established a fourth locus involving a **430 kb tandem duplication** in the HDAC9 region with regulatory contacts to **TWIST1**:
- Capture-C revealed multiple cis interactions between the TWIST1 promoter and regulatory elements in the duplicated region. (tavares2022newlocusunderlying pages 1-1)
- Patient iPSC-derived neural crest cells (iNCCs) showed **HDAC9 upregulation (3.15-fold; p=0.009)** and **TWIST1 upregulation (2.03-fold; p=0.03)**, with **~4.3-fold reduced migratory capacity (p=0.0009)**. (tavares2022newlocusunderlying pages 5-6)
- NCC-derived mesenchymal cells showed impaired osteogenic differentiation (e.g., markedly reduced ALP activity and reduced mineralization). (tavares2022newlocusunderlying pages 5-6)

### 6.3 Suggested GO biological process terms (examples)
- Neural crest cell migration: **GO:0001755**
- Craniofacial morphogenesis: **GO:0060325**
- Pharyngeal arch development: **GO:0060034**
- Endothelin receptor signaling pathway: **GO:0072000** (related terms depending on curation)
- Osteoblast differentiation / ossification: **GO:0001649**, **GO:0001503**

### 6.4 Suggested cell types (Cell Ontology; examples)
- Cranial neural crest cell: **CL:0002638** (commonly used for neural crest lineage)
- Mesenchymal stem cell: **CL:0000134**
- Osteoblast: **CL:0000062**

(Functional evidence for NCC involvement and osteogenic defects is supported by iPSC-derived NCC and nMSC assays in Tavares et al. 2022.) (tavares2022newlocusunderlying pages 5-6)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level (with UBERON suggestions)
Primary structures:
- External ear / pinna (**UBERON:0001690**) — QME malformation at helix–lobule junction. (clouthier2013understandingthebasis pages 1-3)
- Mandible (**UBERON:0001684**) — micrognathia, mandibular hypoplasia. (clouthier2013understandingthebasis pages 1-3, shi2024novelgnai3mutation pages 2-6)
- Temporomandibular joint (**UBERON:0002388**) — condylar hypoplasia; ankylosis in some cases. (rieder2012ahumanhomeotic pages 1-2)
- First/second pharyngeal arches (**UBERON:0004456**, **UBERON:0004457**; developmental structures) (tavares2022newlocusunderlying pages 1-2)

Secondary/associated:
- Upper airway/oropharynx (**UBERON:0001723** pharynx; airway volumes) in severe micrognathia/OSA. (shi2024novelgnai3mutation pages 2-6)

---

## 8. Temporal development (natural history)
ARCND is a congenital developmental disorder, sometimes detectable prenatally by ultrasound when severe micrognathia/mandibular hypoplasia is present.

Prenatal case evidence: Liu et al. (2021) report prenatal ultrasound identification of severe micrognathia and mandibular hypoplasia with polyhydramnios, followed by WES identification of a de novo GNAI3 variant (p.Ser47Asn). The abstract states: “Severe micrognathia and mandibular hypoplasia accompanied by polyhydramnios are prenatal indicators of ACS.” (https://doi.org/10.1186/s12884-021-04238-x; Nov 2021) (liu2021prenataldiagnosisof pages 1-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
ARCND can be **autosomal dominant or autosomal recessive**, depending on gene and variant class:
- Dominant inheritance with **variable expressivity** and occasional **non-penetrance** is widely noted (e.g., GNAI3/PLCB4 families). (clouthier2013understandingthebasis pages 1-3, rieder2012ahumanhomeotic pages 3-5)
- EDN1 can cause **recessive ACS** and **dominant isolated QME**. (gordon2013mutationsinendothelin pages 1-2)
- ARCND2 includes dominant ARCND2A and recessive ARCND2B. (zhang2024auriculocondylarsyndrome2 pages 1-2)

### 9.2 Epidemiology
ARCND is repeatedly described as extremely rare:
- Orphanet-cited prevalence “under 1 in 1,000,000.” (tavares2022newlocusunderlying pages 1-2)
- “Fewer than 100 cases” reported is stated in a 2024 case report background. (shi2024novelgnai3mutation pages 1-2)

Robust population prevalence/incidence estimates were not provided in the retrieved primary texts.

---

## 10. Diagnostics

### 10.1 Clinical diagnosis
The clinical triad is emphasized as the diagnostic anchor, with recognition that incomplete presentations occur and can lead to misdiagnosis.

Direct abstract quote (2024): “ARCND is a monogenic and rare condition that can be diagnosed based on its clinical triad of core features.” (Shi et al., 2024; https://doi.org/10.1186/s12903-024-04575-1) (shi2024novelgnai3mutation pages 1-2)

### 10.2 Differential diagnosis
A 2024 clinical report lists potential misdiagnoses including:
- Oculo-auriculo-vertebral spectrum
- Treacher Collins syndrome
- Mandibulofacial dysostosis
- Guion-Almeida type
- Meier-Gorlin syndrome

(shi2024novelgnai3mutation pages 1-2)

### 10.3 Genetic testing and real-world implementation
- **WES** is repeatedly used in modern diagnosis and case resolution (including prenatal and postnatal), identifying novel GNAI3 insertions/missense changes. (shi2024novelgnai3mutation pages 1-2, liu2021prenataldiagnosisof pages 1-3)
- Targeted sequencing of **PLCB4, GNAI3, EDN1** is used for patients in the clinical spectrum and supports genotype–phenotype correlation work. (tavares2017targetedmolecularinvestigation pages 4-6)

In prenatal settings, WES has been used as confirmatory testing when ultrasound indicates severe mandibular anomalies. (liu2021prenataldiagnosisof pages 1-3)

### 10.4 Suggested diagnostic workflow (evidence-based synthesis)
1) Recognize craniofacial pattern consistent with ARCND (QME + micrognathia + condylar hypoplasia) (clouthier2013understandingthebasis pages 1-3, tavares2017targetedmolecularinvestigation pages 4-6)
2) Molecular testing: targeted ARCND genes (PLCB4, GNAI3, EDN1) or WES; consider CNV analysis if negative (HDAC9/TWIST1 duplication) (tavares2017targetedmolecularinvestigation pages 4-6, tavares2022newlocusunderlying pages 4-4)
3) Multidisciplinary craniofacial and airway evaluation in severe cases (sleep study/OSA assessment when indicated) (shi2024novelgnai3mutation pages 2-6)

---

## 11. Outcomes / prognosis

ARCND outcomes depend on severity (airway compromise, feeding difficulties, craniofacial growth, TMJ involvement). Quantitative survival data were not found in the retrieved evidence.

Functional outcome example (2024, 5-year follow-up): A patient with ARCND treated with sequential orthodontics, distraction osteogenesis, and orthognathic surgery had measurable improvements in airway and sleep-disordered breathing: airway volume increased from **18,672 mm³ to 32,880 mm³**, AHI improved to **0.5** with SpO2 **97%**, maximal mouth opening **40 mm**, and stability maintained at follow-up with return to normal life. (shi2024novelgnai3mutation pages 2-6)

---

## 12. Treatment

### 12.1 Current applications and real-world implementations
There are **no disease-specific pharmacotherapies** in the retrieved evidence; management is primarily **craniofacial, orthodontic, and surgical**, tailored to severity.

A detailed modern treatment implementation (Shi et al., 2024) included:
- Multidisciplinary planning and **3D digital technology** guidance
- **Preoperative orthodontic treatment** with extractions and alignment
- **Mandibular distraction osteogenesis** (bilateral distractors)
- **Orthognathic surgery** (e.g., Le Fort I, BSSRO, genioplasty)
- Demonstrated 5-year stable functional improvement (airway metrics, OSA resolution) (shi2024novelgnai3mutation pages 2-6)

### 12.2 MAXO (Medical Action Ontology) term suggestions
- Mandibular distraction osteogenesis: **MAXO:0001170** (Distraction osteogenesis; exact ID may vary by MAXO version)
- Orthognathic surgery / corrective jaw surgery: **MAXO:0000127** (Surgical procedure) with more specific jaw surgery subclass if available
- Genetic testing / exome sequencing: **MAXO:0000120** (Genetic testing)
- Polysomnography / sleep study: **MAXO:0000537** (Sleep study; exact ID may vary)

(These MAXO mappings are suggestions; evidence of the interventions is in the cited case report.) (shi2024novelgnai3mutation pages 2-6)

### 12.3 Clinical trials
ClinicalTrials.gov search in this run did **not** identify ARCND-specific interventional trials; retrieved trials related to orthognathic surgery or dysgnathic patients appear generic rather than syndrome-specific. (clinical trial metadata returned; no ARCND-targeted NCT found) (shi2024novelgnai3mutation pages 2-6)

---

## 13. Prevention
Primary prevention is not established because ARCND is genetic and typically congenital.

Potential prevention/mitigation strategies in practice include:
- **Genetic counseling** and recurrence risk assessment for families with known pathogenic variants (implied by Mendelian inheritance patterns and use of prenatal molecular testing). (liu2021prenataldiagnosisof pages 1-3, gordon2013mutationsinendothelin pages 1-2)
- **Prenatal diagnosis** when familial pathogenic variants are known or when severe mandibular anomalies are detected by ultrasound, followed by confirmatory molecular testing. (liu2021prenataldiagnosisof pages 1-3)

---

## 14. Other species / natural disease
Natural disease analogs in other species were not identified in retrieved evidence. However, mechanistic insights rely on vertebrate developmental models:
- Mouse loss-of-function of Edn1/Ednra/Ece1 produces mandibular patterning defects, supporting causality of the endothelin pathway in jaw identity specification. (gordon2013mutationsinendothelin pages 1-2)

---

## 15. Model organisms
ARCND mechanisms are informed by mouse and zebrafish craniofacial development studies summarized in the 2013 Seminars review, alongside human genetics. (clouthier2013understandingthebasis pages 1-3)

A human stem-cell/iPSC model has been used as a complementary system for ARCND4, demonstrating altered gene expression and functional deficits in iPSC-derived cranial neural crest migration and osteogenic differentiation. (tavares2022newlocusunderlying pages 5-6)

---

## Recent developments (prioritizing 2023–2024)

1) **2024: Longitudinal treatment outcomes and digital surgical workflows**
   - BMC Oral Health (Jul 2024) reports a novel inherited GNAI3 insertion and detailed multi-stage orthodontic + surgical treatment with quantitative improvements in airway volume and sleep apnea metrics at 5 years. (https://doi.org/10.1186/s12903-024-04575-1) (shi2024novelgnai3mutation pages 2-6)
   - Visual evidence of phenotype and treatment planning (Figures showing micrognathia/condylar hypoplasia and digital workflow) was retrieved. (shi2024novelgnai3mutation media 1e0f905a, shi2024novelgnai3mutation media 063b200e)

2) **2024: Expanded PLCB4 variant spectrum and neonatal presentation**
   - Molecular Genetics & Genomic Medicine (Apr 2024) reports a de novo PLCB4 variant and consolidates subtype nomenclature and prevalence statements, including ARCND subtype OMIM numbers and literature counts (36 PLCB4-mutant patients retrieved). (https://doi.org/10.1002/mgg3.2441) (zhang2024auriculocondylarsyndrome2 pages 2-5, zhang2024auriculocondylarsyndrome2 pages 1-2)

3) **2023: Continued mechanistic refinement in endothelin receptor signaling (related craniofacial endothelin disorders)**
   - Although focused on EDNRA gain-of-function in mandibulofacial dysostosis with alopecia (MFDA), JCI 2023 provides modern GPCR allostery/ligand affinity mechanistic analysis relevant to endothelin receptor biology broadly. (https://doi.org/10.1172/jci151536; Feb 2023) (tavares2022newlocusunderlying pages 1-2)

---

## Expert opinion / authoritative synthesis
The 2013 Seminars review (Clouthier et al.) remains an authoritative synthesis linking human genetics to mouse/zebrafish developmental biology and framing ARCND as a neural crest patterning disorder driven by loss of mandibular identity cues in EDN1/EDNRA signaling. (clouthier2013understandingthebasis pages 1-3)

A 2022 J Med Genet study provides authoritative locus-level expansion beyond the classic EDN1 pathway genes by demonstrating a regulatory duplication affecting TWIST1 control elements and measurable NCC migration defects in iPSC-derived models—supporting the view that ARCND includes both **signal-transduction** and **regulatory/cranial neural crest migration** etiologies. (tavares2022newlocusunderlying pages 5-6)

---

## Visual evidence (phenotype and management)
- Patient craniofacial phenotype and mandibular condyle hypoplasia on 3D CT reconstructions (Figure 1) and digital treatment workflow (Figure 4) from the 2024 ARCND case report. (shi2024novelgnai3mutation media 1e0f905a, shi2024novelgnai3mutation media 063b200e)

---

## Key limitations of this report (evidence gaps)
- Specific **ICD-10/ICD-11** and **MeSH** identifiers were not present in the retrieved evidence.
- Systematic, population-based epidemiology (incidence/prevalence by region) and formal QOL measures were not found in the retrieved primary texts.
- ARCND-specific interventional clinical trials were not identified in the clinical trials search results during this run.

---

## References (URLs and publication dates)
- Rieder MJ et al. *Am J Hum Genet.* May 2012. https://doi.org/10.1016/j.ajhg.2012.04.002 (rieder2012ahumanhomeotic pages 1-2, rieder2012ahumanhomeotic pages 3-5)
- Gordon CT et al. *Am J Hum Genet.* Dec 2013. https://doi.org/10.1016/j.ajhg.2013.10.023 (gordon2013mutationsinendothelin pages 1-2)
- Clouthier DE et al. *Am J Med Genet C Semin Med Genet.* Nov 2013. https://doi.org/10.1002/ajmg.c.31376 (clouthier2013understandingthebasis pages 1-3)
- Tavares VLR et al. *Am J Med Genet A.* Apr 2017. https://doi.org/10.1002/ajmg.a.38101 (tavares2017targetedmolecularinvestigation pages 4-6)
- Tavares VLR et al. *J Med Genet.* Nov 2022. https://doi.org/10.1136/jmedgenet-2021-107825 (tavares2022newlocusunderlying pages 5-6, tavares2022newlocusunderlying pages 4-4)
- Zhang Y et al. *Mol Genet Genomic Med.* Apr 2024. https://doi.org/10.1002/mgg3.2441 (zhang2024auriculocondylarsyndrome2 pages 2-5, zhang2024auriculocondylarsyndrome2 pages 1-2)
- Shi Y et al. *BMC Oral Health.* Jul 2024. https://doi.org/10.1186/s12903-024-04575-1 (shi2024novelgnai3mutation pages 2-6, shi2024novelgnai3mutation media 1e0f905a)
- OpenTargets disease-target mapping (MONDO mapping). (OpenTargets Search: Auriculocondylar syndrome)


References

1. (clouthier2013understandingthebasis pages 1-3): David E. Clouthier, Maria Rita Passos‐Bueno, Andre L.P. Tavares, Stanislas Lyonnet, Jeanne Amiel, and Christopher T. Gordon. Understanding the basis of auriculocondylar syndrome: insights from human, mouse and zebrafish genetic studies. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 163:306-317, Nov 2013. URL: https://doi.org/10.1002/ajmg.c.31376, doi:10.1002/ajmg.c.31376. This article has 69 citations.

2. (rieder2012ahumanhomeotic pages 1-2): Mark J. Rieder, Glenn E. Green, Sarah S. Park, Brendan D. Stamper, Christopher T. Gordon, Jason M. Johnson, Christopher M. Cunniff, Joshua D. Smith, Sarah B. Emery, Stanislas Lyonnet, Jeanne Amiel, Muriel Holder, Andrew A. Heggie, Michael J. Bamshad, Deborah A. Nickerson, Timothy C. Cox, Anne V. Hing, Jeremy A. Horst, and Michael L. Cunningham. A human homeotic transformation resulting from mutations in plcb4 and gnai3 causes auriculocondylar syndrome. American journal of human genetics, 90 5:907-14, May 2012. URL: https://doi.org/10.1016/j.ajhg.2012.04.002, doi:10.1016/j.ajhg.2012.04.002. This article has 114 citations and is from a highest quality peer-reviewed journal.

3. (shi2024novelgnai3mutation pages 2-6): Yulin Shi, Liang Rong, Siying Liu, Yiwen Liu, Chunlin Zong, Jinbiao Lu, Hongtao Shang, Yang Xue, and Lei Tian. Novel gnai3 mutation in a chinese family with auriculocondylar syndrome and treatment of severe dentofacial deformities: a 5-year follow-up case report. BMC Oral Health, Jul 2024. URL: https://doi.org/10.1186/s12903-024-04575-1, doi:10.1186/s12903-024-04575-1. This article has 2 citations and is from a peer-reviewed journal.

4. (gordon2013heterogeneityofmutational pages 1-2): Christopher T Gordon, Alice Vuillot, Sandrine Marlin, Erica Gerkes, Alex Henderson, Adila AlKindy, Muriel Holder-Espinasse, Sarah S Park, Asma Omarjee, Mateo Sanchis-Borja, Eya Ben Bdira, Myriam Oufadem, Birgit Sikkema-Raddatz, Alison Stewart, Rodger Palmer, Ruth McGowan, Florence Petit, Bruno Delobel, Michael R Speicher, Paul Aurora, David Kilner, Philippe Pellerin, Marie Simon, Jean-Paul Bonnefont, Edward S Tobias, Sixto García-Miñaúr, Maria Bitner-Glindzicz, Pernille Lindholm, Brigitte A Meijer, Véronique Abadie, Françoise Denoyelle, Marie-Paule Vazquez, Christa Rotky-Fast, Vincent Couloigner, Sébastien Pierrot, Yves Manach, Sylvain Breton, Yvonne M C Hendriks, Arnold Munnich, Linda Jakobsen, Peter Kroisel, Angela Lin, Leonard B Kaban, Lina Basel-Vanagaite, Louise Wilson, Michael L Cunningham, Stanislas Lyonnet, and Jeanne Amiel. Heterogeneity of mutational mechanisms and modes of inheritance in auriculocondylar syndrome. Journal of Medical Genetics, 50:174-186, Jan 2013. URL: https://doi.org/10.1136/jmedgenet-2012-101331, doi:10.1136/jmedgenet-2012-101331. This article has 58 citations and is from a domain leading peer-reviewed journal.

5. (OpenTargets Search: Auriculocondylar syndrome): Open Targets Query (Auriculocondylar syndrome, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (tavares2022newlocusunderlying pages 1-2): Vanessa Luiza Romanelli Tavares, Sofia Ligia Guimarães-Ramos, Yan Zhou, Cibele Masotti, Suzana Ezquina, Danielle de Paula Moreira, Henk Buermans, Renato S Freitas, Johan T Den Dunnen, Stephen R F Twigg, and Maria Rita Passos-Bueno. New locus underlying auriculocondylar syndrome (arcnd): 430 kb duplication involving twist1 regulatory elements. Journal of Medical Genetics, 59:895-905, Nov 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107825, doi:10.1136/jmedgenet-2021-107825. This article has 9 citations and is from a domain leading peer-reviewed journal.

7. (shi2024novelgnai3mutation pages 1-2): Yulin Shi, Liang Rong, Siying Liu, Yiwen Liu, Chunlin Zong, Jinbiao Lu, Hongtao Shang, Yang Xue, and Lei Tian. Novel gnai3 mutation in a chinese family with auriculocondylar syndrome and treatment of severe dentofacial deformities: a 5-year follow-up case report. BMC Oral Health, Jul 2024. URL: https://doi.org/10.1186/s12903-024-04575-1, doi:10.1186/s12903-024-04575-1. This article has 2 citations and is from a peer-reviewed journal.

8. (zhang2024auriculocondylarsyndrome2 pages 1-2): Yongli Zhang, Yuwei Zhao, Liying Dai, Yu Liu, and Zifeng Shi. Auriculocondylar syndrome 2 caused by a novel plcb4 variant in a male chinese neonate: a case report and review of the literature. Molecular Genetics & Genomic Medicine, Apr 2024. URL: https://doi.org/10.1002/mgg3.2441, doi:10.1002/mgg3.2441. This article has 3 citations and is from a peer-reviewed journal.

9. (gordon2013mutationsinendothelin pages 1-2): Christopher T. Gordon, Florence Petit, Peter M. Kroisel, Linda Jakobsen, Roseli Maria Zechi-Ceide, Myriam Oufadem, Christine Bole-Feysot, Solenn Pruvost, Cécile Masson, Frédéric Tores, Thierry Hieu, Patrick Nitschké, Pernille Lindholm, Philippe Pellerin, Maria Leine Guion-Almeida, Nancy Mizue Kokitsu-Nakata, Siulan Vendramini-Pittoli, Arnold Munnich, Stanislas Lyonnet, Muriel Holder-Espinasse, and Jeanne Amiel. Mutations in endothelin 1 cause recessive auriculocondylar syndrome and dominant isolated question-mark ears. American journal of human genetics, 93 6:1118-25, Dec 2013. URL: https://doi.org/10.1016/j.ajhg.2013.10.023, doi:10.1016/j.ajhg.2013.10.023. This article has 86 citations and is from a highest quality peer-reviewed journal.

10. (tavares2017targetedmolecularinvestigation pages 4-6): Vanessa L. Romanelli Tavares, Roseli M. Zechi‐Ceide, Debora R. Bertola, Christopher T. Gordon, Simone G. Ferreira, Gabriella S. P. Hsia, Guilherme L. Yamamoto, Suzana A. M. Ezquina, Nancy M. Kokitsu‐Nakata, Siulan Vendramini‐Pittoli, Renato S. Freitas, Josiane Souza, Cesar A. Raposo‐Amaral, Mayana Zatz, Jeanne Amiel, Maria L. Guion‐Almeida, and Maria Rita Passos‐Bueno. Targeted molecular investigation in patients within the clinical spectrum of auriculocondylar syndrome. American Journal of Medical Genetics Part A, 173:938-945, Apr 2017. URL: https://doi.org/10.1002/ajmg.a.38101, doi:10.1002/ajmg.a.38101. This article has 17 citations.

11. (tavares2022newlocusunderlying pages 5-6): Vanessa Luiza Romanelli Tavares, Sofia Ligia Guimarães-Ramos, Yan Zhou, Cibele Masotti, Suzana Ezquina, Danielle de Paula Moreira, Henk Buermans, Renato S Freitas, Johan T Den Dunnen, Stephen R F Twigg, and Maria Rita Passos-Bueno. New locus underlying auriculocondylar syndrome (arcnd): 430 kb duplication involving twist1 regulatory elements. Journal of Medical Genetics, 59:895-905, Nov 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107825, doi:10.1136/jmedgenet-2021-107825. This article has 9 citations and is from a domain leading peer-reviewed journal.

12. (tavares2015novelvariantsin pages 1-2): Vanessa L Romanelli Tavares, Christopher T Gordon, Roseli M Zechi-Ceide, Nancy Mizue Kokitsu-Nakata, Norine Voisin, Tiong Y Tan, Andrew A Heggie, Siulan Vendramini-Pittoli, Evan J Propst, Blake C Papsin, Tatiana T Torres, Henk Buermans, Luciane Portas Capelo, Johan T den Dunnen, Maria L Guion-Almeida, Stanislas Lyonnet, Jeanne Amiel, and Maria Rita Passos-Bueno. Novel variants in gnai3 associated with auriculocondylar syndrome strengthen a common dominant negative effect. European Journal of Human Genetics, 23:481-485, Jul 2015. URL: https://doi.org/10.1038/ejhg.2014.132, doi:10.1038/ejhg.2014.132. This article has 36 citations and is from a domain leading peer-reviewed journal.

13. (tavares2022newlocusunderlying pages 4-4): Vanessa Luiza Romanelli Tavares, Sofia Ligia Guimarães-Ramos, Yan Zhou, Cibele Masotti, Suzana Ezquina, Danielle de Paula Moreira, Henk Buermans, Renato S Freitas, Johan T Den Dunnen, Stephen R F Twigg, and Maria Rita Passos-Bueno. New locus underlying auriculocondylar syndrome (arcnd): 430 kb duplication involving twist1 regulatory elements. Journal of Medical Genetics, 59:895-905, Nov 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107825, doi:10.1136/jmedgenet-2021-107825. This article has 9 citations and is from a domain leading peer-reviewed journal.

14. (rieder2012ahumanhomeotic pages 3-5): Mark J. Rieder, Glenn E. Green, Sarah S. Park, Brendan D. Stamper, Christopher T. Gordon, Jason M. Johnson, Christopher M. Cunniff, Joshua D. Smith, Sarah B. Emery, Stanislas Lyonnet, Jeanne Amiel, Muriel Holder, Andrew A. Heggie, Michael J. Bamshad, Deborah A. Nickerson, Timothy C. Cox, Anne V. Hing, Jeremy A. Horst, and Michael L. Cunningham. A human homeotic transformation resulting from mutations in plcb4 and gnai3 causes auriculocondylar syndrome. American journal of human genetics, 90 5:907-14, May 2012. URL: https://doi.org/10.1016/j.ajhg.2012.04.002, doi:10.1016/j.ajhg.2012.04.002. This article has 114 citations and is from a highest quality peer-reviewed journal.

15. (tavares2016identificaçãodenovas pages 67-68): Vanessa Luiza Romanelli Tavares. Identificação de novas variantes causativas e investigação da heterogeneidade clínica da síndrome aurículo-condilar identification of novel causative variants and investigation of clinical heterogeneity of auriculocondylar syndrome. ArXiv, Mar 2016. URL: https://doi.org/10.11606/t.41.2016.tde-14072016-142513, doi:10.11606/t.41.2016.tde-14072016-142513. This article has 0 citations.

16. (liu2021prenataldiagnosisof pages 1-3): Xiaoliang Liu, Wei Sun, Jun Wang, Guoming Chu, Rong He, Bijun Zhang, and Yanyan Zhao. Prenatal diagnosis of auriculocondylar syndrome with a novel missense variant of gnai3: a case report. BMC Pregnancy and Childbirth, Nov 2021. URL: https://doi.org/10.1186/s12884-021-04238-x, doi:10.1186/s12884-021-04238-x. This article has 8 citations and is from a peer-reviewed journal.

17. (gordon2013heterogeneityofmutational pages 11-12): Christopher T Gordon, Alice Vuillot, Sandrine Marlin, Erica Gerkes, Alex Henderson, Adila AlKindy, Muriel Holder-Espinasse, Sarah S Park, Asma Omarjee, Mateo Sanchis-Borja, Eya Ben Bdira, Myriam Oufadem, Birgit Sikkema-Raddatz, Alison Stewart, Rodger Palmer, Ruth McGowan, Florence Petit, Bruno Delobel, Michael R Speicher, Paul Aurora, David Kilner, Philippe Pellerin, Marie Simon, Jean-Paul Bonnefont, Edward S Tobias, Sixto García-Miñaúr, Maria Bitner-Glindzicz, Pernille Lindholm, Brigitte A Meijer, Véronique Abadie, Françoise Denoyelle, Marie-Paule Vazquez, Christa Rotky-Fast, Vincent Couloigner, Sébastien Pierrot, Yves Manach, Sylvain Breton, Yvonne M C Hendriks, Arnold Munnich, Linda Jakobsen, Peter Kroisel, Angela Lin, Leonard B Kaban, Lina Basel-Vanagaite, Louise Wilson, Michael L Cunningham, Stanislas Lyonnet, and Jeanne Amiel. Heterogeneity of mutational mechanisms and modes of inheritance in auriculocondylar syndrome. Journal of Medical Genetics, 50:174-186, Jan 2013. URL: https://doi.org/10.1136/jmedgenet-2012-101331, doi:10.1136/jmedgenet-2012-101331. This article has 58 citations and is from a domain leading peer-reviewed journal.

18. (zhang2024auriculocondylarsyndrome2 pages 2-5): Yongli Zhang, Yuwei Zhao, Liying Dai, Yu Liu, and Zifeng Shi. Auriculocondylar syndrome 2 caused by a novel plcb4 variant in a male chinese neonate: a case report and review of the literature. Molecular Genetics & Genomic Medicine, Apr 2024. URL: https://doi.org/10.1002/mgg3.2441, doi:10.1002/mgg3.2441. This article has 3 citations and is from a peer-reviewed journal.

19. (tavares2016identificaçãodenovas pages 68-72): Vanessa Luiza Romanelli Tavares. Identificação de novas variantes causativas e investigação da heterogeneidade clínica da síndrome aurículo-condilar identification of novel causative variants and investigation of clinical heterogeneity of auriculocondylar syndrome. ArXiv, Mar 2016. URL: https://doi.org/10.11606/t.41.2016.tde-14072016-142513, doi:10.11606/t.41.2016.tde-14072016-142513. This article has 0 citations.

20. (tavares2022newlocusunderlying pages 1-1): Vanessa Luiza Romanelli Tavares, Sofia Ligia Guimarães-Ramos, Yan Zhou, Cibele Masotti, Suzana Ezquina, Danielle de Paula Moreira, Henk Buermans, Renato S Freitas, Johan T Den Dunnen, Stephen R F Twigg, and Maria Rita Passos-Bueno. New locus underlying auriculocondylar syndrome (arcnd): 430 kb duplication involving twist1 regulatory elements. Journal of Medical Genetics, 59:895-905, Nov 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107825, doi:10.1136/jmedgenet-2021-107825. This article has 9 citations and is from a domain leading peer-reviewed journal.

21. (tavares2022newlocusunderlying pages 6-7): Vanessa Luiza Romanelli Tavares, Sofia Ligia Guimarães-Ramos, Yan Zhou, Cibele Masotti, Suzana Ezquina, Danielle de Paula Moreira, Henk Buermans, Renato S Freitas, Johan T Den Dunnen, Stephen R F Twigg, and Maria Rita Passos-Bueno. New locus underlying auriculocondylar syndrome (arcnd): 430 kb duplication involving twist1 regulatory elements. Journal of Medical Genetics, 59:895-905, Nov 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107825, doi:10.1136/jmedgenet-2021-107825. This article has 9 citations and is from a domain leading peer-reviewed journal.

22. (shi2024novelgnai3mutation media 1e0f905a): Yulin Shi, Liang Rong, Siying Liu, Yiwen Liu, Chunlin Zong, Jinbiao Lu, Hongtao Shang, Yang Xue, and Lei Tian. Novel gnai3 mutation in a chinese family with auriculocondylar syndrome and treatment of severe dentofacial deformities: a 5-year follow-up case report. BMC Oral Health, Jul 2024. URL: https://doi.org/10.1186/s12903-024-04575-1, doi:10.1186/s12903-024-04575-1. This article has 2 citations and is from a peer-reviewed journal.

23. (shi2024novelgnai3mutation media 063b200e): Yulin Shi, Liang Rong, Siying Liu, Yiwen Liu, Chunlin Zong, Jinbiao Lu, Hongtao Shang, Yang Xue, and Lei Tian. Novel gnai3 mutation in a chinese family with auriculocondylar syndrome and treatment of severe dentofacial deformities: a 5-year follow-up case report. BMC Oral Health, Jul 2024. URL: https://doi.org/10.1186/s12903-024-04575-1, doi:10.1186/s12903-024-04575-1. This article has 2 citations and is from a peer-reviewed journal.