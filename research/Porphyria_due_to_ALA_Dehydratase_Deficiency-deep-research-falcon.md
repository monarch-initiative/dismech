---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T02:36:37.568796'
end_time: '2026-05-05T02:50:19.701143'
duration_seconds: 822.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Porphyria due to ALA Dehydratase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Porphyria due to ALA Dehydratase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Porphyria due to ALA Dehydratase Deficiency** covering all of the
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
- **Disease Name:** Porphyria due to ALA Dehydratase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Porphyria due to ALA Dehydratase Deficiency** covering all of the
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


## Comprehensive research report: Porphyria due to ALA Dehydratase Deficiency (ALAD deficiency porphyria; ADP; Doss porphyria)

### Executive summary
Porphyria due to ALA dehydratase deficiency (ADP) is an ultra-rare, autosomal recessive acute hepatic porphyria caused by biallelic pathogenic variants in **ALAD** (also called **porphobilinogen synthase, PBGS**), leading to profound deficiency of ALA dehydratase—the second enzyme in heme biosynthesis. The most characteristic biochemical pattern is **markedly elevated δ-aminolevulinic acid (ALA)** with **porphobilinogen (PBG) normal or only slightly elevated**, plus increased urinary coproporphyrins and erythrocyte zinc protoporphyrin. Clinically it presents with **acute neurovisceral attacks** (severe abdominal pain, autonomic symptoms, and peripheral neuropathy/weakness) without typical cutaneous features. Evidence-based 2023 expert guidance for acute hepatic porphyrias highlights that **PBG is elevated in all acute hepatic porphyrias except ALAD porphyria**, which has important diagnostic implications. First-line management is shared with other acute hepatic porphyrias (trigger avoidance, carbohydrate loading, and IV hemin), but emerging therapies (e.g., givosiran) may be less effective in ADP based on limited case-level evidence. (wang2023agaclinicalpractice pages 1-3, wang2023agaclinicalpractice pages 3-5, graff2022casereportlack pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
ADP is an inborn error of heme biosynthesis classified among **acute hepatic porphyrias (AHPs)**. It results from a **severe deficiency of 5-aminolevulinic acid dehydratase (ALAD)**, causing accumulation of upstream heme precursors—especially **ALA**—and episodic, potentially severe **neurovisceral attacks**. (ramanujam2015porphyriadiagnostics—part1 pages 9-11, wang2023agaclinicalpractice pages 1-3)

### 1.2 Key identifiers (available from retrieved evidence)
- **OMIM:** **612740** (explicitly reported in peer-reviewed sources). (graff2022casereportlack pages 1-2, ramanujam2015porphyriadiagnostics—part1 pages 9-11)
- **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** not directly retrievable from the captured evidence set in this run; therefore not reported here to avoid uncited/incorrect identifiers.

### 1.3 Common synonyms / alternative names
- **ALAD deficiency porphyria (ADP)**
- **ALAD porphyria**
- **ALA dehydratase deficiency porphyria**
- **Doss porphyria** (ramanujam2015porphyriadiagnostics—part1 pages 9-11)

### 1.4 Evidence source type
Most ADP knowledge is derived from:
- **Aggregated disease-level expert reviews and guidelines** (e.g., AGA Clinical Practice Update for AHPs). (wang2023agaclinicalpractice pages 1-3)
- **A very small number of individual human cases/longitudinal follow-up studies** due to extreme rarity. (gross19985aminolevulinicaciddehydratase pages 1-2, doss2004thethirdcase pages 1-4)

---

## 2. Etiology

### 2.1 Primary causal factors
- **Genetic cause:** biallelic pathogenic variants in **ALAD** leading to profound enzyme deficiency. ADP is described as **autosomal recessive**, with affected individuals typically **compound heterozygotes**; heterozygous carriers (~50% activity) are usually asymptomatic. (ramanujam2015porphyriadiagnostics—part1 pages 9-11, gross19985aminolevulinicaciddehydratase pages 1-2)
- **Mechanistic cause:** deficiency of ALAD blocks conversion of **2 ALA → PBG**, leading to **ALA accumulation** and downstream porphyrin abnormalities. (balogun2023thehepaticporphyrias pages 3-5, graff2022casereportlack pages 1-2)

### 2.2 Risk factors / triggers
Evidence across ADP-focused reviews/cases indicates that ALAD activity can be reduced by genetic deficiency or **secondary inhibition**, creating an ADP-like biochemical/clinical picture:
- **Lead exposure:** ALAD is zinc-dependent and susceptible to inactivation when lead replaces Zn2+. (balogun2023thehepaticporphyrias pages 3-5, ramanujam2015porphyriadiagnostics—part1 pages 9-11)
- **Hereditary tyrosinemia type 1:** via succinylacetone-mediated ALAD inhibition (noted as a differential/secondary cause in ADP-focused review). (ramanujam2015porphyriadiagnostics—part1 pages 9-11)
- **Alcohol ingestion:** associated with at least one severe attack in long-term follow-up; alcohol can increase hepatic ALAS activity and precipitate crises. (gross19985aminolevulinicaciddehydratase pages 4-5, gross19985aminolevulinicaciddehydratase pages 2-3)
- Other conditions listed as potential contributors to reduced ALAD activity / ADP-like biochemical patterns include **zinc deficiency, smoking, diabetes, and chronic renal failure**. (ramanujam2015porphyriadiagnostics—part1 pages 9-11)

### 2.3 Protective factors
No ADP-specific protective genetic variants or environmental protective factors were identified in the captured evidence set.

### 2.4 Gene–environment interaction
A practical, clinically relevant interaction is **carrier status + lead exposure**: heterozygotes with partial ALAD activity are generally asymptomatic but may have increased susceptibility to lead toxicity. (ramanujam2015porphyriadiagnostics—part1 pages 9-11)

---

## 3. Phenotypes

### 3.1 Core phenotype types and characteristics
**Symptoms/signs (neurovisceral attacks):**
- Severe **abdominal pain** (often colicky) during acute crises. (doss2004thethirdcase pages 1-4)
- **Peripheral neuropathy / weakness**, including polyneuropathy and potentially persistent deficits (e.g., paresis; “foot and wrist drop” reported in a chronic course). (graff2022casereportlack pages 1-2, gross19985aminolevulinicaciddehydratase pages 1-2)
- Autonomic/cardiovascular involvement reported in long-term follow-up (“cardiovascular symptoms”). (gross19985aminolevulinicaciddehydratase pages 1-2)
- Severe crises can include **transient respiratory paralysis** / respiratory involvement. (gross19985aminolevulinicaciddehydratase pages 1-2)

**Onset / course:**
- Typically **childhood to adolescence** in reported cases; one longitudinal case began at age 12 and continued into adulthood with recurrent attacks. (graff2022casereportlack pages 1-2, gross19985aminolevulinicaciddehydratase pages 1-2)
- The disorder is so rare that phenotype frequency estimates are not robust; older reviews emphasized extremely small case counts (≈6–8 cases worldwide). (ramanujam2015porphyriadiagnostics—part1 pages 9-11, graff2022casereportlack pages 1-2)

**Cutaneous findings:**
- ADP is described as presenting with neurovisceral symptoms similar to other acute porphyrias **without cutaneous manifestations** in classic descriptions. (ramanujam2015porphyriadiagnostics—part1 pages 9-11)

### 3.2 Suggested HPO terms (non-exhaustive; based on reported features)
- Abdominal pain **HP:0002027**
- Peripheral neuropathy **HP:0009830**
- Muscle weakness **HP:0001324**
- Paresis **HP:0003470**
- Respiratory insufficiency / failure **HP:0002878 / HP:0002877**

### 3.3 Quality of life impact
Direct ADP-specific QoL instruments were not captured in the evidence set; however, the described recurrent attacks and persistent neuropathic deficits imply major functional impairment in some individuals (case-level evidence). (graff2022casereportlack pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **ALAD** (porphobilinogen synthase; PBGS), located at **chromosome 9q34** in classic reviews, encoding a zinc-dependent enzyme catalyzing the condensation of two ALA molecules to form PBG. (ramanujam2015porphyriadiagnostics—part1 pages 9-11, balogun2023thehepaticporphyrias pages 3-5)

### 4.2 Example pathogenic variants (illustrative; not comprehensive)
**From an ADP case report (2022):**
- **c.265G>A (p.Glu89Lys)** and **c.394T>C (p.Cys132Arg)** in ALAD. (graff2022casereportlack pages 1-2)

**From a 2004 genetically characterized case:**
- Compound heterozygous **intronic substitutions** in intron 3 (IVS3 -11C substitutions), proposed to alter splicing. (doss2004thethirdcase pages 1-4)

**From 2024 functional characterization (conference poster):**
- Newly reported variants in three young patients including **c.440_441delinsTT (reported to yield p.Arg147Leu)** (homozygous in siblings) and **compound heterozygosity for c.839G>A (p.Gly280Glu) and c.724G>A (p.Val242Ile)**; in vivo hepatocyte expression in C57BL/6 mice showed ~**5%** wild-type activity for one variant. (castelbon202404163functionalcharacterization pages 1-1)

**Protein dysfunction concepts:**
- A 2023 hepatic porphyria review describes ADP as a “conformational disease,” with mutations causing destabilized tertiary/quaternary structure, misfolding, and reduced half-life; it also reiterates lead’s displacement of Zn2+ leading to inactivation. (balogun2023thehepaticporphyrias pages 3-5)

### 4.3 Variant classes
Across reports: missense, small indels, and intronic/splice-affecting variants are represented. (graff2022casereportlack pages 1-2, doss2004thethirdcase pages 1-4, castelbon202404163functionalcharacterization pages 1-1)

### 4.4 Modifier genes / epigenetics
No ADP-specific modifier genes or epigenetic changes were identified in the captured evidence set.

---

## 5. Environmental information

### 5.1 Environmental contributors
- **Lead** is the key environmental factor: it inhibits ALAD by replacing zinc and can mimic ADP. (balogun2023thehepaticporphyrias pages 3-5, ramanujam2015porphyriadiagnostics—part1 pages 9-11)

### 5.2 Lifestyle contributors
- **Alcohol** may precipitate attacks (case-level evidence). (gross19985aminolevulinicaciddehydratase pages 4-5, gross19985aminolevulinicaciddehydratase pages 2-3)

### 5.3 Infectious agents
No infectious etiology is implicated.

---

## 6. Mechanism / pathophysiology

### 6.1 Molecular pathway (heme biosynthesis)
ALAD is the second enzyme in heme biosynthesis and catalyzes the condensation of two ALA molecules to form PBG. Deficiency leads to **ALA accumulation** and characteristic downstream porphyrin abnormalities. (balogun2023thehepaticporphyrias pages 3-5, graff2022casereportlack pages 1-2)

### 6.2 Causal chain (conceptual)
1) **Biallelic ALAD pathogenic variants → profound enzyme deficiency** in relevant tissues (erythrocytes; and likely hepatic/erythroid contributions). (graff2022casereportlack pages 1-2, ramanujam2015porphyriadiagnostics—part1 pages 9-11)
2) **Block in ALA→PBG step → marked ALA accumulation** (urine/plasma). (doss2004thethirdcase pages 1-4, gross19985aminolevulinicaciddehydratase pages 2-3)
3) Accumulated ALA and altered porphyrin intermediates associate with **acute neurovisceral attacks** and neuropathy. (gross19985aminolevulinicaciddehydratase pages 1-2, graff2022casereportlack pages 1-2)

