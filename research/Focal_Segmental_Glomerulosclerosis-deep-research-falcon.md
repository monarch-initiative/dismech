---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T15:56:15.946515'
end_time: '2026-05-08T16:18:46.146625'
duration_seconds: 1350.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Focal Segmental Glomerulosclerosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Focal Segmental Glomerulosclerosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Focal Segmental Glomerulosclerosis** covering all of the
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
- **Disease Name:** Focal Segmental Glomerulosclerosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Focal Segmental Glomerulosclerosis** covering all of the
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


## Comprehensive Research Report: Focal Segmental Glomerulosclerosis (FSGS)

### Executive Summary
Focal segmental glomerulosclerosis (FSGS) is best understood as a **histopathologic lesion pattern (a podocytopathy)** rather than a single disease entity; it arises from heterogeneous upstream causes that converge on **podocyte injury, podocyte depletion, proteinuria, and progressive glomerular scarring**. Contemporary practice increasingly emphasizes **etiology-based classification (primary/immune-mediated vs genetic vs secondary/maladaptive/toxic/infectious vs undetermined)**, because etiology predicts treatment response and informs whether immunosuppression is appropriate. Recent (2023–2024) literature highlights (i) improved mechanistic framing of primary FSGS around immune/circulating-factor biology, (ii) expanding roles for **next-generation sequencing** in steroid-resistant and familial disease, (iii) treatment evolution with **dual endothelin-angiotensin receptor blockade (sparsentan)** showing robust antiproteinuric effects and favorable long-term eGFR slope in extension studies, and (iv) persistent major burden of kidney failure attributable to FSGS, especially in certain US demographic groups.


---

## 1. Disease Information

### 1.1 Definition and overview
- **Definition (current understanding):** FSGS is a *histologic pattern of injury* characterized by **focal (some glomeruli) and segmental (part of the glomerular tuft) sclerosis**, typically accompanied by variable podocyte foot process effacement on electron microscopy, reflecting injury and loss of podocytes (cos2023noveltreatmentparadigms pages 1-2, salfi2023currentunderstandingof pages 1-2).
- **Why classification matters:** Because many different causal pathways produce the same lesion pattern, FSGS is clinically approached as a heterogeneous syndrome requiring etiology stratification (cos2023noveltreatmentparadigms pages 1-2, mirioglu2024managementofadult pages 2-3).

### 1.2 Disease identifiers and ontology mapping
- **MONDO (available from retrieved evidence):**
  - “Inherited focal segmental glomerulosclerosis” **MONDO_0005363** (OpenTargets Search: Focal segmental glomerulosclerosis)
  - Example inherited subtype entities returned by Open Targets include “FSGS 1” **MONDO_0011303** (OpenTargets Search: Focal segmental glomerulosclerosis)
- **Open Targets disease ID:** FSGS is indexed as **EFO_0004236** in Open Targets output (OpenTargets Search: Focal segmental glomerulosclerosis).

**Gap note (knowledge-base readiness):** ICD-10/ICD-11, MeSH, Orphanet, and OMIM cross-references were not present in the retrieved texts and therefore cannot be asserted here without additional ontology lookups.

### 1.3 Synonyms / alternative names
- “Focal segmental glomerulosclerosis” (FSGS) is often used interchangeably with its lesion description; in practice, it is frequently discussed under the umbrella of **“podocytopathies”** with minimal change disease (MCD) (mirioglu2024managementofadult pages 2-3, salfi2023currentunderstandingof pages 1-2).

### 1.4 Source type of information
- The evidence synthesized here is primarily from **aggregated disease-level resources** (peer-reviewed reviews, registry-based cohorts, meta-analyses, and trial registries) rather than individual EHR case series (bensink2024kidneyfailureattributed pages 1-2, elnaga2024safetyandefficacy pages 1-2, mirioglu2024managementofadult pages 2-3).


---

## 2. Etiology

### 2.1 Primary causes (etiologic categories)
Recent reviews explicitly recommend an etiology-based framework:
- **Primary FSGS**: typically conceptualized as immune-mediated and/or driven by circulating permeability factors, presenting with abrupt nephrotic syndrome and diffuse foot process effacement (cos2023noveltreatmentparadigms pages 1-2, salfi2023currentunderstandingof pages 1-2).
- **Genetic FSGS**: monogenic podocyte/GBM disorders with variable presentations; often steroid-resistant (cos2023noveltreatmentparadigms pages 1-2, salfi2023currentunderstandingof pages 4-5).
- **Secondary FSGS**: maladaptive (e.g., hyperfiltration) or associated with drugs/infections; secondary forms may show glomerulomegaly in contexts such as obesity, reflux nephropathy, and low birth weight (cos2023noveltreatmentparadigms pages 1-2).
- **FSGS of undetermined cause (FSGS-UC)**: diagnosis when data are insufficient for classification; immunosuppression is discouraged in non-nephrotic presentations (mirioglu2024managementofadult pages 2-3).

The KDIGO-aligned classification and initial treatment branching are summarized visually in a figure from de Cos et al. (2023) (cos2023noveltreatmentparadigms media ecc573cd).

### 2.2 Risk factors
- **Demographic risk:** higher incidence is reported in **adult males** and **Black individuals** in a 2023 immunology-focused review (salfi2023currentunderstandingof pages 1-2).
- **Progression risk factors (clinical):** high-grade proteinuria, impaired kidney function, presence of FSGS lesions on biopsy, and interstitial fibrosis/tubular atrophy are associated with progression (mirioglu2024managementofadult pages 2-3).

