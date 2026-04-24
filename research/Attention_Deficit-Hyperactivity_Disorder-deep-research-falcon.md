---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T16:58:47.020367'
end_time: '2026-04-24T17:14:09.009479'
duration_seconds: 921.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Attention Deficit-Hyperactivity Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Attention Deficit-Hyperactivity Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Attention Deficit-Hyperactivity Disorder** covering all of the
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
- **Disease Name:** Attention Deficit-Hyperactivity Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Attention Deficit-Hyperactivity Disorder** covering all of the
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


## Comprehensive Research Report: Attention-Deficit/Hyperactivity Disorder (ADHD)

### Scope and evidence base (this run)
This report synthesizes evidence retrieved via tool-based searches in peer‑reviewed literature and clinical-trial registries, prioritizing 2023–2024 where available. Some requested ontology identifiers (MONDO/MeSH/OMIM/Orphanet) and some phenotype/QoL/model-organism details could not be retrieved in this run and are explicitly flagged as gaps.

| Domain | Key finding (with quantitative values) | Population/setting | Source (first author, journal, year) | Publication date/month | PMID | URL |
|---|---|---|---|---|---|---|
| Epidemiology/Burden | In China, age-standardized ADHD prevalence increased by 9.86% from 1990 to 2021 (AAPC 0.272%, 95% CI 0.173–0.372), while age-standardized DALY rates increased by 10.15% (AAPC 0.262%, 95% CI 0.160–0.364); adolescents 10–14 years had prevalence 5,727.28/100,000 and DALY rate 70.55/100,000 (li2025theburdenof pages 1-2, li2025theburdenof pages 2-4) | GBD 2021-based China national burden analysis, children/adolescents | Li, *Frontiers in Psychiatry*, 2025 | Mar 2025 |  | https://doi.org/10.3389/fpsyt.2025.1532156 |
| Epidemiology/Burden | In 2021 China burden estimates, males had higher age-standardized prevalence (3,045.272/100,000) and DALYs (37.291/100,000) than females (1,215.746/100,000; 14.848/100,000), but female rates rose faster over time (li2025theburdenof pages 2-4) | China children/adolescents, sex-stratified burden | Li, *Frontiers in Psychiatry*, 2025 | Mar 2025 |  | https://doi.org/10.3389/fpsyt.2025.1532156 |
| Epidemiology/Burden | In a UK birth cohort, 3.0% of participants were classified with childhood ADHD problems at age 7 (thapar2023childhoodattentiondeficithyperactivity pages 1-2) | National Child Development Study, UK population cohort, n=8,016 with follow-up | Thapar, *British Journal of Psychiatry*, 2023 | Jul 2023 |  | https://doi.org/10.1192/bjp.2023.90 |
| Genetics | In 19,506 genotyped mother-father-offspring trios (child ADHD ratings in n=9,454), associations between maternal and paternal polygenic scores and child ADHD traits dropped markedly after adjustment for child polygenic score (pΔβ=9.95×10−17 maternal; 1.48×10−14 paternal), supporting genetic transmission over genetic nurture (pingault2023geneticnurtureversus pages 1-2) | Norwegian Mother, Father and Child Cohort Study trios | Pingault, *Molecular Psychiatry*, 2023 | Nov 2023 |  | https://doi.org/10.1038/s41380-022-01863-6 |
| Genetics | ADHD GWAS sample included 38,691 cases and 186,843 controls; genetic correlation with cannabis use disorder was rg=0.57 (SE 0.04) and with cannabis use rg=0.20 (SE 0.04); 36 genome-wide significant ADHD–CUD loci identified, including signals near **METTL15** and **FOXP2** (nielsen2024sharedgeneticsof pages 2-3, nielsen2024sharedgeneticsof pages 1-2) | Cross-disorder GWAS/meta-analysis | Nielsen, *Nature Mental Health*, 2024 | Jul 2024 |  | https://doi.org/10.1038/s44220-024-00277-3 |
| Genetics | Multi-omics integration across 14 GTEx v8 brain tissues prioritized 866 genes with significant expression effects and 966 genes with significant alternative-splicing effects; 106 regulatory pathways suggested DNA methylation influences ADHD through expression or splicing (wang2024amultiomicsstudy pages 1-2) | Brain-tissue eQTL/sQTL/mQTL + ADHD GWAS integration | Wang, *Briefings in Bioinformatics*, 2024 | Sep 2024 |  | https://doi.org/10.1093/bib/bbae502 |
| Disease information / diagnostics | DSM-5-TR and ICD-11 both require symptoms before age 12, cross-situational impairment, and duration ≥6 months, but DSM-5-TR specifies thresholds (6 symptoms per domain in children; 5 if age ≥17) while ICD-11 relies on clinician judgment and “several symptoms,” increasing potential heterogeneity (gomez2023differencesbetweendsm5tr pages 3-4, gomez2023differencesbetweendsm5tr pages 5-7) | Diagnostic classification comparison | Gomez, *World Journal of Psychiatry*, 2023 | May 2023 |  | https://doi.org/10.5498/wjp.v13.i5.138 |
| Outcomes/Safety | Childhood ADHD problems predicted higher mid-life cardiovascular risk: BMI +0.92 kg/m², systolic BP +3.5 mmHg, diastolic BP +2.2 mmHg, triglycerides +0.24 mol/L, and current smoking OR 1.6; no association with LDL cholesterol (thapar2023childhoodattentiondeficithyperactivity pages 1-2) | UK prospective population cohort, childhood ADHD assessed at 7 years and CVD risk at 44/45 years | Thapar, *British Journal of Psychiatry*, 2023 | Jul 2023 |  | https://doi.org/10.1192/bjp.2023.90 |
| Outcomes/Safety | Among 217,192 individuals aged 1–24 with ADHD, medication episodes were associated with reduced all-cause mortality (aHR 0.61, 95% CI 0.48–0.76), lower injury-related ED visits (aHR 0.75, 0.74–0.77), and lower injury-related hospitalizations (aHR 0.71, 0.68–0.75) versus non-medication periods (vasiliadis2024adhdmedicationsuse pages 1-2) | Quebec population-based retrospective cohort, 2000–2021 | Vasiliadis, *Translational Psychiatry*, 2024 | Feb 2024 |  | https://doi.org/10.1038/s41398-024-02825-y |
| Outcomes/Safety | In 278,027 Swedish individuals with ADHD, each additional year of ADHD medication use was associated with a 4% increased CVD risk (AOR 1.04, 95% CI 1.03–1.05); compared with nonuse, AORs were 1.27 for 3–5 years and 1.23 for >5 years; strongest signals were for hypertension (AOR 1.72 for 3–5 years; 1.80 for >5 years) (zhang2024attentiondeficithyperactivitydisordermedications pages 1-2, zhang2024attentiondeficithyperactivitydisordermedications pages 6-7) | Swedish nested case-control study with incident CVD cases | Zhang, *JAMA Psychiatry*, 2024 | Feb 2024 |  | https://doi.org/10.1001/jamapsychiatry.2023.4294 |
| Outcomes/Safety | Adults with diagnosed ADHD in UK primary care had reduced life expectancy of 6.78 years for males (95% CI 4.50–9.11) and 8.64 years for females (95% CI 6.55–10.91); only ~0.32% of cohort adults carried an ADHD diagnosis (onions2025lifeexpectancyand pages 1-2) | UK matched cohort: 30,039 adults with diagnosed ADHD vs 300,390 matched controls | O'Nions, *British Journal of Psychiatry*, 2025 | Jan 2025 |  | https://doi.org/10.1192/bjp.2024.199 |
| Treatment innovations | Recent innovation review highlights viloxazine ER, the first FDA-approved transdermal amphetamine patch, digital therapeutics, and trigeminal nerve stimulation (TNS) as new options to personalize ADHD care; TNS initial effect sizes were described as comparable to nonstimulant medications, but long-term cost-effectiveness and acceptability remain uncertain (baweja2024fromconsensusstatement pages 1-2, baweja2024fromconsensusstatement pages 10-11) | Review of recent innovations in ADHD care | Baweja, *Journal of Child and Adolescent Psychopharmacology*, 2024 | May 2024 |  | https://doi.org/10.1089/cap.2024.0022 |
| Treatment innovations | TNS practical/safety summary: >1 year of use had not indicated significant safety concerns; stimulation can be reduced in 0.2 mA steps for adverse effects, and no published studies had evaluated TNS combined with ADHD medications at the time of review (baweja2024fromconsensusstatement pages 9-10) | Pediatric ADHD device-based treatment implementation | Baweja, *Journal of Child and Adolescent Psychopharmacology*, 2024 | May 2024 |  | https://doi.org/10.1089/cap.2024.0022 |
| Treatment innovations | In a 4-week digital therapy study of 52 children aged 6–12, SNAP-IV parent scores improved (P<0.001) and TOVA-ACS improved (P<0.05); parental acceptance was 100%, average compliance 95%, and device-related adverse reactions occurred in 7.69% with no serious adverse events (huang2024clinicalstudyon pages 1-2) | Single-center clinical study, Wuhan Children’s Hospital, stable-treatment children with ADHD | Huang, *Scientific Reports*, 2024 | Oct 2024 |  | https://doi.org/10.1038/s41598-024-73934-3 |


