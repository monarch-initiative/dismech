---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T16:41:49.259314'
end_time: '2026-04-25T16:50:51.075479'
duration_seconds: 541.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ataxia-telangiectasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ataxia-telangiectasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ataxia-telangiectasia** covering all of the
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
- **Disease Name:** Ataxia-telangiectasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ataxia-telangiectasia** covering all of the
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


# Ataxia-telangiectasia (A‑T) — Disease Characteristics Research Report (Mendelian)

## Target Disease
- **Disease name:** Ataxia‑telangiectasia (A‑T)
- **Category:** Mendelian (autosomal recessive DNA repair disorder)
- **MONDO ID:** Not identified in retrieved sources (gap)

---

## 1. Disease Information

### 1.1 Concise overview
Ataxia‑telangiectasia (A‑T) is a rare, autosomal recessive, multisystem disorder caused by **biallelic pathogenic variants (PVs) in ATM**, characterized by progressive cerebellar neurodegeneration (ataxia), oculocutaneous telangiectasia, immunodeficiency with recurrent infections, marked radiosensitivity, and elevated cancer risk. (pereira2024ataxiatelangiectasiainlatin pages 1-6, nakano2024updateonrecommendations pages 1-2, collyer2024ataxiatelangiectasia pages 3-5)

### 1.2 Key identifiers and controlled vocabulary
- **OMIM:** **208900** (pereira2024ataxiatelangiectasiainlatin pages 1-6, tiet2024exploringneurodegenerationin pages 9-16)
- **MeSH:** *Ataxia Telangiectasia* (ClinicalTrials.gov condition browse) (NCT06193200 chunk 2)
- **ICD‑10 / ICD‑11:** Not identified in retrieved sources (gap)
- **Orphanet (ORPHA):** Not identified in retrieved sources (gap)
- **MONDO:** Not identified in retrieved sources (gap)

### 1.3 Synonyms / alternative names
- **Louis‑Bar syndrome** (NCT06193200 chunk 1)
- **Cerebello‑oculocutaneous telangiectasia** (NCT06193200 chunk 1)

### 1.4 Evidence source type
The report integrates:
- **Aggregated disease-level resources / consensus guidance** (AACR Childhood Cancer Predisposition Workshop update in *Clinical Cancer Research*, 2024) (nakano2024updateonrecommendations pages 1-2)
- **Large multi-center human cohort evidence** (Latin America, n=218) (pereira2024ataxiatelangiectasiainlatin pages 1-6)
- **Mechanistic primary research** (Cell Reports 2024 microglia study) (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3)
- **ClinicalTrials.gov interventional trial records** for real‑world implementation of investigational therapies (NCT06193200 chunk 1, NCT04870866 chunk 1, NCT06673056 chunk 1, NCT07215416 chunk 1)


