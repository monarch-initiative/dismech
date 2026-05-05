---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T16:49:03.274437'
end_time: '2026-05-05T16:58:36.766965'
duration_seconds: 573.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cutaneous collagenous vasculopathy
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Cutaneous collagenous vasculopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cutaneous collagenous vasculopathy** covering all of the
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
- **Disease Name:** Cutaneous collagenous vasculopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cutaneous collagenous vasculopathy** covering all of the
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


## Comprehensive Research Report: Cutaneous Collagenous Vasculopathy (CCV)

### Executive summary
Cutaneous collagenous vasculopathy (CCV) is a rare, underrecognized superficial cutaneous microangiopathy/vasculopathy characterized clinically by progressive, diffuse telangiectasias and histopathologically by markedly thickened superficial dermal vessel walls with type IV collagen–rich basement membrane reduplication. (grossman2022cutaneouscollagenousvasculopathy pages 1-1, kanitakis2010cutaneouscollagenousvasculopathy pages 1-3)

| Aspect | Summary | Key citations |
|---|---|---|
| Definition | Rare, underrecognized, usually acquired/idiopathic superficial cutaneous microangiopathy/vasculopathy characterized by progressive diffuse telangiectasias and thickened superficial vessel walls with excess type IV collagen. | (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, devore2023cutaneouscollagenousvasculopathy pages 1-3, grossman2022cutaneouscollagenousvasculopathy pages 1-1) |
| Synonyms / related naming | Cutaneous collagenous vasculopathy; CCV; collagenous vasculopathy; proposed variant term: cutaneous papular collagenous vasculopathy (papular form). | (grossman2022cutaneouscollagenousvasculopathy pages 1-1, grossman2022cutaneouscollagenousvasculopathy pages 4-4) |
| Typical age / sex | Most cases occur in middle-aged to older adults; reported age range 16–83 years, mean about 62 years. Published review data: male:female 10:16 in 26 cases; other summaries note no strong sex preference overall. Pediatric/young-adult onset is rare but documented. | (motegi2017cutaneouscollagenousvasculopathy pages 3-4, devore2023cutaneouscollagenousvasculopathy pages 1-3, motegi2017cutaneouscollagenousvasculopathy pages 4-5, rivera2024cutaneouscollagenousvasculopathy pages 1-3) |
| Clinical features | Usually asymptomatic, blanchable fine branching telangiectatic macules/patches, typically starting on lower extremities and spreading proximally to trunk and arms; lesions may darken over time, occasionally bleed, and rare papular/annular variants occur. Mucosa, nails, and usually head/neck are spared; systemic involvement is uncommon. | (motegi2017cutaneouscollagenousvasculopathy pages 3-4, devore2023cutaneouscollagenousvasculopathy pages 1-3, kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, rivera2024cutaneouscollagenousvasculopathy pages 1-3) |
| Histopathology / immunostains / EM | Dilated superficial dermal capillaries and postcapillary venules with marked hyaline eosinophilic PAS-positive wall thickening, basement membrane reduplication/splitting, and immunoreactivity for type IV collagen; Masson trichrome positive. EM may show granular collagenous wall material, thin collagen fibers, occasional activated perivascular fibroblast-like cells, and sometimes long-spacing collagen (Luse bodies), though Luse bodies are not required for diagnosis. | (bondier2017cutaneouscollagenousvasculopathy pages 5-6, devore2023cutaneouscollagenousvasculopathy pages 1-3, kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, rivera2024cutaneouscollagenousvasculopathy pages 1-3) |
| Comorbidities / associations | Frequently reported comorbidities in literature review: hypertension 41.2% (14 cases), diabetes 29.4% (10), dyslipidemia 20.6% (7); broader cardiovascular/related disease in ~62% (16/26). Autoimmune/hypercoagulable associations reported include anti-endothelial cell antibodies, lupus anticoagulant, anti-RNP antibodies, prothrombin G20210A, and cryofibrinogenemia. Rare malignancy associations reported. | (bondier2017cutaneouscollagenousvasculopathy pages 5-6, grossman2022cutaneouscollagenousvasculopathy pages 1-1, devore2023cutaneouscollagenousvasculopathy pages 1-3, motegi2017cutaneouscollagenousvasculopathy pages 4-5) |
| Drug / exposure associations | Reported concomitant drugs include statins 23.5%, beta blockers 18%, calcium channel blockers, corticosteroids, lithium, thiothixene, interferon, isotretinoin, antibiotics, hydroxyurea, antidepressants, losartan, tetracyclines, acyclovir, ketoconazole, and hypertonic saline sclerotherapy; causality remains uncertain in most cases. | (rivera2024cutaneouscollagenousvasculopathy pages 1-3, devore2023cutaneouscollagenousvasculopathy pages 1-3, bondier2017cutaneouscollagenousvasculopathy pages 5-6) |
| Proposed mechanisms | Pathogenesis remains uncertain. Main hypotheses: primary collagen-synthesis abnormality in cutaneous microvasculature; endothelial injury causing occlusive microthrombi, endothelial hyperplasia, and perivascular fibrosis; autoimmune vascular injury; hypercoagulability; and abnormal collagen production by activated perivascular fibroblasts/periadventitial veil cells. Immune- and non-immune endothelial injury are both proposed. | (motegi2017cutaneouscollagenousvasculopathy pages 3-4, grossman2022cutaneouscollagenousvasculopathy pages 1-1, devore2023cutaneouscollagenousvasculopathy pages 1-3, grossman2022cutaneouscollagenousvasculopathy pages 3-4) |
| Differential diagnosis | Generalized essential telangiectasia (major mimic; biopsy needed to distinguish), hereditary hemorrhagic telangiectasia, hereditary benign telangiectasia, ataxia-telangiectasia, angioma serpiginosum, unilateral nevoid telangiectasia, telangiectasia macularis eruptiva perstans, pigmented purpuric dermatoses, poikiloderma, connective tissue diseases, drug-induced telangiectasia, leukocytoclastic vasculitis, and other telangiectatic disorders. | (motegi2017cutaneouscollagenousvasculopathy pages 3-4, rivera2024cutaneouscollagenousvasculopathy pages 1-3, grossman2022cutaneouscollagenousvasculopathy pages 3-4, bondier2017cutaneouscollagenousvasculopathy pages 5-6) |
| Reported treatments / outcomes | No standard systemic therapy. Many cases untreated because disease is benign/cosmetic. Vascular lasers are the main reported intervention: 585-nm pulsed dye laser can produce blanching/improvement; pulsed light also reported beneficial. In one 2023 case, prolonged PDL plus polidocanol sclerotherapy improved cutaneous lesions without major adverse effects. Some lesions remain stable for years without treatment. | (devore2023cutaneouscollagenousvasculopathy pages 1-3, kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, motegi2017cutaneouscollagenousvasculopathy pages 4-5, rivera2024cutaneouscollagenousvasculopathy pages 1-3) |


