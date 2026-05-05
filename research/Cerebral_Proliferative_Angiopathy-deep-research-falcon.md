---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T11:40:56.092804'
end_time: '2026-05-05T12:00:32.890172'
duration_seconds: 1176.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cerebral Proliferative Angiopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cerebral Proliferative Angiopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cerebral Proliferative Angiopathy** covering all of the
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
- **Disease Name:** Cerebral Proliferative Angiopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cerebral Proliferative Angiopathy** covering all of the
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


# Cerebral Proliferative Angiopathy (CPA): Comprehensive Disease Characteristics Report

## Target disease
- **Disease name:** Cerebral proliferative angiopathy (CPA)
- **Category:** Complex cerebrovascular malformation / AVM-like entity
- **MONDO ID:** Not identified in the accessed primary/review literature in this run (formal MONDO/Orphanet/MeSH/ICD codes were not explicitly provided in retrieved full texts) (yamaki2020thecurrentclinical pages 1-3, tiwari2020cerebralproliferativeangiopathy pages 1-3).

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
CPA is a rare, AVM-like cerebrovascular entity that differs from “classical” brain arteriovenous malformations (bAVMs) in angioarchitecture, clinical presentation, natural history, and treatment implications (lasjaunias2008cerebralproliferativeangiopathy pages 1-2, lasjaunias2008cerebralproliferativeangiopathy pages 2-4). In the foundational Stroke cohort, CPA is described on cross-sectional imaging as **“a diffuse network of densely enhancing vascular spaces with intermingled normal brain parenchyma”** and angiographically by **non-focal angiogenetic activity** with numerous small feeders/drainers rather than a compact nidus with high-flow shunting (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, lasjaunias2008cerebralproliferativeangiopathy pages 1-2).

### 1.2 Synonyms / alternative names
Older or alternative labels used for lesions now considered CPA include:
- **“Diffuse nidus(-type) AVM”** (tiwari2020cerebralproliferativeangiopathy pages 1-3, tiwari2020cerebralproliferativeangiopathy pages 3-4)
- **“Holohemispheric giant AVM”** / “holohemispheric giant cerebral arterio-venous malformation” (yamaki2020thecurrentclinical pages 1-3, lasjaunias2008cerebralproliferativeangiopathy pages 6-7)

### 1.3 Key identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO)
Within the retrieved and read sources, no explicit mapping codes (OMIM/Orphanet/ICD/MeSH/MONDO) were provided in text (yamaki2020thecurrentclinical pages 1-3, tiwari2020cerebralproliferativeangiopathy pages 1-3, lasjaunias2008cerebralproliferativeangiopathy pages 1-2). Therefore, this report cannot safely supply specific code identifiers without introducing uncited assumptions.

### 1.4 Evidence provenance
Evidence is primarily from:
- **Aggregated disease-level resources:** systematic reviews and case series syntheses (e.g., pooled 95 cases) (yamaki2020thecurrentclinical pages 3-4, hess2022cerebralproliferativeangiopathy pages 3-4).
- **Single-center cohorts / databanks:** the Lasjaunias et al. cohort (49 CPA cases identified within an AVM databank) (lasjaunias2008cerebralproliferativeangiopathy pages 2-4).
- **Individual case reports:** especially for emerging diagnostic and therapeutic approaches (2023–2024) (jongaliem2023useofbetablocker pages 1-2, gautam2024thetreatmentof pages 2-4).

---

## 2. Etiology

### 2.1 Disease causal factors (current consensus)
No established single-gene cause, inherited syndrome, or somatic mutation driver was identified in the accessed literature. Instead, CPA is repeatedly framed as a **hemodynamic/angiogenic disorder**, hypothesized to arise from chronic regional hypoperfusion (perinidal oligemia/ischemia) leading to **diffuse angiogenesis** (lasjaunias2008cerebralproliferativeangiopathy pages 6-7, yamaki2020thecurrentclinical pages 1-3).

- Lasjaunias et al. propose: **“diffuse angiogenetic activity… related to reduced perinidal perfusion and subsequent chronic cortical ischemia”** (lasjaunias2008cerebralproliferativeangiopathy pages 1-2).
- A systematic review notes: **“Its epidemiology and pathophysiology are uncertain”** and proposes “vascular proliferation in response to chronic parenchymal ischemia/oligemia” (yamaki2020thecurrentclinical pages 1-3).

### 2.2 Risk factors
Robust epidemiologic risk-factor data (e.g., hypertension, smoking, etc.) were not identified in the accessed evidence base; the available literature is dominated by case reports/series and imaging-characterization studies (yamaki2020thecurrentclinical pages 3-4, hess2022cerebralproliferativeangiopathy pages 3-4). Demographic associations (young age, female predominance) are described (see Epidemiology below) but should be treated as descriptive rather than causal (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, yamaki2020thecurrentclinical pages 3-4).