### Summary identifiers & diagnostic anchors
| Item | Value | Source (with DOI/URL if present) | Publication year |
|---|---|---|---|
| Disease name | Ataxia-telangiectasia (A-T) | Tiet dissertation, DOI: https://doi.org/10.17863/cam.112012 (tiet2024exploringneurodegenerationin pages 9-16) | 2024 |
| OMIM identifier | OMIM 208900 | Tiet dissertation, DOI: https://doi.org/10.17863/cam.112012 (tiet2024exploringneurodegenerationin pages 9-16) | 2024 |
| Common synonyms | Louis-Bar syndrome; cerebello-oculocutaneous telangiectasia | ClinicalTrials.gov NEAT trial keywords, NCT06193200: https://clinicaltrials.gov/study/NCT06193200 (NCT06193200 chunk 1) | 2024 |
| Inheritance | Autosomal recessive | Nakano et al., Clin Cancer Res, DOI: https://doi.org/10.1158/1078-0432.CCR-24-1098 (nakano2024updateonrecommendations pages 1-2) | 2024 |
| Causal gene | ATM (biallelic pathogenic variants) | Pereira et al., Immunologic Research, DOI: https://doi.org/10.1007/s12026-024-09494-5 (pereira2024ataxiatelangiectasiainlatin pages 1-6) | 2024 |
| Gene locus | ATM located at 11q22.3 | Pereira et al., Immunologic Research, DOI: https://doi.org/10.1007/s12026-024-09494-5 (pereira2024ataxiatelangiectasiainlatin pages 1-6) | 2024 |
| Core molecular function | ATM is a serine/threonine kinase central to DNA double-strand break response/repair and cell-cycle checkpoint signaling | Lai et al., Cell Reports, DOI: https://doi.org/10.1016/j.celrep.2023.113622 (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3) | 2024 |
| Genetic testing approach | Sequencing including deletion/duplication assessment of ATM | Nakano et al., Clin Cancer Res, DOI: https://doi.org/10.1158/1078-0432.CCR-24-1098 (nakano2024updateonrecommendations pages 1-2) | 2024 |
| Chromosome instability test | Chromosome breakage analysis; radiation-induced chromosomal breakage used diagnostically | Nakano et al., Clin Cancer Res, DOI: https://doi.org/10.1158/1078-0432.CCR-24-1098; Pereira et al., Immunologic Research, DOI: https://doi.org/10.1007/s12026-024-09494-5 (nakano2024updateonrecommendations pages 1-2, pereira2024ataxiatelangiectasiainlatin pages 1-6) | 2024 |
| Immunoblotting | Immunoblotting listed as a diagnostic laboratory method | Nakano et al., Clin Cancer Res, DOI: https://doi.org/10.1158/1078-0432.CCR-24-1098 (nakano2024updateonrecommendations pages 1-2) | 2024 |
| Alpha-fetoprotein (AFP) | Elevated AFP is a key laboratory biomarker | Nakano et al., Clin Cancer Res, DOI: https://doi.org/10.1158/1078-0432.CCR-24-1098 (nakano2024updateonrecommendations pages 1-2) | 2024 |
| Immunodeficiency profile | Lymphopenia and low immunoglobulins are characteristic; reduced TREC may be seen on newborn screening | Nakano et al., Clin Cancer Res, DOI: https://doi.org/10.1158/1078-0432.CCR-24-1098 (nakano2024updateonrecommendations pages 1-2) | 2024 |
| Common immunoglobulin abnormalities | IgA deficiency, IgG deficiency, and frequent T- and B-lymphopenia | Pereira et al., Immunologic Research, DOI: https://doi.org/10.1007/s12026-024-09494-5 (pereira2024ataxiatelangiectasiainlatin pages 1-6) | 2024 |
| Characteristic karyotype finding | Abnormal karyotype involving chromosomes 7 and 14 | Nakano et al., Clin Cancer Res, DOI: https://doi.org/10.1158/1078-0432.CCR-24-1098 (nakano2024updateonrecommendations pages 1-2) | 2024 |


*Table: This table compiles core identifiers, synonyms, inheritance, ATM gene information, and the main laboratory diagnostics used for ataxia-telangiectasia. It is useful as a concise reference for disease knowledge base curation and diagnostic annotation.*

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic:** A‑T is caused by **biallelic PVs in ATM**, which encodes a serine/threonine kinase central to the DNA damage response, particularly double‑strand break (DSB) signaling/repair and cell‑cycle checkpoints. (pereira2024ataxiatelangiectasiainlatin pages 1-6, lai2024atmdeficiencyinducedmicroglialactivation pages 1-3, nakano2024updateonrecommendations pages 1-2)

**Molecular role:** Upon DNA damage, **ATM activation phosphorylates regulators of cell‑cycle arrest, DNA repair, and apoptosis** (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3). ATM also has cytoplasmic/redox and organelle functions (mitochondrial redox sensing, lysosomal trafficking, autophagy modulation), which are increasingly implicated in neurodegeneration and systemic complications. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3, amirifar2019ataxia‐telangiectasiaareview pages 6-9)

### 2.2 Risk factors
**Genetic risk factors (causal variants):**
- **ATM (11q22.3)**; biallelic PVs cause classic A‑T. (pereira2024ataxiatelangiectasiainlatin pages 1-6)

**Environmental/iatrogenic risk factors (gene–environment interaction):**
- **Ionizing radiation** (clinical radiosensitivity) is a major risk due to the underlying DNA repair defect; exposure can cause toxicity and is generally avoided. (collyer2024ataxiatelangiectasia pages 3-5)
- **Radiomimetic chemotherapy** (example noted: bleomycin) is also discouraged/avoided in A‑T due to hypersensitivity. (collyer2024ataxiatelangiectasia pages 3-5)

### 2.3 Protective factors
Not identified in the retrieved evidence (gap).

### 2.4 Gene–environment interactions
A‑T is a canonical gene–environment interaction disorder where **ATM deficiency → impaired response to radiation‑induced DNA damage**, motivating diagnostic **radiation‑induced chromosomal breakage** testing and clinical avoidance of ionizing radiation exposures when feasible. (pereira2024ataxiatelangiectasiainlatin pages 1-6, nakano2024updateonrecommendations pages 1-2, collyer2024ataxiatelangiectasia pages 3-5)

---

## 3. Phenotypes (with HPO suggestions)

### 3.1 Neurologic phenotypes (symptoms/signs)
**Progressive cerebellar ataxia** (childhood onset; progressive; major cause of disability)
- Quantitative natural history proxy: classic patients often develop symptoms ~2 years and may need ambulatory assistance between ~8–12 years (reviewed trial landscape). (kuhn2023ataxiatelangiectasiaclinicaltrial pages 1-3)
- Review notes many patients lose ambulation by adolescence. (collyer2024ataxiatelangiectasia pages 5-7)
- **HPO:** HP:0001251 (Ataxia); HP:0001272 (Cerebellar atrophy)

