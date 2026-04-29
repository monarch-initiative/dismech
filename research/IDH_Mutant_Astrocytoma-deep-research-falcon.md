---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T17:14:21.238130'
end_time: '2026-04-05T17:22:17.344985'
duration_seconds: 476.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IDH-Mutant Astrocytoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IDH-Mutant Astrocytoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **IDH-Mutant Astrocytoma** covering all of the
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
- **Disease Name:** IDH-Mutant Astrocytoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **IDH-Mutant Astrocytoma** covering all of the
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


# Disease characteristics research report: IDH‑Mutant Astrocytoma

## Target disease
- **Disease name:** Astrocytoma, IDH‑mutant (adult-type diffuse glioma)
- **Category:** Primary malignant brain tumor; adult-type diffuse glioma
- **MONDO ID:** Not recovered from the provided sources in this run (requires ontology lookup outside the retrieved papers).

## Executive overview (current understanding)
Astrocytoma, IDH‑mutant is an adult-type diffusely infiltrating glioma defined by an IDH1 or IDH2 hotspot mutation and the absence of whole-arm 1p/19q codeletion (which would instead define oligodendroglioma). WHO CNS5 (2021) integrates molecular findings into both *classification* and *grading* (grades 2–4), including the key change that **CDKN2A/B homozygous deletion is sufficient for CNS WHO grade 4 assignment even in the absence of necrosis or microvascular proliferation**. (antonelli2022adulttypediffuse pages 1-2, horbinski2022clinicalimplicationsof pages 4-5)

