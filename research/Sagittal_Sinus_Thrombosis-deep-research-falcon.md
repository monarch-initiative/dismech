---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T08:41:30.800310'
end_time: '2026-05-06T08:56:15.283523'
duration_seconds: 884.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sagittal Sinus Thrombosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sagittal Sinus Thrombosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sagittal Sinus Thrombosis** covering all of the
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
- **Disease Name:** Sagittal Sinus Thrombosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sagittal Sinus Thrombosis** covering all of the
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


# Comprehensive Disease Characteristics Report: Sagittal Sinus Thrombosis (Superior Sagittal Sinus Thrombosis)

## Executive summary
Sagittal sinus thrombosis typically refers to **superior sagittal sinus (SSS) thrombosis**, a common site of **cerebral venous thrombosis (CVT)/cerebral venous sinus thrombosis (CVST)**, an uncommon stroke subtype caused by thrombus formation in dural venous sinuses and/or cerebral veins. (umurungi2024cerebralveinthrombosis pages 1-2, research2024newrecommendationson pages 2-4)

Key 2023–2024 updates include: (i) guideline caution that **D-dimer should not be used routinely to rule out CVT**, (ii) stronger consensus toward **LMWH in the acute phase** and increasing adoption of **DOACs in the post-acute maintenance phase** for many patients (except selected thrombophilias such as triple-positive APS), and (iii) ongoing uncertainty about **endovascular therapy (EVT)** benefit, with emerging observational evidence that **earlier EVT** in severe CVST may improve functional outcomes—requiring randomized confirmation. (research2024newrecommendationson pages 4-5, research2024newrecommendationson pages 7-8, bucke2024earlyversuslate pages 1-2)

A structured evidence table (identifiers, epidemiology, risks, phenotypes, diagnostics, treatments, outcomes, trials) is embedded below.