### 2.3 Protective factors
No protective genetic or environmental factors were reported in the accessed literature.

### 2.4 Gene–environment interactions
No gene–environment interactions were reported in the accessed literature.

### 2.5 Genetic/molecular associations (what is known)
- **Genetic causes:** Not reported in the accessed sources (yamaki2020thecurrentclinical pages 1-3, lasjaunias2008cerebralproliferativeangiopathy pages 6-7, jongaliem2023useofbetablocker pages 2-4).
- **Angiogenic mediators:** Reviews describe evidence compatible with angiogenic signaling (e.g., VEGF) and discuss speculative anti-angiogenic approaches; however, high-level clinical evidence is lacking (tiwari2020cerebralproliferativeangiopathy pages 3-4, jongaliem2023useofbetablocker pages 2-4).

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with frequencies)
From Lasjaunias et al. (49 cases): seizures **45%**, headaches **41%**, TIAs/stroke-like symptoms **16%**, hemorrhage **12%** (lasjaunias2008cerebralproliferativeangiopathy pages 2-4). From a 2020 systematic review (95 cases): headache **44.9%**, seizures **37.1%**, transient ischemic attacks **33.7%**, hemorrhage **18.0%** (yamaki2020thecurrentclinical pages 3-4).

**Pediatric phenotype (aggregate of 29 cases):** focal deficits (n=17), headache (n=15), seizures (n=6) (moskalik2026cerebralproliferativeangiopathy pages 1-3).

### 3.2 Phenotype characteristics
- **Typical age of onset/presentation:** young (mean ~22–23 years in mixed-age cohorts) (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, yamaki2020thecurrentclinical pages 3-4).
- **Severity/progression:** presentations often relate to seizures, disabling headaches, and progressive focal deficits; hemorrhagic presentations are comparatively less common but may recur once present (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, lasjaunias2008cerebralproliferativeangiopathy pages 6-7).

### 3.3 Suggested HPO terms (examples)
(terms suggested for knowledge-base structuring; not claims of asserted ontology mapping)
- Headache (HP:0002315)
- Seizures (HP:0001250)
- Transient ischemic attack (HP:0002326)
- Hemiparesis (HP:0001269)
- Aphasia (HP:0002381)
- Intracranial hemorrhage (HP:0002170) / Intraventricular hemorrhage (HP:0002133)

### 3.4 Quality-of-life impact
Disabling headaches and medically refractory seizures are emphasized as reasons patients seek care and as treatment drivers, reflecting substantial functional burden (lasjaunias2008cerebralproliferativeangiopathy pages 1-2, jongaliem2023useofbetablocker pages 1-2).

---

## 4. Genetic / molecular information

### 4.1 Causal genes
No validated causal genes were identified in the accessed CPA literature (yamaki2020thecurrentclinical pages 1-3, lasjaunias2008cerebralproliferativeangiopathy pages 6-7).

### 4.2 Pathogenic variants / somatic vs germline
Not established for CPA in the accessed sources.

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
Not reported in the accessed sources.

### 4.4 Molecular hypotheses (angiogenesis)
CPA is repeatedly linked to **angiogenesis driven by chronic hypoperfusion/oligemia** (lasjaunias2008cerebralproliferativeangiopathy pages 6-7, jongaliem2023useofbetablocker pages 2-4). A 2023 propranolol case report argues for an anti-VEGF/anti-proliferative rationale, stating propranolol is a “VEGF inhibitory agent” and hypothesizing “Propranolol may have an antiproliferative effect on CPA” (jongaliem2023useofbetablocker pages 1-2).

---

## 5. Environmental information
No specific environmental exposures, toxins, lifestyle factors, or infectious triggers were reported in the accessed CPA literature.

---

## 6. Mechanism / pathophysiology

### 6.1 Proposed causal chain (current model)
**Chronic regional hypoperfusion (oligemia/ischemia)** → **reactive/diffuse angiogenesis** (including transdural supply and recruitment of multiple small-caliber vessels) → **diffuse intraparenchymal vascular network with intermingled normal brain** → clinical syndromes dominated by seizures/headache/ischemic deficits rather than primary hemorrhage (lasjaunias2008cerebralproliferativeangiopathy pages 1-2, lasjaunias2008cerebralproliferativeangiopathy pages 6-7, tiwari2020cerebralproliferativeangiopathy pages 3-4).

Key supportive observations include perfusion MRI patterns: CPA shows increased blood volume with **prolonged mean transit time** and broader hemispheric hypoperfusion compared with classical AVMs (lasjaunias2008cerebralproliferativeangiopathy pages 6-7).

### 6.2 Pathology (human)
CPA differs from classic AVM histology by preservation of neural tissue within the lesion; pathology shows vascular wall abnormalities and **“normal appearing neural tissue intermingled between these vascular channels”** (lasjaunias2008cerebralproliferativeangiopathy pages 4-6).

