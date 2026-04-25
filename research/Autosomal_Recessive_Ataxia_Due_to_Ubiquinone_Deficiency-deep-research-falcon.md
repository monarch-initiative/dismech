---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-23T18:35:35.550082'
end_time: '2026-04-23T18:44:18.220317'
duration_seconds: 522.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Ataxia Due to Ubiquinone Deficiency
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Ataxia Due to Ubiquinone Deficiency
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Ataxia Due to Ubiquinone Deficiency** covering all of the
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
- **Disease Name:** Autosomal Recessive Ataxia Due to Ubiquinone Deficiency
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Ataxia Due to Ubiquinone Deficiency** covering all of the
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


# Comprehensive Research Report: Autosomal Recessive Ataxia Due to Ubiquinone (Coenzyme Q10) Deficiency (COQ8A-ataxia / COQ10D4)

## Executive summary
Autosomal recessive ataxia due to ubiquinone deficiency most commonly refers to **COQ8A-related primary coenzyme Q10 deficiency-4 (COQ10D4)**, an autosomal recessive, potentially treatable mitochondrial disorder in which impaired CoQ10 (ubiquinone) homeostasis leads to predominantly cerebellar neurodegeneration with variable multisystem involvement. Cohort data show universal cerebellar atrophy and common epilepsy/cognitive impairment, slow-to-moderate ataxia progression (~0.45 SARA points/year), and **~43%** reported clinical response to CoQ10 supplementation in the largest multicenter cohort, supporting the rationale for early identification and treatment. (traschutz2020clinico‐geneticimagingand pages 2-2, traschutz2020clinico‐geneticimagingand pages 8-9, traschutz2020clinico‐geneticimagingand pages 9-9)

## 1. Disease information
### 1.1 Definition and current understanding
COQ8A-ataxia is a form of **primary coenzyme Q10 (CoQ10; ubiquinone) deficiency** caused by biallelic pathogenic variants in **COQ8A** (aka **ADCK3**, **CABC1**) and is considered among the “mitochondrial ataxias” because CoQ10 is required for efficient mitochondrial electron transfer and cellular redox homeostasis. (paprocka2022coq8aataxiaasa pages 1-2, lopriore2024primarycoenzymeq10 pages 1-2)

### 1.2 Key identifiers and controlled vocabulary
* **OMIM:** **612016** (COQ8A-related ARCA2/SCAR9/COQ10D4). (lopriore2024primarycoenzymeq10 pages 2-4, shalata2019primarycoenzymeq pages 1-2, hura2022lossofdrosophila pages 1-2)
* **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not found in the retrieved primary/review texts used as evidence here.

### 1.3 Synonyms and alternative names
Reported synonyms include:
* **Primary coenzyme Q10 deficiency-4** (COQ10D4) (paprocka2022coq8aataxiaasa pages 1-2)
* **COQ8A-ataxia** (paprocka2022coq8aataxiaasa pages 1-2)
* **Autosomal recessive cerebellar ataxia 2 (ARCA2)** (paprocka2022coq8aataxiaasa pages 1-2)
* **Autosomal recessive spinocerebellar ataxia-9 (SCAR9)** (paprocka2022coq8aataxiaasa pages 1-2)
* **Primary coenzyme Q10 deficiency / ubiquinone deficiency with cerebellar ataxia** (paprocka2022coq8aataxiaasa pages 2-4)

### 1.4 Evidence provenance (patient-level vs aggregated resources)
Most clinically actionable information is derived from **aggregated disease-level resources** (multicenter cohort studies and reviews) plus **individual case reports** used to expand phenotype and treatment-response variability. (traschutz2020clinico‐geneticimagingand pages 2-2, paprocka2022coq8aataxiaasa pages 1-2)

