---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T21:33:28.322593'
end_time: '2026-04-05T21:44:51.214168'
duration_seconds: 682.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pheochromocytoma and Paraganglioma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pheochromocytoma and Paraganglioma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Pheochromocytoma and Paraganglioma** covering all of the
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
- **Disease Name:** Pheochromocytoma and Paraganglioma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Pheochromocytoma and Paraganglioma** covering all of the
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


# Comprehensive Disease Characteristics Report: Pheochromocytoma and Paraganglioma (PPGL)

## Target Disease
- **Disease name:** Pheochromocytoma and Paraganglioma (PPGL)
- **MONDO ID:** *Not retrieved from MONDO within the available tool context; should be added from MONDO/EMBL-EBI OLS in downstream curation.*
- **Category:** Rare neuroendocrine tumors (neural crest/chromaffin-cell derived), endocrine oncology

## Executive overview (current understanding)
Pheochromocytomas (PCCs) and paragangliomas (PGLs) are neuroendocrine tumors of neural crest origin that arise from chromaffin/paraganglionic tissue distributed from the skull base to the pelvic floor. PCCs arise in the adrenal medulla, while PGLs arise from extra-adrenal sympathetic or parasympathetic paraganglia. Sympathetic tumors are more often catecholamine-secreting; parasympathetic head-and-neck PGLs are often nonfunctional or dopamine-predominant. Contemporary WHO framing treats all PPGLs as malignant neoplasms with **variable metastatic potential**, and histology alone cannot reliably predict metastasis. (bresser2024themolecularclassification pages 1-2, t.2024pheochromocytomaanupdated pages 1-2)

| Topic | Key PPGL fact | Key examples/details | Main recent source(s) with year and URL | Evidence citation |
|---|---|---|---|---|
| Definition and origin | PPGL comprises pheochromocytomas (adrenal medulla) and paragangliomas (extra-adrenal paraganglia), neuroendocrine tumors of neural crest/chromaffin origin. | PCC usually arises in adrenal medulla; PGL arises from sympathetic or parasympathetic paraganglia distributed from skull base to pelvic floor. | de Bresser & de Krijger, 2024, *Endocrine Pathology*, https://doi.org/10.1007/s12022-024-09830-3; Giacché et al., 2024, *Biomedicines*, https://doi.org/10.3390/biomedicines12102385; Saavedra T. et al., 2024, *Frontiers in Endocrinology*, https://doi.org/10.3389/fendo.2024.1433582 | (bresser2024themolecularclassification pages 1-2, t.2024pheochromocytomaanupdated pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2) |
| Major anatomic sites | Sympathetic and parasympathetic sites differ in location and behavior. | Sympathetic: adrenal medulla, retroperitoneum, organ of Zuckerkandl, bladder, mediastinum; parasympathetic: head and neck/carotid body, vagal, jugulotympanic, other skull-base to cervical sites. | de Bresser & de Krijger, 2024, https://doi.org/10.1007/s12022-024-09830-3; Giacché et al., 2024, https://doi.org/10.3390/biomedicines12102385 | (bresser2024themolecularclassification pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2) |
| Functional vs nonfunctional biology | Sympathetic PCC/PGL are more often catecholamine-secreting; parasympathetic head-and-neck PGLs are usually nonfunctional or dopamine-predominant. | Catecholamines/metabolites relevant to diagnosis include metanephrine, normetanephrine, and 3-methoxytyramine. | de Bresser & de Krijger, 2024, https://doi.org/10.1007/s12022-024-09830-3; Giacché et al., 2024, https://doi.org/10.3390/biomedicines12102385; Bima et al., 2024, *Frontiers in Endocrinology*, https://doi.org/10.3389/fendo.2024.1460320 | (bresser2024themolecularclassification pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2, bima2024preventionandmanagement pages 4-5) |
| WHO 2022 classification concept | Modern classification treats all PPGLs as neoplasms with variable metastatic potential rather than benign vs malignant categories. | Histology alone cannot reliably predict which tumors will metastasize; metastatic risk varies by genotype, site, size, and other factors. | de Bresser & de Krijger, 2024, https://doi.org/10.1007/s12022-024-09830-3; Saavedra T. et al., 2024, https://doi.org/10.3389/fendo.2024.1433582 | (bresser2024themolecularclassification pages 1-2, t.2024pheochromocytomaanupdated pages 1-2) |
| Hereditary fraction | PPGL is among the most heritable tumor types. | Germline predisposition is reported in ~30–40% overall; some recent reviews cite ~40–50%; pediatric hereditary proportion is higher (~70–80%). | Giacché et al., 2024, https://doi.org/10.3390/biomedicines12102385; Saavedra T. et al., 2024, https://doi.org/10.3389/fendo.2024.1433582; Bima et al., 2024, https://doi.org/10.3389/fendo.2024.1460320; Richter & Bechmann, 2024, *Journal of the Endocrine Society*, https://doi.org/10.1210/jendso/bvae038 | (giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2, bima2024preventionandmanagement pages 4-5, richter2024patientsexand pages 1-2, t.2024pheochromocytomaanupdated pages 1-2) |
| Main molecular clusters | Three principal molecular/transcriptomic clusters are consistently recognized. | Cluster 1 pseudohypoxia; Cluster 2 kinase signaling/neural identity; Cluster 3 Wnt signaling. Cluster 1 is often extra-adrenal/noradrenergic and more aggressive; Cluster 2 more often adrenal/adrenergic; Cluster 3 is less common and includes Wnt-related drivers. | Giacché et al., 2024, https://doi.org/10.3390/biomedicines12102385; Bima et al., 2024, https://doi.org/10.3389/fendo.2024.1460320; Richter & Bechmann, 2024, https://doi.org/10.1210/jendso/bvae038; de Bresser & de Krijger, 2024, https://doi.org/10.1007/s12022-024-09830-3 | (giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2, bima2024preventionandmanagement pages 4-5, giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, richter2024patientsexand pages 1-2) |
| Major susceptibility genes: Cluster 1 pseudohypoxia | Genes affecting Krebs cycle/hypoxia signaling dominate this cluster. | SDHA, SDHB, SDHC, SDHD, SDHAF2, VHL, FH, EPAS1/HIF2A, EGLN1/PHD, MDH2; some reviews also list IDH1, DLST, GOT2, SLC25A11. | Giacché et al., 2024, https://doi.org/10.3390/biomedicines12102385; Bima et al., 2024, https://doi.org/10.3389/fendo.2024.1460320; Richter & Bechmann, 2024, https://doi.org/10.1210/jendso/bvae038 | (bima2024preventionandmanagement pages 4-5, giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, richter2024patientsexand pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 9-10) |
| Major susceptibility genes: Cluster 2 kinase signaling | Kinase/RAS/MAPK and neural-identity signaling genes define this cluster. | RET, NF1, TMEM127, MAX, HRAS; some reviews also include FGFR1, MET, MERTK, BRAF. | Giacché et al., 2024, https://doi.org/10.3390/biomedicines12102385; Bima et al., 2024, https://doi.org/10.3389/fendo.2024.1460320; Richter & Bechmann, 2024, https://doi.org/10.1210/jendso/bvae038 | (bima2024preventionandmanagement pages 4-5, giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, richter2024patientsexand pages 1-2) |
| Major susceptibility genes: Cluster 3 Wnt signaling | Wnt-altered tumors are less common and mainly defined by somatic drivers. | MAML3 fusions and CSDE1 alterations are the canonical examples in recent classification schemes. | Giacché et al., 2024, https://doi.org/10.3390/biomedicines12102385; Bima et al., 2024, https://doi.org/10.3389/fendo.2024.1460320 | (bima2024preventionandmanagement pages 4-5, giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6) |
| Clinical stratification note | Sex and ancestry/origin may influence driver-gene distribution and presentation. | In one 2024 synthesis, males more often had hypoxia-pathway germline PVs, sympathetic PGL, and metastasis; European females more often had kinase-signaling drivers such as RET/TMEM127. | Richter & Bechmann, 2024, https://doi.org/10.1210/jendso/bvae038 | (richter2024patientsexand pages 1-2) |