### 6.3 Suggested GO biological process terms (examples)
- Angiogenesis (GO:0001525)
- Response to hypoxia (GO:0001666)
- Regulation of vascular permeability (GO:0043114)
- Endothelial cell proliferation (GO:0001935)

### 6.4 Suggested Cell Ontology (CL) terms (examples)
- Endothelial cell (CL:0000115)
- Vascular smooth muscle cell (CL:0000192)
- Pericyte (CL:0000669)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- **Primary:** brain (central nervous system) (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, singfer2023cerebralproliferativeangiopathy pages 1-4).

### 7.2 Localization patterns (imaging-derived)
Lesions are often large and may span lobes/hemisphere; in one pooled review, hemispheric extension was reported in **73.0%** (yamaki2020thecurrentclinical pages 3-4). Watershed-zone predominance (70.6%) supports a hypoperfusion-linked distribution (yamaki2020thecurrentclinical pages 3-4).

### 7.3 Suggested UBERON terms (examples)
- Brain (UBERON:0000955)
- Cerebral cortex (UBERON:0000956)
- Cerebral hemisphere (UBERON:0002812)
- Basal ganglia (UBERON:0002532)
- Thalamus (UBERON:0001897)

---

## 8. Temporal development (onset and progression)

### 8.1 Typical onset pattern
CPA is usually recognized in young patients, often after neurologic symptoms (seizures, headache, TIAs) rather than hemorrhage (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, yamaki2020thecurrentclinical pages 3-4).

### 8.2 Evidence for dynamic evolution
A 2023 pediatric case report described diagnosis of CPA **five years after** intraventricular hemorrhage and an initially negative catheter angiogram, interpreted as supportive of new-vessel formation/angiogenesis as part of disease evolution (singfer2023cerebralproliferativeangiopathy pages 1-4).

---

## 9. Inheritance and population

### 9.1 Epidemiology (descriptive)
CPA is a minority subset among lesions labeled AVM in major series:
- Lasjaunias et al.: **49/1434 (3.4%)** of AVM databank cases met CPA criteria (lasjaunias2008cerebralproliferativeangiopathy pages 2-4).

### 9.2 Demographics
- Lasjaunias et al.: mean age **22**, female **67%** (lasjaunias2008cerebralproliferativeangiopathy pages 2-4).
- Systematic review (95 cases): mean age **23**, female **60%** (yamaki2020thecurrentclinical pages 3-4).

### 9.3 Inheritance
No inheritance pattern has been established in the accessed evidence base (yamaki2020thecurrentclinical pages 1-3, lasjaunias2008cerebralproliferativeangiopathy pages 6-7).

---

## 10. Diagnostics

### 10.1 Core diagnostic modalities
**Digital subtraction angiography (DSA)** is emphasized as the diagnostic reference standard for angioarchitecture (tiwari2020cerebralproliferativeangiopathy pages 3-4, yamaki2020thecurrentclinical pages 1-3).

**Key diagnostic imaging features** include:
- Diffuse vascular network with **intermingled normal brain parenchyma** (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, singfer2023cerebralproliferativeangiopathy pages 1-4).
- Discrepancy between **large lesion size** and **small shunting volume** (lasjaunias2008cerebralproliferativeangiopathy pages 1-2).
- **No dominant arterial feeder**, many small feeders; small draining veins relative to lesion (lasjaunias2008cerebralproliferativeangiopathy pages 1-2, lasjaunias2008cerebralproliferativeangiopathy pages 4-6).
- **Transdural supply** and **proximal feeder stenoses** (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, yamaki2020thecurrentclinical pages 3-4).

**Perfusion/functional hemodynamic testing** may support a steal/hypoperfusion mechanism.
- A 2024 case report used **CT perfusion with acetazolamide challenge** to attribute aphasia to steal physiology (gautam2024thetreatmentof pages 1-2, gautam2024thetreatmentof pages 2-4).

### 10.2 Differential diagnosis
Commonly discussed differentials include:
- **Classic brain AVM** (compact nidus, higher hemorrhagic presentation proportion) (yamaki2020thecurrentclinical pages 3-4, lasjaunias2008cerebralproliferativeangiopathy pages 1-2).
- **Moyamoya disease** / moyamoya-like vasculopathies (noted as differential in case literature) (jongaliem2023useofbetablocker pages 1-2).

### 10.3 Visual evidence (representative MRI + DSA)
A 2023 case report provides representative MRI and DSA figures showing a diffuse vascular network with persistent opacification into late arterial/early venous phases and no dominant feeders (singfer2023cerebralproliferativeangiopathy media 68b06269, singfer2023cerebralproliferativeangiopathy media 94c84d95).

---

## 11. Outcome / prognosis

