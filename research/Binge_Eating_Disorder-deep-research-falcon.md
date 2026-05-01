---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-28T09:45:49.812376'
end_time: '2026-04-28T10:17:41.554889'
duration_seconds: 1911.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Binge Eating Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 5000
citation_count: 81
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Binge Eating Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Binge Eating Disorder** covering all of the
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
- **Disease Name:** Binge Eating Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Binge Eating Disorder** covering all of the
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


## Comprehensive Research Report: Binge Eating Disorder (BED)

### Target disease
- **Disease name:** Binge Eating Disorder (BED)
- **Category:** Psychiatric (feeding and eating disorder)
- **MONDO ID:** Not retrieved from the gathered sources (limitation of this run) (melisse2025redefiningdiagnosticparameters pages 1-2, hay2023currentapproachesin pages 1-2)

### Summary artifacts (structured for knowledge-base ingestion)
The following artifacts summarize identifiers/criteria, epidemiology, treatments, and phenotype→ontology mappings:

| Framework/Database | Identifier / code | Key diagnostic / definition highlights | Citation / source |
|---|---|---|---|
| DSM-5-TR |  | BED is defined by recurrent binge-eating episodes with loss of control, marked distress, and no regular compensatory behaviors; episodes occur at least weekly for 3 months and include at least 3 associated features (eg, rapid eating, eating when not hungry, eating alone from embarrassment). (melisse2025redefiningdiagnosticparameters pages 1-2, hay2023currentapproachesin pages 1-2) | Melisse & Dingemans, *Journal of Eating Disorders*, Jan 2025, https://doi.org/10.1186/s40337-025-01187-0; Hay et al., *Medical Journal of Australia*, Jun 2023, https://doi.org/10.5694/mja2.52008 |
| ICD-11 |  | BED was added as a named eating-disorder diagnosis in ICD-11/ICD revision process; compared with DSM-5, ICD-11 criteria are broader and more flexible, including allowance for subjective binge episodes and shorter duration in some circumstances. (palavras2018aninvestigationof pages 1-3, hay2023currentapproachesin pages 1-2) | Palavras et al., *Nutrients*, Nov 2018, https://doi.org/10.3390/nu10111751; Hay et al., *Medical Journal of Australia*, Jun 2023, https://doi.org/10.5694/mja2.52008 |
| ICD-10 |  | BED was not a distinct major diagnosis in ICD-10 in the way it is in ICD-11; older ICD-based literature discusses its addition in ICD-11 as a meaningful classification change. Specific ICD-10 BED code was not retrieved from current evidence. (palavras2018aninvestigationof pages 1-3, hay2023currentapproachesin pages 1-2) | Palavras et al., *Nutrients*, Nov 2018, https://doi.org/10.3390/nu10111751; Hay et al., *Medical Journal of Australia*, Jun 2023, https://doi.org/10.5694/mja2.52008 |
| MeSH |  | MeSH identifier was not retrieved from the current gathered sources. BED terminology in current evidence uses the synonym/abbreviation “binge-eating disorder (BED)”. (melisse2025redefiningdiagnosticparameters pages 1-2, melisse2023efficacyofwebbased pages 1-2) | Melisse & Dingemans, *Journal of Eating Disorders*, Jan 2025, https://doi.org/10.1186/s40337-025-01187-0; Melisse et al., *Journal of Medical Internet Research*, May 2023, https://doi.org/10.2196/40472 |
| MONDO |  | MONDO identifier was not retrieved from the current gathered sources. Current evidence supports BED as an aggregated disease-level psychiatric diagnosis rather than an individual-patient identifier. (melisse2025redefiningdiagnosticparameters pages 1-2, hay2023currentapproachesin pages 1-2) | Melisse & Dingemans, *Journal of Eating Disorders*, Jan 2025, https://doi.org/10.1186/s40337-025-01187-0; Hay et al., *Medical Journal of Australia*, Jun 2023, https://doi.org/10.5694/mja2.52008 |
| Synonyms / naming note | BED | Common naming in current sources is “binge-eating disorder” and abbreviation “BED”; BED is described as the most common named eating disorder in recent reviews. (melisse2025redefiningdiagnosticparameters pages 1-2, melisse2023efficacyofwebbased pages 1-2, kowalewska2024comorbidityofbinge pages 1-2) | Melisse & Dingemans, *Journal of Eating Disorders*, Jan 2025, https://doi.org/10.1186/s40337-025-01187-0; Melisse et al., *Journal of Medical Internet Research*, May 2023, https://doi.org/10.2196/40472; Kowalewska et al., *BMC Psychiatry*, Aug 2024, https://doi.org/10.1186/s12888-024-05943-5 |


*Table: This table summarizes the main diagnostic frameworks and identifier status for binge eating disorder based only on gathered evidence. It is useful for anchoring a knowledge-base entry to current diagnostic systems while clearly noting which ontology IDs were not retrieved.*

| Study (author, year) | Population/setting | Design | Key quantitative findings (prevalence/incidence, odds ratios, remission/relapse) | Notable comorbidities/impairments/treatment uptake | URL/DOI |
|---|---|---|---|---|---|
| Nagata et al., 2023 (nagata2023thesocialepidemiology pages 1-2) | U.S. ABCD Study; 10,197 early adolescents aged 10-14 years | Cross-sectional analysis | BED prevalence 1.0%; binge-eating behaviors 6.3%. Greater odds of BED with gay/bisexual identity vs heterosexual (AOR 2.25, 95% CI 1.01-5.01) and household income <\$75,000 (AOR 2.05, 95% CI 1.21-3.46). Greater odds of binge-eating behaviors in males (AOR 1.28), Native American youth (AOR 1.60), low income (AOR 1.34), and sexual minority responses (~AOR 1.81-1.95). | BED linked to later diabetes, metabolic syndrome, cardiovascular disease, suicidality; adolescent binge eating predicts depressive symptoms. Only 11.9% of adolescents with BED seek clinical care. | https://doi.org/10.1186/s40337-023-00904-x |
| Javaras et al., 2024 (javaras2024thenaturalcourse pages 1-2) | Community-based adults with DSM-IV BED; baseline n=156, follow-up n=137; mean age 47.2 years, mean BMI 36.1 | Prospective natural-history study with 2.5- and 5-year follow-up | At 2.5 years: 61.3% full BED, 23.4% subthreshold, 15.3% no BED. At 5 years: 45.7% full BED, 32.6% subthreshold, 21.7% no BED. Median time to remission >60 months; median time to relapse after remission 30 months. No participants developed AN or BN during follow-up. | Demonstrates protracted course with frequent relapse; baseline sample predominantly female (78.1%). | https://doi.org/10.1017/S0033291724000977 |
| Kowalewska et al., 2024 (kowalewska2024comorbidityofbinge pages 1-2, kowalewska2024comorbidityofbinge pages 2-4) | Systematic review of 63 studies on BED and psychiatric comorbidity | Systematic review | Reported U.S. lifetime incidence 2.8%; global lifetime prevalence ~1.9%. Higher lifetime incidence in women (3.5%) than men (2.0%). | Most frequent psychiatric comorbidities: mood, anxiety, and substance use disorders; also ADHD, personality disorders, stress/adjustment disorders, psychotic disorders, sleep disorders, suicidality. Review highlights barriers to treatment uptake including shame, lack of awareness, and clinician knowledge gaps. | https://doi.org/10.1186/s12888-024-05943-5 |
| Melisse et al., 2023 (melisse2023efficacyofwebbased pages 1-2) | Adults with BED in treatment context; summary epidemiologic framing within RCT report | Randomized controlled trial report background | Reports BED lifetime prevalence about 2% overall and up to 30% among people with excess weight. | Describes BED as the most common eating disorder and emphasizes substantial unmet treatment need due to long waiting periods. | https://doi.org/10.2196/40472 |
| Appolinario et al., 2022 (kowalewska2024comorbidityofbinge pages 38-39) | Representative metropolitan Rio de Janeiro sample; 2,297 adults aged 18-60 years | Cross-sectional population survey | BED prevalence 1.4%; recurrent binge eating 6.2%; BN 0.7%. | BED associated with depression, anxiety, ADHD, elevated BMI, marked impairment in work/school, social and family life, reduced mental and physical HRQoL; under half had sought treatment. | https://doi.org/10.1007/s00127-022-02223-z |
| Caldiroli et al., 2024 (caldiroli2024clinicalfactorsassociated pages 16-17) | ED outpatient sample; subgroup with objective binge-eating episodes (OBEs) | Cross-sectional clinical study | 29% of subjects with OBEs exhibited a chronic ED course. BN/BED comprised 37.3% of ED diagnoses in the sample. | OBE group had longer illness duration, more hospitalizations, more pharmacotherapy exposure; comorbid anxiety disorders, borderline personality disorder, and polysubstance misuse were more common. | https://doi.org/10.3390/jpm14060609 |