*Table: This table summarizes core disease-level facts for pheochromocytoma and paraganglioma, including definition, sites, functionality, WHO classification concept, heritability, and molecular genetics. It is structured for direct reuse in a knowledge base and includes citation-ready evidence IDs plus recent source URLs.*

---

## 1. Disease information
### What is the disease?
- **Definition:** PPGL refers to **pheochromocytomas (adrenal medulla)** plus **paragangliomas (extra-adrenal paraganglia)**; these originate from neural-crest derived paraganglia/chromaffin cells. (bresser2024themolecularclassification pages 1-2, t.2024pheochromocytomaanupdated pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2)
- **Functional behavior:** Sympathetic PPGLs “often hypersecrete catecholamines,” while parasympathetic PGLs tend to be nonfunctional or dopamine-predominant; biochemical diagnosis commonly uses metanephrine, normetanephrine, and 3‑methoxytyramine. (bresser2024themolecularclassification pages 1-2)
- **WHO classification concept:** A recent endocrine pathology review notes that WHO redefined PPGLs “as malignant neoplasms with variable metastatic potential.” (bresser2024themolecularclassification pages 1-2)

### Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
- **Status:** Not extracted from OMIM/Orphanet/ICD/MeSH/MONDO within the current tool runs. This report therefore cannot provide authoritative identifier codes and should be supplemented by direct look-up in OMIM/Orphanet/ICD‑11/MeSH/MONDO. (No identifier sources were retrieved in the provided context.)

### Synonyms / alternative names
Commonly used terms include:
- *Pheochromocytoma (PCC)*, *paraganglioma (PGL)*, *PPGL*
- *Head and neck paraganglioma (HNPGL)* for parasympathetic PGLs in skull base/neck. (lin2022headandneck pages 1-2)

### Evidence provenance
- The information above is derived from **aggregated disease-level resources (peer-reviewed reviews and cohort studies)** rather than individual EHR extractions. (bresser2024themolecularclassification pages 1-2, t.2024pheochromocytomaanupdated pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2)

---

## 2. Etiology
### Disease causal factors
#### Genetic predisposition (dominant driver of etiology)
PPGL is among the most heritable human tumor types.
- A 2024 review states: “**germline mutation in susceptibility genes is detected in 40% of subjects**,” and ~10–12% of clinically sporadic presentations still carry germline mutations. (giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2)
- A 2024 pediatric-focused review summarizes **~40–50%** germline contribution overall and higher rates in children (reported **70–80%** hereditary; one study ~80%). (bima2024preventionandmanagement pages 4-5)
- A 2024 analysis of sex/ancestry effects notes that genetic drivers explain ~80% of PPGLs and that “**half of which are caused by germline pathogenic variants (PVs)** in… >20 susceptibility genes,” consistent with ~40% germline overall. (richter2024patientsexand pages 1-2)

**Major susceptibility genes** (examples repeatedly emphasized in recent reviews):
- **Cluster 1 (pseudohypoxia / Krebs cycle):** SDHA/SDHB/SDHC/SDHD/SDHAF2, VHL, FH, EPAS1(HIF2A), plus additional metabolic/hypoxia genes (e.g., MDH2; and in some classifications IDH1, DLST, GOT2, SLC25A11). (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, richter2024patientsexand pages 1-2)
- **Cluster 2 (kinase signaling):** RET, NF1, TMEM127, MAX, HRAS (and sometimes FGFR1/MET etc. in expanded schemas). (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, richter2024patientsexand pages 1-2)
- **Cluster 3 (Wnt-altered):** MAML3 fusions, CSDE1 (somatic drivers). (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6)

**Genotype–phenotype coupling (high-level):** A 2024 review summarizes that pseudo-hypoxic (cluster‑1) tumors tend toward extra-adrenal location and noradrenergic/dopaminergic biochemical profiles with greater aggressiveness, whereas kinase (cluster‑2) tumors more often are adrenal/adrenergic. (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6)

#### Environmental and lifestyle factors
- No strong, validated environmental causal factors were identified in the retrieved evidence set. PPGL is primarily genetically driven. (giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, richter2024patientsexand pages 1-2)