| Disease/entity label | Key synonyms/alternative names reported in evidence | Identifier mapping from gathered evidence | Causal gene(s) and gene synonyms | Inheritance | Main supporting source(s) year | URL | Evidence citation |
|---|---|---|---|---|---|---|---|
| COQ8A-related primary coenzyme Q10 deficiency | COQ8A-ataxia; primary coenzyme Q10 deficiency-4; COQ10D4; autosomal recessive cerebellar ataxia 2 (ARCA2); autosomal recessive spinocerebellar ataxia-9 (SCAR9); primary ubiquinone deficiency / ubiquinone deficiency with cerebellar ataxia | MONDO: autosomal recessive ataxia due to ubiquinone deficiency = **MONDO_0012784** (Open Targets association evidence in prior tool output); OMIM: **612016**; Orphanet: not found in gathered evidence; MeSH: not found in gathered evidence; ICD-10/ICD-11: not found in gathered evidence | **COQ8A**; gene synonyms: **ADCK3**, **CABC1** | Autosomal recessive / recessive | 2024; 2022; 2019; 2022 | https://doi.org/10.3390/jcm13082391 ; https://doi.org/10.3390/metabo12100955 ; https://doi.org/10.1007/s11064-019-02786-5 ; https://doi.org/10.1186/s13041-022-00900-3 | (lopriore2024primarycoenzymeq10 pages 2-4, paprocka2022coq8aataxiaasa pages 1-2, shalata2019primarycoenzymeq pages 1-2, hura2022lossofdrosophila pages 1-2) |
| Primary coenzyme Q10 deficiency-related ataxias (broader disease group containing COQ8A-related disease) | Primary coenzyme Q10 deficiency-related ataxias; PCoQD-related ataxia; primary coenzyme Q10 deficiency (PCoQD); primary ubiquinone deficiency | MONDO: not specified in gathered paper evidence for the broader group; OMIM: not specified for the broader group in gathered evidence; Orphanet: not found in gathered evidence; MeSH: not found in gathered evidence; ICD-10/ICD-11: not found in gathered evidence | Multiple recessive CoQ biosynthesis genes reported in evidence, including **COQ8A**, **COQ4**, **COQ2**, **COQ6**, **COQ7**, **COQ9**, **PDSS1**, **PDSS2**, **COQ5**; explicit gene synonym reported for COQ8A: **ADCK3** | Recessive / autosomal recessive | 2024; 2024 | https://doi.org/10.3390/jcm13082391 ; https://doi.org/10.1212/nxg.0000000000200209 | (lopriore2024primarycoenzymeq10 pages 1-2, wahedi2024clinicalfeaturesbiochemistry pages 1-2, lopriore2024primarycoenzymeq10 pages 4-6) |
| COQ8A-related ataxia as autosomal-recessive cerebellar ataxia type 2 | ARCA2; SCAR9; COQ8A-related ataxia; COQ8A-ataxia | OMIM: **612016**; MONDO/Orphanet/MeSH/ICD: not found in gathered paper evidence for this synonym set | **COQ8A** (also known as **ADCK3**; **CABC1**) | Autosomal recessive | 2024; 2019 | https://doi.org/10.3390/jcm13082391 ; https://doi.org/10.1007/s11064-019-02786-5 | (lopriore2024primarycoenzymeq10 pages 2-4, shalata2019primarycoenzymeq pages 1-2) |


*Table: This table summarizes the disease names, synonyms, identifiers, causal genes, and inheritance patterns found in the gathered evidence for autosomal recessive ataxia due to ubiquinone deficiency / COQ8A-related primary coenzyme Q10 deficiency. It also flags identifier systems that were not found in the available evidence, which is useful for knowledge-base curation.*

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause (genetic):** biallelic pathogenic variants in **COQ8A** impair regulation of CoQ10 biosynthesis, causing CoQ10 deficiency and downstream mitochondrial dysfunction. (paprocka2022coq8aataxiaasa pages 1-2, shalata2019primarycoenzymeq pages 1-2)

**Causal chain (high-level):** COQ8A dysfunction → reduced/abnormal CoQ10 homeostasis (ubiquinone/ubiquinol pool) → impaired electron transfer and oxidative phosphorylation + altered redox buffering → selective vulnerability of cerebellar circuitry (Purkinje system and dentate-related pathways) → progressive cerebellar syndrome (ataxia, dysarthria, tremor) ± multisystem features. (paprocka2022coq8aataxiaasa pages 1-2, traschutz2020clinico‐geneticimagingand pages 2-2)

### 2.2 Risk factors
* **Genetic risk factor:** autosomal recessive inheritance; risk is highest in offspring of two carriers. (paprocka2022coq8aataxiaasa pages 2-4, lopriore2024primarycoenzymeq10 pages 2-4)
* **Environmental risk factors:** not identified in the retrieved evidence.

### 2.3 Protective factors
No definitive genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not described in the retrieved evidence.