*Table: This table compiles quantitative ADHD findings from the retrieved evidence across epidemiology, genetics, outcomes/safety, diagnostics, and treatment innovation. It is useful as a high-density reference for populating a disease knowledge base with recent, citable statistics and implementation-relevant results.*

---

## 1. Disease information
### 1.1 Concise overview
Attention‑deficit/hyperactivity disorder (ADHD) is a neurodevelopmental/psychiatric condition characterized by persistent, developmentally inappropriate patterns of **inattention** and/or **hyperactivity–impulsivity** that cause impairment across settings (e.g., home/school/work) and typically begin in childhood. Both DSM‑5‑TR and ICD‑11 require: symptoms beginning before age 12, duration of at least 6 months, cross‑situational presence, and clinically significant impairment. (gomez2023differencesbetweendsm5tr pages 3-4)

### 1.2 Key identifiers (availability in retrieved evidence)
* **DSM-5-TR**: ADHD diagnostic entity with presentations (combined; predominantly inattentive; predominantly hyperactive/impulsive). (gomez2023differencesbetweendsm5tr pages 3-4)
* **ICD-11**: ADHD diagnostic entity with similar presentations but different operationalization (see below). (gomez2023differencesbetweendsm5tr pages 3-4)
* **ICD-10 historical**: “hyperkinetic disorder” (HKD) as a narrower/severe construct; ICD‑11 broadened to include less severe presentations. (gomez2023differencesbetweendsm5tr pages 1-3)
* **ICD/MeSH/MONDO/OMIM/Orphanet IDs**: Not retrievable from the tools/evidence in this run; therefore not asserted here.

### 1.3 Synonyms / alternative names
* “Attention deficit hyperactivity disorder” / “Attention-deficit/hyperactivity disorder” (standard in DSM‑5‑TR and ICD‑11). (gomez2023differencesbetweendsm5tr pages 3-4)
* “Hyperkinetic disorder” (ICD‑10 legacy terminology). (gomez2023differencesbetweendsm5tr pages 1-3)