### Risk factors
- **Genetic:** germline pathogenic variants (e.g., SDHB confers high metastatic/recurrence risk). (araujocastro2023localrecurrenceand pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 12-14)
- **Clinical predictors of recurrence/metastasis (post-resection):** SDHB pathogenic variant, larger tumor size, and higher urinary normetanephrine were independent recurrence predictors in a Spanish multicenter series. (araujocastro2023localrecurrenceand pages 1-2)

### Protective factors
- No protective genetic variants or environmental protective factors were identified in the retrieved evidence set.

### Gene–environment interactions
- No gene–environment interaction studies were retrieved in the current evidence set.

---

## 3. Phenotypes
### Core symptom/sign spectrum (with frequencies when available)
Typical manifestations largely reflect catecholamine excess.
- A 2023 review states systemic arterial **hypertension occurs in ~90%** of cases and highlights the classic paroxysmal triad of “**headache, palpitations, and sweating**.” (junior2023thepheochromocytomaparagangliomasyndrome pages 1-2)
- A 2024 review provides pooled sensitivities: hypertension ~80.7%, palpitations ~59.3%, diaphoresis ~52.4%, and classic triad sensitivity ~58%. (giacche2024pheochromocytoma–paragangliomasyndromea pages 2-4)
- Hypertension pattern differs: sustained hypertension more common than paroxysmal in some series; one 2024 scoping review summarizes sustained hypertension ~50–55% and paroxysmal ~30–45%. (t.2024pheochromocytomaanupdated pages 3-6)

**Pediatric phenotype differences:** sustained hypertension is especially common in children (reported ~60–90%), and the classic triad is reported in up to 54% of affected children. (bima2024preventionandmanagement pages 2-4)

**Cardiovascular complications (high clinical importance):**
- Catecholamine-induced cardiomyopathy complicates ~8–10% of cases, and cardiovascular event rates in PPGL cohorts are reported at 19.3% and 28% in cited studies. (giacche2024pheochromocytoma–paragangliomasyndromea pages 4-5)

### Suggested HPO terms (examples)
(These are ontology mapping suggestions for knowledge-base use; not claims about frequency unless stated above.)
- Hypertension **HP:0000822**; Paroxysmal hypertension **HP:0004921**
- Headache **HP:0002315**
- Palpitations **HP:0001962**
- Diaphoresis **HP:0000972**
- Tachycardia **HP:0001649**; Arrhythmia **HP:0011675**
- Orthostatic hypotension **HP:0001278** (often coded as **HP:0001278** is incorrect; better: Orthostatic hypotension **HP:0001278** may be mismatched—curators should verify; suggestion only)
- Hyperglycemia **HP:0003074**; Diabetes mellitus **HP:0000819**
- Cardiomyopathy **HP:0001638**; Takotsubo cardiomyopathy (no single HPO term in this context; curate as appropriate)

### Laboratory abnormalities
- Elevated plasma/urinary metanephrines (metanephrine, normetanephrine) and sometimes 3‑methoxytyramine are the key biochemical signatures used clinically. (bresser2024themolecularclassification pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 4-5)

### Quality-of-life impact
- Direct PPGL patient-reported outcome datasets were not retrieved as full-text evidence in this run; however, a 2024 head-and-neck paraganglioma registry protocol explicitly plans longitudinal PROMs including EQ‑5D‑5L, EORTC QLQ‑C30, fatigue and anxiety/depression scales, indicating recognized QoL burden and need for standardized data capture. (bresser2024headandneck, not in evidence IDs; therefore not cited as evidence here.)

---

## 4. Genetic / molecular information
### Causal genes (high-confidence susceptibility genes)
A 2024 review lists major susceptibility genes including **NF1, VHL, RET, SDHx (SDHA/SDHB/SDHC/SDHD/SDHAF2), TMEM127, MAX, FH**. (giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2)

### Pathogenic variants (types and origin)
- The retrieved evidence supports that PPGL susceptibility includes both **germline** and **somatic** drivers and that drivers are identifiable in a large fraction of tumors (e.g., ~70–80% depending on series and definitions). (giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2, richter2024patientsexand pages 1-2)
- Variant classes are gene-dependent (loss-of-function in tumor suppressor genes such as SDHB/VHL/NF1 is common); detailed allele frequencies in gnomAD and variant-level ClinVar assertions were not retrieved in this run.

### Epigenetic information
- Metabolic derangements (succinate/fumarate accumulation) are linked to epigenetic alterations (hypermethylation/CIMP-like states) and hypoxia-like signaling in PPGL biology. (jeeyavudeen2024tumormetabolismin pages 1-3)

---

## 5. Environmental information
- No specific environmental toxins, lifestyle factors, or infectious agents were identified as causal or protective in the retrieved evidence set.

---

## 6. Mechanism / pathophysiology
### Molecular clusters and causal chains
**Cluster 1: Pseudohypoxia / Krebs cycle dysregulation (SDHx, FH, VHL/EPAS1 axis)**
- Mechanistic chain (conceptual): SDHx/FH dysfunction → accumulation of oncometabolites (succinate, fumarate) → inhibition of α‑ketoglutarate–dependent dioxygenases → epigenetic dysregulation (hypermethylation) and stabilization of hypoxia-inducible signaling → pro-angiogenic and pro-proliferative transcriptional programs contributing to tumorigenesis and aggressiveness. (jeeyavudeen2024tumormetabolismin pages 1-3, bresser2024themolecularclassification pages 6-7)

**Cluster 2: Kinase signaling (RET/NF1/TMEM127/MAX/HRAS)**
- Mechanistic chain (conceptual): kinase/RAS pathway activation → altered growth signaling and adrenal-predominant, adrenergic biochemical phenotypes in many cases. (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, richter2024patientsexand pages 1-2)

**Cluster 3: Wnt-altered (MAML3/CSDE1)**
- Wnt-altered tumors (e.g., MAML3 fusions) are highlighted in modern classifiers and may show higher metastatic propensity and distinct immune features (including PD‑L1 expression in MAML3-related tumors in metastatic cohorts). (bresser2024themolecularclassification pages 7-9, calsina2023genomicandimmune pages 1-2)

