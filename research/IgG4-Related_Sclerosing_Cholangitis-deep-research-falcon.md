---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T22:04:10.418988'
end_time: '2026-05-06T22:24:30.309673'
duration_seconds: 1219.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IgG4-Related Sclerosing Cholangitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IgG4-Related Sclerosing Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **IgG4-Related Sclerosing Cholangitis** covering all of the
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
- **Disease Name:** IgG4-Related Sclerosing Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **IgG4-Related Sclerosing Cholangitis** covering all of the
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


## Comprehensive Disease Characteristics Report: IgG4-Related Sclerosing Cholangitis (IgG4-SC)

### Executive summary
IgG4-related sclerosing cholangitis (IgG4-SC), also termed IgG4-related cholangitis (IRC), is a chronic cholestatic fibroinflammatory disease of the bile ducts and a hepatobiliary manifestation of systemic IgG4-related disease (IgG4-RD). It frequently co-occurs with type 1 autoimmune pancreatitis (AIP) and can mimic primary sclerosing cholangitis (PSC) or cholangiocarcinoma (CCA), making multimodal diagnosis essential. Corticosteroids are highly effective for induction but relapse is common; B-cell depletion (rituximab) reduces relapse in relapsing pancreaticobiliary IgG4-RD cohorts, and large observational cohorts/registries are actively evaluating outcomes and diagnostic biomarkers. (herta2025managementofigg4related pages 1-2, ali2020thelongtermoutcomes pages 1-2, majumder2018rituximabmaintenancetherapy pages 1-2)

| Domain | Finding (with numeric values) | Evidence type (guideline/cohort/review) | Key source (author year journal) | URL | Citation ID |
|---|---|---|---|---|---|
| Epidemiology/demographics | Estimated prevalence in Japan: **2.0 per 100,000** (~2,500 patients); extrapolated prevalence/incidence among AIP patients: **1.8 per 100,000** and **0.5 per 100,000** | Guideline | Kamisawa et al. 2019, *J Hepatobiliary Pancreat Sci* | https://doi.org/10.1002/jhbp.596 | (kamisawa2019clinicalpracticeguidelines pages 6-7) |
| Epidemiology/demographics | IgG4-SC is strongly male-predominant: **~80% male**; reported age at diagnosis generally **60–70 years**, range **23.0–88.5 years** | Guideline/review | Kamisawa et al. 2019, *J Hepatobiliary Pancreat Sci* | https://doi.org/10.1002/jhbp.596 | (kamisawa2019clinicalpracticeguidelines pages 6-7) |
| Epidemiology/demographics | Mayo cohort: median age at diagnosis **67 years**; **81% male** (72/89); median follow-up **5.7 years** | Cohort | Ali et al. 2020, *Journal of Gastroenterology* | https://doi.org/10.1007/s00535-020-01714-7 | (ali2020thelongtermoutcomes pages 2-4) |
| Organ association | Concomitant autoimmune pancreatitis (AIP) is frequent: **~90%** in guideline summary; **72%** had past/present pancreatitis in Mayo cohort | Guideline/cohort | Kamisawa et al. 2019; Ali et al. 2020 | https://doi.org/10.1002/jhbp.596 ; https://doi.org/10.1007/s00535-020-01714-7 | (kamisawa2019clinicalpracticeguidelines pages 6-7, ali2020thelongtermoutcomes pages 2-4) |
| Diagnostic framework | **HISORt** framework = Histology, Imaging, Serology, Other organ involvement, Response to therapy | Review | Herta et al. 2025, *Gastroenterology Report* | https://doi.org/10.1093/gastro/goaf032 | (herta2025managementofigg4related pages 1-2) |
| Diagnostic histology thresholds | Suggestive/definitive histology thresholds: **>10 IgG4+ plasma cells/HPF** in biopsy or **>50/HPF** in resection; **IgG4+/IgG+ ratio >0.4 (40%)** | Review | Herta et al. 2025, *Gastroenterology Report*; Smit et al. 2016, *Clinics in Liver Disease* | https://doi.org/10.1093/gastro/goaf032 ; https://doi.org/10.1016/j.cld.2015.08.004 | (herta2025managementofigg4related pages 1-2, smit2016newthoughtson pages 6-8) |
| Diagnostic serology | Serum IgG4 elevated in **~80%** of patients; **>4× ULN** is highly specific but insensitive; modest elevation can occur in **10–15%** of PSC/CCA | Review | Ren et al. 2026, *Frontiers in Medicine* | https://doi.org/10.3389/fmed.2026.1732637 | (ren2026igg4relatedsclerosingcholangitis pages 2-3) |
| Diagnostic classification | Japanese **IgG4-SC2020** criteria comprise **6 domains**: bile-duct narrowing, bile-duct wall thickening, serology, pathology, other-organ involvement, and treatment/response | Validation study | Naitoh et al. 2026, *J Hepatobiliary Pancreat Sci* | https://doi.org/10.1002/jhbp.70056 | (naitoh2026multicentervalidationstudy pages 2-2) |
| Diagnostic performance | In **1,034 IgG4-SC** cases and **447 mimickers**, sensitivity of IgG4-SC2020 vs 2012 was **99.0% vs 89.1%**; specificity was **100%** for pancreatic cancer and cholangiocarcinoma, and **97.5% vs 100%** for PSC | Validation study | Naitoh et al. 2026, *J Hepatobiliary Pancreat Sci* | https://doi.org/10.1002/jhbp.70056 | (naitoh2026multicentervalidationstudy pages 1-2) |
| Imaging phenotype | Cholangiographic subtype frequencies in Japanese survey: type 1 **64%**, type 2a **5%**, type 2b **8%**, type 3 **10%**, type 4 **10%** | Guideline | Kamisawa et al. 2019, *J Hepatobiliary Pancreat Sci* | https://doi.org/10.1002/jhbp.596 | (kamisawa2019clinicalpracticeguidelines pages 2-4) |
| Outcome/prognosis | Hepatobiliary adverse events were lower than in PSC: **15.6 vs 52.6 events/1000 person-years**; **10-year hepatobiliary event probability 11% vs 45%** | Cohort | Ali et al. 2020, *Journal of Gastroenterology* | https://doi.org/10.1007/s00535-020-01714-7 | (ali2020thelongtermoutcomes pages 1-2) |
| Survival | **10-year survival 79%** in IgG4-SC vs **68%** in matched PSC cohort | Cohort | Ali et al. 2020, *Journal of Gastroenterology* | https://doi.org/10.1007/s00535-020-01714-7 | (ali2020thelongtermoutcomes pages 1-2) |
| Cirrhosis/cancer outcomes | Progression to cirrhosis reported at **~5.2–7.5%**; lifetime cholangiocarcinoma risk in Mayo cohort **3.4%** | Cohort/reviewed cohort findings | Ali et al. 2020, *Journal of Gastroenterology* | https://doi.org/10.1007/s00535-020-01714-7 | (ali2020thelongtermoutcomes pages 7-8) |
| Relapse after steroids | Post-steroid relapse reported as **40%** after an **11-week** steroid course; another study cited **50%** relapse at median **4.6 months** after stopping first steroid course | Review | Hegade et al. 2019, *Frontline Gastroenterology* | https://doi.org/10.1136/flgastro-2018-101001 | (hegade2019diagnosisandmanagement pages 5-6, hegade2019diagnosisandmanagement pages 4-5) |
| Relapse risk summary | Reviews summarize relapse in **30–50%** of patients despite high initial steroid responsiveness | Review | Ren et al. 2026, *Frontiers in Medicine* | https://doi.org/10.3389/fmed.2026.1732637 | (ren2026igg4relatedsclerosingcholangitis pages 2-3) |
| Rituximab outcomes | In pancreaticobiliary IgG4-RD, **86%** achieved steroid-free remission at **6 months** after rituximab; **3-year relapse/event rate 45%** with induction alone vs **11%** with maintenance (**P=.034**) | Cohort | Majumder et al. 2018, *Clin Gastroenterol Hepatol* | https://doi.org/10.1016/j.cgh.2018.02.049 | (majumder2018rituximabmaintenancetherapy pages 1-2) |
| Biliary drainage outcomes | In 69 CS-treated patients, **40.6%** underwent endoscopic biliary drainage before CS; spontaneous stent dislodgement occurred in **35.7%** after CS; bile-duct stones developed in **4.3%**, all in EBD-treated patients | Cohort | Miyazawa et al. 2020, *PLoS ONE* | https://doi.org/10.1371/journal.pone.0232089 | (miyazawa2020managementofbiliary pages 1-2) |


