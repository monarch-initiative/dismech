---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T17:32:53.792604'
end_time: '2026-04-05T17:41:43.774618'
duration_seconds: 529.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma** covering all of the
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
- **Disease Name:** IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma** covering all of the
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


## Comprehensive Research Report: IDH‑Mutant and 1p/19q‑Codeleted Oligodendroglioma

### Target Disease
- **Disease name (WHO CNS5):** *Oligodendroglioma, IDH-mutant and 1p/19q-codeleted* (louis2021the2021who pages 8-9, louis2021the2021who pages 6-8)
- **Category:** Adult-type diffuse glioma (central nervous system tumor) (horbinski2022clinicalimplicationsof pages 1-2, komori2023updateofthe pages 1-2)
- **MONDO ID:** Not directly retrievable in the provided evidence for this *exact* WHO CNS5 entity. Closest related disease terms in retrieved structured resources include **MONDO_0002543 (adult oligodendroglioma)** and **EFO_0000632 (oligodendroglioma)** (ahmad2024idhmutationglioma pages 7-8).

---

## 1. Disease Information

### 1.1 Concise overview
In the 2021 WHO Classification of Tumours of the Central Nervous System (WHO CNS5), *oligodendroglioma* is defined as an adult-type diffuse glioma that is **molecularly defined** by an **IDH1/IDH2 mutation** together with **whole-arm 1p/19q codeletion**, and is graded as **CNS WHO grade 2 or grade 3** within the tumor type (louis2021the2021who pages 8-9, louis2021the2021who pages 6-8, komori2023updateofthe pages 1-2).

### 1.2 Key identifiers and controlled vocabularies
- **WHO entity name:** *Oligodendroglioma, IDH-mutant and 1p/19q-codeleted* (louis2021the2021who pages 8-9).
- **WHO grade range:** CNS WHO grade **2 or 3** (louis2021the2021who pages 8-9, louis2021the2021who pages 9-10).
- **Ontology / database identifiers:** Not comprehensively retrievable from the available sources in this run (e.g., ICD-10/ICD-11, MeSH, Orphanet, OMIM, disease-specific MONDO for the exact entity).

### 1.3 Synonyms and alternative names
- Historical terminology: “oligodendroglioma” and “anaplastic oligodendroglioma” roughly correspond to WHO grade 2 and grade 3 tumors, respectively, but WHO CNS5 emphasizes molecularly defined integrated diagnoses (louis2021the2021who pages 8-9, roux2020imaginggrowthas pages 7-7).
- Legacy mixed-histology term **“oligoastrocytoma”** is deprecated in modern practice because most such cases resolve into astrocytoma vs oligodendroglioma on molecular testing (horbinski2022clinicalimplicationsof pages 1-2).

### 1.4 Evidence source type
The classification statements summarized here are **aggregated, disease-level resources** (WHO CNS5 summaries and implementation reviews), supplemented by clinical trials and cohort studies (horbinski2022clinicalimplicationsof pages 1-2, louis2021the2021who pages 8-9).

---

## 2. Etiology

### 2.1 Disease causal factors (genetic/mechanistic)
- **Founder event:** IDH1/IDH2 gain-of-function (neomorphic) mutation leading to 2-hydroxyglutarate (2-HG) accumulation and epigenetic remodeling (DNA/histone hypermethylation) (martin2023fromtheoryto pages 1-2, carosi2024targetingisocitratedehydrogenase pages 3-4).
- **Definitional chromosomal event:** Whole-arm **1p/19q codeletion** in the setting of IDH mutation defines oligodendroglioma in WHO CNS5 (martin2023fromtheoryto pages 2-4, louis2021the2021who pages 6-8).

### 2.2 Risk factors
- **Genetic/molecular trajectory:** In WHO CNS5-aligned reviews, IDH-mutant diffuse gliomas follow two broad molecular trajectories: (i) IDH + TP53/ATRX (astrocytic), vs (ii) IDH + whole-arm 1p/19q codeletion + TERT promoter mutation (oligodendroglial; generally more favorable) (reuss2023updatesonthe pages 1-2).
- **Epidemiologic modifiers:** Age is a key demographic correlate (typical adult onset; see Epidemiology), but robust environmental risk factors were not retrievable in the evidence assembled for this run.

### 2.3 Protective factors / gene–environment interactions
No high-quality, disease-specific protective factors or gene–environment interaction evidence was retrieved in the assembled corpus for this run.

---

## 3. Phenotypes (Clinical Presentation)

### 3.1 Typical symptom complex
Clinical presentation is often insidious and related to lesion location and intracranial pressure (antonelli2022adulttypediffuse pages 4-6). Across neuroradiology-focused WHO CNS5 reviews:
- **Seizures** are frequently the initial symptom, plausibly due to cortical involvement (gue2024the2021world pages 7-9).
- Other common symptoms include **headache** and **cognitive/personality changes** (notably with frontal lobe involvement) (gue2024the2021world pages 7-9).

### 3.2 Phenotype characteristics (onset, progression, frequency)
- **Age of onset:** commonly adult (often third to fifth decades) (gue2024the2021world pages 7-9).
- **Progression:** infiltrative growth is typical; malignant progression/grade transformation can occur over time (see Temporal Development) (roux2020imaginggrowthas pages 7-7).

### 3.3 Quality of life impact
High-quality, phenotype-specific QoL effect size estimates for *this exact entity* were not retrieved in this run. However, the long expected survival in many patients makes late treatment toxicity and “quality of survival” a major concern in treatment strategy discussions (carosi2024targetingisocitratedehydrogenase pages 4-6).

### 3.4 Suggested HPO terms (examples)
- Seizures: **HP:0001250**
- Headache: **HP:0002315**
- Cognitive impairment: **HP:0100543**
- Personality change: **HP:0000751**