### 2.3 Protective factors
- No specific genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
- The retrieved evidence strongly supports ancestry-linked genetic risk for APOL1 (see Genetics), but does not provide a mechanistically explicit gene–environment interaction model for FSGS beyond this population/ancestry association.


---

## 3. Phenotypes

### 3.1 Core clinical phenotypes and diagnostic features
**Common phenotype cluster (nephrotic syndrome spectrum):**
- **Proteinuria / nephrotic-range proteinuria** and **nephrotic syndrome** are central clinical manifestations; primary FSGS often presents with *abrupt marked proteinuria and overt nephrotic syndrome* (cos2023noveltreatmentparadigms pages 1-2, salfi2023currentunderstandingof pages 1-2).
- FSGS exhibits the **lowest glucocorticoid response** among idiopathic nephrotic syndrome forms; steroid resistance is commonly reported (salfi2023currentunderstandingof pages 1-2).

**Biopsy and pathology phenotypes:**
- Light microscopy: focal/segmental glomerular scarring is required for diagnosis (cos2023noveltreatmentparadigms pages 1-2, bensink2024kidneyfailureattributed pages 1-2).
- Electron microscopy: **foot process effacement (FPE) extent** helps distinguish etiologies; one study summarized in a 2024 ERA working group review reported **primary FSGS had FPE >80%**, whereas **genetic/maladaptive forms had no cases with FPE >50%** (mirioglu2024managementofadult pages 2-3).
- Immunofluorescence: may show **non-specific IgM/C3** staining in sclerotic areas (mirioglu2024managementofadult pages 2-3).

### 3.2 Phenotype characteristics (onset, severity, progression)
- Course is often chronic and progressive in non-remitting disease; in adult FSGS cohorts, “Over half of the patients with nephrotic-range proteinuria progress to ESKD” (mirioglu2024managementofadult pages 2-3).

### 3.3 Frequencies / statistics (recent)
- Steroid resistance in FSGS: reported **26–80%** across studies (salfi2023currentunderstandingof pages 1-2); ERA review summarizes steroid resistance in FSGS as **40–60%** (mirioglu2024managementofadult pages 2-3).
- Remission/relapse: ERA review summarizes **47–66%** remission and **25–36%** relapse among those who remit (mirioglu2024managementofadult pages 2-3).

### 3.4 Suggested HPO terms (non-exhaustive, evidence-aligned)
(These are ontology suggestions; exact IDs should be validated against HPO.)
- Nephrotic syndrome (cos2023noveltreatmentparadigms pages 1-2)
- Proteinuria / Nephrotic-range proteinuria (cos2023noveltreatmentparadigms pages 1-2)
- Podocyte foot process effacement (cos2023noveltreatmentparadigms pages 1-2, mirioglu2024managementofadult pages 2-3)
- Segmental glomerulosclerosis (cos2023noveltreatmentparadigms pages 1-2, bensink2024kidneyfailureattributed pages 1-2)
- Glomerulomegaly (secondary forms) (cos2023noveltreatmentparadigms pages 1-2)
- Steroid resistance (cos2023noveltreatmentparadigms pages 1-2, salfi2023currentunderstandingof pages 1-2)
- Progression to end-stage kidney disease (ESKD) (mirioglu2024managementofadult pages 2-3)

### 3.5 Quality of life impact
- Direct quality-of-life instrument results (e.g., SF-36, EQ-5D) were not present in retrieved evidence.


---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and genetic architecture
- Multiple recent sources emphasize genetic heterogeneity:
  - “Over 50 genes are currently known to be involved in FSGS” (xie2024precisionmedicinefor pages 1-3).
  - Monogenic causes account for roughly **20–30%** of SRNS/FSGS, with detection decreasing with older age of onset; adult genetic diagnosis rates of ~**11–21.3%** are summarized in the 2023 review (salfi2023currentunderstandingof pages 4-5).
  - A 2024 precision-medicine review reports WES detection of pathogenic variants in **26.2% of 187 SRNS patients** (xie2024precisionmedicinefor pages 1-3).

**Key genes highlighted (examples):**
- AR/early-onset genes: **NPHS1, NPHS2, PLCE1, TTC21B** (xie2024precisionmedicinefor pages 1-3).
- Additional genes frequently observed in cohorts: **WT1, NPHS1/NPHS2** (PodoNet); adult genetic FSGS includes **COL4A3–5** (reported as most common single-gene pathogenic mutation) and **INF2** (xie2024precisionmedicinefor pages 1-3).
- The immunology-focused 2023 review enumerates important adult/familial genes including **INF2, ACTN4, TRPC6, PAX2**, and core nephrotic syndrome genes **NPHS1/NPHS2/WT1** (salfi2023currentunderstandingof pages 4-5).

### 4.2 Population differences and APOL1
- APOL1 risk variants in people with recent African ancestry are repeatedly highlighted as major contributors to susceptibility and epidemiology (salfi2023currentunderstandingof pages 4-5).

### 4.3 Open Targets disease–gene associations (translation-focused)
Open Targets returned high-confidence FSGS associations for multiple genes, including **APOL1, TRPC6, INF2, ACTN4, NPHS1, NPHS2, PAX2, CD2AP, MYO1E, CRB2, ANLN, LMX1B**, with supporting evidence rows including genetics and curated sources (OpenTargets Search: Focal segmental glomerulosclerosis).

