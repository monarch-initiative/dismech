---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T16:36:03.222096'
end_time: '2026-04-25T16:50:11.448472'
duration_seconds: 848.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alpha-1 Antitrypsin Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alpha-1 Antitrypsin Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Alpha-1 Antitrypsin Deficiency** covering all of the
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
- **Disease Name:** Alpha-1 Antitrypsin Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Alpha-1 Antitrypsin Deficiency** covering all of the
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


# Alpha-1 Antitrypsin Deficiency (AATD) — Disease Characteristics Research Report (Mendelian)

## Target disease
- **Disease name:** Alpha-1 Antitrypsin Deficiency (AATD) (also written *alpha 1-antitrypsin deficiency*) (feitosa12024recommendationsforthe pages 1-2)
- **Category:** Mendelian / inborn error of protein homeostasis (SERPIN misfolding) (feitosa12024recommendationsforthe pages 2-3, mohammad2024livercharacterizationof pages 1-2)
- **MONDO ID:** **MONDO:0013282** (“alpha 1-antitrypsin deficiency”) from Open Targets disease mapping (feitosa12024recommendationsforthe pages 1-2)

## Evidence note (scope/limitations)
This report is based on the retrieved full-text excerpts and ClinicalTrials.gov records in the current tool state. Some requested identifiers (e.g., **OMIM**, **Orphanet**, **ICD-10/ICD-11**, **MeSH**) could not be confirmed from the retrieved excerpts and therefore are not asserted here.

---

## 1. Disease information

### 1.1 Concise overview / definition
AATD is a **relatively rare genetic disorder** with **autosomal codominant** inheritance that leads to **reduced serum alpha-1 antitrypsin (AAT)** and consequently reduced **anti-elastase activity** in the lung, increasing risk for **pulmonary emphysema/COPD** and also predisposing to **liver disease (fibrosis/cirrhosis)** due to intracellular accumulation of misfolded AAT in hepatocytes (feitosa12024recommendationsforthe pages 1-2, feitosa12024recommendationsforthe pages 2-3, mohammad2024livercharacterizationof pages 1-2). In addition to lung and liver disease, AATD can present with extra-pulmonary manifestations including **necrotizing panniculitis** and **vasculitis** (feitosa12024recommendationsforthe pages 1-2, feitosa2023diagnosisandaugmentation pages 1-2, fouka2026alpha1antitrypsindeficiencyassociated pages 1-2).

### 1.2 Key identifiers (available in retrieved evidence)
- **MONDO:** MONDO:0013282 (Open Targets mapping) (feitosa12024recommendationsforthe pages 1-2)
- **Disease gene (HGNC symbol):** **SERPINA1** (feitosa12024recommendationsforthe pages 1-2, feitosa12024recommendationsforthe pages 2-3)
- **Chromosomal location (gene):** **14q32.1** for SERPINA1 (feitosa12024recommendationsforthe pages 1-2)
- **ClinicalTrials.gov registry for natural history:** **EARCO** registry (NCT04180319) (NCT04180319 chunk 1)

### 1.3 Synonyms / alternative names
- Alpha-1-antitrypsin deficiency; AAT deficiency; AATD; Alpha1-proteinase inhibitor (A1PI) deficiency (in context of augmentation therapy) (feitosa2023diagnosisandaugmentation pages 4-5, miravitlles2023ninecontroversialquestions pages 2-3).

### 1.4 Evidence source type
The current synthesis draws primarily from **aggregated disease-level resources** (guideline/review articles) and **registries/trials**, not EHR-derived single-patient case data (feitosa12024recommendationsforthe pages 1-2, NCT04180319 chunk 1, miravitlles2023ninecontroversialquestions pages 2-3).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** inherited pathogenic variants in **SERPINA1** that reduce circulating AAT levels and/or produce dysfunctional AAT (loss of antiprotease function), and (for Z-type variants) promote misfolding/polymerization with hepatocellular retention (gain-of-toxic-function in liver) (feitosa12024recommendationsforthe pages 2-3, mohammad2024livercharacterizationof pages 1-2).

### 2.2 Risk factors
#### Genetic risk
- **Severe deficiency genotypes** (e.g., Pi*ZZ; null variants) are strongly associated with emphysema and liver disease risk (feitosa12024recommendationsforthe pages 2-3, feitosa12024recommendationsforthe pages 1-2).
- **Heterozygotes** (e.g., Pi*MZ, Pi*SZ) can have increased lung disease risk that is highly contingent on exposures, particularly smoking (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2, fouka2026alpha1antitrypsindeficiencyassociated pages 2-4).

#### Environmental/lifestyle risk
- **Cigarette smoking** is a major modifier that accelerates emphysema progression and increases risk even for some heterozygotes; smoking oxidatively inactivates AAT and amplifies neutrophilic inflammation, worsening protease–antiprotease imbalance (fouka2026alpha1antitrypsindeficiencyassociated pages 2-4, turner2025advancingtheunderstanding pages 1-3).
- Broader **environmental exposures** are recognized modifiers interacting with genotype in determining emphysema risk (feitosa12024recommendationsforthe pages 1-2).

#### Gene–environment interactions (GxE)
A 2024 expert commentary highlights that **Pi*MZ heterozygotes** have a **~5–10× increased COPD risk if they smoke**, whereas **Pi*MZ never-smokers** have risk similar to **Pi*MM never-smokers**, illustrating a strong gene–smoking interaction (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2). Similar “nuanced risk” patterns are described for **Pi*SZ** individuals (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2).

