---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T20:14:49.338657'
end_time: '2026-04-05T20:27:02.470784'
duration_seconds: 733.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multiple Endocrine Neoplasia Type 2
  mondo_id: ''
  category: ''
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
- **Disease Name:** Multiple Endocrine Neoplasia Type 2
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Multiple Endocrine Neoplasia Type 2** covering all of the
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
- **Disease Name:** Multiple Endocrine Neoplasia Type 2
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Multiple Endocrine Neoplasia Type 2** covering all of the
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


## Multiple Endocrine Neoplasia Type 2 (MEN2): Comprehensive Disease Characteristics Report (2023–2024 prioritized)

### Executive summary
Multiple endocrine neoplasia type 2 (MEN2) is an autosomal-dominant hereditary endocrine tumor syndrome caused by activating germline variants in **RET**. It is primarily defined by medullary thyroid carcinoma (MTC) with variable risks of pheochromocytoma (PCC) and primary hyperparathyroidism (PHPT), depending on the specific RET pathogenic variant (binter2024doesgenotypespecificphenotype pages 1-2, binter2024doesgenotypespecificphenotype pages 2-4). Clinical management is increasingly **genotype-guided** (e.g., prophylactic thyroidectomy timing) and now integrates **actionable biomarker testing** (germline and somatic RET) to select targeted systemic therapy, especially selective RET inhibitors such as selpercatinib (mete2024consensusstatementrecommendations pages 3-5, wirth2024durabilityofresponse pages 1-2).

---

## 1. Disease Information

### 1.1 Disease overview (definition)
MEN2 is described in contemporary cohort literature as “an autosomal-dominant inherited orphan disease, caused by activating germline mutations of the RET gene,” characterized mainly by **MTC**, **PCC**, and **PHPT** (binter2024doesgenotypespecificphenotype pages 1-2). MEN2 includes clinically important subtypes:
- **MEN2A** (classically MTC + PCC ± PHPT)
- **MEN2B** (often earlier onset/aggressive MTC; PCC risk; characteristic extra-endocrine phenotypes such as mucosal neuromas and GI ganglioneuromatosis are classically described, though not comprehensively covered in the retrieved evidence set) (binter2024doesgenotypespecificphenotype pages 2-4).

### 1.2 Key identifiers and controlled vocabulary
A compact identifiers table is provided below.

| Identifier type | ID | Label | Notes/source |
|---|---|---|---|
| MONDO | MONDO:0019003 | multiple endocrine neoplasia type 2 | Disease-target association in Open Targets lists MEN2 with MONDO_0019003; associated target RET. URL: https://platform.opentargets.org/ ; 2024/2025 access context (west2025medullarythyroidcancer pages 13-14) |
| Orphanet | ORPHA:653 | Multiple endocrine neoplasia type 2 | 2024 cohort paper reports MEN2 prevalence as 1–9/100,000 and explicitly cites ORPHA:653. URL: https://www.orpha.net ; 2024 (binter2024doesgenotypespecificphenotype pages 1-2) |
| OMIM/MIM subtype | MIM #171400 | MEN2A / classic MEN2A | 2024 genotype-phenotype study states classic MEN2A is associated in ~95% of cases with RET mutations at codons 609, 611, 618, 620, or 634. DOI URL: https://doi.org/10.3390/cancers16030494 ; 2024 (binter2024doesgenotypespecificphenotype pages 2-4) |
| OMIM/MIM subtype | MIM #162300 | MEN2B | 2024 genotype-phenotype study states MEN2B is associated in ~95% with RET p.Met918Thr and in <5% with p.Ala883Phe. DOI URL: https://doi.org/10.3390/cancers16030494 ; 2024 (binter2024doesgenotypespecificphenotype pages 2-4) |
| Synonym | — | MEN2 | Standard abbreviation used throughout recent MEN2 literature for multiple endocrine neoplasia type 2. Supported in 2024 MEN2 cohort/guideline-aligned reviews. DOI URLs: https://doi.org/10.3390/cancers16030494 ; https://doi.org/10.3389/fendo.2024.1445633 ; 2024 (binter2024doesgenotypespecificphenotype pages 1-2, binter2024doesgenotypespecificphenotype pages 2-4) |
| Synonym | — | MEN 2 | Orthographic variant used in recent literature, including nationwide Danish MEN 2A study and other 2023-2025 papers. DOI URL: https://doi.org/10.3390/cancers15072125 ; 2023 (holm2023primaryhyperparathyroidismin pages 1-2) |
| Synonym | — | Sipple syndrome | Not supported in the retrieved evidence snippets; should be treated as unconfirmed from current evidence set. (binter2024doesgenotypespecificphenotype pages 1-2, binter2024doesgenotypespecificphenotype pages 2-4) |
| Core definition | — | Autosomal-dominant hereditary endocrine neoplasia syndrome caused by activating germline RET variants | Recent studies define MEN2 as an autosomal-dominant orphan disease caused by activating germline RET mutations, characterized mainly by medullary thyroid carcinoma, pheochromocytoma, and primary hyperparathyroidism. DOI URLs: https://doi.org/10.3390/cancers16030494 ; https://doi.org/10.3389/fendo.2024.1445633 ; 2024 (binter2024doesgenotypespecificphenotype pages 1-2, binter2024doesgenotypespecificphenotype pages 2-4) |
| Main manifestation | — | Medullary thyroid carcinoma (MTC) | Primary hallmark tumor arising from parafollicular C-cells; emphasized as the core MEN2 manifestation in recent reviews/cohorts. DOI URLs: https://doi.org/10.3390/cancers16030494 ; https://doi.org/10.3390/cancers15194865 ; 2023-2024 (binter2024doesgenotypespecificphenotype pages 1-2, sahakian2023molecularbasisand pages 1-2) |
| Main manifestation | — | Pheochromocytoma (PCC) | Major MEN2 component; 2024 cohort paper notes risk varies by RET variant and that MEN2B patients develop PCC in about 50% of cases. DOI URL: https://doi.org/10.3390/cancers16030494 ; 2024 (binter2024doesgenotypespecificphenotype pages 2-4) |
| Main manifestation | — | Primary hyperparathyroidism (PHPT) | Major MEN2A-associated component; Danish nationwide study found PHPT frequency 8% in MEN2A, often mild/asymptomatic. DOI URL: https://doi.org/10.3390/cancers15072125 ; 2023 (holm2023primaryhyperparathyroidismin pages 1-2) |