### 4.4 Variant-level details
- Specific pathogenic variant nomenclature and allele frequencies (gnomAD/ExAC) were not present in retrieved evidence and therefore are not asserted here.

### 4.5 Modifier genes, epigenetics, chromosomal abnormalities
- Not available in the retrieved evidence.


---

## 5. Environmental Information
- Secondary FSGS mechanisms include maladaptive states (e.g., obesity-related hyperfiltration) and secondary causes such as low birth weight and reflux nephropathy-associated glomerulomegaly (cos2023noveltreatmentparadigms pages 1-2).
- Specific toxin/occupational risk factors and explicit infectious triggers were not detailed in the retrieved 2023–2024 evidence excerpts.


---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
A consistent mechanistic chain across reviews is:
1) **Upstream trigger** (immune/circulating factor, genetic defect, maladaptive hyperfiltration, etc.) →
2) **Podocyte injury and foot process effacement** →
3) **Proteinuria** →
4) **Podocyte depletion and progressive scarring** →
5) Declining GFR and potential progression to **ESKD** (salfi2023currentunderstandingof pages 1-2, cos2023noveltreatmentparadigms pages 1-2).

### 6.2 Immune involvement and circulating factors (primary FSGS)
- The 2023 review states “a growing body of evidence emphasizes the pivotal role of the immune system” and notes that T cells, B cells, and complement have been implicated as crucial actors, with various molecules proposed as “circulating factors” contributing to disease and post-transplant recurrence (salfi2023currentunderstandingof pages 1-2).

### 6.3 Suggested ontology terms (for knowledge-base annotation)
**Cell types (CL suggestions):**
- Podocyte (inferred central cell type) (cos2023noveltreatmentparadigms pages 1-2, salfi2023currentunderstandingof pages 1-2)

**Biological process (GO suggestions):**
- Podocyte differentiation/maintenance; regulation of glomerular filtration; actin cytoskeleton organization; regulation of cell–substrate adhesion; inflammatory response; extracellular matrix organization; fibrotic process (mechanistic categories supported broadly by the reviews emphasizing podocyte injury and inflammation/fibrosis in FSGS) (salfi2023currentunderstandingof pages 1-2).

**Anatomy (UBERON suggestions):**
- Kidney; glomerulus; renal corpuscle; podocyte; glomerular basement membrane (cos2023noveltreatmentparadigms pages 1-2, salfi2023currentunderstandingof pages 1-2).


---

## 7. Anatomical Structures Affected
- Primary organ: **kidney**, specifically the **glomerulus** with podocyte injury and segmental glomerular scarring (cos2023noveltreatmentparadigms pages 1-2, bensink2024kidneyfailureattributed pages 1-2).
- The 2024 ERA update emphasizes tubulointerstitial fibrosis/tubular atrophy as prognostically relevant (mirioglu2024managementofadult pages 2-3).


---

## 8. Temporal Development
- Presentation may be abrupt in primary FSGS with sudden nephrotic syndrome (cos2023noveltreatmentparadigms pages 1-2).
- Progression: in patients with nephrotic-range proteinuria, “Over half… progress to ESKD” (mirioglu2024managementofadult pages 2-3).
- For kidney failure attributed to FSGS in USRDS, downstream kidney replacement pathways show prolonged morbidity (dialysis, transplant) (bensink2024kidneyfailureattributed pages 1-2).


---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent statistics)
- Pediatric vs adult nephrotic syndrome: FSGS ~**20% in children** and **40% in adults** (salfi2023currentunderstandingof pages 1-2).
- Incidence (review-level estimate): **0.2–2.5 per 100,000/year** (salfi2023currentunderstandingof pages 1-2).
- USRDS kidney failure attributable to FSGS (2008–2018): mean annual **prevalence 87.6/million** and **incidence 7.5/million**, with prevalence increasing from **76.5/million (2008)** to **96.0/million (2018)** (bensink2024kidneyfailureattributed pages 2-3).
- Demographic disparities in USRDS: highest prevalence in **Native Hawaiian/Pacific Islander 262.9/million** and **Black/African American 256.3/million**, and higher in males vs females (bensink2024kidneyfailureattributed pages 2-3).

### 9.2 Inheritance patterns
- Autosomal recessive early-onset forms (NPHS1/NPHS2/PLCE1/TTC21B) and autosomal dominant later-onset forms (COL4A3–5, INF2) are emphasized in the 2024 precision-medicine review (xie2024precisionmedicinefor pages 1-3).


---

## 10. Diagnostics

### 10.1 Clinical testing and biopsy
- Kidney biopsy remains foundational and is central to classification/prognosis in contemporary reviews (salfi2023currentunderstandingof pages 1-2, mirioglu2024managementofadult pages 2-3).
- The Columbia histologic lesion patterns do not reliably discriminate etiologies; therefore, clinical context + EM + genetics are required (mirioglu2024managementofadult pages 2-3).

### 10.2 Electron microscopy criterion supporting etiology
- Extent of FPE supports classification: **>80% FPE** supports primary FSGS, while **<50% FPE** is more typical for genetic/maladaptive forms (mirioglu2024managementofadult pages 2-3).