| Domain | Key findings for sagittal (superior) sagittal sinus thrombosis within CVT/CVST | Key numbers / practice points | Source URL / date | Citations |
|---|---|---|---|---|
| Identifiers / definition / synonyms | Sagittal sinus thrombosis usually refers to **superior sagittal sinus (SSS) thrombosis**, a subtype/site of **cerebral venous thrombosis (CVT)** or **cerebral venous sinus thrombosis (CVST)** involving the dural venous sinuses. Common synonyms: **superior sagittal sinus thrombosis**, **sagittal sinus thrombosis**, **cerebral venous sinus thrombosis**, **cerebral sinovenous thrombosis**. SSS is among the most commonly involved sinuses and is particularly associated with impaired CSF reabsorption and intracranial hypertension. | CVT accounts for ~0.5–1.0% of all strokes; SSS is frequently involved, often in combination with other sinuses. | German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9; J Clin Med review, Aug 2024: https://doi.org/10.3390/jcm13164730; CNS Neurosci Ther, Mar 2023: https://doi.org/10.1111/cns.14194 | (umurungi2024cerebralveinthrombosis pages 1-2, wei2023intracranialhypertensionafter pages 1-2, research2024newrecommendationson pages 2-4) |
| Epidemiology | CVT is rare but increasingly recognized. Incidence estimates in recent reviews are ~**1–2/100,000/year** in Western Europe; international agenda paper cites **~1.2–1.6/100,000 person-years**. Historical demographic pattern is strong female predominance, especially in reproductive years, though regional cohorts may differ. | Women ~**75%** in guideline summaries; historical female:male ratio ~**3:1** in fertile-age adults. Registry example from India showed median age **29 years** and male predominance (**63.8%**) in that cohort. Mortality in modern series often **<5%**, but broader literature still cites **3–15%**. | Int J Stroke agenda, Apr 2024: https://doi.org/10.1177/17474930241242266; J Clin Med review, Aug 2024: https://doi.org/10.3390/jcm13164730; Sci Rep registry, Jul 2025: https://doi.org/10.1038/s41598-025-07599-x | (aggarwal2025epidemiologyandrisk pages 1-2, umurungi2024cerebralveinthrombosis pages 1-2, coutinho2024reducingtheglobal pages 1-2) |
| Major risk factors | CVT/SSS thrombosis is usually multifactorial; a provoking factor is identifiable in ~**85%**. Major risks include: female sex-specific factors (**combined hormonal contraceptives**, **pregnancy/postpartum**), **thrombophilia**, **local head/neck infection**, **malignancy**, **myeloproliferative neoplasms/JAK2 V617F**, inflammatory/autoimmune disease, trauma/neurosurgery, and rare immune causes such as **vaccine-induced immune thrombotic thrombocytopenia (VITT)** after adenoviral SARS-CoV-2 vaccination. | Approximate frequencies from guideline/reviews: combined hormonal contraceptives in **40–50% of women** with CVT; thrombophilia **34–40%**; pregnancy/postpartum **10–20%**; local infections ~**10%**; JAK2 V617F **6–7%**; myeloproliferative disease **4%**; idiopathic **10–20%**. In patients >55 years, malignancy may account for ~**25%** of cases. | German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9; J Clin Med review, Aug 2024: https://doi.org/10.3390/jcm13164730 | (research2024newrecommendationson pages 2-4, umurungi2024cerebralveinthrombosis pages 2-4) |
| Genetic / molecular predisposition | Important inherited/acquired thrombophilic contributors include **Factor V Leiden (F5)**, **prothrombin G20210A (F2)**, **antithrombin deficiency (SERPINC1)**, **protein C deficiency (PROC)**, **protein S deficiency (PROS1)**, **antiphospholipid syndrome**, and **JAK2 V617F**-positive myeloproliferative neoplasms. Thrombophilia testing is **not recommended routinely for all patients**, but may influence management in selected patients (young, spontaneous, recurrent, or family history-positive cases). | Genetic factors estimated in ~**20–30%** in one registry summary; hereditary thrombophilia independently associated with intracranial hypertension after CVT in one cohort (**OR 2.21**). Triple-positive APS is an exception where **VKA is preferred over DOACs**. | Sci Rep registry, Jul 2025: https://doi.org/10.1038/s41598-025-07599-x; German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9; CNS Neurosci Ther, Mar 2023: https://doi.org/10.1111/cns.14194 | (aggarwal2025epidemiologyandrisk pages 1-2, wei2023intracranialhypertensionafter pages 1-2, research2024newrecommendationson pages 2-4, research2024newrecommendationson pages 7-8) |
| Common presenting symptoms / phenotypes | Presentation is heterogeneous, but dominant syndromes are **intracranial hypertension** (headache, vomiting, papilledema, visual disturbance), **focal syndrome** (motor/sensory deficits, aphasia, hemianopia, focal seizures), and **encephalopathy / reduced consciousness**. SSS thrombosis is especially linked to raised intracranial pressure because of reduced CSF absorption. | Large-series/guideline frequencies: **headache ~87–90%** (some reviews >90%); **seizures 24–40%**; **focal neurological deficits 18–48%**; **depressed consciousness/encephalopathy 18–22%**; **visual loss 13–27%**; **diplopia/cranial neuropathies 11–14%**. One registry found vomiting **39.5%**, headache **29.6%**. | Canadian Best Practice summary, 2024/2025: no DOI shown in retrieved text; J Clin Med review, Aug 2024: https://doi.org/10.3390/jcm13164730; Sci Rep registry, Jul 2025: https://doi.org/10.1038/s41598-025-07599-x | (aggarwal2025epidemiologyandrisk pages 1-2, umurungi2024cerebralveinthrombosis pages 2-4, field2025canadianstrokebest pages 3-4) |
| SSS-specific phenotype associations | SSS involvement is repeatedly associated with **intracranial hypertension** and with **acute symptomatic seizures**, especially when combined with cortical vein thrombosis, hemorrhage, or parenchymal lesions. | Acute symptomatic seizures occurred in **34%** of 1,281 CVT patients; predictors included **SSS thrombosis (aOR 2.0, 95% CI 1.5–2.6)**. Intracranial hypertension cohort: **83.6%** had intracranial hypertension at diagnosis; SSS + right lateral sinus involvement independently associated (**OR 4.115**). | Neurology, Sep 2020: https://doi.org/10.1212/WNL.0000000000010577; CNS Neurosci Ther, Mar 2023: https://doi.org/10.1111/cns.14194 | (wei2023intracranialhypertensionafter pages 1-2, bucke2024earlyversuslate pages 1-2) |
| Key diagnostics / imaging | **Urgent neurovascular imaging** is required. Recommended tests are **contrast-enhanced CT venography (CTV)** or **contrast-enhanced MR venography (MRV)**; isolated non-contrast CT is insufficient, though a hyperdense sinus may suggest the diagnosis. MRI is preferred for **cortical vein thrombosis** and often in younger/pregnant patients; susceptibility-weighted or gradient-echo MRI can help for cortical veins. DSA is reserved for unresolved high-suspicion cases. | Non-contrast CT abnormal in only about **30%**; hyperdense vein/sinus seen in about **one-third** of those cases. CT and MRI with venography are considered broadly equivalent for sinus thrombosis, but MRI is superior for cortical venous thrombosis. | German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9; Canadian Best Practice summary, 2024/2025; J Clin Med review, Aug 2024: https://doi.org/10.3390/jcm13164730 | (research2024newrecommendationson pages 2-4, umurungi2024cerebralveinthrombosis pages 2-4, field2025canadianstrokebest pages 3-4) |
| D-dimer caveat | **D-dimer should not be used routinely to rule out CVT.** It may be considered only in **selected low-probability patients** with isolated headache, no focal deficits, and symptom duration <30 days; a negative result in that narrow context may help defer imaging, but not otherwise. | Guideline position: routine D-dimer exclusion testing **not recommended**. | German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9 | (research2024newrecommendationson pages 2-4) |
| Acute treatment | **Therapeutic-dose heparin is recommended even if intracranial hemorrhage is present.** **LMWH is preferred over UFH** in the acute phase because of practical advantages and lower HIT risk; **UFH** is preferred if surgery/endovascular therapy may be needed or when LMWH is contraindicated (e.g., severe renal failure). Acute care should occur in monitored stroke-unit/ICU settings when severe. | Acute therapy begins with **parenteral anticoagulation**. Standard approach then transitions to oral maintenance anticoagulation. | German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9 | (research2024newrecommendationson pages 5-7, research2024newrecommendationson pages 4-5) |
| Oral maintenance anticoagulation / DOAC vs VKA | After stabilization, patients are switched to oral anticoagulation for a maintenance phase. Recent guideline/review evidence increasingly supports **DOACs as preferred over VKAs** for many patients after the acute phase, except in **triple-positive antiphospholipid syndrome**, where **VKA** is preferred. | 2024 RCT meta-analysis (4 RCTs, **270** participants): any recanalization **78.2% vs 83.2%** (DOAC vs standard care); complete recanalization **60.9% vs 69.4%**; major bleeding **1.2% vs 2.4%**; ICH **1.9% vs 3.6%**; death **0% vs 0.7%**—all differences non-significant. Larger 2024 meta-analysis (25 studies, **2301** patients) found similar mRS 0–2, ICH, mortality, and recanalization between DOACs and warfarin. | Clin Appl Thromb Hemost, Jan 2024: https://doi.org/10.1177/10760296241256360; Health Sci Rep, Feb 2024: https://doi.org/10.1002/hsr2.1869; German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9 | (research2024newrecommendationson pages 5-7, research2024newrecommendationson pages 7-8, chen2024efficacyandsafety pages 3-4, ranjan2024directoralanticoagulants pages 2-5, ranjan2024directoralanticoagulants pages 1-2, chen2024efficacyandsafety pages 1-2) |
| Duration of anticoagulation | Duration is individualized by provoking-factor and recurrence-risk profile. Guideline minimum is **at least 3 months**; usual maintenance phase is **3–12 months**. Therapy should **not** be extended beyond 3–12 months solely to achieve more recanalization. Longer prophylaxis is considered when strong persistent risk factors remain (e.g., cancer, severe thrombophilia, autoimmune disease). | Recanalization occurs in ~**85%**, mostly within the first **3–6 months**, with little additional recanalization after **>12 months**. | German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9 | (research2024newrecommendationson pages 7-8) |
| Pregnancy / breastfeeding / contraception | In pregnancy or postpartum CVT, **therapeutic LMWH** is recommended; **DOACs and VKAs should not be used during pregnancy** because they cross the placenta. Continue anticoagulation until at least **6 weeks postpartum** and for a **total treatment duration ≥3 months**. During breastfeeding, heparins and VKA/fondaparinux are considered acceptable, whereas **DOACs are not recommended**. Women with previous hormone-associated CVT should avoid **combined estrogen-progestin contraception** and prefer **estrogen-free methods**. | Practical prevention note: women with previous CVT and no contraindications should receive **LMWH prophylaxis during pregnancy and for at least 6 weeks postpartum** in the guideline summary. | German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9 | (research2024newrecommendationson pages 2-4, research2024newrecommendationson pages 7-8) |
| Endovascular therapy | **Not routine first-line therapy.** EVT (mechanical thrombectomy ± local thrombolysis) is considered **rescue therapy** in severe CVT/SSS thrombosis for patients who **deteriorate despite adequate anticoagulation**, ideally in experienced neurointerventional centers. Evidence remains limited after the negative/neutral TO-ACT randomized experience. | 2023 severe-CVT cohort: **21/23 procedures (91.3%)** successful recanalization; **18/21** had mRS 0–2 at 6 months; morbidity and mortality each **4.7%**. 2024 multicenter cohort: early EVT (<24 h) vs late EVT showed mRS 0–2 at 3 months **66.7% vs 27.3%**; 90-day mortality **16.7% vs 36.4%** (not statistically significant). | Diagnostics, Jul 2023: https://doi.org/10.3390/diagnostics13132248; Neurocrit Care, Jul 2024: https://doi.org/10.1007/s12028-024-02046-7; German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9 | (research2024newrecommendationson pages 5-7, research2024newrecommendationson pages 4-5, bucke2024earlyversuslate pages 1-2, burns2024endovasculartherapyfor pages 1-2, piano2023endovasculartreatmentof pages 1-2) |
| Decompressive surgery | **Decompressive hemicraniectomy / craniectomy** is recommended in selected patients with CVT plus **parenchymal lesion (congestive edema and/or hemorrhage) and impending herniation/incarceration** to prevent death. | Review summary: about **two-thirds survive**, and about **one-third** are functionally independent at 6 months after decompressive craniectomy for impending herniation. | Curr Opin Neurol, Oct 2025: https://doi.org/10.1097/WCO.0000000000001329; German S2k guideline, Apr 2024: https://doi.org/10.1186/s42466-024-00320-9 | (rosa2025updateonmanagement pages 1-2, research2024newrecommendationson pages 5-7) |
| Prognosis / outcomes | Modern outcomes are generally favorable with early diagnosis and anticoagulation, but residual symptoms are common. Many patients achieve good functional recovery, yet headache, visual symptoms, fatigue, cognitive symptoms, mood symptoms, and reduced work participation remain important long-term burdens. | About **80%** achieve **mRS 0–1** in recent review summaries; international agenda paper cites mortality **3–15%** overall. Registry example: discharge survival ~**97%**, mortality **3.2%**. In patients with intracranial hypertension after CVT, favorable 6-month outcome (mRS 0–2) was **83.67%**, but residual visual impairment occurred in **15.51% vs 4.17%** without intracranial hypertension. | Curr Opin Neurol, Oct 2025: https://doi.org/10.1097/WCO.0000000000001329; Int J Stroke, Apr 2024: https://doi.org/10.1177/17474930241242266; CNS Neurosci Ther, Mar 2023: https://doi.org/10.1111/cns.14194; Sci Rep, Jul 2025: https://doi.org/10.1038/s41598-025-07599-x | (rosa2025updateonmanagement pages 1-2, aggarwal2025epidemiologyandrisk pages 1-2, wei2023intracranialhypertensionafter pages 1-2, coutinho2024reducingtheglobal pages 1-2) |
| Ongoing / recent real-world trials | Current research is testing oral anticoagulant choices and severe-CVT interventions. Examples include randomized trials of **dabigatran vs apixaban** and **dabigatran vs rivaroxaban**, a dedicated venous sinus thrombectomy stent trial, and a planned multicenter trial of **EVT + anticoagulation vs anticoagulation alone**. | Examples: **NCT06551415** dabigatran vs apixaban (Phase 3, n≈200); **NCT06551402** dabigatran vs rivaroxaban (Phase 3, n≈200); **NCT05291585** dedicated venous sinus thrombectomy stent (n=60); **NCT07548346** REVIVE-CVST EVT trial (planned n≈440). | ClinicalTrials.gov records: https://clinicaltrials.gov/study/NCT06551415 ; https://clinicaltrials.gov/study/NCT06551402 ; https://clinicaltrials.gov/study/NCT05291585 ; https://clinicaltrials.gov/study/NCT07548346 | (NCT06551415 chunk 1, NCT06551415 chunk 2, NCT07548346 chunk 1, NCT05291585 chunk 1) |