### Metastasis biology and immune microenvironment (recent research emphasis)
A large Nature Communications 2023 study profiled metastatic PPGL and identified genomic instability and immune features relevant to prognostication:
- High **TMB**, **MSI**, and **SCNA burden** associated with **ATRX/TERT** alterations were proposed as prognostic markers; transcriptomics highlighted **CDK1** as an additional marker. (calsina2023genomicandimmune pages 1-2, calsina2023genomicandimmune pages 4-5)
- The tumor microenvironment in metastatic PPGL was described as generally **immunosuppressive**, with an exception for **PD‑L1–expressing MAML3-related tumors**, suggesting a subset potentially more amenable to immune checkpoint approaches. (calsina2023genomicandimmune pages 1-2)

### Suggested GO biological-process terms (examples)
- **GO:0007049** cell cycle; **GO:0006281** DNA repair; **GO:0030198** extracellular matrix organization; **GO:0006955** immune response; **GO:0001666** response to hypoxia.

### Suggested CL (cell types) and UBERON (anatomy)
- **CL:** chromaffin cell (curate appropriate CL term), macrophage (tumor-associated), T cell subsets (for immune microenvironment).
- **UBERON:** adrenal medulla; carotid body; sympathetic chain ganglia; jugulotympanic region.

---

## 7. Anatomical structures affected
### Organ/tissue level
- **Primary sites:** adrenal medulla (PCC); extra-adrenal sympathetic chain/retroperitoneum/mediastinum/bladder (sympathetic PGL); head and neck parasympathetic paraganglia (carotid body, vagal, jugulotympanic, etc.). (bresser2024themolecularclassification pages 1-2, lin2022headandneck pages 1-2)
- **Complication targets:** cardiovascular system (catecholamine cardiomyopathy, arrhythmias), kidneys (hypertensive injury), CNS (hypertensive encephalopathy in crises). (giacche2024pheochromocytoma–paragangliomasyndromea pages 4-5, bima2024preventionandmanagement pages 2-4)

---

## 8. Temporal development
### Onset and course
- PPGL can be discovered due to symptoms, incidental imaging, or surveillance of mutation carriers; attacks/paroxysms can be unpredictable and triggered by stressors or procedures. (junior2023thepheochromocytomaparagangliomasyndrome pages 1-2)
- Recurrence/metastasis can occur years to decades after surgery, supporting long-term surveillance. (torresan2023longtermoutcomesafter pages 1-2, araujocastro2023localrecurrenceand pages 1-2)

---

## 9. Inheritance and population
### Epidemiology
- **Incidence:** 2–8 cases per million people is reported in a high-citation 2022 review. (lin2022headandneck pages 1-2)
- **Metastatic potential:** recent estimates cited include ~10–15% metastatic rate for PCC and up to ~50% for abdominal PGL. (bresser2024themolecularclassification pages 1-2, hose2023top2aexpressionin pages 1-2)
- **Recurrence after surgery:** long-term recurrence risk can be substantial; one 2023 surgical cohort reported 10‑year recurrence risk 13% rising to 33% at 30 years. (torresan2023longtermoutcomesafter pages 1-2)

### Inheritance patterns
- The high proportion of germline predisposition implies many familial cases follow autosomal dominant inheritance with variable penetrance (gene-dependent). The retrieved evidence provides gene lists and hereditary fractions but did not provide penetrance curves suitable for numeric annotation.

### Population demographics
- A 2024 synthesis suggests sex and ancestry/origin can influence driver-gene distributions and presentation (e.g., differences in hypoxia-pathway germline PVs and metastasis prevalence by sex; kinase-driver distributions varying between European and Asian cohorts). (richter2024patientsexand pages 1-2)

---

## 10. Diagnostics
### Biochemical testing (real-world standard)
- Plasma/urinary **fractionated metanephrines** are first-line; a 2024 review reports plasma free metanephrines sensitivity ~98% and urinary fractionated metanephrines sensitivity ~93%, NPV >99%, and overall specificity ~94%, emphasizing supine sampling conditions to reduce false positives. (giacche2024pheochromocytoma–paragangliomasyndromea pages 4-5)
- A 2023 review calls plasma free metanephrine the “current gold standard” with sensitivity 99% and notes a normal value “virtually excludes” functioning PPGL. (junior2023thepheochromocytomaparagangliomasyndrome pages 5-7)

### Imaging
**Functional imaging tracer selection is genotype- and site-informed** in modern practice. (giacche2024pheochromocytoma–paragangliomasyndromea pages 10-12)

**Direct head-to-head diagnostic performance (recent, quantitative):**
- In a 2023 retrospective comparison (n=113), **18F‑FDOPA PET/CT detected and correctly localized all 55 PCC lesions** vs 25 by 68Ga‑DOTATOC, with sensitivity **100% vs 49%**, accuracy **98% vs 70%**, and NPV **100% vs 63%**. (iversen2023[18f]fdopapetctis pages 1-2)

### Genetic testing strategy
- Universal germline multi-gene panel testing is advocated in recent hereditary adrenal tumor management review as comprehensive and cost-effective, reflecting the large gene set and high heritability. (ohmoto2024currentprospectsof pages 1-2)

### Pathology
- PPGLs often show “zellballen” architecture; metastatic and non-metastatic tumors can be histologically indistinguishable. (bresser2024themolecularclassification pages 1-2, lin2022headandneck pages 2-3)

---

## 11. Outcomes / prognosis
### Prognostic factors and models
- **Recurrence predictors after surgery:** In a 2023 multicenter cohort (n=303), recurrence occurred in **7.9%** after median 4.8 years; independent predictors were **SDHB pathogenic variant (HR 13.3)**, higher urinary normetanephrine (HR 1.02 per SD), and larger tumor size (HR 1.01 per mm). (araujocastro2023localrecurrenceand pages 1-2)
- **Long-term recurrence:** a 2023 surgical series reported 10‑year recurrence 13% and 30‑year recurrence 33%, with higher new-tumor recurrence in hereditary cases. (torresan2023longtermoutcomesafter pages 1-2)

### Metastatic survival
- Reported 5‑year survival after metastatic progression is heterogeneous; one 2024 endocrine pathology review quotes 40–77%. (bresser2024themolecularclassification pages 1-2)

---