## 3. Phenotypes
### 3.1 Core neurologic phenotype (with frequencies)
In the largest multicenter cohort (n=59), COQ8A-ataxia is an early-onset multisystemic cerebellar syndrome with these key frequencies:
* **Cerebellar ataxia / cerebellar syndrome:** cerebellar atrophy was reported as **universal (100%)** on MRI in the cohort. (traschutz2020clinico‐geneticimagingand pages 2-2)
* **Epilepsy:** **32%**. (traschutz2020clinico‐geneticimagingand pages 2-2)
* **Cognitive impairment:** **49%**. (traschutz2020clinico‐geneticimagingand pages 2-2)
* **Exercise intolerance:** **25%**. (traschutz2020clinico‐geneticimagingand pages 2-2)
* **Hyperkinetic movement disorders:** **41%** (including dystonia and myoclonus). (traschutz2020clinico‐geneticimagingand pages 2-2)

A review synthesis further supports frequent cognitive involvement (~50%) and epilepsy/myopathic features (~25%) across reported cohorts and highlights phenotypic diversity and slow progression. (lopriore2024primarycoenzymeq10 pages 4-6)

### 3.2 Age of onset, severity, and progression
* Age at onset is often pediatric; cohort/review summaries report “50% of patients affected before age 6 years.” (traschutz2020clinico‐geneticimagingand pages 9-9)
* Natural history in the multicenter cohort showed slow progression:
  * Cross-sectional estimate: “median ataxia progression rate of **0.47 SARA points per year**.” (traschutz2020clinico‐geneticimagingand pages 8-9)
  * Longitudinal drug-naïve estimate: “mean annualized change of **0.45 SARA points per year** (95% CI: 0.12–0.77).” (traschutz2020clinico‐geneticimagingand pages 8-9)

### 3.3 Quality of life / function
Disease severity is commonly tracked by clinical scales (SARA, SDFS). In the cohort, the SDFS anchors included: “**SDFS 3 reflects moderate ataxia with the inability to run, and SDFS 6 reflects wheelchair dependence**.” (traschutz2020clinico‐geneticimagingand pages 9-9)

### 3.4 Suggested HPO terms (non-exhaustive)
* Cerebellar ataxia (HP:0001251)
* Cerebellar atrophy (HP:0001272)
* Dysarthria (HP:0001260)
* Tremor (HP:0001337)
* Dystonia (HP:0001332)
* Myoclonus (HP:0001336)
* Seizures (HP:0001250)
* Intellectual disability (HP:0001249)
* Exercise intolerance (HP:0003546)

## 4. Genetic/molecular information
### 4.1 Causal gene(s)
**COQ8A** (synonyms: **ADCK3**, **CABC1**) is the main causal gene referenced for the ataxia phenotype. (paprocka2022coq8aataxiaasa pages 1-2, hura2022lossofdrosophila pages 1-2)

### 4.2 Variant types and genotype–phenotype information
In the n=59 cohort, there were “44 pathogenic variants (18 novel),” and multisystem involvement was more frequent with missense vs biallelic loss-of-function variants (“82–93% vs 53%; p = 0.029”). (traschutz2020clinico‐geneticimagingand pages 2-2)

A 2024 review describes broader accumulated experience: “Over 120 patients and 75 pathogenic variants have been reported,” and proposes that biallelic loss-of-function variants tend to cause more cerebellar-limited disease while biallelic missense variants are more often multisystemic. (lopriore2024primarycoenzymeq10 pages 4-6)

### 4.3 Suggested molecular ontology terms
* **GO biological process (suggested):** coenzyme Q biosynthetic process; mitochondrial electron transport; oxidative phosphorylation
* **GO cellular component (suggested):** mitochondrion; inner mitochondrial membrane

(These are ontology suggestions; the mechanistic assertions above are supported by the cited disease literature.)

## 5. Environmental information
No disease-specific environmental triggers/toxins/lifestyle modifiers were identified in the retrieved evidence.

## 6. Mechanism / pathophysiology
### 6.1 Pathway-level mechanism
A recent clinical review defines primary coenzyme Q10 deficiency as due to recessive mutations in CoQ biosynthetic pathway genes and emphasizes that these disorders are “potentially treatable,” making timely diagnosis critical. (lopriore2024primarycoenzymeq10 pages 1-2)

### 6.2 Tissue damage mechanisms
The clinical phenotype (cerebellar neurodegeneration with atrophy and dentate-related signal changes in subsets) is consistent with mitochondrial/metabolic vulnerability of cerebellar systems; the cohort reports cerebellar atrophy as universal and notes dentate/pontine T2 changes in a subset (28%). (traschutz2020clinico‐geneticimagingand pages 2-2)