### 2.3 Protective factors
- **Never smoking / smoking cessation** is strongly protective against development/progression of AATD-associated emphysema; early genetic diagnosis can facilitate smoking cessation and prevention-oriented counseling (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2).

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core pulmonary phenotypes
- **Emphysema / COPD**: classically earlier-onset emphysema (often before age 50) with heterogeneity in lobar patterns; protease–antiprotease imbalance drives progressive tissue destruction (fouka2026alpha1antitrypsindeficiencyassociated pages 1-2, fouka2026alpha1antitrypsindeficiencyassociated pages 2-4).
- **Bronchiectasis and airway-predominant disease**: AATD-related COPD can include airway-predominant disease, small airways dysfunction, chronic bronchitis, and bronchiectasis (fouka2026alpha1antitrypsindeficiencyassociated pages 1-2).
- **Asthma-like disease / late-onset asthma**: evaluation is recommended in some late-onset asthma contexts (feitosa12024recommendationsforthe pages 1-2).

**Suggested HPO terms (examples):**
- Emphysema **HP:0002097**
- Chronic obstructive pulmonary disease **HP:0006510**
- Bronchiectasis **HP:0002110**
- Reduced forced expiratory volume in 1 second **HP:0030440**
- Reduced diffusing capacity of the lungs for carbon monoxide (DLCO) **HP:0045051**

### 3.2 Hepatic phenotypes
- **Liver fibrosis/cirrhosis** from hepatocyte retention of misfolded/polymerized AAT; associated with hepatocellular damage and increased hepatocellular carcinoma risk (feitosa12024recommendationsforthe pages 2-3, mohammad2024livercharacterizationof pages 1-2).
- Transcriptomic evidence from a 2024 cohort study: livers of AATD individuals with COPD showed upregulation of pathways for **fibrosis, extracellular matrix remodeling, collagen deposition, hepatocellular damage, and inflammation**, with histologic evidence of higher fibrosis and injury (mohammad2024livercharacterizationof pages 1-2).

**Suggested HPO terms (examples):**
- Hepatic fibrosis **HP:0001395**
- Cirrhosis **HP:0001394**
- Elevated transaminases **HP:0002910**

### 3.3 Skin/immune and other systemic phenotypes
- **Necrotizing panniculitis** is a recognized manifestation and may be an indication for augmentation therapy in expert guidance (feitosa12024recommendationsforthe pages 1-2, turner2025advancingtheunderstanding pages 1-3).
- **Systemic vasculitis** (including granulomatosis with polyangiitis contexts) has been reported/recognized in the phenotype spectrum (feitosa12024recommendationsforthe pages 1-2).

**Suggested HPO terms (examples):**
- Panniculitis **HP:0001032**
- Vasculitis **HP:0002633**

### 3.4 Quality-of-life impact
A 2023 cohort comparison found that health status (SGRQ) deteriorated faster in augmentation-naïve severe AATD: **annual SGRQ deterioration 1.43 points/year greater** in controls versus augmented patients (95% CI 0.47–2.39; p=0.003), indicating meaningful QoL burden and potential modification by therapy (ellis2023qualityoflife pages 1-2).

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **SERPINA1** (serpin family A member 1) encodes AAT, a serine protease inhibitor (feitosa12024recommendationsforthe pages 2-3, mazzuca2024immunologicalandhomeostatic pages 1-2).

### 4.2 Pathogenic variants (common)
- **Z variant**: described as a glutamic acid→lysine substitution (position 342) that produces a misfolded protein prone to polymerization and hepatocyte retention, with severe deficiency (feitosa12024recommendationsforthe pages 2-3, feitosa12024recommendationsforthe pages 1-2). 
- **S variant**: common deficiency allele frequently paired with Z in compound heterozygosity (feitosa2023diagnosisandaugmentation pages 1-2, ferrarotti2024rarevariantsin pages 1-2).

**Variant nomenclature from a 2024 systematic review of rare variants:**
- Z: **c.1096G>A; p.Glu366Lys**
- S: **c.863A>T; p.Glu288Val** (ferrarotti2024rarevariantsin pages 1-2)

(Notes: other sources in this tool state describe Z as Glu342Lys; the discrepancy likely reflects different protein numbering conventions, but both refer to the canonical Z-deficiency allele; the report preserves the exact forms as stated in the cited sources.) (feitosa12024recommendationsforthe pages 2-3, ferrarotti2024rarevariantsin pages 1-2)

### 4.3 Variant classes and functional consequences
- **Loss-of-function in lung:** reduced circulating functional AAT removes inhibition of neutrophil elastase (NE) and related proteases (loss of antiprotease protection) (mazzuca2024immunologicalandhomeostatic pages 1-2, turner2025advancingtheunderstanding pages 1-3).
- **Gain-of-toxic-function in liver:** Z-AAT misfolding/polymerization causes ER retention and proteotoxic stress in hepatocytes (feitosa12024recommendationsforthe pages 2-3, mohammad2024livercharacterizationof pages 1-2).

### 4.4 Allele frequency / population distribution (selected)
- Normal **M allele** frequency: ~85–90% (feitosa12024recommendationsforthe pages 2-3).
- Example large DTC-genotyped cohort distribution (reported in a 2025 review): PI*MM 58.1%, PI*MS 28.3%, PI*MZ 12.1%, PI*SZ 0.6%, PI*ZZ 0.2% (yang2025nextgenerationregenerativetherapies pages 2-4).
- Z allele carrier frequency estimate: “~1 in 25 people of European ancestry” (feitosa12024recommendationsforthe pages 2-3).

### 4.5 Modifier genetics / epigenetics
- A 2024 guideline notes that “other genetic factors” interact with genotype and exposures to influence emphysema risk (feitosa12024recommendationsforthe pages 1-2).
- AATD registries include an “Epigenetic regulation of immunity” observational study (NCT02691611; retrieved but not expanded here), indicating active research interest; mechanistic epigenetic conclusions were not extractable from the currently retrieved excerpts.