| Topic | Key finding | Quantitative details | Source (year, URL) | Citation |
|---|---|---|---|---|
| WHO 2021 entity definition | Adult-type diffuse glioma entity is **Astrocytoma, IDH-mutant**; requires **IDH1 or IDH2 mutation** and **absence of whole-arm 1p/19q codeletion**. | WHO CNS5 recognizes grades 2, 3, and 4 within one molecularly defined entity. | Antonelli & Poliani, 2022, https://doi.org/10.32074/1591-951x-823 | (antonelli2022adulttypediffuse pages 1-2, antonelli2022adulttypediffuse pages 2-4) |
| WHO 2021 grading: grade 2 | Grade 2: diffusely infiltrating astrocytoma without brisk mitotic activity, necrosis, or microvascular proliferation. | Histology-based lower grade within IDH-mutant astrocytoma. | Galbraith et al., 2024, https://doi.org/10.1093/neuonc/noae009 | (galbraith2024prognosticvalueof pages 1-2) |
| WHO 2021 grading: grade 3 | Grade 3: increased mitotic activity/significant mitoses, but no necrosis or microvascular proliferation. | Practical pathology review notes mitotic rate ≥2–3 and Ki-67 up to ~10% associated with grade 3/worse survival. | Galbraith et al., 2024, https://doi.org/10.1093/neuonc/noae009; Antonelli & Poliani, 2022, https://doi.org/10.32074/1591-951x-823 | (galbraith2024prognosticvalueof pages 1-2, antonelli2022adulttypediffuse pages 2-4) |
| WHO 2021 grading: grade 4 | Grade 4: necrosis and/or microvascular proliferation **or** **CDKN2A/B homozygous deletion**, even if classic histologic grade-4 features are absent. | CDKN2A/B homozygous deletion is sufficient for CNS WHO grade 4 assignment. | Horbinski et al., 2022, https://doi.org/10.1038/s41582-022-00679-w; Reuss, 2023, https://doi.org/10.1007/s11060-023-04250-5 | (horbinski2022clinicalimplicationsof pages 4-5, reuss2023updatesonthe pages 1-2) |
| Core molecular feature: IDH hotspots | Canonical hotspot mutations define the entity; **IDH1 R132H** is the dominant alteration, with rarer noncanonical IDH1/IDH2 variants. | IDH1 R132H present in **>90%** of cases by review; one genomic cohort found **96.8%** IDH1 R132H, with rare R132S/R132G and IDH2 R172G (~1.1% each). | Antonelli & Poliani, 2022, https://doi.org/10.32074/1591-951x-823; Lee et al., 2023, https://doi.org/10.1038/s41598-023-32153-y | (antonelli2022adulttypediffuse pages 2-4, lee2023genomicprofilesof pages 5-7) |
| Core molecular feature: ATRX | **ATRX loss/inactivation** is typical and supports astrocytic lineage. | ATRX alterations in **82.1%** of one 95-case cohort; ATRX mutation and ATRX loss by IHC were 100% concordant in that study. | Lee et al., 2023, https://doi.org/10.1038/s41598-023-32153-y | (lee2023genomicprofilesof pages 5-7, lee2023genomicprofilesof pages 1-2) |
| Core molecular feature: TP53 | **TP53 mutation** is common and often co-occurs with ATRX alteration in IDH-mutant astrocytoma. | TP53 mutations in **86.3%** of one 95-case cohort. | Lee et al., 2023, https://doi.org/10.1038/s41598-023-32153-y | (lee2023genomicprofilesof pages 5-7, lee2023genomicprofilesof pages 1-2) |
| Core molecular feature: 1p/19q status | **Whole-arm 1p/19q codeletion must be absent**; if present with IDH mutation, diagnosis shifts to oligodendroglioma. | In one astrocytoma cohort, true 1p/19q codeletion was rare (**1.1%**) and represented diagnostic confounding rather than typical biology. | Antonelli & Poliani, 2022, https://doi.org/10.32074/1591-951x-823; Lee et al., 2023, https://doi.org/10.1038/s41598-023-32153-y | (antonelli2022adulttypediffuse pages 4-6, lee2023genomicprofilesof pages 5-7) |
| Core molecular feature: MGMT promoter methylation | MGMT promoter methylation is common in IDH-mutant astrocytoma, though frequency varies by cohort. | Review: commonly observed; genomic cohort: **73.7% (70/95)** overall. | Antonelli & Poliani, 2022, https://doi.org/10.32074/1591-951x-823; Lee et al., 2023, https://doi.org/10.1038/s41598-023-32153-y | (antonelli2022adulttypediffuse pages 2-4, lee2023genomicprofilesof pages 7-8) |
| Core molecular feature: G-CIMP | IDH mutation drives a **glioma CpG island methylator phenotype (G-CIMP)** / hypermethylated epigenetic state. | Qualitative hallmark; no single prevalence estimate reported in the extracted passages. | Antonelli & Poliani, 2022, https://doi.org/10.32074/1591-951x-823 | (antonelli2022adulttypediffuse pages 2-4) |
| Additional adverse molecular markers | **CDKN2A/B homozygous deletion** is a major negative prognostic marker; **MYCN amplification** may identify especially poor-risk tumors. | CDKN2A/B homozygous deletion reported in about **22%** overall in a review and **22.6% (14/95)** in one cohort; MYCN amplification **6.5% (4/95)** in one cohort. | Yuile et al., 2023, https://doi.org/10.3390/cimb45070335; Lee et al., 2023, https://doi.org/10.1038/s41598-023-32153-y | (yuile2023cdkn2abhomozygousdeletions pages 1-2, lee2023genomicprofilesof pages 7-8, lee2023genomicprofilesof pages 8-10) |
| Epidemiology: population-based incidence | Belgian registry reclassified adult diffuse gliomas in the molecular era; provides real-world incidence context but not a standalone incidence for all IDH-mutant astrocytoma grades combined. | Overall adult diffuse glioma ASR **8.55/100,000 person-years**; grade 4 lesions **6.72/100,000**; histologic astrocytoma grade 2 **0.60/100,000** and grade 3 **0.48/100,000**. Full molecular status available in **67.1%** of cases. | Pinson et al., 2024, https://doi.org/10.1093/neuonc/noad158 | (pinson2024epidemiologyandsurvival pages 1-2, pinson2024epidemiologyandsurvival pages 3-4, pinson2024epidemiologyandsurvival pages 2-3) |
| Epidemiology: demographics | IDH-mutant astrocytoma tends to affect younger adults than IDH-wildtype glioblastoma. | Belgian registry median age: grade 2 **37 y**, grade 3 **40 y**; review source notes median age around **~40 y** with slight male predominance. | Pinson et al., 2024, https://doi.org/10.1093/neuonc/noad158; Antonelli & Poliani, 2022, https://doi.org/10.32074/1591-951x-823 | (pinson2024epidemiologyandsurvival pages 3-4, antonelli2022adulttypediffuse pages 2-4) |
| Survival: Belgian registry lower grades | Registry-based survival is favorable relative to IDH-wildtype disease. | **3-year survival** for IDH-mutant astrocytoma: grade 2 **86.0%**, grade 3 **75.7%**. | Pinson et al., 2024, https://doi.org/10.1093/neuonc/noad158 | (pinson2024epidemiologyandsurvival pages 1-2) |
| Survival: Belgian registry grade 4 | Molecularly defined grade 4 IDH-mutant astrocytoma has better survival than IDH-wildtype glioblastoma but remains aggressive. | Median OS **25.9 months**; **3-year survival 40.1%**. Comparator IDH-wildtype glioblastoma median OS **9.3 months**. | Pinson et al., 2024, https://doi.org/10.1093/neuonc/noad158 | (pinson2024epidemiologyandsurvival pages 3-4, pinson2024epidemiologyandsurvival pages 1-2) |
| Recent development: INDIGO / vorasidenib | Phase 3 **INDIGO** established benefit of the brain-penetrant mutant IDH1/2 inhibitor **vorasidenib** in residual/recurrent grade 2 IDH-mutant glioma after surgery. | Median PFS **27.7 vs 11.1 months** for vorasidenib vs placebo; HR **0.39** (95% CI 0.27–0.56); time to next intervention HR **0.26**; grade ≥3 ALT elevation **9.6% vs 0%**. | Mellinghoff et al., 2023, https://doi.org/10.1056/NEJMoa2304194 | (mellinghoff2023vorasidenibinidh1 pages 1-3, mellinghoff2023vorasidenibinidh1 media cdd01275) |