**Oculomotor abnormalities / oculomotor apraxia**
- **HPO:** HP:0000641 (Oculomotor apraxia); HP:0000612 (Oculogyration / abnormal eye movements; placeholder—use most specific term per phenotype)

**Movement disorders** (e.g., dystonia/chorea in some presentations)
- **HPO:** HP:0001332 (Dystonia); HP:0002072 (Chorea)

### 3.2 Vascular/skin phenotype
**Telangiectasia (oculocutaneous)**
- **HPO:** HP:0001083 (Telangiectasia)

### 3.3 Immunologic and infectious phenotypes (with frequencies)
In a 2024 multicenter Latin American cohort (n=218):
- **Recurrent airway infections:** **66.9%** (pereira2024ataxiatelangiectasiainlatin pages 1-6)
- **IgA deficiency:** **60.8%** (pereira2024ataxiatelangiectasiainlatin pages 1-6)
- **IgG deficiency:** **28.6%** (pereira2024ataxiatelangiectasiainlatin pages 1-6)
- **HPO:** HP:0002721 (Immunodeficiency); HP:0002719 (Recurrent infections); HP:0002720 (IgA deficiency)

### 3.4 Pulmonary disease
Pulmonary disease is common and reported to affect **~70%** in a recent pediatric neurology review; pulmonary function testing is recommended beginning around **5–6 years**. (collyer2024ataxiatelangiectasia pages 3-5)
- **HPO:** HP:0006536 (Recurrent respiratory infections); HP:0002204 (Pulmonary fibrosis—if present); HP:0002099 (Asthma—if present)

### 3.5 Hepatic / metabolic phenotypes (recent data)
**Hepatic fibrosis / chronic liver disease**
- Cross‑sectional study (2023; n=25, ages 5–31) found **significant hepatic fibrosis in 5/25 (20%)** by non‑invasive biomarkers and elastography. (barreto2023hepaticfibrosisa pages 1-2)
- **HPO:** HP:0001394 (Hepatic fibrosis); HP:0001397 (Hepatomegaly—if present)

### 3.6 Cancer predisposition
A pediatric neurology review reported malignancy risk estimates with a **minimum ~10%** and ceiling **25–38%**, with hematologic neoplasms predominating in younger individuals; reported hematologic categories include T‑ALL and T‑PLL. (collyer2024ataxiatelangiectasia pages 3-5)
- **HPO:** HP:0003002 (Neoplasm)

### 3.7 Quality‑of‑life impact
A‑T is progressive and disabling; clinical trials and biomarker reviews emphasize the need for validated outcome measures and biomarkers due to functional decline and multisystem disease burden. (kuhn2023ataxiatelangiectasiaclinicaltrial pages 1-3)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **ATM** (ataxia‑telangiectasia mutated), locus **11q22.3**. (pereira2024ataxiatelangiectasiainlatin pages 1-6)

### 4.2 Pathogenic variant classes and functional consequences
The retrieved evidence supports that disease is due to **biallelic ATM PVs** leading to defective ATM kinase function and impaired DSB response, plus broader redox/mitochondrial/lysosomal effects. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3, nakano2024updateonrecommendations pages 1-2)

Variant‑level details (e.g., recurrent founder variants, allele frequencies in gnomAD, ACMG classifications from ClinVar) were not extracted from the retrieved corpus and remain a gap for this report.

### 4.3 Modifier genes
Not identified in the retrieved evidence (gap).

### 4.4 Epigenetic information
Not identified in the retrieved evidence (gap).

### 4.5 Chromosomal abnormalities
Consensus guidance lists **“abnormal karyotype involving chromosomes 7 and 14”** among laboratory abnormalities used in diagnostic workup for A‑T. (nakano2024updateonrecommendations pages 1-2)

---

## 5. Environmental Information

### 5.1 Environmental factors
The dominant environmental sensitivity is **ionizing radiation** exposure, due to impaired DSB repair; clinical reviews explicitly recommend avoiding ionizing radiation when possible. (collyer2024ataxiatelangiectasia pages 3-5)

### 5.2 Lifestyle factors
Not identified in retrieved evidence (gap).

### 5.3 Infectious agents
No single pathogen is causal; however, recurrent respiratory infections are common and linked to immunodeficiency. (pereira2024ataxiatelangiectasiainlatin pages 1-6)

---

## 6. Mechanism / Pathophysiology