### 1.4 Data provenance
The evidence here is predominantly **aggregated disease-level resources**: population cohorts, administrative‑data pharmacoepidemiology, and multi‑cohort genetic studies, rather than EHR case reports. (li2025theburdenof pages 2-4, vasiliadis2024adhdmedicationsuse pages 1-2, zhang2024attentiondeficithyperactivitydisordermedications pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors (current understanding)
ADHD etiology is **multifactorial and polygenic**, with substantial common-variant contribution and extensive pleiotropy with other psychiatric/behavioral traits.

A key recent within‑family study (MoBa trios) supports that much observed parent–child association for ADHD traits is attributable to **genetic transmission** rather than environmentally mediated “genetic nurture.” Specifically, in 19,506 genotyped mother‑father‑offspring trios (child ADHD ratings available for n=9,454 at age 8), associations between maternal/paternal polygenic scores and child ADHD traits decreased markedly after adjusting for the child polygenic score (maternal pΔβ=9.95×10−17; paternal pΔβ=1.48×10−14). (pingault2023geneticnurtureversus pages 1-2)

**Direct quote (abstract):** Pingault et al. conclude that “the intergenerational transmission of risk for ADHD traits is largely explained by the transmission of genetic variants from parents to offspring rather than by genetic nurture.” (pingault2023geneticnurtureversus pages 4-5)

### 2.2 Risk factors (genetic)
#### Cross-disorder and comorbidity genetics (2024)
A 2024 Nature Mental Health study analyzed shared genetics between ADHD, cannabis use disorder (CUD), and cannabis use (CU), with large GWAS sample sizes (ADHD: 38,691 cases and 186,843 controls; CUD: 42,281 cases and 843,744 controls; CU: n=162,082). Genetic correlation was substantial for ADHD–CUD (rg=0.57, SE 0.04) and modest for ADHD–CU (rg=0.20, SE 0.04). (nielsen2024sharedgeneticsof pages 2-3)

The same study identified genome‑wide significant cross‑phenotype loci and highlighted candidate genes near signals including **METTL15** and **FOXP2** for ADHD–CUD. (nielsen2024sharedgeneticsof pages 2-3)

**Direct quote (abstract):** the paper frames aims including “Shared genetics of ADHD, cannabis use disorder and cannabis use” and provides rg estimates and sample sizes in the abstract excerpted here. (nielsen2024sharedgeneticsof pages 2-3)

#### Multi-omics (2024) linking genetics to brain tissue regulation
A 2024 study integrated ADHD GWAS with brain-tissue eQTL/sQTL/mQTL data across 14 GTEx v8 brain tissues using two-sample Mendelian randomization. It prioritized **866 genes** with significant expression effects and **966 unique genes** with significant alternative-splicing effects, and inferred **106 regulatory pathways** in which DNA methylation may influence ADHD through expression or splicing. (wang2024amultiomicsstudy pages 1-2)

**Direct quote (abstract):** “we also prioritized the expression of 866 genes … [and] 966 unique genes that have statistically significant causal AS events … [and] 106 regulatory pathways … where DNAm influences ADHD through gene expression or AS processes.” (wang2024amultiomicsstudy pages 1-2)

### 2.3 Environmental risk factors / protective factors / GxE
Environmental exposures and gene–environment interaction are widely discussed in the broader ADHD literature, but **the specific, high‑quality primary evidence for individual environmental risk/protective factors was not retrieved in this run**. Consequently, no specific environmental causal claims are asserted here.

---

## 3. Phenotypes
### 3.1 Core phenotypes (symptoms/behavioral)
The core symptom domains are:
* **Inattention** and **hyperactivity/impulsivity** (DSM‑5‑TR and ICD‑11). (gomez2023differencesbetweendsm5tr pages 3-4)

DSM‑5‑TR enumerates **9 inattention** and **9 hyperactivity/impulsivity** symptoms with symptom-count thresholds; ICD‑11 includes additional/split items (11 and 11) and differs in operationalization. (gomez2023differencesbetweendsm5tr pages 3-4, gomez2023differencesbetweendsm5tr pages 1-3)

### 3.2 Developmental features
ICD‑11 provides more explicit developmental variants (e.g., childhood fidgeting vs adult “mental restlessness”), and emphasizes that symptom expression can vary by setting and be less evident during stimulating activities. (gomez2023differencesbetweendsm5tr pages 3-4)

### 3.3 Suggested HPO terms (provisional; not exhaustively validated in retrieved evidence)
Because HPO mappings were not retrieved from an ontology source in this run, the following are **conservative suggestions** aligned to the symptom domains documented above:
* Inattention → **HP:0000736 (Short attention span)** (suggested)
* Hyperactivity → **HP:0000752 (Hyperactivity)** (suggested)
* Impulsivity → **HP:0000741 (Impulsivity)** (suggested)

### 3.4 Frequency among affected individuals / QoL impact
Not retrievable from the evidence in this run (e.g., no systematic phenotype frequency table, EQ‑5D/SF‑36 outcomes). Not asserted.

---

## 4. Genetic / molecular information
### 4.1 “Causal genes” vs polygenic architecture
The retrieved evidence supports ADHD as **highly polygenic**, with risk distributed across many variants, rather than a single-gene Mendelian disorder. (pingault2023geneticnurtureversus pages 1-2, nielsen2024sharedgeneticsof pages 1-2)

### 4.2 Example genes/loci implicated in recent analyses (not clinical diagnostic genes)
* ADHD–CUD cross‑disorder loci highlighted near **METTL15** and **FOXP2** (GWAS cross‑trait). (nielsen2024sharedgeneticsof pages 2-3)
* Multi‑omics prioritized gene examples include **COMMD5**, **HYAL3**, **PPP1R16A**, **TREM2** (tissue-specific MR/mediation results). (wang2024amultiomicsstudy pages 1-2)

### 4.3 Variant classification, allele frequency, somatic/germline
ClinVar/gnomAD/COSMIC-derived variant-level evidence was not retrieved in this run; not asserted.

### 4.4 Epigenetics
Evidence for DNA methylation as a mediator in brain tissues is provided by the multi‑omics mediation analysis (106 pathways) integrating mQTL with eQTL/sQTL and ADHD GWAS. (wang2024amultiomicsstudy pages 1-2)

---

## 5. Environmental information
Specific toxins, lifestyle factors, or infectious triggers were not supported by retrieved primary evidence in this run; not asserted.

---

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic understanding supported by retrieved evidence
#### Diagnostic‑framework implications for underlying structure
Gomez et al. (2023) note that DSM‑5‑TR implies a two‑factor structure (inattention vs combined hyperactivity/impulsivity) but that empirical latent-structure work often supports **three-factor** (inattention; hyperactivity; impulsivity) or **bifactor** models emphasizing impulsivity. They also emphasize the lack of validated ICD‑11 rating scales and the absence of reliable biomarkers for ADHD. (gomez2023differencesbetweendsm5tr pages 4-5, gomez2023differencesbetweendsm5tr pages 5-7)

#### Regulatory mechanisms in brain tissues
The 2024 brain multi‑omics MR study provides mechanistic hypotheses in which genetically influenced **gene expression**, **alternative splicing**, and **DNA methylation** in brain tissues contribute to ADHD liability, including mediated DNAm→expression/splicing regulatory pathways. (wang2024amultiomicsstudy pages 1-2)

### 6.2 Causal chain (supported, high-level)
A conservative chain consistent with retrieved evidence is:
1) Distributed inherited genetic risk transmitted from parents → 2) tissue-specific regulatory effects in brain (expression/splicing/methylation) → 3) altered neurodevelopmental/neurocognitive processes (inferred, not directly phenotyped in these sources) → 4) persistent inattention and/or hyperactivity–impulsivity with impairment across settings. (wang2024amultiomicsstudy pages 1-2, pingault2023geneticnurtureversus pages 1-2, gomez2023differencesbetweendsm5tr pages 3-4)