### 6.3 Biochemical abnormalities (with data)
- **Urinary ALA**: reported **32-fold** elevation in a 17-year-old case; in 20-year follow-up, **44–80 fold** elevations were documented at various times. (doss2004thethirdcase pages 1-4, gross19985aminolevulinicaciddehydratase pages 2-3)
- **Urinary PBG**: normal or slightly elevated in ADP (key differentiator), though some long-term data show PBG elevations during crises; expert guidance emphasizes that PBG is not reliably elevated in ALAD porphyria. (graff2022casereportlack pages 1-2, wang2023agaclinicalpractice pages 3-5, gross19985aminolevulinicaciddehydratase pages 2-3)
- **Urinary coproporphyrins**: e.g., **76-fold** increased coproporphyrin in one case; excessive urinary coproporphyrin excretion in long-term follow-up. (doss2004thethirdcase pages 1-4, gross19985aminolevulinicaciddehydratase pages 4-5)
- **Erythrocyte zinc protoporphyrin**: e.g., **5.4-fold** elevated in one case; noted as increased in case report. (doss2004thethirdcase pages 1-4, graff2022casereportlack pages 1-2)
- **ALAD enzyme activity**: often **<10%** of normal, sustained over decades in follow-up; a 2004 case had **10%** activity. (gross19985aminolevulinicaciddehydratase pages 1-2, doss2004thethirdcase pages 1-4)