### 6.1 Core pathway concepts (current understanding)
- **DNA double‑strand break response / cell‑cycle checkpoint:** ATM is a kinase activated by DNA damage and phosphorylates key regulators of DNA repair, cell‑cycle arrest, and apoptosis. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3)
- **Oxidative stress and organelle dysfunction:** Reviews emphasize ATM’s roles beyond nuclear DSB repair, including oxidative stress response and metabolic signaling; oxidative stress is proposed as a contributor to multisystem pathology. (amirifar2019ataxia‐telangiectasiaareview pages 6-9, barreto2023hepaticfibrosisa pages 1-2)

**Suggested pathway/ontology mappings (illustrative):**
- **GO:** DNA damage response, signal transduction by p53 class mediator; double‑strand break repair; cell cycle checkpoint signaling; regulation of intrinsic apoptotic signaling pathway.

### 6.2 Neurodegeneration and neuroinflammation (recent development: 2024)
A 2024 *Cell Reports* study provides mechanistic evidence that **ATM deficiency drives microglial activation that promotes neurodegeneration**. Key findings include:
- **Enriched ATM expression in microglia** and snRNA‑seq evidence of **microglial inflammation in A‑T cerebellum**. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3)
- **Temporal ordering:** pseudotime analyses suggesting **microglial activation precedes neuronal apoptosis‑related gene upregulation**. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3)
- **Cell-intrinsic immune activation:** iPSC‑derived A‑T microglia show activation of innate immune pathways; **co‑culture with neurons increases cytotoxicity** (LDH release; p<0.001). (lai2024atmdeficiencyinducedmicroglialactivation pages 10-11)
- **Upstream pathway:** cell‑intrinsic activation includes **cGAS–STING**, NF‑κB, and type I interferon programs. (lai2024atmdeficiencyinducedmicroglialactivation pages 10-11)

**Suggested cell type ontology mappings:**
- **CL:** microglial cell; Purkinje cell; cerebellar granule cell.

### 6.3 Liver/metabolic pathophysiology
A 2023 Orphanet Journal of Rare Diseases cohort emphasizes that liver disease is an emerging later complication with histopathologic correlates (NASH, cirrhosis, HCC reported in the literature) and identified **20% significant hepatic fibrosis** by non‑invasive tests, associated with metabolic alterations and greater ataxia severity. (barreto2023hepaticfibrosisa pages 1-2)

---

## 7. Anatomical Structures Affected (with UBERON/GO-CC suggestions)

### 7.1 Organ systems
- **Central nervous system:** cerebellum (neurodegeneration) (pereira2024ataxiatelangiectasiainlatin pages 1-6, lai2024atmdeficiencyinducedmicroglialactivation pages 1-3)
  - **UBERON:** cerebellum
- **Immune system:** combined immunodeficiency features (lymphopenia, hypogammaglobulinemia/IgA deficiency) (pereira2024ataxiatelangiectasiainlatin pages 1-6, nakano2024updateonrecommendations pages 1-2)
  - **UBERON:** thymus; bone marrow; lymph node
- **Respiratory system:** chronic sinopulmonary disease (~70% reported) (collyer2024ataxiatelangiectasia pages 3-5)
  - **UBERON:** lung
- **Liver/metabolic:** hepatic fibrosis in a subset (barreto2023hepaticfibrosisa pages 1-2)
  - **UBERON:** liver

### 7.2 Subcellular localization (suggested)
- **GO cellular component:** nucleus (DNA repair foci), mitochondrion (redox/mitochondrial dysfunction), lysosome (perinuclear lysosome accumulation), consistent with ATM’s described roles. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3)

---

## 8. Temporal Development (onset and progression)

### 8.1 Onset
In the 2024 Latin American cohort (n=218), median/mean timing was:
- **Symptom onset:** **mean 1.6 ± 1.1 years**
- **Diagnosis:** **mean 5.7 ± 3.5 years** (pereira2024ataxiatelangiectasiainlatin pages 1-6)

### 8.2 Progression
A‑T is progressive with functional decline; neurological manifestations worsen over time, and multi‑system complications (pulmonary, malignancy, metabolic/liver) accumulate, contributing to premature mortality. (collyer2024ataxiatelangiectasia pages 3-5, pereira2024ataxiatelangiectasiainlatin pages 1-6)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal recessive**, caused by **biallelic ATM PVs**. (nakano2024updateonrecommendations pages 1-2)

### 9.2 Epidemiology
- Estimated prevalence range in a 2023 clinical-trial landscape review: **1/40,000–1/100,000 live births** (kuhn2023ataxiatelangiectasiaclinicaltrial pages 1-3)
- A 2024 dissertation summarizes a lower prevalence estimate (~**1:400,000**) and an estimate of ~**200 UK cases** (lower-authority source; thesis) (tiet2024exploringneurodegenerationin pages 9-16)

