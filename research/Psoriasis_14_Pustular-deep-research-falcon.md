---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:56:03.121721'
end_time: '2026-05-09T10:23:00.663072'
duration_seconds: 1617.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Psoriasis 14, Pustular
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Psoriasis 14, Pustular
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Psoriasis 14, Pustular** covering all of the
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
- **Disease Name:** Psoriasis 14, Pustular
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Psoriasis 14, Pustular** covering all of the
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


# Psoriasis 14, Pustular (Mendelian) — Disease Characteristics Research Report

## Executive overview
“Pustular psoriasis” is a clinically heterogeneous spectrum of inflammatory skin disorders characterized by erythematous plaques bearing *sterile* pustules, with major subtypes including generalized pustular psoriasis (GPP), acrodermatitis continua of Hallopeau (ACH), and palmoplantar pustular psoriasis/palmoplantar pustulosis (PPP/PPPP). (akiyama2022pustularpsoriasisas pages 1-2) Among these, GPP is a severe autoinflammatory disease with episodic or persistent sterile pustulation that can be life-threatening and is increasingly understood as driven by innate immune activation centered on the IL-36 axis. (akiyama2022pustularpsoriasisas pages 1-2, gwillim2024spesolimabforgeneralized pages 1-2)

“Psoriasis 14, pustular” corresponds to a Mendelian disease concept in MONDO (MONDO_0013626) and is linked to genes that predispose to pustular psoriasis, including **AP1S3**, **IL36RN**, and **CARD14** in Open Targets disease–target associations. (OpenTargets Search: pustular psoriasis)

## 1. Disease information
### 1.1 What is the disease?
**Psoriasis 14, pustular** is best interpreted operationally as a monogenic/Mendelian entity within the *pustular psoriasis* spectrum, in which rare high-impact variants (especially in **AP1S3** and IL-36 pathway genes) predispose to pustular phenotypes (GPP/ACH/PPP) with sterile pustules and variable systemic inflammation. (OpenTargets Search: pustular psoriasis, settakaffetzi2014ap1s3mutationsare pages 2-4, akiyama2022pustularpsoriasisas pages 1-2)

### 1.2 Key identifiers
**Available from tool-supported evidence in this run**:
- **MONDO**: 
  - Psoriasis 14, pustular: **MONDO_0013626** (OpenTargets Search: pustular psoriasis)
  - Pustular psoriasis (umbrella): **MONDO_0022205** (OpenTargets Search: pustular psoriasis)
  - Generalized pustular psoriasis: **MONDO_0100491** (OpenTargets Search: pustular psoriasis)

**Not retrieved in the currently available full texts/evidence snippets** (therefore cannot be asserted here): OMIM disease number, Orphanet ID, MeSH descriptor, ICD-10/ICD-11 code.

### 1.3 Synonyms / alternative names (as used in the literature)
For the *clinical spectrum* relevant to PSORS14, commonly used disease labels include:
- **Generalized pustular psoriasis (GPP)**, including “von Zumbusch” acute form (choon2022clinicalcourseand pages 4-6)
- **Acrodermatitis continua of Hallopeau (ACH)** (bachelez2020pustularpsoriasisthe pages 3-4)
- **Palmoplantar pustulosis / palmoplantar pustular psoriasis (PPP/PPPP)** (bachelez2020pustularpsoriasisthe pages 3-4, navarini2017europeanconsensusstatement pages 1-4)

### 1.4 Evidence source types
The PSORS14 concept is supported primarily by:
- **Aggregated disease-level resources** (e.g., MONDO/Open Targets mappings) (OpenTargets Search: pustular psoriasis)
- **Human genetics case-control and case series studies** discovering/enriching rare variants (settakaffetzi2014ap1s3mutationsare pages 2-4, mossner2018thegeneticbasis pages 15-19)
- **Human keratinocyte functional studies** for causal mechanism (in vitro; patient-derived keratinocytes) (settakaffetzi2014ap1s3mutationsare pages 4-6, mahil2016ap1s3mutationscause pages 10-14)

## 2. Etiology
### 2.1 Disease causal factors
**Primary causal factors are genetic**, with additional triggering by environmental/iatrogenic factors precipitating flares.

#### Genetic causes / strong predisposing genes
- **AP1S3 (loss-of-function / destabilizing missense alleles)**: discovery of enriched heterozygous founder variants in pustular psoriasis; functional mechanism via disrupted vesicular trafficking (TLR3) and keratinocyte inflammatory dysregulation. (settakaffetzi2014ap1s3mutationsare pages 2-4, settakaffetzi2014ap1s3mutationsare pages 4-6)
- **IL36RN (IL-36 receptor antagonist deficiency; DITRA)**: biallelic loss-of-function variants are a major cause of many GPP cases and show an autosomal recessive pattern in those families. (yang2023geneticsofgeneralized pages 2-3, yang2023geneticsofgeneralized pages 3-5)
- **CARD14 (gain-of-function)**: heterozygous GOF variants can drive psoriasis phenotypes and are implicated in subsets of pustular psoriasis, including familial autosomal-dominant pedigrees in the broader pustular psoriasis literature. (bachelez2020pustularpsoriasisthe pages 3-4, akiyama2022pustularpsoriasisas pages 2-3)

#### Environmental/iatrogenic triggers (flare precipitants)
For GPP (and relevant pustular phenotypes), triggers include:
- **Withdrawal of systemic corticosteroids** (reported up to ~20% in one review) (choon2022clinicalcourseand pages 3-4)
- **Infections (notably URTIs)**, **stress**, **pregnancy**, **menstruation**, **hypocalcemia**, and multiple medications; biologics can also be triggers in some contexts (e.g., rebound/withdrawal or paradoxical pustulation). (choon2022clinicalcourseand pages 2-3, choon2022clinicalcourseand pages 3-4)

### 2.2 Risk factors
- **Female predominance** has been reported for PPP/PPPP and in several GPP cohorts. (bachelez2020pustularpsoriasisthe pages 3-4, riveradiaz2023generalizedpustularpsoriasis pages 3-4)
- **Smoking** is strongly linked to palmoplantar pustular psoriasis/palmoplantar pustulosis. (bachelez2020pustularpsoriasisthe pages 3-4)
- **Genotype-driven risk**: IL36RN biallelic mutations are associated with earlier onset and more severe/systemic disease features. (akiyama2022pustularpsoriasisas pages 2-3, choon2022clinicalcourseand pages 4-6)

### 2.3 Protective factors
No disease-specific protective genetic or environmental factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interaction
The AP1S3 discovery study supports a model in which heterozygous AP1S3 variants may be **incompletely penetrant**, with flares requiring environmental/inflammatory triggers; affected individuals could inherit the allele from an unaffected parent. (settakaffetzi2014ap1s3mutationsare pages 2-4)

## 3. Phenotypes
Because PSORS14 is best supported by genetics tied to *pustular psoriasis phenotypes*, the phenotype section focuses on pustular psoriasis subtypes, especially GPP (the best-characterized in retrieved sources).

### 3.1 Core clinical features (symptoms/signs)
**Generalized pustular psoriasis (GPP)**
- Hallmark: recurrent **widespread painful erythema** with **sterile pustules** that may coalesce into “lakes of pus.” (choon2022clinicalcourseand pages 4-6, riveradiaz2023generalizedpustularpsoriasis pages 3-4)
- Systemic symptoms during significant flares: **fever**, malaise/fatigue, edema; extracutaneous manifestations can include **arthritis**, **uveitis**, and **neutrophilic cholangitis**. (choon2022clinicalcourseand pages 4-6, choon2022clinicalcourseand pages 3-4)
- Laboratory abnormalities during flares: **leukocytosis/neutrophilia**, elevated **CRP**, **hypocalcemia**, **hypoalbuminemia**, and abnormal liver function tests. (choon2022clinicalcourseand pages 4-6, riveradiaz2023generalizedpustularpsoriasis pages 3-4)
- Course: relapsing-remitting or persistent; typical flares last **2–5 weeks**, but may persist >3 months in chronic variants. (choon2022clinicalcourseand pages 4-6, riveradiaz2023generalizedpustularpsoriasis pages 3-4)

