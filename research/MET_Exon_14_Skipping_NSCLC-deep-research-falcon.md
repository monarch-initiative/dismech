---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T19:24:54.503708'
end_time: '2026-04-05T19:32:08.340566'
duration_seconds: 433.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MET Exon 14 Skipping Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MET Exon 14 Skipping Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **MET Exon 14 Skipping Non-Small Cell Lung Cancer** covering all of the
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
- **Disease Name:** MET Exon 14 Skipping Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **MET Exon 14 Skipping Non-Small Cell Lung Cancer** covering all of the
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


# Comprehensive Research Report: MET Exon 14 Skipping Non-Small Cell Lung Cancer (METex14 NSCLC)

## Target Disease
- **Disease name:** MET Exon 14 Skipping Non-Small Cell Lung Cancer (NSCLC)
- **Category:** Molecularly defined subtype of NSCLC driven by *MET* exon 14 skipping alterations (somatic driver event)
- **MONDO ID:** Not retrieved from the provided sources in this run (no explicit MONDO mapping found in the accessed texts).

---

## 1. Disease Information

### 1.1 Overview / definition
MET exon 14 skipping NSCLC is a subset of NSCLC in which heterogeneous genomic alterations at the *MET* exon 14 splice donor/acceptor region lead to RNA splicing that excludes exon 14 (“METex14”), producing an oncogenic MET receptor with impaired downregulation and sustained signaling. This is widely described as an actionable oncogenic driver in lung cancer. (gow2023survivaloutcomesand pages 1-2, loyaux2024metexon14 pages 1-5)

### 1.2 Synonyms / alternative names
Common names used in the literature include:
- **“MET exon 14 skipping mutation”**
- **“METex14”**
- **“MET exon 14 skipping variant”**
- **“METΔex14”** (delta exon 14)
(gow2023survivaloutcomesand pages 1-2, yuan2023metexon14 pages 1-2)

### 1.3 Key identifiers (ontology / coding systems)
- **MeSH / ICD-10 / ICD-11 / OMIM / Orphanet / MONDO:** Not explicitly provided in the retrieved evidence snippets for this run.
- Practically, this entity is captured clinically as NSCLC (often lung adenocarcinoma) with a molecular alteration (*MET* exon 14 skipping). (yuan2023metexon14 pages 1-2)

