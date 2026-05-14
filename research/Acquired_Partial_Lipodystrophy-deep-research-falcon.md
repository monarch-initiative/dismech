---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T13:57:57.868954'
end_time: '2026-05-11T14:17:14.879336'
duration_seconds: 1157.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acquired Partial Lipodystrophy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acquired Partial Lipodystrophy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acquired Partial Lipodystrophy** covering all of the
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
- **Disease Name:** Acquired Partial Lipodystrophy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acquired Partial Lipodystrophy** covering all of the
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


# Comprehensive Disease Characteristics Report: Acquired Partial Lipodystrophy (APL)

## Executive summary
Acquired partial lipodystrophy (APL), classically termed **Barraquer–Simons syndrome (BSS)**, is an ultra-rare acquired disorder characterized by **progressive, usually symmetric cephalocaudal loss of subcutaneous adipose tissue** (face → neck/shoulders/arms/trunk) with relative sparing of lower extremities (and sometimes relative lower-body fat hypertrophy) and a strong female predominance. (corvillo2020immunologicalfeaturesof pages 1-2, hussain2016lipodystrophysyndromes. pages 1-3, donadille2024diagnosticandreferral pages 4-6)
A central current concept is that **alternative complement pathway dysregulation**—often with **low serum C3** and **C3 nephritic factor (C3NeF)**—is mechanistically linked to adipocyte injury and to major complications such as **membranoproliferative glomerulonephritis/C3 glomerulopathy**. (corvillo2020immunologicalfeaturesof pages 1-2, corvillo2021complementfactord pages 1-2, corvillo2020evidenceofongoing pages 3-6)

## 1. Disease information
### 1.1 Overview / definition
BSS is an acquired form of partial lipodystrophy characterized by “**bilateral symmetrical loss of adipose tissue that begins in the face and may variably spreads to neck, shoulders, arms and trunk, keeping intact the adipose tissue of the lower extremities**.” (corvillo2020immunologicalfeaturesof pages 1-2)

### 1.2 Key identifiers (from retrieved sources)
* **OMIM:** **608709** (reported in review literature). (pliszka2025severeinsulinresistance pages 17-18)
* **Orphanet:** BSS noted as **ORPHA:79087** in complement-focused cohort work; French registry cohort lists APL/BSS as **ORPHA 98,307**. (corvillo2021complementfactord pages 1-2, donadille2024diagnosticandreferral pages 4-6, corvillo2020immunologicalfeaturesof pages 1-2)
* **MONDO:** not identified in the retrieved full-text evidence in this run (cannot be asserted).
* **ICD-10/ICD-11 / MeSH:** not extracted from the retrieved evidence in this run (cannot be asserted).

### 1.3 Synonyms / alternative names
* **Barraquer–Simons syndrome (BSS)**
* **Acquired partial lipodystrophy (APL)**
* **Progressive cephalothoracic / cephalocaudal lipodystrophy** (terminology used in reviews). (pliszka2025severeinsulinresistance pages 18-20, fossfreitas2025lipodystrophysyndromesone pages 10-11)

### 1.4 Evidence source types
The information in this report is derived from: (i) peer-reviewed cohort studies and case reports in humans, (ii) clinical registry/rare-disease referral pathway data, (iii) clinical trials registries for partial lipodystrophy/metreleptin, and (iv) mechanistic reviews integrating human and experimental data. (corvillo2020immunologicalfeaturesof pages 1-2, donadille2024diagnosticandreferral pages 4-6, corvillo2020evidenceofongoing pages 3-6, NCT06484868 chunk 1)

| Disease / preferred name | Definition / fat-loss pattern | Common synonyms | Key identifiers | Key laboratory hallmarks | Key comorbidities / associated findings | Key citation |
|---|---|---|---|---|---|---|
| Acquired Partial Lipodystrophy | Rare acquired partial lipodystrophy with gradual, usually symmetrical cephalocaudal loss of subcutaneous fat beginning in the face and extending to neck, shoulders, arms, trunk/upper body, with relative sparing of lower extremities and often relative lower-body fat accumulation (corvillo2020immunologicalfeaturesof pages 1-2, ceccarini2021autoimmunityinlipodystrophy pages 3-4, fossfreitas2025lipodystrophysyndromesone pages 10-11, hussain2016lipodystrophysyndromes. pages 1-3) | Barraquer–Simons syndrome; BSS; APL; progressive cephalothoracic lipodystrophy; cephalocaudal lipodystrophy (pliszka2025severeinsulinresistance pages 18-20, fossfreitas2025lipodystrophysyndromesone pages 10-11) | OMIM 608709 (reported in reviews) (pliszka2025severeinsulinresistance pages 18-20, fossfreitas2025lipodystrophysyndromesone pages 10-11) | Low serum C3 common; C3 nephritic factor (C3NeF) frequent; reductions in C4 and factor B also reported; other complement autoantibodies include anti-C3, anti-properdin, anti-factor B (corvillo2020immunologicalfeaturesof pages 1-2, ceccarini2021autoimmunityinlipodystrophy pages 3-4) | C3 glomerulopathy / membranoproliferative glomerulonephritis; autoimmune diseases; metabolic abnormalities can occur; retinal drusen reported in recent cohort work (corvillo2020immunologicalfeaturesof pages 1-2, pliszka2025severeinsulinresistance pages 18-20) | Corvillo F et al. *Orphanet J Rare Dis* 2020. DOI: 10.1186/s13023-019-1292-1 (corvillo2020immunologicalfeaturesof pages 1-2) |
| Complement-associated APL phenotype | Complement dysregulation–linked APL phenotype in which adipose tissue is a site of local alternative-pathway activation; adipocytes supply factor D/adipsin and may be selectively injured by complement activation products (corvillo2020evidenceofongoing pages 1-3, corvillo2021complementfactord pages 1-2) | Barraquer–Simons syndrome with complement dysregulation (corvillo2020evidenceofongoing pages 1-3, corvillo2021complementfactord pages 1-2) | No separate disease identifier established in gathered evidence | Persistent C3 hypocomplementemia; C3NeF-mediated stabilization of C3 convertase; elevated factor D/adipsin in plasma and atrophic adipose tissue; adipose deposition of IgG, C3, C5a, C5b-9/MAC in active lesions (corvillo2020evidenceofongoing pages 1-3, corvillo2020evidenceofongoing pages 3-6, corvillo2021complementfactord pages 1-2) | Progressive lipoatrophy; macrophage-rich inflammatory remodeling of adipose tissue; risk of later C3 glomerulopathy (corvillo2020evidenceofongoing pages 1-3, corvillo2021complementfactord pages 2-4) | Corvillo F et al. *J Dermatol* 2020. DOI: 10.1111/1346-8138.15570; Corvillo F et al. *Int J Mol Sci* 2021. DOI: 10.3390/ijms22126608 (corvillo2020evidenceofongoing pages 1-3, corvillo2021complementfactord pages 1-2) |
| Clinical recognition summary | Predominantly affects females, often begins in childhood/adolescence, and is frequently underrecognized with long referral/diagnostic delays in rare-disease pathways (corvillo2020immunologicalfeaturesof pages 1-2, donadille2024diagnosticandreferral pages 4-6, donadille2024diagnosticandreferral pages 2-4) | APL; BSS (donadille2024diagnosticandreferral pages 4-6, donadille2024diagnosticandreferral pages 2-4) | French rare-disease cohort recognized 33 APL/BSS cases among 292 analyzed lipodystrophy/insulin-resistance patients; no separate Orphanet code captured in gathered evidence (donadille2024diagnosticandreferral pages 4-6, donadille2024diagnosticandreferral pages 2-4) | Complement testing recommended in practice context because low C3 and/or C3NeF support diagnosis (donadille2024diagnosticandreferral pages 4-6, donadille2024diagnosticandreferral pages 2-4) | Renal disease association (MPGN/C3G), autoimmune overlap, and ocular drusen are clinically important complications to screen for (corvillo2020immunologicalfeaturesof pages 1-2, pliszka2025severeinsulinresistance pages 18-20) | Donadille B et al. *Orphanet J Rare Dis* 2024. DOI: 10.1186/s13023-024-03173-2 (donadille2024diagnosticandreferral pages 4-6, donadille2024diagnosticandreferral pages 2-4) |