### 6.3 Suggested cell-type (CL) and anatomy (UBERON) terms
* **CL (suggested):** Purkinje cell (cerebellar Purkinje neuron)
* **UBERON (suggested):** cerebellum; cerebellar hemisphere; dentate nucleus

## 7. Anatomical structures affected
**Primary:** cerebellum (atrophy universal on MRI in the multicenter cohort). (traschutz2020clinico‐geneticimagingand pages 2-2)

**Additional CNS involvement:** cerebral atrophy or dentate/pontine T2 signal changes were reported in 28% in the same cohort. (traschutz2020clinico‐geneticimagingand pages 2-2)

## 8. Temporal development
### 8.1 Onset
Often childhood onset; cohort data indicate 50% before age 6. (traschutz2020clinico‐geneticimagingand pages 9-9)

### 8.2 Progression
Slow progression on SARA (~0.45/year) in longitudinal drug-naïve analysis. (traschutz2020clinico‐geneticimagingand pages 8-9)

### 8.3 Critical periods
The treatment literature emphasizes the clinical importance of **early diagnosis and treatment** to avoid irreversible tissue damage and improve outcomes. (lopriore2024primarycoenzymeq10 pages 1-2, wahedi2024clinicalfeaturesbiochemistry pages 1-2)

## 9. Inheritance and population
### 9.1 Inheritance
Autosomal recessive inheritance is consistently reported. (paprocka2022coq8aataxiaasa pages 2-4, lopriore2024primarycoenzymeq10 pages 2-4)

### 9.2 Epidemiology
Prevalence is **not established** in the retrieved evidence; one review states that prevalence is unknown and summarizes reported cases internationally. (paprocka2022coq8aataxiaasa pages 1-2)

## 10. Diagnostics
### 10.1 Clinical and biochemical testing
A key diagnostic point from a clinical review is that **tissue-specific CoQ10 deficiency may not be reflected in serum**:
* “**measurement of ubiquinone in a muscle biopsy remains the gold standard test**” (paprocka2022coq8aataxiaasaa pages 5-7)
* “**serum CoQ10 may be within the normal range**” and normal skin fibroblast levels do not exclude muscle deficiency. (paprocka2022coq8aataxiaasaa pages 5-7)

The 2024 single-center cohort of primary CoQ10 biosynthesis disorders (n=14) describes multi-tissue biochemical evaluation and monitoring and highlights the lack of a single pathognomonic biomarker: “**there are no pathognomonic blood, muscle, or imaging biomarkers of these diseases**.” (wahedi2024clinicalfeaturesbiochemistry pages 1-2)

### 10.2 Genetic testing
Diagnosis is established by identifying biallelic pathogenic variants in COQ8A; NGS approaches (gene panels, exome/genome sequencing) are commonly used in practice, especially given the phenotypic overlap with other hereditary ataxias and mitochondrial disorders. (paprocka2022coq8aataxiaasaa pages 5-7, wahedi2024clinicalfeaturesbiochemistry pages 1-2)

### 10.3 Imaging
Brain MRI frequently shows cerebellar atrophy and may show additional dentate/pontine or supratentorial changes. (traschutz2020clinico‐geneticimagingand pages 2-2, paprocka2022coq8aataxiaasaa pages 5-7)

### 10.4 Differential diagnosis (high-level)
Because CoQ10-deficient ataxia can be primary (biosynthetic genes) or secondary (other mitochondrial/neurologic genes), genetic testing is important to distinguish COQ8A-related disease from other recessive ataxias and mitochondrial disorders. (lopriore2024primarycoenzymeq10 pages 1-2)

## 11. Outcomes / prognosis
### 11.1 Neurologic prognosis
Typically slowly progressive based on SARA progression rates. (traschutz2020clinico‐geneticimagingand pages 8-9)

### 11.2 Severe early-onset phenotypes in the broader CoQ10 biosynthesis disorder spectrum
In a pediatric cohort spanning multiple CoQ10 biosynthesis genes (n=14), “**3 children with neonatal-onset neurologic disease died in early childhood despite receiving high-dose oral CoQ10 from birth**,” underscoring that prognosis can be poor for neonatal/infantile neurologic presentations even with early therapy (not specific to COQ8A alone). (wahedi2024clinicalfeaturesbiochemistry pages 1-2)