### 11.1 Hemorrhage risk and rebleeding
CPA generally presents with hemorrhage less often than classical AVMs, but recurrence risk after hemorrhage may be high.
- Lasjaunias cohort: hemorrhage at presentation **12% (6/49)**; among those with hemorrhage, recurrent bleeding reported in **67%**, with one death (lasjaunias2008cerebralproliferativeangiopathy pages 2-4).
- Systematic review: hemorrhage in **18%** and reported rebleeding up to **67%** in some series (yamaki2020thecurrentclinical pages 3-4).

### 11.2 Functional outcomes (systematic reviews)
- Systematic review (95 cases): improved **50.7%**, stable **40.2%**, worsened **9.0%** at mean follow-up ~17 months (yamaki2020thecurrentclinical pages 3-4).
- Another systematic review (84 patients; 78 with outcomes): conservative management led to spontaneous improvement **39.7%**, worsening **46.1%**, no change **12.8%** (hess2022cerebralproliferativeangiopathy pages 3-4).

---

## 12. Treatment

### 12.1 Overarching strategy (expert synthesis)
Because normal brain tissue is interspersed with abnormal vessels, aggressive curative therapies used for compact AVMs may cause unacceptable neurologic injury. Lasjaunias et al. explicitly caution that “normal brain is interspersed with the abnormal vascular channels increasing the risk of neurological deficit in aggressive treatments,” and given “low risk of hemorrhage,” aggressive treatment is often not indicated (lasjaunias2008cerebralproliferativeangiopathy pages 1-2).

### 12.2 Real-world treatment utilization (systematic review data)
From Yamaki et al. (95 cases): conservative **54.4%**, endovascular **34.2%**, indirect revascularization **7.6%**, radiosurgery **2.5%**, decompression **1.3%** (yamaki2020thecurrentclinical pages 5-7).

From Hess et al. (84 patients): conservative **59.5%**, embolization **28.6%** (hess2022cerebralproliferativeangiopathy pages 3-4).

### 12.3 Endovascular therapy (targeted/partial embolization)
Targeted embolization is discussed as a selective strategy (e.g., fragile angioarchitecture or hemorrhagic foci) rather than curative obliteration, due to risk to intermingled parenchyma (yamaki2020thecurrentclinical pages 3-4, lasjaunias2008cerebralproliferativeangiopathy pages 1-2).

### 12.4 Surgical / revascularization approaches
A systematic review focused on revascularization summarizes the rationale: revascularization is proposed to “disrupt regional hypoperfusion and interrupt the angiogenesis that defines CPA,” with early small-series results favorable but limited (hess2022cerebralproliferativeangiopathy pages 3-4).

Pediatric aggregation emphasizes indirect revascularization (e.g., pial synangiosis, burr-hole dural inversion) for symptomatic hypoperfusion, with reported durable collateralization and functional gains in illustrative follow-up (moskalik2026cerebralproliferativeangiopathy pages 1-3).

### 12.5 Emerging medical therapies (prioritize 2023–2024)

**(a) Propranolol (beta-blocker) – 2023 case report**
A 2023 report describes long-term propranolol use for disabling headaches with reported angiographic “shrinkage of the vascular network” over 7 years, hypothesized via VEGF inhibition/antiproliferative effects; this remains anecdotal evidence (jongaliem2023useofbetablocker pages 2-4).

**(b) Cilostazol (vasodilating agent) – 2024 case report**
A 2024 case report (Diffuse Proliferative Cerebral Angiopathy) reported rapid symptomatic improvement of aphasia after cilostazol in a steal-phenomenon phenotype confirmed by perfusion/acetazolamide challenge. The abstract states: **“Within three days of treatment with cilostazol, the patient showed significant improvement in his aphasia.”** (gautam2024thetreatmentof pages 1-2). Quantitative perfusion metrics (Tmax>4s and rCBF<38% volumes) improved after acetazolamide and over follow-up (gautam2024thetreatmentof pages 2-4).

### 12.6 MAXO term suggestions (examples)
- Endovascular embolization procedure (MAXO:0000508; suggest)
- Cerebral revascularization (MAXO:0000463; suggest)
- Antiepileptic drug therapy (MAXO:0000635; suggest)
- Beta-adrenergic blocker therapy (MAXO:0000955; suggest)
- Antiplatelet therapy (MAXO:0000645; suggest)

### 12.7 Clinical trials
A ClinicalTrials.gov search using CPA terms did not identify CPA-specific interventional trials in the retrieved results; the returned trials were unrelated (diabetes microangiopathy) (tool result; no CPA trial context IDs available for citation).

---