---

## 4. Genetic/Molecular Information

### 4.1 Causal/definitional alterations
WHO CNS5 defines oligodendroglioma as requiring:
- **IDH1 or IDH2 mutation**, and
- **Whole-arm 1p/19q codeletion** (martin2023fromtheoryto pages 2-4, louis2021the2021who pages 6-8).

### 4.2 Common additional (characteristic) alterations
WHO-aligned molecular summaries list recurrent alterations in oligodendroglioma including **TERT promoter**, **CIC**, **FUBP1**, and **NOTCH1** (martin2023fromtheoryto pages 4-6, louis2021the2021who pages 6-8).

### 4.3 Variant types and testing implications
- **IDH mutations** are typically **missense hotspot variants** (e.g., IDH1 R132H is common; non-canonical IDH variants may require sequencing when IHC is negative but suspicion remains) (martin2023fromtheoryto pages 2-4, martin2023fromtheoryto pages 1-2).
- Whole-arm **1p/19q codeletion** is a **structural/copy-number alteration**, classically arising from an unbalanced translocation (conceptually consistent with modern diagnostic descriptions) and must be interpreted as **whole-arm** rather than partial loss (ball2020frequencyoffalsepositive pages 1-2).

### 4.4 Epigenetic information
- IDH neomorphic activity and 2-HG accumulation are linked to **DNA and histone hypermethylation** and the glioma CpG island methylator phenotype (G‑CIMP) (martin2023fromtheoryto pages 1-2, carosi2024targetingisocitratedehydrogenase pages 3-4).

---

## 5. Environmental Information
No robust disease-specific environmental, lifestyle, or infectious causal factors were retrieved in the evidence assembled for this run.

---

## 6. Mechanism / Pathophysiology

### 6.1 Core causal chain (current understanding)
1. **IDH1/2 neomorphic mutation** produces the oncometabolite **2-HG** (martin2023fromtheoryto pages 1-2, carosi2024targetingisocitratedehydrogenase pages 3-4).
2. 2-HG competitively inhibits α-KG–dependent dioxygenases (e.g., TET/Jumonji demethylases), causing **DNA/histone hypermethylation** and an epigenetically constrained cellular state (carosi2024targetingisocitratedehydrogenase pages 3-4).
3. In IDH-mutant gliomas, this is linked to **blocked differentiation programs** and maintenance of an OPC-like developmental state (wei2023stalledoligodendrocytedifferentiation pages 1-2).

### 6.2 Differentiation blockade and cell-of-origin programs (2023 evidence)
A 2023 Genome Medicine multi-omic analysis concludes that IDH-mutant gliomas resemble early oligodendrocyte lineage states and show a **blocked myelination program**, supported by DNA methylation and chromatin accessibility patterns (wei2023stalledoligodendrocytedifferentiation pages 1-2).

### 6.3 Immune microenvironment effects (2024 evidence)
- Reviews describe a mechanistic axis in which IDH-mutant tumors exhibit reduced immunogenicity and immune suppression linked to 2-HG and downstream epigenetic state; one review explicitly notes that **“high levels of D-2-HG in the interstitial fluid of tumor cells”** can impair T-cell proliferation and cytotoxicity (carosi2024targetingisocitratedehydrogenase pages 3-4).
- A 2024 systematic review emphasizes immune suppression in IDH-mutant gliomas and highlights downstream consequences relevant to checkpoint blockade response (ahmad2024idhmutationglioma pages 1-2, ahmad2024idhmutationglioma pages 7-8).

### 6.4 Suggested ontology terms
- **GO biological process (examples):** DNA methylation, histone methylation, glial cell differentiation, oligodendrocyte differentiation, T cell proliferation.
- **CL cell types (examples):** oligodendrocyte progenitor cell (OPC), oligodendrocyte, microglial cell, T cell.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- Primary organ: **brain** (central nervous system).
- Predilection for **supratentorial cerebral hemispheres**, especially **frontal lobe** (~60% reported in one WHO-aligned review), followed by temporal/parietal; occipital is less common; midline/posterior fossa/spinal are rare (antonelli2022adulttypediffuse pages 4-6, martin2023fromtheoryto pages 4-6).

### 7.2 Tissue/cell level
- Tumor is a **diffusely infiltrating glioma** involving **cortex and subcortical white matter** (gue2024the2021world pages 7-9, martin2023fromtheoryto pages 4-6).

### 7.3 Suggested UBERON terms (examples)
- Cerebral cortex; frontal lobe; cerebral white matter.

---

## 8. Temporal Development (Natural History)

### 8.1 Onset pattern
Often **insidious** presentation in adults (gue2024the2021world pages 7-9).

### 8.2 Progression and grading
- WHO CNS5 recognizes grading within the entity: **CNS WHO grade 2 and grade 3** oligodendroglioma (louis2021the2021who pages 8-9, louis2021the2021who pages 9-10).
- Traditional grade 3 (“anaplastic”) criteria in earlier WHO frameworks incorporate brisk mitotic activity and/or microvascular proliferation; one study cites a cutoff of **≥6 mitoses per 10 high-power fields** and highlights that imaging growth rate may capture aggressiveness and predict progression-free survival (roux2020imaginggrowthas pages 7-7).

---

## 9. Inheritance and Population

### 9.1 Inheritance
This tumor entity is primarily considered **sporadic** in routine clinical neuro-oncology practice; heritable Mendelian patterns were not supported by retrieved evidence in this run.

### 9.2 Epidemiology and demographics
A WHO CNS5 implementation review reports:
- **Incidence:** approximately **0.48 per 100,000**.
- **Age:** peak in **fourth–fifth decades**.
- **Median overall survival:** approximately **10–17 years** (reflecting grade and treatment heterogeneity) (martin2023fromtheoryto pages 4-6).

