---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T18:33:45.616901'
end_time: '2026-04-25T18:47:41.219641'
duration_seconds: 835.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kabuki Syndrome
  mondo_id: MONDO:0016512
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
- **Disease Name:** Kabuki Syndrome
- **MONDO ID:** MONDO:0016512 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kabuki Syndrome** covering all of the
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
- **Disease Name:** Kabuki Syndrome
- **MONDO ID:** MONDO:0016512 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kabuki Syndrome** covering all of the
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


# Kabuki Syndrome (MONDO:0016512) — Disease Characteristics Research Report

## 1. Disease Information

### 1.1 Overview (definition and current understanding)
Kabuki syndrome (KS) is a rare, congenital, multisystem neurodevelopmental disorder characterized by a recognizable facial gestalt, developmental delay/intellectual disability, skeletal anomalies, dermatoglyphic anomalies (including persistent fetal fingertip pads), and postnatal growth deficiency, with additional frequent involvement of cardiac, renal, hearing, immune, endocrine, and gastrointestinal systems. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 1-2)

**Epidemiologic frequency (range reported in large review):** estimated frequency ~1:32,000–1:86,000. (barry2022fromgenotypeto pages 1-2)

**Evidence type:** aggregated disease-level literature review synthesizing 152 publications and 1369 individuals. (barry2022fromgenotypeto pages 1-2, barry2022fromgenotypeto pages 2-4)

### 1.2 Key identifiers and synonyms
A structured list of identifiers available from the retrieved sources is provided here:

| Identifier system | Identifier/value | Notes |
|---|---|---|
| MONDO | MONDO:0016512 | User-provided disease identifier for Kabuki syndrome. Not independently verified in retrieved evidence. |
| OMIM | Kabuki syndrome 1 (KS1): 147920 | KMT2D-related Kabuki syndrome; autosomal dominant in retrieved reviews/management sources (dugan2021kabukisyndrome pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 1-2) |
| OMIM | Kabuki syndrome 2 (KS2): 300867 | KDM6A-related Kabuki syndrome; X-linked in retrieved reviews/management sources (dugan2021kabukisyndrome pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 1-2) |
| OMIM / gene | KMT2D: 602113 | Major causal gene for KS1; cited in recent mechanistic and clinical reviews (golden2023molecularinsightsof pages 1-3, golden2023molecularinsightsof pages 9-11) |
| OMIM / gene | KDM6A: 300128 | Causal gene for KS2; X-linked histone demethylase noted in retrieved reviews and KS2 cohort study (golden2023molecularinsightsof pages 1-3, wang2024sexspecificdifferencein pages 2-4) |
| Disease name | Kabuki syndrome | Preferred disease name across retrieved sources (barry2022fromgenotypeto pages 1-2, adam2019kabukisyndromeinternational pages 1-2) |
| Synonym | Kabuki make-up syndrome | Explicit synonym in management/review sources (dugan2021kabukisyndrome pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 8-9) |
| Synonym | Niikawa–Kuroki syndrome | Historical synonym in review sources (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3) |
| Orphanet | Not in retrieved sources | No Orphanet identifier was present in the gathered evidence. |
| MeSH | Not in retrieved sources | No MeSH identifier was present in the gathered evidence. |
| ICD-10 | Not in retrieved sources | No ICD-10 code was present in the gathered evidence. |
| ICD-11 | Not in retrieved sources | No ICD-11 code was present in the gathered evidence. |


*Table: This table summarizes the key disease names and identifiers for Kabuki syndrome that were supported by retrieved evidence, including KS1/KS2 OMIM entries and common synonyms. Fields not found in the evidence are explicitly marked to avoid overclaiming.*

**Synonyms supported by retrieved sources** include *Kabuki make-up syndrome* and *Niikawa–Kuroki syndrome*. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 8-9)

**Note on missing identifiers:** Orphanet IDs, MeSH IDs, and ICD-10/ICD-11 codes were **not present in the retrieved documents** available to this run; therefore they are not asserted here. (artifact-00)

### 1.3 Consensus diagnostic framing (expert consensus)
The international consensus diagnostic criteria emphasize a recognisable clinical pattern plus molecular confirmation when available.

**Direct abstract quote (consensus paper):** “*The authors propose that a definitive diagnosis can be made in an individual of any age with a history of infantile hypotonia, developmental delay and/or intellectual disability, and one or both of the following major criteria: (1) a pathogenic or likely pathogenic variant in KMT2D or KDM6A; and (2) typical dysmorphic features…*” (Adam et al., 2019, *Journal of Medical Genetics*, published online 2019; DOI URL: https://doi.org/10.1136/jmedgenet-2018-105625). (adam2019kabukisyndromeinternational pages 1-2)

## 2. Etiology

### 2.1 Primary causal factors (genetic)
KS is primarily a Mendelian disorder caused by **pathogenic variants in chromatin regulators**:
- **KMT2D (KS1; autosomal dominant):** heterozygous dominant loss-of-function variants are the most common cause (often de novo). (barry2022fromgenotypeto pages 1-2, jung2023characterizingthemolecular pages 1-5, golden2023molecularinsightsof pages 1-3)
- **KDM6A (KS2; X-linked):** heterozygous (female) or hemizygous (male) variants cause KS2. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3, wang2024sexspecificdifferencein pages 2-4)

Mechanistically, KMT2D is an H3K4 methyltransferase, and KDM6A is an H3K27 demethylase; both are key components of enhancer/promoter chromatin regulation during development. (golden2023molecularinsightsof pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 2-3)

### 2.2 Risk factors / protective factors / gene–environment interactions
For KS (a monogenic syndrome), the predominant “risk factor” is carrying a pathogenic germline variant in **KMT2D** or **KDM6A**; additional environmental risk and protective factors are not well-defined in the retrieved sources. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3)