### 9.3 Population genetics
Carrier frequency and founder effects were not identified in the retrieved evidence (gap).

---

## 10. Diagnostics

### 10.1 Core diagnostic tests (consensus guidance; 2024)
The 2024 AACR workshop update lists A‑T diagnostic testing/lab abnormalities including:
- **Genetic testing** (sequencing including deletion/duplication assessment)
- **Chromosome breakage analysis**
- **Immunoblotting**
- **Elevated alpha‑fetoprotein (AFP)**
- **Abnormal karyotype involving chromosomes 7 and 14**
- **Immunodeficiency** (lymphopenia, low immunoglobulin levels, reduced **TREC** in newborn screening) (nakano2024updateonrecommendations pages 1-2)

### 10.2 Practical diagnostic criteria used in a large cohort
In the Latin American cohort, diagnostic biomarkers/criteria included: progressive cerebellar ataxia plus **AFP >2 SD for age**, low IgA (≥2 SD below), and **radiation-induced chromosomal breakage**; definitive diagnosis required biallelic disabling ATM variants plus chromosome breakage or progressive ataxia. (pereira2024ataxiatelangiectasiainlatin pages 1-6)

### 10.3 Differential diagnosis
AT‑like disorders affecting DNA damage response/repair can mimic A‑T and should be considered (e.g., A‑T‑like disorder due to MRE11; other DDR disorders). (collyer2024ataxiatelangiectasia pages 3-5)

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality (recent cohort data)
In the 2024 Latin American cohort (n=218):
- **Mean survival:** **24.2 years**
- **Kaplan–Meier 20‑year survival:** **52.6%**
- **Higher mortality association:** low IgG (HR **2.1**, 95% CI 1.11–3.93); sex association reported (HR 0.52 for males in one analysis). (pereira2024ataxiatelangiectasiainlatin pages 1-6)

### 11.2 Major causes of death
Cancer was reported as the leading cause of death, with infections also contributing substantially. (pereira2024ataxiatelangiectasiainlatin pages 13-16)

---

## 12. Treatment

### 12.1 Current standard-of-care (supportive, real-world implementations)
A‑T currently lacks curative therapy; care is primarily supportive and multidisciplinary. (pereira2024ataxiatelangiectasiainlatin pages 1-6, kuhn2023ataxiatelangiectasiaclinicaltrial pages 1-3)

Implemented supportive strategies with cohort utilization data:
- **Antibiotic prophylaxis:** **57.7%** of patients (Latin American cohort) (pereira2024ataxiatelangiectasiainlatin pages 1-6)
- **Immunoglobulin replacement therapy (IgRT):** **49.1%** (pereira2024ataxiatelangiectasiainlatin pages 1-6)
- Pulmonary monitoring: PFTs recommended starting **~5–6 years** (collyer2024ataxiatelangiectasia pages 3-5)

**MAXO suggestions (illustrative):**
- Immunoglobulin replacement therapy; antibiotic prophylaxis; pulmonary function testing; physical therapy/occupational therapy/speech therapy.

### 12.2 Investigational / emerging therapies and clinical trials

#### Erythrocyte-encapsulated dexamethasone (EryDex)
- **NEAT trial:** Phase 3, randomized placebo-controlled; monthly infusions (every 28 days) (NCT06193200; first posted 2024‑01‑05; start 2024‑06‑24; completion 2025‑12‑17; status verified 2026‑01). Primary endpoint: change in RmICARS over ~6 months (baseline to Visit 9). (NCT06193200 chunk 1)

#### NAD+ boosting via nicotinamide ribonucleoside (NR)
- Phase 2, open-label proof-of-concept in A‑T: NR 300 mg/day for 2 years; endpoints include NAD metabolome in blood, SARA/ICARS/AT‑NEST and exploratory AFP and metabolic markers (NCT04870866; first posted 2021‑05‑04; estimated primary completion 2024‑09‑03). (NCT04870866 chunk 1)

#### N‑acetyl‑L‑leucine (IB1001; levacetylleucine)
- Phase 3 randomized placebo-controlled cross‑over study in patients age ≥4 years; primary endpoint SARA (NCT06673056; first posted 2024‑11‑04). (NCT06673056 chunk 1)

#### Precision genetic therapy (mutation-specific ASO)
- Phase 1/2 ASO therapy (**atipeksen**) for recurrent **ATM c.7865C>T** splice variant; intrathecal dosing; endpoints include AT‑NEST and structured A‑T CGI and exploratory biomarkers including neurofilament light chain and AFP (NCT07215416; first posted 2025‑10‑10; not yet recruiting as of 2025‑10). (NCT07215416 chunk 1)