*Table: This table summarizes evidence-backed epidemiology, diagnostic criteria, and outcome statistics for IgG4-related sclerosing cholangitis/IgG4-related cholangitis. It is useful as a quick-reference artifact for disease knowledge base curation and clinical comparison with PSC and cholangiocarcinoma.*

---

## 1. Disease Information

### 1.1 What is the disease?
IgG4-SC is an immune-mediated chronic fibroinflammatory cholangitis characterized by bile-duct strictures and wall thickening, lymphoplasmacytic inflammation rich in IgG4-positive plasma cells, fibrosis, and a typically strong response to glucocorticoids. It is widely recognized as the biliary manifestation of IgG4-RD and frequently occurs with type 1 AIP. (kamisawa2019clinicalpracticeguidelines pages 2-4, ali2020thelongtermoutcomes pages 1-2, beuers2025igg4relatedcholangitis pages 1-3)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO)
* **ICD-10 / ICD-11 / MeSH / MONDO / Orphanet / OMIM:** Not explicitly provided in the full-text evidence retrievable in this run; therefore these IDs cannot be asserted here without external ontology lookups. (hegade2019diagnosisandmanagement pages 1-2)

### 1.3 Synonyms and alternative names
* **IgG4-related cholangitis (IRC)** (synonym/alternative name) (herta2025managementofigg4related pages 1-2, beuers2025igg4relatedcholangitis pages 1-3)
* **IgG4-associated cholangitis** (common earlier terminology in reviews; overlaps with IgG4-SC/IRC concept) (cargill2017igg4relatedsclerosingcholangitis pages 2-4)
* Broader/related historical umbrella terms for IgG4-RD include **IgG4-related sclerosing disease**, **IgG4-multiorgan lymphoproliferative syndrome**, etc. (hegade2019diagnosisandmanagement pages 1-2)