A plausible **gene–environment interaction** discussed in recent intervention work is that metabolic state (ketosis via dietary intervention) may modulate downstream molecular phenotypes (e.g., ribosomal/protein-translation pathways) in KMT2D-related KS. (tsang2024ketogenicdietmodifies pages 8-10, tsang2024ketogenicdietmodifies pages 2-3)

## 3. Phenotypes (with HPO suggestions)

### 3.1 Core phenotypic domains
Across large reviews and clinical management sources, commonly described domains include:
- **Craniofacial gestalt** (long palpebral fissures with lower-lid eversion; arched/broad eyebrows with lateral sparseness; depressed nasal tip/short columella; prominent/cupped ears) (adam2019kabukisyndromeinternational pages 1-2, dugan2021kabukisyndrome pages 1-3)
- **Neurodevelopmental phenotype** (developmental delay; intellectual disability; hypotonia) (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3)
- **Skeletal anomalies** and **persistent fingertip pads** (barry2022fromgenotypeto pages 1-2, adam2019kabukisyndromeinternational pages 1-2)
- **Postnatal growth deficiency/short stature** (barry2022fromgenotypeto pages 1-2, boniel2021kabukisyndrome—clinicalreview pages 1-2)
- **Congenital heart disease** (barry2022fromgenotypeto pages 1-2, lee2024geneticandphenotypic pages 1-2)
- **Immune dysfunction** (recurrent infections, hypogammaglobulinemia; autoimmunity in a subset) (margot2020immunopathologicalmanifestationsin pages 1-2)
- **Hearing loss** (conductive and sensorineural components) (kalinousky2023kmt2ddeficiencycauses pages 5-7)