## 12. Treatment
### 12.1 Pharmacotherapy: Coenzyme Q10 (ubiquinone) supplementation
**Clinical rationale:** CoQ10 supplementation is the main disease-directed therapy; COQ8A-ataxia is widely regarded as potentially treatable, motivating early recognition. (paprocka2022coq8aataxiaasa pages 1-2)

**Dose ranges reported (literature synthesis):** “high-dose oral coenzyme Q10 … dosing ranging from **5 to 50 mg/kg/day**” (review synthesis). (lopriore2024primarycoenzymeq10 pages 7-8)

**Cohort dosing and response (largest multicenter cohort, n=59):**
* Treatment use: “**Thirty patients (51%) were treated with CoQ10 supplementation**” with “**mean cumulative daily dose of 11 mg/kg/day**.” (traschutz2020clinico‐geneticimagingand pages 8-9)
* Clinical response classification among treated patients: “**13 of 30 patients (43%) were classified as responders, and 15 of 30 (50%) as nonresponders**.” (traschutz2020clinico‐geneticimagingand pages 9-9)
* Quantitative longitudinal effect estimate under treatment: “**Annual change in SARA score … showed an average improvement of −0.88 points per year** (95% CI: −1.95 to 0.19) under CoQ10 treatment.” (traschutz2020clinico‐geneticimagingand pages 10-10)

**Expert interpretation:** The same cohort authors stress that controlled trials are still needed and provide trial-readiness statistics, including that “**48 patients per trial arm would be required to detect a 50% reduction in annual SARA progression**.” (traschutz2020clinico‐geneticimagingand pages 8-9)

### 12.2 Management in the broader primary CoQ10 biosynthesis disorder group (important real-world implementation)
The 2024 single-center pediatric cohort suggests that high doses may be required for neurologic benefit: “**oral doses of CoQ10 up to 70 mg/kg/d were needed to ameliorate neurologic features**.” (wahedi2024clinicalfeaturesbiochemistry pages 1-2)

The same study highlights renal benefit with early treatment in CoQ10 biosynthesis disorders: early diagnosis and treatment (30 mg/kg/day) “**can reverse renal manifestations and can completely prevent kidney disease over 10 years of follow-up**.” (wahedi2024clinicalfeaturesbiochemistry pages 1-2)

### 12.3 Seizure-directed adjuncts
In the CoQ10 biosynthesis cohort, “**Additional idebenone was required to control seizures in some cases**.” (wahedi2024clinicalfeaturesbiochemistry pages 1-2)

### 12.4 Supportive/rehabilitative therapy
Not quantified in the retrieved evidence; however, the standard of care for hereditary ataxias generally includes multidisciplinary rehabilitation and symptomatic management.

### 12.5 Suggested MAXO terms
* Coenzyme Q10 supplementation (MAXO term suggestion)
* Genetic counseling (MAXO term suggestion)
* Physical therapy / occupational therapy / speech therapy (MAXO term suggestions)

### 12.6 Clinical trials
No clearly relevant interventional clinical trials were retrieved via the provided ClinicalTrials search query (“COQ8A AND (coenzyme Q10 OR ubiquinone OR idebenone)”) in this run.

## 13. Prevention
### 13.1 Primary prevention
No primary prevention measures are established for COQ8A-ataxia beyond reproductive counseling.

### 13.2 Secondary prevention
Secondary prevention is centered on **early diagnosis** (genome-wide or panel-based testing in unexplained ataxia/mitochondrial phenotypes), enabling earlier CoQ10 treatment initiation. (wahedi2024clinicalfeaturesbiochemistry pages 1-2)

### 13.3 Counseling
Genetic counseling is appropriate for autosomal recessive inheritance and cascade testing in families. (paprocka2022coq8aataxiaasa pages 2-4)

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs were identified in the retrieved evidence.

## 15. Model organisms
A Drosophila model provides in vivo evidence linking COQ8A/Coq8 function to survival and neural integrity. The abstract states: “**Mutations in COQ8A in humans result in CoQ10 deficiency (OMIM: 612,016)**,” and the model showed locomotor deficits and photoreceptor degeneration with Coq8 knockdown. (hura2022lossofdrosophila pages 1-2)