### 10.3 Genetic testing strategy
- Genetic testing is recommended when early onset, family history, extrarenal features, consanguinity, or early progression suggest a monogenic disorder; and in steroid-resistant presentations (mirioglu2024managementofadult pages 2-3, salfi2023currentunderstandingof pages 4-5).

### 10.4 Differential diagnosis
- FSGS is frequently considered along a spectrum with minimal change disease in idiopathic nephrotic syndrome; biopsy and response patterns help distinguish (salfi2023currentunderstandingof pages 1-2, mirioglu2024managementofadult pages 2-3).


---

## 11. Outcome / Prognosis
- Registry and review estimates converge on high progression risk:
  - “Over half of the patients with nephrotic-range proteinuria progress to ESKD” (mirioglu2024managementofadult pages 2-3).
  - In USRDS kidney failure attributable to FSGS, 7-year kidney survival is reported as **69%** (bensink2024kidneyfailureattributed pages 2-3).
- Response to therapy is prognostic: remission/relapse rates and steroid resistance rates are summarized in Section 3 (mirioglu2024managementofadult pages 2-3, salfi2023currentunderstandingof pages 1-2).


---

## 12. Treatment

A structured treatment summary (with MAXO and NCT mapping) is provided in the artifact table below.

| Therapy/Approach | MAXO term suggestion | Indication/Patient subgroup | Key evidence and quantitative outcomes | Key trial IDs (NCT) | Source (author year) | URL | Evidence type |
|---|---|---|---|---|---|---|---|
| Supportive care: RAAS blockade, blood-pressure control, salt restriction | MAXO: angiotensin receptor antagonist treatment; angiotensin-converting enzyme inhibitor treatment; blood pressure control; dietary sodium restriction | All FSGS categories as baseline care; especially supportive strategy for secondary and genetic FSGS | KDIGO-aligned supportive care includes RAAS blockade, BP control, and salt restriction; de Cos notes these as core background therapy for FSGS. Figure-based treatment algorithm shows RAAS blockade first, with etiology-specific escalation. No quantitative effect size for FSGS-specific remission provided in the gathered excerpt (cos2023noveltreatmentparadigms pages 1-2, cos2023noveltreatmentparadigms media ecc573cd) | — | de Cos 2023 | https://doi.org/10.1016/j.ekir.2022.10.004 | Review/guideline summary |
| SGLT2 inhibitors as adjunct supportive therapy | MAXO: sodium-glucose cotransporter 2 inhibitor treatment | Proteinuric FSGS as adjunct supportive care; not established as disease-specific immunologic therapy | Discussed as supportive option in FSGS; de Cos reports dapagliflozin showed non-significant benefit in the FSGS substudy. Endothelin-review notes concomitant SGLT2i may help optimize ERA safety, but no definitive FSGS-specific efficacy estimate is given in the extracted text (cos2023noveltreatmentparadigms pages 1-2, ma2025theroleof pages 8-9) | NCT02585804 (dapagliflozin trial listed in ClinicalTrials.gov search) (OpenTargets Search: Focal segmental glomerulosclerosis) | de Cos 2023; ClinicalTrials.gov search | https://doi.org/10.1016/j.ekir.2022.10.004 | Review; trial registry |
| High-dose glucocorticoids | MAXO: corticosteroid treatment | Presumed primary FSGS with nephrotic syndrome; first-line for immune-mediated/primary disease | KDIGO-referenced first-line therapy for primary FSGS. Mirioglu reports FSGS remission in 47–66% with 25–36% relapse and steroid resistance in 40–60%; Salfi reports steroid resistance across studies in 26–80%. Not recommended for non-nephrotic FSGS-UC/secondary forms (mirioglu2024managementofadult pages 2-3, salfi2023currentunderstandingof pages 1-2) | — | Mirioglu 2024; Salfi 2023 | https://doi.org/10.1093/ndt/gfae025; https://doi.org/10.3389/fimmu.2023.1247606 | Review/guideline update |
| Calcineurin inhibitors (cyclosporine, tacrolimus) | MAXO: calcineurin inhibitor treatment | Steroid-resistant primary FSGS; steroid-intolerant patients; generally not for clear genetic/secondary disease unless another indication | Salfi states evidence most strongly supports CNIs for steroid-resistant primary FSGS for at least 6 months. de Cos lists CNIs as KDIGO-recommended for steroid-resistant or steroid-intolerant primary disease. No pooled remission percentage for CNIs alone was extracted from the gathered text (salfi2023currentunderstandingof pages 1-2, cos2023noveltreatmentparadigms pages 1-2) | — | Salfi 2023; de Cos 2023 | https://doi.org/10.3389/fimmu.2023.1247606; https://doi.org/10.1016/j.ekir.2022.10.004 | Review/guideline summary |
| Sparsentan vs irbesartan (pooled RCT evidence) | MAXO: endothelin receptor antagonist treatment; angiotensin II receptor antagonist treatment | Proteinuric FSGS, including primary FSGS populations enrolled in DUET/DUPLEX | Meta-analysis of randomized trials: greater UP/C reduction with sparsentan (ratio of percentage reduction 0.66, 95% CI 0.58–0.74, P<0.001); complete remission RR 2.57 (95% CI 1.73–3.81); partial remission RR 1.63 (95% CI 1.40–1.91); no significant eGFR difference (MD 1.98 mL/min/1.73 m2, 95% CI -1.05 to 5.01); hypotension increased (RR 2.02, 95% CI 1.30–3.16) (elnaga2024safetyandefficacy pages 1-2) | NCT01613118; NCT03493685 (OpenTargets Search: Focal segmental glomerulosclerosis) | Elnaga 2024 | https://doi.org/10.1186/s12882-024-03713-9 | Meta-analysis |
| Sparsentan DUET phase 2 + open-label extension | MAXO: proteinuria-reducing therapy; endothelin receptor antagonist treatment; angiotensin II receptor antagonist treatment | FSGS with UP/C ≥1.0 g/g and eGFR >30 mL/min/1.73 m2; long-term treatment follow-up | DUET/OLE analysis: 108 patients received sparsentan; median follow-up 47.0 months; 46/108 (43%) achieved at least one complete remission (UP/C ≤0.3 g/g), and 61% of complete remissions occurred within 12 months. OLE report: 52.8% achieved FSGS partial remission within 9 months; remission associated with slower eGFR decline vs nonresponders (overall slope -2.70 vs -6.56 mL/min/1.73 m2/year, P=0.03; first 2 years -1.69 vs -6.46, P=0.03). Common TEAEs included headache, peripheral edema, URI, hyperkalemia, hypotension; no heart failure events or deaths reported (trachtman2023implicationsofcomplete pages 1-2, campbell2024sparsentanforfocal pages 1-2) | NCT01613118 (OpenTargets Search: Focal segmental glomerulosclerosis) | Trachtman 2023; Campbell 2024 | https://doi.org/10.1016/j.ekir.2023.07.022; https://doi.org/10.1016/j.xkme.2024.100833 | Phase 2 RCT extension / open-label follow-up |
| Sparsentan DUPLEX phase 3 | MAXO: endothelin receptor antagonist treatment; angiotensin II receptor antagonist treatment | Primary FSGS / proteinuric FSGS enrolled in pivotal phase 3 study | Extracted review summary reports DUPLEX randomized sparsentan 800 mg vs irbesartan 300 mg over 108 weeks in 371 participants; partial remission endpoint favored sparsentan (UPCR ≤1.5 g/g and >40% reduction; p=0.0094). Review/meta-analysis materials note strong antiproteinuric effect; detailed AE frequencies not fully extracted from the gathered snippet (rakotoarison2024endothelininhibitorsin pages 8-9, ma2025theroleof pages 8-9) | NCT03493685 (OpenTargets Search: Focal segmental glomerulosclerosis) | Rakotoarison 2024; Ma 2025 review of trial | https://doi.org/10.3390/jcm13206056; https://doi.org/10.1080/0886022x.2025.2465810 | Phase 3 RCT summary / review |
| Immunosuppression avoidance in non-primary disease | MAXO: avoidance of immunosuppressive therapy; supportive care | FSGS of undetermined cause without nephrotic syndrome, and many genetic/secondary forms | ERA Immunonephrology review emphasizes unmet need to identify who should receive immunosuppression vs supportive care; immunosuppression is generally reserved for presumed primary FSGS, and patients with FSGS-UC without nephrotic syndrome should not receive immunosuppression (mirioglu2024managementofadult pages 2-3) | — | Mirioglu 2024 | https://doi.org/10.1093/ndt/gfae025 | Review/guideline update |
| Genetic testing / precision medicine | MAXO: genetic testing; precision medicine approach | Suspected monogenic FSGS, steroid-resistant disease, unclear etiology, biopsy-contraindicated/high-risk settings | de Cos and Mirioglu recommend integrating genetic testing into diagnosis/classification; genetic testing is especially recommended when steroid resistance suggests a genetic form. Precision-medicine review highlights clinical significance of next-generation sequencing and biomarker-guided stratification to avoid unnecessary immunosuppression, but no diagnostic yield percentage was present in extracted snippets (mirioglu2024managementofadult pages 2-3, salfi2023currentunderstandingof pages 1-2, cos2023noveltreatmentparadigms pages 1-2) | — | Mirioglu 2024; Salfi 2023; de Cos 2023 | https://doi.org/10.1093/ndt/gfae025; https://doi.org/10.3389/fimmu.2023.1247606; https://doi.org/10.1016/j.ekir.2022.10.004 | Review / precision-medicine framework |
| Rituximab / other targeted or adjunct therapies under study | MAXO: anti-CD20 monoclonal antibody treatment; B-cell depletion therapy | Selected relapsing/refractory podocytopathies; role in primary FSGS remains less established than in MCD | Mirioglu notes rituximab is highlighted particularly for MCD and discusses ongoing trials in podocytopathies; clinical trial registry search identified FSGS-focused rituximab and abatacept studies, but gathered evidence did not provide robust 2023–2024 quantitative efficacy estimates for routine FSGS use (mirioglu2024managementofadult pages 2-3, OpenTargets Search: Focal segmental glomerulosclerosis) | NCT00550342; NCT01573533; NCT00981838; NCT04369183; NCT02592798 (OpenTargets Search: Focal segmental glomerulosclerosis) | Mirioglu 2024; ClinicalTrials.gov search | https://doi.org/10.1093/ndt/gfae025 | Review; trial registry |
| Real-world implementation / care burden in kidney failure attributed to FSGS | MAXO: kidney replacement therapy; kidney transplantation; hemodialysis | Advanced FSGS progressing to kidney failure | USRDS cohort: 72.1% initiated in-center hemodialysis; 7.3% had an initial transplant; transplant rates were 15% at 1 year and 34% at 5 years; about one-third died during follow-up. These data reflect real-world downstream management burden rather than disease-modifying therapy efficacy (bensink2024kidneyfailureattributed pages 1-2) | — | Bensink 2024 | https://doi.org/10.1016/j.xkme.2023.100760 | Registry/observational |