---

## 5. Mechanism / pathophysiology

### 5.1 Lung disease causal chain (current model)
1) **SERPINA1 deficiency/dysfunction** → reduced functional AAT in blood and airway lining fluid (mazzuca2024immunologicalandhomeostatic pages 1-2, turner2025advancingtheunderstanding pages 1-3).
2) **Protease–antiprotease imbalance**: unopposed **neutrophil elastase** degrades lung elastin and extracellular matrix, driving emphysema progression (turner2025advancingtheunderstanding pages 1-3, yang2025nextgenerationregenerativetherapies pages 5-7).
3) **Inflammation amplification**: neutrophil proteases can activate inflammatory mediators; NETosis and cytokines (e.g., TNF-α, IL-6) contribute to sustained inflammation and recruitment (yang2025nextgenerationregenerativetherapies pages 5-7, yang2025nextgenerationregenerativetherapies pages 9-10).
4) **Exposure interaction**: smoking worsens oxidant stress and can impair AAT function, accelerating tissue destruction (fouka2026alpha1antitrypsindeficiencyassociated pages 2-4, turner2025advancingtheunderstanding pages 1-3).

**Relevant targets/pathways:**
- **ELANE (neutrophil elastase)** is a key mechanistic effector of lung damage in AATD and appears in disease–target associations (Open Targets) (feitosa12024recommendationsforthe pages 1-2).

**Suggested GO biological process terms (examples):**
- Neutrophil degranulation (GO:0043312)
- Inflammatory response (GO:0006954)
- Extracellular matrix disassembly (GO:0022617)
- Proteolysis (GO:0006508)

**Suggested CL cell types (examples):**
- Neutrophil (CL:0000775)
- Alveolar macrophage (CL:0000583)
- Alveolar type II pneumocyte (CL:0002063) (AEC2 implicated in inflammatory/UPR signatures in mechanistic reviews) (yang2025nextgenerationregenerativetherapies pages 4-5)

**Anatomical/UBERON:** lung (UBERON:0002048), alveolus (UBERON:0002299), small airway (UBERON:0002185).

### 5.2 Liver disease causal chain (current model)
1) **Z-AAT misfolding** → polymerization/aggregation and **retention in hepatocyte ER** (feitosa12024recommendationsforthe pages 2-3, mohammad2024livercharacterizationof pages 1-2).
2) **Proteotoxic stress** and perturbed proteostasis (ERAD/autophagy/proteasome handling) → ER stress/UPR-related signaling and inflammatory pathway activation (NF-κB, MAPK; JNK/CHOP-mediated injury described in mechanistic reviews) (yang2025nextgenerationregenerativetherapies pages 5-7).
3) Downstream consequences: hepatocellular injury, ECM remodeling/collagen deposition, progression to fibrosis/cirrhosis; risk is heterogeneous and may be worsened by systemic inflammation associated with COPD (mohammad2024livercharacterizationof pages 1-2).

**Suggested GO processes:**
- Response to endoplasmic reticulum stress (GO:0034976)
- Unfolded protein response (GO:0030968)
- Autophagy (GO:0006914)
- Collagen fibril organization (GO:0030199)

**Suggested cellular component (GO-CC):** endoplasmic reticulum lumen (GO:0005788); endoplasmic reticulum (GO:0005783).

---

## 6. Environmental information

### 6.1 Environmental/lifestyle modifiers
- **Smoking** is the dominant modifiable exposure: increases risk and accelerates progression of emphysema; can oxidatively impair AAT and intensify neutrophilic airway inflammation (fouka2026alpha1antitrypsindeficiencyassociated pages 2-4, turner2025advancingtheunderstanding pages 1-3).
- **Passive smoke exposure**, poverty, and structural inequities contribute to underdiagnosis and outcomes disparities in AATD-related lung disease (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2).

### 6.2 Infectious agents
No specific pathogen is a primary cause; infections are clinically relevant as exacerbation triggers in COPD. Observational reports describe reductions in infections/exacerbations after augmentation therapy initiation in some cohorts (mazzuca2024immunologicalandhomeostatic pages 9-10).

---

## 7. Anatomical structures affected

### 7.1 Organ level (primary)
- **Lung**: emphysema/COPD, bronchiectasis, small airway disease (fouka2026alpha1antitrypsindeficiencyassociated pages 1-2, fouka2026alpha1antitrypsindeficiencyassociated pages 2-4).
- **Liver**: fibrosis/cirrhosis, hepatocellular damage and cancer risk (mohammad2024livercharacterizationof pages 1-2).

### 7.2 Tissue/cell level
- Lung parenchyma elastin and interstitium; immune infiltrates dominated by neutrophils and macrophages (turner2025advancingtheunderstanding pages 1-3, yang2025nextgenerationregenerativetherapies pages 9-10).
- Hepatocytes as primary site of Z-AAT accumulation and fibrosis-related pathways (mohammad2024livercharacterizationof pages 1-2).

### 7.3 Subcellular
- **Endoplasmic reticulum** (ER retention of Z-AAT polymers) (feitosa12024recommendationsforthe pages 2-3, yang2025nextgenerationregenerativetherapies pages 5-7).

---

## 8. Temporal development (onset and progression)

- **Onset:** AATD is genetic (present from birth), but clinical presentation is variable and often adult-onset for lung disease; liver disease can appear in childhood and/or adulthood (biphasic pattern described in mechanistic review) (yang2025nextgenerationregenerativetherapies pages 2-4).
- **Progression:** lung disease is typically progressive; CT densitometry is described as a sensitive indicator of emphysema progression (feitosa12024recommendationsforthe pages 1-2, miravitlles2023ninecontroversialquestions pages 2-3).