### 6.4 Ontology suggestions (for knowledge base population)
- **GO (Biological Process):** heme biosynthetic process; porphyrin-containing compound metabolic process.
- **GO (Molecular Function):** delta-aminolevulinic acid dehydratase activity.
- **UBERON (anatomy):** liver; bone marrow; peripheral nerve.
- **CL (cell types):** hepatocyte; erythroblast/erythroid lineage.

### 6.5 Molecular profiling / multi-omics
No ADP-specific transcriptomic/proteomic/metabolomic multi-omics datasets were identified in the captured evidence set. A 2024 poster used an in vivo hepatocyte expression assay for functional evaluation of variants. (castelbon202404163functionalcharacterization pages 1-1)

---

## 7. Anatomical structures affected
Based on neurovisceral attacks and biochemical production/handling of heme intermediates:
- **Liver (UBERON:0002107)**: central to AHP biochemistry and therapeutic targeting (e.g., ALAS1 suppression strategies). (wang2023agaclinicalpractice pages 1-3, NCT03338816 chunk 1)
- **Peripheral nervous system / peripheral nerves**: neuropathy/weakness and motor deficits are prominent. (graff2022casereportlack pages 1-2, gross19985aminolevulinicaciddehydratase pages 1-2)
- **Blood/erythroid compartment**: erythrocyte ALAD deficiency and zinc protoporphyrin elevation are diagnostic clues. (gross19985aminolevulinicaciddehydratase pages 1-2, graff2022casereportlack pages 1-2)

---

## 8. Temporal development

### 8.1 Onset
- Commonly **childhood/adolescence** in reported cases. (graff2022casereportlack pages 1-2, gross19985aminolevulinicaciddehydratase pages 1-2)

### 8.2 Course
- Can be **episodic** with acute attacks; some cases show **chronic neurologic sequelae** after repeated attacks. (graff2022casereportlack pages 1-2, gross19985aminolevulinicaciddehydratase pages 1-2)

---

## 9. Inheritance and population

### 9.1 Inheritance
- **Autosomal recessive**. (ramanujam2015porphyriadiagnostics—part1 pages 9-11, gross19985aminolevulinicaciddehydratase pages 1-2)

### 9.2 Epidemiology (best available in retrieved evidence)
- Extremely rare: described as only **~6** documented cases in an older authoritative diagnostic review and **~8** documented cases worldwide in a 2022 case report. (ramanujam2015porphyriadiagnostics—part1 pages 9-11, graff2022casereportlack pages 1-2)
- The 2023 AGA expert review notes **fewer than a dozen reported cases**. (wang2023agaclinicalpractice pages 1-3)

### 9.3 Population genetics (carrier frequency / variant distribution)
Not available from the captured evidence set (e.g., gnomAD/ClinVar frequencies were not retrieved in this run).

---

## 10. Diagnostics

### 10.1 Clinical suspicion
Patients can present with recurrent severe abdominal pain and neurologic/autonomic symptoms consistent with acute hepatic porphyria. Because symptoms are nonspecific, expert guidance recommends screening during an attack. (wang2023agaclinicalpractice pages 1-3)

### 10.2 First-line biochemical testing (expert guidance, 2023)
The AGA Clinical Practice Update recommends **random urine ALA and PBG corrected to creatinine** as screening tests in suspected AHP; importantly, it highlights that **PBG is elevated in all AHP except ALAD porphyria**, so an ADP pattern may be **high ALA with absent/minimal PBG elevation**. (wang2023agaclinicalpractice pages 1-3, wang2023agaclinicalpractice pages 3-5)

### 10.3 Second-line / confirmatory testing
- **Porphyrin fractionation** in urine/plasma/feces and erythrocyte porphyrin profiling (e.g., Zn-protoporphyrin) can support subtype differentiation. (pierro2021laboratorydiagnosisof pages 12-13)
- **Erythrocyte ALAD enzyme activity assay**: diagnostically useful but pre-analytically sensitive—ALAD activity deteriorates rapidly; testing should be performed within ~24h of blood draw. (pierro2021laboratorydiagnosisof pages 12-13)
- **Genetic confirmation**: sequencing of **ALAD** is used to confirm subtype after biochemical evidence. (wang2023agaclinicalpractice pages 1-3)