**Acrodermatitis continua of Hallopeau (ACH)**
- Persistent pustulation affecting digits/nail apparatus; may cause **progressive nail destruction** and **bone erosions** if untreated. (bachelez2020pustularpsoriasisthe pages 3-4, navarini2017europeanconsensusstatement pages 1-4)

**Palmoplantar pustulosis / palmoplantar pustular psoriasis (PPP/PPPP)**
- Persistent sterile pustules on **palms and soles**; chronic course; strongly associated with smoking; can cause major quality-of-life impairment. (bachelez2020pustularpsoriasisthe pages 3-4, navarini2017europeanconsensusstatement pages 1-4)

### 3.2 Onset, severity, progression, frequency (data)
- In one single-center series of severe flares (>30% BSA) followed for ~5 years: **56.8%** had one severe flare; **29.5%** had 2–5 flares; **13.7%** had >5 flares. (choon2022clinicalcourseand pages 3-4)
- Hospitalization is often required for significant flares; one review reports hospitalization for **~50% of flares** and average inpatient stay **10–14 days**. (choon2022clinicalcourseand pages 4-6)
- Mortality attributable to GPP or its treatment is reported to range **2–16%** across studies; a Japanese inpatient study reported **4.2%** in-hospital mortality (higher with systemic corticosteroid monotherapy, lower with biologics). (choon2022clinicalcourseand pages 4-6)

### 3.3 Quality-of-life impact
GPP is described as having substantial burden and impaired quality of life, motivating development of targeted therapies and disease-specific endpoints. (gwillim2024spesolimabforgeneralized pages 1-2, choon2022clinicalcourseand pages 4-6)

### 3.4 Suggested HPO terms (examples)
(These are ontology suggestions based on described phenotypes; explicit HPO mappings were not provided in retrieved texts.)
- Sterile pustules: **HP:0100704 (Pustule)**
- Erythema: **HP:0025504 (Erythema)**
- Fever: **HP:0001945 (Fever)**
- Arthralgia/arthritis: **HP:0002829 (Arthralgia)** / **HP:0001369 (Arthritis)**
- Nail dystrophy/destruction (ACH): **HP:0001800 (Nail dystrophy)**
- Elevated C-reactive protein: **HP:0011227 (Elevated C-reactive protein)**
- Neutrophilia/leukocytosis: **HP:0011891 (Neutrophilia)** / **HP:0001974 (Leukocytosis)**
- Hypocalcemia: **HP:0002901 (Hypocalcemia)**
- Hypoalbuminemia: **HP:0003073 (Hypoalbuminemia)**

## 4. Genetic / molecular information
### 4.1 Causal genes and inheritance
#### AP1S3
**Key concept:** heterozygous AP1S3 founder missense variants are enriched in pustular psoriasis and functionally impair AP-1 adaptor complex biology.
- Reported variants (discovery paper):
  - **c.11T>G (p.Phe4Cys)**
  - **c.97C>T (p.Arg33Trp)** (settakaffetzi2014ap1s3mutationsare pages 2-4, settakaffetzi2014ap1s3mutationsare pages 4-6)
- Case-control enrichment (discovery paper): c.11T>G 2.3% cases vs 0.6% controls; c.97C>T 3.6% vs 0.7%; combined significance exceeded exome-wide threshold. (settakaffetzi2014ap1s3mutationsare pages 2-4)
- **Inheritance/penetrance:** heterozygous carriage with segregation from unaffected parent supports **dominant with reduced penetrance / susceptibility allele** model. (settakaffetzi2014ap1s3mutationsare pages 2-4)

**Visual evidence:** Table/figure regions enumerating AP1S3 variants and frequencies are captured from the discovery paper. (settakaffetzi2014ap1s3mutationsare media 63a65913, settakaffetzi2014ap1s3mutationsare media fcbc7708, settakaffetzi2014ap1s3mutationsare media 0828eba0)

#### IL36RN
- Biallelic loss-of-function IL36RN variants are described as a major cause of GPP in many cases and are **autosomal recessive** in the classic DITRA model; allele dosage relates to age of onset and severity. (yang2023geneticsofgeneralized pages 2-3, yang2023geneticsofgeneralized pages 3-5)
- Example IL36RN variants shown as relevant to pustular subtypes include **c.115+6T>C**, **p.Pro76Leu**, and **p.Ser113Leu**. (twelves2019clinicalandgenetic pages 1-2)
- Oligogenic contribution: heterozygous IL36RN variants are overrepresented compared with the general population and may contribute in combination with other rare variants (e.g., AP1S3/CARD14). (mossner2018thegeneticbasis pages 15-19)

#### CARD14
- Reviews describe **heterozygous gain-of-function** CARD14 variants as drivers of psoriasis phenotypes and contributors to pustular psoriasis in subsets; autosomal dominant familial GPP is reported in this broader CARD14 GOF context. (bachelez2020pustularpsoriasisthe pages 3-4, akiyama2022pustularpsoriasisas pages 2-3)

#### Additional genes reported in GPP genetics reviews
MPO, SERPINA1, SERPINA3, BTN3A3, among others, have been described as associated/predisposing genes for GPP in recent genetics reviews, but inheritance patterns and variant-level details were not consistently extractable from the retrieved snippets. (yang2023geneticsofgeneralized pages 2-3, yang2023geneticsofgeneralized pages 3-5)

### 4.2 Functional consequences (mechanistic genetics)
- AP1S3 discovery work supports **loss-of-function** through destabilization of AP1S3 or disruption of AP-1 complex interactions, impairing endosomal trafficking of **TLR3** and downstream signaling (e.g., reduced IFNB1 induction to poly(I:C)). (settakaffetzi2014ap1s3mutationsare pages 4-6)
- Subsequent mechanistic work connects AP1S3 deficiency to **defective keratinocyte autophagy**, **p62 accumulation**, **enhanced NF-κB signaling**, and **upregulated IL-36α** production. (mahil2016ap1s3mutationscause pages 10-14, mahil2016ap1s3mutationscause pages 6-10, mahil2016ap1s3mutationscause pages 1-6)

### 4.3 Modifier genes / oligogenic architecture
Evidence supports that some pustular psoriasis patients show multiple rare variants across IL36RN/AP1S3/CARD14, consistent with **oligogenic inheritance/modifier effects** in subsets. (mossner2018thegeneticbasis pages 15-19, bachelez2020pustularpsoriasisthe pages 3-4)

### 4.4 Allele frequency and founder effects
The AP1S3 discovery paper reports intragenic haplotype associations consistent with founder alleles for the two AP1S3 variants. (settakaffetzi2014ap1s3mutationsare pages 2-4)

## 5. Environmental information
Strongest evidence in retrieved materials is for **iatrogenic and physiologic triggers** rather than toxins/pollutants.
- Triggers include corticosteroid withdrawal, infections, stress, pregnancy/menstruation, and multiple medications. (choon2022clinicalcourseand pages 2-3, choon2022clinicalcourseand pages 3-4)
- PPP/PPPP shows a strong association with **smoking**. (bachelez2020pustularpsoriasisthe pages 3-4)

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic understanding (key concepts)
A contemporary framing is that pustular psoriasis is an **autoinflammatory keratinization disease (AiKD)** with hyperactivation of skin innate immune signaling, especially the **IL-1/IL-36 axis**, leading to chemokine induction and neutrophil recruitment. (akiyama2022pustularpsoriasisas pages 1-2, gwillim2024spesolimabforgeneralized pages 1-2)