## 12. Treatment
### Surgery and perioperative management (curative for localized disease)
- Radical surgery is generally the only curative modality for localized disease; disseminated/metastatic disease requires systemic/radiopharmaceutical approaches. (kornerup2024effectsofpeptide pages 1-2)

### Radiopharmaceutical therapy and theranostics (major real-world implementation)
**PRRT (177Lu‑DOTATATE / 90Y‑DOTATATE) for SSTR-positive advanced/metastatic PPGL**
- **Nationwide cohort (Denmark, 2024; n=28):** median OS **72 months**, 5‑year survival **65%**, median PFS **30 months**, with low toxicity; germline mutation carriers had better survival (p=0.041). (kornerup2024effectsofpeptide pages 1-2)
- **Large multicenter PRRT cohort including PPGL (SEPTRALU, 2023):** PPGL subgroup median PFS **30.6 months** under standard 4-cycle 7.4 GBq q8wk regimen. (mitjavila2023efficacyof[177lu]ludotatate pages 1-2)
- **Meta-analysis (2023; 213 patients):** pooled disease control rate (DCR) **0.81** overall; 177Lu DCR **0.83**, 90Y DCR **0.76**. (marretta2023responsetopeptide pages 1-2)
- **Single-institution long follow-up cohort (2024; n=30 PCC/PGL):** partial response 23% and stable disease 63%; 5- and 10-year OS 75% and 59%, respectively; grade 3–4 acute hematologic toxicity in 10%. (rubino2024peptidereceptorradionuclide pages 1-3)

**131I‑MIBG therapy**
- A 2022 phase II single-dose 131I‑mIBG trial (n=16 treated) reported biochemical response rate **23.5%** (≥50% decrease in urinary catecholamines), RECIST response rate 5.9%, and common hematologic AEs up to grade 3 in 14/16. (inaki2022; not converted to pqac evidence id in this run, so not cited further.)

### Ongoing/active clinical trials (examples)
- **NCT03206060 (NCI; Phase 2; recruiting; est. n=130):** open-label single-arm Lu‑177‑DOTATATE for **inoperable SSTR+ PCC/PGL**, with Ga‑68‑DOTATATE PET confirmation; primary endpoint PFS at 6 months; includes QoL and biochemical outcomes. (NCT03206060 chunk 1, NCT03206060 chunk 2)
- **NCT02186678 (Marseille; completed):** prospective diagnostic comparison of **68Ga‑DOTATATE PET‑CT vs 18F‑FDOPA PET‑CT** for staging/restaging; primary endpoint is additional foci detected by DOTATATE vs FDOPA. (NCT02186678 chunk 1)
- **NCT05948137 (Asan; terminated due to 123I‑MIBG shortages):** prospective observational comparison **18F‑FDOPA PET/CT vs 123I‑MIBG SPECT/CT** with sensitivity non-inferiority endpoint. (NCT05948137 chunk 1)

### Suggested MAXO terms (examples)
- Surgical resection (adrenalectomy / tumor excision)
- Alpha-adrenergic blockade (preoperative medical preparation)
- Peptide receptor radionuclide therapy (PRRT)
- I‑131 metaiodobenzylguanidine therapy
- Radiographic surveillance / biochemical surveillance

---

## 13. Prevention
Primary prevention is not established for genetically driven PPGL; prevention focuses on:
- **Secondary prevention:** cascade genetic testing and structured surveillance of mutation carriers; early biochemical testing and imaging when indicated. High heritability and guideline emphasis on genetic testing support this approach. (lin2022headandneck pages 1-2, ohmoto2024currentprospectsof pages 1-2)
- **Tertiary prevention:** lifelong follow-up to prevent late metastatic recurrence and manage cardiovascular complications. (torresan2023longtermoutcomesafter pages 1-2, araujocastro2023localrecurrenceand pages 1-2)

---

## 14. Other species / natural disease
Naturally occurring PPGL occurs in companion animals and can serve as comparative biology.
- A 2024 prospective metabolomics study of **canine pheochromocytomas** (21 dogs vs 10 controls) found PCC tissue had markedly higher norepinephrine fraction (median 88% vs 14%) and identified a dog with an aberrant succinate:fumarate ratio (~25-fold higher) suggesting SDHx mutation; supporting metabolomics for genetic inference in dogs. (berg2024metabolomicprofilingof; not assigned a pqac evidence id in this run, so not cited further.)

---

## 15. Model organisms and experimental models
A recurring translational gap is the scarcity of faithful PPGL models, especially for SDHB-deficient metastatic biology.
- A zebrafish CRISPR model introducing truncating **sdhb** lesions showed reduced complex II activity and “significant succinate accumulation,” mimicking SDHB-associated metabolic effects and enabling in vivo screening. (dona2021lossofsdhb)
- A 2024 conditional SDHC loss study in early Sox10+ neural crest cells produced developmental phenotypes but “not paraganglioma tumorigenesis,” underscoring difficulty modeling human SDHx-driven tumorigenesis in mice. (lewis2024mousedevelopmentaldefects)

*(These model-system sources were retrieved as paper metadata in this run but not extracted into pqac evidence IDs; therefore, they are described qualitatively here without pqac citation IDs.)*

---

## Recent developments (prioritizing 2023–2024)
1. **Metastatic PPGL molecular stratification** has shifted from single-gene risk rules toward multi-feature classifiers combining ATRX/TERT alterations, MSI/TMB/SCNA burden, and immune microenvironment subtypes, potentially enabling more actionable prognostication and immunotherapy triage. (calsina2023genomicandimmune pages 4-5, bresser2024themolecularclassification pages 7-9, calsina2023genomicandimmune pages 1-2)
2. **Theranostics implementation is expanding**: PRRT outcome datasets in PPGL now include nationwide cohorts with multi-year OS/PFS and long follow-up single-institution series; systematic reviews support high disease control rates (~80%). (kornerup2024effectsofpeptide pages 1-2, rubino2024peptidereceptorradionuclide pages 1-3, marretta2023responsetopeptide pages 1-2)
3. **Imaging evidence is becoming more quantitative and comparative** (e.g., FDOPA vs DOTATOC performance differences for PCC localization), supporting practical algorithm refinement. (iversen2023[18f]fdopapetctis pages 1-2)

---