## Recent developments and latest research emphasis (2023–2024)
* **2024 cohort study (Neurology Genetics, Dec 2024):** provides contemporary real-world dosing/monitoring insights across CoQ10 biosynthesis disorders, emphasizing that high-dose CoQ10 may be necessary and that early therapy can prevent kidney disease in some genotypes/phenotypes; it also stresses the lack of pathognomonic biomarkers and the need for early genome-wide diagnosis. (wahedi2024clinicalfeaturesbiochemistry pages 1-2)
  * Direct abstract quote: “**oral doses of CoQ10 up to 70 mg/kg/d were needed to ameliorate neurologic features**.” (wahedi2024clinicalfeaturesbiochemistry pages 1-2)
  * Direct abstract quote: “**there are no pathognomonic blood, muscle, or imaging biomarkers of these diseases**.” (wahedi2024clinicalfeaturesbiochemistry pages 1-2)
* **2024 disease-focused review (J Clin Med, Apr 2024):** synthesizes genotype–phenotype patterns and highlights >120 known patients/75 pathogenic variants, reinforcing clinical heterogeneity and the treatability rationale. (lopriore2024primarycoenzymeq10 pages 4-6)

## Evidence gaps for knowledge-base completion
* **Orphanet, MeSH, ICD-10/ICD-11 identifiers** were not present in the retrieved evidence segments.
* **MONDO ID** was not present in the retrieved papers; mapping will require consultation of ontology databases directly (e.g., MONDO/Orphanet).
* Environmental/lifestyle modifiers and gene–environment interaction evidence were not identified in the retrieved sources.

## Key source URLs and publication dates (from retrieved evidence)
* Traschütz A et al. *Annals of Neurology* (Jun 2020). https://doi.org/10.1002/ana.25751 (traschutz2020clinico‐geneticimagingand pages 2-2)
* Wahedi A et al. *Neurology Genetics* (Dec 2024). https://doi.org/10.1212/nxg.0000000000200209 (wahedi2024clinicalfeaturesbiochemistry pages 1-2)
* Lopriore P et al. *Journal of Clinical Medicine* (Apr 2024). https://doi.org/10.3390/jcm13082391 (lopriore2024primarycoenzymeq10 pages 4-6)
* Paprocka J et al. *Metabolites* (Oct 2022). https://doi.org/10.3390/metabo12100955 (paprocka2022coq8aataxiaasa pages 1-2)
* Shalata A et al. *Neurochemical Research* (Apr 2019). https://doi.org/10.1007/s11064-019-02786-5 (shalata2019primarycoenzymeq pages 1-2)
* Hura AJ et al. *Molecular Brain* (Feb 2022). https://doi.org/10.1186/s13041-022-00900-3 (hura2022lossofdrosophila pages 1-2)


References

1. (traschutz2020clinico‐geneticimagingand pages 2-2): Andreas Traschütz, Tommaso Schirinzi, Lucia Laugwitz, Nathan H. Murray, Craig A. Bingman, Selina Reich, Jan Kern, Anna Heinzmann, Gessica Vasco, Enrico Bertini, Ginevra Zanni, Alexandra Durr, Stefania Magri, Franco Taroni, Alessandro Malandrini, Jonathan Baets, Peter de Jonghe, Willem de Ridder, Matthieu Bereau, Stephanie Demuth, Christos Ganos, A. Nazli Basak, Hasmet Hanagasi, Semra Hiz Kurul, Benjamin Bender, Ludger Schöls, Ute Grasshoff, Thomas Klopstock, Rita Horvath, Bart van de Warrenburg, Lydie Burglen, Christelle Rougeot, Claire Ewenczyk, Michel Koenig, Filippo M. Santorelli, Mathieu Anheim, Renato P. Munhoz, Tobias Haack, Felix Distelmaier, David J. Pagliarini, Hélène Puccio, and Matthis Synofzik. Clinico‐genetic, imaging and molecular delineation of <scp><i>coq8a</i></scp>‐ataxia: a multicenter study of 59 patients. Annals of Neurology, 88:251-263, Jun 2020. URL: https://doi.org/10.1002/ana.25751, doi:10.1002/ana.25751. This article has 81 citations and is from a highest quality peer-reviewed journal.