### 6.2 Causal chain (genotype → pathway → lesion)
**Representative chain for AP1S3-associated pustular psoriasis (human keratinocyte evidence):**
1) **AP1S3 loss-of-function** (p.Phe4Cys/p.Arg33Trp) disrupts AP-1 adaptor function and autophagosome biology in keratinocytes. (settakaffetzi2014ap1s3mutationsare pages 4-6, mahil2016ap1s3mutationscause pages 6-10)
2) **Defective autophagy** leads to **p62/SQSTM1 accumulation** with downstream **NF-κB hyperactivation**. (mahil2016ap1s3mutationscause pages 6-10, mahil2016ap1s3mutationscause pages 1-6)
3) Keratinocytes exhibit exaggerated innate responses (TLR2/6 and IL-1–responsive cytokines) and **constitutive upregulation of IL36A (IL-36α)** and related inflammatory mediators. (mahil2016ap1s3mutationscause pages 10-14)
4) Unopposed IL-36 signaling amplifies the **IL-36–chemokine–neutrophil axis**, driving sterile neutrophilic pustules and systemic inflammation in severe disease. (gwillim2024spesolimabforgeneralized pages 1-2)

### 6.3 Cell types (CL term suggestions)
- Keratinocyte: **CL:0000312** (supported by AP1S3 expression and keratinocyte-autonomous mechanism). (mahil2016ap1s3mutationscause pages 6-10)
- Neutrophil: **CL:0000775** (dominant infiltrating cell type in pustules; IL-36–chemokine–neutrophil axis). (gwillim2024spesolimabforgeneralized pages 1-2)

### 6.4 GO biological process suggestions
- Neutrophil chemotaxis (GO:0030593) / neutrophil activation (GO:0042119)
- Cytokine-mediated signaling pathway (GO:0019221)
- NF-κB signaling (GO:0043122)
- Autophagy (GO:0006914)

### 6.5 Molecular profiling (omics)
Longitudinal blood transcriptomics in GPP (PBMC RNA-seq) showed that remission after acitretin was associated with downregulation of neutrophil-related inflammatory genes (e.g., CXCL1, CXCL8, S100A8/A9/A12, LCN2) and pathway-level inhibition of pro-inflammatory signaling. (yang2023geneticsofgeneralized pages 2-3)

## 7. Anatomical structures affected
### 7.1 Primary organs/tissues
- Skin epidermis/dermis (sterile pustules, erythema). (choon2022clinicalcourseand pages 4-6)

### 7.2 Specific anatomical sites (UBERON suggestions)
- Skin of body (UBERON:0002097)
- Palm (UBERON:0002387) and sole (UBERON:0002388) for PPP/PPPP
- Nail unit (UBERON:0001828) for ACH

### 7.3 Subcellular components (GO-CC suggestions)
- Endosome (GO:0005768) / trans-Golgi network (GO:0005802) (AP1S3 trafficking biology) (settakaffetzi2014ap1s3mutationsare pages 4-6)
- Autophagosome (GO:0005776) (AP1S3-autophagy mechanism) (mahil2016ap1s3mutationscause pages 6-10)

## 8. Temporal development
- GPP can be relapsing with disease-free intervals of months to years or persistent with chronic pustulation >3 months (ERASPEN framework). (navarini2017europeanconsensusstatement pages 1-4)
- Severe flares can evolve rapidly (≤7 days for von Zumbusch acute GPP) and can be medically emergent. (riveradiaz2023generalizedpustularpsoriasis pages 3-4)

## 9. Inheritance and population
### 9.1 Inheritance patterns
- **IL36RN-associated GPP**: typically **autosomal recessive** for biallelic LOF, with allele-dose effects on severity and age of onset; heterozygous variants may act oligogenically. (yang2023geneticsofgeneralized pages 3-5, mossner2018thegeneticbasis pages 15-19)
- **AP1S3-associated pustular psoriasis (PSORS14 concept)**: heterozygous enriched variants; evidence supports **dominant with reduced penetrance / susceptibility** rather than strict Mendelian segregation. (settakaffetzi2014ap1s3mutationsare pages 2-4)
- **CARD14 GOF**: can be autosomal dominant in familial psoriasis contexts; also implicated in pustular subsets. (bachelez2020pustularpsoriasisthe pages 3-4)

### 9.2 Epidemiology (best-available in retrieved evidence)
Population-based estimates are scarce and vary by definition. Reported prevalence estimates include approximately **1–7 per million** globally and a Swedish registry estimate of **9.1 per 100,000** (female predominance) as cited in a 2023 review. (riveradiaz2023generalizedpustularpsoriasis pages 3-4)

## 10. Diagnostics
### 10.1 Clinical criteria / definitions
- **ERASPEN (European consensus)**: GPP defined by “primary, sterile, macroscopically visible pustules on non-acral skin,” excluding pustulation restricted to psoriatic plaques; classification into relapsing (>1 episode) vs persistent (>3 months) and by coexisting psoriasis vulgaris. (navarini2017europeanconsensusstatement pages 1-4, fujita2022diagnosisofgeneralized pages 1-2)
- **Japanese Dermatological Association (JDA) diagnostic criteria**: require systemic symptoms (e.g., fever/fatigue), extensive erythema with multiple sterile pustules (may form lakes of pus), histopathology showing neutrophilic subcorneal pustules (Kogoj spongiform pustules), and recurrence. (puig2023generalizedpustularpsoriasis pages 6-6)

### 10.2 Laboratory and pathology findings
- Suggested evaluation includes CBC with differential (leukocytosis/neutrophilia), CRP/ESR, albumin, electrolytes (including calcium), and organ function tests to evaluate systemic inflammation and complications. (puig2023generalizedpustularpsoriasis pages 6-6, ly2019diagnosisandscreening pages 2-3)
- Histopathology often shows Kogoj spongiform pustules and psoriasis features including Munro microabscesses. (ly2019diagnosisandscreening pages 2-3)

### 10.3 Differential diagnosis
Key differential includes **acute generalized exanthematous pustulosis (AGEP)**, which can mimic GPP; differentiation relies on clinical course (shorter, nonrecurrent), drug exposure history, lack of psoriasis history, and histopathologic clues (e.g., eosinophilia/necrotic keratinocytes in AGEP). (ly2019diagnosisandscreening pages 2-3, bachelez2020pustularpsoriasisthe pages 3-4)

### 10.4 Clinical outcome measures
GPP-specific measures developed to address limitations of PASI/PGA include:
- **GPPGA (Generalized Pustular Psoriasis Physician Global Assessment)**
- **GPPASI (Generalized Pustular Psoriasis Area and Severity Index)** (burden2022clinicaldiseasemeasures pages 1-3)

### 10.5 Genetic testing strategy (knowledge-base oriented)
For pustular psoriasis phenotypes consistent with PSORS14/GPP/ACH, consider targeted sequencing/panels including **IL36RN, AP1S3, CARD14** (and expanded panels as clinically appropriate) to support subtype definition and potential targeted therapy decisions. (ly2019diagnosisandscreening pages 2-3, akiyama2022pustularpsoriasisas pages 1-2)

## 11. Outcomes / prognosis
- Severe GPP flares can lead to sepsis and organ failure; reported mortality attributable to GPP/treatment ranges **2–16%** across studies summarized in a 2022 review, with substantial hospitalization rates. (choon2022clinicalcourseand pages 4-6)