---

## 10. Diagnostics

### 10.1 Integrated diagnostic criteria (WHO CNS5-aligned workflow)
A practical diagnostic workflow for adult diffuse gliomas is:
1. Test for **IDH1/2** (IHC for IDH1 R132H and/or sequencing).
2. In IDH-mutant tumors, assess **ATRX**: loss supports astrocytoma; retained ATRX prompts 1p/19q testing.
3. If **whole-arm 1p/19q codeletion** is present, diagnose **oligodendroglioma, IDH-mutant and 1p/19q-codeleted** (martin2023fromtheoryto pages 2-4).

### 10.2 Key molecular tests and platforms
- IDH: IHC (IDH1 R132H) and/or sequencing (martin2023fromtheoryto pages 2-4).
- 1p/19q: FISH, chromosomal microarray (CMA), methylation array–derived copy number, or NGS-based copy-number approaches (martin2023fromtheoryto pages 4-6).

### 10.3 Important diagnostic caveat: false-positive FISH for 1p/19q
Because FISH is locus-based, it may not distinguish **partial** from **whole-arm** losses, producing “false-positive” 1p/19q results when partial losses mimic codeletion (ball2020frequencyoffalsepositive pages 1-2). In an adult diffuse astrocytic glioma series, the estimated false-positive FISH rate was **3.6% (8/223)**, with similar rates in IDH-mutant vs IDH-wildtype tumors (ball2020frequencyoffalsepositive pages 2-2). The authors recommend selective testing and/or confirmation with whole-arm–resolving platforms such as CMA when morphology/molecular context is discordant (ball2020frequencyoffalsepositive pages 2-2, ball2020frequencyoffalsepositive pages 13-14).

### 10.4 Imaging features used in real-world workflows (radiology)
Common imaging features reported across WHO-2021 radiology reviews include:
- **Location:** frontal lobe predilection; cortical/subcortical involvement (gue2024the2021world pages 7-9, antonelli2022adulttypediffuse pages 4-6).
- **CT:** hypodense/isodense lesion; **calcifications are common** (reported ~90% in one review) (martin2023fromtheoryto pages 4-6).
- **MRI:** typically **T1 hypointense**, **T2 hyperintense**, often heterogeneous with indistinct margins (gue2024the2021world pages 9-12).
- **Contrast enhancement:** variable; one review reports enhancement in **<20% of grade 2** but **>70% of grade 3** oligodendrogliomas (gue2024the2021world pages 9-12).
- **Perfusion:** may show elevated rCBV reflecting vascularity (antonelli2022adulttypediffuse pages 4-6).

---

## 11. Outcome / Prognosis

### 11.1 Prognosis and survival statistics from pivotal trials (anaplastic/grade 3; codeleted)
Long-term randomized trial evidence (RTOG 9402 and EORTC 26951) demonstrates substantial benefit from adding PCV chemotherapy to radiotherapy in 1p/19q-codeleted anaplastic oligodendroglial tumors, with median OS on the order of a decade or longer and durable long-term survivors.

Key statistics include:
- **RTOG 9402 (JCO 2013):** in codeleted tumors, **median OS 14.7 years** with PCV+RT vs **7.3 years** with RT alone (HR 0.59; P=0.03) (cairncross2013phaseiiitrial pages 1-2).
- **Joint final report (JCO 2022):** in the codeleted subgroup, probable **20-year OS ~37%** with PCV+RT versus ~15% without PCV in RTOG 9402; and ~37% with PCV versus ~14% without PCV in EORTC 26951 (lassman2022jointfinalreport pages 1-2). The Kaplan–Meier curves and numbers-at-risk are shown in Figure 2 (lassman2022jointfinalreport media 697c589d).

### 11.2 Prognostic biomarkers (selected)
- **1p/19q codeletion** is strongly associated with improved outcomes relative to non-codeleted gliomas in the major randomized trial datasets (bent2013adjuvantprocarbazinelomustine pages 2-3, cairncross2013phaseiiitrial pages 1-2).
- Epigenetic classifiers and additional CNV/alterations can stratify prognosis in IDH-mutant gliomas generally, but oligodendroglioma-specific prognostic molecular modeling was not deeply retrievable in this run.

---

## 12. Treatment

### 12.1 Standard-of-care components and real-world implementations
- **Maximal safe surgical resection** followed by risk-adapted adjuvant therapy and MRI surveillance is a common backbone approach in guideline-aligned care pathways (carosi2024targetingisocitratedehydrogenase pages 4-6).
- For grade 3 / anaplastic, randomized data support **radiotherapy + PCV chemotherapy** as a standard option in 1p/19q-codeleted tumors (lassman2022jointfinalreport pages 1-2, cairncross2013phaseiiitrial pages 1-2).

### 12.2 Temozolomide vs RT-containing regimens (evolving practice)
The initial CODEL trial design analysis showed **inferior PFS with temozolomide alone** compared with RT-containing regimens in newly diagnosed 1p/19q-codeleted grade 3 oligodendroglioma (jaeckle2021codelphaseiii pages 1-2). This led to redesign of CODEL to compare RT+PCV vs RT+TMZ rather than including a TMZ-only arm (jaeckle2021codelphaseiii pages 1-2, jaeckle2021codelphaseiii pages 9-10).

### 12.3 Targeted therapy (major 2023 development): IDH inhibitor vorasidenib
A major recent advance is the phase 3 **INDIGO** trial of **vorasidenib** in post-surgical residual/recurrent **grade 2 IDH-mutant glioma** (including oligodendroglioma and astrocytoma, stratified by 1p/19q status) (mellinghoff2023vorasidenibinidh1 pages 3-5).