*Table: This table condenses current evidence and guideline-relevant facts for superior sagittal sinus thrombosis within the broader CVT/CVST spectrum. It is designed to support a knowledge-base entry with identifiers, epidemiology, risk factors, diagnosis, treatment, prognosis, and trial links in one citation-dense artifact.*

## 1. Disease information
### 1.1 What is the disease?
**Cerebral venous thrombosis (CVT)** is thrombosis of the intracranial venous system (dural venous sinuses and/or cerebral veins). **Superior sagittal sinus thrombosis** is a location-specific subtype of CVT/CVST and is often associated with intracranial hypertension due to impaired CSF resorption. (umurungi2024cerebralveinthrombosis pages 1-2, wei2023intracranialhypertensionafter pages 1-2)

**Source types:** The information summarized here is primarily from **aggregated disease-level resources** (e.g., national guideline synthesis and systematic reviews) plus some human clinical cohorts and clinical trial registry entries. (research2024newrecommendationson pages 2-4, chen2024efficacyandsafety pages 3-4, NCT06551415 chunk 1)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
**Limitation:** The full-text sources retrieved in this run did not provide explicit **ICD-10/ICD-11**, **MeSH**, **Orphanet**, **OMIM**, or **MONDO** identifiers for “superior sagittal sinus thrombosis.” Therefore, these identifiers cannot be reliably populated here without direct access to the corresponding ontology databases (not retrieved in-tool in this run). (research2024newrecommendationson pages 2-4)

### 1.3 Synonyms and alternative names
Common clinical synonyms include:
- **Superior sagittal sinus thrombosis (SSS thrombosis)**
- **Sagittal sinus thrombosis**
- **Cerebral venous thrombosis (CVT)** / **cerebral venous sinus thrombosis (CVST)**
- **Cerebral sinovenous thrombosis** (term commonly used in pediatrics)
These terms are used interchangeably in guideline and review sources discussing dural sinus thrombosis. (umurungi2024cerebralveinthrombosis pages 1-2, research2024newrecommendationson pages 2-4)

## 2. Etiology
### 2.1 Disease causal factors (mechanistic, environmental, infectious)
CVT/SSS thrombosis is generally **multifactorial**; a prothrombotic risk factor is identifiable in ~85% of cases in a 2024 DOAC-focused review. (umurungi2024cerebralveinthrombosis pages 1-2)

Major etiologic categories include:
- **Hormonal and pregnancy-related** hypercoagulability (combined hormonal contraceptives; pregnancy/puerperium). (research2024newrecommendationson pages 2-4, umurungi2024cerebralveinthrombosis pages 2-4)
- **Thrombophilia** (inherited or acquired). (research2024newrecommendationson pages 2-4, research2024newrecommendationson pages 7-8)
- **Inflammation/infection**, especially head/neck infections in a subset. (research2024newrecommendationson pages 2-4, umurungi2024cerebralveinthrombosis pages 2-4)
- **Cancer and hematologic disorders**, including myeloproliferative neoplasms (JAK2 V617F). (research2024newrecommendationson pages 2-4, umurungi2024cerebralveinthrombosis pages 2-4)
- **Immune-mediated prothrombotic syndromes**, notably **vaccine-induced immune thrombotic thrombocytopenia (VITT)** after adenoviral SARS‑CoV‑2 vaccination, recognized in guideline updates. (research2024newrecommendationson pages 2-4)

### 2.2 Risk factors
Recent guideline-derived approximate frequencies for CVT risk contexts include: female sex (~75%), combined hormonal contraceptives (40–50% of women with CVT), thrombophilia (34–40%), pregnancy/postpartum (10–20%), local head/neck infections (~10%), JAK2 V617F (6–7%), myeloproliferative disease (4%), and idiopathic (10–20%). (research2024newrecommendationson pages 2-4)

