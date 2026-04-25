---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-20T13:47:08.842467'
end_time: '2026-04-20T14:16:11.418917'
duration_seconds: 1742.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CD27-related lymphoproliferative and immune disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CD27-related lymphoproliferative and immune disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CD27-related lymphoproliferative and immune disorder** covering all of the
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
- **Disease Name:** CD27-related lymphoproliferative and immune disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CD27-related lymphoproliferative and immune disorder** covering all of the
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


# Comprehensive Research Report: CD27-related lymphoproliferative and immune disorder (CD27 deficiency)

## 1. Disease Information

### 1.1 Concise overview
CD27-related lymphoproliferative and immune disorder is a monogenic inborn error of immunity caused by biallelic loss-of-function variants in **CD27 (TNFRSF7)**, characterized by **selective susceptibility to Epstein–Barr virus (EBV)** with chronic/persistent EBV viremia and EBV-driven complications including **lymphoproliferation, hemophagocytic lymphohistiocytosis (HLH), and EBV-associated lymphomas**, often accompanied by **hypogammaglobulinemia and defective T cell–dependent humoral immunity**. (ghosh2020extendedclinicaland pages 2-3, tangye2020primaryimmunodeficienciesreveal pages 7-8, salzer2013combinedimmunodeficiencywith pages 1-2)

### 1.2 Key identifiers (from available evidence)
- **Disease entity name (OMIM):** *Lymphoproliferative syndrome 2* (also written **LPS2**). (golchehre2023newpresentationof pages 1-2, alkhairy2015novelmutationsin pages 1-2)
- **OMIM ID:** **615122** (reported in multiple sources within retrieved evidence). (golchehre2023newpresentationof pages 1-2, alkhairy2015novelmutationsin pages 1-2)
- **Causal gene:** **CD27 / TNFRSF7**, locus 12p13.31. (kishore2020novelmutationin pages 2-3, golchehre2023newpresentationof pages 1-2, alkhairy2015novelmutationsin pages 1-2)
- **IUIS context:** discussed as an immune dysregulation/EBV-susceptibility IEI category in a 2023 case report. (golchehre2023newpresentationof pages 1-2)

**Not found in retrieved evidence:** MONDO ID, Orphanet ID, ICD-10/ICD-11 codes, MeSH descriptor (would require direct OMIM/Orphanet/MONDO retrieval beyond the obtained full texts).

### 1.3 Synonyms and alternative names
- **CD27 deficiency** (common in clinical genetics/immunology literature). (alkhairy2015novelmutationsin pages 4-5)
- **Lymphoproliferative syndrome 2 (LPS2)**. (golchehre2023newpresentationof pages 1-2, alkhairy2015novelmutationsin pages 1-2)
- Descriptive presentations used in titles: **“combined immunodeficiency with life-threatening EBV-associated lymphoproliferative disorder”**. (salzer2013combinedimmunodeficiencywith pages 1-2)