*Table: This table summarizes current FSGS treatment approaches, emphasizing 2023-2024 evidence, patient subgroups, quantitative outcomes, and implementation details. It is useful for mapping supportive care, immunosuppression, sparsentan trial data, and precision-medicine strategies to a knowledge base.*

### 12.1 Sparsentan (dual endothelin–angiotensin receptor antagonist)
- **Efficacy (2024 meta-analysis):** sparsentan improved proteinuria compared with irbesartan (ratio of percentage reduction **0.66**, 95% CI 0.58–0.74) and increased complete and partial remission probabilities (CR RR **2.57**; PR RR **1.63**). Kidney function effects were not significantly different in pooled eGFR change (MD **1.98 mL/min/1.73m²**, P=0.20), and hypotension was more frequent (RR **2.02**) (elnaga2024safetyandefficacy pages 1-2).
- **Long-term extension (DUET OLE):** partial remission achieved by **52.8% within 9 months**, with slower eGFR decline in responders (overall slope −2.70 vs −6.56 mL/min/1.73m²/year; P=0.03) and no heart failure events or deaths reported (campbell2024sparsentanforfocal pages 1-2).

### 12.2 Immunosuppression and supportive care selection
- High-dose glucocorticoids are standard first-line for presumed primary FSGS, with CNIs for steroid-resistant or intolerant patients; immunosuppression is not recommended for FSGS-UC without nephrotic syndrome (cos2023noveltreatmentparadigms pages 1-2, mirioglu2024managementofadult pages 2-3).