*Table: This table summarizes the core nomenclature and identifying features of acquired partial lipodystrophy/Barraquer–Simons syndrome, including its characteristic fat-loss pattern, synonyms, OMIM identifier, hallmark complement abnormalities, and major associated complications. It is useful as a compact reference for disease recognition and knowledge-base curation.*

## 2. Etiology
### 2.1 Primary causal factors (current understanding)
APL/BSS is generally considered **acquired** and frequently linked to **immune/complement dysregulation**, especially **overactivation of the alternative complement pathway** and autoantibodies that stabilize complement convertases. (corvillo2020immunologicalfeaturesof pages 1-2, corvillo2021complementfactord pages 1-2, corvillo2018acquiredpartiallipodystrophy pages 2-4)

Direct abstract support (immunology cohort):
* “**C3 hypocomplementemia and the presence of C3 nephritic factor (C3NeF), an autoantibody causing complement system over-activation, are common features**…” (corvillo2020immunologicalfeaturesof pages 1-2)

### 2.2 Risk factors
**Demographic risk**
* **Sex:** females are more affected (reported ~4:1; cohort ratio 5.5:1 in one study; 90% female in a 2018–2023 French referral cohort’s APL group). (corvillo2020immunologicalfeaturesof pages 1-2, donadille2024diagnosticandreferral pages 4-6)
* **Age of onset:** often **childhood/adolescence** (mean onset ~8 years in one cohort). (corvillo2020immunologicalfeaturesof pages 1-2)

**Immune/complement risk and associated biology**
* **C3NeF prevalence:** 69.2% (9/13) in Corvillo et al. cohort; additional complement autoantibodies were frequent (anti-C3 38.5%; anti-properdin and anti-factor B 30.8% each). (corvillo2020immunologicalfeaturesof pages 1-2)
* **Complement factor D/adipsin** (primarily synthesized by adipose tissue) is implicated because it activates the alternative pathway and may amplify local complement injury within adipose tissue. (corvillo2021complementfactord pages 1-2, corvillo2020evidenceofongoing pages 3-6)