A registry-based cohort (India, July 2022–Oct 2023 recruitment) illustrates region-specific heterogeneity: median age 29 years, male predominance in that cohort, and alcohol consumption associated with higher odds of CVST (OR 1.95). (aggarwal2025epidemiologyandrisk pages 1-2)

### 2.3 Protective factors
**Limitation:** The retrieved sources did not provide evidence for specific genetic or environmental **protective factors** for CVT/SSS thrombosis; this remains unpopulated from the current evidence set.

### 2.4 Gene–environment interactions
Clinically, strong gene–environment interactions are implied where thrombophilia co-occurs with hormonal/pregnancy risks and other prothrombotic exposures; however, the retrieved sources did not provide explicit quantitative interaction models.

## 3. Phenotypes
### 3.1 Common phenotypes and clinical presentation
Guideline-level prevalence estimates for presenting features include headache (~87–90%), seizures (24–40%), focal neurologic deficits (18–48%), depressed consciousness/encephalopathy (18–22%), visual loss (13–27%), and diplopia/cranial neuropathies (11–14%). (field2025canadianstrokebest pages 3-4)

A 2024 review emphasizes that presentations typically cluster into:
- **Intracranial hypertension syndrome** (headache, vomiting, papilledema, visual disturbance)
- **Focal syndrome** (motor/sensory deficits, aphasia, hemianopia, focal seizures)
- **Encephalopathy** (multifocal deficits, altered consciousness)
and notes headache occurs in >90% in many series. (umurungi2024cerebralveinthrombosis pages 2-4)

### 3.2 SSS-associated phenotype patterns
SSS involvement is repeatedly linked to intracranial hypertension and seizure risk. In a 2023 cohort of 293 CVT survivors, 83.6% had intracranial hypertension at diagnosis (opening pressure ≥250 mmH2O), and thrombosis involving SSS plus lateral sinus strongly associated with intracranial hypertension (OR 4.115). (wei2023intracranialhypertensionafter pages 1-2)

### 3.3 Phenotype ontology suggestions (HPO)
(ontology suggestions; not asserted as sourced frequencies)
- Headache: **HP:0002315**
- Nausea/Vomiting: **HP:0002013** / **HP:0002017**
- Papilledema: **HP:0001085**
- Visual impairment: **HP:0000505**; Visual field defect: **HP:0001123**
- Seizure: **HP:0001250**
- Focal neurological deficit / hemiparesis: **HP:0001263** / **HP:0002302**
- Altered mental status / impaired consciousness: **HP:0001254**

### 3.4 Quality of life impact
The 2024 international research agenda highlights high prevalence of long-term sequelae (fatigue, headache, depression, cognitive deficits) and prioritizes PROMs and standardized long-term outcome sets, underscoring substantial post-CVT quality-of-life burden even when functional outcome scales are favorable. (coutinho2024reducingtheglobal pages 4-6, coutinho2024reducingtheglobal pages 2-4)

## 4. Genetic / molecular information
### 4.1 Causal genes and susceptibility genes
CVT is not classically monogenic, but inherited thrombophilia genes are clinically relevant contributors and may guide duration/type of anticoagulation in selected cases. (research2024newrecommendationson pages 2-4, research2024newrecommendationson pages 7-8)

Key genes/conditions highlighted across guideline and summaries include:
- **F5** (Factor V Leiden)
- **F2** (prothrombin G20210A)
- **SERPINC1** (antithrombin deficiency)
- **PROC** (protein C deficiency)
- **PROS1** (protein S deficiency)
- **JAK2** (V617F; myeloproliferative neoplasms)
- **Antiphospholipid syndrome (APS)** (acquired thrombophilia; “triple-positive APS” affects anticoagulant choice)
These are explicitly listed as common thrombophilic risks in recent guideline/review summaries. (research2024newrecommendationson pages 2-4, field2025canadianstrokebest pages 3-4, research2024newrecommendationson pages 7-8)

### 4.2 Variant classes / somatic vs germline
The retrieved sources did not provide variant-level nomenclature, allele frequencies in gnomAD, or ClinVar classifications. JAK2 V617F is typically a somatic driver mutation in myeloproliferative neoplasms, but explicit variant annotations were not provided in the retrieved text.

### 4.3 Epigenetics / chromosomal abnormalities
Not available in the retrieved evidence.

## 5. Environmental information
Key non-genetic contributors include hormonal exposures (estrogen-containing contraceptives), pregnancy/postpartum physiology, infections (including head/neck infections and COVID-19-related contexts), obesity, trauma/neurosurgery, and some medications that increase thrombosis risk. (umurungi2024cerebralveinthrombosis pages 2-4)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (systems-level)
A consistent mechanistic chain across contemporary sources is:
1) **Venous sinus/vein occlusion** (thrombus) →
2) **Venous outflow obstruction and venous hypertension** →
3) **Impaired CSF absorption** (notably when SSS is involved) leading to **intracranial hypertension** →
4) **Secondary parenchymal injury** (edema/venous infarction and/or hemorrhage) and neurological symptoms (headache, focal deficits, seizures, encephalopathy). (umurungi2024cerebralveinthrombosis pages 1-2, wei2023intracranialhypertensionafter pages 1-2)

### 6.2 Suggested pathway/process ontology terms
(ontology suggestions; not asserted as uniquely CVT-specific)
- GO biological processes: **blood coagulation**, **platelet activation**, **fibrin clot formation**, **inflammatory response**, **response to hypoxia**, **regulation of vascular permeability**, **leukocyte adhesion**.
- Cell Ontology (CL) candidates: **endothelial cell**, **platelet**, **neutrophil**, **monocyte/macrophage**, **astrocyte** (secondary injury), **microglia**.

### 6.3 Knowledge gaps (expert consensus)
The 2024 international CVT research agenda identifies major gaps in: CVT-specific thrombosis mechanisms (vs other venous beds), inflammatory contributors to tissue injury, genetic susceptibility beyond limited known signals, biomarkers, and determination of which subgroups benefit from EVT and optimized device design for venous sinuses. (coutinho2024reducingtheglobal pages 2-4, coutinho2024reducingtheglobal pages 8-9, coutinho2024reducingtheglobal pages 6-7)

## 7. Anatomical structures affected
### 7.1 Organ/system level
Primary system: **central nervous system**; primary structures: **dural venous sinuses** and **cerebral veins**, especially the **superior sagittal sinus** in this disease entry. (wei2023intracranialhypertensionafter pages 1-2)

Ontology suggestions:
- UBERON: **dural venous sinus**, **superior sagittal sinus**, **brain**, **meninges**.

### 7.2 Tissue/cell level
Key tissue compartments include venous endothelium and surrounding brain parenchyma affected by venous hypertension and edema/hemorrhage. (wei2023intracranialhypertensionafter pages 1-2)

## 8. Temporal development
CVT can have insidious onset; the Canadian summary notes less than half present within 48 hours, differing from typical arterial stroke. (field2025canadianstrokebest pages 3-4)