## 12. Treatment
### 12.1 Current applications and real-world implementation (2023–2024 priority)
#### IL-36 receptor inhibitors (targeted therapy; major 2022–2024 advance)
**Spesolimab (anti–IL-36R)**
- Regulatory status: US FDA approval **September 2022** for adult GPP flares (reviewed in 2024). (gwillim2024spesolimabforgeneralized pages 1-2)
- Acute flare RCT (Effisayil 1; NCT03782792): at week 1, **pustulation clearance (GPPGA pustulation subscore 0)** in **19/35 (54%)** spesolimab vs **1/18 (6%)** placebo (P<0.001); **GPPGA total 0/1** in **15/35 (43%)** vs **2/18 (11%)** (P=0.02). (gwillim2024spesolimabforgeneralized pages 1-2)
- Safety signal (acute): week-1 infections **6/35 (17%)** spesolimab vs **1/18 (6%)** placebo. (gwillim2024spesolimabforgeneralized pages 1-2)
- Flare prevention trial (Effisayil 2; NCT04399837): a 2024 systematic review summary reports by week 48 flare rates of **10% (high-dose)** vs **52% placebo**, with HR **0.16** (time to first flare) in high-dose vs placebo. (puig2024currenttreatmentsfor pages 19-21)

**Imsidolimab (ANB019; anti–IL-36R)**
- Phase 2 open-label regimen (NCT03619902): 750 mg IV day 1 followed by 100 mg SC on days 29/57/85; primary endpoints included CGI response at weeks 4 and 16 and percent change in pustular erythema BSA. (NCT03619902 chunk 1)
- Phase 3 RCT record (NCT05352893): randomized, double-blind, placebo-controlled with IV 750 mg and 300 mg arms; primary endpoint is GPPPGA clear/almost clear at week 4. (NCT05352893 chunk 1)

**Expert interpretation (authoritative synthesis)**
A 2024 review emphasizes that abnormal IL-36 signaling has a central role in GPP and that spesolimab provides “rapid and sustained clinical improvement,” reflecting a shift from off-label plaque-psoriasis paradigms toward disease-specific targeted therapy. (gwillim2024spesolimabforgeneralized pages 1-2)

### 12.2 Conventional systemic options (context)
Before IL-36R inhibitors, commonly used systemic therapies for GPP included retinoids, cyclosporine, and methotrexate, largely supported by case reports/small studies rather than robust RCT evidence. (bernardo2024spesolimabforthe pages 2-3)

### 12.3 MAXO term suggestions
- Anti–IL-36 receptor monoclonal antibody therapy: **MAXO:0000000 (placeholder; requires ontology lookup outside current tool context)**
- Systemic retinoid therapy; calcineurin inhibitor therapy; antimetabolite therapy (methotrexate) (MAXO terms not resolvable from provided tool context).

## 13. Prevention
Primary prevention is not established for Mendelian pustular psoriasis phenotypes; practical prevention focuses on **avoiding known triggers** (e.g., systemic corticosteroid withdrawal, implicated medications) and **flare prevention** using maintenance strategies such as subcutaneous spesolimab protocols studied in Effisayil 2. (choon2022clinicalcourseand pages 2-3, puig2024currenttreatmentsfor pages 19-21)

## 14. Other species / natural disease
No other-species naturally occurring PSORS14/AP1S3-driven pustular psoriasis evidence was retrieved in this run.

## 15. Model organisms and experimental models
### 15.1 In vitro / cellular models (direct evidence)
- Human keratinocyte models (HaCaT/HEK293; patient-derived keratinocytes) demonstrate AP1S3-dependent defects in TLR3 trafficking and autophagy, supporting a keratinocyte-autonomous disease mechanism. (settakaffetzi2014ap1s3mutationsare pages 4-6, mahil2016ap1s3mutationscause pages 6-10)

### 15.2 Suggested in vivo model directions (not directly retrieved)
No mouse genetic model for AP1S3-driven pustular psoriasis was identified in retrieved evidence. Mechanistic plausibility suggests keratinocyte-specific autophagy pathway perturbation models may recapitulate aspects of inflammation, but explicit AP1S3 animal models require additional retrieval.

---

## Recent developments (2023–2024 highlights)
1) **Genetics consolidation and therapeutic implications**: 2023 genetics review emphasizes IL36RN’s causal role (autosomal recessive biallelic disease) and the expanding gene list (including AP1S3, MPO, SERPIN genes), framing IL-36 axis targeting as mechanism-driven therapy. (yang2023geneticsofgeneralized pages 2-3)
2) **Targeted IL-36R blockade becomes standard of care for flares**: 2024 review summarizes that spesolimab was FDA-approved in Sept 2022 and provides RCT-level efficacy with rapid pustule clearance; flare-prevention studies (Effisayil 2) extend the paradigm toward chronic disease control. (gwillim2024spesolimabforgeneralized pages 1-2, puig2024currenttreatmentsfor pages 19-21)
3) **Clinical practice evolution**: newer trials and systematic reviews note improved standardization using GPP-specific endpoints (GPPGA/GPPASI), addressing prior limitations of psoriasis-vulgaris instruments. (burden2022clinicaldiseasemeasures pages 1-3, gwillim2024spesolimabforgeneralized pages 1-2)

---

## Evidence table (quick reference)
The following table consolidates identifiers, key genes/variants, and IL-36R inhibitor trial outcomes.