### 6.3 Suggested ontology mappings (high-level)
* **UBERON (anatomy; suggested)**: prefrontal cortex / frontal cortex; basal ganglia/striatum (not directly asserted in the retrieved evidence; included only as common ADHD neurocircuit targets—should be validated against additional sources).
* **GO biological processes (suggested)**: regulation of transcription; RNA splicing; DNA methylation; synaptic signaling (as these categories are implicated by multi‑omics gene regulation). (wang2024amultiomicsstudy pages 1-2)
* **CL (cell types; suggested)**: neurons/glia (cell-type specific enrichments are referenced generally in later review excerpts but not quantified in the retrieved text snippets; should be confirmed with additional primary sources). (cortese2025attention‐deficithyperactivitydisorder(adhd) pages 10-10)

---

## 7. Anatomical structures affected
Direct anatomical localization evidence (imaging, lesion, or region-specific pathology) was not retrieved in this run, aside from the fact that the multi‑omics study explicitly focuses on **brain tissues** across 14 regions (GTEx v8). (wang2024amultiomicsstudy pages 1-2)

Suggested (needs confirmation from dedicated neuroimaging literature): CNS structures involved in attention/executive function and motor inhibition.

---

## 8. Temporal development
### 8.1 Onset
Both DSM‑5‑TR and ICD‑11 require **some symptoms before age 12**, and symptoms should persist for at least **6 months**. (gomez2023differencesbetweendsm5tr pages 3-4)

### 8.2 Course / progression
Cortese et al. note that hyperactive/impulsive symptoms tend to decrease more than inattentive symptoms, such that older adolescents/adults often present more prominently with inattentive symptoms. (cortese2025attention‐deficithyperactivitydisorder(adhd) pages 3-4)

---

## 9. Inheritance and population
### 9.1 Inheritance pattern
The evidence in this run supports ADHD as a **polygenic, multifactorial** condition with predominant **genetic transmission** effects in family-based polygenic analyses. (pingault2023geneticnurtureversus pages 1-2)

### 9.2 Epidemiology and burden (recent quantitative data retrieved)
A China-focused GBD analysis (1990–2021) reported increasing age-standardized ADHD burden despite decreasing crude prevalence; adolescents 10–14 years bore the highest burden with prevalence **5,727.28/100,000** and DALY rate **70.55/100,000** (about twice the global average, per authors). (li2025theburdenof pages 1-2)

**Direct quote (abstract excerpt):** “Crude ADHD prevalence declined by 21.17% … yet age-standardized prevalence increased by 9.86% … Similarly, age-standardized DALY rates rose by 10.15% … Adolescents aged 10–14 years bore the highest burden …” (li2025theburdenof pages 1-2)

A UK 1958 birth cohort study used a childhood ADHD-problem screen and found **3.0%** classified with childhood ADHD problems among 8,016 participants with childhood and midlife biomedical data. (thapar2023childhoodattentiondeficithyperactivity pages 1-2)

Global prevalence estimates for 2023–2024 were not retrieved in this run; therefore not asserted.

---