## 9. Inheritance and population
### 9.1 Epidemiology
Recent sources cite incidence around ~1–2 per 100,000 per year in Western Europe, and the 2024 international agenda cites ~1.2–1.6/100,000 person-years. (umurungi2024cerebralveinthrombosis pages 1-2, coutinho2024reducingtheglobal pages 1-2)

### 9.2 Population demographics
Historically, women predominate (≈75% in guideline summaries), driven in part by estrogen-related risks; however, regional cohorts can differ (e.g., one India registry showed male predominance). (aggarwal2025epidemiologyandrisk pages 1-2, research2024newrecommendationson pages 2-4)

## 10. Diagnostics
### 10.1 Imaging
Guideline and best-practice sources emphasize urgent neurovascular imaging:
- **Contrast-enhanced CTV** or **contrast-enhanced MRV** for diagnosis; isolated non-contrast CT is insufficient. (field2025canadianstrokebest pages 3-4)
- MRI is superior to CT for cortical venous thrombosis; CT and MRI with venography are otherwise broadly equivalent. (research2024newrecommendationson pages 2-4)

### 10.2 D-dimer
The 2024 German S2k summary states **routine D-dimer testing to rule out CVT cannot be recommended**, with only a narrow low-probability scenario where a negative D-dimer might justify omitting imaging. (research2024newrecommendationson pages 2-4)

### 10.3 Laboratory / thrombophilia testing
The guideline summary indicates thrombophilia screening is not universally recommended but may be considered when it will change management (e.g., young patients, spontaneous CVT, recurrent thrombosis, or positive family history). (research2024newrecommendationson pages 2-4)

## 11. Outcome / prognosis
Outcomes are often favorable with anticoagulation, but residual symptoms are common. A modern review reports ~80% achieve excellent functional outcome (mRS 0–1), yet persistent symptoms may affect return to work and quality of life. (rosa2025updateonmanagement pages 1-2)

Intracranial hypertension can be highly prevalent at diagnosis and is associated with higher risk of residual visual impairment at follow-up (15.51% vs 4.17% in one cohort). (wei2023intracranialhypertensionafter pages 1-2)

## 12. Treatment
### 12.1 Standard-of-care anticoagulation (real-world implementation)
The 2024 German guideline summary recommends:
- **Therapeutic-dose heparin in acute CVT even with intracranial hemorrhage**.
- Prefer **LMWH over UFH** unless impending surgery/EVT or contraindications (e.g., renal failure) favor UFH. (research2024newrecommendationson pages 4-5)

A treatment-phase schematic in the German guideline (Figure 1) summarizes the initial, maintenance, and secondary prophylaxis phases. (research2024newrecommendationson media 59ded2f2)

### 12.2 Oral maintenance: DOACs vs VKA (2023–2024 evidence)
In a 2024 meta-analysis of 4 RCTs (n=270), DOACs and standard care had similar recanalization and safety outcomes (e.g., any recanalization 78.2% vs 83.2%; major bleeding 1.2% vs 2.4%; ICH 1.9% vs 3.6%; death 0% vs 0.7%). (chen2024efficacyandsafety pages 3-4)

A broader 2024 meta-analysis (25 studies; 2301 patients) found comparable functional recovery (mRS 0–2), ICH, mortality, and recanalization between DOACs and warfarin. (ranjan2024directoralanticoagulants pages 2-5)

The German guideline summary states DOACs should be preferred over VKA for oral anticoagulation in many CVT patients, except **triple-positive APS** (VKA preferred) and pregnancy/breastfeeding contexts. (research2024newrecommendationson pages 5-7, research2024newrecommendationson pages 7-8)

### 12.3 Duration
The 2024 German guideline summary recommends anticoagulation for **at least 3 months**, with typical maintenance 3–12 months, and not to prolong treatment solely to improve recanalization. (research2024newrecommendationson pages 7-8)

### 12.4 Endovascular therapy (EVT)
Guideline consensus: EVT is not routine first-line therapy; it may be considered individually for deterioration despite adequate anticoagulation, and local thrombolysis carries higher bleeding without proven outcome improvement. (research2024newrecommendationson pages 5-7)

Recent real-world data:
- 2023 severe CVT EVT series: successful recanalization 91.3% and mRS 0–2 at 6 months in 18/21, with 4.7% morbidity and 4.7% mortality. (piano2023endovasculartreatmentof pages 1-2)
- 2024 multicenter observational study: early EVT (<24 h) associated with higher 3‑month functional independence than late EVT (66.7% vs 27.3%). (bucke2024earlyversuslate pages 1-2)
A 2024 commentary highlights that evidence remains uncertain and calls for randomized trials of “early EVT” strategies. (burns2024endovasculartherapyfor pages 1-2)

### 12.5 Decompressive surgery
Decompressive hemicraniectomy is recommended in selected patients with parenchymal lesions and impending herniation to prevent death. (research2024newrecommendationson pages 5-7)

### 12.6 Treatment ontology suggestions (MAXO)
(ontology suggestions)
- Therapeutic anticoagulation (heparin/LMWH): **MAXO: anticoagulant therapy**
- Venous thrombectomy / endovascular thrombectomy: **MAXO: thrombectomy**
- Decompressive craniectomy: **MAXO: decompressive craniectomy**
- Management of intracranial hypertension (e.g., acetazolamide in practice; evidence gaps noted): **MAXO: intracranial pressure management**

## 13. Prevention
Guideline-derived prevention points include:
- Avoid estrogen-containing combined contraceptives after hormone-associated CVT; prefer estrogen-free methods. (research2024newrecommendationson pages 7-8)
- In pregnancy/postpartum with prior CVT (without contraindication), LMWH prophylaxis during pregnancy and for at least 6 weeks postpartum is recommended in the German guideline summary. (research2024newrecommendationson pages 7-8)

## 14. Other species / natural disease
Not available in the retrieved evidence.

## 15. Model organisms
Not available in the retrieved evidence.

## Recent developments and current applications (2023–2024 emphasis)
1) **German consensus-based S2k guideline (Apr 2024)** updated recommendations spanning diagnosis, anticoagulation choice, DOAC caveats, pregnancy/breastfeeding, and selective thrombophilia evaluation; it explicitly discourages routine D-dimer exclusion. https://doi.org/10.1186/s42466-024-00320-9 (research2024newrecommendationson pages 2-4, research2024newrecommendationson pages 7-8)

2) **DOAC evidence consolidation (Jan–Feb 2024)** via meta-analyses indicates DOACs are broadly comparable to warfarin/standard care for recanalization, bleeding, and mortality outcomes, supporting increasing real-world adoption post-acute phase. https://doi.org/10.1177/10760296241256360 ; https://doi.org/10.1002/hsr2.1869 (chen2024efficacyandsafety pages 3-4, ranjan2024directoralanticoagulants pages 2-5)