### 10.4 Plasma fluorescence scanning
A diagnostics review describes plasma fluorescence scanning as a rapid qualitative screen; **ADP/AIP/HCP** may show emission maxima around **618–622 nm** in symptomatic patients, supporting porphyria-type discrimination. (pierro2021laboratorydiagnosisof pages 2-4)

### 10.5 Differential diagnosis (high priority)
- **Lead poisoning** (acquired ALAD inhibition) is a major mimic and should be excluded with blood lead testing and exposure history. (ramanujam2015porphyriadiagnostics—part1 pages 9-11, balogun2023thehepaticporphyrias pages 3-5)
- **Hereditary tyrosinemia type 1** (succinylacetone ALAD inhibition). (ramanujam2015porphyriadiagnostics—part1 pages 9-11)

---

## 11. Outcomes / prognosis

### 11.1 Morbidity
- Long-term follow-up documents potentially severe morbidity, including persistent paresis and transient respiratory paralysis during crises. (gross19985aminolevulinicaciddehydratase pages 1-2)
- A 2022 ADP case illustrates chronic sequelae (permanent motor deficits) and complications of long-term therapy (iron overload), plus compensated cirrhosis. (graff2022casereportlack pages 2-4)

### 11.2 Survival
- Long-term outcomes vary: two long-followed patients were reported alive and in good health at age ~40 (historic cohort). (gross19985aminolevulinicaciddehydratase pages 4-5)
- One child reportedly died after liver transplantation, and another older adult died within two years of onset in historical summaries. (gross19985aminolevulinicaciddehydratase pages 4-5)

Because of extreme rarity and case ascertainment bias, formal survival rates are not available.

---

## 12. Treatment

### 12.1 Acute attack management and disease-modifying therapy (expert guidance)
The 2023 AGA Clinical Practice Update for AHPs lists cornerstones of management: discontinuation of porphyrinogenic drugs/chemicals, oral/IV dextrose, IV hemin, and symptomatic therapy; for frequent attacks (≥4/year), prophylaxis with IV hemin or subcutaneous givosiran is considered, and liver transplantation is a curative option in refractory cases (general AHP guidance). (wang2023agaclinicalpractice pages 1-3)

### 12.2 Hemin / heme arginate (best-supported for ADP)
Human case data support efficacy:
- A 20-year follow-up reported acute crises “successfully treated” with glucose plus heme arginate, with reductions in urinary ALA and porphyrins and sustained symptom-free periods. (gross19985aminolevulinicaciddehydratase pages 1-2)
- A 2004 case (17-year-old) improved with haem arginate; weekly haem for one year provided sustained biochemical/clinical benefit and appeared prophylactic. (doss2004thethirdcase pages 1-4)

**Adverse effects / implementation issues:**
- Long-term prophylactic hemin can cause **iron overload**; in a 2022 case, ferritin reached 659 ng/mL and was managed with phlebotomy. (graff2022casereportlack pages 1-2)

**MAXO suggestions:** intravenous hemin administration; heme arginate therapy; intravenous glucose administration.

### 12.3 Givosiran (RNAi targeting hepatic ALAS1)
**Clinical trial landscape:**
- The phase 3 **ENVISION trial (NCT03338816)** lists **ALA dehydratase deficient porphyria** among included conditions and measures urinary ALA/PBG and attack rates; however, the excerpted record does not provide numeric results in this evidence set. (NCT03338816 chunk 1)

**ADP-specific real-world evidence:**
- A 2022 ADP case report describes a patient treated with givosiran (2.5 mg/kg monthly) for 6 months with **no observed liver adverse effects**, but **continued recurrent attacks** and only transient ALA decreases associated with hemin infusions; the authors conclude givosiran “may not be effective” for ADP based on this single case. (graff2022casereportlack pages 1-2, graff2022casereportlack pages 2-4)

**Figure-based evidence:** The paper’s Figure 1 shows urine ALA decreases after hemin but lack of sustained suppression with givosiran and persistent elevation of related markers during the treatment interval. (graff2022casereportlack media 69c1e72f, graff2022casereportlack media 97eb2153, graff2022casereportlack media 0a38561c)

**MAXO suggestions:** small interfering RNA therapy; ALAS1 inhibition therapy (mechanism-based).

### 12.4 Hydroxyurea (experimental/repurposed)
A 2022 case report notes hydroxyurea was “beneficial in one previous case” and was planned for the reported patient due to a possible erythropoietic component of ADP, but controlled evidence is lacking. (graff2022casereportlack pages 1-2)

**MAXO suggestion:** hydroxyurea therapy.

### 12.5 Liver transplantation
Historical evidence suggests limited benefit in at least one child with ADP, and expert reviews reserve transplantation for refractory AHP generally. (ramanujam2015porphyriadiagnostics—part1 pages 9-11, wang2023agaclinicalpractice pages 1-3, gross19985aminolevulinicaciddehydratase pages 4-5)

**MAXO suggestion:** liver transplantation.

---

## 13. Prevention

### 13.1 Primary prevention
- Avoid or minimize exposure to **porphyrinogenic drugs/chemicals** (general AHP prevention principle). (wang2023agaclinicalpractice pages 1-3)
- Prevent **lead exposure**, given its direct ALAD inhibition and potential to mimic/precipitate ADP-like crises. (balogun2023thehepaticporphyrias pages 3-5, ramanujam2015porphyriadiagnostics—part1 pages 9-11)

### 13.2 Secondary prevention
- Early biochemical testing during attacks (urine ALA/PBG) to prevent misdiagnosis and delayed hemin therapy. (wang2023agaclinicalpractice pages 1-3)

### 13.3 Tertiary prevention
- For recurrent attacks, consider prophylaxis (e.g., hemin protocols) and monitor treatment complications (iron overload). (graff2022casereportlack pages 1-2)