## 10. Diagnostics
### 10.1 Diagnostic criteria (DSM‑5‑TR vs ICD‑11)
* **Shared core requirements**: symptoms before age 12; persistence ≥6 months; impairment; cross-situational presence. (gomez2023differencesbetweendsm5tr pages 3-4)
* **DSM‑5‑TR operationalization**: explicit symptom lists and numeric thresholds (children: ≥6 inattention and/or ≥6 hyperactivity/impulsivity; age ≥17: ≥5 per domain). (gomez2023differencesbetweendsm5tr pages 3-4)
* **ICD‑11 operationalization**: similar presentations but relies on clinician judgment and “several symptoms,” without fixed symptom-count thresholds, potentially increasing diagnostic heterogeneity; also includes some additional/split symptom items vs DSM. (gomez2023differencesbetweendsm5tr pages 3-4, gomez2023differencesbetweendsm5tr pages 1-3)

### 10.2 Rating scales / biomarkers
Gomez et al. emphasize a lack of validated **ICD‑11–based** ADHD rating scales and that there are **no reliable biomarkers** for ADHD currently. (gomez2023differencesbetweendsm5tr pages 4-5, gomez2023differencesbetweendsm5tr pages 5-7)

Differential diagnosis evidence was not retrieved in this run.

---

## 11. Outcomes / prognosis
### 11.1 Cardiovascular risk factors (life course)
In a UK prospective cohort, childhood ADHD problems at age 7 predicted adverse cardiovascular risk factor profiles at age 44/45: higher BMI (+0.92 kg/m²), systolic BP (+3.5 mmHg), diastolic BP (+2.2 mmHg), triglycerides (+0.24 mol/L), and current smoking (OR 1.6), but not LDL cholesterol. (thapar2023childhoodattentiondeficithyperactivity pages 1-2)

### 11.2 Mortality and life expectancy
A UK primary-care matched cohort study estimated reduced life expectancy in diagnosed adult ADHD: **6.78 years** lower for males and **8.64 years** lower for females, compared with matched controls. (onions2025lifeexpectancyand pages 1-2)

### 11.3 Medication-associated outcomes: injuries and mortality (youth)
A Quebec population-based cohort (2000–2021; n=217,192 aged 1–24) found medication episodes were associated with lower all-cause mortality (aHR 0.61) and reduced unintentional injury requiring ED visit (aHR 0.75) or hospitalization (aHR 0.71) compared to non-medication periods. (vasiliadis2024adhdmedicationsuse pages 1-2)

### 11.4 Medication-associated cardiovascular risk (long-term)
A Swedish nested case-control study (incident CVD cases among 278,027 individuals with ADHD) reported that each additional year of ADHD medication exposure was associated with ~4% increased CVD risk (AOR 1.04, 95% CI 1.03–1.05), and longer cumulative exposure was associated with higher odds of hypertension and arterial disease. (zhang2024attentiondeficithyperactivitydisordermedications pages 1-2, zhang2024attentiondeficithyperactivitydisordermedications pages 6-7)

---

## 12. Treatment
### 12.1 Current applications and real-world implementations (2023–2024 emphasis)
A 2024 review highlights newer options beyond standard oral stimulants/non‑stimulants, including **viloxazine extended release**, the first **transdermal amphetamine patch**, **digital therapeutics**, and **trigeminal nerve stimulation (TNS)**, framing these as tools for personalization and access. (baweja2024fromconsensusstatement pages 1-2)

#### Digital therapeutics (example: attention training)
A 2024 Scientific Reports clinical study evaluated “MindPro1” attention‑training software in **52 children (6–12 years)** over 4 weeks with stable background treatment. It reported improvement on SNAP‑IV parent scores (P<0.001) and TOVA attention metrics (P<0.05), with **100% parental acceptance** and **95% mean compliance**, and mild transient adverse reactions in 7.69% without serious adverse events. (huang2024clinicalstudyon pages 1-2)

**Direct quote (abstract):** “After 4 weeks … the SNAP-IV parent score improved (P < 0.001) … the TOVA-ACS score improved (P < 0.05) … acceptance rate … 100% … average compliance rate … 95% … 4 cases (7.69%) of adverse reactions … no serious adverse events.” (huang2024clinicalstudyon pages 1-2)

#### Trigeminal nerve stimulation (TNS)
The innovation review describes TNS as “well-tolerated” with early trial effect sizes comparable to nonstimulants, and provides practical use considerations (e.g., sensation is forehead tingling; single-use electrodes; dose adjustments for adverse effects). (baweja2024fromconsensusstatement pages 1-2, baweja2024fromconsensusstatement pages 9-10)

A cropped image of a practical troubleshooting/implementation table for TNS (Table 2) was retrieved from this review and can be used as a visual evidence item. (baweja2024fromconsensusstatement media baf871c0)

### 12.2 Treatment safety tradeoffs (recent evidence)
Real-world studies provide a nuanced picture: medication exposure episodes may reduce injuries and mortality in youth (Quebec cohort) (vasiliadis2024adhdmedicationsuse pages 1-2), whereas long-term cumulative exposure may be associated with elevated CVD risk, particularly hypertension/arterial disease (Swedish nested case-control). (zhang2024attentiondeficithyperactivitydisordermedications pages 1-2, zhang2024attentiondeficithyperactivitydisordermedications pages 6-7)

### 12.3 Suggested MAXO terms (provisional)
* **Pharmacotherapy** (stimulant and non‑stimulant medication treatment)
* **Cognitive training / digital therapeutic intervention**
* **Neurostimulation therapy** (e.g., trigeminal nerve stimulation)

Specific MAXO IDs were not retrieved in this run.

---

## 13. Prevention
Primary/secondary/tertiary prevention evidence (e.g., risk-factor modification trials, screening program evaluations) was not retrieved in this run and is not asserted.

---

## 14. Other species / natural disease
Not retrievable from the evidence in this run.

---

## 15. Model organisms
Model-organism evidence (mouse/rat/zebrafish/Drosophila, iPSC systems) was not retrieved in this run; not asserted.