*Table: This table condenses the main clinicopathologic, epidemiologic, mechanistic, diagnostic, and management findings for cutaneous collagenous vasculopathy. It is useful as a quick reference for knowledge-base curation and differential diagnosis.*

---

## 1. Disease information

### 1.1 Definition and current understanding
CCV is described as an “uncommon microangiopathy” presenting with “progressive telangiectases on the lower extremities that can eventually spread to involve the upper extremities and trunk,” with systemic involvement reported as uncommon. (devore2023cutaneouscollagenousvasculopathy pages 1-3)

Kanitakis et al. (2010-02; *American Journal of Clinical Dermatology*; URL: https://doi.org/10.2165/11311030-000000000-00000) defines CCV as a “very rare entity first described in 2000,” with acquired, progressively diffuse telangiectases and a “histologically distinct aspect” characterized by a “thick hyaline collagenous wall,” with unknown cause. (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3)

### 1.2 Synonyms and alternative names
* Cutaneous collagenous vasculopathy (CCV) (primary term across sources). (devore2023cutaneouscollagenousvasculopathy pages 1-3, rivera2024cutaneouscollagenousvasculopathy pages 1-3)
* Collagenous vasculopathy (shortened usage). (grossman2022cutaneouscollagenousvasculopathy pages 1-1)
* Papular/annular variants have been reported (variant presentations rather than distinct entities). (devore2023cutaneouscollagenousvasculopathy pages 1-3)

### 1.3 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO)
The retrieved primary literature excerpts did **not** provide OMIM, Orphanet, ICD-10/ICD-11, MeSH, or MONDO identifiers for CCV; therefore, these identifiers cannot be confirmed from the current evidence set and should be obtained via direct queries to those terminologies. (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, devore2023cutaneouscollagenousvasculopathy pages 1-3)

### 1.4 Evidence source type
The disease knowledge base evidence is largely derived from **human clinical case reports/series and dermatopathology reviews** (aggregated literature), rather than registry-scale epidemiology or genomics resources. (motegi2017cutaneouscollagenousvasculopathy pages 3-4, bondier2017cutaneouscollagenousvasculopathy pages 5-6)

---

## 2. Etiology

### 2.1 Disease causal factors
Across reviews/case series, the etiology is consistently described as **unknown/idiopathic**. (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, rivera2024cutaneouscollagenousvasculopathy pages 1-3)

### 2.2 Risk factors (genetic, environmental, comorbidities, medications)
**Comorbidity associations (case-aggregation statistics):** Bondier et al. (2017; *American Journal of Dermatopathology*; URL: https://doi.org/10.1097/DAD.0000000000000613) summarizes reported comorbidities among compiled CCV cases, including hypertension in 14 cases (41.2%), diabetes in 10 cases (29.4%), and dyslipidemia in 7 cases (20.6%). (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

**Medication associations:** Bondier et al. notes frequently reported concomitant drugs (not necessarily causal), including statins (8 cases, 23.5%) and beta blockers (6 cases, 18%), and cautions that drug frequency may reflect the frequency of hypertension/dyslipidemia rather than causality. (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

**Autoimmune/hypercoagulable associations:** Grossman et al. (2022; *Journal of Cutaneous Pathology*; URL: https://doi.org/10.1111/cup.14192) reports cases with autoimmune stigmata (anti-endothelial cell antibodies, lupus anticoagulant, anti-RNP antibodies) and one case associated with chronic hydroxyurea therapy. (grossman2022cutaneouscollagenousvasculopathy pages 1-1)

**Genetic factors:** A genetic defect affecting collagen synthesis is discussed as a hypothesis, but **no validated causal gene** is established in the retrieved evidence. (motegi2017cutaneouscollagenousvasculopathy pages 3-4, devore2023cutaneouscollagenousvasculopathy pages 1-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved CCV literature excerpts. (rivera2024cutaneouscollagenousvasculopathy pages 1-3)

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence (e.g., defined loci interacting with exposures) was identified in the retrieved sources; mechanistic discussions remain hypothesis-driven. (motegi2017cutaneouscollagenousvasculopathy pages 3-4, devore2023cutaneouscollagenousvasculopathy pages 1-3)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (signs/symptoms)
**Typical presentation:** Early CCV typically appears as “blanchable pink or red macules, telangiectases, or petechiae on the lower extremities,” progressing to trunk/upper extremities; lesions may darken and bleeding can occur in some cases. (devore2023cutaneouscollagenousvasculopathy pages 1-3)

**Distribution and progression:** CCV is characterized by progressive, widespread telangiectasia on trunk and extremities “without the involvement of mucous membrane and nails.” (motegi2017cutaneouscollagenousvasculopathy pages 3-4)

**Symptoms/impact:** Lesions are commonly asymptomatic and primarily a cosmetic concern, though the appearance may be distressing. (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, rivera2024cutaneouscollagenousvasculopathy pages 1-3)

### 3.2 Age of onset, severity, progression, frequency
**Age:** Reported range 16–83 years, mean age 62 years in one 2023 synthesis; Motegi et al. (2017; URL: https://doi.org/10.1111/ajd.12444) reports mean 62.04±3.11 years across 26 cases, with the youngest at 16 years (rare pediatric case). (devore2023cutaneouscollagenousvasculopathy pages 1-3, motegi2017cutaneouscollagenousvasculopathy pages 3-4)

**Course:** CCV is slowly progressive; stability over long periods can occur (e.g., stable lesions at 7-year follow-up in one case). (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3)

### 3.3 Suggested HPO terms (non-exhaustive)
Based on the reported clinical phenotype:
* Telangiectasia (HP:0001083) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Petechiae (HP:0000967) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Purpura (HP:0000979) / ecchymoses where applicable (clinical spectrum described as violaceous/purple-black patches) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Abnormal skin pigmentation (HP:0000951) (lesions darken over time) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Blanching of erythema (phenotype descriptor; may map to erythema (HP:0000988) with blanching qualifier) (rivera2024cutaneouscollagenousvasculopathy pages 1-3)

### 3.4 Quality of life
No disease-specific validated quality-of-life instruments (e.g., DLQI, SF-36) were reported in the retrieved CCV excerpts; impact is primarily cosmetic/psychosocial. (rivera2024cutaneouscollagenousvasculopathy pages 1-3, kanitakis2010cutaneouscollagenousvasculopathy pages 1-3)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
No causal germline gene(s), pathogenic variants, or Mendelian inheritance pattern have been established in the retrieved evidence; family history was reported as negative in reviewed cases. (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

### 4.2 Molecular tissue signature (type IV collagen)
CCV’s defining molecular-pathology feature is **type IV collagen accumulation/basement membrane reduplication** in superficial dermal vessel walls, demonstrated by collagen type IV immunostaining. (motegi2017cutaneouscollagenousvasculopathy pages 3-4, bondier2017cutaneouscollagenousvasculopathy pages 5-6)

---

## 5. Environmental information
No specific environmental exposures (toxins, occupational exposures, infectious triggers) were identified in the retrieved evidence set. Reported associations are predominantly comorbidities and medications rather than environmental agents. (bondier2017cutaneouscollagenousvasculopathy pages 5-6, devore2023cutaneouscollagenousvasculopathy pages 1-3)

---

## 6. Mechanism / pathophysiology

### 6.1 Proposed causal chain (current hypotheses)
A commonly discussed model is **endothelial injury** (immune-mediated or non-immune) leading to **intravascular occlusive microthrombi**, with downstream **perivascular fibrosis and endothelial hyperplasia**, and ultimately **excess basement membrane/type IV collagen deposition** in superficial dermal vessels. (devore2023cutaneouscollagenousvasculopathy pages 1-3, motegi2017cutaneouscollagenousvasculopathy pages 3-4)

Motegi et al. summarizes that prior reports observed “intravascular organising fibrin thrombi… suggest[ing] that repeated endothelial cell injury may induce intravascular occlusive microthrombosis, leading to endothelial hyperplasia and fibrosis around vessels,” while noting that initiation factors remain unknown. (motegi2017cutaneouscollagenousvasculopathy pages 3-4)

Grossman et al. specifically explores “immune- and non-immune-based endothelial cell injury in the pathogenesis” and reports autoimmune serologies (anti-endothelial cell antibodies; lupus anticoagulant; anti-RNP) and a hydroxyurea-associated case as potential upstream triggers. (grossman2022cutaneouscollagenousvasculopathy pages 1-1)

### 6.2 Cell types and processes (ontology suggestions)
**Likely involved cell types (CL):**
* Endothelial cell (CL:0000115) (endothelial injury hypothesis) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Fibroblast (CL:0000057) (activated perivascular fibroblast collagen synthesis hypothesis) (motegi2017cutaneouscollagenousvasculopathy pages 3-4)

**Candidate GO biological processes (GO):**
* Basement membrane organization (GO:0071711) (type IV collagen/basement membrane reduplication) (bondier2017cutaneouscollagenousvasculopathy pages 5-6)
* Collagen fibril organization (GO:0030199) / extracellular matrix organization (GO:0030198) (perivascular collagen deposition) (motegi2017cutaneouscollagenousvasculopathy pages 3-4)
* Blood coagulation (GO:0007596) / thrombosis-related processes (microthrombi hypothesis) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Endothelial cell activation/injury (broad; captured by inflammatory/vascular injury frameworks) (grossman2022cutaneouscollagenousvasculopathy pages 1-1)

### 6.3 Immune involvement
Autoimmune vascular injury is proposed in some cases (anti-RNP, anti-endothelial cell antibody assays; lupus anticoagulant), suggesting a potential immune contribution in a subset. (devore2023cutaneouscollagenousvasculopathy pages 1-3, grossman2022cutaneouscollagenousvasculopathy pages 1-1)

### 6.4 Molecular profiling and advanced technologies
No transcriptomic/proteomic/metabolomic, single-cell, spatial transcriptomic, or functional genomics screen evidence was identified in the retrieved CCV literature excerpts. (rivera2024cutaneouscollagenousvasculopathy pages 1-3)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
CCV primarily affects the **skin superficial dermal microvasculature** (capillaries and postcapillary venules of the superficial dermis/papillary dermis). (devore2023cutaneouscollagenousvasculopathy pages 1-3, bondier2017cutaneouscollagenousvasculopathy pages 5-6)

**Suggested UBERON terms:**
* Skin of lower limb (UBERON:0004268) (common initial site) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Dermis (UBERON:0002067) (superficial dermal vessels) (bondier2017cutaneouscollagenousvasculopathy pages 5-6)
* Blood vessel (UBERON:0001981) / capillary (UBERON:0002049) (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

### 7.2 Extracutaneous involvement
Extracutaneous manifestations are described as rare; a 2023 case letter reports ocular findings (progressive tortuosity/beading of superficial scleral/episcleral vessels and palpebral conjunctival vessels) in the setting of CCV and retinal bleeding, suggesting that systemic/extracutaneous assessment may be warranted in selected cases. (devore2023cutaneouscollagenousvasculopathy pages 1-3, devore2023cutaneouscollagenousvasculopathy media a372ecf0)

---

## 8. Temporal development

### 8.1 Onset pattern
Onset is typically insidious with gradual progression over years, often beginning on the lower extremities. (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, devore2023cutaneouscollagenousvasculopathy pages 1-3)

### 8.2 Progression
Progression tends to be slow and ascending/proximal, with possible long-term stability. (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3, devore2023cutaneouscollagenousvasculopathy pages 1-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Formal prevalence/incidence estimates were not identified in the retrieved sources; the literature emphasizes rarity and underdiagnosis/underreporting. (devore2023cutaneouscollagenousvasculopathy pages 1-3, kanitakis2010cutaneouscollagenousvasculopathy pages 1-3)

### 9.2 Demographics
CCV affects both sexes; Motegi et al. summarizes male:female ratio 10:16 among 26 reported cases; a 2023 synthesis reports mean age 62 years and predominance in White individuals. (motegi2017cutaneouscollagenousvasculopathy pages 3-4, devore2023cutaneouscollagenousvasculopathy pages 1-3)

### 9.3 Inheritance
Family history is consistently reported as negative in reviewed cases; no autosomal dominant inheritance pattern was found in the compiled reports. (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

---

## 10. Diagnostics

### 10.1 Key diagnostic concept
Because the clinical presentation overlaps with generalized essential telangiectasia and other telangiectatic disorders, **skin biopsy** with special stains and collagen-specific immunostaining is central to diagnosis. (bondier2017cutaneouscollagenousvasculopathy pages 5-6, motegi2017cutaneouscollagenousvasculopathy pages 3-4)

### 10.2 Histopathology (defining features)
Diagnostic histology includes superficial dermal dilated capillaries/postcapillary venules with eosinophilic hyalinized walls that are PAS positive and Masson trichrome positive, with “hyaline eosinophilic deposition of type IV collagen around the affected vessels” and characteristic “duplication of the basal lamina.” (devore2023cutaneouscollagenousvasculopathy pages 1-3)

Bondier et al. explicitly summarizes the “typical” pattern: “dilated blood vessels of the superficial dermal plexus with marked wall thickening due to deposition [of]… PAS positive” material with immunoreactivity to collagen type IV. (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

### 10.3 Dermoscopy (real-world implementation)
Dermoscopy may help distinguish later-stage CCV; Grossman et al. describes “violaceous macules exhibiting tortuous serpiginous vessels” as a distinctive dermoscopic appearance in later-stage disease compared with generalized essential telangiectasia. (grossman2022cutaneouscollagenousvasculopathy pages 3-4)

### 10.4 Differential diagnosis (high priority)
Key clinical differentials include generalized essential telangiectasia (GET) and hereditary hemorrhagic telangiectasia (HHT); biopsy is the reliable discriminator from GET. (bondier2017cutaneouscollagenousvasculopathy pages 5-6, motegi2017cutaneouscollagenousvasculopathy pages 3-4)

Additional differentials listed in recent 2024 clinical literature include angioma serpiginosum, pigmented purpuric dermatoses, telangiectasia macularis eruptiva perstans, poikiloderma, and connective tissue diseases. (rivera2024cutaneouscollagenousvasculopathy pages 1-3)

### 10.5 Genetic testing / omics diagnostics
No genetic testing recommendations specific to CCV were identified; there is no established causal gene in the retrieved literature. (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

---

## 11. Outcome / prognosis

CCV is generally described as benign with chronic course and primarily cosmetic morbidity, with systemic involvement uncommon; lesions may remain stable for years in some patients. (devore2023cutaneouscollagenousvasculopathy pages 1-3, kanitakis2010cutaneouscollagenousvasculopathy pages 1-3)

No survival/mortality statistics or validated prognostic biomarkers were identified in the retrieved evidence set. (devore2023cutaneouscollagenousvasculopathy pages 1-3)

---

## 12. Treatment

### 12.1 Current applications and real-world implementations
Treatment is largely **symptomatic/cosmetic**, with an emphasis on vascular lasers.

DeVore et al. (2023-10; *Cutis*; URL: https://doi.org/10.12788/cutis.0892) states “treatment generally has focused on the use of vascular lasers” and reports a patient treated with pulsed dye laser (PDL) over 3 years with partial improvement, followed by **polidocanol sclerotherapy** (10 mg/mL) leading to “clearance of the majority of telangiectatic vessels,” without adverse effects and with patient satisfaction. (devore2023cutaneouscollagenousvasculopathy pages 1-3)

Rivera et al. (2024-09; *SKIN*; URL: https://doi.org/10.25251/skin.8.5.17) notes “treatment options for CCV remain limited,” and that “pulsed dye laser and pulsed light therapy have been shown to aid in the regression” of lesions (patient lost to follow-up). (rivera2024cutaneouscollagenousvasculopathy pages 1-3)

### 12.2 MAXO term suggestions
* Laser therapy (MAXO:0000507) (PDL/pulsed light) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Sclerotherapy (MAXO:0001012) (polidocanol sclerotherapy in a CCV case) (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Skin biopsy (MAXO:0000475) (diagnostic confirmation) (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

### 12.3 Clinical trials
A ClinicalTrials.gov search via tool did not yield CCV-relevant interventional trials in the retrieved results. (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

---

## 13. Prevention
No primary/secondary prevention strategies are established due to unknown etiology and lack of validated modifiable risk factors; management emphasizes accurate diagnosis to avoid unnecessary testing and to provide reassurance. (rivera2024cutaneouscollagenousvasculopathy pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring CCV-equivalent disease reports in other species were identified in the retrieved evidence set. (bondier2017cutaneouscollagenousvasculopathy pages 5-6)

---

## 15. Model organisms
No model organism (mouse/zebrafish/in vitro genetic model) systems specific to CCV were identified in the retrieved evidence set. (rivera2024cutaneouscollagenousvasculopathy pages 1-3)

---

## Visual documentation from recent literature
Clinical appearance and extracutaneous ocular vascular changes are illustrated in the 2023 case letter (cutaneous lower-extremity lesions and post-treatment improvement; ocular superficial scleral/episcleral vessel dilation/tortuosity). (devore2023cutaneouscollagenousvasculopathy media ac8eef13, devore2023cutaneouscollagenousvasculopathy media 9ca1c09c, devore2023cutaneouscollagenousvasculopathy media a372ecf0)

---

## Notes on evidence gaps and 2023–2024 landscape
* The most actionable 2023–2024 developments in the retrieved set are **expanded phenotypic spectrum** (ocular involvement) and **pragmatic treatment combinations** (PDL + polidocanol sclerotherapy), rather than molecular mechanism breakthroughs. (devore2023cutaneouscollagenousvasculopathy pages 1-3)
* Several large 2024 retrospective analyses/case series appear to exist (based on bibliographic search results) but were **unobtainable** in this session; thus, key 2024 statistics (e.g., n≈34 retrospective series) could not be extracted/verified here without full text access. (devore2023cutaneouscollagenousvasculopathy pages 1-3)



References

1. (grossman2022cutaneouscollagenousvasculopathy pages 1-1): Marc E. Grossman, Marc Cohen, Margaret Ravits, Ralph Blume, and Cynthia M. Magro. Cutaneous collagenous vasculopathy: a report of three cases. Journal of Cutaneous Pathology, 49:491-495, Jan 2022. URL: https://doi.org/10.1111/cup.14192, doi:10.1111/cup.14192. This article has 12 citations and is from a peer-reviewed journal.

2. (kanitakis2010cutaneouscollagenousvasculopathy pages 1-3): Jean Kanitakis, Monique Faisant, Daniel Wagschal, Marek Haftek, and Alain Claudy. Cutaneous collagenous vasculopathy. American Journal of Clinical Dermatology, 11:63-66, Feb 2010. URL: https://doi.org/10.2165/11311030-000000000-00000, doi:10.2165/11311030-000000000-00000. This article has 37 citations and is from a peer-reviewed journal.

3. (devore2023cutaneouscollagenousvasculopathy pages 1-3): Ansley Devore, H. Alshaikh, and Dirk M Elston. Cutaneous collagenous vasculopathy with ocular involvement. Cutis, 112 4:E40-E42, Oct 2023. URL: https://doi.org/10.12788/cutis.0892, doi:10.12788/cutis.0892. This article has 3 citations and is from a peer-reviewed journal.

4. (grossman2022cutaneouscollagenousvasculopathy pages 4-4): Marc E. Grossman, Marc Cohen, Margaret Ravits, Ralph Blume, and Cynthia M. Magro. Cutaneous collagenous vasculopathy: a report of three cases. Journal of Cutaneous Pathology, 49:491-495, Jan 2022. URL: https://doi.org/10.1111/cup.14192, doi:10.1111/cup.14192. This article has 12 citations and is from a peer-reviewed journal.

5. (motegi2017cutaneouscollagenousvasculopathy pages 3-4): Sei‐ichiro Motegi, Masahito Yasuda, Masayoshi Yamanaka, Hiroo Amano, and Osamu Ishikawa. Cutaneous collagenous vasculopathy: report of first japanese case and review of the literature. Australasian Journal of Dermatology, 58:145-149, May 2017. URL: https://doi.org/10.1111/ajd.12444, doi:10.1111/ajd.12444. This article has 26 citations and is from a peer-reviewed journal.

6. (motegi2017cutaneouscollagenousvasculopathy pages 4-5): Sei‐ichiro Motegi, Masahito Yasuda, Masayoshi Yamanaka, Hiroo Amano, and Osamu Ishikawa. Cutaneous collagenous vasculopathy: report of first japanese case and review of the literature. Australasian Journal of Dermatology, 58:145-149, May 2017. URL: https://doi.org/10.1111/ajd.12444, doi:10.1111/ajd.12444. This article has 26 citations and is from a peer-reviewed journal.

7. (rivera2024cutaneouscollagenousvasculopathy pages 1-3): Claudia S. Roldan Rivera, Fabiola Moreno Echevarria, Alyce Anderson, and Jennifer L. Shastry. Cutaneous collagenous vasculopathy in a young adult: a case report. SKIN The Journal of Cutaneous Medicine, 8:1878-1880, Sep 2024. URL: https://doi.org/10.25251/skin.8.5.17, doi:10.25251/skin.8.5.17. This article has 0 citations.

8. (bondier2017cutaneouscollagenousvasculopathy pages 5-6): Laure Bondier, Mathilde Tardieu, Perrine Leveque, Isabelle Challende, Nicole Pinel, and Marie T. Leccia. Cutaneous collagenous vasculopathy: report of two cases presenting as disseminated telangiectasias and review of the literature. The American Journal of dermatopathology, 39 9:682-688, Sep 2017. URL: https://doi.org/10.1097/dad.0000000000000613, doi:10.1097/dad.0000000000000613. This article has 33 citations.

9. (grossman2022cutaneouscollagenousvasculopathy pages 3-4): Marc E. Grossman, Marc Cohen, Margaret Ravits, Ralph Blume, and Cynthia M. Magro. Cutaneous collagenous vasculopathy: a report of three cases. Journal of Cutaneous Pathology, 49:491-495, Jan 2022. URL: https://doi.org/10.1111/cup.14192, doi:10.1111/cup.14192. This article has 12 citations and is from a peer-reviewed journal.

10. (devore2023cutaneouscollagenousvasculopathy media a372ecf0): Ansley Devore, H. Alshaikh, and Dirk M Elston. Cutaneous collagenous vasculopathy with ocular involvement. Cutis, 112 4:E40-E42, Oct 2023. URL: https://doi.org/10.12788/cutis.0892, doi:10.12788/cutis.0892. This article has 3 citations and is from a peer-reviewed journal.

11. (devore2023cutaneouscollagenousvasculopathy media ac8eef13): Ansley Devore, H. Alshaikh, and Dirk M Elston. Cutaneous collagenous vasculopathy with ocular involvement. Cutis, 112 4:E40-E42, Oct 2023. URL: https://doi.org/10.12788/cutis.0892, doi:10.12788/cutis.0892. This article has 3 citations and is from a peer-reviewed journal.

12. (devore2023cutaneouscollagenousvasculopathy media 9ca1c09c): Ansley Devore, H. Alshaikh, and Dirk M Elston. Cutaneous collagenous vasculopathy with ocular involvement. Cutis, 112 4:E40-E42, Oct 2023. URL: https://doi.org/10.12788/cutis.0892, doi:10.12788/cutis.0892. This article has 3 citations and is from a peer-reviewed journal.