### 13.4 Genetic counseling
After biochemical diagnosis, confirm by ALAD sequencing and offer cascade testing to relatives for counseling (general AHP approach). (wang2023agaclinicalpractice pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring ADP in other species was identified in the captured evidence set.

---

## 15. Model organisms
A 2024 conference poster reports **in vivo functional characterization** of newly identified ALAD variants by **vector transfer into hepatocytes of C57BL/6 mice using hydrodynamic tail vein injection**, with one variant showing ~5% wild-type enzyme activity. This supports use of mouse liver expression systems for variant functional validation in ADP. (castelbon202404163functionalcharacterization pages 1-1)

---

## Recent developments and latest research (prioritizing 2023–2024)

1) **2023 expert clinical guidance (AGA Clinical Practice Update)** clarified a key diagnostic pitfall: urinary **PBG is elevated in all AHP except ALAD porphyria**, reinforcing the need to measure **ALA and PBG together** and not rely on PBG alone. Publication date: March 2023. URL: https://doi.org/10.1053/j.gastro.2022.11.034 (wang2023agaclinicalpractice pages 3-5, wang2023agaclinicalpractice pages 1-3)

2) **2023 mechanistic synthesis** emphasized ALAD’s Zn2+ dependence and lead susceptibility and framed ADP as a mutation-driven “conformational disease,” connecting structural disruption to enzyme instability/misfolding. Publication date: November 2023. URL: https://doi.org/10.1055/s-0043-1776760 (balogun2023thehepaticporphyrias pages 3-5)

3) **2024 variant discovery + functional validation (conference poster)** reported previously unreported ALAD variants in young patients and used a mouse hepatocyte expression approach for functional assessment, illustrating continued discovery of allelic heterogeneity and translation of variant interpretation methods. Publication date: September 2024. URL: https://doi.org/10.1136/bmjgast-2024-icpp.75 (castelbon202404163functionalcharacterization pages 1-1)

---

## Key statistics and data (from recent/primary studies)
- **Rarity:** “only eight cases documented worldwide” (case report, Aug 2022). (graff2022casereportlack pages 1-2)
- **ALA elevations:** urinary ALA **32-fold** in one genetically confirmed case; **44–80 fold** in long-term follow-up patients at various times. (doss2004thethirdcase pages 1-4, gross19985aminolevulinicaciddehydratase pages 2-3)
- **Enzyme deficiency:** erythrocyte ALAD activity often **<10%** of normal over decades in follow-up. (gross19985aminolevulinicaciddehydratase pages 1-2)
- **Urinary coproporphyrin:** **76-fold** elevation reported in one acute case. (doss2004thethirdcase pages 1-4)

---