| Category | Entity | Identifier(s) explicitly available from gathered evidence | Key details | Year | Citation(s) |
|---|---|---|---|---|---|
| Disease concept | Psoriasis 14, pustular | **MONDO:** MONDO_0013626; **OMIM:** 614204 (explicitly mentioned in review snippet linking PSORS14 to pustular psoriasis) | Mendelian pustular psoriasis entity within the pustular psoriasis spectrum; Open Targets also maps MONDO_0013626 to AP1S3, IL36RN, CARD14 | 2020-2024 | (OpenTargets Search: pustular psoriasis, settakaffetzi2014ap1s3mutationsare pages 2-4) |
| Disease concept | Pustular psoriasis | **MONDO:** MONDO_0022205 | Umbrella term covering GPP, ACH, PPP/PPPP; clinically heterogeneous autoinflammatory keratinization disease spectrum | 2022-2024 | (OpenTargets Search: pustular psoriasis, akiyama2022pustularpsoriasisas pages 1-2, bachelez2020pustularpsoriasisthe pages 3-4) |
| Disease concept | Generalized pustular psoriasis (GPP) | **MONDO:** MONDO_0100491 | Severe relapsing/life-threatening subtype characterized by widespread sterile pustules, erythema, fever/systemic inflammation | 2022-2024 | (OpenTargets Search: pustular psoriasis, yang2023geneticsofgeneralized pages 1-2, choon2022clinicalcourseand pages 4-6) |
| Gene | **AP1S3** | Disease association to PSORS14 supported; no HGNC/OMIM gene ID explicitly extracted | Discovery paper identified heterozygous founder missense variants **c.11T>G (p.Phe4Cys)** and **c.97C>T (p.Arg33Trp)** in pustular psoriasis; variants enriched in cases vs controls; inheritance appears **dominant with reduced penetrance / susceptibility allele model** rather than classic recessive inheritance | 2014, 2016, 2022-2023 | (settakaffetzi2014ap1s3mutationsare pages 2-4, settakaffetzi2014ap1s3mutationsare pages 4-6, settakaffetzi2014ap1s3mutationsare pages 1-2, mossner2018thegeneticbasis pages 15-19, mahil2016ap1s3mutationscause pages 10-14) |
| Gene | **IL36RN** | Associated with pustular psoriasis/GPP; no explicit OMIM for gene extracted | Major causal gene for many GPP cases; **biallelic homozygous/compound heterozygous loss-of-function** variants cause disease with **autosomal recessive** pattern in many families; heterozygous alleles may contribute oligogenically; exemplar variants shown in subtype paper include **c.115+6T>C, p.Pro76Leu, p.Ser113Leu** | 2019, 2022-2023 | (yang2023geneticsofgeneralized pages 2-3, twelves2019clinicalandgenetic pages 1-2, akiyama2022pustularpsoriasisas pages 2-3, mossner2018thegeneticbasis pages 15-19, yang2023geneticsofgeneralized pages 3-5) |
| Gene | **CARD14** | Associated with pustular psoriasis/PSORS14 spectrum | **Heterozygous gain-of-function** variants reported in pustular psoriasis and plaque psoriasis overlap; **autosomal dominant** familial GPP described in reviews; specific variants not extracted in gathered evidence set | 2020, 2022-2023 | (bachelez2020pustularpsoriasisthe pages 3-4, akiyama2022pustularpsoriasisas pages 2-3, yang2023geneticsofgeneralized pages 3-5) |
| Gene | **MPO** | Associated with GPP | Reported as susceptibility/associated gene; **loss-of-function** variants linked to enhanced neutrophil protease activity and reduced neutrophil turnover; inheritance not established as a single uniform Mendelian model in extracted evidence | 2022-2023 | (yang2023geneticsofgeneralized pages 2-3, akiyama2022pustularpsoriasisas pages 2-3) |
| Gene | **SERPINA3** | Associated with GPP | Susceptibility gene reported in reviews; likely **loss-of-function / reduced protease inhibition** promoting IL-36 activation; inheritance not clearly defined in extracted evidence | 2022-2025 review context | (yang2023geneticsofgeneralized pages 2-3, akiyama2022pustularpsoriasisas pages 2-3) |
| Gene | **SERPINA1** | Associated with GPP | Reported as associated locus in GPP reviews; proposed protease-inhibitor dysfunction increases IL-36 activation; inheritance details not extracted | 2022-2023 | (yang2023geneticsofgeneralized pages 2-3) |
| Gene | **BTN3A3** | Associated with GPP | Loss-of-function association reported in Chinese Han analyses; inheritance details not extracted | 2023 | (yang2023geneticsofgeneralized pages 3-5) |
| Mechanism-linked gene summary | AP1S3 pathway consequence | — | AP1S3 loss disrupts AP-1–dependent trafficking/autophagy, causing **p62 accumulation**, **enhanced NF-κB signaling**, and **upregulated IL-36/IL-1 inflammatory signaling** in keratinocytes | 2014, 2016, 2022-2023 | (settakaffetzi2014ap1s3mutationsare pages 4-6, mahil2016ap1s3mutationscause pages 10-14, mahil2016ap1s3mutationscause pages 6-10, mahil2016ap1s3mutationscause pages 1-6, akiyama2022pustularpsoriasisas pages 3-4, yang2023geneticsofgeneralized pages 3-5) |
| Therapy | **Spesolimab** (anti-IL-36R) | **Trials:** NCT02978690, NCT03782792 (Effisayil 1), NCT04399837 (Effisayil 2) | **Phase 1 proof-of-concept:** 5/7 (71%) achieved GPPGA 0/1 by week 1 and 7/7 by week 4; **Effisayil 1:** GPPGA pustulation score 0 at week 1 in **19/35 (54%)** vs **1/18 (6%)** placebo; GPPGA total 0/1 in **15/35 (43%)** vs **2/18 (11%)**; **Effisayil 2 prevention:** flare rates by week 48 were **10% high-dose** vs **52% placebo**, HR **0.16** for time to first flare | 2022 approval; 2023-2024 analyses | (puig2024currenttreatmentsfor pages 19-21, vilaca2024newandemerging pages 5-6, gwillim2024spesolimabforgeneralized pages 1-2, NCT04399837 chunk 1, alzahrani2026theefficacyand pages 3-4) |
| Therapy safety | **Spesolimab** safety signals | — | Week-1 infections in Effisayil 1: **6/35 (17%)** vs **1/18 (6%)** placebo; reported AEs across studies include infections, infusion reactions, eosinophilia, vomiting, injection-site erythema; serious AEs/infections monitored in post-marketing and extension studies | 2023-2024 | (vilaca2024newandemerging pages 5-6, gwillim2024spesolimabforgeneralized pages 1-2, bernardo2024spesolimabforthe pages 13-14) |
| Therapy/implementation | **Spesolimab** regulatory and real-world use | FDA approval September 2022 for adult GPP flares; later approvals in EU/Japan/other regions reported in reviews | Real-world reports describe successful use but note access/logistics challenges, need for clinician awareness, and ongoing expanded-access/post-marketing studies (e.g., NCT05200247, NCT05239039, NCT05670821) | 2022-2024 | (vilaca2024newandemerging pages 11-12, bernardo2024spesolimabforthe pages 2-3, gwillim2024spesolimabforgeneralized pages 1-2) |
| Therapy | **Imsidolimab** (anti-IL-36R; ANB019) | **Trials:** NCT03619902, NCT05352893 | **Phase 2 open-label (N=8):** 750 mg IV day 1 then 100 mg SC on days 29/57/85; **75%** CGI response at weeks 4 and 16, with 50% “very much improved”; **Phase 3 GEMINI-1:** **53.3%** achieved clear/almost clear skin at week 4 vs **13.3%** placebo (reported in 2024 review citing Br J Dermatol 2023) | 2019-2024 | (NCT03619902 chunk 1, vilaca2024newandemerging pages 8-9, NCT05352893 chunk 1) |
| Therapy safety | **Imsidolimab** safety signals | — | In phase 2, **6/8 (75%)** had at least one TEAE; 2 moderate possibly drug-related TEAEs; 2 SAEs reported in summaries/open-label evidence, though later review notes favorable phase 3 safety with no severe AEs in GEMINI-1 summary | 2022-2024 | (puig2024currenttreatmentsfor pages 19-21, NCT03619902 chunk 1, vilaca2024newandemerging pages 8-9, zhao2022understandingthepathogenesis pages 8-15) |


*Table: This table condenses the main identifiers, gene-level evidence, and IL-36 receptor inhibitor trial results relevant to psoriasis 14, pustular and the broader pustular psoriasis/GPP spectrum. It is useful as a quick-reference scaffold for nomenclature, genetics, mechanism, and therapy evidence.*

---