*Table: This table condenses the most actionable disease-characteristics evidence for Astrocytoma, IDH-mutant, including WHO 2021 grading, hallmark molecular features, key registry epidemiology/survival statistics, and the pivotal INDIGO vorasidenib result. It is useful as a compact reference for knowledge-base population and citation tracking.*

## 1. Disease information
### 1.1 Definition and scope
- **WHO CNS5 (2021) adult-type diffuse glioma taxonomy:** WHO CNS5 defines three adult-type diffuse gliomas: **(i) Astrocytoma, IDH‑mutant; (ii) Oligodendroglioma, IDH‑mutant and 1p/19q‑codeleted; (iii) Glioblastoma, IDH‑wildtype**. (antonelli2022adulttypediffuse pages 1-2, horbinski2022clinicalimplicationsof pages 4-5)
- **Entity definition:** Astrocytoma, IDH‑mutant is characterized by an IDH1/2 mutation and *lack* of 1p/19q codeletion, and commonly shows TP53 and ATRX inactivation. (antonelli2022adulttypediffuse pages 2-4, antonelli2022adulttypediffuse pages 4-6)

### 1.2 Synonyms and alternative names
- Common historical/clinical usage includes “diffuse astrocytoma (IDH‑mutant)”, “anaplastic astrocytoma (IDH‑mutant)”, and what was historically termed “IDH‑mutant glioblastoma”, now reclassified in WHO CNS5 as **astrocytoma, IDH‑mutant, CNS WHO grade 4**. (horbinski2022clinicalimplicationsof pages 4-5)

### 1.3 Derived from individual patients vs aggregated resources
The evidence summarized here is derived primarily from:
- **Aggregated, authoritative standards/reviews** (e.g., Nature Reviews Neurology clinical implications of WHO CNS5). (horbinski2022clinicalimplicationsof pages 4-5)
- **Registry-based epidemiology** (Belgian Cancer Registry reclassified to WHO 2021). (pinson2024epidemiologyandsurvival pages 1-2)
- **Clinical cohorts / institutional series** and **randomized clinical trials** (e.g., INDIGO phase 3). (mellinghoff2023vorasidenibinidh1 pages 1-3)

## 2. Etiology
### 2.1 Causal factors (molecular drivers)
- **Somatic hotspot mutations in IDH1/IDH2** (most often IDH1 R132H) are early/defining driver events in this entity. (antonelli2022adulttypediffuse pages 2-4, lee2023genomicprofilesof pages 5-7)
- Mutant IDH gains neomorphic enzymatic activity producing D‑2‑hydroxyglutarate (2‑HG), with downstream epigenetic effects (DNA/histone methylation changes) linked to altered differentiation programs. (carosi2024targetingisocitratedehydrogenase pages 4-6, gue2024the2021world pages 4-5)

### 2.2 Risk factors (host/environment)
The retrieved sources focus on molecular classification and treatment; they do not provide strong, quantified environmental or lifestyle risk factors specific to IDH‑mutant astrocytoma.

### 2.3 Protective factors / gene–environment interactions
Not established in the retrieved sources.

## 3. Phenotypes (clinical, imaging, pathology)
### 3.1 Typical clinical presentation
- Clinical presentation is location-dependent (e.g., cortical involvement), and WHO CNS5 reviews emphasize that adult-type IDH‑mutant diffuse gliomas often present as grade 2–3 lesions and are typically supratentorial. (antonelli2022adulttypediffuse pages 1-2, antonelli2022adulttypediffuse pages 2-4)
- **Seizures** are a common presenting feature in lower-grade diffuse gliomas in general; however, explicit frequency estimates for IDH‑mutant astrocytoma were not extracted from the retrieved texts in this run.