*Table: This table summarizes recent and closely relevant evidence on binge eating disorder epidemiology, demographic correlates, psychiatric burden, and longitudinal course. It is useful for quickly locating quantitative prevalence, odds ratios, and remission/relapse findings alongside real-world impairment and treatment uptake data.*

| Intervention (psychotherapy/pharmacotherapy/digital) | Evidence type & key study (author year) | Key quantitative outcomes (binge frequency/remission/weight/QoL) | Safety/limitations | Real-world implementation notes | Suggested MAXO term(s) (free text) | DOI/URL |
|---|---|---|---|---|---|---|
| Guided self-help CBT-E (digital psychotherapy) | Randomized controlled trial; Melisse et al. 2023 (melisse2023efficacyofwebbased pages 1-2, melisse2023efficacyofwebbased pages 10-13) | Objective binges fell from mean 19 (SD 16) to 3 (SD 5) by end of treatment; full recovery 40% (36/90); between-group effect size for objective binges d=1.0; treatment completion 78.9%; clinical impairment improved faster in treatment arm (melisse2023efficacyofwebbased pages 1-2, melisse2023efficacyofwebbased pages 10-13) | Dropout ~21.1%; outcomes after both groups received treatment converged at follow-up; QoL not specifically quantified in gathered text (melisse2023efficacyofwebbased pages 1-2) | Addresses long waiting lists and expands access to specialized BED care via web delivery (melisse2023efficacyofwebbased pages 1-2) | cognitive behavioral psychotherapy; guided self-help; telehealth/digital psychotherapy | https://doi.org/10.2196/40472 |
| CBT vs pharmacotherapy for binge-spectrum disorders | Systematic review/meta-analysis; Samara et al. 2024 (samara2024iscognitivebehavioral pages 4-5, samara2024iscognitivebehavioral pages 1-2) | CBT superior to antidepressants for remission (pooled RR 2.24, 95% CI 1.03-4.87); superior for binge-frequency reduction (pooled SMD -0.35, 95% CI -0.69 to -0.01); some individual comparisons showed no significant differences vs methylphenidate/sibutramine (samara2024iscognitivebehavioral pages 4-5, samara2024iscognitivebehavioral pages 1-2) | Small, underpowered trials; heterogeneity; psychotherapy blinding limitations; no clear superiority for QoL, anxiety, depression, weight, or dropouts overall (samara2024iscognitivebehavioral pages 4-5, samara2024iscognitivebehavioral pages 1-2) | Supports guideline positioning of CBT as first-line when available, but access barriers may favor medication use in some settings (samara2024iscognitivebehavioral pages 1-2) | cognitive behavioral psychotherapy; evidence-based psychotherapy selection | https://doi.org/10.1177/00048674231219593 |
| Digital eating-disorder interventions (mostly CBT-informed) | Systematic review/meta-analysis; Thomas et al. 2024 (thomas2024behaviorchangetechniques pages 17-20, thomas2024behaviorchangetechniques pages 20-22, thomas2024behaviorchangetechniques pages 11-14) | Pooled EDE-Q improvement vs WL/TAU MD -0.57 (95% CI -0.80 to -0.39); follow-up EDE-Q MD -0.33; 16/17 studies showed efficacy post-intervention; some studies reported ongoing reductions in bingeing/purging (thomas2024behaviorchangetechniques pages 17-20, thomas2024behaviorchangetechniques pages 20-22) | High heterogeneity (I2 77% for main analysis); attrition ranged 6.7%-58%; limited BED-specific remission or binge-episode data in gathered text (thomas2024behaviorchangetechniques pages 17-20, thomas2024behaviorchangetechniques pages 11-14) | Mostly web-based; therapist involvement ranged none to minimal; useful for scalable, lower-intensity implementation (thomas2024behaviorchangetechniques pages 11-14) | digital behavioral intervention; internet-based psychotherapy; self-management support | https://doi.org/10.2196/57577 |
| Lisdexamfetamine (LDX) | Rapid review and patient-perception synthesis; Rodan et al. 2023, Armanious et al. 2024 (rodan2023pharmacotherapyalternativeand pages 7-8, armanious2024patientperceptionsof pages 1-3) | Recent evidence supports LDX use in BED; phase II/III trials collectively showed reduced weekly binge-eating episodes; efficacy strongest at 50-70 mg/day; patient-reported weight loss associated with higher perceived efficacy (rodan2023pharmacotherapyalternativeand pages 7-8, armanious2024patientperceptionsof pages 1-3) | About 85% reported at least one treatment-emergent adverse event; common AEs include dry mouth, insomnia/sleep disturbance, jitteriness; abuse liability noted at high non-approved doses (armanious2024patientperceptionsof pages 1-3) | Only FDA-approved medication for BED in gathered evidence; real-world perceptions suggest weight change influences acceptability and perceived benefit (armanious2024patientperceptionsof pages 1-3) | stimulant medication administration; pharmacotherapy for binge eating | https://doi.org/10.1186/s40337-023-00833-9; https://doi.org/10.1016/j.psycom.2024.100195 |
| CBT alone | Randomized controlled trial; Grilo et al. 2025 (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 1-3) | Significant binge-frequency reductions; remission 44.7% (21/47); minimal weight loss effect (0.5% mean reduction; 4.3% achieved ≥5% weight loss) (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 8-10) | Less weight loss than LDX-containing arms; not clearly superior to LDX alone on primary binge endpoint in this trial (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 8-10) | Appropriate when psychotherapy access exists and weight loss is not the main treatment target; may be combined with medication for greater effect (grilo2025cognitivebehavioraltherapy pages 6-8) | cognitive behavioral psychotherapy | https://doi.org/10.1176/appi.ajp.20230982 |
| Lisdexamfetamine alone | Randomized controlled trial; Grilo et al. 2025 (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 8-10, grilo2025cognitivebehavioraltherapy pages 1-3) | Remission 40.4% (19/47); binge-eating reduction ~79.7%; mean weight loss 5.5%; 53.2% achieved ≥5% weight loss; fastest early monthly reduction at month 1 (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 8-10) | Medically withdrawn participants 21.3%; detailed AE profile not provided in gathered excerpt, but LDX-associated AEs elsewhere include xerostomia/headache/insomnia and common TEAEs (grilo2025cognitivebehavioraltherapy pages 8-10, armanious2024patientperceptionsof pages 1-3) | Useful when medication access is easier than psychotherapy and weight loss is clinically relevant; FDA-approved option (grilo2025cognitivebehavioraltherapy pages 1-3, armanious2024patientperceptionsof pages 1-3) | stimulant medication administration; pharmacotherapy for binge eating | https://doi.org/10.1176/appi.ajp.20230982 |
| Combined CBT + lisdexamfetamine | Randomized controlled trial; Grilo et al. 2025 (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 8-10, grilo2025cognitivebehavioraltherapy pages 1-3) | Highest remission 70.2% (33/47); largest binge-eating reduction (~96.1%); mean weight loss 4.8%; 42.6% achieved ≥5% weight loss; superior overall symptom reduction vs single modalities (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 8-10) | Medical withdrawal 21.3%; trial lacked placebo/control medication and had limited diversity; AE details not fully reported in gathered text (grilo2025cognitivebehavioraltherapy pages 8-10) | Strongest quantitative efficacy in gathered sources; suggests complementary mechanisms of psychotherapy plus stimulant treatment (grilo2025cognitivebehavioraltherapy pages 8-10) | combination psychotherapy and pharmacotherapy; cognitive behavioral psychotherapy; stimulant medication administration | https://doi.org/10.1176/appi.ajp.20230982 |
| Anti-obesity drugs under investigation (e.g., phentermine/topiramate, naltrexone/bupropion, liraglutide, semaglutide) | Narrative/systematic review of trials; Riboldi & Carrà 2024 (rodan2023pharmacotherapyalternativeand pages 7-8) | Across 14 clinical trials, most anti-obesity drugs except orlistat may improve both body weight and binge severity/frequency; quantitative pooled estimates not provided in gathered excerpt (rodan2023pharmacotherapyalternativeand pages 7-8) | Evidence limited by small samples and methodological variability; misuse risk may potentiate dietary restriction/pathological weight loss (rodan2023pharmacotherapyalternativeand pages 7-8) | Emerging off-label/experimental option, especially where obesity comorbidity is prominent; ongoing trials likely to clarify role (rodan2023pharmacotherapyalternativeand pages 7-8) | anti-obesity pharmacotherapy; appetite-modulating medication administration | https://doi.org/10.5152/alphapsychiatry.2024.241464 |