3) **Severe CVST EVT timing hypothesis (Jul 2024)**: observational data suggest earlier EVT may associate with better functional independence, but commentary stresses major confounding risks and calls for prospective trials. https://doi.org/10.1007/s12028-024-02046-7 ; https://doi.org/10.1007/s12028-024-02045-8 (bucke2024earlyversuslate pages 1-2, burns2024endovasculartherapyfor pages 1-2)

4) **Global expert research agenda (Apr 2024)**: prioritizes long-term follow-up cohorts, improved diagnostic tools (including potential clinical-score + D-dimer strategies), trials for DOAC dosing/duration, and defining EVT candidates and devices optimized for venous sinuses. https://doi.org/10.1177/17474930241242266 (coutinho2024reducingtheglobal pages 2-4, coutinho2024reducingtheglobal pages 6-7)

## Ongoing trials / real-world implementations (examples)
- **NCT06551415** (ClinicalTrials.gov; posted 2021; recruiting): Phase 3 RCT dabigatran 150 mg bid vs apixaban 5 mg bid for 6 months; primary endpoint partial/complete recanalization at Day 180. https://clinicaltrials.gov/study/NCT06551415 (NCT06551415 chunk 1)
- **NCT07548346 (REVIVE-CVST)** (ClinicalTrials.gov; 2026; not yet recruiting): randomized PROBE EVT + anticoagulation vs anticoagulation alone in severe CVST; EVT within 24h. https://clinicaltrials.gov/study/NCT07548346 (NCT07548346 chunk 1)
- **NCT05291585** (ClinicalTrials.gov; 2022; completed): randomized device trial of a dedicated venous sinus thrombectomy stent vs balloon thrombectomy. https://clinicaltrials.gov/study/NCT05291585 (NCT05291585 chunk 1)

## Direct abstract quotes supporting key claims
- German S2k guideline abstract: “**D-dimer testing to rule out CVT cannot be recommended and should therefore not be routinely performed.**” (Neurological Research and Practice; accepted 20 Mar 2024) (research2024newrecommendationson pages 2-4)
- German S2k guideline abstract: “**Patients with CVT should preferably be treated with low molecular weight heparine (LMWH) instead of unfractionated heparine in the acute phase.**” (research2024newrecommendationson pages 2-4)
- German S2k guideline abstract: “**Following the acute phase, oral anticoagulation with direct oral anticoagulants instead of vitamin K antagonists should be given for 3 to 12 months** …” (research2024newrecommendationson pages 2-4)
- DOAC RCT meta-analysis abstract (Jan 2024): “**DOACs and standard of care showed similar efficacy and safety profiles for the treatment of CVT.**” (chen2024efficacyandsafety pages 1-2)

## Notes and limitations for knowledge-base population
- **PMID requirement:** The retrieved evidence in this run is primarily identified by **DOI and journal metadata**; PMIDs were not provided in the tool outputs, so PMID-level citation cannot be guaranteed here.
- **Ontology IDs (MONDO/MeSH/ICD/Orphanet/OMIM):** Not retrieved from ontology databases in this run; should be populated by direct ontology queries.
- **Molecular profiling / multi-omics / animal models:** Not available in the accessed texts; likely requires targeted searches in GEO/PRIDE and preclinical thrombosis models.


References

1. (umurungi2024cerebralveinthrombosis pages 1-2): Johanna Umurungi, Francesca Ferrando, Daniela Cilloni, and Piera Sivera. Cerebral vein thrombosis and direct oral anticoagulants: a review. Journal of Clinical Medicine, 13:4730, Aug 2024. URL: https://doi.org/10.3390/jcm13164730, doi:10.3390/jcm13164730. This article has 4 citations.

2. (research2024newrecommendationson pages 2-4): Neurological Research, C. Weimar, J. Beyer-Westendorf, FO Bohmann, G. Hahn, S. Halimeh, S. Holzhauer, C. Kalka, M. Knoflach, H-C Koennecke, F. Masuhr, M-L Mono, U. Nowak-Göttl, E. Scherret, M. Schlamann, and B. Linnemann. New recommendations on cerebral venous and dural sinus thrombosis from the german consensus-based (s2k) guideline. Neurological Research and Practice, Apr 2024. URL: https://doi.org/10.1186/s42466-024-00320-9, doi:10.1186/s42466-024-00320-9. This article has 29 citations and is from a peer-reviewed journal.

3. (research2024newrecommendationson pages 4-5): Neurological Research, C. Weimar, J. Beyer-Westendorf, FO Bohmann, G. Hahn, S. Halimeh, S. Holzhauer, C. Kalka, M. Knoflach, H-C Koennecke, F. Masuhr, M-L Mono, U. Nowak-Göttl, E. Scherret, M. Schlamann, and B. Linnemann. New recommendations on cerebral venous and dural sinus thrombosis from the german consensus-based (s2k) guideline. Neurological Research and Practice, Apr 2024. URL: https://doi.org/10.1186/s42466-024-00320-9, doi:10.1186/s42466-024-00320-9. This article has 29 citations and is from a peer-reviewed journal.

4. (research2024newrecommendationson pages 7-8): Neurological Research, C. Weimar, J. Beyer-Westendorf, FO Bohmann, G. Hahn, S. Halimeh, S. Holzhauer, C. Kalka, M. Knoflach, H-C Koennecke, F. Masuhr, M-L Mono, U. Nowak-Göttl, E. Scherret, M. Schlamann, and B. Linnemann. New recommendations on cerebral venous and dural sinus thrombosis from the german consensus-based (s2k) guideline. Neurological Research and Practice, Apr 2024. URL: https://doi.org/10.1186/s42466-024-00320-9, doi:10.1186/s42466-024-00320-9. This article has 29 citations and is from a peer-reviewed journal.

5. (bucke2024earlyversuslate pages 1-2): Philipp Bücke, Hans Henkes, Johannes Kaesmacher, Mirjam R. Heldner, Adrian Scutelnic, Marcel Arnold, Thomas R. Meinel, Alexandru Cimpoca, Thomas Horvath, Elina Henkes, Hansjörg Bäzner, and Victoria Hellstern. Early versus late initiation of endovascular therapy in patients with severe cerebral venous sinus thrombosis. Neurocritical Care, 41:1047-1054, Jul 2024. URL: https://doi.org/10.1007/s12028-024-02046-7, doi:10.1007/s12028-024-02046-7. This article has 7 citations and is from a peer-reviewed journal.

6. (wei2023intracranialhypertensionafter pages 1-2): Huimin Wei, Huimin Jiang, Yifan Zhou, Lu Liu, Chen Zhou, and Xunming Ji. Intracranial hypertension after cerebral venous thrombosis—risk factors and outcomes. CNS Neuroscience & Therapeutics, 29:2540-2547, Mar 2023. URL: https://doi.org/10.1111/cns.14194, doi:10.1111/cns.14194. This article has 30 citations and is from a peer-reviewed journal.