## 13. Prevention
No primary-prevention interventions (vaccines, exposure avoidance) are described for CPA in the accessed literature. Prevention is best framed as:
- **Secondary prevention:** avoiding misclassification as classic AVM and avoiding harmful aggressive AVM-directed eradication attempts (lasjaunias2008cerebralproliferativeangiopathy pages 1-2, singfer2023cerebralproliferativeangiopathy pages 1-4).
- **Tertiary prevention:** seizure control, headache management, and individualized management of hypoperfusion/steal phenomena (jongaliem2023useofbetablocker pages 1-2, gautam2024thetreatmentof pages 2-4).

---

## 14. Other species / natural disease
No natural disease analogs in non-human species were identified in the accessed literature.

---

## 15. Model organisms
No CPA-specific animal models, cellular models, or iPSC/organoid models were identified in the accessed literature.

---

# Summary artifact
The following table consolidates key quantitative and qualitative disease facts from the strongest available evidence (foundational cohort + systematic reviews + recent case reports).

| Domain | Key details (with numbers) | Main supporting sources (first author year; include URL) | Evidence type |
|---|---|---|---|
| Definition / classification | CPA is a rare cerebrovascular lesion distinct from classical brain AVM, characterized by a diffuse vascular network intermingled with normal brain parenchyma, large lesion size with relatively small shunting volume, and evidence of diffuse angiogenesis. In the original cohort, CPA represented 49/1434 AVM-database cases (3.4%). (lasjaunias2008cerebralproliferativeangiopathy pages 1-2, lasjaunias2008cerebralproliferativeangiopathy pages 2-4) | Lasjaunias 2008, https://doi.org/10.1161/STROKEAHA.107.493080; Yamaki 2020, https://doi.org/10.1007/s00701-020-04289-7 | Prospective databank cohort; systematic review |
| Demographics | Original series: mean age 22 years, 67% female. Systematic review of 95 cases: mean age 23 years, 60.0% female. Female predominance is roughly 2:1 in several summaries. (lasjaunias2008cerebralproliferativeangiopathy pages 1-2, yamaki2020thecurrentclinical pages 3-4, tiwari2020cerebralproliferativeangiopathy pages 3-4) | Lasjaunias 2008, https://doi.org/10.1161/STROKEAHA.107.493080; Yamaki 2020, https://doi.org/10.1007/s00701-020-04289-7; Tiwari 2020, https://doi.org/10.1055/s-0039-3401329 | Cohort; systematic review; case-based review |
| Presenting symptoms frequencies | Original cohort: seizures 45%, headaches 41%, TIAs/stroke-like symptoms 16%, hemorrhage 12%. Pooled review: headache 44.9%, seizures 37.1%, transient ischemic attacks 33.7%. Pediatric review (29 cases): focal deficits n=17, headache n=15, seizures n=6. (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, yamaki2020thecurrentclinical pages 3-4, moskalik2026cerebralproliferativeangiopathy pages 1-3) | Lasjaunias 2008, https://doi.org/10.1161/STROKEAHA.107.493080; Yamaki 2020, https://doi.org/10.1007/s00701-020-04289-7; Moskalik 2026, https://doi.org/10.1007/s00381-026-07129-8 | Cohort; systematic reviews |
| Hemorrhage frequency / rebleed | Hemorrhagic presentation is uncommon: 12% (6/49) in the original cohort and 18.0% in the pooled review. However, once hemorrhage occurs, reported rebleeding is high: 67% in the original cohort / up to 67% in pooled literature; one death was reported in the original series. (lasjaunias2008cerebralproliferativeangiopathy pages 2-4, yamaki2020thecurrentclinical pages 3-4, lasjaunias2008cerebralproliferativeangiopathy pages 6-7) | Lasjaunias 2008, https://doi.org/10.1161/STROKEAHA.107.493080; Yamaki 2020, https://doi.org/10.1007/s00701-020-04289-7 | Cohort; systematic review |
| Key angiographic hallmarks | Typical DSA features: absence of dominant feeders; many small-caliber feeding arteries and draining veins; fuzzy/poorly circumscribed nidus; discrepancy between large nidus and small shunt volume; capillary angioectatic appearance 85.7% (43/49 in original cohort); perinidal angiogenesis ~46.6%-49%; transdural supply 59%-62.5%; proximal feeder stenosis 39%-43.1%; deep venous drainage 73%; no flow-related aneurysms. Nidus size often 3-6 cm (47.5%) or >6 cm (52.5%), with hemispheric extension 73%. (lasjaunias2008cerebralproliferativeangiopathy pages 4-6, yamaki2020thecurrentclinical pages 1-3, yamaki2020thecurrentclinical pages 3-4, lasjaunias2008cerebralproliferativeangiopathy pages 1-2) | Lasjaunias 2008, https://doi.org/10.1161/STROKEAHA.107.493080; Yamaki 2020, https://doi.org/10.1007/s00701-020-04289-7 | Cohort; systematic review |
| Key MRI / perfusion features | MRI/CT typically show a diffuse enhancing vascular network with normal brain parenchyma interspersed. Perfusion MRI shows increased CBV within the nidus, prolonged mean transit time, and widespread cortical/subcortical hypoperfusion remote from the nidus (increased TTP, decreased CBV in surrounding regions), supporting chronic oligemia/ischemia. DSA remains the diagnostic gold standard. (lasjaunias2008cerebralproliferativeangiopathy pages 6-7, tiwari2020cerebralproliferativeangiopathy pages 3-4, lasjaunias2008cerebralproliferativeangiopathy pages 1-2) | Lasjaunias 2008, https://doi.org/10.1161/STROKEAHA.107.493080; Tiwari 2020, https://doi.org/10.1055/s-0039-3401329; Singfer 2023, https://doi.org/10.5334/jbsr.3247 | Cohort; case-based review; case report |
| Management patterns and outcomes | Pooled review: conservative treatment 54.4%, endovascular treatment 34.2%, indirect revascularization 7.6%, radiosurgery 2.5%, decompression 1.3%. Outcomes at mean ~17 months: improved 50.7%, stable 40.2%, worsened 9.0%. In another review of 84 patients, conservative care was 59.5% and embolization 28.6%; among 78 with outcomes, conservative management led to spontaneous improvement in 39.7%, worsening in 46.1%, and no change in 12.8%. Original cohort follow-up totaled 145 patient-years (mean 3 years): after treatment, 16 improved, 6 were stable, 1 worsened. (yamaki2020thecurrentclinical pages 3-4, hess2022cerebralproliferativeangiopathy pages 3-4, lasjaunias2008cerebralproliferativeangiopathy pages 4-6) | Yamaki 2020, https://doi.org/10.1007/s00701-020-04289-7; Hess 2022, https://doi.org/10.1016/j.wneu.2022.05.096; Lasjaunias 2008, https://doi.org/10.1161/STROKEAHA.107.493080 | Systematic reviews; cohort |
| Selected emerging/individual treatment observations | Indirect cerebral revascularization has shown favorable outcomes in most small reported series and is used particularly for ischemic/hypoperfusion phenotypes. A 2023 case report described symptomatic and angiographic improvement over 7 years with propranolol, proposed as anti-angiogenic/VEGF-modulating therapy, but evidence remains anecdotal. (jongaliem2023useofbetablocker pages 1-2, moskalik2026cerebralproliferativeangiopathy pages 1-3) | Jong-A-Liem 2023, https://doi.org/10.1016/j.inat.2022.101663; Moskalik 2026, https://doi.org/10.1007/s00381-026-07129-8 | Case report; systematic review + illustrative case |