## Notes on evidence limits and curation gaps
- **Ontology identifiers (MONDO/OMIM/Orphanet/ICD/MeSH)** and **variant-level ClinVar/gnomAD details** were not retrieved in this run, so they are intentionally not asserted.
- Several relevant 2024 items surfaced as “unobtainable” in paper search (e.g., Endocrine Reviews imaging review; patient-reported burden), and therefore could not be used for evidence-backed statements here.



References

1. (bresser2024themolecularclassification pages 1-2): Carolijn J. M. de Bresser and Ronald R. de Krijger. The molecular classification of pheochromocytomas and paragangliomas: discovering the genomic and immune landscape of metastatic disease. Endocrine Pathology, 35:279-292, Oct 2024. URL: https://doi.org/10.1007/s12022-024-09830-3, doi:10.1007/s12022-024-09830-3. This article has 13 citations and is from a peer-reviewed journal.

2. (t.2024pheochromocytomaanupdated pages 1-2): J. S. Saavedra T., Humberto Alejandro Nati-Castillo, L. A. Valderrama Cometa, Wilfredo A. Rivera-Martínez, Josué Asprilla, C. M. Castaño-Giraldo, Leonardo Sánchez S., Mishell Heredia-Espín, Marlon Arias-Intriago, and Juan S. Izquierdo-Condoy. Pheochromocytoma: an updated scoping review from clinical presentation to management and treatment. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1433582, doi:10.3389/fendo.2024.1433582. This article has 32 citations.

3. (giacche2024pheochromocytoma–paragangliomasyndromea pages 1-2): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Biomedicines, 12:2385, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 7 citations.

4. (bima2024preventionandmanagement pages 4-5): Chiara Bima, Chiara Lopez, Gerdi Tuli, Jessica Munarin, Stefano Arata, Matteo Procopio, Martina Bollati, Mauro Maccario, Luisa De Sanctis, and Mirko Parasiliti-Caprino. Prevention and management of hypertensive crises in children with pheochromocytoma and paraganglioma. Frontiers in Endocrinology, Aug 2024. URL: https://doi.org/10.3389/fendo.2024.1460320, doi:10.3389/fendo.2024.1460320. This article has 13 citations.

5. (richter2024patientsexand pages 1-2): Susan Richter and Nicole Bechmann. Patient sex and origin influence distribution of driver genes and clinical presentation of paraganglioma. Journal of the Endocrine Society, Feb 2024. URL: https://doi.org/10.1210/jendso/bvae038, doi:10.1210/jendso/bvae038. This article has 11 citations and is from a peer-reviewed journal.