7. (aggarwal2025epidemiologyandrisk pages 1-2): S. Aggarwal, Arun Kumar, Vishal Deo, Bhupen Bipin P. Chandan Kumar Ray Girish Baburao M. Iadar Barman Kulkarni Mohapatra Kulkarni Hemachandren Ti, Bhupen Barman, Bipin P. Kulkarni, Chandan Kumar Ray Mohapatra, Girish Baburao Kulkarni, M. Hemachandren, Iadarilang Tiewsoh, J. Gnanaraj, Karthik Vishwanathan, Narendra Kumar, Vikas Bhatia, Rakesh Yadav, K. S. Lakshmi, Syed Mudasir Qadri, and Heena Tabassum. Epidemiology and risk factors for cerebral venous sinus thrombosis: insights from leading centres in the i-regved registry, india. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-07599-x, doi:10.1038/s41598-025-07599-x. This article has 2 citations and is from a peer-reviewed journal.

8. (coutinho2024reducingtheglobal pages 1-2): Jonathan M Coutinho, Anita van de Munckhof, Diana Aguiar de Sousa, Sven Poli, Sanjith Aaron, Antonio Arauz, Adriana B Conforto, Katarzyna Krzywicka, Sini Hiltunen, Erik Lindgren, Mayte Sánchez van Kammen, Liqi Shu, Tamam Bakchoul, Rosalie Belder, René van den Berg, Elisheva Boumans, Suzanne Cannegieter, Vanessa Cano-Nigenda, Thalia S Field, Isabel Fragata, Mirjam R Heldner, María Hernández-Pérez, Frederikus A Klok, Ronen R Leker, Lia Lucas-Neto, Jeremy Molad, Thanh N Nguyen, Dirk-Jan Saaltink, Gustavo Saposnik, Pankaj Sharma, Jan Stam, Vincent Thijs, Michiel van der Vaart, David J Werring, Diana Wong Ramos, Shadi Yaghi, Nilüfer Yeşilot, Turgut Tatlisumak, Jukka Putaala, Katarina Jood, Marcel Arnold, and José M Ferro. Reducing the global burden of cerebral venous thrombosis: an international research agenda. International Journal of Stroke, 19:599-610, Apr 2024. URL: https://doi.org/10.1177/17474930241242266, doi:10.1177/17474930241242266. This article has 27 citations and is from a peer-reviewed journal.

9. (umurungi2024cerebralveinthrombosis pages 2-4): Johanna Umurungi, Francesca Ferrando, Daniela Cilloni, and Piera Sivera. Cerebral vein thrombosis and direct oral anticoagulants: a review. Journal of Clinical Medicine, 13:4730, Aug 2024. URL: https://doi.org/10.3390/jcm13164730, doi:10.3390/jcm13164730. This article has 4 citations.

10. (field2025canadianstrokebest pages 3-4): TS Field, MP Lindsay, T Wein, and DB Debicki. Canadian stroke best practice recommendations: cerebral venous thrombosis, 2024. Unknown journal, 2025.

11. (research2024newrecommendationson pages 5-7): Neurological Research, C. Weimar, J. Beyer-Westendorf, FO Bohmann, G. Hahn, S. Halimeh, S. Holzhauer, C. Kalka, M. Knoflach, H-C Koennecke, F. Masuhr, M-L Mono, U. Nowak-Göttl, E. Scherret, M. Schlamann, and B. Linnemann. New recommendations on cerebral venous and dural sinus thrombosis from the german consensus-based (s2k) guideline. Neurological Research and Practice, Apr 2024. URL: https://doi.org/10.1186/s42466-024-00320-9, doi:10.1186/s42466-024-00320-9. This article has 29 citations and is from a peer-reviewed journal.

12. (chen2024efficacyandsafety pages 3-4): Xi Chen, Linjuan Guo, and Meiming Lin. Efficacy and safety of direct oral anticoagulants in cerebral venous thrombosis: meta-analysis of randomized clinical trials. Clinical and Applied Thrombosis/Hemostasis, Jan 2024. URL: https://doi.org/10.1177/10760296241256360, doi:10.1177/10760296241256360. This article has 8 citations.

13. (ranjan2024directoralanticoagulants pages 2-5): Redoy Ranjan, Gie Ken‐Dror, and Pankaj Sharma. Direct oral anticoagulants compared to warfarin in long‐term management of cerebral venous thrombosis: a comprehensive meta‐analysis. Health Science Reports, Feb 2024. URL: https://doi.org/10.1002/hsr2.1869, doi:10.1002/hsr2.1869. This article has 15 citations and is from a peer-reviewed journal.

14. (ranjan2024directoralanticoagulants pages 1-2): Redoy Ranjan, Gie Ken‐Dror, and Pankaj Sharma. Direct oral anticoagulants compared to warfarin in long‐term management of cerebral venous thrombosis: a comprehensive meta‐analysis. Health Science Reports, Feb 2024. URL: https://doi.org/10.1002/hsr2.1869, doi:10.1002/hsr2.1869. This article has 15 citations and is from a peer-reviewed journal.

15. (chen2024efficacyandsafety pages 1-2): Xi Chen, Linjuan Guo, and Meiming Lin. Efficacy and safety of direct oral anticoagulants in cerebral venous thrombosis: meta-analysis of randomized clinical trials. Clinical and Applied Thrombosis/Hemostasis, Jan 2024. URL: https://doi.org/10.1177/10760296241256360, doi:10.1177/10760296241256360. This article has 8 citations.

16. (burns2024endovasculartherapyfor pages 1-2): Joseph D. Burns and Emanuele Orru. Endovascular therapy for severe cerebral venous sinus thrombosis: time is vein? Neurocritical care, 41:728-729, Jul 2024. URL: https://doi.org/10.1007/s12028-024-02045-8, doi:10.1007/s12028-024-02045-8. This article has 2 citations and is from a peer-reviewed journal.

17. (piano2023endovasculartreatmentof pages 1-2): Mariangela Piano, Andrea Romi, Amedeo Cervo, Antonella Gatti, Antonio Macera, Guglielmo Pero, Cristina Motto, Elio Clemente Agostoni, and Emilio Lozupone. Endovascular treatment of cerebral vein thrombosis: safety and effectiveness in the thrombectomy era. Diagnostics, 13:2248, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132248, doi:10.3390/diagnostics13132248. This article has 4 citations.

18. (rosa2025updateonmanagement pages 1-2): Sara Rosa, Isabel Fragata, and Diana Aguiar de Sousa. Update on management of cerebral venous thrombosis. Current Opinion in Neurology, 38:18-28, Oct 2025. URL: https://doi.org/10.1097/wco.0000000000001329, doi:10.1097/wco.0000000000001329. This article has 15 citations and is from a peer-reviewed journal.

19. (NCT06551415 chunk 1): Mohamed G. zeinhom, MD. Dabigatran Versus Apixaban in Cerebral Venous Thrombosis. Kafrelsheikh University. 2021. ClinicalTrials.gov Identifier: NCT06551415

20. (NCT06551415 chunk 2): Mohamed G. zeinhom, MD. Dabigatran Versus Apixaban in Cerebral Venous Thrombosis. Kafrelsheikh University. 2021. ClinicalTrials.gov Identifier: NCT06551415