### 12.3 Real-world implementation downstream
- USRDS kidney failure attributable to FSGS: 72.1% started in-center hemodialysis; 7.3% had an initial transplant; transplant rates 15% at 1 year and 34% at 5 years (bensink2024kidneyfailureattributed pages 1-2).


---

## 13. Prevention
- Primary prevention strategies are not well-defined for primary FSGS; secondary prevention focuses on early detection of proteinuria and implementation of renoprotective strategies (RAAS blockade, BP control). Specific guideline-grade prevention programs were not present in retrieved evidence.


---

## 14. Other Species / Natural Disease
- Not available in the retrieved evidence.


---

## 15. Model Organisms
- Specific model-organism details were not extracted from the 2023–2024 evidence presented here.


---

## Key Epidemiology & Prognosis Snapshot (2023–2024)
The following table consolidates identifiers and key statistics (registry + recent reviews).

| Category | Data | Source (first author year) | PMID | URL | Evidence type |
|---|---|---|---|---|---|
| Identifiers/Synonyms | FSGS = focal segmental glomerulosclerosis; described as a **histologic pattern of glomerular injury** / **podocytopathy**, not a single disease entity; classified into **primary, genetic, secondary, and FSGS of undetermined cause** (cos2023noveltreatmentparadigms pages 1-2, mirioglu2024managementofadult pages 2-3) | de Cos 2023; Mirioglu 2024 |  | https://doi.org/10.1016/j.ekir.2022.10.004; https://doi.org/10.1093/ndt/gfae025 | Review |
| Identifiers/Synonyms | Histologic lesion defined by **segmental sclerosis in some glomeruli** with variable podocyte foot-process effacement on EM; primary FSGS often presents with abrupt nephrotic syndrome (cos2023noveltreatmentparadigms pages 1-2) | de Cos 2023 |  | https://doi.org/10.1016/j.ekir.2022.10.004 | Review |
| Epidemiology | FSGS accounts for about **20% of nephrotic syndrome in children** and **40% in adults**; annual incidence estimated **0.2–2.5 per 100,000** (salfi2023currentunderstandingof pages 1-2) | Salfi 2023 |  | https://doi.org/10.3389/fimmu.2023.1247606 | Review |
| Epidemiology | In the USRDS 2008–2018 cohort, mean annual **prevalence of FSGS-attributed kidney failure** was **87.6 per 1,000,000 US persons** and **incidence** was **7.5 per 1,000,000**; prevalence rose from **76.5/million (2008)** to **96.0/million (2018)** (bensink2024kidneyfailureattributed pages 1-2, bensink2024kidneyfailureattributed pages 2-3) | Bensink 2024 |  | https://doi.org/10.1016/j.xkme.2023.100760 | Registry/retrospective cohort |
| Epidemiology | Historical U.S. incidence of FSGS (all disease, 2004–2013) reported as about **3.2 per 100,000 person-years**, a **41% increase** vs 1994–2003 (bensink2024kidneyfailureattributed pages 1-2) | Bensink 2024 |  | https://doi.org/10.1016/j.xkme.2023.100760 | Registry/retrospective cohort |
| Progression/Prognosis | “**Over half of the patients with nephrotic-range proteinuria progress to ESKD**” (mirioglu2024managementofadult pages 2-3) | Mirioglu 2024 |  | https://doi.org/10.1093/ndt/gfae025 | Review |
| Progression/Prognosis | FSGS remission rates: **47–66%** remit; among those, **25–36% relapse**; steroid resistance encountered in **40–60%** of patients (mirioglu2024managementofadult pages 2-3) | Mirioglu 2024 |  | https://doi.org/10.1093/ndt/gfae025 | Review |
| Progression/Prognosis | Across studies, steroid resistance reported in **26–80%** of patients; adults respond less favorably than children, and **<50%** of initially steroid-sensitive patients maintain stable remission (salfi2023currentunderstandingof pages 1-2) | Salfi 2023 |  | https://doi.org/10.3389/fimmu.2023.1247606 | Review |
| Progression/Prognosis | In USRDS, **7-year kidney survival** for FSGS was **69%** (vs 88% membranous nephropathy; 82% IgA nephropathy); **>50%** progress to kidney failure within **5–10 years** (bensink2024kidneyfailureattributed pages 2-3) | Bensink 2024 |  | https://doi.org/10.1016/j.xkme.2023.100760 | Registry/retrospective cohort |
| Transplant recurrence | Small series: anti-nephrin antibodies identified in **11/14 (79%)** patients with recurrence of primary FSGS after kidney transplantation (mirioglu2024managementofadult pages 2-3) | Mirioglu 2024 |  | https://doi.org/10.1093/ndt/gfae025 | Review |
| Demographics | Incidence/prevalence are higher in **male adults** and **Black individuals** (salfi2023currentunderstandingof pages 1-2) | Salfi 2023 |  | https://doi.org/10.3389/fimmu.2023.1247606 | Review |
| Demographics | USRDS prevalence lower in **children <18 y: 31.4/million** vs **adults ≥18 y: 104.9/million**; higher in **males 108.0/million** vs **females 67.9/million** (bensink2024kidneyfailureattributed pages 2-3) | Bensink 2024 |  | https://doi.org/10.1016/j.xkme.2023.100760 | Registry/retrospective cohort |
| Demographics | Highest prevalence of FSGS-attributed kidney failure in **Native Hawaiian/Pacific Islander: 262.9/million** and **Black/African American: 256.3/million** groups (bensink2024kidneyfailureattributed pages 2-3) | Bensink 2024 |  | https://doi.org/10.1016/j.xkme.2023.100760 | Registry/retrospective cohort |