### 12.3 Expert analysis (trial readiness obstacles)
A 2023 Expert Opinion review emphasizes barriers to successful A‑T trials including phenotype variability, delayed diagnosis, lack of validated biomarkers/outcome measures, incomplete understanding of neurologic injury, and rarity that limits randomized trial size. (kuhn2023ataxiatelangiectasiaclinicaltrial pages 1-3)

---

## 13. Prevention

### 13.1 Primary/tertiary prevention
- **Avoid/limit ionizing radiation exposure** and radiomimetic agents due to radiosensitivity. (collyer2024ataxiatelangiectasia pages 3-5)

### 13.2 Vaccination considerations
In the large Latin American cohort, **no live-vaccine complications were reported**, supporting that vaccination practices can be feasible but must be individualized to immune status. (pereira2024ataxiatelangiectasiainlatin pages 1-6)

### 13.3 Genetic counseling
Autosomal recessive inheritance and consensus recommendations for genetic testing imply a central role for genetic counseling and cascade testing, but specific prenatal/carrier screening protocols were not retrieved in this evidence set (gap). (nakano2024updateonrecommendations pages 1-2)

---

## 14. Other Species / Natural Disease
Naturally occurring A‑T in non‑human species was not identified in the retrieved evidence (gap).

---

## 15. Model Organisms

### 15.1 Key models and what they capture
- **ATM-null mouse models:** reported limitation—**do not recapitulate human cerebellar degeneration** well. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3)
- **Human iPSC-derived microglia/neuron co-culture models:** show microglia-driven inflammatory activation and neuronal cytotoxicity, enabling mechanistic dissection and candidate therapeutic testing of neuroinflammatory pathways. (lai2024atmdeficiencyinducedmicroglialactivation pages 10-11)

---

## Direct quotes from abstracts (supporting key statements)

1) **Large human cohort (2024; Immunologic Research):**
- “Ataxia-telangiectasia (AT) is a rare genetic disorder leading to neurological defects, telangiectasias, and immunodeficiency.” (pereira2024ataxiatelangiectasiainlatin pages 1-6)
- “Median (IQR) ages at symptom onset and diagnosis were 1.0 (1.0-2.0) years, respectively.” (pereira2024ataxiatelangiectasiainlatin pages 1-6)

2) **Trial landscape review (2023; Expert Opinion on Investigational Drugs):**
- “Ataxia telangiectasia (A-T) is a life-limiting autosomal recessive disease characterized by cerebellar degeneration, ocular telangiectasias, and sinopulmonary disease.” (kuhn2023ataxiatelangiectasiaclinicaltrial pages 1-3)

---

## Data gaps and curation notes
- **MONDO / Orphanet / ICD‑10/ICD‑11 identifiers** were not retrieved via the current tool evidence set and should be filled from OMIM/Orphanet/MONDO cross-references in a subsequent curation pass.
- **Variant-level spectrum, ClinVar assertions, allele frequencies (gnomAD), founder effects, and carrier frequency** were not captured in retrieved sources.
- **Detailed cancer surveillance modality and schedule for A‑T** beyond diagnostic recognition was not extracted (although AACR 2024 paper establishes A‑T within genomic instability disorders and diagnostic testing framework). (nakano2024updateonrecommendations pages 1-2)


References

1. (pereira2024ataxiatelangiectasiainlatin pages 1-6): Renan A. Pereira, Ellen O. Dantas, Jessica Loekmanwidjaja, Juliana T. L. Mazzucchelli, Carolina S. Aranda, Maria E. G. Serrano, Elisabeth A. De La Cruz Córdoba, Liliana Bezrodnik, Ileana Moreira, Janaira F. S. Ferreira, Vera M. Dantas, Valéria S. F. Sales, Carmen C. Fernandez, Maria M. S. Vilela, Isabela P. Motta, Jose Luis Franco, Julio Cesar Orrego Arango, Jesús A. Álvarez-Álvarez, Lina Rocío Riaño Cardozo, Julio C. Orellana, Antonio Condino-Neto, Cristina M. Kokron, Myrthes T. Barros, Lorena Regairaz, Diana Cabanillas, Carmen L. N. Suarez, Nelson A. Rosario, Herberto J. Chong-Neto, Olga A. Takano, Maria I. S. V. Nadaf, Lillian S. L. Moraes, Fabiola S. Tavares, Flaviane Rabelo, Jessica Pino, Wilmer C. Calderon, Daniel Mendoza-Quispe, Ekaterini S. Goudouris, Virginia Patiño, Cecilia Montenegro, Monica S. Souza, Aniela BXCCastelo Branco, Wilma C. N. Forte, Flavia A. A. Carvalho, Gesmar Segundo, Marina F. A. Cheik, Persio Roxo-Junior, Maryanna Peres, Annie M. Oliveira, Arnaldo C. P. Neto, Maria Claudia Ortega-López, Alejandro Lozano, Natalia Andrea Lozano, Leticia H. Nieto, Anete S. Grumach, Daniele C. Costa, Nelma M. N. Antunes, Victor Nudelman, Camila T. M. Pereira, Maria D. M. Martinez, Francisco J. R. Quiroz, Aristoteles A. Cardona, Maria E. Nuñez-Nuñez, Jairo A. Rodriguez, Célia M. Cuellar, Gustavo Vijoditz, Daniélli C. Bichuetti-Silva, Carolina C. M. Prando, Sérgio L. Amantéa, and Beatriz T. Costa-Carvalho. Ataxia-telangiectasia in latin america: clinical features, immunodeficiency, and mortality in a multicenter study. Immunologic research, 72:864-873, Jun 2024. URL: https://doi.org/10.1007/s12026-024-09494-5, doi:10.1007/s12026-024-09494-5. This article has 4 citations and is from a peer-reviewed journal.