*Table: This table summarizes evidence-based psychotherapy, digital, and pharmacologic interventions for binge eating disorder using only the gathered sources. It highlights quantitative outcomes, safety considerations, implementation issues, and suggested MAXO-style intervention labels for knowledge-base use.*

| Clinical feature/phenotype | Brief description | Typical onset/course notes | Example quantitative frequency/data if available from gathered evidence | Suggested HPO term(s) (free text) | Key citation(s) |
|---|---|---|---|---|---|
| Recurrent binge-eating episodes | Core BED feature: recurrent episodes of eating accompanied by subjective loss of control | Chronic or recurrent; DSM-5-TR requires episodes at least weekly for 3 months | DSM-5-TR threshold: at least 1 episode/week for at least 3 months (melisse2025redefiningdiagnosticparameters pages 1-2, kowalewska2024comorbidityofbinge pages 2-4) | Binge eating; Abnormal eating behavior; Loss of control over eating | (melisse2025redefiningdiagnosticparameters pages 1-2, kowalewska2024comorbidityofbinge pages 2-4) |
| Loss of control during eating | Sense of inability to stop or control what/how much is eaten during episodes | Present during binge episodes; central phenomenologic feature across definitions | Included as an essential feature in DSM-5-TR and ICD-11-oriented summaries (melisse2025redefiningdiagnosticparameters pages 1-2, palavras2018aninvestigationof pages 1-3, melisse2023efficacyofwebbased pages 1-2) | Impaired impulse control; Loss of control over eating | (melisse2025redefiningdiagnosticparameters pages 1-2, palavras2018aninvestigationof pages 1-3, melisse2023efficacyofwebbased pages 1-2) |
| Rapid eating | Eating much more rapidly than normal during episodes | Episodic, occurring during binges; one of the associated DSM-5-TR descriptors | One of the 5 associated DSM-5-TR binge descriptors; ≥3 descriptors required (melisse2025redefiningdiagnosticparameters pages 1-2) | Rapid eating | (melisse2025redefiningdiagnosticparameters pages 1-2) |
| Eating until uncomfortably full | Continued eating beyond comfortable satiety during episodes | Episodic with binge events | One of the 5 associated DSM-5-TR binge descriptors (melisse2025redefiningdiagnosticparameters pages 1-2) | Early satiety abnormality / Postprandial discomfort; Abnormal satiety behavior | (melisse2025redefiningdiagnosticparameters pages 1-2) |
| Eating when not physically hungry | Intake continues despite absence of physiologic hunger cues | Episodic with binge events; suggests disrupted satiety/interoception | One of the 5 associated DSM-5-TR binge descriptors (melisse2025redefiningdiagnosticparameters pages 1-2) | Hyperphagia; Abnormal hunger/satiety behavior | (melisse2025redefiningdiagnosticparameters pages 1-2) |
| Eating alone because of embarrassment | Socially avoidant eating driven by shame/embarrassment | Episodic; may contribute to concealment and delayed care seeking | One of the 5 associated DSM-5-TR binge descriptors (melisse2025redefiningdiagnosticparameters pages 1-2) | Social withdrawal during eating; Embarrassment; Avoidant behavior | (melisse2025redefiningdiagnosticparameters pages 1-2) |
| Negative affect after overeating | Feelings such as guilt, disgust, or low mood after binges | Episodic but can reinforce chronic cycle; linked to impairment and severity | Melisse 2023 describes shame, guilt, and disgust as characteristic feelings in BED (melisse2023efficacyofwebbased pages 1-2) | Guilt; Shame; Dysphoric mood | (melisse2023efficacyofwebbased pages 1-2) |
| Marked distress about binge eating | Clinically significant distress is required for diagnosis | Persistent distress often accompanies chronic course and poorer functioning | Marked distress identified as an essential feature in diagnostic summaries (palavras2018aninvestigationof pages 1-3, hay2023currentapproachesin pages 1-2) | Emotional distress; Psychological distress | (palavras2018aninvestigationof pages 1-3, hay2023currentapproachesin pages 1-2) |
| Absence of regular compensatory behaviors | Distinguishes BED from bulimia nervosa; no recurrent purging/compensation after binges | Stable diagnostic discriminator across DSM-5/DSM-5-TR descriptions | Explicitly noted in Melisse 2023 and Hay 2023 (melisse2023efficacyofwebbased pages 1-2, hay2023currentapproachesin pages 1-2) | Binge eating without compensatory behavior | (melisse2023efficacyofwebbased pages 1-2, hay2023currentapproachesin pages 1-2) |
| Functional impairment / reduced quality of life | BED is associated with impairment in daily functioning and health-related quality of life | Often chronic; persists with ongoing BED and comorbidity | In a population survey, BED was associated with marked work/school, social, and family impairment and reduced mental/physical HRQoL; under half sought treatment (kowalewska2024comorbidityofbinge pages 38-39) | Reduced quality of life; Impaired social functioning; Occupational impairment | (kowalewska2024comorbidityofbinge pages 38-39) |
| Clinical impairment improves with treatment | BED-related impairment is measurable and treatment responsive | Improves with psychotherapy; can recur if illness persists/relapses | Guided self-help CBT-E showed faster reduction in clinical impairment assessment scores vs delayed treatment (melisse2023efficacyofwebbased pages 10-13) | Reduced quality of life; Functional impairment | (melisse2023efficacyofwebbased pages 10-13) |
| Mood, anxiety, and substance-use comorbidity | Most frequent psychiatric comorbidities in BED; associated with greater severity | Often persistent across illness course and important for prognosis | Systematic review identified mood disorders, anxiety disorders, and substance use disorders as the most frequent BED comorbidities (kowalewska2024comorbidityofbinge pages 1-2, kowalewska2024comorbidityofbinge pages 2-4) | Anxiety; Depressive episode; Substance abuse | (kowalewska2024comorbidityofbinge pages 1-2, kowalewska2024comorbidityofbinge pages 2-4) |
| Additional psychiatric comorbidity burden | BED also co-occurs with ADHD, personality disorders, sleep disorders, suicidality, stress-related and psychotic disorders | Contributes to broader morbidity and complexity | Broad psychiatric comorbidity profile summarized in 2024 systematic review (kowalewska2024comorbidityofbinge pages 1-2, kowalewska2024comorbidityofbinge pages 11-12) | Attention deficit hyperactivity disorder; Sleep disturbance; Suicidal ideation/behavior; Personality dysfunction | (kowalewska2024comorbidityofbinge pages 1-2, kowalewska2024comorbidityofbinge pages 11-12) |
| Adult chronicity / slow remission | Natural course in adults is often prolonged rather than brief | Chronic, relapsing course common; remission may take years | Median time to remission exceeded 60 months in a prospective community cohort (javaras2024thenaturalcourse pages 1-2) | Chronic course; Relapsing course | (javaras2024thenaturalcourse pages 1-2) |
| Partial persistence over time | Many adults remain full or subthreshold cases over multi-year follow-up | Fluctuating between full, subthreshold, and remitted states | At 2.5 years: 61.3% full BED, 23.4% subthreshold, 15.3% no BED; at 5 years: 45.7% full, 32.6% subthreshold, 21.7% no BED (javaras2024thenaturalcourse pages 1-2) | Relapsing-remitting course; Fluctuating severity | (javaras2024thenaturalcourse pages 1-2) |
| Relapse after remission | Remission is often not durable | Relapsing course common after initial remission | Median time to relapse after remission was 30 months (javaras2024thenaturalcourse pages 1-2) | Relapsing course | (javaras2024thenaturalcourse pages 1-2) |
| Female predominance but affects all sexes | BED is more common in females, though substantial male burden exists | Lifetime risk spans adolescence to adulthood; prevalence peaks later than some other EDs | Review reported lifetime incidence 3.5% in women vs 2.0% in men; in a natural-history cohort 78.1% were female (kowalewska2024comorbidityofbinge pages 1-2, javaras2024thenaturalcourse pages 1-2) | Abnormal eating behavior in female; Abnormal eating behavior in male | (kowalewska2024comorbidityofbinge pages 1-2, javaras2024thenaturalcourse pages 1-2) |


*Table: This table summarizes the core clinical manifestations, impairment profile, and longitudinal course of binge eating disorder using only gathered evidence. It is useful for mapping BED features into structured phenotype fields and ontology-oriented knowledge base entries.*