*Table: This table summarizes how recent 2023-2024 sources define and classify FSGS and compiles key epidemiology, prognosis, recurrence, and demographic statistics directly from the available evidence snippets.*


---

## Visual Evidence: Classification and Treatment Algorithm
A KDIGO-aligned classification and management flow is available as a figure from de Cos et al. 2023 (cos2023noveltreatmentparadigms media ecc573cd).


---

## Direct abstract-supported statements (quotes)
The following direct statements come from abstracts of retrieved peer-reviewed papers:
- “The pathogenetic mechanisms underlying the onset and the post-transplant recurrence of primary focal segmental glomerulosclerosis (FSGS) are complex and remain yet to be fully elucidated. However, a growing body of evidence emphasizes the pivotal role of the immune system…” (Frontiers in Immunology, 2023-09) (salfi2023currentunderstandingof pages 1-2).
- “Kidney biopsy remains central to diagnosis…” in the ERA Immunonephrology Working Group update on podocytopathies (Nephrology Dialysis Transplantation, 2024-02) (mirioglu2024managementofadult pages 2-3).
- In the sparsentan meta-analysis abstract: “Sparsentan was superior to irbesartan in improving urine protein to creatinine ratio…” and hypotension was higher (BMC Nephrology, 2024-09) (elnaga2024safetyandefficacy pages 1-2).


---

## Limitations / Evidence Gaps for Knowledge Base Completion
- ICD-10/ICD-11, MeSH, OMIM, and Orphanet identifiers were not available in retrieved texts; additional ontology lookups are needed.
- Variant-level details (HGVS nomenclature, allele frequency in gnomAD), epigenetic mechanisms, and quality-of-life instrument results were not present in the retrieved evidence.
- Environmental/toxin and infectious triggers for secondary FSGS were only partially represented in retrieved excerpts.



References

1. (cos2023noveltreatmentparadigms pages 1-2): Marina de Cos, Kristin Meliambro, and Kirk N. Campbell. Novel treatment paradigms: focal segmental glomerulosclerosis. Kidney International Reports, 8:30-35, Jan 2023. URL: https://doi.org/10.1016/j.ekir.2022.10.004, doi:10.1016/j.ekir.2022.10.004. This article has 41 citations and is from a peer-reviewed journal.

2. (salfi2023currentunderstandingof pages 1-2): Giuseppe Salfi, Federica Casiraghi, and Giuseppe Remuzzi. Current understanding of the molecular mechanisms of circulating permeability factor in focal segmental glomerulosclerosis. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1247606, doi:10.3389/fimmu.2023.1247606. This article has 45 citations and is from a peer-reviewed journal.

3. (mirioglu2024managementofadult pages 2-3): Safak Mirioglu, Lisa Daniel-Fischer, Ilay Berke, Syed Hasan Ahmad, Ingeborg M Bajema, Annette Bruchfeld, Gema M Fernandez-Juarez, Jürgen Floege, Eleni Frangou, Dimitrios Goumenos, Megan Griffith, Sarah M Moran, Cees van Kooten, Stefanie Steiger, Kate I Stevens, Kultigin Turkmen, Lisa C Willcocks, and Andreas Kronbichler. Management of adult patients with podocytopathies: an update from the era immunonephrology working group. Nephrology Dialysis Transplantation, 39:569-580, Feb 2024. URL: https://doi.org/10.1093/ndt/gfae025, doi:10.1093/ndt/gfae025. This article has 33 citations and is from a domain leading peer-reviewed journal.