Direct abstract quote supporting the key efficacy claim:
- “**Progression-free survival was significantly improved in the vorasidenib group as compared with the placebo group (median progression-free survival, 27.7 months vs. 11.1 months; hazard ratio … 0.39 …; P<0.001).**” (mellinghoff2023vorasidenibinidh1 pages 1-3)

Safety signal of note:
- Grade ≥3 ALT elevation occurred in **9.6%** on vorasidenib vs **0%** on placebo (mellinghoff2023vorasidenibinidh1 pages 16-18).

### 12.4 Suggested MAXO terms (examples)
- Surgical tumor resection; external beam radiotherapy; chemotherapy with procarbazine/lomustine/vincristine; chemotherapy with temozolomide; targeted therapy with IDH inhibitor.

---

## 13. Prevention
Primary prevention and population-level screening strategies are not established for sporadic adult diffuse gliomas in the retrieved evidence. Secondary prevention largely consists of surveillance imaging in diagnosed patients following surgery and/or adjuvant therapy (carosi2024targetingisocitratedehydrogenase pages 4-6).

---

## 14. Other Species / Natural Disease
No naturally occurring non-human disease analogs were retrieved in this run.

---

## 15. Model Organisms
No specific oligodendroglioma model-organism systems were retrieved in the assembled evidence for this run; however, mechanistic multi-omics studies in human tumor samples (bulk and single-cell transcriptome, methylation, scATAC-seq) provide strong in situ evidence for differentiation blockade and epigenetic mechanisms (wei2023stalledoligodendrocytedifferentiation pages 1-2).

---

## Key Recent Developments (2023–2024 emphasis)
1. **IDH inhibition in earlier-stage disease:** INDIGO (NEJM 2023) demonstrated significant delay in progression and next intervention with vorasidenib in grade 2 IDH-mutant glioma after surgery only (mellinghoff2023vorasidenibinidh1 pages 1-3, mellinghoff2023vorasidenibinidh1 pages 3-5).
2. **Differentiation blockade mapped with multi-omics:** 2023 single-cell/bulk multi-omics indicates stalled oligodendrocyte-lineage differentiation with blocked myelination programs in IDH-mutant gliomas (wei2023stalledoligodendrocytedifferentiation pages 1-2).
3. **Refinement of WHO CNS5 implementation:** Practical guidance emphasizes integrated diagnoses driven by canonical molecular alterations and highlights laboratory workflow for IDH→ATRX→1p/19q testing (martin2023fromtheoryto pages 2-4, komori2023updateofthe pages 1-2).

---

## Key Trials and Outcome Statistics (Table)
| Trial | Population | Interventions | Key efficacy outcomes | Publication | PMID | URL |
|---|---|---|---|---|---|---|
| Joint Final Report: EORTC 26951 + RTOG 9402 | Newly diagnosed anaplastic oligodendroglial tumors; key molecular subgroup: 1p/19q-codeleted tumors | RT alone vs RT + PCV | **EORTC 26951, codeleted subgroup (n=80):** median OS 9.3 y without PCV vs 14.2 y with PCV; HR 0.60 (95% CI 0.35-1.03), *P*=.063; 14-y OS 26.2% vs 51.0%; probable 20-y OS 13.6% vs 37.1%. **RTOG 9402, codeleted subgroup (n=125):** median OS 7.3 y without PCV vs 13.2 y with PCV; HR 0.61 (95% CI 0.40-0.94), *P*=.02; 14-y OS 25.0% vs 46.1%; probable 20-y OS 14.9% vs 37.0%. Median follow-up 18-19 y. (lassman2022jointfinalreport pages 1-2, lassman2022jointfinalreport pages 2-3) | *Journal of Clinical Oncology* (2022) | Not available in retrieved context | https://doi.org/10.1200/JCO.21.02543 |
| RTOG 9402 long-term results | 291 eligible patients with anaplastic oligodendroglioma/oligoastrocytoma; 1p/19q-codeleted subgroup analyzed | Intensive PCV then RT vs RT alone | Overall cohort: median OS 4.6 y vs 4.7 y; HR 0.79 (95% CI 0.60-1.04), *P*=.1. **Codeleted tumors:** median OS 14.7 y with PCV+RT vs 7.3 y with RT alone; HR 0.59 (95% CI 0.37-0.95), *P*=.03. **Non-codeleted:** no benefit (2.6 y vs 2.7 y; HR 0.85, *P*=.39). (cairncross2013phaseiiitrial pages 1-2) | *Journal of Clinical Oncology* (2013) | Not available in retrieved context | https://doi.org/10.1200/JCO.2012.43.2674 |
| EORTC 26951 long-term follow-up | 368 patients with newly diagnosed anaplastic oligodendroglioma; molecular data available for 316; key subgroup: 1p/19q-codeleted tumors | RT alone vs RT followed by adjuvant PCV | Overall cohort: median OS 30.6 mo with RT vs 42.3 mo with RT/PCV; HR 0.75 (95% CI 0.60-0.95). Median PFS 13.2 mo vs 24.3 mo; HR 0.66 (95% CI 0.52-0.83). **Codeleted tumors:** median PFS 76 mo vs 11 mo for non-codeleted; HR 0.39 (95% CI 0.28-0.53); median OS 123 mo vs 23 mo for non-codeleted; HR 0.36 (95% CI 0.27-0.49). In the codeleted treatment comparison, OS was not reached with RT/PCV vs 112 mo with RT; HR 0.56 (95% CI 0.31-1.03). (bent2013adjuvantprocarbazinelomustine pages 2-3, bent2013adjuvantprocarbazinelomustine pages 1-2) | *Journal of Clinical Oncology* (2013) | Not available in retrieved context | https://doi.org/10.1200/JCO.2012.43.2229 |
| CODEL initial design analysis | Newly diagnosed 1p/19q-codeleted WHO grade 3 oligodendroglioma; 36 randomized patients | RT alone vs RT + concomitant/adjuvant TMZ vs TMZ alone; key comparison pooled RT-containing arms vs TMZ alone | With median follow-up 7.5 y: progression in 83.3% (10/12) on TMZ alone vs 37.5% (9/24) on RT-containing arms. PFS significantly shorter with TMZ alone: HR 3.12 (95% CI 1.26-7.69), *P*=0.014; adjusted HR 3.33 (95% CI 1.31-8.45), *P*=0.011. Median PFS 2.9 y with TMZ alone vs not reached with RT-containing arms; 3-y/5-y PFS 50%/33% vs 83%/56%. OS comparison underpowered and not significant. (jaeckle2021codelphaseiii pages 5-7, jaeckle2021codelphaseiii pages 1-2, jaeckle2021codelphaseiii pages 9-10) | *Neuro-Oncology* (2021) | Not available in retrieved context | https://doi.org/10.1093/neuonc/noaa168 |
| INDIGO (vorasidenib) | Residual or recurrent grade 2 IDH1/2-mutant glioma after surgery only; included oligodendroglioma and astrocytoma; no prior RT/chemotherapy | Vorasidenib 40 mg daily vs placebo | 331 randomized. Median PFS 27.7 mo vs 11.1 mo; HR 0.39 (95% CI 0.27-0.56), *P*<0.001. Time to next intervention HR 0.26 (95% CI 0.15-0.43); median time to next intervention not reached vs 17.8 mo. Grade >=3 adverse events 16.2%-22.8% with vorasidenib vs 5.5%-13.5% with placebo across excerpts; grade >=3 ALT increase 9.6% vs 0%. About half of enrolled tumors had 1p/19q codeletion. (mellinghoff2023vorasidenibinidh1 pages 1-3, mellinghoff2023vorasidenibinidh1 pages 6-8, mellinghoff2023vorasidenibinidh1 pages 3-5, mellinghoff2023vorasidenibinidh1 pages 16-18) | *New England Journal of Medicine* (2023) | Not available in retrieved context | https://doi.org/10.1056/NEJMoa2304194 |