2. (nakano2024updateonrecommendations pages 1-2): Yoshiko Nakano, Roland P. Kuiper, Kim E. Nichols, Christopher C. Porter, Harry Lesmana, Julia Meade, Christian P. Kratz, Lucy A. Godley, Luke D. Maese, Maria Isabel Achatz, Payal P. Khincha, Sharon A. Savage, Andrea S. Doria, Mary-Louise C. Greer, Vivian Y. Chang, Lisa L. Wang, Sharon E. Plon, and Michael F. Walsh. Update on recommendations for cancer screening and surveillance in children with genomic instability disorders. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:5009-5020, Sep 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1098, doi:10.1158/1078-0432.ccr-24-1098. This article has 20 citations.

3. (collyer2024ataxiatelangiectasia pages 3-5): John Collyer and Deepa S Rajan. Ataxia telangiectasia. Seminars in Pediatric Neurology, 52:101169, Dec 2024. URL: https://doi.org/10.1016/j.spen.2024.101169, doi:10.1016/j.spen.2024.101169. This article has 15 citations.

4. (tiet2024exploringneurodegenerationin pages 9-16): May Yung Tiet. Exploring neurodegeneration in ataxia-telangiectasia. Dissertation, Sep 2024. URL: https://doi.org/10.17863/cam.112012, doi:10.17863/cam.112012. This article has 0 citations.

5. (NCT06193200 chunk 2):  Evaluate the Neurological Effects of EryDex on Subjects With A-T. Quince Therapeutics S.p.A.. 2024. ClinicalTrials.gov Identifier: NCT06193200

6. (NCT06193200 chunk 1):  Evaluate the Neurological Effects of EryDex on Subjects With A-T. Quince Therapeutics S.p.A.. 2024. ClinicalTrials.gov Identifier: NCT06193200

7. (lai2024atmdeficiencyinducedmicroglialactivation pages 1-3): Jenny Lai, Didem Demirbas, Junho Kim, Ailsa M. Jeffries, Allie Tolles, Junseok Park, Thomas W. Chittenden, Patrick G. Buckley, Timothy W. Yu, Michael A. Lodato, and Eunjung Alice Lee. Atm-deficiency-induced microglial activation promotes neurodegeneration in ataxia-telangiectasia. Cell Reports, 43:113622, Jan 2024. URL: https://doi.org/10.1016/j.celrep.2023.113622, doi:10.1016/j.celrep.2023.113622. This article has 33 citations and is from a highest quality peer-reviewed journal.

8. (NCT04870866 chunk 1): Hilde Nilsen. NAD Supplementation to Prevent Progressive Neurological Disease in Ataxia Telangiectasia. University Hospital, Akershus. 2019. ClinicalTrials.gov Identifier: NCT04870866

9. (NCT06673056 chunk 1):  A Pivotal Study of N-Acetyl-L-Leucine on Ataxia-Telangiectasia (A-T). IntraBio Inc. 2025. ClinicalTrials.gov Identifier: NCT06673056

10. (NCT07215416 chunk 1): Timothy Yu. Safety and Efficacy of Mutation-targeted Precision Genetic Therapy for Ataxia-Telangiectasia (A-T). Timothy Yu. 2025. ClinicalTrials.gov Identifier: NCT07215416

11. (amirifar2019ataxia‐telangiectasiaareview pages 6-9): Parisa Amirifar, Mohammad Reza Ranjouri, Reza Yazdani, Hassan Abolhassani, and Asghar Aghamohammadi. Ataxia‐telangiectasia: a review of clinical features and molecular pathology. Pediatric Allergy and Immunology, 30:277-288, Mar 2019. URL: https://doi.org/10.1111/pai.13020, doi:10.1111/pai.13020. This article has 244 citations and is from a domain leading peer-reviewed journal.