### 3.2 Imaging phenotypes
- Reviews note that MRI often suggests lower grade (2–3) and that gadolinium enhancement can be associated with higher grade. (antonelli2022adulttypediffuse pages 1-2)
- For WHO CNS5 radiology-oriented summaries, the **T2–FLAIR mismatch sign** is highlighted as supportive of IDH‑mutant astrocytoma in appropriate contexts (qualitative statement; no sensitivity/specificity extracted here). (gue2024the2021world pages 5-7)

### 3.3 Pathology (histology)
- WHO CNS5 grading integrates histology with molecular findings. Histologic grade 4 features include **necrosis and/or microvascular proliferation**. (galbraith2024prognosticvalueof pages 1-2, horbinski2022clinicalimplicationsof pages 4-5)

### 3.4 Suggested HPO terms (examples; frequency not established in retrieved sources)
Because frequency-by-phenotype was not available in the retrieved sources, the following are suggested mappings commonly used for diffuse glioma symptom documentation:
- Seizure: **HP:0001250**
- Headache: **HP:0002315**
- Focal neurological deficit (broad): **HP:0001284** (or more specific terms per deficit)
- Cognitive impairment: **HP:0100543**
- Increased intracranial pressure: **HP:0002516**

## 4. Genetic / molecular information
### 4.1 Causal/defining genes
- **IDH1, IDH2** (hotspot missense mutations; IDH1 R132H dominant). (antonelli2022adulttypediffuse pages 2-4, lee2023genomicprofilesof pages 5-7)

### 4.2 Highly recurrent cooperating alterations
- **ATRX** alteration/loss and **TP53** mutation are typical for IDH‑mutant astrocytoma and support astrocytic lineage vs oligodendroglioma. (antonelli2022adulttypediffuse pages 2-4, antonelli2022adulttypediffuse pages 4-6)
- In a genomic cohort of 95 IDH‑mutant astrocytomas, **TP53 mutations were 86.3%** and **ATRX alterations 82.1%**. (lee2023genomicprofilesof pages 1-2, lee2023genomicprofilesof pages 5-7)

### 4.3 Key pathogenic variants (somatic)
- IDH1/2 hotspots: IDH1 R132H dominant; rare noncanonical IDH1/IDH2 variants occur. In one cohort: **IDH1 R132H 96.8%**, with R132S, R132G, and IDH2 R172G each ~1.1%. (lee2023genomicprofilesof pages 5-7)

### 4.4 Chromosomal alterations and grading biomarker
- **CDKN2A/B homozygous deletion** is now a WHO CNS5 molecular criterion sufficient for CNS WHO grade 4 assignment, even absent necrosis/microvascular proliferation. (horbinski2022clinicalimplicationsof pages 4-5, reuss2023updatesonthe pages 1-2)
- Frequency examples:
  - Literature review: CDKN2A/B homozygous deletion reported in ~**22%** of IDH‑mutant astrocytomas. (yuile2023cdkn2abhomozygousdeletions pages 1-2)
  - A genomic cohort: **22.6% (14/95)** had CDKN2A/2B homozygous deletion. (lee2023genomicprofilesof pages 7-8)

### 4.5 Epigenetics (DNA methylation; G‑CIMP) and methylation subtyping
- IDH mutation is associated with a CpG island hypermethylation phenotype (often referred to as **G‑CIMP**). (antonelli2022adulttypediffuse pages 2-4)
- DNA methylation profiling has an increasing clinical role in CNS5 and can support classification while also providing copy number information (e.g., for 1p/19q codeletion). (reuss2023updatesonthe pages 1-2)
- In an NYU cohort (n=98) with validation (TCGA and Heidelberg), **DNA methylation subclassification and CDKN2A/B homozygous deletion stratified overall survival**, while histologic grade alone did not significantly stratify OS/PFS in that dataset (OS p=0.0016 and p=0.0286 respectively). (galbraith2024prognosticvalueof pages 1-2)

## 5. Environmental information
No specific environmental, lifestyle, or infectious causal factors were established from the retrieved sources.

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (high-level)
1. **Somatic IDH1/IDH2 hotspot mutation** → neomorphic enzyme activity producing **D‑2‑hydroxyglutarate (2‑HG)**. (gue2024the2021world pages 4-5)
2. 2‑HG competitively inhibits α‑ketoglutarate–dependent dioxygenases (including TET and histone demethylases) → **genome-wide epigenetic remodeling / hypermethylation programs** (G‑CIMP). (gue2024the2021world pages 4-5, antonelli2022adulttypediffuse pages 2-4)
3. Epigenetic rewiring impacts differentiation programs and tumor cell states; accumulation of additional alterations (TP53, ATRX; and in aggressive cases CDKN2A/B homozygous deletion) drives malignant progression and worsened prognosis. (antonelli2022adulttypediffuse pages 2-4, horbinski2022clinicalimplicationsof pages 4-5)