## Key abstract-supported quotes (for knowledge-base evidence items)
- IL-36 axis therapeutic concept: “Abnormal signaling of the interleukin-36 (IL-36) pathway appears to have a central role in GPP immunopathology, and provides a rational therapeutic target.” (Frontiers in Immunology review; 2024-07; https://doi.org/10.3389/fimmu.2024.1359481) (gwillim2024spesolimabforgeneralized pages 1-2)
- GPP flare prevention trial intent: “The aim of the Effisayil™ 2 study is to see whether long-term treatment with the antibody spesolimab helps prevent skin flares…” (Dermatology and Therapy; 2023-11; https://doi.org/10.1007/s13555-022-00835-6) (vilaca2024newandemerging pages 11-12)
- AP1S3 pathogenic mechanism (study title as mechanistic claim anchor): “AP1S3 Mutations Cause Skin Autoinflammation by Disrupting Keratinocyte Autophagy and Up-Regulating IL-36 Production” (J Invest Dermatol; 2016-11; https://doi.org/10.1016/j.jid.2016.06.618) (mahil2016ap1s3mutationscause pages 1-6)

---

## Limitations of the current report (due to retrieval constraints)
- **OMIM/Orphanet/ICD/MeSH identifiers** for “Psoriasis 14, pustular” were not present in the retrieved full-text excerpts, so they are not provided.
- **MAXO/HPO/GO/CL/UBERON codes** were suggested where appropriate but not validated via ontology lookup tools in this run.
- Some **trial outcomes** for imsidolimab Phase 3 are summarized via secondary review sources; full primary publication text for Br J Dermatol 2023 was not available in the retrieved corpus for direct quotation.


References

1. (akiyama2022pustularpsoriasisas pages 1-2): Masashi Akiyama. Pustular psoriasis as an autoinflammatory keratinization disease (aikd): genetic predisposing factors and promising therapeutic targets. Journal of Dermatological Science, 105:11-17, Jan 2022. URL: https://doi.org/10.1016/j.jdermsci.2021.11.009, doi:10.1016/j.jdermsci.2021.11.009. This article has 38 citations and is from a peer-reviewed journal.

2. (gwillim2024spesolimabforgeneralized pages 1-2): Eran C. Gwillim and Anna J. Nichols. Spesolimab for generalized pustular psoriasis: a review of two key clinical trials supporting initial us regulatory approval. Frontiers in Immunology, Jul 2024. URL: https://doi.org/10.3389/fimmu.2024.1359481, doi:10.3389/fimmu.2024.1359481. This article has 15 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: pustular psoriasis): Open Targets Query (pustular psoriasis, 31 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (settakaffetzi2014ap1s3mutationsare pages 2-4): Niovi Setta-Kaffetzi, Michael A. Simpson, Alexander A. Navarini, Varsha M. Patel, Hui-Chun Lu, Michael H. Allen, Michael Duckworth, Hervé Bachelez, A. David Burden, Siew-Eng Choon, Christopher E.M. Griffiths, Brian Kirby, Antonios Kolios, Marieke M.B. Seyger, Christa Prins, Asma Smahi, Richard C. Trembath, Franca Fraternali, Catherine H. Smith, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations are associated with pustular psoriasis and impaired toll-like receptor 3 trafficking. American journal of human genetics, 94 5:790-7, May 2014. URL: https://doi.org/10.1016/j.ajhg.2014.04.005, doi:10.1016/j.ajhg.2014.04.005. This article has 241 citations and is from a highest quality peer-reviewed journal.

5. (choon2022clinicalcourseand pages 4-6): Siew Eng Choon, Alexander A. Navarini, and Andreas Pinter. Clinical course and characteristics of generalized pustular psoriasis. American Journal of Clinical Dermatology, 23:21-29, Jan 2022. URL: https://doi.org/10.1007/s40257-021-00654-z, doi:10.1007/s40257-021-00654-z. This article has 183 citations and is from a peer-reviewed journal.

6. (bachelez2020pustularpsoriasisthe pages 3-4): H. Bachelez. Pustular psoriasis: the dawn of a new era. Acta Dermato-Venereologica, 100:87-93, Jan 2020. URL: https://doi.org/10.2340/00015555-3388, doi:10.2340/00015555-3388. This article has 165 citations and is from a domain leading peer-reviewed journal.

7. (navarini2017europeanconsensusstatement pages 1-4): A. Navarini, A. Burden, F. Capon, U. Mrowietz, L. Puig, S. Köks, K. Kingo, C. Smith, J. Barker, H. Bachelez, A. Chiricozzi, A. Costanzo, K. Eyerich, L. French, K. Ghoreschi, M. Gilliet, G. Girolomoni, R. Gniadecki, C. Griffiths, H. Koh, D. Lipsker, L. Naldi, E. Prans, J. Prinz, K. Reich, M. Röcken, L. Skov, G. Sorin, M. Ståhle, G. Stingl, P. C. van de Kerkhof, and R. Warren. European consensus statement on phenotypes of pustular psoriasis. Journal of the European Academy of Dermatology and Venereology, 31:1792-1799, Aug 2017. URL: https://doi.org/10.1111/jdv.14386, doi:10.1111/jdv.14386. This article has 612 citations and is from a domain leading peer-reviewed journal.

8. (mossner2018thegeneticbasis pages 15-19): R. Mössner, D. Wilsmann-Theis, V. Oji, P. Gkogkolou, Sabine Löhr, P. Schulz, A. Körber, J. Prinz, Regina Renner, K. Schäkel, L. Vogelsang, K. Peters, S. Philipp, K. Reich, H. Ständer, A. Jacobi, A. Weyergraf, K. Kingo, S. Kõks, S. Gerdes, K. Steinz, T. Schill, K. Griewank, M. Müller, S. Frey, L. Ebertsch, S. Uebe, M. Sticherling, H. Sticht, and U. Hüffmeier. The genetic basis for most patients with pustular skin disease remains elusive. British Journal of Dermatology, 178:740-748, Jan 2018. URL: https://doi.org/10.1111/bjd.15867, doi:10.1111/bjd.15867. This article has 123 citations and is from a highest quality peer-reviewed journal.

9. (settakaffetzi2014ap1s3mutationsare pages 4-6): Niovi Setta-Kaffetzi, Michael A. Simpson, Alexander A. Navarini, Varsha M. Patel, Hui-Chun Lu, Michael H. Allen, Michael Duckworth, Hervé Bachelez, A. David Burden, Siew-Eng Choon, Christopher E.M. Griffiths, Brian Kirby, Antonios Kolios, Marieke M.B. Seyger, Christa Prins, Asma Smahi, Richard C. Trembath, Franca Fraternali, Catherine H. Smith, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations are associated with pustular psoriasis and impaired toll-like receptor 3 trafficking. American journal of human genetics, 94 5:790-7, May 2014. URL: https://doi.org/10.1016/j.ajhg.2014.04.005, doi:10.1016/j.ajhg.2014.04.005. This article has 241 citations and is from a highest quality peer-reviewed journal.

10. (mahil2016ap1s3mutationscause pages 10-14): Satveer K. Mahil, Sophie Twelves, Katalin Farkas, Niovi Setta-Kaffetzi, A. David Burden, Joanna E. Gach, Alan D. Irvine, László Képíró, Maja Mockenhaupt, Hazel H. Oon, Jason Pinner, Annamari Ranki, Marieke M.B. Seyger, Pere Soler-Palacin, Eoin R. Storan, Eugene S. Tan, Laurence Valeyrie-Allanore, Helen S. Young, Richard C. Trembath, Siew-Eng Choon, Marta Szell, Zsuzsanna Bata-Csorgo, Catherine H. Smith, Paola Di Meglio, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations cause skin autoinflammation by disrupting keratinocyte autophagy and up-regulating il-36 production. The Journal of Investigative Dermatology, 136:2251-2259, Nov 2016. URL: https://doi.org/10.1016/j.jid.2016.06.618, doi:10.1016/j.jid.2016.06.618. This article has 184 citations.

11. (yang2023geneticsofgeneralized pages 2-3): Syuan-Fei Yang, Min-Huei Lin, Pei-Chen Chou, Sheng-Kai Hu, Sin-Yi Shih, Hsin-Su Yu, and Sebastian Yu. Genetics of generalized pustular psoriasis: current understanding and implications for future therapeutics. Genes, 14:1297, Jun 2023. URL: https://doi.org/10.3390/genes14061297, doi:10.3390/genes14061297. This article has 31 citations.

12. (yang2023geneticsofgeneralized pages 3-5): Syuan-Fei Yang, Min-Huei Lin, Pei-Chen Chou, Sheng-Kai Hu, Sin-Yi Shih, Hsin-Su Yu, and Sebastian Yu. Genetics of generalized pustular psoriasis: current understanding and implications for future therapeutics. Genes, 14:1297, Jun 2023. URL: https://doi.org/10.3390/genes14061297, doi:10.3390/genes14061297. This article has 31 citations.

13. (akiyama2022pustularpsoriasisas pages 2-3): Masashi Akiyama. Pustular psoriasis as an autoinflammatory keratinization disease (aikd): genetic predisposing factors and promising therapeutic targets. Journal of Dermatological Science, 105:11-17, Jan 2022. URL: https://doi.org/10.1016/j.jdermsci.2021.11.009, doi:10.1016/j.jdermsci.2021.11.009. This article has 38 citations and is from a peer-reviewed journal.

14. (choon2022clinicalcourseand pages 3-4): Siew Eng Choon, Alexander A. Navarini, and Andreas Pinter. Clinical course and characteristics of generalized pustular psoriasis. American Journal of Clinical Dermatology, 23:21-29, Jan 2022. URL: https://doi.org/10.1007/s40257-021-00654-z, doi:10.1007/s40257-021-00654-z. This article has 183 citations and is from a peer-reviewed journal.

15. (choon2022clinicalcourseand pages 2-3): Siew Eng Choon, Alexander A. Navarini, and Andreas Pinter. Clinical course and characteristics of generalized pustular psoriasis. American Journal of Clinical Dermatology, 23:21-29, Jan 2022. URL: https://doi.org/10.1007/s40257-021-00654-z, doi:10.1007/s40257-021-00654-z. This article has 183 citations and is from a peer-reviewed journal.

16. (riveradiaz2023generalizedpustularpsoriasis pages 3-4): Raquel Rivera-Díaz, Esteban Daudén, José Manuel Carrascosa, Pablo de la Cueva, and Luis Puig. Generalized pustular psoriasis: a review on clinical characteristics, diagnosis, and treatment. Dermatology and Therapy, 13:673-688, Jan 2023. URL: https://doi.org/10.1007/s13555-022-00881-0, doi:10.1007/s13555-022-00881-0. This article has 114 citations.

17. (settakaffetzi2014ap1s3mutationsare media 63a65913): Niovi Setta-Kaffetzi, Michael A. Simpson, Alexander A. Navarini, Varsha M. Patel, Hui-Chun Lu, Michael H. Allen, Michael Duckworth, Hervé Bachelez, A. David Burden, Siew-Eng Choon, Christopher E.M. Griffiths, Brian Kirby, Antonios Kolios, Marieke M.B. Seyger, Christa Prins, Asma Smahi, Richard C. Trembath, Franca Fraternali, Catherine H. Smith, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations are associated with pustular psoriasis and impaired toll-like receptor 3 trafficking. American journal of human genetics, 94 5:790-7, May 2014. URL: https://doi.org/10.1016/j.ajhg.2014.04.005, doi:10.1016/j.ajhg.2014.04.005. This article has 241 citations and is from a highest quality peer-reviewed journal.

18. (settakaffetzi2014ap1s3mutationsare media fcbc7708): Niovi Setta-Kaffetzi, Michael A. Simpson, Alexander A. Navarini, Varsha M. Patel, Hui-Chun Lu, Michael H. Allen, Michael Duckworth, Hervé Bachelez, A. David Burden, Siew-Eng Choon, Christopher E.M. Griffiths, Brian Kirby, Antonios Kolios, Marieke M.B. Seyger, Christa Prins, Asma Smahi, Richard C. Trembath, Franca Fraternali, Catherine H. Smith, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations are associated with pustular psoriasis and impaired toll-like receptor 3 trafficking. American journal of human genetics, 94 5:790-7, May 2014. URL: https://doi.org/10.1016/j.ajhg.2014.04.005, doi:10.1016/j.ajhg.2014.04.005. This article has 241 citations and is from a highest quality peer-reviewed journal.

19. (settakaffetzi2014ap1s3mutationsare media 0828eba0): Niovi Setta-Kaffetzi, Michael A. Simpson, Alexander A. Navarini, Varsha M. Patel, Hui-Chun Lu, Michael H. Allen, Michael Duckworth, Hervé Bachelez, A. David Burden, Siew-Eng Choon, Christopher E.M. Griffiths, Brian Kirby, Antonios Kolios, Marieke M.B. Seyger, Christa Prins, Asma Smahi, Richard C. Trembath, Franca Fraternali, Catherine H. Smith, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations are associated with pustular psoriasis and impaired toll-like receptor 3 trafficking. American journal of human genetics, 94 5:790-7, May 2014. URL: https://doi.org/10.1016/j.ajhg.2014.04.005, doi:10.1016/j.ajhg.2014.04.005. This article has 241 citations and is from a highest quality peer-reviewed journal.

20. (twelves2019clinicalandgenetic pages 1-2): Sophie Twelves, Alshimaa Mostafa, Nick Dand, Elias Burri, Katalin Farkas, Rosemary Wilson, Hywel L. Cooper, Alan D. Irvine, Hazel H. Oon, Külli Kingo, Sulev Köks, Ulrich Mrowietz, Luis Puig, Nick Reynolds, Eugene Sern-Ting Tan, Adrian Tanew, Kaspar Torz, Hannes Trattner, Mark Valentine, Shyamal Wahie, Richard B. Warren, Andrew Wright, Zsuzsa Bata-Csörgő, Marta Szell, Christopher E.M. Griffiths, A. David Burden, Siew-Eng Choon, Catherine H. Smith, Jonathan N. Barker, Alexander A. Navarini, and Francesca Capon. Clinical and genetic differences between pustular psoriasis subtypes. The Journal of Allergy and Clinical Immunology, 143:1021-1026, Mar 2019. URL: https://doi.org/10.1016/j.jaci.2018.06.038, doi:10.1016/j.jaci.2018.06.038. This article has 314 citations.

21. (mahil2016ap1s3mutationscause pages 6-10): Satveer K. Mahil, Sophie Twelves, Katalin Farkas, Niovi Setta-Kaffetzi, A. David Burden, Joanna E. Gach, Alan D. Irvine, László Képíró, Maja Mockenhaupt, Hazel H. Oon, Jason Pinner, Annamari Ranki, Marieke M.B. Seyger, Pere Soler-Palacin, Eoin R. Storan, Eugene S. Tan, Laurence Valeyrie-Allanore, Helen S. Young, Richard C. Trembath, Siew-Eng Choon, Marta Szell, Zsuzsanna Bata-Csorgo, Catherine H. Smith, Paola Di Meglio, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations cause skin autoinflammation by disrupting keratinocyte autophagy and up-regulating il-36 production. The Journal of Investigative Dermatology, 136:2251-2259, Nov 2016. URL: https://doi.org/10.1016/j.jid.2016.06.618, doi:10.1016/j.jid.2016.06.618. This article has 184 citations.

22. (mahil2016ap1s3mutationscause pages 1-6): Satveer K. Mahil, Sophie Twelves, Katalin Farkas, Niovi Setta-Kaffetzi, A. David Burden, Joanna E. Gach, Alan D. Irvine, László Képíró, Maja Mockenhaupt, Hazel H. Oon, Jason Pinner, Annamari Ranki, Marieke M.B. Seyger, Pere Soler-Palacin, Eoin R. Storan, Eugene S. Tan, Laurence Valeyrie-Allanore, Helen S. Young, Richard C. Trembath, Siew-Eng Choon, Marta Szell, Zsuzsanna Bata-Csorgo, Catherine H. Smith, Paola Di Meglio, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations cause skin autoinflammation by disrupting keratinocyte autophagy and up-regulating il-36 production. The Journal of Investigative Dermatology, 136:2251-2259, Nov 2016. URL: https://doi.org/10.1016/j.jid.2016.06.618, doi:10.1016/j.jid.2016.06.618. This article has 184 citations.

23. (fujita2022diagnosisofgeneralized pages 1-2): Hideki Fujita, Melinda Gooderham, and Ricardo Romiti. Diagnosis of generalized pustular psoriasis. American Journal of Clinical Dermatology, 23:31-38, Jan 2022. URL: https://doi.org/10.1007/s40257-021-00652-1, doi:10.1007/s40257-021-00652-1. This article has 89 citations and is from a peer-reviewed journal.

24. (puig2023generalizedpustularpsoriasis pages 6-6): Lluís Puig, Siew Eng Choon, Alice B. Gottlieb, Slaheddine Marrakchi, Jörg C. Prinz, Ricardo Romiti, Yayoi Tada, Dorothea von Bredow, and Melinda Gooderham. Generalized pustular psoriasis: a global delphi consensus on clinical course, diagnosis, treatment goals and disease management. Journal of the European Academy of Dermatology and Venereology, 37:737-752, Feb 2023. URL: https://doi.org/10.1111/jdv.18851, doi:10.1111/jdv.18851. This article has 89 citations and is from a domain leading peer-reviewed journal.

25. (ly2019diagnosisandscreening pages 2-3): Karen Ly, Kristen M Beck, Mary P Smith, Quinn Thibodeaux, and Tina Bhutani. Diagnosis and screening of patients with generalized pustular psoriasis. Psoriasis: Targets and Therapy, 9:37-42, Jun 2019. URL: https://doi.org/10.2147/ptt.s181808, doi:10.2147/ptt.s181808. This article has 111 citations.

26. (burden2022clinicaldiseasemeasures pages 1-3): A. David Burden, Siew Eng Choon, Alice B. Gottlieb, Alexander A. Navarini, and Richard B. Warren. Clinical disease measures in generalized pustular psoriasis. American Journal of Clinical Dermatology, 23:39-50, Jan 2022. URL: https://doi.org/10.1007/s40257-021-00653-0, doi:10.1007/s40257-021-00653-0. This article has 64 citations and is from a peer-reviewed journal.

27. (puig2024currenttreatmentsfor pages 19-21): Lluís Puig, Hideki Fujita, Diamant Thaçi, Min Zheng, Ana Cristina Hernandez Daly, Craig Leonardi, Mark G. Lebwohl, and Jonathan Barker. Current treatments for generalized pustular psoriasis: a narrative summary of a systematic literature search. Dermatology and Therapy, 14:2331-2378, Aug 2024. URL: https://doi.org/10.1007/s13555-024-01230-z, doi:10.1007/s13555-024-01230-z. This article has 14 citations.

28. (NCT03619902 chunk 1):  A Study to Evaluate the Efficacy and Safety of Imsidolimab (ANB019) in Adults With Generalized Pustular Psoriasis. Vanda Pharmaceuticals. 2019. ClinicalTrials.gov Identifier: NCT03619902

29. (NCT05352893 chunk 1):  Study to Evaluate the Efficacy and Safety of Imsidolimab (ANB019) in the Treatment of Subjects With GPP. Vanda Pharmaceuticals. 2022. ClinicalTrials.gov Identifier: NCT05352893

30. (bernardo2024spesolimabforthe pages 2-3): Diana Bernardo, Diamant Thaçi, and Tiago Torres. Spesolimab for the treatment of generalized pustular psoriasis. Drugs, 84:45-58, Dec 2023. URL: https://doi.org/10.1007/s40265-023-01988-0, doi:10.1007/s40265-023-01988-0. This article has 44 citations and is from a domain leading peer-reviewed journal.

31. (yang2023geneticsofgeneralized pages 1-2): Syuan-Fei Yang, Min-Huei Lin, Pei-Chen Chou, Sheng-Kai Hu, Sin-Yi Shih, Hsin-Su Yu, and Sebastian Yu. Genetics of generalized pustular psoriasis: current understanding and implications for future therapeutics. Genes, 14:1297, Jun 2023. URL: https://doi.org/10.3390/genes14061297, doi:10.3390/genes14061297. This article has 31 citations.

32. (settakaffetzi2014ap1s3mutationsare pages 1-2): Niovi Setta-Kaffetzi, Michael A. Simpson, Alexander A. Navarini, Varsha M. Patel, Hui-Chun Lu, Michael H. Allen, Michael Duckworth, Hervé Bachelez, A. David Burden, Siew-Eng Choon, Christopher E.M. Griffiths, Brian Kirby, Antonios Kolios, Marieke M.B. Seyger, Christa Prins, Asma Smahi, Richard C. Trembath, Franca Fraternali, Catherine H. Smith, Jonathan N. Barker, and Francesca Capon. Ap1s3 mutations are associated with pustular psoriasis and impaired toll-like receptor 3 trafficking. American journal of human genetics, 94 5:790-7, May 2014. URL: https://doi.org/10.1016/j.ajhg.2014.04.005, doi:10.1016/j.ajhg.2014.04.005. This article has 241 citations and is from a highest quality peer-reviewed journal.

33. (akiyama2022pustularpsoriasisas pages 3-4): Masashi Akiyama. Pustular psoriasis as an autoinflammatory keratinization disease (aikd): genetic predisposing factors and promising therapeutic targets. Journal of Dermatological Science, 105:11-17, Jan 2022. URL: https://doi.org/10.1016/j.jdermsci.2021.11.009, doi:10.1016/j.jdermsci.2021.11.009. This article has 38 citations and is from a peer-reviewed journal.

34. (vilaca2024newandemerging pages 5-6): João Vilaça, Orhan Yilmaz, and Tiago Torres. New and emerging treatments for generalized pustular psoriasis: focus on il-36 receptor inhibitors. Pharmaceutics, 16:908, Jul 2024. URL: https://doi.org/10.3390/pharmaceutics16070908, doi:10.3390/pharmaceutics16070908. This article has 12 citations.

35. (NCT04399837 chunk 1):  A Study to Test Whether BI 655130 (Spesolimab) Prevents Flare-ups in Patients With Generalized Pustular Psoriasis. Boehringer Ingelheim. 2020. ClinicalTrials.gov Identifier: NCT04399837

36. (alzahrani2026theefficacyand pages 3-4): Dhaii Alzahrani, Afnan Hasanain, Renad Alharthy, Yara Aljefri, Yara Alghamdi, Renad Alshaikh, Almaha Alhijab, Faris Neazy, Abdulmajeed Alosaimi, Badr Felemban, Reshale Johar, and Roaa E. Morya. The efficacy and safety of spesolimab in patients with generalized pustular psoriasis flares: a systematic review and meta-analysis. Frontiers in Medicine, Jan 2026. URL: https://doi.org/10.3389/fmed.2025.1749320, doi:10.3389/fmed.2025.1749320. This article has 0 citations.

37. (bernardo2024spesolimabforthe pages 13-14): Diana Bernardo, Diamant Thaçi, and Tiago Torres. Spesolimab for the treatment of generalized pustular psoriasis. Drugs, 84:45-58, Dec 2023. URL: https://doi.org/10.1007/s40265-023-01988-0, doi:10.1007/s40265-023-01988-0. This article has 44 citations and is from a domain leading peer-reviewed journal.

38. (vilaca2024newandemerging pages 11-12): João Vilaça, Orhan Yilmaz, and Tiago Torres. New and emerging treatments for generalized pustular psoriasis: focus on il-36 receptor inhibitors. Pharmaceutics, 16:908, Jul 2024. URL: https://doi.org/10.3390/pharmaceutics16070908, doi:10.3390/pharmaceutics16070908. This article has 12 citations.

39. (vilaca2024newandemerging pages 8-9): João Vilaça, Orhan Yilmaz, and Tiago Torres. New and emerging treatments for generalized pustular psoriasis: focus on il-36 receptor inhibitors. Pharmaceutics, 16:908, Jul 2024. URL: https://doi.org/10.3390/pharmaceutics16070908, doi:10.3390/pharmaceutics16070908. This article has 12 citations.

40. (zhao2022understandingthepathogenesis pages 8-15): An-Qi Zhao and Ming Li. Understanding the pathogenesis of generalized pustular psoriasis based on molecular genetics and immunopathology. International Journal of Dermatology and Venereology, 5:199-206, Dec 2022. URL: https://doi.org/10.1097/jd9.0000000000000277, doi:10.1097/jd9.0000000000000277. This article has 3 citations.