12. (kuhn2023ataxiatelangiectasiaclinicaltrial pages 1-3): Katrina Kuhn, Howard M. Lederman, and Sharon A. McGrath-Morrow. Ataxia-telangiectasia clinical trial landscape and the obstacles to overcome. Expert Opinion on Investigational Drugs, 32:693-704, Aug 2023. URL: https://doi.org/10.1080/13543784.2023.2249399, doi:10.1080/13543784.2023.2249399. This article has 13 citations and is from a peer-reviewed journal.

13. (collyer2024ataxiatelangiectasia pages 5-7): John Collyer and Deepa S Rajan. Ataxia telangiectasia. Seminars in Pediatric Neurology, 52:101169, Dec 2024. URL: https://doi.org/10.1016/j.spen.2024.101169, doi:10.1016/j.spen.2024.101169. This article has 15 citations.

14. (barreto2023hepaticfibrosisa pages 1-2): Talita Lemos Neves Barreto, Roberto José de Carvalho Filho, David Carlos Shigueoka, Fernando Luiz Affonso Fonseca, Ariel Cordeiro Ferreira, Cristiane Kochi, Carolina Sanchez Aranda, and Roseli Oselka Saccardo Sarni. Hepatic fibrosis: a manifestation of the liver disease evolution in patients with ataxia-telangiectasia. Orphanet Journal of Rare Diseases, May 2023. URL: https://doi.org/10.1186/s13023-023-02720-7, doi:10.1186/s13023-023-02720-7. This article has 4 citations and is from a peer-reviewed journal.

15. (lai2024atmdeficiencyinducedmicroglialactivation pages 10-11): Jenny Lai, Didem Demirbas, Junho Kim, Ailsa M. Jeffries, Allie Tolles, Junseok Park, Thomas W. Chittenden, Patrick G. Buckley, Timothy W. Yu, Michael A. Lodato, and Eunjung Alice Lee. Atm-deficiency-induced microglial activation promotes neurodegeneration in ataxia-telangiectasia. Cell Reports, 43:113622, Jan 2024. URL: https://doi.org/10.1016/j.celrep.2023.113622, doi:10.1016/j.celrep.2023.113622. This article has 33 citations and is from a highest quality peer-reviewed journal.

16. (pereira2024ataxiatelangiectasiainlatin pages 13-16): Renan A. Pereira, Ellen O. Dantas, Jessica Loekmanwidjaja, Juliana T. L. Mazzucchelli, Carolina S. Aranda, Maria E. G. Serrano, Elisabeth A. De La Cruz Córdoba, Liliana Bezrodnik, Ileana Moreira, Janaira F. S. Ferreira, Vera M. Dantas, Valéria S. F. Sales, Carmen C. Fernandez, Maria M. S. Vilela, Isabela P. Motta, Jose Luis Franco, Julio Cesar Orrego Arango, Jesús A. Álvarez-Álvarez, Lina Rocío Riaño Cardozo, Julio C. Orellana, Antonio Condino-Neto, Cristina M. Kokron, Myrthes T. Barros, Lorena Regairaz, Diana Cabanillas, Carmen L. N. Suarez, Nelson A. Rosario, Herberto J. Chong-Neto, Olga A. Takano, Maria I. S. V. Nadaf, Lillian S. L. Moraes, Fabiola S. Tavares, Flaviane Rabelo, Jessica Pino, Wilmer C. Calderon, Daniel Mendoza-Quispe, Ekaterini S. Goudouris, Virginia Patiño, Cecilia Montenegro, Monica S. Souza, Aniela BXCCastelo Branco, Wilma C. N. Forte, Flavia A. A. Carvalho, Gesmar Segundo, Marina F. A. Cheik, Persio Roxo-Junior, Maryanna Peres, Annie M. Oliveira, Arnaldo C. P. Neto, Maria Claudia Ortega-López, Alejandro Lozano, Natalia Andrea Lozano, Leticia H. Nieto, Anete S. Grumach, Daniele C. Costa, Nelma M. N. Antunes, Victor Nudelman, Camila T. M. Pereira, Maria D. M. Martinez, Francisco J. R. Quiroz, Aristoteles A. Cardona, Maria E. Nuñez-Nuñez, Jairo A. Rodriguez, Célia M. Cuellar, Gustavo Vijoditz, Daniélli C. Bichuetti-Silva, Carolina C. M. Prando, Sérgio L. Amantéa, and Beatriz T. Costa-Carvalho. Ataxia-telangiectasia in latin america: clinical features, immunodeficiency, and mortality in a multicenter study. Immunologic research, 72:864-873, Jun 2024. URL: https://doi.org/10.1007/s12026-024-09494-5, doi:10.1007/s12026-024-09494-5. This article has 4 citations and is from a peer-reviewed journal.