### 1.4 Evidence source type (individual vs aggregated)
The report is derived from **aggregated disease-level resources** (clinical practice guidelines, multicenter diagnostic validation, and large cohorts) and selected trial registry entries. (kamisawa2019clinicalpracticeguidelines pages 6-7, ali2020thelongtermoutcomes pages 1-2, naitoh2026multicentervalidationstudy pages 1-2, NCT02616705 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
IgG4-SC is best understood as an **immune-mediated, antigen-driven fibroinflammatory disease** in genetically susceptible individuals. Mechanistically, a dysregulated adaptive immune response (including Th2/Treg-skewed cytokine milieu) promotes B-cell activation and expansion of IgG4+ B cells/plasmablasts, contributing to chronic inflammation and progressive fibrosis. (ren2026igg4relatedsclerosingcholangitis pages 2-3, smit2016newthoughtson pages 12-14)

### 2.2 Risk factors

#### Demographic
* Predominantly affects **older men** (guideline summary: ~80% male; typical age at diagnosis ~60–70 years; Mayo cohort median 67 years, 81% male). (kamisawa2019clinicalpracticeguidelines pages 6-7, ali2020thelongtermoutcomes pages 2-4)

#### Clinical
* Strong association with **type 1 autoimmune pancreatitis (AIP)** (≈90% concomitance in guideline summary; 72% with past/present pancreatitis in Mayo cohort). (kamisawa2019clinicalpracticeguidelines pages 6-7, ali2020thelongtermoutcomes pages 2-4)

#### Environmental/occupational (evidence limited)
Occupational antigen exposure has been proposed in some cohorts (e.g., high rates of “blue-collar” work reported in certain populations), but robust causal data for IgG4-SC specifically were not available in the retrieved excerpts. (tanaka2019igg4relatedsclerosingcholangitis pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not established in the retrieved evidence. However, the conceptual model emphasizes genetic susceptibility and environmental triggers acting together. (ren2026igg4relatedsclerosingcholangitis pages 2-3)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with suggested HPO terms)
Common presentations and laboratory abnormalities include:

1. **Obstructive jaundice** (HPO: *Jaundice* **HP:0000952**) (herta2025managementofigg4related pages 1-2, kamisawa2019clinicalpracticeguidelines pages 6-7)
2. **Upper abdominal pain/discomfort** (HPO: *Abdominal pain* **HP:0002027**) (herta2025managementofigg4related pages 1-2, ali2020thelongtermoutcomes pages 2-4)
3. **Cholestatic liver enzyme elevation** (HPO: *Elevated alkaline phosphatase* **HP:0003155**; *Elevated gamma-glutamyltransferase* **HP:0031304**) (ali2020thelongtermoutcomes pages 2-4)
4. **Biliary strictures** (HPO: *Bile duct stenosis* **HP:0031783** [term mapping may vary]) (kamisawa2019clinicalpracticeguidelines pages 2-4, naitoh2026multicentervalidationstudy pages 2-2)
5. **Weight loss** (HPO: *Weight loss* **HP:0001824**)—also contributes to malignancy mimicry (herta2025managementofigg4related pages 1-2)

Phenotype characteristics:
* Typical onset: **adult/older adult** (no pediatric cases reported in Japan guideline summary). (kamisawa2019clinicalpracticeguidelines pages 6-7)
* Variable severity; a meaningful fraction may be **asymptomatic at diagnosis (28%)** in Japanese experience. (kamisawa2019clinicalpracticeguidelines pages 6-7)

### 3.2 Quality of life impact
Specific QoL instruments (SF-36/EQ-5D/PROMIS) were not reported in the retrieved evidence for IgG4-SC.

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
No **monogenic causal gene** for IgG4-SC was identified in the retrieved evidence; the condition is best supported as **complex immune-mediated** with susceptibility signals rather than Mendelian inheritance. (ren2026igg4relatedsclerosingcholangitis pages 2-3)

### 4.2 Susceptibility genetics / loci (strength: moderate)
* Whole-blood methylation/genotyping study in IgG4-SC showed a strong **HLA-region** signal in meQTL analyses, implicating loci including **HLA-DQB2, HLA-DPA1, HLA-F, HLA-DRA** in shaping methylation patterns. (noble2025epigeneticageacceleration pages 1-2)
* Related PSC research demonstrates that elevated IgG4 in PSC associates with specific HLA haplotypes (lower HLA-B*08; higher HLA-B*07 and DRB1*15), underscoring shared immunogenetic architecture relevant for differential diagnosis contexts. (berntsen2015associationbetweenhla pages 1-1)

### 4.3 Epigenetic information (recent “omics”)
Noble et al. profiled whole-blood DNA methylation in **47 IgG4-SC**, 65 PSC, 64 UC, 88 controls and found:
* **19** significant methylation differences vs controls in IgG4-SC (38 in PSC).
* **Epigenetic age acceleration** in IgG4-SC (not PSC/UC).
* Dysregulated methylation in inflammatory genes including **IFNAR1, TXK, HERC6**, etc. (noble2025epigeneticageacceleration pages 1-2)

### 4.4 Chromosomal abnormalities
Not reported.

---

## 5. Environmental Information
No specific toxins, lifestyle exposures, or infectious triggers were established in the retrieved evidence for IgG4-SC. (ren2026igg4relatedsclerosingcholangitis pages 2-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (causal chain)
1. **Predisposition/trigger:** genetic susceptibility and possible environmental triggers (incompletely defined). (ren2026igg4relatedsclerosingcholangitis pages 2-3)
2. **Immune activation:** Th2/Treg-skewed responses with B-cell activation; oligoclonal expansion of IgG4+ plasmablasts. (ren2026igg4relatedsclerosingcholangitis pages 2-3, smit2016newthoughtson pages 12-14)
3. **Tissue inflammation:** lymphoplasmacytic infiltrate rich in IgG4+ plasma cells; formation of fibroinflammatory lesions causing biliary wall thickening/strictures. (herta2025managementofigg4related pages 1-2, smit2016newthoughtson pages 6-8)
4. **Fibrosis and remodeling:** storiform fibrosis and profibrotic cytokine signaling (e.g., TGF-β) contribute to progressive stricturing and potential secondary biliary cirrhosis in a minority. (ren2026igg4relatedsclerosingcholangitis pages 2-3, ali2020thelongtermoutcomes pages 7-8)

### 6.2 Key immune cells (suggested CL terms)
* **CD4-positive T cell** (CL:0000624)
* **Regulatory T cell (Treg)** (CL:0000815)
* **B cell** (CL:0000236)
* **Plasmablast/plasma cell** (CL:0000980 / CL:0000786)
Mechanistic support for T-cell/B-cell involvement and plasmablast expansion is described in mechanistic reviews. (ren2026igg4relatedsclerosingcholangitis pages 2-3, smit2016newthoughtson pages 12-14)

### 6.3 Key biological processes (suggested GO terms)
* **GO:0006954 inflammatory response**
* **GO:0006955 immune response**
* **GO:0042113 B cell activation**
* **GO:0006959 humoral immune response**
* **GO:0042060 wound healing / fibrosis-related processes** (fibrogenesis)
These are consistent with the described immune activation and fibroinflammatory phenotype. (ren2026igg4relatedsclerosingcholangitis pages 2-3, smit2016newthoughtson pages 12-14)

### 6.4 Histopathology (defining features)
Diagnostic histology requires combinations of:
* Dense lymphoplasmacytic infiltrate
* Storiform fibrosis
* Obliterative phlebitis
with IgG4+ plasma cell thresholds of **>10/HPF (biopsy)** or **>50/HPF (resection)** and **IgG4+/IgG+ ratio >0.4**. (herta2025managementofigg4related pages 1-2, smit2016newthoughtson pages 6-8)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level (suggested UBERON terms)
* **Extrahepatic bile duct** (UBERON:0003707)
* **Intrahepatic bile duct** (UBERON:0003708)
* **Liver** (UBERON:0002107)
* Often associated organ involvement: **pancreas** (UBERON:0001264) via type 1 AIP. (kamisawa2019clinicalpracticeguidelines pages 6-7, ali2020thelongtermoutcomes pages 2-4)

### 7.2 Localization patterns
IgG4-SC has diverse cholangiographic patterns; Japanese guidance describes four cholangiographic types, with national survey frequencies: type 1 **64%**, type 2a **5%**, type 2b **8%**, type 3 **10%**, type 4 **10%**. (kamisawa2019clinicalpracticeguidelines pages 2-4)

---

## 8. Temporal Development

### 8.1 Onset
Typically adult/older adult onset; Japan guideline reports no pediatric/adolescent cases. (kamisawa2019clinicalpracticeguidelines pages 6-7)

### 8.2 Progression/course
Course is often responsive to steroids but **relapsing**. Reviews cite relapse rates commonly **30–50%** despite high initial response, and post-steroid relapse rates around **40–50%** in cited studies. (ren2026igg4relatedsclerosingcholangitis pages 2-3, hegade2019diagnosisandmanagement pages 4-5)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Japan guideline estimates prevalence **2.0 per 100,000** (~2,500 patients) and extrapolated prevalence/incidence based on AIP data of **1.8 per 100,000** and **0.5 per 100,000**, respectively. (kamisawa2019clinicalpracticeguidelines pages 6-7)

### 9.2 Population demographics
* Sex ratio: ~80% male (Japan guideline), 81% male in Mayo cohort. (kamisawa2019clinicalpracticeguidelines pages 6-7, ali2020thelongtermoutcomes pages 2-4)
* Typical age: 60–70s. (kamisawa2019clinicalpracticeguidelines pages 6-7, ali2020thelongtermoutcomes pages 2-4)

### 9.3 Inheritance pattern
No Mendelian inheritance is established; evidence supports a complex immune-mediated condition with genetic susceptibility signals. (ren2026igg4relatedsclerosingcholangitis pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical criteria and diagnostic frameworks

#### HISORt
HISORt integrates **Histology, Imaging, Serology, Other organ involvement, and Response to therapy**; it is emphasized because no single pathognomonic test exists and mimics are common. (herta2025managementofigg4related pages 1-2, smit2016newthoughtson pages 6-8)

#### Japanese clinical diagnostic criteria (2012; revision 2020)
The IgG4-SC2020 criteria include six domains: bile-duct narrowing, bile-duct wall thickening, serology, pathology, other-organ involvement, and response to treatment. (naitoh2026multicentervalidationstudy pages 2-2)

A multicenter validation (Japan; 1,034 IgG4-SC and 447 mimickers) found sensitivity **99.0%** (2020) vs **89.1%** (2012) while maintaining specificity **100%** vs pancreatic cancer and cholangiocarcinoma, and **97.5%** vs PSC (2020). (naitoh2026multicentervalidationstudy pages 1-2)

### 10.2 Key diagnostic thresholds and pitfalls
* Serum IgG4 elevated in ~80% but not diagnostic alone; modest elevations can occur in **10–15%** of PSC/CCA; **>4× ULN** is highly specific but insensitive. (ren2026igg4relatedsclerosingcholangitis pages 2-3)
* Histology cutoffs: >10/HPF biopsy; >50/HPF resection; IgG4+/IgG+ >0.4. (herta2025managementofigg4related pages 1-2)
* Tissue pitfalls: IgG4+ cells can appear in PSC/CCA biopsies; thus malignancy must be excluded carefully. (herta2025managementofigg4related pages 1-2, smit2016newthoughtson pages 6-8)

### 10.3 Differential diagnosis
Primary mimickers:
* **Cholangiocarcinoma (CCA)**
* **Primary sclerosing cholangitis (PSC)**
The need to differentiate these is a central theme across guidelines and diagnostic reviews. (herta2025managementofigg4related pages 1-2, kamisawa2019clinicalpracticeguidelines pages 2-4, ren2026igg4relatedsclerosingcholangitis pages 2-3)

### 10.4 Biomarker development and real-world diagnostic implementation
* ClinicalTrials.gov observational cohort NCT02616705 assessed **bile IgG4 concentration** as a diagnostic biomarker to distinguish IgG4-SC from PSC/CCA and other strictures (enrollment 511; completed 2019-09-30). (NCT02616705 chunk 1)

---

## 11. Outcome / Prognosis

### 11.1 Cohort outcomes
In the Mayo Clinic IgG4-SC cohort (n=89; 1999–2018), hepatobiliary adverse events occurred less frequently than in matched PSC patients: **15.6 vs 52.6 events/1000 person-years**, with **10-year hepatobiliary event probability 11% vs 45%**. Ten-year survival was **79%** in IgG4-SC vs **68%** in PSC (trend). (ali2020thelongtermoutcomes pages 1-2)

### 11.2 Cirrhosis and cholangiocarcinoma risk
The Mayo experience excerpt reports progression to cirrhosis in ~**5.2–7.5%** across reports and an estimated lifetime CCA risk of **3.4%** in that cohort; CCA cases occurred 1.5–5.8 years after IgG4-SC diagnosis in that cohort. (ali2020thelongtermoutcomes pages 7-8)

### 11.3 Prognostic factors
Relapse risk is highlighted as substantial; in pancreaticobiliary IgG4-RD cohorts, relapse risk relates to factors such as younger age and higher post-induction disease activity indices (IgG4-RI) and alkaline phosphatase in one rituximab maintenance analysis. (majumder2018rituximabmaintenancetherapy pages 1-2)

---

## 12. Treatment

### 12.1 First-line: glucocorticoids
Steroids are first-line once diagnosis is confirmed.

**Evidence-supported regimens and relapse statistics:**
* Expert centers use prednisolone **0.5 mg/kg (30–40 mg/day) for 2–4 weeks**, then taper by **5 mg steps**. (hegade2019diagnosisandmanagement pages 5-6)
* Reported post-steroid relapse rates include **40%** after an 11-week course and **50%** at median **4.6 months** after stopping first course in cited studies. (hegade2019diagnosisandmanagement pages 4-5)

**MAXO suggestions:**
* MAXO: *glucocorticoid therapy* (term label varies by MAXO release).

### 12.2 Steroid-sparing immunomodulators
Steroid-sparing regimens listed in hepatobiliary IgG4-RD review include:
* Azathioprine **2 mg/kg daily**
* Mycophenolate mofetil **750–1,000 mg BID**
* Methotrexate **10–25 mg weekly** (+ folate)
* Tacrolimus (target level **4–11 ng/mL**)
* Rituximab **1,000 mg at week 0 and week 2** (B-cell depletion) (culver2016igg4relatedhepatobiliarydisease pages 7-8)

**MAXO suggestions:**
* MAXO: *immunosuppressive agent administration*.

### 12.3 B-cell depletion: rituximab (real-world implementation)
In pancreaticobiliary IgG4-RD cohorts:
* 6-month steroid-free remission after rituximab: **86%**.
* 3-year relapse/event rate **45%** (induction only) vs **11%** (maintenance) (P=.034).
* Clinically significant infections occurred in **6/43**, largely during maintenance. (majumder2018rituximabmaintenancetherapy pages 1-2)

**MAXO suggestions:**
* MAXO: *rituximab therapy* / *B cell depletion therapy*.

### 12.4 Endoscopic management of biliary strictures (real-world)
In a 69-patient IgG4-SC cohort treated with corticosteroids:
* **40.6%** underwent endoscopic biliary drainage (EBD) before steroids.
* Planned stent removal: **84.6%** of removals occurred within 1 month after steroids with no early recurrence.
* Spontaneous stent dislodgement occurred in **35.7%** after steroids; **70%** of dislodgements occurred between 2 weeks and 2 months.
* Bile-duct stones developed in **4.3%** (all in EBD group), and none in steroid-only group (p=0.032). (miyazawa2020managementofbiliary pages 1-2)

Supporting visual tables are available from the paper’s extracted tables. (miyazawa2020managementofbiliary media 3f18bf73, miyazawa2020managementofbiliary media a80fe471, miyazawa2020managementofbiliary media 500893f9)

**MAXO suggestions:**
* MAXO: *endoscopic biliary stenting*; *endoscopic stent removal*.

### 12.5 Emerging/novel therapies
Recent reviews note emerging B-cell–targeting approaches (e.g., anti-CD19), but IgG4-SC–specific primary efficacy data were not retrievable in this run. (herta2025managementofigg4related pages 1-2)

---

## 13. Prevention
No established primary prevention strategies are described in the retrieved evidence. Secondary/tertiary prevention centers on early diagnosis to avoid unnecessary surgery and prevent fibrotic complications, plus surveillance for relapse and biliary complications. (herta2025managementofigg4related pages 1-2)

---

## 14. Other Species / Natural Disease
No naturally occurring animal disease or zoonotic aspects were identified in the retrieved evidence.

---

## 15. Model Organisms
No specific animal models or in vitro models of IgG4-SC were identified in the retrieved evidence.

---

## Recent developments and latest research emphasis (2023–2025 within retrieved sources)
* **Diagnostic criteria modernization**: IgG4-SC2020 criteria show markedly improved sensitivity vs 2012 while maintaining high specificity in a large Japanese multicenter validation (published 2026, but directly relevant to the “current understanding”). (naitoh2026multicentervalidationstudy pages 1-2)
* **Epigenetic/omics**: First whole-blood methylation study in IgG4-SC identifies disease-specific methylation differences and epigenetic age acceleration; HLA-region meQTL signals suggest genotype–methylome relationships. (noble2025epigeneticageacceleration pages 1-2)
* **Real-world diagnostic biomarker efforts**: NCT02616705 tests bile IgG4 as a biomarker to distinguish IgG4-SC from PSC/CCA/other strictures in a large prospective cohort (completed 2019; continued relevance for implementation). (NCT02616705 chunk 1)

---

## Direct abstract-supported quotations (for key claims)
* IgG4-SC definition/diagnostic challenge and need for consensus guidance: “IgG4‐related sclerosing cholangitis (IgG4‐SC) is a distinct type of cholangitis frequently associated with autoimmune pancreatitis and currently recognized as a biliary manifestation of IgG4‐related disease.” (kamisawa2019clinicalpracticeguidelines pages 2-4)
* HISORt-based diagnostic concept and relapse: “Diagnosis is challenging due to the absence of pathognomonic findings but can be achieved using the HISORt criteria (histology, imaging, serology, other organ involvement, and response to immunosuppressive therapy).” (herta2025managementofigg4related pages 1-2)
* Steroid response but relapse: “IgG4-SC often has a good response to initial steroid therapy, but a high relapse rate during follow-up.” (majumder2018rituximabmaintenancetherapy pages 1-2)

---

## Limitations of this evidence package
* Formal ontology identifiers (MONDO/MeSH/Orphanet/ICD) and many ontology mappings (HPO/GO/CL/UBERON/MAXO) were not explicitly provided in retrieved full-text sources; ontology suggestions are therefore limited to widely used terms and should be validated against the relevant ontology releases.
* Several key 2023–2024 primary papers/guidelines relevant to IgG4-SC may be unobtainable in this run (e.g., certain systematic reviews/meta-analyses and some 2023 nationwide relapse/cancer-risk studies), so some “latest” claims (e.g., anti-CD19 trial outcomes in IgG4-RD) are discussed only at a high level.



References

1. (herta2025managementofigg4related pages 1-2): Toni Herta, Maik Schröder, Dominik Geisel, Cornelius Engelmann, and Frank Tacke. Management of igg4-related cholangitis: diagnosis, therapy, and long-term surveillance. Gastroenterology Report, Apr 2025. URL: https://doi.org/10.1093/gastro/goaf032, doi:10.1093/gastro/goaf032. This article has 1 citations and is from a peer-reviewed journal.

2. (ali2020thelongtermoutcomes pages 1-2): Ahmad Hassan Ali, Yan Bi, Jorge D. Machicado, Sushil Garg, Ryan J. Lennon, Lizhi Zhang, Naoki Takahashi, Elizabeth J. Carey, Keith D. Lindor, J. Gage Buness, James H. Tabibian, and Suresh T. Chari. The long-term outcomes of patients with immunoglobulin g4-related sclerosing cholangitis: the mayo clinic experience. Journal of Gastroenterology, 55:1087-1097, Aug 2020. URL: https://doi.org/10.1007/s00535-020-01714-7, doi:10.1007/s00535-020-01714-7. This article has 37 citations and is from a domain leading peer-reviewed journal.

3. (majumder2018rituximabmaintenancetherapy pages 1-2): Shounak Majumder, Sonmoon Mohapatra, Ryan J. Lennon, Guilherme Piovezani Ramos, Neil Postier, Ferga C. Gleeson, Michael J. Levy, Randall K. Pearson, Bret T. Petersen, Santhi Swaroop Vege, Suresh T. Chari, Mark D. Topazian, and Thomas E. Witzig. Rituximab maintenance therapy reduces rate of relapse of pancreaticobiliary immunoglobulin g4-related disease. Clinical Gastroenterology and Hepatology, 16:1947-1953, Dec 2018. URL: https://doi.org/10.1016/j.cgh.2018.02.049, doi:10.1016/j.cgh.2018.02.049. This article has 101 citations and is from a domain leading peer-reviewed journal.

4. (kamisawa2019clinicalpracticeguidelines pages 6-7): Terumi Kamisawa, Takahiro Nakazawa, Susumu Tazuma, Yoh Zen, Atsushi Tanaka, Hirotaka Ohara, Takashi Muraki, Kazuo Inui, Dai Inoue, Takayoshi Nishino, Itaru Naitoh, Takao Itoi, Kenji Notohara, Atsushi Kanno, Kensuke Kubota, Kenji Hirano, Hiroyuki Isayama, Kyoko Shimizu, Toshio Tsuyuguchi, Tooru Shimosegawa, Shigeyuki Kawa, Tsutomu Chiba, Kazuichi Okazaki, Hajime Takikawa, Wataru Kimura, Michiaki Unno, and Masahiro Yoshida. Clinical practice guidelines for igg4‐related sclerosing cholangitis. Journal of Hepato-Biliary-Pancreatic Sciences, 26:9-42, Jan 2019. URL: https://doi.org/10.1002/jhbp.596, doi:10.1002/jhbp.596. This article has 225 citations and is from a peer-reviewed journal.

5. (ali2020thelongtermoutcomes pages 2-4): Ahmad Hassan Ali, Yan Bi, Jorge D. Machicado, Sushil Garg, Ryan J. Lennon, Lizhi Zhang, Naoki Takahashi, Elizabeth J. Carey, Keith D. Lindor, J. Gage Buness, James H. Tabibian, and Suresh T. Chari. The long-term outcomes of patients with immunoglobulin g4-related sclerosing cholangitis: the mayo clinic experience. Journal of Gastroenterology, 55:1087-1097, Aug 2020. URL: https://doi.org/10.1007/s00535-020-01714-7, doi:10.1007/s00535-020-01714-7. This article has 37 citations and is from a domain leading peer-reviewed journal.

6. (smit2016newthoughtson pages 6-8): Wouter L. Smit, Emma L. Culver, and Roger W. Chapman. New thoughts on immunoglobulin g4-related sclerosing cholangitis. Clinics in liver disease, 20 1:47-65, Feb 2016. URL: https://doi.org/10.1016/j.cld.2015.08.004, doi:10.1016/j.cld.2015.08.004. This article has 21 citations and is from a peer-reviewed journal.

7. (ren2026igg4relatedsclerosingcholangitis pages 2-3): Xiangxiang Ren, Xiaoshi Jin, Litao Liu, and Meng Zhang. Igg4-related sclerosing cholangitis: navigating diagnostic dilemmas and the challenge of relapse. Frontiers in Medicine, 13:1732637, Feb 2026. URL: https://doi.org/10.3389/fmed.2026.1732637, doi:10.3389/fmed.2026.1732637. This article has 0 citations.

8. (naitoh2026multicentervalidationstudy pages 2-2): Itaru Naitoh, Takahiro Nakazawa, Kensuke Kubota, Takayoshi Nishino, Akira Nakamura, Dai Inoue, Takanori Sano, Kazuhiro Kikuta, Yusuke Kurita, Kazuro Chiba, Tsukasa Ikeura, Hiroyuki Matsubayashi, Takuya Ishikawa, Masaki Kuwatani, Terumi Kamisawa, Ichiro Yasuda, Mitsuhiro Kawano, and Atsushi Masamune. Multicenter validation study of the clinical diagnostic criteria for <scp>igg4</scp> ‐related sclerosing cholangitis 2020 in japan. Journal of Hepato-Biliary-Pancreatic Sciences, 33:294-303, Jan 2026. URL: https://doi.org/10.1002/jhbp.70056, doi:10.1002/jhbp.70056. This article has 3 citations and is from a peer-reviewed journal.

9. (naitoh2026multicentervalidationstudy pages 1-2): Itaru Naitoh, Takahiro Nakazawa, Kensuke Kubota, Takayoshi Nishino, Akira Nakamura, Dai Inoue, Takanori Sano, Kazuhiro Kikuta, Yusuke Kurita, Kazuro Chiba, Tsukasa Ikeura, Hiroyuki Matsubayashi, Takuya Ishikawa, Masaki Kuwatani, Terumi Kamisawa, Ichiro Yasuda, Mitsuhiro Kawano, and Atsushi Masamune. Multicenter validation study of the clinical diagnostic criteria for <scp>igg4</scp> ‐related sclerosing cholangitis 2020 in japan. Journal of Hepato-Biliary-Pancreatic Sciences, 33:294-303, Jan 2026. URL: https://doi.org/10.1002/jhbp.70056, doi:10.1002/jhbp.70056. This article has 3 citations and is from a peer-reviewed journal.

10. (kamisawa2019clinicalpracticeguidelines pages 2-4): Terumi Kamisawa, Takahiro Nakazawa, Susumu Tazuma, Yoh Zen, Atsushi Tanaka, Hirotaka Ohara, Takashi Muraki, Kazuo Inui, Dai Inoue, Takayoshi Nishino, Itaru Naitoh, Takao Itoi, Kenji Notohara, Atsushi Kanno, Kensuke Kubota, Kenji Hirano, Hiroyuki Isayama, Kyoko Shimizu, Toshio Tsuyuguchi, Tooru Shimosegawa, Shigeyuki Kawa, Tsutomu Chiba, Kazuichi Okazaki, Hajime Takikawa, Wataru Kimura, Michiaki Unno, and Masahiro Yoshida. Clinical practice guidelines for igg4‐related sclerosing cholangitis. Journal of Hepato-Biliary-Pancreatic Sciences, 26:9-42, Jan 2019. URL: https://doi.org/10.1002/jhbp.596, doi:10.1002/jhbp.596. This article has 225 citations and is from a peer-reviewed journal.

11. (ali2020thelongtermoutcomes pages 7-8): Ahmad Hassan Ali, Yan Bi, Jorge D. Machicado, Sushil Garg, Ryan J. Lennon, Lizhi Zhang, Naoki Takahashi, Elizabeth J. Carey, Keith D. Lindor, J. Gage Buness, James H. Tabibian, and Suresh T. Chari. The long-term outcomes of patients with immunoglobulin g4-related sclerosing cholangitis: the mayo clinic experience. Journal of Gastroenterology, 55:1087-1097, Aug 2020. URL: https://doi.org/10.1007/s00535-020-01714-7, doi:10.1007/s00535-020-01714-7. This article has 37 citations and is from a domain leading peer-reviewed journal.

12. (hegade2019diagnosisandmanagement pages 5-6): Vinod S Hegade, Maria B Sheridan, and Matthew T Huggett. Diagnosis and management of igg4-related disease. Frontline Gastroenterology, 10:275-283, Oct 2019. URL: https://doi.org/10.1136/flgastro-2018-101001, doi:10.1136/flgastro-2018-101001. This article has 46 citations and is from a peer-reviewed journal.

13. (hegade2019diagnosisandmanagement pages 4-5): Vinod S Hegade, Maria B Sheridan, and Matthew T Huggett. Diagnosis and management of igg4-related disease. Frontline Gastroenterology, 10:275-283, Oct 2019. URL: https://doi.org/10.1136/flgastro-2018-101001, doi:10.1136/flgastro-2018-101001. This article has 46 citations and is from a peer-reviewed journal.

14. (miyazawa2020managementofbiliary pages 1-2): Masaki Miyazawa, Hajime Takatori, Kazunori Kawaguchi, Kazuya Kitamura, Kuniaki Arai, Koichiro Matsuda, Takeshi Urabe, Katsuhisa Inamura, Takuya Komura, Hideki Mizuno, Uichiro Fuchizaki, Taro Yamashita, Yoshio Sakai, Tatsuya Yamashita, Eishiro Mizukoshi, Masao Honda, and Shuichi Kaneko. Management of biliary stricture in patients with igg4-related sclerosing cholangitis. PLoS ONE, 15:e0232089, Apr 2020. URL: https://doi.org/10.1371/journal.pone.0232089, doi:10.1371/journal.pone.0232089. This article has 18 citations and is from a peer-reviewed journal.

15. (beuers2025igg4relatedcholangitis pages 1-3): Ulrich Beuers and David C. Trampert. Igg4-related cholangitis. Seminars in Liver Disease, May 2025. URL: https://doi.org/10.1055/a-2588-3875, doi:10.1055/a-2588-3875. This article has 1 citations and is from a peer-reviewed journal.

16. (hegade2019diagnosisandmanagement pages 1-2): Vinod S Hegade, Maria B Sheridan, and Matthew T Huggett. Diagnosis and management of igg4-related disease. Frontline Gastroenterology, 10:275-283, Oct 2019. URL: https://doi.org/10.1136/flgastro-2018-101001, doi:10.1136/flgastro-2018-101001. This article has 46 citations and is from a peer-reviewed journal.

17. (cargill2017igg4relatedsclerosingcholangitis pages 2-4): T. Cargill, E. Culver, and R. Chapman. Igg4-related sclerosing cholangitis. Biliary Disease, pages 243-261, Jan 2017. URL: https://doi.org/10.1007/978-3-319-50168-0\_12, doi:10.1007/978-3-319-50168-0\_12. This article has 29 citations.

18. (NCT02616705 chunk 1): Lewis R. Roberts. Bile Usefulness for Detecting IgG4-related Sclerosing Cholangitis. Mayo Clinic. 2015. ClinicalTrials.gov Identifier: NCT02616705

19. (smit2016newthoughtson pages 12-14): Wouter L. Smit, Emma L. Culver, and Roger W. Chapman. New thoughts on immunoglobulin g4-related sclerosing cholangitis. Clinics in liver disease, 20 1:47-65, Feb 2016. URL: https://doi.org/10.1016/j.cld.2015.08.004, doi:10.1016/j.cld.2015.08.004. This article has 21 citations and is from a peer-reviewed journal.

20. (tanaka2019igg4relatedsclerosingcholangitis pages 1-2): Atsushi Tanaka. Igg4-related sclerosing cholangitis and primary sclerosing cholangitis. Gut and Liver, 13:300-307, May 2019. URL: https://doi.org/10.5009/gnl18085, doi:10.5009/gnl18085. This article has 84 citations and is from a peer-reviewed journal.

21. (noble2025epigeneticageacceleration pages 1-2): Alexandra Noble, Rodrigo Motta, Silvia Cabras, Belen Moron Flores, Jan Nowak, Aleksandra Glapa-Nowak, Alessandra Geremia, Jack Satsangi, and Emma Culver. Epigenetic age acceleration and methylation differences in igg4-related cholangitis and primary sclerosing cholangitis. Clinical Epigenetics, Jan 2025. URL: https://doi.org/10.1186/s13148-024-01803-x, doi:10.1186/s13148-024-01803-x. This article has 2 citations and is from a peer-reviewed journal.

22. (berntsen2015associationbetweenhla pages 1-1): Natalie L. Berntsen, Olav Klingenberg, Brian D. Juran, Maria Benito de Valle, Björn Lindkvist, Konstantinos N. Lazaridis, Kirsten Muri Boberg, Tom H. Karlsen, and Johannes Roksund Hov. Association between hla haplotypes and increased serum levels of igg4 in patients with primary sclerosing cholangitis. Gastroenterology, 148 5:924-927.e2, May 2015. URL: https://doi.org/10.1053/j.gastro.2015.01.041, doi:10.1053/j.gastro.2015.01.041. This article has 59 citations and is from a highest quality peer-reviewed journal.

23. (culver2016igg4relatedhepatobiliarydisease pages 7-8): Emma L. Culver and Roger W. Chapman. Igg4-related hepatobiliary disease: an overview. Nature Reviews Gastroenterology &Hepatology, 13:601-612, Oct 2016. URL: https://doi.org/10.1038/nrgastro.2016.132, doi:10.1038/nrgastro.2016.132. This article has 109 citations.

24. (miyazawa2020managementofbiliary media 3f18bf73): Masaki Miyazawa, Hajime Takatori, Kazunori Kawaguchi, Kazuya Kitamura, Kuniaki Arai, Koichiro Matsuda, Takeshi Urabe, Katsuhisa Inamura, Takuya Komura, Hideki Mizuno, Uichiro Fuchizaki, Taro Yamashita, Yoshio Sakai, Tatsuya Yamashita, Eishiro Mizukoshi, Masao Honda, and Shuichi Kaneko. Management of biliary stricture in patients with igg4-related sclerosing cholangitis. PLoS ONE, 15:e0232089, Apr 2020. URL: https://doi.org/10.1371/journal.pone.0232089, doi:10.1371/journal.pone.0232089. This article has 18 citations and is from a peer-reviewed journal.

25. (miyazawa2020managementofbiliary media a80fe471): Masaki Miyazawa, Hajime Takatori, Kazunori Kawaguchi, Kazuya Kitamura, Kuniaki Arai, Koichiro Matsuda, Takeshi Urabe, Katsuhisa Inamura, Takuya Komura, Hideki Mizuno, Uichiro Fuchizaki, Taro Yamashita, Yoshio Sakai, Tatsuya Yamashita, Eishiro Mizukoshi, Masao Honda, and Shuichi Kaneko. Management of biliary stricture in patients with igg4-related sclerosing cholangitis. PLoS ONE, 15:e0232089, Apr 2020. URL: https://doi.org/10.1371/journal.pone.0232089, doi:10.1371/journal.pone.0232089. This article has 18 citations and is from a peer-reviewed journal.

26. (miyazawa2020managementofbiliary media 500893f9): Masaki Miyazawa, Hajime Takatori, Kazunori Kawaguchi, Kazuya Kitamura, Kuniaki Arai, Koichiro Matsuda, Takeshi Urabe, Katsuhisa Inamura, Takuya Komura, Hideki Mizuno, Uichiro Fuchizaki, Taro Yamashita, Yoshio Sakai, Tatsuya Yamashita, Eishiro Mizukoshi, Masao Honda, and Shuichi Kaneko. Management of biliary stricture in patients with igg4-related sclerosing cholangitis. PLoS ONE, 15:e0232089, Apr 2020. URL: https://doi.org/10.1371/journal.pone.0232089, doi:10.1371/journal.pone.0232089. This article has 18 citations and is from a peer-reviewed journal.