---

## Expert analysis and interpretation (evidence-grounded)
1) **Diagnostic operationalization matters for research comparability**: DSM‑5‑TR’s algorithmic thresholds vs ICD‑11’s clinician-judgment approach can change case definitions and affect reliability and cross-study comparability; Gomez et al. explicitly raise concerns about ICD‑11 threshold vagueness and lack of validated rating scales. (gomez2023differencesbetweendsm5tr pages 4-5, gomez2023differencesbetweendsm5tr pages 5-7)
2) **Genetic evidence supports transmission-dominant intergenerational risk** in a large trio design, cautioning against interpreting parental exposures as purely environmental without genetically informed designs. (pingault2023geneticnurtureversus pages 1-2)
3) **Real-world benefit–risk is multi-domain**: pharmacoepidemiology suggests potential reductions in injuries/mortality during treated periods in youth (vasiliadis2024adhdmedicationsuse pages 1-2) while also indicating possible long-term cardiovascular risks with cumulative exposure (zhang2024attentiondeficithyperactivitydisordermedications pages 1-2). These findings support the clinical practice emphasis on individualized decision making and monitoring. (zhang2024attentiondeficithyperactivitydisordermedications pages 1-2)

---

## References (URLs with publication dates)
Key URLs and dates are provided inline and in the summary table artifact. The primary evidence base in this run includes: Gomez 2023 (World J Psychiatry; May 2023), Thapar 2023 (Br J Psychiatry; Jul 2023), Pingault 2023 (Molecular Psychiatry; Nov 2023), Zhang 2024 (JAMA Psychiatry; Feb 2024), Vasiliadis 2024 (Transl Psychiatry; Feb 2024), Nielsen 2024 (Nature Mental Health; Jul 2024), Wang 2024 (Briefings in Bioinformatics; Sep 2024), Huang 2024 (Scientific Reports; Oct 2024), Baweja 2024 (J Child Adolesc Psychopharmacol; May 2024), and O’Nions 2025 (Br J Psychiatry; Jan 2025). (gomez2023differencesbetweendsm5tr pages 3-4, thapar2023childhoodattentiondeficithyperactivity pages 1-2, pingault2023geneticnurtureversus pages 1-2, zhang2024attentiondeficithyperactivitydisordermedications pages 1-2, vasiliadis2024adhdmedicationsuse pages 1-2, nielsen2024sharedgeneticsof pages 2-3, wang2024amultiomicsstudy pages 1-2, huang2024clinicalstudyon pages 1-2, baweja2024fromconsensusstatement pages 1-2, onions2025lifeexpectancyand pages 1-2)

References

1. (li2025theburdenof pages 1-2): Ningyu Li, Junqiang Zhao, and Fujun Zhou. The burden of attention deficit hyperactivity disorder and incidence rate forecast in china from 1990 to 2021. Frontiers in Psychiatry, Mar 2025. URL: https://doi.org/10.3389/fpsyt.2025.1532156, doi:10.3389/fpsyt.2025.1532156. This article has 10 citations.

2. (li2025theburdenof pages 2-4): Ningyu Li, Junqiang Zhao, and Fujun Zhou. The burden of attention deficit hyperactivity disorder and incidence rate forecast in china from 1990 to 2021. Frontiers in Psychiatry, Mar 2025. URL: https://doi.org/10.3389/fpsyt.2025.1532156, doi:10.3389/fpsyt.2025.1532156. This article has 10 citations.

3. (thapar2023childhoodattentiondeficithyperactivity pages 1-2): Ajay K. Thapar, Lucy Riglin, Rachel Blakey, Stephan Collishaw, George Davey Smith, Evie Stergiakouli, Kate Tilling, and Anita Thapar. Childhood attention-deficit hyperactivity disorder problems and mid-life cardiovascular risk: prospective population cohort study. The British Journal of Psychiatry, 223:472-477, Jul 2023. URL: https://doi.org/10.1192/bjp.2023.90, doi:10.1192/bjp.2023.90. This article has 18 citations.

4. (pingault2023geneticnurtureversus pages 1-2): Jean-Baptiste Pingault, Wikus Barkhuizen, Biyao Wang, Laurie J. Hannigan, Espen Moen Eilertsen, Elizabeth Corfield, Ole A. Andreassen, Helga Ask, Martin Tesli, Ragna Bugge Askeland, George Davey Smith, Camilla Stoltenberg, Neil M. Davies, Ted Reichborn-Kjennerud, Eivind Ystrom, and Alexandra Havdahl. Genetic nurture versus genetic transmission of risk for adhd traits in the norwegian mother, father and child cohort study. Molecular Psychiatry, 28:1731-1738, Nov 2023. URL: https://doi.org/10.1038/s41380-022-01863-6, doi:10.1038/s41380-022-01863-6. This article has 66 citations and is from a highest quality peer-reviewed journal.

5. (nielsen2024sharedgeneticsof pages 2-3): Trine Tollerup Nielsen, Jinjie Duan, Daniel F. Levey, G. Bragi Walters, Emma C. Johnson, Thorgeir Thorgeirsson, Daniel F. Levey, Joel Gelernter, Thomas Werge, Preben Bo Mortensen, Hreinn Stefansson, Kari Stefansson, David M. Hougaard, Arpana Agrawal, Joel Gelernter, Jakob Grove, Anders D. Børglum, and Ditte Demontis. Shared genetics of adhd, cannabis use disorder and cannabis use and prediction of cannabis use disorder in adhd. Nature Mental Health, 2:1071-1083, Jul 2024. URL: https://doi.org/10.1038/s44220-024-00277-3, doi:10.1038/s44220-024-00277-3. This article has 3 citations and is from a peer-reviewed journal.