*Table: This table summarizes pivotal clinical trials and long-term outcome statistics relevant to IDH-mutant, 1p/19q-codeleted oligodendroglioma and related anaplastic oligodendroglial tumor populations. It is useful for comparing historical RT/PCV evidence, temozolomide-era trial data, and recent IDH-targeted therapy results.*

---

## Evidence Figure
Kaplan–Meier overall survival and progression-free survival curves for 1p/19q-codeleted subgroups comparing RT vs RT+PCV across EORTC 26951 and RTOG 9402 are shown in the joint final report figure (lassman2022jointfinalreport media 697c589d).

---

## Notes on Evidence Gaps
Several template fields (ICD codes, MeSH/Orphanet/OMIM, population-level prevalence estimates, detailed environmental risk factors, structured HPO frequency estimates, and curated animal model resources) were not retrievable from the evidence assembled in this tool run and therefore are not asserted here.

References

1. (louis2021the2021who pages 8-9): David N Louis, Arie Perry, Pieter Wesseling, Daniel J Brat, Ian A Cree, Dominique Figarella-Branger, Cynthia Hawkins, H K Ng, Stefan M Pfister, Guido Reifenberger, Riccardo Soffietti, Andreas von Deimling, and David W Ellison. The 2021 who classification of tumors of the central nervous system: a summary. Neuro-oncology, 23:1231-1251, Jun 2021. URL: https://doi.org/10.1093/neuonc/noab106, doi:10.1093/neuonc/noab106. This article has 12970 citations and is from a domain leading peer-reviewed journal.

2. (louis2021the2021who pages 6-8): David N Louis, Arie Perry, Pieter Wesseling, Daniel J Brat, Ian A Cree, Dominique Figarella-Branger, Cynthia Hawkins, H K Ng, Stefan M Pfister, Guido Reifenberger, Riccardo Soffietti, Andreas von Deimling, and David W Ellison. The 2021 who classification of tumors of the central nervous system: a summary. Neuro-oncology, 23:1231-1251, Jun 2021. URL: https://doi.org/10.1093/neuonc/noab106, doi:10.1093/neuonc/noab106. This article has 12970 citations and is from a domain leading peer-reviewed journal.

3. (horbinski2022clinicalimplicationsof pages 1-2): Craig Horbinski, Tamar Berger, Roger J. Packer, and Patrick Y. Wen. Clinical implications of the 2021 edition of the who classification of central nervous system tumours. Nature Reviews Neurology, 18:515-529, Jun 2022. URL: https://doi.org/10.1038/s41582-022-00679-w, doi:10.1038/s41582-022-00679-w. This article has 334 citations and is from a highest quality peer-reviewed journal.

4. (komori2023updateofthe pages 1-2): Takashi Komori. Update of the 2021 who classification of tumors of the central nervous system: adult diffuse gliomas. Brain Tumor Pathology, 40:1-3, Dec 2023. URL: https://doi.org/10.1007/s10014-022-00446-1, doi:10.1007/s10014-022-00446-1. This article has 12 citations and is from a peer-reviewed journal.

5. (ahmad2024idhmutationglioma pages 7-8): Olfat Ahmad, Tahani Ahmad, and Stefan M. Pfister. Idh mutation, glioma immunogenicity, and therapeutic challenge of primary mismatch repair deficient idh‐mutant astrocytoma pmmrdia: a systematic review. Molecular Oncology, 18:2822-2841, Feb 2024. URL: https://doi.org/10.1002/1878-0261.13598, doi:10.1002/1878-0261.13598. This article has 16 citations and is from a peer-reviewed journal.