## Structured summary table
| Finding | Details | Key source (year; DOI/URL) |
|---|---|---|
| Disease name / identifiers | 5-Aminolevulinic acid dehydratase deficiency porphyria; ALAD deficiency porphyria; ADP; Doss porphyria. OMIM 612740 reported in recent reviews/case reports. Described as the rarest/ultra-rare acute hepatic porphyria (graff2022casereportlack pages 1-2, ramanujam2015porphyriadiagnostics—part1 pages 9-11). | Graff et al., 2022, Front Genet, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2); Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11) |
| Synonyms | ALAD porphyria, ALA dehydratase deficiency porphyria, aminolevulinate dehydratase deficiency porphyria, Doss porphyria (ramanujam2015porphyriadiagnostics—part1 pages 9-11). | Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11) |
| Inheritance | Autosomal recessive; affected patients usually have biallelic/compound heterozygous ALAD variants; heterozygotes have ~50% ALAD activity and are usually asymptomatic (ramanujam2015porphyriadiagnostics—part1 pages 9-11, gross19985aminolevulinicaciddehydratase pages 1-2). | Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 1-2) |
| Causal gene | ALAD (also PBGS), chromosome 9q34; zinc-dependent enzyme catalyzing condensation of 2 ALA molecules to porphobilinogen (PBG) (ramanujam2015porphyriadiagnostics—part1 pages 9-11, balogun2023thehepaticporphyrias pages 3-5). | Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11); Balogun & Nejak-Bowen, 2023, https://doi.org/10.1055/s-0043-1776760 (balogun2023thehepaticporphyrias pages 3-5) |
| Example pathogenic variants | Reported ALAD variants include c.265G>A p.Glu89Lys and c.394T>C p.Cys132Arg; historical/functional examples include K59N, F12L, G133R, R240W, A274T, V275M, delTC; 2024 poster reported c.440_441delinsTT / p.Arg147Leu, c.839G>A / p.Gly280Glu, and c.724G>A / p.Val242Ile (graff2022casereportlack pages 1-2, balogun2023thehepaticporphyrias pages 3-5, castelbon202404163functionalcharacterization pages 1-1). | Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2); Balogun & Nejak-Bowen, 2023, https://doi.org/10.1055/s-0043-1776760 (balogun2023thehepaticporphyrias pages 3-5); Castelbón et al., 2024 poster, https://doi.org/10.1136/bmjgast-2024-icpp.75 (castelbon202404163functionalcharacterization pages 1-1) |
| Key biochemical finding: ALA | Markedly increased urinary/plasma ALA is the hallmark; examples include 32-fold urinary increase in one 17-year-old case, and 44-fold to 80-fold increases in long-term follow-up cases (doss2004thethirdcase pages 1-4, gross19985aminolevulinicaciddehydratase pages 2-3). | Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 1-4); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 2-3) |
| Key biochemical finding: PBG | PBG is normal or only slightly elevated in ADP; this distinguishes ADP from most other acute hepatic porphyrias where PBG is typically elevated (graff2022casereportlack pages 1-2, wang2023agaclinicalpractice pages 3-5, doss2004thethirdcase pages 1-4). | Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2); Wang et al., 2023, https://doi.org/10.1053/j.gastro.2022.11.034 (wang2023agaclinicalpractice pages 3-5); Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 1-4) |
| Key biochemical finding: urinary porphyrins | Urinary coproporphyrin III / coproporphyrin excretion is increased; one case had urinary coproporphyrin increased 76-fold and long-term cases had excessive urinary coproporphyrin excretion (graff2022casereportlack pages 1-2, gross19985aminolevulinicaciddehydratase pages 4-5, doss2004thethirdcase pages 1-4). | Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 4-5); Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 1-4) |
| Key biochemical finding: erythrocyte Zn-protoporphyrin | Erythrocyte zinc protoporphyrin is elevated/markedly increased; one case showed 5.4-fold elevation and case report/review also note increased erythrocyte zinc protoporphyrin (graff2022casereportlack pages 1-2, gross19985aminolevulinicaciddehydratase pages 4-5, doss2004thethirdcase pages 1-4). | Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 4-5); Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 1-4) |
| Key biochemical finding: ALAD activity | Profound ALAD deficiency in erythrocytes/lymphocytes, typically <10% of normal; examples include 10% activity in a 2004 case and <10% activity sustained over 20 years in 2 patients (gross19985aminolevulinicaciddehydratase pages 1-2, doss2004thethirdcase pages 1-4, pierro2021laboratorydiagnosisof pages 12-13). | Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 1-2); Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 1-4); Di Pierro et al., 2021, https://doi.org/10.3390/diagnostics11081343 (pierro2021laboratorydiagnosisof pages 12-13) |
| Hallmark clinical features | Acute neurovisceral attacks with severe abdominal pain, peripheral neuropathy/weakness, polyneuropathy, autonomic/cardiovascular symptoms; can progress to paresis, respiratory paralysis/failure. No cutaneous manifestations are typical (graff2022casereportlack pages 1-2, ramanujam2015porphyriadiagnostics—part1 pages 9-11, gross19985aminolevulinicaciddehydratase pages 1-2, doss2004thethirdcase pages 1-4). | Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2); Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 1-2); Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 1-4) |
| Typical onset / rarity | Usually childhood to adolescence; reported as extremely rare with ~6 cases in older review and ~8 documented worldwide in 2022 case report; historical reports noted all known cases male (graff2022casereportlack pages 1-2, ramanujam2015porphyriadiagnostics—part1 pages 9-11). | Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2); Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11) |
| Recommended first-line diagnostic tests | In suspected acute hepatic porphyria, first-line testing is random urine ALA and PBG corrected to creatinine; in ADP, elevated ALA with absent/minimal PBG rise should raise suspicion. Follow with porphyrin fractionation, erythrocyte ALAD activity assay, and molecular testing of ALAD (wang2023agaclinicalpractice pages 3-5, wang2023agaclinicalpractice pages 1-3, pierro2021laboratorydiagnosisof pages 2-4, pierro2021laboratorydiagnosisof pages 12-13). | Wang et al., 2023, https://doi.org/10.1053/j.gastro.2022.11.034 (wang2023agaclinicalpractice pages 3-5, wang2023agaclinicalpractice pages 1-3); Di Pierro et al., 2021, https://doi.org/10.3390/diagnostics11081343 (pierro2021laboratorydiagnosisof pages 2-4, pierro2021laboratorydiagnosisof pages 12-13) |
| Additional diagnostic clues | Plasma fluorescence scan may show emission peak around 618–622 nm in symptomatic ADP/AIP/HCP; blood lead level should be checked because lead poisoning can mimic ADP by inhibiting ALAD (pierro2021laboratorydiagnosisof pages 2-4, ramanujam2015porphyriadiagnostics—part1 pages 9-11, doss2004thethirdcase pages 1-4). | Di Pierro et al., 2021, https://doi.org/10.3390/diagnostics11081343 (pierro2021laboratorydiagnosisof pages 2-4); Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11); Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 1-4) |
| Differential diagnosis / triggers | Important mimics and modifiers include lead poisoning, hereditary tyrosinemia type 1 (succinylacetone inhibits ALAD), zinc deficiency, alcohol, smoking, diabetes, and chronic renal failure. Lead displaces zinc from ALAD and can produce an ADP-like picture (ramanujam2015porphyriadiagnostics—part1 pages 9-11, balogun2023thehepaticporphyrias pages 3-5, gross19985aminolevulinicaciddehydratase pages 4-5). | Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11); Balogun & Nejak-Bowen, 2023, https://doi.org/10.1055/s-0043-1776760 (balogun2023thehepaticporphyrias pages 3-5); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 4-5) |
| Key treatment: hemin / heme arginate | Best-supported acute and prophylactic treatment. Effective in several reported ADP patients; reduces urinary ALA and porphyrins and improves symptoms. Weekly haem arginate for 1 year produced sustained benefit in one case; long-term weekly prophylactic hemin reduced attacks in another but caused iron overload (doss2004thethirdcase pages 7-8, gross19985aminolevulinicaciddehydratase pages 1-2, doss2004thethirdcase pages 1-4, graff2022casereportlack pages 1-2). | Doss et al., 2004, https://doi.org/10.1023/b:boli.0000037341.21975.9d (doss2004thethirdcase pages 7-8, doss2004thethirdcase pages 1-4); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 1-2); Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2) |
| Key treatment: glucose / dextrose | Used as part of acute attack management in AHPs; historical ADP cases improved with glucose plus heme arginate, but older review notes glucose loading alone was not effective in some young male ADP cases (wang2023agaclinicalpractice pages 1-3, gross19985aminolevulinicaciddehydratase pages 1-2, ramanujam2015porphyriadiagnostics—part1 pages 9-11). | Wang et al., 2023, https://doi.org/10.1053/j.gastro.2022.11.034 (wang2023agaclinicalpractice pages 1-3); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 1-2); Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11) |
| Key treatment: givosiran | Included under broad AHP approvals/trials and ALAD-deficient patients were eligible for ENVISION, but no dedicated ALAD trial identified. Single ADP case report found no durable biochemical or clinical benefit after 6 months; attacks continued, though no liver adverse effects were observed in that patient (NCT03338816 chunk 1, graff2022casereportlack pages 2-4, graff2022casereportlack pages 1-2). | ClinicalTrials.gov NCT03338816, 2017, https://clinicaltrials.gov/study/NCT03338816 (NCT03338816 chunk 1); Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 2-4, graff2022casereportlack pages 1-2) |
| Key treatment: hydroxyurea | Not established, but reported as beneficial in one previous ADP case; considered/planned in 2022 case because ADP may have an erythropoietic component (graff2022casereportlack pages 1-2). | Graff et al., 2022, https://doi.org/10.3389/fgene.2022.867856 (graff2022casereportlack pages 1-2) |
| Key treatment: liver transplantation | Reserved for refractory AHP generally, but evidence in ADP is poor; one child with ADP did not benefit and died after liver transplantation according to historical reports/reviews (wang2023agaclinicalpractice pages 1-3, ramanujam2015porphyriadiagnostics—part1 pages 9-11, gross19985aminolevulinicaciddehydratase pages 4-5). | Wang et al., 2023, https://doi.org/10.1053/j.gastro.2022.11.034 (wang2023agaclinicalpractice pages 1-3); Ramanujam & Anderson, 2015, https://doi.org/10.1002/0471142905.hg1720s86 (ramanujam2015porphyriadiagnostics—part1 pages 9-11); Gross et al., 1998, https://doi.org/10.1093/clinchem/44.9.1892 (gross19985aminolevulinicaciddehydratase pages 4-5) |