*Table: This table summarizes the most clinically relevant facts about cerebral proliferative angiopathy, including how it is defined, how it presents, how it is diagnosed on imaging, and how it is managed. It is useful as a concise evidence-backed reference for distinguishing CPA from classical brain AVM.*

---

## Key references (with publication dates and URLs)
- Lasjaunias PL et al. **2008-03**. *Stroke*. “Cerebral proliferative angiopathy…” https://doi.org/10.1161/STROKEAHA.107.493080 (lasjaunias2008cerebralproliferativeangiopathy pages 2-4)
- Yamaki VN et al. **2020-03**. *Acta Neurochirurgica*. “The current clinical picture…” https://doi.org/10.1007/s00701-020-04289-7 (yamaki2020thecurrentclinical pages 3-4)
- Hess RM et al. **2022-08**. *World Neurosurgery*. “CPA presenting as subdural hematoma…” https://doi.org/10.1016/j.wneu.2022.05.096 (hess2022cerebralproliferativeangiopathy pages 3-4)
- Singfer U et al. **2023-08**. *J Belgian Soc Radiol*. “CPA in a child…” https://doi.org/10.5334/jbsr.3247 (singfer2023cerebralproliferativeangiopathy pages 1-4)
- Jong-A-Liem GS et al. **2023-03**. *Interdisciplinary Neurosurgery*. “Use of beta-blocker…” https://doi.org/10.1016/j.inat.2022.101663 (jongaliem2023useofbetablocker pages 2-4)
- Gautam D et al. **2024-06**. *Cureus*. “Treatment… with cilostazol” https://doi.org/10.7759/cureus.63387 (gautam2024thetreatmentof pages 1-2)


References

1. (yamaki2020thecurrentclinical pages 1-3): Vitor Nagai Yamaki, Davi Jorge Fontoura Solla, João Paulo Mota Telles, Glaucia Lexy Jong Liem, Saul Almeida da Silva, José Guilherme Mendes Pereira Caldas, Manoel Jacobsen Teixeira, Eric Homero Albuquerque Paschoal, and Eberval Gadelha Figueiredo. The current clinical picture of cerebral proliferative angiopathy: systematic review. Acta Neurochirurgica, 162:1727-1733, Mar 2020. URL: https://doi.org/10.1007/s00701-020-04289-7, doi:10.1007/s00701-020-04289-7. This article has 25 citations and is from a peer-reviewed journal.