6. (louis2021the2021who pages 9-10): David N Louis, Arie Perry, Pieter Wesseling, Daniel J Brat, Ian A Cree, Dominique Figarella-Branger, Cynthia Hawkins, H K Ng, Stefan M Pfister, Guido Reifenberger, Riccardo Soffietti, Andreas von Deimling, and David W Ellison. The 2021 who classification of tumors of the central nervous system: a summary. Neuro-oncology, 23:1231-1251, Jun 2021. URL: https://doi.org/10.1093/neuonc/noab106, doi:10.1093/neuonc/noab106. This article has 12970 citations and is from a domain leading peer-reviewed journal.

7. (roux2020imaginggrowthas pages 7-7): Alexandre Roux, Arnault Tauziede-Espariat, Marc Zanello, Sophie Peeters, Gilles Zah-Bi, Eduardo Parraga, Myriam Edjlali, Emmanuèle Lechapt, Natalia Shor, Luisa Bellu, Giulia Berzero, Didier Dormont, Edouard Dezamis, Fabrice Chretien, Catherine Oppenheim, Marc Sanson, Pascale Varlet, Laurent Capelle, Frédéric Dhermain, and Johan Pallud. Imaging growth as a predictor of grade of malignancy and aggressiveness of idh-mutant and 1p/19q-codeleted oligodendrogliomas in adults. Neuro-oncology, 22:993-1005, Feb 2020. URL: https://doi.org/10.1093/neuonc/noaa022, doi:10.1093/neuonc/noaa022. This article has 21 citations and is from a domain leading peer-reviewed journal.

8. (martin2023fromtheoryto pages 1-2): Karina Chornenka Martin, Crystal Ma, and Stephen Yip. From theory to practice: implementing the who 2021 classification of adult diffuse gliomas in neuropathology diagnosis. Brain Sciences, May 2023. URL: https://doi.org/10.3390/brainsci13050817, doi:10.3390/brainsci13050817. This article has 22 citations.

9. (carosi2024targetingisocitratedehydrogenase pages 3-4): Francesca Carosi, Elisabetta Broseghini, Laura Fabbri, Giacomo Corradi, Riccardo Gili, Valentina Forte, Roberta Roncarati, Daria Maria Filippini, and Manuela Ferracin. Targeting isocitrate dehydrogenase (idh) in solid tumors: current evidence and future perspectives. Cancers, 16:2752, Aug 2024. URL: https://doi.org/10.3390/cancers16152752, doi:10.3390/cancers16152752. This article has 27 citations.

10. (martin2023fromtheoryto pages 2-4): Karina Chornenka Martin, Crystal Ma, and Stephen Yip. From theory to practice: implementing the who 2021 classification of adult diffuse gliomas in neuropathology diagnosis. Brain Sciences, May 2023. URL: https://doi.org/10.3390/brainsci13050817, doi:10.3390/brainsci13050817. This article has 22 citations.

11. (reuss2023updatesonthe pages 1-2): David.E. Reuss. Updates on the who diagnosis of idh-mutant glioma. Journal of Neuro-Oncology, 162:461-469, Jan 2023. URL: https://doi.org/10.1007/s11060-023-04250-5, doi:10.1007/s11060-023-04250-5. This article has 73 citations and is from a peer-reviewed journal.

12. (antonelli2022adulttypediffuse pages 4-6): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 67 citations.

13. (gue2024the2021world pages 7-9): Racine Gue and Dhairya A. Lakhani. The 2021 world health organization central nervous system tumor classification: the spectrum of diffuse gliomas. Biomedicines, 12:1349, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061349, doi:10.3390/biomedicines12061349. This article has 13 citations.

14. (carosi2024targetingisocitratedehydrogenase pages 4-6): Francesca Carosi, Elisabetta Broseghini, Laura Fabbri, Giacomo Corradi, Riccardo Gili, Valentina Forte, Roberta Roncarati, Daria Maria Filippini, and Manuela Ferracin. Targeting isocitrate dehydrogenase (idh) in solid tumors: current evidence and future perspectives. Cancers, 16:2752, Aug 2024. URL: https://doi.org/10.3390/cancers16152752, doi:10.3390/cancers16152752. This article has 27 citations.

15. (martin2023fromtheoryto pages 4-6): Karina Chornenka Martin, Crystal Ma, and Stephen Yip. From theory to practice: implementing the who 2021 classification of adult diffuse gliomas in neuropathology diagnosis. Brain Sciences, May 2023. URL: https://doi.org/10.3390/brainsci13050817, doi:10.3390/brainsci13050817. This article has 22 citations.

16. (ball2020frequencyoffalsepositive pages 1-2): Matthew K Ball, Thomas M Kollmeyer, Corinne E Praska, Michelle L McKenna, Caterina Giannini, Aditya Raghunathan, Mark E Jentoft, Daniel H Lachance, Benjamin R Kipp, Robert B Jenkins, and Cristiane M Ida. Frequency of false-positive fish 1p/19q codeletion in adult diffuse astrocytic gliomas. Neuro-oncology Advances, Jan 2020. URL: https://doi.org/10.1093/noajnl/vdaa109, doi:10.1093/noajnl/vdaa109. This article has 42 citations and is from a peer-reviewed journal.

17. (wei2023stalledoligodendrocytedifferentiation pages 1-2): Yanfei Wei, Guanzhang Li, Jing Feng, Fan Wu, Zheng Zhao, Zhaoshi Bao, Wei Zhang, Xiaodong Su, Jiuyi Li, Xueling Qi, Zejun Duan, Yunqiu Zhang, Sandra Ferreyra Vega, Asgeir Store Jakola, Yingyu Sun, Helena Carén, Tao Jiang, and Xiaolong Fan. Stalled oligodendrocyte differentiation in idh-mutant gliomas. Genome Medicine, Apr 2023. URL: https://doi.org/10.1186/s13073-023-01175-6, doi:10.1186/s13073-023-01175-6. This article has 28 citations and is from a highest quality peer-reviewed journal.