### Visual evidence (diagnostic criteria / treatment pathway)
Hay et al. (2023) includes a visual summary of DSM-5-TR eating-disorder criteria (including BED) and a treatment-pathway indicator box, retrievable as cropped images. These can be used to populate UI-facing knowledge-base views of diagnostic criteria and treatment pathways (hay2023currentapproachesin media 97e600c1, hay2023currentapproachesin media 07cb9dc5).

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
Binge eating disorder (BED) is defined by **recurrent binge-eating episodes** characterized by a **sense of loss of control**, accompanied by **marked distress**, and **not followed by compensatory behaviors** (distinguishing it from bulimia nervosa). In DSM-5-TR, binge episodes must occur **at least once per week for at least 3 months** and include **≥3 associated features** (e.g., rapid eating, eating until uncomfortably full, eating when not physically hungry, eating alone due to embarrassment, and negative feelings after overeating). (melisse2025redefiningdiagnosticparameters pages 1-2, melisse2023efficacyofwebbased pages 1-2, hay2023currentapproachesin pages 1-2)

### 1.2 Key identifiers and classification systems
A structured summary of DSM-5-TR vs ICD-11 positioning and identifier availability in the retrieved corpus is provided in Artifact-00. ICD-11 inclusion is supported by clinical-utility work comparing DSM-5 and proposed ICD-11 BED schemes; ICD-11 criteria are described as broader and may include subjective binge episodes and more flexible duration thresholds in certain circumstances. (palavras2018aninvestigationof pages 1-3, hay2023currentapproachesin pages 1-2)

**Limitations:** This run did not retrieve BED’s **MeSH** or **MONDO** identifiers, nor a specific ICD-11 code string for BED from the included texts (melisse2025redefiningdiagnosticparameters pages 1-2, hay2023currentapproachesin pages 1-2).

### 1.3 Synonyms / alternative names
The common naming in the retrieved sources is “**binge-eating disorder**” with the abbreviation “**BED**.” (melisse2025redefiningdiagnosticparameters pages 1-2, melisse2023efficacyofwebbased pages 1-2)