---

## 9. Inheritance and population

### 9.1 Inheritance pattern
- **Autosomal codominant** inheritance is repeatedly stated (feitosa12024recommendationsforthe pages 1-2, feitosa2023diagnosisandaugmentation pages 1-2).

### 9.2 Epidemiology (selected recent quantitative estimates)
- Global burden: >3 million people worldwide estimated to have allele combinations associated with severe AATD (feitosa12024recommendationsforthe pages 1-2, feitosa12024recommendationsforthe pages 2-3).
- Underdiagnosis: “only ~10% diagnosed” is suggested in a 2024 guideline (feitosa12024recommendationsforthe pages 1-2); <10% identified is also stated in a 2026 review (fouka2026alpha1antitrypsindeficiencyassociated pages 1-2).
- Pi*ZZ prevalence estimates:
  - ~1:2,000–5,000 in Europe; ~1:5,000–7,000 in countries with substantial European immigration (feitosa12024recommendationsforthe pages 2-3).
  - ~1 in 3,000–5,000 in people of European descent (miravitlles2023ninecontroversialquestions pages 1-2).
- AATD contribution to COPD/emphysema: ~1% of COPD and up to 2% of emphysema (fouka2026alpha1antitrypsindeficiencyassociated pages 1-2).
- Registry scale: EARCO plans ~3,000 participants across >25 countries over 5 years and tracks FEV1, QoL, and mortality longitudinally (NCT04180319) (NCT04180319 chunk 1).

---

## 10. Diagnostics

### 10.1 Clinical tests and biomarkers
- **Serum AAT concentration** is the first-line quantitative test, followed by **phenotyping and/or genotyping** to identify allelic variants (feitosa12024recommendationsforthe pages 1-2).
- Typical normal serum AAT (Pi*MM): 100–220 mg/dL (guideline) (feitosa12024recommendationsforthe pages 2-3).
- **Severe deficiency threshold used for specific therapy eligibility**: **<57 mg/dL or <11 µM** (feitosa12024recommendationsforthe pages 1-2).

### 10.2 Functional and imaging tests
- **Spirometry** monitoring is emphasized, but **CT lung densitometry** is considered the most sensitive measure of emphysema progression (not recommended for routine monitoring in some guidance) (feitosa12024recommendationsforthe pages 1-2, miravitlles2023ninecontroversialquestions pages 2-3).

### 10.3 Screening and case-finding
- Major societies recommend testing high-risk groups (e.g., COPD, unexplained liver disease, panniculitis, vasculitis), and a 2024 ATS editorial emphasizes that the U.S. lacks newborn or generalized later-life screening for AATD and argues for population/targeted/family-based screening to reduce inequities (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2).

**Diagnostic algorithm (visual evidence):** a guideline diagnostic pathway figure was retrieved (feitosa12024recommendationsforthe media f6c82200).

---

## 11. Outcome / prognosis

### 11.1 Mortality and QoL outcomes (recent observational comparison)
A 2023 analysis of prospectively followed cohorts found:
- **Mean annual SGRQ deterioration**: 1.43 points/year worse in augmentation-naïve controls vs augmented patients (95% CI 0.47–2.39; p=0.003). 
- **7-year median survival**: 82.7% controls vs 87.8% augmented (p=0.66; not statistically significant) (ellis2023qualityoflife pages 1-2, ellis2023qualityoflife pages 3-4).

### 11.2 Prognostic factors
- **Smoking status** is a dominant prognostic modifier (accelerates emphysema; alters risk in heterozygotes) (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2, fouka2026alpha1antitrypsindeficiencyassociated pages 2-4).
- Disease heterogeneity complicates individual prognosis prediction, motivating registry-based prognostic tools (NCT04180319 chunk 1, miravitlles2023ninecontroversialquestions pages 2-3).

---

## 12. Treatment

### 12.1 Disease-specific pharmacotherapy: IV augmentation therapy (A1PI)
**Definition and core claims:** IV augmentation therapy is described as the **only specific disease-modifying therapy** for AATD-associated emphysema (miravitlles2023ninecontroversialquestions pages 1-2).

**Eligibility and thresholds:** generally for severe deficiency (often requiring serum AAT <11 µM or ~50–57 mg/dL) with emphysema and non-smoking status (feitosa12024recommendationsforthe pages 1-2, miravitlles2023ninecontroversialquestions pages 2-3).

**Dosing (common):** weekly IV 60 mg/kg is the standard regimen; alternative regimens have been explored but may provide less consistent time above protective thresholds (feitosa2023diagnosisandaugmentation pages 2-4, feitosa2023diagnosisandaugmentation pages 4-5).

**Effects / endpoints (quantitative):**
- CT densitometry benefit: pooled small RCTs (54 and 77 patients) showing reduction in lung density decline of **2.97 g·L−1 over 2 years** (miravitlles2023ninecontroversialquestions pages 1-2).
- A larger RCT (n=180) showed **0.74 g·L−1·year−1** benefit vs placebo in lung density (miravitlles2023ninecontroversialquestions pages 2-3).
- Systematic review estimate: **23% slowdown in FEV1 decline** (~13.4 mL/year; 95% CI 1.5–25.3 mL/year) (mazzuca2024immunologicalandhomeostatic pages 9-10).

**Controversies / expert opinion:** A 2023 ERS viewpoint argues that because AATD is rare and heterogeneous, trials powered for conventional COPD outcomes are difficult; CT lung densitometry is more sensitive but not widely accepted by regulators, and therefore augmentation decisions should be personalized in reference centers (miravitlles2023ninecontroversialquestions pages 1-2, miravitlles2023ninecontroversialquestions pages 2-3).