18. (ahmad2024idhmutationglioma pages 1-2): Olfat Ahmad, Tahani Ahmad, and Stefan M. Pfister. Idh mutation, glioma immunogenicity, and therapeutic challenge of primary mismatch repair deficient idh‐mutant astrocytoma pmmrdia: a systematic review. Molecular Oncology, 18:2822-2841, Feb 2024. URL: https://doi.org/10.1002/1878-0261.13598, doi:10.1002/1878-0261.13598. This article has 16 citations and is from a peer-reviewed journal.

19. (ball2020frequencyoffalsepositive pages 2-2): Matthew K Ball, Thomas M Kollmeyer, Corinne E Praska, Michelle L McKenna, Caterina Giannini, Aditya Raghunathan, Mark E Jentoft, Daniel H Lachance, Benjamin R Kipp, Robert B Jenkins, and Cristiane M Ida. Frequency of false-positive fish 1p/19q codeletion in adult diffuse astrocytic gliomas. Neuro-oncology Advances, Jan 2020. URL: https://doi.org/10.1093/noajnl/vdaa109, doi:10.1093/noajnl/vdaa109. This article has 42 citations and is from a peer-reviewed journal.

20. (ball2020frequencyoffalsepositive pages 13-14): Matthew K Ball, Thomas M Kollmeyer, Corinne E Praska, Michelle L McKenna, Caterina Giannini, Aditya Raghunathan, Mark E Jentoft, Daniel H Lachance, Benjamin R Kipp, Robert B Jenkins, and Cristiane M Ida. Frequency of false-positive fish 1p/19q codeletion in adult diffuse astrocytic gliomas. Neuro-oncology Advances, Jan 2020. URL: https://doi.org/10.1093/noajnl/vdaa109, doi:10.1093/noajnl/vdaa109. This article has 42 citations and is from a peer-reviewed journal.

21. (gue2024the2021world pages 9-12): Racine Gue and Dhairya A. Lakhani. The 2021 world health organization central nervous system tumor classification: the spectrum of diffuse gliomas. Biomedicines, 12:1349, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061349, doi:10.3390/biomedicines12061349. This article has 13 citations.

22. (cairncross2013phaseiiitrial pages 1-2): Gregory Cairncross, Meihua Wang, Edward Shaw, Robert Jenkins, David Brachman, Jan Buckner, Karen Fink, Luis Souhami, Normand Laperriere, Walter Curran, and Minesh Mehta. Phase iii trial of chemoradiotherapy for anaplastic oligodendroglioma: long-term results of rtog 9402. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 31 3:337-43, Jan 2013. URL: https://doi.org/10.1200/jco.2012.43.2674, doi:10.1200/jco.2012.43.2674. This article has 1403 citations.

23. (lassman2022jointfinalreport pages 1-2): Andrew B. Lassman, Khê Hoang-Xuan, Mei-Yin C. Polley, Alba A. Brandes, J. Gregory Cairncross, Johan M. Kros, Lynn S. Ashby, Martin J.B. Taphoorn, Luis Souhami, Winand N.M. Dinjens, Nadia N. Laack, Mathilde C.M. Kouwenhoven, Karen L. Fink, Pim J. French, David R. Macdonald, Denis Lacombe, Minhee Won, Thierry Gorlia, Minesh P. Mehta, and Martin J. van den Bent. Joint final report of eortc 26951 and rtog 9402: phase iii trials with procarbazine, lomustine, and vincristine chemotherapy for anaplastic oligodendroglial tumors. Journal of Clinical Oncology, 40:2539-2545, Aug 2022. URL: https://doi.org/10.1200/jco.21.02543, doi:10.1200/jco.21.02543. This article has 94 citations and is from a highest quality peer-reviewed journal.

24. (lassman2022jointfinalreport media 697c589d): Andrew B. Lassman, Khê Hoang-Xuan, Mei-Yin C. Polley, Alba A. Brandes, J. Gregory Cairncross, Johan M. Kros, Lynn S. Ashby, Martin J.B. Taphoorn, Luis Souhami, Winand N.M. Dinjens, Nadia N. Laack, Mathilde C.M. Kouwenhoven, Karen L. Fink, Pim J. French, David R. Macdonald, Denis Lacombe, Minhee Won, Thierry Gorlia, Minesh P. Mehta, and Martin J. van den Bent. Joint final report of eortc 26951 and rtog 9402: phase iii trials with procarbazine, lomustine, and vincristine chemotherapy for anaplastic oligodendroglial tumors. Journal of Clinical Oncology, 40:2539-2545, Aug 2022. URL: https://doi.org/10.1200/jco.21.02543, doi:10.1200/jco.21.02543. This article has 94 citations and is from a highest quality peer-reviewed journal.

25. (bent2013adjuvantprocarbazinelomustine pages 2-3): Martin J. van den Bent, Alba A. Brandes, Martin J.B. Taphoorn, Johan M. Kros, Mathilde C.M. Kouwenhoven, Jean-Yves Delattre, Hans J.J.A. Bernsen, Marc Frenay, Cees C. Tijssen, Wolfgang Grisold, László Sipos, Roelien H. Enting, Pim J. French, Winand N.M. Dinjens, Charles J. Vecht, Anouk Allgeier, Denis Lacombe, Thierry Gorlia, and Khê Hoang-Xuan. Adjuvant procarbazine, lomustine, and vincristine chemotherapy in newly diagnosed anaplastic oligodendroglioma: long-term follow-up of eortc brain tumor group study 26951. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 31 3:344-50, Jan 2013. URL: https://doi.org/10.1200/jco.2012.43.2229, doi:10.1200/jco.2012.43.2229. This article has 1457 citations.