### 3.2 Recent cohort statistics (2024 Taiwanese case series)
A 2024 Taiwanese case series (n=23) provides concrete phenotype frequencies (primarily KMT2D):
- Distinct facial features: **100%**
- Intellectual disability: **100%**
- Developmental delay: **95.7%**
- Speech delay: **78.3%**
- Hypotonia: **69.6%**
- Congenital heart abnormalities: **69.6%**
- Recurrent infections: **65.2%**
- Hearing loss: **39.1%**
- Seizures: **26.1%**
- Cleft palate: **26.1%**
- Renal anomalies: **21.7%**
(Lee et al., 2024, *Diagnostics*, Aug 2024; DOI URL: https://doi.org/10.3390/diagnostics14161815). (lee2024geneticandphenotypic pages 1-2)

**Cardiac lesion distribution within CHD subset (n=16):** ASD 37.5% (6/16), VSD 18.8% (3/16), aortic coarctation 18.8% (3/16). (lee2024geneticandphenotypic pages 6-7, lee2024geneticandphenotypic pages 4-6)

### 3.3 Hearing phenotype (recent 2023 human+mouse study)
A 2023 KS1 study (KMT2D; n=21 individuals) reported:
- Current hearing loss in **71.43% (15/21)**
- Female skew in that cohort: **all 12 females** reported hearing loss vs **3/9 (33.33%)** males
- Among those with hearing loss and reported type (n=10): **6 sensorineural**, **1 conductive**, **3 mixed**
- Structural ear abnormalities in **19.05% (4/21)**
(Kalinousky et al., 2023, *Genes*, Dec 2023; DOI URL: https://doi.org/10.3390/genes15010048). (kalinousky2023kmt2ddeficiencycauses pages 5-7)

### 3.4 Immune/autoimmune phenotype statistics (registry)
A registry study (n=177; molecularly confirmed KMT2D/KDM6A) quantified:
- Susceptibility to infections: **44.1% (78/177)**
- Hypogammaglobulinemia: **58.2% (46/79 tested)**
- Autoimmune disease overall: **13.6% (24/177)**; in adults: **25.6% (11/43)**
- Immune thrombocytopenic purpura: **7.3% (13/177)**; autoimmune hemolytic anemia: **4.0% (7/177)**
(Margot et al., 2020, *Genetics in Medicine*, Jan 2020; DOI URL: https://doi.org/10.1038/s41436-019-0623-x). (margot2020immunopathologicalmanifestationsin pages 1-2)

### 3.5 Quality of life / humanistic burden
Caregiver/adolescent report studies indicate substantial multidimensional burden; while this run did not extract instrument-level statistics (e.g., EQ-5D), a qualitative study reports “substantial negative effects on physical, mental, emotional, and social aspects of health-related quality of life.” (barry2022fromgenotypeto pages 1-2)

### 3.6 HPO term suggestions (non-exhaustive; ontology mapping suggestions)
(These are suggested mappings for knowledge-base structuring; the retrieved sources support the clinical concepts but do not enumerate HPO IDs.)
- Facial gestalt: Long palpebral fissures; Everted lower eyelids; Arched eyebrows; Large/protruding ears
- Neurodevelopment: Global developmental delay; Intellectual disability; Hypotonia; Speech delay
- Growth: Postnatal growth retardation; Short stature
- Cardiac: Congenital heart defect; Atrial septal defect; Ventricular septal defect; Coarctation of aorta
- Immune: Recurrent infections; Hypogammaglobulinemia; Immune thrombocytopenia; Autoimmune hemolytic anemia
- Hearing: Hearing impairment; Sensorineural hearing loss; Conductive hearing loss

## 4. Genetic / Molecular Information

### 4.1 Causal genes and inheritance
- **KMT2D (KS1):** autosomal dominant; typically de novo but familial transmission occurs. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3)
- **KDM6A (KS2):** X-linked; sex-dependent expressivity is reported in recent KS2 cohorts. (wang2024sexspecificdifferencein pages 2-4, wang2024sexspecificdifferencein pages 5-6)

### 4.2 Variant classes and spectrum
Large aggregated reviews and recent KS1-focused review note broad variant classes including nonsense, frameshift, splice-site, indels, CNVs, and missense (some clustering near functional domains). (barry2022fromgenotypeto pages 2-4, golden2023molecularinsightsof pages 9-11)

**Examples of quantitative variant spectrum reporting:**
- In the 2024 Taiwanese series (n=23), variant class frequencies were reported (patient-level): missense 26.1%, nonsense 21.7%, frameshift 17.4%. (lee2024geneticandphenotypic pages 1-2)
- In the same study, among **16 unique** KMT2D variants: nonsense 31.3%, missense 18.7%, frameshift 18.7%, deletions 18.7%, splicing 6.3%, insertion/deletion 6.3%. (lee2024geneticandphenotypic pages 2-4)

### 4.3 Epigenetic and transcriptional consequences (human evidence; 2023)
A 2023 study profiled PBMCs from **33 individuals** with KMT2D-related KS and **36 controls**, finding:
- Distinct enhancer signatures in H3K4me1/H3K4me2
- **Reduced promoter-distal enhancer signals at immune-related genes** and overlap with ~**31% of normal blood-cell super-enhancers**
- **Increased enhancer signals near promoters of metabolic genes**, with elevated transcription
(Jung et al., 2023, *Human Molecular Genetics*, Oct 2023; DOI URL: https://doi.org/10.1101/2022.10.25.22280882). (jung2023characterizingthemolecular pages 1-5)

**Direct abstract quote:** “*…we profiled and characterized alterations in histone modification and gene transcription in peripheral blood mononuclear cells (PBMCs) from 33 patients with KMT2D mutations and 36 unaffected healthy controls.*” (jung2023characterizingthemolecular pages 1-5)

### 4.4 Immune mechanism: integrin regulation in T cells (2024)
A 2024 mechanistic immunology study reports that KMT2D directly regulates leukocyte integrin loci (chromatin and expression), with functional impact on thymocyte migration/egress and peripheral T-cell composition.

Key mechanistic findings include:
- Reduced expression of integrins (e.g., Itgal, Itgb7) at transcript and protein levels; H3K4me3 ChIP-PCR supports direct control (potter2024kmt2dregulatesactivation pages 1-2, potter2024kmt2dregulatesactivation pages 9-11)
- Peripheral shifts in humans and mice, including reduced naïve/RTE and increased memory phenotypes (potter2024kmt2dregulatesactivation pages 14-16)
(Potter et al., 2024, *Frontiers in Immunology*, May 2024; DOI URL: https://doi.org/10.3389/fimmu.2024.1341745). (potter2024kmt2dregulatesactivation pages 1-2)

### 4.5 Cell-type specificity of chromatin disruption (2024)
A 2024 Genome Research study in Kabuki mouse models indicates that chromatin accessibility abnormalities in neurons are **largely distinct** from those in peripheral B and T cells, with neuron-specific enrichment at CpG islands and aging-linked elements.

**Direct abstract-level statement from retrieved text:** “*…chromatin accessibility abnormalities in neurons are mostly distinct from those in B or T cells… Neurons, but not B or T cells, show preferential chromatin disruption at CpG islands and at regulatory elements linked to aging.*” (Boukas et al., 2024, *Genome Research*, May 2024; DOI URL: https://doi.org/10.1101/gr.278416.123). (boukas2024neuronspecificchromatindisruption pages 1-2)

### 4.6 KS2 growth mechanism and convergence with KS1 (2024)
A 2024 KS2 mouse study (Kdm6a tm1d/+), focusing on endochondral ossification, found:
- Decreased femur/tibia length; cortical and trabecular structural changes
- Shorter growth plates, driven by reduced hypertrophic chondrocyte size and hypertrophic zone height
- In vitro Kdm6a−/− cells showed premature/enhanced chondrocyte differentiation
- RNA-seq showed **convergent gene expression** between Kdm6a−/− and Kmt2d−/− lines, suggesting shared downstream pathways (Gao et al., 2024, *PLOS Genetics*, Jun 2024; DOI URL: https://doi.org/10.1371/journal.pgen.1011310). (gao2024growthdeficiencyin pages 1-2, gao2024growthdeficiencyin pages 3-6)

## 5. Environmental Information
No specific, reproducible non-genetic environmental causal factors are described in the retrieved sources for Kabuki syndrome, consistent with its primary Mendelian etiology. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3)

Dietary metabolic state (ketogenic/Modified Atkins) is an **intervention** rather than a causal environmental exposure and is covered under Treatment/Applications. (tsang2024ketogenicdietmodifies pages 8-10, NCT04722315 chunk 1)

## 6. Mechanism / Pathophysiology

### 6.1 Chromatin and histone-mark dysregulation (core causal chain)
**Upstream trigger:** germline loss-of-function (typically) variants in KMT2D (H3K4 methyltransferase) and/or KDM6A (H3K27 demethylase). (golden2023molecularinsightsof pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 2-3)

**Intermediate molecular consequence:** altered enhancer/promoter chromatin state and transcriptional dysregulation, measurable in human immune cells as altered H3K4me1/H3K4me2 enhancer signatures with reduced enhancer activity at immune genes. (jung2023characterizingthemolecular pages 1-5)

**Downstream cellular consequences:** impaired maturation/function of immune cells (B- and T-cell defects; altered integrin programs and migration/egress), contributing to recurrent infections, hypogammaglobulinemia, and autoimmune manifestations. (margot2020immunopathologicalmanifestationsin pages 1-2, potter2024kmt2dregulatesactivation pages 14-16)

**Clinical manifestations:** multisystem developmental phenotype including neurodevelopmental delay, craniofacial anomalies, growth deficiency, heart defects, hearing loss, and immune disease. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3, lee2024geneticandphenotypic pages 1-2, kalinousky2023kmt2ddeficiencycauses pages 5-7)

### 6.2 Immune pathway mechanism (integrin/MST1 axis)
In Kmt2d-deficient murine thymocytes, transcriptomics implicate integrin-linked migration programs (including Mst1 pathway-related genes such as Rap1a/Vasp and integrin genes) as dysregulated, aligning with abnormal T-cell maturation and peripheral distribution shifts. (potter2024kmt2dregulatesactivation pages 11-13, potter2024kmt2dregulatesactivation pages 14-16)

### 6.3 Neurodevelopment: tissue specificity and episignature caveat
The 2024 neuron-vs-blood chromatin accessibility study supports a model in which neurodevelopmental chromatin disruptions are not simply recapitulated by blood epigenomic patterns; neurons show preferential disruption at CpG islands and aging-linked regulatory elements. This helps explain why **blood-derived episignatures** can be diagnostically useful yet incomplete as mechanistic proxies for brain phenotypes. (boukas2024neuronspecificchromatindisruption pages 1-2)

### 6.4 Growth-plate biology and endochondral ossification
KS2 growth failure can arise from impaired hypertrophic chondrocyte enlargement (hypertrophic-zone shortening) and premature chondrogenic differentiation, with transcriptional convergence between KS1 and KS2 models supporting a shared downstream program affecting cartilage development. (gao2024growthdeficiencyin pages 1-2, gao2024growthdeficiencyin pages 3-6)

### 6.5 Suggested ontology terms (mechanism structuring; not exhaustively validated here)
- **GO biological process (suggested):** chromatin organization; histone H3-K4 methylation; regulation of transcription by RNA polymerase II; T cell activation; leukocyte migration; endochondral ossification; chondrocyte differentiation.
- **Cell Ontology (suggested):** B cell; T cell; CD4-positive T cell; CD8-positive T cell; thymocyte; natural killer cell; chondrocyte; hypertrophic chondrocyte; neuron.

## 7. Anatomical Structures Affected

### 7.1 Organ/system involvement (supported)
- **Central nervous system / neurodevelopment:** developmental delay, intellectual disability, hypotonia. (barry2022fromgenotypeto pages 1-2, lee2024geneticandphenotypic pages 1-2)
- **Immune system:** recurrent infections, hypogammaglobulinemia, autoimmune cytopenias. (margot2020immunopathologicalmanifestationsin pages 1-2)
- **Cardiovascular system:** congenital heart abnormalities (e.g., ASD, VSD, coarctation). (lee2024geneticandphenotypic pages 1-2)
- **Auditory system:** mixed conductive and sensorineural hearing loss. (kalinousky2023kmt2ddeficiencycauses pages 5-7)
- **Skeletal system / growth plates:** growth deficiency and altered long-bone and growth-plate parameters (mouse models; mechanistic relevance). (gao2024growthdeficiencyin pages 3-6)

### 7.2 UBERON / GO-CC suggestions (not asserted as extracted identifiers)
- UBERON (suggested): heart; cochlea; thymus; bone growth plate; hippocampus
- GO cellular component (suggested): nucleus; chromatin; histone methyltransferase complex

## 8. Temporal Development

### 8.1 Typical onset
KS is congenital with early-life hypotonia and developmental delay emphasized in diagnostic criteria. (adam2019kabukisyndromeinternational pages 1-2)

### 8.2 Hearing temporal profile (example)
In a KS1 cohort, mean onset/presentation of hearing loss was reported as ~7 years, though some individuals had hearing loss at birth. (kalinousky2023kmt2ddeficiencycauses pages 5-7)

## 9. Inheritance and Population

### 9.1 Inheritance patterns
- KS1 (KMT2D): autosomal dominant. (barry2022fromgenotypeto pages 1-2, dugan2021kabukisyndrome pages 1-3)
- KS2 (KDM6A): X-linked; recent cohort work suggests sex-modified severity. (wang2024sexspecificdifferencein pages 2-4, wang2024sexspecificdifferencein pages 5-6)

### 9.2 Sex-specific severity in KS2 (2024 matched case–control)
In a KS2 cohort (n=12; males=5, females=7):
- CHD: **5/5 (100%) males vs 1/7 (14.29%) females** (P=0.015)
- Moderate-to-severe intellectual disability (IQ<55): **4/4 (100%) assessed males vs 0/7 females** (P=0.003)
- Median IQ: **41** in males vs **69** in females (P=0.029)
(Wang et al., 2024, *BMC Pediatrics*, Feb 2024; DOI URL: https://doi.org/10.1186/s12887-024-04562-z). (wang2024sexspecificdifferencein pages 5-6)

## 10. Diagnostics

### 10.1 Clinical criteria and confirmatory testing
The consensus criteria emphasize hypotonia and developmental delay/intellectual disability plus either a pathogenic/likely pathogenic variant in KMT2D/KDM6A and/or typical dysmorphism. (adam2019kabukisyndromeinternational pages 1-2)

### 10.2 Genetic testing (real-world implementation)
Recent reviews describe clinical implementation of **WES/trio-WES** and targeted sequencing to detect SNVs/indels and CNVs, with interpretive challenges including VUS and complex variant classes. (golden2023molecularinsightsof pages 9-11)

### 10.3 Epigenomic “episignature” as a diagnostic adjunct
DNA methylation episignatures are described as capable of identifying KS1 “regardless of variant class” in a review context, supporting clinical adoption of episignature testing when sequence findings are equivocal. (golden2023molecularinsightsof pages 9-11)

### 10.4 Differential diagnosis
This run did not retrieve differential-diagnosis tables or guideline-style differential lists; therefore no specific differentials are asserted here.

## 11. Outcome / Prognosis

The retrieved sources emphasize variable multisystem burden and the need for longitudinal adult natural history data, but did not provide robust survival or life-expectancy statistics in the extracted passages. (barry2022fromgenotypeto pages 1-2)

However, immune complications can be serious: immunopathological manifestations are described as “common and can be life-threatening,” supporting systematic screening and preventive management. (margot2020immunopathologicalmanifestationsin pages 1-2)

## 12. Treatment

### 12.1 Standard of care (current practice)
Clinical management is primarily **supportive and multidisciplinary**, including surveillance and treatment of congenital anomalies, developmental interventions, and management of immune dysfunction, feeding problems, endocrine issues, and seizures as they arise. (dugan2021kabukisyndrome pages 1-3, boniel2021kabukisyndrome—clinicalreview pages 1-2)

### 12.2 Dietary/metabolic interventions (recent developments and real-world implementation)

#### 12.2.1 2024 multi-omics + Modified Atkins/ketogenic diet report (KMT2D)
A 2024 eBioMedicine study combined proteomics (KS n=4 vs controls n=4; significant protein changes at FDR<0.05) and scRNA-seq with a **single-patient** Modified Atkins/ketogenic-style dietary intervention.

Molecular findings included large-scale proteomic dysregulation and downregulation of ribosomal proteins/translation pathways in KS, with partial reversal of ribosomal gene dysregulation after 12 months of diet in the treated participant. (tsang2024ketogenicdietmodifies pages 8-10, tsang2024ketogenicdietmodifies pages 6-8)

Reported clinical signals in the treated child included elimination of “brain fog” episodes, improved neuropsychological testing domains (e.g., attention/impulse control), reduced school absenteeism (8.5→3 days/semester), and reduced antibiotic courses (8.5/year→3.7/year), though this is uncontrolled n=1 evidence. (tsang2024ketogenicdietmodifies pages 8-10)

Intervention details included initial carbohydrate restriction to 15 g/day, ketosis tracking with urinary ketones and serum beta-hydroxybutyrate (BOHB ~1.90–4.86 mmol/L). (tsang2024ketogenicdietmodifies pages 2-3)

**Evidence type:** n=1 intervention with supporting multi-omics; hypothesis-generating. (tsang2024ketogenicdietmodifies pages 8-10, tsang2024ketogenicdietmodifies pages 2-3)

#### 12.2.2 ClinicalTrials.gov: Modified Atkins Diet trial (adults; completed)
A single-group early phase 1 trial evaluated **12-week Modified Atkins Diet** in adults with genetically confirmed KS.
- ClinicalTrials.gov ID: **NCT04722315**
- Status: **Completed**
- Enrollment: **10**
- Primary completion: **2024-01-26**
- Results posted: **2025-05-13**
- Outcome domains: cognitive/visuospatial/memory testing plus serial genome-wide DNA methylation measures. (NCT04722315 chunk 1)

URL: https://clinicaltrials.gov/study/NCT04722315 (NCT04722315 chunk 1)

**Note:** numeric outcome results were not extracted from the record text available in this run. (NCT04722315 chunk 1)

### 12.3 MAXO term suggestions (treatment action structuring)
- Multidisciplinary care coordination
- Genetic counseling
- Developmental therapy (speech therapy; physical therapy; occupational therapy)
- Dietary therapy (Modified Atkins diet / ketogenic diet)
- Immunologic monitoring and management (screening for hypogammaglobulinemia; management of autoimmune cytopenias)

## 13. Prevention

Primary prevention (preventing occurrence) is not generally applicable for a de novo-dominant/X-linked congenital syndrome; however, secondary/tertiary prevention through surveillance and complication prevention is implied in management frameworks and supported by high rates of infection susceptibility and immune abnormalities. (margot2020immunopathologicalmanifestationsin pages 1-2, dugan2021kabukisyndrome pages 1-3)

## 14. Other Species / Natural Disease

No naturally occurring non-human Kabuki syndrome cases were retrieved in this run.

## 15. Model Organisms

### 15.1 Mouse models (key recent 2023–2024 studies)
- **KS1 hearing model:** Kmt2d+/βGeo mice show progressive hearing impairment; ABR thresholds diverge after hearing onset and DPOAEs are diminished at multiple frequencies, consistent with outer hair cell dysfunction despite no gross cochlear malformations on micro-CT. (kalinousky2023kmt2ddeficiencycauses pages 7-9)
- **KS2 growth model:** Kdm6a tm1d/+ mice exhibit postnatal growth deficiency with shortened long bones and growth-plate hypertrophic-zone reductions; Kdm6a−/− and Kmt2d−/− chondrocyte models show convergent transcriptomic changes. (gao2024growthdeficiencyin pages 3-6)
- **Cell-type chromatin comparisons:** ATAC-seq across neurons vs B/T cells demonstrates cell-context-specific chromatin disruptions (neuronal CpG-island/aging enrichment), informing translational interpretation of blood-derived episignatures. (boukas2024neuronspecificchromatindisruption pages 1-2)

## 16. Recent Developments (2023–2024 highlights)

1. **Human epigenomic profiling in KS PBMCs** links KMT2D haploinsufficiency to enhancer dysregulation at immune genes, with super-enhancer overlap (~31%) and metabolic gene upregulation. (Jung et al., 2023; https://doi.org/10.1101/2022.10.25.22280882). (jung2023characterizingthemolecular pages 1-5)
2. **T-cell intrinsic mechanism** in KS: KMT2D control of leukocyte integrins and migration/egress programs, with corroborating human peripheral T-cell shifts (reduced naïve/RTE, expanded memory). (Potter et al., 2024; https://doi.org/10.3389/fimmu.2024.1341745). (potter2024kmt2dregulatesactivation pages 14-16, potter2024kmt2dregulatesactivation pages 1-2)
3. **Neuron-specific chromatin disruption** suggests mechanistic differences across tissues and cautions in interpreting blood episignatures mechanistically for neurodevelopment. (Boukas et al., 2024; https://doi.org/10.1101/gr.278416.123). (boukas2024neuronspecificchromatindisruption pages 1-2)
4. **KS2 skeletal mechanism and convergence with KS1** via shared chondrocyte differentiation programs and growth-plate pathology. (Gao et al., 2024; https://doi.org/10.1371/journal.pgen.1011310). (gao2024growthdeficiencyin pages 3-6)
5. **Dietary intervention translational efforts**: 2024 multi-omics report linking ribosomal protein dysregulation to KMT2D KS and describing Modified Atkins/ketogenic diet-associated molecular and cognitive changes (hypothesis-generating) plus an adult MAD clinical trial completed (NCT04722315). (tsang2024ketogenicdietmodifies pages 8-10, NCT04722315 chunk 1)

## 17. Notes on evidence gaps for this run
- **ICD-10/ICD-11, MeSH, Orphanet identifiers** were not present in retrieved sources; they should be added from dedicated ontology resources (Orphanet/MeSH/ICD) in a follow-on extraction step.
- **Survival/life expectancy statistics** were not captured in the extracted evidence; robust natural history cohorts would be needed.
- **Differential diagnosis lists** and **standardized care pathways** were not extracted in this run.



References

1. (barry2022fromgenotypeto pages 1-2): Kelly K. Barry, Michaelangelo Tsaparlis, Deborah Hoffman, Deborah Hartman, Margaret P. Adam, Christina Hung, and Olaf A. Bodamer. From genotype to phenotype—a review of kabuki syndrome. Genes, 13:1761, Sep 2022. URL: https://doi.org/10.3390/genes13101761, doi:10.3390/genes13101761. This article has 72 citations.

2. (dugan2021kabukisyndrome pages 1-3): Sarah Dugan. Kabuki syndrome. Cassidy and Allanson's Management of Genetic Syndromes, pages 529-538, Oct 2021. URL: https://doi.org/10.1002/9781119432692.ch34, doi:10.1002/9781119432692.ch34. This article has 152 citations.

3. (boniel2021kabukisyndrome—clinicalreview pages 1-2): Snir Boniel, Krystyna Szymańska, Robert Śmigiel, and Krzysztof Szczałuba. Kabuki syndrome—clinical review with molecular aspects. Genes, 12:468, Mar 2021. URL: https://doi.org/10.3390/genes12040468, doi:10.3390/genes12040468. This article has 121 citations.

4. (barry2022fromgenotypeto pages 2-4): Kelly K. Barry, Michaelangelo Tsaparlis, Deborah Hoffman, Deborah Hartman, Margaret P. Adam, Christina Hung, and Olaf A. Bodamer. From genotype to phenotype—a review of kabuki syndrome. Genes, 13:1761, Sep 2022. URL: https://doi.org/10.3390/genes13101761, doi:10.3390/genes13101761. This article has 72 citations.

5. (golden2023molecularinsightsof pages 1-3): Carly S. Golden, Saylor Williams, and Maria A. Serrano. Molecular insights of kmt2d and clinical aspects of kabuki syndrome type 1. Birth Defects Research, 115:1809-1824, May 2023. URL: https://doi.org/10.1002/bdr2.2183, doi:10.1002/bdr2.2183. This article has 10 citations and is from a peer-reviewed journal.

6. (golden2023molecularinsightsof pages 9-11): Carly S. Golden, Saylor Williams, and Maria A. Serrano. Molecular insights of kmt2d and clinical aspects of kabuki syndrome type 1. Birth Defects Research, 115:1809-1824, May 2023. URL: https://doi.org/10.1002/bdr2.2183, doi:10.1002/bdr2.2183. This article has 10 citations and is from a peer-reviewed journal.

7. (wang2024sexspecificdifferencein pages 2-4): Yirou Wang, Yufei Xu, Yao Chen, Yabin Hu, Qun Li, Shijian Liu, Jian Wang, and Xiumin Wang. Sex-specific difference in phenotype of kabuki syndrome type 2 patients: a matched case-control study. BMC Pediatrics, Feb 2024. URL: https://doi.org/10.1186/s12887-024-04562-z, doi:10.1186/s12887-024-04562-z. This article has 2 citations and is from a peer-reviewed journal.

8. (adam2019kabukisyndromeinternational pages 1-2): Margaret P Adam, Siddharth Banka, Hans T Bjornsson, Olaf Bodamer, Albert E Chudley, Jaqueline Harris, Hiroshi Kawame, Brendan C Lanpher, Andrew W Lindsley, Giuseppe Merla, Noriko Miyake, Nobuhiko Okamoto, Constanze T Stumpel, and Norio Niikawa. Kabuki syndrome: international consensus diagnostic criteria. Journal of Medical Genetics, 56:89-95, Dec 2019. URL: https://doi.org/10.1136/jmedgenet-2018-105625, doi:10.1136/jmedgenet-2018-105625. This article has 272 citations and is from a domain leading peer-reviewed journal.

9. (boniel2021kabukisyndrome—clinicalreview pages 8-9): Snir Boniel, Krystyna Szymańska, Robert Śmigiel, and Krzysztof Szczałuba. Kabuki syndrome—clinical review with molecular aspects. Genes, 12:468, Mar 2021. URL: https://doi.org/10.3390/genes12040468, doi:10.3390/genes12040468. This article has 121 citations.

10. (jung2023characterizingthemolecular pages 1-5): Youngsook L Jung, Christina Hung, Jaejoon Choi, Eunjung A Lee, and Olaf Bodamer. Characterizing the molecular impact of kmt2d variants on the epigenetic and transcriptional landscapes in kabuki syndrome. Human molecular genetics, Oct 2023. URL: https://doi.org/10.1101/2022.10.25.22280882, doi:10.1101/2022.10.25.22280882. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (boniel2021kabukisyndrome—clinicalreview pages 2-3): Snir Boniel, Krystyna Szymańska, Robert Śmigiel, and Krzysztof Szczałuba. Kabuki syndrome—clinical review with molecular aspects. Genes, 12:468, Mar 2021. URL: https://doi.org/10.3390/genes12040468, doi:10.3390/genes12040468. This article has 121 citations.

12. (tsang2024ketogenicdietmodifies pages 8-10): Erica Tsang, Velda X. Han, Chloe Flutter, Sarah Alshammery, Brooke A. Keating, Tracey Williams, Brian S. Gloss, Mark E. Graham, Nader Aryamanesh, Ignatius Pang, Melanie Wong, David Winlaw, Michael Cardamone, Shekeeb Mohammad, Wendy Gold, Shrujna Patel, and Russell C. Dale. Ketogenic diet modifies ribosomal protein dysregulation in kmt2d kabuki syndrome. eBioMedicine, 104:105156, Jun 2024. URL: https://doi.org/10.1016/j.ebiom.2024.105156, doi:10.1016/j.ebiom.2024.105156. This article has 16 citations and is from a peer-reviewed journal.

13. (tsang2024ketogenicdietmodifies pages 2-3): Erica Tsang, Velda X. Han, Chloe Flutter, Sarah Alshammery, Brooke A. Keating, Tracey Williams, Brian S. Gloss, Mark E. Graham, Nader Aryamanesh, Ignatius Pang, Melanie Wong, David Winlaw, Michael Cardamone, Shekeeb Mohammad, Wendy Gold, Shrujna Patel, and Russell C. Dale. Ketogenic diet modifies ribosomal protein dysregulation in kmt2d kabuki syndrome. eBioMedicine, 104:105156, Jun 2024. URL: https://doi.org/10.1016/j.ebiom.2024.105156, doi:10.1016/j.ebiom.2024.105156. This article has 16 citations and is from a peer-reviewed journal.

14. (lee2024geneticandphenotypic pages 1-2): Chung-Lin Lee, Chih-Kuang Chuang, Ming-Ren Chen, Ju-Li Lin, Huei-Ching Chiu, Ya-Hui Chang, Yuan-Rong Tu, Yun-Ting Lo, Hsiang-Yu Lin, and Shuan-Pei Lin. Genetic and phenotypic spectrum of kmt2d variants in taiwanese case series of kabuki syndrome. Diagnostics, 14:1815, Aug 2024. URL: https://doi.org/10.3390/diagnostics14161815, doi:10.3390/diagnostics14161815. This article has 0 citations.

15. (margot2020immunopathologicalmanifestationsin pages 1-2): Henri Margot, Guilaine Boursier, Claire Duflos, Elodie Sanchez, Jeanne Amiel, Jean-Christophe Andrau, Stéphanie Arpin, Elise Brischoux-Boucher, Odile Boute, Lydie Burglen, Charlotte Caille, Yline Capri, Patrick Collignon, Solène Conrad, Valérie Cormier-Daire, Geoffroy Delplancq, Klaus Dieterich, Hélène Dollfus, Mélanie Fradin, Laurence Faivre, Helder Fernandes, Christine Francannet, Vincent Gatinois, Marion Gerard, Alice Goldenberg, Jamal Ghoumid, Sarah Grotto, Anne-Marie Guerrot, Agnès Guichet, Bertrand Isidor, Marie-Line Jacquemont, Sophie Julia, Philippe Khau Van Kien, Marine Legendre, K.H. Le Quan Sang, Bruno Leheup, Stanislas Lyonnet, Virginie Magry, Sylvie Manouvrier, Dominique Martin, Godelieve Morel, Arnold Munnich, Sophie Naudion, Sylvie Odent, Laurence Perrin, Florence Petit, Nicole Philip, Marlène Rio, Julie Robbe, Massimiliano Rossi, Elisabeth Sarrazin, Annick Toutain, Julien Van Gils, Gabriella Vera, Alain Verloes, Sacha Weber, Sandra Whalen, Damien Sanlaville, Didier Lacombe, Nathalie Aladjidi, and David Geneviève. Immunopathological manifestations in kabuki syndrome: a registry study of 177 individuals. Genetics in Medicine, 22:181-188, Jan 2020. URL: https://doi.org/10.1038/s41436-019-0623-x, doi:10.1038/s41436-019-0623-x. This article has 73 citations and is from a highest quality peer-reviewed journal.

16. (kalinousky2023kmt2ddeficiencycauses pages 5-7): Allison J. Kalinousky, Teresa R. Luperchio, Katrina M. Schrode, Jacqueline R. Harris, Li Zhang, Valerie B. DeLeon, Jill A. Fahrner, Amanda M. Lauer, and Hans T. Bjornsson. Kmt2d deficiency causes sensorineural hearing loss in mice and humans. Genes, 15:48, Dec 2023. URL: https://doi.org/10.3390/genes15010048, doi:10.3390/genes15010048. This article has 2 citations.

17. (lee2024geneticandphenotypic pages 6-7): Chung-Lin Lee, Chih-Kuang Chuang, Ming-Ren Chen, Ju-Li Lin, Huei-Ching Chiu, Ya-Hui Chang, Yuan-Rong Tu, Yun-Ting Lo, Hsiang-Yu Lin, and Shuan-Pei Lin. Genetic and phenotypic spectrum of kmt2d variants in taiwanese case series of kabuki syndrome. Diagnostics, 14:1815, Aug 2024. URL: https://doi.org/10.3390/diagnostics14161815, doi:10.3390/diagnostics14161815. This article has 0 citations.

18. (lee2024geneticandphenotypic pages 4-6): Chung-Lin Lee, Chih-Kuang Chuang, Ming-Ren Chen, Ju-Li Lin, Huei-Ching Chiu, Ya-Hui Chang, Yuan-Rong Tu, Yun-Ting Lo, Hsiang-Yu Lin, and Shuan-Pei Lin. Genetic and phenotypic spectrum of kmt2d variants in taiwanese case series of kabuki syndrome. Diagnostics, 14:1815, Aug 2024. URL: https://doi.org/10.3390/diagnostics14161815, doi:10.3390/diagnostics14161815. This article has 0 citations.

19. (wang2024sexspecificdifferencein pages 5-6): Yirou Wang, Yufei Xu, Yao Chen, Yabin Hu, Qun Li, Shijian Liu, Jian Wang, and Xiumin Wang. Sex-specific difference in phenotype of kabuki syndrome type 2 patients: a matched case-control study. BMC Pediatrics, Feb 2024. URL: https://doi.org/10.1186/s12887-024-04562-z, doi:10.1186/s12887-024-04562-z. This article has 2 citations and is from a peer-reviewed journal.

20. (lee2024geneticandphenotypic pages 2-4): Chung-Lin Lee, Chih-Kuang Chuang, Ming-Ren Chen, Ju-Li Lin, Huei-Ching Chiu, Ya-Hui Chang, Yuan-Rong Tu, Yun-Ting Lo, Hsiang-Yu Lin, and Shuan-Pei Lin. Genetic and phenotypic spectrum of kmt2d variants in taiwanese case series of kabuki syndrome. Diagnostics, 14:1815, Aug 2024. URL: https://doi.org/10.3390/diagnostics14161815, doi:10.3390/diagnostics14161815. This article has 0 citations.

21. (potter2024kmt2dregulatesactivation pages 1-2): Sarah J. Potter, Li Zhang, Michael Kotliar, Yuehong Wu, Caitlin Schafer, Kurtis Stefan, Leandros Boukas, Dima Qu’d, Olaf Bodamer, Brittany N. Simpson, Artem Barski, Andrew W. Lindsley, and Hans T. Bjornsson. Kmt2d regulates activation, localization, and integrin expression by t-cells. Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1341745, doi:10.3389/fimmu.2024.1341745. This article has 10 citations and is from a peer-reviewed journal.

22. (potter2024kmt2dregulatesactivation pages 9-11): Sarah J. Potter, Li Zhang, Michael Kotliar, Yuehong Wu, Caitlin Schafer, Kurtis Stefan, Leandros Boukas, Dima Qu’d, Olaf Bodamer, Brittany N. Simpson, Artem Barski, Andrew W. Lindsley, and Hans T. Bjornsson. Kmt2d regulates activation, localization, and integrin expression by t-cells. Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1341745, doi:10.3389/fimmu.2024.1341745. This article has 10 citations and is from a peer-reviewed journal.

23. (potter2024kmt2dregulatesactivation pages 14-16): Sarah J. Potter, Li Zhang, Michael Kotliar, Yuehong Wu, Caitlin Schafer, Kurtis Stefan, Leandros Boukas, Dima Qu’d, Olaf Bodamer, Brittany N. Simpson, Artem Barski, Andrew W. Lindsley, and Hans T. Bjornsson. Kmt2d regulates activation, localization, and integrin expression by t-cells. Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1341745, doi:10.3389/fimmu.2024.1341745. This article has 10 citations and is from a peer-reviewed journal.

24. (boukas2024neuronspecificchromatindisruption pages 1-2): Leandros Boukas, Teresa Romeo Luperchio, Afrooz Razi, Kasper D. Hansen, and Hans T. Bjornsson. Neuron-specific chromatin disruption at cpg islands and aging-related regions in kabuki syndrome mice. Genome Research, 34:696-710, May 2024. URL: https://doi.org/10.1101/gr.278416.123, doi:10.1101/gr.278416.123. This article has 3 citations and is from a highest quality peer-reviewed journal.

25. (gao2024growthdeficiencyin pages 1-2): Christine W. Gao, WanYing Lin, Ryan C. Riddle, Sheetal Chopra, Jiyoung Kim, Leandros Boukas, Kasper D. Hansen, Hans T. Björnsson, and Jill A. Fahrner. Growth deficiency in a mouse model of kabuki syndrome 2 bears mechanistic similarities to kabuki syndrome 1. PLOS Genetics, 20:e1011310, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011310, doi:10.1371/journal.pgen.1011310. This article has 3 citations and is from a domain leading peer-reviewed journal.

26. (gao2024growthdeficiencyin pages 3-6): Christine W. Gao, WanYing Lin, Ryan C. Riddle, Sheetal Chopra, Jiyoung Kim, Leandros Boukas, Kasper D. Hansen, Hans T. Björnsson, and Jill A. Fahrner. Growth deficiency in a mouse model of kabuki syndrome 2 bears mechanistic similarities to kabuki syndrome 1. PLOS Genetics, 20:e1011310, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011310, doi:10.1371/journal.pgen.1011310. This article has 3 citations and is from a domain leading peer-reviewed journal.

27. (NCT04722315 chunk 1):  Study of Modified Atkins Diet in Kabuki Syndrome. Hugo W. Moser Research Institute at Kennedy Krieger, Inc.. 2021. ClinicalTrials.gov Identifier: NCT04722315

28. (potter2024kmt2dregulatesactivation pages 11-13): Sarah J. Potter, Li Zhang, Michael Kotliar, Yuehong Wu, Caitlin Schafer, Kurtis Stefan, Leandros Boukas, Dima Qu’d, Olaf Bodamer, Brittany N. Simpson, Artem Barski, Andrew W. Lindsley, and Hans T. Bjornsson. Kmt2d regulates activation, localization, and integrin expression by t-cells. Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1341745, doi:10.3389/fimmu.2024.1341745. This article has 10 citations and is from a peer-reviewed journal.

29. (tsang2024ketogenicdietmodifies pages 6-8): Erica Tsang, Velda X. Han, Chloe Flutter, Sarah Alshammery, Brooke A. Keating, Tracey Williams, Brian S. Gloss, Mark E. Graham, Nader Aryamanesh, Ignatius Pang, Melanie Wong, David Winlaw, Michael Cardamone, Shekeeb Mohammad, Wendy Gold, Shrujna Patel, and Russell C. Dale. Ketogenic diet modifies ribosomal protein dysregulation in kmt2d kabuki syndrome. eBioMedicine, 104:105156, Jun 2024. URL: https://doi.org/10.1016/j.ebiom.2024.105156, doi:10.1016/j.ebiom.2024.105156. This article has 16 citations and is from a peer-reviewed journal.

30. (kalinousky2023kmt2ddeficiencycauses pages 7-9): Allison J. Kalinousky, Teresa R. Luperchio, Katrina M. Schrode, Jacqueline R. Harris, Li Zhang, Valerie B. DeLeon, Jill A. Fahrner, Amanda M. Lauer, and Hans T. Bjornsson. Kmt2d deficiency causes sensorineural hearing loss in mice and humans. Genes, 15:48, Dec 2023. URL: https://doi.org/10.3390/genes15010048, doi:10.3390/genes15010048. This article has 2 citations.