### 1.4 Evidence source type
Most disease-characterization information in this report is derived from **aggregated resources** (reviews) and **human clinical cohorts** (retrospective real-world series, prospective/registrational clinical trials). Some mechanistic evidence is **in vitro** (cell line functional assays). (loyaux2024metexon14 pages 1-5, babey2023realworldtreatmentoutcomes pages 1-2, yang2024vebreltinibforadvanced pages 1-2, mazieres2023tepotinibtreatmentin pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors (genetic/mechanistic)
**Primary causal factor:** Somatic genomic alterations disrupting *MET* exon 14 splicing (splice site point mutations, insertions, deletions, including larger deletions) that result in **exon 14 skipping at the RNA level**. The alterations are described as highly heterogeneous and can be missed by single-modality DNA-only assays. (loyaux2024metexon14 pages 1-5, spagnolo2023targetingmetin pages 2-3)

**Key mechanistic definition:** Exon 14 encodes a regulatory juxtamembrane region containing Tyr1003, which is required for binding of the E3 ubiquitin ligase CBL, enabling ubiquitination/internalization and degradation of MET. Exon 14 skipping removes this region, reducing receptor ubiquitination and degradation and increasing MET signaling. (spagnolo2023targetingmetin pages 2-3, loyaux2024metexon14 pages 1-5)

### 2.2 Risk factors
Risk factors in the strict sense (exposures causing METex14) are not established in the retrieved sources; however, **demographic and clinicopathologic associations** are consistently observed in cohorts:
- METex14-positive lung cancer patients were reported to be “**generally elderly individuals, never-smokers**” in a real-world cohort. (gow2023survivaloutcomesand pages 1-2)
- A large real-world French cohort had **median age 73** and **62.7% female**. (babey2023realworldtreatmentoutcomes pages 1-2)

**Histology enrichment:** METex14 is enriched in pulmonary sarcomatoid carcinoma (PSC). A single-center study reported **24.3% (9/37)** METex14 in PSC. (gow2023survivaloutcomesand pages 1-2)

### 2.3 Protective factors
No genetic or environmental protective factors specific to developing METex14 NSCLC were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No METex14-specific gene–environment interaction evidence was retrieved.

---

## 3. Phenotypes (clinical presentation)

Because METex14 NSCLC is a molecular subtype of NSCLC, phenotypes are largely those of lung cancer, with additional features related to metastatic pattern and biomarker profile.

### 3.1 Core clinical phenotypes
- **Lung cancer symptoms/signs:** cough, dyspnea, hemoptysis, chest pain, weight loss (general NSCLC phenotype; not explicitly quantified in retrieved sources).
- **Advanced stage at detection in many cohorts:** In the GFPC 03-18 cohort, **92.4% were stage IV**. (babey2023realworldtreatmentoutcomes pages 1-2)
- **Brain metastasis as prognostic/clinical feature:** “Initial brain metastasis” was an independent poor prognostic factor in advanced METex14 lung adenocarcinoma in a real-world cohort. (gow2023survivaloutcomesand pages 1-2)

### 3.2 Biomarker phenotypes (tumor immune markers)
High PD-L1 expression is common but not clearly predictive of immunotherapy benefit in available real-world evidence:
- In a screening cohort, **67%** of METex14 tumors had **PD-L1 >50%**. (loyaux2024metexon14 pages 1-5)

### 3.3 Suggested HPO terms (examples)
(Phenotypes are lung-cancer related; examples suitable for a knowledge base entry)
- **HP:0002094** Hemoptysis
- **HP:0002090** Dyspnea
- **HP:0012735** Cough
- **HP:0002664** Neoplasm of the lung
- **HP:0002662** Metastatic neoplasm (if applicable)
- **HP:0002133** Status epilepticus / **HP:0001249** Intellectual disability are *not* typical; for CNS metastasis consider:
  - **HP:0002893** Brain metastasis (term availability may vary; alternatively encode as “metastatic malignant neoplasm in brain” in SNOMED/ICD)

*Note:* Specific HPO term IDs for “brain metastasis” may require mapping via HPO/SNOMED resources not accessed in this run.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **Gene:** *MET* (MET proto-oncogene, receptor tyrosine kinase)
- **Alteration class:** Somatic splice-altering variants leading to **MET exon 14 skipping** (driver event). (spagnolo2023targetingmetin pages 2-3, yuan2023metexon14 pages 1-2)

### 4.2 Pathogenic variant classes that cause exon skipping
- Disrupted splice donor/acceptor sites near exon 14 due to **point mutations, insertions, deletions**, including larger deletions that may be missed by DNA-only NGS. (spagnolo2023targetingmetin pages 2-3, loyaux2024metexon14 pages 1-5)

### 4.3 Functional consequences (causal chain)
1. **Genomic alteration** disrupts exon 14 splicing →
2. **Exon 14 is skipped in the mRNA** →
3. MET protein lacks juxtamembrane regulatory sequence including CBL binding site (Tyr1003) →
4. Reduced ubiquitination/internalization/lysosomal degradation →
5. Increased MET receptor stability and signaling →
6. Activation of downstream oncogenic pathways promoting proliferation, survival, motility, EMT. (spagnolo2023targetingmetin pages 2-3, loyaux2024metexon14 pages 1-5)

Downstream pathways explicitly noted include **RAS–RAF–MEK–MAPK** and **PI3K/AKT**, as well as STAT and NF-κB. (spagnolo2023targetingmetin pages 2-3)

### 4.4 Co-mutations / potential modifiers
In a screening series of METex14 tumors (n=46), **42%** had co-occurring alterations, most commonly **TP53 (24%)** and **PIK3CA (9%)**. (loyaux2024metexon14 pages 1-5)

### 4.5 Epigenetic information
No METex14-specific methylation/histone modification mechanism evidence was retrieved in the accessed texts.

### 4.6 Suggested GO terms (biological processes) and CL terms (cell types)
**GO (examples):**
- **GO:0007169** transmembrane receptor protein tyrosine kinase signaling pathway
- **GO:0038128** ERBB2 signaling pathway (not specific) vs more appropriate:
- **GO:0007173** epidermal growth factor receptor signaling pathway (not specific)
- **GO:0014068** positive regulation of phosphatidylinositol 3-kinase signaling
- **GO:0071902** positive regulation of protein serine/threonine kinase activity
- **GO:0001837** epithelial to mesenchymal transition

**CL (examples):**
- **CL:0000084** T cell (tumor immune microenvironment context)
- **CL:0000066** epithelial cell
- **CL:0002631** lung alveolar type II cell (a common inferred cell-of-origin for lung adenocarcinoma)

*Note:* GO/CL suggestions are ontology mappings; direct ontology annotations were not provided in the retrieved papers.

---

## 5. Environmental Information

No METex14-specific environmental exposures were identified in the retrieved sources. General lung cancer risk factors (e.g., smoking, occupational exposures) apply at the NSCLC level but were not quantified in the provided evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Key molecular mechanism
The defining mechanism is impaired MET downregulation due to loss of the exon 14–encoded juxtamembrane regulatory segment, increasing MET signaling output and driving oncogenesis. (spagnolo2023targetingmetin pages 2-3, loyaux2024metexon14 pages 1-5)

### 6.2 Tumor biology and signaling
MET activation propagates multiple growth and survival pathways (e.g., MAPK and PI3K/AKT), supporting proliferation, survival, motility, and EMT. (spagnolo2023targetingmetin pages 2-3)

### 6.3 Immune microenvironment considerations
Although high PD-L1 expression is frequent (e.g., 67% with PD-L1 >50% in one cohort), real-world evidence suggests relatively limited immunotherapy efficacy in many patients, motivating prioritization of MET-targeted therapy when feasible. (loyaux2024metexon14 pages 1-5)

---

## 7. Anatomical Structures Affected

### 7.1 Primary organ/system
- **Primary:** Lung (respiratory system), typically NSCLC histologies including adenocarcinoma and sarcomatoid carcinoma enrichment. (gow2023survivaloutcomesand pages 1-2, babey2023realworldtreatmentoutcomes pages 1-2)

### 7.2 Secondary involvement
- **Brain metastasis** is clinically important and prognostic in advanced disease. (gow2023survivaloutcomesand pages 1-2)

### 7.3 Suggested UBERON terms (examples)
- **UBERON:0002048** lung
- **UBERON:0000955** brain

---

## 8. Temporal Development

### 8.1 Onset
This is primarily an **adult/older-adult** cancer subtype. Cohort medians around early 70s were reported (median age 72–73 in VISION and a French real-world cohort). (mazieres2023tepotinibtreatmentin pages 1-2, babey2023realworldtreatmentoutcomes pages 1-2)

### 8.2 Progression/course
Many patients present with advanced/metastatic disease in real-world cohorts (e.g., stage IV predominance). (babey2023realworldtreatmentoutcomes pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance
METex14 in NSCLC is generally a **somatic (acquired) oncogenic driver**, not a Mendelian inherited condition. (yuan2023metexon14 pages 1-2)

### 9.2 Epidemiology (prevalence)
Across sources, MET exon 14 skipping is described as a relatively rare but clinically significant NSCLC driver:
- A clinical screening report describes published prevalence estimates of **~1–4%** of NSCLC. (loyaux2024metexon14 pages 1-5)
- A retrospective molecular pathology cohort found **1.9%** MET exon 14 variants among 2296 NSCLCs (with most being exon 14 skipping). (yuan2023metexon14 pages 1-2)

**Histology-specific enrichment:** pulmonary sarcomatoid carcinoma shows markedly higher rates (e.g., 24.3% in one cohort). (gow2023survivaloutcomesand pages 1-2)

---

## 10. Diagnostics

### 10.1 Key diagnostic concept
Because METex14 is defined by **RNA exon skipping** but caused by diverse **DNA splice region alterations**, optimal detection often requires strategies that can directly assess splicing (RNA) and/or cover diverse DNA events.

### 10.2 Testing modalities and pitfalls
- **NGS (DNA and/or RNA):** NGS is described as “the most useful method” for MET alterations but targeted DNA amplicon approaches may miss METex14 due to the high diversity of variants. (spagnolo2023targetingmetin pages 2-3)
- **RT-PCR:** Sensitive and low-cost, but can fail when nucleic acids are fragmented, especially in small/poor specimens. (spagnolo2023targetingmetin pages 2-3)
- **IHC:** Not adequate as a screening test for METex14 (false negatives reported). (spagnolo2023targetingmetin pages 2-3, makimoto2024diagnosisandtreatment pages 1-2)

### 10.3 Quantitative diagnostic performance (recent cohorts)
**Latin American cohort (52-gene NGS panel, n=1560 biopsies):**
- Abstract quote: “**RNA-based diagnosis detected 27% more cases of METex14 than DNA-based methods. Notably, 20% of METex14 cases with RNA reads below the detection threshold were confirmed using DNA analysis.**” (Rivas et al., 2024; https://doi.org/10.3390/ijms252413715) (loyaux2024metexon14 pages 1-5)

**Three-year screening experience (n=1143):** 4 of 46 alterations were missed by DNA sequencing and “rescued” by fragment analysis or RNA sequencing, supporting a multimodal approach for large deletions. (loyaux2024metexon14 pages 1-5)

### 10.4 Liquid biopsy
Liquid biopsy was used in pivotal tepotinib studies and demonstrated meaningful response rates in liquid-biopsy identified patients (see Treatment section). (mahrous2023…thediagnosis pages 6-7)

---

## 11. Outcome / Prognosis

### 11.1 Prognostic factors (real-world)
In a METex14-positive lung adenocarcinoma cohort, independent poor prognostic factors included:
- **Strong c-MET IHC staining**
- **Initial brain metastasis**
- **Supportive-care-only**
(gow2023survivaloutcomesand pages 1-2)

### 11.2 Real-world survival data
In a French real-world cohort (n=118), median overall survival was reported as **27.1 months** (with median follow-up 16 months). (babey2023realworldtreatmentoutcomes pages 1-2)

*Interpretation note:* This cohort also reported treatment heterogeneity and did not demonstrate a clear median OS advantage in those who received anti-MET TKIs in their analyses, underscoring the complexity of real-world comparisons. (babey2023realworldtreatmentoutcomes pages 1-2)

---

## 12. Treatment

### 12.1 Current standard targeted therapies (real-world implementation)
Selective MET tyrosine kinase inhibitors (TKIs) have become standard targeted options in advanced METex14 NSCLC, with capmatinib and tepotinib established by pivotal phase II programs and incorporated into routine precision oncology testing pathways. (spagnolo2023targetingmetin pages 1-2, makimoto2024diagnosisandtreatment pages 1-2)

### 12.2 Tepotinib (VISION) — efficacy and safety
**VISION long-term follow-up (advanced/metastatic METex14 NSCLC):**
- Quantitative outcomes: ORR **51.4%** (95% CI 45.8–57.1) and median DOR **18.0 months**. (mazieres2023tepotinibtreatmentin pages 1-2)
- Safety: peripheral edema was the most frequent treatment-related adverse event (**67.1%**; grade 3 edema **11.2%**). (mazieres2023tepotinibtreatmentin pages 1-2)

**Asian VISION subset (data cut-off Nov 20, 2022):**
- Abstract quote (Kato et al., 2024; https://doi.org/10.1038/s41416-024-02615-9): “**ORR was 56.6%… mDOR 18.5 months… mPFS 13.8 months… mOS 25.5 months**.” (yang2024vebreltinibforadvanced pages 1-2)
- Safety: “**TRAEs occurred in 95.3%… (39.6% Grade ≥3). Most common TRAEs: peripheral edema (62.3%), creatinine increase (38.7%).**” (yang2024vebreltinibforadvanced pages 1-2)

### 12.3 Capmatinib (GEOMETRY mono-1) — efficacy
Makimoto (2024) summarizes pivotal capmatinib outcomes:
- **Treatment-naïve cohort (n=28):** ORR **68%**, median DOR **12.6 months**, median PFS **12.4 months**. (makimoto2024diagnosisandtreatment pages 1-2)
- **Previously treated cohort (n=69):** ORR **41%**, median DOR **9.7 months**, median PFS **5.4 months**. (makimoto2024diagnosisandtreatment pages 1-2)

### 12.4 Newer selective MET inhibitors (2024)
**Vebreltinib (KUNPENG phase II; JCO 2024):**
- Efficacy: ORR **75%** (95% CI 61.1–86), median DOR **15.9 months**, median PFS **14.1 months**, median OS **20.7 months**; DCR **96.2%**. (yang2024vebreltinibforadvanced pages 1-2)
- Safety: common treatment-related adverse events included **peripheral edema (82.7%)**, **QT prolongation (30.8%)**, **elevated serum creatinine (28.8%)**. (yang2024vebreltinibforadvanced pages 1-2)

### 12.5 Immunotherapy outcomes in METex14
In a 3-year testing/outcomes series, immunotherapy-treated patients (n=13) had ORR **30%** and median PFS **4 months**, while MET inhibitor-treated patients (n=15) had ORR **44%** and median PFS **5.5 months** (institutional real-world outcomes). (loyaux2024metexon14 pages 1-5)

### 12.6 Suggested MAXO terms (examples)
- **MAXO:0000757** targeted therapy
- **NCIT:C15986** drug therapy
- **MAXO:0000468** molecular targeted therapy
- For MET TKI administration, represent as targeted small molecule therapy (ontology mapping may require MAXO term resolution outside this run).

---

## 13. Prevention

Subtype-specific primary prevention for METex14 is not established. Prevention is largely that of lung cancer broadly:
- **Primary prevention:** smoking cessation, reduction of occupational exposures (not quantified in retrieved sources).
- **Secondary prevention:** lung cancer screening (e.g., LDCT) is NSCLC-level prevention and not METex14-specific.
- **Tertiary prevention:** early identification of METex14 through comprehensive genomic profiling to enable effective targeted therapy and reduce morbidity. The need for mandatory MET testing in treatment decision-making is emphasized in diagnostic-focused work. (loyaux2024metexon14 pages 1-5)

---

## 14. Other Species / Natural Disease

No naturally occurring METex14 skipping NSCLC analogs in other species were identified in the retrieved evidence.

---

## 15. Model Organisms / Experimental Models

Evidence retrieved in this run includes **in vitro functional modeling** of MET variants:
- In a Latin American cohort study, the functional impact of candidate MET variants (e.g., T992I, H1094Y) was evaluated in multiple cell lines (HEK293T, BEAS-2B, H1993), and effects on proliferation/migration through MET/AKT signaling were tested, alongside inhibitor sensitivity testing in 2D/3D culture. (loyaux2024metexon14 pages 1-5)

This supports the use of:
- **In vitro cell line models** (human lung cancer lines; epithelial cell models) to study MET signaling output and drug sensitivity.
- **3D culture models** to approximate tumor-like behavior for drug testing.

No animal models (GEMMs/PDX) were described in the accessed evidence snippets.

---

# Summary Table of Key Quantitative Findings

| Finding | Numeric value(s) | Population/cohort | Source (DOI URL + publication year) | Evidence citation id |
|---|---:|---|---|---|
| Prevalence in NSCLC (published range) | ~1–4%; also reported ~3% | General NSCLC across reviews/screening reports | Loyaux et al. 2024, https://doi.org/10.21203/rs.3.rs-4520709/v1; Makimoto 2024, https://doi.org/10.21037/tlcr-24-93 | (loyaux2024metexon14 pages 1-5, makimoto2024diagnosisandtreatment pages 1-2) |
| Prevalence in NSCLC (cohort-specific) | 1.9% (44/2296 MET exon 14 variants; 32/44 were MET exon 14 skipping) | Retrospective NSCLC cohort tested 2017–2019 | Yuan et al. 2023, https://doi.org/10.3390/jmp4010006 | (yuan2023metexon14 pages 1-2) |
| Prevalence in NSCLC (cohort-specific) | ~4.0% (46/1143 MET exon 14 alterations) | 3-year screening experience, consecutive NSCLC | Loyaux et al. 2024, https://doi.org/10.21203/rs.3.rs-4520709/v1 | (loyaux2024metexon14 pages 1-5) |
| Enrichment in pulmonary/sarcomatoid carcinoma | 24.3% (9/37) in pulmonary sarcomatoid carcinoma; literature 7.7–32% in sarcomatoid carcinomas; 8–17% noted in sarcomatoid carcinoma | Single-center real-world lung cancer cohort; literature summaries | Gow et al. 2023, https://doi.org/10.3389/fonc.2023.1113696; Yuan et al. 2023, https://doi.org/10.3390/jmp4010006; Makimoto 2024, https://doi.org/10.21037/tlcr-24-93 | (gow2023survivaloutcomesand pages 1-2, yuan2023metexon14 pages 1-2, makimoto2024diagnosisandtreatment pages 1-2) |
| Demographics | Median age 73; 62.7% female; 83.9% adenocarcinoma; 92.4% stage IV; 27% had >3 metastatic sites | GFPC 03-18 real-world French cohort (n=118) | Babey et al. 2023, https://doi.org/10.1007/s11523-023-00976-4 | (babey2023realworldtreatmentoutcomes pages 1-2) |
| Demographics | Median age 72; 50.8% female; 33.9% Asian | VISION pooled Cohorts A+C (n=313) | Mazieres et al. 2023, long-term follow-up of VISION | (mazieres2023tepotinibtreatmentin pages 1-2) |
| Demographics/risk pattern | METex14-positive patients were generally elderly, never-smokers, and had poor performance scores | Single-center real-world lung cancer cohort (n=69 METex14+) | Gow et al. 2023, https://doi.org/10.3389/fonc.2023.1113696 | (gow2023survivaloutcomesand pages 1-2) |
| PD-L1 high expression | 67% with PD-L1 >50% | MET exon 14 tumors (n=46) | Loyaux et al. 2024, https://doi.org/10.21203/rs.3.rs-4520709/v1 | (loyaux2024metexon14 pages 1-5) |
| Co-mutations | 42% with co-occurring alterations; TP53 24%, PIK3CA 9% | MET exon 14 tumors (n=46) | Loyaux et al. 2024, https://doi.org/10.21203/rs.3.rs-4520709/v1 | (loyaux2024metexon14 pages 1-5) |
| Diagnostic performance (RNA vs DNA) | RNA-based diagnosis detected 27% more METex14 cases than DNA-based methods; 20% of RNA-low METex14 cases were confirmed by DNA analysis | Latin American NSCLC cohort, 1560 tumor biopsies | Rivas et al. 2024, https://doi.org/10.3390/ijms252413715 | (loyaux2024metexon14 pages 1-5) |
| Diagnostic performance (DNA-missed rescued) | 4/46 alterations missed by DNA sequencing and rescued by fragment analysis or RNA sequencing | 3-year NSCLC screening cohort | Loyaux et al. 2024, https://doi.org/10.21203/rs.3.rs-4520709/v1 | (loyaux2024metexon14 pages 1-5) |
| Tepotinib efficacy (VISION long-term) | ORR 51.4% (95% CI 45.8–57.1); median DOR 18.0 mo | Advanced/metastatic METex14 NSCLC, Cohorts A+C (n=313) | Mazieres et al. 2023, long-term follow-up of VISION | (mazieres2023tepotinibtreatmentin pages 1-2) |
| Tepotinib subgroup efficacy | Cohort C ORR 55.9%; treatment-naive ORR 57.3%, median DOR 46.4 mo; previously treated ORR 45.0%, median DOR 12.6 mo | VISION subgroup analyses | Mazieres et al. 2023, long-term follow-up of VISION | (mazieres2023tepotinibtreatmentin pages 1-2) |
| Tepotinib safety | Peripheral edema 67.1%; grade 3 edema 11.2% | VISION pooled Cohorts A+C | Mazieres et al. 2023, long-term follow-up of VISION | (mazieres2023tepotinibtreatmentin pages 1-2) |
| Tepotinib efficacy (Asian VISION subset) | ORR 56.6%; median DOR 18.5 mo; median PFS 13.8 mo; median OS 25.5 mo | Asian patients in VISION (n=106) | Kato et al. 2024, https://doi.org/10.1038/s41416-024-02615-9 | (yang2024vebreltinibforadvanced pages 1-2) |
| Tepotinib safety (Asian VISION subset) | TRAEs 95.3%; grade ≥3 TRAEs 39.6%; peripheral edema 62.3%; creatinine increase 38.7% | Asian patients in VISION (n=106) | Kato et al. 2024, https://doi.org/10.1038/s41416-024-02615-9 | (yang2024vebreltinibforadvanced pages 1-2) |
| Capmatinib efficacy (GEOMETRY mono-1, 1L) | ORR 68% (95% CI 48–84); median DOR 12.6 mo; median PFS 12.4 mo | Treatment-naive METex14 NSCLC (n=28) | Makimoto 2024, https://doi.org/10.21037/tlcr-24-93 | (makimoto2024diagnosisandtreatment pages 1-2) |
| Capmatinib efficacy (GEOMETRY mono-1, ≥2L) | ORR 41% (95% CI 29–53); median DOR 9.7 mo; median PFS 5.4 mo | Previously treated METex14 NSCLC (n=69) | Makimoto 2024, https://doi.org/10.21037/tlcr-24-93 | (makimoto2024diagnosisandtreatment pages 1-2) |
| Vebreltinib efficacy (KUNPENG) | ORR 75.0% (95% CI 61.1–86.0); DCR 96.2%; median DOR 15.9 mo; median PFS 14.1 mo; median OS 20.7 mo | Advanced METex14 NSCLC (n=52; 67.3% treatment-naive) | Yang et al. 2024, https://doi.org/10.1200/JCO.23.02363 | (yang2024vebreltinibforadvanced pages 1-2) |
| Vebreltinib subgroup efficacy | ORR 77.1% treatment-naive; 70.6% previously treated | KUNPENG subgroup analyses | Yang et al. 2024, https://doi.org/10.1200/JCO.23.02363 | (yang2024vebreltinibforadvanced pages 1-2) |
| Vebreltinib safety | Peripheral edema 82.7%; QT prolongation 30.8%; elevated serum creatinine 28.8% | KUNPENG phase II | Yang et al. 2024, https://doi.org/10.1200/JCO.23.02363 | (yang2024vebreltinibforadvanced pages 1-2) |


*Table: This table compiles the main quantitative disease-characteristic, diagnostic, and treatment findings for MET exon 14 skipping NSCLC from the gathered evidence. It is useful for rapid knowledge-base population and side-by-side comparison of prevalence, testing yield, and MET inhibitor outcomes.*

---

## Expert synthesis / current understanding (2023–2024 emphasis)
Across 2023–2024 sources, METex14 NSCLC is best understood as (i) a low-prevalence but clinically important NSCLC driver (~1–4%), (ii) strongly defined by a mechanistic loss of MET juxtamembrane negative regulation leading to sustained signaling, and (iii) a subtype where **diagnostic modality matters**—RNA-based approaches and multimodal workflows can recover clinically actionable cases missed by DNA-only assays. (spagnolo2023targetingmetin pages 2-3, loyaux2024metexon14 pages 1-5)

Therapeutically, the field has transitioned from proof-of-concept MET inhibition to routine use of selective MET TKIs (tepotinib/capmatinib) and emergence of additional selective inhibitors (e.g., vebreltinib), with consistently observed class toxicities including peripheral edema and creatinine elevations, and durable responses in substantial fractions of patients. (mazieres2023tepotinibtreatmentin pages 1-2, makimoto2024diagnosisandtreatment pages 1-2, yang2024vebreltinibforadvanced pages 1-2)


References

1. (gow2023survivaloutcomesand pages 1-2): Chien-Hung Gow, Min-Shu Hsieh, Yi-Lin Chen, Yi-Nan Liu, Shang-Gin Wu, and Jin-Yuan Shih. Survival outcomes and prognostic factors of lung cancer patients with the met exon 14 skipping mutation: a single-center real-world study. Frontiers in Oncology, Mar 2023. URL: https://doi.org/10.3389/fonc.2023.1113696, doi:10.3389/fonc.2023.1113696. This article has 11 citations.

2. (loyaux2024metexon14 pages 1-5): Romain Loyaux, Rym Ben Dhiab, Simon Garinet, Mathilda Bastide, Sophie Léonard-Goyet, Elizabeth Fabre, Audrey Mansuet-Lupo, Laure Gibault, Stéphane Jouveshomme, Etienne Giroux-Leprieur, Karen Leroy, Marie Wislez, and Hélène Blons. Met exon 14 skipping mutations in non–small-cell lung cancer: testing considerations and clinical outcomes a 3 years screening experience. Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4520709/v1, doi:10.21203/rs.3.rs-4520709/v1.

3. (yuan2023metexon14 pages 1-2): Lisi Yuan, Harshita Mehrotra, Xin He, and David Bosler. Met exon 14 variants in non-small cell lung carcinoma: prevalence, clinicopathologic and molecular features. Journal of Molecular Pathology, 4:46-56, Feb 2023. URL: https://doi.org/10.3390/jmp4010006, doi:10.3390/jmp4010006. This article has 2 citations.

4. (babey2023realworldtreatmentoutcomes pages 1-2): Hélène Babey, Philippe Jamme, Hubert Curcio, Jean Baptiste Assié, Remi Veillon, Hélène Doubre, Maurice Pérol, Florian Guisier, Eric Huchot, Chantal Decroisette, Lionel Falchero, Romain Corre, Alexis Cortot, Christos Chouaïd, and Renaud Descourt. Real-world treatment outcomes of met exon14 skipping in non-small cell lung cancer: gfpc 03-18 study. Targeted Oncology, 18:585-591, Jun 2023. URL: https://doi.org/10.1007/s11523-023-00976-4, doi:10.1007/s11523-023-00976-4. This article has 7 citations and is from a peer-reviewed journal.

5. (yang2024vebreltinibforadvanced pages 1-2): Jin-Ji Yang, Yan Zhang, Lin Wu, Jie Hu, Zhe-Hai Wang, Jing-Hua Chen, Yun Fan, Gen Lin, Qi-Ming Wang, Yu Yao, Jun Zhao, Yuan Chen, Jian Fang, Yong Song, Wei Zhang, Ying Cheng, Ren-Hua Guo, Xing-Ya Li, He-Peng Shi, Weizhe Xue, Dianqi Han, Peilong Zhang, and Yi‐Long Wu. Vebreltinib for advanced non–small cell lung cancer harboring c-met exon 14 skipping mutation: a multicenter, single-arm, phase ii kunpeng study. Journal of Clinical Oncology, 42:3680-3691, Nov 2024. URL: https://doi.org/10.1200/jco.23.02363, doi:10.1200/jco.23.02363. This article has 32 citations and is from a highest quality peer-reviewed journal.

6. (mazieres2023tepotinibtreatmentin pages 1-2): J Mazieres, PK Paik, MC Garassino, and X Le. Tepotinib treatment in patients with met exon 14–skipping non–small cell lung cancer: long-term follow-up of the vision phase 2 nonrandomized clinical trial. Unknown journal, 2023.

7. (spagnolo2023targetingmetin pages 2-3): Calogera Claudia Spagnolo, Giuliana Ciappina, Elisa Giovannetti, Andrea Squeri, Barbara Granata, Chiara Lazzari, Giulia Pretelli, Giulia Pasello, and Mariacarmela Santarpia. Targeting met in non-small cell lung cancer (nsclc): a new old story? International Journal of Molecular Sciences, 24:10119, Jun 2023. URL: https://doi.org/10.3390/ijms241210119, doi:10.3390/ijms241210119. This article has 42 citations.

8. (makimoto2024diagnosisandtreatment pages 1-2): Go Makimoto. Diagnosis and treatment of non-small cell lung cancer (nsclc) harboring met ex14 skipping: have we met the desired drug? Translational Lung Cancer Research, 13:1438-1443, Jun 2024. URL: https://doi.org/10.21037/tlcr-24-93, doi:10.21037/tlcr-24-93. This article has 2 citations and is from a peer-reviewed journal.

9. (mahrous2023…thediagnosis pages 6-7): M Mahrous, AO Jebriel, A Allehebi, A Shafik, and F El Karak. … the diagnosis, biomarker testing, and clinical management of advanced or metastatic non-small cell lung cancer with mesenchymal-epithelial transition exon 14 …. Unknown journal, 2023.

10. (spagnolo2023targetingmetin pages 1-2): Calogera Claudia Spagnolo, Giuliana Ciappina, Elisa Giovannetti, Andrea Squeri, Barbara Granata, Chiara Lazzari, Giulia Pretelli, Giulia Pasello, and Mariacarmela Santarpia. Targeting met in non-small cell lung cancer (nsclc): a new old story? International Journal of Molecular Sciences, 24:10119, Jun 2023. URL: https://doi.org/10.3390/ijms241210119, doi:10.3390/ijms241210119. This article has 42 citations.
