---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T11:13:40.315476'
end_time: '2026-05-10T11:24:56.960893'
duration_seconds: 676.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inherited Porphyria
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inherited Porphyria
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Inherited Porphyria** covering all of the
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
- **Disease Name:** Inherited Porphyria
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Inherited Porphyria** covering all of the
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


# Inherited Porphyria — Disease Characteristics Research Report (2023–2024 priority)

## Target disease
**Disease name (umbrella):** Inherited porphyrias (group of Mendelian inborn errors of heme biosynthesis; includes acute hepatic and erythropoietic/cutaneous subtypes). (dickey2024updateonthe pages 1-3)

**Note on scope:** “Inherited porphyria” is not a single disease entity but a family of disorders caused by defects at different enzymatic steps in the heme biosynthetic pathway; therefore, the knowledge-base entry typically needs a parent concept (“porphyrias”) plus child subtype entities (e.g., AIP, VP, HCP, ADP, EPP, XLP, CEP). (dickey2024updateonthe pages 1-3, dickey2024updateonthe pages 3-5)

**Key knowledge-base identifiers (requested):** OMIM numbers for several subtypes are present in retrieved evidence (e.g., AIP OMIM #176000; EPP OMIM 177000; XLP OMIM 300752). However, **MONDO / Orphanet / ICD-10 / ICD-11 / MeSH identifiers were not retrieved in the current evidence set** and therefore cannot be cited here without additional retrieval. (belosevic2023firstreportof pages 1-2, annaelisabeth2023afamelanotideisassociated pages 2-3)

**Information source type:** The evidence used here is derived primarily from **aggregated disease-level resources** (recent authoritative reviews) plus **human clinical trial/real-world cohort studies** for modern therapies; there is also limited evidence from **single-patient case/genetics reports** (e.g., mosaic HMBS variant). (dickey2024updateonthe pages 1-3, sardh2024longtermfollowupof pages 7-10, kubisch2024germanrealworldexperience pages 1-2, belosevic2023firstreportof pages 1-2)

---

## 1. Disease information (overview, concepts, definitions)

### Definition and classification (current understanding)
Porphyrias are “rare disorders caused by enzymatic defects in heme synthesis” and can be classified by **primary site of intermediate accumulation** (hepatic vs erythropoietic) and clinically as **acute hepatic porphyrias (AHP)** versus **cutaneous porphyrias** (including blistering vs nonblistering photosensitivity phenotypes). (dickey2024updateonthe pages 1-3)

**Major inherited subtypes explicitly listed in 2024 review evidence:** AIP, VP, HCP, ADP, EPP, XLP, PCT, CEP. (dickey2024updateonthe pages 1-3)

**Visual summary:** A heme-biosynthesis pathway diagram linking each enzymatic step to the corresponding porphyria subtype is available in the retrieved evidence. (dickey2024updateonthe media 522948f9)

### Synonyms / alternative names
- **Acute hepatic porphyrias (AHP)**: includes **AIP, VP, HCP, ADP**. (dickey2024updateonthe pages 1-3)
- **Protoporphyrias**: **EPP** and **XLP**. (madigan2023illuminatingdersimelagona pages 2-3, leaf2024afamelanotidefortreatment pages 1-2)

---

## 2. Etiology (causal factors, triggers, risk/protective factors, G×E)

### Primary causal factors (genetic / mechanistic)
Inherited porphyrias arise from pathogenic variants affecting enzymes of the heme biosynthetic pathway; for AHP, “pathogenic variants in 1 of 4 enzymes of heme synthesis are necessary” with attacks requiring induction of hepatic **ALAS1** (rate-limiting step in liver). (dickey2024givosiranatargeted pages 4-5)

**AHP causal genes (2024 review):**
- **AIP:** HMBS (hydroxymethylbilane synthase) (dickey2024updateonthe pages 1-3)
- **VP:** PPOX (protoporphyrinogen oxidase) (dickey2024updateonthe pages 1-3)
- **HCP:** CPOX (coproporphyrinogen oxidase) (dickey2024updateonthe pages 1-3)
- **ADP:** ALAD (aminolevulinate dehydratase) (dickey2024updateonthe pages 1-3)

**Erythropoietic protoporphyria / X-linked protoporphyria:**
- **EPP:** FECH deficiency (ferrochelatase, final step) (madigan2023illuminatingdersimelagona pages 2-3)
- **XLP:** ALAS2 gain-of-function (erythroid ALAS2) (madigan2023illuminatingdersimelagona pages 2-3)

### Environmental/physiologic triggers (risk factors for attack expression)
Acute attacks in AHP relate to induction of hepatic ALAS1 and accumulation of neurotoxic precursors **ALA** and **PBG**, and are triggered by stressors including “stress, alcohol, smoking, medications, caloric restriction/fasting, acute illnesses, and the luteal menstrual phase.” (dickey2024updateonthe pages 3-5)

A case-based genetics report similarly lists triggers including “drugs metabolised via the cytochrome P450 pathway, exogenous and endogenous hormones, stress, and reduced carbohydrate intake.” (belosevic2023firstreportof pages 1-2)

### Genetic modifiers / penetrance modifiers (recent developments)
AIP is widely recognized as **autosomal dominant with low penetrance** and high heterogeneity. (lei2024acuteintermittentporphyria pages 1-2)

Recent (2023–2024) evidence supports multiple modifier axes:
- **Mitochondrial biogenesis / mtDNA copy number:** A 2023 human study measured mtDNA copy number in blood (34 AIP vs 37 controls) and reported all AIP patients had low mitochondrial count; “mtDNA copy number per cell and mitochondrial biogenesis seem to play a role in either inhibiting or promoting disease expression,” and are proposed as biomarkers. (pierro2023mitochondrialdnacopy pages 1-2)
- **Oligogenic/modifier genes:** A 2024 review highlights candidate modifier loci including CYP2D6 (some alleles potentially protective via reduced sensitivity to porphyrogenic metabolites), **PEPT2** variants linked to differences in renal failure severity/neurotoxicity via altered ALA handling, and other genes (AGRN, DOK7, SCN4A, PPARA). (lei2024acuteintermittentporphyria pages 2-3, lei2024acuteintermittentporphyria pages 4-5)
- **Somatic mosaicism:** 2023 report describes a de novo low-frequency mosaic HMBS pathogenic variant (c.77G>A p.Arg26His at ~22% allele fraction) causing AIP, detectable only via long-read sequencing when routine testing was negative. (belosevic2023firstreportof pages 1-2)

### Protective factors
Protective genetic variants are not established in the retrieved clinical evidence set, but the modifier-gene literature suggests some alleles may reduce sensitivity to porphyrogenic metabolites (e.g., selected CYP2D6 alleles) and thereby lower risk of symptomatic expression. (lei2024acuteintermittentporphyria pages 2-3)

---

## 3. Phenotypes (clinical manifestations, onset, frequency, QoL)

### Acute hepatic porphyrias (AHP; especially AIP)
**Core clinical phenotype:** acute neurovisceral attacks (often abdominal pain with nausea/vomiting) with neurologic/autonomic features; diagnostic delay is common. (dickey2024updateonthe pages 3-5)

**Attack-associated biochemical phenotype:** elevated urinary ALA and PBG during symptomatic episodes. (dickey2024updateonthe pages 3-5, belosevic2023firstreportof pages 1-2)

**Onset/temporal pattern:** attacks typically after puberty and are episodic, precipitated by triggers. (belosevic2023firstreportof pages 1-2)

**Long-term complications (AHP/AIP):** chronic pain, neuropathy, liver and kidney disease; one 2024 review notes chronic kidney disease occurs in “about 60% of symptomatic AIP.” (dickey2024updateonthe pages 5-6)

**Suggested HPO terms (non-exhaustive; based on symptoms explicitly mentioned in retrieved evidence):**
- Abdominal pain (HP:0002027) (dickey2024updateonthe pages 5-6)
- Nausea (HP:0002018) (dickey2024updateonthe pages 5-6)
- Vomiting (HP:0002013) (dickey2024updateonthe pages 3-5)
- Peripheral neuropathy (HP:0009830) (dickey2024updateonthe pages 5-6)
- Autonomic dysfunction (HP:0002459) (dickey2024updateonthe pages 5-6)
- Hyponatremia (HP:0002902) (belosevic2023firstreportof pages 1-2)
- Psychiatric symptoms (HP:0000708) (belosevic2023firstreportof pages 1-2)

### Protoporphyrias (EPP/XLP)
**Core phenotype:** severe cutaneous phototoxicity; EPP described as “painful phototoxic burn injuries after short exposure times to visible light.” (barmanaksozen2023qualityadjustedlifeyears pages 1-2)

**QoL impact:** large, measurable QoL improvements are seen with afamelanotide therapy in real-world cohorts (see Treatment). (leaf2024afamelanotidefortreatment pages 2-5)

**Suggested HPO terms:**
- Photosensitivity (HP:0000992)
- Cutaneous pain (HP:0000989)
- Erythromelalgia-like pain after sun exposure (phenotypic description; closest HPO often Photosensitivity + Pain)

### Congenital erythropoietic porphyria (CEP)
Clinical features noted include fluorescent erythrodontia, red fluorescent urine, corneal ulcers, thrombocytopenia, and transfusion-dependent anemia; severity ranges from hydrops fetalis to adult-onset mild photosensitivity. (dickey2024updateonthe pages 10-11)

**Suggested HPO terms:**
- Hemolytic anemia / anemia (HP:0001903)
- Thrombocytopenia (HP:0001873)
- Photosensitivity (HP:0000992)
- Corneal ulceration (HP:0000481)

---

## 4. Genetic / molecular information

### Causal genes and inheritance patterns (from retrieved evidence)
See table artifact below and the pathway figure. Acute hepatic porphyrias include AD low-penetrance diseases (AIP/VP/HCP) and ultrarare recessive ADP. (dickey2024updateonthe pages 1-3, dickey2024updateonthe pages 3-5)

**AIP genetics details:** AIP is caused by HMBS pathogenic variants (many reported) with very low population penetrance (~1% of heterozygotes symptomatic reported in the mtDNA-copy-number paper’s background). (pierro2023mitochondrialdnacopy pages 1-2)

**Variant-type examples and diagnostic-edge cases (2023–2024):**
- **Somatic mosaic HMBS variant** c.77G>A p.(Arg26His) at ~22% allele fraction, requiring long-read sequencing to detect. (belosevic2023firstreportof pages 1-2)

### Modifier genes (selected)
Proposed modifiers include CYP2D6 alleles and PEPT2 variants, with potential effects on xenobiotic metabolism and ALA handling, respectively. (lei2024acuteintermittentporphyria pages 2-3, lei2024acuteintermittentporphyria pages 4-5)

### Epigenetic / chromosomal abnormality evidence
Not identified in retrieved sources.

---

## 5. Environmental information

**Key non-genetic contributors (attack precipitants):** fasting/caloric restriction, alcohol, smoking, acute illness, medications (porphyrinogenic/CYP450-related), and hormonal cycling (luteal phase/progesterone effects). (dickey2024updateonthe pages 3-5, belosevic2023firstreportof pages 1-2)

---

## 6. Mechanism / pathophysiology

### Core biochemical mechanism (causal chain)
**Upstream trigger:** induction of hepatic **ALAS1** (rate-limiting heme synthesis enzyme in liver) by physiologic/environmental stimuli. (dickey2024updateonthe pages 3-5, dickey2024givosiranatargeted pages 4-5)

**Primary defect:** inherited partial deficiency in a downstream heme biosynthesis enzyme (e.g., HMBS in AIP). (dickey2024updateonthe pages 1-3)

**Downstream accumulation:** increased intermediates including **ALA** and **PBG** (especially in AHP), with ALA “particularly toxic” and implicated as neurotoxic. (dickey2024updateonthe pages 3-5, kubisch2024germanrealworldexperience pages 1-2)

**Clinical manifestations:** neurovisceral attacks with pain, autonomic and neurologic complications, and chronic organ sequelae (kidney/liver). (dickey2024updateonthe pages 5-6, dickey2024updateonthe pages 3-5)

### Photosensitivity mechanism in protoporphyrias (high level)
In EPP/XLP, excess **protoporphyrin IX** accumulates, driving painful photosensitivity and, in a minority, hepatobiliary complications due to elimination of excess PPIX. (annaelisabeth2023afamelanotideisassociated pages 2-3)

### Ontology suggestions
**GO biological process (examples):**
- heme biosynthetic process (GO:0006783)
- porphyrin-containing compound metabolic process (GO:0006778)

**Cell Ontology (examples):**
- hepatocyte (CL:0000182) for hepatic ALAS1-driven AHP mechanisms
- erythroblast / erythroid progenitor (e.g., erythroblast CL:0000765) for ALAS2/FECH context in protoporphyrias

**UBERON (examples):**
- liver (UBERON:0002107)
- skin of body (UBERON:0002097)

**CHEBI (examples):**
- δ-aminolevulinic acid (CHEBI:13772)
- porphobilinogen (CHEBI:15508)
- protoporphyrin IX (CHEBI:15439)

(These ontology IDs are standard terms; specific mapping was not provided in the retrieved papers.)

---

## 7. Anatomical structures affected

**Primary organs (by subtype grouping):**
- **Acute hepatic porphyrias:** liver as the key metabolic source of precursor overproduction; secondary complications include kidney disease and neurologic system involvement. (dickey2024updateonthe pages 3-5, dickey2024updateonthe pages 5-6)
- **Protoporphyrias (EPP/XLP):** skin (phototoxicity) and liver (subset with cholestatic damage/liver failure). (barmanaksozen2023qualityadjustedlifeyears pages 1-2, annaelisabeth2023afamelanotideisassociated pages 1-2)

---

## 8. Temporal development

**AHP (AIP):** episodic acute attacks precipitated by triggers; low penetrance means many carriers remain asymptomatic. (dickey2024updateonthe pages 3-5, lei2024acuteintermittentporphyria pages 1-2)

**Protoporphyrias:** chronic photosensitivity with acute painful reactions after short visible light exposure. (barmanaksozen2023qualityadjustedlifeyears pages 1-2)

---

## 9. Inheritance and population

### Epidemiology (selected quantitative estimates from retrieved evidence)
- **AIP prevalence:** ~0.5–2 per 100,000 clinically (review) (dickey2024updateonthe pages 3-5)
- **Carrier frequency of HMBS pathogenic variants:** ~1:1,700 reported in genetic datasets, implying **overall penetrance <1%** in the general population, but higher (10–20%) among relatives of symptomatic patients. (dickey2024updateonthe pages 3-5)
- **AIP population prevalence estimate (another 2024 review):** 5–10 cases per 100,000; acute attacks in <1% of at-risk individuals. (lei2024acuteintermittentporphyria pages 1-2)

- **EPP prevalence:** ~1:100,000 (reported in 2023 QoL feasibility study and 2023 liver-protection study). (barmanaksozen2023qualityadjustedlifeyears pages 1-2, annaelisabeth2023afamelanotideisassociated pages 1-2)

### Penetrance/expressivity
- **AIP penetrance heterogeneity:** genotype-dependent penetrance described, with population penetrance ~0.5–1% vs family penetrance higher; null HMBS alleles associated with higher penetrance/severity than missense alleles. (lei2024acuteintermittentporphyria pages 3-4, lei2024acuteintermittentporphyria pages 2-3)

---

## 10. Diagnostics

### Biochemical testing (first-line in symptomatic patients)
A 2024 review emphasizes that **spot urine ALA and PBG normalized to creatinine** are key for diagnosing acute attacks; urine porphyrins alone are nonspecific; stool and plasma porphyrins help with VP/HCP and cutaneous presentations. Testing should be obtained during attacks because PBG can normalize between episodes. (dickey2024updateonthe pages 3-5)

A recent diagnostic-recommendations review (2025) reinforces that clinical features alone are insufficient, and diagnosis in symptomatic patients requires biochemical demonstration of characteristic heme precursor/porphyrin patterns; it warns that genomic sequencing should not be used as initial screening without biochemical evidence in symptomatic patients. (aarsand2025practicalrecommendationsfor pages 1-2)

### Genetic testing
Genetic testing is recommended to confirm subtype and test at-risk relatives; enzyme assays may have overlapping ranges and limited usefulness. (dickey2024updateonthe pages 5-6, dickey2024updateonthe pages 3-5)

**Advanced sequencing in edge cases:** somatic mosaicism can evade Sanger sequencing; long-read sequencing can detect low-level mosaic HMBS variants. (belosevic2023firstreportof pages 1-2)

### Protoporphyria diagnostics
EPP/XLP diagnosis begins with total erythrocyte protoporphyrin; metal-free fraction is typically >90% in EPP and 50–85% in XLP; plasma alone is not recommended; plasma fluorescence emission peak at 634 nm supports EPP/XLP. (madigan2023illuminatingdersimelagona pages 2-3)

---

## 11. Outcome / prognosis

**AHP/AIP chronic morbidity:** chronic kidney disease is reported in “about 60% of symptomatic AIP” in a 2024 review, consistent with significant long-term morbidity burden. (dickey2024updateonthe pages 5-6)

**EPP liver outcomes:** ~20% of EPP patients have disturbed liver function and ~4% progress to terminal liver failure from hepatobiliary elimination of excess PPIX. (annaelisabeth2023afamelanotideisassociated pages 1-2)

(Quantitative survival curves and mortality rates were not present in the retrieved evidence set.)

---

## 12. Treatment (current practice, recent developments 2023–2024, real-world implementation)

### Acute hepatic porphyrias / AIP
**Trigger avoidance:** avoidance of unsafe medications, fasting, alcohol, tobacco is emphasized as foundational management. (dickey2024updateonthe pages 5-6)

**Acute attacks:** intravenous **hemin** (example dosing given in review: 3–4 mg/kg daily for 4 days) plus supportive care (analgesia, antiemetics, electrolyte monitoring). (dickey2024updateonthe pages 5-6)

**RNAi disease-modifying therapy — givosiran (ALAS1-targeting):**
- Mechanism: inhibits hepatic ALAS1 to reduce ALA/PBG accumulation. (dickey2024givosiranatargeted pages 4-5)
- **Phase 1/2 open-label extension (48 months; Orphanet J Rare Dis; Oct 2024; URL https://doi.org/10.1186/s13023-024-03284-w):** annualized attack rates and hemin use reduced by **97% and 96%**; median urinary **ALA −95%** and **PBG −98%** at month 48; QoL improved (EQ-VAS +15.8 points; EQ-5D-5L +0.04). (sardh2024longtermfollowupof pages 7-10, sardh2024longtermfollowupof pages 10-12, sardh2024longtermfollowupof pages 1-2)
- **Real-world cohort (Germany; J Clin Med; Nov 2024; URL https://doi.org/10.3390/jcm13226779):** historical AAR 2.9 reduced to **0.45** on givosiran (p<0.01); 75% symptom improvement; biochemical response with ALA <2×ULN in all and PBG <2×ULN in 60% at 6 months. (kubisch2024germanrealworldexperience pages 1-2)
- Safety signals summarized in 2024 hematology review (URL https://doi.org/10.1182/hematology.2024000663): injection-site reactions and nausea; ALT >3×ULN in 15% vs 2% placebo; abnormal renal function ~15% vs 7% placebo; elevated homocysteine 16% in trial summary. (dickey2024givosiranatargeted pages 4-5)
- Additional real-world safety observations (Germany): fatigue leading to discontinuation in some; decreased renal function 30.7%, hepatic enzyme elevations, and homocysteinemia observed in all patients in that cohort excerpt. (kubisch2024germanrealworldexperience pages 12-14)

**MAXO suggestions (examples):**
- Intravenous hemin therapy (MAXO: medical intervention concept; specific ID not retrieved)
- RNA interference therapy (givosiran) (MAXO concept; ID not retrieved)

### Protoporphyrias (EPP/XLP)
**Afamelanotide (α-MSH analogue; implant):**
- **US cohort (Life; May 2024; URL https://doi.org/10.3390/life14060689):** median time to phototoxic symptom onset improved from **12.5 min** to **120 min** (p<0.0001) in those receiving ≥2 implants; disease-specific QoL (EPP-QoL) improved from 27.8 to 75 (p=0.00067); no improvement in liver biochemistries in that cohort despite clinical benefit. (leaf2024afamelanotidefortreatment pages 2-5)
- **QoL feasibility (IJERPH; Mar 2023; URL https://doi.org/10.3390/ijerph20075296):** reports EPP prevalence ~1:100,000 and that EQ-5D under long-term afamelanotide was “comparable to the age-matched population norm.” (barmanaksozen2023qualityadjustedlifeyears pages 1-2)
- **Liver-protection observational evidence (Life; Apr 2023; URL https://doi.org/10.3390/life13041066):** dose-dependent associations between more frequent dosing (more implants in prior 365 days) and lower ALAT and bilirubin; supports potential hepatoprotective effect signals in EPP. (annaelisabeth2023afamelanotideisassociated pages 1-2)

**Emerging therapy — dersimelagon (oral MC1R agonist):** a 2023 review summarizes phase 2 evidence of clinically meaningful and statistically significant benefit with acceptable safety/efficacy profile for EPP/XLP. (madigan2023illuminatingdersimelagona pages 2-3)

**MAXO suggestions (examples):**
- Subcutaneous drug implantation (afamelanotide implant) (MAXO concept; ID not retrieved)
- Photoprotection / sunlight avoidance (MAXO concept; ID not retrieved)

### CEP
Bone marrow transplantation is described as curative in transfusion-dependent or disfiguring disease. (dickey2024updateonthe pages 10-11)

---

## 13. Prevention

**Primary prevention (genetic risk cannot be prevented, but attacks can be prevented):** avoidance of known triggers (unsafe medications, fasting/caloric restriction, alcohol/tobacco; management of hormonal triggers). (dickey2024updateonthe pages 5-6, dickey2024updateonthe pages 3-5)

**Secondary prevention:** family screening with genetic testing for at-risk relatives after biochemical/genetic confirmation in index case. (dickey2024updateonthe pages 5-6, dickey2024updateonthe pages 3-5)

**Tertiary prevention:** long-term suppression of attacks (e.g., givosiran in appropriate patients) and monitoring/management of renal/hepatic complications. (dickey2024givosiranatargeted pages 4-5, kubisch2024germanrealworldexperience pages 12-14)

---

## 14. Other species / natural disease
Not identified in the retrieved evidence set.

---

## 15. Model organisms
Not identified in the retrieved evidence set.

---

## High-value recent resources used (with publication dates and URLs)
- Dickey AK, Leaf RK, Balwani M. **Update on the porphyrias.** *Annual Review of Medicine* (Jan 2024). https://doi.org/10.1146/annurev-med-042921-123602 (dickey2024updateonthe pages 1-3, dickey2024updateonthe pages 3-5)
- Sardh E, et al. **Long-term follow-up of givosiran… 48-month OLE.** *Orphanet Journal of Rare Diseases* (Oct 2024). https://doi.org/10.1186/s13023-024-03284-w (sardh2024longtermfollowupof pages 7-10)
- Kubisch I, et al. **German real-world experience… givosiran.** *Journal of Clinical Medicine* (Nov 2024). https://doi.org/10.3390/jcm13226779 (kubisch2024germanrealworldexperience pages 1-2)
- Leaf RK, et al. **Afamelanotide… US cohort.** *Life* (May 2024). https://doi.org/10.3390/life14060689 (leaf2024afamelanotidefortreatment pages 2-5)
- Lei JJ, et al. **AIP low penetrance/high heterogeneity (modifier genes).** *Frontiers in Genetics* (Aug 2024). https://doi.org/10.3389/fgene.2024.1374965 (lei2024acuteintermittentporphyria pages 1-2)
- Di Pierro E, et al. **mtDNA copy number drives penetrance.** *Life* (Sep 2023). https://doi.org/10.3390/life13091923 (pierro2023mitochondrialdnacopy pages 1-2)

---

## Summary table of major inherited subtypes
| Clinical category | Subtype | Causal gene and enzyme/step | Inheritance | Key diagnostic biochemical markers | Current disease-modifying therapies highlighted in 2023–2024 evidence |
|---|---|---|---|---|---|
| Acute hepatic | AIP | **HMBS**; hydroxymethylbilane synthase, 3rd enzyme of heme biosynthesis | AD, low penetrance | Spot urine **ALA** and **PBG** normalized to creatinine; elevated urinary ALA/PBG during attacks; urine porphyrins alone nonspecific | Acute treatment with **IV hemin** and glucose/carbohydrate support; prevention with **givosiran** for AHP/AIP; trigger avoidance (dickey2024updateonthe pages 1-3, dickey2024updateonthe pages 3-5, dickey2024givosiranatargeted pages 4-5, sardh2024longtermfollowupof pages 7-10) |
| Acute hepatic | VP | **PPOX**; protoporphyrinogen oxidase | AD, low penetrance | Urine ALA/PBG in attacks; **stool and plasma porphyrins** aid diagnosis; can have cutaneous photosensitivity | Hemin/glucose for acute attacks in AHP framework; **givosiran approved for AHP**; subtype-specific quantitative VP treatment data not in retrieved evidence (dickey2024updateonthe pages 1-3, dickey2024updateonthe pages 3-5, dickey2024updateonthe pages 5-6) |
| Acute hepatic | HCP | **CPOX**; coproporphyrinogen oxidase | AD, low penetrance | Urine ALA/PBG in attacks; **stool and plasma porphyrins** aid diagnosis; may show cutaneous photosensitivity | Hemin/glucose for acute attacks in AHP framework; **givosiran approved for AHP**; subtype-specific HCP outcome data not in retrieved evidence (dickey2024updateonthe pages 1-3, dickey2024updateonthe pages 3-5, dickey2024updateonthe pages 5-6) |
| Acute hepatic | ADP | **ALAD**; aminolevulinate dehydratase | AR (ultrarare) | Urine ALA/PBG mentioned within AHP diagnostic framework; subtype-specific marker pattern not in retrieved evidence | Not in retrieved evidence beyond general AHP management context (dickey2024updateonthe pages 1-3, dickey2024updateonthe pages 3-5) |
| Cutaneous / erythropoietic | EPP | **FECH**; ferrochelatase, final enzyme in heme biosynthesis | AR | **Total erythrocyte protoporphyrin** elevated; **metal-free erythrocyte protoporphyrin >90%** typical; plasma may be normal or increased; plasma fluorescence peak at **634 nm** supports diagnosis | **Afamelanotide** approved; large QoL/light-tolerance benefit in 2024 US cohort; **dersimelagon** emerging oral therapy; liver transplant discussed for severe liver failure risk in background evidence (madigan2023illuminatingdersimelagona pages 2-3, leaf2024afamelanotidefortreatment pages 2-5, leaf2024afamelanotidefortreatment pages 1-2, barmanaksozen2023qualityadjustedlifeyears pages 1-2, annaelisabeth2023afamelanotideisassociated pages 1-2) |
| Cutaneous / erythropoietic | XLP | **ALAS2** gain-of-function; erythroid-specific first/rate-controlling step | X-linked | **Total erythrocyte protoporphyrin** elevated; **metal-free fraction 50–85%** typical; plasma fluorescence peak at **634 nm** supports diagnosis | **Afamelanotide** used for protoporphyrias in 2024 cohort (1 XLP patient included); **dersimelagon** emerging for EPP/XLP (madigan2023illuminatingdersimelagona pages 2-3, leaf2024afamelanotidefortreatment pages 2-5, leaf2024afamelanotidefortreatment pages 1-2) |
| Cutaneous / erythropoietic | CEP | **UROS**; uroporphyrinogen III synthase | Not in retrieved evidence | Not in retrieved evidence for specific biochemical markers in gathered excerpts | Supportive photoprotection; **bone marrow transplantation** described as curative for transfusion-dependent or disfiguring disease; phlebotomy in selected non-anemic patients; ciclopirox trial planned (dickey2024updateonthe pages 10-11) |


*Table: This table summarizes the major inherited porphyria subtypes discussed in the gathered evidence, linking each disorder to its causal gene, inheritance, key biochemical diagnostic markers, and therapies emphasized in 2023–2024 sources. It is useful as a quick disease-knowledge-base scaffold across acute hepatic and erythropoietic/cutaneous porphyrias.*

---

## Notes on evidence gaps vs requested template fields
1) **Ontology/registry identifiers (MONDO, Orphanet, ICD-10/ICD-11, MeSH)** were not retrievable from the current evidence set; the report therefore limits itself to OMIM identifiers that were explicitly present in the retrieved texts. (belosevic2023firstreportof pages 1-2, annaelisabeth2023afamelanotideisassociated pages 2-3)
2) **Animal models, model organism databases, and cross-species natural disease** were not identified in the retrieved evidence set.
3) Where HPO/GO/CL/UBERON/CHEBI/MAXO terms are suggested, they are standard ontology terms; the retrieved evidence did not provide ontology IDs directly.

---

## Figure
A pathway figure showing heme biosynthesis steps, subcellular localization (mitochondrial vs cytosolic), and porphyria subtype mapping is available from the 2024 Annual Review of Medicine article. (dickey2024updateonthe media 522948f9)

References

1. (dickey2024updateonthe pages 1-3): Amy K. Dickey, Rebecca Karp Leaf, and Manisha Balwani. Update on the porphyrias. Annual Review of Medicine, 75:321-335, Jan 2024. URL: https://doi.org/10.1146/annurev-med-042921-123602, doi:10.1146/annurev-med-042921-123602. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (dickey2024updateonthe pages 3-5): Amy K. Dickey, Rebecca Karp Leaf, and Manisha Balwani. Update on the porphyrias. Annual Review of Medicine, 75:321-335, Jan 2024. URL: https://doi.org/10.1146/annurev-med-042921-123602, doi:10.1146/annurev-med-042921-123602. This article has 47 citations and is from a domain leading peer-reviewed journal.

3. (belosevic2023firstreportof pages 1-2): Adrian Belosevic, Anna-Elisabeth Minder, Morgan Gueuning, Franziska van Breemen, Gian Andri Thun, Maja P. Mattle-Greminger, Stefan Meyer, Alessandra Baumer, Elisabeth I. Minder, Xiaoye Schneider-Yin, and Jasmin Barman-Aksözen. First report of a low-frequency mosaic mutation in the hydroxymethylbilane synthase gene causing acute intermittent porphyria. Life, 13:1889, Sep 2023. URL: https://doi.org/10.3390/life13091889, doi:10.3390/life13091889. This article has 1 citations.

4. (annaelisabeth2023afamelanotideisassociated pages 2-3): Anna-Elisabeth Minder, Xiaoye Schneider-Yin, Henryk Zulewski, Christoph E. Minder, and Elisabeth I. Minder. Afamelanotide is associated with dose-dependent protective effect from liver damage related to erythropoietic protoporphyria. Life, Apr 2023. URL: https://doi.org/10.3390/life13041066, doi:10.3390/life13041066. This article has 8 citations.

5. (sardh2024longtermfollowupof pages 7-10): Eliane Sardh, Manisha Balwani, David C. Rees, Karl E. Anderson, Gang Jia, Marianne T. Sweetser, and Bruce Wang. Long-term follow-up of givosiran treatment in patients with acute intermittent porphyria from a phase 1/2, 48-month open-label extension study. Orphanet Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1186/s13023-024-03284-w, doi:10.1186/s13023-024-03284-w. This article has 11 citations and is from a peer-reviewed journal.

6. (kubisch2024germanrealworldexperience pages 1-2): Ilja Kubisch, Nils Wohmann, Thaddäus Till Wissniowski, Thomas Stauch, Lucienne Oettel, Eva Diehl-Wiesenecker, Rajan Somasundaram, and Ulrich Stölzel. German real-world experience of patients with diverse features of acute intermittent porphyria treated with givosiran. Journal of Clinical Medicine, 13:6779, Nov 2024. URL: https://doi.org/10.3390/jcm13226779, doi:10.3390/jcm13226779. This article has 9 citations.

7. (dickey2024updateonthe media 522948f9): Amy K. Dickey, Rebecca Karp Leaf, and Manisha Balwani. Update on the porphyrias. Annual Review of Medicine, 75:321-335, Jan 2024. URL: https://doi.org/10.1146/annurev-med-042921-123602, doi:10.1146/annurev-med-042921-123602. This article has 47 citations and is from a domain leading peer-reviewed journal.

8. (madigan2023illuminatingdersimelagona pages 2-3): Katelyn E. Madigan, Sean R. Rudnick, Matthew A. Agnew, Numra Urooj, and Herbert L. Bonkovsky. Illuminating dersimelagon: a novel agent in the treatment of erythropoietic protoporphyria and x-linked protoporphyria. Pharmaceuticals, 17:31, Dec 2023. URL: https://doi.org/10.3390/ph17010031, doi:10.3390/ph17010031. This article has 7 citations.

9. (leaf2024afamelanotidefortreatment pages 1-2): Rebecca K. Leaf, Hetanshi Naik, Paul Y. Jiang, Sarina B. Elmariah, Pamela Hodges, Jennifer Mead, John Trinidad, Behnam Saberi, Benny Tran, Sarah Valiante, Francesca Mernick, David E. Leaf, Karl E. Anderson, and Amy K. Dickey. Afamelanotide for treatment of the protoporphyrias: impact on quality of life and laboratory parameters in a us cohort. Life, 14:689, May 2024. URL: https://doi.org/10.3390/life14060689, doi:10.3390/life14060689. This article has 8 citations.

10. (dickey2024givosiranatargeted pages 4-5): Amy K. Dickey and Rebecca K. Leaf. Givosiran: a targeted treatment for acute intermittent porphyria. Hematology, 2024:426-433, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000663, doi:10.1182/hematology.2024000663. This article has 12 citations and is from a peer-reviewed journal.

11. (lei2024acuteintermittentporphyria pages 1-2): Jia-Jia Lei, Shuang Li, Bai-Xue Dong, Jing Yang, and Yi Ren. Acute intermittent porphyria: a disease with low penetrance and high heterogeneity. Frontiers in Genetics, Aug 2024. URL: https://doi.org/10.3389/fgene.2024.1374965, doi:10.3389/fgene.2024.1374965. This article has 8 citations and is from a peer-reviewed journal.

12. (pierro2023mitochondrialdnacopy pages 1-2): Elena Di Pierro, Miriana Perrone, Milena Franco, Francesca Granata, Lorena Duca, Debora Lattuada, Giacomo De Luca, and Giovanna Graziadei. Mitochondrial dna copy number drives the penetrance of acute intermittent porphyria. Life, 13:1923, Sep 2023. URL: https://doi.org/10.3390/life13091923, doi:10.3390/life13091923. This article has 6 citations.

13. (lei2024acuteintermittentporphyria pages 2-3): Jia-Jia Lei, Shuang Li, Bai-Xue Dong, Jing Yang, and Yi Ren. Acute intermittent porphyria: a disease with low penetrance and high heterogeneity. Frontiers in Genetics, Aug 2024. URL: https://doi.org/10.3389/fgene.2024.1374965, doi:10.3389/fgene.2024.1374965. This article has 8 citations and is from a peer-reviewed journal.

14. (lei2024acuteintermittentporphyria pages 4-5): Jia-Jia Lei, Shuang Li, Bai-Xue Dong, Jing Yang, and Yi Ren. Acute intermittent porphyria: a disease with low penetrance and high heterogeneity. Frontiers in Genetics, Aug 2024. URL: https://doi.org/10.3389/fgene.2024.1374965, doi:10.3389/fgene.2024.1374965. This article has 8 citations and is from a peer-reviewed journal.

15. (dickey2024updateonthe pages 5-6): Amy K. Dickey, Rebecca Karp Leaf, and Manisha Balwani. Update on the porphyrias. Annual Review of Medicine, 75:321-335, Jan 2024. URL: https://doi.org/10.1146/annurev-med-042921-123602, doi:10.1146/annurev-med-042921-123602. This article has 47 citations and is from a domain leading peer-reviewed journal.

16. (barmanaksozen2023qualityadjustedlifeyears pages 1-2): Jasmin Barman-Aksözen, Anna-Elisabeth Minder, Francesca Granata, Mårten Pettersson, Cornelia Dechant, Mehmet Hakan Aksözen, and Rocco Falchetto. Quality-adjusted life years in erythropoietic protoporphyria and other rare diseases: a patient-initiated eq-5d feasibility study. International Journal of Environmental Research and Public Health, 20:5296, Mar 2023. URL: https://doi.org/10.3390/ijerph20075296, doi:10.3390/ijerph20075296. This article has 8 citations.

17. (leaf2024afamelanotidefortreatment pages 2-5): Rebecca K. Leaf, Hetanshi Naik, Paul Y. Jiang, Sarina B. Elmariah, Pamela Hodges, Jennifer Mead, John Trinidad, Behnam Saberi, Benny Tran, Sarah Valiante, Francesca Mernick, David E. Leaf, Karl E. Anderson, and Amy K. Dickey. Afamelanotide for treatment of the protoporphyrias: impact on quality of life and laboratory parameters in a us cohort. Life, 14:689, May 2024. URL: https://doi.org/10.3390/life14060689, doi:10.3390/life14060689. This article has 8 citations.

18. (dickey2024updateonthe pages 10-11): Amy K. Dickey, Rebecca Karp Leaf, and Manisha Balwani. Update on the porphyrias. Annual Review of Medicine, 75:321-335, Jan 2024. URL: https://doi.org/10.1146/annurev-med-042921-123602, doi:10.1146/annurev-med-042921-123602. This article has 47 citations and is from a domain leading peer-reviewed journal.

19. (annaelisabeth2023afamelanotideisassociated pages 1-2): Anna-Elisabeth Minder, Xiaoye Schneider-Yin, Henryk Zulewski, Christoph E. Minder, and Elisabeth I. Minder. Afamelanotide is associated with dose-dependent protective effect from liver damage related to erythropoietic protoporphyria. Life, Apr 2023. URL: https://doi.org/10.3390/life13041066, doi:10.3390/life13041066. This article has 8 citations.

20. (lei2024acuteintermittentporphyria pages 3-4): Jia-Jia Lei, Shuang Li, Bai-Xue Dong, Jing Yang, and Yi Ren. Acute intermittent porphyria: a disease with low penetrance and high heterogeneity. Frontiers in Genetics, Aug 2024. URL: https://doi.org/10.3389/fgene.2024.1374965, doi:10.3389/fgene.2024.1374965. This article has 8 citations and is from a peer-reviewed journal.

21. (aarsand2025practicalrecommendationsfor pages 1-2): Aasne K. Aarsand, Jordi To‐Figueras, Sharon Whatley, Sverre Sandberg, and Caroline Schmitt. Practical recommendations for biochemical and genetic diagnosis of the porphyrias. Liver International, Jun 2025. URL: https://doi.org/10.1111/liv.16012, doi:10.1111/liv.16012. This article has 20 citations and is from a peer-reviewed journal.

22. (sardh2024longtermfollowupof pages 10-12): Eliane Sardh, Manisha Balwani, David C. Rees, Karl E. Anderson, Gang Jia, Marianne T. Sweetser, and Bruce Wang. Long-term follow-up of givosiran treatment in patients with acute intermittent porphyria from a phase 1/2, 48-month open-label extension study. Orphanet Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1186/s13023-024-03284-w, doi:10.1186/s13023-024-03284-w. This article has 11 citations and is from a peer-reviewed journal.

23. (sardh2024longtermfollowupof pages 1-2): Eliane Sardh, Manisha Balwani, David C. Rees, Karl E. Anderson, Gang Jia, Marianne T. Sweetser, and Bruce Wang. Long-term follow-up of givosiran treatment in patients with acute intermittent porphyria from a phase 1/2, 48-month open-label extension study. Orphanet Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1186/s13023-024-03284-w, doi:10.1186/s13023-024-03284-w. This article has 11 citations and is from a peer-reviewed journal.

24. (kubisch2024germanrealworldexperience pages 12-14): Ilja Kubisch, Nils Wohmann, Thaddäus Till Wissniowski, Thomas Stauch, Lucienne Oettel, Eva Diehl-Wiesenecker, Rajan Somasundaram, and Ulrich Stölzel. German real-world experience of patients with diverse features of acute intermittent porphyria treated with givosiran. Journal of Clinical Medicine, 13:6779, Nov 2024. URL: https://doi.org/10.3390/jcm13226779, doi:10.3390/jcm13226779. This article has 9 citations.