6. (nielsen2024sharedgeneticsof pages 1-2): Trine Tollerup Nielsen, Jinjie Duan, Daniel F. Levey, G. Bragi Walters, Emma C. Johnson, Thorgeir Thorgeirsson, Daniel F. Levey, Joel Gelernter, Thomas Werge, Preben Bo Mortensen, Hreinn Stefansson, Kari Stefansson, David M. Hougaard, Arpana Agrawal, Joel Gelernter, Jakob Grove, Anders D. Børglum, and Ditte Demontis. Shared genetics of adhd, cannabis use disorder and cannabis use and prediction of cannabis use disorder in adhd. Nature Mental Health, 2:1071-1083, Jul 2024. URL: https://doi.org/10.1038/s44220-024-00277-3, doi:10.1038/s44220-024-00277-3. This article has 3 citations and is from a peer-reviewed journal.

7. (wang2024amultiomicsstudy pages 1-2): Jingkai Wang, Qiu-Wen Zhu, Jia-Hao Mai, Shun Zhang, Yuqing Wang, Jiatong Liang, and Ji-Yuan Zhou. A multi-omics study of brain tissue transcription and dna methylation revealing the genetic pathogenesis of adhd. Briefings in Bioinformatics, Sep 2024. URL: https://doi.org/10.1093/bib/bbae502, doi:10.1093/bib/bbae502. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (gomez2023differencesbetweendsm5tr pages 3-4): Rapson Gomez, Wai Chen, and Stephen Houghton. Differences between dsm-5-tr and icd-11 revisions of attention deficit/hyperactivity disorder: a commentary on implications and opportunities. World Journal of Psychiatry, 13:138-143, May 2023. URL: https://doi.org/10.5498/wjp.v13.i5.138, doi:10.5498/wjp.v13.i5.138. This article has 58 citations.

9. (gomez2023differencesbetweendsm5tr pages 5-7): Rapson Gomez, Wai Chen, and Stephen Houghton. Differences between dsm-5-tr and icd-11 revisions of attention deficit/hyperactivity disorder: a commentary on implications and opportunities. World Journal of Psychiatry, 13:138-143, May 2023. URL: https://doi.org/10.5498/wjp.v13.i5.138, doi:10.5498/wjp.v13.i5.138. This article has 58 citations.

10. (vasiliadis2024adhdmedicationsuse pages 1-2): Helen-Maria Vasiliadis, Carlotta Lunghi, Elham Rahme, Louis Rochette, Martin Gignac, Victoria Massamba, Fatoumata Binta Diallo, Alvine Fansi, Samuele Cortese, and Alain Lesage. Adhd medications use and risk of mortality and unintentional injuries: a population-based cohort study. Translational Psychiatry, Feb 2024. URL: https://doi.org/10.1038/s41398-024-02825-y, doi:10.1038/s41398-024-02825-y. This article has 24 citations and is from a peer-reviewed journal.

11. (zhang2024attentiondeficithyperactivitydisordermedications pages 1-2): Le Zhang, Lin Li, Pontus Andell, Miguel Garcia-Argibay, Patrick D. Quinn, Brian M. D’Onofrio, Isabell Brikell, Ralf Kuja-Halkola, Paul Lichtenstein, Kristina Johnell, Henrik Larsson, and Zheng Chang. Attention-deficit/hyperactivity disorder medications and long-term risk of cardiovascular diseases. JAMA Psychiatry, 81:178, Feb 2024. URL: https://doi.org/10.1001/jamapsychiatry.2023.4294, doi:10.1001/jamapsychiatry.2023.4294. This article has 135 citations and is from a highest quality peer-reviewed journal.

12. (zhang2024attentiondeficithyperactivitydisordermedications pages 6-7): Le Zhang, Lin Li, Pontus Andell, Miguel Garcia-Argibay, Patrick D. Quinn, Brian M. D’Onofrio, Isabell Brikell, Ralf Kuja-Halkola, Paul Lichtenstein, Kristina Johnell, Henrik Larsson, and Zheng Chang. Attention-deficit/hyperactivity disorder medications and long-term risk of cardiovascular diseases. JAMA Psychiatry, 81:178, Feb 2024. URL: https://doi.org/10.1001/jamapsychiatry.2023.4294, doi:10.1001/jamapsychiatry.2023.4294. This article has 135 citations and is from a highest quality peer-reviewed journal.

13. (onions2025lifeexpectancyand pages 1-2): Elizabeth O'Nions, Céline El Baou, Amber John, Dan Lewer, Will Mandy, Douglas G.J. McKechnie, Irene Petersen, and Josh Stott. Life expectancy and years of life lost for adults with diagnosed adhd in the uk: matched cohort study. The British Journal of Psychiatry, 226:261-268, Jan 2025. URL: https://doi.org/10.1192/bjp.2024.199, doi:10.1192/bjp.2024.199. This article has 56 citations.

14. (baweja2024fromconsensusstatement pages 1-2): Raman Baweja, Stephen V. Faraone, Ann C. Childress, Margaret D. Weiss, Sandra K. Loo, Timothy E. Wilens, and James G. Waxmonsky. From consensus statement to pills to pixels: new innovations in attention-deficit/hyperactivity disorder care. Journal of Child and Adolescent Psychopharmacology, 34:167-182, May 2024. URL: https://doi.org/10.1089/cap.2024.0022, doi:10.1089/cap.2024.0022. This article has 15 citations and is from a peer-reviewed journal.