### 1.4 Evidence provenance (patient-level vs aggregated)
Most evidence in this report is from **aggregated disease-level resources**: clinical reviews, systematic reviews/meta-analyses, and cohort/RCT data, rather than EHR-only descriptions. Examples include: a national adolescent cohort analysis (ABCD), a community adult natural-history cohort, and randomized trials of psychotherapy delivery. (nagata2023thesocialepidemiology pages 1-2, javaras2024thenaturalcourse pages 1-2, melisse2023efficacyofwebbased pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (multifactorial)
BED is understood as multifactorial, with interacting **neurobehavioral mechanisms** (reward/inhibitory-control imbalance), psychosocial drivers (stress/negative affect), and **polygenic genetic liability**, often co-occurring with obesity and cardiometabolic risk but not reducible to obesity alone. (pasquale2024rewardandinhibitory pages 2-4, chen2024neuroimagingstudiesof pages 12-15, burstein2023genomewideanalysisof pages 8-10)

### 2.2 Risk factors
#### 2.2.1 Genetic risk factors
**GWAS/PRS (human):**
- A 2023 Nature Genetics study performed GWAS on a model-derived BED phenotype and validated at least one locus (e.g., **rs17789218 near MCHR2**), with additional replication signals; it also found **nominal enrichment in neural lineages** (limbic neurons, inhibitory/non-excitatory neurons, enteric neurons/glia, astrocytes), supporting a neurobiological substrate. (burstein2023genomewideanalysisof pages 8-10)
- Polygenic liability to schizophrenia in a binge-eating genetics cohort (BEGIN) was associated with **earlier age at first ED symptom** (−0.35 year), **higher ED symptom scores** (0.16), and greater risk of **major depressive disorder** (HR 1.18) and **substance use disorder** (HR 1.36), indicating cross-disorder shared liability relevant to clinical course and comorbidity. (zhang2023theimpactof pages 1-2)

**Candidate-gene synthesis (human):** A 2024 systematic review of genetic polymorphisms/microbiome work summarized repeated candidate associations involving dopaminergic and appetite/reward genes (e.g., **DRD2, COMT, MC4R, BDNF, FTO, OPRM1, SLC6A3, GHRL, CARTPT, MCHR2**), but emphasized heterogeneity and limitations typical of candidate-gene designs. (hernandez2024relationshipofgenetic pages 1-2, hernandez2024relationshipofgenetic pages 5-7)

#### 2.2.2 Environmental / social risk factors
In U.S. early adolescents (ABCD cohort), BED odds were higher with:
- **Gay/bisexual identity** vs heterosexual (AOR 2.25, 95% CI 1.01–5.01)
- **Household income < $75,000** (AOR 2.05, 95% CI 1.21–3.46)
Additionally, binge-eating behaviors (broader than BED diagnosis) were associated with male sex, Native American descent, lower income, and sexual minority status responses. (nagata2023thesocialepidemiology pages 1-2)

#### 2.2.3 Protective factors
No robust, specific protective factors (genetic or environmental) were retrieved in the gathered texts; this remains a gap in this run’s evidence set.

### 2.3 Gene–environment interactions
Direct, quantified GxE interaction studies specific to BED were not retrieved in the gathered texts. However, convergent mechanistic evidence supports that **stress/negative affect** interacts with reward/inhibitory systems to precipitate binge episodes, and animal work demonstrates sex-specific stress-triggered binge-like eating circuitry. (anversa2023aparaventricularthalamus pages 1-2, dufour2026advancingtranslationalresearch pages 5-8)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes and ontology suggestions
A structured phenotype table with suggested **HPO terms** and course features is provided in Artifact-03. Core diagnostic descriptors (DSM-5-TR) are explicitly enumerated in a 2025 BED diagnostic-parameter review and are consistent with clinical summaries. (melisse2025redefiningdiagnosticparameters pages 1-2, hay2023currentapproachesin pages 1-2)

### 3.2 Age of onset, severity, progression
- Early adolescence prevalence and sociodemographic risk patterns are described in ABCD data (age 10–14). (nagata2023thesocialepidemiology pages 1-2)
- In a prospective adult community sample, BED tended to improve but often over years, with substantial subthreshold persistence and relapse. (javaras2024thenaturalcourse pages 1-2)

### 3.3 Quality of life (QoL) impact
A representative population survey reported BED associated with **marked impairments in work/school, social and family life** and **reduced mental and physical HRQoL**, with under half seeking treatment. (kowalewska2024comorbidityofbinge pages 38-39)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
BED is not a monogenic disorder in the retrieved evidence; it is best characterized as **polygenic** with loci contributing small effects. (burstein2023genomewideanalysisof pages 8-10, zhang2023theimpactof pages 1-2)

### 4.2 Pathogenic variants
No ClinVar/ACMG-classified pathogenic variants specific to BED were identified in the retrieved evidence.

### 4.3 Epigenetic information
The retrieved evidence set did not include a BED-specific EWAS. A BED-relevant epigenetic candidate finding in obesity-spectrum males reported **sex-specific OXTR DNA methylation differences** (lower methylation in males with BED vs obese males without BED), suggesting possible sex-dependent epigenetic vulnerability, though peripheral methylation is not a validated diagnostic biomarker. (hernandez2024relationshipofgenetic pages 1-2)

---

## 5. Environmental information

### 5.1 Lifestyle and social context
BED is frequently associated with obesity and may be embedded in contexts of food availability, stress, and socioeconomic adversity; adolescent data specifically highlight income and sexual minority status associations. (nagata2023thesocialepidemiology pages 1-2)

### 5.2 Infectious agents
Not applicable based on retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic model (reward + inhibitory control imbalance)
A 2024 mechanistic review synthesizes evidence that BED involves **reward hypersensitivity** and **impaired inhibitory control**, including an imbalance between **anticipatory reward** and **experienced reward** signals and frontostriatal/prefrontal dysfunction. It describes implicated circuitry including reward regions (VTA, ventral striatum/NAc, OFC/PFC) and inhibitory-control nodes (prefrontal cortex, dACC, inferior frontal gyrus, pre-SMA), consistent with addiction-inspired incentive-sensitization frameworks. (pasquale2024rewardandinhibitory pages 2-4, pasquale2024rewardandinhibitory pages 8-9)

### 6.2 Neuroimaging (rs-fMRI network-level findings)
A 2024 resting-state fMRI review reports BED-associated alterations across large-scale networks (DMN/CEN/salience network) and regionally highlights **reduced dACC connectivity in the salience network** and **increased PCC/mPFC connectivity in the DMN**, aligning with impaired salience/inhibitory control and altered self-referential processing. (chen2024neuroimagingstudiesof pages 1-2)

### 6.3 Stress and negative affect mechanisms
Animal-model evidence indicates a sex-specific “emotional stress-induced binge eating” phenotype and identifies a glutamatergic **paraventricular thalamus (PVT) → medial insular cortex** projection that gates stress-induced binge eating in females; chemogenetic inhibition suppresses the behavior, supporting a causal circuit mechanism. (anversa2023aparaventricularthalamus pages 1-2)

### 6.4 Suggested biological annotation terms
**GO biological processes (examples):** reward processing; dopaminergic synaptic transmission; response to stress; regulation of feeding behavior; inhibitory control/executive function (conceptual mapping) (pasquale2024rewardandinhibitory pages 2-4, chen2024neuroimagingstudiesof pages 12-15).

**Cell Ontology (CL) (examples):** cortical pyramidal neurons; medium spiny neurons; astrocytes (supported by heritability enrichment in astrocytes and neural lineages) (burstein2023genomewideanalysisof pages 8-10).

**UBERON (examples):** brain; prefrontal cortex; anterior cingulate cortex; insular cortex; ventral striatum/nucleus accumbens (pasquale2024rewardandinhibitory pages 2-4, chen2024neuroimagingstudiesof pages 1-2, anversa2023aparaventricularthalamus pages 1-2).

---

## 7. Anatomical structures affected
Primary involvement is functional dysregulation in **brain reward and control circuits** (prefrontal cortex, ACC/dACC, insula, striatum/NAc, OFC), with downstream impacts on eating behavior and metabolic health risk. (pasquale2024rewardandinhibitory pages 2-4, chen2024neuroimagingstudiesof pages 1-2)

---

## 8. Temporal development

### 8.1 Onset
Early adolescence can show measurable BED prevalence (1.0% in a 10–14 year-old U.S. cohort). (nagata2023thesocialepidemiology pages 1-2)

### 8.2 Progression, remission, relapse
In a prospective community-based adult BED cohort:
- At 2.5 years: 61.3% full BED, 23.4% subthreshold, 15.3% no BED
- At 5 years: 45.7% full BED, 32.6% subthreshold, 21.7% no BED
- Median time to remission exceeded 60 months; median time to relapse after remission was 30 months
This supports a **protracted course** with common relapse. (javaras2024thenaturalcourse pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Recent evidence collated in Artifact-01 includes:
- Early adolescent BED prevalence 1.0% in ABCD follow-up data (nagata2023thesocialepidemiology pages 1-2)
- Systematic-review estimates for global lifetime prevalence ~1.9% and U.S. lifetime incidence 2.8%, with higher lifetime incidence in women than men (3.5% vs 2.0%) (kowalewska2024comorbidityofbinge pages 1-2)
- Population-based adult survey prevalence 1.4% in Rio de Janeiro (kowalewska2024comorbidityofbinge pages 38-39)

### 9.2 Inheritance pattern
Evidence supports **polygenic/multifactorial inheritance** rather than Mendelian inheritance. (burstein2023genomewideanalysisof pages 8-10, zhang2023theimpactof pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria
DSM-5-TR diagnostic elements (frequency/duration and associated features) are summarized in recent reviews and are visually represented in Hay et al. (2023) boxes (melisse2025redefiningdiagnosticparameters pages 1-2, hay2023currentapproachesin media 97e600c1).

### 10.2 Screening and assessment tools (real-world implementation)
- **BEDS-7**: a brief 7-item screener with a published scoring algorithm; in an overweight/obesity validation context, the systematic review reports sensitivity and NPV ≥0.83 for BMI >30, though specificity can be modest and depends on BMI range. (herman2016developmentofthe pages 1-2, house2022identifyingeatingdisorders pages 16-16, house2022identifyingeatingdisorders pages 17-17)
- **QEWP-5**: in an Italian obesity-treatment sample (n=604) compared to EDE interview, sensitivity 0.49 and specificity 0.93 (PPV 0.34; NPV 0.96; κ 0.35), supporting use as a screening tool but not a stand-alone diagnostic instrument. (calugi2020psychometricproprietiesof pages 1-3)
- **LOCES**: a 24-item measure capturing subjective loss of control; in an undergraduate sample (n=261) it showed excellent internal consistency (α≈0.95) and predicted OBE and SBE frequency (e.g., OBE: b=2.40, β=0.41; SBE: b=2.95, β=0.43). (stefano2016lossofcontrol pages 2-3, stefano2016lossofcontrol pages 1-2)
- **EDE/EDE-Q**: systematic-review evidence indicates variable sensitivity/specificity depending on population and outcome definition; one bariatric candidate study reported EDE-Q sensitivity 0.59, specificity 0.86 for BED. (house2022identifyingeatingdisorders pages 13-13)

### 10.3 Biomarkers and imaging
No clinically validated blood biomarker was retrieved. Candidate biomarkers include rs-fMRI connectivity patterns (DMN/salience network; dACC/PCC/mPFC), PFC activation patterns (fNIRS), ERP indices of anticipatory vs consummatory reward, and PET measures of dopamine/opioid signaling, but these remain research-stage with small, heterogeneous samples. (pasquale2024rewardandinhibitory pages 2-4, chen2024neuroimagingstudiesof pages 1-2)

---

## 11. Outcome / prognosis

### 11.1 Morbidity and complications
BED is linked to substantial psychiatric comorbidity (mood, anxiety, substance-use disorders most frequent; also ADHD, sleep disorders, personality disorders, suicidality) and is associated with medical sequelae such as diabetes/metabolic syndrome and cardiovascular risk (particularly in obesity contexts). (kowalewska2024comorbidityofbinge pages 1-2, nagata2023thesocialepidemiology pages 1-2)

### 11.2 Prognostic factors
In adolescents, socioeconomic and sexual-minority status markers identify higher odds of BED, suggesting target groups for prevention/screening. (nagata2023thesocialepidemiology pages 1-2)

### 11.3 Mortality
BED-specific mortality rates were not retrieved from the gathered sources; however, eating disorders overall are recognized as severe illnesses with elevated morbidity and mortality. (caldiroli2024clinicalfactorsassociated pages 16-17)

---

## 12. Treatment

A structured treatment evidence table with quantitative outcomes, implementation notes, and MAXO-style term suggestions is provided in Artifact-02.

### 12.1 First-line psychotherapy and digital delivery
A 2023 RCT of **web-based guided self-help CBT-E** showed large reductions in binge episodes and **40% full recovery** in 12 weeks, supporting scalable real-world implementation to address treatment access gaps. (melisse2023efficacyofwebbased pages 1-2)

### 12.2 Pharmacotherapy
**Lisdexamfetamine (LDX)** is described as the only FDA-approved medication for BED in the retrieved 2024 patient-perception analysis, with common treatment-emergent adverse events and ~85% reporting at least one AE in trials. (armanious2024patientperceptionsof pages 1-3)

### 12.3 Combined treatment (psychotherapy + medication)
A randomized controlled trial in adults with BED and obesity reported post-treatment remission rates of **70.2% (CBT+LDX)** vs **44.7% (CBT)** vs **40.4% (LDX)**, and greater weight loss in LDX-containing arms (e.g., LDX mean 5.5% weight loss; 53.2% achieving ≥5% weight loss). (grilo2025cognitivebehavioraltherapy pages 6-8, grilo2025cognitivebehavioraltherapy pages 8-10)

### 12.4 Emerging/adjunct approaches
Anti-obesity drugs (e.g., phentermine/topiramate, naltrexone/bupropion, liraglutide, semaglutide) have been reviewed as potential options to address both binge symptoms and weight outcomes, but evidence is limited and responsible prescribing is emphasized due to misuse risk. (rodan2023pharmacotherapyalternativeand pages 7-8)

---

## 13. Prevention
No BED-specific prevention trial outcomes were retrieved in the evidence set; however, adolescent sociodemographic risk patterns suggest targeted screening and early intervention in high-risk groups may be pragmatic. (nagata2023thesocialepidemiology pages 1-2)

---

## 14. Other species / natural disease
Not applicable as a naturally occurring veterinary diagnosis in retrieved evidence; however, binge-like intake behaviors are modeled in rodents for mechanistic and therapeutic work. (anversa2023aparaventricularthalamus pages 1-2, awad2024alteredrewardprocessing pages 1-3)

---

## 15. Model organisms

### 15.1 Common rodent models and translational relevance
- **Intermittent access palatable food/sucrose** paradigms generate binge-like intake escalation and allow testing reward-related outcomes; sucrose bingeing altered ethanol conditioned place preference without marked emotional changes, with stronger binge escalation in females over prolonged exposure. (awad2024alteredrewardprocessing pages 1-3)
- **Stress-induced binge models**: a female-specific emotional stress-induced binge model identifies the **PVT→insular cortex** pathway as a causal gate. (anversa2023aparaventricularthalamus pages 1-2)
- A translational review emphasizes that animal models capture behavioral hyperphagia/compulsivity but incompletely model human subjective distress, guilt, stigma, and body-image concerns—key limitations for BED translation. (dufour2026advancingtranslationalresearch pages 5-8)

---

## Direct abstract quotes supporting key claims (selected)
- “Objective binges reduced from an average of 19 (SD 16) to 3 (SD 5) binges, and **40% (36/90) showed full recovery** in the guided self-help CBT-E group.” (Melisse et al., May 2023) (melisse2023efficacyofwebbased pages 1-2)
- “At 2.5 (and 5) years, **61.3% (45.7%)**, **23.4% (32.6%)**, and **15.3% (21.7%)** … exhibited full, sub-threshold, and no BED … **Median time to remission exceeded 60 months**, and median time to relapse … was 30 months.” (Javaras et al., May 2024) (javaras2024thenaturalcourse pages 1-2)
- “Identifying as gay or bisexual … (AOR: 2.25 …) and having a household income of less than $75,000 (AOR: 2.05 …) were associated with greater odds of BED.” (Nagata et al., Oct 2023) (nagata2023thesocialepidemiology pages 1-2)

---

## Key limitations of this evidence synthesis
1. **Ontology identifiers** (MONDO/MeSH) and explicit **ICD-11 code** for BED were not retrieved from the available texts in this run. (melisse2025redefiningdiagnosticparameters pages 1-2, hay2023currentapproachesin pages 1-2)
2. **Mortality**: BED-specific mortality estimates were not retrieved; comorbidity and general ED severity were available but not BED-specific mortality rates. (caldiroli2024clinicalfactorsassociated pages 16-17)
3. **Protective factors and formal GxE**: Not well represented in retrieved sources.
4. **Some evidence is from 2025 trials** (e.g., CBT+LDX RCT), included because it provides high-quality quantitative effect estimates; 2023–2024 evidence was prioritized where available. (grilo2025cognitivebehavioraltherapy pages 6-8)


References

1. (melisse2025redefiningdiagnosticparameters pages 1-2): Bernou Melisse and Alexandra Dingemans. Redefining diagnostic parameters: the role of overvaluation of shape and weight in binge-eating disorder: a systematic review. Journal of Eating Disorders, Jan 2025. URL: https://doi.org/10.1186/s40337-025-01187-0, doi:10.1186/s40337-025-01187-0. This article has 20 citations and is from a peer-reviewed journal.

2. (hay2023currentapproachesin pages 1-2): Phillipa J. Hay, Rebekah M. Rankin, Lucie M. Ramjan, and J. Conti. Current approaches in the recognition and management of eating disorders. Medical Journal of Australia, 219:127-134, Jun 2023. URL: https://doi.org/10.5694/mja2.52008, doi:10.5694/mja2.52008. This article has 21 citations and is from a peer-reviewed journal.

3. (palavras2018aninvestigationof pages 1-3): M Amorim Palavras, P Hay, and A Claudino. An investigation of the clinical utility of the proposed icd-11 and dsm-5 diagnostic schemes for eating disorders characterized by recurrent binge eating in people with a high bmi. Nutrients, Nov 2018. URL: https://doi.org/10.3390/nu10111751, doi:10.3390/nu10111751. This article has 21 citations.

4. (melisse2023efficacyofwebbased pages 1-2): Bernou Melisse, Elske van den Berg, Margo de Jonge, Matthijs Blankers, Eric van Furth, Jack Dekker, and Edwin de Beurs. Efficacy of web-based, guided self-help cognitive behavioral therapy–enhanced for binge eating disorder: randomized controlled trial. Journal of Medical Internet Research, 25:e40472, May 2023. URL: https://doi.org/10.2196/40472, doi:10.2196/40472. This article has 43 citations and is from a domain leading peer-reviewed journal.

5. (kowalewska2024comorbidityofbinge pages 1-2): Ewelina Kowalewska, Magdalena Bzowska, Jannis Engel, and Michał Lew-Starowicz. Comorbidity of binge eating disorder and other psychiatric disorders: a systematic review. BMC Psychiatry, Aug 2024. URL: https://doi.org/10.1186/s12888-024-05943-5, doi:10.1186/s12888-024-05943-5. This article has 50 citations and is from a domain leading peer-reviewed journal.

6. (nagata2023thesocialepidemiology pages 1-2): Jason M. Nagata, Zacariah Smith-Russack, Angel Paul, Geomarie Ashley Saldana, Iris Y. Shao, Abubakr A. A. Al-Shoaibi, Anita V. Chaphekar, Amanda E. Downey, Jinbo He, Stuart B. Murray, Fiona C. Baker, and Kyle T. Ganson. The social epidemiology of binge-eating disorder and behaviors in early adolescents. Journal of Eating Disorders, Oct 2023. URL: https://doi.org/10.1186/s40337-023-00904-x, doi:10.1186/s40337-023-00904-x. This article has 34 citations and is from a peer-reviewed journal.

7. (javaras2024thenaturalcourse pages 1-2): Kristin N. Javaras, Victoria F. Franco, Boyu Ren, Cynthia M. Bulik, Scott J. Crow, Susan L. McElroy, Harrison G. Pope, and James I. Hudson. The natural course of binge-eating disorder: findings from a prospective, community-based study of adults. Psychological medicine, 54:1-11, May 2024. URL: https://doi.org/10.1017/s0033291724000977, doi:10.1017/s0033291724000977. This article has 7 citations and is from a highest quality peer-reviewed journal.

8. (kowalewska2024comorbidityofbinge pages 2-4): Ewelina Kowalewska, Magdalena Bzowska, Jannis Engel, and Michał Lew-Starowicz. Comorbidity of binge eating disorder and other psychiatric disorders: a systematic review. BMC Psychiatry, Aug 2024. URL: https://doi.org/10.1186/s12888-024-05943-5, doi:10.1186/s12888-024-05943-5. This article has 50 citations and is from a domain leading peer-reviewed journal.

9. (kowalewska2024comorbidityofbinge pages 38-39): Ewelina Kowalewska, Magdalena Bzowska, Jannis Engel, and Michał Lew-Starowicz. Comorbidity of binge eating disorder and other psychiatric disorders: a systematic review. BMC Psychiatry, Aug 2024. URL: https://doi.org/10.1186/s12888-024-05943-5, doi:10.1186/s12888-024-05943-5. This article has 50 citations and is from a domain leading peer-reviewed journal.

10. (caldiroli2024clinicalfactorsassociated pages 16-17): Alice Caldiroli, Letizia Maria Affaticati, Sara Coloccini, Francesca Manzo, Alberto Scalia, Enrico Capuzzi, Davide La Tegola, Fabrizia Colmegna, Antonios Dakanalis, Maria Salvina Signorelli, Massimiliano Buoli, and Massimo Clerici. Clinical factors associated with binge-eating episodes or purging behaviors in patients affected by eating disorders: a cross-sectional study. Journal of Personalized Medicine, 14:609, Jun 2024. URL: https://doi.org/10.3390/jpm14060609, doi:10.3390/jpm14060609. This article has 7 citations.

11. (melisse2023efficacyofwebbased pages 10-13): Bernou Melisse, Elske van den Berg, Margo de Jonge, Matthijs Blankers, Eric van Furth, Jack Dekker, and Edwin de Beurs. Efficacy of web-based, guided self-help cognitive behavioral therapy–enhanced for binge eating disorder: randomized controlled trial. Journal of Medical Internet Research, 25:e40472, May 2023. URL: https://doi.org/10.2196/40472, doi:10.2196/40472. This article has 43 citations and is from a domain leading peer-reviewed journal.

12. (samara2024iscognitivebehavioral pages 4-5): Myrto T Samara, Niki Michou, Andreas S Lappas, Aikaterini Argyrou, Elissavet Mathioudaki, Dimitra Rafailia Bakaloudi, Eirini Tsekitsidi, Zoi A Polyzopoulou, Nikos Christodoulou, Georgios Papazisis, and Michail Chourdakis. Is cognitive behavioral therapy more effective than pharmacotherapy for binge spectrum disorders? a systematic review and meta-analysis. Australian & New Zealand Journal of Psychiatry, 58:308-319, Jan 2024. URL: https://doi.org/10.1177/00048674231219593, doi:10.1177/00048674231219593. This article has 7 citations and is from a peer-reviewed journal.

13. (samara2024iscognitivebehavioral pages 1-2): Myrto T Samara, Niki Michou, Andreas S Lappas, Aikaterini Argyrou, Elissavet Mathioudaki, Dimitra Rafailia Bakaloudi, Eirini Tsekitsidi, Zoi A Polyzopoulou, Nikos Christodoulou, Georgios Papazisis, and Michail Chourdakis. Is cognitive behavioral therapy more effective than pharmacotherapy for binge spectrum disorders? a systematic review and meta-analysis. Australian & New Zealand Journal of Psychiatry, 58:308-319, Jan 2024. URL: https://doi.org/10.1177/00048674231219593, doi:10.1177/00048674231219593. This article has 7 citations and is from a peer-reviewed journal.

14. (thomas2024behaviorchangetechniques pages 17-20): Pamela Carien Thomas, Kristina Curtis, Henry W W Potts, Pippa Bark, Rachel Perowne, Tasmin Rookes, and Sarah Rowe. Behavior change techniques within digital interventions for the treatment of eating disorders: systematic review and meta-analysis. JMIR Mental Health, 11:e57577, Aug 2024. URL: https://doi.org/10.2196/57577, doi:10.2196/57577. This article has 16 citations and is from a peer-reviewed journal.

15. (thomas2024behaviorchangetechniques pages 20-22): Pamela Carien Thomas, Kristina Curtis, Henry W W Potts, Pippa Bark, Rachel Perowne, Tasmin Rookes, and Sarah Rowe. Behavior change techniques within digital interventions for the treatment of eating disorders: systematic review and meta-analysis. JMIR Mental Health, 11:e57577, Aug 2024. URL: https://doi.org/10.2196/57577, doi:10.2196/57577. This article has 16 citations and is from a peer-reviewed journal.

16. (thomas2024behaviorchangetechniques pages 11-14): Pamela Carien Thomas, Kristina Curtis, Henry W W Potts, Pippa Bark, Rachel Perowne, Tasmin Rookes, and Sarah Rowe. Behavior change techniques within digital interventions for the treatment of eating disorders: systematic review and meta-analysis. JMIR Mental Health, 11:e57577, Aug 2024. URL: https://doi.org/10.2196/57577, doi:10.2196/57577. This article has 16 citations and is from a peer-reviewed journal.

17. (rodan2023pharmacotherapyalternativeand pages 7-8): Sarah-Catherine Rodan, Emma Bryant, Anvi Le, Danielle Maloney, Stephen Touyz, Iain S. McGregor, Sarah Maguire, Phillip Aouad, Sarah Barakat, Robert Boakes, Leah Brennan, Emma Bryant, Susan Byrne, Belinda Caldwell, Shannon Calvert, Bronny Carroll, David Castle, Ian Caterson, Belinda Chelius, Lyn Chiem, Simon Clarke, Janet Conti, Lexi Crouch, Genevieve Dammery, Natasha Dzajkovski, Jasmine Fardouly, John Feneley, Amber-Marie Firriolo, Nasim Foroughi, Mathew Fuller-Tyszkiewicz, Anthea Fursland, Veronica Gonzalez-Arce, Bethanie Gouldthorp, Kelly Griffin, Scott Griffiths, Ashlea Hambleton, Amy Hannigan, Mel Hart, Susan Hart, Phillipa Hay, Ian Hickie, Francis Kay-Lambkin, Ross King, Michael Kohn, Eyza Koreshe, Isabel Krug, Jake Linardon, Randall Long, Amanda Long, Sloane Madden, Sarah Maguire, Danielle Maloney, Peta Marks, Sian McLean, Thy Meddick, Jane Miskovic-Wheatley, Deborah Mitchison, Richard O’Kearney, Shu Hwa Ong, Roger Paterson, Susan Paxton, Melissa Pehlivan, Genevieve Pepin, Andrea Phillipou, Judith Piccone, Rebecca Pinkus, Bronwyn Raykos, Paul Rhodes, Elizabeth Rieger, Sarah-Catherine Rodan, Janice Russell, Haley Russell, Fiona Salter, Susan Sawyer, Beth Shelton, Urvashnee Singh, Sophie Smith, Evelyn Smith, Karen Spielman, Sarah Squire, Juliette Thomson, Stephen Touyz, Ranjani Utpala, Lenny Vartanian, Sabina Vatter, Andrew Wallis, Warren Ward, Sarah Wells, Eleanor Wertheim, Simon Wilksch, and Michelle Williams. Pharmacotherapy, alternative and adjunctive therapies for eating disorders: findings from a rapid review. Journal of Eating Disorders, Jul 2023. URL: https://doi.org/10.1186/s40337-023-00833-9, doi:10.1186/s40337-023-00833-9. This article has 55 citations and is from a peer-reviewed journal.

18. (armanious2024patientperceptionsof pages 1-3): Abanoub J. Armanious, Audrey Asare, Deborah Mitchison, and Morgan H. James. Patient perceptions of lisdexamfetamine as a treatment for binge eating disorder: an exploratory qualitative and quantitative analysis. Psychiatry Research Communications, 4:100195, Dec 2024. URL: https://doi.org/10.1016/j.psycom.2024.100195, doi:10.1016/j.psycom.2024.100195. This article has 6 citations and is from a peer-reviewed journal.

19. (grilo2025cognitivebehavioraltherapy pages 6-8): Carlos M. Grilo, Valentina Ivezaj, Cenk Tek, Sydney Yurkow, Ashley A. Wiedemann, and Ralitza Gueorguieva. Cognitive behavioral therapy and lisdexamfetamine, alone and combined, for binge-eating disorder with obesity: a randomized controlled trial. American Journal of Psychiatry, 182:209-218, Feb 2025. URL: https://doi.org/10.1176/appi.ajp.20230982, doi:10.1176/appi.ajp.20230982. This article has 23 citations and is from a highest quality peer-reviewed journal.

20. (grilo2025cognitivebehavioraltherapy pages 1-3): Carlos M. Grilo, Valentina Ivezaj, Cenk Tek, Sydney Yurkow, Ashley A. Wiedemann, and Ralitza Gueorguieva. Cognitive behavioral therapy and lisdexamfetamine, alone and combined, for binge-eating disorder with obesity: a randomized controlled trial. American Journal of Psychiatry, 182:209-218, Feb 2025. URL: https://doi.org/10.1176/appi.ajp.20230982, doi:10.1176/appi.ajp.20230982. This article has 23 citations and is from a highest quality peer-reviewed journal.

21. (grilo2025cognitivebehavioraltherapy pages 8-10): Carlos M. Grilo, Valentina Ivezaj, Cenk Tek, Sydney Yurkow, Ashley A. Wiedemann, and Ralitza Gueorguieva. Cognitive behavioral therapy and lisdexamfetamine, alone and combined, for binge-eating disorder with obesity: a randomized controlled trial. American Journal of Psychiatry, 182:209-218, Feb 2025. URL: https://doi.org/10.1176/appi.ajp.20230982, doi:10.1176/appi.ajp.20230982. This article has 23 citations and is from a highest quality peer-reviewed journal.

22. (kowalewska2024comorbidityofbinge pages 11-12): Ewelina Kowalewska, Magdalena Bzowska, Jannis Engel, and Michał Lew-Starowicz. Comorbidity of binge eating disorder and other psychiatric disorders: a systematic review. BMC Psychiatry, Aug 2024. URL: https://doi.org/10.1186/s12888-024-05943-5, doi:10.1186/s12888-024-05943-5. This article has 50 citations and is from a domain leading peer-reviewed journal.

23. (hay2023currentapproachesin media 97e600c1): Phillipa J. Hay, Rebekah M. Rankin, Lucie M. Ramjan, and J. Conti. Current approaches in the recognition and management of eating disorders. Medical Journal of Australia, 219:127-134, Jun 2023. URL: https://doi.org/10.5694/mja2.52008, doi:10.5694/mja2.52008. This article has 21 citations and is from a peer-reviewed journal.

24. (hay2023currentapproachesin media 07cb9dc5): Phillipa J. Hay, Rebekah M. Rankin, Lucie M. Ramjan, and J. Conti. Current approaches in the recognition and management of eating disorders. Medical Journal of Australia, 219:127-134, Jun 2023. URL: https://doi.org/10.5694/mja2.52008, doi:10.5694/mja2.52008. This article has 21 citations and is from a peer-reviewed journal.

25. (pasquale2024rewardandinhibitory pages 2-4): Ellen K. Pasquale, Allison M. Boyar, and Kerri N. Boutelle. Reward and inhibitory control as mechanisms and treatment targets for binge eating disorder. Current Psychiatry Reports, 26:616-625, Sep 2024. URL: https://doi.org/10.1007/s11920-024-01534-z, doi:10.1007/s11920-024-01534-z. This article has 25 citations and is from a peer-reviewed journal.

26. (chen2024neuroimagingstudiesof pages 12-15): Xiong Chen, Chunqi Ai, Zhongchun Liu, and Gang Wang. Neuroimaging studies of resting-state functional magnetic resonance imaging in eating disorders. BMC Medical Imaging, Oct 2024. URL: https://doi.org/10.1186/s12880-024-01432-z, doi:10.1186/s12880-024-01432-z. This article has 30 citations and is from a peer-reviewed journal.

27. (burstein2023genomewideanalysisof pages 8-10): David Burstein, Trevor C. Griffen, Karen Therrien, Jaroslav Bendl, Sanan Venkatesh, Pengfei Dong, Amirhossein Modabbernia, Biao Zeng, Deepika Mathur, Gabriel Hoffman, Robyn Sysko, Tom Hildebrandt, Georgios Voloudakis, and Panos Roussos. Genome-wide analysis of a model-derived binge eating disorder phenotype identifies risk loci and implicates iron metabolism. Nature Genetics, 55:1462-1470, Aug 2023. URL: https://doi.org/10.1038/s41588-023-01464-1, doi:10.1038/s41588-023-01464-1. This article has 45 citations and is from a highest quality peer-reviewed journal.

28. (zhang2023theimpactof pages 1-2): Ruyue Zhang, Ralf Kuja-Halkola, Stina Borg, Virpi Leppä, Laura M. Thornton, Andreas Birgegård, Cynthia M. Bulik, and Sarah E. Bergen. The impact of genetic risk for schizophrenia on eating disorder clinical presentations. Translational Psychiatry, Nov 2023. URL: https://doi.org/10.1038/s41398-023-02672-3, doi:10.1038/s41398-023-02672-3. This article has 5 citations and is from a peer-reviewed journal.

29. (hernandez2024relationshipofgenetic pages 1-2): Montserrat Monserrat Hernández and Diana Jiménez-Rodríguez. Relationship of genetic polymorphisms and microbial composition with binge eating disorder: a systematic review. Healthcare, 12:1441, Jul 2024. URL: https://doi.org/10.3390/healthcare12141441, doi:10.3390/healthcare12141441. This article has 3 citations.

30. (hernandez2024relationshipofgenetic pages 5-7): Montserrat Monserrat Hernández and Diana Jiménez-Rodríguez. Relationship of genetic polymorphisms and microbial composition with binge eating disorder: a systematic review. Healthcare, 12:1441, Jul 2024. URL: https://doi.org/10.3390/healthcare12141441, doi:10.3390/healthcare12141441. This article has 3 citations.

31. (anversa2023aparaventricularthalamus pages 1-2): Roberta G. Anversa, Erin J. Campbell, Leigh C. Walker, Sarah S. Ch’ng, Muthmainah Muthmainah, Frederico S. Kremer, Amanda M. Guimarães, Mia J. O’Shea, Suheng He, Christopher V. Dayas, Zane B. Andrews, Andrew J. Lawrence, and Robyn M. Brown. A paraventricular thalamus to insular cortex glutamatergic projection gates “emotional” stress-induced binge eating in females. Neuropsychopharmacology, 48:1931-1940, Jul 2023. URL: https://doi.org/10.1038/s41386-023-01665-6, doi:10.1038/s41386-023-01665-6. This article has 24 citations and is from a highest quality peer-reviewed journal.

32. (dufour2026advancingtranslationalresearch pages 5-8): Rachel Dufour, Uri Shalev, and Linda Booij. Advancing translational research in binge-eating: integrating insights from clinical practice into animal models. Translational Psychiatry, Apr 2026. URL: https://doi.org/10.1038/s41398-026-04035-0, doi:10.1038/s41398-026-04035-0. This article has 0 citations and is from a peer-reviewed journal.

33. (pasquale2024rewardandinhibitory pages 8-9): Ellen K. Pasquale, Allison M. Boyar, and Kerri N. Boutelle. Reward and inhibitory control as mechanisms and treatment targets for binge eating disorder. Current Psychiatry Reports, 26:616-625, Sep 2024. URL: https://doi.org/10.1007/s11920-024-01534-z, doi:10.1007/s11920-024-01534-z. This article has 25 citations and is from a peer-reviewed journal.

34. (chen2024neuroimagingstudiesof pages 1-2): Xiong Chen, Chunqi Ai, Zhongchun Liu, and Gang Wang. Neuroimaging studies of resting-state functional magnetic resonance imaging in eating disorders. BMC Medical Imaging, Oct 2024. URL: https://doi.org/10.1186/s12880-024-01432-z, doi:10.1186/s12880-024-01432-z. This article has 30 citations and is from a peer-reviewed journal.

35. (herman2016developmentofthe pages 1-2): Barry K. Herman, Linda S. Deal, Dana B. DiBenedetti, Lauren Nelson, Sheri E. Fehnel, and T. Michelle Brown. Development of the 7-item binge-eating disorder screener (beds-7). The primary care companion for CNS disorders, Apr 2016. URL: https://doi.org/10.4088/pcc.15m01896, doi:10.4088/pcc.15m01896. This article has 132 citations.

36. (house2022identifyingeatingdisorders pages 16-16): Eve T. House, Natalie B. Lister, Anna L. Seidler, Haozhen Li, Wee Yee Ong, Caitlin M. McMaster, Susan J. Paxton, and Hiba Jebeile. Identifying eating disorders in adolescents and adults with overweight or obesity: a systematic review of screening questionnaires. The International Journal of Eating Disorders, 55:1171-1193, Jul 2022. URL: https://doi.org/10.1002/eat.23769, doi:10.1002/eat.23769. This article has 66 citations.

37. (house2022identifyingeatingdisorders pages 17-17): Eve T. House, Natalie B. Lister, Anna L. Seidler, Haozhen Li, Wee Yee Ong, Caitlin M. McMaster, Susan J. Paxton, and Hiba Jebeile. Identifying eating disorders in adolescents and adults with overweight or obesity: a systematic review of screening questionnaires. The International Journal of Eating Disorders, 55:1171-1193, Jul 2022. URL: https://doi.org/10.1002/eat.23769, doi:10.1002/eat.23769. This article has 66 citations.

38. (calugi2020psychometricproprietiesof pages 1-3): Simona Calugi, Cecilia Serena Pace, Stefania Muzi, Deborah Fasoli, Francesca Travagnin, and Riccardo Dalle Grave. Psychometric proprieties of the italian version of the questionnaire on eating and weight patterns (qewp-5) and its accuracy in screening for binge-eating disorder in patients seeking treatment for obesity. Eating and Weight Disorders - Studies on Anorexia, Bulimia and Obesity, 25:1739-1745, Nov 2020. URL: https://doi.org/10.1007/s40519-019-00818-1, doi:10.1007/s40519-019-00818-1. This article has 17 citations.

39. (stefano2016lossofcontrol pages 2-3): Emily C. Stefano, Allison F. Wagner, Jonathan M. Mond, David C. Cicero, and Janet D. Latner. Loss of control over eating scale (loces): validation in undergraduate men and women with and without eating disorder symptoms. Eating behaviors, 23:137-140, Dec 2016. URL: https://doi.org/10.1016/j.eatbeh.2016.09.005, doi:10.1016/j.eatbeh.2016.09.005. This article has 35 citations and is from a peer-reviewed journal.

40. (stefano2016lossofcontrol pages 1-2): Emily C. Stefano, Allison F. Wagner, Jonathan M. Mond, David C. Cicero, and Janet D. Latner. Loss of control over eating scale (loces): validation in undergraduate men and women with and without eating disorder symptoms. Eating behaviors, 23:137-140, Dec 2016. URL: https://doi.org/10.1016/j.eatbeh.2016.09.005, doi:10.1016/j.eatbeh.2016.09.005. This article has 35 citations and is from a peer-reviewed journal.

41. (house2022identifyingeatingdisorders pages 13-13): Eve T. House, Natalie B. Lister, Anna L. Seidler, Haozhen Li, Wee Yee Ong, Caitlin M. McMaster, Susan J. Paxton, and Hiba Jebeile. Identifying eating disorders in adolescents and adults with overweight or obesity: a systematic review of screening questionnaires. The International Journal of Eating Disorders, 55:1171-1193, Jul 2022. URL: https://doi.org/10.1002/eat.23769, doi:10.1002/eat.23769. This article has 66 citations.

42. (awad2024alteredrewardprocessing pages 1-3): Gaëlle Awad, Anne-Sophie Aubry, Mary C. Olmstead, and Katia Befort. Altered reward processing following sucrose bingeing in male and female mice. Nutritional Neuroscience, 27:1269-1282, Mar 2024. URL: https://doi.org/10.1080/1028415x.2024.2324232, doi:10.1080/1028415x.2024.2324232. This article has 3 citations and is from a peer-reviewed journal.