4. (OpenTargets Search: Focal segmental glomerulosclerosis): Open Targets Query (Focal segmental glomerulosclerosis, 19 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (bensink2024kidneyfailureattributed pages 1-2): Mark E. Bensink, Deborah Goldschmidt, Zheng-Yi Zhou, Kaijun Wang, Richard Lieblich, and C. Martin Bunke. Kidney failure attributed to focal segmental glomerulosclerosis: a usrds retrospective cohort study of epidemiology, treatment modalities, and economic burden. Kidney Medicine, 6:100760, Feb 2024. URL: https://doi.org/10.1016/j.xkme.2023.100760, doi:10.1016/j.xkme.2023.100760. This article has 11 citations.

6. (elnaga2024safetyandefficacy pages 1-2): Ahmed A. Abo Elnaga, Mohamed A. Alsaied, Abdelrahman M. Elettreby, Alaa Ramadan, Mohamed Abouzid, Raghda Shetta, and Yazan A. Al-Ajlouni. Safety and efficacy of sparsentan versus irbesartan in focal segmental glomerulosclerosis and iga nephropathy: a systematic review and meta-analysis of randomized controlled trials. BMC Nephrology, Sep 2024. URL: https://doi.org/10.1186/s12882-024-03713-9, doi:10.1186/s12882-024-03713-9. This article has 4 citations and is from a peer-reviewed journal.

7. (salfi2023currentunderstandingof pages 4-5): Giuseppe Salfi, Federica Casiraghi, and Giuseppe Remuzzi. Current understanding of the molecular mechanisms of circulating permeability factor in focal segmental glomerulosclerosis. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1247606, doi:10.3389/fimmu.2023.1247606. This article has 45 citations and is from a peer-reviewed journal.

8. (cos2023noveltreatmentparadigms media ecc573cd): Marina de Cos, Kristin Meliambro, and Kirk N. Campbell. Novel treatment paradigms: focal segmental glomerulosclerosis. Kidney International Reports, 8:30-35, Jan 2023. URL: https://doi.org/10.1016/j.ekir.2022.10.004, doi:10.1016/j.ekir.2022.10.004. This article has 41 citations and is from a peer-reviewed journal.

9. (xie2024precisionmedicinefor pages 1-3): Yi Xie and Fei Liu. Precision medicine for focal segmental glomerulosclerosis. Kidney Research and Clinical Practice, 43:709-723, Nov 2024. URL: https://doi.org/10.23876/j.krcp.23.227, doi:10.23876/j.krcp.23.227. This article has 3 citations.

10. (bensink2024kidneyfailureattributed pages 2-3): Mark E. Bensink, Deborah Goldschmidt, Zheng-Yi Zhou, Kaijun Wang, Richard Lieblich, and C. Martin Bunke. Kidney failure attributed to focal segmental glomerulosclerosis: a usrds retrospective cohort study of epidemiology, treatment modalities, and economic burden. Kidney Medicine, 6:100760, Feb 2024. URL: https://doi.org/10.1016/j.xkme.2023.100760, doi:10.1016/j.xkme.2023.100760. This article has 11 citations.

11. (ma2025theroleof pages 8-9): Xiaoting Ma, Yuyang Liang, Wenmin Chen, Lingqian Zheng, Haishan Lin, and Tianbiao Zhou. The role of endothelin receptor antagonists in kidney disease. Renal Failure, Feb 2025. URL: https://doi.org/10.1080/0886022x.2025.2465810, doi:10.1080/0886022x.2025.2465810. This article has 13 citations and is from a peer-reviewed journal.

12. (trachtman2023implicationsofcomplete pages 1-2): Howard Trachtman, Ulysses Diva, Edward Murphy, Kaijun Wang, Jula Inrig, and Radko Komers. Implications of complete proteinuria remission at any time in focal segmental glomerulosclerosis: sparsentan duet trial. Kidney International Reports, 8:2017-2028, Oct 2023. URL: https://doi.org/10.1016/j.ekir.2023.07.022, doi:10.1016/j.ekir.2023.07.022. This article has 13 citations and is from a peer-reviewed journal.

13. (campbell2024sparsentanforfocal pages 1-2): Kirk N. Campbell, Loreto Gesualdo, Edward Murphy, Michelle N. Rheault, Tarak Srivastava, Vladimir Tesar, Radko Komers, and Howard Trachtman. Sparsentan for focal segmental glomerulosclerosis in the duet open-label extension: long-term efficacy and safety. Kidney Medicine, 6:100833, Jun 2024. URL: https://doi.org/10.1016/j.xkme.2024.100833, doi:10.1016/j.xkme.2024.100833. This article has 14 citations.

14. (rakotoarison2024endothelininhibitorsin pages 8-9): Agata Rakotoarison, Marta Kepinska, Andrzej Konieczny, Karolina Władyczak, Dariusz Janczak, Agnieszka Hałoń, Piotr Donizy, and Mirosław Banasik. Endothelin inhibitors in chronic kidney disease: new treatment prospects. Journal of Clinical Medicine, 13:6056, Oct 2024. URL: https://doi.org/10.3390/jcm13206056, doi:10.3390/jcm13206056. This article has 15 citations.