### 6.2 Immune microenvironment and emerging multi-omics
The retrieved corpus included high-level discussion that IDH-mutant tumors are “epigenetically driven” and well-suited to single-cell/spatial multi-omics to resolve tumor–microenvironment interactions; however, detailed single-cell quantitative findings specific to IDH‑mutant astrocytoma were not captured in evidence snippets for 2023–2024 in this run. (laurengeleprince2024impactofd2hg pages 15-18)

### 6.3 Suggested ontology terms
**GO Biological Process (examples):**
- DNA methylation or regulation of DNA methylation (e.g., *DNA methylation*, *chromatin organization*)
- Regulation of cell cycle (relevant to CDKN2A/B loss)

**Cell Ontology (CL) (examples):**
- Astrocyte (tumor lineage resemblance)
- Oligodendrocyte progenitor cell (OPC)-like malignant states are frequently discussed in glioma literature; not quantified here
- Microglia/macrophage (tumor-associated myeloid populations; not quantified here)

## 7. Anatomical structures affected
- Primary site is the **central nervous system (brain)**; adult-type diffuse gliomas are often **supratentorial**. (antonelli2022adulttypediffuse pages 2-4, antonelli2022adulttypediffuse pages 1-2)

**UBERON suggestions (examples):**
- Brain: **UBERON:0000955**
- Cerebral cortex: **UBERON:0000956**
- Frontal lobe (if documented clinically): **UBERON:0001870** (frontal lobe is mentioned as a predilection in a WHO CNS5 radiology-oriented review). (gue2024the2021world pages 4-5)

## 8. Temporal development
- WHO CNS5 grades 2–4 represent a spectrum from lower-grade infiltrating disease (grade 2), increased mitotic activity (grade 3), to grade 4 behavior defined by necrosis/microvascular proliferation and/or CDKN2A/B homozygous deletion. (galbraith2024prognosticvalueof pages 1-2, horbinski2022clinicalimplicationsof pages 4-5)
- Registry evidence indicates that for IDH‑mutant astrocytoma, histologic grade may be less prognostic than key molecular events (e.g., CDKN2A/B deletion; methylation subclass). (pinson2024epidemiologyandsurvival pages 1-2, galbraith2024prognosticvalueof pages 1-2)

## 9. Inheritance and population
### 9.1 Epidemiology (recent registry evidence prioritized)
**Belgian Cancer Registry (2017–2019; reclassified to WHO 2021):**
- Full molecular status available in **67.1%** of adult-type diffuse glioma cases. (pinson2024epidemiologyandsurvival pages 1-2)
- For IDH‑mutant astrocytoma:
  - **3-year survival probability:** grade 2 **86.0%**, grade 3 **75.7%**. (pinson2024epidemiologyandsurvival pages 1-2)
  - Grade 4 IDH‑mutant astrocytoma: **median OS 25.9 months** and **3-year survival 40.1%**. (pinson2024epidemiologyandsurvival pages 3-4)
- The registry reported overall adult diffuse glioma age-standardized incidence **8.55 per 100,000 person-years**, and grade 4 lesions **6.72 per 100,000 person-years** (not specific to IDH‑mutant astrocytoma alone). (pinson2024epidemiologyandsurvival pages 1-2)

### 9.2 Demographics
- IDH‑mutant astrocytoma tends to present in younger adults than IDH‑wildtype glioblastoma; Belgian registry medians for IDH‑mutant astrocytoma were **37 years (grade 2)** and **40 years (grade 3)**. (pinson2024epidemiologyandsurvival pages 3-4)

### 9.3 Inheritance
The retrieved sources do not establish a Mendelian inheritance pattern for IDH‑mutant astrocytoma as a disease entity; it is primarily driven by somatic alterations in tumor tissue.

## 10. Diagnostics
### 10.1 Standard integrated diagnostic workflow (WHO CNS5)
WHO CNS5 endorses integrated reporting: “**Diagnostics should include different layers, namely histology, WHO grading and molecular findings**.” (reuss2023updatesonthe pages 1-2)