*Table: This table compiles the most actionable disease-definition, diagnostic, biochemical, and treatment facts for ALAD deficiency porphyria (Doss porphyria) using only gathered evidence. It is useful as a compact source for knowledge-base population and clinical differentiation from other acute hepatic porphyrias and lead toxicity.*

---

## Limitations of this report
- Several requested identifiers (MONDO, Orphanet, ICD, MeSH) and population allele frequencies (gnomAD/ClinVar) were not present in the retrieved full-text evidence set; they are therefore not reported to avoid uncited or incorrect entries.
- Evidence for ADP is dominated by case reports/very small series; conclusions about therapies such as givosiran or hydroxyurea remain low-certainty and should be interpreted cautiously. (graff2022casereportlack pages 1-2, NCT03338816 chunk 1)


References

1. (wang2023agaclinicalpractice pages 1-3): Bruce Wang, Herbert L. Bonkovsky, Joseph K. Lim, and Manisha Balwani. Aga clinical practice update on diagnosis and management of acute hepatic porphyrias: expert review. Gastroenterology, 164:484-491, Mar 2023. URL: https://doi.org/10.1053/j.gastro.2022.11.034, doi:10.1053/j.gastro.2022.11.034. This article has 91 citations and is from a highest quality peer-reviewed journal.

2. (wang2023agaclinicalpractice pages 3-5): Bruce Wang, Herbert L. Bonkovsky, Joseph K. Lim, and Manisha Balwani. Aga clinical practice update on diagnosis and management of acute hepatic porphyrias: expert review. Gastroenterology, 164:484-491, Mar 2023. URL: https://doi.org/10.1053/j.gastro.2022.11.034, doi:10.1053/j.gastro.2022.11.034. This article has 91 citations and is from a highest quality peer-reviewed journal.

3. (graff2022casereportlack pages 1-2): Erica Graff, Karl E. Anderson, and Cynthia Levy. Case report: lack of response to givosiran in a case of alad porphyria. Frontiers in Genetics, Aug 2022. URL: https://doi.org/10.3389/fgene.2022.867856, doi:10.3389/fgene.2022.867856. This article has 11 citations and is from a peer-reviewed journal.

4. (ramanujam2015porphyriadiagnostics—part1 pages 9-11): Vaithamanithi‐Mudumbai Sadagopa Ramanujam and Karl Elmo Anderson. Porphyria diagnostics—part 1: a brief overview of the porphyrias. Current Protocols in Human Genetics, 86:17.20.1-17.20.26, Jul 2015. URL: https://doi.org/10.1002/0471142905.hg1720s86, doi:10.1002/0471142905.hg1720s86. This article has 220 citations.

5. (gross19985aminolevulinicaciddehydratase pages 1-2): Ulrich Gross, Shigeru Sassa, Karl Jacob, Jean-Charles Deybach, Yves Nordmann, Margareta Frank, and Manfred O Doss. 5-aminolevulinic acid dehydratase deficiency porphyria: a twenty-year clinical and biochemical follow-up. Clinical Chemistry, 44:1892-1896, Sep 1998. URL: https://doi.org/10.1093/clinchem/44.9.1892, doi:10.1093/clinchem/44.9.1892. This article has 65 citations and is from a highest quality peer-reviewed journal.

6. (doss2004thethirdcase pages 1-4): M. O. Doss, T. Stauch, U. Gross, M. Renz, R. Akagi, M. Doss‐Frank, H. P. Seelig, and S. Sassa. The third case of doss porphyria (δ-amino-levulinic acid dehydratase deficiency) in germany. Journal of Inherited Metabolic Disease, 27:529-536, Jul 2004. URL: https://doi.org/10.1023/b:boli.0000037341.21975.9d, doi:10.1023/b:boli.0000037341.21975.9d. This article has 68 citations and is from a peer-reviewed journal.

7. (balogun2023thehepaticporphyrias pages 3-5): Oluwashanu Balogun and Kari Nejak-Bowen. The hepatic porphyrias: revealing the complexities of a rare disease. Seminars in Liver Disease, 43:446-459, Nov 2023. URL: https://doi.org/10.1055/s-0043-1776760, doi:10.1055/s-0043-1776760. This article has 10 citations and is from a peer-reviewed journal.