**MAXO suggestions:**
- Intravenous infusion therapy (MAXO:0001052)
- Protein replacement therapy (MAXO:0000647)

### 12.2 COPD/emphysema standard care
Treatment broadly follows standard COPD principles (bronchodilators, pulmonary rehab, vaccinations, smoking cessation), with augmentation as the disease-specific modifier for selected severe patients (feitosa12024recommendationsforthe pages 1-2, fouka2026alpha1antitrypsindeficiencyassociated pages 1-2).

### 12.3 Advanced therapeutics and emerging clinical development (selected trials)
**Recombinant long-acting A1PI biologic:**
- **INBRX-101 / SAR447537** Phase 2 active-controlled trial (ELEVAATE): compares recombinant bivalent Fc-fusion A1PI vs weekly plasma-derived augmentation, using functional AAT (anti-neutrophil elastase capacity) as primary outcome (NCT05856331; first posted 2023-05-12; completed 2025-08-06) (NCT05856331 chunk 1).

**Airway gene delivery (HSV-1 vector expressing SERPINA1):**
- **KB408 (Serpentine-1)** Phase 1 inhaled HSV-1 vector delivering full-length SERPINA1 via nebulization; measures include serum AAT and neutrophil elastase in plasma and BAL (NCT06049082; first posted 2023-09-21; recruiting; start 2024-02-15) (NCT06049082 chunk 1).

**RNAi gene silencing (liver-targeted; historical example):**
- **ALN-AAT** Phase 1/2 RNAi therapeutic trial in ZZ liver disease was terminated due to transient liver enzyme elevations (NCT02503683; posted 2015-07-21; terminated 2019-01) (NCT02503683 chunk 1).

**In vivo gene editing (withdrawn early):**
- **NTLA-3001** Phase 1/2 CRISPR/Cas9 AAV program for AATD-associated lung disease was withdrawn due to sponsor prioritization (NCT06622668; first posted 2024-10-02; withdrawn 2025-01-17) (NCT06622668 chunk 1).

**Mechanism-based emerging strategies:** Reviews describe iPSC-based and CRISPR gene editing approaches for disease modeling and potential curative strategies, including mutation correction to test causality and evaluate therapeutics (yang2025nextgenerationregenerativetherapies pages 1-2, yang2025nextgenerationregenerativetherapies pages 2-4).

---

## 13. Prevention

### 13.1 Primary prevention
- **Avoidance of smoking** (including passive exposure) and smoking cessation are central preventative strategies; early genetic diagnosis enables preventive counseling (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2).

### 13.2 Secondary prevention
- **Targeted testing** in COPD and other high-risk clinical settings is emphasized due to major underdiagnosis and earlier-onset disease (feitosa12024recommendationsforthe pages 1-2, turner2025advancingtheunderstanding pages 1-3).
- **Cascade/family testing** is recommended as a case-finding tool and equity measure (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2, feitosa12024recommendationsforthe pages 1-2).

### 13.3 Tertiary prevention
- Augmentation therapy aims to slow emphysema progression measured by CT densitometry (miravitlles2023ninecontroversialquestions pages 1-2, miravitlles2023ninecontroversialquestions pages 2-3).

---

## 14. Other species / natural disease

The current retrieved excerpts do not provide disease-specific, naturally occurring AATD analogs in non-human species with definitive genetic orthology assertions and curated identifiers (e.g., OMIA). No zoonotic transmission is applicable.

---

## 15. Model organisms / experimental models

### 15.1 Mouse models
Mechanistic reviews refer to **PiZ mouse models** as core in vivo systems for hepatic proteotoxicity and lung/liver pathobiology, including studies comparing iron-related modifiers (Hfe KO context) (yang2025nextgenerationregenerativetherapies pages 2-4).

### 15.2 Human iPSC / organoids and gene editing
Recent reviews describe the use of **patient-derived iPSCs**, **iPSC-derived organoids**, and **CRISPR-based gene correction** to model AATD and to link genotype to cellular phenotypes, supporting drug discovery and regenerative approaches (yang2025nextgenerationregenerativetherapies pages 1-2, yang2025nextgenerationregenerativetherapies pages 2-4).

### 15.3 Clinical “model” resources: real-world registry
The **EARCO** registry provides a large-scale longitudinal observational framework for genotype/phenotype and treatment-effect modeling, including augmentation therapy effects on emphysema progression, FEV1, QoL, and mortality (NCT04180319) (NCT04180319 chunk 1).

---

## Visual evidence (guideline figures/tables retrieved)
- **SERPINA1 allele chart / clinical significance** (includes Z/S/null and clinical risk associations): (feitosa12024recommendationsforthe media 68858213)
- **Diagnostic algorithm figure** for AATD confirmation after screening serum AAT and/or genotyping: (feitosa12024recommendationsforthe media f6c82200)
- **Augmentation therapy criteria across international guidance** (thresholds/criteria table): (feitosa12024recommendationsforthe media 1c9be2df)

---