**Common first-line tests and methods (examples from WHO CNS5 diagnostic review and pathology guidance):**
- **IDH1 R132H immunohistochemistry** as routine screening; if negative in a suggestive case, proceed to **IDH1/IDH2 sequencing** for noncanonical variants. (antonelli2022adulttypediffuse pages 2-4)
- **ATRX immunohistochemistry** (loss supports astrocytoma lineage) and **p53 immunohistochemistry** (strong/diffuse expression supports TP53 mutation, acknowledging limitations). (antonelli2022adulttypediffuse pages 2-4)
- **1p/19q codeletion testing** (FISH or molecular methods) to exclude oligodendroglioma. (antonelli2022adulttypediffuse pages 4-6)
- **CDKN2A/B status determination** (commonly by FISH in some workflows; also inferable from copy-number derived from methylation arrays). (antonelli2022adulttypediffuse pages 4-6, reuss2023updatesonthe pages 1-2)
- **DNA methylation profiling**: has “substantial” influence on WHO CNS5 and can provide both classification support and copy-number information (including 1p/19q). (reuss2023updatesonthe pages 1-2)

### 10.2 Differential diagnosis (high-level)
- Oligodendroglioma (requires IDH mutation + whole-arm 1p/19q codeletion). (horbinski2022clinicalimplicationsof pages 4-5)
- IDH-wildtype glioblastoma (molecularly defined by TERT promoter mutation, EGFR amplification, +7/−10 among other features; beyond scope here but included in WHO CNS5 guidance). (horbinski2022clinicalimplicationsof pages 4-5)

## 11. Outcome / prognosis
### 11.1 Prognostic molecular features
- **CDKN2A/B homozygous deletion** is an adverse prognostic marker and a grade-4 defining criterion in WHO CNS5. (horbinski2022clinicalimplicationsof pages 4-5, yuile2023cdkn2abhomozygousdeletions pages 1-2)
- **DNA methylation subclassification** can outperform histologic grade for OS stratification in institutional cohorts, and can separate IDH‑mutant astrocytomas into epigenetic risk groups. (galbraith2024prognosticvalueof pages 1-2)

### 11.2 Survival statistics (recent)
- Belgian registry (WHO 2021 era): grade 4 IDH‑mutant astrocytoma median OS **25.9 months**; grade 2–3 have high 3-year survival (86.0% and 75.7%). (pinson2024epidemiologyandsurvival pages 3-4, pinson2024epidemiologyandsurvival pages 1-2)

## 12. Treatment
### 12.1 Current applications and real-world implementations
- **Maximal safe resection** is standard initial management. (laurengeleprince2024impactofd2hg pages 15-18)
- WHO CNS5 clinical guidance recommends treating **grade 4 IDH‑mutant astrocytoma** with **radiation therapy and temozolomide**, analogously to IDH‑wildtype glioblastoma. (horbinski2022clinicalimplicationsof pages 4-5)

### 12.2 Evidence-based adjuvant therapy (grade 2)
SEOM‑GEINO grade 2 glioma guidelines (published 2024; based on 2023 guideline process):
- Early RT improves PFS: EORTC 22845 median PFS **5.3 vs 3.4 years**, OS ~**7.4 years** in both arms. (vazsalgado2024seomgeinoclinicalguidelines pages 4-5)
- RT followed by **PCV** is recommended for high-risk grade 2 patients; RTOG 9802: RT+PCV OS **13.3 vs 7.8 years** (HR 0.59, p=0.003). (vazsalgado2024seomgeinoclinicalguidelines pages 4-5)