26. (jaeckle2021codelphaseiii pages 1-2): Kurt A Jaeckle, Karla V Ballman, Martin van den Bent, Caterina Giannini, Evanthia Galanis, Paul D Brown, Robert B Jenkins, J Gregory Cairncross, Wolfgang Wick, Michael Weller, Kenneth D Aldape, Jesse G Dixon, S Keith Anderson, Jane H Cerhan, Jeffrey S Wefel, Martin Klein, Stuart A Grossman, David Schiff, Jeffrey J Raizer, Frederick Dhermain, Donald G Nordstrom, Patrick J Flynn, and Michael A Vogelbaum. Codel: phase iii study of rt, rt + tmz, or tmz for newly diagnosed 1p/19q codeleted oligodendroglioma. analysis from the initial study design. Neuro-Oncology, 23:457-467, Jul 2021. URL: https://doi.org/10.1093/neuonc/noaa168, doi:10.1093/neuonc/noaa168. This article has 122 citations and is from a domain leading peer-reviewed journal.

27. (jaeckle2021codelphaseiii pages 9-10): Kurt A Jaeckle, Karla V Ballman, Martin van den Bent, Caterina Giannini, Evanthia Galanis, Paul D Brown, Robert B Jenkins, J Gregory Cairncross, Wolfgang Wick, Michael Weller, Kenneth D Aldape, Jesse G Dixon, S Keith Anderson, Jane H Cerhan, Jeffrey S Wefel, Martin Klein, Stuart A Grossman, David Schiff, Jeffrey J Raizer, Frederick Dhermain, Donald G Nordstrom, Patrick J Flynn, and Michael A Vogelbaum. Codel: phase iii study of rt, rt + tmz, or tmz for newly diagnosed 1p/19q codeleted oligodendroglioma. analysis from the initial study design. Neuro-Oncology, 23:457-467, Jul 2021. URL: https://doi.org/10.1093/neuonc/noaa168, doi:10.1093/neuonc/noaa168. This article has 122 citations and is from a domain leading peer-reviewed journal.

28. (mellinghoff2023vorasidenibinidh1 pages 3-5): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 772 citations and is from a highest quality peer-reviewed journal.

29. (mellinghoff2023vorasidenibinidh1 pages 1-3): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 772 citations and is from a highest quality peer-reviewed journal.

30. (mellinghoff2023vorasidenibinidh1 pages 16-18): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 772 citations and is from a highest quality peer-reviewed journal.

31. (lassman2022jointfinalreport pages 2-3): Andrew B. Lassman, Khê Hoang-Xuan, Mei-Yin C. Polley, Alba A. Brandes, J. Gregory Cairncross, Johan M. Kros, Lynn S. Ashby, Martin J.B. Taphoorn, Luis Souhami, Winand N.M. Dinjens, Nadia N. Laack, Mathilde C.M. Kouwenhoven, Karen L. Fink, Pim J. French, David R. Macdonald, Denis Lacombe, Minhee Won, Thierry Gorlia, Minesh P. Mehta, and Martin J. van den Bent. Joint final report of eortc 26951 and rtog 9402: phase iii trials with procarbazine, lomustine, and vincristine chemotherapy for anaplastic oligodendroglial tumors. Journal of Clinical Oncology, 40:2539-2545, Aug 2022. URL: https://doi.org/10.1200/jco.21.02543, doi:10.1200/jco.21.02543. This article has 94 citations and is from a highest quality peer-reviewed journal.

32. (bent2013adjuvantprocarbazinelomustine pages 1-2): Martin J. van den Bent, Alba A. Brandes, Martin J.B. Taphoorn, Johan M. Kros, Mathilde C.M. Kouwenhoven, Jean-Yves Delattre, Hans J.J.A. Bernsen, Marc Frenay, Cees C. Tijssen, Wolfgang Grisold, László Sipos, Roelien H. Enting, Pim J. French, Winand N.M. Dinjens, Charles J. Vecht, Anouk Allgeier, Denis Lacombe, Thierry Gorlia, and Khê Hoang-Xuan. Adjuvant procarbazine, lomustine, and vincristine chemotherapy in newly diagnosed anaplastic oligodendroglioma: long-term follow-up of eortc brain tumor group study 26951. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 31 3:344-50, Jan 2013. URL: https://doi.org/10.1200/jco.2012.43.2229, doi:10.1200/jco.2012.43.2229. This article has 1457 citations.

33. (jaeckle2021codelphaseiii pages 5-7): Kurt A Jaeckle, Karla V Ballman, Martin van den Bent, Caterina Giannini, Evanthia Galanis, Paul D Brown, Robert B Jenkins, J Gregory Cairncross, Wolfgang Wick, Michael Weller, Kenneth D Aldape, Jesse G Dixon, S Keith Anderson, Jane H Cerhan, Jeffrey S Wefel, Martin Klein, Stuart A Grossman, David Schiff, Jeffrey J Raizer, Frederick Dhermain, Donald G Nordstrom, Patrick J Flynn, and Michael A Vogelbaum. Codel: phase iii study of rt, rt + tmz, or tmz for newly diagnosed 1p/19q codeleted oligodendroglioma. analysis from the initial study design. Neuro-Oncology, 23:457-467, Jul 2021. URL: https://doi.org/10.1093/neuonc/noaa168, doi:10.1093/neuonc/noaa168. This article has 122 citations and is from a domain leading peer-reviewed journal.

34. (mellinghoff2023vorasidenibinidh1 pages 6-8): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 772 citations and is from a highest quality peer-reviewed journal.