2. (tiwari2020cerebralproliferativeangiopathy pages 1-3): Sarbesh Tiwari, Pawan K. Garg, Pushpinder S. Khera, Santhosh Babu, Binit Sureka, and Taruna Yadav. Cerebral proliferative angiopathy: an uncommon and misdiagnosed entity. Journal of Clinical Interventional Radiology ISVIR, 4:107-110, Feb 2020. URL: https://doi.org/10.1055/s-0039-3401329, doi:10.1055/s-0039-3401329. This article has 7 citations.

3. (lasjaunias2008cerebralproliferativeangiopathy pages 1-2): Pierre L. Lasjaunias, Pierre Landrieu, Georges Rodesch, Hortensia Alvarez, Augustin Ozanne, Staffan Holmin, Wen-Yuan Zhao, Sasikhan Geibprasert, Dennis Ducreux, and Timo Krings. Cerebral proliferative angiopathy: clinical and angiographic description of an entity different from cerebral avms. Stroke, 39:878-885, Mar 2008. URL: https://doi.org/10.1161/strokeaha.107.493080, doi:10.1161/strokeaha.107.493080. This article has 174 citations and is from a highest quality peer-reviewed journal.

4. (lasjaunias2008cerebralproliferativeangiopathy pages 2-4): Pierre L. Lasjaunias, Pierre Landrieu, Georges Rodesch, Hortensia Alvarez, Augustin Ozanne, Staffan Holmin, Wen-Yuan Zhao, Sasikhan Geibprasert, Dennis Ducreux, and Timo Krings. Cerebral proliferative angiopathy: clinical and angiographic description of an entity different from cerebral avms. Stroke, 39:878-885, Mar 2008. URL: https://doi.org/10.1161/strokeaha.107.493080, doi:10.1161/strokeaha.107.493080. This article has 174 citations and is from a highest quality peer-reviewed journal.

5. (tiwari2020cerebralproliferativeangiopathy pages 3-4): Sarbesh Tiwari, Pawan K. Garg, Pushpinder S. Khera, Santhosh Babu, Binit Sureka, and Taruna Yadav. Cerebral proliferative angiopathy: an uncommon and misdiagnosed entity. Journal of Clinical Interventional Radiology ISVIR, 4:107-110, Feb 2020. URL: https://doi.org/10.1055/s-0039-3401329, doi:10.1055/s-0039-3401329. This article has 7 citations.

6. (lasjaunias2008cerebralproliferativeangiopathy pages 6-7): Pierre L. Lasjaunias, Pierre Landrieu, Georges Rodesch, Hortensia Alvarez, Augustin Ozanne, Staffan Holmin, Wen-Yuan Zhao, Sasikhan Geibprasert, Dennis Ducreux, and Timo Krings. Cerebral proliferative angiopathy: clinical and angiographic description of an entity different from cerebral avms. Stroke, 39:878-885, Mar 2008. URL: https://doi.org/10.1161/strokeaha.107.493080, doi:10.1161/strokeaha.107.493080. This article has 174 citations and is from a highest quality peer-reviewed journal.

7. (yamaki2020thecurrentclinical pages 3-4): Vitor Nagai Yamaki, Davi Jorge Fontoura Solla, João Paulo Mota Telles, Glaucia Lexy Jong Liem, Saul Almeida da Silva, José Guilherme Mendes Pereira Caldas, Manoel Jacobsen Teixeira, Eric Homero Albuquerque Paschoal, and Eberval Gadelha Figueiredo. The current clinical picture of cerebral proliferative angiopathy: systematic review. Acta Neurochirurgica, 162:1727-1733, Mar 2020. URL: https://doi.org/10.1007/s00701-020-04289-7, doi:10.1007/s00701-020-04289-7. This article has 25 citations and is from a peer-reviewed journal.

8. (hess2022cerebralproliferativeangiopathy pages 3-4): Ryan M. Hess, Jeff F. Zhang, Justin M. Cappuzzo, Amade Bregy, and Elad I. Levy. Cerebral proliferative angiopathy presenting as subdural hematoma: a case report and systematic literature review. World Neurosurgery, 164:281-289, Aug 2022. URL: https://doi.org/10.1016/j.wneu.2022.05.096, doi:10.1016/j.wneu.2022.05.096. This article has 5 citations and is from a peer-reviewed journal.

9. (jongaliem2023useofbetablocker pages 1-2): Glaucia Suzanna Jong-A-Liem, Lillian dos Santos Carneiro, Fernando Mendes Paschoal Junior, Feres Eduardo Aparecido Chaddad Neto, Eberval Figueiredo Gadelha, E. Bor-Seng-Shu, and Eric Homero Albuquerque Paschoal. Use of beta-blocker in cerebral proliferative angiopathy: a case report. Interdisciplinary Neurosurgery, 31:101663, Mar 2023. URL: https://doi.org/10.1016/j.inat.2022.101663, doi:10.1016/j.inat.2022.101663. This article has 1 citations and is from a peer-reviewed journal.

