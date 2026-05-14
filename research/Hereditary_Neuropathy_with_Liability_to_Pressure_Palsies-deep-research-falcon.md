---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:07:26.739706'
end_time: '2026-05-09T09:20:43.008994'
duration_seconds: 796.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Neuropathy with Liability to Pressure Palsies
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Neuropathy with Liability to Pressure Palsies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Neuropathy with Liability to Pressure Palsies** covering all of the
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
- **Disease Name:** Hereditary Neuropathy with Liability to Pressure Palsies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Neuropathy with Liability to Pressure Palsies** covering all of the
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


# Comprehensive Research Report: Hereditary Neuropathy with Liability to Pressure Palsies (HNPP)

## Executive summary (current understanding)
Hereditary neuropathy with liability to pressure palsies (HNPP) is a Mendelian, typically autosomal dominant, predominantly demyelinating peripheral neuropathy characterized by recurrent focal mononeuropathies precipitated by minor compression/traction/trauma at entrapment sites, with variable recovery and occasional persistent deficits. It is most commonly caused by a heterozygous recurrent ~1.4–1.5 Mb deletion at 17p11.2–p12 encompassing **PMP22**, producing PMP22 haploinsufficiency, abnormal myelin (tomacula/myelin overfolding), and susceptibility to pressure-induced conduction block. (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 1-2)

## 1. Disease information