6. (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Biomedicines, 12:2385, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 7 citations.

7. (giacche2024pheochromocytoma–paragangliomasyndromea pages 9-10): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Biomedicines, 12:2385, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 7 citations.

8. (lin2022headandneck pages 1-2): Edward P. Lin, Bennett B. Chin, Lauren Fishbein, Toshio Moritani, Simone P. Montoya, Shehanaz Ellika, and Shawn Newlands. Head and neck paragangliomas: an update on the molecular classification, state-of-the-art imaging, and management recommendations. Radiology. Imaging cancer, 4 3:e210088, May 2022. URL: https://doi.org/10.1148/rycan.210088, doi:10.1148/rycan.210088. This article has 111 citations.

9. (araujocastro2023localrecurrenceand pages 1-2): Marta Araujo-Castro, Iñigo García Sanz, César Mínguez Ojeda, Felicia Hanzu, Mireia Mora, Almudena Vicente, Concepción Blanco Carrera, Paz de Miguel Novoa, María del Carmen López García, Cristina Lamas, Laura Manjón-Miguélez, María del Castillo Tous, Pablo Rodríguez de Vera, Rebeca Barahona San Millán, Mónica Recasens, Mariana Tomé Fernández-Ladreda, Nuria Valdés, Paola Gracia Gimeno, Cristina Robles Lazaro, Theodora Michalopoulou, Cristina Álvarez Escolá, Rogelio García Centeno, Verónica Barca-Tierno, Aura D. Herrera-Martínez, and María Calatayud. Local recurrence and metastatic disease in pheochromocytomas and sympathetic paragangliomas. Frontiers in Endocrinology, Dec 2023. URL: https://doi.org/10.3389/fendo.2023.1279828, doi:10.3389/fendo.2023.1279828. This article has 13 citations.

10. (giacche2024pheochromocytoma–paragangliomasyndromea pages 12-14): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Biomedicines, 12:2385, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 7 citations.

11. (junior2023thepheochromocytomaparagangliomasyndrome pages 1-2): José Viana Lima Junior and Claudio Elias Kater. The pheochromocytoma/paraganglioma syndrome: an overview on mechanisms, diagnosis and management. International braz j urol, 49:307-319, Jun 2023. URL: https://doi.org/10.1590/s1677-5538.ibju.2023.0038, doi:10.1590/s1677-5538.ibju.2023.0038. This article has 59 citations.

12. (giacche2024pheochromocytoma–paragangliomasyndromea pages 2-4): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Biomedicines, 12:2385, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 7 citations.

13. (t.2024pheochromocytomaanupdated pages 3-6): J. S. Saavedra T., Humberto Alejandro Nati-Castillo, L. A. Valderrama Cometa, Wilfredo A. Rivera-Martínez, Josué Asprilla, C. M. Castaño-Giraldo, Leonardo Sánchez S., Mishell Heredia-Espín, Marlon Arias-Intriago, and Juan S. Izquierdo-Condoy. Pheochromocytoma: an updated scoping review from clinical presentation to management and treatment. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1433582, doi:10.3389/fendo.2024.1433582. This article has 32 citations.

14. (bima2024preventionandmanagement pages 2-4): Chiara Bima, Chiara Lopez, Gerdi Tuli, Jessica Munarin, Stefano Arata, Matteo Procopio, Martina Bollati, Mauro Maccario, Luisa De Sanctis, and Mirko Parasiliti-Caprino. Prevention and management of hypertensive crises in children with pheochromocytoma and paraganglioma. Frontiers in Endocrinology, Aug 2024. URL: https://doi.org/10.3389/fendo.2024.1460320, doi:10.3389/fendo.2024.1460320. This article has 13 citations.

15. (giacche2024pheochromocytoma–paragangliomasyndromea pages 4-5): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Biomedicines, 12:2385, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 7 citations.

16. (jeeyavudeen2024tumormetabolismin pages 1-3): Mohammad Sadiq Jeeyavudeen, Navin Mathiyalagan, Cornelius Fernandez James, and Joseph M. Pappachan. Tumor metabolism in pheochromocytomas: clinical and therapeutic implications. Exploration of Targeted Anti-tumor Therapy, 5:349-373, Apr 2024. URL: https://doi.org/10.37349/etat.2024.00222, doi:10.37349/etat.2024.00222. This article has 3 citations.

17. (bresser2024themolecularclassification pages 6-7): Carolijn J. M. de Bresser and Ronald R. de Krijger. The molecular classification of pheochromocytomas and paragangliomas: discovering the genomic and immune landscape of metastatic disease. Endocrine Pathology, 35:279-292, Oct 2024. URL: https://doi.org/10.1007/s12022-024-09830-3, doi:10.1007/s12022-024-09830-3. This article has 13 citations and is from a peer-reviewed journal.

18. (bresser2024themolecularclassification pages 7-9): Carolijn J. M. de Bresser and Ronald R. de Krijger. The molecular classification of pheochromocytomas and paragangliomas: discovering the genomic and immune landscape of metastatic disease. Endocrine Pathology, 35:279-292, Oct 2024. URL: https://doi.org/10.1007/s12022-024-09830-3, doi:10.1007/s12022-024-09830-3. This article has 13 citations and is from a peer-reviewed journal.

19. (calsina2023genomicandimmune pages 1-2): Bruna Calsina, Elena Piñeiro-Yáñez, Ángel M. Martínez-Montes, Eduardo Caleiras, Ángel Fernández-Sanromán, María Monteagudo, Rafael Torres-Pérez, Coral Fustero-Torre, Marta Pulgarín-Alfaro, Eduardo Gil, Rocío Letón, Scherezade Jiménez, Santiago García-Martín, Maria Carmen Martin, Juan María Roldán-Romero, Javier Lanillos, Sara Mellid, María Santos, Alberto Díaz-Talavera, Ángeles Rubio, Patricia González, Barbara Hernando, Nicole Bechmann, Margo Dona, María Calatayud, Sonsoles Guadalix, Cristina Álvarez-Escolá, Rita M. Regojo, Javier Aller, Maria Isabel Del Olmo-Garcia, Adrià López-Fernández, Stephanie M. J. Fliedner, Elena Rapizzi, Martin Fassnacht, Felix Beuschlein, Marcus Quinkler, Rodrigo A. Toledo, Massimo Mannelli, Henri J. Timmers, Graeme Eisenhofer, Sandra Rodríguez-Perales, Orlando Domínguez, Geoffrey Macintyre, Maria Currás-Freixes, Cristina Rodríguez-Antona, Alberto Cascón, Luis J. Leandro-García, Cristina Montero-Conde, Giovanna Roncador, Juan Fernando García-García, Karel Pacak, Fátima Al-Shahrour, and Mercedes Robledo. Genomic and immune landscape of metastatic pheochromocytoma and paraganglioma. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36769-6, doi:10.1038/s41467-023-36769-6. This article has 85 citations and is from a highest quality peer-reviewed journal.

20. (calsina2023genomicandimmune pages 4-5): Bruna Calsina, Elena Piñeiro-Yáñez, Ángel M. Martínez-Montes, Eduardo Caleiras, Ángel Fernández-Sanromán, María Monteagudo, Rafael Torres-Pérez, Coral Fustero-Torre, Marta Pulgarín-Alfaro, Eduardo Gil, Rocío Letón, Scherezade Jiménez, Santiago García-Martín, Maria Carmen Martin, Juan María Roldán-Romero, Javier Lanillos, Sara Mellid, María Santos, Alberto Díaz-Talavera, Ángeles Rubio, Patricia González, Barbara Hernando, Nicole Bechmann, Margo Dona, María Calatayud, Sonsoles Guadalix, Cristina Álvarez-Escolá, Rita M. Regojo, Javier Aller, Maria Isabel Del Olmo-Garcia, Adrià López-Fernández, Stephanie M. J. Fliedner, Elena Rapizzi, Martin Fassnacht, Felix Beuschlein, Marcus Quinkler, Rodrigo A. Toledo, Massimo Mannelli, Henri J. Timmers, Graeme Eisenhofer, Sandra Rodríguez-Perales, Orlando Domínguez, Geoffrey Macintyre, Maria Currás-Freixes, Cristina Rodríguez-Antona, Alberto Cascón, Luis J. Leandro-García, Cristina Montero-Conde, Giovanna Roncador, Juan Fernando García-García, Karel Pacak, Fátima Al-Shahrour, and Mercedes Robledo. Genomic and immune landscape of metastatic pheochromocytoma and paraganglioma. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36769-6, doi:10.1038/s41467-023-36769-6. This article has 85 citations and is from a highest quality peer-reviewed journal.

21. (torresan2023longtermoutcomesafter pages 1-2): Francesca Torresan, Arianna Beber, Donatella Schiavone, Stefania Zovato, Francesca Galuppini, Filippo Crimì, Filippo Ceccato, and Maurizio Iacobone. Long-term outcomes after surgery for pheochromocytoma and sympathetic paraganglioma. Cancers, 15:2890, May 2023. URL: https://doi.org/10.3390/cancers15112890, doi:10.3390/cancers15112890. This article has 19 citations.

22. (hose2023top2aexpressionin pages 1-2): Karolina Solhusløkk Höse, Adam Stenman, Fredrika Svahn, Catharina Larsson, and C. Christofer Juhlin. Top2a expression in pheochromocytoma and abdominal paraganglioma: a marker of poor clinical outcome? Endocrine Pathology, 34:129-141, Jan 2023. URL: https://doi.org/10.1007/s12022-022-09746-w, doi:10.1007/s12022-022-09746-w. This article has 10 citations and is from a peer-reviewed journal.

23. (junior2023thepheochromocytomaparagangliomasyndrome pages 5-7): José Viana Lima Junior and Claudio Elias Kater. The pheochromocytoma/paraganglioma syndrome: an overview on mechanisms, diagnosis and management. International braz j urol, 49:307-319, Jun 2023. URL: https://doi.org/10.1590/s1677-5538.ibju.2023.0038, doi:10.1590/s1677-5538.ibju.2023.0038. This article has 59 citations.

24. (giacche2024pheochromocytoma–paragangliomasyndromea pages 10-12): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Biomedicines, 12:2385, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 7 citations.

25. (iversen2023[18f]fdopapetctis pages 1-2): Peter Iversen, Stine Kramer, Andreas Ebbehoj, Esben Søndergaard, Kirstine Stochholm, Per Løgstrup Poulsen, and Karin Hjorthaug. [18f]fdopa pet/ct is superior to [68ga]dotatoc pet/ct in diagnostic imaging of pheochromocytoma. EJNMMI Research, Dec 2023. URL: https://doi.org/10.1186/s13550-023-01056-4, doi:10.1186/s13550-023-01056-4. This article has 9 citations and is from a peer-reviewed journal.

26. (ohmoto2024currentprospectsof pages 1-2): Akihiro Ohmoto, Naomi Hayashi, Shunji Takahashi, and Arisa Ueki. Current prospects of hereditary adrenal tumors: towards better clinical management. Hereditary Cancer in Clinical Practice, Mar 2024. URL: https://doi.org/10.1186/s13053-024-00276-6, doi:10.1186/s13053-024-00276-6. This article has 5 citations and is from a peer-reviewed journal.

27. (lin2022headandneck pages 2-3): Edward P. Lin, Bennett B. Chin, Lauren Fishbein, Toshio Moritani, Simone P. Montoya, Shehanaz Ellika, and Shawn Newlands. Head and neck paragangliomas: an update on the molecular classification, state-of-the-art imaging, and management recommendations. Radiology. Imaging cancer, 4 3:e210088, May 2022. URL: https://doi.org/10.1148/rycan.210088, doi:10.1148/rycan.210088. This article has 111 citations.

28. (kornerup2024effectsofpeptide pages 1-2): Linda Skibsted Kornerup, Mikkel Andreassen, Ulrich Knigge, Anne Kirstine Arveschoug, Per Løgstup Poulsen, Andreas Kjær, Peter Sandor Oturai, Henning Grønbæk, and Gitte Dam. Effects of peptide receptor radiotherapy in patients with advanced paraganglioma and pheochromocytoma: a nation-wide cohort study. Cancers, 16:1349, Mar 2024. URL: https://doi.org/10.3390/cancers16071349, doi:10.3390/cancers16071349. This article has 6 citations.

29. (mitjavila2023efficacyof[177lu]ludotatate pages 1-2): Mercedes Mitjavila, Paula Jimenez-Fonseca, Pilar Belló, Virginia Pubul, Juan Carlos Percovich, Amparo Garcia-Burillo, Jorge Hernando, Javier Arbizu, Emilia Rodeño, Montserrat Estorch, Belén Llana, Maribel Castellón, Lina García-Cañamaque, Pablo Gajate, Maria Carmen Riesco, Maria Begoña Miguel, David Balaguer-Muñoz, Ana Custodio, Juana María Cano, Alexandra Repetto, Pilar Garcia-Alonso, Maria Angustias Muros, Jose Luis Vercher-Conejero, and Alberto Carmona-Bayonas. Efficacy of [177lu]lu-dotatate in metastatic neuroendocrine neoplasms of different locations: data from the septralu study. European Journal of Nuclear Medicine and Molecular Imaging, 50:2486-2500, Mar 2023. URL: https://doi.org/10.1007/s00259-023-06166-8, doi:10.1007/s00259-023-06166-8. This article has 57 citations and is from a highest quality peer-reviewed journal.

30. (marretta2023responsetopeptide pages 1-2): Antonella Lucia Marretta, Alessandro Ottaiano, Domenico Iervolino, Alessandra Bracigliano, Ottavia Clemente, Francesca Di Gennaro, Roberto Tafuto, Mariachiara Santorsola, Secondo Lastoria, and Salvatore Tafuto. Response to peptide receptor radionuclide therapy in pheocromocytomas and paragangliomas: a systematic review and meta-analysis. Journal of Clinical Medicine, 12:1494, Feb 2023. URL: https://doi.org/10.3390/jcm12041494, doi:10.3390/jcm12041494. This article has 20 citations.

31. (rubino2024peptidereceptorradionuclide pages 1-3): Manila Rubino, Giuseppe Danilo Di Stasio, Lisa Bodei, Stefano Papi, Paola Anna Rocca, Mahila Esmeralda Ferrari, Cristiana Iuliana Fodor, Vincenzo Bagnardi, Samuele Frassoni, Riccardo Mei, Nicola Fazio, Francesco Ceci, and Chiara Maria Grana. Peptide receptor radionuclide therapy with 177lu- or 90y-sstr peptides in malignant pheochromocytomas (pccs) and paragangliomas (pgls): results from a single institutional retrospective analysis. Endocrine, 84:704-710, Feb 2024. URL: https://doi.org/10.1007/s12020-024-03707-5, doi:10.1007/s12020-024-03707-5. This article has 6 citations and is from a peer-reviewed journal.

32. (NCT03206060 chunk 1):  Lu-177-DOTATATE (Lutathera) in Therapy of Inoperable Pheochromocytoma/ Paraganglioma. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03206060

33. (NCT03206060 chunk 2):  Lu-177-DOTATATE (Lutathera) in Therapy of Inoperable Pheochromocytoma/ Paraganglioma. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03206060

34. (NCT02186678 chunk 1):  Comparison of Diagnostic Performances of 68Ga-DOTATATE PET-CT and 18F-FDOPA PET-CT in Paragangliomas and Pheochromocytomas Evaluation. Assistance Publique Hopitaux De Marseille. 2014. ClinicalTrials.gov Identifier: NCT02186678

35. (NCT05948137 chunk 1): Jin-Sook Ryu. F-18 FDOPA PET/CT Versus I-123 MIBG Scintigraphy With SPECT/CT for the Diagnosis of Pheochromocytoma and Paraganglioma. Asan Medical Center. 2017. ClinicalTrials.gov Identifier: NCT05948137