### 12.3 Key recent development (2023): targeted IDH inhibition (vorasidenib)
**INDIGO phase 3 trial** (NEJM; publication date Aug 2023; URL https://doi.org/10.1056/NEJMoa2304194):
- Abstract quote (efficacy): “**Progression-free survival was significantly improved in the vorasidenib group as compared with the placebo group (median progression-free survival, 27.7 months vs. 11.1 months; hazard ratio for disease progression or death, 0.39; 95% confidence interval [CI], 0.27 to 0.56; P<0.001).**” (mellinghoff2023vorasidenibinidh1 pages 1-3)
- Abstract quote (safety): “**An increased alanine aminotransferase level of grade 3 or higher occurred in 9.6% of the patients who received vorasidenib and in no patients who received placebo.**” (mellinghoff2023vorasidenibinidh1 pages 1-3)
- Figure/table evidence for key endpoints and ALT: median PFS 27.7 vs 11.1 months, HR 0.39; ALT increase grade ≥3 9.6% vs 0%. (mellinghoff2023vorasidenibinidh1 media cdd01275)

### 12.4 MAXO term suggestions (examples)
- Surgical tumor resection: **MAXO:0000445** (surgical excision; placeholder—exact MAXO mapping should be validated)
- Radiotherapy: **MAXO:0000127** (radiation therapy; placeholder)
- Temozolomide chemotherapy: **MAXO:0000647** (antineoplastic drug therapy; placeholder)
- Targeted therapy with IDH inhibitor (vorasidenib): **MAXO:0000058** (targeted therapy; placeholder)

*Note:* MAXO IDs above are suggestions and should be verified against the MAXO ontology.

## 13. Prevention
No established primary prevention strategies were identified in the retrieved sources. For most diffuse gliomas, primary prevention is limited; secondary prevention generally involves prompt evaluation of symptoms and imaging rather than population screening.

## 14. Other species / natural disease
Not addressed in the retrieved sources.

## 15. Model organisms
Not addressed in the retrieved sources collected in this run (no specific GEMMs, PDX, or organoid papers were retrieved/extracted as evidence).

## Expert opinions and authoritative analysis (selected)
- WHO CNS5 clinical implications review emphasizes that the updated molecularly integrated classification has direct therapeutic implications, including the grade 4 assignment based on CDKN2A/B deletion and the recommendation to treat grade 4 IDH‑mutant astrocytoma similarly to glioblastoma. (horbinski2022clinicalimplicationsof pages 4-5)
- WHO diagnostic updates underscore the need for integrated diagnostics and state that DNA methylation profiling substantially influences WHO CNS5 and can provide both classification and copy-number information. (reuss2023updatesonthe pages 1-2)

## Limitations of this run (evidence completeness)
- **PMIDs** were not available in the evidence snippets returned by the tools for many key sources (NEJM/Nature Reviews/Neuro-Oncology), so this report cites DOIs/URLs and publication months/years as available in the retrieved bibliographic records.
- Several requested areas (protective/environmental factors, phenotype frequencies/QoL metrics, model organisms) were not covered by the retrieved evidence in this tool run and would require additional targeted retrieval.


References

1. (antonelli2022adulttypediffuse pages 1-2): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 67 citations.

2. (horbinski2022clinicalimplicationsof pages 4-5): Craig Horbinski, Tamar Berger, Roger J. Packer, and Patrick Y. Wen. Clinical implications of the 2021 edition of the who classification of central nervous system tumours. Nature Reviews Neurology, 18:515-529, Jun 2022. URL: https://doi.org/10.1038/s41582-022-00679-w, doi:10.1038/s41582-022-00679-w. This article has 334 citations and is from a highest quality peer-reviewed journal.

3. (antonelli2022adulttypediffuse pages 2-4): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 67 citations.

4. (galbraith2024prognosticvalueof pages 1-2): Kristyn Galbraith, Mekka Garcia, Siyu Wei, Anna Chen, Chanel Schroff, Jonathan Serrano, Donato Pacione, Dimitris G Placantonakis, Christopher M William, Arline Faustin, David Zagzag, Marissa Barbaro, Maria Del Pilar Guillermo Prieto Eibl, Mitsuaki Shirahata, David Reuss, Quynh T Tran, Zahangir Alom, Andreas von Deimling, Brent A Orr, Erik P Sulman, John G Golfinos, Daniel A Orringer, Rajan Jain, Evan Lieberman, Yang Feng, and Matija Snuderl. Prognostic value of dna methylation subclassification, aneuploidy, and cdkn2a/b homozygous deletion in predicting clinical outcome of idh mutant astrocytomas. Neuro-oncology, 26:1042-1051, Jan 2024. URL: https://doi.org/10.1093/neuonc/noae009, doi:10.1093/neuonc/noae009. This article has 15 citations and is from a domain leading peer-reviewed journal.

5. (reuss2023updatesonthe pages 1-2): David.E. Reuss. Updates on the who diagnosis of idh-mutant glioma. Journal of Neuro-Oncology, 162:461-469, Jan 2023. URL: https://doi.org/10.1007/s11060-023-04250-5, doi:10.1007/s11060-023-04250-5. This article has 73 citations and is from a peer-reviewed journal.

6. (lee2023genomicprofilesof pages 5-7): Kwanghoon Lee, Seong-Ik Kim, Eric Eunshik Kim, Yu-Mi Shim, Jae-Kyung Won, Chul-Kee Park, Seung Hong Choi, Hongseok Yun, Hyunju Lee, and Sung-Hye Park. Genomic profiles of idh-mutant gliomas: mycn-amplified idh-mutant astrocytoma had the worst prognosis. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-32153-y, doi:10.1038/s41598-023-32153-y. This article has 23 citations and is from a peer-reviewed journal.

7. (lee2023genomicprofilesof pages 1-2): Kwanghoon Lee, Seong-Ik Kim, Eric Eunshik Kim, Yu-Mi Shim, Jae-Kyung Won, Chul-Kee Park, Seung Hong Choi, Hongseok Yun, Hyunju Lee, and Sung-Hye Park. Genomic profiles of idh-mutant gliomas: mycn-amplified idh-mutant astrocytoma had the worst prognosis. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-32153-y, doi:10.1038/s41598-023-32153-y. This article has 23 citations and is from a peer-reviewed journal.

8. (antonelli2022adulttypediffuse pages 4-6): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 67 citations.

9. (lee2023genomicprofilesof pages 7-8): Kwanghoon Lee, Seong-Ik Kim, Eric Eunshik Kim, Yu-Mi Shim, Jae-Kyung Won, Chul-Kee Park, Seung Hong Choi, Hongseok Yun, Hyunju Lee, and Sung-Hye Park. Genomic profiles of idh-mutant gliomas: mycn-amplified idh-mutant astrocytoma had the worst prognosis. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-32153-y, doi:10.1038/s41598-023-32153-y. This article has 23 citations and is from a peer-reviewed journal.

10. (yuile2023cdkn2abhomozygousdeletions pages 1-2): Alexander Yuile, Laveniya Satgunaseelan, Joe Q. Wei, Michael Rodriguez, Michael Back, Nick Pavlakis, Amanda Hudson, Marina Kastelan, Helen R. Wheeler, and Adrian Lee. Cdkn2a/b homozygous deletions in astrocytomas: a literature review. Current Issues in Molecular Biology, 45:5276-5292, Jun 2023. URL: https://doi.org/10.3390/cimb45070335, doi:10.3390/cimb45070335. This article has 34 citations.

11. (lee2023genomicprofilesof pages 8-10): Kwanghoon Lee, Seong-Ik Kim, Eric Eunshik Kim, Yu-Mi Shim, Jae-Kyung Won, Chul-Kee Park, Seung Hong Choi, Hongseok Yun, Hyunju Lee, and Sung-Hye Park. Genomic profiles of idh-mutant gliomas: mycn-amplified idh-mutant astrocytoma had the worst prognosis. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-32153-y, doi:10.1038/s41598-023-32153-y. This article has 23 citations and is from a peer-reviewed journal.

12. (pinson2024epidemiologyandsurvival pages 1-2): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 25 citations and is from a domain leading peer-reviewed journal.

13. (pinson2024epidemiologyandsurvival pages 3-4): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 25 citations and is from a domain leading peer-reviewed journal.

14. (pinson2024epidemiologyandsurvival pages 2-3): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 25 citations and is from a domain leading peer-reviewed journal.

15. (mellinghoff2023vorasidenibinidh1 pages 1-3): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 772 citations and is from a highest quality peer-reviewed journal.

16. (mellinghoff2023vorasidenibinidh1 media cdd01275): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 772 citations and is from a highest quality peer-reviewed journal.

17. (carosi2024targetingisocitratedehydrogenase pages 4-6): Francesca Carosi, Elisabetta Broseghini, Laura Fabbri, Giacomo Corradi, Riccardo Gili, Valentina Forte, Roberta Roncarati, Daria Maria Filippini, and Manuela Ferracin. Targeting isocitrate dehydrogenase (idh) in solid tumors: current evidence and future perspectives. Cancers, 16:2752, Aug 2024. URL: https://doi.org/10.3390/cancers16152752, doi:10.3390/cancers16152752. This article has 27 citations.

18. (gue2024the2021world pages 4-5): Racine Gue and Dhairya A. Lakhani. The 2021 world health organization central nervous system tumor classification: the spectrum of diffuse gliomas. Biomedicines, 12:1349, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061349, doi:10.3390/biomedicines12061349. This article has 13 citations.

19. (gue2024the2021world pages 5-7): Racine Gue and Dhairya A. Lakhani. The 2021 world health organization central nervous system tumor classification: the spectrum of diffuse gliomas. Biomedicines, 12:1349, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061349, doi:10.3390/biomedicines12061349. This article has 13 citations.

20. (laurengeleprince2024impactofd2hg pages 15-18): A Laurenge-Leprince. Impact of d-2hg on the tumor microenvironment of idh-mutated gliomas. Unknown journal, 2024.

21. (vazsalgado2024seomgeinoclinicalguidelines pages 4-5): María Ángeles Vaz-Salgado, Belén Cigarral García, Isaura Fernández Pérez, Beatriz Jiménez Munárriz, Paula Sampedro Domarco, Ainhoa Hernández González, María Vieito Villar, Raquel Luque Caro, María Luisa Villamayor Delgado, and Juan Manuel Sepúlveda Sánchez. Seom-geino clinical guidelines for grade 2 gliomas (2023). Clinical and Translational Oncology, 26:2856-2865, Apr 2024. URL: https://doi.org/10.1007/s12094-024-03456-x, doi:10.1007/s12094-024-03456-x. This article has 4 citations and is from a peer-reviewed journal.