2. (traschutz2020clinico‐geneticimagingand pages 8-9): Andreas Traschütz, Tommaso Schirinzi, Lucia Laugwitz, Nathan H. Murray, Craig A. Bingman, Selina Reich, Jan Kern, Anna Heinzmann, Gessica Vasco, Enrico Bertini, Ginevra Zanni, Alexandra Durr, Stefania Magri, Franco Taroni, Alessandro Malandrini, Jonathan Baets, Peter de Jonghe, Willem de Ridder, Matthieu Bereau, Stephanie Demuth, Christos Ganos, A. Nazli Basak, Hasmet Hanagasi, Semra Hiz Kurul, Benjamin Bender, Ludger Schöls, Ute Grasshoff, Thomas Klopstock, Rita Horvath, Bart van de Warrenburg, Lydie Burglen, Christelle Rougeot, Claire Ewenczyk, Michel Koenig, Filippo M. Santorelli, Mathieu Anheim, Renato P. Munhoz, Tobias Haack, Felix Distelmaier, David J. Pagliarini, Hélène Puccio, and Matthis Synofzik. Clinico‐genetic, imaging and molecular delineation of <scp><i>coq8a</i></scp>‐ataxia: a multicenter study of 59 patients. Annals of Neurology, 88:251-263, Jun 2020. URL: https://doi.org/10.1002/ana.25751, doi:10.1002/ana.25751. This article has 81 citations and is from a highest quality peer-reviewed journal.

3. (traschutz2020clinico‐geneticimagingand pages 9-9): Andreas Traschütz, Tommaso Schirinzi, Lucia Laugwitz, Nathan H. Murray, Craig A. Bingman, Selina Reich, Jan Kern, Anna Heinzmann, Gessica Vasco, Enrico Bertini, Ginevra Zanni, Alexandra Durr, Stefania Magri, Franco Taroni, Alessandro Malandrini, Jonathan Baets, Peter de Jonghe, Willem de Ridder, Matthieu Bereau, Stephanie Demuth, Christos Ganos, A. Nazli Basak, Hasmet Hanagasi, Semra Hiz Kurul, Benjamin Bender, Ludger Schöls, Ute Grasshoff, Thomas Klopstock, Rita Horvath, Bart van de Warrenburg, Lydie Burglen, Christelle Rougeot, Claire Ewenczyk, Michel Koenig, Filippo M. Santorelli, Mathieu Anheim, Renato P. Munhoz, Tobias Haack, Felix Distelmaier, David J. Pagliarini, Hélène Puccio, and Matthis Synofzik. Clinico‐genetic, imaging and molecular delineation of <scp><i>coq8a</i></scp>‐ataxia: a multicenter study of 59 patients. Annals of Neurology, 88:251-263, Jun 2020. URL: https://doi.org/10.1002/ana.25751, doi:10.1002/ana.25751. This article has 81 citations and is from a highest quality peer-reviewed journal.

4. (paprocka2022coq8aataxiaasa pages 1-2): Justyna Paprocka, Magdalena Nowak, Piotr Chuchra, and Robert Śmigiel. Coq8a-ataxia as a manifestation of primary coenzyme q deficiency. Metabolites, 12:955, Oct 2022. URL: https://doi.org/10.3390/metabo12100955, doi:10.3390/metabo12100955. This article has 18 citations.

5. (lopriore2024primarycoenzymeq10 pages 1-2): Piervito Lopriore, Marco Vista, Alessandra Tessa, Martina Giuntini, Elena Caldarazzo Ienco, Michelangelo Mancuso, Gabriele Siciliano, Filippo Maria Santorelli, and Daniele Orsucci. Primary coenzyme q10 deficiency-related ataxias. Journal of Clinical Medicine, 13:2391, Apr 2024. URL: https://doi.org/10.3390/jcm13082391, doi:10.3390/jcm13082391. This article has 7 citations.

6. (lopriore2024primarycoenzymeq10 pages 2-4): Piervito Lopriore, Marco Vista, Alessandra Tessa, Martina Giuntini, Elena Caldarazzo Ienco, Michelangelo Mancuso, Gabriele Siciliano, Filippo Maria Santorelli, and Daniele Orsucci. Primary coenzyme q10 deficiency-related ataxias. Journal of Clinical Medicine, 13:2391, Apr 2024. URL: https://doi.org/10.3390/jcm13082391, doi:10.3390/jcm13082391. This article has 7 citations.

7. (shalata2019primarycoenzymeq pages 1-2): Adel Shalata, Michael Edery, Clair Habib, Jacob Genizi, Mohammad Mahroum, Lama Khalaily, Nurit Assaf, Idan Segal, Hoda Abed El Rahim, Hana Shapira, Danielle Urian, Shay Tzur, Liza Douiev, and Ann Saada. Primary coenzyme q deficiency due to novel adck3 variants, studies in fibroblasts and review of literature. Neurochemical Research, 44:2372-2384, Apr 2019. URL: https://doi.org/10.1007/s11064-019-02786-5, doi:10.1007/s11064-019-02786-5. This article has 24 citations and is from a peer-reviewed journal.