10. (gautam2024thetreatmentof pages 2-4): Diwas Gautam, Daryl E Morrison, Michael T. Bounajem, Lubdha M. Shah, and Ramesh Grandhi. The treatment of symptomatic diffuse proliferative cerebral angiopathy with cilostazol: a case report. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.63387, doi:10.7759/cureus.63387. This article has 2 citations.

11. (jongaliem2023useofbetablocker pages 2-4): Glaucia Suzanna Jong-A-Liem, Lillian dos Santos Carneiro, Fernando Mendes Paschoal Junior, Feres Eduardo Aparecido Chaddad Neto, Eberval Figueiredo Gadelha, E. Bor-Seng-Shu, and Eric Homero Albuquerque Paschoal. Use of beta-blocker in cerebral proliferative angiopathy: a case report. Interdisciplinary Neurosurgery, 31:101663, Mar 2023. URL: https://doi.org/10.1016/j.inat.2022.101663, doi:10.1016/j.inat.2022.101663. This article has 1 citations and is from a peer-reviewed journal.

12. (moskalik2026cerebralproliferativeangiopathy pages 1-3): Anzhela D. Moskalik, Jonathan Mo, Monifa Sawyerr, Marike Zwienenberg, Branden Cord, and Julia D. Sharma. Cerebral proliferative angiopathy in pediatric patients: case-based review with an illustrative case. Child's Nervous System, Feb 2026. URL: https://doi.org/10.1007/s00381-026-07129-8, doi:10.1007/s00381-026-07129-8. This article has 0 citations.

13. (lasjaunias2008cerebralproliferativeangiopathy pages 4-6): Pierre L. Lasjaunias, Pierre Landrieu, Georges Rodesch, Hortensia Alvarez, Augustin Ozanne, Staffan Holmin, Wen-Yuan Zhao, Sasikhan Geibprasert, Dennis Ducreux, and Timo Krings. Cerebral proliferative angiopathy: clinical and angiographic description of an entity different from cerebral avms. Stroke, 39:878-885, Mar 2008. URL: https://doi.org/10.1161/strokeaha.107.493080, doi:10.1161/strokeaha.107.493080. This article has 174 citations and is from a highest quality peer-reviewed journal.

14. (singfer2023cerebralproliferativeangiopathy pages 1-4): Uri Singfer, Edward Baert, and Luc Defreyne. Cerebral proliferative angiopathy in a child, five years after an intraventricular hemorrhage and negative catheter angiography. Journal of the Belgian Society of Radiology, Aug 2023. URL: https://doi.org/10.5334/jbsr.3247, doi:10.5334/jbsr.3247. This article has 5 citations.

15. (gautam2024thetreatmentof pages 1-2): Diwas Gautam, Daryl E Morrison, Michael T. Bounajem, Lubdha M. Shah, and Ramesh Grandhi. The treatment of symptomatic diffuse proliferative cerebral angiopathy with cilostazol: a case report. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.63387, doi:10.7759/cureus.63387. This article has 2 citations.

16. (singfer2023cerebralproliferativeangiopathy media 68b06269): Uri Singfer, Edward Baert, and Luc Defreyne. Cerebral proliferative angiopathy in a child, five years after an intraventricular hemorrhage and negative catheter angiography. Journal of the Belgian Society of Radiology, Aug 2023. URL: https://doi.org/10.5334/jbsr.3247, doi:10.5334/jbsr.3247. This article has 5 citations.

17. (singfer2023cerebralproliferativeangiopathy media 94c84d95): Uri Singfer, Edward Baert, and Luc Defreyne. Cerebral proliferative angiopathy in a child, five years after an intraventricular hemorrhage and negative catheter angiography. Journal of the Belgian Society of Radiology, Aug 2023. URL: https://doi.org/10.5334/jbsr.3247, doi:10.5334/jbsr.3247. This article has 5 citations.

18. (yamaki2020thecurrentclinical pages 5-7): Vitor Nagai Yamaki, Davi Jorge Fontoura Solla, João Paulo Mota Telles, Glaucia Lexy Jong Liem, Saul Almeida da Silva, José Guilherme Mendes Pereira Caldas, Manoel Jacobsen Teixeira, Eric Homero Albuquerque Paschoal, and Eberval Gadelha Figueiredo. The current clinical picture of cerebral proliferative angiopathy: systematic review. Acta Neurochirurgica, 162:1727-1733, Mar 2020. URL: https://doi.org/10.1007/s00701-020-04289-7, doi:10.1007/s00701-020-04289-7. This article has 25 citations and is from a peer-reviewed journal.