15. (baweja2024fromconsensusstatement pages 10-11): Raman Baweja, Stephen V. Faraone, Ann C. Childress, Margaret D. Weiss, Sandra K. Loo, Timothy E. Wilens, and James G. Waxmonsky. From consensus statement to pills to pixels: new innovations in attention-deficit/hyperactivity disorder care. Journal of Child and Adolescent Psychopharmacology, 34:167-182, May 2024. URL: https://doi.org/10.1089/cap.2024.0022, doi:10.1089/cap.2024.0022. This article has 15 citations and is from a peer-reviewed journal.

16. (baweja2024fromconsensusstatement pages 9-10): Raman Baweja, Stephen V. Faraone, Ann C. Childress, Margaret D. Weiss, Sandra K. Loo, Timothy E. Wilens, and James G. Waxmonsky. From consensus statement to pills to pixels: new innovations in attention-deficit/hyperactivity disorder care. Journal of Child and Adolescent Psychopharmacology, 34:167-182, May 2024. URL: https://doi.org/10.1089/cap.2024.0022, doi:10.1089/cap.2024.0022. This article has 15 citations and is from a peer-reviewed journal.

17. (huang2024clinicalstudyon pages 1-2): Sheng Huang, Tianhui Zhang, Qing Lu, Xueqin Xiong, Zhisheng Liu, and Dan Sun. Clinical study on the intervention effect of digital therapy on children with attention deficit hyperactivity disorder (adhd). Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-73934-3, doi:10.1038/s41598-024-73934-3. This article has 13 citations and is from a peer-reviewed journal.

18. (gomez2023differencesbetweendsm5tr pages 1-3): Rapson Gomez, Wai Chen, and Stephen Houghton. Differences between dsm-5-tr and icd-11 revisions of attention deficit/hyperactivity disorder: a commentary on implications and opportunities. World Journal of Psychiatry, 13:138-143, May 2023. URL: https://doi.org/10.5498/wjp.v13.i5.138, doi:10.5498/wjp.v13.i5.138. This article has 58 citations.

19. (pingault2023geneticnurtureversus pages 4-5): Jean-Baptiste Pingault, Wikus Barkhuizen, Biyao Wang, Laurie J. Hannigan, Espen Moen Eilertsen, Elizabeth Corfield, Ole A. Andreassen, Helga Ask, Martin Tesli, Ragna Bugge Askeland, George Davey Smith, Camilla Stoltenberg, Neil M. Davies, Ted Reichborn-Kjennerud, Eivind Ystrom, and Alexandra Havdahl. Genetic nurture versus genetic transmission of risk for adhd traits in the norwegian mother, father and child cohort study. Molecular Psychiatry, 28:1731-1738, Nov 2023. URL: https://doi.org/10.1038/s41380-022-01863-6, doi:10.1038/s41380-022-01863-6. This article has 66 citations and is from a highest quality peer-reviewed journal.

20. (gomez2023differencesbetweendsm5tr pages 4-5): Rapson Gomez, Wai Chen, and Stephen Houghton. Differences between dsm-5-tr and icd-11 revisions of attention deficit/hyperactivity disorder: a commentary on implications and opportunities. World Journal of Psychiatry, 13:138-143, May 2023. URL: https://doi.org/10.5498/wjp.v13.i5.138, doi:10.5498/wjp.v13.i5.138. This article has 58 citations.

21. (cortese2025attention‐deficithyperactivitydisorder(adhd) pages 10-10): Samuele Cortese, Mark A. Bellgrove, Isabell Brikell, Barbara Franke, David W. Goodman, Catharina A. Hartman, Henrik Larsson, Frances R. Levin, Edoardo G. Ostinelli, Valeria Parlatini, Josep A. Ramos‐Quiroga, Margaret H. Sibley, Anneka Tomlinson, Timothy E. Wilens, Ian C.K. Wong, Nina Hovén, Jeremy Didier, Christoph U. Correll, Luis A. Rohde, and Stephen V. Faraone. Attention‐deficit/hyperactivity disorder (<scp>adhd</scp>) in adults: evidence base, uncertainties and controversies. World Psychiatry, 24:347-371, Sep 2025. URL: https://doi.org/10.1002/wps.21374, doi:10.1002/wps.21374. This article has 35 citations and is from a highest quality peer-reviewed journal.

22. (cortese2025attention‐deficithyperactivitydisorder(adhd) pages 3-4): Samuele Cortese, Mark A. Bellgrove, Isabell Brikell, Barbara Franke, David W. Goodman, Catharina A. Hartman, Henrik Larsson, Frances R. Levin, Edoardo G. Ostinelli, Valeria Parlatini, Josep A. Ramos‐Quiroga, Margaret H. Sibley, Anneka Tomlinson, Timothy E. Wilens, Ian C.K. Wong, Nina Hovén, Jeremy Didier, Christoph U. Correll, Luis A. Rohde, and Stephen V. Faraone. Attention‐deficit/hyperactivity disorder (<scp>adhd</scp>) in adults: evidence base, uncertainties and controversies. World Psychiatry, 24:347-371, Sep 2025. URL: https://doi.org/10.1002/wps.21374, doi:10.1002/wps.21374. This article has 35 citations and is from a highest quality peer-reviewed journal.

23. (baweja2024fromconsensusstatement media baf871c0): Raman Baweja, Stephen V. Faraone, Ann C. Childress, Margaret D. Weiss, Sandra K. Loo, Timothy E. Wilens, and James G. Waxmonsky. From consensus statement to pills to pixels: new innovations in attention-deficit/hyperactivity disorder care. Journal of Child and Adolescent Psychopharmacology, 34:167-182, May 2024. URL: https://doi.org/10.1089/cap.2024.0022, doi:10.1089/cap.2024.0022. This article has 15 citations and is from a peer-reviewed journal.