*Table: This table summarizes the key disease identifiers, accepted subtype OMIM numbers, supported synonyms, and hallmark manifestations for multiple endocrine neoplasia type 2. It is useful as a compact reference for standardizing a disease knowledge base entry.*

**Additional identifiers not captured in retrieved evidence:** ICD-10/ICD-11 codes and MeSH identifiers were not directly retrievable from the current evidence set and are therefore not reported here.

### 1.3 Common synonyms / alternative names
- Supported in retrieved sources: “MEN2”, “MEN 2” (binter2024doesgenotypespecificphenotype pages 1-2, holm2023primaryhyperparathyroidismin pages 1-2).
- “Sipple syndrome” is commonly used in practice but was **not** evidenced in the retrieved texts and is therefore not asserted (artifact-00).

### 1.4 Evidence source type
The evidence used here is largely **aggregated disease-level resources** (reviews, consensus statements), **single-center cohorts**, and **nationwide/population-based cohorts**, rather than EHR-only individual case data (binter2024doesgenotypespecificphenotype pages 1-2, holm2023primaryhyperparathyroidismin pages 1-2, west2025medullarythyroidcancer pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Activating **germline RET** pathogenic variants (gain-of-function) are the recognized causal driver of MEN2 (binter2024doesgenotypespecificphenotype pages 1-2, binter2024doesgenotypespecificphenotype pages 2-4).

**Ontology suggestions**
- MONDO: **MONDO:0019003** (artifact-00)
- Gene: **RET** (HGNC symbol RET)

### 2.2 Risk factors
#### Genetic risk factors (causal variants)
A 2024 cohort study summarizes that >100 RET pathogenic variants influence MEN2 manifestations and that classic MEN2A is associated in ~95% of cases with RET variants at **codons 609, 611, 618, 620 (exon 10)** or **codon 634 (exon 11)**; MEN2B is associated in ~95% with **RET p.Met918Thr (M918T; exon 16)** and <5% with **p.Ala883Phe (A883F; exon 15)** (binter2024doesgenotypespecificphenotype pages 1-2, binter2024doesgenotypespecificphenotype pages 2-4).

Population sequencing cohorts indicate that many incidentally discovered RET variants are “moderate-risk” per ATA categories, with markedly lower observed MTC risks than clinically ascertained MEN2 cohorts (west2025medullarythyroidcancer pages 1-2, west2025medullarythyroidcancer pages 3-5). This is relevant for counseling, though it reflects a mixture of ascertainment and penetrance effects.

**Key quantitative risk data (population cohorts):** In clinically unselected cohorts (UK Biobank, Geisinger MyCode), cumulative MTC risk to age 75 among incidentally identified RET carriers was 2.2% (UK) to 19.3% (US), compared with ~95.7% in clinically ascertained matched-variant cases (west2025medullarythyroidcancer pages 1-2). Variant prevalence was ~0.044% in UKB and ~0.06% in MyCode (west2025medullarythyroidcancer pages 3-5).

#### Environmental risk factors
No specific environmental exposures were evidenced in the retrieved MEN2-focused texts; MEN2 is treated as a predominantly genetic syndrome in the cited cohort and consensus sources (binter2024doesgenotypespecificphenotype pages 1-2, mete2024consensusstatementrecommendations pages 2-3).

### 2.3 Protective factors
No protective genetic or environmental factors were directly identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not established in the retrieved MEN2-specific evidence set.

---

## 3. Phenotypes (with ontology suggestions)

### 3.1 Core phenotypes and frequencies
MEN2 phenotype frequencies vary by RET genotype (binter2024doesgenotypespecificphenotype pages 2-4). From a large single-center cohort (n=158), the authors report management aligned with ATA risk groups and note that for MEN2B, “About 50% of patients with MEN2B develop PCC” (binter2024doesgenotypespecificphenotype pages 2-4).

**Key phenotype-specific population-based statistic (MEN2A—PHPT):** In a nationwide Danish MEN2A cohort (N=204), PHPT frequency was **8% (95% CI 5–12)**, with **age-related penetrance 8% by age 50** (holm2023primaryhyperparathyroidismin pages 1-2). Most were mild/asymptomatic (75%) (holm2023primaryhyperparathyroidismin pages 1-2).

### 3.2 Phenotype characteristics (examples)
#### Medullary thyroid carcinoma (MTC)
- Type: neoplasm / endocrine tumor
- Notes: arises from thyroid C-cells (binter2024doesgenotypespecificphenotype pages 1-2)
- Clinical course: strongly genotype-influenced; MEN2B (M918T) associated with earlier onset and typically aggressive disease in clinical paradigms (lagana2023theevolvingtreatment pages 1-3, binter2024doesgenotypespecificphenotype pages 2-4).

**Suggested HPO terms (non-exhaustive)**
- Medullary thyroid carcinoma: **HP:0002894** (suggested; not directly evidenced in retrieved texts)
- Elevated calcitonin: **HP:0030632** (suggested; calcitonin secretion is described for MTC in MTC reviews) (zhang2024moleculargeneticstherapeutics pages 1-2)

#### Pheochromocytoma (PCC)
- Type: neoplasm; catecholamine-secreting adrenal medulla tumor
- Risk varies by RET variant and ATA risk stratification (binter2024doesgenotypespecificphenotype pages 2-4).

**Suggested HPO terms**
- Pheochromocytoma: **HP:0002666** (suggested)
- Paroxysmal hypertension: **HP:0002645** (suggested)

#### Primary hyperparathyroidism (PHPT)
Population-based Danish MEN2A PHPT features:
- Frequency: 8% overall (holm2023primaryhyperparathyroidismin pages 1-2)
- Penetrance by age: 0% at 20y → 8% at 50y → 25% at 80y (holm2023primaryhyperparathyroidismin pages 4-7) (holm2023primaryhyperparathyroidismin media 7f070ef5)
- Symptoms: 75% asymptomatic; symptomatic cases included osteoporosis, nephrolithiasis (holm2023primaryhyperparathyroidismin pages 4-7)
- Surgical outcomes (13/16 operated): cure 69%, persistence 8%, recurrence 23%; permanent hypoparathyroidism 46% after first parathyroid surgery (holm2023primaryhyperparathyroidismin pages 9-10).

**Suggested HPO terms**
- Primary hyperparathyroidism: **HP:0000834** (suggested)
- Hypercalcemia: **HP:0003072** (suggested)
- Elevated parathyroid hormone: **HP:0030469** (suggested)

### 3.3 Quality of life impact
In advanced RET-mutant MTC, treatment-related symptoms (notably diarrhea) are important; patient-reported outcomes literature exists for selpercatinib but was not deeply retrieved in this run. However, long-term response durability and improved tolerability relative to MKIs are emphasized in trial updates and comparative analyses (wirth2024durabilityofresponse pages 2-3, braud2023comparativeeffectivenessof pages 2-4).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **RET** proto-oncogene is the causal gene for MEN2 (binter2024doesgenotypespecificphenotype pages 1-2).

**Open Targets disease–target mapping:** MEN2 (MONDO:0019003) is strongly associated with RET (west2025medullarythyroidcancer pages 13-14).

### 4.2 Pathogenic variants and classes
- MEN2A: enriched for extracellular cysteine-region variants (exons 10–11; codons 609/611/618/620/634) (binter2024doesgenotypespecificphenotype pages 2-4).
- MEN2B: most often RET **M918T** (binter2024doesgenotypespecificphenotype pages 2-4).
- Variant types are typically activating missense changes; a RET alteration database review (not prioritized by year) notes clustering in exons 10–11 and predominance of missense variants (tenore2025retgenealterations pages 14-16).

### 4.3 Somatic vs germline
In MTC, RET alterations can be germline (hereditary) or somatic (sporadic). A 2024 consensus statement notes ~75–80% of MTC are sporadic and ~50% of those harbor somatic RET variants (mete2024consensusstatementrecommendations pages 5-7).

### 4.4 Modifier genes / additional drivers
MTC biology can include additional alterations (e.g., RAS pathway changes), and the importance of non-RET factors for heterogeneity is discussed in recent MTC reviews (sahakian2023molecularbasisand pages 1-2). A 2024 MTC review further emphasizes that MTC is often driven by mutually exclusive **RET** or **RAS** alterations (papachristos2024medullarythyroidcancer pages 16-17).

---

## 5. Environmental Information
MEN2 is primarily genetic. No specific environmental, lifestyle, or infectious contributors were evidenced in the retrieved MEN2-focused sources.

---

## 6. Mechanism / Pathophysiology

### 6.1 RET signaling and downstream pathways
RET is a receptor tyrosine kinase activated by GDNF-family ligands with GFRα co-receptors; downstream signaling includes **MAPK** and **PI3K/AKT**, among other pathways (zhang2024moleculargeneticstherapeutics pages 2-5). RET-driven MTC features constitutive RET activation from point mutations that drive downstream pathway activation (RAS/MAPK, PI3K/AKT) (papachristos2024medullarythyroidcancer pages 10-12).

**Suggested GO biological process terms (examples)**
- Receptor tyrosine kinase signaling pathway: **GO:0007169** (suggested)
- MAPK cascade: **GO:0000165** (suggested)
- PI3K/AKT signaling: **GO:0014065** (suggested)

### 6.2 Immune microenvironment and immunotherapy considerations
MTC tends to have **low tumor mutational burden**, low neoantigen load, and reduced tumor visibility to the immune system, implying limited immunotherapy efficacy (papachristos2024medullarythyroidcancer pages 1-2, papachristos2024medullarythyroidcancer pages 12-13). Increased regulatory T cells and reduced MHC class II expression associated with poorer prognosis are among reported immune features (papachristos2024medullarythyroidcancer pages 16-17).

### 6.3 Resistance mechanisms to RET inhibition
Resistance emerges through:
- **On-target kinase mutations** (e.g., gatekeeper **RET V804M/L** and solvent-front **G810R/S/C**) that reduce inhibitor binding (papachristos2024medullarythyroidcancer pages 10-12)
- **Bypass/alternative pathway activation** (e.g., MET, KRAS) converging on MAPK/PI3K cascades (papachristos2024medullarythyroidcancer pages 10-12)
- Tumor microenvironment cytokine/chemokine-mediated effects that may modulate signaling and reduce TKI efficacy (papachristos2024medullarythyroidcancer pages 10-12).

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level
- Thyroid (parafollicular C cells → MTC) (binter2024doesgenotypespecificphenotype pages 1-2)
- Adrenal medulla (PCC)
- Parathyroid glands (PHPT)

**Suggested UBERON terms (examples)**
- Thyroid gland: **UBERON:0002046** (suggested)
- Adrenal gland: **UBERON:0002369** (suggested)
- Parathyroid gland: **UBERON:0002110** (suggested)

### 7.2 Cell level (suggested)
- Thyroid parafollicular cell (C cell): **CL:0000564** (suggested; MTC arises from C-cells) (binter2024doesgenotypespecificphenotype pages 1-2)
- Chromaffin cell: **CL:0000161** (suggested)
- Parathyroid chief cell: (ontology suggestion; not evidenced)

---

## 8. Temporal Development (natural history)
- MEN2 manifestations are genotype-dependent, affecting age of onset and surveillance decisions (binter2024doesgenotypespecificphenotype pages 2-4, mete2024consensusstatementrecommendations pages 2-3).
- Population-based PHPT penetrance increases with age (Figure 2) (holm2023primaryhyperparathyroidismin media 7f070ef5) and can recur decades after surgery (recurrence at 3, 13, and 20 years in the Danish cohort) (holm2023primaryhyperparathyroidismin pages 9-10).

---

## 9. Inheritance and Population

### 9.1 Inheritance
MEN2 is autosomal dominant (binter2024doesgenotypespecificphenotype pages 1-2).

### 9.2 Epidemiology
- A 2024 MEN2 cohort paper reports prevalence **1–9 per 100,000** (Orphanet ORPHA:653) (binter2024doesgenotypespecificphenotype pages 1-2).
- Population exome sequencing suggests RET pathogenic variant prevalence ~0.044% in UK Biobank (1 in 2500) and ~0.06% in Geisinger MyCode (1 in 1666), predominantly “moderate-risk” variants per ATA risk classification (west2025medullarythyroidcancer pages 3-5).

### 9.3 Founder effects
The Danish nationwide MEN2A PHPT analysis suggests findings may be influenced by a Danish **RET p.Cys611Tyr** founder effect (holm2023primaryhyperparathyroidismin pages 12-13).

---

## 10. Diagnostics

### 10.1 Biomarkers and laboratory tests (MTC-focused)
MTC is described as a neuroendocrine tumor that **secretes calcitonin and CEA** (carcinoembryonic antigen) (zhang2024moleculargeneticstherapeutics pages 1-2). (Detailed sensitivity/specificity statistics were not available in retrieved evidence.)

### 10.2 Genetic testing (current consensus)
A 2024 expert consensus statement on actionable biomarker testing recommends:
- **Constitutional (germline) RET testing at initial diagnosis** of MTC to identify familial MEN2 syndromes, including the fact that “up to ~10% of apparently sporadic MTC cases harbor de novo germline RET variants” (mete2024consensusstatementrecommendations pages 3-5).
- **Cascade testing** should be offered to relatives of individuals with germline RET pathogenic/likely pathogenic variants (mete2024consensusstatementrecommendations pages 5-7, mete2024consensusstatementrecommendations pages 8-10).
- If germline RET is positive, additional somatic testing is not required for RET-driven therapy selection (mete2024consensusstatementrecommendations pages 5-7).
- If germline RET is negative/VUS or unavailable, **tumor (somatic) RET testing is required** in advanced/metastatic/recurrent/inoperable disease to guide targeted therapy (mete2024consensusstatementrecommendations pages 5-7).

### 10.3 Somatic testing method considerations
For somatic RET detection, RNA-based NGS is preferred for fusions, while DNA-based NGS has moderate sensitivity (mete2024consensusstatementrecommendations pages 3-5). Although RET fusions are not the typical MEN2 mechanism, tumor profiling is relevant for treatment selection in advanced thyroid cancers (mete2024consensusstatementrecommendations pages 1-2).

---

## 11. Outcomes / Prognosis

### 11.1 MEN2A PHPT prognosis (population-based)
In the Danish MEN2A PHPT cohort:
- Cure after first surgery: **69%**
- Persistence: **8%**
- Recurrence: **23%** (including recurrences decades later)
- Permanent hypoparathyroidism after first parathyroid surgery: **46%** (holm2023primaryhyperparathyroidismin pages 9-10).

Figure evidence for penetrance and surgical outcome curves is available in the retrieved images (holm2023primaryhyperparathyroidismin media 7f070ef5, holm2023primaryhyperparathyroidismin media 6891f0e9).

### 11.2 Advanced RET-mutant MTC prognosis under selective RET inhibition
In LIBRETTO-001 (long-term follow-up), median PFS was **not reached** in cabozantinib/vandetanib-naïve MTC and **41.4 months** in previously treated MTC; 3-year PFS was **75.2%** (naïve) and **54.6%** (pretreated) (data cutoff Jan 13, 2023) (wirth2024durabilityofresponse pages 2-3).

---

## 12. Treatment

### 12.1 Surgery and interventional management (core MEN2 implementation)
- MTC primary therapy: surgery (thyroidectomy) is emphasized as curative in early disease (lagana2023theevolvingtreatment pages 1-3).
- PHPT: selective or subtotal parathyroidectomy strategies and long-term recurrence monitoring are important (holm2023primaryhyperparathyroidismin pages 9-10).

**Suggested MAXO terms (examples)**
- Thyroidectomy: **MAXO:0001212** (suggested)
- Parathyroidectomy: **MAXO:0000587** (suggested)
- Adrenalectomy (for PCC): **MAXO:0000747** (suggested)

### 12.2 Targeted systemic therapy for advanced MTC
#### Selective RET inhibitor: selpercatinib (LIBRETTO-001)
LIBRETTO-001 long-term update (JCO, Sep 2024; data cutoff Jan 13, 2023) reported durable efficacy in RET-mutant MTC:
- ORR **82.5%** in cabozantinib/vandetanib-naïve MTC; ORR **77.6%** in MKI-pretreated MTC (wirth2024durabilityofresponse pages 1-2).
- Median PFS: **not reached** (naïve) and **41.4 months** (pretreated) (wirth2024durabilityofresponse pages 2-3).

**Direct abstract-quotable statement (trial update abstract):** “At the data cutoff of January 2023, the objective response rate was 82.5% among patients with cabozantinib/vandetanib-naïve MTC…” (wirth2024durabilityofresponse pages 1-2).

#### Phase 3 comparative evidence: selpercatinib vs MKIs (LIBRETTO-531)
A LIBRETTO-001 comparative analysis paper reports interim phase 3 LIBRETTO-531 PFS results: median PFS **not reached** for selpercatinib vs **16.8 months** for cabozantinib/vandetanib, HR **0.28** (95% CI 0.16–0.48; p<0.001) (braud2023comparativeeffectivenessof pages 2-4).

#### Real-world implementation: actionable biomarker testing
Consensus guidance frames RET testing as integral to MTC treatment selection and family management, i.e., germline testing for all MTC and somatic testing when germline is negative/VUS/pending in advanced disease (mete2024consensusstatementrecommendations pages 3-5, mete2024consensusstatementrecommendations pages 5-7).

#### Multi-kinase inhibitors (MKIs)
MKI options include vandetanib and cabozantinib for advanced MTC; they improve PFS but have off-target toxicities and limited OS benefit in reviewed sources (zhang2024moleculargeneticstherapeutics pages 1-2).

---

## 13. Prevention

### 13.1 Primary/secondary prevention in MEN2
Core prevention is **genotype-guided early intervention**:
- Identification of RET carriers via germline testing at MTC diagnosis and cascade testing in relatives (mete2024consensusstatementrecommendations pages 5-7).
- Prophylactic/early thyroid surgery timing is guided by genotype/ATA risk groups (lagana2023theevolvingtreatment pages 1-3, mete2024consensusstatementrecommendations pages 2-3).

---

## 14. Other Species / Natural Disease
No other-species natural disease evidence was retrieved in the current evidence set.

---

## 15. Model Organisms
No model organism studies were retrieved in the current evidence set (e.g., RET transgenic mouse MEN2 models). This is a limitation of the current retrieval.

---

## Visual evidence (retrieved figures/tables)
- Age-related penetrance of PHPT (Figure 2) and surgical outcome curve(s) are present in the Holm et al. nationwide MEN2A cohort paper (holm2023primaryhyperparathyroidismin media 7f070ef5, holm2023primaryhyperparathyroidismin media 6891f0e9).
- Patient-level clinical table(s) for PHPT cases (Table 1) were also retrieved as images (holm2023primaryhyperparathyroidismin media 2ec34948, holm2023primaryhyperparathyroidismin media 6ce0a3fe).

---

## Key recent references (URLs and dates)
- Mete et al. **Consensus Statement: Recommendations on Actionable Biomarker Testing for Thyroid Cancer Management**. *Endocrine Pathology*. **Nov 2024**. https://doi.org/10.1007/s12022-024-09836-x (mete2024consensusstatementrecommendations pages 3-5)
- Binter et al. **Does Genotype-Specific Phenotype in Patients with MEN2 Occur as Current Guidelines Predict?** *Cancers*. **Jan 2024**. https://doi.org/10.3390/cancers16030494 (binter2024doesgenotypespecificphenotype pages 1-2)
- Wirth et al. **Durability of response with selpercatinib… LIBRETTO-001**. *Journal of Clinical Oncology*. **Sep 2024**. https://doi.org/10.1200/JCO.23.02503 (wirth2024durabilityofresponse pages 1-2)
- Holm et al. **PHPT in MEN2A in Denmark 1930–2021**. *Cancers*. **Apr 2023**. https://doi.org/10.3390/cancers15072125 (holm2023primaryhyperparathyroidismin pages 1-2)

---

## Limitations of this report (evidence gaps)
- ICD-10/ICD-11 and MeSH identifiers, MEN2B extra-endocrine phenotype frequencies, detailed PCC epidemiology, and model organism evidence were not directly available in the retrieved evidence set.
- Several statements (e.g., HPO/GO/UBERON/MAXO IDs) are provided as **ontology suggestions** and should be verified against the relevant ontology browser for exact term IDs and labels.
- PMID-level citations could not be reliably provided because PMIDs were not included in the retrieved snippets for most sources; DOIs/URLs are provided instead.


References

1. (binter2024doesgenotypespecificphenotype pages 1-2): Teresa Binter, Sabina Baumgartner-Parzer, Marie Helene Schernthaner-Reiter, Melisa Arikan, Lindsay Hargitai, Martin Bruno Niederle, Bruno Niederle, Christian Scheuba, and Philipp Riss. Does genotype-specific phenotype in patients with multiple endocrine neoplasia type 2 occur as current guidelines predict? Cancers, 16:494, Jan 2024. URL: https://doi.org/10.3390/cancers16030494, doi:10.3390/cancers16030494. This article has 11 citations.

2. (binter2024doesgenotypespecificphenotype pages 2-4): Teresa Binter, Sabina Baumgartner-Parzer, Marie Helene Schernthaner-Reiter, Melisa Arikan, Lindsay Hargitai, Martin Bruno Niederle, Bruno Niederle, Christian Scheuba, and Philipp Riss. Does genotype-specific phenotype in patients with multiple endocrine neoplasia type 2 occur as current guidelines predict? Cancers, 16:494, Jan 2024. URL: https://doi.org/10.3390/cancers16030494, doi:10.3390/cancers16030494. This article has 11 citations.

3. (mete2024consensusstatementrecommendations pages 3-5): Ozgur Mete, Andrée Boucher, Kasmintan A. Schrader, Omar Abdel-Rahman, Houda Bahig, Cheryl Ho, Olfat Kamel Hasan, Bernard Lemieux, Eric Winquist, Ralph Wong, Jonn Wu, Nicole Chau, and Shereen Ezzat. Consensus statement: recommendations on actionable biomarker testing for thyroid cancer management. Endocrine Pathology, 35:293-308, Nov 2024. URL: https://doi.org/10.1007/s12022-024-09836-x, doi:10.1007/s12022-024-09836-x. This article has 28 citations and is from a peer-reviewed journal.

4. (wirth2024durabilityofresponse pages 1-2): Lori J. Wirth, Marcia S. Brose, Vivek Subbiah, Francis Worden, Ben Solomon, Bruce Robinson, Julien Hadoux, Pascale Tomasini, Daniela Weiler, Barbara Deschler-Baier, Daniel S.W. Tan, Patricia Maeda, Yan Lin, Ravinder Singh, Theresa Bayt, Alexander Drilon, and Philippe A. Cassier. Durability of response with selpercatinib in patients with <i>ret</i>-activated thyroid cancer: long-term safety and efficacy from libretto-001. Journal of Clinical Oncology, 42:3187-3195, Sep 2024. URL: https://doi.org/10.1200/jco.23.02503, doi:10.1200/jco.23.02503. This article has 39 citations and is from a highest quality peer-reviewed journal.

5. (west2025medullarythyroidcancer pages 13-14): Courtney E. West, Uyenlinh L. Mirshahi, Katherine S. Ruth, Luke N. Sharp, Ankit M. Arni, Clare Turnbull, Caroline F. Wright, Bijay Vaidya, Martina M. Owens, David J. Carey, and Kashyap A. Patel. Medullary thyroid cancer risk and mortality in carriers of incidentally identified men2a <i>ret</i> variants. JAMA Network Open, 8:e2517937, Jun 2025. URL: https://doi.org/10.1001/jamanetworkopen.2025.17937, doi:10.1001/jamanetworkopen.2025.17937. This article has 8 citations and is from a peer-reviewed journal.

6. (holm2023primaryhyperparathyroidismin pages 1-2): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.

7. (sahakian2023molecularbasisand pages 1-2): Nicolas Sahakian, Frédéric Castinetti, and Pauline Romanet. Molecular basis and natural history of medullary thyroid cancer: it is (almost) all in the ret. Cancers, 15:4865, Oct 2023. URL: https://doi.org/10.3390/cancers15194865, doi:10.3390/cancers15194865. This article has 21 citations.

8. (west2025medullarythyroidcancer pages 1-2): Courtney E. West, Uyenlinh L. Mirshahi, Katherine S. Ruth, Luke N. Sharp, Ankit M. Arni, Clare Turnbull, Caroline F. Wright, Bijay Vaidya, Martina M. Owens, David J. Carey, and Kashyap A. Patel. Medullary thyroid cancer risk and mortality in carriers of incidentally identified men2a <i>ret</i> variants. JAMA Network Open, 8:e2517937, Jun 2025. URL: https://doi.org/10.1001/jamanetworkopen.2025.17937, doi:10.1001/jamanetworkopen.2025.17937. This article has 8 citations and is from a peer-reviewed journal.

9. (west2025medullarythyroidcancer pages 3-5): Courtney E. West, Uyenlinh L. Mirshahi, Katherine S. Ruth, Luke N. Sharp, Ankit M. Arni, Clare Turnbull, Caroline F. Wright, Bijay Vaidya, Martina M. Owens, David J. Carey, and Kashyap A. Patel. Medullary thyroid cancer risk and mortality in carriers of incidentally identified men2a <i>ret</i> variants. JAMA Network Open, 8:e2517937, Jun 2025. URL: https://doi.org/10.1001/jamanetworkopen.2025.17937, doi:10.1001/jamanetworkopen.2025.17937. This article has 8 citations and is from a peer-reviewed journal.

10. (mete2024consensusstatementrecommendations pages 2-3): Ozgur Mete, Andrée Boucher, Kasmintan A. Schrader, Omar Abdel-Rahman, Houda Bahig, Cheryl Ho, Olfat Kamel Hasan, Bernard Lemieux, Eric Winquist, Ralph Wong, Jonn Wu, Nicole Chau, and Shereen Ezzat. Consensus statement: recommendations on actionable biomarker testing for thyroid cancer management. Endocrine Pathology, 35:293-308, Nov 2024. URL: https://doi.org/10.1007/s12022-024-09836-x, doi:10.1007/s12022-024-09836-x. This article has 28 citations and is from a peer-reviewed journal.

11. (lagana2023theevolvingtreatment pages 1-3): Marta Laganà, Valentina Cremaschi, Andrea Alberti, Danica M. Vodopivec Kuri, Deborah Cosentini, and Alfredo Berruti. The evolving treatment landscape of medullary thyroid cancer. Current Treatment Options in Oncology, 24:1815-1832, Nov 2023. URL: https://doi.org/10.1007/s11864-023-01145-5, doi:10.1007/s11864-023-01145-5. This article has 14 citations and is from a peer-reviewed journal.

12. (zhang2024moleculargeneticstherapeutics pages 1-2): Ying Zhang, Wei-Hui Zheng, Shi-Hong Zhou, Jia-Lei Gu, Qing Yu, Yi-Zhou Zhu, Yu-Jie Yan, Zhi Zhu, and Jin-Biao Shang. Molecular genetics, therapeutics and ret inhibitor resistance for medullary thyroid carcinoma and future perspectives. Cell Communication and Signaling : CCS, Sep 2024. URL: https://doi.org/10.1186/s12964-024-01837-x, doi:10.1186/s12964-024-01837-x. This article has 18 citations.

13. (holm2023primaryhyperparathyroidismin pages 4-7): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.

14. (holm2023primaryhyperparathyroidismin media 7f070ef5): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.

15. (holm2023primaryhyperparathyroidismin pages 9-10): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.

16. (wirth2024durabilityofresponse pages 2-3): Lori J. Wirth, Marcia S. Brose, Vivek Subbiah, Francis Worden, Ben Solomon, Bruce Robinson, Julien Hadoux, Pascale Tomasini, Daniela Weiler, Barbara Deschler-Baier, Daniel S.W. Tan, Patricia Maeda, Yan Lin, Ravinder Singh, Theresa Bayt, Alexander Drilon, and Philippe A. Cassier. Durability of response with selpercatinib in patients with <i>ret</i>-activated thyroid cancer: long-term safety and efficacy from libretto-001. Journal of Clinical Oncology, 42:3187-3195, Sep 2024. URL: https://doi.org/10.1200/jco.23.02503, doi:10.1200/jco.23.02503. This article has 39 citations and is from a highest quality peer-reviewed journal.

17. (braud2023comparativeeffectivenessof pages 2-4): Filippo De Braud, Barbara Deschler-Baier, John C. Morris, Francis Worden, Yimei Han, Urpo Kiiskinen, Min-Hua Jen, Scott S. Barker, Sylwia Szymczak, and Adrienne M. Gilligan. Comparative effectiveness of first-line selpercatinib versus standard therapies in patients with ret-activated cancers: an exploratory interpatient analysis of libretto-001. Cancers, 16:140, Dec 2023. URL: https://doi.org/10.3390/cancers16010140, doi:10.3390/cancers16010140. This article has 3 citations.

18. (tenore2025retgenealterations pages 14-16): Claudio Ricciardi Tenore, Eugenia Tulli, Alessia Perrucci, Roberto Bertozzi, Ludovica Fortuna, Giulia Maneri, Concetta Santonocito, Andrea Urbani, Maria De Bonis, and Angelo Minucci. Ret gene alterations in clinical practice: a comprehensive review and database update. Genes, 16:1472, Dec 2025. URL: https://doi.org/10.3390/genes16121472, doi:10.3390/genes16121472. This article has 1 citations.

19. (mete2024consensusstatementrecommendations pages 5-7): Ozgur Mete, Andrée Boucher, Kasmintan A. Schrader, Omar Abdel-Rahman, Houda Bahig, Cheryl Ho, Olfat Kamel Hasan, Bernard Lemieux, Eric Winquist, Ralph Wong, Jonn Wu, Nicole Chau, and Shereen Ezzat. Consensus statement: recommendations on actionable biomarker testing for thyroid cancer management. Endocrine Pathology, 35:293-308, Nov 2024. URL: https://doi.org/10.1007/s12022-024-09836-x, doi:10.1007/s12022-024-09836-x. This article has 28 citations and is from a peer-reviewed journal.

20. (papachristos2024medullarythyroidcancer pages 16-17): Alexander J. Papachristos, Hazel Serrao-Brown, Anthony J. Gill, Roderick Clifton-Bligh, and Stanley B. Sidhu. Medullary thyroid cancer: molecular drivers and immune cellular milieu of the tumour microenvironment—implications for systemic treatment. Cancers, 16:2296, Jun 2024. URL: https://doi.org/10.3390/cancers16132296, doi:10.3390/cancers16132296. This article has 4 citations.

21. (zhang2024moleculargeneticstherapeutics pages 2-5): Ying Zhang, Wei-Hui Zheng, Shi-Hong Zhou, Jia-Lei Gu, Qing Yu, Yi-Zhou Zhu, Yu-Jie Yan, Zhi Zhu, and Jin-Biao Shang. Molecular genetics, therapeutics and ret inhibitor resistance for medullary thyroid carcinoma and future perspectives. Cell Communication and Signaling : CCS, Sep 2024. URL: https://doi.org/10.1186/s12964-024-01837-x, doi:10.1186/s12964-024-01837-x. This article has 18 citations.

22. (papachristos2024medullarythyroidcancer pages 10-12): Alexander J. Papachristos, Hazel Serrao-Brown, Anthony J. Gill, Roderick Clifton-Bligh, and Stanley B. Sidhu. Medullary thyroid cancer: molecular drivers and immune cellular milieu of the tumour microenvironment—implications for systemic treatment. Cancers, 16:2296, Jun 2024. URL: https://doi.org/10.3390/cancers16132296, doi:10.3390/cancers16132296. This article has 4 citations.

23. (papachristos2024medullarythyroidcancer pages 1-2): Alexander J. Papachristos, Hazel Serrao-Brown, Anthony J. Gill, Roderick Clifton-Bligh, and Stanley B. Sidhu. Medullary thyroid cancer: molecular drivers and immune cellular milieu of the tumour microenvironment—implications for systemic treatment. Cancers, 16:2296, Jun 2024. URL: https://doi.org/10.3390/cancers16132296, doi:10.3390/cancers16132296. This article has 4 citations.

24. (papachristos2024medullarythyroidcancer pages 12-13): Alexander J. Papachristos, Hazel Serrao-Brown, Anthony J. Gill, Roderick Clifton-Bligh, and Stanley B. Sidhu. Medullary thyroid cancer: molecular drivers and immune cellular milieu of the tumour microenvironment—implications for systemic treatment. Cancers, 16:2296, Jun 2024. URL: https://doi.org/10.3390/cancers16132296, doi:10.3390/cancers16132296. This article has 4 citations.

25. (holm2023primaryhyperparathyroidismin pages 12-13): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.

26. (mete2024consensusstatementrecommendations pages 8-10): Ozgur Mete, Andrée Boucher, Kasmintan A. Schrader, Omar Abdel-Rahman, Houda Bahig, Cheryl Ho, Olfat Kamel Hasan, Bernard Lemieux, Eric Winquist, Ralph Wong, Jonn Wu, Nicole Chau, and Shereen Ezzat. Consensus statement: recommendations on actionable biomarker testing for thyroid cancer management. Endocrine Pathology, 35:293-308, Nov 2024. URL: https://doi.org/10.1007/s12022-024-09836-x, doi:10.1007/s12022-024-09836-x. This article has 28 citations and is from a peer-reviewed journal.

27. (mete2024consensusstatementrecommendations pages 1-2): Ozgur Mete, Andrée Boucher, Kasmintan A. Schrader, Omar Abdel-Rahman, Houda Bahig, Cheryl Ho, Olfat Kamel Hasan, Bernard Lemieux, Eric Winquist, Ralph Wong, Jonn Wu, Nicole Chau, and Shereen Ezzat. Consensus statement: recommendations on actionable biomarker testing for thyroid cancer management. Endocrine Pathology, 35:293-308, Nov 2024. URL: https://doi.org/10.1007/s12022-024-09836-x, doi:10.1007/s12022-024-09836-x. This article has 28 citations and is from a peer-reviewed journal.

28. (holm2023primaryhyperparathyroidismin media 6891f0e9): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.

29. (holm2023primaryhyperparathyroidismin media 2ec34948): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.

30. (holm2023primaryhyperparathyroidismin media 6ce0a3fe): Magnus Holm, Peter Vestergaard, Morten Poulsen, Åse Rasmussen, Ulla Feldt-Rasmussen, Mette Bay, Lars Rolighed, Stefano Londero, Henrik Pedersen, Christoffer Hahn, Klara Rask, Heidi Nielsen, Mette Gaustadnes, Maria Rossing, Anne Hermann, Christian Godballe, and Jes Mathiesen. Primary hyperparathyroidism in multiple endocrine neoplasia type 2a in denmark 1930–2021: a nationwide population-based retrospective study. Cancers, 15:2125, Apr 2023. URL: https://doi.org/10.3390/cancers15072125, doi:10.3390/cancers15072125. This article has 22 citations.