8. (gross19985aminolevulinicaciddehydratase pages 4-5): Ulrich Gross, Shigeru Sassa, Karl Jacob, Jean-Charles Deybach, Yves Nordmann, Margareta Frank, and Manfred O Doss. 5-aminolevulinic acid dehydratase deficiency porphyria: a twenty-year clinical and biochemical follow-up. Clinical Chemistry, 44:1892-1896, Sep 1998. URL: https://doi.org/10.1093/clinchem/44.9.1892, doi:10.1093/clinchem/44.9.1892. This article has 65 citations and is from a highest quality peer-reviewed journal.

9. (gross19985aminolevulinicaciddehydratase pages 2-3): Ulrich Gross, Shigeru Sassa, Karl Jacob, Jean-Charles Deybach, Yves Nordmann, Margareta Frank, and Manfred O Doss. 5-aminolevulinic acid dehydratase deficiency porphyria: a twenty-year clinical and biochemical follow-up. Clinical Chemistry, 44:1892-1896, Sep 1998. URL: https://doi.org/10.1093/clinchem/44.9.1892, doi:10.1093/clinchem/44.9.1892. This article has 65 citations and is from a highest quality peer-reviewed journal.

10. (castelbon202404163functionalcharacterization pages 1-1): Francisco Javier Castelbón, Elena Di Pierro, Isabel Solares, Daniel Jericó, Javier Tomás Solera, Antoni Riera-Mestre, María Barreda, Annamaria Nicolli, Rafael Enríquez de Salamanca, Carlo Poci, Marta Gloria Fanlo-Maresma, Matías A Ávila, Matteo Marcacci, Pauline Harper, Encarna Guillén-Navarro, Giovanna Graziadei, Bodo Beck, Paolo Ventura, Montserrat Morales-Conejo, and Antonio Fontanellas. 04163 functional characterization of new pathogenic and lead-poisoning predisposing variants in ala dehydratase porphyria (adp). Poster 49, pages A42-A43, Sep 2024. URL: https://doi.org/10.1136/bmjgast-2024-icpp.75, doi:10.1136/bmjgast-2024-icpp.75. This article has 0 citations.

11. (NCT03338816 chunk 1):  ENVISION: A Study to Evaluate the Efficacy and Safety of Givosiran (ALN-AS1) in Patients With Acute Hepatic Porphyrias (AHP). Alnylam Pharmaceuticals. 2017. ClinicalTrials.gov Identifier: NCT03338816

12. (pierro2021laboratorydiagnosisof pages 12-13): Elena Di Pierro, Michele De Canio, Rosa Mercadante, Maria Savino, Francesca Granata, Dario Tavazzi, Anna Maria Nicolli, Andrea Trevisan, Stefano Marchini, and Silvia Fustinoni. Laboratory diagnosis of porphyria. Diagnostics, 11:1343, Jul 2021. URL: https://doi.org/10.3390/diagnostics11081343, doi:10.3390/diagnostics11081343. This article has 61 citations.

13. (pierro2021laboratorydiagnosisof pages 2-4): Elena Di Pierro, Michele De Canio, Rosa Mercadante, Maria Savino, Francesca Granata, Dario Tavazzi, Anna Maria Nicolli, Andrea Trevisan, Stefano Marchini, and Silvia Fustinoni. Laboratory diagnosis of porphyria. Diagnostics, 11:1343, Jul 2021. URL: https://doi.org/10.3390/diagnostics11081343, doi:10.3390/diagnostics11081343. This article has 61 citations.

14. (graff2022casereportlack pages 2-4): Erica Graff, Karl E. Anderson, and Cynthia Levy. Case report: lack of response to givosiran in a case of alad porphyria. Frontiers in Genetics, Aug 2022. URL: https://doi.org/10.3389/fgene.2022.867856, doi:10.3389/fgene.2022.867856. This article has 11 citations and is from a peer-reviewed journal.

15. (graff2022casereportlack media 69c1e72f): Erica Graff, Karl E. Anderson, and Cynthia Levy. Case report: lack of response to givosiran in a case of alad porphyria. Frontiers in Genetics, Aug 2022. URL: https://doi.org/10.3389/fgene.2022.867856, doi:10.3389/fgene.2022.867856. This article has 11 citations and is from a peer-reviewed journal.

16. (graff2022casereportlack media 97eb2153): Erica Graff, Karl E. Anderson, and Cynthia Levy. Case report: lack of response to givosiran in a case of alad porphyria. Frontiers in Genetics, Aug 2022. URL: https://doi.org/10.3389/fgene.2022.867856, doi:10.3389/fgene.2022.867856. This article has 11 citations and is from a peer-reviewed journal.

17. (graff2022casereportlack media 0a38561c): Erica Graff, Karl E. Anderson, and Cynthia Levy. Case report: lack of response to givosiran in a case of alad porphyria. Frontiers in Genetics, Aug 2022. URL: https://doi.org/10.3389/fgene.2022.867856, doi:10.3389/fgene.2022.867856. This article has 11 citations and is from a peer-reviewed journal.

18. (doss2004thethirdcase pages 7-8): M. O. Doss, T. Stauch, U. Gross, M. Renz, R. Akagi, M. Doss‐Frank, H. P. Seelig, and S. Sassa. The third case of doss porphyria (δ-amino-levulinic acid dehydratase deficiency) in germany. Journal of Inherited Metabolic Disease, 27:529-536, Jul 2004. URL: https://doi.org/10.1023/b:boli.0000037341.21975.9d, doi:10.1023/b:boli.0000037341.21975.9d. This article has 68 citations and is from a peer-reviewed journal.