### 1.1 What is the disease?
**Definition/overview.** A recent perioperative-focused narrative review defines HNPP as an “**autosomal dominant demyelinating neuropathy characterized by an increased susceptibility to peripheral nerve injury from trauma, compression, or shear forces**” (published April 2024; Healthcare; https://doi.org/10.3390/healthcare12080858). (laudanski2024anestheticconsiderationsfor pages 1-2)

An Orphanet-focused review describes the classic clinical phenotype as “**episodic, painless, recurrent, focal motor and sensory peripheral neuropathy, preceded by minor compression** on the affected nerve” (published March 2014; Orphanet Journal of Rare Diseases; https://doi.org/10.1186/1750-1172-9-38). (paassen2014pmp22relatedneuropathies pages 1-2)

### 1.2 Key identifiers (ontology/database cross-references)
* **MONDO:** MONDO:0008087 (MONDO_0008087) (OpenTargets Search: Hereditary neuropathy with liability to pressure palsies-PMP22)
* **Orphanet:** ORPHA:640 (paassen2014pmp22relatedneuropathies pages 7-9)

**Not retrieved in the current evidence set:** OMIM number(s), ICD-10/ICD-11 codes, and MeSH descriptor IDs were not available from the retrieved sources and should be confirmed via OMIM/Orphanet/ICD/MeSH lookups during knowledge-base curation.

### 1.3 Synonyms and alternative names
Synonyms reported in peer-reviewed literature include:
* **Tomaculous neuropathy**; **familial recurrent polyneuropathy** (Orphanet review) (paassen2014pmp22relatedneuropathies pages 7-9)
* Historical term **“potato grubbing disease”** (case report; Aug 2025; Frontiers in Genetics; https://doi.org/10.3389/fgene.2025.1613022) (savasta2025casereporthereditary pages 1-2)

### 1.4 Evidence provenance (individual vs aggregated)
The information summarized here is derived from aggregated disease-level resources and published case/cohort literature (reviews, cohort diagnostic series, and mechanistic animal studies), rather than EHR-only sources. (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 1-2, chen2025literaturereviewof pages 1-2)

## 2. Etiology

### 2.1 Disease causal factors (primary causes)
HNPP is primarily a **genetic** disease driven by **PMP22 dosage reduction** (haploinsufficiency):
* The canonical lesion is a recurrent heterozygous **~1.4–1.5 Mb deletion** in the 17p11.2–p12 region including **PMP22**. (paassen2014pmp22relatedneuropathies pages 7-9, fabrizi2015disordersofperipheral pages 7-9)
* A minority of HNPP cases result from **PMP22 sequence-level loss-of-function variants** (e.g., truncating/null alleles). (li2013thepmp22gene pages 15-17, paassen2014pmp22relatedneuropathies pages 7-9)

A recent literature review summarizing cases from January 2003–June 2024 states: “**Most patients with HNPP have a heterozygous deletion on chromosome 17p11.2, the region that encompasses the gene for peripheral myelin protein 22 (PMP22).**” (Journal of Neurology; online 2024/print 2025; https://doi.org/10.1007/s00415-024-12839-7). (chen2025literaturereviewof pages 1-2)

### 2.2 Risk factors
**Genetic risk factor (causal).** Carrying the heterozygous 17p11.2–p12 deletion encompassing PMP22 is the principal causal risk factor. (paassen2014pmp22relatedneuropathies pages 7-9)

**Environmental/mechanical triggers.** Many episodes are precipitated by mechanical stressors (compression/traction/prolonged positioning), acting as trigger exposures in genetically susceptible nerves. (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 4-5)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
A clinically important G×E interaction is that **PMP22 haploinsufficiency creates a vulnerable myelin architecture**, such that ordinary mechanical exposures (compression/traction) can precipitate focal conduction failure/mononeuropathy episodes. (paassen2014pmp22relatedneuropathies pages 7-9, pantera2020pmp22superenhancerdeletion pages 4-7)

## 3. Phenotypes

### 3.1 Core clinical phenotype (signs/symptoms)
Typical manifestations include recurrent focal motor and sensory deficits in single-nerve distributions or plexus patterns, particularly at entrapment sites. Commonly affected nerves include peroneal/common fibular, ulnar, median, radial, and brachial plexus distributions. (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 4-5, chen2025literaturereviewof pages 1-2)

A 2024 review notes episodes may last “**hours to months**” and recurrence is common. (laudanski2024anestheticconsiderationsfor pages 1-2)

### 3.2 Phenotype frequencies and clinical heterogeneity (recent compiled case series)
A clinical literature review (cases assembled through June 2024) reported the following frequencies in 124 HNPP cases:
* “**Typical weakness and numbness in vulnerable areas**” in **63.7%**
* **62%** experienced **recurrent episodes**
* **Atypical symptoms** in **29.8%**
* **Asymptomatic** in **6.5%**
* “**Pain and muscular dystrophy**” in **17.7%**
* **Pes cavus** in **12.1%**
* **Family history** in **64.5%**
* Triggers among symptomatic patients: **traction or compression (57.8%)**, **temperature changes (3.4%)**, unclear (38.8%). (chen2025literaturereviewof pages 1-2)

**Pain as an under-recognized feature.** A case report emphasizes that although HNPP is “classically described as a painless condition,” pain is “frequently reported,” and may represent an early feature in some individuals. (savasta2025casereporthereditary pages 1-2)

### 3.3 Suggested HPO terms (not exhaustive; based on reported clinical patterns)
* Recurrent focal neuropathy / mononeuropathy: **HP:0009830** (Peripheral neuropathy) (conceptual mapping)
* Paresthesia: **HP:0003401**
* Numbness: **HP:0003401/HP:0003402** (conceptual; depending on ontology granularity)
* Foot drop: **HP:0001761**
* Muscle weakness: **HP:0001324**
* Areflexia/hyporeflexia: **HP:0001284**
* Pes cavus: **HP:0001761** (note: HPO has **HP:0001761** for foot drop; pes cavus is **HP:0001761?**—verify exact HPO IDs during curation)

Because HPO identifiers are not provided directly in the retrieved literature excerpts, these should be validated against the current HPO release before ingestion.

## 4. Genetic / molecular information

### 4.1 Causal genes
* **PMP22 (peripheral myelin protein 22)** is the principal causal gene. (OpenTargets Search: Hereditary neuropathy with liability to pressure palsies-PMP22, paassen2014pmp22relatedneuropathies pages 7-9)

### 4.2 Pathogenic variants (variant classes and frequencies)
* **Canonical CNV:** recurrent heterozygous deletion spanning PMP22 (~1.4–1.5 Mb), responsible for the majority of HNPP cases (multiple reviews). (paassen2014pmp22relatedneuropathies pages 7-9, fabrizi2015disordersofperipheral pages 7-9)
* **Sequence variants:** PMP22 truncating/null alleles and other variants can also cause HNPP; a mechanistic review of PMP22 disease biology states that many HNPP mutations are truncations and are “**functionally equivalent to classical chromosome 17p11.2 deletion with loss of function of PMP22**.” (li2013thepmp22gene pages 15-17)

**Inheritance and penetrance.** HNPP is autosomal dominant; a 2024 narrative review reports penetrance “**70–100%**,” and notes that “approximately 20% of cases” result from de novo deletions or point mutations. (laudanski2024anestheticconsiderationsfor pages 1-2)

### 4.3 Modifier genes / epigenetics
No specific modifier genes or epigenetic mechanisms for HNPP were identified in the retrieved evidence set.

### 4.4 Disease-target association (curated evidence)
OpenTargets links **PMP22** to HNPP (MONDO_0008087) with multiple literature evidence items (e.g., PubMed IDs 9748013, 12796555, 15099592 in the OpenTargets evidence list). (OpenTargets Search: Hereditary neuropathy with liability to pressure palsies-PMP22)

## 5. Environmental information
HNPP is not an infectious disease and is not primarily environmentally caused; however, **mechanical exposures** (compression, traction, shear forces, prolonged positioning) are major **episode triggers** in genetically affected individuals. (laudanski2024anestheticconsiderationsfor pages 4-5, laudanski2024anestheticconsiderationsfor pages 1-2)

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (from genotype to clinical episodes)
1. **Genetic lesion**: PMP22 dosage reduction (typically 17p11.2–p12 deletion). (paassen2014pmp22relatedneuropathies pages 7-9)
2. **Cell type**: Schwann-cell myelin maintenance is compromised by PMP22 haploinsufficiency, producing focal myelin architectural abnormalities. (paassen2014pmp22relatedneuropathies pages 7-9)
3. **Tissue-level hallmark**: **tomacula** (myelin overfolding/focal thickenings) and related nodal/paranodal changes. (paassen2014pmp22relatedneuropathies pages 7-9)
4. **Physiology**: predisposition to **pressure/stretch-induced reversible conduction block**, clinically manifesting as recurrent focal palsies at entrapment sites. (paassen2014pmp22relatedneuropathies pages 7-9, fabrizi2015disordersofperipheral pages 7-9)

### 6.2 Primary mechanistic evidence (animal model; regulatory mechanism)
Pantera et al. (Human Molecular Genetics; April 2020; https://doi.org/10.1093/hmg/ddaa082) tested whether deleting a distal **Pmp22 super-enhancer** reduces expression and phenocopies HNPP. The abstract states that “**the reciprocal deletion of this gene causes a separate neuropathy termed Hereditary Neuropathy with Liability to Pressure Palsies (HNPP)**,” and reports that super-enhancer deletion reduces Pmp22 expression and leads to “**tomacula formed by excessive myelin folding, a pathological hallmark of HNPP**.” (pantera2020pmp22superenhancerdeletion pages 1-2)

The same study reports functional vulnerability to mechanically induced conduction failure (compression assay) and impaired recovery in more severe genotypes, linking PMP22 transcriptional control to conduction block susceptibility. (pantera2020pmp22superenhancerdeletion pages 4-7)

**Visual evidence.** Cropped panels from this study show teased-fiber tomacula quantification and the mechanical compression assay demonstrating time-to-conduction-block and recovery curves. (pantera2020pmp22superenhancerdeletion media 04ee1ad6, pantera2020pmp22superenhancerdeletion media 85bcd5c7)

### 6.3 Suggested GO biological process terms (verify IDs during curation)
* Schwann cell differentiation / myelination
* Peripheral nervous system myelination
* Axon ensheathment
* Response to mechanical stimulus (contextual)

### 6.4 Suggested Cell Ontology (CL) terms (verify IDs during curation)
* **Schwann cell** (myelinating Schwann cell)

### 6.5 Suggested UBERON anatomical terms
* Peripheral nerve
* Sciatic nerve (commonly studied in models)

## 7. Anatomical structures affected

### 7.1 Organ/system level
* Primary system: **Peripheral nervous system** (peripheral nerves subject to entrapment/compression). (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 4-5)

### 7.2 Tissue/cell level
* Tissue: peripheral myelin; nerve fascicles at entrapment sites.
* Cell type: Schwann cells. (pantera2020pmp22superenhancerdeletion pages 1-2, paassen2014pmp22relatedneuropathies pages 7-9)

### 7.3 Subcellular level
No specific subcellular compartment signature for HNPP was identified in the retrieved evidence set.

## 8. Temporal development (natural history)

### 8.1 Onset
Typical onset is often in the **2nd–3rd decade**, but a wide age range is reported. (paassen2014pmp22relatedneuropathies pages 7-9, chen2025literaturereviewof pages 1-2)

### 8.2 Course/progression
The course is often **episodic** with recurrent focal palsies and variable recovery. The perioperative-focused review notes that episodes usually resolve over “days to months” but persistent deficits can occur. (laudanski2024anestheticconsiderationsfor pages 4-5)

## 9. Inheritance and population

### 9.1 Inheritance pattern
Autosomal dominant inheritance is consistently reported. (paassen2014pmp22relatedneuropathies pages 1-2, savasta2025casereporthereditary pages 1-2)

### 9.2 Epidemiology (statistics)
Frequently cited prevalence/incidence estimates are ~**7–16 per 100,000**. (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 1-2)

Regional estimates include **~7.3/100,000 in England** and **~16/100,000 in southwestern Finland**. (paassen2014pmp22relatedneuropathies pages 7-9, lehtilahti2022charcotmarietoothdiseasemolecular pages 25-28)

**Underdiagnosis and higher genetic prevalence signals.** A 2024 narrative review notes that the reported incidence may be an underestimation due to underdiagnosis. (laudanski2024anestheticconsiderationsfor pages 1-2) A compiled literature review reports newborn-screening-based prevalence estimates up to **58.9/100,000**, suggesting population prevalence may exceed clinically ascertained estimates. (chen2025literaturereviewof pages 1-2)

## 10. Diagnostics

### 10.1 Clinical/electrodiagnostic evaluation
Electrophysiology is central: characteristic findings include increased distal motor latencies, focal slowing at entrapment sites, and sensory nerve conduction abnormalities. (paassen2014pmp22relatedneuropathies pages 7-9, paassen2014pmp22relatedneuropathies pages 1-2)

A 2024 perioperative review summarizes a suggestive signature: bilateral median sensorimotor latency prolongation plus at least unilateral peroneal motor abnormality, and notes diminished/absent sural responses in ~one-third of patients. (laudanski2024anestheticconsiderationsfor pages 4-5)

### 10.2 Imaging
Nerve ultrasound and MRI (including diffusion tensor imaging) can provide supportive findings in some settings. (laudanski2024anestheticconsiderationsfor pages 4-5)

### 10.3 Genetic testing approach (real-world implementation)
**First-line molecular test (typical workflow):** assay for **PMP22 deletion** (copy number) using **MLPA** or **chromosomal microarray**, with confirmatory approaches including **FISH** or **PCR-based** methods depending on laboratory practice. (laudanski2024anestheticconsiderationsfor pages 4-5, cesaroni2025pmp22relatedneuropathiesa pages 13-15)

**If deletion testing is negative or phenotype is atypical:** sequence analysis of PMP22 and/or inherited neuropathy gene panels, WES, or WGS may be used to detect rarer sequence variants or alternative diagnoses. (cesaroni2025pmp22relatedneuropathiesa pages 15-17, record2024wholegenomesequencing pages 1-2)

**2024 genomic diagnostics data (large specialist cohort).** In a single inherited neuropathy center cohort (Brain; March 2024; https://doi.org/10.1093/brain/awae064), 1,515 patients with CMT and related disorders were studied; **72 were HNPP (4.8%)**, and “**PMP22 deletion (HNPP; 72/1165, 6.2%)**” represented a major solved diagnosis category. (record2024wholegenomesequencing pages 1-2)

The same study emphasizes pragmatic workflow: “**it is essential to ensure MLPA for PMP22 CNV has been performed, before moving to NGS**.” (record2024wholegenomesequencing pages 3-5)

### 10.4 Differential diagnosis
HNPP can be misdiagnosed as radiculopathy or focal chronic inflammatory demyelinating polyneuropathy (CIDP), among others, and recurrence plus supportive electrodiagnostics and genetic confirmation aid distinction. (savasta2025casereporthereditary pages 1-2)

## 11. Outcome / prognosis
Life expectancy is generally reported as normal in PMP22-related neuropathy reviews, and many episodes recover; however, persistent deficits may occur. (paassen2014pmp22relatedneuropathies pages 1-2, laudanski2024anestheticconsiderationsfor pages 4-5)

Quantitative quality-of-life instrument results (e.g., SF-36/EQ-5D) were not available in the retrieved evidence set.

## 12. Treatment

### 12.1 Current standard management (real-world implementation)
There is no established disease-modifying pharmacotherapy for HNPP in the retrieved evidence set; management is mainly supportive and preventive:
* Avoidance of compressive/traction triggers; ergonomic/occupational modifications. (laudanski2024anestheticconsiderationsfor pages 4-5)
* Multidisciplinary rehabilitation (physiotherapy/occupational therapy) is described in PMP22-related neuropathy reviews. (paassen2014pmp22relatedneuropathies pages 1-2)

### 12.2 Perioperative/anesthesia precautions (2024 expert synthesis)
Because surgical positioning and anesthesia can impose prolonged compression/shear on nerves, perioperative teams are advised to implement tailored positioning/monitoring strategies for HNPP patients. (laudanski2024anestheticconsiderationsfor pages 1-2, laudanski2024anestheticconsiderationsfor pages 4-5)

### 12.3 Procedures and symptomatic interventions
**Entrapment neuropathies (e.g., carpal tunnel syndrome) in inherited neuropathy.** A completed observational study used patient-reported outcomes to evaluate carpal tunnel therapies in adults with inherited neuropathy including HNPP (ClinicalTrials.gov NCT02788734; start June 2016; primary completion Nov 2016). Outcomes included Boston Carpal Tunnel Questionnaire (BCTQ) and DASH (Disabilities of the Arm, Shoulder and Hand). (NCT02788734 chunk 1)

### 12.4 MAXO term suggestions (verify IDs during curation)
* Physical therapy; occupational therapy
* Genetic counseling
* Avoidance of mechanical nerve compression
* Perioperative positioning precautions
* Nerve decompression surgery (in selected entrapment neuropathies)

## 13. Prevention
Primary and tertiary prevention focus on reducing mechanical nerve injury risk:
* Avoid prolonged pressure at bony prominences; protective padding and repositioning during sleep, work, and surgery. (laudanski2024anestheticconsiderationsfor pages 4-5)
* Perioperative positioning protocols for known/suspected HNPP. (laudanski2024anestheticconsiderationsfor pages 1-2)

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence set.

## 15. Model organisms

### 15.1 Mouse regulatory-element model phenocopying HNPP
Pantera et al. (2020) created mice with CRISPR deletion of a distal **Pmp22 super-enhancer**, demonstrating reduced Pmp22 expression, **tomacula formation**, and susceptibility to **compression-induced conduction block**, thereby modeling a regulatory mechanism for PMP22 haploinsufficiency phenotypes relevant to HNPP. (pantera2020pmp22superenhancerdeletion pages 1-2, pantera2020pmp22superenhancerdeletion pages 4-7)

## Recent developments and “latest research” (prioritizing 2023–2024)

### A. Precision diagnostics: WGS as a complement to traditional CNV testing (2024)
A 2024 Brain study from a specialist center reported a very high overall genetic diagnostic rate (76.9% overall in 1,515 CMT-related patients) and quantified the contribution of PMP22 deletion diagnoses (HNPP) in the solved cohort, while reporting a modest additional uplift attributable to WGS in their end-to-end pipeline. (record2024wholegenomesequencing pages 1-2, record2024wholegenomesequencing pages 3-5)

### B. Perioperative risk management and implementation guidance (2024)
A 2024 narrative review synthesized contemporary evidence and recommendations for anesthesia/surgical teams, emphasizing that HNPP patients may be under-recognized perioperatively and benefit from tailored positioning and monitoring strategies. (laudanski2024anestheticconsiderationsfor pages 1-2, laudanski2024anestheticconsiderationsfor pages 4-5)

### C. Real-world registries capturing outcomes and heterogeneity
* **GRIN registry / natural history survey** includes HNPP among inherited neuropathies in a large recruiting observational program (ClinicalTrials.gov **NCT05902351**, start 2013; estimated primary completion 2029). (NCT05902351 chunk 1)
* Carpal tunnel PRO study in inherited neuropathies (ClinicalTrials.gov **NCT02788734**) included HNPP and used standardized PRO instruments, illustrating how patient-centered outcomes are being deployed in real-world inherited neuropathy populations. (NCT02788734 chunk 1)

## Key evidence gaps for knowledge-base completion
* OMIM/ICD/MeSH identifiers were not retrieved in the current evidence set.
* Robust population-based carrier frequency/founder-effect data were not found in the retrieved corpus.
* Quantitative QoL data using standardized instruments (EQ-5D/SF-36/PROMIS) were not found in retrieved excerpts.

---

## Evidence summary table (knowledge-base scaffold)

| Domain | Key fact | Details | Citation placeholder |
|---|---|---|---|
| Disease name | Hereditary Neuropathy with Liability to Pressure Palsies (HNPP) | Mendelian inherited peripheral neuropathy characterized by recurrent focal pressure palsies/mononeuropathies | (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 1-2) |
| Identifiers | MONDO | MONDO:0008087 | (OpenTargets Search: Hereditary neuropathy with liability to pressure palsies-PMP22) |
| Identifiers | Orphanet | ORPHA:640 | (paassen2014pmp22relatedneuropathies pages 7-9) |
| Synonyms | Common alternative names | Hereditary neuropathy with liability to pressure palsy; tomaculous neuropathy; familial recurrent polyneuropathy; historical term “potato grubbing disease” | (paassen2014pmp22relatedneuropathies pages 7-9, savasta2025casereporthereditary pages 1-2, fabrizi2015disordersofperipheral pages 7-9) |
| Information source type | Evidence provenance | Aggregated disease-level resources and published case/cohort literature; not primarily EHR-derived | (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 1-2, chen2025literaturereviewof pages 1-2) |
| Inheritance | Mode of inheritance | Autosomal dominant; offspring recurrence risk typically 50% for an affected heterozygous parent | (paassen2014pmp22relatedneuropathies pages 1-2, laudanski2024anestheticconsiderationsfor pages 1-2) |
| Inheritance | Penetrance / de novo | Penetrance reported ~70–100%; de novo events occur, estimated around 20% in some reviews | (laudanski2024anestheticconsiderationsfor pages 1-2, paassen2014pmp22relatedneuropathies pages 7-9) |
| Causal gene | Primary gene | PMP22 (peripheral myelin protein 22) | (OpenTargets Search: Hereditary neuropathy with liability to pressure palsies-PMP22, paassen2014pmp22relatedneuropathies pages 7-9) |
| Causal lesion | Canonical pathogenic lesion | Recurrent heterozygous ~1.4–1.5 Mb deletion at 17p11.2/17p12 including PMP22; causes PMP22 haploinsufficiency | (paassen2014pmp22relatedneuropathies pages 7-9, fabrizi2015disordersofperipheral pages 7-9) |
| Causal lesion | Less common pathogenic variants | PMP22 sequence variants/small indels/splice variants can also cause HNPP; loss-of-function/null alleles are important | (cesaroni2025pmp22relatedneuropathiesa pages 12-13, li2013thepmp22gene pages 15-17, laudanski2024anestheticconsiderationsfor pages 4-5) |
| Mechanistic summary | Core disease mechanism | PMP22 dosage reduction in Schwann cells destabilizes peripheral myelin, producing tomacula/myelin overfolding and susceptibility to pressure-induced conduction block | (pantera2020pmp22superenhancerdeletion pages 1-2, pantera2020pmp22superenhancerdeletion pages 4-7, paassen2014pmp22relatedneuropathies pages 7-9) |
| Prevalence / incidence | Classic epidemiologic estimate | Frequently cited prevalence/incidence range: ~7–16 per 100,000 | (laudanski2024anestheticconsiderationsfor pages 1-2, paassen2014pmp22relatedneuropathies pages 7-9) |
| Prevalence / incidence | Regional estimates | Approx. 7.3/100,000 in England and 16/100,000 in southwestern Finland | (paassen2014pmp22relatedneuropathies pages 7-9, lehtilahti2022charcotmarietoothdiseasemolecular pages 25-28) |
| Prevalence / incidence | Potential underdiagnosis / higher genomic estimate | Underdiagnosis is likely; newborn genetic screening data have suggested substantially higher prevalence, including ~58.9/100,000 and 1 in 1,698 in one report/reviewed literature | (chen2025literaturereviewof pages 1-2, savasta2025casereporthereditary pages 1-2) |
| Typical onset | Age at onset | Usually 2nd–3rd decade, but can range from childhood to late adulthood; mean onset in one 2025 review was 26.5 ± 18 years | (paassen2014pmp22relatedneuropathies pages 7-9, chen2025literaturereviewof pages 1-2) |
| Typical course | Clinical pattern | Episodic, recurrent, often painless focal motor and sensory neuropathies; recovery may occur over days to months, but residual deficits can persist | (paassen2014pmp22relatedneuropathies pages 1-2, laudanski2024anestheticconsiderationsfor pages 4-5) |
| Typical triggers | Mechanical triggers | Minor compression, traction, shear forces, prolonged limb positioning, repetitive local pressure, mild trauma | (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 1-2, laudanski2024anestheticconsiderationsfor pages 4-5) |
| Typical triggers | Quantified trigger data | In a 2025 literature review, triggers were traction/compression 57.8%, temperature change 3.4%, unclear 38.8% | (chen2025literaturereviewof pages 1-2) |
| Typical nerves affected | Most commonly involved nerves | Peroneal/common fibular and ulnar nerves are most frequent; median, radial, and brachial plexus involvement are also typical | (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 4-5, chen2025literaturereviewof pages 1-2) |
| Typical manifestations | Common presentations | Foot drop/peroneal palsy, ulnar neuropathy at the elbow, carpal tunnel syndrome/median neuropathy, brachial plexopathy, focal numbness/paresthesia | (paassen2014pmp22relatedneuropathies pages 7-9, laudanski2024anestheticconsiderationsfor pages 4-5) |
| Phenotype frequencies | Selected recent review statistics | Typical weakness/numbness in vulnerable areas 63.7%; recurrent episodes 62%; atypical symptoms 29.8%; asymptomatic 6.5%; family history 64.5%; pes cavus 12.1%; pain/muscle atrophy 17.7% | (chen2025literaturereviewof pages 1-2) |
| Electrophysiology | Characteristic nerve conduction pattern | Demyelinating polyneuropathy pattern with increased distal motor latencies, especially median and peroneal; focal slowing/conduction block at entrapment sites; reduced sensory conduction velocities and SNAP amplitudes | (paassen2014pmp22relatedneuropathies pages 7-9, paassen2014pmp22relatedneuropathies pages 1-2, laudanski2024anestheticconsiderationsfor pages 4-5) |
| Electrophysiology | Suggestive electrodiagnostic signature | Bilateral median sensorimotor latency prolongation with at least unilateral peroneal motor abnormality is highly suggestive; sural responses may be reduced/absent in ~1/3 | (laudanski2024anestheticconsiderationsfor pages 4-5) |
| Pathology | Nerve biopsy hallmark | Tomacula (sausage-like focal myelin thickening/overfolding), plus segmental de- and remyelination | (paassen2014pmp22relatedneuropathies pages 7-9, fabrizi2015disordersofperipheral pages 7-9) |
| Diagnostic modalities | First-line molecular confirmation | PMP22 copy-number testing for the recurrent deletion using MLPA, chromosomal microarray, FISH, or PCR-based methods | (laudanski2024anestheticconsiderationsfor pages 4-5, record2024wholegenomesequencing pages 3-5, cesaroni2025pmp22relatedneuropathiesa pages 13-15) |
| Diagnostic modalities | Sequencing methods | If deletion testing is negative or phenotype is atypical, consider PMP22 sequencing and/or neuropathy gene panels, WES, or WGS | (record2024wholegenomesequencing pages 3-5, record2024wholegenomesequencing pages 1-2, cesaroni2025pmp22relatedneuropathiesa pages 15-17) |
| Diagnostic modalities | Relative use of methods in recent review | Among 2,571 genetically tested PMP22-related neuropathy cases, MLPA 41.9%, NGS 20.4%, Sanger 17.8%, WES 0.4%, CGH/SNP array 1.4% | (cesaroni2025pmp22relatedneuropathiesa pages 13-15) |
| Diagnostic yield / cohorts | Large inherited neuropathy center data | In a 2024 Brain cohort of 1,515 inherited neuropathy patients, 72 HNPP cases (4.8%) were identified; PMP22 deletion represented 6.2% of solved genetic diagnoses | (record2024wholegenomesequencing pages 2-3, record2024wholegenomesequencing pages 1-2) |
| Imaging / adjunct tests | Supportive non-genetic tests | Nerve ultrasound and MRI/DTI can provide supportive structural information; muscle fatty infiltration has been proposed as a biomarker of progression | (laudanski2024anestheticconsiderationsfor pages 4-5, paassen2014pmp22relatedneuropathies pages 1-2) |


*Table: This table summarizes core identifiers, genetics, epidemiology, phenotype, electrophysiology, and diagnostic approaches for hereditary neuropathy with liability to pressure palsies. It is formatted for direct reuse as a knowledge-base scaffold with citation placeholders tied to available context IDs.*

---

## Primary visual evidence (mechanism)
Tomacula formation and compression-induced conduction block are shown in the Pmp22 super-enhancer deletion mouse model figures. (pantera2020pmp22superenhancerdeletion media 04ee1ad6, pantera2020pmp22superenhancerdeletion media 85bcd5c7)

References

1. (paassen2014pmp22relatedneuropathies pages 7-9): Barbara W van Paassen, Anneke J van der Kooi, Karin Y van Spaendonck-Zwarts, Camiel Verhamme, Frank Baas, and Marianne de Visser. Pmp22 related neuropathies: charcot-marie-tooth disease type 1a and hereditary neuropathy with liability to pressure palsies. Orphanet Journal of Rare Diseases, 9:38-38, Mar 2014. URL: https://doi.org/10.1186/1750-1172-9-38, doi:10.1186/1750-1172-9-38. This article has 258 citations and is from a peer-reviewed journal.

2. (laudanski2024anestheticconsiderationsfor pages 1-2): Krzysztof Laudanski, Omar Elmadhoun, Amal Mathew, Yul Kahn-Pascual, Mitchell J. Kerfeld, James Chen, Daniella C. Sisniega, and Francisco Gomez. Anesthetic considerations for patients with hereditary neuropathy with liability to pressure palsies: a narrative review. Healthcare, 12:858, Apr 2024. URL: https://doi.org/10.3390/healthcare12080858, doi:10.3390/healthcare12080858. This article has 1 citations.

3. (paassen2014pmp22relatedneuropathies pages 1-2): Barbara W van Paassen, Anneke J van der Kooi, Karin Y van Spaendonck-Zwarts, Camiel Verhamme, Frank Baas, and Marianne de Visser. Pmp22 related neuropathies: charcot-marie-tooth disease type 1a and hereditary neuropathy with liability to pressure palsies. Orphanet Journal of Rare Diseases, 9:38-38, Mar 2014. URL: https://doi.org/10.1186/1750-1172-9-38, doi:10.1186/1750-1172-9-38. This article has 258 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: Hereditary neuropathy with liability to pressure palsies-PMP22): Open Targets Query (Hereditary neuropathy with liability to pressure palsies-PMP22, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (savasta2025casereporthereditary pages 1-2): Salvatore Savasta, Fabiola Serra, Lucrezia Galimberti, Francesco Fabrizio Comisi, Marcello Cossu, Alessandro Vannelli, Maddalena Masala, Sara Tanca, and Stefania Murru. Case report: hereditary neuropathy with liability to pressure palsy (hnpp): the role of genetic investigation in diagnostic assessment. Frontiers in Genetics, Aug 2025. URL: https://doi.org/10.3389/fgene.2025.1613022, doi:10.3389/fgene.2025.1613022. This article has 2 citations and is from a peer-reviewed journal.

6. (chen2025literaturereviewof pages 1-2): Limin Chen, Hongbo Zhang, Chunnv Li, Nuo Yang, Jiangtao Wang, and Jianmin Liang. Literature review of clinical analysis of hereditary neuropathy with liability to pressure palsies. Journal of Neurology, Dec 2025. URL: https://doi.org/10.1007/s00415-024-12839-7, doi:10.1007/s00415-024-12839-7. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (fabrizi2015disordersofperipheral pages 7-9): Gian Maria Fabrizi and Giampietro Zanette. Disorders of peripheral nerves. ArXiv, pages 405-444, Jan 2015. URL: https://doi.org/10.1007/978-88-470-5755-5\_35, doi:10.1007/978-88-470-5755-5\_35. This article has 1 citations.

8. (li2013thepmp22gene pages 15-17): Jun Li, Brett Parker, Colin Martyn, Chandramohan Natarajan, and Jiasong Guo. The pmp22 gene and its related diseases. Molecular Neurobiology, 47:673-698, Dec 2013. URL: https://doi.org/10.1007/s12035-012-8370-x, doi:10.1007/s12035-012-8370-x. This article has 362 citations and is from a peer-reviewed journal.

9. (laudanski2024anestheticconsiderationsfor pages 4-5): Krzysztof Laudanski, Omar Elmadhoun, Amal Mathew, Yul Kahn-Pascual, Mitchell J. Kerfeld, James Chen, Daniella C. Sisniega, and Francisco Gomez. Anesthetic considerations for patients with hereditary neuropathy with liability to pressure palsies: a narrative review. Healthcare, 12:858, Apr 2024. URL: https://doi.org/10.3390/healthcare12080858, doi:10.3390/healthcare12080858. This article has 1 citations.

10. (pantera2020pmp22superenhancerdeletion pages 4-7): Harrison Pantera, Bo Hu, Daniel Moiseev, Chris Dunham, Jibraan Rashid, John J Moran, Kathleen Krentz, C Dustin Rubinstein, Seongsik Won, Jun Li, and John Svaren. Pmp22 super-enhancer deletion causes tomacula formation and conduction block in peripheral nerves. Human molecular genetics, 29:1689-1699, Apr 2020. URL: https://doi.org/10.1093/hmg/ddaa082, doi:10.1093/hmg/ddaa082. This article has 9 citations and is from a domain leading peer-reviewed journal.

11. (pantera2020pmp22superenhancerdeletion pages 1-2): Harrison Pantera, Bo Hu, Daniel Moiseev, Chris Dunham, Jibraan Rashid, John J Moran, Kathleen Krentz, C Dustin Rubinstein, Seongsik Won, Jun Li, and John Svaren. Pmp22 super-enhancer deletion causes tomacula formation and conduction block in peripheral nerves. Human molecular genetics, 29:1689-1699, Apr 2020. URL: https://doi.org/10.1093/hmg/ddaa082, doi:10.1093/hmg/ddaa082. This article has 9 citations and is from a domain leading peer-reviewed journal.

12. (pantera2020pmp22superenhancerdeletion media 04ee1ad6): Harrison Pantera, Bo Hu, Daniel Moiseev, Chris Dunham, Jibraan Rashid, John J Moran, Kathleen Krentz, C Dustin Rubinstein, Seongsik Won, Jun Li, and John Svaren. Pmp22 super-enhancer deletion causes tomacula formation and conduction block in peripheral nerves. Human molecular genetics, 29:1689-1699, Apr 2020. URL: https://doi.org/10.1093/hmg/ddaa082, doi:10.1093/hmg/ddaa082. This article has 9 citations and is from a domain leading peer-reviewed journal.

13. (pantera2020pmp22superenhancerdeletion media 85bcd5c7): Harrison Pantera, Bo Hu, Daniel Moiseev, Chris Dunham, Jibraan Rashid, John J Moran, Kathleen Krentz, C Dustin Rubinstein, Seongsik Won, Jun Li, and John Svaren. Pmp22 super-enhancer deletion causes tomacula formation and conduction block in peripheral nerves. Human molecular genetics, 29:1689-1699, Apr 2020. URL: https://doi.org/10.1093/hmg/ddaa082, doi:10.1093/hmg/ddaa082. This article has 9 citations and is from a domain leading peer-reviewed journal.

14. (lehtilahti2022charcotmarietoothdiseasemolecular pages 25-28): M Lehtilahti. Charcot-marie-tooth disease: molecular epidemiology in northern ostrobothnia. Unknown journal, 2022.

15. (cesaroni2025pmp22relatedneuropathiesa pages 13-15): Carlo Alberto Cesaroni, Laura Caiazza, Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Susanna Rizzi, Agnese Pantani, Daniele Frattini, and Carlo Fusco. Pmp22-related neuropathies: a systematic review. Genes, 16:1279, Oct 2025. URL: https://doi.org/10.3390/genes16111279, doi:10.3390/genes16111279. This article has 3 citations.

16. (cesaroni2025pmp22relatedneuropathiesa pages 15-17): Carlo Alberto Cesaroni, Laura Caiazza, Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Susanna Rizzi, Agnese Pantani, Daniele Frattini, and Carlo Fusco. Pmp22-related neuropathies: a systematic review. Genes, 16:1279, Oct 2025. URL: https://doi.org/10.3390/genes16111279, doi:10.3390/genes16111279. This article has 3 citations.

17. (record2024wholegenomesequencing pages 1-2): Christopher J Record, Menelaos Pipis, Mariola Skorupinska, Julian Blake, Roy Poh, James M Polke, Kelly Eggleton, Tina Nanji, Stephan Zuchner, Andrea Cortese, Henry Houlden, Alexander M Rossor, Matilde Laura, and Mary M Reilly. Whole genome sequencing increases the diagnostic rate in charcot-marie-tooth disease. Brain, 147:3144-3156, Mar 2024. URL: https://doi.org/10.1093/brain/awae064, doi:10.1093/brain/awae064. This article has 49 citations and is from a highest quality peer-reviewed journal.

18. (record2024wholegenomesequencing pages 3-5): Christopher J Record, Menelaos Pipis, Mariola Skorupinska, Julian Blake, Roy Poh, James M Polke, Kelly Eggleton, Tina Nanji, Stephan Zuchner, Andrea Cortese, Henry Houlden, Alexander M Rossor, Matilde Laura, and Mary M Reilly. Whole genome sequencing increases the diagnostic rate in charcot-marie-tooth disease. Brain, 147:3144-3156, Mar 2024. URL: https://doi.org/10.1093/brain/awae064, doi:10.1093/brain/awae064. This article has 49 citations and is from a highest quality peer-reviewed journal.

19. (NCT02788734 chunk 1):  Patient Reported Outcomes Measures (PROM) in Carpal Tunnel Therapies in Patients With Inherited Neuropathies. University of South Florida. 2016. ClinicalTrials.gov Identifier: NCT02788734

20. (NCT05902351 chunk 1):  Natural History Study for Charcot Marie Tooth Disease. Hereditary Neuropathy Foundation. 2013. ClinicalTrials.gov Identifier: NCT05902351

21. (cesaroni2025pmp22relatedneuropathiesa pages 12-13): Carlo Alberto Cesaroni, Laura Caiazza, Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Susanna Rizzi, Agnese Pantani, Daniele Frattini, and Carlo Fusco. Pmp22-related neuropathies: a systematic review. Genes, 16:1279, Oct 2025. URL: https://doi.org/10.3390/genes16111279, doi:10.3390/genes16111279. This article has 3 citations.

22. (record2024wholegenomesequencing pages 2-3): Christopher J Record, Menelaos Pipis, Mariola Skorupinska, Julian Blake, Roy Poh, James M Polke, Kelly Eggleton, Tina Nanji, Stephan Zuchner, Andrea Cortese, Henry Houlden, Alexander M Rossor, Matilde Laura, and Mary M Reilly. Whole genome sequencing increases the diagnostic rate in charcot-marie-tooth disease. Brain, 147:3144-3156, Mar 2024. URL: https://doi.org/10.1093/brain/awae064, doi:10.1093/brain/awae064. This article has 49 citations and is from a highest quality peer-reviewed journal.