## Direct abstract quotes (supporting key statements)
- Underdiagnosis and organ involvement: “**Unfortunately, underdiagnosis is quite common; it is possible that only 10% of cases are diagnosed**.” (Feitosa et al., 2024, *Jornal Brasileiro de Pneumologia*, published Nov 2024, https://doi.org/10.36416/1806-3756/e20240235) (feitosa12024recommendationsforthe pages 1-2)
- Augmentation therapy effects (mechanistic/endpoint framing): “**Augmentation therapy with AAT increases serum and pulmonary epithelial AAT levels, restores anti-elastase capacity, and decreases inflammatory mediators in the lung.**” (Feitosa, 2023, *Drugs in Context*, published Jul 2023, https://doi.org/10.7573/dic.2023-3-1) (feitosa2023diagnosisandaugmentation pages 1-2)
- Augmentation therapy trial limitations: “Because AATD is a rare disease, it has not been possible to conduct randomised, placebo-controlled trials that are adequately powered for … outcomes … such as lung function decline, exacerbations, symptoms or quality of life.” (Miravitlles et al., 2023, *European Respiratory Review*, published Dec 2023, https://doi.org/10.1183/16000617.0170-2023) (miravitlles2023ninecontroversialquestions pages 1-2)

---

## Key real-world implementation points (2023–2024 emphasis)
- **Guideline-based case finding and treatment thresholds (2024):** severe deficiency defined by **AAT <57 mg/dL or <11 µM**, with phenotyping/genotyping confirmation and COPD-like management plus augmentation in selected severe cases (feitosa12024recommendationsforthe pages 1-2, feitosa12024recommendationsforthe media 1c9be2df).
- **Equity and screening discussion (2024 ATS editorial):** AATD remains underdiagnosed; early genetic diagnosis enables preventive smoking cessation and family testing; U.S. lacks newborn screening and broad screening programs (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2).

---

## Requested items not fully satisfied from retrieved evidence
- **OMIM / Orphanet / ICD-10/ICD-11 / MeSH IDs**: not extractable from currently retrieved texts.
- **Population incidence**: not found in retrieved excerpts.
- **Comprehensive protective-factor catalog** (beyond smoking avoidance): insufficient evidence in retrieved excerpts.
- **Validated epigenetic biomarkers**: not extractable from retrieved excerpts.



References

1. (feitosa12024recommendationsforthe pages 1-2): Paulo Henrique Ramos Feitosa1, Maria Vera Cruz de Oliveira Castellano2, Claudia Henrique da Costa, Amanda da Rocha Oliveira Cardoso4, Luiz Fernando Ferreira Pereira5, Frederico Leon Arrabal Fernandes6, Fábio Marcelo Costa7, Manuela Brisot Felisbino8, Alina Faria França de Oliveira9, Jose R Jardim10, and Marc Miravitlles11. Recommendations for the diagnosis and treatment of alpha-1 antitrypsin deficiency. Jornal Brasileiro de Pneumologia, 50:e20240235, Nov 2024. URL: https://doi.org/10.36416/1806-3756/e20240235, doi:10.36416/1806-3756/e20240235. This article has 9 citations and is from a peer-reviewed journal.

2. (feitosa12024recommendationsforthe pages 2-3): Paulo Henrique Ramos Feitosa1, Maria Vera Cruz de Oliveira Castellano2, Claudia Henrique da Costa, Amanda da Rocha Oliveira Cardoso4, Luiz Fernando Ferreira Pereira5, Frederico Leon Arrabal Fernandes6, Fábio Marcelo Costa7, Manuela Brisot Felisbino8, Alina Faria França de Oliveira9, Jose R Jardim10, and Marc Miravitlles11. Recommendations for the diagnosis and treatment of alpha-1 antitrypsin deficiency. Jornal Brasileiro de Pneumologia, 50:e20240235, Nov 2024. URL: https://doi.org/10.36416/1806-3756/e20240235, doi:10.36416/1806-3756/e20240235. This article has 9 citations and is from a peer-reviewed journal.

3. (mohammad2024livercharacterizationof pages 1-2): Naweed Mohammad, Regina Oshins, Tongjun Gu, Virginia Clark, Jorge Lascano, Naziheh Assarzadegan, George Marek, Mark Brantly, and Nazli Khodayari. Liver characterization of a cohort of alpha-1 antitrypsin deficiency patients with and without lung disease. Journal of Clinical and Translational Hepatology, 12:845-856, Sep 2024. URL: https://doi.org/10.14218/jcth.2024.00201, doi:10.14218/jcth.2024.00201. This article has 5 citations.

4. (feitosa2023diagnosisandaugmentation pages 1-2): Paulo Henrique Ramos Feitosa. Diagnosis and augmentation therapy for alpha-1 antitrypsin deficiency: current knowledge and future potential. Drugs in Context, 12:1-9, Jul 2023. URL: https://doi.org/10.7573/dic.2023-3-1, doi:10.7573/dic.2023-3-1. This article has 17 citations.

5. (fouka2026alpha1antitrypsindeficiencyassociated pages 1-2): Evangelia Fouka, Argyro Vrouvaki, Marina Moustaka Christodoulou, Stelios Loukides, and Georgios Hillas. Alpha-1 antitrypsin deficiency-associated chronic obstructive pulmonary disease. Medicina, 62:639, Mar 2026. URL: https://doi.org/10.3390/medicina62040639, doi:10.3390/medicina62040639. This article has 0 citations.

6. (NCT04180319 chunk 1):  EARCO REGISTRY. History Of Patients With Alpha-1 Antitrypsin. Hospital Universitari Vall d'Hebron Research Institute. 2020. ClinicalTrials.gov Identifier: NCT04180319

7. (feitosa2023diagnosisandaugmentation pages 4-5): Paulo Henrique Ramos Feitosa. Diagnosis and augmentation therapy for alpha-1 antitrypsin deficiency: current knowledge and future potential. Drugs in Context, 12:1-9, Jul 2023. URL: https://doi.org/10.7573/dic.2023-3-1, doi:10.7573/dic.2023-3-1. This article has 17 citations.

8. (miravitlles2023ninecontroversialquestions pages 2-3): Marc Miravitlles, Antonio Anzueto, and Miriam Barrecheguren. Nine controversial questions about augmentation therapy for alpha-1 antitrypsin deficiency: a viewpoint. European Respiratory Review, 32:230170, Dec 2023. URL: https://doi.org/10.1183/16000617.0170-2023, doi:10.1183/16000617.0170-2023. This article has 24 citations and is from a peer-reviewed journal.

9. (mcelvaney2024undiagnosedalpha1antitrypsin pages 1-2): Oliver J. McElvaney, Jon Hagstrom, Marilyn G. Foreman, and Noel G. McElvaney. Undiagnosed alpha-1 antitrypsin deficiency and the perpetuation of lung health inequity. American Journal of Respiratory and Critical Care Medicine, 209:3-5, Jan 2024. URL: https://doi.org/10.1164/rccm.202307-1171ed, doi:10.1164/rccm.202307-1171ed. This article has 8 citations and is from a highest quality peer-reviewed journal.

10. (fouka2026alpha1antitrypsindeficiencyassociated pages 2-4): Evangelia Fouka, Argyro Vrouvaki, Marina Moustaka Christodoulou, Stelios Loukides, and Georgios Hillas. Alpha-1 antitrypsin deficiency-associated chronic obstructive pulmonary disease. Medicina, 62:639, Mar 2026. URL: https://doi.org/10.3390/medicina62040639, doi:10.3390/medicina62040639. This article has 0 citations.

11. (turner2025advancingtheunderstanding pages 1-3): Alice M. Turner, Joachim H. Ficker, Andrea Vianello, Christian F. Clarenbach, Sabina Janciauskiene, Joanna Chorostowska-Wynimko, Jan Stolk, and Noel Gerard McElvaney. Advancing the understanding and treatment of lung pathologies associated with alpha 1 antitrypsin deficiency. Therapeutic Advances in Respiratory Disease, Jan 2025. URL: https://doi.org/10.1177/17534666251318841, doi:10.1177/17534666251318841. This article has 12 citations.

12. (ellis2023qualityoflife pages 1-2): Paul R. Ellis, Kristen E. Holm, Radmila Choate, David M. Mannino, Robert A. Stockley, Robert A. Sandhaus, and Alice M. Turner. Quality of life and mortality outcomes for augmentation naïve and augmented patients with severe alpha-1 antitrypsin deficiency. Chronic obstructive pulmonary diseases, 10:139-147, Feb 2023. URL: https://doi.org/10.15326/jcopdf.2022.0339, doi:10.15326/jcopdf.2022.0339. This article has 17 citations.

13. (mazzuca2024immunologicalandhomeostatic pages 1-2): Carmen Mazzuca, Laura Vitiello, Silvia Travaglini, Fatima Maurizi, Panaiotis Finamore, Simona Santangelo, Amelia Rigon, Marta Vadacca, Silvia Angeletti, and Simone Scarlata. Immunological and homeostatic pathways of alpha -1 antitrypsin: a new therapeutic potential. Frontiers in Immunology, Aug 2024. URL: https://doi.org/10.3389/fimmu.2024.1443297, doi:10.3389/fimmu.2024.1443297. This article has 29 citations and is from a peer-reviewed journal.

14. (ferrarotti2024rarevariantsin pages 1-2): Ilaria Ferrarotti, Marion Wencker, and Joanna Chorostowska-Wynimko. Rare variants in alpha 1 antitrypsin deficiency: a systematic literature review. Orphanet Journal of Rare Diseases, Feb 2024. URL: https://doi.org/10.1186/s13023-024-03069-1, doi:10.1186/s13023-024-03069-1. This article has 33 citations and is from a peer-reviewed journal.

15. (yang2025nextgenerationregenerativetherapies pages 2-4): Se-Ran Yang and Hyung-Ryong Kim. Next-generation regenerative therapies for alpha-1 antitrypsin deficiency: molecular pathogenesis to clinical translation. International Journal of Molecular Sciences, 26:8504, Sep 2025. URL: https://doi.org/10.3390/ijms26178504, doi:10.3390/ijms26178504. This article has 1 citations.

16. (yang2025nextgenerationregenerativetherapies pages 5-7): Se-Ran Yang and Hyung-Ryong Kim. Next-generation regenerative therapies for alpha-1 antitrypsin deficiency: molecular pathogenesis to clinical translation. International Journal of Molecular Sciences, 26:8504, Sep 2025. URL: https://doi.org/10.3390/ijms26178504, doi:10.3390/ijms26178504. This article has 1 citations.

17. (yang2025nextgenerationregenerativetherapies pages 9-10): Se-Ran Yang and Hyung-Ryong Kim. Next-generation regenerative therapies for alpha-1 antitrypsin deficiency: molecular pathogenesis to clinical translation. International Journal of Molecular Sciences, 26:8504, Sep 2025. URL: https://doi.org/10.3390/ijms26178504, doi:10.3390/ijms26178504. This article has 1 citations.

18. (yang2025nextgenerationregenerativetherapies pages 4-5): Se-Ran Yang and Hyung-Ryong Kim. Next-generation regenerative therapies for alpha-1 antitrypsin deficiency: molecular pathogenesis to clinical translation. International Journal of Molecular Sciences, 26:8504, Sep 2025. URL: https://doi.org/10.3390/ijms26178504, doi:10.3390/ijms26178504. This article has 1 citations.

19. (mazzuca2024immunologicalandhomeostatic pages 9-10): Carmen Mazzuca, Laura Vitiello, Silvia Travaglini, Fatima Maurizi, Panaiotis Finamore, Simona Santangelo, Amelia Rigon, Marta Vadacca, Silvia Angeletti, and Simone Scarlata. Immunological and homeostatic pathways of alpha -1 antitrypsin: a new therapeutic potential. Frontiers in Immunology, Aug 2024. URL: https://doi.org/10.3389/fimmu.2024.1443297, doi:10.3389/fimmu.2024.1443297. This article has 29 citations and is from a peer-reviewed journal.

20. (miravitlles2023ninecontroversialquestions pages 1-2): Marc Miravitlles, Antonio Anzueto, and Miriam Barrecheguren. Nine controversial questions about augmentation therapy for alpha-1 antitrypsin deficiency: a viewpoint. European Respiratory Review, 32:230170, Dec 2023. URL: https://doi.org/10.1183/16000617.0170-2023, doi:10.1183/16000617.0170-2023. This article has 24 citations and is from a peer-reviewed journal.

21. (feitosa12024recommendationsforthe media f6c82200): Paulo Henrique Ramos Feitosa1, Maria Vera Cruz de Oliveira Castellano2, Claudia Henrique da Costa, Amanda da Rocha Oliveira Cardoso4, Luiz Fernando Ferreira Pereira5, Frederico Leon Arrabal Fernandes6, Fábio Marcelo Costa7, Manuela Brisot Felisbino8, Alina Faria França de Oliveira9, Jose R Jardim10, and Marc Miravitlles11. Recommendations for the diagnosis and treatment of alpha-1 antitrypsin deficiency. Jornal Brasileiro de Pneumologia, 50:e20240235, Nov 2024. URL: https://doi.org/10.36416/1806-3756/e20240235, doi:10.36416/1806-3756/e20240235. This article has 9 citations and is from a peer-reviewed journal.

22. (ellis2023qualityoflife pages 3-4): Paul R. Ellis, Kristen E. Holm, Radmila Choate, David M. Mannino, Robert A. Stockley, Robert A. Sandhaus, and Alice M. Turner. Quality of life and mortality outcomes for augmentation naïve and augmented patients with severe alpha-1 antitrypsin deficiency. Chronic obstructive pulmonary diseases, 10:139-147, Feb 2023. URL: https://doi.org/10.15326/jcopdf.2022.0339, doi:10.15326/jcopdf.2022.0339. This article has 17 citations.

23. (feitosa2023diagnosisandaugmentation pages 2-4): Paulo Henrique Ramos Feitosa. Diagnosis and augmentation therapy for alpha-1 antitrypsin deficiency: current knowledge and future potential. Drugs in Context, 12:1-9, Jul 2023. URL: https://doi.org/10.7573/dic.2023-3-1, doi:10.7573/dic.2023-3-1. This article has 17 citations.

24. (NCT05856331 chunk 1):  Study of SAR447537 (INBRX-101) Compared to Plasma-derived A1PI Therapy in Adults With AATD Emphysema. Sanofi. 2023. ClinicalTrials.gov Identifier: NCT05856331

25. (NCT06049082 chunk 1):  A Study of KB408 for the Treatment of Alpha-1 Antitrypsin Deficiency. Krystal Biotech, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06049082

26. (NCT02503683 chunk 1):  A Study of an Investigational Drug, ALN-AAT, in Healthy Adult Subjects and Patients With ZZ Type Alpha-1 Antitrypsin Deficiency Liver Disease. Alnylam Pharmaceuticals. 2015. ClinicalTrials.gov Identifier: NCT02503683

27. (NCT06622668 chunk 1):  NTLA-3001 in Adults with Alpha-1 Antitrypsin Deficiency-Associated Lung Disease. Intellia Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06622668

28. (yang2025nextgenerationregenerativetherapies pages 1-2): Se-Ran Yang and Hyung-Ryong Kim. Next-generation regenerative therapies for alpha-1 antitrypsin deficiency: molecular pathogenesis to clinical translation. International Journal of Molecular Sciences, 26:8504, Sep 2025. URL: https://doi.org/10.3390/ijms26178504, doi:10.3390/ijms26178504. This article has 1 citations.

29. (feitosa12024recommendationsforthe media 68858213): Paulo Henrique Ramos Feitosa1, Maria Vera Cruz de Oliveira Castellano2, Claudia Henrique da Costa, Amanda da Rocha Oliveira Cardoso4, Luiz Fernando Ferreira Pereira5, Frederico Leon Arrabal Fernandes6, Fábio Marcelo Costa7, Manuela Brisot Felisbino8, Alina Faria França de Oliveira9, Jose R Jardim10, and Marc Miravitlles11. Recommendations for the diagnosis and treatment of alpha-1 antitrypsin deficiency. Jornal Brasileiro de Pneumologia, 50:e20240235, Nov 2024. URL: https://doi.org/10.36416/1806-3756/e20240235, doi:10.36416/1806-3756/e20240235. This article has 9 citations and is from a peer-reviewed journal.

30. (feitosa12024recommendationsforthe media 1c9be2df): Paulo Henrique Ramos Feitosa1, Maria Vera Cruz de Oliveira Castellano2, Claudia Henrique da Costa, Amanda da Rocha Oliveira Cardoso4, Luiz Fernando Ferreira Pereira5, Frederico Leon Arrabal Fernandes6, Fábio Marcelo Costa7, Manuela Brisot Felisbino8, Alina Faria França de Oliveira9, Jose R Jardim10, and Marc Miravitlles11. Recommendations for the diagnosis and treatment of alpha-1 antitrypsin deficiency. Jornal Brasileiro de Pneumologia, 50:e20240235, Nov 2024. URL: https://doi.org/10.36416/1806-3756/e20240235, doi:10.36416/1806-3756/e20240235. This article has 9 citations and is from a peer-reviewed journal.