**Potential triggers**
* Viral infections are noted as preceding onset in some patients (reported in cohort background). (corvillo2020immunologicalfeaturesof pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not directly established in the retrieved evidence; however, a plausible interaction is that environmental triggers (e.g., infections) may initiate or amplify autoimmune complement dysregulation in genetically susceptible backgrounds (e.g., HLA association signals). (corvillo2020immunologicalfeaturesof pages 1-2)

## 3. Phenotypes
### 3.1 Core phenotype: fat distribution
* **Cephalocaudal lipoatrophy** of face/neck/upper trunk/upper limbs with sparing of lower body is the defining clinical pattern. (corvillo2020immunologicalfeaturesof pages 1-2, hussain2016lipodystrophysyndromes. pages 1-3)

### 3.2 Metabolic phenotypes
Metabolic disease is **variable** and often **less frequent/severe** than in generalized lipodystrophy, but can still be clinically significant. (corvillo2020immunologicalfeaturesof pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2)
* In a 13-patient immunologic cohort: diabetes in 1 patient; elevated triglycerides/cholesterol in 2; fatty liver in 3. (corvillo2020immunologicalfeaturesof pages 1-2)
* Case-based epidemiologic estimates summarized in Oliveira et al. (2016): diabetes ~10%, hypertriglyceridemia ~30%. (oliveira2016barraquer–simonssyndromea pages 1-2)

### 3.3 Renal phenotypes
Renal disease is a major determinant of prognosis.
* APL is described as associated with **membranoproliferative glomerulonephritis** in ~20% in one review/clinical classification source. (hussain2016lipodystrophysyndromes. pages 1-3)
* Other summaries note **one third** with MPGN and that low C3/C3NeF may indicate renal involvement. (oliveira2016barraquer–simonssyndromea pages 1-2)
* Complement cohort paper notes literature risk that **~20% of BSS patients eventually develop C3 glomerulopathy (C3G)**. (corvillo2020immunologicalfeaturesof pages 1-2)

### 3.4 Ocular phenotypes
**Drusen** may develop in complement-mediated renal disease contexts, and C3 glomerulopathy review notes that DDD patients may develop drusen and that DDD can be preceded/followed by APL. (ponticelli2023c3glomerulopathiesdense pages 1-2)

### 3.5 Autoimmune phenotypes
Autoimmune disease associations are common in some cohorts.
* Corvillo et al.: autoimmune diseases in 38.5% (5/13). (corvillo2020immunologicalfeaturesof pages 1-2)

### 3.6 Quality of life impact
Facial/upper-body lipoatrophy can cause major psychosocial burden, and reconstructive procedures are implemented clinically to restore appearance. (jeon2020lipotransferprovideseffective pages 1-2)

### 3.7 Suggested HPO terms
A phenotype table with suggested HPO terms is provided below.

| Domain | Phenotype/complication | Frequency/statistic (with numerator/denominator if available) | Typical onset/progression notes | Suggested HPO terms |
|---|---|---|---|---|
| Body fat distribution | Symmetric cephalocaudal loss of subcutaneous fat affecting face, neck, shoulders, arms, trunk/upper thorax with sparing of lower extremities | Core defining phenotype; no pooled percentage given because it is used diagnostically (corvillo2020immunologicalfeaturesof pages 1-2, hussain2016lipodystrophysyndromes. pages 1-3, donadille2024diagnosticandreferral pages 4-6) | Usually begins in childhood or adolescence; gradual progressive spread from face downward over months to years; lower-body fat may become relatively increased after puberty, especially in females (corvillo2020immunologicalfeaturesof pages 1-2, hussain2016lipodystrophysyndromes. pages 1-3, oliveira2016barraquer–simonssyndromea pages 1-2) | HP:0001596 Lipodystrophy; HP:0001018 Facial hemiatrophy/facial lipoatrophy-like term not exact; HP:0010623 Abnormality of the neck; HP:0009125 Abnormal subcutaneous adipose tissue |
| Body fat distribution | Relative hypertrophy/increased fat in lower extremities or gluteofemoral region | Qualitative, reported in many women after puberty; no exact denominator in gathered cohort texts (corvillo2020immunologicalfeaturesof pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2) | Develops after upper-body fat loss; contributes to regional disproportion (corvillo2020immunologicalfeaturesof pages 1-2) | HP:0009125 Abnormal subcutaneous adipose tissue; HP:0012743 Abnormality of adipose tissue distribution |
| Body fat distribution | Female predominance | 90% women in French APL cohort (33 cases) (donadille2024diagnosticandreferral pages 4-6); literature female:male ratio about 4:1 (corvillo2020immunologicalfeaturesof pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2) | Sex bias apparent across cohorts; often recognized late despite childhood onset (donadille2024diagnosticandreferral pages 4-6, corvillo2020immunologicalfeaturesof pages 1-2) | HP:0011458 Abnormal sex ratio (disease-level descriptor; no exact patient HPO) |
| Metabolic | Diabetes mellitus / glucose intolerance | Diabetes about 10% in review/case-based overview (oliveira2016barraquer–simonssyndromea pages 1-2); one of 13 patients with diabetes in Corvillo cohort (1/13) (corvillo2020immunologicalfeaturesof pages 1-2) | Metabolic complications less common than in generalized or familial partial lipodystrophies, but can emerge with more extensive fat loss or longer disease duration (corvillo2020immunologicalfeaturesof pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2) | HP:0005978 Diabetes mellitus; HP:0003074 Hyperglycemia |
| Metabolic | Hypertriglyceridemia / dyslipidemia | Hypertriglyceridemia about 30% in review/case-based overview (oliveira2016barraquer–simonssyndromea pages 1-2); elevated TG in 2/13 in Corvillo cohort (corvillo2020immunologicalfeaturesof pages 1-2) | Often mild or absent early; should be monitored longitudinally because severity is variable (corvillo2020immunologicalfeaturesof pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2) | HP:0002155 Hypertriglyceridemia; HP:0003124 Hypercholesterolemia |
| Metabolic | Fatty liver / hepatic steatosis | 3/13 with fatty liver in immunologic cohort (corvillo2020immunologicalfeaturesof pages 1-2) | Can occur despite overall lower metabolic burden than other lipodystrophies; linked to ectopic fat and insulin resistance when present (corvillo2020immunologicalfeaturesof pages 1-2, hussain2016lipodystrophysyndromes. pages 1-3) | HP:0001397 Hepatic steatosis |
| Metabolic | Low/normal leptin, often less severe leptin deficiency than generalized lipodystrophy | Mild low leptin in 1/13 in Corvillo cohort (corvillo2020immunologicalfeaturesof pages 1-2) | Helps explain why metreleptin may be less effective in APL than in generalized lipodystrophy (oliveira2016barraquer–simonssyndromea pages 2-4) | HP:0012548 Abnormal circulating leptin level |
| Renal | Membranoproliferative glomerulonephritis / C3 glomerulopathy / dense deposit disease | ~20% develop MPGN in review (hussain2016lipodystrophysyndromes. pages 1-3); one third with MPGN in Oliveira overview (oliveira2016barraquer–simonssyndromea pages 1-2); 20–40% MPGN in later review (fossfreitas2025lipodystrophysyndromesone pages 10-11); 20% eventually develop C3G in immunology review (corvillo2020immunologicalfeaturesof pages 1-2); 3/13 had renal diagnoses in Corvillo cohort (DDD, IgA nephropathy, C3-related disease) (corvillo2020immunologicalfeaturesof pages 1-2) | Often occurs years after onset of fat loss; renal disease is the major prognostic determinant and may progress to ESRD (oliveira2016barraquer–simonssyndromea pages 1-2, corvillo2020immunologicalfeaturesof pages 1-2) | HP:0000093 Proteinuria; HP:0000083 Renal insufficiency; HP:0012590 Membranoproliferative glomerulonephritis; HP:0012584 C3 glomerulopathy |
| Renal | Low serum C3 associated with renal risk | Up to 80% with low serum C3 in review (fossfreitas2025lipodystrophysyndromesone pages 10-11); ~69% C3NeF positive and significant C3 reduction in 13-patient cohort (corvillo2020immunologicalfeaturesof pages 1-2) | Persistent hypocomplementemia may parallel disease activity and supports renal surveillance (corvillo2020immunologicalfeaturesof pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2) | HP:0012213 Decreased circulating complement C3 level |
| Ocular | Drusen / retinal deposits | Reported as a complication in DDD/APL overlap; no numerator in the specified evidence set here (ponticelli2023c3glomerulopathiesdense pages 1-2) | May occur in patients with complement-mediated disease, analogous to renal dense deposits (ponticelli2023c3glomerulopathiesdense pages 1-2) | HP:0000608 Retinal drusen |
| Autoimmune | Autoimmune disease association overall | 38.5% (5/13) in Corvillo cohort (corvillo2020immunologicalfeaturesof pages 1-2) | Autoimmune conditions may precede, accompany, or follow lipodystrophy; supports periodic autoimmune review of systems and serology as clinically indicated (corvillo2020immunologicalfeaturesof pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2) | HP:0002960 Autoimmunity |
| Autoimmune | Specific associated autoimmune conditions | Qualitative spectrum includes SLE, dermatomyositis, autoimmune thyroiditis, localized scleroderma, idiopathic thrombocytopenic purpura, Sjögren syndrome (corvillo2020immunologicalfeaturesof pages 1-2) | Association reinforces acquired/immune-mediated etiology in at least a subset of patients (corvillo2020immunologicalfeaturesof pages 1-2, donadille2024diagnosticandreferral pages 4-6) | HP:0002725 Systemic lupus erythematosus; HP:0003541 Dermatomyositis; HP:0000821 Hypothyroidism; HP:0002960 Autoimmunity |
| Diagnostic course / natural history | Childhood onset | Mean onset 8 years in Corvillo cohort (corvillo2020immunologicalfeaturesof pages 1-2); described as during childhood in review/classification texts (hussain2016lipodystrophysyndromes. pages 1-3, oliveira2016barraquer–simonssyndromea pages 1-2) | Insidious onset contributes to delayed diagnosis (donadille2024diagnosticandreferral pages 4-6) | HP:0011463 Childhood onset |
| Diagnostic course / natural history | Delayed recognition/referral | In French rare-disease cohort, APL median age at referral 42.3 years [IQR 28.7–58.8]; overall cohort diagnostic delay 6.4 years and referral delay 15.1 years (donadille2024diagnosticandreferral pages 4-6) | Suggests substantial under-recognition and need for earlier specialist referral (donadille2024diagnosticandreferral pages 4-6) | HP:0034198 Progressive course (disease-level descriptor) |


*Table: This table summarizes the main clinical domains, complication frequencies, and onset/progression patterns reported for acquired partial lipodystrophy/Barraquer–Simons syndrome from the gathered evidence. It is useful for rapid knowledge-base curation and phenotype mapping with suggested HPO terms.*

## 4. Genetic / molecular information
### 4.1 Causal genes
APL/BSS is typically **acquired** and not defined by single-gene causation in the retrieved primary evidence; however, immune-genetic associations have been reported.
* **HLA association signal:** HLA **DRB1*11** was present in 54% of BSS patients in one cohort (with enrichment of *11:03). (corvillo2020immunologicalfeaturesof pages 1-2)

### 4.2 Pathogenic variants
No specific pathogenic germline variants were established as causal for classic acquired APL/BSS in the retrieved evidence.

### 4.3 Molecular pathways and mechanistic causal chain (current concept)
**Alternative complement pathway dysregulation → terminal complement activation → adipocyte injury** is a leading mechanistic chain supported by human tissue evidence.

Key steps supported by retrieved evidence:
1. **C3NeF stabilizes the alternative-pathway C3 convertase (C3bBb)**, preventing normal regulator-mediated decay and increasing C3 consumption and activation. (corvillo2020immunologicalfeaturesof pages 1-2, corvillo2018acquiredpartiallipodystrophy pages 2-4)
2. **Adipose tissue produces complement components**, especially **factor D/adipsin**, which is “a key activator of the AP,” making local adipose complement activation plausible. (corvillo2020evidenceofongoing pages 3-6, corvillo2021complementfactord pages 1-2)
3. In an 11-year-old with active disease, adipose tissue showed: atrophied/dead adipocytes, high extracellular matrix/fibrosis, increased **CD68+ macrophages**, recruitment of **c-Kit+ adipocyte precursors**, plus **local complement deposition** (C3, C5a, C5b-9) in affected tissue but not control tissue—supporting ongoing local complement-mediated injury. (corvillo2020evidenceofongoing pages 3-6)
4. The authors explicitly interpret colocalized **C5a** with macrophage crown-like structures as consistent with chemotaxis and inflammatory perpetuation. (corvillo2020evidenceofongoing pages 3-6)

Direct excerpted statements supporting local complement injury:
* “**C3 was detected…surrounding some adipocytes… C5a stained the CLS macrophages… C5b-9 was found ubiquitously**…” (corvillo2020evidenceofongoing pages 3-6)
* “**This is the first report showing evidence of the activation of the complement system in affected subcutaneous WAT from a patient with BSS**.” (corvillo2020evidenceofongoing pages 3-6)

**Complement factor D/adipsin as a biomarker and potential amplifier**
* In Corvillo et al. 2021, FD was “**significantly elevated**” in BSS versus comparator cohorts and the authors conclude: “**FD could be a reliable diagnostic biomarker…by promoting unrestrained local complement system activation in the adipose tissue environment**.” (corvillo2021complementfactord pages 1-2)

### 4.4 Suggested ontology terms (mechanism annotations)
**GO biological processes (suggested)**
* complement activation, alternative pathway
* regulation of complement activation
* membrane attack complex assembly
* macrophage chemotaxis
* extracellular matrix organization / fibrosis

**Cell Ontology (CL) (suggested)**
* **macrophage** (CD68+)
* **adipocyte**
* **adipose stromal/progenitor cell** (c-Kit+ precursors)

**UBERON anatomical (suggested)**
* subcutaneous adipose tissue of face/neck/upper limb/trunk
* kidney glomerulus
* retina/macula (for drusen)

## 5. Environmental information
No specific toxic, occupational, lifestyle, or infectious agent has been established as causal; however, viral infections are described as preceding onset in some patients. (corvillo2020immunologicalfeaturesof pages 1-2)
Lifestyle factors are relevant for management of metabolic complications but are not established as protective/causal in APL onset. (oliveira2016barraquer–simonssyndromea pages 2-4)

## 6. Mechanism / pathophysiology
### 6.1 Complement-centric pathophysiology (upstream → downstream)
**Upstream drivers:** C3NeF and other complement autoantibodies (anti-C3, anti-properdin, anti-factor B) and reduced complement components (C3/C4/factor B) indicate complement dysregulation. (corvillo2020immunologicalfeaturesof pages 1-2)

**Tissue-level effect:** Local complement deposition and terminal pathway activation (C5b-9) are detected in affected subcutaneous adipose tissue during active disease, along with adipocyte death, macrophage infiltration, and fibrosis. (corvillo2020evidenceofongoing pages 3-6)

**Downstream clinical manifestations:** progressive lipoatrophy; risk of renal complement-mediated glomerular disease (C3G/DDD/MPGN) and occasional ocular drusen in complement-mediated contexts. (corvillo2020immunologicalfeaturesof pages 1-2, ponticelli2023c3glomerulopathiesdense pages 1-2)

## 7. Anatomical structures affected
**Primary**: subcutaneous adipose tissue (face, neck, upper limbs, upper trunk/thorax). (corvillo2020immunologicalfeaturesof pages 1-2, donadille2024diagnosticandreferral pages 4-6)

**Secondary/complications**
* **Kidney:** glomerular disease including MPGN/C3G/DDD. (hussain2016lipodystrophysyndromes. pages 1-3, corvillo2020immunologicalfeaturesof pages 1-2)
* **Liver:** fatty liver/steatosis in a subset. (corvillo2020immunologicalfeaturesof pages 1-2)
* **Eye:** macular drusen in some complement-mediated cases. (ponticelli2023c3glomerulopathiesdense pages 1-2)

## 8. Temporal development
* **Onset:** typically childhood/adolescence (mean onset ~8 years in a cohort; example onset age 12 in review figure caption context). (corvillo2020immunologicalfeaturesof pages 1-2, hussain2016lipodystrophysyndromes. pages 1-3)
* **Course:** gradual progressive fat loss over months/years. (pliszka2025severeinsulinresistance pages 17-18)
* **Care pathway reality (2023–2024 development):** substantial delays—French reference center cohort reports a **median diagnostic delay 6.4 years** and **median referral delay 15.1 years** (whole cohort), while APL patients were referred at median age 42.3 years. (donadille2024diagnosticandreferral pages 4-6)

## 9. Inheritance and population
### 9.1 Epidemiology
Prevalence/incidence estimates were not directly extractable from the retrieved texts; the disease is generally described via **case counts**.
* Multiple sources report **~250 cases** described in the literature. (pliszka2025severeinsulinresistance pages 17-18, oliveira2016barraquer–simonssyndromea pages 1-2)

### 9.2 Population demographics
* **Sex ratio:** female predominance ~3–4× in case-based overviews; ~4:1 in literature and 5.5:1 in one cohort; 90% female in a 33-case French APL group. (corvillo2020immunologicalfeaturesof pages 1-2, donadille2024diagnosticandreferral pages 4-6, oliveira2016barraquer–simonssyndromea pages 1-2)
* **Geography/ancestry:** many reported cases in individuals of European descent (case-based overview). (oliveira2016barraquer–simonssyndromea pages 1-2)

### 9.3 Inheritance
APL/BSS is an **acquired** disorder and usually lacks family history. (corvillo2020immunologicalfeaturesof pages 1-2, corvillo2021complementfactord pages 1-2)

## 10. Diagnostics
### 10.1 Clinical recognition
Diagnosis is primarily clinical based on characteristic fat-loss pattern, supported by complement and renal evaluation. (corvillo2020immunologicalfeaturesof pages 1-2, donadille2024diagnosticandreferral pages 4-6)

### 10.2 Laboratory testing / biomarkers
Key laboratory markers:
* **Complement C3:** often low; persistent low C3 tracked with disease progression in an active pediatric case. (corvillo2020evidenceofongoing pages 3-6)
* **C3 nephritic factor (C3NeF):** frequently present (e.g., 69.2% in one cohort). (corvillo2020immunologicalfeaturesof pages 1-2)
* **Complement factor D/adipsin (FD):** elevated in BSS and proposed as a diagnostic biomarker. (corvillo2021complementfactord pages 1-2)

Example work-up elements reported in a clinical case-based overview include: CBC; renal/liver function tests; urinalysis and urinary albumin excretion; fasting glucose/insulin; HbA1c; OGTT; lipid profile; endocrine testing; and complement testing (C3, C4; C3NeF context). (oliveira2016barraquer–simonssyndromea pages 1-2)

### 10.3 Renal and ocular evaluation
Because renal prognosis is critical, renal screening/monitoring (renal function, urinalysis/albumin; nephrology referral) is emphasized in clinical descriptions and implemented in case management. (jeon2020lipotransferprovideseffective pages 1-2, oliveira2016barraquer–simonssyndromea pages 1-2)

### 10.4 Differential diagnosis
In a rare-disease referral cohort, differential diagnoses (e.g., Cushing syndrome, acromegaly) were explicitly excluded as part of the diagnostic process for lipodystrophy/insulin-resistance presentations. (donadille2024diagnosticandreferral pages 2-4)

## 11. Outcome / prognosis
* Prognosis is strongly influenced by **renal involvement** (MPGN/C3G/DDD), which can progress to ESRD and may require transplantation. (oliveira2016barraquer–simonssyndromea pages 1-2, corvillo2020immunologicalfeaturesof pages 1-2)
* Corvillo et al. note C3G outcomes (general C3G context) include progression to ESRD within 10 years in ~70% of affected children and 30–50% of affected adults. (corvillo2020immunologicalfeaturesof pages 1-2)

## 12. Treatment
Treatment is individualized and typically targets (i) metabolic complications when present and (ii) disfiguring lipoatrophy.

### 12.1 Metabolic management
Conventional approaches include diet/exercise, antihyperglycemics, and lipid-lowering therapy (general lipodystrophy management). (hussain2016lipodystrophysyndromes. pages 1-3, meehan2016metreleptinforinjection pages 1-3)

### 12.2 Metreleptin (leptin replacement)
**Evidence in partial lipodystrophy:** In an expanded-access open-label study of 23 partial lipodystrophy patients, 1-year mean changes were HbA1c −0.88%, fasting glucose −42.0 mg/dL, triglycerides −119.8 mg/dL; common TEAEs included nausea 39.1%, hypoglycemia 26.1%, and UTI 26.1%, with no new immune-related safety signals. (ajluni2016efficacyandsafety pages 1-3)
**Regulatory context:** Metreleptin is FDA-approved for generalized lipodystrophy (not partial), and expert summaries note less predictable efficacy in APL given less marked hypoleptinemia in many cases. (ajluni2016efficacyandsafety pages 1-3, oliveira2016barraquer–simonssyndromea pages 2-4)

**Clinical-trial landscape (recent/active):**
* **NCT06484868** (posted 2024-07-03; recruiting; Phase IV; open-label; n=12) explicitly includes confirmed familial **or acquired** partial lipodystrophy and uses HbA1c and triglyceride responder endpoints. (NCT06484868 chunk 1)
* **NCT05164341** (Phase III RCT; n=69) studies metreleptin in partial lipodystrophy but **explicitly excludes acquired/radiation-induced partial lipodystrophy**, limiting direct applicability to classic APL/BSS. (NCT05164341 chunk 1)

### 12.3 Reconstructive interventions (real-world implementation)
Autologous fat grafting (lipotransfer) is used to restore soft tissue in APL, especially facial lipoatrophy.
* In a BMJ Case Report (published 2020-05), the patient underwent **four procedures over 3 years**, with average injected volume **~23 mL to the face per sitting** and **~19 mL per breast** in breast procedures; follow-up visits were arranged at 3–6 months and no major complications beyond minor donor-site bruising were reported. (jeon2020lipotransferprovideseffective pages 1-2)

A structured treatment table (with MAXO suggestions and key outcomes) is provided below.

| Intervention | Indication/target problem | Evidence type (trial/case report/review) | Key outcomes/stats | Safety notes | MAXO term suggestions | Citation |
|---|---|---|---|---|---|---|
| Diet and exercise / lifestyle modification | Baseline management of insulin resistance, dyslipidemia, hepatic steatosis, overall metabolic burden in APL/partial lipodystrophy | Review / case-based management summary | Recommended as foundational therapy; Oliveira et al. describe hypolipidic diet and regular exercise as part of APL management, especially when metabolic abnormalities are present or to reduce future risk; conventional therapy is often needed because metabolic burden is variable in APL (oliveira2016barraquer–simonssyndromea pages 2-4, hussain2016lipodystrophysyndromes. pages 1-3) | No disease-specific safety signal; effectiveness may be limited in severe metabolic disease | MAXO: dietary modification; exercise recommendation; metabolic disease management | (oliveira2016barraquer–simonssyndromea pages 2-4, hussain2016lipodystrophysyndromes. pages 1-3) |
| Conventional glucose-lowering therapy (e.g., metformin, insulin when needed) | Diabetes / severe insulin resistance in partial lipodystrophy | Review | Standard-of-care approach used before or alongside leptin therapy; partial lipodystrophy may require conventional antihyperglycemics, and severe cases may need high-dose insulin; benefit is supportive rather than disease-modifying (meehan2016metreleptinforinjection pages 1-3, hussain2016lipodystrophysyndromes. pages 1-3) | High insulin requirements may be needed in lipodystrophy; no APL-specific adverse-event profile reported in gathered evidence | MAXO: antihyperglycemic therapy; insulin therapy | (meehan2016metreleptinforinjection pages 1-3, hussain2016lipodystrophysyndromes. pages 1-3) |
| Lipid-lowering therapy (e.g., fibrates/statins/fish oil per standard practice) | Hypertriglyceridemia, dyslipidemia, pancreatitis risk reduction | Review / general management guidance | Used as part of conventional management for lipodystrophy-associated dyslipidemia; important because hypertriglyceridemia occurs in a subset of APL patients and may be difficult to normalize with standard therapy alone (hussain2016lipodystrophysyndromes. pages 1-3, meehan2016metreleptinforinjection pages 1-3) | Routine lipid-lowering drug safety considerations; no APL-specific signal in gathered evidence | MAXO: lipid-lowering therapy; hypertriglyceridemia management | (hussain2016lipodystrophysyndromes. pages 1-3, meehan2016metreleptinforinjection pages 1-3) |
| Thiazolidinediones (e.g., rosiglitazone/pioglitazone) | Insulin resistance and adipose redistribution in partial lipodystrophy | Review / case-based discussion | Reviews note thiazolidinediones have been used with good results in partial lipodystrophy; Oliveira et al. note rosiglitazone may increase fat in some affected areas but can worsen fat accumulation in unaffected areas, so use is individualized (meehan2016metreleptinforinjection pages 1-3, oliveira2016barraquer–simonssyndromea pages 2-4) | Potential to worsen regional fat distribution in APL; standard TZD adverse effects also apply | MAXO: thiazolidinedione therapy; insulin sensitizer therapy | (meehan2016metreleptinforinjection pages 1-3, oliveira2016barraquer–simonssyndromea pages 2-4) |
| Metreleptin in partial lipodystrophy (expanded access; not FDA-approved for PL/APL) | Diabetes, hypertriglyceridemia, leptin deficiency-related metabolic complications in partial lipodystrophy | Open-label expanded-access study (FHA101; NCT00677313) | In 23 PL patients, 1-year mean changes were HbA1c −0.88%, fasting glucose −42.0 mg/dL, triglycerides −119.8 mg/dL; larger effects in those with worse baseline abnormalities. Authors concluded benefits “may extend to patients with partial lipodystrophy,” but evidence remained preliminary (ajluni2016efficacyandsafety pages 1-3) | TEAEs mostly mild/moderate: nausea 39.1%, hypoglycemia 26.1%, urinary tract infections 26.1%; no new immune-related safety signals reported. Regulatory status: FDA approval is for generalized lipodystrophy, not PL/APL (ajluni2016efficacyandsafety pages 1-3) | MAXO: leptin replacement therapy; recombinant hormone therapy; subcutaneous drug administration | (ajluni2016efficacyandsafety pages 1-3) |
| Metreleptin in acquired partial lipoatrophy after transplantation / GVHD | Severe insulin resistance, hyperglycemia, hypertriglyceridemia in acquired partial lipoatrophy | Two case reports | In two adult acquired partial lipoatrophy cases, recombinant methionyl human leptin “reversed all of the metabolic abnormalities”; case 1 included TG 968 mg/dL, HbA1c 8.7%, GIR 2.32 mg/kg/min before therapy, with normalization of HbA1c and triglycerides reported after treatment (shibata2018acquiredpartiallipoatrophy pages 1-3) | Long-term treatment described as successful in these cases; detailed AE table not provided in extracted text | MAXO: leptin replacement therapy; insulin resistance treatment; hypertriglyceridemia treatment | (shibata2018acquiredpartiallipoatrophy pages 1-3) |
| Metreleptin for classic APL/BSS | Metabolic complications in APL/Barraquer–Simons syndrome | Review / expert commentary | Considered less predictably effective in classic APL because leptin levels are often relatively preserved compared with generalized lipodystrophy; Oliveira et al. specifically note lower efficacy in APL than in generalized forms (oliveira2016barraquer–simonssyndromea pages 2-4) | Use remains individualized and off-label in APL; benefit more likely when marked metabolic abnormalities/hypoleptinemia are present | MAXO: leptin replacement therapy | (oliveira2016barraquer–simonssyndromea pages 2-4) |
| Autologous fat grafting (lipotransfer) | Facial and breast lipoatrophy; psychosocial and cosmetic restoration | Single-patient real-world reconstructive case report | Four procedures over 3 years; mean injected volume about 23 mL to face per sitting and about 19 mL per breast in breast procedures. Report described effective soft-tissue replacement and real-world implementation for visible deformity (jeon2020lipotransferprovideseffective pages 1-2) | No major complications reported aside from minor donor-site bruising; follow-up scheduled at 3–6 months after procedures (jeon2020lipotransferprovideseffective pages 1-2) | MAXO: autologous fat grafting; reconstructive surgery; soft tissue augmentation | (jeon2020lipotransferprovideseffective pages 1-2) |
| Facial surgical correction / cosmetic reconstruction broadly | Disfiguring facial lipoatrophy and quality-of-life impact | Case report / review | Oliveira et al. emphasize surgical correction can successfully improve facial lipoatrophy and quality of life in APL, reflecting real-world practice when metabolic disease is absent or mild but deformity is substantial (oliveira2016barraquer–simonssyndromea pages 1-2, oliveira2016barraquer–simonssyndromea pages 2-4) | Standard surgical risks; no disease-specific complication pattern detailed in extracted evidence | MAXO: facial reconstructive surgery; cosmetic surgical procedure | (oliveira2016barraquer–simonssyndromea pages 1-2, oliveira2016barraquer–simonssyndromea pages 2-4) |
| Ongoing trial: metreleptin in partial lipodystrophy (NCT06484868) | Familial or acquired partial lipodystrophy with metabolic endpoints | Ongoing Phase IV open-label post-authorisation study | Recruiting; 24-month, single-group, estimated n=12; includes confirmed familial or acquired partial lipodystrophy. Primary endpoints at Month 12: proportion with ≥0.5% HbA1c reduction (or HbA1c <6.5%) and proportion with ≥30% TG reduction among those with severe baseline abnormalities (NCT06484868 chunk 1) | Safety endpoints include TEAEs, SAEs, deaths, AESIs, and discontinuations; no DMC listed in record (NCT06484868 chunk 1) | MAXO: leptin replacement therapy; clinical trial participation | (NCT06484868 chunk 1) |
| Ongoing trial: randomized metreleptin in PL (NCT05164341) | Partial lipodystrophy metabolic complications | Phase III randomized double-blind placebo-controlled trial | Actual enrollment 69; primary endpoints are change in HbA1c and percent change in fasting triglycerides at Month 6. Important limitation for APL knowledge base: this trial explicitly excludes acquired or radiation-induced partial lipodystrophy, so it does not directly study classic APL/BSS (NCT05164341 chunk 1, NCT05164341 chunk 2) | Quadruple masking; independent DMC; FDA-regulated drug study. Exclusion of acquired APL limits direct applicability to Barraquer–Simons syndrome (NCT05164341 chunk 1, NCT05164341 chunk 2) | MAXO: leptin replacement therapy; randomized controlled trial participation | (NCT05164341 chunk 1, NCT05164341 chunk 2) |


*Table: This table summarizes treatment options and real-world implementations relevant to acquired partial lipodystrophy/Barraquer–Simons syndrome, including metabolic management, metreleptin evidence, reconstructive procedures, and ongoing trials. It is useful for quickly distinguishing what is standard practice, what is off-label or investigational, and which trial data are directly applicable to classic acquired APL.*

## 13. Prevention
No disease-specific primary prevention is established. Secondary/tertiary prevention focuses on: early recognition to reduce diagnostic delay and early screening for renal and metabolic complications. (donadille2024diagnosticandreferral pages 4-6, oliveira2016barraquer–simonssyndromea pages 1-2)

## 14. Other species / natural disease
No naturally occurring APL/BSS analog in other species was identified in the retrieved evidence for this run.

## 15. Model organisms
No dedicated APL/BSS animal model evidence was retrieved in this run. Mechanistic reviews suggest broader experimental work on complement’s terminal cascade effects in adipose tissue (including the concept of complement-induced adipocyte autolysis), but this is not specific to a validated BSS model system in the evidence retrieved here. ()

## Recent developments and latest research (prioritizing 2023–2024)
1. **Rare-disease pathway quantification (2024):** A French national reference-center analysis (2018–2023) quantified diagnostic/referral delays and included 33 APL/BSS patients, highlighting under-recognition and delayed access to specialized care (median referral delay 15.1 years in the overall cohort). (donadille2024diagnosticandreferral pages 4-6)
2. **C3 glomerulopathy link (2023):** A 2023 C3 glomerulopathy review explicitly notes that DDD diagnosis may be preceded or followed by APL/BSS and proposes that fat loss “**may be due to the lysis of adipocytes expressing factor D induced by C3 nephritic factor (C3NeF)**.” (ponticelli2023c3glomerulopathiesdense pages 1-2)
3. **Clinical trial activity (posted 2024):** An open-label Phase IV metreleptin study (NCT06484868) includes both familial and acquired partial lipodystrophy, formalizing real-world evidence collection with metabolic responder endpoints through 24 months. (NCT06484868 chunk 1)

## Notes on citation requirements (PMIDs)
The retrieved full texts in this run provided DOIs and journal metadata but not PMIDs for many citations; therefore, PMID identifiers cannot be reliably asserted from the available evidence without external database lookup.


References

1. (corvillo2020immunologicalfeaturesof pages 1-2): Fernando Corvillo, Giovanni Ceccarini, Pilar Nozal, Silvia Magno, Caterina Pelosini, Sofía Garrido, Alberto López-Lera, Manuela Moraru, Carlos Vilches, Silvia Fornaciari, Sabrina Gabbriellini, Ferruccio Santini, David Araújo-Vilar, and Margarita López-Trascasa. Immunological features of patients affected by barraquer-simons syndrome. Orphanet Journal of Rare Diseases, Jan 2020. URL: https://doi.org/10.1186/s13023-019-1292-1, doi:10.1186/s13023-019-1292-1. This article has 19 citations and is from a peer-reviewed journal.

2. (hussain2016lipodystrophysyndromes. pages 1-3): Iram Hussain and Abhimanyu Garg. Lipodystrophy syndromes. Endocrinology and metabolism clinics of North America, 45 4:783-797, Dec 2016. URL: https://doi.org/10.1016/j.ecl.2016.06.012, doi:10.1016/j.ecl.2016.06.012. This article has 240 citations and is from a peer-reviewed journal.

3. (donadille2024diagnosticandreferral pages 4-6): Bruno Donadille, Sonja Janmaat, Héléna Mosbah, Inès Belalem, Sophie Lamothe, Mariana Nedelcu, Anne-Sophie Jannot, Sophie Christin-Maitre, Bruno Fève, Camille Vatier, and Corinne Vigouroux. Diagnostic and referral pathways in patients with rare lipodystrophy and insulin-resistance syndromes: key milestones assessed from a national reference center. Orphanet Journal of Rare Diseases, 19:1-10, Apr 2024. URL: https://doi.org/10.1186/s13023-024-03173-2, doi:10.1186/s13023-024-03173-2. This article has 9 citations and is from a peer-reviewed journal.

4. (corvillo2021complementfactord pages 1-2): Fernando Corvillo, Laura González-Sánchez, Alberto López-Lera, Emilia Arjona, Giovanni Ceccarini, Ferruccio Santini, David Araújo-Vilar, Rebecca J Brown, Joan Villarroya, Francesc Villarroya, Santiago Rodríguez de Córdoba, Teresa Caballero, Pilar Nozal, and Margarita López-Trascasa. Complement factor d (adipsin) levels are elevated in acquired partial lipodystrophy (barraquer–simons syndrome). International Journal of Molecular Sciences, 22:6608, Jun 2021. URL: https://doi.org/10.3390/ijms22126608, doi:10.3390/ijms22126608. This article has 17 citations.

5. (corvillo2020evidenceofongoing pages 3-6): Fernando Corvillo, Pilar Nozal, Alberto López‐Lera, María P. De Miguel, Juan Alberto Piñero‐Fernández, Raúl De Lucas, María D García‐Concepción, María J. Beato, David Araújo‐Vilar, and Margarita López‐Trascasa. Evidence of ongoing complement activation on adipose tissue from an 11‐year‐old girl with barraquer–simons syndrome. The Journal of Dermatology, 47:1439-1444, Sep 2020. URL: https://doi.org/10.1111/1346-8138.15570, doi:10.1111/1346-8138.15570. This article has 6 citations.

6. (pliszka2025severeinsulinresistance pages 17-18): Monika Pliszka and Leszek Szablewski. Severe insulin resistance syndromes: clinical spectrum and management. International Journal of Molecular Sciences, 26:5669, Jun 2025. URL: https://doi.org/10.3390/ijms26125669, doi:10.3390/ijms26125669. This article has 13 citations.

7. (pliszka2025severeinsulinresistance pages 18-20): Monika Pliszka and Leszek Szablewski. Severe insulin resistance syndromes: clinical spectrum and management. International Journal of Molecular Sciences, 26:5669, Jun 2025. URL: https://doi.org/10.3390/ijms26125669, doi:10.3390/ijms26125669. This article has 13 citations.

8. (fossfreitas2025lipodystrophysyndromesone pages 10-11): Maria Foss-Freitas, Donatella Gilio, and Elif A. Oral. Lipodystrophy syndromes: one name but many diseases highlighting the importance of adipose tissue in metabolism. Current Diabetes Reports, Aug 2025. URL: https://doi.org/10.1007/s11892-025-01602-5, doi:10.1007/s11892-025-01602-5. This article has 5 citations and is from a peer-reviewed journal.

9. (NCT06484868 chunk 1):  Open-label Study to Evaluate Metreleptin in Patients With Partial Lipodystrophy. Amryt Pharma. 2024. ClinicalTrials.gov Identifier: NCT06484868

10. (ceccarini2021autoimmunityinlipodystrophy pages 3-4): Giovanni Ceccarini, Silvia Magno, Donatella Gilio, Caterina Pelosini, and Ferruccio Santini. Autoimmunity in lipodystrophy syndromes. La Presse Médicale, 50:104073, Nov 2021. URL: https://doi.org/10.1016/j.lpm.2021.104073, doi:10.1016/j.lpm.2021.104073. This article has 37 citations.

11. (corvillo2020evidenceofongoing pages 1-3): Fernando Corvillo, Pilar Nozal, Alberto López‐Lera, María P. De Miguel, Juan Alberto Piñero‐Fernández, Raúl De Lucas, María D García‐Concepción, María J. Beato, David Araújo‐Vilar, and Margarita López‐Trascasa. Evidence of ongoing complement activation on adipose tissue from an 11‐year‐old girl with barraquer–simons syndrome. The Journal of Dermatology, 47:1439-1444, Sep 2020. URL: https://doi.org/10.1111/1346-8138.15570, doi:10.1111/1346-8138.15570. This article has 6 citations.

12. (corvillo2021complementfactord pages 2-4): Fernando Corvillo, Laura González-Sánchez, Alberto López-Lera, Emilia Arjona, Giovanni Ceccarini, Ferruccio Santini, David Araújo-Vilar, Rebecca J Brown, Joan Villarroya, Francesc Villarroya, Santiago Rodríguez de Córdoba, Teresa Caballero, Pilar Nozal, and Margarita López-Trascasa. Complement factor d (adipsin) levels are elevated in acquired partial lipodystrophy (barraquer–simons syndrome). International Journal of Molecular Sciences, 22:6608, Jun 2021. URL: https://doi.org/10.3390/ijms22126608, doi:10.3390/ijms22126608. This article has 17 citations.

13. (donadille2024diagnosticandreferral pages 2-4): Bruno Donadille, Sonja Janmaat, Héléna Mosbah, Inès Belalem, Sophie Lamothe, Mariana Nedelcu, Anne-Sophie Jannot, Sophie Christin-Maitre, Bruno Fève, Camille Vatier, and Corinne Vigouroux. Diagnostic and referral pathways in patients with rare lipodystrophy and insulin-resistance syndromes: key milestones assessed from a national reference center. Orphanet Journal of Rare Diseases, 19:1-10, Apr 2024. URL: https://doi.org/10.1186/s13023-024-03173-2, doi:10.1186/s13023-024-03173-2. This article has 9 citations and is from a peer-reviewed journal.

14. (corvillo2018acquiredpartiallipodystrophy pages 2-4): Fernando Corvillo and Margarita López-Trascasa. Acquired partial lipodystrophy and c3 glomerulopathy: dysregulation of the complement system as a common mechanism. Nefrologia, 38:258-266, May 2018. URL: https://doi.org/10.1016/j.nefroe.2018.04.002, doi:10.1016/j.nefroe.2018.04.002. This article has 21 citations and is from a peer-reviewed journal.

15. (oliveira2016barraquer–simonssyndromea pages 1-2): Joana Oliveira, Paula Freitas, Eva Lau, and Davide Carvalho. Barraquer–simons syndrome: a rare form of acquired lipodystrophy. BMC Research Notes, Mar 2016. URL: https://doi.org/10.1186/s13104-016-1975-9, doi:10.1186/s13104-016-1975-9. This article has 32 citations and is from a peer-reviewed journal.

16. (ponticelli2023c3glomerulopathiesdense pages 1-2): Claudio Ponticelli, Marta Calatroni, and Gabriella Moroni. C3 glomerulopathies: dense deposit disease and c3 glomerulonephritis. Frontiers in Medicine, Nov 2023. URL: https://doi.org/10.3389/fmed.2023.1289812, doi:10.3389/fmed.2023.1289812. This article has 19 citations.

17. (jeon2020lipotransferprovideseffective pages 1-2): Faith Hyun Kyung Jeon, Michelle Griffin, Carole Frosdick, and Peter Edward Michael Butler. Lipotransfer provides effective soft tissue replacement for acquired partial lipodystrophy. BMJ Case Reports, 13:e232601, May 2020. URL: https://doi.org/10.1136/bcr-2019-232601, doi:10.1136/bcr-2019-232601. This article has 4 citations and is from a peer-reviewed journal.

18. (oliveira2016barraquer–simonssyndromea pages 2-4): Joana Oliveira, Paula Freitas, Eva Lau, and Davide Carvalho. Barraquer–simons syndrome: a rare form of acquired lipodystrophy. BMC Research Notes, Mar 2016. URL: https://doi.org/10.1186/s13104-016-1975-9, doi:10.1186/s13104-016-1975-9. This article has 32 citations and is from a peer-reviewed journal.

19. (meehan2016metreleptinforinjection pages 1-3): Cristina Adelia Meehan, Elaine Cochran, Andrea Kassai, Rebecca J. Brown, and Phillip Gorden. Metreleptin for injection to treat the complications of leptin deficiency in patients with congenital or acquired generalized lipodystrophy. Expert Review of Clinical Pharmacology, 9:59-68, Jan 2016. URL: https://doi.org/10.1586/17512433.2016.1096772, doi:10.1586/17512433.2016.1096772. This article has 94 citations and is from a peer-reviewed journal.

20. (ajluni2016efficacyandsafety pages 1-3): Nevin Ajluni, M. Dar, John Xu, A. Neidert, and E. Oral. Efficacy and safety of metreleptin in patients with partial lipodystrophy: lessons from an expanded access program. Journal of diabetes & metabolism, Mar 2016. URL: https://doi.org/10.4172/2155-6156.1000659, doi:10.4172/2155-6156.1000659. This article has 62 citations.

21. (NCT05164341 chunk 1):  Study to Evaluate the Safety and Efficacy of Daily Subcutaneous Metreleptin Treatment in Subjects With PL. Amryt Pharma. 2021. ClinicalTrials.gov Identifier: NCT05164341

22. (shibata2018acquiredpartiallipoatrophy pages 1-3): Yusuke Shibata, Atsuko Nakatsuka, Jun Eguchi, Satoshi Miyamoto, Yukari Masuda, Motoharu Awazawa, Akinobu Takaki, Ryuichi Yoshida, Takahito Yagi, and Jun Wada. Acquired partial lipoatrophy as graft-versus-host disease and treatment with metreleptin: two case reports. Journal of Medical Case Reports, Dec 2018. URL: https://doi.org/10.1186/s13256-018-1901-y, doi:10.1186/s13256-018-1901-y. This article has 13 citations and is from a peer-reviewed journal.

23. (NCT05164341 chunk 2):  Study to Evaluate the Safety and Efficacy of Daily Subcutaneous Metreleptin Treatment in Subjects With PL. Amryt Pharma. 2021. ClinicalTrials.gov Identifier: NCT05164341