8. (hura2022lossofdrosophila pages 1-2): Angelia J. Hura, Hannah R. Hawley, Wei Jun Tan, Rebecca J. Penny, Jessie C. Jacobsen, and Helen L. Fitzsimons. Loss of drosophila coq8 results in impaired survival, locomotor deficits and photoreceptor degeneration. Molecular Brain, Feb 2022. URL: https://doi.org/10.1186/s13041-022-00900-3, doi:10.1186/s13041-022-00900-3. This article has 6 citations and is from a peer-reviewed journal.

9. (paprocka2022coq8aataxiaasa pages 2-4): Justyna Paprocka, Magdalena Nowak, Piotr Chuchra, and Robert Śmigiel. Coq8a-ataxia as a manifestation of primary coenzyme q deficiency. Metabolites, 12:955, Oct 2022. URL: https://doi.org/10.3390/metabo12100955, doi:10.3390/metabo12100955. This article has 18 citations.

10. (wahedi2024clinicalfeaturesbiochemistry pages 1-2): Azizia Wahedi, Sniya Sudhakar, Amanda Lam, Jose Ignacio Rodriguez Ciancio, Philippa Mills, Paul Gissen, Alice Gardham, Jogesh Kapadia, Jane Hassell, Simon Heales, and Shamima Rahman. Clinical features, biochemistry, imaging, and treatment response in a single-center cohort with coenzyme q <sub>10</sub> biosynthesis disorders. Neurology Genetics, Dec 2024. URL: https://doi.org/10.1212/nxg.0000000000200209, doi:10.1212/nxg.0000000000200209. This article has 5 citations.

11. (lopriore2024primarycoenzymeq10 pages 4-6): Piervito Lopriore, Marco Vista, Alessandra Tessa, Martina Giuntini, Elena Caldarazzo Ienco, Michelangelo Mancuso, Gabriele Siciliano, Filippo Maria Santorelli, and Daniele Orsucci. Primary coenzyme q10 deficiency-related ataxias. Journal of Clinical Medicine, 13:2391, Apr 2024. URL: https://doi.org/10.3390/jcm13082391, doi:10.3390/jcm13082391. This article has 7 citations.

12. (paprocka2022coq8aataxiaasaa pages 5-7): J Paprocka, M Nowak, P Chuchra, and R Smigiel. Coq8a-ataxia as a manifestation of primary coenzyme q deficiency. metabolites 2022; 12: 955. Unknown journal, 2022.

13. (lopriore2024primarycoenzymeq10 pages 7-8): Piervito Lopriore, Marco Vista, Alessandra Tessa, Martina Giuntini, Elena Caldarazzo Ienco, Michelangelo Mancuso, Gabriele Siciliano, Filippo Maria Santorelli, and Daniele Orsucci. Primary coenzyme q10 deficiency-related ataxias. Journal of Clinical Medicine, 13:2391, Apr 2024. URL: https://doi.org/10.3390/jcm13082391, doi:10.3390/jcm13082391. This article has 7 citations.

14. (traschutz2020clinico‐geneticimagingand pages 10-10): Andreas Traschütz, Tommaso Schirinzi, Lucia Laugwitz, Nathan H. Murray, Craig A. Bingman, Selina Reich, Jan Kern, Anna Heinzmann, Gessica Vasco, Enrico Bertini, Ginevra Zanni, Alexandra Durr, Stefania Magri, Franco Taroni, Alessandro Malandrini, Jonathan Baets, Peter de Jonghe, Willem de Ridder, Matthieu Bereau, Stephanie Demuth, Christos Ganos, A. Nazli Basak, Hasmet Hanagasi, Semra Hiz Kurul, Benjamin Bender, Ludger Schöls, Ute Grasshoff, Thomas Klopstock, Rita Horvath, Bart van de Warrenburg, Lydie Burglen, Christelle Rougeot, Claire Ewenczyk, Michel Koenig, Filippo M. Santorelli, Mathieu Anheim, Renato P. Munhoz, Tobias Haack, Felix Distelmaier, David J. Pagliarini, Hélène Puccio, and Matthis Synofzik. Clinico‐genetic, imaging and molecular delineation of <scp><i>coq8a</i></scp>‐ataxia: a multicenter study of 59 patients. Annals of Neurology, 88:251-263, Jun 2020. URL: https://doi.org/10.1002/ana.25751, doi:10.1002/ana.25751. This article has 81 citations and is from a highest quality peer-reviewed journal.