### 1.4 Evidence type
Knowledge is derived primarily from **aggregated disease-level cohort studies and case series** (e.g., multicenter cohorts) plus **individual case reports** adding phenotypic expansions. (ghosh2020extendedclinicaland pages 2-3, alkhairy2015novelmutationsin pages 4-5, golchehre2023newpresentationof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic cause:** biallelic pathogenic variants in **CD27 (TNFRSF7)** causing absent or markedly reduced CD27 surface expression and functional loss of CD27–CD70 costimulation. (montfrans2012cd27deficiencyis pages 2-4, alkhairy2015novelmutationsin pages 7-9, ghosh2020extendedclinicaland pages 2-3)

**Inheritance pattern:** **autosomal recessive**; many patients reported from consanguineous families, with heterozygous relatives typically unaffected in early reports. (montfrans2012cd27deficiencyis pages 2-4, alkhairy2015novelmutationsin pages 1-2)

### 2.2 Risk factors
- **Genetic:** biallelic CD27 variants (see Variant Table below). (alkhairy2015novelmutationsin pages 4-5, alkhairy2015novelmutationsin pages 1-2)
- **Infectious trigger:** **EBV infection** is a major precipitant of clinical disease (viremia, LPD, HLH, lymphoma). (ghosh2020extendedclinicaland pages 2-3, salzer2013combinedimmunodeficiencywith pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No protective variants or environmental protective factors were identified in the retrieved evidence. The dominant gene–environment interaction described is that **EBV exposure** triggers severe disease manifestations in genetically susceptible hosts (CD27 deficiency). (ghosh2020extendedclinicaland pages 2-3, salzer2013combinedimmunodeficiencywith pages 1-2)

---

## 3. Phenotypes

A multicenter cohort (CD27 n=33 within a 49-patient CD27/CD70 cohort) reported: **EBV-positive at diagnosis ~90%**, **lymphoproliferation 70%**, **lymphoma 43%**, **autoinflammatory features 43%**, and **HLH in 9 CD27-deficient patients**. (ghosh2020extendedclinicaland pages 2-3)

A separate 17-patient CD27 cohort reported **mortality 29%**, and that **very high EBV plasma loads** were often seen (up to ~5×10^6–8×10^6 copies/mL in a table excerpt). (alkhairy2015novelmutationsin pages 5-6, alkhairy2015novelmutationsin pages 7-9)

| Feature | Description | HPO term(s) | Frequency/statistics (with cohort/source) | Notes |
|---|---|---|---|---|
| EBV susceptibility / EBV positivity | Marked susceptibility to Epstein-Barr virus with chronic/persistent viremia and EBV-driven immune dysregulation | HP:0012378 Elevated circulating Epstein-Barr virus load; HP:0002731 Recurrent viral infections | EBV-positive at diagnosis in 90% of the CD27/CD70 cohort; in Alkhairy 2015, high EBV loads were documented in 11/12 tested and plasma loads reached up to ~5×10^6–8×10^6 copies/mL (ghosh2020extendedclinicaland pages 2-3, alkhairy2015novelmutationsin pages 5-6) | Core disease-defining feature; often precedes lymphoproliferation and lymphoma |
| Lymphoproliferation | Persistent or recurrent EBV-driven lymphadenopathy/hepatosplenomegaly and benign or malignant lymphoid expansion | HP:0002716 Lymphadenopathy; HP:0001433 Hepatosplenomegaly; HP:0002841 Lymphoproliferative disorder | Lymphoproliferation reported in 70% of the multicenter cohort (49 total; 33 CD27-deficient) (ghosh2020extendedclinicaland pages 2-3) | Can mimic CVID, ALPS, chronic active EBV, or lymphoma |
| Lymphoma | Increased risk of EBV-associated lymphoma, including Hodgkin and non-Hodgkin lymphoma | HP:0002665 Lymphoma; HP:0012197 Hodgkin lymphoma; HP:0100827 Non-Hodgkin lymphoma | Lymphoma in 43% of the Ghosh 2020 cohort; cases in Alkhairy 2015 included DLBCL, extranodal EBV-related LPD, and classical Hodgkin lymphoma (ghosh2020extendedclinicaland pages 2-3, alkhairy2015novelmutationsin pages 5-6) | Malignant transformation is a major indication for HSCT |
| Hemophagocytic lymphohistiocytosis (HLH) | Hyperinflammatory episodes triggered by EBV with hemophagocytosis/HLH phenotype | HP:0003125 Hemophagocytosis; HP:0032243 Hemophagocytic lymphohistiocytosis | 9 CD27-deficient patients developed HLH in the Ghosh cohort; HLH also described in earlier cases and pooled reviews (ghosh2020extendedclinicaland pages 2-3, kishore2020novelmutationin pages 4-5) | Severe, potentially life-threatening presentation |
| Hypogammaglobulinemia / antibody deficiency | Low immunoglobulins and impaired humoral immunity, sometimes CVID-like | HP:0004313 Decreased circulating IgG level; HP:0010701 Hypogammaglobulinemia; HP:0002845 Functional abnormality of humoral immunity | Primary hypogammaglobulinemia in 3/17 in Alkhairy 2015; secondary/treatment-related hypogammaglobulinemia also common (rituximab/chemotherapy) (alkhairy2015novelmutationsin pages 4-5) | May be present at onset or emerge after EBV disease/treatment |
| Impaired vaccine / protein antigen responses | Defective T-cell–dependent antibody responses despite some preserved vaccine responses to other antigens | HP:0034335 Abnormality of immune response to vaccination | Montfrans 2012: severely impaired antibody responses to repeated protein antigens (rabies, tetanus), despite preserved responses to polysaccharide/conjugate vaccines (montfrans2012cd27deficiencyis pages 6-7) | Supports combined immunodeficiency rather than isolated antibody deficiency |
| Memory B-cell defect | Abnormal or reduced memory B-cell generation; absent/reduced CD27 expression on B cells | HP:0011839 Abnormal B-cell subset distribution; HP:0011813 Reduced memory B cell count | Ghosh 2020 reported aberrant generation of memory B and T cells; Alkhairy 2015 and related cases documented absent/reduced CD27 expression and reduced memory-cell compartments (ghosh2020extendedclinicaland pages 2-3, alkhairy2015novelmutationsin pages 7-9) | CD27 itself is a canonical memory B-cell marker, so interpretation requires genotype context |
| T-cell dysfunction / paucity of EBV-specific T cells | Impaired expansion and effector differentiation of EBV-specific CD8 T cells; reduced cytotoxic antiviral immunity | HP:0003202 Abnormal T-cell proliferation; HP:0011832 Abnormality of CD8-positive T cells | Ghosh 2020: paucity of EBV-specific T cells and impaired CD8 effector function; Montfrans 2012: reduced IL-2 production by EBV-specific CD8 T cells (ghosh2020extendedclinicaland pages 2-3, montfrans2012cd27deficiencyis pages 6-7) | Mechanistically central to failure of EBV control |
| NK / iNKT abnormalities | In some severe patients, reduced NK-cell function and/or low iNKT cells | HP:0011837 Abnormal natural killer cell count; HP:0011838 Abnormal natural killer cell function | Salzer 2013: in severely affected patients, iNKT-cell numbers and NK-cell function were reduced; Alkhairy 2015 reported reduced NK/NKT function in 5/7 measured (alkhairy2015novelmutationsin pages 7-9) | Not universal; may correlate with more severe phenotypes |
| Recurrent respiratory infections | Recurrent sinopulmonary infections, often preceding EBV-LPD recognition | HP:0002205 Recurrent respiratory infections | Frequent across reports; highlighted in case reports and pooled reviews (kishore2020novelmutationin pages 2-3, kishore2020novelmutationin pages 4-5) | Often leads initially to a CVID diagnosis |
| Bronchiectasis | Chronic airway damage from recurrent respiratory infections | HP:0002110 Bronchiectasis | Reported in the Kishore 2020 case with long-standing recurrent infections and hypogammaglobulinemia (kishore2020novelmutationin pages 2-3) | Represents chronic morbidity from delayed diagnosis |
| Hepatosplenomegaly | Enlarged liver and spleen, often with EBV-LPD | HP:0001433 Hepatosplenomegaly | Seen in Montfrans 2012 and Kishore 2020 case descriptions (montfrans2012cd27deficiencyis pages 2-4, kishore2020novelmutationin pages 2-3) | Common accompaniment of lymphoproliferation/HLH |
| Uveitis / inflammatory complications | Immune dysregulation can include ocular and systemic inflammatory disease | HP:0000554 Uveitis; HP:0002721 Immune dysregulation | EBV-associated uveitis reported in Montfrans 2012; autoinflammatory features occurred in 43% of the Ghosh cohort (montfrans2012cd27deficiencyis pages 2-4, ghosh2020extendedclinicaland pages 2-3) | Broadens phenotype beyond infection and malignancy |
| Autoinflammation | Periodic fever, arthritis, uveitis, and other inflammatory manifestations | HP:0012649 Autoinflammation; HP:0001945 Fever; HP:0001369 Arthritis | Autoinflammatory features in 21/49 overall (43%) in Ghosh 2020 (ghosh2020extendedclinicaland pages 2-3) | Important because disease may present as immune dysregulation rather than infection alone |
| Coronary ectasia / aneurysm | Unusual cardiovascular inflammatory phenotype reported in a recent child with CD27 deficiency | HP:0031364 Coronary artery aneurysm; HP:0031363 Coronary artery ectasia | Single 2023 case report of a 20-month-old boy with coronary ectasia/aneurysm plus EBV-associated lymphoma and COVID-19 (golchehre2023newpresentationof pages 1-2, golchehre2023newpresentationof pages 2-4) | Recent phenotype expansion; causality uncertain (EBV, lymphoma, inflammation, or CD27 deficiency itself) |
| Mortality | Substantial disease-related mortality without curative treatment in severe cases | HP:0003826 Reduced life expectancy | Mortality 29% in Alkhairy 2015 (approximately 5/17); two of eight died in Salzer 2013; pooled review summarized mortality as 30% (6/18) (alkhairy2015novelmutationsin pages 4-5, kishore2020novelmutationin pages 4-5) | Deaths attributed to malignancy, sepsis, aplastic anemia, hepatic failure, and severe EBV disease |
| Response to rituximab | Anti-CD20 B-cell depletion can reduce EBV load and improve EBV-LPD/HLH, sometimes transiently | HP:0031370 Abnormal response to treatment | Rituximab used in 6/17 in Alkhairy 2015; favorable but sometimes transient responses reported; Salzer 2013 reported repeated anti-CD20 therapy in one patient (alkhairy2015novelmutationsin pages 4-5, alkhairy2015novelmutationsin pages 1-2) | Useful for EBV-driven B-cell disease but not curative |
| HSCT outcome | Allogeneic HSCT is the only curative immune reconstitution approach for severe disease | HP:0012337 Abnormality of immune system physiology | Ghosh 2020: 19 patients underwent allogeneic HSCT with 95% overall survival; Alkhairy 2015: 3/17 received cord blood HSCT and were alive; Salzer 2013: 2 underwent HSCT successfully (ghosh2020extendedclinicaland pages 2-3, alkhairy2015novelmutationsin pages 4-5, alkhairy2015novelmutationsin pages 7-9) | Strong real-world evidence supporting HSCT in severe EBV-LPD/lymphoma or refractory disease |


*Table: This table summarizes the major clinical features of CD27-related lymphoproliferative and immune disorder, with suggested HPO terms and quantitative observations from key cohorts and case reports. It is useful for knowledge-base curation because it links phenotype labels to disease frequency, mechanism-relevant findings, and treatment context.*

### Additional phenotype expansions (2023–2024 prioritized)
A 2023 case report described a **20-month-old** with CD27 deficiency and **EBV-associated lymphoma** plus **coronary artery ectasia/aneurysm** (Kawasaki-like phenotype) and **SARS-CoV-2 infection**, which the authors presented as an expansion beyond the canonical EBV phenotype spectrum. (golchehre2023newpresentationof pages 1-2, golchehre2023newpresentationof pages 2-4)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **Gene:** CD27 (TNFRSF7), TNF receptor superfamily costimulatory receptor. (tangye2020primaryimmunodeficienciesreveal pages 7-8, golchehre2023newpresentationof pages 1-2)

### 4.2 Pathogenic variants (examples)
Multiple pathogenic variants (nonsense and missense) have been reported across cohorts, including **c.24G>A (p.W8X)**, **p.C53Y**, **p.C10X**, **p.R78W**, **p.C96Y**, **p.R107C**, **p.W110X**, and additional novel alleles across multicenter studies. (montfrans2012cd27deficiencyis pages 2-4, alkhairy2015novelmutationsin pages 4-5, alkhairy2015novelmutationsin pages 7-9)

| Variant (cDNA/protein as reported) | Variant type | Inheritance / zygosity | Key phenotype highlights | Key treatment / outcome notes | Primary source(s) with year / journal / URL |
|---|---|---|---|---|---|
| c.24G>A, p.W8X | Nonsense / truncating | Homozygous AR in affected siblings; heterozygous carrier parents/unaffected sib | Persistent symptomatic EBV viremia; severe EBV-driven lymphadenopathy; fever; hepatosplenomegaly; EBV-associated uveitis; hypogammaglobulinemia with impaired T-cell–dependent antibody responses; one sibling died of aplastic anemia with sepsis. EBV detected in purified B cells; viral loads reported as ~3000 and 2050 copies/µg DNA in one report. Broader pooled reports associate this variant with very high EBV loads and EBV-LPD/lymphoma. (montfrans2012cd27deficiencyis pages 2-4, montfrans2012cd27deficiencyis pages 6-7, alkhairy2015novelmutationsin pages 1-2) | Immunoglobulin replacement used in surviving patient with stabilization; no HSCT/rituximab described in Montfrans excerpt. Included among variants in later pooled series/case summaries. (montfrans2012cd27deficiencyis pages 2-4, alkhairy2015novelmutationsin pages 4-5, kishore2020novelmutationin pages 4-5) | van Montfrans 2012, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2011.11.013; Alkhairy 2015, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2015.02.022 (montfrans2012cd27deficiencyis pages 2-4, alkhairy2015novelmutationsin pages 1-2) |
| c.G158A, p.C53Y | Missense | Homozygous AR in 3 independent families (8 patients total in Salzer cohort) | Phenotypic range from asymptomatic memory B-cell deficiency to EBV-associated hemophagocytosis/HLH, lymphoproliferative disorder, and malignant lymphoma; after EBV infection, hypogammaglobulinemia developed in at least 3 affected individuals; reduced iNKT cells and impaired NK function in severe cases. (salzer2013combinedimmunodeficiencywith pages 1-2, alkhairy2015novelmutationsin pages 1-2) | Two of 8 patients died; two underwent allogeneic HSCT successfully; one received repeated anti-CD20 (rituximab) therapy. (salzer2013combinedimmunodeficiencywith pages 1-2) | Salzer 2013, *Haematologica*, https://doi.org/10.3324/haematol.2012.068791; Alkhairy 2015, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2015.02.022 (salzer2013combinedimmunodeficiencywith pages 1-2, alkhairy2015novelmutationsin pages 1-2) |
| c.C30A, p.C10X | Nonsense / truncating | Reported in pooled CD27-deficient cohort; zygosity not specified in excerpt | Listed among pathogenic CD27 variants in patients with EBV viremia / EBV-related LPD / HLH / lymphoma and hypogammaglobulinemia spectrum. (kishore2020novelmutationin pages 4-5, alkhairy2015novelmutationsin pages 4-5) | Included in cohorts where rituximab often produced favorable but sometimes transient responses and HSCT was curative in selected severe cases; variant-specific outcome not isolated in excerpt. (alkhairy2015novelmutationsin pages 4-5, kishore2020novelmutationin pages 4-5) | Alkhairy 2015, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2015.02.022; Kishore 2020, *BMJ Case Rep*, https://doi.org/10.1136/bcr-2019-233482 (alkhairy2015novelmutationsin pages 4-5, kishore2020novelmutationin pages 4-5) |
| c.C232T, p.R78W | Missense | Reported in pooled cohort; zygosity not specified in excerpt | In silico prediction damaging; associated within pooled CD27-deficiency series with EBV viremia/LPD, lymphoma, HLH, and antibody deficiency spectrum. (alkhairy2015novelmutationsin pages 5-6, kishore2020novelmutationin pages 4-5) | Variant-specific treatment not isolated; pooled cohort treatments included IVIG, rituximab, chemotherapy, and HSCT. (alkhairy2015novelmutationsin pages 5-6, kishore2020novelmutationin pages 4-5) | Alkhairy 2015, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2015.02.022; Kishore 2020, *BMJ Case Rep*, https://doi.org/10.1136/bcr-2019-233482 (alkhairy2015novelmutationsin pages 5-6, kishore2020novelmutationin pages 4-5) |
| c.G287A, p.C96Y | Missense | Reported in pooled cohort; zygosity not specified in excerpt | In silico prediction damaging; reported among pathogenic variants in CD27 deficiency with EBV-related disease, including chronic/persistent EBV viremia, LPD, lymphoma, and hypogammaglobulinemia. (alkhairy2015novelmutationsin pages 5-6, kishore2020novelmutationin pages 4-5) | Variant-specific treatment not isolated; pooled treatment experience includes IVIG, rituximab, conventional chemotherapy, and HSCT. (alkhairy2015novelmutationsin pages 4-5, kishore2020novelmutationin pages 4-5) | Alkhairy 2015, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2015.02.022; Kishore 2020, *BMJ Case Rep*, https://doi.org/10.1136/bcr-2019-233482 (alkhairy2015novelmutationsin pages 5-6, kishore2020novelmutationin pages 4-5) |
| c.C319T, p.R107C | Missense | Reported in pooled cohort; one report notes structural misfolding prediction; zygosity not specified in excerpt | Associated with EBV viremia / EBV-related extranodal LPD / Hodgkin or diffuse large B-cell lymphoma / HLH spectrum in pooled cases; impaired CD27 expression and high EBV loads reported across affected cohort. (alkhairy2015novelmutationsin pages 5-6, kishore2020novelmutationin pages 4-5) | Variant-specific response not isolated; pooled cohort notes rituximab can be favorable but transient, chemotherapy responses variable, and HSCT successful in selected cases. (alkhairy2015novelmutationsin pages 4-5, alkhairy2015novelmutationsin pages 7-9) | Alkhairy 2015, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2015.02.022; Kishore 2020, *BMJ Case Rep*, https://doi.org/10.1136/bcr-2019-233482 (alkhairy2015novelmutationsin pages 5-6, kishore2020novelmutationin pages 4-5) |
| c.G329A, p.W110X | Nonsense / truncating | Reported in pooled case summary; zygosity not specified in excerpt | Listed among CD27 pathogenic variants in patients with recurrent infections, hypogammaglobulinemia/CVID-like disease, persistent lymphadenopathy/hepatosplenomegaly, high EBV titers, EBV-driven LPD, HLH, and lymphoma. (kishore2020novelmutationin pages 4-5, izawa2017inheritedcd70deficiency pages 10-11) | Variant-specific treatment not isolated; broader cohort experience supports rituximab for EBV-driven B-cell disease and HSCT as definitive therapy in severe disease. (kishore2020novelmutationin pages 4-5, tangye2020primaryimmunodeficienciesreveal pages 7-8) | Kishore 2020, *BMJ Case Rep*, https://doi.org/10.1136/bcr-2019-233482; Izawa 2017 mechanistic comparison, *J Exp Med*, https://doi.org/10.1084/jem.20160784 (kishore2020novelmutationin pages 4-5, izawa2017inheritedcd70deficiency pages 10-11) |
| Homozygous CD27 variant (not specified in excerpt) | Not specified in excerpt | Homozygous AR | 20-month-old boy with CD27 deficiency; EBV-associated lymphoma (EBER-positive), dysgammaglobulinemia / impaired antibody responses in disease background, coronary artery ectasia / aneurysm, and later SARS-CoV-2 infection; authors note >35 CD27-deficient patients reported. (golchehre2023newpresentationof pages 1-2, golchehre2023newpresentationof pages 2-4) | Treated with IVIG and aspirin for Kawasaki-like/coronary presentation; lymphoma treated with ABVD and COPP; coronary aneurysm size decreased with aspirin/Plavix; short-term survival reported. (golchehre2023newpresentationof pages 2-4) | Golchehre 2023, *Iran J Allergy Asthma Immunol*, https://doi.org/10.18502/ijaai.v22i1.12013 (golchehre2023newpresentationof pages 1-2, golchehre2023newpresentationof pages 2-4) |
| Multiple biallelic CD27 variants (16 distinct mutations across cohort) | Mixed: nonsense, missense, other LOF | Predominantly homozygous / biallelic AR; some compound heterozygous | In the largest multicenter cohort of CD27/CD70 defects, 90% were EBV-positive at diagnosis; lymphoproliferation 70%; lymphoma 43%; 9 CD27-deficient patients developed HLH; autoinflammatory features in 43%; aberrant memory B/T-cell generation and paucity of EBV-specific T cells. (ghosh2020extendedclinicaland pages 2-3) | 19 patients underwent allogeneic HSCT with 95% overall survival and no disease recurrence reported; timely HSCT advocated, especially for malignant transformation. (ghosh2020extendedclinicaland pages 2-3, ghosh2020extendedclinicaland pages 3-4) | Ghosh 2020, *Blood* (cohort summarized in retrieved evidence), DOI noted in excerpt as 10.1182/blood.2020006738 (ghosh2020extendedclinicaland pages 2-3, ghosh2020extendedclinicaland pages 3-4) |
| Mixed CD27 cohort variants including c.24G>A/p.W8X, c.G158A/p.C53Y, c.C30A/p.C10X, c.C232T/p.R78W, c.G287A/p.C96Y, c.C319T/p.R107C | Mixed | Mixed biallelic AR; many from consanguineous families | 17-patient cohort: EBV disease prominent; high EBV plasma loads in 11/12 tested, up to ~5×10^6–8×10^6 copies/mL; DLBCL, extranodal EBV-related LPD, classical Hodgkin lymphoma, HLH, and hypogammaglobulinemia/secondary HGG all reported; mortality 29%. (alkhairy2015novelmutationsin pages 5-6, alkhairy2015novelmutationsin pages 7-9, alkhairy2015novelmutationsin pages 4-5) | Rituximab used in 6/17 with favorable sometimes transient response; conventional chemotherapy responses variable; 3/17 underwent cord blood HSCT and were alive. (alkhairy2015novelmutationsin pages 4-5, alkhairy2015novelmutationsin pages 7-9) | Alkhairy 2015, *J Allergy Clin Immunol*, https://doi.org/10.1016/j.jaci.2015.02.022 (alkhairy2015novelmutationsin pages 4-5, alkhairy2015novelmutationsin pages 5-6, alkhairy2015novelmutationsin pages 7-9) |


*Table: This table compiles reported pathogenic CD27 (TNFRSF7) variants from the retrieved evidence and links each variant to the clinical phenotype spectrum, EBV-related manifestations, and available treatment/outcome data. It is useful for quickly mapping genotype to phenotype and identifying where variant-specific versus cohort-level evidence is currently available.*

### 4.3 Functional consequence
The consistent mechanistic interpretation is **loss of CD27 function** (reduced/absent CD27 expression and/or impaired CD70 binding/costimulation), leading to defective EBV-specific T-cell expansion and impaired post-germinal-center B-cell responses. (montfrans2012cd27deficiencyis pages 8-10, tangye2020primaryimmunodeficienciesreveal pages 7-8, izawa2017inheritedcd70deficiency pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No specific modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities were identified in the retrieved evidence.

---

## 5. Environmental Information

The key environmental/infectious factor is **EBV** as a trigger for disease expression and progression to LPD/HLH/lymphoma. (ghosh2020extendedclinicaland pages 2-3, salzer2013combinedimmunodeficiencywith pages 1-2)

A 2023 report noted concomitant **SARS-CoV-2 infection** in an infant with CD27 deficiency, but causal contribution to the phenotype remains uncertain. (golchehre2023newpresentationof pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Core molecular mechanism (CD27–CD70 costimulation)
CD27 is a **TNFR superfamily** costimulatory receptor expressed on multiple immune subsets, and its ligand **CD70** is induced on activated and EBV-infected B cells. CD27–CD70 engagement provides costimulation that enhances **T-cell activation, survival, proliferation, and differentiation**, which is required for effective anti-EBV immunity. (tangye2020primaryimmunodeficienciesreveal pages 7-8, izawa2017inheritedcd70deficiency pages 1-2, ghosh2020extendedclinicaland pages 2-3)

**Direct abstract-supported statement (example):** Salzer et al. reported: “*CD27… interacts with CD70 and influences T-, B- and NK-cell functions. Disturbance of this axis impairs immunity and memory generation against viruses including Epstein Barr virus (EBV)*.” (salzer2013combinedimmunodeficiencywith pages 1-2)

### 6.2 Causal chain (from genotype to clinical manifestations)
1. **Biallelic CD27 LOF** → absent/reduced CD27 signaling. (montfrans2012cd27deficiencyis pages 2-4, alkhairy2015novelmutationsin pages 7-9)
2. **Activated/EBV-infected B cells upregulate CD70**, but cannot deliver effective CD70→CD27 costimulation to T cells. (tangye2020primaryimmunodeficienciesreveal pages 7-8, izawa2017inheritedcd70deficiency pages 1-2)
3. **Impaired EBV-specific T-cell expansion/effector function** → failure of EBV control → chronic EBV viremia and EBV-driven lymphoproliferation and lymphoma. (ghosh2020extendedclinicaland pages 2-3, tangye2020primaryimmunodeficienciesreveal pages 7-8)
4. Parallel **humoral defects** (post-germinal-center/plasma-cell biology and memory generation abnormalities) contribute to hypogammaglobulinemia and recurrent infections. (montfrans2012cd27deficiencyis pages 8-10, ghosh2020extendedclinicaland pages 2-3)

### 6.3 Cell types involved (Cell Ontology suggestions)
- **CD8+ T cells** (CL:0000625): EBV-specific cytotoxic responses impaired. (ghosh2020extendedclinicaland pages 2-3, tangye2020primaryimmunodeficienciesreveal pages 7-8)
- **B cells** (CL:0000236), especially **memory B cells** (CL:0000787) and **plasma cells** (CL:0000786): memory/plasma cell abnormalities and hypogammaglobulinemia. (montfrans2012cd27deficiencyis pages 8-10, alkhairy2015novelmutationsin pages 7-9)
- **Natural killer (NK) cells** (CL:0000623) and **invariant NKT cells** (CL:0000814): reduced function/numbers in subsets of severe patients. (alkhairy2015novelmutationsin pages 7-9, salzer2013combinedimmunodeficiencywith pages 1-2)

### 6.4 Pathway / ontology mapping suggestions
- **GO:0002429** immune response-activating cell surface receptor signaling pathway
- **GO:0031295** T cell costimulation
- **GO:0042110** T cell activation
- **GO:0002250** adaptive immune response
- **GO:0045321** leukocyte activation

(These GO mappings are consistent with costimulatory receptor biology described in primary texts but were not enumerated as GO terms in the retrieved papers.)

---

## 7. Anatomical Structures Affected

**Primary systems/organs:**
- **Lymphoid system**: lymph nodes (lymphadenopathy/LPD), spleen and liver (hepatosplenomegaly). Suggested UBERON: lymph node (UBERON:0000029), spleen (UBERON:0002106), liver (UBERON:0002107). (montfrans2012cd27deficiencyis pages 2-4, ghosh2020extendedclinicaland pages 2-3)
- **Respiratory system**: recurrent airway infections and bronchiectasis. Suggested UBERON: lung (UBERON:0002048), bronchus (UBERON:0002185). (kishore2020novelmutationin pages 2-3)
- **Eye**: uveitis in EBV context. Suggested UBERON: uvea (UBERON:0001769). (montfrans2012cd27deficiencyis pages 2-4)
- **Cardiovascular system (recent report)**: coronary artery ectasia/aneurysm. Suggested UBERON: coronary artery (UBERON:0001621). (golchehre2023newpresentationof pages 2-4)

---

## 8. Temporal Development

**Onset:** typically **childhood** (mean age of disease manifestation ~7.3 years in one multicenter cohort). (ghosh2020extendedclinicaland pages 3-4)

**Course:** variable; patients may be asymptomatic early, or develop progressive EBV viremia leading to LPD/HLH/lymphoma; autoinflammatory features may occur. (ghosh2020extendedclinicaland pages 2-3, salzer2013combinedimmunodeficiencywith pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
No robust population-level prevalence/incidence estimates were identified in the retrieved evidence. The disease is described via **rare-case aggregation**, with authors noting “more than 35 patients” reported as of 2023. (golchehre2023newpresentationof pages 1-2)

### 9.2 Population genetics and counseling-relevant points
- **Autosomal recessive inheritance**, often with **consanguinity** reported in cohorts. (alkhairy2015novelmutationsin pages 1-2)
- **High penetrance of EBV-related disease features at cohort level:** EBV positivity at diagnosis ~90% in a large cohort. (ghosh2020extendedclinicaland pages 2-3)
- **Variant spectrum:** multiple distinct mutations across cohorts, including recurrent truncating and missense variants. (alkhairy2015novelmutationsin pages 4-5, ghosh2020extendedclinicaland pages 2-3)

Carrier frequencies and founder effects were not extractable from the obtained texts (gnomAD and population-genetic databases were not queried by tools in this run).

---

## 10. Diagnostics

### 10.1 Clinical and laboratory tests
- **Flow cytometry screening:** CD27 expression on lymphocytes can be used as a screening test. (kishore2020novelmutationin pages 4-5, salzer2013combinedimmunodeficiencywith pages 1-2)
- **Humoral immunity:** serum immunoglobulins and specific antibody responses (including protein antigen responses) are informative; CD27 deficiency can present as CVID-like hypogammaglobulinemia with impaired T-dependent antibody responses. (montfrans2012cd27deficiencyis pages 6-7, alkhairy2015novelmutationsin pages 4-5)
- **EBV testing:** plasma EBV PCR/viral load monitoring, EBV serology, and detection of EBV in purified B-cell fractions were used in diagnostic workups. (montfrans2012cd27deficiencyis pages 2-4)
- **Tissue pathology:** immunohistochemistry panels and EBV tissue detection (e.g., **EBER** by CISH in lymphoma tissue) were used in a 2023 case report. (golchehre2023newpresentationof pages 2-4)

### 10.2 Genetic testing
Approaches used in reported studies include:
- **Targeted Sanger sequencing** of CD27 and related differential genes (e.g., SH2D1A, XIAP, PRF1 in one report). (montfrans2012cd27deficiencyis pages 2-4)
- **Whole-exome sequencing** with confirmatory Sanger sequencing and family segregation. (salzer2013combinedimmunodeficiencywith pages 1-2, alkhairy2015novelmutationsin pages 1-2)

### 10.3 Differential diagnosis (examples from retrieved evidence)
- **CVID** and CVID-like antibody deficiency. (kishore2020novelmutationin pages 4-5, salzer2013combinedimmunodeficiencywith pages 1-2)
- **ALPS** and lymphoproliferation/autoimmune cytopenia syndromes. (kishore2020novelmutationin pages 4-5)
- EBV-susceptibility IEIs: **XLP1 (SH2D1A)**, **XLP2 (XIAP)**, **ITK**, **MAGT1**, **CTPS1**, **CD70**, and others. (kishore2020novelmutationin pages 1-2, salzer2013combinedimmunodeficiencywith pages 1-2)

---

## 11. Outcome / Prognosis

- Disease severity is variable, ranging from asymptomatic immune subset abnormalities to life-threatening EBV-LPD/HLH and lymphoma. (salzer2013combinedimmunodeficiencywith pages 1-2)
- Reported mortality in a 17-patient cohort was **29%**. (alkhairy2015novelmutationsin pages 7-9)
- Mortality in a larger multicenter cohort included 6/33 CD27-deficient deaths (within 49 total), attributed to lymphoproliferation/lymphoma and infections. (ghosh2020extendedclinicaland pages 3-4)
- HSCT appears associated with favorable outcomes in appropriately selected severe cases (see Treatment). (ghosh2020extendedclinicaland pages 3-4)

---

## 12. Treatment (current applications / real-world implementation)

### 12.1 Supportive care
- **Immunoglobulin replacement (IgRT/IVIG):** hypogammaglobulinemia detected in **18/49** and IgG substitution given to **18/49** in a multicenter cohort. (ghosh2020extendedclinicaland pages 8-8)
- **Antibiotic prophylaxis:** provided in **17/49** in that same cohort. (ghosh2020extendedclinicaland pages 8-8)

### 12.2 EBV-driven lymphoproliferation: B-cell–directed therapy
- **Rituximab (anti-CD20):** used in **6/17** in one cohort; reported to yield **favorable (sometimes transient) responses** in EBV-related LPD/HLH/lymphoma contexts. (alkhairy2015novelmutationsin pages 4-5)

### 12.3 Hyperinflammation / HLH
- **HLH-2004/HLH-1994 protocols** were used in cohort practice; HLH-2004 was also explicitly referenced in a CD27 cohort. (ghosh2020extendedclinicaland pages 8-8, alkhairy2015novelmutationsin pages 4-5)

### 12.4 Lymphoma therapy
- Treated using disease-specific protocols; regimens cited include **ABVD/R-ABVD** and **CHOP-based** approaches in multicenter summaries. (alkhairy2015novelmutationsin pages 4-5, ghosh2020extendedclinicaland pages 8-8)
- In a 2023 case report, lymphoma was treated with **ABVD and COPP**, alongside cardiovascular-directed therapy for coronary disease. (golchehre2023newpresentationof pages 2-4)

### 12.5 Curative therapy: allogeneic HSCT
- In the multicenter cohort, **20 allogeneic HSCT procedures** were performed in **19 patients** with **95% overall survival**. (ghosh2020extendedclinicaland pages 3-4)
- Within that cohort, **11/33 (33%)** CD27-deficient patients underwent HSCT; major indications included persistent EBV viremia/LPD, lymphoma, and HLH combinations. (ghosh2020extendedclinicaland pages 8-8)

**MAXO term suggestions (not exhaustive):** hematopoietic stem cell transplantation; immunoglobulin replacement therapy; anti-CD20 monoclonal antibody therapy; antimicrobial prophylaxis; chemotherapy; HLH treatment protocol.

**Clinical trials:** No CD27-deficiency–specific interventional trials were identified via the clinical trials tool in this run.

---

## 13. Prevention

No disease-specific primary prevention strategies exist beyond genetic counseling and early diagnosis; however, practical risk reduction includes:
- **Early identification** and monitoring for EBV DNAemia and lymphoproliferation. (montfrans2012cd27deficiencyis pages 2-4, ghosh2020extendedclinicaland pages 2-3)
- **Family testing/cascade screening** in autosomal recessive pedigrees once a familial variant is known. (montfrans2012cd27deficiencyis pages 2-4)

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary CD27-deficiency disease analogs were identified in the retrieved evidence.

---

## 15. Model Organisms and Experimental Systems

### 15.1 Mouse models
Mouse studies cited in human CD27-deficiency literature indicate that **Cd27−/−** impacts antiviral T-cell biology (e.g., impaired primary/memory CD4/CD8 responses and reduced IL-2–producing CD8 memory cells), supporting biological plausibility for human EBV susceptibility. (montfrans2012cd27deficiencyis pages 7-8, salzer2013combinedimmunodeficiencywith pages 1-2)

### 15.2 Human in vitro / ex vivo systems
- **EBV-transformed B-cell lines (LCLs)** and patient T cells are used to demonstrate that CD70 on B cells and CD27 on T cells are required for robust T-cell proliferation/costimulation in EBV contexts; CRISPR-modified CD70-deficient LCLs and CD27-blocking antibodies were used in mechanistic experiments. (izawa2017inheritedcd70deficiency pages 10-11)
- Patient-derived systems in early reports included **EBV-specific T-cell assays** and lysis of autologous EBV-transformed B cells, plus detailed immunophenotyping and functional B-cell differentiation assays. (montfrans2012cd27deficiencyis pages 6-7)

---

## Notes on evidence gaps (limitations of this run)
- MONDO, Orphanet, ICD-10/11, MeSH identifiers were not recovered from the obtained documents.
- Population prevalence/incidence, carrier frequency estimates (gnomAD), and founder effects were not extracted.
- No figures/tables could be retrieved via the image tool due to an extraction error for the key cohort paper.



References

1. (ghosh2020extendedclinicaland pages 2-3): S Ghosh, SK Bal, and ES Edwards. Extended clinical and immunological phenot pe and transplant outcome in cd27 and cd70 deficienc.,(23), 2638-2655. doi: 10.1182/blood. 2020006738 …. Unknown journal, 2020.

2. (tangye2020primaryimmunodeficienciesreveal pages 7-8): Stuart G. Tangye and Sylvain Latour. Primary immunodeficiencies reveal the molecular requirements for effective host defense against ebv infection. Blood, 135:644-655, Feb 2020. URL: https://doi.org/10.1182/blood.2019000928, doi:10.1182/blood.2019000928. This article has 128 citations and is from a highest quality peer-reviewed journal.

3. (salzer2013combinedimmunodeficiencywith pages 1-2): E. Salzer, S. Daschkey, S. Choo, M. Gombert, E. Santos-Valente, S. Ginzel, M. Schwendinger, O. A. Haas, G. Fritsch, W. F. Pickl, E. Forster-Waldl, A. Borkhardt, K. Boztug, K. Bienemann, and M. G. Seidel. Combined immunodeficiency with life-threatening ebv-associated lymphoproliferative disorder in patients lacking functional cd27. Haematologica, 98:473-478, Mar 2013. URL: https://doi.org/10.3324/haematol.2012.068791, doi:10.3324/haematol.2012.068791. This article has 200 citations.

4. (golchehre2023newpresentationof pages 1-2): Zahra Golchehre, Samin Sharafian, Nader Momtazmanesh, Zahra Chavoshzadeh, Abdollah Karimi, Hassan Abolhassani, Maryam Kazemi Aghdam, Koroush Vahidshahi, Seyedehatefeh Hashemimoghaddam, Farid Kosari, Zahra Khafafpour, Bibi Shahin Shamsian, and Mohammad Keramatipour. New presentation of cd27 deficiency; coronary ectasia and covid-19. Iranian Journal of Allergy, Asthma and Immunology, Feb 2023. URL: https://doi.org/10.18502/ijaai.v22i1.12013, doi:10.18502/ijaai.v22i1.12013. This article has 7 citations.

5. (alkhairy2015novelmutationsin pages 1-2): Omar K. Alkhairy, Ruy Perez-Becker, Gertjan J. Driessen, Hassan Abolhassani, Joris van Montfrans, Stephan Borte, Sharon Choo, Ning Wang, Kiki Tesselaar, Mingyan Fang, Kirsten Bienemann, Kaan Boztug, Ana Daneva, Francoise Mechinaud, Thomas Wiesel, Christian Becker, Gregor Dückers, Kathrin Siepermann, Menno C. van Zelm, Nima Rezaei, Mirjam van der Burg, Asghar Aghamohammadi, Markus G. Seidel, Tim Niehues, and Lennart Hammarström. Novel mutations in tnfrsf7/cd27: clinical, immunologic, and genetic characterization of human cd27 deficiency. The Journal of allergy and clinical immunology, 136 3:703-712.e10, Sep 2015. URL: https://doi.org/10.1016/j.jaci.2015.02.022, doi:10.1016/j.jaci.2015.02.022. This article has 160 citations.

6. (kishore2020novelmutationin pages 2-3): Rashmi Kishore, Aditya Gupta, Aditya Kumar Gupta, and Sushil Kumar Kabra. Novel mutation in the cd27 gene in a patient presenting with hypogammaglobulinemia, bronchiectasis and ebv-driven lymphoproliferative disease. BMJ Case Reports, 13:e233482, Feb 2020. URL: https://doi.org/10.1136/bcr-2019-233482, doi:10.1136/bcr-2019-233482. This article has 8 citations and is from a peer-reviewed journal.

7. (alkhairy2015novelmutationsin pages 4-5): Omar K. Alkhairy, Ruy Perez-Becker, Gertjan J. Driessen, Hassan Abolhassani, Joris van Montfrans, Stephan Borte, Sharon Choo, Ning Wang, Kiki Tesselaar, Mingyan Fang, Kirsten Bienemann, Kaan Boztug, Ana Daneva, Francoise Mechinaud, Thomas Wiesel, Christian Becker, Gregor Dückers, Kathrin Siepermann, Menno C. van Zelm, Nima Rezaei, Mirjam van der Burg, Asghar Aghamohammadi, Markus G. Seidel, Tim Niehues, and Lennart Hammarström. Novel mutations in tnfrsf7/cd27: clinical, immunologic, and genetic characterization of human cd27 deficiency. The Journal of allergy and clinical immunology, 136 3:703-712.e10, Sep 2015. URL: https://doi.org/10.1016/j.jaci.2015.02.022, doi:10.1016/j.jaci.2015.02.022. This article has 160 citations.

8. (montfrans2012cd27deficiencyis pages 2-4): Joris M. van Montfrans, Andy I.M. Hoepelman, Sigrid Otto, Marielle van Gijn, Lisette van de Corput, Roel A. de Weger, Linda Monaco-Shawver, Pinaki P. Banerjee, Elisabeth A.M. Sanders, Cornelia M. Jol–van der Zijde, Michael R. Betts, Jordan S. Orange, Andries C. Bloem, and Kiki Tesselaar. Cd27 deficiency is associated with combined immunodeficiency and persistent symptomatic ebv viremia. The Journal of allergy and clinical immunology, 129 3:787-793.e6, Mar 2012. URL: https://doi.org/10.1016/j.jaci.2011.11.013, doi:10.1016/j.jaci.2011.11.013. This article has 259 citations.

9. (alkhairy2015novelmutationsin pages 7-9): Omar K. Alkhairy, Ruy Perez-Becker, Gertjan J. Driessen, Hassan Abolhassani, Joris van Montfrans, Stephan Borte, Sharon Choo, Ning Wang, Kiki Tesselaar, Mingyan Fang, Kirsten Bienemann, Kaan Boztug, Ana Daneva, Francoise Mechinaud, Thomas Wiesel, Christian Becker, Gregor Dückers, Kathrin Siepermann, Menno C. van Zelm, Nima Rezaei, Mirjam van der Burg, Asghar Aghamohammadi, Markus G. Seidel, Tim Niehues, and Lennart Hammarström. Novel mutations in tnfrsf7/cd27: clinical, immunologic, and genetic characterization of human cd27 deficiency. The Journal of allergy and clinical immunology, 136 3:703-712.e10, Sep 2015. URL: https://doi.org/10.1016/j.jaci.2015.02.022, doi:10.1016/j.jaci.2015.02.022. This article has 160 citations.

10. (alkhairy2015novelmutationsin pages 5-6): Omar K. Alkhairy, Ruy Perez-Becker, Gertjan J. Driessen, Hassan Abolhassani, Joris van Montfrans, Stephan Borte, Sharon Choo, Ning Wang, Kiki Tesselaar, Mingyan Fang, Kirsten Bienemann, Kaan Boztug, Ana Daneva, Francoise Mechinaud, Thomas Wiesel, Christian Becker, Gregor Dückers, Kathrin Siepermann, Menno C. van Zelm, Nima Rezaei, Mirjam van der Burg, Asghar Aghamohammadi, Markus G. Seidel, Tim Niehues, and Lennart Hammarström. Novel mutations in tnfrsf7/cd27: clinical, immunologic, and genetic characterization of human cd27 deficiency. The Journal of allergy and clinical immunology, 136 3:703-712.e10, Sep 2015. URL: https://doi.org/10.1016/j.jaci.2015.02.022, doi:10.1016/j.jaci.2015.02.022. This article has 160 citations.

11. (kishore2020novelmutationin pages 4-5): Rashmi Kishore, Aditya Gupta, Aditya Kumar Gupta, and Sushil Kumar Kabra. Novel mutation in the cd27 gene in a patient presenting with hypogammaglobulinemia, bronchiectasis and ebv-driven lymphoproliferative disease. BMJ Case Reports, 13:e233482, Feb 2020. URL: https://doi.org/10.1136/bcr-2019-233482, doi:10.1136/bcr-2019-233482. This article has 8 citations and is from a peer-reviewed journal.

12. (montfrans2012cd27deficiencyis pages 6-7): Joris M. van Montfrans, Andy I.M. Hoepelman, Sigrid Otto, Marielle van Gijn, Lisette van de Corput, Roel A. de Weger, Linda Monaco-Shawver, Pinaki P. Banerjee, Elisabeth A.M. Sanders, Cornelia M. Jol–van der Zijde, Michael R. Betts, Jordan S. Orange, Andries C. Bloem, and Kiki Tesselaar. Cd27 deficiency is associated with combined immunodeficiency and persistent symptomatic ebv viremia. The Journal of allergy and clinical immunology, 129 3:787-793.e6, Mar 2012. URL: https://doi.org/10.1016/j.jaci.2011.11.013, doi:10.1016/j.jaci.2011.11.013. This article has 259 citations.

13. (golchehre2023newpresentationof pages 2-4): Zahra Golchehre, Samin Sharafian, Nader Momtazmanesh, Zahra Chavoshzadeh, Abdollah Karimi, Hassan Abolhassani, Maryam Kazemi Aghdam, Koroush Vahidshahi, Seyedehatefeh Hashemimoghaddam, Farid Kosari, Zahra Khafafpour, Bibi Shahin Shamsian, and Mohammad Keramatipour. New presentation of cd27 deficiency; coronary ectasia and covid-19. Iranian Journal of Allergy, Asthma and Immunology, Feb 2023. URL: https://doi.org/10.18502/ijaai.v22i1.12013, doi:10.18502/ijaai.v22i1.12013. This article has 7 citations.

14. (izawa2017inheritedcd70deficiency pages 10-11): Kazushi Izawa, Emmanuel Martin, Claire Soudais, Julie Bruneau, David Boutboul, Rémy Rodriguez, Christelle Lenoir, Andrew D. Hislop, Caroline Besson, Fabien Touzot, Capucine Picard, Isabelle Callebaut, Jean-Pierre de Villartay, Despina Moshous, Alain Fischer, and Sylvain Latour. Inherited cd70 deficiency in humans reveals a critical role for the cd70–cd27 pathway in immunity to epstein-barr virus infection. The Journal of Experimental Medicine, 214:73-89, Jan 2017. URL: https://doi.org/10.1084/jem.20160784, doi:10.1084/jem.20160784. This article has 181 citations.

15. (ghosh2020extendedclinicaland pages 3-4): S Ghosh, SK Bal, and ES Edwards. Extended clinical and immunological phenot pe and transplant outcome in cd27 and cd70 deficienc.,(23), 2638-2655. doi: 10.1182/blood. 2020006738 …. Unknown journal, 2020.

16. (montfrans2012cd27deficiencyis pages 8-10): Joris M. van Montfrans, Andy I.M. Hoepelman, Sigrid Otto, Marielle van Gijn, Lisette van de Corput, Roel A. de Weger, Linda Monaco-Shawver, Pinaki P. Banerjee, Elisabeth A.M. Sanders, Cornelia M. Jol–van der Zijde, Michael R. Betts, Jordan S. Orange, Andries C. Bloem, and Kiki Tesselaar. Cd27 deficiency is associated with combined immunodeficiency and persistent symptomatic ebv viremia. The Journal of allergy and clinical immunology, 129 3:787-793.e6, Mar 2012. URL: https://doi.org/10.1016/j.jaci.2011.11.013, doi:10.1016/j.jaci.2011.11.013. This article has 259 citations.

17. (izawa2017inheritedcd70deficiency pages 1-2): Kazushi Izawa, Emmanuel Martin, Claire Soudais, Julie Bruneau, David Boutboul, Rémy Rodriguez, Christelle Lenoir, Andrew D. Hislop, Caroline Besson, Fabien Touzot, Capucine Picard, Isabelle Callebaut, Jean-Pierre de Villartay, Despina Moshous, Alain Fischer, and Sylvain Latour. Inherited cd70 deficiency in humans reveals a critical role for the cd70–cd27 pathway in immunity to epstein-barr virus infection. The Journal of Experimental Medicine, 214:73-89, Jan 2017. URL: https://doi.org/10.1084/jem.20160784, doi:10.1084/jem.20160784. This article has 181 citations.

18. (kishore2020novelmutationin pages 1-2): Rashmi Kishore, Aditya Gupta, Aditya Kumar Gupta, and Sushil Kumar Kabra. Novel mutation in the cd27 gene in a patient presenting with hypogammaglobulinemia, bronchiectasis and ebv-driven lymphoproliferative disease. BMJ Case Reports, 13:e233482, Feb 2020. URL: https://doi.org/10.1136/bcr-2019-233482, doi:10.1136/bcr-2019-233482. This article has 8 citations and is from a peer-reviewed journal.

19. (ghosh2020extendedclinicaland pages 8-8): S Ghosh, SK Bal, and ES Edwards. Extended clinical and immunological phenot pe and transplant outcome in cd27 and cd70 deficienc.,(23), 2638-2655. doi: 10.1182/blood. 2020006738 …. Unknown journal, 2020.

20. (montfrans2012cd27deficiencyis pages 7-8): Joris M. van Montfrans, Andy I.M. Hoepelman, Sigrid Otto, Marielle van Gijn, Lisette van de Corput, Roel A. de Weger, Linda Monaco-Shawver, Pinaki P. Banerjee, Elisabeth A.M. Sanders, Cornelia M. Jol–van der Zijde, Michael R. Betts, Jordan S. Orange, Andries C. Bloem, and Kiki Tesselaar. Cd27 deficiency is associated with combined immunodeficiency and persistent symptomatic ebv viremia. The Journal of allergy and clinical immunology, 129 3:787-793.e6, Mar 2012. URL: https://doi.org/10.1016/j.jaci.2011.11.013, doi:10.1016/j.jaci.2011.11.013. This article has 259 citations.