21. (NCT07548346 chunk 1): Ossama Mansour. MENA Regional Endovascular Intervention for Venous Cerebral Venous Sinus Thrombosis. Middle East North Africa Stroke and Interventional Neurotherapies Organization. 2026. ClinicalTrials.gov Identifier: NCT07548346

22. (NCT05291585 chunk 1): Ji Xunming,MD,PhD. The Dedicated Venous Sinus Thrombectomy Stent for Endovascular Treatment of Cerebral Venous Sinus Thrombosis.. Ji Xunming,MD,PhD. 2022. ClinicalTrials.gov Identifier: NCT05291585

23. (coutinho2024reducingtheglobal pages 4-6): Jonathan M Coutinho, Anita van de Munckhof, Diana Aguiar de Sousa, Sven Poli, Sanjith Aaron, Antonio Arauz, Adriana B Conforto, Katarzyna Krzywicka, Sini Hiltunen, Erik Lindgren, Mayte Sánchez van Kammen, Liqi Shu, Tamam Bakchoul, Rosalie Belder, René van den Berg, Elisheva Boumans, Suzanne Cannegieter, Vanessa Cano-Nigenda, Thalia S Field, Isabel Fragata, Mirjam R Heldner, María Hernández-Pérez, Frederikus A Klok, Ronen R Leker, Lia Lucas-Neto, Jeremy Molad, Thanh N Nguyen, Dirk-Jan Saaltink, Gustavo Saposnik, Pankaj Sharma, Jan Stam, Vincent Thijs, Michiel van der Vaart, David J Werring, Diana Wong Ramos, Shadi Yaghi, Nilüfer Yeşilot, Turgut Tatlisumak, Jukka Putaala, Katarina Jood, Marcel Arnold, and José M Ferro. Reducing the global burden of cerebral venous thrombosis: an international research agenda. International Journal of Stroke, 19:599-610, Apr 2024. URL: https://doi.org/10.1177/17474930241242266, doi:10.1177/17474930241242266. This article has 27 citations and is from a peer-reviewed journal.

24. (coutinho2024reducingtheglobal pages 2-4): Jonathan M Coutinho, Anita van de Munckhof, Diana Aguiar de Sousa, Sven Poli, Sanjith Aaron, Antonio Arauz, Adriana B Conforto, Katarzyna Krzywicka, Sini Hiltunen, Erik Lindgren, Mayte Sánchez van Kammen, Liqi Shu, Tamam Bakchoul, Rosalie Belder, René van den Berg, Elisheva Boumans, Suzanne Cannegieter, Vanessa Cano-Nigenda, Thalia S Field, Isabel Fragata, Mirjam R Heldner, María Hernández-Pérez, Frederikus A Klok, Ronen R Leker, Lia Lucas-Neto, Jeremy Molad, Thanh N Nguyen, Dirk-Jan Saaltink, Gustavo Saposnik, Pankaj Sharma, Jan Stam, Vincent Thijs, Michiel van der Vaart, David J Werring, Diana Wong Ramos, Shadi Yaghi, Nilüfer Yeşilot, Turgut Tatlisumak, Jukka Putaala, Katarina Jood, Marcel Arnold, and José M Ferro. Reducing the global burden of cerebral venous thrombosis: an international research agenda. International Journal of Stroke, 19:599-610, Apr 2024. URL: https://doi.org/10.1177/17474930241242266, doi:10.1177/17474930241242266. This article has 27 citations and is from a peer-reviewed journal.

25. (coutinho2024reducingtheglobal pages 8-9): Jonathan M Coutinho, Anita van de Munckhof, Diana Aguiar de Sousa, Sven Poli, Sanjith Aaron, Antonio Arauz, Adriana B Conforto, Katarzyna Krzywicka, Sini Hiltunen, Erik Lindgren, Mayte Sánchez van Kammen, Liqi Shu, Tamam Bakchoul, Rosalie Belder, René van den Berg, Elisheva Boumans, Suzanne Cannegieter, Vanessa Cano-Nigenda, Thalia S Field, Isabel Fragata, Mirjam R Heldner, María Hernández-Pérez, Frederikus A Klok, Ronen R Leker, Lia Lucas-Neto, Jeremy Molad, Thanh N Nguyen, Dirk-Jan Saaltink, Gustavo Saposnik, Pankaj Sharma, Jan Stam, Vincent Thijs, Michiel van der Vaart, David J Werring, Diana Wong Ramos, Shadi Yaghi, Nilüfer Yeşilot, Turgut Tatlisumak, Jukka Putaala, Katarina Jood, Marcel Arnold, and José M Ferro. Reducing the global burden of cerebral venous thrombosis: an international research agenda. International Journal of Stroke, 19:599-610, Apr 2024. URL: https://doi.org/10.1177/17474930241242266, doi:10.1177/17474930241242266. This article has 27 citations and is from a peer-reviewed journal.

26. (coutinho2024reducingtheglobal pages 6-7): Jonathan M Coutinho, Anita van de Munckhof, Diana Aguiar de Sousa, Sven Poli, Sanjith Aaron, Antonio Arauz, Adriana B Conforto, Katarzyna Krzywicka, Sini Hiltunen, Erik Lindgren, Mayte Sánchez van Kammen, Liqi Shu, Tamam Bakchoul, Rosalie Belder, René van den Berg, Elisheva Boumans, Suzanne Cannegieter, Vanessa Cano-Nigenda, Thalia S Field, Isabel Fragata, Mirjam R Heldner, María Hernández-Pérez, Frederikus A Klok, Ronen R Leker, Lia Lucas-Neto, Jeremy Molad, Thanh N Nguyen, Dirk-Jan Saaltink, Gustavo Saposnik, Pankaj Sharma, Jan Stam, Vincent Thijs, Michiel van der Vaart, David J Werring, Diana Wong Ramos, Shadi Yaghi, Nilüfer Yeşilot, Turgut Tatlisumak, Jukka Putaala, Katarina Jood, Marcel Arnold, and José M Ferro. Reducing the global burden of cerebral venous thrombosis: an international research agenda. International Journal of Stroke, 19:599-610, Apr 2024. URL: https://doi.org/10.1177/17474930241242266, doi:10.1177/17474930241242266. This article has 27 citations and is from a peer-reviewed journal.

27. (research2024newrecommendationson media 59ded2f2): Neurological Research, C. Weimar, J. Beyer-Westendorf, FO Bohmann, G. Hahn, S. Halimeh, S. Holzhauer, C. Kalka, M. Knoflach, H-C Koennecke, F. Masuhr, M-L Mono, U. Nowak-Göttl, E. Scherret, M. Schlamann, and B. Linnemann. New recommendations on cerebral venous and dural sinus thrombosis from the german consensus-based (s2k) guideline. Neurological Research and Practice, Apr 2024. URL: https://doi.org/10.1186/s42466-024-00320-9, doi:10.1186/s42466-024-00320-9. This article has 29 citations and is from a peer-reviewed journal.